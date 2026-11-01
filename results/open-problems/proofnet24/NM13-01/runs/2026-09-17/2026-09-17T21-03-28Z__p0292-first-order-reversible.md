Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. Movement: `D_rev,0` UNMEASURED -> **0 exactly**. Methods actually tried: **#2, #11, #24**.

# NM13-01 — P0292 first research attack

## 1. Status

- Track: NM13-01, CLOSABLE OUTSIDE.
- Source target: P0292 = Lasse Leskelä (2022), *Ross's second conjecture and supermodular stochastic ordering*, Problem 4.
- Canonical claim: `operations/claims/P0292.md`, created this run at commit `949e138d4b6069321b2f2afc705c45d771662dc5` and read back there.
- Source-level status after this run: **OPEN**.
- This report proves a theorem-sized **PARTIAL** result for every finite stationary irreducible reversible CTMC. It does **not** give the necessary-and-sufficient characterization requested by Problem 4 and does not certify novelty.
- No finite checker is needed for the theorem below; its full proof is on this page. Historical floating-point/LP experiments are treated only as prior exploratory evidence and are not promoted to certificates.

## 2. Required continuity and admission check

The run re-read `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, the canonical campaign catalogue, and the recovered P0292 attempt/scripts. There was no previous NM13-01 run report, and a bounded search found no NM13-02 run report yet.

Canonical dedup key: `characterize_ctmc_speed_monotonicity_in_supermodular_order`.
Its SHA256 is `3aded70a56a908e9042798ee4a8ac614005a51635e52453716ea79167c073ae5`, whose integer value is `0 mod 13`, so P0292 is in NM13-01's shard.

P0292 is not virgin inventory. The recovered campaign row says `attempted_unsolved`. The strongest recovered prior result, `P0292-A002`, studied the reversible three-state star

`1 -> 2 at a2, 1 -> 3 at a3, 2 -> 1 at b2, 3 -> 1 at b3`.

It records: source order failure when `b3>b2`; a full proof in the equal-exit case `b2=b3`; and the still-unproved star conjecture that the source order holds exactly when `b2>=b3`. Existing numerical LP maps sampled the remaining region and a slow-eigenvector sign criterion, but do not prove the all-dimensional source order. This run preserves that history and does not count it as movement.

Immediately before claiming, `operations/claims/P0292.md` was absent. Repository searches found P0292 only in historical intake/attempt/scripts/rankings, not in a live exclusive claim, worker assignment, POSTED exclusion, or current RESULTS row. P0289/Problem 1 and P0291/Problem 3 are different source scopes and remain excluded from reopening.

### Fresh source/literature screen — 2026-09-17 UTC

Primary source was read from the accepted-author PDF, DOI `10.1007/s11134-022-09824-0`, source page 215. Problem 4 asks for a simple necessary and sufficient condition on a stationary ergodic CTMC for

`c1 <= c2  ==>  lambda_{c1} >=_sm lambda_{c2}`,

for **all** finite-dimensional supermodular tests. The source says that outside stochastically monotone CTMCs little was known even for three states and that the discrete-time analogue was likewise open at publication.

Fresh bounded searches of the exact Problem-4 wording, supermodular time-scale ordering, the author's publication page, and later/citing literature recovered the 2022 source and older dependence-in-lag literature (notably Hu--Pan 2000 and later dependence-in-lag work), but no later source-matching general characterization. This is only a bounded negative search. It is **not** proof of global openness or novelty of the theorem below.

## 3. Frozen metric

For a finite stationary irreducible reversible CTMC `X` with ordered state values, observation times

`0=t_1 <= t_2 <= ... <= t_n=1`,

and a bounded supermodular test `phi` with `|phi|<=1`, set

`F_phi(c)=E[phi(X_{c t_1},...,X_{c t_n})]`.

The claim freezes the local extremal defect

`D_rev,0 = sup F_phi'(0+)`,

where the supremum is over all such finite reversible chains, all `n>=2`, all normalized observation vectors, and all such tests. A positive value would be an infinitesimal counterexample to Leskelä's required monotonic decrease in speed. The baseline before this attack was **UNMEASURED**.

This run proves the sharp value

`D_rev,0 = 0`.

The zero is sharp because every additive/modular test `phi(x_1,...,x_n)=sum_k h_k(x_k)` has speed-independent expectation under stationarity and hence derivative zero.

## 4. New theorem — no first-order frozen-limit obstruction for reversible chains

### Theorem NM13-01-P0292-REVERSIBLE-FROZEN-DERIVATIVE-01

Let `X=(X_t)_{t>=0}` be a finite-state stationary reversible continuous-time Markov chain. Embed its distinct states in increasing real order. Fix `n>=2`, times

`0=t_1 <= ... <= t_n`,

and any supermodular function `phi` on the product of the ordered state space. Define

`F(c)=E phi(X_{c t_1},...,X_{c t_n})`.

Then the right derivative at the frozen endpoint exists and satisfies

`F'(0+) <= 0`.

More precisely, writing `Delta_k=t_{k+1}-t_k`, generator `Q=(q_ij)`, stationary law `pi`, and reversible edge conductance

`w_ij = pi_i q_ij = pi_j q_ji`  for `i != j`,

we have

`F'(0+) = sum_{k=1}^{n-1} Delta_k sum_{i<j} w_ij B_{ij,k}(phi)`,

where

`B_{ij,k}(phi)
 = phi(i^k,j^(n-k)) + phi(j^k,i^(n-k)) - phi(i^n) - phi(j^n) <= 0`.

Here `i^k,j^(n-k)` denotes the vector with the first `k` coordinates equal to state `i` and the remaining coordinates equal to state `j`.

Consequently the normalized extremal constant frozen in this track is exactly

`D_rev,0=0`.

### Proof

Let `P_t=e^{tQ}`. Stationarity lets us shift the first observation time to zero. For finite state space,

`P_{c Delta_k}=I+c Delta_k Q+o(c)`

entrywise as `c downarrow 0`. The finite-dimensional expectation is

`F(c)=sum_{x_1,...,x_n} pi_{x_1} phi(x_1,...,x_n)
      product_{k=1}^{n-1} P_{c Delta_k}(x_k,x_{k+1}).`

At `c=0` every transition factor is an identity matrix, so all coordinates coincide. Differentiating at zero, exactly one transition factor can contribute a generator term. Thus

`F'(0+)
 = sum_k Delta_k sum_i pi_i sum_{j!=i} q_ij
   [phi(i^k,j^(n-k))-phi(i^n)].`          (4.1)

Now pair the directed terms `i->j` and `j->i`. Reversibility gives the same nonnegative coefficient `w_ij`. For `i<j`, define

`x=(i^k,j^(n-k))`,  `y=(j^k,i^(n-k))`.

Coordinatewise,

`x wedge y = i^n`,  `x vee y = j^n`.

Supermodularity of `phi` says

`phi(x wedge y)+phi(x vee y) >= phi(x)+phi(y)`.

Equivalently,

`B_{ij,k}(phi)
 = phi(x)+phi(y)-phi(i^n)-phi(j^n) <= 0`.      (4.2)

Using detailed balance in (4.1) and summing each unordered edge once gives

`F'(0+)
 = sum_k Delta_k sum_{i<j} w_ij B_{ij,k}(phi) <= 0`,

because every `Delta_k`, every `w_ij`, and every `-B_{ij,k}` is nonnegative. This proves the derivative claim.

For the metric, the theorem gives `D_rev,0<=0`. If `phi` is additive across coordinates, it is modular and its expectation is `sum_k E h_k(X_{ct_k})`, constant in `c` by stationarity. Hence `F'(0+)=0`, so `D_rev,0>=0`. Therefore `D_rev,0=0`. QED.

### Equality face

The proof also gives an exact equality criterion for a fixed chain/time vector/test:

`F'(0+)=0`

iff every pair `(i,j)` with `w_ij>0` and every split `k` with `Delta_k>0` saturates the corresponding lattice inequality,

`phi(i^n)+phi(j^n)
 = phi(i^k,j^(n-k))+phi(j^k,i^(n-k)).`

This is not a full characterization of source condition (2); it identifies the extremal face invisible to first-order frozen-limit analysis.

## 5. Section-B methods actually tried

### #2 — ATTACK THE NEGATION FIRST

I asked for the cheapest possible counterexample: can a finite reversible CTMC violate the desired speed monotonicity immediately as `c` leaves the frozen endpoint `0`? Formula (4.1), paired by detailed balance, proves the answer is **no** for every dimension and every bounded supermodular test. So any reversible counterexample to Leskelä's full condition must be genuinely nonlocal in the speed parameter: it cannot be witnessed by a positive first derivative at `c=0`.

This kills an entire counterexample mechanism rather than merely failing to find a numerical example.

### #11 — DUALIZE

The key move was to replace the finite-dimensional law comparison by its infinitesimal linear functional on the cone of supermodular tests. Reversibility dualizes directed generator flow into unordered edge conductances `w_ij`; each edge coefficient multiplies exactly one elementary lattice supermodularity slack. This turns the sign question into a sum of manifestly nonpositive terms and gives the theorem.

### #24 — FIND THE EXTREMAL OBJECT

For the normalized local defect, the extremizers are the zero-slack face. Additive/modular tests already attain derivative `0`, proving the upper bound is sharp. The edgewise equality characterization above identifies exactly what a higher-order attack must study: tests for which all first-order edge slacks vanish. This points away from another broad LP sweep and toward second/higher-order generator terms restricted to the equality face.

## 6. What this does and does not settle

What moved:
- exact local defect `D_rev,0`: **UNMEASURED -> 0**;
- a theorem valid for every finite stationary reversible CTMC, every finite observation dimension, and every supermodular test;
- a structural exclusion: reversible source counterexamples, if they exist, cannot emerge to first order from `c=0`.

What remains open:
- Leskelä Problem 4 asks for a necessary-and-sufficient condition valid globally in `c`, not only a frozen-endpoint derivative;
- the unresolved `b2>b3` star regime from P0292-A002 remains unresolved globally;
- nonreversible chains are not covered by the detailed-balance pairing;
- the theorem has not received either required OTHER-track audit and is not called closed or novel.

The most direct next attack is to restrict the second derivative `F''(0+)` to the equality face characterized above, first on the three-state star. A sign theorem there would convert the endpoint calculation into a genuine local interval result; a positive second-order coefficient would give an exact counterexample mechanism to test against the existing star conjecture. Do not repeat #2/#11/#24 as the next method triple.

## 7. Runtime/model control

The exposed scheduler/runtime control surface in this context still has title, prompt, schedule, enablement and timing mode but no binding model selector and no reasoning-effort selector. Therefore the requested `GPT-6 / maximum` is prompt text only. This invocation actually identifies as **GPT-5.6 Sol**; authenticated reasoning level is **UNVERIFIED**. Nothing in this report claims otherwise or claims an hour-long guaranteed execution.

The dated owner policy records historical modification denials for P26/P01/P03 in one context. They were not retested by NM13-01 in this research invocation. The lawful resolution is an authorized owner/admin/product interface that exposes the setting or permission; no duplicate job or permission bypass is attempted.

## 8. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-01
  allocation: CLOSABLE_OUTSIDE
  canonical_problem: P0292
  canonical_dedup_key: characterize_ctmc_speed_monotonicity_in_supermodular_order
  source: "Leskela 2022, Ross's second conjecture and supermodular stochastic ordering, Problem 4"
  claim_path: operations/claims/P0292.md
  claim_creation_commit: 949e138d4b6069321b2f2afc705c45d771662dc5
  source_status: OPEN
  mathematical_status: PARTIAL
  metric: D_rev,0
  before: UNMEASURED
  after: 0
  movement: true
  new_claim: NM13-01-P0292-REVERSIBLE-FROZEN-DERIVATIVE-01
  theorem_scope: "finite stationary irreducible reversible CTMCs; frozen-endpoint first derivative; all finite-dimensional bounded supermodular tests"
  section_B_methods: [2, 11, 24]
  unchanged_run_count: 0
  audits:
    P26: PENDING
    NM13-02: PENDING
  prior_art: "bounded fresh search 2026-09-17; novelty UNVERIFIED"
  next: "analyze F''(0+) on the first-order equality face, beginning with the 3-state star; choose three new Section-B methods"
```

**End of complete run report.**
