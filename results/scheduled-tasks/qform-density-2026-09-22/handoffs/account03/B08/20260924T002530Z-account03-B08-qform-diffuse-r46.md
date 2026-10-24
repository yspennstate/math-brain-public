SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T00:25:30Z.
attacking: large physical diagonal twists in the aligned two-bank survivor; exact light-coordinate Schur determinant plus diffuse leverage stability.

# account03/B08 r46 handoff

Full immutable mathematics: `yspennstate/math-open-problems@4e3e8cd533ab1faa782cbb5018bfa5ffb5417df7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T002530Z-account03-B08-qform-diffuse-r46/`.

Final prepublication control refresh: `yspennstate/math-research-brain@0282b435ab3980c0e3bfdf42f526eecdf44aabea`; OWNER CONTROL remains `2026-09-22.15`, QFORM only. Live corrections reread. The newest account01/B15 endpoint correction was also consumed directly: a bare `sqrt(rho)` small-ball certificate plus a square is insufficient; r46 instead uses the stronger completed rank-two translation-uniform half-Riesz theorem.

## New theorem

In the exact aligned physical normal form `A=[[B,M],[M^T,M^T R M + D]]`, let `G=MM^T`, `ell_j=m_j^T G^-1 m_j`, `mu=max ell_j<=1/3`, `a_j=d_j+m_j^T R m_j`. If `d_j!=0`, `a_j!=0`, and `det R!=0`, then after pivoting the ORIGINAL light coordinate `j`:

`det(M_K M_K^T)=det(G)(1-ell_j)`,
`det(R_j)=det(R)d_j/a_j`,

and every remaining normalized arm leverage is at most `mu/(1-mu)<=1/2`. Applying the completed account01/B14 separable rank-two Schur half-Riesz theorem gives

`||p_Q||_inf <= 4 sqrt(2e) [ |a_j d_j| |det R| det(MM^T)(1-ell_j) ]^(-1/4)`.

Writing `Gamma=sqrt(|det R|det(MM^T))`, if `|d_j|>=delta L`, `|a_j|>=alpha L`, `Gamma>=gamma L`, then

`||p_Q||_inf <= 4 sqrt(2e) ((2/3) alpha delta gamma^2)^(-1/4)/L`.

At `alpha=delta/2`, this is `<12.274465 (delta gamma)^(-1/2)/L`.

## Cancellation router

With `K_R=G^(1/2) R G^(1/2)`, if `|a_j|<theta|d_j|`, then

`ell_j >= (1-theta)|d_j|/||K_R||op`.

Moreover, over any set of coordinates satisfying that gate,

`(1-theta) sum |d_j| < ||K_R||_*`.

Thus near-cancellation of large twists forces either actual arm localization or quantitatively large normalized carrier curvature.

## Existing theorem applications

Account01/B19 low-rank paving: since the aligned skeleton has rank at most four, if `s3(A0)>=L/128` and range leverage is at most `1/320`, arbitrary diagonal `D` is already paid continuously by `<2894.213/L`.

Designated partner account04/B08 `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` was applied to the same selected light coordinate: if its deletion child has three eigenvalues `>=L/64` in modulus and its `|lambda|>=L/4096` window leverage is at most `1/32`, then `||p_Q||_inf<4096/L` and `p_Q in C0`.

Regression: `CHECKS.py` / `CHECKS.txt` terminate `QFORM_B08_R46_CHECK_PASS`; 1915 admissible seeded instances, determinant-identity errors below `2.21e-12`, zero leverage-inequality violations.

Full target: OPEN. Global continuity: OPEN. New Schur branch: essential boundedness only.

Next: `QFORM-ALIGNED-CANCELLED-TWIST-HUGECARRIER-OR-CHILDLOCALIZED-v1`: consume zero/tiny `a_j` with large normalized carrier curvature, or the partner-failure child with third-spectral loss/high window leverage; separately handle `det R=0` when the child-window theorem does not pay it.

Execution remains `WITHOUT_VERIFIED_BRAIN`; no task/schedule state, quiet-delivery setting, email/push notification, permission, public-release setting, or paid model/API/Codex setting was changed.
