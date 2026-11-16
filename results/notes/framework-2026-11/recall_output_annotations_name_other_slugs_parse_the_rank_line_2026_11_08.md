---
name: recall_output_annotations_name_other_slugs_parse_the_rank_line_2026_11_08
description: "Scoring brain.py recall output with a loose slug regex counts slugs named inside annotations (moved -> / supersedes) as ranked hits; parse the rank line only"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T08:07:45+02:00
  status: verified
  evidence: "IMPROVEMENT_LEDGER row 31"
---

**Trap.** `brain.py recall` prints each ranked memory on a line `  0.68 [lanes; status; ...] <slug>`, and the bracket can carry pointers to OTHER memories (`moved: ... -> <slug>`, `supersedes <slug>`). A scorer that pulls every slug-shaped string from the output (`re.finditer(r"[a-z0-9_]+_20\d\d_\d\d_\d\d")`) counts those pointers as ranked results.

**What it cost.** 8 Nov (an agent, brain loop ticks 62-66): ledger row 30 reported 12 of 120 top-5 slots held by standing-order memories and named microsoft_accounts_emptied_box3_own_store_2026_09_12 a repeat off-topic intruder. It was never ranked; it sat inside merging_catalogues' annotation. Re-parsed on the rank line: 6 of 120, two of them the right answer; target top5 22/24, not 21. Row 31 corrects rows 29-30.

**How to apply.** Parse recall output with the rank-line pattern `^\s+(\d\.\d\d)\s+\[([^\]]*)\]\s+(\S+)` (multiline), as `eval_recall_attractor.py` does, and take the last group as the slug.

Evidence: brainloop_c462/hub24_top8.json (loose) vs hub24b_top8.json (rank line); IMPROVEMENT_LEDGER row 31.


**Second time.** The same trap was recorded on 3 Nov (the supersedes tag printed old slugs first): [[recall_scorer_first_slug_reads_supersedes_tag_round_u_8_vs_9_2026_11_03]]. A scar met twice in five days is filed but not yet learned; a reflex that fires on a scorer regex over recall output is the next step.

Reflex (8 Nov 08:3x, ledger row 32): `recall_scorer_loose_slug_regex` (mode fire) now fires on a Bash or Write that runs brain.py recall and pulls slug-date names with re.finditer/findall/search, and stays silent when the script parses the rank line. The first build never fired live because the hook matches json.dumps(tool_input), which doubles every backslash; a trigger that contains backslashes has to be tested on that JSON form, not on the file text. Controls: brainloop_c462/rankreflex2_controls.json and rankreflex2_live.json.

The lane word (8 Nov 08:5x, ledger row 33): until then a row ranked by the BM25 block, or promoted to the head, printed as [weak] whenever its seed-lexical, graph and semantic components were all at or below 0.15. That was 39 of 192 top-8 rows on 24 questions, scoring 0.49 to 1.00. Such a row is a real lexical leader, not an intruder; the label now says bm25 or head. Only a row scoring under about 0.13 is a true weak tail row.
