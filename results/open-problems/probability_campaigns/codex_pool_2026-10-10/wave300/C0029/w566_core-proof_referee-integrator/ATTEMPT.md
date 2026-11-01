# C0029 referee attempt and exact gap

## Target

For iid signs in an n-by-n matrix B, seek an absolute q<1 with P(s_min(B)≤ε/√n)≤ε+q^n for every ε≥0 and sufficiently large n. The 2025 Sah–Sahasrabudhe–Sawhney bound is (1+O((log n)^(-1/16)))ε+exp(-Ω(n)). Current exact-target openness is UNKNOWN pending a stronger contemporary literature verification.

## Reviewed reduction

w564 L1 is an exact Schur-complement characterization for appending one row to an (n−1)-by-n matrix. I rederived it from the inertia of AA^T−r²I. The branch s_min(D)≤r forces s_min(A)≤r by principal-submatrix interlacing. On s_min(D)>r, the Schur complement is |⟨v,X⟩|²−r²(1+Σ_i⟨v_i,X⟩²/(s_i²−r²)). This handles r=0, equality, and deficient row rank.

w564 L2 follows by conditioning on the same skeleton D_k when row k is switched from signs to Gaussian; summing p_{k−1}−p_k telescopes exactly. It does not require independent projections of a sign row.

The missing H is precisely a signed bound on Σ_k E[Q_R(D_k,r)−Q_G(D_k,r)] by ε−F_n(ε)+q^n, with r=ε/√n and F_n the finite-n Gaussian CDF. Algebra makes H equivalent to the parent bound in 0≤ε<1; that algebra offers no estimate of H. This is the single hardest open piece in this route.

w564 L3 gives a Hadamard skeleton for which Q_R−Q_G≥3/[4(n+1)] at r=1/[8(n+1)]. I checked the two-dimensional spectral block, the central-binomial atom, and the Gaussian density/Jensen bound independently. Thus orthogonality and flatness do not give a pointwise sign.

## Own narrow lemma L4: charge the exact orthogonal skeleton event

Let n be even and D have n−1 independent iid sign rows. Then

P(the rows of D are pairwise orthogonal) ≤ p_n^(n−2) ≤ 2^(−(n−2)), where p_n=2^(−n) binom(n,n/2).

Proof: condition on the first sign row. Each of the remaining n−2 rows independently has dot product zero with it with probability p_n. Pairwise orthogonality implies all these n−2 simpler events. To see p_n≤1/2, set n=2m: p_2=1/2 and p_(2m+2)/p_(2m)=(2m+1)/(2m+2)<1. For n≥4 a mixed D_k containing a Gaussian row has probability zero of exact pairwise orthogonality, since that continuous row has zero inner product with an independent nonzero row with probability zero. This directly charges the *exact* Hadamard family in L3 under the true iid skeleton distribution; it says nothing about nearly orthogonal or other arithmetic skeletons.

This L4 is my new result and has **not** received independent review. Request w569 to audit it before a theorem card is submitted. It does not prove H or the parent problem.

## Archive correction

The 2026-09-07 C0029-A001 attempt calls 1−exp(−t²/2−t) an exact finite-n Gaussian law. At n=1, t=1, the exact Gaussian CDF is erf(1/√2)=0.6826894921370857, versus 0.7768698398515702 for that expression. It is a limiting law; finite-n comparison should use F_n, or Edelman's finite-n bound F_n(ε)≤ε as stated in the 2025 paper's Theorem 9.4.

## NEXT

An independent referee should check L4. Then attempt a signed estimate for the typical mixed skeletons, allowing structured exceptions to be charged at their actual probability. Do not substitute a uniform pointwise row bound, and do not promote H as proved.
