# D0024 literature and source audit — 2026-10-11

## Verdict and source

No SOLVED_IN_LITERATURE designation is made. The source's literal finite-range-kernel question is false without an irreducibility assumption; ATTEMPT.md gives complete counterexamples. A positive result for the nearest-neighbor one-dimensional model is proved in the 2020 paper below, but is not a theorem for the source's full standing scope.

Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, arXiv:math/9906194v1, submitted 28 June 1999 (manuscript marked 1998). URL https://arxiv.org/pdf/math/9906194. Downloaded 2026-10-11, HTTP 200, 164,945 bytes; saved source.pdf and source.txt.

Verbatim Problem 3, Section 4, PDF/printed p.9 (mathematical notation typeset here):

> Problem 3. An interesting open problem for the disordered ZRP concerns the weak convergence of the process: Fix the rates α, and take the initial distribution of η(0) spatially ergodic with density ρ. Does the distribution of η(t) converge weakly, as t → ∞, to one of the equilibria νᵅ_φ? If ρ > ρ* in the phase transition case, does η(t) converge weakly to the equilibrium with density ρ*? For the standard ZRP results of this type were proved by Andjel et al. (1985).

Hypotheses: pp.3–4 describe a bounded monotone rate r, an arbitrary finite-range probability distribution p on Z^d, and an ergodic [c,1]-valued random environment with c>0 its marginal essential infimum. They do not require nearest-neighbor jumps or connectivity. Assumption (A.1) on p.6 is in the hypotheses of Theorem 1. Problem 3 does not invoke it. Q being iid, d=1 and p(1)=1 are assumptions of Theorem 2, not the general model. The source's 1985 reference is Andjel, Cocozza-Thivent and Roussignol, *Quelques compléments sur le processus de misanthropes et le processus “zéro-range”*, Ann. Inst. H. Poincaré Probab. Statist. 21 (1985), 363–382; the intake's mention of Ferrari–Guiol–Landim is not the source's exact reference.

## Verified major lead: nearest-neighbor convergence

Christophe Bahadoran, Thomas Mountford, Krishnamurthi Ravishankar, Ellen Saada, *Quenched convergence and strong local equilibrium for asymmetric zero-range process with site disorder*, Probability Theory and Related Fields 176 (2020), 149–202. DOI 10.1007/s00440-019-00916-2. arXiv:1804.06148v1. Fetched https://arxiv.org/pdf/1804.06148 on 2026-10-11, HTTP 200, 596,751 bytes; saved quenched_1804.06148.pdf and .txt. Crossref independently returned the title and DOI.

Theorem 2.5, PDF/printed p.18, verbatim words with the displayed formula typeset:

> Theorem 2.5 Let η₀ ∈ X be such that, for some ρ > 0,
>
> lim_{n→+∞} (1/n) ∑_{x=−n}^0 η₀(x) = ρ. (43)
>
> Then ηᵅ_t converges in distribution as t → +∞ to μᵅ,ρ∧ρc.

Scope checks, line by line:

1. Section 2.1, PDF p.7, explicitly sets p supported on {-1,1}, p(1)>1/2 and d=1. This excludes both p(2)=1 counterexamples and arbitrary-dimensional kernels permitted by the old source.
2. The bounded monotone g on p.7 agrees with source r after dividing by r(∞) and rescaling time. This part of the objects matches.
3. Environment averaging and macroscopically dense defects are Assumptions 2.1–2.2, pp.9–10. Example 2.1 and the following remark, p.10, say these hold for almost every spatially ergodic environment. For a finite critical density, α(x)>c at every site almost surely, and the fixed-site sequence x_N=0 satisfies the typicality condition of Definition 2.1, p.15.
4. For a finite-density spatially ergodic initial law, Birkhoff gives the displayed left-density hypothesis almost surely. Bounded convergence integrates deterministic-start convergence over the initial law. This is an implication we spell out in ATTEMPT.md, not a new printed theorem for the full source model.
5. The equilibrium parametrization μᵅ,ρ uses the inverse averaged one-site mean, matching source νᵅ_{f(ρ)} (with rate normalization accounted for); its critical member matches νᵅ_{r(∞)c}.
6. Thus the paper resolves the nearest-neighbor specialization in both regimes. It does not state or prove the old source's claim for arbitrary finite-range kernels. Do not expand its quantifiers silently.

The proof of Theorem 2.5 is in Section 7, PDF pp.60–63. This is genuinely an unscaled large-time convergence theorem, not merely a hydrodynamic theorem. The old intake's suspicion that the paper only gave a scaling result is corrected.

## Other relevant papers fetched

* Enrique D. Andjel, Pablo A. Ferrari, Hervé Guiol, Claudio Landim, *Convergence to the maximal invariant measure for a zero-range process with random rates*, Stochastic Processes and their Applications 90 (2000), 67–81; arXiv:math/9911205v2. Downloaded PDF as search_math_9911205.txt (binary PDF despite suffix); extraction paper_math_9911205.txt. Totally asymmetric nearest-neighbor, constant nonzero occupation rate. Abstract gives convergence above critical density and classification of invariant measures. Restricted model, not full source solution.
* Pablo A. Ferrari and Valentin V. Sisko, *Escape of mass in zero-range processes with random rates*, IMS Lecture Notes–Monograph Series 55 (2007), 108–120, DOI 10.1214/074921707000000300; arXiv:math/0609469v2. Downloaded binary search_math_0609469.txt, extraction paper_math_0609469.txt. General-dimensional iid disorder; upper domination of weak limits under a growth condition, and convergence when the initial law stochastically dominates the critical equilibrium. Arbitrary spatial ergodicity alone does not give this domination.
* Bahadoran, Mountford, Ravishankar, Saada, *Supercriticality conditions for asymmetric zero-range process with sitewise disorder*, Brazilian Journal of Probability and Statistics 29(2) (2015), 313–335; arXiv:1411.4318v2. Binary search_1411.4318.txt, extraction paper_1411.4318.txt. Theorem 2.3, PDF p.7, produces non-nearest-neighbor counterexamples from deterministic configurations satisfying a liminf density condition. The construction on p.23 places mass on a very sparse sequence of sites. This is not asserted to be a spatially ergodic initial law, so it is not counted as a printed resolution of THIS question. It confirms that nearest-neighbor restrictions in this literature matter.
* Bahadoran, Mountford, Ravishankar, Saada, *Supercritical behavior of asymmetric zero-range process with sitewise disorder*, Annales de l'Institut Henri Poincaré Probabilités et Statistiques 53(2) (2017), 766–801; arXiv:1411.4305v2. Binary search_1411.4305.txt, extraction paper_1411.4305.txt. Necessary/sufficient conditions in one-dimensional nearest-neighbor model with a weak convexity hypothesis; partial general-dimensional domination result. A lead/special case.
* Bahadoran, Mountford, Ravishankar, Saada, *Hydrodynamics in a condensation regime: The disordered asymmetric zero-range process*, Annals of Probability 48(1) (2020), 404–444, DOI 10.1214/19-AOP1365; arXiv:1801.01654. Located in arXiv and Crossref search and in references of the convergence paper. Hydrodynamic scaling result, not by itself unscaled convergence. Not separately read in full.
* Mustansir Barma and Kavita Jain, *Locating the minimum: Approach to equilibrium in a disordered, symmetric zero range process*, Pramana 58(2) (2002), 409–417; arXiv:cond-mat/0112113; Crossref DOI 10.1007/s12043-002-0024-y. Search lead only, different symmetric model; not used as a proof.

## Brain, intake, and repository audit (read only)

On 2026-10-11 ran math_recall.py on `disordered zero range convergence equilibrium Bahadoran Mountford`, brain.py recall on `disordered zero range process mistakes` and `disordered zero range convergence equilibrium`. No directly useful theorem card was returned. The mistakes recall warned about declaring a different-model theorem a resolution. No brain/store write command was run.

Searched probability_1000_intake_D_20260908/*.jsonl for D0024 and read the matched problems/attempts entries. They identify arXiv:1804.06148 but had not fetched its theorem, so their status is not a mathematical verdict. Also searched codex_pool_2026_10_10; no match returned. One attempted path probability_1000_intake_2026_10_10 did not exist; the subsequent directory listing located the actual intake paths.

Read via `git show origin/master:runs/R08/20260918T0030Z_d0024_resolution_d0025_plateau_screen_c7a4e2.md` in ~/math-open-problems. That report declares the problem resolved in the "source's intended one-dimensional" scope. The source's Section 2 does not have that restriction; the later theorem does. Therefore the report is reliable as a lead to the nearest-neighbor result but its full-source status declaration is not accepted. No repository working tree was changed.

## Search audit

All service queries, dates, URL parameters, HTTP outcomes, and saved response sizes are in search_log.jsonl; the complete readable listing is generated below in SEARCH_AUDIT.md. These were fetched through Python urllib/requests from the shell; no built-in web search was used.

OpenAlex search and source-identity requests returned HTTP 429, so its citation graph could not be retrieved. One diagnostic request used an arXiv identifier in the cites filter; OpenAlex requires its own work ID there. This is NOT counted as a successful or valid citing-works search. A source work ID was not recovered, so a valid OpenAlex cites:W... request remains unavailable. Semantic Scholar's ordinary search returned 429; the bulk endpoint succeeded. These access limitations preclude an exhaustive literature-status claim, but do not affect the explicit counterexamples.

## Complete service-query listing

# Complete HTTP query audit — 2026-10-11

Source PDF and convergence PDF were fetched separately; see LITERATURE.md. All queries below retain exact URLs.

- Service: arxiv; date: 2026-10-11
  - URL: http://export.arxiv.org/api/query?search_query=all%3A%22disordered%22%20AND%20all%3A%22zero-range%22&max_results=40
  - Outcome: 200; bytes: 67583

- Service: arxiv_https; date: 2026-10-11
  - URL: https://export.arxiv.org/api/query?search_query=all%3A%22zero-range%22%20AND%20all%3A%22convergence%22&max_results=40
  - Outcome: 200; bytes: 73578

- Service: openalex; date: 2026-10-11
  - URL: https://api.openalex.org/works?search=disordered%20zero%20range%20convergence%20equilibrium&per-page=30
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: openalex_source; date: 2026-10-11
  - URL: https://api.openalex.org/works?search=Recent%20results%20and%20open%20problems%20on%20the%20hydrodynamics%20of%20disordered%20asymmetric%20exclusion%20and%20zero-range%20processes&per-page=5
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: crossref; date: 2026-10-11
  - URL: https://api.crossref.org/works?query=disordered%20zero%20range%20convergence%20equilibrium&rows=30
  - Outcome: 200; bytes: 238411

- Service: semantic; date: 2026-10-11
  - URL: https://api.semanticscholar.org/graph/v1/paper/search?query=disordered%20zero%20range%20convergence&limit=30&fields=title,authors,year,externalIds,url,abstract
  - Outcome: HTTP Error 429: ; bytes: not saved

- Service: github; date: 2026-10-11
  - URL: https://api.github.com/search/repositories?q=disordered%20zero%20range&per_page=20
  - Outcome: 200; bytes: 17645

- Service: openalex_retry; date: 2026-10-11
  - URL: https://api.openalex.org/works?search=quenched%20convergence%20zero-range&per-page=10
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: semantic_bulk; date: 2026-10-11
  - URL: https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=disordered%20zero%20range&fields=title,authors,year,externalIds,url
  - Outcome: 200; bytes: 586922

- Service: openalex_source_retry; date: 2026-10-11
  - URL: https://api.openalex.org/works?filter=title.search:Recent%20Results%20and%20Open%20Problems%20on%20the%20Hydrodynamics&per-page=5
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: math_9911205; date: 2026-10-11
  - URL: https://arxiv.org/pdf/math/9911205
  - Outcome: 200; bytes: 176364

- Service: math_0609469; date: 2026-10-11
  - URL: https://arxiv.org/pdf/math/0609469
  - Outcome: 200; bytes: 216248

- Service: 1411.4305; date: 2026-10-11
  - URL: https://arxiv.org/pdf/1411.4305
  - Outcome: 200; bytes: 520962

- Service: 1411.4318; date: 2026-10-11
  - URL: https://arxiv.org/pdf/1411.4318
  - Outcome: 200; bytes: 268511

- Service: crossref_source; date: 2026-10-11
  - URL: https://api.crossref.org/works?query.title=Recent%20results%20and%20open%20problems%20on%20the%20hydrodynamics%20of%20disordered%20asymmetric%20exclusion%20and%20zero-range%20processes&rows=5
  - Outcome: 200; bytes: 45034

- Service: openalex_citations_attempt; date: 2026-10-11
  - URL: https://api.openalex.org/works?filter=cites:arxiv:math/9906194&per-page=50
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: arxiv_metadata; date: 2026-10-11
  - URL: https://export.arxiv.org/api/query?id_list=math/9911205,math/0609469,1411.4305,1411.4318,1804.06148,1801.01654
  - Outcome: 200; bytes: 11283

- Service: semantic_source; date: 2026-10-11
  - URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/9906194?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds
  - Outcome: 200; bytes: 278

- Service: openalex_source_identifier; date: 2026-10-11
  - URL: https://api.openalex.org/works/arxiv:math/9906194
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved


Semantic Scholar bulk returned 1,000 of 3,429 hits (a bounded first-page search). Its direct source-record lookup returned the correct source title/arXiv ID with an empty citations array; this is API metadata, not evidence that the paper has no citations. Crossref title search did not recover a matching source DOI. OpenAlex work-ID resolution stayed blocked (429), including a diagnostic arXiv-ID route that is not a supported identifier lookup.
