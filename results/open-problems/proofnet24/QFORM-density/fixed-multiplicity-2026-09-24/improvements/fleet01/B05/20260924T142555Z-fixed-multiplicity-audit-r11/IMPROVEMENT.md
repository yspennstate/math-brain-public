# fleet01/B05 r11 — nine-direction reconstruction and a sharp threshold-eight no-go

Run: `20260924T142555Z-fixed-multiplicity-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, owner-recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **complete independent reconstruction of the nine-direction replacement; eight-direction bounded density remains open.** This file does not self-award release or independent-validation status and does not claim the unrestricted three-eigenvalue conjecture.

## 1. The nine-direction theorem

Let `X=(X_1,...,X_n)` have independent real coordinate densities bounded by `K`. Let `A=A^T` be arbitrary and let `b,c` be arbitrary. If

` s_9(A)>=s>0, `

then

` Q=X^TAX+b^TX+c `

has an essentially bounded density with

`boxed: ||p_Q||_infinity <= (2010+1200 log16) K^2/s <5338 K^2/s.`

No Gaussianity, log-concavity, moment, support, iid, exact-rank, leverage, sign, or post-rotation-independence assumption is used. Global continuity is not asserted; the order-three no-pivot Fourier receiver gives a `C_0` density, while pivot branches are measure-domination arguments.

The proof below is a B05 reconstruction from the audited 17-direction baseline plus the grouped product-Fourier mechanism. Normalize `K=s=1` until the final scaling step and retain

`eta=1/100,  kappa=1/6400.`

## 2. Grouped product-Fourier compiler

Let `H,I,J` be disjoint original-coordinate banks. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`. Consider

`Q=F(X_H)+2<W,M X'+beta>+R(X'),   X'=(X_I,X_J),`

with arbitrary measurable finite `F`, arbitrary quadratic/affine `R`, and assume the `J` restriction `M_J` has row rank `k`. Let `S` be the product of its nonzero singular values.

For each physical `I` row `a_i` in the `I-J` crossing of `R`, decompose

`a_i=c_i+lambda_i M_J,    c_i perpendicular to row(M_J).`

Write the residual rows as `C`. For `ell>=1`, set

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0,`

`w_T=det(C_T C_T^T)/Z_ell,`

`alpha_i=sum_{T contains i} w_T,`

and assume each positive `alpha_i<=1/2`. Put `d=k+ell`.

### Claim

For `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,                 (2.1)

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`   (2.2)

If `d>2`,

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d))(ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d)).`                                  (2.3)

### Proof

Push the complex measure `e^{itF}dP_H` through `W`. Its complex density `a_t` satisfies `|a_t|<=p_W`, hence

`||a_t||_2^2<=M_H`.

Plancherel and `xi=2t(y+beta)` give

`int |hat a_t(2t(y+beta))|^2 dy <= M_H (pi/|t|)^k.`            (2.4)

Push `e^{itR}dP_{X'}` through `M X'`, obtaining a complex density `mu_t`; full row rank of `M_J` and the audited product-projection theorem ensure absolute continuity. Cauchy–Schwarz gives

`|phi_Q(t)|^2 <= M_H(pi/|t|)^k ||mu_t||_2^2.`                  (2.5)

For rough laws, condition on literal `X_I=x` and convolve the conditional complex pushforward with a compact approximate identity. Expand the squared `L^2` norm using one independent copy `X'_J`. Put `D=X_J-X'_J`; its coordinates are independent and have densities at most one. Pure `I` phases cancel, pure `J` phases have modulus one, and averaging the original independent `X_i`, `i in I`, produces

`prod_i |psi_i(2t<a_i,D>)|.`

The mollifier contributes a probability-density kernel in `M_JD`. The resulting estimates are uniform in the mollifier; weak compactness/lower semicontinuity in `L^2` passes the estimate to the unsmoothed pushforward. This is the only delicate density-version step and does not use a conditional density cap.

Weighted Hölder over the subset law `w_T` rewrites the Fourier product using exponents `1/alpha_i`. For one positive-weight `T`, the deterministic linear image

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T).`

The audited product-projection lemma plus deterministic SVD scaling therefore gives density cap

`e^(d/2)/(S sqrt(det(C_T C_T^T))).`                              (2.6)

Because `alpha_i<=1/2`, the audited scalar Fourier-power theorem applies at `p=1/alpha_i>=2`; after scale `2t`,

`int |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`                                   (2.7)

The determinant geometric mean is

`prod_T det(C_TC_T^T)^(-w_T/2)
 =Z_ell^(-1/2) exp(H(w)/2).`

The marginal factors contribute

`exp((1/2)sum_i alpha_i log alpha_i).`

Uniformly order a subset sampled from `w`. Entropy subadditivity gives

`H(w)+log(ell!) <= ell log ell-sum_i alpha_i log alpha_i`,

so

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`      (2.8)

Substitute (2.6)–(2.8) in (2.5) and take a square root; this is (2.1)–(2.2). For `d>2`,

`int_R min(1,K|t|^(-d/2))dt=2d/(d-2)K^(2/d)`;

Fourier inversion cancels the remaining `pi` and gives (2.3). Every probabilistic factor before deterministic SVD scaling is an original-coordinate product law.

## 3. Marginal-free order-three density receiver

Let `M` be any literal physical cross block and put

`Z=E_3(M)=e_3(MM^T)>0`.

For row `i`, let `J_i` be the sum of the three-row Gram determinants containing that row. Then `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, (2.3) with `(k,ell,d)=(0,3,3)` gives

`||p_Q||_infinity <= C_3 Z^(-1/6),`

where

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                (3.1)

If one row `w` is heavy, promote that literal original coordinate. Project all remaining rows off `w`; exact Gram–Schmidt/Cauchy–Binet gives

`J_i=||w||^2 e_2(CC^T).`                                       (3.2)

If the residual order-two marginals are light, use `(k,ell)=(1,2)`. If a residual row is heavy, promote it; with two-row promoted matrix `P` and residual `C_2`,

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4.`                     (3.3)

If the residual one-volume is light, use `(2,1)`. If another row is heavy, its literal three-row determinant exceeds `H_ij/2>Z/8`; the terminal rank-three Plancherel receiver gives

`||p_Q||_infinity <=3 sqrt(e)[det(P_3P_3^T)]^(-1/6)<7Z^(-1/6).`

The intermediate constants are smaller than `C_3`, so universally

`boxed: ||p_Q||_infinity <= C_3 E_3(M)^(-1/6).`                 (3.4)

Each branch has an integrable characteristic-function majorant, hence the fixed-crossing conclusion is `C_0`.

## 4. Marginal-free order-two half-potential receiver

For a literal cross block with `Z=E_2(M)>0`, the same promotion tree one dimension lower yields

`boxed: sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8),`                  (4.1)

where

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796486...`.

In the diffuse branch `(k,ell,d)=(0,2,2)`,

`|phi(t)|<=min(1,pi e 2^(3/4)Z^(-1/4)|t|^-1)`.

Insert this in the audited Riesz identity; `int |t|^-1/2 min(1,L/|t|)dt=8sqrt L`. One heavy-row promotion and the terminal rank-two half-potential receiver have strictly smaller constants. This is deliberately not a rank-two density theorem.

## 5. Assembly under `s_9(A)>=1`

### No pivot

The audited baseline `prop:volume` at order three gives

`V_3(A)>=kappa^3.`

The fair physical cut gives a cross block with

`E_3(M)>=4^-3 kappa^3`, hence `E_3(M)^(-1/6)<=160`. By (3.4),

`||p_Q||_infinity <=160 C_3=2370.93402605488...<2400.`          (5.1)

### Scalar pivot

A scalar pivot leaves at least eight unit Schur directions. If that Schur complement itself has a pivot, the audited baseline pivot half-potential bound is exactly

`H(R)<=200+120 log16`;

adding the outside-unit tail gives

`sup_a E|R-a|^-1/2 <=201+120 log16.`                            (5.2)

If the Schur complement has no pivot, it has `s_5>=1`; baseline `prop:volume` at order two and a fair cut give

`E_2(M_R)>=4^-2 kappa^2`.

Equation (4.1) gives

`sup_a E|R-a|^-1/2 <=C_2 sqrt(160)=152.99191115498...`,          (5.3)

smaller than (5.2). The outer square profile contributes `eta^-1/2=10`, so

`||p_Q||_infinity <=2010+1200 log16
 =5337.106466687737...<5338.`                                   (5.4)

### Pair pivots

A definite pair gives at most `pi/sqrt(eta)=10pi<32`. An indefinite pair removes at most two spectral directions, leaving at least seven under `s_9`; in particular the Schur remainder has operator norm at least one, so the audited hyperbolic/logarithmic argument applies verbatim and gives `<251`.

These alternatives exhaust the normalized theorem.

### Scaling

Let `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

The coordinates of `Y` have densities at most one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Thus

`||p_Q||_infinity <=(2010+1200 log16)K^2/s<5338K^2/s.`          (5.5)

This is a complete replacement proof modulo only the baseline lemmas audited line-by-line in the companion B05 `AUDIT.md`.

## 6. How far the threshold lowers here

The complete theorem lowers `17 -> 9`. The current repository also contains multiple genuinely separate end-to-end PASS reconstructions of the nine-direction argument. I independently reconstructed it above; I do not convert review counts into an owner-level validation/release claim.

The threshold `8` remains open. In the no-pivot `s_8>=1` terminal chamber, existing exact work forces nonzero overlap-one and two-sided collar currencies and a critical split-row Fourier endpoint, but the endpoint has only `|phi(t)|<=min(1,U/|t|)`. This gives every finite `L^r` norm and `epsilon log(1/epsilon)` small balls, not `L^infinity`.

The new B05 result below shows that one particularly tempting repair is impossible: **two-sided `E_2`/`Xi_2` or a bounded product-projection coefficient law alone cannot remove the logarithm when arbitrary same-bank quadratic phases are retained.** The overlap-one/spectral currency really must be spent.

## 7. New theorem: `QFORM-S8-XI2-ONLY-RECEIVER-FALSE-v1`

For every `c>0` there is a six-coordinate admissible cap-one product law and a symmetric no-scalar-pivot quadratic matrix for which the three-bank two-sided collar `Xi_2` and both split-row order-two volumes are strictly positive, while the scalar output density is unbounded. If `c^2<eta`, the matrix even has no manuscript `eta`-pivot. Its overlap-one three-minor currency is identically zero because the matrix has rank two.

Consequently **no theorem whose only structural input is a positive lower bound on `Xi_2` (or on the product `Z_2(B_L)Z_2(B_R)`) can imply a bounded scalar density while allowing arbitrary same-bank quadratic phases.** This is an intermediate-receiver counterexample, not an `s_8` counterexample.

### Construction

Let

`H=[[0,1],[1,0]]`

and let `J_3` be the `3x3` all-ones matrix. Put

`A=c (J_3 tensor H).`                                           (7.1)

Partition the six physical coordinates into three two-coordinate banks `L,M,R`. Let all six input variables be independent `Unif[-1/2,1/2]`, so every density is exactly one on its support.

All diagonal entries of `A` vanish. Any principal physical two-by-two block is either zero or

`cH`,

whose determinant has modulus `c^2`. Hence if `c^2<eta=1/100`, this example has no manuscript `eta`-pivot.

Because `rank(J_3)=1` and `rank(H)=2`,

`rank(A)=2.`                                                     (7.2)

Therefore every `3x3` minor is zero, including every overlap-one bordered minor; in particular

`Omega_1(A)=0.`                                                  (7.3)

On the other hand, the literal two-bank cross blocks are

`A[L,M]=A[M,R]=A[R,M]=cH`,

so

`Z_2(A[L,M])=c^4,   Z_2(A[R,M])=c^4,`

and the split-row product is

`P_*=c^8>0.`                                                     (7.4)

The ordered collar `Xi_2(A)` contains the triple `(L,M,R)`, for which

`det A[L,M]^2 det A[M,R]^2=c^8`;

therefore

`Xi_2(A)>=c^8>0.`                                                (7.5)

### Output density

Write each bank as a two-vector and set

`S=X_L+X_M+X_R=(S_1,S_2).`

From (7.1),

`Q=X^TAX=c S^T H S=2c S_1S_2.`                                 (7.6)

`S_1` and `S_2` are independent because they use disjoint original coordinates. Each is the sum of three centered unit uniforms and has a continuous density `g` with

`g(0)=3/4.`                                                     (7.7)

Choose `delta>0` so that `g(x)>=3/8` whenever `|x|<=delta`. For `0<|z|<delta^2`, the product `P=S_1S_2` has density

`p_P(z)=int g(x)g(z/x) dx/|x|`.

Restricting to `|z|/delta <= |x| <= delta` gives

`p_P(z) >= (9/32) log(delta^2/|z|)`,                            (7.8)

(up to an inessential improvement of the front constant depending on whether one keeps both signs). Hence

`lim_{z->0} p_P(z)=infinity`,

and scaling in (7.6) gives

`||p_Q||_infinity=infinity.`                                    (7.9)

Thus the two-sided `E_2` collar can be strong while arbitrary same-bank phases align all three banks into one rank-two opposite-sign/product saddle. The missing ingredient in the genuine `s_8` terminal chamber is precisely what this example lacks: nonzero overlap-one / higher-rank spectral provenance.

## 8. Consequence for the threshold-eight program

The counterexample rules out a broad B05/product-projection shortcut:

> `Xi_2>0` + good two-dimensional product-projection density of the random linear coefficient + arbitrary same-bank phases  **does not** imply bounded scalar output density.

A correct `s_8` proof must use the terminal `Omega_1` / rank-saturated interpolation structure *before* collapsing to the critical split-row `1/|t|` envelope or to an order-two half-potential. In particular, simply conditioning on the middle bank and invoking a bounded two-dimensional coefficient density loses exactly the same-bank phase alignment exhibited by (7.6).

The current lowest complete fixed multiplicity checked in this run is therefore **nine**. Multiplicity eight remains a specific overlap/shared-hub logarithm-removal problem; multiplicity three remains unrestricted and open.

## 9. Review/scope status

- 17-direction pinned baseline: PASS in companion full B05 audit.
- 9-direction replacement: complete proof reconstructed here, same original hypotheses, constant `<5338 K^2/s`; PASS in this B05 review.
- 8-direction theorem: OPEN. New Section 7 is a counterexample only to a weaker intermediate receiver, not to the theorem.
- Full 3-direction conjecture: OPEN / not claimed.
- Full global continuity: not claimed.

Model: GPT-5.6 Sol. Reasoning-effort/provider counters: `UNKNOWN / NOT_EXPOSED`.