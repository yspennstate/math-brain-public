SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-24T14:02:04.972115Z.
attacking: after a full PASS audit of the pinned 17-eigenvalue manuscript, independently reconstruct a complete nine-eigenvalue replacement with explicit constants; do not claim the unrestricted three-eigenvalue theorem.

# fleet02/B12 auto11 — complete nine-eigenvalue replacement

Pinned baseline dependency: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This proof is an independent reconstruction of the order-three/order-two grouped product-Fourier route. I use only baseline lemmas that passed the sibling end-to-end audit and reprove the new grouped step here with an explicit Gaussian Fourier cutoff, so there is no unproved approximate-identity passage.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, `b in R^n`, `c in R`, and suppose

` s_9(A) >= s > 0.`

Then `Q=X^TAX+b^TX+c` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 6010 K^2/s.`

The no-pivot Fourier branch has a continuous `C_0` density. Global continuity is not claimed by this proof. The unrestricted three-eigenvalue QFORM conjecture remains OPEN.

## Dependency map from the audited baseline

All line numbers refer to the pinned 790-line manuscript.

1. Fourier/Riesz normalization: lines 91--160.
2. Schur spectral count and singular-value rank inequalities: lines 169--207.
3. Product-projection density bound: lines 258--282.
4. Scalar Fourier powers: lines 284--301.
5. Scalar-square profile, definite pair, hyperbolic pair, quarter-power/log potential: lines 404--525.
6. No-pivot spectral-to-volume proposition: lines 582--619.
7. Fair original-coordinate cut: lines 621--630.
8. Pivot truncated-half-potential bound: lines 676--714.

No moment, support, smoothness, iid, log-concavity, leverage, exact-rank, diagonal-basis, or post-rotation-independence assumption is added.

Throughout the normalized proof use

`eta=1/100`, `kappa=1/80^2`.

## 1. Grouped product-Fourier lemma

Let `H,I,J` be disjoint sets of original coordinates. Put `Y=X_I`, `Z=X_J`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`. Consider

`Q = F(X_H) + 2 <W, M_I Y + M_J Z + beta>
     + R_I(Y) + 2 Y^T C_0 Z + R_J(Z)`,                            (1.1)

where `F,R_I,R_J` are arbitrary measurable/quadratic phases allowed by the original polynomial, `M_J` has row rank `k`, and all affine terms may be absorbed in the displayed pieces. Let

`S = product of the k nonzero singular values of M_J`              (1.2)

(with `S=1` for `k=0`). For each row `a_i` of `C_0`, decompose

`a_i = c_i + lambda_i M_J`,                                       (1.3)

where `c_i` is orthogonal to `row(M_J)`. Let `C` be the matrix of rows `c_i`.

Fix `ell>=1` and define

`Z_ell = sum_{|T|=ell} det(C_T C_T^T) > 0`,                        (1.4)

`w_T = det(C_T C_T^T)/Z_ell`,                                    (1.5)

`alpha_i = sum_{T contains i} w_T`.                               (1.6)

Assume `alpha_i<=1/2` for every row and put `d=k+ell`.

### Lemma 1

For `t!=0`,

`|phi_Q(t)| <= min(1, K_{k,ell}|t|^{-d/2})`,                      (1.7)

where

`K_{k,ell}
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`                   (1.8)

If `d>2`,

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`            (1.9)

### Proof

Push the complex measure `exp(itF)dP_H` to `W`. Its density `a_t` obeys

`|a_t|<=p_W`, `||a_t||_2^2<=M_H`.                                 (1.10)

Let `mu_t` be the complex pushforward of `exp(it[R_I+2Y^TC_0Z+R_J])dP_{Y,Z}` under

`l=M_IY+M_JZ`.

It has an `L^2` density: `M_JZ` has a bounded `k`-dimensional density by the audited product-projection lemma and full row rank of `M_J`, and the complex pushforward is dominated in total variation by the corresponding ordinary pushforward. Fourier pairing followed by `k`-dimensional Plancherel gives

`|phi_Q(t)|^2
 <= M_H (pi/|t|)^k ||mu_t||_2^2.`                               (1.11)

For completeness, the `k`-dimensional Plancherel constant is `(2pi)^k`; after the change `xi=2t(l+beta)` it becomes `(pi/|t|)^k`.

It remains to bound `||mu_t||_2`. Conditional on `Y=y`, let `tau_{t,y}` be the complex pushforward of

`exp(it[R_J(Z)+2y^TC_0Z])dP_Z`

under `M_JZ`. Hilbert-space Jensen gives

`||mu_t||_2^2 <= E_Y ||tau_{t,Y}||_2^2`.                           (1.12)

To evaluate the right side without a distributional delta, insert the Gaussian Fourier cutoff `exp(-eps|xi|^2)`, `eps>0`, in Plancherel. Expanding the square with an independent copy `Z'`, then averaging over `Y`, yields

`E_Y (2pi)^(-k) int e^{-eps|xi|^2}|hat tau_{t,Y}(xi)|^2 dxi`

`<= E_D [ kappa_eps(M_JD)
          prod_{i in I} |hat f_i(2t <a_i,D>)| ],`                  (1.13)

where `D=Z-Z'` has independent coordinate densities bounded by one and

`kappa_eps(u)=(4pi eps)^(-k/2) exp(-|u|^2/(4eps))`                 (1.14)

is a probability density. Same-bank `R_J` phases have modulus one; the `R_I` phase disappeared before (1.12). Thus arbitrary same-bank curvature is retained, not deleted.

Now apply weighted Holder to (1.13): for a subset `T` of size `ell`, the relevant integral contains

`kappa_eps(M_JD) prod_{i in T}|hat f_i(2t<a_i,D>)|^(1/alpha_i)`.   (1.15)

The full-row-rank linear map

`D -> (M_JD, (<c_i,D>)_{i in T})`                                 (1.16)

has Gram determinant

`S^2 det(C_T C_T^T)`.                                             (1.17)

Indeed the `c_i` are orthogonal to `row(M_J)`, so the two Gram blocks are orthogonal. By the audited product-projection lemma plus deterministic singular-value scaling, its pushforward density is at most

`e^(d/2) / [ S sqrt(det(C_T C_T^T)) ].`                            (1.18)

The shifts `lambda_i M_JD` in (1.3) are harmless inside one-dimensional integration. Since `1/alpha_i>=2`, the audited scalar Fourier-power lemma gives

`int_R |hat f_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`                                     (1.19)

Therefore the `T`-integral is at most

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_{i in T} sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))].`                                     (1.20)

Take the weighted geometric mean over `T`. Since

`w_T = det(C_TC_T^T)/Z_ell`,

the determinant factor equals

`Z_ell^(-1/2) exp(H(w)/2)`.                                      (1.21)

The marginal factors equal

`exp[(1/2) sum_i alpha_i log alpha_i]`.                           (1.22)

To bound the entropy exactly, sample `T` with law `w` and then order its `ell` elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`. Every ordered position has marginal `alpha_i/ell`, hence entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i
 <= ell log ell - log(ell!).`                                     (1.23)

Equations (1.20)--(1.23) bound the right side of (1.13), uniformly in `eps`. On the left, `exp(-eps|xi|^2)` increases to one as `eps downarrow0`, so monotone convergence and Plancherel give the same bound for `E||tau||_2^2` and hence `||mu_t||_2^2`. Combining with (1.11) and taking square roots gives exactly (1.7)--(1.8).

Finally

`int_R min(1,K|t|^(-d/2))dt = [2d/(d-2)] K^(2/d)`                (1.24)

for `d>2`. Fourier inversion cancels the `pi` factor in `K^(2/d)` and yields (1.9). QED.

No random coordinate is rotated in this argument. Orthogonal decompositions occur only in deterministic row spaces and in pushforward-density calculations.

## 2. Terminal exact-rank bounds

For `r` literal original physical coordinates crossing an opposite product bank through a rank-`r` block `P`, arbitrary same-bank/affine phases retained, the same complex-pushforward/Plancherel argument with no residual rows gives

`|phi(t)| <= min(1,
  pi^(r/2)e^(r/4)[det(PP^T)]^(-1/4)|t|^(-r/2)).`                 (2.1)

Indeed the physical `r`-coordinate density cap is one, while the opposite `r`-dimensional linear projection has density cap at most `e^(r/2)/sqrt(det(PP^T))`.

For `r=3`, direct envelope integration gives

`||p||_infinity <= 3 sqrt(e) [det(PP^T)]^(-1/6).`                 (2.2)

For `r=2`, the audited Riesz identity gives

`sup_a E|Q-a|^(-1/2)
 <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8).`                           (2.3)

These are respectively a density statement and a half-potential statement; (2.3) is not misused as a rank-two density bound.

## 3. Marginal-free third crossing volume

For a literal original-coordinate cross block `M`, let

`E_3(M)=e_3(MM^T)=:Z>0`.                                         (3.1)

For physical row `i`, let `J_i` be the sum of three-row Gram determinants containing `i`, so `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, Lemma 1 with `(k,ell,d)=(0,3,3)` gives

`||p_Q||_infinity <= C_3 Z^(-1/6)`,                              (3.2)

where

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843... .`                 (3.3)

If some `J_i>Z/2`, promote that literal row `w=m_i` and project every other row orthogonally off `w`, obtaining `C`. Gram--Schmidt gives

`J_i=||w||^2 e_2(CC^T).`                                         (3.4)

If all residual `E_2` row marginals are at most `1/2`, Lemma 1 with `(1,2,3)` applies; the powers of `||w||` cancel and the resulting constant is `<C_3` times `Z^(-1/6)`.

Otherwise promote a residual row `j` of marginal greater than `1/2`. If `P` denotes the two promoted rows and `C_2` the remaining rows projected off `row(P)`, then another exact Gram--Schmidt sum gives

`H_ij:=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4.`                      (3.5)

If all one-volume marginals of `C_2` are at most `1/2`, Lemma 1 at `(2,1,3)` gives a constant `<C_3 Z^(-1/6)`.

Otherwise promote one more row. Its three-row Gram determinant is `>H_ij/2>Z/8`, and (2.2) gives

`||p_Q||_infinity < 3 sqrt(2e) Z^(-1/6) < C_3 Z^(-1/6).`         (3.6)

Thus in all cases

`boxed: ||p_Q||_infinity <= C_3 E_3(M)^(-1/6).`                  (3.7)

Every branch above has an integrable characteristic-function envelope, hence this fixed-cross-block receiver has a continuous `C_0` density.

## 4. Marginal-free second crossing volume

Let

`E_2(M)=e_2(MM^T)=:Z>0`.                                         (4.1)

If every `E_2` row marginal is at most `1/2`, Lemma 1 at `(0,2,2)` gives

`|phi(t)| <= min(1,
 pi e 2^(3/4) Z^(-1/4)|t|^(-1)).`                                (4.2)

Since

`int_R min(1,L/|t|)|t|^(-1/2)dt = 8 sqrt(L)`,                    (4.3)

the audited Riesz inequality yields

`sup_a E|Q-a|^(-1/2)
 <= C_2 Z^(-1/8)`,                                                (4.4)

where

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796... .`                    (4.5)

If a row `i` carries more than half the `E_2` mass, project the other rows off `w=m_i`. If all residual one-volume marginals are at most `1/2`, Lemma 1 at `(1,1,2)` plus (4.3) gives a smaller constant after using the exact identity

`K_i=||w||^2||C||_F^2>Z/2`.                                      (4.6)

If a residual row has marginal greater than `1/2`, the corresponding literal two-row Gram determinant satisfies `D>Z/4`; (2.3) again gives a constant smaller than `C_2 Z^(-1/8)`. Therefore

`boxed: sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8).`               (4.7)

The logarithmic/rank-two endpoint is respected: this is only a half-potential conclusion.

## 5. Nine large eigenvalues close every branch

Normalize first to `K=s=1` and assume `s_9(A)>=1`.

### 5.1 No physical pivot

If `A` has no `eta`-pivot, the audited baseline spectral-to-volume proposition with order `k=3` gives

`V_3(A)>=kappa^3`.                                                (5.1)

The audited fair original-coordinate cut gives a literal cross block `M` with

`E_3(M)>=4^(-3)kappa^3`,                                         (5.2)

so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160.`                             (5.3)

By (3.7),

`||p_Q||_infinity
 <=160 C_3
 =2370.93402605488... < 2371.`                                   (5.4)

This branch is continuous `C_0`.

### 5.2 Scalar pivot

Suppose `|A_hh|>=eta`. Complete the square in the literal original coordinate `X_h`. The audited Schur count leaves at least eight eigenvalues of modulus at least one in the residual Schur complement `S`.

If `S` has an `eta`-pivot, the audited baseline pivot proposition applies (it needs only two surviving large eigenvalues) and gives truncated half potential `<=600`; outside distance one the half kernel is `<=1`. Therefore

`sup_a E|R-a|^(-1/2) <=601.`                                     (5.5)

If `S` has no pivot, then `s_5(S)>=1`. Apply the audited baseline spectral-to-volume proposition with order `k=2` and a fair cut:

`E_2(M_S)>=4^(-2)kappa^2`.                                       (5.6)

Equation (4.7) gives

`sup_a E|R-a|^(-1/2)
 <= C_2 sqrt(160)
 =152.99191115498... <153.`                                      (5.7)

Hence (5.5) is valid in both scalar-pivot subcases. The audited conditional square profile gives

`||p_Q||_infinity
 <= eta^(-1/2)*601
 =6010.`                                                          (5.8)

This step is valid for rough laws because the completing-square shift is conditional on original coordinates and the profile is a domination of measures, not an independence assertion.

### 5.3 Two-coordinate pivot

If no scalar pivot is chosen but a definite principal pair has determinant magnitude at least `eta`, the audited deterministic two-dimensional polar calculation gives

`||p_Q||_infinity <= pi/sqrt(eta)=10pi<32.`                       (5.9)

If the principal pair is indefinite, its Schur complement retains at least seven eigenvalues of modulus at least one, hence operator norm at least one. The audited hyperbolic logarithmic envelope plus quarter-power logarithmic potential therefore gives, exactly as in the baseline main proof,

`||p_Q||_infinity <251.`                                         (5.10)

The logarithmic endpoint cannot be replaced by a bounded conditional pair density: for independent uniform `X,Y in[-1/2,1/2]`, the density of `X^2-Y^2` diverges like `log(1/|z|)` at zero. The residual log-potential in (5.10) is essential.

The no-pivot, scalar-pivot, definite-pair, and indefinite-pair branches are exhaustive. Their maximum is 6010. This proves the normalized theorem.

## 6. Scaling

For general `K,s`, set `Y=KX`. The coordinates of `Y` have densities bounded by one. Define

`Q_tilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then `s_9(A/s)>=1` and

`Q=(s/K^2)Q_tilde`.

The normalized result and the scalar density change of variables give

`boxed: ||p_Q||_infinity <=6010 K^2/s.`                           (6.1)

## 7. Why this proof stops at nine

The new analytic endpoint uses order-three crossing volume for a density. The audited interpolation proposition forces that volume from `s_{4*3-3}=s_9`. At multiplicity eight, only the terminal sampled ratio `r=2` can fail; the repository contains a proved structural description of that chamber, but no complete density receiver for it. Rank-two/order-two crossing information alone cannot be promoted to a density bound because the opposite-sign logarithmic example above is a genuine obstruction.

Therefore this run lowers the complete fixed-multiplicity theorem from 17 to **9**, and no further. This is not a counterexample to an eight-eigenvalue theorem and not a proof of unrestricted three-eigenvalue QFORM.

## 8. Review status

- Pinned 17-eigenvalue baseline: PASS in this run's sibling audit.
- Nine-eigenvalue theorem above: complete replacement proof supplied here with explicit constants and dependency map; mathematical status **PASS in this independent reconstruction**, while repository release/validation policy remains a separate owner/keeper decision.
- Eight eigenvalues: OPEN in this route.
- Three eigenvalues: OPEN.

Execution context: `WITHOUT_VERIFIED_BRAIN`; repository transport is not native Brain ingestion.
