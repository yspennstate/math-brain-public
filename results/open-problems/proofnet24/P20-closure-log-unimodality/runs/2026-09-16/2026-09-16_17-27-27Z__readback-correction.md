Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime and the exposed scheduler interface provide no model selector and no reasoning-effort selector, so I do not claim GPT-6 or maximum reasoning.

# P20 readback correction — continuity dependency in Section 8

Canonical report corrected by this note:

`proofnet24/P20-closure-log-unimodality/runs/2026-09-16/2026-09-16_17-27-27Z__run-report.md`

creation commit `b933703b69369e169a8f5be13810c955399c2024`, verified blob `df609b653193e5c6a6ba3f519a5c01479524f357`.

## Correction

Section 8 says:

> `AHK regularity gives a continuous density, analytic where it is positive and finite...`

The continuity conclusion used there is correct, but the clean primary theorem to cite for **global continuity on `(0,infinity)` for these compact positive atomless inputs** is H. C. Ji, *Regularity Properties of Free Multiplicative Convolution on the Positive Line*, IMRN 2021, Theorem 3.2 (arXiv:1903.02326), rather than relying on the more recent AHK statement for that exact continuity clause.

Ji Theorem 3.2 states, for nondegenerate probability measures on `R_+`, under the displayed integrability hypotheses and atom condition, that `mu boxtimes nu` is absolutely continuous and its density is continuous on `(0,infinity)`. The theorem's own following remark records that compactly supported measures in `(0,infinity)` satisfy the integrability hypotheses trivially.

The two P20 inputs in the canonical report are absolutely continuous and supported on

`[exp(-130), exp(130)] subset (0,infinity)`.

They are nondegenerate and have no atoms. Hence Ji Theorem 3.2 applies directly and gives the continuity needed in Section 8. The interval certificate separately proves strictly positive density at all twelve derivative-test endpoints, and the subordination/implicit-function argument gives the local differentiability/analyticity used at those endpoints.

Therefore the six compact-interval maximum arguments remain valid exactly as written: on each disjoint interval `[a,b]`, global continuity gives existence of a maximizer, while the certified strict endpoint derivatives exclude both endpoints.

## Status

This is a **source-attribution / proof-dependency correction only**. It changes none of:

- `P20-I0081-ASYM-SIXLEVEL-ADMISSIBLE-07 = PROVED`;
- `P20-I0081-UNEQUAL-PHYSICAL-SYSTEM-07 = PROVED`;
- `P20-I0081-TWELVE-MODE-INTERVAL-07 = PROVED / interval-certified SELF-CHECK`;
- `P20-I0081-TWELVEMODES-07 = PROVED`;
- the tracked metric `8 -> 12`;
- source status `REFUTED`;
- fleet closure status `OPEN, 0/2 qualifying complete OTHER-track audits`.

No historical report was edited.

END OF READBACK CORRECTION
