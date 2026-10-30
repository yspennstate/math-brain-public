# Multiplicity nine with a rough-law-safe grouped Fourier compiler

Run: `20260924T141121Z-fleet02-B14-FIXMULT-auto11`  
Pinned baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K`. Let `A=A^T`, `b` and `c` be arbitrary. If

` s_9(A) >= s > 0,`

then `Q=X^TAX+b^TX+c` has an essentially bounded density and

`||p_Q||_infinity <= C_9 K^2/s`,

where

`C_9 = 2010 + 1200 log 16 = 5337.106466687737... < 5610`.

No support, moment, smoothness, iid, log-concavity, sign, diagonal-basis, exact-rank, leverage or post-rotation-independence hypothesis is added. This theorem does not imply the unrestricted three-eigenvalue conjecture.

The algebraic and scalar/two-coordinate ingredients are exactly the independently audited baseline lemmas. The new ingredient is a grouped physical-product Fourier compiler, proved below with an explicit Gaussian regularization so all rough-law and fiber-measurability steps are legal.

## 1. Grouped compiler with explicit regularization

Let `H,I,J` be disjoint sets of original coordinates. Let `W` be a `k`-dimensional orthogonal projection of `X_H`, with density `p_W` satisfying `||p_W||_infinity<=M_H`. Write `X'=(X_I,X_J)` and suppose

`Q = F(X_H) + 2 <W, M X' + beta> + R(X')`,

where `F` is arbitrary measurable and finite a.s., and `R` is an arbitrary quadratic/affine polynomial. Assume the literal `J` restriction `M_J` has row rank `k`. Let

`S = product of the k nonzero singular values of M_J`.

Write the physical `I-J` crossing part of `R` as `2 X_I^T A_IJ X_J`. For each physical row `a_i` of `A_IJ`, decompose

`a_i = c_i + lambda_i M_J`,

where `c_i` is orthogonal to `row(M_J)`. Let `C` be the matrix of rows `c_i`.

For an integer `ell>=1`, define

`Z_ell = sum_(|T|=ell) det(C_T C_T^T)`.

Assume `Z_ell>0`. Put

`w_T = det(C_T C_T^T)/Z_ell`,
`alpha_i = sum_(T contains i) w_T`,

and assume every positive `alpha_i<=1/2`. Let `d=k+ell`.

### Claim

For `t!=0`,

`|phi_Q(t)| <= min(1, K_(k,ell) |t|^(-d/2))`,

where

`K_(k,ell)
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

If `d>2`, Fourier inversion yields

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d))`.

### Proof — complex pushforwards

Push the complex measure `e^(itF)dP_H` forward by `W`. Its total variation is dominated by the actual law of `W`, so it has a density `a_t` satisfying

`|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`.

Push `e^(itR)dP_(X')` forward by `L=M X'`; call the resulting complex measure `mu_t`. Because `M_J` has full row rank, the law of `M_JX_J` has a density (apply the audited product-projection lemma after polar decomposition), and convolution with the independent shift `M_I X_I` preserves absolute continuity. Total-variation domination therefore gives `mu_t<<Lebesgue`; write its density again as `mu_t`.

Pairing the two pushforwards gives

`phi_Q(t)=int hat(a_t)(2t(l+beta)) mu_t(l) dl`.

By Cauchy–Schwarz, k-dimensional Plancherel and the substitution `u=2t(l+beta)`,

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                 (1)

No density cap for a conditional law has been inferred here; only an actual linear pushforward of original independent coordinates was used.

### Proof — the missing rough-law regularization step

Let `U=X_I`, `V=X_J`, let `D=V-V'` for an independent copy `V'`, and let `psi_i` be the characteristic function of the physical coordinate `U_i`. Each coordinate of `D` has an independent probability density bounded by one.

For `epsilon>0`, define

`G_epsilon(x)=(4 pi epsilon)^(-k/2) exp(-|x|^2/(4 epsilon))`.

Plancherel gives

`||mu_t||_2^2=(2pi)^(-k) int |hat(mu_t)(xi)|^2 dxi`.

Apply Cauchy–Schwarz in the probability law of `U` to `hat(mu_t)(xi)`, multiply by `exp(-epsilon|xi|^2)`, and integrate in `xi`. Expanding the square duplicates only `V`. The pure `U-U` terms cancel; the pure `V-V'` phase has modulus one; integrating in `U` gives the product of physical characteristic functions. Gaussian Fourier inversion gives, with no pointwise conditional density or fiber disintegration,

`(2pi)^(-k) int exp(-epsilon|xi|^2)|hat(mu_t)(xi)|^2 dxi
 <= E[ G_epsilon(M_JD) prod_i |psi_i(2t <a_i,D>)| ]`.          (2)

The left side increases to `||mu_t||_2^2` as `epsilon downarrow0` by monotone convergence. It is therefore enough to bound the right side uniformly in `epsilon`.

This identifies precisely the unspecified probability density `rho` in the earlier compressed proof: it is an approximate-identity kernel in the promoted variables, not a conditional density of a rough fiber.

### Proof — weighted Holder and projection density

For each positive-weight `ell`-set `T`, set

`F_T(D)=prod_(i in T) |psi_i(2t<a_i,D>)|^(1/alpha_i)`.

Because `sum_(T contains i) w_T/alpha_i=1`, generalized Holder with base measure

`G_epsilon(M_JD) dP_D`

gives the right side of (2) at most

`prod_T [ E( G_epsilon(M_JD) F_T(D) ) ]^(w_T)`.                (3)

For fixed `T`, consider the literal linear image

`D -> (u,y) = (M_JD, (<c_i,D>)_(i in T))`.

Since `row(C_T)` is orthogonal to `row(M_J)`, the Gram determinant of its `d=k+ell` rows is

`S^2 det(C_T C_T^T)`.

The audited product-projection lemma plus polar decomposition therefore gives a joint density bounded by

`e^(d/2) / [ S sqrt(det(C_T C_T^T)) ]`.                         (4)

Because `<a_i,D>=y_i+lambda_i u`, integrate first in `(u,y)`. The Gaussian has total mass one, while translation in `y_i` costs nothing. The audited scalar Fourier-power estimate with `p=1/alpha_i>=2` yields

`int_R |psi_i(2t(y+lambda_i u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.                                  (5)

Combining (4) and (5),

`E( G_epsilon(M_JD) F_T(D) )
 <= e^(d/2) [pi sqrt(2e)/|t|]^ell
    prod_(i in T) sqrt(alpha_i)
    / [ S sqrt(det(C_T C_T^T)) ]`.                             (6)

This bound is uniform in `epsilon` and uses only actual densities of finite-dimensional linear images of the original product difference law.

### Proof — entropy cancellation and constants

Since `det(C_T C_T^T)=w_T Z_ell`, the weighted geometric mean of determinant denominators contributes

`Z_ell^(-1/2) exp(H(w)/2)`.

The row factors contribute

`exp((1/2) sum_i alpha_i log alpha_i)`.

Order a random `ell`-set `T` uniformly after sampling it with law `w`. The ordered tuple has entropy `H(w)+log(ell!)`; each coordinate position has marginal `alpha_i/ell`. Entropy subadditivity gives

`H(w)+log(ell!) <= ell H(alpha/ell)
 = -sum_i alpha_i log alpha_i + ell log ell`.

Hence

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.       (7)

Insert (6),(7) into (3), then into (2), let `epsilon downarrow0`, and use (1). Taking square roots gives exactly the displayed `K_(k,ell)`.

For `d>2`,

`int_R min(1,K|t|^(-d/2)) dt = 2d/(d-2) K^(2/d)`;

the factor `1/(2pi)` in Fourier inversion cancels the `pi` contributed by `K^(2/d)`, giving the stated density constant. This completes the compiler with no hidden smoothness, support, moment, or conditional-version assumption.

## 2. Marginal-free `E_3` density receiver

For a literal original-coordinate cross block `M`, put

`Z=E_3(M)=e_3(MM^T)>0`.

Let `J_i` be the total Gram-determinant mass of row triples containing row `i`; `sum_i J_i=3Z`.

- If every `J_i/Z<=1/2`, use the compiler with `(k,ell,d)=(0,3,3)`:

  `||p_Q||_infinity <= C_3 Z^(-1/6)`,

  `C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.

- If some `J_i>Z/2`, promote that physical row `w`. Project the remaining physical crossing rows off `w`, obtaining `C`. Gram–Schmidt gives

  `J_i=||w||^2 e_2(CC^T)`.

  If the residual `E_2` row marginals are all at most one half, `(k,ell)=(1,2)` gives a coefficient `<10.958 Z^(-1/6)` after using `J_i>Z/2`.

- If a residual row is heavy, promote its physical preimage as a second row. If `P` is the two-row physical matrix and `C_2` the remaining rows projected off its span, then

  `det(PP^T)||C_2||_F^2 > Z/4`.

  If no residual one-volume row is heavy, `(k,ell)=(2,1)` gives `<8.264 Z^(-1/6)`.

- If a third residual row is heavy, the three promoted physical rows satisfy

  `det(P_3P_3^T)>Z/8`.

  The `ell=0,k=3` terminal (the same Plancherel argument with the residual Fourier factors discarded by `<=1`) gives

  `||p_Q||_infinity <=3 sqrt(e)[det(P_3P_3^T)]^(-1/6) <7 Z^(-1/6)`.

Thus in every branch

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.                       (8)

All promotions are physical original-coordinate rows; no post-rotation independence is used.

## 3. Marginal-free `E_2` full half-potential receiver

Put `Z=E_2(M)=e_2(MM^T)>0`.

If all row marginals are at most one half, the `(0,2)` compiler gives

`|phi_Q(t)| <= min(1, pi e 2^(3/4) Z^(-1/4)|t|^(-1))`.

The audited Riesz formula and

`int_R |t|^(-1/2) min(1,L/|t|) dt = 8 sqrt(L)`

give

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.                    (9)

If a row is heavy, promote it. If the projected one-volume marginals are all at most one half, `(1,1)` gives `<9.79 Z^(-1/8)` after the heavy-row factor. If one projected row is heavy, promote it too; the resulting physical two-row Gram determinant is `>Z/4`, and the exact-rank `k=2` Riesz terminal gives `<8.64 Z^(-1/8)`. Hence (9) is valid without a leverage/marginal assumption.

This is intentionally a half-potential result, not a bounded-density theorem: the `|t|^-1` endpoint is not integrable.

## 4. Complete multiplicity-nine proof

Normalize to `K=s=1`, and retain the baseline

`eta=1/100`, `kappa=1/80^2`.

### No pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited spectral-to-volume proposition at `k=3` gives

`V_3(A)>=kappa^3`.

The audited fair cut produces a literal cross block `M` with

`E_3(M)>=4^-3 kappa^3`,

so `E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`. By (8),

`||p_Q||_infinity <=160 C_3 = 2370.93402605488... <2400`.       (10)

### Scalar pivot

Suppose `|A_hh|>=eta`. The audited Schur-count lemma leaves at least eight unit-scale eigenvalues in the scalar Schur complement `S`.

If `S` has an `eta`-pivot, the audited pivot-half-potential proof actually gives truncated half-potential at most

`H_* = 200+120 log16`;

the other pivot subbranches are smaller. Adding the tail `|R-a|>1`, where the kernel is at most one, gives full half-potential at most

`201+120 log16`.

If `S` has no pivot, then certainly `s_5(S)>=1`. The audited spectral-to-volume proposition at `k=2`, followed by the fair cut and (9), gives full half-potential

`<= C_2 (4^-2 kappa^2)^(-1/8)
 = C_2 sqrt(160)
 = 152.99191115498...`.

Therefore the first subcase is the worse one. The audited square profile gives

`||p_Q||_infinity
 <= eta^(-1/2)(201+120 log16)
 = 2010+1200 log16
 = 5337.106466687737...`.                                      (11)

### Definite pair pivot

The audited definite-pair lemma gives

`||p_Q||_infinity <= pi/sqrt(eta)=10pi<32`.                    (12)

### Indefinite pair pivot

The two-coordinate Schur complement retains at least seven unit-scale eigenvalues, hence operator norm at least one. The audited hyperbolic envelope plus quarter-power logarithmic potential gives exactly the baseline estimate

`||p_Q||_infinity<251`.                                        (13)

The four cases exhaust the normalized problem. The maximum of (10)–(13) is (11), proving the normalized theorem with `C_9=2010+1200 log16`.

For general `K,s`, set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q`.

The coordinates of `Y` have cap one and `s_9(A/s)>=1`; scalar density rescaling proves

`||p_Q||_infinity <= C_9 K^2/s`.

## 5. Closed dependency map

The proof uses only the following audited dependencies:

`bounded-Borel representatives`
` -> Fourier identities / Riesz / scalar Fourier powers`
` -> geometric BL / product projection`
` -> grouped Gaussian-regularized compiler`
` -> {E3 density receiver, E2 half-potential receiver}`

and independently

`sampling + completion + nonsymmetric rank perturbation + diagonal dominance`
` -> spectral-to-volume proposition`
` -> random coordinate cut`.

The four final branches are then

- `no pivot + s9 -> V3 -> E3 -> bounded density`;
- `scalar pivot + Schur -> {pivot half-potential OR no-pivot s5 -> V2 -> E2 half-potential} -> square profile`;
- `definite pair -> direct two-dimensional density cap`;
- `indefinite pair -> Schur operator norm + hyperbolic/log potential`.

Every conditioning step is on original coordinates, every promoted row is a physical original-coordinate row, and all limit/interchange steps are Gaussian-regularized or nonnegative Tonelli arguments. No hidden support or smoothness assumption enters.

## 6. Why this proof stops at nine

This theorem does not establish multiplicity eight. The existing barriers are structural:

- `s_8>=1` does not force an `eta`-pivot (four diffuse rank-one bipartite blocks give an exact no-pivot example with eight unit-modulus eigenvalues);
- the audited interpolation rank count is one diagonal direction short at the terminal `r=2` chamber for multiplicity eight;
- an order-two crossing gives a genuine Fourier `1/|t|` endpoint and can have logarithmically unbounded density (`U^2-V^2` for cap-one uniforms).

These do not disprove an eight-eigenvalue theorem; they show that another mechanism is required.
