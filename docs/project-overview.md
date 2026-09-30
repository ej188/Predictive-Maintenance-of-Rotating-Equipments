# Project overview

## Problem

Maintenance teams need to interpret changing equipment behavior alongside repair history. Telemetry can suggest degradation, but noisy measurements, shutdowns, incomplete records, and changes after maintenance make a simple trend insufficient for a defensible prediction.

My internship developed an AI predictive-maintenance proof of concept connecting these sources and estimating a reference remaining useful life. The intended business use was earlier investigation and better maintenance planning. The project did not establish that the estimates could safely drive maintenance decisions.

## My scope

I selected a business-relevant asset, integrated telemetry with maintenance history, prepared time-series data, reconstructed maintenance-related operating cycles, compared sensor behavior against healthy reference periods, engineered features, built Random Forest regression strategies, and evaluated retrospective performance. I presented the proof of concept to the company's C-suite and global reliability and maintenance leaders. I worked with management and reliability-engineering guidance; the account does not imply sole ownership of the company's systems or domain knowledge.

## Outcomes

1. **An integrated analytical foundation.** Sensor history and maintenance events became usable together for degradation analysis.
2. **A candidate degradation signal.** Vibration showed a pronounced departure from the selected healthy reference. The finding motivated investigation; it did not prove a universal precursor or causal mechanism.
3. **A forecasting prototype.** Cross-cycle learning, early current-cycle learning, and an adaptive combination provided complementary modeling strategies.
4. **An evaluation finding with practical consequences.** Aggregate error concealed substantial weakness close to failure. Overestimating remaining life in that region undermines maintenance usefulness even when overall fit appears favorable.
5. **An actionable path forward.** Recommendations focused on work-order quality, synchronization of event and sensor timestamps, and validation across more equipment histories.

## Working style illustrated

I connected the modeling question to an engineering need, examined the data before fitting a model, accounted for operating context, investigated the meaning of the prediction target, and communicated limitations alongside results. This repository presents those reasoning steps without relying on proprietary artifacts.

## Evidence limits

The sources for this account are my supplied internship summary and clarification about the proof-of-concept presentation audience. No original code, notebooks, event records, or experiment logs were reviewed to prepare this version. Contributions are self-reported and cannot be audited from the public repository. Details absent from those sources—including split implementation, exact feature windows, hyperparameters, weighting rules, and confidence intervals—are not asserted here.
