Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: repair menus are doubly-exponentially complete locally; raw variable capacity is not the remaining obstruction

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with three distinct variables and independent uniform signs**  
Status: **OPEN / PARTIAL**

## 0. Source-level bracket before / after

For the exact proper iid model with `m=floor(alpha n)`, the externally literature-supported explicit-decimal theorem bracket remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le 4.4898}.
\]

Hajiaghayi--Sorkin prove the constructive lower endpoint `3.52`; Diaz--Kirousis--Mitsche--Perez-Gimenez prove a.a.s. UNSAT at `4.4898`. The 27 March 2026 Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis paper still states that exact fixed-small-`k` satisfiability thresholds are unresolved; its table records the physics `d_sat(3)≈12.801` (`alpha≈4.267`) but this worker has not independently interval-certified the full rigorous interpolation functional at that decimal.

Therefore the **externally certified source metric** is unchanged:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

Separately, companion NM13-13 has now advanced its own interpolation route from the previous `4.39539` candidate to an explicit **CANDIDATE_FULL pending independent review** endpoint `4.3911`. Thus the current project-candidate bracket is `[3.52,4.3911]`, width `0.8711`. I do **not** promote that peer candidate into the externally verified metric in this report.

No source-threshold endpoint is improved by the present run.

## 1. Compact handoff: what has already failed or been isolated

The constructive line has produced real structural information without an endpoint gain:

1. the four-parameter degree / unit-propagation calculation gave an exact local polarity index and then an exact branching-ratio barrier controller, but no closed global density evolution;
2. majority-start two-choice repair proved the local repair genealogy subcritical (`r_2<1`) even near `4.4898`, so ordinary local branching is not the obstruction;
3. the static blocked-majority hypergraph was proved subcritical through `4.4898`, so there is no initial giant blocked core causing the `3.52` barrier;
4. the promotion calculation showed that repeated safe-looking flips dynamically consume/promote the zero-break reservoir;
5. the previous run then proved a universal no-go theorem for **all one-shot independent degree-type zero-break thinnings**, while a correlated conflict-free batch can evade that no-go.

Historical parked routes remain parked: one-variable cavity iteration, fractional solution-count martingales, randomized booster/helper replacement, loose-hypertree cavity, positive-temperature compactification, and an unclosed full four-spectrum ODE. NM13-13 remains on cluster/interpolation counting; this run stays on constructive repair geometry.

The previous report left one sharply defined question: does a typical unsatisfied root even possess enough finite repair-tree **menus** for an independent-transversal / Haxell-type global selection to be plausible? This run answers the local-availability and raw-capacity parts rigorously. The answer is surprisingly favorable; the unresolved obstruction is now genuinely global compatibility.

## 2. Majority Palm law and the exact repair-menu recursion

Let the initial assignment set each variable to its majority sign, with independent fair tie-breaking. In the local weak limit,

\[
P,N\stackrel{\rm iid}{\sim}{\rm Pois}(\mu),
\qquad \mu=\frac{3\alpha}{2},
\]

and put

\[
Z=\min(P,N),\qquad M=\max(P,N),\qquad
q=\frac{\mathbb EZ}{2\mu}.
\]

A variable reached through an occurrence that is false under the majority assignment has Palm law

\[
\Pr\{(P,N)=(p,n)\mid F\}
=\frac{\min(p,n)\,\pi_\mu(p)\pi_\mu(n)}{\mathbb EZ}.
\tag{2.1}
\]

If this variable is flipped, each of its `M` originally true occurrences becomes a broken clause exactly when the other two literals were false. Hence on the collision-free factor-tree limit

\[
B\mid(P,N)\sim {\rm Bin}(M,q^2).
\tag{2.2}
\]

A false-Palm variable is **depth-0 repairable** when `B=0`. Recursively, it is depth-`d+1` repairable when, for every one of its `B` break clauses, at least one of the two fresh nonparent false-Palm variables in that clause is depth-`d` repairable.

Let

\[
p_d=\Pr\{\text{a false-Palm variable is depth-}d\text{ repairable}\},
\qquad y_d=1-p_d.
\]

Because the two child candidates are independent on the factor tree,

\[
\boxed{
 p_0=\Pr(B=0),
 \qquad
 p_{d+1}=\mathbb E\big[(2p_d-p_d^2)^B\big].
}
\tag{2.3}
\]

Equivalently, since `B|M~Bin(M,q^2)`,

\[
\boxed{
 y_{d+1}=\mathbb E_F\left[1-(1-q^2y_d^2)^M\right].
}
\tag{2.4}
\]

This recursion is different from the earlier single greedy-tree Galton--Watson calculation: (2.3) keeps the **whole two-choice menu** at every repair obligation rather than selecting one child immediately.

## 3. Theorem — repair-menu failure decays doubly exponentially

Define

\[
r_1:=\mathbb E_F B.
\]

The identity `ZM=PN` and independence of `P,N` give

\[
\mathbb E_F M=\frac{\mathbb E[ZM]}{\mathbb EZ}
=\frac{\mu^2}{2\mu q}=\frac{\mu}{2q},
\]

so

\[
\boxed{r_1=q^2\mathbb E_FM=\frac{\mu q}{2}=\frac{3\alpha q}{4}.}
\tag{3.1}
\]

### Theorem 3.1 — quadratic menu contraction

For every `d>=0`,

\[
\boxed{y_{d+1}\le r_1y_d^2.}
\tag{3.2}
\]

Consequently, if

\[
\boxed{c:=r_1y_0<1,}
\tag{3.3}
\]

then

\[
\boxed{
 y_d\le \frac{c^{2^d}}{r_1}.
}
\tag{3.4}
\]

For an initially unsatisfied clause, whose three variables are iid false-Palm candidates on the factor-tree limit, the probability that **none** of the three admits a depth-`d` repair tree is at most

\[
\boxed{
 f_d\le y_d^3\le r_1^{-3}c^{3\cdot2^d}.
}
\tag{3.5}
\]

Thus whenever `c<1`, finite repair menus become complete at a double-exponential rate in depth.

### Proof

From (2.4) and the elementary inequality `1-(1-x)^M <= Mx` for `x in [0,1]`,

\[
y_{d+1}
\le q^2\mathbb E_F[M]y_d^2
=r_1y_d^2,
\]

which is (3.2). Since `y_0=c/r_1`, induction gives

\[
y_d\le r_1^{-1}c^{2^d}:
\]

if it holds at `d`, then

\[
y_{d+1}\le r_1(r_1^{-1}c^{2^d})^2
=r_1^{-1}c^{2^{d+1}}.
\]

Finally an unsatisfied root clause presents three fresh false-Palm candidates; all three must fail for the root to have no depth-`d` repair tree, giving (3.5). QED.

## 4. Certified scale at alpha=3.6

The new outward-interval checker uses `K=55`, `mpmath.iv.dps=60`, and analytic Chernoff bounds for the omitted Poisson/Palm tails. At `alpha=3.6` it certifies

\[
q\in[0.380036729791158,0.380036729791158],
\]

\[
p_0\ge0.346665436124719,
\qquad
r_1\le1.026099170436126,
\]

and therefore

\[
\boxed{c=r_1(1-p_0)\le0.670386054009674<1.}
\tag{4.1}
\]

The simple theorem bound already yields

\[
\Pr(\text{root has no depth-4 menu})\le4.266\times10^{-9},
\]

\[
\boxed{
\Pr(\text{root has no depth-5 menu})\le1.966\times10^{-17}.
}
\tag{4.2}
\]

These are conservative bounds from (3.5), not Monte Carlo estimates. The exact recursion is smaller still; I retain only the proved upper bound.

The same checker finds `c<1` at the five benchmark densities `3.52, 3.6, 4.0, 4.3911, 4.4898`; at the old explicit UNSAT endpoint the margin is small but still certified:

\[
c(4.4898)\le0.984023179674328<1.
\]

I do **not** infer satisfiability there: this is only a local repair-menu statement, and `4.4898` is rigorously UNSAT globally.

## 5. Finite-model consequence — all but subpolynomially many roots have an individual shallow menu

The double-exponential estimate has a useful finite consequence that was absent from the earlier repair-tree report.

### Proposition 5.1 — individual near-cover by shallow repair menus

Fix a density `alpha` for which `c(alpha)<1`; in particular this applies at `alpha=3.6`. For every fixed `epsilon>0`, there is a depth

\[
d_n=O(\log\log n)
\]

such that in the proper iid random 3-SAT formula, with high probability, **all but at most `n^epsilon` initially majority-unsatisfied clauses individually admit a collision-free depth-`d_n` repair tree**.

This is an individual-existence statement. It does not assert that the trees can be chosen simultaneously.

### Proof

Choose, for example,

\[
2^{d_n}\ge \frac{2\log n}{-\log c}.
\tag{5.1}
\]

Then (3.5) gives, on the limiting tree law,

\[
f_{d_n}
\le r_1^{-3}c^{3\cdot2^{d_n}}
\le C_\alpha n^{-6}
\tag{5.2}
\]

for a fixed constant `C_alpha`.

Now expose the signed factor neighborhood of a uniformly chosen clause to repair depth `d_n`. Clause degree is exactly three and the variable excess degree has all exponential moments. The expected number of nonbacktracking exposure paths of length `O(d_n)` is therefore at most

\[
C^{d_n}=(\log n)^{O(1)}.
\]

During a configuration-style exposure, two frontier half-edges collide with probability `O(1/n)` per ordered pair. Hence the probability that this radius-`O(d_n)` neighborhood is not a tree is

\[
\frac{(\log n)^{O(1)}}{n}.
\tag{5.3}
\]

The same exposure couples the finite binomial degree law to the Poisson Palm law with an error of this order because only polylogarithmically many half-edges are revealed. Combining (5.2)--(5.3), the expected number of initially unsatisfied root clauses that either see a collision/coupling defect or lack a depth-`d_n` repair tree is `(log n)^{O(1)}`. Markov's inequality then makes this number at most `n^epsilon` with probability tending to one, for every fixed `epsilon>0`. QED.

This proposition is not a satisfiability algorithm because the individually valid trees can overlap one another and can destroy each other's break-count assumptions if chosen simultaneously. It does, however, remove **local menu nonexistence** as the obstruction at `3.6`.

## 6. Second theorem-level gain — raw variable capacity has large slack

There is a distinct possible obstruction: perhaps even if every root has a menu, the total number of variable slots demanded by reasonable repair trees exceeds `n` before compatibility is considered. The earlier `r_2` calculation lets us test this exactly.

Let `B_1,B_2,B_3` be iid copies of the false-Palm break count and define

\[
Y_2=\min(B_1,B_2),
\qquad
Y_3=\min(B_1,B_2,B_3).
\]

Then

\[
r_2:=\mathbb EY_2=\sum_{t\ge1}\Pr(B\ge t)^2,
\qquad
r_3:=\mathbb EY_3=\sum_{t\ge1}\Pr(B\ge t)^3.
\tag{6.1}
\]

For the greedy minimum-break tree, every nonroot vertex has offspring law `Y_2`, while the root has offspring law `Y_3`. Therefore, whenever `r_2<1`, its expected number of flipped variables is exactly

\[
\boxed{
S_{\rm root}=1+\frac{r_3}{1-r_2}.
}
\tag{6.2}
\]

This follows by conditioning on the root offspring: each child begins an iid Galton--Watson subtree of mean total progeny `1/(1-r_2)`.

At `alpha=3.6`, the checker certifies

\[
r_2\le0.508148367896451,
\qquad
r_3\le0.299808316800522,
\]

hence

\[
\boxed{S_{\rm root}\le1.609550314021127.}
\tag{6.3}
\]

The initial majority-unsatisfied clause density satisfies

\[
u_0=\alpha q^3\le0.197596486380699.
\]

Thus the **fresh-copy Palm demand density** obtained by giving every unsatisfied root an independent greedy repair tree obeys

\[
\boxed{
\ell_{\rm Palm}:=u_0S_{\rm root}
\le0.318041486703526<1.
}
\tag{6.4}
\]

Even at `alpha=4.4898`, the same certificate gives `ell_Palm<=0.735192694214709<1`.

Equation (6.4) is deliberately not called a packing theorem: different roots in the real formula reuse variables and clauses. What it proves is that the global obstruction is **not a first-moment shortage of variable slots** in the fresh-copy repair-tree model. At the first target `alpha=3.6`, there is roughly `0.682 n` slots of raw capacity slack before overlap constraints are imposed.

## 7. What this run changes mathematically

Before this run, the repair route knew only that one greedily chosen local genealogy was subcritical. That left two very different possibilities unresolved:

- perhaps a positive density of roots simply had **no** finite repair alternative at all; or
- perhaps menus were abundant but could not be selected globally without collisions.

Theorem 3.1 and Proposition 5.1 separate those possibilities. At `alpha=3.6`, local menu failure contracts quadratically and all but subpolynomially many initial bad clauses individually possess a shallow repair tree. Equation (6.4) further shows that the expected raw variable demand of one greedy tree per root is only `0.3181 n` in the fresh-copy model.

So the remaining obstruction is now sharply global:

\[
\boxed{\text{compatible repair-tree transversal / Hall expansion under shared clauses and shared variables}.}
\]

That is a more informative target than another scalar ODE or another one-shot thinning parameter.

## 8. What is not proved

This run does **not** prove:

- satisfiability at `alpha=3.6` or any lower-bound improvement above `3.52`;
- simultaneous compatibility of the individual repair trees;
- a Hall/Haxell condition for the repair-tree menu hypergraph;
- preservation of the majority Palm law after a positive density of actual flips;
- the NM13-13 candidate upper `4.3911` independently;
- convergence of the fixed-`k=3` threshold sequence.

The finite near-cover theorem is about individual menus before global selection. The Palm load statistic is a proved tree-model expectation with rigorous numeric upper bounds, but it is not a finite-formula matching certificate.

## 9. Next decisive attack

The next run should not return to independent thinning or to a full-spectrum ODE. At `alpha=3.6`, expose repair menus only to depth `3`--`5`, truncate exceptionally high variable degrees, and build the finite **menu conflict hypergraph**:

- left parts = initially unsatisfied root clauses;
- vertices in a left part = bounded repair trees for that root;
- incompatibility = shared flipped variable, shared repair clause, or a satisfied clause whose support would be jointly destroyed.

The proof target is a Haxell/LLL-style independent transversal after deleting the `n^{o(1)}` collision-exception roots from Proposition 5.1, followed by a separate absorber for those exceptions. The numerical facts proved here (`f_5<2e-17`, `ell_Palm<0.319`) give this attack genuine room. If the truncated menu conflict graph violates the necessary Hall expansion already at `alpha=3.6`, that is a decisive obstruction and the majority-repair family should be retired rather than tuned again.

## 10. Artifacts

Executed outward-interval checker:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T08-29-06__repair_menu_certificate.py`

creation commit: `ed0e896beee19adcb7b22f81137c9808919e2505`

Archived executed output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T08-29-06__repair_menu_certificate.out`

creation commit: `cd19ec3238611932e355448ad5a570bddda8b509`

The checker certifies all displayed inequalities using outward interval arithmetic and analytic Poisson-tail bounds; no simulation or replica assumption enters Theorems 3.1, 5.1, or the tree-demand calculation.

## 11. ledger_delta

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
  source_endpoint_movement_this_run: false
  project_candidate_upper_from_NM13-13: 4.3911
  project_candidate_review_state: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  mechanism_gain:
    - exact repair-menu recursion p_(d+1)=E[(2p_d-p_d^2)^B]
    - quadratic failure contraction y_(d+1)<=r1*y_d^2
    - alpha=3.6 certificate c=r1*y0<=0.670386054009674<1
    - alpha=3.6 depth-5 root no-menu probability <=1.966e-17
    - finite near-cover: all but n^epsilon initial bad roots individually have depth O(log log n) collision-free repair trees w.h.p.
    - greedy-tree Palm demand density <=0.318041486703526 at alpha=3.6
  demonstrated_but_not_threshold_gain: true
  retired_or_failed_routes_preserved:
    - full four-spectrum ODE remains unclosed
    - static blocked-core explanation rejected
    - one-shot independent zero-break thinning proved impossible
    - local ordinary branching not the obstruction
  remaining_obstruction: global compatible repair-tree transversal / Hall expansion under shared variables and dangerous satisfied clauses
  next_attack: bounded-depth menu conflict hypergraph at alpha=3.6; prove Haxell/LLL/Hall expansion or expose a decisive obstruction
  companion_nonduplication: NM13-13 remains on cluster-aware interpolation upper bounds; this run is constructive repair-menu geometry
  artifacts:
    code: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T08-29-06__repair_menu_certificate.py
    code_commit: ed0e896beee19adcb7b22f81137c9808919e2505
    output: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T08-29-06__repair_menu_certificate.out
    output_commit: cd19ec3238611932e355448ad5a570bddda8b509
```
