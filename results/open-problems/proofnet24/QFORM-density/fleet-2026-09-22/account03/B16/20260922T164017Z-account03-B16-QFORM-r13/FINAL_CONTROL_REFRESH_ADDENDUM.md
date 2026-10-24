# account03/B16 final control-refresh addendum

**Run:** `20260922T164017Z-account03-B16-QFORM-r13`  
**Final fresh main observed before finish:** `yspennstate/math-research-brain@c9283f9ffd32cdc340c22ce4a7625213c2e3797f`  
**Final OWNER CONTROL revision:** `2026-09-22.8`  
**Status:** main scientific results remain valid; full QFORM remains open.

## 1. Later owner revision and newest correction

After the main report and the rank-two independent review were written, the live OWNER CONTROL advanced from revision `2026-09-22.7` to `2026-09-22.8`. The sole target remains QFORM. The new owner message proposes, as a high-value route, conditioning on all remaining spectral coordinates and seeking a universal cap on the **normalized conditional three-dimensional projection density** of three selected large directions.

A newer source-valid correction, account02/B07 event `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1` at brain commit `20e26983d6246b9fa0d18c770275c765e23827d4`, refutes precisely that intermediate claim. Its explicit target-valid example uses independent `Uniform[0,1]` inputs and an orthogonal spectral basis

`r1=(e1+e4)/sqrt(2), r2=e2, r3=e3, r4=(e1-e4)/sqrt(2)`.

Conditioning on `Y4=v`, the conditional density cap of `(Y1,Y2,Y3)` is

`1/(sqrt(2)-2|v|)`,

which diverges as `|v|` approaches `1/sqrt(2)` through conditioning values of positive probability. Therefore the proposed normalized-conditional-projection sublemma cannot be used in the full proof.

This is a correction to the proposed route, **not** a counterexample to the QFORM conjecture.

## 2. Why this run's results survive the correction

`QFORM-ZEROPAIR-CUBIC-BANK-CLOSURE-v1` never assumes a normalized conditional spectral-density cap. It conditions only on the original coordinates outside one physical pair, where the two surviving coordinates remain genuinely independent with their original density caps. The dependence on the conditioned variables enters solely through translations, and the product envelope is uniform over those translations. The rank-one bank `L` is paid through its **unconditional** original-coordinate projection density cap.

Likewise, the independently reviewed `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` preserves original-coordinate product provenance: its heavy branch conditions on one original coordinate complement, and its diffuse branch uses Brascamp–Lieb/Hausdorff–Young before any spectral conditional normalization. Thus the new conditional-3D correction does not invalidate the review verdict.

## 3. Updated next implication

The next projection-product step should **not** seek a universal normalized conditional 3-D spectral density. The target-relevant replacement is:

`QFORM-WEIGHTED-OUTER-PIVOT-FUSION-v1`: combine the reviewed nonzero-outer-pivot rank-two affine half-Riesz theorem with the zero/near-zero outer-pivot product-bank mechanism in a way that keeps the unnormalized/product fiber weight until after the curved quadratic payment. The estimate must remain finite as the outer physical diagonal tends to zero and must avoid a pointwise conditional projection-density supremum.

A separate debt remains stability under arbitrary additional spectral components.

**Full QFORM conjecture: OPEN / NOT PROVED.** Essential boundedness is proved only in the scoped branches recorded in this run. Continuity remains unproved here.
