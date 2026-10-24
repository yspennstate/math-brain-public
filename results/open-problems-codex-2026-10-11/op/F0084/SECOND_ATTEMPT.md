# Second serious attempt — 2026-10-11

The first attempt's gap is quantitative control near criticality of noncritical exponential constants, or a spatial multiscale estimate directly at criticality. The small-distance formula and abstract nearcritical comparison do not bridge it.

## Two new approaches

1. **Finite-window certificates using monotonicity in centres.** Remove all centres outside a deterministic box and compute the finite-centre stable allocation against all Lebesgue sites. Adding centres makes every site's assignment distance shorter (source Proposition 21). Thus a finite-window assignment of the origin gives a rigorous certificate valid regardless of centres outside. Unlike the previous comparison in appetite, this uses a purely local Poisson input. Try bounding the probability of no certificate at scale L, and determine whether the finite-centre allocation admits an effective truncation and volume computation.

2. **Transfer the stable two-colour Poisson matching multiscale argument.** Holroyd–Pemantle–Peres–Schramm's *Poisson Matching* gives power-law upper tails for two-colour stable point matching. In the allocation problem, sites assigned beyond r and centres whose territories extend beyond r cannot lie within distance r of each other. This resembles the separation of unmatched points in the matching proof. Try transferring its packing/renormalization estimate, or discretizing Lebesgue into very fine sites with many slots at each centre. Audit whether diffuse mass and unequal local capacities invalidate the counting argument or make constants diverge.

Approach 2 is initially more promising because its neighbouring theorem supplies a quantitative power law rather than another qualitative continuity statement. It will be pursued first; approach 1 is a fallback if the transfer breaks at an identifiable step.

## Brain query on the actual gap

Read-only math_recall.py query `replete boxes critical stable allocation quantitative Hoffman Holroyd Peres` returned unrelated cards (Hoffman–Wielandt, occupancy boxes, general stable distributions). A second query `Holroyd Pemantle Schramm Poisson Matching power law upper bound` also returned no matching theorem card. No card was used as evidence.

## Potential decisive lead — saved immediately

The PDF of *Poisson Matching*, arXiv:0712.1867v3, downloaded successfully. Theorem 19, PDF pp.29–33, proves polynomial tails for two-colour stable point matching. The remark on PDF p.34 explicitly says to adapt it to stable allocation of Lebesgue to Poisson by replacing point counts with site volumes and centre territory-tail volumes, and says mass transport gives the analogue of its inequality (23). This is potentially sufficient for the original problem, but the transfer is being checked independently before assigning a solved verdict.

The previously unretrieved paper *Hyperuniform and rigid stable matchings*, arXiv:1810.00265v3, was also obtained. Its abstract and Theorem 5.1 (PDF p.13) concern stable matching of a lattice to a point process of intensity strictly greater than one. It does not provide the critical continuum allocation theorem requested here.

## Transfer checked: the decisive weighted argument works

The matching paper's “Extensions to other processes” (PDF pp.7–8) expressly states that Theorem 6(ii) extends to fair Poisson–Lebesgue allocation and identifies X as the origin's site distance. This is a statement of the exact upper-bound answer, not merely a theorem about a neighbouring object. Exact quotations and the hypothesis map are now saved at the top of LITERATURE.md.

The tempting obstruction that centre maximum-radius tails differ from site tails is avoided by using *volume of the far part of each centre's territory*. Its Palm expectation is exactly the site tail. The stability exclusion, weighted flow balance, and expectation equality all hold. An independent derivation in SOLUTION.md proves the explicit weaker exponent 1/(4d), with an explicit finite constant K_d. Thus approach 2 succeeds. Approach 1 is not needed to resolve the question and has not been developed into a claimed new theorem.

The optimum tail exponent remains outside the resolved scope. The honest verdict for the source's explicitly requested quantitative upper bound is SOLVED_IN_LITERATURE, rather than a claimed novel solution.

The published journal PDF was then obtained directly from Numdam, HTTP 200. It independently confirms Theorem 6(ii) on printed p.269, the exact same-model extension on p.270, and the proof remark on p.286. Its reference [11] is the original 2006 HHP source, and [10] is HHP's tail-bounds paper. Thus this is an answer in the actual published paper, not only in a preprint. The two arXiv downloads and journal download are recorded in second_search_log.json and in LITERATURE.md.

Hostile finite checks completed: 3,600 ball/origin combinations in 30 finite stable critical allocations obeyed the flow identities, exclusion, and inequality. The contraction constant was numerically checked in six dimensions, while the uniform bound was proved analytically. No finite experiment is used to assert an infinite-model limit.

2026-10-12 final verification: re-read the complete independent proof and the actual journal theorem, extension and adaptation remark. No gap found for the any-upper-bound question. The resumed Lean check waited 420 seconds for a slot and then completed with exit code 0 for the weighted-flow and dyadic-induction lemmas; see LEAN_CHECK.md for scope. The old literature conclusions and route-specific gap are explicitly marked historical. The attempt closes as SOLVED_IN_LITERATURE. The sharp exponent and asymptotic equivalence have not been established by this work.
