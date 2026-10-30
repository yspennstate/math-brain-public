# fleet02/B01 improvement — independently reconstructed nine-direction theorem, 4880 constant

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `fleet02-B01-20260924T1500Z-auto11`  
Pinned baseline manuscript: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Result

After the independent baseline audit in the sibling audit artifact, I reconstructed a complete replacement proof lowering the fixed multiplicity from seventeen to **nine** while preserving all original quantifiers.

### Theorem `QFORM-FIXED-MULTIPLICITY-9-B01-AUTO11-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=K`, `0<K<infinity`. Let `A=A^T` be any real symmetric matrix, and let `b,c` be arbitrary. If

` s_9(A)>=s>0,`

then `Q=X^TAX+b^TX+c` has a Lebesgue density and

`boxed: ||p_Q||_infinity <= 4880 K^2/s.`

No global continuity claim is made. No Gaussian/log-concavity, moment, support, sign, diagonal-basis, exact-rank, leverage or post-rotation-independence hypothesis is added.

This proof is independent of the baseline 17-direction main theorem. It imports only baseline lemmas individually audited in this run, then replaces the order-five no-pivot density receiver by a marginal-free order-three receiver and replaces the scalar-pivot nine-direction Schur remainder by an order-two full half-potential receiver.

## 1. Normalization

It suffices to prove `K=s=1`. Set `Y=KX`; then every coordinate density of `Y` is at most one. Define

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q`.

The normalized theorem for `Qtilde` therefore scales back with the exact factor `K^2/s`.

Keep the baseline constants

`eta=1/100`, `kappa=1/80^2=1/6400`.

## 2. Grouped product-Fourier compiler

Let `H,I,J` be disjoint original-coordinate banks. Let `W` be a `k`-dimensional linear image of `X_H` with density bounded by `M_H`. Write `X'=(X_I,X_J)` and

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,

with arbitrary measurable `F`, arbitrary real quadratic polynomial `R`, and `M_J` of row rank `k`. Let `S` be the product of the nonzero singular values of `M_J` (`S=1` for `k=0`). If `a_i` is row `i` of the `I-J` cross block of `R`, decompose

`a_i=c_i+lambda_i M_J`,

with `c_i` orthogonal to the row space of `M_J`. Let `C` have rows `c_i`. For `ell>=1`, put

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,
`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=sum_{T containing i}w_T`.

Assume `alpha_i<=1/2` for all nonzero marginals and put `d=k+ell`.

### Lemma 2.1

For `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`

If `d>2`, Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d)).`                                    (2.1)

### Proof

Push the complex measure `exp(itF)dP_H` by `W`. Its complex density `a_t` satisfies `|a_t|<=p_W`, so `||a_t||_2^2<=M_H`. Push `exp(itR)dP_X'` by the `k`-dimensional map `MX'`, obtaining a complex measure `mu_t`. Because `M_J` has row rank `k`, conditioning on `X_I` shows that this measure is absolutely continuous after an arbitrarily small convolution regularization. Cauchy–Schwarz and `k`-dimensional Plancherel at scale `2t` give

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2.`                  (2.2)

To bound `mu_t` without any conditional density cap, condition on one value of `X_I`, mollify the conditional pushforward from the `J` bank by a nonnegative approximate identity, and expand its squared `L^2` norm with one independent copy `X'_J`. Put `D=X_J-X'_J`. The pure `I` phase cancels, the pure `J` phase has modulus one, and the `I-J` cross phase is linear in each original `X_i`. Averaging the original independent `I` coordinates therefore produces

`int rho_delta(M_JD) prod_i |psi_i(2t<a_i,D>)| dP_D`,           (2.3)

where `rho_delta` is a probability kernel and each `psi_i` is the characteristic function of a cap-one original coordinate. The coordinates of `D` are independent and cap one.

Weighted Hölder with weights `w_T` is exact because

`sum_{T containing i}w_T/alpha_i=1`.

For a fixed `T`, the map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has row Gram determinant `S^2 det(C_T C_T^T)`: the `c_i` are orthogonal to `row(M_J)`. The audited product-projection lemma plus deterministic scaling bounds its density by

`e^(d/2)/[S sqrt(det(C_T C_T^T))].`                              (2.4)

Conditional on the first `k` coordinates of that image, `a_i=c_i+lambda_i M_J` changes only the frequency shift. Since `alpha_i<=1/2`, the audited scalar Fourier-power lemma at `p=1/alpha_i` and the scale `2t` gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|.`                                   (2.5)

Thus the `T` term is at most

`e^(d/2)[pi sqrt(2e)/|t|]^ell
 prod_{i in T}sqrt(alpha_i)/[S sqrt(det(C_T C_T^T))].`           (2.6)

Taking the weighted geometric mean, the determinant factors contribute

`Z_ell^(-1/2) exp(H(w)/2)`,

while the marginals contribute

`exp[(1/2)sum_i alpha_i log alpha_i]`.

Draw `T~w` and uniformly order its `ell` elements. Entropy subadditivity gives

`H(w)+log(ell!) <= ell log ell-sum_i alpha_i log alpha_i`,       (2.7)

hence

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`

Combining (2.2)–(2.7), then taking a square root, yields the displayed `K_{k,ell}`. The mollified `L^2` bounds are uniform; weak `L^2` compactness/lower semicontinuity identifies the unmollified pushforward and preserves the bound. Finally

`int min(1,K|t|^(-d/2))dt = [2d/(d-2)]K^(2/d)`

for `d>2`; the audited `1/(2*pi)` inversion normalization gives (2.1). No copy of `I`, conditional recap of a rotated variable, or scalar rough quadratic-phase decay is used.

### Exact-rank terminal form

The same pushforward/Plancherel argument with `r` literal physical hub rows crossing an independent product bank through a full-row-rank block `P` gives

`|phi(t)|<=min(1,pi^(r/2)e^(r/4)det(PP^T)^(-1/4)|t|^(-r/2)).`   (2.8)

Therefore

`r=3: ||p||_infinity <=3 sqrt(e)det(PP^T)^(-1/6),`              (2.9)

and the audited Riesz formula gives

`r=2: sup_a E|Q-a|^(-1/2)
 <=4 sqrt(2)e^(1/4)det(PP^T)^(-1/8).`                            (2.10)

## 3. Marginal-free order-three crossing volume

For a literal original-coordinate cross block `M`, put

`Z=E_3(M)=e_3(MM^T)>0`.

For row `i`, let `J_i` be the sum of all three-row Gram determinants containing `i`; then `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, Lemma 2.1 at `(k,ell,d)=(0,3,3)` gives

`||p_Q||_infinity<=C_3 Z^(-1/6),`

with

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843... .`                (3.1)

If some row `w` has `J_i>Z/2`, project the remaining rows orthogonally off `w`, obtaining `C`. Gram–Schmidt gives exactly

`J_i=||w||^2 e_2(CC^T).`                                        (3.2)

If the residual order-two marginals are light, apply Lemma 2.1 at `(1,2,3)`; after `J_i>Z/2`, its coefficient is `<10.958 Z^(-1/6)`.

Otherwise promote a residual heavy row. If `P` is the two-row hub and `C_2` the remaining rows projected off `row(P)`, then

`H_ij=det(PP^T)||C_2||_F^2>J_i/2>Z/4.`                          (3.3)

A light residual one-volume is paid by `(2,1,3)` with coefficient `<8.264 Z^(-1/6)`. A final heavy residual row gives a literal three-row block `P_3` with

`det(P_3P_3^T)>H_ij/2>Z/8`,

and (2.9) costs `<7 Z^(-1/6)`. Thus in all cases

`boxed: ||p_Q||_infinity<=C_3 E_3(M)^(-1/6).`                   (3.4)

Each branch has an integrable characteristic-function majorant; continuity is available locally but is not needed for the global theorem.

## 4. Marginal-free order-two crossing volume

For a literal cross block put `Z=E_2(M)>0`. If all order-two row marginals are at most `1/2`, Lemma 2.1 at `(0,2,2)` gives

`|phi(t)|<=min(1,pi e 2^(3/4)Z^(-1/4)/|t|).`

Using

`int |t|^(-1/2)min(1,L/|t|)dt=8 sqrt(L)`

in the audited Riesz formula gives

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796... .`                    (4.1)

If one row is heavy, projection off that row gives the exact currency

`K_i=||w||^2||C||_F^2>Z/2`.

A light residual order-one bank is paid by `(1,1,2)` with coefficient `<9.79 Z^(-1/8)`; a second heavy row gives a two-row Gram determinant `>Z/4`, and (2.10) costs `<8.64 Z^(-1/8)`. Therefore

`boxed: sup_a E|Q-a|^(-1/2)<=C_2 E_2(M)^(-1/8).`                 (4.2)

This is deliberately a half-potential theorem, not a density theorem. For independent cap-one uniforms, `2XY` has a logarithmically divergent density at zero, so a generic order-two bounded-density upgrade is false.

## 5. Sharper audited pivot half-potential constant

The baseline quarter-concentration proof establishes the coefficient before its last rounding as

`2^(5/8) pi^(-1/4)e^(3/8)Gamma(3/8)<40/3`.

Hence, whenever the quadratic coefficient has operator norm at least one,

`sup_a E log_+(1/|R-a|)<=L_*:=4+4log(40/3)
 =14.3610686617833... .`                                        (5.1)

The baseline singular-kernel proof also gives, before rounding,

`J(d)<=8+2 sqrt(2)log_+(1/|d|).`                                (5.2)

At a scalar `eta`-pivot, (5.1)–(5.2) yield the truncated half-potential

`eta^(-1/2)[8+2 sqrt(2)L_*]
 =486.192361433304...<487.`                                      (5.3)

The definite-pair branch is `<126` and the indefinite-pair branch is `<433`. Thus every pivoted quadratic form with at least two unit spectral directions has truncated half-potential `<487`, and full half-potential `<488` after adding the tail `|Q-a|>1`.

## 6. Nine spectral directions: complete replacement proof

Assume `K=s=1` and `s_9(A)>=1`.

**No pivot.** The audited spectral-to-volume proposition at `k=3` gives `V_3>=kappa^3`. A fair original-coordinate cut gives `E_3(M)>=4^(-3)kappa^3`, so `E_3(M)^(-1/6)<=160`. By (3.4),

`||p_Q||_infinity<=160 C_3
 =2370.93402605488...<2400.`                                     (6.1)

**Scalar pivot.** Complete one literal original coordinate. The audited Schur count leaves at least eight unit spectral directions in the exact remainder `S`. If `S` has a pivot, Section 5 applies because it has at least two large directions, giving full half-potential `<488`. If `S` has no pivot, then `s_5(S)>=1`; the audited structural proposition at `k=2` plus a fair cut gives

`E_2(M_S)>=4^(-2)kappa^2`.

Equation (4.2) gives

`sup_a E|R-a|^(-1/2)
 <=C_2 sqrt(160)
 =152.99191115498...<153<488.`                                   (6.2)

The audited conditional square profile therefore yields

`||p_Q||_infinity<eta^(-1/2)*488=4880.`                          (6.3)

**Definite pair pivot.** The audited pair lemma gives `10*pi<32`.

**Indefinite pair pivot.** The Schur complement retains at least seven unit spectral directions, hence operator norm at least one; the audited hyperbolic/logarithmic argument is already `<251`.

The alternatives exhaust the normalized theorem, so the bound is `4880`. Section 1 scales it to

`boxed: ||p_Q||_infinity <=4880 K^2/s.`                          (6.4)

## 7. Closed dependency map

Imported from the independently audited baseline only:

1. Fourier inversion and Riesz half-potential (`lem:fourier`, `lem:riesz`).
2. Geometric BL, product projection and scalar Fourier powers (`thm:bl`, `lem:projection`, `lem:scalar-fourier`).
3. Schur count, scalar square profile, definite/hyperbolic pair and quarter/log bounds (`lem:schur`, `lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`).
4. Nonsymmetric sampling/completion, spectral-to-volume and fair cut (`lem:sampling`, `lem:completion`, `prop:volume`, `lem:cut`).

New Lemma 2.1 is derived from items 1–2. Sections 3–4 are finite physical-row promotion trees. Section 5 only sharpens constants already proved in the baseline. Section 6 combines them with items 3–4. There is no dependency on the 17-direction main theorem, no rotated product law, and no conditional marginal-cap shortcut.

## 8. Why this run stops at nine, not eight

I also attacked the `s_8` no-pivot boundary. The current source-backed structural work shows that `s_8`, no pivot, and small `V_3` still forces a positive dimension-free **overlap-one** volume based on packets

`det A_{S union {h}, T union {h}}`, `|S|=|T|=2`,

and a five-role entropy inequality removes packet-cardinality loss. Independently checking that arithmetic confirms this is genuine currency, but the row and column packets share the physical coordinate `h`. It therefore does not fit Lemma 2.1, whose banks are disjoint original coordinates. The best dependence-safe endpoint currently available remains critical `1/|t|` decay / all finite `L^r`, not an integrable characteristic function or `L^infinity` density.

The remaining obligation is therefore

**GAP `QFORM-S8-SHARED-ANCHOR-ANALYTIC-LOG-REMOVAL`:** consume the shared physical anchor in the overlap-one packet, including heavy-marginal promotion cases, and gain any integrable improvement over the critical `1/|t|` endpoint without duplicating the shared coordinate or asserting independence of its copy-sum/copy-difference variables.

A useful adversarial warning is that order two alone cannot pay this gap: `2XY` for independent cap-one uniforms has an unbounded logarithmic density at zero. Likewise a purely algebraic attempt to lower the structural count by replacing the manuscript's global `3r` rank with `2r` is false in generic exact interpolation examples. Thus I do **not** claim multiplicity eight, and I do not claim the unrestricted three-eigenvalue conjecture.

## Status

This run supplies one complete independent audit of the pinned 17-direction baseline and one complete independent reconstruction of the nine-direction replacement theorem with explicit constant `4880`. Other source-backed nine-direction notes exist, but their PASS labels were not used as substitutes for the derivation above. Release/independent-validation status still requires owner/B20 synthesis and the required genuinely separate reviews.
