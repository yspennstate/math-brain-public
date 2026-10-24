# FEI source-bound handoff — account03/B17 even-moment repair barrier

Outcome: `CANDIDATE_REFUTED / AUXILIARY_ONLY`. Full uniform-cube FEI remains `OPEN / NOT PROVED`. Execution context: `WITHOUT_VERIFIED_BRAIN`.

Authoritative scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T090815Z-even-moment-repair-barrier/REPORT.md` in `yspennstate/math-open-problems`, report blob `82f2023c96920d67156b21a23a788963b77f1051`. Exact checker blob `be5018df99abfc40b36a48b6cc90cd2ce350deb1`; captured PASS output blob `9c13dd554f3ba4530eacd3eb4fb903abf7b2dc2e`.

Consumed peer artifact: account04/B17 `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T071535Z-quartic-universal-repair/REPORT.md`. It proves universal gate safety of the quartic direction `eta_4(u)=[1-(1-2u)^4]/8`.

New exact adversarial result: for the genuine four-input selector gate with selector bias `3/8`, three unbiased data bits, child positive set `{000,001,010}`, pivotal probabilities `(3/8,9/32,3/32,3/32)`, and output bias `55/64`, the pure even-moment repair

`eta_r(u)=[1-(1-2u)^r]/(2r)`

has gate-defect increment

`2r Delta_r=(23/32)^r-5/32-(3/8)4^{-r}`.

It is positive for `r=2,4` but `Delta_6=-6611525/4294967296<0`; moreover the displayed sequence is strictly decreasing along even `r`, so `Delta_r<0` for every even `r>=6`. Hence the natural independent higher-even-moment extension of the peer quartic theorem is REFUTED on an exact admissible Boolean gate.

For a mixed nonnegative repair `a eta_2+b eta_4+c eta_6`, this witness forces the necessary face

`72,351,744 a + 11,721,216 b >= 1,322,305 c`.

Applied_to_claim: universal quartic safety does not extend independently to all higher even moments. Replacement obligation: return directly to the owner's normalized `c_G` extremality/falsification target; search a genuinely composition-prime arity-five gate at non-dyadic/asymmetric biases, or prove decomposable extremality, while treating only the quadratic/quartic directions as independently universal from the present evidence. Another pure higher-moment sweep is dead.

Next recipient: primary `account04/B17` for repair-cone design; secondary `account03/B18` for all-gate integration. This result removes a proof mechanism but does not itself produce a gate with `c_G` above AND and does not change the target-level FEI status.
