# Literature search

Search date: 2026-10-11 (session date).

- source: `https://arxiv.org/pdf/1705.04787` — OK 245224
- arxiv: `https://export.arxiv.org/api/query?search_query=all:%22Derrida-Retaux%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending` — OK 20454
- openalex: `https://api.openalex.org/works?search=Derrida%20Retaux&per-page=100` — <HTTPError 429: 'Too Many Requests'>
- crossref: `https://api.crossref.org/works?query=Derrida%20Retaux&rows=60` — OK 277053
- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Derrida%20Retaux&limit=100&fields=title,year,authors,abstract,externalIds,url` — <HTTPError 429: ''>
- github: `https://api.github.com/search/repositories?q=Derrida+Retaux&per_page=50` — OK 55
- stable: `https://arxiv.org/pdf/2006.06140` — OK 297385
- sustainability: `https://arxiv.org/pdf/2108.05610` — OK 469768
- openalex_retry: `https://api.openalex.org/works?search=A%20max-type%20recursive%20model&per_page=5` — <HTTPError 429: 'Too Many Requests'>
- openalex_citing: `https://api.openalex.org/works?filter=cites:W2609440919&per_page=100` — <HTTPError 429: 'Too Many Requests'>
- semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1705.04787?fields=title,citations.title,citations.year,citations.externalIds` — <HTTPError 429: ''>
- crossref_source: `https://api.crossref.org/works?query.title=A%20max-type%20recursive%20model%20some%20properties%20and%20open%20questions&rows=3` — OK 23049
- arxiv_http: `http://export.arxiv.org/api/query?search_query=all:%22Derrida%22+AND+all:%22Retaux%22&max_results=60` — OK 28063
- openalex_source_title: `https://api.openalex.org/works?filter=title.search:A%20max-type%20recursive%20model&per_page=5` — <HTTPError 429: 'Too Many Requests'>
- openalex_source_doi: `https://api.openalex.org/works/https://doi.org/10.1007/978-981-15-0302-3_6` — <HTTPError 429: 'Too Many Requests'>
- openalex_citing_doi: `https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1007%2F978-981-15-0302-3_6&per_page=100` — <HTTPError 429: 'Too Many Requests'>
- semantic_citing: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-981-15-0302-3_6/citations?fields=title,year,externalIds&limit=100` — OK 2973


## Search limitations and corrections

All URLs above are queries run from Python urllib on 2026-10-11. Raw successful responses are retained in this folder. OpenAlex consistently returned HTTP 429; its source and source-citing queries could not be inspected. The early OpenAlex `cites:W2609440919` call used an unverified candidate identifier and provides no source-citation evidence; discard that query for inference. After Crossref identified the exact source DOI, direct source lookup and citing-work queries with that DOI were attempted and also rate-limited. Semantic Scholar text and arXiv-paper queries returned 429, but its DOI-based citation endpoint succeeded. GitHub returned zero repositories for the stated query. No built-in web search was used.

## Verified source

Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits, Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787v2 (26 June 2019); in *Sojourns in Probability Theory and Statistical Physics III* (2019), pp. 166–186. DOI: 10.1007/978-981-15-0302-3_6.

PDF p. 1: “To avoid trivial discussions, we assume that X₀ is not almost surely a constant.” This standing hypothesis matters and is absent from the supplied transcription.

PDF p. 3, Conjecture 1 (text and formula transcribed, with mathematical superscripts restored):

> Conjecture 1. Assume (4). Then we have
> P(Xₙ ≠ 0) ∼ [4/(m − 1)²] [1/n²], n → ∞.

Condition (4) on that page is (m−1)E(X₀ m^{X₀}) = E(m^{X₀}) < ∞. The recursion is equation (1), PDF p. 1, with deterministic m≥2 independent copies and decrement 1.

PDF p. 4: “Possibly some additional integrability conditions, such as E(X₀³ m^{X₀}) < ∞ in Theorem 3 below, are necessary for our conjectures to hold.”

## Decisive external input; not a printed solution to D0056

Xinxing Chen and Zhan Shi, *The stable Derrida–Retaux system at criticality*, arXiv:2006.06140v1 (11 June 2020); *In and Out of Equilibrium 3: Celebrating Vladas Sidoravicius*, Progress in Probability (2020), pp. 239–264. DOI: 10.1007/978-3-030-60754-8_12.

PDF p. 3, Theorem 1.1, verbatim prose with mathematical formula layout restored:

> Theorem 1.1. Let (Yₙ, n ≥ 0) be such that (m − 1)E(Y₀ m^{Y₀}) = E(m^{Y₀}) < ∞. Under assumption (1.4), there exist constants c₂ ≥ c₁ > 0 such that for all n ≥ 1,
> c₁ n^{α−2} ≤ ∏_{i=0}^{n−1} [E(m^{Yᵢ})]^{m−1} ≤ c₂ n^{α−2}.

Assumption (1.4) is P(Y₀=k) ∼ c₀ m^{−k}k^{−α}, k→∞, for 2<α<4 and c₀>0. Page 1 additionally assumes P(Y₀≥2)>0 throughout. PDF p. 4 explicitly includes the case α=3. The upper-bound proof was checked on PDF pp. 20–21; its truncated third weighted moment is c(3n−1) for the explicit law here.

Application, line by line: ATTEMPT.md section 3 constructs a probability law with m=2, α=3, c₀=c>0, finite critical weighted first moment, and P(X₀≥2)>0. The theorem therefore gives Qₙ≤Cn. Sections 4–5 prove that qₙ∼4/n² would imply eₙ>3/(2n) eventually. Section 6 then gives Qₙ≥Kn^{3/2}, contradicting the published upper bound. The implication from survival to the incompatible product is proved in our note, not stated as this theorem in print; therefore the verdict is SOLVED, not SOLVED_IN_LITERATURE.

## Strongest directly relevant survival theorem inspected

Xinxing Chen, Yueyun Hu, Zhan Shi, *The sustainability probability for the critical Derrida–Retaux model*, arXiv:2108.05610v1 (12 August 2021); *Probability Theory and Related Fields* 182 (2022), 641–684. DOI: 10.1007/s00440-021-01091-z (online publication 19 October 2021).

PDF p. 3, Theorem 1.2 assumes E(t^{Y₀})<∞ for some t>m and gives P(Yₙ≥1)=n^{−2+o(1)} and E(Yₙ)=n^{−2+o(1)}. This has stronger hypotheses and no sharp multiplicative constant. It does not solve the exact question.

PDF p. 4 states that the universal coefficient should require E(Y₀³m^{Y₀})<∞; for m=2 and tails c₀ 2^{−k}k^{−α}, its equation (1.5) predicts coefficient α(α−2)/2. At α=3 this is 3/2. This prediction is not used as a theorem.

## All arXiv topic matches and their search summaries

The following exact bibliographic entries and abstracts came from the logged broad arXiv query; their presence does not certify a theorem. The unrelated exclusion-process match is omitted from the relevant-paper list.

- Xinxing Chen, Victor Dagard, Bernard Derrida, Yueyun Hu, Mikhail Lifshits, Zhan Shi. *The Derrida--Retaux conjecture on recursive models*. http://arxiv.org/abs/1907.01601v3, first submitted 2019-07-02. Search abstract: We are interested in the nearly supercritical regime in a family of max-type recursive models studied by Collet, Eckman, Glaser and Martin and by Derrida and Retaux, and prove that under a suitable integrability assumption on the initial distribution, the free energy vanishes at the transition with an essential singularity with exponent $\tfrac12$. This gives a weaker answer to a conjecture of Derrida and Retaux. Other behaviours are obtained when the integrability condition is not satisfied.

- Xinxing Chen, Yueyun Hu, Zhan Shi. *The dual Derrida-Retaux conjecture*. http://arxiv.org/abs/2306.12717v1, first submitted 2023-06-22. Search abstract: We consider a recursive system $(X_n)$ which was introduced by Collet et al. [10] as a spin glass model, and later by Derrida, Hakim, and Vannimenus [13] and by Derrida and Retaux [14] as a simplified hierarchical renormalization model. The system $(X_n)$ is expected to possess highly nontrivial universalities at or near criticality. In the nearly supercritical regime, Derrida and Retaux [14] conjectured that the free energy of the system decays exponentially with exponent $(p-p_c)^{-\frac12}$ as $p \downarrow p_c$. We study the nearly subcritical regime ($p \uparrow p_c$) and aim at a dual version of the Derrida-Retaux conjecture; our main result states that as $n \to \infty$, both $\E(X_n)$ and $¶(X_n\neq 0)$ decay exponentially with exponent $(p_c-p)^{\frac12 +o(1)}$, where $o(1) \to 0$ as $p \uparrow p_c$.

- Xinxing Chen, Zhan Shi. *The stable Derrida--Retaux system at criticality*. http://arxiv.org/abs/2006.06140v1, first submitted 2020-06-11. Search abstract: The Derrida--Retaux recursive system was investigated by Derrida and Retaux (2014) as a hierarchical renormalization model in statistical physics. A prediction of Derrida and Retaux (2014) on the free energy has recently been rigorously proved (Chen, Dagard, Derrida, Hu, Lifshits and Shi (2019+)), confirming the Berezinskii--Kosterlitz--Thouless-type phase transition in the system. Interestingly, it has been established in Chen, Dagard, Derrida, Hu, Lifshits and Shi (2019+) that the prediction is valid only under a certain integrability assumption on the initial distribution, and a new type of universality result has been shown when this integrability assumption is not satisfied. We present a unified approach for systems satisfying a certain domination condition, and give an upper bound for derivatives of all orders of the moment generating function. When the integrability assumption is not satisfied, our result allows to identify the large-time order of magnitude of the product of the moment generating functions at criticality, confirming and completing a previous result in Collet, Eckmann, Glaser and Martin (1984).

- Xinxing Chen. *Infinite differentiability of the free energy for a Derrida-Retaux system*. http://arxiv.org/abs/2405.09741v1, first submitted 2024-05-16. Search abstract: We consider a recursive system which was introduced by Derrida and Retaux (J. Stat. Phys. ${\bf 156}$ (2014) 268-290) as a toy model to study the depinning transition in presence of disorder. Derrida and Retaux predicted the free energy $F_\infty(p)$ of the system exhibit quite an unusual physical phenomenon which is an infinite order phase transition. Hu and Shi (J. Stat. Phys. ${\bf 172}$ (2018) 718-741) studied a special situation and obtained other behavior of the free energy, while insisted on $p=p_c$ being an essential singularity. Recently, Chen, Dagard, Derrida, Hu, Lifshits and Shi (Ann. Probab. ${\bf 49}$ (2021) 637-670) confirmed the Derrida-Retaux conjecture under suitable integrability condition. However, in the mathematical review, it is still unknown whether the free energy is infinitely differentiable at the critical point. So that, we continue to study the infinite differentiability of the free energy in this paper.

- Yueyun Hu, Bastien Mallein, Michel Pain. *An exactly solvable continuous-time Derrida--Retaux model*. http://arxiv.org/abs/1811.08749v2, first submitted 2018-11-21. Search abstract: To study the depinning transition in the limit of strong disorder, Derrida and Retaux (2014) introduced a discrete-time max-type recursive model. It is believed that for a large class of recursive models, including Derrida and Retaux' model, there is a highly non-trivial phase transition. In this article, we present a continuous-time version of Derrida and Retaux model, built on a Yule tree, which yields an exactly solvable model belonging to this universality class. The integrability of this model allows us to study in details the phase transition near criticality and can be used to confirm the infinite order phase transition predicted by physicists. We also study the scaling limit of this model at criticality, which we believe to be universal.

- Yueyun Hu, Zhan Shi. *The free energy in the Derrida--Retaux recursive model*. http://arxiv.org/abs/1705.03792v3, first submitted 2017-05-10. Search abstract: We are interested in a simple max-type recursive model studied by Derrida and Retaux (2014) in the context of a physics problem, and find a wide range for the exponent in the free energy in the nearly supercritical regime.

- Xinxing Chen, Yueyun Hu, Zhan Shi. *The sustainability probability for the critical Derrida-Retaux model*. http://arxiv.org/abs/2108.05610v1, first submitted 2021-08-12. Search abstract: We are interested in the recursive model $(Y_n, \, n\ge 0)$ studied by Collet, Eckmann, Glaser and Martin [9] and by Derrida and Retaux [12]. We prove that at criticality, the probability ${\bf P}(Y_n>0)$ behaves like $n^{-2 + o(1)}$ as $n$ goes to infinity; this gives a weaker confirmation of predictions made in [9], [12] and [6]. Our method relies on studying the number of pivotal vertices and open paths, combined with a delicate coupling argument.

- Zenghu Li, Run Zhang. *Asymptotic behavior of the generalized Derrida-Retaux recursive model*. http://arxiv.org/abs/2411.13068v3, first submitted 2024-11-20. Search abstract: We study the max-type recursive model introduced by Hu and Shi (J. Stat. Phys., 2018), which generalizes the model of Derrida and Retaux (J. Stat. Phys., 2014). The class of geometric-type marginal distributions is preserved by the model with a geometric offspring distribution. We give some long-time asymptotic expansions of the parameters of the marginal distribution. From the expansions, we derive the asymptotics of the sustainability probability, marginal distribution, first moment and probability generating function.

- Gerold Alsmeyer, Yueyun Hu, Bastien Mallein. *The Derrida-Retaux model on a geometric Galton-Watson tree*. http://arxiv.org/abs/2502.02991v2, first submitted 2025-02-05. Search abstract: We consider a generalized Derrida-Retaux model on a Galton-Watson tree with a geometric offspring distribution. For a class of recursive systems, including the Derrida-Retaux model with either a geometric or exponential initial distribution, we characterize the critical curve using an involution-type equation and prove that the free energy satisfies the Derrida-Retaux conjecture.

- Thomas Duquesne, Zhan Shi. *The continuous Derrida-Retaux branching process in the Brownian CRT*. http://arxiv.org/abs/2609.11435v1, first submitted 2026-09-10. Search abstract: The Derrida-Retaux continuous branching process, which is conjectured to be the scaling limit of the corresponding discrete model and of many other critical hierarchical renormalization models, is a process of cells evolving inhomogeneously on the time interval $[0, 1)$ via linear growth of each cell and independent splitting of cells at a specific rate. In this article, we show that the Derrida-Retaux continuous branching process is, on the one hand, encoded by a family of processes converging to a Brownian motion and on the other hand, fully obtained from the continuum Brownian tree encoded by the limiting Brownian path by time reversal and through length erasure of this tree. This direct representation explains the specific laws governing the significant quantities featuring the model (total mass, number of cells, law of large numbers) and provides a better understanding of its dynamics.

- Bernard Derrida, Zhan Shi. *Results and conjectures on a toy model of depinning*. http://arxiv.org/abs/2005.10208v1, first submitted 2020-05-20. Search abstract: We review recent results and conjectures for a simplified version of the depinning problem in presence of disorder which was introduced by Derrida and Retaux in 2014. For this toy model, the depinning transition has been predicted to be of the Berezinskii--Kosterlitz--Thouless type. Here we discuss under which integrability conditions this prediction can be proved and how it is modified otherwise.

- Zenghu Li, Run Zhang. *Derrida-Retaux type models and related scaling limit theorems*. http://arxiv.org/abs/2411.12189v2, first submitted 2024-11-19. Search abstract: We give characterizations of the transition semigroup and generator of a continuous-time Derrida--Retaux type process that generalizes the one introduced by Hu, Mallein and Pain (Commun. Math. Phys., 2020). It is shown that the process arises naturally as the scaling limit of the discrete-time max-type recursive models introduced by Hu and Shi (J. Stat. Phys., 2018).

- Xinxing Chen, Victor Dagard, Bernard Derrida, Zhan Shi. *The critical behaviors and the scaling functions of a coalescence equation*. http://arxiv.org/abs/2001.00853v1, first submitted 2020-01-03. Search abstract: We show that a coalescence equation exhibits a variety of critical behaviors, depending on the initial condition. This equation was introduced a few years ago to understand a toy model {studied by Derrida and Retaux to mimic} the depinning transition in presence of disorder. It was shown recently that this toy model exhibits the same critical behaviors as the equation studied in the present work. Here we find several families of exact solutions of this coalescence equation, in particular a family of scaling functions which are closely related to the different possible critical behaviors. These scaling functions lead to new conjectures, in particular on the shapes of the critical trees, that we have checked numerically.

- Alexey Lotnikov, Anna Kotova. *Criticality conditions in the Derrida-Retaux model with a random number of terms*. http://arxiv.org/abs/2502.02535v1, first submitted 2025-02-04. Search abstract: The article considers the Derrida-Retaux model with a random number of terms, i.e. a sequence of integer random variables defined by the relations $ X_{n + 1} = (X_n^{(1)} + X_n^{(2)} + ... + X_n^{(N_n)} - a)^{+}$, $n\ge 0$, where $X_n^{j}$ are independent copies of $X_n$, the values of $N_j$ are independent and identically distributed, $a$ is a positive integer. The energy in the model is defined as $Q:=\lim\limits_{n\to\infty} \frac{\mathbb{E}(X_{n})}{(\mathbb{E}N_1)^{n}}$. We present sufficient conditions (in terms of distributions of $X_0$ and $N_1$) for subcritical ($Q=0$) and supercritical ($Q>0$) regimes of model behavior.

- Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits, Zhan Shi. *A max-type recursive model: some properties and open questions*. http://arxiv.org/abs/1705.04787v2, first submitted 2017-05-13. Search abstract: We consider a simple max-type recursive model which was introduced in the study of depinning transition in presence of strong disorder, by Derrida and Retaux. Our interest is focused on the critical regime, for which we study the extinction probability, the first moment and the moment generating function. Several stronger assertions are stated as conjectures.

- Bernard Derrida, Martin Retaux. *The depinning transition in presence of disorder: a toy model*. http://arxiv.org/abs/1401.6919v1, first submitted 2014-01-27. Search abstract: We introduce a toy model, which represents a simplified version of the problem of the depinning transition in the limit of strong disorder. This toy model can be formulated as a simple renormalization transformation for the probability distribution of a single real variable. For this toy model, {the critical line is known exactly in one particular case} and it can be calculated perturbatively in the general case. One can also show that, at the transition, there is no strong disorder fixed distribution accessible by renormalization. Instead, both our numerical and analytic approaches indicate a transition of infinite order (of the Berezinskii-Kosterlitz-Thouless type). We give numerical evidence that this infinite order transition persists for the problem of the depinning transition with disorder on the hierarchical lattice.

- Anastasia Doikou, Simon J. A. Malham, Ioannis Stylianidis, Anke Wiese. *Applications of Grassmannian flows to coagulation systems*. http://arxiv.org/abs/2201.05487v2, first submitted 2022-01-14. Search abstract: We demonstrate how many classes of Smoluchowski-type coagulation models can be realised as multiplicative Grassmannian flows and are therefore linearisable, and thus integrable in this sense. First, we prove that a general Smoluchowski-type equation with a constant frequency kernel, that encompasses a large class of such models, is realisable as a multiplicative Grassmannian flow. Second, we establish that several other related constant kernel models can also be realised as such. These include: the Gallay--Mielke coarsening model; the Derrida--Retaux depinning transition model and a general mutliple merger coagulation model. Third, we show how the additive and multiplicative frequency kernel cases can be realised as rank-one analytic Grassmannian flows.

## Semantic Scholar source-citing works

{"paperId": "90b52cdc4a85c79d30d842e06d07702008196d84", "externalIds": {"ArXiv": "2411.13068", "DOI": "10.1007/s10955-025-03480-3", "CorpusId": 274150291}, "title": "Asymptotic Behavior of the Generalized Derrida–Retaux Recursive Model", "year": 2024}

{"paperId": "bda2fa4c104394ec8deed7fbef8ddfb8c4a1c202", "externalIds": {"ArXiv": "2405.09741", "DOI": "10.1007/s10114-026-4249-z", "CorpusId": 269790966}, "title": "Infinite Differentiability of the Free Energy for a Derrida–Retaux System", "year": 2024}

{"paperId": "548e53adc910f9c6fc0d2f777d94cce59cf51b2b", "externalIds": {"ArXiv": "2306.12717", "DOI": "10.1016/j.spa.2024.104332", "CorpusId": 259224678}, "title": "The dual Derrida–Retaux conjecture", "year": 2023}

{"paperId": "e740366745d4588a1e93b6242b322b130fdb043a", "externalIds": {"DOI": "10.1007/s00440-021-01091-z", "CorpusId": 253979633}, "title": "The sustainability probability for the critical Derrida–Retaux model", "year": 2021}

{"paperId": "fef35cdf7a13a1574f38742d64d892dd91a4b38c", "externalIds": {"ArXiv": "2108.05610", "DOI": "10.1007/s00440-021-01091-z", "CorpusId": 236987104}, "title": "The sustainability probability for the critical Derrida–Retaux model", "year": 2021}

{"paperId": "53e0c0788f3b852e57e5eff533b9e25ed4da6106", "externalIds": {"MAG": "3035673895", "ArXiv": "2006.06140", "DOI": "10.1007/978-3-030-60754-8_12", "CorpusId": 219573635}, "title": "The Stable Derrida–Retaux System at Criticality", "year": 2020}

{"paperId": "f2b6753f0f9a8c2f905d15e442c2efc4e2705d84", "externalIds": {"MAG": "3028159918", "ArXiv": "2005.10208", "DOI": "10.17323/1609-4514-2020-20-4-695-709", "CorpusId": 218719344}, "title": "Results and Conjectures on a Toy Model of Depinning", "year": 2020}

{"paperId": "e830fc9ef32c49666c788ed70d62a57e4a0e425a", "externalIds": {"ArXiv": "2005.06018", "MAG": "3024516091", "DOI": "10.1214/23-aop1653", "CorpusId": 218614042}, "title": "Particle density in diffusion-limited annihilating systems", "year": 2020}

{"paperId": "8d953e09564ecead4e6aec38050dadf4f3b90bf6", "externalIds": {"MAG": "2997148878", "ArXiv": "2001.00853", "DOI": "10.1088/1751-8121/ab8134", "CorpusId": 209832550}, "title": "The critical behaviors and the scaling functions of a coalescence equation", "year": 2020}

{"paperId": "7a2d2d0c1df01eb9915a15ae3df13e2b0c15fdbc", "externalIds": {"MAG": "2953424202", "ArXiv": "1907.01601", "DOI": "10.1214/20-AOP1457", "CorpusId": 195791617}, "title": "The Derrida–Retaux conjecture on recursive models", "year": 2019}

{"paperId": "f8a0556d18df6d06597bb0a429999f6f9c9cb9bf", "externalIds": {"CorpusId": 250454995}, "title": "Submitted to the Annals of Probability THE DERRIDA – RETAUX CONJECTURE ON RECURSIVE MODELS By", "year": 2020}

## Read-only earlier work and its audit

The intake directories were searched with rg for D0056; the prior attempt D0056-A001 was read. Its claim that eₙ∼2/((m−1)n) automatically yields the survival constant by taking differences is unsupported without additional regularity. The present persistent-gap proof avoids that issue.

Read-only git tree search and `git show origin/master:research7_2026-09-17/R7-02/paper_d0059_stable_tail_refutation/main.tex` retrieved the earlier D0059 stable-tail argument; a read-only copy is in prior_D0059_readonly.txt. Its explicit normalization and product-exponent argument were checked independently. That result concerns endpoint generating functions, not survival, so it is a lead rather than a previously proved D0056 answer.

Brain topic and mistakes recall and math-store recall were run as requested. They found no directly relevant theorem card. No brain/store/ledger/repository writes were intentionally made.

## Status conclusion

No fetched paper was found to state and prove the exact survival assertion under exactly the original hypotheses. Current evidence instead supports the counterexample proved in ATTEMPT.md. The stronger finite-third-weighted-moment question is outside the solved claim; the bounded and partially rate-limited search does not establish its current global status.

Additional during-attempt read-only math-store query (2026-10-11): `Chen Shi stable Derrida Retaux system criticality`; results were word matches for unrelated Chen/Shi papers and stable-distribution material, not a usable Derrida–Retaux theorem.
