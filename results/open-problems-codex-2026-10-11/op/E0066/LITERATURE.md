# E0066 literature audit — 2026-10-12

Verdict: NOT SOLVED_IN_LITERATURE. The source is an open-ended investigation. The later general finite-omega theorem and regularity criteria are substantial established structure, but no retrieved theorem states and proves a complete classification of the broad programme. No implication reconstructed here is counted as a solution in print.

## Source

R. N. Ganikhodzhaev and U. A. Rozikov, Quadratic Stochastic Operators: Results and Open Problems, arXiv:0902.4207 (2009), https://arxiv.org/pdf/0902.4207. Saved source.pdf and source.txt. Problem 13 is printed on PDF page 8; the complete-simplex definition is on page 7. QSO coefficient hypotheses are on pages 1–2.

> Problem 13. Investigate the behavior of trajectories of the bistochastic quadratic operators.

## Every HTTP query / fetch

- 2026-10-12: Full-text fetch https://arxiv.org/pdf/2001.10444, HTTP 200; saved regular.pdf and regular.txt.
- 2026-10-12: OpenAlex source identification https://api.openalex.org/works?search=Quadratic%20stochastic%20operators%20results%20and%20open%20problems&per-page=5, HTTP 200; saved openalex_source.json.

- 2026-10-12: ['source', 200, 165225, 'https://arxiv.org/pdf/0902.4207']
- 2026-10-12: ['arxiv', 200, 14586, 'https://export.arxiv.org/api/query?search_query=all:%22bistochastic%22+AND+all:%22quadratic%22&max_results=50']
- 2026-10-12: ['openalex', 200, 430400, 'https://api.openalex.org/works?search=quadratic%20bistochastic%20operators&per-page=30']
- 2026-10-12: ['crossref', 200, 223894, 'https://api.crossref.org/works?query=quadratic%20bistochastic%20operators&rows=30']
- 2026-10-12: ['semantic', 429, 174, 'https://api.semanticscholar.org/graph/v1/paper/search?query=quadratic%20bistochastic%20operators&limit=30&fields=title,year,authors,url,externalIds,abstract']
- 2026-10-12: ['github', 200, 55, 'https://api.github.com/search/repositories?q=quadratic+bistochastic+operators']
- 2026-10-12: {'service': 'citing_source', 'url': 'https://api.openalex.org/works?filter=cites:W1544252356&per-page=100', 'date': '2026-10-12', 'status': 200, 'bytes': 365967}
- 2026-10-12: {'service': 'citing_survey', 'url': 'https://api.openalex.org/works?filter=cites:W2081343974&search=bistochastic&per-page=100', 'date': '2026-10-12', 'status': 200, 'bytes': 453797}
- 2026-10-12: {'service': 'crossref_dynamics', 'url': 'https://api.crossref.org/works?query=trajectories%20doubly%20stochastic%20quadratic%20operators&rows=20', 'date': '2026-10-12', 'status': 200, 'bytes': 226158}
- 2026-10-12: {'service': 'arxiv_dynamics', 'url': 'http://export.arxiv.org/api/query?search_query=all:%22doubly+stochastic%22+AND+all:%22quadratic%22&max_results=30', 'date': '2026-10-12', 'status': 200, 'bytes': 58604}
- 2026-10-12: {'service': 'semantic_retry', 'url': 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2001.10444?fields=title,authors,year,abstract,citations.title,citations.year', 'date': '2026-10-12', 'status': 429, 'bytes': 174}
- 2026-10-12: ['saburov2016', 'https://iopscience.iop.org/article/10.1088/1742-6596/697/1/012014/pdf', 200, 14371]
- 2026-10-12: ['abdulghafor2016', 'https://www.degruyterbrill.com/document/doi/10.1515/math-2016-0045/pdf', 202, 0]
- 2026-10-12: ['abdulghafor_meta', 'https://api.openalex.org/works/https://doi.org/10.1515/math-2016-0045', 200, 16027]
- 2026-10-12: ['saburov_meta', 'https://api.openalex.org/works/https://doi.org/10.1088/1742-6596/697/1/012014', 200, 14258]

Semantic Scholar returned HTTP 429 on both attempts; no Semantic Scholar substantive evidence was recovered. GitHub returned zero repositories. OpenAlex source-citation search returned 24 records; the 2011 survey citation search was filtered by bistochastic. The metadata for Saburov contains an unrelated repository item about banana flour; that location was rejected without treating it as evidence. The IOP endpoint returned HTML rather than a PDF; the De Gruyter endpoint returned HTTP 202 and zero bytes. Neither counts as a paper read.

## Relevant references and exact status

Mirmukhsin Makhmudov, Description of the Set of Strictly Regular Quadratic Bistochastic Operators and Examples, Discontinuity, Nonlinearity, and Complexity 10(3) (2021), 425–433, DOI 10.5890/dnc.2021.09.006; arXiv:2001.10444v3 (11 January 2021). Full PDF retrieved as regular.pdf, text regular.txt.

Verbatim theorem text, with mathematical typography transcribed (PDF page 3):

> Theorem 2.1. [2] Let V : S^{m−1} → S^{m−1} be a quadratic bistochastic operator then:
> i) |ω_V(x_0)| < ∞, for ∀x_0 ∈ S^{m−1}, where ω_V(x_0) (ω−limit set of x_0) is the set of limit points of {V^n(x_0)}_{n=0}^∞;
> ii) P ◦ V is quadratic bistochastic operator for any coordinate permutation operator P : S^{m−1} → S^{m−1};
> iii) |Extr(B_m)| < ∞.

This theorem is quoted from reference [2], R. Ganikhodjaev, Doctoral thesis (1993), without proof in this paper. It has exactly the source object/hypotheses/initial-state quantifier but gives one structural conclusion rather than a complete answer to the broad investigation. The transition from finite omega-set to phase convergence is independently proved in ATTEMPT.md, not claimed as a theorem proved here in print.

> Theorem 2.2. ([7], [8]) Let V : S^{m−1} → S^{m−1} be a bistochastic operator, then V is regular if and only if it has no periodic points except fixed points.

Also PDF page 3; again attributed, not proved in this article.

> Theorem 3.3. Any operator in ri(B_m) is strictly regular.

PDF page 7; proved there using convex combinations and periodic-point inclusion. It addresses the relative interior of the operator polytope, not every operator. Corollary 3.3 (page 8) states density of strictly regular QBO. These are leads and known special/general structural results, not an exact-scope solution certificate.

Further exact references obtained from this paper and API metadata:

- M. Saburov, Dynamics of Double Stochastic Operators, Journal of Physics: Conference Series 697 (2016), 012014, DOI 10.1088/1742-6596/697/1/012014. Full text fetch blocked by HTML response.
- R. Abdulghafor, F. Shahidi, A. Zeki, S. Turaev, Dynamics of doubly stochastic quadratic operators on a finite-dimensional simplex, Open Mathematics 14 (2016), 509–519, DOI 10.1515/math-2016-0045. Full text unavailable from attempted endpoint; conclusions reported by earlier memo are unverified here beyond Makhmudov’s explicit attribution.
- M. Saburov, On Regularity of Diagonally Positive Quadratic Doubly Stochastic Operators, Results in Mathematics 72 (2017), 1907–1918, DOI 10.1007/s00025-017-0723-3. A subclass criterion; not fetched.
- M. Saburov, On Regularity of Positive Quadratic Doubly Stochastic Operators, Mathematical Notes 103 (2018), 328–333, DOI 10.1134/S0001434618010376. A subclass criterion; not fetched.
- R. Ganikhodzhaev and F. Shahidi, Doubly stochastic quadratic operators and Birkhoff’s problem, Linear Algebra and its Applications 432 (2010), 24–35, DOI 10.1016/j.laa.2009.07.002; arXiv:0802.1100. Structure of the coefficient polytope, a lead rather than trajectory classification.
- F. Shahidi, Doubly stochastic operators on a finite-dimensional simplex, Siberian Mathematical Journal 50 (2009); arXiv:1211.5639. Prior memo lead; not fetched in this check.
- F. Mukhamedov and A. F. Embong, On b-bistochastic quadratic stochastic operators, Journal of Inequalities and Applications (2015), DOI 10.1186/s13660-015-0744-y. Uses an unsorted partial-sum order, a different model; excluded from exact-scope evidence.

## Search result inventories


### openalex.json

- Mirmukhsin Makhmudov. Description of the Set of Strictly Regular Quadratic Bistochastic Operators and Examples. 2021. DOI: https://doi.org/10.5890/dnc.2021.09.006. OpenAlex: https://openalex.org/W3004055123.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. On b-bistochastic quadratic stochastic operators. 2015. DOI: https://doi.org/10.1186/s13660-015-0744-y. OpenAlex: https://openalex.org/W1896458915.
- Rasul Ganikhodzhaev. On the definition of bistochastic quadratic operators. 1993. DOI: https://doi.org/10.1070/rm1993v048n04abeh001058. OpenAlex: https://openalex.org/W2064278765.
- A.I. Eshniyоzov; T.А.Iskandarova. MODELS DESCRIBED BY BISTOCHASTIC QUADRATIC OPERATORS. 2022. DOI: https://doi.org/10.5281/zenodo.6419008. OpenAlex: https://openalex.org/W4226514521.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. b— Bistochastic Quadratic Stochastic Operators and Their Properties. 2016. DOI: https://doi.org/10.1088/1742-6596/697/1/012010. OpenAlex: https://openalex.org/W2320288045.
- Ahmad Fadillah Embong; Nur Natasha Lim Boon Chye Mohd Hairie Lim. Regularity of b-bistochastic-Volterra quadratic stochastic operators. 2022. DOI: https://doi.org/10.1063/5.0078952. OpenAlex: https://openalex.org/W4285295774.
- Ahmad Fadillah Embong; M. I. E. Zulkifly; D. N. A. Awg Arifin. Genetic Algebras generated by b−bistochastic Quadratic Stochastic Operators: The Character and Associativity. 2023. DOI: https://doi.org/10.47836/mjms.17.1.03. OpenAlex: https://openalex.org/W4362575149.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. On stable b-bistochastic quadratic stochastic operators and associated non-homogenous Markov chains. 2017. DOI: https://doi.org/10.1080/03081087.2017.1281215. OpenAlex: https://openalex.org/W2419215362.
- Azman, Abdurrahman; Wan Rozali, Wan Nur Fairuz Alwani. The rate of convergence of b-Bistochastic quadratic stochastic operator on 1-dimensional simplex. 2025. DOI: None. OpenAlex: https://openalex.org/W7112793757.
- Ahmad Fadillah Embong;  Nur Natasha Lim Boon Chye @ Mohd Hairie Lim. A Class of Two-Sex Population Quadratic Stochastic Operators: b-Bistochastic-Volterra. 2024. DOI: https://doi.org/10.17576/jqma.2001.2024.15. OpenAlex: https://openalex.org/W4392852955.
- Ahmad Fadillah Embong; Norhuda Afini Mohd Rosli. The fixed point of two-dimensional b−bistochastic quadratic stochastic operators and their dynamics. 2023. DOI: https://doi.org/10.1063/5.0165698. OpenAlex: https://openalex.org/W4386265107.
- Abdurrahman Azman; Wan Nur Fairuz Alwani Wan Rozali; Farrukh Maksutovich Mukhamedov. The Dynamics of Non-homogeneous Markov Chains Associated with the b-bistochastic Quadratic Stochastic Operators on 1-dimensional Simplex. 2026. DOI: https://doi.org/10.11113/mjfas.v22n1.4643. OpenAlex: https://openalex.org/W7131799377.
- Abdumalik I. Eshniyazov, Olimdjan G. Gaymnazarov, Utkir T. Davlatov,  Zuhra N. Obidova, Shakhnoza Khidirova. Extreme Points of the Set of Bistochastic Operators. 2023. DOI: None. OpenAlex: https://openalex.org/W7220530945.
- Otabek Khakimov; Sabokhat Eshmetova. Infinite-Dimensional Nonlinear Stochastic Operators: b-Bistochastic Case. 2025. DOI: https://doi.org/10.1007/s11117-025-01163-7. OpenAlex: https://openalex.org/W4416796897.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. On mixing of Markov measures associated with b−bistochastic QSOs. 2016. DOI: https://doi.org/10.1063/1.4952570. OpenAlex: https://openalex.org/W2415673656.
- Azam Abdurakhimovich Imomov; Abdumalik I. Eshniyazov. Infinite distohastic square operators in li. 2022. DOI: https://doi.org/10.17223/19988621/76/2. OpenAlex: https://openalex.org/W4320807761.
- Rasul Ganikhodzhaev; Farruh Shahidi. Doubly stochastic quadratic operators and Birkhoff’s problem. 2009. DOI: https://doi.org/10.1016/j.laa.2009.07.002. OpenAlex: https://openalex.org/W2051263599.
- Michał Badocha; Wojciech Bartoszek. Quadratic stochastic operators on Banach lattices. 2017. DOI: https://doi.org/10.1007/s11117-017-0522-9. OpenAlex: https://openalex.org/W2755190401.
- Farruh Shahidi. On infinite-dimensional dissipative quadratic stochastic operators. 2013. DOI: https://doi.org/10.1186/1687-1847-2013-272. OpenAlex: https://openalex.org/W2113772960.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nasir Ganikhodjaev. On nonhomogeneous geometric quadratic stochastic operators. 2022. DOI: https://doi.org/10.55730/1300-0098.3168. OpenAlex: https://openalex.org/W4285298137.
- Mansoor Khajibaevich Saburov. Ergodicity of p-majorizing quadratic stochastic operators. 2018. DOI: None. OpenAlex: https://openalex.org/W2918706903.
- Farrukh Mukhamedov; Abduaziz Abduganiev. On Kadison-Schwarz Type Quantum Quadratic Operators on. 2013. DOI: https://doi.org/10.1155/2013/278606. OpenAlex: https://openalex.org/W1728782796.
- Farruh Shahidi. Necessary and sufficient conditions for doubly stochasticity of infinite-dimensional quadratic operators. 2012. DOI: https://doi.org/10.1016/j.laa.2012.08.011. OpenAlex: https://openalex.org/W2021879318.
- Farrukh Maksutovich Mukhamedov; Izzat Qaralleh; Taimun Qaisar; M. A. K. Hasan. Genetic Algebras Associated with ξ(a)-Quadratic Stochastic Operators. 2023. DOI: https://doi.org/10.3390/e25060934. OpenAlex: https://openalex.org/W4380536631.
- M. A. Tadzhieva; Dilfuza Eshmamatova; Rasul Ganikhodzhaev. Volterra-type Quadratic Stochastic Operators with a Homogeneous Tournament. 2021. DOI: https://doi.org/10.22363/2413-3639-2021-67-4-783-794. OpenAlex: https://openalex.org/W4206950003.
- Mansoor Khajibaevich Saburov; Khikmat Khajibaevich Saburov. Ganikhodjaev's conjecture on mean ergodicity of quadratic stochastic operators. 2019. DOI: https://doi.org/10.56017/2181-1318.1032. OpenAlex: https://openalex.org/W2998532448.
- Sh. B. Abdurakhimova; Utkir Abdulloevich Rozikov. Dynamical system of a quadratic stochastic operator with two discontinuity points. 2021. DOI: https://doi.org/10.48550/arxiv.2103.14834. OpenAlex: https://openalex.org/W4301187254.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sherzod Turaev; Akram M. Zeki. Necessary and Sufficient Conditions for Complementary Stochastic Quadratic Operators of Finite-Dimensional Simplex. 2017. DOI: https://doi.org/10.30537/sjcms.v1i1.2. OpenAlex: https://openalex.org/W2794296397.
- Fatima T. Adilova; Uygun Umurovich Jamilov; Andrejs Reinfelds. ON DISCRETE-TIME MODELS OF NETWORK WORM PROPAGATION GENERATED BY QUADRATIC OPERATORS. 2023. DOI: https://doi.org/10.3846/mma.2023.15999. OpenAlex: https://openalex.org/W4328099301.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nasir Ganikhodjaev. Regularity of Geometric quadratic stochastic operator generated by 2-partition of infinite points. 2020. DOI: https://doi.org/10.11113/mjfas.v16n3.1737. OpenAlex: https://openalex.org/W3035091940.

### citing_source.txt

- Nasir Ganikhodjaev; Rasul Ganikhodjaev; Uygun Umurovich Jamilov. Quadratic stochastic operators and zero-sum game dynamics. 2014. DOI: https://doi.org/10.1017/etds.2013.109. OpenAlex: https://openalex.org/W1986168457.
- M. Ladra; Utkir Abdulloevich Rozikov. Evolution algebra of a bisexual population. 2013. DOI: https://doi.org/10.1016/j.jalgebra.2013.01.002. OpenAlex: https://openalex.org/W2964340998.
- Jochen Blath; Uygun Umurovich Jamilov; Michael Scheutzow. G,μ)-quadratic stochastic operators. 2014. DOI: https://doi.org/10.1080/10236198.2014.906591. OpenAlex: https://openalex.org/W2068209185.
- Uygun Umurovich Jamilov. Quadratic stochastic operators corresponding to graphs. 2013. DOI: https://doi.org/10.1134/s1995080213020042. OpenAlex: https://openalex.org/W2065976456.
- Mansoor Khajibaevich Saburov. On divergence of any order Cesàro mean of Lotka--Volterra operators. 2015. DOI: https://doi.org/10.15352/afa/06-4-247. OpenAlex: https://openalex.org/W1655907307.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sherzod Turaev. Consensus of fractional nonlinear dynamics stochastic operators for multi-agent systems. 2017. DOI: https://doi.org/10.1016/j.inffus.2017.11.003. OpenAlex: https://openalex.org/W2767251479.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sherzod Turaev; Adamu Abubakar; Akram M. Zeki. The Extreme Doubly Stochastic Quadratic Operators on Two Dimensional Simplex. 2015. DOI: https://doi.org/10.1109/acsat.2015.36. OpenAlex: https://openalex.org/W2394866025.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sherzod Turaev; Mohd Izzuddin. Nonlinear Consensus for Multi-Agent Systems using Positive Intractions of Doubly Stochastic Quadratic Operators. 2016. DOI: https://doi.org/10.31436/ijpcc.v2i1.30. OpenAlex: https://openalex.org/W2580793018.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sherzod Turaev; Akram M. Zeki; Adamu Abubaker. Nonlinear Convergence Algorithm: Structural Properties with Doubly Stochastic Quadratic Operators for Multi-Agent Systems. 2017. DOI: https://doi.org/10.1515/jaiscr-2018-0003. OpenAlex: https://openalex.org/W2766566522.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sherzod Turaev; Akram M. Zeki. Necessary and Sufficient Conditions for Complementary Stochastic Quadratic Operators of Finite-Dimensional Simplex. 2017. DOI: https://doi.org/10.30537/sjcms.v1i1.2. OpenAlex: https://openalex.org/W2794296397.
- Utkir Abdulloevich Rozikov; Shaheen Nazir. Separable quadratic stochastic operators. 2010. DOI: https://doi.org/10.1134/s1995080210030030. OpenAlex: https://openalex.org/W2020256906.
- Nasir Ganikhodjaev; Ramazon To’Xtayevich Muhitdinov; Mansoor Khajibaevich Saburov. ON LEBESGUE NONLINEAR TRANSFORMATIONS. 2017. DOI: https://doi.org/10.4134/bkms.b160212. OpenAlex: https://openalex.org/W2223169301.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sultan Almotairi; Hamad Almohamedh; Badr Almutairi; Abdullah Bajahzar; Sulaiman Sulmi Almutairi. A Nonlinear Convergence Consensus: Extreme Doubly Stochastic Quadratic Operators for Multi-Agent Systems. 2020. DOI: https://doi.org/10.3390/sym12040540. OpenAlex: https://openalex.org/W3015100875.
- Utkir Abdulloevich Rozikov; Akbar Zada. On a class of separable quadratic stochastic operators. 2011. DOI: https://doi.org/10.1134/s1995080211040196. OpenAlex: https://openalex.org/W1972299599.
- A. Yu. Khamrayev. On the Dynamics of a Quasistrictly Non-Volterra Quadratic Stochastic Operator. 2019. DOI: https://doi.org/10.1007/s11253-019-01712-w. OpenAlex: https://openalex.org/W2996909383.
- Farruh Shahidi. On infinite-dimensional dissipative quadratic stochastic operators. 2013. DOI: https://doi.org/10.1186/1687-1847-2013-272. OpenAlex: https://openalex.org/W2113772960.
- Nasir Ganikhodjaev; Mansoor Khajibaevich Saburov. On Rare Mutation, Chaos and Darwin's Theory. 2014. DOI: None. OpenAlex: https://openalex.org/W188297833.
- M. A. Tadzhieva; Dilfuza Eshmamatova; Rasul Ganikhodzhaev. Volterra-type Quadratic Stochastic Operators with a Homogeneous Tournament. 2021. DOI: https://doi.org/10.22363/2413-3639-2021-67-4-783-794. OpenAlex: https://openalex.org/W4206950003.
- Nasir Ganikhodjaev; Uygun Umurovich Jamilov. Contracting Quadratic Operators of Bisexual Population. 2012. DOI: https://doi.org/10.48550/arxiv.1204.0349. OpenAlex: https://openalex.org/W1769263789.
- Jochen Blath; Uygun Umurovich Jamilov; Michael Scheutzow. (G,μ)- Quadratic Stochastic Operators. 2013. DOI: https://doi.org/10.48550/arxiv.1307.1265. OpenAlex: https://openalex.org/W2083649573.
- M. Ladra; Utkir Abdulloevich Rozikov. Evolution algebra of a bisexual population. 2010. DOI: https://doi.org/10.48550/arxiv.1003.2541. OpenAlex: https://openalex.org/W2012248755.
- Utkir Abdulloevich Rozikov; Shaheen Nazir. Separable Quadratic Stochastic Operators. 2009. DOI: https://doi.org/10.48550/arxiv.0904.3688. OpenAlex: https://openalex.org/W2949938146.
- Utkir Abdulloevich Rozikov; M. M. Karimov. Dynamics of linear maps of idempotent measures. 2012. DOI: https://doi.org/10.48550/arxiv.1201.6183. OpenAlex: https://openalex.org/W2951566942.
- Nasir Ganikhodjaev; Mansoor Khajibaevich Saburov; Ashraf Mohamed Nawi. Mutation and Chaos in Nonlinear Models of Heredity. 2013. DOI: https://doi.org/10.48550/arxiv.1304.5710. OpenAlex: https://openalex.org/W2951868224.

### citing_survey.txt

- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. On b-bistochastic quadratic stochastic operators. 2015. DOI: https://doi.org/10.1186/s13660-015-0744-y. OpenAlex: https://openalex.org/W1896458915.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. b— Bistochastic Quadratic Stochastic Operators and Their Properties. 2016. DOI: https://doi.org/10.1088/1742-6596/697/1/012010. OpenAlex: https://openalex.org/W2320288045.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. On mixing of Markov measures associated with b−bistochastic QSOs. 2016. DOI: https://doi.org/10.1063/1.4952570. OpenAlex: https://openalex.org/W2415673656.
- Mirmukhsin Makhmudov. Description of the Set of Strictly Regular Quadratic Bistochastic Operators and Examples. 2021. DOI: https://doi.org/10.5890/dnc.2021.09.006. OpenAlex: https://openalex.org/W3004055123.
- Otabek Khakimov; Sabokhat Eshmetova. Infinite-Dimensional Nonlinear Stochastic Operators: b-Bistochastic Case. 2025. DOI: https://doi.org/10.1007/s11117-025-01163-7. OpenAlex: https://openalex.org/W4416796897.
- Farrukh Maksutovich Mukhamedov; Hasan Akın. Characterization of Bistochastic Kadison–Schwarz Operators on $$M_2(\mathbb C)$$. 2021. DOI: https://doi.org/10.1134/s0081543821020164. OpenAlex: https://openalex.org/W3216482688.
- Ahmad Fadillah Embong; M. I. E. Zulkifly; D. N. A. Awg Arifin. Genetic Algebras generated by b−bistochastic Quadratic Stochastic Operators: The Character and Associativity. 2023. DOI: https://doi.org/10.47836/mjms.17.1.03. OpenAlex: https://openalex.org/W4362575149.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. On stable b-bistochastic quadratic stochastic operators and associated non-homogenous Markov chains. 2017. DOI: https://doi.org/10.1080/03081087.2017.1281215. OpenAlex: https://openalex.org/W2419215362.
- Ahmad Fadillah Embong;  Nur Natasha Lim Boon Chye @ Mohd Hairie Lim. A Class of Two-Sex Population Quadratic Stochastic Operators: b-Bistochastic-Volterra. 2024. DOI: https://doi.org/10.17576/jqma.2001.2024.15. OpenAlex: https://openalex.org/W4392852955.
- Ahmad Fadillah Embong; Nur Natasha Lim Boon Chye Mohd Hairie Lim. Non-Associativity of two-dimensional b-Bistochastic-Volterra genetic algebra. 2024. DOI: https://doi.org/10.1063/5.0228101. OpenAlex: https://openalex.org/W4402511315.
- Ahmad Fadillah Embong; Norhuda Afini Mohd Rosli. The fixed point of two-dimensional b−bistochastic quadratic stochastic operators and their dynamics. 2023. DOI: https://doi.org/10.1063/5.0165698. OpenAlex: https://openalex.org/W4386265107.
- Nicolas Grosjean; Thierry Huillet; G. Rollet. On discrete evolutionary dynamics driven by quadratic interactions. 2016. DOI: https://doi.org/10.48550/arxiv.1607.01885. OpenAlex: https://openalex.org/W2950411684.
- Nicolas Grosjean; Thierry Huillet; G. Rollet. On discrete evolutionary dynamics driven by quadratic interactions. 2016. DOI: https://doi.org/10.1007/s12064-016-0232-z. OpenAlex: https://openalex.org/W2492202289.
- Sirojiddin Masharipov; A.I. Eshniyоzov. Constructing model of nonlinear operators with three-dimensional matrices. 2023. DOI: https://doi.org/10.1063/5.0113690. OpenAlex: https://openalex.org/W4327519909.
- Farrukh Maksutovich Mukhamedov; Chin Hee Pah; Azizi Rosli. On Non-ergodic Volterra Cubic Stochastic Operators. 2019. DOI: https://doi.org/10.1007/s12346-019-00334-8. OpenAlex: https://openalex.org/W2967747016.
- Rawad Abdulkhaleq Abdulmolla Abdulghafor; Sultan Almotairi; Hamad Almohamedh; Badr Almutairi; Abdullah Bajahzar; Sulaiman Sulmi Almutairi. A Nonlinear Convergence Consensus: Extreme Doubly Stochastic Quadratic Operators for Multi-Agent Systems. 2020. DOI: https://doi.org/10.3390/sym12040540. OpenAlex: https://openalex.org/W3015100875.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nasir Ganikhodjaev. On nonhomogeneous geometric quadratic stochastic operators. 2022. DOI: https://doi.org/10.55730/1300-0098.3168. OpenAlex: https://openalex.org/W4285298137.
- Izzat Qaralleh. Classification of a new subclass of ξ(as)-QSO and its dynamics. 2017. DOI: https://doi.org/10.22436/jmcs.017.04.08. OpenAlex: https://openalex.org/W2766070682.
- Farrukh Maksutovich Mukhamedov; Izzat Qaralleh; Taimun Qaisar; M. A. K. Hasan. Genetic Algebras Associated with ξ(a)-Quadratic Stochastic Operators. 2023. DOI: https://doi.org/10.3390/e25060934. OpenAlex: https://openalex.org/W4380536631.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nasir Ganikhodjaev. Regularity of Geometric quadratic stochastic operator generated by 2-partition of infinite points. 2020. DOI: https://doi.org/10.11113/mjfas.v16n3.1737. OpenAlex: https://openalex.org/W3035091940.
- Farruh Shahidi. On infinite-dimensional dissipative quadratic stochastic operators. 2013. DOI: https://doi.org/10.1186/1687-1847-2013-272. OpenAlex: https://openalex.org/W2113772960.
- Mansoor Khajibaevich Saburov; Khikmat Khajibaevich Saburov. Ganikhodjaev's conjecture on mean ergodicity of quadratic stochastic operators. 2019. DOI: https://doi.org/10.56017/2181-1318.1032. OpenAlex: https://openalex.org/W2998532448.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nurfarhana Nisa Muhammad Fauzi; Nasir Ganikhodjaev. New Class of 2-Partition Poisson Quadratic Stochastic Operators on Countable State Space. 2021. DOI: https://doi.org/10.1088/1742-6596/1988/1/012080. OpenAlex: https://openalex.org/W3194609334.
- Uygun Umurovich Jamilov; Farrukh Maksutovich Mukhamedov; Farzona Mukhamedova; Abdessatar Souissi. Dynamics of nonlinear stochastic operators and associated Markov measures. 2024. DOI: https://doi.org/10.1002/mma.10191. OpenAlex: https://openalex.org/W4397020817.
- Michał Badocha; Wojciech Bartoszek. Quadratic stochastic operators on Banach lattices. 2017. DOI: https://doi.org/10.1007/s11117-017-0522-9. OpenAlex: https://openalex.org/W2755190401.
- Fatima T. Adilova; Uygun Umurovich Jamilov; Andrejs Reinfelds. ON DISCRETE-TIME MODELS OF NETWORK WORM PROPAGATION GENERATED BY QUADRATIC OPERATORS. 2023. DOI: https://doi.org/10.3846/mma.2023.15999. OpenAlex: https://openalex.org/W4328099301.
- Farrukh Mukhamedov; Abduaziz Abduganiev. On Kadison-Schwarz Type Quantum Quadratic Operators on. 2013. DOI: https://doi.org/10.1155/2013/278606. OpenAlex: https://openalex.org/W1728782796.
- Farrukh Maksutovich Mukhamedov; Hasan Akın. Характеризация бистохастических операторов Кадисона-Шварца на $M_2(\mathbb C)$. 2021. DOI: https://doi.org/10.4213/tm4179. OpenAlex: https://openalex.org/W3174291515.

### crossref.json

- ['On the definition of bistochastic quadratic operators']; DOI 10.1070/rm1993v048n04abeh001058; {'date-parts': [[1993, 8, 31]]}
- ['A Class of Two-Sex Population Quadratic Stochastic Operators: b-Bistochastic-Volterra']; DOI 10.17576/jqma.2001.2024.15; {'date-parts': [[2024, 3, 16]]}
- ['On b-bistochastic quadratic stochastic operators']; DOI 10.1186/s13660-015-0744-y; {'date-parts': [[2015, 7, 21]]}
- ['Description of the Set of Strictly Regular Quadratic Bistochastic Operators and Examples']; DOI 10.5890/dnc.2021.09.006; {'date-parts': [[2021, 10, 1]]}
- ['<i>b</i>— Bistochastic Quadratic Stochastic Operators and Their Properties']; DOI 10.1088/1742-6596/697/1/012010; {'date-parts': [[2016, 3]]}
- ['The fixed point of two-dimensional b−bistochastic quadratic stochastic operators and their dynamics']; DOI 10.1063/5.0165698; {'date-parts': [[2023]]}
- ['Genetic Algebras generated by b−bistochastic Quadratic Stochastic Operators: The Character and Associativity']; DOI 10.47836/mjms.17.1.03; {'date-parts': [[2023, 3, 27]]}
- ['On stable <i>b</i>-bistochastic quadratic stochastic operators and associated non-homogenous Markov chains']; DOI 10.1080/03081087.2017.1281215; {'date-parts': [[2017, 1, 19]]}
- ['Regularity of b-bistochastic-Volterra quadratic stochastic operators']; DOI 10.1063/5.0078952; {'date-parts': [[2022]]}
- ['Infinite-Dimensional Nonlinear Stochastic Operators: b-Bistochastic Case']; DOI 10.1007/s11117-025-01163-7; {'date-parts': [[2025, 11, 28]]}
- ['The Dynamics of Non-homogeneous Markov Chains Associated with the  b-bistochastic Quadratic Stochastic Operators on 1-dimensional Simplex']; DOI 10.11113/mjfas.v22n1.4643; {'date-parts': [[2026, 2, 27]]}
- ['On a Random Ergodic Theorem for Bistochastic Operators']; DOI 10.1515/9783110889383.365; {'date-parts': [[1996, 12, 31]]}
- ['On the extreme points of the set of bistochastic operators']; DOI 10.1134/s0001434608090150; {'date-parts': [[2008, 10]]}
- ['Quadratic operators on AM-spaces']; DOI 10.3336/gm.48.2.12; {'date-parts': [[2013, 12, 16]]}
- ['Quantum Quadratic Stochastic Operators']; DOI 10.1007/978-3-319-22837-2_5; {'date-parts': [[2015]]}
- ['Infinite-Dimensional Quadratic Operators']; DOI 10.1007/978-3-319-22837-2_7; {'date-parts': [[2015]]}
- ['On bistochastic Kadison-Schwarz operators on<i>M</i><sub>2</sub>(ℂ)']; DOI 10.1088/1742-6596/435/1/012018; {'date-parts': [[2013, 4, 26]]}
- ['Quadratic Stochastic Operators and Their Dynamics']; DOI 10.1007/978-3-319-22837-2_2; {'date-parts': [[2015]]}
- ['SIX DIMENSIONAL ALGEBRAS GENERATED BY QUADRATIC STOCHASTIC OPERATORS']; DOI 10.29229/uzmj.2024-1-8; {'date-parts': [[2024]]}
- ['Quadratic Forms and Linear Operators']; DOI 10.1007/978-94-011-4619-7_2; {'date-parts': [[1999]]}
- ['Characterization of Bistochastic    Kadison–Schwarz Operators on $$M_2(\\mathbb C)$$']; DOI 10.1134/s0081543821020164; {'date-parts': [[2021, 7]]}
- ['Quantum Quadratic Stochastic Operators on $$\\mathbb{M}_{2}(\\mathbb{C})$$']; DOI 10.1007/978-3-319-22837-2_6; {'date-parts': [[2015]]}
- ['On the Description of Bistochastic Kadison–Schwarz Operators on 𝕄<sub>2</sub>(ℂ)']; DOI 10.1142/s1230161210000151; {'date-parts': [[2010, 9]]}
- ['О крайних точках множества бистохастических операторов', 'On the Extreme Points of the Set of Bistochastic Operators']; DOI 10.4213/mzm5545; {'date-parts': [[2008]]}
- ['On second order operators and quadratic operators']; DOI 10.1109/icpr.2008.4761685; {'date-parts': [[2008, 12]]}
- ['Hecke Operators']; DOI 10.1007/978-3-642-70341-6_4; {'date-parts': [[1987]]}
- ['Scalar approximants of quadratic operators with applications']; DOI 10.7153/oam-2018-12-16; {'date-parts': [[2018]]}
- ['Quadratic Operators and Quadratic Functional Equation']; DOI 10.1007/978-1-4614-3498-6_2; {'date-parts': [[2012]]}
- ['Integration of virtually continuous functions over bistochastic measures and the trace formula for nuclear operators']; DOI 10.1090/spmj/1394; {'date-parts': [[2016, 3, 30]]}
- ['Quadratic Stochastic Processes']; DOI 10.1007/978-3-319-22837-2_3; {'date-parts': [[2015]]}

### crossref_dynamics.txt

- ['On Regularity of Positive Quadratic Doubly Stochastic Operators']; DOI 10.1134/s0001434618010376; {'date-parts': [[2018, 1]]}
- ['Doubly stochastic quadratic operators and Birkhoff’s problem']; DOI 10.1016/j.laa.2009.07.002; {'date-parts': [[2010, 1]]}
- ['Dynamics of doubly stochastic quadratic operators on a finite-dimensional simplex']; DOI 10.1515/math-2016-0045; {'date-parts': [[2016, 1, 1]]}
- ['Nonlinear Consensus for Multi-Agent Systems using Positive Intractions of Doubly Stochastic Quadratic Operators']; DOI 10.31436/ijpcc.v2i1.30; {'date-parts': [[2016, 6, 17]]}
- ['Nonlinear Consensus Protocol Modified from Doubly Stochastic Quadratic Operators in Networks of Dynamic Agents']; DOI 10.3390/sym11121519; {'date-parts': [[2019, 12, 15]]}
- ['The Extreme Doubly Stochastic Quadratic Operators on Two Dimensional Simplex']; DOI 10.1109/acsat.2015.36; {'date-parts': [[2015, 12]]}
- ['Counting extreme U 1 matrices and characterizing quadratic doubly stochastic operators']; DOI 10.1007/s11464-016-0533-z; {'date-parts': [[2016, 3, 23]]}
- ['Periodic and Regular Trajectories of Non-Volterra Quadratic Stochastic Operators']; DOI 10.1134/s1995080223100219; {'date-parts': [[2023, 10]]}
- ['A Nonlinear Convergence Consensus: Extreme Doubly Stochastic Quadratic Operators for Multi-Agent Systems']; DOI 10.3390/sym12040540; {'date-parts': [[2020, 4, 3]]}
- ['The convergence consensus of multi-agent systems controlled via doubly stochastic quadratic operators']; DOI 10.1109/isamsr.2015.7379131; {'date-parts': [[2015, 8]]}
- ['SIX DIMENSIONAL ALGEBRAS GENERATED BY QUADRATIC STOCHASTIC OPERATORS']; DOI 10.29229/uzmj.2024-1-8; {'date-parts': [[2024]]}
- ['Global Stability of Quadratic Stochastic Operators Associated with Column Primitive Cubic Doubly Stochastic Matrices']; DOI 10.1007/978-3-032-09176-5_10; {'date-parts': [[2025]]}
- ['Asymptotical Behavior of Trajectories of Non-Volterra Quadratic Stochastic Operators']; DOI 10.1134/s1995080222140165; {'date-parts': [[2022, 11]]}
- ['Quantum Quadratic Stochastic Operators']; DOI 10.1007/978-3-319-22837-2_5; {'date-parts': [[2015]]}
- ['Quadratic Stochastic Operators and Their Dynamics']; DOI 10.1007/978-3-319-22837-2_2; {'date-parts': [[2015]]}
- ['Dynamics Classifications of Extreme Doubly Stochastic Quadratic Operators on 2D Simplex']; DOI 10.1007/978-3-319-24584-3_26; {'date-parts': [[2015, 12, 29]]}
- ['Nonlinear Convergence Algorithm: Structural Properties with Doubly Stochastic Quadratic Operators for Multi-Agent Systems']; DOI 10.1515/jaiscr-2018-0003; {'date-parts': [[2017, 11, 1]]}
- ['Quantum Quadratic Stochastic Operators on $$\\mathbb{M}_{2}(\\mathbb{C})$$']; DOI 10.1007/978-3-319-22837-2_6; {'date-parts': [[2015]]}
- ['On Regularity of Diagonally Positive Quadratic Doubly Stochastic Operators']; DOI 10.1007/s00025-017-0723-3; {'date-parts': [[2017, 7, 18]]}
- ['Majorization and doubly stochastic operators']; DOI 10.2298/fil1509087l; {'date-parts': [[2015]]}

### arxiv.xml

- http://arxiv.org/abs/2001.10444v3 — Description of the set of strictly regular quadratic bistochastic operators and examples; published 2020-01-26T04:45:00Z
- http://arxiv.org/abs/1601.04297v1 — Uniqueness of fixed points of $ b$-bistochastic quadratic stochastic operators and associated nonhomogenous Markov chains; published 2016-01-17T13:59:08Z
- http://arxiv.org/abs/2510.26574v3 — Accelerated decomposition of bistochastic kernel matrices by low rank approximation; published 2025-10-30T15:01:19Z
- http://arxiv.org/abs/1607.01885v1 — On discrete evolutionary dynamics driven by quadratic interactions; published 2016-07-07T06:55:58Z
- http://arxiv.org/abs/0806.2890v1 — Learning Graph Matching; published 2008-06-17T23:28:08Z
- http://arxiv.org/abs/2202.03237v1 — Introducing the Expohedron for Efficient Pareto-optimal Fairness-Utility Amortizations in Repeated Rankings; published 2022-02-07T14:43:35Z
- http://arxiv.org/abs/2307.09816v2 — Manifold Learning with Sparse Regularised Optimal Transport; published 2023-07-19T08:05:46Z

### arxiv_dynamics.txt

- http://arxiv.org/abs/0802.1100v1 — On doubly stochastic quadratic operators and Birkhoff's problem; published 2008-02-08T07:13:40Z
- http://arxiv.org/abs/2205.05289v1 — Backward doubly stochastic differential equations and SPDEs with quadratic growth; published 2022-05-11T06:34:58Z
- http://arxiv.org/abs/1809.07618v1 — On constructing orthogonal generalized doubly stochastic matrices; published 2018-09-20T13:42:35Z
- http://arxiv.org/abs/1005.4129v1 — Maximum Principle for Forward-Backward Doubly Stochastic Control Systems and Applications; published 2010-05-22T14:21:59Z
- http://arxiv.org/abs/1009.6061v4 — General Doubly Stochastic Maximum Principle and Its Applications to Optimal Control of SPDEs; published 2010-09-30T08:17:42Z
- http://arxiv.org/abs/1005.3085v2 — A maximum principle for controlled time-symmetric forward-backward doubly stochastic differential equation with initial-terminal sate constraints; published 2010-05-18T01:55:29Z
- http://arxiv.org/abs/2107.09631v1 — A Semismooth Newton-Type Method for the Nearest Doubly Stochastic Matrix Problem; published 2021-07-20T17:22:51Z
- http://arxiv.org/abs/2006.13439v1 — Riemannian Newton-CG Methods for Constructing a Positive Doubly Stochastic Matrix From Spectral Data; published 2020-06-24T03:00:24Z
- http://arxiv.org/abs/1108.5590v1 — Mean-Field Backward Doubly Stochastic Differential Equations and Applications; published 2011-08-29T14:59:29Z
- http://arxiv.org/abs/2509.23436v2 — LOTFormer: Doubly-Stochastic Linear Attention via Low-Rank Optimal Transport; published 2025-09-27T18:11:09Z
- http://arxiv.org/abs/1108.3153v1 — Differential games of partial information forward-backward doubly stochastic differential equations and applications; published 2011-08-16T05:02:29Z
- http://arxiv.org/abs/2603.14447v2 — Backward doubly stochastic differential equations with or without reflection under weak conditions; published 2026-03-15T15:44:46Z
- http://arxiv.org/abs/2304.02458v1 — Doubly Stochastic Matrix Models for Estimation of Distribution Algorithms; published 2023-04-05T14:36:48Z
- http://arxiv.org/abs/1609.00585v2 — Doubly stochastic large scale kernel learning with the empirical kernel map; published 2016-09-02T13:20:06Z
- http://arxiv.org/abs/2605.17883v1 — On the convergence of doubly stochastic Primal-Dual Hybrid Gradient Method; published 2026-05-18T05:43:50Z
- http://arxiv.org/abs/2304.00320v1 — Doubly Stochastic Models: Learning with Unbiased Label Noises and Inference Stability; published 2023-04-01T14:09:07Z
- http://arxiv.org/abs/1705.07765v1 — Exact Recovery with Symmetries for the Doubly-Stochastic Relaxation; published 2017-05-22T14:20:20Z
- http://arxiv.org/abs/2408.07871v2 — Monotonicity in Quadratically Regularized Linear Programs; published 2024-08-15T00:56:51Z
- http://arxiv.org/abs/2208.10149v6 — Hoffman-Wielandt type inequality for block companion matrices of certain matrix polynomials; published 2022-08-22T08:55:53Z
- http://arxiv.org/abs/1705.06148v1 — DS++: A flexible, scalable and provably tight relaxation for matching problems; published 2017-05-17T13:33:41Z
- http://arxiv.org/abs/2211.11751v2 — Denoising Multi-Similarity Formulation: A Self-paced Curriculum-Driven Approach for Robust Metric Learning; published 2022-11-19T15:28:19Z
- http://arxiv.org/abs/2210.11844v1 — Cox-Hawkes: doubly stochastic spatiotemporal Poisson processes; published 2022-10-21T09:47:34Z
- http://arxiv.org/abs/2606.15581v1 — Phase Transition in Convex Relaxations for Graph Alignment; published 2026-06-14T03:47:45Z
- http://arxiv.org/abs/1407.7585v1 — Lyapunov Approach to Consensus Problems; published 2014-07-28T22:03:39Z
- http://arxiv.org/abs/1807.06955v2 — Sinkhorn-Knopp Theorem for PPT states; published 2018-07-15T19:35:20Z
- http://arxiv.org/abs/0801.3654v2 — A path following algorithm for the graph matching problem; published 2008-01-23T20:20:32Z
- http://arxiv.org/abs/2608.16271v1 — Stochastic Gradient Tracking over Time-Varying Networks: One-Step Lyapunov Analysis; published 2026-08-17T08:44:34Z
- http://arxiv.org/abs/2411.10707v2 — Differentiable Extensions with Rounding Guarantees for Combinatorial Optimization over Permutations; published 2024-11-16T05:27:34Z
- http://arxiv.org/abs/2605.27430v4 — Lowering LCU Circuit Width through Maximum-Weight Birkhoff-von Neumann Decomposition; published 2026-05-22T04:29:13Z
- http://arxiv.org/abs/2403.12213v2 — Private graphon estimation via sum-of-squares; published 2024-03-18T19:54:59Z

## Read-only brain and earlier work

- brain.py recall: “quadratic bistochastic operators mistakes”, and “Trajectories of quadratic bistochastic operators”.
- brain.py node: audit_qso_barycenter_boundary_overstatement_2026_09_09. Its example f(t)=2t(1-t) has fixed endpoint 0; universal barycentre convergence is false.
- math_recall.py: “quadratic bistochastic trajectories majorization”. Retrieved generic doubly stochastic matrix card and mostly off-topic cards.
- rg E0066 in probability_1000_intake_* and codex_pool_2026_10_10 (first wildcard path attempt failed under Windows; reran using PowerShell directory enumeration).
- Read with git show origin/master: prob1000_lean_20260908/ultracode_20260909/E0066/memo.md and research7_2026-09-17/R7-01/admission/2026-09-19T181100Z__E0066_source_scope_gate.md. The former proves interior distinct-coordinate rigidity and leaves boundary periods unexplained. The latter confirms the broad endpoint and rejects promotion to a solved claim. Neither is publication evidence or an instruction governing this attempt.

## Follow-up brain queries, 2026-10-12

- math_recall.py: quadratic bistochastic periodic cycles repeated coordinates permutation majorization. Mostly off-topic averaging cards; no gap solution.
- brain.py recall: quadratic bistochastic repeated coordinates cycles gap mistakes. Boundary-scope caution, no gap solution.
- math_recall.py: Birkhoff von Neumann doubly stochastic equality Jensen permutation. Card claim_175fd53b84b64795985d832c226ffdbd states Birkhoff–von Neumann and cites Horn and Johnson, Matrix Analysis. A self-contained matching/decomposition proof is included in FOLLOWUP.md, so the recall is not treated as proof or publication evidence.

No new external HTTP literature search was made in the follow-up; it pursues the mathematical gap from the earlier checked source.
