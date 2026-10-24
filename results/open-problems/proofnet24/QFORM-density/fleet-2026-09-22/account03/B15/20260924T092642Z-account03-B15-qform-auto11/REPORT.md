SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T09:26:42Z.
attacking: no-loss homogenization of arbitrary affine terms by a remote-support auxiliary coordinate, plus fixed-instance affine C0 closure.

# account03/B15 — affine fixed-instance C0 regularity and sharp square-root marginal stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T092642Z-account03-B15-qform-auto11`  
Status: `AFFINE_FIXED_C0_PROVED / AFFINE_L1_TO_LINF_HALF_HOLDER_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Duplicate route terminated, successor regularity gap attacked

The initially planned measure-level affine homogenization is already proved, with the exact universal constant and no moment assumption, by account03/B14:

`yspennstate/math-open-problems@6d920f5ad706016d41d3072a2dc6e71a64bc0296`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T213400Z-account03-B14-QFORM-auto11/REPORT.md`.

That theorem proves that a homogeneous target interval bound with constant `C` implies the same affine-quadratic interval bound for `X^TAX+b^TX+c`, using one far-translated independent cap-one coordinate. It explicitly does **not** obtain continuity through that weak-limit passage. Therefore this run does not duplicate that theorem. It closes the next regularity question instead.

## 2. Main theorem

### Theorem A — `QFORM-AFFINE-FIXED-C0-v1`

Let `A` be any fixed real symmetric matrix with `rank(A)>=3`, let `b in R^n`, `c in R`, and let `X_1,...,X_n` be independent with arbitrary measurable probability densities `0<=f_i<=1`. Then

`q(X)=X^TAX+b^TX+c`

has a canonical density

`p_q in C_0(R) cap L^infinity(R)`.

The height is finite for each fixed `A`, but the theorem does not claim a matrix-uniform bound under `s_3(A)>=1`.

Moreover, for every original coordinate `j` there is a finite constant `K(A,j)`, depending on `A,j` only and **independent of b,c and of all input laws**, such that if two cap-one product inputs differ only in marginal `j`, then

`boxed( ||p_f-p_g||_infinity <= sqrt(2) K(A,j) ||f_j-g_j||_1^(1/2). )`       (2.1)

If every marginal changes, telescoping gives

`boxed( ||p_f-p_g||_infinity <= sqrt(2) sum_j K(A,j)||f_j-g_j||_1^(1/2). )`   (2.2)

Thus cap-preserving smooth compact approximation of the marginals converges **uniformly at the affine output-density level** for every fixed rank-at-least-three Hessian.

### Corollary — same-constant affine C0 closure

If the universal homogeneous QFORM interval theorem is eventually proved with constant `C`, then account03/B14 already gives the same interval constant `C` for every affine perturbation with the same target Hessian. Theorem A then upgrades that affine law to its canonical `C_0` representative, and interval domination forces

`boxed( p_q in C_0(R),  ||p_q||_infinity <= C. )`                              (2.3)

So deterministic affine terms create no additional quantitative regularity debt once the central universal height estimate is paid.

## 3. Absolute continuity for affine quadratics

The qualitative statement holds under much weaker assumptions. Let the joint input law merely be absolutely continuous and let

`q(x)=x^TAx+b^Tx+c`

be nonconstant. Its gradient is

`grad q(x)=2Ax+b`.

The critical set is either empty, or (when `-b/2` lies in `Range(A)`) an affine translate of `ker A`. If `A!=0`, this is a proper affine subspace and hence Lebesgue-null. If `A=0` and `b!=0`, the critical set is empty. For a one-dimensional null set `N`, apply coarea on

`E_k=q^{-1}(N) intersect {|grad q|>=1/k}`.

Then

`int_{E_k}|grad q| dx = int_N H^{n-1}(q^{-1}(t) intersect {|grad q|>=1/k}) dt =0`,

so `|E_k|=0`. Adding the null critical set shows `|q^{-1}(N)|=0`. Therefore every nonconstant affine quadratic pushforward of an absolutely continuous joint law is absolutely continuous. This proves density existence only, not boundedness or continuity.

## 4. Affine extension of the scaled-coordinate certificate

The key input is account03/B15 auto32:

`yspennstate/math-open-problems@f4dee8a3ff12ab02f8efd52fb80a0d169b7cd708`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T032517Z-account03-B15-qform-auto32/REPORT.md`.

For fixed rank-at-least-three `A` and coordinate `j`, that report constructs `K(A,j)<infinity` such that, with

`T_m=diag(1,...,1,m,1,...,1)`, `A_m=T_m A T_m`, `0<m<=1`,

one has

`P(Y^T A_m Y in I) <= K(A,j)m^(-1/2)|I|`.                         (4.1)

The proof is an exhaustive rank split on the principal complement. Every analytic receiver used in the split is uniform in arbitrary affine terms: the rank-at-least-three complement certificate is affine-uniform after conditioning; the physical-pair half-Riesz certificate is affine-uniform; and the independently reviewed rank-three principal-block consequence is affine-uniform. Repeating that exact split therefore gives the affine strengthening

`boxed( P(Y^T A_mY + ell^T Y+d in I) <= K(A,j)m^(-1/2)|I| )`       (4.2)

for every deterministic `ell,d`, with the **same** `K(A,j)`.

No bound on `ell` occurs. This translation-uniformity is essential because the affine vector can become arbitrarily large in conditioning and remote-support arguments.

## 5. Submass square-root theorem for affine outputs

Let `g` be a subdensity in coordinate `j` with

`0<=g<=1`, `int g=m<=1`,

and keep arbitrary cap-one probability marginals in all other coordinates. Normalize the `j`-th law to `h=g/m`. If `X_j` has density `h` and `Y_j=X_j/m`, then `Y_j` has probability density

`m h(my)=g(my)<=1`.

Writing `X=T_mY`,

`X^TAX+b^TX+c = Y^T A_mY + (T_m b)^T Y+c`.                         (5.1)

Apply (4.2) with `ell=T_m b`. The normalized output law has interval constant `K(A,j)m^(-1/2)`. Multiplying back by the submass `m`, the original subprobability pushforward has a density `r_g` with

`boxed( ||r_g||_infinity <= K(A,j) sqrt(m). )`                     (5.2)

This bound is uniform in `b,c`.

Now let `f_j,g_j` be two probability densities and put `delta=||f_j-g_j||_1`. The positive and negative parts of `f_j-g_j` each have mass `delta/2` and each are bounded by one. Their affine quadratic pushforwards therefore have densities of height at most `K(A,j)sqrt(delta/2)`. Their signed difference is exactly the difference of the two output laws, so

`||p_f-p_g||_infinity <=2K(A,j)sqrt(delta/2)=sqrt(2)K(A,j)sqrt(delta)`,

which proves (2.1). Telescoping one marginal at a time proves (2.2).

The exponent `1/2` is already sharp for the homogeneous owner-target example in auto32, so no exponent larger than `1/2` can hold uniformly over all affine terms either (take `b=0`).

## 6. Smooth affine outputs are C0

It remains to supply one `C_0` anchor to which (2.2) can converge. Let the joint density `F` be `C_c^infinity`, and assume `rank(A)=r>=3`.

Decompose

`b=b_R+b_K`, `b_R in Range(A)`, `b_K in ker(A)`.

Put `h=(1/2)A^dagger b_R` and translate `x=y-h`. Translation preserves smooth compactness. Up to an output constant,

`q(x)=y^T A y+b_K^T y`.                                             (6.1)

If `b_K=0`, the fixed smooth quadratic theorem from account01/B15 applies directly: a rank-at-least-three quadratic pushforward of any `C_c^infinity` joint density has a `C_0` density (its fixed-instance characteristic function decays like `|t|^{-r/2}`).

If `b_K!=0`, choose an orthogonal decomposition `R^n=Range(A) direct_sum ker(A)` and a kernel coordinate `z_1` in the direction of `b_K`. In these coordinates

`q(y,z)= y^T Lambda y + beta z_1 + const`, `beta=|b_K|>0`.           (6.2)

The rotated amplitude is still `C_c^infinity`; no independence after rotation is asserted or needed. Integrating out `z_1` gives the explicit density

`p(t)=|beta|^{-1} int F_tilde(y,z', (t-const-y^TLambda y)/beta) dy dz'`.  (6.3)

The integrand is continuous in `t`, is supported in one fixed compact set in `(y,z')`, and is uniformly bounded. Dominated convergence makes `p` continuous. Compactness of the original support makes the output support compact. Hence `p in C_c subset C_0`.

Therefore every smooth compact affine instance with rank-at-least-three Hessian has a `C_0` density.

## 7. Passage to arbitrary rough marginals

Use the cap-preserving approximation theorem from account01/B15:

`yspennstate/math-open-problems@48d4e5be4428f09a1972d51bede192357fab1675`
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260924T070755Z-account01-B15-QFORM-auto11/REPORT.md`.

Choose `f_{j,k} in C_c^infinity`, `0<=f_{j,k}<=1`, `int f_{j,k}=1`, with

`sum_j ||f_{j,k}-f_j||_1 ->0`.

Let `p_k` be the affine output density. Section 6 gives `p_k in C_0`. By (2.2), `(p_k)` is uniformly Cauchy, so it converges uniformly to some `p in C_0`.

The product input laws converge in total variation, hence their deterministic affine-quadratic pushforwards converge in total variation to the target output law. For every bounded interval `I`, uniform convergence gives

`int_I p_k -> int_I p`,

while total variation gives

`P(q(X^{(k)}) in I) -> P(q(X) in I)`.

Thus the target law agrees with `p(t)dt` on every bounded interval and hence on every Borel set. Therefore `p` is the canonical rough-output density and Theorem A follows.

This is stronger than weak-limit continuity: the output densities themselves converge in sup norm for each fixed Hessian.

## 8. Designated partner applied to an actual inequality

Use account04/B15's completed dense range-aligned family:

`yspennstate/math-open-problems@ae87801238cf5756c153d27fed0bb6524d88ee17`
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T231929Z-account04-B15-range-aligned-c0-r9/REPORT.md`,

and its same-constant compiler at

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`.

For `m>=1`, `a>=1`, arbitrary real `R in R^{2xm}`, set

`H=[[a I_2,R],[R^T,-a I_m]]`.                                      (8.1)

The partner square identity gives

`H^2=diag(a^2 I_2+RR^T, a^2 I_m+R^TR) >= a^2 I`,                  (8.2)

so `H` is invertible and has rank `m+2>=3`. Appending one inert cap-one coordinate to any product law on the active variables puts (8.1) exactly inside the partner r9 family. Its interval inequality therefore gives

`P(X^T H X in I) <= (2pi/a)|I|`.                                  (8.3)

Now take an arbitrary deterministic `b in R^{m+2}` and `c in R`, and put

`h=(1/2)H^{-1}b`.

Then, exactly,

`X^THX+b^TX+c = (X+h)^T H(X+h) + c-h^T Hh`.                        (8.4)

Coordinatewise translation preserves independence and the cap-one property. Applying the partner inequality (8.3) to `X+h` gives the **actual affine inequality**

`boxed( P(X^THX+b^TX+c in I) <= (2pi/a)|I|. )`                    (8.5)

The account04/B15 same-constant `C_0` compiler applied to the translated homogeneous instance then yields

`boxed( p in C_0(R),  ||p||_infinity <=2pi/a. )`                  (8.6)

As a Fourier consequence, Plancherel and `||p||_1=1` give

`boxed( int_R |phi_q(t)|^2 dt =2pi ||p||_2^2 <=4pi^2/a. )`        (8.7)

This is a concrete quantitative regularity estimate for an arbitrary-dimensional dense cross-coupled target family with arbitrary deterministic affine terms.

## 9. Exact status

Proved in this run:

1. every nonconstant affine quadratic of an absolutely continuous joint input is absolutely continuous;
2. for every fixed `rank(A)>=3`, arbitrary rough cap-one product inputs and arbitrary `b,c` give a canonical `C_0 cap L^infinity` density;
3. output densities are `1/2`-Holder in each marginal's `L^1` distance with matrix-dependent constant, uniformly in all affine terms;
4. homogeneous-to-affine universal interval reduction from B14 plus this theorem gives same-constant affine `C_0` closure;
5. the designated account04/B15 dense family extends to all affine terms with height `2pi/a`, and satisfies the actual `L^2` Fourier bound (8.7).

Not proved:

- no matrix-uniform `K(A,j)` follows from the bare three-large-eigenvalue hypothesis;
- the central universal interval/height theorem is still OPEN;
- no law-uniform or target-uniform modulus of continuity is claimed;
- no pointwise van-der-Corput decay, post-rotation independence, support/moment assumption, arbitrary-joint bounded coarea lemma, or numerical extremality claim is used.

The first unpaid target implication is unchanged: obtain a dimension-free product-preserving interval estimate from `s_3(A)>=1`. Regularity and arbitrary deterministic affine terms are now downstream once that height is paid.
