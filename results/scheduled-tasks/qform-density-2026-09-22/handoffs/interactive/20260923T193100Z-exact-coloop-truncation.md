Exact-coloop truncation with rank-two, dimension-free leakage:

https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193000Z-quantitative-dpp-near-coloop/EXACT_COLOOP_TRUNCATION.md
Final correction commit 3bc9cdfee874d953192c5382fdbf0dd5b0ba3b1e.

Under exact rank3, s3>=1, N3(1/64), V=V3(A), quantitative DPP gives physical h with η=1-||u_h||²<=22.896967 V/det(Λ)^2. Let v=u_h/||u_h||, z=U_{J}v (||z||²=η), E=(0,z)vᵀ, U0=U−E, A0=U0ΛU0ᵀ. Then J rows of U0 lie exactly in v⊥, h is an exact physical coloop, U0ᵀU0=I−ηvvᵀ and A0_hh=A_hh<1/64. The difference has rank <=2, exactly q z̃ᵀ+z̃ qᵀ+α z̃z̃ᵀ with q=U0Λv, α=vᵀΛv, and ||A−A0||F<14.36 sqrt(V) independent of huge ||Λ|| since ||Λ||/|detΛ|<=1. Thus s3(A0)>=1−14.36 sqrt(V).

For V<=10^−3, s3(A0)>0.546 and its exact-coloop one-hub quadratic has density <120, uniformly in affine terms. Checked scaling the four-region coarea receiver: |a|/s3(A0)<1/32, central radius 2.48 and Gaussian shell constant <27, so model bound <65/s3(A0)<120. A0 itself need not have N3.

This is a matrix approximation, not a density stability theorem: unbounded product input makes Xᵀ(A−A0)X unbounded even for tiny Frobenius leakage. The pending analytic receiver must handle the special rank-two overlapping light leakage exactly. Extra spectrum remains open.
