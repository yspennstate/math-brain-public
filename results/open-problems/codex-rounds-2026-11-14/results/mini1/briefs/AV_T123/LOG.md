# T123 verification log

Task: “Verify: has open problem T123 been settled by the OpenAI math release?”
Started: 2026-11-14 21:06 Asia/Tbilisi (UTC+04:00).

## 1. Orientation and access checks

Read the local directory listing, compute state, and agent-mesh protocol using a short Python command launched with `OMP_NUM_THREADS=1 nice -n 15`. The folder initially contained `PROMPT.md`, `codex.log`, and `run.pid`. Compute state was `warn`, with CPU saturation; no heavy compute is planned. The sandbox prints `nice: setpriority: Operation not permitted`, even for this lowering-priority request. Commands remain tiny, single-threaded, and prefixed as requested; the priority change cannot be enforced here.

The task's specific instruction forbids edits outside this folder. Accordingly, no mesh registration, checklist update, brain-log write, git operation, or external posting is performed. Read-only orientation is allowed.

Opened all three supplied GitHub folder URLs with the web tool. Each returned `Failed to fetch ...: Cache miss`; no paper text was obtained. Next: try raw TeX/PDF and repository metadata directly, then search for independent records.

## 2. Raw paths and initial search

Read startup memory index, identity, and writing-method cards directly without running the logging brain CLI. Web opens of each candidate's `paper.tex` and `build/paper.tex` returned 404. The repository root raw `README.md` opened successfully. Searches: `site:github.com/openai/math percolation`, exact nonuniqueness title, and exact no-percolation title.

Search results include an OpenAI abstract explicitly claiming `p_c < p_{2→2} ≤ p_u` for the nonuniqueness paper. This is potentially strong enough for T123; a verdict cannot be based on title similarity alone. Results also identify a rendered manuscript at Plectis Atlas, community pages, the repository `history.md`, a Lean critical-percolation file, and a site-percolation follow-up by Yan Ru Pei. These are leads, not yet checked evidence.

A short process-priority inspection using `/bin/ps` was blocked by the sandbox; because the script stopped there, its subsequent planned HTTP request did not run. No priority or remote response is inferred from that failed command.

## 3. Manuscript render and stronger claim

Opened the full Plectis Atlas rendering of the nonuniqueness manuscript. The rendering explicitly warns that its numbering/text can differ from the PDF. Its Theorem 1.1 claims bounded critical connection operator and `p_c < p_{2→2} ≤ p_u`; its critical-laws corollary explicitly states the finite triangle diagram, susceptibility exponent 1, order-parameter exponent 1, and critical cluster-size tail exponent 1/2. This appears to cover the whole row, subject to checking the original manuscript.

Raw PDF URLs exist but the web parser rejects their `application/octet-stream` content type. GitHub blob PDF pages open but expose only metadata (560 KB for criticality, 416 KB for cubic lattice), not the PDF text. The Atlas TeX-source link points to the `build/` directory at commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, not a file named `paper.tex`. The pinned directory and PDF links did not load. Direct Python `urllib.request.urlopen` of GitHub API failed DNS resolution; no network download was obtained through the shell.

Opened repository `README.md` and `history.md`: the release identifies the manuscripts as model-produced raw research data; the history lists corrections and withdrawals through 29 October, with no named percolation correction in that file. Opened linked MathVet CSV and cert-machine JSON GitHub pages, but their content was not exposed; these are not yet verified formalization evidence.

## 4. Original TeX located

Successful original source opens: `.../Nonuniqueness-.../build/main.tex` and `.../No-percolation-.../build/main.tex`. Both identify the author as OpenAI and the date as September 24, 2026; both input `sections/introduction`. The nonuniqueness source also inputs `sections/conclusion` and `sections/consequences`. Cubic `build/main.tex` was 404; its README and full Atlas rendering opened, and its TeX-source link is being followed to find the actual filename.

Opened `lean/README.md`, `lean/formalization.yaml`, and `lean/ComparatorChallenges/README.md`. The catalogue includes the cubic paper; a search for the exact general criticality title finds no entry. These absences alone do not show that the results lack formalizations, since family/statement names may differ. No Lean compilation is attempted.

## 5. Original statements, formalization, and follow-up leads

Opened the original `build/sections/introduction.tex` for nonuniqueness and general criticality, and nonuniqueness `sections/consequences.tex`. Read the exact main theorem in each introduction. Read the nonuniqueness critical-laws corollary in the original introduction: the full triangle/exponent conclusion is explicit, with two-sided `asymp` bounds rather than limiting amplitudes.

Opened `lean/docs/214.md`, `lean/docs/213.md`, the three relevant Comparator JSON configurations, `lean/ComparatorChallenges/BenjaminiSchramm.lean`, and all three solution `Main.lean` files. The family-214 challenge explicitly encodes the actual Bernoulli law, connection kernel, triangle sum, and mean-field laws; solution `Main.lean` states unconditional theorems by invoking imported inputs. Comparator challenges contain intentional `sorry` placeholders; they are specifications, not the supplied solution. The YAML catalogue omits names that do have separate scope notes and Comparator files.

Searched exact titles with `arxiv`, `error`, `gap`, `review`, plus `OpenAI nonamenable triangle percolation`. Opened the Mathcommunity family-214 page (automatically collected notes labelled unreviewed), the original MathVet fidelity CSV, the original Proofs and Prompts reactions page, and Yan Ru Pei's Hexagon landing page. The latter identifies a November 10, 2026 site-percolation adaptation, explicitly reliant on unrefereed inputs and with no formal verification. The Latent Seminar URL opened but exposed no readable text. Raw cubic source filename guesses and GitHub API listing failed; these failures are access failures, not evidence of a missing paper.

Following Mathcommunity's direct PDF link successfully opened the actual 53-page nonuniqueness preprint on that mirror. This provides the PDF itself, independently of the Atlas HTML conversion. Next: open the other two mirrored PDFs, read exact statements, and save the verdict.

## 6. Verdict saved before optional proof check

Created `VERIFY.md` and `REPORT.md`. Verdict: `SOLVED-CLAIMED` for the entire T123 statement, on the strength of original Theorem 1.1 and its explicit critical-laws corollary. The report distinguishes statement coverage, supplied formal artifacts, external reported automated checking, and refereed acceptance. The exact main statements from original TeX are saved; cubic wording is provisionally quoted from the full Atlas rendering with an explicit access qualification.

Read MathVet rows 213 and 214: both say full fidelity and sandboxed Comparator pass; family 214 includes the critical laws. Read Tasmin Chu's and Inhyeok Choi's comments in the original Proofs and Prompts post; these are reactions, not detailed reviews. Opened Tom Hutchcroft's arXiv:1904.05804v2 landing page and full HTML to independently check the established operator-to-triangle/exponent implication. No exact-title arXiv version or specific refutation was identified. Direct guessed mirror URLs for the other PDFs failed; now following the actual links on their opened landing pages.

## 7. All three PDFs opened; spot check selected

Clicking the actual Mathcommunity PDF links opened the 20-page cubic preprint and the 42-page general criticality preprint. Their Theorem 1.1 texts agree with the saved statements. The nonuniqueness PDF confirms Theorem 1.1 (printed p. 3), Corollary 1.3 (printed p. 6), and the proof of the triangle implication (printed p. 49). Screenshot requests for three pages returned cache misses; the general criticality page screenshot request succeeded. PDF text extraction, not an assumed image reading, is the basis of the quotations.

Opened Olle Häggström's original 7 October post; it points to the percolation papers without a detailed mathematical review. Opened the arXiv record and full HTML of Omer Angel, Daniel de la Riva, Christoforos Panagiotis, and Yuliang Shi, arXiv:2610.35233v1 (26 October 2026), as a later citation lead.

After saving REPORT.md, opened the original nonuniqueness `sections/deformation.tex` in full relevant ranges, including all template definitions, deletion estimate, and the two-cluster lemma. Selected Lemma 7.7 (Two distinct exterior clusters), the step supplying the product term in the susceptibility-decrease estimate, for a careful conditional-exposure and error-bound check. No numerical simulation or Lean build is needed for this local check.

Read back the saved files. Found escaped mathematical notation damaged by the first writing command (including one control character in the comparison table). A clean rewrite using literal strings will repair presentation before completion.

## 8. Final literature and local lemma findings saved

Opened the actual 60-page Yan Ru Pei site-percolation preprint, confirming the author name and explicit adaptation of the OpenAI proof. Read Section 1.2 of Angel–de la Riva–Panagiotis–Shi in full HTML: it calls the general criticality result an OpenAI claim, not a theorem independently reviewed there. Opened MathVet's review README: the review is pre-referee; the second-reader/referee fields are pending. Its README revision and the current table's linked release revision differ, and VERIFY.md records this limitation.

Checked Lemma 7.7 by re-deriving the conditional-exposure identity, the deletion error using the full neighbor set, the Harris comparison, the three-leg tree bound, and the final constant `1 + 2d/p_c`. No discrepancy was found in this local calculation; no conclusion about the entire proof is drawn.

Rewrote VERIFY.md with literal mathematical notation, replaced the provisional cubic rendering quote with the confirmed PDF theorem, added exact printed page numbers, completed primary-source follow-ups, and appended the spot check. One attempted literal-string rewrite failed JavaScript parsing before any execution or mutation; the corrected command succeeded. REPORT.md remains saved with the full-statement SOLVED-CLAIMED verdict.

## 9. Final artifact audit

At 2026-11-14 21:17 Asia/Tbilisi, ran a tiny Python read-back under `OMP_NUM_THREADS=1 nice -n 15`. Verified that REPORT.md has the prescribed verdict prefix and exactly three reason lines; VERIFY.md has both exact original-TeX theorem blocks, the PDF-confirmed cubic theorem, the comparison table, follow-ups, recommended two-sentence status, and Spot check. Confirmed no stray control characters in any deliverable and no stale provisional access qualification. Only LOG.md, VERIFY.md, and REPORT.md were created by this task; no git command or external write was used.

Task complete: “Verify: has open problem T123 been settled by the OpenAI math release?” — requested/start clock 14 November 2026, 21:06 Asia/Tbilisi; result SOLVED-CLAIMED for the whole statement, with no judgment on the correctness of the full proof.
