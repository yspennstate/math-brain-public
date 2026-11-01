Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family/reasoning-effort selector or per-run attestation, so I do not claim otherwise. **NO MOVEMENT: active R19/F0057 `M_TV: 1 -> 1`; unchanged count `5 -> 6`; mandatory CLOSABLE ROTATION; methods #4 PROVE SOMETHING WEAKER COMPLETELY, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS.**

# R19 — F0057 source-only repair and mandatory rotation

Run date: 2026-09-17 UTC. Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Repository continuity and preserved history

Before new mathematics I reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md` and `QUEUE.md`, the operative follow-up implementation manifest, the current F0057 create-only claim, the newest R19/F0057 report, the source-proof artifacts, the older F0057 campaign memo, current audit searches, and the newest coordinator admission screen.

The create-only owner before this run remains R19 at `operations/claims/F0057.md`. The frozen F0057 metric is binary:

`M_TV = 1` iff the complete source fixed-`j` total-variation theorem is proved under the exact Janson Theorem 18.7/19.7 scope, including the source's tuned `xi^(n)` formulation when invoked.

The first R19/F0057 run already moved `M_TV: 0 -> 1`; the five intervening runs left it at `1`.

The original Hasebe--Ueda I0084 assignment remains frozen at its rotation handoff and was **not reopened**. Preserve exactly Conjecture 5.5's ordinary classical convolution

\[
\mu*S_t,
\]

including when `S_t` is the law of a free stable distribution. Its exact `(2+alpha)`-moment assumption, original skewness conventions and retained `alpha=1/2` internal count `2/2` remain preserved. Stronger-moment and compact-support statements remain restricted/PARTIAL.

## 2. Fresh source / literature / audit check

The primary Janson source was rechecked on 2026-09-18 local date. Its published Problem 19.10 still reads: does

\[
d_{\rm TV}(Y_{(j)},\xi_{(j)})\to0
\]

hold for every fixed `j` under Theorem 19.7? The surrounding text says the author proves only the maximum in total variation, expects a modification for fixed `j`, and also expects a finite-dimensional joint extension.

Fresh exact and near-exact web searches for the problem wording, the `d_TV(Y_(j),xi_(j))` statement and conditioned random-allocation order statistics recovered the original source and neighboring literature but no later primary theorem explicitly resolving this exact problem. This remains a **bounded negative search**, not a novelty certificate.

Repository-wide exact audit search still found no completed current `P26-AUDIT-R19-F0057` PASS and no distinct second OTHER-track end-to-end PASS. The recovered audit count remains `0/2`.

## 3. Method #4 — source-only proof package

The first proof artifact had become surrounded by several later strengthenings. This run removed all unnecessary dependencies and wrote a short proof using only four source inputs:

1. fixed-`j` Kolmogorov convergence;
2. the source global cutoff `B_n`;
3. the source uniform fixed-coordinate conditioned/iid local ratio below `B_n`;
4. the resulting finite moving-set Poisson limits.

No growing-rank theorem is needed. The complete source-only argument is written at

`artifacts/R19/2026-09-17_23-36-18_UTC__f0057_source_only_rotation_handoff_b742.md`

created at commit

`ffff70e2570940460422d1711f41cf0e9a34d839`

and read back from that exact commit, blob

`48844b6475e45f4413ece26abb5f249b16b9059a`.

## 4. Method #24 — exact extremal block identity

The least transparent step in the first R19 proof was the good-block estimate. This run replaces it by an exact identity.

For one thin good block, let

\[
X\sim{\rm Po}(\alpha),\qquad
Z\sim{\rm Po}(\gamma),\qquad
R\sim{\rm Po}(\beta)
\]

be the limiting counts in the positive-set part `A`, complement part `C`, and above-block region. Conditional on `R=r<j`, put `k=j-r`. The necessary event for the conditioned order statistic to land in `A` is

\[
\{X\ge1,\ X+Z\ge k\},
\]

while the sufficient iid event is

\[
\{Z=0,\ X\ge k\}.
\]

The latter is a subset of the former, so their gap is exactly

\[
\boxed{
\Delta_k(\alpha,\gamma)
=P(Z\ge1,\ X\ge1,\ X+Z\ge k)
\le(1-e^{-\alpha})(1-e^{-\gamma})
\le\alpha\gamma.
}
\]

The threshold extremizer is explicit: at `k=1` equality holds in the first inequality, so the worst rank branch is `r=j-1`. Thinness gives

\[
\alpha+\gamma\le\eta_j(D,\delta)
=(j!e^D\delta)^{1/j},
\]

and disjointness of the complement pieces gives total `gamma` intensity at most `D`. Therefore all good blocks contribute at most

\[
D\eta_j(D,\delta),
\]

improving and simplifying the previous `2D\eta_j` estimate.

Together with the unchanged bad-block estimate,

\[
\limsup_{n\to\infty}d_{\rm TV}(Y_{(j)},\zeta_{n,(j)})
\le
D(j!e^D\delta)^{1/j}+\delta+e^{-D/8}.
\]

First `\delta\downarrow0` at fixed `D`, then `D\to\infty`, proves the source fixed-`j` theorem.

## 5. Method #27 — quantifier swap removes set-selection dependence

Before defining the total-variation maximizing set, I stated and proved the uniform moving-set lemma:

for every fixed number of arbitrary disjoint moving sets `E_{s,n}\subseteq[0,B_n]`, every fixed joint factorial moment of their conditioned occupancy counts is `1+o(1)` times the iid factorial moment, **uniformly over the moving sets**.

This follows directly from the source's uniform fixed-coordinate ratio, since the factorial-moment expansion has nonnegative summands. Only after this uniform statement is established do we define

\[
S_n=\{k:P(Y_{(j)}=k)>P(\zeta_{n,(j)}=k)\}.
\]

Thus no hidden dependence on the `n`-dependent TV-positive set remains.

## 6. Metric and status

These are proof repairs and simplifications, not a second source case. Therefore

`M_TV: 1 -> 1`.

The honest mathematical status remains

**PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED**.

No finite checker was created: the new claim is an analytic local-limit/Poisson inequality with its complete elementary core written on the page, and there is no finite computational certificate that would establish the asymptotic theorem.

## 7. Mandatory CLOSABLE rotation

This is the **sixth consecutive unchanged F0057 run** after the original metric movement. The controlling rule therefore requires rotation rather than another hour of F0057 polishing.

F0057 is now operationally

**ROTATED / PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED**.

Rotation is not mathematical closure. If reassigned later, the remaining obligation is exactly:

- one P26 end-to-end audit of the exact source package;
- one distinct OTHER-track end-to-end audit;
- ordinary publication-level prior-art/novelty review.

The durable handoff is the source-only artifact at commit `ffff70e2570940460422d1711f41cf0e9a34d839`, together with the earlier first full proof and weak-fixed-law stress test listed there.

## 8. Successor gate

The newest coordinator admission screen establishes **zero currently free READY + CLOSABLE + UNASSIGNED successors** on the screened front. Historical candidates I0004 and I0075 that had once been admitted as free are now canonically claimed elsewhere. Other attractive front rows are claimed, resolved, held, or not fully admitted.

Accordingly R19 does **not** fabricate a successor, steal another worker's target, overwrite an owner, or promote a PENDING row to READY. The post-rotation R19 state is

`SUCCESSOR_ADMISSION_REQUIRED`.

No new claim file was created.

## 9. Model / scheduler truth

The exposed task-management surface still has prompt/title/schedule/timing/enabled-state controls but no binding model-family selector, reasoning-effort selector, authenticated completed-run model telemetry, or guaranteed-duration setting. GPT-6 / maximum remains prompt-only on this surface.

The historical P26 `You cannot modify this task` response was authorization-context-specific. Current root evidence records a later authorized P/C context in which the P26 prompt update succeeded. The lawful workaround is the owning/authorized context or product/backend support that exposes model/reasoning controls; no duplication, permission bypass or scheduler change was attempted here.

## 10. `ledger_delta`

```yaml
ledger_delta:
  worker: R19
  active_source: F0057
  source_citation: "Svante Janson, Probability Surveys 9 (2012), Problem 18.10/19.10"
  preserved_rotated_source: I0084
  preserved_i0084_convolution: "ordinary classical convolution mu*S_t, including free-stable-law S_t"
  metric_name: M_TV
  metric_before: 1
  metric_after: 1
  movement: "NO MOVEMENT"
  unchanged_count_before: 5
  unchanged_count_after: 6
  tried_moves: [4, 24, 27]
  outcome: "source-only proof isolated; exact extremal block identity Delta_k<=alpha gamma with k=1 extremizer; moving-set quantifiers made uniform before TV-positive set"
  status: "ROTATED / PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED"
  remaining_obligation: "two independent OTHER-track end-to-end PASS audits; publication novelty unverified"
  audit_ids: []
  successor_state: "SUCCESSOR_ADMISSION_REQUIRED"
  evidence:
    - "artifacts/R19/2026-09-17_23-36-18_UTC__f0057_source_only_rotation_handoff_b742.md @ ffff70e2570940460422d1711f41cf0e9a34d839"
    - "artifacts/R19/2026-09-17_22-36-42_UTC__f0057_weak_fixed_transfer_stress_e4a7.md"
    - "artifacts/R19/2026-09-17_17-37-27_UTC__f0057_full_proof_6c1e.md"
```

No shared root, peer file, email, Drive item, public post, permission or scheduler was modified.