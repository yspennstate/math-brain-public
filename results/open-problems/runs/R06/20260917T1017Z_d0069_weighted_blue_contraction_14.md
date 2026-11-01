Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `C5: 3/5 -> 4/5`; methods #11 DUALIZE, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.**

# R06 CLOSABLE OUTSIDE — D0069 weighted-blue contraction

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler mutation.

## 1. Continuity and source scope

I did not reopen the stale prompt target I0056. Its authoritative R06 handoff already reached the six-unchanged-run rotation threshold with the frozen regular/co-regular `H_{5,5}` interval `[sqrt(5),sqrt(5)]`, width zero. The exact Lyons--Peres Question 6.20 remains:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The preserved `f>=5` regular/co-regular result remains **PARTIAL** for that full question. The triangular/quadrangular results of Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain prior art and are not relabelled as new.

The current canonical R06 successor is instead the create-only claim `operations/claims/D0069.md`: Grimmett--Li, *Bounds on connective constants of regular graphs* / the 2017 survey Question 2.2. The source class is an infinite, connected, loopless, vertex-transitive `Delta`-regular multigraph, with parallel edge copies counted as distinct SAW choices. The source proves

`mu(G) >= sqrt(Delta-1)`

for simple graphs and for nonsimple graphs when `Delta<=4`, and explicitly asks whether the nonsimple conclusion extends to larger degree.

The frozen first unresolved degree is `Delta=5`, so the target is `mu(G)>=2`. The five nonsimple parallel-class types are

`[4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1]`.

The frozen metric is

`C5 = number of these five types for which mu(G)>=2 is proved for every graph of that type`.

The preceding report `runs/R06/20260917T0920Z_d0069_degree5_three_partitions_13.md` proved the first, second and fourth types, so the entering state was

`C5 = 3/5`, covered set `{[4,1],[3,2],[2,2,1]}`.

This run proves the entire `[3,1,1]` type, hence

`C5 = 4/5`.

Even `C5=5/5` would remain **PARTIAL** for the full Grimmett--Li question because `Delta>=6` would still remain.

## 2. Required repository and literature reread

Before new work I reread the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the latest implementation manifest, the D0069 claim, the preceding R06 report, and the newest visible neighboring R07 report. The large intake JSONL files are connector-truncated when rendered wholesale; this run therefore used exact-ID/source searches rather than falsely claiming byte-for-byte rendering of every intake file.

Fresh dated literature queries on 2026-09-17 included the exact Grimmett--Li title/question, `nonsimple multigraph connective constant degree 5`, `sqrt(Delta-1) larger degree`, `weighted self-avoiding walks matching contraction`, and recent factor-invariant cubic-graph work. The original 2012 paper still contains the explicit larger-degree question. The 2017 survey repeats it. Grimmett--Li's 2020 *Weighted self-avoiding walks* develops weighted connective/bridge constants and continuity under graph-height hypotheses, but I found no theorem there giving the degree-5 multigraph result below. Recent 2024/2026 factor-invariant cubic-graph papers classify particular invariant `2-factor + perfect-matching` structures, but the bounded search found no source-matching connective-constant theorem resolving `[3,1,1]` or the full nonsimple `Delta>=5` question.

This is a bounded negative search, not a novelty certificate. **Publication novelty remains UNVERIFIED.**

## 3. Idea before code — contract the heavy matching

Assume now that `G` has type `[3,1,1]`. The three parallel edges at each vertex go to one distinguished neighbor. Because multiplicity is automorphism-invariant, these triple-edge classes form an invariant perfect matching `M`. The two singleton edges form an invariant spanning `2`-factor.

Contract every matched pair `{x,Mx}` to one supervertex. Keep the singleton edges as edge copies. Call the quotient multigraph `Q`.

There are no loops in `Q`: a singleton edge joining `x` to `Mx` would make the multiplicity of that neighbor class at least four, contradicting type `[3,1,1]`. Each supervertex has four singleton-edge incidences, so `Q` is `4`-regular counting multiplicity. It is infinite and connected. Every automorphism of `G` preserves the unique multiplicity-three matching and therefore induces an automorphism of `Q`; vertex transitivity of `G` makes `Q` vertex-transitive.

Thus `Q` lies exactly in the degree-four class treated by Grimmett--Li. If `Q` is simple, the proof of their Theorem 4.1(a) gives condition `Pi`; if it is nonsimple, their Theorem 4.1(b) proof gives condition `Pi` because `Delta=4`. I use the stronger on-page consequence from their Theorem 4.3 proof, not merely the numerical lower bound `mu(Q)>=sqrt(3)`.

## 4. Method #25 — recover the source blue-edge inequality

Let

`pi=q_0 e_0 q_1 ... e_{L-1} q_L`, `L=2n`,

be any extendable `L`-step SAW of `Q`. In Grimmett--Li's notation, for `0<=s<L`, let `b_s` be the number of blue alternatives among the two edges at `q_s` other than the incoming and chosen outgoing edges (with their harmless artificial incoming edge at `s=0`). Their condition-`Pi` double count gives

`sum_{s=0}^{L-1} b_s >= L`.

At every genuine prefix position `1<=s<L`, the number of extendable non-reversing children of that prefix is exactly

`c_s = 1+b_s`:

the chosen continuation contributes one, and the other extendable continuations are exactly the blue edges. Since `0<=b_0<=2`, after dropping the artificial-root position we retain

`sum_{s=1}^{L-1} b_s >= L-2`.

Put `N=L-1` and let `n_j` be the number of indices `1<=s<L` with `b_s=j`. Then

`n_0+n_1+n_2=N`,

and

`n_1+2 n_2 >= N-1`,

so

`n_2-n_0 >= -1`.                                           (4.1)

This one-unit root loss is the only loss in the argument.

## 5. Method #11 — dualize the child weights at the critical point

Fix the critical SAW generating-function point

`z=1/2`.

At an intermediate quotient supervertex, the incoming singleton edge lands at one endpoint `x` of its contracted matching pair. Of the three non-reversing quotient edge copies:

- exactly one singleton edge leaves again from `x`; its lift in `G` takes one edge, so its critical weight is `1/2`;
- exactly two singleton edges leave from the mate `Mx`; to use either one, the lifted walk first crosses one of the **three** parallel matching edges and then takes that singleton edge. The three edge-copy choices therefore have total critical weight

`3*(1/2)^2 = 3/4`

for each such quotient child.

Thus the three candidate child weights are exactly

`1/2, 3/4, 3/4`.

If a prefix has `b` blue alternatives, it has `1+b` extendable children. The least possible total critical child mass is consequently

`F(0)=1/2`,

`F(1)=1/2+3/4=5/4`,

`F(2)=1/2+3/4+3/4=2`.                                  (5.1)

For a fixed extendable quotient path, (4.1) gives

`prod_{s=1}^{L-1} F(b_s)`

`>= (1/2)^{n_0} (5/4)^{n_1} 2^{n_2}`

`= 2^{n_2-n_0}(5/4)^{n_1}`

`>= 1/2`.                                                (5.2)

The important point is that this is a **pathwise** bound, not an average over sampled quotient walks.

Now dualize the extendable-SAW tree. For each extendable prefix `eta`, let

`S(eta) = sum of the critical weights of all extendable children of eta`,

and define transition probabilities

`p(eta -> eta') = w(eta,eta') / S(eta)`.

For all extendable quotient paths of a fixed depth sharing a fixed first edge, the total critical lift mass equals

`sum_paths prod w = E_p[ prod S(eta_s) ]`.

By (5.2), every path inside this expectation has product at least `1/2`. Therefore the total critical lift mass after the fixed first quotient edge is at least `1/2` at every even macro-depth.

This probability normalization is the dual certificate: it turns the source's blue/red branch count into a lower bound on weighted SAW mass without assuming that every individual prefix has many children.

## 6. Theorem R06-D0069-T2 — the full `[3,1,1]` class

**Theorem.** Let `G` be an infinite, connected, loopless, vertex-transitive `5`-regular multigraph whose parallel-class partition at every vertex is `[3,1,1]`. Then

`mu(G) >= 2`.

**Proof.** Use the quotient `Q` and the extendable-SAW tree above. Choose one extendable quotient edge `e_0` from a supervertex `q_0` to `q_1`; such an edge exists because `Q` is infinite and locally finite. Choose as the fixed starting vertex of `G` the endpoint of `e_0` inside the pair `q_0`. Taking `e_0` contributes the initial critical factor `1/2`.

For every later quotient transition, if the outgoing singleton lies at the same endpoint of the current matching pair as the incoming singleton, lift it directly. If it lies at the other endpoint, first choose one of the three parallel matching edges and then take the outgoing singleton. Because the quotient SAW visits each contracted pair at most once, every lift visits at most the two vertices of that pair, consecutively in the switch case, and can never revisit an original vertex. Every lift is therefore a genuine multigraph SAW.

Different matching-edge-copy choices are distinct SAWs, and projection back to `Q` recovers the quotient edge sequence, so no two terms in the critical mass calculation are spuriously identified.

For every even quotient length `L=2n`, Section 5 gives total critical mass at least

`(1/2)*(1/2)=1/4`

from the family of lifted `G`-SAWs projecting to extendable quotient paths of length `L` sharing `e_0`. Families belonging to different `L` are disjoint because a lifted path contains exactly `L` singleton edges, so its quotient length is recoverable from the original multigraph walk.

Hence

`sum_{m>=0} sigma_m(G) 2^{-m} = infinity`.

If `mu(G)<2`, then `z=1/2` would lie strictly inside the SAW generating function's radius of convergence `1/mu(G)`, a contradiction. Thus

`mu(G)>=2`.

This proves the entire `[3,1,1]` partition class. QED.

Consequently the frozen metric moves

`C5: 3/5 -> 4/5`,

with covered set

`{[4,1],[3,2],[3,1,1],[2,2,1]}`.

The full source question remains **PARTIAL**.

## 7. Method #14 — group action and the final `[2,1,1,1]` obstruction

The group action also yields a useful exact reduction of the only remaining degree-five type.

Assume `G` has type `[2,1,1,1]`. The unique double-edge class is an invariant perfect matching `M`, and the three singleton edges form a simple cubic spanning subgraph. Contract each matching pair. The quotient `Q` is an infinite, connected, loopless, vertex-transitive `6`-regular multigraph.

Between two contracted two-point fibers there are only four possible singleton edges, so every parallel class of `Q` has multiplicity at most four.

At `z=1/2`, the contraction is especially clean. If a quotient transition leaves from the same endpoint as the incoming singleton, its critical weight is `1/2`. If it leaves from the mate, the lift uses one of the two parallel matching edges and then the singleton, giving

`2*(1/2)^2 = 1/2`.

Therefore every quotient SAW of `n` edges contributes **exactly `2^{-n}`** in total critical lift mass, independent of how often it switches endpoints. In particular,

`mu(Q)>=2  ==>  mu(G)>=2`.                              (7.1)

This transforms the last degree-five class into a sharply constrained degree-six quotient problem.

### 7.1 Exact quotient partition screen

With total degree six and parallel multiplicity at most four, the possible local partitions of `Q` are

`[4,2], [4,1,1], [3,3], [3,2,1], [3,1,1,1], [2,2,2], [2,2,1,1], [2,1,1,1,1], [1,1,1,1,1,1]`.

Seven of these nine quotient types already force `mu(Q)>=2`:

1. `[4,2]` and `[3,3]`: the underlying simple quotient is a double ray. Consecutive multiplicities have products `8` and `9`, respectively, so the weighted line connective constants are `sqrt(8)` and `3`.

2. `[2,2,2]`: `Q` is the double of a simple cubic vertex-transitive skeleton. Grimmett--Li gives skeleton connective constant at least `sqrt(2)`, hence `mu(Q)>=2sqrt(2)>2`.

3. `[2,1,1,1,1]` and `[1,1,1,1,1,1]`: the simple skeleton has degree five or six, respectively, so the simple-graph theorem gives connective constant at least `2` or `sqrt(5)`; adding multiplicity cannot reduce SAW counts.

4. `[4,1,1]`: the multiplicity-four classes form an invariant perfect matching. Contract them. The new quotient is `4`-regular and satisfies condition `Pi`. Its three candidate critical child weights are now

`1/2, 1, 1`,

because a switch contributes `4*(1/2)^2=1`. With `b=0,1,2` blue alternatives, the minimum child masses are

`1/2, 3/2, 5/2`.

The same source inequality gives `n_2-n_0>=-1`, and therefore

`(1/2)^{n_0}(3/2)^{n_1}(5/2)^{n_2} >= 1/2`.

The same normalized-tree argument proves `mu(Q)>=2`.

5. `[3,2,1]`: the multiplicity-three and multiplicity-two edge classes are two invariant perfect matchings, and their union is a spanning `2`-factor whose components are alternating `(3,2)` cycles or double rays. If a component is a double ray, following it already gives critical edge factors alternating `3/2` and `1`, hence `mu(Q)>2`. If the components are finite cycles, the singleton classes form a perfect matching between distinct cycles; otherwise vertex transitivity and connectedness would force a finite connected component. Contract the alternating cycles and choose an infinite simple ray of components. Between distinct entry/exit ports of one alternating cycle there are two simple arcs. Every edge on either arc has critical factor at least one, and the outgoing singleton has factor `1/2`; each arc therefore contributes at least `1/2`, so the two arcs contribute at least one per quotient block. Summing over arbitrarily many blocks makes the critical generating function diverge. Hence `mu(Q)>=2`.

Thus the only degree-six quotient types not settled by this run are

`[3,1,1,1]` and `[2,2,1,1]`.                            (7.2)

Combining (7.1) and (7.2), the **only remaining obligation for the frozen degree-five metric** is:

> prove `mu(G)>=2` for `[2,1,1,1]` when its double-matching contraction has quotient type `[3,1,1,1]` or `[2,2,1,1]`, or construct an exact source-valid counterexample in one of those two residual quotient types.

This is a real reduction of the final class, not metric movement by sampling.

## 8. Exact finite self-check

Only after the proof route was complete, I added and executed the exact-arithmetic self-check

`artifacts/R06/d0069_run14_weighted_contraction_selfcheck.py`

creation commit `6d7aa6a7a40eec69665d283ce4d1f459d660b983`, with archived output

`artifacts/R06/d0069_run14_weighted_contraction_selfcheck.out`

creation commit `c3ea499b8064008ffad44199d5073208f0c63df4`.

It uses `Fraction` arithmetic and verifies exactly:

- the five degree-five nonsimple partitions;
- the local child-mass triples `(1/2,5/4,2)` and `(1/2,3/2,5/2)`;
- the finite degree-six partition list under the exact multiplicity-at-most-four constraint;
- that the seven covered quotient types leave exactly `[3,1,1,1]` and `[2,2,1,1]`;
- the elementary line and alternating-factor critical inequalities.

The output ends `EXACT_SELF_CHECK_PASS`. The loops over exponent triples are labelled self-checks only; the all-exponent product inequalities and all infinite graph arguments are proved on the page above.

## 9. Section-B outcomes

### #11 DUALIZE

**Succeeded.** Normalizing critical child weights into transition probabilities converted the Grimmett--Li blue-edge double count into a pathwise martingale/tree-mass certificate. This is what closes `[3,1,1]`; a direct fixed quotient-ray estimate was too weak.

### #14 FIND THE GROUP ACTING

**Succeeded.** Multiplicity is automorphism-invariant, so the triple/double heavy classes are canonical perfect matchings, and contraction preserves vertex transitivity. This moves the hard geometry to a degree-four quotient in `[3,1,1]` and to a degree-six quotient with multiplicity at most four in `[2,1,1,1]`.

### #25 COUNT THE SAME THING TWICE

**Succeeded.** The source blue/red incidence count gives `sum b_s>=L`; the lifted critical mass counts the same branch choices with weights. Their combination yields the exact product inequalities and the `1/4` lower critical mass at every even macro-depth.

Next unused moves for the residual `[2,1,1,1]` obstruction: **#3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED, #24 FIND THE EXTREMAL OBJECT.** In particular, the next run should attack the two residual quotient types in (7.2), not re-prove any of the four covered degree-five classes.

## 10. Neighbor audit — R07/T18

I independently checked the newest visible R07 theorem `I0077-R07-T18`, the power-sheared parabolic-tube phase theorem. The `rho<1/2` far-past clauses correctly reduce by endpoint perturbation to the source OU threshold; the seam obstruction correctly uses Brownian local `alpha`-Hölder regularity simultaneously at every finite time with `rho<alpha<1/2`, so no stopping-time assumption on the random FBM witness terminal time is needed. The `rho>1/2` far-past obstruction is consistent with the witness-Brownian normalization argument, and the critical `rho=1/2` case is correctly identified as the original parabolic theorem. The report deliberately leaves the `lambda_0=1` converse unclassified rather than inventing an endpoint theorem.

Audit verdict:

`R06-AUDIT-R07-I0077-T18-20260917T1017Z = PASS_SCOPED / NOVELTY_UNVERIFIED`.

This is an independent mathematical audit of the stated scope only; it is not a novelty certificate and does not close the open-ended Problem 7.8.

## 11. Model / scheduler control status

The limitation requested by the owner is still present. The exposed task-control interface offers prompt/title, schedule, timing mode and enabled state, but **no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution control**. GPT-6 / maximum is therefore prompt text only in this task. I report the actually exposed run identity as GPT-5.6 Sol / reasoning UNVERIFIED and do not claim otherwise.

The implementation manifest records a historical P26 update attempt returning `You cannot modify this task`; the root reconciliation also records that P26 was later successfully updated from a different authorized context. The legitimate route for protected-task changes is the owning/authorized admin context or platform support. Enforcing GPT-6/maximum would require the scheduler/product backend to expose model and reasoning fields together with authenticated run telemetry. This run did not attempt a permission bypass, duplicate task, or scheduler mutation.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  run_id: 20260917T1017Z_d0069_weighted_blue_contraction_14
  source: "Grimmett--Li, Bounds on connective constants of regular graphs / survey Question 2.2, D0069"
  lane: CLOSABLE_OUTSIDE
  frozen_degree: 5
  metric: C5
  metric_before: "3/5"
  metric_after: "4/5"
  covered_before:
    - "[4,1]"
    - "[3,2]"
    - "[2,2,1]"
  covered_after:
    - "[4,1]"
    - "[3,2]"
    - "[3,1,1]"
    - "[2,2,1]"
  status: PARTIAL
  unchanged_count: 0
  tried_moves: [11, 14, 25]
  theorem_ids:
    - R06-D0069-T2
  remaining_obligation: "[2,1,1,1]; after double-matching contraction it is enough to settle quotient types [3,1,1,1] and [2,2,1,1], or give an exact source-valid counterexample there"
  exact_evidence:
    - "artifacts/R06/d0069_run14_weighted_contraction_selfcheck.py @ 6d7aa6a7a40eec69665d283ce4d1f459d660b983"
    - "artifacts/R06/d0069_run14_weighted_contraction_selfcheck.out @ c3ea499b8064008ffad44199d5073208f0c63df4"
  audit_ids:
    - "R06-AUDIT-R07-I0077-T18-20260917T1017Z=PASS_SCOPED/NOVELTY_UNVERIFIED"
  prior_art_status: "bounded dated search found no source-matching resolution; novelty UNVERIFIED"
  next_moves: [3, 12, 24]
```

No shared root, peer file, email, Drive object, public post, permission setting, or scheduler configuration was modified in this run.
