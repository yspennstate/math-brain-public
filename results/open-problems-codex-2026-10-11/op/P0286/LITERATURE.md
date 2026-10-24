# Literature and status check — 12 October 2026

No paper checked here proves the full canonical growing-ring covariance question with its density regimes and finite-size corrections. The verdict is not SOLVED_IN_LITERATURE. Searches are bounded and some services were rate-limited; this is not a proof that no solution exists.

## Source

Leonid Petrov and Axel Saenz (organizers), Evan Sorensen (moderator), Hieu Trung Vu (scribe), *AIM Workshop: All roads to KPZ Universality Open Problems*, March 19, 2025, Section 5, PDF p.3. Downloaded from https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ.pdf into source.pdf; full extraction source.txt. Exact question quoted in ATTEMPT.md. The statement supplies no asymmetry parameter or quantitative limiting regime.

## API searches (raw responses retained)

- 2026-10-12; arxiv_recent; query URL: https://export.arxiv.org/api/query?search_query=all%3AASEP+AND+%28all%3Acorrelation+OR+all%3Astationary%29+AND+submittedDate%3A%5B20250319+TO+20261012%5D&max_results=50. Result: 200; arxiv_recent.txt
- 2026-10-12; arxiv_queue; query URL: http://export.arxiv.org/api/query?search_query=all%3AASEP+AND+all%3Aqueue&max_results=30. Result: 200; arxiv_queue.txt
- 2026-10-12; openalex; query URL: https://api.openalex.org/works?search=two+species+ASEP+stationary+correlations&per-page=25. Result: HTTP Error 429: Too Many Requests
- 2026-10-12; openalex_source; query URL: https://api.openalex.org/works?search=All+roads+to+KPZ+Universality+Open+Problems&per-page=5. Result: HTTP Error 429: Too Many Requests
- 2026-10-12; crossref; query URL: https://api.crossref.org/works?query=two+species+ASEP+stationary+correlations&rows=25. Result: 200; crossref.txt
- 2026-10-12; semantic; query URL: https://api.semanticscholar.org/graph/v1/paper/search?query=two+species+ASEP+stationary+correlations&limit=20&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract. Result: HTTP Error 429: 
- 2026-10-12; github; query URL: https://api.github.com/search/repositories?q=ASEP+stationary+correlations&per_page=20. Result: 200; github.txt
- 2026-10-12; arxiv_spatial; query URL: https://export.arxiv.org/api/query?search_query=%28all%3A%22multi-species%22+OR+all%3A%22two-species%22%29+AND+%28all%3Acorrelations+OR+all%3Acovariance%29&max_results=50. Result: 200; arxiv_spatial.txt
- 2026-10-12; arxiv_horizon; query URL: https://export.arxiv.org/api/query?search_query=all%3A%22stationary+horizon%22&max_results=30. Result: 200; arxiv_horizon.txt
- 2026-10-12; crossref_focused; query URL: https://api.crossref.org/works?query.title=Decoupling+and+decay+of+two-point+functions+in+a+two-species+ASEP&rows=5. Result: 200; crossref_focused.txt
- 2026-10-12; openalex_retry; query URL: https://api.openalex.org/works?search=ASEP+covariance&per-page=10. Result: HTTP Error 429: Too Many Requests
- 2026-10-12; semantic_retry; query URL: https://api.semanticscholar.org/graph/v1/paper/arXiv:2504.00765?fields=title,authors,year,citations.title,citations.externalIds. Result: HTTP Error 429: 

OpenAlex source discovery and retry both returned HTTP 429. No indexed work ID for the workshop source could be obtained, so its citing-works endpoint could not be addressed. This citation-following branch remains incomplete. Semantic Scholar search and the known-paper citation endpoint also returned HTTP 429. GitHub returned zero repositories. Crossref broad search mostly returned irrelevant items; focused search and arXiv identified the leads below.

## Relevant records and classification

- Patrik L. Ferrari, Sabrina Gernholt. *Decoupling and decay of two-point functions in a two-species (T)ASEP*. http://arxiv.org/abs/2504.00765v3; first submitted 2025-04-01T13:17:35Z, last update 2026-07-20T13:52:13Z.
- James B. Martin. *Stationary distributions of the multi-type ASEP*. http://arxiv.org/abs/1810.10650v3; first submitted 2018-10-24T23:03:41Z, last update 2020-03-08T14:55:48Z.
- Amol Aggarwal, Matthew Nicoletti, Leonid Petrov. *Colored Interacting Particle Systems on the Ring: Stationary Measures from Yang-Baxter Equation*. http://arxiv.org/abs/2309.11865v2; first submitted 2023-09-21T08:08:13Z, last update 2025-06-21T06:22:09Z.
- Olya Mandelshtam. *New formulas for Macdonald polynomials via the multispecies exclusion and zero range processes*. http://arxiv.org/abs/2508.04666v1; first submitted 2025-08-06T17:35:46Z, last update 2025-08-06T17:35:46Z.
- Ofer Busani, Timo Seppäläinen, Evan Sorensen. *The stationary horizon and semi-infinite geodesics in the directed landscape*. http://arxiv.org/abs/2203.13242v8; first submitted 2022-03-24T17:51:05Z, last update 2023-10-13T17:50:43Z.
- Evan Sorensen. *The stationary horizon as the central multi-type invariant measure in the KPZ universality class*. http://arxiv.org/abs/2306.09584v2; first submitted 2023-06-16T02:01:19Z, last update 2023-10-13T17:21:45Z.
- Ofer Busani, Timo Seppäläinen, Evan Sorensen. *Scaling limit of the TASEP speed process*. http://arxiv.org/abs/2211.04651v4; first submitted 2022-11-09T02:58:18Z, last update 2023-04-14T12:28:17Z.
- Ofer Busani, Timo Seppäläinen, Evan Sorensen. *Scaling limit of multi-type invariant measures via the directed landscape*. http://arxiv.org/abs/2310.09284v4; first submitted 2023-10-13T17:52:09Z, last update 2024-07-29T21:59:16Z.
- Amol Aggarwal, Ivan Corwin, Milind Hegde. *Scaling limit of the colored ASEP and stochastic six-vertex models*. http://arxiv.org/abs/2403.01341v2; first submitted 2024-03-02T23:29:04Z, last update 2024-04-27T16:57:38Z.
- V. karimipour. *A multi-species asymmetric exclusion process;steady state and correlation functions on a periodic lattice*. http://arxiv.org/abs/cond-mat/9809193v2; first submitted 1998-09-14T12:05:11Z, last update 1998-10-15T11:14:37Z.

Martin: James B. Martin, *Stationary distributions of the multi-type ASEP*, Electronic Journal of Probability **25** (2020), paper 36, 1–41, DOI 10.1214/20-EJP421, arXiv:1810.10650v3. Downloaded and read the relevant sections in martin.pdf/martin_clean.txt. Theorem 3.1 (arXiv PDF p.19) is the infinite-line stationary queue construction; Theorem 3.3 (p.22) is its canonical-ring counterpart. These are reductions, not a covariance asymptotic theorem.

Ferrari–Gernholt: arXiv:2504.00765v3, 20 July 2026 (first submitted 1 April 2025). Downloaded decoupling.pdf and inspected main results plus Sections 3 and 5.3. Its abstract and introduction explicitly study large-time mixed space-time correlations on Z. Theorem 1.3 and Corollary 1.9 give time-scaled distributional decay of off-diagonal normal-mode two-point functions. They do not state the equal-time, canonical finite-ring asymptotic asked here. The queue drift/return-time estimates in Section 5.3.2 are relevant leads, and overlap the qualitative infinite-line exponential-mixing methods. They are NOT a solution in print to this question.

Stationary-horizon/speed-process papers: relevant to convergence of cumulative height fields in closing-density-gap regimes. Height-field convergence alone does not give pointwise occupation covariance asymptotics or canonical ring corrections; those require additional estimates. No theorem from these records is asserted to solve P0286.

Karimipour, cond-mat/9809193: the abstract advertises exact periodic correlations for a generalized overtaking model. Treat as a lead only: its model identification with the common-rate priority ASEP has not been verified here. Other arXiv recent hits include type-D ASEP, modified colloidal exclusion, open ASEP, and q-TAZRP: different models or time/geometry regimes.

## Read-only research brain and earlier work

Ran brain.py recall on “two species ASEP covariance mistakes” and on “Stationary two color ASEP covariance decay on a large ring”. The returned memories were mostly off-topic; none was used as mathematical authority. The recall helper reported an attempted detached index refresh which failed; no remember/write command was issued.

Ran math_recall.py on “Ferrari Martin queue two species stationary correlations”, and walked card claim_cbc6339431b41ebf26b756f6ded4a38087e5458884d5c62f68aff575b286e430. That prior attempt proves conservation/uniform-baseline identities but explicitly leaves asymmetric decay unresolved. Those identities were re-proved here.

Searched P0286 in the intake area and codex_pool_2026_10_10 with rg. A literal wildcard path failed on Windows; a follow-up Python glob search of probability_1000_intake_* JSONL files returned no matching records. The broader rg found the October 10 open-problems list entry, reproducing the supplied statement. A read-only git ls-tree of origin/master and a targeted Python path filter found no P0286-named answer path. No checkout file or repository state was changed. Raw path/ledger outputs are in previous_paths.txt and previous_ledger.txt.

## Search limitation

## Further attempt searches, 12 October 2026

- Read ATTEMPT.md in full and its explicit remaining gaps.
- math_recall.py query: "ASEP queue spectral gap Al Salam Chihara q Charlier birth death correlations". Returned a constant-rate M/M/1 busy-period card and general spectral-gap material; no matching ASEP/q-polynomial spectral theorem was returned. None was used as authority.
- math_recall.py query: "Darboux transformation Jacobi big q Hermite orthogonal polynomials discrete spectrum". Returned generic Hermite/orthogonal polynomial and Jacobi triple-product cards. No matching Darboux spectral classification was returned. One off-target card warns against assuming orthogonality from a formal polynomial basis; the new proof avoids that shortcut.
- brain.py recall: "ASEP stationary queue spectral gap mistakes". No on-target memory stood out. The helper itself reported starting its detached index refresh; no remember command or manual brain/store modification was issued, and this helper is not invoked again in this attempt.
- Python urllib request of https://dlmf.nist.gov/18.28 (NIST DLMF, q-orthogonal polynomials), seeking a checked neighbouring-area theorem for the continuous big q-Hermite spectral measure. Status and any used formula will be appended after inspection. This is a lead, not a solution in print to the ring question.

- The DLMF request returned HTTP 403. No DLMF formula was treated as fetched or checked.
- arXiv API query `ti:"Askey-scheme"`, max_results=5, https://export.arxiv.org/api/query?search_query=ti%3A%22Askey-scheme%22&max_results=5, returned five related modern records (askey_api.txt), not the older reference used below. This is a recorded search, not an identification of a solution to P0286.
- Fetched the separately known reference URL https://arxiv.org/pdf/math/9602214 into askey.pdf: Roelof Koekoek and Rene F. Swarttouw, *The Askey-scheme of hypergeometric orthogonal polynomials and its q-analogue*, February 20, 1996. The PDF has 127 pages; Section 3.18 is on PDF pp.82–83, printed pp.80–81. Inspected its strict real-parameter orthogonality (3.18.2), recurrence (3.18.4), and generating function (3.18.7); the a>1 relation (3.18.3) is present but not needed as an external input. The old PDF's extracted custom-font digits appear as control characters; the relevant raw extraction is saved in askey_big_q_hermite_raw.txt, and the normalized formulas and exact hypotheses are restated in SECOND_ATTEMPT.md Section 4.
- The only substantive new external mathematical input is (3.18.2), with |a|<1, together with the recurrence identifying the family. Extension to the threshold is proved here by bounded-operator convergence and density domination; the generating function is also independently proved from its recurrence. The reference is an orthogonal-polynomial identity, not a theorem solving stationary canonical ring ASEP covariance. The new covariance and limiting formulas are reductions argued here and therefore do not warrant SOLVED_IN_LITERATURE.

A final `check_prior.py` query filtered origin/master paths case-insensitively for p0286; it also returned no paths. The intake directory glob did resolve seven probability_1000_intake_* directories. The ledger search result remains zero matching JSONL records in those directories; the broader October 10 list entry and recalled prior attempt remain the available earlier record.

Only Martin and Ferrari–Gernholt full papers and the workshop PDF were downloaded/read. Other listed papers were screened from API metadata/abstracts. No theorem with the required identical ring objects, hypotheses and quantifiers was found and checked, so no word-for-word solution theorem or line-by-line solution mapping is claimed.
