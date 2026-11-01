Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum.** No authenticated runtime model/effort telemetry establishes the requested GPT-6/maximum setting.

# R7-01 admission screen — F0119, exact 3-state Potts reconstruction region

Date checked: **2026-09-19 UTC**.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: `R7-01`; recovered native ID `6aabe777361481919c9e614646464772`.  
Pre-write master snapshot: `0ff23443b8929e660d775069fa40ab02ddfd4eef`.  
Previous R7-01 report creation commit: `0f3f5251537523fc9cafc0810cd17adff76e935b`.

## 1. Why this candidate is in the R7-01 shard

The exact case-sensitive identifier is `F0119`. Its character sum is

\[
\operatorname{ord}(F)+\operatorname{ord}(0)+\operatorname{ord}(1)+\operatorname{ord}(1)+\operatorname{ord}(9)
=70+48+49+49+57=273,
\]

and `273 mod 7 = 0`. Thus `F0119` is eligible for *screening* by R7-01 under the owner's initial-assignment partition. This arithmetic partition is not an ownership claim.

The current canonical-claim path `operations/claims/F0119.md` was absent when checked before this screen. Absence of a claim is not admission: source identity, current status, scope, prior attempts, and CLOSABLE shape must still pass.

## 2. Cumulative nondeduplication state

Before this screen I reread the controlling owner directive, visible-fleet record, `QUEUE.md`, `RESULTS.md`, `POSTED.md`, the campaign `INDEX.md` and `RANKING.md`, the R7 registry, the newest own checkpoint, current canonical claims, relevant F-intake records, and useful neighboring reports/history.

Path-scoped Git history for `research7_2026-09-17/R7-01/` exists, so there is no `HISTORY_GAP`. The previous own report is the E0093 report at `0f3f5251537523fc9cafc0810cd17adff76e935b`.

A compare from that report to the fresh pre-write snapshot `0ff23443b8929e660d775069fa40ab02ddfd4eef` is **120 commits ahead, 0 behind**. The changed-file set contains no mutation of `QUEUE.md`, `RESULTS.md`, `POSTED.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, or the F intake ledger. The canonical claim changes in that delta do not release a residue-zero CLOSABLE F target. Therefore there is no lawful reason to reset the cumulative screen or manufacture a READY successor.

### Previously under-documented residue-zero F rows

The exact shard arithmetic also identifies seven F rows that deserve an explicit cumulative disposition:

| ID | Exact mod-7 residue | Current disposition for R7-01 |
|---|---:|---|
| `F0013` | 0 | unavailable: canonical claim exists; substantial NM13-13 work/handoff exists |
| `F0029` | 0 | HARD: Járai Abelian-sandpile toppling exponent, substantive earlier attempt |
| `F0031` | 0 | HARD: existence of avalanche-radius exponent in low dimensions |
| `F0038` | 0 | HARD/BROAD: Brownian-web maximal-noise/factorisation problem |
| `F0099` | 0 | HARD: asymptotics of the random three-dimensional assignment problem |
| `F0119` | 0 | screened in detail below |
| `F0128` | 0 | excluded/known: intake itself marks Aldous's weighted-graph FPP weak law resolved |

This table closes an admission-cursor documentation gap; it does not assert that negative code search proves global openness or ownership freedom.

## 3. Exact outside source and source statement

**Author:** Elchanan Mossel.  
**Title:** *Survey: Information flow on trees*.  
**Year:** 2004.  
**Primary source:** `https://arxiv.org/abs/math/0406446`.  
**Locator:** Problem 1, Section 5, PDF p. 8.  
**Canonical intake ID:** `F0119`.  
**Canonical dedup key:** `mossel_info_flow_trees_2004::problem_1_three_state_potts`.

The source-level endpoint is:

> For the 3-symbol Potts model, find the values for which reconstruction is solvable on the `b`-ary tree.

The source setting, as preserved in the canonical intake, is the symmetric `q`-state channel

\[
M_{ii}=1-(q-1)\varepsilon,\qquad M_{ij}=\varepsilon\quad(i\ne j),
\]

with

\[
\lambda_2(M)=1-q\varepsilon.
\]

The root state is broadcast independently down each edge through `M`. Reconstruction is solvable when the total-variation distance between level-`n` configurations conditioned on distinct root states does **not** tend to zero. For `q=3`, the problem asks for the full parameter region in `(b,\varepsilon)` (equivalently `(b,\lambda_2)`).

The source/intake records the following bounds:

1. reconstruction is solvable if
   \[
   b\lambda_2^2>1;
   \]
2. non-reconstruction holds if
   \[
   b|\lambda_2|\le 1;
   \]
3. for the symmetric Potts channel, another non-reconstruction criterion is
   \[
   \frac{b(1-q\varepsilon)^2}{1-(q-2)\varepsilon}\le1.
   \]

These are hypotheses/bounds, not a full answer to Problem 1.

## 4. Dated later-literature/status check

Bounded current-literature searches were run on **2026-09-19 UTC** using the exact source title/problem, 3-state Potts reconstruction, binary/small-degree trees, and later reconstruction-threshold papers. Search misses are not treated as proof of openness.

### 4.1 Allan Sly — large-degree regular trees

Allan Sly, *Reconstruction for the Potts model*, Annals of Probability 39 (2011), arXiv:0811.1208, proves the first exact non-binary threshold and establishes that the Kesten–Stigum bound is the exact threshold for the 3-state Potts model on **regular trees of sufficiently large degree**. This is genuine progress on the source problem, but it does not supply the complete all-`b` region asked for by Mossel.

Primary URL: `https://arxiv.org/abs/0811.1208`.

### 4.2 Mossel–Sly–Sohn — large average degree

Elchanan Mossel, Allan Sly, and Youngtak Sohn, *Exact Phase Transitions for Stochastic Block Models and Reconstruction on Trees*, arXiv:2212.03362, prove for `q=3,4` that reconstruction is impossible below the Kesten–Stigum bound on Galton–Watson trees when the average degree is sufficiently large. Again this strongly confirms the large-degree picture but does not give Mossel Problem 1's full small-degree regular-tree parameter region.

Primary URL: `https://arxiv.org/abs/2212.03362`.

### 4.3 Small-degree computational bounds are not an exact solution

The 2011 SIAM paper *A Computational Method for Bounding the Probability of Reconstruction on Trees* develops certified recursive bounds and applies them to Potts models on small-degree trees. Such bounds are relevant evidence that the small-degree regime is nontrivial, but a bounds algorithm is not automatically a source-level exact classification for every parameter.

### 4.4 Antiferromagnetic Gibbs uniqueness is not interchangeable with reconstruction

Galanis–Goldberg–Yang (2018), *Uniqueness for the 3-State Antiferromagnetic Potts Model on the Tree*, determines the Gibbs uniqueness threshold for the antiferromagnetic 3-state Potts model on `d`-ary trees. This is closely related structure, but uniqueness of a Gibbs measure and the broadcast reconstruction/extremality endpoint in Mossel's Problem 1 are not predicates that may be silently identified without a theorem matching the precise parametrization and boundary law. I therefore do **not** use the uniqueness paper as a closure certificate for F0119.

Primary URL: `https://arxiv.org/abs/1804.03514`.

### Status conclusion from the bounded search

The positive later evidence establishes substantial large-degree resolution. I did **not** find a current source that claims the full exact 3-state reconstruction region for every regular-tree degree, especially the small-degree regime. This is **bounded negative evidence only**, not a proof that the residual problem is open worldwide.

Accordingly the correct safe status for R7-01 is:

`PARTIALLY RESOLVED IN LITERATURE / RESIDUAL SMALL-DEGREE SCOPE CURRENT-OPEN-LOOKING BUT UNVERIFIED`.

## 5. New exact admission diagnostic: the source-era binary-tree gap

The mathematical point of this screen is to freeze an exact, source-matching scalar diagnostic rather than merely repeat “small degree is hard.”

Set `q=3` and write

\[
\lambda:=\lambda_2=1-3\varepsilon.
\]

The source's stronger non-reconstruction condition becomes

\[
\frac{b\lambda^2}{1-\varepsilon}\le1.
\]

Since

\[
\varepsilon=\frac{1-\lambda}{3},
\qquad
1-\varepsilon
=1-\frac{1-\lambda}{3}
=\frac{2+\lambda}{3},
\]

we get the exact equivalent inequality

\[
3b\lambda^2\le 2+\lambda.
\]

For the binary tree `b=2`, in the ferromagnetic branch `\lambda\ge0`, this is

\[
6\lambda^2-\lambda-2\le0.
\]

The positive root is exact:

\[
\lambda_{\rm NR}
=\frac{1+\sqrt{1+48}}{12}
=\frac{1+7}{12}
=\frac23.
\]

Thus the source criterion proves non-reconstruction through `\lambda=2/3`.

The Kesten–Stigum sufficient reconstruction condition is

\[
2\lambda^2>1,
\]

so it proves reconstruction for

\[
\lambda>\frac1{\sqrt2}.
\]

Therefore the two source-era rigorous bounds leave the exact ferromagnetic interval

\[
\boxed{
\frac23<\lambda\le\frac1{\sqrt2}
}
\]

unclassified by those two criteria. Its width is the exact constant

\[
\boxed{
\Delta_2^{\rm(source)}
=\frac1{\sqrt2}-\frac23
=\frac{3\sqrt2-4}{6}
\approx0.04044011451988083.
}
\]

In the source's `\varepsilon` parametrization this same interval is

\[
\boxed{
\frac{1-1/\sqrt2}{3}
\le \varepsilon<\frac19
}
\]

with width approximately `0.013480038173293588`.

This is **not** asserted to be the exact current-literature unresolved interval: later bounds can narrow it. It is a frozen source-matching diagnostic showing concretely how much remains after the elementary source criteria at the smallest nontrivial regular-tree degree.

### Frozen admission diagnostic

`source_bound_gap_width_at_b2_ferromagnetic`

- before: `UNKNOWN/UNMEASURED`
- after: `(3*sqrt(2)-4)/6 ≈ 0.04044011451988083`

This diagnostic belongs to the admission analysis only. It is **not** inherited as the slot's successor metric because F0119 is not admitted.

## 6. Closability and admission decision

The literal source asks for a complete exact phase diagram over all 3-state Potts parameters and all `b`-ary trees. The residual small-degree problem requires control of a nonlinear distributional belief-propagation/reconstruction recursion (or an equivalent extremality/information-flow theorem) across a continuum of channel parameters. The bounded current literature found exact large-degree thresholds and small-degree bounds, not a finite certificate, isolated sharp constant with a short route, or one counterexample that would close the full source.

Therefore F0119 is classified for this worker as:

`HARD OUTSIDE / PARTIALLY RESOLVED IN LITERATURE / SMALL-DEGREE EXACT-THRESHOLD RESIDUAL / NOT_ADMITTED`.

Consequences:

- no `operations/claims/F0119.md` is created;
- R7-01 remains `PENDING_ADMISSION`;
- the slot successor metric remains `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`;
- successor stagnation remains `NOT_STARTED`;
- Section-B methods B2/B24/B11 are **not charged**, because admission never occurred;
- no closure, novelty, or worldwide-open claim is made.

## 7. Next admission frontier

The useful action next run is not to keep re-deriving F0119 bounds. Continue the exact residue-zero cursor into the remaining canonical families after a fresh claim/queue delta check, preferring a genuinely CLOSABLE outside problem. If no such source appears, perform another bounded source/status screen and preserve `PENDING_ADMISSION` rather than narrowing a hard problem into a new theorem and calling it the original source.

## 8. Ledger delta

```yaml
ledger_delta:
  worker: R7-01
  native_id: 6aabe777361481919c9e614646464772
  repository: yspennstate/math-open-problems
  branch: master
  prior_report_commit: 0f3f5251537523fc9cafc0810cd17adff76e935b
  prewrite_master: 0ff23443b8929e660d775069fa40ab02ddfd4eef
  git_delta_from_prior:
    ahead: 120
    behind: 0
  status_before: PENDING_ADMISSION
  status_after: PENDING_ADMISSION
  successor_metric:
    before: UNKNOWN/UNMEASURED
    after: UNKNOWN/UNMEASURED
    stagnation: NOT_STARTED
  candidate:
    id: F0119
    residue_mod_7: 0
    source: Elchanan_Mossel_Survey_Information_flow_on_trees_2004
    locator: Problem_1_Section_5_PDF_page_8
    dedup_key: mossel_info_flow_trees_2004::problem_1_three_state_potts
    source_scope: exact_3_state_Potts_reconstruction_region_on_b_ary_tree
    literature_status: PARTIALLY_RESOLVED_large_degree__residual_small_degree_current_open_looking_unverified
    classification: HARD_OUTSIDE
    disposition: NOT_ADMITTED
    canonical_claim_created: false
  admission_diagnostic:
    name: source_bound_gap_width_at_b2_ferromagnetic
    before: UNKNOWN/UNMEASURED
    after_exact: (3*sqrt(2)-4)/6
    after_decimal: 0.04044011451988083
    interpretation: source-era bound gap only, not asserted current exact unresolved interval
  section_b_methods_charged: []
  useful_new_result:
    - exact reduction of q=3 source nonreconstruction criterion to 3*b*lambda^2 <= 2+lambda
    - exact b=2 source-era gap lambda in (2/3,1/sqrt(2)]
    - cumulative disposition of previously under-documented residue-zero F rows
  shared_ledgers_edited: false
  peer_files_edited: false
  next_action: fresh residue-zero claim/queue delta then next bounded genuinely-CLOSABLE source admission screen
```
