Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **not GPT-6 at maximum. NO MOVEMENT: `C_E0071: 1 -> 1`; unchanged count `0 -> 1`; methods #3, #14, #25.**

# R19 CLOSABLE OUTSIDE — E0071 / Björklund Problem 3, source-suggested special-case strengthening

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and preserved predecessor state

I continued from the newest R19 report, `runs/R19/2026-09-18_03-48-00_UTC__e0071-bjorklund-problem3-refutation_b7e1.md`, rather than restarting from the native task title.

The original R19 Hasebe--Ueda target remains frozen exactly as handed off:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084;
- the initial law has the source's exact `(2+alpha)` moment assumption;
- `S_t` may be the law of a classical or a free alpha-stable process;
- the frozen arXiv-v2 conclusion uses **ordinary classical convolution `mu * S_t` even when `S_t` is a free-stable law**;
- the retained alpha=`1/2` source metric is `2/2`;
- stronger-moment/compact-support-only statements are not substituted for source cases;
- the frozen arXiv ordinary-`*` package still lacks the required P26 and distinct OTHER-track end-to-end audits. ALEA free-`boxplus` audits do not discharge that version-specific gate.

I0084 is not reopened in this run. The rotated F0057/Janson package is likewise preserved and not reopened.

## 2. Required repository/source refresh

Before new mathematics I refreshed the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current follow-up implementation manifest, the canonical E0071 claim, the newest R19 report, the I0084 rotation handoff, the current E0071 intake/attempt material, and the newest neighboring Björklund/E0070 report.

The repository remains internally explicit that configuration evidence does not authenticate the runtime model or reasoning level. The scheduler-facing manifests expose prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed duration field, or authenticated applied-run model receipt. The historical P26 `You cannot modify this task` response was an authorization-context event; later authorized contexts may succeed, but R19 does not bypass that boundary and made no scheduler change.

The current active exclusive claim remains `operations/claims/E0071.md`, created by R19 at commit `ab98a7408443ffdbf67834dc1878e058305746dd`.

## 3. Current outside source and status check

Active source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3.

The current source still prints the question

\[
\lim_{n\to\infty}\frac1n\sum_{k=1}^n
\int_G d(gH,H)\,d\mu^{*k}(g)=0?
\tag{P3}
\]

when `H<G` acts ergodically on the Poisson boundary and `d` is a left `G`-invariant metric on `G/H`.

Crucially for this run, immediately after Problem 3 the source itself suggests beginning with the symmetric product/diagonal case

\[
G=G_0\times G_0,\qquad H=\Delta G_0,\qquad \mu=\mu_0\otimes\mu_0,
\]

with symmetric `mu_0`.

A dated 2026-09-18 primary-source/current-literature search again checked the exact formula, the immediately following suggested special case, later Björklund work and citing literature. I recovered no later primary erratum or paper explicitly correcting/resolving this exact printed Problem 3. That remains bounded negative evidence only. Because the obstruction below is elementary and the normalization is suspicious relative to the usual drift theorem, typo/folklore risk is high and publication novelty remains **UNVERIFIED**.

Repository search also still found no completed `P26` E0071 end-to-end PASS and no distinct OTHER-track E0071 end-to-end PASS.

## 4. New idea before validation

The previous run used the smallest Liouville quotient `G=Z`, `H={0}` and parity. The natural objection is that this may be too degenerate relative to the intended homogeneous-space phenomenon.

The new route is therefore to attack the **exact source-suggested product/diagonal class**, preserve symmetry and infinite index, and ask whether the quotient displacement can be identified with an elementary random walk. This is methods #3, #14 and #25 in that order: strengthen the statement, expose the group action, then count/represent the quotient walk in two ways.

## 5. #3 PROVE SOMETHING STRONGER — exact source-suggested special case

Take

\[
G_0=\mathbb Z,
\qquad
\mu_0=\frac14\delta_{-1}+\frac12\delta_0+\frac14\delta_1,
\]

and set

\[
G=\mathbb Z^2,
\qquad
H=\Delta\mathbb Z=\{(m,m):m\in\mathbb Z\},
\qquad
\mu=\mu_0\otimes\mu_0.
\]

The support of `mu` contains `(1,0),(-1,0),(0,1),(0,-1)`, so it semigroup-generates `Z^2`; `mu` is symmetric. The diagonal has infinite index.

Identify

\[
G/H\cong\mathbb Z,
\qquad (x,y)H\mapsto x-y,
\]

and use the left `G`-invariant quotient metric

\[
d((x,y)H,(x',y')H)
=|(x-y)-(x'-y')|.
\tag{1}
\]

The quotient increment is bounded, hence the source integral is finite.

### Poisson-boundary hypothesis

A `mu_0` increment `A` has the exact representation

\[
A\overset d=\frac{\varepsilon_1+\varepsilon_2}{2}
\]

for independent Rademacher variables. Thus after `k` steps one coordinate has distribution `(1/2)S_{2k}` and

\[
P(X_k=0)=\frac{\binom{2k}{k}}{2^{2k}}.
\]

The product coordinates are independent, so

\[
P((X_k,Y_k)=(0,0))
=
\left(\frac{\binom{2k}{k}}{2^{2k}}\right)^2
\sim \frac1{\pi k}.
\]

The return-probability sum diverges. The chain is irreducible, hence recurrent. For any bounded `mu`-harmonic function `f`, optional stopping of the bounded martingale at the almost-sure hitting time of an arbitrary state gives `f(x)=f(y)`. Therefore every bounded harmonic function is constant, the Poisson boundary is a point, and `H` acts ergodically on it.

Thus all Problem-3 hypotheses are satisfied in the source's own proposed structural class.

## 6. #14 FIND THE GROUP ACTING — the diagonal action leaves only the difference coordinate

Let `A_i,B_i` be iid with law `mu_0`, with the two sequences independent. The quotient coordinate after `k` product steps is

\[
Q_k=\sum_{i=1}^k(A_i-B_i).
\]

The diagonal subgroup is exactly what removes the common-coordinate direction: only `x-y` survives. This turns a homogeneous-space question into a one-dimensional random-walk calculation without changing any source hypothesis.

## 7. #25 COUNT THE SAME THING TWICE — exact simple-random-walk law

Because a difference of two independent `mu_0` increments is half the sum of four independent Rademachers,

\[
Q_k\overset d=\frac12S_{4k}.
\tag{2}
\]

Therefore

\[
a_k:=\int_Gd(gH,H)\,d\mu^{*k}(g)
=E|Q_k|
=\frac12E|S_{4k}|.
\tag{3}
\]

For ordinary simple symmetric random walk,

\[
E|S_{2m}|
=2m\frac{\binom{2m}{m}}{2^{2m}}.
\tag{4}
\]

Hence exactly

\[
a_k
=2k\frac{\binom{4k}{2k}}{2^{4k}}
\sim\sqrt{\frac{2k}{\pi}}.
\tag{5}
\]

Consequently

\[
\boxed{
\frac1n\sum_{k=1}^n
\int_Gd(gH,H)\,d\mu^{*k}(g)
\sim
\frac23\sqrt{\frac2\pi}\sqrt n
\longrightarrow+\infty.
}
\tag{6}
\]

This is strictly stronger than the previous parity witness. The printed Problem 3 fails **inside the exact symmetric product/diagonal special case proposed by Björklund**, and its left-hand side diverges rather than merely having positive liminf.

At the same time the ordinary drift normalization behaves as the surrounding Karlsson--Ledrappier motivation suggests:

\[
\frac{a_k}{k}\to0.
\]

This supports a normalization-issue diagnosis but does **not** establish what correction the author intended.

## 8. Validation budget and artifact

The complete proof is in

`artifacts/R19/2026-09-18_04-36-42_UTC__e0071_suggested_special_case_divergence_c314.md`

creation commit

`056e57b23049ffa3b01b4212f50183a4c451055e`.

It was read back from that exact commit. No exact-arithmetic checker was created because the result is an analytic identity/asymptotic argument rather than a finite exhaustive claim. The exact binomial identity is proved on the page.

## 9. Metric and closure status

The frozen source metric was already saturated in the previous run:

\[
C_{E0071}:1\to1.
\]

Therefore this run is honestly **NO MOVEMENT**, and the post-movement unchanged count is `0 -> 1`.

Mathematical label remains **REFUTED AS PRINTED**. Fleet/process status remains

**REFUTED_CANDIDATE / SOURCE_MATCHING / AUDIT_PENDING / NOVELTY_UNVERIFIED**.

The remaining closure obligations are still external to this worker's self-check:

- one independent P26 end-to-end audit of the exact source statement and counterexample;
- one distinct OTHER-track end-to-end audit;
- preserve the bounded prior-art/erratum search and do not convert failure to find a correction into a novelty certificate.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_predecessors:
    I0084:
      source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5"
      convention: "ordinary classical convolution mu * S_t, including when S_t is a free-stable law"
      metric_name: "complete alpha=1/2 source cases under frozen arXiv scope"
      metric_value: "2/2"
      status: "ROTATED_HANDOFF; ordinary-* source-version audits still pending"
    F0057:
      status: "ROTATED / PROVED_CANDIDATE / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  active_source:
    id: E0071
    source: "Michael Bjorklund, arXiv:1406.0763v2, Appendix II section 7.1, Problem 3"
    exact_scope: "printed Cesaro quotient-space drift formula"
    claim_commit: "ab98a7408443ffdbf67834dc1878e058305746dd"
  metric:
    name: C_E0071
    before: 1
    after: 1
    movement: false
  unchanged_count:
    before: 0
    after: 1
  tried_moves: [3, 14, 25]
  status: "REFUTED_CANDIDATE / SOURCE_MATCHING / AS_PRINTED / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  result: "In the source-suggested symmetric product/diagonal case G0=Z, lazy symmetric mu0, G=Z^2, H=Delta Z, the printed Cesaro quantity is asymptotic to (2/3)*sqrt(2/pi)*sqrt(n) and diverges."
  remaining_obligation: "two independent end-to-end audits (P26 plus one distinct OTHER track); prior-art/erratum risk remains independently unchecked"
  evidence:
    claim: "operations/claims/E0071.md @ ab98a7408443ffdbf67834dc1878e058305746dd"
    first_source_refutation: "artifacts/R19/2026-09-18_03-44-00_UTC__e0071_bjorklund_problem3_counterexample.md @ b11f7f1cc91306329e451e08ef505c0e31d75b72"
    strengthening: "artifacts/R19/2026-09-18_04-36-42_UTC__e0071_suggested_special_case_divergence_c314.md @ 056e57b23049ffa3b01b4212f50183a4c451055e"
  audits:
    P26: null
    other: null
```
