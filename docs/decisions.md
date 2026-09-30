# Technical decisions and open questions

These are retrospective summaries of reported choices, not contemporaneous decision logs. Motivations beyond the source summary are identified as analytical interpretations.

## Organize observations into maintenance-related cycles

**Reported choice:** segment equipment history around maintenance-related operating periods.

**Interpretation:** repairs can change the relationship between sensor level and asset condition, so a single stationary baseline across all history may be inadequate.

**Tradeoff:** an imperfect event record can create an imperfect cycle boundary. A planned intervention does not necessarily mark a failure or restore the equipment to an identical condition.

**Open question:** how sensitive are features and targets to uncertain cycle boundaries?

## Condition analysis on operating state

**Reported choice:** use rotational speed to distinguish running and idle periods.

**Interpretation:** operating context can explain sensor changes that would otherwise resemble degradation.

**Tradeoff:** a state rule needs to handle transitions and unreliable measurements. The actual state thresholds are not included.

**Open question:** do conclusions persist when transitions and ambiguous states are excluded?

## Combine historical and current-cycle prediction

**Reported choice:** develop cross-cycle, early current-cycle, and adaptively combined regressors.

**Motivation reported:** investigate how different post-maintenance baselines affect transfer between cycles.

**Tradeoff:** adaptation may help with baseline shift but adds another component requiring validation. Current-cycle data cannot reveal late-cycle behavior before it is observed.

**Open question:** does a frozen, causally chosen combination improve held-out near-failure performance over each individual strategy?

## Inspect performance near failure

**Reported action:** examine a late-lifecycle slice after reporting overall performance.

**Observed consequence:** the slice exposed larger error and systematic overprediction.

**Implication:** the important decision region deserves explicit reporting even when it contains fewer observations.

**Open question:** what evaluation unit and error costs best reflect the intended maintenance decision?
