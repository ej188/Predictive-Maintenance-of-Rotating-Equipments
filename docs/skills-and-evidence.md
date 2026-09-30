# Skills and evidence

This map helps a reviewer inspect the substance of the work. It describes demonstrated project activities rather than declaring proficiency levels or experience in every target role.

| Capability | Evidence in the internship account | Where to inspect | Limit |
| --- | --- | --- | --- |
| Applied problem framing | Selected an equipment-reliability use case and asset | [Overview](project-overview.md) | Business impact not measured |
| Data engineering | Integrated telemetry and maintenance records using Python and a cloud warehouse | [Architecture](data-and-architecture.md) | Original pipeline and runtime benchmarks unavailable |
| Time-series reasoning | Resampling, missingness, operating states, and maintenance-related cycles | [Architecture](data-and-architecture.md) | Specific preprocessing rules unavailable |
| Feature engineering | Rolling statistics, trends, baseline comparisons, and health-index construction | [Methodology](methodology.md) | Exact formulas and window settings unavailable |
| Applied machine learning | Random Forest regression and complementary prediction strategies | [Methodology](methodology.md) | Reproducible training experiments unavailable |
| Statistical judgment | Identified imbalance across RUL regions and near-failure overprediction | [Evaluation](evaluation.md) | Formal uncertainty estimates not reported |
| Mathematical communication | Explains error decomposition, temporal features, and mixture reasoning | [Methodology](methodology.md), [example](../examples/README.md) | Explanations are newly authored; they do not prove novel mathematical research |
| Decision science | Connected prediction errors to maintenance relevance and evidence limits | [Evaluation](evaluation.md) | No decision-cost optimization or causal impact study reported |
| Applied LLM work | Refined enterprise classification prompts | [LLM contribution](llm-workflow.md) | No quantified prompt evaluation supplied |
| Stakeholder communication | Presented findings and data-improvement recommendations | [Overview](project-overview.md) | Internal presentation excluded |

## How to read this portfolio for different roles

- **Data scientist, applied scientist, ML scientist, statistical modeling:** focus on target construction, lifecycle slicing, transfer across cycles, and validation limits.
- **ML engineer, AI engineer, forward deployed engineer:** focus on turning an operational problem into a prototype and explaining the missing steps between retrospective modeling and deployment.
- **Data engineer:** focus on event alignment, data quality, operating context, and the proposed data contract.
- **Quantitative analyst:** inspect temporal reasoning, error aggregation, and the distinction between a proxy target and an observed outcome. This work does not demonstrate financial-market modeling or trading research.

## Interview discussion prompts

What makes a maintenance event a valid label? How can hindsight enter a healthy baseline? Why can overall MAE disagree with event-level usefulness? When should a current-cycle model outweigh a historical model? What evidence would justify an operational warning claim?

These questions invite discussion of reasoning without requiring disclosure of private systems or results.
