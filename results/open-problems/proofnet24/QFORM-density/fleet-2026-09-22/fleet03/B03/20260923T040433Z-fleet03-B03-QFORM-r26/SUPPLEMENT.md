# r26 scope reconciliation — why the logarithmic theorem is not subsumed by r18

After writing `REPORT.md`, I reread the earlier B03 theorem `QFORM-ISOTROPIC-CROSSBANK-HALF-RIESZ-v1` at `yspennstate/math-open-problems@d18302d55f907552185a42994d48b09f39737cbd` and the fresh fleet01/B03 r22 handoff (`yspennstate/math-open-problems@8fd11b9c3d1abd0cc47e0e861907b6bb3305c30b`). This supplement records the exact scope comparison.

The r18 isotropic theorem assumes

`R=2 U^T T V + b(W)^T U + c(V,W)`,

so the active bank `U` enters **only linearly**: there is no `U^T C U` self block. In the r26 two-physical-coordinate packet

`R=X^T B X + X^T(2MY+beta)+S0(Y)`,

choosing `U=Xj` leaves the physical self term `Bjj Xj^2`. Therefore r18 does not apply when `Bjj!=0`. It does apply in the special zero-diagonal chamber `Bjj=0`, and there it is stronger than r26: it gives a uniform half-Riesz estimate depending only on the aggregate star singular value, with no logarithmic `Delta` loss. Accordingly, r26 should be viewed specifically as an **arbitrary-active-diagonal extension** obtained by combining the random-slope critical estimate with a second-gradient supercritical estimate.

Fresh fleet01/B03 r22 proves directly that if `X` is cap-one and independent of `(L,R0)`, with `p_L<=M`, then

`P(|aX^2+2LX+R0-z|<=eps) <= min(1,4 sqrt(M eps))`

for every real `a`, including nonzero `a`. For the physical aggregate star `L=B12 X_other + m_j^T Y + beta_j/2`, the original-product projection bound gives `M<=sqrt(2)/S_j`. Hence

`4 sqrt(M)=4*2^(1/4) S_j^(-1/2)=2^(9/4)S_j^(-1/2)`,

exactly the `H1` used in r26. Thus the fresh independent worker result validates the critical input and clarifies the novelty: the new step is the exact two-scale layer-cake glue

`H1 eps^(1/2) + H2 eps^(2/3)  ->  H1[4+3 log_+(H2/H1^(4/3))]`

at the half-Riesz endpoint, followed by the whole-copy weighted-time identity.

Consequently the useful proof tree is:

- if an active physical row has zero self coefficient, use r18 and pay no area logarithm;
- if its self coefficient is arbitrary/nonzero and a rank-two physical gradient survives, use r26 and pay only `log(S^2/Delta)` rather than `Delta^(-1/4)`;
- if the second-gradient area vanishes exactly, a separate non-isotropic rank-one/coloop endpoint is still required unless another paid branch applies.

This reconciliation does not change the status: full QFORM and full-target continuity remain open.
