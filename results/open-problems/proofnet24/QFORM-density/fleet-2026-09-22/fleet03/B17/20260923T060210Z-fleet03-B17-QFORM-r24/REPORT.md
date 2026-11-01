SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T06:02:10Z.
attacking: sharp centered-Gaussian ceiling under the density-one variance floor, with exact partner saturation.

# Sharp centered-Gaussian ceiling at `3 sqrt(2)`

## Status and scope

This report proves a sharp theorem for **centered Gaussian quadratic forms** with a covariance floor, then connects it to the density-one input class through the sharp variance lower bound `Var(X)>=1/12`. It is a supporting theorem and a sharp-witness constraint. It does **not** prove the full arbitrary-input QFORM conjecture, and it does not establish the requested full-target continuity conclusion.


Designated partner result actually applied below: `fleet04/B17`, `yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

---

## 1. Density-one laws have variance at least `1/12`

### Lemma 1 (sharp variance floor)
Let `X` have a probability density `f` with `0<=f<=1`. For every `a in R`,

\[
\mathbb E (X-a)^2 \ge \int_{-1/2}^{1/2}u^2\,du=\frac1{12},
\]

with the convention that an infinite second moment satisfies the inequality. Hence, whenever `Var(X)` is finite,

\[
\boxed{\operatorname{Var}(X)\ge \frac1{12}.}
\]

The constant is sharp, attained by a centered unit interval.

### Proof
For fixed `a`, minimizing `\int (x-a)^2f(x)dx` over `0<=f<=1`, `\int f=1`, is the elementary bathtub problem for the increasing cost `|x-a|^2`. The minimizing density fills the unit-measure sublevel set nearest `a`, namely `1_[a-1/2,a+1/2]`. Thus

\[
\int (x-a)^2f(x)dx\ge \int_{a-1/2}^{a+1/2}(x-a)^2dx=1/12.
\]

Taking `a=EX` when the variance is finite gives the claim. `\square`

A direct consequence is that for independent coordinates with finite variances, the centered covariance matrix `D=diag(Var X_i)` obeys

\[
D\succeq \frac1{12}I.
\]

---

## 2. Sharp Gaussian theorem in arbitrary dimension

### Theorem 2 (sharp centered-Gaussian QFORM ceiling)
Let `G~N(0,\Sigma)` in `R^n`, where

\[
\Sigma\succeq \sigma^2 I_n,\qquad \sigma>0.
\]

Let `A=A^T` have at least three eigenvalues of absolute value at least `1` (equivalently, its third singular value satisfies `s_3(A)>=1`). Then

\[
Q_G=G^T A G
\]

has a bounded continuous density and

\[
\boxed{\|p_{Q_G}\|_\infty\le \frac1{2\sqrt2\,\sigma^2}.}
\]

The constant is sharp. In rank three, equality is attained for

\[
\Sigma=\sigma^2 I_3,\qquad A=\operatorname{diag}(1,1,-1)
\]

and its orthogonal conjugates (or the global sign reversal).

At the density-one variance floor `\sigma^2=1/12`,

\[
\boxed{\|p_{Q_G}\|_\infty\le 3\sqrt2.}
\]

### Step 2.1: covariance whitening preserves three strong quadratic modes
Write `G=\Sigma^{1/2}Z`, `Z~N(0,I_n)`, and

\[
B=\Sigma^{1/2}A\Sigma^{1/2}.
\]

For every singular-value index `k`,

\[
s_k(A)=s_k(\Sigma^{-1/2}B\Sigma^{-1/2})
\le \|\Sigma^{-1/2}\|^2 s_k(B)
\le \sigma^{-2}s_k(B).
\]

Therefore

\[
\boxed{s_3(B)\ge \sigma^2s_3(A)\ge \sigma^2.}
\]

Since `B` is symmetric, at least three eigenvalues of `B` have absolute value at least `\sigma^2`. Orthogonally diagonalize `B`; rotational invariance of `Z` makes the resulting Gaussian coordinates independent standard normals. Select any three strong eigenvalues. The remaining quadratic terms are independent of this selected triple, so convolution with them cannot raise an `L^infinity` density bound. It is therefore enough to prove the theorem for a three-term standard-Gaussian quadratic form whose three coefficient magnitudes are at least `\sigma^2`.

---

## 3. The three-mode lemma: all signatures

Let `Z_1,Z_2,Z_3` be iid `N(0,1)` and let all displayed positive coefficients be at least `\sigma^2`.

### 3A. Same-sign triple
Consider

\[
S=\alpha Z_1^2+\beta Z_2^2+\gamma Z_3^2,
\qquad \alpha,\beta,\gamma\ge\sigma^2.
\]

Put `M=max(alpha,beta,gamma)`. With the change of variables

\[
y=(\sqrt\alpha z_1,\sqrt\beta z_2,\sqrt\gamma z_3),
\]

coarea on the Euclidean sphere gives, for `s>0`,

\[
p_S(s)=
\frac{\sqrt s}{2(2\pi)^{3/2}\sqrt{\alpha\beta\gamma}}
\int_{\mathbb S^2}
\exp\!\left[-\frac s2\left(\frac{\omega_1^2}{\alpha}+\frac{\omega_2^2}{\beta}+\frac{\omega_3^2}{\gamma}\right)\right]d\omega.
\]

Because the parenthesis is at least `1/M`,

\[
p_S(s)\le
\frac{\sqrt s}{\sqrt{2\pi\alpha\beta\gamma}}e^{-s/(2M)}.
\]

The right-hand side is maximized at `s=M`. If, say, `M=alpha`,

\[
\|p_S\|_\infty
\le \frac{e^{-1/2}}{\sqrt{2\pi\beta\gamma}}
\le \frac1{\sqrt{2\pi e}\,\sigma^2}.
\]

Since `\pi e>4`,

\[
\frac1{\sqrt{2\pi e}}<\frac1{2\sqrt2},
\]

so every same-sign triple is strictly below the claimed universal Gaussian ceiling. Three negative coefficients reduce to this case by reflection.

The displayed formula also shows continuity at the support edge: `p_S(s)=O(\sqrt s)` as `s downarrow 0`.

### 3B. Indefinite triple
Now consider

\[
T=\alpha Z_1^2+\beta Z_2^2-\gamma Z_3^2,
\qquad \alpha,\beta,\gamma\ge\sigma^2.
\]

Assume without loss of generality `alpha>=beta`. Let

\[
U=\alpha Z_1^2+\beta Z_2^2,
\qquad V=\gamma Z_3^2.
\]

The density of `U` is the exact Bessel formula

\[
h(u)=\frac1{2\sqrt{\alpha\beta}}
\exp\!\left[-\frac u4\left(\frac1\alpha+\frac1\beta\right)\right]
I_0\!\left(\frac u4\left(\frac1\beta-\frac1\alpha\right)\right),
\qquad u>0.
\]

Set

\[
a=\frac14\left(\alpha^{-1}+\beta^{-1}\right),
\qquad b=\frac14\left(\beta^{-1}-\alpha^{-1}\right)\ge0.
\]

Since `I_1(x)<I_0(x)` for `x>0` and `b<a`,

\[
h'(u)=\frac{e^{-au}}{2\sqrt{\alpha\beta}}
[-aI_0(bu)+bI_1(bu)]<0.
\]

Thus `h` is decreasing. The density

\[
k(v)=\frac{e^{-v/(2\gamma)}}{\sqrt{2\pi\gamma v}},\qquad v>0,
\]

of `V` is also decreasing.

For `s>=0`,

\[
p_T(s)=\int_0^\infty h(s+v)k(v)dv\le p_T(0),
\]

and for `r>0`,

\[
p_T(-r)=\int_0^\infty h(u)k(u+r)du\le p_T(0).
\]

Hence

\[
\boxed{\|p_T\|_\infty=p_T(0).}
\]

At zero,

\[
p_T(0)=\frac1{2\sqrt{2\pi\alpha\beta\gamma}}
\int_0^\infty u^{-1/2}e^{-Au}I_0(bu)du,
\]

where

\[
A=a+\frac1{2\gamma}.
\]

Using the elementary integral representation `I_0(x)=pi^{-1}\int_0^\pi e^{x\cos\theta}d\theta`, hence `I_0(x)<=e^x`, gives

\[
p_T(0)
\le
\frac1{2\sqrt{2\pi\alpha\beta\gamma}}
\int_0^\infty u^{-1/2}e^{-(A-b)u}du.
\]

Since

\[
A-b=\frac1{2\alpha}+\frac1{2\gamma},
\]

and `\int_0^\infty u^{-1/2}e^{-cu}du=\sqrt{\pi/c}`,

\[
\boxed{
\|p_T\|_\infty
\le \frac1{2\sqrt{\beta(\alpha+\gamma)}}
\le \frac1{2\sqrt2\,\sigma^2}.
}
\]

The signature `(1,2)` follows by reflection.

For `alpha=beta=gamma=sigma^2`, `b=0`, every inequality above is equality and

\[
\boxed{\|p_T\|_\infty=p_T(0)=\frac1{2\sqrt2\,\sigma^2}.}
\]

The difference density is continuous: away from zero this follows directly from the integral formulas; at zero, the positive- and negative-side formulas converge to the same finite integral by monotone/dominated convergence. It vanishes at infinity. Therefore convolution with any independent residual quadratic law preserves continuity and cannot increase the sup norm.

This completes Theorem 2. `\square`

---

## 4. Consequence for density-one Gaussian surrogates

Suppose independent cap-one inputs have finite variances and form

\[
D=\operatorname{diag}(\operatorname{Var}X_1,\ldots,\operatorname{Var}X_n).
\]

By Lemma 1,

\[
D\succeq \frac1{12}I.
\]

Therefore the **centered matching Gaussian quadratic surrogate** `G^T A G` with `G~N(0,D)` obeys

\[
\boxed{\|p_{G^T A G}\|_\infty\le3\sqrt2}
\]

for every symmetric `A` with at least three eigenvalues of absolute value at least one.

This statement is deliberately about the centered Gaussian surrogate. It does not silently center the original QFORM inputs and it does not claim that a nonzero Gaussian mean can simply be dropped from a quadratic form. Its use is to constrain CLT/local-limit witness mechanisms: covariance anisotropy above the density-one variance floor cannot make a centered Gaussian endpoint exceed `3sqrt(2)`.

---

## 5. Designated-partner saturation: an actual inequality

The completed `fleet04/B17` result constructs, for every `m`, a source-valid cap-one rotated witness from three independent `m`-variable centered-uniform banks and the rational orthogonal matrix

\[
O=\frac17\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\]

Its physical matrix has exact nonzero spectrum `{1,1,-1}`, and its effective bank-level matrix is

\[
O^T\operatorname{diag}(1,1,-1)O
=\frac1{49}
\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix},
\]

with every entry nonzero. The partner proves the finite local expansion

\[
\boxed{
p_{Q_m}(0)
=3\sqrt2\left(1-\frac{5295}{21952m}+O(m^{-2})\right).
}
\]

Each normalized centered-uniform bank has variance `1/12`; the three-bank CLT endpoint is therefore isotropic Gaussian with covariance `(1/12)I_3`. Because the effective matrix is orthogonally similar to `diag(1,1,-1)`, Theorem 2 gives the sharp endpoint inequality

\[
\|p_{Q_\infty}\|_\infty\le3\sqrt2.
\]

The partner expansion gives the reverse saturation statement

\[
\lim_{m\to\infty}p_{Q_m}(0)=3\sqrt2.
\]

Hence

\[
\boxed{
3\sqrt2
=\sup\{\|p_{G^T A G}\|_\infty:
G\sim N(0,\Sigma),\ \Sigma\succeq I/12,\ s_3(A)\ge1\},
}
\]

and the supremum is approached by **actual admissible cap-one, genuinely rotated, finite-dimensional product inputs** through the partner family.

This is the promised application of a completed partner result to an actual inequality: the partner lower-bound family exactly saturates the new Gaussian upper envelope.

---

## 6. Sharp-witness implications

1. **No centered Gaussian covariance trick can beat `3sqrt(2)`.** Once the covariance floor forced by `f_i<=1` is respected, arbitrary anisotropy and arbitrary additional Gaussian quadratic modes cannot raise the density above `3sqrt(2)`.

2. **Same-sign Gaussian triples are not extremal.** They satisfy the stronger bound

\[
\|p\|_\infty\le \frac1{\sqrt{2\pi e}\,\sigma^2},
\]

which at `sigma^2=1/12` is

\[
\frac{12}{\sqrt{2\pi e}}=2.903648694229720\ldots<3\sqrt2.
\]

Thus the sharp Gaussian obstruction is necessarily indefinite.

3. **Any source-valid witness above `3sqrt(2)` must exploit a genuinely non-Gaussian local mechanism.** It cannot arise solely from a covariance-preserving centered CLT endpoint. Candidate mechanisms would have to involve non-Gaussian finite-scale concentration, nonzero-mean/affine effects not removable by centering, or a failure of uniform local-limit control.

4. The partner coefficient

\[
\frac{5295}{21952}=0.241208090379\ldots>0
\]

shows its exact dense rotated witness approaches the Gaussian ceiling from below.

---

## 7. Checks

Deterministic arithmetic used in the sibling checker:

- `1/(2 sqrt(2) (1/12)) = 3 sqrt(2) = 4.242640687119285...`;
- same-sign ceiling at `sigma^2=1/12` is `12/sqrt(2 pi e)=2.903648694229720...`;
- partner first correction coefficient is `5295/21952=0.24120809037900875...`;
- the mixed-sign bound was numerically cross-checked on several coefficient triples by direct quadrature of the exact Bessel integral, always below `1/[2 sqrt(min(alpha,beta)(max(alpha,beta)+gamma))]`, with equality at `(1,1,1)` after normalization.

No Monte Carlo or histogram inference is used in any proof.

---

## 8. What remains open

The full QFORM target remains **OPEN / NOT PROVED**. The theorem above only identifies the exact sharp ceiling for centered Gaussian surrogates and shows the known source-valid rotated witness saturates it. It does not control arbitrary cap-one inputs at finite dimension, arbitrary translations/nonzero means, or the local-limit error needed to replace an arbitrary product law by a Gaussian surrogate. Full-target continuity also remains open.

The next nonredundant B17 sharp-witness question is therefore: can an explicitly non-Gaussian, multiscale rotated product law produce a finite-dimensional peak strictly above `3sqrt(2)`, or can one prove a sharp comparison/local-limit inequality showing that `3sqrt(2)` remains the global constant?

Status: `NEW_SUPPORTING_THEOREM`; `WITHOUT_VERIFIED_BRAIN`.
