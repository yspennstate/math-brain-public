# Literature and source verification

Research date: 2026-10-12 (environment date). All online requests use Python urllib.

## Status conclusion

No source-matching solution in print was found in this bounded search. This is not a claim of exhaustive bibliographic coverage. In particular, the later multiscale paper explicitly leaves the resonance regime open and changes the conjecture's scope. **Not SOLVED_IN_LITERATURE.**

## Relevant references and exact scope

1. Achyut Kumar. *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*. arXiv:2608.15987v1, submitted 17 August 2026, 00:45:04 UTC according to the fetched arXiv API. Source downloaded as source_pdf.pdf and source_html.txt; extracted PDF text in source_pages.txt. Definition 2.3 and Hypothesis 2.4 are on printed page 9; Proposition 9.1 and Example 9.2 on page 23; Conjecture 11.8 on page 30. ATTEMPT.md records the statement and hypotheses. Its source-authored p=3/4 example is the target used in the counterexample.

2. Achyut Kumar and Abhinav Duddala. *Two problems for threshold cascades of interacting diffusions on unimodular random trees: front propagation with a Bramson correction, and the continuous-type limit theory*. arXiv:2608.21125v1, submitted 21 August 2026, 14:04:51 UTC in the fetched arXiv API. Recovered by arXiv search and OpenAlex; abstract page fetched as companion_abs.txt. Related front/continuous-type problems, not a theorem with the exact hypotheses and quantifiers of Conjecture 11.8. Prior local repository attempt also identifies this as a companion, not a closure. No solution-in-print claim is made from its abstract.

3. Achyut Kumar and Abhinav Duddala. *A multiscale front-decoupling criterion for threshold cascades on unimodular random trees*. arXiv:2609.27972v1. The fetched arXiv API and PDF header say 24 August 2026, 02:34:25 UTC despite the identifier's 2609 prefix; this metadata discrepancy is retained rather than silently corrected. Saved later_pdf.pdf, later_abs.txt and later_pages.txt. Theorem 3.1 starts on printed page 7 and its bound is on page 8. It requires bounded degrees, ellipticity, irreducibility, a finite block with ρ(G_{L0,T0})<1, and an additional block echo/volume inequality. Its stated bound is subcritical with an explicit factor (1−ρ(M))^−1; the critical-window version retains nε(δ_n)→0. These are extra hypotheses, not the conjecture's full regime or uniform window. Theorem 4.6 on page 11 requires a channel contraction condition and an additional derivative-tail hypothesis. Page 2 explicitly calls several steps proof sketches. Page 12 states a new Conjecture 5.2 about a possible phase boundary, not a proof of full-regime decoupling.

Exact decisive quotations from the later paper:

> “We do not prove κ_eff < 1 throughout κ ≥ 1, and give a heuristic for why the resonance regime γL_σ/α ≥ 1 should be a genuine phase boundary rather than a technical gap. The series’ conjecture is rescoped accordingly.” (Abstract, printed page 1; mathematical typography converted to linear notation.)

> “The resonance regime γ_max L_σ/α_min ≥ 1 is left open deliberately, with a heuristic (Remark 5.1) for why no bound of the present type can close it.” (Printed page 2.)

Consequently this paper is a relevant extension/lead and cannot justify SOLVED_IN_LITERATURE.

4. Crossref returned Daniel Lacker, Kavita Ramanan and Ruoyu Wu's related *Marginal dynamics of interacting diffusions on unimodular Galton–Watson trees*, DOI 10.1007/s00440-023-01226-4, 2023. Related general interacting-diffusion methodology; neither the search result nor its title establishes this conjecture. Also returned *Particle Systems with Local Interactions via Hitting Times and Cascades on Graphs*, arXiv:2505.18448 via OpenAlex; the math store associates cascade minimality results with this source. These are different objects/results and are not used in the proof.

Crossref also returned *Stochastic Threshold Cascades of Interacting Diffusions on the Connectome: A Branching-Process Universality Theory for Critical Neurodegeneration*, DOI 10.2139/ssrn.7491898, 2026; title-only lead, not verified as a solution. Remaining results were generic network contagion, diffusion and random-tree papers unrelated to an exact closure; raw metadata remains saved in crossref.txt and openalex.txt.

## Citation and repository searches

The exact-title OpenAlex search identified the source as W7203703212. The works-citing query `filter=cites:W7203703212` returned zero records (openalex_citing.txt). This is bounded database coverage, not evidence that the source has no citing papers; the later preprint itself cites it.

GitHub exact-id search ultimately succeeded and returned zero repositories. The phrase `front-Markov` returned one irrelevant repository, JuanRuano1247723/frontend-markov; it is a lexical false positive, not a probability paper. Initial 403 errors and the successful retry are both recorded below.

Semantic Scholar exact-id request returned HTTP 429; the retry is recorded below. Failure to query a service is not a negative search result.

## Read-only brain and earlier attempts

On 2026-10-12 ran math_recall.py with `saturated cascade Front Markov`, brain.py recall with `front Markov saturated cascade branching mistakes`, and brain.py recall with `threshold cascade front Markov`. Store results included minimality for the different arXiv:2505.18448 system; no retrieved card closes this conjecture. No brain/store write command was invoked. The final authorized recall command itself reported an automatic detached index-refresh side effect; no such refresh was requested, and no further brain command was run after observing that output.

Searched the intake ledgers and codex_pool_2026_10_10 with rg for H0003 and 2608.15987. The wildcard passed as a literal path initially failed; the corrected recursive search in 06_math_research recovered intake_H_verification.md and problems.jsonl in probability_1000_intake_H_20260914. These confirm the source's locator but do not replace direct source verification.

Read git objects, without modifying the checkout, using `git -C ~/math-open-problems show origin/master:<path>` for operations/claims/H0003.md and proofnet24/NM13-11/runs/2026-09-18/2026-09-18T02-55-00Z__H0003-bethe-explicit-tv-gap.md. The latter reports the same support obstruction and exact 8/9 calculation as unpublished work, with external audit pending. It is a lead, not SOLVED_IN_LITERATURE. This report independently supplies the complete proof, the graph-approximation construction, saturation-quantifier audit, and fresh verification. We make no novelty or external-publication claim.

## Complete network request log

Each entry below records service/query URL, date, success/error, and retained response file. A second batch inadvertently reran the initial requests when importing search.py; its outputs overwrote the same raw response files. Both outcomes are retained in this log. This explains the repeated entries and the later successful GitHub requests.

- 2026-10-12: {"service": "source_abs", "url": "https://arxiv.org/abs/2608.15987", "status": 200, "bytes": 43938, "file": "source_abs.txt", "content_type": "text/html; charset=utf-8"}

- 2026-10-12: {"service": "source_pdf", "url": "https://arxiv.org/pdf/2608.15987", "status": 200, "bytes": 460608, "file": "source_pdf.pdf", "content_type": "application/pdf"}

- 2026-10-12: {"service": "source_html", "url": "https://arxiv.org/html/2608.15987v1", "status": 200, "bytes": 806073, "file": "source_html.txt", "content_type": "text/html; charset=utf-8"}

- 2026-10-12: {"service": "arxiv_id", "url": "http://export.arxiv.org/api/query?id_list=2608.15987", "status": 200, "bytes": 3333, "file": "arxiv_id.txt", "content_type": "application/atom+xml; charset=utf-8"}

- 2026-10-12: {"service": "arxiv_search", "url": "https://export.arxiv.org/api/query?search_query=all%3A%22Front-Markov%22%20OR%20all%3A%22Threshold%20cascades%22&max_results=30", "status": 200, "bytes": 43189, "file": "arxiv_search.txt", "content_type": "application/atom+xml; charset=utf-8"}

- 2026-10-12: {"service": "openalex", "url": "https://api.openalex.org/works?search=Threshold%20cascades%20of%20interacting%20diffusions%20on%20unimodular%20random%20trees&per-page=10", "status": 200, "bytes": 173999, "file": "openalex.txt", "content_type": "application/json"}

- 2026-10-12: {"service": "crossref", "url": "https://api.crossref.org/works?query=Threshold%20cascades%20of%20interacting%20diffusions%20on%20unimodular%20random%20trees&rows=10", "status": 200, "bytes": 96485, "file": "crossref.txt", "content_type": "application/json"}

- 2026-10-12: {"service": "semantic", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.15987?fields=title,authors,year,citations.title,citations.externalIds,citations.year", "error": "HTTP Error 429: "}

- 2026-10-12: {"service": "github", "url": "https://api.github.com/search/repositories?q=%222608.15987%22", "error": "HTTP Error 403: rate limit exceeded"}

- 2026-10-12: {"service": "github_front", "url": "https://api.github.com/search/repositories?q=%22front-Markov%22", "error": "HTTP Error 403: rate limit exceeded"}

- 2026-10-12: {"service": "source_abs", "url": "https://arxiv.org/abs/2608.15987", "status": 200, "bytes": 43938, "file": "source_abs.txt", "content_type": "text/html; charset=utf-8"}

- 2026-10-12: {"service": "source_pdf", "url": "https://arxiv.org/pdf/2608.15987", "status": 200, "bytes": 460608, "file": "source_pdf.pdf", "content_type": "application/pdf"}

- 2026-10-12: {"service": "source_html", "url": "https://arxiv.org/html/2608.15987v1", "status": 200, "bytes": 806073, "file": "source_html.txt", "content_type": "text/html; charset=utf-8"}

- 2026-10-12: {"service": "arxiv_id", "url": "http://export.arxiv.org/api/query?id_list=2608.15987", "status": 200, "bytes": 3333, "file": "arxiv_id.txt", "content_type": "application/atom+xml; charset=utf-8"}

- 2026-10-12: {"service": "arxiv_search", "url": "https://export.arxiv.org/api/query?search_query=all%3A%22Front-Markov%22%20OR%20all%3A%22Threshold%20cascades%22&max_results=30", "status": 200, "bytes": 43189, "file": "arxiv_search.txt", "content_type": "application/atom+xml; charset=utf-8"}

- 2026-10-12: {"service": "openalex", "url": "https://api.openalex.org/works?search=Threshold%20cascades%20of%20interacting%20diffusions%20on%20unimodular%20random%20trees&per-page=10", "status": 200, "bytes": 173999, "file": "openalex.txt", "content_type": "application/json"}

- 2026-10-12: {"service": "crossref", "url": "https://api.crossref.org/works?query=Threshold%20cascades%20of%20interacting%20diffusions%20on%20unimodular%20random%20trees&rows=10", "status": 200, "bytes": 96481, "file": "crossref.txt", "content_type": "application/json"}

- 2026-10-12: {"service": "semantic", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.15987?fields=title,authors,year,citations.title,citations.externalIds,citations.year", "error": "HTTP Error 429: "}

- 2026-10-12: {"service": "github", "url": "https://api.github.com/search/repositories?q=%222608.15987%22", "status": 200, "bytes": 55, "file": "github.txt", "content_type": "application/json; charset=utf-8"}

- 2026-10-12: {"service": "github_front", "url": "https://api.github.com/search/repositories?q=%22front-Markov%22", "status": 200, "bytes": 5754, "file": "github_front.txt", "content_type": "application/json; charset=utf-8"}

- 2026-10-12: {"service": "later_pdf", "url": "https://arxiv.org/pdf/2609.27972", "status": 200, "bytes": 523196, "file": "later_pdf.pdf", "content_type": "application/pdf"}

- 2026-10-12: {"service": "later_abs", "url": "https://arxiv.org/abs/2609.27972", "status": 200, "bytes": 43308, "file": "later_abs.txt", "content_type": "text/html; charset=utf-8"}

- 2026-10-12: {"service": "openalex_citing", "url": "https://api.openalex.org/works?filter=cites:W7203703212&per-page=100", "status": 200, "bytes": 383, "file": "openalex_citing.txt", "content_type": "application/json"}

- {"date": "2026-10-12", "service": "semantic_retry", "url": "https://api.semanticscholar.org/graph/v1/paper/search?query=%22front%20decoupling%22%20%22threshold%20cascades%22&limit=10&fields=title,authors,year,externalIds", "error": "HTTP Error 429: "}

- {"date": "2026-10-12", "service": "companion_abs", "url": "https://arxiv.org/abs/2608.21125", "status": 200, "bytes": 43781}
