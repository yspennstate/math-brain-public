# Grouped rank-two coefficient plus transverse receiver Fresnel packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account02/B01` — Oscillatory replacement  
Run: `20260923T073435Z-account02-B01-qform-aggfresnel`  
Status: `PROVED_SUPPORTING_TARGET-LEVEL THEOREM`; full QFORM remains OPEN.

## 1. Source scope and correction discipline


The phase-aligned-density counterexample remains binding: there is no law-uniform pointwise scalar quadratic-phase decay under only `f<=1`. Nothing below asserts one. The proof obtains integrability only after averaging a two-dimensional random cross coefficient and then performing a joint Fresnel/Brascamp--Lieb integral.

## 2. The theorem

### Theorem (grouped rank-two coefficient + r transverse receiver Fresnel directions)

Let the original independent coordinates be split into disjoint banks `I,J` (any other original coordinates may first be conditioned). Every coordinate density is bounded by one.

Assume the exact physical cross matrix `K=A_{IJ}` has rank two. Write an SVD

`K = U Sigma V^T`,

where `U` and `V` have two orthonormal columns and `Sigma=diag(kappa_1,kappa_2)` with `kappa_1,kappa_2>0`. Put

`Delta = kappa_1 kappa_2`, `R0=range(V)`.

Assume the receiver-bank self curvature has the form

`A_{JJ} = D + R Lambda R^T`,

where `D` is an arbitrary diagonal matrix, `R` has `r` orthonormal columns, and `Lambda=diag(lambda_1,...,lambda_r)` is invertible. Assume `[V R]` has full column rank. Define

`Omega^2 = det( R^T (I - V V^T) R ) > 0`

(and by convention `Omega=1` when `r=0`). Let

`S = span(V,R)`, `d=dim S=2+r`,

and suppose the physical-coordinate leverages of this augmented receiver subspace obey

`ell_j := e_j^T P_S e_j <= 1/2` for every `j in J`.

Then, uniformly over every arbitrary real measurable function `H(X_I)`, every affine term on `J`, and every conditioned value of outside coordinates, the random variable

`Q = H(X_I) + 2 X_I^T K X_J + X_J^T (D+R Lambda R^T) X_J + b^T X_J + c`

has a continuous density and

`|phi_Q(t)| <= min(1, B_r |t|^{-(2+r/2)})`,

where

`B_r = (4*pi)^(2+r/2) / [ 2 Delta Omega sqrt(|det Lambda|) ]`.

Consequently

`||p_Q||_infinity <= 4(r+4)/(r+2) * [2 Delta Omega sqrt(|det Lambda|)]^(-2/(r+4)).`      (2.1)

For one genuinely transverse receiver square (`r=1`),

`||p_Q||_infinity <= [20/(3*2^(2/5))] (Delta Omega sqrt(|lambda|))^(-2/5)`

and

`20/(3*2^(2/5)) = 5.0523885550...`.

The estimate is invariant under signs of the `lambda_k`; only `|det Lambda|` appears.

## 3. Proof

Condition all outside coordinates. Their couplings contribute only to `H`, `b`, and `c`, so it is enough to prove the displayed conditional estimate uniformly in those values.

### 3.1 The random cross coefficient has a planar density cap

Put

`A = K^T X_I`.

In coordinates of `R0`,

`A = V Sigma (U^T X_I)`.

The source-valid two-dimensional projection theorem for a product of cap-one one-dimensional densities gives

`||p_{U^T X_I}||_infinity <= 2`.

Therefore, with planar Lebesgue measure on `R0`,

`||p_A||_infinity <= 2/Delta`.                                      (3.1)

This is an ordinary marginal statement; no conditional projection-density cap is used.

### 3.2 Remove arbitrary curvature on the conditioned bank

For fixed `a in R0`, define

`F_t(a) = E_J exp{ i t [ X_J^T(D+R Lambda R^T)X_J + 2 a^T X_J + b^T X_J + c ] }`.

Since the entire `I`-self part has modulus one,

`|phi_Q(t)| = |E_I e^{itH(X_I)} F_t(K^T X_I)| <= E_I |F_t(K^T X_I)|`.

Using (3.1),

`|phi_Q(t)| <= (2/Delta) integral_{a in R0} |F_t(a)| da`.            (3.2)

This is the step that lets completely arbitrary nonlinear same-bank curvature survive on the `I` side.

### 3.3 Fresnel-linearise only the receiver low-rank curvature

For each `j in J` absorb the diagonal and affine receiver terms into a twisted one-dimensional amplitude

`g_{j,t}(x)=f_j(x) exp{i t(D_j x^2 + b_j x)}`,

so `|g_{j,t}|<=f_j`. Apply the proved Fresnel identity in the required source package to the `r` squares `lambda_k <R_k,X_J>^2`. After removing the damping by dominated convergence,

`|F_t(a)| <= prod_k (4*pi*|t lambda_k|)^(-1/2)`

`    * integral_{u in R^r} prod_{j in J} | ghat_{j,t}( (R u)_j + 2 t a_j ) | du`.          (3.3)

Any additional fixed receiver frequency translation is harmless below, because the geometric Brascamp--Lieb inequality is invariant under translating each one-dimensional argument.

### 3.4 Average before paying the transverse determinant

Insert (3.3) into (3.2). In the two-dimensional space `R0`, set `s=2t a`; hence

`da=(2|t|)^(-2) ds`.

The linear map

`T : R0 x R^r -> S`, `T(s,u)=s+Ru`,

has volume Jacobian

`sqrt(det([V R]^T[V R])) = sqrt(det(R^T(I-VV^T)R)) = Omega`.

Thus

`ds du = Omega^(-1) dxi_S`.                                       (3.4)

The averaging has therefore aggregated the entire rank-two cross area `Delta` before any physical minor is selected.

### 3.5 The augmented subspace integral

Choose orthonormal coordinates on `S`. Let `a_j` denote the row representing the physical coordinate functional `xi -> xi_j`; then

`sum_j a_j a_j^T = I_d`, `|a_j|^2=ell_j`, `sum_j ell_j=d`.

Ignoring rows with `ell_j=0`, set `u_j=a_j/sqrt(ell_j)`. The geometric Brascamp--Lieb inequality gives

`integral_S prod_j |ghat_{j,t}(xi_j+q_j)| dxi`

` <= prod_j [ ell_j^(-1/2) integral_R |ghat_{j,t}(z)|^(1/ell_j) dz ]^(ell_j)`.

Because `ell_j<=1/2`, the source Fourier lemma applies with `p=1/ell_j>=2`:

`integral |ghat_{j,t}|^(1/ell_j) <= 4*pi*sqrt(ell_j)`.

The leverage factors cancel exactly, leaving

`integral_S prod_j |ghat_{j,t}(xi_j+q_j)| dxi <= (4*pi)^d = (4*pi)^(2+r)`.              (3.5)

Combining (3.2)--(3.5),

`|phi_Q(t)| <= [2/Delta] [2|t|]^(-2) Omega^(-1)`

`   * (4*pi)^(-r/2) |t|^(-r/2) |det Lambda|^(-1/2) * (4*pi)^(2+r)`

` = (4*pi)^(2+r/2) / [2 Delta Omega sqrt(|det Lambda|)] * |t|^(-(2+r/2))`.

This is the claimed characteristic-function envelope.

### 3.6 Inversion

Let `alpha=2+r/2=(r+4)/2>1`. For `B>0`,

`integral_R min(1,B|t|^(-alpha)) dt = 2 alpha/(alpha-1) B^(1/alpha)`.

Fourier inversion therefore gives

`||p_Q||_infinity <= [alpha/(pi(alpha-1))] B_r^(1/alpha)`

` = 4(r+4)/(r+2) [2 Delta Omega sqrt(|det Lambda|)]^(-2/(r+4))`,

which proves (2.1). Since `phi_Q in L^1`, this scoped branch also has a continuous density representative.

## 4. Exact designated-partner endpoint

At `r=0` there is no receiver low-rank self-curvature. The theorem above gives, under the receiver leverage gate,

`||p_Q||_infinity <= 4 sqrt(2) Delta^(-1/2)`.

The completed designated-partner account03/B01 determinant-area theorem applies to this exact one-sided-affine packet with no leverage assumption and gives the strictly sharper actual inequality

`||p_Q||_infinity <= 2 sqrt(pi) Delta^(-1/2)`.                       (4.1)

Thus (4.1) is the correct completed zero-Fresnel endpoint to use when available; the new result supplies a different resource: one or more genuinely transverse receiver Fresnel directions while retaining arbitrary nonlinear curvature on the opposite bank.

This is an equation-level application of the completed partner result, not a summary-only citation.

## 5. Strict-N3 target family paid by the new theorem

The theorem is not merely an abstract interpolation. It uniformly controls a target-valid family with a dense full-rank non-diagonal self block on the conditioned bank.

Let `m=2^q>=8`. Let `H_m` be a symmetric normalized Sylvester-Hadamard matrix, so

`H_m^T=H_m`, `H_m^2=I`, and every entry has magnitude `m^(-1/2)`.

Choose two orthonormal Walsh vectors `u_1,u_2` in the `I` bank and three orthonormal Walsh vectors `v_1,v_2,w` in the `J` bank. Every coordinate of each has magnitude `m^(-1/2)`. Fix `0<eta<=1/4`, set `c=1+eta`, and define

`K = c (u_1 v_1^T + u_2 v_2^T)`,

`A_{m,eta} = [[ eta H_m, K ], [ K^T, w w^T ]]`.                    (5.1)

### Target spectrum

Let `A_0` be (5.1) with the `eta H_m` block replaced by zero. Its nonzero singular values are

`c,c,c,c,1`:

there are two cross pairs with eigenvalues `+c,-c`, and the orthogonal receiver direction `w` has eigenvalue one. The perturbation `diag(eta H_m,0)` has operator norm `eta`. Hence singular-value Weyl gives

`s_k(A_{m,eta}) >= c-eta = 1`, `k=1,2,3,4`.

Since `A_{m,eta}` is symmetric, its singular values are the absolute eigenvalues. Thus (5.1) has at least four eigenvalues of absolute value at least one, so it satisfies the exact spectral hypothesis.

### Strict no-pivot geometry

Physical diagonals obey

`|A_ii| <= max(eta/sqrt(m),1/m)`.

For two `I` coordinates, every physical `2x2` principal determinant has magnitude at most

`2 eta^2/m`.

For two `J` coordinates the determinant is zero because `w w^T` has rank one. For one `I` and one `J` coordinate,

`|det A_{ij}| <= eta/m^(3/2) + 4 c^2/m^2`.

Therefore for every fixed N3 threshold `tau>0`, all physical diagonals and physical-pair determinants are smaller than `tau` for all sufficiently large powers of two `m`.

### New averaged-frequency bound

Here

`Delta=c^2`, `r=1`, `lambda=1`, `Omega=1`,

and the augmented receiver subspace `span(v_1,v_2,w)` has every leverage equal to `3/m<=1/2`. Therefore

`||p_{X^T A_{m,eta} X}||_infinity`

` <= [20/(3*2^(2/5))] c^(-4/5)`

` <= 5.0523885551`.                                                (5.2)

For the concrete stress value `eta=1/4` (`c=5/4`), (5.2) is

`||p_Q||_infinity <= 4.2263818466`.

The full-rank non-diagonal Hadamard curvature `eta H_m` is retained exactly; it is not treated as a small random quadratic perturbation.

### Partner endpoint on the same stress architecture

If only the receiver square is removed, define

`A^0_{m,eta} = [[eta H_m,K],[K^T,0]]`.

This remains target-valid: its first four singular values are at least `c-eta=1`. It remains strict N3 for large `m`. The designated partner theorem (4.1) applies directly, with `Delta=c^2`, and yields

`||p_{X^T A^0_{m,eta}X}||_infinity <= 2 sqrt(pi) / c`.              (5.3)

Thus the completed partner pays the exact zero-receiver-curvature endpoint, while the new theorem pays the genuinely non-diagonal receiver-square case without discarding the dense opposite-bank curvature.

## 6. Why this does not violate the pointwise-decay correction

For a fixed scalar density `f<=1`, a phase-aligned fragmented support can make `|E e^{isX^2}|` stay close to one at an arbitrarily prescribed large frequency. The present argument never bounds that scalar quantity by a power of `|s|`.

The integrable exponent in Section 3 comes only after:

1. averaging the two-dimensional random coefficient `K^T X_I` using its product-projection density cap;
2. Fresnel-linearising the receiver low-rank curvature jointly;
3. integrating over the entire augmented subspace `span(range K^T,R)`;
4. applying the source `L^p` Fourier estimate through geometric Brascamp--Lieb.

Hence the decay is a distributional/joint-frequency phenomenon and is compatible with the phase-aligned counterexample.

## 7. Remaining implication

The new theorem pays a substantial slice of the previous `two-sided-curved bicore` gap: one side may have completely arbitrary nonlinear curvature, while the other may carry any diagonal curvature plus an `r`-dimensional non-diagonal packet whose directions are quantitatively transverse to the rank-two cross row space and whose augmented physical leverage is at most `1/2`.

What is still unpaid is a structural routing statement for the complementary strict-N3 states:

`QFORM-CURVED-RECEIVER-TRANSVERSE-OR-ALIGN-ROUTING-v1`.

Given a strict-N3 rank-two bicore with substantial nonlinear self-curvature on both active banks, show quantitatively that either

* a receiver curvature packet has controlled transverse determinant `Omega`, determinant scale `|det Lambda|`, and augmented leverage, so (2.1) applies;
* the receiver curvature is sufficiently aligned/concentrated to route to the one-sided-affine determinant-area theorem, a physical pair, a mixed-hub/ridge/volume packet, or another already-paid branch;
* or a different product-preserving third-curvature packet can spend the existing bilateral half-Riesz estimate.

The full QFORM conjecture is not proved or disproved here. No two independent end-to-end reviews of a full candidate exist.
