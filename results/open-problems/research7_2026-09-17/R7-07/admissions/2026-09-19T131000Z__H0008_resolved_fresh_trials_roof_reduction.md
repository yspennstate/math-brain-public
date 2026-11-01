Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding model selector is exposed.**

# R7-07 admission-feasibility mathematics — H0008 resolved fresh trials and a finite-roof criterion

Date: 2026-09-19 UTC  
Worker: `R7-07` / native identity `6aabe8413f60819197825dd81ca138ae`  
Root: `research7_2026-09-17/R7-07/`  
Admission state: **PENDING_ADMISSION**. This document does not acquire H0008.  
Canonical source history: `operations/claims/H0008.md`, presently `UNASSIGNED AFTER R14 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`.  
Exact source: Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), “Boundary fluctuations.”

## 1. Purpose and continuity

The previous R7-07 admission-feasibility run proved the exact fresh-edge reset law

\[
Q_j(dT)=\frac{B(T)}{b_j}P_j(dT),\qquad b_j=E_{P_j}B(T),
\]

at a successful no-return regeneration edge, and showed the block-start logarithmic bound

\[
E_{Q_j}[-\log B]\le \frac1{e b_j}.
\]

It also gave the conditional Markov-renewal/Rokhlin occupation formula once the exit-level regeneration roof has finite mean. The unresolved point was C4: prove finite mean of the roof without the invalid shortcut

\[
P(H>m)\stackrel{\rm invalid}{\le}(1-b_*)^m,
\qquad b_*:=\min_j b_j>0,
\]

because candidate no-return events at nested fresh edges are not sequentially resolved.

This note replaces that invalid nested-trial argument by a **resolved fresh-edge trial scheme**. The resulting theorem reduces C4 to one explicit failed-excursion first moment. A second theorem proves C4 outright under a uniform quenched escape lower bound. Neither theorem is asserted to hold under the full H0008 source hypotheses without the stated extra moment/lower-bound condition.

The Section-B methods used here are deliberately different from the previous run's B2/B1/B21 triple:

- **B25 — COUNT THE SAME THING TWICE:** count roof height through sequentially resolved fresh-edge failures rather than nested candidate levels;
- **B11 — DUALIZE:** dualize failed-excursion depth into return probabilities from deep levels;
- **B30 — ONE SCALE / ONE DIRECTION:** isolate the single scalar failed-excursion moment whose finiteness suffices for C4, and solve the stronger uniform-escape slice completely.

## 2. Source-compatible setup

Let the finite type set be `D`. For each type `j`, let `P_j` be the source forward-subtree law. Attach an artificial parent to the root and let

\[
B(T)=P^T_{\varnothing}\{\text{never hit the artificial parent}\}\in[0,1]
\]

be the quenched no-return probability. Put

\[
b_j:=E_{P_j}B(T),\qquad b_*:=\min_{j\in D}b_j.
\]

For the surviving/transient type classes relevant to the harmonic-flow problem, the previous feasibility note assumes/uses `b_j>0`; finite `D` then gives `b_*>0`.

Start the simple random walk at a regeneration vertex `v_0`: the edge by which the walk entered `v_0` was fresh and will never be crossed backwards. Consequently the entire forward subtree below `v_0` was fresh at the regeneration crossing.

Let `H` denote the increase in genealogical level from `v_0` to the **next** fresh-edge regeneration vertex. This is the roof needed by the exit-level Rokhlin tower; physical walk time is deliberately not used.

## 3. B25 — resolved fresh-edge trials

The dependence flaw in the naive geometric argument comes from declaring every nested fresh edge a trial before the preceding no-return event has been resolved. Instead use only trials whose predecessors have actually failed.

### Definition 3.1 (resolved trial sequence)

Set the initial resolved time to the regeneration time at `v_0`. Inductively, provided no successful trial has occurred:

1. after the previous trial has returned across its candidate edge, wait until the walk first traverses an oriented parent-to-child edge `(x_r,y_r)` whose head `y_r` has never previously been visited;
2. call that crossing time `sigma_r`;
3. set
   \[
   rho_r:=\inf\{t>\sigma_r:X_t=x_r\};
   \]
4. the trial **succeeds** if `rho_r=infinity`, and **fails** otherwise;
5. only after a finite `rho_r` do we start looking for trial `r+1`.

On a failed trial define the downward exploration depth

\[
D_r:=\max_{\sigma_r\le t\le\rho_r}
\bigl(|X_t|-|y_r|\bigr)_+.
\]

A transient nearest-neighbour walk on a locally finite tree visits only finitely many vertices during each finite failed trial. If the trial fails, transience then guarantees that a later fresh edge is eventually crossed. Thus the sequence is well-defined until its first success.

Let

\[
N:=\inf\{r\ge1:\rho_r=\infty\}
\]

be the index of the first successful resolved trial.

### Lemma 3.2 (fresh law and one-step success probability)

Conditional on the complete pre-`sigma_r` history and on the type `J_r=j` of `y_r`, the forward subtree below `y_r` has law `P_j` and is independent of the explored past. Consequently

\[
P(\rho_r=\infty\mid\mathcal F_{\sigma_r-},J_r=j)=b_j\ge b_*.
\]

#### Proof

The head `y_r` is unvisited by definition. In a multitype branching tree, conditional on its type, the descendants below an unvisited child are generated independently of the already exposed part of the tree with law `P_j`. Once the edge is crossed, the event that the walk never returns to `x_r` depends only on that forward subtree and the post-crossing walk. Averaging the quenched no-return probability `B(T)` under `P_j` gives `b_j`. `square`

### Corollary 3.3 (the number of resolved failures really is geometric-dominated)

For every `r>=0`,

\[
P(N>r)\le(1-b_*)^r.
\]

In particular `N<infinity` almost surely and

\[
E(N-1)\le\frac{1-b_*}{b_*}.
\]

#### Proof

Unlike the discarded nested candidates, trial `r+1` is not exposed until trial `r` has returned and is therefore known to have failed. Lemma 3.2 applies at each actual trial time. Induction gives the tail bound. `square`

This is the correct place where a geometric estimate is legitimate: it controls the **number of sequentially resolved failures**, not the roof height itself.

## 4. The exact new scalar obstruction

For a fresh type-`j` trial, let `F` denote the event that the walk returns to the parent and let `D` be its maximum downward depth before that return, as above. Define the annealed failed-excursion depth moment

\[
\ell_j
:=E_{T\sim P_j}E^T_{\varnothing}
\bigl[D\,\mathbf 1_F\bigr]
\in[0,\infty],
\qquad
\ell_*:=\max_j\ell_j.
\]

Also define

\[
c_j:=E[(1+D)\mathbf1_F]
=(1-b_j)+\ell_j,
\qquad c_*:=\max_j c_j.
\]

The point is that `ell_j` is an **unconditional** failed-excursion moment. It does not divide by a possibly tiny return probability and it contains exactly the height cost generated when a resolved trial fails.

### Lemma 4.1 (deterministic roof domination)

For every sample path on which `N<infinity`,

\[
\boxed{
H\le 1+\sum_{r=1}^{N-1}(1+D_r).
}
\tag{4.1}
\]

#### Proof

Maintain the maximal genealogical depth, relative to `v_0`, of the already explored forward set immediately before each trial. Initially it is zero. A fresh candidate head `y_r` lies one edge beyond an already explored vertex, so its depth is at most the current explored maximum plus one.

If trial `r` fails, the excursion below `y_r` returns across `(x_r,y_r)` and can enlarge the explored maximum by at most `1+D_r`. Between this return and the next trial, the walk stays inside the already explored set until it first crosses a new edge, so there is no additional increase before the next candidate head is reached.

When trial `N` succeeds, its head is itself a regeneration vertex and lies at most one level beyond the explored maximum accumulated through the preceding failures. Summing these increments gives (4.1). `square`

### Theorem 4.2 (finite-roof reduction)

Assume

\[
b_*>0,\qquad \ell_*<\infty.
\tag{4.2}
\]

Then the next regeneration exists almost surely and its exit-level roof has finite mean, uniformly over the starting regeneration type. Quantitatively,

\[
\boxed{
E H\le 1+\frac{c_*}{b_*}
=1+\frac{\max_j\{1-b_j+\ell_j\}}{b_*}<\infty.
}
\tag{4.3}
\]

#### Proof

By Corollary 3.3, `N<infinity` almost surely. From (4.1), Tonelli, and the fact that trial `r` occurs only on `{N>=r}`,

\[
E H
\le 1+
\sum_{r\ge1}
E\left[
\mathbf1_{\{N\ge r\}}
(1+D_r)\mathbf1_{\{\rho_r<\infty\}}
\right].
\]

Condition on the history immediately before trial `r` and then on the type `j` of its fresh head. The forward subtree is fresh with law `P_j`; hence

\[
E[(1+D_r)\mathbf1_{\{\rho_r<\infty\}}
\mid\mathcal F_{\sigma_r-},J_r=j]
=c_j\le c_*.
\]

Therefore

\[
E H
\le1+c_*\sum_{r\ge1}P(N\ge r)
\le1+c_*\sum_{r\ge1}(1-b_*)^{r-1}
=1+\frac{c_*}{b_*}.
\]

This proves (4.3). `square`

### What this theorem changes

The earlier C4 obstruction was “nested no-return dependence.” Theorem 4.2 removes that obstruction completely. The remaining C4 question is now the single, explicit moment problem

\[
\boxed{
\max_j E_{P_j}E^T_{\varnothing}
[D\,\mathbf1_{\{\text{return to parent}\}}]<\infty.
}
\tag{4.4}
\]

No independence between nested candidate edges is needed.

The R14 extinction-Jacobian theorem already proves exponential decay for **genealogical stretches with exactly one infinite child**. That is relevant evidence for (4.4), but it does not by itself prove (4.4): a failed excursion may enter a branch-producing region, wander deeply, and eventually return. I do not identify those two notions.

## 5. B11 — dualizing failed depth into return probabilities

For a fixed rooted transient tree `T` with artificial parent `o_*`, write `o` for its root. Let

\[
D=\max_{0\le t\le\tau_{o_*}}|X_t|
\]

on the event `F={tau_{o_*}<infinity}`. Tail summation gives the exact identity

\[
E_o^T[D\mathbf1_F]
=\sum_{h\ge1}P_o^T(D\ge h,\tau_{o_*}<\infty).
\tag{5.1}
\]

At the first hit of level `h`, say at vertex `z`, a subsequent return to `o_*` must cross the unique `h+1` ancestral edges. If `B(v)` denotes the no-return probability from a vertex `v` to its parent in its forward subtree, then strong Markov along the ancestral chain yields

\[
P_z^T(\tau_{o_*}<\infty)
=\prod_{v\in[o,z]}(1-B(v)).
\tag{5.2}
\]

Consequently

\[
P_o^T(D\ge h,F)
\le
E_o^T\!\left[
\mathbf1_{\{\tau_h<\tau_{o_*}\}}
\prod_{v\in[o,X_{\tau_h}]}(1-B(v))
\right]
\le
\sup_{|z|=h}\prod_{v\in[o,z]}(1-B(v)).
\tag{5.3}
\]

The last supremum bound is crude, but it exposes the correct dual object: failed-depth integrability is controlled by products of **return probabilities** down ancestral rays, not by products of unresolved regeneration indicators.

This is the natural bridge to the R14 pipe calculation: its matrix `J` controls one particular return-heavy channel (unique infinite-child pipes). To finish the full source, one needs an annealed summability statement for (5.3) that also covers branch-producing excursions.

## 6. B30 — complete uniform-escape slice

The scalar obstruction (4.4) can be solved under a transparent stronger hypothesis.

### Hypothesis UE(epsilon)

There exists `epsilon>0` such that for every surviving forward subtree of every type,

\[
B(T)\ge\epsilon
\qquad\text{almost surely.}
\tag{6.1}
\]

This is **not** asserted for the general H0008 source; long thin pipes can drive conductance toward zero. The purpose is to certify that the resolved-trial mechanism itself closes C4 once small-conductance traps are excluded.

### Lemma 6.1 (failed excursions have an exponential depth moment under UE)

Under UE(epsilon), for every fresh trial and every `h>=1`,

\[
P(D\ge h,F\mid\text{pretrial history})
\le(1-\epsilon)^{h+1}.
\tag{6.2}
\]

Hence

\[
E[D\mathbf1_F\mid\text{pretrial history}]
\le\frac{(1-\epsilon)^2}{\epsilon},
\tag{6.3}
\]

and

\[
E[(1+D)\mathbf1_F\mid\text{pretrial history}]
\le\frac{1-\epsilon}{\epsilon}.
\tag{6.4}
\]

#### Proof

On `{D>=h}`, stop when level `h` below the fresh trial root is first hit, at some vertex `z`. To return across the trial edge, the walk must then hit the parent successively across `h+1` ancestral edges. At each vertex `v`, UE gives

\[
P_v(\text{ever hit parent}(v))=1-B(v)\le1-\epsilon.
\]

Strong Markov at the successive ancestor hitting times gives conditional return probability at most `(1-epsilon)^{h+1}`. This proves (6.2). Summing over `h` gives (6.3). Finally `P(F)=1-B(root)<=1-epsilon`; adding this to (6.3) yields

\[
(1-\epsilon)+\frac{(1-\epsilon)^2}{\epsilon}
=\frac{1-\epsilon}{\epsilon},
\]

which is (6.4). `square`

### Theorem 6.2 (explicit finite roof under UE)

Under UE(epsilon), the resolved-trial regeneration roof satisfies

\[
\boxed{
E H\le 1+\frac{1-\epsilon}{\epsilon^2}.
}
\tag{6.5}
\]

#### Proof

Here `b_*>=epsilon`, while Lemma 6.1 gives `c_*<=(1-epsilon)/epsilon`. Insert those two bounds in Theorem 4.2. `square`

Thus the finite-roof problem is fully solved for the uniform-escape slice. The general source question is exactly how far one can replace UE by the annealed return-product summability in (4.4)/(5.3).

## 7. A second exact reformulation: renewal density instead of roof tails

There is another useful way to package C4 which matches the one-type Rousselin construction.

Let `(J_k,H_k)` be the regeneration-type Markov renewal process once C1--C3 are valid. Start its finite-state type chain in a stationary distribution `pi`, and let

\[
S_n=H_0+\cdots+H_{n-1},\qquad
N(t)=\max\{n:S_n\le t\}.
\]

### Proposition 7.1 (positive regeneration-level density iff finite mean roof)

Assume the stationary Markov-renewal sequence is ergodic and `H_k>=1`. Put

\[
m=E_\pi H_0\in[1,\infty].
\]

Then

\[
\frac{N(t)}t\longrightarrow
\begin{cases}
1/m,&m<\infty,\\
0,&m=\infty,
\end{cases}
\quad\text{a.s. and in }L^1.
\tag{7.1}
\]

In particular, any bound

\[
\liminf_{t\to\infty}\frac{E_\pi N(t)}t\ge c>0
\tag{7.2}
\]

implies

\[
E_\pi H_0\le1/c.
\tag{7.3}
\]

#### Proof

If `m<infinity`, the ergodic theorem gives `S_n/n -> m`; inversion of the increasing sequence gives `N(t)/t -> 1/m`.

If `m=infinity`, for every `M`, set `H_k^(M)=min(H_k,M)`. The ergodic theorem gives

\[
\liminf_{n\to\infty}\frac{S_n}{n}
\ge E_\pi H_0^{(M)}.
\]

Let `M->infinity`; monotone convergence makes the right side diverge, so `S_n/n->infinity` and therefore `N(t)/t->0`. Since `0<=N(t)/t<=1`, dominated convergence upgrades both cases to `L^1`. Equation (7.2) then forces `m<infinity` and (7.3). `square`

Rousselin's one-type exit-time tower has precisely this architecture: regeneration heights form the base-return roof, and the paper establishes a finite mean before building the tower. The proposition shows that a future multitype proof does **not** need a geometric tail for `H`; a positive first-moment density of regeneration levels would suffice.

## 8. Relation to the previous reset/tower note

Combining the previous R7-07 results with Theorem 4.2 gives the following conditional chain, all within the source-matching simple random walk:

1. **fresh reset:** `Q_j=(B/b_j)P_j`;
2. **finite-state regeneration kernel:** branching + strong Markov reduce successive blocks to their regeneration types once the source-matching resolved trial is used;
3. **finite roof:** follows from `(4.4)`, and in particular from UE(epsilon);
4. **tower:** the occupation formula
   \[
   \mu(A)=
   \frac{\sum_i\pi_iE_{Q_i}\sum_{r=0}^{H-1}\mathbf1_{\{\mathcal E_r\in A\}}}
        {\sum_i\pi_iE_{Q_i}H}
   \]
   is then a probability and is invariant by the previously proved telescoping argument;
5. **one direction of absolute continuity:** the block-start term plus `Q_i~P_i` yields the source mixture `<< mu` under the recorded positivity assumptions;
6. **block-start log control:** `E_Q[-log B]<=1/(e b_i)` is already finite.

What is still missing for the full harmonic-measure clause is:

- prove (4.4) under the actual source hypotheses, or replace it by a direct positive regeneration-level density argument;
- prove the reverse within-block absolute continuity/equivalence needed by the PF-KL route;
- verify all remaining log-integrability terms under the actual source law;
- identify the projected tower law with the stationary solution needed by the prior PF-KL theorem;
- then execute the source-level dimension-drop argument and independent audits.

## 9. Why this does not silently claim H0008

H0008 is released by R14 but its canonical history already occupies `operations/claims/H0008.md`. R7-07's installed acquisition rule is create-only at exactly that path and forbids overwriting a competing/historical claim on collision. Therefore this worker remains **PENDING_ADMISSION** and records this theorem only as bounded admission-feasibility work. No claim file is changed.

The theorem is useful even if another worker later lawfully acquires H0008: it replaces the false nested-geometric heuristic by a correct sequential mechanism and leaves a single explicit moment as the C4 gate.

## 10. Dated prior-art/source check (2026-09-19)

Primary/source records checked in this run:

- Kumar, arXiv:2608.15987v1, 17 Aug 2026, Section 12.3 OP(6), remains the source in the canonical repository history;
- Kumar--Duddala, arXiv:2608.21125, 21 Aug 2026, is the later companion on front propagation/Bramson correction and continuous-type limit theory, not a finite-type harmonic-exit solution;
- Pierre Rousselin, arXiv:1711.07920, constructs an invariant forward environment at exit times in the one-type Galton--Watson random-environment setting using regeneration and a Rokhlin tower;
- Rousselin, arXiv:1708.06965, gives explicit invariant measures for one-type marked Galton--Watson flow rules;
- the R14 handoff also records the neighboring finite-type reversible-environment work of Altok and Dembo--Sun.

No source located in the bounded check was used as a theorem that directly proves Theorem 4.2 for this multitype model. Search misses do not prove novelty, so **novelty is UNVERIFIED**.

## 11. Bottom line

The invalid inference

\[
b_*>0\quad\Longrightarrow\quad P(H>m)\le(1-b_*)^m
\]

is still rejected.

The correct replacement is

\[
\boxed{
 b_*>0,\quad
 \ell_*:=\max_jE[D\mathbf1_{\rm return}]<\infty
 \quad\Longrightarrow\quad
 E H\le1+\frac{\max_j(1-b_j+\ell_j)}{b_*}<\infty.
}
\]

The nesting problem disappears because only **resolved** fresh-edge failures are counted. Under the stronger uniform-escape hypothesis `B>=epsilon`, this gives the explicit source-slice bound

\[
\boxed{
EH\le1+\frac{1-\epsilon}{\epsilon^2}.
}
\]

The next mathematically useful attack is therefore not another generic regeneration argument. It is to bound the annealed failed-excursion depth moment (4.4), preferably by combining the R14 subcritical extinction-Jacobian control of one-infinite-child pipes with a separate estimate for genuine branch-producing returns.
