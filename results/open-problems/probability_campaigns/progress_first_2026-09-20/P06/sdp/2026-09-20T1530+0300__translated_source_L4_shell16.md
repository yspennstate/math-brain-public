Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — translated source `L^4` tail and degree-16 fixed-projector shell

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1432+0300__translated_comparator_galerkin_squeeze.md`, creation commit `9a17d5f6d663f0e8cb6052efb7e8cb2e973fca67`, readback blob `51055afb465ea951efccf24f5da34f1415054945`.

Outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed here.

## 0. New result in one sentence

At the fixed Gibbs point

\[
a_*=0.430159709001947\ldots,\qquad c_*=4a_*=1.72063883600779\ldots,
\]

the **actual degree-16 same-mask Galerkin Newton score** now has the finite-model limits

\[
\boxed{
\nu_{16}^2=0.439112404044658+o_{\mathbf P}(1),
\qquad
\mathbf E_p g_{16}^4=1.069308307545+o_{\mathbf P}(1),
}
\tag{0.1}
\]

and hence

\[
\boxed{K_{16}=5.54563817270+o_{\mathbf P}(1).}
\tag{0.2}
\]

More importantly for the unresolved full-score problem, if `q_16` is the exact translated target mismatch from the previous Galerkin squeeze, then the **source function before the final feature projection** obeys

\[
\boxed{
\left\|{q_{16}\over f}\right\|_{L^2(p)}^2
=2.628730863\times10^{-15}+o_{\mathbf P}(1),
}
\tag{0.3}
\]

and the new fourth-moment estimate

\[
\boxed{
\mathbf E_p\left({q_{16}\over f}\right)^4
\le 2.44\times10^{-13}+o_{\mathbf P}(1),
\qquad
\left\|{q_{16}\over f}\right\|_{L^4(p)}
\le 7.03\times10^{-4}+o_{\mathbf P}(1).
}
\tag{0.4}
\]

Thus the obstruction is no longer an uncontrolled analytic Hermite tail. It is isolated to the `L^4` amplification of **one source-coupled orthogonal projection**

\[
e_{16}=-P_{K_{16}^{\perp,p}}(q_{16}/f).
\tag{0.5}
\]

The full Newton score satisfies

\[
\boxed{
\|e_{16}\|_2^2\le 2.628730863\times10^{-15}+o_{\mathbf P}(1),
}
\tag{0.6}
\]

and it is enough to prove only

\[
\boxed{\|e_{16}\|_4<0.09}
\tag{0.7}
\]

with source-sufficient failure. Equivalently, a source-specific projection amplification below about `128` from the input bound (0.4) already closes the absolute coarse-entry criterion. No worst-case `L^4` norm of the whole random Fourier projector is required or sought.

---

## 1. Inherited translated-comparator identity

Use the previous notation. On odd cyclic order, `u_*` is uniform on the nonzero support, the positive fixed-c seed is

\[
p=fu_*,\qquad
f(z)=e^{-az-a^2/2},
\tag{1.1}
\]

in the Gaussian reference normalization, and `K_R` is the actual same-mask fixed-projector Hermite/convolution Galerkin subspace through degree `R`.

For the restricted Newton score `g_R`, set

\[
D_R=f(1+g_R)-L,
\qquad
q_R=\Pi_*D_R.
\tag{1.2}
\]

The previous report proved the exact target-preserving translated comparator

\[
\widehat L_R=f(1+g_R)-q_R
\tag{1.3}
\]

and the deterministic squeeze

\[
g_N=g_R+e_R,
\qquad
 e_R\perp_p K_R,
\tag{1.4}
\]

\[
\boxed{
 e_R=-P_{K_R^{\perp,p}}(q_R/f),
\qquad
\|e_R\|_p^2=\nu^2-\nu_R^2
\le \epsilon_R:=\mathbf E_*{q_R^2\over f}.
}
\tag{1.5}
\]

Equation (1.5) is the starting point of this run. The new work is to quantify the `L^4` size of the **specific source** `q_R/f` itself and to transport the next finite Galerkin shell exactly.

---

## 2. Degree-16 actual Galerkin fourth moment

The deterministic reference covariance and residual are the inherited matrices

\[
C_R=T_RT_R^T+N_R,
\qquad
N_R=\operatorname{diag}(0,1/2,\ldots,1/2),
\tag{2.1}
\]

with

\[
(T_R)_{11}=1,
\qquad
(T_R)_{kj}
={\binom{k}{j}(-a)^{k-j}\sqrt{j!}\over\sqrt{2k!}}
\quad(2\le k\le R,\ 1\le j\le k),
\tag{2.2}
\]

and

\[
r_1=1-a,
\qquad
r_k={(-a)^k\over\sqrt{2k!}},\quad k\ge2.
\tag{2.3}
\]

Let

\[
h_R=C_R^{-1}r_R,
\qquad
\nu_R^2=r_R^Th_R.
\tag{2.4}
\]

For `R=16`, direct evaluation at `a=a_*` gives

\[
\nu_{16}^2=0.43911240404465807\ldots .
\tag{2.5}
\]

In the calibrated reference representation, write `Y\sim N(0,1)` and `Z=Y-a`. Then the centered degree-R score is

\[
g_R=A_R(Y)+G_R,
\tag{2.6}
\]

where

\[
A_R(Y)=h_1Y+
\sum_{k=2}^R {h_k\over\sqrt2}
{H_k(Y-a)-(-a)^k\over\sqrt{k!}},
\tag{2.7}
\]

and `G_R` is an independent centered Gaussian with variance

\[
\sigma_R^2={1\over2}\sum_{k=2}^R h_k^2.
\tag{2.8}
\]

Hence the fourth moment is the exact one-dimensional Gaussian integral

\[
\mathbf E g_R^4
=
\mathbf E A_R^4
+6\sigma_R^2\mathbf E A_R^2
+3\sigma_R^4.
\tag{2.9}
\]

At `R=16`,

\[
\boxed{
\mathbf E g_{16}^4
=1.069308307544934\ldots,
}
\tag{2.10}
\]

so

\[
\boxed{
K_{16}
={1.069308307544934\ldots\over
 (0.43911240404465807\ldots)^2}
=5.54563817269747\ldots .
}
\tag{2.11}
\]

All quantities in (2.5)--(2.11) use only the fixed degree-16 same-mask convolution dictionary. The inherited fixed-degree Walsh/additive-collision transport with exponential insertion therefore gives, in the **actual finite cyclic model**, with failure `o(1/sqrt(log n))`,

\[
\nu_{16,D}^2=0.439112404044658+o_{\mathbf P}(1),
\tag{2.12}
\]

\[
\mathbf E_{p_D}g_{16,D}^4
=1.069308307545+o_{\mathbf P}(1),
\tag{2.13}
\]

and (0.2).

This is a genuine finite-model theorem; it is not an independent-projector surrogate.

### 2.1 The shell from degree 8 to degree 16 is already harmless

Because the Galerkin spaces are nested,

\[
d_{8,16}:=g_{16}-g_8\perp_p K_8
\]

and

\[
\|d_{8,16}\|_2^2
=\nu_{16}^2-\nu_8^2
=5.39138305\times10^{-10}+o_{\mathbf P}(1).
\tag{2.14}
\]

The same fixed-degree transport applied directly to the shell polynomial gives

\[
\boxed{
\mathbf E_p d_{8,16}^4
=4.081\times10^{-12}+o_{\mathbf P}(1),
\qquad
\|d_{8,16}\|_4
=1.422\times10^{-3}+o_{\mathbf P}(1).
}
\tag{2.15}
\]

Thus the previously unknown `L^4` correction is not hiding in degrees 9--16. It lies, if anywhere, in the genuinely infinite feature-projection remainder after degree 16.

---

## 3. Exact analytic form of the translated source tail

In the reference system the mismatch coefficient in chaos `k>R` is

\[
\rho_k^{(R)}
=r_k-C_{k,1:R}h_R.
\tag{3.1}
\]

For fixed `R`, the inherited translation identities give

\[
\rho_k^{(R)}
={(-a)^k\over\sqrt{2k!}}P_R(k),
\tag{3.2}
\]

where `P_R` is a polynomial of degree at most `R`. Hence every Gaussian exponential moment of the tail converges absolutely.

Write

\[
q_R(Z,W)
={1\over\sqrt2}
\sum_{k>R}\rho_k^{(R)}e_k(Z)
+{1\over\sqrt2}
\sum_{k>R}\rho_k^{(R)}W_k,
\tag{3.3}
\]

where

\[
e_k(Z)={H_k(Z)\over\sqrt{k!}},
\]

and the `W_k` are independent standard Gaussians, independent of `Z`.

Set

\[
A_R(z)={1\over\sqrt2}
\sum_{k>R}\rho_k^{(R)}e_k(z),
\qquad
s_R^2={1\over2}\sum_{k>R}(\rho_k^{(R)})^2.
\tag{3.4}
\]

Conditionally on `Z=z`, `q_R` is Gaussian with mean `A_R(z)` and variance `s_R^2`. Therefore

\[
\mathbf E[q_R^2\mid Z]
=A_R(Z)^2+s_R^2,
\tag{3.5}
\]

\[
\mathbf E[q_R^4\mid Z]
=A_R(Z)^4+6s_R^2A_R(Z)^2+3s_R^4.
\tag{3.6}
\]

These identities allow the source-tail `L^4` problem to be reduced to one-dimensional shifted-Gaussian integrals.

---

## 4. Tilt-shift identities for `q_R/f`

Under the base Gaussian reference law `Z\sim N(0,1)`,

\[
f(Z)=e^{-aZ-a^2/2}.
\tag{4.1}
\]

Under the Gibbs law `p=fu_*`, the reference variable is `Z\sim N(-a,1)`. Completing the square gives the exact identities

\[
\boxed{
\left\|{q_R\over f}\right\|_{L^2(p)}^2
=\mathbf E_*{q_R^2\over f}
=e^{a^2}
\mathbf E_{Z\sim N(a,1)}
\left[A_R(Z)^2+s_R^2\right],
}
\tag{4.2}
\]

and

\[
\boxed{
\left\|{q_R\over f}\right\|_{L^4(p)}^4
=e^{6a^2}
\mathbf E_{Z\sim N(3a,1)}
\left[A_R(Z)^4+6s_R^2A_R(Z)^2+3s_R^4\right].
}
\tag{4.3}
\]

For `R=16`, evaluating the absolutely convergent series in (3.4) at `a=a_*` gives

\[
\boxed{
\epsilon_{16}^{\rm ref}
=2.6287308629\times10^{-15},
}
\tag{4.4}
\]

and

\[
\boxed{
\left\|{q_{16}\over f}\right\|_{4,\rm ref}^4
<2.44\times10^{-13},
\qquad
\left\|{q_{16}\over f}\right\|_{4,\rm ref}
<7.03\times10^{-4}.
}
\tag{4.5}
\]

The inequalities in (4.5) are intentionally rounded upward.

### 4.1 Why (4.4)--(4.5) transport to the same-mask finite model

This step is different from trying to control the final orthogonal projection. The source `q_{16}/f` is an **explicit analytic convolution word**.

Fix a truncation level `L>16` in (3.3). The truncated source is a finite polynomial/exponential insertion in the inherited same-mask dictionary. Therefore its second and fourth moments transport by the fixed-degree collision theorem with failure `o(1/sqrt(log n))`.

For the remainder `k>L`, (3.2) and the factorial `k!` denominator imply absolute convergence after multiplication by every fixed Gaussian exponential weight. The same finite-model bulk subgaussian exponential-moment bounds used in the earlier fixed-c partition theorem dominate the remainder uniformly in `n`. Hence one may first take `n\to\infty` at fixed `L`, then let `L\to\infty` by dominated convergence.

Consequently the **actual finite-model source tail** satisfies

\[
\boxed{
\mathbf E_{p_D}\left({q_{16,D}\over f_D}\right)^2
=2.628730863\times10^{-15}+o_{\mathbf P}(1),
}
\tag{4.6}
\]

\[
\boxed{
\mathbf E_{p_D}\left({q_{16,D}\over f_D}\right)^4
\le2.44\times10^{-13}+o_{\mathbf P}(1),
}
\tag{4.7}
\]

with source-sufficient failure.

This is the main new `L^4` theorem of the run.

---

## 5. The final coarse-entry margin after degree 16

The previous report identified the actual full decrement limit

\[
\nu_*^2=0.439112404044659\ldots,
\qquad
\beta_*=0.378893227408\ldots .
\tag{5.1}
\]

The deterministic criterion `Gamma^2<=K-1` requires

\[
K<1+\beta_*^{-2}
=7.965724841\ldots .
\tag{5.2}
\]

Equivalently, the full fourth moment needs to be below

\[
K_{\rm crit}\nu_*^4
=1.53594870118\ldots .
\tag{5.3}
\]

Taking fourth roots,

\[
(1.53594870118\ldots)^{1/4}
=1.11325377827\ldots .
\tag{5.4}
\]

while the actual degree-16 Galerkin score has

\[
\|g_{16}\|_4
=(1.069308307545\ldots)^{1/4}
=1.01689411792\ldots .
\tag{5.5}
\]

Thus Minkowski leaves the explicit gap

\[
\boxed{
1.11325377827-1.01689411792
=0.09635966035\ldots .
}
\tag{5.6}
\]

Therefore the convenient strict target

\[
\boxed{\|e_{16}\|_4<0.09}
\tag{5.7}
\]

is enough to establish the actual full-score kurtosis criterion.

On the other hand, (4.7) gives

\[
\|q_{16}/f\|_4<7.03\times10^{-4}+o_{\mathbf P}(1).
\tag{5.8}
\]

Since

\[
e_{16}=-P_{K_{16}^{\perp,p}}(q_{16}/f),
\]

it would suffice to prove the **single-source** estimate

\[
\boxed{
\left\|P_{K_{16}^{\perp,p}}(q_{16}/f)\right\|_4
\le 128\left\|q_{16}/f\right\|_4+o_{\mathbf P}(1).
}
\tag{5.9}
\]

Indeed the right side is below `0.09` asymptotically. The exact available ratio from (5.6) and (4.5) is about `137`; `128` is chosen only to keep a strict margin.

This is qualitatively much weaker than bounding the worst-case `L^4` operator norm of the whole selected Fourier projection, which can be large because arbitrary coefficient vectors can create point spikes. Only the translated source in (3.3) matters.

---

## 6. What failed / what this rules out

A tiny `L^2` remainder alone still does **not** imply (5.7): an arbitrary feature-space vector can place its `L^2` mass on a very small set of time points. The report therefore does not claim that (0.6) solves the fourth-moment problem.

Likewise, a worst-case `2->4` bound for the whole selected Fourier subspace is the wrong target. It pays for spike directions unrelated to the source and would erase the enormous analytic-tail margin established in Section 4.

What the new calculation does prove is that the **input** to the remaining projection is already harmless in `L^4`; any counterexample to coarse entry must come from an amplification of more than two orders of magnitude by this one source-coupled weighted projection.

---

## 7. Intermediate-obligation ledger

Fixed full-source metric:

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}
\]

is unchanged.

Current complementary obligations:

1. **DONE:** source-coupled fixed-c decrement identified exactly asymptotically:
   `nu^2 -> 0.439112404044659...`.
2. **DONE:** actual same-mask Galerkin fourth moment through degree 16:
   `K_16 -> 5.54563817270...`.
3. **DONE:** translated source before the final projection has actual
   `L4 <= 7.03e-4+o_P(1)` and `L2^2 <=2.629e-15+o_P(1)`.
4. **OPEN:** prove the one-source projection amplification (5.9), or any direct bound `||e_16||_4<0.09`, with failure `o(1/sqrt(log n))`.
5. **THEN:** `Gamma^2<=K-1` gives absolute contracting coarse entry; invoke the inherited growing-degree superlinear tail and the slightly-stronger-target one-sided certificate.
6. Even-order self-inverse frequency remains untreated.

---

## 8. Next attack

Spend at least 90% useful effort on (5.9), not on another generic covariance-eigenvalue or max-score estimate.

A promising route is to expand the weighted projection equation for the **single source**

\[
e=-P_{K_{16}^{\perp,p}}(q/f)
\]

in the same Hermite/convolution Krylov chain. The finite shells through any fixed degree have exact fourth moments by the existing collision theorem; the shell `8->16` already has `L4=1.422e-3`, and the analytic source tail starts at only `7.03e-4` in `L^4`. Track the Schur-complement correction generated by the fixed projector and prove that its connected fourth-moment diagrams sum to a finite amplification below `128`.

Do this source-wise: pair the four copies of the translated tail first, then sum the fixed-projector resolvent/Krylov insertions. Factorial Hermite coefficients should be kept before diagram counting so that Wick-pairing growth is cancelled by the `sqrt(k!)` normalization. A normalized diagram estimate exponential in total chaos degree is useful; the earlier raw `exp(CR log R)` envelope is unnecessarily wasteful for this Hermite-normalized source.

If direct infinite summation is awkward, prove (5.9) first with projection onto the degree-32 Krylov space and control the remaining Schur complement separately. Do not replace the fixed selected projector by a fresh independent half-projection.

Expectation/high-probability distinctions remain explicit. Any source-closing certificate must still fail with `o(1/sqrt(log n))` so that the inherited `O(sqrt(n log n))` fallback transfers to expectation.
