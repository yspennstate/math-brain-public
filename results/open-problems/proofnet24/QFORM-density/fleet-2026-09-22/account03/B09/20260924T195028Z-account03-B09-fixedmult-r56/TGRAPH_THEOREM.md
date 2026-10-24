SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T19:50:28Z.
attacking: rank-one common-heavy near-zero hub and s7 structural closure; audit spectral-rank perturbation and diagonal-dominance dependencies.

# QFORM-RANKONE-TGRAPH-L1-v1

Run: 20260924T195028Z-account03-B09-fixedmult-r56.
Source input: yspennstate/math-open-problems@2688a04edbcc2792f33f4069f6582a3c89383846, proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T181608Z-account03-B09-fixedmult-r54/S7_TWOSTAR_PROOF.md.
Status: supporting theorem; s7 and full s3 remain open.

Let the ORIGINAL coordinates split as {h} disjoint union L disjoint union R disjoint union W. Condition on X_W. Suppose A[L,R]=u v^T has exact rank one. Put c=A[L,h], r=A[R,h] and
alpha=||u||^2||c||^2-(u.c)^2,
beta =||v||^2||r||^2-(v.r)^2.
If alpha beta>0, then the full ambient quadratic-plus-affine law has a continuous C0 density and
[
 ||p_Q||_infty <= 3 e^{2/3}(alpha beta)^{-1/6}.
]
Hence P{Q in I} <= 3 e^{2/3}(alpha beta)^{-1/6}|I| for every interval I. There is no dependence on A_hh; exact zero and arbitrarily small nonzero hub squares are covered.

## Proof

After conditioning on W, absorb every same-bank quadratic and affine term into real phases:
[
Q=q_h(H)+q_L(Y)+q_R(Z)+2H(c.Y+r.Z)+2(u.Y)(v.Z).
]
Set U=(u.Y,c.Y), V=(v.Z,r.Z). Product-projection density control gives
[
 ||p_U||_infty <= e/sqrt(alpha)=:G,qquad
 ||p_V||_infty <= e/sqrt(beta)=:K.
]
This is a deterministic projection estimate only; no independence of U's or V's coordinates is asserted.

At frequency t, push e^{it q_L}dP_Y and e^{it q_R}dP_Z to U,V. Their complex densities g_t,k_t satisfy |g_t|<=p_U and |k_t|<=p_V, hence ||g_t||_2^2<=G and ||k_t||_2^2<=K. Let f_t(x)=f_h(x)e^{itq_h(x)}, so |f_t|=f_h<=1 and int f_h=1.

For fixed x define
[
A_x(s)=int g_t(s,y)e^{2itxy}dy,qquad
B_x(r)=int k_t(r,z)e^{2itxz}dz.
]
Then
[
phi_Q(t)=int f_t(x),[int int A_x(s)B_x(r)e^{2itsr}dsdr],dx.
]
Plancherel at scale 2t gives
[
|int int A(s)B(r)e^{2itsr}dsdr|
 <=(pi/|t|)^{1/2}||A||_2||B||_2.
]
Cauchy in x, f_h<=1, and a second Plancherel calculation give
[
int ||A_x||_2^2dx=(pi/|t|)||g_t||_2^2<=pi G/|t|,
]
[
int ||B_x||_2^2dx<=pi K/|t|.
]
Therefore
[
|phi_Q(t)|<=min{1,pi^{3/2}(GK)^{1/2}|t|^{-3/2}}.
]
For C=pi^{3/2}(GK)^{1/2},
[
int_R min(1,C|t|^{-3/2})dt=6C^{2/3}.
]
Fourier inversion gives
[
||p_Q||_infty <=(3/pi)C^{2/3}=3(GK)^{1/3}
 <=3e^{2/3}(alpha beta)^{-1/6}.
]
The L1 characteristic-function bound gives a continuous C0 density. All outside conditioning is uniform. QED.

## Rank-one packet router for the live r54 s7 branch

For an actual partition H,L,R with N=A[L,R]=u v^T, write
alpha_h=||u wedge c_h||^2 and beta_h=||v wedge r_h||^2.
Every fixed-hub complete overlap packet satisfies exactly
[
sum_{|P|=|Q|=2} det A[P+h,Q+h]^2=alpha_h beta_h,
]
independently of A_hh. For distinct hubs g!=h,
[
sum_{P,Q} det A[P+g,Q+h]^2=beta_g alpha_h.
]
Put S=sum_h alpha_h beta_h, A0=sum alpha_h, B0=sum beta_h and Omega=A0 B0-S.

If Omega>=S/4, a fair split of H into row/column hubs keeps each ordered distinct pair with probability 1/4, so some literal disjoint cross block has Z3>=Omega/4>=S/16. The completed marginal-free cross-E3 theorem gives
[
||p_Q||_infty <= C_E3(S/16)^{-1/6},
quad C_E3=3,2^{4/3}e^{1/3},
]
continuously.

If Omega<S/4, normalize p_h=alpha_h/A0, q_h=beta_h/B0 and rho=sum p_hq_h=S/(A0B0)>4/5. Since sum sqrt(p_hq_h)<=1,
[
rho=sum (sqrt(p_hq_h))^2
 <=max_h sqrt(p_hq_h),
]
so for some h*, p_h*q_h>=rho^2 and
[
alpha_{h*}beta_{h*}>=S rho>4S/5.
]
The theorem above then gives
[
||p_Q||_infty <=3e^{2/3}(4S/5)^{-1/6},
]
again continuously.

At the live r54 currency
S>=S0=4322241/61035156250=7.0815596544e-5,
the distinct-hub branch is <82.337 and the common-hub branch is <29.816. Thus the ENTIRE exact-rank-one middle-crossing realization of the r54 S0 packet is paid continuously. This strictly extends the earlier coherent-star rank-one payment: no global star coherence across hubs is required.

Remaining s7 debt: genuine rank-at-least-two middle crossing / non-rank-one packet. Full s7 and s3 remain open.
