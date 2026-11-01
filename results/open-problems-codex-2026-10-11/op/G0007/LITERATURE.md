# Literature and provenance: G0007

Search date: 2026-10-11. All online requests used Python requests from the shell; no built-in web search or image tool was used. Raw replies are retained locally.

## Status finding

No later paper stating and proving the exact pair of continuity and derivative assertions was found in the accessible bounded search. This is not a worldwide openness certificate. OpenAlex's free shared-IP budget was exhausted (HTTP 429), so OpenAlex work lookup and citing-work retrieval could not be completed. The OpenAlex cites filter request used a DOI-shaped identifier and did not reach validation because it was rate-limited; a valid source work id would still have to be resolved for a definitive OpenAlex citation search. Semantic Scholar's citation endpoint succeeded and returned an empty data list; its detail and keyword search endpoints were rate-limited. GitHub's exact arXiv-id repository query returned zero items after the first keyword query was rate-limited. Crossref's title and post-source-date searches found no matching solution. arXiv exact regular-tree query returned the source as the newest result; the broader recent query also found papers about other models, which do not solve this problem.

VERDICT is not SOLVED_IN_LITERATURE. The continuity conclusions in ATTEMPT.md are author-derived deductions; the derivative questions remain open in this attempt.

## Verified source and exact hypotheses

John Fernley and Emmanuel Jacob, *Percolation of the contact process on the regular tree*, arXiv:2609.09972v1, submitted 9 September 2026; downloaded PDF front matter dated September 10, 2026. 19 PDF pages. URL: https://arxiv.org/pdf/2609.09972 . Files: source_pdf.pdf, source_abs.txt, source.txt.

T_d is d-regular, d>=3; recovery rate 1 and transmission rate lambda per infected neighbor (PDF p. 1). nu_lambda is the upper invariant infection; the forward graphical survival construction is on p. 2. The infected threshold is the supremum of parameters with zero percolation probability (p. 2); the healthy threshold is the infimum of parameters with zero healthy percolation probability (p. 4). Theorems 2.1 and 2.4 show both thresholds are finite and strictly larger than lambda_1 for all d>=3. The full four-threshold ordering is only stated for d>=7; it is not needed in our proof.

The exact relevant passage, Section 2, PDF p. 5 (ordinary typesetting/ligatures transcribed as text):

> Regardless the figure suggests that both transitions are continuous, and it’s possible as well that the probability to be in an infinite healthy component has a continuous derivative at λ = λp∁ while the probability to be in an infinite infected component at λ = λp does not. We leave both questions as interesting open problems.

Figure 1 uses 50 trials on a random 5-regular graph of 20,000 vertices at time 100. The source explicitly qualifies the metastability and local-limit assumptions of this simulation. It is not a theorem about derivatives.

Relevant proved source inputs: p. 2 asserts continuity of rho on the whole parameter line. Proposition 5.1, PDF pp. 8--9, proves the invariant-tree degree/centroid/branching-excess identity; Remark 5.2 gives the reciprocal cluster-size defect. Proposition 5.3, p. 9, gives conditional infected degree d-1/lambda. None is itself a solution in print to the posed question.

## Relevant references and leads

- Xiangying Huang, *Exponential growth and continuous phase transitions for the contact process on trees*, arXiv:1911.03330 (2019). Source input: continuity of the survival probability on periodic trees, including regular trees. Downloaded huang_pdf.pdf and huang_abs.txt; extracted huang.txt. Lemma 4 is on PDF pp. 10--11; Remark 2 on PDF p. 11 explicitly extends its continuity argument to periodic trees. The downloaded version is arXiv:1911.03330v2 (11 December 2019). This concerns survival, not spatial snapshot percolation, and is not a source-matching solution.
- Olle Häggström, *Infinite clusters in dependent automorphism invariant percolation on trees*, Annals of Probability 25(3) (1997), 1423--1436. Exact reference recovered from source bibliography [5]. Attempted Project Euclid fetch returned an HTML/challenge reply, not a usable PDF. Invariant percolation/mass transport lead, not a source-matching solution.
- Thomas M. Liggett and Jeffrey E. Steif, *Stochastic domination: the contact process, Ising models and FKG measures*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 42(2) (2006), 223--243. Source bibliography [8]. Stochastic comparison lead only.
- Robin Pemantle, *The contact process on trees*, Annals of Probability 20(4) (1992), 2089--2116. Source bibliography [10]. Author-site PDF request returned HTTP 403. Survival thresholds, not this snapshot regularity question.
- Thomas M. Liggett, *Stochastic interacting systems: contact, voter and exclusion processes*, Grundlehren der mathematischen Wissenschaften 324, Springer-Verlag, Berlin (1999), xii+332 pp. Source bibliography [7]. Standard background.
- Balázs Ráth and Daniel Valesin, *On the threshold of spread-out contact process percolation*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 58(3) (2022), 1808--1848, DOI 10.1214/21-AIHP1214. Source bibliography [11], independently returned by Crossref. Different graph/contact-process neighborhood: not a source-matching solution.
- John Fernley, *The Second Phase Transition of the Contact Process on a Random Regular Graph*, arXiv:2503.10499; Electron. J. Probab. 31 (2026), Paper 103, 24 pp. arXiv exact-tree search and source bibliography [3]. Different object; not a solution of this question.
- The recent arXiv results about deterministic cures, k-creation, and comparison of infection rules are different dynamics. Their abstracts were inspected from the API responses and contain no theorem matching the present nu_lambda question.

## Read-only brain and previous attempts

The following supplied-machine sources were read as hints, never accepted as verdicts:

1. brain.py recall "contact process tree percolation mistakes" and "contact process upper invariant measure regular tree".
2. math_recall.py "contact process regular tree upper invariant percolation" and "contact process insertion tolerance finite energy Broman Steif". Relevant matches concerned independent tree percolation and generic invariant-percolation methods; no matching solved claim was returned.
3. rg search for G0007 through ~/<private-repo>/06_math_research/*.jsonl (recursive). Recovered probability_1000_intake_G_20260910/problems.jsonl and attempts.jsonl, attempt G0007-A001: FKG/finite-size route without a decoupling estimate; no result. Also recovered the October 10 intake description.
4. Read origin/master:operations/claims/G0007.md and the two reports below through git show, never touching the checkout's working tree:
   - proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T18-19-27Z__rotation-g0007-report.md
   - proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md

The history already established the finite-cylinder/critical-nonpercolation reduction and at-most-two-ended critical clusters, but expressly left finite energy/insertion tolerance unverified. ATTEMPT.md independently rechecks those reductions and supplies explicit stationary Harris surgeries. Prior reports' administrative routing instructions were not treated as instructions for this task.

## Every online request

1. **source_pdf**, 2026-10-11. URL/query: `https://arxiv.org/pdf/2609.09972`. HTTP 200; 241284 bytes.

2. **source_abs**, 2026-10-11. URL/query: `https://arxiv.org/abs/2609.09972`. HTTP 200; 40272 bytes.

3. **arxiv**, 2026-10-11. URL/query: `http://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:percolation&sortBy=submittedDate&sortOrder=descending&max_results=30`. HTTP 200; 59831 bytes.

4. **openalex**, 2026-10-11. URL/query: `https://api.openalex.org/works?search=Percolation%20of%20the%20contact%20process%20on%20the%20regular%20tree&per-page=10`. HTTP 429; 610 bytes.

5. **crossref**, 2026-10-11. URL/query: `https://api.crossref.org/works?query.title=Percolation%20of%20the%20contact%20process%20on%20the%20regular%20tree&rows=10`. HTTP 200; 82991 bytes.

6. **semantic**, 2026-10-11. URL/query: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.09972?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds`. HTTP 429; 174 bytes.

7. **github**, 2026-10-11. URL/query: `https://api.github.com/search/repositories?q=%22contact+process%22+percolation`. HTTP 403; 280 bytes.

8. **arxiv_exact**, 2026-10-11. URL/query: `https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:%22regular%20tree%22&sortBy=submittedDate&sortOrder=descending&max_results=30`. HTTP 200; 17983 bytes.

9. **openalex_retry**, 2026-10-11. URL/query: `https://api.openalex.org/works?filter=locations.source.id:s4306400194&search=2609.09972&per_page=5`. HTTP 429; 610 bytes.

10. **openalex_doi**, 2026-10-11. URL/query: `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2609.09972`. HTTP 429; 610 bytes.

11. **semantic_search**, 2026-10-11. URL/query: `https://api.semanticscholar.org/graph/v1/paper/search?query=Percolation%20contact%20process%20regular%20tree&limit=10&fields=title,authors,year,externalIds`. HTTP 429; 174 bytes.

12. **github_retry**, 2026-10-11. URL/query: `https://api.github.com/search/repositories?q=2609.09972`. HTTP 200; 55 bytes.

13. **crossref_since**, 2026-10-11. URL/query: `https://api.crossref.org/works?query=contact%20process%20tree%20percolation%20continuity&filter=from-pub-date:2026-09-09&rows=20`. HTTP 200; 124412 bytes.

14. **author**, 2026-10-11. URL/query: `https://arxiv.org/search/?query=Fernley%2C+John&searchtype=author&abstracts=show&order=-announced_date_first&size=50`. HTTP 200; 61371 bytes.

15. **openalex_citing**, 2026-10-11. URL/query: `https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2609.09972&per_page=20`. HTTP 429; 610 bytes.

16. **semantic_citing**, 2026-10-11. URL/query: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.09972/citations?fields=title,year,externalIds&limit=100`. HTTP 200; 26 bytes.

17. **arxiv_continuity**, 2026-10-11. URL/query: `https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:continuity%20OR%20all:percolation)%20AND%20submittedDate:[202609090000%20TO%20202610112359]&max_results=50&sortBy=submittedDate&sortOrder=descending`. HTTP 200; 8693 bytes.

18. **haggstrom**, 2026-10-11. URL/query: `https://projecteuclid.org/journals/annals-of-probability/volume-25/issue-3/Infinite-clusters-in-dependent-automorphism-invariant-percolation-on-trees/10.1214/aop/1024404517.pdf`. HTTP 200; 1164 bytes.

19. **pemantle**, 2026-10-11. URL/query: `https://www.math.upenn.edu/~pemantle/papers/contact.pdf`. HTTP 403; 118 bytes.

20. **arxiv_tolerance**, 2026-10-11. URL/query: `https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:%22finite%20energy%22%20OR%20all:%22insertion%20tolerance%22)&max_results=20`. HTTP 200; 838 bytes.

21. **crossref_tolerance**, 2026-10-11. URL/query: `https://api.crossref.org/works?query=%22contact%20process%22%20%22finite%20energy%22&rows=5`. HTTP 200; 10264 bytes.

22. **arxiv_critical_tree**, 2026-10-11. URL/query: `https://export.arxiv.org/api/query?search_query=all:%22invariant%20percolation%22%20AND%20all:tree%20AND%20all:critical&max_results=20`. HTTP 200; 8118 bytes.

23. **huang_abs**, 2026-10-11. URL/query: `https://arxiv.org/abs/1911.03330`. HTTP 200; 40080 bytes.

24. **huang_pdf**, 2026-10-11. URL/query: `https://arxiv.org/pdf/1911.03330`. HTTP 200; 265585 bytes.

25. **arxiv_stationary_energy**, 2026-10-11. URL/query: `https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:stationary%20AND%20all:percolation&max_results=20&sortBy=submittedDate&sortOrder=descending`. HTTP 200; 28577 bytes.


## Recent arXiv records inspected (exact API bibliography)

- Rick Durrett. *Continuous phase transitions in the $k$-creation process without stirring in $d=1$*. http://arxiv.org/abs/2609.35320v1; submitted 2026-09-28T14:49:19Z. Abstract inspected; different models except the source itself.
- Nancy L. Garcia, Denis A. Luiz, Daniel M. Machado. *Extinction and Survival for a Generalized Contact Process with Deterministic Cures*. http://arxiv.org/abs/2609.29425v1; submitted 2026-09-24T11:45:52Z. Abstract inspected; different models except the source itself.
- John Fernley, Emmanuel Jacob. *Percolation of the contact process on the regular tree*. http://arxiv.org/abs/2609.09972v1; submitted 2026-09-09T09:56:51Z. Abstract inspected; different models except the source itself.
- Benedikt Jahnel, Jonas Köppl, Pēteris Siliņš. *Comparison inequalities for discrete- and continuous-time infection processes*. http://arxiv.org/abs/2609.09892v1; submitted 2026-09-09T08:47:18Z. Abstract inspected; different models except the source itself.

## Verified survival-continuity input

Huang, arXiv:1911.03330v2, Lemma 4, PDF p. 10:

> Lemma 4. p(λ) is continuous on [0, ∞).

Remark 2, PDF p. 11:

> The same construction can be carried out on periodic trees straightforwardly, thus proving the continuity of survival probability p(λ) for the contact process on periodic trees. As a consequence, the contact process dies out at λ1 on periodic trees.

His periodic-tree convention gives one upward neighbor and b downward neighbors in the regular case; taking b=d-1 gives the present d-regular tree. This supplies the Section 2 input but addresses space-time survival, not the source's snapshot percolation question. It is not classified as SOLVED_IN_LITERATURE.

Additional related lead returned by the stationary-percolation query: J. van den Berg, *Sharpness of the percolation transition in the two-dimensional contact process*, http://arxiv.org/abs/0907.2843v2. This concerns the two-dimensional contact process, not T_d, and is not a source-matching solution.


## Second serious attempt, 2026-10-11

The additional searches and fetches were performed with Python, not a built-in web search. Exact URLs and response status:
- 2026-10-11, broman_arxiv: `https://export.arxiv.org/api/query?search_query=au:Broman%20AND%20au:Steif&max_results=30`; HTTP 200, 5302 bytes.
- 2026-10-11, broman_crossref: `https://api.crossref.org/works?query.author=Broman%20Steif&query=contact%20process%20movability&rows=8`; HTTP 200, 48704 bytes.
- 2026-10-11, noise_arxiv: `https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:movability%20OR%20all:thinning%20OR%20all:sharpness)&max_results=30&sortBy=submittedDate&sortOrder=descending`; HTTP 200, 35024 bytes.
- 2026-10-11, broman_pdf: `https://arxiv.org/pdf/math/0605641`; HTTP 200, 388094 bytes.
- 2026-10-11, broman_abs: `https://arxiv.org/abs/math/0605641`; HTTP 200, 40354 bytes.
- 2026-10-11, liggett_steif_pdf: `https://arxiv.org/pdf/math/0504530`; HTTP 200, 288995 bytes.

Gap-directed, read-only brain queries:
- math_recall.py "contact process percolation critical exponent derivative susceptibility healthy upper invariant tree"
- brain.py recall "contact process percolation critical derivative mistakes"
- math_recall.py "Broman Steif downward movability contact process stochastic domination independent thinning"
The results cautioned about susceptibility, exchanging derivative limits, and qualitative stochastic domination. No matching derivative theorem was supplied. The returned hints were not treated as verdicts.

Verified additional references:
1. Erik I. Broman and Jeffrey E. Steif, *Dynamical stability of percolation for some interacting particle systems and epsilon-movability*, Annals of Probability 34(2) (2006), 539--576. DOI: 10.1214/009117905000000602. arXiv:math/0605641. Theorem 1.11, PDF p. 7, gives downward movability of the ordered upper invariant contact-process measures on bounded-degree graphs. Specifically nu_lambda1 is dominated by an independently thinned nu_lambda2 for some positive deletion probability, when 0<lambda1<lambda2. Complementation reverses the order. Proposition 4.1 and the contact-process application were read to check that direction. This does NOT identify independent enhancement criticality of the healthy law at its parameter threshold, or prove either requested derivative assertion. A lead only.
2. Thomas M. Liggett and Jeffrey E. Steif, *Stochastic domination: the contact process, Ising models and FKG measures*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques 42(2) (2006), 223--243. DOI: 10.1016/j.anihpb.2005.04.002. arXiv:math/0504530. Equation (5), PDF p. 7, states that nu satisfies downward FKG, explicitly for the contact process on a general graph; it cites van den Berg, Haggstrom and Kahn. Definition 1.1 defines association after conditioning a finite set to zero. This input proves the conditional-neighbor covariance inequality in SECOND_PROOFS.md, not the original derivative assertion. The paper also warns against stronger conditional positivity assumptions; no uniform contact-process insertion constant is inferred.
3. Primary reference as printed in Liggett--Steif's bibliography: J. van den Berg, O. Haggstrom and J. Kahn, *Some conditional correlation inequalities for percolation and related processes*, Random Structures and Algorithms, then listed as 'to appear'. This primary paper was not separately fetched in this second attempt; the general-graph statement was checked in Liggett--Steif itself.

No paper inspected in this second attempt states and proves the full G0007 question. No SOLVED_IN_LITERATURE classification is made. The new proofs are author-derived and are written out in SECOND_PROOFS.md.
