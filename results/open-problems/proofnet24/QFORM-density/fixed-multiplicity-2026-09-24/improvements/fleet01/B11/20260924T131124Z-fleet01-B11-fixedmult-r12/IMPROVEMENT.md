# fleet01/B11 r12 — independent nine-eigenvalue reconstruction and sharper constant

Run: `20260924T131124Z-fleet01-B11-fixedmult-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **COMPLETE 9-EIGENVALUE REPLACEMENT PROOF IN THIS WORKER; 8-EIGENVALUE THEOREM NOT CLOSED**.

## 1. The improved theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

` s_9(A) >= s > 0, `

then

` Q=X^T A X+b^T X+c `

has an essentially bounded density and

` ||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s. `

No Gaussian, log-concavity, moment, bounded-support, connected-support, iid, diagonal-basis, exact-rank, leverage, or post-rotation-independence assumption is used. The theorem is sign-independent and retains all remaining spectrum and arbitrary affine terms.

Global continuity is **not** asserted. The no-pivot branch below has an integrable characteristic function and hence a continuous `C_0` density; the scalar/pair pivot branches are used only through domination of measures.

### Review provenance

A source-matched first proof of the 9-direction mechanism is fleet03/B04:

`improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`, blob `054facef834d29927713c5d42a1f09a541c5644b`.

A genuinely separate fleet01/B16 reconstruction reported PASS at commit

`54ec2a651d854563f8db0d92c4c3426f76551786`, path

`improvements/fleet01/B16/20260924T124038Z-r11/REPORT.md`.

The proof below is this B11 worker's complete reconstruction, including a missing-explicit-sentence check in the light-bank `L^2` passage and independent constant bookkeeping. Thus there are now two distinct worker PASS reconstructions of the 9-direction replacement (B16 and B11) in addition to the author-side B04 report. This factual review count does not self-award an owner release/priority certificate.

Throughout Sections 2–7 normalize `K=s=1` and retain the baseline parameters

` eta=1/100,  kappa=1/80^2=1/6400. `

The baseline 17-direction manuscript has been independently audited in this run and all reused lemmas below are PASS.

## 2. Grouped product-Fourier compiler

This is the only genuinely new analytic engine needed to move the density endpoint from crossing order five to crossing order three.

Let `H,I,J` be disjoint sets of original coordinates. Let `X_H` be independent of `X'=(X_I,X_J)`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`. Consider

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,

where `F` is arbitrary measurable and finite a.s., `R` is an arbitrary quadratic/affine polynomial, and the restriction `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`.

After removing from the `I x J` quadratic crossing in `R` the row-space component already represented by `M_J`, write the residual physical rows as a matrix `C`. For an integer `ell>=1`, put

` Z_ell = sum_{|T|=ell} det(C_T C_T^T) > 0, `

where the sum is over physical row subsets. Define probability weights

` w_T=det(C_T C_T^T)/Z_ell `

and inclusion marginals

` alpha_i=sum_{T contains i} w_T. `

Assume every `alpha_i<=1/2` and put `d=k+ell`.

### Compiler theorem

For `t!=0`,

` |phi_Q(t)| <= min(1,K_{k,ell}|t|^{-d/2}), `

where

`K_{k,ell}
 = M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
   (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`              (2.1)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`       (2.2)

### Proof, with the light-bank limiting step made explicit

Push the complex measure `e^{itF}dP_H` to `W`. It has a complex density `a_t` with

` |a_t|<=p_W,  ||a_t||_2^2<=M_H. `

By Plancherel and the change `xi=2t(l+beta)`,

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k.`         (2.3)

Push `e^{itR}dP_{X'}` to `M X'`; since `M_J` has full row rank, conditioning on `X_I` and using the baseline product-projection theorem supplies an absolutely continuous complex pushforward. Denote its density by `mu_t`. Cauchy--Schwarz gives

` |phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2. `              (2.4)

It remains to bound `||mu_t||_2`. This is the point where dependence must not be hidden.

Condition on the actual original-coordinate vector `X_I=x`. Translation by `M_Ix` does not change an `L^2` norm, and the pure `I` phase is modulus one. Regularize the conditional phase-weighted pushforward of `X_J` by a compact approximate identity. Expanding its squared `L^2` norm introduces only an independent copy `X'_J`; put `D=X_J-X'_J`. Pure `J` phases survive only with modulus one. Now average in the original independent `X_i`, `i in I`. Their linear cross phases give scalar characteristic-function factors. Jensen in the Hilbert space `L^2` gives

`|| E_{X_I} nu_{X_I} ||_2^2 <= E_{X_I}||nu_{X_I}||_2^2`,

so no copy of `X_I` and no conditional density cap is invented. The resulting mollified bound has the form

`E[ KERNEL(M_JD) product_i |psi_i(2t<a_i,D>)| ]`,             (2.5)

where `KERNEL` is a probability density and the `psi_i` are characteristic functions of cap-one original coordinate laws. The bound is uniform in the mollifier. Weak compactness in `L^2` and lower semicontinuity pass it to `mu_t` itself. This closes the limiting sentence compressed in the original B04 report.

Write

` a_i=c_i+lambda_i M_J `

with `c_i` orthogonal to `row(M_J)`. Weighted Holder with the subset weights `w_T` turns (2.5) into the geometric mean of integrals containing exponents `1/alpha_i`. For one `ell`-subset `T`, the linear map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant

` S^2 det(C_T C_T^T). `                                      (2.6)

The baseline product-projection lemma, followed by deterministic scaling, therefore bounds the density of this image by

` e^(d/2)/(S sqrt(det(C_T C_T^T))). `                          (2.7)

Because `alpha_i<=1/2`, the baseline scalar Fourier-power lemma applies at `p=1/alpha_i>=2`. Including the scale `2t`,

`int |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`                                  (2.8)

Hence the `T`-integral is at most

`e^(d/2) [pi sqrt(2e)/|t|]^ell
 product_{i in T}sqrt(alpha_i)
 /[S sqrt(det(C_T C_T^T))].`                                  (2.9)

The determinant geometric mean equals

`Z_ell^(-1/2) exp(H(w)/2)`,

and the marginal factors contribute

`exp((1/2) sum_i alpha_i log alpha_i)`.

To bound them, sample `T` with law `w` and then uniformly order its `ell` elements. Entropy subadditivity for the ordered tuple gives

`H(w)+log(ell!)
 <= ell log ell - sum_i alpha_i log alpha_i`,

or

`H(w)+sum_i alpha_i log alpha_i
 <= ell log ell-log(ell!).`                                    (2.10)

Combining (2.4), (2.9), and (2.10), then taking the square root, proves (2.1). For `d>2`, direct integration gives

`int_R min(1,K|t|^(-d/2))dt=2d/(d-2) K^(2/d)`.

The factor `pi` arising from `K_{k,ell}^{2/d}` cancels the `1/(2pi)` Fourier inversion normalization, yielding (2.2). No random-variable rotation appears anywhere.

## 3. Exact promoted-row terminals

If the residual projected block has vanished after promoting `r` literal physical rows, the same complex-pushforward/Plancherel argument gives for their rank-`r` cross block `P`

`|phi(t)| <= min(1, pi^(r/2)e^(r/4)
 [det(PP^T)]^(-1/4)|t|^(-r/2)).`                              (3.1)

Therefore

`r=3: ||p||_infinity <=3 sqrt(e)[det(PP^T)]^(-1/6),`          (3.2)

and, by the baseline Riesz formula,

`r=2: sup_a E|Q-a|^(-1/2)
 <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8).`                        (3.3)

All same-bank quadratic and affine terms remain in complex pushforwards; they are not discarded as independent remainders.

## 4. Marginal-free third crossing volume gives a density

For a literal original-coordinate cross block `M`, set

`Z=E_3(M)=e_3(MM^T)>0`.

For physical row `i`, let `J_i` be the sum of three-row Gram determinants containing `i`; then `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply the compiler with `(k,ell,d)=(0,3,3)`. This gives

`||p_Q||_infinity <= C_3 Z^(-1/6),`

where

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`.                (4.1)

If some `J_i>Z/2`, promote the literal row `w=m_i` and project every other physical row orthogonally off `w`, obtaining `C`. Gram--Schmidt gives the exact aggregate identity

` J_i=||w||^2 e_2(CC^T). `                                    (4.2)

If the normalized `E_2(C)` row marginals are all at most one half, apply the compiler at `(1,2,3)`, obtaining a constant `<10.958` times `Z^-1/6`.

Otherwise promote a heavy residual row `j`. With promoted two-row matrix `P` and remaining residual `C_2`, exact Gram--Schmidt gives

`H_ij=det(PP^T)||C_2||_F^2>J_i/2>Z/4.`                         (4.3)

If the residual one-volume marginals are all at most one half, use `(2,1,3)`, giving `<8.264 Z^-1/6`. If one residual row is heavy, promote it and obtain

`det(P_3P_3^T)>H_ij/2>Z/8`;                                   (4.4)

then (3.2) gives `<7 Z^-1/6`.

Thus every branch obeys the single marginal-free theorem

` ||p_Q||_infinity <= C_3 E_3(M)^(-1/6). `                     (4.5)

Every branch above has an integrable characteristic-function majorant, hence this fixed-cross-block conclusion has a continuous `C_0` density.

## 5. Marginal-free second crossing volume gives a half potential

For a literal cross block set

`Z=E_2(M)=e_2(MM^T)>0`.

If all normalized row marginals are at most one half, the compiler at `(0,2,2)` gives

`|phi(t)|<=min(1, pi e 2^(3/4) Z^(-1/4)|t|^-1).`              (5.1)

Using the baseline Riesz inequality and

`int_R min(1,L/|t|)|t|^-1/2 dt=8 sqrt(L)`

gives

`sup_a E|Q-a|^-1/2 <= C_2 Z^-1/8,`

`C_2=8 sqrt(e)2^-1/8=12.095072570796...`.                      (5.2)

If row `i` carries more than half of the second-volume mass, project the remaining rows off `w=m_i`. Exact Gram--Schmidt gives

`K_i=||w||^2||C||_F^2>Z/2.`                                   (5.3)

If the residual first-volume marginals are light, the compiler at `(1,1,2)` plus Riesz gives `<9.79 Z^-1/8`; if a residual row is heavy, the corresponding promoted physical two-row Gram determinant exceeds `K_i/2>Z/4`, and (3.3) gives `<8.64 Z^-1/8`.

Therefore (5.2) holds without a row-marginal hypothesis. This is a half-potential theorem, not a rank-two bounded-density assertion.

## 6. Nine large spectral directions: no-pivot branch

Assume `s_9(A)>=1` and no `eta`-pivot. The baseline spectral-to-volume proposition with crossing order `k=3` gives

` V_3(A)>=kappa^3. `                                           (6.1)

The baseline fair-coordinate-cut lemma supplies a literal cross block `M` with

`E_3(M)>=4^-3 kappa^3`.

Hence

`E_3(M)^-1/6 <=2 kappa^-1/2=160`.

By (4.5),

`||p_Q||_infinity <=160 C_3
 =2370.93402605488...<2400.`                                   (6.2)

This branch has a continuous `C_0` density.

## 7. Nine directions: pivot branches

### Scalar pivot

Suppose `|A_hh|>=eta`. Complete the square in the original coordinate `X_h`. The Schur complement `S` retains at least eight eigenvalues of modulus at least one by the audited Schur lemma.

If `S` has an `eta`-pivot, the baseline pivot proposition applies because it needs only two surviving directions. Keep its exact scalar-pivot constant rather than rounding:

`H(R)<=200+120 log16.`                                         (7.1)

The definite and indefinite pair subcases in that proposition are smaller. Outside `|R-a|<=1`, the kernel `|R-a|^-1/2` is at most one, so

`sup_a E|R-a|^-1/2 <=201+120 log16.`                            (7.2)

If instead `S` has no `eta`-pivot, then `s_5(S)>=1`. Apply the baseline spectral-to-volume proposition with `k=2`, then the fair cut:

`E_2(M_S)>=4^-2 kappa^2.`                                      (7.3)

By (5.2),

`sup_a E|R-a|^-1/2
 <=C_2 (4^-2 kappa^2)^-1/8
 =C_2 sqrt(160)
 =152.99191115498...<153,`                                     (7.4)

which is smaller than (7.2).

The scalar-square profile therefore gives

`||p_Q||_infinity
 <=eta^-1/2(201+120 log16)
 =2010+1200 log16
 =5337.106466687737... .`                                      (7.5)

### Definite pair

A definite principal two-coordinate pivot with determinant modulus at least `eta` has conditional density at most

`pi/sqrt(eta)=10pi<32.`                                        (7.6)

### Indefinite pair

An indefinite principal pair leaves at least seven Schur directions under `s_9(A)>=1`, hence in particular one eigenvalue of modulus at least one. The baseline hyperbolic envelope plus quarter-power logarithmic potential applies verbatim and gives

`||p_Q||_infinity<251.`                                        (7.7)

The no-pivot, scalar, definite-pair and indefinite-pair cases exhaust the normalized theorem. The maximum is (7.5).

## 8. Scaling

For general `K,s`, set `Y=KX`. Its coordinates have densities at most one. Define

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`.

Then `s_9(A/s)>=1` and

`Q=(s/K^2)Qtilde`.

Scalar density scaling gives

` ||p_Q||_infinity
 <=(2010+1200 log16) K^2/s
 <5338 K^2/s. `                                                 (8.1)

This completes a full replacement proof with every original hypothesis retained.

## 9. How far can the multiplicity be lowered in this run?

A source-matched later fleet03/B04 result (`improvements/fleet03/B04/20260924T124904Z-fleet03-B04-fixedmult-audit-r2/REPORT.md`, blob `851e0ae9c78a4d9a49f60a1cc5f0026b734579e6`) proves useful **eight-direction structure**, but not an eight-direction density theorem. Under no pivot and `s_8(A)>=1`, either third disjoint volume is already large (paid by Section 4), or a quantitative overlap-one/two-sided collar survives. The pivot branches above already work with only eight directions. The remaining unresolved branch therefore is a no-pivot physical collar requiring a product-preserving analytic receiver; no such receiver is proved in this B11 run.

Consequently:

- **9 directions:** complete theorem proved above, same full hypotheses.
- **8 directions:** not proved; reduced by peer structural work to a specific no-pivot collar.
- **3 directions:** unrestricted conjecture remains open.

I do not claim that nine is optimal. It is the lowest complete fixed-multiplicity theorem for which this run has a closed end-to-end proof.

## 10. Review gate and scope

- Baseline 17 manuscript: independently PASS in this B11 run.
- Nine-direction replacement: complete B11 reconstruction above; fleet01/B16 supplies a genuinely separate prior PASS reconstruction at commit `54ec2a651d854563f8db0d92c4c3426f76551786`.
- This satisfies the factual requirement that two distinct workers have complete mathematical PASS reconstructions of the nine-direction candidate, but owner/release synthesis remains a separate action and no publication/priority certificate is self-issued here.
- Full global continuity remains unproved; only the no-pivot/E3 branch is explicitly continuous.
- Model: GPT-5.6 Sol. Configured reasoning effort/provider thinking counters: `UNKNOWN / NOT_EXPOSED`.
