Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# E0052 / Feige source-resolution reconciliation for R7-03

Date checked: 2026-09-18 UTC  
Slot: `R7-03 Boundary-Case Research`  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Repository: private `yspennstate/math-open-problems`, existing `master`  
R7-03 assignment status: **PENDING_ADMISSION**

## 1. Why this screen is material

R7-03's earlier immutable report `research7_2026-09-17/R7-03/runs/2026-09-18/2026-09-17T222857Z__report.md` classified shard-2 candidate `E0052` as a genuine sharp-constant problem but honestly **HARD**, because that run did not recover a source-matching resolution.

That disposition is now obsolete. A useful neighboring screen, `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T07-32-00Z__successor-admission-screen-2-e-series.md`, already records `E0052` as resolved in 2026 literature. This artifact does not claim to discover that fact first. It reconciles R7-03's own cumulative state, checks the exact event convention against the corrected intake, and records the precise theorem-to-source implication so that R7-03 will not reconsider the row as open.

Canonical shard check is exact and case-sensitive:

`sum(ord(c) for c in "E0052") = 268`, hence `268 mod 7 = 2`.

No `operations/claims/E0052.md` exists at the checked fresh master. That absence is not a reason to claim it: the source is positively resolved.

## 2. Exact source statement and the intake correction

The canonical source record is Afonso S. Bandeira, *Ten Lectures and Forty-Two Open Problems in the Mathematics of Data Science* (2015/2016 lecture notes), Section 4.8, Conjecture 4.33, attributed there to Uriel Feige. Stable lecture-note URL checked:

`https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf`

The repository correction file `probability_1000_intake_E_20260908/CORRECTIONS.md` is essential. It records that the original E0052 row misstated the source. The source statement is:

> For independent nonnegative random variables `X_1,...,X_n` satisfying `E X_i = 1`, prove
> `P(sum_i X_i >= n+1) <= 1-e^{-1}`.

The original row had instead written a lower bound for `P(sum_i X_i <= n+1)`. Those are not complements because they overlap on the atom `S=n+1`.

Write

`S = X_1 + ... + X_n`.

The exact complementary event to the source upper tail `{S >= n+1}` is the **strict** event `{S < n+1}`. Any source reconciliation must preserve this strict/non-strict boundary.

## 3. Positive current resolution evidence

### 3.1 Fu--Han--Wang--Yan--Zhang--Zhou, 27 July 2026

Primary source checked on 2026-09-18:

Weibo Fu, Yanjun Han, Guanyang Wang, Jun Yan, Peng Zhang, Zhengqing Zhou, *Sharp small-deviation inequalities for sums of independent nonnegative random variables*, arXiv:2607.23980, submitted 27 July 2026.

`https://arxiv.org/abs/2607.23980`

Their Theorem 1.1 states: if `X_1,...,X_n` are independent, nonnegative and `E X_i <= 1`, then for `delta>0`,

`P(S < E S + delta) >= b_{n,delta}`,

where for `delta >= 1`,

`b_{n,delta} = (1 - 1/(n+delta))^n`,

and the bound is optimal for every fixed `n` and every `delta>=1`.

The paper itself explicitly states that the `delta=1` specialization proves Feige's conjecture.

### 3.2 Independent same-day proof

Zipei Nie and Jiaye Wei, *On Feige's conjecture*, arXiv:2607.24528, submitted 27 July 2026:

`https://arxiv.org/abs/2607.24528`

Its abstract states directly that for independent nonnegative mean-one variables,

`P(S < n+1) >= (n/(n+1))^n >= 1/e`.

Thus the source conclusion is not supported by a single isolated search hit.

### 3.3 Later stronger route through Samuels' conjecture

Zhi Ling, *On Samuels' Conjecture*, arXiv:2608.18392, submitted 18 August 2026:

`https://arxiv.org/abs/2608.18392`

The paper claims a sharp general product formula for arbitrary prescribed coordinate means and states that Feige's conjecture follows immediately in the equal-means case. The Fu et al. and Nie--Wei papers already suffice for E0052, so E0052's disposition does not depend on independently validating this later stronger claim.

## 4. Exact theorem-to-source derivation

This is the key semantic check missing from a title-only status screen.

Assume the exact E0052 source hypotheses:

1. `X_1,...,X_n` are independent;
2. `X_i >= 0` almost surely;
3. `E X_i = 1` for each `i`.

Then

`E S = n`.

Apply Fu et al. Theorem 1.1 with `delta=1`. Because `delta>=1`,

`b_{n,1} = (1 - 1/(n+1))^n = (n/(n+1))^n`.

Therefore

`P(S < n+1) >= (n/(n+1))^n`.                 (4.1)

The source event is the exact complement:

`{S >= n+1} = {S < n+1}^c`.

Taking complements in (4.1),

`P(S >= n+1) <= 1 - (n/(n+1))^n`.            (4.2)

Finally, for `x>=0`, `log(1+x)<=x`. With `x=1/n`,

`n log(1+1/n) <= 1`,

hence

`(n/(n+1))^n = exp(-n log(1+1/n)) >= e^{-1}`.

Substituting into (4.2),

`P(S >= n+1) <= 1 - e^{-1}`,

which is exactly Bandeira Conjecture 4.33 / Feige's source statement.

Thus E0052 is **KNOWN / RESOLVED_IN_LITERATURE_2026**, not an open R7-03 target.

## 5. Finite-n sharpness and the boundary atom

The resolved theorem is stronger than the source uniform constant.

For each fixed `n`, take independent variables

`X_i = n+1` with probability `1/(n+1)`,

`X_i = 0` with probability `n/(n+1)`.

Then `E X_i=1`. Moreover,

`S < n+1`

holds if and only if **all** `X_i` vanish. Therefore

`P(S < n+1) = (n/(n+1))^n`,

and hence

`P(S >= n+1) = 1 - (n/(n+1))^n`.

So the finite-`n` improvement in (4.2) is exact. As `n -> infinity`,

`(n/(n+1))^n -> e^{-1}`,

so the source constant `1-e^{-1}` is asymptotically optimal uniformly over `n`.

This example also explains why the intake's old event `P(S <= n+1)` was semantically dangerous: here the event includes configurations with exactly one nonzero coordinate, whereas the correct strict lower event `{S<n+1}` includes only the all-zero configuration.

## 6. Admission-side Section-B methods

No source is being admitted, so these are source-screening mathematics rather than an admitted-target research iteration.

### B2 — attack the negation first

Stress-test the claimed resolution against the source's extremal two-point law and especially the atom at `S=n+1`. The exact strict complement survives: Fu et al. control `{S<n+1}`, whose complement is precisely the source tail `{S>=n+1}`. No hidden equality-event gap remains.

**Outcome:** the positive resolution is source-matching, not merely nearby.

### B6 — deform from a solved parameter point

The 2026 theorem is a one-parameter sharp inequality in `delta`. Specializing the solved family to the source endpoint `delta=1` produces the exact finite-`n` strengthening (4.2), not just the asymptotic `1-e^{-1}` constant.

**Outcome:** source closure follows as an immediate exact specialization.

### B30 — localize the gluing/status failure

The only repository-level mismatch was semantic: E0052's original intake row had swapped to `P(S<=n+1)`, while the source and 2026 proofs naturally pair the strict lower event `{S<n+1}` with the upper event `{S>=n+1}`. Once the correction file is obeyed, there is no remaining mathematical gluing gap.

**Outcome:** disposition corrected from R7-03's old `HARD` screen to `KNOWN / RESOLVED_IN_LITERATURE_2026`.

## 7. Ownership and admission consequence

- Exact candidate ID: `E0052`.
- R7-03 shard: yes, residue 2 mod 7.
- Canonical claim file at checked master: absent.
- Source status: **positively resolved in 2026 literature**.
- R7-03 action: **DO NOT CLAIM / DO NOT ADMIT**.
- R7-03 remains **PENDING_ADMISSION**.
- No successor metric is initialized from E0052.
- No predecessor metric or stagnation count is inherited.

The neighboring NM13-05 screen already recorded the resolution; this artifact's value is exact event-convention reconciliation and repair of R7-03's own earlier HARD disposition, not priority or novelty.
