# Literature and status search — F0022

Date: 2026-10-12. All network reads used Python requests from the shell. No built-in web search was used. Raw responses and the machine-readable URL log are retained in this folder. HTTP failures are search limitations, not negative literature evidence.

## Exact source

Vincent Beffara and Hugo Duminil-Copin, *Planar percolation with a glimpse of Schramm–Loewner Evolution*, Probability Surveys **10** (2013), 1–50, DOI 10.1214/11-PS186; arXiv:1107.0158v3 (2013-06-07), first submission 2011-07-01. Download: https://arxiv.org/pdf/1107.0158, saved as source.pdf with text source.txt. Section 5, printed/PDF p. 44:

> Question 1. Prove that the mean number of clusters per site κ(p) = E_p(|C|^{-1}) behaves like |1/2−p|^{2+α+o(1)}, where C is the cluster at the origin and α = −2/3.

The heading immediately above specifies **site percolation on the triangular lattice**. The displayed sentence includes neither a subtraction nor a derivative. It prints 2+α, giving 4/3, not 8/3. The source uses “behaves like” without a separate definition here. The contradiction applies to a power-law asymptotic of κ itself, including a logarithmic exponent or asymptotic order up to bounded factors.

## Relevant primary leads (not solutions of the printed question)

1. **Yu Zhang**, *A singularity at the criticality for the free energy in percolation*, arXiv:math/0301160v6, updated 2020-03-01, manuscript dated 2020-03-03; first submission 2003-01-15. Download https://arxiv.org/pdf/math/0301160, saved as zhang.pdf and zhang.txt. Definition (1.2), p. 2, and (1.4), p. 3, identify κ with the expectation of the reciprocal of the nonempty occupied cluster, with zero contribution from infinite clusters. The unnumbered **Theorem**, p. 5, reads (mathematical typesetting transcribed):

> Theorem. For percolation on the triangular lattice,
> |κ'''(p)| ≤ |p − p_c|^{−1/3+o(1)} if p ≠ p_c.
> Furthermore, we show that there is a sequence ε_n ↓ 0 such that
> |κ'''(p_c ± ε_n)| ≥ ε_n^{−1/3+o(1)}.

This is a relevant result for the intended singularity, not SOLVED_IN_LITERATURE. Line by line: (a) the model and κ agree; (b) the object in the conclusion is the third derivative, not κ; (c) the lower bound is existential in a sequence, rather than uniform for all p approaching p_c; (d) neither line asserts the printed vanishing law for κ; (e) neither line states the full background-subtracted 8/3 asymptotic. The preceding text explicitly gives the conventional heat-exponent law κ'''(p)≈|p−p_c|^{−1−α}. Its Remark 2 says: “We are unable to prove the lower bound in the Theorem for any sequence ε_n ↓ 0.” A reference to the theorem is not an independent verification of its 38-page proof.

2. **Stephan Mertens, Iwan Jensen, Robert M. Ziff**, *Universal features of cluster numbers in percolation*, Physical Review E **96**, 052119 (2017), DOI 10.1103/PhysRevE.96.052119; arXiv:1602.00644v2, updated 2017-11-15. Download https://arxiv.org/pdf/1602.00644, saved as ziff.pdf and ziff.txt. Equation (2), p. 2, gives the physics expansion

   n(p)=A_0+B_0(p−p_c)+C_0(p−p_c)^2+A_±|p−p_c|^{2−α}+…,

   with α=−2/3. This confirms the distinction between the analytic background and the singular part, and the conventional **2−α=8/3** power. The paper uses series analysis, simulation and exact enumeration, rather than a theorem proving the full infinite-lattice asymptotic with the requested quantifiers. It is a lead, not a printed solution. Its introductory p. 1 says α=2/3 while p. 2 says −2/3; our convention is fixed by the source and Eq. (2).

3. **Clément Hongler and Stanislav Smirnov**, *Critical percolation: the expected number of clusters in a rectangle*, Probability Theory and Related Fields **151** (2011), 735–756, DOI 10.1007/s00440-010-0313-8; arXiv:0909.4490. Recovered by arXiv/Crossref. The abstract concerns conformally invariant observables at criticality separating boundary points. Different observable and no near-critical κ law. Abstract-level screening only; not used in a proof.

4. **Shu-Chiuan Chang and Robert Shrock**, *Exact Results for Average Cluster Numbers in Bond Percolation on Infinite-Length Lattice Strips*, arXiv:2105.13415 (2021). Abstract-level screening only. Bond percolation on fixed-width strips, not site percolation on the full triangular lattice.

## Search ledger

Each entry below states service, exact URL encoding the query, date, result status, and raw-response filename. All returned arXiv titles/abstracts and Crossref titles were screened. GitHub returned no matching repository for the submitted query. OpenAlex and Semantic Scholar returned HTTP 429, including source-lookup/citation requests; their citation graphs could not be inspected. The attempted OpenAlex cites filter used the source DOI, but no response validated that identifier syntax. No claim of an exhaustive search or present openness is made.

- 2026-10-12 — arxiv — https://export.arxiv.org/api/query?search_query=all%3A%22percolation%22+AND+%28all%3A%22cluster+number%22+OR+all%3A%22free+energy%22+OR+all%3A%22cluster+density%22%29&max_results=30 — 200; arxiv.response
- 2026-10-12 — openalex — https://api.openalex.org/works?search=percolation+mean+number+clusters+singularity&per-page=30 — 429; openalex.response
- 2026-10-12 — crossref — https://api.crossref.org/works?query=percolation+number+clusters+singularity+critical+triangular&rows=30 — 200; crossref.response
- 2026-10-12 — semantic_scholar — https://api.semanticscholar.org/graph/v1/paper/search?query=percolation+number+clusters+singularity&limit=30&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract — 429; semantic_scholar.response
- 2026-10-12 — github — https://api.github.com/search/repositories?q=percolation+cluster+singularity&per_page=30 — 200; github.response
- 2026-10-12 — openalex_source — https://api.openalex.org/works?search=Planar+percolation+with+a+glimpse+of+Schramm+Loewner+evolution&per-page=5 — 429; openalex_source.response
- 2026-10-12 — arxiv_specific — https://export.arxiv.org/api/query?search_query=all%3Apercolation+AND+%28all%3A%22cluster+density%22+OR+all%3A%22number+of+clusters%22+OR+all%3A%22free+energy%22%29&max_results=60 — 200; arxiv_specific.response
- 2026-10-12 — crossref_specific — https://api.crossref.org/works?query=percolation+free+energy+differentiability+cluster+density+Zhang&rows=20 — 200; crossref_specific.response
- 2026-10-12 — openalex_retry — https://api.openalex.org/works?search=percolation+cluster+density&per_page=10 — 429; openalex_retry.response
- 2026-10-12 — openalex_doi — https://api.openalex.org/works/https://doi.org/10.1214/11-PS186 — 429; openalex_doi.response
- 2026-10-12 — semantic_retry — https://api.semanticscholar.org/graph/v1/paper/ARXIV:1107.0158?fields=title%2Cyear%2Ccitations.title%2Ccitations.year%2Ccitations.externalIds — 429; semantic_retry.response
- 2026-10-12 — openalex_citing — https://api.openalex.org/works?filter=cites%3Adoi%3A10.1214%2F11-PS186&per-page=50 — 429; openalex_citing.response
- 2026-10-12 — crossref_zhang — https://api.crossref.org/works?query.title=A+singularity+at+the+criticality+for+the+free+energy+in+percolation&rows=3 — 200; crossref_zhang.response
- 2026-10-12 — crossref_ziff — https://api.crossref.org/works?query.title=Universal+features+of+cluster+numbers+in+percolation&rows=3 — 429; crossref_ziff.response

## Read-only brain, intake, and repository checks

- math_recall.py query: “percolation mean number clusters free energy alpha”. Returned mostly off-topic cards; no proof inherited.
- brain.py recall queries: “percolation cluster count mistakes” and “percolation mean number clusters singularity”. Returned mostly off-topic memories. These commands were the prescribed recall interface; no remember/update command was used.
- Intake JSONL and codex_pool search: F0022; saved prior_ledger_hits.txt. The 2026-09-08 attempt incorrectly says “2 + alpha = 8/3” and mixes the printed formula with a Taylor-subtracted formulation. Those claims were not inherited.
- git ls-tree of origin/master, filtered to F0022, followed by git show (no working-tree change). Saved prior_git_paths.txt and prior_git_endpoint.txt. Read research7_2026-09-17/R7-01/admission/2026-09-19T151417Z__F0022_literal_endpoint_screen.md, which already contains the singleton lower bound and refuses to equate it with the intended singularity. Our elementary proof was written before reading this note, and agrees with it. No novelty is claimed.

## Status conclusion

**No SOLVED_IN_LITERATURE verdict.** The exact printed formula is false by the elementary proof in ATTEMPT.md. Zhang's revised primary manuscript is a substantial lead for a different, intended formulation. The bounded search does not certify whether that repaired formulation is open today.
