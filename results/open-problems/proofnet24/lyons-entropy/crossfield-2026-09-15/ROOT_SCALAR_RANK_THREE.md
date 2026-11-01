# Scalar rank-three supports: an exact two-frame Fisher reduction

Coordinator derivation, 15 September 2026, building on X004's mixed-exterior representation. This is an exact reduction and a constructive proof lead, not a universal concavity theorem. It does not count as a sub-agent execution.

Let V:C^3→C^n be isometric, P=VV*, K=sP with 0<s<1, and vary the active covariance as sI+tA for Hermitian A. Write q=1−s, t_i=||v_i||², r_ij=||w_ij||²=det P_ij, and r_ijk=|det V_ijk|², where w_ij are the Hodge-dual two-row columns with the conjugation convention of X004. Initially all minors through order three are nonzero.

The fixed-support atoms are

    p_empty=q³, p_i=sq²t_i, p_ij=s²q r_ij, p_ijk=s³r_ijk.

Let h=tr A, a_i=v_i A v_i*, and b_ij=w_ij* A w_ij. Differentiation in the active matrix gives

    p'_empty=−q²h,
    p'_i=q(a_i−s t_i h),
    p'_ij=s(q r_ij h−b_ij),
    p'_ijk=s²r_ijk h.

These follow directly by writing the atom generating determinant as det(I−M)det[V M(I−M)^−1 V*]_S, or by the elementary symmetric adjugate formulas in dimension three.

Both row frames are Parseval:

    Σ_i v_i* v_i=I, Σ_ij w_ij w_ij*=I.

Consequently Σt_i=Σr_ij=3, Σa_i=Σb_ij=h, and Σr_ijk=1. Define the two positive quadratic forms

    F_v(A)=Σ_i a_i²/t_i,
    F_w(A)=Σ_ij b_ij²/r_ij.

Then the full Fisher information simplifies exactly to

    FI_s(A)=F_v(A)/s+F_w(A)/q.                         (1)

Indeed the empty and triple layers contribute h², the singleton layer contributes F_v/s+(3s−2)h², and the pair layer contributes F_w/q+(3q−2)h². Their h² coefficients sum to zero. No statistic projection or lower bound was used.

The higher Möbius coefficients of −log p_S are independent of s because the scalar odds factors contribute only an affine function of |S|. With X004's frozen matrix W and scalar τ, the full entropy curvature is therefore

    −H''_s(A)=F_v(A)/s+F_w(A)/q−2 tr[(W+sτI)adj A].   (2)

Equivalently the required sign at every scalar active base for this fixed frame is positivity, for all A, of the cubic matrix polynomial

    q F_v(A)+s F_w(A)−2sq tr[(W+sτI)adj A].           (3)

This is a nine-real-dimensional quadratic-form-valued polynomial of degree at most three in s. It admits exact Bernstein or algebraic certificates for specified frames without logarithms depending on s. It could also admit a universal frame inequality; such an inequality is not proved here.

For a fixed A, the negative-curvature expression in (2) has

    d²/ds²[−H''_s(A)]=2F_v(A)/s³+2F_w(A)/q³ ≥ 0.

Thus it is convex as a function of scalar base s. This convexity does not imply its nonnegativity; the interior minimum remains the issue. In particular, positivity near s=0 and s=1 cannot alone establish the desired result.

The point of (1) is to connect the entropy problem to complementary Parseval-frame measurements. The single remaining task is a sharp frame-dependent inequality paying the log-minor exterior term in (2). X004 is developing the general polarization and a fixed-frame consequence; future rank-three and uncertainty assignments can use this exact reduction.
