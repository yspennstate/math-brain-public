Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; supported H0022 substantive unchanged count `1 -> 2`; methods actually used: **#9 RANDOMIZE, #11 DUALIZE, #25 COUNT THE SAME THING TWICE**.

# R16 HARD OUTSIDE — H0022: conditioning out the global edge-count fluctuation localizes the second-moment obstruction to mesoscopic overlaps

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, **Conjecture 1.5 (cycle-factor universality)**.

Source status after this run: **OPEN / PARTIAL METHOD PROGRESS**. No source theorem is claimed proved or refuted.

## 1. Continuity, exclusions, ownership, and current-source refresh

I continued from the newest supported R16 report

`runs/R16/2026-09-18T02-25-49Z_h0022-first-moment-type-entropy_f0f1b8.md`

and the active exclusive claim

`operations/claims/H0022.md`.

I also recovered the earlier H0022 report

`runs/R16/2026-09-18T01-44-28Z_h0022-cycle-defect-hamilton-skeleton-route_6f2c.md`.

Both earlier reports used the same initial Section-B triple `#2,#18,#24`; the latest report is the controlling baseline and records supported H0022 unchanged count `0 -> 1`. I therefore advance only the supported count `1 -> 2` in this genuinely different run and do not invent a hidden streak from duplicate historical reporting.

Before new mathematics I reread the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H0022 claim, the H-intake verification, the newest own R16 report, and the neighboring H0023/P20 final handoff. H0023's fixed-permutation path-hypergraph route already exposed quenched clustering and perfect-completion difficulties, so H0022 must not silently assume that stronger linking conjecture.

A fresh bounded literature check on 2026-09-18 still finds arXiv:2608.06358v1 as the current primary H0022 source and no later source-matching proof of Conjecture 1.5. The source still conjectures that for every fixed `epsilon>0` and every integer

\[
\ell\ge (1+\epsilon)\frac{\log n}{\log\log n},
\]

with high probability

\[
G\!\left(n,(1+\epsilon)\frac{\log n}{n}\right)
\]

contains every `n`-vertex cycle factor whose cycles all have length at least `ell`. The source proves only a sufficiently-large-constant analogue, including girth `100 log n/loglog n` at density `C log n/n` for a large absolute `C`.

The fixed R16 metric remains the complete coefficient curve `A_cyc(c)` from the claim: for fixed `c>1`, `A_cyc(c)` is the smallest coefficient for which R16 has a complete proof of universality at density `c log n/n`, with every restriction retained. Unknown slices are `UNMEASURED`, not infinity. The source target is

\[
A_{\rm cyc}(1+\epsilon)\le 1+\epsilon
\quad\text{for every fixed }\epsilon>0.
\]

Before: `A_cyc(1+epsilon)=UNMEASURED`. After: `UNMEASURED`.

## 2. Why change from `G(n,p)` to `G(n,M)` now

The preceding report proved the exact `G(n,p)` second-moment identity

\[
\frac{\mathbb E X_\lambda^2}{(\mathbb E X_\lambda)^2}
=\mathbb E[p^{-K}],
\]

where `F,F'` are independent uniform labelled copies of one cycle-factor type and

\[
K=|E(F)\cap E(F')|.
\]

Since `E K=2n/(n-1)`, Jensen already forces a factor roughly `p^{-2}`. That obstruction is dominated by a common host fluctuation: all spanning factors simultaneously become more numerous when the host has more edges. The same phenomenon is classical for Hamilton-cycle counts; Janson's decomposition/projection work distinguishes the much stronger fluctuations in `G(n,p)` from the more regular counts in `G(n,M)`.

So method **#9 RANDOMIZE** in this run is not another random construction of a factor. It is to randomize the host at **fixed edge count** and ask what overlap scale remains after the global edge-density fluctuation has been conditioned out.

This is a route tool, not a model change in the source statement. H0022 is monotone in the host graph, and a sufficiently uniform theorem across the typical `M`-window could later be transferred back to `G(n,p)`. No such transfer theorem is claimed here.

## 3. #11 DUALIZE — exact fixed-edge-count overlap kernel

Let

\[
N=\binom n2,
\qquad
M=\left\lfloor pN\right\rfloor,
\qquad
p=c\frac{\log n}{n},
\quad c>1\text{ fixed},
\]

and let `G_M` be uniform from `G(n,M)`. For a fixed `s`-edge set `S`, define

\[
Q_s:=\Pr(S\subseteq E(G_M))
=\frac{\binom{N-s}{M-s}}{\binom NM}
=\frac{(M)_s}{(N)_s}.
\]

Fix any cycle-factor type `lambda` on `[n]`, let `F_lambda` denote the family of its labelled copies, and let `X_lambda` count copies inside `G_M`. Every factor has exactly `n` edges. If `F,F'` are independent uniform elements of `F_lambda` and

\[
K:=|E(F)\cap E(F')|,
\]

then the union has `2n-K` edges. Therefore, exactly,

\[
\mathbb E X_\lambda=|F_\lambda|Q_n,
\]

and

\[
\boxed{
\frac{\mathbb E X_\lambda^2}{(\mathbb E X_\lambda)^2}
=
\mathbb E\,W_n(K),
\qquad
W_n(k):=\frac{Q_{2n-k}}{Q_n^2}.
}
\tag{3.1}
\]

This is the fixed-edge-count analogue of the preceding `p^{-K}` identity. The advantage is that `W_n(k)` contains a large *negative* finite-population correction for small overlaps.

### Lemma 3.1 (the overlap-weight transition)

Uniformly for

\[
0\le k=O\!\left(\frac{n}{\log n\log\log n}\right),
\]

we have

\[
\boxed{
\log W_n(k)
=
k\log\frac NM-rac{n^2}{M}
+O\!\left(\frac{n}{\log^2 n}\right).
}
\tag{3.2}
\]

In particular the weight changes from exponentially small to exponentially large at the first scale

\[
\boxed{
k_0
=(1+o(1))\frac{n^2/M}{\log(N/M)}
=\left(\frac2c+o(1)\right)\frac{n}{\log^2n}.}
\tag{3.3}
\]

#### Proof

For `s<=2n`,

\[
\log Q_s
=s\log(M/N)
+\sum_{j=0}^{s-1}
\left[
\log(1-j/M)-\log(1-j/N)
\right].
\]

Here `j/M=O(1/log n)` and `j/N=O(1/n)`. Expanding `log(1-x)` and summing gives, uniformly for `s<=2n`,

\[
\log Q_s
=s\log(M/N)
-\frac{s(s-1)}{2M}
+O\!\left(\frac{n}{\log^2n}ight)
+O(1).
\]

Apply this to `s=2n-k` and twice to `s=n`. The quadratic difference is

\[
(2n-k)(2n-k-1)-2n(n-1)
=2n^2-4nk+k^2+k.
\]

Since `k=O(n/(log n loglog n))`, the `nk/M` and `k^2/M` corrections are `O(n/log^2n)`. This yields (3.2). Since

\[
\frac{n^2}{M}
=\left(\frac2c+o(1)\right)\frac{n}{\log n},
\qquad
\log(N/M)=\log n-\log\log n-\log c+o(1),
\]

(3.3) follows. `square`

This is already qualitatively different from `G(n,p)`: every fixed `k=O(1)` overlap was amplified by `p^{-k}` there, whereas in `G(n,M)` every such overlap receives an overall penalty

\[
\exp\left[-\left(\frac2c+o(1)\right)\frac n{\log n}\right].
\]

So conditioning on the edge count really does remove the elementary Jensen obstruction. But it does **not** finish the second moment: the variance must reappear at a much larger overlap scale.

## 4. #25 COUNT THE SAME THING TWICE — a uniform tail bound for overlaps of long-cycle factors

The key new count is uniform over **every** target type with minimum cycle length at least `ell`.

Fix one labelled cycle factor `F` all of whose cycles have length at least `ell`, and let `F'` be a uniform labelled copy of the same isomorphism type. Put

\[
K=|E(F)\cap E(F')|.
\]

Take a fixed set `S subseteq E(F)` of `j` edges. Write `a(S)` for the number of path components of `S` and `z(S)` for the number of cyclic components. Any cyclic component of `S` is an entire cycle of `F`, hence

\[
z(S)\le j/\ell.
\]

Also

\[
|V(S)|=j+a(S).
\]

### Lemma 4.1 (embedding bound for a prescribed overlap set)

If `2j<=n/2`, then

\[
\boxed{
\Pr(S\subseteq E(F'))
\le
4^j\,e^{8j^2/n}\,n^{-j+j/\ell}.
}
\tag{4.1}
\]

#### Proof

Write the abstract target factor as `H`, and generate `F'=pi(H)` with a uniform permutation `pi` of `[n]`. An injective edge-preserving map of one path component of `S` into `H` has at most `2n` choices: choose the first image vertex and one of at most two directions around its target cycle. An injective map of one cyclic component likewise has at most `2n` choices, because it must map onto one target cycle of the same length, with a choice of start and orientation.

Therefore the number of injective edge-preserving maps `S -> H` is at most

\[
(2n)^{a(S)+z(S)}.
\]

For every such injection there are exactly `(n-|V(S)|)!` extensions to a permutation, so

\[
\Pr(S\subseteq F')
\le
\frac{(2n)^{a+z}}{(n)_{j+a}}.
\]

Using `(n)_v >= (n-v)^v`, `v=j+a<=2j`, `a+z<=2j`, and `z<=j/ell`,

\[
\frac{(2n)^{a+z}}{(n)_{j+a}}
\le
4^j n^{-j+z}(1-2j/n)^{-2j}
\le
4^j e^{8j^2/n}n^{-j+j/\ell}.
\]

This is (4.1). `square`

Now if `K>=j`, some `j`-edge subset `S` of the `n` edges of `F` is contained in `F'`. Union-bounding over those subsets gives

\[
\boxed{
\Pr(K\ge j)
\le
\left[
\frac{4e\,e^{8j/n} n^{1/\ell}}{j}
\right]^j
}
\tag{4.2}
\]

for the range above.

The importance of (4.2) is not that it is a sharp overlap large-deviation theorem. It is that it is **uniform over every allowed cycle-length partition** and explicitly records the only place where whole shared cycles are cheaper than paths: the factor `n^{j/ell}`.

## 5. Main route theorem — after conditioning on edge count, all second-moment mass is forced into a mesoscopic-overlap tail

Combine (3.1), (3.2), and (4.2).

### Theorem 5.1 (uniform conditioned-overlap localization)

Fix constants `c>1`, `A>1`, and

\[
0<\delta<\frac{2}{c(1+1/A)}.
\]

Let

\[
p=c\frac{\log n}{n},
\qquad
M=\lfloor p\binom n2\rfloor,
\qquad
\ell\ge A\frac{\log n}{\log\log n}.
\]

For **every** cycle-factor type `lambda` whose cycles all have length at least `ell`, let `F,F'` be independent uniform labelled copies and `K=|E(F) cap E(F')|`. Put

\[
J_n
:=
\left(
\frac{2}{c(1+1/A)}-\delta
\right)
\frac{n}{\log n\log\log n}.
\]

Then

\[
\boxed{
\mathbb E\!\left[W_n(K)\,\mathbf 1_{\{K\le J_n\}}\right]
\le
\exp\!\left[-\Omega_{c,A,\delta}\!\left(\frac n{\log n}\right)\right].
}
\tag{5.1}
\]

Consequently, because a second-moment ratio is always at least one,

\[
\boxed{
\mathbb E\!\left[W_n(K)\,\mathbf 1_{\{K>J_n\}}\right]
\ge 1-o(1).
}
\tag{5.2}
\]

In words: **once the global edge count is conditioned out, essentially all of the second-moment obstruction is forced into pairs of target factors sharing at least order `n/(log n loglog n)` edges.**

At the exact source coefficients `c=A=1+epsilon`,

\[
\boxed{
J_n
=
\left(
\frac{2}{2+\epsilon}-\delta
\right)
\frac{n}{\log n\log\log n}.
}
\tag{5.3}
\]

#### Proof

The kernel `W_n(k)` is increasing in `k`, since reducing the size of the required union can only increase its fixed-`M` inclusion probability.

First take

\[
j_*:=\frac1c\frac{n}{\log^2 n}.
\]

By Lemma 3.1, uniformly for `j<=j_*`,

\[
\log W_n(j)
\le
-\left(\frac1c+o(1)\right)\frac n{\log n},
\]

so the contribution from `K<=j_*` is exponentially small on the `n/log n` scale.

For `j_*<=j<=J_n`, combine (3.2) and (4.2):

\[
\log\bigl(W_n(j)\Pr(K\ge j)\bigr)
\le
-\frac{n^2}{M}
+j\left[
\log\frac NM-\log j+rac{\log n}{\ell}+O(1)
\right]
+O\!\left(\frac n{\log^2n}\right).
\]

Because `j>=j_*`,

\[
\log j\ge \log n-2\log\log n+O(1),
\]

while

\[
\log(N/M)=\log n-\log\log n+O(1),
\qquad
\frac{\log n}{\ell}\le\left(\frac1A+o(1)\right)\log\log n.
\]

Therefore the bracket is at most

\[
\left(1+\frac1A+o(1)\right)\log\log n.
\]

For `j<=J_n`, its total contribution is at most

\[
\left[
\frac2c-\delta\left(1+\frac1A\right)+o(1)
\right]\frac n{\log n},
\]

whereas

\[
\frac{n^2}{M}
=\left(\frac2c+o(1)\right)\frac n{\log n}.
\]

Thus every term in this range is at most `exp[-Omega(n/log n)]`. Summing over at most `n` possible values of `j` preserves the exponential bound and proves (5.1). Equation (5.2) follows from (3.1) and `E X^2/(E X)^2>=1`. `square`

## 6. What this changes in the route

This is a genuine improvement over the preceding diagnosis.

The last report only showed that the *unconditioned* second moment is bad because `E[p^{-K}]` is already large at constant overlap. Theorem 5.1 shows that after the most obvious common fluctuation is removed, the problem does **not** remain at constant overlap, nor even at the first kernel transition `n/log^2 n`: a uniform count pushes the entire surviving weighted obstruction out to at least

\[
\Theta\!\left(\frac n{\log n\log\log n}\right).
\]

That is a macroscopic number of shared edges compared with the typical overlap `E K=2+o(1)`.

So a conditioned/truncated second-moment route is not dead. It has been reduced to a concrete large-deviation problem:

\[
\boxed{
\text{control the overlap generating function of two long-cycle factors for }
K\gtrsim n/(\log n\log\log n).
}
\]

The crude union bound in Lemma 4.1 loses exactly on overlap sets with many path components (especially matching-like overlap patterns). That identifies the next structure to exploit: **runs of consecutive common edges along the target cycles**, rather than only the total number of common edges.

The simplest unresolved test case remains the first-moment extremal type: equal `C_ell`-factors with

\[
\ell\sim A\frac{\log n}{\log\log n}.
\]

For this type, the intersection of two factors is a union of common runs plus occasionally entire common cycles. A sharp two-parameter count by `(number of common edges, number of runs)` could plausibly close the fixed-type second moment in `G(n,M)` or produce an explicit overlap obstruction. Either outcome moves the route materially.

## 7. Relation to existing literature — mechanism known, exact present scale not certified as novel

I do **not** claim the general `G(n,M)` overlap-second-moment mechanism as new.

- Oliver Riordan, *Spanning Subgraphs of Random Graphs*, CPC 9 (2000), explicitly uses the second moment in `G(n,M)` and expands the variance over overlap subgraphs of the target spanning graph. That is the nearest methodological ancestor of Sections 3--5.
- Svante Janson's work on counts of spanning trees, Hamilton cycles and perfect matchings shows much more regular behaviour in `G(n,m)` than in `G(n,p)` and uses decomposition/projection methods. Its stated normal regime begins around much denser `m` than the present `Theta(n log n)` boundary, so it does not settle H0022.
- Kahn--Lubetzky--Wormald, *Cycle Factors and Renewal Theory* (CPAM 70, 2017), develop sharp renewal-without-replacement estimates for cycle-factor questions in random regular graphs. Their model is different, but their run/renewal technology is now the most concrete candidate for the large-overlap counting problem isolated above.

I found no source in this bounded search that states Theorem 5.1 with this uniform long-cycle-factor scale. That negative search is **not** a novelty certificate.

## 8. Why the fixed metric does not move

Theorem 5.1 is a reduction of the fixed-type second moment, not an existence theorem. It does not show that even one prescribed long-cycle factor occurs with high probability at the source density, and therefore does not show universality over all factor types.

Accordingly:

`A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`.

Supported H0022 substantive unchanged count:

`1 -> 2`.

This is not yet a stuck run. If the next substantive H0022 run again leaves the metric unchanged, the supported count reaches three and the following invocation must execute the Section-I thinking-only stuck protocol.

## 9. Next methods

The next nonrepeating Section-B triple is:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce an overlap fugacity `z` and a second parameter counting common runs, then locate the saddle of the exact overlap generating function rather than bounding only `K`;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** compare the resulting saddle/renewal equation with Kahn--Lubetzky--Wormald's renewal-without-replacement constants and Riordan's overlap expansion;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** port the best available renewal/polymer counting machinery for path runs in permutations/cycle factors, while keeping the `G(n,M)` weight kernel exact.

The goal of that run is binary and falsifiable: either obtain a summable uniform overlap expansion for the equal-short `C_ell` factor at some explicit `A,c`, which would finally produce a measured `A_cyc(c)` fixed-type milestone, or exhibit a specific overlap family whose weighted contribution prevents that second-moment closure.

## 10. Beck--Fiala native-title refresh

The stale native R16 title still should not be reopened.

- Bansal--Jiang, arXiv:2508.03961v2, prove the `O(sqrt(t))` Beck--Fiala order for `t>=log^2 n` and have extra logarithmic losses below that regime.
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 September 2026), claim the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no `n` restriction.
- Karingula--Lovett, ECCC TR26-188 (17 September 2026), give a separately authored elementary simplification with Komlos constant `36`, hence another complete uniform Beck--Fiala consequence `B(t,n)<=36 sqrt(t)`.

These are extremely recent preprint/report resolutions, not mature refereed consensus. But the native all-`t,n` Beck--Fiala gap is no longer an appropriate active R16 research target under the current repository continuity policy.

## 11. Model/scheduler control status

The model-control limitation remains unchanged. The exposed scheduling control schema provides task identity, prompt/title, schedule or relative start, timing mode, and enabled state, but **no binding model-family field, no reasoning-effort field, and no authenticated applied-model receipt**. Therefore GPT-6/maximum can be requested in prompt text only in this surface.

Actually enforcing GPT-6/maximum would require an authorized product/workspace scheduler or API that exposes those selectors and runtime telemetry. The historical P26 `You cannot modify this task` error was authorization-context-specific; repository reconciliation records a later successful P26 update from an authorized context. For a task that still returns that error, the compliant workaround is the owning workspace/account context or platform support, not duplication or permission bypass.

No scheduler state was changed in this run.

## 12. Verification and artifacts

No finite checker was manufactured. The new claims are asymptotic analytic identities/inequalities and their full proofs are written above. There is no finite enumeration claim whose truth depends on code.

This run writes only this immutable R16 report. It does not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, any peer track, email, Drive, public sites, permissions, purchases, or workflows.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  active_source: H0022
  source_status: OPEN_PARTIAL
  metric: A_cyc(1+epsilon)
  before: UNMEASURED
  after: UNMEASURED
  movement: NO_MOVEMENT
  supported_unchanged_before: 1
  supported_unchanged_after: 2
  methods_used: [9, 11, 25]
  new_result:
    name: uniform_conditioned_overlap_localization
    statement: >-
      In G(n,M) with M=(c/2+o(1)) n log n, for every cycle-factor type
      of minimum cycle length at least A log n/loglog n, the normalized
      second-moment contribution from pairs sharing at most
      (2/[c(1+1/A)]-delta) n/(log n loglog n) edges is
      exp(-Omega(n/log n)).
    scope: route theorem; not source closure
  next_methods: [5, 17, 21]
  next_obligation: >-
    Count overlap runs for the equal-short C_ell factor in the exact G(n,M)
    kernel; either prove a summable overlap expansion for an explicit A,c or
    identify an explicit weighted overlap family that blocks the second moment.
  checker: NONE_ANALYTIC_PROOF_ON_PAGE
  shared_roots_edited: false
  scheduler_changed: false
```
