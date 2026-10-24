Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector/receipt, so I do not claim otherwise. **NO MOVEMENT: active R19/F0057 `M_TV: 1 -> 1`; unchanged count `4 -> 5`; STUCK RECOVERY 1 action executed; methods #15 BREAK THE SYMMETRY, #26 HUNT THE SPORADIC CASE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R19 — F0057 weak fixed-law adversarial recovery

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

This invocation executes the single recovery action selected by the preceding mandatory stuck report: **REFUTE INSTEAD OF PROVE**. I did not strengthen the already-saturated binary metric and did not manufacture an audit. The target of the adversarial check was the weakest source interface: `j=2`, `lambda<nu`, `m/n=lambda+o(1/log n)`, nontrivial lattice span, ties, and an `n`-dependent TV-positive set.

---

## 1. Continuity / whole-repository state

I read the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md` / `RESULTS.md` / `QUEUE.md` surfaces as available through the repository connector, the latest operations implementation record, the owner directive, the create-only F0057 claim, the newest R19 report, the source-proof artifact and the relevant older F0057 campaign history. I also searched current repository state for the required F0057 audit labels.

The controlling create-only owner remains **R19** at `operations/claims/F0057.md`. Its metric is binary:

`M_TV = 1` iff the full source fixed-`j` total-variation statement is proved under the exact Theorem 18.7/19.7 scope, including the tuned-law formulation where invoked.

The original Hasebe--Ueda I0084 assignment remains frozen at its rotation handoff and was **not reopened**. Preserve exactly its source convention: Conjecture 5.5 of arXiv:1710.08240v2 uses ordinary **classical convolution**

\[
\mu*S_t,
\]

including when `S_t` is the law of a free stable distribution. Its exact `(2+alpha)`-moment scope, original skewness conventions, and retained `alpha=1/2` internal count `2/2` are preserved; stronger-moment / compact-support statements remain restricted/PARTIAL. I0110 and I0120 likewise remain rotated at their handoffs.

The active source is F0057: Svante Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, arXiv:1112.0510 / Probability Surveys 9 (2012), Problem 18.10 in the arXiv numbering (Problem 19.10 in the published numbering).

---

## 2. Fresh source and literature check

The primary source was reread on 2026-09-18 local date. Problem 18.10 asks exactly whether

\[
d_{\rm TV}(Y_{(j)},\xi_{(j)})\to0
\]

for every fixed `j` under Theorem 18.7's assumptions. Theorem 18.7 states the main fixed-law branch under `m=lambda n+o(sqrt n)` and finite variance (the variance assumption is redundant for `lambda<nu`), proves Kolmogorov convergence for every fixed rank, and proves TV for `j=1`. The source then treats arbitrary `m/n->lambda<nu` with the tuned law `xi^(n)`, obtains a logarithmic cutoff `B(n)=O(log n)` and a uniform local ratio below it, and finally returns to fixed `xi` when

\[
m/n=\lambda+o(1/\log n)
\]

via its displayed estimate (18.46)

\[
P(\xi^{(n)}=k)=(1+o(1))P(\xi=k)
\]

uniformly for `k<=B(n)`, together with `o(n^{-1})` tails for both laws. The source's Remark 13.2 explicitly allows `o(sqrt n)` recentering in the lattice local CLT and relaxes the triangular-array third-moment condition to uniform square integrability.

Fresh web searches used exact/near-exact combinations of `Problem 18.10`, `Problem 19.10`, Janson, `d_TV(Y_(j),xi_(j))`, conditioned random allocations, total variation and order statistics. They recovered the source and neighboring/general order-statistic-TV literature but no later primary theorem explicitly resolving this exact conditioned-allocation problem. This remains **bounded negative evidence only**, not a novelty certificate.

Repository search again found no completed current `P26-AUDIT-R19-F0057` and no distinct second-track end-to-end PASS audit. Search-index lag is possible, so this is only the evidence recovered by this invocation; I do not manufacture an audit from absence.

---

## 3. Adversarial hypothesis

The preceding stuck report isolated a plausible proof failure:

> Janson's weak fixed-law comparison (18.46) is pointwise-uniform below a logarithmic cutoff. Could an `n`-dependent TV-positive set, a rank-two count event, ties, or nontrivial lattice span amplify the tuned/fixed discrepancy enough that the current R19 higher-rank proof does not transfer?

This run attacked that statement instead of proving another strengthening.

---

## 4. Result: the suspected interface survives

I wrote a complete self-check at

`artifacts/R19/2026-09-17_22-36-42_UTC__f0057_weak_fixed_transfer_stress_e4a7.md`.

The key lemma is the following. Let `p_n` be the tuned law and `p` the fixed law. For every fixed `q`, uniformly over every supported tuple `k_1,...,k_q<=B_n=O(log n)`,

\[
\boxed{
P(Y_1=k_1,\ldots,Y_q=k_q)
=(1+o(1))\prod_{i=1}^q p(k_i).
}
\tag{4.1}
\]

Indeed, conditioning the tuned iid variables on their sum gives the exact factorization

\[
P(Y_1=k_1,\ldots,Y_q=k_q)
=\left(\prod_i p_n(k_i)\right)
\frac{P(S^{(n)}_{n-q}=m-\sum_i k_i)}{P(S^{(n)}_n=m)}.
\]

Because `E xi^(n)=m/n`, the residual target differs from its residual mean by

\[
q\,m/n-\sum_i k_i=O(\log n)=o(\sqrt n),
\]

uniformly. Remark 13.2 therefore makes the residual local-CLT ratio `1+o(1)` uniformly; (18.46) turns the fixed finite product of tuned masses into the corresponding fixed-law product with uniform relative error.

This uniform coordinate ratio immediately passes through **arbitrary moving nonnegative sums**. Hence for any fixed finite family of moving sets `E_{a,n}\subseteq[0,B_n]`, all fixed joint factorial moments of their conditioned occupancy counts equal the fixed-iid factorial moments up to `1+o(1)`. Whenever their intensities converge, both count vectors converge to the same independent Poisson vector. This includes moving pieces cut out by the actual TV-positive set.

The global cutoff also transfers: the source itself records `P(Y_(1)>=B_n)->0` and both `P(xi^(n)>=B_n)=o(1/n)` and `P(xi>=B_n)=o(1/n)`. Thus all moving-set truncations are charged to one global maximum-bad event on each side. The old `P30H-F001` bookkeeping issue does not reappear in this source branch.

---

## 5. The three methods and what happened

### #15 BREAK THE SYMMETRY ON PURPOSE

I forced nontrivial lattice span rather than hiding behind an aperiodic law. Exponential tilting preserves support. If the common span is `d`, every exposed supported value is a multiple of `d`, so the residual target stays in the admissible lattice class. The same local-CLT factor `d` occurs in numerator and denominator and cancels. An explicit span-two stress family is

\[
P(\xi=2r)=(1-a)a^r,
\]

for which the tuned law is again even-geometric. Under the weak `o(1/log n)` drift, the tuned/fixed mass ratio is uniformly `1+o(1)` at all `r=O(log n)`. **No parity failure.**

### #26 HUNT THE SPORADIC CASE

I targeted the first higher rank `j=2`, ties/repeated observations, and an `n`-dependent TV-positive set. The R19 rank event is expressed by exact integer occupancy-count inequalities, not by a no-ties ordering argument. The moving-set factorial-moment lemma therefore includes ties automatically. **No sporadic rank-two failure found.**

### #30 ONE SCALE / ONE DIRECTION AT A TIME

There are only two relevant scales. Below `B_n=O(log n)`, `tau_n-1=o(1/log n)` makes the exponential tilt uniformly invisible and the residual-sum displacement is `o(sqrt n)`. Above `B_n`, both iid reference maxima and the conditioned maximum are negligible. **The scales glue without a gap.**

---

## 6. What this does and does not establish

The chosen adversarial recovery did **not** find a source-valid counterexample or proof gap. It strengthens the auditability of the existing source-matching proof by spelling out the weak fixed-law transfer for arbitrary moving tail sets, nontrivial span and ties.

It does **not** count as an independent audit, and it does not create a second source case. Therefore

`M_TV: 1 -> 1`.

The source target remains

**PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED**.

The recovered independent-audit count remains `0/2` for the exact current R19/F0057 package.

---

## 7. Why there is no checker this run

No finite claim was introduced. The new material is an analytic transfer lemma derived from exact conditioning identities, the source's uniform estimate (18.46), and the source lattice local CLT. The even-geometric stress family is handled by closed-form algebra. A finite checker would be decorative rather than evidentiary, so none was created.

---

## 8. Next-run rule

The frozen source metric has now been unchanged for five consecutive F0057 runs after its initial `0 -> 1` movement. One further unchanged run reaches the operational six-run CLOSABLE rotation threshold.

Because the mathematical stress test succeeded and the remaining obligation is external certification rather than another asymptotic lemma, the next run must not return to the same three methods or invent another stronger theorem. Freeze the next Section-B triple as:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — extract the shortest source-only fixed-`j` proof package, deleting every growing-`r` strengthening from the dependency chain;
- **#24 FIND THE EXTREMAL OBJECT** — adversarially identify the worst block/intensity configuration in the rank-`j` count sandwich, so an auditor can check one explicit inequality rather than prose;
- **#27 SWAP THE QUANTIFIERS** — test whether the moving-set uniformity can be formulated as one uniform lemma before choosing the TV-positive set, eliminating any hidden set-selection dependence.

If that run does not move the frozen metric, rotate F0057 under the six-unchanged CLOSABLE rule and leave a durable handoff; do not keep polishing it indefinitely.

---

## 9. Model / scheduler control

The limitation remains current on the available task surface: it exposes prompt/title/schedule/timing/enabled-state controls but no model-family selector, no reasoning-effort selector, no guaranteed-duration control and no authenticated per-run model receipt. Thus GPT-6 / maximum can be requested in prompt text but cannot be forced or attested here. Enforcing it requires an authorized product/backend scheduler surface exposing model/reasoning fields plus runtime attestation.

The historical P26 `You cannot modify this task` response is an authorization-context boundary, not a mathematical blocker. Repository history records that an authorized/owning context could later act on P26. The lawful workaround is the owning/authorized context or platform support; no duplication, permission bypass or scheduler change was attempted here.

---

## 10. `ledger_delta`

```yaml
ledger_delta:
  worker: R19
  active_source: F0057
  source_citation: "Svante Janson, arXiv:1112.0510 / Probability Surveys 9 (2012), Problem 18.10/19.10"
  preserved_rotated_source: I0084
  preserved_i0084_convolution: "ordinary classical convolution mu*S_t, including free-stable-law S_t"
  metric_name: M_TV
  metric_before: 1
  metric_after: 1
  movement: "NO MOVEMENT"
  status: "PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED"
  unchanged_count_before: 4
  unchanged_count_after: 5
  recovery: "STUCK RECOVERY 1 — REFUTE INSTEAD OF PROVE"
  tried_moves: [15, 26, 30]
  outcome: "weak fixed-law j=2/span/ties/moving-set stress test found no source-valid failure; uniform q-coordinate and moving-set transfer written explicitly"
  remaining_obligation: "two independent OTHER-track end-to-end PASS audits of the exact R19/F0057 source package; novelty search remains bounded, not certified"
  audit_ids: []
  evidence:
    - "artifacts/R19/2026-09-17_22-36-42_UTC__f0057_weak_fixed_transfer_stress_e4a7.md"
    - "source equations/steps: Janson Remark 13.2, (18.43)-(18.46), Problem 18.10"
  next_moves: [4, 24, 27]
  rotation_if_next_unchanged: true
```

---

## 11. Delivery receipt

The proof/stress artifact was created on `master` at commit

`3eefc78b4544c941a26ede7d5ac73d892ad6f7d4`

and read back from that exact commit. No shared root, claim file, other track file, email, Drive item, public post, permission or scheduler was modified.
