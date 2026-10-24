Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: one-shot independent zero-break thinning is impossible; conflict-free correlated batches are the next constructive object

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with three distinct variables and independent uniform signs**  
Status: **OPEN / PARTIAL**

## 0. Source-level bracket before / after

For the exact fixed-count proper iid model with `m=floor(alpha n)`, the externally literature-supported explicit-decimal theorem bracket remains

\[
\boxed{3.52\le \alpha_{3\mathrm{SAT}}\le 4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52`; Diaz--Kirousis--Mitsche--Perez-Gimenez prove a.a.s. unsatisfiability at `4.4898`. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis (CPC 2026) still describe fixed small `k`, including `k=3`, as unresolved, while explaining that interpolation gives a rigorous 1RSB variational upper mechanism. Their physics table lists `d_sat(3)≈12.801`, i.e. `alpha≈4.267`, but this worker has not reconstructed an independent interval-certified evaluation of the full variational functional at that decimal.

Therefore this run's externally certified source metric is

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

Separately, companion NM13-13 has an immutable **CANDIDATE_FULL pending independent review** upper-bound report at `4.39539`, so the current project-candidate bracket is `[3.52,4.39539]`. I do not relabel that peer candidate as externally certified here, and this run does not improve it.

## 1. Compact handoff and why this run changes method

Recent NM13-06 constructive work produced several real mechanism results but no threshold endpoint movement:

1. the four-parameter degree / unit-propagation route produced an exact local polarity index and then a branching-ratio barrier controller, but no certified full density evolution;
2. the majority two-choice repair route proved the local repair genealogy subcritical even near the old UNSAT endpoint, so local branching is not the obstruction;
3. the static blocked-majority hypergraph was proved subcritical through `alpha=4.4898`, so a static percolating blocked core is not the obstruction;
4. the remaining failure mechanism was dynamic promotion: safe zero-break variables are depleted/promoted when flips are made at positive density.

Because the source endpoint has stayed unchanged across these substantive runs, this run does **not** add another ODE tweak. It executes a materially different attack: classify an entire natural family of one-shot randomized zero-break algorithms and prove a no-go theorem for all of them. The same derivation then identifies the missing ingredient exactly: **negative correlation between simultaneously chosen repairs**. I give a deterministic conflict-graph lemma that produces safe correlated batches and becomes the next constructive object.

Historical parked routes remain parked: one-variable cavity iteration, fractional solution-count martingales, randomized booster/helper replacement, loose-hypertree cavity, positive-temperature compactification, and the unclosed full four-spectrum ODE. NM13-13 remains on cluster-aware / interpolation counting; this report is constructive and does not duplicate that route.

## 2. Majority local limit

Let the initial assignment `sigma^0` set each variable to its majority sign; ties are broken by an independent fair coin. In the local weak limit,

\[
P,N\stackrel{\rm iid}{\sim}\operatorname{Pois}(\mu),
\qquad \mu=\frac{3\alpha}{2},
\]

where `P,N` are the two sign degrees. Put

\[
Z=\min(P,N),\qquad M=\max(P,N).
\]

Thus `Z` occurrences of the variable are false and `M` are true under `sigma^0`. The false-literal occurrence fraction is

\[
q=\frac{\mathbb EZ}{2\mu}
=\frac12\left[1-e^{-2\mu}\{I_0(2\mu)+I_1(2\mu)\}\right].
\tag{2.1}
\]

A true occurrence is **critical** if the other two literals in its clause are false under `sigma^0`. On the factor-tree limit this has probability `q^2`. Let `B_v` be the number of critical true occurrences of variable `v`; a variable is **zero-break** if `B_v=0`.

## 3. The algorithm class being ruled out

Fix any deterministic kernel

\[
\theta_{z,m}\in[0,1],\qquad 0\le z\le m.
\]

A **one-shot independent zero-break thinning** does the following:

- compute the majority assignment and all initial zero-break variables;
- for each zero-break variable of type `(Z,M)=(z,m)`, flip it independently with probability `theta_{z,m}`;
- never flip a variable with positive initial break count.

The kernel may depend on `alpha` and on the complete pair `(z,m)`; it is otherwise arbitrary. This contains the uniform-thinning idea and every degree-type biased independent one-shot version of it.

The point of the theorem below is not that independence is a good algorithm. It proves that **independence itself is the obstruction**.

## 4. Exact residual-clause law

Consider a uniformly sampled clause in the local factor-tree limit. Define

\[
a=
\frac{\mathbb E\big[Z\theta_{Z,M}(1-q^2)^M\big]}{\mathbb EZ},
\tag{4.1}
\]

and

\[
b=
\frac{\mathbb E\big[M\theta_{Z,M}(1-q^2)^{M-1}\big]}{\mathbb EM}.
\tag{4.2}
\]

Interpretation:

- `a` is the probability that the variable reached through an initially false occurrence is selected for flipping;
- `b` is the corresponding cavity probability through an initially true occurrence of a clause that was **not** initially critical for that variable.

The exponent differs by one because a false focal occurrence does not participate in the break count, while a true focal occurrence in a clause having at least two true literals is known not to be critical and is removed from the `M` potential critical locations.

Let `j` be the number of literals initially true in the focal clause.

- `j=0`: the clause remains unsatisfied iff none of its three false variables is selected, probability `(1-a)^3`.
- `j=1`: the unique true variable has this clause itself as a critical clause, hence is **not** zero-break and cannot be selected. Therefore such a clause cannot become unsatisfied.
- `j=2`: the clause becomes unsatisfied iff both true variables are selected and the one false variable is not, probability `b^2(1-a)`.
- `j=3`: it becomes unsatisfied iff all three true variables are selected, probability `b^3`.

Since the initial truth pattern is asymptotically `Bin(3,1-q)`, the exact residual unsatisfied-clause density per clause is

\[
\boxed{
U(a,b)=
q^3(1-a)^3
+3q(1-q)^2b^2(1-a)
+(1-q)^3b^3.
}
\tag{4.3}
\]

For every fixed kernel, standard marked local weak convergence gives convergence of the empirical residual bad-clause density to `U(a,b)`. A direct finite-graph proof follows by truncating variable degree at a fixed `D`, applying bounded differences to the radius-two marked statistic, and then sending `D\to\infty`; the Poisson tail controls the discarded density. Thus any strictly positive lower bound on `U` becomes a linear w.h.p. residual obstruction.

## 5. The key ratio inequality

The majority imbalance `M>=Z` forces a relation between the benefit `a` and the risk `b`. Since

\[
\mathbb EZ=2\mu q,
\qquad
\mathbb EM=2\mu(1-q),
\]

for every type with `M>0`,

\[
\frac{Z(1-q^2)^M/\mathbb EZ}
     {M(1-q^2)^{M-1}/\mathbb EM}
=
\frac ZM\,(1-q^2)\frac{1-q}{q}
\le
(1-q^2)\frac{1-q}{q}.
\]

Multiplying by the nonnegative `theta_{Z,M}` and summing gives

\[
\boxed{
a\le R(q)b,\qquad
R(q)=\frac{(1-q)(1-q^2)}{q}.}
\tag{5.1}
\]

This is the exact tradeoff missing from the earlier independent-thinning intuition: a rule that selects more variables through false incidences necessarily selects them through enough true incidences to create a positive density of `j=2` and `j=3` failures.

## 6. Theorem — every independent zero-break thinning leaves linearly many bad clauses

### Theorem 6.1

For every fixed `alpha>0` and every kernel `theta_{z,m}`, the one-shot independent zero-break thinning above leaves, in the proper iid random 3-SAT model,

\[
\left(L(q)+o_p(1)\right)m
\]

or more unsatisfied clauses, where

\[
\boxed{
L(q)=
\frac{q^3}
{\left[1+(1-q^2)^{3/2}\right]^2}>0.
}
\tag{6.1}
\]

Consequently **no member of this entire one-shot independent family can be a satisfiability algorithm at any fixed positive clause density**, regardless of how the degree-type retention probabilities are optimized.

### Proof

From (4.3), discard the nonnegative middle term:

\[
U(a,b)\ge q^3(1-a)^3+(1-q)^3b^3.
\tag{6.2}
\]

Because the first term decreases in `a`, (5.1) implies that for `R(q)b\le1`, with `x=R(q)b`,

\[
U(a,b)
\ge q^3(1-x)^3+rac{(1-q)^3}{R(q)^3}x^3.
\tag{6.3}
\]

But

\[
\frac{(1-q)^3}{R(q)^3}
=
\frac{q^3}{(1-q^2)^3}.
\tag{6.4}
\]

For positive `A,B`,

\[
\min_{0\le x\le1}\{A(1-x)^3+Bx^3\}
=
\frac{AB}{(\sqrt A+\sqrt B)^2}.
\tag{6.5}
\]

Substituting

\[
A=q^3,
\qquad
B=\frac{q^3}{(1-q^2)^3}
\]

into (6.5) gives exactly (6.1).

If `R(q)b>1`, then the second term in (6.2) alone is at least

\[
(1-q)^3R(q)^{-3}
=\frac{q^3}{(1-q^2)^3}>L(q),
\]

so the same lower bound holds. The local-limit / truncation concentration argument following (4.3) upgrades the deterministic limit inequality to the finite proper model. QED.

### Numerical scale

The theorem is symbolic and does not depend on floating-point certification. The executed high-precision diagnostic gives:

| alpha | q | universal residual lower `L(q)` per clause | lower residual clauses per variable `alpha L(q)` |
|---:|---:|---:|---:|
| 3.52 | 0.378714713369405 | 0.0168999915581041 | 0.0594879702845266 |
| 3.60 | 0.380036729791158 | 0.0171041468894677 | **0.0615749288020838** |
| 4.00 | 0.386054739748189 | 0.0180581924731612 | 0.0722327698926450 |
| 4.39539 | 0.391194219181242 | 0.0189058235241936 | 0.0830984676600055 |
| 4.4898 | 0.392321936451922 | 0.0190959611366054 | 0.0857370463111309 |

For the much narrower uniform kernel `theta_{z,m}=theta`, direct optimization at `alpha=3.6` gives `theta*=0.352313...` and residual density `U=0.0450788...` per clause, well above the universal lower bound. These numbers are diagnostics; the theorem is the closed-form inequality above.

Executed artifact:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__zero_break_thinning_eval.py`

Archived output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__zero_break_thinning_eval.out`

## 7. Positive counterpart — a deterministic correlated safe-batch lemma

The no-go theorem identifies exactly what must replace independent thinning: chosen repairs must be negatively correlated on clauses containing multiple currently true literals.

For an arbitrary current assignment, call a variable **zero-break** if it is not the unique true literal of any currently satisfied clause. Form a conflict graph on the zero-break variables by joining `u,v` whenever some currently satisfied clause contains both `u` and `v` as true literals.

### Lemma 7.1

If `S` is an independent set in this conflict graph, then flipping all variables of `S` simultaneously creates **no new unsatisfied clause**. Every currently unsatisfied clause meeting `S` becomes satisfied.

### Proof

Take a currently satisfied clause.

- If it has exactly one true literal, that variable has positive break count by definition, so it is not in the zero-break vertex set and cannot be flipped.
- If it has two true literals, the two true variables are adjacent in the conflict graph, so independence allows at most one to be flipped; at least one true literal remains.
- If it has three true literals, every pair of its variables is adjacent, so again at most one is flipped and at least two true literals remain.

Flipping a currently false literal can only help that clause. Hence no satisfied clause is destroyed. A currently unsatisfied clause has all literals false, so if it meets `S`, at least one literal becomes true. QED.

This lemma is qualitatively different from the independent family ruled out above: the dangerous `b^2` and `b^3` simultaneous-selection events are deleted **combinatorially**, not merely made small.

There is also a crude positive-density packing certificate. Call a zero-break variable **useful** if it lies through a false occurrence in at least one initially unsatisfied clause. On the tree limit its density is

\[
p_{\rm use}
=
\mathbb E\left[(1-q^2)^M\{1-(1-q^2)^Z\}\right].
\tag{7.1}
\]

Build a stronger packing graph on useful variables by joining any two that share any clause. Its degree at `v` is at most twice the total occurrence degree `D_v=Z_v+M_v`. Therefore Caro--Wei / the greedy bound gives asymptotically a packing of density at least

\[
\boxed{
c_{\rm safe}
\ge
\frac{p_{\rm use}}
{1+2\,\mathbb E[D\mid \mathrm{useful}]}.}
\tag{7.2}
\]

No two variables in such a packing share a clause, so their simultaneous flips create no new bad clause, and each selected useful variable repairs at least one **distinct** initially unsatisfied clause.

The executed diagnostic gives at `alpha=3.6`

\[
p_{\rm use}\approx0.1601033,
\qquad
\mathbb E[D\mid\mathrm{useful}]\approx10.76683,
\]

and hence the conservative explicit batch size

\[
\boxed{c_{\rm safe}\approx0.00710508}
\]

variables per original variable, safely removing at least that many distinct unsatisfied clauses in one batch. This is only about `3.60%` of the initial majority-unsatisfied clause density, so it is **not** a threshold proof. Its role is structural: correlations can provably evade the independent-thinning obstruction without paying new unsatisfied clauses.

Executed artifact:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__safe_batch_eval.py`

Archived output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__safe_batch_eval.out`

## 8. What failed, what is proved, and the next attack

**Proved this run:**

- exact local residual law (4.3) for every degree-type independent one-shot thinning of initial zero-break variables;
- exact benefit/risk inequality `a<=R(q)b`;
- the closed-form no-go bound `U>=L(q)>0`, hence a linear residual w.h.p. for every such kernel;
- deterministic conflict-free safe-batch Lemma 7.1;
- a positive-density one-batch packing lower bound (7.2).

**Failed / retired:** one-shot independent zero-break thinning, including arbitrary optimization over `(Z,M)`-dependent retention probabilities. It cannot yield satisfiability and should not receive another tuning run.

**Not proved:** a lower-bound improvement above `3.52`; convergence of a multi-round correlated repair process; a global independent transversal that hits every bad clause; or any improvement to the peer candidate upper `4.39539`.

The next constructive attack is now forced and materially narrower: combine subcritical two-choice repair trees with the conflict graph and prove a **correlated independent-transversal theorem**. The first target remains `alpha=3.6`: associate to each unsatisfied root a finite menu of terminating repair trees, put an incompatibility edge between menus whose selected variables share a dangerous true clause, and prove that one compatible tree can be selected for every root (or expose the precise Hall/LLL obstruction). If the required transversal fails already in the local limit, retire the majority-repair family entirely rather than returning to an ODE closure.

## 9. ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  parent: T04
  status: OPEN_PARTIAL
  exact_model: fixed-count proper iid random 3-SAT, three distinct variables, independent uniform signs
  literature_explicit_bracket_before: [3.52, 4.4898]
  literature_explicit_bracket_after: [3.52, 4.4898]
  literature_width_before: 0.9698
  literature_width_after: 0.9698
  project_candidate_upper_from_NM13-13: 4.39539
  project_candidate_review_state: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  source_endpoint_movement_this_run: false
  mechanism_gain:
    - exact residual law for arbitrary degree-type independent zero-break thinning
    - universal no-go U >= q^3/[1+(1-q^2)^(3/2)]^2 > 0
    - deterministic conflict-free correlated safe-batch lemma
    - conservative positive-density safe packing certificate
  retired_route: one-shot independent zero-break thinning, including arbitrary theta_(Z,M)
  alpha_3_6_universal_residual_lower_per_variable: 0.0615749288020838
  alpha_3_6_safe_batch_density_diagnostic: 0.00710507700906051
  next_attack: correlated independent transversal over finite repair-tree menus at alpha=3.6
  companion_nonduplication: NM13-13 remains on cluster-aware/interpolation upper bounds; this run is constructive repair geometry
  artifacts:
    zero_break_code: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__zero_break_thinning_eval.py
    zero_break_output: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__zero_break_thinning_eval.out
    safe_batch_code: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__safe_batch_eval.py
    safe_batch_output: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T07-23-15__safe_batch_eval.out
```
