# QFORM handoff: two-bank outer-level one-hub density theorem

**Status:** proved scoped theorem; full conjecture open.

[Source-pinned proof and partition lemma](https://github.com/yspennstate/math-open-problems/blob/f0d3e4df297cf45c4f8a0298051cef186faf1de4/proofnet24/QFORM-density/interactive/20260923T203000Z-two-bank-outer-density/REPORT.md).

Let H have arbitrary cap-one density, independent of light (L,V,P)=Y1+Y2. Banks Y1,Y2 are independent; each (L,V) bank marginal density is bounded by Mj. P may depend arbitrarily on L,V within either bank. For Q=2HL+βL²+V²+2εLP, all β,ε, the density on |s|≥1 obeys p_Q(s)≤1/2+C√(M1M2). This is uniform as ε→0 and permits fragmented unbounded supports. If ε=0, the earlier beta-uniform coarea theorem covers every s.

Proof heart: condition light to express the dyadic density as (2|L|)^−1 f_H([s−V²−βL²]/[2L]−εP). Fourier transform in P gives ε^−1 hat f_H(ζ/ε). Fresnel in V and second-derivative van der Corput in L give a dual-kernel bound min{√(εr/|ζ|), εr/|ζ|} for |s|≥1. Planar Plancherel and bank independence give ∫|Φ1(ξ,ζ)Φ2(ξ,ζ)|dξ≤(2π)²√(M1M2) at every ζ. Substitute ζ=εu. The low, middle, and high u ranges cost r, r log(1/r), and r; the high range uses ∥hat f_H∥₂≤√(2π). Sum dyadic r. No hub support interval decomposition or ε loss occurs.

A planar Parseval original-product frame with every row leverage≤1/144 can be split into independent banks with Grams ≥(1−1/√72)I₂/2>.44I. Proof: random signs S=Σ ε_i w_iw_iᵀ have E∥S∥F²=Σ∥w_i∥⁴≤1/72. Each bank planar projection density cap <4.55.

**Remaining exact gaps:** For |s|<1, the van der Corput factor from s/L degenerates. Fresnel alone leaves the critical high-frequency weight |u|^−1/2 against arbitrary L² hub Fourier transform. A nonzero physical hub square aH² is also untreated. Quantitative bank splitting may fail when a light physical row is heavy. The theorem is exact rank-three canonical scope, not a full general-matrix solution.
