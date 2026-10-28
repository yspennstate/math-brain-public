SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T23:08:00Z.
attacking: regularity transfer for the grouped pivot/leaf receiver and the first nonzero-leaf-curvature extension, entirely in original independent coordinates.

# account01/B15 — dominated C0 compiler and a rank-one leaf-curvature receiver

Programme: `QFORM-DENSITY-3EIG-20260922`, activation revision `2026-09-22.5`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Full unrestricted QFORM status: `OPEN_NOT_PROVED`.

The designated completed partner source actually used below is account02/B15:
`yspennstate/math-open-problems@58b7dd57dc1282bcf84fd0ceb0c314baca3a5abe`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T220140Z-account02-B15-QFORM-auto11/REPORT.md`.
Its proved grouped receiver is used only in its stated original-coordinate scope.

## 1. Regularity ledger

The three notions must remain separate.

1. Qualitative absolute continuity is much easier than the target height bound. If the joint input law is absolutely continuous and `A != 0`, then `X^T A X` is absolutely continuous. This does not use the density cap, independence, or three large eigenvalues.
2. The central QFORM problem is a universal essential `L^infinity` bound. It must be proved by interval/small-ball or equivalent height estimates; continuity is not a substitute.
3. A continuous representative is a stronger, subsequent conclusion. The main lemma below shows one clean mechanism: once conditional `C_0` densities are dominated by an integrable conditional height, the mixture is `C_0` with no height loss.

No pointwise quadratic Fourier decay, spectral-coordinate independence, or projection-only shortcut is used.

## 2. Qualitative absolute continuity in original coordinates

### Proposition 2.1
Let `X_1,...,X_n` be independent absolutely continuous real random variables and let `A` be a nonzero real symmetric matrix. Then

`X^T A X << Lebesgue`.

### Proof
If some `A_ii != 0`, condition on every coordinate except `X_i`. The remaining map is a nonconstant quadratic polynomial

`x -> A_ii x^2 + b x + c`.

A nonconstant one-variable polynomial with finitely many critical points sends an absolutely continuous law to an absolutely continuous law: on each interval avoiding the finitely many critical points the inverse branches are locally Lipschitz, and the critical set itself has input probability zero. Averaging the conditional laws proves the claim.

If every diagonal entry is zero, choose `i != j` with `A_ij != 0`. Condition on every coordinate except `X_i`. Then

`Q = B X_i + C`,
`B = 2 sum_{k != i} A_ik X_k`.

Choose `j` with `A_ij != 0`. Conditional on all variables entering `B` except `X_j`, the random coefficient `B` is a nonconstant affine image of `X_j`; hence `B` is absolutely continuous and `P(B=0)=0`. For almost every conditioning value, `x -> Bx+C` is a nonconstant affine map, so the conditional output law is absolutely continuous. Average again. QED.

This establishes only qualitative absolute continuity; it contains no universal height estimate.

## 3. A dominated conditional-C0 compiler

### Lemma 3.1
Let `(Omega,P)` be a probability space. For almost every `omega`, let `q_omega` be a probability density in `C_0(R)`. Assume the map is jointly measurable and

`||q_omega||_infinity <= H(omega)`,
`E H < infinity`.

Then

`q(t) := E q_omega(t)`

is a probability density in `C_0(R)` and

`||q||_infinity <= E H`.

Moreover, for every `h`,

`sup_t |q(t+h)-q(t)| <= E[ min(2H(omega), sup_t |q_omega(t+h)-q_omega(t)| ) ]`.      (3.1)

### Proof
The height estimate is immediate from Tonelli. For fixed `h`, the integrand in (3.1) tends pointwise to zero as `h -> 0` and is dominated by `2H`, so dominated convergence yields uniform continuity of `q`. For vanishing at infinity, `sup_{|t|>=R} q_omega(t) -> 0` for each `omega` and is dominated by `H(omega)`; another dominated-convergence step gives

`sup_{|t|>=R} q(t) <= E sup_{|t|>=R} q_omega(t) -> 0`.

Thus `q in C_0`. QED.

The significance is logical: an integrable conditional height certificate pays the `L^infinity` problem first; conditional `C_0` then upgrades the representative afterward with the same constant.

## 4. Two scalar estimates

### Lemma 4.1 — negative moments under a density cap
Let `Z` have a density bounded by `H`. For `0<alpha<1`,

`E |Z|^{-alpha} <= [2^alpha/(1-alpha)] H^alpha`.                    (4.1)

### Proof
Among densities bounded by `H` and having total mass one, the integral against the symmetric decreasing weight `|z|^{-alpha}` is maximized by placing density `H` on the centered interval of length `1/H`. Hence

`E |Z|^{-alpha}`
` <= H int_{-1/(2H)}^{1/(2H)} |z|^{-alpha} dz`
` = [2^alpha/(1-alpha)] H^alpha`.
QED.

At `alpha=2/3`,

`E |Z|^{-2/3} <= 3*2^(2/3) H^(2/3)`.                              (4.2)

### Lemma 4.2 — sharp-enough L^(3/2) square estimate
Let `V` have density `f<=1`, let `b in R`, and let `d != 0`. The law of

`S = d(V-b)^2`

has a density `h` satisfying

`||h||_(3/2) <= 2 |d|^(-1/3)`.                                    (4.3)

### Proof
Translations of `V` preserve the cap, so take `b=0`; reflection handles `d<0`. First take `d=1`. For `y>0`,

`h(y) = [f(sqrt y)+f(-sqrt y)]/(2 sqrt y)`.

For every `1<=p<2`, changing variables `y=x^2`, using `(u+v)^p <=2^(p-1)(u^p+v^p)` and `f^p<=f`, gives

`||h||_p^p <= int_R f(x)|x|^(1-p) dx`.

The weight is symmetric decreasing, so the density-cap bathtub bound gives

`int f(x)|x|^(1-p) dx <= int_{-1/2}^{1/2}|x|^(1-p) dx`
` = 2^(p-1)/(2-p)`.

At `p=3/2` the right side is `2 sqrt 2`, whose `(2/3)` power is exactly `2`. Scaling by `d` multiplies the `L^p` norm by `|d|^{-1+1/p}`; at `p=3/2` this is `|d|^{-1/3}`. QED.

## 5. Square-plus-linear smoothing

### Lemma 5.1
Let `U,V` be independent real variables with densities bounded by one. For `d != 0`, arbitrary `a`, and `b != 0`, the random variable

`T = dU^2 + aU + bV`

has a canonical density in `C_0(R)` and

`||p_T||_infinity <= 2 |d|^(-1/3) |b|^(-2/3)`.                    (5.1)

### Proof
Complete the square in the ORIGINAL coordinate `U`:

`dU^2+aU = d(U+a/(2d))^2 - a^2/(4d)`.

The translated `U` still has a cap-one density. By Lemma 4.2, the first summand has an `L^(3/2)` density of norm at most `2|d|^(-1/3)`. The variable `bV` has density `g_b` with

`||g_b||_3 <= ||g_b||_infinity^(2/3)||g_b||_1^(1/3) <= |b|^(-2/3)`.

Young's conjugate-exponent inequality (`3/2` and `3`) gives (5.1). In addition, convolution maps `L^(3/2)*L^3` into `C_0`: approximate both factors by compactly supported continuous functions in their respective `L^p` spaces and use Young's inequality for uniform convergence of the convolutions. The deterministic completed-square translation does not affect the assertion. QED.

This is already a useful regularity separation: the `C_0` conclusion follows from a finite-height convolution estimate, not conversely.

## 6. Main new receiver: one curved leaf plus one linear leaf

### Theorem 6.1 — `QFORM-SQUARE-LINEAR-LEAF-C0-v1`
Let `P=(P_1,...,P_k), U, V` be independent original input coordinates, each with density at most one, and let `W` denote all remaining original coordinates. After conditioning on `W=w`, suppose the quadratic form can be written

`Q = R_w(P) + d U^2 + a_w(P) U + b_w(P) V`,                       (6.1)

where

- `d != 0` is deterministic;
- `R_w(P)` is arbitrary (in particular, an arbitrary quadratic polynomial in the pivots);
- `a_w(P)` is arbitrary affine in the pivots;
- `b_w(P)=2 m.P + beta(w)` for a deterministic vector `m != 0`;
- there is no `UV` term and no `V^2` term.

Put

`m_* = max_j |m_j|`.

Then the full, unconditioned output law has a canonical density in `C_0(R)` and

`boxed( ||p_Q||_infinity <= 6 |d|^(-1/3) m_*^(-2/3). )`           (6.2)

No condition is imposed on the support, moments, continuity, centering, or connectedness of the input densities.

### Proof
Fix `(w,p)`. By Lemma 5.1, provided `b_w(p) != 0`, the conditional law in `(U,V)` has a `C_0` density with

`||p_(Q|w,p)||_infinity <= 2 |d|^(-1/3)|b_w(p)|^(-2/3).`          (6.3)

Now choose `j` with `|m_j|=m_*`. Conditional on all pivot coordinates except `P_j`,

`b_w(P)=2m_jP_j+constant`.

Therefore `b_w(P)` has a one-dimensional density bounded by

`H_b <= 1/(2m_*)`,                                                   (6.4)

uniformly in `w`; in particular `P(b_w(P)=0)=0`. Applying (4.2),

`E_P |b_w(P)|^(-2/3)`
` <= 3*2^(2/3)*(1/(2m_*))^(2/3)`
` = 3m_*^(-2/3).`                                                    (6.5)

Average (6.3) and use (6.5):

`E_P ||p_(Q|w,P)||_infinity <= 6 |d|^(-1/3)m_*^(-2/3)`,             (6.6)

uniformly in `w`. This gives the interval domination and hence essential boundedness (6.2) before continuity is invoked. Finally apply Lemma 3.1 to the conditional `C_0` densities using the integrable dominator in (6.3). This yields a canonical `C_0` representative with exactly the same height bound. QED.

### Matrix form
A sufficient original-coordinate physical pattern is: select a pivot set `P`, two leaf coordinates `(U,V)`, and condition on all other coordinates. If

`A_UU=d != 0`, `A_UV=0`, `A_VV=0`,

and at least one pivot-to-`V` entry is nonzero, then (6.2) holds with

`m_* = max_{j in P}|A_{jV}|`.

All pivot-pivot curvature, all pivot-to-`U` couplings, all outside curvature, and all couplings to conditioned outside coordinates are arbitrary. Outside couplings to `V` merely alter `beta(w)` and disappear from the bound. This is a product-preserving physical-coordinate receiver; no diagonalization of the source is performed.

## 7. Genuine full-target chamber not covered by the zero-leaf grouped hypothesis

Take four independent cap-one variables `(X,Z,Y,U)` and

`Q = -X^2 - Z^2 + Y^2 + 2XY + 2ZU`.                               (7.1)

Its symmetric matrix in the displayed ordering is

`A = [[-1,0,1,0],`
`     [ 0,-1,0,1],`
`     [ 1,0,1,0],`
`     [ 0,1,0,0]].`                                                 (7.2)

The eigenvalues are

`-sqrt(2), sqrt(2), (-1-sqrt(5))/2, (-1+sqrt(5))/2`.                (7.3)

Hence three eigenvalues have modulus at least one: `sqrt(2),sqrt(2),(1+sqrt(5))/2`.

In Theorem 6.1 use pivots `P=(X,Z)`, curved leaf `Y`, linear leaf `U`, `d=1`, and `m_* = |A_ZU|=1`. Therefore

`boxed( ||p_Q||_infinity <= 6,   p_Q in C_0(R). )`                 (7.4)

This is a genuine instance of the owner's target. It is structurally outside account02/B15's zero-internal-leaf-block receiver for any two-leaf reordering of these four coordinates: only `U` has zero diagonal, while a zero `2x2` leaf block would require two zero diagonal entries. Thus Theorem 6.1 pays a nonzero-leaf-curvature chamber that the newest grouped theorem does not itself cover.

## 8. Required application of completed account02/B15 result

Now apply the designated partner theorem to the actual target family

`Q_0 = 2XY + Z^2 + 2ZU`.                                           (8.1)

Order pivots and leaves as

`P=(X,Z)`, `L=(Y,U)`.

Then the selected physical block is

`[[C,M],[M^T,0]]`, with `C=diag(0,1)` and `M=I_2`.

Account02/B15's completed theorem therefore gives, for every interval `I`,

`boxed( P(Q_0 in I) <= 2 |I| )`,                                   (8.2)

hence

`boxed( ||p_(Q_0)||_infinity <= 2. )`                               (8.3)

This is an actual use of the completed partner result, not merely a citation. The same source also checked the ruled majority inequality

`P(Q_0 in I, Q_0 >= -U^2) <= pi sqrt(2)|I|`.                        (8.4)

For the continuity upgrade, one may either use the partner's cited endpoint-convolution compiler or Lemma 3.1 directly: conditional on `(X,Z)`, the leaf variable is `2XY+2ZU`, whose density is a convolution whenever `XZ != 0`; the exceptional axes have zero pivot probability. The conditional height is dominated by `1/(2 max(|X|,|Z|))`, and the partner's layer-cake calculation proves its expectation is at most `2`. Thus

`boxed( p_(Q_0) in C_0(R) )`                                       (8.5)

with no loss from (8.3). Again, the logical order is height first, continuity second.

## 9. Why the new theorem does not solve full QFORM

Theorem 6.1 requires an ORIGINAL-coordinate leaf `V` with zero quadratic coefficient and no coupling to the curved leaf `U`, together with a nonzero pivot-to-`V` coupling. The bare hypothesis `s_3(A)>=1` does not force such a pattern. Nor does it force account02/B15's invertible grouped cross determinant with a zero internal leaf block. Therefore (6.2) is a genuine new paid chamber, not a structural reduction of every target matrix.

The first unpaid implication for this B15 line is to replace the aligned rank-one leaf block by a genuinely nonzero `2x2` leaf block, especially an indefinite one, while averaging its logarithmic critical singularity against the pivot-generated affine coefficient before any fiber supremum. Any such extension must preserve the original product coordinates; generic projection/X-ray information is insufficient by the live correction.

## 10. Status

- Qualitative absolute continuity: proved under the much weaker condition `A!=0` and absolutely continuous inputs.
- Universal essential height: still OPEN in full target scope.
- Conditional regularity compiler: proved; integrable conditional `C_0` heights yield full `C_0` with no constant loss.
- New square-linear leaf receiver: proved with constant `6 |d|^(-1/3)m_*^(-2/3)` and `C_0` conclusion.
- Designated account02/B15 theorem: applied to the genuine target family (8.1), yielding the concrete inequality `P(Q_0 in I)<=2|I|` and `p_Q0 in C_0`.
- No pointwise quadratic Fourier decay, rotated-independence assumption, or projection-only shortcut was used.
