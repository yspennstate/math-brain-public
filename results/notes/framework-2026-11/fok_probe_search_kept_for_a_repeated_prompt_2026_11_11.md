---
name: fok_probe_search_kept_for_a_repeated_prompt_2026_11_11
description: "fok_probe 650 ms per prompt? One BM25 search (280-375 ms, 1.2 s loaded) re-run on every loop prompt; since 11 Nov kept per query+index generation, hit 3.7 ms, exact 60/60"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T05:47:20+02:00
  status: verified
  evidence: "fok_memo_test.py 11 Nov 05:1x: 60/60 identical fresh/miss/hit, stale-generation and off-switch controls pass; commit 37877a6e on main equals live"
---

Question: fok_probe.py (the feeling-of-knowing hook, in-process on every content prompt) has a 650 ms median. Where does it go, and can a loop prompt skip it?

Almost all of it is one BM25 search. Timed piece by piece on the 11 Nov loop prompt (48 query words): importing the hook and bm25 about 100 ms, BM25() 8 ms, supersessions 2 ms, the search 280-375 ms of wall on nearly the same CPU, the rest under 20 ms. On the loaded box at 05:1x the same search averaged 1,206 ms over 60 of his prompt lines. A loop prompt repeats his ask word for word every few minutes in many sessions, and after the first fire _fresh_knowing keeps the hook silent on the same memory for 3 h, so most of those searches end in nothing.

Since 11 Nov 05:1x (an agent) the raw (slug, score) list is kept in <sha1 of the query>.json. The key is the full query text, topk and the live postings header (signature, n, avgdl), so a rebuilt index searches again; supersession, the thresholds and the fresh-knowing gate still run every time. Files older than 2 h go when a miss writes. No postings sidecar means no memo; BRAIN_FOK_MEMO=0 turns it off. Test on 60 of his prompt lines with a scratch memo folder: fresh, miss and hit identical on 60 of 60; a hit 3.7 ms against 1,206 ms fresh; a kept file naming another generation was not served; the off switch returns the fresh search. Backup fok_probe.py.bak_memo_20261111; mirror 12_cognitive_architecture/dreaming/fok_probe.py, commit 37877a6e.

Not measured yet: the share of live fok calls that hit. The index publishes a new generation every 12-19 min, so a loop prompt hits on roughly four of five ticks at best. What would change this: fok_probe's median in hook_profile.jsonl not falling after 05:20 on 11 Nov.

Other sites with the same shape: spread_recall.py scores a normalized query with bm.score(q, 5) on every prompt and has no memo of its own; the membrane's word step got the same memo earlier the same night (membrane_word_step_memo_on_same_ask_prompts_2026_11_11).

Related: [[membrane_word_step_memo_on_same_ask_prompts_2026_11_11]] [[prompt_wait_is_the_in_process_hook_sum_not_the_spawned_hooks_2026_11_10]] [[movie_hook_spawned_nvidia_smi_and_schtasks_inside_the_prompt_2026_11_11]]

