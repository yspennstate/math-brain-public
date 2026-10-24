# QFORM B17 — one-heavy majority-sign Gaussian-completion branch is strictly below `3 sqrt(2)`

Run: `B17-20260923T014533Z-r14-multiscale`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM remains **OPEN / NOT PROVED**.  
Continuity of the full target remains separate.  

## 1. The exact unpaid branch

The designated partner `account03/B17` has completed the one-heavy **minority-sign** branch. Its theorem says that if the two same-sign directions are symmetric-unimodal and the minority-sign direction is one arbitrary cap-one coordinate, then the heavy law is optimized by the centered unit interval; for two diffuse centered-uniform banks the limiting sharp branch value is

\[
\sqrt{6\pi}\,\operatorname{erf}(\sqrt{3/2})
=3.9801056750420088\ldots<3\sqrt2.
\]

Source actually read and used: `yspennstate/math-open-problems@9661cb6a0a2ab0075e8b7f62145a7af3c147c243`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T010156Z-account03-B17-QFORM-r21/REPORT.md`.

The complementary one-heavy placement is the majority-sign direction. The exact source-valid finite family is

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m).
\tag{1}
\]

Every `J_m/m` has spectrum `{1,0,...,0}`, hence every finite `A_m` has exact nonzero spectrum

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.}
\tag{2}
\]

Put an arbitrary independent cap-one density on the singleton coordinate `X`, and iid `Unif[-1/2,1/2]` variables on the two `m`-coordinate banks. With

\[
S_{\pm,m}=m^{-1/2}\sum_{k=1}^m U_{\pm,k},
\]

we have exactly

\[
X_{\rm phys}^T A_m X_{\rm phys}=X^2+S_{+,m}^2-S_{-,m}^2.
\tag{3}
\]

Thus no spectral rotation or post-rotation independence assumption is being used. The physical inputs are genuinely independent and each has density at most one.

As `m->infinity`, the two banks converge to independent `N(0,1/12)` variables. The still-unpaid limiting mechanism is therefore

\[
Q_\infty=X^2+G_+^2-G_-^2,
\qquad G_\pm\stackrel{iid}{\sim}N(0,1/12),
\tag{4}
\]

with **arbitrary** independent cap-one law for `X`.

The theorem below closes this limiting mechanism strictly below the existing lower-bound scale `3 sqrt(2)`.

---

## 2. Main theorem

### QFORM-ONE-HEAVY-MAJORITY-GAUSSIAN-NOESCAPE-v1

Let `X` have any probability density `0<=f<=1`, and let `G_+,G_-` be independent `N(0,1/12)`, independent of `X`. Then `Q_infty` in (4) has an essentially bounded density and

\[
\boxed{
\|p_{Q_\infty}\|_\infty
\le C_*:=\frac6\pi\left(\frac52+\log\frac43-\gamma\right)
<3\sqrt2.
}
\tag{5}
\]

Numerically only for orientation,

\[
C_*=4.2216798636024726412\ldots,
\qquad
3\sqrt2=4.2426406871192851464\ldots .
\tag{6}
\]

The gap in (5) is analytic; the decimals are not used in the proof.

This theorem optimizes over **all** cap-one heavy laws at each output level through the bathtub principle. It therefore allows disconnected supports, remote translations and arbitrarily many fragments. It is not an assertion that centered intervals are globally extremal for QFORM.

---

## 3. Exact product-normal kernel

Set

\[
D=G_+^2-G_-^2=(G_++G_-)(G_+-G_-).
\]

The two factors on the right are independent `N(0,1/6)` variables. Hence `D` has the standard product-normal density

\[
\boxed{
d(w)=\frac6\pi K_0(6|w|),
}
\tag{7}
\]

where `K_0` is the modified Bessel function. It is even and strictly decreasing in `|w|>0`.

Conditioning on `X=x`, for every output `s`,

\[
p_{Q_\infty}(s)=\int_{\mathbb R} f(x)d(s-x^2)\,dx.
\tag{8}
\]

For fixed `s`, the kernel `x -> d(|s-x^2|)` is nonnegative. Maximizing (8) over all `0<=f<=1` with total mass one is exactly the one-dimensional bathtub problem: take a measure-one top superlevel set of that kernel. Since `d` decreases with `|s-x^2|`, this means taking the measure-one set of points closest to the level `x^2=s`.

For `s<0`, that set is

\[
E_s=[-1/2,1/2].
\tag{9}
\]

For `s>=0`, define

\[
m_s(r)=|\{x:\ |x^2-s|\le r\}|.
\]

When `r<s`,

\[
m_s(r)=2\left(\sqrt{s+r}-\sqrt{s-r}\right),
\tag{10}
\]

while for `r>=s`, `m_s(r)=2\sqrt{s+r}`. Solving `m_s(r)=1` yields two regimes:

* if `0<=s<=1/8`, the threshold is `r=1/4-s>=s` and again
  \[
  E_s=[-1/2,1/2];
  \tag{11}
  \]
* if `s>=1/8`,
  \[
  E_s=[-a,-b]\cup[b,a],
  \qquad a-b=1/2,\quad a^2+b^2=2s,
  \tag{12}
  \]
  equivalently
  \[
  b=\frac{-1+\sqrt{16s-1}}4,\qquad a=b+\frac12.
  \tag{13}
  \]

Thus the exact cap-one optimum at level `s` is

\[
F(s):=\sup_{0\le f\le1,\int f=1}p_{Q_\infty}(s)
=\int_{E_s}d(|s-x^2|)\,dx.
\tag{14}
\]

No fixed-fragment-count assumption is made; the two intervals in (12) arise here from the exact geometry of this one specific kernel, not from a claimed universal localization theorem.

---

## 4. Negative outputs and the small-positive window

For `s<0`, monotonicity of `d` gives pointwise

\[
d(|s|+x^2)\le d(x^2),
\]

so

\[
F(s)\le F(0).
\tag{15}
\]

It remains to treat `0<=s<=1/8`, where the optimizer is still the centered unit interval.

We use a global elementary upper bound for `K_0`. From

\[
K_0(z)=\int_1^\infty \frac{e^{-zt}}{\sqrt{t^2-1}}\,dt,
\qquad
E_1(z)=\int_1^\infty \frac{e^{-zt}}t\,dt,
\]

we have

\[
K_0(z)-E_1(z)
\le \int_1^\infty\left(\frac1{\sqrt{t^2-1}}-\frac1t\right)dt
=\log2.
\tag{16}
\]

Also

\[
E_1(z)=-\gamma-\log z+\int_0^z\frac{1-e^{-u}}u\,du
\le -\gamma-\log z+z.
\tag{17}
\]

Therefore, for every `z>0`,

\[
\boxed{K_0(z)\le-\log(z/2)-\gamma+z.}
\tag{18}
\]

Set `b=1/2`, `a=sqrt(s)`. From (7), (11) and (18),

\[
F(s)\le U(s):=\frac6\pi\{J(s)-\log3-\gamma+6A(s)\},
\tag{19}
\]

where

\[
J(s)=\int_{-b}^b-\log|s-x^2|\,dx,
\qquad
A(s)=\int_{-b}^b|s-x^2|\,dx.
\tag{20}
\]

For `0<=a<b`, direct integration gives

\[
J(a^2)
=-2\left[(b-a)\log(b-a)+(b+a)\log(b+a)-2b\right]
\tag{21}
\]

and

\[
A(a^2)=\frac{2b^3}{3}+\frac{8a^3}{3}-2a^2b.
\tag{22}
\]

Hence, up to the positive constant `6/pi`, the derivative of the nonconstant part of `U` is

\[
B'(a)
=-2\log\frac{b+a}{b-a}+24a(2a-b).
\tag{23}
\]

For `0<=a<=b/2`, both terms in (23) are nonpositive. For `b/2<=a<=b/sqrt(2)`, write `x=a/b=2a`; then

\[
B'(a)=-4\operatorname{artanh}x+12x(x-1/2).
\tag{24}
\]

Since `artanh x>=x` and here `x<=1/sqrt(2)<5/6`,

\[
3x(x-1/2)\le x\le\operatorname{artanh}x,
\]

which again gives `B'(a)<=0`. Therefore

\[
U(s)\le U(0),\qquad 0\le s\le1/8.
\tag{25}
\]

At zero,

\[
J(0)=2+2\log2,
\qquad
A(0)=\frac1{12},
\]

so

\[
\boxed{
U(0)=\frac6\pi\left(\frac52+\log\frac43-\gamma\right)=C_*.
}
\tag{26}
\]

Together, (15) and (25) prove `F(s)<=C_*` for every `s<=1/8`.

### Completely elementary comparison `C_*<3 sqrt(2)`

The alternating logarithm series gives

\[
\log\frac43
<\frac13-\frac1{18}+\frac1{81}-\frac1{324}+\frac1{1215}
=\frac{1399}{4860}<0.288.
\tag{27}
\]

The standard harmonic-log remainder `H_n-log n-gamma<1/(2n)` at `n=10`, together with `log 10<2.303`, gives `gamma>0.57`. (The saved checker certifies `log 10<2.303` by the positive degree-nine Taylor polynomial for `e^{2.303}`.) Using `pi>3.14` and `sqrt(2)>1.414`,

\[
C_*<\frac{6(2.5+0.288-0.57)}{3.14}
=\frac{3327}{785}
<\frac{2121}{500}
<3\sqrt2.
\tag{28}
\]

The middle rational comparison has positive cross-product gap `2970`.

---

## 5. All larger positive outputs: stochastic shell domination

Let

\[
s_0=1/8.
\]

For `s>=s_0`, regard `R_s(x)=|x^2-s|` on the bathtub optimizer `E_s`, which has Lebesgue mass one. Its distribution function is

\[
M_s(r)=\min\{m_s(r),1\}.
\tag{29}
\]

For every `0<=r<s_0<=s`, differentiating (10) in `s` gives

\[
\partial_s m_s(r)
=\frac1{\sqrt{s+r}}-\frac1{\sqrt{s-r}}<0.
\tag{30}
\]

Thus `M_s(r)<=M_{s_0}(r)` for `r<s_0`. For `r>=s_0`, `M_{s_0}(r)=1`, so the same inequality is automatic. Hence `R_s` is stochastically larger than `R_{s_0}` on these measure-one shells. Because `d(r)` is decreasing,

\[
\boxed{F(s)\le F(s_0),\qquad s\ge1/8.}
\tag{31}
\]

For the unbounded value `d(0)`, apply this first to `min(d,N)` and pass to the limit by monotone convergence.

Now use the second elementary Bessel envelope. From

\[
K_0(z)=\int_0^\infty e^{-z\cosh t}\,dt
\]

and `cosh t>=1+t^2/2`,

\[
\boxed{K_0(z)\le e^{-z}\sqrt{\frac\pi{2z}}.}
\tag{32}
\]

At `s_0=1/8`, `E_{s_0}=[-1/2,1/2]`. Substituting `x=(1/(2sqrt2))y`, then `y=sin theta` on `[0,1]` and `y=cosh u` on `[1,sqrt2]`, (32) yields

\[
F(s_0)
\le2\sqrt{\frac3\pi}\left(I_1+I_2\right),
\tag{33}
\]

with

\[
I_1=\int_0^{\pi/2}e^{-(3/4)\cos^2\theta}\,d\theta,
\qquad
I_2=\int_0^{\operatorname{arcosh}\sqrt2}e^{-(3/4)\sinh^2u}\,du.
\tag{34}
\]

Convexity of `z -> e^{-(3/4)z}` on `[0,1]` places it below its endpoint chord, so

\[
I_1\le\frac\pi4(1+e^{-3/4}),
\tag{35}
\]

while trivially

\[
I_2\le\operatorname{arcosh}\sqrt2.
\tag{36}
\]

Therefore

\[
F(s_0)\le C_{\rm shell}:=
2\sqrt{\frac3\pi}
\left[\frac\pi4(1+e^{-3/4})+\operatorname{arcosh}\sqrt2\right].
\tag{37}
\]

An elementary rational comparison gives `C_shell<3 sqrt(2)`: use

\[
\sqrt{3/\pi}<0.978,
\quad \pi<22/7,
\quad e^{-3/4}<0.473,
\quad \operatorname{arcosh}\sqrt2<0.882,
\quad \sqrt2>1.414.
\]

The exponential bounds follow from positive Taylor lower polynomials for `e^{3/4}` and `e^{0.882}`, and `sqrt(2)<1.415` in the latter comparison. Then

\[
C_{\rm shell}
<\frac{13961439}{3500000}
=3.9889825714\ldots
<4.242
<3\sqrt2.
\tag{38}
\]

Equations (31) and (38) close every `s>=1/8`.

Combining Sections 4 and 5 proves (5).

---

## 6. Required newest-Claude result applied to a real obstruction

The user-required source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, proves Theorem C: for every source-valid exact rank-three signature `(+,+,-)` form with eigenvalue magnitudes at least one,

\[
\boxed{p_Q(s)\le\pi\sqrt2\qquad(s\ge0).}
\tag{39}
\]

Apply it directly to the **finite** matrices (1), not to the Gaussian spectral limit. For every `m`, every cap-one heavy singleton law and the centered-unit-interval bank laws,

\[
p_{Q_m}(s)\le\pi\sqrt2\qquad(s\ge0).
\tag{40}
\]

This is a genuine inequality on the original product source and exact target spectrum. It rules out any unbounded one-sheet positive-output escape in this stress family, but it leaves a sharp-constant gap because `pi sqrt(2)>3 sqrt(2)`. Sections 3--5 exploit the extra one-heavy Gaussian-completion structure to close that asymptotic gap below `3 sqrt(2)`.

The other required files at the same source commit were also read. `RESULTS.md` and `FOURIER_ROUTE_REPORT.md` supply the decoupling/Fresnel-Brascamp-Lieb bounds and explicitly retain the full conjecture as open; no pointwise scalar stationary-phase decay or post-rotation independence from those routes is used here.

---

## 7. Partner synthesis: every one-heavy sign placement in the canonical Gaussian-completion mechanism

There are only two sign placements for one localized active coordinate in a canonical three-mode `(+,+,-)` completion:

1. **minority-sign heavy:** completed by `account03/B17` at the source cited in Section 1, with exact cap-one optimization and limiting value
   \[
   3.9801056750\ldots<3\sqrt2;
   \]
2. **majority-sign heavy:** the present theorem, with arbitrary cap-one heavy law and universal limiting bound
   \[
   C_*=4.2216798636\ldots<3\sqrt2.
   \]

Sign reversal covers `(-,-,+)`. Thus

\[
\boxed{
\text{the canonical disjoint-bank Gaussian-completion mechanism with exactly one macroscopic row cannot exceed }3\sqrt2,
}
\tag{41}
\]

regardless of whether that heavy row carries the majority or minority sign.

This is a statement about the **Gaussian-completion limit mechanism**, not a proof that every finite mixed-leverage target is bounded by `3 sqrt(2)`.

---

## 8. Source-valid finite interpretation and remaining gap

The matrices (1) and physical laws above are valid target instances for every finite `m`: original-coordinate independence is exact, every density cap is one, and the matrix has exactly three nonzero eigenvalues `{1,1,-1}`. The multivariate CLT gives

\[
X^2+S_{+,m}^2-S_{-,m}^2\Longrightarrow Q_\infty.
\tag{42}
\]

The present theorem therefore excludes **asymptotic Gaussian-completion escape** of the one-heavy majority-sign branch. It does **not** prove a uniform-in-`m` `3 sqrt(2)` bound, because a finite/mesoscopic density overshoot could disappear under weak convergence and is not ruled out by (42).

That distinction is essential: failure to prove a finite local-limit transfer would be failure of this auxiliary sharp-constant mechanism, not a counterexample to QFORM.

The next B17 witness search should therefore leave the now-closed one-heavy Gaussian-completion classification and attack one of:

* a genuinely finite/mesoscopic overshoot in (3), with exact density computation rather than weak convergence;
* two or more non-collinear macroscopic rows with arbitrary fragmented cap-one laws;
* shared-coordinate heavy loading across several spectral directions;
* multiscale arithmetic fragmentation coupled to a nonseparable residual spectrum;
* an extra-mode construction that survives the completed extra-eigenvalue and diffuse-limit penalties.

The full universal QFORM conjecture remains OPEN.

---

## 9. Corrections and forbidden mechanisms

The live correction inbox was reread before this write. This proof does **not** use any of the following refuted interfaces:

* uniform pointwise quadratic-phase decay;
* independence after spectral rotation;
* arbitrary-joint rank-three coarea bounds;
* positive moments of worst conditional projection-density caps;
* worst spectral-fiber suprema;
* a universal finite fragment-count reduction;
* a uniformly conditioned single physical minor or universal rank-three cross cut.

The only optimization over fragmented laws is the exact one-dimensional bathtub problem (14) for a fixed explicit kernel; no universal product-law extremality claim is inferred from it.

---

## 10. Deterministic verification

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify the exact rational comparisons and high-precision diagnostic constants. The executed output begins

`PASS QFORM-ONE-HEAVY-MAJORITY-GAUSSIAN-NOESCAPE-v1`.

The numerical Bessel integral for the centered heavy interval at zero,

\[
\frac{12}{\pi}\int_0^{1/2}K_0(6x^2)\,dx
=3.5306641257709305\ldots,
\]

is recorded only as a diagnostic and is not used in the proof.
