# Literature search log

Started 2026-10-12. Initial status was unverified; final outcome below is SOLVED_IN_LITERATURE. Search responses and source excerpts are saved locally.

## Final finding: direct resolution in the literature

Keming Chen and Guillaume Woessner, **Zeros of the Brownian Sheet**, *Journal of Theoretical Probability* **38** (2025), article 33. Published 6 February 2025. DOI: https://doi.org/10.1007/s10959-024-01399-1. Preprint: https://arxiv.org/abs/2405.20019; the full text checked here is **arXiv:2405.20019v2**, 31 May 2024, 22 pages, saved as `resolution_pdf.pdf` and `resolution.txt`.

**Exact theorem quotation, Theorem 1.2, printed page 2 / PDF page 2 of v2** (only mathematical typography and line wrapping are normalized):

> Theorem 1.2 (Open problem). For N = 2 and d = 2 or 3, almost surely, for any non-zero linear map p : R² → R,
>
> dim_H[p(Z)] = dim_H(Z). (2)

The immediately preceding sentence on the same page says:

> The following theorem answers Open Problem 4.

The paragraph immediately following the theorem explicitly emphasizes that “almost surely” precedes the quantification of the linear maps. The proof is Section 2, printed/PDF pages 4–7; its final part is **Step 3**, on page 7, proving uniformity in p. Proposition 1.1, printed/PDF page 2, supplies dim_H Z = (N − d/2)⁺ almost surely. Definitions on page 1 give the same continuous, centered Gaussian Brownian sheet, with independent coordinates and covariance equal to the product of coordinate minima. Section 2, page 4, works on [1,2]² and explicitly extends to [a,b]² for 0 < a < b, so the substantive zero set is in the strictly positive quadrant, not the deterministic zero axes.

The journal publication and bibliographic details are verified by the Crossref DOI record `crossref_resolution.response`. Both the Springer article request and its PDF request returned HTTP 200 **client-challenge HTML, not usable article text or a PDF**. Accordingly, the theorem quotation and page number above refer specifically to the accessible arXiv v2, not to an uninspected journal PDF. This is a full paper containing a theorem and proof, and Crossref independently establishes its journal publication; the finding does not rely on an abstract alone.

## Source and exact hypothesis match

Davar Khoshnevisan, **Slices of Brownian Sheet: New Results, and Open Problems**, arXiv:math/0510518v1, 24 October 2005; published as **Slices of a Brownian Sheet: New Results and Open Problems**, in *Seminar on Stochastic Analysis, Random Fields and Applications V* (2007), pp. 135–174, DOI https://doi.org/10.1007/978-3-7643-8458-6_9. Fetched https://arxiv.org/pdf/math/0510518 on 2026-10-12; saved as `source.pdf` and `source.txt`.

**Exact question, Section 8.3, printed/PDF page 34** (mathematical typography normalized):

> Open Problem 4. Is there a (random) orthogonal projection such that the said projection of B⁻¹{0} has a different Hausdorff dimension than 2 − (d/2)?

> I believe that the answer is “no.” However, I have no proof nor counter-proof.

Open Problem 4 does not repeat a restriction on d. The surrounding statement is interpreted using the introduction: page 3, equation (1.7) gives dim_H Z_d = 1 ∧ (2 − d/2)⁺, and the next sentence explicitly specifies **d ∈ {2,3}** when comparing this with dim_H B⁻¹{0}. Remarks 1.3 explain that these are the only interesting dimensions for that equality. The problem concerns zeros with both parameters positive, as in (1.3) and the slice formulation (1.8). Including the zero axes would change the problem for d=3. For d=1 the displayed target 3/2 cannot be a line-image dimension; it is not the intended projection-preservation question.

**Line-by-line application (complete deduction, not a proposed extension):**

1. Set N=2 and W=B. Their coordinate covariances and coordinate independence are identical to the source's equation (1.1), so their Z is the same positive-parameter zero set in the source's substantive question.
2. Take d=2 or d=3, exactly the range singled out on source page 3. Theorem 1.2 explicitly covers both values.
3. Intersect the probability-one event of Theorem 1.2 with that of Proposition 1.1. On this single event, every nonzero scalar linear map preserves dimension, and dim_H Z = 2 − d/2.
4. For any line L through the origin, choose a unit vector u spanning L. Its orthogonal projection is P_L(x)=⟨x,u⟩u. The scalar map p_u(x)=⟨x,u⟩ is nonzero. The map r↦ru is an isometry R→L, so dim_H P_L(Z)=dim_H p_u(Z).
5. Apply the universal conclusion of Theorem 1.2 to p_u. It gives dim_H P_L(Z)=dim_H Z=2 − d/2 for **every L on the same event**.
6. In particular, for any random choice L=L(ω), including one depending arbitrarily on B, the equality holds pointwise whenever ω belongs to that event. No independence or stopping-time assumption is needed. Thus no random exceptional orthogonal line projection exists, almost surely.

This is precisely the theorem stated and proved in the later paper, not a related-model theorem or a new implication requiring additional probability estimates. Verdict: **SOLVED_IN_LITERATURE; the answer is no**.

## Read-only research-brain and earlier-attempt checks

- 2026-10-12: `brain.py recall "Brownian sheet projections mistakes"`; returned related slice-count audits, not a projection resolution.
- 2026-10-12: `math_recall.py "Brownian sheet zero set projections"`; returned related claims, none solving this question.
- 2026-10-12: searched the requested intake/pool directories for D0019. Found D0019-A001, 2026-09-08, in `probability_1000_intake_D_20260908/attempts.jsonl`. Its fixed-direction extension was asserted rather than proved; it was not used as a theorem here. An initial literal PowerShell wildcard path failed (Windows error 123); repeated with enumerated directories.
- 2026-10-12: read, using `git show origin/master:...`, `runs/R15/20260917_2358Z_successor_admission_d0019_resolution_n43d1b.md`. It named Chen–Woessner as the resolver. Independently fetched and checked the full later paper; this checkout record was only a discovery hint.
- 2026-10-12: `brain.py recall "Chen Woessner Zeros Brownian Sheet D0019"`; no exact memory entry returned.

## Search coverage and limits

All network requests were made using Python urllib from the shell. URLs, outcomes and raw responses follow below. The arXiv query returned two papers, including the exact resolver; GitHub returned zero repositories. Semantic Scholar's source lookup returned the resolver among the works citing the source. OpenAlex search, source DOI lookup, resolver DOI lookup, and citing-source query were all attempted but returned HTTP 429; no successful OpenAlex coverage is claimed. Broad Semantic Scholar search was also rate-limited, but the source-specific citation lookup succeeded. These limits do not affect the direct full-text theorem match.

- 2026-10-12 `arxiv`: http://export.arxiv.org/api/query?search_query=all%3A%22Brownian+sheet%22+AND+%28all%3Aprojection+OR+all%3AMarstrand%29&max_results=40
  Outcome: arxiv: HTTP 200, 3760 bytes. Raw response: `arxiv.response`.

- 2026-10-12 `arxiv_https`: https://export.arxiv.org/api/query?search_query=all%3A%22Brownian+sheet%22+AND+all%3Aprojection&max_results=40
  Outcome: arxiv_https: HTTP 200, 3722 bytes. Raw response: `arxiv_https.response`.

- 2026-10-12 `openalex`: https://api.openalex.org/works?search=Brownian+sheet+projections&per-page=40
  Outcome: openalex: HTTPError: HTTP Error 429: Too Many Requests. Raw response: `openalex.response`.

- 2026-10-12 `openalex_source`: https://api.openalex.org/works?search=Slices+of+Brownian+Sheet+New+Results+and+Open+Problems&per-page=5
  Outcome: openalex_source: HTTPError: HTTP Error 429: Too Many Requests. Raw response: `openalex_source.response`.

- 2026-10-12 `crossref`: https://api.crossref.org/works?query=Brownian+sheet+zero+set+projection+Marstrand&rows=30
  Outcome: crossref: HTTP 200, 159251 bytes. Raw response: `crossref.response`.

- 2026-10-12 `semantic_scholar`: https://api.semanticscholar.org/graph/v1/paper/search?query=Brownian+sheet+projection&limit=40&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract
  Outcome: semantic_scholar: HTTPError: HTTP Error 429: . Raw response: `semantic_scholar.response`.

- 2026-10-12 `github`: https://api.github.com/search/repositories?q=Brownian+sheet+projection&per_page=30
  Outcome: github: HTTP 200, 55 bytes. Raw response: `github.response`.

- 2026-10-12 `resolution_pdf`: https://arxiv.org/pdf/2405.20019v2
  Outcome: HTTP 200, 324474 bytes.

- 2026-10-12 `resolution_publisher`: https://link.springer.com/article/10.1007/s10959-024-01399-1
  Outcome: HTTP 200, 3038 bytes.

- 2026-10-12 `crossref_resolution`: https://api.crossref.org/works/10.1007/s10959-024-01399-1
  Outcome: HTTP 200, 9789 bytes.

- 2026-10-12 `openalex_retry_source`: https://api.openalex.org/works?search=Slices+of+Brownian+Sheet&per-page=5
  Outcome: HTTPError: HTTP Error 429: Too Many Requests.

- 2026-10-12 `openalex_resolution`: https://api.openalex.org/works/https://doi.org/10.1007/s10959-024-01399-1
  Outcome: HTTPError: HTTP Error 429: Too Many Requests.

- 2026-10-12 `semantic_resolution`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2405.20019?fields=title,authors,year,externalIds,abstract
  Outcome: HTTPError: HTTP Error 429: .

- 2026-10-12 `semantic_source`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0510518?fields=title,externalIds,citations.title,citations.year,citations.externalIds
  Outcome: HTTP 200, 940 bytes.

- 2026-10-12 `journal_pdf`: https://link.springer.com/content/pdf/10.1007/s10959-024-01399-1.pdf
  Outcome: HTTP 200; 3038 bytes.

- 2026-10-12 `openalex_source_doi`: https://api.openalex.org/works/https://doi.org/10.1007/978-3-7643-8458-6_9
  Outcome: HTTPError: HTTP Error 429: Too Many Requests.

- 2026-10-12 `openalex_citing_source`: https://api.openalex.org/works?filter=cites%3Ahttps%3A%2F%2Fdoi.org%2F10.1007%2F978-3-7643-8458-6_9&per-page=100
  Outcome: HTTPError: HTTP Error 429: Too Many Requests.

- 2026-10-12 `crossref_source`: https://api.crossref.org/works/10.1007/978-3-7643-8458-6_9
  Outcome: HTTP 200; 12751 bytes.

## Related search hits (not used as solutions)

- Safari Mukeru, **The Zero Set of Fractional Brownian Motion Is a Salem Set**, Journal of Fourier Analysis and Applications; publication date [[2017, 6, 19]]; volume 24, pages/article 957-999, DOI https://doi.org/10.1007/s00041-017-9551-9. Related model or general projection theorem; not a source-matching resolution.
- Shengwen Gan, **A Marstrand projection theorem for lines**, Journal d'Analyse Mathématique; publication date [[2025, 1, 21]]; volume 155, pages/article 571-607, DOI https://doi.org/10.1007/s11854-025-0363-6. Related model or general projection theorem; not a source-matching resolution.
- Willem L. Fouché; Safari Mukeru, **On the Fourier structure of the zero set of fractional Brownian motion**, Statistics &amp; Probability Letters; publication date [[2013, 2]]; volume 83, pages/article 459-466, DOI https://doi.org/10.1016/j.spl.2012.10.015. Related model or general projection theorem; not a source-matching resolution.
- Antoine-Marie Bogso; Moustapha Dieye; Olivier Menoukeu Pamen, **Stochastic integration with respect to local time of the Brownian sheet and regularising properties of Brownian sheet paths**, Bernoulli; publication date [[2023, 11, 1]]; volume 29, pages/article 2627-2651, DOI https://doi.org/10.3150/22-bej1555. Related model or general projection theorem; not a source-matching resolution.

- arXiv also returned Enkelejd Hashorva and Yuliya Mishura, **Boundary Non-Crossings of Additive Wiener Fields**, arXiv:1402.2620v2; *Lithuanian Mathematical Journal* 54(3), 277–289 (2014). The projection in its abstract is an RKHS projection, not a zero-set projection; discarded.
- Semantic Scholar source citations additionally listed **Packing dimension of images of additive Lévy processes** (2013), DOI 10.1090/S0002-9947-2013-05970-3, and **Hausdorff dimension of limsup random fractals** (2013), DOI 10.1214/EJP.V18-2273. These metadata-only leads were not used.
