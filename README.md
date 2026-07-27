# DD Bible — Transaction DD Copilot

DD Bible is a teaching-first Codex skill for project-specific due diligence planning. It guides beginners through a multi-round planning conversation, explains the purpose and evidence chain behind each diligence requirement, develops risk thinking, and dynamically updates the plan as new facts emerge.

## Core workflow

1. **Planning** — establish the project profile and scope.
2. **Teaching** — explain what each requirement proves and why it matters.
3. **Risk Thinking** — connect facts, risks, evidence, procedures, red flags, and follow-up branches.
4. **Dynamic Update** — revise the scope and risk analysis when new information appears.

The output is organized into:

- complete applicable baseline matters from a general due diligence manual;
- topic-specific business and financial procedures;
- recent industry, business-model, and market-specific regulatory focus.

## Information-security notice

Do not upload or provide state secrets, work secrets, trade secrets, sensitive personal information, or other content that is not authorized for disclosure. Complete sufficient and effective desensitization before using any project material, and comply with your organization's confidentiality and information-security requirements.

## Repository contents

The installable skill is located at `skills/dd-bible/`.

This repository intentionally excludes:

- proprietary due diligence manuals;
- exchange inquiry and response source files;
- client or project data;
- local indexes, logs, caches, and generated search results.

## Knowledge-base configuration

Set `DDBIBLE_KNOWLEDGE_ROOT` to an authorized local knowledge base. If the environment variable is absent, the skill looks for:

`skills/dd-bible/knowledge/`

Expected modules are documented in `skills/dd-bible/references/knowledge-map.md`.

Only use materials that you are authorized and licensed to store, process, and cite.

## Install

Copy `skills/dd-bible/` into your Codex skills directory:

`$CODEX_HOME/skills/dd-bible`

When `CODEX_HOME` is not set, use the default Codex skills directory for your operating system.

Restart or refresh Codex so it discovers the skill, then invoke `$dd-bible`.

## Limitations

This skill supports diligence planning and professional training. It does not replace audit, legal, valuation, regulatory, or investment advice. Source-grounded output requires a separately configured authorized knowledge base.
