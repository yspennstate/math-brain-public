from pathlib import Path
p=Path('ATTEMPT.md')
p.write_text(p.read_text(encoding='utf8')+r'''
## 8. A sharper a.e.-Hessian criterion (proved conditional reduction)

This replaces the need for an open quadratic-patch cover. Let S be the set of points x!=0 where U(x)>0, U is twice differentiable in the pointwise Taylor-expansion sense, and D^2U(x) belongs to Gamma_3^+. Suppose almost every point of R^2 is either in S or has limiting mean height s(x) equal to 0 or 3. Then all four height-frequency fields converge weak-*; consequently the requested fractions converge on every ball. At x in S their limiting frequencies are f_j(D^2U(x)), the canonical-pattern frequencies; at mean-0 or mean-3 points they are respectively the unit vectors at 0 or at 3.

All membership and coverage assumptions in this statement are hypotheses, NOT established facts about the point-source limit. The relevant matrices in Gamma_3^+ are the countable isolated maximal matrices with canonical patterns from LPS/Pegden–Smart, so the frequency function on S is measurable. Equivalently the conclusion's measurability follows from the weak-* subsequential limit identified below.

Proof. Extend the indicator 1_{s_n=j} constantly over lattice squares of side 1/N, N=sqrt(n). These functions take values in [0,1]. From any subsequence, extract a further subsequence for which the four indicators converge weak-* locally to g_j, using Banach–Alaoglu, separability of L^1 on bounded sets, and a diagonal exhaustion by balls. Then g_j>=0, sum_j g_j=1, and sum_j j g_j=s almost everywhere. The last equality follows from the supplied weak-* convergence of s_n and the exact pointwise linear identity. At points where s=0 or 3, nonnegativity and these two equations force the asserted unit vectors.

It remains to identify g_j almost everywhere in S. Fix x in S which is a Lebesgue point of each of the four g_j; this excludes only a null set. Write A=D^2U(x). For any sufficiently small rho, the closed ball B_{2rho}(x) lies away from 0 and in {U>0}. Twice differentiability gives a quadratic Taylor polynomial Q_x with Hessian A and

sup_{|y-x|<=2rho}|U(y)-Q_x(y)| <= e(rho) rho^2,

where e(rho)->0. At scale N, compare u_n on the lattice ball of radius R=N rho centered at a nearest lattice point to Nx to the polynomial N^2 Q_x(y/N). Uniform odometer convergence gives an error e(rho) R^2+o_rho(N^2); the subscript emphasizes that rho is fixed while n tends to infinity. Center rounding introduces O_rho(N) errors, absorbed in o_rho(N^2). After subtracting the integer q with Delta q=1, the Taylor Hessian is A-E in Gamma_2^+. Lemma 13 and Proposition 8 fit its affine part by a translated canonical witness with additional O_A(R+1) error, exactly as in section 5. Local recurrence follows from the least-action lemma, since the ball is inside a positive-U region.

Fix r_A large enough for Theorem 10 and to contain an a-period square window for this pattern together with its nearest neighbors. Choose h so that

h>=C_A, h^2>=e(rho)R^2+o_rho(N^2)+O_A(R+1),

and h/R has limsup at most sqrt(e(rho)); one may add N^(1/4) to h to satisfy the lower-bound hypotheses. For rho sufficiently small, C_10 r_A sqrt(e(rho))<1/2. The hypotheses R>=C_10 h r_A and h r_A>=C_10|V_A|^3 then hold for large n, increasing the negligible N^(1/4) term if necessary. Theorem 10 bounds the bad fraction by C_A r_A h/R. The fixed outer annulus and the window-boundary error are O_A(r_A/R), which tends to zero. The translated-period window argument of section 3 therefore implies

limsup_{n->infinity} | average_{B_rho(x)} 1_{s_n=j} - f_j(A) |
 <= C_A sqrt(e(rho)).

Here average over lattice points and average over lattice-square extensions differ by o(1) for each fixed rho: only cells meeting the sphere contribute, their total area is O(rho/N+N^(-2)), and the fields are bounded. Along the extracted subsequence the average converges to the average of g_j on the ball because its indicator is an L^1 test. Thus

| average_{B_rho(x)} g_j - f_j(A) | <= C_A sqrt(e(rho)).

Let rho tend to zero. The Lebesgue differentiation theorem and e(rho)->0 give g_j(x)=f_j(A). This identifies every subsequential limit with the same four densities almost everywhere under the stated coverage assumption. If the original sequence failed weak-* convergence against some compactly supported L^1 test, a subsequence with discrepancy bounded below would have a convergent further subsequence, contradicting this uniqueness. Exhaustion and boundedness extend the conclusion to arbitrary L^1 tests. Taking indicators of balls and dividing by their area proves all ball-frequency limits. The sphere-cell comparison above converts these integral averages back to site fractions.

Precise new bottleneck. It suffices to prove that, at almost every point with intermediate mean height 0<s(x)<3, U(x)>0 and its second-order Taylor Hessian belongs to Gamma_3^+. The known viscosity constraint D^2U in partial Gamma_3 is weaker. This reduction is not a proof of that missing isolated-maximal-Hessian assertion. The square identity question still requires a separate analysis of the zero equivalence class with its own boundary problem; this theorem does not identify that limit.

## 9. Consequence of the ellipse theorem (proved special case, using literature)

For a positive-definite A in the admissible Gamma_3^+ class of Melchionna's Theorem 4.3, let E_A={x: x^T A x/2<1} and let e_{A,k} be the recurrent identity on sqrt(k) E_A intersect Z^2 with the exterior wired to a sink. For every ball B, the fractions among the sites in sqrt(k)(B intersect E_A) tend to the periodic frequencies f_{A,j}, provided |B intersect E_A|>0. Extending the identity by zero outside the ellipse instead gives the ball fraction

(|B intersect E_A| f_{A,j} + |B\E_A| 1_{j=0})/|B|.

Proof. Take r fixed large enough to exceed both 3|V_A|^3 and a full-period square-window radius plus one. Theorem 4.3, printed/PDF p. 13, states that the fraction of non-r-good sites in the radius-r inner ellipse is O_A(r k^(-1/4)). Equality of odometers in Br implies equality of height patterns in B_{r-1}, since computing a Laplacian uses one extra nearest-neighbor layer. The ellipse boundary layer has O_A(r sqrt(k)+r^2)=o(k) sites, using its smooth perimeter and elementary lattice-square covering. Hence the bad centers in the whole ellipse are o(k). Restricting to any fixed B intersect E_A retains that bound. This intersection is Jordan measurable, since its boundary is contained in a circle and an ellipse, both null curves. Apply the window averaging proof of section 3 at scale N=sqrt(k), first on inner compact Jordan sets and then exclude a small boundary strip, or directly bound fixed-window shifts by the smooth boundaries. The outside-zero contribution follows by Jordan lattice counting. No claim is made for arbitrary ellipses or square identities.
''',encoding='utf8')
