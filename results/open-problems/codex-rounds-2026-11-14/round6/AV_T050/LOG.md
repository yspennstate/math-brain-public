# T050 round 6 log

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — continuation received 15 November 2026, 09:46 +04.

## 1. Orientation and bounded literature update

Read rounds 3, 4, 5 REPORT.md, LOG.md and PROOF.md; rereading proofs and scripts in bounded chunks because combined tool output was truncated. Read startup memory index and compute state: status ok, owner_away_open, adequate free memory. All Python commands use OMP_NUM_THREADS=1 and nice -n 15; no subagents, git, builds, or writes outside this folder. The task-specific folder restriction excludes global brain, checklist and mesh mutations.

Web search used the exact convexity title with error/refutation/review/November, openai/math first-passage errors, and arXiv strict convexity first-passage 2026 exponential. Opened lean/docs/212.md and arXiv:2610.42124 (Scott Armstrong and Ahmed Bou-Rabee). No new solution or substantive proof assessment found. The guessed uppercase HISTORY.md URL returned 404; will use the recorded lowercase history path. Search discoveries alone are not source citations. The Lean scope still excludes strict convexity. This update search began at 09:46 and is limited to five minutes.

## 2. Selected next step

First independently rederive round 5's signed network estimate and rerun its small exact checks. Then audit only found:lem-envelope, particularly its simultaneous U' lower bound for physical competitors, as round 5 recommends. This is the next input downstream of the already checked finite-cell, common-gauge and comparison-network statements. The result will retain every necessary hypothesis and will not be presented as a proof of T050.

## 3. Update complete; earlier result holds

Within the bounded update opened fresh foundations, lean/docs/212.md and lowercase history.md through the read-only GitHub connector, saving source-foundations.tex, source-lean-scope.md and source-history.md locally. History lists no relevant repair or withdrawal. Issue search with is:issue returned total_count=0, incomplete_results=false. Initial query without that qualifier returned 422 and was corrected. No SOLVED_ELSEWHERE result. The earlier arXiv abstract still concerns rotationally invariant continuum models rather than the full T050 statement.

Read all three mathematical proofs and unique check scripts. Independently rederived the network count: four attachment intervals of at most 4 beta each and at most 4 ceil(D)+5 grid intervals of at most 5 beta each yield 16+5(4 ceil(D)+5)=20 ceil(D)+41. The route's input radius is at most D+5+20+2, below ceil(D)+30. Signed defects telescope; a physical reverse traversal is not a signed reverse comparison. The conditional round 5 claim holds.

Command: OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/AV_T050/check_network.py. Exit 0: 131225 rounding/route checks, 243 rational endpoint checks, 35721 crossing pairs, repeated occurrences and 230 signed-telescoping checks passed. Runtime 0.265 seconds, peak RSS 14.06 MiB, inherited nice 20. The nice warning reports inability to raise priority from 20; the program retained lower priority.

## 4. Envelope derivation in progress

Let e=g-P at anchors, D_i the nonnegative full-period defect, and C_i=Q_i-g_(i+1)+g_i. Then C_i=D_i-(e_(i+1)-e_i). For an occurrence x at fraction theta of its nominal period, direct substitution gives

e(x)=(1-theta)e_i+theta e_(i+1)+D(i,x)-theta D_i.

The last two terms have absolute value at most D_i, including pauses and interior-edge occurrences. A finite connected graph of prescribed anchor comparisons controls their entire error range by A=sum |delta e|, with expectation at most M kappa beta. Writing D=sum D_i over N prescribed periods, every pair of attachment errors differs by at most A+2D. Hence every physical corrected cost is at least -(A+2D), uniformly over paths and endpoints. Defining U' from the actual local infimum gives a local variable, although A and D may be nonlocal.

For exactly two natural signed center-anchor adjustments, a second algebraic expansion cancels every interpolated gauge: the adjusted objective is the physical path defect plus the two signed adjustment defects plus the difference of center-anchor errors. The same A+2D bound follows. This will be written in full, including existence and measurability of the local infimum and explicit U bounds for a fixed number of switches. A patch with an incomplete line context was rejected before mutation; corrected here.

## 5. Detailed proof and fresh theorem sources saved

Wrote PROOF.md with the complete conditional envelope argument. Careful center audit clarified the preceding provisional claim: A+2D applies when both center anchors are marked cuts. For arbitrary center occurrences, including noninteger wall-center levels, the proved bound is A+4D. The original lemma needs only an O(beta) bound, so this distinction does not create a gap in it. Both cases are stated explicitly.

For a comparison graph with M edges of expected error <=kappa beta and N covered periods, the local physical envelope has mean <=(M kappa+2N) beta; the two-center envelope has mean <=(M kappa+4N) beta, improved to 2N for marked centers. For at most k>=1 switches, the local signed-trip/switch envelope has mean <=[(2k+1)M kappa+(3k+1)N] beta. Connected anchor errors are controlled by their edge sum, while interpolation adds at most one full-period defect at either endpoint. M<=N(4b+3), and N<=m(ceil(L)+2), for a fixed coarse neighborhood Q_b. All counts are independent of microscopic occurrences.

Freshly reopened all three candidate introduction TeX files and both selected Lean statements through the read-only GitHub connector, saving them here. They still state planar exponential strict convexity, Gamma differentiability only, planar no-bigeodesics, and the unrelated univalent estimate. Reopened the improvement source to fix the meaning of signed wall-center arms. Later refreshes are source checks, not an extension of the bounded literature search.

## 6. Exact checks launched

Saved check_envelope.py. Command: OMP_NUM_THREADS=1 nice -n 15 python3 -B check_envelope.py. One standard-library process, 120 CPU-second limit, fixed small state spaces, inherited nice>=15 and OMP_NUM_THREADS=1 checked, peak RSS checked below 768 MiB. Tests include all 2187 exact interpolation configurations with pauses, a subdivided physical graph dominated in both directions, independent Dijkstra and Floyd shortest paths, signed center arms, repeated visits and negative controls. Awaiting output.

## 7. Checks passed; second derivations and attempted failures

check_envelope.py exit 0: 2187 exact interpolation configurations, 54675 ordered/reversed occurrence pairs, 441 independent Dijkstra/Floyd distances on a 21-vertex subdivided graph, 5808 physical endpoint checks, 17424 center-adjusted checks and 480 physical switch coincidences passed. Runtime 1.393 seconds, peak RSS 15.94 MiB, inherited nice 20. The total fixture defect 517/91 agrees when computed as a sum of period defects or as total road cost minus calibration increment. Largest sampled negative parts were 164/221 and 1489/476; these are toy checks, not FPP constants or claims of sharpness.

Re-derived the interpolation by expanding the gauge formula directly, independently of the slope identity. Re-derived the centered physical objective both by adding corrected arms to the endpoint objective and by telescoping calibration increments to the two centers. Every evaluated case agrees exactly. M's count has two expressions, 2N(2b+1)+N and 4bN+3N. The coefficients in U follow separately from (k+1)(A+D)+k(A+2D). The checks retain both orientations, interior-edge centers, nominal pauses at integers, repeated physical vertices, and adding positive loops.

Negative controls show why equal anchor errors do not imply equal interpolated errors, why physical reversal is not a signed reverse comparison, why different calibrations cannot be canceled at a switch, and why a per-label bound cannot control an unrestricted selected maximum. Empty feasible families give zero envelopes. PROOF.md explicitly bounds the number of repeated trips/switches and keeps all center-adjustment spans covered.

Fresh foundations, improvement, three introductions and two Lean challenges agree with round 5 after terminal-whitespace normalization. Current foundations SHA256 is c36fa30b4efe9790d8fac1f8a409353181902e33d7ae11841bcc343994a387e0; the local save has terminal blank lines normalized, so it is not claimed byte-identical to the older save. Checked that round 5's other scripts are byte-identical to the already-read round 3/4 scripts.

No mathematical check failed. The bounded update found no full solution; current work proves only the conditional local-envelope input. Next deliverables: concise standalone VERIFY.md, final REPORT.md, and a source/link/statement audit.

## 8. Deliverables complete; final check pending

Saved a standalone VERIFY.md with exact main theorem quotations for all three candidates, the Gamma theorem, clause-by-clause comparison, newly opened follow-up records, a three-sentence replacement status, and the new spot check. It distinguishes fresh evidence from inherited reports. Finalized REPORT.md with PROVED applying only to the conditional local-envelope lemma.

Added an independent hand count of the fixture defect on the original unsubdivided roads: absolute calibration increments total 24/7, net increments total 16/7, and edge-slack numerators total 3*2+5+2*6+7+8+9+12=59. Thus D=8/7+59/13=517/91, agreeing with the period and telescoping computations. Reran the script after adding this independent assertion: exit 0, all prior checks passed, 1.002 seconds and 15.06 MiB peak RSS. No further mathematical changes were needed.

The next check is found:lem-gauge-tail. Remaining hypotheses are explicit; no claim is made that this sequence of conditional lemma audits proves the full strict-convexity result.

## 9. Final audit passed

Command: OMP_NUM_THREADS=1 nice -n 15 python3 -B (small inline standard-library document/source audit). The first link scan falsely interpreted the TeX expression M[f'](r) inside a code fence as a Markdown link; excluding fenced code corrected that audit bug. No document or mathematical change was needed.

Final audit exit 0: all four theorem environments exactly match the freshly reopened primary TeX; all 14 local document links resolve; the replacement status has exactly three sentences and names the title/date; REPORT's first line has the required PROVED verdict and explicit conditional scope; all nine saved source records resolve and the saved issue-search result has total_count=0. Peak RSS 13.91 MiB.

Completed REPORT.md, VERIFY.md, PROOF.md, check_envelope.py, source-audit.json and local primary-source snapshots. The new result is the conditional simultaneous local-envelope lemma. General T050 literature status remains PARTIAL-CLAIMED. No git, subagents, builds, posts, accounts, messages or intentional writes outside this folder.

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — continuation received 15 November 2026, 09:46 +04.
