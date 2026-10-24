# account02/B13 improvement — complete nine-direction theorem with constant 5460

Run: `20260924T145501Z-account02-B13-fixedmult-auto11b`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline manuscript: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Theorem `QFORM-FIXED-MULTIPLICITY-9-5460-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K`. Let `A=A^T`, `b` and `c` be arbitrary. If

\[
s_9(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density and

\[
\boxed{\ \|p_Q\|_\infty\le 5460\,K^2/s.\ }
\]

No sign, moment, bounded-support, connected-support, log-concavity, iid, diagonal-basis, exact-rank, leverage, or post-rotation-independence hypothesis is used. Global continuity is not claimed. This theorem does **not** solve the unrestricted three-eigenvalue conjecture.

This is a complete replacement proof. The threshold-nine structural/analytic receiver is reconstructed below; the new B13 contribution is a zero-loss sharpening of the scalar-pivot logarithmic-kernel constant from `6010` to `5460`.

## 1. Dependencies from the pinned baseline

Only the following proved baseline ingredients are used:

1. Fourier/Riesz inversion and Schur spectral count (`manuscript.tex` lines 91--207).
2. Geometric BL, product-projection densities and scalar Fourier powers (221--301).
3. Scalar-square, definite-pair, hyperbolic-pair and quarter-power/log-potential lemmas (404--525).
4. The ordered-disjoint-minor interpolation, completion, spectral-to-volume proposition and fair coordinate cut (528--645).
5. The sharper pre-relaxation kernel estimate proved inside lines 654--674.

The grouped receivers in Sections 2--4 below are the replacement analytic endpoints that make order three sufficient for density and order two sufficient for the half-potential.

Throughout Sections 2--6 normalize `K=s=1`, and keep

\[
\eta=1/100,\qquad\kappa=1/80^2.
\]

## 2. Grouped weighted-subset receiver

Let `H,I,J` be pairwise disjoint sets of original coordinates. Let `W` be a `k`-dimensional orthogonal linear image of `X_H` whose density is bounded by `M_H`. Consider a quadratic polynomial written as

\[
Q=F(X_H)+2\langle W,MX'+\beta\rangle+R(X'),
\qquad X'=(X_I,X_J),
\]

where `F` is arbitrary measurable, `R` is an arbitrary quadratic/affine phase, and the restriction `M_J` has row rank `k`. Let

\[
S=\prod_{r=1}^k s_r(M_J)
\]

(the empty product is one when `k=0`). Project the physical `I-J` crossing rows of the residual quadratic part orthogonally off `row(M_J)` and call the resulting row matrix `C`.

For `ell>=1`, define

\[
Z_\ell=\sum_{|T|=\ell}\det(C_TC_T^T),
\qquad
w_T=\det(C_TC_T^T)/Z_\ell,
\]

summing only positive determinants, and let the inclusion marginals be

\[
\alpha_i=\sum_{T\ni i}w_T.
\]

Assume every positive `alpha_i<=1/2`, and put `d=k+ell>2`. Then

\[
|\phi_Q(t)|\le \min\{1,K_{k,\ell}|t|^{-d/2}\},
\]

where

\[
K_{k,\ell}=M_H^{1/2}\pi^{d/2}2^{\ell/4}e^{(k+2\ell)/4}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
S^{-1/2}Z_\ell^{-1/4}.
\tag{2.1}
\]

### Proof

Push the complex measure `e^{itF}dP_H` to `W`. Its density `a_t` obeys `|a_t|<=p_W`, hence

\[
\|a_t\|_2^2\le \|p_W\|_\infty\|p_W\|_1\le M_H.
\]

Plancherel after the scale `2t` gives a hub factor

\[
M_H(\pi/|t|)^k.
\tag{2.2}
\]

For the light bank, condition on the literal `I` coordinates and square the resulting complex pushforward. Introduce an independent copy only of `X_J`. The same-bank `I` phases cancel, same-bank `J` phases have modulus one, and `D=X_J-X'_J` has independent cap-one coordinates. Integrating each original `X_i`, `i in I`, produces literal scalar Fourier factors

\[
|\widehat f_i(2t\langle a_i,D\rangle)|.
\]

For a determinant-weighted `ell`-set `T`, write `a_i=c_i+\lambda_iM_J`, with `c_i` orthogonal to `row(M_J)`. The linear map

\[
D\longmapsto\bigl(M_JD,(\langle c_i,D\rangle)_{i\in T}\bigr)
\]

has squared Jacobian/Gram determinant

\[
S^2\det(C_TC_T^T).
\tag{2.3}
\]

The baseline product-projection lemma therefore bounds the density of this `d`-dimensional image by

\[
\frac{e^{d/2}}{S\sqrt{\det(C_TC_T^T)}}.
\tag{2.4}
\]

Weighted Holder uses exponent `1/alpha_i>=2` for each **positive** marginal; zero marginals are omitted. The scalar Fourier-power lemma, including the scale `2t`, gives

\[
\int_\mathbb R
|\widehat f_i(2t(y+u))|^{1/\alpha_i}\,dy
\le \frac{\pi\sqrt{2e\alpha_i}}{|t|}.
\tag{2.5}
\]

The determinant geometric mean is

\[
Z_\ell^{-1/2}e^{H(w)/2}.
\]

Order a sampled `ell`-subset uniformly. Entropy subadditivity yields

\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le \ell\log\ell-\log(\ell!).
\tag{2.6}
\]

Combining (2.2)--(2.6), then taking the square root from the light-bank `L^2` step, gives (2.1). For `k=0` there is simply no hub: the zero-dimensional projected density cap and empty singular product are one. This is a separate endpoint convention, not a division by zero.

Integrating the power envelope for `d>2` and using Fourier inversion gives

\[
\|p_Q\|_\infty\le
\frac d{d-2}
M_H^{1/d}2^{\ell/(2d)}e^{(k+2\ell)/(2d)}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/(2d)}
S^{-1/d}Z_\ell^{-1/(2d)}.
\tag{2.7}
\]

No projected random coordinates are declared independent anywhere in the argument.

## 3. Marginal-free third-volume density receiver

For a literal physical crossing matrix `M`, let

\[
E_3(M)=e_3(MM^T)=:Z>0.
\]

Let `J_i` be the third-volume mass incident to physical row `i`, so `sum_iJ_i=3Z`.

If every normalized marginal `J_i/Z<=1/2`, use (2.7) at `(k,ell)=(0,3)`. Otherwise promote a heavy literal row `w`. Orthogonal Gram--Schmidt gives exactly

\[
J_i=\|w\|^2e_2(CC^T).
\]

If the residual order-two packet has a heavy row, promote it; for the promoted two-row matrix `P`, exact Gram--Schmidt gives

\[
H_{ij}=\det(PP^T)\,\|C_2\|_F^2>J_i/2.
\]

If the residual order-one packet is heavy, promote that row as well, obtaining an actual physical three-row Gram determinant `>H_{ij}/2`. Thus the four branches are paid by the grouped receiver at `(0,3)`, `(1,2)`, `(2,1)`, or the terminal exact-rank-three Plancherel/Jacobian estimate.

The worst branch constant is

\[
C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots,
\]

so universally

\[
\boxed{\ \|p_Q\|_\infty\le C_3E_3(M)^{-1/6}.\ }
\tag{3.1}
\]

All same-bank quadratic and affine phases are retained inside complex pushforwards.

## 4. Marginal-free second-volume half-potential receiver

The identical promotion tree one dimension lower, with the Riesz weight rather than direct density inversion, gives

\[
\boxed{\ \sup_a\mathbb E|Q-a|^{-1/2}
\le C_2E_2(M)^{-1/8},\ }
\tag{4.1}
\]

where

\[
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots.
\]

This is deliberately a half-potential theorem, **not** a rank-two density theorem. The latter would be false in the indefinite case because a logarithmic singularity is possible.

## 5. New B13 constant lemma: sharper scalar-pivot truncated half-potential

The baseline proposition used the relaxed kernel bound

\[
J(d)\le8+3\log_+(1/|d|)
\]

and the relaxed quarter-power coefficient `16`, producing the convenient scalar-pivot bound `<560` and the global pivot bound `600`. The proof actually contains strictly sharper information at no additional hypothesis.

### Lemma `QFORM-SCALAR-PIVOT-H545-v1`

If `A=A^T` has at least two eigenvalues of modulus at least one and a scalar pivot

\[
|A_{ii}|\ge\eta=1/100,
\]

then every affine quadratic polynomial with this quadratic part satisfies

\[
\boxed{\ H(Q)\le545.\ }
\tag{5.1}
\]

### Proof

After completing the square in the pivot coordinate, the Schur critical value `R` has a quadratic matrix with operator norm at least one by the baseline Schur-count lemma.

The quarter-power proof obtains the explicit coefficient

\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)
\]

and proves elementarily

\[
C_q<40/3<16.
\tag{5.2}
\]

Hence, uniformly in `a`,

\[
\mathbb P\{|R-a|<\rho\}\le\min(1,C_q\rho^{1/4}).
\tag{5.3}
\]

Before its final relaxation, the baseline kernel proof gives

\[
J(d)\le J_*+2\sqrt2\log_+\frac1{2|d|},
\tag{5.4}
\]

with

\[
J_*=2\operatorname{arsinh}\sqrt2+\pi+2\operatorname{arcosh}\sqrt2<8.
\]

By layer cake and (5.3),

\[
\begin{aligned}
\mathbb E\log_+\frac1{2|R-a|}
&=\int_0^\infty
\mathbb P\{|R-a|<\tfrac12e^{-u}\}\,du\\
&\le4+4\log_+(C_q2^{-1/4}).
\end{aligned}
\tag{5.5}
\]

Using only the manuscript's elementary `C_q<40/3`, together with `log(40/3)<log16<3` and `log2>1/2`, gives

\[
4+4\log_+(C_q2^{-1/4})<4+4(3-1/8)=15.5.
\tag{5.6}
\]

(The elementary `log2>1/2` follows, for example, from `e<4`.) Since `2sqrt2<3`, (5.4)--(5.6) yield

\[
\mathbb E J(R-a)<8+3(15.5)=54.5.
\]

The scalar square profile contributes `|A_ii|^{-1/2}<=10`, so

\[
H(Q)<545,
\]

which proves (5.1). No smoothness, moment, support, or independence between the square and `R` is used.

For comparison, the definite-pair and indefinite-pair pivot branches in the baseline are already `<160` and `<444`, respectively. Thus one could also replace the baseline global pivot constant `600` by `545` whenever only that proposition is needed.

## 6. Assemble multiplicity nine

Normalize `K=s=1`.

### 6.1 No pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the pinned spectral-to-volume theorem at order three gives

\[
V_3(A)\ge\kappa^3.
\]

A fair physical coordinate cut has

\[
E_3(M)\ge4^{-3}\kappa^3,
\qquad E_3(M)^{-1/6}\le160.
\]

By (3.1),

\[
\|p_Q\|_\infty\le160C_3<2400.
\tag{6.1}
\]

### 6.2 Scalar pivot

A scalar pivot removes one original coordinate. The Schur complement retains at least eight eigenvalues of modulus at least one.

If that Schur complement has a pivot, Lemma (5.1) and the already smaller pair-pivot branches give its truncated half potential at most `545`; outside `|R-a|<=1`, the kernel is at most one, so

\[
\sup_a\mathbb E|R-a|^{-1/2}\le546.
\tag{6.2}
\]

If instead the Schur complement has no pivot, it has in particular `s_5>=1`. The pinned spectral-to-volume theorem at order two and a fair cut give

\[
E_2(M)\ge4^{-2}\kappa^2,
\qquad E_2(M)^{-1/8}\le\sqrt{160}.
\]

By (4.1), its full half potential is

\[
\le C_2\sqrt{160}<153<546.
\tag{6.3}
\]

Thus in every scalar-pivot subcase the Schur half potential is at most `546`. The outer square profile contributes at most `eta^{-1/2}=10`, hence

\[
\boxed{\ \|p_Q\|_\infty\le5460.\ }
\tag{6.4}
\]

### 6.3 Definite pair pivot

The conditioned physical pair has joint cap one and determinant modulus at least `eta`; the definite-pair Jacobian gives

\[
\|p_Q\|_\infty\le\pi/\sqrt\eta=10\pi<32.
\tag{6.5}
\]

### 6.4 Indefinite pair pivot

The Schur complement retains at least seven unit-scale spectral directions and in particular has operator norm at least one. The full hyperbolic envelope plus quarter-power logarithmic averaging gives the baseline bound `<251`.

The maximum of (6.1), (6.4), (6.5) and the indefinite-pair branch is `5460`.

## 7. Restore `K,s`

Set `Y=KX`; its coordinate densities are bounded by one. Define

\[
\widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad
Q=(s/K^2)\widetilde Q.
\]

Since `s_9(A/s)>=1`, the normalized theorem gives `||p_{Qtilde}||_infinity<=5460`. Density scaling therefore gives

\[
\boxed{\ \|p_Q\|_\infty\le5460K^2/s.\ }
\]

This completes the replacement proof.

## 8. Why this does not claim multiplicity eight

Under no pivot and `s_8(A)>=1`, the current structural theorem says either the order-three volume already pays through (3.1), or a quantitatively nonzero overlap-one/two-sided physical collar remains. The present proof has no product-preserving receiver that turns that shared-anchor collar into an integrable characteristic-function envelope. The critical rank-two indefinite endpoint can have a logarithmically unbounded density, so `E_2` alone cannot close the gap.

Therefore the lowest complete theorem supported here is **nine**, with the improved constant `5460`. Multiplicity eight and the unrestricted three-eigenvalue conjecture remain open.

## Closed dependency map

`baseline Fourier/Riesz + BL/projection/scalar powers`
` -> grouped weighted-subset compiler`
` -> marginal-free E3 density + E2 half-potential`
` -> baseline no-pivot spectral-to-volume/random cut`
` -> s9 no-pivot density and scalar-Schur half potential`;

`baseline scalar square + Schur count`
` -> sharper pre-relaxation J kernel + explicit quarter coefficient`
` -> scalar-pivot H<=545`
` -> full Schur half potential<=546`
` -> outer scalar density<=5460`;

`baseline definite/hyperbolic pair lemmas`
` -> remaining pivot branches <32 and <251`;

`normalization Y=KX, A/s`
` -> 5460 K^2/s`.

Manual changed-file review found only mathematical content, source hashes/commits, logical run metadata and no credentials, machine paths, scheduler identifiers, private personal data, email, or unrelated material.
