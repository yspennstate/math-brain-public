# QFORM B17 — exact one-heavy-minority reduction and strict mixed-leverage gap

Run: `20260923T010156Z-fleet03-B17-QFORM-r21`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control observed before work: revision `2026-09-22.15`.  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM remains **OPEN / NOT PROVED**.  
Continuity: proved below for the explicit bank family for `m>=2`; no full-target continuity claim is made.

## Executive result

There is a natural mixed-leverage escape from the previously completed infinitesimal-frame analysis: keep one physical coordinate fully localized while Gaussianizing the other two active directions. This report closes the case in which the localized coordinate is the **minority-sign direction**, and it does so sharply with respect to its arbitrary cap-one law.

Let `Y_1,Y_2` be independent with even densities `g_1,g_2` nonincreasing on `[0,infinity)`, let

\[
U=Y_1^2+Y_2^2,
\]

and let `X` be independent with an arbitrary probability density `0<=f<=1`. Write `h` for the density of `U`. Then `h` is nonincreasing and

\[
\boxed{
\|p_{U-X^2}\|_\infty\le C(g_1,g_2):=2\int_0^{1/2}h(v^2)\,dv.
}
\tag{1}
\]

The bound is **sharp over the entire cap-one class for the heavy coordinate**: equality is attained at output level zero by

\[
f=\mathbf 1_{[-1/2,1/2]}.
\]

Thus arbitrary fragmentation, disconnected support and remote translations of the one localized minority-sign coordinate do not help at all in this branch.

Apply (1) to two normalized `m`-fold centered-uniform banks

\[
Y_{j,m}=m^{-1/2}\sum_{k=1}^m X_{jk},\qquad X_{jk}\sim\mathrm{Unif}[-1/2,1/2],\quad j=1,2,
\]

and an arbitrary independent cap-one heavy coordinate `X_0`. The physical matrix is

\[
A_m=\operatorname{diag}(J_m/m,J_m/m,-1),
\]

so its exact nonzero spectrum is `{1,1,-1}` for every `m`. If `h_m` is the density of `Y_{1,m}^2+Y_{2,m}^2`, then

\[
\boxed{
\sup_{0\le f_{X_0}\le1}\|p_{Y_{1,m}^2+Y_{2,m}^2-X_0^2}\|_\infty
=C_m:=2\int_0^{1/2}h_m(v^2)\,dv.
}
\tag{2}
\]

Using the completed weighted local Edgeworth expansion of the designated partner `fleet04/B17`,

\[
\boxed{
C_m=C_\infty-\frac{\kappa}{m}+O(m^{-2}),
}
\tag{3}
\]

where

\[
C_\infty=\sqrt{6\pi}\,\operatorname{erf}\!\left(\sqrt{\frac32}\right)
=3.9801056750420088339\ldots,
\tag{4}
\]

and

\[
\kappa=\frac9{20}e^{-3/2}+\frac9{80}C_\infty
=0.5481704605090194168\ldots>0.
\tag{5}
\]

Moreover, analytically (not numerically),

\[
\boxed{C_\infty<3\sqrt2.}
\tag{6}
\]

Therefore this exact mixed-leverage branch has a strict asymptotic gap below the established universal lower-bound obstruction `3 sqrt(2)`. A witness above `3 sqrt(2)` cannot arise merely by replacing the minority-sign diffuse bank by one fully localized arbitrary cap-one coordinate while leaving the two same-sign banks in their minimum-variance Gaussian regime.

The complementary branch in which the heavy coordinate belongs to the **majority-sign pair** is not closed by this argument and remains a legitimate stress mechanism.

---

## 1. Monotonicity of the same-sign two-square density

Let `Y_1,Y_2` be independent with even densities `g_1,g_2` that are nonincreasing on `[0,infinity)`. In polar coordinates, for `u>0`, the density of

\[
U=Y_1^2+Y_2^2
\]

is

\[
h(u)=\frac12\int_0^{2\pi}
 g_1(\sqrt u\cos\theta)g_2(\sqrt u\sin\theta)\,d\theta.
\tag{7}
\]

Indeed, writing `(y_1,y_2)=(r cos theta,r sin theta)` and `u=r^2`, the Jacobian is `r dr dtheta=(1/2)du dtheta`.

For each fixed `theta`, both absolute arguments in (7) increase with `u`. Since the `g_j` are even and nonincreasing in absolute value, the integrand is nonincreasing in `u`. Therefore

\[
\boxed{h\text{ is nonincreasing on }[0,\infty).}
\tag{8}
\]

For the normalized sums of centered uniforms used later, `g_m` is even and unimodal because convolution preserves symmetric unimodality; scaling preserves it as well. For `m>=2`, `g_m` is continuous, hence `h_m` is bounded and continuous.

---

## 2. Sharp optimization over the arbitrary heavy cap-one law

Let `X` be independent of `U`, with probability density `f` satisfying `0<=f<=1`. For

\[
Q=U-X^2,
\]

conditioning on `X=x` gives the density representative

\[
p_Q(s)=\int_{\mathbb R}f(x)h(s+x^2)\mathbf 1_{\{s+x^2\ge0\}}\,dx.
\tag{9}
\]

We optimize this linear functional over every admissible `f`, without imposing connected support or a fragment-count bound.

### Case A: `s>=0`

The kernel

\[
k_s(x)=h(s+x^2)
\]

is even and nonincreasing in `|x|`. Among all `0<=f<=1` of total mass one, the bathtub/rearrangement principle therefore gives

\[
p_Q(s)\le\int_{-1/2}^{1/2}h(s+x^2)\,dx
\le2\int_0^{1/2}h(x^2)\,dx.
\tag{10}
\]

The second inequality uses monotonicity of `h`.

### Case B: `s=-r<0`

Now the kernel vanishes on `|x|<sqrt(r)` and, on each exterior ray, decreases as one moves away from the threshold `|x|=sqrt(r)`. Hence its measure-one superlevel optimizer is exactly the pair of adjacent half-length intervals

\[
[-\sqrt r-1/2,-\sqrt r]\cup[\sqrt r,\sqrt r+1/2].
\]

Consequently

\[
\begin{aligned}
p_Q(-r)
&\le2\int_{\sqrt r}^{\sqrt r+1/2}h(x^2-r)\,dx\\
&=2\int_0^{1/2}h(u^2+2\sqrt r\,u)\,du\\
&\le2\int_0^{1/2}h(u^2)\,du.
\end{aligned}
\tag{11}
\]

Again only monotonicity of `h` is used.

Combining (10) and (11) proves (1).

For `s=0` and `f=1_{[-1/2,1/2]}` we have equality:

\[
p_Q(0)=2\int_0^{1/2}h(x^2)\,dx.
\tag{12}
\]

Therefore the constant in (1) is the exact optimum over **all** cap-one laws of the heavy coordinate, including arbitrarily fragmented ones. This is a genuine extremality statement for this branch; it does not assert interval extremality for the full rotated QFORM problem.

If `h` is bounded continuous (as for the bank family with `m>=2`), formula (9) and dominated convergence give a continuous representative of `p_Q` for every admissible heavy `f`.

---

## 3. Exact target-admissible finite-dimensional family

Let

\[
P_m=J_m/m.
\]

Take two independent `m`-coordinate banks and one additional independent coordinate. Set

\[
A_m=\operatorname{diag}(P_m,P_m,-1).
\tag{13}
\]

Each `P_m` has spectrum `{1,0,...,0}`, so

\[
\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.
\tag{14}
\]

With

\[
Y_{j,m}=m^{-1/2}\sum_{k=1}^mX_{jk},
\]

we have exactly

\[
X^TA_mX=Y_{1,m}^2+Y_{2,m}^2-X_0^2.
\tag{15}
\]

The first `2m` physical inputs are centered unit intervals and `X_0` is arbitrary with density cap one. Thus (2) is an exact finite-dimensional target statement, not a Gaussian-input example.

At `m=1`, `h_1(u)=pi` for `0<=u<=1/4`, so

\[
C_1=\pi,
\]

recovering the diagonal control. As `m` grows, the two banks move into the Gaussian regime, but the heavy minority-sign coordinate remains fully localized.

---

## 4. Partner-applied local Edgeworth calculation

The completed designated-partner result is:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

Its weighted one-dimensional local Edgeworth lemma states, for the normalized centered-uniform bank density `g_m`, with `sigma^2=1/12`,

\[
g_m(y)=\gamma_\sigma(y)
\left[1-\frac1{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8},
\tag{16}
\]

where `H_4(z)=z^4-6z^2+3`.

Insert (16) into (7). On the circle `y_1^2+y_2^2=u`, the Gaussian product is constant and yields

\[
h_\infty(u)=\frac1{2\sigma^2}e^{-u/(2\sigma^2)}=6e^{-6u}.
\tag{17}
\]

The angular average of the first Edgeworth polynomial is

\[
\begin{aligned}
&\frac1{2\pi}\int_0^{2\pi}
\left[H_4\!\left(\frac{\sqrt u\cos\theta}{\sigma}\right)
+H_4\!\left(\frac{\sqrt u\sin\theta}{\sigma}\right)\right]d\theta\\
&\qquad=\frac34q^4-6q^2+6,
\qquad q^2=u/\sigma^2=12u\\
&\qquad=108u^2-72u+6.
\end{aligned}
\tag{18}
\]

Therefore, uniformly for `u` in the compact interval `[0,1/4]`,

\[
h_m(u)=6e^{-6u}
\left[1-\frac{108u^2-72u+6}{20m}\right]
+O(m^{-2}).
\tag{19}
\]

Substitute `u=v^2` into (2):

\[
C_m=12\int_0^{1/2}e^{-6v^2}\,dv
-\frac{12}{20m}\int_0^{1/2}e^{-6v^2}
(108v^4-72v^2+6)\,dv
+O(m^{-2}).
\tag{20}
\]

The first integral is

\[
C_\infty=\sqrt{6\pi}\,\operatorname{erf}(\sqrt{3/2}).
\tag{21}
\]

The weighted integral evaluates exactly to

\[
12\int_0^{1/2}e^{-6v^2}(108v^4-72v^2+6)\,dv
=9e^{-3/2}+\frac94C_\infty.
\tag{22}
\]

Equations (20)--(22) prove (3)--(5). In particular the first finite-bank correction is negative, so this branch approaches its mixed-leverage limiting ceiling from below.

This is an actual application of the completed partner theorem to the exact sharp heavy-coordinate inequality (2), not a restatement of the partner's three-diffuse-bank witness.

---

## 5. Analytic strict comparison with `3 sqrt(2)`

The comparison in (6) can be proved without decimal arithmetic. For `x>=0`, define

\[
R(x)=\frac{2x}{\sqrt\pi\sqrt{1+2x^2/3}}-\operatorname{erf}(x).
\]

Then `R(0)=0` and

\[
R'(x)=\frac2{\sqrt\pi}
\left[(1+2x^2/3)^{-3/2}-e^{-x^2}\right]\ge0,
\tag{23}
\]

because

\[
\frac32\log(1+2x^2/3)\le x^2.
\]

Hence

\[
\operatorname{erf}(x)
\le\frac{2x}{\sqrt\pi\sqrt{1+2x^2/3}},
\tag{24}
\]

strictly for `x>0`. At `x=sqrt(3/2)`, (24) becomes

\[
\operatorname{erf}(\sqrt{3/2})<\sqrt{3/\pi}.
\]

Multiplying by `sqrt(6 pi)` gives

\[
C_\infty<\sqrt{6\pi}\sqrt{3/\pi}=3\sqrt2.
\]

Numerically the strict gap is

\[
3\sqrt2-C_\infty
=0.2625350120772763124\ldots.
\tag{25}
\]

---

## 6. What this rules out and what remains

This closes a specific mixed-leverage mechanism left open by the infinitesimal-frame ceiling:

* two same-sign active directions may be completely diffuse and Gaussianized at the minimum cap-one variance;
* the opposite-sign active direction may remain a single fully localized physical coordinate;
* that heavy coordinate may have **any** density bounded by one, with arbitrary fragmentation and translations;
* nevertheless its optimal output-density peak is asymptotically `C_infty<3 sqrt(2)`, and the exact finite-bank optimum over the heavy law is (2).

So one localized **minority-sign** coordinate cannot improve the known lower bound.

This does **not** close:

1. one heavy coordinate in the majority-sign pair (the kernel is then the logarithmically singular difference-of-two-squares density and the same monotone argument no longer applies);
2. two or more non-infinitesimal rows with shared-coordinate coupling;
3. multiscale fragmented heavy rows coupled to nonseparable residual spectrum;
4. the unrestricted universal upper bound or full-target continuity.

The most informative next B17 witness search is therefore the majority-sign one-heavy-row optimization, where the heavy cap-one law sees the exact kernel of a diffuse opposite-sign Gaussian pair. If that kernel's measure-one bathtub optimum can be bounded by `3 sqrt(2)`, then the entire one-heavy-row aligned escape is closed; if not, it may produce a new lower bound.

## Integrity notes

No pointwise law-uniform van-der-Corput estimate, post-rotation independence claim, arbitrary-joint coarea lemma, conditional-density cap, bounded fragment-count reduction, one-minor inversion, or Monte Carlo histogram is used. The only numerical values reported above evaluate exact analytic formulas. The full QFORM conjecture remains open.
