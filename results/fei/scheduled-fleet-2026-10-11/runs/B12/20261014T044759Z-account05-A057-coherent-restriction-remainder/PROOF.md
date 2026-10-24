# Later point test before an undecided earlier test (bits)

## 1. Exact later-test erasure and its fine release
After the shared physical bit is resolved, consider

    F=A u+(1-A)[B v+(1-B)],

where A,B are point indicators on disjoint private control blocks and u,v are arbitrary Boolean cores on disjoint data cubes, also disjoint from the controls. At any actual data/control cylinder where both tests are unfinished put p=EA=2^-r, q=EB=2^-s, r,s>=1, m=Eu, n=Ev, a=1-m, b=1-n. The same physical u persists in both children of any B query. Put U=sum_j P_j E_ne(u_j), R=sum_j phi(P_j)Var(u_j), with fine selector probabilities P_u=p, P_v=(1-p)q and phi(t)=t log2(1/t).

For a queried private B coordinate, its influence is

    d=(1-p)q b,

and its fine reserve release is exactly kappa=(1-p)q Var(v). The u selector probability does not change; the v probability doubles on one branch and vanishes on the other. No independent-copy substitution of u occurs.

Separating empty/nonempty core Fourier frequencies, every nonempty u row has no B-query partner and gives zero erasure. The nonempty v rows give exactly kappa. On the empty-data profile g=1-a A-b(1-A)B, the remaining B frequencies give the exact residual

    B_i(F)-kappa
       = b^2 q(1-2q)(1-p)
         +Phi([1-ap-bq(1-p)]^2,[bq(1-p)]^2)
         +p(1-p)Phi((a-bq)^2,(bq)^2),               (1)

where Phi(x,y)=phi(x)+phi(y)-phi(x+y). All three terms are nonnegative. For nonempty remaining B masks both amplitudes have magnitude bq times the corresponding (1-A) coefficient, so their total is the first term. For empty remaining B, the empty A Fourier row gives the second term; the 2^r-1 nonempty A rows all have magnitude p and give the third. These are actual coherent rows, including coincident empty rows.

Use Phi(x^2,y^2)<=2|xy| in bits, already independently reconstructed in the campaign. The mean amplitude |1-ap-bq(1-p)|<=1; |a-bq|<=2 since a,bq are in [0,2]. Dividing by d when d>0 gives the three prices respectively b(1-2q)<=2, 2, and 4p<=2. Therefore

    0<=B_i(F)-kappa<=6d,
    D_i H(F)-kappa<=(6+2/ln2)d.                   (2)

The last line adds the full physical concavity gap J<=2d/ln2. Zero d follows directly from (1). If the earlier test failed, p=0 and (1) still holds; if it succeeded, the later test is irrelevant and has zero influence/entropy debit. If B is already resolved there is no B query. All actual core biases, constants, and prior data restrictions are admitted. The explicit alpha^2 log(1/alpha^2) data-sector term remains in the existing signed data drift; it is not replaced by O(alpha^2).

## 2. One reviewed earlier-test payment
For an A query, write F=A u+(1-A)G with G=Bv+(1-B), physically independent of A,u. A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT@1 reconstructs the fine reserve release and actual shared-fallback erasure and proves

    D_A H(F)-kappa_A<=(8+2/ln2)Inf_A(F).

This treats G as the same fallback on both children. Its proof needs no assumption that B has remained unqueried; a current point restriction of B or a constant resolved B is a valid G. REVIEW_A059.md independently reconstructs the source algebra and price, without repair; the source's broader many-stage priority theorem remains at its original order scope. Our later-test calculation is a new order extension, not a modification of the source.

## 3. The shared bit may also remain unresolved
The preceding first-controller restriction can itself be removed by keeping the two X rows explicitly. Still write p=EA,q=EB,a=1-m,b=1-n and Z=pa+(1-p)bq.

For same orientation and a B query BEFORE X, d=(1-p)qb/2 and kappa=(1-p)qVar(v)/2. Its exact residual is

    b^2 q(1-2q)(1-p)/2
     +Phi((1-Z/2)^2,d^2)+Phi((Z/2)^2,d^2)
     +[p(1-p)/2]Phi((a-bq)^2,(bq)^2).              (4)

The two X amplitudes are nonnegative magnitudes adding to1, since 0<=Z<=2, so the two Phi packets together cost at most2d. The other terms cost at most2d each as in Section1. Therefore B-kappa<=6d without revealing X first. Failed or successful earlier tests are handled directly; when p=1 this B query is irrelevant and every term is zero.

For same orientation and an A query before X put nG=1-qb, VG=1-nG^2, h=m-nG, L=1-m nG. Its influence is d=pL/2 and fine release is [p Var(u)+k(p)q Var(v)]/2, k(p)=phi(1-p)-phi(1-2p)/2>=0. Direct empty/nonempty A,B,X rows give

    B = p Var(u)/2 +(p-2p^2)(VG+h^2)/2
          +(VG/2)Phi((1-p)^2,p^2)
          +Phi((1-Z/2)^2,p^2h^2/4)
          +Phi((Z/2)^2,p^2h^2/4).                 (5)

After subtracting the owned first release and dropping only the nonnegative off-label release, the three remaining groups cost at most2d,4d,2d, respectively: VG+h^2<=2L, VG<=2L, |h|<=L, and the two X amplitude magnitudes add to1. Thus B-kappa<=8d even though the fallback and selected branch share the unresolved physical X. Equation(5), not an independent-child replacement, pays this case.

For opposite orientation, an A query has d=pa/2, kappa=p Var(u)/2, and exact residual

    a^2 p(1-2p)/2
       +Phi([1-(ap+bq)/2]^2,[ap/2]^2)
       +Phi([(ap-bq)/2]^2,[ap/2]^2).              (6)

The B formula swaps a,p with b,q. The two first amplitudes have absolute values adding to max(|1-ap|,|1-bq|)<=1; hence residual<=4d. All currently resolved point probabilities0 or1 are allowed for the OTHER test; the queried test has positive remaining width and probability<=1/2. The formulas hold under every actual prior data restriction. Physical JS adds 2d/ln2 throughout.

## 4. Arbitrary controller order, with data interruptions
Start with the shared-bit priority family of A091/A087: select u when X=0 and A succeeds; otherwise select v when X=o and B succeeds; otherwise +1, where o=0 or1. Private point widths are arbitrary positive integers; both data blocks are disjoint and independent. Every controller and data coordinate may be queried in any adaptive order. Irrelevant zero-influence coordinates may be skipped or queried without changing any bill.

For same orientation the X query has one constant killed child, and A087's exact residual price is 3+2/ln2. For opposite orientation its two children depend on disjoint physical blocks, so the price is 4+2/ln2. These geometries hold after any earlier private/data restrictions. Before X use Section3. After same-orientation X, A queries use Section2 and B queries Section1, regardless of which private test is currently ahead. After opposite-orientation X, each live child is a point activation; its query price is at most 3+2/ln2. Thus every controller query on every physical policy obeys D-kappa<=K_ctrl d, K_ctrl=8+2/ln2. Distinct rates are alternatives for nodes, not multiple charges on one edge.

At a data query of core j the actual signed-sector identity and singleton-entropy cancellation give

    D H(F)<=drop(U+R)+(3/ln2)P_j beta_j^2.

Here R is the nonresetting current-probability reserve from A057 stage4, and U uses the current nonempty-core raw entropies. The control-step U drift is zero. Telescoping on the same stopped physical tree proves

    H(F_root)<=U_root+R_root+(3/ln2)T_data
                +(8+2/ln2)Pi_ctrl
                +E[H(F_leaf)-U_leaf-R_leaf].       (7)

The expectation retains actual leaf functions and physical reach weights. At a controller-resolved leaf the profile is phi(m_selected^2)<=Var(selected)/ln2<=I_leaf/ln2; no arbitrary core entropy is dropped. At an unresolved stop its literal profile remains. R_root<=2 I_ctrl(root) funds R once, separately from the controller-node residual rate. It must be added as its own debit, never hidden by taking a maximum of those rates.

## 5. Exact remaining gap
The stopped theorem removes every controller-order restriction for this two-event shared-bit family, including a private query before unresolved X. It does not cover three or more mutually interfering priority tests, shared data between distinct cores, or a generic non-point controller. It retains inherited U_root and the actual terminal profile; these are not universally paid. Full FEI remains open.

The shortest next extension is a third point test queried while two earlier tests remain unresolved, with the same complete core-label rows and fine R. That tests whether the order-free two-event price survives a larger repeated fallback. Another width census or ordered-controller proof would leave that exact gap unchanged.
