# Private point query before an unresolved shared activation

All entropies are bits. phi(t)=t log2(1/t), phi(0)=0, and Phi(a,b)=phi(a)+phi(b)-phi(a+b). The scalar physical-packet bound Phi(a^2,b^2)<=2|ab| includes zero amplitudes. The full physical child concavity gap is J_i<=2 Inf_i/ln2.

## 1. Actual decomposition and its scope
Let Y be a fresh fair physical bit in {0,1}. Let A be a private point indicator of current probability q=2^-r, r>=1. On disjoint independent blocks let u be a Boolean selected core and G a Boolean fallback, with G itself optionally a fine selector of independent disjoint cores. Let C_j be exclusive indicators on a controller block disjoint from u,G and all selected cores v_j. Put E=1-sum C_j, e=EE, and

    H=sum C_j v_j+E G,
    F=(1-Y)G+Y[A u+(1-A)H].                    (1)

Every v_j occupies a separate physical block disjoint from u and G. There is ONE G, shared on inactive Y and active failed-prefix histories. C_j may have arbitrary internal overlap; priority point lists are an application. All actual preceding restrictions preserving these blocks and leaving Y fresh are allowed, including nonconstant core-data exposures. No shared-data replacement is allowed. Write m=Eu, n=EH, nG=EG, L=1-mn, Vu=Var(u), VH=Var(H). A private A-coordinate has actual influence

    d=q L/2.                                   (2)

For a core-only nonempty G frequency S, Hhat(S)=e Ghat(S). At every other nonempty frequency Ghat(S)=0. Consequently

    sum_{S nonempty}|Hhat(S)Ghat(S)|=e Var(G)
       <=Var(H),                               (3)

by total variance conditioning on the exclusive controller: VH=sum P(C_j)Var(v_j)+e Var(G)+Var(conditional mean). This is the correlation fact that a generic arbitrary correlated H,G would not provide.

## 2. Exact private erasure with Y retained
Embed u,H,G on their union of physical blocks. At every Fourier frequency S set U_S=uhat(S), H_S=Hhat(S), G_S=Ghat(S),

    M_S=(1-q)H_S+q U_S, w_S=q(U_S-H_S).

Pairing the queried A bit at the empty remaining-A mask gives the two Y rows with amplitudes (G_S+M_S)/2,w_S/2 and (M_S-G_S)/2,w_S/2. Nonempty remaining-A masks have equal paired squares. Since u and H are independent, E(u-H)^2=2L. The exact physical erasure is therefore

    B_A=(q-2q^2)L+S,
    S=sum_S [Phi((G_S+M_S)^2/4,w_S^2/4)
             +Phi((M_S-G_S)^2/4,w_S^2/4)].       (4)

This reconstructs A091 NEXT_IDENTITY equation(1), generalized only from one later B event to the exclusive mixture in (1). Y is still physically unexposed. Every coincident empty row remains coherent.

## 3. Uniform packet payment
The two Phi inequalities together give, for each row,

    packet sum <=|w_S| max(|G_S|,|M_S|),          (5)

because |a+b|+|a-b|=2 max(|a|,|b|). Separate three ACTUAL frequency sectors.

On nonempty u-only frequencies, G_S=H_S=0, and the packet is exactly q^2 U_S^2. Their total is q^2 Vu. Frequencies involving u and any other block vanish. On every other nonempty frequency U_S=0. Using max(a,b)<=a+b and (3), their total is at most

    q sum_nonempty |H_S|[|G_S|+(1-q)|H_S|]
       <=q(2-q)VH.                              (6)

At the completely empty row |G_0|=|nG|<=1 and |M_0|=|EF given Y=1|<=1. Its cost is at most q|m-n|<=qL. For all m,n in [-1,1], Vu<=2L, VH<=2L and |m-n|<=L; the last identity follows by squaring: L^2-(m-n)^2=(1-m^2)(1-n^2)>=0. Combining all rows,

    B_A <=(q-2q^2)L+q^2 Vu+q(2-q)VH+qL
         <=(6-2q)qL=(12-4q)d <=12d.             (7)

This is already a price for the FULL actual erasure, without requiring a reserve debit. It is not claimed sharp. In particular rare q does not create a logarithmic loss from the SAME fallback: its absolute Fourier cross mass is e Var(G), not an uncontrolled square-root estimate. For d=0, independence forces u=H equal constant almost surely, and F=G+Y[H-G+A(u-H)]=G+Y(H-G), independent of A; equation(4) gives B_A=0. Thus all zero-influence endpoints are included.

## 4. Original merged reserve, signed data and stopping
If G has original fine labels a_l and variances V_l, write ZG=sum a_l V_l. Let c_j=P(C_j). Prefix labels v_j have mass (1-q)c_j/2; G's physical label l has MERGED mass a_l s, s=[1+(1-q)e]/2. The original nonresetting R=sum phi(P_label)Var(core_label) has exact A-query release

    kappa=q Vu/2+[k(q)/2]sum c_j Var(v_j)+kG(q,e)ZG,
    k(q)=phi(1-q)-phi(1-2q)/2,
    kG=phi(s)-[phi((1+e)/2)+phi((1+(1-2q)e)/2)]/2.
                                                       (8)

All three terms are nonnegative, by concavity of phi and physical fair reach probabilities. Logarithms of c_j and a_l cancel in each fine release; no separate copies of G receive budgets. Therefore

    D_A H(F)-kappa <=(12-4q+2/ln2)d
                         <=(12+2/ln2)d.          (9)

Fine U=sum P_label[H(core)-phi(mean^2)] is harmonic at this controller query. At every data query the existing signed identity is D H<=drop(U+R)+(3/ln2)P_label beta^2, retaining the exact singleton beta^2 log2(1/beta^2) through cancellation with the signed empty-core sector, not replacing it by O(beta^2).

For private point-priority C_j and a disjoint private point-priority fallback G with constant final default, this pays every query of the EARLIEST still-undecided prefix test before Y. Earlier failed tests can be discarded; after an earlier successful test, the active child is that independent core. A091-SHARED-ACTIVATION-REPEATED-FALLBACK-PAYMENT@1 pays revealing Y after any such history at8+2/ln2. After Y the accepted A059 v2 pays private controllers in arbitrary order. Data may be interrupted arbitrarily throughout. For policies respecting prefix priority BEFORE Y and postponing fallback-internal controller queries until Y is resolved, all controller nodes have rate

    K=max{12+2/ln2, 8+2/ln2, 6+(5+ln10)/ln2}
      =6+(5+ln10)/ln2 <17.                       (10)

Indeed exp(1)<3: the factorial series through degree2 is5/2 and its remaining tail is at most(1/6)/(1-1/4)=2/9. Hence exp(2)<9<10, so ln10>2. Also exp(3/4)>1+3/4+(3/4)^2/2>2, so ln2<3/4. These imply 3+ln10>6ln2. The upper bound K<17 is the accepted A059 rational exponential certificate, source PROOF Section3. The same original fine U/R telescope on every finite such physical stopping tree yields

    H_root<=U_root+R_root+(3/ln2)T_data+K Pi_ctrl
                +E[H_leaf-U_leaf-R_leaf].       (11)

At controller-resolved leaves the profile is phi(mean_selected^2)<=Var(selected)/ln2<=I_leaf/ln2. At unresolved stops its actual profile remains literal. Root funding R_root<=2I_ctrl(root) is separately paid ONCE, never absorbed into the maximum in (10). Equations(9)-(11) are a scoped extension, not an arbitrary-order theorem before Y.

## 5. First unpaid line
If an A query is BEHIND an earlier unfinished prefix test, H and G also share prefix guard-frequency rows. Equation(3)'s present complete-row payment no longer suffices for that query: those earlier mean-profile rows need an actual guarded packet price with the same merged G reserve. Also unpaid are internal G-controller queries before Y when the prefix remains unresolved, generic nonpoint current queries, and shared selected-core data. Inherited U_root and unresolved terminal profiles remain unpaid universally. Full FEI is OPEN. The shortest next step is the later private B query before both Y and A, after an actual non-flat data restriction, retaining both G+M and M-G rows and the original merged release.
