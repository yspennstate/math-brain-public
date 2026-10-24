Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`; successor-gate unchanged count remains `UNKNOWN`. Methods **#8 GO THE OTHER WAY AND DISCRETIZE, #19 MAKE IT AN ALGORITHM, #30 DO ONE PRIME / SCALE / DIRECTION AT A TIME**.

# R15 CLOSABLE OUTSIDE — successor admission, exact Pascal hazard recursion, and the gap state

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity: exact Brownian source recovered, predecessor not reopened

I began from current repository state rather than the stale native title. I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the current coordinator report `operations/task_health/runs/2026-09-18T085900Z/status.md`;
- the controlling R15 six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the preceding R15 report `runs/R15/20260918_0824Z_successor_admission_f0111_schur_ties_v53c.md`;
- the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`;
- targeted I0076/F0111/intake-history searches and the current same-source I0077 ownership/report state.

The GitHub connector cannot literally render every roughly 780-row intake collection end-to-end without truncation. I therefore do not claim a byte-for-byte display of every unrelated row. The newest coordinator strict-admission screen explicitly records a completed intake/root delta pass with **no source crossing all READY + current-open + ownership-clear + genuinely CLOSABLE gates**, and my targeted searches below agree with it. I do not fabricate a READY target.

The exact predecessor source is Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2. I reopened the primary source on 2026-09-18. Definition 2.1 says:

- `X=(X_t)_{t in R}` is an FBM iff there are random times `S_n -> -infinity` a.s. such that every shifted future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is a BBM iff the time reversal is an FBM;
- `X` is a 2BM iff there is a random time `S` for which `(X_{S+t}-X_S)_{t>=0}` and `(X_{S-t}-X_S)_{t>=0}` are independent **standard Brownian motions**.

Problem 7.2 itself assumes only that `X` is both FBM and BBM and that there exists an arbitrary random time `T` for which the two complete centered half-paths

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent. It asks whether this forces `X` to be 2BM. There is **no stopping-time hypothesis on `T`** and neither seam half is separately assumed Brownian. Problem 7.5 is a different source question and remains excluded.

The six-run handoff remains controlling. The source Theorem-6.1 FBM+BBM non-2BM candidate was eliminated because it has no source-required independent real seam. The later alternating Brownian-prefix/BES candidate attained FBM + BBM + exact seam independence but was then proved to be 2BM by finite-intensity excursion-Palm de-biasing. Hence there is presently **no surviving frozen counterexample candidate** to which a third or fourth source obligation can honestly be attached. The marked Brownian-cell / sparse copied-continuous-block scheme is only a future architecture, not a candidate. The historical source metric therefore remains `2/4` and I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF`.

A fresh bounded 2026-09-18 exact-title / Problem-7.2 / random-time search again recovered the original source and related Brownian splitting/concatenation work but no accessible later source explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

The same source's Problem 7.8 / I0077 is **not available as a successor**. `operations/claims/I0077.md` reserves it to R07, and the newest R07 report advances that distinct problem. I do not duplicate it.

## 2. Admission metric

The successor-admission metric is unchanged from the recent R15 screening runs:

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`.  
After: `0`.

The latest coordinator screen also reports zero new strict admissions; recent new claims only reduce free inventory. Therefore I create no ownership claim this run.

With no lawful fresh CLOSABLE assignment, I continue F0111 only as **successor-screening mathematics**, not as an R15 ownership claim.

## 3. F0111 exact source and carried-forward state

Screening source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9.

For

`A_{n,k}={X subset [n]: |X|>=k}`

and independent coordinates with

`P_t(i in X)=1-exp(-t_i)`, `t_i>=0`,

define

`F_{n,k}(t)=-log P_t(|X|<k)`.

Talagrand's `C_gamma` requirement asks whether there is one universal `gamma>0` such that, for every `n,k` and every base point `q>=0`, there is a multilinear polynomial with nonnegative coefficients and no constant term,

`P_q(t)=sum_{empty != I subset[n]} beta_I(q) t_I`, `beta_I(q)>=0`,

such that

`F_{n,k}(t)<=P_q(t)` for all `t>=0`

and

`P_q(gamma q)<=gamma F_{n,k}(q)`.

The source's Proposition 10.5 composes classes built on **disjoint blocks**. Its two-variable analytic core is

`Phi(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v))`,

which appears explicitly in the source's Theorem 10.7 argument.

A fresh 2026-09-18 exact-title / `Problem 10.9` / `C_gamma` search recovered Talagrand's source and the later threshold literature (including DeMarco--Kahn and later Talagrand/Kahn--Kalai threshold work), but no accessible theorem explicitly resolving this exact heterogeneous-`q` positive-multilinear-majorant question. Negative search evidence is not a novelty certificate.

I do **not** reprove previous R15/R20 work. Carried forward are: the exact elementary-symmetric formula, the FKG envelope `F_{n,k}<=e_k`, boundary lifting, failure of the natural exchangeable one-orbit dual refutation, R15's homogeneous `k=2` `gamma=1/4` certificate, R20's radial/tropical reductions, and R15's preceding Schur-concavity and second-order cutoff-tie theorem.

This run asks a different question: can the threshold family itself be organized into an exact finite recursion whose state exposes why Talagrand's disjoint-block composition theorem stops one step short?

## 4. Method #8 — DISCRETIZE: exact Pascal hazard recursion

Let

`N_m=sum_{i=1}^m xi_i`,

where the `xi_i` are independent and

`P(xi_i=1)=1-exp(-t_i)`.

For `1<=k<=m+1` set

`F_{m,k}(t)=-log P(N_m<k)`.

Thus

`F_{m,1}(t)=sum_i t_i`,

and

`F_{m,m+1}(t)=0`.

For `2<=k<=m+1`, introduce the **threshold gap**

`G_{m,k}(t)=F_{m,k-1}(t)-F_{m,k}(t)>=0`.                 (4.1)

### Theorem R15-F0111-PASCAL

For every `m>=1`, every `2<=k<=m+1`, every `t in R_+^m`, and every new coordinate `s>=0`,

```
F_{m+1,k}(t,s)
 = F_{m,k}(t) + Phi(s,G_{m,k}(t)),                         (4.2)
```

where

```
Phi(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v)).                  (4.3)
```

In words: **adding one Bernoulli coordinate updates a cardinality-threshold hazard by applying exactly Talagrand's two-variable all-elements hazard to the new coordinate and one local threshold gap.**

#### Proof

Condition on the last Bernoulli variable. Put

`A=P(N_m<k)=exp(-F_{m,k})`,

`B=P(N_m<k-1)=exp(-F_{m,k-1})`.

Since the last coordinate fails with probability `exp(-s)`,

```
P(N_m+xi_{m+1}<k)
 = exp(-s) A + (1-exp(-s)) B.
```

By (4.1), `B=A exp(-G_{m,k})`. Therefore

```
P(N_m+xi_{m+1}<k)
 = A[exp(-s)+(1-exp(-s))exp(-G_{m,k})].
```

Taking `-log` gives

```
F_{m+1,k}
 = F_{m,k}
   -log[exp(-s)+exp(-G_{m,k})-exp(-s-G_{m,k})],
```

which is exactly (4.2). QED.

This identity can also be read from the elementary-symmetric formula

`Z_{k-1}(y',y_{m+1})=Z_{k-1}(y')+y_{m+1}Z_{k-2}(y')`,

but conditioning makes the source-level meaning clearer.

### Why this is not Talagrand's Proposition 10.5 in disguise

At the Boolean-event level,

`{N_m+xi_{m+1}>=k}`

is

`{N_m>=k} union ({xi_{m+1}=1} intersect {N_m>=k-1})`.

The two threshold events on the first `m` coordinates are nested and use the **same block**. Proposition 10.5 composes simpler classes supported on disjoint blocks. Formula (4.2) shows the exact price of that overlap: the second input to `Phi` is not `F_{m,k-1}` itself but the difference

`G_{m,k}=F_{m,k-1}-F_{m,k}`.

That difference is not automatically an up-class hazard to which the source's positive-polynomial induction applies. This is the precise obstruction to the naive Pascal induction.

## 5. Method #19 — MAKE IT AN ALGORITHM: the missing induction state is the gap array

Formula (4.2) gives a finite triangular dynamic program. Starting from

`F_{1,1}(t_1)=t_1`, `F_{1,2}(t_1)=0`,

one can insert coordinates one at a time and compute every `F_{m,k}` from the local gaps. The algebraic operation count for the whole triangular array through level `n` is `O(n^2)` evaluations of elementary functions. This is not presented as a computational certificate; it is an exact analytic recursion.

More importantly, the gaps themselves close under a local update.

For `3<=k<=m+1`, subtracting two copies of (4.2) gives

```
G_{m+1,k}
 = G_{m,k}
   + Phi(s,G_{m,k-1}) - Phi(s,G_{m,k}).                    (5.1)
```

For `k=2`, the boundary equation is

```
G_{m+1,2}
 = G_{m,2} + s - Phi(s,G_{m,2}).                           (5.2)
```

Thus the true finite induction state is not one scalar hazard `F`; it is the **Pascal gap profile**

`(G_{m,2},...,G_{m,m+1})`.

### Theorem R15-F0111-GAP-MONO

For every fixed `m` and activity vector `t`, the threshold gaps are decreasing in the threshold:

```
G_{m,2}(t)>=G_{m,3}(t)>=...>=G_{m,m+1}(t)>=0.              (5.3)
```

Moreover, adding a coordinate can only increase every pre-existing fixed-threshold gap:

```
G_{m+1,k}(t,s)>=G_{m,k}(t),    2<=k<=m+1.                 (5.4)
```

#### Proof of (5.3)

Let

`p_j=P(N_m=j)`, `C_j=P(N_m<=j)`.

The Poisson-binomial generating polynomial

`prod_i[(1-p_i^*)+p_i^* z]`, where `p_i^*=1-exp(-t_i)`,

has only real nonpositive zeros, so Newton's inequalities give log-concavity of the mass sequence `(p_j)` with no internal zeros.

The cumulative sequence `(C_j)` is also log-concave. One elementary verification is as follows. Log-concavity of `(p_j)` means its consecutive ratios decrease, hence for `1<=r<=j`,

`p_j p_r >= p_{j+1} p_{r-1}`.

Summing over `r=1,...,j` and then adding the nonnegative term `p_j p_0` gives

`p_j C_j >= p_{j+1} C_{j-1}`.

Since `C_{j+1}=C_j+p_{j+1}` and `C_j=C_{j-1}+p_j`, this is equivalent to

`C_j^2>=C_{j-1}C_{j+1}`.

Boundary zero cases follow by continuity.

But

`G_{m,k}=log(C_{k-1}/C_{k-2})`.

Log-concavity of `C` says exactly that these ratios decrease with `k`, proving (5.3).

#### Proof of (5.4)

The function `Phi(s,v)` is increasing in `v`. For `k>=3`, (5.1) and (5.3) give

`Phi(s,G_{m,k-1})>=Phi(s,G_{m,k})`,

so `G_{m+1,k}>=G_{m,k}`.

For `k=2`, `Phi(s,v)<=s` because the quantity inside `-log` in (4.3) is at least `exp(-s)`. Equation (5.2) then gives the result. QED.

### What this identifies

A positive proof of Problem 10.9 by induction would need to control not only a threshold hazard but its entire nested **gap profile**, with budget-compatible positive majorants that survive the nonlinear local map (5.1). Talagrand's disjoint-block theorem controls `Phi`; it does not by itself provide positive-polynomial certificates for the differences `G_{m,k}`. That is the missing state variable.

The gap formula is also explicit in the elementary-symmetric coordinates:

```
G_{m,k}
 = log[Z_{k-1}(exp(t)-1)/Z_{k-2}(exp(t)-1)].               (5.5)
```

The elementary bound `log(1+x)<=x` recovers the crude positive envelope behind the earlier FKG route, but the high-activity budget loss shows why a sharper gap certificate is needed.

I treat the Poisson-binomial log-concavity used above as classical machinery, not as a novelty claim. The source-relevant point is the exact coupling of that monotone gap array to Talagrand's own two-variable `Phi`.

## 6. A finite-scale envelope that explains the tropical limit

The recursion makes one very simple but useful global bound impossible to miss.

### Proposition R15-F0111-TAIL

Order the activity coordinates decreasingly,

`t_(1)>=...>=t_(n)>=0`.

Then

```
F_{n,k}(t) <= sum_{j=k}^n t_(j).                           (6.1)
```

More strongly, for **every** set `J subset[n]` of cardinality `n-k+1`,

```
F_{n,k}(t) <= sum_{i in J} t_i.                            (6.2)
```

#### Proof

If every coordinate in `J` fails, at most the `k-1` coordinates outside `J` can succeed. Hence

`{xi_i=0 for all i in J} subset {N_n<k}`.

The left event has probability

`exp(-sum_{i in J}t_i)`.

Therefore

`P(N_n<k)>=exp(-sum_{i in J}t_i)`,

which gives (6.2) after `-log`. Minimizing over `J` yields (6.1). QED.

Thus every complement of a `(k-1)`-set gives an elementary positive **linear** global majorant. Talagrand's difficulty is not existence of a global positive majorant; it is the budget condition at the prescribed base point. On the homogeneous ray the symmetrized linear envelope has exactly the correct leading slope `(n-k+1)/n`, but misses the finite budget by the logarithmic tie defect seen in the preceding R15 run. That is a useful diagnosis for the next route.

This proposition is elementary and almost certainly folklore; I make no novelty claim.

## 7. Method #30 — ONE SCALE / DIRECTION AT A TIME: tropicalizing the exact recursion

The source's two-variable update has the exact min-plus limit

```
lim_{L->infinity} Phi(Lu,Lv)/L = min(u,v).                 (7.1)
```

Therefore the Pascal hazard recursion tropicalizes to a one-coordinate insertion rule. If `x` is sorted decreasingly and `f_{m,k}(x)` denotes the carried-forward first-order limit, then the gap state tropicalizes to the cutoff coordinate,

`g_{m,k}(x)=f_{m,k-1}(x)-f_{m,k}(x)=x_(k-1)`,

and (4.2) becomes

```
f_{m+1,k}(x,s)=f_{m,k}(x)+min(s,x_(k-1)).                 (7.2)
```

Equation (7.2) is exactly insertion-sort for the sum of the smallest `m-k+2` coordinates. This is a consistency explanation of the earlier R20/R15 first-order tropical formula, not a new claim of that formula.

The new point is where the **next-order** information enters. For `a,b>0`, fixed constants `alpha,beta`,

```
Phi(La+alpha,Lb+beta)
 = L a + alpha + o(1),                         if a<b,
 = L b + beta  + o(1),                         if b<a,
 = L a - log(exp(-alpha)+exp(-beta)) + o(1),   if a=b.      (7.3)
```

Thus all fixed-order corrections are created precisely when two local tropical channels tie. Iterating (7.3) through the Pascal recursion gives the same combinatorial tie multiplicities isolated in the preceding R15 theorem: generic rays have a unique insertion history and zero constant defect, while cutoff-tie strata accumulate logarithmic multiplicity.

There is also a clean completion of the boundary case deliberately omitted from the preceding tie theorem. If

`x_(k-1)=0`,

then at most `k-2` coordinates of `x` are positive. For every `L`, coordinates with `x_i=0` have activity `t_i=0` and therefore success probability zero. Hence `N_n<k` almost surely and

```
F_{n,k}(Lx)=0    for every L>=0.                           (7.4)
```

So the tropical/tie analysis has only two regimes: an interior regime with the explicit cutoff-tie logarithm from the preceding report, and a zero-boundary regime where the hazard vanishes identically.

## 8. Research conclusion: a sharper route, but still not a CLOSABLE admission

The three moves substantially sharpen the F0111 mechanism without pretending to solve it.

1. The threshold family has an **exact finite Pascal recursion** driven by Talagrand's own two-variable all-elements function `Phi`.
2. The obstruction to source Proposition 10.5 is exactly the overlapping-block **gap variable** `G=F_{k-1}-F_k`; it is not a vague failure of independence.
3. The full gap profile is ordered in `k` and monotone under coordinate insertion.
4. The finite-scale linear tail envelope is already asymptotically optimal in slope; the missing budget is lower-order and concentrated on tie geometry.
5. Tropicalization turns the recursion into min-plus insertion sort, and its soft-min tie rule generates the logarithmic multiplicity defect.

The most promising next positive route is therefore **not** another global majorant guessed directly for `F`. It is to construct q-adaptive positive multilinear majorants for the local gap array `G_{m,k}` with a budget stable under (5.1), then feed them through Talagrand's existing two-variable certificate. The most promising negative route is to show that no such gap-budget state can be uniform in a multiscale heterogeneous base point even though the raw hazards themselves satisfy the Schur and tail envelopes.

Neither route is complete here. F0111 remains `OPEN-looking / screening only / HARD-leaning / NOT CLOSABLE-ready`, and no ownership claim is created.

## 9. Validation discipline

No numerical path sample was used to verify a Brownian law or any theorem here.

No finite claim required a checker. The new claims are symbolic analytic identities/inequalities with proofs on the page. Creating a ceremonial checker for unchanged `E_ready=0` would violate the 90/10 instruction, so `artifacts/R15/` receives no new file this run.

No independent audit is claimed. These are `SELF_CHECK_ONLY` until a source-level closure package exists.

## 10. Model / scheduler / P26 boundary

The scheduler limitation is still true in the interface exposed to this run. The task controls available here cover prompt/title, schedule or relative-start data, timing mode, and enabled state. They do **not** expose a binding model-family selector, a reasoning-effort selector, authenticated applied-model telemetry, or a guaranteed hour-long execution field. Therefore `GPT-6 / maximum` remains a prompt request only; the actual run is reported as GPT-5.6 Sol with reasoning level UNVERIFIED.

The implementation manifest still records that native P26 task ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task`. I do not attempt to bypass that authorization boundary and I do not create a replacement schedule. The legitimate remedies are the owning/authorized task context, supported owner/admin reassignment, or platform support exposing the required controls. This run makes **no scheduler change**.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  predecessor_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2 / I0076"
  predecessor_target: "FBM + BBM + independence of the two complete centered half-paths at an arbitrary random time T => 2BM?"
  predecessor_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  predecessor_before: "2/4"
  predecessor_after: "2/4"
  predecessor_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  surviving_frozen_candidate: false
  successor_screen_source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
  successor_metric: E_ready
  successor_before: 0
  successor_after: 0
  successor_status: "NO_ADMISSION_MOVEMENT / SCREENING_ONLY / NOT_CLOSABLE_READY"
  unchanged_count: UNKNOWN
  tried_moves: [8, 19, 30]
  new_results:
    - "R15-F0111-PASCAL: F_{m+1,k}=F_{m,k}+Phi(s,G_{m,k})"
    - "exact local gap recursion"
    - "R15-F0111-GAP-MONO: gaps decrease in k and increase under coordinate insertion"
    - "R15-F0111-TAIL: F_{n,k}(t)<=sum of any n-k+1 selected activity coordinates"
    - "soft-min tropical insertion rule and exact zero-boundary completion"
  remaining_obligation: "find a source-clean current-open ownership-clear genuinely CLOSABLE successor; for F0111, control the overlapping-block gap profile by budget-compatible positive multilinear majorants or produce a source-valid multiscale obstruction"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_0824Z_successor_admission_f0111_schur_ties_v53c.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-18T085900Z/status.md"
    - "operations/claims/I0077.md"
  audit_ids: []
```

Next fresh Section-B moves if the admission gate remains empty: **#9 RANDOMIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #25 COUNT THE SAME THING TWICE**. They should be replaced if intervening R15 history uses them before the next invocation.
