# P0323 literature check ? 2026-10-12

## Verified source
Jeanne Boursier, *Decay of correlations and thermodynamic limit for the circular Riesz gas*, arXiv:2209.00396v4, 19 July 2023 (downloaded from https://arxiv.org/pdf/2209.00396).
Theorem 3, PDF page 4: s in (0,1) union (1,infinity), beta>0 from (1.4); translation-invariant point-process limit and convergence of expectations of every bounded Borel local test function. This is stronger than mere vague weak convergence.
Section 1.3, PDF page 5: ?The first step in that direction could be to establish the Dubroshin-Landford-Ruelle (DLR) equations for the Riesz_s,beta process as was done for the Sine_beta process in [DHLM21].? (Subscripts rendered in plain text.) No explicit specification is stated there. Equation (1.3) sums over i != j, so the unordered-pair inverse temperature is 2 beta.

## Leads, not solutions in print
- David Dereudre and Thibaut Vasseur, *Number-rigidity and ?-circular Riesz gas*, arXiv:2104.09408; Annals of Probability, DOI 10.1214/22-AOP1606. Search abstract: existence of a non-number-rigid circular thermodynamic limit for d-1<s<d; canonical DLR approach. Need check exact quantifier and ensemble conventions before identification with Boursier.
- Yan Ru Pei, *Uniform displacement bounds and Gibbs limits for periodic one-dimensional Riesz gases*, arXiv:2609.28503v1, 15 September 2026. Theorem 1.3, PDF page 3, canonical Gibbs equations for negative potential -|r|^a, 0<a<1. Different exponent/model; does not solve P0323. Saved PDF/text.
- David Dereudre, Adrien Hardy, Thomas Lebl?, Myl?ne Ma?da, *DLR equations and rigidity for the Sine-beta process*, Communications on Pure and Applied Mathematics 74 (2021), 172?222; arXiv:1809.03989. Log interaction, different model.
- Semantic Scholar source citations also include: *Gap metrics for stationary point processes and quantitative convexity of the free energy* (2025), arXiv:2509.08659; other titles in saved semantic.json concern fluctuations, trapped gases, or negative exponents. No exact solution identified in these titles/abstracts.

## Searches and access outcomes
All requests used Python requests, not built-in search. Full responses saved in this folder. The search scope is bounded; failed requests are not negative evidence.

- 2026-10-12: source: https://arxiv.org/pdf/2209.00396 ? HTTP 200; 

- 2026-10-12: arxiv: https://export.arxiv.org/api/query?search_query=all:%22Riesz%22+AND+all:%22DLR%22&max_results=30 ? HTTP 200; 

- 2026-10-12: openalex: https://api.openalex.org/works?search=Riesz%20DLR&per-page=30 ? HTTP 429; 

- 2026-10-12: openalex_source: https://api.openalex.org/works?search=Decay%20of%20correlations%20and%20thermodynamic%20limit%20for%20circular%20Riesz%20gas&per-page=5 ? HTTP 429; 

- 2026-10-12: crossref: https://api.crossref.org/works?query=Riesz%20DLR&rows=20 ? HTTP 200; 

- 2026-10-12: semantic: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2209.00396?fields=title,authors,year,citations.title,citations.year,citations.externalIds ? HTTP 200; 

- 2026-10-12: github: https://api.github.com/search/repositories?q=Riesz+DLR ? HTTP 200; 

- 2026-10-12: lead2609: https://arxiv.org/pdf/2609.28503 ? HTTP 200; 

- 2026-10-12: arxiv_recent: https://export.arxiv.org/api/query?search_query=all:%22Riesz%22+AND+(all:%22Gibbs%22+OR+all:%22circular%22)&sortBy=submittedDate&sortOrder=descending&max_results=50 ? HTTP 200; 

- 2026-10-12: crossref_precise: https://api.crossref.org/works?query.bibliographic=circular%20Riesz%20gas%20Gibbs%20DLR&rows=20 ? HTTP 200; 

- 2026-10-12: openalex_retry: https://api.openalex.org/works?search=circular%20Riesz%20gas&per_page=10 ? HTTP 429; 

- 2026-10-12: sine: https://arxiv.org/pdf/1809.03989 ? HTTP 200; 

- 2026-10-12: arxiv_candidate: https://arxiv.org/pdf/2104.09408 ? HTTP 200; 

- 2026-10-12: openalex_doi: https://api.openalex.org/works?filter=doi:https://doi.org/10.1214/22-AOP1606&per-page=1 ? HTTP 429; 

- 2026-10-12: dv_html: https://arxiv.org/html/2104.09408 ? HTTP 200; 

- 2026-10-12: dv_source: https://arxiv.org/src/2104.09408 ? HTTP 200; 

## Exact candidate theorem and scope audit
Dereudre?Vasseur, arXiv:2104.09408v1, PDF page 8, Theorem 1.8, says:

> Theorem 1.8. Let P^? be a ?-Circular Riesz gas, ? be a bounded Borel subset of R^d and f be a bounded measurable function. Then
> ? f(?) P^?(d?) = ?? [1/Z^?_?(?)] f(? ? ?_{?^c}) e^{-?(H(?)+M_?(?,?))} B_{?,N_?(?)}(d?) P^?(d?),
> with the normalisation constant
> Z^?_?(?) = ? e^{-?(H(?)+M_?(?,?))} B_{?,N_?(?)}(d?).

The text is transcribed verbatim with mathematical typography reconstructed from the PDF; saved PDF is authoritative. The theorem has the surrounding hypothesis d-1<s<d, so d=1 gives ONLY 0<s<1. Remark 1.9 explicitly conditions on both N_? and the exterior. Proposition 1.5 defines a circular Riesz gas as any subsequential periodic limit. Theorem 1.11 chooses a special subsequential limit, and Theorem 1.14 (PDF page 10) gives its grand-canonical DLR with a measurable compensator. Section 2.4.1, PDF page 31, constructs that special limit from the same periodic laws at fixed temperature.

This is a strong lead and likely already implies the long-range part after matching ensembles. It is not a solution-in-print of the whole P0323 range: it excludes s>1 and predates Boursier's limit. Our ATTEMPT.md supplies an independent canonical passage for both ranges. We do NOT assign SOLVED_IN_LITERATURE.

## Search correction and limitations
The Crossref title search for Boursier returned Dereudre?Vasseur as its first result rather than Boursier. Consequently the OpenAlex DOI lookup/citation attempt in search_log.json used DOI 10.1214/22-AOP1606 (Dereudre?Vasseur), NOT Boursier. All those OpenAlex requests returned 429 and cannot be treated as a valid Boursier citation search. The Boursier Semantic Scholar ARXIV:2209.00396 citation list did succeed. The OpenAlex source ID could not be resolved under the repeated 429 response. No negative bibliographic conclusion is drawn from its failure.

## Read-only brain and prior-work checks
- math_recall.py: query ?Boursier Riesz DLR?; then walked claim_b2d7742dc0f38b378d96a39cccfd6bf5a9b9853c1c78c3dac019e506b502a50b. Warning concerns conditional-law passage under weak convergence; checked independently. Our proof uses stronger local Borel convergence and uniform tail comparison.
- brain.py recall: ?Riesz gas DLR mistakes?; results mostly off-topic, no theorem relied upon.
- Intake directories: searched P0323 in JSONL/Markdown and inspected the three named JSONL filenames where present; found intake statement, not a complete prior proof.
- math-open-problems origin/master: read-only ls-tree search for P0323 paths returned no match; no working-tree mutation.

- 2026-10-12: semantic_search: https://api.semanticscholar.org/graph/v1/paper/search?query=circular%20Riesz%20DLR&limit=20&fields=title,year,authors,externalIds ? HTTP 429; 

- 2026-10-12: arxiv_boursier: https://export.arxiv.org/api/query?search_query=au:Boursier+AND+all:Riesz&max_results=20 ? HTTP 200; 

- 2026-10-12: github_circular: https://api.github.com/search/repositories?q=%22circular+Riesz%22 ? HTTP 200; 

- 2026-10-12: crossref_source: https://api.crossref.org/works?query.title=Decay%20of%20correlations%20and%20thermodynamic%20limit%20for%20the%20circular%20Riesz%20gas&rows=3 ? HTTP 200; 

- 2026-10-12: openalex_id_lookup: https://api.openalex.org/works?search=2209.00396&per-page=5 ? HTTP 429; 

- 2026-10-12: openalex_source_doi: https://api.openalex.org/works/https://doi.org/10.1214/22-aop1606 ? HTTP 429; 

- 2026-10-12: openalex_citations_attempt: https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/22-aop1606&per-page=100 ? HTTP 429; 

## Continuation: short-range equivalence-of-ensembles check

- Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, Journal of Mathematical Physics 63, 061101 (2022), arXiv:2202.09240. Retrieved review saved as lewin.pdf/lewin.txt. PDF page 17, equation (45) and Definition 15, give the ordinary short-range exterior-only DLR density. That page explicitly says canonical states are convex combinations of grand-canonical ones and cites Georgii (1976). PDF pages 31?32 discuss the Dereudre?Vasseur long-range DLR construction. This supports the distinction between canonical and exterior-only formulations; it does not literally identify Boursier's particular limit.
- Hans-Otto Georgii, *Canonical and grand canonical Gibbs states for continuum systems*, Communications in Mathematical Physics 48 (1976), 31?51, DOI 10.1007/BF01609410. Publisher abstract retrieved through the PDF URL (response is HTML, not a PDF): ?It is shown that for a large class of interactions any canonical Gibbs state satisfying a natural temperedness condition is a mixture of Gibbs states with appropriate activities, and vice versa.? This is a lead, not a verified application: full hypotheses/theorem numbers unavailable, and a mixture does not by itself identify a single activity.
- Georgii, *Large deviations and the equivalence of ensembles for gibbsian particle systems with superstable interaction*, Probability Theory and Related Fields 99 (1994), 171?195; *The equivalence of ensembles for classical systems of particles*, Journal of Statistical Physics 80 (1995), 1341?1378. References found in Lewin; not fetched or applied as theorem inputs.
- Source Boursier Appendix C, PDF page 58, Lemma C.1 includes short-range indexed-spacing concentration (C.2). Read as a possible density-law lead. Its proof is labelled a sketch in the source; no additional theorem is claimed from it in this attempt.
- Read-only math-store continuation query: ?canonical Gibbs measures equivalence ensembles Georgii Ruelle?. Retrieved generic cards, no applicable precise mixture theorem. No brain/store mutation.

The Numdam request https://archive.numdam.org/article/CMP_1976__48_1_31_0.pdf failed certificate hostname verification; it is an attempted guessed locator, not a retrieved source. Project Euclid guessed-locator responses gave an anti-bot HTML page. Publisher HTTP 200 must not be mistaken for successful full-PDF access.

- 2026-10-12: openalex_boursier_citations_attempt: https://api.openalex.org/works?filter=cites:https://arxiv.org/abs/2209.00396&per-page=100 -- HTTP 429; 

- 2026-10-12: arxiv_review: https://arxiv.org/pdf/2202.09240 -- HTTP 200; 

- 2026-10-12: crossref_georgii: https://api.crossref.org/works?query.bibliographic=Georgii%20canonical%20Gibbs%20measures%20continuum&rows=8 -- HTTP 200; 

- 2026-10-12: arxiv_equivalence: https://export.arxiv.org/api/query?search_query=all:%22canonical%20Gibbs%22&max_results=20 -- HTTP 200; 

- 2026-10-12: georgii_springer: https://link.springer.com/content/pdf/10.1007/BF01609410.pdf -- HTTP 200; 

- 2026-10-12: georgii_euclid: https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-48/issue-1/Canonical-and-grand-canonical-Gibbs-states-for-continuum-systems/cmp/1103899519.pdf -- HTTP 200; 

- 2026-10-12: georgii_pdf_encoded: https://link.springer.com/content/pdf/10.1007%2FBF01609410.pdf -- HTTP 200; 

- 2026-10-12: georgii_euclid_search: https://projecteuclid.org/search?term=Canonical%20and%20grand%20canonical%20Gibbs%20states -- HTTP 200; 

- 2026-10-12: georgii_project_old: https://projecteuclid.org/euclid.cmp/1103899519 -- HTTP 200; 
