# Literature check

Search date: 2026-10-11 (local environment date). Raw responses are retained in this folder.

## Verified source

Yi Han, *Brown measure convergence for the spectrum of polynomials in Ginibre matrices*, arXiv:2606.01664v1 [math.PR], 1 June 2026, https://arxiv.org/pdf/2606.01664. PDF saved as source.pdf; complete extracted text saved as source.txt. Normalization: independent real and imaginary entry parts with variance 1/(2N), Definition 1.1, page 2.

Question 1.6, page 6 (word-for-word text, mathematical superscripts rendered inline):

> Does the singular value estimate in Theorem 1.3 hold at the point z = p(0), so that in particular the matrix polynomial P^N is invertible with high probability for a nonzero polynomial p with p(0) = 0? The answer is positive when p has degree 2, as proven in [10], but higher degrees are not covered.

Theorem 1.3, page 3, has: any p in C<x_1,...,x_n>; any z != p(0); constants c_0(p), c(p), c_1(p) depending only on p, C-hat(p,z)>0 and N_0(p,z); every N>=N_0 and epsilon>0; bound C-hat (N^(c_0) epsilon^c + exp(-c_1 N)). Question 1.6 therefore concerns a quantitative estimate, not just qualitative invertibility. Its nonzero, zero-constant-term formulation excludes constant polynomials. The N_0 exception excludes fixed-small-dimension polynomial identities from being counterexamples.

At page 4 Han explains the obstruction: the deterministic linearization coefficient K_z is invertible away from p(0), but singular at p(0); his normalization to identity is unavailable there.

No paper is certified here as solving Question 1.6. Search failures are recorded as failures, not negative search results.

## Search findings and leads

- arXiv, query Ginibre AND polynomial, latest submitted first, 30 records: the June source is the only returned recent paper whose abstract addresses the full polynomial least-singular-value setting. Newer returned records include *An optimal Poincare inequality for the complex Ginibre log-gas*, arXiv:2608.19358, and *On the heat flow conjecture for random matrices*, arXiv:2608.05185. Neither returned abstract states the requested extension.
- arXiv, query "least singular" AND polynomial, 30 records: the source appears; the one newer record returned is *Sharp singularity asymptotics for discrete random matrices*, arXiv:2609.39463, a different model. A methodological lead is *New Tools for Smoothed Analysis: Least Singular Value Bounds for Random Matrices with Dependent Entries*, arXiv:2405.01517, whose abstract studies polynomial entries and limited randomness. No matching theorem for the source question was identified or claimed.
- Crossref, Ginibre polynomial least singular value, 20 records: relevant deformed-single-matrix leads are *The Least Singular Value of the General Deformed Ginibre Ensemble*, DOI 10.1007/s10955-022-02989-1, and *Optimal lower bound on the least singular value of the shifted Ginibre ensemble*, DOI 10.2140/pmp.2020.1.101. These are not arbitrary noncommutative polynomial extensions. The additional search restricted to publication dates from 2026-06-01 returned no matching title/theorem. Full metadata is in the raw JSON files.
- Semantic Scholar broad search was rate-limited. Direct lookup ARXIV:2606.01664 succeeded: paper ID 2eb9b7403cc84d4a3018946bb390dffd5ef01122, one indexed citation, Yi Han, *Circular law for non-Hermitian block band matrices with slowly growing bandwidth*, arXiv:2511.01744 (initially 2025). Its title concerns block band matrices, not an asserted solution of Question 1.6; its arXiv metadata was requested separately. Citation indexing is not a complete literature census.
- GitHub query Ginibre polynomial singular returned zero repositories. Query "2606.01664" returned `hanyi162013-Yihan/ginibre-lsv-lean`, https://github.com/hanyi162013-Yihan/ginibre-lsv-lean, created 22 August 2026. Its stated scope is formalization of Sections 3--4 and Theorem 1.5 of the source, not a paper proving Question 1.6. README and contents were requested for inspection.
- OpenAlex broad search, repeat search, and source-resolution requests returned HTTP 429. A final title-filter source-resolution request was made, with a conditional citing-works query if an ID is returned. The lack of an answer is an access limitation, not evidence of no citations or solutions.

The existing degree-two result, cited as [10] by Han, is Nicholas A. Cook, Alice Guionnet, Jonathan Husson, *Spectrum and pseudospectrum for quadratic polynomials in Ginibre matrices*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques **58**(4) (2022), 2284--2320. Han explicitly credits its Theorem 1.3 with the degree-two all-shifts estimate (page 3), and credits it in Question 1.6. This is a solved special case, not a solution of the general higher-degree question. Its arXiv metadata was requested separately.

Final metadata inspection: the Cook--Guionnet--Husson arXiv identifier is **2008.08833v1**. The indexed citing paper is **2511.01744v3**, by Yi Han; its fetched abstract concerns independent-entry block tridiagonal matrices and circular-law convergence, and does not state the constant-term polynomial bound. The GitHub README explicitly identifies `GinibreLSV.Section3.theorem15` as the endpoint and says it formalizes Theorem 1.5. Its advertised formal verification is treated as a lead, not independently certified here. The last OpenAlex title-resolution attempt again returned HTTP 429, so a source work ID could not be resolved and its citing-works search could not be executed. This portion of the requested literature check remains access-limited.

## Read-only prior work

- 2026-10-11: `math_recall.py "Ginibre polynomial least singular value constant term"`: returned open-problem card claim_89f5b49d7300874a6da0c7da5434f8f904dab5659e2bb85db6bd04bc463d9aed and earlier-attempt card claim_14c12c7b91aefe74cc26707557546cd14e890eb6b58adfe07c423604685765a6. The earlier attempt proves only monomials by product propagation; checked independently here and extended in ATTEMPT.md.
- 2026-10-11: `brain.py recall "Ginibre polynomial least singular value mistakes"`: no directly applicable verified resolution; recalled the warning to search for existing solutions before proving special cases.
- 2026-10-11: intake/codex-pool JSONL search for P0191: the initial rg command failed because PowerShell did not expand a directory wildcard; a Python glob/rglob fallback completed without printed matches. This is not a proof that no old attempt exists.
- 2026-10-11: read-only `git ls-tree -r --name-only origin/master` of ~/math-open-problems, followed by filtering paths for P0191/p0191: no matching paths. No working tree or repository content was modified.
- 2026-10-11: during the attempt, math-store recall requested for "noncommutative rank Gaussian matrix pencil least singular value" to look for a general full-rank linearization theorem beyond the source's identity-shift theorem.
  This additional read-only recall completed and was inspected. It returned row-extension, ordinary least-singular-value, Gaussian-conditioning/support, Schatten/stable-rank, and real hard-edge caution cards, but no full-noncommutative-rank Gaussian pencil theorem. No card is treated as settling the problem. Relevant conditioning card: claim_48af3a6fd03947cbcdabf6bd6b3e4cb1b207dec1875c259967eba79d14075634; finite-n hard-edge caution: claim_864ac65ee832a56f490f29ef75d94196e858e05abbcacda1533f60609dc9caa4. Our Gaussian covariance decomposition is proved directly and uses no hard-edge asymptotic formula.

- 2026-10-11: `https://arxiv.org/pdf/2606.01664`; response `source.pdf` (or adjacent error file).

- 2026-10-11: `http://export.arxiv.org/api/query?search_query=all:%22Ginibre%22+AND+all:%22polynomial%22&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending`; response `arxiv_search.xml` (or adjacent error file).

- 2026-10-11: `https://api.openalex.org/works?search=Brown%20measure%20convergence%20for%20the%20spectrum%20of%20polynomials%20in%20Ginibre%20matrices&per-page=10`; response `openalex_search.json` (or adjacent error file).

- 2026-10-11: `https://api.crossref.org/works?query=Ginibre%20polynomial%20least%20singular%20value&rows=20`; response `crossref_search.json` (or adjacent error file).

- 2026-10-11: `https://api.semanticscholar.org/graph/v1/paper/search?query=Brown%20measure%20convergence%20Ginibre&limit=10&fields=title,authors,year,externalIds,url`; response `semantic_search.json` (or adjacent error file).

- 2026-10-11: `https://api.github.com/search/repositories?q=Ginibre+polynomial+singular`; response `github_search.json` (or adjacent error file).

- 2026-10-11: `https://export.arxiv.org/api/query?search_query=all:%22least+singular%22+AND+all:%22polynomial%22&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending`; raw response `arxiv_targeted.xml` or adjacent error file.

- 2026-10-11: `https://api.openalex.org/works?search=Ginibre%20polynomials&per_page=10`; raw response `openalex_retry.json` or adjacent error file.

- 2026-10-11: `https://api.openalex.org/works/https://arxiv.org/abs/2606.01664`; raw response `openalex_source.json` or adjacent error file.

- 2026-10-11: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.01664?fields=title,authors,year,citationCount,citations.title,citations.externalIds,citations.year`; raw response `semantic_source.json` or adjacent error file.

- 2026-10-11: `https://api.crossref.org/works?query.bibliographic=Ginibre%20polynomial&filter=from-pub-date:2026-06-01&rows=20`; raw response `crossref_recent.json` or adjacent error file.

- 2026-10-11: `https://api.github.com/search/repositories?q=%222606.01664%22`; raw response `github_targeted.json` or adjacent error file.

- 2026-10-11: `https://api.github.com/repos/hanyi162013-Yihan/ginibre-lsv-lean/contents`; result `github_contents.json` or adjacent error file.

- 2026-10-11: `https://raw.githubusercontent.com/hanyi162013-Yihan/ginibre-lsv-lean/main/README.md`; result `github_readme.md` or adjacent error file.

- 2026-10-11: `https://api.openalex.org/works?filter=title.search:Brown%20measure%20convergence%20for%20the%20spectrum%20of%20polynomials%20in%20Ginibre%20matrices&select=id,title,doi,cited_by_count&per-page=5`; result `openalex_resolve.json` or adjacent error file.

- 2026-10-11: `https://export.arxiv.org/api/query?id_list=2511.01744`; result `citing_paper.xml` or adjacent error file.

- 2026-10-11: `https://export.arxiv.org/api/query?search_query=ti:%22Spectrum+and+pseudospectrum+for+quadratic+polynomials%22&max_results=5`; result `quadratic_search.xml` or adjacent error file.


## Second attempt: additional neighbouring-area searches

- 2026-10-11: `https://export.arxiv.org/api/query?search_query=ti:%22Gaussian+regularization%22+AND+all:%22pseudospectrum%22&max_results=5`, saved as `retry_pseudospectrum.xml` or adjacent error file.

- 2026-10-11: `https://api.crossref.org/works/10.1063/1.1704292`, saved as `retry_ginibre_reference.json` or adjacent error file.

- 2026-10-11: `https://export.arxiv.org/api/query?search_query=all:%22operator+scaling%22+AND+all:%22singular%22&max_results=10&sortBy=submittedDate&sortOrder=descending`, saved as `retry_operator_scaling.xml` or adjacent error file.

- 2026-10-11: brain math recall: `noncommutative rank singular deterministic coefficient Gaussian pencil operator scaling Gurvits`.

Second-attempt results: Crossref confirms Jean Ginibre, *Statistical Ensembles of Complex, Quaternion, and Real Matrices*, Journal of Mathematical Physics **6** (1965), 440--449, DOI **10.1063/1.1704292**. The standard finite-N complex eigenvalue kernel is the external known input used in RETRY_PROOF.md; every sublevel bound from it is derived explicitly there.

The pseudospectrum query returned Jess Banks, Archit Kulkarni, Satyaki Mukherjee, Nikhil Srivastava, *Gaussian Regularization of the Pseudospectrum and Davies' Conjecture*, **arXiv:1906.11819v4**. Its abstract concerns Gaussian regularization and diagonalizer condition numbers; it is a neighbouring-area method lead, not a paper asserted to solve Han's Question 1.6. Our truncated spectral-projection moment is proved directly from our own Gaussian deformation bound and Fatou, without importing an unverified quantitative theorem from this paper.

The broad operator-scaling/singular query returned four unrelated applied/physics records (retained in retry_literature_summary.txt). It did not provide a full-rank Gaussian-pencil bound. No absence theorem is inferred from this narrow query.

The gap-specific Gurvits/noncommutative-rank brain recall completed: it returned Lam's noncommutative-rings reference and Gaussian-conditioning/covariance/SVD cards, but no applicable quantitative pencil theorem. A second read-only recall, `Banks Kulkarni Mukherjee Srivastava pseudospectrum eigenvector overlap`, completed and returned, among other cards, a bounded-density bilinear-form result (claim_d9f3dbc365ca4e0870b0925e5f01e8fe, arXiv:2005.08930) and the high-nonnormality numerical warning (claim_1017be2729940a46aa4916004543d63e3f7681f54be5ed34acab17c956ea0ee3). Neither is used as a theorem settling the gap. The numerical warning was respected: numerical eigenvalues are only small-dimension diagnostic inputs; the probabilistic proof uses exact eigenvalue correlation laws and written norm inequalities.

No new search result is certified as SOLVED_IN_LITERATURE. The stronger polynomial classes proved in RETRY_PROOF.md are our reductions from standard inputs, not matching published solutions of the full question.
