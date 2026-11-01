# Independent reconstruction of the repaired physical reference bill

A011 version 6 holds at its stated inherited-reference scope. The original arbitrary-core source remains unpaid. The reference class in this result does not include prescribed fresh nonempty floors.

## 1. Signs, normalization and the exact query loss

Let f be Boolean on a finite uniform cube. At a query write its signed Fourier coefficients as u_T and v_T for the two parent frequencies. The actual restricted coefficients are u_T+v_T and u_T-v_T. Thus

    P_+(T)+P_-(T)=2(u_T^2+v_T^2)=2m(T).

The cross terms cancel before any absolute value or square is bounded. Each child has total mass one because it is itself Boolean. In particular m(T)=0 implies both child masses vanish. This is a finite algebraic identity, with no limit or exchange of sums.

Let the covering parent reference Q have mass s in (0,1], and let r be its marginal under the query. Set K_b(T)=P_b(T)/(2m(T)) on m>0. On a ghost fiber m=0 choose any stochastic pair K_+(T),K_-(T); equal halves give precisely A011's prescription. Define raw child references L_b=2rK_b, Z_b=sum L_b, and Q_b=sL_b/Z_b. Their mass is s. Cover implies Z_b>0 and Z_++Z_-=2s, including every ghost.

On occupied child cells Q_b/P_b=sr/(mZ_b), so direct summation yields

    average D(P_b||Q_b)=D(m||r)+(1/2)log2(Z_+Z_-/s^2).

The contraction is therefore

    delta = D(P||Q)-average D(P_b||Q_b)
          = sum_T m(T) D(P(.|T)||Q(.|T))
            -(1/2)log2(Z_+Z_-/s^2) >=0.

The conditional terms are normalized because r>0 wherever m>0. AM-GM applies to positive Z_+,Z_-. Complete D(P||Q)=D(P||Q/s)-log2(s) retains the scalar mass. If Q=sP, both terms vanish. Ghost choices affect the outcome term and cannot simply be removed.

This reconstructs A011 DERIVATION section 1 without changing its equal-ghost specialization. It also reconstructs the portion of A096 ghost transport needed here. In the moving-witness decomposition Q=beta P+sum c_W delta_W, each original label follows the SAME K. Reference outcome probability is Z_b/(2s), the new true-law coefficient is beta*s/Z_b, and every witness coefficient is c_W K_b(W)/(Z_b/(2s)). Their atomwise sum equals Q_b, including ghost-to-occupied collisions.

## 2. Full finite-tree bill and calibration

Use actual physical reaches lambda_v=2^{-depth(v)}. A reset after inheritance costs its actual signed divergence difference, weighted by the child's reach. Let E be their total, L=sum_v lambda_v delta_v, and D_leaf the reached average FULL terminal divergence. Exact cancellation of all interior divergences gives

    D_leaf=D_root+E-L,
    B_raw=CE_root+E=H_root+D_leaf+L.

This holds for every finite adaptive stopped tree, including both terminal children and constants. Thus H_root+D_leaf is a terminal functional, smaller than the actual transaction bill by L. A011 version 5's transaction identification is withdrawn; its separate numerical terminal estimate is not refuted.

For normalized-vacuum calibration write Q=sq, r0=P(empty), z=q(empty). When r0<1, cover implies z<1. Set q*(empty)=r0 and q*(T)=(1-r0)q(T)/(1-z) otherwise, and retain Q*=s q*. If r0=1 use Q*=sP. With zero terms understood by continuity,

    D(P||Q*)-D(P||Q)=-D(Bern(r0)||Bern(z))<=0.

This is an exact finite sum, including r0=0,1. If r0>0 then z>0 by cover. The subprobability mass s is unchanged, so a constant leaf still has full divergence -log2 s. All calibrations have nonpositive signed cost. Consequently B_raw<=CE_root, and L+D_leaf<=D_root. No query loss is credited twice. No nonempty floor is supplied by this identity.

## 3. Independent audit of A011's original source envelope

Here the detailed supplied-source construction and its actual first/two/later ROOT floors are exactly those in A011 version 6. The derivation below audits those definitions; it does not assume their old transaction reading.

At one edit let t=2^{-n}, p=2^{-r}<=1/2, rho=pt, and A the old signed coefficient. The new data mass is A^2-4rho b A+4pt^2. Young's inequality, applied after retaining the actual sign b, bounds this by (1+eta)A^2+4rho(1+1/eta)t. Choose eta=1/8, 1/4, and 1/[8j(j+1)] at the first, second and later edits. These give gamma=36rho,20rho and gamma<=2beta for the specified beta=4(1+4j(j+1))rho.

For the actual floor (Q+beta U)/(1+beta), every point loss is nonnegative because the reference is a subprobability. On the P term its loss is bounded by the old loss plus log2(1+beta); on the uniform term it is at most n+log2((1+beta)/beta). Thus CE_new,data <=alpha CE_old+(alpha+gamma)log2(1+beta)+gamma[n+log2(1/beta)]. The control contribution is at most 16rho D. Since D>=14 here, log2(1+beta)<=2beta and <=D, and n+log2(1/beta)<=2D, the loose coefficients 160,112,64B_j in A011 follow. For example the first cost is <=(27/2)rho+124rho D<=160rho D; the second is <=20rho+76rho D<=112rho D. Later, alpha<=97/96, beta=4B_j rho and B_j>=1 give a cost <49B_j rho D<64B_j rho D. The actual strong bounds n>=13 and nonempty fresh controls supply every endpoint used here.

The later amplification has sum_{j>=3}eta_j=1/24. For finite products with total eta<1, product(1+eta)<=1/(1-sum eta), by expanding nonnegative products or induction. Hence it is <=24/23. Multiplying the first two amplifiers gives (24/23)(45/32)=135/92. Since B_j<=4A_j with A_j=1+j(j+1), all additive costs are bounded by 320S, S=sum_j A_j rho_j D_j: (24/23)256<320, and the first two coefficients are smaller. M=0 and M=1 obey the same envelope directly.

The geometric sums sum A_j 2^{-j}=9 and sum j A_j 2^{-j}=34 give S<=2^{-a-b}[9(a+b)+34]. A nonconstant a-dimensional Boolean cut has at least a edges, even with dummy variables, so I(g)>=a/2^{a-1}. Therefore S/I(g)<=(9b+43)/2^{b+1}<=151/8192 for b>=12. Both b-dependent upper bounds decrease. Literal edge counting for each actual point edit gives E_j=2rho_j d_previous and G_j=2rho_j(D_j-d_previous)>=0, with I(F)=I(g)+sum(G_j-E_j). The function D*2^{-D} decreases for D>=2, so arbitrary larger fresh widths only reduce the upper sums. It follows that sum E_j/I(g)<=(b+3)/2^b<=15/4096.

For K=4C0+15 and the SAME old 0<=U<=(C0+37/8)I(g), direct rational collection gives

    K I(F)-B_raw-U >=
      [(35751/23552)C0+18111/4096]I(g)+K sum G_j >0.

Indeed the C0 coefficient is 4*(4081/4096)-135/92-1 and the constant is 15*(4081/4096)-320*(151/8192)-37/8. This uses the original source c<=C0 I(g) once, and calibrations only decrease the signed raw bill. The initial reference already contains its full entropy price. There is no inference that every arbitrary core has such an O(I) source.

## 4. Adversarial checks and exact scope

Potential failures tested explicitly: child normalization and signed cancellation; constant and irrelevant queries; covering references with ghost fibers; unequal ghost kernels; biased reference outcomes; scalar mass 1/2; early stopping and all terminal divergences; calibration at r0=0,1; exact SAME-owner constants; every sign of every attainable small-cube Walsh coefficient in the Young domination; allowed b>=12 normalizer witnesses. Logarithmic identities have the finite proofs above; floating diagnostics are not sign certificates. Fraction checks certify the finite atomwise identities, coefficient signs and scalar inequalities. The analytic proof supplies all dimensions and adaptive policies, rather than extrapolating the finite census.

No new general B07 entropy inequality is claimed. In particular this inherited continuation result is generic conditional on the actual normalized restriction laws; it is not new F^4=1 source admission. For the normalized real Fourier vector (4/5,3/5) on one bit, the purported child masses are 49/25 and 1/25, so this physical-child interpretation fails before any entropy conclusion. Full signed Booleanity supplies actual Boolean restrictions; it does not, here, supply the missing source price.

The independent review verdict for the EXACT A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@6 statement is HOLDS, within its supplied-source/inherited-reference scope and normalized-shape interpretation at mass<1. Its own exclusions remain in force. The exact original statement and hash are copied unchanged into the local claim record. A096's whole named theorem is not blanket reviewed: only its atomwise transport and full physical bill used by this audit are reconstructed.

Universal bridge: C024 history transfer and C019 stopping-tree payment advance by independent reconstruction of the repaired full transaction bill and the SAME-original-owner reserve, including ghost fibers and retained subprobability mass. This clears a concrete dependency for B07's inherited-reference route; the numerical universal FEI improvement is zero. C020's original arbitrary-core O(I) complete source remains unpaid, and fresh nonempty floors still need separately justified admission with actual query losses. NEXT prices that original source in the now explicit inherited/vacuum class, rather than adding another optional compatible reset.
