# Writing-brain reader tools (16 November 2026)

Seven standard-library Python tools from the writing brain's tests of 15 and 16 November 2026. Each was kept because a
rule fixed before the run held against blind readers or blind judges, or is kept as a sheet with its limits stated.
The notes that record the tests are in `results/notes/framework-2026-11/` (named below).

| file | what it does | evidence |
|---|---|---|
| `turn/verdict_read.py` | Builds one packet per reader asking a single question: list the sentences where the narrator passes a verdict on what the paragraph before has already shown. `make <text> --out <dir>`, run the readers, then `collect <dir> --targets <file>`. | `r10_verdict_reader_question_shown_2026_11_16` (listed sentences faulted by blind readers at 4.6 and 7.1 times the base rate) |
| `turn/line_read.py` | A keep-or-cut read: marks candidate sentences among controls in a chapter and asks readers to rank them; the key stays off any machine a reader runs on. | first use 16 Nov; pairs with `verdict_read.py` |
| `turn/reader_checks.py` | Eight sentence checks a machine pass misses (doubled connectives, repeated quantities, bare pointers, retold facts, default beats, handed-on nouns, the narrator's maxim, echoes across a full stop), plus `--sheet`, `--totals`, `--figures`, `--speeches`. Each count is printed beside the same count on the openings of forty published novels. | `reader_checks_vs_blind_readers_only_maxim_finds_2026_11_15` (only R7 points where readers point) |
| `turn/turn.py` | `plan`: five lines written before a scene and one cutting pass after; `draw`, `commons`, `bank`, `selftest`. | `wbab6_plan_wins_by_rule_second_reader_sees_no_gap_2026_11_16` (wins by the registered rule; one model's judges) |
| `turn/wants_sheet.py` | Counts spoken turns that ask, order or refuse, and their length. A description of a page's dialogue, not a quality check. | `wants1_ask_order_refuse_turns_do_not_separate_2026_11_16` (does not separate drafts from published openings) |
| `creative/abstract_close.py` | Flags narrated sentences with an abstract noun and no concrete one (a summing-up), and marks those in a chapter's last two paragraphs. Read a flag as "look again", never "cut". | `summing_up_flag_is_not_a_length_proxy_2026_11_16`, `draft_chapter_endings_sum_up_half_as_often_as_published_2026_11_15` |
| `creative/process_lint.py` | Flags sentences in a LaTeX paper that are about the paper or its making rather than the mathematics ("not proved here", "we took six draws", AI named in the body, "an earlier version"), outside the AI declaration and acknowledgments; also lemmas cited as theorems. `process_lint.py main.tex`, `--selftest`. | `process_lint_catches_paper_self_narration_paper_lint_misses_2026_11_16` (5 of 5 must-fix sentences from eleven audits, no flags on 8 clean papers) |

## Data

- `creative/data/noun_kinds_v2.json.gz` classes nouns as concrete or abstract from the lexicographer files of
  Open English WordNet 2025 (J. P. McCrae and the Open English WordNet contributors, CC BY 4.0), itself descended from
  Princeton WordNet (G. A. Miller, C. Fellbaum and colleagues). `abstract_close.py --build` rebuilds it from the OEWN
  XML release, located by the `OEWN_XML` environment variable.
- `turn/evidence/commons_bank.json` holds the words shared by several machine drafts of each of six judged briefs,
  used by `turn.py bank`.

## Acknowledgements

The comparison shelves (openings of forty published novels and of 387 works by authors born 1880 to 1945) are public
domain texts, mostly from Project Gutenberg and Standard Ebooks, whose volunteers transcribed and edited them. The blind-reader protocol follows the usual
practice of registered reports: the rule and its pass bar are written down before any reading is scored. The
Mantel-Haenszel stratified odds ratio used in the length check is due to N. Mantel and W. Haenszel (J. Natl. Cancer
Inst. 22 (1959) 719-748).

## Limits

The readers and judges in these tests are language models, mostly of one family, and most test texts are chapters of
one draft manuscript. Every tool here produces candidates for a writer to read, not edits to apply.
