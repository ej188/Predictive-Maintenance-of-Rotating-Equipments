# Modeling methodology

## What was developed

The reported approach segmented history into maintenance-related operating cycles, used rotational speed to separate running from idle periods, established a healthy-operation reference, and compared pre-failure behavior against that reference. A sensor-derived health index and a constructed RUL reference target supported modeling. Multiscale features included rolling statistics, trends, and operating-state information.

Random Forest regression was used for RUL estimation. The source summary does not supply the health-index formula, target-construction algorithm, exact window sizes, hyperparameters, or weighting function. The mathematical expressions below explain general concepts, not a recovered implementation.

## Baseline comparison

For a measurement x and a nonzero healthy-reference mean mu, a general relative deviation is:

```text
relative_deviation(t) = (x(t) - mu) / mu
```

Its interpretation depends on the reference period, units, operating state, and variability. A large departure is a signal to investigate rather than proof of failure. Near-zero reference means make this ratio unstable; standardized deviations or robust location-and-scale comparisons may be preferable in a future implementation.

Baseline periods must be selected using a rule that can be applied without hindsight if the comparison is to support prospective prediction. Choosing a reference because a future outcome is known can overstate usefulness.

## Temporal features

A trailing average at time t over window W is generally:

```text
mean_W(t) = mean{x(s) : t-W < s <= t}
```

Other candidate summaries include variation, extrema, rates of change, and differences from an operating-state baseline. Multiscale windows can describe both short fluctuations and sustained changes. Window coverage matters: the same mean computed from a few observations and from a complete history has different reliability.

These expressions clarify feature reasoning. They do not establish which statistics or window lengths were used in the original code.

## Three reported prediction strategies

| Strategy | Information source | Motivation | Main concern |
| --- | --- | --- | --- |
| A: cross-cycle | Other operating cycles | Use historical degradation behavior | Transfer may fail when baselines or repair effects differ |
| B: current-cycle | Early observations from the current cycle | Adapt to local behavior | Early data may contain little evidence about late-cycle behavior |
| C: combined | Adaptive weighting of A and B | Balance historical information and local adaptation | Weights must be selected without future target information |

A general mixture can be expressed as:

```text
prediction_C(t) = w(t) * prediction_A(t) + (1-w(t)) * prediction_B(t)
0 <= w(t) <= 1
```

This expression illustrates a two-predictor mixture. The original adaptive rule is not disclosed or independently verified.

## Target validity

A reference RUL target is a modeling label, not a direct observation of the equipment's true remaining lifetime. If the target depends on a health index also represented in the features, a model can learn that construction without learning physical failure behavior. If it uses a recorded event endpoint, the endpoint must be interpreted: inspection, planned repair, and failure are not interchangeable outcomes.

Unobserved failures, incomplete cycles, and planned interventions create additional label ambiguity. A later extension could treat incomplete histories as censored observations in a survival-analysis formulation; survival modeling was not reported as internship work.

## Proposed next experiments

Compare the regression strategies with simple baselines, isolate the contribution of each feature family, test across held-out cycles and assets, and examine how target uncertainty changes conclusions. These are proposed validation steps rather than completed results.
