# QFORM fixed multiplicity: complete threshold-nine replacement and exact s8 shortcut barriers

Run: `20260924T131357Z-fleet02-B17-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, package SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **complete mathematical replacement proving multiplicity nine with explicit constant 6010; no multiplicity-eight theorem proved.** The unrestricted three-eigenvalue QFORM conjecture remains open.

The grouped Fourier mechanism below was independently reconstructed in this B17 run after the 17-eigenvalue source audit. Related fleet reports exist, but no peer verdict is used as a logical premise below.

## Theorem

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary real symmetric, and let `b,c` be arbitrary. If

` s_9(A) >= s > 0,`

then

`Q=X^T A X+b^T X+c`

has an essentially bounded density and

`||p_Q||_infinity <= 6010 K^2/s`.

There is no support, moment, iid, log-concavity, sign, diagonal-basis, exact-rank, leverage, smoothness, or post-rotation-independence assumption. The theorem asserts essential boundedness, not full global continuity.

Normalize first to `K=s=1`, with the baseline constants

`eta=1/100`, `kappa=1/80^2`.

## 1. Grouped physical-product Fourier compiler

Let `H,I,J` be disjoint sets of original coordinates. Let `X_H` be independent of `X'=(X_I,X_J)`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`. Suppose

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,

where `F` is arbitrary measurable and `R` is an arbitrary quadratic/affine polynomial. Assume the restriction `M_J` has row rank `k`; let `S` be the product of its nonzero singular values. Project the physical `I-J` crossing-row matrix of the quadratic part of `R` orthogonally off `row(M_J)` and call the resulting row matrix `C`.

For an integer `ell>=1`, put

`Z_ell = sum_(|T|=ell) det(C_T C_T^T)`.

Assume `Z_ell>0`, use determinant weights

`w_T=det(C_T C_T^T)/Z_ell`,

and write

`alpha_i = sum_(T contains i) w_T`.

Assume every positive `alpha_i<=1/2`, and set `d=k+ell`.

### Compiler lemma

For `t!=0`,

`|phi_Q(t)| <= min(1,K_(k,ell)|t|^(-d/2))`,

where

`K_(k,ell)=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

When `d>2`, Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
 (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

### Proof

Push the complex measure `e^(itF)dP_H` to `W`; call its density `a_t`. Since its total variation is dominated by the actual projection law,

`|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`.

With the baseline Fourier convention, `k`-dimensional Plancherel and the substitution `u=2t(l+beta)` give

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.       (1)

Push the complex measure `e^(itR)dP_(X')` to the `k`-vector `M X'`; because the literal `J`-block has full row rank, this pushforward is absolutely continuous (after a harmless compact mollifier if desired). Call its density `mu_t`. Pairing the two pushforwards and applying Cauchy--Schwarz gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.             (2)

To estimate the last norm without rotating the product law, mollify `mu_t`, square its `L2` norm, and duplicate only the literal independent `J` coordinates. Pure same-bank quadratic phases have modulus one. Writing `D=X_J-X'_J`, whose coordinates remain independent with densities bounded by one, the standard decoupling expansion reduces the estimate to an integral of the form

`E[ rho(M_J D) prod_i |psi_i(2t<a_i,D>)| ]`,              (3)

where `rho` is a probability density and each `psi_i` is the characteristic function of a physical cap-one coordinate law. Decompose each physical crossing row

`a_i=c_i+lambda_i M_J`,  with `c_i` perpendicular to `row(M_J)`.

Weighted Holder over the `ell`-subsets with weights `w_T` is exact because

`sum_(T contains i) w_T/alpha_i=1`.

For a fixed `T`, the linear map

`D -> (M_JD,(<c_i,D>)_(i in T))`

has Gram determinant

`S^2 det(C_T C_T^T)`.

The baseline product-projection lemma therefore bounds its joint density by

`e^(d/2)/(S sqrt(det(C_T C_T^T)))`.                         (4)

Since `alpha_i<=1/2`, the baseline scalar Fourier-power lemma with `p=1/alpha_i>=2`, followed by the scale `2t`, gives

`int |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.                                  (5)

Thus the fixed-`T` Holder factor is at most

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_(i in T) sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))]`.                                  (6)

The weighted geometric mean of the determinant denominators is

`Z_ell^(-1/2) exp(H(w)/2)`,

while the row-marginal factors contribute

`exp((1/2) sum_i alpha_i log alpha_i)`.

The required entropy cancellation is dimension-free. Sample `T` with law `w_T` and then order its `ell` elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`. Each position has marginal probability `alpha_i/ell`; entropy subadditivity yields

`H(w)+log(ell!) <= ell H(alpha/ell)
 = -sum_i alpha_i log alpha_i + ell log ell`,

hence

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.       (7)

Combining (2)--(7), and then taking square roots, gives the stated `K_(k,ell)|t|^(-d/2)` bound. The mollifier may be removed by the uniform `L2` bound and weak lower semicontinuity; all product structure used above is in original coordinates. Finally

`int_R min(1,K|t|^(-d/2))dt = 2d/(d-2) K^(2/d)`

for `d>2`, and inversion gives the density bound. QED.

### Exact-rank terminals

The same complex-pushforward/Plancherel argument with no residual crossing block gives, for `r` promoted physical rows crossing a product bank through a full-rank matrix `P`,

`|phi(t)| <= min(1, pi^(r/2)e^(r/4)[det(PP^T)]^(-1/4)|t|^(-r/2)).`

Therefore

`r=3:  ||p||_infinity <= 3 sqrt(e)[det(PP^T)]^(-1/6)`,

and, by the baseline Riesz formula,

`r=2:  sup_a E|Q-a|^(-1/2)
       <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8)`.                   (8)

## 2. A third crossing volume now gives a density

Let `M` be any literal original-coordinate cross block and set

`Z=E_3(M)=e_3(MM^T)>0`.

Equivalently `Z` is the sum of the Gram determinants of all physical row triples. Let `J_i` be the part of this sum over triples containing row `i`, so `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply the compiler with `(k,ell,d)=(0,3,3)`. This gives

`||p||_infinity <= C_3 Z^(-1/6)`,

with

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                (9)

If some `J_i>Z/2`, promote the literal physical row `w=m_i` and project all other rows orthogonally off `w`; call the residual matrix `C`. Gram--Schmidt gives the exact aggregate identity

`J_i=||w||^2 e_2(CC^T)`.                                        (10)

If every canonical `e_2` row marginal of `C` is at most one half, use `(k,ell,d)=(1,2,3)`; its constant is `<10.958 Z^(-1/6)`.

Otherwise promote a residual-heavy row `j`. Promoting the corresponding **physical** original row is legitimate because adding its component parallel to `w` does not alter the span or Gram determinant. If `P` is the two promoted physical rows and `C_2` is the rest projected off their span, another Gram--Schmidt identity gives

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4`.                      (11)

If every one-volume marginal of `C_2` is at most one half, use `(k,ell,d)=(2,1,3)`, giving `<8.264 Z^(-1/6)`.

Otherwise a residual-heavy third physical row has

`det(P_3P_3^T)>H_ij/2>Z/8`,                                    (12)

and the `r=3` terminal (8) gives `<7 Z^(-1/6)`.

Thus all branches obey the uniform marginal-free receiver

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,                        (13)

with `C_3` from (9). Every branch has an integrable characteristic-function majorant, so this receiver has a continuous `C_0` density.

## 3. A second crossing volume gives the full half potential

For a literal cross block put `Z=E_2(M)=e_2(MM^T)>0`.

If all canonical row marginals are at most one half, the compiler with `(k,ell,d)=(0,2,2)` gives

`|phi(t)| <= min(1, pi e 2^(3/4) Z^(-1/4)|t|^(-1))`.

The baseline Riesz estimate uses

`int_R min(1,L/|t|)|t|^(-1/2)dt=8 sqrt(L)`

and yields

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

where

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.                    (14)

If one row carries more than half the `E_2` mass, promote it. Gram--Schmidt gives incident mass

`K_i=||w||^2||C||_F^2>Z/2`.

If all residual one-volume marginals are at most one half, the `(1,1,2)` compiler plus Riesz gives `<9.79 Z^(-1/8)`. If a residual row is heavy, the corresponding physical two-row Gram determinant satisfies

`D>K_i/2>Z/4`,

and the `r=2` terminal in (8) gives `<8.64 Z^(-1/8)`. Therefore (14) holds without any marginal hypothesis. This is a full negative-half-potential estimate, not a rank-two density theorem.

## 4. Nine large eigenvalues suffice

Assume `s_9(A)>=1`.

### No `eta`-pivot

The audited baseline spectral-to-volume proposition at `k=3` applies because `4k-3=9`:

`V_3(A)>=kappa^3`.

The audited fair coordinate cut gives a literal physical cross block `M` with

`E_3(M)>=4^(-3)kappa^3`.

Hence

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

Using (13),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488... <2400`.                                   (15)

### Scalar pivot

Suppose `|A_hh|>=eta`. The audited Schur count leaves at least eight eigenvalues of modulus at least one in the scalar Schur complement `S`.

If `S` has an `eta`-pivot, the audited baseline pivot theorem (which needs only two surviving unit-scale directions) gives truncated half potential `<=600`; the tail `|R-a|>1` contributes at most one, so the full half potential is `<=601`.

If `S` has no `eta`-pivot, then `s_5(S)>=1`. Apply the audited spectral-to-volume proposition at `k=2`, then the fair cut:

`E_2(M_S)>=4^(-2)kappa^2`.

Equation (14) gives

`sup_a E|R-a|^(-1/2)
 <= C_2 (4^(-2)kappa^2)^(-1/8)
 = C_2 sqrt(160)
 =152.99191115498... <153`.                                     (16)

Thus in both scalar-pivot subcases the full Schur half potential is at most `601`. The audited square profile multiplies by `eta^(-1/2)=10`, giving

`||p_Q||_infinity <=6010`.                                      (17)

### Definite two-coordinate pivot

The audited definite-pair lemma gives directly

`||p_Q||_infinity <= pi/sqrt(eta)=10pi<32`.                     (18)

### Indefinite two-coordinate pivot

The pair Schur complement retains at least seven unit-scale eigenvalues, hence operator norm at least one. The audited hyperbolic envelope and quarter-power logarithmic-potential bound therefore apply exactly as in the baseline and give

`||p_Q||_infinity<251`.                                         (19)

The no-pivot, scalar-pivot, definite-pair, and indefinite-pair cases exhaust the normalized problem. Equations (15)--(19) prove the normalized theorem with constant `6010`.

For general `K,s`, set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q`.

The coordinates of `Y` have density cap one and `s_9(A/s)>=1`; scalar density rescaling gives

`||p_Q||_infinity <=6010 K^2/s`.

## 5. Closed dependency map

The threshold-nine theorem uses only these audited baseline components plus the new compiler/receivers proved above:

`BL heat flow -> product-projection cap + scalar Fourier powers`

`product-projection/scalar Fourier -> grouped compiler -> E3 density receiver + E2 half-potential receiver`

`sampling/completion/rank + diagonal dominance -> baseline spectral-to-volume proposition`

`random cut + spectral-to-volume(k=3) + E3 receiver -> no-pivot s9 density`

`Schur count + {pivot-H OR spectral-to-volume(k=2)+E2 receiver} + square profile -> scalar-pivot s9 density`

`definite/hyperbolic pair lemmas -> pair-pivot branches`

`four normalized branches + scaling -> 6010 K^2/s`.

No unproved lower-threshold statement is inserted into this dependency chain.

## 6. Exact adversarial barriers at multiplicity eight

The theorem above rigorously lowers 17 to 9. I do **not** claim 8. Three tempting shortcuts are invalid.

### Barrier A: `s_8>=1` does not force a physical pivot

For any integer `m>=11`, let `J_m` be the all-ones `m x m` matrix and

`B_m = [[0,J_m/m],[J_m/m,0]]`,

and set

`A_m = B_m direct-sum B_m direct-sum B_m direct-sum B_m`.

Each `J_m/m` has singular values `1,0,...,0`, so each `B_m` has spectrum

`{1,-1,0,...,0}`.

Therefore

`spec_nonzero(A_m)={1,1,1,1,-1,-1,-1,-1}`,

so `s_8(A_m)=1` and `s_9(A_m)=0`.

Every physical diagonal entry is zero. A principal `2x2` determinant is either zero or `-1/m^2`; since `m>=11`,

`1/m^2 <=1/121 < eta=1/100`.

Thus `A_m` has **no `eta`-pivot**. Choosing, for example, independent `Unif[-1/2,1/2]` physical inputs gives a perfectly source-valid cap-one family. This is not a counterexample to an eight-eigenvalue density theorem; it is an exact counterexample to the shortcut “eight large eigenvalues force the pivot branch.” Any s8 proof must genuinely close a no-pivot chamber.

### Barrier B: the existing interpolation rank count is exactly one direction short at `m=8,r=2`

The abstract rank data used in the audited spectral-to-volume proof cannot by themselves turn `s_8` into the order-three volume lower bound. Let the first four coordinates be the seed `S union T` and `L={5,6,7,8}`. Set

`D=diag(0,0,0,0,1,1,0,0)`,

`R=I_8-D`.

Then

`D+R=I_8`, so `s_8(D+R)=1`,

`rank R=6=3r`,

`rank R[L,L]=2=r`,

and `D` vanishes on the `2r=4` seed coordinates. Exactly two, not three, large diagonal entries are forced in `L`. Therefore the rank inequalities used by the existing `r=2` contradiction are saturated at multiplicity eight and cannot alone produce the required `r+1=3` diagonal-dominance directions. This is a proof-mechanism obstruction, not a QFORM counterexample.

### Barrier C: order two cannot simply be promoted from half-potential to density

Let `U,V` be independent `Unif[-1/2,1/2]`. The density of `U^2` is

`h(x)=x^(-1/2) 1_(0,1/4)(x)`.

For `Q=U^2-V^2`, the difference density at zero would be

`p_Q(0)=int_0^(1/4) h(x)^2 dx = int_0^(1/4) dx/x = infinity`,

and in fact the density has the familiar logarithmic singularity near zero. Thus the order-two `|t|^-1` Fourier endpoint is genuinely insufficient for a leverage-free bounded-density conclusion under the target rough-law class. The E2 receiver above is correctly used only for a negative-half potential inside the scalar-pivot branch.

These barriers explain why the completed proof stops at nine without asserting optimality. Current multiplicity eight remains an open fixed-multiplicity endpoint; the unrestricted three-eigenvalue problem remains open as well.