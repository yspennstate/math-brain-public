# account01/B17 FEI handoff — partial-branch shared-core witness

Status: `WITHOUT_VERIFIED_BRAIN`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T014112Z-partial-branch-shared-core/REPORT.md`, report blob `317694313bd078634b62d252fe9efa0085afcb14`; verifier commit `1c965a35663f990c6395e3b7df67cd80f2ed5275`; output commit `f4640f26fd6f07c4ca6088bb8b7638f785331110`.

Consumed exact peer inputs: account02/B17 balanced-excess equivalence (blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`), account02/B15 exact shared-core operator and `K(ell^4)` certificate, and account03/B13's completed full-fourfold recurrence tail theorem whose certified `R6` upper endpoint is

`6.5218509495504481848824149770395541197961122790612205924109263953322714`.

New Boolean construction: let `F` be the certified 162-input balanced monotone shared-graft gate with reusable singleton/influence `ell=14593/65536`. Form `h1=F` and recursively form `h_{m+1}` by replacing only the distinguished input of a fresh outer `F` by `h_m`, leaving the other 161 inputs as fresh characters. Exact balanced composition gives

`I(h_{m+1})-1 = (I(F)-1) + ell (I(h_m)-1)`,

`H(h_{m+1}) = H(F) + ell H(h_m)`,

and distinguished singleton `c(h_m)=ell^m`. Hence `H(h_m)/(I(h_m)-1)` is preserved exactly. For `m=4`, `h4` has only 645 variables and distinguished coefficient `ell^4`, so it uses the already-certified positive core correction `K(ell^4)`.

Applying the exact nine-host operator once gives a genuine 5,805-variable balanced monotone Boolean gate `G_*` with

`H(G_*)/(I(G_*)-1) > 6.5218511190811741401649047123074662558509151627606049713533024`.

This exceeds the **entire** account03/B13 `R6` upper endpoint by more than

`1.6953072595528248973526791213605480288369938437894e-7`,

far larger than that old recurrence's certified `<2.833e-30` remaining tail. Thus this is not another round of the exhausted full-fourfold recurrence.

By the consumed balanced equivalence,

`C_FEI > 6.5218511190811741401649047123074662558509151627606049713533024`.

Outcome: `CANDIDATE_REFUTED` for every all-gate potential with center cap at or below the previous full-fourfold `R6` endpoint. This is a lower-bound advance only, not a universal FEI upper bound.

Next exact adversarial target: optimize partial heterogeneous substitution while tracking the pair `(balanced excess ratio, distinguished singleton coefficient)` against the exact shared-core objective. Do not continue the exhausted full-fourfold recurrence unchanged.