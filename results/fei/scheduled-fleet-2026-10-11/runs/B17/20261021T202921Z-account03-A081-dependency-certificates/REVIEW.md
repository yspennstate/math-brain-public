# Independent reconstruction of the A095 wide-block history theorem

Verdict: HOLDS at the entire original stated scope; the independent exact replay passes. This review supplies no repair. All information uses base-two logarithms; all physical cubes are uniform. It accepts no fresh descendant reset and no arbitrary incoming reference theorem.

## 1. Source and exact reference

The target is A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY@1, with the source statement and hypotheses preserved verbatim in CLAIMS.json. Its proof is A095's 20261021T180853Z DERIVATION sections 1–4. Source bytes, rather than mutable board summaries, are pinned in out/SOURCE_PINS.json. A094's AUDIT sections 3–5 supplies the transport and physical-debit background, reconstructed below.

Let w>=4,m>=0,k=w+2,n=k+m,delta=2^-n. The source is g=h_w h_2, where h_j is negative only at the zero vertex. Its zero value is +1. A fresh fair selector chooses padded g or its zero-vertex flip. If a_T is an original source coefficient, the old root coefficient is a_T-delta. Every complementary root coefficient has magnitude delta. All 2^k original coefficients are nonzero. Put W=2delta-2^k delta^2. The prescribed normalized reference is (1-W)a_T^2 on the original support and delta^2 on each complementary atom. Their total mass is exactly one. Here 0<W<1 and no old coefficient vanishes: min|a_T|=2^-w>=4delta. These facts justify every division and logarithm used below, including m=0,w=4.

## 2. Independent signed-profile calculation

Write q=2^(1-w),b=1-q. The wide-factor coefficients are b and 2^w-1 copies of -q; the narrow-factor coefficients are 1/2 and three copies of -1/2. Multiplying and summing the four coefficient classes gives, with ell_T=-log2(a_T^2),

    c = 2-b^2 log2(b^2)+(2q-q^2)(2w-2),
    A = sum a_T ell_T = 2+2b log2 b+(2-q)(2w-2),
    B = sum ell_T = -8log2 b+2^(w+3)w-8w+8.

Consequently the complete root price is

    CE = c-2delta A+delta^2 B-(1-W)log2(1-W)+2nW.

This follows by expanding each old squared coefficient against its actual prescribed reference. The last term includes every complementary atom. In particular it is not an entropy calculation with the old reference silently replaced.

Use ln2>2/3, -ln(1-x)<=x/(1-x), and -(1-x)ln(1-x)<=x. The first follows from the positive atanh series; the other two follow by integrating 1/(1-x) and multiplying the resulting inequality. Since q<=1/8,

    c < 2+(4w-1)q-(2w-2)q^2 <=121/32.

For w=4 the last expression equals 121/32. For w>=5, dropping its negative term and using that (4w-1)2^(1-w) decreases gives the stronger 51/16. Similarly A>=4w-2-(2w+1)q. Since -log2 b<(3/2)q/b<=3/14<w-1, B/2^k<=2w. Also W<=2delta and delta<=2^-k. Substitution gives

    CE < c+delta[4m-2w+15+(4w+2)q]
       <=c+delta(4m+37/4).

The factor (4w+2)q is at most 9/4: its ratio at successive widths is (4w+6)/(8w+4)<=1. Finally 16m+37<=37*2^m for every m>=0. At zero it is equality; at the next integer its left side increases by 16 while the previous left side is already at least 37. This is a finite induction, with no limit exchange. Therefore CE<121/32+37/256=1005/256 for all the stated parameters. The finite log checks validate actual cases; this induction supplies the unbounded parameter step.

## 3. Adaptive physical influence, without independent branch events

Let Pi_g be the original queried influence, averaged with original physical reaches. There is exactly one history path containing the edited vertex. If it queries t wide coordinates, every queried point edge was originally pivotal and every remaining original core point edge is pivotal. A point-edge correction at depth d has point probability 2^d delta and physical reach 2^-d, so their product is the SAME delta. Direct edge counting gives

    E I_leaf = 1+wq-Pi_g+delta(m-w-1+t).

At the edited-path leaf the w-t surviving wide coordinates each have conditional influence 2^t q. Multiplication by its reach 2^-t gives (w-t)q. Every other leaf contributes nonnegative influence, hence wq-Pi_g>=(w-t)q. Thus

    E I_leaf >=1+delta[m-1+(w-t)(q/delta-1)]
             >=1-delta>=63/64,

because q/delta=2^(m+3)>1 and n>=6. This uses the actual unique edited path, not a product of marginal probability bounds. The width-two factor remains unqueried and nonconstant, including t=w. Both siblings and all endpoints remain in the mean account. Querying that factor is outside the theorem and destroys this lower-bound argument.

## 4. Complete inherited reference and zero fibers

For actual child laws P_0,P_1 put p=(P_0+P_1)/2 and let r be the incoming Q marginalized over queried spectral membership. On p>0 use pi_b=P_b/(2p). On p=0 retain r with pi_0=pi_1=1/2. Raw child references are 2r pi_b. Their normalizers are positive and sum to two. Positive actual child atoms have reference likelihood P_b/Q_b=(p/r)Z_b. KL disintegration therefore gives

    D_parent-mean D_child=L-mean log2 Z_b,

where L is the nonnegative conditional membership divergence. Concavity of log and Z_0+Z_1=2 show mean log2 Z_b<=0. The physical entropy identity adds Delta=B_query+JS_query>=0, giving CE_parent>=mean CE_child. All sets are finite. Induction over the actual finite adaptive tree retains the original reaches and gives E CE_leaf<=CE_root. Combining sections 2 and 3 proves the strict mean surplus >3/256 at the unchanged rate four. It asserts no individual-child solvency.

An independent untouched terminal with a prescribed product reference factors throughout this transport, provided the zero-fiber kernel also factors through the core. Its whole CE and KL remain additive outside this bank. Arbitrary zero-fiber kernels need not preserve that product statement; the hypothesis is retained explicitly.

## 5. Dependency and universal boundary

The signed profile, edge identity and finite posterior transport are reconstructed from definitions here. They do not depend on FEI or on a recursive rate-inflation lemma. The prior A094 acceptance of A095's scoped transport is review evidence, not a proof edge from A094's new profile back into A095's profile. Keeping those roles separate prevents a spurious proof cycle.

The first unsupported universal line is payment of an arbitrary inherited positive signed profile, or a specified descendant reference reset, together with the complementary complete terminal and executed old debit, from one genuinely unused original bank at an absolute rate. This theorem pays no such reset. An arbitrary supplied reference can put arbitrarily small mass on a positive true atom and make its CE unbounded at fixed physical influence; it cannot be substituted into the theorem. Full FEI remains OPEN.
