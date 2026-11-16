"""Search quality regressions with synthetic, non-client fixtures."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/dd-mentor/scripts/search_knowledge.py'
spec = importlib.util.spec_from_file_location('search', SCRIPT)
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


def record(topic='收入', market='主板', industry='', date='2025-03-01', **overrides):
    fields = dict(company='测试公司', source_title='测试公司主板问询回复',
                  source_file='test.pdf', source_pages='1-2', topic=topic,
                  market=market, industry_name=industry, source_date=date)
    fields.update(overrides)
    return '---\n' + ''.join(f'{k}: {v}\n' for k, v in fields.items()) + '---\n\n' + topic


class SearchTests(unittest.TestCase):
    def test_empty_metadata_cannot_consume_next_field_or_body(self):
        text = record(industry='') + '\nindustry_name: 伪元数据'
        self.assertEqual(search.value(text, 'industry_name'), '')

    def test_no_industry_bonus_for_empty_industry(self):
        text = record()
        self.assertEqual(search.score_record(text, ['收入'], '', '工业', ''),
                         search.score_record(text, ['收入'], '', '', ''))

    def test_preferences_cannot_replace_topic_match(self):
        self.assertEqual(search.score_record(record(topic='环保', industry='工业'), ['收入'], '主板', '工业', ''), 0)

    def test_date_is_not_guessed_from_filename(self):
        self.assertEqual(search.record_date(record(date='', source_file='20260101.pdf')), ('', 'missing'))

    def test_invalid_date_reported(self):
        self.assertEqual(search.record_date(record(date='2025-02-30')), ('', 'invalid:source_date'))

    def test_market_conflict_detected(self):
        self.assertEqual(search.metadata_warnings(record(source_title='测试创业板问询回复')), ['market_title_conflict'])

    def run_search(self, records, *args):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'README.md').write_text('synthetic corpus')
            (root/'review_comments').mkdir()
            for i, text in enumerate(records):
                (root/'review_comments'/f'Q{i}.md').write_text(text)
            proc = subprocess.run([sys.executable, str(SCRIPT), '--root', tmp, '--query', '收入', '--module', 'review', *args], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            return json.loads(proc.stdout)

    def test_strict_market_rejects_other_unknown_and_conflicting(self):
        result = self.run_search([record(), record(market=''), record(market='科创板', source_title='科创板回复'), record(source_title='创业板回复')], '--market', '主板', '--strict-market')
        self.assertEqual(result['total_matches'], 1)
        self.assertEqual(result['regulatory_stats']['excluded_market'], 3)

    def test_inclusive_dates_unknown_and_future_excluded(self):
        result = self.run_search([record(date=d) for d in ['2025-01-01', '2025-12-31', '2026-01-01', '', 'bad']], '--date-from', '2025-01-01', '--date-to', '2025-12-31', '--sort', 'date')
        self.assertEqual([r['source_date'] for r in result['results']], ['2025-12-31', '2025-01-01'])
        self.assertEqual(result['regulatory_stats']['excluded_date'], 3)
        self.assertFalse(result['regulatory_stats']['date_range_complete'])

    def test_truncation_and_missing_citations_visible(self):
        result = self.run_search([record(), record(), record(source_pages='')], '--limit', '1')
        self.assertEqual(result['total_matches'], 2)
        self.assertTrue(result['truncated'])
        self.assertEqual(result['regulatory_stats']['missing_citation'], 1)

    def test_no_hits_not_replaced_by_preference_matches(self):
        result = self.run_search([record(topic='环保')], '--market', '主板')
        self.assertEqual(result['result_count'], 0)
        self.assertEqual(result['regulatory_stats']['no_topic_match'], 1)

    def test_invalid_cli_inputs_rejected(self):
        for args in [['--query', ' '], ['--query', '收入', '--strict-market'], ['--query', '收入', '--date-from', '2026-01-01', '--date-to', '2025-01-01'], ['--query', '收入', '--date-to', '2025-02-30']]:
            with self.subTest(args=args):
                p = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True)
                self.assertEqual(p.returncode, 2)

    def test_scalar_quoted_metadata(self):
        self.assertEqual(search.value(record(company='"测试公司"'), 'company'), '测试公司')


if __name__ == '__main__':
    unittest.main()
