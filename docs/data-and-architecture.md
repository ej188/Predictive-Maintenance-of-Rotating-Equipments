# Data and architecture

## Reported implementation

The project used Python and a cloud data warehouse to integrate industrial sensor readings with enterprise maintenance records. Measurements covered vibration, temperature, rotational speed, and acceleration. Preparation included resampling irregular readings, handling missing values, and aligning sensor trends with maintenance events.

The pipeline supported analytical development. This account does not assert scheduled production orchestration, streaming inference, a feature store, service-level guarantees, or a deployed monitoring system.

## Sources of uncertainty

| Issue identified during the project | Analytical consequence | Validation question |
| --- | --- | --- |
| Extended telemetry gaps | Apparent continuity can conceal unobserved degradation | Which windows contain enough actual observations to support a feature? |
| Uneven sampling | Dense periods can dominate analysis; resampling changes what is measured | How sensitive are results to cadence and aggregation? |
| Incomplete or ambiguous maintenance records | A repair record may not locate failure onset or restore a healthy state | Which events support a target, and which require uncertainty or exclusion? |
| Running and idle periods | Shutdown behavior can differ from operating degradation | Are comparisons conditioned on operating state? |
| Post-maintenance baseline changes | A prior cycle may not represent the current cycle | Does a model transfer across changed operating conditions? |

## A generic data contract for future replication

The following is a proposed contract, not an internal schema:

| Record | Minimum generic fields | Checks |
| --- | --- | --- |
| Telemetry | anonymized asset key, observation time, measurement family, value, unit, quality flag | timestamp convention, duplicates, unit consistency, gaps |
| Maintenance event | anonymized asset key, event interval, event category, event-confidence flag | ambiguous timing, overlaps, distinction between inspection and repair |
| Derived feature row | asset key, cycle key, prediction time, observed-history coverage, features | history available at prediction time, cycle boundaries, missingness |
| Evaluation row | cycle key, prediction time, reference target, prediction, target-confidence flag | split membership, target provenance, horizon membership |

Avoid treating an imputed value as an observation. Keep coverage and imputation indicators alongside derived features. A missing sensor interval provides no direct evidence that equipment was healthy.

## Time alignment and information availability

For a prediction at time t, features should use observations available at or before t. Future repairs may define retrospective labels but must not enter the feature computation, normalization, cycle selection, or adaptive weighting available to the predictor at t.

A defensible implementation distinguishes event occurrence, event recording, and ingestion time. The internship summary identifies timestamp synchronization as an improvement priority; it does not verify a complete availability-time audit.

## Reproducibility boundary

Actual timestamps, asset keys, warehouse objects, connection details, site information, and event records are excluded. The conceptual flow and contract explain the engineering approach without providing access to internal systems.
