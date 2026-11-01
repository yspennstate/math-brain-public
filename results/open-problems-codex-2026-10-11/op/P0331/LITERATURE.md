# Literature audit — P0331

Search date: 2026-10-12. No paper inspected here proves the full question as posed. Verdict is PARTIAL, not SOLVED_IN_LITERATURE. This is a bounded search, with important coverage failures stated below.

## Search record

Every HTTP request, query string, date, success/failure, and response size is recorded verbatim in `search_log.jsonl`; a readable list is in `SEARCHES.md`. Successful raw responses remain in this folder. The services queried were:

* arXiv export API: Coulomb plus Debye/Poisson (30 newest); Coulomb gas plus local laws/high temperature/Poissonian (80 newest); Debye plus jellium/sharpness/Serfaty (30); title Poisson plus Coulomb/Lambert (25). The last query found the important intermediate-temperature paper missed by the earlier phrase query.
* OpenAlex works search: `Coulomb Debye Poisson`; source title lookup twice; source lookup by DOI `10.48550/arXiv.2407.21194`. All returned HTTP 429. A citing-works request was also attempted with the **unverified guessed ID W4401113170** and returned 429. This ID was not established to denote the source and that request supplies no evidence whatsoever. The source's citing works could not be reliably enumerated.
* Crossref works: `Coulomb gas Debye Poisson`, 30 items. Mostly classical screening results and physical applications; the relevant recent form-factor paper is listed below.
* Semantic Scholar: `Coulomb Debye Poisson` with abstracts, and ARXIV:2407.21194 with citations. Both returned 429. No negative inference is possible.
* GitHub repositories: `Coulomb Debye`; the API returned total_count=0. This is only repository search, not an exhaustive code or paper search.
* Direct PDF fetches: source arXiv:2407.21194; Thoma arXiv:2501.02733; Rosenzweig arXiv:2608.24863; Padilla-Garza–Peilen–Thoma arXiv:2507.08198; Lambert arXiv:1912.10261. Each successful PDF and its extracted text are saved.

Read-only local checks: math_recall queried `Coulomb gas Poisson high temperature Debye`; brain recall queried `Coulomb Debye scale mistakes`. The latter unexpectedly reported an automatic cache refresh/background process; no further brain.py calls were made. The returned cards did not provide a relevant proof. The user's supplied prior attempt is a screened-structure-factor heuristic, not a nonlinear Coulomb theorem. Searches for P0331/op-p0331/Debye in accessible intake JSONL and pool paths found the current campaign formulation but no stronger proof. The recorded-answers checkout was accessed only via `git ls-tree origin/master`, including a P0331-filtered query which returned no paths; its working tree was not modified.

## Verified source

Final local follow-up: read the full prior-attempt math-store card `claim_0ffc540cf432216cce64d4e5ad7a44caf83962cdc061a29a2b5fcf1245c7738e` with `math_recall.py --id`. It explicitly labels its structure-factor calculation as only a linear-response diagnostic and leaves the nonlinear energy estimate and d=2 correction unjustified. A full read-only `git ls-tree -r --name-only origin/master` captured through Python and filtered case-insensitively for P0331/Debye returned zero matching paths, exit 0.

Sylvia Serfaty, *Lectures on Coulomb and Riesz gases*, arXiv:2407.21194 (2024), https://arxiv.org/abs/2407.21194. Downloaded PDF has 303 pages. Equations (8.0.1)–(8.0.2) are on PDF page 163; conjecture on PDF page 164; actual Theorem 8.2 and estimate (8.3.3) on PDF pages 169–170; chi definition (5.2.27) on PDF page 108; local energy definition (7.1.23) on PDF page 148.

Verbatim conjecture:

> We conjecture that this lengthscale is sharp and that (8.0.1) is optimal, in particular that local laws do not hold below ρβ because particle numbers behave in a Poissonian way below that scale.

The exact scale and additional hypotheses are detailed in ATTEMPT.md Section 1. The conjecture does not formally quantify what Poissonian means. Equation (8.3.3) has an added C0 particle-count term. Poisson local statistics alone are not a proof of sharpness of either energy estimate.

## Relevant papers and their limits

1. Scott Armstrong and Sylvia Serfaty, *Local laws and rigidity for Coulomb gases at any temperature*, Annals of Probability **49**(1), 46–121 (2021). Exact reference from the source bibliography [AS21]. Establishes the local laws; it predates the conjecture and is not a scale-sharpness proof.

2. David Padilla-Garza, Luke Peilen, Eric Thoma, *Poisson Statistics for Coulomb Gases at Intermediate Temperature Regimes*, arXiv:2507.08198v2, posted 20 August 2025 (PDF dated 21 August), https://arxiv.org/abs/2507.08198. This is the strongest post-source lead found. The abstract explicitly identifies beta N ->infinity and beta sqrt(N) log N ->0. Theorem 1, PDF page 3, verbatim with mathematical typesetting restored:

> Theorem 1. Assume (Temp) and (Grow), and let z ∈ int(supp(µV)). Then the local point process Qz,N under PN,β converges weakly to a Poisson point process with intensity µV(z)Leb for the Lebesgue measure Leb on Rd.

The surrounding standing assumptions are d=2, theta_*=inf N beta_N>0, and (Conf): integrable confinement tails, V in C2, positive Delta V near the droplet, and V-log|x|->infinity. (Grow) imposes polynomial lower growth and bounded-above Delta V; (Temp) is beta_N=o(1/(sqrt N log N)). The printed Theorem 1 omits beta_N N ->infinity, although its identification mu_theta->mu_V uses this condition. Our application imposes it explicitly rather than claiming the larger printed scope. Proposition 3.7, PDF pages 20–21, estimates k-point correlations with k fixed. This does not establish uniform Poisson convergence for all growing windows below rho_beta and proves no lower bound contradicting the localized electric-energy estimate. It is restricted to d=2 and a temperature subregime. ATTEMPT.md Section 5 proves a limited diagonal-window consequence of this theorem. Thus this is a lead/special case, not SOLVED_IN_LITERATURE.

3. Eric Thoma, *A maximum principle for the Coulomb gas: microscopic density bounds, confinement estimates, and high temperature limits*, arXiv:2501.02733v1, 6 January 2025, https://arxiv.org/abs/2501.02733. Theorem 4, PDF page 7, is a d=2 theorem: for beta_N->0 the limiting recentered microscopic process is homogeneous **mixed** Poisson, with deterministic intensity only under an additional density-concentration criterion. Standing hypotheses include inf beta_N N^{2/d}>2 and conditions (A2)–(A7) on the potential/droplet. It neither gives the claimed crossover for all dimensions nor disproves the energy bound below that crossover. The abstract's broad phrasing must not be mistaken for an all-dimensional pure-Poisson theorem.

4. Gaultier Lambert, *Poisson statistics for Gibbs measures at high temperature*, arXiv:1912.10261v1, 21 December 2019, https://arxiv.org/abs/1912.10261; cited as [Lam21b] by the intermediate-temperature paper. Its abstract treats beta N->gamma>=0 for general interacting gases, including Coulomb/Riesz applications. Its temperature normalization must be translated before comparing with Serfaty's dimension-dependent blown-up beta. It predates the source, treats the mean-field high-temperature regime, and does not prove local-energy sharpness.

5. Matthew Rosenzweig, *Uniform logarithmic Sobolev inequalities for the 2D Coulomb gas at the diffusive temperature scale*, arXiv:2608.24863v1, 25 August 2026, https://arxiv.org/abs/2608.24863. The Gaussian planar ensemble has pair exponent beta/N, with fixed beta. The abstract asserts an N-uniform logarithmic Sobolev inequality and explicitly asserts no uniformity as beta->0 or infinity. This is a functional inequality at a particular mean-field scaling, not a theorem about sharpness of the Debye local-energy scale.

6. Matteo Massaro and Adolfo del Campo, *Spatial form factor for point patterns: Poisson point process, Coulomb gas, and vortex statistics*, Physical Review Research **7**, 023107 (2025), DOI 10.1103/PhysRevResearch.7.023107; arXiv:2410.04816v3 was returned by the Poisson query. Crossref metadata is preserved in `crossref.raw`. This is a form-factor/model-comparison lead, not verified as a rigorous solution of the source conjecture; its full text was not inspected. No conclusion rests on it.

Classical Crossref screening hits include *Debye screening for jellium and other Coulomb systems*, DOI 10.1007/BF01208264; *A rigorous approach to Debye screening in dilute classical Coulomb systems*, DOI 10.1007/BF01614227; and *Debye screening for two-dimensional Coulomb systems at high temperatures*, DOI 10.1007/BF01009952. These are older screening works, not a verified solution of this particular canonical local-energy sharpness question. Their full texts were not fetched.

## Status conclusion

Second-attempt math-store queries, 2026-10-12: `Coulomb localized electric energy lower bound Poisson tails Debye screening Onsager`; `relative entropy superadditivity stationary point processes Poisson Coulomb torus Onsager`; `Brydges Federbush Debye Huckel jellium free energy high temperature`. These are read-only hint searches, not verified external literature solutions. The first returned only the old heuristic and unrelated results; the second returned basic PPP/relative-entropy cards (including claim_9a0024c47f80d6e08a113cbde08d41df), not a model-specific localization theorem. Source Lemma 7.8, PDF page 150, equations (7.1.26), (7.1.36) and (7.1.38), was reread for the actual localized-energy calculation. New proofs and precise model distinctions are in SECOND_ATTEMPT.md. No new web search was needed for the elementary entropy/heat-kernel proofs; no stronger literature solution is claimed.

The downloaded post-source Poisson papers supply real progress on microscopic statistics, but the mismatch in objects, growing-window quantifiers, dimensions, and the missing electric-energy lower bound rules out declaring SOLVED_IN_LITERATURE. Rate-limited citation services make the present audit incomplete; it is not a certificate that no solution exists anywhere.

The second attempt's named Brydges/Federbush/Debye–Hückel math-store query completed with unrelated Potts and Riesz cards. No matching finite-volume free-energy theorem was found through that recall. The conditional reduction in SECOND_ATTEMPT.md Section 7 is proved as an implication, with its free-energy premise left unproved.
