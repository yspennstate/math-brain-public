# Historical four-problem target catalogue

**Inactive for the current scheduled fleet.** FEI-ALL-TEAM-20260922T095941Z assigns all eighty workers to FEI. Use [current research](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md) and [assignments](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/ASSIGNMENTS.json). FOREST, BT4, MOC4 and POS3 results are preserved; their suspension does not change their mathematical status.

## Preserved target definitions and source checks

# Source-exact targets and selection record

Owner-directed portfolio: COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z.
Primary-literature checks: 21 September 2026 UTC (22 September in the account timezone).
Scientific history snapshot: master 2d9669d532d826d4d41aa23b710a19b4566618b0.

These are research assignments, not claims of tractability, novelty, or new mathematical results. The selection aims at substantial specialist recognition without assigning another unrestricted flagship conjecture. Small parameters do not make an open problem easy. FOREST is the broadest new target; the other three fix a natural first unresolved regime. Exact source matching is more important than a promise about prestige or time to solution.

## FOREST — uniform-forest pairwise negative correlation

For every finite simple undirected graph G=(V,E), let F be uniformly chosen from ALL subsets of E for which (V,F) is acyclic. Isolated vertices, disconnected forests and the empty forest are allowed. Prove, for all distinct e,f in E,

    Pr(e,f in F) <= Pr(e in F) Pr(f in F).

Equivalently, if Z counts all forests, Z_e those containing e, and Z_ef those containing both, prove Z_e Z_f - Z Z_ef >= 0. A source-valid counterexample must include exact integer counts with a negative difference. The target is pairwise correlation at unit edge weights, not full negative association, all matroids, arbitrary positive weights, rooted forests, spanning trees, or forests with a fixed component count. Stronger statements may be tools only with separate hypotheses.

Primary sources checked:
- Grimmett and Winkler, Negative association in uniform forests and connected graphs, arXiv:math/0302185, Conjecture 1.1 and its forest-count formulation (pages 2-3): https://arxiv.org/pdf/math/0302185 . The connected-subgraph half is not this assignment.
- Grimmett, Selected problems in probability theory, arXiv:2205.07318, Conjecture 4.2, identified by the inherited exact-source claim.
- Tang and Zhang, Pairwise Negative Correlation for Uniform Spanning Subgraphs of the Complete Graph, arXiv:2603.10738 (11 March 2026): https://arxiv.org/abs/2603.10738 . Its sufficiently-large complete-graph and fixed-component/excess statements are NOT the all-graphs uniform-forest theorem.
- Bado, Negative edge correlation for uniform random forests on wheel graphs, Statistics & Probability Letters, online 6 September 2026, DOI 10.1016/j.spl.2026.110960: https://www.sciencedirect.com/science/article/pii/S016771522600324X . The introduction explicitly leaves the general conjecture open; all wheels are now covered. Do not rediscover that class as new.

Inherited work recovered: operations/claims/P0001.md; proofnet24/P14-probability-correlation/runs/; runs/R02/20260918T0024Z_8c7d1e52.md; runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md. The canonical P0001 claim retains a historical block-cycle-rank metric; it is not a current universal proof. Recover the latest relevant descendants before using a claimed class theorem or census. Do not reset old finite baselines or treat the search index as a complete history. New shared work uses proofnet24/P14-probability-correlation/collective-2026-09-22/.

Initial decisive problem: a valid global comparison/counting or decomposition argument for the actual unrooted measure, including overlapping cycles and separator compatibility. The known tree determinant, log-concavity of a related polynomial, and unproved weighted closure are not shortcuts to the target.

## BT4 — four vertex-disjoint directed cycles

For EVERY finite loopless digraph D with at most one arc per ordered pair of distinct vertices and minimum OUT-degree at least seven, prove the existence of four vertex-disjoint directed cycles. Opposite arcs are allowed; a directed digon counts as a cycle. Each cycle is genuinely directed in the original graph. The graph order is arbitrary, not a fixed finite search range.

Primary current source: Bessy, Muis, Sereni, Steiner and Wiederrecht, A relaxation of the Bermond-Thomassen conjecture, arXiv:2608.12948 (13 August 2026): https://arxiv.org/abs/2608.12948 . The retrieved author abstract explicitly says every k>=4 remains unresolved. It proves the 2k-1 threshold only with each cycle directed OR made directed by reversing one arc. That relaxed theorem, tournament cases, edge-disjoint cycles, or a larger degree threshold do NOT settle BT4. The k<=3 results are inputs, not new achievements.

This is deliberately k=4, not the all-k Bermond-Thomassen conjecture. It is a recognizable difficult first-parameter case. Initial mechanisms: minimal-counterexample reductions that preserve the seven-outdegree condition; cycle-packing exchanges that repair the lost out-neighbors; and a source-valid way to eliminate the reversed-arc defects in the recent relaxation. Simply deleting a shortest cycle without charging degree losses is not a proof.

Bounded repository search for Bermond/Thomassen returned no matching prior target. That is not an exhaustive no-history certificate. Check newer exact matches once before starting; inherit any compatible result rather than create a competing research restart. New root: proofnet24/collective-BT4/.

## MOC4 — the four-dimensional Marcus-de Oliveira conjecture

For all COMPLEX NORMAL 4-by-4 matrices A,B, with eigenvalues a_1,...,a_4 and b_1,...,b_4 counted with multiplicity, prove

    det(A+B) in conv{ product_(i=1)^4 (a_i+b_(sigma(i))) : sigma in S_4 }.

After diagonalizing, the candidate is the same assertion for det(diag(a)+U diag(b) U*) for every unitary U. The hull is the convex hull of 24 complex points, with repetitions allowed. Singular matrices and repeated eigenvalues are included, handled directly or by a justified limit. A separating-support-functional argument must cover every direction and the entire unitary group.

Primary sources checked:
- Bebiano and da Providencia, Revisiting the Marcus-de Oliveira Conjecture, Mathematics 13(5), 711 (22 February 2025), DOI 10.3390/math13050711: https://www.mdpi.com/2227-7390/13/5/711 . Author survey and accessible indexed text state the conjecture remains open and list proven special settings, including n=4 Householder instances. Direct page opening was rate-limited; exact-source indexed text was retrieved, not an independent review of every proof.
- Drury, The external vertices conjecture in case n=4, Electronic Journal of Linear Algebra 11 (2004), DOI 10.13001/1081-3810.1131: https://journals.uwyo.edu/index.php/ela/article/view/263 . Its abstract explicitly distinguishes the known 3-by-3 result, open n=4 problem, and a WEAKENED n=4 result proved there.
- Mulero-Martinez, A variational framework for determinantal inequalities of normal matrices: Successes and obstructions, Linear Algebra and its Applications 740 (1 July 2026), 19-38, DOI 10.1016/j.laa.2026.03.019: https://www.sciencedirect.com/science/article/pii/S0024379526001266 . The author abstract retains the general open problem and cautions against inferring the desired extremal conclusion from a first-order argument. A nonmonomial stationary point, or even a nonmonomial maximizer, is NOT by itself a counterexample to the hull assertion or to existence of another monomial maximizer.

Do not replace complex normal pairs by commuting/Hermitian pairs, assume arbitrary compound-minor arrays are realizable, or call Drury's weakened result the full n=4 theorem. Initial mechanisms: exact exterior-power/minor expansion retaining common-unitary compatibility, support-function geometry with second-order analysis, and rigorous candidate searches over true unitary matrices and spectra.

Bounded repository name searches returned no source-matching active MOC4 report; unrelated Marcus/Oliveira hits were not treated as matches. This is not exhaustive. New root: proofnet24/collective-MOC4/. No n>4 claim is required or implied.

## POS3 — balanced pairs in width-three posets

For EVERY finite partially ordered set P that is not a chain and has width at most three, prove that there are incomparable x,y such that

    1/3 <= Pr_L(x precedes y) <= 2/3,

where L is UNIFORM among all linear extensions of P. Width means the maximum antichain size; it is not order dimension or height. Every finite size is included. Equivalently define b(P)=max_(x||y) min(p_xy,1-p_xy) and prove b(P)>=1/3. Avoid carrying a source's different delta normalization into this formula.

Primary sources checked:
- Chan and Pak, Linear extensions of finite posets, EMS Surveys in Mathematical Sciences (2025), DOI 10.4171/EMSS/97; arXiv:2311.02743v2, Section 13, especially Conjecture 13.1 and Theorem 13.2: https://arxiv.org/pdf/2311.02743 . Width two, height two and several other structural cases are already known. This assignment selects the width-three regime of the recognized conjecture, not an invented finite exercise.
- Aires and Kahn, Balancing Extensions in Posets of Large Width, arXiv:2509.11549: https://arxiv.org/abs/2509.11549 . Large-width/minimal-set/height asymptotic results do not establish all width-three posets.
- Aires and Kahn, Variance vs. range for linear extensions, and balancing extensions in posets of bounded width, arXiv:2510.26134: https://arxiv.org/abs/2510.26134 . Bounded-width/high-variance progress is a relevant newer input, not automatic coverage of all cases.
- Kahn's Harvard-MIT seminar on 11 May 2026 explicitly still describes the general balancing conjectures as unresolved: https://www.math.harvard.edu/event/balancing-extensions-in-posets-of-large-width/ . The bounded targeted literature check did not recover a source-matching width-three proof. This is a selection check, not a guarantee against undiscovered later work.

Inherited exact-source claim: operations/claims/I0122.md, read at the scientific snapshot above; earlier root probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/rotations/I0122/. It records the general conjecture and a finite n_bal=14 frontier from Gupta, arXiv:2607.23926. Preserve that history; do not report its finite frontier as new or as width-three closure. The new scoped root is proofnet24/collective-POS3/ and must link that lineage. Existing scalar extremal examples are tests, not a proposed improved universal constant.

Initial mechanisms: encode extensions through a three-chain cover and actual weighted lattice paths; prove a comparison that survives the third-chain constraints; combine bounded-width/variance inputs with a proved treatment of the exceptional configurations. The induced ordering after deleting a chain need not be uniform; its multiplicity must be retained. A finite counterexample needs exact extension counts for EVERY incomparable pair. Counting many posets without a structural reduction remains auxiliary, not the campaign's objective.

## Selection limits and excluded detours

The searches covered the exact conjecture names, fixed-parameter scopes, recent primary literature and available repository matches/POSTED exclusions. They are bounded checks, not a worldwide status certificate. The 2025-2026 papers supply explicit open-problem context; the older papers fix definitions and known special cases. Read any theorem's complete proof and hypotheses before importing it into new mathematics.

No number-theory target, private-manuscript polishing target, easy textbook exercise, or new unrestricted Millennium/headline problem is assigned. Preserve all prior posted-claim exclusions. Several initially considered candidates had recent source-matching proof announcements and were screened out instead of being assigned from stale memory. A later credible solution to an assigned scope must be recorded, not ignored to preserve a task label.

The initial allocation of thirteen workers per target is a coordination choice. It is not an estimated probability of success, a completion deadline, or a claim that the four problems have equal difficulty. Only an actual source-matching proof or counterexample closes the selected scope.
