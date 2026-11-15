# T095 verification log

Task received: “Verify: has open problem T095 been settled by the OpenAI math release?” Session date: 2026-11-14; first clock reading 17:04:21 UTC (21:04:21 Asia/Tbilisi).

## Step 1 — scope and initial access

- Read the supplied task and working-folder listing. Existing files: PROMPT.md, codex.log, run.pid. No git commands used.
- Commands: `OMP_NUM_THREADS=1 nice -n 15 /bin/pwd`, `/bin/ls -la`, `/bin/cat ~/.claude/compute/compute_state.json`, and narrow startup-memory location checks. Compute state reported `status: ok`, `mode: owner_away_open`.
- Every shell invocation requested `nice -n 15`, but the sandbox printed `nice: setpriority: Operation not permitted`; these were small read-only commands. No heavy computation is planned.
- The later task-specific order confines all writes to this folder, so global brain/checklist/mesh commands that write elsewhere are excluded.
- Web-tool opens of all three supplied GitHub directory URLs returned “Failed to fetch … Cache miss”. This is an access failure, not evidence about the mathematical claims. Next: use the connected GitHub read-only tools and raw files, then web searches for follow-ups.

## Step 2 — repository access and first follow-up searches

- Read-only GitHub `fetch` successfully listed all three supplied folders and their `build/` directories. Each contains `build/main.tex` and section sources; the FPP folders contain `main.pdf`.
- Opened repository README.md and Lean scope notes `lean/docs/212.md` and `lean/docs/281.md` with GitHub `fetch_file`. Family 212 explicitly describes differentiability for positive Gamma laws (including exponential), and excludes strict convexity from the selected formal statements. Family 281 explicitly excludes convergence of QAOA circuit energies from its selected value identities.
- Web searches used the three exact titles, plus `arxiv error`, `OpenAI error review`, and `"openai/math" "212" "error"`. Results include family catalogues and expositions, plus possible later arXiv papers; these are leads only until opened. No proof verdict inferred from search snippets.
- Scope comparison still pending direct theorem text. The Gamma extension is relevant to T095 but would not cover every continuous law.

## Step 3 — exact theorems saved; provisional deliverables written

- GitHub `fetch_file` opened all three `build/main.tex` files and their introduction sections. All three name OpenAI as author. Dates: September 24, 2026 (both FPP papers); September 25, 2026 (QAOA).
- Copied the exact theorem environments into VERIFY.md and saved all three introduction sources locally. The shape paper has Theorem 1.1 for exponential weights and Theorem 1.2 for every positive Gamma shape/rate. The no-bigeodesics theorem matches the general law assumptions but has no differentiability conclusion. QAOA concerns an SK energy limit.
- Wrote REPORT.md with PARTIAL-CLAIMED and the covered subclass. Wrote the clause-by-clause comparison and a three-sentence replacement status in VERIFY.md. Follow-up section remains to be completed.
- Opened `history.md` and both family-212 Comparator challenge sources. History has no family-212 repair/withdrawal entry. Challenge statements cover Gamma differentiability, not arbitrary continuous laws.
- Opened arXiv abstracts 2610.42124 (Scott Armstrong, Ahmed Bou-Rabee; October 30, 2026) and 2611.05446 (Dylan Herman, Shouvanik Chakrabarti, Junhyung Lyle Kim, Guneykan Ozgul; November 3, 2026), following citation leads. They are different papers, not arXiv versions of the supplied preprints; full-text citation context remains to inspect.
- Opened the Plectis Atlas family-212 page, which links primary external comparison/checking reports. These reports will be opened rather than inferred from the catalogue.

## Step 4 — version notes and broader searches

- Opened the three manuscript README files: all confirm the author/date and carry no revision or withdrawal notice.
- Web search queries included each FPP title restricted to arxiv.org, plus `"first passage" "OpenAI" Damron error` and `"first passage" "OpenAI" Hoffman review`. No same-title arXiv version or named specialist refutation was identified in this pass. Search results instead point to expositions, scope audits, and unrelated papers.
- Followed Atlas links to primary MathVet and cert-machine report URLs and the formal proof `lean/OAI/Probability/FirstPassage/BoundaryCurve.lean`. GitHub HTML did not expose all report data; next read the actual raw report files through the GitHub connector.
- GitHub code search found the separate Gamma proof library at `lean/OAI/Probability/GammaPassage/`.

## Step 5 — primary scope audits and actual proof files

- Opened the actual exponential solution `lean/OAI/Probability/FirstPassage/BoundaryCurve.lean`: it supplies `manuscriptMain` using the actual time constant, differentiability, unique supports, and boundary charts. Also opened the Gamma library's `Main.lean` import catalogue and `lean/README.md`. No Lean compilation was attempted.
- Opened MathVet's `reviews/openai-math/fidelity-table.csv` at commit 14c7f918cd336d0da03a02aae5a0eed4a429d4db. Its family-212 row reports `partial` and `comparator-sandboxed-pass`, distinguishing Gamma differentiability from the absent no-bigeodesics and strict-convexity conclusions.
- Opened Carlos Toledo's cert-machine `certs/openai-math-statements.json` at commit 9814e4c06281e34a113ce853d7d99ccce160b750. The family-212 record likewise says the selected statements are narrower and maps the Gamma differentiability clause explicitly to GammaPassage.
- Opened full HTML of arXiv:2610.42124v1 and arXiv:2611.05446v1. Armstrong–Bou-Rabee's introduction says exponential strict convexity/differentiability were recently announced; this is a citation, not proof certification. The SK paper cites the QAOA preprint and separately retains related support/value properties as hypotheses.
- Opened all six differentiability section sources of the shape paper after REPORT.md was saved. Their lemma/proposition statements are now available for choosing one load-bearing spot check.

## Step 6 — chosen spot check and final search leads

- Chose the shape paper's “Arbitrary endpoints” lemma (`df:gr:variable-endpoints`) as the load-bearing lemma for the differentiability claim relevant to T095: it upgrades prescribed-column crossing estimates to paths whose endpoints depend on the environment. Read its complete proof and the simultaneous-grid connection proof; saved endpoints.tex locally. Checked the extension errors, the possibility of backward endpoint order, the number of coarse-column tests, and the order of limits. Findings will be appended under Spot check.
- Opened actual Gamma solution `lean/OAI/Probability/GammaPassage/Differentiability.lean`; it derives the target from no-corner and actual-time-constant inputs. Opened `lean/formalization.yaml` and Comparator instructions. An attempted path `lean/ComparatorConfigs` was absent; actual configs are under ComparatorChallenges and will be opened there.
- GitHub read-only issue search `repo:openai/math "first-passage"` returned an empty issue list; this is a search result, not proof that no criticism exists.
- Final web searches added QAOA's exact title restricted to arxiv.org, the FPP titles with error/refutation, and GammaPassage with error. They surfaced two further leads: a MathDB conditional moment-removal claim and arXiv:2611.03739, “Reasoning is topologically simple”. These will be opened before deciding whether they matter.

## Step 7 — checking reports and later-source context

- Opened both actual Comparator JSON configurations. They permit only propext, Quot.sound, Classical.choice and list no definition holes; the repository configs disable nanoda.
- Opened cert-machine's primary `certs/openai-math-kernel.json` at the pinned audit revision. Its GammaPassage and PlanarFirstPassage rows report Comparator exit 0 and acceptance by both Lean and nanoda, dated October 10, 2026. This is a reported external rerun; no local rerun was performed. The recorded runs exceed the present task's 1 GB ceiling, reinforcing the decision not to compile locally.
- Opened arXiv:2611.03739, “Reasoning is topologically simple”, by Chris Kapulkin and Nathan Kershaw (submitted November 2, 2026), to distinguish a possible corpus-matching discussion from an FPP theorem review.
- Opened the MathDB page for the bigeodesics conjecture. It links a conditional extension on Zenodo, says it relies on the OpenAI proof machinery, and distinguishes its selected Lean lemmas from the full probability claim. Followed links to the actual manuscript/record next; no mathematical reliance on the summary.

## Step 8 — follow-ups and spot check appended

- Opened Myeongjin Kang's author-deposited Zenodo record 23647122 (October 25, 2026) and MathDB abstract 2610.00759. Both explicitly describe the result as conditional on the OpenAI no-bigeodesics theorem and proof inputs. The PDF download URL returned a Unicode decoding error in the web reader, and its query-free URL was inaccessible; no theorem or proof quotation is taken from that unread PDF. Its deposited abstract was readable and suffices to identify it as a different, conditional claim.
- Read the relevant full-HTML passages in Kapulkin–Kershaw: their no-bigeodesics title occurs in the appendix's text-corpus pairing table. This is not a proof review or refutation. The arXiv author page names Chris Kapulkin; the HTML title page expands that name to Krzysztof Kapulkin.
- Confirmed main's snapshot via read-only GitHub commit API: 4eaee87548250b2682affda7d05d947c05554bae, October 30, 2026.
- Appended primary source/checking links, later papers, the bounded negative search finding, and the detailed arbitrary-endpoint spot check to VERIFY.md. No local Lean builds or numerical experiments were run.
- Two exact-line patch attempts failed because the target sentence was embedded in a longer paragraph; they made no changes. The subsequent append used the full matching paragraph and succeeded.

## Step 9 — final artifact audit

- Removed the preliminary follow-up wording and updated REPORT.md to mention the external checking records with their limited scope.
- A direct `rg` check using `/usr/bin/rg` failed because that executable path does not exist. Used a short, one-thread Python text audit instead, under `OMP_NUM_THREADS=1 nice -n 15` with a 30-second alarm; no heavy computation.
- Audit compares every main theorem environment in all three saved introduction sources byte-for-byte with VERIFY.md, checks REPORT.md's verdict and three reason lines, checks local source links, and checks that the recommended replacement status is three sentences.
- Audit passed (exit 0): 2 exact theorem blocks for the shape paper, 1 for no-bigeodesics, 1 for QAOA; REPORT.md has the required first line plus three reason lines; all local source links exist; replacement status has three sentences. The sandbox again refused the requested niceness change; the text audit completed immediately.
- Completed deliverables: VERIFY.md, REPORT.md, LOG.md, and four local source excerpts. Final verdict: PARTIAL-CLAIMED for every positive Gamma shape/rate, including exponential; no full T095 claim located. No gap identified in the checked endpoint-extension reduction conditional on its earlier inputs. No writes outside this folder, git commands, external posts, account creation, subagents, builds, simulations, or heavy computation.
