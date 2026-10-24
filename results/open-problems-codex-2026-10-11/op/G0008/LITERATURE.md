# Literature search

Date: 2026-10-11 (local). All requests use Python urllib; response files preserved.

- source_pdf: `https://arxiv.org/pdf/2601.00291` — ('source_pdf', 200, 447630)
- source_abs: `https://arxiv.org/abs/2601.00291` — ('source_abs', 200, 40303)
- arxiv: `https://export.arxiv.org/api/query?search_query=all:%22percolation%22+AND+all:%22monotonicity%22&start=0&max_results=40&sortBy=submittedDate&sortOrder=descending` — ('arxiv', 200, 82693)
- openalex: `https://api.openalex.org/works?search=probability%20connection%20monotone%20percolation&per-page=25` — ('openalex', 'HTTP Error 429: Too Many Requests')
- crossref: `https://api.crossref.org/works?query=percolation%20connection%20monotonicity&rows=25` — ('crossref', 200, 139149)
- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2601.00291?fields=title,authors,year,citations.title,citations.year,citations.externalIds` — ('semantic', 'HTTP Error 429: ')
- github: `https://api.github.com/search/repositories?q=percolation+monotonicity` — ('github', 200, 55)

- 2026-10-11 openalex_retry: `https://api.openalex.org/works?search=monotonicity%20Bernoulli%20bond%20percolation&per_page=10` — HTTP Error 429: Too Many Requests

- 2026-10-11 openalex_source: `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2601.00291` — HTTP Error 429: Too Many Requests

- 2026-10-11 arxiv_2015: `https://export.arxiv.org/api/query?search_query=ti:%22remark%20on%20monotonicity%22&max_results=10` — OK 4673 bytes

- 2026-10-11 semantic_search: `https://api.semanticscholar.org/graph/v1/paper/search?query=monotonicity%20Bernoulli%20percolation&limit=10&fields=title,authors,year,externalIds` — HTTP Error 429: 

- 2026-10-11 github_title: `https://api.github.com/search/repositories?q=%22percolation%22+%22connection%22` — OK 39179 bytes

- 2026-10-11 arxiv_recent: `https://export.arxiv.org/api/query?search_query=all:%22percolation%22+AND+(all:%22two-point%22+OR+all:%22connection%22)+AND+submittedDate:[202601010000+TO+202610112359]&max_results=100&sortBy=submittedDate&sortOrder=descending` — OK 212109 bytes

- 2026-10-11 crossref_since: `https://api.crossref.org/works?query=percolation%20two%20point%20monotonicity&filter=from-pub-date:2026-01-01&rows=25` — OK 108499 bytes

- 2026-10-11 openalex_citing: `https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2601.00291&per-page=50` — HTTP Error 429: Too Many Requests

- 2026-10-11 arxiv_exact: `https://export.arxiv.org/api/query?search_query=(all:%222601.00291%22+OR+ti:%22monotonicity%22)+AND+all:%22percolation%22&max_results=100&sortBy=submittedDate&sortOrder=descending` — OK 56239

- 2026-10-11 old_pdf: `https://arxiv.org/pdf/1110.0927v5` — OK 246117

- 2026-10-11 layered_pdf: `https://arxiv.org/pdf/2207.13173` — OK 275577

- 2026-10-11 corrected exact 2015 PDF fetch: https://arxiv.org/pdf/1504.06549. The earlier old_pdf file accidentally selected an unrelated Lagrangian paper from the broad title results; it is excluded.

- 2026-10-11 openalex_title: `https://api.openalex.org/works?search=%22The%20probability%20of%20connection%20between%20two%20vertices%22&per-page=5` — HTTP Error 429: Too Many Requests

- 2026-10-11 semantic_citing: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2601.00291/citations?fields=title,year,authors,externalIds&limit=100` — OK 26

- 2026-10-11 crossref_exact: `https://api.crossref.org/works?query.title=The%20probability%20of%20connection%20between%20two%20vertices%20cannot%20be%20monotone%20with%20the%20distance&rows=5` — OK 25766

- 2026-10-11 arxiv_recent_page2: `https://export.arxiv.org/api/query?search_query=all:%22percolation%22+AND+(all:%22two-point%22+OR+all:%22connection%22)+AND+submittedDate:[202601010000+TO+202610112359]&start=100&max_results=100&sortBy=submittedDate&sortOrder=descending` — OK 99105


## Search assessment and exact relevant references (2026-10-11)

1. Alberto M. Campos and Bernardo N. B. de Lima, *The probability of connection between two vertices cannot be monotone with the distance for Bernoulli Percolation on transitive graphs*, arXiv:2601.00291v1, submitted 1 January 2026. https://arxiv.org/abs/2601.00291. Downloaded current PDF and abstract record; PDF header gives v1. Abstract p.1 explicitly leaves axial square-lattice monotonicity open, p.2 defines ordinary iid bond percolation, and Section 3 p.4 repeats openness. Its counterexamples are on other graphs or in Pipe-Dust with noninteger points, not the requested lattice-vertex axis question.

2. Bernardo N. B. de Lima, Aldo Procacci and Remy Sanchis, *A remark on monotonicity in Bernoulli bond Percolation*, Journal of Statistical Physics **160** (2015), 1244-1248. DOI: 10.1007/s10955-015-1284-z. arXiv:1504.06549v1. https://arxiv.org/abs/1504.06549. Downloaded exact PDF to lps_2015.pdf; text to lps_2015.txt. Theorem 1(i), PDF p.2: for every d>=2 there exists p'>0 such that the ordinary axial connection probabilities strictly decrease for all n when 0<p<p'. Theorem 1(ii): for p sufficiently close to 1, the analogous statement is for the FINITE-CLUSTER (truncated) function. It does not claim the every-p question or the full supercritical function. The abstract says anisotropic but the displayed main theorem specifies ordinary percolation; we use the theorem's exact scope.

3. Philipp Koenig and Thomas Richthammer, *Monotonicity properties for Bernoulli percolation on layered graphs -- a Markov chain approach*, Stochastic Processes and their Applications **181** (2025), article 104549. DOI: 10.1016/j.spa.2024.104549. arXiv:2207.13173v1 (26 July 2022). https://arxiv.org/abs/2207.13173. Downloaded layered_pdf.pdf and text. Their finite transverse graph G times Z theorem gives eventual monotonicity uniformly in p, after an onset depending on G. The abstract and Conjecture 1 explicitly include Z^2 as unresolved motivation. Width-dependent eventual results do not imply fixed-distance monotonicity in Z^2.

4. Geoffrey Grimmett, *Percolation*, 2nd ed., Grundlehren der mathematischen Wissenschaften **321**, Springer, Berlin, 1999. DOI: 10.1007/978-3-662-03981-6. Standard background for Harris association, square-lattice critical point and absence of a critical infinite cluster. Referenced in both downloaded percolation sources; no new independent full-book fetch was performed.

5. J. M. Hammersley and D. J. A. Welsh, *First-Passage Percolation, Subadditive Processes, Stochastic Networks, and Generalized Renewal Theory*, in *Bernoulli 1713, Bayes 1763, Laplace 1813*, Springer, 1965, pp. 61-110. DOI: 10.1007/978-3-642-99884-3_7. Historical analogy in first-passage percolation; the downloaded 2026 source traces its distance question to this paper. This is not itself a theorem settling Bernoulli connection monotonicity.

### Accessible follow-up searches

- arXiv's monotonicity/percolation title and all-field searches included results through October 2026, with no later all-p/all-n axial solution surfaced.
- The 2026 connection/two-point/percolation query returned 144 results. Both pages (100 and 44 entries) were fetched and titles/pertinent abstracts inspected; no settling paper was found. Responses are preserved for independent inspection.
- Crossref broad, date-restricted and exact-source-title searches returned no settling result. The broad query recovered the layered-graph publication.
- Semantic Scholar's initial paper/search requests returned 429, but its explicit source citations endpoint succeeded at the final check: {"offset":0,"data":[]}. This means zero citing works in that endpoint's current index, not a proof that no citing paper exists.
- OpenAlex search and source-DOI lookup requests repeatedly returned 429. A real OpenAlex source W-id could not be obtained, so a reliable works-citing-source search could not be completed. The attempted cites:doi filter request also failed with 429; that filter is not a substitute for a proper W-id lookup and is NOT claimed as a successful citation search.
- GitHub repository search "percolation monotonicity" returned zero repositories. The broader "percolation connection" query returned six unrelated algorithm/simulation repositories, recorded in github_title.response; none settled the question.

Conclusion: no literature solution was found in these bounded accessible searches; source still labels the question open. OpenAlex limitations prevent an exhaustive status claim. Publication novelty of our partial certificates is unverified. VERDICT is PARTIAL, not SOLVED_IN_LITERATURE.

### Read-only brain and prior-work searches

On 2026-10-11 ran brain.py recall for "percolation connection distance monotonicity mistakes" and "percolation two point connection monotonicity", and math_recall.py for "percolation two point monotonicity reflection". Retrieved cards were mostly off-target and were not used as mathematical authority. Local rg over the specified intake and codex-pool JSONL files for G0008 recovered the G intake A001/A002 correction. Git ls-tree origin/master filtered for G0008, followed by git show of its mathematical MD artifacts, admissions and terminal handoff, recovered the critical-star and finite-partition attempts. Exact matching paths are preserved in prior_paths.txt; MD copies are prior_*.md. No brain store or git checkout was changed.


## Continuation brain queries, 2026-10-11

- math_recall.py "percolation axial connectivity monotonicity width uniform transfer Bernstein wired boundary Koenig Richthammer": mostly unrelated cards; relevant continuity source Aizenman--Kesten--Newman, *Uniqueness of the infinite cluster and continuity of connectivity functions for short and long range percolation* (1987), DOI 10.1007/bf01219071. No returned card settled the gap.
- math_recall.py "Messager Miracle Sole inequality random cluster reflection positivity Potts q": recovered Froehlich, Israel, Lieb and Simon, *Phase transitions and reflection positivity. I. General theory and long range lattice models*, Communications in Mathematical Physics **62** (1978), 1-34, DOI 10.1007/bf01940327, and a prior random-cluster lace-expansion attempt card. Its suggestion of automatically extending Potts reflection positivity to noninteger q was treated only as a hint; the explicit three-terminal boundary-join matrix calculation shows the attempted positivity step fails for 1<q<2. No new bibliographic assertion was inferred from that card.

This continuation focused on the new common-boundary comparison proof. The earlier bounded literature status remains unchanged; novelty of the uniform n=1 theorem is not claimed.
