# T304 verification log

Task received: 14 November 2026, 21:15 +04 (Asia/Tbilisi). Verify whether the OpenAI math release settles “The query complexity of sampling from strongly log-concave distributions.”

## Step 1 — orientation

- Read the task and folder restrictions. No subagents, git operations, external writes, or messages will be used. The task-specific restriction to this folder precludes shared brain, checklist, and mesh mutations.
- Command: `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'pwd; rg --files -g "AGENTS.md" -g "LOG.md" -g "VERIFY.md" -g "REPORT.md"; date "+%Y-%m-%d %H:%M:%S %Z"; ls -la ~/brain-views; cat ~/.claude/compute/compute_state.json'`.
- Output: correct task directory; no matching existing deliverables; 2026-11-14 21:15:11 +04. Compute governor reports `status: ok`, `mode: owner_away_open`.
- Environment limitation: `nice` printed `setpriority: Operation not permitted`; only short read-only commands ran. No heavy computation is planned.
- Discovered available web and GitHub read tools for primary-source retrieval.

## Step 2 — source discovery

- Web `open` attempted all three supplied GitHub folders: each returned a cache miss. GitHub connector `fetch` successfully opened repository metadata; repository exists, default branch `main`, issues and discussions disabled, last push shown as 2026-10-30.
- Located startup memory using read-only `rg --files` and read its opening sections. No brain scripts were run because recall itself may write logs outside the permitted folder.
- Requested all three folder listings through the GitHub connector, and ran web searches for each exact or near-exact title. Results are recorded in subsequent steps.

## Step 3 — manuscripts and release documents opened

- GitHub connector opened each candidate's `README.md` and `build/main.tex`. All three papers list author **OpenAI** and the dates supplied in the task. Their text is split into `build/sections/`; fetching the introductions next.
- Saved the opened source files and release documents in `sources/`, preserving repository-relative paths.
- Opened repository `README.md`, `history.md`, `lean/README.md`, `lean/formalization.yaml`, `lean/ComparatorChallenges/README.md`, and the `lean/` listing. Root `docs/` returns 404; documentation is under `lean/docs/`.
- The first paper's abstract claims a bound for known-minimizer, Hessian-between-I-and-2I targets at fixed TV error 1/10; its epsilon is a dimension exponent. The second concerns total Boolean functions and bit queries. The third concerns logarithmic Sobolev inequalities.
- Web searches returned exposition/atlas leads at lowrank.github.io, wcook04.github.io, closedform.nishachay.tech, and emergentmind.com. These are leads until actually opened. A November Bayesian-estimation paper also appeared as a possible follow-up to the Sobolev paper.

## Step 4 — theorem statements saved and provisional verdict written

- Opened all three original introduction TeX files, read their model definitions and main theorems, and saved copies under `sources/`.
- Wrote `VERIFY.md` with each main theorem copied exactly as TeX. Wrote `REPORT.md` with PARTIAL-CLAIMED verdict and explicit scope limits before continuing follow-up work. An initial patch failed because theorem lines lacked patch prefixes; corrected the patch, with no source changes lost.
- Key distinction: the first theorem's epsilon quantifies the dimension exponent; sampling error is fixed at TV 1/10. Its normalized curvature class and supplied minimizer do not match general κ and accuracy parameters in T304.
- The other two main theorems have different quantities: Boolean bit-query complexity and an entropy/Dirichlet-energy inequality.

## Step 5 — follow-up search and formalization retrieval

- Web searches: each exact title with `error OR correction OR arxiv OR review`. Opened arXiv:2611.05813, Plectis Atlas LogConcaveQuery statement page, and two lowrank exposition URLs (the latter open with zero readable lines).
- arXiv:2611.05813 exists and is dated 4 November 2026. Retrieved the full abstract next rather than relying on the supplied note.
- Search found candidate follow-ups arXiv:2611.05831 (Bayesian estimation and functional inequalities) and arXiv:2611.15849 (parallel log-concave sampling). Opened their abstract pages next to verify titles, dates, and authors.
- Requested the original Lean scope note, Comparator challenge/configuration, implementation, and sampling/lower-bound source files. Also checked the candidate family 093 and 284 scope-note paths.

## Step 6 — later papers and Lean scope checked

- Opened full HTML of Huanjian Zhou and Taiji Suzuki, *Towards the Query Complexity of Sampling under Strong Log-Concavity and Log-Sobolev Inequalities*, arXiv:2611.05813v1 (4 November 2026). Its introduction explicitly combines the OpenAI upper bound with its own lower bound and calls the resulting regime super-polylogarithmic and subpolynomial. It says the lower bound holds with mode and mean known to be zero.
- Opened abstract and full HTML of Evan Dogariu, *Sharp Lower Bounds for Parallel Log-Concave Sampling*, arXiv:2611.15849v1 (11 November 2026). Its related-work paragraph cites the OpenAI upper bound and Zhou–Suzuki's lower bound; its own result is about parallel depth/width, not a matching sequential total-query rate.
- Opened abstract and full HTML of Shuchen Li and Ilias Zadik, *Functional inequalities from the fundamental limits of Bayesian estimation*, arXiv:2611.05831v1 (4 November 2026). It explicitly distinguishes its dimension-dependent log-Sobolev bound from OpenAI's claimed dimension-free one.
- Opened all three mathcommunity/oai-math-revised candidate pages, plus Closed Form's sampling exposition and Plectis Atlas's statement page. The community pages' named notes are empty; automatically collected notes are expressly unreviewed. Following primary-source links before using their claims.
- Opened `lean/docs/139.md`, Comparator challenge and JSON, and `OAI/Probability/LogConcave/Main.lean`; saved them in `sources/`. Scope matches the fixed-error theorem, and the solution module has an explicit proof combining upper, lower, and exponent results. The challenge's `sorry` is its placeholder, not evidence of a missing solution proof. No Lean compilation was run.
- `lean/docs/093.md` and `lean/docs/284.md` return 404; the full `lean/docs/` listing has neither entry. The formalization catalogue contains LogConcaveQuery and no matching entries for the other two candidates.
- Read the sampling proof's normalization and query model: its large-dimension construction uses gradients; the bounded-dimension fallback also uses values. Thus the stated theorem is a joint value-and-gradient-oracle theorem.
- Attempted a short process-priority read; sandbox disallows `ps`. No heavy computation or proof compilation has been attempted.

## Step 7 — scope cross-check and targeted review search

- Read Zhou–Suzuki's results table and surrounding text: constant TV error 1/10, condition number 2, and supplied zero mode are explicitly consistent with OpenAI's model. Its super-polylogarithmic lower bound does not contradict a subpolynomial upper bound.
- Read Dogariu's explicit related-work paragraph and Li–Zadik's references to the Sobolev claim. These are later mathematical discussions, not referee reports or full proof certificates.
- Read the full standalone-accuracy induction in the sampling preprint's implementation section, alongside the Gaussian-center absorption lemma and corresponding Lean noisy-center error source. The key issue for a spot check is whether restored Gaussian seeds have the correct conditional law before the recursive accuracy guarantee is invoked.
- Ran additional web searches for sampling/Chewi/error/proof, quartic/Aaronson/review/error, subgaussian/Sobolev/gap/error/review, and the sampling title restricted to arXiv. Opened the primary links for the Samplinglib integration proposal and quantum-query exposition, and Li–Zadik Section 1.2.

## Step 8 — substantive extension found

- The broader search found *Subpolynomial-Query Proximal Sampling Beyond Log-Concavity*, arXiv:2611.03442v1, submitted 2 November 2026. Opened the arXiv abstract and full HTML; authors exactly as printed: Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, Yongxin Chen.
- Its abstract gives a deterministic gradient-query cap `C_ν κ (d+κ+ε^{-1}+||∇V(x₀)||²/β)^ν` for each fixed ν>0 under LSI, explicitly using the OpenAI noisy conditional sampler. This is a broader dependent extension, not a matching minimax theorem or an independent reproof of the OpenAI primitive.
- Read its related-work and Appendix B.1 passages, which identify the recursive and derivative estimates imported from OpenAI Sections 3–7 and state that neither its own accuracy dependence nor prior polylog-accuracy bounds uniformly dominates.
- Corrected the lowrank exposition URL capitalization (`OpenAI-Math/`): both sampling (7 October) and Sobolev (6 October) expositions now open readably. Their notices disavow independent full-proof verification.
- Opened AI Proof Watch's quartic assessment (18 October) and kusasyu36/openai-math-audit's README. The latter distinguishes an exponent approaching four from a single quartic-up-to-polylogs family; following its 284 audit source.

## Step 9 — completed comparison, recommendation, and spot check

- Replaced VERIFY.md's provisional follow-up section with a clause-by-clause comparison table for the relevant candidate, explicit NOT-THIS comparisons for the other two, linked follow-up records, and the three-sentence recommended replacement status.
- Opened the original 29 October audit 284 report: it names a Claude subagent as auditor, reports no clear error in checked parts, and distinguishes the exponent claim from a single near-exact quartic family. Recorded it as an AI audit, not independent expert certification.
- Li–Zadik Section 1.2 explicitly says they have not verified OpenAI's proof. Recorded this limitation.
- Spot-checked Lemma 7.1 (Gaussian center absorption) algebraically in two ways: covariance of the restored Gaussian array and its characteristic function. Checked the negative translation sign, spectrum of the covariance square root, residual correlation with the center noise, and conditional use in the compiled-routine accuracy induction. No defect found in this identity under its stated hypotheses; no global correctness verdict given.
- Updated sources with the actual Lean model and noisy-center error statement. No Lean build, simulation, or heavy program was used.

## Step 10 — final audit

- Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B -` with a short pathlib/re script restricted to reading this folder.
- Re-extracted each main theorem from the saved original introduction and asserted exact inclusion in VERIFY.md; all three match.
- Checked REPORT.md starts with PARTIAL-CLAIMED and has exactly three reason lines; checked the provisional placeholder is gone, the Spot check section exists, Markdown fences are paired, and the recommendation has exactly three sentence-ending periods.
- The command remains tiny and single-threaded; `nice` still reports the sandbox's priority-setting limitation. No git commands or writes outside this folder were used.
- Corrected two standalone backslash lines in the follow-up bound to display-math delimiters after two failed patch attempts (a JavaScript quoting error and then a mismatched backslash count). Final files: REPORT.md, VERIFY.md, LOG.md, and 24 source snapshots in sources/.
