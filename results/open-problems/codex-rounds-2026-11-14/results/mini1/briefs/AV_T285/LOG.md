# T285 verification log

Task received: 2026-11-14, approximately 21:14 Asia/Tbilisi (local session log time).

## 1. Orientation

Read the working directory, existing file list, compute state, and mesh protocol with `OMP_NUM_THREADS=1 nice -n 15` commands. Compute state reported `ok`; only PROMPT.md and runner files existed here. The sandbox printed `nice: setpriority: Operation not permitted`; no heavy computation will be used. Started the required brain recall and interrupted it after it did not immediately finish. The task-specific rule forbids writes outside this folder, so mesh/checklist/brain updates outside it are not attempted. No git commands or subagents used.

Next: open the supplied preprints with the web tool and save exact theorem text here.

## 2. First web pass

`web.run open` on all three supplied GitHub folder URLs failed with cache misses; raw top-level `paper.tex` URLs returned 404. The repository root opened successfully. `web.run search_query` used the three exact titles and `site:github.com/openai/math "committee"`. Search surfaced an HTML transcription of the scheduling paper, a scheduling follow-up claiming a smaller exponent, and a normalized-volume exposition. These are leads, not yet treated as opened papers. Read-only GitHub connector retrieval is the next fallback for the actual source folders. Brain recall completed and returned orientation memory names; no further brain command is needed for this narrow verification.

## 3. Actual repository folders opened

Read-only `github_fetch` opened the three supplied folder contents and repository root. Each candidate contains `README.md`, `build/`, and `paper.pdf`; the TeX is consequently sought under `build/`. PDF sizes are approximately 247 KB (scheduling), 627 KB (geodesics), and 383 KB (volume). Root includes `lean/`, README.md, history.md, CONTENTS.md, and overview.tex; no root `docs/` directory was listed.

## 4. Main theorem extraction and saved verdict

Opened all three `build/paper.tex` files, each candidate README, and the geodesic paper's `build/sections/introduction.tex`. All name OpenAI as author and September 24, 2026 as date. Extracted the first theorem environment verbatim into VERIFY.md. Scheduling: exact optimum in O((L+2)^150020) time; geodesics: infinitely many prime images for every smooth metric on S^n, n >= 2; volume: <=162 for singular boundary-zero klt fourfolds, equality iff ordinary double point. None concerns the T285 learning model. Wrote REPORT.md with NOT-THIS and the requirement-by-requirement comparison in VERIFY.md.

Opened repository README, history, lean/README.md, lean/formalization.yaml, and lean/docs directory listing. The YAML keyword pass did not list these three titles (this is not sufficient to infer that no Lean proof exists). Web searches for each subject with OpenAI/error/arxiv returned follow-up leads; these will be checked directly. No correctness judgment made.

## 5. Follow-up sources opened

Opened arXiv:2610.21054 abstract page: *Infinitely many closed geodesic images on simply connected compact rank-one symmetric spaces*, Zhiqi Chen, Shaoqiang Deng, Hui Zhang, submitted 15 October 2026. Opened David Niedbala Giraudin's three-page *Three-machine unit-job scheduling in time O((L+2)^276)*, dated 3 November 2026, at https://hexagonmath.org/pdf/2611.00060v1; it claims a reduced exponent and expressly does not reprove correctness. The Borowiecki PDF lead timed out. Opened AI Proved What's scheduling exposition (last checked 30 October), which reports a Lean artifact but says it has not run the check; this is not an expert/referee certification. The volume exposition URL failed to open and is not used as evidence.

Opened lean/docs/124.md: it explicitly describes a formalisation of the full scheduling algorithm. lean/docs/037.md returned 404. Opened CONTENTS.md, lean/OAI.lean and Comparator README; a catalogue omission must not be read as proof absence. The manuscript map has no committee/Aubin match in the keyword pass. All actions were read-only external fetches; local files only were written.

## 6. Formalisation and later literature confirmed directly

Opened `lean/ComparatorChallenges/ThreeMachine.lean`, `ThreeMachine.json`, and `lean/OAI/Computability/Scheduling/Main.lean`. The comparator template has a `sorry`, as expected for a challenge; the JSON points to the separate solution module, whose `main_theorem` has a proof body. No Lean build or whole-import audit was run. CONTENTS.md associates scheduling with family 124 and a Lean scope note; geodesics is family 345 and volume family 037 without such links. The formalization YAML omits scheduling despite its separately present artifacts.

Opened arXiv HTML for 2610.21054: Section 1.3 explicitly credits OpenAI's sphere paper as antecedent and strategy source, while claiming a proof that does not assume its theorem or lemmas; acknowledgements disclose Codex assistance. Opened arXiv:2611.09392 abstract: Klaus Jansen, *Precedence Constraint Scheduling on a Fixed Number of Machines*, 6 November 2026, claims exact polynomial-time scheduling for every fixed m >= 3. Opened community pages for the volume and scheduling papers: volume has no contributed notes and only automated unreviewed links; scheduling records an October 27 reference/cross-reference revision. Opened Latent Seminar's October 7 geodesic exposition, which explicitly disclaims independent full verification. No opened source established refereeing or a refutation of these three papers.

For the optional spot check, opened scheduling `build/descriptions.tex` and selected Lemma 8.1 (global child predicates), the step eliminating dependence on ancestor interval descriptions. Opening its boundary/list/separator dependencies next. REPORT.md already exists.

## 7. Search completion and spot-check dependencies

`web.run search_query` searched committee-machine/Aubin/specialization/K-squared/low-degree and committee-machine/OpenAI/threshold combinations. It returned the original Aubin et al. paper and unrelated material, not a matching release result. Opened the HTML of Jansen's arXiv:2611.09392, including its explicit relation to the OpenAI construction. Opened scheduling `construction.tex`, `boundary.tex`, `lists.tex`, `separators.tex` and reread the main file's cone and sentinel definitions. Re-derived both inclusions in Lemma 8.1 under its stated construction invariants; details will be appended under Spot check. No full-paper proof certification is inferred.

GitHub issue searches initially returned 422 because the connector requires `is:issue` or `is:pull-request`; retrying with `is:issue`. Attempts to follow two exposition/comment links using URL-based click references failed; retrying with the returned web references. All failed accesses are recorded rather than counted as opened sources.

## 8. Findings saved

Corrected GitHub issue searches each returned zero hits. Successfully opened NotOscarWilde's original Hacker News comment and the volume OpenAI Math Digest guide. Opened Aubin et al.'s original arXiv abstract and author list. Appended all follow-up findings, links to actually opened sources, the two-sentence recommended status, and the conditional Lemma 8.1 spot check to VERIFY.md. A JavaScript quoting error prevented the first append from executing; the corrected append succeeded. Distinguish present Lean artifacts from rerun verification, AI exposition from expert review, and no located report from proof that none exists. Next: final audit of saved files and exact quotations.

## 9. Final audit — 2026-11-14 21:20:47 Asia/Tbilisi

Ran a small standard-library-only file audit with `OMP_NUM_THREADS=1 nice -n 15 python3` (the sandbox again denied changing priority; the read-only check finished in under one second). Compared each saved TeX theorem environment against the directly fetched source strings: exact matches for all three. REPORT.md has the required NOT-THIS first line and three reason lines. VERIFY.md has 115 lines, all requested sections, no placeholder text, and a two-sentence recommended status. Checked load-bearing distinctions again: processors versus hidden units, sphere/complex dimensions versus feature dimension, scheduling upper bound versus learning lower bound. The spot check is explicitly conditional and gives no whole-proof correctness verdict. Completed VERIFY.md, REPORT.md, LOG.md; no git, posting, accounts, subagents, or heavy computation used.
