Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `epsilon_sep = 3/5 -> 3/5`. Methods actually tried: #3, #14, #16.**

# NM13-05 — D0004 all-n symmetry theorem and exact rational two-point classification

Run UTC: 2026-09-18T00:20:43Z  
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE.  
Canonical source/claim: `D0004`, `operations/claims/D0004.md`.  
Parent source status after this run: **OPEN / PARTIAL**.  
Frozen metric after this run: **exactly `epsilon_sep = 3/5` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

I continued the already admitted D0004 target. I did not reopen intake, create a second claim, or alter any shared ledger.

Canonical identity remains:

- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv:`1411.6190v3`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 `e67bdcaad853cdecbd238c339238d02b54c7704249727749f1fe86428f88b065`;
- SHA256 residue modulo 13: `4`, matching NM13-05's exclusive shard;
- exclusive owner: NM13-05 under `operations/claims/D0004.md`.

Before new mathematics I reread/recovered the controlling policy surfaces `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, and the later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the D0004 claim and D0004 intake/attempt history; my three preceding D0004 reports; the newest recovered neighboring NM13-04 report (`2026-09-17T23-19-15Z__p0457-s3-support-sharpness.md`); and the newest recovered NM13-06 report (`2026-09-17T22-47-00Z__admission-screen-2.md`). A fresh search found no newer NM13-06 report under 2026-09-18. NM13-06 remains admission-pending and has not supplied an audit.

Historical attempt `D0004-A001` proved the `n=2` case and stalled at `n>=3`; it remains preserved and is not recounted as movement. The preceding NM13-05 runs used, in order, methods `#2/#8/#11`, `#5/#15/#20`, and `#18/#19/#24`. The last run proved the frozen smooth two-bump threshold exactly `epsilon_sep=3/5`. Hence this run deliberately uses three methods not previously tried on D0004.

Large root/JSONL files are connector-truncated when fetched wholesale. I used their current visible root views plus exact-ID, dedup-key, claim, attempt, report, and ownership searches; I do not infer that inaccessible/deleted/non-master history is empty. No release, handoff, competing owner, posted D0004 closure, or later source-specific correction was recovered.

The current task-control surface still exposes prompt/title, schedule or relative-start fields, timing mode, and enabled state, but **no binding model-family selector and no reasoning-effort selector**. Therefore the requested `GPT-6 / maximum` remains prompt text only. This invocation actually runs GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so the reasoning level is reported as `UNVERIFIED`. The historical `You cannot modify this task` result for one P26 context is an authorization/context boundary; later repository state records a successful P26 update in another authorized context. A future denial must be handled through the owning account/workspace or an authorized product/admin surface, not by cloning the task or bypassing permissions. No support escalation is claimed here.

## 2. Exact source statement and fresh bounded literature check — 2026-09-18 UTC

I rechecked the source PDF directly. Definition 5 defines a law-determined norm by homogeneity, triangle inequality, definiteness, law invariance, and monotonicity on nonnegative random variables. Theorem 5 states that if `F` is `n`-CM with center `mu`, then for every law-determined norm and every real `t`, with `s=(n mu-t)/(n-1)`, one has

`||(X-t)_+|| <= (n-1)||(X-s)_-||`,

`||(X-t)_-|| <= (n-1)||(X-s)_+||`.

Open Problem 4 then asks: if these inequalities hold for **all** law-determined norms and all thresholds, under what extra conditions (possibly smoothness conditions) are they sufficient for `n`-complete mixability?

Fresh bounded web searches used the exact title and Open Problem 4 wording; `law-determined norm complete mixability`; `complete mixability two-point distribution Bernoulli`; `complete mixability smooth density sufficient conditions`; and current author/joint-mixability queries. I rechecked Wang's current homepage/publications (site updated 14 September 2026), the current joint-mixability working-paper series, Puccetti–Wang's detection literature, and Koike–Lin–Wang, *Joint Mixability and Notions of Negative Dependence*, Mathematics of Operations Research 49(4) (2024). The 2024 paper develops negative-dependence and multimarginal-optimal-transport structure, but does not state a resolution of Open Problem 4. I did not locate a later source-matching solution, nor a paper stating the exact all-law-determined-norm rational two-point criterion proved below.

This is **bounded negative evidence only**. It is not proof of worldwide openness and not a novelty certificate. In particular, the count criterion for complete mixability of a two-point law is elementary/folklore and is not claimed novel. The finite weak-majorization mechanism below is standard Hardy–Littlewood–Pólya / sub-Birkhoff machinery. Publication novelty of the combined criterion remains **UNVERIFIED**.

## 3. Frozen metric: no movement

The claim file freezes the smooth two-bump family

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`,

with `U_epsilon` having an even `C^infinity` density strictly positive on `(-epsilon,epsilon)` and zero outside `[-epsilon,epsilon]`, and tracks

`epsilon_sep = sup{epsilon : every frozen F_epsilon is proved to satisfy all n=3 source norm inequalities but is not 3-CM}`.

The previous run proved

`epsilon_sep = 3/5`.

That value is already exact, and I do not silently replace it with a new quantity. Therefore

**before: `epsilon_sep = 3/5`; after: `epsilon_sep = 3/5`; no frozen-metric movement.**

The new theorem below is source-relevant restricted-class progress despite the frozen scalar being saturated.

---

## 4. Method #3 — PROVE SOMETHING STRONGER: symmetry is invisible to Theorem 5 for every n

The first D0004 run proved the following only at `n=3`: every distribution symmetric about its mean satisfies all of Theorem 5's law-determined-norm inequalities. The same mechanism actually works for **every** `n>=2`.

### Theorem D0004-SYM-N

Let `n>=2`, let `F` be integrable and symmetric about its mean `mu`, and let `X~F`. Then for every law-determined norm in Wang's Definition 5 and every real threshold `t`, both Theorem-5 inequalities hold.

### Proof

Translate by `mu`; it is enough to treat `mu=0`. Put `m=n-1`.

For the positive-part inequality we must prove

`||(X-t)_+|| <= m ||(X+t/m)_-||`.  (1)

First suppose `t>=0`. By symmetry,

`(X+t/m)_- = (-X-t/m)_+  =^d  (X-t/m)_+`.

Since `t/m <= t`, pointwise

`0 <= (X-t)_+ <= (X-t/m)_+`.

Monotonicity and `m>=1` give (1).

Now suppose `t<0`, and write `t=-mc` with `c>0`. By symmetry,

`(X-c)_-=(c-X)_+ =^d (X+c)_+`.

Set

`A=(X+c)_+`, `B=(-X+c)_+`.

Then `A =^d B`. Pointwise,

`A+B >= 2c`,

so by monotonicity, homogeneity, the triangle inequality, and law invariance,

`2||c|| = ||2c|| <= ||A+B|| <= ||A||+||B|| = 2||A||`.

Hence `||c||<=||A||`. Also pointwise

`(X+mc)_+ <= (X+c)_+ + (m-1)c = A+(m-1)c`.

Therefore

`||(X+mc)_+|| <= ||A||+(m-1)||c|| <= m||A||`,

which is exactly (1).

The negative-part inequality follows either by repeating the argument or by replacing `X` by `-X` and `t` by `-t`. QED.

### Consequence

For every odd `n>=3`, the symmetric Rademacher law gives an immediate discrete example satisfying all source inequalities but failing `n`-CM, since an odd number of `+1/-1` values cannot sum to zero. For even `n`, every symmetric law is itself `n`-CM by pairing opposite copies, so asymmetry is where a two-point counterexample must live. This observation motivated the exact classification below rather than another isolated example.

---

## 5. Method #14 — FIND THE GROUP ACTING: affine normalization and the sign-flip involution

Consider a nondegenerate two-point law with **rational atom probability**. Translation and positive scaling preserve both `n`-complete mixability and the source Theorem-5 property (with the threshold transformed accordingly). Thus every such mean-zero law can be normalized to

`F_q = q delta_p + p delta_{-q}`,  where `p=1-q`, `q in Q intersect (0,1)`.

Indeed, `q p + p(-q)=0`.

The key involution is sign flip:

`-F_q = F_p`, so `q <-> p=1-q`.

Under the same transformation the source positive-part inequality becomes the negative-part inequality. Thus one only has to solve the positive-part inequality and then invoke the involution. It also predicts that the admissible interval must be symmetric around `q=1/2`.

To handle **every law-determined norm** without assuming any unproved infinite-dimensional characterization, I stay inside the rational-mass class. If `q=a/N` in lowest terms, realize `F_q` on `N` equiprobable atoms. For nonnegative `N`-vectors `u,v`, the standard finite Fan/Hardy–Littlewood–Pólya dominance principle says:

> if the sorted prefix sums satisfy `sum_{i<=k} u_i^down <= sum_{i<=k} v_i^down` for every `k`, then `||u||<=||v||` for every law-determined norm restricted to these `N` equal atoms.

For completeness, the finite proof uses no classification theorem. Weak majorization is equivalent to `u=Dv` for a doubly substochastic matrix `D`. The finite sub-Birkhoff theorem writes `D` as a convex combination of subpermutation matrices. For nonnegative `v`, every subpermutation image is coordinatewise bounded by a full permutation image after filling unused rows. Monotonicity and law invariance bound each such image by `||v||`; the triangle inequality and homogeneity then bound their convex combination by `||v||`.

This finite reduction is why rational atom masses form a genuinely complete, source-faithful special class rather than a numerical approximation.

---

## 6. Exact rational two-point classification for every n

### Theorem D0004-TWOPOINT-CLASS

Fix `n>=2` and a rational `q in (0,1)`. Put `p=1-q` and let

`X = p` with probability `q`,
`X = -q` with probability `p`.

Then:

1. **All-norm criterion.** Wang's two Theorem-5 inequalities hold for every law-determined norm and every threshold `t` **iff**

   `1/n <= q <= (n-1)/n`.

2. **Complete-mixability criterion.** `F_q` is `n`-CM **iff**

   `n q` is an integer.

Consequently, within the rational two-point class, the source norm condition is sufficient exactly at

`q in {1/n, 2/n, ..., (n-1)/n}`,

and is insufficient at every other rational `q` in the full interval `[1/n,(n-1)/n]`.

In particular, for every `n>=3`, the explicit choice

`q=1/(n-1)`

satisfies all source inequalities but is not `n`-CM (because `n/(n-1)` is not an integer).

### Proof of Part 1: necessity

Use the law-determined `L^infinity` norm at threshold `t=0`. The positive-part inequality gives

`p <= (n-1)q`,

hence `q>=1/n`. The negative-part inequality gives

`q <= (n-1)p`,

hence `q<=(n-1)/n`.

### Proof of Part 1: sufficiency

Assume

`1/n <= q <= (n-1)/n`.

Set `m=n-1`. It is enough to prove the positive-part inequality; the negative-part inequality follows from the sign-flip involution `q<->p`.

By homogeneity, the positive-part inequality is equivalent to

`||U_t|| <= ||V_t||`,

where

`U_t=(X-t)_+`,
`V_t=m(X+t/m)_- = (-mX-t)_+`.

On the positive atom `X=p` and the negative atom `X=-q`, these variables take the values

`U_t:  a=(p-t)_+` with probability `q`, and `c=(-q-t)_+` with probability `p`;

`V_t:  b=(mq-t)_+` with probability `p`, and `d=(-mp-t)_+` with probability `q`.

Always `a>=c` and `b>=d`. Because `q` lies in the stated interval,

`p <= mq`,  `q <= mp`,

so

`-mp <= -q <= p <= mq`.

Also `a<=b` and `c<=b` for every `t`.

Let

`D(t)=E[V_t]-E[U_t]`.

Direct calculation on the four breakpoint intervals gives

`D(t)=0`, for `t<=-mp`;

`D(t)=q(mp+t)`, for `-mp<=t<=-q`;

`D(t)=(m-1)pq+(2q-1)t`, for `-q<=t<=p`;

`D(t)=p(mq-t)`, for `p<=t<=mq`;

`D(t)=0`, for `t>=mq`.

The first, second, fourth, and fifth pieces are visibly nonnegative. On the middle interval:

- if `q<=1/2`, its slope is nonpositive, so the minimum is at `t=p`, where

  `D(p)=p((m+1)q-1)=p(nq-1)>=0`;

- if `q>=1/2`, its slope is nonnegative, so the minimum is at `t=-q`, where

  `D(-q)=q(m-(m+1)q)=q((n-1)-nq)>=0`.

Thus `D(t)>=0` for every `t`.

It remains to check every sorted prefix, not only the total sum. Because each vector has just two levels, this is exact.

#### Case A: `q<=p`

The high value of `U_t` occupies fraction `q`; the high value of `V_t` occupies fraction `p`. Up to fraction `q`, prefix domination follows from `a<=b`. Between fractions `q` and `p`, it follows from both `a<=b` and `c<=b`. From fraction `p` to `1`, the difference of the two integrated decreasing rearrangements is affine; it is nonnegative at fraction `p` by the preceding inequalities and nonnegative at fraction `1` because `D(t)>=0`. Hence every prefix is dominated.

#### Case B: `q>=p`

Up to fraction `p`, prefix domination again follows from `a<=b`. Between `p` and `q` it suffices, by linearity, to check the endpoint at fraction `q`. Define

`J(t)=H_{V_t}(q)-H_{U_t}(q)=p b+(q-p)d-q a`,

where `H_Z(r)` is the integral of the decreasing rearrangement of `Z` over `[0,r]`. Exact simplification gives

`J(t)=p(m-(m+1)q)`, for `t<=-mp`;

`J(t)=(m-1)pq+(2q-1)t`, for `-mp<=t<=p`;

and `J(t)=p(mq-t)_+ >=0` for `t>=p`.

Since now `2q-1>=0`, the middle expression is minimized at `t=-mp`, where it equals

`p(m-(m+1)q)=p((n-1)-nq)>=0`.

Thus the prefix gap is nonnegative at fraction `q`. From `q` to `1` it is affine and is nonnegative at the other endpoint because `D(t)>=0`. Again every prefix is dominated.

Therefore `U_t` is weakly majorized by `V_t` on an equal-atom realization of the rational law. The finite dominance principle above yields `||U_t||<=||V_t||` for **every** law-determined norm. The sign-flip involution gives the second Theorem-5 inequality. This proves Part 1.

### Proof of Part 2

Take any coupling `(X_1,...,X_n)` of `n` copies of `F_q` and let `K` be the number of coordinates equal to the positive value `p`. Then pointwise

`X_1+...+X_n = K p -(n-K)q = K-nq`.

Since the marginal mean is zero, an `n`-complete mix must have sum zero almost surely. Thus necessarily

`K=nq`

almost surely, which forces `nq` to be an integer.

Conversely, if `k=nq` is an integer, take a deterministic vector with exactly `k` entries equal to `p` and `n-k` entries equal to `-q`, and uniformly permute its coordinates. Each coordinate has probability `k/n=q` of taking the positive value, and the sum is

`k-nq=0`.

Hence the law is `n`-CM. QED.

### Source-level meaning

The theorem gives a complete answer on one explicit marginal class. The source all-norm test detects only the interval

`1/n <= q <= 1-1/n`,

whereas exact complete mixability detects the discrete arithmetic lattice

`q=k/n`.

Thus the obstruction missed by every law-determined norm in Theorem 5 is not merely geometric; even for a two-point law it can be a discrete integrality constraint. This is a complete restricted-class theorem, not a solution of Open Problem 4's requested general extra-condition characterization.

---

## 7. Method #16 — COMPUTE SMALL CASES, THEN REMOVE THE COMPUTATION

Before the analytic proof above, I used exact rational arithmetic on small `n` and small rational atom masses to inspect all breakpoints of the two step functions and every sorted prefix sum. The experiments consistently showed the interval

`q in [1/n,(n-1)/n]`

for the all-norm condition and the arithmetic sublattice `nq in Z` for actual complete mixability. That pattern suggested the two scalar quantities `D(t)` and `J(t)` used in the proof.

This finite scan is **route-selection only**. I do not promote its finite coverage as a mathematical claim, do not use it as evidence for the theorem, and therefore do not manufacture an artifact merely to certify a computation superseded by the exact argument. The theorem is proved on the page for every `n` and every rational `q` in the stated class.

---

## 8. Refutation/self-checks of the new theorem

I attacked the likely failure points rather than assuming the interval proof was correct.

First, the necessity endpoints are forced by `L^infinity`, which is explicitly listed as a law-determined norm in the source. Second, the sufficiency proof does not assume a characterization of arbitrary infinite-dimensional law-determined norms: rational atom mass lets us realize the law on finitely many equal atoms and use the finite sub-Birkhoff argument. Third, the breakpoint order `-mp<=-q<=p<=mq` is exactly equivalent to the two endpoint inequalities `q<=m/(m+1)` and `q>=1/(m+1)`; outside that interval the `L^infinity` test already fails. Fourth, the sign-flip map converts the second source inequality exactly into the first with `q` and `p` exchanged. Fifth, the complete-mixability criterion is pointwise: the sum is `K-nq`, so there is no hidden coupling capable of evading the integer count.

I found no gap in the theorem as stated. The rationality restriction is deliberate: it keeps the all-norm dominance argument finite and exact. I do **not** claim the same proof establishes the all-norm criterion for irrational two-point masses; extending it would require an additional theorem about arbitrary law-determined norms that the source itself explicitly flags as an interesting characterization problem.

## 9. What is and is not proved

New theorem-sized results in this run:

- `D0004-SYM-N`: every integrable law symmetric about its mean satisfies all of Wang's Theorem-5 norm inequalities for every `n>=2`;
- `D0004-TWOPOINT-CLASS`: for rational-mass mean-zero two-point laws, the all-law-determined-norm criterion is exactly `1/n<=q<=(n-1)/n`, while exact `n`-complete mixability is exactly `nq in Z`;
- consequently, for every `n>=3` there is an explicit rational two-point law satisfying every source norm inequality but failing `n`-CM.

Not proved:

- a general characterization of the extra hypotheses that make Theorem 5 sufficient;
- the analogous all-norm classification for irrational two-point atom masses;
- a finite-support classification beyond two points;
- a new improvement to the already exact frozen smooth-family metric `epsilon_sep=3/5`;
- publication novelty beyond the bounded search;
- source-level closure;
- any P26 or NM13-06 audit.

Therefore D0004 remains **OPEN / NM13-05 PARTIAL**.

## 10. Counters and next route

The previous run moved the frozen metric, so the unchanged-run counter before this invocation was `0`.

After this invocation:

- frozen metric: `3/5 -> 3/5`;
- `unchanged_runs_since_metric_movement = 1`;
- `stuck_recoveries_used = 0`;
- P26 audit: not counted;
- NM13-06 audit: not counted.

Do not repeat `#3/#14/#16` next run. The next source-relevant target is the **three-point rational class**, where the two-point arithmetic obstruction becomes a small transportation polytope rather than one integer count. Planned new methods:

- **#1 CHANGE THE CATEGORY:** translate the three-point all-norm conditions into a finite polyhedral/matrix problem on equal atoms;
- **#25 COUNT THE SAME THING TWICE:** compare the integer composition counts forced by a constant-sum coupling with the marginal counts;
- **#30 ONE SCALE/ONE SUPPORT SIZE AT A TIME:** solve one denominator/support size exactly before attempting a general three-point theorem.

If the frozen metric remains unchanged for three consecutive runs, the Section-I thinking-only stuck protocol will trigger even if restricted-class theorems continue to accumulate. The closable-track six-unchanged rotation rule remains binding; I will not rename a new class cutoff as the frozen metric.

## 11. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-05
  canonical_id: D0004
  category: CLOSABLE_OUTSIDE
  source: "Ruodu Wang (2015), Current Open Questions in Complete Mixability, Open Problem 4"
  claim_path: operations/claims/D0004.md
  source_status: OPEN
  mathematical_status: PARTIAL
  frozen_metric: epsilon_sep
  metric_before: "= 3/5"
  metric_after: "= 3/5"
  movement: false
  methods_tried: [3, 14, 16]
  new_internal_theorems:
    - D0004-SYM-N
    - D0004-TWOPOINT-CLASS
  unchanged_runs_before: 0
  unchanged_runs_after: 1
  stuck_recoveries_used: 0
  p26_audit: NOT_COUNTED
  secondary_audit_partner: NM13-06
  secondary_audit: NOT_COUNTED
  next_methods: [1, 25, 30]
  next_step: "Attack the rational three-point class as an equal-atom transportation/polyhedral problem without changing epsilon_sep."
  bounded_literature_check_date_utc: 2026-09-18
  novelty: UNVERIFIED
```

No shared root, peer namespace, historical report, claim file, schedule, workflow, email, Drive item, or public site was modified by this invocation.