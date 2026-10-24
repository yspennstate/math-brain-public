# P0360 literature check — 2026-10-11

## Status and scope

No paper found in this bounded search states and proves Question 1 with its unrestricted quantifiers. This is not a certificate that no such paper exists. Several API requests were rate limited; successful and failed requests are recorded below and in `search_log.json`. Verdict is PARTIAL, not SOLVED_IN_LITERATURE.

## Verified primary source

Balázs Ráth, Jan M. Swart, Márton Szőke, *A phase transition between endogeny and nonendogeny*, Electronic Journal of Probability **27** (2022), 1–43, DOI **10.1214/22-ejp872**; arXiv **2103.14408v2**. Downloaded https://arxiv.org/pdf/2103.14408 as `source.pdf`; extracted text in `source.txt`.

Question 1, PDF p.8, verbatim (mathematical typography transcribed):

> Does endogeny of the RTP (ω_i, Y_i)_{i∈T} imply almost sure uniqueness of solutions to the frozen percolation equation (1.3)?

Immediately following, the authors write:

> In other words, Question 1 asks whether in part (ii) of Lemma 7, one can remove the conditions that F and F′ are stationary, adapted, and respect the tree structure.

The general freezing set is a deterministic relatively closed subset Ξ⊂(0,1]. Innovations are iid uniform on [0,1]×{1,2}. Equation (1.3), p.4, defines the frozen set by existence of an infinite legal open path above an internal point at an allowed time no later than its activation. The comparison is of solutions on the SAME innovations, with arbitrary extra randomness permitted. It is not merely a question about the local burning-time recursion.

Relevant results and limitations:

- Theorem 1, p.4: existence and uniqueness in law under stationarity, adaptation and respect for the tree structure. These are exactly the restrictions the question asks to remove.
- Lemma 7, p.8: endogeny is equivalent to almost sure uniqueness WITH those three restrictions.
- Theorem 9, p.9: for Ξ_θ={θ^n:n≥0}, the canonical burning RTP is endogenous for 0<θ≤θ_* and nonendogenous for θ_*<θ≤1; θ_* is strictly above 1/2. This theorem does not establish unrestricted uniqueness in the endogenous regime.
- Pages 8–9 conjecture unrestricted uniqueness for θ<1/2 and equality of the alternating frozen-set envelopes. On p.9 the authors expressly say that even this would not fully settle Question 1 because θ_*>1/2.
- Page 7 observes unrestricted uniqueness for finite Ξ. Proposition A in ATTEMPT.md extends this elementary argument to well-ordered Ξ. This is our argument, not a solution in print.

## Later citing papers checked

Semantic Scholar's DOI citation endpoint returned two citing records:

1. Jacob van den Berg and Pierre Nolin, *A 2D forest fire process beyond the critical time*, arXiv:2210.05642v1 (2022). Downloaded and text-extracted as `forest_pdf.pdf` and `forest_pdf.txt`. The paper studies finite-volume-threshold forest fires on planar lattices. Its discussion cites the nonendogeny work and the phase-transition source, but its main theorem answers a planar forest-fire question, not unrestricted uniqueness of (1.3). Different objects and hypotheses: not a solution of P0360.
2. Dhruv Bhasin and Moumanti Podder, *Combinatorial games on Galton–Watson trees involving several-generation-jump moves*, arXiv:2205.02124; published DOI 10.2140/cnt.2024.13.1. Downloaded and text-extracted as `games_pdf.pdf` and `games_pdf.txt`. The phase-transition paper is cited among references about interpretability and endogeny of tree automata. The paper's results concern normal/misère games with k-jump moves, not frozen-percolation equation (1.3). Not a solution of P0360.

OpenAlex source lookup identified **W3151302596**, with cited_by_count=1. Citation requests are separately logged; API coverage differs from Semantic Scholar and is not taken as definitive.

## General-theory lead checked

Tibor Mach, Anja Sturm and Jan M. Swart, *A new characterization of endogeny*, Mathematical Physics, Analysis and Geometry **21** (2018), article 30; arXiv:1801.05253v4. Downloaded and extracted as `characterization_pdf.pdf` and `characterization_pdf.txt`. Theorem 1, PDF p.5, equates endogeny with bivariate uniqueness in the class of symmetric probability measures with a SPECIFIED marginal μ. Lemma 6, p.8, concerns iid boundary variables of law μ, independent of the innovations. Neither result supplies the missing marginal or independence properties for arbitrary frozen solutions. This is a lead and an explanation of why the usual bivariate argument does not settle the question.

Other relevant records returned by arXiv:

- Balázs Ráth, Jan M. Swart and Tamás Terpai, *Frozen percolation on the binary tree is nonendogenous*, Annals of Probability **49** (2021), 2272–2316, DOI 10.1214/21-aop1507, arXiv:1910.09213v3. This is the prior nonendogenous continuous-time model, not a proof of the endogenous implication.
- Antar Bandyopadhyay, *Bivariate Uniqueness and Endogeny for Recursive Distributional Equations: Two Examples*, arXiv:math/0407175v2. The returned abstract explicitly says the paper was withdrawn because of a flaw in the claimed frozen-percolation endogeny proof. It is not usable as a theorem establishing P0360.
- Antar Bandyopadhyay, *A Necessary and Sufficient Condition for the Tail-Triviality of a Recursive Tree Process*, arXiv:math/0511203v2. Tail triviality is a different property and does not remove P0360's restrictions.
- Victor Kleptsyn and Michele Triestino, *Cut-off method for endogeny of recursive tree processes*, arXiv:1610.06946v1. Returned by the general endogeny query; not fetched or used as a theorem about P0360.

## Read-only research brain and prior records

Read math-store attempt card `claim_fcd7e048146e9447002600e2274fbc2261998c4606ed8a47a7ff8b2627161729`. It records the alternating antitone-envelope bound and the failure of that method when F_2=empty for θ≥1/2; source p.9 independently confirms this obstruction. No reliance on the card as a correctness verdict.

Ran brain recalls for “frozen percolation endogeny mistakes” and “frozen percolation recursive tree process”; returned memories were not sufficiently on target to use as mathematical evidence. Did not intentionally write to the brain or any external repository.

Searched intake and pool ledgers named problems.jsonl, attempts.jsonl, sources.jsonl, recording 19 inspected paths in `prior_ledger_files.txt`; no P0360 rows were found by this filename-limited scan (`prior_ledger.json`). An initial directory-wide text search did expose the previous ranking's antitone-envelope summary but produced excessive unrelated output; it was not treated as an exhaustive prior-work review. A read-only `git ls-tree origin/master` filename scan found no P0360-named published paths (`published_paths.txt`). No repository working tree was changed.

## All HTTP requests

The generated appendix below records every source/search/lead-fetch URL, date, service and outcome. Raw successful API responses are retained beside this file. Rate-limit failures are search limitations, not negative literature evidence.

Additional attempt on 2026-10-11: reread source Lemma 20, equation (2.11), PDF p.14, to verify the finite-cutoff burning-law recurrence used in SECOND_ATTEMPT.md. Also used the previously downloaded Mach–Sturm–Swart paper as context for why its iid-boundary convergence theorem cannot be applied to arbitrary solutions. No new online-paper claim or literature-solved verdict was made.

Additional read-only math-store queries: “endogeny arbitrary boundary conditions frozen percolation disagreement cascade Rath Swart”; “tree automata pivot tree interpretations endogeny rogue fixed point”; “Mach Sturm Swart endogeny boundary distributions convergence probability”. They returned neighbouring frozen-percolation/tree-automaton problems and standard convergence cards, but no theorem closing P0360. The precise gap is recorded in SECOND_ATTEMPT.md as a finite-time attainability probability bound.

Standard background reference for the measurability step: Alexander S. Kechris, *Classical Descriptive Set Theory*, Graduate Texts in Mathematics 156, Springer, 1995. Used standard analytic-set universal measurability and Jankov–von Neumann measurable uniformization; no assertion that those theorems imply P0360. Martingale convergence and maximal coupling are used only with the hypotheses spelled out in Proposition F.

| Date | Service/request | URL/query | Outcome |
|---|---|---|---|
| 2026-10-11 | arXiv primary PDF | https://arxiv.org/pdf/2103.14408 | OK; source.pdf and source.txt |
| 2026-10-11 | arxiv | https://export.arxiv.org/api/query?search_query=all%3A%22frozen%20percolation%22%20AND%20%28all%3Aendogeny%20OR%20all%3Auniqueness%29&max_results=30 | OK |
| 2026-10-11 | openalex | https://api.openalex.org/works?search=A%20phase%20transition%20between%20endogeny%20and%20nonendogeny&per-page=10 | HTTP Error 429: Too Many Requests |
| 2026-10-11 | crossref | https://api.crossref.org/works?query=frozen%20percolation%20endogeny%20uniqueness&rows=20 | OK |
| 2026-10-11 | semantic | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2103.14408?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds | HTTP Error 429:  |
| 2026-10-11 | github | https://api.github.com/search/repositories?q=frozen%20percolation%20endogeny | OK |
| 2026-10-11 | openalex_retry | https://api.openalex.org/works?search=frozen%20percolation&per-page=50 | HTTP Error 429: Too Many Requests |
| 2026-10-11 | crossref_source | https://api.crossref.org/works?query.title=A%20phase%20transition%20between%20endogeny%20and%20nonendogeny&rows=5 | OK |
| 2026-10-11 | arxiv_broad | https://export.arxiv.org/api/query?search_query=all:%22frozen%20percolation%22&sortBy=submittedDate&sortOrder=descending&max_results=60 | OK |
| 2026-10-11 | semantic_retry | https://api.semanticscholar.org/graph/v1/paper/search?query=frozen%20percolation&limit=50&fields=title,year,externalIds | OK |
| 2026-10-11 | openalex_doi | https://api.openalex.org/works/https://doi.org/10.1214/22-ejp872 | HTTP Error 429: Too Many Requests |
| 2026-10-11 | semantic_citations | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/22-ejp872/citations?fields=title,year,externalIds&limit=100 | OK |
| 2026-10-11 | arxiv_endogeny | https://export.arxiv.org/api/query?search_query=all:endogeny&sortBy=submittedDate&sortOrder=descending&max_results=50 | OK |
| 2026-10-11 | openalex_select | https://api.openalex.org/works/doi:10.1214/22-ejp872?select=id,title,cited_by_count | OK |
| 2026-10-11 | openalex_citing | https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1214%2F22-ejp872&per-page=50 | HTTP Error 429: Too Many Requests |
| 2026-10-11 | games_pdf | https://arxiv.org/pdf/2205.02124 | OK |
| 2026-10-11 | forest_pdf | https://arxiv.org/pdf/2210.05642 | OK |
| 2026-10-11 | characterization_pdf | https://arxiv.org/pdf/1801.05253 | OK |
| 2026-10-11 | openalex_citations | https://api.openalex.org/works?filter=cites:W3151302596&per-page=50&select=id,title,doi,publication_year,primary_location | HTTP Error 429: Too Many Requests |
| 2026-10-11 | openalex_citations_retry | https://api.openalex.org/works?filter=referenced_works:W3151302596&select=id,title,doi,publication_year&per-page=10 | HTTP Error 429: Too Many Requests |
| 2026-10-11 | crossref_focused | https://api.crossref.org/works?query.bibliographic=frozen%20percolation%20endogeny&rows=30 | OK |
| 2026-10-11 | github_broad | https://api.github.com/search/repositories?q=%22frozen%20percolation%22 | OK |
