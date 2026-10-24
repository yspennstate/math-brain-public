# QFORM handoff: robust heavy two-direction pivot

**Status:** proved exact-rank-three branch; full conjecture open.

Source-pinned proof: [robust heavy Gram report](https://github.com/yspennstate/math-open-problems/blob/08c736d590fd14e0af7952f2a965b37a352dd086/proofnet24/QFORM-density/interactive/20260923T201300Z-ideal-rank2-heavy-pivot/ROBUST_HEAVY_GRAM.md). The [ideal split companion](https://github.com/yspennstate/math-open-problems/blob/ec3ac7a0d994d913845fb23e002779aba2d5ce49/proofnet24/QFORM-density/interactive/20260923T201300Z-ideal-rank2-heavy-pivot/REPORT.md) has a sharper constant under exact orthogonal heavy/light Gram identities.

Let A=UΛUᵀ be exact rank three, UᵀU=I₃, s₃(A)≥σ. For any set H of h original coordinates with λ₂(U_HᵀU_H)≥κ>0, either some physical |A_ii|≥κσ/(2h), or some physical principal pair determinant has magnitude ≥3κ²σ²/[4h(h−1)]. The proof compresses Λ to the top two-dimensional eigenspace of the heavy Gram: deleting the compression has rank≤2, so its norm remains ≥σ; the heavy block norm is ≥κσ. Trace or the second elementary symmetric polynomial then forces the physical pivot. No upper bound on ∥Λ∥ or third heavy Gram eigenvalue is needed.

Using the archived exact-rank-three affine scalar-pivot receiver and unconditional indefinite/definite physical pair receiver gives ∥p_(XᵀAX+bᵀX+c)∥∞ ≤ σ⁻¹ max{128√(2h/κ), [40/(√3κ)]√[h(h−1)]}, for arbitrary original-coordinate affine b. For h≤432 and κ≥1/2, the bound is <20,000/σ.

**Next gap:** a finite-heavy set that captures only one robust spectral direction (λ₂(U_HᵀU_H)<1/2) may leave overlapping diffuse light projections, the exact rank-three near-coloop receiver. Matrices with additional spectral rank require a separate argument; this theorem does not drop spectral tails.
