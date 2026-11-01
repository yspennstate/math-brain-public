Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `d_bad = +infinity -> +infinity`; Section-B methods #23 DO WHAT THE PROPOSER DID NOT EXPECT, #7 TAKE THE LIMIT, and #21 ASK WHO ELSE HAS THIS SHAPE were genuinely attempted and together prove that the literal even-dimensional positive-Maclaurin-coefficient clause of P0411 fails in every even dimension.**

# NM13-05 — P0411: all even-dimensional positive-coefficient claims fail by a complex singularity / Pringsheim argument

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-05` / `proofnet24/NM13-05/`  
Canonical source claim: `P0411`  
Category: **CLOSABLE OUTSIDE**  
Canonical dedup key: `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`  
Canonical SHA-256: `55ed478fc4a65273f15d74d172f46ee938595061ac9a7d82ad3a03afcfd6c1cc`  
Selection shard: `4 mod 13`  
Run date: 2026-09-19 UTC

## 1. Runtime truth and control-plane status

The prompt requests GPT-6 with maximum reasoning, but this invocation actually runs as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed scheduled-task control surface still offers title/prompt, schedule/start configuration, timing mode, enabled state, and ordinary update controls. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-runtime receipt**. Therefore GPT-6/maximum remains prompt text only. Making it binding would require an authorized product/workspace/API/admin surface that persists model/reasoning fields into inference routing and returns trustworthy applied-runtime metadata.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary, not a mathematical event. The compliant remedy is the task-owning or otherwise authorized account/workspace/API/admin context, ownership repair/transfer, or authorized platform support for that same task; never clone the task or bypass access controls. No schedule or permission was modified in this invocation.

## 2. Authoritative continuity recovered

I continued the already admitted P0411 target from the immutable predecessor

`proofnet24/NM13-05/runs/2026-09-19/2026-09-19T07-31-30Z__p0411-strict-ifr-sharp-tail-asymptotic.md`

created at commit `bc499a1e25d639596181984f8894f3fdb2b6c186`.

Before new mathematics I reread or recovered the current controlling and source state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0411.md`;
- prior attempt `P0411-A001` and `probability_campaign_2026_09/codex_20h_20260906/proofs/IPVT_boundary_hole_partial.md`;
- newest visible neighboring NM13-06 and current P26 audit activity;
- current primary source and 2026 author/follow-up literature.

The current claim still names `proofnet24/NM13-05` as exclusive owner. No handoff, retirement, release, claim deletion, source-scope mutation, or audit PASS for P0411 was recovered. The newest NM13-06 continuity explicitly treats P0411 as owned by NM13-05 rather than as free inventory. P26 activity in the recovered interval concerns other packages, not P0411.

The frozen marginal family and metric therefore remain unchanged:

`R_d := d_H(o, partial C_d), d>=2`,  
`H_d(u):=P(R_d>=u)`, `g_d(u):=-H_d'(u)`,  
`d_bad := min{d>=2 : g_d is not nonincreasing on [0,infinity)}`, with `+infinity` if the set is empty.

The predecessor established `d_bad=+infinity` and, more strongly, strict increasing hazard / log-concave survival and a sharp tail asymptotic. This run does **not** replace that metric with a coefficient count.

## 3. Frozen repository delta before this write

Predecessor creation commit: `bc499a1e25d639596181984f8894f3fdb2b6c186`.  
Frozen pre-write `master`: `961cbc86dbfa16235d6a2d7c897adfce8f9605fa`.

The exact Git comparison is **108 commits ahead and 0 behind**. The interval contains substantial concurrent fleet work but no P0411 ownership release, no P0411 source/attempt rewrite that invalidates the target, and no P0411 audit PASS. The canonical claim remains active and exclusive to NM13-05.

No shared root, peer namespace, D-series file, workflow, permission, public surface, email/Drive resource, paid-compute resource, or schedule is edited by this run. The only write is this immutable report.

## 4. Exact source clause and bounded literature refresh

Primary source: Matteo D'Achille, Nicolas Curien, Nathanael Enriquez, Russell Lyons, Meltem Unel, *Ideal Poisson-Voronoi tessellations on hyperbolic spaces*, **Annals of Probability 54(2) (2026), 846-891**, DOI `10.1214/25-AOP1781`.

Conjecture 7.5 states, in the displayed distance variable `u`, that for even `d`

`H_d(u)=e^{-(d-1)u}/f(u)`

where `f` is an **infinite power series with positive coefficients** (the coefficients are further conjectured to be rational linear combinations of `1` and `1/pi`). The same conjecture also contains the scaled-hole monotonicity and decreasing-boundary-density clauses treated in earlier runs.

The archived campaign attempt `P0411-A001` had already found the exact `d=2` Maclaurin obstruction

`[u^6](e^{-u}/H_2(u)) = 61/240 - 4/(5*pi) < 0`.

That is prior campaign work and is not relabeled as NM13-05 progress. It nevertheless left an interpretation concern: perhaps the `d=2` coefficient failure was isolated, or perhaps a different transformed variable was intended. The present run attacks the literal displayed-variable clause structurally in **every even dimension**.

Fresh bounded searches dated 2026-09-19 used the exact source title with `Conjecture 7.5`, `positive coefficients`, `boundary distance`, and current-author/follow-up terms. They recovered:

- the 2026 Annals source itself;
- D'Achille-Thale, *Face volume densities of positive-intensity and ideal Poisson--Voronoi tessellations in hyperbolic spaces*, arXiv:2606.26049 (2026-06-24);
- D'Achille-Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517 (2026-06-29);
- Mellick's 2026 resolution of the separate indistinguishability question.

None of the retrieved sources states a resolution of the even-dimensional positive-Maclaurin-coefficient clause. This is a **bounded negative search**, not proof of worldwide novelty or priority. The complex-analytic mechanism below uses the classical **Pringsheim theorem** for nonnegative-coefficient power series; that theorem is standard prior art and is not claimed as new.

## 5. Frozen metric and counters

- metric before: **`d_bad=+infinity`**;
- metric after: **`d_bad=+infinity`**;
- metric movement: **NO MOVEMENT**;
- unchanged-run counter after the metric-setting run: **`1 -> 2`**;
- stuck/recovery count: **`0 -> 0`**.

There is genuine source-level progress below, but it does not alter the deliberately frozen density-monotonicity threshold.

## 6. Three new Section-B attacks

### #23 — DO WHAT THE PROPOSER DID NOT EXPECT

Instead of trying to prove positivity in higher even dimensions, assume the opposite: the `d=2` negative coefficient is not sporadic and **every even dimension must eventually have a negative Maclaurin coefficient**. The question becomes structural: what obstruction forces a positive-coefficient generating function to fail?

Outcome: **succeeded** after coupling it to #7 and #21. The obstruction is a nonremovable complex singularity off the positive real axis together with Pringsheim's theorem.

### #7 — TAKE THE LIMIT

Do not inspect one more coefficient. Move to the analytic boundary of the exact integral after setting `q=e^{2u}`. For even `d`, the radial exponent is half-integral. The first branch point occurs at `q=-1`; approaching it from the right reveals a logarithmically divergent derivative.

Outcome: **succeeded**. The relevant derivative is computed exactly below and proves that `q=-1` is a genuine singularity.

### #21 — ASK WHO ELSE HAS THIS SHAPE

A power series with nonnegative coefficients is a classical analytic-combinatorics object. Pringsheim's theorem says that if such a series has finite radius of convergence, then the positive real point at that radius is singular. But the IPVT function is analytic at every positive real `u`. Thus any finite complex singularity contradicts all-nonnegative Maclaurin coefficients.

Outcome: **succeeded**. The complex singularity furnished by #7 and Pringsheim together refute the literal positive-coefficient clause in every even dimension.

## 7. New theorem — every even dimension has a negative Maclaurin coefficient

Let `d>=2` be even and put

`n:=d-1` (so `n` is odd),  
`alpha:=(n-2)/2` (so `alpha` is a half-integer),  
`F_n(u):=e^{-nu}/H_d(u)`.

The source's even-dimensional positivity clause says precisely that the Maclaurin series of `F_n` in the displayed variable `u` has positive coefficients.

### Theorem

For **every even integer `d>=2`**, the Maclaurin coefficients of

`F_{d-1}(u)=e^{-(d-1)u}/H_d(u)`

cannot all be nonnegative. Equivalently, under the literal/source-displayed Maclaurin-at-zero interpretation, Conjecture 7.5's even-dimensional positive-coefficient clause is false in every even dimension.

This theorem is stronger than the archived `d=2` coefficient witness. It does not identify the first negative coefficient in each higher even dimension; it proves that at least one must occur.

## 8. Full proof

### Step 1. Exact radial representation

The source Proposition 5.1 gives the reciprocal hole probability as an explicit `R^n` integral. The source-faithful polar reduction used in the two predecessor runs gives, with `q=e^{2u}`,

`F_n(u)=G_n(q)`,

where

`G_n(q) = K_n integral_1^infinity (z-1)^alpha z^{-2n} (q+z)^alpha (q+2z-1) dz`,

and

`K_n = Gamma(n)/Gamma(n/2)^2 > 0`.

For real `q>-1`, every factor is real and the integral converges. More importantly, choosing the principal branch of `(q+z)^alpha`, the same integral defines a holomorphic function on the slit plane

`Omega := C \ (-infinity,-1]`.

Indeed, on every compact subset of `Omega`, `q+z` stays uniformly away from the branch cut for `z>=1`, while the large-`z` kernel and all fixed-order `q` derivatives have integrable polynomial domination. Thus differentiation under the integral is legitimate on compact subsets of `Omega`.

Since `q=e^{2u}` maps a neighborhood of `u=0` into `Omega`, `F_n` is holomorphic near `u=0`. It is also holomorphic in a neighborhood of **every positive real `u`**, because then `q>0` is an interior point of `Omega`.

### Step 2. Differentiate to the first logarithmic singular order

Write

`B(q,z):=(q+z)^alpha(q+2z-1)`.

For every integer `k>=1`, direct differentiation gives

`partial_q^k B(q,z)`

`= (alpha)_(k-1) (q+z)^(alpha-k) * [ (alpha-k+1)(q+2z-1) + k(q+z) ]`,

where `(alpha)_(k-1)=alpha(alpha-1)...(alpha-k+2)` is the falling factorial (and equals `1` when `k=1`).

Take `k=n+1` and approach the slit endpoint from the right:

`q=-1+epsilon`, `epsilon>0`, `z=1+t`.

Then

`q+z=epsilon+t`,  
`q+2z-1=epsilon+2t`,

and because `alpha=(n-2)/2`, the bracket simplifies **exactly** to

`(n/2) epsilon - t`.

Hence

`G_n^(n+1)(-1+epsilon)`

`= K_n (alpha)_n integral_0^infinity t^alpha (1+t)^(-2n) (epsilon+t)^(alpha-n-1) ((n/2)epsilon-t) dt`.

Because `alpha` is half-integral, `(alpha)_n != 0`.

Scale `t=epsilon s`. Since `2alpha=n-2`, all powers of `epsilon` combine to `epsilon^(-1)`:

`G_n^(n+1)(-1+epsilon)`

`= K_n (alpha)_n epsilon^(-1) integral_0^infinity B_n(s)(1+epsilon s)^(-2n) ds`,

where

`B_n(s):=s^alpha(1+s)^(alpha-n-1)(n/2-s)`.

### Step 3. The zeroth-order integral cancels exactly

The cancellation responsible for the logarithm is exact. Since `alpha+1=n/2`, beta integrals give

`integral_0^infinity B_n(s) ds`

`= (n/2) B(n/2,2) - B((n+2)/2,1)`

`= (n/2) * 4/(n(n+2)) - 2/(n+2)`

`= 0`.

Therefore

`integral B_n(s)(1+epsilon s)^(-2n) ds`

`= integral B_n(s)[(1+epsilon s)^(-2n)-1] ds`.

Also, direct expansion at infinity gives

`B_n(s) = -s^(-2) + O(s^(-3))`.

### Step 4. Exact logarithmic asymptotic

Split the last integral into `s in (0,1)`, `s in [1,epsilon^(-1)]`, and `s>epsilon^(-1)`.

On `(0,1)`, the bracket is `O(epsilon s)` and `B_n(s)` is integrable (`alpha>=-1/2`), so the contribution is `O(epsilon)`.

On `[1,epsilon^(-1)]`, uniformly `0<=epsilon s<=1`,

`(1+epsilon s)^(-2n)-1 = -2n epsilon s + O_n(epsilon^2 s^2)`.

Together with `B_n(s)=-s^(-2)+O(s^(-3))`, this gives

`B_n(s)[(1+epsilon s)^(-2n)-1]`

`= 2n epsilon/s + O_n(epsilon/s^2) + O_n(epsilon^2)`.

Integrating from `1` to `epsilon^(-1)` yields

`2n epsilon log(1/epsilon) + O_n(epsilon)`.

Finally, on `(epsilon^(-1),infinity)`, the bracket is bounded and `B_n(s)=O(s^(-2))`, so the contribution is again `O(epsilon)`.

Thus

`integral_0^infinity B_n(s)(1+epsilon s)^(-2n) ds`

`= 2n epsilon log(1/epsilon) + O_n(epsilon)`.

Substituting into Step 2 gives the decisive asymptotic

`G_n^(n+1)(-1+epsilon)`

`= 2n K_n (alpha)_n log(1/epsilon) + O_n(1)`.

Because `K_n>0` and `(alpha)_n!=0`, the derivative diverges logarithmically in magnitude as `epsilon downarrow 0`. Therefore **`q=-1` is a genuine, nonremovable singularity of `G_n`**.

### Step 5. Transport the singularity to the `u`-plane

The map `q=e^{2u}` is locally biholomorphic at

`u_0=i*pi/2`, because `e^{2u_0}=-1` and `(d/du)e^{2u}|_{u_0}=-2 != 0`.

If `F_n(u)=G_n(e^{2u})` were holomorphic at `u_0`, local inversion of `q=e^{2u}` would make `G_n` holomorphic at `q=-1`, contradicting Step 4. Hence `u=i*pi/2` is a genuine complex singularity of the analytic germ of `F_n` at zero.

Consequently, the Maclaurin series of `F_n` has **finite** radius of convergence `R` (indeed `R<=pi/2`; an exact value is not needed).

### Step 6. Pringsheim contradiction

Assume, for contradiction, that every Maclaurin coefficient of `F_n` is nonnegative. The classical Pringsheim theorem then says that for a power series with nonnegative real coefficients and finite radius `R`, the positive real boundary point `u=R` is a singularity.

But Step 1 showed that `F_n` is holomorphic in a neighborhood of **every positive real `u`**: for `u>0`, `q=e^{2u}>0` lies strictly inside the slit domain `Omega` of the exact integral.

This contradiction proves that the Maclaurin coefficients cannot all be nonnegative.

Since the argument used only that `n=d-1` is odd, it applies to **every even `d>=2`**. QED.

## 9. What this proves — and what it does not

### Proved candidate in this run

Under the literal/source-displayed Maclaurin-at-zero interpretation of the even-dimensional statement, the positive-coefficient clause is false for **all even dimensions**, not merely `d=2`.

The proof is theorem-sized and is written in full above. No finite enumeration or numerical checker is being used as its certificate. The only imported analytic fact is the classical Pringsheim theorem, explicitly identified as prior art.

### Preserved predecessor results

The predecessor's all-dimensional decreasing-density and strict-IFR results remain unchanged:

- `d_bad=+infinity`;
- `g_d'(u)<0` for every `d>=2`;
- `h_d'(u)>0` for every `d>=2`;
- sharp all-dimensional exponential tail constant and hazard endpoint.

### Source-wide status

The literal Conjecture 7.5 conjunction is therefore a **REFUTED candidate** because one of its universal even-dimensional clauses is false; the old `d=2` exact coefficient already supplied a finite witness, and the present theorem removes the possibility that this is a single-dimensional accident. The monotonicity/density subclauses have separate PROVED-candidate arguments.

This is **not yet fleet CLOSED**. Closure still requires the protocol's two independent OTHER-track audits (P26 and NM13-06) and a sufficiently deep prior-art/source-interpretation audit. If the authors intended a transformed expansion variable rather than the displayed Maclaurin variable `u`, that different statement would require a separate formulation and is not refuted by merely renaming variables here.

## 10. Audit and artifact discipline

Current independent audit count for P0411: **0/2**.

- P26: no recovered P0411 PASS;
- NM13-06: no recovered P0411 PASS.

No new artifact is created in this run. That is deliberate: the new result is analytic, and the full argument is on the page. Manufacturing another checker for the already settled frozen metric would violate the new-methods-first instruction. The archived exact `d=2` coefficient checker belongs to prior campaign work and is not counted as this run's progress.

## 11. Next step

The most valuable next action is not another density lemma. It is to stress-test the complex-singularity proof against the exact source normalization and then obtain the two required independent audits. In particular, an auditor should check:

1. the radial `G_n(q)` representation and branch domain;
2. the `(n+1)`st derivative identity and exact beta cancellation;
3. the logarithmic asymptotic at `q=-1`;
4. the local transport to `u=i*pi/2`;
5. the hypotheses/application of Pringsheim;
6. the literal source meaning of “infinite power series with positive coefficients”.

If those survive, the source-level refutation has a short analytic certificate independent of locating any particular higher-dimensional negative coefficient.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-05
  source_id: P0411
  claim_id: P0411
  category: CLOSABLE_OUTSIDE
  canonical_dedup_key: boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells
  canonical_sha256: 55ed478fc4a65273f15d74d172f46ee938595061ac9a7d82ad3a03afcfd6c1cc
  shard_mod_13: 4
  owner: proofnet24/NM13-05
  metric_name: d_bad
  metric_definition: "min d>=2 where g_d=-H_d' is not nonincreasing; +infinity if none"
  metric_before: +infinity
  metric_after: +infinity
  metric_movement: NO_MOVEMENT
  unchanged_runs_before: 1
  unchanged_runs_after: 2
  recovery_count_before: 0
  recovery_count_after: 0
  methods:
    - number: 23
      name: DO_WHAT_THE_PROPOSER_DID_NOT_EXPECT
      outcome: "SUCCESS: assumed universal even-d coefficient positivity false and found a structural all-even obstruction"
    - number: 7
      name: TAKE_THE_LIMIT
      outcome: "SUCCESS: q -> -1+ exposes logarithmic divergence of G_n^(n+1), proving a genuine complex singularity"
    - number: 21
      name: ASK_WHO_ELSE_HAS_THIS_SHAPE
      outcome: "SUCCESS: classical Pringsheim theorem converts finite complex radius + positive-real analyticity into contradiction with all-nonnegative Maclaurin coefficients"
  new_claims:
    - "For every even d>=2, F_{d-1}(u)=e^{-(d-1)u}/H_d(u) has at least one negative Maclaurin coefficient under the literal displayed-u interpretation."
    - "For odd n=d-1, the exact q-plane continuation G_n has a nonremovable singularity at q=-1; its (n+1)st derivative diverges as 2n K_n (alpha)_n log(1/epsilon)+O(1)."
  preserved_prior_work:
    - "P0411-A001 exact d=2 coefficient [u^6]=61/240-4/(5*pi)<0; not NM13-05 progress"
    - "NM13-05 density monotonicity / strict IFR / sharp tail theorem"
  source_status_candidate: REFUTED_LITERAL_EVEN_COEFFICIENT_CLAUSE
  fleet_closed: false
  independent_audits_required: [P26, NM13-06]
  independent_audits_passed: []
  prior_art_scope: "bounded 2026-09-19 primary/author/follow-up search; no source-matching coefficient resolution found; Pringsheim is classical prior art"
  repository_predecessor_commit: bc499a1e25d639596181984f8894f3fdb2b6c186
  frozen_prewrite_master: 961cbc86dbfa16235d6a2d7c897adfce8f9605fa
  predecessor_to_prewrite_ahead_by: 108
  predecessor_to_prewrite_behind_by: 0
  next_step: "independent audit of the complex singularity + Pringsheim refutation and exact source-variable interpretation; do not change frozen metric"
```

## 13. Safeguards

No shared root ledger was edited. No other track's file was edited. No claim was overwritten. No D-series ownership or closure was touched. No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, or schedule creation/modification occurred. This report is the single immutable write for the invocation.
