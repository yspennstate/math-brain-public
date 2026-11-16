# Writing-brain reader tools (16 November 2026)

Twelve Python tools (standard library, with numpy for the draws in `creative_draw.py`) from the writing brain's tests of 15 and 16 November 2026. Each was kept because a
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
| `turn/numbers_sheet.py` | Lists every number in a chapter by the thing it counts, the clock times, and each number that counts four or more different things, so counts that cannot both be true sit side by side. `numbers_sheet.py chapter.md [--all]`. | `draft_numbers_repeats_openers_against_published_fiction_2026_11_16` (published openings median 1.8 counted numbers per thousand words, drafts about 9.5) |
| `creative/sentence_repeat_rate.py` | The paper repeat rule moved to prose: a long sentence sharing most of its word pairs with an earlier one in the same chapter, counted beside published novels cut to the same length. Needs the corpus catalogue (`WRITING_BRAIN_DIR`). | same note (no repeats in 2,801 draft sentences; 5 in 33,708 published; not printed on a page) |
| `creative/paragraph_openers.py` | Runs of three or more prose paragraphs opening on the same word, beside published novels. Needs the corpus catalogue. | same note (drafts 4.7 per 100 paragraphs, novels median 3.3; inside the published range) |
| `creative/creative_draw.py` | Probability used to keep a writer off the obvious. `refs` hands the writer model passages chosen to differ in manner (a style kernel, a self-repelling memory per agent, optionally an exact k-determinantal draw); `pick` keeps, among the writer's candidate next moves with its own p= guesses, the one whose surprisal is nearest the entropy (the typical set), with `--shelf` dropping stock pairings first; `spent` and `page` list the words a page repeats beyond the shelf's rate and the words that come back in three or more paragraphs. `selftest` runs controls both ways. | mixed: the k-DPP drew no more varied passages than a plain random draw on this shelf (stated in the file); a stock pairing is not where blind readers find weak lines (`stock_word_pairings_are_not_where_readers_find_weak_lines_2026_11_16`); words back in 3+ paragraphs tracked worse judge rank (`writing_recurring_business_tracks_worse_judge_rank_2026_11_14`, a hypothesis) |
| `creative/phrase_df.py` | Counts in how many literary passages of the shelf each pair of consecutive content words occurs; `build` writes the table `creative_draw.py pick --shelf` reads, `show` prints a sentence's counts. Needs the corpus catalogue. | used by `creative_draw.py`; the table is not in this repository |

`papers/` holds the paper shelf tools (harvest refereed, openly licensed arXiv papers; cut them into the moves a paper
makes; compare a paragraph with published ones making the same move). See `papers/README.md`.

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
practice of registered reports: the rule and its pass bar are written down before any reading is scored. The exact
k-determinantal draw in `creative_draw.py` uses the spectral algorithm of J. B. Hough, M. Krishnapur, Y. Peres and
B. Virag (Probab. Surv. 3 (2006) 206-229) with the k-DPP step of A. Kulesza and B. Taskar (Found. Trends Mach. Learn.
5 (2012) 123-286). The
Mantel-Haenszel stratified odds ratio used in the length check is due to N. Mantel and W. Haenszel (J. Natl. Cancer
Inst. 22 (1959) 719-748).

## Limits

The readers and judges in these tests are language models, mostly of one family, and most test texts are chapters of
one draft manuscript. Every tool here produces candidates for a writer to read, not edits to apply.
