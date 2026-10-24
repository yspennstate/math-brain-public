SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T21:50:55Z.
attacking: the factorized incident-minor survivor by turning an exact rank-one Schur-minor bank into a product-preserving two-dimensional active channel after the normalized right preconditioner, and isolating why a merely small tail cannot be discarded.

# account03/B06 QFORM r20 — weighted Schur-flag endpoint and the nonperturbative tail barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T215055Z-account03-B06-qform-r20`  
**Assignment:** Curved fiber integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Fresh control before publication:** `yspennstate/math-research-brain@aa4db9cf93e815b7b4663e6980e2d6f98b78a5cb`, OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`.  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not proved by the endpoint below; it gives an `L^3` residual density and, after the genuine outer square, an essentially bounded density.

## 1. Scope and source-valid inputs

The full target remains the arbitrary-dimensional theorem for independent original coordinates with one-dimensional probability densities bounded by one and a real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concave, connected-support, diagonal-basis, or post-rotation-independence assumption is added.

The live corrections are retained: no law-uniform pointwise quadratic-phase decay; no arbitrary-joint rank-three coarea; no positive moment of a worst normalized conditional projection density; no unrestricted spectral-fiber supremum; no X-ray-only indefinite trace bound; and no reciprocal selection of one tiny physical minor.

The current B06 r19 source is

`yspennstate/math-open-problems@f82fe367b06909082f94eda2b98f4a2fd2a5bb7`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T212328Z-account03-B06-qform-r19/REPORT.md`.

In the surviving bicolooop branch, with `g=gamma/16`, the normalized cross matrix is

`Z=H(g^2 I+H^T H)^(-1/2)`,

and for a physical row `j` and physical normalized-column index `r` its incident-minor matrix

`M_ks=det Z[{j,k},{r,s}]`

obeys

`||M||_F^2>1067/2000`.                                             (1.1)

The r19 third-curvature payment already closes the branch if `E_2(M)>=1/4096`. If that payment fails, `M` is within relative Frobenius distance `<0.041455` of rank one. The present run pays the **exact factorized endpoint** of that tube without selecting an individual minor.

The projection input used below is the completed weighted affine-fiber Brascamp--Lieb theorem from account02/B06, already source-pinned in the B06 chain: every `k`-dimensional orthonormal projection of an independent cap-one product measure has density at most `exp(k/2)`. By linear change of variables, if `C` is a full-row-rank `k x m` matrix, then

`||p_(C X)||_infinity <= exp(k/2)/sqrt(det(C C^T)).`             (1.2)

The compatible completed account04 result actually applied is account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its exact dependence-safe kernel inequality is applied in Section 5. The designated `account04/B06` still had no completed current-QFORM canonical handoff at the source refresh; no partner theorem or PASS is fabricated.

## 2. A product-preserving Schur flag

Let `U=(U_0,u)` and `V` be disjoint ORIGINAL-coordinate banks. Their laws are independent, and within each bank the original coordinates are independent with densities at most one. Let `L` be an invertible deterministic linear map on the right bank with

`s_min(L)>=g>0`,                                                     (2.1)

and put `W=L V`. Consider a conditional residual quadratic form

`R=F(U)+2 U^T Z W+G(W)+c_0`,                                       (2.2)

where `F,G` are arbitrary real measurable within-bank phases (in the QFORM application they are quadratic-affine), and partition

`Z=[[alpha,b^T],[c,D]]`, `alpha!=0`.                               (2.3)

Define the physical Schur-minor matrix

`M=alpha D-c b^T`.                                                   (2.4)

The elementary triangular changes within the two banks

`x=U_0+c^T u/alpha`,
`y=W_0+b^T w/alpha`                                                  (2.5)

give the exact cross identity

`U^T Z W=alpha x y+u^T (M/alpha) w`.                                (2.6)

No probability assumption is used in (2.6).

The left change has an important product remnant. Conditional on `u`, `x` is only a translation of the untouched original variable `U_0`; hence its conditional density is at most one. If `p` is any unit vector on the residual left coordinates and `xi=p^T u`, then

`||p_(x,xi)||_infinity <= ||p_xi||_infinity <= sqrt(e)`.             (2.7)

This uses the one-dimensional case of (1.2), not a conditional spectral-density moment.

On the right, let `q` be a unit vector on the residual `W` coordinates and set `eta=q^T w`. The active pair `(y,eta)` is a two-dimensional linear image `A_R W=A_R L V`, where

`A_R=[[1,b^T/alpha],[0,q^T]]`.

Its row Gram determinant is

`det(A_R A_R^T)=1+(||b||^2-(b^Tq)^2)/alpha^2 >=1`.                  (2.8)

From `L L^T>=g^2 I`,

`det(A_R L L^T A_R^T)>=g^4 det(A_R A_R^T)>=g^4`.                    (2.9)

Applying (1.2) with `k=2` therefore yields the dimension-free weighted cap

`boxed( ||p_(y,eta)||_infinity <= e/g^2. )`                         (2.10)

Equations (2.7) and (2.10) are the weighted replacement for a fiber supremum: the full product structure is spent before taking a curved trace.

## 3. Exact factorized incident bank gives an `L^3` residual density

### Theorem 3.1 — `QFORM-WEIGHTED-SCHUR-FLAG-RANK1-ENDPOINT-v1`

Under (2.1)--(2.4), suppose

`rank(M)=1`, and let `m=sigma_1(M)>0`.                               (3.1)

Then `R` has an `L^3` density and

`boxed(
 ||p_R||_3 <= 3^(2/3) e^(1/2) g^(-2/3) m^(-1/3).
)`                                                                   (3.2)

This estimate is independent of `alpha`, the dimensions of the banks, all within-bank quadratic terms, and all translations.

### Proof

Write a singular factorization

`M=m p q^T`

with unit residual vectors `p,q`; signs may be absorbed into one vector. By (2.6), the entire cross interaction is

`alpha x y+(m/alpha) xi eta`,                                       (3.3)

with `xi=p^T u`, `eta=q^T w`. There is **no remaining cross-fiber term** because (3.1) uses all of `M`.

Disintegrate the two independent bank laws over the active variables

`Y=(x,xi)`, `T=(y,eta)`.

All same-bank terms, including those introduced by the triangular changes, remain inside conditional complex amplitudes. Their moduli are bounded by the active marginal densities. From (2.7)--(2.10),

`||p_Y||_infinity<=sqrt(e)`,
`||p_T||_infinity<=e/g^2`.                                          (3.4)

Hence the `L^2` norms of the two complex amplitudes have product at most

`(sqrt(e)*e/g^2)^(1/2)=e^(3/4)/g`.                                 (3.5)

The active bilinear coefficient matrix is diagonal with entries `alpha` and `m/alpha`; the product of its two singular magnitudes is exactly

`|alpha| |m/alpha|=m`.                                               (3.6)

The same two-dimensional mixed-Hessian Plancherel calculation as in the completed B06 exact-rank-two theorem therefore gives, for `t!=0`,

`|phi_R(t)| <= pi e^(3/4) g^(-1) m^(-1/2) |t|^(-1)`.                (3.7)

Together with `|phi_R(t)|<=1`,

`int_R |phi_R(t)|^(3/2) dt
 <=6 pi e^(3/4) g^(-1) m^(-1/2).`                                  (3.8)

Inverse Hausdorff--Young in the standing Fourier convention gives

`||p_R||_3
 <=(2pi)^(-2/3)[6 pi e^(3/4)g^(-1)m^(-1/2)]^(2/3)
 =3^(2/3)e^(1/2)g^(-2/3)m^(-1/3)`,

which is (3.2). QED.

### Why this is not a disguised independence-after-rotation argument

`W=L V` is generally highly dependent coordinatewise. The proof never calls its coordinates independent. The right-hand payment is the density estimate (2.10) for one **linear image of the original product law**. On the left, (2.7) uses the untouched physical coordinate conditionally on the residual original coordinates. Independence is used only where it genuinely survives: between the disjoint left and right original-coordinate banks.

## 4. Application to the normalized B06/B08 exact endpoint

For the live normalization

`Z=H(g^2I+H^T H)^(-1/2)`,

set

`L=(g^2 I+H^T H)^(1/2)`.                                            (4.1)

Then `H=ZL` and `s_min(L)>=g`, exactly the hypothesis of Theorem 3.1. Thus the theorem applies directly to the **actual original quadratic form** after changing only the deterministic coordinates used to describe the right bank; the product provenance is paid through (2.10), not assumed for `W`.

If the r19 incident-minor bank is exactly rank one, (1.1) gives

`m^2=||M||_F^2>1067/2000`,
`m>sqrt(1067/2000)`.                                                 (4.2)

Therefore

`||p_R||_3
 <3^(2/3)e^(1/2)g^(-2/3)(2000/1067)^(1/12)`.                       (4.3)

This closes the exact factorized endpoint of the current physical-minor tube at the residual `L^3` level without selecting any one minor.

## 5. Spend the result through the genuine original-coordinate square

The current B08/B06 setup arose from completing a nonzero ORIGINAL-coordinate scalar pivot with coefficient `a`. The completed account04/B18 proof gives the actual inequality

`p_Q(t)<=|a|^(-1/2) int_0^infinity
 p_R(t-sgn(a)u) u^(-1/2) du`.                                      (5.1)

For a probability density with `||p_R||_3<=M`, Holder on `[0,U]` and mass one on the tail, optimized in `U`, gives the already proved B06 transducer

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <=(8/3^(3/4)) M^(3/4).`                                           (5.2)

Substitute (3.2):

`boxed(
 ||p_Q||_infinity
 <= [8 e^(3/8)/3^(1/4)]
 |a|^(-1/2) g^(-1/2) m^(-1/4).
)`                                                                   (5.3)

With `g=gamma/16` and (4.2),

`boxed(
 rank(M)=1, alpha!=0
 => ||p_Q||_infinity
 <38.269 / sqrt(|a| gamma).
)`                                                                   (5.4)

This is a genuine current-branch payment. It uses the aggregate singular value of the **entire incident-minor bank** and never pays the reciprocal of one physical minor.

## 6. Why the 4.15-percent tail cannot be removed by a small-coefficient perturbation

The r19 survivor is not exactly rank one: it only guarantees

`||M-M_1||_F/sigma_1(M)<0.041455`.

It is tempting to call this tail small and perturb from Theorem 3.1. That implication is false under the owner's quantifiers without additional structure.

### Lemma 6.1 — `QFORM-SMALL-BILINEAR-COEFFICIENT-PERTURBATION-NONUNIFORM-v1`

There is no law-uniform statement saying that a bilinear term with coefficient tending to zero has a vanishing effect on characteristic functions over all independent density-cap-one inputs.

For `epsilon>0`, take independent

`X~Uniform[0,1]`, `U~Uniform[0,1]`,
`Y_epsilon=epsilon^(-1)+U`.

Every density is bounded by one. The bilinear term with coefficient `epsilon` is

`epsilon X Y_epsilon=X+epsilon XU`.                                (6.1)

Hence by dominated convergence,

`E exp(i epsilon X Y_epsilon) -> E exp(iX)=(e^i-1)/i`,              (6.2)

whereas dropping the coefficient-`epsilon` term gives characteristic function `1`. At frequency one the limiting discrepancy is

`|(e^i-1)/i-1|=0.4862647618...>0`.                                 (6.3)

Thus a Hilbert--Schmidt/operator-norm-small quadratic tail cannot be discarded merely because its matrix coefficient is small: admissible input laws may translate or spread on the reciprocal scale. In the quadratic-form convention this example is the off-diagonal symmetric coefficient `A_12=epsilon/2`.

This does **not** refute the QFORM conjecture, nor a stronger nonperturbative stability theorem that uses product structure. It refutes only the naive coefficient-perturbation bridge from the exact endpoint (5.4) to the r19 near-rank-one tube.

## 7. Exact unpaid implication after this run

The current survivor is now sharply localized:

* r19 pays `E_2(M)>=1/4096` by third exterior curvature;
* the complementary bank obeys `||M-M_1||_F/sigma_1(M)<0.041455` and `sigma_1(M)^2>0.532584`;
* **new here:** if that tail is exactly zero and the intersection entry `alpha=Z_jr` is nonzero, the whole branch is paid by (5.4), with the normalized right preconditioner handled without inventing independence;
* Lemma 6.1 shows that the remaining nonzero tail cannot be removed by norm perturbation alone.

Therefore the next precise obligation is

`QFORM-SCHUR-FLAG-NONZERO-TAIL-REGULARIZED-TRANSDUCER-v1`:

prove a mixed exact/regularized product estimate for the Schur-flag representation (2.6) that keeps the leading rank-one channel and handles the orthogonal nonzero tail **inside** the oscillatory/product integral, rather than perturbing it away. The zero-intersection branch `alpha=0` must be handled separately because (2.5) is then unavailable. A valid mechanism may use the tail's regularized determinant or an exact physical-star alternative, but may not use moments, fiber suprema, conditional projection-density moments, or post-rotation independence.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Continuity remains OPEN in this branch.
