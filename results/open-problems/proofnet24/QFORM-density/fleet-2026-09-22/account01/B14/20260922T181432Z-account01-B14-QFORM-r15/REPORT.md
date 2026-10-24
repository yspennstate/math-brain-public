# account01/B14 — diffuse rank-two separable half-Riesz localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T181432Z-account01-B14-QFORM-r15`  
**Assignment:** Translations and localization  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_TRANSLATION_UNIFORM_FRACTIONAL_TRACE`  
**Full conjecture:** OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

For every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, the full target is a universal finite `C` such that

\[
\Pr\{X^TAX\in I\}\le C|I|
\]

for every interval `I`, equivalently an essentially bounded output density. No moment, bounded-support, connected-support, centering, identical-law, sign or coordinate-alignment hypothesis is available.

Fresh control used before derivation/publication: `yspennstate/math-research-brain@72974f9bca2247eeabf9c6bb290f51bc5029f44d`, OWNER CONTROL revision `2026-09-22.11`, programme revision `2026-09-22.5`.

Corrections retained: law-uniform pointwise quadratic Fourier decay is false; arbitrary-joint 3D coarea is false; conditioning on a spectral complement and paying positive moments of a conditional projection cap is false; bounded-diameter/fixed-fragment localization is false; physical small-minor extraction is not exhaustive. None of those false interfaces is used below.

## 2. Completed partner result actually applied

I use account02/B14's complete `QFORM-MASS-LINEAR-LOCALIZATION-COMPILER-v1`:

`yspennstate/math-open-problems@09de6ccb5717e33b999cae0cf0c6b5f6a3579f08`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T170244Z-account02-B14-QFORM-r16/REPORT.md`.

If a positive measure decomposition `nu=sum_alpha nu_alpha`, with masses `w_alpha`, satisfies

\[
\nu_\alpha\{Q\in I\}\le w_\alpha C_\alpha |I|,
\]

then

\[
\nu\{Q\in I\}\le \Big(\sum_\alpha w_\alpha C_\alpha\Big)|I|.
\]

In particular, a deterministic-outside estimate with one constant `K` is zero-tax under arbitrary positive localization of the outside law: each piece contributes `w_alpha K|I|`, and the masses sum to one. This is the exact interface used in Section 6.

The analytic starting point is the completed rank-two affine half-Riesz argument

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

and the complex-amplitude/separable-phase mechanism in

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`

`proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

The new step is their rank-two **fractional** synthesis: at rank two the density Fourier integral is critical and need not converge, but the half-Riesz trace is subcritical and does converge, even after completely arbitrary coordinatewise measurable perturbations.

## 3. Main analytic theorem: diffuse rank-two separable half-Riesz

### Theorem 3.1 — `QFORM-RANK2-DIFFUSE-SEPARABLE-HALF-RIESZ-v1`

Let `U` be an `m x 2` real matrix with orthonormal columns. Write its rows as `u_j^T` and

\[
c_j=\|u_j\|_2^2\le \frac12.
\]

Let `Lambda` be any invertible real symmetric `2 x 2` matrix. Let `X_1,...,X_m` be independent with probability densities bounded by one. Let `V_j:R->R` be arbitrary measurable functions, finite almost surely, and put

\[
R=(U^T X)^T\Lambda(U^T X)+\sum_{j=1}^m V_j(X_j).
\]

Define

\[
B(U)=\prod_{c_j>0}(1-c_j)^{-(1-c_j)/2}.
\]

Then for every `w in R`,

\[
\boxed{
\mathbb E|R-w|^{-1/2}
\le 4\sqrt{2B(U)}\,|\det\Lambda|^{-1/4}
\le 4\sqrt{2e}\,|\det\Lambda|^{-1/4}.
}
\tag{3.1}
\]

There are no assumptions on the size, growth, support, or translations contained in the `V_j`. In particular `V_j` may be arbitrary diagonal quadratic plus linear perturbations.

### Proof

Use the Fourier convention

\[
\widehat h(\xi)=\int_{\mathbb R}e^{-i\xi x}h(x)\,dx.
\]

Fix a real frequency `t` and set

\[
h_{j,t}(x)=f_j(x)e^{itV_j(x)}.
\]

For every `p>=1`,

\[
\|h_{j,t}\|_p^p=\int f_j(x)^p dx\le\int f_j(x)dx=1. \tag{3.2}
\]

The phase therefore costs nothing in every norm used below.

Push the complex product measure with density `prod_j h_{j,t}` through the linear map `x -> U^T x`. It has a complex `L^1` density `g_t` of total variation at most one. Coordinates with `c_j=0` contribute scalar factors of modulus at most one and may be omitted. For `c_j>0`, set

\[
v_j=u_j/\sqrt{c_j}.
\]

Then

\[
\sum_j c_j v_jv_j^T=I_2,
\qquad \sum_jc_j=2. \tag{3.3}
\]

Geometric rank-one Brascamp--Lieb applied to

\[
\widehat g_t(\xi)=\prod_j\widehat h_{j,t}(u_j\cdot\xi)
\]

and sharp Hausdorff--Young with conjugate exponent `1/c_j` give exactly as in the source diffuse proof

\[
\|\widehat g_t\|_1
\le (2\pi)^2 B(U). \tag{3.4}
\]

Indeed `c_j<=1/2` puts `1/c_j` in the Hausdorff--Young range `[2,infinity)`, and the powers of `c_j` cancel. Also

\[
\log B(U)
=\frac12\sum_j -(1-c_j)\log(1-c_j)
\le \frac12\sum_jc_j=1, \tag{3.5}
\]

so `B(U)<=e`.

Now write the characteristic function of `R` as the quadratic oscillatory integral against `g_t`. Gaussian regularization, Fourier inversion, and diagonalization of `Lambda` in the two-dimensional **spectral** integral (not in the original product coordinates) yield

\[
|\phi_R(t)|
\le \min\left\{1,
\pi B(U)|\det\Lambda|^{-1/2}|t|^{-1}\right\}. \tag{3.6}
\]

This is the same complex-amplitude argument as the separable-phase source, specialized to rank two. It is not the false one-dimensional law-uniform pointwise decay: the `|t|^{-1}` comes from joint two-dimensional projected curvature after the product Fourier/Brascamp--Lieb aggregation, with the coordinate phases retained inside `h_{j,t}`.

For completeness, the distributional Fourier transform is

\[
\widehat{|x|^{-1/2}}(t)=\sqrt{2\pi}\,|t|^{-1/2}. \tag{3.7}
\]

Gaussian regularization makes the following identity/inequality rigorous and Tonelli applies to the resulting nonnegative majorant:

\[
\mathbb E|R-w|^{-1/2}
\le (2\pi)^{-1/2}
\int_{\mathbb R}|t|^{-1/2}|\phi_R(t)|dt. \tag{3.8}
\]

Set

\[
K=\pi B(U)|\det\Lambda|^{-1/2}.
\]

Then

\[
\int_{\mathbb R}|t|^{-1/2}\min(1,K/|t|)dt
=8\sqrt K. \tag{3.9}
\]

Substituting into (3.8) gives

\[
(2\pi)^{-1/2}8\sqrt{\pi B(U)}|\det\Lambda|^{-1/4}
=4\sqrt{2B(U)}|\det\Lambda|^{-1/4}.
\]

Together with `B(U)<=e`, this proves (3.1). QED.

## 4. Exact translation-uniform scalar shell

The following elementary inequality is useful because it converts (3.1) directly to a density bound without assuming the rank-two random variable itself has a bounded density.

### Lemma 4.1

Let `a!=0`, `I=[t,t+h]`, `h>0`, and define

\[
s_I(a)=\begin{cases}t,&a>0,\\ t+h,&a<0.\end{cases}
\]

For every real `r` and every translation `g`,

\[
\left|\{x:a(x+g)^2+r\in I\}\right|
\le h|a|^{-1/2}|r-s_I(a)|^{-1/2}. \tag{4.1}
\]

At `r=s_I(a)` the right side is interpreted as `+infinity`.

### Proof

Translation removes `g`. For `a>0`, if `r<t`, the preimage length is

\[
\frac2{\sqrt a}\left(\sqrt{t+h-r}-\sqrt{t-r}\right)
\le \frac h{\sqrt a\sqrt{t-r}}.
\]

If `t<=r<=t+h`, it is `2sqrt((t+h-r)/a)`, while

\[
2\sqrt{(r-t)(t+h-r)}\le h
\]

proves the same bound. The remaining cases are empty. The case `a<0` follows after reflecting the output interval and uses the upper endpoint `t+h`. QED.

Thus, if `X` has density at most one and is independent of `Y`,

\[
Q=a(X+g(Y))^2+H(Y)
\]

obeys

\[
\Pr\{Q\in I\}
\le h|a|^{-1/2}\mathbb E|H-s_I(a)|^{-1/2}, \tag{4.2}
\]

with **no dependence at all** on the size or distribution of the possibly correlated translation `g(Y)`.

## 5. Grouped Schur theorem with arbitrary diagonal bank perturbation

### Theorem 5.1 — `QFORM-SCHUR-DIFFUSE-RANK2-PLUS-SEPARABLE-v1`

Let `A` be any real symmetric `n x n` matrix. Choose one original coordinate `i` with

\[
a=A_{ii}\ne0
\]

and let `S` be the full Schur complement after pivoting coordinate `i`:

\[
S=A_{-i,-i}-a^{-1}A_{-i,i}A_{i,-i}. \tag{5.1}
\]

Suppose that for some bank `J` of original coordinates disjoint from `i`,

\[
S_{JJ}=D+U\Lambda U^T, \tag{5.2}
\]

where `D` is an arbitrary real diagonal matrix, `U^TU=I_2`, every row leverage of `U` is at most `1/2`, and `Lambda` is invertible symmetric. No assumption is made on `S_{J,J^c}`, `S_{J^c,J^c}`, or the remaining entries/eigenvalues of `A`.

Then for independent cap-one inputs,

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
4\sqrt{2B(U)}\,|a|^{-1/2}|\det\Lambda|^{-1/4}
\le
4\sqrt{2e}\,|a|^{-1/2}|\det\Lambda|^{-1/4}.
}
\tag{5.3}
\]

The conclusion is an essential density bound; no support or moment condition is present.

### Proof

Condition on every original coordinate outside `{i} union J`; call its deterministic value `z`. Complete the square only in the original pivot coordinate. The conditional form is

\[
Q_z=a\bigl(X_i+g_z(X_J)\bigr)^2+H_z(X_J), \tag{5.4}
\]

where `g_z` may be any affine function of the bank variables. The Schur identity gives

\[
H_z(X_J)
=(U^TX_J)^T\Lambda(U^TX_J)
+\sum_{j\in J}d_jX_j^2+b_z^TX_J+c_z. \tag{5.5}
\]

Apply Lemma 4.1 and average the pivot coordinate:

\[
\Pr\{Q_z\in I\}
\le h|a|^{-1/2}
\mathbb E_{X_J}|H_z-s_I(a)|^{-1/2}. \tag{5.6}
\]

Theorem 3.1 applies to (5.5) with

\[
V_j(x)=d_jx^2+(b_z)_jx,
\]

and is uniform in every coefficient of the affine vector `b_z` and scalar `c_z`. Therefore the right side of (5.6) is bounded by the right side of (5.3) times `h`, uniformly in `z`. Averaging the conditioned outside coordinates proves the interval bound. The standard domination criterion for measures (`mu(I)<=C|I|` for every interval) gives an absolutely continuous law with essential density at most `C`. QED.

This strictly enlarges the preceding B14 grouped-Schur theorem: the bank need not have exact rank two. It may have full rank because of the entire arbitrary diagonal `D`; the rank-two curvature is aggregated **before** any tiny physical-minor inversion.

## 6. Exact application of the account02/B14 mass-linear compiler

Let the outside law in Theorem 5.1 be decomposed arbitrarily into positive submeasures

\[
\rho=\sum_\alpha\rho_\alpha,
\qquad w_\alpha=\rho_\alpha(\mathbb R^{J^c\setminus\{i\}}).
\]

For every deterministic outside value, (5.6) gives one constant

\[
C_*=4\sqrt{2B(U)}|a|^{-1/2}|\det\Lambda|^{-1/4}.
\]

Hence each unnormalized outside component satisfies the **actual partner inequality**

\[
\nu_\alpha\{Q\in I\}
=\int\rho_\alpha(dz)\Pr_{i,J}\{Q_z\in I\}
\le w_\alpha C_*|I|. \tag{6.1}
\]

The account02/B14 compiler sums (6.1) to

\[
\Pr\{Q\in I\}\le C_*|I| \tag{6.2}
\]

with exactly zero localization tax. Thus distant outside fragments, arbitrary support translations, unbounded support, and infinite moments do not enter the constant. No tiny component is normalized, so the partner's normalized-cap obstruction is avoided exactly.

Combined with the underlying law-level localization used by account02/B14, any compact finite-fragment approximation of the outside laws passes to the arbitrary-law result with the same constant; however, Theorem 5.1 itself already works directly for arbitrary outside product laws and does not require compactification.

## 7. A full-rank target family where aggregation removes a diverging minor cost

This section shows that the new diagonal-separable extension is not cosmetic.

Let `m>=4` be even. Put

\[
s_j=\begin{cases}+1,&j\le m/2,\\-1,&j>m/2,\end{cases}
\qquad
u_j=\frac1{\sqrt m}(1,s_j),
\]

and let `U` have rows `u_j`. Then

\[
U^TU=I_2,
\qquad c_j=2/m\le1/2. \tag{7.1}
\]

Take

\[
\Lambda=\operatorname{diag}(2,-2),
\qquad \varepsilon=m^{-2},
\qquad S_m=\varepsilon I_m+U\Lambda U^T,
\qquad A_m=[1]\oplus S_m. \tag{7.2}
\]

Because the nonzero eigenvalues of `U Lambda U^T` are exactly `2,-2`,

\[
\operatorname{spec}(A_m)
=\{1,\,2+\varepsilon,\,-2+\varepsilon,
\underbrace{\varepsilon,\ldots,\varepsilon}_{m-2}\}. \tag{7.3}
\]

Hence `A_m` is full rank, indefinite, and lies in the exact target class for every even `m>=4`.

Theorem 5.1 applies with `a=1`, `D=epsilon I_m`. Since

\[
B(U)=\left(1-\frac2m\right)^{-(m-2)/2}\le e,
\qquad |\det\Lambda|=4,
\]

we obtain the dimension-free arbitrary-law bound

\[
\boxed{
\|p_{X^TA_mX}\|_\infty
\le4\sqrt{B(U)}\le4\sqrt e<6.595.
}
\tag{7.4}
\]

By contrast, the physical entries of the rank-two core satisfy

\[
(U\Lambda U^T)_{jk}
=\frac2m(1-s_js_k), \tag{7.5}
\]

so a same-sign physical pair has determinant `epsilon^2`, while an opposite-sign pair has determinant

\[
\varepsilon^2-16/m^2. \tag{7.6}
\]

Therefore every physical `2 x 2` principal determinant has magnitude below `16/m^2`. If one applies the preceding exact-rank-two physical-bank certificate to a two-coordinate bank, its **certificate constant** is at least

\[
128(16/m^2)^{-1/4}=64\sqrt m, \tag{7.7}
\]

while (7.4) stays below `6.595`. The statement (7.7) is about deterioration of that proof certificate, not a lower bound on the true output density. The new theorem succeeds because it keeps the whole diffuse rank-two bank intact and treats the full-rank diagonal perturbation as cost-free coordinatewise phase before inversion.

Arbitrary extra original coordinates, arbitrary quadratic coefficients on them, and arbitrary couplings to this bank may be appended to the ambient matrix. Conditioning them merely changes the affine vector `b_z` and scalar term in (5.5), so the same bound survives. The target spectral hypothesis is retained whenever the displayed principal block remains present, by eigenvalue interlacing.

## 8. What changed and what remains unpaid

**Old B14 missing implication:** after the grouped exact-rank-two Schur theorem, a full-rank Schur bank with many small diagonal directions fell outside the theorem even when its two-dimensional aggregate curvature was perfectly diffuse; reducing to physical pairs could pay a reciprocal minor cost growing with dimension.

**New essential step:** arbitrary diagonal/separable perturbations of a diffuse rank-two Schur bank cost nothing in the half-Riesz stage. The exact translation-uniform bound is (5.3), and partner mass-linear localization shows arbitrary outside fragmentation costs nothing as well. The explicit family (7.2) exhibits a dimension-free new closure where the former physical-pair certificate grows like `sqrt(m)`.

**Still unpaid:** the bare hypothesis “at least three spectral eigenvalues of magnitude >=1” does not yet force a scalar pivot plus Schur bank satisfying (5.2) with `|a|`, `|det Lambda|` and leverage quantitatively favorable. Nor does every nonseparable higher-rank Schur remainder reduce to diagonal plus a diffuse rank-two component. The full theorem therefore remains OPEN.

The next high-value structural implication is an exhaustive product-preserving decomposition showing that every remaining target matrix enters at least one of:

1. a ridge/diffuse branch already certified at a universal constant;
2. the present scalar-pivot plus diffuse-rank-two-with-separable-remainder branch with controlled `|a|^{-1/2}|det Lambda|^{-1/4}`;
3. a heavy/near-zero-pivot grouped branch that aggregates an original-coordinate bank before any reciprocal tiny-minor payment.

The known singleton-plus-two-banks and small-minor counterexamples must remain explicit controls on such a decomposition.

## 9. Integrity/status

This is a supporting theorem, not a proof of the full QFORM conjecture. No arbitrary-joint coarea lemma, conditional projection-cap moment, pointwise one-dimensional quadratic decay, bounded support, bounded diameter, fixed fragment count, or moment assumption is used. The theorem preserves original-coordinate independence throughout; only the two-dimensional spectral integral is orthogonally diagonalized inside a Fourier calculation.

Changed-file allowlist for this mathematical archive is only this report. Manual privacy review finds pure mathematical content and source pins only; no credentials, scheduler IDs, machine paths, unrelated private data, or public-release action are present. No paid/remote computation was used.
