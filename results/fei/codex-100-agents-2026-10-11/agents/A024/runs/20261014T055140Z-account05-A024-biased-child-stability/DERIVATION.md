# General controller lift: exact prefix accounts

All coordinates are physical independent uniform bits. Let w(z),h(u) be disjoint Boolean signs, W=(1-w)/2, t=E W and r=Pr[h=-1]=(1-E h)/2. Define F=1-W(1-h). At a controller node w_v with queried coordinate x, put d_v=Inf_x(w_v), a=E w_v and beta=(E w_v0-E w_v1)/2. Define L(a,b)=e(a^2)+e(b^2)-e(a^2+b^2), e(p)=p log2(1/p).

Writing F=(1+h)/2+[(1-h)/2]w, direct edge and mixed-face counting gives

    Inf_x(F_v)=r d_v,
    q_x(F_v)=r q_x(w_v)+(I(h)/2)d_v.                 (1)

The h block remains untouched and uniform. The queried controller's child means change the outer-gate law, not the physical measure. Its exact erasure is

    B_x(F_v)=r B_x(w_v)+R_r(a,beta),
    R_r(a,beta)=L(1-r+r a,r beta)
                   +r(1-r)L(1-a,beta)-r L(a,beta).   (2)

To prove (2), the h-empty Fourier fiber of A=(1+h)/2,B=(1-h)/2 is (Ahat,Bhat)=(1-r,r). Every nonempty h fiber has (Ahat,Bhat)=(hhat/2,-hhat/2), whose squared norm sums to Var(h)/4=r(1-r). Substitute these into the previous exact empty-fiber reconstruction. Retain the negative r L(a,beta). No normalization by t,r or a variance is needed, so r=0,1 and deterministic controller endpoints are included.

Let T_w be any complete controller restriction tree, with physical weights p_v, and let E be the nodes of that tree which are K4-bad AFTER lifting, i.e. r B_x(w_v)+R_r(a,beta)>4r d_v. Define

    Q_w(E)=sum_{v in E}p_v q_x(w_v),
    P_w(E)=sum_{v in E}p_v d_v.

Then the exact bad odd-face bill of the controller prefix is

    Q_bad,prefix(F)=r Q_w(E)+(I(h)/2)P_w(E).          (3)

It is important that E is the lifted bad set, not automatically the controller's own bad set. For the full prefix (all nodes), the face and influence telescopes give

    Q_prefix(F)=r Q(w)+(I(h)/2)I(w),
    I_spent,prefix(F)=r I(w),
    E H(terminal)=t H(h), E I(terminal)=t I(h),
    E Q(terminal)=t Q(h).                            (4)

Terminal branches are exactly h when w=-1 and the constant +1 otherwise. Their weights are t and 1-t, with no fitted or reset rarity. A continuation tree on h contributes t times its own bad bill. Thus pricing (3) cannot discard or spend t H(h) a second time.

## Repair of the overly strong inherited-tree step

The previous parity controller has zero lifted bad pivot mass P_w(E). That is why its mixed faces were free at good nodes. A controller tree satisfying its own Q_bad<=K'I(w) does NOT by itself give a bound for (3): the new multiplicative I(h)P_w(E)/2 account is missing. This is the precise candidate failure to check below, rather than a proposed universal theorem.

Use the same five-bit module c(s,x) as the previous stage, b(x)=(-1)^(x0*x1+x2*x3), c(0,x)=b(x), c(1,x)=b(x) except x=0 is flipped. Write d=1/16, m=3/16 and J=I(c)=37/16. The exact certificate B_s(c)-L(m,d)>1/4 is 2^182*13^156>5^210*3^162. It implies that the queried selector stays K4-bad in EVERY nonignored disjoint outer composition. This clause is reconstructed from nonnegativity of the outer L fibers, not assumed accepted.

Let G_L be the product of L independent modules. Set w=-G_L and h=G_M. Then

    F_LM=1-(1+G_L)(1-G_M)/2,
    t=(1+m^L)/2, r=(1-m^M)/2,
    I(F_LM)=t J M+r J L.                            (5)

Give w its complete selectors-first tree (all module selectors, then their data). Tensor erasure and influence agree with the queried module. Every selector is bad with q=1/4,d=1/16. All subsequent data nodes are good: b or its point flip has first data influence 1/2 or 5/8; every later relevant function on at most three bits has influence at least 1/4. Consequently this tree on w has exactly Q_bad=L/4=(4/37)I(w) and own bad pivot mass L/16.

In the lifted controller prefix all these L selector levels remain bad, regardless of the previous selector answers. Each contributes r/4+JM/32 by (1). Hence

    Q_bad,prefix(F_LM)>=r L/4+JLM/32.                (6)

For M=L, equation (5) reduces to I(F_LL)=JL, so (6) gives

    Q_bad,prefix(F_LL)/I(F_LL)>=4r/37+L/32.           (7)

The inherited controller tree and the core's selectors-first tree individually have bad credit/I exactly 4/37, yet lifting this already-paid controller tree has unbounded prefix credit/I. Terminal entropy t H(G_L) is still present. The support bound H(F_LL)<=10L gives H/I<=160/37; this is NOT an FEI counterexample and does not refute the some-tree bridge.

The logarithmic outer term is also visible in (2). At these selector nodes a=-A tends to zero and beta=a/3. The first L term has leading coefficient r^2 beta^2 log(1/beta^2); the second has r(1-r) beta^2 log(1/beta^2). The subtracted L(a,beta) is homogeneous with BOTH arguments shrinking proportionally, so it is only O(beta^2). Consequently R=r beta^2 log2(1/A^2)+O(beta^2), uniformly for 13/32<=r<=1/2. A fixed nonzero a and a proportional vanishing a are different regimes.

The signed bank is tiny even in this controller obstruction. At every selector level |a|<=3/16, beta^2<=16^(-(L+1)) and 13/32<=r<=1/2. By homogeneity, the first positive term in (2) is r^2 L((1-r)/r+a,beta); its first argument has magnitude at least |a|. The second has first argument 1-a with magnitude at least |a|. Their combined coefficient is r^2+r(1-r)=r, so R>=0 after the exact subtraction. Both first squared arguments plus beta^2 are <5, and L(x,b)<=b^2 log2(e(x^2+b^2)/b^2). Thus R<=r beta^2 log2(5e/beta^2)<=(2L+4)16^(-(L+1)). The total expected selector bank is at most L times that expression. These mean logs occur at bad nodes, while the divergent bill in (7) is the mixed-face term.

First unsupported universal line: select or alter the controller/core tree so that BOTH r Q_w(E) and I(h)P_w(E)/2 are bounded by unused source influence while preserving all actual terminal bills. An inherited bound on the controller's own bad q alone cannot establish this line.

## Exact K7 repair for this fixed-module family

There is no obstruction to the lead's existence of some absolute K on this family. In ANY controller-first physical tree, every live controller factor is a restriction of c to at most five remaining bits. Its nonzero coordinate influence is at least 1/16 by the uniform edge-count granularity. Tensor multiplication does not change that queried influence. Since the untouched core has r>=13/32, every relevant lifted controller query has d_F>=13/512. After the controller is determined, every relevant core query has influence at least 1/16, or it lies in a constant branch.

The scalar ratio h2(d)/d is decreasing on (0,1], since its derivative is log2(1-d)/d^2. The exact integer inequality

    13^13 * 499^499 > 2^4517

certifies h2(13/512)<7*(13/512). Therefore B_i<=h2(d_i)<7d_i at every relevant node of any such complete controller-first tree. Its K7 bad bill is zero, all terminal entropy is eventually retained then resolved, and no mixed-face charge is needed at this threshold. This closes all L,M>=1 for K7. It does not give a uniform granularity threshold for controllers with unbounded local module dimension, so it supplies no universal FEI proof. The K4 data-first prefix bill is exactly zero in the three frozen finite pairs, but no all-L,M K4 data-first assertion is inferred from those checks.
