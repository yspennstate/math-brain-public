# C0031 — literature and provenance, 2026-10-11

All network access used Python urllib from the shell. Raw responses and exact request URLs are retained in `search_log.json` and `search_more_log.json`.

## Searches so far

- arXiv: `all:"heavy tailed" AND all:"circular law"`, 40 results requested; success.
- arXiv: `all:"heavy-tailed" AND (all:"non-Hermitian" OR all:"circular")`, 80 results requested, newest first; success.
- arXiv: `all:"smallest singular" AND (all:"heavy" OR all:"moment assumptions")`, 50 results requested, newest first; success.
- OpenAlex works search: `heavy tailed circular law`, 40 results requested; HTTP 429.
- OpenAlex works search: `Spectrum of non-Hermitian heavy tailed random matrices`, 20 results requested; HTTP 429.
- OpenAlex source lookup by DOI `10.1016/j.probab.2012.02.004`; HTTP 429; identity not yet validated. Citing-works search still to be attempted explicitly.
- Crossref: `heavy tailed circular law`, 30 results requested; success, poorly targeted results.
- Crossref: `smallest singular value heavy tailed no moment assumptions`, 25 results requested; success.
- Crossref: `almost sure heavy tailed circular law`, 25 results requested; success.
- Semantic Scholar paper search: `heavy tailed circular law`, 30 results requested; HTTP 429.
- Semantic Scholar: citations of `ARXIV:1109.3343`, 1000 results requested; success, retained in `semantic_retry.json`.
- GitHub repository search: `heavy tailed circular law`; success, mostly irrelevant results (raw response retained). Repository search is discovery only, not a theorem-level check.

## Sources fetched

Charles Bordenave and Djalil Chafai, *Around the circular law*, Probability Surveys 9 (2012), 1–89, arXiv:1109.3343. PDF and extracted text are `survey.pdf` and `survey.txt`. The downloaded latest arXiv version has the heavy-tail theorem on printed page 39 and the detailed Section 6.6 on printed page 51.

Charles Bordenave, Pietro Caputo and Djalil Chafai, *Spectrum of non-Hermitian heavy tailed random matrices*, Communications in Mathematical Physics 307 (2011), 513–560, arXiv:1006.1713. PDF and text are `original.pdf` and `original.txt`. The theorem is being inspected; its abstract expressly mentions additional smoothness assumptions for almost-sure convergence.

## Read-only prior-work checks

Math recall query: `heavy tailed circular law smallest singular value almost surely`; memories query: `heavy tailed circular law mistakes`; topic recall: `Almost-sure convergence heavy-tailed circular law`. The September intake's smallest-singular-value diagnosis is a hint, not an independently checked theorem.

The authorized October pool's `team_O/w339/results.jsonl` records (i) a diagonal example showing that polynomial s_min alone does not imply log uniform integrability, (ii) an almost-sure subsequence consequence, (iii) the already-known bounded-density almost-sure special case. These do not solve the unrestricted upgrade.

The September ledger entries C0031 and C0031-A001 were found by read-only Python access. The git checkout is being inspected using `git ls-tree` and `git show origin/master:<path>` only.

The first published-checkout filename scan was too broad and encountered unrelated files before a read timed out. This does not establish full coverage of the published repository; no relevant C0031 answer was verified from that scan. The script was narrowed to problem-specific filenames for reproducibility.

## Status discipline

No theorem proving the unrestricted almost-sure upgrade has been verified. A bounded-density theorem does not justify SOLVED_IN_LITERATURE. Exact hypotheses, theorem quotations and promising later papers will be recorded below as checked.

## Exact source theorem and open remark

Theorem 6.2, *Around the circular law*, printed page 39 (also PDF page 39), reads:

> Theorem 6.2 (Eigenvalues of heavy tailed random matrices). There exists a probability measure μ_α on C such that in probability μ_(n^{-1/α}X) ⇝ μ_α as n → ∞. Moreover, if X_11 has a bounded density, then the convergence is almost sure.

Immediately after it:

> We believe that theorem 6.2 can be upgraded to an a.s. weak convergence, but our method does not catch this due to slow “in probability” controls on small singular values.

Mathematical symbols have been transcribed from the PDF; words are unchanged. The assumptions immediately before the theorem, on printed page 38, are t^α P(|X_11| >= t) -> 1 for 0 < α < 2 and convergence of the conditional angle distribution on S^1. Thus generic stable attraction with an arbitrary slowly varying tail is a broader formulation with a potentially different normalization. Section 6.6 is the proof of the density upgrade, not the location of the open remark.

The original paper's Theorem 1.2, printed/PDF page 3, reads:

> Theorem 1.2 (Eigenvalues). If (H1-H2-H3) hold then there exists a probability measure μ_α on C depending only on α such that a.s. μ_A ⇝_(n→∞) μ_α.

Its H1 is regular variation and angular convergence, H2 is P(|X_11| >= t) ~ c t^{-α}, c > 0, and H3 is a bounded Lebesgue density on R or C (page 2). The scale is a_n = inf{a > 0: n P(|X_11| >= a) <= 1}, and A = a_n^{-1} X. This is an already-known smoothness special case, not a solution of the unrestricted question. The abstract's shorthand a_n ~ n^{1/α} must be read with the explicit hypotheses and constant c.

## Follow-up leads checked or being checked

- Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, arXiv:2010.01261v3 (2 February 2022). Fetched PDF/text. Theorem 1.6, printed/PDF page 4, explicitly concludes convergence **in probability**, under Condition C2. Remark 1.7, page 5, identifies the independent-entry limit with Bordenave–Caputo–Chafai. It is a relevant extension and invertibility lead, not the requested almost-sure theorem. The introduction's informal description of the older iid theorem omits the older smoothness restrictions; the actual older Theorem 1.2 controls scope.
- *The smallest singular value of inhomogenous random rectangular matrices*, arXiv:2408.14389v2. The abstract describes a result under fixed-scale anti-concentration, which might sound applicable without moments. Full hypotheses are being checked rather than inferred from the abstract.
- Galyna V. Livshyts, *The smallest singular value of heavy-tailed not necessarily i.i.d. random matrices via random rounding*, arXiv:1811.07038v4. Full hypotheses are being checked; the title's “heavy-tailed” does not by itself mean infinite variance is allowed.
- Elizaveta Rebrova and Konstantin Tikhomirov, *Coverings of random ellipsoids, and invertibility of matrices with i.i.d. heavy-tailed entries*, arXiv:1508.06690v3. The abstract explicitly assumes mean zero and variance one; this is outside α < 2 infinite-variance entries. Lead only.
- Anirban Basak and Mark Rudelson, *Invertibility of Sparse non-Hermitian matrices*, arXiv:1507.03525v3, Advances in Mathematics 310 (2017), 426–483, DOI 10.1016/j.aim.2017.02.009. Abstract concerns sparse models and optimal moment assumptions, not the unrestricted stable heavy-tail almost-sure law.

Raw arXiv summaries and selected Semantic Scholar citing-paper metadata are also retained in `targeted_literature.txt`; they are discovery material, not theorem verification.

OpenAlex follow-up used the survey's correct DOI, `10.1214/11-PS183`, to resolve the source before attempting a citing-works filter. That lookup also returned HTTP 429, so a verified citing-works list could not be obtained. See `openalex_citation_attempt.json`. The earlier DOI lookup was not a verified source identity and is not counted as citation coverage.

## Refereeing the recent invertibility leads

Max Dabagia and Manuel Fernandez V, *The smallest singular value of inhomogenous random rectangular matrices*, arXiv:2408.14389v2, uploaded 25 July 2025 (PDF dated 28 July 2025). Theorem 1, printed/PDF page 2, states its hypotheses explicitly:

> Let A ∈ R^{N×n} be a random matrix with independent entries ξ that satisfy Eξ = 0, Eξ² = 1, sup_(z∈R) P(|ξ − z| < a) < b.

Thus its abstract's replacement of a higher-moment assumption by anti-concentration still keeps variance one. Page 4 defines the more general Hilbert-Schmidt norm assumption as E||A||²_HS ≲ Nn. Neither directly covers the source's α<2 fixed entry law. This is a related theorem, not a solution of C0031.

Galyna V. Livshyts, *The smallest singular value of heavy-tailed not necessarily i.i.d. random matrices via random rounding*, arXiv:1811.07038v4. Theorem 1, printed/PDF pages 3–4, requires fixed p>0 and an absolute K for which both

sum_i (E|A e_i|^{2p})^{1/p} <= K n²,
sum_i (E|A^T e_i|^{2p})^{1/p} <= K n².

The constants depend on K and on fixed-scale anti-concentration. For α-tail iid entries, each row or column norm has scale n^{1/α}, so these sums have scale n^{1+2/α}, strictly larger than n². A uniform K is not available. The paper's Remark 1.5, page 5, expressly discusses the failure of its row-norm condition for fixed distributions of infinite variance. The theorem therefore cannot simply be applied here. Its more general regularized-norm ideas remain a lead; no full implication is claimed.

These PDFs and extraction logs are retained as `2408.14389.pdf/.txt`, `1811.07038.pdf/.txt`, `2010.01261.pdf/.txt`, and `leads_log.json`. No inspected theorem states and proves the unrestricted almost-sure upgrade with the source hypotheses. This is a bounded search with OpenAlex unavailable; it is not a proof of present openness.

## Earlier published/recorded attempts recovered

A targeted read-only `git grep` at `origin/master` located the C0031 research handoff and its mathematical artifact. Both were read in full with `git show`, without touching the working tree:

- `research7_2026-09-17/R7-05/handoffs/2026-09-19T032418Z__C0031_sixrun_handoff.md`.
- `research7_2026-09-17/R7-05/artifacts/2026-09-19/2026-09-19T030855Z__C0031_independent_smoothing_and_fair_edge_decomposition.md`.

The handoff reports PARTIAL, not a solution. Its mathematical leads include prescribed sparse subsequences, almost-sure control above a stretched-exponential hard-edge threshold, independent finite-variance additive smoothing, and a fair Bernoulli decomposition of symmetric discrete Pareto entries with a bounded but nonseparable amplitude profile. The latter reduces an atomic benchmark to high-confidence invertibility for D_n + K_n ∘ E_n under arbitrary polynomial-norm complex deterministic cores. These are prior author-checked claims, not accepted here as verified theorems. Our Cantor-plus-integer example also has an independent finite-variance convolution factor and hence overlaps that prior smoothing subclass; no novelty is claimed for it.

The prior artifact identifies Cook, *Lower bounds for the smallest singular value of structured random matrices*, Annals of Probability 46 (2018), arXiv:1608.07347v5, Theorems 1.8 and 1.26, as relevant shifted-iid versus bounded-profile results. It describes the latter's error as O(sqrt(log n/n)), still nonsummable. A final arXiv author/topic query `all:"invertibility" AND au:Jain` is being run because the handoff also names Jain's quantitative invertibility work. Its exact URL/response will be kept in `final_lead_log.json` and `arxiv_jain.xml`.

That final query succeeded. The relevant hit is Vishesh Jain, *Quantitative invertibility of random matrices: a combinatorial perspective*, arXiv:1908.11255v3. Its abstract expressly treats M+N_n with iid noise of mean zero and variance one and complex deterministic M of norm at most exp(n^c). The abstract therefore provides a lead for independent finite-variance smoothing, not a direct theorem for the fixed infinite-variance source entry law. No claim of a source-matching theorem is made; the PDF was not theorem-checked. The other relevant hit, *Sharp invertibility of random Bernoulli matrices*, arXiv:2010.06553v2, concerns ordinary Bernoulli entries and a slice model, not the unrestricted heavy-tailed law. The query also returned many irrelevant author-name/stemming matches; only the random-matrix hits were considered.

Final Crossref requests on 2026-10-11: DOI lookup `10.1214/11-PS183` (HTTP 429); `query.title=Spectrum of non-Hermitian heavy tailed random matrices` (10 requested, HTTP 429); `query.bibliographic=almost sure convergence heavy tailed circular law random matrices` (20 requested, success). Exact URLs and service status are in bibliography_log.json. The last search returned no theorem establishing the unrestricted almost-sure question; its hits include finite-variance circular-law convergence rates and heavy-tailed Hermitian/circulant results. Search metadata alone is not a solution check. Every search's response or failure is preserved in the folder.

**Final bounded-search verdict:** no source-matching published solution was verified. The original bounded-density theorem and later related theorems must not be labeled SOLVED_IN_LITERATURE. The present work proves special cases and a conditional reduction, with the general hard-edge discrepancy left open.


## Second-attempt searches and exact theorem audit, 2026-10-11

Read-only math-store query: `Cook Jain bounded amplitude Bernoulli profile arbitrary deterministic perturbation summable smallest singular value`. Returned generic subgaussian and Borel--Cantelli cards; none supplies the missing conditional profile theorem. No brain write was performed.

Direct arXiv PDF fetches: https://arxiv.org/pdf/1608.07347 ; https://arxiv.org/pdf/1908.11255 ; https://arxiv.org/pdf/0805.3167 . All succeeded. Files second_cook.pdf/.txt, second_jain.pdf/.txt, second_taovu.pdf/.txt preserve the versions inspected. The precise URLs and date are in second_search_log.json.

ArXiv API query: `(ti:"invertibility" OR ti:"singular value") AND (all:"perturbation" OR all:"inhomogeneous") AND cat:math.PR`, newest first, max_results=60. Successful response in second_inhomogeneous_search.xml; exact escaped URL in second_search_log.json. Relevant neighboring hits include arXiv:1909.04219v4, *The smallest singular value of inhomogeneous square random matrices*, whose abstract assumes expected squared Hilbert--Schmidt norm <=Kn^2; and arXiv:2412.18906v2, *The Rank and Singular Values of the Inhomogeneous Subgaussian Random Matrices*, a subgaussian model. These are abstract-level leads, not verified solutions or direct implications for the unrestricted infinite-variance model.

Theorem-level references:

- Nicholas Cook, *Lower bounds for the smallest singular value of structured random matrices*, Annals of Probability 46 (2018), 3442--3500, arXiv:1608.07347. In the currently fetched PDF, the relevant super-regular-profile result is **Theorem 1.24, printed page 15**, and its definition is Definition 1.23, page 14. This corrects reliance on the prior handoff's different numbering (1.26). Its error is O(sqrt(log n/n)) under a polynomial norm cap. SECOND_ATTEMPT.md proves why the conditioned two-atom mask meets its hypotheses, and why the error still does not settle the question.
- Terence Tao and Van Vu, *Smooth analysis of the condition number and the least singular value*, Mathematics of Computation 79 (2010), 2333--2352, arXiv:0805.3167v3. Theorem 3.2, printed page 6, includes an o(1) term; Definition 5.1, page 10, includes bounded second moment; Remark 5.3, page 10, describes rather than proves a likely non-identically distributed extension. The fixed-vector Theorem 6.4, page 12, is insufficient on its own to control the least singular value over all directions.
- **Vishesh Jain**, *Quantitative Invertibility of Random Matrices: a Combinatorial Perspective*, Discrete Analysis 2021:10, 40 pp., DOI 10.19086/da.27994, arXiv:1908.11255v3. Theorem 1.1, printed pages 4--5, requires iid mean-zero variance-one noise. The previously recorded first name 'Ashwin' was an error, corrected here and in the earlier paragraph. The conditional masked noise does not meet the iid hypothesis.

No inspected paper states and proves the source-matching unrestricted almost-sure theorem. The new averaged theorem is our deduction from source estimates, not a theorem in print asserted to solve C0031. The literature verdict therefore remains unverified as to present openness, with no SOLVED_IN_LITERATURE claim.
