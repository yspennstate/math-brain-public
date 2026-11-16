---
name: learned_edges_predict_later_cocitation_only_where_words_already_overlap_2026_11_10
description: "[PROVISIONAL] Do use-learned edges predict links written later (date-split)? The store's 600 s edges: only where slugs share words. SESSION co-reads: yes, also at zero word overlap - 23 pct of later co-cited old pairs vs 3.8 pct random (1 Oct, p 7e-9; holds 15 Oct, 1 Nov), but only ~10 pct of pairs are evaluable"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T18:55:00+02:00
  status: provisional
  evidence: "Downloads/career/drafts_2026-11-10/rs_implement/learned_edge_datesplit.py, datesplit_result_v2.json, datesplit_run_v2.log (an agent)"
  modified: 2026-11-10T17:11:12.153Z
---

The research statement (section 3) claims edges learned from use predict links that later memories write. The test, 10 Nov:
memories dated on or after D that cite two or more pre-D memories give positive pairs (co-cited, not already typed-linked,
hub targets with in-degree > 200 left out); negatives are random pairs from the same pool of cited memories. A pair counts as
joined when the store's edges.npz has a memory-to-memory edge (mem/memw/recalled/served mapped to the slug) with p_first one day
before D (slug dates are local time; without the margin half the Oct 1 hits, 13 of 25, came from the last day - a leak).
Typed links come from GRAPH.md (310,375 links), so no memory file is opened.

| D | joined among co-cited | among random | zero word overlap (pos / neg) | some overlap, Jaccard <= .2 |
|---|---|---|---|---|
| 1 Oct | 12/781 (1.5%) | 7/9071 (0.08%) | 1/516 vs 7/8560, p 0.37 | 7/236 vs 0/508, p 0.0003 |
| 15 Oct | 7/374 (1.9%) | 3/5056 | 1/211 vs 2/4758, p 0.12 | 5/150 vs 1/295, p 0.018 |
| 1 Nov | 4/237 (1.7%) | 1/2062 | 1/150 vs 0/1923, p 0.07 | 3/74 vs 1/136, p 0.13 |

Reading: the edges carry some signal inside the word-overlap stratum (pairs whose slugs share a word), not explained by write
date (it holds for pairs written more than 7 days apart). There is no evidence yet that use finds links the words miss, which
is the claim that matters. The bottleneck is coverage, not ranking: 18,692 memory-memory edges among 14,814 touched slugs
against 310k typed links, because a memory-memory edge needs two memory touches within the 600 s window and recalled/served
nodes are context only, never targets. Doubling coverage (served/recalled as targets, or session-level co-use) is the change to
test next; rerun this script after it, same D values, same strata.

**Same day, the coverage variant (cosession_datesplit.py, measured):** join two memories when one non-test session READ both
(mem/recalled/served; memw write-touches removed so writing two memories together does not count) before D minus a day, any
time apart; sessions touching more than 40 memories left out (300 of 1,021 sessions used: 389 the author's, 303 script, 329 test).

| D | zero word overlap: co-cited / random | p (Fisher, one-sided) |
|---|---|---|
| 1 Oct | 18/77 (23%) vs 26/691 (3.8%) | 7e-9 |
| 15 Oct | 7/33 (21%) vs 8/378 (2.1%) | 8e-5 |
| 1 Nov | 7/28 (25%) vs 9/165 (5.5%) | 0.003 |

So use DOES predict links the words miss, once the window is the session rather than 600 s - the statement's claim survives in
that form. Doubts to carry: only about 10 pct of positive pairs are evaluable (both memories read by a used session before D);
the D windows overlap so the three rows are not independent; a session that read a and b before D may be the same agent's
session that wrote the citing memory after D (true prediction, but a narrow one) - SEPARATED the same evening
(cosession_same_writer.py, writers from memw touches plus frontmatter originSessionId / claude-xxxxxxxx): of the zero-overlap
hits, 12/18 (1 Oct), 6/7, 6/7 came only from sessions other than the citing memory's writer, none only from the writer, the
rest have no recorded writer (control: 5 of 9 writer ids appear as sessions in the touch log, so a same-session hit was
detectable). POPULARITY checked 19:1x (cosession_popularity.py, popularity_result.json): co-cited pairs are more read (median
product of pre-D read-session counts 4 vs 2), but inside terciles of that product the lift holds - Mantel-Haenszel odds ratio
6.3 (1 Oct; high tercile 11/34 vs 14/164, p 7e-4), 8.9 (15 Oct), 3.8 (1 Nov, small cells). Next: make session
co-reads an edge type in the store (claim graph_store owners first) and test whether recall ranks improve.

Related: [[frontier_route_bandit_thompson_built_needs_failure_records_2026_11_10]] [[math_store_links_help_only_when_the_card_words_miss_2026_11_10]] [[the_logged_use_of_the_brain_was_mostly_test_workers_2026_09_27]]

- 23:2x co-read store as the graph arm (eval_graph_mixture.py, 544-question bank, coread_only.json): reworded held-out n 488 at mix 0.1 hit1 103 / hit5 170 / MRR .2749 (vs 0.0: 101 / 170 / .2713; up 15, down 9) - the same as the live use graph (103 / 170 / .2749; up 16, down 10). The author's 56: identical at 0.1. A co-read graph adds nothing over the live one; neither moves hit5 or hit10.
