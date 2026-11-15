# T144 literature verification log

Task: “Verify: has open problem T144 been settled by the OpenAI math release?” Received 14 November 2026 (Asia/Tbilisi; prompt gives no clock time).

## 1. Orientation and first source requests

- Read local startup instructions and compute_state.json; governor reports status `ok`. The task-specific restriction to this folder overrides shared-brain/checklist/mesh writes; none were made. No git or subagents used.
- Commands: `OMP_NUM_THREADS=1 nice -n 15 pwd`, `OMP_NUM_THREADS=1 nice -n 15 rg --files ...`, and `OMP_NUM_THREADS=1 nice -n 15 /bin/cat .../brain_startup.md .../compute_state.json`. Sandbox reports `nice: setpriority: Operation not permitted`; the short read-only commands completed. No computation or persistent process was started.
- Web tool: opened all three candidate GitHub folder URLs exactly as supplied. All returned `Failed to fetch ...: Cache miss`, so no theorem text has yet been read.
- Discovered connected GitHub read-only fetch/search tools as an alternative source route. Next: request raw preprint files and repository metadata, and search the web.

## 2. Candidate folders accessible through GitHub connector

- Read-only `github_fetch` opened `/repos/openai/math/contents/preprints/<each supplied folder>` successfully. Each contains README.md, build/, and paper.pdf; the first two PDFs are about 0.8 MB.
- `web.run` searched `site:github.com/openai/math Anderson "2026"`, `"Absolutely Continuous Spectrum" "Weak Disorder" Anderson OpenAI`, and `"Fixed-energy universality" "weak Anderson"`.
- Search returned candidate source sections, two possible arXiv follow-ups (2609.06987 and 2610.11611), expositions, and independent review repositories. These are leads only until opened; no claim of expert validation follows from the snippets.

## 3. Opened actual preprint sources

- `github_fetch` opened all three `build/paper.tex` files and the first paper's `build/01-introduction.tex`; author is OpenAI on all three title pages. Dates are September 23, September 23, and October 5, 2026, respectively.
- First main theorem is purely absolutely continuous spectrum on an explicit interval just above the lower free edge, for iid uniform potentials and every fixed d >= 3. It contains no microscopic eigenvalue-statistics conclusion.
- Read build/ listings and identified the other introductions: `build/sections/introduction.tex` (2D) and `build/sections/01-introduction.tex` (random regular graphs).
- Opened repository root contents; README.md, LICENSE, history.md, lean/, overview.tex, and CONTENTS.md exist. No repository mutation occurred.

## 4. Main statements read and saved

- Opened both remaining introduction source files. Saved exact title-page sources and introductions under sources/AC-*, sources/PP-*, and sources/RRG-* using apply_patch. Main theorem labels: `thm:main`, `main:theorem`, `thm:main`.
- AC: iid uniform law, Z^d, d >= 3, fixed weak disorder, spectral purity on a restricted interval. PP: iid uniform law, Z^2, every fixed positive disorder, pure-point spectral type on the whole spectrum. RRG: uniformly random simple fixed-degree regular graphs with independent uniform diagonal disorder, fixed-energy full GOE point-process convergence in a compact clean-bulk interval.
- Opened and saved repository LICENSE (Apache 2.0), README, and history. The history through October 29 lists no Anderson-specific correction or withdrawal; README expressly cautions that unformalized results may contain issues.
- Provisional scope conclusion: none of the three states T144 for periodic boxes in Z^3. The RRG theorem matches the kind of limiting statistics but changes the graph ensemble; AC supplies a related spectral-type claim only.

## 5. Formalization scope and follow-up search

- Opened `lean/README.md`, `lean/formalization.yaml`, and `CONTENTS.md`. Catalogue family 219 is graph universality; family 261 is lattice localization/delocalization.
- Opened `lean/docs/261.md`: explicitly says the formalized supporting statement constructs the planar operator and identifies its spectral set [-4-h,4+h], and does NOT assert pure-point spectral type. `lean/docs/219.md` returned 404.
- Opened the three manuscript READMEs: no withdrawal/correction/version notice in any.
- Web searches: `"openai/math" "Anderson" error refutation`; `"Fixed-energy universality for weak Anderson disorder" arxiv comment`; `"Pure-Point Spectrum" "OpenAI" Anderson criticism`; `"Absolutely Continuous Spectrum" "OpenAI" "Anderson" correction`.
- Opened arXiv abstract pages 2610.11611 and 2609.06987, MathVet EXPLAINER, fortnow/AI-Papers README, and kusasyu36/openai-math-audit root. Detailed relevance is being checked; the September 7 arXiv item predates all three supplied manuscripts.

## 6. Follow-up relevance checked

- arXiv 2610.11611: Vojkan Jaksic and Yoram Last, *Extended States on the Bethe Lattice Revisited*, submitted October 8, 2026. Abstract explicitly discusses shortening the last boundary-positivity-to-purity step of the OpenAI lattice paper. This is a related follow-up, not a T144 theorem or a review of the full lattice proof.
- arXiv 2609.06987: Vojkan Jaksic, Yoram Last, Simone Warzel, *A Note on Extended States on the Bethe Lattice*, September 7, 2026. Predates the supplied preprints; tree AC and a conditional lattice criterion, not a later solution of lattice statistics.
- Opened MathDB's extended-states page and Plectis Atlas's PlanarAndersonSpectrum statement page. Opened actual Comparator challenge through GitHub connector; detailed formal statement is being checked against docs/261.md.
- MathVet EXPLAINER by Tejpal Virk explicitly flags family 261's spectral-set-only scope and describes its review as pre-referee/model-assisted; no mathematical refutation follows. fortnow/AI-Papers README lists complexity expositions, not Anderson expositions. Audit-repository README has no Anderson-specific entry.

## 7. Verdict saved; additional follow-ups found

- Wrote REPORT.md with verdict NOT-THIS based on the exact main statements, without judging proof correctness.
- Web searches additionally checked `"Anderson" "OpenAI" "level statistics" "2026"`, `"Wigner" "Anderson" "openai/math"`, the exact graph title outside GitHub, and `site:arxiv.org "Anderson" "OpenAI"`. No T144 solution appeared in these results.
- Opened full arXiv HTML 2610.11611v1. MathDB exposes a third-party AC Lean project by Yao Xu (cadamcat/anderson-ac-lean4) and November expositions; these must be inspected separately from the release's spectral-set-only formalization.
- Opened the actual PlanarAndersonSpectrum Comparator statement: it quantifies an operator on sites Z x Z and asserts its spectrum, with no spectral-type or level-statistics conclusion. Its `sorry` is the challenge placeholder, not evidence of a gap in the separate solution.

## 8. Third-party formalization and exposition

- Opened `cadamcat/anderson-ac-lean4/README.md` (Yao Xu) and `cadamcat/anderson-exposition/README.md` (Yao Xu, AI-assisted). The former claims a full AC formalization, with standard-axiom verification records; this is separate from the release's own supporting-only planar formalization. The stated target is spectral purity for the uniform model, not eigenvalue statistics.
- MathDB dates the third-party formalization's public release to October 14, 2026; the exposition identifies v1.0.2 on November 6. These are attributed publication/verification records, not builds performed here.
- Opened full Appendix B of Jaksic–Last's arXiv follow-up: it takes OpenAI's positive-probability boundary-imaginary-part estimate as input to a structural purity argument. It does not check the finite-volume construction or give GOE statistics.
- REPORT.md is already saved. Next: complete VERIFY.md and inspect the AC paper's certificate-to-resolvent bridge as the optional spot check. Also opened the graph paper's entropy section as a possible check target, but selected the lattice AC bridge because it concerns the matching lattice model.

## 9. VERIFY.md saved with full quotations and comparison

- Wrote VERIFY.md with all three main theorem environments copied directly from fetched introduction strings (no retyping), clause-by-clause comparison, follow-up sources, and a three-sentence replacement status.
- Opened and checked the later AC project's actual Challenge.lean: it concludes spectral purity/nonzero spectral weight on an interval, with no eigenvalue-statistics clause. Opened its verification record and the exposition article source. Verification successes are attributed reports, not checks rerun here.
- Opened arXiv 2611.08087: Jonathan P. Keating and Henrik Ueberschaer, November 5, 2026; abstract concerns eigenfunction multifractality for point-like bump potentials in d >= 5, not T144.
- Opened the AC source's `build/02-state.tex` and `build/09-spectral.tex` in preparation for the spot check. No heavy computation is needed.

## 10. Spot-check evidence saved

- Saved full AC state and spectral-readout sections, release Lean scope/challenge, and third-party AC challenge/verification record under sources/.
- Read the full spectral-readout proposition and proof. Re-derived the active-column lower bound, the low-rank spectral-cut comparison, the truncated-average inequality, and its constants. The calculation uses unconditioned own-site averaging, not independence after adaptive selection of A. No discrepancy found in this finite-dimensional bridge; the long certificate-construction argument is not audited by this check.
- Added targeted searches for the 2D paper's Lean/error/review record, graph theorem errors, Z^3 GOE claims in 2026, and Anderson/OpenAI refutations. Requested read-only issue searches on the primary repository to supplement general web searches.

## 11. Spot check appended; final search lead

- Appended the detailed spectral-readout spot check to VERIFY.md. Confirmed both noncommutative resolvent identities, rank/HS bound, positivity truncation, and the constants c_*/4 - 8 epsilon/lambda >= c_*/8. Checked the exponential finite-to-infinite-volume comparison against L_m and eta_m. This checks one transfer argument only, not the certificate proof.
- Repository issue searches for `Anderson repo:openai/math`, `"Absolutely Continuous Spectrum" repo:openai/math`, and `"Fixed-energy universality" repo:openai/math` all returned empty issue lists.
- A final search found Xujie Lai and Fan Yang's random-band-matrix paper. Opened arXiv abstract 2609.24426 (latest v4, November 8) and full HTML v3 (October 18). It is a band-matrix result, not T144; checking its explicit OpenAI comment for the follow-up record.
- Corrected two phrases in VERIFY.md: the AC theorem is an almost-sure spectral-type assertion; only writes, not reads, were restricted to this folder.

## 12. Final audit and completed deliverables

- Opened full arXiv 2609.24426v4. Xujie Lai and Fan Yang's November 8 introduction explicitly discusses both OpenAI lattice claims and a qualitative implication of the planar fractional-moment theorem; it neither refutes the claims nor establishes T144. Added this mathematical commentary to VERIFY.md. The v3 HTML has no OpenAI match; the added discussion is present in v4.
- Validation command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nice -n 15 python3 - <<'PY' ...` with a small standard-library-only read-only script. Exit 0. It verified each full theorem environment occurs exactly once in VERIFY.md and exactly matches its saved source; REPORT.md has the verdict plus three reason lines; the replacement status has three sentences; the spot-check section exists.
- The script read inherited niceness as 20. Thus the sandbox's `setpriority` denial prevented changing it to 15, but the actual process already had an even lower scheduling priority. No heavy compute, builds, GPU, ML workers, or persistent processes were used.
- Deliverables: REPORT.md; VERIFY.md with three exact main statements, scope table, opened follow-ups, three-sentence status, and bounded spot check; LOG.md; 15 source snapshots/license files in sources/.
- Final result: NOT-THIS. Retain T144 as open; the inspected release claims do not include GOE level statistics for periodic three-dimensional lattice boxes. Proof correctness remains unjudged. All writes stayed in this folder; no git, push, account creation, posts, email, or subagents.
- Task: “Verify: has open problem T144 been settled by the OpenAI math release?” — 14 November 2026, Asia/Tbilisi; request clock time was not supplied.
