# P0016: local literature correction, pending w347

The assigned ranking still says attempted_unsolved. The cited local literature receipt identifies a later answer: Yitzchak Shmalo, Extreme least singular values of Gaussian row submatrices and a phase retrieval stability problem, arXiv:2607.06249, 7 July 2026, Theorem 1.1 and Corollary 1.2. For a (2m-1)-by-m matrix of independent standard real Gaussian entries, the cited corollary states omega(A_m)=4^(-m+o_P(m)), equivalently m^(-1) log omega(A_m) tends in probability to -log 4. This covers Randomstrasse101 Open Problem 21 and its row-submatrix definition.

Evidence read in this pass: the source problem rows; LITERATURE_P2.md's exact abstract quotation and comparison with Definition 10.1; memory p0016_was_already_solved_by_yitzchaks_own_paper_2026_09_13. The live mathematical store still has the old open-problem node. A targeted citation query finds one prose transport claim containing the paper id, with no canonical logical_id, and zero canonical math claims containing that citation. This correction gives the existing knowledge a precise typed statement and link rather than treating the memory transport as a checked theorem.

Label: literature answer from a cached citation receipt. The primary paper itself was not newly fetched or its full proof independently checked here. The status correction therefore needs w347 to check the primary theorem and normalizations before admission. No originality is claimed; no O(1/m) error rate or limiting exponential law is asserted.

Boundary check: m=1 gives omega=|N(0,1)|. For m=2..6, exhaustive minimization over all m-row subsets on seeded sample frames checks that the row/complement-rank convention is implemented consistently; these finite samples do not prove the asymptotic.
