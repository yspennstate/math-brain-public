# T115 verification log

Task: “Verify: has open problem T115 been settled by the OpenAI math release?” Received 14 November 2026; exact prompt clock time unavailable. Session directory timestamp: 21:04 local (Asia/Tbilisi).

## Step 1 — orientation and first retrieval

Read the startup memory index and compute_state.json; governor reported `ok`, `owner_away_open`. Ran only small read commands, prefixed `OMP_NUM_THREADS=1 nice -n 15`. `nice` reports `setpriority: Operation not permitted`; startup memory specifically records this macOS failure when already at nice 20. Process priority inspection is denied by the sandbox, so actual priority cannot be independently confirmed. No computation or worker processes launched.

Folder initially contained PROMPT.md, codex.log and run.pid. Current task instructions prohibit edits outside this folder; therefore no global mesh, checklist, brain recall (which logs), or memory mutations were attempted. Startup orientation used read-only access.

Web tool opened raw `paper.tex` for all three supplied folders: all returned 404. `build/paper.tex` for the average-sensitivity folder also returned 404. Opened repository root successfully; candidate GitHub folder returned cache miss. Searched `site:github.com/openai/math "Average Sensitivity"` and `"Average Sensitivity of Polynomial Threshold Functions" "2026" OpenAI`.

Search results identify the first paper's actual PDF as `main.pdf`, and advertise the uniform bound `8 d sqrt(n)`, Lean family 127, `lean/docs/127.md`, and `ComparatorChallenges/GotsmanLinial.lean`. These are discovery leads, not yet primary-source verification. Other leads include a later Research Square manuscript and several automated expositions.

## Step 2 — actual source locations

GitHub connector GET directory listings for all three candidate folders succeeded. Each contains a `build/` directory. PDF names: `main.pdf` (354487 bytes), `paper.pdf` (370807 bytes), and `power-saving-intersective-polynomial-differences.pdf` (644894 bytes), respectively. Web opening raw first PDF failed because of octet-stream content type; GitHub blob PDF wrapper opened but did not expose the paper text. Next retrieve build sources.

Opened the primary `lean/docs/127.md`: states a formalization for real multilinear polynomials of degree at most d on the n-cube, average sensitivity at most `8d sqrt(n)`, with sign(0)=1, and explicitly distinguishes exact extremizers. Opened Plectis's converted first-paper page as a discovery aid; primary source remains necessary for exact quotation.

## Step 3 — main statements and formal statement opened

Directory listings located split TeX sources. Web opened first paper's `build/main.tex` and `build/sections/01-introduction.tex`: author OpenAI, date September 25, 2026; main theorem is exactly the uniform-cube total-influence bound `I(f) <= 8 d sqrt(n)` for real multilinear degree-at-most-d polynomials, n>=1, 1<=d<=n, including zeros with sign(0)=1. Definition is the sum of single-coordinate flip probabilities, not the square-root sensitivity moment.

Web opened second paper's `build/paper.tex` and `build/sections/00-introduction.tex`: author OpenAI, same date; main theorem constructs total Boolean functions with block sensitivity exceeding any constant times maximum sensitivity squared. No threshold-degree bound occurs.

Web opened `lean/ComparatorChallenges/GotsmanLinial.lean` and `lean/OAI/Combinatorics/GotsmanLinial/Main.lean`. Comparator file has the intended quantified statement and a `sorry` placeholder; solution Main.lean separately assembles a theorem without extra grading/counting hypotheses, including a final theorem with the same name. The placeholder by itself is not evidence that the solution uses an admitted proof. Need inspect README, mapping and dependencies before describing formalisation status.

## Step 4 — saved initial verdict and comparison

GitHub connector opened third paper's actual `build/manuscript/main.tex` and `sections/introduction.tex`: author OpenAI, October 5, 2026; Theorem 1.1 is a degree-uniform power saving for polynomial-difference-free integer sets, unrelated to T115. Opened Lean README and solution Statement.lean. Wrote REPORT.md with SOLVED-CLAIMED for the whole row, and VERIFY.md with exact TeX main-theorem statements for all three candidates and parameter/quantity comparisons. Follow-up search and optional spot check remain.

## Step 5 — follow-up search, first pass

Web searches: exact first title with `OpenAI error refutation arxiv`; `GotsmanLinial OpenAI verification`; exact `A compensated coupling bound`; `Gotsman OpenAI 2026 mathematician`. Results chiefly catalogues/expositions and formal checking leads, with no specific refutation surfaced. Opened primary Comparator README and solution Model.lean. Confirmed the latter defines exactly uniform single-bit total influence, true=+1/false=−1 encoding, degree-at-most-d, and sign(0)=1. A guessed `ComparatorChallenges/solutions.json` path returned 404; use the specific challenge JSON next.

## Step 6 — comparator mapping and later leads

Opened `lean/ComparatorChallenges/GotsmanLinial.json`: solution is `OAI.Combinatorics.GotsmanLinial.Main`; permitted axioms are propext, Quot.sound and Classical.choice; release config has enable_nanoda=false. Thus challenge `sorry` is deliberate and is replaced by the solution module in comparison.

Web searches added exact compensated-coupling title; site:arxiv.org with OpenAI/sensitivity/2026; GotsmanLinial CERTIFIED; Gotsman/OpenAI with error/refutation/gap/incorrect. Opened oai-math-revised page; it links a later Research Square claim but calls its synopsis AI-generated and says the original was inaccessible to its collectors. Plectis search results link three independent Comparator run reports; retrieve original reports next. Two GitHub issue searches failed with 422 because `is:issue` was required; retry with it. No conclusion is drawn from these failed searches.

## Step 7 — primary later acknowledgement

Opened arXiv:2604.08095 itself. Its v3 is dated 26 October 2026; current title “The estimates for Boolean surface area of polynomial threshold functions”; authors exactly Fan Chang, Joseph Slote, Chun-Kai Tseng, Alexander Volberg, Haonan Zhang. The abstract explicitly says the Gotsman–Linial conjecture was recently solved by OpenAI. This is a primary later scholarly acknowledgement, not a referee report. It still studies E sqrt(s_f), so the original caution about its quantity remains valid while its revised literature discussion has changed.

Opened Plectis family 127, Gist.Science synopsis, and AI Proved What exposition. These are discovery/context sources, not independent mathematical certification. GitHub issue search `repo:openai/math is:issue "sensitivity"` succeeded: total_count=0, incomplete_results=false.

Opened first paper's actual coupling and parity-coupling sections. Optional spot-check candidate: the one-sided equal-marginal coupling lemma E(U−V)^2<=8a sigma, and its binomial specialization. REPORT.md already exists before this optional work.

## Step 8 — later paper text, original verification reports, inaccessible lead

Opened arXiv:2604.08095v3 HTML. Introduction equations (1.6) and (1.15) explicitly state AS[f]<=8d sqrt(n) and attribute it to OpenAI's September 25 manuscript. Bibliography identifies that same title and date. This is stronger than a passing abstract mention, although it is not a full proof audit or referee report.

Followed Plectis links to original pinned report files in mathvet/mathvet, carlostoledo1891/cert-machine, and nealmcb/openai-math-lean-tooling. GitHub web wrappers opened; retrieve raw rows with connector next. Research Square original article and v1 PDF both returned 403; do not cite its mathematical claim or author list as independently verified.

Opened first paper's weighted-grading and edge-recovery TeX through GitHub connector, and repository history.md. No sensitivity/Gotsman/family-127 line found in history.md. Chose the edge-recovery lemma for the single detailed spot check: it is the substantive bridge from weighted spectral energy to unweighted sensitive-edge count. No numerical experiment or Lean build is needed or run.

## Step 9 — original independent check records retrieved

Connector opened the pinned original files, not merely Atlas summaries. MathVet `challenge-status.csv` at 14c7f918cd336d0da03a02aae5a0eed4a429d4db has GotsmanLinial family 127, scope `full`, `comparator-sandboxed-pass`, closure problems 0, no shadowing, and only standard axioms; completion timestamps 8 October 2026. Carlos Toledo's `certs/openai-math-kernel.json` at 9814e4c06281e34a113ce853d7d99ccce160b750 has GotsmanLinial and a nanoda run dated 10 October; inspect the complete relevant object before summarizing. Neal McBurnett's `configs.csv` at 824beb05b35eb09eeb8c8571be7dbb61975c2e46 reports GotsmanLinial accepted on 10 October 2026, 143.007 seconds and 3.3 GiB check peak RAM; this is a reported remote run, not a program run here.

Further web searches: site:arxiv.org exact average-sensitivity/OpenAI; site:github.com/openai/math/issues Gotsman; each other candidate title with error/refutation/arxiv. No specific refutation surfaced. Search discovered later arXiv:2611.05267 discussing the unrelated polynomial-difference claim; open its primary page rather than cite a mirror.

## Step 10 — scope of the other candidates and complete check record

Read complete GotsmanLinial object in Carlos Toledo's pinned JSON: release commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, definitionHoles=0, run at 2026-10-10T14:00:12Z, exit=0, both Lean and nanoda acceptance, word CERTIFIED. The report itself explicitly distinguishes proof of the Lean challenge from fidelity to the manuscript.

Opened primary `lean/docs/132.md`: formalization covers the second paper's maximum-sensitivity/block-sensitivity separation, including a fixed exponent >2. Opened `lean/docs/182.md`: covers only the square-difference-free special case, not the third candidate's full intersective-polynomial theorem. Neither changes T115's verdict.

Opened arXiv:2611.05267 primary abstract page: Steve Fan, Andrew Lott, Ákos Magyar, Máté Matolcsi, Imre Z. Ruzsa; submitted 3 November 2026. Need HTML text for its discussion before attributing any comment about OpenAI. No local computation performed.

## Step 11 — follow-ups integrated and spot check completed

Opened arXiv:2611.05267v1 HTML: introduction calls the general polynomial-difference result an OpenAI claim by a different method and compares cubic parameters. Recorded as later discussion of nonmatching candidate 3. Corrected issue/PR searches (Gotsman issues, sensitivity PRs, intersective issues) each succeeded with zero matches. Fetched first two main-theorem source files through connector as a second direct check; source blob SHAs: 16ade5e4d1fe086adc8f7ebb012b759601471af1 (candidate 1 introduction), c0130588575857a7a68e3ff2dcc016dac5026bf4 (candidate 2 introduction), e5db249b0a4de89590e048685326ea3ffe5af9ad (candidate 3 introduction).

Expanded VERIFY.md with primary later acknowledgement, the three pinned independent formal-check records, negative-search limits, inaccessible Research Square lead, and the other two candidates' Lean scopes. Replaced the recommended status with three sentences incorporating the later evidence. Updated REPORT.md's final reason accordingly.

Spot-checked the single edge-recovery lemma algebraically: verified weighted-filtration dimensions and tridiagonality; unitary phase conversion of the commutator; entry cap 1/4; distance-energy identity; far energy <= diagonal energy; ordered-edge deficits; and final factor 2. No gap found in this local lemma. Did not infer validity of the whole proof. No local Lean build or numerical computation was run.

## Step 12 — final audit

Read back REPORT.md and checked its required format: one SOLVED-CLAIMED first line, followed by three reason lines. Re-extracted all three main-theorem environments directly from the stored primary TeX fetches and compared their wording and formulas with VERIFY.md; quotations agree. Rechecked the first candidate's quantifiers and influence definition against both manuscript and Lean Model/Comparator statements. Recommended replacement has three sentences. Verified that the detailed spot check is explicitly local and that failed/inaccessible searches are not presented as evidence of absence. Removed a stale “so far” phrase. Final deliverables: REPORT.md, VERIFY.md, LOG.md, all inside this folder. No git operations, external writes, subagents, heavy computation, or local formal-proof builds were used.
