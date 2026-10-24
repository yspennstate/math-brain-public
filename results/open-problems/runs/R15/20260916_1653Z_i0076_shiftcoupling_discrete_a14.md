Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no verified GPT-6/maximum model or reasoning selector; I do not claim otherwise.
Problem: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (2014), arXiv:1302.6958, Problem 7.2; intake I0076. **DOCUMENTED ROUTE SWITCH / METRIC MOVEMENT:** the frozen counterexample metric ended at `3/4` when `X_BS` was eliminated in run a13; this run changes once, transparently, to a positive-route metric `0/4 -> 2/4`. Section-B moves tried: **#18, #27, #6**.

# Status

**PARTIAL / SOURCE PROBLEM OPEN.**

The source asks whether the following three assumptions imply 2BM:

1. `X` is a forward Brownian motion (FBM);
2. `X` is a backward Brownian motion (BBM);
3. there is a random real time `T` such that the entire centered half-processes

   `F_t=X_{T+t}-X_T, t>=0`,

   `G_t=X_{T-t}-X_T, t>=0`

   are independent.

The source does **not** assume that either half-process at `T` is Brownian and does not assume `T` is a stopping time.

Definition 2.1 of Burdzy--Scheutzow says:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. such that each process `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM if `(X_{-t})_{t in R}` is FBM;
- `X` is 2BM if there is a random time `S` such that the centered future and backward half-processes at `S` are independent standard Brownian motions.

Problem 7.2 is exactly the implication above. Problem 7.5 remains excluded as already settled in the campaign.

# Repository continuity and recovered state

This run continued from current `master`, not from chat memory. Before research I read or queried:

- `probability_campaign_2026_09/INDEX.md`, `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `DEPLOYMENT.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- I0076 intake/search records under `probability_1000_intake_*/problems.jsonl`;
- the three current R15 I0076 reports;
- newest neighboring R14 and R17 reports relevant to audit/continuity.

Latest own report before this run:

`runs/R15/20260916_1556Z_i0076_any_seam_elimination_a13.md`.

Its frozen Theorem-6.1 candidate `X_BS` had three source obligations proved from the source (FBM, BBM, not-2BM), but this track proved the missing independence obligation impossible at **every real random time**. Thus that candidate is permanently retired as a counterexample and its old metric remains `3/4`, with the third obligation disproved for the candidate rather than proved.

The previous candidate-specific theorem `I0076-R15-T1` has an independent R14 audit:

`R14-AUDIT-R15-I0076-T1-03 = PASS`.

That audit does not audit any new positive-route claim below.

# Model / scheduler interface status

The scheduler interface available to this run still exposes task title, prompt, schedule, timing mode and enabled state; it exposes no model selector and no reasoning-effort selector. The installed prompt requests GPT-6/maximum, but that is prompt text rather than an authenticated runtime setting. The repository deployment record states the same.

The repository also records a separate P26/P04 modification-denial history (`You cannot modify this task`). There is no same-object workaround through the exposed interface: an owner-side/platform-side permission change or authorized replacement/handoff would be required. Creating a parallel duplicate task would violate the current instructions and was not attempted.

No scheduler change is made in this run.

# Current source / literature pass — 2026-09-16

Original source rechecked:

K. Burdzy and M. Scheutzow, *Forward Brownian Motion*, Probability Theory and Related Fields 160 (2014), 95--126, arXiv:1302.6958, DOI `10.1007/s00440-013-0524-x`.

The exact Definition 2.1 and Problem 7.2 were rechecked. The authors' current open-problems page was also checked; it lists another old FBM problem (the bounded-piece question corresponding to the old paper's later problem) but does not presently list Problem 7.2. I treat that omission as an ambiguous status signal, **not** evidence that 7.2 was solved.

Bounded dated searches on 2026-09-16 included the exact title/problem number, `1302.6958 Problem 7.2`, `independent past future random time`, the authors' later papers, shift-coupling literature, and citing literature. No paper explicitly claiming a resolution of Problem 7.2 was found in this bounded pass. This is not a proof of continued openness.

Relevant prior-art located for the route below:

- H. Thorisson, “Transformations of random variables on groups,” *Annals of Probability* 24 (1996), 2057--2064, DOI `10.1214/aop/1041903217`: equality on invariant events is equivalent to existence of a random group transformation carrying one law to the other.
- D. Aldous and H. Thorisson, shift-coupling work (1993).
- G. Last, P. Mörters and H. Thorisson, “Unbiased shifts of Brownian motion,” *Annals of Probability* 42 (2014): Brownian shift/Palm/allocation framework.
- G. Last, W. Tang and H. Thorisson (2018): Brownian path decomposition / invariant transport machinery.
- Classical “splitting time” literature (Jacobsen; Evstigneev--Ovseevich) was located through bounded searches. The abstracts reinforce the countable-vs-continuum distinction below, but I do not import an unverified theorem from inaccessible text.

# Transparent metric switch

The counterexample metric cannot move after `X_BS` was eliminated. Rather than silently rename progress, this run retires that metric and defines the positive-route metric once:

- **P1**: prove a shift-coupling compiler that turns the seam law into 2BM whenever it agrees with two-sided Wiener law on shift-invariant events; in particular, absolute continuity is sufficient.
- **P2**: prove the full **discrete source analogue**: FRW + BRW + independent halves at a finite integer random time imply 2RW, without assuming those halves are random walks at the seam.
- **P3**: remove the continuous uncountable-offset / anticipative-singularity obstruction under the exact source hypotheses.
- **P4**: deduce the full source implication and then complete prior-art/package/two-audit closure requirements.

This run proves P1 and P2. Hence the new positive-route metric is

`0/4 -> 2/4`.

This is the one transparent metric change permitted by the protocol; it is not a claim that the source problem is half solved in any canonical mathematical sense.

# New-method research before validation

## Move #18 — say it in another language: shift coupling and invariant sigma-fields

The key reformulation is to forget the particular Brownian origins and ask about the **law at the independent seam** modulo re-rooting. Two-sided Brownian motion is a stationary ergodic law under time re-rooting. Thorisson's transformation-group theorem then identifies the exact abstract target: show that the seam law and two-sided Wiener law agree on the re-rooting-invariant sigma-field.

This gives a clean positive compiler and reveals that absolute continuity of the seam law is much stronger than needed but sufficient.

## Move #27 — swap quantifiers: union over deterministic shifts before selecting the random seam

In discrete time the random offset from a certified FRW origin to the seam is integer-valued. A Wiener/RW-null event can therefore be tested after **every deterministic shift** and then unioned over a countable set. The random offset is allowed to depend arbitrarily on the whole path; no stopping-time assumption is needed.

This closes the full discrete analogue exactly. It also isolates the continuous obstruction: the corresponding random offset is real-valued, so the countable-null-union proof breaks.

## Move #6 — deform to a point we can solve

The exact deformation is the source's discrete Definition 2.5 (FRW/BRW/2RW). The full discrete analogue is solved below. I also prove a continuous restricted theorem when the witness-to-seam offsets are countably valued (or product-dominated), which shows precisely which step fails when the parameter set deforms from countable to continuum.

# R15-SC1 — shift-coupling compiler

**Status: PROVED.**

Let

`E=C_0(R)={y in C(R): y(0)=0}`

with the compact-open Borel structure and the re-rooting action

`(theta_s y)(t)=y(t+s)-y(s)`.

Let `P` be two-sided Wiener law on `E` (the law of a 2BM rooted at zero), and let `mu` be another probability law on `E`.

### Claim

If `mu(A)=P(A)` for every Borel event `A` invariant under every `theta_s`, then there exists a random real shift `Gamma` (after an auxiliary probability-space extension if needed) such that

`theta_Gamma Y ~ P` for `Y~mu`.

Consequently any process whose rooted law is `mu` is 2BM.

In particular, the sufficient condition

`mu << P`

implies the conclusion.

### Proof

The group `R` acts measurably (indeed continuously) on `E` by re-rooting. Thorisson's 1996 transformation-group theorem states for such a locally compact second-countable transformation group that two probability laws are related by a random transformation if and only if they agree on invariant Borel events. Applying that theorem to `(E,R,theta)` gives the random shift `Gamma`.

The conclusion that the original process is 2BM is distributional: after shifting by `Gamma`, its centered two-sided path has two-sided Wiener law, i.e. independent standard Brownian halves. Auxiliary randomization in an enlarged probability space is harmless for this law property.

For the absolute-continuity corollary, two-sided Wiener law is ergodic under re-rooting. (For compact cylinder events this follows from independent increments at large separations, and the standard monotone-class argument yields ergodicity.) Hence an invariant `A` has `P(A)` equal to `0` or `1`. If `P(A)=0`, `mu<<P` gives `mu(A)=0`; if `P(A)=1`, apply the same statement to `A^c` to get `mu(A)=1`. Thus `mu` and `P` agree on all invariant events and Thorisson applies. `□`

### Seam-law corollary

Suppose at the Problem-7.2 seam `T`, the future and backward half-processes are independent with laws `mu_+` and `mu_-`. If

`mu_+ << W` and `mu_- << W`,

where `W` is one-sided Wiener law, then their glued two-sided rooted law satisfies

`mu_- tensor mu_+ << W tensor W = P`.

By R15-SC1, `X` is 2BM.

So the continuous source problem would be solved if FBM/BBM forced these two one-sided absolute-continuity statements at an arbitrary independent seam. The next sections show this is automatic in discrete time but not by the same argument in continuous time.

# R15-D1 — full discrete analogue of Problem 7.2

**Status: PROVED.**

Use source Definition 2.5. Let `Z=(Z_k)_{k in Z}` be a process with increments in `{+1,-1}`. Assume:

1. `Z` is FRW: there are integer-valued random origins `S_n -> -infinity` a.s. such that `(Z_{S_n+k}-Z_{S_n})_{k>=0}` is simple symmetric random walk for every `n`;
2. `Z` is BRW, i.e. the reversed process has the analogous property;
3. there is an a.s.-finite integer random time `T` such that the entire future and backward increment processes rooted at `T` are independent.

Then `Z` is 2RW.

### Proof: future half is absolutely continuous

Let `rho_+` be one-sided fair-coin increment law on `{+1,-1}^{N_0}` and let `mu_+` be the increment law of the future half rooted at `T`.

Take a Borel event `N` with `rho_+(N)=0`. For each FRW origin `S_n`, put

`B^(n)_j = Z_{S_n+j+1}-Z_{S_n+j}, j>=0`.

As a process, `B^(n)` has law `rho_+`.

On `{S_n<T}`, the integer offset

`K_n=T-S_n`

belongs to `{1,2,...}`, and the future increment sequence at `T` is exactly the deterministic tail shift `sigma^{K_n} B^(n)`. Therefore

`P(F in N, S_n<T)`

is at most

`sum_{k>=1} P(sigma^k B^(n) in N, K_n=k)`

which is at most

`sum_{k>=1} P(sigma^k B^(n) in N)=0`,

because for every deterministic `k`, the shifted fair-coin sequence still has law `rho_+` and `N` is `rho_+`-null.

Since `S_n -> -infinity` and `T` is finite,

`union_n {S_n<T}`

has probability one. Hence `P(F in N)=0`. Thus

`mu_+ << rho_+`.

No stopping-time property or independence involving `T`, `S_n`, or `B^(n)` was used.

### Proof: backward half is absolutely continuous

Apply the same argument to the BRW witness origins on the right. Equivalently, there are random integers `R_n -> +infinity` such that

`H^(n)_j = Z_{R_n-j-1}-Z_{R_n-j}, j>=0`

(with the harmless symmetric sign/orientation convention) has fair-coin law. On `{R_n>T}`, the backward half at `T` is a deterministic integer tail shift of `H^(n)` by `R_n-T`. Countability gives

`mu_- << rho_+`.

### Glue and shift-couple

By the assumed seam independence, the two-sided increment law rooted at `T` is

`mu=mu_- tensor mu_+`.

Hence

`mu << rho_- tensor rho_+ = rho`,

where `rho` is the iid fair-coin law on `{+1,-1}^Z`, i.e. the rooted 2RW increment law.

The Bernoulli shift `rho` is ergodic. Therefore `mu` and `rho` agree on all integer-shift-invariant events. Applying Thorisson's transformation-group theorem to the `Z`-action gives a random integer shift `Gamma` such that the rooted increments at `T+Gamma` have law `rho`.

At `S=T+Gamma`, the future and backward increment sequences are independent simple symmetric random walks. Thus `Z` is 2RW. `□`

This exactly matches the source's complete discrete analogue and does not strengthen `T` to a stopping time.

# R15-C2 — continuous countable-offset / product-domination theorem

**Status: PROVED RESTRICTED CASE / PARTIAL for Problem 7.2.**

Let `X` satisfy the full Problem-7.2 FBM/BBM assumptions and let `T` be an independent-halves seam.

Assume in addition that for the FBM witness origins `S_n`, on `{S_n<T}`, the offsets

`A_n=T-S_n`

belong to deterministic countable sets `D_n`. Assume analogously that the BBM witness-to-seam offsets on the right are countably valued.

Then `X` is 2BM.

### Proof

Let `N` be a Wiener-null event in one-sided path space. For the FBM origin `S_n`, set

`B^(n)_t=X_{S_n+t}-X_{S_n}, t>=0`.

Then `B^(n)` has one-sided Wiener law. On `{S_n<T,A_n=a}`, the seam future path is exactly

`theta_a^+ B^(n)`.

Hence

`P(F in N,S_n<T)`

is at most

`sum_{a in D_n} P(theta_a^+ B^(n) in N)=0`,

because every deterministic future shift of standard Brownian motion is again standard Brownian motion. Union over `n`, using `S_n -> -infinity`, gives `mu_+ << W`.

The BBM side is identical after time reversal, giving `mu_- << W`. Seam independence then gives a rooted law absolutely continuous with respect to two-sided Wiener law, and R15-SC1 implies 2BM. `□`

The same proof works if the joint law of `(B^(n),A_n)` is dominated by `W tensor nu_n` for some sigma-finite offset measure `nu_n`; Fubini replaces the countable sum.

# Why the continuous full problem remains open after D1/C2

The discrete proof uses exactly one feature that fails in continuous time:

`K=T-S_n` is integer-valued.

For a real-valued anticipative random offset `A=T-S_n`, the implication

`W(N)=0  =>  P(theta_A B in N)=0`

is false without extra structure. An uncountable union of deterministic-shift null events need not be null, and a path-selected random time can put the re-rooted path on a Wiener-singular law. Nothing in the FBM definition makes `T-S_n` a stopping time or independent of the Brownian future from `S_n`.

This is the precise P3 blocker.

The splitting-time literature found in the status search is consistent with this diagnosis: countable-valued splitting times are much easier to characterize than arbitrary uncountable-valued times. I do not treat those abstracts as a proof of the present implication.

# Counterexample-first branch before committing to the positive route

Before switching metrics, I tried to replace the eliminated `X_BS` candidate with a genuinely decomposable pasting candidate whose seam independence is automatic.

The most promising family uses iid Brownian pieces cut at infinite-mean path-defined times, motivated by source Remark 7.6: identifiable infinite-mean renewal boundaries cannot be stationarized in the usual finite-intensity way, while independent lengths give an obvious 2BM.

Two concrete ideas were rejected:

1. **Inverse-local-time blocks.** Stopping Brownian motion when local time reaches a fixed amount gives infinite-mean lengths and attractive time-reversal symmetry, but concatenating iid such pieces appears to reconstruct ordinary Brownian motion; moreover the integer local-time phase is not evidently identifiable from the unrooted path. It did not produce a verified not-2BM witness.
2. **Marked-excursion boundaries.** Ending a block at the next marked large excursion makes a path-identifiable renewal boundary, but time reversal moves the marked excursion to the beginning of the reversed block. The reversed iid piece law is therefore not the same Brownian stopped-piece law, so BBM verification fails.

These failures are why the run makes the documented positive-route switch rather than freezing an unverified new candidate.

# What P1+P2 teach about the full source problem

The source's implication can now be written as one missing invariant statement:

> Let `mu=mu_- tensor mu_+` be the rooted law at the independent seam. Prove that `mu` and two-sided Wiener law agree on every re-rooting-invariant Borel event.

Absolute continuity is one sufficient route, but D1 shows that its easy proof was a **countability artifact**. The correct continuous proof may have to work directly on the invariant sigma-field rather than prove `mu_± << W`.

This reframes the old “common splice” obstruction: FBM supplies many Brownian future origins and BBM supplies many Brownian backward origins, but they need not align. Seam independence might be exactly what allows their orbit information to glue; no proof of that step is yet known here.

# Next attack

The next run should not manufacture another finite checker. The highest-value route is the **Palm / invariant-event route**:

1. model the seam-rooted product law `mu_- tensor mu_+` as a point on the re-rooting orbit space;
2. use FBM and BBM origins to prove equality with two-sided Wiener law for a generating class of shift-invariant events, or construct a mass-transport/allocation that balances the two orbit laws;
3. compare directly with Thorisson shift coupling and Last--Mörters--Thorisson unbiased Brownian shifts;
4. adversarially test whether independence can coexist with a nontrivial invariant event of probability strictly between the values under 2BM.

A second counterexample branch remains possible through path-identifiable infinite-mean decomposable Brownian pieces, but only after an explicit reversible stopped-piece law is found. The two rejected constructions above should not be repeated unchanged.

Suggested section-B moves for the next run, not yet executed: **#11 (dualize to invariant/Palm measures), #21 (ask who else has this splitting shape), #29 (compactify/orbit boundary).**

# R17 directed-audit state

Newest R17 report read:

`runs/R17/20260916_1611Z_stuck1_transferstate_b84f.md`.

It is explicitly `OPEN / STUCK RECOVERY 1`, makes no new theorem claim, and contains no closure package requiring an R15 independent audit. No audit verdict is invented.

# Old R15 Cugliandolo--Kurchan handoff

The old R15 spherical-p-spin assignment remains retired. Historical reports are preserved. Handoff status remains:

**OPEN; no verified full-aging closure was recorded at retirement.**

Nothing in that retired track was edited or revived.

# Validation / artifacts

No new finite claim was made in this run, so under the 90/10 policy I deliberately did **not** create a decorative checker. R15-SC1, R15-D1 and R15-C2 are theorem-sized claims and their complete arguments are written above.

The prior candidate-elimination exact artifacts remain in `artifacts/R15/`; they are not rerun merely to show activity.

# Ledger delta for P26

```yaml
ledger_delta:
  track: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; I0076"
  target: "Decide whether FBM + BBM + independent centered halves at some random T imply 2BM"
  metric_change:
    retired_counterexample_metric:
      definition: "source-witness obligations for frozen Theorem-6.1 candidate X_BS"
      final_value: "3/4"
      reason: "candidate's required independence obligation was disproved at every real random seam in run a13"
      final_unchanged_count: 2
    new_positive_metric:
      definition: "four proof gates P1 shift-coupling compiler; P2 full discrete analogue; P3 continuous arbitrary-offset invariant step; P4 source conclusion plus closure package/audits"
      before: "0/4"
      after: "2/4"
  status: PARTIAL
  unchanged_count: 0
  tried_moves: [18, 27, 6]
  proved_this_run:
    - "R15-SC1: invariant-sigma / absolute-continuity shift-coupling compiler"
    - "R15-D1: full FRW+BRW+independent integer-seam implies 2RW theorem"
    - "R15-C2: countable-offset/product-dominated continuous restricted theorem"
  remaining_obligation: "P3: under the exact continuous source hypotheses, prove seam rooted law agrees with two-sided Wiener law on re-rooting-invariant events; then P4"
  current_route_obstruction: "real anticipative offset T-S_n is uncountable and can destroy Wiener null sets under path-selected re-rooting"
  exact_evidence:
    - "this immutable report; theorem proofs are on-page"
    - "prior R15 candidate-elimination artifacts retained but not rerun"
  audit_ids_for_new_claims: []
  prior_candidate_audit_ids:
    - "R14-AUDIT-R15-I0076-T1-03 = PASS"
  requested_shared_ledger_action: "P26 may replace stale R15 UNMEASURED row with the transparent route-switch metric; do not label source closed"
```

# Delivery / restrictions

GitHub only. No Gmail, email, Drive, public posting, purchases, permission changes, workflow execution, shared-root edits, peer-file edits or scheduler changes were performed.
