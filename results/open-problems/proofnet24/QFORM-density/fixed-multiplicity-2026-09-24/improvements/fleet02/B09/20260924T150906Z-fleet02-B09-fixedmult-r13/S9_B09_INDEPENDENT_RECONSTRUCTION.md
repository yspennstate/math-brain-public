# QFORM-S9-B09-INDEPENDENT-RECONSTRUCTION-v1

Run: `20260924T150906Z-fleet02-B09-fixedmult-r13`.

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **complete replacement proof independently reconstructed in this run; threshold 9; multiplicity 8 and unrestricted multiplicity 3 remain open.** This is not a release certificate.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K`. Let `A=A^T`, `b in R^n`, `c in R`, and assume `s_9(A)>=s>0`. Then

`Q=X^TAX+b^TX+c`

has an essentially bounded density with

`||p_Q||_infty < 5338 K^2/s`.

The proof adds no support, moment, iid, sign, log-concavity, diagonal-basis, exact-rank, leverage, or post-rotation-independence hypothesis.

## Dependency map

From the pinned manuscript use only the already audited results:

- Fourier inversion/Riesz, lines 91–160;
- singular-value rank perturbation and Schur spectral count, lines 169–207;
- product-projection density and scalar Fourier powers, lines 258–301;
- scalar-square, definite-pair, hyperbolic-pair and quarter-power bounds, lines 404–525;
- no-pivot spectral-to-volume proposition, lines 582–619;
- fair literal-coordinate cut, lines 621–630;
- singular kernels and pivot half-potential estimates, lines 654–714.

The only new analytic input is the grouped product-Fourier lemma proved next, followed by two promotion corollaries.

## 1. Grouped product-Fourier lemma

Let `H,I,J` be disjoint original-coordinate banks, `Y=X_I`, `Z=X_J`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`, and suppose

`Q = F(X_H)+2<W,M_IY+M_JZ+beta>+R_I(Y)+2Y^T C_0 Z+R_J(Z)`

with arbitrary measurable same-bank phases. Assume `M_J` has row rank `k`; let `S` be the product of its nonzero singular values, with `S=1` for `k=0`. Project every row of `C_0` orthogonally off `row(M_J)` and call the residual row matrix `C`.

For `ell>=1`, define

`Z_ell = sum_{|T|=ell} det(C_T C_T^T) > 0`,

`w_T = det(C_T C_T^T)/Z_ell`,

`alpha_i = sum_{T contains i} w_T`,

and suppose `alpha_i<=1/2` for all rows. Put `d=k+ell`. Then, for `t!=0`,

`|phi_Q(t)| <= min(1, K_{k,ell}|t|^{-d/2})`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
 (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

If `d>2`, Fourier inversion gives

`||p_Q||_infty <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
 (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

### Proof

Push the complex measure `e^{itF}dP_H` to `W`. Its density `a_t` satisfies `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Push the remaining complex measure to `l=M_IY+M_JZ`, obtaining `mu_t`. Plancherel at scale `2t` gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                                                     (1)

Condition on literal `Y`. The conditional pushforward in `l` has density `tau_{t,Y}` because `M_J` has row rank `k`, and Hilbert-space Jensen gives

`||mu_t||_2^2 <= E_Y ||tau_{t,Y}||_2^2`.                                                          (2)

Insert a Gaussian Fourier cutoff and expand the squared Fourier norm with an independent copy `Z'`. With `D=Z-Z'`, averaging over the original independent coordinates of `Y` and discarding the remaining modulus-one phases leaves

`E_D kappa_epsilon(M_JD) prod_i |hat f_i(2t <a_i,D>)|`,                                           (3)

where `a_i` is row `i` of `C_0`; each coordinate of `D` is independent with density cap one.

Use determinant weights `w_T`. Since

`prod_i F_i = prod_T [prod_{i in T} F_i^(1/alpha_i)]^{w_T}`,

weighted Holder bounds (3) by the product over `T` of the corresponding `T`-integrals to powers `w_T`. For fixed `T`, write `c_i` for the residual row of `C`. The linear map

`D -> (M_JD, (<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T)`.

The manuscript product-projection lemma therefore bounds its density by

`e^(d/2)/[S sqrt(det(C_T C_T^T))]`.                                                               (4)

The removed row-space components of `a_i` become only translations once `M_JD` is fixed. Since `1/alpha_i>=2`, the manuscript scalar Fourier-power bound at scale `2t` gives, uniformly in every translation `u`,

`int |hat f_i(2t(y+u))|^(1/alpha_i) dy <= pi sqrt(2e alpha_i)/|t|`.                                (5)

Integrating the Gaussian kernel in the first `k` variables and using (4)–(5), then taking the weighted geometric mean, yields

`||mu_t||_2^2 <= e^(d/2) S^-1 pi^ell (2e)^(ell/2) |t|^-ell
  [prod_T det(C_T C_T^T)^(-w_T/2)] [prod_i alpha_i^(alpha_i/2)].`                                  (6)

Now

`prod_T det(C_T C_T^T)^(-w_T/2)=Z_ell^(-1/2) exp(H(w)/2)`.

Order a random `ell`-subset with law `w` uniformly. Entropy subadditivity gives

`H(w)+log(ell!) <= ell H(alpha/ell)
 = -sum_i alpha_i log alpha_i + ell log ell`,                                                       (7)

so

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining (1), (6), (7) and taking square roots gives exactly `K_{k,ell}`. Monotone convergence removes the Gaussian cutoff. For `d>2`,

`int_R min(1,K|t|^{-d/2})dt = [2d/(d-2)]K^(2/d)`;

multiplication by the inversion factor `1/(2pi)` gives the stated density constant. Every conditioning step is on original coordinates.

## 2. Exact-rank endpoints

For `r` literal physical coordinates crossing a disjoint product bank through a rank-`r` cross matrix `P`, with arbitrary same-bank phases retained, the same complex-pushforward/Plancherel calculation gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4) det(PP^T)^(-1/4)|t|^{-r/2}).`                                  (8)

For `r=3`, envelope integration gives

`||p||_infty <= 3 sqrt(e) det(PP^T)^(-1/6)`.                                                       (9)

For `r=2`, the Riesz identity gives the full half-potential bound

`sup_a E|Q-a|^(-1/2) <= 4 sqrt(2)e^(1/4) det(PP^T)^(-1/8)`.                                       (10)

No density conclusion is inferred from rank two alone.

## 3. Marginal-free order-three density receiver

Let `E_3(M)=e_3(MM^T)>0` for a literal cross block `M`. Give every row its inclusion mass in the determinant-squared distribution on row triples.

If all row masses are at most one half, apply the grouped lemma with `(k,ell,d)=(0,3,3)`. If a row `w` is heavier than one half, promote that literal coordinate to the retained hub and project the remaining rows off `w`. Exact Gram–Schmidt says

`||w||^2 e_2(C C^T) > E_3(M)/2`.

If the residual order-two masses are diffuse, apply `(1,2,3)`. Otherwise promote a second literal row, obtaining

`det(PP^T)||C_2||_F^2 > E_3(M)/4`.

If the residual order-one masses are diffuse, apply `(2,1,3)`. Otherwise promote a third row, whose literal three-row Gram determinant is `>E_3(M)/8`, and use (9). The largest of the four resulting constants is the fully diffuse one:

`C_3 = 3 sqrt(2)e(9/2)^(1/6) = 14.818337662843...`.

Therefore, with no leverage hypothesis,

`||p_Q||_infty <= C_3 E_3(M)^(-1/6)`.                                                            (11)

The characteristic function is integrable, so this branch has a continuous density.

## 4. Marginal-free order-two full half-potential receiver

Repeat the same promotion tree one dimension lower. The diffuse `(0,2,2)` branch has

`|phi(t)| <= min(1, L/|t|)`,

`L=pi e 2^(3/4) E_2(M)^(-1/4)`.

Then

`int |t|^(-1/2) min(1,L/|t|)dt = 8 sqrt(L)`,

and the Riesz coefficient gives

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,                                                       (12)

where

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.

One heavy row uses `(1,1,2)`; a second heavy row terminates at the exact rank-two endpoint (10), and both constants are smaller after the corresponding half-mass losses. Thus (12) is uniform and marginal-free.

## 5. Complete normalized `s_9` proof

Set `K=s=1`, `eta=1/100`, `kappa=1/80^2`, and suppose `s_9(A)>=1`.

### No pivot

The manuscript proposition at `k=3` gives `V_3(A)>=kappa^3`. The fair literal cut gives a cross block with

`E_3(M)>=4^-3 kappa^3`,

so `E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`. Equation (11) gives

`||p_Q||_infty <= 160 C_3 = 2370.93402605488...`.                                                 (13)

### Scalar pivot

If `|A_hh|>=eta`, completing the square in literal `X_h` leaves a Schur complement `S` with at least eight eigenvalues of modulus at least one.

If `S` has an `eta`-pivot, reusing the exact three constants in the manuscript's pivot-half-potential proof gives

- scalar subpivot: `H(S)<=10(20+12 log16)=532.7106466687737...`;
- definite pair: `H(S)<=40pi`;
- indefinite pair: `H(S)<=10(32+4log16)+4/e=432.375066654277...`.

Thus in every pivoted child

`sup_a E|S-a|^(-1/2) <= 1+10(20+12log16)=533.7106466687737...`.                                  (14)

If `S` has no pivot, its `s_5` is at least one. The manuscript volume proposition at `k=2` and fair cut give

`E_2(M_S)>=4^-2 kappa^2`.

Equation (12) therefore gives

`sup_a E|S-a|^(-1/2) <= C_2 sqrt(160)=152.99191115498024...`,                                     (15)

which is smaller than (14).

The outer scalar-square profile now yields

`||p_Q||_infty <= eta^(-1/2) * 533.7106466687737...
 = 5337.106466687737... < 5338`.                                                                  (16)

### Two-coordinate pivots

A definite pair of determinant modulus at least `eta` gives directly

`||p_Q||_infty <= pi/sqrt(eta)=10pi<32`.                                                          (17)

An indefinite pair removes two coordinates; its Schur complement still has at least seven unit spectral directions, hence operator norm at least one. The manuscript hyperbolic envelope plus logarithmic potential therefore gives the unchanged bound

`||p_Q||_infty <251`.                                                                              (18)

The four cases are exhaustive, and (16) dominates.

## 6. Scaling

For general `K,s`, put `Y=KX` and

`Q_tilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

The coordinates of `Y` have density cap one, `s_9(A/s)>=1`, and `Q=(s/K^2)Q_tilde`. Hence

`||p_Q||_infty < 5338 K^2/s`.

This proves the theorem.

## 7. B09 threshold obstruction below nine

The manuscript's rank bookkeeping is generically sharp. For arbitrary `r>=1` and `0<delta<1/10`, on disjoint `r`-sets `S,T,L`, the symmetric no-pivot matrix

`A=[[0,delta^2 I,delta I],[delta^2 I,0,delta I],[delta I,delta I,0]]`

with seed `A[S,T]=delta^2 I` has manuscript completion

`E=0`, `D=diag(0,0,-I_L)`,

`rank P=r`, `rank(R-P)=2r`, `rank R=3r`, `rank R_LL=r`,

and `V_{r+1}(A)=0`. Thus the `3r/r` support charges cannot be lowered abstractly. At `r=2`, this is precisely the algebraic saturation that appears one direction below the order-three `s_9` argument.

This family does not have eight unit spectral directions for small `delta`, so it is not a counterexample to an `s_8` density theorem. It proves only that multiplicity eight needs genuinely new spectral/analytic information rather than a generic rank-count improvement.

Current frontier: multiplicity **8 remains open**. The unrestricted three-eigenvalue conjecture remains **open**.
