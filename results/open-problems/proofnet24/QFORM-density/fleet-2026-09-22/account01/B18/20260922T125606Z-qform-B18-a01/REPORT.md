# account01/B18 — heavy-row Schur determinant conservation and rank-two fractional smoothing

**Run:** `20260922T125606Z-qform-B18-a01`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer / STRUCTURE  
**Status:** new supporting theorem proved; full conjecture OPEN / NOT PROVED  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and dependencies

The target remains: independent real coordinates `X_i` with densities `0<=f_i<=1`, arbitrary real symmetric `A` with at least three eigenvalues of magnitude at least one, and one universal bound on the density of `X^T A X`.

This report treats an exact rank-three branch and does not claim a full proof. It consumes and applies two exact prior results:

1. `QFORM-JOINT-BILINEAR-SQUARE-v1`, account02/B18, scientific commit `43d49b06197ea4f07770f8dae426236ad074b684`, especially its conditional-square-smoothing principle: a translated physical square can smooth a residual without independence of the two summands.
2. `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, interactive scientific commit `773b7fb6f0e6a8142066f0bac08d228dfc164fdb`. Its geometric Brascamp--Lieb + sharp Hausdorff--Young proof is applied below at rank two only to obtain the borderline `|t|^{-1}` characteristic-function estimate. Rank two alone does not give a bounded quadratic density, but the additional physical square makes the weighted Fourier integral convergent.

Primary analytic inputs are the geometric Brascamp--Lieb marginal argument of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, and Beckner's sharp Hausdorff--Young inequality, *Annals of Mathematics* 102 (1975), 159--182.

Fresh corrections consumed before publication include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`. In particular, no claim is made that a single physical Schur pivot must exist with a rank-two cross block.

## 2. Algebraic heavy-row identity

Let

`A = U Lambda U^T`,

where `U` is `n x 3`, `U^T U=I_3`, and `Lambda` is an invertible real symmetric `3 x 3` matrix. Thus `A` has rank exactly three. Choose a physical coordinate `i`. Write the `i`th row of `U` as `u^T`, let

`c=||u||_2^2`,  `a=u^T Lambda u`,

and let `V` be `U` with that row removed. Then, in the physical split `{i} union {i}^c`,

`A = [[a, b^T],[b,C]]`,

with

`b=V Lambda u`,  `C=V Lambda V^T`.

Assume `c>0` and `a!=0`. Completing the physical square gives

`X^T A X = a [X_i + b^T X_{-i}/a]^2 + X_{-i}^T S X_{-i}`,

where

`S=C-bb^T/a = V M V^T`,

`M=Lambda - Lambda u u^T Lambda/a`.                                      (2.1)

Because `M u=0`, the residual has rank at most two. Let `e_3=u/sqrt(c)` and let `E` be a `3 x 2` matrix whose columns are an orthonormal basis of `u^perp`. Put

`W=V E`,  `M_2=E^T M E`.

Since `V^T V=I_3-u u^T`,

`W^T W = E^T(I_3-u u^T)E=I_2`.                                           (2.2)

Hence `W` is an exact two-dimensional orthogonal projection frame on the remaining original coordinates, and

`S=W M_2 W^T`.                                                            (2.3)

### Determinant conservation

In the orthonormal basis `[E,e_3]`, write

`Lambda = [[B,d],[d^T,e]]`.

Here `e=e_3^T Lambda e_3=a/c`. Direct substitution into (2.1) gives

`M_2=B-dd^T/e`.

The Schur determinant formula therefore yields

`det Lambda = e det(M_2)`, hence

`boxed: det(M_2) = c det(Lambda)/a`,                                      (2.4)

and in absolute values

`boxed: |a| |det M_2| = c |det Lambda|`.                                  (2.5)

This is exact. It shows that the physical square curvature and residual two-dimensional curvature are not independent resources: their determinant product is the original rank-three spectral determinant times the selected row leverage.

For later use, if the remaining rows of `U` are `u_j^T`, the row leverages of `W` are

`d_j=||E^T u_j||_2^2 = ||u_j||_2^2 - (u_j dot u)^2/c`,                    (2.6)

and `sum_{j!=i} d_j=2`.

## 3. Rank-two diffuse residual: the exact borderline Fourier estimate

Assume now that

`max_{j!=i} d_j <= 1/2`.                                                   (3.1)

Let `R=X_{-i}`, `Z=W^T R`, and denote the density of `Z` by `g`. The rank-two part of the geometric Brascamp--Lieb/Hausdorff--Young calculation gives

`||hat g||_1 <= (2 pi)^2 B(W)`,                                           (3.2)

where

`B(W)=prod_{d_j>0}(1-d_j)^(-(1-d_j)/2) <= e`.                             (3.3)

For completeness: set `v_j=w_j/sqrt(d_j)` so `sum d_j v_j v_j^T=I_2`; apply geometric Brascamp--Lieb to

`H_j(s)=|hat f_j(sqrt(d_j)s)|^(1/d_j)`

and Beckner's Hausdorff--Young inequality with conjugate exponents

`q_j=1/d_j>=2`, `p_j=1/(1-d_j)<=2`.

The powers of `d_j` cancel exactly and `||f_j||_{p_j}<=1` because `0<=f_j<=1` and `||f_j||_1=1`. Equation (3.3) follows from `-(1-d)log(1-d)<=d` and `sum d_j=2`.

Let

`T=Z^T M_2 Z`,  `D=|det M_2|`.

The same Gaussian-regularized Fresnel inversion used in the cited diffuse theorem, now in dimension two, yields for every `t!=0`

`|phi_T(t)| <= pi B(W) D^(-1/2) |t|^(-1)`.                               (3.4)

Thus, with

`K=pi B(W) D^(-1/2)`,

`|phi_T(t)| <= min(1,K/|t|)`.                                             (3.5)

Rank two is exactly borderline: (3.5) is not integrable, so it does not by itself prove a bounded density for `T`. The next step is where the physical square is used.

## 4. Fractional square-smoothing lemma

### Lemma

Let `T` be a real random variable satisfying

`|phi_T(t)| <= min(1,K/|t|)` for all `t!=0`.                              (4.1)

Let `(T,W_0)` be any pair such that the regular conditional density of `W_0` given `T=t` is bounded by `1` for almost every `t`. Then for every `a!=0`,

`Y=T+a W_0^2`

has an essentially bounded density and

`boxed: ||p_Y||_infty <= 4 sqrt(K/(pi |a|))`.                             (4.2)

### Proof

Take first `a>0`. Conditional on `T=t`, the change of variables through the two roots of `a w^2=s` gives

`p_{aW_0^2 | T=t}(s) <= 1_{s>0}/sqrt(a s)`.

Hence at the measure level

`p_Y(y) <= a^(-1/2) (k*p_T)(y)`,  `k(s)=1_{s>0}s^(-1/2)`.                 (4.3)

Equation (4.1) implies `phi_T in L^2`, so `T` has an `L^2` density. To justify the fractional convolution, regularize

`k_epsilon(s)=1_{s>0}s^(-1/2)e^{-epsilon s}`.

Its Fourier transform (under `hat h(xi)=int e^{-i xi x}h(x)dx`) is

`hat k_epsilon(xi)=sqrt(pi)(epsilon+i xi)^(-1/2)`,

so

`|hat k_epsilon(xi)| <= sqrt(pi)|xi|^(-1/2)`.                             (4.4)

Moreover (4.1) gives

`int_R |phi_T(xi)| |xi|^(-1/2) dxi`
`<= 2[ int_0^K xi^(-1/2) dxi + int_K^infty K xi^(-3/2) dxi ]`
`=8 sqrt(K)`.                                                             (4.5)

Fourier inversion applied to `k_epsilon*p_T`, followed by (4.4)--(4.5), gives

`||k_epsilon*p_T||_infty <= [sqrt(pi)/(2pi)] 8sqrt(K)=4sqrt(K/pi)`.

Monotone convergence as `epsilon downarrow0` proves the same bound for `k*p_T`, and (4.2) follows from (4.3). For `a<0`, reflect the one-sided kernel. QED.

This is the precise way the account02/B18 conditional-square mechanism is used here: the rank-two residual need not have a bounded density; its borderline Fourier decay is enough after the extra physical square.

## 5. New target-level sufficient condition

Return to the rank-three form in Section 2. Set

`W_0=X_i + b^T X_{-i}/a`.

Because the original physical `X_i` is independent of `X_{-i}` and has density at most one, the conditional law of `W_0` given any measurable function of `X_{-i}`, in particular given `T=X_{-i}^T S X_{-i}`, is a mixture of translations of the `X_i` law and therefore has density at most one.

Under (3.1), Lemma 4 applied with (3.5) proves

`||p_{X^TAX}||_infty <= 4 sqrt(B(W)) / [ |a|^(1/2) D^(1/4) ]`.             (5.1)

Using determinant conservation (2.5),

`boxed: ||p_{X^TAX}||_infty <= 4 sqrt(B(W)) / [c |det Lambda| |a|]^(1/4)`. (5.2)

Since `B(W)<=e`, if the selected physical row satisfies

`c>1/2`,  `|a|>=delta>0`,  and `max d_j<=1/2`,                           (5.3)

and the three nonzero eigenvalues satisfy `|lambda_k|>=1`, then

`boxed: ||p_{X^TAX}||_infty <= 4 sqrt(e) (2/delta)^(1/4)`.                (5.4)

No moments, support, centering, identical-law, sign, or log-concavity hypotheses are used.

This is a genuine coupled/rotated rank-three theorem. It is complementary to the existing fully diffuse branch `max_i ||u_i||^2<=1/2`, which is already covered directly by the rank-three diffuse theorem with bound `3e`.

## 6. What this removes, and the exact remaining branch

For rank-exactly-three matrices with three large eigenvalues, the current state now covers:

1. **Fully diffuse frame:** every row leverage `<=1/2` — density `<=3e` by the existing diffuse theorem.
2. **One heavy row with a diffuse Schur residual and non-negligible Rayleigh pivot:** (5.3) — density bounded by (5.4).

The remaining rank-three geometry is therefore localized to at least one of the following:

- every heavy physical row has `|u_i^T Lambda u_i|` arbitrarily small (near-isotropic heavy rows in an indefinite form); or
- after selecting a heavy row with nonzero pivot, the exact residual two-dimensional frame `W` itself has a row leverage `>1/2`.

The fresh correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` shows that this remaining localized branch cannot be closed by asserting a universal single-pivot rank-two cross block. The correct next move is a second product-preserving heavy-row extraction / high-cardinality aggregation on the two-dimensional residual, or a direct treatment of near-isotropic heavy rows using their necessarily large off-diagonal coupling.

An elementary identity makes the latter concrete. For the selected row,

`a^2+||b||_2^2 = ||Lambda u||_2^2`.                                      (6.1)

Thus if the three eigenvalues have magnitude at least one and `c>1/2`, then

`||b||_2^2 >= c-a^2`.                                                     (6.2)

So the only way the square coefficient `a` can become too small for (5.4) is that the physical off-diagonal coupling vector becomes quantitatively large. This identifies a genuine alternate smoothing resource rather than a loss of total curvature. Turning (6.2) into a source-valid product-preserving bound without using the refuted single-Schur-rank-two extraction is the first unpaid inference.

## 7. Status

**Classification:** PROVED_SUPPORTING_THEOREM / ESSENTIAL_STEP_APPLIED.  
**Full target:** OPEN / NOT PROVED.  
**Independent end-to-end reviews:** not requested because this is not a full candidate proof.

No pointwise law-uniform stationary-phase claim, generic bounded-projection-density shortcut, bare cross-minor criterion, or conditional-density-under-sum/difference claim is used.
