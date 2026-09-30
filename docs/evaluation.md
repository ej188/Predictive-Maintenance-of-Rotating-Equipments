# Evaluation and limitations

## The finding that matters

The retrospective analysis reported favorable aggregate agreement with the constructed reference target. Further inspection found that the evaluation was dominated by observations farther from failure, while the final part of the lifecycle showed substantially larger error and systematic RUL overprediction.

Exact internal metrics, sample counts, thresholds, and event timelines are withheld. This preserves the methodological finding without publishing company-specific experiment results.

## Why overall error can mislead

For error e_i = prediction_i - reference_i:

```text
MAE  = mean(abs(e_i))
RMSE = sqrt(mean(e_i**2))
bias = mean(e_i)
```

If most rows come from an easier lifecycle region, overall MAE largely reflects that region. More frequent readings from one cycle also give that cycle greater influence. Rows in a time series are correlated; treating every timestamp as an independent sample understates uncertainty.

Positive bias means overprediction of reference RUL. In a maintenance context, this can suggest more time remains than the reference supports. The operational cost is context-dependent and was not quantified in this project.

The [synthetic example](../examples/README.md) illustrates the aggregation issue with invented values.

## Validation needed before an operational claim

| Question | Proposed evaluation | What it resolves |
| --- | --- | --- |
| Can the model predict at a real decision time? | Audit feature availability, baseline selection, target construction, and weight selection | Future-information leakage |
| Does it generalize beyond one history? | Hold out complete cycles and then complete assets; use chronological backtesting | Memorization and domain shift |
| Does it work where intervention matters? | Report errors, bias, and counts by reference horizon and by cycle | Aggregate masking |
| Does an alert help? | Define the alert rule first; measure event-level recall, false-alert burden, missed events, and lead-time distribution | Difference between regression fit and warning usefulness |
| Are results stable? | Compare simple baselines, feature ablations, and uncertainty estimated at the cycle or asset level | Improvement and variability |
| Is the label meaningful? | Review event confidence and sensitivity to plausible target definitions | Proxy-label validity |

The table is a future validation plan. The source summary does not confirm that these experiments were completed.

## Warning lead time

A warning horizon cannot be established from a low regression MAE alone. It requires an alert criterion, an event definition, a rule for persistent alerts, and an evaluation across both failure and non-failure periods. Any initially reported warning lead time requires revalidation and is not a portfolio achievement claim here.

## Model status

| Item | Public account |
| --- | --- |
| Task | Regression against a constructed reference RUL target |
| Model family | Random Forest |
| Inputs | Derived industrial sensor and operating-context features |
| Validation setting | Retrospective; original split details unavailable in the source summary |
| Identified weakness | Degraded performance and overprediction near failure |
| Deployment status | Deployment readiness not established |
| External validity | Broad asset/site generalization not established |
| Access | No weights, training data, or original implementation released |

The responsible outcome was to communicate both the prototype's promise and the limits of the evidence.
