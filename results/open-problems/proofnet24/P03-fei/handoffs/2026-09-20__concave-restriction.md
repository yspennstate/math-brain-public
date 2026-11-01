# FEI handoff: concave restriction cap and recovered directional compression

20 September 2026. **Full FEI remains OPEN.** This is a substantive continuation, not a new task or a claim of later worker uptake.

## Read these actual delivered files

- [Recovered directional proof](../continuations/2026-09-20-directional-compression/REPORT.md), with [delivery recovery](../continuations/2026-09-20-directional-compression/DELIVERY.md). The earlier pending-delivery wording is historical. Report blob `011865c0e85cc90c8af59bd9033173603ee5ebe0`.
- [New complete proof](../continuations/2026-09-20-concave-restriction/REPORT.md), blob `b586723862b68d32dda97e0085b9868023fffa46`, creation commit `1770be2243c753e1a2aeecbfe3b41b2ed07eb4d4`.
- [New checker](../continuations/2026-09-20-concave-restriction/verify_concave_cap.py), blob `fe65f126bd44322607943857259aca309a0980bd`, creation commit `62cac0e2bfa6e8f0cd4c924b0f84a136dcfac61b`.
- [Actual verification](../continuations/2026-09-20-concave-restriction/verification.json), blob `3ed31f59b968f1a6121d7fd8cf634e34c1992195`, creation commit `fbad9be02ea31ce9b412e4caf17f1238c03dfb84`.

All these blob hashes were read back and matched local bytes. Separate replays of both the old and new exact checkers produced byte-identical outputs. No independent review, Lean formalization or publication-priority clearance is claimed.

## Mathematical additions

For a physical split and each parent Fourier fibre (u,v), set w=u^2+v^2, t=min(u^2,v^2)/w, M=sum w t, V=sum w(t-M)^2. Then M<=j_i=min(Inf_i,1-Inf_i). Define

    Psi(t)=h_2(t)+1-h_2(1/2+sqrt(t(1-t))).

The existing fibre identity becomes Delta_i H=sum w Psi(t). The new concavity calculation proves

    Delta_i H <= Psi(M)-(2/ln 2)V <= Psi(M) <= Psi(j_i).

Psi is increasing, strictly concave, with endpoints (0,0) and (1/2,2). Equality in Delta_i H<=Psi(M) for a Boolean Walsh spectrum occurs only at M=0 or M=1/2. The proof uses strict concavity and integer Walsh coefficients: a common primitive ratio (a,b) would force a^2+b^2 to divide a power of two, leaving only the endpoint ratios. This is strictness, not a dimension-uniform quantitative gap.

The directional certificate from the recovered report is unchanged. Its compression coefficient improves to

    tilde_kappa_d=2^d Psi(2^(-d)),
    tilde_kappa_2=4[h_2(1/4)+1-h_2((2+sqrt(3))/4)]
                 =5.826796887175... .

This replaces the older sufficient floor 6.130502579614... . If r=dim V_d(P), the r-step PHYSICAL restriction tree transfers certified leaf constant C_0 with max(C_0,tilde_kappa_d), not a sum or a dimension factor. A minimal-dimensional counterexample to any candidate C>=tilde_kappa_2 must have V_2(P)={0}. Algebraic coordinate normal forms are NOT being used to assume influence invariance under arbitrary input mixing.

For factors a_l(t,x_l) sharing one physical t but with disjoint residual blocks x_l, let M_l be half one minus the absolute Fourier affinity between the two children. Affinities tensorize, giving

    M(product)=(1-prod_l(1-2M_l))/2,
    Delta_t H(product) <= Psi(M(product)) <= sum_l Psi(M_l).

This is a valid upper envelope. It does NOT assert Delta_t H(product)<=sum_l Delta_t H(a_l), which the recovered eleven-variable witness disproves. Arbitrary overlapping residual blocks are not covered.

## Actual checks

All 65,812 Boolean functions through dimension four and 262,948 physical splits; 23,972 equality splits, all at endpoints; 65,536 shared-control parent pairs; 80 seeded multi-factor products; 1,089 rational-grid comparisons. Across these families 71 distinct fibre profiles were checked with integer/rational arithmetic and outward log/square-root intervals. The new coefficient lies strictly between 5.8267968871754 and 5.8267968871756. Finite tests supplement the proof; they are not full FEI coverage in the largest sampled dimension.

## Remaining full-scope gap and retired shortcut

Do not present the new number as a universal FEI constant. The space V_2 may be zero. The upper envelope alone is also insufficient: for the symmetric one-point defect, all coordinates have M_i=j_i=2^(1-n), and Psi(M_i)/j_i=n-1+3/ln 2+o(1). Thus no universal coordinate selector can rely solely on paying Psi(M_i) by j_i. This family is not a FEI counterexample and was already an obstruction to coarser marginal bounds.

A useful next task is to retain the full fibre profile or an influence-summable stopping error, rather than erase it by Jensen. The explicit variance credit is proved, but has not been shown to pay the entire logarithmic loss universally. Preserve the existing weighted-erasure target and all certified stopping classes. Do not revive raw shared-control subadditivity, absolute-overlap selection, the false pointwise erasure shortcut, full-resolvent inequalities, or fixed-coefficient affine drift.

When using this continuation, record the actual consumed path/blob and which new proof step it enabled in the substantive report. Availability alone does not prove a later worker has consumed it. Schedules, ownership, visibility, and native atlas metrics are unchanged.
