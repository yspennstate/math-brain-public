# fleet01/B14 — translation-uniform grouped Schur localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T171237Z-fleet01-B14-QFORM-r14`  
**Assignment:** Translations and localization  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_GROUPED_SCHUR_THEOREM`  
**Full conjecture:** OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and mechanism change

The target is: for every finite `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove one universal finite `C` such that

\[
\Pr\{X^TAX\in I\}\le C|I|
\]

for every bounded interval `I`, or give a valid counterexample.

The previous B14 runs completed law-level localization and several fragment/gap compilers. This run changes mechanism as required: it uses the current orientation-free rank-two half-Riesz theorem to produce an **unnormalized deterministic-outside curved certificate** for a higher-rank grouped Schur branch. The active bank is never fragmented or normalized; arbitrary outside tails, translations, distant fragments, and additional quadratic components are conditioned and summed mass-linearly.

## 2. Exact source dependencies

### 2.1 Assigned partner actually applied

Fleet02/B14 run `20260922T170244Z-fleet02-B14-QFORM-r16`, canonical report

`yspennstate/math-open-problems@09de6ccb5717e33b999cae0cf0c6b5f6a3579f08`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T170244Z-fleet02-B14-QFORM-r16/REPORT.md`

proves `QFORM-MASS-LINEAR-LOCALIZATION-COMPILER-v1`: if a positive decomposition `nu=sum_alpha nu_alpha` has masses `w_alpha` and each piece obeys

\[
\nu_\alpha\{Q\in I\}\le w_\alpha C_\alpha |I|,
\]

then

\[
\nu\{Q\in I\}\le \Big(\sum_\alpha w_\alpha C_\alpha\Big)|I|.
\]

In particular, a deterministic-outside estimate with one constant `K` may be integrated over arbitrary outside fragment submeasures with **zero localization tax**. The same report records the normalize-then-cap, distant-shift, and no-moment barriers; the present proof avoids all three.

### 2.2 Analytic input

Interactive report

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

at

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

proves the supporting theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`: if `U` has two orthonormal columns, `Lambda` is invertible symmetric `2x2`, `b` is arbitrary, and `Y_j` are independent with densities at most one, then

\[
\sup_s \mathbb E\big|(U^TY)^T\Lambda(U^TY)+b^TY-s\big|^{-1/2}
\le128\,|\det\Lambda|^{-1/4}. \tag{2.1}
\]

The report supplies a complete proof of this supporting theorem; independent end-to-end review of that source theorem was still pending in the source status, so this report does not promote it beyond its stated status.

## 3. Exact scalar-square shell lemma

### Lemma 3.1 — one-coordinate shell to half-Riesz, translation-uniform

Let `a!=0`, let `I=[t,t+h]` with `h>0`, and define the distinguished endpoint

\[
s_I(a)=\begin{cases}
t,&a>0,\\
t+h,&a<0.
\end{cases}
\]

For every real `r`, with the right side interpreted as `+infinity` if `r=s_I(a)`,

\[
\left|\{x\in\mathbb R: ax^2+r\in I\}\right|
\le \frac{h}{\sqrt{|a|}}\,|r-s_I(a)|^{-1/2}. \tag{3.1}
\]

Consequently, if `X` is independent of a random object `Y`, `X` has density at most one, and

\[
Q=a(X+g(Y))^2+H(Y),
\]

then

\[
\Pr\{Q\in I\}
\le \frac{h}{\sqrt{|a|}}\,
\mathbb E|H(Y)-s_I(a)|^{-1/2}. \tag{3.2}
\]

#### Proof

It suffices first to take `a>0`. Put `d=t-r`.

If `d>=0`, the inverse image has total length

\[
\frac{2}{\sqrt a}(\sqrt{d+h}-\sqrt d)
=\frac{2h}{\sqrt a(\sqrt{d+h}+\sqrt d)}
\le \frac{h}{\sqrt a\sqrt d}.
\]

If `-h<d<0`, write `u=-d\in(0,h)`. The inverse image has length

\[
\frac{2}{\sqrt a}\sqrt{h-u}.
\]

The inequality

\[
2\sqrt{h-u}\le \frac{h}{\sqrt u}
\]

is equivalent after squaring to `4u(h-u)<=h^2`, i.e. `(2u-h)^2>=0`. If `d<=-h` the inverse image is empty. This proves (3.1) for `a>0`. For `a<0`, replace the expression by its negative and apply the positive case to the reflected interval `[-t-h,-t]`; the distinguished endpoint becomes `t+h`.

Condition on `Y=y`. Translation by `g(y)` does not increase the density cap of `X`; hence the conditional probability is bounded by the Lebesgue length in (3.1). Integrating gives (3.2). `QED`

This lemma is exactly translation-uniform: `g(Y)` may be arbitrarily large and correlated with `H(Y)`.

## 4. Main theorem: grouped rank-two Schur bank with arbitrary residual

Reorder original coordinates as

\[
x=(x_0,y,z),\qquad y\in\mathbb R^m,\ z\in\mathbb R^k,
\]

and write

\[
A=
\begin{pmatrix}
a&u^T&v^T\\
u&B&C\\
v&C^T&D
\end{pmatrix},\qquad a\ne0. \tag{4.1}
\]

Let the scalar-pivot Schur complement be

\[
S=
\begin{pmatrix}B&C\\C^T&D\end{pmatrix}
-\frac1a\binom uv(u^T\ v^T)
=
\begin{pmatrix}S_{yy}&S_{yz}\\S_{zy}&S_{zz}\end{pmatrix}. \tag{4.2}
\]

Assume only that the physical grouped principal block `S_yy` has **exact rank two**. Let its two nonzero eigenvalues be `mu_1,mu_2`, and set

\[
\Delta_2:=|\mu_1\mu_2|>0. \tag{4.3}
\]

No assumption is imposed on `S_yz` or `S_zz`; in particular the full Schur complement may have arbitrary rank and arbitrary additional eigenvalues.

### Theorem 4.1 — `QFORM-GROUPED-SCHUR-RANK2-OUTSIDE-FREE-v1`

For independent original coordinates with densities bounded by one,

\[
\boxed{
\|p_{X^TAX}\|_{L^\infty}
\le128\,|a|^{-1/2}\Delta_2^{-1/4}.
} \tag{4.4}
\]

Equivalently, for every bounded interval `I`,

\[
\Pr\{X^TAX\in I\}
\le128\,|a|^{-1/2}\Delta_2^{-1/4}|I|. \tag{4.5}
\]

The bound is uniform over all translations, tails, fragments, moments, the dimension and law of `z`, the cross block `S_yz`, and the entire quadratic residual `S_zz`.

#### Proof

Complete the square in the single original coordinate `x_0`:

\[
X^TAX
=a\left(x_0+\frac{u^Ty+v^Tz}{a}\right)^2
+\begin{pmatrix}y\\z\end{pmatrix}^T
S
\begin{pmatrix}y\\z\end{pmatrix}. \tag{4.6}
\]

Because `S_yy` has rank two, write

\[
S_{yy}=U\Lambda U^T,
\]

where `U` is `m x 2` with orthonormal columns and `Lambda` is an invertible symmetric `2x2` matrix with

\[
|\det\Lambda|=\Delta_2. \tag{4.7}
\]

For fixed `z`, define

\[
H_z(y)
=y^TS_{yy}y+2y^TS_{yz}z+z^TS_{zz}z. \tag{4.8}
\]

The variables in `y` remain independent cap-one coordinates after conditioning on `z`. Equation (4.8) is precisely

\[
H_z(y)=(U^Ty)^T\Lambda(U^Ty)+b_z^Ty+c_z,
\]

with arbitrary affine vector `b_z=2S_{yz}z` and constant `c_z=z^TS_{zz}z`. Therefore (2.1), with the constant absorbed into the target level, gives uniformly in `z` and `s`,

\[
\mathbb E_y|H_z(Y)-s|^{-1/2}
\le128\Delta_2^{-1/4}. \tag{4.9}
\]

Now apply Lemma 3.1 to the original coordinate `X_0`, conditional on `(Y,Z)`. Its translation

\[
\frac{u^TY+v^TZ}{a}
\]

may be arbitrarily large and correlated with `H_Z(Y)`; Lemma 3.1 is uniform in precisely this translation. For `I=[t,t+h]`,

\[
\Pr\{Q\in I\mid Z=z\}
\le \frac{h}{\sqrt{|a|}}
\mathbb E_y|H_z(Y)-s_I(a)|^{-1/2}
\le128|a|^{-1/2}\Delta_2^{-1/4}h. \tag{4.10}
\]

Integrate in `z`. This proves (4.5).

Finally, an interval bound `\mu(I)<=K|I|` for every interval implies `\mu<<Leb` and `d\mu/dx<=K` almost everywhere (cover null sets by intervals and then use Radon--Nikodym/Lebesgue differentiation). Hence (4.4). `QED`

### Remark 4.2 — why this is genuinely higher-rank

The whole Schur complement `S` need not have rank two or three. The `z`-quadratic form `z^TS_zz z` is completely arbitrary, and `S_yz` is completely arbitrary. Conditioning on `z` turns `S_yz` only into an affine term in the active bank `y`, exactly the perturbation allowed by the orientation-free half-Riesz theorem. Thus arbitrary additional quadratic spectral components survive outside the active grouped rank-two bank.

## 5. Exact application of the assigned partner's mass-linear compiler

Let the outside `z` law be decomposed into arbitrary positive submeasures

\[
\rho=\sum_\alpha \rho_\alpha,
\qquad w_\alpha=\rho_\alpha(\mathbb R^k).
\]

No normalization of `rho_alpha` is performed. Because (4.10) is uniform in every deterministic `z`, the contribution of piece `alpha` is

\[
\nu_\alpha\{Q\in I\}
=\int \Pr\{Q\in I\mid Z=z\}\,d\rho_\alpha(z)
\le w_\alpha\,K|I|, \tag{5.1}
\]

where

\[
K=128|a|^{-1/2}\Delta_2^{-1/4}. \tag{5.2}
\]

Fleet02/B14's `QFORM-MASS-LINEAR-LOCALIZATION-COMPILER-v1` therefore sums (5.1) to the identical global constant `K`, regardless of fragment count, support diameter, distant translations, or moments. This is an actual use of the partner theorem in the target inequality, not a citation-only dependency.

The active variables `(x_0,y)` are deliberately selected before outside localization and are never renormalized on tiny fragments. Thus the normalized-cap barrier in the partner report is avoided exactly.

## 6. Nontrivial target-class family closed uniformly

Let `J_m` denote the `m x m` all-ones matrix and define

\[
B_m=\frac1mJ_m\oplus\left(-\frac1mJ_m\right). \tag{6.1}
\]

Its only nonzero eigenvalues are `+1` and `-1`, so its rank-two pseudo-determinant has absolute value one.

For arbitrary `k`, arbitrary real symmetric `D`, and arbitrary cross block `C`, consider

\[
A=
\begin{pmatrix}
1&0&0\\
0&B_m&C\\
0&C^T&D
\end{pmatrix}. \tag{6.2}
\]

The principal submatrix on the first `1+2m` coordinates is `1\oplus B_m`, with eigenvalues `1,1,-1` and zeros. Cauchy interlacing therefore implies that the full matrix (6.2), **for every `C,D`**, has at least two eigenvalues `>=1` and one eigenvalue `<=-1`. Hence it lies in the exact target class.

Take the first coordinate as scalar pivot. Its Schur complement is the lower block of (6.2); choose the entire `2m`-coordinate bank as `y`. Then `S_yy=B_m`, `|a|=1`, and `Delta_2=1`. Theorem 4.1 gives

\[
\boxed{\|p_{X^TAX}\|_\infty\le128} \tag{6.3}
\]

for every `m,k`, every `C,D`, and every independent cap-one input law, with arbitrary translations, fragments, and unbounded supports.

This contains the familiar singleton-plus-two-banks obstruction `1\oplus J_m/m\oplus(-J_m/m)` as the case `k=0`, but is stable under **arbitrary extra quadratic dimensions and arbitrary couplings from the two-bank core to them**. It therefore demonstrates why a grouped bank can remain strong even when every fixed small physical principal minor is weak.

If in a given application every column of `S_yz` lies in `range(U)`, the sharper source constant `16sqrt(30)` may replace `128`; no such assumption is used in (4.4).

## 7. Relation to current corrections

This theorem does **not**:

- rotate the original independent coordinates and then declare the rotated coordinates independent;
- invoke the false law-uniform pointwise quadratic Fourier envelope;
- normalize thin fragments or conditional spectral slices;
- pay support diameter, location, fragment count, or moments;
- claim that one small physical minor is universally bounded below;
- drop arbitrary additional spectral components.

The active grouped bank remains in original coordinates. Outside variables are conditioned only, so their effect is affine on the bank and an arbitrary scalar shift. This is consistent with the current conditional-cap and small-minor counterexamples.

## 8. What changed and what remains unpaid

### New proved implication, conditional only on the stated source theorem status

A scalar physical pivot plus an **exact-rank-two grouped principal block of its Schur complement** is enough for a density bound even when the rest of the Schur complement has arbitrary rank and arbitrary cross couplings. The outside law can be fragmented/localized with zero tax at the unnormalized mass level.

This removes the need to demand that the entire Schur remainder have rank two. It supplies one concrete instance of the proof-first request for a product-preserving **grouped-coordinate reduction** and one concrete `QFORM-UNNORMALIZED-CURVED-CERTIFICATE` in the partner's terminology.

### First unpaid implication

To reach the full target, one still needs an exhaustive quantitative matrix reduction from the bare spectral hypothesis to one of the already controlled mechanisms. For the present branch this can be stated as:

> Given symmetric `A` with at least three eigenvalues of absolute value at least one, either enter a diffuse/ridge-certified branch, or find an original scalar pivot `a` and a physical coordinate bank `J` such that the Schur principal block `S_JJ` has exact rank two with `|a|^{-1/2} pdet_2(S_JJ)^{-1/4}` universally bounded, or provide another grouped active mechanism with an equally uniform mass-linear certificate.

The existing singleton-plus-two-banks corrections rule out replacing this by a fixed-small-minor criterion. A general exact-rank-two bank is also not forced by the spectral hypothesis. Thus the full QFORM conjecture remains OPEN.

## 9. Status discipline

This report proves the scalar shell lemma and the grouped conditional reduction directly, and applies the assigned partner theorem exactly. Its quantitative analytic constant inherits the source status of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, whose report contains a complete proof but whose stated independent review was pending at the source version read here. No claim of full QFORM completion or independent review is made.
