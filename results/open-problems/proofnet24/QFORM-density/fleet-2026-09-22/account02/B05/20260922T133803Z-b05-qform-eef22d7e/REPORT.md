# account02/B05 — weighted coordinate coarea threshold and diffuse obstruction

**Run:** `20260922T133803Z-b05-qform-eef22d7e`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM + MECHANISM COUNTEREXAMPLE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target, corrections, and first unpaid implication

The exact target is the arbitrary-law statement: for independent real `X_i` with densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal dimension- and law-independent bound on the essential density of `Q=X^TAX`, or give a valid counterexample.

This run preserves the live corrections: no law-uniform pointwise Fresnel decay, no independence after spectral rotation, no unrestricted spectral-fiber supremum, and no inference from a single tiny physical minor. The first unpaid implication entering this run was to replace the already-closed fixed nonsingular physical triple by a genuinely dimension-free aggregation of coordinate coarea information, or to identify the exact factor that prevents such an aggregation.

The run does both: it proves an exact weighted coordinate-coarea theorem reducing the problem to a scalar gradient small-ball estimate, and then gives a target-valid flat rank-three family showing that no dimension-free scalar weighted-gradient scale can hold. Thus the missing factor is explicit: in the diffuse branch the coordinate-gradient scale is at most order `n^(-1/2)`, which would force at least an `n^(1/4)` loss after the half-Riesz closure.

## 2. Partner result actually applied

The assigned partner `account03/B05` completed `QFORM-OUTER-SQUARE-RANK2-CROSSBLOCK-v1` and `QFORM-GENERIC-SCHUR-HLS-v1` in canonical report

`yspennstate/math-open-problems@f528f2fe40b414a4e87f7d2abbcd153c75d52214:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/account03-B05-20260922T1237Z-qform-r11/REPORT.md`

(blob `e98dac2c5fef3dc0abb61bc802930c4c0caf37b1`). In particular, after a genuine physical outer square, a rank-two residual original-coordinate cross block with singular-value product `Delta` gives

`||p_Q||_inf <= 8 sqrt(3) |a|^(-1/2) Delta^(-1/4)`,

and every fixed nonsingular physical `3x3` Schur branch is now quantitatively closed. I use this result to remove the fixed-triple residual from the B05 debt: the remaining coarea question is aggregation, not generic binary Schur geometry.

I also use the current owner-supplied supporting theorem `QFORM-REGULARIZED-DETERMINANT` (canonical proof `math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`) only at its stated scope: if the **entire range** projection has row leverage at most `1/32`, then the full form has a continuous density bounded by `96e/(7sqrt(2))<27`, retaining arbitrarily small extra eigenvalues. This will close the stress family below for large `n`; it is not promoted to the unrestricted theorem.

## 3. New dimension-free weighted coordinate-coarea inequality

### Lemma 3.1 — `QFORM-WEIGHTED-COAREA-v1`

Let `R:R^m -> R` be a quadratic polynomial and let `X=(X_1,...,X_m)` have independent coordinates with probability densities bounded by one. Let `w_i>=0`, `sum_i w_i=1`, and define

`S_w(x)=sum_i w_i |partial_i R(x)|`.

Then for every real `t` and every `r,s>0`,

`P(|R(X)-t|<r) <= 4r/s + P(S_w(X)<s)`.                    (3.1)

#### Proof

Put `B={|R-t|<r}`. For a fixed coordinate `i` and fixed values of all other coordinates, write `q(u)=R(x_1,...,u,...,x_m)`. This is a polynomial of degree at most two. Because `f_i<=1`,

`int_{|q(u)-t|<r} |q'(u)| f_i(u) du <= int_{|q(u)-t|<r}|q'(u)|du`.

A nonconstant quadratic has at most two monotonicity intervals. On each, the image of the displayed preimage is contained in `(t-r,t+r)`, so the variation of `q` there is at most `2r`. Hence the last integral is at most `4r`; for a linear polynomial it is at most `2r`, and for a constant polynomial the derivative vanishes. Integrating the other product coordinates gives

`E[1_B |partial_i R(X)|] <= 4r`.

Therefore

`P(B and S_w>=s) <= s^(-1) E[1_B S_w] <= 4r/s sum_i w_i =4r/s`.

Adding `P(S_w<s)` proves (3.1). No curved-fiber supremum is taken; the only one-dimensional integrations remain in the original independent coordinates. QED.

## 4. Exact exponent threshold for an outer square

### Theorem 4.1 — `QFORM-GRADIENT-SMALLBALL-TO-HALFRIESZ-v1`

In the setting of Lemma 3.1, suppose for some `alpha>1`, `C>=1`, `sigma>0`,

`P(S_w(X)<s) <= C (s/sigma)^alpha`                         (4.1)

for every `s>0`. Put

`beta=alpha/(alpha+1)`,

`D=(alpha+1) C^(1/(alpha+1)) (4/alpha)^beta`.

Then uniformly in `t`,

`P(|R-t|<r) <= min(1, D (r/sigma)^beta)`.                  (4.2)

Consequently

`sup_t E |t-R|^(-1/2)`
` <= K_alpha C^(1/(2alpha)) sigma^(-1/2)`,                 (4.3)

where

`K_alpha = [4 sqrt(alpha)/(alpha-1)] (alpha+1)^((alpha+1)/(2alpha))`.

Therefore, if an independent scalar `X_0` of density at most one occurs as

`Q=a(X_0+m(X))^2+R(X)`, `a!=0`,

then

`||p_Q||_inf <= K_alpha C^(1/(2alpha)) |a|^(-1/2) sigma^(-1/2)`.          (4.4)

#### Proof

Insert (4.1) into (3.1) and optimize `4r/s+C(s/sigma)^alpha`. The optimizer satisfies

`s^(alpha+1)=4r sigma^alpha/(C alpha)`,

which gives (4.2). For `beta>1/2`, layer cake yields

`E|t-R|^(-1/2)=(1/2) int_0^infinity r^(-3/2) P(|R-t|<r) dr`.

Splitting where `D(r/sigma)^beta=1` gives

`E|t-R|^(-1/2) <= [beta/(beta-1/2)] D^(1/(2beta)) sigma^(-1/2)`,

which simplifies exactly to (4.3). Finally, conditioning on `X` and applying the square pushforward bound for the original independent coordinate `X_0` gives

`p_Q(t)<=|a|^(-1/2) E|t-R|^(-1/2)`.

This proves (4.4). QED.

### The exact threshold

The condition `alpha>1` is not cosmetic. At `alpha=1`, (3.1) gives only the borderline `r^(1/2)` small-ball exponent, and the half-Riesz layer-cake integral diverges logarithmically. Thus **superlinear small-ball decay for the scalar weighted gradient is exactly what coordinate coarea needs after one outer square.**

## 5. Coordinate-minor corollary and recovery of the previous binary constant

Let `H=nabla^2 R`, which is constant. Suppose `I={i_1,...,i_k}` and `J={j_1,...,j_k}` with `k>=2`, all selected weights positive, and `det H[I,J]!=0`. Conditional on `X_{J^c}`, the affine map `X_J -> (partial_i R)_{i in I}` has Jacobian `|det H[I,J]|`. The event `S_w<s` forces

`|partial_i R|<s/w_i` for every `i in I`.

Hence

`P(S_w<s) <= 2^k s^k / [ (prod_{i in I} w_i) |det H[I,J]| ]`.            (5.1)

Thus Theorem 4.1 applies with `alpha=k`, `C=2^k`, and

`sigma=[(prod_{i in I} w_i)|det H[I,J]|]^(1/k)`.                        (5.2)

For the binary Schur residual

`R(y,z)=beta y^2+2gamma yz+delta z^2+linear`, `Delta=beta delta-gamma^2!=0`,

take `w_y=w_z=1/2`. Then `det H=4Delta`, so `(prod w_i)|det H|=|Delta|`. Formula (4.4) at `alpha=2,C=4` gives exactly

`||p_Q||_inf <= 8*3^(3/4) |a|^(-1/2) |Delta|^(-1/4)`,                    (5.3)

recovering the preceding B05 gradient-box constant. This is an internal consistency check and shows that the new theorem genuinely generalizes the earlier two-coordinate calculation.

## 6. Source-valid falsifier: a global weighted-gradient scale is impossible

A tempting next implication would be: from three eigenvalues of modulus at least one, choose weights `w_i>=0`, `sum w_i=1`, so that `S_w= sum w_i |partial_i Q|` satisfies (4.1) with `alpha>1`, `C=O(1)` and `sigma>=c>0` universally. This is false even for an exact rank-three positive semidefinite target family.

Let `n` admit three orthonormal Walsh vectors `u_1,u_2,u_3` with every coordinate equal in modulus to `n^(-1/2)`, let `U=[u_1 u_2 u_3]`, and set

`A=UU^T`.

Then `A` has eigenvalues `1,1,1,0,...,0`, so it satisfies the exact target spectral hypothesis. Let the independent inputs be `X_i ~ Uniform[-1/2,1/2]`, all of density one. Put `Z=U^T X`. Since `Cov(X)=(1/12)I`,

`E ||Z||_2^2 = 3/12 =1/4`.

Therefore Markov gives

`P(||Z||_2<=1) >=3/4`.                                                   (6.1)

Every row of `U` has squared norm `3/n`, and `AX=UZ`. Hence on the event in (6.1),

`|(AX)_i| <= sqrt(3/n)` for every `i`.

Since `nabla Q=2AX`, **for every possible simplex weight vector `w`**,

`S_w(X) <= 2 sqrt(3/n)` on an event of probability at least `3/4`.        (6.2)

Thus for `s_n=3 sqrt(3/n)`,

`P(S_w<s_n) >=3/4`                                                      (6.3)

uniformly over all choices of the weights. If (4.1) held with fixed `C,alpha>0` and a scale bounded below independently of `n`, the right side at `s_n` would tend to zero, contradicting (6.3). Quantitatively, any valid scale in such a bound must satisfy

`sigma <= s_n (4C/3)^(1/alpha) = O(n^(-1/2)).`                           (6.4)

The half-Riesz conclusion (4.3) would therefore pay at least `Omega(n^(1/4))`. This is the exact missing dimension factor for the scalar weighted-coordinate-gradient route.

The same family also explains why the assigned partner's outer-square theorem cannot by itself furnish a global proof via one physical pivot: every physical diagonal coefficient is

`A_ii=3/n`,

so its factor `|a|^(-1/2)` is already order `sqrt(n)`. This does not refute the partner theorem; it refutes the proposed *global extraction* of a uniformly strong single physical outer square.

Crucially, this is **not** a counterexample to QFORM. For `n>=96`, the entire range projection of `A` has leverage exactly `3/n<=1/32`, so the current regularized-determinant diffuse-range theorem applies and bounds the full density by `<27`. The family therefore cleanly separates two mechanisms: scalar coordinate coarea must be localized, while the genuinely diffuse branch requires collective cross-block/Fourier geometry.

## 7. Conditional end-to-end route and first remaining implication

The current conditional route is now:

1. If the entire range of `A` is diffuse at leverage `<=1/32`, apply the supplied regularized-determinant theorem; arbitrary tiny extra eigenvalues are retained.
2. In a localized branch admitting a genuine physical outer square, use the assigned partner's rank-two residual cross-block theorem when a quantitative rank-two cross product is available.
3. Otherwise use Theorem 4.1 whenever the residual has a scalar weighted-gradient small-ball exponent `alpha>1` at a universal scale. Formula (5.1) supplies this from any quantitative original-coordinate Hessian minor of order at least two.
4. Fixed nonsingular physical triples are no longer an independent gap because the assigned partner's generic Schur-HLS theorem closes them.

The first unpaid implication is therefore `QFORM-COAREA-OR-REGDET-BRIDGE-v1`: in the complement of the full-range diffuse theorem, aggregate the heavy physical coordinates and the small-eigenvalue nonseparable phase so as to force either a quantitatively strong rank-two residual cross block (partner interface) or a weighted-gradient exponent `>1` at a universal scale (this report's interface), without selecting a tiny scalar pivot/minor. The flat Walsh family proves that the second alternative alone cannot be universal. Because full-range leverage can equal one merely from arbitrarily small extra eigenvalues, the bridge cannot simply discard those directions or replace the full range by the three active eigenvectors without a source-valid argument.

This is a narrower and more explicit debt than “control the curved fiber”: the local coarea integral is solved once a superlinear scalar gradient small-ball estimate is available, and the exact obstruction is the `n^(-1/2)` gradient scale in diffuse physical coordinates.

## 8. Status

`ESSENTIAL_STEP_APPLIED`. Full QFORM remains **OPEN**. No target counterexample is claimed. The new theorem is a dimension-free geometric inequality conditional only on an explicit gradient small-ball input; the Walsh construction is a rigorous counterexample to the stronger proposed global gradient-scale implication. No moments, compact support (except in the explicit stress law), post-rotation independence, or sign restriction is introduced into the proved theorem.
