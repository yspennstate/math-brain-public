# T050 verification log

Task received 2026-11-14, about 21:00 +04: “Verify: has open problem T050 been settled by the OpenAI math release?”

## Step 1 — orientation and initial retrieval (21:01 +04)

Read local file list, startup memory index, compute state and mesh protocol. The task confines all writes to this folder, so global mesh/checklist/brain writes are excluded. No git, external writes, subagents, or heavy computation.

Shell commands were prefixed `OMP_NUM_THREADS=1 nice -n 15`. macOS returned `nice: setpriority: Operation not permitted`; `ps` was sandbox-blocked. An attempted 900 MB address-space limit exceeded the inherited maximum; that Python process exited before writing anything. No load-intensive work was run.

Web opens of all three candidate root `paper.tex` URLs returned 404. First candidate directory returned cache miss. `build/paper.tex` attempts returned cache miss (first two) or 404 (third). Repository root opened successfully. Web search found all three candidate abstracts, Plectis Atlas transcriptions, a repository formalization manifest, Prove2Me review entries, and secondary expositions. These are discovery results, not yet theorem evidence.

Commands: `rg --files`, read-only `head`, `date`; `web.run` open and search batches. Current files initially: PROMPT.md, run.pid, codex.log.

## Step 2 — repository discovery

GitHub read-only connector successfully opened all three candidate directories: each has README.md, build/, and main.pdf (not paper.pdf at root). Opened repository root and Plectis Atlas transcription of the strict-convexity paper. Its displayed Theorem 1.1 claims strict convexity only for exponential weights on Z^2; Theorem 1.2 claims differentiability for Gamma weights. This points to PARTIAL-CLAIMED, pending exact primary-source confirmation. Atlas also links outside reviews warning that Lean targets are narrower; those reviews remain to be opened.

## Step 3 — primary statements read and saved

Opened each `build/main.tex` and its introduction section through the GitHub read-only connector. All papers name author OpenAI and date September 24, 2026. Saved exact primary introduction sources as convexity-introduction.tex, bigeodesics-introduction.tex, and univalent-introduction.tex. Main theorem of the first paper is strict convexity and differentiability for exponential weights on Z^2; Gamma extension is differentiability only. Second paper explicitly assumes no strict convexity and claims simultaneous absence of bigeodesics under the planar minimum-of-four second moment. Third paper concerns integral means of univalent maps and is unrelated to FPP.

Opened and saved `lean/docs/212.md`, `lean/docs/072.md`, `lean/formalization.yaml`, and `history.md` (filenames here replace slashes with hyphens). Doc 212 explicitly says strict convexity is outside the selected formalization statements. History contains no listed correction or withdrawal of these three papers. Repository-level docs/ returned 404; the relevant directory is lean/docs/.

Web searches performed: exact titles; strict convexity/OpenAI/error/refutation; no bigeodesics/OpenAI/error/refutation; exact strict-convexity title/arxiv. Opened Atlas family 212 and its links to MathVet's fidelity table and cert-machine's statement audit. Detailed primary audit records will be read next. No arXiv version of the candidate papers located so far.

## Step 4 — formalization scope and follow-up audits

Opened PlanarFirstPassage.lean, GammaPassage.lean, StrictMeans.lean, their FPP Comparator JSON configurations, Comparator README, and all candidate READMEs. FPP challenge statements contain differentiability, C1 boundary, and uniqueness of a support at each point; they do not contain strict convexity. Challenge files intentionally contain `sorry`; separate solution modules are named by the JSON configurations. No Lean builds were run.

Opened primary external audit artifacts through GitHub: mathvet/mathvet fidelity-table.csv at 14c7f918cd336d0da03a02aae5a0eed4a429d4db, and carlostoledo1891/cert-machine certs/openai-math-statements.json at 9814e4c06281e34a113ce853d7d99ccce160b750. Family 212 is partial / NARROWER — UNLINKED: neither strict convexity nor no-bigeodesics is in the selected Lean targets. MathVet reports comparator-sandboxed-pass for the differentiability targets. These are scope/checker reports, not expert certification of strict convexity.

Exact-title arXiv-domain searches for all three papers located no arXiv versions. GitHub issue search `repo:openai/math "first-passage"` returned no issues. Search found further expositions/catalogue entries; none yet establishes a named specialist review or a refutation. Web PDF attempts at main.pdf failed on content type for first two; third main.pdf cache miss. Primary TeX sources are readable and remain the quotation basis.

## Step 5 — core deliverables saved

Wrote REPORT.md with PARTIAL-CLAIMED on its first line and three reason lines. Wrote VERIFY.md with exact primary TeX theorem environments for all candidates (and the Gamma theorem), clause-by-clause comparison, follow-up evidence, source links, and a three-sentence replacement status. Saved Lean challenge files and relevant external audit excerpts. Opened both Orply expositions. Additional searches for exact titles plus referee/expert/error/refutation found no named expert review or refutation. Opened arXiv abstract 2610.42124 as a possible later citation lead; its relationship to the candidate is not yet established and is not used in the verdict. AI Proof Watch full-page open failed (cache miss), so that page is not used as primary evidence.

Next: spot-check the central strict-convexity contraction proposition. Its conclusion and dependencies were opened and saved as strict-conclusion.tex, strict-improvement.tex, and strict-foundations.tex. The main proof iterates a contraction b(Dn) <= rho b(n) against a uniform lower bound c0 > 0.

## Step 6 — spot-check reading and resource confirmation

Read the contraction proposition (Section 15.7), the main theorem's flat-face conclusion (Section 16), and the finite-range replacement lemma (Section 15.5). Verified by direct algebra that the final scale factor is D(C1*s + epsilon), with D fixed before s and epsilon. Checking the replacement cost inputs and infimum step next.

Read-only Python confirmation, under `OMP_NUM_THREADS=1 nice -n 15`, reports inherited nice = 20. Thus the earlier nice warning is caused by an already lower-priority process; no CPU-priority escalation was requested. The only Python commands have been tiny file/metadata reads, with no heavy numerical or symbolic work.

Opened arXiv:2610.42124 abstract: Scott Armstrong and Ahmed Bou-Rabee, “Fluctuation bounds for rotationally invariant first-passage percolation,” submitted October 30, 2026. It studies a rotationally invariant model on R^d, not the lattice strict-convexity statement. Full text being checked for the apparent citation lead; this paper is not treated as a version or validation of the OpenAI theorem.

## Step 7 — later citation confirmed and spot check saved

Opened arXiv:2610.42124v1 full HTML and located its introduction's acknowledgment of the planar exponential announcement and reference [Ope26]. Added this later citation, with authors exactly as shown on arXiv, to VERIFY.md. It does not assess or certify the proof.

Appended Spot check to VERIFY.md. Target is the decisive contraction proposition in Section 15.7 (source label improvement:contraction-proposition), including its supporting finite-range replacement cost estimate. Recomputed the three epsilon/3 error terms, the D rescaling factor, the infimum limit, and the final contradiction. Checked the independence and sign bookkeeping in the replacement lemma. No algebraic error isolated; upstream construction and uniformity assumptions (G)/(L) remain outside this limited check. This does not judge the full proof correct.

Correction to Step 2's directory summary: the first two candidates have main.pdf, while the univalent-functions candidate has paper.pdf. Its readable primary source is build/main.tex with sections/00-introduction.tex. The primary-source theorem quotations were unaffected.

## Step 8 — final audit

Ran a small read-only Python audit under OMP_NUM_THREADS=1 and nice -n 15 (inherited nice 20). PASS: REPORT has the required verdict first line and three reason lines; all four quoted theorem environments in VERIFY exactly match the saved primary TeX; every local evidence link exists; recommended replacement is at most three sentences; Spot check is present. Corrected math formatting in the appended spot check before this audit. Tried the third candidate's correct paper.pdf URL: browser returned unsupported application/octet-stream; readable TeX remains the evidence source.

Completed: VERIFY.md, REPORT.md, LOG.md and local source/audit excerpts. No git commands, builds, external writes, accounts, posts, messages to third parties, or subagents. Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — received 14 November 2026, about 21:00 +04.

Audit correction: the first link-check regex also interpreted mathematical `M[f'](r)` inside a TeX quote as a file link and stopped at the spurious target `r`; it did not identify a document defect. Restricted the check to Markdown links outside fenced quotations and reran the audit. The rerun passed all checks listed above.
