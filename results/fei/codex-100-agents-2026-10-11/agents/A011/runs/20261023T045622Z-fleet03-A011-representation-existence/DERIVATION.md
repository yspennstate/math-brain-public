# Two actual nested edits, one original bank and unchanged rate

Author proof; independent reconstruction pending. Bits throughout. This refines the existing A011 arbitrary-core envelope, not a proof of full FEI.

Let g be nonconstant Boolean on a>=1 bits, with supplied subprobability R of mass s in (0,1], finite c=CE(P_g,R)<=C0 I_g. Write H=H(g), D=c-H>=0. Add b>=6 unused data bits and r1>=1 first controls. Translate the first edited point to zero. Put D1=a+b+r1, rho1=2^-D1, and let F1 flip g at that one point of its D1-dimensional cube. Add r2>=1 fresh controls and flip F1 at ANY point z* of its entire D1-cube when the fresh controls match their point. This genuine second operation gives F2 on D2=D1+r2 bits, rho2=2^-D2. The second point may agree with, overlap, or depart from the first edit. K=4C0+15 is fixed before either operation.

The F1 model at the root is exactly the old floor (Rpad+6rho1 U)/(1+6rho1), lifted by the true first-control kernel. At each old padding/source frontier it is exactly the model prescribed in A011 v2, not a fresh optimal code. Source models are inherited from ORIGINAL R, each retaining mass s and zero-true-fiber model mass. On the first active branch expose padding in any order, then source bits in any adaptive order; stop nonmatching siblings, leaving the first controls unqueried. Include every nonempty padding prefix and every source prefix, including full source collapse.

## 1. Smaller coefficient for the second prescribed floor

For ANY Boolean h on m>=1 bits, any finite-cost source subprobability Q, r>=1 point controls, p=2^-r,t=2^-m,rho=pt, the true data marginal after a point flip is q_T=A_T^2-4pt b_T A_T+4pt^2. Young's inequality with eta=1/2 gives

    q <= (3/2) P_h + 8rho U_m.

Define Qnew_data=(Q+8rho U_m)/(1+8rho), then lift by the TRUE conditional new-control law. The entire new mass is (mass(Q)+8rho)/(1+8rho); it is not discarded. Let beta=8rho<=2. Nonnegative log losses, log2(1+beta)<=2beta and log2(1/beta)=m+r-3 imply

    CE_data <= (3/2)c_h + beta(2m+r+4).

For completeness, total nonempty new-control spectral mass is e=4p(1-p)t, and Jensen gives conditional-control entropy B<=h2(e)+er. Since e<=4rho, e>=2rho, and h2(e)<=e[log2(1/e)+log2(euler)] with log2(euler)<2, we obtain the elementary bound B<=4rho(m+2r+2). Thus

    CE_new <= (3/2)c_h+40rho(m+r).                 (A)

Indeed the direct bound is rho(20m+16r+40)<=40rho(m+r), because20m+24r>=44>40. This requires only finite CE, including constants and subprobabilities; it needs no new influence certificate. Every second-edit terminal below uses this ACTUAL floor based on its ACTUAL old F1 reference.

## 2. Auxiliary scalar entropy estimate for both edits together

As functions on the final cube, F2=g+delta1+delta2. Each delta_i is a signed point cylinder: its squared Fourier coefficients equal 4rho_i U_Di on the corresponding frequency subcube. The sign of delta2 is determined by F1(z*), including the overlapping case. Pointwise,

    P_F2 <= (3/2)P_g,embedded + 6 delta1hat^2 + 6 delta2hat^2
          = (3/2)P_g,embedded + 24rho1 U_D1 +24rho2 U_D2.

Use ONLY to bound scalar entropy the normalized mixture of exact P_g and these two floors. Put beta_i=24rho_i, B=beta1+beta2<=9/64<1/2, since D1>=8,D2>=9. Its cross entropy bounds H(F2), and

    H(F2) <= (3/2)H + sum_i beta_i(2Di+4)
           <= (3/2)H+60rho1 D1+60rho2 D2.          (B)

Here log(1+B)<=2B, log(1/beta_i)=Di-log24<=Di, and Di>=8. This auxiliary exact-source model is NEVER substituted for a prescribed terminal or an actual reference.

## 3. Old complete references and new physical history

At any old frontier let v denote its effective first-path reach: v=2^-ell<=1/2 at a padding prefix ell, and v=2^-b after padding during any source prefix. Let h be the active source restriction, lambda its physical reach; after k source queries lambda=v2^-k. Source stopping-tree entropy and complete divergence contract separately under the mass-preserving source inheritance of A011 v2. In particular

    sum_leaves lambda_j D_j <=D,
    lambda H_h<=vH,  lambda c_h<=vc.

The old first-edited active terminal has ACTUAL CE

    CE1_active<=2c_h+30rho1_local(D1-depth).

Multiplication by its reach turns rho1_local into rho1. At the final source collapse, c_h=-log s and the scalar floor is (s+6p1)/(1+6p1)>=s. Its true r1-control entropy is at most16p1 r1: if e=4p1(1-p1), h2(e)+e r1<=4p1(r1+2)+4p1r1<=16p1r1. Thus the displayed looser 30p1r1 bound also covers this zero-source boundary without applying a positive-dimensional source theorem to dimension zero.

Now evaluate the SAME physical padding/source tree on F2. Exactly ONE current leaf contains z*. At that leaf use (A) based on the OLD F1 model there; all other leaves retain their old models, embedded with zero new-control frequency. At every internal node on the second point's path use its prescribed second floor based on that node's old F1 model; other nodes retain their old models. At the root use (A) based on the old F1 ROOT reference. All second floors have positive-dimensional source because r1 controls remain unqueried. This specifies a genuine coherent list of models at every node; they need not be physical inheritances of one another, and their signed conversions must be paid.

Let L2 be root CE plus ALL reach-weighted signed physical reset increments avg D_child-D_parent for this actual F2 tree and these prescribed models. With full costs, including all normalizers,

    L2=H(F2)+sum_leaves lambda_j D(P_F2,j || Q2,j).   (C)

This is an exact telescope, not a free reset. Intermediate prescribed models cancel only in the signed ledger; neither terminal cost nor reference mass is removed.

If z* lies in the FIRST active leaf, the off-path terminals are unedited source leaves and their total divergence is at most D. Combining its second-floor divergence bound with its old CE gives

    avg D_final <=D+(3/2)lambda CE1_active
                      +40rho2(D2-depth).

Thus (B) gives L2<=3c+105rho1D1+100rho2D2. The crucial cancellation is D1_active+H1_active=CE1_active; discarding that negative entropy term would lose the useful rate.

If z* lies in an OFF-path leaf j, the first active leaf keeps its original floor. Relative to the complete source stopping tree, the extra divergence is at most

    lambda_active(D_h+2H_h+30rho1_local(D1-depth))
       +lambda_j[(1/2)D_j+(3/2)H_j+40rho2_local(D2-depth_j)].

The two source leaves are distinct, so their additional weighted D terms total at most D, not two independently reusable copies of D. The active weighted H_h is at most vH. An off-padding leaf has reach<=1/2 and source g; an off-source leaf has weighted entropy<=2^-b H. Consequently lambda_j H_j<=H/2 in either case. Together with (B),

    L2 <=2D+(3/2+2v+3/4)H+90rho1D1+100rho2D2
       <= (13/4)c+105rho1D1+100rho2D2.             (D)

The extra 15rho1D1 in the last expression merely unifies both cases. This holds at EVERY nonempty old padding/source frontier, not just the final one. At the root (A) and the old root envelope give CE2_root<=3c+45rho1D1+40rho2D2, also bounded by (D).

## 4. One source bank; actual erased edges and the old booking retained

Let d be g's original pivotal degree at its edited point, and d1 the actual pivotal degree of F1 at z*. Set

    E1=2rho1 d, G1=2rho1(D1-d),
    E2=2rho2 d1, G2=2rho2(D2-d1).

Physical edge counting gives I1=Ig+G1-E1 and I2=Ig+G1+G2-E1-E2 EXACTLY. Minimum nonzero cube edge boundary gives Ig>=2a2^-a and also Ig>=2*2^-a*d. For q=b+r1>=7, r2>=1, the decreasing sequences (1+q)/2^q yield

    rho1D1/Ig<=1/32, rho2D2/Ig<=9/512,
    E1/Ig<=1/128, E2/Ig<=1/32, G1/Ig<=1/16.

For E2 use d1<=D1 and (a+q)/(a2^(q+r2))<=8/256. Hence I2>=(123/128)Ig+G1+G2. Equation(D) costs at most(13/4)c+(645/128)Ig. At UNCHANGED K=4C0+15,

    K I2-L2 >=[(19/32)C0+75/8]Ig+K(G1+G2).        (E)

Retain the ENTIRE previously allowed extra booking

    0<=U<=U_star=min{(C0+1)Ig,K G1}.

Because U_star<=K Ig/16=(C0/4+15/16)Ig, the conservative residual at the root and EVERY old padding/source frontier is

    K I2-L2-U >=[(11/32)C0+135/16]Ig+K(G1+G2)>0. (F)

The same original source account is S=KIg-c. Algebraically the operation ledger is S+K(I2-Ig)-(L2-c)-U=KI2-L2-U: c is initially charged once, with all subsequent costs paid by the unused remainder and actual physical influence increments. Equivalently, if the full first-history bill L1 is already booked, retain it and charge Delta=L2-L1; then B2=(KI1-L1-U)+K(I2-I1)-Delta. Delta changes both target law and reference and is NOT falsely called a KL-only reset. This equality retains the first bill rather than refunding or erasing it. The theorem prices representation construction stages of different target functions; it is not permission to change the Boolean function during an ordinary restriction history. No descendant source certificate and no C0 renewal is used.

Independent terminal factors retain their full additive CE/KL and multiplied masses; their own rate accounts are separate and are not borrowed by (F). Integer rounding remains separate.

## 5. First unsupported continuation

Two actual nested representation edits, including arbitrary second locations and every old active frontier, now fit the original rate and old U_star when b>=6. This is a restricted repair of the per-edit inflation mechanism; it does not construct arbitrary f at that fixed rate. A third edit increases the number of exceptional leaves and can accumulate the source-entropy coefficients in (D). Arbitrarily many edit operations, arbitrary physical queries of the second controller, and an influence-paid universal initial reference remain unproved. Six padding bits are sufficient, not claimed necessary. Full FEI remains OPEN pending an all-dimensional universal argument and independent reconstruction.
