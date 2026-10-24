SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T01:47:17Z.
attacking: bridge ridge leverage to admissible fractional three-volume weights at an intrinsic scale, then optimize and compare both certificates on one explicit rotated indefinite matrix with q=1 volume failure.

# account02/B04 handoff — KL-balanced three-volume versus ridge

Status: `PROVED_SUPPORTING_THEOREMS / EXPLICIT_TARGET_VALID_APPLICATION / FULL_QFORM_OPEN`. Execution remained `WITHOUT_VERIFIED_BRAIN`.

Fresh owner control used before publication: `yspennstate/math-research-brain@fa5b6cb07eb8657bc99baaed2335a375bf15aceb`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only, no applicable stop.

Canonical mathematics: `yspennstate/math-open-problems@061327b7e45c28e5b8c898ed3729456fcea6f7d7`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T014717Z-account02-B04-QFORM-auto11-cont/REPORT.md`; deterministic finite checks and their source are in the same immutable run folder.

## New mathematics

1. `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`. For any probability weights `w` on nonzero physical `3x3` cross minors, with row marginals `alpha_i`, entropy-adjusted volume

`G(w)=exp(E_w log det(M_ST)^2+H(w))`,

if `1<=q<3/2` and `max alpha_i<=q/2`, then

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`.

The proof applies the `e5f71d79...` determinant/entropy AM-GM step and the `c2414ef...` sharp-HY q-calculation at the actual BL inequality. For the squared-minor Gibbs law `w*`, `log G(w)=log E3-KL(w||w*)`; hence marginal repair is paid exactly by KL cost.

2. `QFORM-INTRINSIC-RIDGE-VOLUME-BRIDGE-v1`. If `C=MM^T`, `rho=e3(lambda)/e2(lambda)`, `gamma_a^2=a rho`, and `K_a=C(C+gamma_a^2 I)^(-1)`, then the third-volume marginal matrix `W` satisfies

`W <= (1+a)K_a`.

Thus `alpha_i<=(1+a)(K_a)_ii` and `tr K_a>=3/(1+a)`. For `0<a<1/2`, a ridge leverage cap `max diag K_a<=1/2` automatically makes the same cross block admissible both for the q=1 ridge theorem (`theta>2`) and for fractional volume with `q=1+a`.

3. Explicit rotated target matrix. Starting from the first three normalized H8 columns, rotate two coincident physical rows so the rank-three projection diagonal is `17/32,7/32,3/8 x6`. Put `M=2[.01 I+.99P]` and

`Q_*=(Z+X_1/100)^2+2X^T M Y`.

It has at least six eigenvalues of modulus `>1.9899`. Raw volume sampling fails q=1 because `alpha_max=0.5311251373...`. The globally KL-optimal q=1 tilt is the exponential tilt of that one heavy-row inclusion event, with

`KL_min=0.00194131217...`, `G_opt=63.97170952...`,

and the new weighted theorem gives

`||p_Q*||_inf <=4.0777232167`.

The direct unweighted fractional-q optimum is `4.5176015429` at `q=1.0622502747...`.

On the identical cross block, the completed ridge theorem at `gamma=127/250` has `max diag K=0.4997785303`, `theta=2.8259201813`, and gives

`||p_Q*||_inf <2.9194493068`.

The designated partner account03/B04 theorem at source `48c622953108fd3e77f7b3f5e155e082337804d7` applies to the best local residual pair, whose coefficient is `1.071875`, and gives the actual but weaker inequality

`||p_Q*||_inf <=60.9610584535`.

This comparison is on the same physical target matrix and supports aggregate-before-local-inversion routing.

## Corrections preserved

No law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, conditional projection-density moment, post-rotation independence, or universal good-minor/cross-rank-three assertion was used. The full conjecture is not claimed solved.

## First unpaid implication

`QFORM-KL-BALANCED-VOLUME-OR-RIDGE-ROUTING-v1`: from only `s_3(A)>=1`, obtain a cut with either bounded-KL admissible three-volume at target scale or a target-scale ridge exit; otherwise prove the remaining high-leverage/low-tail state enters an existing grouped-coordinate/hub mechanism before any reciprocal tiny local minor is paid.

Independent review of the two new supporting claims remains pending.
