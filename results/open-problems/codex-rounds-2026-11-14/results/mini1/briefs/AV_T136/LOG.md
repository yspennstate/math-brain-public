# T136 verification log

Task: Verify: has open problem T136 been settled by the OpenAI math release?
Started: 2026-11-14T21:08:07.480055+04:00

## Step 1 — orientation and initial opens
Read startup memory index, compute state and mesh protocol; listed local Markdown files. Attempted the three supplied GitHub folder URLs with the web tool. No git used. The task-specific instruction forbids writes outside this folder, so shared checklist, mesh and brain logging commands are not run (they mutate outside it). All local commands are prefixed `nice -n 15 env OMP_NUM_THREADS=1`; nice reports `setpriority: Operation not permitted`, consistent with the inherited process already having a lower priority. Will check the effective priority before further programs. No heavy computation is needed.

## Step 3 — recovered repository sources
GitHub connector opened all three folders, their build folders, history.md, and lean/docs listing. No lean/docs/217.md exists. Saved responses in sources/access-snapshot.json. Root paper.tex guesses failed; actual sources are under build/. ps priority inspection was denied by sandbox; initial nice explanation is only a hypothesis, not verified.

## Step 4 — preprints opened
Opened all three main TeX files, both fluctuation-paper introductions and foundations, companion interfaces, limiting-law consequences, scale fluctuations, all three READMEs and Lean formalization.yaml. Saved exact text in sources/. First paper claims full-sequence limiting law and a positive variance prefactor for fixed beta>1; second claims exponent only; third asserts full support of the zero-temperature Parisi minimizer, a different quantity. Web searches found candidate expositions and a later upper-deviation paper; these are leads pending opening.

## Step 5 — scope comparison
Read the introductions in full. Limiting law Theorems 1.1/1.2 and Proposition 1.3 use exactly our Gaussian i<j normalization and unnormalized spin sum. Scale Theorem 1.1 absorbs beta into H and uses 2^-n sum: centered F is unchanged. It gives n^(1/6+o(1)), not a constant prefactor or limit. Zero-temperature Theorem 1.1 asserts support of a deterministic Parisi minimizer, not random maximum fluctuations. Lean manifest contains none of these three titles. Preliminary verdict: PARTIAL-CLAIMED, finite-temperature part only.

## Step 6 — follow-ups and formalizations
Opened Latent Seminar, AI Proved What, Closed Form and oai-math-revised expositions; used these only as leads. Opened Yan Ru Pei arXiv:2610.06480 abstract and v3 HTML. Opened P. M. Aronow and Patrick Lopatto, hexagon:2610.00402v1 (20 Oct 2026), PDF and accompanying fluctuations-palomar README. Important correction to preliminary Lean search: official manifest omission does not imply absent code. OpenAI SKFluctuations has a conditional main_of_positiveLaplaceWindow; external package claims to prove that input internally. Opened actual OpenAI SKFullSupport challenge and SKSupport/Main.lean plus docs/281.md: zero-temperature support does have a formalization. No claim found formalizing the limiting law. Saved relevant primary-source texts. arXiv:2610.00402 is unrelated; the follow-up identifier is hexagon:2610.00402v1, a different service.

## Step 7 — deliverables saved
Wrote VERIFY.md with verbatim TeX theorems extracted directly from opened source, exact model/normalization comparisons, follow-ups, formalization distinctions and a three-sentence proposed status update. Wrote REPORT.md with PARTIAL-CLAIMED first line and three reasons. Spot check remains to be appended. Time: 2026-11-14T21:12:03.017299+04:00

## Step 8 — central estimate and external proof interface
Opened limiting-law reduction (including the stopped pressure increment proposition and full deduction), parameter choices, and expansion section. Opened fluctuations-palomar Challenge.lean, Solution.lean and submission/claims.json: exported theorem_1_6 has no explicit PositiveLaplaceWindow hypothesis and states all three exponent assertions. No kernel replay attempted. Opened arXiv pages for our original 2609.09103 and survey 2510.26960; inspected Pei v3 section 10.2 distinguishing fixed-s large deviations from the central scale and noting missing zero-temperature uniformity. Auditing file rendering and central estimate arithmetic next.

## Step 9 — spot check appended
Selected the central stopped pressure increment estimate. Checked the size-factor derivative/stencil identity, all three smoothing/error exponents, direct-path exponent signs, cumulant interpolation loss, dyadic summability and positivity deduction. Exact rational arithmetic saved in sources/spot-check-arithmetic.txt. The analytic uniform overlap estimates were not certified. Repaired backspace/tab escapes in explanatory math; quoted TeX was unaffected. Opened additional mean-bias and perceptron follow-up pages and their actual PDF/HTML links. 2026-11-14T21:13:37.283425+04:00

## Step 10 — final audit
All five TeX quotation blocks match their saved opened source exactly; no stray control characters or tabs remain. REPORT.md has the required verdict first line plus three reason lines. VERIFY.md includes scope comparison, follow-ups, a three-sentence proposed status and Spot check. Added the actual mean-bias and perceptron follow-ups and baseline arXiv pages to the inventory. Saved SHA256 hashes of local evidence files. No git, external writes, posts, accounts, subagents, builds or heavy compute used. 2026-11-14T21:14:15.135240+04:00
