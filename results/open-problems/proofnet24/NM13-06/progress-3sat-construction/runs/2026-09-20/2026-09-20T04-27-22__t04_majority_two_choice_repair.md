Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 constructive random 3-SAT: majority start + nonbacktracking two-choice repair

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT, constructive lower-bound route**  
Status: **OPEN / PARTIAL**

## 0. Source-level threshold metric before / after

Freeze the source model exactly: `m=floor(alpha n)` clauses, each clause chooses three distinct variables uniformly and then independent uniform signs.

The predecessor reports used the clean explicit theorem bracket

\[
3.52\le \alpha \le 4.4898,
\]

from Hajiaghayi--Sorkin on the lower side and Diaz--Kirousis--Mitsche--Perez-Gimenez on the upper side.

A fresh primary-status check found an important nuance that future reports should preserve. Coja-Oghlan et al., *The random k-SAT Gibbs uniqueness threshold revisited* (CPC, 2026), state that the interpolation method of Franz--Leone / Panchenko--Talagrand yields a **rigorous upper bound on the sharp threshold sequence matching the 1RSB variational prediction**. Their table reports the physics value `d_sat(3)≈12.801` in their average-degree normalization `d=k alpha`, corresponding numerically to `alpha≈4.267`. But the same discussion explicitly labels `12.801` as the physics prediction; in this run I did **not** recover a separately interval-certified numerical evaluation of the relevant interpolation variational functional at `k=3`. Therefore I record two levels rather than silently turning a rounded physics table entry into a machine-certified theorem constant:

- strongest supported **variational** upper: the rigorous interpolation/1RSB upper functional, reported numerically near `alpha≈4.267`;
- strongest explicit decimal theorem endpoint independently recovered here: `4.4898`.

Also, for fixed `k=3`, existence of a single uniform limiting threshold is itself still open; Friedgut gives a sharp threshold sequence. Thus the correct source object is the SAT/UNSAT threshold sequence (or its liminf/limsup bounds), not an already-proved limiting constant.

For the stable explicit-decimal fleet metric this run therefore records

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad
W:0.9698\longrightarrow0.9698.
\]

**No fleet-produced threshold endpoint moved this run.** The new result below is a constructive mechanism theorem.

Source checks used this run:

- M. Hajiaghayi, G. Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193.
- J. Diaz, L. Kirousis, D. Mitsche, X. Perez-Gimenez, *A new upper bound for 3-SAT*, arXiv:0807.3600.
- A. Coja-Oghlan et al., *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 2026; their discussion explicitly separates small-fixed-`k` openness from the interpolation upper bound.
- S. Franz, M. Leone, *Replica bounds for optimization problems and diluted spin systems*, cond-mat/0208280, for the rigorous variational-upper-bound mechanism.

## 1. Compact handoff, and why this run changes method

The previous two substantive NM13-06 T04 runs pursued Hajiaghayi--Sorkin's degree-spectrum direction. They derived:

1. a four-parameter local polarity rule for the clause-risk potential `m2+eta m3`;
2. the corrected two-type unit-propagation branching factor
   \[
   \rho=\frac{\sum ab x_{a,b,c,d}}{m_2};
   \]
3. an exact first-order drift formula for `rho`;
4. the logarithmic barrier candidate
   \[
   \Phi_{\eta,\beta}=m_2+\eta m_3-\beta\log(1-\rho).
   \]

That route produced real local-control information but **did not move the threshold** and still required a full high-dimensional degree ODE plus certified terminal analysis. Rather than spend a third run elaborating the same ODE, I execute a materially different constructive attack now: start from the literal-majority assignment and analyze a nonbacktracking local repair process as a branching system.

Historical routes not restarted: one-variable cavity iteration, fractional solution-count martingales, randomized booster replacement, generic helper replacement, mesoscopic-to-local Fourier transfer, loose-hypertree cavity, ranked-spreadness black boxes, and positive-temperature/free-energy compactification. NM13-13 is separately pursuing cluster-aware upper-bound counting/rescue-star penalties; the present run stays constructive and does not duplicate it.

## 2. Majority assignment and its exact local weak limit

Put

\[
\mu=\frac{3\alpha}{2}.
\]

For a uniformly selected variable, let `P` and `N` denote its positive and negative occurrence counts. In the local weak limit of the iid proper random 3-CNF,

\[
P,N\stackrel{\mathrm{ind}}\sim \operatorname{Pois}(\mu).
\]

Define the **majority assignment** `sigma^maj` by setting each variable to satisfy whichever sign occurs more often; ties are broken by an independent fair coin. Let

\[
Z=\min(P,N),\qquad M=\max(P,N).
\]

Exactly `Z` occurrences of the variable are false and `M` are true under `sigma^maj`, including the tied case. Hence the limiting fraction of literal occurrences that are false is

\[
\boxed{
q(\alpha)=\frac{\mathbb E Z}{2\mu}.
}
\tag{2.1}
\]

For independent equal-mean Poisson variables the Skellam identity gives the useful closed form

\[
\boxed{
q(\alpha)=\frac12\left[1-e^{-2\mu}\{I_0(2\mu)+I_1(2\mu)\}\right].
}
\tag{2.2}
\]

A uniformly sampled **false occurrence** is not attached to an ordinary Poisson variable: it size-biases the pair `(P,N)` by `Z`. Thus

\[
\Pr\{(P,N)=(p,n)\mid\hbox{sampled false occurrence}\}
=\frac{\min(p,n)\,\pi_\mu(p)\pi_\mu(n)}{\mathbb EZ}.
\tag{2.3}
\]

This size bias is the key correction that a naive independent-literal branching estimate misses.

A random clause is unsatisfied by `sigma^maj` with local-limit probability `q^3`, so the initial unsatisfied-clause density is

\[
u_0(\alpha)=\alpha q(\alpha)^3.
\tag{2.4}
\]

This is a mechanism statistic, not a lower-bound theorem.

## 3. Break count of a candidate flip

Fix a variable reached through one of its false occurrences. If we flip it away from its majority value, that occurrence becomes true and can repair its current unsatisfied clause. The danger is its `M` occurrences that were true before the flip.

Call one of those `M` clauses a **break clause** if the selected variable was its unique true literal under `sigma^maj`. On a collision-free local neighborhood the two partner literals are asymptotically independent false occurrences, each false with probability `q`. Therefore, conditionally on `(P,N)`, the number `B` of break clauses has the local weak-limit law

\[
\boxed{
B\mid(P,N)\sim\operatorname{Bin}(M,q^2),
}
\tag{3.1}
\]

where `(P,N)` has the false-occurrence size-biased law (2.3).

Equivalently, for `t>=1`,

\[
\Pr(B\ge t)
=\frac1{\mathbb EZ}
\sum_{p,n\ge0}\min(p,n)\pi_\mu(p)\pi_\mu(n)
\Pr\{\operatorname{Bin}(\max(p,n),q^2)\ge t\}.
\tag{3.2}
\]

### Exact mean identity

Because `Z M=P N` pointwise and `P,N` are independent Poisson,

\[
\mathbb E[ZM]=\mathbb E[PN]=\mu^2.
\]

Thus a uniformly chosen candidate reached through a false occurrence has

\[
\begin{aligned}
r_1(\alpha):=\mathbb EB
&=q^2\frac{\mathbb E[ZM]}{\mathbb EZ}\\
&=q^2\frac{\mu^2}{2\mu q}\\
&=\boxed{\frac{\mu q}{2}=\frac{3\alpha q}{4}}.
\end{aligned}
\tag{3.3}
\]

At `alpha=3.52`, the validated value is already

\[
r_1=0.9998068432952295\ldots,
\]

while at `alpha=4` it is `1.1581642192445678...`. This explains a feature of the old 3.52 barrier from a completely different angle: **single-choice local repair is essentially critical exactly there.**

This numerical coincidence is not itself a proof that Hajiaghayi--Sorkin's algorithm is equivalent to this process, and I do not claim such an equivalence.

## 4. A materially different algorithm: nonbacktracking two-choice repair

Start from `sigma^maj`.

For an unsatisfied root clause `C`:

1. for each of its three variables compute its break count `B` with respect to the initial majority assignment;
2. flip a variable with minimum `B` (fixed deterministic tie rule after the majority tie coins);
3. every break clause thereby created is a child repair obligation;
4. at a nonroot child clause, **do not flip the parent variable back**. The two other literals were false under the original majority assignment. Among their two variables, flip the one with smaller break count;
5. recurse.

On a collision-free factor neighborhood, the three root candidates have iid copies of `B`, while each nonroot repair has two fresh iid copies. Therefore the local repair tree has root offspring

\[
Y_3=\min(B_1,B_2,B_3)
\]

and nonroot offspring

\[
Y_2=\min(B_1,B_2).
\tag{4.1}
\]

The correct reproduction mean is consequently

\[
\boxed{
r_2(\alpha)=\mathbb E Y_2
=\sum_{t\ge1}\Pr(B\ge t)^2.
}
\tag{4.2}
\]

This is the key gain from the extra local choice. It is not the same mechanism as the preceding `rho` barrier: there the algorithm controls an evolving 2-clause unit cascade; here the starting assignment is globally degree-biased, and the process selects between **two repair parents** at each newly broken clause.

## 5. Theorem — local repair is a subcritical Galton--Watson process when `r2<1`

### Theorem 5.1

Fix `alpha` and consider the radius-`L` local weak limit around a uniformly sampled clause that is unsatisfied by the majority assignment. On the event that the explored factor neighborhood is a tree, the nonbacktracking two-choice repair exploration is a Galton--Watson tree with root offspring `Y3` and all subsequent offspring iid with law `Y2` from (4.1).

If

\[
r_2(\alpha)<1,
\]

then the infinite local-limit repair dies out almost surely. Moreover its total progeny has an exponential tail.

### Proof

An initially unsatisfied clause contains three false occurrences. In the local weak limit their variables are distinct and their marked degree pairs are independent with the false-occurrence Palm law (2.3). Their break counts are therefore iid with law (3.1)--(3.2), giving `Y3` at the root.

Suppose a flip creates a child obligation. By definition the child clause was critical for the parent variable under `sigma^maj`: the parent literal was its unique true literal. Thus its other two literals were false under `sigma^maj`. Conditional on a tree neighborhood, those two occurrences lead to fresh independent variables with the same false-occurrence Palm law. Excluding the parent variable leaves exactly those two candidates. Choosing the smaller break count gives an iid copy of `Y2`. Induction over generations proves the branching representation.

`B` has an exponential moment because the size-biased Poisson pair does, and `0<=Y2<=B1`. Hence `Y2` has an exponential moment. A Galton--Watson process with mean strictly below one dies almost surely; with an offspring exponential moment its total progeny has an exponential tail (e.g. by the standard generating-function argument: the progeny pgf is analytic in a neighborhood of one because the offspring pgf is analytic there and has derivative `<1`). QED.

## 6. Rigorous numerical certificate: two-choice repair remains strongly subcritical across the old explicit bracket

I wrote and executed an outward-rounded interval checker:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T04-27-22__majority_repair_interval.py`

Archived output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T04-27-22__majority_repair_interval.out`

The computation truncates `P,N` at `K=50` and rigorously covers the omitted tail. For `K>mu`,

\[
\Pr\{\operatorname{Pois}(\mu)\ge K\}
\le e^{-\mu}\left(\frac{e\mu}{K}\right)^K.
\tag{6.1}
\]

The omitted false-occurrence size-biased mass is bounded by

\[
\delta_Z\le2\mu\Pr\{\operatorname{Pois}(\mu)\ge K\}.
\tag{6.2}
\]

For the tail of (4.2), use `x^2<=x` and `ZM=PN`:

\[
\sum_{t>K}\Pr(B\ge t)^2
\le \mathbb E[(B-K)_+]
\le \frac{2\mu^2\Pr\{\operatorname{Pois}(\mu)\ge K\}}{\mathbb EZ_{\le K}}.
\tag{6.3}
\]

All finite sums/binomial tails are evaluated with `mpmath.iv` interval arithmetic. The actual executed bounds are:

| alpha | q | random-candidate `r1=EB` | certified `r2=E min(B1,B2)` upper | initial unsat density `alpha q^3` |
|---:|---:|---:|---:|---:|
| 3.52 | 0.378714713369405 | 0.999806843295230 | **0.489551142506079** | 0.191196174205506 |
| 4.0 | 0.386054739748189 | 1.158164219244568 | **0.603250743183232** | 0.230147709922421 |
| 4.4898 | 0.392321936451922 | 1.321085272711379 | **0.723865274237294** | 0.271115765044649 |

At `alpha=4.4898` the Poisson Chernoff remainder is `<1.81e-25`; the omitted size-biased mass is `<2.44e-24` and the conservative omitted `r2`-tail numerator is `<1.65e-23`.

Thus, in particular,

\[
\boxed{r_2(4.4898)<0.724<1.}
\tag{6.4}
\]

This is a large, rigorously checked mechanism margin. It **does not** imply satisfiability at `4.4898`; indeed that would contradict the known UNSAT theorem. What it proves is more diagnostic: the obstruction beyond `3.52` is not local repair-tree branching by itself.

## 7. Deterministic finite-patch correctness

The branching computation would be useless if the repair genealogy did not correspond to an actual satisfying local move. The next lemma supplies that deterministic bridge.

### Lemma 7.1 — clean finite repair tree

Fix a formula and its majority assignment. Suppose the recursive repair exploration of an initially unsatisfied root clause terminates and its **closed factor neighborhood** has the following properties:

1. no variable is selected twice;
2. apart from parent-child repair clauses, no clause contains two selected variables;
3. the closed neighborhood includes every clause incident to every selected variable.

Flip every selected variable. Then:

- the root clause becomes satisfied;
- every repair child clause becomes satisfied by its selected child variable;
- no initially satisfied clause becomes unsatisfied;
- no clause outside the closed patch changes.

### Proof

The root variable is selected from a literal false under `sigma^maj`, so its flip makes the root clause true. If a selected variable `v` creates a repair child `D`, then before flipping `v`, `D` had the literal of `v` as its unique true literal. After flipping `v`, that literal is false; the recursive construction chooses one of the two other variables of `D`, whose literal was false under `sigma^maj`, and flips it, making that literal true. By property 2 no later selected variable occurs in `D`, so `D` remains satisfied.

Now consider any other initially satisfied clause incident to a selected variable `v`. If `v` was not its unique true literal, flipping `v` cannot falsify the clause unless a second selected variable simultaneously removes another true literal. Property 2 excludes that. If `v` was its unique true literal, that clause is exactly one of `v`'s break clauses and hence appears as a repair child; the preceding paragraph applies. Property 3 says every clause whose truth value can change is inside the patch. Therefore clauses outside the patch are unchanged. QED.

## 8. Corollary — a rigorous one-round linear improvement exists whenever `r2<1`

### Corollary 8.1

Fix `alpha` with `r2(alpha)<1`. There exist constants `L,D,K` and `c(alpha)>0` such that, with high probability over the random formula and majority tie coins, one can find at least `c(alpha)n` pairwise noninteracting clean repair patches, each of size at most `K`, rooted at distinct clauses unsatisfied by `sigma^maj`.

Flipping all selected variables in these patches produces an assignment with at least `c(alpha)n` fewer unsatisfied clauses and no new unsatisfied clause caused outside those patches. The patches can be found in polynomial time for fixed `L,D,K` by bounded-depth exploration and greedy packing.

### Proof

By Theorem 5.1, the local-limit repair tree is finite almost surely and has exponentially decaying total size. Choose finite depth/size cutoffs `L,K` so that a root repair terminates within those cutoffs with positive probability. Then choose a finite degree cutoff `D` large enough that, simultaneously, every variable in the closed patch has degree at most `D` with still positive probability. For a fixed finite neighborhood, the probability of a collision in the random proper 3-CNF tends to zero. Lemma 7.1 therefore identifies a finite rooted factor-neighborhood type (indeed a finite family of types) having strictly positive limiting probability among majority-unsatisfied roots.

The density of majority-unsatisfied roots converges to `alpha q^3>0`. Counts of any fixed bounded rooted neighborhood type in a sparse random factor graph concentrate around their local-weak-limit expectations (one may expose clauses one at a time and use bounded differences after the fixed degree truncation). Consequently, whp there are `Theta(n)` clean bounded repair roots.

Associate to each such root its closed patch. Because every patch has bounded radius and all degrees in its closure are at most `D`, a patch can intersect or directly interact with only `O_{L,D}(1)` other candidate patches. The conflict graph therefore has bounded maximum degree. Greedy independent-set selection leaves `Omega(n)` pairwise noninteracting patches. Apply Lemma 7.1 to all selected patches simultaneously; their closures are disjoint and no clause connects two selected-variable sets, so their effects cannot interfere. Each patch repairs its root and creates no unrepaired new clause. QED.

This corollary is the **demonstrated mechanism gain of the run**. It is substantially stronger than a simulation: it proves a linear-density constructive repair improvement in the random model from a quantitatively subcritical local process.

It is still far weaker than a threshold lower-bound improvement because it performs only one bounded-patch packing round.

## 9. What the calculation teaches: the missing obstruction is global load/interference, not local branching

The most useful negative information is the contrast

\[
r_1(3.52)\approx1
\qquad\text{but}\qquad
r_2(4.4898)<0.724.
\]

A one-candidate repair process naturally runs into a branching barrier near the known constructive `3.52` point. Two-choice nonbacktracking repair destroys that local barrier all the way across the old explicit bracket.

Yet formulas are rigorously UNSAT by `4.4898`. Therefore any attempted proof that equates `r2<1` with global satisfiability is false. The missing phenomenon must live in the **linear-density interaction between repair demands**: different initial unsatisfied roots compete for variables, repair trees merge, a variable cannot be flipped independently for many obligations, and clauses can receive multiple flips. Said differently, the local branching tree is easy; the unresolved object is a random packing/orientation/load problem for a positive density of such trees.

This diagnosis rules out a tempting but invalid next step: iterating the scalar Galton--Watson estimate as though every repaired root saw a fresh majority environment. That would falsely predict success even in the proven UNSAT regime.

## 10. Next attack

The next constructive obligation is now sharply defined and is not another local branching lemma.

Build a **marked configuration-model density evolution** for simultaneous two-choice repair. The state must at minimum distinguish:

- untouched majority variables by `(Z,M)` and current flip status;
- outstanding unsatisfied-clause demand;
- break-clause demand created by flips;
- variables already claimed by another repair tree;
- merger/collision mass between active repair components.

The target is a rigorous contraction region: for some explicit `alpha>3.52`, prove that one batched repair stage decreases the outstanding unsatisfied-clause density by a multiplicative factor while keeping the claimed-variable/merger density controlled, then iterate until the residual is `o(n)`. Only after such a global load theorem is proved is it legitimate to attach a cleanup procedure and claim a new lower endpoint.

A particularly useful first checkpoint is `alpha=3.6`: the one-choice mean has crossed or nearly crossed its natural barrier, while the two-choice local margin is still large. The proof must exploit that margin without assuming fresh independence after a linear number of flips.

## 11. Essential artifacts and persistence

Executed rigorous checker:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T04-27-22__majority_repair_interval.py`

Archived actual output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T04-27-22__majority_repair_interval.out`

Artifact creation commits:

- code: `66e455511279112691ccbba033c4956f798b1299`
- output: `d226f5260e7c24896db18536c37e98c468e21240`

## 12. ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  role: NM06_Constructive_Random_3SAT
  target: T04
  status: OPEN/PARTIAL
  source_model: iid proper signed random 3-CNF, m=floor(alpha*n)
  explicit_decimal_bracket_before: [3.52, 4.4898]
  explicit_decimal_bracket_after: [3.52, 4.4898]
  explicit_width_before: 0.9698
  explicit_width_after: 0.9698
  threshold_endpoint_movement: none
  literature_correction: >-
    2026 primary status literature says the rigorous interpolation method gives
    an upper bound on the sharp threshold sequence matching the 1RSB variational
    prediction; its table reports d_sat(3) about 12.801 (alpha about 4.267), but
    this run did not independently interval-certify that variational numerical
    evaluation, so 4.267 is not promoted here to the fleet's explicit certified
    decimal endpoint.
  method_change: >-
    Switched from the four-degree rho-barrier ODE route to majority-start
    nonbacktracking two-choice repair, rather than spending a third unchanged
    run on the same local-control obstruction.
  mechanism_gain: >-
    Proved the false-occurrence Palm law and B|P,N~Bin(max(P,N),q^2), the exact
    one-choice mean r1=mu*q/2, the two-choice Galton-Watson reproduction
    r2=sum_t P(B>=t)^2, deterministic finite-patch correctness, and a one-round
    linear-density clean-repair corollary. Validated r2(4.4898)<0.723866 by
    outward interval arithmetic with analytic Poisson-tail bounds.
  decisive_numbers:
    alpha_3_52:
      q: 0.378714713369405
      r1: 0.999806843295230
      r2_upper: 0.489551142506079
    alpha_4_0:
      q: 0.386054739748189
      r1: 1.158164219244568
      r2_upper: 0.603250743183232
    alpha_4_4898:
      q: 0.392321936451922
      r1: 1.321085272711379
      r2_upper: 0.723865274237294
  interpretation: >-
    Local repair branching is not the obstruction beyond 3.52; global
    linear-density load, mergers and variable competition are. r2<1 alone
    cannot imply satisfiability because it remains true in the proven UNSAT
    region.
  previous_failed_or_parked_routes:
    - four-parameter clause-risk rule without global trajectory certification
    - logarithmic rho-barrier rule without full degree ODE/terminal proof
    - one-variable cavity iteration
    - fractional solution-count martingales
    - randomized booster/helper replacement
    - mesoscopic-to-local Fourier transfer
    - loose-hypertree cavity
    - ranked-spreadness black boxes
    - positive-temperature/free-energy compactification
  neighbor_nonduplication: >-
    NM13-13 remains on cluster-aware upper-bound counting/rescue-star penalties;
    this run is a constructive local-repair lower-bound mechanism.
  residual_obstruction: >-
    Control simultaneous repair of a positive density of roots under mergers,
    repeated-variable claims and loss of fresh independence.
  next_attack: >-
    Marked configuration-model density evolution for batched two-choice repair;
    seek a rigorous contraction region first at alpha=3.6, then attach a
    residual cleanup only after the global load theorem is proved.
  artifacts:
    code: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T04-27-22__majority_repair_interval.py
    output: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T04-27-22__majority_repair_interval.out
```

No claim of a new 3-SAT threshold endpoint, full satisfiability algorithm, convergence of the fixed-`k=3` threshold sequence, or replica-derived theorem is made in this report. The local theorem and finite-patch corollary are proved; the repeated global repair program is the remaining constructive gap.
