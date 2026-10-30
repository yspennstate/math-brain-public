# B05/A023 — arbitrary shared-core spectral tail

**Run:** 20261019T101236Z-fleet01-B05-shared-core-tail-budget-a023  
**Result:** exact arbitrary-core spectral identities and a tail-only GU transfer proved; full shared-core GU transfer and universal GU remain OPEN.  
**Model / effort:** GPT-6 / UNKNOWN.  
**Endpoint:** 2026-10-21T19:15:57Z, unchanged.  
**Ownership:** B05 primary; A021–A025 retained. No shared indices or schedules changed.

## Candidate and prior bound

The sole target remains one absolute pair a>=0, 0<=b<1 such that every genuine Boolean function on every finite uniform cube satisfies G(f)<=a I(f)+b U(f). The prior local run proved scoped rare-control, point-defect, and one fixed nonfactorizing-core bounds, but not arbitrary shared cores. Review found a coefficient typo in the prior F-series intermediate bound; the rare-gate conclusion survives with the corrected estimate in PRIOR_RUN_CORRECTION.md. The original prior files are preserved.

The source-reviewed implication was reread: universal GU with (a,b) implies U<=a I/(1-b) by restriction induction and H<=(2+2a/(1-b))I by the reviewed granularity theorem. The universal premise remains OPEN.

## New exact result

For arbitrary Boolean q(x,u), fresh controls z disjoint from u but with the gate sharing physical x, let epsilon=2^-r, E={all controls +1}, s_r=1_E+(1-1_E)x, and w=q s_r. Put a=xq and d=q(1-x)=q_-(1-x), where q_-=q|x=-1.

The exact Fourier coefficients are a_hat(R)+epsilon d_hat(R) on control-free labels and epsilon d_hat(R) on every nonempty control label. The marginal spectrum over control subsets is exactly (1-epsilon)p_{xq}+epsilon p_q. The nonempty-control upper cones are epsilon^2 2^(r-|T|) pi_d(R).

The nonempty-control U contribution is
U_tail(w)=r epsilon-2r epsilon^2+(epsilon-epsilon^2)(2U(q_-)+1).
The signed nonempty-control GU contribution is
G_tail(w)=C_r+2r epsilon^2 U(q_-)+2epsilon(1-epsilon)G(q_-),
where C_r=(r+1)epsilon+(2r^2-3r-1)epsilon^2.

The proof is dimension-uniform and retains the changed-core U(q_-) endpoint. Since I(w)>=(r+1)epsilon+I_u(q) and I(q_-)<=2I_u(q), the rare-control constant is paid by physical influence. For r>=2, if q_- satisfies GU with (a,b), the tail obeys
G_tail(w)<=(a+2)I(w)+(b+theta_r)U_tail(w), theta_r=r/(2^r-1)<=2/3.
This is only a tail transfer; it is not the full GU inequality or a depth-stable transfer.

## Exact remaining gap

The full U decomposes as U(w)=U(bar p)+D_r(q), where bar p=(1-epsilon)p_{xq}+epsilon p_q and D_r(q) is an exact signed conditional upper-cone mismatch. It is bounded above by H(T|R), but its physical restriction differences are not controlled by that upper bound. The missing lemma is a uniform bound on the control-free mixture GU contribution plus the signed changes of D_r(q) by A I(w)+b U(w) with b<1. No singleton-potential closure is claimed.

For the corrected A025 example q=x K_n, w=K_n s_r is a disjoint product, so its full GU bound reduces to the rare-gate bound and is independent of majority depth. The arbitrary shared-core head term remains OPEN. The rank-six correction 109/128<1 remains binding; no GU or FEI disproof is claimed.

## Validation and next action

The deterministic checker exhausts 1,104 combinations (all Boolean cores through three variables and gate ranks 1–4). Exact rational Walsh/upper-set arithmetic and float64 logarithms verify the tail identities to displayed precision; the corrected prior D_r bound is checked for ranks 2–20. This is corroboration, not a uniform proof. Full proof, code, actual output, claims, progress, packet delta, source pins, and correction are in this run directory.

Next: bound the signed control-free mixture mismatch and its restriction differences while retaining U(bar p), U(q_-), and terminal U separately. Universal GU and full FEI remain OPEN.