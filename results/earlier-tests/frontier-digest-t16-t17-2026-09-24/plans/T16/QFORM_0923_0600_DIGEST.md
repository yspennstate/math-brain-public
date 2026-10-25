# QFORM: research plan for the next few hours

## Starting point (to audit, not to trust)
Proved in the notes: the separable case (coarea on a same-sign pair, constant pi), rank exactly three with a universal constant (20:45), a localized regime (Prop. 4, 22:27), uniform L^3 bounds for the characteristic function of one squared direction (22:39), and sharpness (one large eigenvalue gives a 1/sqrt(s) singularity, two of opposite sign a log). Corrections: pi is not the general constant (19:54); the Fourier route is viable. Literature: no proof. Outside tools: marginal bounds (a k-dimensional orthogonal projection of a product of densities <=1 has density <=2^{k/2}: Rogozin, Bobkov-Chistyakov, Ball, Livshyts-Paouris-Pivovarov), the definite-core coarea lemma (19:38), Plancherel.

## First concrete step (hour 1)
Read the rank-three theorem and Prop. 4 in full and redo both proofs by hand, checking that the constants are uniform in n, in the ratios lambda_i/lambda_j and in the laws; then write down, as a condition on A, the exact regime neither covers. Everything below extends them. Same hour, a cheap stress test (Monte Carlo, n <= 8, coordinates uniform on unions of short intervals): find the example behind 19:54 and try to iterate or tensor it until the density grows; and test whether two same-sign eigenvalues >=1 already suffice. They do in the separable and rank-two cases; if in general, the third eigenvalue only supplies the sign pair.

## Reductions
(a) Densities <=1 form a convex set whose extreme points are indicators of measure-one sets, and M(Q(X)) is convex in each coordinate's law; by Choquet (after truncation) each X_i may be taken uniform on a set of measure one.
(b) Conditioning on X_{S^c} leaves X_S^T A_SS X_S + <b, X_S> + c. Prove the bound uniformly in the linear term b; the statement becomes hereditary: a definite 2x2 principal block with determinant >= c gives pi/sqrt(c), and a 3x3 principal block with three eigenvalues of modulus >= c gives C/c by the rank-three theorem. Test the strengthening first on small examples with b in ker A.

## Hours 2-3: a decoupling theorem
For disjoint S, T with |S| = |T| = k, condition on the rest; one Cauchy-Schwarz gives |phi_Q(t)|^2 <= E|psi_S(2t A_ST (X_T - X'_T))|, psi_S the characteristic function of X_S. Each X_i - X'_i still has density <=1, so Plancherel on R^S gives

    |phi_Q(t)| <= (pi/|t|)^{k/4} |det A_ST|^{-1/4},   hence   M(Q) <= (k/(k-4)) |det A_ST|^{-1/k}   for k >= 5.

With the marginal bounds the same holds when A_ST has exact rank k. It settles forms with a square off-diagonal block of size >= 5 whose singular values have geometric mean bounded below (generic spread matrices), and explains the threshold: Cauchy-Schwarz halves the decay exponent, hence five, as in the Bentkus-Goetze / Goetze-Zaitsev ellipsoid rates. Write out constants; check numerically.

## Hours 3-5: the crux
Left: spread forms of effective rank three or four, with no good bounded principal block and only three or four off-diagonal singular values that are not small. Here |phi_Q| must decay like |t|^{-3/2} with no loss: no Cauchy-Schwarz. (i) Extend the rank-three proof to rank four, using the L^3 lemma if that proof is Fourier-side. (ii) Handle the remainder in physical space: with Y = (Y_1, Y_2) the definite pair and W = Q - lambda_1 Y_1^2 - lambda_2 Y_2^2, coarea needs only the mixed-norm bound int sup_y rho_{Y,W}(y, w) dw <= C, automatic when Y and W are independent. Proving it for spread directions is the key lemma. Fallback: an inverse route (a density peak forces near-low-rank structure, in the spirit of Kwan-Sauermann), with lattice-like coordinates as the adversaries.

## Avoid
- Conditioning on P^perp X and bounding the sup of the pair's conditional density: for the cube with spread directions the expected sup is of order n (thin sections). Average before taking the sup.
- Pointwise decay of characteristic functions: densities on many short, evenly spaced intervals keep |psi| near 1 at large frequencies; only L^q averages with q >= 2 are uniform.
- Kolmogorov-distance CLT or invariance principles: no control at small scales, and a density <=1 need have no moments.
- Rogozin-type rearrangement to intervals: unjustified for quadratic level sets.
- Aiming for pi.
