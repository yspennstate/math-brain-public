# r35 supplement — reconciliation with the 14:23 B03 memory and a sharper physical-pivot theorem

After the first r35 report was committed, the worker-owned `LATEST.json` was reread and exposed a prior same-day B03 run that had not been in the prompt transcript:

`yspennstate/math-open-problems@47f5fd760f92c306e2105c2de46bf1859d47f56d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T142318Z-fleet03-B03-QFORM-r35/REPORT.md`.

That run proves the heavy-row pair cap and the endpoint Fresnel-Plancherel estimate for every row leverage `c>2/3`, yielding an `L^2` density and a translation-uniform half-Riesz potential stable as the angular coefficient `h_r` tends to zero. It explicitly stops short of one-copy `L^infinity` for the exact three-direction packet.

The present 16:23 run is therefore **not** duplicating that result: its new theorem closes the one-copy `L^infinity` endpoint at the exact coloop `c=1`. The prior pair-cap coordinates also allow the following additional sharpening of the nonzero physical-pivot branch.

## Theorem S.1 — `QFORM-HEAVY-ROW-SCALAR-SCHUR-HALFRIESZ-v1`

Work in the same exact one-sided packet

`Q=a^(-1)H^2+2 sigma U V`,

with right spectral vectors `v,q` orthonormal and

`h_R=beta v+m q`, `m>0`.

Fix a physical right coordinate `r` with leverage

`c=v_r^2+q_r^2>0`,

and physical square coefficient

`h_r=beta v_r+m q_r !=0`.

Then

`boxed:
 int_R |t|^(-1/2)|phi_R(t)|^2 dt
 <=8 sqrt(pi) L0
   sqrt(|h_r|/(|sigma|m sqrt(c))),
}`

for the exact Schur residual `R` after completing the square in `X_r`, and

`boxed:
 sup_s E|R-s|^(-1/2)
 <=4 sqrt(2) L0
   sqrt(|h_r|/(|sigma|m sqrt(c))).
}`

Consequently

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2) L0
   sqrt(|a|/(|sigma|m sqrt(c)|h_r|)),
 L0=sqrt(e).
}`

This is the same structural scope as the nonzero physical-pivot part of r27, but the exact pair aggregation collapses its rank-two Schur residual to a single scalar product projection and improves the analytic constant from `16sqrt(30)` to `4sqrt(2e)`.

### Proof

Use the pair-cap coordinates from the 14:23 run. Put

`e1=(v_r,q_r)/sqrt(c)`

and choose `e2` orthogonal. On the complement bank define orthogonal product projections `Y,Z` so that

`S=sqrt(c)X_r+sqrt(1-c)Y`.

Write, in the `(e1,e2)` basis,

`V=alpha S+gamma Z`,
`h_R.X_R=w1 S+w2 Z`,

with

`|alpha w2-gamma w1|=m`,
`h_r=sqrt(c)w1`.

Let `H0` denote all terms in `H` outside the right bank. Then

`H=H0+w1[sqrt(c)X_r+sqrt(1-c)Y]+w2Z`.

Complete the square in the **genuine original coordinate** `X_r`. The residual right-bank linear form is

`alpha sqrt(1-c)Y+gamma Z
 -(alpha/w1)[w1 sqrt(1-c)Y+w2Z+H0]`.

The `Y` term cancels exactly. The remaining `Z` coefficient is

`gamma-alpha w2/w1
 =(gamma w1-alpha w2)/w1`,

whose absolute value is

`m/|w1|=m sqrt(c)/|h_r|`.

Thus the Schur residual has the exact form

`R=S0(background)-2 sigma (m sqrt(c)/h_r) U Z`,

up to the harmless orientation sign. Crucially, `Z` is a normalized scalar projection of the complement product bank, so `p_Z<=L0`; it is independent of the left bank containing `U`, and `p_U<=L0`. The narrow complement projection `Y` has disappeared from the residual rather than being assigned a false conditional cap.

Apply the scalar bilinear lemma proved in the main r35 report with selector cap `M_Y=L0`, coefficient cap `M_U=L0`, and

`|b|=|sigma|m sqrt(c)/|h_r|`.

This gives the displayed half-Riesz and weighted independent-copy time estimates. The square in `X_r` has coefficient `h_r^2/a` and `X_r` has density cap one, so the square receiver gives the density bound.

No sum/difference independence, post-rotation independence, or pointwise oscillatory decay is used.

## Relation to the exact-coloop theorem

For `c=1`, Theorem S.1 is the physical-coordinate branch of the main report. It still deteriorates as `h_r->0`. The genuinely new exact-coloop aggregate branch in the main report pivots the **independent complementary scalar projection** instead; that second pivot exists with the required independence only at `c=1`, and it removes the `h_r=0` singularity.

For `2/3<c<1`, the prior 14:23 pair-cap theorem remains stable at `h_r=0` but currently yields only finite-`L^p` and half-Riesz control, whereas Theorem S.1 yields one-copy `L^infinity` when `h_r!=0` with the explicit reciprocal-square-root dependence above. The genuinely unpaid collar is therefore the joint limit

`c->1`, `h_r->0`, with `c<1`,

where the weak complement direction must be retained quantitatively.

`QFORM_B03_R35_SUPPLEMENT_PASS`
