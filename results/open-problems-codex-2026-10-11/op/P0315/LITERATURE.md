# P0315 — literature audit, 2026-10-11

Second-attempt supplement (same date): re-read the downloaded Qu–Valko
PDF, (20), Lemma 10 (PDF pp. 10–11), (29)–(30) (PDF p. 12), and
Theorem 1. These confirm the normalized Holder-beta circle observable
and drift/noise normalization used in SECOND_ATTEMPT.md. No new external
literature search or novelty claim was made for the coupling-derived bound.
The source's Problem 2 (PDF p. 29) concerns uniqueness of the infinite
moment ODE system with possible additional constraints; the second
attempt proves uniqueness only in the positive-definite, normalized
probability-valued class and only for 0<beta<1.

Read-only brain queries during the second attempt:
'Qu Valko infinite Fourier moment hierarchy asymptotic uniqueness weighted
remainder'; and 'synchronous coupling fractional distance contraction
diffusion circle stochastic sine'. Neither produced a theorem applicable
to this diffusion or the needed large-parameter smoothing estimate.
The latter returned reflected-Brownian-motion coupling in planar domains;
that geometry is different, so its claim was not used in our proof.

No paper has yet been verified to solve the question with all beta values,
all harmonics, and pointwise remainder estimates. VERDICT is not
SOLVED_IN_LITERATURE. Failed API requests are coverage gaps, not negative results.

## Primary sources actually downloaded and read

1. Laure Dumaz and Martin Malvy, *Long-Range Correlation of the Sine_beta
point Process*, arXiv:2603.15289v1, submitted 16 March 2026 (PDF dated
17 March 2026), 30 pages. https://arxiv.org/abs/2603.15289
Saved as source.pdf and source.txt. PDF pp. 3–4, Theorem 1.1 and (1.3).
Theorem 1.1 is a bound on the signed locally averaged pair correlation:
|integral_0^lambda T_beta(r+x) dx| <= C r^(-c beta/(1+beta^2)).
The constants are absolute c>0 and C=C(beta,lambda_0)>0, for fixed
beta,lambda_0>0, 0<lambda<=lambda_0 and r>=1.
This does not establish the pointwise expansion.

2. Yahui Qu and Benedek Valko, *On the pair correlation function of the
Sine_beta process*, arXiv:2509.15446v1, submitted 18 September 2025,
32 pages. https://arxiv.org/abs/2509.15446
Saved as qu_valko.pdf and qu_valko.txt. Theorem 1 (PDF pp. 2–3)
is an exact Fourier/SDE representation, Proposition 8 (PDF p. 10)
is a reduced-Palm/Hua–Pickrell identity, Theorem 3 (PDF p. 3) proves
|rho_beta^(2)(0,lambda)-(4 pi^2)^(-1)|
 <= c_beta (lambda^(-1)+lambda^(-beta/2)+lambda^(-4/beta)), lambda>=2.
It matches the predicted upper-bound order for beta>=4; it does NOT
identify a leading oscillatory coefficient or prove exact first-order
asymptotics. Dumaz–Malvy PDF p. 4 describes this as “exact first order
asymptotics”; the actual quoted Theorem 3 is weaker. Equations (14) and
(16), PDF pp. 5–6, give the classical beta=4 formula and discuss the
conjectured harmonic family. Forrester's even-beta formula is discussed
with an explicit caveat about exchange of limits, not silently upgraded.

3. Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*,
Journal of Mathematical Physics **63**, 061101 (2022), arXiv:2202.09240.
https://arxiv.org/abs/2202.09240
Saved as lewin.pdf and lewin.txt (96 PDF pages). PDF p. 64,
(148) gives the classical beta=1,2,4 cases; (149)–(150) give the
conjectured family at unit density. The paragraph below (150) explicitly
says it does not seem that (149) has been shown in all cases.

4. Theo Assiotis and Joseph Najnudel, *Moments of the C_beta E field
partition function, Sine_beta correlations and stochastic zeta*,
arXiv:2602.08739 (2026), 35 PDF pages.
https://arxiv.org/abs/2602.08739
Saved as assiotis_najnudel.pdf and assiotis_najnudel.txt. Lead: exact
correlation identities; extracting large-distance asymptotics remains
a separate problem. Not a verified solution to P0315.

5. Peter J. Forrester, *Log-Gases and Random Matrices*, Princeton
University Press (2010). Dumaz–Malvy cite Proposition 13.2.4 and
formula 13.226; Qu–Valko cite Proposition 13.13. Book not downloaded.
F. D. M. Haldane, *Effective harmonic-fluid approach to low-energy
properties of one-dimensional quantum fluids*, Physical Review Letters
**47** (1981), 1840–1843. Physical prediction, not a general-beta proof.

## Search and recall audit

6. Shengqi Qiu, Yahui Qu, Lingfan Yuan, Benedek Valko, and Spencer
Venancio, *The pair correlation function of the Sine_6 process*,
arXiv:2607.26223v1, submitted 28 July 2026.
https://arxiv.org/abs/2607.26223
Saved as sine6.pdf and sine6.txt. Theorem 1 (PDF p. 2) gives an exact
one-variable Bessel-function representation. Proposition 2 (PDF p. 3)
gives at density (2 pi)^(-1):

    4 pi^2 rho_6^(2)(0,r) = 1-2/(3r^2)
       +Gamma(1/3)^2 [ (2/9)cos(r)r^(-2/3)
          -(16/81)sin(r)r^(-5/3)
          -(64/729)cos(r)r^(-8/3)
          +(8/81)cos(2r)r^(-8/3)] + O(r^(-11/3)).

This is a genuine post-source special-case lead and does not solve
general beta. Its proof section describes an outline using Forrester's
oscillatory-integral methods. Its introduction says Assiotis–Najnudel
identify the even-beta integral limit, addressing the earlier
Qu–Valko interchange-of-limits caveat. Equation (2) also provides the
classical beta=1 exact formula used in ATTEMPT section 5.

7. Theodoros Assiotis and Kohei Suzuki, *Sine beta is tail trivial*,
arXiv:2610.10849v1, submitted 7 October 2026.
https://arxiv.org/abs/2610.10849
Saved as search_tail.pdf and tail.txt. The abstract proves tail triviality
and applications to Gibbs extremality and diffusions. It uses correlation
bounds as inputs; it does not claim the full pointwise pair expansion.
This is a neighboring problem, not P0315 solved in print.

Machine-readable complete HTTP queries/outcomes: search_log.json;
raw responses: search_*.txt. All searches dated 2026-10-11 and fetched
using Python requests from the shell, without built-in web search.
The initial arXiv exact phrase query missed Unicode/subscript variants;
a follow-up broad query is necessary and recorded, so that initial small
result set is not taken as exhaustive.

The broad date-window arXiv query returned five entries: tail triviality,
the beta=6 paper, and three unrelated items. The Unicode/subscript/author
follow-up returned 47 entries and included Qu–Valko and the beta=6 paper;
its other first-page matches are mainly nuclear beta-decay literature.
The focused Crossref title query again returned mostly irrelevant matches.
The bounded search identified no theorem solving the full question.
OpenAlex/Semantic Scholar remain rate-limited, so the search is incomplete.

Direct source fetches, also on 2026-10-11: arxiv.org/pdf/2603.15289,
2509.15446, 2602.08739, 2202.09240, 2607.26223, and 2610.10849.
Source-version lookup used export.arxiv.org/api/query?id_list=2603.15289.
No claim of a full literature solution is made.

OpenAlex search, source-title lookup, retry, and citing-source request
returned HTTP 429. The citing request used the source DOI filter but
could not resolve a work ID because the source lookup was rate-limited.
Semantic Scholar search and direct source/citations lookup also returned
HTTP 429. These services cannot support an absence-of-solution claim.
GitHub repository search for '"sine beta" correlation' returned 0.
Crossref broad query returned mainly irrelevant entries; a focused title
query was subsequently run. arXiv source metadata reports v1 only.

Read-only brain: math_recall 'sine beta Forrester Haldane correlation';
brain recall 'sine beta pair correlation mistakes' and
'Forrester Haldane sine beta'. The earlier attempt proves only beta=2.
The brain's density warning was checked directly by a change of variables.
Ledger glob search first failed because rg does not expand Windows globs;
retry enumerated probability_1000_intake_* directories and found no P0315
line. codex_pool_2026_10_10 search also found no matching line.
Read-only origin/master tree search for P0315 and forrester-haldane found
no matching path. No shared repository or brain was changed.
During the attempt another read-only math-store recall used
'Hua Pickrell Qu Valko Fourier moment correlation'; it returned no useful
new card on this hierarchy, so no additional brain hint was used as a theorem.

## Exact HTTP query log

- {"date": "2026-10-11", "service": "arxiv", "url": "https://export.arxiv.org/api/query", "query": {"search_query": "all:\"sine beta\" AND (all:correlation OR all:Forrester)", "start": 0, "max_results": 50, "sortBy": "submittedDate", "sortOrder": "descending"}, "outcome": "HTTP 200; saved search_arxiv.txt"}
- {"date": "2026-10-11", "service": "openalex", "url": "https://api.openalex.org/works", "query": {"search": "sine beta correlation", "per-page": 50}, "outcome": "HTTP 429; saved search_openalex.txt"}
- {"date": "2026-10-11", "service": "crossref", "url": "https://api.crossref.org/works", "query": {"query": "sine beta correlation Forrester Haldane", "rows": 30}, "outcome": "HTTP 200; saved search_crossref.txt"}
- {"date": "2026-10-11", "service": "semantic", "url": "https://api.semanticscholar.org/graph/v1/paper/search", "query": {"query": "sine beta correlation", "limit": 50, "fields": "title,authors,year,externalIds,url,abstract"}, "outcome": "HTTP 429; saved search_semantic.txt"}
- {"date": "2026-10-11", "service": "github", "url": "https://api.github.com/search/repositories", "query": {"q": "\"sine beta\" correlation", "per_page": 30}, "outcome": "HTTP 200; saved search_github.txt"}
- {"date": "2026-10-11", "service": "openalex_source", "url": "https://api.openalex.org/works", "query": {"search": "Long-Range Correlation of Sine beta Point Process", "per-page": 10}, "outcome": "HTTP 429; saved search_openalex_source.txt"}
- {"date": "2026-10-11", "service": "arxiv_source", "url": "https://export.arxiv.org/api/query", "query": {"id_list": "2603.15289"}, "outcome": "HTTP 200; saved search_arxiv_source.txt"}
- {"date": "2026-10-11", "service": "openalex_retry", "url": "https://api.openalex.org/works?search=Long-Range%20Correlation%20Sine&per_page=10", "outcome": "HTTP 429"}
- {"date": "2026-10-11", "service": "openalex_citing", "url": "https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2603.15289&per_page=100", "outcome": "HTTP 429"}
- {"date": "2026-10-11", "service": "semantic_retry", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.15289?fields=title,year,citations.title,citations.year,citations.externalIds", "outcome": "HTTP 429"}
- {"date": "2026-10-11", "service": "arxiv_recent", "url": "https://export.arxiv.org/api/query?search_query=all:sine%20AND%20all:beta%20AND%20submittedDate:[202603160000%20TO%20202610112359]&max_results=100&sortBy=submittedDate&sortOrder=descending", "outcome": "HTTP 200"}
- {"date": "2026-10-11", "service": "arxiv_variants", "url": "https://export.arxiv.org/api/query", "query": {"search_query": "all:\"Sineβ\" OR all:\"Sine_beta\" OR (au:Qu AND au:Valko) OR (all:\"pair correlation\" AND all:beta)", "max_results": 100, "sortBy": "submittedDate", "sortOrder": "descending"}, "outcome": "HTTP 200"}
- {"date": "2026-10-11", "service": "crossref_title", "url": "https://api.crossref.org/works", "query": {"query.title": "On the pair correlation function of the Sine beta process", "rows": 15}, "outcome": "HTTP 200"}
- {"date": "2026-10-11", "service": "tail", "url": "https://arxiv.org/pdf/2610.10849", "query": {}, "outcome": "HTTP 200"}
