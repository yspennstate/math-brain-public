# T116 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: November 15, 2026, 10:54 Asia/Tbilisi.

## Startup and prior work, 10:54–10:56

Read REPORT.md, LOG.md, all available PROOF.md and AUDIT.md, and SOLVED_ELSEWHERE.md in the four earlier folders. Round 5 alone has PROOF.md; no research scripts were present. Earlier files remain unchanged. Read startup memory and compute state directly. State: ok, owner_away_open; no heavy work planned. The folder-only restriction overrides shared brain, mesh and checklist mutations and recall logging. No subagents, git or external writes.

Local commands use OMP_NUM_THREADS=1 nice -n 15 python3 -B. The wrapper emits setpriority: Operation not permitted, but os.getpriority independently reports effective nice 20.

Independent recheck of round 5: under a uniform prior on K distinct words, write a_i(z) for decoder output probabilities. Comparing P_i with one common R gives average success <= K^(-1) + K^(-1) sum_i TV(P_i,R), since sum_i a_i <= 1. A second derivation compares the joint laws K^(-1)P_i and K^(-1)R and uses their total variation, equal to the same average distance. Thus round 5 holds, conditional on its hard-family estimate. For epsilon=sqrt(m*g*N^(-d))+2*m*g*E, m<=eta^2*N^d/(4*g) bounds the first term by eta/2. The case g=0 cannot contradict any success <=1; for s>0 choose g with 2^(-g)<s. No construction is certified by this check.

## Bounded literature check and choice, 10:54–10:56

Web search queries: `"trace reconstruction" "superpolynomial" "2026"`; `site:openai.com "trace reconstruction"`.
Opened primary manuscript main.tex and sections/introduction.tex and lean/docs/122.md under https://raw.githubusercontent.com/openai/math/main/. Header: OpenAI, September 24, 2026. The theorem still states T_{q,s}(n)>=n^{c log(q^3 log n)} eventually for fixed s>0 and 0<c<1/(4 log 2), when q^3 log n tends to infinity. No later result settling the exact order was found. This is a reported resolution of the polynomial-sample question, so the requested literature-stop branch applies.

New source leads in search results: full revision adc7f1241b42e322a6451854ab7e4b4c146bf78a and another purported revision 1581d4cbdd69a0faf34b2089614fe2a814316a6a. Opening the first GitHub commit page succeeds and shows the initial commit. Pinned raw Induction.lean URLs for both revisions fail with cache miss. An incorrectly short main/lean/TraceReconstruction.lean path also fails; the prior report gives the correct OAI/Probability path.

Choice before further checking: attempt a bounded immutable-source audit of the quantitative construction, the specific next step named by round 5. This is verification of the reported resolution, not a new research extension. Do not attempt a Lean build: no dependency installation is authorized and no compliant sub-1-GB build has been established. Record the exact boundary reached, write SOLVED_ELSEWHERE.md and REPORT.md, then stop.

## Immutable-source access, 10:56

The read-only connected GitHub fetch_file tool succeeds at ref adc7f1241b42e322a6451854ab7e4b4c146bf78a. Its content[] says only “Action completed.”, but structuredContent contains the full UTF-8 source, blob SHA and pinned display_url. This explains the uninformative connected-tool response in round 4. Induction.lean blob SHA: 933f46fdee0b606ec611e3c92a631077d7dd1d18. Comparator JSON blob SHA: 734fb3a2e226775e1f9145f0e6f37bb121a1ba32. These two pinned files are available; a full proof snapshot has not yet been obtained.

Next bounded action: save the pinned entry point, comparator, induction, manuscript theorem and environment metadata with independent Git blob hash checks. This makes round 5’s requested immutable-source step concrete. No formal checker will run.

The literature decision is complete within five minutes. Extend the same source audit to the entry point’s transitive OAI imports, with Mathlib treated as an explicit external boundary. Save only the needed source files and recorded toolchain/dependency manifest; do not install or build anything. This addresses reproducibility of the already reported resolution. All fetched bytes will be checked against GitHub’s blob SHA using SHA-1 of the Git blob header plus bytes, and also assigned SHA-256 checksums.

Saved first 15 pinned files under snapshot/, independently verified all Git blob SHA-1 values before writing, and recorded SHA-256 values in snapshot/MANIFEST.json. Initial OAI import frontier continues through Simulation and LayoutRates.

Pinned snapshot now contains 37 files and 1580481 source bytes; all blob hashes checked before saving.

Recursive OAI import retrieval finished; checking exact closure independently from files on disk is next. No tool errors occurred during recursive source retrieval. lean/lakefile.toml was absent (404); lean/lakefile.lean was fetched successfully instead.

## Pinned artifact verification

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_snapshot.py`.
Output: 38 files; 1,680,281 source bytes; 31 OAI modules; 33,984 OAI source lines. Git blob SHA-1 and SHA-256 checks PASS for all files. Exact reachable OAI closure PASS; the only external import boundary is Mathlib. No sorry, admit, axiom or opaque tokens remain in the 31 solution modules after nested-comment and string masking. The separate challenge has three sorry tokens, as expected for a statement file. This source scan is not a Lean parse, elaboration, kernel check or axiom inspection.

Environment: leanprover/lean4:v4.34.1; Mathlib revision d13f23b723b8a846827a245b89c10fc7d3f11612; effective nice 20. Script reports elapsed 0.517 seconds and peak resident memory 27,475,968 bytes on macOS. No Lean executable ran, and no package was installed. Tools retrieved source at the pinned ref using read-only GitHub fetch_file calls; only local snapshot files were written.

Independent checks: each hash was computed both from complete file bytes and incrementally in 8192-byte chunks; source byte count was checked with filesystem stat; module reachability was checked both forward from the entry point and backward from each file to the entry. A raw lexical scan had matched “admit” in an English comment at Differences.lean:899. Masking comments removes this false positive. The scanner remains a deliberately limited source check, so zero flagged tokens does not imply accepted axioms.

## Completion

Written: REPORT.md, SOLVED_ELSEWHERE.md, SNAPSHOT.md, PROOF.md, verify_snapshot.py, and the pinned source artifact. The acquisition used `github_fetch_file(repository_full_name="openai/math", ref="adc7f1241b42e322a6451854ab7e4b4c146bf78a", path=...)`; every successful path and returned blob SHA is preserved in snapshot/MANIFEST.json. Independent calls were batched; dependent import discovery and local writes were sequential.

Primary paper URLs opened with the web tool:
- https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex
- https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex
- https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex
Also opened the primary lean/docs/122.md, main-branch Induction.lean, and commit page. Pinned raw Induction URLs failed for adc7f1241b42e322a6451854ab7e4b4c146bf78a and 1581d4cbdd69a0faf34b2089614fe2a814316a6a; only the former revision was ultimately obtained, via the connected tool. Failed main/lean/TraceReconstruction.lean was a path error. Several pinned GitHub blob pages also failed; no inference of absent files was made from those failures.

Final command: OMP_NUM_THREADS=1 nice -n 15 python3 -B with nonempty-file, verdict, manifest count, byte count, independent newline-based source-line count, and theorem-name checks. Output: final file audit PASS; 38 fetched files; 1,680,281 bytes; 31 OAI modules; independently counted 33,984 lines; effective nice 20. The full source-integrity/import checker had already passed, so no Lean or further mathematical computation was run. Mathematical boundary checks are in PROOF.md; no new lower-bound claim is made.

Stop: the literature branch has been completed. New beyond round 5 is a pinned, byte-checked source artifact and reproducible closure audit. Construction estimates, theorem axioms and comparator acceptance remain unverified here.

Completion clock: 2026-11-15T11:01:34.853325+04:00
