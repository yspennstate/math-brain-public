SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T05:05:09Z.
attacking: the newest fleet02/B07 incident-E2 branch by a sharp all-orders anchored compound-tail ladder; then use adjacent anchored-volume ratios to force a condition-number-free physical Schur low-tail alternative before any reciprocal minor selection.

# Early substantive checkpoint

Full QFORM remains OPEN. This checkpoint records the first proved calculation; no density conclusion is claimed yet.

Let M be any real m x n matrix, fix a physical row i and physical column a, and for k>=1 put

H_k^(i,a)(M) = sum_{|R|=|C|=k, i in R, a in C} det(M[R,C])^2,
T_k(M) = dist_F(M,{rank<=k})^2 = sum_{j>k} s_j(M)^2.

## New lemma (proved): anchored compound-tail ladder

For every k>=1,

    H_{k+1}^(i,a) >= [T_k(M)/k] H_k^(i,a).                 (1)

For M_{ia}=b !=0, write M=[[b,r^T],[c,D]] and S=D-c r^T/b. Exact scalar Schur expansion gives

    H_k^(i,a)=b^2 E_{k-1}(S),

where E_j(S)=e_j(SS^T). If S_{k-1} is a best rank-(k-1) Frobenius approximation and M_{k} is obtained by replacing D with c r^T/b+S_{k-1}, then rank M_k<=k and

    T_k(M)<=T_{k-1}(S).

The standard compound-tail inequality T_{k-1}(S)E_{k-1}(S)<=k E_k(S) therefore proves (1). For b=0 perturb only M_{ia} by epsilon and pass epsilon->0; H_k and T_k are continuous. The constant 1/k is sharp: M=I_{k+1}, anchored at (1,1), has H_k=k, H_{k+1}=1, T_k=1.

At k=2, (1) is exactly the newest designated partner fleet02/B07 theorem H_3 >= (1/2)T_2 H_2; thus this run genuinely applies and extends that completed result rather than merely citing it.

## Immediate new condition-number-free consequence

When b!=0, the same formulas and the compound-tail inequality give

    T_{k-1}(S) <= k H_{k+1}/H_k                         (2)

whenever H_k>0. In particular,

    T_2(S)<=3 H_4/H_3,
    T_3(S)<=4 H_5/H_4,
    T_3(S)^2<=12 H_5/H_3.                               (3)

No inverse power of the possibly tiny physical entry b remains in (2)-(3).

Newest partner source actually used: yspennstate/math-open-problems, path proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T043951Z-fleet02-B07-4c9e7a/REPORT.md. In its incident branch it gives T_2(M)>=theta F^2 and sqrt(H_2)>11 theta F^2/7200, hence H_3>omega(theta)F^6 with omega(theta)=121 theta^3/(2*7200^2). The next calculation will combine (3) with the e5 D5 failure H_5<=E_5<eta_*F^10 to obtain a same-anchor rank-2/rank-3 Schur collar and a concentrated-H_4 physical-core exit.

Execution status: WITHOUT_VERIFIED_BRAIN. Independent review not claimed.
