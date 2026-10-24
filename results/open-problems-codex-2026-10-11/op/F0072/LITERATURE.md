# F0072 literature audit
Date: 2026-10-12. Bounded API search; no built-in web search used.

## Verified source
Yvan Velenik, *Localization and delocalization of random interfaces*, Probability Surveys **3** (2006), 112–169. DOI: 10.1214/154957806000000050. arXiv:math/0509695v3 (15 May 2006). Download: https://arxiv.org/pdf/math/0509695; local source_pdf.pdf and source.txt.

Open Problem 5, PDF pp. 22–23, printed pp. 133–134 (line-wrap hyphenation removed):
> Prove similar results (even without the proper constants) when V(x) is not uniformly strictly convex. In particular prove it for the continuous SOS model, that is, the continuous effective interface model with interaction V(x) = |x|. Note that the behavior should be different as soon as the tail of V changes. This has important impact on other related issues, as is discussed in Sections 4 and 6.

Section 1.1, PDF pp. 5–6: heights are real (the continuous model) or integer (the discrete model); V is even and convex with V(0)=0. The Hamiltonian includes a symmetric random-walk kernel p and inverse temperature beta; zero exterior boundary is the default. Uniform strict convexity requires C^2 and positive upper and lower bounds on V second derivative. Nearest-neighbour interactions are a special case of this framework.

Section 3.1, PDF pp. 19–20: positivity is imposed on Lambda_M inside Lambda_N. Section 3.2, PDF pp. 21–22: for d>=3 the main formulation first takes N to infinity and then M to infinity, with a supremum of expectations over ALL wall sites. The finite full-wall alternative restricts the supremum to a bulk box. In d=2, M=epsilon N, equation (20) has a supremum of individual probabilities over ALL sites in epsilon Lambda_N. Its Gaussian leading height is 2 sqrt(g_2) log N (not sqrt(4g_2 log N)); the PDF text extraction loses the distinction between the square root and following logarithm. The source uses epsilon for both the wall-box proportion and the error tolerance. The continuous SOS problem permits a different scale because its potential has different tails.

## Status conclusion
No fetched theorem was found that states and proves this same real-valued, one-hard-wall entropic-repulsion question with its full quantifiers. This is NOT proof of absence from the literature, and SOLVED_IN_LITERATURE is not assigned. Related results below are leads only. The new arguments in ATTEMPT.md must be judged on their proofs, rather than inferred from these papers.

## Relevant papers and scope checks
1. Paul Dario, *Upper bounds on the fluctuations for a class of degenerate ∇φ-interface models*, ALEA **21** (2024), DOI 10.30757/alea.v21-17; arXiv:2302.00547v3. Full PDF downloaded as degenerate_pdf.pdf. Assumption 1.1 and Theorem 1.2, PDF p. 2: twice continuously differentiable convex potential, with V second derivative comparable at infinity to |x|^(r-2), r>2; a mean-zero field on a torus; variance bounded by C log L in d=2 and C in d>=3. |x| does not meet that assumption, and the theorem does not impose a wall. On PDF p. 2 the paper explicitly mentions known free-field fluctuation bounds for |x| via Bricmont–Fontaine–Lebowitz and Brydges–Spencer. This is useful background, not a wall theorem.
2. Alexander Magazinov and Ron Peled, *Concentration inequalities for log-concave distributions with applications to random surface fluctuations*, Annals of Probability **50**(2) (2022), 735–770, DOI 10.1214/21-aop1545. Retrieved OpenAlex abstract: free fluctuation bounds on a discrete torus for convex potentials with second derivative vanishing only on a null set, including |x|^p for p>1. This does not include |x|, and does not prove the requested hard-wall statement.
3. Max Mihailescu and Ron Peled, *Entropic repulsion to the middle layer*, arXiv:2609.07578v1 (September 2026). PDF downloaded as middle_pdf.pdf. Corollary 1.9, PDF p. 6, proves absence of a Gibbs measure for nonnegative INTEGER-valued heights with general even convex W. The real-valued extension concerns bounded intervals between two walls and uniqueness, as explained on PDF p. 2. Neither result states the finite one-wall logarithmic heights for unbounded real-valued SOS.
4. Pietro Caputo, Fabio Martinelli and Fabio Lucio Toninelli, *Entropic repulsion in |∇φ|^p surfaces: a large deviation bound for all p>=1*, arXiv:1701.03327v1 (2017), DOI 10.1007/s40574-017-0137-x. The fetched arXiv abstract expressly says “random discrete surface” and low temperature. It gives a wall-probability large-deviation formula for that discrete model, not the continuous question.
5. Pietro Caputo, Eyal Lubetzky, Fabio Martinelli, Allan Sly and Fabio Lucio Toninelli, *Dynamics of (2+1)-dimensional SOS surfaces above a wall: Slow mixing induced by entropic repulsion*, Annals of Probability **42** (2014), DOI 10.1214/13-AOP836; arXiv:1205.6884v3. Abstract gives low-temperature SOS equilibrium height (1/(4 beta)) log L + O(1). Integer heights and low-temperature contours differ from the present real-height model. No same-model theorem inferred.
6. Yvan Velenik, *Wetting of gradient fields: pathwise estimates*, Probability Theory and Related Fields (2008), DOI 10.1007/s00440-007-0130-x; arXiv:0706.1632v4. Fetched abstract studies localization in the partial wetting regime and approach to wetting transition via reflection positivity. The abstract is not a theorem about the neutral continuous-SOS wall height; no matching solution certified.
7. Hironobu Sakagawa, *Entropic Repulsion of the Massless Field with a Class of Self-potentials*, Journal of Statistical Physics (2009), DOI 10.1007/s10955-009-9745-x. Located in citing-source search. Title alone does not establish applicability to |gradient| interactions; no exact theorem fetched or asserted. Unresolved bibliographic lead.
8. David Brydges and Thomas Spencer, *Fluctuation estimates for sub-quadratic gradient field actions*, Journal of Mathematical Physics **53**(9) (2012), 095216. Exact reference checked in Dario bibliography [37], PDF p. 38. Dario says this covers free-field |x| fluctuation bounds. Gaussian-mixture methodology is relevant, but no hard-wall theorem was verified from this paper.
9. Jean Bricmont, Jean-René Fontaine and Joel L. Lebowitz, *Surface tension, percolation, and roughening*, Journal of Statistical Physics **29**(2) (1982), 193–203. Reference checked in Dario bibliography [36], PDF p. 38. Pre-source free-field infrared-bound lead.
10. Zhan Ye, *Models of gradient type with sub-quadratic actions*, Journal of Mathematical Physics **60**(7) (2019), 073304. Reference checked in Dario bibliography [94], PDF p. 40. Gaussian-mixture free-field lead; no matching wall theorem verified.
11. Arka Adhikari, Reza Gheissari and Ron Peled, *On the rigidity of sloped height functions in d>=3 and non-crossing surfaces*, arXiv:2609.01499v2 (2026). Fetched abstract explicitly studies integer heights, slopes, low-temperature zero-slope coordinates and non-crossing surfaces. This is another different model.

## Search log (every network search/fetch recorded)
All queries below were run on 2026-10-12. Raw responses remain in this folder. API searches are bounded and can miss papers.

- source_pdf: https://arxiv.org/pdf/math/0509695
  Outcome: ok; bytes=722547.

- arxiv_sos: http://export.arxiv.org/api/query?search_query=all%3A%22entropic+repulsion%22+AND+all%3A%22solid-on-solid%22&max_results=30
  Outcome: ok; bytes=15865.

- openalex_sos: https://api.openalex.org/works?search=continuous+solid+on+solid+entropic+repulsion&per-page=30
  Outcome: ok; bytes=786540.

- openalex_source: https://api.openalex.org/works?search=Localization+and+delocalization+of+random+interfaces&per-page=5
  Outcome: ok; bytes=73707.

- crossref_sos: https://api.crossref.org/works?query=continuous+solid+on+solid+entropic+repulsion&rows=30
  Outcome: ok; bytes=151218.

- semantic_sos: https://api.semanticscholar.org/graph/v1/paper/search?query=continuous+solid+on+solid+entropic+repulsion&limit=30&fields=title%2Cauthors%2Cyear%2Curl%2Cabstract%2CexternalIds
  Outcome: <HTTPError 429: ''>; bytes=not retrieved.

- github_sos: https://api.github.com/search/repositories?q=%22entropic+repulsion%22+%22SOS%22&per_page=20
  Outcome: ok; bytes=55.

- arxiv_absolute: https://export.arxiv.org/api/query?search_query=all%3A%22random+surfaces%22+AND+all%3A%22absolute+value%22&max_results=30
  Outcome: ok; bytes=2422.

- openalex_laplace: https://api.openalex.org/works?search=entropic+repulsion+non+uniformly+convex+continuous+interface&per-page=30
  Outcome: <HTTPError 429: 'Too Many Requests'>; bytes=not retrieved.

- openalex_citing: https://api.openalex.org/works?filter=cites%3AW2172014396&per-page=200
  Outcome: ok; bytes=1597187.

- openalex_citing_preprint: https://api.openalex.org/works?filter=cites%3AW4353013745&per-page=200
  Outcome: ok; bytes=383.

- arxiv_continuous: https://export.arxiv.org/api/query?search_query=all%3A%22continuous%22+AND+%28all%3A%22SOS%22+OR+all%3A%22solid-on-solid%22%29+AND+%28all%3A%22repulsion%22+OR+all%3A%22fluctuations%22%29&max_results=50
  Outcome: ok; bytes=109449.

- arxiv_leads: https://export.arxiv.org/api/query?id_list=2609.07578%2C2302.00547%2C2609.01499&max_results=10
  Outcome: ok; bytes=7439.

- crossref_focused: https://api.crossref.org/works?query.title=entropic+repulsion+interface&rows=30
  Outcome: ok; bytes=302014.

- semantic_source: https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0509695?fields=title,citations.title,citations.year,citations.externalIds
  Outcome: ok; bytes=35954.

- middle_pdf: https://arxiv.org/pdf/2609.07578
  Outcome: ok; bytes=939702.

- degenerate_pdf: https://arxiv.org/pdf/2302.00547
  Outcome: ok; bytes=559602.

- arxiv_gradient_repulsion: https://export.arxiv.org/api/query?search_query=ti%3A%22entropic+repulsion%22+AND+%28all%3A%22gradient%22+OR+all%3A%22continuous%22%29&max_results=50
  Outcome: ok; bytes=2624.

- arxiv_wetting: https://export.arxiv.org/api/query?search_query=ti%3A%22Wetting+of+gradient+fields%22+OR+ti%3A%22Entropic+Repulsion+of+the+Massless+Field%22+OR+%28au%3A%22Brydges%22+AND+au%3A%22Spencer%22%29&max_results=20
  Outcome: ok; bytes=2420.

- arxiv_random_environment: https://export.arxiv.org/api/query?id_list=2510.24562&max_results=1
  Outcome: <HTTPError 429: 'Unknown Error'>; bytes=not retrieved.

- openalex_exact_sos: https://api.openalex.org/works?search=%22continuous+SOS%22&per-page=30
  Outcome: <HTTPError 429: 'Too Many Requests'>; bytes=not retrieved.

- sakagawa_page: https://link.springer.com/article/10.1007/s10955-009-9745-x
  Outcome: ok; bytes=3038.

The initial fetch script was inadvertently run twice while checking PDF extraction. Both source downloads succeeded; the second OpenAlex broad search returned HTTP 429, while the first response was already saved. Semantic Scholar search returned HTTP 429, but its source-paper citation endpoint succeeded. GitHub search returned zero repositories. OpenAlex citing-source query returned 93 works, all fitting in its 200-result page; citing the arXiv duplicate returned zero. The final exact-phrase OpenAlex query returned HTTP 429. The Sakagawa publisher fetch returned HTTP 200 but its 3038-byte content is a Client Challenge page, not the article or abstract; this remains an unverified lead. Crossref focused results and relevant Semantic Scholar citing titles were inspected; none supplied a verified same-model theorem.

## Citing-source inventory
These are bibliographic candidates returned by OpenAlex, not all papers individually read.
- Marek Biskup. Recent progress on the Random Conductance Model (2011). https://doi.org/10.1214/11-ps190.
- Louis‐Pierre Arguin; Anton Bovier; Nicola Kistler. Genealogy of extremal particles of branching Brownian motion (2011). https://doi.org/10.1002/cpa.20387.
- Christof Külske. The Ising model: highlights and perspectives (2025). https://doi.org/10.1007/s11040-025-09515-1.
- Francesco Caravenna; Loïc Chaumont. Invariance principles for random walks conditioned to stay positive (2008). https://doi.org/10.1214/07-aihp119.
- Marek Biskup. Reflection Positivity and Phase Transitions in Lattice Spin Models (2009). https://doi.org/10.1007/978-3-540-92796-9_1.
- Marek Biskup; Roman Kotecký. Phase coexistence of gradient Gibbs states (2007). https://doi.org/10.1007/s00440-006-0013-6.
- Aernout C. D. van Enter; Christof Külske. Nonexistence of random gradient Gibbs measures in continuous interface models in d=2 (2008). https://doi.org/10.1214/07-aap446.
- Loren Coquille; Christof Külske; Arnaud Le Ny. Extremal Inhomogeneous Gibbs States for SOS-Models and Finite-Spin Models on Trees (2023). https://doi.org/10.1007/s10955-023-03081-y.
- Francesco Caravenna; Jean-Dominique Deuschel. Pinning and wetting transition for (1+1)-dimensional fields with Laplacian interaction (2008). https://doi.org/10.1214/08-aop395.
- Pietro Caputo; Eyal Lubetzky; Fabio Martinelli; Allan Sly; Fabio; Lucio Toninelli. DYNAMICS OF 2+1 DIMENSIONAL SOS SURFACES ABOVE A WALL: SLOW MIXING INDUCED BY ENTROPIC REPULSION (2013). https://openalex.org/W3098780177.
- Pietro Caputo; Fabio Martinelli; Fabio Lucio Toninelli. On the Approach to Equilibrium for a Polymer with Adsorption and Repulsion (2008). https://doi.org/10.1214/ejp.v13-486.
- Marek Biskup; Herbert Spohn. Scaling limit for a class of gradient fields with nonconvex potentials (2010). https://doi.org/10.1214/10-aop548.
- Codina Cotar; Jean‐Dominique Deuschel. Decay of covariances, uniqueness of ergodic component and scaling limit for a class of $\nabla\phi$ systems with non-convex potential (2012). https://doi.org/10.1214/11-aihp437.
- Piotr Miłoś; Ron Peled. Delocalization of Two-Dimensional Random Surfaces with Hard-Core Constraints (2015). https://doi.org/10.1007/s00220-015-2419-4.
- Alessandra Cipriani; Biltu Dan; Rajat Subhra Hazra. The scaling limit of the membrane model (2019). https://doi.org/10.1214/19-aop1351.
- Nishant Chandgotia; Ron Peled; Scott Sheffield⋆; Martin Tassy. Delocalization of Uniform Graph Homomorphisms from Z2 to Z (2021). https://openalex.org/W3199439366.
- Ostap Hryniv; Mikhail V. Menshikov; Andrew R. Wade. Excursions and path functionals for stochastic processes with asymptotically zero drifts (2013). https://doi.org/10.1016/j.spa.2013.02.001.
- Erwin Bolthausen; Alessandra Cipriani; Noemi Kurt. Exponential Decay of Covariances for the Supercritical Membrane Model (2017). https://doi.org/10.1007/s00220-017-2886-x.
- Tulasi Ram Reddy; Sreekar Vadlamani; Dhandapani Yogeshwaran. Central Limit Theorem for Exponentially Quasi-local Statistics of Spin Models on Cayley Graphs (2018). https://doi.org/10.1007/s10955-018-2026-9.
- Paul Dario; Matan Harel; Ron Peled. Random-field random surfaces (2023). https://doi.org/10.1007/s00440-022-01179-0.
- Piet Lammers; Fabio Lucio Toninelli. Height function localisation on trees (2023). https://doi.org/10.1017/s0963548323000329.
- Alberto Abbondandolo; Florian Henning; Christof Külske; Pietro Majer. Infinite-Volume States with Irreducible Localization Sets for Gradient Models on Trees (2024). https://doi.org/10.1007/s10955-024-03278-9.
- Benedikt Jahnel; Utkir Abdulloevich Rozikov. Gibbs measures for hardcore-solid-on-solid models on Cayley trees (2024). https://doi.org/10.1088/1742-5468/ad5433.
- Benedikt Jahnel; Utkir Abdulloevich Rozikov. Three-state p-SOS models on binary Cayley trees (2024). https://doi.org/10.1088/1742-5468/ad8749.
- Francesco Caravenna; Giambattista Giacomin; Lorenzo Zambotti. Sharp asymptotic behavior for wetting models in (1+1)-dimension (2006). https://doi.org/10.1214/ejp.v11-320.
- Giambattista Giacomin. Renewal convergence rates and correlation decay for homogeneous pinning models (2008). https://doi.org/10.1214/ejp.v13-497.
- Pietro Caputo; Eyal Lubetzky; Fabio Martinelli; Allan Sly; Fabio Lucio Toninelli. Dynamics of $(2+1)$-dimensional SOS surfaces above a wall: Slow mixing induced by entropic repulsion (2014). https://doi.org/10.1214/13-aop836.
- Александр Георгиевич Басуев. Ising model in half-space: A series of phase transitions in low magnetic fields (2007). https://doi.org/10.1007/s11232-007-0132-y.
- Codina Cotar; Christof Külske. Uniqueness of gradient Gibbs measures with disorder (2014). https://doi.org/10.1007/s00440-014-0580-x.
- Sébastien Ott; Yvan Velenik. Potts Models with a Defect Line (2018). https://doi.org/10.1007/s00220-018-3197-6.
- Sébastien Ott; Yvan Velenik. Potts models with a defect line (2018). https://openalex.org/W3098438831.
- Shirshendu Ganguly; Reza Gheissari. Local and global geometry of the 2D Ising interface in critical prewetting (2021). https://doi.org/10.1214/21-aop1505.
- Piet Lammers; Sébastien Ott. Delocalisation and absolute-value-FKG in the solid-on-solid model (2023). https://doi.org/10.1007/s00440-023-01202-y.
- Ron Peled; Wojciech Samotij; Amir Yehudayoff. Grounded Lipschitz functions on trees are typically flat (2013). https://doi.org/10.1214/ecp.v18-2796.
- Stefan Müller; Florian Schweiger. Estimates for the Green’s Function of the Discrete Bilaplacian in Dimensions 2 and 3 (2018). https://doi.org/10.1007/s10013-018-0325-8.
- Nishant Chandgotia; Ron Peled; Scott Sheffield⋆; Martin Tassy. Delocalization of Uniform Graph Homomorphisms from $${\mathbb {Z}}^2$$ to $${\mathbb {Z}}$$ (2021). https://doi.org/10.1007/s00220-021-04181-0.
- Simon Buchholz. Phase transitions for a class of gradient fields (2021). https://doi.org/10.1007/s00440-020-01021-5.
- J. De Coninck; François Dunlop; Thierry Huillet. Random walk versus random line (2009). https://doi.org/10.1016/j.physa.2009.06.030.
- Reza Gheissari; Eyal Lubetzky. Entropic repulsion of 3D Ising interfaces conditioned to stay above a floor (2023). https://doi.org/10.1214/23-ejp987.
- Alexander Magazinov; Ron Peled. Concentration inequalities for log-concave distributions with applications to random surface fluctuations (2022). https://doi.org/10.1214/21-aop1545.
- Scott Armstrong; Paul Dario. Quantitative hydrodynamic limits of the Langevin dynamics for gradient interface models (2024). https://doi.org/10.1214/23-ejp1072.
- Nasir Ganikhodjaev; Nosirzhon Muidinovich Khatamov; Utkir Abdulloevich Rozikov. Gradient Gibbs measures of an SOS model with alternating magnetism on Cayley trees (2023). https://doi.org/10.1016/s0034-4877(23)00082-4.
- Christof Külske; Enza Orlandi. A simple fluctuation lower bound for a disordered massless random continuous spin model in $d=2$ (2006). https://doi.org/10.1214/ecp.v11-1218.
- Loren Coquille; Piotr Miłoś. A note on the discrete Gaussian free field with disordered pinning on Zd , d≥2 (2013). https://doi.org/10.1016/j.spa.2013.04.022.
- Pietro Caputo; Fabio Martinelli; Fabio Lucio Toninelli. On the probability of staying above a wall for the (2+1)-dimensional SOS model at low temperature (2015). https://openalex.org/W3099457103.
- Hironobu Sakagawa. On the Free Energy of a Gaussian Membrane Model with External Potentials (2012). https://doi.org/10.1007/s10955-012-0475-0.
- Giambattista Giacomin; Hubert Lacoin. Disorder and wetting transition: The pinned harmonic crystal in dimension three or larger (2018). https://doi.org/10.1214/17-aap1312.
- Christof Külske; Enza Orlandi. Continuous interfaces with disorder: Even strong pinning is too weak in two dimensions (2007). https://doi.org/10.1016/j.spa.2007.11.005.
- Pietro Caputo; Fabio Martinelli; Fabio Lucio Toninelli. On the probability of staying above a wall for the $$(2+1)$$-dimensional SOS model at low temperature (2015). https://doi.org/10.1007/s00440-015-0658-0.
- Giambattista Giacomin; Hubert Lacoin. Disorder and wetting transition: The pinned harmonic crystal in dimension three or larger (2018). https://openalex.org/W3099433815.
- Pablo A. Ferrari; Sebastian P. Grynberg. No Phase Transition for Gaussian Fields with Bounded Spins (2007). https://doi.org/10.1007/s10955-007-9423-9.
- Pietro Caputo; Fabio Martinelli; Fabio Lucio Toninelli. Entropic repulsion in $$|\nabla \phi |^p$$ | ∇ ϕ | p surfaces: a large deviation bound for all $$p\ge 1$$ p ≥ 1 (2017). https://doi.org/10.1007/s40574-017-0137-x.
- Reza Gheissari; Eyal Lubetzky. Approximate Domain Markov Property for Rigid Ising Interfaces (2023). https://doi.org/10.1007/s10955-023-03101-x.
- Rustamjon Maxmudovich Khakimov; M. T. Makhammadaliev; Utkir Abdulloevich Rozikov. Gibbs Measures for HC-Model with a Cuountable Set of Spin Values on a Cayley Tree (2023). https://doi.org/10.1007/s11040-023-09453-w.
- Paul Dario. Convergence to the thermodynamic limit for random-field random surfaces (2023). https://doi.org/10.1214/22-aap1844.
- Naomi Dvora Feldheim; Shangjie Yang. Typical height of the (2+1)-D Solid-on-Solid surface with pinning above a wall in the delocalized phase (2023). https://doi.org/10.1016/j.spa.2023.08.009.
- Paul Dario. Upper bounds on the fluctuations for a class of degenerate ∇φ-interface models (2024). https://doi.org/10.30757/alea.v21-17.
- Serte Donderwinkel; Brett Kolesnik. Sinaĭ Excursions: An Analogue of Sparre Andersen’s Formula for the Area Process of a Random Walk (2026). https://doi.org/10.1007/s10955-025-03560-4.
- Giambattista Giacomin; Benjamin Havret. Localization, Big-Jump Regime and the Effect of Disorder for a Class of Generalized Pinning Models (2020). https://doi.org/10.1007/s10955-020-02653-6.
- Simon Buchholz; Jean‐Dominique Deuschel; Noemi Kurt; Florian Schweiger. Probability to be positive for the membrane model in dimensions 2 and 3 (2019). https://doi.org/10.1214/19-ecp245.
- S. Friedli; D. Ioffe; Y. Velenik. Subcritical percolation with a line of defects (2013). https://doi.org/10.1214/11-aop720.
- Giambattista Giacomin; Hubert Lacoin. The disordered lattice free field pinning model approaching criticality (2022). https://doi.org/10.1214/22-aop1566.
- Hironobu Sakagawa. Entropic Repulsion of the Massless Field with a Class of Self-potentials (2009). https://doi.org/10.1007/s10955-009-9745-x.
- Yvan Velenik. Wetting of gradient fields: pathwise estimates (2008). https://doi.org/10.1007/s00440-007-0130-x.
- Hironobu Sakagawa. Bounds on the Mass for the High Dimensional Gaussian Lattice Field between Two Hard Walls (2007). https://doi.org/10.1007/s10955-007-9394-x.
- Florian Schweiger. Pinning for the critical and supercritical membrane model (2021). https://doi.org/10.2140/pmp.2021.2.745.
- Sacha Friedli; Dmitry Ioffe; Yvan Velenik. SUBCRITICAL PERCOLATION WITH A LINE OF DEFECTS (2013). https://openalex.org/W3100816257.
- Yvan Velenik. WETTING OF GRADIENT FIELDS: PATHWISE ESTIMATES (2007). https://openalex.org/W3101666794.
- Itaï Benjamini. Gaussian Free Field on Hyperbolic Lattices (2014). https://doi.org/10.1007/978-3-319-09477-9_2.
- Hironobu Sakagawa. Confinement of the Two Dimensional Discrete Gaussian Free Field Between Two Hard Walls (2009). https://doi.org/10.1214/ejp.v14-711.
- Hironobu Sakagawa. Behavior of the Lattice Gaussian Free Field with Weak Repulsive Potentials (2021). https://doi.org/10.1007/s10955-020-02676-z.
- Alessandra Cipriani; Rajat Subhra Hazra; Alan M. Rapoport; Wioletta M. Ruszel. Properties of the Gradient Squared of the Discrete Gaussian Free Field (2023). https://doi.org/10.1007/s10955-023-03187-3.
- Rustamjon Maxmudovich Khakimov; M. T. Makhammadaliev. Translation-Invariant Gibbs Measures for the Hard Core Model with a Countable Set of Spin Values (2024). https://doi.org/10.1134/s1995080224604508.
- Jiwoon Park. Central Limit Theorem for Multi-Point Functions of the 2D Discrete Gaussian Model at High Temperature (2025). https://doi.org/10.1007/s00220-025-05396-1.
- Hironobu Sakagawa. Localization of a Gaussian membrane model with weak pinning potentials (2018). https://doi.org/10.30757/alea.v15-41.
- Marek Biskup; Herbert E. Spohn. Scaling limit for a class of gradient fields with nonconvex potentials (2007). https://openalex.org/W3098771595.
- Francesco Caravenna; Jean‐Dominique Deuschel. Pinning and wetting transition for (1+1)-dimensional fields with Laplacian interaction (2007). https://openalex.org/W3102278326.
- Hironobu Sakagawa. Entropic Repulsion for the High Dimensional Gaussian Lattice Field Between Two Walls (2006). https://doi.org/10.1007/s10955-006-9049-3.
- J. De Coninck; F. Dunlop; Thierry Huillet. Correlations of a bound interface over a random substrate (2006). https://doi.org/10.1140/epjb/e2007-00009-7.
- Giambattista Giacomin. Homogeneous Pinning Systems: A Class of Exactly Solved Models (2011). https://doi.org/10.1007/978-3-642-21156-0_2.
- Александр Георгиевич Басуев; Alexander Georgievich Basuev. Модель Изинга в полупространстве. Серия фазовых переходов при малых магнитных полях (2007). https://doi.org/10.4213/tmf6136.
- Paul Dario. Quantitative hydrodynamic limits of the Langevin dynamics for gradient interface models (2022). https://doi.org/10.5802/slsedp.146.
- U. R. Olimov; Utkir Abdulloevich Rozikov. Неподвижные точки бесконечномерного оператора, связанного с мерами Гиббса (2023). https://doi.org/10.4213/tmf10331.
- U. R. Olimov; Utkir Abdulloevich Rozikov. Fixed points of an infinite-dimensional operator related to Gibbs measures (2023). https://doi.org/10.1134/s0040577923020125.
- Quentin Berger; Brune Massoulié. Wetting on a wall and wetting in a well: Overview of equilibrium properties (2024). https://doi.org/10.1016/j.spa.2024.104299.
- Loren Coquille; Aernout C. D. van Enter; Arnaud Le Ny; Wioletta M. Ruszel. Absence of Shift-Invariant Gibbs States (Delocalisation) for One-Dimensional $$\pmb {\mathbb {Z}}$$-Valued Fields With Long-Range Interactions (2024). https://doi.org/10.1007/s10955-024-03294-9.
- Hironobu Sakagawa. Maximum of the Gaussian Interface Model in Random External Fields (2024). https://doi.org/10.1007/s10955-024-03309-5.
- Joseph Chen; Reza Gheissari; Eyal Lubetzky. Critical wetting in the (2+1)D solid-on-solid model (2024). https://doi.org/10.1214/24-ecp628.
- Aser Cortines; Itamar Harel; Dmitry Ioffe; Oren Louidor. Wetting Transition on Trees I: Percolation With Clustering (2025). https://doi.org/10.1007/s10955-025-03479-w.
- Christof Külske; Niklas Schubert. A-Localized States for Clock Models on Trees and Their Extremal Decomposition into Glassy States (2025). https://doi.org/10.1007/s10955-025-03543-5.
- Alexandre Bordas. Homogénéisation stochastique quantitative (2018). https://doi.org/10.70675/02a7a2fdz3d3bz4f9bzae72zfe2b26d4700c.
- Anil Thapa; Washburn. Finite-Volume Stability and Flux Sectors in a Reciprocal Ratio Gradient Model on Graphs (2026). https://doi.org/10.3390/math14152726.
- R. M. Khakimov; N. N. Mutalliev; U.A. Rozikov. Positive Solutions of a Nonlinear System Characterizing Gibbs Measures in Hard-Core SOS Models on Cayley Trees (2026). https://doi.org/10.1134/s0001434625603247.

## Read-only research brain and prior records
Read-only recall was run on “continuous SOS entropic repulsion Velenik”, “entropic repulsion”, and “entropic repulsion mistakes”. The scripted retries did not complete within 90 seconds. The original shell calls subsequently returned: eight math-store cards (including Friedli–Velenik lattice systems, an unrelated percolation entropy bound, basic calculus, and off-target graph-theory SOS matches); topic/mistake memories were likewise off-target. No theorem used here rests on a recalled claim. The supplied initial cards were reviewed as hints. The F0072-A001 ledger attempt of 2026-09-08 was read in full from the intake and is copied as text in prior_records.txt. It proposed the Gaussian-mixture route but did not check the tilted conductance law; ATTEMPT.md audits and advances that route. Its bibliographic lead arXiv:2510.24562, *Hard wall repulsion for the discrete Gaussian free field in random environment on Z^d, d>=3*, was fetched through an arXiv id query but returned HTTP 429; no theorem from it is asserted to apply. The origin/master repository tree was searched read-only for F0072 paths and returned no matching path. No brain/store/ledger/repository writes were requested.

## Gap-specific brain recall in the second attempt

2026-10-12: Read-only math_recall.py queries: (1) entropic repulsion hard wall boundary subbox reflection positivity chessboard Velenik; (2) absolute value FKG continuous SOS Lammers Lis; (3) convex gradient model conditional fluctuations hard wall Brascamp Lieb duplication. All three completed; full outputs are gap_recall_1.txt, gap_recall_2.txt and gap_recall_3.txt. These were gap/toolkit recalls, not fresh network searches.

Relevant returned references were J. Fröhlich, R. Israel, E. H. Lieb and B. Simon, “Phase transitions and reflection positivity. I. General theory and long range lattice models”, Communications in Mathematical Physics 62 (1978), 1–34, DOI 10.1007/BF01940327; and Richard Holley, “Remarks on the FKG inequalities”, Communications in Mathematical Physics 36 (1974), 227–231, DOI 10.1007/BF01645980. The reflection-positivity technique card explicitly warns that altered wall/field geometry requires rechecking the structure. Neither recalled reference was verified as a theorem resolving this SOS wall-edge gap. The other matches were largely unrelated (basic absolute values, graph-theory SOS, optimization convexity). No original proof here rests on a recalled unverified statement.
