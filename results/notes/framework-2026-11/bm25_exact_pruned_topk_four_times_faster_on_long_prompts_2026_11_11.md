---
name: bm25_exact_pruned_topk_four_times_faster_on_long_prompts_2026_11_11
description: "BM25 search slow on a long prompt (400k postings, 200+ ms)? Since 11 Nov score_postings prunes exactly: rarest terms first, bound idf*(K1+1), survivors rescored the plain way, bit-identical; 213->56 ms, 2.4x under load. Off: BRAIN_BM25_PRUNE=0"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T10:37:58+02:00
  status: verified
  evidence: "brain main e9239cfb3843 bm25.py; ~90 prompts x k 5/12/40/300 zero mismatches vs the previous score_postings (eq_copy2.py)"
---

A long prompt made every BM25 search on this brain read about 400,000 postings, and most of them belonged to words like "every", "fire" and "tasks", which cannot change the top twelve. Since 11 Nov 2026, bm25.score_postings first runs an exact pruned search (`_score_pruned`), and only falls back to the plain loop when no bound helps.

How it works. A term's contribution ((idf*f)*(K1+1))/(f+norm) is always below idf*(K1+1). Terms are read rarest first. Once the k-th best partial score beats everything the unread terms could still add (with a 1e-9 margin for rounding), an untouched document is out. Each further term then adds only to the survivors, and the survivors are cut again against a rising k-th score and a shrinking remainder. When few survivors are left they are found by binary search in each word's postings (records are in increasing position order; `_rec_find` and the incremental build rely on the same). Survivors are finally rescored from scratch, every term in sorted order with the same expression, so the scores are the plain loop's doubles bit for bit, ties included.

Measured on the 10-day loop prompt (48 terms, 402,722 postings): k=12 213 -> 56 ms quiet. On about 90 real prompts with the laptop's cores all busy, k=12 went from 1,550-1,835 ms to 650-860 ms mean (2.4x), with results identical at k=5, 12, 40 and 300 (live brain main e9239cfb3843, ledger fdf7e0fbe9d2). At k=300 the gain is small (237 -> 179), since the bound bites late. The plain path also picks its top k faster: it finds the k-th value on plain floats first, then sorts only the items at or above it (89 -> 37 ms on 62,000 candidates).

Why fok_probe's memo did not help: its key holds the document count, and that moves every time a fresh memory is folded in (several times an hour). So nearly every prompt missed, and paid the full search. Keeping the memo across folds would be wrong, because idf changes with n.

Off switches: BRAIN_BM25_PRUNE=0, BRAIN_BM25_KTH=0. Rollback: ~/.claude/dreaming/bm25.py.bak_prune_20261111.

How to apply elsewhere: when a ranking needs only the top k of a sum of bounded nonnegative parts, bound the unread parts before reading them. Prove exactness by rescoring the survivors the original way, not by trusting the bound's arithmetic. Related: [[bm25_lazy_imports_save_30_ms_per_scoring_hook_2026_11_11]], [[fok_probe_search_kept_for_a_repeated_prompt_2026_11_11]], [[stop_hooks_three_faster_by_skipping_work_whose_answer_is_known_2026_11_11]].

