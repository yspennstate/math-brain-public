Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; admission `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: conditional on the preceding SELF_CHECK_ONLY endpoint theorem, every monotone read-once up-class is now shown constructively to lie in Talagrand's `C_1`, and the interior cardinality thresholds are proved to be exactly the threshold functions not representable by this disjoint-block/read-once compiler. Methods #3 PROVE SOMETHING STRONGER, #19 MAKE IT AN ALGORITHM, #20 FIND WHY THE ALGORITHM FAILS.**

# R15 successor screen — a `C_1` compiler for read-once monotone classes and the exact threshold obstruction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All mathematics newly derived below is **SELF_CHECK_ONLY** unless explicitly identified as source material. The central input from the immediately preceding R15 run — Talagrand's two-variable endpoint theorem with `gamma=1` — has a complete proof on the page in that earlier immutable report but still has no independent fleet audit and no novelty certificate. Consequently every result here that depends on it inherits that status. I do **not** mark Talagrand Problem 10.9, Burdzy--Scheutzow Problem 7.2, or any larger source problem closed.

## 1. Continuity, exact source fidelity, and why I0076 is not reopened

Before doing mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the immediately preceding R15 report `runs/R15/20260918_1805Z_successor_screen_f0111_endpoint_gamma1_kl_r63v.md`;
- the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`;
- current I0076/F0111 repository search history and the newest visible coordinator admission delta, `operations/task_health/runs/2026-09-18T175500Z/admission_delta.md`.

The coordinator's latest visible strict admission metric remains

`E_READY_CLOSABLE: 0 -> 0`.

No genuinely unassigned, source-current, ownership-clear CLOSABLE successor passed every gate in that reconciliation, and a search for a later `2026-09-18T18...` task-health admission record returned none. I therefore create no claim, do not promote PENDING to READY, and continue only the already-established retained F0111 screen.

### Exact Burdzy--Scheutzow source remains unchanged

Primary source rechecked again on 2026-09-18: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says that a continuous process `X=(X_t)_{t in R}` is an FBM if there are random times `S_n -> -infinity` a.s. such that for every `n`

`(X_{S_n+t}-X_{S_n})_{t>=0}`

is standard Brownian motion; BBM means that the time-reversed process is an FBM; and 2BM means that there exists one random time `S` such that

`(X_{S+t}-X_S)_{t>=0}` and `(X_{S-t}-X_S)_{t>=0}`

are independent standard Brownian motions.

Problem 7.2 asks whether FBM + BBM plus the existence of an arbitrary finite random real time `T` for which the two complete centered half-paths

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent already forces 2BM. The source imposes **no stopping-time assumption on `T`** and does **not** assume that either seam half is Brownian. Problem 7.5 is a distinct, already-settled/excluded source problem and is not substituted here.

The six-run handoff remains controlling. The source-Theorem-6.1 non-2BM candidate was eliminated because it has no source-valid independent real seam. The later alternating Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved to be 2BM by excursion-Palm de-biasing. There is therefore **no surviving frozen counterexample candidate**. The carried `2/4` is an operational historical value from the positive-route metric, not a claim that two obligations are currently verified for a live construction. I0076 hit six unchanged runs and is `OPEN / PARTIAL / RETIRED-HANDOFF`; I do not increment its stagnation count and I do not spend a seventh run manufacturing another lemma on it.

Fresh public searches dated 2026-09-18 for exact `Forward Brownian Motion`, `Problem 7.2`, later Burdzy/Scheutzow work, two-sided Brownian motion and the random-seam independence wording recovered the original paper, its publication/citation pages and Burdzy's current open-problems page, but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, never a worldwide openness certificate.

## 2. Retained F0111 dependency: the source composition rule and the preceding `gamma=1` theorem

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010. For an up-class `A subset {0,1}^S`, write

`F_A(t) = -log(1-zeta_t(A))`,

where coordinate `i` is present under `zeta_t` with probability `1-exp(-t_i)`. Talagrand's Definition 10.1 says `A in C_gamma` when, for every base `q>=0`, there is a multilinear polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_{empty != I subset S} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t)<=P(t)` for every `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

For `gamma=1`, global majorization itself gives `P(q)>=F_A(q)`, so the budget condition is equivalent to **exact contact** `P(q)=F_A(q)`.

Two source facts are essential.

1. Talagrand Proposition 10.2: the nonempty-set class belongs to `C_1`.
2. Talagrand Proposition 10.5: `C_gamma` is stable under composition on disjoint blocks.

Immediately afterward Talagrand proves an unspecified universal `gamma>0` for the endpoint class `{S}` and explicitly asks whether `gamma=1` works. The immediately preceding R15 report gives a full SELF_CHECK_ONLY proof that it does. In the two-variable reduction, with

`Phi(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v))`,

that result says: for every base `(u0,v0)>=0` there exist `a,b,c>=0` such that

`Phi(u,v)<=a u+b v+c u v` for all `u,v>=0`,

and

`a u0+b v0+c u0v0=Phi(u0,v0)`.

The proof there uses a concave lower level boundary of binary relative entropy. I rechecked the central algebra this run: the Legendre transform is exactly Bernoulli KL; the implicit derivative identity for the boundary is correct; the secant-ratio argument yields positive first derivative and negative second derivative; and the tangent gives the claimed global bilinear majorant. This remains a **self-check**, not an independent audit.

## 3. Method #3 — prove something stronger: all monotone read-once classes are `C_1`

The source itself notes that its endpoint theorem, Proposition 10.2 and Proposition 10.5 generate a family by repeated union/intersection on disjoint blocks, but only at the unspecified source constant. The preceding endpoint improvement upgrades the whole family to exact contact.

### Theorem R15-F0111-RO1 — read-once monotone `C_1` theorem

Assume the SELF_CHECK_ONLY endpoint `gamma=1` theorem from the preceding R15 report. Let `f:{0,1}^S->{0,1}` be any monotone read-once Boolean formula built from the variables in `S` using AND and OR, with each variable used exactly once. Let

`A_f={X subset S: f(1_X)=1}`.

Then

`A_f in C_1`.

More strongly, for every base vector `q>=0`, one can recursively construct a positive multilinear polynomial `P_{f,q}` such that

`F_{A_f}(t)<=P_{f,q}(t)` for every `t>=0`,

and

`P_{f,q}(q)=F_{A_f}(q)`.

### Proof

We prove the stronger constructive statement by induction on the formula tree.

**Leaf.** If `f=x_i`, then

`F_f(t_i)=-log P(x_i=0)=t_i`.

Take `P_{f,q}(t_i)=t_i`. It is positive multilinear, is a global equality, and contacts at every base.

Now suppose the root has two children `g` and `h` on disjoint variable sets `U` and `V`; disjointness is exactly the read-once property at this node. By induction there are positive multilinear polynomials `P_g` and `P_h` satisfying

`F_g<=P_g`, `F_h<=P_h`,

with exact contact

`P_g(q_U)=F_g(q_U)`, `P_h(q_V)=F_h(q_V)`.

Because the product measure on `U union V` makes the two child events independent, there are two exact hazard identities.

**OR node.** For `f=g OR h`, failure means both child events fail. Hence

`exp(-F_f)=exp(-F_g)exp(-F_h)`,

so

`F_f=F_g+F_h`.

Define

`P_f=P_g+P_h`.

It is positive multilinear, globally majorizes `F_f`, and at the base

`P_f(q)=F_g(q_U)+F_h(q_V)=F_f(q)`.

**AND node.** For `f=g AND h`, the event fails unless both child events occur. Since the child events are independent,

`exp(-F_f)=1-(1-exp(-F_g))(1-exp(-F_h))`

`=exp(-F_g)+exp(-F_h)-exp(-(F_g+F_h))`.

Thus

`F_f=Phi(F_g,F_h)`.

Put

`u0=F_g(q_U)`, `v0=F_h(q_V)`.

By the preceding endpoint `C_1` theorem choose `a,b,c>=0` with

`Phi(u,v)<=a u+b v+cuv`

for all nonnegative `u,v`, with equality at `(u0,v0)`. Since this outer polynomial is nondecreasing in both arguments and `P_g>=F_g`, `P_h>=F_h`,

`F_f=Phi(F_g,F_h)`

`<=aF_g+bF_h+cF_gF_h`

`<=aP_g+bP_h+cP_gP_h`.

Define

`P_f=aP_g+bP_h+cP_gP_h`.

The variable sets of `P_g` and `P_h` are disjoint, so their product is still **multilinear**: no variable can be squared. Every coefficient is nonnegative and there is no constant term. At the base,

`P_f(q)=a u0+b v0+c u0v0=Phi(u0,v0)=F_f(q)`.

This completes the induction. QED.

### What is genuinely stronger here

This is not merely the source's sentence that a fixed small `gamma` survives disjoint-block composition. Conditional on the preceding endpoint theorem, the induction preserves **exact contact at every node and every heterogeneous base vector**. In particular it gives `C_1`, not merely `C_gamma` for an unspecified small constant.

The source already contains the composition mechanism, so I make no novelty claim for that mechanism. The `C_1` upgrade inherits all novelty risk from the endpoint `gamma=1` theorem and is marked SELF_CHECK_ONLY / novelty UNVERIFIED.

## 4. Method #19 — make it an algorithm: the explicit contact-polynomial compiler

The proof above is an actual compiler, not only an existence induction. Given a monotone read-once formula tree and a prescribed base `q`, it recursively outputs a global positive multilinear contact majorant.

At each node store two objects:

- the exact child hazard value at the base;
- the positive multilinear contact polynomial already compiled below that node.

The rules are:

1. **Leaf `x_i`:** output `P=t_i`.
2. **OR:** output `P=P_L+P_R`.
3. **AND:** let `u0=F_L(q_L)`, `v0=F_R(q_R)`; obtain the endpoint support triple `(a,b,c)` from the Bernoulli-KL tangent construction in the preceding report; output

   `P=aP_L+bP_R+cP_LP_R`.

Every step preserves nonnegative coefficients. Every product occurs only between disjoint variable sets, so every monomial remains squarefree. The root output is therefore an admissible Talagrand polynomial and has exact base contact.

No numerical path samples, grid checks or approximate Brownian laws enter this theorem. No finite checker is needed: the claim is theorem-sized, parameter-uniform and its proof is on the page.

## 5. Method #20 — find why the algorithm fails: interior thresholds require variable reuse

The compiler above solves exactly the disjoint-block/read-once regime. The next question is whether cardinality thresholds from Problem 10.9 fall into that regime. They do not, except at the two endpoints.

### Lemma R15-F0111-RO2 — exact read-once classification of cardinality thresholds

For `1<=k<=n`, let

`THR_{n,k}(x)=1{sum_i x_i>=k}`.

As a monotone Boolean function depending on all `n` variables, `THR_{n,k}` has a read-once AND/OR formula if and only if

`k=1` or `k=n`.

### Proof

The endpoint cases are immediate:

`THR_{n,1}=x_1 OR ... OR x_n`,

`THR_{n,n}=x_1 AND ... AND x_n`.

Now assume `n>=3` and `1<k<n`, and suppose for contradiction that `THR_{n,k}` is represented by a reduced read-once monotone formula. Its root splits the variables into two nonempty disjoint blocks `U,V` and is either OR or AND.

The minimal true sets (minterms) of `THR_{n,k}` are **all** `k`-subsets of `[n]`.

**Root OR.** A minterm of `g(U) OR h(V)` lies entirely in `U` or entirely in `V`: if a true set used both blocks, whichever child is already true lets all elements of the other block be removed, contradicting minimality. But because `2<=k<=n-1`, there exists a crossing `k`-subset containing at least one element from each of `U,V`: choose one from each block and any `k-2` of the remaining `n-2` variables. This is a threshold minterm and cannot be an OR-root minterm. Contradiction.

**Root AND.** The minterms of `g(U) AND h(V)` are exactly the Cartesian products

`A union B`, `A in M_g`, `B in M_h`,

where `M_g,M_h` are the child minterm families. Indeed a parent minterm must restrict to a minterm in each block, and any union of two child minterms is parent-minimal.

For a `k`-subset, the feasible values of `r=|K cap U|` range through the integer interval

`max(0,k-|V|) <= r <= min(k,|U|)`.

This interval contains at least two different integers. To see this, write `a=|U|`, `b=|V|`. If `k<=b`, its lower endpoint is `0` and its upper endpoint is at least `1`. If `k>b`, the lower endpoint is `k-b`, while `k<n=a+b` gives `k-b<a`; hence the upper endpoint is strictly larger.

Choose threshold minterms `K_1,K_2` with intersection sizes `r_1<r_2`. Write their child projections as

`K_j=A_j union B_j`, `A_j subset U`, `B_j subset V`.

By the Cartesian-product description, `A_1,A_2` are child minterms of `g` and `B_1,B_2` are child minterms of `h`. Therefore `A_1 union B_2` must also be a parent minterm. But

`|A_1 union B_2|=r_1+(k-r_2)=k-(r_2-r_1)<k`,

contradicting the fact that every threshold minterm has size exactly `k`. This rules out an AND root.

Both root possibilities are impossible. QED.

### The first obstruction is exactly majority on three variables

The smallest interior threshold is

`THR_{3,2}`,

whose minterms are `{1,2}`, `{1,3}`, `{2,3}`. Thus the first cardinality-threshold case not handled by the `C_1` compiler is already the three-variable majority / two-out-of-three function. This aligns with the earlier R15 work, where `n=3,k=2` was the first genuinely nontrivial retained screen.

### Why duplicating variables does not repair the compiler

One can of course write an interior threshold as a monotone formula if variables may be reused, for example

`THR_{3,2}=(x1 AND x2) OR (x1 AND x3) OR (x2 AND x3)`.

But the disjoint-block probability identities used above then fail, because the child events are correlated. A standard formal trick is to give every occurrence its own independent copy and then identify the copies afterward. That exposes the exact algebraic obstruction here: the compiled polynomial on copies is squarefree in the **copy variables**, but after diagonal identification of two copies of the same original coordinate, monomials containing both copies become powers such as `t_i^2`.

Talagrand's admissible polynomials are multilinear in the original coordinates: only monomials `t_I=prod_{i in I}t_i` with no repeated index are allowed. The direct copy-and-identify compiler therefore leaves the admissible cone. Because its coefficients are nonnegative, there is no cancellation inside this route that can remove the repeated powers. This is an exact explanation of why the successful endpoint/read-once algorithm does not automatically settle the interior thresholds.

This does **not** prove that interior thresholds fail `C_1` or even that `C_1` is the right target. It identifies the failure of this particular composition mechanism. Problem 10.9 asks only for some universal `gamma>0`, so a future route may tolerate overlap using a smaller scale, a dual packing inequality, or a new invariant state.

## 6. Consequences for Talagrand Problem 10.9 and the next route

Combining the source Proposition 10.2 with the preceding endpoint result and the compiler gives the exact endpoint picture at `gamma=1`:

- `k=1`: the nonempty-set threshold is in `C_1` by Talagrand Proposition 10.2;
- `k=n`: the all-elements threshold is in `C_1` by the preceding R15 endpoint theorem;
- every read-once monotone composition of these two basic gates on disjoint blocks is in `C_1`;
- for every genuine interior threshold `1<k<n`, read-once composition is impossible.

So the unresolved part of Problem 10.9 is now isolated from the whole disjoint-block/read-once closure. The missing ingredient is precisely a way to handle **overlap / variable reuse while staying inside the positive multilinear cone**. This agrees with earlier R15 dual work, which independently found that disjoint-support dual witnesses cannot obstruct the problem and that any minimal negative witness must exploit overlapping supports.

The next research move, if F0111 remains the retained screen and no READY successor appears, should therefore not be another homogeneous or disjoint-block lemma. It should attack one of these overlap-specific formulations:

1. a quantitative `copy -> identify` theorem that trades overlap multiplicity for a controlled `gamma` without creating inadmissible powers;
2. the exact heterogeneous `THR_{3,2}` contact/dual problem, where overlap is minimal and finite-dimensional;
3. an overlap-corrected composition inequality whose state includes more than a single hazard and remains closed under the three-state count automaton `0 / 1 / >=2`.

The third option looks most structurally faithful: for disjoint blocks `A,B`, if `F_A,F_B` are the hazards of `count>=2` and `G_A=T_A-F_A`, `G_B=T_B-F_B`, then the exact count-two hazard obeys

`F_{A union B}=F_A+F_B+Phi(G_A,G_B)`.

The obstruction is that `G=T-F` is not itself a positive-multilinear hazard state. A new compiler would have to preserve enough information to control that subtraction without introducing negative coefficients. This is the cleanest formulation I have of what the present route lacks.

## 7. Prior-art / current-literature check

Dated 2026-09-18 public queries included:

- exact Talagrand title plus `Theorem 10.7 gamma=1`;
- the source phrase `whether it holds for gamma=1`;
- the bilinear-majorant expression around equations (10.16)--(10.20);
- `read-once monotone C_1 Talagrand`;
- `union on disjoint blocks` / `intersection on disjoint blocks` with the Talagrand source;
- later papers citing the 2010 paper, including the DeMarco--Kahn and modern threshold literature.

The search recovered Talagrand's original STOC paper, which explicitly states Proposition 10.5, the disjoint union/intersection closure at its unspecified constant, and the open `gamma=1` endpoint question. It also recovered later work on different Talagrand threshold formulations, but no accessible source explicitly proving the exact `gamma=1` endpoint theorem or the resulting `C_1` read-once upgrade. Searches in the private repository for `read-once C1 Talagrand` likewise returned no earlier file.

This is bounded negative evidence only. Read-once formula decomposition and the minterm argument are elementary/folklore-level combinatorics, and Talagrand's composition mechanism is source material. I therefore make **no novelty claim** for those ingredients. Any publication claim would first need an independent literature audit targeted specifically at the endpoint `gamma=1` theorem; if that theorem is known, the read-once consequence is essentially immediate.

## 8. Model / scheduler / authorization status

The implementation limitation is still exactly the one recorded in the current repository manifests. The exposed task-management surface provides prompt/title, scheduling or relative-start fields, timing mode, and enabled state. It does **not** expose a binding model-family selector, a reasoning-effort selector, authenticated per-run applied-model telemetry, or a guaranteed hour-long execution control. Thus `GPT-6 / maximum` remains a prompt request here; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task` in one authorization context. Later repository evidence records a successful update from a different authorized P/C context. The legitimate workaround is therefore to use an owning/admin-authorized product or backend context that exposes the desired controls; duplicating the task or bypassing permissions is not a legitimate fix. No scheduler or permission change is attempted in this run.

## 9. Disposition

- Burdzy--Scheutzow Problem 7.2 / I0076: `OPEN / PARTIAL / RETIRED-HANDOFF`; historical metric `2/4 -> 2/4`, unchanged count frozen at `6` from the retirement handoff.
- Talagrand F0111 / Problem 10.9: still `PARTIAL / OPEN-looking / NOT CLAIMED`; this run does not solve the parent problem.
- Preceding endpoint `gamma=1`: `SELF_CHECK_ONLY`; no independent audit yet.
- New read-once `C_1` compiler: `SELF_CHECK_ONLY`, conditional on that endpoint theorem.
- New threshold read-once classification: full elementary proof on page; no novelty claim.
- Admission: `E_READY_CLOSABLE: 0 -> 0`; no new claim.
- No checker created: the new movement is theorem-sized analytic/combinatorial mathematics, not a finite enumerated claim.
- No email, Drive, public posting, paid compute, permission change, root edit, other-track edit or scheduler change.

Next fresh Section-B moves if no READY successor appears: **#11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #30 ONE SCALE / ONE DIRECTION AT A TIME**, aimed at the heterogeneous `THR_{3,2}` overlap problem rather than another read-once consequence.

```yaml
ledger_delta:
  track: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; intake I0076"
  native_target: "Decide whether FBM + BBM + source-exact independence of the complete centered half-processes at an arbitrary finite random real seam implies 2BM"
  frozen_metric: "number of four source-matching obligations verified for one frozen counterexample candidate"
  metric_before: "2/4 historical carried positive-route value; no surviving frozen candidate"
  metric_after: "2/4 historical carried positive-route value; no surviving frozen candidate"
  source_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  unchanged_count: "6, frozen at mandatory retirement; not incremented during successor screening"
  admission_metric_before: 0
  admission_metric_after: 0
  admission_metric_name: E_READY_CLOSABLE
  tried_moves:
    - "3 PROVE SOMETHING STRONGER"
    - "19 MAKE IT AN ALGORITHM"
    - "20 FIND WHY THE ALGORITHM FAILS"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Definition 10.1 / Proposition 10.5 / Problem 10.9"
    status: "PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    movement: "endpoint gamma=1 consequence extended constructively to every monotone read-once up-class; exact proof that THR(n,k) is read-once iff k=1 or k=n"
  remaining_native_obligation: "No active I0076 obligation under six-run retirement; future reassignment must start from the common-re-rooting relative-phase blocker in the handoff, not from a seventh lemma"
  remaining_retained_screen_obligation: "handle overlapping/variable-reuse composition; minimal case heterogeneous THR(3,2); parent Problem 10.9 remains open"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_1805Z_successor_screen_f0111_endpoint_gamma1_kl_r63v.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-18T175500Z/admission_delta.md"
    - "operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md"
    - "operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md"
  audit_ids: []
  next_moves:
    - "11 DUALIZE"
    - "15 BREAK THE SYMMETRY ON PURPOSE"
    - "30 ONE SCALE / ONE DIRECTION AT A TIME"
```
