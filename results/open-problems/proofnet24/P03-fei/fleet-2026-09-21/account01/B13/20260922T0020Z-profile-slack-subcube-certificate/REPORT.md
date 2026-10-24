# B13 FEI campaign A — near-minimal folded-influence profile forces the selected physical certificate

**Run:** `20260922T001652Z-account01-B13-r11`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Classification:** **ESSENTIAL_STEP_APPLIED**. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Owner execution order:** `FEI-PROOF-EXECUTION-20260921T230620Z`, campaign A assignment: prove the structural condition actually needed by the selected restriction.

No novelty/publication-priority claim is made.

## 0. Exact candidate and peer versions consumed

The campaign-A lead candidate used here is the latest complete account01/B18 compiler visible on fresh scientific `master`:

- `account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.

Its complete sufficient statement is: for fixed universal `gamma>0`, `K<infinity`, `lambda>=0`, full FEI follows if every nonconstant physical-restriction core maximizing `G_lambda/J` above the scalar low-ratio threshold has one physical block/survivor certificate

\[
c_j(A)\ge\gamma j_j,
\qquad
E_A-\lambda\Lambda_A\le K h_2(j_j).
\]

The exact other-account inputs applied, rather than merely cited, are:

1. **account02/B14**, `20260921T210915Z-crossing-information-selector/REPORT.md`, blob `673dbf5d2bc162fc43b7931e88a5449fce2a219a`. It proves the Boolean-square pivotality boundary estimate and the physical crossing/information conversion.
2. **account02/B12**, `20260921T175134Z-physical-erasure-budget/REPORT.md`, blob `4d83eff4cf5396b2d5a14ed577ad55f0ff5c6990`. It identifies the support-isoperimetric excess and imports Ellis cube-isoperimetric stability in the form
   \[
   \delta\le {2\epsilon_{\rm iso}\over \log_2(1/\epsilon_{\rm iso})}
   \]
   below an absolute stability threshold `epsilon_E`.
3. **account04/B14**, `20260921T221102Z-recursive-certified-peeling/REPORT.md`, blob `253268f70202891aa12c36d2ff4cf76519fa8241`. It proves that a **maximum folded-influence** pivot whose pivotality support is within `q/(16r)` of a codimension-`r` coordinate subcube supplies an actual lead-candidate certificate with
   \[
   (\gamma,K)=(14/15,12)
   \]
   for every `lambda>=0`.

The newer account01/B14 adaptive pivotality report, `20260921T224055Z-adaptive-pivotality-selector/REPORT.md`, blob `585cbdfc282e636c95b70bd479d4c720b19f1948`, is compatible but not substituted for the campaign lead. Its folded Boolean-square lemma is rederived below in the exact form needed.

The half-band correction in the live `RESEARCH_STATE.md` was retained: no Brownian finite-window positive-current estimate, and no constant derived from that refuted step, is used below.

## 1. Compact conditional end-to-end chain and the old gap

Work in the median-character gauge, so every active folded influence is an ordinary influence

\[
0<p_i=\operatorname{Inf}_i(f)\le {1\over2},
\qquad
J=\sum_i p_i.
\]

On a high `G_lambda/J` critical core, the lead compiler reduces full FEI to finding one actual physical certificate. Account04/B14 already closes the branch where a **maximum-influence** pivot `x`, with `p=p_x`, has a codimension-`r` coordinate-subcube proxy `Q` for its pivotality support `E_x` satisfying

\[
 e:=\mu(E_x\triangle Q)\le {2^{-r}\over16r}.
\tag{1.1}
\]

The old first missing structural inference was therefore:

> force (1.1) from a property that is genuinely available on the selected critical core, without assuming small mixed-depth defect and without reviving fixed-relative `q/16`.

This report proves such an inference from a **two-sided folded influence profile slack**. It gives a new certified branch and leaves an explicit complementary spread branch.

## 2. Universal two-sided pivotality/profile inequality

For an active target `j`, let `Y_j` be its **folded pivotality event**: the usual pivotality indicator if `Inf_j(f)<=1/2`, and its complement otherwise. In the median gauge this simply has density

\[
p_j=\Pr(Y_j=1)\le {1\over2}.
\]

For `i!=j`, write `Inf_i(Y_j)` for the physical boundary of this event in direction `i`.

### Lemma 2.1 — Boolean square capacity

For every pair `i!=j`,

\[
\boxed{\operatorname{Inf}_i(Y_j)\le2p_i.}
\tag{2.1}
\]

#### Proof

Freeze every coordinate except `i,j`. If the `j`-pivotality status changes across the `i` direction, then on that Boolean square exactly one of the two `j`-edges is bichromatic. A four-cycle has an even number of bichromatic edges, so exactly one of the two `i`-edges is bichromatic. Hence every square counted by `Inf_i(Y_j)` contributes exactly `1/2` to the conditional `i`-influence of the median-gauged Boolean function. Averaging gives (2.1). Complementing the pivotality event does not change its boundary. QED.

This is the account02/B14 square mechanism, now used against the *whole* support boundary rather than one prescribed reveal.

### Theorem 2.2 — folded influence profile inequality

For every active coordinate `j`,

\[
\boxed{
J-p_j\ge p_j\log_2{1\over p_j}.
}
\tag{2.2}
\]

Equivalently,

\[
\boxed{
J\ge p_j\left(1+\log_2{1\over p_j}\right).
}
\tag{2.3}
\]

#### Proof

Let
\[
b_j:=\sum_{i\ne j}\operatorname{Inf}_i(Y_j)
\]
be the total physical edge boundary of the folded pivotality event. The cube edge-isoperimetric inequality gives

\[
b_j\ge2p_j\log_2{1\over p_j}.
\tag{2.4}
\]

On the other hand, summing Lemma 2.1 gives

\[
b_j\le2\sum_{i\ne j}p_i=2(J-p_j).
\tag{2.5}
\]

Combine (2.4) and (2.5). QED.

This is a genuinely two-sided Booleanity constraint: the rarity of the `j`-pivotality event must be supported by enough **other original-coordinate folded influence**. It is false as a generic statement about arbitrary spectral subset laws because the proof uses the physical Boolean-square relation.

## 3. The profile slack controls the actual support-isoperimetric deficit

Put

\[
L_j:=\log_2{1\over p_j},
\qquad
\Theta_j:={J-p_j\over p_j}-L_j\ge0.
\tag{3.1}
\]

For the folded pivotality support, define its normalized isoperimetric excess

\[
\epsilon_{\rm iso,j}:={b_j-2p_jL_j\over2p_j}\ge0.
\tag{3.2}
\]

### Theorem 3.1 — profile slack dominates geometric support slack

\[
\boxed{0\le\epsilon_{\rm iso,j}\le\Theta_j.}
\tag{3.3}
\]

#### Proof

The lower bound is edge isoperimetry. The upper bound follows directly from (2.5):

\[
\epsilon_{\rm iso,j}
\le {2(J-p_j)-2p_jL_j\over2p_j}
=\Theta_j.
\]
QED.

This is the main structural bridge of the run. It converts a scalar folded-influence profile statement into the **exact geometric slack** consumed by the account02/B12 Ellis-stability theorem. It does not use the derivative energy `d_j`; in particular it remains informative even when the internal derivative-sign defect is large.

## 4. New certificate theorem from near-minimal global folded influence

Let `epsilon_E>0` denote the absolute small-excess threshold in the Ellis-stability input used by account02/B12/account04. No numerical value is assumed.

Choose a maximum folded-influence coordinate `x` and put

\[
p:=p_x,
\qquad
L:=\log_2(1/p),
\qquad
\Theta:={J-p\over p}-L.
\tag{4.1}
\]

Assume `p<=1/4`, hence `L>=2`.

### Theorem 4.1 — profile-slack-to-physical-certificate

If

\[
\boxed{
\Theta\le
\min\left\{\epsilon_E,{1\over16L}\right\},
}
\tag{4.2}
\]

then the folded pivotality support of `x` has a coordinate-subcube proxy `Q` of codimension `r` with density `q=2^{-r}` satisfying

\[
\boxed{
\mu(E_x\triangle Q)\le {q\over16r}.
}
\tag{4.3}
\]

Consequently the defining physical block `Z` is a genuine account01/B18 certificate with

\[
\boxed{
 c_x(Z)\ge {14\over15}p,
\qquad
E_Z-\lambda\Lambda_Z\le12h_2(p)
}
\tag{4.4}
\]

for every `lambda>=0`.

#### Proof

By Theorem 3.1,

\[
0\le\epsilon_{\rm iso,x}\le\Theta\le\epsilon_E,
\]
so the account02/B12 Ellis-stability theorem applies. If the isoperimetric excess is zero, the equality case is an exact coordinate subcube and (4.3) is immediate. Otherwise it supplies `Q` with relative support error

\[
\delta:={\mu(E_x\triangle Q)\over p}
\le
{2\epsilon_{\rm iso,x}\over
 \log_2(1/\epsilon_{\rm iso,x})}.
\tag{4.5}
\]

The function `2t/log_2(1/t)` is increasing for `0<t<1`. Since `Theta<=1/(16L)` and `L>=2`,

\[
\log_2(1/\Theta)\ge\log_2(16L)\ge5,
\]
so

\[
\boxed{
\delta\le {2\Theta\over\log_2(1/\Theta)}
\le {1\over40L}.
}
\tag{4.6}
\]

Let `q=2^{-r}=mu(Q)`. Symmetric-difference error controls density error, hence

\[
q\ge(1-\delta)p.
\tag{4.7}
\]

Since `delta<=1/(40L)<=1/80<1/2`,

\[
r=\log_2(1/q)
\le L+\log_2{1\over1-\delta}<L+1.
\tag{4.8}
\]

Using (4.6) and (4.8),

\[
\delta(16r+1)
< {16L+17\over40L}<1
\qquad(L\ge2).
\tag{4.9}
\]

Thus

\[
\delta\le {1-\delta\over16r}.
\]
Multiplying by `p` and using (4.7) yields

\[
e:=\mu(E_x\triangle Q)=\delta p
\le{(1-\delta)p\over16r}
\le{q\over16r},
\]
which is (4.3).

Because `x` is maximum folded influence, every physical control in `Z` has influence at most `p`, so `I_Z<=rp`. Therefore all hypotheses of account04/B14's certified near-subcube theorem hold. That theorem gives

\[
c_x(Z)\ge14p/15,
\qquad
\Delta_ZH\le12I_Z\le12h_2(p).
\]
Finally the corrected erasure and activation refund satisfy

\[
E_Z-\lambda\Lambda_Z\le E_Z\le\Delta_ZH,
\]
which proves (4.4). QED.

### Corollary 4.2 — a new exact terminal-profile gap

At any centered high-ratio core with `p_max<=1/4` on which the current certified near-subcube selector **does not** fire at a maximum-influence pivot, writing `p=p_max`, `L=log_2(1/p)`, one must have

\[
\boxed{
{J-p\over p}-L
>
\min\left\{\epsilon_E,{1\over16L}\right\}.
}
\tag{4.10}
\]

Equivalently,

\[
\boxed{
J>
 p\left(
 1+L+\min\{\epsilon_E,1/(16L)\}
 \right).
}
\tag{4.11}
\]

This is a new scalar description of part of the terminal class. Previously terminality was expressed only as separation of the pivotality support from all `q/(16r)` subcubes or as a positive depth-defect condition. Equation (4.11) says a terminal maximum row must also have **strictly more global folded influence than the edge-isoperimetric minimum needed to support its rarity**.

## 5. Exact application to the lead candidate

On a `G_lambda/J`-critical core of the account01/B18 lead, singleton criticality implies `p_i<1/4` once the corrected ratio exceeds the lead's scalar low-ratio threshold. Therefore Theorem 4.1 applies automatically to the maximum folded-influence row whenever (4.2) holds.

Hence the lead's universal missing assertion can be split without introducing a new hypothetical profile theorem:

1. **near-minimal profile branch**: (4.2) holds at a maximum row. The actual physical certificate exists with `(gamma,K)=(14/15,12)` and this branch is discharged;
2. **spread branch**: every terminal high core satisfies the quantitative excess (4.10)--(4.11).

The remaining universal work is now only the spread branch: use the positive excess

\[
J-p_{\max}\left(1+\log_2(1/p_{\max})\right)
\]

to force one of the already spendable mechanisms (mixed-depth/companion flow, adaptive pivotality determination, total-correlation Booleanity, or another realizable block), without charging raw second-factorial depth or an unbounded coordinate label.

This is a real narrowing of the exact lead candidate. It does **not** assert that every hard core is near-minimal.

## 6. Mandatory obstruction checks

The theorem was checked against the campaign's required obstruction families before being promoted.

### Sparse / one-point defect

For the character-centered one-point-defect family on `n` variables,

\[
p_i=2^{1-n},
\quad J=np_i,
\quad L=n-1,
\]
so

\[
\Theta=(J-p_i)/p_i-L=0.
\]
The pivotality support is exactly a codimension-`n-1` subcube. The theorem therefore fires with equality, as it should.

### Addressing

The standard address coordinates have folded influence `1/2`, so the maximum row is outside the `p<=1/4` high-core regime. The theorem makes no false cheap-block assertion for addressing. Data-bit pivotality supports are subcubes, but they are not maximum-influence rows in the usual addressing function.

### Majority

For balanced majority the individual influences are comparable while the number of active coordinates grows. Thus `J/p_max` is of order the number of coordinates, whereas `log(1/p_max)` is only logarithmic. `Theta` is large, so the theorem correctly leaves majority in the spread branch.

### Tribes

The active influences are again numerous and comparable. `J/p_max` is much larger than `log(1/p_max)`, so no near-minimal-profile claim is triggered.

### Tensor powers

For disjoint tensor products, folded influence adds across factors while the largest individual folded influence does not scale with the number of factors. Consequently the profile excess grows under replication rather than falsely remaining in the near-minimal branch. No tensor-amplified global payment is inferred from (4.2).

### Biased/rare limits and half-band correction

The argument is purely physical-cube isoperimetry plus Boolean-square parity and does not use the refuted Brownian positive-current closure. Rare limits are handled by the explicit `L=log_2(1/p)` dependence; the threshold shrinks rather than silently becoming fixed-relative.

## 7. Decisive finite falsification calculation

A fresh exact truth-table diagnostic was run for all Boolean functions modulo global sign through dimension four. For every active folded coordinate it checked

\[
J-p_j\ge p_j\log_2(1/p_j).
\]

Counts:

| dimension | Boolean classes modulo sign | active-coordinate checks | violations | equality checks |
|---:|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 | 0 |
| 2 | 8 | 8 | 0 | 8 |
| 3 | 128 | 336 | 0 | 240 |
| 4 | 32,768 | 130,048 | 0 | 2,752 |

For the **maximum folded-influence** coordinate, among nonconstant classes:

| dimension | nonconstant classes | `Theta=0` classes | classes with `p_max<=1/4` and `Theta<=1/(16L)` |
|---:|---:|---:|---:|
| 2 | 4 | 4 | 0 |
| 3 | 120 | 88 | 64 |
| 4 | 32,752 | 864 | 768 |

The analytic proof, not this finite calculation, establishes the theorem.

## 8. Claim ledger

**ESSENTIAL_STEP_APPLIED.** A source-exact structural condition stated only in the variables actually present on the selected restriction has been proved and inserted into the campaign lead compiler.

**PROVED:** for every active folded coordinate,
\[
J-p_j\ge p_j\log_2(1/p_j).
\]

**PROVED:** its slack `Theta_j` upper-bounds the actual normalized edge-isoperimetric deficit of the folded pivotality support.

**PROVED:** for a maximum row with `p<=1/4`,
\[
Theta<=min\{epsilon_E,1/(16log_2(1/p))\}
\]
forces the exact `q/(16r)` support accuracy required by the existing physical near-subcube theorem, hence a genuine `(14/15,12,lambda)` lead certificate.

**Old missing implication:** somehow force the `q/(16r)` near-subcube hypothesis (or another certificate) on every terminal high core.

**New missing implication:** only the **profile-spread terminal branch** remains from this structural channel; on every uncertified maximum row it obeys the quantitative lower gap (4.10)--(4.11). One must convert that excess into a nonreused payable mechanism. No such universal conversion is proved here.

**NOT PROVED:** that every high core satisfies (4.2), that the spread branch is impossible, a universal Bellman bound, or full FEI.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
