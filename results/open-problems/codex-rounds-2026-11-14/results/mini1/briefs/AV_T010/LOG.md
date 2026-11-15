# T010 verification log

Task: “Verify: has open problem T010 been settled by the OpenAI math release?” Start: 2026-11-14 20:55 Asia/Tbilisi (16:55 UTC).

## 1. Orientation and scope

Read the startup memory index, compute state, and mesh protocol with `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c ...`. Compute state reports `status: ok`, `mode: owner_away_open`. Only lightweight reads are planned. `nice` prints `setpriority: Operation not permitted`; process-priority inspection with `ps` is also blocked by the sandbox, so effective priority could not be verified. No numerical computation was launched.

The task-specific rule forbids writes outside this folder. Therefore no mesh registration, checklist update, brain recall that logs externally, or memory write was run. No git and no subagents. Initial folder contains `PROMPT.md`, `codex.log`, and `run.pid`; no existing deliverables were found.

The startup memory includes a verified note that macOS can emit a nice error when an already-low-priority process receives another relative adjustment. That is a possible explanation here, not a measured effective priority.

## 2. First source-opening attempt

Used the web tool to open all three exact GitHub folder URLs supplied in the task. Each returned `Failed to fetch ...: Cache miss`. This is an access failure, not evidence that the papers do not exist. Next attempt: exact raw `paper.tex` URLs, repository root, and web search.

## 3. Raw-source discovery and first search

`web.run` opened the three raw root-level `paper.tex` URLs: each returned HTTP 404. Repository root opened successfully. Searched `"Pure Point Spectrum" "Two Dimensional" "OpenAI"` and `"openai/math" Anderson September 2026`. Search found the exact pure-point paper and a repository introduction source under `build/sections/introduction.tex`; its abstract restricts the claim to independent uniform potentials and pure-point spectral type. This is only a lead pending the theorem itself. Search also found `lean/docs/261.md` via a result-family page, repository `history.md`, and a later random-band-matrix paper mentioning the claim. No theorem has yet been copied from a preprint.

## 4. Preprint entry sources and formalization scope opened

Opened all three raw `build/paper.tex` entry sources successfully. Each gives author `OpenAI`; dates are September 23, September 23, and October 5, 2026 respectively. Their `input` commands identify the introduction files to open next. The raw pure-point PDF URL returned an unsupported `application/octet-stream` response; the TeX sources are readable.

Opened `https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md`: the formalization covers the almost-sure spectral set `[-4-h,4+h]` for uniform `[-h,h]` potentials, and explicitly does not assert pure-point type. Opened raw `history.md`: updates through October 29; no Anderson-specific withdrawal or correction is listed. This does not establish that no error exists.

## 5. All main theorem statements located

Opened raw `build/sections/introduction.tex` for the pure-point paper, `build/01-introduction.tex` for the absolutely-continuous paper, and `build/sections/01-introduction.tex` for the random-regular-graph paper. Read the complete main theorem in each (Theorem 1.1). Pure-point theorem: every fixed `h>0`, iid uniform `[-h,h]`, complete eigenbasis, spectrum `[-4-h,4+h]`, dense eigenvalues. Its introduction explicitly says it does not assert exponential eigenfunction decay (lines 85–86). Thus it is partial relative to our broader statement, even before assessing any proof.

The second theorem is for fixed dimension at least three, sufficiently small positive disorder, and a specified open energy interval of purely absolutely continuous spectrum. The third concerns microscopic GOE eigenvalue statistics of finite random regular graphs as size tends to infinity. Neither is a claim about localization on `Z^2`.

Opened all three preprint READMEs; none contains a correction or withdrawal notice in the retrieved version. Opened pure-point `bootstrap.tex` and `spectral.tex`, locating the true-torus fractional-moment theorem and its spectral readout. A direct shell download using `OMP_NUM_THREADS=1 nice -n 15 curl --fail --location --max-time 30 --max-filesize 1048576 <raw introduction URL> -o pure-point-introduction.tex` failed with DNS resolution error; no source download was obtained by shell. Web access remains usable.

## 6. Follow-up searches begun

Web queries: exact distinctive titles plus `error OR gap OR refutation OR review OR arxiv`, the AC title plus `Xu`, the random-graph title plus `review OR error OR arxiv OR Lean`, and `site:github.com/openai/math/issues Anderson`. Results will be checked against pages actually opened; search snippets alone will not be treated as verification.

## 7. Provisional deliverable saved; further primary sources opened

Saved `REPORT.md`: `PARTIAL-CLAIMED`, restricted to pure-point type for the uniform law, without exponential eigenfunction decay. It is a scope verdict, not proof approval.

Opened repository `lean/formalization.yaml`, `lean/ComparatorChallenges/PlanarAndersonSpectrum.lean`, and the GitHub issues landing page. Attempted `lean/docs/219.md`: HTTP 404. Opened `https://github.com/cadamcat/anderson-ac-lean4`, an external repository claiming a formalization of the dimension-at-least-three AC result; README details are still being checked. Opened `https://arxiv.org/abs/2609.24426`, a different paper on random band matrices, revised November 8, 2026. Exact-title arXiv-restricted searches did not surface an arXiv version of any of the three candidate manuscripts.

## 8. Follow-up findings checked further

Opened the HTML full text `https://arxiv.org/html/2609.24426v4`; authors on the arXiv page are Xujie Lai and Fan Yang. Located the passage discussing OpenAI for contextual follow-up, not as a proof endorsement. GitHub’s rendered `cadamcat/anderson-ac-lean4` README names Yao Xu and claims a Lean formalization of the AC theorem in dimensions at least three; its raw README failed to fetch, but the rendered README is readable. No connection to proving planar pure-point type follows from this.

The GitHub issues page displays zero open issues and no matching results; this is not an expert assessment. Searches for the planar title with `Lean`, and `"Anderson" "OpenAI" "refutation"` / `"error" mathematics`, found no specific primary-source refutation or named referee report. Several catalogs/explanations appeared; no mathematical conclusion is being taken from those secondary summaries. The repository’s `formalization.yaml` has no `Anderson` match.

## 9. Verification document saved

Created `VERIFY.md` with all three exact main theorem bodies copied from their TeX sources, model definitions, a clause-by-clause comparison for the planar claim, comparisons for the other two, sources opened, search limits, and a three-sentence replacement status.

Important later comment: Lai and Yang’s v4 introduction says the planar Theorem 10.1 also implies eigenvector localization, but describes the OpenAI results as claims and gives no referee certification. This was recorded alongside the planar paper’s express disclaimer of an asserted exponential-eigenfunction conclusion. It does not extend the potential law beyond uniforms. Xu’s README reports an axiom-free (apart from standard Lean axioms) formalization for the different, d>=3 AC problem; no build was run.

The Lean comparator challenge was read through its conclusion: only existence/self-adjointness and the spectral set. Its `sorry` is a challenge-template placeholder, not by itself a finding about the solution. Next: inspect the solution mapping and one load-bearing planar lemma if accessible.

## 10. Exposition opened; spot-check target selected

Opened Yao Xu’s *Extended states in the Anderson model*, version 1.0.2 (November 2026), via the MathDB-hosted PDF returned by web search. It distinguishes a formalized theorem from unrefereed manuscript arguments, describes the d>=3 formalization, and says planar all-disorder localization remains open. That broad sentence is not an audit of the separate planar manuscript and must not override its explicit claim or be treated as a refutation.

Opened planar `build/sections/vanishing.tex`. Proposition `van:zero` (Section 9) asserts the limiting affine energy d=0, the dimension-specific bottleneck feeding Section 10. Selected that proposition and especially its analytic-submean lemma for the optional spot check. Opened Comparator README; attempted `PlanarAndersonSpectrum.config.json` (cache miss), then the documented `.json` naming convention.

## 11. Vanishing argument and solution mapping

Opened successive ranges of `vanishing.tex`: geometry and scale order; the signed affine adjustment; small annular transmission and surviving internal jump energy; the analytic-trace bounds; the law-change estimate; and the final submean contradiction. These depend on earlier screening and thinning estimates; reading the final contradiction does not verify those inputs. The independent spot check will focus on the finite-matrix analytic-trace lemma that makes this bottleneck work.

Opened `lean/ComparatorChallenges/PlanarAndersonSpectrum.json`: solution module is `OAI.MathematicalPhysics.PlanarAnderson.Spectrum`, theorem `OAI.PlanarAnderson.anderson_spectrum_ae`, with the three standard permitted axioms. This confirms the limited comparator target and identifies the solution file to inspect; no Lean toolchain was run.

## 12. Analytic lemma read in full

Opened the entire `van:analytic-bounds` lemma and proof, the law-change subsection, and the final lines of the d=0 contradiction. Opened `build/sections/matrix.tex` for its supporting weak-integral estimate and `lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean` for the actual comparator solution. The latter defines a pure-point `MainStatement`, but merely defining a proposition is not proving it; checking the exported theorem is essential. Updated `VERIFY.md` to record Xu’s exposition as opened and to distinguish its broad planar-status remark from a specific assessment.

## 13. Lean conclusion and independent algebra checks

In the actual `Spectrum.lean` solution, lines 623–628 prove `anderson_spectrum_ae` with only existence, self-adjointness, and the spectral interval. A text search finds no `sorry`; later helper statements involving eigenbases do not change the comparator target. Further inspected the end of that source to rule out mistaking an implication assuming an eigenbasis for a proof of localization.

For the spot check, independently re-derived (i) `|det A|² >= 1-K` from the eigenvalues of `TT*`; (ii) `||A^{-1}-A*||_1 <= K/sqrt(1-K)`; (iii) the nonnegative symmetric internal-trace identity; and (iv) the small-moment exponent restriction `p<1/2`. No numerical calculation or proof-assistant build was needed. The earlier screening/good-event inputs remain outside this local check.

## 14. Spot check appended

Appended `Spot check` to `VERIFY.md`. Checked the analytic lemma’s determinant bound, trace sign, boundary analyticity, weak-tail moment integration, dimension dependence, and the submean/Hölder exponents. Found no local algebraic error conditional on the earlier good-event hypotheses. Explicitly left screening, thinning, good-event construction, and hierarchy invariance unverified. This is not a correctness finding for the paper.

Opened the actual MathDB problem page for Xu’s exposition context and the external repository’s `docs/verification.md` GitHub page. The latter returned mainly page chrome rather than useful verification content in the retrieved view; no new kernel-check evidence was inferred. Sources are mutable `main` URLs or identified arXiv versions; no repository snapshot or local build was obtained. Next and final step: read back the deliverables and check format and transcription.

## 15. Final audit and completion

Read back `REPORT.md`, `VERIFY.md`, and the log using `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'wc -l REPORT.md VERIFY.md LOG.md; cat REPORT.md; sed -n "15,190p" VERIFY.md; tail -n 16 LOG.md'` (exit 0, with the already-recorded nice warning). `REPORT.md` has the required verdict first line and three reason lines. Checked the three theorem transcriptions against the opened source passages, both energy-window formulas and the graph-size parity condition, the three-sentence status recommendation, source author names, and the distinction between a comparator statement and the actual solution. The spot check is appended after the main literature report and explicitly conditional. No git, posts, accounts, subagents, external writes, heavy programs, or Lean compilation were used.

Completed task: “Verify: has open problem T010 been settled by the OpenAI math release?” — asked at this session’s start, 2026-11-14 20:55 Asia/Tbilisi. Result: `PARTIAL-CLAIMED`; the full row is not claimed by these candidates.
