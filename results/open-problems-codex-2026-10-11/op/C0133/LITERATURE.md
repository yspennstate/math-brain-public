# Literature audit for C0133

Audit date: 2026-10-12. Web access used only Python urllib; no built-in web search.

## Exact source
Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2, 8 October 2012, Problem 4.7, printed/PDF p. 19. Downloaded source.pdf; extracted source.txt (37 pages).

> Problem 4.7. (d ≥ 1) Assume (IID), (EL), ℓ ∈ R^d \ {0}. Does X_n · ℓ/n converge P_0-a.s. on {|X_n| → ∞}^c to 0 as n → ∞? This would generalize [Zer02, Th. 1].

Page 2 defines nearest-neighbor steps, cookie index equal to the number of visits including the current visit, and the annealed law P_0. (IID) means whole cookie stacks are independent and identically distributed across sites, not independence within stacks. Page 3: (EL) means every individual transition probability is strictly positive almost surely. Infinite stacks are allowed; no uniform lower bound, finite-stack hypothesis, or common drift sign occurs in Problem 4.7.

Theorem 4.6 is restricted to A_ℓ = {X_n·ℓ → +∞}; it does not control returning excursions. Theorem 4.8 assumes P_0[A_{ℓ_i} ∪ A_{−ℓ_i}] = 1 for a basis. This implies spatial transience and makes the event in Problem 4.7 null. It therefore cannot answer the question on an event of positive probability.

## Searches (exact URLs and outcomes)

### search_log.json (2026-10-12)
- arxiv_velocity: `https://export.arxiv.org/api/query?search_query=all%3A%22excited%20random%20walk%22%20AND%20%28all%3Avelocity%20OR%20all%3A%22law%20of%20large%20numbers%22%29&max_results=40`
- openalex_source: `https://api.openalex.org/works?search=Excited%20random%20walks%20results%20methods%20open%20problems&per-page=5`
- openalex_velocity: `https://api.openalex.org/works?search=excited%20random%20walks%20zero%20velocity%20non%20transient&per-page=30`
- crossref: `https://api.crossref.org/works?query=excited%20random%20walks%20law%20large%20numbers%20zero%20velocity&rows=30`
- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=excited%20random%20walks%20velocity&limit=30&fields=title,authors,year,externalIds,abstract,url`
- github: `https://api.github.com/search/repositories?q=excited%20random%20walks&per_page=30`

Outcomes: `[["arxiv_velocity", 200, 11822], ["openalex_source", 200, 81804], ["openalex_velocity", 200, 569144], ["crossref", 200, 152062], ["semantic", "HTTP Error 429: "], ["github", "HTTP Error 403: rate limit exceeded"]]`

### search_log_2.json (2026-10-12)
- openalex_citing_published: `https://api.openalex.org/works?filter=cites:W2962897620&per-page=200`
- openalex_citing_arxiv: `https://api.openalex.org/works?filter=cites:W2276429711&per-page=200`
- arxiv_zeroone: `https://export.arxiv.org/api/query?search_query=all%3A%22excited%20random%20walks%22%20AND%20%28all%3A%22zero-one%22%20OR%20all%3A%22non-transient%22%20OR%20all%3A%22non-ballistic%22%29&max_results=50`
- crossref_excited: `https://api.crossref.org/works?query.title=excited%20random%20walk&rows=50`
- paper_exchangeable: `https://arxiv.org/pdf/1311.6158`
- openalex_lln: `https://api.openalex.org/works?search=excited%20random%20walk%20law%20large%20numbers&per-page=40`

Outcomes: `[["openalex_citing_published", 200, 722019], ["openalex_citing_arxiv", 200, 326566], ["arxiv_zeroone", 200, 5171], ["crossref_excited", 200, 226028], ["paper_exchangeable", 200, 301664], ["openalex_lln", 200, 644607]]`

### search_log_3.json (2026-10-12)
- paper_counterexample: `https://arxiv.org/pdf/1909.03159`
- paper_mob: `https://arxiv.org/pdf/1307.6052`
- paper_zeroone: `https://projecteuclid.org/journals/annales-de-linstitut-henri-poincare-probabilites-et-statistiques/volume-52/issue-1/Zeroone-law-for-directional-transience-of-one-dimensional-excited-random/10.1214/14-AIHP615.pdf`

Outcomes: `[["paper_counterexample", 200, 309812], ["paper_mob", 200, 402504], ["paper_zeroone", 200, 1157]]`

### search_log_4.json (2026-10-12)
- paper_zeroone_arxiv: `https://arxiv.org/pdf/1304.7287`

Outcomes: `[["paper_zeroone_arxiv", 200, 231984]]`


Rate-limited services are coverage gaps, not negative search results. The first Project Euclid zero-one PDF request returned a 1157-byte HTML response despite HTTP 200; this was not treated as a paper. The arXiv copy was requested separately.

## Read-only prior work
- Intake ledger: probability_1000_intake_claude_20260907/{problems,attempts}.jsonl, C0133 and C0133-A001. Its claimed exponential returning-excursion estimate is not established.
- Git origin/master: probability_campaigns/codex_pool_2026-10-10/team_O/w338/PROOFS.md, C0133 section. Correctly distinguishes an unrestricted spatial tail 1/(2L) from a time-constrained tail. Rechecked independently below; no repository was changed.
- math_recall.py: “excited random walks zero velocity recurrence”; brain.py recall: “excited random walks mistakes” and “C0133 zero velocity non-transient”. No useful problem-specific memory beyond the existing attempt; unrelated memories were not used.

## Status of this audit
No theorem giving the full question under the exact hypotheses has been verified. This is a bounded audit, not a certificate that the problem remains open globally. Later special-case papers are leads; they are not SOLVED_IN_LITERATURE for C0133.


## Verified d=1 special-case theorem (not a full solution of C0133)
Gideon Amir, Noam Berger and Tal Orenshtein, *Zero–one law for directional transience of one dimensional excited random walks*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques **52**(1) (2016), 47–57, DOI: 10.1214/14-AIHP615; arXiv:1304.7287v2. The arXiv PDF is paper_zeroone.pdf, text paper_zeroone.txt.

Theorem 1.3, arXiv PDF p. 3, verbatim (mathematical layout linearized):
> Theorem 1.3. Let µ be a stationary ergodic (with respect to the Z-shift θ) and elliptic probability measure on the space Ω of cookie environments. Then P_0(lim_{n→∞} X_n/n = v) = 1 for some deterministic v ∈ [−1, 1].

Application, line by line:
1. IID whole stacks on Z give a stationary ergodic law for the Z-shift.
2. The source's (EL) in d=1 is exactly µ((0,1)^{Z×N})=1 (use countability to combine the individual almost-sure conditions).
3. Hence Theorem 1.3 gives X_n/n→v almost surely, with no bounded-stack or uniform-ellipticity requirement.
4. On {|X_n|→∞}^c there is a finite R and a sequence n_k→∞ with |X_{n_k}|≤R. Therefore v=lim X_{n_k}/n_k=0 on this event.
5. A direction ℓ∈R\{0} is a scalar; multiplying by it yields X_n·ℓ/n→0 on that event.

This covers d=1 under exactly the relevant hypotheses. It does not cover d≥2, so the overall verdict remains PARTIAL and not SOLVED_IN_LITERATURE. The LLN implication in line 4 is an explicit argument here, not a claim that the article states the whole Problem 4.7.

## Other inspected leads
- Gideon Amir and Tal Orenshtein, *Excited Mob*, Stochastic Processes and their Applications (2016), DOI 10.1016/j.spa.2015.09.007; arXiv:1307.6052v2. Downloaded/read introductory results and Section 4. Theorem 4.3, PDF p. 15, states a one-dimensional LLN under (SE). We use the elliptic theorem of Amir–Berger–Orenshtein instead, whose hypotheses match directly and avoid relying on typographical issues in the earlier preprint.
- Cong-Dan Pham, *Monotonicity and regularity of the speed for excited random walks in higher dimensions*, Electronic Journal of Probability **20** (2015), DOI 10.1214/EJP.v20-3522; arXiv:1311.6158v3. Downloaded/read model description and Theorem 1.1, PDF pp. 1–4. Only excitation in coordinate e_1, with all transverse transition probabilities fixed at 1/(2d), and LLN for d≥6. This is a restricted model and does not cover arbitrary cookies in Problem 4.7. The transverse component is itself a lazy simple walk and in these dimensions is transient, so the relevant returning event is null.
- Rafael Santos, *An excited random walk counter-example*, São Paulo Journal of Mathematical Sciences **16** (2022), 1194–1201 (online 22 February 2021), DOI 10.1007/s40863-021-00214-7; arXiv:1909.03159v1 (preprint title *An important excited random walk counter-example*). Downloaded and read. Constructs a stationary/ergodic environment with zero speed and infinite mean cookie count. It is not a nonzero-speed returning counterexample, and its correlated renewal environment is not IID across sites. The publication title and volume/year were checked against Crossref: container-title São Paulo Journal of Mathematical Sciences, volume 16, printed December 2022.

OpenAlex openalex_citing_published.json: indexed total 44; returned 44 (all fit in one page).

OpenAlex openalex_citing_arxiv.json: indexed total 18; returned 18 (all fit in one page).

### Citation leads reviewed at metadata/abstract level only
- Elena Kosygina, Martin Zerner, *Excursions of excited random walks on integers*, 2014, Electronic Journal of Probability, {"volume": "19", "issue": "none", "first_page": "1", "last_page": "25"}, https://doi.org/10.1214/ejp.v19-2940. Model-specific result; no exact-hypothesis solution verified.
- Elena Kosygina, Jonathon Peterson, *Excited random walks with Markovian cookie stacks*, 2017, Annales de l Institut Henri Poincaré Probabilités et Statistiques, {"volume": "53", "issue": "3", "first_page": "1458", "last_page": "1497"}, https://doi.org/10.1214/16-aihp761. Model-specific result; no exact-hypothesis solution verified.
- Elena Kosygina, Thomas Mountford, Jonathon Peterson, *Convergence of random walks with Markovian cookie stacks to Brownian motion perturbed at extrema*, 2021, Probability Theory and Related Fields, {"volume": "182", "issue": "1-2", "first_page": "189", "last_page": "275"}, https://doi.org/10.1007/s00440-021-01055-3. Model-specific result; no exact-hypothesis solution verified.
- Elena Kosygina, Jonathon Peterson, *Functional limit laws for recurrent excited random walks with periodic cookie stacks*, 2016, Electronic Journal of Probability, {"volume": "21", "issue": "none", "first_page": "1", "last_page": "24"}, https://doi.org/10.1214/16-ejp14. Model-specific result; no exact-hypothesis solution verified.
- Nicholas F. Travers, *Excited random walk in a Markovian environment*, 2018, Electronic Journal of Probability, {"volume": "23", "issue": "none", "first_page": "1", "last_page": "60"}, https://doi.org/10.1214/18-ejp155. Model-specific result; no exact-hypothesis solution verified.
- Swee Hong Chan, Lila Greco, Lionel Levine, Peter Chi-Win Li, *Random Walks with Local Memory*, 2021, Journal of Statistical Physics, {"volume": "184", "issue": "1", "first_page": null, "last_page": null}, https://doi.org/10.1007/s10955-021-02791-5. Model-specific result; no exact-hypothesis solution verified.
- Swee Hong Chan, *Recurrence of horizontal–vertical walks*, 2023, Annales de l Institut Henri Poincaré Probabilités et Statistiques, {"volume": "59", "issue": "2", "first_page": "578", "last_page": "605"}, https://doi.org/10.1214/22-aihp1277. Model-specific result; no exact-hypothesis solution verified.
- Elena Kosygina, Martin Zerner, *Excursions of excited random walks on integers*, 2013, arXiv (Cornell University), {"volume": null, "issue": null, "first_page": null, "last_page": null}, https://doi.org/10.48550/arxiv.1307.6830. Model-specific result; no exact-hypothesis solution verified.
- Dmitry Dolgopyat, Elena Kosygina, *Excursions and occupation times of critical excited random walks*, 2014, arXiv (Cornell University), {"volume": null, "issue": null, "first_page": null, "last_page": null}, https://doi.org/10.48550/arxiv.1410.7090. Model-specific result; no exact-hypothesis solution verified.
- Sebastian Mueller, Tal Orenshtein, *Infinite excursions of rotor walks on regular trees*, 2015, arXiv (Cornell University), {"volume": null, "issue": null, "first_page": null, "last_page": null}, https://doi.org/10.48550/arxiv.1511.05896. Model-specific result; no exact-hypothesis solution verified.
- Daniel Camarena, Gonzalo Panizo, Alejandro F. Ramı́rez, *An Overview of the Balanced Excited Random Walk*, 2020, Progress in probability, {"volume": null, "issue": null, "first_page": "207", "last_page": "217"}, https://doi.org/10.1007/978-3-030-60754-8_10. Model-specific result; no exact-hypothesis solution verified.
- Gady Kozma, Tal Orenshtein, Igor Shinkar, *Excited random walk with periodic cookies*, 2016, Annales de l Institut Henri Poincaré Probabilités et Statistiques, {"volume": "52", "issue": "3", "first_page": "1023", "last_page": "1049"}, https://doi.org/10.1214/15-aihp669. Model-specific result; no exact-hypothesis solution verified.
- Ross G. Pinsky, *Transience, recurrence and speed of diffusions with a non-Markovian two-phase “use it or lose it” drift*, 2014, Annales de l Institut Henri Poincaré Probabilités et Statistiques, {"volume": "50", "issue": "4", "first_page": "1198", "last_page": "1212"}, https://doi.org/10.1214/13-aihp549. Model-specific result; no exact-hypothesis solution verified.
- Sebastian Müller, Tal Orenshtein, *Infinite Excursions of Rotor Walks on Regular Trees*, 2017, The Electronic Journal of Combinatorics, {"volume": "24", "issue": "2", "first_page": null, "last_page": null}, https://doi.org/10.37236/5781. Model-specific result; no exact-hypothesis solution verified.

Additional request search_log_4.json: `{"date": "2026-10-12", "queries": {"paper_zeroone_arxiv": "https://arxiv.org/pdf/1304.7287"}, "results": [["paper_zeroone_arxiv", 200, 231984]]}`

Additional request search_log_5.json: `{"date": "2026-10-12", "queries": {"zeroone_published": "https://projecteuclid.org/download/pdfview_1/euclid.aihp/1452089259"}, "results": [[200, 1165, "valid PDF"]]}`

Additional read-only math-store recall during the proof attempt: “martingale bounded increments Azuma strong law”. Its scalar Azuma card was checked by the direct moment-generating-function proof in ATTEMPT.md; no brain/store writes occurred.

The later Project Euclid published-PDF request returned a one-page PDF containing only “Request unsuccessful. Incapsula incident ID”. Although the container parses as a PDF, it is a bot-challenge response, not the article. All theorem quotations in this audit use the verified arXiv copy.

Original RWRE comparison: M. P. W. Zerner, *A non-ballistic law of large numbers for random walks in i.i.d. random environment*, Electronic Communications in Probability **7**(19) (2002), 191–197, DOI 10.1214/ecp.v7-1060. Exact reference checked in the survey bibliography (source.txt, final PDF page). The environment does not depend on visit index in RWRE; this is a model-specific precedent, not a theorem for arbitrary cookie stacks.


## Second serious attempt: searches and retrievals, 2026-10-12
Each following record gives the service through its URL, the exact query or retrieval URL, the date, and the response. All requests used Python from the shell. HTTP success alone was not accepted as evidence of article retrieval.

### second_search_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_openalex": "https://api.openalex.org/works?search=A%20non-ballistic%20law%20of%20large%20numbers%20for%20random%20walks%20in%20iid%20random%20environment&per-page=3",
    "zerner_arxiv": "https://export.arxiv.org/api/query?search_query=all%3A%22non-ballistic%22%20AND%20au%3AZerner&max_results=10",
    "hewitt_crossref": "https://api.crossref.org/works?query.title=Symmetric%20measures%20on%20Cartesian%20products&rows=3"
  },
  "results": [
    [
      "zerner_openalex",
      "HTTP Error 429: Too Many Requests"
    ],
    [
      "zerner_arxiv",
      "HTTP Error 429: Unknown Error"
    ],
    [
      "hewitt_crossref",
      200,
      11951
    ]
  ]
}
```

### second_fetch_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_pdf": "https://projecteuclid.org/download/pdf_1/euclid.ecp/1463434786"
  },
  "results": [
    200,
    1163
  ]
}
```

### second_mirror_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_emis_html": "https://www.emis.de/journals/EJP-ECP/article/view/1060.html",
    "zerner_emis_pdf": "https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1060/1060-1-PB.pdf",
    "zerner_euclid_modern": "https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/ecp.v7-1060.pdf"
  },
  "results": [
    [
      "zerner_emis_html",
      "HTTP Error 403: Forbidden"
    ],
    [
      "zerner_emis_pdf",
      "HTTP Error 404: Not Found"
    ],
    [
      "zerner_euclid_modern",
      200,
      1055
    ]
  ]
}
```

### second_author_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_author": "https://www.math.uni-tuebingen.de/user/zerner/",
    "zerner_jina": "https://r.jina.ai/https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/ecp.v7-1060.full"
  },
  "results": [
    [
      "zerner_author",
      200,
      3434
    ],
    [
      "zerner_jina",
      200,
      7877
    ]
  ]
}
```

### second_archive_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_archive": "https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/ECP/Vol.7/paper19.pdf",
    "zerner_emis_archive": "https://www.emis.de/journals/EJP-ECP/ECP/Vol.7/paper19.pdf",
    "zerner_author_publications": "https://www.math.uni-tuebingen.de/user/zerner/publications.html"
  },
  "results": [
    [
      "zerner_archive",
      "HTTP Error 404: Not Found"
    ],
    [
      "zerner_emis_archive",
      "HTTP Error 403: Forbidden"
    ],
    [
      "zerner_author_publications",
      200,
      11198
    ]
  ]
}
```

### second_primary_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_legacy_reader": "https://r.jina.ai/https://projecteuclid.org/euclid.ecp/1463434786",
    "zerner_doi": "https://doi.org/10.1214/ecp.v7-1060",
    "hewitt_pdf": "https://www.ams.org/tran/1955-080-02/S0002-9947-1955-0076206-8/S0002-9947-1955-0076206-8.pdf"
  },
  "results": [
    [
      "zerner_legacy_reader",
      200,
      17604,
      "https://r.jina.ai/https://projecteuclid.org/euclid.ecp/1463434786"
    ],
    [
      "zerner_doi",
      200,
      1167,
      "https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/10.1214/ECP.v7-1060.full"
    ],
    [
      "hewitt_pdf",
      "HTTP Error 403: Forbidden"
    ]
  ]
}
```

### second_download_log.json

```json
{
  "date": "2026-10-12",
  "queries": {
    "zerner_download": "https://projecteuclid.org/journalArticle/Download?urlid=10.1214%2FECP.v7-1060",
    "zerner_download_reader": "https://r.jina.ai/https://projecteuclid.org/journalArticle/Download?urlid=10.1214%2FECP.v7-1060",
    "zerner_correct_pdf": "https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/10.1214/ECP.v7-1060.pdf"
  },
  "results": [
    [
      "zerner_download",
      200,
      1164
    ],
    [
      "zerner_download_reader",
      200,
      15362
    ],
    [
      "zerner_correct_pdf",
      200,
      1159
    ]
  ]
}
```

### Retrieval assessment and exact references

Martin P. W. Zerner, *A non-ballistic law of large numbers for random walks in i.i.d. random environment*, Electronic Communications in Probability **7** (2002), paper 19, 191–197, DOI: 10.1214/ECP.v7-1060. The author publication list and Project Euclid article landing page agree with the survey bibliography. Direct PDF requests returned approximately 1.2 KB bot-challenge PDFs, not the article. Archive/mirror failures and incorrect modern URL attempts are retained above. The public text reader of the correct Project Euclid journalArticle/Download URL returned the complete seven-page text, with original printed page boundaries, saved as zerner_download_reader.txt. This is the source actually used for theorem verification.

Theorem 1, printed p.192, verbatim with mathematical layout linearized:
> Theorem 1. Assume (1) and let e ∈ Z^d with |e| = 1 and P_0[A_e ∪ A_{−e}] = 0. Then lim_{n→∞} X_n e/n = 0 P_0-a.s.

Here condition (1), printed pp.191–192, is:
> (ω(z, z + e))_{|e|=1}, z ∈ Z^d, are i.i.d. under P with ω(z, z + e) > 0 P-a.s. for all z ∈ Z^d, |e| = 1.

It is a theorem for Markovian RWRE, not a literature solution for general excited walks. It verifies the exchangeable-arrow special-case application in SECOND_ATTEMPT.md, Section 8. No uniform ellipticity is required.

Lemma 3, printed p.193, verbatim with mathematical layout linearized:
> Lemma 3. Let (X_n)_n ∈ (Z^d)^N be a fixed nearest neighbor path with X_0 = 0 and lim sup_{n→∞} X_n e/n > 0. Then sup_{c≥0} inf_{L≥1} lim sup_{M→∞} F_{M,L}(c) > 0.

Its definition of F uses the diameter of the plane-visit TIME set, not just its cardinality. This lemma is deterministic and therefore applies to cookie walks. A self-contained proof with simpler constants is also recorded in DETERMINISTIC_PLANE_LEMMA.md. Using it to solve the general problem requires the new probabilistic argument here; it is not a solution already in print.

Edwin Hewitt and Leonard J. Savage, *Symmetric measures on Cartesian products*, Transactions of the American Mathematical Society **80** (1955), 470–501, DOI: 10.1090/S0002-9947-1955-0076206-8. Crossref metadata retrieved successfully in hewitt_crossref.json; the AMS full PDF request failed with HTTP 403. The finite-alphabet representation needed for the attempt is proved directly in SECOND_ATTEMPT.md, Section 5, rather than relying on an unread theorem number.

### Exact source inputs for the fresh-hyperplane proof

Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2 (2012), https://arxiv.org/pdf/1204.1895. The already retrieved source.pdf is the complete 37-page source; source.txt preserves page boundaries.

Problem 4.7, p.19, verbatim with mathematical layout linearized:
> Problem 4.7. (d ≥ 1) Assume (IID), (EL), ℓ ∈ R^d\{0}. Does X_n · ℓ/n converge P_0-a.s. on {|X_n| → ∞}^c to 0 as n → ∞? This would generalize [Zer02, Th. 1].

Theorem 2.5, p.7:
> Theorem 2.5. (d ≥ 1, range) Assume (IID) and (EL). If there is an orthogonal set F ⊂ E such that b_F = 0 then the range is P_0-a.s. infinite. If there is no such set then the range is P_0-a.s. finite.

Only its finite/infinite range dichotomy is used.

Theorem 3.16, p.14:
> Theorem 3.16. (d ≥ 1, Kalikow-type zero-one law) Assume (IID), (EL) and let ℓ ∈ R^d\{0}. Then P_0[|X_n · ℓ| → ∞] = P_0[A_ℓ ∪ A_{−ℓ}] ∈ {0, 1}.

Lemma 3.18, p.14, proof pp.14–16:
> Lemma 3.18. (d ≥ 1) Assume (IID), E[ω(0, e, 1)] > 0 for all e ∈ E and let ℓ ∈ R^d\{0} and u, w ∈ R with u < w. Furthermore assume that the range of the ERW is P_0-a.s. infinite. Then P_0[{X_n · ℓ ≥ u i.o.} ∩ {∀n ≥ 0 : X_n · ℓ ≤ w}] = 0.

These quotations are theorem inputs, not quotations of a paper answering Problem 4.7. The fresh-hyperplane proof is an original implication proved in this folder. It has now passed the recorded hostile review; its verdict is SOLVED rather than SOLVED_IN_LITERATURE. No exact-hypothesis solution already in print was verified in this bounded literature audit.

### Read-only brain questions in this second attempt

- math_recall.py "excited random walk recurrent sublinear range bounded cookie stacks drift budget": returned the old unproved excursion estimate and related recurrence cards; no closure was accepted.
- math_recall.py "Zerner non-ballistic law large numbers iid random environment": returned neighbouring LLN references, not the exact 2002 theorem; the original paper was retrieved separately.
- math_recall.py "de Finetti exchangeable sequences directing measure": card claim_20e7e94fd93a2e51ba5becdbc47068b21245cc7d9d4def4e9e32ec611d9265ad distinguished infinite representation from finite exchangeability. The needed representation was independently proved.
- math_recall.py "excited random walks Lemma 3.18 infinite range slab finite modification": returned source and open-problem/attempt cards, including the warning that depleted environments need not be IID. No independent finite-modification theorem was supplied. The positive-replay argument was checked directly instead.

The initial topic and topic-mistakes brain.py recalls remain recorded above. No brain, store, ledger or repository was modified.
