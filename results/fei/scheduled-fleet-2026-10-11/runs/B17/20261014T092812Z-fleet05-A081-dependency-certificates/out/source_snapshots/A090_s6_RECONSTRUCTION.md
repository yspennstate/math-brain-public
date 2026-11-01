# Independent reconstruction from A001 theorem statement

Read the source statement, not its derivation, before reconstructing this file. Units: bits; all influences physical. Let d>=2 even, delta=2^-d, t=sqrt(delta), alpha=2^-r, w=4^(1-r), e=delta/2, a=1/2+delta(1-alpha), J=r delta. The quadratic bent core has signed flat coefficients sigma t with N_sigma=(2^d+sigma 2^(d/2))/2 occurrences. Q_r has coefficients of magnitude alpha, with empty coefficient alpha. Point attachment F=b+1_0(Q_r-1) therefore has amplitudes sigma t+delta(alpha-1) at empty selector mask and signed delta alpha elsewhere. Every amplitude is nonzero: even the smallest empty-mask amplitude is t-delta(1-alpha)>0. Nonempty mask amplitudes have alpha>0. Actual selector flip probability is delta/2; a core-direction edge at 0 was nonpivotal and is toggled when Q_r=-1, giving a=1/2+delta(1-alpha).

Fix one selector query; retain its pair partner occupancy and whether every other pair's residual mask is empty. Since all selector Fourier coefficients have equal squared magnitude, derivative cell masses are (w/2,(1-w)/2,w/2,(1-w)/2). Sum the complete reference without support conditioning. Its cell masses are (A,e(1-w),ew,e(1-w)), A=1-delta+2delta alpha^2. All sum to one, since ew=2delta alpha^2. Each nonexceptional cell's core conditional derivative/reference laws coincide. In the first cell, derivative core is uniform, reference core has mass delta R_sigma/A, with R_sigma=1+2sigma t(alpha-1)+delta[(alpha-1)^2+alpha^2]. Thus chain rule gives per-row loss L_C=e w D_y/2, D_y=sum_sigma N_sigma delta log(A/R_sigma). Direct KL of the four cell probabilities gives

    M_C/e=log(1/e)-D_C=1+(w/2)[d+2r-1+log A].

Full M=M_C-L_C. The source ledger charges M_C+L_C, conservatively exceeding full M by 2L_C; its dominance assertion is valid, not an equality. This sign is an audit guard.

For 0<t<=1/2 and 0<alpha<=1/2,

    3R_+-A=2(1-t)(1-2t)+6t(1-t)alpha+4t^2 alpha^2>=0,
    R_->=R_+.

Therefore 0<=D_y<=log(3)<2. The combined selector extra above J is

    E=sum_selectors(M_C+L_C)-J
      =(r delta w/2)[d+2r-1+log A+D_y]
      <(r delta w/2)(d+2r+1).

Since d delta<=1/2 and delta<=1/4, E<rw(2r+3)/8<=5/8<3a/2. The inequality r(2r+3)/4^(r-1)<=5 follows by its strictly decreasing successive ratio (r+1)(2r+5)/[4r(2r+3)]<1, r>=1. This establishes the stated single-root-owner bound, without summing a separate core allowance for each row.

For every complete spectral row, B_i<=M_i+e_i/ln2 by (1-x)log(1/(1-x))<=x/ln2 in each residual pair; zero masses by continuity. Each core row has B_i<=1, so B_core<=d<=2I_core. Therefore B(F)<=2I_core+sum_selectors(M_C+L_C)+J/ln2. The latter is <2I_core+(1+1/ln2)J+3a/2. As I_core=d a and d>=2, its core coefficient is <=11/4<7/2; and 1+1/ln2<3<7/2 (ln2>1/2 by integration). This proves the source's (7/2)I root bill.

Deleting all information except the pair partner gives binary laws (1/2,1/2),(1-e,e). The exact per-row lost KL is

    L_binary=e/2[(1-w)log((1-e)/e)+w log(w(1-e)/A)+w D_y].

For r>=2: w<=1/4, log((1-e)/e)>=d, log(1-e)>=-1, log A<=0, D_y>=0, and w(2r-1)<=3/4 (successive ratio is <1). Summing 2r rows yields >=r delta(3d/8-3/8)>=r delta(3d/8-1/2). At r=2^d, r delta=1, so total binary loss grows at least linearly in d while one specified core coordinate influence a<=3/4 stays bounded. Hence one fixed multiple of that coordinate cannot pay the repeated binary loss.

Finally, root entropy is independently bounded without the source's derivation. Let W be nonempty-selector spectral mass; W=delta(1-alpha^2). Condition on selector emptiness. Each conditional core law has entropy <=d; the nonempty selector masks have entropy <=log(4^r-1)<2r. Hence H(F)<=d+h(W)+2rW<=d+1+2r delta<=2d+4r delta<=4I(F). This is an actual family proof, not evidence or a full FEI theorem.

## First unreconstructed universal implication

All clauses of A001-SHARED-CORE-FOUR-CELL-OWNERSHIP@1 reconstruct at its original root-fixture scope. The first unsupported implication beyond it is that the same root allowance survives an actual mixed core-data restriction as genuinely UNUSED child entropy surplus, with the incoming complete reference, both terminal spectra and every old debit retained. The root bound establishes no such hereditary reserve. Full C018 still requires sum_i e_i D(mu_i||r_i)>=sum_i e_i log(1/e_i)-K I for arbitrary Boolean functions; C024 needs a reference/history transfer with a single conserved budget. Neither follows from this scoped ledger.
