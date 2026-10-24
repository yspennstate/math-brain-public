# R15 idea-before-code note — N=12,13 heavy-coordinate / K-excess compression

Date: 2026-09-20 UTC.  Scope: retained Talagrand F0111 k=2 screen only; PENDING / SELF_CHECK_ONLY / NOT CLAIMED. This does not reopen I0076 and does not promote any queue item.

Immediate predecessor: `runs/R15/20260920_0514Z_successor_screen_f0111_n11_fullcell_elimination_n99v.md`, which eliminates N=11 and leaves N in {12,13} for the n=30 full-support two-level Hessian-null branch.

All 30 Section-B numbers have already appeared in older R15 history, so the globally-never-used condition is exhausted. This run deliberately avoids the predecessor's #5/#13/#18 triple and uses:

- #6 DEFORM TO A POINT YOU CAN SOLVE: trap each remaining scalar cell in a narrow rational slanted band and seek an exact projective-Gram heavy-coordinate threshold there;
- #14 FIND THE GROUP ACTING: test the block-constant S_M x S_N subfamily across the entire two remaining cells, not only at the z->1 boundary;
- #20 FIND WHY THE ALGORITHM FAILS: try to port the N=11 entropy elimination to arbitrary heterogeneity, and record the quantitative obstruction if the same route cannot close N=12 or N=13.

## Proposed new route before any checker

Write z=1+s, a=1+delta, b=1-delta, N=|K| and M=30-N. Carry the exact scalar quantities x,y,k,A_J,A_K,A_JK,L_K,Q_K,U_K and the residual Gram representation from the preceding reports.

### 1. Exact K-excess invariant

At any contact,

`sum_{j in K} exp(q_j) = S(q) y = U_K`,

because `S(q)=-29/k` and `U_K=-29 y/k`. Hence

`sum_{j in K} (exp(q_j)-1) = U_K-N`.

Since q_j>0 and exp(q_j)-1 >= q_j,

`sum_{j in K} q_j <= U_K-N`.

This is distribution-free and should compress all K-coordinate logarithms by the scalar slack to the U_K=N wall. On the N=12 and N=13 scalar cells, try to prove exact global roofs U_K-N<15/64 and U_K-N<439/2197 respectively.

### 2. Strong heavy-coordinate exclusion for arbitrary heterogeneity

Let r_* = max_{i in J} r_i. For a proposed threshold r0=1-C s, let ell=x-r0 and

`Tcap = y(N-L_K)`,

`e = r0(1-A_J r0)`,

`Delta = s(x-2 ell)/b - (b/a)Tcap - A_JK ell y`.

The previous residual-Gram argument shows that if `e>0`, `2 A_J r0>1`, `Delta>0`, and `Delta^2>e Tcap` throughout the scalar cell, then `r_*<r0` for every heterogeneous contact. Test C=15 on N=12 and C=17 on N=13.

### 3. Block-constant full-cell contradiction

If a contact point itself is block-constant, average the certificate over S_M x S_N. Then the within-K Hessian eigenvalue is `r_K-beta_K`, so PSD forces `beta_K<=r_K`. The K null equation gives an O(s) upper bound on the cross coefficient eta; the J null equation then gives an O(s) upper bound on beta_J. Exact value contact, however, is

`E = log S(q)-x u-y v = k log S(q)+x log(M/x)+y log(N/y)`.

The scalar cells are so narrow that the PSD-induced coefficient-energy upper bound should be <1 while the exact value side should be >2.6. If this survives exact rational log bounds, it removes the entire block-constant N=12 and N=13 subfamilies, not merely a boundary neighborhood.

### 4. Expected obstruction to a full heterogeneous elimination

The N=11 proof used a much stronger heavy-coordinate threshold (C=25). Preliminary hand algebra suggests the same projective-Gram inequality may top out around C≈15-18 on N=12,13. If so, the old entropy-energy upper bound remains too large because heterogeneous J-J coefficient flow can be routed through low-q light coordinates. Record this failure honestly rather than manufacturing another checker-only result.

No finite claim is asserted in this note; exact validation comes only after the route is written.