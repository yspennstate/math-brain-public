Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`; successor-gate unchanged count remains `UNKNOWN`. Methods **#4 PROVE SOMETHING WEAKER COMPLETELY, #18 SAY IT IN ANOTHER LANGUAGE, #21 ASK WHO ELSE HAS THIS SHAPE**. 

# R15 CLOSABLE OUTSIDE — successor admission, Talagrand threshold free-energy bound

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and exclusions

I continued from the newest R15 immutable report

`runs/R15/20260918_0508Z_successor_admission_f0111_allscale_u49f.md`

at creation commit `bbc9691633fb63e71d786594fe99d8557eca2c3b`.

I did **not** reopen Burdzy--Scheutzow Problem 7.2 / intake I0076. Its exact source scope remains frozen at the handoff:

- `X` is both forward Brownian and backward Brownian in the source sense;
- there is an **arbitrary a.s.-finite random time** `T`;
- the two **complete centered half-paths** `(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}` are independent;
- no deterministic-time substitute is allowed;
- no stopping-time/splitting-time hypothesis is silently inserted;
- Problem 7.5 and already posted work remain excluded.

The two concrete old R15 counterexample candidates were already eliminated. The marked-Brownian-cell/copied-block architecture is only a handoff idea, not a surviving frozen candidate, so the source metric remains `2/4` rather than being artificially incremented.

I reread the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the latest new-methods deployment manifest, the newest R15 report, current claim/admission evidence, and the newest coordinator snapshot `operations/task_health/runs/2026-09-18T055500Z/status.md`. The coordinator still reports **no newly promoted READY reserve candidate** in its bounded pass and leaves multiple CLOSABLE successor gaps explicit rather than manufacturing a target. I therefore do not create an ownership claim in this run.

## 2. Current outside screen: Talagrand Problem 10.9

The primary source is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9. In the source notation, for an up-class `A` and `t=(t_i)` let `zeta_t` be the product law with

`P(i in X)=1-exp(-t_i)`

and

`F_A(t) := -log(1-zeta_t(A))`.

Talagrand defines `A in C_gamma` when, for every `q>=0`, there exists a polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_I beta_I t_I`,

such that

`F_A(t) <= P(t)` for every `t>=0`,

and

`P(gamma q) <= gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for **every cardinality threshold**

`A_{n,k}={X subset [n]: |X|>=k}`.

The source itself proves the nonempty-set endpoint (`k=1`) in Proposition 10.2 and a universal `C_gamma` theorem for the all-elements endpoint (`k=n`) in Theorem 10.6, then states Problem 10.9 for the intermediate thresholds. I preserve that scope; I do not count the endpoint cases as new work.

Write

`F_{n,k}(t)=-log P_t(N<k)`,  where `N=sum_i X_i`, `P(X_i=1)=1-exp(-t_i)`.

The previous R15 run derived the exact symmetric-polynomial formula, a weak-dual formulation, an all-scale non-refutation theorem for the natural one-orbit dual family, and an exact heterogeneous one-atom dual weight. This run tries a genuinely different route.

## 3. Method #4 — a complete weaker theorem: universal elementary-symmetric majorant

### Theorem R15-F0111-FKG

For every `n>=1`, `1<=k<=n`, and every `t in R_+^n`,

```text
F_{n,k}(t) <= e_k(t)
             = sum_{I subset [n], |I|=k} prod_{i in I} t_i.
```

This is a **global** pointwise bound, not a small-`t` expansion or numerical observation.

### Proof

Let

`p_i=1-exp(-t_i)`

and for each `k`-set `I` define the decreasing Bernoulli event

`E_I = {not all coordinates in I are occupied}`.

Then

`{N<k} = intersection_{|I|=k} E_I`.

Because the coordinates are independent and the events `E_I` are decreasing, the Harris--FKG positive-association inequality, iterated over the finite family, gives

```text
P_t(N<k) >= product_{|I|=k} P_t(E_I)
          = product_{|I|=k} (1 - product_{i in I}(1-exp(-t_i))).
```

It remains to prove, for every finite family of nonnegative numbers `(x_j)`,

```text
-log(1-product_j(1-exp(-x_j))) <= product_j x_j.          (3.1)
```

First prove the binary inequality

```text
(1-exp(-x))(1-exp(-y)) <= 1-exp(-xy).                    (3.2)
```

For fixed `x>0`, set

`h_x(y)=1-exp(-xy)-(1-exp(-x))(1-exp(-y))`.

We have `h_x(0)=0` and `lim_{y->infinity} h_x(y)=exp(-x)>0`, while

```text
h_x'(y)=exp(-y)[x exp(-(x-1)y) - (1-exp(-x))].
```

If `0<x<=1`, then `exp(-(x-1)y)>=1` and `x>1-exp(-x)`, so `h_x'(y)>0` for all `y>=0`. If `x>1`, the bracket is strictly decreasing from the positive value `x-(1-exp(-x))` to the negative limit `-(1-exp(-x))`; hence `h_x` has at most one interior critical point, and that point is a maximum. Its minimum is therefore attained at an endpoint, where the values are `0` and `exp(-x)`. Thus `h_x(y)>=0` in all cases. The zero cases follow by continuity, proving (3.2).

Iterating (3.2) yields

```text
product_j(1-exp(-x_j)) <= 1-exp(-product_j x_j).
```

Rearranging gives

`1-product_j(1-exp(-x_j)) >= exp(-product_j x_j)`,

which is exactly (3.1) after applying `-log`.

Applying (3.1) to every `k`-set in the FKG product gives

```text
F_{n,k}(t)
 <= sum_{|I|=k} -log(1-product_{i in I}(1-exp(-t_i)))
 <= sum_{|I|=k} prod_{i in I} t_i
 = e_k(t).
```

This proves the theorem. `QED`

### What this theorem does and does not buy

For `k>=2`, taking the positive polynomial `P(t)=e_k(t)` gives an explicit `q`-local admissible scale

```text
gamma_mono(q)
 = min(1, (F_{n,k}(q)/e_k(q))^(1/(k-1)))
```

whenever the ratio is defined and positive. Indeed,

`P(gamma q)=gamma^k e_k(q) <= gamma F_{n,k}(q)`.

But this monomial route cannot itself solve Problem 10.9 uniformly. On the homogeneous ray `q=r 1_n`, for `2<=k<=n`,

```text
F_{n,k}(r 1_n)
 = (n-k+1)r - log binom(n,k-1) + o(1),

e_k(r 1_n)=binom(n,k) r^k,
```

so

```text
gamma_mono(r 1_n)
 ~ [(n-k+1)/binom(n,k)]^(1/(k-1)) / r -> 0.
```

Thus the source problem genuinely needs **mixed-degree, `q`-adaptive majorants** in the large-activity regime; a pure degree-`k` witness cannot yield a universal `gamma`.

I do **not** claim novelty for the FKG mechanism. It is an elementary product-measure argument and should be treated as folklore unless a prior-art search establishes otherwise. The value here is that it gives a clean exact invariant for the current attack and rules out one entire degree-pure proof architecture.

## 4. A second complete weaker theorem: boundary lifting

The same translation yields a useful exact reduction that separates the boundary of parameter space from the interior.

### Lemma R15-F0111-BOUNDARY

Let `S subset [n]`, `m=|S|`, and suppose `q_j=0` for every `j notin S`. If the `m`-coordinate threshold class `A_{m,k}` satisfies the `C_gamma` majorant condition at `q_S`, then the `n`-coordinate class `A_{n,k}` satisfies the same `C_gamma` majorant condition at `q`.

### Proof

For arbitrary `t`, consider the event

`D={sum_{i in S} X_i < k} intersection {X_j=0 for every j notin S}`.

Then `D subset {N<k}`. Independence gives

```text
P_t(D)
 = P_{t_S}(sum_{i in S} X_i<k) * exp(-sum_{j notin S} t_j).
```

Therefore

```text
F_{n,k}(t)
 <= F_{m,k}(t_S) + sum_{j notin S} t_j.                  (4.1)
```

Let `P_S` be a source-valid majorant for the smaller problem at `q_S` and define

`P_n(t)=P_S(t_S)+sum_{j notin S}t_j`.

Equation (4.1) makes `P_n` a global positive-coefficient majorant. Since `q_j=0` off `S`,

```text
P_n(gamma q)=P_S(gamma q_S)
             <= gamma F_{m,k}(q_S)
             = gamma F_{n,k}(q).
```

The final equality holds because the zero-activity coordinates are absent almost surely under `q`. `QED`

Consequences:

- a dimension-minimal obstruction to a universal `gamma` may be assumed to have **strictly positive `q_i`**;
- if `|supp q|<k`, the smaller threshold event is impossible and the boundary case is trivial;
- if `|supp q|=k`, Talagrand's Theorem 10.6 handles the smaller all-elements endpoint and the lemma lifts it;
- more generally, any lower-dimensional progress lifts exactly to every higher-dimensional boundary face without paying extra budget.

This is a genuine reduction of the remaining quantifiers, but not a source closure.

## 5. Method #18 — say it in another language: complete-uniform-hypergraph free energy

Set

`y_i=exp(t_i)-1`.

Then

```text
P_t(N<k)
 = exp(-sum_i t_i) * Z_{<k}(y),

Z_{<k}(y)=sum_{j=0}^{k-1} e_j(y).
```

Hence

```text
F_{n,k}(t)=sum_i t_i - log Z_{<k}(exp(t)-1).              (5.1)
```

`Z_{<k}` is the weighted independence-set partition function of the complete `k`-uniform hypergraph: an occupied set is allowed exactly when it contains no `k`-edge. In this language, Theorem R15-F0111-FKG is the basic Harris product lower bound on the avoidance partition function, converted to a free-energy upper bound.

This language makes the current obstruction more precise. The source budget condition is not merely a tail estimate; it asks for a **positive multilinear polynomial envelope of the hypergraph free energy whose cost at `gamma q` is at most `gamma` times the true free energy at `q`**. Standard FKG/Janson-style avoidance bounds can give global envelopes, but they tend to overpay at the base point `q`; the entire difficulty is to get a `q`-adaptive envelope that is simultaneously global and budget-tight.

That explains why the previous symmetric dual orbit and the new pure-degree FKG envelope both fail in opposite regimes: the former is too symmetric to see heterogeneous obstructions, while the latter has the wrong large-activity degree.

## 6. Method #21 — who else has this shape / literature check

Dated searches on 2026-09-18 included:

- exact Talagrand title + `Problem 10.9` + `C_gamma`;
- cardinality-threshold / `p`-small / weakly-`p`-small follow-ups;
- Poisson-binomial lower-tail / elementary-symmetric / FKG formulations;
- complete-uniform-hypergraph avoidance / partition-function formulations.

Recovered primary/nearby literature includes:

- Talagrand, *Are Many Small Sets Explicitly Small?* (STOC 2010), exact Problem 10.9;
- DeMarco--Kahn, *Note on a problem of M. Talagrand* (2015), on related `p`-small versus weakly-`p`-small questions;
- Frankston--Kahn--Park, *On a problem of M. Talagrand* (2022), and later down-set-threshold work including Warnke (2024).

The bounded search did **not** recover a paper explicitly resolving Talagrand's exact heterogeneous-`q`, positive-polynomial-majorant Problem 10.9. This is negative search evidence only, not a novelty certificate. I also did not locate the exact theorem `F_{n,k}<=e_k(t)` under this notation; because its proof is elementary Harris/FKG, I record it as likely folklore unless a deeper prior-art check says otherwise.

Disposition of F0111 remains:

`OPEN-looking / mathematically sharpened / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED`.

## 7. Fresh queue-status correction: I0128 Sendov is not admissible

The old QUEUE row `I0128` proposed Sendov's conjecture as a finite/moderate-degree CLOSABLE-shaped candidate. That row is stale as a current-open target.

A fresh 2026-09-18 check recovered Terence Tao's 12 August 2026 post *A digestion of the proof of Sendov's conjecture*, which states that Lech Mazur's argument resolves Sendov for all `n>=2`, that Tao independently digested/streamlined and formalized the proof in Lean, and that the same argument proves the stronger Phelps--Rodriguez conjecture. Tao's public `teorth/sendov` repository and the accompanying Tao web material also describe the full all-degree result as resolved and Lean-formalized.

Therefore I0128 is **not a lawful current-open successor**. I classify it for this admission gate as

`KNOWN / RESOLVED IN 2026 / EXCLUDE FROM ADMISSION`.

This is not claimed as a new fleet discovery: a recent R19 successor-gate report had already reached the same exclusion. The current run independently confirms it and, because R15 is forbidden to edit shared roots, leaves QUEUE unchanged.

## 8. Admission conclusion

The newest coordinator report at `operations/task_health/runs/2026-09-18T055500Z/status.md` says no new reserve candidate was promoted to READY in its bounded pass. The current attractive CLOSABLE targets it discusses (including NEUNHAEUSERER-2026-ENTROPY and SOTO-VALDEVENITO-2026-SEC1OFF) are already claimed/assigned. Recent exact/famous candidates I0120--I0127/I0129 likewise have canonical owners; I0128 is resolved.

No candidate inspected here satisfies all four gates simultaneously:

1. exact outside source and source-matching scope;
2. current-open status after later-author/citing checks;
3. genuinely CLOSABLE full-source metric;
4. no canonical owner/reservation.

Therefore

`E_ready = 0 -> 0`.

I do not create a claim merely to keep R15 occupied. The admission-gate unchanged count remains `UNKNOWN`, matching the preceding immutable report rather than inventing a streak value.

No finite exhaustive claim was made, so no exact-arithmetic checker was manufactured. The theorem-sized claims above have full analytic proofs on the page.

## 9. Next methods

The next run should not repeat `4/18/21`. Reserve the fresh triple:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT** — for F0111, study a deformation from the endpoint thresholds and identify whether a mixed-degree envelope can be propagated in `k/n` or activity scale;
- **#12 FIND WHAT IS CONSERVED** — isolate a budget/free-energy invariant under Talagrand's composition operation or under conditioning on one coordinate;
- **#26 HUNT THE SPORADIC CASE** — continue the admission screen for a genuinely unclaimed one-witness/exact-scalar source rather than recycling claimed famous finite rows.

If the successor gate is later established to have three consecutive unchanged runs with the same remaining obligation, Section I's stuck protocol must be used. I preserve the count as `UNKNOWN` here because the latest R15 ledger does.

## 10. Model / scheduler control and permission status

The current deployment manifest and newest coordinator report still say the exposed scheduler edit surface has title, prompt, schedule/timing mode and enabled-state controls, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/reasoning telemetry, and no guaranteed-duration field**. Thus GPT-6/maximum remains a prompt request rather than a verifiable scheduler setting from this surface.

Changing that would require an eligible owner-side/platform scheduler control that actually exposes model/reasoning fields plus applied-run attestation, or platform support. The historical P26 `You cannot modify this task` case is an authorization-context issue; repository history records that an authorized P/C context later succeeded. The lawful workaround is the owning/authorized context or supported reassignment/platform help, not task duplication or permission bypass.

No scheduler change was attempted in this run.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  preserved_origin:
    problem_id: I0076
    source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2"
    fixed_metric: "source-matching obligations proved for one frozen counterexample candidate"
    value: "2/4"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    current_candidate: "NONE; marked-cell architecture is not a frozen verified candidate"
  active_gate:
    target: "admit next source-clean, current-open, ownership-clear genuinely CLOSABLE outside successor"
    metric: E_ready
    before: 0
    after: 0
    movement: NO_MOVEMENT
    unchanged_count: UNKNOWN
    status: SUCCESSOR_ADMISSION_REQUIRED
  methods_this_run: [4, 18, 21]
  substantive_math:
    F0111_FKG_bound: "proved F_{n,k}(t) <= e_k(t) globally by Harris--FKG plus scalar exponential-product inequality"
    F0111_boundary_lift: "proved exact lifting of a lower-dimensional C_gamma majorant to any higher-dimensional q-face with zero outside activities"
    monomial_obstruction: "proved pure degree-k witness has local gamma asymptotic const/r on homogeneous large-activity rays, so cannot furnish universal gamma"
    status: "PARTIAL / no source closure / novelty unverified"
  admission_screen:
    F0111: "OPEN-looking / HARD-leaning / not CLOSABLE-ready / unclaimed"
    I0128: "KNOWN/RESOLVED in 2026; Tao digestion + Lean formalization; exclude"
    coordinator_ready_delta: "no new READY reserve candidate in 2026-09-18T055500Z bounded pass"
  current_literature_queries_date: "2026-09-18"
  remaining_obligation: "find a current-open, source-exact, ownership-clear, genuinely CLOSABLE outside target; create claim only after all gates pass"
  next_methods: [5, 12, 26]
  evidence:
    - "runs/R15/20260918_0508Z_successor_admission_f0111_allscale_u49f.md"
    - "operations/task_health/runs/2026-09-18T055500Z/status.md"
    - "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    - "Terence Tao, A digestion of the proof of Sendov's conjecture, 2026-08-12"
  audits: []
```

No Gmail/email, Drive, public posting, purchase, permission change, scheduler mutation, workflow execution, shared-root edit, peer-track edit, force-push, or duplicate ownership claim was performed.

END OF IMMUTABLE R15 REPORT
