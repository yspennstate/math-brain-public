# Top-200 list review: state and next steps

Task T-20261110-055 (his 10 Nov 05:29 order, a 10-day loop). Agent an agent. Written 10 Nov 2026 06:34.

## Where it stands

- `VERDICTS.tsv` is the per-row verdict for all 422 rows (built by `tools/build_verdicts.py` from `rows_status.tsv`
  and `verdict_overrides.tsv`). Probability: 163 keep, 35 move to the general list, 2 removed (T067, solved by others, 10 Nov 09:05: see CLOSEST.md; T004, claimed
  solved). Deep learning: 183 keep, 12 restate, 2 duplicates, 2 solved by others, 1 solved by us (T255).
- `replacements_probability.tsv` proposes 36 rows; since 10 Nov 09:05 there are 37 open probability slots (T067 left the list), so one more row is owed. Every candidate was screened
  against the titles and statements of all listed and retired rows (`candidates_probability*_screen.tsv`). The
  column `known_from_memory_to_verify` is written from memory; each row's status must be checked against the
  literature to November 2026 before it enters the list. The list's own retired rows cite results from
  mid and late 2026, so a candidate may have been settled since.
- `REVIEW_NOTES.md` is the first-pass log. Its flags on T067, T070, T076, T107, T129 and T030 were cleared on
  reading the statements: the open core of each is stated correctly and the rows stay.

## Not done

1. Verify the 36 replacement rows against the literature, then write them as full rows (statement, what is
   known, sources) in the list's format (`../top200_probability_2026_10_14/src/rows_NN.py`).
2. Deep-learning replacements: five candidates are in `replacements_dl.tsv` (chosen from the 14 of 50 screened
   topics in `candidates_dl_screen.tsv` that no row covers). Verify each against the literature, then write the
   full rows. T255, T314, T352, T303 and T363 leave.
3. Rewrite the statements of the 12 RESTATE rows (open core is in `verdict_overrides.tsv`).
4. The third list, 200 open problems in mathematics generally: `../top200_general_2026_11_10/` holds the plan,
   the 35 seeded rows and 165 candidates written from memory (10 Nov 07:20). Verify, then write the full rows.
5. Rank rows by distance to a solution and work them. `CLOSEST.md` is the starting rank, built from
   PAPER_CANDIDATES.md; frontier BOARD.md and the OPEN_PROBLEMS_200 pool are not yet read for it (not pushed yet). A solved row goes through two audits, then into the public math brain
   repository and its own public repository with the paper.
6. Write the revised `list.jsonl` and `LIST.md` only after steps 1 to 3; until then the published list is unchanged.

## Commands

    /c/Python314/python -I -X utf8 tools/build_verdicts.py rows_status.tsv verdict_overrides.tsv VERDICTS.tsv
    /c/Python314/python -I -X utf8 tools/screen_candidates.py ../top200_probability_2026_10_14/list.jsonl CANDS.tsv OUT.tsv

## 12 Nov 10:51 (an agent): steps 1-2 written, staged

The T400 replacement run (codex_local_1108/briefs/T400REP, audited in AUDIT_claude-agent_2026_11_12.md) gave 24
probability rows (23 + D30, found open on 12 Nov) and 3 deep-learning rows (H31 replaces T255, H35 replaces T314,
H12 replaces T363). They are written in the list's short-key form as T423-T449 in
../top200_probability_2026_10_14/src/rows_31.py.staged (converter: scratchpad t400_convert.py); a dry build with it
renamed gives 449 rows and passes build.py's checks. Not live: rename it in the same change that sets x= on the rows
leaving (VERDICTS.tsv: 35 probability rows to the general list, T067 and T004; T255, T314, T352, T303, T363) and
rewrites the 12 RESTATE rows from restated.jsonl. Still owed: 13 probability slots and 2 deep-learning slots.

## 12 Nov 11:02 (an agent): steps 1-3 and 6 landed

list.jsonl and LIST.md rebuilt: 187 probability rows live, 198 deep-learning rows live, 64 retired (449 ids). The 42
rows leaving carry x= (35 moved to the general list, T004 claimed, T067 T314 T352 solved by others, T255 ours, T303
T363 duplicates); the 12 RESTATE rows carry the T400 restatements (note names the audit; T283 and T361 say the scope
changed, T350 and T361 that the open part is our formulation); T423-T449 are live from rows_31.py. Before this, the
16 Oct edits made directly to list.jsonl (49 statements, 2 sources, the changed_since_audit flag on 60 rows) were
ported back into src (short key a), so a rebuild from src reproduced the published list exactly except 20 audit
records w687 wrote after the last build. Scripts: scratchpad t400_backport.py, t400_merge.py, patch_build.py.
Still owed: 13 probability rows and 2 deep-learning rows; re-audit of the 12 restated statements.

## 12 Nov 11:23 (an agent): Codex brief T400REP2 for the 15 owed rows
Running in codex_local_1108/briefs/T400REP2 (gpt-6.1-sol, normal speed, windowless, under run_one.py's memory gate). Input: the 28 screened candidates no row covers and no run has used (19 probability, 9 deep learning; six are area labels the worker must turn into one problem or drop), plus its own candidates if too few survive. Asked for 18 probability and 4 deep-learning rows verified OPEN so the best 13 and 2 can be chosen. Output: VERIFIED.tsv, rows_probability.jsonl, rows_dl.jsonl, REPORT.md. Integrate as T450 onward after an audit of its evidence, as for T400REP.
