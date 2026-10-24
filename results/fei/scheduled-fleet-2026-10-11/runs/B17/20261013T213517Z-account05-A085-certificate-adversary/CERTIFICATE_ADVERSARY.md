# Stage 2 source-bound verdicts

| Target | Verdict | Scope / consequence |
|---|---|---|
| certlog.py advertised error <2^-46 S for up to 600 terms | ERROR | Allowed Fortran (2,130) input gives certified error >8.0557 while bound <8.0001; complete coefficient vector saved |
| Existing 2^-40 S_computed sign threshold | HOLDS | eta_600=601/(2^53-600)<2^-43; elementary rounding bound proves sign safety on matching <=600-prime integer domain |
| Actual 54-prime four-bit screen | HOLDS | eta_54=55/(2^53-54)<2^-46, independent of layout |
| Exact prime-log fallback | HOLDS | Rational positive remainder, signed endpoints and exact product comparison; undecided fixtures resolved correctly |
| B17 four-bit comparison/orbit logic | HOLDS WITH REPLAY LIMIT | Source logic and all attaining witnesses audited; 64/32/192 orbits generated; A074 equality masks reconciled; no full census rerun |
| B17-KB5-CUTOFF@1 | HOLDS | Five-bit exact Walsh/edge/prime formulas independently reconstructed; K5>107/40>K4 |
| A071 five-bit integer lookup and coverage | HOLDS WITH REPLAY LIMIT | All 289 upper lookup entries checked, int64 bounds proved, 640 orbit generated; prior A071/A082 full-replay artifacts reconcile |
| Extend K5 to all dimensions | FALSE | Existing actual six-bit matching witness has every ratio >368/125>K5; no FEI disproof follows |

The helper-contract witness is not asserted to be a Boolean spectrum. It changes the generic error budget, not any finite mathematical conclusion. '130' means smallest tested prefix in the saved construction, not global minimality. Full proofs, limitations and outputs are in REPORT.md.
