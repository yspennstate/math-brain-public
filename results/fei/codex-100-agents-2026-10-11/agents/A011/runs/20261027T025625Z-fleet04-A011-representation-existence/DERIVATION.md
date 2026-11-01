# A011: inherited references repair the physical transaction theorem

All entropy, complete cross-entropy CE, and divergence D=CE-H are in bits. Full FEI remains open. The previous v5 equation (6) omits a nonnegative term. A094's objection holds unchanged; A100 supplies an independent reconstruction. The terminal-functional estimates are separate from that incorrect identification.

## 1. Exact physical-query contraction

Fix a Boolean target on a finite uniform cube. P is its squared Fourier law and Q is a covering finite-cost subprobability reference of mass s in (0,1]. At a physical query, group parent atoms into pairs, writing m(T)=P(T,0)+P(T,1) and r(T)=Q(T,0)+Q(T,1). The true child laws P_b satisfy (P_0+P_1)/2=m. This follows by expanding (u+v)^2 and (u-v)^2. Thus m=0 implies both child probabilities are zero.

Use exactly the existing inheritance: raw Q_b(T)=r(T)P_b(T)/m(T) for m>0 and raw Q_b(T)=r(T) for m=0. Let Z_b be its total mass and Q_b^inh=s raw Q_b/Z_b. Cover implies Z_b>0: each true child has total probability one and a positive reference on its support. Ghost reference fibers contribute to Z_b even though their true mass is zero. In particular (Z_0+Z_1)/2=s, including these fibers. Each child reference has mass s.

Finite algebra gives

    avg_b D(P_b || Q_b^inh) = D(m || r) + avg_b log2(Z_b/s).

The query contraction is

    delta = D(P||Q)-avg_b D(P_b||Q_b^inh)
          = sum_(T:m>0) m(T) D(P(.|T)||Q(.|T))
            - (1/2)log2(Z_0 Z_1/s^2) >= 0.                 (1)

All conditional reference pairs are probabilities because r>0 on m>0. The first term is a conditional KL divergence. The second is nonnegative since Z_0 Z_1<=s^2. Equality requires both matched conditional pair laws on every occupied fiber and Z_0=Z_1=s. Neither condition alone is used as a substitute for both. For Q=sP, both hold; this checks the zero-cost boundary. Complete divergence is nonnegative for a subprobability Q because D(P||Q)=D(P||Q/s)-log2 s.

## 2. Two ledgers, with exact conversion charges

At node v write lambda_v=2^(-depth v). After inheritance, conversion to the prescribed child model R_vb costs e_vb=(lambda_v/2)[D(P_vb||R_vb)-D(P_vb||Q_vb^inh)]. Signed costs retain negative values. Let E be their sum, Qloss=sum_v lambda_v delta_v, and Dbar the complete terminal divergence, with both children and all leaves included. Cancellation of the finitely many interior divergences proves

    Dbar = D_root + E - Qloss,
    Braw := CE_root+E = H_root+Dbar+Qloss,
    Lterminal := H_root+Dbar = Braw-Qloss.                 (2)

The same identity applies at every full frontier. There is no infinite-sum interchange. A target change is a separate transaction and is not counted as a same-target reset. Query contraction cannot be credited a second time if a bank has already used the complete CE release.

Consequently the previous v5 terminal bound yields only

    KI(F)-Braw-U = KI(F)-Lterminal-U-Qloss.                 (3)

For the prescribed v5 descendant floors the numerical residual alone does not establish payment until Qloss is bounded from the same original account. This obligation remains open. Equations (1)--(3) are a reconstruction of A094's unchanged objection, not a claim that A011 independently discovered it.

## 3. Exact witness in the allowed b>=12 construction

Take g(x)=(-1)^x on one source bit, b>=12 padding bits, one fresh control w, supplied original reference P_g, c=C0=0. Put n=1+b and epsilon=2^(-n). Flip the point with x=padding=w=0. At the root the actual first floor has beta=3epsilon. Its data marginal and reference for old coefficient A are

    q(A)=(A-epsilon)^2+epsilon^2,
    R(A)=(A^2+3epsilon^2)/(1+3epsilon).

There is one A=1 and 2^n-1 atoms A=0. The full parent reference uses the true control kernel. Thus its conditional-pair KL term in (1) is zero. On querying w,

    Zclean=(1+3epsilon^2)/[(1+3epsilon)(1-2epsilon+2epsilon^2)],
    Zedit=2-Zclean,
    denominator-numerator=epsilon(1-epsilon)(1-6epsilon)>0,
    delta=-(1/2)log2(Zclean Zedit)>0.                       (4)

Here 0<epsilon<=1/8192<1/6; all denominators and normalizers are positive. The exact rational certificate 1-Zclean Zedit=(1-Zclean)^2 proves the sign without subtracting floating entropies. This witnesses a real missing charge, not failure of the large reserve to cover it.

## 4. A complete all-policy transaction theorem with inherited descendants

Retain the original conditional source and root construction: any nonconstant Boolean g on a>=1 bits, supplied covering reference R with c=CE(P_g,R)<=C0 I(g), fixed b>=12, and any finite sequence of actual point edits with nonempty fresh control blocks of widths r_j. Write D_j=a+b+sum_(i<=j)r_i, rho_j=2^(-D_j), A_j=1+j(j+1), B_j=1+4j(j+1), and S=sum_j A_j rho_j D_j. At the ROOT use the actual first 6rho, second 8rho, and later 4B_j rho floors and true fresh-control kernels. This is exactly v5's root model, denoted R_M.

The repaired reference policy is explicit: fix this final root model once; on ANY finite adaptive physical tree inherit it by section 1, with no descendant conversion. Coordinates are not repeated along a branch. Stop anywhere. Earlier target prefixes are extended by zero frequencies to the final cube. Descendant models retain mass and ghost fibers but are not asserted to be the locally rebuilt v5 floors.

Every same-target reset charge is now zero. Equations (1)--(2) give, for every tree/frontier,

    Braw=CE(P_F,R_M)=H(F)+Qloss+Dbar,
    0<=Qloss<=D(P_F||R_M),
    Qloss+Dbar=D(P_F||R_M).                              (5)

Thus all the physical query contraction is paid inside the original root bill. No hypothetical source certificate or query credit is introduced. This is an actual complete transaction result for inherited references; it does not settle local-floor compatibility.

### 4.1 A useful compatible interface: vacuum calibration

The new A050 vacuum-calibration dependency gives more than an optional uncalibrated policy. This paragraph derives its relevant specialization directly. Write the actual inherited subprobability model as Q=s q, keeping its mass penalty -log2 s. Let r=P(empty) and z=q(empty). For r<1, cover implies z<1 and set q*(empty)=r, q*(T)=(1-r)q(T)/(1-z) on nonempty T. For r=1 set q*=P. Prescribe the ACTUAL full reference Q*=s q*, so scalar mass remains s. Direct summation, including r=0 and r=1 by zero conventions, gives

    CE(P,Q*)-CE(P,Q)=-D(Bern(r)||Bern(z))<=0.           (5a)

Thus arbitrary physical queries followed by these mandatory normalized-vacuum calibrations have E<=0 and Braw<=CE(P_F,R_M); Qloss+Dbar<=D_root still holds. At s=1 this is exactly the actual vacuum condition in A050. At s<1 it is explicitly a condition on the NORMALIZED SHAPE; no assertion that the actual vacuum mass equals r is made, and -log2 s remains in every complete terminal. Constant leaves retain Q*=s P and D=-log2 s.

For the moving-witness representation, every finite covering q has q=beta P+sum c_W delta_W with beta=(1/2)min_(P(W)>0)q(W)/P(W)>0 and residual coefficients c_W=q(W)-beta P(W)>=0. There are at most 2^N original witness labels, including ghosts. Since the weighted mean of q/P on occupied atoms is <=1, beta<=1/2. The inherited normalized shape has exactly the usual moving-label form under K_b=P_b/(2m) on m>0 and K_b=1/2 on m=0. Calibration scales the nonempty coefficients by (1-r)/(1-z), changes beta to beta* = beta(1-r)/(1-z)<=1, and uses one reusable empty witness with coefficient r(1-beta*). For r=1 take beta*=1. All denominators and coefficients have their stated sign. No fixed nonempty floor or fixed alpha is preserved. This is a specialization of A096's ghost-complete transport and A050's calibration, not a new proof of their whole statements. It makes the repaired policy compatible with a concrete hereditary interface, while leaving initial influence pricing unpaid.

For clarity the root price is rederived, without the disputed v5 equation (6). If h is the old target on n bits, r>=1 fresh controls, t=2^-n and p=2^-r, then rho=pt and the new data marginal is q_T=A_T^2-4rho b_T A_T+4pt^2, where b_T is a sign. Young's inequality yields q<=alpha P_h+gamma U_n with

    j=1: alpha=9/8, gamma=36rho;
    j=2: alpha=5/4, gamma=20rho;
    j>=3: alpha=1+1/[8j(j+1)],
          gamma=4(1+8j(j+1))rho<=2 beta, beta=4B_j rho.

Indeed the constant term after Young is 4pt^2+4rho^2/eta; dividing by the uniform atom t gives 4rho(1+p/eta)<=4rho(1+1/eta). It bounds the cross term for either edit sign.

The floor is (Q+beta U_n)/(1+beta). Since its mass is <=1, all its losses are nonnegative, so the pointwise domination can be integrated. Its data CE is at most alpha CE_old+(alpha+gamma)log2(1+beta)+gamma[n+log2(1/beta)]. Here log2(1+beta)<=2beta and <=d=D_j. The latter follows from beta<=6 or 8 at the first two stages; later 1+beta<=5+16j(j+1)<=2^(j+5)<=2^d for j>=3. The polynomial inequality starts at j=3 and follows inductively. Also n+log2(1/beta)<=2d.

The control law has nonempty mass e=4p(1-p)t, uniform among the nonempty control frequencies. Since r>=1, 2rho<=e<=4rho. Therefore H(control|data)<=H(control)<=h2(e)+er<=4rho(n+2r+2)<=16rho d, using h2(e)<=e log2(1/e)+2e. At root n>=13, so there is no e=1 logarithm endpoint; limits give the usual boundary convention. Combining these bounds gives

    c_1<=9c/8+160rho_1 D_1,
    c_2<=45c/32+200rho_1 D_1+112rho_2 D_2,
    c_j<=alpha_j c_(j-1)+64B_j rho_j D_j (j>=3).

Since sum_(j>=3)(alpha_j-1)=1/24 and finite product(1+eta)<=1/(1-sum eta),

    CE(P_F,R_M)<=135c/92+
       (24/23)[200rho_1D_1+112rho_2D_2+64sum_(j>=3)B_jrho_jD_j]
       <=135c/92+320S.                                  (6)

The M=0,1 endpoints satisfy the same bound directly. The last comparison uses B_j<=4A_j and 6144/23<320; first and second coefficients are smaller still.

## 5. The same original owner pays the inherited-reference theorem

The geometric sums sum A_j 2^-j=9 and sum j A_j 2^-j=34 give S<=2^(-a-b)[9(a+b)+34]. A nonconstant a-bit Boolean function has at least a boundary edges, hence I(g)>=a/2^(a-1); dummy coordinates do not invalidate this lower bound. One proof of the edge count is cube induction: if both half-cube cuts are nontrivial, their internal boundaries contribute at least 2(a-1)>=a; if only one is nontrivial it contributes a-1 and at least one cross edge; if both are constant but different there are 2^(a-1)>=a cross edges. Thus

    S/I(g)<=(9b+43)/2^(b+1)<=151/8192.

Both displayed b-functions decrease for b>=12. At edit j, if d_(j-1) is the actual previous pivotal degree at its point, literal edge counting gives E_j=2rho_j d_(j-1), G_j=2rho_j(D_j-d_(j-1))>=0 and I(F)=I(g)+sum(G_j-E_j). Since sum E_j<=2sum rho_jD_j<=2^(1-a-b)(a+b+2), we have sum E_j/I(g)<=15/4096. These facts hold even for signs that undo earlier edits.

For the SAME original K=4C0+15 and FULL old 0<=U<=(C0+37/8)I(g), equations (5)--(6) imply

    KI(F)-Braw-U >=
       [(35751/23552)C0+18111/4096]I(g)+K sum G_j >0.    (7)

The C0 coefficient is 4*(4081/4096)-135/92-1; the constant is 15*(4081/4096)-320*(151/8192)-37/8. No new owner is opened. For target changes, a previously booked root bill is changed by its actual signed difference c_j-c_(j-1); independently paying each complete history from a fresh budget is not asserted.

## 6. Scope of the repair and the universal line

Version 6 retains v5's numerical terminal-functional statement only at that scope and adds the complete transaction theorem (7) for inherited descendants. The all-local-floor transaction claim is withdrawn pending an accumulated Qloss bound; neither a zero-cost admission to those floors nor a useful arbitrary-core initial O(I) reference follows. The checks below test (1)--(5) on actual Boolean restrictions, ghost fibers and subprobability masses, and (4) at allowed padding sizes. They do not replace the analytic finite-tree and all-dimensional arguments above. The first unpaid universal line remains the original arbitrary-core source or required compatible admission, priced from unused original influence.

The optional extension (5a) adds compulsory normalized-vacuum calibration at every query. It consumes the newer A050 interface instead of extending another closed edit history. Independent review of this repaired version is pending; A094/A086 are credited for the accounting correction, and A050/A096 for the inherited compatible interface.
