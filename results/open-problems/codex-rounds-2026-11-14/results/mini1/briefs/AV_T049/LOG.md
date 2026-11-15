# T049 verification log

Task: “Verify: has open problem T049 been settled by the OpenAI math release?” Started 14 November 2026, about 21:00 Asia/Tbilisi (workspace timestamps).

## 1. Scope and initial retrieval

- Read the supplied task and standing instructions. All output stays in this folder; no git, external posting, subagents, mesh/checklist writes, or brain writes. The task-specific prohibition on editing elsewhere overrides the general shared-state routines.
- Commands (all prefixed `OMP_NUM_THREADS=1 nice -n 15`): `pwd`, `rg --files` for existing task files, `cat ~/.claude/compute/compute_state.json`, `ls -la`, and read the brain navigation index. Existing task input is `PROMPT.md`; no prior VERIFY.md or REPORT.md. The compute state is `warn`, `owner_away_open`; no heavy compute is planned. `nice` reports `setpriority: Operation not permitted` in this sandbox; commands are tiny read-only utilities. No unbounded computation was launched.
- `web.run open` on the three supplied GitHub folders returned cache misses. Opening the first candidate's guessed `paper.tex` returned 404.
- `web.run search_query`: `site:github.com/openai/math "The-free-uniform-spanning-forest"`; exact first title; `"Metric measure limits" "subcritical" "2026"`; `"sharp factor" "free Ising" "2026"`.
- Results identify all three as OpenAI manuscripts, with dates matching the prompt. The first PDF has the long folder name as its filename, rather than `paper.pdf`. Search results also identify possible later expositions and Lean scope pages; these remain leads until opened. The repository root opened successfully.

## 2. Repository documentation and access checks

- Opened actual repository files through `web.run`: `README.md`, `CONTENTS.md`, `history.md`, `lean/README.md`, and `lean/formalization.yaml` (raw.githubusercontent.com/openai/math/main/...). The README describes model-produced research with differing verification stages. History through 29 October mentions no change to these three candidates. This is a repository statement, not an expert endorsement.
- Raw PDF endpoints for the forest and Ising preprints returned `Unsupported content-type: application/octet-stream`; guessed TeX filenames returned 404 or cache miss. Continued trying actual paper source routes and PDF rendering endpoints rather than treating abstracts as theorem statements.
- Tiny network check: `OMP_NUM_THREADS=1 nice -n 15 curl -L --max-time 30 --max-filesize 3000000 -I https://raw.githubusercontent.com/openai/math/main/README.md` failed DNS resolution in the shell. Web search remains usable. No files outside the task folder were changed.

## 3. Actual source and formalisation scope

- Opened the first preprint itself: `preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/paper.tex` and `build/sections/introduction.tex`. Author `OpenAI`; date 25 September 2026. Theorem 1.1 is a universal Borel equivariant IID sampler for FUSF, not a minimal-forest component theorem. The same source contains Theorem 1.3 for invariant strongly Rayleigh laws on countable groups.
- Opened all three manuscript README files; these confirm exact titles, author `OpenAI`, dates, and filenames. Opened the planar-map preprint's `build/main.tex`; it includes `sections/01-introduction` and uses `main.pdf`.
- Opened `lean/docs/231.md`, `lean/docs/236.md`, and both linked Comparator challenge files (`FreeUniformSpanningForest.lean`, `FreeIsing.lean`). Documentation claims formalisation of FUSF sampling and the free-Ising IID threshold respectively. The challenge files contain `sorry` placeholders, so they must not be misreported as completed proofs; the Comparator instructions and actual solution mapping need separate inspection. Neither statement counts minimal-spanning-forest components.
- API directory listing URLs were inaccessible. GitHub raw-PDF query variations were cache misses or robots-denied. TeX access works once the actual `build/` location is used.

## 4. Main statements read; first report saved

- Opened the actual `build/sections/01-introduction.tex` for both remaining papers, after reading their `build/main.tex`. The planar Theorem 1.1 is GHP convergence of finite FK/spanning-tree maps to LQG spheres. The Ising Theorem 1.1 is the threshold `tanh(beta) ≤ (d−1)^(-1/2)` for IID-factor spins on the d-regular tree, including equality.
- Opened solution mappings and actual Lean entry points: `lean/ComparatorChallenges/FreeUniformSpanningForest.json` → `OAI.Probability.SpanningForest.Factor`; `FreeIsing.json` → `OAI.Probability.FreeIsing.Main`. Both entry points supply proofs using imports. They were read, not compiled. Family 211's scope note covers only the different q>4 CRT manuscript.
- Opened Lyons–Peres–Schramm, *Minimal spanning forests*, arXiv:math/0412263, abstract page and full PDF; authors checked on both. The introduction distinguishes the minimal and uniform models directly.
- Opened Latent Seminar's 6 October forest exposition and the community Ising record (AI-collected unreviewed notes dated 21 October). Neither is a referee report.
- Saved REPORT.md with `VERDICT: NOT-THIS`, and VERIFY.md with all three exact theorem statements, phrase-by-phrase comparison, opened sources, formalisation scope, and a provisional three-sentence replacement status. Further follow-up search and a single load-bearing-lemma check remain.

## 5. Follow-up queries and spot-check source selection

- `web.run search_query` for each complete candidate title plus `arxiv error correction review`, and for `"minimal spanning forest" "dimension" "2026"`. These found later expositions and status aggregators, but no candidate arXiv version or specific refutation in the returned results. Search snippets alone are not endorsements or papers opened.
- Opened the first preprint's `build/sections/decoder.tex` and `build/sections/response.tex`. The decoder's deterministic inverse is the bridge from the response estimate to an actual IID sampler, and is the intended single-lemma spot check. REPORT.md was already saved before this optional check.

## 6. Focused arXiv search and deterministic inversion read

- Searched `site:arxiv.org "free uniform spanning forest" "factor" "OpenAI"`, `site:arxiv.org "Metric-measure limits of subcritical"`, and `site:arxiv.org "sharp factor-of-IID threshold"`. No matching candidate arXiv version was returned. Also searched `"minimal spanning forest" "d" "8" "open"`; this found primary book/paper discussions of the same open question and competing conjectural thresholds. These are leads until opened.
- Opened community records for the forest and planar-map candidates. The Ising Latent Seminar URL with lowercase `openAI` returned no readable lines; retry with `OpenAI-Math` is needed.
- Read decoder.tex lines 11–88 in full: Lemma 4.1, deterministic inversion. Re-derived the factorial Picard bounds and checked the uniqueness argument using bounded drift, not boundedness of the countably many input paths. Checked Borel measurability via rational-time evaluations, causality, and relabeling. No gap found in this isolated lemma under its stated assumptions; this is not a validation of the full sampling theorem or of its response assumptions.

## 7. Later expositions and primary follow-up leads

- Opened and read the forest and planar-map community pages. The forest page reports a Comparator acceptance on 26 October and links its log; the planar page lists two independent October arXiv papers by Nina Holden, and Nina Holden with Pu Yu, as relevant follow-ups. Those primary papers must be opened before attributing their comments.
- Opened Orply's planar-map exposition, credited `Perplexity`, dated 11 October 2026. Opened the Ising Latent Seminar exposition at the corrected `OpenAI-Math/236-tree-ising-factors` URL, dated 6 October. Both are expositions; neither is a referee report. The AI Proof Watch URL failed cache retrieval and is not treated as an opened source.
- Tried opening the corrected Lyons–Peres book PDF, but the web tool refused its 23.5 MB size; did not download it or treat it as read. The full Lyons–Peres–Schramm paper had already opened successfully.

## 8. Primary follow-ups opened

- Opened arXiv:2610.10501 abstract and HTML: **Nina Holden**, *The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity*, submitted 7 October 2026. It concerns conformal/Tutte embedding and random walks on tree-weighted planar maps, not a version of the OpenAI manuscript or T049.
- Opened arXiv:2610.10505 abstract: **Nina Holden, Pu Yu**, *The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity*, submitted 7 October 2026. The abstract concerns conformal embeddings in disk/sphere/whole-plane topology. HTML without the version suffix timed out; retry remains.
- Clicked the forest community page's Comparator log and Lean-check documentation, and the Ising page's existing-issues link. The log and issues page failed cache retrieval; the documentation opened. Raw-file retries are the next read-only step. No issue, account, or comment was created.

## 9. Follow-up findings and spot check saved

- Read Holden's statement following Section 1.3 in full HTML: it explicitly names the planar-map candidate and says the Open AI papers solve several previously listed open problems. This is a named expert comment about related planar-map claims, not a referee report. Opened the versioned HTML of Holden–Yu successfully; the arXiv abstract title and HTML title differ slightly, so the report records that difference instead of silently inventing a uniform title.
- Repeated exact-title searches with `refutation mistake gap` / `mistake gap referee`; no specific candidate refutation, error report, or referee report found. Raw Comparator-log retry also failed cache retrieval; its reported acceptance remains attributed to the community page.
- Appended all positive follow-ups, negative-search limits, original-model cross-check, and the complete isolated Lemma 4.1 spot check to VERIFY.md. Kept the recommendation to three sentences and retained `NOT-THIS` in REPORT.md. Final file/format audit remains.

## 10. Final audit and completion

- Checked Holden–Yu's actual HTML statement before the acknowledgements: they say neither their results nor the OpenAI results imply the other, to their knowledge. Added that expert scope comment to VERIFY.md. Read the community Lean-check documentation's explanation of challenge placeholders, solution modules, and the limits of reported Comparator runs. No new claim about proof correctness was made.
- Command: `OMP_NUM_THREADS=1 nice -n 15 python3` with a short inline `pathlib`/`re` audit. Output: REPORT.md has exactly four lines (NOT-THIS verdict plus three reason lines); VERIFY.md includes all theorem comparisons, primary follow-ups, and Spot check; the replacement status has exactly three sentences. All assertions passed. Sizes at audit: REPORT.md 605 bytes, VERIFY.md 21,868 bytes, LOG.md 10,252 bytes before this final log entry. The audit consumed negligible memory and finished immediately; `nice` again reported the sandbox's priority-setting restriction.
- Workspace clock at audit: **2026-11-14 21:07:20 +04:00 (Asia/Tbilisi)**. All deliverables are inside AV_T049. No git, posting, accounts, outside-folder edits, heavy compute, or subagents were used.
- Result: these three candidates do not claim either requested component-count conclusion for the minimal spanning forest on Z^d. The original row should not be marked solved by these matches. No specific refutation or candidate arXiv version was found; related planar-map papers and expert comments are recorded with their actual scope. Isolated deterministic-inversion spot check found no gap under its assumptions.
