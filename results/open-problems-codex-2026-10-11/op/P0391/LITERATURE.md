# Literature and provenance — P0391, 11 October 2026

## Status of the literature check

No inspected paper states and proves the full arbitrary-gamma, finite-second-service-moment, empty-start diffusion theorem. This is NOT a certificate of current openness: OpenAlex returned HTTP 429 on all requests, so its citation graph could not be inspected. No SOLVED_IN_LITERATURE verdict is warranted.

## Exact primary reference

Bert Zwart (2022), “Conjectures on symmetric queues in heavy traffic,” Queueing Systems 100(3–4), 369–371. DOI 10.1007/s11134-022-09746-x. arXiv:2202.02366v1, posted 4 February 2022; manuscript dated 8 February 2022. Downloaded PDF and extracted text are source_pdf.pdf and source.txt. Problem 1 is on PDF p. 2, with hypotheses beginning on p. 1.

The source defines gamma(n,i) as both the service share at position i and the probability of insertion at i into a queue of new size n. Gamma is fixed, nonnegative, and sums to one. Poisson arrival rates vary; the service law is fixed, has mean m>0 and finite second moment. The parameter r(1-rho_r) tends to a real constant, not necessarily positive. The formal problem sentence does not specify initial state; PDF p. 2 explicitly limits the universal fixed-time marginal identity to Q_r(0)=0. The attempt follows the user’s empty-start caveat.

## Searches actually run

- Date 2026-10-11; service source_pdf; exact request: `https://arxiv.org/pdf/2202.02366`; result: saved.
- Date 2026-10-11; service arxiv; exact request: `http://export.arxiv.org/api/query?search_query=all:%22symmetric%20queues%22&start=0&max_results=30`; result: saved.
- Date 2026-10-11; service openalex_search; exact request: `https://api.openalex.org/works?search=Conjectures%20on%20Symmetric%20Queues%20in%20Heavy%20Traffic&per-page=10`; result: HTTP Error 429: Too Many Requests.
- Date 2026-10-11; service openalex_related; exact request: `https://api.openalex.org/works?search=symmetric%20queues%20heavy%20traffic&per-page=30`; result: HTTP Error 429: Too Many Requests.
- Date 2026-10-11; service crossref; exact request: `https://api.crossref.org/works?query=symmetric%20queues%20heavy%20traffic&rows=30`; result: saved.
- Date 2026-10-11; service semantic; exact request: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2202.02366?fields=title,authors,year,citations.title,citations.year,citations.externalIds`; result: HTTP Error 429: .
- Date 2026-10-11; service github; exact request: `https://api.github.com/search/repositories?q=%22symmetric+queues%22`; result: saved.
- Date 2026-10-11; service openalex_doi; exact request: `https://api.openalex.org/works/https://doi.org/10.1007/s11134-022-09746-x`; result: HTTP Error 429: Too Many Requests.
- Date 2026-10-11; service openalex_citing; exact request: `https://api.openalex.org/works?filter=cites:doi:10.1007/s11134-022-09746-x&per-page=100`; result: HTTP Error 429: Too Many Requests.
- Date 2026-10-11; service semantic_retry; exact request: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11134-022-09746-x/citations?fields=title,year,externalIds&limit=100`; result: saved.
- Date 2026-10-11; service arxiv_broad; exact request: `https://export.arxiv.org/api/query?search_query=all:%22symmetric%20queue%22%20OR%20(all:%22service%20disciplines%22%20AND%20all:%22heavy%20traffic%22)&max_results=50`; result: saved.
- Date 2026-10-11; service crossref_fralix; exact request: `https://api.crossref.org/works?query.title=Time-dependent%20properties%20of%20symmetric%20queues&rows=3`; result: saved.
- Date 2026-10-11; service citing_stable; exact request: `https://arxiv.org/pdf/2105.02349`; result: saved.
- Date 2026-10-11; service citing_fairness; exact request: `https://arxiv.org/pdf/1411.4841`; result: saved.
- Date 2026-10-11; service fralix_page; exact request: `https://doi.org/10.1007/s11134-010-9202-1`; result: saved.

The first arXiv phrase search returned two records: the source and Guillemin–Simonian (2013), “Stationary analysis of the Shortest Queue First service policy: the asymmetric case,” arXiv:1305.3496, a different two-queue model. GitHub returned total_count=0 for the quoted phrase. Crossref returned the source DOI and otherwise mostly unrelated heavy-traffic papers. The OpenAlex DOI-resolution requests failed before a canonical work ID could be obtained; the attempted DOI-based citing filter also returned 429. Therefore the requested OpenAlex works-citing search remains unavailable, rather than being represented as an empty citation set.

The successful Semantic Scholar citation endpoint for the source DOI returned two records: the stable-local-time paper and the proportional-fairness paper below. Their metadata years are 2021 and 2014 respectively, although later publication metadata exist. The retrieved arXiv versions and publication metadata are kept distinct.

## Relevant references and leads

1. Brian Fralix and Bert Zwart (2011), “Time-dependent properties of symmetric queues,” Queueing Systems 67(1), 33–45, DOI 10.1007/s11134-010-9202-1. Crossref has online date 24 November 2010. Source reference [2] and PDF p. 2 explicitly credit the empty-start fixed-time queue-length identity to this paper. It is a marginal-law input, not the requested process theorem. The publisher landing-page fetch was attempted separately.

2. Frank P. Kelly (1979), Reversibility and stochastic networks, Wiley, Chichester. Source reference [4]. Used for the standard full stationary residual-service product form; ATTEMPT.md gives its balance calculation. This is not a diffusion-limit theorem.

3. H. C. Gromoll (2004), “Diffusion approximation for a processor sharing queue in heavy traffic,” Annals of Applied Probability 14(2), 555–611, arXiv:math/0405298. Source [3]. PS special case with stronger service moments; not universal gamma.

4. A. L. Puha and R. J. Williams (2004), “Invariant states and rates of convergence for a critical fluid model of a processor sharing queue,” Annals of Applied Probability 14(2), 517–554. Source [10]. PS fluid model, not arbitrary gamma.

5. A. Lambert, F. Simatos, and B. Zwart (2013), “Scaling limits via excursion theory: interplay between Crump-Mode-Jagers branching processes and processor-sharing queues,” Annals of Applied Probability 23(6), 2357–2381. Source [7]. The source explicitly credits this paper with removing the fourth-moment assumption for PS with Poisson arrivals. Used only as the known PS finite-second-moment input.

6. V. Limic (2000), “On the behavior of LIFO preemptive resume queues in heavy traffic,” Electronic Communications in Probability 5, 13–27, DOI 10.1214/ecp.v5-1014; V. Limic (2001), “A LIFO queue in heavy traffic,” Annals of Applied Probability 11(2), 301–331. Source [8], [9]. LCFS special cases, not universal gamma.

7. W. Whitt (2002), Stochastic-process limits, Springer, New York. Source [12]. Standard workload FCLT and reflection-map input, not the conjectured queue-length theorem.

8. A. Lambert and F. Simatos (2014), “The weak convergence of regenerative processes using some excursion path decompositions,” Annales de l’Institut Henri Poincare, Probabilites et Statistiques 50(2), 492–511. Source [5]. A possible general framework, but excursion convergence hypotheses must still be established for arbitrary gamma.

9. Maria Vlasiou, Jiheng Zhang, and Bert Zwart, “Insensitivity of proportional fairness in critically loaded bandwidth sharing networks,” arXiv:1411.4841; retrieved manuscript dated 2 June 2021; later DOI 10.1007/s11134-026-09978-1 appears in Semantic Scholar. Retrieved PDF abstract concerns proportional fairness and a dense class of service laws in bandwidth-sharing networks. The allocation model and quantifier are not arbitrary rank-based symmetric gamma. A related lead, not an exact solution.

10. Wei Xu, “Stochastic Volterra equations for the local times of spectrally positive stable processes,” arXiv:2105.02349v4 (30 January 2024), DOI 10.1214/23-AAP2017. Retrieved PDF explicitly says its queueing consequence partially answers Zwart's Problem 2 for heavy-tailed PS. It concerns a different limit regime and a special discipline, not Problem 1 for arbitrary gamma.

## Broader arXiv query results

- H. Thorsdottir, I. M. Verloop; Markov-modulated M/G/1 type queue in heavy traffic and its application to time-sharing disciplines; http://arxiv.org/abs/1509.01944v2; posted 2015-09-07T08:28:44Z.
- Lisa Aoki Hillas, Rene Caldentey, Varun Gupta; Heavy Traffic Analysis of Multi-Class Bipartite Queueing Systems Under FCFS; http://arxiv.org/abs/2303.17588v1; posted 2023-03-30T17:57:02Z.
- J. G. Dai, Yiquan Ji, Masakiyo Miyazawa; Tight matrices and heavy traffic steady state convergence in queueing networks; http://arxiv.org/abs/2404.13651v3; posted 2024-04-21T13:00:47Z.
- H. Christian Gromoll; Diffusion approximation for a processor sharing queue in heavy traffic; http://arxiv.org/abs/math/0405298v1; posted 2004-05-14T16:30:14Z.
- Marko Boon, Rob van der Mei, Erik Winands; Queueing networks with a single shared server: light and heavy traffic; http://arxiv.org/abs/1408.0151v1; posted 2014-08-01T12:29:30Z.
- Wanyang Dai; Heavy traffic limit theorems for a queue with Poisson ON/OFF long-range dependent sources and general service time distribution; http://arxiv.org/abs/1105.1363v1; posted 2011-05-06T19:33:31Z.
- Bert Zwart; Conjectures on Symmetric Queues in Heavy Traffic; http://arxiv.org/abs/2202.02366v1; posted 2022-02-04T20:05:17Z.
- Anton Braverman, J. G. Dai, Masakiyo Miyazawa; The BAR approach for multiclass queueing networks with SBP service policies; http://arxiv.org/abs/2302.05791v4; posted 2023-02-11T21:59:05Z.
- Binyamin Oz, Seva Shneer, Ilze Ziedins; Static vs accumulating priorities in healthcare queues under heavy loads; http://arxiv.org/abs/2003.14087v2; posted 2020-03-31T10:49:41Z.
- Patrick Eschenfeldt, Ben Gross, Nicholas Pippenger; Analysis of an M/M/1 Queue Using Fixed Order of Search for Arrivals and Service; http://arxiv.org/abs/1108.5356v1; posted 2011-08-26T17:24:38Z.
- Xin Liu, Ananda Weerasinghe; Admission Control for Double-ended Queues; http://arxiv.org/abs/2101.06893v2; posted 2021-01-18T06:07:50Z.
- Marko Boon, Erik Winands; Critically loaded k-limited polling systems; http://arxiv.org/abs/1505.04996v2; posted 2015-05-19T13:52:43Z.
- Nikolai Lipscomb, Xin Liu, Vidyadhar G. Kulkarni; Asymptotically Optimal Appointment Scheduling in the Presence of Patient Unpunctuality; http://arxiv.org/abs/2412.18215v2; posted 2024-12-24T06:44:03Z.
- Fabrice Guillemin, Alain Simonian; Stationary analysis of the "Shortest Queue First" service policy: the asymmetric case; http://arxiv.org/abs/1305.3496v1; posted 2013-05-15T14:39:03Z.

## Brain and earlier-attempt provenance

Read-only math recall: “symmetric queues Zwart heavy traffic”; walked claim_62a81d9a9cbfc54c216f7baa59f5a4c1f0ef1c5d4f6c3f2a818f1942f1f67925. The earlier card establishes the constants and flags uniform state-space collapse as the gap; no complete theorem was claimed.

Read-only memory recalls: “symmetric queue heavy traffic” and “symmetric queue heavy traffic mistakes.” Returned mostly unrelated records; none was used as mathematical evidence. The recall utility reported an internal failed detached-index refresh; this task issued only the specifically requested recall commands and no brain-write command.

Initial rg lookup of a literal wildcard directory failed on Windows. A subsequent Python glob/rglob search over the requested intake and codex-pool locations saved prior_records.txt (no P0391 matches at those paths). The read-only origin/master git tree was searched, with relevant paths saved in prior_git_paths.txt; git grep results are saved in prior_git_hits.txt. No repository working tree was changed.

The relevant earlier record was also read with `git show origin/master:probability_1000/probability_1000_intake_claude_20260907/raw/rank_sheet_2026-09-07.txt`; its P0391 line is saved in prior_git_show.txt. It records only the workload-collapse reduction and explicitly leaves uniform collapse unproved. This attempt does not inherit a solved verdict from that record.


## Continuation reference checks, 11 October 2026

Read-only math-store query: renewal reward regenerative stationary occupation formula. The returned renewal/occupation cards were methodological hints; none proved the present universal diffusion theorem.

Kelly author archive requests (Python urllib): https://www.statslab.cam.ac.uk/~frank/BOOK/ returned HTTP 404; https://www.statslab.cam.ac.uk/~frank/BOOKS/ succeeded (kelly_books_index.html); https://www.statslab.cam.ac.uk/~frank/rsn.html succeeded (kelly_rsn.html); https://www.statslab.cam.ac.uk/~frank/BOOKS/kelly_book.html succeeded (kelly_book.html); https://www.statslab.cam.ac.uk/~frank/BOOKS/book/ch3.pdf succeeded (kelly_ch3.pdf). The archive identifies the scan as the 1979 Wiley edition, available with copyright-holder permission. Chapter 3, Queueing Networks, has 38 scanned pages; pypdf extraction produced no body text (kelly_ch3.txt). No word-for-word theorem quotation from this scan is asserted. This reference is a standard stationary product-form input, not a literature solution of P0391.

Local corroboration search, 2026-10-11: rg -n -C 3 with pattern symmetric|residual|remaining|stationary distribution|product.form on citing_fairness.txt returned no matches (exit 1). No additional stationary-law theorem was inferred from that search. Final literature classification: no exact published solution verified; the solved verdict refers to the new proof in FULL_PROOF.md, not SOLVED_IN_LITERATURE.
