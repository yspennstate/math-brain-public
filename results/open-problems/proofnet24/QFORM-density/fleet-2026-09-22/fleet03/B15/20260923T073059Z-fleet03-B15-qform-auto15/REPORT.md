SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T07:30:59Z.
attacking: a mode-restricted regularity reduction for the fixed-Gaussian formulation, with an exact posterior subgaussian certificate that removes the arbitrary output center from the remaining height estimate.

# fleet03/B15 auto15 — Gaussian-mode posterior certificate and mode-centered small-ball equivalence

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Run:** `20260923T073059Z-fleet03-B15-qform-auto15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / MODE_RESTRICTED_SMALL_BALL_COMPILER / FULL_TARGET_OPEN`

The full unrestricted universal-height conjecture is still OPEN. This run changes mechanism from the preceding punctured-kernel / Fourier-envelope / one-scale-normal-form runs: the new step is a variational theorem at an actual Gaussian heat **mode**. It turns the free output center into an exact nonlinear subgaussian constraint and shows that the full conjecture is equivalent, up to an explicit factor <2.073, to one fixed-radius small-ball estimate evaluated only at those constrained mode centers.

## 1. Gaussian-mode posterior theorem

Let `mu` be any nonzero finite positive measure on `R`, let

\[
\gamma_\varepsilon(u)=\frac{1}{\sqrt{2\pi}\varepsilon}
\exp\!\left(-\frac{u^2}{2\varepsilon^2}\right),
\qquad
h_\varepsilon(y)=(\mu*\gamma_\varepsilon)(y).
\]

Since a finite measure convolved with a `C_0` kernel belongs to `C_0`, `h_epsilon` attains its positive global maximum. Fix a maximizer `y_*`, and define the Gaussian posterior / tilted probability law

\[
d\nu_*(z)=\frac{\gamma_\varepsilon(z-y_*)}{h_\varepsilon(y_*)}\,d\mu(z),
\qquad
U=\frac{Z-y_*}{\varepsilon}.
\]

### Theorem — `QFORM-GAUSSIAN-MODE-POSTERIOR-SUBGAUSSIAN-v1`

For every real `v`,

\[
\boxed{\quad \mathbb E_{\nu_*}e^{vU}\le e^{v^2/2}.\quad}
\tag{1.1}
\]

In fact this condition is **equivalent** to `y_*` being a global maximizer of `h_epsilon`.

### Proof

For every real `v`, the Gaussian ratio is exact:

\[
\frac{\gamma_\varepsilon(z-y_*-\varepsilon v)}
     {\gamma_\varepsilon(z-y_*)}
=
\exp\!\left(v\frac{z-y_*}{\varepsilon}-\frac{v^2}{2}\right).
\]

Therefore

\[
\frac{h_\varepsilon(y_*+\varepsilon v)}{h_\varepsilon(y_*)}
=
\mathbb E_{\nu_*}\exp(vU-v^2/2).
\tag{1.2}
\]

If `y_*` is a global maximizer, the left side is at most one, proving (1.1). Conversely, (1.1) inserted into (1.2) says `h_epsilon(y_*+epsilon v)<=h_epsilon(y_*)` for every `v`, hence for every real center. QED.

This is stronger than the local first/second derivative conditions. In particular,

\[
\boxed{\mathbb E_{\nu_*}U=0,\qquad \mathbb E_{\nu_*}U^2\le1,}
\tag{1.3}
\]

and Chernoff gives

\[
\boxed{\nu_*(|U|\ge R)\le2e^{-R^2/2}.}
\tag{1.4}
\]

Equation (1.3) also follows directly from `h_epsilon'(y_*)=0` and `h_epsilon''(y_*)<=0`.

No property of `mu` other than finiteness and positivity is used. Thus it applies in particular to every target quadratic-form law before any density theorem is invoked.

## 2. Exact application of the designated fleet04/B15 theorem

The completed designated partner `fleet04/B15` proved, for every probability law `mu`,

\[
\sup_{\varepsilon>0,y}(\mu*\gamma_\varepsilon)(y)=\|p_\mu\|_\infty,
\tag{2.1}
\]

with the value `+infinity` if no bounded density exists. Its canonical source is

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`.

Apply (2.1) to `Q_A=X^TAX`. Write `s_3(A)` for the third singular value and define the scale-invariant optimal constant

\[
C_*:=\sup_{\operatorname{rank}A\ge3} s_3(A)\,\|p_{Q_A}\|_\infty,
\tag{2.2}
\]

where the supremum also ranges over all independent cap-one input laws. By scalar homogeneity, (2.2) equals the owner's optimal constant restricted to `s_3(A)>=1`.

Using (2.1) and setting `B=A/epsilon`, `z=y/epsilon`,

\[
\begin{aligned}
s_3(A)\,\mathbb E\gamma_\varepsilon(Q_A-y)
&=\frac{s_3(A)}{\varepsilon}
  \mathbb E\gamma_1(Q_A/\varepsilon-y/\varepsilon)\\
&=s_3(B)\,\mathbb E\gamma_1(Q_B-z).
\end{aligned}
\]

Hence the partner theorem gives the actual equality

\[
\boxed{
C_*=\sup_{\operatorname{rank}A\ge3}
 s_3(A)\max_y\mathbb E\gamma_1(Q_A-y).
}
\tag{2.3}
\]

Every maximizing center in (2.3) satisfies the exact posterior condition (1.1). Thus the free center in the fixed-Gaussian formulation may be removed **with zero loss** and replaced by the self-consistency requirement that the Gaussian-tilted residual be 1-subgaussian.

## 3. Fixed-radius mode-centered small-ball compiler

For each admissible `(A,f)`, put

\[
H_A(y)=\mathbb E\gamma_1(Q_A-y),
\qquad
\mathcal M_A=\operatorname*{argmax}_{y\in\mathbb R}H_A(y).
\]

The mode set is nonempty. For `R>1`, define

\[
S_R:=
\sup_{A,f}\ \inf_{y\in\mathcal M_A}
\frac{s_3(A)}{2R}\Pr(|Q_A-y|\le R).
\tag{3.1}
\]

Then

\[
\boxed{
S_R\le C_*\le
\frac{2R}{\sqrt{2\pi}(1-R^{-2})}\,S_R.
}
\tag{3.2}
\]

Therefore `C_*<infinity` **if and only if** the single fixed-radius mode-centered small-ball quantity `S_R` is finite.

### Proof of the right inequality

Fix any heat mode `y in M_A`, let `M_A=H_A(y)`, and use the posterior `nu` from Section 1 with `epsilon=1`. From `E_nu U^2<=1`, Chebyshev gives

\[
\nu(|U|\le R)\ge1-R^{-2}.
\]

Consequently

\[
M_A(1-R^{-2})
\le
\mathbb E[\gamma_1(Q_A-y)\mathbf1_{\{|Q_A-y|\le R\}}]
\le
\gamma_1(0)\Pr(|Q_A-y|\le R).
\]

Since this holds for **every** global heat mode, it also holds after taking the infimum in (3.1). Multiply by `s_3(A)`, take the supremum, and use (2.3).

### Proof of the left inequality

Whenever `C_*<infinity`, every instance has density height

\[
\|p_{Q_A}\|_\infty\le C_*/s_3(A).
\]

Hence for every center, in particular every heat mode,

\[
\Pr(|Q_A-y|\le R)
\le2R\,\|p_{Q_A}\|_\infty
\le\frac{2R C_*}{s_3(A)}.
\]

This proves `S_R<=C_*`. The same inequalities are valid in the extended sense if `C_*=+infinity`.

The Chebyshev compiler constant in (3.2) is

\[
c(R)=\frac{2R}{\sqrt{2\pi}(1-R^{-2})}
=\frac{2}{\sqrt{2\pi}}\frac{R^3}{R^2-1}.
\]

Differentiating `R^3/(R^2-1)` shows its minimum over `R>1` occurs at `R=sqrt(3)`. Thus

\[
\boxed{
S_{\sqrt3}\le C_*\le
\frac{3\sqrt3}{\sqrt{2\pi}}S_{\sqrt3}
<2.073\,S_{\sqrt3}.
}
\tag{3.3}
\]

Numerically `3sqrt(3)/sqrt(2pi)=2.072964896828013`.

## 4. Why this is a genuine restriction on the remaining proof

Earlier punctured-kernel attempts could not exploit a zero at an arbitrary test center, because the center was free and a dangerous interval could simply be translated into the annulus where the kernel is large. The present lemma changes that interface: in the fixed-Gaussian formulation it is enough to work at a **global heat mode**, and such a center is not arbitrary. Its Gaussian posterior obeys the exact global family

\[
\mathbb E_\nu e^{v(Q-y)}\le e^{v^2/2}\qquad(v\in\mathbb R),
\tag{4.1}
\]

not merely a first-order stationarity equation. Any two-sheet, ridge, grouped-bank, or fractional-trace estimate may therefore assume (4.1) when estimating the mode value in (2.3).

The fixed-radius version (3.3) is especially concrete: to prove the full conjecture it suffices, up to the explicit factor `2.073`, to prove a dimension-free bound for an ordinary interval probability of width `2sqrt(3)`, but **only at a center whose Gaussian posterior is 1-subgaussian**. Scaling is already carried by `s_3(A)`; no limit in the output window is needed.

This does not by itself bound `S_sqrt3`. The hard product-geometry step remains: use original-coordinate independence and the three large spectral directions to prove `S_sqrt3<infinity` without a reciprocal tiny physical-minor loss. The theorem is therefore a supporting reduction, not a full solution.

## 5. Continuity and absolute continuity remain separate from universal height

The completed fixed-matrix regularity theorem at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T200544Z-fleet02-B15-qform-r11/REPORT.md`,

proves that every fixed rank-`>=3` target instance has an instance-dependent bounded density in `C_0(R)`. The earlier independent fleet03/B15 review checked both its nonzero-diagonal and zero-diagonal branches. Thus continuity is a qualitative fixed-instance fact; it supplies no uniform modulus and no universal height constant. This run uses the Gaussian mode only to constrain the remaining **height** problem.

## 6. Correction and scope ledger

- Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- No Gaussian, log-concavity, moment, support, connectedness, or diagonal-basis assumption is imposed on the inputs.
- The Gaussian appears only as an output regularization kernel; the original coordinates remain independent cap-one variables.
- No law-uniform pointwise van-der-Corput estimate is used.
- No arbitrary-joint rank-three coarea bound is used.
- No conditional projection-cap moment, dimension-free fiber supremum, uniform physical minor, or centered-interval extremality claim is used.
- The partner fleet04/B15 result is applied to the exact equality (2.3), and then to the quantitative inequalities (3.2)-(3.3).
- The new theorem is valid for every probability law, so it remains valid through all target signs and degeneracies; the QFORM-specific difficulty enters only in proving a uniform bound for the mode-centered small-ball quantity.

**Next mathematical step:** insert the exact posterior constraint (4.1) into the current low-volume/high-leverage or minority/two-sheet conditional geometry and try to bound `S_sqrt3` directly before any fiber supremum or reciprocal-minor extraction.
