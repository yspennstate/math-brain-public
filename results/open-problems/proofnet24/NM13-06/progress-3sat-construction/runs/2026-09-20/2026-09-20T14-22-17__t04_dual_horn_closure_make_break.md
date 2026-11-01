Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-effort telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: exact flip-closure normal form and make-minus-break repair rule

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with independent fair signs on three distinct variables**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, separately from mechanism progress

The directly auditable explicit-decimal published bracket remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability with high probability below `3.52` by a constructive degree-based algorithm. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at `4.4898`. The March 2026 Cambridge status paper still states that for fixed small `k`, including `k=3`, even existence of one uniform limiting threshold is unresolved. It also states that interpolation yields a rigorous variational upper bound matching the 1RSB prediction; the quoted numerical physics value is `d_sat(3)≈12.801`, i.e. `alpha≈4.267`, but this run did not recover an independently interval-certified decimal evaluation of that variational functional. I therefore keep the explicit theorem-number metric fixed rather than silently promote a physics decimal.

Thus the **external explicit source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

Companion NM13-13's latest report on current `master`, `2026-09-20T11-12-00Z__t04_direct_product_gauss9_4388865_upper.md`, records **CANDIDATE_FULL pending later independent review** for a fixed-count upper endpoint `4.388865`. Hence the internal project-candidate bracket is `[3.52,4.388865]`, but I do not relabel that as externally certified.

This run makes no source-threshold endpoint claim. It does make a structural correction and a new exact reduction that materially changes the constructive route: the previous “repair menus must be pairwise resource-disjoint” surrogate was far too restrictive. For the clauses that actually generate ordinary repair-tree cascades, arbitrary unions of repairs remain satisfying. The true global obstruction is only the interaction with clauses that had two or three true literals under the reference assignment.

## 1. Compact handoff: what is preserved and what is not repeated

The preceding majority-repair line established:

- with `P,N iid Pois(mu)`, `mu=3 alpha/2`, `Z=min(P,N)`, `M=max(P,N)`, the false-occurrence fraction under the literal-majority assignment is `q=E Z/(2 mu)`;
- a variable reached through a false occurrence has the `Z`-Palm law, and its initial break count is `B|Z,M ~ Bin(M,q^2)`;
- minimum-break repair trees are locally subcritical throughout the explicit source bracket, and the initial blocked-majority hypergraph is also subcritical;
- independent one-shot zero-break thinning leaves a positive linear residual bad-clause density;
- finite repair menus are locally abundant, while simultaneous globalization was unresolved;
- the previous run's fresh-label two-menu surrogate gave a branching number `C_2=2uS_*^2` crossing near `3.5806856` when **any shared resource label was declared a conflict**.

The separate four-spectrum line obtained exact unit-cascade drifts, a polarity-refinement theorem and an adjoint compiler, but it has not yet produced a certified terminal 2-SAT margin above `3.52`; naive full sparse integration was not usable.

The present run does not tune either old calculation. Instead it returns to the exact Boolean semantics of “flip variables relative to majority” and derives the correct global closure structure.

## 2. Exact four-type normal form relative to an arbitrary reference assignment

Fix any 3-CNF formula `Phi` and any reference assignment `sigma_0` (later, the literal-majority assignment). For each variable `v`, introduce

\[
x_v=\mathbf 1\{\text{the final assignment flips }v\text{ relative to }\sigma_0\}.
\]

For a clause `C`, let `T_C` be the variables whose literals are true under `sigma_0`, and `F_C` those whose literals are false. A literal initially false becomes true exactly when its variable is flipped; a literal initially true remains true exactly when its variable is not flipped. Therefore `C` is satisfied after the flip set `X={v:x_v=1}` iff

\[
\boxed{
\bigvee_{v\in F_C}x_v\ \vee\ 
\bigvee_{v\in T_C}\neg x_v.
}
\tag{2.1}
\]

For a 3-clause there are exactly four semantic types, indexed by `j=|T_C|`:

\[
\begin{array}{c|c|c}
 j & \text{name} & \text{constraint in flip variables}\\ \hline
0&A&x_1\vee x_2\vee x_3,\\
1&B&\neg x_t\vee x_f\vee x_g,\\
2&C&\neg x_s\vee\neg x_t\vee x_f,\\
3&D&\neg x_1\vee\neg x_2\vee\neg x_3.
\end{array}
\tag{2.2}
\]

The executed truth-table checker exhausts all `8 x 8` reference/flip patterns and verifies (2.1). It also verifies the closure statements below exactly.

## 3. The missing structural fact: A/B satisfaction is closed under unions

### Proposition 3.1 — union closure of the repair-tree subsystem

Let `Psi_AB` be any CNF consisting only of type-A and type-B clauses from (2.2). If flip sets `X` and `Y` both satisfy `Psi_AB`, then `X union Y` also satisfies `Psi_AB`.

#### Proof

A type-A clause is monotone positive. If `X` hits its three-variable set, then so does every superset, in particular `X union Y`.

For a type-B clause

\[
\neg x_t\vee x_f\vee x_g,
\tag{3.1}
\]

suppose for contradiction that `X union Y` violates it. Then `t in X union Y` while `f,g notin X union Y`. Whichever of `X,Y` contains `t` contains neither `f` nor `g`, and therefore itself violates (3.1), contradiction. QED.

Equivalently, the A/B subsystem is dual-Horn and its satisfying flip sets are closed under bitwise OR.

### Corollary 3.2 — repair trees for different bad roots do not intrinsically conflict

Suppose every initially unsatisfied A-clause `R` is assigned a flip set `X_R` that satisfies **all A/B clauses it touches and recursively repairs every B-clause it activates**. Then

\[
X=\bigcup_R X_R
\]

still satisfies every A/B clause. In particular, two repair trees may share variables, overlap clauses, or merge completely without creating an A/B violation merely because of that overlap.

This directly corrects the interpretation of the preceding fresh-label selector surrogate. The numerical crossing near `3.5806856` remains correct **for that deliberately disjoint resource-packing model**, but it is not an obstruction to the actual majority-repair process: declaring any shared variable to be a conflict throws away the exact union closure of the clause types that generate the ordinary repair cascade.

The exact checker finds the sharp boundary: type `j=0` and `j=1` are union-closed, while `j=2` and `j=3` are not. For example, for the C-clause with truth pattern `(0,1,1)`, the two satisfying flip vectors `(0,0,1)` and `(0,1,0)` have union `(0,1,1)`, which violates the clause; similarly a D-clause can be violated by unioning two individually satisfying flip sets.

## 4. Exact closure/avoidance reduction for the full 3-CNF

The union-closure observation can be sharpened to an exact deterministic characterization.

For every A-clause choose one of its three variables as a **seed**. For every B-clause `not x_t or x_f or x_g`, choose one of its two initially-false variables, denoted `h(C) in {f,g}`, as its **orientation**. Given all these choices `pi`, define `K_pi` to be the least variable set satisfying:

1. every chosen A-seed lies in `K_pi`;
2. for each oriented B-clause, `t in K_pi` implies `h(C) in K_pi`;
3. for each C-clause `not x_s or not x_t or x_f`, `{s,t} subset K_pi` implies `f in K_pi`.

This is a monotone closure operator. A fixed `pi` can be closed by a queue: B-rules are one-input implications, C-rules fire when their two antecedents have entered. The closure is computable in time linear in the formula size after incidence lists are built.

### Theorem 4.1 — exact seed/orientation closure criterion

The original formula `Phi` is satisfiable iff there exists a choice policy `pi` such that the least closure `K_pi` contains no complete D-clause, i.e.

\[
\boxed{
\forall D,\qquad D\not\subseteq K_\pi.
}
\tag{4.1}
\]

#### Proof: policy implies satisfying assignment

Take the final flip set to be `K_pi`. Every A-clause is satisfied because its chosen seed is present. For a B-clause, if its initially-true variable `t` is absent then `not x_t` satisfies it; if `t` is present, rule 2 puts the chosen false endpoint `h(C)` into the closure, satisfying it. For a C-clause, if one of its two initially-true variables is absent then a negative literal satisfies it; if both are present, rule 3 inserts its initially-false endpoint. Finally every D-clause is satisfied by (4.1), because not all three of its variables are flipped. Thus `K_pi` satisfies every clause.

#### Proof: satisfying assignment implies policy

Conversely, let `X` be any satisfying flip set. For each A-clause select as its seed any member of `X` in that clause; such a member exists because `X` satisfies A. For each B-clause whose true endpoint `t` lies in `X`, satisfaction guarantees that at least one of its two false endpoints is also in `X`; orient the B-clause to such an endpoint. If `t notin X`, orient arbitrarily.

I claim `K_pi subseteq X`. This follows inductively during closure: all seeds were chosen in `X`; every fired B-rule points to an endpoint chosen in `X`; and if a C-rule fires, both of its true endpoints lie in `K_pi subseteq X`, so satisfaction of that C-clause forces its false endpoint to lie in `X` as well. Therefore the entire least closure is contained in `X`. Since `X` satisfies every D-clause, it contains no D-clause completely, and neither can `K_pi`. QED.

### Consequence

The global constructive problem is **not** “pack disjoint repair trees.” It is exactly:

- choose one seed in every A-clause;
- choose one outgoing child for every activated B-clause;
- accept all deterministic C-promotions;
- keep the resulting monotone closure from swallowing all three variables of any D-clause.

This is a substantially smaller obstruction. A/B overlap is harmless; C-promotions and D-forbidden triples are the only source of non-union behavior.

## 5. A local control rule that rewards merged repairs: minimize break minus make

The previous repair tree chose the candidate variable with minimum break count `B`. Once overlaps are recognized as useful rather than forbidden, that local objective is incomplete because flipping one variable can repair several currently unsatisfied clauses at once.

For any current assignment define for a variable `v`:

- `A_v`: number of currently unsatisfied clauses incident to `v` (so the literal of `v` is currently false in each);
- `B_v`: number of currently uniquely satisfied clauses whose unique true literal is the literal of `v`.

### Proposition 5.1 — exact one-flip energy identity

If `U` is the number of unsatisfied clauses, then flipping `v` changes it by

\[
\boxed{U_{\rm after}-U_{\rm before}=B_v-A_v.}
\tag{5.1}
\]

#### Proof

Every currently unsatisfied clause incident to `v` becomes satisfied, contributing `-A_v`. A currently satisfied clause becomes unsatisfied iff the literal of `v` was its unique true literal, contributing `+B_v`. No other clause changes satisfaction status. QED.

Thus a natural repair rule at an unsatisfied root is to choose the candidate minimizing

\[
D_v:=B_v-A_v,
\tag{5.2}
\]

not merely `B_v`. The difference matters precisely because shared repairs are beneficial: `A_v>1` means one flip simultaneously absorbs several A-roots.

## 6. Exact local weak-limit law at the majority start

Return now to iid random proper 3-SAT and the literal-majority reference assignment. Put

\[
P,N\stackrel{\rm iid}{\sim}{\rm Pois}(\mu),\qquad
\mu={3\alpha\over2},\qquad
Z=\min(P,N),\quad M=\max(P,N),
\tag{6.1}
\]

and

\[
q={\mathbb EZ\over2\mu}.
\tag{6.2}
\]

A variable reached through a false literal has the false-occurrence Palm law

\[
\Pr_F(Z=z,M=m)={z\Pr(Z=z,M=m)\over\mathbb EZ}.
\tag{6.3}
\]

Condition on `(Z,M)=(z,m)` for a candidate variable in an initially unsatisfied A-clause. The root consumes one false occurrence. In the local tree limit, each of the remaining `z-1` false occurrences belongs to another A-clause exactly when its two other literals are false, probability `q^2`; each of the `m` true occurrences belongs to a B-clause exactly under the same two-neighbor event. Distinct incident clause neighborhoods are asymptotically disjoint. Hence

\[
\boxed{
A=1+{\rm Bin}(Z-1,q^2),\qquad
B={\rm Bin}(M,q^2),
}
\tag{6.4}
\]

with conditional independence given `(Z,M)`.

For the three distinct variables of an A-root, the three Palm pairs are asymptotically iid. Therefore the initial make-minus-break greedy rule has local drift

\[
\boxed{
\delta_{MB}(\alpha)=\mathbb E\min_{1\le i\le3}(B_i-A_i).
}
\tag{6.5}
\]

This is a local weak-limit theorem, not a claim that repeatedly applying the rule sees fresh copies of (6.4). C/D activation and degree depletion change the environment after the first wave.

## 7. Executed calculation

The reusable checker is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T14-22-17__union_make_break.py`

created at commit `f1c6d17fe07a46b9611a4b8d064e0c5a95b3910f`. Its actual output is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T14-22-17__union_make_break.out`

created at commit `877d7376892915fa75e0222837b27d7358849d9d`.

The exact portion exhaustively checks all flip truth tables and verifies A/B union closure plus explicit C/D nonclosure witnesses. The numerical portion truncates `P,N<=45`, uses ordinary IEEE double arithmetic, and repeats at cutoff `40`; all displayed scalar diagnostics are unchanged at the shown precision. These decimals are therefore **high-precision mechanism diagnostics, not outward-rounded interval certificates**.

The key values are

\[
\begin{array}{c|c|c|c|c}
\alpha&q&\delta_{MB}&E[A\mid MB]&E[B\mid MB]\\ \hline
3.52&0.378714713369405&-1.47467826881464&1.91647965641605&0.441801387601404\\
3.60&0.380036729791158&-1.48238343365564&1.94262805513647&0.460244621480841\\
4.4898&0.392321936451921&-1.56108556213028&2.23575544066830&0.674669878538030
\end{array}
\tag{7.1}
\]

At `alpha=3.6`, the old minimum-break root rule has expected net change

\[
E[B-A\mid\text{min-}B]=-1.22754132124461,
\]

whereas minimum make-minus-break gives

\[
\boxed{-1.48238343365564},
\]

a local improvement of

\[
\boxed{0.254842112411027}
\tag{7.2}
\]

unsatisfied clauses per first repair flip in the fresh local limit.

The distribution is also strongly favorable at the first step. At `alpha=3.6`, only

\[
\Pr\{\min_i(B_i-A_i)\ge0\}\approx0.1003637943
\tag{7.3}
\]

of A-roots lack a strictly decreasing candidate, and only

\[
\Pr\{\min_i(B_i-A_i)>0\}\approx0.00549622695
\tag{7.4}
\]

have all three candidates strictly worsening.

For context, the initial majority clause-type densities per variable at `alpha=3.6` are

\[
(c_A,c_B,c_C,c_D)
\approx
(0.1975964864,\ 0.9670320336,\ 1.5775431555,\ 0.8578283246).
\tag{7.5}
\]

Thus there is no shortage of C/D constraints: the fact that the first make-minus-break step is very favorable does not imply the process can be iterated with the same law.

## 8. What moved mathematically, and what did not

### Demonstrated mechanism gains

1. **Exact global normal form.** Relative to the majority assignment, random 3-SAT becomes an A/B/C/D flip-CNF with A/B dual-Horn union closure, C pair-promotions, and D forbidden triples.
2. **Exact closure criterion.** Satisfiability is equivalent to choosing A-seeds and B-orientations whose least B/C closure avoids every D triple. This is a deterministic iff theorem, not a simulation.
3. **Prior obstruction narrowed.** The previous `alpha≈3.5806856` all-resource collision transition is not an obstruction to actual repair-tree merging; it only rules out a deliberately disjoint packing proof architecture.
4. **Better local objective.** The exact identity `Delta U=B-A` yields a make-minus-break rule. Its initial local-tree gain over min-break at `alpha=3.6` is about `0.254842` clauses per first flip, and the expected first-step drift is strongly negative.

### What did not move

No repeated-process coupling, no C/D-safe closure theorem, no terminal 2-SAT criterion, and no source-level threshold `alpha>3.52` has been proved. The numerical local drift remains only a first-wave mechanism diagnostic. It would be invalid to iterate (6.4) as though the environment refreshed independently after every flip.

## 9. Residual obstruction and next decisive attack

The right global object is now much more specific than a Hall packing of whole repair trees. Fixing A-seeds and B-orientations produces a monotone bootstrap closure with one-input B rules and two-input C rules; failure occurs only when that closure captures all three vertices of a D-hyperedge.

The next constructive attack should therefore track **D-danger rather than generic overlap**. A minimal state evolution at `alpha=3.6` should distinguish:

- A-demand removed by a flip (`make`);
- activated B one-input obligations (`break`);
- C clauses with zero, one, or two selected true endpoints, the last state forcing a promotion;
- D clauses with zero, one, or two selected vertices, the last state making a third vertex forbidden.

A candidate controller is the exact make-minus-break score augmented only by the incremental number of C-promotions and D-two-hit hazards. The decisive goal is to derive and interval-integrate this finite state system and show that all A-demand reaches zero while the D-three-hit density remains zero, first at `alpha=3.6`. If the D hazard necessarily becomes positive before A-demand vanishes, the majority-repair family has a concrete structural obstruction and should be retired; if it stays zero with margin, the resulting process is a genuine route to an improved constructive lower bound.

## 10. Literature/status scope

Bounded fresh checks this run covered Hajiaghayi--Sorkin (`3.52` constructive lower bound), Díaz--Kirousis--Mitsche--Pérez-Giménez (`4.4898` explicit UNSAT upper bound), the March 2026 Cambridge fixed-small-`k` status paper, and Carenini's August 2026 fixed-`k` scaling-window theorem. The latter narrows the window but does not locate the `k=3` center; large-`k` threshold theorems and k-wise-independent variants are not used as closure. `POSTED.md` was checked for exclusions; no posted T04 claim was reopened.

## ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  parent: T04
  status: OPEN/PARTIAL
  source_model: classical iid uniform signed proper 3-SAT
  source_metric:
    name: explicit published satisfiability-threshold bracket
    before: "[3.52, 4.4898]"
    after: "[3.52, 4.4898]"
    width_before: 0.9698
    width_after: 0.9698
    movement: none
  companion_candidate:
    worker: NM13-13
    endpoint: 4.388865
    status: CANDIDATE_FULL pending later independent review
  substantive_advance:
    theorem_1: "A/B flip-clause satisfaction is closed under unions"
    theorem_2: "Phi is satisfiable iff some A-seed/B-orientation policy has D-free least B/C closure"
    exact_identity: "one flip changes unsatisfied count by B_v-A_v"
    alpha_3_6_local_make_break_drift: -1.48238343365564
    alpha_3_6_old_min_break_net_drift: -1.22754132124461
    alpha_3_6_local_gain: 0.254842112411027
  correction_to_previous_obstruction:
    prior_value: "fresh-label disjoint two-menu branching crossed near 3.5806856"
    retained_scope: "valid only for surrogate declaring any resource overlap a conflict"
    new_scope: "not an obstruction to actual A/B repair merging because A/B solutions are union-closed"
  numerical_status: "high-precision finite Poisson truncation; not interval-certified"
  residual_obstruction: "control C pair-promotions and avoid complete D triples during monotone closure"
  next_attack: "derive finite C/D-danger state evolution for make-minus-break controller at alpha=3.6 and interval-certify it"
  artifacts:
    code: "proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T14-22-17__union_make_break.py"
    code_commit: f1c6d17fe07a46b9611a4b8d064e0c5a95b3910f
    output: "proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T14-22-17__union_make_break.out"
    output_commit: 877d7376892915fa75e0222837b27d7358849d9d
```
