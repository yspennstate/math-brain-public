# Cayley proof: formal correspondence and limits

The manuscript is `cayley_paper.pdf`. Its full handwritten proof covers the explicitly defined finite graphs, projected semigroup, auxiliary-coordinate coupling, full Fourier spectrum, cube limit, and mixing-time brackets.

`CayleyAlgebra.lean` verifies eight exact algebraic components. It is not a complete Lean formalization of that probability theorem. The earlier `CayleyCore.lean` prototype with logarithm imports timed out; it is retained in evidence and excluded from the delivery archive.

| Lean declaration | Corresponding calculation |
|---|---|
| nonzero_jump_generator | θ(Q−I)=β(Π−I), entry by entry |
| cube_sector_gap | The gap formula for a nontrivial cube character |
| auxiliary_sector_gap | The gap formula for a nontrivial auxiliary character |
| mixed_sector_gap | The sector with both characters nontrivial |
| first_cube_gap | The first cube-mode gap is 2α/d+β |
| gap_times_comparison_scale | Multiplication by T gives L/2+βT |
| reset_times_comparison_scale | The reset scale equals 2^d L/[4(m−1)] |
| sector_numerator_comparison | Sufficient exact comparisons for the slowest sector |

All expressions are over the real field. L is arbitrary, so the identities can be specialized to L=log(d); the file does not prove any limit involving log. The identities prove the algebra after the graph and character formulas have been established. They do not prove that an arbitrary graph has this spectrum.

The full formal work still needed is: encode the finite product group and generating set; prove its graph properties and transition counts; construct the Markov semigroup and conditional auxiliary coupling; prove the character basis and spectral interpretation; establish the cube cutoff bounds and the limit/mixing-time argument; identify the exact source conjecture. There are no placeholder declarations pretending these steps are complete.

Successful build: Lean 4.33.1, eight printed target declarations, transitive axioms restricted to propext, Classical.choice and Quot.sound. Compiler and exact-source hashes, imports and output are pinned in the audit evidence. The small graph check separately enumerated 168 characters in six graphs and rejected the wrong reset rate in each; finite checks do not prove the asymptotic theorem.

Novelty is independent of compilation. The reset mechanism is classical; only the explicit unweighted realization/application is proposed as potentially new. Degrees grow, and bounded-degree or typical random-generator statements remain outside scope.
