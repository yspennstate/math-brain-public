SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B07, 2026-09-22T18:04:12Z.
attacking: zero-pivot/finite-heavy coordinate-minor payment; replace reciprocal tiny-minor selection by a product-preserving disjoint-cross-block estimate and apply the latest partner collar.

# fleet02/B07 — disjoint 3x3 cross-block Plancherel payment

**Run:** `20260922T180412Z-b07-afd8d7`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control before publication:** revision `2026-09-22.11` at `yspennstate/math-research-brain@224b1e0e76c1a2647a98008384abeaaf230f2791`  
**Assignment:** Coordinate minor selection  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and corrections consumed

The target remains the unrestricted statement: independent real coordinates with densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of absolute value at least one; prove one dimension-free density bound for `X^T A X`, or give a target-valid counterexample.

This run used the live corrections, in particular:

* the general law-uniform `L^1` characteristic-function route is false and must not be used as a universal reduction;
* `QFORM-CROSSMINOR-ALONE-FALSE` refutes a **2x2** nonsingular cross block as a sufficient density certificate. Its explicit witness has only rank two. The event's safe replacement already records the zero-self-block `m>=2` bilinear theorem. Nothing in that correction refutes a 3x3 cross block with arbitrary self blocks.

The theorem below is a scoped sufficient condition. It obtains `L^1` Fourier decay from an actual invertible disjoint physical `m x m` cross block with `m>2`; it does not claim that every QFORM instance has integrable characteristic function.

## 2. New theorem

### Theorem — `QFORM-DISJOINT-CROSS-PLANCHEREL-v1`

Let `I,J` be disjoint sets of original independent coordinates with `|I|=|J|=m>=3`. Put

`C=A[I,J]`.

If `C` is invertible, then for arbitrary values of every other entry of the symmetric matrix `A` and arbitrary independent input laws with densities bounded by one, the full quadratic form `Q=X^TAX` has a continuous density and

`||p_Q||_infinity <= [m/(m-2)] |det C|^(-1/m).`          (2.1)

In particular, for `m=3`,

`||p_Q||_infinity <= 3 |det C|^(-1/3).`                    (2.2)

No moment, support, sign, definiteness, centering, post-rotation independence, or assumption on either principal self block is used. All outside quadratic terms and couplings are retained.

### Proof

Condition on all original coordinates outside `I union J`. This preserves independence of the selected original coordinates. Writing the selected vectors as `x in R^m`, `y in R^m`, the conditional phase has the exact form

`q_z(x,y)=x^T P x + 2 x^T C y + y^T R y + alpha_z dot x + beta_z dot y + d_z`,

where `P,R` are arbitrary symmetric matrices and the affine coefficients can depend arbitrarily on the conditioned outside vector `z`.

Let `f_I(x)=prod_{i in I} f_i(x_i)` and `f_J(y)=prod_{j in J} f_j(y_j)`. Since every scalar density has `0<=f_i<=1` and integral one,

`||f_I||_2 <=1`, `||f_J||_2 <=1`.                         (2.3)

For fixed real `t`, absorb every term except the cross interaction into unimodular factors:

`h_t(x)=f_I(x) exp(i t[x^T P x+alpha_z dot x])`,
`g_t(y)=f_J(y) exp(i t[y^T R y+beta_z dot y])`.

Use the Fourier convention

`hat h(xi)=int exp(-i xi dot x) h(x) dx`.

Ignoring the irrelevant constant phase, the conditional characteristic function is

`phi_z(t)=int g_t(y) hat h_t(-2t C y) dy`.

Cauchy--Schwarz, the invertible change of variables `xi=-2tCy`, and Plancherel give, for `t!=0`,

`|phi_z(t)|
 <= ||g_t||_2 [int |hat h_t(-2tCy)|^2 dy]^(1/2)
 = ||g_t||_2 (2|t|)^(-m/2)|det C|^(-1/2)||hat h_t||_2
 <= (2|t|)^(-m/2)|det C|^(-1/2)(2pi)^(m/2)
 = pi^(m/2)|det C|^(-1/2)|t|^(-m/2).`                      (2.4)

The estimate is uniform in the outside conditioning. Averaging over `z` therefore yields

`|phi_Q(t)| <= min(1, K |t|^(-m/2)),`
`K=pi^(m/2)|det C|^(-1/2).`                                (2.5)

For `m>2` this envelope is integrable. Let

`t0=K^(2/m)=pi |det C|^(-1/m).`

Then exactly

`int_R min(1,K|t|^(-m/2)) dt
 =2 t0 m/(m-2).`                                            (2.6)

Fourier inversion therefore gives a continuous density and

`||p_Q||_infinity
 <=(2pi)^(-1) int |phi_Q(t)|dt
 <=[m/(m-2)] |det C|^(-1/m).`

This proves (2.1). QED.

### Endpoint check

At `m=2`, (2.4) decays only as `|t|^-1`, so this proof has a logarithmic endpoint failure. That is exactly compatible with the source-valid rank-two cross-minor counterexample in `QFORM-CROSSMINOR-ALONE-FALSE`. The threshold `m=3` is therefore structural here, not an artifact of claiming the refuted 2x2 statement.

## 3. Direct application of the designated partner result

The latest completed partner result consumed is fleet03/B07 r13, `QFORM-O0-HEAVY-PACKET-ISOLATION-v1`, source-pinned at

`yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T173711Z-fleet03-B07-qform-r13/REPORT.md`.

On its O0 branch, the third-volume resource is `E>=1/256`. If at least three calibrated row ridge leverages are at least `3/4`, the partner produces three original rows `H` carrying `det(B_HB_H^T)>=1/4096`. Its transpose-diffuse subbranch is already paid by fleet01/B04 with density `<79`.

In the complementary localized subbranch, if at least three column projection leverages are at least `11/16`, the partner proves that there are three original columns `T`, disjoint from `H`, with

`|det B[H,T]| >=1/256`.                                     (3.1)

The partner report stopped here because it conservatively invoked `QFORM-CROSSMINOR-ALONE-FALSE`. The live correction itself is specifically 2x2. Applying (2.2) to the genuine **3x3** disjoint physical cross block `C=B[H,T]` gives immediately

`||p_Q||_infinity
 <=3 |det C|^(-1/3)
 <=3*256^(1/3)
 =19.048812623618... <19.049.`                               (3.2)

Thus the entire six-coordinate, three-heavy-row/three-heavy-column O0 collar is now paid, with arbitrary self blocks, outside couplings, signs and extra spectrum retained. It also has a continuous density because the characteristic function is integrable in this scoped branch.

This is an actual application of the named fleet03/B07 result, not only a citation.

## 4. Conditional end-to-end position

The existing third-compound overlap reduction splits the structural proof into O0/O1/O2/O3 overlap branches. In O0:

1. the ridge-diffuse case is already paid;
2. fleet03/B07 r13 isolates a constant third-volume packet from three heavy rows;
3. the transpose-diffuse packet is already paid `<79`;
4. this run pays the complementary branch with at least three heavy transpose columns by (3.2).

Therefore the first O0 obstruction has been reduced to the genuinely finite-heavy case: at most one or two heavy coordinates on at least one side, while a constant aggregate third-volume packet remains. If the original side begins with fewer than three heavy rows, the partner's one-/two-heavy skeleton is exactly the same residual geometry.

The separate O1 zero/near-pivot hyperbolic packet from the preceding fleet02/B07 run, plus O2/O3 aggregate payment, also remain open. Consequently the full QFORM theorem is **not proved** by this report.

## 5. First unpaid implication

`QFORM-O0-ONE-TWO-HEAVY-AGGREGATE-PAYMENT-v2`:

> Given a disjoint physical cross block whose total third-volume `e_3(s(B)^2)` is bounded below, and whose calibrated effective-rank-three row/column leverage obstruction has at most two heavy original coordinates on one side, convert the retained determinant-weighted aggregate into either (i) a product-preserving rank-two/grouped-coordinate smoothing certificate, or (ii) a 3x3 cross block with a dimension-free determinant lower bound after paying the diffuse remainder. No reciprocal worst-minor selection is allowed.

A solution must remain valid for the singleton-plus-two-banks family and the live cross-minor/conditional-cap corrections.

## 6. Exact arithmetic check used

`CHECK.py` and `CHECK_OUTPUT.txt` beside this report verify the integration constant and the partner numerical specialization. Terminal marker:

`STATUS=QFORM_DISJOINT_3CROSS_L2_CHECK_PASS`.

The check is arithmetic only; the proof of the theorem is the analytic argument in Section 2.

## 7. Status

* `QFORM-DISJOINT-CROSS-PLANCHEREL-v1`: **PROVED SUPPORTING THEOREM**.
* fleet03/B07 r13 six-coordinate localized O0 collar: **PAID**, density `<19.049`.
* `QFORM-O0-ONE-TWO-HEAVY-AGGREGATE-PAYMENT-v2`: **OPEN**.
* O1/O2/O3 aggregate branches: **OPEN**.
* full QFORM conjecture: **OPEN / neither proved nor disproved**.
