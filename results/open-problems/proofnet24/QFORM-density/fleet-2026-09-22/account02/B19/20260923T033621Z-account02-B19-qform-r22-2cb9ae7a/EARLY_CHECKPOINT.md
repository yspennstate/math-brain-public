# account02/B19 early substantive checkpoint — leverage-free E2 quarter-Riesz currency

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

This checkpoint records the first substantive calculation of the run before the synthesis is expanded. It uses only original-coordinate product structure.

## Candidate supporting theorem

Let `U,V` be disjoint original-coordinate banks, with all coordinates independent and one-dimensional densities bounded by one. Let

`R=F(U)+2 U^T M V+G(V)`

where `F,G` are arbitrary measurable real functions finite almost surely, and let

`Z2=e_2(M^T M)>0`.

The general `D_k` decoupling/Brascamp--Lieb estimate in Claude's source package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

may be run with determinant order `k=2` and Jensen exponent `q=2`. The row-marginal gate is automatic because every order-two inclusion marginal is at most one, exactly `q/2`. The resulting characteristic-function envelope is

`|phi_R(t)| <= min(1, B2 |t|^(-1/2))`,

with

`B2=e^(1/4) 2^(1/4) pi^(1/2) Z2^(-1/8)`.

The same source's fractional-potential lemma, at `alpha=1/4`, gives

`H_(1/4)(R):=sup_s E|R-s|^(-1/4)
 <=16 c_(1/4) B2^(1/2)
 =C2 Z2^(-1/16)`,

where

`c_(1/4)=2^(3/4) Gamma(3/8)/(2 sqrt(pi) Gamma(1/8))`

and

`C2=16 c_(1/4)e^(1/8)2^(1/8)pi^(1/4)=3.9291317704... <3.930.`

This is leverage-free and retains all extra cross singular values and arbitrary same-bank curvature. It is weaker than an `L^infinity` theorem but is exactly strong enough for a physical zero-diagonal hyperbolic peel.

## Immediate target-level splice

If a parent form has an ORIGINAL physical pair `i,j` with

`A_ii=A_jj=0`, `A_ij=mu!=0`,

and its exact two-coordinate Schur residual contains a disjoint physical cross block `M` with `e_2(M^T M)>=zeta`, then Claude's completed coordinate-hyperbola peel gives

`||p_Q||_infinity
 <=2^(3/4) kappa |mu|^(-3/4) H_(1/4)(R)
 <5.318 |mu|^(-3/4) zeta^(-1/16)`,

where `kappa=sup_(y>0) log(1+y)/sqrt(y)=0.8047...`.

At the current O0 residual threshold `zeta=1/48`, this becomes

`||p_Q||_infinity <6.774 |mu|^(-3/4)`.

The calculation is source-coordinate safe: no spectral rotation is used probabilistically and no small matrix tail is discarded.

This is only an early checkpoint. The final report will place it into the current no-pivot proof graph, consume the designated account03/B19 partner at an actual inequality, and state the first still-unpaid structural gate.
