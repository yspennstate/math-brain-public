# Literature record ? F0034

Date: 2026-10-12. No exact published solution identified; this is a bounded search, not a certificate of openness.

## Searches

- source: `https://arxiv.org/pdf/1506.00724` ? HTTP 200, 1399192 bytes; saved source.pdf

- arxiv: `https://export.arxiv.org/api/query?search_query=all%3A%22Brownian+net%22&max_results=100&sortBy=submittedDate&sortOrder=descending` ? HTTP 200, 25350 bytes; saved arxiv.xml

- openalex: `https://api.openalex.org/works?search=Brownian+net+bubble&per-page=50` ? HTTP 200, 1007404 bytes; saved openalex.json

- openalex_source: `https://api.openalex.org/works?search=The+Brownian+web+the+Brownian+net+and+their+universality&per-page=5` ? HTTP 200, 98739 bytes; saved openalex_source.json

- crossref: `https://api.crossref.org/works?query=Brownian+net+bubble+hypothesis&rows=30` ? HTTP 200, 206021 bytes; saved crossref.json

- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Brownian+net+bubble&limit=50&fields=title%2Cauthors%2Cyear%2Cabstract%2CexternalIds%2Curl` ? HTTP Error 429: 

- github: `https://api.github.com/search/repositories?q=%22Brownian+net%22&per_page=50` ? HTTP 200, 11362 bytes; saved github.json

- citing_book: `https://api.openalex.org/works?filter=cites:W2121110727&per-page=200` ? HTTP 200, 931676 bytes, citing_book.json

- citing_arxiv: `https://api.openalex.org/works?filter=cites:W4300525659&per-page=200` ? HTTP 200, 383 bytes, citing_arxiv.json

- arxiv_bubble: `https://export.arxiv.org/api/query?search_query=all%3A%22bubble+hypothesis%22&max_results=100` ? HTTP 200, 6834 bytes, arxiv_bubble.xml

- openalex_backbone: `https://api.openalex.org/works?search=%22Brownian+net%22+backbone&per-page=100` ? HTTP 200, 161247 bytes, openalex_backbone.json

- semantic_citations: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1506.00724/citations?limit=100&fields=title,year,authors,abstract,externalIds` ? HTTP Error 429: 

- special_times: `https://arxiv.org/pdf/2512.10761` ? HTTP 200, 300677 bytes, special_times.pdf

- universality: `https://arxiv.org/pdf/2401.09370` ? HTTP 200, 753232 bytes, universality.pdf

- special_points: `https://arxiv.org/pdf/0806.2326` ? HTTP 200, 790904 bytes, special_points.pdf

## Source verified

Emmanuel Schertzer, Rongfeng Sun and Jan M. Swart, *The Brownian web, the Brownian net, and their universality*, arXiv:1506.00724v3, 9 January 2017. Published chapter DOI 10.1017/9781316403877.007 (2016). Source PDF pp. 70?71, Section 8.2. Standard Brownian net, stationary backbone; time slices have Poisson intensity 2. Backward paths are forward backbone paths followed backward, explicitly NOT dual paths. The two infinite endpoints map to each other.

Exact conjecture (PDF page 71, typography normalized):

> Conjecture 8.1 (Bubble hypothesis)

> (a) Almost surely, there does not exist an infinite sequence of points (z_k)_{k?0} in S* ? M*, all different from each other, such that ?(z_{k?1}) = z_k for all k ? 1.

> (b) Almost surely, there does not exist an infinite sequence of points (z_k)_{k?0} in S* ? M*, all different, such that ?(z_k) = z_{k?1} for all k ? 1.

Source definitions: S consists of backbone separation points of type (p,pp)_s and M of meeting points of type (pp,p). ? sends separation points to their first extremal forward reunion, or +?; reversed backbone definition sends meetings to first backward reunion, or ??.

## Retrieved related papers

- Ruibo Kou. Special times for the point set process of the Brownian Net. http://arxiv.org/abs/2512.10761v1. PDF retrieved and text screened.

- Rongfeng Sun, Jan M. Swart, Jinjiong Yu. Universality of the Brownian net. http://arxiv.org/abs/2401.09370v2. PDF retrieved and text screened.

- Rafael Santos, Glauco Valle, Leonel Zuaznábar. On the convergence of the drainage network with branching. http://arxiv.org/abs/2206.04235v2. Metadata and abstract screened; no asserted exact solution.

- Jean-François Le Gall. Brownian disks and the Brownian snake. http://arxiv.org/abs/1704.08987v2. Metadata and abstract screened; no asserted exact solution.

- C. M. Newman, K. Ravishankar, E. Schertzer. Perturbations of the Voter Model in One-Dimension. http://arxiv.org/abs/1607.06058v1. Metadata and abstract screened; no asserted exact solution.

- Barnaby Garrod, Roger Tribe, Oleg Zaboronski. Examples of interacting particle systems on $\mathbb{Z}$ as Pfaffian point processes: coalescing branching random walks and annihilating random walks with immigration. http://arxiv.org/abs/1605.09668v2. Metadata and abstract screened; no asserted exact solution.

- Alison Etheridge, Nic Freeman, Daniel Straulino. The Brownian Net and Selection in the Spatial Lambda-Fleming-Viot Process. http://arxiv.org/abs/1506.01158v2. Metadata and abstract screened; no asserted exact solution.

- Emmanuel Schertzer, Rongfeng Sun, Jan M. Swart. The Brownian web, the Brownian net, and their universality. http://arxiv.org/abs/1506.00724v3. Metadata and abstract screened; no asserted exact solution.

- Charles M. Newman, K. Ravishankar, Emmanuel Schertzer. The Brownian Net with Killing. http://arxiv.org/abs/1309.5651v1. Metadata and abstract screened; no asserted exact solution.

- Emmanuel Schertzer, Rongfeng Sun, Jan M. Swart. Stochastic flows in the Brownian web and net. http://arxiv.org/abs/1011.3895v2. Metadata and abstract screened; no asserted exact solution.

- Emmanuel Schertzer, Rongfeng Sun, Jan M. Swart. Special points of the Brownian net. http://arxiv.org/abs/0806.2326v2. PDF retrieved and text screened.

- C. M. Newman, K. Ravishankar, E. Schertzer. Marking (1,2) Points of the Brownian Web and Applications. http://arxiv.org/abs/0806.0158v2. Metadata and abstract screened; no asserted exact solution.

- L. R. G. Fontes, C. M. Newman, K. Ravishankar, E. Schertzer. The Dynamical Discrete Web. http://arxiv.org/abs/0704.2706v1. Metadata and abstract screened; no asserted exact solution.

- Rongfeng Sun, Jan M. Swart. The Brownian net. http://arxiv.org/abs/math/0610625v5. Metadata and abstract screened; no asserted exact solution.

Special times (R. Kou, arXiv:2512.10761) studies exceptional-time Hausdorff dimension, not ?-orbits. Universality (Sun?Swart?Yu, arXiv:2401.09370) studies scaling limits and backbone equilibrium. Special points (Schertzer?Sun?Swart, arXiv:0806.2326) supplies structural and relevant-point finiteness facts, predating the conjecture. None is recorded as a solution.

## OpenAlex citing-source screen

Published chapter identity W2121110727 returned 52 citing records, all included below. Preprint identity W4300525659 returned zero; this is an indexing limitation. Titles and available abstract text were inspected for bubble hypothesis/backbone orbit claims; no exact-solution candidate identified. Full texts were not retrieved for every citation.

- Guillaume Barraquand, Mark Rychnovsky. Large deviations for sticky Brownian motions. 2020. https://doi.org/10.1214/20-ejp515

- Thimothée Thiery, Pierre Le Doussal. Exact solution for a random walk in a time-dependent 1D random environment: the point-to-point Beta polymer. 2016. https://doi.org/10.1088/1751-8121/50/4/045001

- Andreas Greven, Rongfeng Sun, Anita Winter. Continuum space limit of the genealogies of interacting Fleming-Viot processes on $\mathbb{Z}$. 2016. https://doi.org/10.1214/16-ejp4514

- Alison M. Etheridge, Nic Freeman, Daniel Straulino. The Brownian net and selection in the spatial $\Lambda $-Fleming-Viot process. 2017. https://doi.org/10.1214/17-ejp61

- Ellen Baake, Anton Wakolbinger. Probabilistic Structures in Evolution. 2021. https://doi.org/10.4171/ecr/17

- David Coupier, Kumarjit Saha, Anish Sarkar, Viet Chi Tran. The 2d-directed spanning forest converges to the Brownian web. 2021. https://doi.org/10.1214/20-aop1478

- Vitalii Konarovskyi. Coalescing-fragmentating Wasserstein dynamics: Particle approach. 2023. https://doi.org/10.1214/22-aihp1271

- Jacopo Borga, Mickaël Maazoun. Scaling and local limits of Baxter permutations and bipolar orientations through coalescent-walk processes. 2022. https://doi.org/10.1214/21-aop1559

- Barnaby Garrod, Roger Tribe, Oleg V. Zaboronski. Examples of Interacting Particle Systems on $$\mathbb {Z}$$ as Pfaffian Point Processes: Coalescing–Branching Random Walks and Annihilating Random Walks with Immigration. 2019. https://doi.org/10.1007/s00023-019-00877-1

- Subhroshekhar Ghosh, Kumarjit Saha. Transmission and Navigation on Disordered Lattice Networks, Directed Spanning Forests and Brownian Web. 2020. https://doi.org/10.1007/s10955-020-02604-1

- Sayan Das, Hindy Drillick, Shalin Parekh. Multiplicative SHE limit of random walks in space–time random environments. 2024. https://doi.org/10.1007/s00440-024-01339-4

- Simone Floreani, Sabine Jansen, Frank Redig, Stefan Wagner. Intertwining and duality for consistent Markov processes. 2024. https://doi.org/10.1214/24-ejp1124

- David Coupier, Jean‐François Marckert, Viet Chi Tran. Directed, cylindric and radial Brownian webs. 2019. https://doi.org/10.1214/18-ejp255

- Giuseppe Cannizzaro, Martin Hairer. The Brownian Castle. 2022. https://doi.org/10.1002/cpa.22085

- Raphaël Forien. The stepping stone model in a random environment and the effect of local heterogneities on isolation by distance patterns. 2019. https://doi.org/10.1214/19-ejp314

- Michael Damron, Jack Hanson, David Harper, Wai‐Kit Lam. Transitions for exceptional times in dynamical first-passage percolation. 2022. https://doi.org/10.1007/s00440-022-01178-1

- Nic Freeman, Jan M. Swart. Weaves, webs and flows. 2024. https://doi.org/10.1214/24-ejp1161

- Elena Kosygina, Jonathon Peterson. Convergence of rescaled “true” self-avoiding walks to the Tóth-Werner “true” self-repelling motion. 2026. https://doi.org/10.1214/26-ejp1489

- David Aldous. Waves in a Spatial Queue. 2017. https://doi.org/10.1287/15-ssy208

- Guillaume Barraquand, Mark Rychnovsky. Tracy-Widom Asymptotics for a River Delta Model. 2019. https://doi.org/10.1007/978-3-030-15096-9_17

- Matthias Birkner, Nina Gantert, Sebastian Steiber. Coalescing directed random walks on the backbone of a 1+1-dimensional oriented percolation cluster converge to the Brownian web. 2019. https://doi.org/10.30757/alea.v16-37

- Charles M. Newman, K. Ravishankar, Emmanuel Schertzer. Perturbations of Voter model in one-dimension. 2017. https://doi.org/10.1214/17-ejp37

- Emmanuel Schertzer, Rongfeng Sun. Perturbations of Supercritical Oriented Percolation and Sticky Brownian Webs. 2019. https://doi.org/10.1007/978-981-15-0298-9_11

- Rongfeng Sun, Jan M. Swart, Jinjiong Yu. Equilibrium interfaces of biased voter models. 2019. https://doi.org/10.1214/19-aap1461

- Matthias Birkner, Nina Gantert. Ancestral lineages in spatial population models with local regulation. 2021. https://doi.org/10.4171/ecr/17-1/14

- James Bell. Time-reversal of coalescing diffusive flows and weak convergence of localized disturbance flows. 2020. https://doi.org/10.1214/20-ejp500

- Jochen Blath, Marcel Ortgiese. The symbiotic branching model: Duality and interfaces. 2021. https://doi.org/10.4171/ecr/17-1/15

- Andreas Greven, Rongfeng Sun, Anita Winter. Continuum Space Limit of the Genealogies of Interacting Fleming-Viot Processes on $\Z$. 2015. https://doi.org/10.48550/arxiv.1508.07169

- Barnaby Garrod, Roger Tribe, Oleg V. Zaboronski. Examples of interacting particle systems on $\mathbb{Z}$ as Pfaffian point processes II - coalescing branching random walks and annihilating random walks with immigration. 2016. https://openalex.org/W2419545643

- Matthias Ludwig Alfons Hammer, Marcel Ortgiese, Florian Völlering. Entrance laws for annihilating Brownian motions. 2018. https://openalex.org/W2784342039

- Pascal Maillard, Gaël Raoul, Julie Tourniaire. Spreading speed of locally regulated population models in macroscopically heterogeneous environments. 2021. https://doi.org/10.48550/arxiv.2105.06985

- David Aldous. Waves in a Spatial Queue: Stop-and-Go at Airport Security. 2015. https://doi.org/10.48550/arxiv.1511.05140

- Charles M. Newman, K. Ravishankar, Emmanuel Schertzer. Perturbations of the Voter Model in One-Dimension. 2016. https://doi.org/10.48550/arxiv.1607.06058

- Kumarjit Saha. On a conjecture of David Aldous: river network and the continuum random tree. 2017. https://openalex.org/W2626558614

- Rongfeng Sun, Jan M. Swart, Jinjiong Yu. Equilibrium interfaces of biased voter models. 2018. https://doi.org/10.48550/arxiv.1804.04342

- Federico Camia, Daniel L. Stein. Probability Theory in Statistical Physics, Percolation, and Other Random Topics: The Work of C. Newman. 2019. https://doi.org/10.1007/978-981-15-0294-1_1

- Federico Camia, Stein, Daniel L.. Probability Theory in Statistical Physics, Percolation, and Other Random Topics: The Work of C. Newman. 2020. https://doi.org/10.48550/arxiv.2002.00342

- Subhroshekhar Ghosh, Kumarjit Saha. Transmission and navigation on disordered lattice networks, directed spanning forests and scaling limits. 2020. https://openalex.org/W3005879356

- Kumarjit Saha. Continuum random tree as the scaling limit for a drainage network model: a Brownian web approach. 2017. https://doi.org/10.48550/arxiv.1704.00429

- Azadeh Parvaneh, Afshin Parvardeh, Rahul Roy. A Drainage Network with Dependence and the Brownian Web. 2022. https://doi.org/10.1007/s10955-022-02978-4

- Amaury Lambert. Modèles aléatoires pour l’inférence de l’évolution du vivant / Stochastic models for the inference of life evolution (SMILE). 2019. https://doi.org/10.4000/annuaire-cdf.14742

- Lung-Chi Chen, Satoshi Handa, Yoshinori Kamijima. Mean-field behavior of Nearest-Neighbor Oriented Percolation on the BCC Lattice Above 8 + 1 Dimensions. 2023. https://doi.org/10.1007/s11040-022-09441-6

- Giuseppe Cannizzaro, Martin Hairer. The Brownian Web as a random R-tree. 2023. https://doi.org/10.1214/23-ejp984

- Konstantin Mikhailovich Khanin, Liying Li. On the rate of convergence to coalescing Brownian motions. 2024. https://doi.org/10.1214/22-aihp1348

- R. Santos, Glauco Valle, Leonel Zuaznábar. On the Convergence of the Drainage Network with Branching. 2024. https://doi.org/10.61102/1024-2953-mprf.2024.30.2.001

- Michael Damron, Jack Hanson, David A. T. Harper, Wai‐Kit Lam. Exceptional behavior in critical first-passage percolation and random sums. 2026. https://doi.org/10.1214/26-ejp1503

- Thimothée Thiery. Analytical methods and field theory for disordered systems. 2016. https://doi.org/10.70675/46fefaddz179dz4666z8445z6f90cd74da5a

- Mickaël Maazoun. Universal permuton limits of random pattern-avoiding permutations. 2020. https://doi.org/10.70675/5c97ca54ze592z4463zbff6ze6468e3bc148

- Julie Tourniaire. Spatial dynamic of interfaces in ecology : deterministic and stochastic models. 2021. https://doi.org/10.70675/2039765cz5936z4589zbb59z81d5d07cbc4a

- Lucas Flammant. Directed and Radial Random Spanning Forests in Hyperbolic Spaces. 2022. https://doi.org/10.70675/9adb2166z865dz4713za3e3z3282dae0ed78

- Alice Contat. Parking on random trees. 2023. https://doi.org/10.70675/28598a09z935cz4b4bz8163z9244bbb8e7fe

- Shalin Parekh. Hierarchy of KPZ limits arising from directed random walk models in random media. 2026. https://doi.org/10.1017/fms.2026.10220

## Read-only prior-work checks

Intake F_20260908, F0034-A001: heuristic only; unproved nested-bubble assertion and inaccurate heavy-tail argument must not be used. An infinite chain escaping to infinity does not satisfy the conjecture.

math_recall query: Schertzer Sun Swart Brownian net backbone bubbles. Returned unrelated signed-net Laplacian cards; no useful lead. brain.py recall query: Brownian net backbone bubble hypothesis mistakes. No useful lead. The supplied recall script reported an automatic detached refresh; no further brain.py calls were made.

Read origin/master in math-open-problems with git grep for F0034/bubble hypothesis and git show of F0036/memo.md. Neighbouring attempt remains partial and reports a 31 March 2025 Swart talk as still listing the hypotheses; that talk has not yet been independently fetched here.

Semantic Scholar search and citation endpoint both returned HTTP 429. This gap is explicitly retained. GitHub returned two unrelated Brownian-network repositories. No proof found there.


## Related exceptional-time theorem checked

R. Kou, *Special times for the point set process of the Brownian Net*, arXiv:2512.10761v1, 11 December 2025, Theorem 1, PDF page 2:

> Let T := {t : ?_t^R contains cluster points}. Then almost surely dim T = 1/2.

This is not Conjecture 8.1: it proves a dimension statement about point-set special times. ATTEMPT.md, Corollary 6 applies it to bound the set of possible inverse-chain limit times; this implication is our argument, not a solution in print.

The arXiv exact-phrase bubble-hypothesis search returned three unrelated social/financial bubble papers. Available abstracts of all 52 OpenAlex citing records were screened for bubble/backbone/separation/meeting terms; only an oriented-percolation-backbone convergence paper matched, and concerns a different object.


## Second-attempt gap search and source audit ? 2026-10-12

Read-only math_recall query: Brownian net exceptional times cluster points inverse chain Kou Schertzer. No direct net card returned. Walked card claim_644045ce021d905aa60b2d065f197a6a96352a41bb3aa633d62cefdb1144e0c6: quasi-multiplicativity of arm events in planar percolation. Its hypotheses concern percolation, not the Brownian net; it explicitly cautions against multiplying scale estimates without constants or unproved independence. It is a method hint only.

Re-read retrieved Schertzer, Sun and Swart, Special points of the Brownian net, arXiv:0806.2326v2: Proposition 2.6 (PDF pp. 22?24; separation point is (1,2)_l in the left web), Lemma 3.7 (PDF p. 33; one-sided isolation), Proposition 3.11(a,b) (PDF pp. 34?35; nested cluster excursions), Lemma 3.12 (PDF pp. 36?37; cluster-point equivalence for image-set paths), Theorem 1.7 (PDF p. 10; 20 types) and Theorem 1.12 (PDF pp. 13?14; continuation restrictions). These remain structural inputs and do not prove the bubble hypothesis.

Kou arXiv:2512.10761v1, Lemma 7 and Proposition 8, PDF p. 5, restate the isolation and nested-excursion facts. No new exact literature solution is asserted. The common incoming/outgoing equivalence of cluster-point image-set paths is already present in the 2009 special-points source; the new reduction records the specific inverse-chain vertices as forced bottlenecks, not a novel equivalence-class theorem.


2026-10-12 fetch with Python urllib: https://arxiv.org/pdf/math/0610625 ? HTTP 200; saved original_net.pdf (800969 bytes), extracted original_net.txt. Reference: Rongfeng Sun and Jan M. Swart, The Brownian net, Annals of Probability 36(3), 1153?1208 (2008), DOI 10.1214/07-AOP357, arXiv:math/0610625. Lemma 3.4(b), PDF page 27: every web path agrees after a positive delay with a path from a deterministic countable dense skeleton. Applies to drifted webs by their deterministic tilt. Used only for the countable-spine corollary in SECOND_ATTEMPT.md, not as a literature solution of Conjecture 8.1.
