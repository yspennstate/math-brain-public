# Immutable adversarial audit: input-regular odd-crossing FEI

Date: 2026-10-03 UTC. Auditor: independent `/root/balanced_fei_audit`
agent. This file is an immutable audit checkpoint; it does not modify or
supersede the candidate or proof.

## Verdict

**PASS as a restricted theorem, conditional only on the two cited standard
inputs (the KOS halfspace noise theorem and Berry--Esseen).** I reconstructed
every displayed inequality and constant in the newest finite-crossing,
input-regular candidate and found no mathematical gap. In particular, the
new mask-averaging step has the correct inequality direction, and the extra
factor (B^2) in the definition of (K) is both necessary for this proof and
present.

This does **not** prove unrestricted Boolean FEI, arbitrary-weight
three-crossing FEI, an even-crossing theorem, or an arbitrary-bias theorem.
Those statements remain outside the result; full Boolean FEI remains a
conjecture. Historical novelty of the restricted theorem is also unverified.

## Audited immutable inputs

The audit targeted these exact file contents:

| File | SHA-256 |
|---|---|
| `input_regular_moderate_bias_odd_crossing_fei_candidate.md` | `1af5cb060563fc75138a9fea8c7a6be891f505c0017ab96ab0d3daa40fe94ed4` |
| `input_regular_moderate_bias_odd_crossing_fei_proof.md` | `385cfe7db4a71c2c579a7fef034ab0ffa7bc677050646fcca20b445db524d6e7` |
| `verify_input_regular_odd_crossing_heat.py` | `431b3a7c0e5f57a2e9802d564aed187144be4e9e239baccb102263791251bdcd` |
| `input_regular_odd_crossing_heat_checks.json` | `9dc7168d815d3ec9b704197473f6a9f71230838dc0e892dcd1c21431e0ac8682` |
| `verify_input_regular_odd_crossing_mask.py` | `854496809a9a9a495787406cfdfc695a81d7c52076f5bb79cfb6a37245df1f24` |
| `input_regular_odd_crossing_mask_checks.json` | `c92cf35ad86c73cd3e86fdfa585565335b25c8e48dd5ef268116e9e04836c1c3` |
| `verify_regular_moderate_bias_odd_crossing.py` | `13b2b60ae7dcfe03213766a580cee76c32ec9ca817a221e495f4b2c48439738a` |
| `regular_moderate_bias_odd_crossing_checks.json` | `e5a6d2b3f04d6a677dfe4cb30036204cb00534afe14b029a49913be790ded18b` |

The completed proof adds a full derivation of the entropy tail and weak
logarithmic FEI inputs to the shorter candidate. The theorem proved by both
documents is the same.

## Exact scope

Let

\[
S(X)=\sum_{i=1}^n w_iX_i,\qquad
\sigma^2=\sum_iw_i^2>0,
\]

with uniform independent signs and

\[
w_{\max}:=\max_i|w_i|\le B\sigma/\sqrt n,
\qquad B\ge1.
\tag{A1}
\]

Let (F:\mathbb R\to\{-1,1\}) be a step function with exactly (m)
distinct genuine crossings, (m) odd, alternating interval labels, arbitrary
adjacent labels at the crossing points, and no other isolated anomalies.
Every crossing satisfies

\[
|\theta_r|\le\lambda\sigma.
\tag{A2}
\]

The proved conclusion is a constant ordinary FEI bound for (g=F(S)),
where the constant depends on the fixed parameters (m,B,\lambda), but not
on (n), individual crossing gaps, or the smallest nonzero weight.

Coordinate sign changes make the weights nonnegative and merely sign-change
Fourier coefficients; squared Fourier masses and physical influences are
unchanged. Zero weights are allowed. If all weights vanish, the output is
constant and the conclusion is immediate. Deleting a zero coordinate changes
(n) to a smaller value and makes the right side of (A1) larger, so the same
(B) remains valid.

## 1. Entropy upper bound and the constant (A)

Each crossing step, with either legal tie convention on the finite attained
score set, is a halfspace after an arbitrarily small threshold perturbation.
The product of the (m) steps equals (g) up to a constant sign. KOS
Theorem 18 gives, under independent bit-flip noise,

\[
\operatorname{NS}_\varepsilon(h)
 \le 20.5p\sqrt{\varepsilon\ln(1/p)}
 \le20.5\sqrt\varepsilon.
\]

The second bound is deliberately loose and valid; constants have zero noise.
A union bound therefore gives

\[
\operatorname{NS}_\varepsilon(g)\le20.5m\sqrt\varepsilon.
\tag{A3}
\]

For the squared-Fourier degree random variable (D), physical bit-flip noise
satisfies

\[
2\operatorname{NS}_\varepsilon(g)
=\sum_S\widehat g(S)^2[1-(1-2\varepsilon)^{|S|}].
\tag{A4}
\]

At \(\varepsilon=1/(2k)\), every degree at least (k\ge1) contributes at
least (1-(1-1/k)^k\ge1-e^{-1}). Combining (A3)--(A4) gives

\[
\Pr[D\ge k]
 \le \frac{41m}{\sqrt{2k}(1-e^{-1})}
 =\frac{Am}{\sqrt k},
\qquad
A=\frac{41}{\sqrt2(1-e^{-1})}.
\tag{A5}
\]

The (k=1) case is valid: its positive-degree multiplier in (A4) is one.
For real (t>0), integer-valuedness gives the same bound with (k=\lceil
t\rceil), weakened to (Am/\sqrt t).

Conditioning the spectral law on (D) yields

\[
H(g)\le\log_2(n+1)
+\frac1{\ln2}\mathbb E[D\ln(en/D)].
\]

For (b(t)=t\ln(en/t)), (b'(t)=\ln(n/t)\ge0) on ((0,n]). Layer cake
and (A5) give

\[
\mathbb Eb(D)
\le Am\int_0^nt^{-1/2}\ln(n/t)\,dt
=4Am\sqrt n.
\]

Also (ln(n+1)\le\sqrt n) for (n\ge1). Thus

\[
H(g)\le C_H\sqrt n,
\qquad C_H=\frac{1+4Am}{\ln2}.
\tag{A6}
\]

All atoms, including degree zero, are retained. No regularity, bias, or
oddness is used in (A6).

## 2. Odd-tail translation inequality

For fixed shifts (u,v), delete every translated crossing endpoint from

\[
\{r:F(r+u)\ne F(r+v)\}
\]

and call the remaining open set (A^\circ_{u,v}). It is a union of at most
(2m) bounded open components, all lying in

\[
[\theta_1-\max(u,v),\theta_m-\min(u,v)].
\tag{A7}
\]

Because (m) is odd, the two tail labels satisfy (a_+=-a_-). Direct
translation of the step function gives

\[
\int_{\mathbb R}[F(r+v)-F(r+u)]\,dr
=(v-u)(a_+-a_-).
\]

The absolute integrand equals two on the pivotal set and zero off it, away
from the finitely many deleted endpoints. Cancellation can only reduce the
absolute signed integral, so

\[
|A^\circ_{u,v}|\ge|u-v|.
\tag{A8}
\]

This is exactly where oddness is used. Arbitrary legal endpoint labels cause
no gap: deleting pivotal endpoint atoms only lowers the discrete pivotal
probability that will later be estimated.

## 3. Remainder Gaussian comparison and (d,E)

For a uniform (K)-subset (J), define

\[
U=\sum_{i\in J}w_iX_i,\quad
V=\sum_{i\in J}w_iY_i,\quad
R=\sum_{i\notin J}w_iX_i,
\]

and

\[
a_J=\sum_{i\in J}w_i^2,qquad s_J^2=\sigma^2-a_J.
\]

The cutoff is chosen so that every mask satisfies

\[
a_J\le K w_{\max}^2
 \le\frac{KB^2\sigma^2}{n}\le\frac{\sigma^2}{2},
\quad
s_J\ge\frac\sigma{\sqrt2},
\tag{A9}
\]

and

\[
|U|,|V|\le K w_{\max}
 \le\frac{KB\sigma}{\sqrt n}\le\sigma.
\tag{A10}
\]

Equations (A2), (A7), and (A10) put every relevant open interval inside
([-(\lambda+1)\sigma,(\lambda+1)\sigma]). On this range, using
(s_J\le\sigma) in the prefactor and (s_J^2\ge\sigma^2/2) in the
exponent, the (N(0,s_J^2)) density is at least

\[
\frac{e^{-(\lambda+1)^2}}{\sqrt{2\pi}\sigma}
=\frac d\sigma,
\qquad
d=\frac{e^{-(\lambda+1)^2}}{\sqrt{2\pi}}.
\tag{A11}
\]

Berry--Esseen with constant (0.56) gives a CDF error

\[
\delta_J
\le0.56\frac{\sum_{i\notin J}|w_i|^3}{s_J^3}
\le0.56\frac{w_{\max}}{s_J}
\le\frac{0.56\sqrt2B}{\sqrt n}.
\tag{A12}
\]

The middle inequality uses
(\sum_{i\notin J}|w_i|^3\le w_{\max}s_J^2); it does not use a minimum
weight. An open interval costs at most (2\delta_J), and at most (2m)
components cost at most (4m\delta_J). Hence (A8), (A11), and (A12) give

\[
\Pr[F(R+u)\ne F(R+v)]
\ge\frac{d|u-v|}{\sigma}-\frac{EmB}{\sqrt n},
\quad
E=4(0.56)\sqrt2=2.24\sqrt2.
\tag{A13}
\]

The CDF bound extends to left limits because the Gaussian CDF is continuous,
so open intervals and attained discrete score atoms are handled correctly.
A negative right side for an individual pair (u,v) is harmless when the
inequality is averaged.

## 4. Difference moment and the constant (c_D)

Conditional on (J), the independent old and fresh block scores satisfy

\[
\mathbb E(U-V)^2=2a_J,
\]

\[
\mathbb E(U-V)^4
=12a_J^2-4\sum_{i\in J}w_i^4
\le12a_J^2.
\tag{A14}
\]

Log-convexity of (L^p) norms, equivalently Hölder interpolation, gives

\[
\mathbb E|U-V|
\ge\frac{[\mathbb E(U-V)^2]^{3/2}}
          {[\mathbb E(U-V)^4]^{1/2}}
\ge\sqrt{\frac23}\sqrt{a_J}.
\tag{A15}
\]

Thus

\[
c_D=\sqrt{2/3}.
\]

When (a_J=0), both sides of (A15) are zero and the conclusion follows
directly; the proof need not divide by a zero fourth moment.

## 5. The genuinely new mask average

Uniform fixed-size subset sampling gives the exact first moment

\[
\mathbb E_Ja_J=\frac K n\sigma^2.
\tag{A16}
\]

Every mask obeys

\[
0\le a_J\le L:=\frac{KB^2\sigma^2}{n}.
\]

Pointwise,

\[
\sqrt{a_J}\ge\frac{a_J}{\sqrt L}.
\]

Averaging this inequality and using (A16), rather than misusing concavity,
gives

\[
\mathbb E_J\sqrt{a_J}
\ge\frac{\sqrt K\,\sigma}{B\sqrt n}.
\tag{A17}
\]

This remains valid with tiny weights and masks of all zero-weight
coordinates. The (1/B) loss in (A17) is the reason that the new theorem's
block-size threshold contains (B^2) inside the squared quantity.

## 6. Choice of (K,N_0) and influence lower bound

The proof defines

\[
K=\max\left\{1,\left\lceil
 \left(\frac{2EmB^2}{dc_D}\right)^2\right\rceil\right\},
\]

\[
N_0=\left\lceil\max\{2KB^2,K^2B^2\}\right\rceil.
\tag{A18}
\]

For (n\ge N_0), the first cutoff in (A18) proves (A9), and the second
proves (A10). It also ensures (K\le n), so a (K)-subset exists. The
definition of (K) is exactly equivalent to

\[
EmB\le\frac{dc_D\sqrt K}{2B}.
\tag{A19}
\]

Average (A13), then apply (A15), (A17), and (A19):

\[
\Pr[g(X)\ne g(X^{\mathrm{resample} J})]
\ge\frac{dc_D\sqrt K/B-EmB}{\sqrt n}
\ge\frac{dc_D\sqrt K}{2B\sqrt n}.
\tag{A20}
\]

Successively resampling the coordinates in a fixed mask keeps every
intermediate vector uniform. Resampling coordinate (i) changes the output
with probability exactly (I_i(g)/2). A union bound and uniform-subset
averaging give

\[
\Pr[g(X)\ne g(X^{\mathrm{resample} J})]
\le\frac12\mathbb E_J\sum_{i\in J}I_i(g)
=\frac K{2n}I(g).
\tag{A21}
\]

Combining (A20)--(A21) cancels both factors of two and yields

\[
I(g)\ge\frac{dc_D}{B\sqrt K}\sqrt n,
\qquad n\ge N_0.
\tag{A22}
\]

## 7. Weak small-dimensional bound and final constant

For completeness, the proof's weak bound is also correct. With minority
probability (r\le1/2), variance (v=4r(1-r)), and physical influence,
cube edge isoperimetry gives

\[
I(f)\ge2r\log_2(1/r).
\]

The binary entropy calculation in the proof gives

\[
h_2(v)\le4r\log_2(1/r)\le2I(f).
\]

Condition the squared-Fourier law on a nonempty set and compare it with

\[
Q(S)=n^{-|S|}/Z_n,qquad
Z_n=(1+1/n)^n-1<2.
\]

Nonnegative relative entropy, (v\mathbb E_{P_+}|S|=I(f)), and
Poincaré (v\le I(f)) give

\[
H(f)\le(\log_2n+3)I(f).
\tag{A23}
\]

This retains the empty Fourier atom and handles constants separately. For
(n<N_0), (A23) supplies the first branch. For (n\ge N_0), divide (A6)
by (A22). The resulting valid constant is exactly

\[
C(m,B,\lambda)=
\max\left\{\log_2N_0+3,
 \frac{(1+4Am)B\sqrt K}{(\ln2)dc_D}\right\}.
\tag{A24}
\]

As a numerical constant sanity check, at (m=B=1,\lambda=0), the formulas
give

\[
d\approx0.1467626632,quad c_D\approx0.8164965809,quad
E\approx3.167838380,quad A\approx45.86368474,
\]

\[
K=2796,qquad N_0=7{,}817{,}616,qquad
C_{\rm large}\approx117{,}425.65.
\]

The constants are intentionally enormous but finite and internally
consistent.

## Adversarial failure probes

I specifically checked the following possible failure modes.

1. **Wrong Jensen direction:** concavity would upper-bound
   (ℝ\sqrt{a_J}). The proof instead uses the pointwise chord inequality
   (sqrt a\ge a/\sqrt L), so (A17) is valid.
2. **Reusing the bounded-ratio (K):** that would miss one factor of (B)
   after (A17). The candidate correctly uses (B^2) in (A18).
3. **Zero-energy masks:** (A15) is interpreted directly at (a_J=0); no
   division by zero occurs.
4. **Degenerate remainder:** (n\ge2KB^2) forces
   (s_J^2\ge\sigma^2/2>0) for every mask.
5. **A nonexistent (K)-subset:** (n\ge K^2B^2\), with (K,B\ge1),
   implies (n\ge K).
6. **Endpoint atoms and arbitrary ties:** all translated endpoints are
   discarded for a lower bound, and Berry--Esseen is applied to open
   intervals using CDF left limits.
7. **Coincident translated crossings:** the deliberately loose (2m)
   component count still covers point holes and coincident endpoints.
8. **Noise convention mismatch:** KOS defines noise by independently
   flipping bits, matching (A4), and the factor two in (A4) is retained.
9. **Empty spectral atom:** both the degree-conditioning argument and the
   weak bound explicitly retain it.
10. **Unstated spacing assumption:** none is used. Only the total measure
    bound (A8), component count, regularity, and normalized location bound
    enter.

No probe produced a counterexample or missing case under the stated
hypotheses.

## Rerun and static-check record

I read all three relevant programs and reran isolated copies, so the
checked-in reports were not overwritten.

| Program | Rerun result |
|---|---|
| `verify_input_regular_odd_crossing_heat.py` | PASS: 63 weight vectors, 3,339 exact masks/moment checks, 459 zero-energy masks, 189 exact mask-energy averages, 126 exact resampling comparisons |
| `verify_input_regular_odd_crossing_mask.py` | PASS: 11,868 exact mask/moment checks, 362 exact first moments, 279 zero-energy masks, 87 small-cube truth/Walsh checks, positive weight ratio up to 1,048,576 |
| `verify_regular_moderate_bias_odd_crossing.py` | PASS: 9,552 exact translation checks, 53,661 endpoint exclusions, 648 exact difference-moment and resampling checks, 960 exact degree/noise-tail checks, 5,974 numerical open-interval Berry--Esseen checks, 64 constant-regime checks |

All three original programs also pass Python bytecode compilation. The exact
assertions use rational arithmetic where claimed. Entropy, square roots,
Gaussian CDFs, and a few displayed constant comparisons are numerical
supplements with stated tolerances.

The programs do **not** truth-table enumerate the regime (n\ge N_0); for
even the smallest baseline parameters (N_0) exceeds 7.8 million. They test
constituent identities, not the dimension-independent theorem. The analytic
argument above is therefore essential and cannot be replaced by the PASS
reports.

## Theorem versus conjecture/status table

| Claim | Status after this audit |
|---|---|
| FEI for fixed odd (m), fixed input regularity (B), and crossings in ([-λσ,λσ]) | **Theorem proved by the audited argument** |
| No lower bound on individual nonzero weights | **Proved** |
| Uniformity over all crossing spacings and legal tie choices | **Proved** |
| Same conclusion for even (m) by this argument | **Not proved; odd-tail step fails** |
| Same conclusion for arbitrary irregular weights | **Not proved** |
| Same conclusion with unbounded normalized crossing locations | **Not proved** |
| Arbitrary-weight, arbitrary-bias three-crossing FEI | **Open here** |
| Full Boolean Fourier entropy--influence conjecture | **Still conjectural** |
| Historical novelty of this restricted formulation | **Unverified** |

## Final audit conclusion

The input-regular extension is not merely a conjectural route: under its
explicit hypotheses it is a complete proof. Every loss is accounted for:
(m) in the halfspace union and interval count, (B) in Berry--Esseen,
another effective (B) through the mask square-root average, and
(λ) through the Gaussian density floor. The definitions of (K) and
(N_0) absorb exactly those losses. I found no hidden minimum-weight,
spacing, atom-avoidance, or large-dimension assumption.

The correct research-level label is therefore **restricted FEI theorem,
internal analytic PASS; novelty and external peer review not certified**.
