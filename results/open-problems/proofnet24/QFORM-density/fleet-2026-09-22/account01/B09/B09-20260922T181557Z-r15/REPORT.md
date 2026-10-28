# account01/B09 — rank-two hollow Schur routing with diagonal-safe half-Riesz smoothing

Run: `B09-20260922T181557Z-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Outcome: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full target remains open: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove `P{X^T A X in I} <= C |I|` with one universal finite `C`, or give a genuine counterexample. No continuity claim is made by the endpoint below.

## 1. Corrections and exact dependencies

This run does not use the now-refuted arbitrary-joint coarea `2/3` estimate or positive conditional projection-density moments. It also does not use law-uniform pointwise van-der-Corput decay, post-rotation independence, one-small-minor selection, or the false claim that one heavy off-diagonal row can always be absorbed by its own square.

The two main proof inputs are:

1. `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, complete source `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`. Its complex-amplitude argument gives, for a rank-`r` quadratic core with row leverage at most `1/2`, the phase-uniform Fourier bound even after multiplying each original-coordinate amplitude by an arbitrary unit-modulus separable phase.
2. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, complete source `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`. It supplies the Gaussian representation of the half-Riesz potential, the translated quadratic kernel, and the arbitrary-affine rank-two endpoint.

The required named partner result is account02/B09 `QFORM-PIVOT-OFFDIAG-STABLERANK-v1`, complete source `yspennstate/math-open-problems@77d71ed8bbd7f8a3fd40958e54b5bf658163c27a`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T160923Z-account02-B09-QFORM-r4/REPORT.md`. It is applied quantitatively in Section 7.

## 2. New rank-one small-ball lemma with arbitrary diagonal curvature

### Lemma 2.1 — `QFORM-DIFFUSE-RANK1-DIAG-SMALLBALL-v1`

Let `q in R^m` be a unit vector with `max_j q_j^2 <= 1/2`. Let `Y_j` be independent real random variables with probability densities bounded by one. For arbitrary real `lambda != 0`, arbitrary diagonal coefficients `d_j`, arbitrary affine vector `b`, and arbitrary constant `c`, define

`R = lambda (q^T Y)^2 + sum_j d_j Y_j^2 + b^T Y + c`.

Then, uniformly in `w in R` and `rho>0`,

`P{|R-w|<rho} <= min(1, 10 sqrt(rho/|lambda|)).`              (2.1)

#### Proof

For each frequency `t`, put

`h_{j,t}(x)=f_j(x) exp(i t[d_j x^2+b_j x])`.

The extra diagonal quadratic and affine terms are coordinate-separable and unit-modulus, so every `L^p` norm of `h_{j,t}` equals that of `f_j`. The rank-one `r=1` Brascamp--Lieb/Hausdorff--Young calculation from the separable-phase source therefore gives exactly

`|phi_R(t)| <= min(1, sqrt(e pi) |lambda t|^(-1/2)).`        (2.2)

No transformed coordinate is asserted independent.

Use the standard Gaussian majorant

`1_{|z|<rho} <= exp(v) exp(-v z^2/rho^2)`

and scalar Gaussian Fourier inversion. As in the rank-one affine lemma in the orientation-free rank-two source,

`P{|R-w|<rho}`
` <= exp(v) rho/(2 sqrt(pi v))`
`    * integral exp(-rho^2 t^2/(4v)) |phi_R(t)| dt.`         (2.3)

Insert the second term of (2.2), evaluate the Gaussian `|t|^{-1/2}` integral, and take `v=1/4`. The coefficient is `e^(3/4) Gamma(1/4)<10`. This proves (2.1). The crucial point is that arbitrary diagonal curvature survives because it was kept inside the original-coordinate complex amplitudes before any absolute value was taken. QED.

## 3. New rank-two half-Riesz endpoint with arbitrary diagonal curvature in the diffuse orientation

### Lemma 3.1 — `QFORM-DIFFUSE-RANK2-DIAG-HALFRIESZ-v1`

Let `U` be `m x 2` with `U^T U=I_2` and every row leverage `||U_{j,*}||^2 <=1/2`. Let `Lambda` be invertible symmetric `2 x 2`, and write `D0=|det Lambda|`. For arbitrary real diagonal coefficients `d_j`, affine vector `b`, and independent cap-one inputs `Y_j`, put

`F=(U^T Y)^T Lambda (U^T Y)+sum_j d_jY_j^2+b^TY+c`.

Then

`sup_w E |F-w|^(-1/2) <= 4 sqrt(2e) D0^(-1/4).`             (3.1)

#### Proof

Exactly as in Lemma 2.1, absorb `exp(i t[d_jx^2+b_jx])` into the original product amplitudes. The `r=2` separable-phase Brascamp--Lieb/Hausdorff--Young calculation gives

`|phi_F(t)| <= min(1, e pi D0^(-1/2)|t|^(-1)).`             (3.2)

The Gaussian half-Riesz representation used in `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` gives

`E|F-w|^(-1/2)`
` <= (2pi)^(-1/2) integral_R |t|^(-1/2)|phi_F(t)|dt.`        (3.3)

With `K=e pi D0^(-1/2)`, the integral of `|t|^(-1/2) min(1,K/|t|)` over the real line is `8 sqrt(K)`. Hence (3.1). This weighted integral is finite although the characteristic function itself need not be in `L^1`; therefore this argument does not revive the refuted absolute-Fourier route. QED.

## 4. Exact structure of every hollow rank-two symmetric matrix

### Lemma 4.1 — `QFORM-HOLLOW-RANK2-BIPARTITE-IDENTITY-v1`

Let `H` be real symmetric, nonzero, `diag H=0`, and `rank H=2`. Then its two nonzero eigenvalues are `+gamma,-gamma` for some `gamma>0`, and there exist disjoint physical coordinate sets `P,N` and unit vectors `p,q`, supported respectively on `P,N`, such that

`H = gamma (p q^T + q p^T).`                                  (4.1)

Moreover if `U=[u,v]` is an orthonormal eigenframe with

`H=gamma(uu^T-vv^T)`,                                         (4.2)

then the physical row leverages of `U` are exactly `p_i^2` on `P` and `q_i^2` on `N`.

#### Proof

Because `tr H=0` and `rank H=2`, the two nonzero eigenvalues sum to zero, giving (4.2). Zero diagonal gives `u_i^2=v_i^2` for every `i`. Thus, where `u_i!=0`, write `v_i=sigma_i u_i` with `sigma_i in {+1,-1}`. Orthogonality gives

`sum_i sigma_i u_i^2=0`, `sum_i u_i^2=1`,

so the `+` and `-` sign classes each contain exactly half of the `u`-mass. Put

`P={i:sigma_i=+1}`, `N={i:sigma_i=-1}`,
`p=sqrt(2) u_P`, `q=sqrt(2) u_N`.

Then `p,q` are unit and disjointly supported. Same-class entries of `H` vanish, while for `i in P,j in N`,

`H_ij=gamma(u_i u_j-v_i v_j)=2gamma u_i u_j=gamma p_iq_j`.

This is (4.1). Finally `u_i^2+v_i^2=2u_i^2`, which equals `p_i^2` or `q_i^2`. QED.

Thus a low-rank hollow Schur remainder is not an arbitrary rank-two object: it is an exact complete bipartite rank-one cross bank in the original coordinates.

## 5. Main theorem: diagonal-safe half-Riesz smoothing unless both bipartite banks have a heavy atom

### Theorem 5.1 — `QFORM-HOLLOW-RANK2-ONEBANK-DIFFUSE-HALFRIESZ-v1`

Let

`S = D + gamma(pq^T+qp^T)`,                                     (5.1)

where `D` is arbitrary real diagonal, `p,q` are disjointly supported unit vectors, and `gamma>0`. Let `Y` have independent cap-one coordinates and allow an arbitrary affine term `ell^TY+c`.

If it is **not** the case that both `p` and `q` possess a coordinate of squared magnitude greater than `1/2`, then

`sup_w E |Y^T S Y + ell^TY+c-w|^(-1/2)`
` <= C_RD gamma^(-1/2),`                                      (5.2)

where

`C_RD = 32 sqrt(10) 2^(1/4) = 120.3392989787... .`           (5.3)

#### Proof: both banks diffuse

If `max_i p_i^2<=1/2` and `max_jq_j^2<=1/2`, the two columns

`u=(p+q)/sqrt(2)`, `v=(p-q)/sqrt(2)`

are orthonormal and diagonalize the hollow term with eigenvalues `+gamma,-gamma`. Every row leverage of `[u,v]` is `p_i^2` on `P` or `q_j^2` on `N`, hence at most `1/2`. Apply Lemma 3.1 with `|det Lambda|=gamma^2`:

`sup_w E|...|^(-1/2) <=4sqrt(2e) gamma^(-1/2),`               (5.4)

which is stronger than (5.2).

#### Proof: one bank heavy and the opposite bank diffuse

Assume without loss that `|p_i|>1/sqrt(2)` for one physical coordinate `i in P`, while `max_j q_j^2<=1/2`. Condition every coordinate in `P\{i}` and every coordinate outside `supp(p) union supp(q)`. The remaining random variables are the physical variable `x=Y_i` and the independent physical bank `Y_N`. All conditioned terms only create constants and affine terms. Put

`Z=q^T Y_N`, `c0=gamma p_i`.

The surviving expression has the exact form

`F=d_i x^2+2c0 x Z+sum_{j in N} d_jY_j^2+alpha x+beta^T Y_N+C.`  (5.5)

If `d_i!=0`, complete the square in `x`. The translated one-dimensional quadratic kernel from the rank-two source gives, for fixed `Y_N`,

`E_x |F-w|^(-1/2) <=8|d_i|^(-1/2) Psi(W),`                  (5.6)

where, as a function of `Y_N`, `W` has a rank-one quadratic term

`(c0^2/d_i^2)(q^T Y_N)^2`

plus arbitrary diagonal and affine terms. Lemma 2.1 therefore gives

`P{|W|<rho} <=10 |d_i| |c0|^(-1) sqrt(rho).`                 (5.7)

The layer-cake kernel averaging lemma from the rank-two source, `E Psi(W)<=4sqrt(L)` when `P{|W|<rho}<=L sqrt(rho)`, yields

`E|F-w|^(-1/2) <=32sqrt(10)|c0|^(-1/2).`                    (5.8)

If `d_i=0`, then for fixed `Y_N` the expression is affine in `x`. The elementary rearrangement bound

`int f(x)|x-a|^(-1/2) dx <=2sqrt(2)`                         (5.9)

reduces the expectation to a constant times `E|2c0Z+alpha|^(-1/2)`. Since `q` is unit, the Rogozin--Ball scalar projection theorem gives `||p_Z||_infinity<=sqrt(2)`. Rearrangement of the kernel `|z|^(-1/2)` then gives a bound strictly smaller than the right side of (5.8). Thus (5.8) holds in both cases.

Finally `|p_i|>1/sqrt(2)`, so `|c0|>gamma/sqrt(2)`. Hence

`32sqrt(10)|c0|^(-1/2)`
` <32sqrt(10)2^(1/4)gamma^(-1/2)=C_RD gamma^(-1/2).`         (5.10)

The case `q` heavy and `p` diffuse is symmetric. QED.

This theorem directly survives the account02/B09 same-square falsifier: that falsifier corresponds to two singleton banks, hence both banks are heavy and lies exactly in the exceptional regime rather than contradicting (5.2).

## 6. Square-pivot consequence and direct O(|I|) bound

### Corollary 6.1 — `QFORM-PIVOT-RANK2-HOLLOW-ROUTING-v1`

Take any physical coordinate pivot `k` with `a=A_kk!=0`, and after completing its square write the Schur complement as

`S=A_{-k,-k}-A_{-k,k}A_{k,-k}/a`.

Suppose `H=S-diag(S)` has rank two and nonzero eigenvalues `+gamma,-gamma`. Use Lemma 4.1 to write `H=gamma(pq^T+qp^T)`. If not both `p,q` have a coordinate with squared magnitude exceeding `1/2`, then

`boxed: ||p_{X^TAX}||_infinity <= C_RD / sqrt(|a| gamma).`   (6.1)

Consequently every interval `I` satisfies

`P{X^TAX in I} <= C_RD (|a|gamma)^(-1/2)|I|.`                (6.2)

#### Proof

Completing the physical square gives

`Q=a(X_k+m(Y))^2 + R(Y)`.

For each fixed `Y`, the pushforward of a cap-one density under `a(x+m)^2` has density at most

`|a|^(-1/2)|z|^(-1/2)`

on its relevant half-line. Therefore

`p_Q(t) <= |a|^(-1/2) E|R(Y)-t|^(-1/2).`                    (6.3)

Apply Theorem 5.1, which permits every diagonal coefficient and every induced affine term. This proves (6.1)-(6.2). The argument establishes an essentially bounded density. It does not by itself prove continuity for arbitrary input densities. QED.

## 7. Assigned partner result applied to an actual target inequality

The account02/B09 theorem `QFORM-PIVOT-OFFDIAG-STABLERANK-v1` states that with the same physical pivot, `s=||S||_op`, and `S^o=S-diag S`,

`||S^o||_F^2 >=24s^2`

implies

`||p_Q||_infinity <=11.876 / sqrt(|a|s).`                    (7.1)

This is not merely cited. Apply it to the already completed diagonal-heavy post-window target branch from the partner report: `|a|>=1/312` and

`s>=delta0:=2/(3+sqrt(5))=0.381966...`.

Then (7.1) gives

`||p_Q||_infinity <339.42<340.`                              (7.2)

On the complementary exact rank-two hollow Schur branch, if the bipartite resource also satisfies `gamma>=s/4`, Corollary 6.1 gives, unless both banks are heavy,

`||p_Q||_infinity`
` <= C_RD / sqrt((1/312)(delta0/4))`
` <6878.64<6879.`                                            (7.3)

If both banks are diffuse, the sharper constant from (5.4) gives instead

`||p_Q||_infinity <533.12<534.`                              (7.4)

Thus the partner's high-stable-rank branch and the new low-rank bipartite branch are quantitatively compatible pieces of the same physical-pivot route.

## 8. The exceptional two-heavy regime is now very small and explicit

When Theorem 5.1 does not apply, Lemma 4.1 forces unique physical coordinates `i in P`, `j in N` with

`p_i^2>1/2`, `q_j^2>1/2`.

Their physical cross coefficient satisfies

`|H_ij|=gamma|p_iq_j|>gamma/2.`                              (8.1)

Let

`B=[[D_ii,H_ij],[H_ij,D_jj]].`                               (8.2)

Conditioning all other residual coordinates leaves this physical pair with arbitrary affine terms. The orientation-free rank-two half-Riesz theorem therefore gives

`sup_w E|Y_{ij}^T B Y_{ij}+affine-w|^(-1/2)`
` <=128 |det B|^(-1/4)`                                     (8.3)

whenever `det B!=0`. For example, if

`|det B| >= gamma^2/16`,                                     (8.4)

then the outer square-pivot argument gives

`||p_Q||_infinity <=256 / sqrt(|a|gamma).`                   (8.5)

Therefore the only exact-rank-two hollow Schur configurations not paid by Sections 5-8 are quantitatively concentrated near a **two-heavy, nearly singular physical pair**:

`p_i^2>1/2`, `q_j^2>1/2`, `|det B|<gamma^2/16`.              (8.6)

In that regime (8.1) and (8.6) imply

`D_ii D_jj > 3gamma^2/16>0`,                                 (8.7)

so the two diagonal entries have the same sign and the pair is close to the same-square cancellation mechanism. The global target's required third spectral resource must therefore be routed from outside this near-rank-one pair. This is a substantially narrower structural obligation than an arbitrary low-stable-rank Schur complement.

## 9. Compact conditional end-to-end route and first unpaid implication

The current B09 route is:

1. Use the established spectral-window/heavy-coordinate reductions from the shared state. In the diagonal-heavy pivot branch, a genuine scalar pivot has `|a|>=1/312` and its Schur complement retains at least two singular values at universal scale.
2. If the Schur off-diagonal stable-rank gate fires, apply the assigned account02/B09 theorem and obtain `<340` as in (7.2).
3. If the Schur off-diagonal part is exactly rank two, use the exact bipartite identity (4.1). If at least one sign bank is diffuse, the new diagonal-safe half-Riesz theorem gives a direct `O(|I|)` estimate even with arbitrary diagonal Schur curvature. If both banks are heavy but the heavy physical `2 x 2` pair is not nearly singular, (8.5) pays it.
4. The surviving exact-rank-two case is the two-heavy nearly singular pair (8.6), which is the source-valid analogue of the same-square obstruction. Any proof must now extract the third target spectral resource outside that pair and combine it with the existing outer pivot without normalizing away product provenance.

The first unpaid implication is therefore

**`QFORM-TWOHEAVY-NEARSINGULAR-THIRDRESOURCE-v1` (OPEN):** under the full target spectral hypothesis and the current post-window physical-pivot reduction, prove that the two-heavy near-singular survivor (8.6) supplies, outside its two physical coordinates, either a universal diagonal/square smoother, a nested cross bank already covered by the half-barrier theorem, or a ridge/diffuse resource. The argument must retain arbitrary extra spectrum and must not use the refuted conditional-density or single-good-minor interfaces.

This report does not prove the full conjecture and does not prove continuity. It does give a new direct linear small-ball branch and an exact product-coordinate description of the previously opaque rank-two hollow low-stable-rank Schur case.
