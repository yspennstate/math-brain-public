# account02/B10 improvement — complete nine-direction replacement

Status: **COMPLETE REPLACEMENT PROOF IN THIS RUN; do not self-award release/validation status.**

Pinned baseline: source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This proof preserves all original hypotheses: independent arbitrary real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine `b,c`. It uses only literal original-coordinate product independence. It does **not** solve the unrestricted three-eigenvalue conjecture.

## Theorem

If `s_9(A)>=s>0`, then

`Q=X^T A X+b^T X+c`

has an essentially bounded density satisfying

`||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s`.

Global continuity is not asserted; the no-pivot Fourier branch is continuous, while the pivot branches are measure-domination arguments.

Normalize first to `K=s=1`, and retain the baseline parameters

`eta=1/100`, `kappa=1/80^2`.

## 1. Grouped product-Fourier compiler

Let `H,I,J` be disjoint literal original-coordinate banks. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`. Consider

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`,

with arbitrary measurable `F`, arbitrary quadratic/affine `R`, and `M_J` of row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`. Let `C` be the physical `I-J` crossing block of the quadratic part of `R`, projected orthogonally in coefficient space away from `row(M_J)`.

For `ell>=1`, set

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,
`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=sum_{T contains i} w_T`,

and assume every positive `alpha_i<=1/2`. Indices with `alpha_i=0` are discarded from the Fourier product (their factors have modulus at most one); this explicit convention repairs the otherwise undefined notation `1/alpha_i`. Put `d=k+ell`.

Then, for `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
 (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`                 (1)

For `d>2`,

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d))(ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d)).`                                    (2)

### Proof of (1)--(2), including rough laws

Push `e^{itF}dP_H` through `W`. Its complex density `a_t` is dominated in variation by `p_W`, so `||a_t||_2^2<=M_H`. Plancherel and `xi=2t(y+beta)` give

`int |hat a_t(2t(y+beta))|^2 dy <= M_H (pi/|t|)^k`.             (3)

Push `e^{itR}dP_{X'}` through the relevant `k`-dimensional linear image; call the complex density `mu_t`. Cauchy--Schwarz yields

`|phi_Q(t)|^2 <= M_H(pi/|t|)^k ||mu_t||_2^2`.                   (4)

For rough densities, do not assume the conditional pushforward is already in `L^2`. Condition on `X_I=x`, convolve the conditional complex pushforward with a compact approximate identity `rho_eps`, expand its square with an independent copy `X'_J`, and then average in the original `X_I` variables before taking absolute values. Pure `I` terms cancel and pure `J` terms have modulus one. With `D=X_J-X'_J`, whose coordinates remain independent cap-one variables, one obtains uniformly in `eps`

`E_D[kappa_eps(M_JD) prod_i |psi_i(2t<a_i,D>)|]`,              (5)

where `kappa_eps=rho_eps*tilde(rho_eps)` is a probability density. Fourier Fatou (`hat rho_eps ->1`, `|hat rho_eps|<=1`) and Fatou in the conditioning variable pass the uniform bound to the unsmoothed `L^2` pushforward. Thus no moments, smoothness, bounded support, or illicit conditional density cap is introduced.

Write each physical row `a_i=c_i+lambda_i M_J`, with `c_i` orthogonal to `row(M_J)`. Weighted Hoelder over the positive-weight `ell`-subsets reduces (5) to a geometric mean. For fixed `T`, the linear map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant exactly

`S^2 det(C_T C_T^T)`.

The baseline product-projection theorem, followed only by deterministic SVD scaling, bounds its density by

`e^(d/2)/(S sqrt(det(C_T C_T^T)))`.                              (6)

For every positive `alpha_i<=1/2`, the baseline scalar Fourier-power lemma at `p=1/alpha_i` gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy <= pi sqrt(2e alpha_i)/|t|`. (7)

The weighted determinant product contributes

`Z_ell^(-1/2) exp(H(w)/2)`,

and the marginal factors contribute

`exp((1/2) sum_i alpha_i log alpha_i)`.

Order a random `ell`-subset uniformly after sampling it from `w`. Entropy subadditivity gives

`H(w)+log(ell!) <= -sum_i alpha_i log(alpha_i/ell)`,

hence

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.       (8)

Combining (3)--(8) and taking the square root gives (1). Direct integration of `min(1,K|t|^(-d/2))` is `2d/(d-2) K^(2/d)`; Fourier inversion gives (2). The formal `k=0` case is interpreted as a zero-dimensional hub, with `M_H=S=1`; equivalently repeat the light-bank part directly.

## 2. Terminal exact-rank receivers

If there is no residual projected block and `r` literal physical original coordinates cross the independent product bank through a rank-`r` block `P`, the same complex-pushforward/Plancherel calculation gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4)[det(PP^T)]^(-1/4)|t|^(-r/2)).` (9)

Consequently

`r=3: ||p||_infinity <= 3 sqrt(e)[det(PP^T)]^(-1/6)`,           (10)

and the baseline Riesz inequality gives

`r=2: sup_a E|Q-a|^(-1/2) <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8)`. (11)

Same-bank phases remain in the complex measures; no projected coordinates are declared independent.

## 3. Third crossing volume implies bounded density

Let a literal original-coordinate crossing block be `M`, and set

`Z=E_3(M)=e_3(MM^T)>0`.

Let `J_i` be the sum of all three-row Gram determinants containing physical row `i`. Then `sum_i J_i=3Z`.

If every canonical marginal `J_i/Z<=1/2`, (2) at `(k,ell,d)=(0,3,3)` gives

`||p_Q||_infinity <= C_3 Z^(-1/6)`,

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                 (12)

If some `J_i>Z/2`, keep row `w=m_i` as a literal hub and project all other crossing rows orthogonally off `w`. Gram--Schmidt/Cauchy--Binet gives the exact aggregate identity

`J_i=||w||^2 e_2(CC^T)`.                                        (13)

If the residual second-volume marginals are diffuse, use (2) at `(1,2,3)`. If a residual physical row is heavy, promote it. With the two promoted rows `P` and remaining projected rows `C_2`, the exact identity is

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4`.                      (14)

If the residual one-volume is diffuse, use `(2,1,3)`. If another row is heavy, its literal three-row Gram determinant is `>H_ij/2>Z/8`, and (10) applies. The corresponding constants are respectively

`14.81834`, `<10.958`, `<8.264`, `<7`,

so (12) is the uniform worst branch:

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.                        (15)

Every branch here has an integrable characteristic-function envelope.

## 4. Second crossing volume implies a full half-potential

For `Z=E_2(M)>0`, the same promotion tree one dimension lower gives

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

where

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796486...`.                  (16)

In the diffuse branch, (1) at `(0,2,2)` is

`|phi(t)|<=min(1,L/|t|)`,
`L=pi e 2^(3/4) Z^(-1/4)`.

The baseline Riesz formula and

`int_R |t|^(-1/2) min(1,L/|t|) dt = 8 sqrt L`

give (16). One heavy-row promotion and the terminal rank-two receiver give strictly smaller constants. This is deliberately a half-potential theorem, not a rank-two density theorem.

## 5. Assembly under nine large singular values

### 5.1 No pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited baseline spectral-to-volume proposition at order three gives

`V_3(A)>=kappa^3`.

A fair literal original-coordinate cut gives a crossing block with

`E_3(M)>=4^(-3)kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

Equation (15) yields

`||p_Q||_infinity <=160 C_3=2370.93402605488...<2400`.           (17)

### 5.2 Scalar pivot

If `|A_hh|>=eta`, complete the square in the original coordinate `X_h`. The Schur complement retains at least eight unit-scale eigenvalues.

If that Schur complement has an `eta`-pivot, the audited baseline pivot calculation (which needs only two surviving large directions) gives exactly

`H(R)<=200+120 log16`.

The tail outside distance one costs at most one, hence

`sup_a E|R-a|^(-1/2) <=201+120 log16`.                            (18)

If the Schur complement has no pivot, it has `s_5>=1`. The baseline structural proposition at order two and a fair cut give

`E_2(M_R)>=4^(-2)kappa^2`.

Using (16),

`sup_a E|R-a|^(-1/2) <= C_2 sqrt(160)
 =152.99191115498024...`,                                        (19)

which is smaller than (18). The outer square profile contributes `eta^(-1/2)=10`, so

`||p_Q||_infinity <=2010+1200 log16
 =5337.106466687737...<5338`.                                    (20)

### 5.3 Two-coordinate pivots

A definite pair has conditional density at most

`pi/sqrt(eta)=10pi<32`.

An indefinite pair removes only two Schur directions; at least seven remain, so in particular the Schur quadratic part has norm at least one. The audited baseline hyperbolic envelope plus quarter-power logarithmic potential gives

`||p_Q||_infinity <=10(10+5 log16)+1/e
 =238.99731555316...<251`.                                       (21)

The no-pivot, scalar-pivot, definite-pair and indefinite-pair alternatives exhaust the normalized problem. Equation (20) is largest.

## 6. Scaling

For general `K,s`, let `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then the coordinates of `Y` have densities at most one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Therefore

`||p_Q||_infinity <=(2010+1200 log16)K^2/s<5338 K^2/s`.          (22)

## Closed dependency map

Pinned manuscript inputs:

`Fourier/Plancherel + geometric BL -> product projection cap + scalar Fourier powers`;

`rank perturbation + Schur count + square/definite/hyperbolic kernels + quarter-power log control -> pivot branches`;

`disjoint-minor sampling + nonsymmetric completion + restricted rank + diagonal dominance -> no-pivot V_2,V_3`;

`fair original-coordinate cut -> literal E_2,E_3 crossing volumes`.

New replacement inputs proved above:

`complex-pushforward Plancherel + rough-law mollification/Fatou + weighted physical-minor entropy -> grouped compiler`;

`grouped compiler + exact Gram--Schmidt promotion identities -> E_3 density receiver and E_2 half-potential receiver`;

`those receivers + pinned structural/pivot branches -> threshold nine`.

No source-variable rotation, post-rotation independence, support/moment/log-concavity assumption, or spectral truncation is introduced.

## Why this proof stops at nine

At the order-three structural step the worst bad-ratio seed is `r=2`. The audited completion only gives global `rank R<=6` and restricted `rank R_LL<=2`. Under `s_8>=1`, rank subtraction can force only two large diagonal residual coordinates, and an invertible diagonally dominant `2x2` block is perfectly compatible with restricted rank two. Under `s_9`, three such coordinates are forced and the contradiction closes. The exact finite matrix recorded in the sibling B10 audit simultaneously attains `rank R=6` and `rank R_LL=2`, so these rank constants cannot be lowered by a cosmetic rewrite.

Nor can a generic order-two indefinite quadratic replace the order-three density endpoint. For independent `U,V~Uniform[-1,1]` (densities `1/2<=1`), `U^2` has density `1/(2 sqrt y)` on `(0,1)`, and the density of `U^2-V^2` at zero contains

`int_0^1 (1/(2 sqrt y))^2 dy = infinity`.

Thus an `E_2` crossing-volume lower bound alone cannot imply bounded density. This is a counterexample to that prospective proof interface, not to an eight-direction theorem. A threshold below nine needs genuinely additional overlap/multibank structure or a different receiver.
