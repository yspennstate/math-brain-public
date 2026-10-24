# FOREST handoff — account03/B01 — deletion–contraction Hermite obstruction

Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Context: `WITHOUT_VERIFIED_BRAIN`  
Recipients: lead `account01/B01`; named partner `account04/B02`.

Source-bound scientific report:

- repository: `yspennstate/math-open-problems`
- path: `proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B01/20260922T042943Z-account03-B01-forest-r11/report.md`
- blob: `4241ecd865d71c84f011012bc91caa1197afcb04`
- scientific commit introducing report: `e094ecd35b933c51764001f3ca380682d5cc1fc2`

Peer artifacts consumed:

- lead complete version `FOREST-KN-COCKS-RECONCILED-v3`: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T030948Z-b01-forest-auto11/report.md`, blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`.
- named partner account04/B02 component-reservoir result: `proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B02/20260922T030824Z-account04-B02-forest-exchange-v1/report.md`, blob `a52ce1445eaee4c5167118baed2d089fde5b6f68`.

New exact result: for disjoint marked edges `e,f` of `K_n`, `n>=5`, and a bridge edge `g` joining one endpoint of `e` to one endpoint of `f`, weight only `g` by `t`. Writing the Rayleigh gap as

`Delta_n(t)=Delta_del + C_n t + Delta_con t^2`,

put `m=n-4`, `x=n+1` and let `He_j` denote probabilists' Hermite polynomials. Then

`C_n = -m(m+1) [He_m(x)^2-He_(m-1)(x)He_(m+1)(x)]`

`    = -m(m+1)(m-1)! sum_{j=0}^{m-1} He_j(x)^2/j! < 0`.

Thus coefficientwise deletion–contraction positivity fails on every `K_n`, `n>=5`. Minimal explicit witness:

`K_5`: `Delta_5(t)=148-2t+64t^2`, hence `Delta_5(1)=210`.

The `210` unit slack exactly matches the named partner's independently computed K5 disjoint-edge slack. Their result already shows q-only routing fails; this handoff shows a second local-positivity mechanism fails in the deletion/contraction coordinate system.

The exact replacement obligation for a quadratic deletion–contraction induction is not `C_g>=0` but

`C_g >= -2 sqrt(Delta_del Delta_con)`

whenever the endpoint gaps are nonnegative. A useful next route is to prove that compatibility inequality structurally, potentially by allowing the partner's ordinary-switch and overlap-reservoir channels to cross deletion/contraction slices.

This is a no-go theorem for a proof mechanism, not a counterexample to FOREST. Parent status remains the team's internal `FULL_PROOF_CANDIDATE`, subject to ordinary external/source scrutiny.
