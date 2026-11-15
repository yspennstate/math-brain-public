# T030 verification log

Task: “Verify: has open problem T030 been settled by the OpenAI math release?”
Started: 2026-11-14 20:58 Asia/Tbilisi (16:58 UTC).

## 1. Orientation

Read the workspace listing, global instructions and compute state with a small Python read-only command prefixed `OMP_NUM_THREADS=1 nice -n 15`. Workspace initially contains PROMPT.md, codex.log and run.pid. Compute status is warn, mode owner_away_open; no heavy computation planned. The sandbox printed `nice: setpriority: Operation not permitted`; the read-only command nevertheless completed. No subagents, git, or external writes will be used. The task's folder-only rule takes precedence over global memory/checklist/mesh writes; those state-changing commands are omitted. Startup memory at the attempted path was absent.

Next: open the three supplied preprints and search the web for follow-ups.

## 2. First web search

Used `web.run` to open the three supplied folders and search `"Strict hot spots" "OpenAI"` and `"openai/math" "hot"`. Folder opens returned cache misses. Search located the hot-spots manuscript (Theorem 1.1, smooth simply connected domains), upstream Lean scope document 369, community pages, and a follow-up titled *Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*, arXiv:2610.12622. These are leads until opened. The theorem's smoothness restriction is potentially material to the row's arbitrary convex domains.

## 3. Repository access and follow-up leads

Read all three directory listings and build-directory listings through the read-only GitHub connector (`github_fetch`, GitHub contents API). The first has `main.pdf`, `build/main.tex` and split sections; the others have `paper.pdf` and split TeX sources. No git used. Web searches for the other exact titles locate optimal-transport and complex-geometry papers. Opened arXiv abstracts 2610.12622 and 2610.18546 and the community hot-spots page; the latter lists a comparator acceptance and warns that statement correspondence has not been checked. Further source reads follow.

## 4. Main theorem sources opened and saved

Opened the three main TeX files and the first two introductions via `github_fetch_file`. Saved exact upstream text locally as `source-0-main.tex`, `source-0-introduction.tex`, `source-1-main.tex`, `source-1-introduction.tex`, `source-2-main.tex`. All three name OpenAI as author. Hot-spots Theorem 1.1 assumes C-infinity boundary; MTW Theorems 1.1–1.2 concern compact boundaryless Riemannian manifolds and squared-distance transport; symmetry Theorem 1.1 concerns complex affine varieties and biholomorphisms.

Opened arXiv:2610.18546v2 full HTML (Haiyun Deng, Xuyong Jiang, Xiaoping Yang, revised 2 Nov 2026). Theorem 1.2 controls strict boundary maximum modulus, not both signed extrema; the text explicitly distinguishes these. Opened arXiv:2604.19003 abstract. A community link to Jizhou Guo's GitHub follow-up PDF returned 404, and its comparator-log link returned a cache miss; these require connector checks. No finding yet establishes the whole exact row.

## 5. Formal statements and expert-comment sources

Opened upstream `lean/docs/369.md`, `lean/ComparatorChallenges/HotSpots.lean`, `lean/README.md`, `lean/ComparatorChallenges/README.md`, `lean/formalization.yaml`, `lean/docs/360.md`, `lean/docs/058.md`, repository README and history, using `github_fetch_file`. HotSpots assumes `SmoothBoundary`; its challenge ends in `sorry` because it is a target statement with a separate proof. No Lean build attempted. The history does not list these candidates as withdrawn. MTW scope explicitly limits one formalized intermediate result to finite target families.

Opened full HTML for Burdzy, arXiv:2610.12622, and Deng et al., arXiv:2604.19003v4. Burdzy explicitly treats OpenAI's theorem as an unassessed external input. Deng et al.'s Declaration explicitly says smooth boundary excludes their polygons. Searched the exact other titles with arXiv/error terms: no directly relevant error report or arXiv replacement found in the returned results.

## 6. Saved verdict before optional spot check

Created REPORT.md: PARTIAL-CLAIMED, smooth convex planar domains. Opened actual Lean proof module `lean/OAI/Analysis/HotSpots/Main.lean` and comparator configuration `HotSpots.json`; it points to that module and permits only the listed standard axioms. Opened the community comparator log through the connector: it reports successful build of the solution, kernel acceptance and “Your solution is okay!” This is a read of a published log, not a local replay. The GitHub follow-up repository `aster2024/openai-math-followups` also returned 404 through the connector. Burdzy's Theorem 2.1 and Corollary 2.2 explicitly distinguish non-strict extrema from exclusion of interior extrema. REPORT.md is saved before any spot check.

## 7. Saved full verification

Created VERIFY.md with verbatim main-theorem TeX for all three candidates (also MTW Theorem 1.2), assumptions, phrase-by-phrase comparison, opened follow-ups and Lean evidence, bounded search conclusions, and a three-sentence replacement status. Four GitHub issue queries returned no issues. The inaccessible Guo lead is expressly excluded from evidence. No correctness certification made. Next: optional focused check of the central reciprocal-kernel lemma.

## 8. Spot-check source read

Opened and saved the actual hot-spots sections `04-boundary-kernels.tex`, `05-reciprocal-kernels.tex`, and `06-conclusion.tex` through `github_fetch_file`; snapshots use the prefix `source-0-`. The introduction identifies the reciprocal-kernel construction as the central analytic step. Selected its bounded Green-kernel regularization lemma (`lem:regularization`) for a detailed algebraic check, using the Green normalization in Section 4. No numerical computation or Lean compilation is needed.

## 9. Final follow-up search

Web search with the title plus “gap” and “counterexample”, and a site:arxiv.org title query, returned a further lead: Rodrigo Bañuelos, arXiv:2610.32920. Opened community pages for the two unrelated candidates; checking their commentary and this additional nonsmooth-domain follow-up before finalizing. Search also located an explicitly AI-written, not independently reviewed exposition at openmaths.org; opened its course page. No direct hot-spots refutation surfaced in these results.

## 10. Final follow-up and spot check saved

Opened Bañuelos's arXiv abstract and full HTML, including Theorem 1.2, Remark 1.3, AI Disclosure and Section 6. The paper name is Rodrigo Bañuelos (the abstract metadata misspells it); the result is explicitly conditional and non-strict, assumes simplicity, and Section 6 asks about removing simplicity. Added this source, the opened exposition and the unrelated candidates' community-page results to VERIFY.md. One intermediate patch failed to match an incomplete context line and made no change; corrected it with the exact section-heading context.

Appended “Spot check” to VERIFY.md: rederived the Green normalization, Lorentz-form identity, logarithmic-mean mixture, PSD geometric series including the diagonal, and regularization bounds/limits in `lem:regularization`. No algebraic defect found in that lemma; no claim that the complete preprint proof is correct. REPORT.md remains PARTIAL-CLAIMED.

## 11. Final artifact audit

Ran a tiny read-only Python audit prefixed `OMP_NUM_THREADS=1 nice -n 15`. An initial attempt to impose a 512 MiB RLIMIT_AS failed before any audit work (`ValueError: current limit exceeds maximum limit`); reran the same small text-only check without changing that limit. It completed in under a second and checked that all four theorem blocks in VERIFY.md match the saved sources exactly, REPORT.md has the required first line and three reason lines, the spot-check section exists, code fences balance, and no string-escape control characters corrupted the text. All passed. Although `nice` prints a sandbox warning, `os.getpriority` returned 20: the inherited process priority is already at least as yielding as requested. Output sizes: REPORT.md 954 bytes; VERIFY.md 23,353 bytes (LOG.md subsequently grew with this entry). Only this task folder was written. No git, subagents, build, GPU, messages, accounts, or external mutations were used.

Completed task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 14 November 2026, 20:58 Asia/Tbilisi (start time).
