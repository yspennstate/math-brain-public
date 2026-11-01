# fleet02/B11 — complete nine-eigenvalue replacement review and Schur barrier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `fleet02-B11-20260924T134908Z-r11`  
Pinned baseline: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Upstream candidate reconstructed after my independent baseline audit: `improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`, blob `054facef834d29927713c5d42a1f09a541c5644b`. I also read the later independent fleet01/B07 reconstruction, blob `974f935ea42a5f8f6dcdeb6255b0ca64d7d59ffd`, only after reconstructing the essential argument.

## Verdict

**PASS in this B11 reconstruction of a complete fixed-multiplicity improvement from 17 to 9 eigenvalues.** More precisely:

> Let `X_1,...,X_n` be independent real random variables with densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, with arbitrary `b,c`. If `s_9(A)>=s>0`, then
> 
> `Q=X^T A X+b^T X+c`
> 
> has an essentially bounded density and
> 
> `||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s`.

The no-pivot branch has an integrable characteristic function and hence a continuous `C_0` density. I do not claim global continuity for pivot branches. This is **not** the unrestricted three-eigenvalue theorem; that problem remains open. I am recording a mathematical review/improvement artifact, not changing an owner-level release flag.

The proof below is dependency-closed relative to the audited baseline manuscript: it invokes only baseline lemmas whose hypotheses were independently checked in the sibling B11 audit, and it proves the one new grouped product-Fourier compiler and its promotion consequences.

## 1. New grouped product-Fourier compiler

Let `H,I,J` be disjoint sets of original coordinates. Let `W=L_H X_H` be a `k`-dimensional orthogonal projection of the product vector `X_H`, and suppose its density is bounded by `M_H`. Let `X'=(X_I,X_J)`, independent of `X_H`, and consider

`Q=F(X_H)+2 <W,M X'+beta>+R(X')`,

where `F` is arbitrary measurable, `R` is an arbitrary quadratic/affine polynomial, and `M_J` has row rank `k`. Let `S>0` be the product of the nonzero singular values of `M_J` (empty product one when `k=0`).

Write the physical `I x J` cross rows of the quadratic part of `R` as

`a_i=c_i+lambda_i M_J`,

with each `c_i` orthogonal to `row(M_J)`. For `ell>=1` define

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,

`w_T=det(C_T C_T^T)/Z_ell`,

and row marginals

`alpha_i=sum_{T contains i} w_T`.

Assume `alpha_i<=1/2` for every row with `alpha_i>0`, and put `d=k+ell`.

### Claim 1: characteristic-function bound

For `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^{-d/2})`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.       (1)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
 e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
 S^(-1/d) Z_ell^(-1/(2d))`.                                    (2)

### Proof

Push the complex measure `e^{itF} dP_H` through `W`; call its density `a_t`. Since `|a_t|<=p_W`,

`||a_t||_2^2 <= ||p_W||_infinity int p_W <= M_H`.

The baseline proves one-dimensional Plancherel. Iterating that identity by Fubini first on tensor products and then by `L^2` density gives the standard `k`-dimensional version with this Fourier convention,

`int_R^k |hat a(xi)|^2 dxi=(2pi)^k ||a||_2^2`.

After the affine scaling `xi=2t(l+beta)`, therefore

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.             (3)

Push `e^{itR}dP_{X'}` through the linear variable `M X'`; denote the resulting complex measure by `mu_t`. Pairing the two pushforwards and applying Cauchy–Schwarz gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`,                 (4)

provided the right side is finite. We now prove the required `L^2` bound without assuming smooth input laws.

Condition on the original coordinates `X_I=x`. Convolve the conditional complex pushforward through `M_J X_J` with a compact probability approximate identity `rho_epsilon`. Hilbert-space Jensen bounds the squared norm of the global smoothed mixture by the average conditional squared norms. Expand each squared norm with an independent copy `X'_J`. Pure `I` phases cancel; pure `J` phases remain modulus one. With `D=X_J-X'_J`, whose coordinates are independent and have density cap one, integration over the original independent `X_i`, `i in I`, leaves

`E_D [kappa_epsilon(M_J D) prod_i |psi_i(2t<a_i,D>)|]`,         (5)

where `kappa_epsilon=rho_epsilon*tilde(rho_epsilon)` is a probability density and each `psi_i` is a characteristic function of a cap-one scalar law. The estimate derived below is independent of `epsilon`. On the Fourier side `hat rho_epsilon ->1` and `|hat rho_epsilon|<=1`; Fatou therefore promotes the uniform smoothed `L^2` bound to the unsmoothed complex pushforward. Equivalently, the limiting Fourier transform is in `L^2`, so Plancherel identifies an `L^2` density. This closes the rough-law limit without moments or support assumptions.

Discard rows with `alpha_i=0`. The exact weighted identity

`prod_i |psi_i| = prod_T [prod_{i in T}|psi_i|^(1/alpha_i)]^(w_T)`

and generalized Holder reduce (5) to a weighted geometric mean over fixed `ell`-subsets `T`.

For a fixed `T`, the linear map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T)`,

because all `c_i` are orthogonal to `row(M_J)`. Factoring this full-row-rank map into an invertible `d x d` matrix times an orthonormal projection and using the audited baseline product-projection lemma shows that its joint density is at most

`e^(d/2)/[S sqrt(det(C_T C_T^T))]`.                             (6)

Using `int kappa_epsilon=1`, we may integrate the first `k` output variables. For each `i in T`, the baseline scalar Fourier-power lemma with `p=1/alpha_i>=2`, including the scale `2t`, gives

`int_R |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|`.                                   (7)

Hence the fixed-`T` integral is at most

`e^(d/2)[pi sqrt(2e)/|t|]^ell
 prod_{i in T}sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))]`.                                   (8)

The weighted geometric mean of the determinant factors is exactly

`Z_ell^(-1/2) exp(H(w)/2)`,

because `det(C_T C_T^T)=Z_ell w_T`. The marginal factors contribute

`exp((1/2) sum_i alpha_i log alpha_i)`.

To bound their product, sample `T` with law `w` and then order its `ell` elements uniformly. The ordered tuple has entropy `H(w)+log(ell!)`; each position has marginal probabilities `alpha_i/ell`. Entropy subadditivity yields

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.       (9)

Combine (8) and (9), then (4), and take square roots. This gives (1). For `d>2`,

`int_R min(1,K|t|^(-d/2))dt = 2d/(d-2) K^(2/d)`.

Division by `2pi` in Fourier inversion cancels the `pi` arising from `(pi^(d/2))^(2/d)` and gives (2). QED.

### Terminal promoted rows

If `r` literal original coordinates are promoted as a physical hub and cross a disjoint product bank through a rank-`r` block `P`, the same complex-pushforward/Plancherel proof with no residual projected rows gives

`|phi(t)| <= min(1, pi^(r/2)e^(r/4)[det(PP^T)]^(-1/4)|t|^(-r/2))`. (10)

Here the physical `r`-coordinate density cap is one and the opposite `r`-dimensional product projection has density cap at most `e^(r/2)`. Thus

`r=3: ||p||_infinity <= 3 sqrt(e)[det(PP^T)]^(-1/6)`,           (11)

and the audited baseline Riesz formula gives

`r=2: sup_a E|Q-a|^(-1/2)
 <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8)`.                         (12)

All same-bank quadratic phases and affine terms remain inside complex pushforwards; no rotated variables are declared independent.

## 2. Unconditional third crossing-volume density receiver

For any literal original-coordinate cross block `M`, put

`Z=E_3(M)=e_3(MM^T)>0`.

Let `J_i` be the sum of all three-row Gram determinants containing row `i`. Then `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply (2) with `(k,ell,d)=(0,3,3)`:

`||p||_infinity <= C_3 Z^(-1/6)`,

where

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                (13)

If some row `w` has `J_i>Z/2`, promote it. Project every other row orthogonally off `w`; call the residual matrix `C`. Gram–Schmidt on each three-row volume gives the exact aggregate identity

`J_i=||w||^2 e_2(CC^T)`.                                       (14)

If all residual `E_2` row marginals are at most one half, use (2) with `(1,2,3)`; the resulting constant is smaller than `C_3`.

Otherwise promote a residual heavy row `j`. If `P` is the two-row promoted matrix and `C_2` the remaining rows projected off `row(P)`, a second Gram–Schmidt decomposition gives

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4`.                     (15)

If the residual one-volume marginals are diffuse, `(2,1,3)` in (2) is again smaller than (13). Otherwise a third promoted row has literal three-row Gram determinant

`det(P_3P_3^T)>H_ij/2>Z/8`,                                    (16)

and the terminal estimate (11) is also smaller than (13). Therefore, without a marginal hypothesis,

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.                        (17)

Every branch here has an `L^1` characteristic-function envelope, hence a continuous density.

## 3. Unconditional second crossing-volume half-potential receiver

Put `Z=E_2(M)>0`. If every `E_2` row marginal is at most one half, Claim 1 at `(k,ell,d)=(0,2,2)` gives

`|phi(t)| <= min(1,L/|t|)`,

`L=pi e 2^(3/4) Z^(-1/4)`.                                     (18)

The baseline half-Riesz inequality and the exact elementary integral

`int_R |t|^-1/2 min(1,L/|t|) dt=8 sqrt(L)`

give

`sup_a E|Q-a|^-1/2 <= C_2 Z^-1/8`,

`C_2=8 sqrt(e)2^-1/8=12.095072570796...`.                       (19)

If one row is heavy, promote it and project the others orthogonally off it. The incident mass equals `||w||^2||C||_F^2>Z/2`. A diffuse residual uses `(1,1,2)` in Claim 1 and gives a smaller constant. If one residual row is heavy, its promoted two-row determinant is `>Z/4`, and terminal estimate (12) is smaller. Consequently (19) is unconditional.

This is a half-potential theorem, not a rank-two bounded-density assertion.

## 4. Assembly under `s_9(A)>=1`

Retain the baseline's `eta=1/100`, `kappa=1/80^2`.

### No pivot

The audited baseline structural proposition with order `k=3` requires exactly `4k-3=9` unit-scale singular values and gives

`V_3(A)>=kappa^3`.

The fair coordinate cut produces a literal cross block with

`E_3(M)>=4^-3 kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^-1/2=160`.

By (17),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488...<2400`.                                    (20)

### Scalar pivot

If `|A_hh|>=eta`, the audited Schur count loses at most one direction, including when the ambient matrix is singular. Thus its Schur complement has at least eight eigenvalues of modulus at least one.

If that Schur complement has an `eta`-pivot, re-read the three cases in the baseline proof of `prop:pivot-H`. The largest explicit truncated half-potential bound is the scalar subcase

`H(R)<=eta^-1/2(8+3L_0)
     =200+120 log16`,                                           (21)

while the definite and indefinite pair subcases are smaller. Adding the tail `|R-a|>1`, where the kernel is at most one, gives

`sup_a E|R-a|^-1/2 <=201+120 log16`.                            (22)

If the Schur complement has no pivot, eight surviving directions imply in particular `s_5>=1`. The baseline order-two structural proposition gives `V_2>=kappa^2`, and a fair cut gives

`E_2>=4^-2 kappa^2`,

so

`E_2^-1/8<=sqrt(160)`.

Equation (19) then yields

`sup_a E|R-a|^-1/2 <=C_2 sqrt(160)
 =152.99191115498...<153`,                                      (23)

which is below (22). The outer scalar-square profile contributes `eta^-1/2=10`, hence

`||p_Q||_infinity <=2010+1200 log16
 =5337.106466687737...<5338`.                                   (24)

### Two-coordinate pivot

A definite pair of determinant magnitude at least `eta` has conditional density at most

`pi/sqrt(eta)=10pi<32`.

For an indefinite pair, the Schur lemma loses at most two directions. Starting from nine leaves at least seven unit-scale directions, so its Schur complement has operator norm at least one. The baseline hyperbolic envelope plus quarter-power/logarithmic-potential proof therefore applies verbatim and stays below `251`.

The no-pivot, scalar, definite-pair, and indefinite-pair cases exhaust the normalized theorem. The largest branch is (24).

## 5. Scaling and dependency map

For general `K,s`, set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`.

The coordinates of `Y` have density cap one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Therefore

`||p_Q||_infinity <=(2010+1200 log16)K^2/s <5338K^2/s`.

Closed dependencies:

1. Baseline Fourier inversion/Plancherel, Riesz half-potential, product-projection and scalar Fourier-power lemmas.
2. New grouped compiler Claim 1, with the multidimensional Plancherel extension and rough-law Fatou step explicitly supplied above.
3. Exact Gram–Schmidt promotion identities, yielding unconditional `E_3` density and `E_2` half-potential receivers.
4. Baseline disjoint-volume interpolation at orders 3 and 2, plus random coordinate cuts.
5. Baseline scalar-square, definite-pair, hyperbolic-pair, quarter-concentration and Schur-count lemmas.
6. Original-coordinate conditioning only; arbitrary affine terms and all remaining spectrum are retained.

No Gaussian, log-concave, bounded-support, diagonal, exact-rank, leverage, or post-rotation-independence hypothesis is introduced.

## 6. B11 Schur barrier: why this review does not claim eight

The sibling B11 baseline audit gives exact examples showing the losses one and two in the Schur lemma are sharp even for arbitrarily small/near-singular invertible pivots, including indefinite pairs. Consequently a further threshold reduction cannot be obtained by merely charging the Schur loss to the number of large eigenvalues of the pivot.

More importantly, the nine count in this replacement theorem is already forced in the **no-pivot** branch by the current structural proposition: order-three crossing volume uses sampled seed size up to `r=2`, and the present nonsymmetric interpolation argument needs `4r+1=9` large singular values. Schur complementation is not involved there. Thus this B11 review rigorously supports the complete nine-eigenvalue theorem but supplies no complete eight-eigenvalue replacement proof.

The unrestricted three-eigenvalue QFORM conjecture remains open.
