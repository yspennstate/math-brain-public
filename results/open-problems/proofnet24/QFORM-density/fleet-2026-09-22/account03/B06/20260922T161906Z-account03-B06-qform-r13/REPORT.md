# account03/B06 — heavy-pivot all-second-minors-zero closure

**Run:** `20260922T161906Z-account03-B06-qform-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration / quantitative inequalities  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_BRANCH_CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write was authenticated, but no native learned-memory receiver/ingestion was verified.

## 0. Fresh control and correction state

The run began from owner revision `2026-09-22.5`. A required prepublication refresh found the later owner control revision **`2026-09-22.6`**. The research target and B06 assignment are unchanged: all research remains exclusively on the quadratic-form bounded-density conjecture, and B06 remains `Curved fiber integration`. The later revision therefore supersedes only the control revision metadata, not the mathematics below.

The exact target remains: independent real coordinates `X_i` with probability densities `0<=f_i<=1`; real symmetric `A` with at least three eigenvalues of absolute value at least one; prove one universal bound on the essential density of `Q=X^TAX`, or produce a valid counterexample. Continuity is tracked separately.

The live correction inbox was reread through the current `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`. In particular this proof does **not** use: law-uniform pointwise quadratic-phase decay, post-rotation independence, unrestricted fiber suprema, generic X-ray-only two-sheet control, conditional caps created by spectral conditioning, or a universal good fixed minor. The newest `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1` is directly relevant: it shows that the preceding B06 two-pivot endpoint cannot simply be averaged against same-sign Pluecker mass. The present run therefore changes mechanism and treats the maximally singular second-pivot branch directly.

### Completed results actually consumed

1. account02/B06, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical report `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, proves that a unit one-dimensional linear projection of an arbitrary cap-one product law has density at most `e^(1/2)` (the `k=1` specialization of its product-fiber Brascamp--Lieb theorem). This is used at an actual inequality in Section 2.
2. account04/B18, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical report `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, supplies the source-valid square-kernel domination used in Section 4 without manufacturing independence after square completion.
3. Own predecessor account03/B06, `QFORM-RANK3-TWO-PIVOT-ENDPOINT-v1`, canonical report `yspennstate/math-open-problems@8624700dc9342807bbdf427e271fffcc518a0315`, handles a rank-three form once one physical scalar pivot and one nonzero second physical pivot determinant are quantitatively paid.

The exact assigned partner `account04/B06` still had no completed current-QFORM handoff/check-in or canonical current-QFORM report visible at startup or the partner refresh, so no result or PASS is fabricated. Work continued asynchronously as instructed; the compatible completed account04/B18 theorem above was used instead.

## 1. First unpaid implication attacked

Let

`A=R Lambda R^T`, `R^T R=I_3`,                                      (1.1)

have **exact rank three**, with the three nonzero eigenvalues `lambda_1,lambda_2,lambda_3` satisfying `|lambda_j|>=1`. For a physical coordinate `i`, put

`a=A_ii`, `ell_i=||r_i||^2`,                                        (1.2)

where `r_i` is row `i` of `R`, and for `k!=i` put

`d_ik=A_ii A_kk-A_ik^2`.                                            (1.3)

The preceding B06 theorem uses a pair with `a d_ik !=0`. The strongest possible failure of that second-pivot mechanism, after a nonzero first pivot, is

`d_ik=0 for every k!=i`.                                             (1.4)

The main result below closes this entire branch **uniformly whenever the first pivot row is heavy**, `ell_i>1/2`. The mechanism is not another fixed pair. It first identifies the whole rank-two Schur remainder as an exact hyperbolic product of two independent coordinate banks and then proves that the spectral threshold itself pays the remaining scalar factor.

## 2. A product-density lemma with the rare logarithm retained

### Lemma 2.1 — `QFORM-INDEPENDENT-PRODUCT-L3-v1`

Let `U,V` be independent real random variables whose densities are bounded by `H`. Let `Z=UV`. Then `Z` has a density `h` and, for `z!=0`,

`h(z) <= 2 H^2 [1+log_+(1/(H^2 |z|))]`,                             (2.1)

and

`||h||_3^3 <= 260 H^4`.                                              (2.2)

#### Proof

The standard product change of variables gives

`h(z)=int_R f(u) g(z/u) du/|u|`.                                    (2.3)

Put `R_0=1/H`. On `|u|>=R_0`,

`int f(u)g(z/u)du/|u| <= H/R_0=H^2`.                                (2.4)

On `|u|<R_0`, substitute `v=z/u`. With `alpha=H|z|`,

`int_(|u|<R_0) ... <= H int_(|v|>alpha) g(v)dv/|v|`.                 (2.5)

If `alpha<1/H`, split at `|v|=1/H`. The middle part is at most

`2H log(1/(H alpha))`,

while the tail is at most `H` because `int g=1`. If `alpha>=1/H`, the same term is at most `H/alpha<=H`. Combining with (2.4) gives (2.1).

On `|z|>=H^(-2)`, (2.1) gives `h<=2H^2`, hence

`int_(|z|>=H^-2) h^3 <=4H^4 int h <=4H^4`.                           (2.6)

On `|z|<H^(-2)`, cube (2.1), scale `s=H^2|z|`, and use

`int_0^1 [1+log(1/s)]^3 ds
 =int_0^infinity (1+t)^3 e^(-t)dt=16`.                               (2.7)

The two signs contribute at most `256H^4`. Adding (2.6) proves (2.2). `QED`

The logarithm is explicit rather than hidden in a false continuity estimate; it is exactly the harmless hyperbolic singularity expected from a product.

## 3. Rank-two zero-diagonal forms are an exact independent product

### Theorem 3.1 — `QFORM-RANK2-ZERODIAG-L3-v1`

Let `S` be a real symmetric matrix of exact rank two acting on independent cap-one original coordinates, and suppose

`S_jj=0 for every physical coordinate j`.                            (3.1)

Then the two nonzero eigenvalues of `S` are `+beta,-beta` for some `beta>0`, and the quadratic variable `R=X^T S X` has an `L^3` density satisfying

`||p_R||_3 <= C_0 beta^(-2/3)`,                                      (3.2)

with

`C_0=(65 e^2)^(1/3)<7.832`.                                          (3.3)

#### Proof

Since `tr S=0` and `rank S=2`, its nonzero eigenvalues are `+beta,-beta`. Let `v,w` be corresponding orthonormal eigenvectors and set

`u=(v+w)/sqrt(2)`, `q=(v-w)/sqrt(2)`.                                (3.4)

Then `u,q` are orthonormal and

`S=beta(u q^T+q u^T)`.                                               (3.5)

The diagonal condition says

`0=S_jj=2 beta u_j q_j` for every j.                                 (3.6)

Thus the supports of `u` and `q` are disjoint. Consequently

`U=u.X`, `V=q.X`                                                     (3.7)

are functions of disjoint sets of the original independent coordinates, hence are genuinely independent; no rotated-independence assertion is being made.

Now apply account02/B06's completed weighted affine-fiber Brascamp--Lieb theorem in dimension one to the two unit coefficient vectors: both `U` and `V` have densities bounded by

`H=e^(1/2)`.                                                         (3.8)

Equation (3.5) gives

`R=2 beta U V`.                                                      (3.9)

By Lemma 2.1 and the scaling rule `||p_(cZ)||_3=|c|^(-2/3)||p_Z||_3`,

`||p_R||_3
 <= (2 beta)^(-2/3) 260^(1/3) e^(2/3)
 = (65 e^2)^(1/3) beta^(-2/3)`.                                     (3.10)

This proves the theorem. `QED`

A sharper one-dimensional projection constant such as `sqrt(2)` improves `C_0`, but is unnecessary for the universal branch closure below.

## 4. The all-second-minors-zero heavy branch closes universally

### Theorem 4.1 — `QFORM-HEAVY-PIVOT-SECOND-MINORS-ZERO-v1`

Assume the exact-rank-three target (1.1), with `|lambda_j|>=1`. Suppose there is an original coordinate `i` such that

`ell_i>1/2`, `a=A_ii!=0`, and `d_ik=0` for every `k!=i`.              (4.1)

Then `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity < 30.579`.                                         (4.2)

More precisely, for arbitrary `ell_i>0` under the same zero-second-minor hypothesis,

`||p_Q||_infinity
 <= C_* (|a| |det Lambda| ell_i)^(-1/4)`,                            (4.3)

where

`C_* = [8/3^(3/4)] (65 e^2)^(1/4) <16.430`,                         (4.4)

and the spectral threshold forces

`|a| |det Lambda| ell_i >= ell_i^2/3`.                              (4.5)

Hence (4.2) follows from `ell_i>1/2`.

#### Proof, step 1: exact Schur structure

Complete the square only in the original independent coordinate `X_i`. The Schur complement on the remaining coordinates is

`S_i=A_(-i,-i)-a^(-1)A_(-i,i)A_(i,-i)`.                             (4.6)

Since `rank A=3` and `a!=0`, `rank S_i=2`. Its physical diagonal is

`(S_i)_kk=A_kk-A_ik^2/a=d_ik/a=0`.                                  (4.7)

Thus Theorem 3.1 applies to the residual variable

`R_i=X_(-i)^T S_i X_(-i)`.                                          (4.8)

Write its nonzero eigenvalues as `+beta,-beta`.

#### Step 2: exact Schur pseudodeterminant identity

For every two-set `J` disjoint from `i`, Schur's determinant identity gives

`det (S_i)_J = det A_({i} union J)/a`.                              (4.9)

For exact rank three,

`det A_K=det(Lambda) det(R_K)^2`.                                    (4.10)

Summing (4.9) over all `|J|=2` and using the volume-sampling marginal identity

`sum_(J:|J|=2, i notin J) det(R_({i} union J))^2 = ell_i`            (4.11)

gives

`pdet(S_i)=det(Lambda) ell_i/a`.                                    (4.12)

For completeness, (4.11) follows by orthogonally rotating the three-dimensional coefficient space so that `r_i=(sqrt(ell_i),0,0)`, then applying Cauchy--Binet to the two remaining columns on the rows other than `i`.

Since the nonzero spectrum of `S_i` is `+beta,-beta`,

`beta^2=|det Lambda| ell_i/|a|`.                                    (4.13)

#### Step 3: spend the completed account04 square smoother

The original-coordinate completion has the exact form

`Q=a (X_i+h(X_(-i)))^2+R_i`.                                        (4.14)

Conditioned on the residual coordinates, `X_i+h` is a translate of `X_i`, so its conditional density is at most one. The source-valid account04/B18 domination therefore gives

`p_Q(t)<=|a|^(-1/2) int p_(R_i)(r)|t-r|^(-1/2)dr`.                  (4.15)

For any probability density `h` with `||h||_3=M`, split the last integral at `rho`. Holder on the near part and total mass one on the far part give the already-validated endpoint inequality

`sup_t int h(r)|t-r|^(-1/2)dr
 <= [8/3^(3/4)] M^(3/4).`                                            (4.16)

Theorem 3.1 gives `M<=C_0 beta^(-2/3)`. Therefore

`||p_Q||_infinity
 <= [8/3^(3/4)] C_0^(3/4) |a|^(-1/2) beta^(-1/2)`                   (4.17)

`= C_* (|a| |det Lambda| ell_i)^(-1/4)`,                            (4.18)

using (4.13). This is (4.3).

#### Step 4: the zero-second-minor hypothesis itself pays the scalar factor

The key new structural observation is that (4.1) makes the remaining factor in (4.3) automatically universal on a heavy row.

Sum the identities `d_ik=0` over `k!=i`:

`0 = a(tr A-a)-[(A^2)_ii-a^2]
  = a tr A-(A^2)_ii`.                                                (4.19)

Put

`T=lambda_1+lambda_2+lambda_3`, `D=|lambda_1 lambda_2 lambda_3|`.     (4.20)

Then

`|a| |T|=(A^2)_ii
 =sum_(j=1)^3 lambda_j^2 r_(ij)^2
 >=sum_(j=1)^3 r_(ij)^2
 =ell_i`.                                                            (4.21)

In particular `T!=0` and

`|a| >= ell_i/|T|`.                                                  (4.22)

Because every `|lambda_j|>=1`, the product `D` dominates each `|lambda_j|`, hence

`|T|<=sum_j |lambda_j| <=3D`.                                       (4.23)

Combining (4.22)--(4.23) gives the exact universal payment

`|a| D ell_i >= ell_i^2/3`.                                         (4.24)

For `ell_i>1/2`, the right side exceeds `1/12`. Inserting this into (4.3) gives

`||p_Q||_infinity
 < C_* 12^(1/4)
 <30.579`.                                                           (4.25)

This proves Theorem 4.1. `QED`

## 5. Why this is a genuine repair rather than a census

The previous B06 two-pivot endpoint needs a nonzero `d_ik`. The present theorem treats the exact opposite extreme: after a nonzero heavy first pivot, **every** second physical pivot determinant vanishes. Instead of trying to choose another local pair, it uses all of those failures simultaneously:

1. `d_ik=0` for every `k` forces the entire Schur remainder to have zero physical diagonal;
2. rank two plus zero diagonal factorizes exactly into two independent original-coordinate banks;
3. the product's unavoidable logarithm is finite in `L^3` with an explicit constant;
4. the same collection of failed minors yields `(A^2)_ii=a tr A`, which, together with the three-large-eigenvalue threshold, quantitatively pays the scalar pivot factor.

So the failures are converted into the decisive universal lemma rather than recorded as a list of exceptional configurations.

A deterministic fully coupled test instance is

`A=[[2,1,-2],[1,1/2,2],[-2,2,2]]`.

For pivot `i=1`, both second principal determinants vanish exactly:

`2*(1/2)-1^2=0`, `2*2-(-2)^2=0`.

The Schur remainder is `[[0,3],[3,0]]`, and the eigenvalues of `A` are approximately

`-1.9236770391, 2.2326415796, 4.1910354595`,

so all three satisfy the target threshold. This checks that the branch is fully coupled and nonempty; the theorem itself is the algebraic proof above, not the numerical check.

## 6. Exact remaining debt

This closes one previously singular endpoint branch but not the full conjecture. The first unpaid exact-rank-three geometry is now concentrated in two cases:

1. **heavy isotropic first row:** `ell_i>1/2` but `A_ii=0`; the preceding heavy-isotropic B06 report provides an `L^2` density and a uniform half-Riesz potential in a transverse-diffuse subbranch, but not the endpoint;
2. **partially paid second minors:** `A_ii!=0` and some `d_ik!=0`, but every available pair certificate is quantitatively small. The new support-disjoint correction shows that direct averaging against same-sign Pluecker mass is invalid. A valid continuation must aggregate the product law before reciprocal minor payment, using the weighted affine-fiber structure rather than selecting one pair.

After exact rank three is closed, extra correlated spectral directions remain a separate target-level issue.

**Continuity:** Theorem 4.1 proves absolute continuity and an essential `L^infinity` bound on its branch. It does **not** prove that the density has a continuous representative under merely measurable cap-one input densities.

**Full QFORM status:** `OPEN / NOT PROVED / NOT DISPROVED`.
