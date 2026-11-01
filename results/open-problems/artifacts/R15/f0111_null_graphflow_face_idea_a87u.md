# R15 idea note — F0111 k=2 null graph flow versus global two-coordinate faces

UTC 2026-09-19. SELF_CHECK_ONLY / NOT CLAIMED. This is a retained-screen idea, not movement on retired-handoff I0076.

The preceding R15 report reduced unequal-amplitude two-block Hessian-null candidates to three scalar regimes. The new route is not to differentiate the one-dimensional partition function again.

1. Dualize the contact-Hessian kernel equation. For `F(t)=sum_i t_i-log(sum_i exp(t_i)-(n-1))`, put `r_i=exp(q_i)/S(q)` and `p=sum_i r_i h_i`. If a quadratic exact-contact gap `G=P-F` has `H_G(q)h=0`, then

   `sum_{j != i} B_ij h_j = r_i (p-h_i)`.

   For `h=a 1_J-b 1_K`, this is a weighted graph-flow system. Test whether its nonnegativity alone eliminates the three scalar regimes.

2. Find why that algorithm fails. If both active blocks have at least two vertices, the bare nonnegative row system appears always realizable: choose a large total cross-flow W, use equal positive internal degrees in each active block, and realize the cross marginals by a rank-one transport matrix. Rest vertices can be repaired independently because their h-coordinate is zero. Thus kernel-row nonnegativity by itself is likely vacuous in the genuinely multi-vertex case; full PSD and global majorization must enter.

3. Use the smallest global face instead. On the two-coordinate equal ray `t=s(e_i+e_j)`, the exact k=2 hazard is

   `f_2(s)=2s-log(2 exp(s)-1)`.

   The elementary inequality `f_2(s) >= s^2/(1+s)` should give a sharp closed-form necessary coefficient condition for any global quadratic majorant. At an interior contact, PSD supplies an independent upper bound on `B_ij` from the direction `e_i-e_j`. Combine the two.

4. Stress-test whether even full local PSD can coexist with the preceding null-curve conditions while globality fails. A promising exact rational scalar point in the surviving `z>1` branch is

   `delta=4/5`, `z=31/20`, `n=4`, two coordinates in each active block, no rest coordinates.

   The cubic-null formulas give

   `x=39151/26160`, `y=14993/8720`, `k=-5797/2616`, `S(q)=7848/5797`,
   `exp(u)=6909/6820`, `exp(v)=12267/10540`,

   with `q=(u,u,v,v)` and `h=(9/5,9/5,-1/5,-1/5)`. Solve the block-symmetric exact-contact equations for the unique cross coefficient. The target is to certify, using exact rational log intervals, that all polynomial coefficients are positive and the full contact Hessian is PSD with h in its kernel, while the two-coordinate face coefficient condition fails. If so, this proves that the remaining obstruction is genuinely global, not merely another local derivative or graph-flow constraint.

Methods used in new roles: #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #4 PROVE SOMETHING WEAKER COMPLETELY.
