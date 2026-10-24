# B12 / A060 run report: optimal constant-branch selector tax

- Run: `20261012T002107Z-account01-B12-optimal-selector-tax`
- Primary packet: `A060` (Composition sharpness)
- Stable gap: `FEI-B12-A060-SELECTOR-TAX-SHARPNESS`
- Attempt: `B12-A060-ATTEMPT-002`
- Claim: `B12-A060-SELECTOR-TAX-SHARPNESS-v2`
- Exact-scope mathematical status: **PROVED**
- Packet status: **DELIVERED_FOR_REVIEW**, not accepted or complete
- Full FEI status: **OPEN**

## Objective and previous value

This second bounded A060 pilot froze the same local functional as the previous
run:

\[
\frac{H(K)-H(D)/2}{I_x(K)},
\qquad K(+1,z)=1,\quad K(-1,z)=D(z),
\]

with (D) a genuine Boolean child and (x) one fresh selector.  The previous
value was the proved lower bound

\[
12-\frac94\log_2 9=4.8676687467\ldots
\]

from a two-bit point defect.  It was unknown whether that witness was sharp.

The new idea is to cancel the paired nonconstant Fourier contributions exactly.
The cancellation shows that the entire residual tax depends only on the bias
(p=\Pr[D=-1]).  This converts the all-dimensional Boolean optimization into
a one-variable calculus problem and determines its sharp constant.

## Main theorem: exact bias-only reduction

### PROVED

For every (n\geq0), every Boolean
(D:\{-1,1\}^n\to\{-1,1\}), and

\[
K(+1,z)=1,\qquad K(-1,z)=D(z),
\]

let (p=\Pr[D=-1]=(1-\mathbb ED)/2).  Then

\[
I_x(K)=p,\qquad I(K)=\frac12I(D)+p,
\]

and

\[
H(K)=\frac12H(D)+p c(p),
\]

where

\[
\begin{aligned}
c(p)=\frac1p\bigg[&2(1-p)^2\log_2\frac1{1-p}
+2p^2\log_2\frac1p+4p(1-p)\\
&-(1-2p)^2\log_2\frac1{|1-2p|}\bigg].
\end{aligned}
\]

The zero-log terms and endpoints are interpreted continuously.

### Proof

Write

\[
K=u+xv,qquad u=\frac{1+D}{2},\quad v=\frac{1-D}{2}.
\]

If (m=\widehat D(\varnothing)=1-2p), the two constant-frequency squared
masses of (K) are ((1-p)^2) and (p^2).  For every nonempty (S), the
single squared mass (widehat D(S)^2) is replaced by two masses
(widehat D(S)^2/4).  Their combined entropy is

\[
\frac12\widehat D(S)^2\log_2\frac1{\widehat D(S)^2}
+\widehat D(S)^2.
\]

Summing and using

\[
\sum_{S\ne\varnothing}\widehat D(S)^2
=1-m^2=4p(1-p)
\]

gives the entropy identity.  Characters containing (x) carry the full
Fourier mass of (v=\mathbf1_{\{D=-1\}}), so

\[
I_x(K)=\sum_S\widehat v(S)^2=\mathbb Ev^2=p.
\]

The data-degree contribution is exactly half that of (D), proving the
influence identity.  No inequality or external claim is used.

## Sharp constant

Define

\[
C_*=\max_{0\le p\le1}c(p).
\]

### PROVED

There is a unique maximizer (p_*\in(0,1/2)), and

\[
0.22944127<p_*<0.22944128,
\qquad
4.872321<C_*<4.872322.
\]

Numerically,

\[
p_*=0.2294412760815327967\ldots,qquad
C_*=4.8723210717843492888\ldots,
\]

where these longer decimals are **NUMERICAL**; the displayed interval bounds
are rigorous.

Let (A(p)=(\ln2)p c(p)).  For (p\ne1/2),

\[
A(p)=-2(1-p)^2\ln(1-p)-2p^2\ln p
+4(\ln2)p(1-p)+(1-2p)^2\ln|1-2p|.
\]

The sign of (c'(p)) is the sign of

\[
\begin{aligned}
F(p)=pA'(p)-A(p)
={}&2(1-p^2)\ln(1-p)-2p^2\ln p-4p^2\ln2\\
&-(1-4p^2)\ln|1-2p|.
\end{aligned}
\]

Direct differentiation yields

\[
F'(p)=4p\ln\frac{(1-2p)^2}{4p(1-p)}.
\]

The logarithm changes sign only at

\[
\alpha=\frac{1-1/\sqrt2}{2},\qquad
\beta=\frac{1+1/\sqrt2}{2}.
\]

Together with

\[
F(0+)=0,qquad F(1/2)=-2\ln2,qquad F(1-)=-4\ln2,
\]

this proves that (F) has exactly one zero (p_*\) and that (c) increases
before it and decreases afterward.  The rational-interval checker certifies
the root bracket and the bound (C_*<4.872322).

For sharpness over genuine Boolean functions, note that all Boolean biases are
dyadic and dyadic numbers are dense.  For every (p=k/2^n), some Boolean
function has exactly that density, and the exact identity gives tax ratio
(c(p)).  Choosing dyadic biases approaching (p_*) proves that no smaller
constant works.

## Exact near-extremal Boolean witness

Let (D_{10}) be (-1) on lexicographic indices (0,\ldots,234) of the
ten-cube and (+1) elsewhere.  Then

\[
p=\frac{235}{1024},\quad
\mathbb ED_{10}=\frac{277}{512},\quad
I(D_{10})=\frac{277}{256}.
\]

Its integer Walsh coefficients, grouped by absolute value, are

```text
2:768, 6:128, 10:64, 22:32, 42:28, 470:3, 554:1
```

with normalization (1/1024).  The eleven-bit splice (K_{11}) has

\[
I_x(K_{11})=\frac{235}{1024},\qquad
I(K_{11})=\frac{789}{1024},\qquad
\mathbb EK_{11}=\frac{789}{1024},
\]

and integer absolute-Walsh histogram

```text
2:1536, 6:256, 10:128, 22:64, 42:56, 470:7, 1578:1
```

with normalization (1/2048).  Rigorous interval evaluation gives

\[
H(D_{10})=2.7360726600842987160\ldots,
\]

\[
H(K_{11})=2.4861959444122207961\ldots,
\]

and

\[
\frac{H(K_{11})-H(D_{10})/2}{I_x(K_{11})}
=4.8723210430423538411\ldots>4.872321.
\]

Thus the earlier point-defect lower bound is valid but not sharp.  The new
witness lies within (3\times10^{-8}) of the numerical optimum.

Its actual FEI ratio is only

\[
\frac{H(K_{11})}{I(K_{11})}
=3.2266979050419697025\ldots.
\]

Disjoint tensor powers preserve this latter ratio.  They do not convert the
local additive coefficient (C_*) into a universal FEI lower bound.

## Closure consequence

### PROVED, restricted class

If the child obeys (H(D)\le C I(D)), then

\[
\begin{aligned}
H(K)&\le \frac C2I(D)+C_*p\\
&\le\max\{C,C_*\}\left(\frac12I(D)+p\right)\\
&=\max\{C,C_*\}I(K).
\end{aligned}
\]

Thus constant-branch fresh-selector extension preserves FEI with the optimal
scalar overhead (C_*).  This does not prove FEI for an arbitrary child and
does not cover arbitrary two-branch or overlapping-input compositions.

## Verification

The archived checker uses integer Walsh transforms and rational intervals for
all logarithmic sign claims.  Logarithms are range-reduced by powers of two
and enclosed by the positive atanh series with a geometric tail.

Command:

```text
TIMEFORMAT='real %3R user %3U sys %3S'; time python3 check_optimal_selector_tax.py
```

Results:

- exact root-sign certificate at (0.22944127) and (0.22944128);
- rigorous (C_*<4.872322);
- rigorous (235/1024) witness tax (>4.872321);
- exact Walsh histograms and rational influences for the 10/11-bit witness;
- exhaustive audit of 65,808 Boolean children on one through four data bits,
  excluding only the zero-tax (D\equiv1) endpoint;
- zero failures;
- randomness: none;
- observed runtime: 4.664 seconds under Python 3.12.14.

The small-cube maximum was the earlier (p=1/4) value
(4.867668746754797\ldots), confirming why the improvement first appears at
higher bias resolution.

## Obstruction and scope audit

- **Addressing/multiplexers:** the identity is exact for any such child, but it
  retains (H(D)/2), which must be paid by the child influence budget.  No
  address label is charged coordinate-by-coordinate.
- **Rare restrictions and sparse defects:** all biases are included, including
  (p\to0), where (c(p)\to4).  Rare logarithmic costs are not discarded.
- **Near tensors:** the local tax and actual FEI ratio are distinguished; only
  the latter is preserved by disjoint tensor powers.
- **Actual prime Boolean gates:** the explicit 10-bit child and 11-bit splice
  are genuine Boolean gates with exact Walsh certificates.
- **Parity-zero erasure:** the child mean and constant Fourier masses are kept
  explicitly.
- **Selector-erasure obstruction:** no contradiction; this theorem has one
  constant branch and retains half the complete child entropy.  It does not
  assert selector-only payment for arbitrary neighboring branches.
- **Shared-variable interference:** no overlapping-input or reused-selector
  product law is asserted.
- **Activation equivalence:** selector influence is exactly (p), and data
  influence is exactly (I(D)/2); neither is double-counted.

## Mathematical delta and acceptance

Previous value/status:

- `B12-A060-SELECTOR-TAX-SHARPNESS-v1`: **PROVED** finite lower bound
  (4.8676687467\ldots), independent review pending.

New value/status:

- `B12-A060-SELECTOR-TAX-SHARPNESS-v2`: **PROVED** exact all-dimensional
  bias reduction and sharp coefficient (C_*\in(4.872321,4.872322)),
  independent review pending.

Version 2 supersedes version 1 as the sharpness result but preserves version
1 as a valid witness.  The already refuted coefficient-four helper remains
refuted.  No other campaign claim is invalidated.

The A060 mathematical deliverables are complete at contributor-proof level:
exact examples, necessary coefficient, means/correlations, and the
additive-versus-multiplicative distinction are all present.  Packet acceptance
still requires independent full-source reconstruction by A090 and A091 and
B20 evidence adoption.  No independent review was observed in this run.

## Sources actually read

Open-problems current files:

- `CURRENT_STATUS.md`, blob
  `74f6ae761739455083804505ba0e0fd7aaf2f3e2`;
- `STREAM_PACKET_INDEX.json`, blob
  `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`;
- `assignments/B12.json`, blob
  `40935ac651643a17815d0addf664ec4c1c0313cc`;
- `EXECUTION_PROTOCOL.json`, blob
  `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
- `PACKET_STATUS.json`, blob
  `66a78ef3249a89d481a47320f990dc2aec002ccb`;
- `CLAIM_REGISTRY.json`, blob
  `bef50513c8309b0e601aec42470bc09162f26ea8`;
- `OBSTRUCTION_REGISTRY.json`, blob
  `d9c8b8632d019aa9e4d5c7394001d116fd21d94e`.

Previous complete B12 source:

- `runs/B12/20261011T232432Z-account01-B12-selector-tax-sharpness/REPORT.md`,
  open-problems commit `12f0dfa4ab3a5c94f58d717d17dbb64ee61953ac`,
  blob `a46cdba579b4a5bb54a9632ed8d41fa777fee984`;
- matching Brain handoff at commit
  `4eb49018fd88a66482cbedfd38a75c11793f1048`, same report blob.

Brain mirrors freshly checked:

- `CURRENT_STATUS.md`, blob
  `74f6ae761739455083804505ba0e0fd7aaf2f3e2`;
- `STREAM_PACKET_INDEX.json`, blob
  `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`;
- `assignments/B12.json`, blob
  `40935ac651643a17815d0addf664ec4c1c0313cc`.

No literature-novelty claim is made.  The proof is a self-contained exact
calculation and calculus argument.

## Execution and handoff

- Natural mathematical execution: completed.
- New workers: none.
- Schedule changes: none.
- Model identifier exposed to this run: not exposed.
- Reasoning-effort selector exposed to this run: not exposed.
- Native Brain ingestion: not claimed.
- Independent review: pending.

Next action: A090 should reconstruct the Fourier cancellation and endpoint
calculus from source; A091 should adversarially verify sharpness over dyadic
Boolean biases and the separation from the actual tensor-stable FEI ratio.
After those reviews, B20 can adopt A060 as complete at its restricted scope.
B12 should then move to A057 or A059 rather than opening a third unreviewed
composition candidate.

