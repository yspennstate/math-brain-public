# Adaptive collision payment for hereditary shared spectral norm

Let G(S,X), H(S,Y) be Boolean signs with disjoint private blocks X,Y, arbitrary finite common physical block S, and fresh fair selector z. Set F=(G+H)/2+z(G-H)/2. Entropy is in bits. Fix L>=1 and assume every fully private-fixed shared slice of each core has Fourier l1 norm at most L. This is a sufficient structural hypothesis; it is not implied by Booleanity with a universal L.

## 1. Hereditary admission and concrete nonlinear classes

This slice hypothesis is equivalent to the following hereditary condition: at every physical data restriction the conditional private mean of each core, as a function of remaining S, has Fourier l1 norm at most L. Necessity follows by fully fixing private inputs. Sufficiency follows because restrictions merge Fourier coefficients by signed addition (so cannot increase l1 norm), and conditional private means are convex averages of restricted slices.

For |S|<=2 every Boolean slice has l1<=sqrt(2^|S|)<=2 by Parseval. Thus ALL such two-shared-bit compositions satisfy admission at L=2, including arbitrary nonlinear slices and private indexing. The private dimensions and adaptive data-query order are unrestricted.

A second class has arbitrary shared width: each fixed private assignment chooses an arbitrary sign and an arbitrary shared subcube C, giving a slice epsilon(1-2*1_C). The subcube may be empty, the whole cube, or have any location and codimension r. For r>=1 its p=2^-r Fourier spectrum has constant 1-2p and 2^r-1 nonconstant coefficients of magnitude 2p. Therefore its l1 norm is 3-4p<=3. Constant/empty cases have norm one. These privately indexed subcube-switch branches, for BOTH cores, satisfy hereditary L=3 even with arbitrarily rare influences. No derivative-gap policy is required.

## 2. Exact coherent ledger

Write phi(p)=p log2(1/p), Phi(p,q)=phi(p)+phi(q)-phi(p+q). At a reached restriction let C run through all subsets of remaining S; g_C,h_C are the common-frequency coefficients with no private input. Fourier expansion gives two amplitudes (g_C+h_C)/2,(g_C-h_C)/2 at selector frequencies 0,1. All other core coefficients are copied twice at half amplitude. Hence

    H(F)=(H(G)+H(H))/2+R,
    R=2-sum_C(g_C^2+h_C^2)
      +sum_C[phi((g_C+h_C)^2/4)+phi((g_C-h_C)^2/4)
                          -(phi(g_C^2)+phi(h_C^2))/2].

This is a coherent collision identity, not a reuse of disjoint-block composition. Querying the actual selector shows R=Delta_z H>=0. The shared physical influences obey Inf_i(F)=(Inf_i(G)+Inf_i(H))/2 by conditioning on z.

## 3. Signed physical-query prices

Define D_i=B_i(F)-(B_i(G)+B_i(H))/2, with B_i the paired-amplitude erasure. At a private X query only common rows collide. With u_C=g_C,d_C=ghat(C union {i}),v_C=h_C, the correction is the sum of

    S(u,d;v)=[Phi((u+v)^2,d^2)+Phi((u-v)^2,d^2)]/4
                          -Phi(u^2,d^2)/2.

The scalar comparison -Phi(u^2,d^2)/2<=S<=Phi(v^2,d^2)/2 and envelope Phi(a^2,b^2)<=2|ab| give

    |D_i|<=L Inf_i(G)=2L Inf_i(F).

Every derivative coefficient |d_C| is bounded by physical Inf_i(G), since the half-difference is valued in {-1,0,1}. Private Y exchanges the cores. Both positive and negative credits are retained.

At a shared query i, C ranges over subsets of S minus {i}. Let mu_C=g_C,a_C=ghat(C union {i}),nu_C=h_C,b_C=hhat(C union {i}). Exactly D_i=P-N, with

    P=sum_C[Phi((mu_C+nu_C)^2,(a_C+b_C)^2)
                         +Phi((mu_C-nu_C)^2,(a_C-b_C)^2)]/4,
    N=sum_C[Phi(mu_C^2,a_C^2)+Phi(nu_C^2,b_C^2)]/2.

The envelope bounds a P row by (|mu_C|+|nu_C|)(|a_C|+|b_C|). Summing and using the two admitted mean norms gives P<=2L(Inf_i(G)+Inf_i(H)). Similarly N<=L(Inf_i(G)+Inf_i(H)). As both are nonnegative,

    |D_i|<=4L Inf_i(F).

Also universally |D_i|<=1 because B_i(F) and the inherited half-sum are both in [0,1]. Thus the sharper shared bound is min{1,4L Inf_i(F)}. This does not supply a price at a rare query if L is unbounded.

## 4. One conserved stopping reserve

For any physical split Delta_i H=B_i+JS_i, 0<=JS_i<=(2/ln2)Inf_i. Subtracting both inherited decrements gives

    Delta_i R=D_i+JS_i(F)-(JS_i(G)+JS_i(H))/2.

The two nonnegative JS quantities on the right each lie in [0,(2/ln2)Inf_i(F)], so their signed difference has that radius, not twice that radius. Put K_L=4L+2/ln2. For every finite adaptive data-only prefix, with actual probabilities w_v and arbitrary stopping leaves,

    |R_root-E R_leaf| <= K_L Pi_data,
    sum_v w_v |D_v| <= 4L Pi_data,
    Pi_data=I(F_root)-E I(F_leaf).

The last identity is the actual physical influence telescope: influences of an unqueried z also average under a data restriction, and both cores are put on the same data tree with dummy coordinates. No nominal per-core shared allowances are added. Completing only the data makes both cores constant and the wrapper a constant or character, with R_leaf=0. Consequently

    0<=R<=K_L I_data(F),   I_data(F)=(I(G)+I(H))/2,
    H(F)<=(H(G)+H(H))/2+K_L I_data(F).

For any partial prefix, Pi_data+E I_data(F_leaf)=I_data(F_root). An optional terminal selector query spends exactly R_leaf from the remaining K_L I_data(F_leaf), leaving the exact inherited terminal half-sum of core entropies. Thus prefix and suffix have one reserve, not two. This is a transport theorem, not a universal terminal-core entropy certificate.

In particular nonlinear overlap two has K_2=8+2/ln2<11; arbitrary-width privately indexed subcube switches have K_3=12+2/ln2<15. These constants are not claimed sharp. A012 already supplies a better ROOT selector-reference tax for overlap two. The additional conclusion here is arbitrary adaptive DATA-prefix signed transport, including rare/rare queries and the same stopped terminal reserve. A097 already treats root reference transfer under l1 admission; that closure is not newly claimed.

## 5. Scalar proofs and exact boundary

In natural units Phi(u^2,d^2)=integral_0^(d^2)ln(1+u^2/t)dt. The symmetric shifted ratio satisfies
((u+v)^2+t)((u-v)^2+t)/(u^2+t)^2 <=(1+v^2/t)^2;
expansion uses (t-u^2)/(u^2+t)^2<=1/t and (u^2+t)^(-2)<=t^(-2). Integrating proves the upper S comparison; nonnegative shifted Phi terms prove the lower. The envelope follows by homogeneity from Phi_nat(1,t^2)/(2t)<=ln2 for t in (0,1]. Its derivative numerator is (t^2-1)ln(1+t^2)-t^2 ln(t^2)>=0, using ln(1+t^2)<=t^2 and -ln(t^2)>=1-t^2. Continuous zero endpoints are included.

For the JS bound use [(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2). The derivative comparison follows from (1-t^2)^(-3/2)>=(1-t^2)^(-1); summing paired amplitudes gives JS<=2sum min(u_T^2,v_T^2)/ln2<=2 Inf_i/ln2.

No dimension-independent L follows for arbitrary Boolean slices: quadratic bent slices on k even shared bits have norm 2^(k/2). A078's actual rare private query has D/Inf>=k-4, so an unrestricted all-query extension with an absolute price is FALSE, not just unproved. Our L-dependent theorem does not contradict that obstruction. A076's source-owned derivative-gap policy is a complementary valid mechanism, independently reviewed here. The live universal first unsupported line is a selected physical-query rule or a signed terminal-slack payment when both hereditary spectral norm and derivative gaps fail, retaining both actual core debts. Iterating K_L as a new whole-core allowance at every hierarchy level is not authorized.
