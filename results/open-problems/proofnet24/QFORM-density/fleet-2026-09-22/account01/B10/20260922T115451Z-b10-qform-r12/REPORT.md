# account01/B10 — rank-three coupled case: heavy-row Schur smoothing

**Run:** `20260922T115451Z-b10-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.5`  
**Assignment:** `Rank-three coupled case` / GEOMETRY  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 0. Fresh-control pivot and exact source state

The invocation arrived with an obsolete FEI order. Fresh `math-research-brain/main` instead assigns all workers to the quadratic-form density conjecture and explicitly suspends FEI. The source version used at startup was `a98dedb8b1cde2236af52747273866300a3a24f9`; immediately before scientific delivery the control was re-resolved at `21f8b8cdde140cba387de73334c93ed02a671fda`. Both carry OWNER CONTROL revision `2026-09-22.5` and the same target.

The target is: for independent real random variables `X_1,...,X_n` with probability densities `0<=f_i<=1`, and real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has an essentially bounded density with one universal bound, or give a valid counterexample.

This B10 report addresses the assigned **rank-exactly-three coupled subproblem**. It does not treat arbitrary extra nonzero eigenvalues and therefore is not a full solution.

Required standing corrections consumed:

1. `QFORM-POINTWISE-DECAY-FALSE`: arbitrary density-`<=1` laws can be phase aligned, so law-uniform pointwise one-dimensional quadratic stationary-phase decay is false.
2. `QFORM-FIBER-SUP-DIMENSION-LOSS`: naive spectral-fiber supremum integration can lose dimension.
3. `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: spectral coordinates are generally dependent.
4. Fresh event `QFORM-CROSSMINOR-ALONE-FALSE` from account02/B09: a nonsingular cross block alone does not force bounded density without a suitable pivot-side condition. This is used below to keep the new heavy-pair resource from being incorrectly promoted to a closure theorem.

No refuted pointwise Fresnel estimate, no independence after spectral rotation, and no reciprocal-minor linear averaging are used.

## 1. Peer results actually consumed

### 1.1 Diffuse-frame theorem, account02/B08

Canonical source:

`yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T113624Z-qform11/REPORT.md`

It proves: if `A=U Lambda U^T` has rank exactly `3`, `U^TU=I_3`, all `|lambda_k|>=1`, and every spectral-row leverage `||u_j||^2<=1/2`, then

`||p_Q||_infinity <= 3e`.

The mechanism is a two-stage Fourier–Brascamp–Lieb / Fresnel argument and keeps the original product structure before projection.

### 1.2 Named partner account02/B10

Canonical source:

`yspennstate/math-open-problems@1eba911614ef9f6683f8eacb5d6608a0f9a4b833`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`

The partner proves the exact physical-space theorem

`T=2aXY+H(Y)+b(Z+theta(Y))^2  =>  ||p_T||_infinity <= 4/sqrt(|ab|)`

for independent density-`<=1` variables and arbitrary measurable shifts. It also gives a source-valid Walsh obstruction to naively averaging local reciprocal Pluecker/minor bounds.

The present report uses that result in the rank-three decision tree: partner smoothing closes triangular hyperbolic-square physical triples, while the new theorem below closes a complementary **spectral-heavy but residual-diffuse** branch before paying any reciprocal physical minor. The partner's Walsh falsifier is exactly why the residual heavy-pair alternative below is recorded as a structural resource rather than averaged linearly.

## 2. Setup for one leverage-heavy physical coordinate

Let

`A=U Lambda U^T`,

where `U` is `n x 3` with orthonormal columns and

`Lambda=diag(lambda_1,lambda_2,lambda_3)`, `|lambda_k|>=1`.

Write `u_j^T` for row `j` of `U`. Thus

`sum_j u_j u_j^T = I_3`.

Assume a row `u=u_i` is leverage-heavy:

`c:=||u||^2 > 1/2`.

Put

`e=u/sqrt(c)`, `P=I-ee^T`, `alpha=e^T Lambda e`, `a=u^T Lambda u=c alpha`.

For every `j != i`, define the residual two-dimensional row

`w_j=P u_j`, `d_j=||w_j||^2`.

Because `Pu=0`,

`sum_{j != i} w_j w_j^T = P`.

After identifying `e^perp` with `R^2`, the `w_j` therefore form an exact Parseval frame and

`sum_{j != i} d_j=2`.

The branch attacked first is the residual-diffuse case

`d_j <= 1/2` for all `j != i`.

## 3. Exact Schur complement after completing the heavy coordinate

Write

`z=sum_{j != i} u_j X_j`.

Then

`Q=(u X_i+z)^T Lambda (u X_i+z)`

` = a (X_i + (u^T Lambda z)/a)^2 + R`,

provided `a != 0`, where

`R=z^T S z`,

`S=Lambda - (Lambda u u^T Lambda)/a`.

Since `Su=0` and `S` is symmetric, `R` depends only on the residual projection

`W=Pz=sum_{j != i} w_j X_j in e^perp`.

Thus there is a nonsingular two-dimensional symmetric operator `S_perp` on `e^perp` such that

`R=W^T S_perp W`.

To identify its determinant, use the orthogonal basis with first vector `e` and write

`Lambda = [[alpha, beta^T],[beta,C]]`.

Then

`S_perp=C-beta beta^T/alpha`.

The block determinant identity gives the exact formula

`det S_perp = det Lambda / alpha`.

Therefore, with

`D:=|det S_perp|=|det Lambda|/|alpha|`,

we have

`D>=1`.

Indeed if `M=max_k |lambda_k|`, then `|alpha|<=M`, while `|det Lambda|>=M` because the other two eigenvalue magnitudes are each at least `1`.

This determinant identity was independently stress-checked numerically on random indefinite and definite `3x3` diagonal `Lambda` and random directions; the maximum floating discrepancy in 100 trials was below `3.2e-13`. The proof above is exact and does not depend on the check.

## 4. Residual diffuse frame has a dimension-free Wiener bound

Assume `d_j<=1/2` for all `j != i`. Let `g` denote the density of

`W=sum_{j != i} w_j X_j in R^2`.

The account02/B08 Brascamp–Lieb calculation applies verbatim in dimension two. For nonzero `w_j`, put

`v_j=w_j/sqrt(d_j)`.

Then

`sum d_j v_j v_j^T=I_2`.

Geometric rank-one Brascamp–Lieb followed by sharp Hausdorff–Young at exponent `q_j=1/d_j>=2`, using `0<=f_j<=1` and `int f_j=1`, yields

`||hat g||_1 <= (2pi)^2 e`.                                             (4.1)

This is an averaged Fourier statement; it does not resurrect the refuted law-uniform pointwise one-dimensional decay claim.

## 5. The two-dimensional Schur remainder has an L^3 density

For

`R=W^T S_perp W`,

Gaussian-regularized Fresnel inversion combined with (4.1) gives, for `t !=0`,

`|phi_R(t)| <= e pi D^(-1/2) |t|^(-1)`.

Set

`K=e pi D^(-1/2)`.

Together with `|phi_R(t)|<=1`,

`|phi_R(t)|<=min(1,K/|t|)`.

Hence

`int_R |phi_R(t)|^(3/2) dt <= 6K`.                                    (5.1)

The inverse Fourier transform maps `L^(3/2)` to `L^3` with the elementary interpolation constant `(2pi)^(-2/3)` in the convention `hat f(t)=int e^{-itx}f(x)dx`. Thus the law of `R` has an `L^3` density `p_R` satisfying

`||p_R||_3 <= (2pi)^(-2/3) (6K)^(2/3)`

`             = (3e)^(2/3) D^(-1/3)`.                                (5.2)

No bounded density for the rank-two remainder is asserted: an indefinite rank-two quadratic can have a logarithmic singularity. The `L^3` conclusion is exactly the amount of smoothing used next.

## 6. Main theorem: heavy square + residual diffuse Schur remainder

### Theorem 6.1 — `QFORM-HEAVY-ROW-SCHUR-DIFFUSE-v1`

Under the setup above, suppose

1. `c=||u_i||^2>1/2`;
2. `alpha=e^T Lambda e !=0`;
3. every residual leverage satisfies `d_j=||P u_j||^2<=1/2` for `j != i`.

Then `Q=X^TAX` has an essentially bounded density, with

`||p_Q||_infinity`

` <= |a|^(-1/2) [1 + (12e)^(2/3) D^(-1/3)]`,                         (6.1)

where

`a=c alpha`, `D=|det Lambda|/|alpha|`.

Equivalently,

`||p_Q||_infinity`

` <= (c|alpha|)^(-1/2)`
`    * [1 + (12e)^(2/3)(|alpha|/|det Lambda|)^(1/3)]`.                (6.2)

In particular, because `D>=1`, if

`|alpha|>=1/2`,

then

`||p_Q||_infinity < 2 [1+(12e)^(2/3)] < 22.419`.                     (6.3)

#### Proof

Condition on all variables except `X_i`. The completed-square representation is

`Q=a(X_i+s)^2+R`,

where the shift `s=(u^T Lambda z)/a` is now fixed. Translation does not affect the cap on the density of `X_i`. Therefore the conditional density of `a(X_i+s)^2` is bounded on the sign-compatible half-line by

`|a|^(-1/2) |v|^(-1/2)`.

Averaging over the other variables gives, for every output point `y`,

`p_Q(y) <= |a|^(-1/2) int_0^infinity s^(-1/2) p_R(y-sgn(a)s) ds`.     (6.4)

Split at `s=1`. On `(0,1)`, Holder with exponents `3` and `3/2` and (5.2) gives

`int_0^1 s^(-1/2)p_R(y-sgn(a)s)ds`

` <= ||p_R||_3 (int_0^1 s^(-3/4)ds)^(2/3)`

` <= (3e)^(2/3)D^(-1/3) 4^(2/3)`

` = (12e)^(2/3)D^(-1/3)`.                                           (6.5)

On `(1,infinity)`, `s^(-1/2)<=1`, so the contribution is at most the total mass of `p_R`, namely `1`. Substitution into (6.4) proves (6.1). Since `c>1/2`, `|alpha|>=1/2` implies `|a|>1/4`; using `D>=1` gives (6.3). `QED`.

The decimal constant in (6.3) is `22.4180289052...`.

## 7. Structural heavy-row trichotomy

The theorem combines with elementary frame geometry to give a useful exact decision tree.

### Proposition 7.1 — `QFORM-RANK3-HEAVY-TRICHOTOMY-v1`

Fix any leverage-heavy row `u_i`, `c>1/2`. Then at least one of the following occurs.

**(A) Residual diffuse and non-isotropic.**  
All `d_j<=1/2` and `|alpha|>=1/2`. Then Theorem 6.1 closes this rank-three form with the universal bound `<22.419`.

**(B) Residual frame contains a second heavy direction.**  
Some `j !=i` has `d_j>1/2`. Then the spectral row pair has quantitative Gram area

`det Gram(u_i,u_j)=c d_j > 1/4`.                                      (7.1)

Moreover, by Parseval,

`sum_{k != i,j} det[u_i;u_j;u_k]^2 = det Gram(u_i,u_j) >1/4`.         (7.2)

This is a dimension-free **aggregate** triple-volume resource. It is not, by itself, a bounded-density theorem.

**(C) Residual diffuse but near-isotropic at the heavy row.**  
All `d_j<=1/2` and `|alpha|<1/2`. In the block representation of `Lambda`,

`Lambda=[[alpha,beta^T],[beta,C]]`,

one has the strong cross-coupling estimate

`||beta|| > sqrt(3)/2`.                                               (7.3)

Indeed `Lambda^2 >= I` in the positive-semidefinite order because every eigenvalue magnitude is at least `1`; hence

`1 <= ||Lambda e||^2=alpha^2+||beta||^2`,

and `|alpha|<1/2` gives (7.3).

#### Proof of (7.1)-(7.2)

Since `w_j=P u_j`, the squared area of the parallelogram spanned by `u_i,u_j` is

`||u_i||^2 ||P u_j||^2 = c d_j`.

For `a_vec=u_i cross u_j`,

`sum_k det[u_i;u_j;u_k]^2`

`=sum_k (a_vec dot u_k)^2`

`=a_vec^T (sum_k u_k u_k^T) a_vec`

`=||a_vec||^2=c d_j`.

The `k=i,j` terms vanish, proving (7.2).

## 8. What the named partner and the fresh correction now imply

The partner account02/B10 theorem closes any physical triangular hyperbolic-square triple before one ever pays a reciprocal determinant average. Thus a surviving rank-three counterexample must avoid both:

- the diffuse global Fourier–Brascamp–Lieb branch;
- the new heavy-row Schur-diffuse/non-isotropic branch;
- every physical triple to which `QFORM-HYPERBOLIC-SQUARE-v1` applies with dimension-free `|ab|`;
- known definite physical-pair / nonsingular principal-triple closure branches from the current team state.

The fresh account02/B09 correction is essential when interpreting alternative (B). A large spectral pair area or nonsingular cross minor **alone** is not a license to condition and claim bounded density: their explicit two-large-eigenvalue counterexample has a nonsingular cross block but a logarithmic output singularity. Therefore (7.1)-(7.2) must be coupled to either a valid pivot-side condition, partner hyperbolic-square smoothing, or an operator-level aggregate argument. No false cross-minor closure is claimed here.

Likewise the partner's flat-Walsh Pluecker calculation shows that (7.2) cannot be converted into a universal estimate by selecting/averaging local constants proportional to an inverse square root of individual minor weight. The aggregation must happen before reciprocal-minor payment.

## 9. Compact conditional end-to-end route and first unpaid implication

For rank exactly three:

1. If all spectral-row leverages are `<=1/2`, account02/B08 gives `||p_Q||_infinity<=3e`.
2. Otherwise select a heavy row.
3. If its residual two-frame is diffuse and `|alpha|>=1/2`, Theorem 6.1 gives `||p_Q||_infinity<22.419`.
4. If a partner-type triangular hyperbolic-square physical triple appears, account02/B10 closes it with `4/sqrt(|ab|)`.
5. Therefore the genuinely unresolved rank-three geometry can be forced into the union of:
   - **two-heavy-frame resource:** a row pair with spectral area squared `>1/4`, but no admissible local pivot theorem yet;
   - **near-isotropic heavy row:** residual diffuse frame and `|alpha|<1/2`, which necessarily carries cross coupling `||beta||>sqrt(3)/2`.

The first essential missing implication is therefore narrower than the previous generic heavy/light statement:

### `QFORM-HEAVY-PAIR-OR-ISOTROPIC-SPLICE-v1`

Prove a dimension-free density/small-ball estimate in alternatives (B) and (C), using the aggregate product structure **before** paying any reciprocal local minor, and respecting `QFORM-CROSSMINOR-ALONE-FALSE`. In branch (C), exploit the quantitative cross coupling `||beta||>sqrt(3)/2`; in branch (B), exploit the aggregate triple-volume identity (7.2) together with a valid pivot-side or hyperbolic-square mechanism.

Even a complete proof of this splice would close only **rank exactly three**. The owner target permits additional nonzero eigenvalues of arbitrary small magnitude; handling those without treating the spectral remainder as independent noise remains a separate full-target obstruction.

## 10. Status and integrity

- Full owner conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- `QFORM-HEAVY-ROW-SCHUR-DIFFUSE-v1`: **PROVED SUPPORTING THEOREM**.
- `QFORM-RANK3-HEAVY-TRICHOTOMY-v1`: **PROVED STRUCTURAL REDUCTION**.
- Named partner `QFORM-HYPERBOLIC-SQUARE-v1`: consumed and applied as a complementary closure branch.
- Fresh `QFORM-CROSSMINOR-ALONE-FALSE`: consumed and enforced; no cross-minor-alone claim is made.
- No numerical experiment is used as proof. The random determinant check is only a regression check of an exact symbolic identity.
- No projected-coordinate independence assumption is used.
- No law-uniform pointwise oscillatory decay is used.
- No public release, paid/remote model, email, Drive, workflow, scheduler mutation, permission change, or unrelated private data is involved.

**Next recipient:** rank-three / universal-proof synthesis workers, with special relevance to workers attacking bilinear blocks, coordinate minors, and B19/B20 integration.
