# FEIB14 learnings for the launching session

PROVED: a read-once formula has an exact erasure witness consisting of the occupied-sibling bits along the literal-to-root path. This works for arbitrary gates and biased intermediate outputs. The bits can be much less information than all other spectral coordinates, yet preserve the posterior exactly. The proof is the cancellation of common factors in the biased disjoint-block spectral product. It makes the FLOW block suggestion precise; one block bit at one level is generally too coarse.

PROVED: the exact E_i composition recursion has two terms. Nonempty remaining sets inside the target block scale by the outer inclusion probability divided by child variance. An empty remaining set can activate the block when i is inserted, and gives a separate outer edge-entropy term. Omitting that activation term, or using the outer uniform spectrum with biased children, is wrong. composition.json supplies direct checks.

PROVED: the constant statistic already gives H,H^-<=2^(d-1)h(2^(1-d))I for degree-d Boolean functions, since every nonzero derivative has support at least 2^(1-d). This improves the granularity-only coefficient used by FEIB12 and also applies to depth-d trees. It is an elementary bound, not a novelty claim. It should be the first benchmark before trying a complicated degree-specific witness.

PROVED failures: optimizing every parity mask does not rescue parity-only witnesses. AND_n has cost/I=n/2+1+1/(2 ln 2)+o(1). Total cardinality also fails: adding independent spectral blocks hides the local membership signal, and XORs of many AND_w blocks make its cost approach h(delta)/delta. The true erasure remains the child's bounded value. Local block counts resolve that example. These are failures of the statistic, not FEI counterexamples.

CHECKED: on the NPN census through five variables, the parity-plus-block and subset-count families substantially reduce the largest coarse witness cost. The coordinatewise union is useful, but a finite bound is not evidence of a universal constant at that same value. FLOW's known general erasure lower bound is already larger than our finite-set maximum. No general bound for the union was proved.

PROVED: log-likelihood ratios are sufficient, and dyadic bins of the ratios increase cost by at most Inf_i. This gives a single general statistic template with O(n) bins, but it is spectrum-dependent and its required cost bound is equivalent to FEI. Calling that observation a universal cheap-witness solution would be circular.

CHECKED provenance scar: ../../inputs/fei_sym_v4/paper/main.tex is the 4.657435 version. The 4.650431 version is in ../FSYM47/repository/paper/main.tex and ../../inputs/fsym44_cert. inherited_audit.py independently reconstructs the rational seed and ledger and saves input hashes. A recalled number can be right while the first guessed file containing it is wrong.

CHECKED literature scar: WWW's 4I+2Cov protocol length counts ternary characters, not bits, and an empty-set charge remains. The correct explicit Shalev/WWW transfer used here is [2+(4+4sqrt(k))log_2 3]I. Also, the Upper Bounds paper has Kulkarni among its authors; the random-LTF paper has Karmalkar and Kundu. FMEI for a DNF class must not be promoted to Shannon FEI.

CHECKED recent source: the October 2026 threshold preprint explicitly states LTF and arbitrary-fan-in symmetric-threshold/parity read-once FEI bounds. Older handoffs saying these targets are open omit that cited result. This task verifies the theorem text and constants and gives the erasure transfer, but does not referee the complete new gate/antichain proof. Uniform all-monotone and unrestricted width-only DNF targets are still open in this report.

CHECKED numerical scar: the first NumPy mixed-integer matrix multiplication emitted invalid-operation warnings on this Mac. The final LTF generation uses elementwise products and sums, and final_audit.py reconstructs every score by sequential weighted addition and verifies all saved truth tables. No warned run is used as the final dataset. Above n=10, unsearched witness families are explicitly labelled candidate upper bounds and excluded from optimized maxima.

Brain recall helped locate the later symmetric certificate and the provisional monotone-DNF lead. The latter remains unverified here. The math store was unavailable. These learnings stay local because the fleet rules forbid shared-memory and mesh writes; the launching session can decide what to remember.
