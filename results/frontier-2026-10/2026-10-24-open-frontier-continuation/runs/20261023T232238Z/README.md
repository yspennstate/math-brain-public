# T384: nonorthogonal boundary-grid law and sliding selection

This run advances the unsolved nonorthogonal-input part of T384. **Full T384 remains OPEN.** The previous orthonormal absorbing-flow theorem and scalar GD theorem remain dependencies with their original assumptions.

## New internally proved and reviewed results

1. **Actual simultaneous GD, arbitrary fixed full-rank input matrix:** BOUNDARY_GRID.md proves the joint critical-step boundary-grid limit at h=gamma/(log m)^(1/alpha), for every fixed finite number of steps. The marked endpoint recursion retains crossing and reactivation. Its tangent-Gram and scaled-output limits are explicit absolutely convergent Poisson sums. Three independent reviews check the proof. This is not a macroscopic-time result.
2. **Finite-width obstruction:** agents/e01_obstruction.md gives fixed labels and an open positive-probability iid-stable initialization event at every fixed m>=2 where zero-at-kink ReLU flow has no Caratheodory continuation. The residual evolves in the proof. The generalized-gradient/Filippov slide is calculated exactly. No width-uniform failure probability is claimed.
3. **Frozen-pair marked entrance:** agents/e02_endpoint.md solves the generic frozen-residual two-input sector/face dynamics and its eventual affine ray. Different original marks can select different scaled paths from the same collapsed origin.
4. **Local general-face selection:** FACE_SCHUR.md gives unique convex-inclusion flow, vanishing-step Euler selection, finite-time capture, and the Schur-complement output action under explicit strict attraction hypotheses.
5. **Euler chatter and a persistent correction:** agents/e03_discrete.md proves exact occupation and output identities, phase-dependent secant averages, and failure of naive averaged-tangent output dynamics. The frozen example also rules out L1 convergence of the tangent kernel to its time mean. A conditional changing-residual identity is retained with its unpaid network hypotheses.
6. **Macroscopic subsequential characterization:** MACRO_COMPACTNESS.md proves tightness of actual GD outputs on every fixed physical-time horizon, frozen second-layer Gram, uniform small-atom removal, and a compatible endpoint/residual differential inclusion for every subsequential limit. Every such limit has exponential residual decay controlled by C. Two independent reviews check the growing-step and infinite-atom arguments. Mark-dependent selection and uniqueness remain OPEN; this is not a unique limiting law and its effective matrix is not claimed to be a limit of tangent Grams.

CLAIMS.json separates these scopes, disproved extrapolations, and open tasks. PROVED means internally derived and independently checked under the written assumptions. External priority remains unverified. Primary literature already describes the general inward-boundary nonexistence mechanism; this package does not claim it as new.

## Exact proof dependencies

The parent continuation's research/T384_marked_PPP.md and research/T384_orthogonal_initialization.md supply scalar/category joint stable initialization. Run 20261023T224735Z supplies its finite-ray formulation and independent audit. That run's Math Brain proof commit is dc1b78f433593629b70b69182265c0683fccd4c4 and Brain proof commit is 9d9b368b2d2276429e5fc9b6e595c7d6f98f22f0. Fresh reads at this run's start found identical latest continuation subtrees in both repositories, with no newer run or native T384 closure. Current T384 moves still record only the earlier literature/numerical work; their blob is 6289f46595e36a85cd9388d16c84f89bc57fc774. The catalog has 422 rows, blob b8d4607e60eafcce5b3e8286cf882e8931737bd6.

## Actual checks and continuation

code/e03_chatter_check.py uses exact rational arithmetic; outputs/e03_chatter_check.txt is executed stdout, and outputs/EXECUTION_READBACK.json records the root rerun and full equality. code/check_vector_identity.py additionally checks both the one-step and cross-time exact vector output identities on 400 updates with activation and deactivation; outputs/vector_identity.json records its actual output. These are algebraic checks, not stochastic simulations. Reviews include independent proof checks and ROOT_REVIEW.md. All failed extrapolations are retained in DIRECTIONS.md and the proofs.

The exact next gap is **mark-dependent selection and uniqueness for the nonorthogonal macroscopic inclusion**, beginning with a pair. The compactness theorem has paid uniform estimates and subsequential representation. DIRECTIONS.md gives the local invariant that may pay the sliding part, and lists the remaining entrance and transition issues. Do not replace that gap with another derivation of this finite boundary grid or the new compactness theorem.

This run used four parallel workers selected as gpt-6-sol/max within the available concurrency limit; actual backend metadata and root model metadata are UNKNOWN. It did not use thirty simultaneous workers or uninterrupted background execution. No held/protected sources, public repository release, core-store deployment, paid compute, or routine emails were used.

## Exact continuation pointers

- Math Brain: research_pushes/2026-10-24-open-frontier-continuation/runs/20261023T232238Z/
- Brain: 06_math_research/open_frontier_continuation_2026_10_24/runs/20261023T232238Z/

Post-write verification and handoff receipts are saved as supplements. Git persistence, full-file readbacks, inbox transport, recipient acknowledgement, and native ingestion are distinct states; native ingestion remains unconfirmed unless a later receipt supplies native IDs.
