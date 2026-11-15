# FEIB21 results

Work in progress. Every theorem will be labelled in PROOFS.md; numerical evidence will be saved with commands.

The supplied model self-test passes (tree_selftest.log), including independent truth-table Fourier evaluation and all supplied mate-window checks. PROOFS.md sections 1–2 give an explicit error estimate proving E_root/Inf_root -> 2 in the balanced regime. Section 3 extends the same proof to monotone uniform DNFs with acyclic incidence graphs; cycles remain a real gap for the larger linear-hypergraph target.

The one-mate witness grows as log2 D+O(1), and the two-mate witness is bounded in the balanced regime; explicit finite bounds and the full-window/mate-window distinction are now in PROOFS.md sections 4–7. The candidate sharp two-mate limit is 2+7lambda/16, labelled HEURISTIC. The compressed evaluator agrees with the supplied code on all tested r=1,2,3 values; tensor_validate.json gives residuals.

PROVED: in the unbalanced scaling D^2 2^-L -> c>0, root erasure still tends to 2, but every fixed mate window diverges for every mate order, with an explicit positive logarithmic lower coefficient (PROOFS.md section 8). This does not optimize over other coordinates or arbitrary leaf interleavings.

An exact subset dynamic program now minimizes full r-windows over all orders. windows_scan.json contains the finite search, including a 22-variable transitive cyclic DNF and the PM(K33) host. It found no universal minimum-coordinate refutation.

The cycle gap mentioned earlier is now removed in a quantified sparse range. PROOFS.md section 12 proves (LIN) for every monotone uniform linear DNF, without branch independence. For any fixed epsilon>0 and D<=2^((1-epsilon)(w-1)), every live coordinate has E_i/Inf_i ->2 uniformly in the number of terms. The explicit finite coefficient is 2 plus (LIN)'s error; coefficient 3 applies whenever that error is <=1. The weaker hypothesis D 2^-w ->0 by itself remains open here.

The maximum-influence selection rule is FALSE: bent-point replacement followed by balanced low-influence compositions preserves the bad root erasure while making it the unique most influential coordinate (PROOFS.md section 11). extra_checks.json confirms the mechanism on a full 19-variable table. The same file tests growing neighborhoods on the PM tower; fixed bottom neighborhoods diverge by (PMB), while growing bottom depth controls the tested ratio.

The finite two-level tree is ruled out as an all-coordinate fixed-window counterexample: its private leaf mates give an order with L_leaf^1/Inf_leaf ->2 even in the unbalanced regime. Section 8 includes the explicit bound. The all-mate-order root obstruction is therefore a statement about a specified interior coordinate, not a claim that more finite-tree scans will settle the universal minimum.

Final audit: audit.json confirms 17 required artifacts, 21 finite window cases and 101 evaluated coordinates through dimension 22, 96 comparisons with all permutations, six tensor-reference cases, and 1212 direct-versus-spectral derivative checks. All instrumented runs used actual nice 10. Largest measured RSS: 1100627968 bytes. Folder size at audit: 3257076 bytes. The full conjecture and the explicitly listed wider parameter/order questions remain unresolved; REPORT.md records the mathematical stopping points.
