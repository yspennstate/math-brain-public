# fleet02/B16 improvement — independently checked nine-eigenvalue replacement

Run: `fleet02-B16-20260924T141036Z-audit11`.

Baseline: pinned 790-line manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, source SHA-256 recorded by the package as `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **complete replacement proof checked in this B16 run**. This is one review/improvement artifact, not a release certificate. Threshold eight and the unrestricted three-eigenvalue conjecture remain open.

## Theorem

Let `X_1,...,X_n` be independent real random variables with densities bounded by `K`. Let `A=A^T` be arbitrary real symmetric, and let `b,c` be arbitrary. If

` s_9(A)>=s>0,`

then

`Q=X^TAX+b^TX+c`

has an essentially bounded density with

`||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s.`

No moments, support, iid, log-concavity, signature, exact-rank, diagonal-basis or post-rotation-independence assumption is added. Global continuity is not claimed.

Normalize to `K=s=1`, and retain the baseline `eta=1/100`, `kappa=1/80^2`.

## 1. Grouped product-Fourier compiler

Split the literal source coordinates into disjoint banks `H,I,J`. Let `W=U^T X_H in R^k` be an orthogonal projection whose joint density satisfies `||p_W||_infinity<=M_H`. Consider

`Q=F(X_H)+2 <W, M_I X_I+M_J X_J+beta>+R(X_I,X_J)`,                 (1)

where `F` is arbitrary measurable, `R` is arbitrary quadratic/affine, and `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J` (`S=1` for `k=0`). Write the literal `I-J` cross rows of the quadratic part of `R` as `a_i`, and decompose

`a_i=c_i+lambda_i M_J`, with `c_i` orthogonal to `row(M_J)`.

Let `C` be the row matrix with rows `c_i`. For `ell>=1`, put

`Z_ell=sum_(|T|=ell) det(C_T C_T^T)>0`,
`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=sum_(T contains i) w_T`.

Discard indices with `alpha_i=0` (their Fourier factors have modulus at most one), and assume every remaining `alpha_i<=1/2`. Put `d=k+ell`.

Then, for `t!=0`,

`|phi_Q(t)| <= min(1,K_(k,ell)|t|^(-d/2))`,                       (2)

where

`K_(k,ell)=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`           (3)

If `d>2`, Fourier inversion yields

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d))(ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d)).`                                      (4)

### Proof, including rough laws

Push the complex measure `e^{itF}dP_H` through `W`; its density `a_t` is dominated in variation by `p_W`. Hence

`||a_t||_2^2<=M_H`.

Plancherel and the dilation `xi=2t(y+beta)` give

`int |hat a_t(2t(y+beta))|^2 dy <= M_H (pi/|t|)^k.`               (5)

Push `e^{itR}dP_(I,J)` through `Y=M_I X_I+M_J X_J`; call the complex density `mu_t`. This density exists and is in `L^2`: conditional on `X_I`, its variation is dominated by the density of `M_JX_J`, which by the baseline product-projection theorem is bounded by `e^(k/2)/S`; averaging preserves that cap. Cauchy--Schwarz in `y` therefore gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2.`                    (6)

It remains to sharpen `||mu_t||_2`. Let `rho_eps` be a compact approximate identity on `R^k` and `kappa_eps=rho_eps*tilde(rho_eps)`. Conditional on `X_I=x`, convolve the corresponding complex pushforward with `rho_eps`. Pointwise Jensen followed by integration gives an upper bound on the squared `L^2` norm by the average of the conditional squared norms. Expanding the latter uses an independent copy `X'_J` only. With `D=X_J-X'_J`, the shift `M_Ix` cancels, pure `I` terms cancel, and pure `J` terms have modulus one. Averaging over the literal independent `I` coordinates gives

`||mu_t*rho_eps||_2^2
 <= E_D [ kappa_eps(M_JD) prod_i |hat f_i(2t<a_i,D>)| ].`          (7)

The coordinates of `D` are independent and have densities bounded by one. The bound derived below is uniform in `eps`. Since `mu_t in L^2`, approximate-identity convergence in `L^2` passes (7) to the unsmoothed density. Thus no conditional marginal cap, moment or smoothness is inserted.

For every positive-volume `ell`-set `T`, the linear map

`D -> (M_JD, (<c_i,D>)_(i in T))`

has Gram determinant

`S^2 det(C_T C_T^T)`,                                             (8)

because the `c_i` are orthogonal to `row(M_J)`. The baseline product-projection theorem plus deterministic whitening therefore bounds this joint density by

`e^(d/2)/[S sqrt(det(C_T C_T^T))].`                               (9)

Represent the product in (7) as a weighted geometric product over `T` and apply Holder with weights `w_T`. For each included row the Holder exponent is `1/alpha_i>=2`. The baseline scalar Fourier-power estimate gives, uniformly in the shift `u`,

`int |hat f_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`                                    (10)

The `kappa_eps` factor integrates to one in the first `k` projected variables. Hence weighted Holder, (9) and (10) give

`||mu_t||_2^2 <= e^(d/2) S^-1 pi^ell(2e)^(ell/2)|t|^-ell
                  Z_ell^-1/2
                  exp[(H(w)+sum_i alpha_i log alpha_i)/2].`       (11)

To control the entropy, first sample `T~w` and then order its `ell` elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`; each of its `ell` coordinate marginals is `alpha_i/ell`. Entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`        (12)

Insert (12) into (11), then into (6), and take square roots. This is exactly (2)--(3). Finally

`int_R min(1,K|t|^(-d/2))dt = [2d/(d-2)] K^(2/d)`                (13)

for `d>2`; the factor `pi` cancels against Fourier inversion and gives (4).

For `k=0`, the same proof starts directly from the baseline second-power decoupling; there is no `kappa_eps` variable. This is exactly the zero-dimensional interpretation of the formulas above.

## 2. Exact-rank terminal receivers

If `r` literal physical source coordinates cross an independent product bank through a rank-`r` row matrix `P`, keep those physical coordinates as the hub. Their joint density is bounded by one. Conditional variation of the pushforward through the crossed bank is bounded by `e^(r/2)/S`, where `S^2=det(PP^T)`. The same Plancherel argument gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4) det(PP^T)^(-1/4)|t|^(-r/2)).` (14)

Consequently

`r=3: ||p||_infinity <= 3 sqrt(e) det(PP^T)^(-1/6),`              (15)

and the baseline Riesz formula gives

`r=2: sup_a E|Q-a|^-1/2 <= 4 sqrt(2)e^(1/4) det(PP^T)^(-1/8).`   (16)

All same-bank phases remain inside complex measures; no projected coordinates are made independent.

## 3. Third crossing volume gives a bounded density

For a literal cross-row matrix `B`, let

`Z=E_3(B)=sum_(|T|=3) det(B_TB_T^T)>0`.

Let `J_i` be the determinant mass of triples containing physical row `i`; `sum_i J_i=3Z`.

**Diffuse branch.** If every `J_i/Z<=1/2`, apply (4) with `(k,ell,d)=(0,3,3)`. This gives

`||p_Q||_infinity <= C_3 Z^-1/6`,
`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                  (17)

**One promoted row.** If `J_i>Z/2`, let `w` be row `i` and orthogonally project all other rows off `w`, obtaining `C`. Gram--Schmidt and Cauchy--Binet give the exact identity

`J_i=||w||^2 E_2(C).`                                            (18)

If the residual order-two inclusion marginals are diffuse, apply `(k,ell,d)=(1,2,3)` with the literal physical source `X_i` as hub. The coefficient after `J_i>Z/2` is `<10.958 Z^-1/6`.

**Two promoted rows.** If a residual row is heavy, promote that literal row as well. If `P` is the resulting two-row matrix and `C_2` the remaining rows projected off `row(P)`, exact base-times-height gives

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4.`                       (19)

If the residual one-volume marginals are diffuse, `(k,ell,d)=(2,1,3)` gives `<8.264 Z^-1/6`.

**Three promoted rows.** If one residual row is heavy, its literal three-row Gram determinant exceeds `H_ij/2>Z/8`. Apply (15), giving `<7 Z^-1/6`.

Thus the diffuse coefficient (17) dominates all branches:

`boxed: ||p_Q||_infinity <= C_3 E_3(B)^(-1/6).`                  (20)

Every branch here has an integrable characteristic-function majorant.

## 4. Second crossing volume gives a full negative-half potential

Let `Z=E_2(B)>0` and define incident masses analogously.

If all inclusion marginals are `<=1/2`, (2)--(3) with `(k,ell,d)=(0,2,2)` gives

`|phi(t)|<=min(1,L/|t|)`,
`L=pi e 2^(3/4) Z^-1/4.`                                        (21)

The baseline Riesz identity and

`int_R |t|^-1/2 min(1,L/|t|)dt=8 sqrt(L)`                       (22)

give

`sup_a E|Q-a|^-1/2 <= C_2 Z^-1/8`,
`C_2=8 sqrt(e) 2^-1/8=12.095072570796486...`.                   (23)

If a row is heavy, promote it. Exact Gram--Schmidt gives `J_i=||w||^2 E_1(C)>Z/2`. A diffuse residual one-volume branch uses `(k,ell,d)=(1,1,2)` and has coefficient `<9.79 Z^-1/8`; a heavy residual row gives a rank-two Gram determinant `>Z/4` and (16), with coefficient `<8.64 Z^-1/8`. Hence (23) is uniform without any marginal assumption.

This is deliberately a **half-potential** theorem, not a rank-two density theorem.

## 5. Assembly under nine large singular values

### 5.1 No physical pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited baseline spectral-to-volume proposition at order three gives

`V_3(A)>=kappa^3`.

A fair literal coordinate cut gives a crossing block `B` with

`E_3(B)>=4^-3 kappa^3`,

so `E_3(B)^(-1/6)<=2 kappa^-1/2=160`. By (20),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488...<2400.`                                     (24)

### 5.2 Scalar pivot

If `|A_hh|>=eta`, complete the square in that original coordinate. The Schur complement `R` retains at least eight eigenvalues of modulus at least one.

If `R` has an `eta`-pivot, the baseline pivot calculation (which only needs two surviving large directions) gives the exact worst truncated bound

`H(R)<=200+120 log16`.

The kernel outside distance one is at most one, hence

`sup_a E|R-a|^-1/2 <=201+120 log16.`                              (25)

If `R` has no pivot, then in particular `s_5(R)>=1`. The baseline spectral-to-volume proposition at order two and a fair cut give

`E_2(B_R)>=4^-2 kappa^2`.

Equation (23) yields

`sup_a E|R-a|^-1/2 <= C_2 sqrt(160)
 =152.99191115498...`,                                           (26)

which is smaller than (25). The outer scalar square profile costs `eta^-1/2=10`, so

`||p_Q||_infinity <=2010+1200 log16
 =5337.106466687737...<5338.`                                    (27)

### 5.3 Two-coordinate pivots

A definite pair has conditional density at most

`pi/sqrt(eta)=10pi<32`.

For an indefinite pair, the Schur complement retains at least seven unit-scale eigenvalues, hence operator norm at least one. The audited baseline hyperbolic envelope plus the quarter-power logarithmic potential gives the same bound as in the baseline main proof,

`||p_Q||_infinity <251.`                                        (28)

The no-pivot, scalar-pivot, definite-pair and indefinite-pair cases exhaust the normalized problem. The scalar branch (27) is largest.

## 6. Scaling

For general `K,s`, let `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q`.

The coordinates of `Y` have density caps one and `s_9(A/s)>=1`. Therefore (27) and density scaling give

`boxed: ||p_Q||_infinity <=(2010+1200 log16) K^2/s <5338 K^2/s.`  (29)

## Closed dependency map

Baseline inputs independently checked in this B16 run:

`Fourier/Gaussian/Riesz -> geometric BL -> product projection -> scalar Fourier powers`;

`Schur count + square/definite/hyperbolic physical pivots + quarter-power logarithmic control`;

`disjoint-minor sampling + nonsymmetric completion + global/restricted rank + diagonal dominance -> no-pivot V_2,V_3`;

`fair literal coordinate cut -> E_2,E_3 crossing volumes`.

New proof supplied above:

`complex source-bank pushforward + Plancherel + mollified conditional square -> grouped compiler`;

`weighted determinant subsets + entropy -> diffuse receiver`;

`exact Gram--Schmidt row promotion -> marginal-free E_3 density and E_2 half-potential`;

`those receivers + baseline pivot/volume alternatives -> normalized s_9 theorem -> K,s scaling`.

No external theorem or peer verdict is a logical dependency of (29).

## Why this proof does not claim threshold eight

The current structural order-three argument has a genuine bookkeeping endpoint at the worst bad-ratio seed `r=2`: `rank R<=6` and `rank R[L,L]<=2`. With only `s_8>=1`, rank subtraction can force only two large diagonal residual entries, and an invertible `2x2` block is compatible with restricted rank two. I independently checked a finite exact interpolation example attaining `rank R=6` and `rank R[L,L]=2`; this shows the two rank constants cannot be lowered by a cosmetic support recount, though it is not itself an `s_8` counterexample.

Analytically, order two is also only an endpoint half-potential resource. For independent `U,V~Uniform[-1,1]`, the density of `U^2-V^2` is infinite at zero because

`int_0^1 (1/(2 sqrt y))^2 dy=infinity.`

Thus a generic order-two indefinite receiver cannot supply the missing bounded-density endpoint. A proof at eight or below must exploit additional structure beyond the present rank bookkeeping and generic `E_2` receiver.
