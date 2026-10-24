Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-13 — T04 cluster-aware 3-SAT counting: two-flip rescue stars and a Diaz-compatible refinement

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — limiting satisfiability threshold for classical iid random 3-SAT with uniform signed clauses on three distinct variables**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after

The strongest explicit rigorous numerical bracket I can presently support for the exact classical model remains

\[
\boxed{3.52\le \alpha_{3\text{-SAT}}\le 4.4898},
\qquad W=4.4898-3.52=0.9698.
\]

Therefore the source metric in this run is

\[
[3.52,4.4898]\longrightarrow[3.52,4.4898],\qquad
W:0.9698\longrightarrow0.9698.
\]

**No source-level threshold endpoint moved in this run.** I did obtain a new cluster-aware counting lemma and a concrete refinement of the best upper-bound architecture, but the final certified global optimization below `4.4898` has not yet been completed. I do not relabel the mechanism gain as a threshold improvement.

The endpoints are still supported by Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193, and Diaz--Kirousis--Mitsche--Perez-Gimenez, *A new upper bound for 3-SAT*, arXiv:0807.3600 / FSTTCS 2008. The latter proves a.a.s. unsatisfiability at density `4.4898` for uniform simple proper formulas; the iid-with-replacement proper-clause model in the owner statement is whp equivalent for this threshold purpose because with `m=O(n)` and `8*binom(n,3)=Theta(n^3)` possible proper signed clauses, the probability of a repeated clause is `O(1/n)`.

Fresh bounded checks on 2026-09-20 found no later fixed-`k=3` classical-iid theorem improving either explicit endpoint. Caragiannis--Gravin--Jiang (ESA 2025, DOI `10.4230/LIPIcs.ESA.2025.103`) studies `k`-wise-independent clauses and explicitly changes the independence assumption. Maneva--Sinclair, arXiv:0710.0805, rules out nontrivial core assignments at density `>=4.453`, but its conclusion is the alternative that either the 3-SAT threshold is below `4.453` or the anticipated core geometry fails; it is not an unconditional `4.453` threshold upper bound. Large-`k` threshold identification and sharp-window existence likewise do not identify the limiting `k=3` threshold.

## 1. Short handoff and exact failures that must not be repeated

The predecessor cluster-counting report is

`runs/prob10_2026-09-20/PROB10-04/2026-09-19T23-59-30Z__cluster_weight_barrier_component_quotient.md`.

It established two useful no-go results and one route change:

1. For any fixed positive clause-local multiplicative weight depending only on the number `1,2,3` of true literals, ordinary second-moment stationarity forces `u=v+w`. Under that condition the identical-pair ratio has exact minimum `5/4`, attained at weight ratio `3:2:1`. Thus that entire mechanism can have subexponential normalized second moment only when
   \[
   \alpha\le \frac{\log 2}{\log(5/4)}=3.1062837\ldots,
   \]
   already below the rigorous lower endpoint `3.52`.
2. Dividing by solution-graph balls of radius `R=o(n/log n)` changes the count by only `exp(o(n))`, so it cannot pay the positive exponential overlap defect above.
3. The exact full-component quotient cancels same-component pair multiplicity, but the remaining cross-component overlap estimate was not closed.

The older R03 history additionally killed: one-variable cavity iteration; fractional solution-count martingales; randomized booster replacement; loose-hypertree transfer; positive-temperature/free-energy compactification; and bounded-excess minimal-UNSAT enumeration below the pure-literal threshold. I do not restart those lines.

The companion worker NM13-06 is currently on the constructive Hajiaghayi--Sorkin route. Its latest report derives exact first-order drift for the unit-propagation branching ratio `rho=S/m2` and a logarithmic barrier control law. This run deliberately stays on the complementary upper-bound / cluster-aware counting side.

## 2. Why the Diaz count is the right place to inject cluster geometry

Diaz et al. do not count all satisfying assignments. Their proof first passes to a typical Poisson 2D degree sequence, removes pure literals, positively unbalances the impure core, treats high-degree variables as heavy jokers, and counts only assignments satisfying the weaker `flat'` condition. Every light variable assigned `0` must occur in at least one **blocking clause**, i.e. a clause in which its negative literal is the only satisfied light literal.

For light degree cap `M=23`, their type variables include

- `t_{i,j}`: light variables assigned `1` with positive/negative degree `(i,j)`;
- `f_{i,j,k}`: light variables assigned `0` with degree `(i,j)` and exactly `k>=1` negative occurrences in blocking clauses;
- literal-copy labels `ps, ns1, ns2, pu, nu`;
- 16 extended clause types.

Their Appendix E gives at an interior critical point

\[
t_{i,j}=\widehat\delta_{i,j}\frac{\nu_{ps}^i}{\Psi_{i,j}},
\qquad
f_{i,j,k}=\widehat\delta_{i,j}
\binom{j}{k}\frac{\nu_{ns1}^k\nu_{ns2}^{j-k}}{\Psi_{i,j}},
\]

with all displayed multipliers positive. At `gamma=4.4898` the reported critical values include

`nu_ps≈1.2782018`, `nu_ns1≈0.33277280`, `nu_ns2≈0.95336927`,

and the first-moment maximum is bounded by

\[
E X\le \bigl((1+10^{-7})\,0.9999998965\bigr)^n.
\]

The numerical base is

\[
q_0=0.9999999964999897,
\qquad \log q_0=-3.5000102877\times10^{-9}.
\]

That margin is extraordinarily thin. The opportunity is therefore not to replace their syntactic restrictions, but to add a **necessary cluster-local maximality constraint** on top of their existing `flat'` count.

## 3. New deterministic lemma: a clean two-flip rescue edge

Fix a satisfying assignment `sigma`. For clarity write variables as `0/1` values.

A clause is **blocking for a variable v** if the literal belonging to `v` is the unique satisfied literal in that clause. Call a true variable `y` a **root** if it has no blocking clause. Call a false variable `x` a **singleton child** if it has exactly one blocking clause `C_x`.

Suppose:

1. `sigma(x)=0` and `sigma(y)=1`;
2. `x` has exactly one blocking clause `C_x`;
3. `y` has no blocking clause;
4. `C_x` contains the literal `not y`, which is false under `sigma`;
5. there is no other clause `D` containing simultaneously the literals `not x` and `y` with every remaining literal of `D` false under `sigma`.

Then call `x -> y` a **clean rescue edge**.

### Lemma 3.1 — two-flip rescue

If `x -> y` is a clean rescue edge, then there is a length-two path of satisfying assignments

\[
\sigma\;\longrightarrow\;\sigma^{y}\;\longrightarrow\;\sigma^{x,y},
\]

where the first step changes `y:1->0` and the second changes `x:0->1`.

### Proof

Because `y` has no blocking clause, flipping `y` alone cannot destroy the last satisfied literal of any clause. Therefore `sigma^y` is satisfying.

Now flip `x`. Under the original assignment, the only clause in which the true literal `not x` was the unique satisfied literal is `C_x`. After `y` has been flipped to `0`, the literal `not y` in `C_x` is true, so `C_x` remains satisfied when `not x` becomes false.

A different clause can become newly vulnerable to the two flips only if it contained two true literals under `sigma`, namely `not x` and `y`, and no other true literal: each of those two literals becomes false after the pair of flips. Hypothesis 5 excludes exactly this case. All other clauses retain a true literal or gain one. Hence `sigma^{x,y}` is satisfying. QED.

The executable truth-table artifact independently enumerates all sign patterns on a clause containing `x,y` and a third variable. After excluding clauses critical at `x` or at `y`, the only newly falsified type is precisely

`(not x) OR y OR (a literal false under sigma)`.

The archived check ends `truth_table_pass=True`.

The same argument applies to the Diaz `flat` semantics for light variables: any clause containing a heavy joker is automatically safe, so heavy clauses only remove potential obstructions.

## 4. Random positive scores turn rescue stars into an exact exponential penalty

Give each light variable an iid continuous positive weight `W_v` (Exp(1) is convenient but the next identity is distribution-free for iid continuous weights) and define

\[
S_W(\sigma)=\sum_v W_v\sigma(v).
\]

For any `flat`-satisfiable configuration, choose an assignment maximizing `S_W` over all `flat`-satisfying assignments. Because every `W_v>0`, every false light variable at this maximum must have at least one blocking clause: otherwise flipping it from `0` to `1` would strictly raise the score while preserving `flat` satisfiability. Thus the maximizing assignment is automatically among the assignments counted by Diaz's `flat'` first moment.

If `x -> y` is a clean rescue edge at such a maximum, Lemma 3.1 gives another satisfying assignment of score difference

\[
S_W(\sigma^{x,y})-S_W(\sigma)=W_x-W_y.
\]

Maximality therefore forces

\[
W_x\le W_y.\tag{4.1}
\]

Choose at most one root for each singleton child by a deterministic tie rule. Because children are false and roots true, the resulting rescue graph is a disjoint union of stars. If a root `y` has `r` children, all `r` inequalities in (4.1) hold exactly when `W_y` is the maximum among the `r+1` iid continuous weights consisting of the root and its children. Hence

\[
\Pr_W[W_x\le W_y\text{ for every child of }y]=\frac1{r+1}.\tag{4.2}
\]

Multiplying over disjoint stars gives the exact score-averaged factor

\[
\boxed{\prod_y\frac1{r_y+1}}.\tag{4.3}
\]

This is the main proved mechanism of the run. It is genuinely cluster/local-geometry aware: it pays for actual satisfying paths of length two, not merely literal counts.

In the Diaz light-variable regime each rescue edge uses one negative occurrence of its root. Since every light root has negative degree at most `M=23`, `r_y<=23`. Therefore, if `E` is the total number of selected clean rescue edges,

\[
\prod_y\frac1{r_y+1}
=\exp\!\left(-\sum_y\log(r_y+1)\right)
\le \exp\!\left(-\frac{\log2}{23}E\right).\tag{4.4}
\]

Thus a linear density `E/n>=eta>0` buys a uniform exponential factor `exp[-eta(log2/23)n]`.

## 5. Why the published Diaz critical type should have positive rescue density

This is the bridge to the `4.4898` architecture. It is not yet promoted to a certified new endpoint, because the refined type enumeration and global maximization remain to be executed.

At the published interior critical point:

- `f_{i,j,1}>0` for allowed light classes with `j>=1`, directly from the positive-multiplier formula above. Hence there is positive density of false singleton-blocked light variables.
- `t_{i,j}>0` for light classes with positive limiting degree mass.
- all relevant extended clause-type weights at the interior critical point are positive powers of positive Lagrange multipliers. In particular there are both blocking and nonblocking placements of `ps` copies and blocking clauses with `nu` slots.

Refine each `t_{i,j}` by the number of its positive-satisfied copies which lie in a clause where that copy is the unique satisfied light literal. A true degree-`(1,1)` variable whose one `ps` copy lands in a nonblocking `ps` slot is a root. Because the old critical type has positive masses of `t_{1,1}` and nonblocking `ps` slots, the entropy-maximizing refinement has a positive root density.

Now refine `f_{i,j,1}` according to whether one of the two unsatisfied literals in its unique blocking clause is a `nu` copy belonging to such a root. Positive root-`nu` mass and positive blocking-clause `nu` slots imply a positive rescue-incidence density in the entropy-typical refinement. Repeated `x,y` co-occurrences which make an edge dirty require an additional pairing of a prescribed bounded-degree variable pair. A linear number of such extra pairings has an `n^{-Theta(n)}` configuration penalty, so it cannot dominate the exponential method-of-types maximum; this collision statement still needs to be written into the refined count rather than merely invoked qualitatively.

Consequently the **candidate refined Diaz functional** is the old finite `M=23` functional multiplied by the score factor (4.3), with new finite type coordinates recording:

1. zero-blocking true roots;
2. `k=1` false singleton children;
3. which blocking `nu` slots meet roots;
4. rescue-star occupancies `r=0,...,23`;
5. dirty pair-collision exceptions.

At the old interior maximizer this refinement is expected to have a strictly negative extra exponential rate. The precise quantitative statement is currently **CONDITIONAL** on completing that finite type count and certifying the new global maximum. I do not claim an endpoint improvement from interior positivity alone.

## 6. An explicit variational toy model: the rescue penalty is large enough to matter, but not enough by itself

To test the mechanism before rebuilding the full Diaz polytope, I derived an unconditioned first-moment EGF model.

Fix an assignment with true fraction `p`, and designate a fraction `u` of all variables as true zero-blocking roots. For a random signed proper clause relative to this assignment:

- unsatisfied clauses have probability `1/8` and are forbidden;
- satisfying noncritical clauses have probability `1/2`;
- a given variable is the unique satisfied variable of a critical clause with probability `3/(8n)`.

Let `s>0` be the coefficient saddle and put `x=3s/8`. Root boxes require critical degree zero; non-root true boxes require positive critical degree. Among false boxes, a singleton critical box is a potential rescue child when at least one of the two other variables in its blocking clause belongs to the root set. At exponential scale this probability is

\[
c(u)=1-(1-u)^2=2u-u^2.
\]

If `gamma` is the fraction of false variables selected as such children, then before the score penalty the exponent is

\[
\begin{aligned}
F_0(p,u,\gamma;s)=&\ H(p)+pH(u/p)+\alpha\log\alpha-\alpha+s/2-\alpha\log s\\
&+(p-u)\log(e^x-1)\\
&+(1-p)H\!\left(\frac{\gamma}{1-p}\right)
+\gamma\log(c(u)x)\\
&+(1-p-\gamma)\log(e^x-1-c(u)x).
\end{aligned}\tag{6.1}
\]

When each child chooses one encountered root symmetrically, the root occupancies have the usual multinomial exponential generating function. Equation (4.2) replaces the ordinary occupancy EGF `e^y` by

\[
A(y)=\sum_{r\ge0}\frac{y^r}{r!(r+1)}=\frac{e^y-1}{y}.
\]

The exact exponential score-averaging correction for child density `gamma` and root density `u` is therefore

\[
\psi(\gamma,u)
=\gamma\log(\gamma/u)-\gamma
+\inf_{y>0}\{u\log A(y)-\gamma\log y\}.\tag{6.2}
\]

The diagnostic variational exponent is

\[
\Phi_\alpha^{\rm rescue}
=\sup_{p,u,\gamma}\inf_{s>0}
\{F_0(p,u,\gamma;s)+\psi(\gamma,u)\}.\tag{6.3}
\]

I executed a deterministic multi-start floating optimization of (6.3), together with the same model with `psi=0`. This is **not** an interval/global certificate and is not used as a theorem. The output is archived verbatim.

At the rigorous source upper endpoint the best local values found were

\[
\Phi_{4.4898}^{\rm rescue}\approx0.003113528916,
\qquad
\Phi_{4.4898}^{\rm no\ pair}\approx0.015135215438.
\]

So the two-flip score penalty buys about

\[
0.01202168652
\]

in exponential rate in this stripped model. However the rescued exponent is still positive at `4.4898`, so the toy model **does not** improve the source bound. The local numerical crossing is near `4.5245`, still worse than `4.4898`. This is a decisive route comparison: the rescue constraint is strong, but it must be grafted onto the Poisson-degree / impure-core / positive-unbalance restrictions of Diaz rather than used alone.

## 7. A tempting margin-transfer shortcut fails for an exact reason

The Diaz conditional first-moment calculation at `4.4898` has the tiny exponential base

\[
q_0=(1+10^{-7})0.9999998965
=0.9999999964999897,
\]

with rate `-log q0≈3.5000103e-9`.

A tempting argument is: if the *full* satisfiability probability at density `alpha_0` were bounded by `q_0^n`, then coupling a lower-density formula with `delta n` extra random clauses and following one canonical satisfying assignment would give

\[
P_{\alpha_0-\delta}(SAT)
\lesssim q_0^n(8/7)^{\delta n},
\]

which would already allow any

\[
\delta<\frac{-\log q_0}{\log(8/7)}
\approx2.6211\times10^{-8}.
\]

That would produce a tiny explicit source improvement almost for free. It is **not valid from the published proof as written**. Proposition 2.3 controls the pure-literal-core degree sequence only with error `O(beta^{sqrt(n)})`, and the final proof of Theorem 1.1 consequently has a subexponential exceptional term. The exponentially small conditional count in Lemma 2.5 is therefore not an exponential upper bound for the full SAT probability. A linear-density downward coupling would multiply the exceptional term by `exp(Theta(n))` and loses all control.

I record this failed shortcut because it is easy to make the wrong inference from equation (21). No bound such as `4.489799975` is claimed.

## 8. What is proved, what is conditional, and what remains

### PROVED in this run

**T04-RESCUE-STAR-01.** For any satisfying assignment, every clean rescue edge gives a satisfying two-step path. For an iid continuous positive-score maximum, each edge forces `W_child<=W_root`; a rescue star with `r` children contributes exact score probability `1/(r+1)`. In the Diaz light degree cap `M=23`, `E` clean rescue edges contribute at most `exp[-(log2/23)E]` after averaging over scores.

This theorem is deterministic except for the elementary iid-score averaging identity and is independently checked at the local clause truth-table level by the archived script.

### CONDITIONAL / incomplete

**T04-DIAZ-RESCUE-REFINEMENT-02.** The old `M=23` first-moment polytope can be finitely refined by root/blocking/rescue-star types, and its old interior critical type has positive rescue density. The expected consequence is a strict decrease of the Diaz exponent. The missing work is the explicit refined multinomial functional, collision bookkeeping, and certified global maximization at a density **strictly below** `4.4898`.

No cavity/replica prediction is being used as proof.

## 9. Next attack

The next run should not spend time on another toy count. It should build the finite Diaz-compatible refinement directly:

1. split each `t_{i,j}` by the number of `ps` occurrences that are blocking; retain the zero-blocking class as roots;
2. retain `f_{i,j,1}` children separately;
3. split blocking clause types according to `nu` slots from zero-blocking roots;
4. introduce root star counts `r=0,...,23` and multiply the count by `1/(r+1)` per star;
5. include a dirty-pair coordinate or prove its positive-density regime superexponentially negligible in the bounded-degree configuration model;
6. eliminate the added variables analytically where possible, then perform a **certified** interval/global optimization, first at `4.4898` to reproduce a strict improved margin and then at a concrete lower density.

A successful next run must report an explicit new `alpha_U<4.4898` with a checkable numerical certificate before the source metric moves.

## 10. Essential artifacts and ledger delta

Executed code:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T00-54-08Z__rescue_variational.py`

Archived output:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T00-54-08Z__rescue_variational.out`

Structured delta:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T00-54-08Z__ledger_delta.json`

No historical report, peer file, shared root ledger, POSTED entry, workflow, permission, schedule, email, Drive object, or public surface was modified.
