# Literature audit — F0136, 2026-10-11

## Status assessment

No exact solution has been verified. The directly relevant 2025 paper by Perrel and Sabot assumes (T′) in the planar transient case. Nonzero drift alone does not supply that hypothesis in the general parameter range in this audit. This is a lead and a conditional result, not SOLVED_IN_LITERATURE.

## Search ledger

All requests used Python urllib from the shell. Raw successful responses are retained in this folder. Exact URL, date, and success/error are in `search_log.json`. No built-in web search was used.

1. arXiv API, 2026-10-11: `all:"Dirichlet" AND (all:"ballistic" OR all:"ballisticity")`, newest first, max_results=80; HTTPS export endpoint. Successful, `arxiv.xml`. Mostly irrelevant PDE hits; relevant RWDE results inspected separately.
2. OpenAlex works search, 2026-10-11: `random walk Dirichlet environment ballisticity`, per-page=60. HTTP 429.
3. Crossref works search, 2026-10-11: `Dirichlet random environment ballisticity`, rows=40. Successful, `crossref.json`.
4. Semantic Scholar paper search, 2026-10-11: `Dirichlet random environment ballisticity`, limit=50, fields title,authors,year,externalIds,abstract,url. Successful, `semantic.json`. Crucially identified arXiv:2501.06767, missed by the first arXiv query.
5. GitHub repository search, 2026-10-11: `Dirichlet random walk ballisticity`. Successful, `github.json`, zero repository results. This is not evidence of mathematical openness.
6. OpenAlex works search, 2026-10-11: `Random walks in Dirichlet environment an overview`, per-page=5. HTTP 429.
7. arXiv API HTTP export endpoint, 2026-10-11: `all:"Dirichlet" AND all:"ballisticity"`, max_results=30. Successful, `arxiv_http.json` (XML response despite filename).
8. arXiv API, 2026-10-11: `all:"Dirichlet" AND (all:"2D" OR all:"two-dimensional" OR all:"dimension 2")`, newest first, max_results=60. Successful, `arxiv_planar.xml`.
9. OpenAlex source lookup by DOI, 2026-10-11: `https://api.openalex.org/works/https://doi.org/10.5802/afst.1542`. HTTP 429. Since the work identifier was unavailable, the requested cited-by works lookup could not be completed; the intended query was `works?filter=cites:<source work id>&per-page=100`. A citation search was performed with Semantic Scholar instead. OpenAlex coverage remains incomplete.
10. Semantic Scholar source citations, 2026-10-11: `/graph/v1/paper/ARXIV:1601.08219/citations?fields=title,year,authors,externalIds,abstract&limit=100`. Successful, `semantic_citations.json`.
11. Full-text PDFs from arXiv: 1601.08219, 0801.2875, 1310.6281, 2404.06502, and 2501.06767. Saved PDFs and extracted text with explicit PDF page markers.
12. arXiv title search, 2026-10-11: `ti:"Dirichlet" AND ti:"environment"`, newest first, max_results=100. Successful, `arxiv_titles.xml`; retrieves the 2025 planar paper and the 2026 time-dependent paper, plus earlier results. No retrieved later static planar theorem removes (T′).
13. Full-text PDF arXiv:2107.00113, 2026-10-11. Successful, saved with extracted text; Theorem 1, PDF p.4, explicitly assumes (P)ᶩ_M with M>35, in addition to its local ellipticity conditions. Theorem 2 also explicitly assumes a polynomial spatial ballisticity condition. Thus this paper does not remove the global gap in F0136.

## Source and relevant references

* Christophe Sabot and Laurent Tournier, **Random walks in Dirichlet environment: an overview**, arXiv:1601.08219 (2016); Annales de la Faculté des Sciences de Toulouse, DOI 10.5802/afst.1542. Primary source, stored as `source_pdf.pdf`. The requested conjecture concerns d=2, all strictly positive parameters, nonzero dα, and κ=2Σα−max opposite-direction sum greater than one. Directional transience is already known; ballisticity is the missing assertion.
* Adrien Perrel and Christophe Sabot, **Invariant measure for the process viewed from the particle for 2D random walks in Dirichlet environment**, arXiv:2501.06767v1, 12 January 2025. Direct planar lead. Abstract explicitly says: “Besides, if the walk is directional transient and under condition (T′), we prove that there exists such an invariant probability measure if the trapping parameter verifies κ > 1 or after acceleration of the process by a local function of the environment.” This is transcribed with PDF typography normalized. It has the extra (T′) hypothesis. Its introduction, PDF p.2, says (T′) for dα≠0 is widely conjectured, with a known sufficient condition |α₁−α₃|+|α₂−α₄|>1.
* Élodie Bouchet, Alejandro F. Ramírez and Christophe Sabot, **Sharp ellipticity conditions for ballistic behavior of random walks in random environment**, arXiv:1310.6281v3; Bernoulli 22(2) (2016), 969–994, DOI 10.3150/14-BEJ683. Supplies conditional ballisticity and planar parameter regions, not all nonzero drifts with κ>1. Its PDF was fetched to check the exact conditions.
* Laurent Tournier, **Integrability of exit times and ballisticity for random walks in Dirichlet environment**, arXiv:0801.2875; Electronic Journal of Probability 14 (2009), 431–451, DOI 10.1214/EJP.v14-609. Finite directed graph Green-function/exit-time integrability criterion and a refined sufficient ballisticity condition. Does not equate local integrability with planar ballisticity. Semantic Scholar incorrectly associated this title with DOI 10.1214/09-AIHP344; Crossref identifies that DOI as Sabot–Tournier's different paper “Reversed Dirichlet environment and directional transience of random walks in Dirichlet environment”. The Crossref title/DOI match is used here.
* Adrien Perrel, **Limit theorem for subdiffusive random walk in Dirichlet random environment in dimension d≥3**, arXiv:2404.06502 (2024). Restricted to d≥3 and assumes (T) for the fluctuation theorem. Does not settle F0136.
* Rémy Poudevigne–Auboiron, **Limit theorem for sub-ballistic random walks in Dirichlet environment in dimension d≥3**, arXiv:1909.03866; Electronic Journal of Probability (2023), DOI 10.1214/23-EJP945. Wrong dimension and κ regime for the target.
* Daniel J. Slonim, **Random Walks in Dirichlet Random Environments on Z with Bounded Jumps**, arXiv:2104.14950; Ann. Inst. Henri Poincaré Probab. Statist. (2024), DOI 10.1214/22-aihp1352. One-dimensional model with separate finite/infinite trapping parameters. A methodological warning against extrapolating finite traps to global speed, not a result for Z².
* Guillaume Barraquand, Alexander K. Hartmann and Pierre Le Doussal, **Random walks in Dirichlet random environment in dimension d+1**, arXiv:2607.20279 (2026), surfaced in Semantic Scholar. Its abstract concerns a time-dependent environment and numerical KPZ comparisons. Different objects; not a solution to static i.i.d. nearest-neighbour RWDE on Z².
* Dongjian Qian and Yang Xiao, **Speed of Random Walks in Dirichlet Environment on a Galton-Watson Tree**, arXiv:2405.11845 (2024). The graph is a random tree, not Z². Its velocity criterion does not resolve this question.
* Alejandro F. Ramírez and Rodrigo Ribeiro, **Computable criteria for ballisticity of random walks in elliptic random environment**, arXiv:2107.00113; Electronic Journal of Probability 27 (2022), DOI 10.1214/22-EJP856. Found among source citations. General elliptic-environment criteria, not a stated unconditional classification of planar RWDE; full text fetched to check the extra hypotheses.

Full-text check of the last reference: Theorem 1 (PDF p.4) gives ballisticity on Z² assuming (E)₀, (X)₁, and (P)ᶩ_M for M>35. Theorem 2 replaces the local condition but retains (P)ᶩ_M. Directional transience alone is not its stated global hypothesis. The article's introduction also distinguishes finite exit-time criteria from spatial ballisticity criteria, consistent with the obstruction recorded in ATTEMPT.md.

## Read-only research-brain and earlier-attempt checks

Executed the requested `math_recall.py` on “Dirichlet random environment ballisticity Sabot Tournier dimension two”, and `brain.py recall` on “Dirichlet random environment ballisticity” and “Dirichlet random environment mistakes”. No applicable exact resolution was supplied. The card claiming refutation of a more general ellipticity criterion is a warning, not a counterexample within the Dirichlet model.

Searched intake ledger directories and the codex_pool_2026_10_10 for F0136. The initial literal wildcard directory argument failed in PowerShell; repeated with enumerated directories. Searched `origin/master` using read-only git commands; C0041 is the related general uniformly elliptic directional-transience problem. Earlier papers/reports are not treated as proof of this problem.

No statement here claims exhaustive coverage through the date: APIs have incomplete indexes, and OpenAlex was rate-limited. SOLVED_IN_LITERATURE is deliberately not assigned.

During the attempt, additionally ran `math_recall.py` on “Perrel Sabot Dirichlet invariant measure planar T prime”; the complete output is saved as `brain_followup.txt`. Hints in that output were not treated as verified mathematical statements.

## Exact primary-source confirmation

Sabot–Tournier, arXiv:1601.08219v1, PDF p.11, immediately following Proposition 2, states word for word:

> As we will see below (Theorem 5), the assumption κ ≤ 1 is sharp in dimension d ≥ 3, and this is also conjectured to be true in dimension 2.

The definition on that page, equation (4.3), is κ=2Σᵢαᵢ−max₁≤ᵢ≤d(αᵢ+αᵢ₊d). Theorem 5(i), PDF p.16, says:

> Assume d ≥ 3 and dα ≠ 0. Then if κ > 1, there exists v ∈ Rᵈ \ {0} such that limₙ→∞ Xₙ/n = v.

The hypothesis d≥3 is explicit. Theorem 1, PDF p.12, provides directional transience and the asymptotic direction, as in the problem intake. Remark 7, PDF p.17, explains that the invariant-measure proof uses bounded-L² unit flows and explicitly leaves d=2 unresolved.

Theorem 6, PDF p.18, states (mathematical symbols laid out inline; wording preserved):

> Consider the RWDE with parameters (αᵢ)ᵢ₌₁,…,₂d in dimension d ≥ 2. Assume that there exist ℓ such that dα·ℓ > 0. Consider the renewal times (τₖ)ₖ≥₁ in the direction ℓ. Assume that (T)γ is satisfied for some γ ∈ (0, 1). Then E₀⁽α⁾[(τ₁)ˢ] < ∞ if and only if s < κ.

This gives ballisticity for κ>1 **with the additional (T)γ hypothesis**; it is not a solution of the question with only nonzero drift. Theorem 7, also p.18, supplies Kalikow's condition and (T)₁ under Σᵢ|αᵢ−αᵢ₊d|>1. This supplies the special case detailed in ATTEMPT.md.

## Exact 2025 theorem and hypothesis mismatch

Perrel–Sabot, arXiv:2501.06767v1, Theorem 2.3, PDF p.8, states:

> Under the hypothesis that the random walk in Dirichlet environment P on Z² satisfies the condition (T′) (and in particular that dα ≠ 0), and that κ > 1, there exists an invariant probability measure Q from the point of view of the particle which is absolutely continuous with respect to P. Moreover, dQ/dP ∈ Lᵖ for every p < κ, where κ is the parameter introduced in Theorem 1.2.

Line-by-line comparison: (1) the lattice Z² and Dirichlet environment match; (2) κ>1 matches; (3) (T′) is extra, and p.7 expressly calls its equivalence to directional transience conjectural; (4) the stated conclusion is an invariant probability, rather than the exact nonzero-velocity assertion. No hypothesis-free planar solution is claimed. This is a relevant advance in the invariant-measure method.

**Typographical warning checked against the PDF:** the introduction on p.2 of 2501.06767 writes “2Σα−min(α₁+α₃,α₂+α₄)”. Theorem 1.2 on p.5 instead correctly defines κ=minⱼ{2Σα−(αⱼ+αⱼ₊d)}, which equals 2Σα−maxⱼ(αⱼ+αⱼ₊d). Theorem 2.3 expressly refers to the latter definition. The p.2 expression must not be substituted into this problem.

The Semantic Scholar source-citation response contains 30 entries, including the 2025 planar paper, the 2024 fluctuation paper, 2021 computable elliptic ballisticity criteria, and several different models. No title/abstract in that response states a proof of the unconditional planar claim. The broad arXiv query and source citations complement one another; neither alone is treated as exhaustive.

## Additional attempt: criterion source and gap-focused recall

2026-10-11: reread the stored full text of Tournier, arXiv:0801.2875, specifically to check the definition of Kalikow's auxiliary walk and its condition. Its extraction splits “Kalikow” into “Kalik / o / w”; an initial literal text search therefore missed the occurrences. The page containing the actual auxiliary definition was extracted separately into `kalikow_definition_excerpt.txt`.

2026-10-11: fetched Nathanael Enriquez and Christophe Sabot, **Random walks in a Dirichlet environment**, arXiv:math/0503713; Electronic Journal of Probability 11 (2006), DOI 10.1214/EJP.v11-350. Stored as `math0503713.pdf` and `.txt`. Purpose: independently check the Green-function occupation weighting for Kalikow's auxiliary walk. Exact request and result are in `second_attempt_search_log.json`. This is a neighbouring-method source, not a later solution of F0136.

2026-10-11: executed the two gap-focused math-store queries listed in SECOND_ATTEMPT.md. Results are saved whole in `brain_gap_recall.txt` and `brain_kalikow_recall.txt`. They yielded no applicable theorem for the missing planar regeneration estimate; symmetric Hunt processes and Dirichlet forms were not substituted for this nonreversible RWDE.

The additional attempt's explicit failure of Kalikow's condition is derived in SECOND_ATTEMPT.md. No paper is asserted to have settled F0136 and no novelty claim is made for that auxiliary obstruction.

The finite-domain auxiliary transition formula was verified directly on Tournier's arXiv:0801.2875 PDF p.14, Section 4. Enriquez–Sabot, arXiv:math/0503713, Section 4, PDF pp.4–5, uses connected domains and the same occupation-weighted construction. The output from Tournier's page is preserved in `kalikow_definition_excerpt.txt` with the original extraction's word fragmentation.

A further relevant lead emerged on rereading Tournier's **2008 preprint version**, arXiv:0801.2875v1, PDF p.16, “Concluding remarks and computer simulations”: it reports apparent sublinear displacement for parameters (alpha_1,alpha_-1,alpha_2,alpha_-2)=(0.5,0.2,0.1,0.1), with a fitted exponent near 0.9 over the tested finite times. In this problem's indexing these are (0.5,0.1,0.2,0.1), with A=0.9 and kappa=1.1. The preprint explicitly says the intermediate regime was not proved. This is historical numerical evidence and a counterexample-search lead, not a theorem resolving F0136. The additional attempt ran a small, separately seeded finite-time probe of that exact parameter vector; results are in `walk_probe.json`.
