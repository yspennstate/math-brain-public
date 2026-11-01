# QFORM-S7-TWOSTAR-FORCING-v1

Run: 20260924T181608Z-fleet03-B09-fixedmult-r54.

This is a supporting theorem for the fixed-multiplicity program. It does not prove multiplicity seven or the full three-eigenvalue conjecture.

## Statement

Normalize the coordinate density cap and spectral scale to one. Put eta=1/100. Assume A is real symmetric, s_7(A)>=1, and there is no eta scalar or principal-pair pivot. For
V_r(A)=sum det(A[S,T])^2 over ordered disjoint r-sets S,T, one has

V_1 >= 9801/10000,
V_2 >= 9801/250000.

Moreover one of two alternatives holds.

(A) V_3 >= V_2/800. Then the completed marginal-free order-three crossing theorem gives a continuous density with

||p_Q||_infinity < 155.

(B) V_3 < V_2/800. Then there is an actual partition of the original coordinates [n]=H disjoint_union L disjoint_union R such that, with

N=A[L,R],
c_h=A[L,h],
r_h=A[h,R],
T_h=||c_h||^2 ||r_h||^2 ||P_(c_h^perp) N P_(r_h^perp)||_F^2,

the grouped two-star resource satisfies

S(H,L,R):=sum_(h in H) T_h
>= S0 := 4322241/61035156250
= 7.0815596544e-5.

The identity used for T_h is

T_h = sum_{P subset L,Q subset R, |P|=|Q|=2}
      ( r_h[Q]^T adj(N[P,Q]) c_h[P] )^2.

## Proof of the V1 and V2 floors

No scalar pivot gives |A_ii|<eta. No principal-pair pivot gives, for i!=j,

|A_ij|^2 < eta+eta^2 = 101/10000.

Since V1=||offdiag(A)||_F^2 and ||A||>=1,

1 <= ||A|| <= ||diag(A)||+||offdiag(A)|| < eta+sqrt(V1),

so V1 >= (1-eta)^2=9801/10000.

Assume, for contradiction, V2<V1/25. Apply the volume-sampled interpolation/completion theorem at seed order r=1. For some nonsingular disjoint one-seed,

A=D+R+E,

where D is diagonal and vanishes on the two seed coordinates, E has zero diagonal,

rank(R)<=3,
rank(R[L,L])<=1,
||E||<=||E||_F<2 sqrt(V2/V1)<2/5.

Hence

s_7(D+R)=s_7(A-E)>3/5.

The rank-three perturbation inequality gives s_4(D)>3/5. Thus at least four complement coordinates have |D_ii|>3/5. Choose any two, i,j. Since E_ii=0,

|R_ii| > 3/5-1/100 = 59/100.

For their off-diagonal entry,

|R_ij| <= |A_ij|+|E_ij|
< sqrt(101)/100+2/5
=0.5004987562....

The exact diagonal-dominance margin is

59/100-(sqrt(101)/100+2/5)
=0.0895012437... >0.

Therefore the 2x2 restriction of R to these two complement coordinates is strictly row-diagonally dominant and has rank two, contradicting rank(R[L,L])<=1. Hence

V2 >= V1/25 >= 9801/250000.

## The paid V3 branch

If V3>=V2/800, then

V3 >= 9801/200000000 = 4.9005e-5.

A fair original-coordinate cut has third crossing volume at least V3/64. The completed marginal-free E3 receiver has constant

C3=3 sqrt(2) e (9/2)^(1/6).

Thus

||p_Q||_infinity <= C3 (64/V3)^(1/6)
                   =2 C3 V3^(-1/6)
                   <154.926<155.

The characteristic-function envelope in that theorem is integrable, so this branch has a continuous C0 density.

## Strong two-star forcing in the small-V3 branch

Assume V3/V2<1/800.

Sample nonsingular disjoint order-two seeds B=A[S,T] with probability det(B)^2/V2. The interpolation theorem gives

E ||F_B||_F^2 <= 9 V3/V2.

Call a seed good if

||F_B||_F^2 <= 18 V3/V2.

By Markov, good seeds carry determinant-squared mass at least V2/2.

For a good seed the completion A=D+R+E has

rank(R)<=6,
rank(R[L0,L0])<=2,
||E||<=||E||_F<sqrt(18/800)=3/20.

Since s7(A)>=1,

s7(D+R)=s7(A-E)>17/20.

Rank six forces s1(D)>17/20. Hence some complement coordinate h satisfies |D_hh|>17/20. For the interpolation

P=A[:,T] B^(-1) A[S,:],

one has D_hh=A_hh-P_hh. Therefore

|P_hh|>17/20-1/100=21/25.

Write u=A[S,h] and v^T=A[h,T]. Then

P_hh=v^T B^(-1) u,

and the exact polynomial identity

det(B) P_hh = v^T adj(B) u

gives

|v^T adj(B)u|^2 > (441/625) det(B)^2.

Select one such h for every good seed. Summing over the good-seed mass yields

sum_selected |v^T adj(B)u|^2
> (441/625)(V2/2)
>= 4322241/312500000.

Now color every physical coordinate independently into H,L,R with probabilities 1/5,2/5,2/5. A fixed selected five-coordinate packet (h,S,T) survives with h in H, S subset L, T subset R with probability

(1/5)(2/5)^4=16/3125.

Hence some actual physical partition retains at least that fraction of the preceding sum. For that partition every retained coefficient is a summand of the exact exterior identity for T_h. Therefore

sum_(h in H) T_h
>= (16/3125)(4322241/312500000)
= 4322241/61035156250.

This proves the theorem.

## Existing receiver and remaining debt

The source-pinned theorem QFORM-GROUPED-SHAREDHUB-SCHUR-L1-v1 at commit
96fdf63fbef72c07e56005074c9f9d5703888697,
path
proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260924T000644Z-fleet03-B02-qform-r40/REPORT.md,
proves in the coherent-star rank-one realization

||p_Q||_infinity <= 6 S^(-1/6),
integral |phi_Q| <= 12 pi S^(-1/6).

At S>=S0 this gives

||p_Q||_infinity <29.499

and a continuous C0 density.

The general incoherent/rank-at-least-two packet remains unpaid. Formally duplicating the shared coordinate into independent row and column copies would turn the same coefficients into an order-three crossing block, but the copies are the same physical random variable in QFORM. Such duplication is not permitted. The next exact analytic debt is therefore an overlap-aware shared-coordinate receiver consuming S0 without inventing independence.

The indicative value C3*S0^(-1/6)=72.853 is recorded only as the constant that an independence-preserving order-three receiver would deliver; it is not claimed for the physical law.
