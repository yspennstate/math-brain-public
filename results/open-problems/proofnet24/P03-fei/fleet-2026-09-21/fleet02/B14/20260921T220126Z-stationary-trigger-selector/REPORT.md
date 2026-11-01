TASK: B14 ACCOUNT: fleet02 RUN: 2026-09-21T22:01:26.449481Z — stationary closed-trigger selector and globally nonreused physical restriction compiler

**Status:** PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical/cognitive brain retrieval was consumed.

**Model self-report:** GPT-5.6 Sol. **Requested reasoning:** maximum actually supported. **Configured reasoning:** UNKNOWN / not exposed. **Known reasoning level:** UNKNOWN / not exposed. Provider reasoning-token usage and provider thinking time are not exposed.

**FULL-PROBLEM CHANGE:** NONE. No universal FEI theorem is proved.

**MECHANISM CHANGE:** YES. The preceding B14 run reduced a useful physical step to finding one block/survivor pair with a substantial posterior crossing and a paid corrected erasure. The present run does not rescan scalar thresholds. It builds a mass-weighted selector on the directed system of near-subcube control blocks. A closed certified trigger subsystem automatically contains one row whose average control influence is no larger than the pivot influence. That converts the existing coefficient-12 near-support block theorem into a genuinely realizable physical step. Iterating only such steps gives an exact globally nonreused entropy ledger; if the policy stalls, the remaining leaf has an explicit graph-theoretic obstruction (empty certified trigger kernel).

No novelty or publication-priority claim is made.

## 0. Fresh sources and required last-three comparison

Fresh scientific `master` was resolved before this write. Applicable `FLEET_RULES.md` and `proofnet24/P03-fei/README.md` were read. The named completed cross-account inputs actually used are:

1. **fleet04/B14**, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260921T211337Z-posterior-variance-short-circuit/REPORT.md`. It supplies the physical short-circuit posterior-crossing ledger and, in particular, the fact that a pivotality event within error `epsilon` of a defining subcube has crossing at least `(p-epsilon)_+`; it also keeps the exact folded drift `D_A=I_A+C_A` and explicitly distinguishes the certified `q/(16r)` Shannon-payment regime from the false fixed-relative full-block claim.
2. **fleet01/B18**, newest compatible `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`. It supplies the character-invariant folded activation potential `A_z`, the globally telescoping adaptive reserve `sum w_u Lambda_u<=J(root)`, and the corrected entropy/crossing compiler. The selector below is physical and descendant-recentering compatible, so this reserve can be attached without a gauge leak.
3. **fleet03/B13**, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260921T203308Z-integrability-dag/REPORT.md`. It supplies the robust trigger-DAG theorem: reciprocal low-defect near-subcube rows form exact compatible cliques, one-way edges have a strict dyadic scale drop, and sink cliques integrate to near one-point-defect factors. I use it only to interpret the stalled selector geometry; I do not reprove its stability theorem.
4. **fleet03/B14**, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B14/20260921T214637Z-adaptive-fixed-relative/REPORT.md`. It proves that the known fixed-relative `q/16` family does *not* inherit the full-block logarithmic obstruction under the natural short-circuit tree: the exact stopped crossing/drift are proved and finite computations through `r=200` approach ratio four. This means that family cannot be cited as a refutation of the adaptive stalled-leaf programme below; its all-r bound remains unproved.

The preceding three substantive B14 reports were:

- `20260921T193008Z-affine-partition-hash-budget`: a spendable affine coalescence drop, but a one-shot hash erasure remained;
- `20260921T195815Z-sequential-erasure-refund`: exact projection refund, but still the residual `B_seq=O(D)` on the same high-drop partition;
- `20260921T210915Z-crossing-information-selector`: materially changed to a physical posterior-crossing/KL mechanism and proved that substantial crossing pays one rare survivor's Shannon scale, but still required existence of one block with corrected erasure `O(h_2(p_j))`.

Thus the universal missing implication across the last three reports is still a realizable selective restriction with globally nonreused Shannon payment. This report executes a different mechanism: finite-state stationary flow on the *control-block dependency graph*, followed by a real physical block restriction.

Fleet creative moves used here: **#25 count the same thing twice** (stationary mass flow), **#27 swap the quantifiers** (closed subsystem first, then existential row), and **#13 find what only increases/terminates** (iterative pruning to a maximal closed certified kernel). A deliberate negation test shows closure is necessary; see Section 6.

## 1. Normalization and certified near-subcube rows

Work in the median-character gauge. For every active physical coordinate `i`,

\[
p_i=\operatorname{Inf}_i(f)\in(0,1/2],\qquad
J(f)=\sum_i p_i.
\]

For a pivot `j`, let

\[
\eta_j(x_{-j})=1_{\{f(x)\ne f(x+e_j)\}}
\]

be its pivotality event, so `Pr(eta_j=1)=p_j`.

Call a chosen triple `(j,Z_j,Q_j)` **C12-certified** when:

- `Z_j` is a nonempty physical control block disjoint from `{j}`, with `r_j=|Z_j|`;
- `Q_j` is one atom of the `Z_j` cube, hence has density
  \[
  q_j=2^{-r_j};
  \]
- the support error obeys
  \[
  \epsilon_j:=\Pr(\eta_j\triangle1_{Q_j})
  \le \frac{q_j}{16r_j}.
  \tag{1.1}
  \]

The already proved near-support block theorem says that if, in addition,

\[
I_{Z_j}:=\sum_{i\in Z_j}p_i\le r_jp_j,
\tag{1.2}
\]

then the genuine PHYSICAL block restriction satisfies

\[
\boxed{\Delta_{Z_j}H\le12 I_{Z_j}.}
\tag{1.3}
\]

No every-coordinate statement is being asserted. The entire task below is to produce (1.2) for one row from a realizable system.

## 2. PROVED: stationary mass-weighted control selector

### Theorem 2.1 — closed-trigger selector

Let `S` be a nonempty finite set of C12-certified pivots, with one chosen block `Z_j` for each `j in S`. Assume the system is **closed**:

\[
\boxed{Z_j\subseteq S\qquad\text{for every }j\in S.}
\tag{2.1}
\]

Then there exists `j in S` such that

\[
\boxed{
\frac1{r_j}\sum_{i\in Z_j}p_i\le p_j,
\qquad\text{equivalently } I_{Z_j}\le r_jp_j.
}
\tag{2.2}
\]

### Proof

Define a row-stochastic matrix on `S` by

\[
P_{ji}=\frac{1_{\{i\in Z_j\}}}{r_j}.
\tag{2.3}
\]

Because `S` is finite, `P` has a stationary probability vector `pi` (choose any recurrent class if the chain is reducible):

\[
\pi_i=\sum_j\pi_jP_{ji}.
\]

Count the same influence mass before and after one stationary transition:

\[
\begin{aligned}
\sum_j\pi_j\frac{I_{Z_j}}{r_j}
&=\sum_j\pi_j\sum_iP_{ji}p_i\\
&=\sum_i\left(\sum_j\pi_jP_{ji}\right)p_i\\
&=\sum_i\pi_ip_i.
\end{aligned}
\tag{2.4}
\]

Hence the stationary average of `I_{Z_j}/r_j-p_j` is exactly zero. It cannot be positive at every state in the support of `pi`; therefore some `j` satisfies (2.2). QED.

This is the requested **existential-coordinate selector** in a mass-weighted form. It does not say that every prescribed row pays, and it uses physical controls only.

## 3. PROVED: the selected row is a paid physical restriction with a real crossing refund

Fix the row `j` given by Theorem 2.1. By (1.1)--(1.2), the coefficient-12 block theorem gives (1.3).

The same near-subcube geometry gives an actual posterior crossing on the same block. Revealing all of `Z_j`, the atom `Q_j` alone contributes

\[
c_j(Z_j)\ge p_j-\epsilon_j.
\tag{3.1}
\]

Since `|p_j-q_j|<=epsilon_j`,

\[
p_j\ge q_j-\epsilon_j
\quad\Longrightarrow\quad
\frac{\epsilon_j}{p_j}\le\frac1{16r_j-1}.
\]
Therefore, with

\[
\alpha_r:=\frac{16r-2}{16r-1},
\]

\[
\boxed{c_j(Z_j)\ge\alpha_{r_j}p_j.}
\tag{3.2}
\]

Fleet04's exact centered folded-drift identity gives

\[
D_{Z_j}:=J(f)-\mathbb E_zJ(f_{Z_j=z})
=I_{Z_j}+C_{Z_j}
\ge I_{Z_j}+c_j(Z_j).
\tag{3.3}
\]

Combining (1.3), (2.2), (3.2), and (3.3),

\[
\boxed{
\frac{\Delta_{Z_j}H}{D_{Z_j}}
\le
\frac{12r_j}{r_j+\alpha_{r_j}}
=:
C_{r_j}<12.
}
\tag{3.4}
\]

Explicitly

\[
C_r=\frac{12r(16r-1)}{16r^2+15r-2}.
\tag{3.5}
\]

For `r=1,2,3,4,5` this is approximately

\[
6.20690,\ 8.08696,\ 9.04813,\ 9.63057,\ 10.02114,
\]

and `C_r` increases to 12. These are local paid-step constants, not a universal FEI constant.

The same step is compatible with the two newest global refund banks. With

\[
\mathcal F=H-\sum_i\mathfrak j(p_i),
\]

fleet01/fleet04 curvature gives

\[
\Delta_{Z_j}\mathcal F
\le B_{Z_j}-\mathfrak j'(p_j)c_j(Z_j)
\le12I_{Z_j}-\mathfrak j'(p_j)c_j(Z_j).
\tag{3.6}
\]

And for fleet01's folded cooling potential `A_z`, at the current dimension-cooling scale,

\[
\Delta_{Z_j}(\mathcal F-\lambda\mathcal A_z)
\le
12I_{Z_j}-\mathfrak j'(p_j)c_j(Z_j)-\lambda\Lambda_{Z_j}.
\tag{3.7}
\]

Here `Lambda` is globally summable by the fleet01 theorem. Equation (3.7) is only a compatibility refinement; the basic global compiler below already closes every successful step using (1.3), without double-counting crossing or activation credits.

## 4. PROVED: an adaptive physical compiler with exact nonreuse

At any centered noncharacter node, form a chosen C12-certified trigger system. Repeatedly prune rows whose chosen control block is not contained in the current row set:

\[
S_0=S,\qquad
S_{m+1}=\{j\in S_m:Z_j\subseteq S_m\}.
\tag{4.1}
\]

Because the set is finite, this stabilizes at a maximal closed subset `S_infty`.

**Policy.** If `S_infty` is nonempty, apply Theorem 2.1 inside it and physically restrict the selected block `Z_j`. Re-center each child and repeat. If `S_infty` is empty, stop and label that leaf **STALLED**. Characters also stop.

Every successful internal node `v` obeys

\[
\Delta_vH\le12D_v.
\tag{4.2}
\]

Let `w_v` be the reach probability. Physical folded drift and entropy both telescope on the finite tree:

\[
\sum_{v\text{ successful}}w_vD_v
=J(f)-\mathbb E_{\ell}J(f_\ell),
\tag{4.3}
\]

\[
\sum_{v\text{ successful}}w_v\Delta_vH
=H(f)-\mathbb E_{\ell}H(f_\ell).
\tag{4.4}
\]

Hence

\[
\boxed{
H(f)-12J(f)
\le
\mathbb E_{\ell}
\bigl[H(f_\ell)-12J(f_\ell)\bigr].
}
\tag{4.5}
\]

Character leaves contribute zero to the right side, so only stalled leaves remain.

### Corollary 4.2 — restriction-closed class compiler

Any restriction-closed class for which every centered noncharacter state has `S_infty!=empty` satisfies

\[
\boxed{H(f)\le12J(f)\le12I(f).}
\tag{4.6}
\]

This is a structured-class theorem and a compiler, **not** full FEI.

### Corollary 4.3 — primitive-core localization

If some Boolean function has `H/J>12`, execute the policy until it stalls and choose a stalled descendant with positive excess in (4.5); among such descendants choose one of minimum relevant dimension. That descendant is a legitimate existential **primitive** obstruction and has

\[
H/J>12,
\qquad S_\infty=\varnothing.
\tag{4.7}
\]

Thus any counterexample above 12 can be localized to a minimum-dimensional state with **no nonempty closed C12-certified trigger subsystem**.

This is deliberately different from the refuted claim that every weakly ratio-critical tensor power must have a shell or selector property. Tensor replication does not invalidate (4.7): the descendant is selected existentially after running a real physical policy.

## 5. What the stalled state means in the current joint geometry

When `S_infty=empty`, every C12-certified row is removed at a finite pruning rank. Following a control that caused removal produces a finite directed path from that row to a coordinate that is *not* C12-certified. Thus the paid sector cannot trap itself; it must leak to an exceptional endpoint.

In the stronger fleet03 low-defect / fixed-relative near-subcube regime, reciprocal incidences collapse to exact cliques and every one-way edge drops the dyadic proxy codimension by at least two. Therefore a stalled high-ratio state cannot hide the obstruction in a cyclic family of mutually certified rows. Closed reciprocal C12-certified cliques would trigger Theorem 2.1 and be paid. The remaining obstruction lies at an exceptional endpoint or in a row whose approximation is only at the weaker fixed-relative scale.

The newest fleet03/B14 result matters here. The known fixed-relative family has error `q/16`, so for large `r` it is **not** C12-certified and correctly lands in the stalled residual. But fleet03/B14's exact stopped-tree calculation shows that the same family no longer exhibits the full-block logarithmic divergence under short-circuiting; tested ratios approach four. Therefore that family does not refute the next adaptive extension. It instead identifies the exact next target: extend the paid row definition from `q/(16r)` error toward fixed-relative `q/16` using a nonreused error-discovery ledger.

## 6. Negation test: closure cannot be dropped

The tempting stronger assertion

> every nonempty collection of certified rows contains a row with `I_{Z_j}<=r_jp_j`

is false as a pure selector statement if the controls may leave the collection. The one-row system `S={j}` with `Z_j={e}` and `p_e>p_j` already violates it. This is exactly why Theorem 2.1 requires closure and why the pruning residual in Section 4 is real rather than cosmetic.

No every-coordinate payment proposal is revived.

## 7. Exact before/after and remaining universal obligation

### FULL-PROBLEM CHANGE

**Before:** full FEI open; the best B14 physical compiler required finding one pair `(A,j)` with substantial crossing and corrected erasure at the same Shannon scale.

**After:** full FEI is still open. No finite universal constant is proved. However the entire C12-certified **closed trigger sector** is now solved by an explicit physical adaptive policy with a one-use influence ledger. A high-ratio primitive obstruction above 12 must have empty certified trigger kernel.

### MECHANISM CHANGE

**Before:** search directly for one good block/survivor pair by posterior crossing and scalar erasure bounds.

**After:** construct the directed family of near-subcube control blocks, use stationary flow to force one low-average-control row on every closed component, execute the actual physical block, and prune/recurse. The mechanism is graph/stationary-flow selection, not another threshold scan.

### Quantified remaining formula

For the actual policy,

\[
\boxed{
H(f)-12J(f)
\le
\mathbb E_{\rm stalled}
[H(g)-12J(g)].
}
\tag{7.1}
\]

Thus the universal obligation has become:

> prove that every stalled primitive state with empty C12-certified trigger kernel has `H<=12J`, **or** enlarge the certified class (the fixed-relative short-circuit branch is the immediate candidate) while preserving a physical one-use ledger.

The fleet01 folded activation bank is compatible with that enlargement and can pay an additional globally summable reserve. The fleet04 posterior-crossing ledger supplies the real survivor refund. What is still missing is an analytic fixed-relative error-discovery entropy bound for arbitrary Boolean rows, not a new scalar crossing threshold.

## 8. Literature/status check

A current primary-source check found González--MacManus--Pereyra (29 May 2026), whose stopping-tree framework proves FEI for classes in which the needed restriction-decrement inequalities hold at branching nodes, and Potapov (18 September 2026), who proves FEI for plateaued and partially bent functions with class constants 4 and 2. Neither source supplies the stationary closed-trigger selector above or a universal fixed-relative short-circuit theorem; I make **no novelty claim** from that bounded search. Full classical FEI remains open in the checked literature.

## 9. Claim ledger

- **PROVED:** stationary closed-trigger selector, Theorem 2.1.
- **PROVED:** same selected block has near-maximal pivot crossing and paid physical ratio (3.4).
- **PROVED:** adaptive pruning compiler and exact stalled-leaf residual (4.5).
- **PROVED:** any `H/J>12` counterexample has an existential minimum-dimensional stalled descendant with empty C12-certified trigger kernel.
- **COMPATIBLE / NOT NEWLY AUDITED HERE:** coefficient-12 near-support block theorem, fleet04 crossing/drift identities, fleet01 folded activation telescope, fleet03 integrability DAG.
- **OPEN:** analytic payment for arbitrary fixed-relative/adaptive error-discovery rows; control of the stalled kernel-free primitive state.
- **OPEN:** full uniform-cube FEI.

The report contains no claim that finite checks, a structured class, or the coefficient 12 settle the universal conjecture.
