# Literature record — P0287 — 2026-10-12

## Further-attempt searches and neighbouring theorem

All searches/fetches in this subsection were performed on 2026-10-12, using Python from the shell. They supplement, rather than replace, the earlier search log below.

- Read-only math store query: `TASEP killing defect positive transmitted current invariant coupling Liggett`. Returned the old current/product obstruction and unrelated Liggett cards, not a result about transmitted flow.
- Read-only math store query: `exclusion process translation invariant stationary measures mixtures Bernoulli Liggett Spitzer`. No usable homogeneous classification card; definitions and unrelated cards were not treated as theorem evidence.
- Full-paper fetch: https://arxiv.org/pdf/1704.07799 — successful PDF, saved as slowbond.pdf, text slowbond.txt. R. Basu, S. Sarkar, A. Sly, *Invariant Measures for TASEP with a Slow Bond* (2017). Its PDF p.4 background explicitly states: “In [21], Liggett identified the set of all invariant measures for TASEP, and showed that apart from a few trivial measures, the extremal invariant measures for TASEP are the Bernoulli product measures {νρ : ρ ∈ (0, 1)}.” This homogeneous-model input, not a slow-bond theorem, is used in SECOND_ATTEMPT Theorems C and D. The zero-current trivial measures can also be identified directly from vanishing nonnegative bond rates. No assertion that the slow-bond theorem solves killing is made.
- Crossref exact-title query: https://api.crossref.org/works?query.title=Coupling%20the%20simple%20exclusion%20process&rows=3 — successful JSON in liggett_crossref.json. Verified exact reference: T. M. Liggett, *Coupling the Simple Exclusion Process*, Annals of Probability 4(3) (1976), 339–356, DOI 10.1214/aop/1176996084. The other returned records were the Springer chapter *The Simple Exclusion Process*, DOI 10.1007/978-3-642-29880-6_5, and *Asymmetric simple exclusion process*, DOI 10.29172/24d2edc1-911e-428d-b58d-d7a815949b4c; they were not used as results.
- Primary Liggett request: https://projecteuclid.org/journals/annals-of-probability/volume-4/issue-3/Coupling-the-Simple-Exclusion-Process/10.1214/aop/1176996084.pdf — HTTP 200 but a 1,158-byte Incapsula HTML challenge, not a PDF; saved as liggett_modern.txt. No theorem number or page is claimed from it.
- Alternate primary request, URL supplied by Crossref: https://projecteuclid.org/download/pdf_1/euclid.aop/1176996084 — same non-PDF challenge, saved as liggett_legacy.txt. Machine outcomes in liggett_fetch_log.json. No access-control bypass was attempted.

Theorems A and B of the second attempt give self-contained positive-transmitted-flow existence proofs, including the ordinary Bernoulli invariance they need. Theorems C and D are complete reductions to the stated classical homogeneous classification, which is supported by the fetched secondary paper but not independently re-proved here. The new results are restricted constructions/uniqueness, not a full solution of the workshop question and not a SOLVED_IN_LITERATURE claim.

## Status and exact source
Leonid Petrov and Axel Saenz Rodriguez (organizers), *All roads to the KPZ universality class*, AIM Workshop Summary (workshop 2025), PDF p.5, section “ASEP on graphs or trees,” system S2. https://aimath.org/pastworkshops/roadtokpzrep.pdf. Saved as aim_https.pdf, with extracted text source.txt.

> S2 TASEP on the full line with a particle removal mechanism at site 0 (where particles disappear from the system at a fixed rate).

> We then focused on studying the invariant measure of the second system using the matrix product ansatz.

> A key challenge in applying the matrix ansatz to our system lies in identifying the appropriate telescoping structure.

> We agreed to continue working on this problem after the workshop. However, there has been no progress since then.

The report names Zongrui Yang as contact. It specifies full-line TASEP and fixed-rate removal at 0, but does not state the rate normalization, positivity explicitly, tail densities, extremality, or an all-measures quantifier. This attempt uses unit jump rate and kappa>0, as in the supplied problem; “characterize invariant measures” is the research objective inferred from the report, not a separately numbered theorem. The fetched workshop page identifies the event as 2025; the PDF itself is a follow-up summary rather than a journal article.

No paper proving the full classification was identified. This is NOT a verified assertion that no such paper exists. OpenAlex and Semantic Scholar requests were rate-limited; no exact source record was obtained from OpenAlex, so its citing-works query could not be performed with a verified work ID. These search gaps preclude an exhaustive status claim. No SOLVED_IN_LITERATURE verdict is assigned.

## Search log
All requests below were made on 2026-10-12 using Python urllib, never built-in web search. Exact URLs contain the exact queries and parameters. Response bodies and machine logs are retained in this folder.

- Initial source fetch with the default urllib user-agent: https://aimath.org/pastworkshops/roadtokpzrep.pdf — HTTP 403; retried successfully with a browser user-agent.
- **aim_https**: https://aimath.org/pastworkshops/roadtokpzrep.pdf — 200; saved aim_https.pdf
- **aim_http**: http://aimath.org/pastworkshops/roadtokpzrep.pdf — 200; saved aim_http.pdf
- **arxiv_http**: http://export.arxiv.org/api/query?search_query=all%3ATASEP%20AND%20%28all%3Akilling%20OR%20all%3Aannihilation%20OR%20all%3Adefect%29&max_results=40 — 200; saved arxiv_http.txt
- **arxiv_https**: https://export.arxiv.org/api/query?search_query=all%3ATASEP%20AND%20%28all%3Akilling%20OR%20all%3Aannihilation%20OR%20all%3Adefect%29&max_results=40 — 200; saved arxiv_https.txt
- **openalex_killing**: https://api.openalex.org/works?search=TASEP%20killing&per-page=30 — HTTP Error 429: Too Many Requests
- **openalex_source**: https://api.openalex.org/works?search=all%20roads%20to%20KPZ&per-page=10 — HTTP Error 429: Too Many Requests
- **crossref**: https://api.crossref.org/works?query=TASEP%20killing%20invariant%20measures&rows=30 — 200; saved crossref.json
- **semantic**: https://api.semanticscholar.org/graph/v1/paper/search?query=TASEP%20killing&limit=30&fields=title,authors,year,abstract,url,externalIds — HTTP Error 429: 
- **github**: https://api.github.com/search/repositories?q=TASEP%20killing&per_page=30 — 200; saved github.json
- **openalex_invariant**: https://api.openalex.org/works?search=TASEP%20invariant%20measures%20local%20particle%20removal&per-page=30 — HTTP Error 429: Too Many Requests
- **workshop_page**: https://lpetrov.cc/kpz2025/index.html — 200; saved workshop_page.txt
- **arxiv_removal**: https://export.arxiv.org/api/query?search_query=all%3ATASEP%20AND%20%28all%3Akilling%20OR%20all%3Aremoval%20OR%20all%3Asink%29&max_results=100&sortBy=submittedDate&sortOrder=descending — 200; saved arxiv_removal.txt
- **arxiv_halfline**: https://export.arxiv.org/api/query?search_query=all%3AASEP%20AND%20%28all%3Asemi-infinite%20OR%20all%3Ahalf-line%29%20AND%20all%3Astationary&max_results=30 — 200; saved arxiv_halfline.txt
- **openalex_retry**: https://api.openalex.org/works?search=TASEP%20killing%20at%20one%20site&per_page=5 — HTTP Error 429: Too Many Requests
- **openalex_report_retry**: https://api.openalex.org/works?search=roadtokpzrep&per_page=5 — HTTP Error 429: Too Many Requests
- **semantic_retry**: https://api.semanticscholar.org/graph/v1/paper/search?query=TASEP%20particle%20removal%20invariant&limit=5&fields=title,year,authors,url — HTTP Error 429: 
- **crossref_target**: https://api.crossref.org/works?query.bibliographic=TASEP%20particle%20removal%20single%20site&rows=20 — 200; saved crossref_target.json
- **github_target**: https://api.github.com/search/repositories?q=TASEP%20stationary&per_page=20 — 200; saved github_target.json

### Read-only brain and earlier-record searches
- math_recall.py: “TASEP invariant measures killing defect”; returned the previous local-current/product-obstruction attempt and its dependencies.
- brain.py recall: “TASEP invariant measures mistakes”; no useful mathematical result. The helper reported its own automatic index refresh; no remember/write command was requested. No further brain.py commands were used.
- math_recall.py: “Liggett half line exclusion stationary measures boundary”; results mostly off topic, not used as premises.
- math_recall.py --id claim_0b7f0cf3843d83b7cb84de2998e8f8a53197aacc6cf57f7a75d24c2f4d06c4ba: read the earlier attempt whole; independently rechecked both its current and covariance formulas, and extended its interior-density obstruction to a full product classification.
- rg for P0287 in intake problems.jsonl, attempts.jsonl and sources.jsonl, and codex_pool_2026_10_10: no matching earlier files found in these targeted paths; two intake directories lacked attempts/sources files. An initial broader jsonl search found the 2026-10-10 problem-list record with the supplied statement and caveat.
- Read-only git ls-tree origin/master filtered for P0287/p0287 in ~/math-open-problems: no matching path. No repository was changed.

## Relevant leads, with scope differences
- B. Derrida, M. R. Evans, V. Hakim, V. Pasquier, “Exact solution of a 1D asymmetric exclusion model using a matrix formulation,” *Journal of Physics A: Mathematical and General* 26 (1993), 1493–1517. Explicitly cited by the workshop source. Finite open ASEP matrix ansatz, not full-line single-site killing; no inference of a printed solution.
- Riddhipratim Basu, Sourav Sarkar, Allan Sly, “Invariant Measures for TASEP with a Slow Bond,” arXiv:1704.07799 (2017). Read the returned abstract. A conservative slow hopping bond is a different generator: no death and no current loss at the defect. Its invariant-measure theorem cannot answer this question.
- Tomohiro Sasamoto, Lauren Williams, “Combinatorics of the asymmetric exclusion process on a semi-infinite lattice,” arXiv:1204.1114v1 (2012). Full PDF fetched from https://arxiv.org/pdf/1204.1114 to halfline.pdf, text halfline.txt. Directly relevant to the reduction in ATTEMPT Section 5, but treats a semi-infinite boundary and supplies formulas under a semi-infinite matrix ansatz; no full-line killing classification claimed here.
- The same paper: Theorem 4.1 begins on PDF p.6; the word-functional formulation is Remark 4.3 on p.9. Theorem 5.1 on p.9 guarantees positivity when q<=1 and either a>=1, c<=(1-q)a/(1+a)^2, or a<=1, c<=(1-q)/4. For q=gamma=0, alpha=kappa, a=max(1-kappa,0)/kappa, these bounds become c<=kappa(1-kappa) for kappa<=1/2 and c<=1/4 otherwise. ATTEMPT Section 8 gives a direct elementary q=0 proof and transfers it to full-line killing with the downstream half frozen occupied. This is a special-case construction from a related known model, not a new claim of novelty or a literature solution of the full question. Neither these ansatz theorems nor their transfer proves exhaustion of the full-line invariant laws.
- T. M. Liggett, “Ergodic theorems for the asymmetric simple exclusion process,” *Transactions of the American Mathematical Society* 213 (1975), 237–261. Exact reference from Sasamoto–Williams bibliography p.13; further half-line classification lead, not independently fetched or used as a theorem here. S. Grosskinsky, Ph.D. dissertation, Technical University of Munich (2004), is cited there for the q=gamma=0 semi-infinite ansatz (Theorem 3.2); dissertation title not established in this search.
- Zongrui Yang, “Limits of open ASEP stationary measures near a boundary,” arXiv:2402.13675v2 (submitted 2024). Returned abstract concerns limits of finite open stationary measures and convergence near a boundary. A useful half-line lead, not the killing-site model.
- Yuliy Baryshnikov, Alexander Stolyar, “Multi-floor generalization of TASEP,” arXiv:2603.13610v2 (submitted 2026-03-13). This is a post-workshop hit, but the model has multiple occupancy, back-pressure movement, and boundary input/output. Its standard-TASEP c=1 case is still boundary-driven and has no interior killing; not a solution.
- Sourav Pal, Abhik Basu, “Stationary densities in a weakly nonconserving asymmetric exclusion processes with finite resources,” arXiv:2602.08405v1 (2026). Post-workshop hit. Langmuir kinetics and a finite-resource reservoir differ from single-site full-line killing; abstract describes density/phase diagrams, not the requested classification.
- ExclusionProcess-tools/TASEPy and Francesco-Cerutti/TASEP-inhomogeneities-approximations, GitHub repositories returned by “TASEP stationary”. Numerical/approximation packages for inhomogeneous TASEP, not proof of this classification. Query “TASEP killing” returned zero repositories.

## All arXiv records returned (for audit)

### arxiv_https.txt
- Nikhil Bhatia, Arvind Kumar Gupta. Modified version of open TASEP with dynamic defects. http://arxiv.org/abs/2405.04956v2; submitted 2024-05-08T10:51:08Z.
- Riddhipratim Basu, Sourav Sarkar, Allan Sly. Invariant Measures for TASEP with a Slow Bond. http://arxiv.org/abs/1704.07799v1; submitted 2017-04-25T17:22:47Z.
- K. Kavanagh, S. Dooley, J. K. Slingerland, G. Kells. Effects of Quantum Pair Creation and Annihilation on a Classical Exclusion Process: the transverse XY model with TASEP. http://arxiv.org/abs/2110.08283v1; submitted 2021-10-15T18:00:05Z.
- J. J. Dong, R. K. P. Zia, B. Schmittmann. Understanding the edge effect in TASEP with mean-field theoretic approaches. http://arxiv.org/abs/0809.1974v1; submitted 2008-09-11T12:28:22Z.
- L. Jonathan Cook, J. J. Dong. Power spectra of TASEPs with a localized slow site. http://arxiv.org/abs/1008.1527v2; submitted 2010-08-09T15:23:16Z.
- Sumit Sinha, Debashish Chowdhury. TASEP on parallel tracks: effects of mobile bottlenecks in fixed segments. http://arxiv.org/abs/1409.2998v2; submitted 2014-09-10T09:10:19Z.
- Robert Juhasz, Ludger Santen. Dynamics of an exclusion process with creation and annihilation. http://arxiv.org/abs/cond-mat/0311208v2; submitted 2003-11-10T13:00:47Z.
- Gunter M. Schütz. On the phase transition in the sublattice TASEP with stochastic blockage. http://arxiv.org/abs/2006.05395v1; submitted 2020-06-09T16:45:30Z.
- Atri Goswami, Rohn Chatterjee, Sudip Mukherjee. Defect versus defect: stationary states of single file marching in periodic landscapes with road blocks. http://arxiv.org/abs/2402.08499v3; submitted 2024-02-13T14:53:18Z.
- Johannes Schmidt, Vladislav Popkov, Andreas Schadschneider. Defect-induced phase transition in the asymmetric simple exclusion process. http://arxiv.org/abs/1504.04652v1; submitted 2015-04-17T22:34:16Z.
- J. J. Dong, B. Schmittmann, R. K. P. Zia. Inhomogeneous exclusion processes with extended objects: The effect of defect locations. http://arxiv.org/abs/0710.3865v1; submitted 2007-10-20T19:05:46Z.
- Bartlomiej Waclaw, Justyna Cholewa-Waclaw, Philip Greulich. Totally asymmetric exclusion process with site-wise dynamic disorder. http://arxiv.org/abs/1809.05441v1; submitted 2018-09-14T14:27:39Z.
- Sourav Pal, Abhik Basu. Stationary densities in a weakly nonconserving asymmetric exclusion processes with finite resources. http://arxiv.org/abs/2602.08405v1; submitted 2026-02-09T09:06:52Z.
- J. Szavits-Nossan, K. Uzelac. Impurity-induced shocks in the asymmetric exclusion process with long-range hopping. http://arxiv.org/abs/0911.5280v1; submitted 2009-11-27T15:11:11Z.
- Hyungjoon Soh, Meesoon Ha. Passive Tracer Dynamics in Slow-Bond Problem. http://arxiv.org/abs/1905.00083v3; submitted 2019-04-30T20:05:10Z.
- Bijoy Daga, Souvik Mondal, Anjan Kumar Chandra, Tirthankar Banerjee, Abhik Basu. Nonequilibrium steady states in a closed inhomogeneous asymmetric exclusion process with particle nonconservation. http://arxiv.org/abs/1609.03814v1; submitted 2016-09-13T13:08:41Z.
- P. Pierobon, M. Mobilia, R. Kouyos, E. Frey. Bottleneck-induced transitions in a minimal model for intracellular transport. http://arxiv.org/abs/cond-mat/0604356v1; submitted 2006-04-13T17:43:13Z.
- Hyungjoon Soh, Meesoon Ha, Hawoong Jeong. Jamming and condensation in one-dimensional driven flow. http://arxiv.org/abs/1711.02728v4; submitted 2017-11-07T21:17:57Z.
- Philip Greulich, Andreas Schadschneider. Phase diagram and edge effects in the ASEP with bottlenecks. http://arxiv.org/abs/0711.3103v1; submitted 2007-11-20T10:37:41Z.
- R. M. Green. The nil Temperley--Lieb algebra of type affine C. http://arxiv.org/abs/1703.02609v4; submitted 2017-03-07T21:52:29Z.
- Cecile Appert-Rolland, Maximilian Ebbinghaus, Ludger Santen. Intracellular transport driven by cytoskeletal motors: General mechanisms and defects. http://arxiv.org/abs/1507.06166v1; submitted 2015-07-22T12:59:36Z.

### arxiv_removal.txt
- Yuliy Baryshnikov, Alexander Stolyar. Multi-floor generalization of TASEP. http://arxiv.org/abs/2603.13610v2; submitted 2026-03-13T21:38:05Z.
- Patrik L. Ferrari, Herbert Spohn, Thomas Weiss. Brownian Motions with One-Sided Collisions: The Stationary Case. http://arxiv.org/abs/1502.01468v1; submitted 2015-02-05T09:15:49Z.
- Peter Mottishaw, Bartlomiej Waclaw, Martin R. Evans. An exclusion process on a tree with constant aggregate hopping rate. http://arxiv.org/abs/1306.0360v4; submitted 2013-06-03T11:25:36Z.
- S. S. Poghosyan, A. M. Povolotsky, V. B. Priezzhev. Universal exit probabilities in the TASEP. http://arxiv.org/abs/1206.3429v2; submitted 2012-06-15T11:34:16Z.
- Jose Eduardo de Oliveira Rodrigues, Ronald Dickman. Asymmetric Exclusion Process in a System of Interacting Brownian Particles. http://arxiv.org/abs/1002.0273v1; submitted 2010-02-01T15:25:43Z.
- J. G. Brankov, N. C. Pesheva, N. Zh. Bunzarova. One-Dimensional Traffic Flow Models: Theory and Computer Simulations. http://arxiv.org/abs/0803.2625v1; submitted 2008-03-18T13:24:33Z.

### arxiv_halfline.txt
- Zongrui Yang. Limits of open ASEP stationary measures near a boundary. http://arxiv.org/abs/2402.13675v2; submitted 2024-02-21T10:19:37Z.
- Tomohiro Sasamoto, Lauren Williams. Combinatorics of the asymmetric exclusion process on a semi-infinite lattice. http://arxiv.org/abs/1204.1114v1; submitted 2012-04-05T02:54:28Z.
- Nils Haug, Sergei Nechaev, Mikhail Tamm. From generalized directed animals to the asymmetric simple exclusion process. http://arxiv.org/abs/1210.8060v6; submitted 2012-10-30T15:54:57Z.
- Vladislav Popkov, Mario Salerno, Gunter M. Schutz. Asymmetric simple exclusion process with periodic boundary driving. http://arxiv.org/abs/0811.1928v1; submitted 2008-11-12T16:15:35Z.

## Crossref returned records
Broad queries were noisy; irrelevant matches are listed to make the search reproducible. No exact killing-site theorem was identified in these records.

### crossref.json
- Linjie Zhao, Dayue Chen. The invariant measures and the limiting behaviors of the facilitated TASEP. DOI 10.1016/j.spl.2019.108557; publication date [[2019, 11]].
- Sudipto Muhuri. Scale-invariant density profiles of a dynamically extending TASEP. DOI 10.1209/0295-5075/101/38001; publication date [[2013, 2, 1]].
- . Quasiinvariant and invariant measures. DOI 10.1142/9789812816191_0003; publication date [[1998, 10]].
- Alfonso Sorrentino. Action-Minimizing Invariant Measures for Tonelli Lagrangians. DOI 10.23943/princeton/9780691164502.003.0003; publication date [[2017, 10, 19]].
- . Nonmeasurable sets with respect to quasiinvariant and invariant measures. DOI 10.1142/9789812816191_0005; publication date [[1998, 10]].
- . 7. Invariant and Relatively Invariant Measures on Locally Compact Groups and Spaces. DOI 10.1214/lnms/1215540662; publication date [[1990]].
- Ole E. Barndorff-Nielsen, Preben Blæsild, Poul Svante Eriksen. Invariant, relatively invariant, and quasi-invariant measures. DOI 10.1007/978-1-4612-3682-5_4; publication date [[1989]].
- Mouhamadou Sy. Invariant measures for Hamiltonian PDE. DOI 10.70675/b8adadf4ze6f5z422fzb167za59d2c1fbe93; publication date [[None]].
- Gerard Thompson. Killing Vector Fields of Invariant Metrics. DOI 10.3390/geometry2040017; publication date [[2025, 10, 22]].
- . Invariant and Quasi-invariant Measures. DOI 10.1017/9781009562256.005; publication date [[2024, 11, 30]].
- Paul Malliavin. Invariant or quasi-invariant probability measures for infinite dimensional groups. DOI 10.1007/s11537-008-0752-5; publication date [[2008, 3]].
- . Invariant measures. DOI 10.1017/cbo9780511623813.005; publication date [[1995, 4, 28]].
- . Review for "Data-driven discovery of invariant measures". DOI 10.1098/rspa.2023.0627/v2/review2; publication date [[2024, 2, 18]].
- . Review for "Data-driven discovery of invariant measures". DOI 10.1098/rspa.2023.0627/v1/review1; publication date [[2023, 11, 14]].
- . Review for "Data-driven discovery of invariant measures". DOI 10.1098/rspa.2023.0627/v2/review1; publication date [[2024, 2, 14]].
- Alexander Kharazishvili. Invariant and Quasi-Invariant Measures. DOI 10.1007/978-3-031-95369-9_21; publication date [[2025]].
- . Review for "Data-driven discovery of invariant measures". DOI 10.1098/rspa.2023.0627/v1/review2; publication date [[2023, 11, 27]].
- . Chad: Austerity measures killing students' dreams and ambitions. DOI 10.1163/2210-7975_hrd-9211-20180490; publication date [[None]].
- . Almost invariant sets. DOI 10.1142/9789812816191_0007; publication date [[1998, 10]].
- Cédric Bernardin, Patrícia Gonçalves, Claudio Landim. Entropy of Non-equilibrium Stationary Measures of Boundary Driven TASEP. DOI 10.1007/s10955-013-0882-x; publication date [[2013, 11, 20]].
- Shengzhong Chen. Automatic Continuities of Law-Invariant Risk Measures. DOI 10.32920/26064085; publication date [[2024, 6, 19]].
- Shengzhong Chen. Automatic Continuities of Law-Invariant Risk Measures. DOI 10.32920/26064085.v1; publication date [[2024, 6, 19]].
- . Chapter 3 Generalized Killing Equations. DOI 10.1016/s0076-5392(08)61832-9; publication date [[1977]].
- ANDRE RUBENS FRANCA CARNEIRO. SURFACE DIFFEOMORPHISMS WITH NON-TRIVIAL INVARIANT MEASURES. DOI 10.17771/pucrio.acad.12308; publication date [[None]].
- Ziye Zhu. Invariant Measures in Ergodic Theory. DOI 10.14418/wes01.1.3131; publication date [[None]].
- . Exponents and invariant measures. DOI 10.1017/cbo9781139976602.007; publication date [[2014, 7, 24]].
- . Existence of invariant measures. DOI 10.1017/cbo9781316422601.003; publication date [[2015, 11, 30]].
- Kazimierz Nikodem. On $\varepsilon$-invariant measures and a functional equation. DOI 10.21136/cmj.1991.102491; publication date [[1991]].
- Jialin Hong, Xu Wang. Invariant Measures and Ergodicity. DOI 10.1007/978-981-32-9069-3_1; publication date [[2019]].
- . Invariant Measures and Some Ergodic Theory for Random Dynamical Systems. DOI 10.4324/9780203219119_chapter_6; publication date [[None]].

### crossref_target.json
- . Deciphering Site-Specific Kinetics on Shaped Pd Nanocrystals via Single-Particle Electrocatalysis. DOI 10.1021/jacs.6c03289.s001; publication date [[None]].
- . Resistive Pulse Sensing on a Capillary-Assisted Microfluidic Platform for On-Site Single-Particle Analyses. DOI 10.1021/acs.analchem.3c02539.s001; publication date [[None]].
- . Correlating Acid Site Distribution and Catalytic Activity in Dealuminated Mordenite at the Single-Particle Level. DOI 10.1021/acscatal.0c04144.s001; publication date [[None]].
- Fabian H. L. Essler, Werner Krauth. Lifted TASEP: A Solvable Paradigm for Speeding up Many-Particle Markov Chains. DOI 10.1103/physrevx.14.041035; publication date [[2024, 11, 6]].
- . Improving Fine Particle Removal Using a Single-Channel Slit Bubbling Device in Wet Flue Gas Desulfurization System. DOI 10.1021/acsomega.3c08250.s003; publication date [[None]].
- . Improving Fine Particle Removal Using a Single-Channel Slit Bubbling Device in Wet Flue Gas Desulfurization System. DOI 10.1021/acsomega.3c08250.s002; publication date [[None]].
- . Improving Fine Particle Removal Using a Single-Channel Slit Bubbling Device in Wet Flue Gas Desulfurization System. DOI 10.1021/acsomega.3c08250.s001; publication date [[None]].
- Armin Saeedi Vahdat, Cetin Cetinkaya. Characterization of Single Particle Adhesion: A Review of Recent Progress. DOI 10.1002/9781118831571.ch4; publication date [[2015, 1, 19]].
- . Decision letter: TASEP modelling provides a parsimonious explanation for the ability of a single uORF to derepress translation during the integrated stress response. DOI 10.7554/elife.32563.029; publication date [[2017, 12, 6]].
- J.E. Brockmann, C.L.J. Adkins, F. Gelbard. Alternate particle removal technologies for the Airborne Activity Confinement System at the Savannah River Site. DOI 10.2172/7237439; publication date [[1991, 9, 1]].
- Chul-Un Ro. Single-particle characterization of aerosols collected at a remote site in the Amazonian rainforest and an urban site in Manaus, Brazil. DOI 10.5194/acp-2018-1067-ac1; publication date [[2019, 1, 18]].
- You Q, Feng X, Cai Y, Baylin SB, Li H. Single particle cryoEM data of Nucleosome core particle containing an 8-oxoG damage site. DOI 10.6019/empiar-12495; publication date [[2024, 12, 19]].
- . (no title). DOI 10.3030/101163231; publication date [[2025, 2, 1]].
- M. Takaffoli, M. Papini. Material deformation and removal due to single particle impacts on ductile materials using smoothed particle hydrodynamics. DOI 10.1016/j.wear.2011.08.012; publication date [[2012, 1]].
- C. Bahadoran, T. Bodineau. Quantitative estimates for the flux of TASEP with dilute site disorder. DOI 10.1214/18-ejp137; publication date [[2018, 1, 1]].
- . Review for "Moisture removal behaviour of single hard lignite particle during drying and quantitative characterization for its surface damage". DOI 10.1002/cjce.24315/v1/review2; publication date [[2021, 3, 23]].
- . Review for "Moisture removal behaviour of single hard lignite particle during drying and quantitative characterization for its surface damage". DOI 10.1002/cjce.24315/v1/review1; publication date [[2021, 2, 10]].
- . Review for "Moisture removal behaviour of single hard lignite particle during drying and quantitative characterization for its surface damage". DOI 10.1002/cjce.24315/v1/review3; publication date [[2021, 4, 2]].
- . Review for "Moisture removal behaviour of single hard lignite particle during drying and quantitative characterization for its surface damage". DOI 10.1002/cjce.24315/v2/review1; publication date [[2021, 7, 2]].
- V.S. Poghosyan, V.B. Priezzhev. The relaxation dynamics of the tasep with particle-dependent hopping probabilities on a ring. DOI 10.1016/s0034-4877(08)80012-2; publication date [[2008, 4]].
