SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T21:03:58.325290Z.
attacking: robustify the rank-two Schur-DPP receiver against the retained Frobenius twist from the finite-hub normal form, without deleting the rough-law residual.

# Early substantive calculation

Programme: QFORM-DENSITY-3EIG-20260922. Full unrestricted theorem OPEN; continuity separate. Owner continuation QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z acknowledged. Execution WITHOUT_VERIFIED_BRAIN.

Use the current finite-hub normal form on a physical complement,

A = D + U Lambda U^T + E,

where U^T U=I_2, Lambda is invertible symmetric 2x2, D is diagonal, and E is symmetric with zero diagonal. E is retained; no random quadratic term is deleted. Fix an original physical scalar pivot z and write

u=u_z, c=||u||^2, d=D_zz, a=A_zz=d+u^T Lambda u,
r=U_- Lambda u, e=E[-z,z].

Assume a d !=0 and c<1. The exact Schur remainder is

S=A[-z,-z]-a^(-1)A[-z,z]A[z,-z] = S_0+F,

S_0=D_-+U_-[Lambda-a^(-1)Lambda u u^T Lambda]U_-^T,
F=E[ -z,-z]-a^(-1)(r e^T+e r^T+e e^T).                         (E1)

If epsilon=||E||_F, then

||F||_F <= epsilon_z
:= epsilon(1+2||r||/|a|)+epsilon^2/|a|.                          (E2)

Normalize S_0 exactly as in the completed fleet01/B13 Schur-DPP theorem:

S_0=D_-+W N W^T, W^T W=I_2,
det N=(1-c)d det(Lambda)/a.

Let q_H=det(W_H)^2 be the physical pair-volume law and delta=P(H cap K=empty) for independent q-pairs. Its random-cut argument supplies disjoint original banks I,J for which B_0=S_0[I,J] obeys

||wedge^2 B_0||_HS >= |det N| sqrt(delta)/4
                    =s_1(N)s_2(N)sqrt(delta)/4.                  (E3)

The actual Schur cross block is B=S[I,J]=B_0+G with ||G||_F<=epsilon_z. Tensorization followed by antisymmetrization gives the deterministic exterior perturbation inequality

||wedge^2(B_0+G)-wedge^2 B_0||_HS
 <=2||B_0||_F||G||_F+||G||_F^2
 <=2 sqrt(2) s_1(N) epsilon_z+epsilon_z^2.                        (E4)

If

s_2(N) >= 24 epsilon_z/sqrt(delta),                              (E5)

then the right side of (E4) is < one half of (E3): indeed its ratio to (E3) is at most 8 sqrt(2)/24+4/24^2<1/2. Hence

boxed: e_2(B^T B) >= delta |det N|^2/64.                          (E6)

This spends the retained twist only through the ACTUAL physical Schur cross block. No small-coefficient-to-small-random-variable inference is made. Applying the completed unconditional pair-volume half-Riesz theorem to B and then the original-coordinate scalar-square peel gives

boxed:
rho <= C_R delta^(-1/8)[(1-c)|a d det Lambda|]^(-1/4),
C_R=2^(3/4) C_E2 <=44.2884100651.                                (E7)

Thus the retained twist is robustly harmless whenever the exact rank-two Schur carrier has transverse singular value above the scale 24 epsilon_z/sqrt(delta).

The latest completed designated partner fleet03/B13 r34 now converts failure of (E5) into physical finite-center structure. Since failure gives

delta < (24 epsilon_z/s_2(N))^2,

the partner's weighted-pair stability theorem yields either a physical center h with

s_2(W_{-h}) <= sqrt(2)(24 epsilon_z/s_2(N))^(1/3),

or a physical three-set T with

||W_{T^c}||_op <=2(24 epsilon_z/s_2(N))^(1/3).                    (E8)

So a rough-law Frobenius twist does not merely leave an unspecified rank-two failure: either the actual Schur cross volume survives and the half-Riesz receiver pays it, or the carrier itself becomes quantitatively one-coloop/three-coordinate.

Pinned-source application: the immutable e5f71d79... D' theorem remains an equation-level obstruction for an augmented physical cross block N0=[M c]. If its natural squared-3x3-minor row marginals are <=2/3 and tau=||(I-P_2)c|| for the top left singular plane of M, then

rho <=9 sqrt(3e) e_3(N0^T N0)^(-1/6)
    <=9 sqrt(3e)(s_1(M)s_2(M)tau)^(-1/3),

hence

s_1(M)s_2(M)tau <=(9 sqrt(3e)/rho)^3.                             (E9)

This is a real pinned Fourier obstruction and preserves original-coordinate product provenance.
