Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 constructive random 3-SAT: the static blocked-majority core is subcritical; dynamic promotion is the obstruction

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT, constructive lower-bound route**  
Status: **OPEN / PARTIAL**

## 0. Source-level threshold metric before / after

Freeze the exact source model: `m=floor(alpha n)` clauses; each clause chooses three distinct variables uniformly and gives the three literals independent uniform signs.

The strongest explicit decimal theorem bracket I can presently support without converting a physics table entry into a certified numerical variational evaluation is

\[
\boxed{3.52\le \alpha_{3\text{-SAT}}\le 4.4898}.
\]

The lower endpoint is Hajiaghayi--Sorkin's constructive theorem. The upper endpoint is Diaz--Kirousis--Mitsche--Perez-Gimenez's a.a.s.-UNSAT theorem. The 2026 paper of Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis reiterates that the fixed-small-`k` threshold problem remains unresolved and explains that interpolation turns the 1RSB variational prediction into a rigorous upper functional. Its table displays the physics value `d_sat(3)≈12.801`, i.e. `alpha≈4.267`, but this run did not recover an independently interval-certified numerical evaluation of that variational functional at `k=3`. I therefore preserve the auditable explicit-decimal bracket and separately record the stronger symbolic variational upper mechanism.

Thus the source metric is

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

**No source-level threshold endpoint moved this run.** The gain below is a structural theorem that removes one candidate global obstruction and identifies the next one quantitatively.

Fresh bounded source check, 2026-09-20:

- M. Hajiaghayi, G. B. Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193.
- J. Diaz, L. Kirousis, D. Mitsche, X. Perez-Gimenez, *A new upper bound for 3-SAT*, arXiv:0807.3600 / FSTTCS 2008.
- A. Chatterjee et al., *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (2026), published online 27 March 2026.
- A 2025 Aarhus thesis still describes `4.4898` as the best explicit upper bound for ordinary iid random 3-SAT.

Large-`k` threshold theorems, sharp-window existence, random quantum SAT, `(3+p)`-SAT, and `k`-wise-independent clause models are not used as solutions of the fixed iid `k=3` target.

## 1. Compact handoff and why this is the right continuation

The preceding run abandoned the four-degree / unit-propagation ODE route after two substantive local-control advances without a threshold move. It switched to the majority assignment and proved a genuinely different mechanism:

- if `P,N iid Pois(mu)`, `mu=3 alpha/2`, `Z=min(P,N)`, `M=max(P,N)`, then the false-occurrence Palm law is weighted by `Z`;
- the majority break count satisfies `B|(P,N) ~ Bin(M,q^2)`, where `q=E Z/(2mu)`;
- one-choice repair has mean `r1=mu q/2`, essentially critical at `alpha=3.52`;
- nonbacktracking two-choice repair has offspring `Y2=min(B1,B2)` and certified mean `r2(4.4898)<0.723866`;
- a terminating clean repair tree is an exact finite satisfying move, and bounded clean patches occur with positive linear density.

That calculation proved that **local repair-tree branching is not the barrier**, because it is still strongly subcritical in a density range known to be UNSAT. The unresolved issue was global load: positive-density repair trees may merge, compete for variables and promote new break constraints.

This run attacks that exact obstruction rather than deriving another repair-tree lemma. It asks whether a *static global blocked core* already percolates under the majority assignment. The answer is no, rigorously all the way through the old explicit upper endpoint. The calculation then isolates dynamic **promotion of previously zero-break variables** as the missing mechanism.

Historical failed/parked routes remain preserved: one-variable cavity iteration, fractional solution-count martingales, randomized booster/helper replacement, mesoscopic-to-local Fourier transfer, loose-hypertree cavity, ranked-spreadness black boxes, positive-temperature/free-energy compactification, and the unclosed four-parameter `rho`-barrier ODE. NM13-13 remains on cluster-aware weighted counting / rescue penalties; this report is constructive and does not duplicate that route.

## 2. Majority marks and the static blocked hypergraph

Let

\[
\mu=\frac{3\alpha}{2},\qquad P,N\stackrel{\rm iid}{\sim}\operatorname{Pois}(\mu),
\qquad Z=\min(P,N),\quad M=\max(P,N).
\]

Under the literal-majority assignment (fair independent tie coin), a variable has exactly `Z` false and `M` true occurrences. Put

\[
q=\frac{\mathbb EZ}{2\mu}.
\tag{2.1}
\]

As proved in the predecessor report, a variable reached through one of its false occurrences has Palm law

\[
\Pr_F(P=p,N=n)=\frac{\min(p,n)\,\pi_\mu(p)\pi_\mu(n)}{\mathbb EZ},
\tag{2.2}
\]

and its number `B` of **break clauses** -- initially satisfied clauses in which its literal is the unique true literal -- obeys

\[
B\mid(P,N)\sim\operatorname{Bin}(M,q^2).
\tag{2.3}
\]

Define

\[
f(M)=\Pr(B\ge1\mid M)=1-(1-q^2)^M,
\tag{2.4}
\]

and the two Poisson expectations

\[
A_1=\mathbb E[Zf(M)],\qquad
A_2=\mathbb E[Z(Z-1)f(M)].
\tag{2.5}
\]

Let

\[
s=\Pr_F(B\ge1)=\frac{A_1}{\mathbb EZ}.
\tag{2.6}
\]

Since `EZ=2mu q`, the combined probability that a uniformly sampled signed occurrence is false **and** belongs to a variable with positive break count is

\[
\boxed{qs=\frac{A_1}{2\mu}}.
\tag{2.7}
\]

Now define the **static blocked-majority hypergraph** `H_blk(F)` on the formula variables: an original 3-clause is a hyperedge iff

1. all three literals are false under the initial majority assignment, and
2. each of its three variables has initial break count `B>=1`.

Thus an unsatisfied clause outside `H_blk` has at least one zero-break variable and admits an immediate one-flip repair that creates no new unsatisfied clause *relative to the initial majority assignment*.

Important: `H_blk` is static. It does not update the break counts after flips. The distinction is the point of this run.

## 3. Theorem — exact local branching law of the blocked-majority hypergraph

### Theorem 3.1

For fixed `alpha`, in the local weak limit of the proper iid random 3-CNF with majority marks:

**(a) Blocked-edge density.** The number of blocked clauses divided by `n` converges in probability to

\[
\boxed{
\beta(\alpha)=\alpha\left(\frac{A_1}{2\mu}\right)^3.
}
\tag{3.1}
\]

**(b) Component exploration.** Follow a uniformly sampled incidence from a blocked clause to one of its variables. Conditional on its type `(P,N)`, the number `D` of *other* blocked clauses reached through that variable has law

\[
D\mid(P,N),B\ge1
\sim \operatorname{Bin}\left(Z-1,(qs)^2\right),
\tag{3.2}
\]

where the type distribution is the false-occurrence Palm law tilted by `f(M)`.

A nonroot blocked clause has two fresh variables after deleting its parent incidence. Hence the clause-to-clause offspring is `Y=D_1+D_2`, and its mean is exactly

\[
\boxed{
R(\alpha)=2(qs)^2\frac{A_2}{A_1}
=\frac{A_1A_2}{2\mu^2}.
}
\tag{3.3}
\]

**(c) Subcritical consequence.** If `R(alpha)<1`, the rooted local-limit blocked component has an exponential total-size tail. In the finite random formula the largest blocked component is `o(n)` in probability. Equivalently, for every `eps>0` there is a finite `K=K(alpha,eps)` such that with probability tending to one, fewer than `eps n` blocked clauses belong to components containing more than `K` blocked clauses.

### Proof

For (a), expose one uniformly sampled clause. In the local weak limit its three variable neighborhoods are disjoint. Each incident signed occurrence is false with probability `q`. Conditional on being false, its variable has the Palm law (2.2), and by (2.3) has `B>=1` with probability `s`. The three branches are independent in the tree limit. Thus the blocked probability is `(qs)^3`, and there are `alpha n+o(n)` clauses. The indicator depends on a finite marked neighborhood after any fixed degree truncation. Bounded-differences concentration applies to the truncated statistic; the Poisson degree tail makes the discarded density arbitrarily small. Letting the truncation grow proves (3.1).

For (b), condition on arriving at a variable through one of its false occurrences and on `B>=1`. Given `(P,N)`, there are `Z-1` remaining false occurrences. Consider one. Its clause is blocked exactly when its two partner occurrences are both false and both partner variables have positive break count. On a factor tree those partner branches are fresh. Each has probability `qs` of carrying the joint mark `false and B>=1`, independently, so the child-clause probability is `(qs)^2`. This gives (3.2).

The type law on arrival is proportional to

\[
Z\,\pi_\mu(P)\pi_\mu(N)f(M).
\]

Consequently

\[
\mathbb E[Z-1\mid F,B\ge1]
=\frac{\mathbb E[Z(Z-1)f(M)]}{\mathbb E[Zf(M)]}
=\frac{A_2}{A_1}.
\tag{3.4}
\]

A nonroot blocked clause has two fresh variable branches, yielding

\[
\mathbb EY=2(qs)^2\frac{A_2}{A_1}.
\]

Substituting `qs=A1/(2mu)` gives (3.3).

For (c), the tilted Poisson type law has exponential moments, and `D<=Z-1`; hence `Y` has an exponential moment. If `EY=R<1`, the corresponding Galton--Watson total progeny has an exponential tail by the standard pgf argument: for sufficiently small `t>0`, `E exp(t(Y-1))<1`, so the exploration admits an exponential supermartingale until extinction.

For the finite formula, fix `K`. Whether the blocked component of a uniformly sampled blocked clause contains more than `K` blocked clauses is determined by exposing only finitely many factor-graph incidences, except on a degree-tail event. After truncating degrees, the proper random 3-CNF converges locally to the marked Poisson factor tree, so the expected fraction of blocked clauses lying in components larger than `K` converges to the corresponding Galton--Watson tail, up to an arbitrarily small truncation error. Since the local tail tends exponentially to zero as `K` grows, choose `K` so that this expectation is below `eps^2`. Markov's inequality then gives, with probability at least `1-eps-o(1)`, fewer than `eps n` blocked clauses in components larger than `K`. Replacing `eps` by an arbitrary sequence tending slowly to zero yields `max_component/n -> 0` in probability. This proves the stated finite consequence. QED.

This theorem is deliberately weaker than an `O(log n)` maximum-component assertion; the `o(n)` statement is all that is needed here and follows directly from local weak convergence without hiding a global collision estimate.

## 4. Rigorous interval certificate: even the static blocked core is subcritical at 4.4898

I wrote and executed

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T05-29-47__blocked_majority_core.py`

and archived the actual output in

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T05-29-47__blocked_majority_core.out`.

The finite Poisson sums use `mpmath.iv` outward interval arithmetic with cutoff `K=60`. For `K>mu`,

\[
\Pr\{\operatorname{Pois}(\mu)\ge K\}
\le e^{-\mu}\left(\frac{e\mu}{K}\right)^K.
\tag{4.1}
\]

For the omitted first moment,

\[
\mathbb E[Z;\max(P,N)\ge K]
\le 2\mu\Pr\{\operatorname{Pois}(\mu)\ge K-1\}.
\tag{4.2}
\]

For `A2`, use `Z(Z-1)<=(P+N)^2` and a union bound over `P>=K` or `N>=K`; the script evaluates the resulting Poisson first/second tail moments explicitly. The actual certified intervals are:

| alpha | q | blocked-edge density beta | blocked reproduction R |
|---:|---:|---:|---:|
| 3.52 | `[0.378714713369389, 0.378714713369527]` | `[0.051004438894262, 0.051004438894412]` | `[0.463065417187514, 0.463065417188413]` |
| 3.60 | `[0.380036729791130, 0.380036729791383]` | `[0.055104380166073, 0.055104380166288]` | `[0.492947921718411, 0.492947921719673]` |
| 4.00 | `[0.386054739748161, 0.386054739748392]` | `[0.078191135485644, 0.078191135485898]` | `[0.655018496174727, 0.655018496176092]` |
| 4.4898 | `[0.392321936451894, 0.392321936452100]` | `[0.112041316970440, 0.112041316970733]` | **`[0.879523134003874, 0.879523134005534]`** |

At `alpha=4.4898` the omitted `EZ` tail is below `1.653e-32` and the conservative omitted `A2` tail is below `1.221e-30`. Therefore

\[
\boxed{R(4.4898)<0.88<1.}
\tag{4.3}
\]

is certified.

This is the main demonstrated mechanism gain. The previous run showed that a *single repair genealogy* is locally subcritical. The present theorem is stronger in a different direction: **the entire initial hypergraph of clauses with no zero-break escape has no linear component even at the proven UNSAT endpoint.** Therefore a static blocked-core/percolation explanation cannot be the missing threshold obstruction.

It would be incorrect to infer satisfiability: `H_blk` freezes break counts at time zero, while actual flips change which variables have positive break count.

## 5. Exact promotion susceptibility of a zero-break variable

The static theorem forces attention to that dynamic change. There is a simple exact local calculation.

Condition on a false-Palm variable having `B=0`. For each of its `M` initially true occurrences, `B=0` means the two partner literals are **not both false**. Imagine, only for this diagnostic, that every other variable is independently flipped with probability `theta`, while the focal variable is held fixed. Conditional on `not both false`, the probability that a true occurrence becomes a new break occurrence is

\[
a_\theta
=\frac{2q(1-q)\theta(1-\theta)+(1-q)^2\theta^2}{1-q^2}.
\tag{5.1}
\]

Hence the exact tree-limit survival probability that a zero-break variable remains zero-break is

\[
\boxed{
S_0(\theta)=
\frac{\mathbb E_F[(1-q^2)^M(1-a_\theta)^M]}
{\mathbb E_F[(1-q^2)^M]}.
}
\tag{5.2}
\]

Differentiating at zero gives the **promotion susceptibility**

\[
\boxed{
\chi(\alpha)=-S_0'(0)
=\frac{2q}{1+q}\,
\frac{\mathbb E_F[M(1-q^2)^M]}
{\mathbb E_F[(1-q^2)^M]}.
}
\tag{5.3}
\]

The high-precision diagnostic output (not used as an interval-certified theorem constant) gives

\[
\chi(3.52)\approx3.50262,\quad
\chi(3.60)\approx3.57582,\quad
\chi(4.00)\approx3.94075,\quad
\chi(4.4898)\approx4.38549.
\]

At `alpha=3.6`, (5.2) gives

\[
S_0(0.1)\approx0.700996,\quad
S_0(0.2)\approx0.493735,\quad
S_0(0.3)\approx0.349467.
\]

Thus the reservoir of apparently safe zero-break variables is highly fragile under a positive density of flips. This is precisely the effect absent from `H_blk` and from the predecessor's independent clean-patch theorem.

### Local supply drift for an isolated zero-break repair

One further local identity shows the sign of the problem. Let a candidate be reached through an unsatisfied root and condition on `B=0`. Write

\[
\bar M_0=\mathbb E_F[M\mid B=0],\qquad
\bar Z_0=\mathbb E_F[Z-1\mid B=0].
\]

Flipping it creates, before checking whether the affected neighbor was already nonzero-break,

\[
\text{promotion opportunities}
=\bar M_0\frac{2q(1-q)}{1-q^2}=\chi,
\tag{5.4}
\]

while it destroys old unique-support relations at expected rate

\[
\text{demotion opportunities}
=2q(1-q)\bar Z_0.
\tag{5.5}
\]

For a partner reached through a true occurrence, let

\[
h=\Pr\{\text{no other break occurrence}\mid\text{true-Palm partner}\}.
\tag{5.6}
\]

Then the tree-limit expected first-order change in the number of **zero-break candidate variables** caused by one isolated zero-break repair, counting the selected candidate itself as leaving the reservoir, is

\[
\boxed{
\Delta_0=-1+h\{2q(1-q)\bar Z_0-\chi\}.
}
\tag{5.7}
\]

At `alpha=3.6` the diagnostic values are

\[
\chi=3.5758214,\quad
2q(1-q)\bar Z_0=1.6819124,\quad
h=0.3915451,
\]

so

\[
\boxed{\Delta_0\approx-1.74155.}
\tag{5.8}
\]

The same flip repairs an expected

\[
1+q^2\bar Z_0\approx1.51551
\]

initially unsatisfied roots in this isolated-tree calculation. Thus a naive greedy strategy can remove more than one bad clause per step while consuming roughly `1.74` units of its zero-break-variable supply. This is a mechanism diagnosis, **not** a global density-evolution theorem: after linearly many flips the Palm environment is no longer fresh and correlations must be tracked.

## 6. What failed, what was ruled out, and what remains

The source bracket did not move. Two tempting constructive shortcuts are now ruled out as proof strategies:

1. `r2<1` for two-choice local repair does not imply satisfiability; it remains true at `alpha=4.4898`.
2. Absence of a giant **initial** blocked-majority component does not imply satisfiability; Theorem 3.1 plus (4.3) shows the static blocked hypergraph is subcritical at the same proven-UNSAT density.

The shared failure has one mathematical cause: **dynamic promotion**. A flip changes unique-support status of clauses incident to its neighbors, so a variable with `B=0` can become `B>0` even if no static blocked path reached it. Equation (5.3) quantifies that instability and (5.7) shows that an isolated zero-break greedy step has a sharply negative easy-supply drift already at `alpha=3.6`.

This is not bad news for the constructive route: it reduces the global obstruction to a much smaller state description. Tracking full `(P,N)` plus every repair tree was overkill for the first global test. What must be controlled is the joint evolution of

- unsatisfied-clause density `u(t)`;
- zero-break false-incidence mass `z_0(t)`;
- positive-break false-incidence mass `z_+(t)`;
- unique-support incidence mass that can create promotions;
- collision/claimed-variable mass.

The exact static formulas in Sections 2--5 give the initial conditions and the first derivative terms for such a promoted-break density evolution.

## 7. Next decisive attack

The next run should not repeat a static-core calculation. Derive a **four-mass Wormald system for zero-break peeling with promotion**, starting from the exact Palm initial law above. The first target is `alpha=3.6`:

- choose an unsatisfied clause with a zero-break candidate whenever available;
- include both demotions and promotions of neighboring break counts rather than freezing `B`;
- prove the differential equations under bounded degree truncation and then remove the truncation;
- determine whether `u(t)` reaches zero before `z_0(t)` is exhausted.

If the ODE predicts exhaustion, this route has supplied a decisive obstruction and should be abandoned rather than tuned. If it predicts a positive safety margin, the same equations can be interval-integrated and coupled to the finite random process, creating the first realistic path to a certified `alpha>3.52` lower endpoint.

## 8. Persistence and essential artifacts

Code commit:

`35f36e228465328deeec889f66cc168a32421e92`

Output commit:

`db31e3eb10de6e02bb9ca38783d7e9dcd8b78956`

Artifacts:

- `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T05-29-47__blocked_majority_core.py`
- `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T05-29-47__blocked_majority_core.out`

The rigorous claim uses only the outward interval lines `q`, `beta`, `R` and their analytic tail bounds. The `diagnostic` and `local_B0_flip` lines are high-precision local-limit calculations and are explicitly not promoted to a source threshold improvement.

## 9. ledger_delta

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
  stronger_symbolic_upper_status: >-
    Rigorous interpolation gives an upper variational functional matching the
    1RSB prediction; 2026 literature displays d_sat(3) about 12.801 (alpha
    about 4.267) as the physics value, but this worker has not interval-certified
    the k=3 numerical functional evaluation, so it is not substituted for the
    explicit 4.4898 theorem endpoint.
  previous_run_gain: >-
    Majority-start two-choice nonbacktracking repair is locally Galton-Watson
    subcritical through alpha=4.4898, with certified r2<0.723866, and clean
    bounded patches give a one-round linear-density repair improvement.
  new_theorem: >-
    Defined the static blocked-majority hypergraph. Its blocked-edge density is
    beta=alpha(A1/(2mu))^3 and its exact local clause-to-clause reproduction
    mean is R=A1*A2/(2mu^2), where A1=E[Z f(M)],
    A2=E[Z(Z-1) f(M)], f(M)=1-(1-q^2)^M. If R<1 the local component has an
    exponential tail and the largest finite-n blocked component is o(n) in
    probability.
  certified_numbers:
    alpha_3_52:
      beta_upper: 0.051004438894412
      R_upper: 0.463065417188413
    alpha_3_60:
      beta_upper: 0.055104380166288
      R_upper: 0.492947921719673
    alpha_4_0:
      beta_upper: 0.078191135485898
      R_upper: 0.655018496176092
    alpha_4_4898:
      beta_upper: 0.112041316970733
      R_upper: 0.879523134005534
  mechanism_gain: >-
    Certified that even the entire initial hypergraph of majority-unsatisfied
    clauses whose three variables all have positive break count is subcritical
    at alpha=4.4898. Therefore neither local repair branching nor a static
    blocked-core percolation is the obstruction beyond 3.52.
  promotion_diagnostic: >-
    Derived exact tree-limit zero-break survival S0(theta) and susceptibility
    chi=-S0'(0). At alpha=3.6, chi about 3.57582; an isolated zero-break repair
    has local easy-supply drift about -1.74155 while repairing about 1.51551
    initial unsatisfied roots. These are mechanism diagnostics, not threshold
    gains and not a global fresh-independence assertion.
  failed_or_ruled_out_this_run:
    - infer global satisfiability from r2<1
    - infer global satisfiability from absence of a giant initial blocked core
    - freeze break counts during a positive-density repair process
  inherited_parked_routes:
    - four-parameter rho-barrier without full trajectory certification
    - one-variable cavity iteration
    - fractional solution-count martingales
    - randomized booster/helper replacement
    - mesoscopic-to-local Fourier transfer
    - loose-hypertree cavity
    - ranked-spreadness black boxes
    - positive-temperature/free-energy compactification
  companion_nonduplication: >-
    NM13-13 remains on cluster-aware weighted-counting / rescue penalties;
    NM13-06 remains on the constructive lower-bound side.
  residual_obstruction: >-
    Dynamic promotion and depletion of zero-break variables under a linear
    density of flips; static initial-core and local branching effects are not
    sufficient explanations.
  next_attack: >-
    Derive and interval-test a four-mass zero-break peeling ODE with promotion,
    demotion and collisions at alpha=3.6; prove a finite-process coupling only
    if the ODE reaches u=0 before exhausting the zero-break reservoir.
  artifacts:
    code: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T05-29-47__blocked_majority_core.py
    output: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T05-29-47__blocked_majority_core.out
```

No new 3-SAT threshold endpoint, full satisfiability algorithm, fixed-`k=3` limiting-threshold existence theorem, or replica-only numerical theorem is claimed.