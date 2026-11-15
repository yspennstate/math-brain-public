# T127 log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 08:25 Asia/Tbilisi (04:25 UTC tool clock).

All writes stay in this folder. No git, external messages, subagents or heavy
computation. The task-specific prohibition on writes elsewhere excludes the
global mesh, checklist and brain-writing commands. Read-only orientation uses
the brain index and compute-state file. Commands use OMP_NUM_THREADS=1 and
nice -n 15; the sandbox rejects the priority change (Operation not permitted).

## 1. Initial recheck

Read the predecessor reports and logs. Round 4 has no PROOF.md or scripts.
The original result is a Bernoulli-sleeper transience certificate, not the
one-sleeper problem. Round 4's main claim is retrieval of a claimed outside
solution, without independently checking its proof.

At 04:26 UTC, web search queries were `"frog-model-tree" "mt0-svg"` and
`frog model 3 4 ary tree recurrence transience solution 2026`.
Independently opened both raw URLs from round 4:

- https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/paper/main.tex
- https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/STATEMENTS.md

Both are accessible through the web tool. This confirms the retrieval claim.
It does not yet confirm the mathematics. The paper is 1333 source lines;
the statement map is 76 lines. The web source default excerpt budget is
200 words per page, so the local account will cite brief facts, not reproduce
large portions of these documents.

First shell inventory was accidentally too broad and produced a truncated
list of filenames. Subsequent reads use exact paths. No unrelated file
contents were used.

Chosen next checkable piece, if the outside solution cannot be confirmed:
inspect its model definitions and theorem dependencies, the specific gap
identified by round 4, before returning to a diluted comparison model.

## 2. Formal sources obtained (04:26–04:27 UTC)

The raw web URLs for Defs.lean, D3/Defs.lean, Solution.lean,
SolutionRecurrent.lean, ASSETS.md and CITATION.cff all returned cache misses.
The Zenodo URL was inaccessible. The connected GitHub read-only tools work:
`github_fetch` on the Defs.lean blob URL succeeded; `github_fetch_file`
then retrieved the other files. This removes round 4's retrieval obstruction.

The GET commits/main response identified commit
`d6b298c0100af57a8f46f8314eca8bf8f7eb4693`, dated 2026-10-04T09:08:44Z.
Re-fetched all files at this exact ref, and saved them under outside/ with
their Git blob identifiers and URLs in outside_manifest.json. These include
both independent challenge files, both target files, citation metadata,
certificate-input manifest, paper, statement map, license, and recorded
comparator/nanoda/build-time outputs. No certificates or build were run.
An accidentally unfiltered commit response produced a large truncated tool
output; the retained manifest contains only the commit and per-file metadata.

Source inspection: Defs.lean explicitly defines the product law of independent
uniform step variables, the root/non-root neighbor rule, activation and the
visit set. D3/Defs.lean defines recurrence as almost-sure infinitude of this
same visit set. Both target files use these definitions. CITATION.cff names
mt0-svg, version v2.0.0, release date 2026-10-04 and DOI
10.5281/zenodo.23121586. No personal name is inferred.

The literature check is closed at 04:27 UTC, under five minutes from start.
The outside paper asserts the full answer. Stop original-model research
under step 1. Complete only the concrete retrieval/model audit and its
artifacts, with an explicit limit: no independent Lean/certificate replay.

## 3. Archive and frozen-definition checks

Created audit_sources.py. It recomputes Git blob hashes, strips nested Lean
block comments and line comments, and compares definition text after removing
whitespace. It checks only specified definitions and four inspected source
files; it is not a Lean verifier.

First command:
`OMP_NUM_THREADS=1 nice -n 15 python3 audit_sources.py > audit_sources_output.txt 2>&1`
verified all 14 source Git blob hashes after removing one extra terminal LF
introduced by the patch-saving operation. Then it confirmed 13 definitions
in the d=4 challenge but stopped on `AssertionError: Transient` for the d=3
challenge. The d=3 challenge intentionally lacks the transience predicate.
Corrected the comparison to use its 12 shared definitions and check its
Recurrent predicate separately. No source definitions were changed.

The retrieved records are historical reports, not verification performed here.
They include earlier failed and later passing builds, and runs on internal
pre-release commit identifiers. They do not themselves establish verification
of the current pinned tree. The reported comparator peak was 8482160640 bytes
and time 1581 seconds, each exceeding the present task limit. No build,
export or binary download was attempted.

Corrected audit command, same as above, exited 0 in under one second:
```
commit: d6b298c0100af57a8f46f8314eca8bf8f7eb4693
Git blob SHA-1 checks: 14 PASS; terminal LF repairs: 0
FrogModel/Challenge.lean: 13 definitions equal after comment/whitespace removal
FrogModel/ChallengeRecurrent.lean: 12 definitions equal after comment/whitespace removal
Recurrent definition equals recurrence challenge: PASS
No sorry/axiom/native_decide in four inspected development files: PASS
Other imported modules and certificates are NOT checked by this script.
peak_RSS_bytes: 18497536
```
The command also printed the sandbox's nice denial. The four files scanned
for forbidden proof tokens exclude the challenge files, whose target
placeholders intentionally contain sorry. No assertion about all transitive
imports follows from this scan. Hashes were computed from Git's documented
blob header plus raw bytes using hashlib; no git executable was used.

## 4. Applicability proof and attempts to break it

Wrote PROOF.md checking definitions rather than assuming the README's prose
matches the formal model. Counted the fibers of the step rule: d+1 choices
per root neighbor and d choices per non-root neighbor out of d(d+1).
Independently, ignoring the unused component leaves a uniform Fin d or
Fin(d+1) variable, giving the same probabilities. Product coordinates give
independent frog paths. Induction on wake gives the usual synchronous
activation rule. The finite-active bound 2^t rules out infinitely many
visit pairs at only finitely many root times.

Checked the root convention explicitly: the formal model excludes a second
root frog, whereas a literal reading of the task can include one. The
directed path-reachability argument in PROOF.md proves that two-seed
activation is the union of the two single-seed closures, and its total
visits are bounded above by their sum. This preserves a.s. transience;
inclusion of either single-seed closure preserves a.s. recurrence.
The argument uses each frog's whole path, so shifted wake times do not
invalidate it. It does not assume independence of the two coupled systems.

Checked cases: root degree versus interior degree; no path steps before
activation; simultaneous arrivals wake one sleeper; a newly awake frog
moves only on the next step; time-zero exclusion; repeated visits by one
frog; common non-root frogs in the two root-seed comparison. No discrepancy
in the model meaning was found. This does not validate the imported proof.

Wrote SOLVED_ELSEWHERE.md and REPORT.md. The new deliverable is the pinned
formal-source archive and applicability audit, not a full-solution claim.
The previous Bernoulli computations were not rerun under the literature
stopping branch. All new files remain here, and no shared-state procedures,
git, other workers, publication or external messages were used.

Final artifact inspection at 04:31 UTC (08:31 Asia/Tbilisi) confirmed the
required verdict line and the report, proof, literature record, source
manifest, audit script and successful output. Re-read the remaining
predecessor proof/log sections for boundary and time-shift pitfalls; these
agree with the root-convention audit above. No unresolved source-identity
failure remains. Full imported-proof verification remains outstanding.
