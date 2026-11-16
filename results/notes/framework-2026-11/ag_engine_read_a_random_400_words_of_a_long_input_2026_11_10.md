---
name: ag_engine_read_a_random_400_words_of_a_long_input_2026_11_10
description: "AG card fires on one run and not the next on the same long input? ag_core cut an unordered set of words to 400 (list(set)[:400]); 11-16 of 25 cards missed per run; fixed 10 Nov by sorting and reading every word; ambient.json needs a re-measure"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T09:13:56+02:00
  status: provisional
  evidence: ""
---

Why did an AG card fire on one run and stay silent on the next, same input? Until 10 Nov 2026 09:12 the engine read an arbitrary 400 of a long input's words.

**The bug.** `ag_core.lex_candidates` built the set of words in the text and then took `list(toks)[:400]`. A set of strings has a different order in every Python process (hash randomisation), so on any input with more than 400 distinct words (a file write of a few thousand characters is enough) a different 400 were looked up each time. A card whose gate word fell outside the cut did not wake. It fired by chance, and the ambient-rate replay that decides which cards are too loud measured the same chance.

**Measured.** A control added to `--selftest`: 25 cards, each given its own fire example followed by 700 other distinct words. Old engine, five runs: 14, 14, 11, 16, 13 of the 25 failed, a different set each run. New engine: none, three runs.

**The fix.** `toks = sorted(toks)`, no cut. The text is already capped at 8,000 characters, so the lookup is at most a few more index queries. Live `~/.claude/agentic/ag_core.py` f9a403b81810b282 (was 2308dd60aab1a593, backup `ag_core.py.bak_tokcap_20261110`); selftest PASS, 965 cards, 2,203 checks.

**What it leaves open.** `ambient.json` (measured 10 Nov 03:14) was taken with the old engine, so long tool inputs were under-counted there and some cards may be louder than their recorded rate. Re-run `tools/ambient_rate.py` when the workstation has memory to spare (it reads about 900 sessions) before any decision on SPEAK.

**The general form.** Slicing a `set` (or a dict built from one) to cap work picks a different subset in every process. Cap after sorting, or cap the input, never the set. Related: [[a_hook_cards_examples_do_not_measure_its_ambient_rate_replay_and_hold_2026_11_10]].

