# QFORM universal proof assembly: a full-matrix near-diagonal theorem and a hard saddle aggregation family

Run: `20260922T121338Z-b19-qform-r11`  
Worker: `fleet01/B19`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction-aware starting point

The target is: for every `n`, independent real `X_i` with densities `0 <= f_i <= 1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove

`P(X^T A X in [t,t+h]) <= C h`

for one universal finite `C`, every real `t`, and every `h>0`.

Fresh controls supersede the older POS3 assignment. The following current corrections are enforced here:

* law-uniform pointwise Fresnel decay for arbitrary density-`<=1` inputs is false;
* a fixed cross minor by itself does not close the rank-two indefinite endpoint;
* generic projection/X-ray or fiber-sup information loses essential product provenance;
* the diagonal `C=pi` result is valid, but `pi` is not a universal constant for the rotated target.

The latest complete synthesis consumed here is fleet04/B19 run `20260922T122030Z-fleet04-B19-QFORM-r1`, report `math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`, which proves the finite-union product-indicator testing core and isolates `QFORM-PRODUCT-ELLIPTIC-TRACE-v1` as its first unpaid implication. The principal named external worker result applied below is fleet02/B10 run `20260922T1147Z-qform-rank3-coupled-B10-r1`, report `math-open-problems@1eba911614ef9f6683f8eacb5d6608a0f9a4b833`, which proves the hyperbolic-square smoothing theorem.

## 2. Compact conditional end-to-end argument

Fleet04/B19 gives an exact reduction from arbitrary input densities to bounded finite-union product indicators for interval concentration. Among three large eigenvalues, two have the same sign. Fleet03/B06 then gives a dimension-free `L^p` elliptic-energy estimate for the pushforward along that same-sign spectral plane. Thus the full theorem follows from the following single trace statement:

**Product-elliptic trace implication.** For the special `H(z,s)` arising from an original-coordinate product law and a same-sign spectral plane with both eigenvalue magnitudes at least one, the graph trace

`int H(z, sigma(t-q_perp(z))) 1_{sigma(t-q_perp(z))>=0} dz`

is bounded uniformly in `t`, dimension, the product law, and the remaining quadratic form `q_perp`, provided `q_perp` contains the third large spectral direction.

The generic `L^1/L^2/L^infinity` norms of `H` are not enough; current correction evidence already rules that out. The mathematical issue is therefore to preserve and spend product provenance before the trace loses it.

This run proves the full target in a nontrivial full-matrix basin and then constructs an exact target-family showing that the hard trace cannot be reduced to either a single well-conditioned physical triple or a rank-three original-coordinate cross block.

## 3. New theorem: full target in a near-coordinate-diagonal basin

### Theorem `QFORM-NEAR-DIAGONAL-FULL-v1`

Let `A` be a real symmetric `n x n` matrix with third singular value `s_3(A) >= 1`. Let

`D = diag(A_11,...,A_nn)`, `R=A-D`, `delta=||R||_op`.

If `delta < 1/2`, then for every independent real `X_i` with densities bounded by one, `Q=X^T A X` has an essentially bounded density satisfying

`||p_Q||_infinity <= pi / sqrt(1-2 delta)`.

In particular, if `||A-diag(A)||_op <= 1/4`, then

`||p_Q||_infinity <= pi sqrt(2)`.

The theorem allows arbitrary dimension, arbitrary signs and sizes of all additional eigenvalues, arbitrary cross couplings to all outside coordinates, and arbitrary density-`<=1` input laws. No moment, support, continuity, log-concavity, or post-rotation independence is used.

### Proof

Singular values are 1-Lipschitz in operator norm, so

`s_3(D) >= s_3(A)-||R||_op >= 1-delta`.

Because `D` is diagonal, at least three physical indices have

`|A_ii| >= 1-delta`.

Among these three diagonal entries, two have the same sign. Call their indices `i,j`. Since `|A_ij| <= ||R||_op <= delta`, the physical `2 x 2` principal block

`B = [[A_ii,A_ij],[A_ij,A_jj]]`

is definite and

`det B = A_ii A_jj - A_ij^2 >= (1-delta)^2-delta^2 = 1-2 delta >0`.

Condition on every coordinate except `X_i,X_j`. The conditional quadratic is

`q(x)=x^T B x + 2 ell^T x + c`, `x=(X_i,X_j)`,

where `ell,c` may depend arbitrarily on the conditioned variables. The conditional joint density of `x` is at most one. Completing the square and applying the linear map `y=|B|^{1/2}(x+B^{-1}ell)` reduces the quadratic to `+|y|^2` or `-|y|^2` plus a constant. The Jacobian is `1/sqrt(det B)`.

For every interval `J` of length `h`, the planar Lebesgue measure of

`{y: +/- |y|^2 in J}`

is at most `pi h`: it is an annulus (possibly truncated at radius zero) whose area is `pi` times the length of the corresponding interval in `r^2`. Therefore, conditionally on the outside variables,

`P(Q in J | outside) <= pi h / sqrt(det B) <= pi h/sqrt(1-2delta)`.

Averaging proves the same inequality unconditionally. The interval inequality implies absolute continuity and an essentially bounded Radon-Nikodym derivative with the stated bound. No continuity claim is made here. QED.

### Consequence for proof assembly

For a target matrix, `s_3(A)>=1` automatically. Hence any remaining proof may, at no loss, put the quantitative hard branch behind

`||A-diag(A)||_op > 1/4`,

because the complementary branch already has the universal cap `pi sqrt(2)`. This is a full-matrix statement and therefore already handles arbitrary extra spectrum in this basin.

## 4. Exact hard family: fixed local extraction and rank-three cross cuts both fail

The next construction is not a counterexample to the conjecture. It is a counterexample to a tempting proof mechanism: after entering the strongly coupled branch, one cannot insist on extracting either a uniformly well-conditioned fixed physical triple or a rank-three disjoint original-coordinate cross block.

For integer `m>=2`, set `n=2m+1`. Partition coordinates as one pivot `0`, a group `Y` of size `m`, and a group `Z` of size `m`. Define orthonormal columns

`u_1=e_0`,

`u_2=m^{-1/2} 1_Y`,

`u_3=m^{-1/2} 1_Z`,

write `U=[u_1,u_2,u_3]`, and let

`Lambda = [[0,1,0],[1,0,0],[0,0,1]]`,

`A_m=U Lambda U^T`.

### Exact spectral and physical properties

Because `U^T U=I_3`, the nonzero eigenvalues of `A_m` are exactly those of `Lambda`, namely `1,1,-1`. Thus every `A_m` satisfies the full three-large-eigenvalue hypothesis.

In physical coordinates the only nonzero structures are

* `A_{0j}=A_{j0}=m^{-1/2}` for `j in Y`;
* the `Z x Z` block is the all-ones matrix divided by `m`;
* all other entries vanish.

The off-diagonal operator norm is exactly one: the `0-Y` star has singular/eigenvalue magnitude one, while the off-diagonal part of the `Z` block has norm `(m-1)/m`.

### No rank-three disjoint cross block

For any disjoint coordinate sets `S,T`, the cross block is

`A_m[S,T]=U_S Lambda U_T^T`.

At most one of `S,T` contains the unique support point of `u_1=e_0`. The other side therefore sees only the `u_2,u_3` spectral coordinates and has row-span dimension at most two. Consequently

`rank A_m[S,T] <=2`

for every disjoint `S,T`.

Hence the rank-`>=3` cross-block theorems, powerful as they are, cannot even start on this family.

### Every fixed physical triple degenerates

Take any principal `3 x 3` block.

* If it omits coordinate `0`, it lies in the direct residual `Y/Z` structure and is singular.
* If it contains `0` and two coordinates from the same residual group, it is singular.
* If it contains `0`, one `Y` coordinate, and one `Z` coordinate, then after permutation it is

`[[0,m^{-1/2},0],[m^{-1/2},0,0],[0,0,m^{-1}]]`,

whose singular values are `m^{-1/2},m^{-1/2},m^{-1}`.

Therefore

`max_{|I|=3} sigma_min(A_m[I,I]) = 1/m ->0`.

Any argument that first chooses one principal triple and pays a reciprocal conditioning constant necessarily loses dimension on this target family.

## 5. The same hard family is nevertheless uniformly controlled by aggregation

For independent input variables write

`Y_m=m^{-1/2} sum_{j in Y} X_j`,

`Z_m=m^{-1/2} sum_{k in Z} X_k`.

The coordinate groups are disjoint, so `X_0,Y_m,Z_m` are independent, and exactly

`X^T A_m X = 2 X_0 Y_m + Z_m^2`.

A standard one-dimensional product-marginal bound, used explicitly in fleet02/B07, gives a universal density cap `K=2 sqrt(2)` for each normalized aggregate `Y_m,Z_m`. Put

`Y'=K Y_m`, `Z'=K Z_m`.

Then `Y',Z'` have densities bounded by one and

`Q = 2(1/K) X_0 Y' + (1/K^2) (Z')^2`.

Now apply the named OTHER-account theorem fleet02/B10, `QFORM-HYPERBOLIC-SQUARE-v1`: for independent density-`<=1` variables,

`2 a X Y + H(Y) + b(Z+theta(Y))^2`

has density at most `4/sqrt(|ab|)`. Here `a=1/K`, `b=1/K^2`, `H=theta=0`, so

`||p_Q||_infinity <= 4 K^(3/2) = 2^(17/4) < 19.1`,

uniformly in `m` and in all input laws.

Thus this family is a clean model of the correct hard mechanism: local minors go to zero and rank-three physical cross blocks do not exist, yet high-cardinality product-preserving aggregation reveals a uniformly smooth hyperbolic-square normal form.

## 6. What this says about the latest product-elliptic-trace residual

The latest fleet04/B19 candidate isolates a special product-origin graph trace. The results above show two things.

First, a substantial full-matrix basin is already closed without solving the general trace inequality: when the off-diagonal operator norm is at most `1/4`, the density cap is `pi sqrt(2)`.

Second, in the complementary strongly coupled branch, the trace proof cannot be reduced to either:

1. one uniformly nonsingular physical triple; or
2. one rank-three disjoint physical cross block.

The family `A_m` refutes both reductions while remaining uniformly controlled after aggregate variables are formed. Consequently any valid solution of the product-elliptic trace residual must preserve enough product structure to permit such aggregation before paying inverse-minor or inverse-singular-value costs.

A sharpened first missing implication is therefore:

**`QFORM-PRODUCT-ELLIPTIC-TRACE-AGGREGATE-v2`.** In the hard branch `||A-diag(A)||_op>1/4`, prove a dimension-free graph-trace/small-ball bound using original-coordinate product provenance in a form stable under high-cardinality aggregation. The lemma must include the family `A_m` above by reducing it to the aggregate hyperbolic-square channel, and it must not require a fixed rank-three cross block or a uniformly conditioned fixed principal triple.

For exact rank three, this aligns with fleet03/B19's localized-indefinite cross-aggregation residual and fleet01/B10's heavy-row Schur trichotomy: the difficult branch is a leverage-heavy, near-isotropic/minority-sign saddle where total coupling is dimension-free but individual coefficients can all be small. For general matrices, additional spectral components remain a separate interaction debt except in the near-diagonal basin proved here.

## 7. Honest status

`QFORM-NEAR-DIAGONAL-FULL-v1` is a proved target-level implication with arbitrary dimension and extra spectrum.

The family `A_m` is a proved algebraic counterexample to fixed-localization/cross-rank-three proof mechanisms, not to the quadratic-form conjecture. It is itself uniformly bounded by a direct application of the fleet02/B10 theorem after product-preserving aggregation.

The full conjecture remains **OPEN / NOT PROVED**. No universal constant for the full class is claimed, and the separate continuity conclusion remains open outside already controlled Fourier/convolution branches.
