# Central near-coloop receiver with a physical independent square component

Status at 2026-09-23 20:37 UTC: scoped theorem proved; the full QFORM conjecture remains open.

Source and read-back: [math-open-problems commit 06480f5, full theorem and proof](https://github.com/yspennstate/math-open-problems/blob/06480f5486450bc5b4230280ecbd5ae89a687d88/proofnet24/QFORM-density/interactive/20260923T203741Z-independent-v-square-product-band/REPORT.md). Standard sharp product-marginal input: [Livshyts–Paouris–Pivovarov, arXiv:1507.07949](https://arxiv.org/abs/1507.07949), theorem 1.1.

For physical H independent cap one, and genuine orthonormal original-product leaf forms L,V,P, let \(Q=2HL+\beta L^2+V^2+2\epsilon LP\). If the original leaves include a set T with \(\ell_T=p_T=0\) and \(\rho=\|v_T\|_2>0\), then, for all real beta and epsilon,
\[
\operatorname*{ess,sup}_{|s|\le1}p_Q(s)\le(12+3\sqrt2)/\rho.
\]
The supports of L,P can overlap arbitrarily and V can share their sources outside T. With V itself in an independent bank, rho=1.

Mechanism: \(U=H+\beta L/2+\epsilon P\) has a joint (L,U) density at most \(p_L\le\sqrt2\) and marginal U density at most one, despite any L–P dependence. For \(|c|\le1,0<t\le1\),
\[
\Pr\{c<2LU<c+t\}\le 2Kt+2t+2Kt\log(1/t),\quad K=\sqrt2.
\]
An independent square component Z of V contributes conditional density at most \((\sqrt2/\rho)y^{-1/2}\); its half-power singularity integrates against the \(t\log(1/t)\) product band, giving the displayed bound uniformly beta and epsilon.

Exact gap: when every V-support coordinate also appears in L or P, rho=0 and there is no independent square component to condition on. Neither an arbitrary capped joint law for (L,V,P) nor arbitrary conditional independence can replace the original-product hypothesis. This result is not an original-product high-density counterexample and does not finish the full conjecture.
