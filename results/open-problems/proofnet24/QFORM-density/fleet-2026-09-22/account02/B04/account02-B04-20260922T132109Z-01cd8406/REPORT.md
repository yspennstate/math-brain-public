# account02/B04 — rank-three pivot bridge and leverage-heavy product rearrangement

Run: `account02-B04-20260922T132109Z-01cd8406`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, conditional route, and first unpaid implication

The target remains the full arbitrary-product-law statement: for every independent real `X_i` with densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound on the density of `X^T A X`, or give a genuine counterexample. No moment, compact-support, log-concavity, diagonal-basis, or post-rotation-independence assumption is used below.

A compact conditional route is now:

1. a rank-three curvature component whose physical spectral frame has maximum row leverage at most `1/2` is closed by the source-pinned diffuse product-space theorem, with explicit `3e |det Lambda|^{-1/3}`-type control;
2. if a physical scalar pivot is nonzero and its rank-two Schur range is diffuse, the completed account03/B04 Schur-pivot theorem gives a bounded density;
3. the new calculation below expresses every quantity in step 2 directly in the original rank-three spectral frame and proves an exact pivot-product identity;
4. what remains is a **global leverage-heavy aggregation/decomposition theorem** for arbitrary `A`: one must either find enough diffuse curvature or aggregate localized pivots/cross blocks without paying a tiny physical coefficient or one tiny principal minor.

The first unpaid implication is therefore not another local stationary-phase estimate. It is:

> `QFORM-HIGH-LEVERAGE-AGGREGATION`: starting only from the three-large-eigenvalue hypothesis, convert a leverage-heavy rank-three component (or the relevant rank-three piece of a higher-rank form) into either a diffuse rank-three block, a diffuse rank-two Schur pivot with a dimension-free product parameter, or a genuinely aggregated original-coordinate inequality. A single-pivot lower bound is insufficient.

The explicit Fourier-frame construction in Section 5 proves the last sentence quantitatively: all scalar pivots can be `delta/n` while the three spectral eigenvalues stay at `2+delta,-1,-1` and a dimension-free density bound remains available by the diffuse product-space theorem.

## 2. Source-pinned inputs and corrections

Fresh control before publication: `yspennstate/math-research-brain@556bbb0ae467b4f586505010af4da4cd99c5921e`, owner revision `2026-09-22.5`; owner README blob `433b2d57345823967480245b59a7c47d51019c37`; live correction-inbox blob `752bf867375ef2a2ddbd0cf8570e8370c4b38e79`.

The calculation respects all live corrections, in particular the false law-uniform one-dimensional pointwise oscillatory-decay claim, the fiber-sup dimension loss, the lack of independence after spectral rotation, the single-Schur-extraction failure, the conditional-cap failure, and the new local-cross/rank-three dichotomy counterexample. No refuted premise is used.

Named partner actually applied:

- `account03/B04`, canonical report `yspennstate/math-open-problems@f82e7bb9a6376c69615e136da4d1fc67343d46ef`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/a03-b04-20260922T125025Z-qform-r12/REPORT.md`, blob `b3504f05f6f75a6537327d5c213a235159cb781f`. Its theorem `QFORM-DIFFUSE-SCHUR-PIVOT-v1` says that for an original-coordinate scalar pivot `a!=0`, rank-two Schur complement with nonzero eigenvalues `mu_1,mu_2`, and Schur-range row leverage at most `1/2`,

  `||p_Q||_infinity <= 4 sqrt(3e) |a|^{-1/2}|mu_1 mu_2|^{-1/4}`.        (2.1)

The partner proof uses product-space Brascamp--Lieb/Hausdorff--Young and a source-pinned dependent-square `L^3` smoothing lemma; it does not assume rotated-coordinate independence.

Compatible diffuse theorem actually applied:

- `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, canonical report `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, path `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`, blob `d08d2488c072386e2b8ad818e30b1a6dec79e63a`. For rank `r>=3`, orthonormal-column frame `U` with row leverages `c_i<=1/2`, arbitrary coordinate-separable phases, and invertible `Lambda`, it gives

  `||p||_infinity <= [r/(r-2)] B(U)^{2/r}|det Lambda|^{-1/r}`,

  `B(U)=prod_i (1-c_i)^{-(1-c_i)/2}`.                            (2.2)

This run uses (2.2) only at its proved scope; the full conjecture remains open.

## 3. Exact rank-three scalar-pivot identity

### Theorem 3.1 — `QFORM-RANK3-PIVOT-TRANSFER-v1`

Let `A=U Lambda U^T` have rank exactly three, where `U` is `n x 3` with `U^T U=I_3` and `Lambda` is an invertible real symmetric `3 x 3` matrix. Let `u_i` be row `i` of `U`, put

`r_i=||u_i||_2^2`,

`a_i=u_i Lambda u_i^T=A_{ii}`,

and suppose `a_i!=0`. For `j!=i` define the conditional/projected row leverage

`c_{j|i}=||u_j||_2^2-(u_j u_i^T)^2/r_i`.                        (3.1)

Then the Schur complement of the scalar pivot `a_i` has rank exactly two. If its nonzero eigenvalues are `mu_1,mu_2`, then

`boxed(mu_1 mu_2 = det(Lambda) r_i/a_i.)`                       (3.2)

Moreover its two-dimensional range projector has diagonal entries exactly `c_{j|i}`. Consequently, if

`max_{j!=i} c_{j|i} <= 1/2`,                                    (3.3)

then for arbitrary independent input densities bounded by one,

`boxed(||p_{X^TAX}||_infinity
 <=4 sqrt(3e) (|det Lambda| r_i |a_i|)^{-1/4}. )`                (3.4)

This is an actual application of the completed account03/B04 theorem (2.1), not a restatement of its conclusion.

### Proof

Permute coordinates so that `i` is last and write `U=(U_0;u)` with `u=u_i`. Partition

`A=[[C,b],[b^T,a]]`, `a=a_i`.

Since `C=U_0 Lambda U_0^T` and `b=U_0 Lambda u^T`, the Schur complement is

`S=C-bb^T/a = U_0 M U_0^T`,                                    (3.5)

where

`M=Lambda-Lambda u^T u Lambda/a`.                               (3.6)

Directly, `M u^T=0`. Because `M` is symmetric, its range is `u^perp`. Also

`U_0^T U_0=I_3-u^T u`.                                         (3.7)

For every `v,w in u^perp`, (3.7) gives

`<U_0v,U_0w>=<v,w>`.

Thus `U_0` is an isometry on `u^perp`, and the two nonzero eigenvalues of `S` are exactly the two eigenvalues of `M` restricted to `u^perp`.

To compute their product, use the determinant lemma with a scalar regularizer `t`:

`det(M+tI)
 =det(Lambda+tI)
  [1-a^{-1} u Lambda (Lambda+tI)^{-1} Lambda u^T].`              (3.8)

The bracket vanishes at `t=0` because `u Lambda u^T=a`. Its derivative at zero is

`a^{-1} ||u||_2^2 = r_i/a`,                                    (3.9)

since

`d/dt [Lambda(Lambda+tI)^{-1}Lambda]_{t=0}=-I`.

As `M` has rank two, the derivative of `det(M+tI)` at zero is exactly the product of its two nonzero eigenvalues. Equations (3.8)--(3.9) prove (3.2).

For the range leverage, the orthogonal projector onto `u^perp` is

`P=I_3-u^T u/r_i`.

Because `U_0:u^perp -> range(S)` is an isometry, the range projector of `S` is `U_0 P U_0^T`. Its `j`-th diagonal entry is

`u_j P u_j^T = ||u_j||^2-(u_j u_i^T)^2/r_i=c_{j|i}`,            (3.10)

which proves the leverage assertion. Under (3.3), the account03/B04 theorem (2.1) applies to the **actual Schur complement (3.5)**. Substituting (3.2) into (2.1) gives

`4 sqrt(3e)|a_i|^{-1/2}
 (|det Lambda|r_i/|a_i|)^{-1/4}
 =4 sqrt(3e)(|det Lambda|r_i|a_i|)^{-1/4}`,

which is (3.4). QED.

### What this pays

The theorem removes the need to diagonalize or numerically inspect each rank-two Schur complement. In rank exactly three, both its determinant scale and its product-space leverage are explicit functions of the original spectral frame. The first global question is now purely structural: find/aggregate a pivot with (3.3) and non-negligible `r_i|a_i|`, or switch to a diffuse/full-frame mechanism.

## 4. A leverage-heavy exact-threshold rotated indefinite family

The new transfer theorem closes a branch where the rank-three diffuse theorem (2.2) does **not** apply.

Fix `rho in (1/2,1)` and put `alpha=sqrt(1-rho)/2`. Let `U_rho` have rows

`u_0=(sqrt(rho),0,0)`,

`u_1=( alpha, 1/2, 1/2)`,

`u_2=(-alpha, 1/2,-1/2)`,

`u_3=(-alpha,-1/2, 1/2)`,

`u_4=( alpha,-1/2,-1/2)`.

A direct calculation gives `U_rho^T U_rho=I_3`. Take

`Lambda=diag(1,1,-1)`, `A_rho=U_rho Lambda U_rho^T`.             (4.1)

The nonzero eigenvalues are exactly `{1,1,-1}`. Hence the form lies at the sharp spectral threshold and is indefinite.

The original rank-three row leverages are

`r_0=rho`,

`r_1=...=r_4=(3-rho)/4`.

For every `rho in (1/2,1)`, all five are strictly bigger than `1/2`; therefore the rank-three diffuse theorem cannot be invoked on this spectral frame. Nevertheless pivoting the original coordinate `0` gives

`a_0=rho`,

and the Schur range is generated by the last two spectral coordinates, whose four row leverages are **exactly `1/2`**. Theorem 3.1 therefore gives

`boxed(||p_{X^T A_rho X}||_infinity <=4 sqrt(3e/rho).)`          (4.2)

This is uniform over all independent input laws with densities bounded by one.

### Fully explicit `rho=3/4` matrix

At `rho=3/4`,

`A_* =
[[3/4, sqrt(3)/8,-sqrt(3)/8,-sqrt(3)/8, sqrt(3)/8],
 [sqrt(3)/8,1/16,7/16,-9/16,1/16],
 [-sqrt(3)/8,7/16,1/16,1/16,-9/16],
 [-sqrt(3)/8,-9/16,1/16,1/16,7/16],
 [sqrt(3)/8,1/16,-9/16,7/16,1/16]].`                            (4.3)

Every diagonal entry and every off-diagonal entry in (4.3) is nonzero, while the spectrum is `{1,1,-1,0,0}`. Thus this is genuinely rotated and fully coupled in the original independent coordinates, not a disguised diagonal or disjoint-block example.

Its pivot Schur complement is

`S=
[[0,1/2,-1/2,0],
 [1/2,0,0,-1/2],
 [-1/2,0,0,1/2],
 [0,-1/2,1/2,0]],`                                              (4.4)

with nonzero eigenvalues `1,-1`. In fact

`w^T S w=(w_1-w_4)(w_2-w_3)`,                                  (4.5)

so the logarithmic rank-two indefinite control is visible rather than suppressed. The completed square is

`X^T A_* X
 =(W_1-W_4)(W_2-W_3)
 +(3/4)[X_0+(sqrt(3)/6)(W_1-W_2-W_3+W_4)]^2.`                   (4.6)

The two factors in (4.5) are independent differences of disjoint coordinate pairs and each has density at most one; however the square shift in (4.6) is correlated with those differences. The account03/B04 dependent-square mechanism is therefore the correct product-space tool: it retains the original product provenance without asserting conditional independence of the transformed variables.

Equation (4.2) at `rho=3/4` becomes the explicit estimate

`boxed(||p_{X^T A_* X}||_infinity <=8 sqrt(e) <13.190.)`        (4.7)

This is the requested explicit estimate for a genuinely rotated indefinite exact-threshold form.

## 5. Quantitative counterexample to a single-pivot lower-bound strategy

A scalar-pivot route cannot be made universal merely by proving that some physical diagonal entry is nonzero or by lower-bounding one such entry from the spectral hypothesis.

For every integer `n>=6`, let `theta_j=2pi j/n`, `j=0,...,n-1`, and define the real Fourier frame

`u_j=(1/sqrt(n), sqrt(2/n) cos(theta_j), sqrt(2/n) sin(theta_j)).` (5.1)

Then `U_n^T U_n=I_3` and every row leverage is exactly `3/n`. For `delta>=0`, put

`Lambda_delta=diag(2+delta,-1,-1)`,

`A_{n,delta}=U_n Lambda_delta U_n^T`.                             (5.2)

The nonzero spectrum is exactly `{2+delta,-1,-1}`, while the original-coordinate entries are explicitly

`(A_{n,delta})_{jk}
 =[2+delta-2 cos(2pi(j-k)/n)]/n`.                                (5.3)

In particular every scalar pivot is

`(A_{n,delta})_{jj}=delta/n`.                                   (5.4)

At `delta=0` **every physical scalar pivot vanishes**, although the form has the exact target spectrum `{2,-1,-1}`. For `delta>0` every pivot is nonzero but arbitrarily small as either `delta downarrow0` or `n to infinity`.

For a fixed pivot `i`, (3.1) becomes

`c_{j|i}
 = [3-(1+2cos(theta_j-theta_i))^2/3]/n
 <=3/n<=1/2`.                                                    (5.5)

Thus Theorem 3.1 really does apply for `delta>0`, but its scalar-pivot estimate is

`||p||_infinity
 <=4 sqrt(3e) n^{1/2}[3 delta(2+delta)]^{-1/4}.`                 (5.6)

The right side diverges like `sqrt(n) delta^{-1/4}` despite the fixed three-large-eigenvalue hypothesis.

The same family is globally diffuse, so the source-pinned product-space theorem (2.2) gives instead, including at `delta=0`,

`B(U_n)=(1-3/n)^{-(n-3)/2}`,

hence

`boxed(||p_{X^T A_{n,delta}X}||_infinity
 <=3(1-3/n)^{-(n-3)/3}(2+delta)^{-1/3}. )`                       (5.7)

In particular

`||p||_infinity <=3e (2+delta)^{-1/3}`                          (5.8)

uniformly in `n`. Equations (5.6)--(5.8) are a source-valid mechanism counterexample: **the problem is not the quadratic form but the attempt to pay for it through one physical scalar pivot**. A correct full proof must switch to a diffuse product-space estimate or aggregate pivots before taking reciprocal powers.

This is consistent with, and quantitatively strengthens the lesson of, the live `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` corrections; it is not a counterexample to the QFORM conjecture.

## 6. Product-rearrangement interpretation

The run deliberately avoids the known false inference

`|E exp(it lambda X^2)| <= C |t lambda|^{-1/2}`

for arbitrary density-`<=1` inputs. The valid estimates use two different product-space mechanisms:

1. in the leverage-heavy family (4.1), the rank-two Schur range satisfies the exact Brascamp--Lieb leverage threshold; account03/B04 first obtains an `L^3` density bound for the indefinite rank-two base and then smooths it with the translated original-coordinate square;
2. in the Fourier family (5.2), all three spectral directions are globally diffuse and the complex product amplitude is controlled before the quadratic Fresnel integration.

Both mechanisms are compatible with arbitrary fragmented input densities. No centered-interval rearrangement, moment condition, or rotated-coordinate independence is inserted.

A useful exact structural quantity emerging from Theorem 3.1 is

`Pi_i := |det Lambda| r_i |a_i|`.                               (6.1)

Whenever the projected Schur frame is diffuse, the density cost is only `Pi_i^{-1/4}`. The open aggregation problem can therefore be phrased sharply: control a suitable mixture of `Pi_i` and projected leverage failures, rather than trying to lower-bound one `|a_i|` or one principal determinant.

## 7. Exact symbolic verification used in this run

The following finite computation was used only to verify the algebra of the explicit matrix (4.3); it is not a proof certificate for the analytic inequality.

```python
import sympy as sp
U=sp.Matrix([
 [sp.sqrt(3)/2,0,0],
 [sp.Rational(1,4), sp.Rational(1,2), sp.Rational(1,2)],
 [-sp.Rational(1,4),sp.Rational(1,2),-sp.Rational(1,2)],
 [-sp.Rational(1,4),-sp.Rational(1,2),sp.Rational(1,2)],
 [sp.Rational(1,4),-sp.Rational(1,2),-sp.Rational(1,2)]])
L=sp.diag(1,1,-1)
A=sp.simplify(U*L*U.T)
a=A[0,0]; b=A[1:,0]; C=A[1:,1:]
S=sp.simplify(C-b*b.T/a)
print(U.T*U)
print(A)
print(A.eigenvals())
print(S)
print(S.eigenvals())
```

Exact output:

```text
Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
Matrix([
[3/4, sqrt(3)/8, -sqrt(3)/8, -sqrt(3)/8, sqrt(3)/8],
[sqrt(3)/8, 1/16, 7/16, -9/16, 1/16],
[-sqrt(3)/8, 7/16, 1/16, 1/16, -9/16],
[-sqrt(3)/8, -9/16, 1/16, 1/16, 7/16],
[sqrt(3)/8, 1/16, -9/16, 7/16, 1/16]])
{-1: 1, 1: 2, 0: 2}
Matrix([[0,1/2,-1/2,0],[1/2,0,0,-1/2],[-1/2,0,0,1/2],[0,-1/2,1/2,0]])
{-1: 1, 1: 1, 0: 2}
```

The numerical value in (4.7) is `8 sqrt(e)=13.1897701656...`.

## 8. Full-target status and next derivation

Status is `ESSENTIAL_STEP_APPLIED`, not a full proof. The new theorem pays one leverage-heavy rank-three branch exactly and turns the partner Schur bound into an invariant original-frame inequality. The Fourier-frame family proves that one cannot finish by forcing a dimension-free scalar-pivot lower bound.

The next concrete derivation is to attack the remaining leverage-heavy flag:

- choose a row `i` with `r_i>1/2`;
- if `a_i!=0` and `max_j c_{j|i}<=1/2`, Theorem 3.1 closes it;
- otherwise a second row has projected leverage `>1/2` or the pivot is near-isotropic. The unpaid step is to use the resulting fixed-row wedge budget together with product rearrangement to aggregate the heavy second direction, rather than selecting one tiny `3x3` minor.

For higher-rank `A`, one additionally needs a product-preserving way to isolate such a rank-three curvature component while treating the remainder by an allowed separable/conditioned mechanism. No claim is made that the present rank-three theorem supplies that decomposition.

No full-solution, continuity-beyond-proved-branches, or novelty claim is made.
