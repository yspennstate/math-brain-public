SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T10:05:29Z.
attacking: the latest rank-one full-cross collar; determine whether a vanishing nonzero second cross singular value is a genuine density obstruction or only an overlap-sensitive proof-certificate loss.

# Early calculation — source-separated rank-one collar tail

Let m be even and take four pairwise-disjoint original-coordinate banks I0,J0,I1,J1, each of size m. Choose unit flat vectors u on I0, u2 on I1, v on J0, v2 on J1, and a balanced flat w on J0 with v perpendicular w. Thus every nonzero coordinate of these vectors has modulus m^(-1/2).

For 0<eps<1 define

Q_eps = 2 (u^T X_I0)(v^T X_J0) + (w^T X_J0)^2 + 2 eps (u2^T X_I1)(v2^T X_J1).

The physical symmetric matrix has nonzero spectrum exactly

{-1,1,1,-eps,eps}.

Hence it is a literal owner-target family with exactly three eigenvalues of modulus at least one. On the zero-self X-bank I0 union I1, the full cross map to J0 union J1 has singular values d1=1,d2=eps. The newest completed fleet03/B18 receiver therefore gives the valid but degenerating certificate

||p_Qeps||_infinity <= 2 sqrt(pi) eps^(-1/2).

However the last term uses original coordinates disjoint from the first two terms. Put

Q0 = 2UV + W^2,
R_eps = 2 eps U2 V2.

Then Q0 and R_eps are genuinely independent, so once Q0 has an L-infinity density,

p_Qeps = p_Q0 * mu_Reps,
||p_Qeps||_infinity <= ||p_Q0||_infinity.

For U=u^T X_I0, LPP Theorem 1.1 gives ||p_U||_infinity<=sqrt(2). For the orthonormal pair (V,W)=(v^T X_J0,w^T X_J0), the same theorem gives the JOINT density cap <=2; no independence between V and W is asserted. Applying the completed fleet02/B18 theorem QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1 with K=sqrt(2), M=2, beta=gamma=1 gives

||p_Q0||_infinity <= 3 (2 M K)^(2/3)
                    = 3 * 2^(5/3)
                    = 9.524406311809198... .

Therefore

boxed: sup_(0<eps<1) ||p_Qeps||_infinity <= 3*2^(5/3),

with the nonzero eps-tail retained exactly, not discarded.

This shows that reciprocal payment in sigma_2(D) is not structurally necessary when the small tail is source-separated. The genuinely unpaid near-rank-one collar is the OVERLAPPING tail case.

A second obstruction is physical localization. Every nonzero entry of A_eps has modulus at most 1/m. Hence for every physical principal subset S of cardinality k,

||A_eps[S,S]||_op <= ||A_eps[S,S]||_infinity <= k/m.

Thus no bounded-size physical principal core can carry a fixed spectral scale as m tends to infinity, even though the full matrix remains in the exact target and the density bound above is uniform.

Pinned e5f Theorem F independently pays Q0: its rank-three spectral range is span{u,v,w}; leverages are 1/m on I0 and 2/m on J0, so for m>=4 all are <=1/2 and Theorem F gives ||p_Q0||_infinity<=12. Independent convolution therefore also gives ||p_Qeps||_infinity<=12. This is a real application of the pinned theorem, not a novelty inference from the counterexample search.

Unpaid implication: isolate or aggregate a rank-one cross plus transverse curvature while classifying the retained small second cross tail by ORIGINAL-source overlap. Source-separated tails are harmless by convolution; the difficult case is a small tail sharing coordinates with the main bilinear/curvature packet, where it cannot be deleted or convolved away.
