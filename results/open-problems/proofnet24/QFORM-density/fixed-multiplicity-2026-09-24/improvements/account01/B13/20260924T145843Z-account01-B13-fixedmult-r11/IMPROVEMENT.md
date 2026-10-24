# account01/B13 replacement theorem: multiplicity nine

Run: `20260924T145843Z-account01-B13-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Audited baseline source: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

**Status:** complete B13 reconstruction of a full-scope candidate lowering `17 -> 9`. It preserves arbitrary independent rough laws, all signatures, arbitrary remaining spectrum, arbitrary affine terms and arbitrary dimension. It does **not** prove multiplicity eight or the unrestricted three-eigenvalue conjecture. It is not self-certified as independently validated.

After deriving/checking the argument, I source-checked the concurrent account01/B17 replacement proof (`IMPROVEMENT.md`, blob `1ca905f5fdd67ce22ec7717488b865a387ad7e48`), which reaches the same threshold through the same grouped physical Fourier mechanism. The reconstruction below is complete enough to stand on the audited baseline plus the displayed new lemmas.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T`, `b` and `c` be arbitrary. If

` s_9(A) >= s > 0, `

then

` Q=X^TAX+b^TX+c `

has an essentially bounded density satisfying

` ||p_Q||_infinity <= 6010 K^2/s. `

No support, moment, smoothness, iid, sign, exact-rank, leverage, diagonal-coordinate, Gaussian or log-concavity assumption is added.

The proof uses the audited baseline constants

`eta=1/100`, `kappa=1/80^2`.

The only genuinely new analytic ingredients are an order-three crossing-volume density receiver and an order-two crossing-volume full negative-half-potential receiver. Both are established through a grouped product-Fourier compiler that promotes heavy determinant marginals only through literal original coordinates.

---

## 1. Grouped physical product-Fourier compiler

Let `H,I,J` be disjoint banks of original independent coordinates. Let

`W=U^T X_H in R^k`, `U^TU=I_k`,

and suppose the density of `W` is bounded by `M_H`. Consider

`Q=F(X_H)+2 <W, M X' + beta> + R(X')`, `X'=(X_I,X_J)`,

where `F` is arbitrary measurable and finite a.s., and `R` is an arbitrary quadratic-affine polynomial in the light original coordinates. Assume the literal `J` restriction `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`.

For each physical row `a_i` of the `I-J` crossing matrix occurring in `R`, decompose orthogonally in coefficient space

`a_i=c_i+lambda_i M_J`, `c_i perpendicular row(M_J)`.

Let `C` have rows `c_i`. For an integer `ell>=1`, define

`Z_ell = sum_{|T|=ell} det(C_T C_T^T)`,

and, when `Z_ell>0`, weights

`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=sum_{T contains i} w_T`.

Assume every positive `alpha_i<=1/2`, and put `d=k+ell`.

### Lemma 1 (compiler)

For every `t!=0`,

`|phi_Q(t)| <= min(1, K_(k,ell) |t|^(-d/2))`,

where

`K_(k,ell)
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`

If `d>2`, then

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

### Proof

Push the complex measure `e^(itF)dP_H` through `W`. Its total variation is dominated by the law of `W`, so it has a complex density `a_t` with

`|a_t|<=p_W`, `||a_t||_2^2<=M_H`.

Push `e^(itR)dP_X'` through the `k`-vector `L=M X'`; call the complex density `mu_t`. Because the literal map `M_J X_J` has full row rank, polar decomposition plus the audited product-projection lemma gives an absolutely continuous bounded law for `M_JX_J`, hence for `L` after adding the independent/conditional translation from the other coordinates. Total-variation domination then gives `mu_t` and `mu_t in L^2`.

Pair the two pushforwards. Cauchy--Schwarz and `k`-dimensional Plancherel give

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.               (1.1)

To control `mu_t`, let `D=X_J-X'_J`, where `X'_J` is an independent copy. Its coordinates are independent and each difference density is at most one. For `epsilon>0`, let

`G_epsilon(x)=(4 pi epsilon)^(-k/2) exp(-|x|^2/(4epsilon)).`

Insert the Gaussian multiplier in the Plancherel formula for `mu_t`. Apply Cauchy--Schwarz in the original `X_I` law, expand the square by duplicating only the literal `J` bank, and integrate the Fourier variable. Pure `I` phases disappear in the Cauchy--Schwarz step; pure `J,J'` phases have modulus one; averaging the independent `X_i`, `i in I`, produces their physical characteristic functions `psi_i`. Consequently

`(2pi)^(-k) int e^(-epsilon|xi|^2)|hat(mu_t)(xi)|^2 dxi
 <= E[ G_epsilon(M_JD) prod_i |psi_i(2t<a_i,D>)| ].`          (1.2)

The left side increases to `||mu_t||_2^2` as `epsilon downarrow0`.

Weighted Holder with the determinant-subset law `w_T` gives

`RHS(1.2) <= prod_T I_T^(w_T)`,                                (1.3)

where

`I_T=E[G_epsilon(M_JD) prod_{i in T}|psi_i(2t<a_i,D>)|^(1/alpha_i)].`

For positive-weight `T`, the literal linear map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has row-Gram determinant

`S^2 det(C_T C_T^T)`,

because the residual rows `c_i` are orthogonal to `row(M_J)`. The audited product-projection lemma therefore bounds the density of this `d`-dimensional image by

`e^(d/2)/[S sqrt(det(C_T C_T^T))]`.                             (1.4)

Integrate first in this image. `G_epsilon` has mass one, translations by `lambda_i M_JD` do not affect the one-dimensional integral, and `1/alpha_i>=2`; the audited scalar Fourier-power lemma gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|.`                                  (1.5)

Thus

`I_T <= e^(d/2)[pi sqrt(2e)/|t|]^ell
        prod_{i in T} sqrt(alpha_i)
        /[S sqrt(det(C_T C_T^T))].`                            (1.6)

Since `det(C_T C_T^T)=w_T Z_ell`, the determinant geometric mean contributes

`Z_ell^(-1/2) exp(H(w)/2)`,

while the row factors contribute

`exp((1/2)sum_i alpha_i log alpha_i)`.

Order a random `ell`-subset with law `w` uniformly. Entropy subadditivity gives

`H(w)+log(ell!) <= -sum_i alpha_i log alpha_i + ell log ell`,

hence

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`      (1.7)

Insert (1.6)--(1.7) into (1.3), then (1.2), let `epsilon downarrow0`, and use (1.1). Taking square roots gives the displayed characteristic-function constant. If `d>2`, direct integration gives

`int_R min(1,K|t|^(-d/2))dt = [2d/(d-2)] K^(2/d)`,

and Fourier inversion gives the density estimate. Every stochastic conditioning/duplication was on original-coordinate product banks; coefficient-space orthogonal projections were deterministic only. QED.

---

## 2. Exact-rank physical terminal

### Lemma 2

Let `X,Y` be independent random vectors. Let `B=U Sigma V^T` have exact rank `r`, nonzero singular-value product `P`. Suppose `U^TX` and `V^TY` have density caps `M_X,M_Y`. For arbitrary measurable real `F,G`,

`Q=F(X)+2X^TBY+G(Y)`

satisfies

`|phi_Q(t)| <= min(1,(pi/|t|)^(r/2)(M_XM_Y)^(1/2)P^(-1/2)).`   (2.1)

If `r>2`,

`||p_Q||_infinity <= [r/(r-2)](M_XM_Y/P)^(1/r).`                (2.2)

### Proof

Push `e^(itF)dP_X` and `e^(itG)dP_Y` through the two orthogonal projections. Their complex densities have `L^2` norms squared at most the corresponding density caps. Fubini writes `phi_Q` as the pairing of one density with the Fourier transform of the other at `2t Sigma v`. Cauchy--Schwarz, Plancherel, and the change of variables through `Sigma` give (2.1); integrating the envelope gives (2.2). No independence of rotated coordinates is asserted: only density caps of deterministic projections are used. QED.

---

## 3. Order-three crossing volume gives a density

Let `B` be a literal original-coordinate crossing matrix and

`Z=E_3(B):=e_3(BB^T)>0`.

For each physical row `i`, let `J_i` be the total squared three-volume of row triples containing `i`. Then `sum_i J_i=3Z`.

### Proposition 3

For the full ambient quadratic polynomial, retaining all same-bank quadratic and affine terms,

`||p_Q||_infinity <= C_3 Z^(-1/6)`,

with

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`.             (3.1)

### Proof

If every normalized row marginal `J_i/Z<=1/2`, apply Lemma 1 with `(k,ell,d)=(0,3,3)`; this is exactly (3.1).

Otherwise select a heavy physical row `w`, with `J_i>Z/2`, and project every remaining crossing row orthogonally off `w`, obtaining residual matrix `C`. Exterior Gram--Schmidt/Cauchy--Binet gives the exact identity

`||w||^2 e_2(CC^T)=J_i>Z/2`.                                   (3.2)

If all order-two residual marginals are `<=1/2`, promote this one literal coordinate to the hub and use Lemma 1 with `(k,ell,d)=(1,2,3)`. Equation (3.2) yields a coefficient strictly below `C_3`.

If some residual row is heavy, promote its literal physical preimage as well. Let `P_2` be the resulting two-row hub-to-opposite-bank matrix and let `Z_1` be the one-volume remaining after projecting all other rows off `row(P_2)`. Another exact base-times-height identity gives

`det(P_2P_2^T) Z_1 > Z/4`.                                     (3.3)

If the one-volume marginals are all `<=1/2`, Lemma 1 with `(k,ell,d)=(2,1,3)` again gives a coefficient below `C_3`.

Finally, if one one-volume row is heavy, promote it. The resulting literal three-row crossing matrix `P_3` obeys

`det(P_3P_3^T)>Z/8`.                                            (3.4)

Condition all other original coordinates on the promoted side. Lemma 2 with `r=3` applies: the three literal hub variables have joint density cap one, and the opposite orthogonal three-projection has cap `e^(3/2)` by the audited product-projection lemma. Since the singular-value product is `sqrt(det(P_3P_3^T))`,

`||p_Q||_infinity < 3 sqrt(2e) Z^(-1/6) < C_3 Z^(-1/6)`.

The cases exhaust all determinant marginals. QED.

---

## 4. Order-two crossing volume gives the full half potential

Let `Z=E_2(B)=e_2(BB^T)>0` for a literal crossing matrix.

### Proposition 4

For the full ambient quadratic polynomial,

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

where

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.                    (4.1)

### Proof

If every order-two row marginal is at most one half, Lemma 1 with `(k,ell,d)=(0,2,2)` yields

`|phi_Q(t)| <= min(1, pi e 2^(3/4) Z^(-1/4)|t|^-1)`.            (4.2)

The audited Riesz inequality and

`int_R |t|^-1/2 min(1,L/|t|)dt=8 sqrt(L)`

give (4.1).

If a physical row is heavy, promote it. Exact Gram--Schmidt gives

`||w||^2 Z_1>Z/2`                                               (4.3)

for the projected one-volume. If its row marginals are light, Lemma 1 with `(k,ell,d)=(1,1,2)` gives a smaller `|t|^-1` coefficient than (4.2). If a projected row is heavy, promote it as well; the literal two-row matrix satisfies

`det(P_2P_2^T)>Z/4`,                                            (4.4)

and Lemma 2 with `r=2`, hub cap one and opposite projection cap `e`, again gives a smaller endpoint coefficient. Therefore (4.2) dominates every branch and (4.1) follows. QED.

The endpoint is deliberately a full negative-half-potential estimate, not a bounded-density theorem: `|t|^-1` is not integrable without the Riesz weight.

---

## 5. Five spectral directions suffice for the full half potential

### Proposition 5

If a symmetric quadratic part `S` satisfies `s_5(S)>=1`, then for every affine part and independent cap-one coordinates,

`sup_a E|R-a|^(-1/2) <=601`.                                   (5.1)

### Proof

If `S` has an `eta`-pivot, the audited baseline pivot proposition gives truncated half potential `<=600`; outside `|R-a|<=1`, the kernel is at most one.

If `S` has no pivot, the audited spectral-to-volume proposition with `k=2` gives

`V_2(S)>=kappa^2`.

A fair literal coordinate cut gives a crossing with

`E_2>=4^-2 kappa^2=kappa^2/16`.

Proposition 4 then yields

`sup_a E|R-a|^-1/2 <= C_2 (kappa^2/16)^(-1/8)
 = C_2 sqrt(160)=152.991911...<153<601`.

QED.

---

## 6. Assembly of the multiplicity-nine theorem

Normalize `K=s=1`.

### No pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited baseline spectral-to-volume proposition with `k=3` gives

`V_3(A)>=kappa^3`.

A fair literal cut gives

`E_3(B)>=4^-3 kappa^3`,

so `E_3(B)^(-1/6)<=2 kappa^(-1/2)=160`. Proposition 3 gives

`||p_Q||_infinity <=160 C_3=2370.934026...<2371`.               (6.1)

### Scalar pivot

If `|A_hh|>=eta`, the scalar Schur complement retains at least eight unit-scale spectral directions, hence at least five. Proposition 5 gives its full negative-half potential `<=601`. The audited scalar square profile therefore yields

`||p_Q||_infinity <= eta^-1/2 * 601 = 6010`.                    (6.2)

### Definite pair pivot

The audited two-dimensional Jacobian estimate gives

`||p_Q||_infinity <= pi eta^-1/2=10pi<32`.                      (6.3)

### Indefinite pair pivot

A two-coordinate Schur complement loses at most two unit-scale directions. Under `s_9(A)>=1`, at least seven remain, so in particular its operator norm is at least one. The audited hyperbolic envelope plus the quarter-power logarithmic-potential bound applies verbatim and gives

`||p_Q||_infinity<251`.                                         (6.4)

The four cases exhaust the normalized theorem; the largest constant is `6010`.

For general `K,s`, put `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then `s_9(A/s)>=1` and `Q=(s/K^2)Qtilde`. Density scaling proves

`||p_Q||_infinity <=6010 K^2/s`.

This proves the stated multiplicity-nine replacement candidate. QED.

---

## 7. Second end-to-end review of the nine-direction replacement

I independently re-ran the proof backwards from its final branches.

- The no-pivot branch spends exactly order-three crossing volume. The new receiver needs three total grouped physical Fourier dimensions and is integrable because its tail is `|t|^-3/2`.
- The scalar-pivot branch loses one spectral direction but needs only the new order-two full half-potential theorem; baseline order-two structural volume requires five directions, so eight surviving directions are more than sufficient.
- Definite and indefinite pair branches require no new threshold input beyond the audited baseline Jacobian/logarithmic arguments.
- Every promotion in Propositions 3–4 selects literal original coordinates. Orthogonal projections occur only in deterministic coefficient space or in density-cap statements for projections; no rotated independence is used.
- Same-bank quadratic terms, the remaining spectrum and arbitrary affine terms stay inside the arbitrary phase functions in Lemmas 1–2; none is discarded.

Result: **PASS** for this same-worker second reconstruction. This is not a second independent worker review and does not satisfy the owner's independent-release gate by itself.

---

## 8. Why I do not lower nine to eight in this run

The audited baseline structural proof at order three uses `4r+1` spectral directions at the terminal interpolation ratio `r=2`. With only eight directions, subtracting the global rank-`<=6` correction forces only two large diagonal entries on the seed complement; this matches, rather than exceeds, the restricted rank bound `<=2`, so the diagonal-dominance contradiction no longer closes.

I also checked the newest exact obstruction recorded by account02/B17 (`S8_ROBUST_PAIR_SHORTCUT_FALSE.md`, blob `d47bf7ac7912a5c6f0a1a3d2d5eaf93221035377`). It constructs a no-pivot rank-two matrix with a dimension-free robust two-anchor cross map and arbitrarily small indefinite anchor determinant for which iid unit-uniform inputs still give a logarithmically unbounded output density. This is **not** a counterexample to an `s_8` theorem (the matrix has only two nonzero spectral directions), but it rigorously rules out the tempting `s_8` shortcut that throws away the remaining Schur spectrum after extracting the robust pair.

A separate account03/B17 reduction source-pinned in the repository shows that the unpaid `s_8` collar can be reduced to a robust two-anchor / near-singular self-block chamber, but the nonlogarithmic determinant singularity remains. I do not have a complete receiver for that chamber that retains the ambient Schur spectral currency. Therefore:

- multiplicity **9**: complete replacement candidate in this report;
- multiplicity **8**: **OPEN** in this run;
- unrestricted multiplicity **3**: **OPEN**.

No weaker-law or special-sign theorem is being substituted for the full scope.
