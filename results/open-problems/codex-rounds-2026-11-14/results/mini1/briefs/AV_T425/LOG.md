# T425 verification log

Task: “Verify: has open problem T425 been settled by the OpenAI math release?”
Start: 2026-11-14T21:16:19.897556+04:00

## Step 1 — orientation and initial access
Read working directory and compute state: ok, owner_away_open. Programs invoked with OMP_NUM_THREADS=1 and nice -n 15; nice reports setpriority: Operation not permitted. Work is tiny and single-threaded; no heavy computation planned. Two memory-limit setter attempts raised ValueError before writing; omitted the unsupported setter.
Task-specific folder-only writes override global checklist/mesh/brain writes. No git or subagents.
Web open attempted all three supplied GitHub folders; all returned Cache miss. Web searches returned a matching abstract claiming the full second Kahn–Kalai bound, repository overview and formalization.yaml entries, Plectis Atlas, and arXiv 2609.20546 and 2508.14269. These snippets are leads, not yet verified papers. GitHub connector fallback follows.

## Step 2 — source locations
GitHub read-only connector opened all three supplied folders successfully: each has README.md, build/, paper.pdf. PDF sizes respectively 382191, 619479, 387437 bytes. Read startup memory index and brain index; no external writes. Build directories and primary paper/Plectis/arXiv pages requested next.

## Step 3 — theorem lead and prior literature opened
Opened arXiv 2609.20546 (Tuan Tran; v1 17 September, v2 24 September 2026), 2508.14269 (Quentin Dubroff, Jeff Kahn, Jinyoung Park; 19 August 2025), and Plectis Atlas paper page. Atlas reproduces Theorem 1.1 with explicit constant 2048 e^50 and ordinary expectation threshold, and links Lean SecondKahnKalai plus outside audit reports. These need primary-source checks. Raw PDF web open failed unsupported application/octet-stream. GitHub build listing locates Kahn–Kalai and Seymour sources under build/source, Tachikawa under build/paper.tex and build/sections.

## Step 4 — repository and source access
GitHub connector read root README, all three build layouts, and Tachikawa paper.tex (OpenAI, September 23, 2026). Root README calls the collection raw research data and links lean/formalization.yaml and lean/docs; root docs/ request did not yield content. Sources now being saved under sources/ through apply_patch. Lean directory exists with OAI, ComparatorChallenges, docs, formalization.yaml.

## Step 5 — exact candidate statements obtained
Saved Tachikawa introduction (Theorem 1.1: symmetric algebra over F_2(q,H_1,H_2), nonprojective self-orthogonal module); Seymour introduction (Theorem 1.1: every nonempty finite oriented graph has a vertex with first out-neighborhood no larger than exact second out-neighborhood); Kahn–Kalai main file identifies author OpenAI and September 24, 2026. Both near-title candidates concern different conjectures. Saved repository history and formalization catalogue; catalogue maps SecondKahnKalai to OAI/Combinatorics/GraphThreshold/Main.lean. No matching correction appears in opened history.

## Step 6 — main paper and Lean artifacts saved
Read and saved all four Kahn–Kalai sections, main Lean module, family 176 formalization note, Comparator config and manuscript README. Web searches: OpenAI second Kahn error/proof, exact folder refutation, OpenAI arXiv 2026, SecondKahnKalai MathVet. Returned exposition/audit leads and arXiv 2611.05831 citing the claimed proof. Need inspect direct audit records, not infer acceptance from snippets.

## Step 7 — verdict saved before further checks
Wrote REPORT.md: SOLVED-CLAIMED the whole statement is claimed. Exact primary Theorem 1.1 uses min{1,2048 exp(50) p_E(n,H)(1+log_2 h)}, all n>=2 and all simple H with h>=1 and <=n vertices. Its p_E definition counts ordinary unlabelled copies and has budget 1/2; no multiplicity factor. Isolated-vertex constraints are redundant. Opened direct MathVet CSV and cert-machine JSON pages through Atlas; fetching raw records next. Opened arXiv 2209.03326 and 2611.05831.

## Step 8 — direct formal statement and external records
Saved Comparator challenge and ThresholdBounds.lean. Challenge uses Mathlib copyCount, independent Bernoulli edge weights, sInf thresholds, all H.Subgraph, and precisely the paper constants; its sorry is the challenge placeholder, while Main.lean supplies the proof. Config permits propext, Quot.sound, Classical.choice. Direct MathVet family 176 row says full and comparator-sandboxed-pass; direct cert-machine family 176 row says MATCHES and no gap. These are reports, not a local Lean rerun or specialist refereeing. Search also found acprk/openai-math-remarks R13 claiming a constant improvement, to inspect.

## Step 9 — wider follow-ups and limits
GitHub issue search repo:openai/math Kahn returned no issues. Saved primary lean/docs/173.md and 199.md: formalizations address Seymour and Tachikawa, not T425. Saved Seymour main.tex confirming OpenAI, September 23, 2026. MathVet README identifies pre-referee scope; acprk remarks README identifies AI-assisted drafts with placeholder authorship and says parameter changes depend on the original manuscript. R13 is a proposed constant improvement, not a refutation. Opened arXiv 2611.05831 full HTML for the actual discussion of the Kahn–Kalai announcement. Web searches for other candidate errors yielded follow-up leads, not a T425 refutation.

## Step 10 — detailed verification saved
Wrote VERIFY.md with exact source theorem quotations for all three candidates, parameter-by-parameter comparison, isolated-vertex and logarithm normalization checks, direct formalization evidence, and opened follow-up reports. Li–Zadik arXiv 2611.05831 authors and Section 1.1 checked directly; its announcement is not a proof verification. REPORT.md remains SOLVED-CLAIMED. Remaining: finish R13 follow-up, recommended row wording, source/search inventory, then spot check the simultaneous reduction lemma.

## Step 11 — follow-ups and row recommendation completed
Saved R13 note, README and verification; exact author is [AUTHOR NAME], date October 9, 2026. Recorded as conditional AI-assisted parameter follow-up, not independent proof confirmation. Appended bounded negative-search findings, prior literature with exact authors, access failures, and a three-sentence recommended row update to VERIFY.md. REPORT.md was already saved before spot-check work.

## Step 12 — spot check completed
Checked Lemma 3.2 Reduction, conditional on the preceding local estimates: bad-node potential, outside-label dependence, distortion application, unrolling and geometric summation, conditional spread and path recovery. No gap found in this selected lemma; no claim of whole-proof correctness. Tiny one-thread math calculations confirmed 16*128=2048, 2048*exp(50)≈1.062e25, and sum exp(-7m)=0.000912714<1/4; also checked the paper’s local-failure and inflation-product numerical slack. Latest web searches added a community catalogue lead but no opened contrary evidence.

## Step 13 — final audit
2026-11-14T21:21:44.887316+04:00
Verified all three theorem blocks byte-for-byte against saved primary TeX; REPORT.md has the required first line and three reason lines. Confirmed recommended row wording and Spot check are present. Saved SOURCES.sha256 for 28 source files. All task-created files are inside AV_T425; no git, outgoing messages, accounts, subagents, or heavy computation used. Completed T425 literature verification.
