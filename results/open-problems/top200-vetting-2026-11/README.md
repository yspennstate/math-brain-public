# Vetting the list of two hundred open problems, 11-14 November 2026

The attempts in this repository draw on a working list of two hundred open problems in probability, combinatorics,
statistical physics and the mathematics of deep learning. A list like this goes stale quickly: problems get solved,
statements drift from their sources, and some entries turn out to be too vague to attack. This folder is the record
of one pass that checked every row against the literature before more work was spent on it.

## What the pass did

1. **Does the problem deserve a row?** (`DESERVE.tsv`) Each entry was scored for whether it is a recognised problem
   with a published source, or a narrow question that only looks open because nobody stated it. Borderline rows were
   settled one by one (`settle_borderline_1113.py`, `SETTLE_BORDERLINE_1113.tsv`).
2. **Is it still open?** (`LITCHECK.tsv`, `GENERAL_LITCHECK.tsv`, `DL_LITCHECK.tsv`, `FAMOUS_LITCHECK*.{tsv,md}`) The
   arXiv API was searched with queries written per problem (`q*.txt`, the `general_lit*.py` and `*_litcheck_*.sh`
   scripts). Abstracts were read wherever a title suggested a solution, and the row records the arXiv identifier that
   settled the question either way. The raw API responses are not included; the identifiers are.
3. **Does the statement match the source?** (`STATEMENT_PASS.tsv`, `PROB_STATEMENT_PASS.tsv`,
   `RESTATED_STATEMENTS.tsv`) Each statement was re-read against the paper or book it cites, and restated where the
   list had drifted.
4. **Replacements.** Rows retired as solved or unsuitable were replaced from screened candidates
   (`REPLACEMENTS_1113*.tsv`, `SCREEN_*`, `FAMOUS_CANDIDATES_1114*.tsv`), and the replacements went through the same
   three checks.
5. **Spot computations.** A few rows needed a quick numerical probe before a verdict, for example the three-point
   case of T111 (`t111_three_point/`), and short notes on two attempts sit in `attempts/`.

`STATUS_1114.tsv` is the state of the list at the end of the pass, with the date and the sources checked per row.

## Credit

Every problem on the list belongs to the mathematicians who posed it, and every verdict of "solved" belongs to the
authors of the paper that solved it; the tables give the arXiv identifiers so the credit can be followed. The pass
itself was carried out by AI agents, with each verdict recorded next to the evidence. It has not been reviewed by a
person, and a row marked "still open" means only that the searches recorded here found no solution.

## Reusing it

The scripts are small and specific to this list, but the shape carries over to any problem list: score whether each
entry deserves its place, search per entry with a written query, keep the identifier that decided the verdict, re-read
the statement against its source, and replace what is retired by candidates that pass the same checks.
