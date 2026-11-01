# Literature search

## Status assessment

**Not established as SOLVED_IN_LITERATURE.** Later papers explicitly give partial answers to Malrieu's Open question 4. None of the fetched papers states a classification for the entire class with the source's hypotheses and quantifiers. Rate thresholds, compactness, nondegeneracy, smooth rates, common-matrix affine form, or dimension-one restrictions are additional assumptions. This assessment concerns this bounded search, not an assertion that no other paper can exist.

Exact source quote, arXiv:1412.7516, PDF p. 13:

> Open question 4. What can be said on the smoothness of the density of the invariant measure of such processes?

Section 4 begins on PDF p. 8 with finitely many smooth globally forward-complete vector fields on R^d and nonnegative continuous position-dependent transition rates. Section 4.2, PDF pp. 12–13, discusses additional conditions for absolute continuity and provides both boundary and interior singularity examples. The source itself already rules out automatic everywhere smoothness. Its cited dimension-one regularity paper predates this question.

## Relevant references and coverage

1. **Florent Malrieu**, *Some simple but challenging Markov processes*, Annales de la Faculté des sciences de Toulouse: Mathématiques, série 6, **24**(4), 857–883, issue year 2015; DOI **10.5802/afst.1468**; arXiv:**1412.7516**. Crossref records publication on 2016-01-20; the article is commonly cited by its 2015 issue year. Source PDF and extracted text: `source.pdf`, `source.txt`. Open question 4: PDF p. 13. Example 4.7: the stable rotating affine fields with A=[[-1,-1],[1,-1]], a=(1,0).

2. **Yuri Bakhtin and Tobias Hurth**, *Invariant densities for dynamical systems with random switching*, Nonlinearity **25**(10) (2012), 2937–2952; arXiv:**1203.5744**. Absolute continuity and uniqueness under accessibility and a Lie-algebra condition. This does not imply density smoothness. Source reference [2]; arXiv query returned its abstract.

3. **Yuri Bakhtin, Tobias Hurth and Jonathan C. Mattingly**, *Regularity of invariant densities for 1D systems with random switching*, Nonlinearity **28**(11) (2015), 3755-3787; DOI **10.1088/0951-7715/28/11/3755**; arXiv:**1406.5425**. Full one-dimensional analysis of regularity away from critical points and singularity asymptotics. The source already cites this preprint as [3]. A dimension-one result is not the higher-dimensional answer.

4. **Yuri Bakhtin, Tobias Hurth, Sean D. Lawley and Jonathan C. Mattingly**, *Smooth invariant densities for random switching on the torus*, Nonlinearity **31**(4) (2018), 1331–1350; DOI **10.1088/1361-6544/aaa04f**; arXiv:**1708.01390**, fetched v2 (2018-03-21). Two-dimensional torus, globally transverse fields, positive smooth invariant densities for the individual flows, no periodic orbits. Smoothness for all positive rates in this restricted class. These hypotheses exclude contracting equilibria such as Example 4.7.

5. **Yuri Bakhtin, Tobias Hurth, Sean D. Lawley and Jonathan C. Mattingly**, *Singularities of Invariant Densities for Random Switching between Two Linear ODEs in 2D*, SIAM Journal on Applied Dynamical Systems **20**(4) (2021), 1917–1958; DOI **10.1137/20M1364345**; arXiv:**2009.01299**. Fetched v1. Uses a common diagonal stable matrix with distinct eigenvalues and two distinct equilibria. Theorems 1 and 2 give parameter-dependent singularity and boundedness results. The introduction itself conjectures interior C-infinity smoothness. It is a different affine subfamily from the rotating source example and not a general solution.

6. **Michel Benaïm and Oliver Tough**, *Regularity of the stationary density for systems with fast random switching*, Nonlinearity **38**(8) (2025), 085012; DOI **10.1088/1361-6544/adeef8**; arXiv:**2212.03632**, fetched v2 (2023-02-12). Smooth fields on a compact forward-invariant set; spatially constant irreducible rate matrix. Theorem 2.8 gives finite-order smoothness for sufficiently fast switching under additional bracket hypotheses; Theorem 2.11 gives singularities under sufficiently slow switching. General sufficient/obstruction results, not a classification of all source objects and parameters.

7. **Michel Benaïm and Oliver Tough**, *On invariant distributions of Feller Markov chains with applications to dynamical systems with random switching*, Probability Theory and Related Fields **192**(3–4), 1283–1324; DOI **10.1007/s00440-024-01307-y**, online publication 2024-08-12; arXiv:**2310.17543**, fetched v7 (2024-10-24). Theorem 4.15, PDF p. 41: finite-order regularity under a global 1-bracket condition and sufficiently fast spatially constant switching. Example 4.18, PDF pp. 46–47, explicitly calls the conclusion “a partial answer to his Open Question 4.” Broader regularity follows under stated kernel decomposition conditions, which must be separately verified.

8. **Michel Benaïm and Améthyste Bichard**, *Regularity of Invariant Densities for Random Switching between Two Linear ODEs in R^d*, SIAM Journal on Applied Dynamical Systems **24**(3) (2025), 2473–2488; DOI **10.1137/24M1696172**; arXiv:**2406.17891**, fetched v2 (2024-07-18; manuscript dated 2024-07-19). Example 1.3, PDF p. 5, is exactly Malrieu's rotating affine Example 4.7 and names Open question 4. Theorem 2.2, PDF p. 8, gives the quantitative C^r sufficient condition quoted below. This is highly relevant, but its extra rate and common-matrix/controllability hypotheses make it a partial answer under the requested criterion.

9. **Leo Hahn**, *Invariant-measure regularity for one-dimensional PDMPs with applications to shape transitions in run-and-tumble particle systems*, arXiv:**2506.02274**, fetched current PDF dated 2026-08-20. Found through Semantic Scholar's source-citation list. Covers simultaneously vanishing fields and sharp dimension-one regularity with position-dependent rates and resetting. The abstract explicitly restricts to dimension one. It cannot classify the higher-dimensional switched flows in the source.

## The closest quantitative theorem, quoted as a partial result

Benaïm–Bichard, arXiv:2406.17891v2, **Theorem 2.2, PDF p. 8** (formula layout transcribed into mathematical notation; wording retained):

> Theorem 2.2 Let r ≥ 0 be a integer. Assume that
>
> min(α₀₁, α₁₀) > −[∑ᵈᵢ₌₁ Λᵢ + rΛ₁]. (3)
>
> Then, ρ is Cʳ on Rᵈ × {0, 1}, and {ρ > 0} = Int(Γ), where ρ is, like in Proposition 2.1, the density of Π.

Its standing assumptions on PDF pp. 3–4 are A Hurwitz, p nonzero, constant positive switching rates and linear independence of p,Ap,...,A^(d-1)p. The Λ_i are ordered real parts of eigenvalues.

Line-by-line specialization to the source example:

- Its p is the source's a=(1,0); both use F_0(x)=Ax and F_1(x)=A(x-a).
- The source's A has eigenvalues −1±i, so d=2 and Λ_1=Λ_2=−1.
- The columns a and Aa have determinant 1, so the standing controllability assumption holds.
- α_01=λ_0 and α_10=λ_1 match the source's constant exit rates.
- The right side of (3) equals −[−2−r]=2+r.
- Hence the theorem gives C^r regularity for this exact example whenever min(λ_0,λ_1)>2+r.
- It does **not** say what happens for all the other rates, nor does it handle arbitrary families of smooth vector fields with merely continuous position-dependent rates. A single fixed finite rate satisfying the inequality for one r does not thereby yield C-infinity regularity.

There is no theorem quoted here as a complete printed solution of the source's broad question, and no SOLVED_IN_LITERATURE verdict is assigned.

## Read-only research brain and previous attempts

The initial math-store query was “PDMP invariant density regularity switching flows Bakhtin Hurth”; its matches were irrelevant. The initial memories query was “PDMP invariant density smoothness mistakes”, also with no useful PDMP match. A further topic recall “random switching invariant densities Bakhtin Hurth” was saved to `brain_topic_recall.txt`.

Read-only intake search found `probability_1000_intake_E_20260908/attempts.jsonl`, E0019-A001, and its `problems.jsonl` entry. They make an invalid inference from drift collinearity to bracket degeneracy and contain an incorrectly transcribed determinant. ATTEMPT.md Section 5 gives the correction. The records were not modified. A filtered `git ls-tree` search of `origin/master` in the recorded-answers checkout found no E0019 or invariant-density answer path; no working tree was touched.

## Search limitations and corrections

OpenAlex returned HTTP 429 on all attempts. Consequently no verified OpenAlex source identifier or its citing-works list was obtained. Preliminary diagnostic requests used DOI 10.5802/afst.1463 and unverified identifier W2095592930; neither was verified as the source and neither response was used as evidence. Crossref subsequently resolved the correct source DOI **10.5802/afst.1468**, and requests with that DOI were also logged below. This explicitly corrects the preliminary requests.

Semantic Scholar's search and arXiv-id endpoints initially returned HTTP 429. Its DOI endpoint succeeded and returned the source citation list, including the 2024 linear paper and the newer Hahn dimension-one paper. GitHub returned zero repositories for “PDMP invariant density”; the broader query returned repository metadata without a theorem solving the question. arXiv searches and Crossref lookups succeeded. Broad arXiv search had many irrelevant results; the later targeted title query found the directly relevant regularity papers. No built-in web-search tool was used.

## Complete web request log

Date: 2026-10-12. Raw responses saved locally.

- source: `https://arxiv.org/pdf/1412.7516` — OK; 952986 bytes.
- arxiv: `https://export.arxiv.org/api/query?search_query=all%3A%22invariant%20density%22%20AND%20all%3A%22switching%22&max_results=20` — OK; 14246 bytes.
- openalex: `https://api.openalex.org/works?search=regularity%20invariant%20density%20randomly%20switched%20vector%20fields&per-page=15` — HTTP Error 429: Too Many Requests; 0 bytes.
- openalex_source: `https://api.openalex.org/works?search=Some%20simple%20but%20challenging%20Markov%20processes&per-page=5` — HTTP Error 429: Too Many Requests; 0 bytes.
- crossref: `https://api.crossref.org/works?query=invariant%20density%20randomly%20switched%20vector%20fields&rows=15` — OK; 57976 bytes.
- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=regularity%20invariant%20density%20switching&limit=10&fields=title,authors,year,url,externalIds` — HTTP Error 429: ; 0 bytes.
- github: `https://api.github.com/search/repositories?q=PDMP%20invariant%20density` — OK; 55 bytes.

- 2026-10-12 linear2024: `https://arxiv.org/pdf/2406.17891` — OK; 603538 bytes.

- 2026-10-12 singular2020: `https://arxiv.org/pdf/2009.01299` — OK; 459834 bytes.

- 2026-10-12 general_regular: `https://export.arxiv.org/api/query?search_query=all%3A%22regularity%22%20AND%20%28all%3A%22switching%22%20OR%20all%3A%22PDMP%22%29&max_results=40&sortBy=submittedDate&sortOrder=descending` — OK; 89658 bytes.

- 2026-10-12 torus2017: `https://arxiv.org/pdf/1708.01390` — OK; 268736 bytes.

- 2026-10-12 crossref_exact: `https://api.crossref.org/works?query.title=Some%20simple%20but%20challenging%20Markov%20processes&rows=3` — OK; 24116 bytes.

- 2026-10-12 openalex_retry: `https://api.openalex.org/works?search=Some%20simple%20but%20challenging%20Markov%20processes&per_page=3` — HTTP Error 429: Too Many Requests; 0 bytes.

- 2026-10-12 semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1412.7516?fields=title,authors,year,citations.title,citations.year,citations.externalIds` — HTTP Error 429: ; 0 bytes.

- 2026-10-12 github_retry: `https://api.github.com/search/repositories?q=random%20switching%20vector%20fields` — OK; 8374 bytes.

- 2026-10-12 fast2022: `https://arxiv.org/pdf/2212.03632` — OK; 320654 bytes.

- 2026-10-12 feller2023: `https://arxiv.org/pdf/2310.17543` — OK; 466094 bytes.

- 2026-10-12 arxiv_targeted: `https://export.arxiv.org/api/query?search_query=%28ti%3A%22random%20switching%22%20OR%20ti%3A%22randomly%20switched%22%20OR%20ti%3A%22piecewise%20deterministic%22%29%20AND%20%28all%3A%22smoothness%22%20OR%20all%3A%22regularity%22%29&max_results=60&sortBy=submittedDate&sortOrder=descending` — OK; 30890 bytes.

- 2026-10-12 openalex_doi: `https://api.openalex.org/works/https://doi.org/10.5802/afst.1463` — HTTP Error 429: Too Many Requests; 0 bytes.

- 2026-10-12 openalex_citing: `https://api.openalex.org/works?filter=cites:W2095592930&per_page=50` — HTTP Error 429: Too Many Requests; 0 bytes.

- 2026-10-12 openalex_search_alt: `https://api.openalex.org/works?search=Some%20simple%20but%20challenging%20Markov%20processes&per_page=5&select=id,title,doi,publication_year` — HTTP Error 429: Too Many Requests; 0 bytes.

- 2026-10-12 openalex_correct_doi: `https://api.openalex.org/works/https://doi.org/10.5802/afst.1468` — HTTP Error 429: Too Many Requests; 0 bytes.

- 2026-10-12 openalex_doi_search: `https://api.openalex.org/works?filter=doi:https://doi.org/10.5802/afst.1468` — HTTP Error 429: Too Many Requests; 0 bytes.

- 2026-10-12 semantic_doi: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.5802/afst.1468?fields=title,year,citations.title,citations.year,citations.externalIds` — OK; 14595 bytes.

- 2026-10-12 crossref_regular_exact: `https://api.crossref.org/works?query.title=Regularity%20of%20the%20stationary%20density%20for%20systems%20with%20fast%20random%20switching&rows=3` — OK; 18553 bytes.

- 2026-10-12 one_dim_2025: `https://arxiv.org/pdf/2506.02274` — OK; 521338 bytes.

- 2026-10-12 linear2024_metadata: `https://api.crossref.org/works/10.1137/24M1696172` — OK; 5642 bytes.

- 2026-10-12 feller2023_metadata: `https://api.crossref.org/works/10.1007/s00440-024-01307-y` — OK; 14033 bytes.

- 2026-10-12 singular2020_metadata: `https://api.crossref.org/works/10.1137/20M1364345` — OK; 6305 bytes.

- 2026-10-12 torus2017_metadata: `https://api.crossref.org/works/10.1088/1361-6544/aaa04f` — OK; 10573 bytes.

- 2026-10-12 source_metadata: `https://api.crossref.org/works/10.5802/afst.1468` — OK; 20800 bytes.


## Follow-up searches, 2026-10-12

These narrowly test whether the proposed finite-p classification is explicitly covered; no originality claim is made.

- followup_arxiv_lp: `https://export.arxiv.org/api/query?search_query=%28all%3A%22invariant%20density%22%20OR%20all%3A%22invariant%20densities%22%29%20AND%20%28all%3A%22integrability%22%20OR%20all%3A%22Lp%22%29%20AND%20all%3A%22switching%22&max_results=20` — OK; 4435 bytes.

- followup_crossref_lp: `https://api.crossref.org/works?query=Lp%20integrability%20invariant%20densities%20random%20switching%20stable%20linear%20flows&rows=8` — OK; 39313 bytes.

Follow-up query results: the arXiv Lp/integrability query returned the already known torus paper (1708.01390) and an unrelated resetting paper (2306.13621). The Crossref query returned the already recorded Bakhtin--Hurth, Benaim--Bichard, torus and dimension-one references, plus unrelated titles. No theorem stating the exact finite-p equivalence was located by this narrow search. This is not a novelty certification and does not change the overall literature verdict.

Follow-up brain questions, 2026-10-12:
- `math_recall.py "PDMP invariant density critical switching rate resolvent positive density equilibrium Benaim Tough"`, raw `gap_math_recall.txt`; no relevant specialized card.
- `math_recall.py "Feller Markov kernel Q Delta Neumann series Lp invariant densities Benaim Tough spectral radius"`, raw `gap_transfer_recall.txt`; relevant standard Neumann-series card.
- Walked `math_recall.py --id claim_d42919cf2ac24118a84a6be3f315f5c9`, raw `gap_neumann_card.txt`. Its bounded-operator norm<1 hypotheses are explicitly verified in FOLLOWUP.md instead of assumed. No brain memory was written.
