TASK: B14 ACCOUNT: account02 RUN: 2026-09-21T21:09:15.663058Z — posterior-crossing information selector and a physical Shannon-certificate compiler

**Status:** PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated `math_brain` or cognitive-memory retrieval/context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. **Configured reasoning:** UNKNOWN / not exposed. **Known reasoning level:** UNKNOWN / not exposed. Provider reasoning-token usage and provider thinking time are not exposed.

**FULL-PROBLEM CHANGE:** NONE. No finite universal FEI constant is proved in this report.

**MECHANISM CHANGE:** YES. The preceding three B14 reports moved through pair-affine spendability, partition-hash spendability, and sequential affine projection refunds, but left a residual of the form `B_seq <= L D`, which is still a direct high-ratio payment problem. This run deliberately leaves that affine residual and returns to a *physical* adaptive interface, but with a new information-theoretic bridge: a posterior-majority crossing of one pivotality event cannot be produced cheaply. Quantitatively, the crossing itself forces a logarithmic amount of revealed physical influence. This turns a crossing certificate plus a one-survivor Shannon-scale erasure bound into a genuinely globally payable restriction step.

No novelty or publication-priority claim is made.

## 0. Fresh sources, peer result actually consumed, and last-three comparison

Fresh scientific `master` was resolved during the run. The applicable root instructions, `FLEET_RULES.md`, hourly protocol, and `proofnet24/P03-fei/README.md` were read before writing.

The current joint interface-A state was consumed from the shared brain handoff and from complete scientific reports. In particular:

1. **account01/B18**, `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md` (recorded blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d` in the joint handoff), supplies the corrected potential
   \[
   \mathcal P(f)=\sum_i\mathfrak j(p_i),\qquad \mathcal F=H-\mathcal P,
   \]
   the exact folded physical drift and the critical-core implication. I use its singleton consequence
   \[
   h_2(p_i)\ge \rho p_i
   \]
   on an `F/J`-critical core of ratio `rho`.
2. **account04/B14**, `proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260921T194301Z-crossing-amplified-erasure/REPORT.md`, supplies the exact physical identities
   \[
   D_A:=\Delta_A\mathcal J=I_A+C_A,
   \qquad
   \Delta_A\mathcal F=B_A-Q_A,
   \]
   with `C_A=sum_{j notin A} c_j(A)` and `Q_A>=0`. I keep the same posterior crossing functional and use it as an actual spendable term, not a heuristic.
3. **account01/B13**, `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260921T2020Z-crossing-depth-nearsubcube/REPORT.md`, proves that a rare pivotality event cannot cross posterior majority before logarithmic information depth and that a near-coordinate-subcube support produces an almost-maximal crossing on its defining physical block. I use this as the concrete structural interpretation of the new inequality below; I do not reannounce its theorem.
4. The newest joint interactive handoff `proofnet24/P03-fei/fleet-2026-09-21/account02/interactive/20260921T192650Z-joint-fei-subcube-peeling/REPORT.md` supplies the exact signed-subcube low-surplus peeling theorem. I use it only as a compatibility check for the new compiler, not as a claimed new class theorem.

The preceding three substantive B14 reports were:

- `20260921T190143Z-affine-pair-global-budget`: exact globally telescoping pair-parity drop, but only an aggregate pair-supply statistic;
- `20260921T193008Z-affine-partition-hash-budget`: random affine coalescence converted shell-poor pair supply into one spendable large drop, but left a one-shot hash erasure;
- `20260921T195815Z-sequential-erasure-refund`: sequential realization recovered an exact projection refund, but the remaining target was still `B_seq=O(D_P)` on the same high-drop partition.

The unpaid universal implication was therefore unchanged in substance across the affine sequence: obtain a realizable restriction whose Shannon loss is bounded by a nonreused `O(J)` budget. The present run changes the mechanism rather than optimizing that residual.

FLEET_RULES creative moves used here: **#1 CHANGE THE CATEGORY** (crossing -> likelihood-ratio information), **#18 SAY IT IN ANOTHER LANGUAGE** (pivotality crossing -> KL/mutual information), and **#19 MAKE IT AN ALGORITHM** (a physical crossing-certificate compiler with an exact tree budget).

## 1. Normalization and the posterior crossing object

Let
\[
f:\{0,1\}^n\to\{-1,+1\}
\]
be Boolean. Character-center the current state, so every relevant coordinate has
\[
0<p_i=\operatorname{Inf}_i(f)\le\frac12,
\qquad
\mathcal J(f)=\sum_i p_i.
\]

For a fixed survivor `j`, let
\[
\eta_j(x_{-j})=1_{\{f(x)\ne f(x\oplus e_j)\}}
\]
be the `j`-pivotality event. Then
\[
\Pr(\eta_j=1)=p_j.
\]

For a physical reveal block `A subseteq [n]\\{j}`, put
\[
U=\Pr(\eta_j=1\mid X_A),
\qquad
c_j(A)=\mathbb E(2U-1)_+.
\tag{1.1}
\]
This is exactly the account01/account04 posterior-majority crossing term.

The aim is to connect `c_j(A)` to the *actual original-coordinate influence spent by revealing A*,
\[
I_A=\sum_{i\in A}p_i.
\]

## 2. PROVED: posterior majority crossing has logarithmic information cost

### Lemma 2.1 — sharp KL threshold inequality

Let `0<p<1/2`, let
\[
L(p)=\log_2\frac{1-p}{p},
\]
and let `d_2(u||p)` denote binary relative entropy in bits. For every `0<=u<=1`,
\[
\boxed{
 d_2(u\Vert p)\ge L(p)(2u-1)_+.
}
\tag{2.1}
\]
Equality on the positive half-line occurs at `u=1-p`.

### Proof

For `u<=1/2` the right side is zero. For `u>=1/2`, define
\[
g(u)=d_2(u\Vert p)-L(p)(2u-1).
\]
Binary relative entropy is convex in `u`, hence so is `g`. Its derivative is
\[
g'(u)=\log_2\frac{u(1-p)}{p(1-u)}-2L(p).
\]
At `u=1-p` this vanishes. Also
\[
d_2(1-p\Vert p)=(1-2p)L(p),
\]
so `g(1-p)=0`. Thus the convex function `g` has global minimum zero at `u=1-p`, proving (2.1). QED.

### Corollary 2.2 — crossing forces mutual information

For any Boolean event `Y` of density `p<=1/2` and any physical block `A`, if
\[
U=\Pr(Y=1\mid X_A),
\qquad c(A)=\mathbb E(2U-1)_+,
\]
then
\[
\boxed{
I(Y;X_A)\ge L(p)c(A).
}
\tag{2.2}
\]

### Proof

The posterior representation of mutual information gives
\[
I(Y;X_A)=\mathbb E\,d_2(U\Vert p).
\]
Apply Lemma 2.1 pointwise and average. QED.

This is stronger than a variance/Pinsker estimate: for rare `p`, one unit of posterior crossing costs order `log(1/p)` bits of information.

## 3. PROVED: information about a pivotality event is paid by physical influences

### Lemma 3.1 — mutual information is at most event boundary in the revealed block

For every Boolean event `Y` and every coordinate block `A`,
\[
\boxed{
I(Y;X_A)\le\sum_{i\in A}\operatorname{Inf}_i(Y).
}
\tag{3.1}
\]

### Proof

Reveal the coordinates of `A` in any order. By the chain rule,
\[
I(Y;X_A)=\sum_s I(Y;X_{i_s}\mid X_{i_1},\ldots,X_{i_{s-1}}).
\]
Fix a history. Conditional on that history, the two laws of `Y` for `X_{i_s}=0,1` are Bernoulli laws `P_0,P_1`, and the displayed conditional mutual information is their equal-weight Jensen--Shannon divergence.

For arbitrary probability laws,
\[
JS_{1/2}(P_0,P_1)\le \operatorname{TV}(P_0,P_1)
\]
in bits. One elementary proof is to split `P_0,P_1` into their maximal common part of mass `1-delta` plus residual parts of mass `delta=TV`; the observation can reveal at most one bit on the residual event and no label information on the common event.

For the Boolean event, couple `P_0,P_1` by using the same remaining coordinates. Their total variation is at most the conditional probability that flipping `i_s` changes `Y`, i.e. the conditional `i_s`-influence. Averaging the history returns the original `Inf_{i_s}(Y)`. Summing proves (3.1). QED.

### Lemma 3.2 — a pivotality boundary costs at most twice the parent influence

For distinct physical coordinates `i,j`,
\[
\boxed{
\operatorname{Inf}_i(\eta_j)\le2p_i.
}
\tag{3.2}
\]

### Proof

Freeze all coordinates except `i,j`, producing one Boolean square. If the `j`-pivotality status changes when `i` is flipped, then exactly one of the two `j`-edges of the square is bichromatic. In that situation at least one of the two `i`-edges must be bichromatic; otherwise both `i`-edges are monochromatic and the two `j`-edges have the same pivotality status. Therefore every square counted by `Inf_i(eta_j)` contributes at least `1/2` to the conditional `i`-influence of `f`. Averaging the frozen coordinates yields
\[
p_i\ge\frac12\operatorname{Inf}_i(\eta_j).
\]
QED.

This local square statement is compatible with account04/B18's exact mixed-derivative curvature identity `support-boundary + 4 opposite-sign-overlap = mixed curvature`; here only the support-boundary part is needed.

### Theorem 3.3 — crossing-to-physical-influence inequality

For every centered Boolean `f`, every survivor `j` with `0<p_j<1/2`, and every physical block `A subseteq[n]\\{j}`,
\[
\boxed{
I_A
\ge
\frac12\log_2\frac{1-p_j}{p_j}\;c_j(A).
}
\tag{3.3}
\]

### Proof

Combine Corollary 2.2, Lemma 3.1 applied to `Y=eta_j`, and Lemma 3.2:
\[
L(p_j)c_j(A)
\le I(\eta_j;X_A)
\le\sum_{i\in A}\operatorname{Inf}_i(\eta_j)
\le2\sum_{i\in A}p_i=2I_A.
\]
QED.

This is the main new implication of the run. It is completely physical: no affine change of basis and no transformed-coordinate cost appears.

## 4. PROVED: a substantial crossing pays one survivor's full Bernoulli Shannon entropy

The high-ratio critical regime supplied by account01 automatically lies below the influence threshold `1/4`. This is exactly where Theorem 3.3 turns into a clean Shannon payment.

### Lemma 4.1 — scalar comparison below `1/4`

For `0<p<=1/4`, with `L(p)=log_2((1-p)/p)`,
\[
\boxed{
h_2(p)\le\frac94\,pL(p).}
\tag{4.1}
\]

### Proof

Use the exact identity
\[
\frac{h_2(p)}p
=L(p)+\frac{-\log_2(1-p)}p.
\]
Since `-ln(1-p)<=p/(1-p)` and `p<=1/4`,
\[
\frac{-\log_2(1-p)}p\le\frac4{3\ln2}.
\]
Also `L(p)>=log_2 3`. The numerical-free inequality
\[
\frac4{3\ln2}\le\frac54\log_2 3
\]
is equivalent to `16/3<=5 ln 3`, which holds. Therefore `h_2(p)/p <= (9/4)L(p)`. QED.

### Theorem 4.2 — crossing-to-Shannon payment

Assume `0<p_j<=1/4`. If one physical block `A` satisfies
\[
c_j(A)\ge\gamma p_j
\qquad(0<\gamma<=1),
\tag{4.2}
\]
then
\[
\boxed{
h_2(p_j)\le\frac9{2\gamma}I_A.}
\tag{4.3}
\]
Consequently, using the exact account04 drift `D_A=I_A+C_A`,
\[
\boxed{
h_2(p_j)\le\frac9{2\gamma}D_A.}
\tag{4.4}
\]

### Proof

Theorem 3.3 and (4.2) give
\[
p_jL(p_j)\le\frac2\gamma I_A.
\]
Apply (4.1). QED.

This is the missing conversion that the previous crossing ledgers did not have: an order-one fraction of a rare pivotality crossing automatically carries enough *actual physical influence spend* to pay that survivor's logarithmic Bernoulli entropy.

## 5. PROVED: critical cores are automatically in the applicable rarity regime

Let
\[
\rho=\frac{\mathcal F}{\mathcal J}
\]
for a centered `F/J`-critical physical restriction descendant from account01/account04. Their singleton criticality gives
\[
h_2(p_i)\ge\rho p_i
\tag{5.1}
\]
for every relevant coordinate.

The function `h_2(p)/p` is decreasing on `(0,1/2]`. Therefore, with
\[
\rho_*:=4h_2(1/4)=3.245112497836531\ldots,
\tag{5.2}
\]
we have
\[
\boxed{
\rho>\rho_*\quad\Longrightarrow\quad p_i<1/4\text{ for every relevant }i.
}
\tag{5.3}
\]

This is the account01/B13 singleton-zero-crossing regime, now used positively: every nontrivial *multi-bit* posterior crossing in a high-ratio core is eligible for Theorem 4.2.

## 6. NEW universal compiler: a realizable selective certificate sufficient for full FEI

For a physical block `A`, retain account04's exact corrected decrement
\[
E_A:=\Delta_A\mathcal F=B_A-Q_A,
\qquad Q_A\ge0,
\tag{6.1}
\]
and exact folded drop
\[
D_A=I_A+C_A.
\tag{6.2}
\]

### Definition 6.1 — `(gamma,K)` Shannon crossing certificate

At a centered node, a pair `(A,j)` with `j notin A` is a `(gamma,K)` certificate if
\[
\boxed{
c_j(A)\ge\gamma p_j}
\tag{6.3}
\]
and
\[
\boxed{E_A=B_A-Q_A\le K h_2(p_j).}
\tag{6.4}
\]

Both conditions refer to the **same physical block**. No prescribed-coordinate statement is made; existence of one useful pair is enough.

### Theorem 6.2 — certificate compiler

Fix universal `gamma>0` and `K<infinity`. Suppose every centered `F/J`-critical Boolean core with ratio `rho>rho_*` admits a `(gamma,K)` Shannon crossing certificate. Then full FEI follows, quantitatively:
\[
\boxed{
\mathcal F(f)\le
\max\left\{\rho_*,\frac{9K}{2\gamma}\right\}\mathcal J(f)
}
\tag{6.5}
\]
and hence
\[
\boxed{
H(f)\le
\left[
\max\left\{\rho_*,\frac{9K}{2\gamma}\right\}
+\frac2{\ln2}
\right]I(f)
}
\tag{6.6}
\]
for every Boolean `f`.

### Proof

Take a centered physical restriction descendant maximizing `F/J`, with ratio `rho`. If `rho<=rho_*`, there is nothing to prove. Otherwise every active `p_i<1/4` by Section 5.

For every physical block, criticality gives
\[
E_A=\Delta_A\mathcal F\ge\rho D_A.
\tag{6.7}
\]
Choose the assumed certificate `(A,j)`. By Theorem 4.2,
\[
K h_2(p_j)
\le\frac{9K}{2\gamma}I_A
\le\frac{9K}{2\gamma}D_A.
\]
Together with (6.4) and (6.7),
\[
\rho D_A\le E_A\le\frac{9K}{2\gamma}D_A.
\]
The certificate has positive crossing, hence `D_A>0`, so
\[
\rho\le\frac{9K}{2\gamma}.
\]
This proves (6.5). Finally `0<=P<= (2/ln2)J` and `J<=I`, giving (6.6). QED.

### Quantitative target

The compiler is concrete. For example, a universal certificate theorem with `gamma=1` and `K=1` would give
\[
H(f)\le\left(\frac92+\frac2{\ln2}\right)I(f)
<7.386 I(f).
\]
This is **not** claimed. It identifies the exact unpaid interface: find one block whose corrected erasure is at most a constant times the binary entropy of one survivor whose pivotality is substantially crossed.

The point is that the crossing condition now automatically pays the logarithmic rarity of that survivor in the *same physical budget*. One no longer needs to postulate a direct `B_A=O(I_A)` bound for an arbitrary block.

## 7. Relation to the newest near-subcube handoffs

Account01/B13 proves that if a pivotality support is within relative error `epsilon` of a coordinate subcube with defining block `F_j`, then
\[
c_j(F_j)\ge(1-\epsilon)p_j.
\tag{7.1}
\]
Therefore Theorem 4.2 immediately gives, throughout the high-ratio critical regime,
\[
\boxed{
h_2(p_j)\le\frac9{2(1-\epsilon)}I_{F_j}.}
\tag{7.2}
\]

This is a new *interface conversion*, not a new near-subcube FEI theorem. The joint interactive exact signed-subcube/low-surplus peeling result already gives a stronger specialized exclusion. What (7.2) adds is a support-shape-independent explanation of why an almost-maximal posterior crossing carries the correct logarithmic physical price: the price comes from mutual information about pivotality and the Boolean square constraint, not from counting the defining coordinates one by one.

For arbitrary blocks the same theorem applies with the actual crossing fraction `gamma=c_j(A)/p_j`; no subcube hypothesis is needed.

## 8. Preserved failures and what this does NOT prove

1. **No every-coordinate payment.** The certificate is existential in `(A,j)`. All known counterexamples to a bound at every prescribed coordinate remain valid.
2. **Crossing alone is not a full selector.** Theorem 3.3 is a lower bound on the physical influence needed to create crossing. It does not upper-bound the block erasure `B_A`. A block may reveal much unrelated spectral information.
3. **No reuse across multiple targets.** Applying (4.3) separately to many survivors with the same block would reuse `I_A`. The compiler deliberately uses one target survivor for one selected block. Aggregating many crossings requires an additional nonreuse argument, such as the mixed-derivative depth conservation being developed in the neighboring tracks.
4. **The previous affine residual is retired for this run.** On a high-ratio critical core, `Delta H>=rho D`; since the sequential recombination refund is globally only `O(J)`, proving `B_seq<=L D` with universal `L` remains essentially the same high-ratio obstruction. This run does not rename that gap.
5. **Tensor replication is respected.** The certificate condition is local to one physical descendant and one selected block. No tensor-stable shell statistic is asserted.
6. **Full FEI remains open.** The universal missing arrow is now the existence, in every high-ratio primitive core, of a physical `(gamma,K)` certificate for fixed positive `gamma` and finite `K`, or a complementary branch that is already globally paid.

## 9. Diagnostic finite checks

`check_crossing_information.py` was executed as a floating regression diagnostic. The analytic proof above is the theorem.

Event-level exhaustive scope:

- every Boolean event through 4 variables and every coordinate block;
- `628,572` event/block cases;
- `203,232` cases with positive crossing;
- maximum observed violation of `L(p)c<=I(Y;X_A)`: `0.0`;
- maximum observed violation of `I(Y;X_A)<=sum_{i in A} Inf_i(Y)`: `0.0`.

Pivotality specialization:

- every Boolean function through 3 variables, every pivot and every block of nonpivot variables;
- `1,568` local-square checks of `Inf_i(eta_j)<=2p_i`;
- `768` combined crossing-to-physical-influence block checks;
- maximum observed violation: `0.0`.

These are finite floating diagnostics only and do not establish the all-dimensional theorem.

## 10. Literature/status check

A fresh public search found no universal FEI solution. González--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (arXiv:2606.00246, 29 May 2026), develops a stopping/restriction-decrement framework: a suitable restriction inequality at branch nodes compiles to FEI. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions* (arXiv:2609.21563, 18 September 2026, updated 21 September), proves FEI for plateaued and partially bent classes, with sharp class constants 4 and 2 respectively, not universally.

The KL threshold inequality and `JS<=TV` are standard information-theoretic facts proved here directly. A bounded search was not used to infer novelty, and no publication-priority claim is made for Theorem 3.3 or the certificate compiler.

## 11. Claim ledger

- `B14-CROSS-KL-01`: `I(Y;X_A)>=log_2((1-p)/p)c(A)` for `p<1/2`. **PROVED**.
- `B14-PIVOTAL-BOUNDARY-02`: `Inf_i(eta_j)<=2 Inf_i(f)`. **PROVED**.
- `B14-CROSS-PHYSICAL-03`: `I_A >= (1/2) log_2((1-p_j)/p_j)c_j(A)`. **PROVED**.
- `B14-CROSS-SHANNON-04`: for `p_j<=1/4` and `c_j(A)>=gamma p_j`, `h_2(p_j)<=9 I_A/(2gamma)`. **PROVED**.
- `B14-CERTIFICATE-COMPILER-05`: universal `(gamma,K)` certificates on all high-ratio corrected critical cores imply full FEI with (6.6). **PROVED, CONDITIONAL ON THE CERTIFICATE EXISTENCE HYPOTHESIS**.
- Universal existence of fixed `(gamma,K)` certificates: **OPEN**.
- Full uniform-cube FEI: **OPEN / NOT PROVED**.

## 12. Before/after and exact next obligation

**Before:** after the affine sequence, the remaining selector condition was a direct block-history erasure estimate `B_seq<=L D` on a high-drop affine partition. It had no separate mechanism forcing the logarithmic Shannon cost of a rare survivor to be present in the physical denominator.

**After:** for any physical block that crosses a survivor `j`, the exact logarithmic rarity is automatically present in the revealed physical influence:
\[
I_A\ge\frac12\log_2\frac{1-p_j}{p_j}\,c_j(A).
\]
At high corrected ratio, a constant-fraction crossing therefore pays the full one-bit marginal entropy `h_2(p_j)` at constant price. This yields the explicit universal compiler (6.6).

**Remaining universal obligation:** construct, on every high-ratio primitive core, one physical block/survivor pair with
\[
c_j(A)\ge\gamma p_j,
\qquad
B_A-Q_A\le K h_2(p_j)
\]
for universal `gamma>0,K<infinity`, or force the core into a complementary already-paid structural branch. The next B14 attack should target the second inequality using *minimal posterior-crossing certificates*: prove that a block which first produces a fixed crossing fraction has corrected erasure controlled by the target event's Shannon information plus a nonreused mixed-derivative credit. If that fails, preserve the counterexample and switch to a decision-tree/Holevo formulation rather than returning to affine threshold scans.
