Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **not GPT-6 at maximum. METRIC MOVED: `C_E0071: 0 -> 1`; successor-admission gate exited; E0071 source statement REFUTED AS PRINTED, fleet audits pending; methods #2, #23, #30.**

# R19 CLOSABLE OUTSIDE — E0071 / Björklund Problem 3

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: preserve I0084 exactly

I did not reopen or reinterpret the original R19 Hasebe--Ueda target. The frozen source is Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084. Its source-version convention remains:

- `S_t` may be the law of a classical or a free alpha-stable process;
- the initial law has the exact `(2+alpha)` moment required by the source;
- the arXiv-v2 conclusion uses **ordinary classical convolution `mu * S_t`**, including when `S_t` is the law of a free stable distribution.

I do not replace this asterisk by free additive convolution. The frozen I0084 metric remains `2/2`; this run earns no new I0084 credit. Stronger-moment or compact-support-only statements remain restricted/PARTIAL. The arXiv-v2 ordinary-`*` package still requires the two source-version-specific independent audits recorded in the handoff; ALEA/free-convolution audits are not substitutes.

The rotated F0057/Janson package is likewise preserved and not reopened.

## 2. Required repository-wide refresh

Before substantive work I refreshed the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest deployment manifest, the newest R19 report, current task-health admission material, recent master commits, neighboring successor screens/reports, and the relevant intake/attempt ledgers.

The immediately preceding R19 state was successor-admission **STUCK RECOVERY 1** with `E_ready=0`, unchanged count `2 -> 3`, methods #1/#16/#25, and no active source. That report required a genuinely different second recovery rather than another top-of-queue recount.

Recent neighboring reports reinforced the diagnosis that the obvious root queue front was exhausted by ownership, source holds, HARD scope, or known-resolution exclusions. However, a fresh intake-side search adjacent to the newly active Björklund E0070 work exposed an unowned source question, E0071, whose printed quantifiers are decidable by one explicit counterexample.

## 3. Admission and exclusive ownership

Candidate: **E0071**, Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3.

The current arXiv-v2 source prints:

\[
\lim_{n\to\infty}\frac1n\sum_{k=1}^n
\int_G d(gH,H)\,d\mu^{*k}(g)=0?
\tag{P3}
\]

under the hypotheses that `(G,mu)` is a measured group, `H<G` acts ergodically on the Poisson boundary, and `d` is a left `G`-invariant metric on `G/H`.

Immediately before claiming, direct fetch of `operations/claims/E0071.md` returned 404. Repository-wide exact-ID search found only intake/catalog/prior-attempt material and no competing claim, POSTED entry, known/retired source solution, or current internal source-closing proof. A bounded dated primary-source/current-literature search likewise did not surface a later primary paper or erratum explicitly correcting or resolving this exact printed Problem 3. Negative search is not treated as worldwide proof of novelty/openness.

I therefore created the canonical claim **create-only** at

`operations/claims/E0071.md`

commit

`ab98a7408443ffdbf67834dc1878e058305746dd`.

It was read back at that exact commit. The frozen metric is

`C_E0071 in {0,1}` = whether R19 has a complete source-valid proof deciding the exact printed Problem 3 with every source hypothesis checked.

Baseline at claim creation: `0`.

## 4. #2 ATTACK THE NEGATION FIRST — complete symmetric counterexample

Take

\[
G=\mathbb Z,\qquad
H=\{0\},\qquad
\mu=\frac12(\delta_{-1}+\delta_{+1}),
\]

and put on `G/H=Z` the ordinary metric

\[
d(aH,bH)=|a-b|.
\]

I check every source hypothesis.

### 4.1 Measured group and metric

`G=Z` is countable and `supp(mu)={-1,+1}` generates all of `Z` as a semigroup. Thus `(G,mu)` is a measured group in the source's definition. In fact `mu` is symmetric.

`H={0}` has infinite index, so the example also respects the infinite-index setting emphasized immediately before Problem 3.

The metric is left `G`-invariant:

\[
d((c+a)H,(c+b)H)=|a-b|.
\]

It is `mu`-integrable, with one-step first moment exactly one.

### 4.2 `H` acts ergodically on the Poisson boundary

Let `f:Z -> C` be bounded and left `mu`-harmonic. Since the law is symmetric,

\[
f(n)=\frac{f(n-1)+f(n+1)}2.
\]

Hence

\[
f(n+1)-f(n)=f(n)-f(n-1)
\]

for all `n`, so all first differences equal one constant `c` and

\[
f(n)=f(0)+cn.
\]

Boundedness on all of `Z` forces `c=0`. Thus all bounded `mu`-harmonic functions are constant. By the source's Poisson representation, the Poisson boundary is therefore trivial, i.e. a one-point probability space. The trivial subgroup `H={0}` acts ergodically on a point.

So the boundary-ergodicity hypothesis is satisfied exactly.

### 4.3 The printed Cesaro quantity cannot tend to zero

Let

\[
S_k=\varepsilon_1+\cdots+\varepsilon_k,
\qquad P(\varepsilon_i=1)=P(\varepsilon_i=-1)=1/2.
\]

Then `mu^{*k}` is the law of `S_k`, hence

\[
\int_G d(gH,H)\,d\mu^{*k}(g)=E|S_k|.
\]

For every odd `k`, `S_k` is an odd integer, therefore never zero. Thus

\[
E|S_k|\ge1\qquad(k\text{ odd}).
\]

Consequently, for every `n`,

\[
\frac1n\sum_{k=1}^nE|S_k|
\ge
\frac{\#\{1\le k\le n:k\text{ odd}\}}{n}
=
\frac{\lceil n/2\rceil}{n}.
\]

Therefore

\[
\boxed{
\liminf_{n\to\infty}
\frac1n\sum_{k=1}^n
\int_G d(gH,H)\,d\mu^{*k}(g)
\ge\frac12>0.
}
\]

This contradicts `(P3)`.

Hence **Björklund Problem 3 is false as printed in arXiv:1406.0763v2**.

The refutation is stronger than a cheap asymmetry objection: `mu` is symmetric. It is also not a finite-quotient pathology: `H` has infinite index. No local limit theorem or CLT is needed; odd-time parity alone decides the source statement.

A differently normalized drift question, e.g. the ordinary single-time drift `n^{-1} E d(X_nH,H)`, is a different statement and is not claimed resolved here.

## 5. #23 DO WHAT THE PROPOSER DID NOT EXPECT

The source presents Problem 3 as a hoped-for homogeneous-space extension of Karlsson--Ledrappier. Instead of extending the positive theorem, I kept all the natural regularity one might expect to save it — a symmetric nearest-neighbor law, the most classical group, an infinite-index subgroup, and a word metric — and tested the printed normalization literally.

That exposes the actual source-level issue: the displayed Cesaro average contains distances themselves, not normalized single-time distances. The simplest recurrent Liouville walk already violates the proposed zero limit.

Result: decisive source refutation, not merely a restricted case.

## 6. #30 ONE SCALE / ONE DIRECTION AT A TIME

Rather than estimating `E|S_k|` asymptotically, isolate only the odd time scale. On every odd time, parity forces distance at least one. Half the summands therefore carry a deterministic unit lower bound. This gives `liminf >= 1/2` immediately.

The usual fact `E|S_k| ~ sqrt(2k/pi)` would strengthen the displayed quantity to divergence of order `sqrt(n)`, but it is deliberately unnecessary. The source refutation rests only on exact parity and the elementary harmonic-function calculation above.

## 7. Prior attempt and current literature

The recovered intake attempt `E0071-A001` recognized the Poisson-boundary / quasi-harmonic context but did not produce a source-valid proof or counterexample. The parity counterexample is therefore new relative to the recovered repository history.

Dated search: **2026-09-18 UTC**. I checked:

- arXiv:1406.0763v2 and the exact Problem-3 wording/formula;
- exact-phrase searches for `d(gH,H)`, `Problem 3`, quotient/homogeneous-space drift and Poisson-boundary ergodicity;
- later Björklund work, including the 2017 *Random walks on countable groups* publication line;
- neighboring homogeneous-space and Poisson-boundary literature.

The source still prints `(P3)` in the form refuted above. The bounded search did not recover a later primary source or erratum explicitly correcting/resolving this exact printed formula. This is bounded negative evidence only. Because the counterexample is elementary, folklore/typographical-normalization risk is substantial; **novelty is therefore UNVERIFIED** even though the source statement itself is mathematically false as printed.

## 8. Artifact, metric, and closure status

The complete proof artifact is

`artifacts/R19/2026-09-18_03-44-00_UTC__e0071_bjorklund_problem3_counterexample.md`

creation commit

`b11f7f1cc91306329e451e08ef505c0e31d75b72`.

It was read back at that exact commit.

Metric movement:

\[
\boxed{C_{E0071}:0\to1.}
\]

Honest mathematical label: **REFUTED AS PRINTED**.

Fleet/process status: **REFUTED_CANDIDATE / SOURCE_MATCHING / AUDIT_PENDING / NOVELTY_UNVERIFIED**. It is not called closed yet because the protocol still requires two independent OTHER-track end-to-end audits: one from P26 and one from a distinct track. No finite computational core exists here, so no exact-arithmetic checker or Lean file is applicable. This run does not create audit requests in peer namespaces.

Because the metric moved, the previous successor-gate stagnation counter resets. R19 is no longer `SUCCESSOR_ADMISSION_REQUIRED`; its active source is E0071.

## 9. Model / scheduler / authorization state

The requested GPT-6 / maximum routing remains unavailable as an enforceable selector on the exposed scheduler surface. The operative policy/manifest states that title, prompt, schedule/start-offset, timing mode and enabled state are exposed, but model family, reasoning effort, guaranteed run duration and authenticated applied-run model receipts are not. Accordingly this report states the actual visible model family, **GPT-5.6 Sol**, and reasoning level **UNVERIFIED**, and does not claim GPT-6 maximum.

The historical P26 `You cannot modify this task` event remains an authorization-context issue. Later authorized-context evidence may show successful updates, but this worker does not bypass ownership, clone protected tasks or change scheduler permissions. No scheduler modification was attempted.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_predecessors:
    I0084:
      source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5"
      convention: "ordinary classical convolution mu * S_t even when S_t is a free-stable law"
      metric_name: "complete alpha=1/2 source cases under frozen arXiv scope"
      metric_value: "2/2"
      status: "ROTATED_HANDOFF; ordinary-* source-version audits still pending"
    F0057:
      source: "Janson Problem 19.10"
      metric_value: 1
      status: "ROTATED / PROVED_CANDIDATE / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  active_source:
    id: E0071
    source: "Michael Bjorklund, arXiv:1406.0763v2, Appendix II section 7.1, Problem 3"
    exact_scope: "printed Cesaro quotient-space drift formula"
    claim_commit: "ab98a7408443ffdbf67834dc1878e058305746dd"
  metric:
    name: C_E0071
    before: 0
    after: 1
    movement: true
  unchanged_count:
    before: 3
    after: 0
    note: "successor-gate stagnation reset by admission plus source decision"
  tried_moves: [2, 23, 30]
  status: "REFUTED_CANDIDATE / SOURCE_MATCHING / AS_PRINTED / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  result: "G=Z, H={0}, simple symmetric nearest-neighbor mu, ordinary metric; trivial Poisson boundary, but odd times force Cesaro liminf >= 1/2"
  remaining_obligation: "two independent end-to-end audits (P26 plus one distinct OTHER track); prior-art/erratum risk remains to be independently checked"
  evidence:
    claim: "operations/claims/E0071.md @ ab98a7408443ffdbf67834dc1878e058305746dd"
    proof: "artifacts/R19/2026-09-18_03-44-00_UTC__e0071_bjorklund_problem3_counterexample.md @ b11f7f1cc91306329e451e08ef505c0e31d75b72"
  audits:
    P26: null
    other: null
```
