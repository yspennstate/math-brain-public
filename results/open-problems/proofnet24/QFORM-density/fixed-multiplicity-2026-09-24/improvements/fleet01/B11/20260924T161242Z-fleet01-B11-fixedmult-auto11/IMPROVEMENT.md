# Threshold-eight structural reduction

Pinned source: eeb752c8943536541b34b42b8bf48e924f4d3d2f, blob 19fb119877426b640b2c0dae19ec2f78a399fe11.

This is not an eight-eigenvalue density theorem.

Assume the normalized no-pivot setting of the pinned paper and s_8(A)>=1. Then s_5(A)>=1, so V_2>=kappa^2, where kappa=4/625.

If V_3>=kappa V_2, then V_3>=kappa^3. A fair coordinate cut gives a literal crossing block M with Z_3(M)>=V_3/64>=kappa^3/64. The marginal-free order-three receiver gives
||p_Q||_infinity <= C_3 Z_3(M)^(-1/6)
<= 2 C_3/sqrt(kappa)=25 C_3<375.
Thus this branch is closed.

Now suppose V_3<kappa V_2. Apply the volume-sampled interpolation lemma with r=2. There is an invertible disjoint seed B=A_{S,T} and a completion A=D+R+E such that
||E||_F < 3 sqrt(kappa)=6/25,
rank(R)<=6,
rank(R_LL)<=2,
D is diagonal and zero on the seed, and E has zero diagonal.

Singular-value perturbation gives s_8(A-E)>19/25. Since A-E=D+R and rank(R)<=6, rank shift gives s_2(D)>19/25. Hence two distinct external coordinates h_1,h_2 satisfy
|D_{h_j h_j}|>19/25.

The exact bordered determinant identity gives
|det A_{S+h_j,T+h_j}|>(19/25)|det A_{S,T}|,
for j=1,2.

Let H={h_1,h_2}. The two-by-two Schur residual
C_H=A_{H,H}-A_{H,T}B^{-1}A_{S,H}
equals (D+E)_{H,H}. Its diagonal entries have modulus >19/25 and its off-diagonal entries have modulus <6/25. Therefore
|det C_H|>(19/25)^2-(6/25)^2=13/25,
and
|det A_{S union H,T union H}|>(13/25)|det A_{S,T}|.

Thus the normalized s_8 no-pivot problem has a rigorous dichotomy:
1. disjoint third volume already gives density <375; or
2. one invertible disjoint 2x2 seed has two strong same-index extensions, each >19/25 relative to the seed, with joint two-coordinate Schur-residual determinant >13/25.

The missing analytic obligation is a product-preserving density receiver for case 2. The shared coordinates occur on both row and column sides; the existing disjoint-bank order-three receiver cannot be invoked by treating them as independent copies. Conditioning them away leaves only the rank-two receiver and does not close an L-infinity estimate.

Status: multiplicity nine remains proved. Multiplicity eight remains open, reduced in the normalized no-pivot chamber to this double-shared-border configuration.