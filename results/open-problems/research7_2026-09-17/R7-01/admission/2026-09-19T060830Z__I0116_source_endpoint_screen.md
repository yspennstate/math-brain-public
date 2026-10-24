Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-01 source-admission screen — I0116 / SIRSN Open Problem 28

Date of source/current-status check: **2026-09-19**.

Slot: `R7-01`  
Native ID: `6aabe777361481919c9e614646464772`  
Own root: `research7_2026-09-17/R7-01/`  
State entering screen: `PENDING_ADMISSION`  
Captured fresh master immediately before this artifact: `b0568b0becdb4b5b9a4c81c24a92fb761e0ed128`.

## 1. Why this row is in the R7-01 shard

The exact canonical candidate ID is `I0116`.

```
ord('I') + ord('0') + ord('1') + ord('1') + ord('6')
= 73 + 48 + 49 + 49 + 54
= 273
273 mod 7 = 0.
```

Thus I0116 is eligible for *screening* by R7-01. The shard computation is not an ownership claim and does not by itself make the row admissible.

Current `operations/claims/I0116.md` returns 404. Under the owner protocol this is not a release and not evidence of no historical ownership. Repository code search finds no dedicated current claim or prior research report for I0116 beyond the intake copies; the absence is recorded only as a bounded-history observation.

## 2. Exact outside source and locator

**Author:** David J. Aldous.  
**Title:** *Scale-invariant random spatial networks*.  
**Year:** 2014 (Electronic Journal of Probability 19, paper no. 15); arXiv source originally posted 2012 as arXiv:1204.0817.  
**Primary source URL:** https://arxiv.org/abs/1204.0817  
**Author open-problem page:** https://www.stat.berkeley.edu/~aldous/Research/OP/sirsn.html  
**Locator:** Section 8, **Open Problem 28** in the source/intake numbering.

The repository intake record reproduces the operative statement:

> Give a construction of a SIRSN which is “visually realistic” in the sense of not looking very different from a real-world road network.

The surrounding source then turns to quantitative SIRSN statistics such as total network length and route excess, but Open Problem 28 itself does **not** specify a metric, topology, statistical test, quantitative tolerance, target road-network ensemble, data set, or falsifiable mathematical predicate for “visually realistic” / “not looking very different.”

The source framework does rigorously define a SIRSN and its scale/Euclidean invariance and finiteness axioms. The missing object here is not the SIRSN definition; it is the terminal realism criterion in the numbered problem.

## 3. Later-author/current literature check

The dated bounded check on 2026-09-19 recovered the following relevant source chain.

1. Aldous's current Berkeley open-problem page still describes Section 8 as a collection of ten open problems of different styles and says subsequent work by Wilfrid Kendall and Jonas Kahn develops Poisson-line constructions while substantial work remains.
2. Jonas Kahn, *Improper Poisson line process as SIRSN in any dimension*, Annals of Probability (2016), proves that a marked Poisson-line construction yields a SIRSN. This is important progress on the construction side but does not supply a source-defined predicate certifying “visually realistic.”
3. Searches for the exact “visually realistic” formulation mainly surface procedural/computer-graphics road-network generation work, not a theorem that turns Aldous's qualitative criterion into a mathematical yes/no endpoint.

These searches are bounded negative evidence only. They do **not** certify novelty or continued openness. The admission decision below does not rely on a claim that the problem is open; it relies on the stronger source-scope fact that the literal numbered endpoint is not mathematically specified enough to support the owner's source-level closure protocol.

## 4. Admission classification

### Classification: `PROGRAMMATIC / QUALITATIVE ENDPOINT / NOT CLOSABLE AS WRITTEN / NOT_ADMITTED`

R7-01 is instructed to prefer genuinely CLOSABLE outside problems with a counterexample, sharp constant, finite certificate, or complete short-theorem route. Open Problem 28 does not provide a source-defined mathematical criterion against which a proof or counterexample can be certified.

Any attempt to make it closable would require adding at least one non-source choice, for example:

- a feature vector of road-network statistics;
- a real-world data set or distribution;
- a distance/divergence between model and data;
- a prescribed tolerance;
- a visual-test protocol or observer distribution.

A theorem for one such choice could be interesting new work, but it would be a **new formalization**, not a complete solution of Aldous's literal Open Problem 28 under the owner's full-source closure rule. R7-01 therefore must not create `operations/claims/I0116.md` and must not spend Section-B research moves on an invented surrogate endpoint.

## 5. Source-matching metric

The owner requires a source-matching frozen mathematical quantity only after an honest source target is admitted. For I0116, the literal source supplies no quantitative realism statistic to freeze.

Therefore:

`metric = UNKNOWN/UNMEASURED`

and no replacement metric is invented. This is not zero and is not a failed research movement; research has not started because admission failed.

## 6. Adjacent shard-zero correction: I0107

For completeness of the shard cursor, the other late-I shard-zero row that can look superficially available is `I0107` (Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055, Question 4.1, pp. 53–54), asking the Peres–Tetali inequality in the source notation.

It is **not admissible**. The repository's current QUEUE/RESULTS/RFLEET reconciliation already marks I0107 as refuted/current-known. Fresh 2026-09-19 web verification recovers Florentin Münch, arXiv:2309.06493, *Ollivier curvature, Isoperimetry, concentration, and Log-Sobolev inequality*, whose abstract explicitly states that it gives a counterexample to the Peres–Tetali conjecture; Caputo–Münch–Salez (arXiv:2401.17148) gives a positive replacement under non-negative sectional curvature.

Thus the 404 at `operations/claims/I0107.md` is irrelevant: the literal source question is already **KNOWN / REFUTED IN LITERATURE**, not free open inventory.

## 7. Cumulative cursor consequence

The current root `QUEUE.md` has not changed since the previously recorded September 17 queue refresh, and the I-intake has not acquired a new row. Earlier R7-01 immutable screens already disposed of the other shard-zero high-priority rows through claims/holds, source resolution, posting/known exclusions, hard/broad classification, or prior handoff. This artifact closes the remaining unformalized late-I endpoint I0116 and freshly confirms the I0107 correction.

No new source crosses all of:

1. exact shard 0;
2. outside source with recoverable exact statement;
3. source-level mathematical endpoint;
4. current-status plausibility;
5. nonduplication / ownership clearance;
6. genuine CLOSABLE classification.

Accordingly R7-01 remains `PENDING_ADMISSION` after this screen.

## 8. Ledger delta for this admission screen

```yaml
admission_delta:
  slot: R7-01
  native_id: 6aabe777361481919c9e614646464772
  start_state: PENDING_ADMISSION
  end_state: PENDING_ADMISSION
  snapshot_master: b0568b0becdb4b5b9a4c81c24a92fb761e0ed128
  screened:
    I0116:
      source: David J. Aldous, Scale-invariant random spatial networks, 2014
      locator: Section 8, Open Problem 28
      shard: 0
      disposition: PROGRAMMATIC_QUALITATIVE_ENDPOINT_NOT_CLOSABLE_AS_WRITTEN
      claim_created: false
      metric: UNKNOWN_UNMEASURED
    I0107:
      source: Justin Salez, Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon, 2025
      locator: Question 4.1
      shard: 0
      disposition: KNOWN_REFUTED_IN_LITERATURE
      claim_created: false
  section_B_methods_charged: NONE_PRE_ADMISSION
  successor_metric: UNKNOWN_UNMEASURED
  successor_stagnation: NOT_STARTED
  shared_ledgers_edited: false
  peer_files_edited: false
  next_state: PENDING_ADMISSION
```
