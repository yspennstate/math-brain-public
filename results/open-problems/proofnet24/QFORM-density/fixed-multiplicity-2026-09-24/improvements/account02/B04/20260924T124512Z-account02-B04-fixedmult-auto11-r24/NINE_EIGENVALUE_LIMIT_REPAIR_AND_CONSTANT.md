# QFORM-NINE-DIRECTION-GROUPED-COMPILER-REVIEW-v1

Status: **independent derivation/review of a new nine-eigenvalue candidate, with an explicit rough-law limiting repair and a sharpened constant; not yet independently validated under the owner's two-review gate.**

Pinned baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Peer candidate reviewed: account03/B04 `20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`.

The unrestricted three-eigenvalue conjecture remains open.

## Candidate theorem after this review

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K<infinity`. Let `A=A^T`, `b` and `c` be arbitrary. If

` s_9(A)>=s>0,`

then the law of

`Q=X^TAX+b^TX+c`

has an essentially bounded density satisfying

`||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s.`

Global continuity is not asserted. The no-pivot grouped-Fourier branch is continuous; pivot branches are used only as measure domination.

The rest of this note gives the missing explicit limit passage in the grouped compiler and records the closed dependency map I independently checked.

## 1. Grouped product-Fourier compiler: exact rough-law proof

Use disjoint original-coordinate sets `H,I,J`. Let `X_H` be independent of `X'=(X_I,X_J)`. Let `W=L_H X_H` be a `k`-dimensional orthogonal projection of `X_H` with density bounded by `M_H`. Consider

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,

where `F` is arbitrary measurable, `R` is an arbitrary quadratic polynomial, and the restriction `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`. Write `A_R[I,J]` for the physical cross block of the quadratic part of `R`, and let

`C=A_R[I,J](I-Pi_row(M_J))`

in coefficient space. For an integer `ell>=1`, put

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,

`w_T=det(C_T C_T^T)/Z_ell`,

`alpha_i=sum_{T contains i} w_T`.

Assume all `alpha_i<=1/2`, and put `d=k+ell`.

Then

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^{-d/2})`,

with

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
             (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`      (1)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d))
   e^((k+2ell)/(2d)) (ell^ell/ell!)^(1/(2d))
   S^(-1/d) Z_ell^(-1/(2d)).`                                  (2)

### 1.1 First Plancherel step

Push the complex measure `e^{itF}dP_H` through `W`. Because it is dominated in variation by the ordinary law of `W`, it has a density `a_t` satisfying

`|a_t(w)|<=p_W(w)`, hence `||a_t||_2^2<=M_H`.

Push `e^{itR}dP_{X'}` through `y=M X'`; call the complex density `mu_t`. Then

`phi_Q(t)=int hat(a_t)(2t(y+beta)) mu_t(y)dy`.

Cauchy--Schwarz and the manuscript Plancherel convention give

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.                 (3)

Indeed, after `xi=2t(y+beta)`, the Fourier `L^2` integral contributes `(2pi)^k/(2|t|)^k=(pi/|t|)^k`.

### 1.2 The rough `L^2` pushforward step, with the limit made explicit

Split `M=(M_I,M_J)`. Condition on the original physical variables `X_I=x`. Translation by `M_Ix` is unitary in `L^2`, so Jensen for the mixture gives

`||mu_t||_2^2 <= E_x ||nu_{t,x}||_2^2`,                        (4)

where `nu_{t,x}` is the complex pushforward through `M_JX_J` of the conditional phase. Since `M_J` has full row rank, its ordinary pushforward has a Lebesgue density; the complex measure is dominated by it.

Do not assume `nu_{t,x}` is already in `L^2`. Let `rho_epsilon` be a nonnegative compactly supported approximate identity on `R^k` and set `nu_{epsilon,x}=nu_{t,x}*rho_epsilon`. Then `nu_{epsilon,x}` is bounded and square-integrable on the relevant finite calculation, and expansion of its square is justified by Fubini:

`||nu_{epsilon,x}||_2^2
 = E_{X_J,X'_J}[kappa_epsilon(M_JD)
    exp(it(R_x(X_J)-R_x(X'_J)))],`                              (5)

where `D=X_J-X'_J` and

`kappa_epsilon=rho_epsilon*tilde(rho_epsilon)`

is a probability density on `R^k`.

Now average (5) in `x=X_I` **before taking absolute values**. Pure `I` terms cancel, pure `J` terms retain modulus one, and the `I-J` cross phase is linear in each independent physical `X_i`. Thus

`E_x exp(2it sum_i X_i <a_i,D>)
  = prod_i psi_i(2t<a_i,D>),`

where `a_i` are the physical rows of `A_R[I,J]` and each `psi_i` is the characteristic function of a cap-one one-dimensional law. Therefore

`E_x ||nu_{epsilon,x}||_2^2
 <= E_D[kappa_epsilon(M_JD)
          prod_i |psi_i(2t<a_i,D>)|].`                           (6)

The right side will be bounded uniformly in `epsilon`.

To remove the smoothing, use Plancherel/Fourier Fatou rather than an unproved strong convergence assertion. Since `hat rho_epsilon(xi)->1` and `|hat rho_epsilon|<=1`,

`||nu_{t,x}||_2^2
 <= liminf_{epsilon->0} ||nu_{t,x}*rho_epsilon||_2^2`            (7)

with the left side interpreted as `+infinity` if necessary. Fatou in `x` and the uniform estimate from (6) then imply the required finite bound on the unsmoothed `E_x||nu_{t,x}||_2^2`, hence on `||mu_t||_2^2`. This closes the rough-density endpoint without moments, smoothness, bounded support, or conditional density caps inferred from unconditional marginals.

### 1.3 Weighted physical-minor aggregation

Decompose each physical row

`a_i=c_i+lambda_i M_J`, with `c_i` perpendicular to `row(M_J)`.

Because

`prod_i |psi_i| = prod_T [prod_{i in T}|psi_i|^(1/alpha_i)]^(w_T),`

generalized Holder bounds (6) by the weighted geometric mean of the corresponding `T`-integrals.

For a fixed `T`, the physical linear map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T)`.

The manuscript product-projection lemma, followed only by deterministic SVD scaling, bounds its density by

`e^(d/2)/[S sqrt(det(C_T C_T^T))]`.

The `kappa_epsilon` coordinate integrates to one. Since `alpha_i<=1/2`, the manuscript scalar Fourier-power lemma at `p=1/alpha_i>=2` gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <= pi sqrt(2e alpha_i)/|t|`.                                   (8)

Thus the `T`-integral is bounded by

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 prod_{i in T} sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))].`                                    (9)

For `w_T=det/Z_ell`, the weighted determinant product is

`Z_ell^(-1/2) exp(H(w)/2)`.

The marginal terms contribute

`exp((1/2)sum_i alpha_i log alpha_i)`.

To close them, sample `T~w` and then order its `ell` members uniformly. The ordered tuple has entropy `H(w)+log(ell!)`. Subadditivity, with each position having averaged marginal distribution `alpha_i/ell`, gives

`H(w)+log(ell!) <= -sum_i alpha_i log(alpha_i/ell)
                 = -sum_i alpha_i log alpha_i + ell log ell.`   (10)

Equations (3),(6),(9),(10), followed by the smoothing limit above, give (1). Integration of `min(1,K|t|^{-d/2})` gives (2).

This proof uses only original-coordinate product independence. Coefficient-space orthogonal projections enter deterministic Gram determinants and Jacobians only.

## 2. Marginal-free third crossing volume

For a literal physical cross block with

`Z=E_3(M)=e_3(MM^T)>0`,

let `J_i` be the sum of the three-row Gram determinants containing physical row `i`. Then `sum_i J_i=3Z`.

If all canonical marginals `J_i/Z<=1/2`, (2) at `(k,ell,d)=(0,3,3)` gives

`||p_Q||_infinity <= C_3 Z^(-1/6)`,

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                 (11)

If some `J_i>Z/2`, keep that literal physical row as a hub. Orthogonal Gram--Schmidt in coefficient space gives the exact identity

`J_i=||w_i||^2 e_2(CC^T)`.                                      (12)

If the residual `E_2` canonical marginals are diffuse, (2) at `(1,2,3)` pays the branch. If a residual physical row `j` is heavy, promote it too. Then

`H_ij=det(PP^T)||C_2||_F^2 > J_i/2 > Z/4`.                      (13)

If the residual one-volume is diffuse, use `(2,1,3)`. Otherwise a heavy third physical row has literal Gram determinant `>H_ij/2>Z/8`, and the exact rank-three Plancherel receiver gives the density bound. The worst constant among all four branches is (11), so

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.                        (14)

## 3. Marginal-free second crossing volume and half potential

For `Z=E_2(M)>0`, the same promotion chain with at most one hub gives

`sup_a E|Q-a|^(-1/2) <= C_2 Z^(-1/8)`,

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.                     (15)

In the diffuse branch, the grouped compiler gives

`|phi(t)| <= min(1,L/|t|)`,

`L=pi e 2^(3/4)Z^(-1/4)`.

The manuscript Riesz inequality and

`int_R |t|^(-1/2)min(1,L/|t|)dt=8 sqrt(L)`

give (15). Heavy-row promotion gives smaller constants; a final heavy residual row is paid by the exact rank-two half-potential receiver. This is a half-potential theorem, not a rank-two density theorem.

## 4. Assembly under nine large singular values

Normalize `K=s=1`, and retain the baseline `eta=1/100`, `kappa=1/80^2`.

### No pivot

The audited baseline spectral-to-volume proposition at order three uses exactly `4*3-3=9` large singular values:

`V_3(A)>=kappa^3`.

A fair physical cut gives `E_3(M)>=4^(-3)kappa^3`, so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

By (14),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488...<2400`.                                    (16)

### Scalar pivot

An outer scalar pivot leaves at least eight unit-scale Schur eigenvalues. If that Schur complement has a pivot, the baseline pivot-half-potential proof gives, without rounding,

`H(R)<=200+120 log16`.

The tail outside distance one costs at most one, so

`sup_a E|R-a|^(-1/2)<=201+120 log16`.                            (17)

If the Schur complement has no pivot, it has in particular `s_5>=1`. Apply the audited baseline spectral-to-volume proposition at order two and a random cut, then (15):

`sup_a E|R-a|^(-1/2)
 <=C_2 sqrt(160)
 =152.99191115498...`,                                           (18)

which is below (17). The outer square profile contributes `eta^(-1/2)=10`, hence

`||p_Q||_infinity
 <=2010+1200 log16
 =5337.106466687737...`.                                        (19)

### Pair pivots

A definite pair has conditional density at most `pi/sqrt(eta)=10pi<32`. An indefinite pair loses only two Schur directions; seven remain, so the baseline logarithmic-critical-value argument has much more than its one surviving spectral direction and remains below `251`.

Thus (19) is the largest normalized branch.

### Scaling

With `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`,

one has `Q=(s/K^2)Qtilde`, giving

`||p_Q||_infinity <=(2010+1200 log16)K^2/s<5338K^2/s`            (20)

under `s_9(A)>=s`.

## 5. Dependency map and review state

The nine-direction proof uses only these audited baseline ingredients:

1. Fourier/Plancherel and Riesz identities;
2. geometric rank-one Brascamp--Lieb, including its heat-flow limits;
3. product-projection density bound;
4. scalar integrated Fourier-power estimate;
5. Schur spectral count;
6. scalar-square, definite-pair, hyperbolic-pair and quarter-power/logarithmic pivot estimates;
7. ordered disjoint-volume sampling/completion and the no-pivot spectral-to-volume proposition, only at orders two and three;
8. random physical-coordinate cut.

New ingredients are exactly Sections 1--3 above. No Gaussian, log-concavity, bounded support, moment, exact-rank, diagonal, leverage, or post-rotation-independence hypothesis is introduced.

Review state: the mathematical argument in this note is **PASS in account02/B04's independent derivation**, but the owner requires two genuinely separate complete reviews before a lower-threshold candidate may be called independently validated. This artifact is therefore a review/improvement input, not a release certificate.

## 6. Current barrier below nine

The order-three no-pivot spectral-to-volume proof can sample a bad ratio at seed order `r=2`. Its present global correction rank is `<=3r=6` while the seed-complement correction rank is `<=r=2`; the diagonal-dominance contradiction needs three large diagonal entries outside the seed, leading to the existing `4r+1=9` count. I do not have a complete eight-direction replacement for that structural step.

This is a proof-route barrier only. It is not a counterexample to an eight-eigenvalue density theorem, and no claim below nine is made.
