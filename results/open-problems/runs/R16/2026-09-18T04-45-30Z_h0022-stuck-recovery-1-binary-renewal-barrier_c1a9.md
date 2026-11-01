Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT / STUCK_RECOVERY_1 / THINKING-ONLY:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; the supported substantive unchanged count remains `3`; methods actually used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS**.

# R16 HARD OUTSIDE — H0022 STUCK_RECOVERY_1: the missing coefficient is a near-degenerate renewal problem, not another overlap lemma

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, Conjecture 1.5.

Source status after this recovery: **OPEN / PARTIAL METHOD PROGRESS**. This is the required thinking-only recovery. It deliberately adds **no new source theorem, no new certified coefficient, and no checker**.

## 1. Continuity, exclusions, ownership, and current-source refresh

I continued from the newest supported R16 report

`runs/R16/2026-09-18T03-58-30Z_h0022-overlap-gas-transfer-matrix_2d7a.md`

rather than restarting from the stale native Beck--Fiala title, H0021, or an older H0022 route. The canonical active ownership record remains

`operations/claims/H0022.md`,

with R16 as `ADMITTED_ACTIVE / HARD_OUTSIDE` owner.

Before this recovery I reread the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H-intake ledger, the current H0022 claim, the newest own H0022 report, and the neighboring H0023/P20 final report. The neighbor remains source-open and research-retired; its fixed-permutation path-hypergraph program ended with quenched clustering and growing-uniformity perfect-completion barriers, so I do not assume H0023 or use it as a black box.

A fresh bounded source check on 2026-09-18 again found arXiv:2608.06358v1 as the current primary H0022 source and did not locate a later source-matching proof of Conjecture 1.5. The source still proves only a sufficiently-large-constant analogue; its abstract records, in particular, universality for cycle factors of girth at least `100 log n/loglog n` at density `C log n/n` for a sufficiently large absolute `C`. This is bounded dated evidence, not a worldwide openness or novelty certificate.

The frozen metric is unchanged. For fixed `c>1`, `A_cyc(c)` is the least coefficient `A` for which R16 has a complete proof that `G(n,c log n/n)` is whp universal for every `n`-vertex cycle factor with all cycle lengths at least `A log n/loglog n`, retaining every restriction. Unknown slices remain `UNMEASURED`, not infinity. The source target is

\[
A_{\rm cyc}(1+\varepsilon)\le 1+\varepsilon
\qquad\text{for every fixed }\varepsilon>0.
\]

Before this recovery: `UNMEASURED`. After: `UNMEASURED`.

## 2. Why a recovery fires now

The three supported substantive H0022 runs did not move `A_cyc(1+epsilon)`:

1. the Hamilton-skeleton / cycle-defect run;
2. the first-moment / type-entropy and fixed-host-obstruction run;
3. the fixed-`M` overlap localization followed by the exact overlap-run gas / matching-polynomial run.

The metric therefore had three consecutive substantive non-movements. Under Section I, this invocation is not allowed to manufacture another lemma on the same route. Its job is to state the obstruction exactly, account for the failed routes, identify the simplest still-unproved case, compare with the nearest solved problem, and choose one recovery action.

## 3. (a) Exact displayed blocker

For the simplest source-relevant equal-cycle case, let `k|n`, let

\[
H=C_k^{\,n/k},
\]

let `F_0,F` be independent uniform labelled copies of `H`, and work in the fixed-edge-count host model `G(n,M)` with

\[
N={n\choose2},\qquad M\sim c\frac{\log n}{n}N,
\qquad
Q_s=\frac{(M)_s}{(N)_s}.
\]

The preceding R16 report established the exact fixed-`M` second-moment kernel

\[
W_n(j)=\frac{Q_{2n-j}}{Q_n^2}.
\]

The clean fixed-type second-moment obligation is therefore

\[
\boxed{
\mathbb E_{F}\,W_n\!\left(|E(F_0)\cap E(F)|\right)=O(1)
}
\tag{B}
\]

(or a suitably truncated/conditioned substitute strong enough to give a high-probability lower tail).

R16 does **not** know how to prove (B) in the sharp window

\[
k\asymp \frac{\log n}{\log\log n},
\qquad c=1+\varepsilon.
\]

That is the exact statement blocking the current second-moment route. Proving (B) would still not settle universality, but it would close the first genuinely unresolved equal-short-cycle factor step of this route. A proof of the source needs more; failure even to control (B) means the present route has not yet reached that later quantifier.

## 4. (b) Every H0022 route tried so far, and the precise failure

### Route 1 — one Hamilton skeleton plus closure matching

Cut one edge from every shortest cycle and place the resulting paths along a Hamilton skeleton. Complete-space symmetry gives an ideally spread closure matching, at the correct `Theta(1/(nk))` scale. But one fixed Hamilton cycle has only `k` offsets and its closure probability is exponentially too small. Using exponentially many Hamilton cycles could in principle recover the entropy balance at coefficient `A=1`, but the available Hamilton-cycle count does not give the required **quenched local equidistribution of cyclic spacings/closure matchings**. The route stopped at exactly that missing spread theorem.

### Route 2 — first moment and type entropy

For an arbitrary cycle type `lambda`, the exact first moment is enormous at the source parameters; the equal-short-cycle type is the first-moment extremal type on the relevant divisibility subsequences. This rules out a hidden first-moment counterexample among irregular cycle partitions. It does not give concentration. All types also share common host failures, so one cannot union-bound unconditional per-type failure probabilities of the strength needed for universality.

### Route 3 — ordinary `G(n,p)` second moment

If `K=|E(F_0) cap E(F)|`, the raw second-moment weight is `p^{-K}`. Ordinary `O(1)` overlaps already force the relative second moment to diverge polynomially. This is a genuine architecture failure, not a missing Chernoff estimate.

### Route 4 — condition on the edge count, `G(n,M)`

Passing to `G(n,M)` removes the largest global edge-count fluctuation. The exact kernel `W_n(K)` suppresses constant overlaps exponentially and the preceding report localized essentially all surviving weighted mass beyond `n/(log n loglog n)`. But its crude subset-count bound loses the **geometry of the common edges**; it cannot decide the natural weighted-overlap window.

### Route 5 — independent-edge overlap gas / transfer matrix

The exact run enumerator on one target factor predicts a natural activity of order `1/log n` and hence a weighted saddle

\[
K_*\asymp \frac{n}{\log n}.
\]

At that activity, almost all selected overlap edges in the surrogate are isolated one-edge runs; adjacent selected pairs are only `Theta(n/log^2 n)`. The problem is that this is precisely the precision at which the finite-population correction in `W_n(K)` also lives. Replacing the actual pair of cycle factors by independent edge indicators discards the term that can decide the sign.

### Route 6 — matching polynomial / common-matching factorial moments

The exact identity for common `j`-matchings and the matching polynomial of a cycle factor capture the leading isolated-edge overlap contribution. But they do not by themselves control how those common edges are stitched into the prescribed `k`-cycles of the second factor, nor do they include adjacent common runs at the needed `n/log^2 n` scale. Another expansion of the same matching polynomial without a completion coefficient would repeat the same loss.

### Neighboring H0023 linking-system route

This is stronger than H0022 needs. P20's final H0023 report leaves both the quenched local clustering and perfect-completion problems unresolved even for fixed endpoint permutations, followed by an all-permutation gap. Importing H0023 wholesale would therefore replace the present obstruction by a strictly stronger open obstruction.

## 5. #6 DEFORM TO A POINT YOU CAN SOLVE — the matching-only overlap deformation

The simplest deformation of the true overlap is to retain the natural saddle scale `j=Theta(n/log n)` but forbid adjacent common edges and whole common cycles. Then the common intersection is a matching of `j` edges.

For purposes of the next substantive test, contract each common edge to a rod of vertex-length `2`; every vertex outside the matching is a rod of length `1`. There are `n-j` rods of total weight `n`. To stitch those rods into `n/k` cycles of vertex-length exactly `k`, a rod ordering must hit every multiple

\[
k,2k,\ldots,n-k
\]

in its partial sums.

The resulting **binary-rod coefficient object** is the right solvable point to study next. Let

\[
F_k(z)=\sum_{s=0}^{\lfloor k/2\rfloor}{k-s\choose s}z^s.
\]

For the toy binary-rod renewal model, the canonical coefficient ratio is

\[
\mathcal R_{n,k,j}
:=
\frac{[z^j]F_k(z)^{n/k}}{{n-j\choose j}}.
\tag{R}
\]

Interpretation: the denominator counts all `1/2` rod sequences of total weight `n` with exactly `j` two-rods, while the numerator restricts to those sequences whose block sums can be cut at every multiple of `k`. I am recording (R) as the **coefficient object for the next test**, not promoting an asymptotic evaluation of it as a theorem in this thinking-only run.

This deformation is attractive for two reasons. First, it keeps the overlap scale predicted by the previous exact kernel instead of fleeing to a much easier `K=o(n/log n)` regime. Second, `F_k` is a Fibonacci/transfer-matrix polynomial, so its coefficient saddle is explicit enough to attack without inventing another high-dimensional combinatorial lemma.

## 6. #20 FIND WHY THE ALGORITHM FAILS — the missing quantity is a repeated-hit probability in a singular renewal regime

The nearest solved machinery is Kahn--Lubetzky--Wormald, *Cycle factors and renewal theory* (arXiv:1401.2707v2; CPAM 70 (2017), 289--339). Their second-moment argument also turns intersections of cycle factors into rods that must be stitched so partial sums hit multiples of `k`. Their Theorem 3 develops sharp renewal-without-replacement estimates, and the **size-biased first rod** removes a second-order `1/m` term that would otherwise accumulate across the many required hits.

This is exactly the shape needed here, but a literal citation does not close H0022. KLW's decisive application has a nondegenerate limiting rod law (heuristically geometric, with mean bounded away from one). At the H0022 fixed-`M` weighted saddle, by contrast, the previous overlap gas says that all but an `O(1/log n)` fraction of the vertex mass is in singleton rods. In generating-function language the empirical rod law tends toward the point mass at `1`; the relevant `g_n` tends to `z`. The constants/uniformity in KLW's published theorem are not stated for this **near-degenerate, n-dependent renewal law**.

That is the precise reason “apply KLW” is not yet a proof.

There is a second precision issue. The matching-only deformation has `j=Theta(n/log n)` defects spread across roughly `n/k=Theta(n loglog n/log n)` required cycle boundaries. Even a per-boundary error that looks negligible in an ordinary renewal theorem can accumulate on the `n/log^2 n` or `n loglog n/log^2 n` scale. Those are exactly the scales on which the fixed-`M` kernel and adjacent-run corrections compete. A proof must preserve that cancellation; an `exp(o(n/log n))` estimate is too crude.

So the present algorithm fails for a structural reason: it knows the leading overlap activity but not the **canonical completion coefficient** at the repeated-boundary precision that the source scale demands.

## 7. #27 SWAP THE QUANTIFIERS — stop asking for all cycle types before solving one extremal type

The source says “for every admissible cycle factor.” The current proof attempt should temporarily reverse the order of difficulty:

1. fix the first-moment extremal type `H=C_k^{n/k}`;
2. prove a fixed-type statement uniformly for `k` in the source window;
3. only then return to the `exp(O(sqrt n))` possible cycle partitions and ask for a common-host, uniform lower tail.

This is not a weakening presented as a solution; it is the smallest source-relevant case that still exercises the exact `log n/loglog n` cycle scale. If the equal-cycle fixed-type case cannot be controlled, the all-types universality quantifier is premature.

The corresponding second quantifier swap is inside the overlap sum: instead of bounding every intersection set separately by a worst-case estimate and summing afterward, first group intersections by their rod empirical law and evaluate the canonical coefficient/renewal cost of that class. KLW's method suggests that the ordering matters because second-order errors cancel only under the correct size-biased representation.

## 8. (c) What a successful proof must contain that no route so far contains

A viable continuation must put four pieces in one calculation:

1. **canonical overlap weight:** the exact `G(n,M)` kernel `W_n(j)`, not merely `(N/M)^j`;
2. **completion coefficient:** a repeated-hit/rod-stitching factor for an equal `C_k`-factor, beginning with the binary-rod object (R);
3. **second-order geometry:** a perturbation from matching-only overlap to the `Theta(n/log^2 n)` adjacent-run population, rather than discarding it;
4. **uniform error below the accumulated boundary scale:** enough precision to decide the sign after `n/k` cycle boundaries, not just a leading exponential rate.

No previous R16 route contains all four. The transfer-matrix route has (3) in a grand-canonical surrogate but not (2) for the true factor pair. The matching polynomial has the dominant isolated-edge count but not the repeated-hit completion penalty. The fixed-`M` localization has (1) but used a shape-blind tail bound.

## 9. (d) Simplest special case still unproved by R16

Take a single equal-cycle target

\[
H=C_k^{n/k},
\qquad
k\mid n,
\qquad
k=(1+\varepsilon+o(1))\frac{\log n}{\log\log n},
\]

in

\[
G\left(n,(1+\varepsilon)\frac{\log n}{n}\right).
\]

R16 does not have a complete sharp-density existence proof for this single target, let alone a uniform theorem over all allowed factor types. Within the present second-moment route, the smallest analytic subcase is narrower still: control the matching-only contribution with `j=Theta(n/log n)` via (R), before allowing adjacent common runs.

This is the special case selected for the next substantive test.

## 10. (e) Nearest solved problem and the ingredient it has that H0022 lacks

**Nearest solved analogue:** Kahn--Lubetzky--Wormald, *Cycle factors and renewal theory*, arXiv:1401.2707v2 (17 April 2014), published in *Communications on Pure and Applied Mathematics* 70 (2017), 289--339.

They solve the `k`-cycle-factor threshold in a random 3-regular graph using small-subgraph conditioning and a very sharp second moment. Their key new ingredient is a renewal-without-replacement theorem: common paths become rods, and constructing all target cycles requires a random rod ordering to hit multiples of `k`. Crucially, a size-biased first sample cancels a destructive `1/m` second-order term; their theorem tracks errors sharply enough to survive repeated hits.

**What their proof has that the current H0022 route lacks:** a validated renewal law at the actual intersection distribution, with error control uniform enough to be iterated. In H0022 the weighted rod distribution is asymptotically singular (`delta_1` plus a `Theta(1/log n)` defect density), so the KLW theorem cannot simply be quoted with its published fixed nondegenerate limiting law. The host model and eventual universality quantifier are also different.

This comparison is favorable rather than discouraging: the missing object is now a one-dimensional near-degenerate renewal/coefficient estimate, not an unspecified “better second moment.”

## 11. Recovery choice — exactly one

**Choice: PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The port is KLW's *size-biased renewal / exact intersection-stitching principle*, specialized first to the binary-rod near-degenerate law rather than importing their random-regular-graph theorem wholesale.

The next substantive run must test the port in this order:

- derive and verify the exact mapping between a matching-only common intersection and the canonical coefficient `R_{n,k,j}`;
- obtain a uniform saddle estimate for `R_{n,k,j}` when `j` is in a constant-width `n/log n` window and `k~A log n/loglog n`;
- insert that coefficient into the exact fixed-`M` kernel contribution;
- only if that closes with room, perturb to one adjacent-pair scale and see whether the `n/log^2 n` correction preserves the sign.

If the binary-rod coefficient already has the wrong sign after the fixed-`M` weight is included, this route should be abandoned immediately rather than decorated with another overlap lemma.

## 12. Fresh source/prior-art comparison, including the stale Beck--Fiala title

The active H0022 primary source remains arXiv:2608.06358v1 in the bounded search performed today; no later source-matching resolution was located.

For the stale native Beck--Fiala title, the current comparison has changed materially since Bansal--Jiang. Bansal--Jiang, arXiv:2508.03961, state `O(sqrt(t))` for `t>=log^2 n` and weaker polylogarithmic-loss bounds below that regime. On **17 September 2026**, Sankeerth Rao Karingula and Shachar Lovett posted ECCC TR26-188, *An elementary proof of the Komlos conjecture*, proving the dimension-free Komlos constant `36`. Applied to a `0/1` incidence matrix with column sparsity at most `t`, scaling columns by `1/sqrt(t)` gives the complete uniform Beck--Fiala consequence

\[
B(t,n)\le 36\sqrt t
\]

for every `t,n`. Their report explicitly says it simplifies the recent Guo--Fang--Lu proof. This is a very recent technical report, not mature refereed consensus, but it is a current primary claim of a theorem stronger than Beck--Fiala. Therefore the stale native title should not cause R16 to discard the supported H0022 handoff and restart Beck--Fiala from the pre-September baseline.

## 13. Model/scheduler-control status

The exposed task-control surface in this runtime still provides task identity, prompt/title, schedule or relative start, timing mode, and enablement, but **no binding model-family selector and no reasoning-effort selector**, and it returns no authenticated applied-model receipt. Thus GPT-6/maximum remains prompt-only here. Enforcing it would require an authorized scheduler/API product surface exposing those fields plus execution telemetry.

The historical P26 `You cannot modify this task` error is not universal: root `RESULTS.md` records a later successful P26 full update from an authorized P/C context. For any task that still returns that denial, the compliant route is the owning workspace/account context or platform support, not duplication, permission bypass, or another shadow schedule.

No scheduler state was changed in this run.

## 14. No checker in a thinking-only recovery

No finite source claim was made, and no new theorem was promoted. In compliance with the owner instruction, I did **not** create a checker merely to prove the worker ran. The next run should spend its validation budget only after the binary-renewal port produces a sign or a bound worth checking.

## 15. Next methods and hard-limit state

This run consumes **H0022 stuck recovery 1 of at most 2**.

The next substantive H0022 test uses the nonrepeating Section-B triple

- **#3 PROVE SOMETHING STRONGER:** prove the binary-rod coefficient estimate uniformly across the whole natural `j` window rather than at one saddle point;
- **#8 GO THE OTHER WAY AND DISCRETIZE:** discretize the empirical rod law by defect count and adjacent-run count so the renewal coefficient is a finite-dimensional saddle problem;
- **#30 ONE SCALE AT A TIME:** handle matching-only `Theta(n/log n)` overlap first, then the `Theta(n/log^2 n)` adjacent-run correction, then whole-cycle defects.

If that substantive test leaves `A_cyc(1+epsilon)` unchanged and the same coefficient obligation unresolved, the following invocation must be **STUCK_RECOVERY_2 / thinking-only**. There is no third recovery on H0022; a third stuck episode requires a handoff and rotation.

```yaml
ledger_delta:
  track: R16
  active_source: H0022
  source_status: OPEN
  research_status: PARTIAL
  metric: A_cyc(1+epsilon)
  before: UNMEASURED
  after: UNMEASURED
  substantive_unchanged_count_before: 3
  substantive_unchanged_count_after: 3
  run_mode: STUCK_RECOVERY_1_THINKING_ONLY
  recovery_count: 1_of_2
  methods_actual: [6, 20, 27]
  recovery_choice: PORT_NEAREST_SOLVED_TECHNIQUE
  port_source: Kahn-Lubetzky-Wormald_cycle_factors_and_renewal_theory
  exact_blocker: fixed_M_weighted_overlap_second_moment_for_equal_cycle_factor
  simplest_next_case: matching_only_binary_rod_overlap_equal_Ck_factor
  next_methods: [3, 8, 30]
  checker: NONE_BY_DESIGN
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
```
