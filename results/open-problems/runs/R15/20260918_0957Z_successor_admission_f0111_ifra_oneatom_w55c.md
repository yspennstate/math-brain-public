Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at historical `2/4`; successor-gate unchanged count remains `UNKNOWN`. Methods **#9 RANDOMIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #25 COUNT THE SAME THING TWICE**.**

# R15 CLOSABLE OUTSIDE — reliability-theory transfer and a one-atom dual no-go for Talagrand 10.9

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

All new derivations below are **SELF_CHECK_ONLY** unless explicitly identified as prior art. No independent audit is claimed.

## 1. Continuity, exact Brownian source, and admission state

I began from the current repository state, rereading/recovering:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the current coordinator report `operations/task_health/runs/2026-09-18T085900Z/status.md`;
- the controlling I0076 six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the immediately preceding R15 report `runs/R15/20260918_0858Z_successor_admission_f0111_pascal_u54.md`;
- the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`;
- current ownership searches, including a fresh check that `operations/claims/F0111.md` is absent.

I also reread the primary Burdzy--Scheutzow paper. Definition 2.1 says that `X` is FBM if random origins tending to `-infinity` have standard-Brownian futures; BBM is the time-reversed notion; and 2BM means that at some random origin the two centered halves are **independent standard Brownian motions**. Problem 7.2 asks whether FBM + BBM plus independence of the two complete centered half-paths at an arbitrary random time `T` already implies 2BM. There is no stopping-time assumption on `T`, and the problem does not assume either seam half is Brownian. Problem 7.5 is distinct and excluded.

The six-run handoff remains controlling. The Theorem-6.1-based candidate was eliminated because it has no source-required independent real seam. The alternating Brownian-prefix/BES candidate attained FBM, BBM and exact seam independence but was then proved to be 2BM by the excursion/Palm argument. Therefore there is still **no surviving frozen counterexample candidate**. The marked Brownian-cell / sparse copied-continuous-block idea remains only an architecture. I do not restart it.

The historical source metric remains `2/4`, status `OPEN / PARTIAL / RETIRED-HANDOFF`.

The strict successor metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

The newest coordinator strict-admission pass likewise found no source crossing every admission gate, and current queue searches show that superficially attractive CLOSABLE rows continue to acquire other owners/reservations. I create no ownership claim.

With no lawful fresh CLOSABLE assignment, I continue F0111 only as **successor-screening mathematics**, not as an R15 assignment.

## 2. Screening source: Talagrand Problem 10.9

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9.

For an up-class `A` on a finite set `S`, Talagrand uses the product law `zeta_t` with coordinate-inclusion probabilities

`P_t(i in X)=1-exp(-t_i)`

and the hazard

`F_A(t)=-log(1-zeta_t(A)).`

The class `A` belongs to `C_gamma` if, for every base point `q>=0`, there is a multilinear polynomial

`P(t)=sum_{empty != I subset S} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t)<=P(t)` for every `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold

`A_{n,k}={X subset [n]: |X|>=k}`.

A dated 2026-09-18 current-literature search again recovered Talagrand's source and related threshold work of DeMarco--Kahn, Frankston--Kahn--Park and the later Kahn--Kalai literature, but no accessible source explicitly resolving this exact heterogeneous-`q` positive-multilinear-majorant problem. This is bounded negative evidence, not a worldwide openness or novelty certificate.

The preceding R15 weak-dual lemma is carried forward, not reproved: a finite positive measure `mu` satisfying

`int t_I dmu(t) <= (gamma q)_I` for every nonempty `I`

obeys

`P(gamma q)>=int F_A(t)dmu(t)`

for every admissible positive polynomial `P`. Hence a strict inequality

`int F_A dmu > gamma F_A(q)`

would refute `C_gamma` at that base point.

This run asks whether the **smallest randomized dual witnesses, one-atom measures `mu=w delta_t`, can ever do this**.

## 3. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the radial inequality is a classical IFRA theorem

The earlier R20 screen proved for `k=2` that

`F_{n,2}(lambda q)<=lambda F_{n,2}(q)`, `0<=lambda<=1`.

Reliability theory shows that the same fact is much broader and is **KNOWN prior art in disguise**.

Fix any finite up-class `A` and `q>=0`. Let independent component-failure clocks have laws

`tau_i ~ Exp(q_i)`

(with `q_i=0` interpreted as `tau_i=infinity`) and let

`Y_s={i: tau_i<=s}`.

Then `Y_s` is a pure-birth Markov chain on the subset lattice, with monotone sample paths, and

`P(Y_s in A)=zeta_{s q}(A)`.

Let

`T_A=inf{s>=0: Y_s in A}`.

Because `A` is increasing,

`P(T_A>s)=1-zeta_{s q}(A)`,

so the cumulative hazard of `T_A` is exactly

`H_q(s):=-log P(T_A>s)=F_A(s q)`.                         (3.1)

Brown--Chaganty (1983), *On the First Passage Time Distribution for a Class of Markov Chains*, proves that first-passage times to increasing sets for stochastically monotone chains with monotone paths are IFRA, with coherent systems among the listed applications. Shanthikumar--Shaked (1987) gives the Markov-jump-process version for upper sets. The subset-failure chain above is exactly in that framework.

For an IFRA law the average failure rate `H_q(s)/s` is nondecreasing. Therefore, for every up-class `A`, every `q>=0`, and every `0<=lambda<=1`,

```
F_A(lambda q) <= lambda F_A(q).                            (3.2)
```

This is **not a new theorem**. It is a reliability-theoretic prior-art transfer. It subsumes the earlier R20 `k=2` radial theorem and shows that the zero-cost necessary radial test can never refute `C_gamma` for **any** up-class, not only cardinality thresholds.

Primary prior-art records checked on 2026-09-18:

- M. Brown and N. R. Chaganty, *Annals of Probability* 11 (1983), 1000--1008, DOI `10.1214/aop/1176993448`;
- J. G. Shanthikumar and M. Shaked, *Mathematics of Operations Research* 12 (1987), 562--568, DOI `10.1287/moor.12.3.562`.

The exact connection (3.1) is elementary, but I make no publication-novelty claim for noticing it in Talagrand's notation.

## 4. Method #25 — COUNT THE SAME THING TWICE: every up-class hazard is separately concave

The same reliability representation gives another exact structural fact, this time by conditioning on a single coordinate.

### Lemma R15-F0111-SEPCONC

For every finite up-class `A`, the function `F_A(t)` is nondecreasing and concave in each coordinate separately.

#### Proof

Fix coordinate `i` and all other hazards. Let

`a=P(X notin A | i absent)`,

`b=P(X notin A | i present)`.

Because `A` is an up-class, its complement is a down-class, so `0<=b<=a`. If the `i`-th hazard is `x`, then

```
1-zeta_t(A)
 = a exp(-x)+b(1-exp(-x))
 = b+(a-b)exp(-x).
```

Thus, with `d=a-b>=0`,

`f(x):=F_A(t)=-log(b+d exp(-x)).`

Its first derivative is

`f'(x)=d exp(-x)/(b+d exp(-x))>=0`,

and its second derivative is

`f''(x)=-b d exp(-x)/(b+d exp(-x))^2<=0`.

Hence `f` is increasing and concave. QED.

A useful consequence is the coordinate-stretch inequality. For `c>=1`, concavity on the interval `[0,cx]` gives

```
F_A(...,c x,...)
 <= c F_A(...,x,...)-(c-1)F_A(...,0,...)
 <= c F_A(...,x,...).                                     (4.1)
```

Iterating (4.1) over a set of coordinates gives a product cost for heterogeneous stretches.

This is the exact local fact needed to analyze one-atom dual witnesses.

## 5. Method #9 — RANDOMIZE: all one-atom weak-dual refutations are impossible

### Theorem R15-F0111-ONEATOM

Let `A` be **any** finite up-class, let `0<gamma<=1`, and let `q,t>=0`. Suppose `w>=0` satisfies all one-atom weak-dual moment constraints

```
w t_I <= (gamma q)_I
```

for every nonempty `I subset S`, where `t_I=product_{i in I} t_i`. Then

```
w F_A(t) <= gamma F_A(q).                                 (5.1)
```

Consequently, **no positive dual measure supported on one point, `mu=w delta_t`, can strictly refute `A in C_gamma`** through the weak-duality certificate. In particular, a dual disproof of Talagrand Problem 10.9 must use at least two support points whose moment budgets interact, or a genuinely different negative mechanism.

#### Proof

Put

`u=gamma q`.

If `t=0`, then `F_A(t)=0` and there is nothing to prove.

Let

`J={i: t_i>u_i}`.

### Case 1: `J` is nonempty

If some `i in J` has `u_i=0`, then the singleton moment constraint gives `w t_i<=0`; since `t_i>0`, this forces `w=0`, and (5.1) is trivial. Hence assume `u_i>0` on `J`.

For `i in J`, set

`c_i=t_i/u_i>1`.

The moment constraint for the **single subset `I=J`** yields

```
w product_{i in J} t_i <= product_{i in J} u_i,
```

or

```
w <= product_{i in J} c_i^(-1).                           (5.2)
```

Define `v` by

- `v_i=t_i=c_i u_i` for `i in J`;
- `v_i=u_i` for `i notin J`.

Since `t_i<=u_i` outside `J`, coordinate monotonicity gives

`F_A(t)<=F_A(v)`.

Starting from `u` and stretching the coordinates in `J` one at a time, (4.1) gives

```
F_A(v) <= (product_{i in J} c_i) F_A(u).                  (5.3)
```

Combining (5.2)--(5.3),

```
w F_A(t) <= F_A(u)=F_A(gamma q).
```

The known IFRA radial inequality (3.2) now gives

`F_A(gamma q)<=gamma F_A(q)`,

which proves (5.1).

### Case 2: `J` is empty

Thus `t<=u` coordinatewise. Let

```
c=min_{i:t_i>0} u_i/t_i >=1.
```

The singleton moment constraints imply `w<=c`. Also `t<=u/c` coordinatewise. Hence monotonicity and (3.2), now applied on the ray through `u`, give

```
F_A(t)<=F_A(u/c)<=c^(-1)F_A(u).
```

Therefore

```
wF_A(t)<=F_A(u)<=gamma F_A(q).
```

This proves the theorem. QED.

### Why this is materially stronger than the previous screens

Earlier R15 work eliminated one natural **exchangeable one-orbit** family and gave the exact feasible weight of a one-atom witness. The theorem above eliminates **every one-atom witness at once**, for arbitrary heterogeneous `q`, arbitrary `t`, every threshold `k`, and in fact every up-class `A`.

The negative dual route is therefore forced into genuine support interaction: no single atom can spend the monomial moment budget efficiently enough to beat the Talagrand base-point budget.

I have not found this exact weak-dual corollary stated in the bounded literature search. The IFRA ingredient is definitely classical; separate coordinate concavity is elementary; novelty of their combination is **UNVERIFIED**.

## 6. What this changes, and what it does not

This does **not** solve Talagrand Problem 10.9. It narrows the negative route and corrects prior-art attribution:

1. radial sublinearity is not a new `k=2` phenomenon; it is a classical IFRA consequence for every up-class;
2. one-point dual counterexamples are impossible for every up-class;
3. any dual counterexample to Problem 10.9 must use a measure with support size at least two and exploit tradeoffs among different monomial moments;
4. the positive route still needs a `q`-adaptive positive multilinear majorant with one universal `gamma`.

The natural next negative question is now genuinely finite-support/multiscale: can two atoms trade singleton and higher-order moment budgets in a way that defeats (5.1) collectively? The natural next positive question is whether the separate-concavity stretch argument can be upgraded from atoms to arbitrary dual measures, which would amount to a much stronger dual inequality.

Because F0111 still quantifies over every `n,k,q` and no finite closure route has emerged, its disposition remains

`OPEN-looking / screening only / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED`.

## 7. Current-source / prior-art / access log

Checked on 2026-09-18:

- Burdzy--Scheutzow, *Forward Brownian Motion*, Definition 2.1 and Problem 7.2 from the University of Washington copy / arXiv record; source wording matches the repository handoff. The web PDF text was accessible; screenshot retrieval returned a cache-miss error, so no claim relies on image-only inspection.
- Talagrand, *Are Many Small Sets Explicitly Small?*, Definition 10.1 and Problem 10.9. PDF text extraction was accessible; screenshot retrieval returned a cache-miss error.
- Brown--Chaganty 1983 IFRA first-passage theorem and its coherent-system application.
- Shanthikumar--Shaked 1987 general-state/Markov-jump IFRA extension.
- DeMarco--Kahn and Frankston--Kahn--Park as nearby later Talagrand-threshold literature.
- Current repository ownership/admission state, including the absent `operations/claims/F0111.md` and the coordinator's 08:59Z strict-admission report.

Search/indexing is bounded. Failure to find an explicit statement of Theorem R15-F0111-ONEATOM is not a novelty certificate.

## 8. Validation discipline

No exact-arithmetic checker was created. The load-bearing claims are analytic and their proofs are on the page. A checker for an unchanged admission count would be ceremonial and contrary to the 90/10 rule.

No audit was requested this run because there is no source closure claim. The theorem remains SELF_CHECK_ONLY pending any future use in a paper or source-level closure argument.

## 9. Model / scheduler-control boundary

The actually running model is GPT-5.6 Sol. Authenticated reasoning-effort telemetry is unavailable, so the reasoning level is UNVERIFIED. This is not GPT-6 maximum.

The exposed scheduler surface still has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt and no guaranteed hour-long runtime control. GPT-6 / maximum remains prompt-only from this interface. The historical P26 ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task`; repository history records later success from an authorized context. The lawful workaround remains an owning/admin-authorized product or backend surface, or platform support that exposes and attests model/reasoning controls — not duplication or permission bypass.

No scheduler, permission, email, Drive, public-posting or purchase action was taken.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  predecessor:
    source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
    metric_name: source_matching_obligations_for_one_frozen_counterexample
    metric_before: "2/4"
    metric_after: "2/4"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    surviving_frozen_candidate: false
    active_research_this_run: false
  successor_gate:
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    movement: none
    unchanged_count: UNKNOWN
    claim_created: false
  tried_moves: [9, 17, 25]
  screening:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
    disposition: "OPEN-looking / screening only / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED"
    exact_results:
      - "KNOWN prior-art transfer: F_A(lambda q) <= lambda F_A(q) for every up-class, via IFRA first-passage theory"
      - "SELF_CHECK_ONLY: F_A is separately concave in every hazard coordinate"
      - "SELF_CHECK_ONLY: every one-atom weak-dual witness satisfies w F_A(t) <= gamma F_A(q)"
    prior_art_correction:
      - "R20 k=2 radial-sublinearity theorem is subsumed by classical coherent-system IFRA theory"
    remaining_obligation: >-
      A source closure still requires one universal gamma and a q-adaptive positive multilinear
      majorant for every n,k,q, or an exact counterexample. The weak-dual negative route now
      requires genuine multi-atom moment-budget interaction; support size one cannot refute.
  evidence:
    - "runs/R15/20260918_0858Z_successor_admission_f0111_pascal_u54.md"
    - "runs/R15/20260918_0355Z_successor_admission_f0111_dual_s48a.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-18T085900Z/status.md"
    - "Brown-Chaganty 1983, DOI 10.1214/aop/1176993448"
    - "Shanthikumar-Shaked 1987, DOI 10.1287/moor.12.3.562"
  finite_checker_needed: false
  audit_ids: []
  closure_claim: false
  next_methods: [10, 20, 28]
```

## 11. Next cursor

If no strict CLOSABLE successor is admitted before the next invocation, do **not** return to one-atom dual searches. Fresh methods: **#10 DERANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE FOR ALL WITH FOR TYPICAL**. The most useful concrete mathematical question is whether the one-atom inequality tensorizes or disintegrates over a two-atom dual measure; failure of such an extension would identify the first genuinely multiscale obstruction.

**NO I0076 REOPENING. NO F0111 CLAIM. R15 remains `SUCCESSOR_ADMISSION_REQUIRED`.**