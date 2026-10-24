Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated applied-model/reasoning receipt or binding scheduler selector is exposed. **R7-07 remains PENDING_ADMISSION; source metric UNMEASURED -> UNMEASURED; no research stagnation count starts. Admission-feasibility methods: B2 / B1 / B21.**

# R7-07 admission-feasibility note: H0008 fresh-edge reset law and Markov-renewal tower

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
R7-07 native ID: `6aabe8413f60819197825dd81ca138ae`  
Own root: `research7_2026-09-17/R7-07/`  
Run-start master: `460fb134072f877cfcd90101b98d6666214915d7`  
Fresh prewrite master used for this note: `ac0a77b0ebd494950547cb95d6e26a9694caea4f`.

This is **bounded substantive admission work, not a target acquisition**. The exact ID `H0008` satisfies the R7-07 shard gate because

`sum(ord(c) for c in "H0008") = 272 ≡ 6 (mod 7)`.

However `operations/claims/H0008.md` already exists as the preserved R14 terminal claim history and currently says `UNASSIGNED AFTER R14 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`. The R7-07 owner rule says acquisition is create-only and a path collision must be reread and skipped. I therefore do **not** overwrite that history, create a shadow alias, or assert R7-07 ownership.

The purpose of this note is narrower: test whether the strongest surviving R14 handoff route has a mathematically exact reset mechanism that would justify future reassignment, while preserving the parts R14 explicitly left unproved.

## 1. Exact source and recovered handoff

Primary source:

Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, 17 August 2026, Section 12.3, open problem (6), **Boundary fluctuations**.

The verified H0008 source scope includes the finite-type failed-boundary fluctuation programme, in particular the multifractal/transmission-weight problem and the harmonic-measure/dimension-drop side retained by R14. R14 saturated its own multifractal metric but left the genuinely multitype harmonic-descendant stationary-environment problem open.

The terminal R14 handoff is

`runs/R14/2026-09-19T10-06-00Z_h0008_stuck_recovery2_markov_renewal_m7q4.md`

and the released canonical history is

`operations/claims/H0008.md`.

The six surviving regeneration obligations recorded there are:

1. a source-matching fresh-edge no-return regeneration event;
2. exact type-indexed reset laws `Q_i`;
3. a finite-state regeneration-type kernel `K` with true reset/independence;
4. a finite-mean roof in exit-ray generations;
5. a Markov-renewal/Rokhlin occupation law for the one-level harmonic shift;
6. equivalence to the source survival law plus the logarithmic integrability needed by the PF-KL identity.

R14 deliberately did **not** infer item 4 from a positive typewise escape probability, because the nested no-return events are not automatically independent or sequentially resolved. That caution is preserved below.

## 2. Dated source / literature check

Fresh bounded check on 2026-09-19:

- the current arXiv record for `2608.15987` remains the 17 August 2026 Kumar source;
- the later Kumar--Duddala companion `2608.21125` (21 August 2026) concerns the Bramson/front and continuous-type problems and does not advertise a solution of the finite-type harmonic-exit stationary law;
- Pierre Rousselin, arXiv:1711.07920, constructs an absolutely continuous invariant forward environment at exit times for a **one-type** Galton--Watson random-environment model using regeneration and ergodic theory;
- Serdar Altok's multitype unimodularity work gives finite-type reversible/unimodular measures for different rerooting kernels;
- bounded searches combining `multitype Galton-Watson`, `harmonic measure`, `regeneration`, `exit ray`, and `invariant measure` did not surface a paper stating the exact finite-type fresh-edge reset/tower result needed here.

This is negative search evidence only. **Novelty is UNVERIFIED.** The local Bayes/change-of-measure identities below should be treated as mathematical reductions, not a publication-priority claim.

## 3. Setting for the admission theorem

Work inside the finite-type Galton--Watson regime already isolated in the R14 handoff. Let the finite type set be `D`. For a fresh vertex of type `j`, let `P_j` denote the law of its unrevealed forward rooted subtree under the relevant survival-conditioned source law. We use the branching property in the standard deferred-revelation form: conditional on the type of a fresh child and on everything revealed outside that child's descendants, its forward subtree has law `P_j` and is independent of the revealed past.

After a simple random walk first crosses a fresh directed edge

`e = (parent(v), v)`, 

define

`B(T_v) = P_v( never cross e backwards | forward subtree T_v )`.

Thus `0 <= B <= 1`. On the surviving/transient type classes relevant to harmonic measure, assume

`B(T) > 0` for `P_j`-a.e. `T`,

and write

`b_j = E_{P_j}[B(T)] > 0`.

Let `R_e` be the event that, after the first crossing of `e`, the walk never crosses `e` backwards.

The key point is that `R_e`, once the edge has been crossed, is a property of the forward subtree and future walk randomness **before any return to the parent**. Siblings of `v` at the parent cannot be visited without first crossing `e` backwards, which is exactly the complement of `R_e`. This is the structural reason the sibling-conductance denominator from direct harmonic-child selection disappears at a genuine fresh-edge regeneration.

## 4. Method B2 — attack the negation: the exact fresh-edge reset law

### Theorem 4.1 (fresh-edge Palm/Bayes reset)

Conditional on the fresh child's type being `j`,

`P(R_e | type(v)=j) = b_j`,

and the conditional forward-subtree law at a successful fresh-edge regeneration is

`Q_j(dT) = [B(T)/b_j] P_j(dT)`.

If `B>0` `P_j`-a.s., then `Q_j` and `P_j` are mutually absolutely continuous.

### Proof

Let `A` be a measurable set of forward subtrees. By deferred revelation and the branching property, before the descendants of `v` are exposed we have `T_v ~ P_j`. Conditional on the realised forward subtree `T`, the probability of never crossing back to the parent is exactly `B(T)`. Therefore

`P(T_v in A, R_e | type(v)=j)`

`= integral_A P(R_e | T_v=T, type(v)=j) P_j(dT)`

`= integral_A B(T) P_j(dT)`.

Taking `A` equal to the whole subtree space gives

`P(R_e | type(v)=j) = integral B dP_j = b_j`.

Dividing the first identity by `b_j` gives

`P(T_v in A | R_e, type(v)=j)`

`= (1/b_j) integral_A B(T) P_j(dT)`,

which is exactly the claimed `Q_j`. If `B>0` `P_j`-a.s., then the Radon--Nikodym derivative `B/b_j` is strictly positive `P_j`-a.s., hence `Q_j ~ P_j`. QED.

### Why this is genuinely different from the failed direct harmonic-child chain

For direct harmonic-child selection at a branch point, the selected child is weighted by its conductance divided by a random sibling sum, so integrating siblings leaves a denominator bias. The fresh-edge event above is conditioned **after the walk has already crossed the chosen edge**. On the event of never returning, the walk never reaches the parent again; the parent's other children therefore play no role in the success probability. The exact reset density is `B/b_j`, not a sibling-normalized expression.

This discharges the algebraic content of R14 obligation C2 **conditional on having a source-matching fresh-edge regeneration construction C1**. It does not by itself prove the frequency or finite mean spacing of such regenerations.

## 5. Method B21 — import the Palm/spine change-of-measure idea: automatic block-start logarithmic integrability

The same exact reset density gives a useful integrability fact that was only a route note in the R14 handoff.

### Corollary 5.1

For every type `j` with `b_j>0`,

`E_{Q_j}[-log B] <= 1/(e b_j)`.

Consequently

`E_{Q_j}[ |log(dQ_j/dP_j)| ]`

`<= 1/(e b_j) + |log b_j| < infinity`.

### Proof

Since `dQ_j/dP_j = B/b_j`,

`E_{Q_j}[-log B]`

`= (1/b_j) E_{P_j}[ B(-log B) ]`.

For `x in (0,1]`, the elementary function `x(-log x)` is bounded above by `1/e`. Hence the first bound follows. Moreover

`log(dQ_j/dP_j)=log B-log b_j`,

so the triangle inequality gives

`E_{Q_j}|log(dQ_j/dP_j)|`

`<= E_{Q_j}[-log B] + |log b_j|`,

which is finite by the first estimate. QED.

This resolves the **block-start** logarithmic-integrability issue in C6 under the stated assumptions. It does not yet prove the needed integrability for every environment level inside a regeneration block.

## 6. Method B1 — change category: from the fixed-point equation to a Markov-renewal suspension

Assume now that C1 has been implemented: there is an infinite sequence of source-matching fresh-edge regeneration times. Let

- `J_k` be the type at regeneration `k`;
- `T_k` be the forward subtree rooted at that regeneration vertex;
- `H_k >= 1` be the number of **harmonic-descendant / exit-ray levels** from regeneration `k` to regeneration `k+1`;
- `E_{k,r}`, `0 <= r < H_k`, be the forward environment at the `r`-th one-level descendant shift inside the block.

### Proposition 6.1 (finite-type reset implies Markov-renewal structure)

Under the branching and strong-Markov properties, if the regeneration is defined by the fresh-edge no-return event above, then conditional on `J_k=j`,

`T_k ~ Q_j`

and is independent of the pre-regeneration history given `J_k`. Hence there is a finite-state kernel

`K_ij = P(J_{k+1}=j | J_k=i)`

such that successive regeneration blocks form a Markov-renewal process with state chain `J_k`.

### Proof

At a successful regeneration edge, Theorem 4.1 gives the exact conditional law `Q_j` of the fresh forward subtree given the endpoint type `j`. The event of success and all information before crossing the fresh edge involve no descendant information beyond the `B`-tilt already accounted for in `Q_j`. By the branching property, after conditioning on `J_k=j` and the successful fresh-edge event, the unrevealed descendants reset to `Q_j`; by the strong Markov property, future walk randomness is independent of the past. The law of the next block therefore depends on the past only through the present type `j` (and the fixed reset law `Q_j`). Marginalizing the next block defines `K`. QED.

This is the exact sense in which the reset can be finite-state without claiming that **direct harmonic-child selection** is finite-state.

### Proposition 6.2 (Rokhlin/renewal occupation law)

Assume additionally that `K` is irreducible, let `pi K=pi`, and assume the mean exit-level roof

`Hbar = sum_i pi_i E_{Q_i}[H]`

is finite. Then

`mu(A) = [sum_i pi_i E_{Q_i}[ sum_{r=0}^{H-1} 1{E_r in A} ]] / Hbar`

defines an invariant probability measure for the one-level harmonic-descendant shift `S`.

### Proof

Normalization is immediate from the definition of `Hbar`. For a bounded measurable test function `f`,

`int (f o S - f) dmu`

`= (1/Hbar) E_pi[ sum_{r=0}^{H-1} ( f(E_{r+1}) - f(E_r) ) ]`

`= (1/Hbar) E_pi[ f(E_H)-f(E_0) ]`.

Under the stationary regeneration chain, `E_H` is the start environment of the next regeneration block and has the same distribution as `E_0`; therefore the final expectation is zero. Thus `mu` is `S`-invariant. QED.

With the usual irreducibility/nonperiodicity hypotheses on the stationary regeneration-block chain, the standard regenerative argument also yields ergodicity. No such ergodicity claim is needed for the algebraic invariance identity above.

## 7. A rigorous one-sided equivalence consequence

Assume all surviving source types have positive source weight `q_j>0`, all stationary regeneration weights satisfy `pi_j>0`, and `Q_j ~ P_j` as in Theorem 4.1. Let

`Pbar = sum_j q_j P_j`

be the corresponding source mixture on forward environments.

Because the occupation sum contains the block-start term `r=0`,

`mu(A) >= (1/Hbar) sum_j pi_j Q_j(A)`.

Therefore

`Pbar << mu`.

Indeed, if `mu(A)=0`, then `Q_j(A)=0` for every `j` with `pi_j>0`; equivalence gives `P_j(A)=0` for each surviving type, hence `Pbar(A)=0`.

The reverse direction `mu << Pbar` is **not** claimed automatically. It requires control of the laws of the intermediate environments `E_{k,r}` inside failed/unfinished regeneration blocks. This is one of the precise pieces that remains in C6.

## 8. What is still genuinely unproved

This note does **not** close H0008 and does not move any R7-07 source metric. The hard pieces that remain are now more sharply separated.

### C1 remains a source-matching construction issue

The local fresh-edge event is exact, but one still has to construct the regeneration sequence for the same simple random walk/harmonic ray in the source setting and prove that it is infinite almost surely under the relevant survival/transience assumptions.

### C4 remains the main recurrence/roof obstruction

Let `b_* = min_j b_j`. It is tempting to argue that `b_*>0` gives a geometric roof. That inference is **not justified merely from the one-step marginals**. Fresh-edge no-return events encountered at nested depths can share future path information; an earlier candidate's failure need not be resolved before a deeper candidate is exposed. In abstract probability, events can each have marginal success probability at least `b_*` while being maximally dependent, so no product tail follows without an actual sequential regeneration/deferred-decision argument.

Thus R14's refusal to promote

`P(H>m) <= (1-b_*)^m`

from positivity alone was mathematically correct. A future proof needs either a true sequence of resolved trials, a Lyapunov/renewal estimate, or a direct bound on the exit-level cut-time gaps.

### C6 is only partially reduced

The exact reset law gives `Q_j~P_j` and finite block-start logarithmic density, and the tower gives `Pbar<<mu`. Still needed are:

- `mu<<Pbar` for all within-block environments;
- logarithmic integrability of the PF--KL observables under the full occupation law, not only at block starts;
- identification of the tower law with the harmonic-descendant stationary law entering R14's exact transfer equation.

These are honest remaining gaps.

## 9. Admission assessment

Mathematically, H0008 is **more sharply feasible than the terminal handoff alone showed**: the sibling-denominator obstruction does disappear exactly at a fresh-edge regeneration; the reset law is the simple `B`-Palm tilt; the block-start entropy/log terms are automatically integrable; and, once a finite-mean regeneration roof exists, the desired invariant one-level environment law is the standard stationary suspension with an elementary telescoping proof.

Operationally, none of this authorizes R7-07 to acquire H0008. The canonical path already exists and the R7-07 rule is create-only. The collision was reread at fresh master and therefore skipped. No `operations/claims/H0008.md` write was attempted.

The R7-07 state remains:

`PENDING_ADMISSION`.

No successor metric is inherited from F0012 or R14; the R7-07 source metric remains `UNMEASURED -> UNMEASURED`, and there is no stagnation count to increment.

## 10. Method outcomes

- **B2 — ATTACK THE NEGATION FIRST:** attacked the reason R14 rejected a type-only harmonic-child chain. At a genuine fresh-edge no-return event, the sibling denominator vanishes exactly and the reset law is `Q_j=(B/b_j)P_j`. **Substantive exact lemma proved.**
- **B1 — CHANGE THE CATEGORY:** replaced direct infinite-dimensional fixed-point iteration by a finite-state Markov-renewal suspension. Conditional on C1 and finite mean roof, the occupation law is rigorously invariant; one direction of source equivalence follows from the block-start mass. **Substantive conditional theorem proved.**
- **B21 — IMPORT AN ANALOGOUS TECHNIQUE:** used the Palm/spine measure-change shape from one-type regeneration theory to obtain an explicit logarithmic-integrability bound `E_Q[-log B] <= 1/(e b_j)`. **Substantive exact bound proved.**

No checker is appropriate: these are symbolic measure-theoretic identities, and the unresolved part is probabilistic recurrence/absolute-continuity rather than a finite arithmetic certificate.

## 11. Next admission action

First inspect fresh master for either:

1. a genuinely new populated shard-6 canonical source row beyond the currently evidenced frontier, or
2. an explicit owner/coordinator reassignment mechanism that creates a lawful R7-07-exclusive acquisition without overwriting the preserved H0008 history.

Absent such a delta, do not silently resume R14's H0008 programme and do not repeat I0106. The most useful next bounded H0008 feasibility question, only if admission work is again necessary, is C4: prove or refute a finite-mean **exit-level** regeneration roof using a true resolved-trial or cut-level argument, not the invalid marginal-probability product shortcut.