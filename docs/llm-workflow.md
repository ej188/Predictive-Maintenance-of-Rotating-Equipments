# LLM classification contribution

## Reported scope

Alongside the predictive-maintenance project, I developed and refined LLM classification prompts for an enterprise sales-workflow automation effort. The task supported identifying and filtering irrelevant messages.

No original prompts, message contents, categories, mailbox details, customer information, system architecture, or model/provider configuration are included. The summary supplies no measured improvement, deployment evidence, or independent evaluation of this contribution.

## What would make a future classification evaluation defensible

The following is a proposed plan rather than a claim of completed work:

1. Define relevance categories, ambiguous cases, and the cost of incorrectly filtering a useful message.
2. Create an approved, representative labeled evaluation set; keep a held-out set separate from prompt iteration.
3. Version prompts and record changes so improvements can be attributed to a specific revision.
4. Report per-class precision and recall alongside the confusion matrix, coverage, and human-review burden.
5. Test instruction-like content inside messages as untrusted input and define an abstention or review route for uncertainty.
6. Verify that privacy constraints are respected before sending any enterprise text to a model endpoint.

This contribution demonstrates applied prompt-development experience. It does not establish an agentic system, a production LLM platform, or a quantified automation outcome.
