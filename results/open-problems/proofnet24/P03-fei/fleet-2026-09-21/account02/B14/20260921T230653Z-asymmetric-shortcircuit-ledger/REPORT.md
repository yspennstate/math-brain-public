# B14 — asymmetric support-error payment and a realizable random-order short-circuit ledger

**Status:** PARTIAL. Full Friedgut--Kalai Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval/context was used.  
**Role:** FEI erasure/selector/restriction, shared interface A.  
**Method change:** YES. This run leaves the stationary closed-trigger selector and attacks the fixed-relative near-subcube obstruction with an asymmetric full-block theorem plus a randomized physical short-circuit tree.  
**Novelty/priority:** UNVERIFIED; no novelty claim.

## 0. Source snapshot and completed peer results actually consumed

Fresh scientific master was read first at `5c658032d1c9b10145087cfb92bc1295331d22b9` and refreshed before delivery to `11cd046311584902959d4ee453b6fec3c2a235e7`. The applicable repository rules and `proofnet24/P03-fei/README.md` were read before writing.

Named completed cross-account inputs used in the derivation:

1. `account01/B14/20260921T224055Z-adaptive-pivotality-selector/REPORT.md`, blob `585cbdfc282e636c95b70bd479d4c720b19f1948`. It proves the folded square estimate
   \[
   \operatorname{Inf}_k(\eta_x)\le 2\min\{\operatorname{Inf}_k(f),1-\operatorname{Inf}_k(f)\}=2q_k
   \tag{0.1}
   \]
   for `k != x`, and the adaptive pivotality-determination compiler. I use (0.1) below. I do **not** reannounce it as new.

2. `account04/B14/20260921T211337Z-posterior-variance-short-circuit/REPORT.md`, blob `dd147272df8df45d1284474bf5a04eeaaf1b908e`. It supplies the exact folded restriction drift accounting and the physical first-mismatch short-circuit tree.

3. `account03/B14/20260921T214637Z-adaptive-fixed-relative/REPORT.md`, blob `6af53e122aef35d646dab1e695d138bf3125448d`. It proves that the explicit fixed-relative obstruction is **not** killed by the natural short-circuit tree: its exact stopped drift is on the correct `r q` scale and numerically its entropy/drift ratio tends toward 4. That makes the adaptive mechanism worth analyzing universally rather than treating the full-block counterexample as decisive.

4. `account02/interactive/20260921T192650Z-joint-fei-subcube-peeling/ADDENDUM.md`, blob `baa3155a268d936d6b191667ee71a6df84969292`. Theorem C.1 proves the coefficient-12 full physical block step under total support error `E <= q/(16 r)`. I reuse its punctured-cube/log-Sobolev estimates, but sharpen its first boundary step by separating false negatives from false positives.

5. The current account01 curvature-refunded critical-core work is compatible but does not itself upper-bound the Shannon decrement: its all-block inequalities are lower/obstruction inequalities on a critical core. The new paid branch below can therefore be inserted into that critical-core architecture, while the remaining fixed-relative false-positive branch still needs an upper adaptive entropy payment.

## 1. Last three B14 reports: exact before/after

The preceding three substantive account02/B14 mechanisms left progressively narrower versions of the same universal gap:

- `20260921T195815Z-sequential-erasure-refund`: exact projection refund, but the same high-drop partition still needed `B_seq = O(D)`.
- `20260921T210915Z-crossing-information-selector`: physical posterior crossing pays one rare survivor Shannon scale, but still needed a block with corrected erasure `O(h_2(p_j))`.
- `20260921T220126Z-stationary-trigger-selector`: closed `q/(16r)`-certified systems are paid by a stationary physical selector; a stalled core is localized to the **fixed-relative** `q/16` error regime.

**FULL-PROBLEM CHANGE:** NONE. Full FEI is still open.

**MECHANISM CHANGE:** YES. The present run does not scan another scalar threshold. It executes a new physical mechanism on the stalled branch: split support error by side, prove a stronger full-block theorem when only the outside pollution is `O(q/r)`, and in the truly fixed-relative outside-error regime choose a random-order first-mismatch tree whose actual folded-influence spend remains `Theta(rq)` and whose residual pivotality uncertainty is quantitatively small.

## 2. Setup and the one-sided error split

Let `f` be Boolean. Fix a pivot `x` and physical controls
\[
Z=\{z_1,\dots,z_r\},\qquad Q=\{Z=a\},\qquad q=2^{-r}.
\]
Let
\[
\eta_x=1_{\{f(0,Z,w)\ne f(1,Z,w)\}}
\]
be the `x`-pivotality event. Split the support error into
\[
E^-:=\Pr(Q\cap\{\eta_x=0\}),\qquad
E^+:=\Pr(Q^c\cap\{\eta_x=1\}).
\tag{2.1}
\]
Then
\[
p:=\operatorname{Inf}_x(f)=q+E^+-E^-.
\tag{2.2}
\]
Write
\[
I_Z:=\sum_{k\in Z}\operatorname{Inf}_k(f).
\]
As in Theorem C.1, the average-control hypothesis is
\[
I_Z\le r p.
\tag{2.3}
\]
No sign agreement for the derivative is assumed.

The key point is that `E^-` and `E^+` play different roles. An inside false negative lives at the exceptional vertex `a`; an outside false positive can create arbitrary punctured-cube variation away from `a`.

## 3. PROVED: the punctured internal boundary only charges outside false positives

Let
\[
e_a=\Pr_w(\eta_x(a,w)=0),
\qquad
E^-=q e_a.
\]
For `b != a`, let
\[
e_b=\Pr_w(\eta_x(b,w)=1).
\]
Let
\[
E^+_1:=q\sum_{b:\,d_H(a,b)=1}e_b\le E^+
\tag{3.1}
\]
be the first-shell part of the outside error.

Exactly as in C.1, an edge from `a` to `a+e_k` on which the pivotality status differs forces at least one of the two corresponding `k`-edges of `f` to be bichromatic. Therefore the total control influence incident to `a` obeys
\[
I_{\rm inc}\ge rq-rE^- -E^+_1.
\tag{3.2}
\]
Let `B_int` be the remaining internal punctured control boundary, so
\[
I_Z=I_{\rm inc}+B_{\rm int}.
\]
Using (2.2)--(2.3),
\[
\begin{aligned}
B_{\rm int}
&\le r(q+E^+-E^-)-\bigl(rq-rE^- -E^+_1\bigr)\\
&=rE^+ +E^+_1\\
&\le (r+1)E^+.
\end{aligned}
\tag{3.3}
\]
Thus the inside false-negative error cancels **exactly** from the expensive punctured-boundary term.

This is the first new implication of the run. The old coarse line `B_int <= 2r(E^-+E^+)` hid this cancellation and made both sides appear to need `1/r` accuracy.

## 4. PROVED: asymmetric coefficient-12 full-block theorem

### Theorem 4.1 — fixed-relative false negatives are allowed

Under (2.3), suppose
\[
\boxed{
E^-\le {q\over16},
\qquad
E^+\le {q\over 8(r+1)}.
}
\tag{4.1}
\]
Then the genuine physical block restriction of **all** controls `Z` satisfies
\[
\boxed{
\Delta_Z H
:=H(f)-\mathbb E_z H(f_{Z=z})
\le 12 I_Z.
}
\tag{4.2}
\]

This strictly strengthens C.1 in the false-negative direction: the old theorem required the **total** error to be at most `q/(16r)`, whereas (4.1) permits inside false-negative mass `q/16`, independent of `r`. It also permits outside false positives of order `q/(8r)` asymptotically. The statement is still a conditional row theorem, not full FEI.

### Proof

By (3.3),
\[
B_{\rm int}\le (r+1)E^+\le q/8.
\tag{4.3}
\]
The rest of C.1's source-exact punctured-cube argument now applies without change. If `S_Z` is the spectral intersection with the control block and `theta=Pr(S_Z != empty)`, its variance step gives
\[
\theta\le2B_{\rm int}+4q\le {17q\over4}.
\tag{4.4}
\]
The full-cube log-Sobolev restriction-mixture estimate gives
\[
\Delta_Z H\le H(S_Z)+{2\over\ln2}I_Z.
\tag{4.5}
\]
For `r>=3`, the same entropy envelope as C.1 yields
\[
H(S_Z)
\le \Phi_{2^r}(17q/4)
< {17\over2}qr-{17\over8}q.
\tag{4.6}
\]

We also retain a better lower bound than the coarse total-error estimate. From (3.2),
\[
I_Z\ge rq-rE^- -E^+_1
\ge q\left({15r\over16}-{1\over8(r+1)}\right).
\tag{4.7}
\]
Set
\[
A:=12-{2\over\ln2}.
\]
The positive-series identity
\[
\ln2=2\sum_{m\ge0}{1\over(2m+1)3^{2m+1}}
>2\left({1\over3}+{1\over81}\right)
={56\over81}
\]
gives
\[
A>{255\over28}.
\tag{4.8}
\]
Hence, for `r>=3`,
\[
\begin{aligned}
{A I_Z\over q}
&>{255\over28}
\left({15r\over16}-{1\over8(r+1)}\right)\\
&={3825\over448}r-{255\over224(r+1)}\\
&>{17\over2}r-{17\over8},
\end{aligned}
\tag{4.9}
\]
because the difference is
\[
{17r\over448}+{17\over8}-{255\over224(r+1)}>0.
\]
Combining (4.5)--(4.9) proves (4.2) for `r>=3`.

For `r=1,2`, use the trivial `H(S_Z)<=r` in (4.5), together with (4.7). At `r=1`, (4.7) gives `I_Z>=7/16`; at `r=2` it gives `I_Z>=11/24`; in both cases `r < A I_Z`. Thus (4.2) also holds for `r=1,2`. QED.

### Corollary 4.2 — a sharper high-ratio critical-core obstruction

Let `f` be centered and `H/J`-critical under proper physical restrictions, with
\[
R={H(f)\over J(f)}>12.
\]
For any pivot/control row satisfying `I_Z<=r I_x`, if
\[
E^-\le q/16,
\]
then necessarily
\[
\boxed{
E^+>{q\over8(r+1)}.
}
\tag{4.10}
\]
Indeed, otherwise Theorem 4.1 gives `Delta_Z H<=12 I_Z<=12 D_Z`, while criticality gives `Delta_Z H>=R D_Z` and `D_Z>0`.

So a putative ratio-`>12` hard core cannot hide merely by deleting a fixed `1/16` fraction of the ideal subcube support. The surviving obstruction must put genuine pivotality mass **outside** the proxy subcube at scale at least `q/r`.

This is an actual universal-facing reduction toward a finite FEI constant, not a structured-class conclusion. It does not show that every core has a near-subcube row.

## 5. Fixed-relative outside pollution: switch to a physical random-order short circuit

Theorem 4.1 still leaves the regime
\[
E^-+E^+\le q/16
\quad\text{but}\quad
E^+\gg q/r,
\tag{5.1}
\]
which includes the known fixed-relative obstruction. The full block is not the right operation there.

For a permutation `pi` of the `r` defining literals, let `T_pi` be the physical decision tree which queries them in that order and stops at the first mismatch with `a`; it reaches depth `r` only on the all-match branch. For `t=0,...,r-1`, let `P_t^pi` be the event that the first `t` queried literals match `a`.

Define the outside-error survival ledger
\[
L_\pi^+:=\sum_{t=0}^{r-1}\Pr\bigl((Q^c\cap\{\eta_x=1\})\cap P_t^\pi\bigr).
\tag{5.2}
\]
This is a root-measure quantity: an outside false-positive point is charged only until its first mismatching proxy literal is discovered.

### Lemma 5.1 — random-order survival identity

For an outside-error point `y`, let `m(y)>=1` be its number of mismatching defining literals. Under a uniformly random permutation,
\[
\mathbb E_\pi\#\{t:y\in P_t^\pi\}
={r+1\over m(y)+1}
\le {r+1\over2}.
\tag{5.3}
\]
Consequently there exists a deterministic permutation `pi` with
\[
\boxed{
L_\pi^+\le {r+1\over2}E^+.
}
\tag{5.4}
\]

#### Proof

For fixed mismatch set of size `m`,
\[
\Pr_\pi(y\in P_t^\pi)
={\binom{r-m}{t}\over\binom rt}.
\]
Summing over `t=0,...,r-1` gives the expected position of the first marked item in a random permutation,
\[
\sum_t{\binom{r-m}{t}\over\binom rt}={r+1\over m+1}.
\]
Integrate over the outside-error set and average over `pi`; some permutation is no worse than the mean. QED.

## 6. PROVED: the stopped tree really spends `Theta(rq)` folded influence at fixed-relative error

The subtle point is that the stopped tree has expected query **count** below two, but the conditional queried influences increase along the rare all-match spine. The next theorem shows that the *actual folded-J spend* remains of order `rq` for an arbitrary Boolean row, not only for account03's explicit example.

### Theorem 6.1 — fixed-relative random-order drift lower bound

Assume only
\[
E^-+E^+\le q/16.
\tag{6.1}
\]
There is a deterministic permutation `pi` of the defining literals such that the short-circuit tree `T_pi` has total folded influence drift
\[
D_{T_\pi}
:=J(f)-\mathbb E_{\ell}J(f_\ell)
\]
satisfying
\[
\boxed{
D_{T_\pi}\ge {15\over16}r q.
}
\tag{6.2}
\]
More precisely, if `Q_pi` is the reach-weighted sum of the folded influences of the actually queried control coordinates,
\[
Q_\pi:=\sum_{t=0}^{r-1}\Pr(P_t^\pi)\,
q_{\pi(t+1)}(f\mid P_t^\pi),
\]
then
\[
\boxed{
Q_\pi\ge rq-rE^- -L_\pi^+
\ge rq-rE^- -{r+1\over2}E^+.
}
\tag{6.3}
\]
Since every one-step folded restriction drift equals the queried folded influence plus nonnegative crossing refunds, `D_{T_pi}>=Q_pi`, giving (6.2).

### Proof

Fix a reached all-match prefix `P_t^pi`. Put `s=r-t`, so in this node the residual ideal event is a codimension-`s` subcube of density
\[
q_s=2^{-s},
\qquad
\Pr(P_t^\pi)q_s=q.
\]
Let `eps_t` be the conditional symmetric-difference probability between the restricted pivotality event and that residual ideal subcube.

For the next defining coordinate `k=pi(t+1)`, the ideal subcube indicator has `k`-influence `2q_s`. Changing a Boolean event on mass `eps_t` can change one-coordinate boundary by at most `2eps_t`; hence
\[
\operatorname{Inf}_k(\eta_x\mid P_t^\pi)
\ge2(q_s-\varepsilon_t).
\tag{6.4}
\]
Now use the completed account01 folded-square estimate (0.1) at this restricted node:
\[
q_k(f\mid P_t^\pi)
\ge {1\over2}\operatorname{Inf}_k(\eta_x\mid P_t^\pi)
\ge q_s-\varepsilon_t.
\tag{6.5}
\]
Multiplying by the node reach probability gives
\[
\Pr(P_t^\pi)q_k(f\mid P_t^\pi)
\ge q-\Pr\bigl((\eta_x\triangle1_Q)\cap P_t^\pi\bigr).
\tag{6.6}
\]
Sum over `t`. Every inside false negative belongs to all `r` prefixes, contributing `rE^-`; outside false positives contribute exactly `L_pi^+`. This gives the first inequality in (6.3). Choose `pi` from Lemma 5.1. Since `(r+1)/2<=r`, (6.1) gives
\[
Q_\pi\ge rq-r(E^-+E^+)\ge15rq/16.
\]
Finally sum the exact account04/account01 one-step folded-drift identities along the physical tree; all crossing terms are nonnegative, so `D_T>=Q_pi`. QED.

This is the second new implication of the run. The fixed-relative branch no longer has a denominator/summability collapse: the actual physical stopped tree spends a dimension-free fraction of the natural `rq` budget, and that spend telescopes exactly in `J`.

## 7. PROVED: the same tree removes most pivotality uncertainty

The transcript of `T_pi` determines whether `Q` occurred. Therefore, with the error indicator
\[
R=1_{\{\eta_x\ne1_Q\}},
\]
we have
\[
\boxed{
H(\eta_x\mid T_\pi)
=H(R\mid T_\pi)
\le H(R)=h_2(E^-+E^+).
}
\tag{7.1}
\]
The same conditional entropy holds for the folded event `Y_x`, since complementing a Bernoulli variable does not change entropy.

For `r>=2`, `q<=1/4` and (6.1) imply
\[
15q/16\le p\le17q/16<1/2,
\]
so `Y_x=eta_x`. Moreover
\[
\boxed{
h_2(E^-+E^+)\le {1\over4}h_2(p).}
\tag{7.2}
\]
Thus
\[
\boxed{
I(Y_x;T_\pi)\ge {3\over4}h_2(p).
}
\tag{7.3}
\]

A short proof of (7.2): put `u=q/16<=1/64` and `L=log_2(1/u)>=6`. The standard bounds
\[
h_2(u)\le u(L+\log_2 e),
\qquad
h_2(15u)\ge15u(L-\log_2 15)
\]
and the crude strict inequalities `log_2 e<3/2`, `log_2 15<4` imply
\[
L+\log_2 e < {15\over4}(L-\log_2 15).
\]
Hence `h_2(u)<h_2(15u)/4`. Use monotonicity of `h_2` on `[0,1/2]` and `E<=u`, `p>=15u` after restoring the factor `q`.

So the natural short-circuit is a **3/4-information preconditioner** for the adaptive pivotality-determination compiler of account01/B14, while spending at least `15rq/16` folded influence. It is not yet a determining tree: the residual error event must still be resolved.

## 8. What this does and does not pay globally

The two theorems separate the stalled interface into two genuinely different pieces.

### Paid branch

If a row has
\[
E^-\le q/16,
\qquad
E^+\le q/[8(r+1)],
\qquad
I_Z\le rI_x,
\]
then the entire physical block is paid with coefficient 12. In an `H/J`-critical core of ratio above 12 such a row is impossible. This is a complete all-dimensional restriction implication.

### Fixed-relative branch

If only `E^-+E^+<=q/16` is known, choose the permutation from Theorem 6.1 and run the first-mismatch tree. Then
\[
D_T\ge15rq/16,
\qquad
H(Y_x\mid T)\le h_2(E),
\tag{8.1}
\]
and for `r>=2` the tree has already extracted at least `3/4` of the target pivotality entropy.

The remaining universal arrow is now an **upper corrected-entropy estimate for this same physical tree**, or a recursive determination of the residual error event with a geometrically summable cost. A sufficient local target is
\[
\boxed{
\Delta_T\mathcal F\le K rq
}
\tag{8.2}
\]
for a universal `K` on the selected primitive-core row; Theorem 6.1 would then give
\[
\Delta_T\mathcal F\le {16K\over15}D_T.
\]
More source-exactly, one may append a residual determining subtree and prove that its corrected entropy cost is `O(h_2(E))` without reusing the already-spent query/crossing credits.

This residual is narrower than the previous `B_seq=O(D)` or fixed-block `Delta_ZH=O(D_Z)` gaps. It has three precise features:

1. inside false negatives no longer require `1/r` support accuracy;
2. the fixed-relative outside-error tree has a proved spendable denominator `>=15rq/16`;
3. only the entropy created while resolving the residual false-positive/error event remains unpaid.

The account01 curvature-refunded inequalities are compatible with this localization but do not provide the missing **upper** entropy estimate. The account04 posterior-crossing ledger supplies additional nonnegative drift and therefore only helps the denominator. No universal supremum comparison is turned into a pointwise inequality.

## 9. Counterexamples and killed stronger statements preserved

Nothing here asserts a cheap **prescribed** coordinate or block. The old addressing counterexamples remain valid.

Nothing here restores the false fixed-relative **full-block** theorem: account03/account02's family still has `Delta_ZH/D_Z -> infinity` for the full defining block. Theorem 6.1 instead changes the physical operation to a stopped tree.

Nothing here claims a tensor-stable shell statistic, a sign-free parity-profile sufficiency theorem, or a global phase/rank/l1 optimizer. Those routes remain killed in the current handoffs.

Finite checks below are sanity checks only and do not prove FEI.

## 10. Exact sanity checks

A small exact checker accompanies this report. It verifies:

- the combinatorial identity in (5.3) for every `1<=m<=r<=64` using rational arithmetic;
- the folded pivotality boundary estimate (0.1) exhaustively for all `65,536` Boolean functions on four variables and every ordered distinct coordinate pair;
- the displayed coefficient-12 scalar inequalities for a broad integer range.

These checks are regression evidence. The proofs above are the mathematical deliverable.

## 11. Current primary-literature status

A fresh bounded primary-source search was performed before delivery. The May 29, 2026 González--MacManus--Pereyra paper develops restriction-decrement/stopping-tree sufficient conditions for FEI, not a universal proof. Potapov's September 18, 2026 paper proves FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2), not for all Boolean functions. No priority claim is made for Theorems 4.1 or 6.1.

## 12. Joint handoff

**New proved interface-A payload:**
\[
E^-\le q/16,\ E^+\le q/[8(r+1)]
\Longrightarrow
\Delta_ZH\le12I_Z
\]
under `I_Z<=rI_x`; and under total fixed-relative error `E<=q/16` there exists a realizable first-mismatch order with
\[
D_T\ge15rq/16,
\qquad
H(Y_x\mid T)\le h_2(E).
\]

**Exact next unpaid implication:** prove (8.2), or give a source-exact recursive residual-error determination whose corrected entropy charges sum to `O(rq)` while each folded drift/crossing/refund is used once. The natural recipient is the account01 adaptive pivotality Bellman compiler, with account04's crossing/defect ledger as the nonreuse accounting layer.

**FULL-PROBLEM CHANGE:** NONE — full uniform-cube FEI remains OPEN / NOT PROVED.  
**MECHANISM CHANGE:** YES — the fixed-relative stalled branch now has an asymmetric paid full-block subcase and a genuinely physical random-order stopped-tree denominator/information theorem.
