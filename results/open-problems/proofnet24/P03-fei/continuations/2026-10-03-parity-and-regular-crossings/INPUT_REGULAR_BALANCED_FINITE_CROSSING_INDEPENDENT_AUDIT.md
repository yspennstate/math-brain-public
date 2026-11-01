# Immutable adversarial audit: balanced input-regular finite-crossing FEI

Date: 2026-10-03 UTC. Auditor: independent `/root/balanced_fei_audit`
agent.

## Verdict

**PASS for the patched candidate.** The argument proves a restricted ordinary
Fourier entropy--influence theorem for every fixed finite crossing count
(m), fixed input-regularity parameter (B), and fixed output-balance floor
(r_0>0). I reconstructed the endpoint comparison, protected-interval
extraction, local signed-translation identity, component count, Gaussian
comparison, mask average, and all constants. No analytic gap remains in the
patched file.

An initial version incorrectly compared the discrete score with open label
interiors, thereby omitting crossing atoms. That version was not auditable as
written. The exact candidate hashed below is the repaired version: it uses
the actual Borel label sets (B_\pm), including assigned crossings, and
compares them with Gaussian-measure-equivalent open interiors (G_\pm).
The repair is sufficient and preserves every stated constant.

This is an internal proof audit, not external peer review or a historical
priority certificate. It does not prove unrestricted Boolean FEI,
arbitrary-irregular-weight finite-crossing FEI, or a balance-free theorem.

## Immutable target and check artifacts

| File | SHA-256 |
|---|---|
| `input_regular_balanced_finite_crossing_fei_candidate.md` | `2c66fe2937cb6c5a5df6ff82f9477e0ade0364c55d92c040614cd3d079287aff` |
| `verify_input_regular_balanced_finite_crossing.py` | `cab178da9b2e04e18df3811ec78d1148d098ff882c2de936c165a5cfc89e08d6` |
| `input_regular_balanced_finite_crossing_checks.json` | `ee5f0c9a5c066190c7fa0d06ea475083bacc677d5dc20dc4b03359817d1eb6ea` |
| `independent_input_regular_balanced_finite_crossing_endpoint_check.py` | `0a8c1468a9dcc8cd7cf6c4a4c92c7d7eb9f17066b9062b340a26610f6b1f6f7e` |
| `independent_input_regular_balanced_finite_crossing_endpoint_checks.json` | `bce301decd76c16d9544f349216f5d705734be7dedf85b926f4ae7c82b03a24a` |

## Scope proved

The score is

\[
S(X)=\sum_{i=1}^n w_iX_i,\qquad
\sigma^2=\sum_iw_i^2>0,
\]

with independent uniform signs and input regularity

\[
w_{\max}\le \frac{B\sigma}{\sqrt n}.                  \tag{A1}
\]

The outer step function (F) has exactly (m) distinct genuine crossings,
alternating open-interval labels, a legal adjacent label at each crossing,
and no other point anomalies. The crossing locations and gaps are arbitrary.
The additional hypothesis is

\[
\min\{\Pr[F(S)=1],\Pr[F(S)=-1]\}\ge r_0.             \tag{A2}
\]

For fixed (m,B,r_0), the proof gives (H(F(S))\le C I(F(S))) with (C)
independent of dimension, crossing locations, crossing spacing, and the
smallest nonzero input weight.

Coordinate sign changes preserve squared Fourier coefficients and physical
influences, so weights may be made nonnegative. Zero weights do not disturb
the argument. Constant outputs and zero variance are removed before any
division; (A2) already excludes a constant output.

## 1. Inherited entropy bound

Each legal crossing step is a halfspace on the finite cube-score set, with
its tie choice realized by a sufficiently small threshold perturbation.
Their product equals (g=F(S)) up to a constant sign. The KOS halfspace noise
bound and a union bound give

\[
\operatorname{NS}_\varepsilon(g)\le20.5m\sqrt\varepsilon.
\]

For the squared-Fourier degree law (D), the exact flip-noise identity at
(\varepsilon=1/(2k)) gives

\[
\Pr[D\ge k]\le\frac{Am}{\sqrt k},
\qquad
A=\frac{41}{\sqrt2(1-e^{-1})}.
\]

Indeed, degree at least (k) contributes at least (1-e^{-1}), and the
factor (41/\sqrt2) is (2(20.5)/\sqrt2). Degree conditioning and

\[
\int_0^nt^{-1/2}\ln(n/t)\,dt=4\sqrt n,
\qquad \ln(n+1)\le\sqrt n,
\]

then yield

\[
H(g)\le \frac{1+4Am}{\ln2}\sqrt n.                   \tag{A3}
\]

This part needs neither balance nor a crossing-location bound.

## 2. Patched endpoint/tie comparison

Let (Z\sim N(0,\sigma^2)). From Berry--Esseen and (A1),

\[
\delta:=\sup_t|\Pr[S\le t]-\Pr[Z\le t]|
\le\frac{0.56B}{\sqrt n}.                             \tag{A4}
\]

The repaired proof defines (B_\pm=\{t:F(t)=\pm1\}), including every
crossing in its assigned class. Because each crossing is assigned one of its
adjacent labels and there are no other anomalies, each (B_\pm) is a union
of at most (m+1) intervals whose endpoints may independently be open or
closed. There are no singleton components.

For one component, all four endpoint conventions are handled by the CDF and
its left limit:

\[
\begin{array}{c|c}
(a,b)&F_S(b^-)-F_S(a)\\
[a,b]&F_S(b)-F_S(a^-)\\
(a,b]&F_S(b)-F_S(a)\\
[a,b)&F_S(b^-)-F_S(a^-).
\end{array}
\]

The Gaussian CDF is continuous, so both (F_S(t)) and (F_S(t^-)) are
within (delta) of the same Gaussian value. Thus every component costs at
most (2\delta). Unbounded endpoints only reduce this cost. If (G_\pm)
denotes the union of the corresponding open interiors, then the continuous
Gaussian assigns (B_\pm) and (G_\pm) the same probability. Summing the
component errors gives exactly

\[
|\Pr[S\in B_\pm]-\Pr[Z\in G_\pm]|
\le\frac{1.12(m+1)B}{\sqrt n}.                        \tag{A5}
\]

Hence the patched equation (8) retains every discrete score atom assigned
at a crossing. This is the required resolution of the main endpoint risk.

## 3. Protected opposite-label intervals

The third term in (N_0) ensures that the right side of (A5) is at most
(r_0/4). Balance therefore implies

\[
\Pr[Z\in G_\pm]\ge3r_0/4.                             \tag{A6}
\]

With

\[
L=\frac2{\sqrt{r_0}},
\]

Chebyshev gives

\[
\Pr[|Z|>L\sigma]\le L^{-2}=r_0/4.
\]

Each label consequently has Gaussian mass at least (r_0/2) in
([-L\sigma,L\sigma]). Since the Gaussian density is everywhere at most
(1/(\sigma\sqrt{2\pi})), the total Lebesgue length occupied there by each
open label interior is at least

\[
\frac{r_0\sigma\sqrt{2\pi}}2.                         \tag{A7}
\]

Intersection with the central interval does not increase the number of
components, so there are at most (m+1). For

\[
h=\frac{r_0\sqrt{2\pi}}{8(m+1)},
\]

one component for each label has length at least

\[
\frac{r_0\sigma\sqrt{2\pi}}{2(m+1)}=4h\sigma.
\]

Its midpoint is protected by an open radius-(2h\sigma) neighborhood on
which (F) is constant. Equality in the length bound is harmless because
only open neighborhoods are needed, and all later shifts have magnitude at
most (h\sigma). Selecting one component of each label gives protected
points (a,b\in[-L\sigma,L\sigma]) with opposite labels.

## 4. Local signed-translation identity

Take (|u|,|v|\le h\sigma), assume (u<v), and first suppose (a<b). A
direct antiderivative calculation gives

\[
\begin{aligned}
\int_a^b[F(r+v)-F(r+u)]\,dr
&=\int_{b+u}^{b+v}F(t)\,dt
  -\int_{a+u}^{a+v}F(t)\,dt.
\end{aligned}                                         \tag{A8}
\]

Both boundary intervals lie strictly inside their protected neighborhoods.
Their labels are opposite, so the absolute value of (A8) is exactly
(2(v-u)). Reversing the order of (a,b), or of (u,v), changes only an
orientation sign.

Delete from the interval between (a,b) all points where either translated
argument is a crossing. Off those finitely many points the integrand has
absolute value two precisely on the open pivotal set. The triangle
inequality applied to (A8) therefore yields

\[
|\{r\in J_{a,b}:F(r+u)\ne F(r+v)\}^{\circ}|
\ge |u-v|.                                             \tag{A9}
\]

Endpoint tie assignments affect only the deleted zero-measure points. They
cannot alter (A8) or (A9).

There are at most (2m) translated crossing locations before coincidences,
so the deleted pivotal set has at most (2m) open components. This loose
bound is sufficient. The parenthetical sharper (m) bound is also valid:
the pivotal indicator is zero near both protected endpoints; a single
translated crossing toggles it, while a coincident pair does not toggle it
but can split one open component. Each resulting component consumes two of
the total (2m) crossing occurrences, counting multiplicity.

## 5. Gaussian remainder bound and constants (d,E)

For a uniform (K)-subset (J), set

\[
a_J=\sum_{i\in J}w_i^2,
\qquad s_J^2=\sigma^2-a_J.
\]

The first two large-dimension cutoffs imply, for every mask,

\[
a_J\le\frac{KB^2\sigma^2}{n}\le\frac{\sigma^2}{2},
\qquad s_J\in[\sigma/\sqrt2,\sigma],                  \tag{A10}
\]

and

\[
|U|,|V|\le\frac{KB\sigma}{\sqrt n}\le h\sigma.       \tag{A11}
\]

The interval (J_{a,b}) lies in ([-L\sigma,L\sigma]). For a centered
Gaussian of variance (s_J^2), (A10) gives the density floor

\[
\frac1{\sqrt{2\pi}s_J}e^{-r^2/(2s_J^2)}
\ge\frac{e^{-L^2}}{\sqrt{2\pi}\sigma}
=\frac d\sigma,
\qquad d=\frac{e^{-L^2}}{\sqrt{2\pi}}.                \tag{A12}
\]

Berry--Esseen for the remainder gives

\[
\delta_J\le0.56\frac{w_{\max}}{s_J}
\le\frac{0.56\sqrt2B}{\sqrt n}.                      \tag{A13}
\]

An open interval loses at most (2\delta_J); at most (2m) components
lose at most

\[
4m\delta_J
\le\frac{2.24\sqrt2\,mB}{\sqrt n}
=\frac{EmB}{\sqrt n},
\qquad E=2.24\sqrt2.                                  \tag{A14}
\]

Combining (A9), (A12), and (A14) proves the candidate's conditional bound

\[
\Pr[F(R+u)\ne F(R+v)]
\ge\frac{d|u-v|}{\sigma}-\frac{EmB}{\sqrt n}.          \tag{A15}
\]

## 6. Mask average, (K,N_0), and influence

Conditional on (J), independence gives

\[
\mathbb E(U-V)^2=2a_J,
\]

\[
\mathbb E(U-V)^4
=12a_J^2-4\sum_{i\in J}w_i^4\le12a_J^2.
\]

Hölder interpolation yields

\[
\mathbb E[|U-V|\mid J]\ge c_D\sqrt{a_J},
\qquad c_D=\sqrt{2/3}.                                \tag{A16}
\]

At (a_J=0) this is read directly as (0\ge0). Uniform-subset sampling
gives

\[
\mathbb E_Ja_J=K\sigma^2/n,
\qquad
0\le a_J\le KB^2\sigma^2/n.
\]

The pointwise chord inequality (sqrt x\ge x/\sqrt M) on ([0,M]), not
Jensen in the wrong direction, gives

\[
\mathbb E_J\sqrt{a_J}
\ge\frac{\sqrt K\sigma}{B\sqrt n}.                    \tag{A17}
\]

The candidate chooses

\[
K=\max\left\{1,\left\lceil
\left(\frac{2EmB^2}{dc_D}\right)^2\right\rceil\right\}.
\]

This is exactly the condition

\[
EmB\le\frac{dc_D\sqrt K}{2B}.                         \tag{A18}
\]

It follows from (A15)--(A18) that

\[
\Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
\ge\frac{dc_D\sqrt K}{2B\sqrt n}.                    \tag{A19}
\]

Successive resampling changes coordinate (i) with probability
(I_i(g)/2), and every intermediate vector remains uniform. A union bound
and mask averaging give

\[
\Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
\le\frac K{2n}I(g).                                   \tag{A20}
\]

Thus

\[
I(g)\ge\frac{dc_D}{B\sqrt K}\sqrt n.                 \tag{A21}
\]

Every term in

\[
N_0=\left\lceil\max\left\{
2KB^2,\frac{K^2B^2}{h^2},
\left(\frac{4.48(m+1)B}{r_0}\right)^2
\right\}\right\rceil
\]

has now been accounted for: respectively (A10), (A11), and the
(r_0/4) error requirement in (A5). Since (h<1), (B\ge1), and (K\ge1),
this cutoff also ensures (n\ge K), so the required mask exists.

Combining (A3) and (A21), and using the established weak bound
(H(g)\le(\log_2n+3)I(g)) below (N_0), gives exactly

\[
C(m,B,r_0)=\max\left\{\log_2N_0+3,
\frac{(1+4Am)B\sqrt K}{(\ln2)dc_D}\right\}.           \tag{A22}
\]

The constants are extremely large, particularly because
(d=e^{-4/r_0}/\sqrt{2\pi}), but finite for every fixed (r_0>0).

## 7. Checker audit and independent endpoint closure

The author checker was read and rerun from an isolated copy. It passes:

- 440 exact local signed-translation and boundary-integral checks, including
  160 even-crossing and 280 odd-crossing cases;
- 40,700 small score functions from 291 regular weight families;
- 35,259 balanced truth tables; and
- exact equality of Walsh spectral energy and physical total influence.

Its maximum observed entropy/influence ratio is approximately (3.37109).
The checker compiles successfully.

The author checker intentionally uses crossing locations strictly between
attained score levels in its truth-table portion, and its translation helper
also avoids evaluating ties. It therefore does not test the endpoint content
of patched equation (8). This is a scope limitation, not a proof gap.

The new independent endpoint checker closes that finite-test scope. It puts
cuts both on and between score levels and enumerates every legal adjacent
label at each crossing. Its report passes:

- 5 rational weight vectors;
- 14,386 cut/tie families;
- 28,772 two-label comparison inequalities;
- 2,970 attained-cut occurrences across the distinct cut tuples; and
- 41,534 legal endpoint assignments counted across crossings.

Discrete score laws, endpoint labels, probabilities, and left/right CDF
values are exact rational calculations. Gaussian CDF comparisons are
numerical with tolerance (2\times10^{-15}). The largest observed ratio of
actual error to the proof's (2(m+1)\delta) bound is (1/3). The independent
checker also compiles successfully.

Neither suite enumerates the huge (n\ge N_0) regime or proves
Berry--Esseen. They corroborate constituent identities; the analytic proof
above establishes the theorem.

## Adversarial status table

| Claim | Status |
|---|---|
| Fixed-(m,B,r_0) ordinary FEI for the stated score functions | **Proved** |
| Arbitrary crossing locations and spacings | **Proved** |
| Even as well as odd crossing counts | **Proved** |
| Arbitrary legal crossing tie assignments | **Proved after the Borel-set patch** |
| No positive lower bound on individual weights | **Proved** |
| Constant uniform as (r_0\downarrow0) | **Not proved; constants diverge** |
| Unbounded input irregularity (B) | **Not proved** |
| General Boolean FEI | **Still conjectural** |
| Historical novelty | **Unverified** |

## Final conclusion

The protected-interval mechanism legitimately replaces the earlier global
opposite-tail lemma. Balance creates macroscopic opposite-label intervals in
a central Gaussian window; their midpoints supply local boundary data whose
signed translation forces pivotal Lebesgue measure. Input regularity then
turns that measure into an influence lower bound. Endpoint atoms, coincident
translated crossings, zero-energy masks, and all normalization factors are
accounted for.

Final label: **complete restricted theorem; independent internal analytic
audit PASS on the patched candidate; novelty and external review not
certified**.
