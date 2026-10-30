# AB30: the rows behind the report

Every number in REPORT.md's tables and STATUS.json can be recomputed from the files in this folder:

    python recompute.py

It prints each reported number beside the one it gets from the rows and exits 0 when all of them agree. On 28 Sep all
did, once STATUS.json's round-1 counter was corrected (it had read 11 pairs since the interim of 24 Sep; all 30 were done).

## What is here

| folder | files | what they are |
|---|---|---|
| round1 | results.jsonl | one row per run: item, arm, answer, tokens, cost, time, hook bytes; re-runs included |
| | RESULT_final.json, RESULT_final_A/B/C.json | the adjudicated grades and each blind grader's, per item and arm |
| | AGREEMENT_final.json, AUDIT.json | grader agreement; the audit of the runs |
| | TOKENS.csv, TOKENS.json, GRADER_TOKENS.jsonl | tokens per run and per grader |
| | BRAIN_CONTRIB.json, RESULT_interim_p01_11.json | what the brain delivered per run; the interim grade of pairs 1-11 |
| round2 | results.jsonl, TOKENS.* | the two brain arms of the headless-diet test; not graded against keys, the report compares their answers and cost |
| round3 | results.jsonl, RESULT_r3_A/B.json, TOKENS.*, GRADER_TOKENS.jsonl | the proof audits with the checks delivered |
| round4 | results.jsonl, RESULT_r4_final.json, REPORT_r4_final.json, AGREEMENT_r4*.json, RESULT_r4x_final.json | research questions |
| round5a | the same for round 5a | the feeling-of-knowing fix |
| . | timeout_items_grades.jsonl | the grades of the answers given on items where another arm timed out |
| . | MANIFEST.json | the sha256 and size of every file |

The counted run of an item and arm is the last row for that (id, arm) in results.jsonl. The runner appended a re-run
after a failed or session-limited attempt (DEVIATION.md items 7-9); this rule reproduces round 1's cost table exactly.

## What is not here, and why

- The raw session streams. Each carries the full context the hooks injected into the session, which includes material
  that stays on the machine. The rows above hold what the analysis uses from them.
- The graders' notes and the answer keys. The notes quote the keys, and the keys stay out of the repository so that no
  later test can be contaminated by them; timeout_items_grades.jsonl keeps each grade and the sha256 of the grades file
  it came from.
- The masked-id maps of round 1's graders were kept in a session's scratch folder and are gone; round 1's RESULT files
  already carry each grade unmasked, so nothing in the tables depends on them.

## Reading the rounds

Rounds 1 and 3 used the same twenty proof audits with a different delivery, so they are two measurements of one bank,
not forty independent tasks; the report treats each round as its own result, and so should any later use of these rows.
Almost every answer in every round received full credit, and every difference between arms in rounds 4 and 5a was a
90-minute timeout. What these rows can support is the cost of the brain and what it delivered, not a gain in accuracy.

## Claims, derivation and check

The published numbers are in CLAIMS.json, one entry per claim, each naming where it appears in REPORT.md or STATUS.json
and the rule that computes it. derive.py computes every quantity from the rows alone and writes results.json; it holds
none of the published values. check.py compares results.json with CLAIMS.json and exits 1 on any difference, a claim
nothing derives, or a derived value nothing claims; it imports nothing from derive.py. `python recompute.py` runs the
two in turn. On 28 Sep all 21 claims matched, and STATUS.json itself says 30; changing one expected value in a copy of
CLAIMS.json makes check.py fail on that claim.

Since 29 Sep check.py treats this folder as a closed package (scheduled audit fleet04/B20 r37). It first checks every file
against MANIFEST.json and compares no claim when one differs. The status counter is read from STATUS.json in this
folder, a copy of the campaign's listed in the manifest, and a claim whose source is missing or unbound fails the
check. REPORT.md is bound by the git blob id the claims were copied from (MANIFEST.json, "external"). The campaign's
own files beside the folder are reported on their own lines and decide nothing, so a copy of this folder checked
elsewhere gives the same result.

## Treatment commitments

TREATMENT_COMMITMENTS.jsonl has one row for every counted run (the last row of each item and arm): 177 rows, 60 in
round 1, 20 in round 2, 40 in round 3, 33 in round 4 and 24 in round 5a. Each gives, for that run's session stream in the
private run tree, the sha256 and size of the whole stream file and the sha256 of the hook context the session received,
with the count and UTF-8 bytes of the hook outputs per hook. The hook-context hash is taken over every
system/hook_response event in stream order as its hook_name, a tab, its output field and a newline, in UTF-8; an arm with
no hook responses carries the hash of nothing. The text itself is not released. If a stream is disclosed later, these
hashes say whether it is the one the row was counted from.

Each commitment was also checked against the row it belongs to: the stream's final result event gives the row's
num_turns and duration_ms (checked on the 170 runs whose row has them; the other 7 timed out and have no result event),
and the stream's hook output bytes per hook equal the row's hook_bytes (checked on all 177; every brain-off arm has
none). All 177 agree. Pairing each row with another item's stream of the same arm instead matched none (0 of 60 in round
1, 0 of 31 in round 4), so the check can fail. The commitments were built by tools/ab30_treatment_commitments.py, which
needs the private run tree to run.

## Per-event commitments and single disclosures

TREATMENT_EVENTS.jsonl adds one row per hook response of every counted run (3,499 rows): round, id, arm, its position in
the run, the hook's name, and the sha256 and UTF-8 size of that hook's output. Each run's row in
TREATMENT_COMMITMENTS.jsonl also carries events_root_sha256, the sha256 over one line per hook response in order
("position, tab, hook name, tab, output sha256, newline"), so the event list of a run cannot lose or reorder an entry
without its root failing. That root leaves each response's size free, so each run also carries events_root_v2_sha256,
the same with the size in the line ("position, tab, hook name, tab, bytes, tab, output sha256, newline"). The v2 roots
were added on 28 Sep by running tools/ab30_treatment_commitments.py again on the same private streams: every earlier field
of the 177 rows and the whole events file came out byte-identical, and each v2 root equals the one the events file
rebuilds.

verify_disclosure.py checks one disclosed output against all of it: saved as the exact UTF-8 text of that response's
output field, it must hash to the committed value, be as long as the committed size, and its run's list must rebuild to
both roots. `python verify_disclosure.py --files` requires both roots on every run, each 64 lowercase hex digits, rebuilds
them, and fails a run or event row that appears twice (177 runs and 3,499 events pass on 28 Sep).
tools/test_verify_disclosure.py makes one change at a time on copies and runs the checker on each: a root deleted, all
roots deleted, a malformed root, a v2 root deleted, 7 bytes moved between two responses of one hook, a repeated
commitment row, a repeated event row, and an event dropped with both roots regenerated all fail, and a real output of
round 1 verifies while the same output with its last byte changed does not. Which outputs to disclose is a decision about
private material and is not made here.

Since 28 Sep 16:5x `--files` also checks each run's own fields (fleet01/B19 R44): the stream and context digests are 64
lowercase hex digits, the byte and response counts are whole numbers, a run with no hook responses commits the empty
context, the status is "committed" with every matches_row value true, and matches_row carries exactly the keys the
generator writes for the run's counted row in roundN/results.jsonl, so a disagreeing key cannot be dropped to make the rest
read true. The hook-bytes match is redone from the public files. The stream digests and sizes bind private streams, so
the checker tests their form only and reports their values as UNVERIFIED_PRIVATE. tools/ab30_private_holder_check.py,
run by the holder of the streams, recomputes every commitment row and every event row from them and compares field by
field: on 28 Sep all 177 rows and 3,499 events were identical (PRIVATE_HOLDER_RECEIPT_2026-09-28.json, counts and hashes
only). The holder's check counts rows before keying them, so a row repeated in either file fails
it even when the two copies agree, and MATCH also needs the public check to pass on the same files;
tools/test_private_holder_check.py runs eleven altered copies of the release through it.
Every JSON line, in the public check and the holder's check alike, is read with a loader that fails an object naming a
member twice; Python's own loader keeps the last value and would let a row carry a second, hidden one. The ladder now also fails a deleted stream digest, a negative stream size, a malformed context digest, a false
matches_row value, a status declaring disagreement, an empty run with a non-empty context, a dropped matches_row key and a
changed public hook_bytes; a stream digest changed to another well-formed value passes the public check, marked
UNVERIFIED_PRIVATE, and fails the holder's recomputation.
