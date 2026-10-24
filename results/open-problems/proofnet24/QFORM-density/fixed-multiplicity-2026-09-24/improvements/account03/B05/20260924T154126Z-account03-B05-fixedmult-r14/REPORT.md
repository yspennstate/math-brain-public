SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T15:41:26Z.

# account03/B05 r14 — s8 B05 audit and s7 coarea/minor escalation

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.
Execution label: WITHOUT_VERIFIED_BRAIN.

Pinned standalone source: yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f, paper.tex blob 19fb119877426b640b2c0dae19ec2f78a399fe11.

Later candidate inspected: yspennstate/math-open-problems@42decd5b0bac31666cbbc613bcd2d64194775063, asserting s_8(A)>=s => ||p_Q||_infinity<2400 K^2/s. Two distinct complete PASS reviews are now present at 63696675198a6f7359f17414d55cc27a68116656 (account03/B08) and d4eee5296bcc7fea885435e9cee72379d0e902eb (account03/B18). This report does not itself promote release status.

## B05 audit of the s8 analytic interfaces

PASS — product projections. The nine-eigenvalue proof uses a deterministic orthogonal fiber parametrization and geometric Brascamp-Lieb, not independence after rotation. The density bound ||p_(U^T X)||_infinity<=e^(d/2) is valid for arbitrary rough cap-one product laws. The known wording repair is sum_(b_i>0)(1-b_i)<=d after zero rows are omitted.

PASS — product-safe incident receiver, source d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f. For a literal pair H and complement L, if Delta=det(CC^T)>0 and s_8(A)>=1, then s_4(D)>=1 and
W_tot(H)=Delta ||D(I-P)||_F^2>=Delta.
For the disjoint part W_dis, a fair original-coordinate cut keeps each term with probability 1/16. On a chosen cut,
W(I,J)=S^2 Z_1
by the exact three-row Gram/Cauchy-Binet identity. Diffuse residual rows use the reviewed grouped (k,l)=(2,1) compiler with the two literal anchors; one heavy residual row is promoted as a third literal hub. Hence
||p_Q||_infinity <= C_inc W_dis^(-1/6),
C_inc=3*2^(5/6)*e^(2/3),
and this branch has a C_0 density. No conditional projection cap is asserted.

PASS — zero/one-high leverage closure, source 74542593cca87e76d83b07f98e2c895f76b90796. With q_i the leverage scores of the rank-two cross map and J={i:q_i>2/3}, |J|<=1 implies W_dis>g/48. The contradiction uses a zero-diagonal error E with ||E||_F<=1/4, global remainder rank <=5, restricted low-low rank <=2, and a 3x3 strictly diagonally dominant physical restriction forced by s_8.

PASS — two-high endpoint, source 42decd5b0bac31666cbbc613bcd2d64194775063. If q_i,q_j>2/3, the determinantal weights w_ij=det(C_{ij})^2/g give w_ij>1/3. Since g>8/25, det(C_ij)^2>8/75. No-pivot physical entry bounds give |det C_ij|<101/5000, so det(C_ij)^2<10201/25000000<8/75, contradiction.

PASS — exceptional slices in B05 scope. The designated partner account04/B05 audit at 84b63093480022df1a463895b8b77eb2a2ea19db reconstructs definite/hyperbolic coarea through nonnegative test functions and Tonelli, so condition-dependent critical levels are not silently treated as common pointwise exceptional sets.

Actual partner application: in the normalized s8 pair-pivot branch, any literal definite principal pair with |det B|>=1/100 obeys
||p_Q||_infinity <= pi/sqrt(|det B|) <= 10 pi <31.416.
All conditioning is on original coordinates.

B05 verdict on the s8 chain: PASS for product-projection, coarea, rough-law, conditioning and exceptional-slice interfaces. This is not presented as a third full structural review.

## New s7 result

The complete proof and exact arithmetic are in TECHNICAL_LEMMA.md in this same immutable run folder.

The new theorem QFORM-S7-GOODSEED-PAIR-ESCALATION-v1 is:

In the normalized no-pivot chamber eta=1/100, kappa=1/6400, let B=A[S,T] be a nonsingular good order-two interpolation seed with ||E||<=epsilon_*=3sqrt(2)/80 and assume s_7(A)>=1. Then some h outside S union T gives two literal successor 2x2 minors C1,C2 satisfying

C1^2+C2^2 >= R_esc det(B)^2,

R_esc=((1-epsilon_*-eta)^2)/(2(eta+eta^2))
     =78633/1616-(1485 sqrt(2))/404
     =43.4607496531583....

Hence one successor has determinant square >21.73037 times the seed determinant square.

In the unpaid small-V3 branch, good seeds carry at least V2/2. Counting both successor incidences gives

sum_(H,T) m_(H,T) det A[H,T]^2
 >= R_esc V2/2.

Since sum_(H,T)det A[H,T]^2=V2, the determinant-volume weighted average incidence multiplicity is >21.73037. Therefore

max_(H,T) m_(H,T) >=22.

An explicit symmetric no-pivot family in TECHNICAL_LEMMA.md shows m_(H,T) can be arbitrarily large purely combinatorially. Thus the exact missing factor is not local determinant size but many-to-one source sharing: a successful s7 receiver must spend the repeated predecessor bank before conditioning or reciprocal-minor selection.

## Status

Multiplicity eight: complete candidate with two distinct full PASS reviews observed; owner-level promotion not asserted here.
Multiplicity seven: OPEN.
Unrestricted three-large-eigenvalue conjecture: OPEN / NOT PROVED / NOT DISPROVED.
Global continuity: OPEN outside branches where an L1 characteristic-function estimate is proved.
