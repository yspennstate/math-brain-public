VERDICT: PROVED optimal scalar field-selection criterion from a magnetization tail

The earlier report's scope check holds. OpenAI's September 24, 2026 manuscript claims precisely the required spontaneously magnetized KMS state. Independently read the manuscript, comparator and implementation. Also read the October 26 comparator log through its kernel-acceptance message, which the earlier worker had not established. This is reported formal verification, not a local reproduction or a complete mathematical audit. Details and references are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

The mathematical addition is [PROOF.md](PROOF.md). Suppose M lies in [-V/2,V/2], V>0, and its zero-field law satisfies P(M>=V/4)>=L>0. Put z=bV/8, where b is the tilting parameter. The tilted mean is at least V/8 for every such scalar law exactly under these conditions:

    z<=1/5:   exp(6z) >= 5(1-L)/L;
    z>=1/5:   z exp(z) >= (1-L)/(eL).

The proof includes two-point extremizers, a second derivation and exact equality checks at z=0, 1/5 and 1. A separate convexity argument proves the convenient sufficient condition

    bV >= 8 log(1/L).

For the spin model, V=2S|Lambda| and b=beta h. This improves the source's sufficient selection condition bV>=16 log(11/L). With a surface-cost tail L=exp(-A)/2, the new sufficient field satisfies beta hV>=8(A+log 2). The optimality assertion concerns scalar laws with the stated support and tail; it need not be optimal on the physical magnetization spectrum. No novelty claim is made for the elementary extremal method.

This does not prove T078. The missing spatial input is still the uniform low-temperature magnetization tail. The source audit traced `field_ordered_cubes` through `physical_surface_bound`, `symmetrized_surface_bound` and `completed_surface_bound` to `mesh_matrix_surface`. That deeper estimate was not verified. No counterexample to the manuscript was found, and no improvement of its temperature threshold is claimed.

Commands and outputs are in [LOG.md](LOG.md). Work used web search/open/click, read-only shell inspection prefixed with `OMP_NUM_THREADS=1 nice -n 15`, and `apply_patch` for local files. A small curl directory request failed with DNS error. The sandbox rejected priority adjustments; no numerical computation, Lean build, heavy process, git command, subagent or external write was used. All mathematical checks are exact and written out.

Next worker: audit `mesh_matrix_surface` and the finite-mesh loop estimate supplying the surface tail. Start with [CompletedSurface.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/CompletedSurface.lean), line 31, and its `MeshRoom` import. The field-selection implication can now be used with the sharper bound proved here, but proving that implication does not verify its tail hypothesis.

Task: “take the NEXT checkable step on this problem, building on that work” — session start 2026-11-15 01:14 +04; exact user-message clock time unavailable.
