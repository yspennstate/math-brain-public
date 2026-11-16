---
name: bm25_pruned_search_lazy_kth_bound_skips_nlargest_2026_11_11
description: "BM25 pruned search still slow on a 64-word prompt? Since 11 Nov a bound on the k-th best partial score (rises at most idf*(K1+1) per term) skips heapq.nlargest until it could matter; term rows in one IN select; k12 426->354 ms, k300 663->574, bit-identical"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T16:35:20+02:00
  status: verified
  evidence: "brain main 872db6294b78 bm25.py; 280 queries x k 5/12/40/300 zero mismatches vs the previous score_postings (scratch fok/eq3.py)"
---

Since 11 Nov 2026 the exact pruned BM25 search (`_score_pruned` in ~/.claude/dreaming/bm25.py) skips most of its per-term `heapq.nlargest`. On a 64-word prompt that call had been about a quarter of the search.

How. Phase 1 reads terms rarest first and, after each term, asks whether the k-th best partial score already beats everything the unread terms could still add. Finding the exact k-th best is O(number of touched documents) each time. But the k-th best can rise by at most idf*(K1+1) per term read, because each document gains at most that from one term (idf = log(1 + (n-df+0.5)/(df+0.5)) is always positive). So after one exact reading, `ub` = that value plus idf*(K1+1) for each term since is an upper bound. While even the bound fails the break test, the exact value would fail it too, and nlargest is skipped. The loop still breaks at the same term with the same cut, so the survivors and the final rescoring are unchanged. The skip test carries the same relative margin as the break test, widened, so float rounding in `ub` can only make it check more often, never skip wrongly. The term rows are also read with one `IN` select per 500 terms (term is the table's primary key) instead of one select per term.

Measured on the loaded workstation, 280 queries (the sessions' real orders queries, fok memo queries, 60 plain-language prompts, edge cases), call order alternated: k5 353 -> 317 ms, k12 426 -> 354, k40 468 -> 429, k300 663 -> 574 (mean). 0 mismatches at k 5/12/40/300 against the previous score_postings, bit for bit. Live md5 43277e87, brain main 872db6294b78, ledger an agent-20261111-bm25-lazy-kth-bound. Rollback: bm25.py.bak_lazyub_20261111 (md5 daca442d). Off switch for the whole pruned path: BRAIN_BM25_PRUNE=0.

Where it shows: the graph hook's orders phase (score_postings at k=300 on a long query, 238 ms median per prompt before) and every long-query caller of the word index.

How to apply elsewhere: when a loop recomputes an exact order statistic only to compare it against a threshold, keep a cheap bound on how fast the statistic can move. Recompute only when the bound says the comparison could flip. Related: [[bm25_exact_pruned_topk_four_times_faster_on_long_prompts_2026_11_11]], [[bm25_lazy_imports_save_30_ms_per_scoring_hook_2026_11_11]].

