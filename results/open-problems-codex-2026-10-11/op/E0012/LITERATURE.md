# Literature audit
Date: 2026-10-12 (machine date). API coverage limited to responses returned.

## Findings and references (not a declaration of a literature solution)

* Rick Durrett, “Coexistence in stochastic spatial models,” *Annals of Applied Probability* 19(2) (2009), 477–496, DOI **10.1214/08-AAP590**, arXiv:0906.2293. Source PDF saved as source.pdf, text as source.txt. Problem 6, PDF p.14, reads: “Show that coexistence is not possible in the colicin model when β1 < β2 and δ1 = δ2 = 1.” Rates appear in Example 2.3, PDF p.13. Coexistence is defined in the Case 1 discussion, PDF p.4, as an invariant distribution concentrated on configurations containing infinitely many individuals of each species. The survey uses Z^d and usually d=2; Problem 6 itself does not spell out a dimension/range quantifier.
* Nicolas Lanchier and Max Mercer, “Durrett-Levin spatial model of allelopathy,” *ALEA, Latin American Journal of Probability and Mathematical Statistics* **21 (2024), 321–343**, DOI **10.30757/ALEA.v21-14**, arXiv:2305.17016v1 (26 May 2023). Preprint saved as allelopathy.pdf; successfully fetched journal version saved as journal_retry.pdf, extracted text as journal_2024.txt. This is the exact rate model, with a uniform finite Euclidean-ball neighborhood. It is a major partial-result lead, not a solution of Problem 6.
* Rick Durrett and Simon A. Levin, “Allelopathy in Spatially Distributed Populations,” *Journal of Theoretical Biology* 185 (1997), 165–172, DOI **10.1006/jtbi.1996.0292**. Original model/mean-field/simulation reference, not a later proof.
* Nicolas Lanchier, “A multitype contact process with frozen sites: a spatial model of allelopathy,” *Journal of Applied Probability* 42 (2005), DOI **10.1239/jap/1134587820** (Crossref also returns publisher record 10.1017/S0021900200001145), arXiv:math/0401353. Different model with frozen sites; not a solution for density-dependent deaths.
* Claudia Neuhauser, “Ergodic theorems for the multitype contact process,” *Probability Theory and Related Fields* 91 (1992), 467–506. Relevant only for g=0 comparison and perturbation; not a solution for all positive g. Bibliography in the Lanchier–Mercer PDF is the reference source.

### Exact partial statements from Lanchier–Mercer, preprint

Theorem 1, PDF p.4 (line breaks in displayed math normalized):

> Theorem 1 For all β2 > β1 > βc, there is γ− > 0 such that
> γ < γ− ⇒ species 2 wins.

Theorem 2, PDF p.5:

> Theorem 2 For all β2 > β1 > βc, there is γ+ < ∞ such that
> γ > γ+ ⇒ species 1 survives.
> Species 1 wins if in addition M = d = 1.

The immediately following paragraph on PDF p.5 explicitly says:

> Numerical simulations suggest that clusters quickly form and either the susceptible species or the inhibitory species wins. In particular, we conjecture that, like in the mean-field model, coexistence is not possible except maybe for a parameter region with measure zero.

Line-by-line relevance and limits: (1) β2>β1 agrees with Problem 6; the paper additionally assumes both birth parameters exceed the one-type critical value. (2) Its rates (1), PDF p.2, coincide with the source's δ1=δ2=1 rates. (3) Theorem 1 covers only sufficiently small γ. (4) Theorem 2 gives survival, not extinction of the other type, in general d. (5) Its winning conclusion at large γ additionally restricts d=M=1. (6) Neither statement covers intermediate γ in d=2. (7) The phase statement (9), PDF p.6, follows only after the stated conjecture, so cannot be treated as a proved all-parameter noncoexistence theorem. (8) Its 'both survive' formulation and assumptions on a translation-invariant initial law also require attention when applying results to the survey's invariant-law formulation. No **SOLVED_IN_LITERATURE** designation is justified.

### Published-version verification

The successful browser-agent/query-string retry allowed inspection of the published journal version, including all introduction theorem statements and its explicit open-problem statement. Theorem numbers change to 1.1–1.5.

Theorem 1.1, printed p.324, PDF p.4:

> Theorem 1.1. For all β2 > β1 > βc, there is γ− > 0 such that
> γ < γ− ⇒ species 2 wins.

Theorem 1.2, printed p.324, PDF p.4:

> Theorem 1.2. For all β2 > β1 > βc, there is γ+ < ∞ such that
> γ > γ+ ⇒ species 1 survives.
> Species 1 wins if in addition M = d = 1.

Theorem 1.4, printed p.326, PDF p.6:

> Theorem 1.4. For all β1, γ > 0, there is β+ < ∞ such that
> β2 > β+ ⇒ species 2 wins.

Most decisively, printed p.327, PDF p.7, says word for word (line breaks normalized):

> The phase structure does not show any coexistence phase because this is what our numerical simulations suggest. However, the absence of a phase of coexistence in the spatial model is still an open problem.

The conjecture on printed p.325 has the same wording as the preprint quotation above. Thus the published version explicitly confirms that its theorems do not close E0012. Theorem 1.3 assumes equal birth parameters (outside the strict inequality in E0012) and d≥3. Theorem 1.5, p.326, only proves species-2 survival for large range when β2>β1²>1 and γ≤β1. It does not prove extinction of species 1. These statements do not bridge the gap.

### Coverage and failures

Every API URL/query and its response is logged below; raw successful responses remain in the folder. arXiv searches for colicin alone missed the relevant paper, while allelopathy found it. Crossref exact-title search identified the 2024 journal version. Semantic Scholar's source-citation endpoint returned 27 records (see semantic_retry.json and final_search.txt); none of the returned titles states this noncoexistence theorem. Its 2023-paper citation endpoint returned an empty data list, which is an indexing result, not proof that there are no citing papers. GitHub returned ingallslab/colicin_model, ingallslab/colicin-ODE-model and Pavi31/Plasmid_Genome_conflicts; these repository search hits do not establish a theorem. The allelopathy-contact-process repository query returned no hits.

OpenAlex returned HTTP 429 on both search queries and correct DOI resolution. Its citing-works query could not be constructed from a resolved work ID. This portion of the requested citation audit is incomplete; it must not be described as a negative literature result. The initial OpenAlex DOI request used the wrong DOI 10.1214/09-PS153; after extracting the source header this was corrected to 10.1214/08-AAP590 and retried, again returning 429. No result was inferred from the failed request.

Brain/prior work: called math_recall.py on “colicin Durrett Levin competition”; recalled memories on “colicin model” and “colicin model mistakes,” neither of which contained colicin. Read the E0012 intake entry and attempt in probability_1000_intake_E_20260908. Its non-attractiveness assertion and scalar-PDE inference are invalid (see ATTEMPT.md). Read-only git ls-tree of origin/master in math-open-problems found no path named E0012 or colicin; this is a filename check, not a full content search. A second math-store query on “multitype contact process Neuhauser competitive exclusion” is saved in brain_contact_process.txt.

## Raw search log

Journal-version follow-up: 2026-10-12, https://alea.impa.br/articles/v21/21-14.pdf returned HTTP 400 (saved in journal_inspection.txt). Crossref gives ALEA volume 21, start page 321, 2024, DOI 10.30757/alea.v21-14. This failed request was superseded by the successful retry below.

Journal retry: 2026-10-12, Python urllib with browser user agent, https://alea.impa.br/articles/v21/21-14.pdf?download=1 succeeded (1,425,055 bytes saved as journal_retry.pdf). Extracted all 23 pages into journal_2024.txt; inspected PDF pp.1–7 for the model, all main theorem statements and the explicit open-problem assertion.

The second math-store recall returned generic interacting-particle-system and unrelated exclusion/branching-process cards, not a model-specific extinction theorem. None was used as a mathematical authority.

Recorded-answer follow-up, 2026-10-12: read-only git grep of origin/master for E0012 or colicin in *.md and *.jsonl (raw output in published_content_matches.txt) found the October list, the same September intake attempt in duplicate locations, and the September campaign report's E0012 entry. The E0012 entries record attempted_unsolved/source_says_open and repeat the defective scalar-PDE/non-attractiveness argument, rather than a checked proof. A git show of the report section was used for the follow-up read; no working tree was touched.

('source', 'OK', 502730, 'https://arxiv.org/pdf/0906.2293')

('arxiv', 'OK', 7605, 'https://export.arxiv.org/api/query?search_query=all:colicin&max_results=30')

('openalex', 'ERROR', 'HTTP Error 429: Too Many Requests', 'https://api.openalex.org/works?search=colicin%20interacting%20particle&per-page=30')

('crossref', 'OK', 269560, 'https://api.crossref.org/works?query=colicin%20spatial%20model&rows=30')

('semantic', 'ERROR', 'HTTP Error 429: ', 'https://api.semanticscholar.org/graph/v1/paper/search?query=colicin%20spatial%20model&limit=30&fields=title,authors,year,externalIds,abstract')

('github', 'OK', 16377, 'https://api.github.com/search/repositories?q=colicin+model&per_page=30')

('openalex_source', 'ERROR', 'HTTP Error 429: Too Many Requests', 'https://api.openalex.org/works/https://doi.org/10.1214/09-PS153')

2026-10-12 ['arxiv_allelopathy', 'https://export.arxiv.org/api/query?search_query=all:allelopathy&max_results=50', 'OK', 11911]

2026-10-12 ['crossref_allelopathy', 'https://api.crossref.org/works?query=allelopathy%20contact%20process&rows=25', 'OK', 88358]

2026-10-12 ['openalex_retry', 'https://api.openalex.org/works?search=allelopathy%20contact%20process&per_page=25', 'ERROR', 'HTTP Error 429: Too Many Requests']

2026-10-12 ['openalex_source_correct', 'https://api.openalex.org/works/https://doi.org/10.1214/08-AAP590', 'ERROR', 'HTTP Error 429: Too Many Requests']

2026-10-12 ['semantic_retry', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0906.2293/citations?limit=100&fields=title,year,authors,externalIds', 'OK', 11751]

2026-10-12 ['github_allelopathy', 'https://api.github.com/search/repositories?q=allelopathy+contact+process&per_page=20', 'OK', 55]

2026-10-12 fetched https://arxiv.org/pdf/2305.17016 OK

2026-10-12 fetched https://api.crossref.org/works?query.title=Durrett-Levin%20spatial%20model%20of%20allelopathy&rows=5 OK

2026-10-12 ['arxiv_targeted', 'https://export.arxiv.org/api/query?search_query=all:%22colicin%22+OR+all:%22allelopathic%22+OR+all:%22allelopathy%22&sortBy=submittedDate&sortOrder=descending&max_results=100', 'OK', 30053]

2026-10-12 ['openalex_doi_filter', 'https://api.openalex.org/works?filter=doi:https://doi.org/10.1214/08-AAP590&per-page=1', 'ERROR', 'HTTP Error 429: Too Many Requests']

2026-10-12 ['semantic_later', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2305.17016/citations?limit=100&fields=title,year,authors,externalIds', 'OK', 26]

2026-10-12 ['crossref_later', 'https://api.crossref.org/works?query=Durrett%20Levin%20allelopathy%20Lanchier%20Mercer&rows=15', 'OK', 86980]
