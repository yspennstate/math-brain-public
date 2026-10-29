# Archive of earlier brain tests

`TESTS.md` describes the tests the paper relies on. This folder keeps the rows of earlier tests that are not in it, so
that each number can still be recomputed. Each subfolder is self-contained and has its own README.

## general-and-hard300-2026-10-04: 854 general problems and the hard 300, five and six arms

On 854 general problems no arm differs (86.2 to 86.9 percent right). On the hard 300, which ask about the store's own mathematics, the documents and recall arm leads at 96.0 percent, against 88.0 with documents alone and 62.3 with nothing; the served note alone reaches 73.7. Aggregate tables only.

## ab30-2026-09-23: thirty math tests, brain on against brain off, with every agent's tokens counted

Thirty questions (twenty proof audits and ten questions about results held in the store), each answered by one Claude
agent with the brain and one without, graded blind against keys by three graders. Four later rounds reused the design:
round 2 compared two ways of delivering the brain to headless agents, round 3 re-ran the twenty proof audits with the
checks delivered, round 4 asked research questions, and round 5a tested a change to how the store reports what it does
not hold.

| round | items | points, brain on / off | cost, brain on / off |
|---|---|---|---|
| 1 | 30 | 27 / 26 | $61.26 / $40.48 in total; median $1.68 / $0.77 a run |
| 2 | 10 | not graded (two brain arms) | $17.05 as delivered / $17.37 with the lighter delivery |
| 3 | 20 | 18 / 17 (both graders) | $30.88 / $15.66; median $1.37 / $0.56 |
| 4 | 14 | 13 / 13 | median item cost 1.81 times the control |
| 5a | 8 | 7 / 6 (6 for the earlier version of the brain) | median item cost 1.56 times the control |

Almost every answer in every round received full credit, and every difference between arms in rounds 4 and 5a was a
90-minute timeout. What these rows support is the cost of the brain and what it delivered, not a gain in accuracy: on
questions a strong model already answers, the brain made a run cost between 1.5 and 2.2 times as much. The later tests in `TESTS.md`
moved to questions whose answer has to be recalled for that reason.

`python recompute.py` derives every number above from the rows and compares it with `CLAIMS.json`; all 21 claims
match. The claims name the tables of the campaign's report, which is not included because it also carries notes about
the machine the tests ran on; every number it published is in `CLAIMS.json`. The answer keys, the graders' notes and
the raw session streams are not included either (see the folder's own README); `TREATMENT_COMMITMENTS.jsonl` holds a
hash of each counted session stream.

## open-problem-candidate-checks-2026-09-06: nine open-problem candidates with analyses and exact checks

Candidate answers to nine questions from surveys, monographs and recent papers (Hasebe and Ueda; van Handel; Hasebe, Ueda and Wang; Aldous and Fill, twice; the critical variational SPDE survey, twice; Salez; Pollett), each with a note that rederives its load-bearing steps by a second route and names the narrower versions it does not reach. Five scripts check the finite identities exactly and reject deliberately wrong variants; four need only the standard library and one needs sympy. No novelty is claimed: two of the notes point to published work that already contains the main construction.

## three-arm-house-2026-09-29: 281 recall questions, three arms

A Sonnet solver answered 281 questions about results held in the store, drawn from seven banks (proof-audit cards,
held-out statements, blind questions written from the store's own result notes, and three levels of "where is this
proved" questions). Each question was asked three times: with nothing (`nodata`), with read access to the store's
exported files (`data`), and with the files plus the recall tool and the block the math hook serves (`data_brain`).
Two graders marked each answer correct or not and a third decided the 41 disagreements.

| arm | correct of 281 | median input tokens | median turns | total cost |
|---|---|---|---|---|
| nothing | 42 | 2,985 | 1 | $2.32 |
| files | 230 | 36,017 | 7 | $13.85 |
| files + recall + served block | 252 | 7,320 | 1 | $4.45 |

Files against nothing: 190 against 2 discordant pairs (exact McNemar p = 5.9e-54). Recall on top of the files: 36
against 14 (p = 0.0026), +7.8 points on first attempts, at a fifth of the input tokens and a third of the cost of
reading the files. `REPORT_r2.txt` adds two arms run the same evening: `data_nav`, the files with one added sentence
telling the agent that computed results live in the store rather than the memory folder (29 against 22 over files
alone, p = 0.40; it gained on the bank that needs both sources and lost 10 items on another), and `data_recall`, the
files and the recall tool without the served block (32 against 21, p = 0.17). `REPORT_CONTRACT.txt` reports the
same run by cohort, with the check that the store did not change between the export and the run. The rows give
each item's id and verdict per arm; the questions and keys are not included.

## three-arm-w7-2026-10-04: 80 problems on our own mathematics, five arms

Eighty problems (50 about stored results, 10 open conjectures from the store, 20 controls that need no store) answered
by a Sonnet solver under five arms and graded blind on a 0 / 0.5 / 1 scale, with a separate flag for a false claim made
with confidence.

| arm | full credit of 80 | mean mark | confident false claims |
|---|---|---|---|
| nothing | 27 | 0.41 | 5 |
| files | 62 | 0.82 | 8 |
| files + served block + recall | 68 | 0.89 | 7 |
| served block only | 53 | 0.73 | 4 |
| files + recall | 71 | 0.92 | 9 |

Files against nothing: +43.8 points (p = 2.8e-9). The full brain against files alone: +7.5 points, not significant at
n = 80 (p = 0.29); recall on top of files +11.2 points (p = 0.064). The served block on its own, without any search,
lifted full credit from 27 to 53. It carried the right card unasked on 36 of the 60 store and conjecture problems.

## two-opus-2026-09-22: 27 results new to the store that month, Opus 5 with and without the brain

With the brain 27 of 27 correct, without it 1 (25 abstentions), 26 helped and 0 harmed, graded blind. The run also
found three questions the math hook's anchor gate refused and widened the anchors to admit them, measured against
the archive of refused prompts. Marks only; `python recompute.py` checks the table.

## w7-first-run-2026-09-23: the same 80 problems, Opus 5.5 with the brain against Opus 5.5 alone

The first run of the bank above, with two arms. With the brain 79 of 79 had full credit after adjudication, without
it 32 of 79 (47 helped, 0 harmed): 49 against 8 on stored results, 10 against 4 on the conjectures, and 20 against 20
on ordinary mathematics. Three of the keys came from store cards that were wrong or out of date, and the brain arm
answered past them; those cards are now superseded. Marks only; `python recompute.py` checks both tables.

## hook-path-ablations-2026-09-23: two selection changes to the math hook, off against on

Two changes measured on the hook's own path before they were switched on, on 218 prompts (89 results in two wordings
and 40 the store did not hold). Treating a named family as one family moved four items from silence to the right
theorem and none back (named wording 83 -> 86 of 89 served); expanding the store's acronyms changed no count on the
bank. False fires stayed at 28 of 40. Marks only; `python recompute.py` checks all four runs.

## nightly-math-gate-2026-09-11-to-10-25: six weeks of the nightly gate on one fixed bank

The math hook's marks on the same 218 prompts for each of 51 runs of the nightly gate, with the verdict of every gate
run. The unnamed form went from 66 to 72 of 89 served and the named form from 81 to 87; wrong cards on unanswerable
prompts fell from 30 to 16 of 40. Both breaches are traced to their causes. `python recompute.py` rebuilds every count.

## frontier-digest-t16-t17-2026-09-24: does the store's frontier on a program improve a research plan?

Planning agents on FEI and the quadratic-form conjecture, with and without the digest of what the store held at a
cut-off, scored by a blind judge against what the next twelve hours established. The first digest was preferred 5 of
8 but missed the on-target bar after carrying a later-refuted house claim as a theorem; the rewritten digest, which
marks house results as unrefereed and lists withdrawn ones, was preferred 7 of 8 with on-target 10 against 6.

## locate-four-arms-2026-09-25: the locate banks with the brain, with files, with both, with neither

The 130 locate questions put to Sonnet 5 four ways: the served block plus file tools (130 right), file tools alone
(100), the served block alone (129), nothing (3). Paired, both against files is 30 to 0 (p = 1.9e-9); the files arm
lost by searching the wrong place, at three times the cost. `python recompute.py` rebuilds the table.

## equal-tools-five-arms-2026-10-05: the same Python and Lean in every arm, five arms

300 problems, every arm given the same Python and Lean tools; the arms differ only in what memory they add. Tools
alone answered 299. The gaps in the other arms were mostly refused tool calls, not wrong mathematics. Aggregate
scores only, no items.

## trap-bank-four-arms-2026-09-25: superseded, unanswerable and join questions, four arms

34 questions an agent working from a changing record gets wrong in three ways: an older answer a later entry
replaced, a question the record cannot answer, and an answer split across two places. Right out of 34: brain
connected 31, records with the recall tool run by hand 31, records alone 30, nothing 10. The records decide the score;
the connection adds nothing measurable here and costs about twice as much. README only: the items are about private records.

## mathbrain-10d-landings-2026-09-24: twenty landings of the math hook in five days

The twenty packages of the 24-28 September campaign that changed the live math hook, in the order the file hashes fix:
what each changed, which files and how many lines, and the hook's counts on the fixed 218-prompt bank before each
landing. That bank held (unnamed 71 of 89 served throughout, named 86 -> 87); the changes were aimed at long prompts,
named sub-queries, accented names and caching faults. `python check.py` walks the hash chain.

## agents100-2026-09-07: 100 proof-audit items, an agent that queries the store against one that cannot

One hundred items drawn with a fixed seed from a bank of 12,193 arXiv probability results whose proofs were rewritten
as numbered steps, with one step altered in 67 of them. Ten agents per arm, same model; the only difference was whether
the agent could query the store. The design was registered in `PROTOCOL_100Q.md` before any answer was served.

| arm | full credit on the 67 flawed items | detected at all | false positives on the 33 clean |
|---|---|---|---|
| no store | 37 | 40 | 6 |
| with store | 36 | 38 | 5 |

Paired by item: -1.5 points, 95% interval -11.2 to +8.2, exact McNemar p = 1.0. The store was used (about 95 queries,
65 items marked as informed by it) and no item's unaltered step was in the store, so the null is not a delivery or
leakage failure. It is underpowered (a powered test needs 129 flawed pairs) but it had room to show a gain: the
control arm sat at 55 percent. Both arms missed the altered hypotheses almost entirely (1 of 9 with the store, 0 of 9
without). The report reads this with two earlier tests: retrieving notes about a result does not check whether a step
uses that result correctly. The per-item verdicts, the sample's item list and the per-item fault labels are not
included.

## codex-20h-audit-2026-09-07: a twenty-hour audit of the proof hook and the store's proof notes

A Codex agent re-derived two earlier results from their rows by a second code path and read every note the proof hook
can serve. The proof hook's pooled gain (63 against 53 of 74 flawed-proof pairs, p = 0.006) comes mostly from the
easier tiers; on the hard tier it is 25 against 21 of 33 (p = 0.125). Twelve stored notes were wrong or stronger than
the theorem, each shown so by a counterexample; `corrections.jsonl` holds every one before and after. The hook's
wording, its note clipping and the Lean checker (which passed `sorry` and a false axiom) were fixed; the checker's
controls are in the folder. A five-arm pilot on 12 items is reported as a pilot.

## brain-eval-2026-09-07: PLIT stage 1 rescored on the protocol's primary tiers

The overnight grader called its pooled all-tier contrast primary. The frozen protocol names tier A for Haiku and tier B for Opus. Rescored on those tiers, Haiku answered 44 of 82 pairs correctly with the brain and 46 of 82 without it, and Opus answered 37 of 64 against 38 of 64. Neither result shows a benefit or a harm, and neither reached its planned pair count (120 and 146). An independent SQL count over 1,170 response rows reproduced all four figures. The folder holds the report producer, the inventory checks for 46 accepted calibration forms from 25 proofs in 13 families, and their tests. Item text, keys and snapshots are not included.

## proof-bank-gate-2026-09-06: acceptance contract for literature proof questions

A literature proof question changes one step of a published proof or leaves the proof unchanged, and generating one does not make it usable. The gate accepts an item only when it matches its full source except at the keyed step, carries canonical hashes, and has affirmative reviews from two distinct reviewers, one the author and one independent. A flawed item must also have exactly one semantic defect at that step, and no paper or proof group may cross the development, calibration and held-out splits. The folder holds the gate, its contract, two fixes to the PLIT extractor (proof-to-statement pairing and full source identity on served notes) and their tests. The tests use synthetic fixtures only; the bank, keys and reviews are not included.

## proofcheck-5h-2026-09-08: a Lean checker that certifies a named theorem, not a compiled file

The twenty-hour audit of 7 September found that the Lean checker passed a file containing `sorry` and a false axiom.
Three further cases in the old checker returned PASS when they should not: a source file missing after compilation,
a file with definitions and no theorem, and a `--target` that `--file` ignored. The candidate here issues a
certificate only when the named target exists and is a theorem, a transitive axiom receipt matches it, and a
source-review assertion is bound to the exact bytes compiled; missing, changed or ambiguous evidence fails closed.
Translation fidelity, whether the Lean statement says what the informal one says, is left open. The folder holds the
old and new checkers, the receipt and admission code, and their tests.

## proof-corpus-construction-2026-09-06: matched clean and one-step-flawed forms from literature proofs

Each reviewed source proof yields a clean form and a form with one changed step, kept in the same split, with source binaries, licence evidence, proof locations and assumptions bound by hash. The folder holds the pair builder, a source-context extractor that pins its proof extractor by SHA-256 and checks every source file against the archived download, and 20 tests on synthetic fixtures. The first accepted packet, from Tropp's 2011 matrix-martingale paper, gave ten calibration forms from five proofs; none has been evaluated. Items, keys, sources and reviews are not included.

## plit-probability-bank-2026-09-06: literature proof bank in probability, tools

The tools behind the probability literature bank: proof extraction from arXiv LaTeX, the one-step mutation operators, the pairing audit, the BM25 notes index served to the brain arm, the solver wrapper and the grader. Five of the six were rebuilt from the edit history and compile to code identical to the surviving bytecode; the sixth (extract_proofs.py) is the closest surviving copy. No items, keys, outputs or per-item notes are included. Sibling: mdlit-multidomain-bank-2026-09-06.

## mdlit-multidomain-bank-2026-09-06: literature proof bank outside probability

The sibling of the probability bank: 4,144 items (1,250 clean, 2,894 with one changed step) from 4,208 accepted proofs in 578 arXiv papers of 2026 in analysis, algebra, number theory, combinatorics, geometry, topology, logic and learning theory, built by eighteen operators over an eleven-class fault taxonomy and sealed with a Merkle root over the keys. A hand read of 201 flawed items before any verdict found 178 real defects (88.6 percent, 95 percent interval 83.4 to 92.3); a validity gate now keeps rejected items out of every sample. The folder holds the harvest, extraction, mutation, build, seal, sampling, notes and grading tools, the pre-registered four-arm protocol, the build report, the seal and the gate with its 15 tests. It holds no solver results, and the items, keys and per-item review notes are not included.

## bank10k-runner-2026-08-22: the three-arm runner

run_bank10k.py, the none / placebo / brain runner used by the bank10k tests and imported by both literature banks: stratified frozen sampling, deranged placebo notes, sterile solver calls with a transcript check, and exact-step grading. Its result is results/earlier-tests/bank10k-replication-2026-08-22. Generator, items and keys are not included.

## bank10k-replication-2026-08-22: right notes against scrambled notes, 160 paired proof audits

A replication of an 80-item test from 17 Aug on a second, difficulty-screened bank. A Haiku solver audited flawed and
clean proofs under three arms: three notes served from the brain, the same notes reassigned to the wrong items (a
placebo matched in titles and length), and no notes. The protocol was frozen before the analysis (`PROTOCOL_FROZEN.md`).

| arm | full credit on the 160 primary items | false positives on clean controls |
|---|---|---|
| brain notes | 128 (80.0%) | 1 of 40 |
| scrambled notes | 117 (73.1%) | 2 of 41 |

Brain against placebo: +6.9 points, 95% interval +0.8 to +12.9, discordant items 18 to 7, exact McNemar p = 0.043, so
the pre-registered replication succeeds. Against no notes at all (77.4%) the brain arm gains only +2.6 points (p = 0.50):
about half of the gap is the placebo pulling the solver below the no-notes arm. What the run shows is that the right
notes beat wrong ones; it does not show that an agent with the brain beats one without it. `METRIC_CARD.md` is the
one-page statement; `audit_regrade.json` holds the primary and sensitivity contrasts.

## locate-and-proof-banks-2026-09-11: questions only the store can answer, and two proof-bank reruns

Three banks whose answer is a value recorded only in the store (60 walk counts and campaign constants, 40 ledger
pages, 30 two-fact differences), run in rounds after each repair of the hook: with the store 57 of 60, 40 of 40 and
30 of 30 in the last rounds, against 3, 0 and 0 without it, and no wrong value in any round. Beside them, the 100- and
35-item proof-audit banks rerun with a Sonnet auditor on two days: 87 / 90, 32 / 31, 91 / 94 and 29 / 33 without and
with the served block, none significant. A third run of the 35 items on 22 September, with an Opus 5 auditor, read
34 / 34: the bank is at its ceiling. Verdict rows only; `python recompute.py` checks all seventeen runs.

## hard1k-ab-2026-09-12: 1,000 items, Opus 5 with and without the served block

Ledger lookups (page sums, page differences, highest page, odd source), self-avoiding-walk counts and authored proof
audits, each answered by an Opus 5 agent at maximum effort with nothing and with the block the math hook serves.
Without the brain 538 of 1,000, with it 1,000 of 1,000: 462 helped, 0 harmed (exact McNemar p = 1.7e-139), every
gain on the items whose answer is held only in the store. The walk counts, the odd-source letters and the proof
audits were at 100% in both arms. Verdict rows only; `python recompute.py` checks the table.

## graph-lane-2026-09-26: a diffusion lane over the use-grown graph, blended into recall

Personalised PageRank over a graph of 4.8 million agent touches (test sessions removed), blended into BM25 recall of
the memory notes behind one dial. On 948 reworded questions no blend beat BM25 alone (hit@1 257, MRR 0.352; the best
blend 258 and 0.352, moving 16 answers up and 73 down), and a second bank of 968 gave the same. The graph predicts
where work goes next rather than which note answers a question. Aggregate numbers only; `python best_arm.py` checks them.

## math-transport-2026-09-22: carrying results from the notes into the math store

A job that scans the working notes every 15 minutes and writes recognised results into the store as claims. Of 16,998
notes, 54 were taken and 13 queued for review. The first run wrote 54 claims that the hook could not serve (its
integrity check binds a claim to its node by exact statement, and the node body carried extra text); after the repair
the hook's reader accepted 54 of 54 and served the proved result ahead of the open-problem card. Counts only.

## proof-sense-posture-2026-09-12: rewording the proof-audit posture, and the batch size

On 103 proof-audit items (67 flawed, 36 clean), two rewordings of the posture the hook serves with proof items,
each naming the fault the auditor kept missing, against the live wording: 94, 94 and 94 correct (2 helped and 2
harmed; 5 and 5), so the live wording stayed. Five items per solver instead of fifteen: 97 against 94, 3 helped and
0 harmed (p = 0.25). Counts only.

## teams-and-vote-pilots-2026-10-08: teams, single agents and a three-member vote

Twenty items answered by four Codex arms on 8 October (brain or not, single agent or team) and three on 9 October (the
hook layer, a team whose checker verifies first), plus a three-member Claude vote. Graded with the current grader: 19,
20, 18 and 17 of 20 on 8 October, 20, 19 and 17 on 9 October, and 19 of 20 for the vote. Every contrast is one to three
items; a team cost about three times the tokens of a single agent and bought nothing measurable. Counts only.

## two-families-2026-10-10: two agents through the brain, one model family or two

Forty-eight proof audits. GPT single agents 37 (brain block) and 35 (none); GPT pairs of one model, with or without the
crux block, 35; pairs of two GPT models 36 and 35, at four to six times the tokens; a Claude single agent 42. Two
copies of one model were both wrong on the same 12 items, ten of them with the same wrong answer; Claude solved 8 of
those 12. The same solver-and-referee arrangement on open problems is summarised beside it. Counts only.

## research-bank-b12-2026-09-01: a research-grade fault bank, and notes from the store against no notes

Two tests of whether notes served from the math store help a solver find the faulty step in an argument.
Both come out null. The bank built for the second is the larger of the store's proof-audit banks.

## fresh-bank-2026-09-03: a fresh bank of plain questions, and the older audit-brief bank

Measurements of the math hook on two banks, taken on a store that grew from 4,732 to 4,895 nodes over the
evening. The later reruns in `locate-and-proof-banks-2026-09-11` compare against these numbers.

## harder-bank-and-own-facts-2026-09-05: a harder fault bank, and questions only the store can answer

Two tests run on the same evening, each under a protocol sealed before serving. One was a null at the
ceiling. The other gave the first controlled positive for the math hook.

## multidomain-bank-2026-09-06: a literature proof bank outside probability

A sealed fault-location bank built from published proofs in analysis, algebra, number theory, combinatorics,
geometry, topology, logic and learning theory. It is the sibling of the probability literature bank used in
`agents100-2026-09-07` and shares its item shape, runner and scoring rule. The bank was built, sealed and
checked for validity. Its powered comparison was never served, so it has no brain-against-control result.
The twenty proof audits in `papers/pseudo-cognitive-dynamics-2026-09-23` were drawn from it.

## hook-rewrites-2026-10-04: does the math hook survive a reworded question?

A metamorphic test of the math brain's prompt hook. Each of the 218 questions of the fresh bank (178 whose
answer is in the store, 40 whose answer is not) was rewritten in ways that keep its meaning, and the live hook
was run on every version, 1,427 calls in all. A rewrite should not change whether the hook serves the stored
answer, and it should not make the hook fire on a question the store cannot answer. The bank's questions are not
published.

## meaning-channel-probes-2026-10-04: the meaning channel inside the math hook: three probes

The math hook ranks cards by BM25 over a prefilter pool of 300 candidates. Beside it sits a meaning channel: the
question is embedded and compared by cosine with a vector for every claim in the store. Three probes asked what that
channel can and cannot do for the hook. None ran a solver; they read the store and the hook's own functions.

## answer-bearing-values-2026-10-04: answer-bearing values in recall

When a question asks for a value, recall can rank a card that only restates the question above the card that states
the answer. A scheduled diagnosis on six delivery cases found two faults behind this. On three of the six, the one-hit
cut went to a short layout or notation card that repeated the question's words, with the answer card at rank 2 every
time; the square-root length divisor in every channel and the title-phrase bonus put it there. On four of the six, the
passage served from the right card held the problem's opening rather than the closing sentence that states the result.

## hard1k-v3-six-arms-2026-10-05: a hard computation bank, six arms, and the calculator inside the brain arm

The bank hard1k_v3 holds 1,000 generated problems in 25 families over algebra, combinatorics, games, geometry,
graphs, linear algebra, number theory and probability, each at three difficulty tiers, with exact answers. The
first 300 in id order were served to every arm. Claude Sonnet solved, ten minutes a problem. Every stream was
scanned for leak markers and none was flagged. The problems and keys are not published.

## reasoning-pilots-and-house-banks-2026-10-05: reasoning pilots, house banks and hook versions v5 to v8

A series of small preregistered banks run over two days to find where documents, recall or the math brain can
help a solver that already reasons well. Every bank was frozen with its own snapshot of the store and the
documents before any arm ran, every prediction was written before the answers were read, and every solver
stream was scanned afterwards for markers of the bank, its keys or its authors. No stream in any arm touched
one. The items and keys are not published.

## query-term-weighting-2026-10-06: query term counts in the math hook: linear or binary

The math hook scores a stored card against the problem by the query terms they share. The question was whether
a term repeated in the problem should count once (binary) or once per occurrence (linear, the production
setting).

## symbol-channel-2026-10-06: which notation tokens the recall symbol channel should count

A ranking test on 328 labelled questions from seven banks, eight token sets. Dropping punctuation and the subscript
sign put the known card first on 250 questions against 237 (18 gained, 5 lost, top ten unchanged at 317); dropping digits as
well cost 26 first places. The change was reverted from the live build on 7 October after it lost four content
questions on the nightly gate's bank. Bank-level counts only.
