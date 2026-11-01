# C0048 referee attempt — w458

2026-10-10. Parent conjecture: for integer q,d>=3, nearest-neighbor ferromagnetic Potts on Z^d has M(beta_c)>0. In delta-spin normalization, p=1-exp(-beta) and M(beta)=theta_w(p), the wired FK probability that the origin belongs to an infinite open cluster. The exact source and limitations are in SOURCE_STATUS.json.

## Hardest input

The outstanding case includes q=d=3. The shortest rigorous route in the peer packets is to show a constant eta>0 such that theta_w(p)>=eta for **every** p in (p_c,p_c+epsilon). w457's checked right-continuity would then yield theta_w(p_c)>=eta. w456 replaces this with SP(q,d): an actual lattice branch potential on a fixed interval, with positive uniform cubic coefficient, uniform C1 quartic remainder, and a physical stationary/minimum comparison. Its elementary exclusion lemma would give eta. These are equivalent in consequence but SP is a stronger and structurally different input. Neither is proved.

## Attempt through cluster-color cumulants

Try to obtain w456's uniform potential from field derivatives. On a finite free-boundary graph, write X=sum_x(1{sigma_x=1}-1/q) and P_G(h)=N^-1 log E exp(hX). The exact cumulants are P''=a2 E S2/N and P'''=a3 E S3/N. Since S2^2<=N S3, their ratio satisfies B/(6A^3)>=q(q-2)/[6(q-1)A], with A=P'' and B=P'''. This does not produce a fixed b>0 if A can grow. A uniform lower bound on B/A^3 would still need a uniform fourth-order remainder, not just derivatives at h=0.

The decisive obstruction appears at fourth order: P''''=[a4 E S4+3a2^2 Var(S2)]/N. The variance term survives FK averaging and may compete with the negative q=3 single-cluster term. It cannot be discarded by a sign argument. Exact enumeration at q=3 on a two-vertex edge with exp(beta)=2 gives unnormalized cumulants (5/9,7/27,-8/27); this confirms the formula but provides no volume-independent bound. At beta=0, P'''=a3>0 even though the spins are independent and the pressure is analytic, so the cubic sign alone has no first-order content. At planar q=3 the same sign coexists with a continuous thermal transition, as the 2017 primary lecture source states.

One might identify the Legendre transform I(m)=sup_h(hm-P(h)) with the desired branch potential. This does not work without a separate argument: I is convex by definition and, at coexistence, may have a flat segment. The nonconvex scalar entropy J_q(m)-lambda m^2 used in mean-field theory is an exact special model calculation, not a bound for nearest-neighbor constrained free energy. The peer derivation gives q=3 mean-field b=1/3 and C=8/9, but the spatial correction and physical branch link remain uncontrolled.

## Result and next proof step

The attempt proves only the finite-volume identities and a conditional reduction already scoped in REVIEW_PACKET.md. The single missing mathematical estimate is a q=3,d=3 lattice-uniform ordered-branch gap, expressed either directly as inf_{p_c<p<p_c+epsilon} theta_w(p)>0 or through SP(3,3) with a justified physical potential. A useful next attack would derive an explicit fixed-scale inequality that bounds the spatial-correlation correction to the constrained potential on a beta interval approaching beta_c, then check whether its constants remain positive at q=3,d=3. No such inequality is established here.
