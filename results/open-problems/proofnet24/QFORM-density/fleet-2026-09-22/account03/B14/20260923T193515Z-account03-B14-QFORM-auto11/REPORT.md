SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T19:35:15Z.
attacking: Lp localization through an arbitrary disjoint quadratic receiver bank with one physical diagonal, sharpening the rough-hub L3 endpoint while preserving arbitrary translations, distant fragments and unbounded supports.

# account03/B14 — exact Lq quadratic-receiver localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T193515Z-account03-B14-QFORM-auto11`  
Control refresh: math-research-brain `133485801d290cfa098b37df20f8655c1d7fd44c`, OWNER CONTROL revision `2026-09-22.15`.  
Status: `SUPPORTING_THEOREM_PROVED / FULL_QFORM_OPEN`.  
Continuity: proved on the branch below; full-target continuity remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. New result

This run proves a zero-tail-cost localization theorem for a whole disjoint quadratic receiver bank. It improves the preceding B14 scalar-square compiler and removes all restrictions on the receiver bank's internal quadratic curvature and internal cross-couplings, except that one untouched original receiver coordinate has a nonzero physical diagonal coefficient.

The result is deliberately formulated in original coordinates. No rotation of the random variables is made.

### Theorem 1 — `QFORM-LP-PHYSICAL-DIAGONAL-RECEIVER-LOCALIZATION-v1`

Let `1<q<2`, `p=q/(q-1)`. Let `W=(W_1,...,W_m)` have independent real probability densities bounded by one. Let `Z` be any random object independent of `W`. Suppose that, conditional on `Z=z`, another random variable `T_z`, built from variables independent of `W`, has a density satisfying

\[
\|p_{T_z}\|_p\le K
\tag{1.1}
\]

for almost every `z`, with the same `K`.

Let `C` be an arbitrary real symmetric `m x m` matrix with one fixed physical diagonal

\[
a=C_{11}\ne0.
\tag{1.2}
\]

Allow completely arbitrary measurable conditioning-generated affine terms `beta(z) in R^m` and `gamma(z) in R`, and set

\[
R_z(W)=W^TCW+\beta(z)^TW+\gamma(z),
\qquad
Q=T_Z+R_Z(W).
\tag{1.3}
\]

Then `Q` has a density and

\[
\boxed{
\|p_Q\|_\infty
\le
K\left(\frac{2^{q-1}}{2-q}\right)^{1/q}
|a|^{-(q-1)/q}.
}
\tag{1.4}
\]

The constant is independent of the receiver dimension, every coefficient of `C` other than the selected diagonal `a`, `beta`, `gamma`, all translations of all input laws, support radii, fragment counts, fragment separations and moments.

For the exponent needed by the current rough-hub core, `q=3/2`, `p=3`, this simplifies to the especially clean bound

\[
\boxed{
\|p_Q\|_\infty\le 2K|a|^{-1/3}.
}
\tag{1.5}
\]

Moreover the density is continuous.

## 2. Exact cap-one Riesz inequality

The only one-dimensional input is an exact bathtub estimate that is itself translation-uniform.

### Lemma 2

If `0<=f<=1`, `int f=1`, and `0<alpha<1`, then for every `s in R`,

\[
\boxed{
\int |x-s|^{-\alpha}f(x)\,dx
\le
\frac{2^\alpha}{1-\alpha}.
}
\tag{2.1}
\]

Proof. The kernel `|x-s|^{-alpha}` is radially decreasing about `s`. Among all densities between zero and one of total mass one, the bathtub principle maximizes its integral by filling the measure-one interval `[s-1/2,s+1/2]`. Thus

\[
\int |x-s|^{-\alpha}f(x)dx
\le2\int_0^{1/2}u^{-\alpha}du
=\frac{2^\alpha}{1-\alpha}.
\]

No moment or support information is used. The constant is attained by the centered unit interval law. `square`

This is a safe use of localization: it optimizes a single decreasing singular kernel, not the full QFORM law and not a Fourier phase.

## 3. Exact Lq estimate for an arbitrarily translated physical square

### Lemma 3

Let `W` have a probability density bounded by one. For any `a!=0` and any real `b,c`,

\[
S=aW^2+bW+c
\]

has a density satisfying, for `1<q<2`,

\[
\boxed{
\|p_S\|_q
\le
\left(\frac{2^{q-1}}{2-q}\right)^{1/q}
|a|^{-(q-1)/q}.
}
\tag{3.1}
\]

Proof. Complete the square. Translation of `W` and translation/reflection of the output reduce to `S=aU^2`. The standard two-sheet change of variables gives the pointwise envelope

\[
p_S(y)\le |a|^{-1/2}|y|^{-1/2}
\tag{3.2}
\]

on the appropriate half-line. Therefore

\[
\begin{aligned}
\|p_S\|_q^q
&=\int p_S(y)^{q-1}\,d\mu_S(y)\\
&\le |a|^{-(q-1)/2}
\mathbb E|S|^{-(q-1)/2}\\
&=|a|^{-(q-1)}\mathbb E|U|^{-(q-1)}\\
&\le |a|^{-(q-1)}\frac{2^{q-1}}{2-q},
\end{aligned}
\tag{3.3}
\]

where the last line is Lemma 2 with `alpha=q-1`. Taking the qth root proves (3.1). For the centered unit-interval law equality holds in (3.3), so the scalar constant is sharp. `square`

In particular,

\[
\boxed{\|p_S\|_{3/2}\le2|a|^{-1/3}.}
\tag{3.4}
\]

This improves the preceding B14 bound `5^(2/3)|a|^(-1/3)`.

## 4. Whole receiver bank: arbitrary internal curvature is free

Fix `z` and condition further on `W_2,...,W_m`. As a function of the untouched original coordinate `W_1`, the receiver in (1.3) is exactly

\[
aW_1^2+B(z,W_{-1})W_1+D(z,W_{-1}).
\tag{4.1}
\]

All receiver self-curvature away from coordinate one, every cross term `W_1W_j`, all cross terms among `W_2,...,W_m`, and all translations have merely entered the arbitrary real coefficients `B,D` after this conditioning. Lemma 3 therefore gives the same conditional Lq bound for every `(z,W_{-1})`.

Averaging these conditional densities and using Minkowski gives

\[
\boxed{
\|p_{R_z}\|_q
\le
\left(\frac{2^{q-1}}{2-q}\right)^{1/q}
|a|^{-(q-1)/q}
}
\tag{4.2}
\]

uniformly in `z`.

Since, conditional on `Z=z`, `T_z` is independent of the complete receiver bank `W`, Young/Hölder convolution gives

\[
\|p_{Q\mid Z=z}\|_\infty
\le \|p_{T_z}\|_p\|p_{R_z}\|_q,
\tag{4.3}
\]

which is (1.4). Averaging over `z` cannot increase the uniform bound.

For each fixed `z`, convolution of an `L^p` function with an `L^q` function for conjugate finite exponents is continuous. The conditional densities are uniformly bounded by the right side of (1.4), so dominated convergence after averaging over `z` proves continuity of the unconditional density as well.

This is the localization point: arbitrary remote fragments and unbounded supports are never truncated or normalized separately. The whole receiver law is retained until the final Lq estimate, so there is no reciprocal fragment-mass or diameter cost.

## 5. Actual application of account04/B14 r9

The designated partner's immutable report is

`yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`.

I use only its still-valid slice-Fourier inequality (3.6), not its later interval-only rough-hub L-infinity inference. In the partner's heavy-null residual-diffuse normal form, the unnormalised frozen slices satisfy

\[
|\widehat\mu_{l,g}(t)|
\le4\sqrt\pi\,|\gamma t|^{-1/2}
\tag{5.1}
\]

uniformly in arbitrary affine leakage, support/tail geometry and dimension.

Write the physical hub coefficient as `L=hV+q_0`. Changing the slice variable multiplies the slice constant by `1/|h|`; hence

\[
|\widehat\mu_l(t)|\le A|t|^{-1/2},
\qquad
A=\frac{4\sqrt\pi}{|h|\sqrt{|\gamma|}}.
\tag{5.2}
\]

Let an arbitrary measurable real hub phase `H(X_0)` be retained and define

\[
T=H(X_0)+2X_0L+Y.
\tag{5.3}
\]

For completeness, the whole-law Plancherel step is as follows. Writing

\[
F_t(l)=\int f_0(x)e^{itH(x)}e^{2itlx}dx,
\]

Plancherel gives

\[
\int|F_t(l)|^2dl
=\frac\pi{|t|}\int f_0(x)^2dx
\le\frac\pi{|t|}.
\tag{5.4}
\]

Also `|mu_hat_l(t)|<=mu_l(R)` and the slice masses integrate to one, so (5.2) implies

\[
\int|\widehat\mu_l(t)|^2dl\le A|t|^{-1/2}.
\tag{5.5}
\]

Cauchy-Schwarz therefore yields the whole-law characteristic bound

\[
\boxed{
|\phi_T(t)|
\le \min\{1,B|t|^{-3/4}\},
\qquad
B=2\pi^{3/4}|h|^{-1/2}|\gamma|^{-1/4}.
}
\tag{5.6}
\]

No pointwise van-der-Corput estimate for an input marginal is used.

Integrating the `3/2` power exactly at the crossover `t_0=B^{4/3}` gives

\[
\int_{\mathbb R}|\phi_T(t)|^{3/2}dt
\le18B^{4/3}.
\tag{5.7}
\]

Inverse Hausdorff-Young, with Fourier convention `phi(t)=int e^{itx}p(x)dx`, then gives

\[
\boxed{
\|p_T\|_3
\le
3^{4/3}2^{8/9}|h|^{-4/9}|\gamma|^{-2/9}.
}
\tag{5.8}
\]

Now append a disjoint original-coordinate receiver bank satisfying (1.3), with arbitrary symmetric internal receiver matrix but with one physical diagonal `a!=0`. Applying Theorem 1 with `p=3,q=3/2` gives the actual partner-derived inequality

\[
\boxed{
\|p_Q\|_\infty
\le
3^{4/3}2^{17/9}
|a|^{-1/3}|h|^{-4/9}|\gamma|^{-2/9}.
}
\tag{5.9}
\]

At `|a|,|h|,|gamma|>=1`, the numerical constant is

\[
3^{4/3}2^{17/9}=16.024108871458075\ldots.
\tag{5.10}
\]

The density on this branch is continuous.

## 6. Exact-target control and quantitative improvement

The preceding B14 run used the target-valid control family

\[
L=\frac{X_1+X_2+X_3+X_4}{2},\qquad
V=\frac{X_1+X_2-X_3-X_4}{2},
\]
\[
Q=2X_0L+\frac12V^2+X_5^2,
\tag{6.1}
\]

for arbitrary independent cap-one `X_0,...,X_5`. The deterministic coefficient vectors defining `L,V` are orthonormal. In the orthonormal deterministic basis `(e_0,L,V,e_5)`, the nonzero spectrum is

\[
\{1,-1,1/2,1\},
\tag{6.2}
\]

so exactly three eigenvalues have modulus at least one. The earlier source identification has `|h|=2^{-1/2}`, `|gamma|=1`, and the disjoint square has `|a|=1`. The sharpened receiver lemma therefore improves the previous branch constant to

\[
\boxed{
\|p_Q\|_\infty
\le3^{4/3}2^{19/9}
=18.69258833188512\ldots,
}
\tag{6.3}
\]

again with a continuous density. The estimate is unchanged under arbitrary translations, fragmentation or unbounded support of any input marginal.

## 7. Scope and remaining implication

This is not the unrestricted conjecture. The bare hypothesis `s_3(A)>=1` does not force a disjoint receiver bank containing a physical diagonal `|a|` bounded below by a universal constant. In particular, a third spectral resource may be entirely overlapping/off-diagonal relative to the rough-hub core, and small physical diagonals may coexist with large global spectral mass.

The new theorem removes a narrower but real obstruction: **once one disjoint physical diagonal is available, every other quadratic coefficient inside that receiver bank, all conditioning-generated shifts, arbitrary remote fragments and all tail geometry are free.** The next B14 problem is therefore an overlapping-third-resource localization that replaces `|a|` by a product-preserving aggregate certificate before conditioning destroys the L3 core.

Full QFORM status: `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity: `OPEN`.

## 8. Correction discipline and sources

Consumed current corrections include the failure of law-uniform pointwise quadratic-phase decay, failure of arbitrary-joint coarea, failure of conditional projection positive-moment shortcuts, failure of fixed-fragment/diameter localization, and the B14 rough-hub warning that an interval-only square-root slice estimate is not a Borel profile. None is used as a premise.

Partner result actually applied at an equation:
- account04/B14 r9, commit `b5f173477a3889ad9432ea7d97767e969c83b279`, equation (3.6), slice-Fourier estimate only.

Previous B14 branch used for the target-valid control family:
- `yspennstate/math-open-problems@78e87f9d9fe723b40aa38e71426458283366f8a5`.

No Gaussian, log-concavity, compact support, connected support, moment, post-rotation independence, or Monte Carlo hypothesis is introduced.
