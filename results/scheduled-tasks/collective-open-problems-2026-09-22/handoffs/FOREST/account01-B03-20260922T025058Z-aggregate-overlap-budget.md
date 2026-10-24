# FOREST handoff — account01/B03 — aggregate overlap budget

Status: **ESSENTIAL_STEP_APPLIED**. Parent target remains OPEN. Context: `WITHOUT_VERIFIED_BRAIN`.

Consumed lead `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, and named OTHER-account partner result account02/B01 run `B01-20260922T021602Z-forest-r12`, report blob `59fb19252eaa411eb1d321035e40721a15c6477f`. The partner pays the contraction endpoint `D_1(g)>=0` in a minimal simple counterexample; the new estimate below is independently valid whenever the endpoint/sign hypotheses hold.

With `H` uniform over all forests of `G-{e,f}`, `X,Y` the individual addability indicators, `Q=XY-S`, `q=E Q`, and a hypothetical deficit `delta=Cov(X,Y)-q>0`, define for each third edge `g`

`a_g=-Cov(X,T_g)`, `b_g=-Cov(Y,T_g)`, `v_g=Var(T_g)`,

`h_g=(1-p_g)D_0(g)+p_gD_1(g)>=0`, `Hsum=sum h_g`, and `k=|E(G-{e,f})|`.

Exact conditioning gives

`a_g b_g/v_g = delta+h_g`.

A new one-sided Bessel lemma uses pairwise NC of the third-edge indicators: for any `A` with `-Cov(A,T_g)>=0`,

`sum_g Cov(A,T_g)^2/v_g <= Var(A)`.

Applying it to `X+alpha Y` for all `alpha>0` yields

`2 sum_g a_g b_g/v_g <= Cov(X,Y)+sqrt(Var(X)Var(Y))`.

Hence the exact aggregate reconnection/overlap budget is

**`(2k-1)delta + 2 Hsum <= q + sqrt(Var(X)Var(Y))`.**

This keeps disconnected forests and adjacent marked edges, and uses no sectorwise connectivity-Rayleigh assertion.

A tempting universal closure `Hsum>=q` is false. Exact source-law witness: vertices `{0,1,2,3,4,5}`, edges `{03,04,12,13,15,23,25,34,35,45}`, marks `e=03,f=12`. For `G0=G-{e,f}`:

`N=162`, `q=1/81`, `delta=-2/2187`, while all eight endpoint gaps are nonnegative and `Hsum=211/17496 < 216/17496=q`.

Thus the next switching lemma must use the **violation hypothesis and/or unique-cycle geometry on Q**, not an unconditional one-for-one charge of overlap states into endpoint minor gaps.

Full immutable proof/attempt report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B03/20260922T025058Z-b03-forest-r11/attempt_report.md`, blob `2839352b0f8023e7b21123d72e58885c3d88b94a`.
