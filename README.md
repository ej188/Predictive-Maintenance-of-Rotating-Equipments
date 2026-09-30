# Predictive Maintenance of Rotating Equipments

### An anonymized internship proof of concept in equipment-health analysis and RUL modeling

An internship project connecting industrial telemetry and maintenance history to study equipment degradation and build a remaining-useful-life (RUL) regression prototype.

**My contribution:** I carried the proof of concept from asset selection and data integration through operating-cycle analysis, feature engineering, modeling, and retrospective evaluation. I presented it to the company's C-suite and global reliability and maintenance leaders.

**The central lesson:** agreement with a constructed RUL reference target does not establish reliable failure prediction. Evaluating the period closest to failure exposed weaknesses that overall metrics concealed.

This is an independently written, anonymized portfolio account based on my internship summary. It contains no company datasets, source code, model artifacts, maintenance records, internal slides, or operational identifiers. The implementation and results cannot be independently reproduced from this repository. The optional synthetic example is a new educational artifact created for this portfolio, separate from the internship implementation.

## Work at a glance

| Area | What I contributed | Why it mattered |
| --- | --- | --- |
| Problem definition | Selected a maintenance-relevant asset and framed an equipment-reliability use case | Connected model development to a practical engineering question |
| Data engineering | Built a Python and cloud-warehouse pipeline joining sensor readings with enterprise maintenance records | Created a shared analytical view of equipment behavior and maintenance history |
| Time-series analysis | Resampled irregular telemetry, handled missingness, separated running and idle periods, and organized maintenance-related cycles | Made operating context explicit before modeling |
| Feature engineering | Developed baseline comparisons, a sensor-derived health index, rolling statistics, trends, and operating-state features | Translated raw measurements into indicators of asset condition |
| Machine learning | Developed Random Forest RUL regression with cross-cycle, current-cycle, and combined prediction strategies | Explored how historical experience and local operating behavior could complement each other |
| Evaluation | Examined overall and near-failure errors, target validity, and systematic overprediction | Identified limitations relevant to maintenance decisions |
| Communication | Presented the proof of concept to C-suite and global reliability and maintenance leaders; recommended stronger records, timestamp alignment, and broader validation | Explained technical findings and validation priorities to senior decision-makers |
| Applied LLM work | Refined classification prompts for a separate enterprise message-filtering workflow | Applied prompt engineering to an operational use case |

## Start here

- [Project narrative and ownership](docs/project-overview.md): problem, contributions, and outcomes.
- [Data and architecture](docs/data-and-architecture.md): data preparation, provenance, and operating context.
- [Modeling approach](docs/methodology.md): features, reference targets, and prediction strategies.
- [Evaluation and limitations](docs/evaluation.md): the distinction between retrospective fit and decision usefulness.
- [Technical decisions](docs/decisions.md): observed choices, tradeoffs, and questions still open.
- [Skills and evidence](docs/skills-and-evidence.md): where to inspect my reasoning for applied science and engineering roles.
- [LLM contribution](docs/llm-workflow.md): scope of the secondary project.
- [Confidentiality and provenance](docs/disclosure.md): publication boundaries and claim status.

## Conceptual workflow

1. Integrate telemetry and maintenance history; check time alignment and data quality.
2. Identify operating states and maintenance-related cycles.
3. Compare against a healthy reference and construct temporal features.
4. Develop complementary RUL regression strategies.
5. Examine overall and near-failure performance; communicate engineering findings and validation priorities.

This summarizes the work at a general level. Using only information available at prediction time is a required validation principle; the source summary does not verify that every original feature met it.

## Achievements and boundaries

I delivered an integrated analytical foundation, identified a promising vibration-based degradation indicator, developed a complementary set of regression strategies, and communicated limitations and data-improvement priorities. Retrospective results showed that performance weakened near failure, including overprediction of the reference RUL.

This account makes no claim of production deployment, verified warning lead time, reduced downtime, cost savings, or measured improvement from the LLM contribution. Internal numerical results and event details are intentionally omitted. The project is best understood as a prototype and an exercise in evidence-driven evaluation.

## A small, reproducible evaluation example

The [synthetic example](examples/README.md) demonstrates why overall MAE can obscure errors in the final part of a lifecycle. It uses invented values and Python's standard library; it does not train a model or reproduce company results.

```bash
python3 examples/evaluation_slices.py
```

Check the public documentation's local links and prohibited artifact types:

```bash
python3 scripts/check_repository.py
```

## Repository map

```text
README.md
docs/                    Technical narrative, evaluation, evidence, and disclosure
examples/                Clearly labeled synthetic educational example
scripts/                 Documentation and artifact checks
.github/                 Review template
CONTRIBUTING.md           Rules for safe, evidence-backed changes
SECURITY.md               Handling accidental disclosure
.gitignore               Exclusions for private and generated artifacts
```

## Documentation conventions

The structure adapts a few public conventions: a clear README entry point and discoverable examples from the [OpenAI Cookbook](https://github.com/openai/openai-cookbook); topic-oriented navigation and contributor guidance from [Anthropic's Claude Cookbooks](https://github.com/anthropics/claude-cookbooks); and separate documentation from [Google DeepMind's WeatherNext repository](https://github.com/google-deepmind/weathernext). This portfolio is independently authored and has no affiliation with or endorsement from those organizations.

No open-source license has been selected. This repository does not grant rights to any employer-owned material.
