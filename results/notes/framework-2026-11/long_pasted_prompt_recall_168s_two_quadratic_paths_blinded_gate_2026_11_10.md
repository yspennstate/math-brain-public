---
name: long_pasted_prompt_recall_168s_two_quadratic_paths_blinded_gate_2026_11_10
description: "Recall slow / minutes on a long pasted prompt? Regression gate real-prompt pass rc 124 at 900 s (28 of 32 runs 9 Oct-10 Nov)? Two quadratic paths: brain_syn stacked-lookahead rows under search, bm25_fold overlay with no arrays(). Fixed 10 Nov: 25 KB prompt 168 s -> 24.5 s; evaluator finishes 32/139 = 0.230 in 757 s (343 s resident). hit@8 fell 0.291 -> 0.230 while dark."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T08:40:14+02:00
  status: verified
  evidence: "timed in process on episode 20 (25,621 chars) before and after each fix; parity 0 differences (brain_syn: bank + 300 built texts; bm25_fold: 190 scorer calls on recall's own index objects); state/regression_gate.jsonl rows counted; evaluator run as the gate runs it rc 0"
---

Recall on a long pasted prompt took minutes, and that is what blinded the nightly regression gate's real-prompt
instrument: 28 of its 32 runs from 9 Oct to 10 Nov ended rc 124 at the 900 s cap with no summary line (count from
state/regression_gate.jsonl, key `recall_real_prompts`; the four parsed rows are 9, 11, 19 Oct and 3 Nov).

**What was slow.** The evaluator (eval_recall_real_prompts.py) replays 139 real prompts through brain.recall() in one
process. Episode 20 is a 25,621-char paste. Timed alone, in process, on 10 Nov:

| state | episode 20 | ordinary prompt |
|---|---|---|
| before | 168.2 s | about 4.5 s |
| brain_syn.py fixed | 50.9 s | |
| bm25_fold.py fixed too | 24.5 s | 4.4-4.8 s |

1. `brain_syn.expand()`: some of its rows are nothing but stacked lookaheads, `(?=.*A)(?=.*B)`, compiled with re.S
   and run with `search`. Such a row matches somewhere exactly when it matches at position 0, but `search` does not
   know that: when it fails at 0 it starts again from every later position and each start walks to the end of the
   text. Quadratic in the length: eight rows took 106 s of the one recall (and held the recall server's single
   lock for two minutes). The fix (`_stack_rows`) finds the rows of that shape by parsing the pattern and runs them
   with `match` at 0; a row of any other shape, a row without re.S and every row when the parse fails keep
   `search`. Parity: old against new `expand()` on the bank questions and 300 built texts around rows 19 and 22,
   0 differences. Switch `BRAIN_RECALL_SYN_STACK0=0` puts `search` back everywhere.
2. `bm25_fold._Overlay` had no `arrays()`, so `score()` took its per-posting branch for every term: one struct call a
   posting, a dict a term. A 25 KB prompt has 1,606 distinct terms and recall scores it five times: 14.7 million
   struct calls, 36 s. The fix adds `arrays()` (decode with `array`, drop the re-read positions, append the fresh
   documents). Parity on the index objects recall really builds: 108 texts, 190 scorer calls (185 overlay, 5
   sidecar), 0 differences, floats included; score time 112.7 s -> 68.3 s over the set.

**Files (dreaming/, mirrored byte for byte to the brain repo's 12_cognitive_architecture/dreaming).**
brain_syn.py sha256 5bb3d1f0d594d537 (backup .bak_20261110_0805, commit ffd2b9c8); bm25_fold.py a536e3867a808095
(backup .bak_20261110_0810, commit 2d8ea18b).

**After the fixes** the installed evaluator, run as the gate runs it, finishes: 139 episodes, hit@8 32/139 = 0.230,
MRR 0.1238, 757 s on a busy box. That is inside the 900 s cap by 140 s only, so the evaluator also takes
`--deadline-s` (seeded random order, same summary line over the prompts asked, plus `partial: asked a of b`) and the
gate records the partial sample - see the gate file's REAL_PROMPTS_DEADLINE_S comment.

**The number itself moved and nobody saw it.** Parsed rows: 0.278 (7 Oct), 0.293 (9 and 11 Oct), 0.291 (19 Oct),
0.230 (3 Nov), 0.230 (10 Nov). The drop of six points between 19 Oct and 3 Nov happened while the instrument was
dark. A lead, not a finding: [[compaction_nodes_crowd_bm25_top8_2026_11_09]] measured that compaction nodes in the
top 8 cost 6 of 139 on this bank.

**What is still slow on the long prompt (24.5 s):** spread_recall's `_runindex_hits` / `sync` / `_add` about 9 s,
`_seeds_from_prompt` 6.3 s, and per-call reloads of 1-2 s each that the resident server memoizes. Not fixed.

**Checked and clean:** the 388 instincts.tsv triggers (re.I only, no re.S) take 1.58 s on the same 25 KB prompt and
scale linearly; bm25.py's lookahead is anchored on tokens.

**How to find the next one of these:** time the longest real prompt alone under cProfile
(scratch `syn_extra.py`, `retime.py` pattern: `eval_recall_real_prompts._inproc_recall()` on
`max(episodes(), key=len of prompt)`). A pattern that can only match at one place run with `search`, and a per-item
struct/dict path where an array path exists beside it, are the two shapes that bit here.

What would change this: a recall path that no longer goes through brain_syn.expand or bm25_fold.score; a re-timing
of episode 20 well above 25 s means one of the two fixes was reverted or bypassed.


Method drawn from this and two sibling fixes of the same morning: [[method_measure_what_an_event_reads_before_its_logic_2026_11_10]] (measure what an event reads or spawns before reading its logic).
