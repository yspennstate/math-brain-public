# B16 — shared-graft tail theorem: the recursive balanced obstruction converges after one more effective step

**Outcome:** `ESSENTIAL_STEP_APPLIED` to the exact tail inference left open by the current all-gate obstruction programme. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository control and source mathematics were read directly; no authenticated cognitive-brain retrieval/runtime entered the proof.

## 0. Live target and exact peer version consumed

Fresh owner control revision `2026-09-22.2` directs all FEI workers to the all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le \sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},\qquad V_u=4u(1-u),
\tag{G}
\]

and to prove or falsify decomposable/AND extremality. That extremality is already source-validly falsified: on the balanced-uniform slice `(G)` is exactly `H(G)<=C(I(G)-1)`, constant-for-constant equivalent to full FEI, and explicit balanced gates exceed the old read-once cap. I therefore do not repeat an arity sweep or the already completed arity-10 falsifier.

The exact named other-account candidate consumed here is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`, blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`, together with its source checker blob `dc24627e2c157e87992698b4e43a28315548d3fc`.

That report continues fleet01/B18's genuine Boolean shared-core transform. For a balanced monotone gadget with influence `I>1`, excess ratio

\[
R=\frac{H}{I-1},
\]

and designated singleton coefficient `c`, one transform gives

\[
I'=\frac{261}{128}+\frac9{256}(I^4-1),
\tag{0.1}
\]

\[
c'=\frac{57}{256}+\frac{c^4}{256},
\tag{0.2}
\]

and

\[
R'-R=
\frac{K(c^4)-\frac{133}{128}R}
{\frac9{256}I^4+\frac{257}{256}},
\tag{0.3}
\]

where

\[
K(b)=H_{\rm core}(b)+\frac9{256}\bigl[-\phi(b^2)+16(1-b^2)\bigr],
\qquad \phi(x)=-x\log_2x.
\tag{0.4}
\]

The peer certifies the source-valid gates through `F_4`, in particular

\[
\begin{aligned}
6.5218509485644448965490881329959858569477358114202361
&<R_4\\
&<6.5218509485644448965496895824490791318643557898359042,
\end{aligned}
\tag{0.5}
\]

and leaves as its exact next inference a theorem controlling all later rounds of (0.1)--(0.3), rather than certifying one enormous rational round at a time.

I also consume fleet04/B12's completed two-step Poincare-refund theorem, which shows that the arity-10 balanced prime gate is not an intrinsic depth-two obstruction: every branch-adaptive two-step block is safe in the `Gamma_0=0` entropy/Poincare ledger. This is why the present run treats the recursive shared-graft family as a lower-bound obstruction to be *settled*, not as evidence for another one-step universal criterion.

## 1. Exact convex-combination form of the recurrence

Write

\[
\beta=\frac{133}{128},\qquad
T(c)=\frac{128}{133}K(c^4).
\tag{1.1}
\]

Because the denominator in (0.3) is exactly `I'-1`,

\[
I'-1=\frac9{256}I^4+\frac{257}{256},
\]

(0.3) is equivalent to

\[
\boxed{
R'=(1-w)R+wT(c),
\qquad
w=\frac{\beta}{I'-1}.
}
\tag{1.2}
\]

Thus every new excess ratio is a literal convex interpolation between the old ratio and a scalar threshold `T(c)` whenever `0<w<1`. The point of the tail proof is that the threshold stabilizes while `w` collapses super-quartically.

## 2. A uniform threshold interval for every later round

The exact singleton recurrence starting from the inherited

\[
c_1=\frac{14593}{65536}
\]

gives

\[
c_4=
0.222665852283236823458540779730159822307896295\ldots .
\tag{2.1}
\]

Let

\[
J_c=[0.22266585228,\ 0.22266585229].
\]

Since `F(c)=57/256+c^4/256` is increasing and exact rational arithmetic gives

\[
F(0.22266585228)>0.22266585228,
\qquad
F(0.22266585229)<0.22266585229,
\tag{2.2}
\]

`J_c` is forward invariant and contains `c_4`; hence `c_t in J_c` for every `t>=4`.

To control `T` rigorously, reconstruct the source core in the inherited checker. Its Walsh data satisfy

\[
|A_s|\le114,\qquad |Q_s|\le18,
\]

and whenever `A_s=0` one also has `Q_s=0`; otherwise `|A_s|>=2`. On

\[
0.0024\le b\le0.0026
\]

this gives

\[
1.95<|A_s+bQ_s|<115
\]

for every nonzero core amplitude. For

\[
p_s(b)=\frac{(A_s+bQ_s)^2}{512^2},
\]

we have

\[
|\phi'(p_s)|<18,
\qquad
|p_s'|\le\frac{2\cdot18\cdot115}{512^2}.
\]

Summing the 512 terms gives `|H_core'(b)|<146`. The remaining scalar term in (0.4) contributes less than `0.01` in derivative magnitude on the same interval. Therefore the deliberately loose but rigorous bound

\[
\boxed{|K'(b)|<200}
\tag{2.3}
\]

holds throughout the entire relevant interval.

Evaluate `K` by exact rational log intervals at the low-denominator centre

\[
b_0=0.002458184508619374.
\]

The exact `b_4=c_4^4` differs from `b_0` by less than `4.521\times10^{-20}`. Combining the exact interval evaluation with (2.3) gives

\[
\boxed{
6.521851167347822388384297326823537716400838569
<T(c_4)
<6.521851167347822405785933006746517402280652165.
}
\tag{2.4}
\]

Using the whole invariant interval `J_c` instead gives the all-future enclosure

\[
\boxed{
6.521851167290336696020501001116840568369969012
<T(c_t)
<6.521851167405308098149729332453214550311521722
}
\tag{2.5}
\]

for every `t>=4`.

## 3. One more effective step gives a new certified FEI lower bound

The exact influence recurrence gives

\[
I_4=
8.989183126916552511946952686219547074893649501\ldots
\]

and

\[
I_5=
231.5571615297100612740059318140455420921042533\ldots .
\tag{3.1}
\]

Hence

\[
w_4=\frac{133/128}{I_5-1}
=0.0045067457159256547692771845041936253\ldots .
\]

Apply the monotone affine map (1.2) to the certified `R_4` interval (0.5) and the exact threshold interval (2.4). This yields

\[
\boxed{
\begin{aligned}
6.521850949550445945776161786330284662707526592
&<R_5\\
&<6.521850949550445945855185272254223770969081665.
\end{aligned}}
\tag{3.2}
\]

`F_5` is a genuine finite balanced monotone Boolean gate by the inherited transform. Balanced self-composition therefore gives

\[
\frac{H(F_5^{\circ d})}{I(F_5^{\circ d})}\to R_5.
\]

Consequently

\[
\boxed{
C_{\rm FEI}>6.5218509495504459457.
}
\tag{3.3}
\]

This is a strict source-valid lower bound, not an upper bound and not a proof of FEI.

## 4. Complete tail theorem: every later round improves, but the entire remaining gain is below 4.1e-15

The threshold lower bound in (2.5) exceeds the upper endpoint in (3.2) by more than

\[
2.1773989\times10^{-7}.
\tag{4.1}
\]

Meanwhile `I_5>200`, so the next interpolation weight obeys

\[
w_5
<\frac{133/128}{(9/256)200^4}
<1.8472223\times10^{-8}.
\tag{4.2}
\]

After this, `I_6>56,250,000`. For every later iterate, (0.1) implies

\[
I_{t+1}-1>I_t^2,
\]

so the subsequent reciprocal weights square at least geometrically. A direct rational bound gives

\[
\sum_{t\ge5}w_t<1.8472224\times10^{-8}.
\tag{4.3}
\]

Using the uniform threshold upper bound in (2.5), the total possible increase after `R_5` is therefore

\[
\boxed{
\sum_{t\ge5}(R_{t+1}-R_t)
<4.024264\times10^{-15}.
}
\tag{4.4}
\]

In particular the entire future increase is far smaller than the threshold gap (4.1). Inductively every later `R_t` stays below the common threshold lower bound, so every increment is strictly positive. Thus `R_t` is strictly increasing for `t>=4`, converges, and its limit `R_infty` satisfies

\[
\boxed{
6.5218509495504459457
<R_\infty
<6.521850949550449970118998440020895162082174085
<6.5218509495504501.
}
\tag{4.5}
\]

This settles the infinite source-valid shared-graft tail. The limiting threshold itself is around `6.5218511673`, but the ratio cannot approach it: the influence explosion makes the interpolation weights summable after `F_5`. In particular, further round-by-round certification of this exact recurrence can improve (3.3) by at most about four quadrillionths.

## 5. Exact old/new implication and status

**Exact candidate version.** fleet03/B18 report blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`, equations (1.3)--(1.6) there, i.e. (0.1)--(0.4) above.

**Old missing implication.** Control *all later* source-valid shared-graft rounds: prove a stable interval for the singleton coefficient/threshold, determine whether the certified positive increments continue, and bound their total rather than certifying one enormous rational round at a time.

**New proved inference.** Equations (2.5), (3.2), and (4.4)--(4.5) close that tail completely. The source family continues to improve strictly but essentially saturates after `F_5`. It yields the improved lower bound (3.3), and it cannot by itself drive the FEI lower floor materially beyond `6.52185094955045`.

**Replacement obligation.** Full FEI still requires a finite *upper* bound for every Boolean gate/bias instance, equivalently a universal potential satisfying `(G)`. The shared-graft family is now a settled obstruction/lower-bound calibration, not a reason to spend more FEI runs on additional recurrence rounds. A successor proof must attack the universal signed block/potential mechanism (retaining child continuation, as in fleet02/B16 and fleet04/B12) or produce a genuinely stronger gate construction outside this settled recurrence.

**Classification:** `ESSENTIAL_STEP_APPLIED` for the exact peer tail inference; **not** `FULL_PROOF_CANDIDATE`.

## 6. Verification boundary

`check_b16_shared_graft_tail.py` is standard-library-only. It reconstructs the inherited 9-bit core Walsh data, proves the data bounds used for the derivative envelope, evaluates `K(b_0)` with exact rational atanh/log intervals, computes the exact `c_4,I_4,I_5` recurrences, imports only the certified `R_4` interval from the named peer report, proves the invariant `c` interval, the `R_5` enclosure, the uniform threshold enclosure, and the all-future tail bound.

Local execution returned `PASS`.

Checker SHA-256: `7ae78d4831bca13abf5a83ef395b3c57d304391a7906f04363dafa42f5e6fd84`.

Captured output SHA-256: `e39d8e023e86998f810c8907e50fc98a3d8d5ac23569bccae0f29d4da0d8acf5`.

No novelty/publication-priority claim is made. Full unrestricted FEI remains **OPEN / NOT PROVED**.
