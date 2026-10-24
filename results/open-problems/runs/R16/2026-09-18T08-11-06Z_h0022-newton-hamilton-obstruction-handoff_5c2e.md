Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO SOURCE-METRIC MOVEMENT + MANDATORY HARD HANDOFF:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; supported substantive unchanged count `4 -> 5`; methods actually used: **#1 CHANGE THE CATEGORY, #11 DUALIZE, #28 REPLACE FOR ALL WITH TYPICAL**.

# R16 HARD OUTSIDE — H0022 exact Newton overlap expansion, Hamilton-cycle obstruction, and mandatory handoff

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.
Deployment: `NEW-METHODS-2026-09-16`.

Active source entering this run: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, Conjecture 1.5.

Status after this run: **SOURCE OPEN / R16 PARTIAL METHOD PROGRESS / RELEASED BY R16 / ROTATION_WAIT**. Both permitted H0022 stuck recoveries were already consumed before this substantive test. The frozen source metric did not move, so the HARD protocol forbids any `STUCK_RECOVERY_3` and requires handoff now.

## 1. Continuity, required repository read, and why Beck--Fiala is not restarted

I continued from

`runs/R16/2026-09-18T06-43-45Z_h0022-stuck-recovery-2-degree-sequence-profile_83c1.md`

rather than restarting the stale native Beck--Fiala title or any earlier R16 target.

At run start I recovered/read the required current repository surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, current H0022 claim/intake evidence, the newest own R16 report, recent commits, and current neighboring successor-gate evidence. The H0022 canonical claim still records R16 as the active HARD owner at entry; its frozen quantity is the complete coefficient curve `A_cyc(c)`.

The root ledger still has the historical R16/Beck--Fiala title, but it explicitly says newer complete own-track reports control and must be recovered before replacing the stale row. That continuity now runs through H0021 and H0022. The old Beck--Fiala target is additionally obsolete as an active research problem at the current preprint level: Bansal--Jiang only gave the square-root order for `t >= log^2 n`, but Guo--Fang--Lu (arXiv:2609.11189v1, 10 September 2026) now state the stronger Komlos theorem with constant `3 sqrt(2 pi)`, implying

`disc(A) < 3 sqrt(2 pi t)`

for every integer `t>=1` with no `n` restriction. Karingula--Lovett, ECCC TR26-188 (17 September 2026), give a separately authored elementary Komlos proof with constant `36`. These are extremely recent preprint/technical-report results, not mature refereed consensus, but they make the native Beck--Fiala source inappropriate to restart.

A fresh bounded source check also still finds arXiv:2608.06358v1 as the current H0022 primary paper; its abstract proves only a sufficiently-large-constant analogue, including cycle-factor universality at `C log n/n` above girth `100 log n/loglog n`, not Conjecture 1.5 at coefficient `1+epsilon`. No later source-matching proof was located in the bounded search. This is dated evidence, not a worldwide novelty certificate.

## 2. Frozen H0022 metric

For fixed `c>1`, `A_cyc(c)` is the smallest coefficient `A` for which R16 has a complete proof that

`G(n,c log n/n)`

is whp universal for every `n`-vertex cycle factor whose cycles all have length at least

`A log n/loglog n`,

with all restrictions retained.

At the sharp source density the target is

`A_cyc(1+epsilon) <= 1+epsilon`

for every fixed `epsilon>0`.

Before this run: `UNMEASURED`.
After this run: `UNMEASURED`.

The run nevertheless obtains a concrete theorem about why the raw fixed-edge-count second-moment architecture cannot close even the one-cycle special case.

## 3. #1 CHANGE THE CATEGORY — replace overlap tails by an exact positive subset gas

The previous H0022 route worked in `G(n,M)` and organized the second moment by the common-edge count

`K = |E(F_0) cap E(F)|`.

This run changes the category from a tail problem for `K` to an **exact positive Newton expansion over common edge subsets**.

Let

`N = binom(n,2)`,
`Q_s = (M)_s/(N)_s`,
`W(k) = Q_{2n-k}/Q_n^2`.

For any fixed `n`-edge spanning target `H`, if `F_0,F` are independent uniform labelled copies of `H`, then

`E X_H^2/(E X_H)^2 = E W(K)`.

The kernel obeys the exact ratio

`W(k+1)/W(k) = (N-2n+k+1)/(M-2n+k+1)`.

Put

`A=N-2n+1`, `B=M-2n+1`.

Then

`W(k)=W(0) (A)^(overline k)/(B)^(overline k)`.

## 4. #11 DUALIZE — exact Newton coefficients and positivity

For integer `K`, Newton's forward-difference formula gives

`W(K) = sum_{j=0}^K binom(K,j) Delta^j W(0)`.

The hypergeometric finite-difference identity

`sum_{i=0}^j (-1)^(j-i) binom(j,i) (A)^(overline i)/(B)^(overline i)
 = (A-B)_(underline j)/(B)^(overline j)`

therefore yields the exact coefficient formula

**(4.1)**

`Delta^j W(0)
 = W(0) (N-M)_(underline j)/(M-2n+1)^(overline j)`.

For `M=Theta(n log n)` and every `0<=j<=n`, these coefficients are positive for all sufficiently large `n`.

Taking expectations gives an exact positive subset expansion:

**(4.2)**

`E W(K)
 = W(0) sum_{j=0}^n c_j E binom(K,j)`,

where

`c_j=(N-M)_(underline j)/(M-2n+1)^(overline j)`

and

**(4.3)**

`E binom(K,j)
 = sum_{S subset E(F_0), |S|=j} P(S subset E(F))`.

This is the useful dual form: instead of upper-bounding the dependent random variable `K`, one can select one positive family of common subsets `S` and obtain a rigorous lower bound on the full second moment. No cancellation can hide that family.

### Proof of (4.1)

From the kernel ratio,

`W(i)/W(0)=(A)^(overline i)/(B)^(overline i)`.

Hence

`Delta^j W(0)/W(0)
 = sum_{i=0}^j (-1)^(j-i) binom(j,i) (A)^(overline i)/(B)^(overline i)`.

The displayed finite hypergeometric identity follows by Chu--Vandermonde (and can also be proved by induction on `j` from the ratio of consecutive rising factorials). Since `A-B=N-M`, (4.1) follows. Equation (4.2) is Newton's formula, and (4.3) is the identity

`binom(K,j)=sum_{S subset E(F_0), |S|=j} 1_{S subset E(F)}`.

## 5. #28 REPLACE FOR ALL WITH TYPICAL — solve the exact Hamilton-cycle run statistic first

The easiest cycle-factor type is a single Hamilton cycle `H=C_n`. It is source-admissible for every H0022 girth threshold, so it is a legitimate stress test even though Hamiltonicity itself is known far below the source density.

Fix one Hamilton cycle `F_0`. Let `S subset E(F_0)` have `j<n` edges and exactly `r` cyclic runs (path components). Contract the `j` selected edges. The result has `n-j` objects. Each of the `r` path components can be oriented in two ways, so the number of undirected Hamilton cycles containing `S` is exactly

`2^r (n-j-1)!/2`.

Since the complete graph has `(n-1)!/2` undirected Hamilton cycles,

**(5.1)**

`P(S subset E(F)) = 2^r/(n-1)_j`.

The number of `j`-edge subsets of a fixed `n`-cycle with exactly `r` runs is the circular-composition count

**(5.2)**

`R_n(j,r)
 = (n/r) binom(j-1,r-1) binom(n-j-1,r-1)`,

for `1<=r<=min(j,n-j)`.

Combining (4.2), (5.1), and (5.2), every individual `(j,r)` class supplies the rigorous positive lower bound

**(5.3)**

`E X^2/(E X)^2
 >= W(0) c_j R_n(j,r) 2^r/(n-1)_j`.

This removes the principal ambiguity in the preceding recovery: run multiplicity and fixed-`M` weight now sit in one exact expression.

## 6. The natural run profile makes the raw fixed-M second moment exponentially large

Fix `c>1`, write `L=log n`, and take

`M = floor((c L/n) N)`.

Choose

`j = floor(2n/(cL))`,
`a = floor(2n/(c^2 L^2))`,
`r = j-a`.

Here `a=j-r` is exactly the number of internal vertices of the common runs when no whole common cycle occurs; it is the earlier `A_2=K-R` statistic.

More generally put

`j = b n/L + o(n/L)`,
`a = alpha n/L^2 + o(n/L^2)`,
`r=j-a`.

Stirling's formula and Taylor expansion of the falling/rising factorials in (5.3) give, uniformly for fixed positive `b,alpha,c`,

**(6.1)**

`(1/n) log[ W(0)c_j R_n(j,r)2^r/(n-1)_j ]
 = Phi_c(b)/L + Psi_{c,b}(alpha)/L^2 + o(L^-2)`,

where

`Phi_c(b)=b(1+log(2/(bc)))-2/c`,

and

`Psi_{c,b}(alpha)
 = alpha(1+log(b^2/(2alpha))) - (b-2/c)^2`.

For completeness, the pieces at the required accuracy are

`log W(0)/n = -2/(cL)-4/(c^2L^2)+o(L^-2)`,

`[log c_j-log(n-1)_j]/n
 = -b(log L+log c)/L + (4b/c+b^2/2)/L^2+o(L^-2)`,

and

`[log R_n(j,r)+r log2]/n
 = b(1+log(2L/b))/L
   + [alpha(1+log(b^2/(2alpha)))-3b^2/2]/L^2
   +o(L^-2)`.

At the leading saddle

`b_* = 2/c`

we have `Phi_c(b_*)=0`. The second-order expression is maximized at

`alpha_* = b_*^2/2 = 2/c^2`,

and there

`Psi_{c,b_*}(alpha_*) = 2/c^2 > 0`.

Therefore (5.3) proves the concrete asymptotic obstruction

**THEOREM (raw fixed-M Hamilton second-moment blow-up).**
For every fixed `c>1`, if `X` denotes the number of Hamilton cycles in

`G(n,M)`, `M=floor((c log n/n) binom(n,2))`,

then

**(6.2)**

`E X^2/(E X)^2
 >= exp[(2/c^2+o(1)) n/(log n)^2]`.

A single positive overlap family already forces this divergence. Its geometry is

`K=j=(2/c+o(1)) n/log n`,

`A_2=j-r=(2/c^2+o(1)) n/(log n)^2`.

This is exactly the run-profile scale isolated in the previous H0022 reports.

### Interpretation

This theorem is **not** a counterexample to H0022 and not a statement that Hamiltonicity fails. At `c>1`, Hamiltonicity is a much easier property than the full cycle-factor universality target. What (6.2) certifies is narrower and useful: conditioning only on the total host edge count cannot make the raw Hamilton-cycle count amenable to an ordinary bounded-relative-variance second moment. The surviving obstruction is already exponentially large on the `n/log^2 n` exponent scale.

It also corrects the easy interpretation of the previous recovery. Degree-sequence conditioning remains a live possibility: the regular-graph literature handles Hamilton-cycle counts by small-subgraph conditioning, and fixing degrees can remove large fluctuations that fixed-`M` conditioning leaves behind. The previous local factor `(d-3)/(d-2)` diagnosed the relevant run statistic but did not by itself prove that the full degree-conditioned saddle fails.

## 7. Exact finite self-check

Only after deriving the exact identities above, I built one exact-arithmetic self-check. It verifies:

1. the Newton coefficient identity (4.1) for multiple integer parameter sets;
2. the circular run-count formula (5.2) for every `4<=n<=10`;
3. by exhaustive enumeration of undirected Hamilton cycles, the containment count `2^r(n-j-1)!/2` for every realized `(j,r)` with `4<=n<=8`.

The executed output ends `ALL_EXACT_CHECKS_PASS`.

Artifacts:

- `artifacts/R16/2026-09-18T08-11-06Z_h0022_newton_hamilton_checker.py`
- `artifacts/R16/2026-09-18T08-11-06Z_h0022_newton_hamilton_checker.out`

This is a self-check of finite identities. The asymptotic theorem is proved on the page above; the checker is not substituted for that proof.

## 8. Prior-art positioning

I make no broad novelty claim for Hamilton-cycle second-moment clustering, conditioning, or run enumeration. Classical work of Robinson--Wormald uses small-subgraph conditioning for Hamilton cycles in random regular graphs, and related Hamilton-cycle count/contiguity literature shows that degree/short-cycle conditioning can materially regularize spanning-count fluctuations. The contribution of this run to the H0022 route is the exact positive Newton/subset representation together with the explicit source-scale run family (6.2) that certifies why the current fixed-`M` architecture cannot close.

The nearest next technical category, if another worker revisits H0022, is therefore not another `K`-tail estimate. It is one of:

- a degree-sequence/small-subgraph conditioned count with error `o(n/log^2 n)` at the Hamilton saddle and ultimately finer accuracy for equal-short factors;
- a truncation/size-bias that removes the positive `(j,r)` family before the second moment;
- or an absorber/linking construction that avoids raw spanning-count second moments entirely.

## 9. Mandatory H0022 handoff

H0022 has now consumed both allowed stuck recoveries and this subsequent substantive test leaves the source metric unchanged. There is no legal third recovery. I therefore release H0022 from active R16 research with status

`SOURCE OPEN / PARTIAL / HANDOFF_REQUIRED`.

The handoff state that must be preserved is:

- exact first-moment extremal cycle type and type-entropy reduction;
- fixed-`M` localization of surviving overlaps;
- exact `(K,R,Z)` overlap transfer matrix;
- matching-only third-order deficit `-16/(3c^3) n/log^3 n`;
- degree-demand/run-profile diagnosis;
- and now the exact positive Newton expansion plus Hamilton run-family blow-up (6.2).

The simplest still-open proof test is the equal-short factor `C_k^{n/k}`, `k~A log n/loglog n`, after enough host conditioning/truncation to remove the Hamilton-type positive run family.

## 10. Successor admission screen and ROTATION_WAIT

The HARD protocol says to rotate to an **eligible** outside target, not to invent one from a stale PENDING queue row. Current repository evidence shows the hard-reserve admission gate is itself congested. I checked the current queue/claim state of several plausible rows while preserving the no-restart rule:

- `I0078`: claimed by C27;
- `I0060`: prior R12 target with completed handoff; do not restart;
- `I0073`: claimed by another HARD slot;
- `I0068` and `I0066`: claimed;
- `I0028`: already claimed by another HARD slot;
- `I0079`: already claimed by R06;
- `I0049`: current task-health evidence classifies the queued scope as KNOWN/resolved;
- `I0047`: current admission evidence says later-work residual scope is not frozen cleanly enough for dispatch.

A current neighboring admission report at `runs/R12/2026-09-18T07-30-15Z_rotation_admission_wait_16_b4e2c9.md` independently reaches the same operational conclusion for the obvious remaining HARD rows: absence of a same-ID claim file is not enough; many attractive rows are owned, source-ambiguous, or PENDING rather than READY.

I therefore do **not** fabricate a successor claim in this run. R16 enters

`ROTATION_WAIT / NO_SUCCESSOR_CLAIMED`.

The next invocation must continue from previously unscreened or materially changed HARD OUTSIDE intake candidates and perform exact source/current-literature/prior-attempt/source-level-ownership checks before any create-only claim. It must not return to H0022, H0021, I0043, or any earlier exhausted R16 target absent an explicit fresh reassignment.

## 11. Scheduler/model-control boundary

Still true: the exposed task-control interface has prompt/title, schedule/start, timing mode, enabled state, and task identity, but no binding model-family selector, no reasoning-effort selector, and no authenticated per-run applied-model/effort receipt. GPT-6/maximum is therefore prompt-only here. Enforcing it requires product/runtime support exposing those controls plus execution attestation.

The historical P26 `You cannot modify this task` outcome was authorization-context-specific; repository evidence records a later successful P26 update from an authorized context. For any task that still returns that error, the compliant workaround is the owning workspace/account context or platform support, not duplication or permission bypass.

No scheduler state, shared root ledger, peer research file, email, Drive content, public post, purchase, permission, or workflow was changed.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  lane: HARD_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  source_id_entering_run: H0022
  source_status: OPEN
  source_locator: arXiv:2608.06358v1, Conjecture 1.5
  metric:
    name: A_cyc(1+epsilon)
    before: UNMEASURED
    after: UNMEASURED
  metric_movement: false
  supported_substantive_unchanged_count:
    before: 4
    after: 5
  methods_attempted: [1, 11, 28]
  new_results:
    exact_newton_subset_expansion: true
    hamilton_run_containment_formula: true
    fixed_M_hamilton_second_moment_lower_bound: "exp((2/c^2+o(1))*n/(log n)^2)"
  finite_self_check:
    path: artifacts/R16/2026-09-18T08-11-06Z_h0022_newton_hamilton_checker.py
    output: artifacts/R16/2026-09-18T08-11-06Z_h0022_newton_hamilton_checker.out
    result: ALL_EXACT_CHECKS_PASS
  h0022_stuck_recoveries_used: 2
  next_h0022_recovery_permitted: false
  h0022_disposition: PARTIAL_HANDOFF_RELEASED_BY_R16
  successor_status: ROTATION_WAIT
  successor_source_id: null
  successor_claim_id: null
  beck_fiala_native_title:
    disposition: STALE_NOT_RESTARTED
    current_preprint_bound: "B(t,n) < 3 sqrt(2 pi t) for all t>=1,n (Guo-Fang-Lu 2026-09-10)"
    independent_recent_check: "Komlos <=36 (Karingula-Lovett ECCC TR26-188, 2026-09-17)"
  next_step: >-
    Continue source/current-status/ownership admission screening on previously unscreened
    HARD OUTSIDE intake candidates. If one is genuinely READY and unowned, claim it
    create-only, freeze one source-valid metric, and begin counterexample-first research.
    Do not reopen H0022 or fabricate a successor from a PENDING row.
```
