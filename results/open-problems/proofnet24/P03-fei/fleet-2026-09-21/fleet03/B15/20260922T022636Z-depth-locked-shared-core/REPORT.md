# fleet03/B15 — the current shared-core obstruction has a unique increasing integer depth

**Run:** `20260922T022636Z-fleet03-B15-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` at the current shared-core replacement obligation.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository mathematical sources were retrieved through the authorized connector, but no authenticated mathematical-brain retrieval/receiver context was consumed.

## 1. Live target and candidate version

The current natural-language owner control supersedes the older packet-only B15 duty and asks the FEI workers to converge on the all-gate formulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i {\rm It}_i(G;p)\,
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-cap potential and every Boolean gate and product bias. At a balanced gate at uniform bias, the obstruction is

\[
R(G):=\frac{H(G)}{I(G)-1}\le \Gamma(1/2),
\tag{1.1}
\]

and relative to the historical read-once reference \(C_0=6.4548\), the comparable gate margin is

\[
c_G=4(R(G)-C_0).
\tag{1.2}
\]

The named compatible peer result consumed here is

`fleet04/B17/20260922T014537Z-shared-graft-tail-closure/REPORT.md`,
Git blob `9eaad387fb0d3812cb2b6c65d8510afc4639ae18`.

That report consumes the preceding fleet03/B15 construction, certifies the actual balanced Boolean gate \(F_7\),

\[
6.5218509495504481848401605388605115013503296799038586768578
<
R_7
<
6.5218509495504481848401605388605115013503296832418414558148,
\tag{1.3}
\]

and proves that the total possible positive tail from continuing the same depth-four transformation after \(F_7\) is less than \(5.44\times10^{-118}\). It also derives the exact source-valid transformation for every integer self-composition depth \(d\ge1\).

The prior missing implication attacked here is therefore precise:

> At the current \(F_7\) state, can a different integer self-composition depth \(d\neq4\), followed by the same exact shared-core graft, give another positive ratio increment?

This is a materially different calculation from continuing the already-closed \(d=4\) tail.

## 2. Exact peer recurrence applied

Use the peer notation

\[
\alpha=\frac9{256},\qquad B=\frac{257}{256},\qquad d_0=\frac{133}{128},
\]

and

\[
K(b)=H_{\rm core}(b)+\alpha[-\phi(b^2)+16(1-b^2)],
\qquad \phi(x)=-x\log_2x.
\tag{2.1}
\]

For a balanced monotone Boolean gadget with \(R=H/(I-1)\), influence \(I\), and designated singleton coefficient \(c\), depth-\(d\) disjoint self-composition followed by the exact nine-host shared-core graft gives

\[
R_d'-R=
\frac{K(c^d)-d_0R}{\alpha I^d+B},
\tag{2.2}
\]

\[
I_d'=\frac{261}{128}+\alpha(I^d-1),
\qquad
c_d'=\frac{57}{256}+\frac{c^d}{256}.
\tag{2.3}
\]

The denominator in (2.2) is positive, so the sign is governed exactly by

\[
N_d:=K(c^d)-d_0R.
\tag{2.4}
\]

The peer construction supplies the exact singleton recurrence. Starting from its source rational \(c_1=14593/65536\), the checker reconstructs \(c_7\) by exact rational arithmetic. In particular

\[
0<c_7<\frac14.
\tag{2.5}
\]

No packet integrality, interpolated spectral law, or credit-free relaxation is used: this is the same actual finite Boolean shared-coordinate construction as the consumed peer theorem.

## 3. Certified finite range: \(d=1,\ldots,14\)

The accompanying standard-library checker uses exact rational recurrence data and outward Decimal intervals for the entropy evaluation. Python's `Decimal.ln` is correctly rounded; the checker evaluates it at 90 digits and then pads by \(10^{-65}\), while all arithmetic interval endpoints use directed rounding.

It certifies the following signs for (2.4):

| \(d\) | certified interval information for \(N_d\) | sign |
|---:|---|:---:|
| 1 | \(N_1<-2.0136846519597\times10^{-2}\) | \(-\) |
| 2 | \(N_2<-1.2150974833627\times10^{-3}\) | \(-\) |
| 3 | \(N_3<-4.5530740259\times10^{-5}\) | \(-\) |
| 4 | \(2.2630508414240\times10^{-7}<N_4<2.2630508414241\times10^{-7}\) | \(+\) |
| 5 | \(N_5<-3.29768482166\times10^{-6}\) | \(-\) |
| 6 | \(N_6<-4.91382487750\times10^{-6}\) | \(-\) |
| 7 | \(N_7<-5.32241932824\times10^{-6}\) | \(-\) |
| 8 | \(N_8<-5.41618799757\times10^{-6}\) | \(-\) |
| 9--14 | each upper endpoint is \(<-5.4372\times10^{-6}\) | \(-\) |

The complete endpoints are in `CHECK_OUTPUT.txt`. Thus among \(1\le d\le14\), exactly \(d=4\) increases \(R\).

## 4. Analytic tail: every integer \(d\ge15\) is negative

Because \(c_7<1/4\), for every \(d\ge15\),

\[
0\le b:=c_7^d<4^{-15}=2^{-30}.
\tag{4.1}
\]

The source core has 512 Fourier masses

\[
p_{a,q}(b)=\left(\frac{a+bq}{512}\right)^2
\]

with the exact 19 \((a,q)\)-classes and multiplicities reproduced in `CHECKER.py`. For a nonzero class and \(0\le b\le2^{-30}\),

\[
|a+bq|>1,\qquad |a+bq|\le132,\qquad |q|\le18.
\]

Hence \(2^{-18}<p_{a,q}(b)<1/e\), so

\[
|\phi'(p_{a,q}(b))|<20
\]

and

\[
\left|\frac{dp_{a,q}}{db}\right|
\le \frac{2\cdot18\cdot132}{512^2}.
\]

Summing with total multiplicity 512 gives

\[
|H_{\rm core}'(b)|
<
512\cdot20\cdot\frac{2\cdot18\cdot132}{512^2}
=185.625.
\tag{4.2}
\]

For the remaining term in \(K\),

\[
\alpha[-\phi(b^2)+16(1-b^2)],
\]

its derivative has absolute value below \(10^{-3}\) on \(0\le b\le2^{-30}\): indeed \(b\log(1/b)\) is increasing throughout this tiny interval and its endpoint bound is already below \(10^{-7}\) before multiplication by \(\alpha\). Therefore

\[
|K'(b)|<186
\qquad (0\le b\le2^{-30}).
\tag{4.3}
\]

The checker independently encloses

\[
N_\infty:=K(0)-d_0R_7
<
-5.4432612844845406890880\times10^{-6}.
\tag{4.4}
\]

By the mean-value theorem and (4.1)--(4.3),

\[
N_d
\le N_\infty+186\,2^{-30}
<
-5.4432612\times10^{-6}+1.7322600\times10^{-7}
<0
\tag{4.5}
\]

for every integer \(d\ge15\).

Combining Sections 3 and 4 proves

\[
\boxed{N_d>0\ \Longleftrightarrow\ d=4\qquad\text{for every integer }d\ge1.}
\tag{4.6}
\]

Equivalently, **at the exact current \(F_7\) state, the only integer self-composition depth that gives an immediate increasing edge for this shared-core graft is \(d=4\).**

## 5. What is closed and what is not

The peer already proves that continuing the \(d=4\) edge after \(F_7\) has total possible positive tail below \(5.44\times10^{-118}\). Equation (4.6) now rules out every alternative *immediate* integer depth at \(F_7\). Thus changing only the self-composition depth does not produce another positive first step from the current state.

This statement is deliberately narrower than a global optimization theorem. It does **not** prove that an arbitrary mixed sequence which first accepts a negative step can never later exceed \(R_7\); it does not rule out a different shared host/core, a biased product point, or another composition-prime gate. It supplies no finite universal upper bound.

The currently certified balanced obstruction remains the peer value

\[
C_{\rm FEI}>
6.521850949550448184840160538860511501350329679\ldots,
\]

with old-reference comparable margin

\[
c_{F_7}>
0.2682037982017927393606421554420460054013187196.
\tag{5.1}
\]

**Full FEI remains OPEN / NOT PROVED.**

## 6. Replacement obligation and handoff

- `candidate_version`: all-gate inequality (G), tested on the exact source-valid nine-host shared-core family at the certified \(F_7\) state.
- `prior_missing_implication`: after the fixed-\(d=4\) tail closure, determine whether another integer depth can immediately raise the same source-valid obstruction.
- `new_proved_inference`: \(d=4\) is the unique positive integer depth at \(F_7\); the finite range is interval-certified and all \(d\ge15\) are excluded analytically.
- `exact_failed_claim`: “choose another integer self-composition depth at \(F_7\) to obtain a positive shared-core gain.”
- `replacement_obligation`: either control genuinely mixed negative-first depth sequences, or change a substantive ingredient of the same all-gate falsification problem (host/core geometry or product bias) rather than recomputing the closed \(d=4\) tail.
- `consumed_peer_artifact`: fleet04/B17 `20260922T014537Z-shared-graft-tail-closure/REPORT.md`, blob `9eaad387fb0d3812cb2b6c65d8510afc4639ae18`.
- `applied_to_claim`: peer equation \(R'_d-R=[K(c^d)-d_0R]/(\alpha I^d+B)\) at its certified \(F_7\) interval.
- `next_recipient`: fleet03/B18, with the composition-prime reduction from fleet01/B13 as the structural filter for any replacement gate.
- `implication_to_full_FEI`: mechanism elimination only. A finite dimension-independent all-gate upper bound is still unproved.

No novelty or publication-priority claim is made.
