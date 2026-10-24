SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T11:05:46Z.
attacking: aggregate a disjoint fresh source bank before the curved pushforward, then use a quantitative cross-volume cut to recover continuity while preserving the partner's sharp essential bound.

Programme: QFORM-DENSITY-3EIG-20260922. Full target OPEN. Continuity tracked separately. Execution status: WITHOUT_VERIFIED_BRAIN.

Substantive checkpoint. For the latest account02/B16 family, write theta=eta^2(1+rho^2), s^2=1+theta, normalize p=y/s, and use the orthonormal spectral frame R=[p,u,v]. If m is divisible by 8, split exactly half of each of the four shared sign classes and half of the fresh bank into a diffuse side J, leaving the hub in I. Then

S_J=R_J^T R_J=diag(theta/(2s^2),1/2,1/2),
S_I=I-S_J=diag((2+theta)/(2s^2),1/2,1/2).

For a shared row j in J, the leverage in col(R_J) is

r_j^T S_J^{-1} r_j = (2/m)[(1+rho tau_j)^2/(1+rho^2)+1] <= 6/m,

while a fresh row has leverage 2/m. Hence m>=16 forces max row leverage <=1/2. The cross block A_{J,I}=R_J Gamma R_I^T has the same nonzero singular values as S_J^{1/2} Gamma S_I^{1/2}, so

s_3(A_{J,I}) >= s_min(Gamma) sqrt(theta)/(2s).

For Gamma=4[[delta s^2,s,0],[s,0,0],[0,0,1]], the partner eigenvalue calculation gives s_min(Gamma)>=4s/(1+delta s), and therefore

s_3(A_{J,I}) >= 2 eta sqrt(1+rho^2)/(1+delta s).

This makes the newest volume-stability theorem applicable with E=0. The intended synthesis is: partner account02/B16 gives ess sup p_Q<=4; volume stability gives existence of a continuous density representative. Continuity plus the a.e. bound then upgrades the same representative to pointwise sup<=4.

Control refresh pinned at math-research-brain@daef91678005d93e27eb75e565e7f8c2a50d689f, OWNER CONTROL revision 2026-09-22.15. Latest partner source: math-open-problems@ade5cfe51d454341667779f7d9da714e4de99ed9. New volume-stability source required by the owner continuation: math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba.
