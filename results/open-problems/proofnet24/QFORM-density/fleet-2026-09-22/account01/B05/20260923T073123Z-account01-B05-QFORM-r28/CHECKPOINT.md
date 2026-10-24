SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T07:31:23Z.
attacking: uncovered indefinite two-sheet curved integral; condition away genuinely mixed rows only when their spectral Gram operator mass is small, then apply the completed account02/B05 support-separated theorem to the surviving product frame.

# Early substantive checkpoint

Let `A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`, and let physical row `i` have leverage `c=||r_i||^2>1/2`. Rotate only the deterministic 3D active basis so `r_i=sqrt(c)e1`, and write for `j!=i`

`r_j=u_j e1+v_j`,  `v_j in e1^perp`.

Let `H={j!=i: u_j!=0 and v_j!=0}` be the same-coordinate overlap support and

`K_H=sum_(j in H) r_j r_j^T`, `kappa=||K_H||op`.

First calculation: if `kappa<1`, conditioning all `X_H` leaves a frame with exact support separation. Its Gram matrix is

`G=I-K_H=sum_(j notin H) r_j r_j^T`.

Because every unconditioned residual row is now either parallel or orthogonal to `e1`, `G` is block diagonal for `Re1 direct_sum e1^perp`; moreover `G >= (1-kappa)I`.

Whiten only this deterministic frame: `R_tilde=R_U G^(-1/2)` has orthonormal columns and preserves support separation, while the heavy row leverage becomes `c/g11 >= c>1/2`. The conditioned quadratic core is

`R_U Lambda R_U^T = R_tilde M R_tilde^T`,  `M=G^(1/2)Lambda G^(1/2)`,

and

`s_min(M)>=s_min(G)s_min(Lambda)>=1-kappa`.

Therefore, after scaling by `1-kappa`, the completed account02/B05 theorem `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1` applies to the conditioned law. Its proof is stable under arbitrary affine terms: conditioning `X_H` only adds a linear term, and an invertible active matrix lets us complete the square; deterministic translations preserve scalar/pair independence and all density caps. Consequently

`P(Q in J | X_H) <= 248 |J|/(1-kappa)`

for every interval `J`, hence after averaging

`||p_Q||infinity <=248/(1-kappa)`.

In particular, `kappa<=1/2` closes the branch with constant `496`.

Structural consequence: because `G` is block diagonal, so is `K_H`. Its longitudinal block is `sum_H u_j^2 <= ||u||^2=1-c<1/2`. Thus any survivor after the `kappa<=1/2` exit must satisfy

`||sum_(j in H) v_j v_j^T||op >1/2`.

So more than half of some transverse spectral direction is carried by coordinates that have *nonzero* longitudinal contamination. This remains possible even when `sum |u_j|||v_j||` is arbitrarily small, explaining why coefficient-size perturbation is the wrong currency: the remaining obstruction is hard support incidence of infinitesimal overlaps.

To finish this run: audit the affine extension carefully against the partner proof; apply newest Claude Theorem C to the already-paid one-sheet half-line; refresh live corrections; then publish the full theorem and exact remaining implication.
