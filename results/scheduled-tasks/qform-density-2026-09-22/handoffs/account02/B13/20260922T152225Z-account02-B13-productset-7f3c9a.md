# account02/B13 handoff — residual Pluecker pair-incidence forcing

Run `20260922T152225Z-account02-B13-productset-7f3c9a`; programme `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. Execution `WITHOUT_VERIFIED_BRAIN`. Full QFORM remains **OPEN / NOT PROVED**.

Canonical mathematics: `yspennstate/math-open-problems@93bed74b07afe996a4aa08eaeb88f35060653134`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T152225Z-account02-B13-productset-7f3c9a/REPORT.md`. Standard-library checker/output are committed in the same directory at `f5912d48e08567cf57cec5fe11a7b074fe6415b7` and `58ea72cdd6479baf1589f9c39b1c99f10a212feb`.

Applied partner in full: account03/B13 `yspennstate/math-open-problems@dd421029601cf5663685c49f225af55567332fb6`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/b13-20260922T143428Z-qform11/REPORT.md`. That theorem forces `d_*->0` and `Delta->0` in any unbounded nested-heavy exact-rank-three sequence and uses the completed disjoint-exterior estimate `||p_Q||_inf <= 12 D0^(-1/6)`.

New exact identities: with partner notation, residual rows `r_k=(a_k,b_k,z_k)`, `B=1-h`, `s=h+rho^2`, `beta=rho^2+h(1-c)`, and `u_k=(sqrt(h)a_k-rho b_k)/sqrt(s)`, define physical pair weights

`p_kl=c(b_k z_l-z_k b_l)^2`, `q_kl=s(u_k z_l-z_k u_l)^2`.

Their masses are `alpha=cB`, `beta`, and coordinate incidences are exactly

`p_k=c(b_k^2+B z_k^2)`, `q_k=s u_k^2+beta z_k^2`.

If `M` is the cross mass of disjoint residual pairs, then

`D0 >= 2M >= 2[alpha beta-sum_k p_k q_k]`,

hence

`D0 >= 2 alpha(beta-2 max q_k)` and `D0 >= 2 beta(alpha-2 max p_k)`.

Also the normalized residual planar vectors `x=b/sqrt(B)` and `y=u/sqrt(beta/s)` satisfy the exact alignment identity

`|<x,y>|^2 = 1-h Delta/(B beta)`.

Consequently any unbounded nested-heavy sequence has a sharper dichotomy. Either `alpha beta->0`, forcing `c->1` or `h->1` (a physical row leverage tends one), or along a subsequence with `alpha beta>=eta>0` there is a **third residual physical row** `k` with `z_k^2->0` and simultaneously

`b_k^2/B >= 1/2-o(1)`, `u_k^2/(beta/s) >= 1/2-o(1)`.

Thus the old residual `(d_*,Delta)->(0,0)` is narrowed to a leverage-one boundary or a three-planar-heavy plus diffuse-transverse geometry. The identities use physical original-coordinate Pluecker weights and do not assume interval extremality, bounded fragment count, support diameter, or post-rotation independence.

First unpaid implication: `QFORM-RANK3-THREE-HEAVY-DIFFUSE-TRANSVERSE-v1` — aggregate the final diffuse transverse bank before conditioning while retaining the three concentrated physical coordinates, or construct a genuine product-indicator counterexample. Arbitrary extra spectrum remains separately open.
