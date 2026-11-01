SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T16:14:04Z.
attacking: a two-physical-hub averaged-frequency compiler in which arbitrary curvature on the hub-slope bank is combined with a source-disjoint hyperbolic edge through an L2-in-frequency budget.

# Early substantive checkpoint

Goal: replace the false law-uniform scalar pointwise Fresnel estimate by a genuinely integrated mechanism.

Proposed packet: original independent coordinates split as physical hubs H=(H1,H2), a product bank Y, two further scalar physical coordinates U,V, and conditioned outside coordinates. After conditioning, assume

Q = H^T C H + 2 H^T (B Y + d) + R(Y) + 2 c U V + alpha U + beta V + const,

where C is arbitrary symmetric, B is 2 x m of rank two, R is an arbitrary measurable phase on Y, c != 0, and the groups H,Y,U,V are source-disjoint original coordinates.

Two ingredients already checked algebraically:

1. Product L2 lemma. If X,Y are independent probability densities with caps M,N, then the density q of XY satisfies ||q||_2^2 <= 4 M N. For cap-one X,Y and Z=2cXY+aX+bY, translation/completion gives ||p_Z||_2 <= sqrt(2)|c|^{-1/2}.

2. Two-hub Plancherel compiler. Let S=BY+d and, for each t, push e^{itR(Y)}dP_Y through S to obtain a complex density a_t with |a_t|<=p_S. Multiplying by the independent hyperbolic-edge characteristic function chi_Z(t) gives g_t(s)=a_t(s)chi_Z(t). The 2D projection bound gives ||p_S||_infinity <= 2 det(BB^T)^(-1/2), hence ||p_S||_2 <= sqrt(2) det(BB^T)^(-1/4). Plancherel in the two hub variables gives |phi_Q(t)| <= pi |t|^{-1} ||g_t||_2. Cauchy-Schwarz in frequency and Plancherel for Z should then yield an L1 characteristic-function bound, expected to optimize to

||p_Q||_infinity <= 3 det(BB^T)^(-1/6) |c|^(-1/3).

This would give a continuous density in this packet, retain arbitrary R(Y), and use no pointwise quadratic-phase decay.

Latest designated partner fleet02/B01 r46 (brain commit 18178557f2d489d701d736cc278f24dc8e17aca8; math report a9cb334579e92753035a96d258fa94cac01cdbfc) supplies an independent pair-Schur W2 receiver. The final report will apply that theorem to an explicit target-valid six-coordinate family and compare the two certificates at an actual inequality.

Full QFORM remains OPEN. The intended remaining structural gap is to route a general <=2-by-<=2 heavy-volume survivor to this source-disjoint hyperbolic-edge packet or to another already-paid receiver before selecting a tiny local minor.