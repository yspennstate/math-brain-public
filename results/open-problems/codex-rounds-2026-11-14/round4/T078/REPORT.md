VERDICT: PROVED smaller boundary-coloring cost for finite transposition meshes

The round 3 scalar field-selection criterion holds. An independent derivation is recorded in [LOG.md](LOG.md). The initial literature check found the same September 24, 2026 solution claim by OpenAI and its known companion claims, with no newly established resolution or correction. The manuscript was opened; its full proof remains unaudited here. T078 is not proved by this work.

The new result is a boundary-cost estimate in [PROOF.md](PROOF.md). In a finite exchange mesh, let D be a set of slots, let r_j be the independent base activation probabilities, and let X contain exactly the transpositions crossing between D and its complement. Weight each picture by 2 to the number of cycles and color the cycles independently and fairly. Then

    P(all cycles visiting D are up)
      >= 2^(-|D|) product_(j in X) (1+r_j)^(-1).

The proof counts one directed exit per active crossing transposition and uses the exact conditional activation bound 2r/(1+r). It does not assume independent marks after loop weighting. An algebraic partition-weight argument checks the conditional factor a second way. Two-slot examples and all endpoint cases are checked exactly; the estimate is not asserted to be optimal.

For repeated spatial sweeps at rate delta/2 and fixed time t, the boundary factor becomes

    exp[-|D| log 2 - t J_cross/2].

A separate Poisson insertion argument re-derives the coefficient 1/2. The inspected source instead uses exp[-|D| log 2 - 2 log(2) t J_K], where J_K>=J_cross also counts edges with both endpoints in D. This sharpens the boundary cost in the next dependency named by round 3, rather than repeating the field-selection improvement.

If the boundary-pinned law makes every slot's avoidance probability at most p<1/2, the corresponding zero-field magnetization tail at one quarter of the slot count is at least 1-2p times the proved boundary factor. That spatial hypothesis remains unproved here. The audit traced `mesh_matrix_surface` to `mesh_surface_tail` in MeshSurface.lean, whose inputs are `mean_boundary_cycles` in BoundaryMesh.lean and `Bootstrap.mesh_pin_bound`. The result improves the former input; it does not verify the latter, the physical-spin projection, or the infinite-volume state construction. No source error or improved temperature threshold is claimed.

Commands: read prior files using `cat`, inventory using `rg --files` and `find`, and inspect local artifact sizes using `wc`. Shell reads after the initial inventory used `OMP_NUM_THREADS=1 nice -n 15`; priority adjustments were denied by the sandbox. No numerical script or Lean build was run. All mathematical verification is written out exactly. Web search/open/click supplied the literature and Lean sources linked in PROOF.md. Local edits used `apply_patch`. The initial brain recall was interrupted after an unexpected ONNX import; its internal logging was not inspected. No git or subagents were used; all explicit file edits stayed in this folder.

Access failures: guessed MeshSurfaceTail.lean returned 404, while MeshSurface.lean opened successfully; GitHub directory/API listings failed. They do not indicate missing mathematical dependencies. These failures and the priority restriction are recorded in LOG.md.

Next worker: audit `mesh_pin_bound` in [MeshPin.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/MeshPin.lean), especially `periodic_return_estimate` (line 45), `regularity_of_pin_induction` (line 46), and the uniform parameter choice (lines 47–49). The single-slot avoidance bound is sufficient for the tail proved here. Establish it uniformly in volume, or locate a failed hypothesis; another scalar tilt or boundary-cost estimate will not supply that spatial input.

Task: “take the NEXT checkable step on this problem, building on that work” — session start 2026-11-15 04:40 +04; exact user-message clock time unavailable.
