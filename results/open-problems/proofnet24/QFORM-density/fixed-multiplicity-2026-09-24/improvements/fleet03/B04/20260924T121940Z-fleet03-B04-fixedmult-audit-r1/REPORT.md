SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T12:19:40Z.
attacking: lower the audited fixed-multiplicity theorem by replacing the order-five no-pivot density endpoint with a self-contained marginal-free order-three product-Fourier compiler, while retaining the manuscript's original-coordinate pivot analysis.

# Candidate improvement: seventeen eigenvalues -> nine

Status: **NEW CANDIDATE IMPROVEMENT, PENDING INDEPENDENT END-TO-END REVIEW**.

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.

The baseline 17-eigenvalue proof was independently audited in the sibling `audits/fleet03/B04/.../REPORT.md`. The argument below does not edit or overwrite that baseline. It uses the baseline's proved geometric Brascamp--Lieb theorem, product-projection density lemma, scalar Fourier-power estimate, Fourier/Riesz inversion, Schur spectral count, pivot estimates, disjoint-volume interpolation proposition, and random coordinate cut. The only new analytic ingredient is proved here from those baseline lemmas.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K<infinity`. Let `A=A^T`, `b` and `c` be arbitrary. If

` s_9(A) >= s > 0,`

then

`Q=X^T A X+b^T X+c`

has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 6010 K^2/s.`

The global continuity conclusion is **not** claimed. The no-pivot branch below has a continuous `C_0` density, but the scalar/pair pivot branches are used only through measure domination.

The proof is first given for `K=s=1`, with the manuscript's parameters

`eta=1/100`, `kappa=1/80^2`.

## 1. A self-contained grouped product-Fourier compiler

The purpose of this lemma is to aggregate physical crossing volume before any reciprocal local minor is paid.

Let `H,I,J` be disjoint sets of original coordinates. Let `X_H` be independent of the light product vector `X'=(X_I,X_J)`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`. Consider

`Q=F(X_H)+2 <W, M X'+beta>+R(X')`,

where `F` is arbitrary measurable, `R` is an arbitrary quadratic polynomial, the restriction `M_J` has row rank `k`, and `S` is the product of its nonzero singular values. Write

`C=(A_R)_[I,J](I-Pi_row(M_J))`.

For `ell>=1`, put

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,

let `w_T=det(C_T C_T^T)/Z_ell`, and let

`alpha_i=P_w(i in T)`.

Assume `alpha_i<=1/2` for every physical row. Set `d=k+ell`.

### Lemma 1.1 — weighted-subset estimate with manuscript constants

For `t!=0`,

`|phi_Q(t)| <= min(1, K_{k,ell}|t|^{-d/2})`,

where

`K_{k,ell}
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4)
   S^(-1/2) Z_ell^(-1/4).`                                      (1.1)

If `d>2`, then

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`           (1.2)

#### Proof

Push the complex measure `exp(itF)dP_H` to `W`; its density `a_t` obeys `|a_t|<=p_W` and hence `||a_t||_2^2<=M_H`. Plancherel with the manuscript Fourier convention gives

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.              (1.3)

Push `exp(itR)dP_{X'}` to the linear variable `M X'`, giving a complex density `mu_t`. Cauchy--Schwarz gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                   (1.4)

To bound the last norm, convolve `mu_t` with a compactly supported approximate identity and expand the square with an independent copy of `X_J`. Pure `I` terms cancel and pure `J` terms have modulus one. If `D=X_J-X'_J`, its coordinates remain independent and each has density at most one. One obtains, uniformly in the approximate identity,

`E[kappa(M_J D) prod_i |psi_i(2t <a_i,D>)|]`,                   (1.5)

where `kappa` is a probability density and each `psi_i` is the characteristic function of a cap-one one-dimensional law.

For a subset `T` of size `ell`, write `a_i=c_i+lambda_i M_J` with `c_i` perpendicular to `row(M_J)`. Weighted Holder with weights `w_T` reduces (1.5) to the geometric mean of integrals containing powers `1/alpha_i`. The linear map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T)`.

The baseline product-projection lemma therefore bounds its density by

`e^(d/2)/(S sqrt(det(C_T C_T^T)))`.                              (1.6)

For `alpha_i<=1/2`, the baseline scalar Fourier-power lemma at `p=1/alpha_i>=2` gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|`.                                    (1.7)

Thus the `T`-integral is at most

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_{i in T}sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))]`.                                    (1.8)

The weighted geometric mean of the determinant factors is

`Z_ell^(-1/2) exp(H(w)/2)`,

and the marginal factors contribute

`exp((1/2)sum_i alpha_i log alpha_i)`.

For completeness, order a random `ell`-subset uniformly after it is sampled. Entropy subadditivity gives the sharp dimension-free inequality

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.        (1.9)

Combining (1.8)--(1.9), passing through the `L^2` approximate-identity limit, and then using (1.4) proves (1.1). Integrating `min(1,K|t|^{-d/2})` gives

`int_R min(1,K|t|^{-d/2})dt = 2d/(d-2) K^(2/d)`,

and Fourier inversion gives (1.2). No random-variable rotation is used; rotations appear only in deterministic projection/Jacobian calculations. QED.

### Terminal exact-rank crossing bounds

The same complex-pushforward/Plancherel argument without a residual projected block gives, for `r` physical original coordinates crossing a product bank through a rank-`r` block `P`,

`|phi(t)| <= min(1, pi^(r/2)e^(r/4)
 [det(PP^T)]^(-1/4)|t|^(-r/2)).`                                (1.10)

Here the physical `r`-coordinate density cap is one, while the opposite `r`-dimensional projection has cap at most `e^(r/2)` by the baseline projection theorem. Hence

`r=3:  ||p||_infinity <=3 sqrt(e) [det(PP^T)]^(-1/6),`           (1.11)

and, using the baseline Riesz formula,

`r=2:  sup_a E|Q-a|^(-1/2)
       <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8).`                    (1.12)

All same-bank and affine phases are retained in the complex pushforwards.

## 2. Marginal-free third crossing volume gives a density

Let `M` be any literal original-coordinate cross block and put

`Z=E_3(M):=e_3(MM^T)>0`.

For a physical row `i`, let `J_i` be the sum of the three-row Gram determinants containing `i`. Then

`sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply Lemma 1.1 with `(k,ell,d)=(0,3,3)` to obtain

`||p_Q||_infinity <= C_3 Z^(-1/6)`,                              (2.1)

where

`C_3=3 sqrt(2)e(9/2)^(1/6)
    =14.818337662843...`.                                        (2.2)

If instead `J_i>Z/2`, keep the literal row `i` as one hub. Let `w` be that row and project every other row orthogonally off `w`, giving `C`. Gram--Schmidt gives the exact aggregate identity

`J_i=||w||^2 e_2(CC^T)`.                                        (2.3)

If the canonical `E_2(C)` row marginals are all at most `1/2`, Lemma 1.1 with `(k,ell,d)=(1,2,3)` gives

`||p_Q||_infinity
 <=3 sqrt(2)e^(5/6) J_i^(-1/6)
 <10.958 Z^(-1/6)`.                                              (2.4)

Otherwise promote a residual physical row `j` of marginal greater than `1/2`. Writing `P` for the two promoted rows and `C_2` for the remaining rows projected off `row(P)`, another exact Gram--Schmidt identity gives

`H_ij=det(PP^T)||C_2||_F^2>J_i/2>Z/4`.                           (2.5)

If all one-volume marginals of `C_2` are at most `1/2`, Lemma 1.1 at `(k,ell,d)=(2,1,3)` gives

`||p_Q||_infinity <8.264 Z^(-1/6)`.                              (2.6)

If one residual row has one-volume marginal greater than `1/2`, the three promoted physical rows have

`det(P_3P_3^T)>H_ij/2>Z/8`,                                     (2.7)

and (1.11) gives

`||p_Q||_infinity <3 sqrt(2e) Z^(-1/6)<7 Z^(-1/6)`.              (2.8)

Therefore all branches satisfy the single marginal-free estimate

`boxed: ||p_Q||_infinity <= C_3 E_3(M)^(-1/6),
        C_3=3 sqrt(2)e(9/2)^(1/6)<14.819.`                       (2.9)

Every branch has an integrable characteristic-function envelope, so this particular fixed-cross-block conclusion has a continuous `C_0` density.

## 3. Marginal-free second crossing volume gives a half potential

For a literal cross block `M` put

`Z=E_2(M):=e_2(MM^T)>0`.

If all canonical `E_2` row marginals are at most `1/2`, Lemma 1.1 at `(k,ell,d)=(0,2,2)` yields

`|phi(t)| <= min(1, pi e 2^(3/4) Z^(-1/4)|t|^(-1)).`             (3.1)

Using the baseline Riesz inequality and

`int_R min(1,L/|t|)|t|^(-1/2)dt=8 sqrt(L)`,                     (3.2)

we get

`sup_a E|Q-a|^(-1/2)
 <= C_2 Z^(-1/8),
 C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.                      (3.3)

If a physical row `i` carries more than half the `E_2` mass, let `K_i>Z/2` be its incident mass. Projecting the other rows off `w=m_i` gives

`K_i=||w||^2||C||_F^2`.                                         (3.4)

If every one-volume residual marginal is at most `1/2`, Lemma 1.1 at `(k,ell,d)=(1,1,2)` and (3.2) give

`sup_a E|Q-a|^(-1/2)
 <=8*2^(-3/8)e^(3/8) K_i^(-1/8)
 <9.79 Z^(-1/8)`.                                                (3.5)

If a residual row has marginal greater than `1/2`, the corresponding physical two-row Gram determinant obeys

`D>K_i/2>Z/4`,                                                   (3.6)

and the exact-rank-two bound (1.12) gives less than `8.64 Z^(-1/8)`. Consequently

`boxed: sup_a E|Q-a|^(-1/2)
        <= C_2 E_2(M)^(-1/8),
        C_2=8 sqrt(e)2^(-1/8)<12.096.`                           (3.7)

This is a fractional-potential conclusion, not a rank-two bounded-density assertion.

## 4. Nine large eigenvalues suffice

Assume now `K=s=1` and `s_9(A)>=1`.

### 4.1 No coordinate pivot

If `A` has no `eta`-pivot, apply the baseline spectral-to-volume proposition with `k=3`. Since `4k-3=9`,

`V_3(A)>=kappa^3`.                                               (4.1)

The baseline random coordinate cut gives a literal cross block `M` with

`E_3(M)>=4^(-3)kappa^3`,

hence

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.                             (4.2)

By (2.9),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488...<2400.`                                     (4.3)

This branch has a continuous `C_0` density.

### 4.2 A scalar pivot

Suppose `|A_hh|>=eta`. Complete the square in the original coordinate `X_h`. The baseline Schur spectral lemma leaves at least eight eigenvalues of modulus at least one in the Schur complement `S`.

If `S` has an `eta`-pivot, the audited baseline pivot proposition applies (it only requires two surviving large eigenvalues) and gives truncated half potential at most `600`; adding the tail `|R-a|>1` costs at most one. Thus the full half potential is at most `601`.

If `S` has no `eta`-pivot, then in particular `s_5(S)>=1`. Apply the baseline spectral-to-volume proposition with `k=2`, then the random cut:

`E_2(M_S)>=4^(-2)kappa^2`.                                      (4.4)

Equation (3.7) gives

`sup_a E|R-a|^(-1/2)
 <= C_2 (4^(-2)kappa^2)^(-1/8)
 =C_2 sqrt(160)
 =152.99191115498...<153.`                                      (4.5)

Therefore in either subcase the full Schur half potential is at most `601`. The baseline scalar-square profile now gives

`||p_Q||_infinity <=eta^(-1/2)*601=6010`.                        (4.6)

### 4.3 A two-coordinate pivot

If there is no chosen scalar pivot but a definite principal two-coordinate pivot has determinant magnitude at least `eta`, the audited baseline definite-pair lemma gives

`||p_Q||_infinity <=pi/sqrt(eta)=10pi<32`.                       (4.7)

If the pair is indefinite, its Schur complement retains at least seven eigenvalues of modulus at least one, hence operator norm at least one. The audited baseline hyperbolic-pair plus quarter-power/logarithmic-potential calculation applies verbatim and gives the same bound as in the manuscript,

`||p_Q||_infinity<251`.                                         (4.8)

The scalar, definite-pair, indefinite-pair, and no-pivot cases exhaust the normalized problem. The maximum is (4.6), proving

`||p_Q||_infinity<=6010`.                                       (4.9)

## 5. Scaling

For general coordinate cap `K` and spectral scale `s`, set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

The coordinates of `Y` have densities at most one, `s_9(A/s)>=1`, and

`Q=(s/K^2)Qtilde`.

Therefore

`boxed: ||p_Q||_infinity<=6010 K^2/s.`                           (5.1)

## 6. What is and is not improved

This lowers the written fixed-multiplicity candidate from 17 to **9** without Gaussian, log-concave, moment, bounded-support, connected-support, diagonal, exact-rank, leverage, or post-rotation-independence assumptions. Arbitrary affine terms and all remaining spectrum are retained.

The mechanism cannot lower the **no-pivot** spectral count below nine merely by reusing the manuscript's current interpolation rank estimate: order-three crossing volume uses `k=3`, and its worst sampled seed has `r=2`, where the existing argument needs `m>=4r+1=9`. This is a limitation of this proof route, not a claim that eight or fewer eigenvalues are impossible.

The unrestricted three-eigenvalue conjecture remains OPEN. The candidate nine-eigenvalue theorem requires independent end-to-end review before it should replace the pinned baseline. In particular, reviewers should reconstruct Lemma 1.1, the physical-row promotion identities (2.3), (2.5), (2.7), and the passage from the manuscript's structural proposition to (4.1)--(4.5).

Execution status: `WITHOUT_VERIFIED_BRAIN`. No scheduler state, task identity, notification/email setting, public release, paid API/model, permission, or cross-account authentication was changed.
