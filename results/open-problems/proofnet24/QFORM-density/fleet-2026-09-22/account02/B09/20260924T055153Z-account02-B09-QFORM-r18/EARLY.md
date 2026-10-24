SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-24T05:51:53Z.
attacking: the small-pair survivor by retaining one physical hub density inside the mixed-hub Brascamp--Lieb integral, so a hub-heavy source row no longer kills the leverage gate while dense same-side curvature remains exact.

# Early substantive checkpoint

Full QFORM remains OPEN.

First unpaid implication: `QFORM-SMALLPAIR-TO-RETAINED-HUB-FRAME-OR-GROUPEDCROSSING-v1`.

New analytic step (proof completed below in the final report): in pinned Theorem H one need not discard every hub density by `f_h<=1`. If a subset `S` of physical hub densities is retained in the Brascamp--Lieb integral, augment the mixed Gram by the corresponding hub coordinate vectors. With

- `h=|H|`, `d=r+h`;
- mixed rows `rho_i=((v_k)_i;A_{ih}) in R^d`;
- `Gbar=sum_i rho_i rho_i^T + sum_{a in S} e_a e_a^T`;
- leaf leverages `c_i=rho_i^T Gbar^{-1}rho_i <=1/2`;
- retained-hub leverages `b_a=e_a^T Gbar^{-1}e_a`, `B=sum b_a`;
- `alpha=h+r/2-B>1`;

one gets, with all other blocks arbitrary,

`|phi_Q(t)| <= K |t|^{-alpha}`,

`K = [prod_{a in S} b_a^{-b_a/2}] 2^{-h+B}(4pi)^alpha [prod_k |lambda_k|]^{-1/2} det(Gbar)^{-1/2}`.

Hence

`||p_Q||_infinity <= alpha/[pi(alpha-1)] K^{1/alpha}`,

with a continuous density and the same coefficient for interval small-ball probability. This is undecoupled: there is no probability squaring.

Strict-extension example. Let `m=2^k>=8`, let `u,v,w` be flat orthonormal Walsh vectors on a leaf bank `T`, add one leaf `0`, and set

`c=sqrt(3/5)e_0 + sqrt(2/5)u`, `d=v`, `q=w`.

For

`Q=2U<c,Y>+2V<d,Y>+<q,Y>^2`

(and arbitrary additional outside quadratic/cross blocks), the active principal spectrum is `{1,1,1,-1,-1}`. The original pinned-Theorem-H mixed Gram is `I_3`, but row `0` has leverage `3/5>1/2`, so the original gate fails. Retain the physical density of hub `U`. Then

`Gbar=diag(1,2,1)`, `b_U=1/2`, `alpha=2`,

row `0` has augmented leverage `3/10`, and each Walsh-bank row has augmented leverage `11/(5m)<=11/40`. Thus

`|phi_Q(t)| <= 2^(9/4) pi^2 |t|^-2`,

and

`||p_Q||_infinity <= 2^(17/8) = 4.3620309307...`.

This is a literal-source target-valid family beyond the original Theorem-H leverage gate, with dense same-side rank-one curvature retained.
