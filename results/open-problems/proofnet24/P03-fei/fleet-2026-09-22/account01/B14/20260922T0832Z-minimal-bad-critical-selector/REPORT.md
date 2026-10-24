# account01/B14 — minimal-bad physical block selector produces a terminal strict critical core with positive-excess budget

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact change in the missing implication

The live full target remains FEI, equivalently the universal all-gate inequality from `continuations/2026-09-22-gate-reformulation/REPORT.md`. The fixed scalar-lift potential `Gamma^dagger` is already refuted by the source-certified composition-prime Numaro gate, so nothing below promotes that fixed candidate.

This run addresses the restriction-selector subproblem assigned to B14: turn an arbitrary bad restriction state into an actual source-valid critical state on which the corrected-ratio terminal inequalities and the all-row Han crossing bank apply simultaneously.

The named newest compatible other-account theorem used substantively is account04/B13,

`proofnet24/P03-fei/fleet-2026-09-22/account04/B13/20260922T074113Z-han-crossing-collapse/REPORT.md`,

which proves, on an actual corrected-ratio critical core,

\[
\rho\sum_i C_i+\sum_i W_i\le \mathcal P.
\]

Its stated remaining arrow is to pass from an arbitrary bad terminal leaf to an actual critical restriction descendant without losing the physical-row structure. The theorem below supplies exactly that passage, and yields a positive-excess strengthening of the Han budget.

The source-exact singleton identities used are

\[
\Delta_i\mathcal F\le B_i-W_i,
\qquad
D_i:=\mathcal J(f)-\mathbb E_b\mathcal J(f_{i=b})=q_i+C_i.
\tag{0.1}
\]

After minimizing-character/median recentering,

\[
q_i=\min(\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f))\le\frac12,
\qquad \mathcal J=\sum_iq_i,
\]

\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),
\quad
\mathcal P=\sum_i\mathfrak j(q_i),
\quad
\mathcal F=H-\mathcal P,
\]

and

\[
c_j(i)=\mathbb E(2q_j(X_i)-1)_+,
\quad C_i=\sum_{j\ne i}c_j(i),
\quad W_i=\sum_{j\ne i}\mathfrak j'(q_j)c_j(i),
\quad B_i=H(X_i\mid X_{-i}).
\]

Character multiplication preserves `H`, the folded influences, hence `J`, `P`, and `F`, so recentering after a physical restriction does not alter the quantities used below.

## 1. Actual physical block-selection policy

Fix `K>2` and call a state `K`-bad if

\[
\mathcal F(f)>K\mathcal J(f).
\tag{1.1}
\]

Given a `K`-bad physical restriction state `g`, inspect its finite family of physical restriction descendants. Choose a `K`-bad descendant `h` with the **smallest number of remaining original coordinates**; break ties lexicographically by the fixed coordinate set and branch assignment. Equivalently, choose the largest-cardinality genuine physical block `A` and branch value `z` for which `g_{A=z}` remains `K`-bad, and recenter the resulting state by a character.

This is a genuine original-coordinate block-selection policy. It uses no auxiliary selector labels, no affine coordinate change, no fixed-depth hypothesis and no coverage assumption. It is intentionally a global/existential block search rather than the false local rule “follow an immediately bad child”: a safe intermediate restriction can in principle have a bad deeper descendant, so the proof must minimize over **all** physical descendants.

## 2. Minimal-bad descendant theorem

### Theorem 2.1

Let `h` be the minimum-remaining-dimension `K`-bad descendant selected above and put

\[
E:=\mathcal F(h)-K\mathcal J(h)>0.
\tag{2.1}
\]

Then `h` has dimension at least two and satisfies:

1. Every proper physical restriction descendant of `h` is `K`-safe. In particular, for every remaining coordinate `i` and both branches `b`,
   \[
   \mathcal F(h_{i=b})\le K\mathcal J(h_{i=b}).
   \tag{2.2}
   \]
2. Every physical singleton obeys
   \[
   \boxed{B_i-W_i\ge E+K(q_i+C_i).}
   \tag{2.3}
   \]
3. Hence every singleton lies in the strict terminal class:
   \[
   \boxed{h_2(q_i)-W_i\ge E+K(q_i+C_i)>K(q_i+C_i).}
   \tag{2.4}
   \]
4. `h` is a strict restriction-critical core. If
   \[
   \rho:=\frac{\mathcal F(h)}{\mathcal J(h)}=K+\frac{E}{\mathcal J(h)},
   \tag{2.5}
   \]
   every proper noncharacter physical descendant has corrected ratio at most `K<rho`.
5. Writing `n` for the remaining dimension,
   \[
   \boxed{(n-1)E+K\sum_iC_i+\sum_iW_i\le\mathcal P.}
   \tag{2.6}
   \]
   Consequently
   \[
   \boxed{E\le\frac{\mathcal P}{n-1}\le\frac{2}{(n-1)\ln2}\mathcal J,}
   \tag{2.7}
   \]
   \[
   \boxed{\sum_iC_i\le\frac{\mathcal P}{K}\le\frac{2}{K\ln2}\mathcal J.}
   \tag{2.8}
   \]
6. Every coordinate satisfies the scalar gap
   \[
   \boxed{h_2(q_i)-Kq_i\ge E.}
   \tag{2.9}
   \]
   Thus if `x_K` is the nonzero root of `h_2(x)=Kx` in `(0,1/2]`, then `q_i<x_K` for all remaining coordinates.

### Proof

Minimum remaining dimension gives (2.2) for **every** proper descendant, not just the immediate children. A one-variable state is never `K`-bad: after character recentering a nonconstant one-variable Boolean function is a character and has `H=P=F=J=0`; constants are harmless. Hence `n>=2`.

For a remaining coordinate `i`, average (2.2) over the two branches and subtract from (2.1):

\[
\begin{aligned}
\Delta_i\mathcal F
&=\mathcal F(h)-\mathbb E_b\mathcal F(h_{i=b})\\
&\ge K\mathcal J(h)+E-K\mathbb E_b\mathcal J(h_{i=b})\\
&=E+KD_i\\
&=E+K(q_i+C_i).
\end{aligned}
\tag{2.10}
\]

Together with the source-exact upper bound `Delta_i F<=B_i-W_i`, this proves (2.3).

Also

\[
B_i=H(X_i\mid X_{-i})\le H(X_i)=h_2(\Pr[X_i=1])=h_2(q_i),
\tag{2.11}
\]

because `h_2` is symmetric under folding. This yields (2.4) and (2.9).

Equation (2.5) follows from the definition of `E`, and every proper descendant is `K`-safe, so `h` is strict restriction-critical.

Summing (2.3) gives

\[
nE+K\left(\mathcal J+\sum_iC_i\right)\le\sum_iB_i-\sum_iW_i.
\tag{2.12}
\]

Han/chain rule gives

\[
\sum_iB_i\le H(X)=H(h)=\mathcal F(h)+\mathcal P
=K\mathcal J+E+\mathcal P.
\tag{2.13}
\]

Insert (2.13) into (2.12) and cancel `K J` to obtain (2.6). Since `C_i,W_i>=0` and the source scalar estimate gives `P<=(2/ln2)J`, (2.7)-(2.8) follow. `QED`

## 3. Substantive use of account04/B13

The endpoint `h` is now proved to satisfy the exact hypothesis that account04/B13 previously had to assume: it is a genuine strict corrected-ratio critical core. Therefore its all-row theorem applies to the same physical rows without any relabeling:

\[
\boxed{\rho\sum_iC_i+\sum_iW_i\le\mathcal P.}
\tag{3.1}
\]

The new bound (2.6) is not a restatement: it retains the positive badness excess and charges `(n-1)E` globally. Hence a high-dimensional minimum bad core must lie within `O(J/n)` of the boundary `F=KJ` while also obeying the account04/B13 dimension-free crossing bank.

This closes the specific descendant-selection interface left open by that peer report: one does not need a separate compactness assumption, fixed-depth terminal coverage, or a change of physical coordinates to put the terminal and critical structures on the same Boolean state.

## 4. Required obstruction checks

**Addressing.** The known addressing examples refute every-coordinate local payment on an arbitrary parent. The policy here selects one deepest bad physical block globally; simultaneous endpoint inequalities then follow from minimality and the exact restriction identity, not from a prescribed-coordinate erasure majorant.

**Majority.** The prior B14 result shows that every fixed-depth local `F(d)`-only tree is defeated by sufficiently large odd majority. The present policy has no fixed-depth requirement and can select a block whose size grows with dimension, so that obstruction is preserved rather than contradicted.

**Tribes / sparse defect.** No density or regularity hypothesis appears. If such a state is `K`-bad, finite descendant minimization applies; otherwise no selector conclusion is asserted.

**Tensor replication.** Tensor replication can preserve weak critical ratios while destroying normalized shell mass. Minimum-dimension bad selection avoids that weak-shell inference: all proper descendants are `K`-safe and hence have ratio strictly below the selected endpoint's `rho`.

**Biased/all-gate limit.** The fixed `Gamma^dagger` remains refuted by the certified Numaro prime gate. The theorem here is a restriction-side structural implication and is not a claim that this fixed potential, or any finite test, proves FEI.

## 5. Exact old/new missing implications

**Old missing implication.** From an arbitrary bad terminal state, obtain an actual corrected-ratio critical physical restriction descendant while retaining the terminal row inequalities and the all-row crossing bank.

**New proved implication.** The global physical-block selector produces `h` which is simultaneously:

- `K`-bad with excess `E>0`;
- `K`-safe on every proper physical descendant;
- strict ratio-critical with `rho>K`;
- in the strict terminal class `h_2(q_i)-W_i>K(q_i+C_i)` on every physical row;
- subject to the inherited Han bank (3.1) and the stronger positive-excess budget (2.6).

**First remaining target-level implication.** Rule out the existence of a Boolean state satisfying this simultaneous terminal-plus-strict-critical system for some finite universal `K`, or construct a realizable physical block at such an `h` whose corrected-ratio drop contradicts minimal badness. That universal exclusion/block theorem is not proved here.

Therefore this run is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 6. Provenance and scope

Named cross-account result consumed and applied: account04/B13 `20260922T074113Z-han-crossing-collapse/REPORT.md`, specifically its critical-core all-row crossing theorem and its explicit missing descendant-selection arrow. The source-exact corrected restriction inequality and folded-drift identity are from the current joint research state and the same A-interface chain.

No finite test, heuristic or equivalence is promoted to full FEI. No credentials, scheduler identifiers, machine paths, unrelated private data, paid/remote compute, workflows, email/Drive action, public posting or permission changes are included.
