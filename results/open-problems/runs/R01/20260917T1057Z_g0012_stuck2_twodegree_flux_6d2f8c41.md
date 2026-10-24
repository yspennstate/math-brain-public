Model actually running: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so GPT-6 maximum is not claimed. **NO FIXED-METRIC MOVEMENT: `alpha_univ = 1 -> 1`; G0012 unchanged count `3 -> 4`, status `STUCK_RECOVERY_2 / OPEN_PARTIAL`. Section-B methods actually used: #1 CHANGE THE CATEGORY, #14 FIND THE GROUP ACTING, #30 ONE SCALE AT A TIME.**

# R01 — G0012 Alon–Peres non-backtracking birthday conjecture — stuck recovery 2

Repository/branch: `yspennstate/math-open-problems` / `master`. Private GitHub only.

## 1. Continuity, exclusions, source and current literature

I continued from the newest complete R01 report

`runs/R01/20260917T0930Z_g0012_stuck1_local_volume_1c7e9a42.md`,

which explicitly selected the Section-I recovery action **PROVE THE SIMPLEST UNPROVED SPECIAL CASE: the `{3,D}` degree-set case** and prescribed methods `#1/#14/#30` for the next attack.

I did not reopen either retired predecessor:

- `I0024` / Aldous–Fill Open Problem 3.44 remains **PROVED / INTERNAL-CLOSED** at exact distortion `C=1`, with its right-inverse formula and distinct R20/P26 PASS audits.
- `I0113` / Salez Problem 2.7 remains **PARTIAL / PROVED-CANDIDATE / ROTATED** after its six-run gate.
- `G0012` remains the exclusive R01 successor under `operations/claims/G0012.md`.

Before new mathematics I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/DEPLOYMENT.md`, the G0012 claim, the newest own report and the newest neighboring R02 reports. The newest R02 material located is still **OPEN / PARTIAL** on I0095; no complete neighboring closure package is ready, so I spent no second-audit budget.

### Source/current-status refresh — 2026-09-17

Primary source: Benjamin Dozier, *The Birthday Paradox for non-backtracking walks on regular graphs*, arXiv:2608.26321, 26 August 2026, Conjecture 1.5 (Alon–Peres). The source target remains:

> for every `epsilon>0` there is a universal `C(epsilon)` such that every simple `n`-vertex graph of minimum degree at least `3`, every starting oriented edge, and every `k>C(epsilon) sqrt(n)` has simple-NBW probability below `epsilon`.

Fresh bounded queries on 2026-09-17 rechecked Dozier, the citing/follow-up literature, and the 10 August 2026 paper of Bencs–Goldberg–Jenssen–Jerrum–Pete–Regts–Yin, arXiv:2608.09729. Current primary metadata still says Dozier resolves the **fixed-degree regular** case. Bencs et al. still prove `O_Delta(sqrt(n) log n)` expected self-intersection for fixed maximum degree and `O(sqrt(n))` for regular uniform expanders; their paper explicitly leaves the minimum-degree-only `O(sqrt(n))` question open. A bounded search found no later source-matching resolution. Negative search is not a novelty certificate.

I also recovered the classical Erdős–Kelly regular-completion theorem through a primary mathematical source quoting the exact criterion: if a finite simple graph has maximum degree `d`, maximum deficiency `e` and total deficiency `s`, then the least number `m` of new vertices needed for an induced `d`-regular supergraph is the least integer satisfying

`m d >= s`, `m^2-(d+1)m+s >= 0`, `m>=e`, and `(m+p)d` even.

This is classical machinery, not a novelty claim.

### Frozen metric

`alpha_univ` is still the smallest exponent proved over the **full minimum-degree-3 source domain**.

Before: `1`.

After: `1`.

**No movement.** The new theorem below is a nontrivial `{3,D}` special-case theorem, but it has an additional cross-flux hypothesis and therefore cannot move the unrestricted metric.

---

## 2. Recovery target and notation

The simplest unproved special case selected in the previous stuck report is:

> every vertex has degree either `3` or `D`, where `D>=4` may grow with `n`, with no bipartiteness, expansion or placement assumptions.

Write

`L={v:d(v)=3}`, `H={v:d(v)=D}`,

and let

`B=e(L,H)`

be the number of cross edges. The dimensionless normalized cross flux is

\[
A:=\frac{B}{D-1}.
\tag{2.1}
\]

The point of this normalization is probabilistic: from a high-degree vertex `v`, one NBW departure has denominator `D-1`, while the number of low-degree candidate outputs is the cross-degree of `v`.

The previous report showed why a single-plan splice loses a factor `D-1`. This run first changes category to preserve that information, then uses a two-scale decomposition to prove the full square-root birthday law whenever `A` is bounded independently of `n` and `D`.

---

## 3. Method #1 — CHANGE THE CATEGORY: exact degree-free tail swapping on a two-path space

The single-plan derangement surgery from the preceding run has a local information bottleneck. A two-path space removes that bottleneck at the level of path weights.

For a finite NBW path

\[
P=(x_0,x_1,\ldots,x_r),
\]

started from a fixed oriented edge, write its path weight as

\[
w(P)=\prod_{i=1}^{r-1}\frac1{d(x_i)-1}.
\tag{3.1}
\]

Let two NBW paths meet at a marked vertex `z`:

\[
P=(x_0,\ldots,x_{a-1},z,x_{a+1},\ldots,x_r),
\]

\[
Q=(y_0,\ldots,y_{b-1},z,y_{b+1},\ldots,y_s).
\]

Assume the cross-splices are themselves non-backtracking,

\[
y_{b+1}\ne x_{a-1},\qquad x_{a+1}\ne y_{b-1}.
\tag{3.2}
\]

Swap the two future tails at the marked meeting:

\[
P'=(x_0,\ldots,x_{a-1},z,y_{b+1},\ldots,y_s),
\]

\[
Q'=(y_0,\ldots,y_{b-1},z,x_{a+1},\ldots,x_r).
\]

### Lemma 3.1 — marked tail-swap invariance

Under (3.2),

\[
\boxed{w(P)w(Q)=w(P')w(Q').}
\tag{3.3}
\]

**Proof.** Every transition denominator away from `z` appears once on each side. At `z`, the ordered pair has two transition factors `1/(d(z)-1)` before the swap and the same two factors after it. No degree comparison between the two paths is needed. The operation is an involution when the two marked split locations are retained. ∎

This is exactly what the single-plan splice lacked: the old outgoing tail is not destroyed; it is carried by the second path. Hence the pair-space surgery is genuinely degree-free. What is not yet proved is a bounded-preimage map from one primary simple path plus an auxiliary continuation to a bad primary path after forgetting the auxiliary marker. That remaining inverse-map problem is where the next attack must concentrate.

**Outcome of #1:** no `alpha_univ` movement, but the `(D-1)` entropy loss is not fundamental once the probability space is enlarged to retain the old tail.

---

## 4. Method #14 — FIND THE GROUP ACTING: the missing entropy is exactly one `(d-1)`-valued marker

Let `N` be a `d`-element neighbor set, `q in N`, and let `D_d` be the derangements of `N`. For `p!=q`, define the fiber

\[
D_d(q\to p)=\{\pi\in D_d:\pi(q)=p\}.
\]

The stabilizer of `q` in the symmetric group on `N` acts transitively on `N\setminus\{q\}` and, by conjugation, gives bijections between all fibers `D_d(q->p)`. Consequently all fibers have one common size `R'_d` and

\[
\boxed{|D_d|=(d-1)R'_d.}
\tag{4.1}
\]

This recovers the local cardinality obstruction from the previous report in an invariant form: any map that sends all unmarked local states into one prescribed fiber must have average reverse multiplicity at least `d-1`.

But (4.1) also says exactly how much auxiliary state is sufficient. Choose for each `p!=q` a permutation `sigma_p` fixing `q` and carrying `p` to a fixed `p_*`. Then

\[
\pi\mapsto
\bigl(\sigma_{\pi(q)}\pi\sigma_{\pi(q)}^{-1},\,\pi(q)\bigr)
\tag{4.2}
\]

is a bijection from `D_d` to

\[
D_d(q\to p_*)\times (N\setminus\{q\}).
\]

So a forced splice becomes information-preserving after carrying **one marker with `d-1` possible values**. The marked tail in Lemma 3.1 is a natural probabilistic carrier for precisely this marker.

This rules out wasting more runs looking for a miraculous one-plan conjugation that beats the cardinality ratio: without auxiliary state it cannot. It also makes the next target precise — turn the marker-preserving pair involution into a collision-producing many-to-one comparison whose marker can be summed out at bounded cost.

**Outcome of #14:** no metric movement; exact structural diagnosis and a canonical marker-preserving local model.

---

## 5. Method #30 — ONE SCALE AT A TIME: solve a two-scale `{3,D}` regime

The rest of the run separates long homogeneous degree blocks from degree-class switching.

### 5.1 First remove a stale restriction: the previous heat-bath proof is uniform over *all* regular degrees

The preceding `0802Z` report stated its theorem for bipartite biregular graphs. Its corrected global-averaging argument actually gives a useful corollary that does not need bipartiteness.

### Lemma 5.1 — uniform-in-degree regular birthday bound

For every simple `r`-regular graph on `N` vertices, every `r>=3`, every starting oriented edge and every `ell>=1`,

\[
\boxed{
\Pr(\text{length-}\ell\text{ NBW is simple})
\le 4800\,\frac{N}{\ell^2}.
}
\tag{5.1}
\]

**Proof.** If `ell^2<4704 N`, the right side exceeds one, so (5.1) is trivial. Otherwise repeat the corrected heat-bath plan proof from `runs/R01/20260917T0802Z_g0012_biregular_heatbath_7b4e2c19.md` and its correction memo. The only class-specific inputs in that proof are now immediate:

\[
2m=Nr,
\qquad
W=(\ell-1)(r-2),
\]

so for `ell>=4`,

\[
\frac{2m}{W}
=\frac{Nr}{(\ell-1)(r-2)}
\le \frac{4N}{\ell},
\tag{5.2}
\]

which is stronger than the `6N/ell` estimate used there. The final-endpoint fraction, discarded late-index fraction and reverse heat-bath mass are also no larger than the corresponding biregular estimates because `(r-2)/W=1/(ell-1)`. Excursion inversion uses only that inverse derangements are derangements and that the corrected averaging is over all simple plans; bipartite alternation is not used. Thus the same choice `L=ceil(48N/ell)` and the same loose constants yield (5.1). ∎

This is stronger than Dozier's fixed-degree formulation in the sense that the displayed constant is independent of `r`. A bounded dated search did not surface a paper explicitly stating this uniform-in-`r` corollary, but **publication novelty is UNVERIFIED** and no priority claim is made.

### 5.2 Classical regular completion turns a same-degree block into a regular-graph event

Let `F` be any simple graph on `q` vertices with maximum degree at most `r`, where `r<=n-1`. We need an `r`-regular induced supergraph of controlled size even when `Delta(F)<r`.

Add a disjoint clique `K_{r+1}` and call the resulting graph `F_0`. Then

\[
p=|V(F_0)|=q+r+1,
\]

and `Delta(F_0)=r`. Its total deficiency relative to `r` is

\[
s=\sum_{v\in V(F)}(r-d_F(v))\le qr,
\]

and its maximum deficiency is at most `r`.

Apply the exact Erdős–Kelly induced regular-completion criterion quoted above. Taking the number of new vertices to be `m=p` satisfies every condition:

\[
pr\ge qr\ge s,
\]

\[
p^2-(r+1)p+s=pq+s\ge0,
\]

`p>=r`, and `(m+p)r=2pr` is even. Therefore there is a simple `r`-regular induced supergraph `\widehat F` with

\[
|V(\widehat F)|\le2(q+r+1)\le4n.
\tag{5.3}
\]

Now return to a `{3,D}` graph `G`. For `r in {3,D}`, put `F_r=G[V_r]`, where `V_r={v:d_G(v)=r}`. Consider a segment of the original NBW that stays inside `V_r` for `ell` consecutive transitions. Conditional on the entire history up to the segment start, every specified continuation inside `V_r` has exactly the same product of transition factors `1/(r-1)` as it has in the `r`-regular completion.

If the predecessor of the segment start lies outside `V_r`, then the start vertex has positive deficiency in `F_r`; choose one new neighbor in the completion to stand for that predecessor. If the predecessor already lies in `V_r`, use the actual edge. Hence the original event “this `ell`-step same-degree segment is simple and remains in `V_r`” injects weight-for-weight into the simple-NBW event in an `r`-regular graph of at most `4n` vertices. Lemma 5.1 gives the uniform conditional estimate

\[
\boxed{
\Pr(\text{simple same-degree segment of length }\ell\mid\text{past})
\le 19200\,\frac n{\ell^2}.
}
\tag{5.4}
\]

No dependence on `D` survives.

### 5.3 Switch budget: long simple paths with few switches contain a long regular block

For a path `v_0,...,v_k`, let `S` be the number of indices `t` for which `d(v_t)` and `d(v_{t+1})` are different. If `S<=s`, the degree word has at most `s+1` homogeneous blocks. For `k>=2(s+1)`, at least one block contains at least

\[
\ell\ge \frac{k}{2(s+1)}
\tag{5.5}
\]

same-degree transitions.

Expose the path until the start of the `j`-th homogeneous block. Estimate (5.4) is uniform over that stopping history and starting oriented edge. Union-bounding over at most `s+1` possible block indices gives

\[
\boxed{
\Pr(\text{path simple and }S\le s)
\le 76800\,\frac{n(s+1)^3}{k^2}.
}
\tag{5.6}
\]

This is the first half of the two-scale estimate.

### 5.4 Many degree switches are controlled by normalized high-to-low flux

For a high vertex `v in H`, write

\[
c(v)=|N(v)\cap L|.
\]

Before the first collision, a high vertex can be used as a departure vertex at most once. Conditional on arriving at a previously unvisited high vertex `v`, the probability that the next NBW step goes to `L` is

\[
\frac{c(v)-\mathbf 1_{\{\text{predecessor}\in L\}}}{D-1}
\le \frac{c(v)}{D-1}.
\tag{5.7}
\]

Let `N_HL` be the number of `H->L` transitions before the first collision (or before time `k`, whichever comes first). Summing (5.7) over distinct high vertices gives the exact first-moment bound

\[
\boxed{
\mathbb E N_{HL}\le
\sum_{v\in H}\frac{c(v)}{D-1}
=\frac{B}{D-1}=A.
}
\tag{5.8}
\]

The two kinds of degree switch alternate, so their counts differ by at most one. Consequently

\[
S\le2N_{HL}+1.
\tag{5.9}
\]

For

\[
r=\lceil s/2\rceil,
\]

`S>s` on a simple path implies `N_HL>=r`. Markov's inequality and (5.8) therefore give

\[
\boxed{
\Pr(\text{path simple and }S>s)
\le \frac{A}{r}.
}
\tag{5.10}
\]

This estimate is deliberately only first-moment. I did not claim a Poisson/Chernoff tail: adaptive visits can favor vertices with large cross degree, so a stronger tail would need a separate argument.

### 5.5 The partial theorem

Combining (5.6) and (5.10):

### Theorem 5.2 — square-root birthday bound for bounded normalized cross flux

Let `G` be a simple `n`-vertex graph all of whose degrees lie in `{3,D}`, with `D>=4`. Let `B=e(V_3,V_D)` and `A=B/(D-1)`. For every starting oriented edge, every integer `s>=1`, every `k>=2(s+1)`, and `r=ceil(s/2)`,

\[
\boxed{
\Pr(\text{length-}k\text{ NBW is simple})
\le
76800\,\frac{n(s+1)^3}{k^2}
+\frac{A}{r}.
}
\tag{5.11}
\]

In particular, for every fixed `A_0<infinity` and `epsilon>0`, choose an integer

\[
r\ge \frac{2A_0}{\epsilon},
\qquad s=2r.
\]

Then `A/r<=epsilon/2` for every graph with `A<=A_0`, and

\[
k>
\sqrt{\frac{153600}{\epsilon}}\,(2r+1)^{3/2}\sqrt n
\tag{5.12}
\]

makes the first term below `epsilon/2`. Therefore every `{3,D}` family satisfying

\[
\boxed{\frac{e(V_3,V_D)}{D-1}\le A_0}
\tag{5.13}
\]

obeys the Alon–Peres `sqrt(n)` birthday law with a constant depending only on `epsilon` and `A_0`, **uniformly in the growing degree `D` and in the placement of the cross edges**.

This is a restricted theorem, not a solution of Conjecture 1.5 and not a solution of the entire `{3,D}` case selected by the stuck protocol.

---

## 6. What the run learned about the full `{3,D}` case

The previous obstruction “high degree causes a reverse multiplicity” was too coarse. The combination of Sections 3–5 gives a sharper picture.

1. **Within one degree scale**, arbitrary growing degree is harmless: the heat-bath plan proof is uniform over regular degree, and classical induced regular completion transfers this to any long same-degree block.

2. **A high-degree splice does not intrinsically lose probability mass** if the old output is retained as auxiliary state: the marked two-path tail swap is exactly weight-preserving.

3. **The unresolved two-degree regime is specifically high cross flux**

\[
A=\frac{e(V_3,V_D)}{D-1}\to\infty,
\]

where a simple trajectory may switch scales many times and no one homogeneous block is forced to be long enough for (5.4) by itself.

4. The single-plan local cardinality identity says exactly what must be carried through such a switch: one `(D-1)`-valued marker. A future proof should therefore not try another unmarked splice; it should use a marked/multi-path construction and then show the marker can be amortized across many scale switches.

Thus the simplest unresolved source-valid case has been narrowed from “all `{3,D}` graphs” to the **many-switch / unbounded-normalized-cross-flux subcase**.

---

## 7. Why the fixed metric does not move

The frozen metric `alpha_univ` is defined over every minimum-degree-three graph. Theorem 5.2 has two restrictions:

- only two degree values `{3,D}`;
- bounded `A=e(V_3,V_D)/(D-1)` for its source-scale corollary.

Therefore the honest ledger remains

`alpha_univ: 1 -> 1`.

This is the fourth consecutive unchanged source-domain run. Under the contract this is `STUCK_RECOVERY_2`, not closure and not a source-level exponent improvement.

No finite checker was built: every new statement is analytic and proved on the page. Producing an arithmetic replay would violate the 90/10 intent without certifying a finite core.

---

## 8. Prior-art qualification

The ingredients have different novelty status and must not be conflated.

- Dozier 2026 supplies the plan/excursion-reversal architecture and proves the fixed-degree regular theorem.
- Bencs et al. 2026 supply the best nearby general bounded-degree result located in the dated search and explicitly leave the full minimum-degree question open.
- Erdős–Kelly regular completion is classical and is used here as machinery.
- The present uniform-in-degree regular heat-bath corollary, marker interpretation and bounded-normalized-cross-flux `{3,D}` theorem were not found verbatim in the bounded search, but **publication novelty remains UNVERIFIED**. No negative search is treated as a priority certificate.

---

## 9. Neighbor audit budget

The latest neighboring R02 material recovered this run is still an active **OPEN / PARTIAL** I0095 stream, including a 2026-09-17 10:17Z report. It is not a complete closure/paper package. I therefore supplied no second audit and made no peer-track edit.

---

## 10. Next recovery moves if G0012 remains active

Do not repeat `#1/#14/#30` next run. The next three new-method attacks should be:

- **#3 PROVE SOMETHING STRONGER:** formulate the marked two-path tail-swap as a global switching theorem in which the `(D-1)` marker is conserved across successive high/low switches, rather than treating switches independently;
- **#19 MAKE IT AN ALGORITHM:** build an explicit continuation-tree procedure that follows the marker until it either closes a collision or creates two fresh marked probes, and identify the exact potential that forces termination;
- **#26 HUNT THE SPORADIC CASE:** search analytically for the extremal high-cross-flux `{3,D}` geometry (complete bipartite-like pieces are already known not to obstruct) and determine whether many switches themselves force a birthday collision.

If the source-domain metric remains unchanged through run six, the CLOSABLE rotation rule requires a handoff/rotation rather than a seventh unchanged attack.

---

## 11. Model / scheduler / permission status

The deployment evidence remains unchanged: the exposed task-management surface has title, prompt, schedule, timing mode and enabled-state controls, but **no model selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed full-hour execution control**. GPT-6/maximum therefore remains prompt-only. This run actually identifies as GPT-5.6 Sol; reasoning is UNVERIFIED.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary, not a mathematical issue. Repository reconciliation says P26 was later editable from another authorized P/C context while other contexts denied R-series edits. Lawful remedies are an owner-authorized management context or platform/support ownership migration. Duplicate jobs and permission bypass are not valid workarounds. This run performs no scheduler change.

---

## 12. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R01
  source_id: G0012
  source: "Benjamin Dozier (2026), arXiv:2608.26321, Conjecture 1.5 (Alon-Peres)"
  metric_name: alpha_univ
  metric_before: 1
  metric_after: 1
  metric_direction: smaller_is_stronger
  movement: no
  unchanged_count_before: 3
  unchanged_count_after: 4
  stuck_state: STUCK_RECOVERY_2
  status: OPEN_PARTIAL
  tried_moves: [1, 14, 30]
  new_partial_results:
    - "Marked two-NBW tail swap preserves the exact product path weight on arbitrary irregular graphs whenever the two splice transitions are non-backtracking."
    - "Local derangement forcing loses exactly one (d-1)-valued marker; with that marker, conjugation gives a bijective state-preserving forced splice."
    - "Uniform-in-degree regular bound: P(simple length ell) <= 4800 N/ell^2 for every simple r-regular graph, all r>=3."
    - "Two-degree cross-flux theorem: for degrees {3,D}, P(simple) <= 76800 n(s+1)^3/k^2 + A/ceil(s/2), A=e(V3,VD)/(D-1). Hence bounded A gives the source sqrt(n) scale uniformly in D."
  remaining_obligation: "Handle the unbounded-normalized-cross-flux / many-switch {3,D} case via a marker-preserving multi-path switching; then remove the two-degree restriction. Full source-domain alpha_univ remains 1."
  evidence:
    - "operations/claims/G0012.md"
    - "runs/R01/20260917T0802Z_g0012_biregular_heatbath_7b4e2c19.md"
    - "artifacts/R01/20260917T0802Z_g0012_global_averaging_correction.md"
    - "runs/R01/20260917T0930Z_g0012_stuck1_local_volume_1c7e9a42.md"
    - "Dozier arXiv:2608.26321 checked 2026-09-17"
    - "Bencs et al. arXiv:2608.09729 checked 2026-09-17"
    - "Erdos-Kelly induced regular-completion criterion recovered 2026-09-17"
  audit_ids:
    G0012: NONE_REQUESTED
    neighboring_R02: NOT_COMPLETE_NO_AUDIT
  publication_novelty: UNVERIFIED
```

## 13. Delivery scope

One immutable own-track report only. No shared root, peer-track file, Gmail/email, Drive, public post, purchase, permission change, force-push or scheduler change is authorized or performed in this run.
