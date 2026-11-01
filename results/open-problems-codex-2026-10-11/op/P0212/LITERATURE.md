
## Searches on 2026-10-11

Status: no theorem proving the complete two-model stationary genealogical limit was identified in this bounded search. This is not a certification that no such paper exists. Some services were rate-limited. No SOLVED_IN_LITERATURE claim is made.

## Relevant sources and assessment

1. David Aldous, *The low-density limit of coalescing branching random walk*, Problem A, 2012, update March 2018. Author's web page, URL below. Exact target, not a proof. The linked talk *The constrained Ising model as an algorithm for storage in dynamic graphs*, slides 16–17, gives the edge-additive Ising rates and the heuristic walk rate O(p), splitting rate O(p^2).
2. Siva R. Athreya and Jan M. Swart, *Branching-coalescing particle systems*, Probability Theory and Related Fields **131** (2005), 376–414; source-linked preprint isid/ms/2003/22, August 8, 2003, 43 PDF pages. Downloaded and extracted as athreya.pdf and athreya_text.txt. The abstract and main-results setting concern invariant laws and convergence using duality, not a beta-down-to-zero stationary genealogical limit. Their model also permits finite-rate coalescence and deaths, so its general invariant-law discussion must not override the immediate-coalescence detailed-balance calculation for the concrete source model.
3. Athreya and Swart, *Correction to: Branching-coalescing particle systems*, arXiv:0904.2288 (2009). Retrieved via the arXiv title query; the correction says original Theorem 7's duality identity need only hold almost everywhere in time, rather than at every time. A caution when using that theorem. No use of the corrected theorem is needed in our proofs.
4. Natesh S. Pillai and Aaron Smith, *Mixing times for a constrained Ising process on the torus at low density*, Annals of Probability **45**(2) (2017), 1003–1070, DOI 10.1214/15-AOP1080. Source-linked PDF downloaded. Theorem 2, printed page 1006 (PDF page 4), bounds discrete-time torus mixing by C1 n^3 <= tau_mix <= C2 n^3 log n for p=c/n, d>=3. Its counterexample concerns the separate finite-graph mixing-time conjecture, not Problem A's genealogy. Furthermore their at-least-one-neighbor constraint differs from the talk's sum-of-occupied-neighbors clock when several neighbors are occupied. The two rates are comparable on bounded-degree graphs, which is not an equality of genealogical laws.
5. Ivailo Hartarsky, Fabio Martinelli and Cristina Toninelli, *Coalescing and branching simple symmetric exclusion process*, Annals of Applied Probability **32**(4) (2022), 2841–2859, DOI 10.1214/21-AAP1750; arXiv:2006.01426, v2 dated February 9, 2021. Full arXiv PDF downloaded as cbsep.pdf (text cbsep_text.txt). Introduction, PDF page 1, explicitly gives Bernoulli(beta/(1+beta)) reversibility for the immediate branching/coalescing walk. Section 1.1, PDF page 2, gives the same model up to global time rescaling. Thus our Proposition 1 rederives a known fact, not a new stationary-law theorem. Theorem 1 and Corollaries 3.1–3.2 concern logarithmic Sobolev constants, relaxation, and mixing on finite graphs. They do not state the stationary rooted split/merge graph limit. The later Semantic Scholar citing-paper list was also checked at title/abstract level; none states the full target.
6. Assaf Shapira, *A Note on the Spectral Gap of the Fredrickson–Andersen One Spin Facilitated Model*, Journal of Statistical Physics **181**(6) (2020), 2346–2352, DOI 10.1007/s10955-020-02666-1. Exact author/title/DOI and publication details confirmed via Crossref; also appears in Pillai–Smith and CBSEP citing-paper searches. Abstract describes sharp spectral-gap exponents and finite-graph bounds, not the recursive genealogical limit. Lead only, not read as a full proof of Problem A.
7. Rick Durrett and Wai-Tong Louis Fan, *Genealogies in Expanding Populations*, arXiv:1507.00918, v2. API abstract inspected. It treats a one-dimensional long-range biased voter model and a dual converging to branching Brownian motion with coalescence by intersection local time. This is a spatial, recurrent, different scaling limit; it does not answer the stationary transient space-forgotten two-model question.

Other screened arXiv genealogy papers include Imanol Nuñez and José Luis Pérez, *The frequency process in a non-neutral two-type continuous-state branching process with competition and its genealogy*, arXiv:2406.04255; Adrián González Casanova, Dario Spanò and Maite Wilke-Berenguer, *The effective strength of selection in random environment*, arXiv:1903.12121; and Adrian Gonzalez Casanova, Veronica Miro Pina and Juan Carlos Pardo, *The Wright-Fisher model with efficiency*, arXiv:1902.07359. Their abstract-level population genetics/continuous-state objects do not match this question. The broad low-density arXiv query also returned irrelevant astrophysics; those hits were discarded. The math.PR-filtered query screened 80 recent title/abstract records and reached the CBSEP paper; the final phrase-restricted query returned no entries. Search coverage is finite, and this is explicitly not a global nonexistence result.

## Citation-search limitations

The Aldous source is an unnumbered web page with no supplied DOI. The OpenAlex source-title lookup and all OpenAlex works queries returned HTTP 429, including a direct DOI lookup of Pillai–Smith; therefore no OpenAlex source work ID could be established and a valid works-citing-that-ID query could not be formed. A Semantic Scholar URL lookup of the Aldous page also returned HTTP 429. Do not describe the source's citation graph as fully checked. Semantic Scholar DOI citation queries for the identifiable Pillai–Smith and CBSEP papers succeeded, and their results are preserved. GitHub's repository query returned total_count=0. Crossref title queries succeeded, but broad query ranks were often unrelated.

## Read-only brain / prior-work checks

- Before the attempt: brain.py recall for "branching coalescing walks low density mistakes" and for the full title; no directly useful verified memory was returned.
- math_recall.py --id claim_a957a3ebd565ceaf68665829f95158697343dbfcf0342e25a65486418e6a49d5: read the full earlier isolated-pair attempt, rechecked its Green identity, and avoided its unproved Poisson-thinning inference.
- During the attempt: math_recall.py on "branching coalescing exclusion Bernoulli reversible Hartarsky Martinelli Toninelli".
- rg over the permitted probability_1000_intake_* directories and codex_pool_2026_10_10 for P0212 and title fragments: found the old ranking entry calling the problem attempted-unsolved, but no matching detailed attempt text. An initial literal Windows glob path failed and was replaced with an enumerated directory list.
- git ls-tree origin/master in the read-only math-open-problems checkout, filtered for P0212 / coalescing-branch names: no matching named paths. The working tree was not touched.

## Search log (URLs, dates, success/failure and raw responses)

Primary-source fetch: https://www.stat.berkeley.edu/~aldous/Research/OP/cbrw.html, 2026-10-11, successful; preserved as source.html. Problem A and its construction were read in full. It remains phrased as a conjectural convergence, with an update in March 2018 about related torus mixing work. Model 1 uses Z^3 for concreteness, transience, nearest-neighbor daughters, continuous simple walks, stationary intensity tending to zero. Model 2 uses iid Bernoulli equilibrium and the dynamics on slides 16–17 of the linked talk. Dynamic-graph Problem B is not included.
- arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22branching%20coalescing%22%20AND%20%28all%3A%22low%20density%22%20OR%20all%3Agenealogy%20OR%20all%3Agenealogical%29&max_results=30
  Result: OK 8523 bytes
- openalex: https://api.openalex.org/works?search=low%20density%20branching%20coalescing%20random%20walk%20genealogy&per-page=20
  Result: <HTTPError 429: 'Too Many Requests'>
- crossref: https://api.crossref.org/works?query=low%20density%20coalescing%20branching%20random%20walk&rows=20
  Result: OK 201481 bytes
- semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=branching%20coalescing%20genealogy&limit=20&fields=title,authors,year,url,abstract
  Result: <HTTPError 429: ''>
- github: https://api.github.com/search/repositories?q=branching%20coalescing%20random%20walk
  Result: OK 55 bytes
- ising: https://www.stat.berkeley.edu/~aldous/Talks/persi-ising.pdf
  Result: OK 81709 bytes
- pillai: https://www.stat.berkeley.edu/~aldous/Research/OP/pillai-smith.pdf
  Result: OK 1294234 bytes
- athreya: https://www.isid.ac.in/~statmath/eprints/2003/isid200322.pdf
  Result: OK 361966 bytes
- openalex_source: https://api.openalex.org/works?search=The%20low-density%20limit%20of%20coalescing%20branching%20random%20walk&per-page=10
  Result: <HTTPError 429: 'Too Many Requests'>
- arxiv_low, 2026-10-11: https://export.arxiv.org/api/query?search_query=all%3A%22coalescing%22%20AND%20all%3A%22low%20density%22&max_results=60
  Result: OK 125595 bytes
- arxiv_ising, 2026-10-11: https://export.arxiv.org/api/query?search_query=%28all%3A%22constrained%20Ising%22%20OR%20all%3A%22FA-1f%22%29%20AND%20%28all%3Alimit%20OR%20all%3Abranching%29&max_results=60
  Result: OK 4352 bytes
- openalex_pillai, 2026-10-11: https://api.openalex.org/works/https://doi.org/10.1214/15-AOP1080
  Result: <HTTPError 429: 'Too Many Requests'>
- semantic_pillai_citations, 2026-10-11: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/15-AOP1080/citations?fields=title,year,authors,abstract&limit=100
  Result: OK 17537 bytes
- crossref_genealogy, 2026-10-11: https://api.crossref.org/works?query=constrained%20Ising%20genealogy%20scaling%20limit&rows=25
  Result: OK 249059 bytes
- arxiv_athreya, 2026-10-11: https://export.arxiv.org/api/query?search_query=ti%3A%22Branching-coalescing%20particle%20systems%22&max_results=10
  Result: OK 1954 bytes
- arxiv_mathlow, 2026-10-11: https://export.arxiv.org/api/query?search_query=cat%3Amath.PR%20AND%20all%3Acoalescing%20AND%20%28all%3Adensity%20OR%20all%3Agenealogy%29&max_results=80&sortBy=submittedDate&sortOrder=descending
  Result: OK 155803 bytes
- arxiv_cbsep, 2026-10-11: https://export.arxiv.org/api/query?search_query=ti%3A%22Coalescing%20and%20branching%20simple%20symmetric%20exclusion%20process%22&max_results=10
  Result: OK 2737 bytes
- semantic_cbsep, 2026-10-11: https://api.semanticscholar.org/graph/v1/paper/020d65a04951ea2d5d626cf83796d35c81175360?fields=title,authors,year,externalIds,url
  Result: OK 513 bytes
- crossref_cbsep, 2026-10-11: https://api.crossref.org/works?query.title=Coalescing%20and%20branching%20simple%20symmetric%20exclusion%20process&rows=3
  Result: OK 32679 bytes
- cbsep.pdf, 2026-10-11: https://arxiv.org/pdf/2006.01426
  Result: OK 300850
- arxiv_focused.txt, 2026-10-11: https://export.arxiv.org/api/query?search_query=cat%3Amath.PR%20AND%20%28all%3A%22branching-coalescing%22%20OR%20all%3A%22branching%20coalescing%22%29%20AND%20%28all%3A%22low-density%22%20OR%20all%3A%22low%20density%22%20OR%20all%3Alineages%29&max_results=50&sortBy=relevance
  Result: OK 964
- semantic_cbsep_citations, 2026-10-11: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/21-AAP1750/citations?fields=title,year,authors,abstract&limit=100
  Result: OK 10897
- semantic_source, 2026-10-11: https://api.semanticscholar.org/graph/v1/paper/URL:https%3A%2F%2Fwww.stat.berkeley.edu%2F~aldous%2FResearch%2FOP%2Fcbrw.html?fields=title,year,citationCount
  Result: <HTTPError 429: ''>
- crossref_shapira, 2026-10-11: https://api.crossref.org/works?query.title=A%20Note%20on%20the%20Spectral%20Gap%20of%20the%20Fredrickson%20Andersen%20One%20Spin%20Facilitated%20Model&rows=3
  Result: OK 19132

## Second-attempt named-theorem verification
- 2026-10-11: https://api.crossref.org/works/10.1214/aop/1176996798; OK 1753; saved as kingman_crossref.json
- 2026-10-11: https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf; OK 2195717; saved as durrett_PTE5.pdf

Second attempt: full math-store Kingman card read and independently checked against Durrett PTE5 author PDF, Theorem 6.4.1, printed p.343 / PDF p.351. Extracted statement in subadditive_reference.txt. J. F. C. Kingman (1968), JRSS B 30, 499-510; Kingman (1973), Ann. Probab. 1(6), 883-909, DOI 10.1214/aop/1176996798. No literature solution to P0212 is inferred. Brain gap query returned the earlier attempt and a caution that a Wiener-sausage reduction alone does not close a geometry problem; named Kingman query supplied the theorem hypotheses, checked here independently.
