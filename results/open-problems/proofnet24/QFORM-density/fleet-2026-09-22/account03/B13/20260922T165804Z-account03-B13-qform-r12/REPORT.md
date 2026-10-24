# account03/B13 — null-pair product smoothing and the exact-rank-three light-cone endpoint

**Run:** `20260922T165804Z-account03-B13-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / LOCAL-DEGENERACY-CLOSED / EXACT-RANK3-ENDPOINT-CLOSED / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains **OPEN / NOT PROVED**. This run attacks the simultaneous-zero-physical-pivot/light-cone endpoint left by the preceding B13 run. The main new result is a support-free density estimate for a physical hyperbolic pair plus one independent square. It works with arbitrary fragmented one-dimensional laws and arbitrary outside coordinates. In exact rank three it closes the simultaneous-null endpoint of the previous nested-heavy collar with an explicit constant `<27.649` when the spectral-row wedge mass is at least `1/4`.

A continuous representative is **not proved** here; the results establish absolute continuity and an essentially bounded density.

## 1. Fresh control, corrections, and sources actually used

Fresh control was resolved from `yspennstate/math-research-brain` main and refreshed before publication. The final prepublication snapshot was

`yspennstate/math-research-brain@9ac01bffe18c04113ed63a0b7800d50ce96210ad`,

whose OWNER CONTROL revision is `2026-09-22.8`. The sole target remains the full quadratic-form bounded-density conjecture; there is no later pause/stop for this slot.

The live corrections consumed include the failures of law-uniform pointwise quadratic phase decay, unrestricted fiber-sup integration, conditional-cap-for-independence substitution, a universal good-small-minor/cross-rank-three dichotomy, bounded-diameter localization, fixed fragment count, and direct Pluecker-weighted reciprocal-pivot averaging. None is used as a positive premise.

The designated `account04/B13` current-QFORM artifact remained absent both in the shared handoff tree and at the canonical math-open-problems B13 path at the prepublication check, so no partner result is fabricated or awaited. Compatible completed peer mathematics actually applied is:

1. **Exact product bang-bang reduction**, account02/B13, source snapshot  
   `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.  
   For every fixed slab kernel, the supremum over product densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over unit-measure product indicators. This is applied in Section 6.

2. **Weak-L2 logarithmic-ridge theorem**, account03/B16, read at math-open-problems snapshot `c301be6b21f382934962aeb4c019b713377eac2f`, path  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/B16-20260922T135620Z-r11/REPORT.md`.  
   With
   `Psi(u)=1+log(1/|u|)` for `0<|u|<=1` and `Psi(u)=|u|^(-1/4)` for `|u|>=1`, it proves
   `||Psi(a+z^2)||_{L^{2,infinity}(dz)}<=sqrt(15)` uniformly in `a`; scaling a coefficient `delta>0` costs `delta^(-1/4)`.

3. **Weighted affine-fiber Brascamp--Lieb theorem**, account02/B06, read at the same snapshot, path  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.  
   In the one-dimensional case, every normalized original-coordinate aggregate `Z=sum a_k X_k`, `sum a_k^2=1`, has a density cap at most `sqrt(e)`. This is applied in the exact-rank-three aggregate endpoint in Section 5.

## 2. A sharp-enough support-free envelope for a product

Let `U,V` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Put `P=UV`.

### Lemma 2.1 — `QFORM-PRODUCT-ASINH-ENVELOPE-v1`

For almost every `z!=0`,

`p_P(z) <= 4 asinh( 1/(2 sqrt(|z|)) ) <= 2 Psi(z)`.

The same statement holds after arbitrary deterministic translations of `U` and `V`.

### Proof

It suffices to treat one sign branch. Suppose `z>0` and `x>0`. With `x=e^t`, the positive-positive contribution is

`L = integral_R f(e^t) g(z e^{-t}) dt`.

Set `H(t)=f(e^t)g(z e^{-t})`. Then `0<=H<=1`, and

`A:=integral e^t H(t)dt <=1`,

because `H<=f(e^t)`, while

`B:=integral e^{-t}H(t)dt <=1/z`,

because after `y=z e^{-t}` the integral is at most `z^{-1} int_0^infinity g(y)dy`.

Translate `H` in `t`; this keeps its mass `L` and the product `AB` fixed. Choose the translation so the new exponential moments are equal. Then both equal `sqrt(AB)`, hence

`sqrt(AB)= integral cosh(t) H_shift(t)dt`.

Among all `0<=H<=1` of mass `L`, the integral against the even increasing function `cosh(t)` is minimized by the centered interval `1_{[-L/2,L/2]}`. Therefore

`sqrt(AB) >= 2 sinh(L/2)`.

Since `AB<=1/z`,

`L <= 2 asinh(1/(2sqrt(z)))`.

There are at most two sign branches for a fixed nonzero product (`++` and `--` when `z>0`, or `+-` and `-+` when `z<0`), so

`p_P(z)<=4 asinh(1/(2sqrt(|z|)))`.

For `0<u<=1`,

`asinh(1/(2sqrt(u)))
 = log((1+sqrt(1+4u))/(2sqrt(u)))
 <= log(phi)+(1/2)log(1/u)`,

where `phi=(1+sqrt5)/2` and `4log(phi)<2`. Hence the first bound is at most `2[1+log(1/u)]=2Psi(u)`. For `u>=1`, `asinh x<=x` gives

`4 asinh(1/(2sqrt(u))) <=2u^{-1/2}<=2u^{-1/4}=2Psi(u)`.

Translations preserve the density caps and masses, so the same proof applies. QED.

A scaled form used below is therefore

`p_{2b(U+u_0)(V+v_0)}(y)
 <= |b|^{-1} Psi(y/(2|b|))`                                            (2.1)

for every `b!=0`, uniformly in `u_0,v_0`.

This estimate is deliberately logarithmically singular at the hyperbolic critical value. The next independent coordinate pays that singularity in weak `L^2`; no false pointwise bounded-density claim for an indefinite rank-two form is made.

## 3. New arbitrary-ambient local theorem: two null physical diagonals

Let `A` be any real symmetric ambient matrix, with no restriction on additional eigenvalues. Select three **original independent coordinates** and suppose their physical principal block is

`B = [[0,b,c],[b,0,d],[c,d,gamma]]`,                                  (3.1)

with `b!=0` and `det B!=0`.

### Theorem 3.1 — `QFORM-NULLPAIR-PLUS-SQUARE-v1`

For arbitrary independent one-dimensional input laws of density at most one,

`||p_{X^T A X}||_infinity
 <= 2^(5/4) sqrt(15) ( |b| |det B| )^(-1/4).`                         (3.2)

Numerically the prefactor is

`2^(5/4)sqrt(15)=9.211558703193814...`.

The theorem permits arbitrary outside quadratic coefficients and arbitrary cross couplings to the three selected coordinates.

### Proof

Condition on every original coordinate outside the selected triple. Outside couplings become deterministic affine terms in the three remaining variables; the three conditional input laws are still independent and cap one.

Let `C=[[0,b],[b,0]]`. Complete the square/rectangle in the first two variables. Because `C` is invertible, the conditioned polynomial can be written exactly as

`Q = 2b (X_i+u(X_k,w))(X_j+v(X_k,w))
      + s (X_k+h(w))^2 + c(w)`,                                      (3.3)

where `w` denotes the conditioned outside coordinates. The scalar Schur coefficient is

`s = gamma - (c,d) C^{-1} (c,d)^T
  = - det(B)/b^2`,                                                     (3.4)

because `det C=-b^2` and `det B=(det C)s`. In particular `s!=0`.

For fixed `X_k,w`, the first term in (3.3) is the product of two independently translated cap-one variables. By (2.1), its conditional density is bounded by

`|b|^{-1} Psi( y/(2|b|) )`.

Therefore, after averaging only in `X_k`,

`p_{Q|w}(t)
 <= |b|^{-1} E_{X_k}
    Psi( (t-c(w)-s(X_k+h(w))^2)/(2|b|) ).`                            (3.5)

Put `delta=|s|/(2|b|)`. The account03/B16 weak-`L^2` theorem (the minus sign is absorbed by the absolute-value definition of `Psi`) gives

`|| z -> Psi(a +/- delta z^2) ||_{L^{2,infinity}}
 <= sqrt(15) delta^(-1/4)`.

For any probability density `g<=1`, layer cake yields

`int g(z)F(z)dz <=2 ||F||_{L^{2,infinity}}`.

Thus

`||p_{Q|w}||_infinity
 <= 2 sqrt(15)|b|^{-1} (2|b|/|s|)^(1/4)
 = 2^(5/4)sqrt(15)(|b|^3|s|)^(-1/4)`.

Using `|b|^3|s|=|b||det B|` proves (3.2). The bound is uniform in `w`; averaging the conditional laws preserves it. QED.

### Corollary 3.2 — every invertible physical triple is now locally paid

The completed account03/B16 theorem already controls every invertible physical `3x3` principal block having a nonzero diagonal pivot. If an invertible symmetric `3x3` block has all three diagonal entries zero, every off-diagonal entry must be nonzero and Theorem 3.1 applies. Therefore **there is no remaining algebraic sign/zero-diagonal degeneracy inside a fixed invertible physical principal triple**.

This does **not** solve QFORM because the three-large-eigenvalue hypothesis does not force a physical triple for which the reciprocal local payment in (3.2), or the B16 payment, is uniformly bounded. The live fixed-minor corrections remain fully operative.

## 4. Exact-rank-three simultaneous-null decomposition

Now assume `A=R Lambda R^T` has exact rank three, `R^TR=I_3`, and all three nonzero eigenvalues have modulus at least one. Let `r_i,r_j` be two linearly independent physical spectral rows satisfying

`r_i^T Lambda r_i = r_j^T Lambda r_j =0`.                              (4.1)

Set

`Delta=||r_i wedge r_j||^2>0`,
`b=r_i^T Lambda r_j`.

The nondegenerate signature in dimension three has Witt index one, so two independent null vectors cannot be mutually `Lambda`-orthogonal; hence `b!=0`. Let `v` be a unit Euclidean vector perpendicular to `span{r_i,r_j}` and define the original-coordinate tail aggregate

`Z=sum_{k notin {i,j}} <r_k,v> X_k`.                                  (4.2)

Parseval gives

`sum_{k notin{i,j}} <r_k,v>^2=1`,                                    (4.3)

so the account02/B06 affine-fiber theorem gives

`||p_Z||_infinity<=sqrt(e)`.                                          (4.4)

Writing the tail spectral vector in the basis `(r_i,r_j,v)` and completing the first two coordinates gives the exact identity

`Q=2b(X_i+U_tail)(X_j+V_tail)+s Z^2`,                                 (4.5)

up to an irrelevant deterministic/affine translation already absorbed into the two factors, with

`|s| = |det Lambda| Delta / b^2`.                                     (4.6)

Indeed the `2x2` pair compression has determinant `-b^2`, while

`det([r_i,r_j,v]^T Lambda [r_i,r_j,v])
 = det(Lambda) det([r_i,r_j,v])^2
 = det(Lambda) Delta`.

Combining the product envelope with the weak-`L^2` ridge theorem as in Section 3, but pairing against a density of cap `sqrt(e)`, gives

### Theorem 4.1 — `QFORM-RANK3-NULLPAIR-AGGREGATE-v1`

`||p_Q||_infinity
 <= 2^(5/4)sqrt(15)e^(1/4)
    ( |det Lambda| Delta |b| )^(-1/4).`                               (4.7)

The numerical prefactor before the geometric denominator is

`11.827875502212029...`.

No selected third physical minor is paid. The entire tail is aggregated first in the original product coordinates.

## 5. Wedge mass forces enough hyperbolic coupling

The factor `b` in (4.7) is not independent of `Delta`. Multiply the quadratic form by `-1` if necessary, and assume the signature is `(2,1)`. On the plane spanned by the two null rows, the restricted form has eigenvalues `alpha>0` and `-beta<0`. Cauchy interlacing gives `alpha>=1` because the ambient form has two positive eigenvalues of size at least one.

In an orthonormal eigenbasis of this plane, the two independent null rows have the form

`r_i=t(sqrt(beta),sqrt(alpha))`,
`r_j=s(sqrt(beta),-sqrt(alpha))`.

Hence

`Delta=4t^2s^2 alpha beta`,
`b=2ts alpha beta`,
`b^2=Delta alpha beta`.                                                (5.1)

Writing `c=||r_i||^2`, `h=||r_j||^2`,

`rho:=Delta/(ch)=4alpha beta/(alpha+beta)^2`.                          (5.2)

Every row of an orthonormal-column frame has squared norm at most one, so `c,h<=1` and therefore `rho>=Delta`.

Let `x=beta/alpha`. Since

`rho=4x/(1+x)^2`,

one always has

`x >= x_-(rho) >= x_-(Delta)`,

where

`x_-(u)=(1-sqrt(1-u))/(1+sqrt(1-u))`                                  (5.3)

is the smaller root and is increasing on `[0,1]`. Because `alpha>=1`,

`alpha beta=alpha^2x >= x_-(Delta)`.

Using (5.1),

`|b| >= sqrt( Delta x_-(Delta) ).`                                    (5.4)

Substitution into (4.7) yields the wedge-only bound

`||p_Q||_infinity
 <= 2^(5/4)sqrt(15)e^(1/4)|det Lambda|^(-1/4)
    Delta^(-3/8) x_-(Delta)^(-1/8).`                                  (5.5)

In particular, if `Delta>=1/4`, then

`x_-(1/4)=7-4sqrt(3)=(2-sqrt(3))^2`,
`|b| >= (2-sqrt(3))/2`,

and, since `|det Lambda|>=1`,

`boxed( ||p_Q||_infinity < 27.649 ).`                                 (5.6)

The deterministic checker gives the sharper displayed numerical value

`27.64815326104556...`.

### Consequence for the preceding B13 collar

The previous B13 run reduced the nested-heavy non-leverage-one exact-rank-three endpoint to two heavy rows with `Delta>1/4`, while its remaining terminal obstruction was simultaneous vanishing of their physical diagonal Rayleigh coefficients. Equation (5.6) pays exactly that endpoint. Thus the **simultaneous-null endpoint itself is closed**; any surviving instability in that route must be genuinely near-null (small but nonzero diagonals with a stability argument still required), leave exact rank three, or fall into another unresolved aggregate-selection branch.

## 6. Exact geometric product-set consequence

Apply the completed account02/B13 bang-bang theorem to the slab kernel. Under the hypotheses of Theorem 3.1, for every interval `J` and arbitrary measurable sets `E_l subset R` with `|E_l|=1`,

`|{x in prod_l E_l : x^T A x in J}|
 <= 2^(5/4)sqrt(15)(|b||det B|)^(-1/4) |J|.`                          (6.1)

Under the exact-rank-three null-pair hypotheses, (4.7) and (5.5) give the corresponding product-set estimates with identical constants. Thus the result is already stated in the exact extremal formulation appropriate to arbitrary admissible one-dimensional laws. No interval, centered-uniform, compact-support, bounded-diameter, or bounded-fragment assumption is inserted.

## 7. What remains for full QFORM

Full QFORM remains **OPEN**. The new work closes an algebraic local degeneracy and one exact-rank-three light-cone endpoint, but it does not provide the global original-coordinate aggregation theorem required by the bare three-large-eigenvalue hypothesis.

The first unpaid B13 implication is now a **near-null stability / aggregate-selection** statement: combine the null-pair estimate continuously with the nonzero-pivot affine half-Riesz theorem without any support-dependent perturbation, and then aggregate over high-cardinality physical rows before paying reciprocal local minors. The arbitrary-extra-spectrum branch must remain in the argument. A coefficient-continuity argument in operator norm is not permitted because arbitrary fragmented supports can live arbitrarily far away.

A useful next mechanism is to retain the exact `asinh` product envelope while allowing small diagonal squares in the two hyperbolic coordinates, rather than perturbing the law or the support. This would interpolate analytically between the present null-pair theorem and the completed nonzero-pivot fractional-trace theorem.

## 8. Verification

The proof above is analytic. `CHECK.py` is a deterministic diagnostic for the elementary constant comparisons, the inequality `4 asinh(1/(2sqrt(u)))<=2Psi(u)` over a wide logarithmic grid, and the null-plane algebraic identities. It records `QFORM_NULLPAIR_PRODUCT_CHECK_PASS` and the constants quoted above. Numerical checks are not used as substitutes for any universal step.

No claim of full solution, universal final constant, continuity, novelty, or independent end-to-end review is made.
