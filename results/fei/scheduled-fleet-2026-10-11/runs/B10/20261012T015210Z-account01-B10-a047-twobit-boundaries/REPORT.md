# B10 / A047 — two-bit continuum reduction and sharp endpoint asymptotics

**Run:** `20261012T015210Z-account01-B10-a047-twobit-boundaries`  
**Primary packet:** A047 (Boundary search)  
**Attempt:** `A047-HALF-TAX-TWOBIT-1`  
**Frozen candidate:** `B10-A046-HALF-BIAS-TAX@1`  
**New claim:** `B10-A047-TWOBIT-ENDPOINTS@1`  
**Status:** endpoint theorem author-proved; bounded diagnostics passed; full two-bit continuum and full FEI remain **OPEN**.

## Outcome

The exact half-tax candidate is

\[
J_A\le M_A+\frac12\Delta_A,\qquad
\Delta_A=\sum_{i\in A}\left[h_2(p_i)+\log_2\max(p_i,1-p_i)\right].
\]

This run proves the complete Boolean classification for two input bits and
reduces the only nontrivial class to one explicit function $D(p,q)$. It then
settles the sharp rare revealed boundary to the first nonzero order. At the
unique coefficient-$1/2$ saturation point,

\[
D(p,1/4)=\frac{\frac12-\ln2}{\ln2}\,p
          +O\!\left(p^2\ln\frac1p\right)<0
\]

for all sufficiently small $p$. Thus the previously known ratio limit
$1/2$ is approached from below; it does not conceal a boundary
counterexample. The opposite endpoint $p\uparrow1$ is also strictly safe.

This is mathematical movement but not a proof of the candidate: a compact
interior continuum inequality and genuinely joint corners remain unpaid.

## Exact two-bit reduction

Up to output sign, input complements, and swapping the inputs, every Boolean
gate on two bits is one of:

1. constant;
2. dictator;
3. parity;
4. a one-point defect (equivalently its three-point complement).

Output sign does not change squared Fourier masses. Constants and irrelevant
reveals have $J=M=0$. Revealing a dictator gives $J=0\le M$.
For parity, the squared spectrum is a product law and physical restriction
changes only a sign, so $J=0\le M$. Therefore only the point defect matters.

Let $p$ be the probability of the exceptional value of the revealed bit and
$q$ the probability of the exceptional value of the other bit. Put

\[
s=4q(1-q),\qquad c=4q^2.
\]

The four squared biased Fourier masses are

\[
(1-2pq)^2,\quad 4q^2p(1-p),\quad
4p^2q(1-q),\quad4p(1-p)q(1-q).
\]

They give the exact identities

\[
J=h_2(sp)-p h_2(s),
\]

\[
M=(1-sp)h_2\!\left(\frac{cp(1-p)}{1-sp}\right)+sp h_2(p).
\]

Hence every two-bit instance is reduced to

\[
D(p,q):=J-M-\frac12\delta(p)\le0,
\quad
\delta(p)=\min(p,1-p)\log_2\frac{\max(p,1-p)}{\min(p,1-p)}.
\]

## Proved endpoint expansion

Using

\[
h_2(x)=\frac{x\ln(1/x)+x+O(x^2)}{\ln2}
\]

in the exact formula yields, for fixed $q\in(0,1)$,

\[
D(p,q)=\frac p{\ln2}
\left[-8\left(q-\frac14\right)^2\ln\frac1p+B(q)\right]
+O_q\!\left(p^2\ln\frac1p\right),
\]

where

\[
B(q)=4q(1-2q)+(1-4q(1-q))\ln(1-4q(1-q))
     +4q^2\ln(4q^2).
\]

The remainder is uniform on a compact neighborhood of $q=1/4$: the entropy
remainders are uniform there, and replacing
$cp(1-p)/(1-sp)$ by $cp$ costs
$O(p^2\ln(1/p))$. The logarithmic coefficient equals
$-8(q-1/4)^2$, so it is negative except at $q=1/4$. At that unique point

\[
B(1/4)=\frac12-\ln2<0,
\]

because $\ln2=\int_0^1(1+x)^{-1}dx>1/2$.
Therefore the rare boundary is valid for every fixed $q$, and uniformly in
a neighborhood of its only saturation point.

For $\varepsilon=1-p\downarrow0$ and fixed $q\ne1/2$, the same expansion
at the other endpoint gives

\[
D(1-\varepsilon,q)
=-\frac{4q+\frac12}{\ln2}\,
  \varepsilon\ln\frac1\varepsilon+O_q(\varepsilon)<0.
\]

At $q=1/2$, $J=M$ exactly and $D=-\delta/2$. For fixed interior $p$,
the limits $q\downarrow0$ and $q\uparrow1$ are respectively
$-\delta(p)/2$ and
$-h_2(4p(1-p))-\delta(p)/2$, both nonpositive.

Full derivation is preserved in `BOUNDARY_ASYMPTOTICS.tex`.

## Bounded deterministic diagnostic

`verify_twobit_boundaries.py` performed:

- 159,201 interior point-defect evaluations on
  $p,q\in\{1/400,\ldots,399/400\}$;
- 967 high-precision evaluations in the dangerous tube
  $p=2^{-k}$,
  $q=1/4+j/(40\sqrt{k})$, through $k=512$, plus joint endpoint paths;
- 1,980 high-precision evaluations at
  $p=1-2^{-k}$, through $k=256$.

No positive gap occurred. The interior maximum gap was zero at the balanced
degeneracy $(p,q)=(1/2,1/2)$. In the rare tube the largest ratio
$(J-M)/\delta$ was approximately
$0.4994557568758681$ at $p=2^{-512},q=1/4$, matching approach from below.
The computed $D(p,1/4)/p$ converged to

\[
\frac{1/2-\ln2}{\ln2}
=-0.2786524795555182963\ldots.
\]

Command:

`python3 verify_twobit_boundaries.py > CHECK.out`

Randomness: none. Decimal precision: 240 digits. These calculations are
diagnostics, not outward-rounded interval certificates.

## Mandatory controls and scope

- The corrected B09 certificate refutes only $J\le M$, with
  $J-M>0.1195$ for a biased two-bit gate.
- The prior A046 intake proves every coefficient below $1/2$ fails on the
  rare AND boundary. This run does not change that lower bound.
- The B05 rare-refund, weighted pivotal/TC, fixed-prefix, raw-convolution, and
  overlap-product failures concern distinct quantities. None is promoted into
  a falsifier of this candidate.
- Fixed spectral Rényi orders below one fail on point defects; this candidate
  uses Shannon conditional entropy and does not infer a Rényi replacement.
- A local half-tax theorem, even if eventually proved, would still require a
  nonreusing global payment and terminal entropy. It would not by itself prove
  FEI.

## Source pins

- B10 contract blob `00939b50127519cdd7089770b49884220fa34d1d`.
- Protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Packet status blob `1beba565780ac4c3c1f28a00b20ca4d5e4e59ebb`.
- Claim registry blob `bceaed2294e4dab574d363750858c6d3866137f8`.
- Obstruction registry blob `e111933338dff1d7798c5e59b43700bbf30f7b96`.
- A046 frozen-candidate report blob
  `5c37e135ea3cd03fbaeefd635e79904e7683d1d5`.
- Corrected B09 interval report/source are preserved at the canonical
  `verification/B09_interval_repair_20261011/` path.

## Remaining obstacle and handoff

The sharp rare revealed boundary is no longer the leading two-bit threat.
The exact next action is to prove $D(p,q)\le0$ on a compact interior
rectangle and close joint $q\to0,1$ corners, using either a monotonicity
decomposition or signed rational logarithmic intervals. Only then may the
two-bit continuum case be called complete.

Route the frozen formula and endpoint theorem to A049 only if a certified
violation appears; otherwise route them to A048 for tensor stress and to A087
or A092 for independent reconstruction. No independent review, packet
acceptance, full-FEI solution, native ingestion, scheduler change, merge,
deployment, or public release is claimed. The runtime exposed no separate
model or reasoning-effort selector.

