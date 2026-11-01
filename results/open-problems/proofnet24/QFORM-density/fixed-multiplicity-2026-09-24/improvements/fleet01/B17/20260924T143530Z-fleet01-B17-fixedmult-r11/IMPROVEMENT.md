# QFORM fixed multiplicity: complete replacement proof at multiplicity nine

Run: `20260924T143530Z-fleet01-B17-fixedmult-r11`  
Pinned baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

**Status:** complete written **candidate** lowering `17 -> 9`, preserving the full rough-law scope. This file does not self-award independent-validation or release status. The owner gate still requires two genuinely separate full reviews of this replacement proof. It does not prove the three-eigenvalue conjecture.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

` s_9(A) >= s > 0, `

then

` Q=X^TAX+b^TX+c `

has an essentially bounded density and

` ||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s. `

No moment, support, smoothness, iid, sign, Gaussian, log-concavity, exact-rank, leverage, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity is obtained on the new no-pivot Fourier branch, but is not asserted globally across the measure-domination pivot branches.

The proof retains the audited baseline constants

` eta=1/100,   kappa=1/80^2=1/6400. `

The new ingredients are a rough-law-safe grouped physical-product Fourier compiler, a marginal-free order-three density receiver, and a marginal-free order-two full negative-half-potential receiver. They are proved below using only the baseline product-projection lemma, scalar Fourier-power lemma, Plancherel, Gaussian regularization, weighted Holder, Gram determinants and physical row promotion.

---

## 1. Grouped physical-product Fourier compiler

Let `H,I,J` be disjoint banks of original coordinates. Let `W=U^T X_H` be a `k`-dimensional orthogonal projection of the hub coordinates, with density cap

` ||p_W||_infinity <= M_H. `

Consider

` Q=F(X_H)+2<W,M X'+beta>+R(X'),   X'=(X_I,X_J), `

where `F` is arbitrary measurable and finite a.s., and `R` is an arbitrary quadratic/affine polynomial in the light original coordinates. Assume the literal `J` restriction `M_J` has row rank `k`; let `S` be the product of its nonzero singular values. For each physical `I` row `a_i` of the `I-J` crossing of `R`, decompose

` a_i=c_i+lambda_i M_J,   c_i perpendicular to row(M_J). `

Let `C` be the matrix with rows `c_i`. For an integer `ell>=1` put

` Z_ell=sum_(|T|=ell) det(C_T C_T^T)>0, `

` w_T=det(C_T C_T^T)/Z_ell, `

` alpha_i=sum_(T contains i) w_T. `

Assume every positive `alpha_i<=1/2`, and put `d=k+ell`.

### Lemma 1 — compiler

For every `t!=0`,

` |phi_Q(t)| <= min(1,K_(k,ell)|t|^(-d/2)), `

where

` K_(k,ell)
 =M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
  (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4). `

If `d>2`,

` ||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)). `

### Proof

Push the complex measure `e^(itF)dP_H` through `W`. Its total variation is dominated by the actual law of `W`, hence it has a complex density `a_t` with `|a_t|<=p_W` and

` ||a_t||_2^2<=M_H. `

Push `e^(itR)dP_(X')` through `L=M X'`; denote the complex density by `mu_t`. Full row rank of `M_J`, polar decomposition and the baseline product-projection lemma show that `M_JX_J`, hence `L`, has an absolutely continuous bounded law, so total-variation domination gives such a density. Pairing the pushforwards, Cauchy–Schwarz, `k`-dimensional Plancherel and `u=2t(l+beta)` give

` |phi_Q(t)|^2 <= M_H(pi/|t|)^k ||mu_t||_2^2. `                 (1.1)

It remains to control `||mu_t||_2` without a conditional-density shortcut. Let `D=X_J-X'_J`, where `X'_J` is an independent copy. Each coordinate of `D` has an independent density bounded by one. For `epsilon>0` put

` G_epsilon(x)=(4pi epsilon)^(-k/2) exp(-|x|^2/(4epsilon)). `

By Plancherel,

` ||mu_t||_2^2=(2pi)^(-k) int |hat(mu_t)(xi)|^2 dxi. `

Apply Cauchy–Schwarz in the probability law of `X_I`, multiply by `exp(-epsilon|xi|^2)`, expand the square using only the independent copy `X'_J`, and integrate in `xi`. The pure `I` phases cancel, the pure `J-J'` phase has modulus one, and averaging the original independent coordinates `X_i`, `i in I`, produces their physical characteristic functions. Gaussian Fourier inversion gives

` (2pi)^(-k) int exp(-epsilon|xi|^2)|hat(mu_t)(xi)|^2 dxi
 <= E[ G_epsilon(M_JD) prod_i |psi_i(2t<a_i,D>)| ]. `          (1.2)

The left side increases to `||mu_t||_2^2` as `epsilon downarrow0`. We bound the right side uniformly.

Weighted Holder with subset law `w_T` gives

` E[G_epsilon(M_JD) prod_i |psi_i(2t<a_i,D>)|]
 <= prod_T I_T^(w_T), `                                          (1.3)

where

` I_T=E[G_epsilon(M_JD)
       prod_(i in T)|psi_i(2t<a_i,D>)|^(1/alpha_i)]. `

For a positive-weight `T`, the literal linear image

` D -> (M_JD,(<c_i,D>)_(i in T)) `

has row-Gram determinant

` S^2 det(C_T C_T^T). `

The baseline product-projection lemma and deterministic polar decomposition therefore bound its joint density by

` e^(d/2)/[S sqrt(det(C_T C_T^T))]. `                              (1.4)

Since `<a_i,D>=<c_i,D>+lambda_i M_JD`, integrate first in this joint image. `G_epsilon` has total mass one, and translations of the one-dimensional Fourier arguments cost nothing. Because `1/alpha_i>=2`, the baseline scalar Fourier-power lemma yields

` int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|. `                                   (1.5)

Thus

` I_T <= e^(d/2)[pi sqrt(2e)/|t|]^ell
          prod_(i in T)sqrt(alpha_i)
          /[S sqrt(det(C_T C_T^T))]. `                           (1.6)

Now `det(C_TC_T^T)=w_T Z_ell`. The determinant geometric mean contributes

` Z_ell^(-1/2) exp(H(w)/2), `

and the row factors contribute

` exp((1/2)sum_i alpha_i log alpha_i). `

To bound the entropy exactly, sample an `ell`-set with law `w` and then order its elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`, and each coordinate position has marginal `alpha_i/ell`. Entropy subadditivity therefore gives

` H(w)+log(ell!)
 <= -sum_i alpha_i log alpha_i + ell log ell, `

or

` H(w)+sum_i alpha_i log alpha_i
 <= ell log ell-log(ell!). `                                     (1.7)

Insert (1.6)–(1.7) into (1.3), then into (1.2), let `epsilon downarrow0`, and use (1.1). Taking square roots gives the displayed `K_(k,ell)`. If `d>2`,

` int_R min(1,K|t|^(-d/2))dt=2d/(d-2) K^(2/d), `

and Fourier inversion gives the density formula. Every conditioning/promotion used above is on literal original-coordinate product banks. QED.

---

## 2. Exact-rank physical crossing terminal

We also need a terminal when all required smoothing dimensions have been promoted to genuine physical hub coordinates.

### Lemma 2 — exact-rank crossing

Let `X,Y` be independent random vectors and let `B=U Sigma V^T` have exact rank `r`, with singular-value product `P`. Assume `U^TX` and `V^TY` have density caps `M_X,M_Y`. For arbitrary measurable real `F,G`,

` Q=F(X)+2X^TBY+G(Y) `

satisfies

` |phi_Q(t)| <= min(1,(pi/|t|)^(r/2)(M_XM_Y)^(1/2)P^(-1/2)). `  (2.1)

For `r>2`,

` ||p_Q||_infinity <= [r/(r-2)](M_XM_Y/P)^(1/r). `               (2.2)

### Proof

Push the complex measures `e^(itF)dP_X`, `e^(itG)dP_Y` through `U^T` and `V^T`. Their densities `a_t,b_t` satisfy `||a_t||_2^2<=M_X`, `||b_t||_2^2<=M_Y`. Fubini gives

` phi_Q(t)=int hat(a_t)(2t Sigma v)b_t(v)dv. `

Cauchy–Schwarz and Plancherel yield

` int |hat(a_t)(2t Sigma v)|^2dv
 =(pi/|t|)^r P^(-1)||a_t||_2^2, `

which proves (2.1). Integrating its minimum with one proves (2.2). QED.

For `r=2`, (2.1) is the endpoint `|t|^-1` needed below. For a literal `r`-coordinate hub, its joint density cap is one. On the other side the baseline product-projection lemma gives the orthogonal `r`-projection cap `e^(r/2)`.

---

## 3. Marginal-free order-three density receiver

Let `M` be any literal original-coordinate cross block of the full quadratic form and put

` Z=E_3(M)=e_3(MM^T)>0. `

For physical row `i`, let `J_i` be the total squared three-volume of row triples containing `i`. Thus

` sum_i J_i=3Z. `

### Proposition 3

For arbitrary same-bank quadratic terms, arbitrary affine terms and arbitrary additional spectrum,

` ||p_Q||_infinity <= C_3 Z^(-1/6), `                            (3.1)

where

` C_3=3 sqrt(2) e (9/2)^(1/6)
     =14.818337662843... . `                                     (3.2)

Every branch in this proposition has an integrable characteristic-function envelope, so its density is `C_0`.

### Proof

If every `J_i/Z<=1/2`, Lemma 1 with `(k,ell,d)=(0,3,3)` gives exactly (3.1)–(3.2).

Otherwise choose a physical row `w` with `J_i>Z/2`. Put `S=||w||` and project every remaining physical crossing row orthogonally off `w`, producing `C`. Exterior Gram–Schmidt/Cauchy–Binet gives the exact identity

` S^2 e_2(CC^T)=J_i>Z/2. `                                       (3.3)

If all order-two row marginals of `C` are at most one half, promote this one physical coordinate to the hub and use Lemma 1 with `(k,ell,d)=(1,2,3)`. Its coefficient before (3.3) is

` 3 sqrt(2) e^(5/6) S^(-1/3)e_2(CC^T)^(-1/6). `

Using (3.3) gives the branch coefficient

` 3*2^(2/3)e^(5/6)=10.95771464927... < C_3. `                    (3.4)

If instead some residual row `c_j` is heavy, promote its physical preimage too. Let `P_2` be the two-row hub-to-`J` matrix. Project the remaining rows off `row(P_2)` and call their total one-volume `Z_1`. Gram–Schmidt gives

` det(P_2P_2^T) Z_1 > J_i/2 > Z/4. `                             (3.5)

If all one-volume marginals are at most one half, use Lemma 1 with `(k,ell,d)=(2,1,3)`. Equation (3.5) gives the coefficient

` 3 sqrt(2)e^(2/3)=8.26353569027... < C_3. `                      (3.6)

Finally, if one projected one-volume row is heavy, promote that physical row as well. The literal three-row hub matrix `P_3` then satisfies

` det(P_3P_3^T)>Z/8. `                                            (3.7)

Condition all other rows on that side and apply Lemma 2 with `r=3`. The three promoted original coordinates have joint density cap one, while the opposite orthogonal three-projection has density cap `e^(3/2)`. Since the singular-value product is `sqrt(det(P_3P_3^T))`, (2.2) and (3.7) give

` ||p_Q||_infinity <3 sqrt(2e) Z^(-1/6)<C_3Z^(-1/6). `           (3.8)

The cases are exhaustive. No coefficient outside the physical crossing is deleted; all same-bank terms are retained inside the arbitrary functions/polynomials allowed by Lemmas 1–2. QED.

---

## 4. Marginal-free order-two full half-potential receiver

Let `M` be a literal physical cross block with

` Z=E_2(M)=e_2(MM^T)>0. `

### Proposition 4

For the full ambient quadratic polynomial,

` sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8), `                         (4.1)

with

` C_2=8 sqrt(e) 2^(-1/8)
     =12.095072570796486... . `                                  (4.2)

### Proof

If every order-two row marginal is at most one half, Lemma 1 with `(k,ell,d)=(0,2,2)` gives

` |phi_Q(t)|
 <=min(1, pi e 2^(3/4) Z^(-1/4)|t|^-1). `                        (4.3)

The baseline Riesz inequality and the exact integral

` int_R |t|^-1/2 min(1,L/|t|)dt=8 sqrt(L) `

give (4.1)–(4.2).

If a physical row is heavy, promote it. With row norm `S` and residual projected one-volume `Z_1`, exact Gram–Schmidt gives

` S^2 Z_1>Z/2. `                                                  (4.4)

If the one-volume marginals are light, Lemma 1 with `(k,ell,d)=(1,1,2)` gives a `|t|^-1` envelope with coefficient at most

` pi sqrt(2)e^(3/4) Z^(-1/4), `

which is strictly below the coefficient in (4.3).

If a projected row is heavy, promote it too. The literal two-row hub matrix `P_2` satisfies

` det(P_2P_2^T)>Z/4. `                                            (4.5)

Lemma 2 with `r=2`, hub-side density cap one and opposite projection cap `e`, gives another `|t|^-1` envelope with coefficient `<pi sqrt(2e)Z^(-1/4)`, again below (4.3). Therefore the diffuse coefficient (4.3) dominates every branch, and the same Riesz integral proves (4.1). QED.

This is deliberately a half-potential theorem, not an `L^infinity` density theorem: the endpoint `|t|^-1` is not absolutely integrable.

---

## 5. Five-direction full half-potential lemma

### Proposition 5

If a symmetric quadratic part `S` has `s_5(S)>=1`, then for every affine part and independent cap-one coordinates,

` sup_a E|R-a|^(-1/2) <= 601. `                                  (5.1)

### Proof

If `S` has an `eta`-pivot, the baseline pivot proposition gives the truncated half-potential `H(R)<=600`, and the contribution from `|R-a|>1` is at most one.

If `S` has no pivot, baseline Proposition `prop:volume` with `k=2` gives

` V_2(S)>=kappa^2. `

The baseline random-cut identity gives a literal physical crossing with

` E_2(M)>=4^-2 kappa^2=kappa^2/16. `

Proposition 4 therefore gives

` sup_a E|R-a|^(-1/2)
 <=C_2(kappa^2/16)^(-1/8)
 =C_2 sqrt(160)
 =152.99191115498024... <153. `                                  (5.2)

Thus (5.1) holds in both cases. QED.

For later constants, the baseline pivot proof actually yields the sharper pivot-side truncation

` H(R)<=200+120 log16, `                                         (5.3)

because its scalar-pivot branch dominates the definite/indefinite pair branches. Hence in a pivoted remainder

` sup_a E|R-a|^-1/2 <=201+120log16. `                             (5.4)

---

## 6. Assembly: the nine-eigenvalue density theorem

Normalize first to `K=s=1`.

### 6.1 No physical pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, baseline Proposition `prop:volume` with `k=3` gives

` V_3(A)>=kappa^3. `

The baseline fair random cut produces a literal physical cross block `M` with

` E_3(M)>=4^-3 kappa^3. `

Hence

` E_3(M)^(-1/6)<=2 kappa^(-1/2)=160. `

Proposition 3 gives

` ||p_Q||_infinity <=160 C_3
 =2370.9340260548797... <2371. `                                  (6.1)

### 6.2 Scalar pivot

Suppose `|A_hh|>=eta`. The baseline Schur-count lemma leaves at least eight unit-scale eigenvalues in the scalar Schur complement, hence certainly at least five.

If that Schur complement has a pivot, use the sharper (5.4). If it has no pivot, use (5.2). Thus in every case the remainder `R` satisfies

` sup_a E|R-a|^-1/2 <=201+120log16. `                             (6.2)

The baseline scalar square profile now gives

` ||p_Q||_infinity
 <=eta^-1/2(201+120log16)
 =2010+1200log16
 =5337.106466687737... . `                                       (6.3)

### 6.3 Definite pair pivot

The baseline two-coordinate area argument gives

` ||p_Q||_infinity <=pi eta^-1/2=10pi<32. `                      (6.4)

### 6.4 Indefinite pair pivot

A two-coordinate Schur complement removes at most two spectral directions. Under `s_9(A)>=1`, at least seven unit-scale directions remain; in particular its operator norm is at least one. The baseline quarter-power/logarithmic remainder estimate and hyperbolic pair envelope apply verbatim, giving

` ||p_Q||_infinity<251. `                                        (6.5)

The four cases exhaust the normalized theorem, and (6.3) is the largest constant.

### 6.5 Scaling

For general `K,s`, put `Y=KX`. Its coordinate densities are bounded by one. Define

` Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c. `

Then `s_9(A/s)>=1` and

` Q=(s/K^2)Qtilde. `

Scalar density scaling gives

` ||p_Q||_infinity
 <=(2010+1200log16) K^2/s
 <5338 K^2/s. `                                                   (6.6)

This proves the stated multiplicity-nine candidate. QED.

---

## 7. Why this run stops at nine

The new order-two receiver is exactly a negative-half-potential endpoint: its characteristic-function tail is `|t|^-1`, which becomes integrable only after the Riesz weight `|t|^-1/2`. It does **not** by itself give a bounded output density. Thus it repairs the scalar-pivot remainder but not the no-pivot density branch.

The no-pivot order-three structural proposition still spends `4*3-3=9` directions. At the terminal interpolation ratio `r=2`, only eight large singular directions yield, after subtracting a rank-`<=6` global correction, two forced large diagonal entries. That exactly matches the restricted rank bound `rank R[L,L]<=2`; the baseline diagonal-dominance contradiction needs a third such entry. Therefore the existing interpolation proof cannot simply change `9` to `8`.

A threshold-eight theorem would require a genuinely new terminal `r=2` transversality/overlap argument, or an order-two endpoint receiver that can spend an additional same-bank spectral direction while retaining arbitrary rough product laws and all same-bank quadratic phases. No such complete full-scope argument is proved in this B17 run.

---

## 8. Independent checks performed in this run

- Recomputed the constants:
  - `C_3=14.818337662843...`, `160C_3=2370.93402605488...`;
  - `C_2=12.095072570796486...`, `sqrt(160)C_2=152.99191115498...`;
  - final scalar branch `2010+1200log16=5337.106466687737...`.
- Random finite-dimensional Gram tests verified to relative error below `2e-15` the promotion identities
  - `||w||^2 E_2(C)=J_i` for order three;
  - `||w||^2 E_1(C)=J_i` for order two.
- No computation is used as a substitute for the analytic proof.

## 9. Concurrency / validation status

After deriving the nine-direction compiler in this run, fresh `master` showed concurrent independent nine-direction artifacts at commits `30525aa82e000f8673dc62e0cd000ed6c9770da4` (fleet02/B14) and `3012277a558ac65251355e9887bc9beda5181b6e` (fleet01/B05). I read them only after my derivation. They independently reach the same threshold and essentially the same grouped-Fourier mechanism. Their existence is corroborating evidence, **not** a substitute for the owner-required two separate full reviews of the replacement proof, and I do not mark multiplicity nine validated/released here.
