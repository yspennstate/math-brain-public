# Literature and provenance — P0336

Date of all searches: 2026-10-12. Access used Python urllib from the shell, no built-in web search.

## Primary source, confirmed

Eustasio del Barrio, Alberto González-Sanz, Jean-Michel Loubes, David Rodríguez-Vítores. *Distributional Limit Theory for Optimal Transport*. arXiv:2505.19104v2, revised 13 July 2026. https://arxiv.org/abs/2505.19104v2 ; DOI 10.48550/arXiv.2505.19104. Problem 4, PDF page 30 (context starts page 29). Both downloaded PDF URLs yielded the same 43-page document. The abstract page confirms v2 and the revision date.

Exact Problem 4 wording (line breaks/typesetting normalized, notation retained):

> Problem 4 ([128]). Let X₁, …, Xₙ iid ∼ Uniform[0,1]² and Y₁, …, Yₙ iid ∼ Uniform([2,3] × [0,1]). Let πₙ be the empirical optimal transport plan. Find the limit as n → ∞ of πₙ.

Its preceding paragraph specifies Euclidean cost and notes that every vertical-coordinate-preserving population coupling has cost 2. The problem line does not explicitly state independence between the two samples or a convergence mode; our exact task additionally specifies sample independence. It uses equal sample sizes and uniform atom weights. Reference [128] is Filippo Santambrogio, *Optimal Transport for Applied Mathematicians*, Birkhäuser/Springer, 2015.

## Complete request log

- 2026-10-12 | source_pdf | https://arxiv.org/pdf/2505.19104 | ok | 537560 bytes
- 2026-10-12 | source_abs | https://arxiv.org/abs/2505.19104 | ok | 40605 bytes
- 2026-10-12 | arxiv | http://export.arxiv.org/api/query?search_query=all:%22empirical%20optimal%20transport%22%20AND%20all:%22Euclidean%22&start=0&max_results=20 | ok | 3528 bytes
- 2026-10-12 | openalex | https://api.openalex.org/works?search=Distributional%20Limit%20Theory%20for%20Optimal%20Transport&per-page=10 | HTTP Error 429: Too Many Requests
- 2026-10-12 | crossref | https://api.crossref.org/works?query=empirical%20Euclidean%20transport%20plan%20rectangles&rows=10 | ok | 99690 bytes
- 2026-10-12 | semantic | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2505.19104?fields=title,authors,year,citations.title,citations.externalIds,citations.year | HTTP Error 429: 
- 2026-10-12 | github | https://api.github.com/search/repositories?q=empirical+optimal+transport+euclidean | ok | 55 bytes
- 2026-10-12 | source_v2 | https://arxiv.org/pdf/2505.19104v2 | ok | 537560 bytes
- 2026-10-12 | arxiv_selection | http://export.arxiv.org/api/query?search_query=all%3A%22optimal%20transport%22%20AND%20%28all%3Aselection%20OR%20all%3Anonunique%20OR%20all%3Arectangles%29&start=0&max_results=40&sortBy=submittedDate&sortOrder=descending | ok | 95103 bytes
- 2026-10-12 | openalex_retry | https://api.openalex.org/works?search=%22Distributional%20Limit%20Theory%20for%20Optimal%20Transport%22&per_page=5 | HTTP Error 429: Too Many Requests
- 2026-10-12 | semantic_retry | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2505.19104/citations?fields=title,year,externalIds&limit=100 | ok | 1446 bytes
- 2026-10-12 | crossref_recent | https://api.crossref.org/works?query=empirical%20optimal%20transport%20nonunique%20Euclidean&filter=from-pub-date:2026-07-13&rows=20 | ok | 221599 bytes
- 2026-10-12 | github_rectangles | https://api.github.com/search/repositories?q=optimal%20transport%20rectangles | ok | 5916 bytes
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2609.22240 | ok
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2608.29565 | ok
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2607.18191 | ok
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2610.10257 | ok
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2609.13587 | ok
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2609.05062 | ok
- 2026-10-12 | arxiv_pdf_lead | https://arxiv.org/pdf/2607.16881 | ok
- 2026-10-12 | openalex_doi | https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2505.19104 | HTTP Error 429: Too Many Requests
- 2026-10-12 | openalex_source_filter | https://api.openalex.org/works?filter=title.search:Distributional%20Limit%20Theory%20for%20Optimal%20Transport&per-page=5 | HTTP Error 429: Too Many Requests
- 2026-10-12 | arxiv_specific | http://export.arxiv.org/api/query?search_query=%28all%3A%22Euclidean%22%20AND%20all%3A%22empirical%22%20AND%20all%3A%22transport%22%29%20OR%20%28all%3A%22transport%22%20AND%20all%3A%22separated%20rectangles%22%29%20OR%20%28all%3A%22transport%22%20AND%20all%3A%22separated%20squares%22%29&max_results=50&sortBy=submittedDate&sortOrder=descending | ok

Search queries are encoded exactly in the logged URLs. Raw replies are saved by service name in this folder. Failed requests are recorded, not interpreted as zero results. OpenAlex source searches and DOI lookup all returned HTTP 429; therefore its source identifier could not be resolved and a reliable OpenAlex citing-works query was not possible. Semantic Scholar citations succeeded on retry, providing an independent citing-paper list.

## Results screened

arXiv first query returned Hundrieser et al. (2022), a cost distributional-limit paper. The broader selection query returned 40 recent entries through 2026-10-08; the specific Euclidean/empirical/rectangles query returned 50 entries. None of their titles or abstracts stated a theorem settling this empirical-plan selection question. Crossref queries returned mostly unrelated records; the recent query includes regularization and free-probability works, but no identified exact answer. GitHub first query returned zero repositories; the rectangle query returned philippbogdan/historical-cartogram, an application rather than a proof.

The three post-revision Semantic Scholar citing arXiv papers and four selection-related leads were downloaded and text-screened in full for rectangles, Problem 4, empirical optimal transport plans, separation, and selection. Their main statements and abstracts concern different models:

- Jakwang Kim and Dohyun Kwon. *Statistical Inference for Adversarial Training: Central Limit Theorems via Optimal Transport*. arXiv:2609.22240, 2026. https://arxiv.org/abs/2609.22240. Partial transport/adversarial classification and CLTs for values/potentials, not the selected bipartite Euclidean plan.
- Yuanlong Ruan. *Central limit theorem for Wasserstein projection — the case of convex order*. arXiv:2608.29565, 2026. https://arxiv.org/abs/2608.29565. Convex-order projection and limit theorems for transport values/potentials; different optimization constraints.
- Carlos Cardoso-Perelló, Alberto González-Sanz, Marcel Nutz. *Sharp Asymptotics for Regularized Optimal Transport*. arXiv:2607.18191, 21 July 2026. https://arxiv.org/abs/2607.18191. Small Lp/entropic regularization asymptotics; different perturbation mechanism from empirical unregularized optimization.
- Luca Nenna, Brendan Pass, Paul Pegon, Louis Tocquec. *First-order Γ-expansion for entropic optimal transport with non-degenerate costs*. arXiv:2610.10257, 8 October 2026. https://arxiv.org/abs/2610.10257. Entropic selection for non-degenerate contact sets; Euclidean cost here is degenerate along a continuum of horizontal destinations and no empirical selection theorem is supplied.
- Yash Kanoria. *The Generalized Excursion Coupling as the Limit of Concave Optimal Transport*. arXiv:2609.13587, 15 September 2026. https://arxiv.org/abs/2609.13587. Concave cost perturbations with fixed measures, not sampling. May inform comparison models but cannot answer Problem 4 as posed.
- Marcello Carioni, Leonardo Del Grande, José A. Iglesias, Hidde Schönberger. *From plans to maps: Nonlocal regularization of optimal transport*. arXiv:2609.05062, September 2026. https://arxiv.org/abs/2609.05062. Nonlocal regularization and vanishing-regularization selection, not unregularized empirical plans.
- Maja Gwóźdź. *Entropic optimal transport need not select a zero-temperature limit*. arXiv:2607.16881, July 2026. https://arxiv.org/abs/2607.16881. Counterexample on a different compact metric space with a constructed Lipschitz cost; neither Euclidean rectangles nor empirical sampling.

Earlier citing papers returned by Semantic Scholar: *Finite-sample bounds for regularized optimal transport*, arXiv:2606.25947; *Distributional Convergence of Empirical Entropic Optimal Transport and Statistical Applications*, arXiv:2604.12940; *Linearization of Monge–Ampère Equations and Statistical Applications*, arXiv:2408.06534. They predate the source revision and are leads concerning regularized/strictly convex settings, not identified exact solutions.

## Read-only research brain and previous attempts

Before/during the attempt: brain.py recall "Euclidean optimal transport empirical plan nonunique mistakes" and "optimal transport empirical Euclidean"; math_recall.py --id claim_3c392ffd6a1ec5cf5a1a7386052aac8df99c7623f256e41bddf475ceb9ecb092. Memories were mostly off-topic; the mathematical card contains the correct vertical-support reduction. The recall command itself reported an automatic detached index refresh; no remember/update command was issued. Further brain recalls were avoided.

Read intake problems.jsonl/attempts.jsonl/sources.jsonl matching P0336, the 2026-10-10 codex-pool result, and git show origin/master for P0336 paths. Saved repository extracts repo_P0336_*.txt are reference material, not external instructions. Important prior material: research7_2026-09-17/R7-05/artifacts/2026-09-19/2026-09-19T075000Z__P0336_ray_degeneracy_and_fiber_cell_problem.md and the 2026-09-19T135300Z six-run handoff. It reports quadratic/common-slope degeneracy and a remaining microscopic compatibility problem. Its two-bin/conditioned surrogate results do not settle the original iid continuous-mark problem and have not been adopted without proof.

## Literature verdict

No exact solving theorem was located. This is a bounded search, with OpenAlex rate limits, not a certificate that the literature contains no solution. VERDICT is not SOLVED_IN_LITERATURE. Related regularization results and prior local-model calculations remain leads.

## Additional exact references from arXiv screening

- Shayan Hundrieser, Marcel Klatt, Thomas Staudt, Axel Munk. *A Unifying Approach to Distributional Limits for Empirical Optimal Transport*. arXiv:2202.12790v1, 25 February 2022. https://arxiv.org/abs/2202.12790. Limit laws for the cost functional via dual empirical processes, not identification of nonunique primal plan selection.
- Johan Segers. *Graphical and uniform consistency of estimated optimal transport plans*. arXiv:2208.02508v1, 4 August 2022. https://arxiv.org/abs/2208.02508. Abstract explicitly discusses squared Euclidean cost, so it cannot be substituted for the non-strict Euclidean distance model here.

Full titles, authors, timestamps and abstracts from all three arXiv API searches are saved in arxiv_screening.json. Publication/submission dates can differ from dates printed inside downloaded PDFs; those differences are retained in the raw records. No exact solving theorem was found in the inspected material.

## Second-attempt brain questions and neighboring theorem

2026-10-12, math_recall.py: "Euclidean empirical transport horizontal kernel selection noncrossing transport rays microscopic matching". Returned the prior P0336 vertical-support card and off-target cards; no selection theorem.

2026-10-12, math_recall.py: "Hamilton Jacobi Burgers Benamou Brenier perspective quadratic cost noncrossing optimal matching". Returned mostly algebraic Jacobi/quadratic cards and other off-target work; no applicable kinetic or Hamilton–Jacobi selection theorem. These calls used only the read-only math-recall interface.

The maximum-displacement probability rate uses the standard Dvoretzky–Kiefer–Wolfowitz bound with the sharp constant: P(sup|F_n-F|>t) <= 2 exp(-2nt^2). Reference: Pascal Massart, *The tight constant in the Dvoretzky–Kiefer–Wolfowitz inequality*, Annals of Probability 18(3) (1990), 1269–1283, DOI 10.1214/aop/1176990746. Original reference: Aryeh Dvoretzky, Jack Kiefer, Jacob Wolfowitz, *Asymptotic minimax character of the sample distribution function and of the classical multinomial estimator*, Annals of Mathematical Statistics 27(3) (1956), 642–669, DOI 10.1214/aoms/1177728174. These standard references are not solving the P0336 plan-selection question. No additional online solution search or claim of literature closure is made in the second attempt.

The Hopf–Lax semigroup and kinetic formulas in the new attempt are proved directly for the finite problem. No external viscosity or superposition theorem is asserted to identify empirical endpoint labels.
