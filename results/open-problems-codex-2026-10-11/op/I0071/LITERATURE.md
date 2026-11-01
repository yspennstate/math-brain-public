# Literature search

## Source and status standard

Antonio Agresti and Mark Veraar, **Nonlinear SPDEs and Maximal Regularity:
An Extended Survey**, *Nonlinear Differential Equations and Applications
NoDEA* **32**, article 123 (2025), DOI **10.1007/s00030-025-01090-2**;
preprint **arXiv:2501.18561**. Final publication fetched 2026-10-12 from
https://repository.tudelft.nl/file/File_783e6459-5d3b-4957-bcd3-64da5b8d9025
and saved as source.pdf; source.txt contains page-delimited extraction.
Problem 7 is on printed page 131, PDF page 132 including the cover.
Equation (8.14), Assumption 8.4, Theorem 8.6, Theorem 8.9 and Proposition
8.10 are on printed pages 96--100. The source includes two additional
superlinear-noise questions after its six conditions. Full transcription
and conventions are in ATTEMPT.md Section 1.

**No SOLVED_IN_LITERATURE verdict is established.** No inspected paper
states and proves the full question with its domain, coefficient and
noise-growth scope. The literature search is bounded, not an exhaustive
certificate of openness. Rate-limited searches are explicitly incomplete.

## Relevant references and hypothesis comparison

1. **Dionysis Milesis and Michael Salins**, *Global in time solutions to
   stochastic reaction-diffusion systems with superlinear reactions
   satisfying a triangular control of mass*, **arXiv:2604.06645v2**,
   revised 26 May 2026 (PDF date 27 May 2026),
   https://arxiv.org/abs/2604.06645. Saved lead2604.pdf and lead2604.txt.
   This is a directly relevant post-source positive result, not a full
   solution to I0071: equation (1), PDF p. 1, has multiplicative
   reaction noise and **no b dot grad u transport noise**. It works on
   bounded smooth domains with Dirichlet or Neumann conditions. Its
   Assumptions 5--7, p. 11, give local Lipschitz continuity, face
   vanishing, and **linear growth** of sigma; "superlinear" in the
   title refers to the reactions. Its Assumptions 8--11, pp. 12--13,
   concern covariance kernels and heat kernels. Thus neither arbitrary
   source-admissible transport nor optimal superlinear reaction noise is
   covered. Its stochastic-convolution/duality method is a useful lead.
   Theorems 5.1 and 5.2 are on PDF pp. 29 and 31, respectively; the
   latter concludes: "In particular, system (53) has a unique global
   mild solution." This is quoted only as a related theorem: system
   (53) omits transport, so no line-by-line implication for full I0071
   is asserted. Remark 1, p. 10, explains the general nonnegative lower
   triangular-matrix variant of its displayed prefix-sum assumption.

2. **Antonio Agresti, Michael Kniely and Bao Quoc Tang**, *Global
   classical solutions by transport noise for reaction-diffusion systems
   with entropy dissipation*, **arXiv:2608.13332v1**, submitted
   13 August 2026 (PDF date 14 August 2026),
   https://arxiv.org/abs/2608.13332. Saved lead2608.pdf and lead2608.txt.
   The abstract and equation (1.1), pp. 1--2, impose a specially chosen
   divergence-free transport noise and an entropy/complex-balance
   structure. The conclusion is global existence with arbitrarily high
   probability after suitable choice of noise, not almost sure global
   existence for every source-admissible species-dependent coefficient.
   It therefore does not solve Problem 7 as posed.

3. **Antonio Agresti, Max Sauerbrey and Mark Veraar**, *A stochastic flow
   approach to De Giorgi-Nash-Moser estimates for SPDEs with smooth
   transport noise*, **arXiv:2511.12692v1**, submitted 16 November 2025
   (PDF date 18 November 2025),
   https://arxiv.org/abs/2511.12692. Retrieved through the source's
   Semantic Scholar citation list; saved lead2511.pdf and lead2511.txt.
   A scalar regularity tool with smooth transport is a relevant duality
   lead, not a theorem identifying all the triangular hypotheses of
   Problem 7. Its Theorem 1.1 is a scalar regularity result.

4. **Antonio Agresti and Mark C. Veraar**, *Reaction-diffusion equations
   with transport noise and critical superlinear diffusion: Local
   well-posedness and positivity*, *Journal of Differential Equations*
   **368**, 247--300 (2023). Source reference [13]. This supplies local
   theory, not the global triangular conclusion.

5. **Antonio Agresti and Mark C. Veraar**, *Reaction-diffusion equations
   with transport noise and critical superlinear diffusion: global
   well-posedness of weakly dissipative systems*, *SIAM Journal on
   Mathematical Analysis* **56**(4), 4870--4927 (2024), DOI
   **10.1137/23M1562482**. Source reference [14]. This gives related
   coercive/weakly dissipative models; the later survey still poses
   general triangular systems as Problem 7.

6. **Jeff Morgan**, *Boundedness and decay results for reaction-diffusion
   systems*, *SIAM Journal on Mathematical Analysis* **21**(5),
   1172--1189 (1990). Source reference [200]. A deterministic lead for
   triangular Lyapunov estimates, not a stochastic theorem.

7. **Michel Pierre**, *Global existence in reaction-diffusion systems
   with control of mass: a survey*, *Milan Journal of Mathematics*
   **78**(2), 417--455 (2010). The source bibliography lists this as
   **[212]**, whereas the paragraph following Problem 7 says
   "[213, Theorem 3.5]"; [213] is actually Pisier's martingale book.
   Similarly its reference [201] is Neelima and Siska's SPDE paper,
   despite being cited there as a deterministic triangular result.
   We record this reference-number inconsistency rather than silently
   treating the wrong numbered references as proofs.

8. *An optimal local theory for reaction-diffusion equations driven by
   non-trace-class noise*, **arXiv:2606.07417**, was identified in the
   source's Semantic Scholar citing list. Its arXiv metadata request was
   rate-limited. The title is a local-theory lead, not a verified global
   triangular theorem; it is not credited as solving any part of I0071.

## Read-only prior-work consultation

On 2026-10-12 ran math_recall.py with "Agresti Veraar triangular reaction
diffusion", brain.py recall with "stochastic reaction diffusion triangular
structure" and "reaction diffusion mistakes", and subsequently
math_recall.py with "Morgan polynomial Lyapunov intermediate sums reaction
diffusion" and --id
claim_f7f4e25ba040e644da3bc17c836e3e862b47b1982649e742a1fe20b8f5865d7e.
The useful earlier attempt establishes nonexplosion for spatially
constant SDEs and records the missing spatial estimates. It does not
provide a checked general theorem. Unrelated trading and Arnold-diffusion
recall hits were not opened or used.

The I0071 intake row was read from
06_math_research/probability_1000_intake_I_20260914/problems.jsonl.
The requested intake attempts and codex_pool were searched; no matching
I0071 attempt provided a full proof. The first PowerShell rg invocation
used an unexpanded path wildcard and failed; it was repeated using actual
directory paths. A broad repository path listing was then narrowed.

Read only, using git show origin/master, the two files
research7_2026-09-17/R7-01/admission/2026-09-18T200857Z__I0071_full_source_scope_screen.md
and
research7_2026-09-17/R7-01/admission/2026-09-18T201007Z__I0071_source_scope_erratum.md.
They correctly warn that the two final reaction-noise questions must be
retained. Their procedural admission instructions are not applicable to
this task and were not treated as instructions.

## API search log

The OpenAlex source-ID lookup was rate-limited, so a correctly resolved
OpenAlex-ID citing-works search could not be completed. A subsequent
`filter=cites:doi:...` request was also made but is not a valid substitute
for the required OpenAlex work-ID filter; its failed response is
inconclusive. Semantic Scholar's direct DOI request did return 40 citing
entries, all saved in search_semantic_doi.txt, and those titles were
screened. The title search returned 429 before that successful DOI query.
The arXiv polynomial/Lyapunov follow-up returned a non-XML failure rather
than an empty result list; no negative result is inferred from it.

Search date: 2026-10-12. Raw responses saved locally; failed requests do not establish absence of a solution.

- arxiv: `https://export.arxiv.org/api/query?search_query=all%3A%22triangular%22%20AND%20all%3A%22stochastic%22%20AND%20all%3A%22reaction%22&max_results=30`. Result: OK. Saved search_arxiv.txt.
- openalex: `https://api.openalex.org/works?search=stochastic%20reaction%20diffusion%20triangular&per-page=30`. Result: <HTTPError 429: 'Too Many Requests'>. Saved search_openalex.txt.
- crossref: `https://api.crossref.org/works?query=stochastic%20reaction%20diffusion%20triangular&rows=20`. Result: OK. Saved search_crossref.txt.
- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=stochastic%20reaction%20diffusion%20triangular&limit=20&fields=title,authors,year,externalIds,abstract`. Result: <HTTPError 429: ''>. Saved search_semantic.txt.
- github: `https://api.github.com/search/repositories?q=stochastic%20reaction%20diffusion%20triangular`. Result: OK. Saved search_github.txt.
- source_metadata: `https://api.openalex.org/works?search=Nonlinear%20SPDEs%20and%20maximal%20regularity&per-page=5`. Result: <HTTPError 429: 'Too Many Requests'>. Saved search_source_metadata.txt.

- 2026-10-12, follow-up: `https://arxiv.org/pdf/2604.06645`. OK 426416; lead2604.pdf.

- 2026-10-12, follow-up: `https://export.arxiv.org/api/query?search_query=all%3A%22reaction-diffusion%22%20AND%20all%3A%22transport%22%20AND%20submittedDate%3A%5B202501010000%20TO%20202610122359%5D&max_results=40`. OK 87134; search_arxiv_transport.txt.

- 2026-10-12, follow-up: `https://api.openalex.org/works/https://doi.org/10.1007/s00030-025-01090-2`. <HTTPError 429: 'Too Many Requests'>; search_openalex_doi.txt.

- 2026-10-12, follow-up: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s00030-025-01090-2?fields=title,year,citations.title,citations.year,citations.externalIds`. OK 9963; search_semantic_doi.txt.

- 2026-10-12, follow-up: `https://api.crossref.org/works?query.title=Global%20stochastic%20reaction%20diffusion%20triangular&filter=from-pub-date:2025-01-01&rows=15`. OK 189346; search_crossref_focused.txt.

- 2026-10-12: `https://export.arxiv.org/api/query?search_query=all%3A%22reaction-diffusion%22%20AND%20%28all%3A%22Lyapunov%22%20OR%20all%3A%22polynomial%22%29%20AND%20all%3A%22transport%20noise%22&max_results=30`. TimeoutError('The read operation timed out'); search_arxiv_lyapunov.txt.

- 2026-10-12: `https://api.openalex.org/works?filter=cites:doi:10.1007/s00030-025-01090-2&per-page=30`. <HTTPError 429: 'Too Many Requests'>; search_openalex_citing.txt.

- 2026-10-12, citation/transport lead: `https://arxiv.org/pdf/2608.13332`. OK 891533; lead2608.pdf.

- 2026-10-12, citation/transport lead: `https://arxiv.org/pdf/2511.12692`. OK 757230; lead2511.pdf.

- 2026-10-12, citation/transport lead: `https://export.arxiv.org/api/query?id_list=2606.07417`. <HTTPError 429: 'Unknown Error'>; lead2606_metadata.txt.
