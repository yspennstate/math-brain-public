# T129 verification log

Task received: 2026-11-14, approximately 21:07 Asia/Tbilisi (17:07 UTC): “Verify: has open problem T129 been settled by the OpenAI math release?”

## Step 1: orientation and first retrieval attempts

- Read the workspace listing, compute state and mesh protocol using `OMP_NUM_THREADS=1 nice -n 15 python3 ...`. Workspace initially contained only PROMPT.md, codex.log and run.pid. Compute state: warn, owner_away_open, CPU saturated; no heavy computation planned.
- Attempted the prescribed brain recall with `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall ...`; interrupted it to avoid unnecessary model-based recall during a literature-only task.
- `nice -n 15` reported `setpriority: Operation not permitted`; later commands must check inherited priority. No subagents, git commands, or external writes are authorized. The task-specific folder-only instruction takes precedence over the global mesh/checklist/memory write requirements, so those external state updates will not be run.
- Web tool `open` was called on all three supplied GitHub folder URLs. Each returned “Failed to fetch ... Cache miss”. These are retrieval failures, not evidence about theorem contents. Will try raw files and repository access.

## Step 2: successful repository access and initial search

- Used the read-only GitHub connector `github_fetch` on the GitHub Contents API for each supplied folder. All three directories are accessible; each contains README.md, a PDF, and build/. No git command was used.
- Web search queries were the exact three manuscript titles. Results identify family 239 for the two singularity papers and family 211 for the planar-map paper. Search snippets claim the October 3 paper covers the fair-sign model and the October 4 paper explicitly excludes p=1/2; this will be checked against the actual sources.
- Located possible follow-up pages at MathDB, Plectis Atlas, Proofweave and Open Math Atlas. They remain leads until opened.
- Checked inherited priority using `OMP_NUM_THREADS=1 nice -n 15 python3 -c ...`: inherited nice value is 20, lower priority than the requested 15. The setpriority warning is from attempting to raise that priority; future commands will use `nice -n 15` with this inherited value and remain at 20.

## Step 3: source files, author/date and repository notices

- Opened all three `build/main.tex` files, all three manuscript README.md files, and all three build/sections directory listings through the GitHub reader. Author on every manuscript: OpenAI. Dates are October 4, October 3 and September 24, 2026, respectively.
- The actual October 3 abstract states exactly the target fair-sign asymptotic. The October 4 abstract excludes p=1/2. The September 24 main theorem is a Gromov–Hausdorff–Prokhorov scaling limit of critical Fortuin–Kasteleyn planar maps, not a matrix theorem.
- Opened root README.md, history.md, lean/README.md, lean/formalization.yaml, and lean/docs/211.md. README describes manuscripts as raw research data and says unformalized results could have issues. history.md contains no named update or withdrawal for these candidates. The formalization catalogue has no singularity/Bernoulli/biased/Fortuin textual match; the planar-map coverage must be followed through the explicit docs link instead. lean/docs/211.md explicitly names the planar-map theorem and FKCRT.lean. lean/docs/239.md returned 404. Root docs/ also returned 404; the relevant docs directory is lean/docs/.
- One JavaScript orchestration call failed before collecting output because `.entries()` was called on a Promise; the corrected call completed. No local files or repository state were altered by that failed read call.

## Step 4: exact theorems and provisional verdict saved

- Opened both singularity manuscripts’ build/sections/01-introduction.tex. Both main statements are Theorem 1.1. October 3 states the whole T129 claim exactly; October 4 states a fixed-p nth-root limit with p=1/2 excluded.
- Saved REPORT.md with `VERDICT: SOLVED-CLAIMED the whole statement is claimed`. Saved manuscript sources and repository notices under sources/ using apply_patch, entirely within this folder.
- Read-only GitHub issue search `repo:openai/math singularity` returned no issues. Directory commit-history API for the October 3 manuscript returned only initial commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, dated October 6, 2026, 21:58:50 UTC.
- Opened MathDB’s target page: both manuscripts are marked claims, each with zero endorsements. Opened Columbia’s Fall 2026 Student Probability Seminar schedule: Jiahe Shen’s October 8 survey explicitly distinguishes the new symmetric sharp-rate claim from established published results. This is evidence of discussion, not a proof audit.
- Opened arXiv:2610.39424: authors Huaijin Liang, Kexin Yu, Tingzhou Yu; submitted October 29, 2026. It claims a general exponential rank bound, not the sharp base 1/2 and not verification of OpenAI’s proof.
- Opened the lean/docs and ComparatorChallenges directory listings and lean/OAI.lean. No 239 doc or singularity comparator is listed; the only Bernoulli comparator is BernoulliNonflatInSeven (a different subject). FKCRT.lean exists for the unrelated planar-map theorem and was opened. Absence from formalization.yaml alone is insufficient: that file also lacks the documented FKCRT name.
- Retrieved and saved all remaining October 3 proof sections for the requested optional spot check. No proof correctness conclusion has been drawn.

## Step 5: follow-up searches and spot-check selection

- Web search included both exact singularity titles with `site:arxiv.org`, plus combinations of OpenAI, symmetric Bernoulli, singularity, error, gap, refutation, Sahasrabudhe and family 239. No arXiv repost or specific refutation was identified in these results. Searched the exact planar-map title with arxiv/error as well. Negative search results do not prove absence.
- Opened Plectis Atlas family 239 and Proofweave family 239. They are catalogue/exposition leads; neither supplies independent verification of the proof. The lowrank latent-seminar exposition appeared in search but direct web open failed, so its full text is not used as evidence.
- Selected the October 3 paper’s Lemma 11.2 (“Cost of heavy retained layers”) for the spot check. It supplies the key conditional probability bound in the long-path tail estimate underlying Proposition 2.7 (“Potential moment”). Reading its proof and the retention-lattice dependency; the spot check will not certify the whole paper.

## Step 6: complete verification note and spot check saved

- Wrote VERIFY.md with exact source quotations of all three main theorems, model/range/quantity/strength comparisons, follow-up sources actually opened, negative-search limits, and a three-sentence recommended replacement for the row. An initial write orchestration had a JavaScript string quoting error and was corrected before any write occurred.
- Directory histories for the biased-sign and FK-map candidates also returned only the October 6 initial commit. The theorem citations in VERIFY.md are pinned to that commit.
- Opened Carlos Toledo’s release audit; a text search for 239 found no match, so no assessment of these singularity proofs is inferred from its general findings. Opened FKCRT.json and recorded its solution module/theorem; it concerns the planar-map candidate only.
- Spot check: rederived the retention-lattice implication, maximal-dissociated-set fixed-mask exponent 2qN/3, and both mask-entropy bounds in Lemma 11.2. The union bound retains coefficient margin 1/15 over 3/5, with entropy o(qN) uniformly for q ≥ eta/(100 log N). No error was found in that local argument; the rest of the paper remains unverified.
- All deliverables and source snapshots were written with apply_patch inside AV_T129. No new computational test or Lean build was needed; no subagents, git commands, external posts or accounts were used.

## Step 7: final artifact audit

- Ran a small standard-library-only audit with `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B ...`. Inherited nice remained 20; runtime was under one second. No simulation, model, or Lean build was run for this audit.
- All three theorem quotations in VERIFY.md match the saved preprint TeX byte for byte. REPORT.md has the required verdict on line 1 and exactly three reason lines. The recommended status paragraph has three sentences.
- Files audited: VERIFY.md 17,781 bytes; REPORT.md 553 bytes; 26 source snapshots totaling 370,610 bytes. LOG.md records the retrievals, failures, comparisons, follow-up searches, and spot check.
- Completed outcome: the entire T129 statement is claimed by the October 3 OpenAI preprint. No independent verification or Lean formalization of that singularity result was found in the checked sources; one local lemma check found no error and does not certify the proof.

Task: “Verify: has open problem T129 been settled by the OpenAI math release?” — received November 14, 2026, approximately 21:07 Asia/Tbilisi.
