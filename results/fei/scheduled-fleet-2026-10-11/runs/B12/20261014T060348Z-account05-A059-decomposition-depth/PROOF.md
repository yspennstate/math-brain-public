# All-order private priority stopping via a last-frequency logarithmic moment

Entropy units are bits. Write eta(t)=-t log2(t), Phi(a,b)=eta(a)+eta(b)-eta(a+b), with zero terms interpreted by continuity. All controls and data cores occupy pairwise disjoint physical cubes. Point-test widths, number of tests and actual physical tree depth are arbitrary finite numbers.

## 1. Exact residual at an arbitrary priority test

At any physical restriction node, disregard failed tests, and cut off tests after an already successful test (that successful core is the suffix default). Every unfinished test remains a point indicator on its still-unqueried private bits. Query a bit of test j, whose current point probability is q=2^-r, r>=1. Let earlier unfinished tests have point indicators A_1,...,A_l and probabilities p_i in (0,1). Set

    E=prod_i(1-A_i), e=EE=prod_i(1-p_i),
    C_i=A_i prod_{h<i}(1-A_h), K=sum_i m_i C_i.

Here m_i are current earlier-core means, |m_i|<=1. The actual earlier outputs occupy the complement of E; their nonempty data Fourier rows have no queried-test frequency and contribute zero erasure. On E, the remaining function is B u+(1-B)G, where B is the queried point test, u its current core and G the SAME later fallback on both children. Current u and G remain on disjoint physical blocks even after data queries. Write m=Eu, n=EG, delta=m-n, M=n+q delta, V=Var(G). The fine selectors of G have probabilities a_h and core variances V_h; Z=sum_h a_h V_h. The actual queried influence and fine reserve release are

    i=e q(1-m n),
    kappa=e[q Var(u)+k(q) Z],
    k(q)=eta(1-q)-eta(1-2q)/2 >=0.                  (1)

The earlier selector masses are unchanged. For every later label a_h, probability changes from e(1-q)a_h to ea_h and e(1-2q)a_h; the logarithm of ea_h cancels from its reserve drift. The u rows give erasure e q Var(u), exactly its part of kappa. Pairing all remaining physical Fourier coefficients yields

    B_i(F)-kappa = e(q-2q^2)(V+delta^2)
          + e V Phi((1-q)^2,q^2)-e k(q) Z
          + S,
    S=sum_T Phi((Khat(T)+M Ehat(T))^2,
                         q^2 delta^2 Ehat(T)^2).    (2)

T ranges over earlier controller frequencies. Nonempty remaining queried-test masks have equal paired magnitudes and total multiplier q-2q^2. Nonempty u rows cancel as above. Nonempty fallback frequencies contribute e V, combining fallback mean-profile and data variance by total variance. The empty current/suffix-data sector at empty remaining queried-test mask gives precisely S. Earlier nonempty data rows have second paired amplitude zero, as already excluded. No earlier-output frequencies are discarded or declared independent children.

## 2. Last nonempty earlier frequency

If Ehat(T)=0, its term in S is zero. Define the probability law nu(T)=Ehat(T)^2/e. Since E is a product of private failure indicators, its block frequencies are independent under nu. On block i, the nonempty-frequency probability is p_i, and the empty-frequency probability is 1-p_i: the nonempty squared mass of 1-A_i is p_i(1-p_i), and its total squared norm is 1-p_i.

Let J be the last nonempty earlier block, J=0 when all blocks are empty. Put t_j=prod_{h>j}(1-p_h) and t_0=e. Then

    Pr_nu(J=j)=p_j t_j=t_j-t_{j-1}, j>=1,
    Pr_nu(J=0)=e.

For each frequency with J=j>=1, direct product Fourier division gives

    Khat/Ehat = -m_j/t_j
                  +sum_{h>j} m_h p_h/t_{h-1}.      (3)

Earlier summands have a later nonempty frequency and vanish. On block j the point-indicator Fourier coefficient divided by its failure coefficient is -1. Later blocks are empty. Moreover

    sum_{h>j}p_h/t_{h-1}=1/t_j-1,
    |Khat/Ehat|<=2/t_j.

At J=0, Khat/Ehat=EK/e, with |EK|<=1-e, so the same bound 2/t_0 holds. Since |M|<=1, in every case

    |Khat/Ehat+M|<=3/t_J.                          (4)

Crucially the LOGARITHMIC cost of this tail, rather than its first moment, is uniformly bounded. Let h(t)=ln(1/t). On [t_{j-1},t_j], h(t)>=h(t_j). Therefore

    E_nu ln(1/t_J)
       =sum_j(t_j-t_{j-1})ln(1/t_j)+e ln(1/e)
       <= integral_e^1 ln(1/t)dt+e ln(1/e)
       =1-e <=1.                                 (5)

This is an analytic bound for any number of blocks and any probabilities p_i<1, not an inference from small-width enumeration. In fact the earlier indicators may be ANY Boolean events on independent private blocks: for every indicator A, at every nonempty frequency (1-A)hat=-Ahat, and the total nonempty squared mass is p(1-p). These are the only prefix properties used in (3)-(5). Only the CURRENT queried test needs the point geometry in (1),(2). With no earlier blocks, J=0,t_0=e=1, and (3)-(5) remain valid by empty-product conventions.

## 3. Uniform price for the coherent packet

For a,b>=0, Phi(a,b)<=b[1+ln(1+a/b)]/ln2; this follows from a ln(1+b/a)<=b. Let x=q|delta| in [0,1]. If x=0 then S=0. Otherwise (4),(5) give

    S <= e x^2/ln2 * [3+ln(1+9/x^2)].              (6)

Indeed the ratio a/b of every nonzero Ehat row is at most 9/(x^2 t_J^2), and 1+9/(x^2 t^2)<=(1+9/x^2)/t^2. The two logarithmic tail moments cost at most2.

The function x[3+ln(1+9/x^2)] is increasing on (0,1]: its derivative is 3+ln(1+9/x^2)-18/(x^2+9)>1. Hence its maximum is 3+ln10. Since |m-n|<=1-mn (square both sides),

    S <= [(3+ln10)/ln2] e q|delta|
       <= [(3+ln10)/ln2] i.                       (7)

The other terms in (2) have total cost at most6i, dropping only the nonpositive -e k(q)Z. Namely V+delta^2=1+m^2-2mn<=2(1-mn) gives the first cost <=2i. Phi((1-q)^2,q^2)<=2q(1-q), and V<=2(1-mn), give the second cost <=4i. The latter binary entropy/Hellinger inequality is proved in the prior A059 PRIORITY_PROOF.md and independently reconstructed by A091/A057; it is also reproduced in REVIEW.md here.

Adding the physical child-channel bound J_i<=2i/ln2 to D_i H=B_i+J_i proves, for EVERY unfinished private test, in EVERY actual mixed history,

    D_i H(F)-kappa <= K_ctrl i,
    K_ctrl=6+(5+ln10)/ln2 <17.                    (8)

For the rational upper constant17, ln2>2/3 follows from the first atanh term with positive remaining terms; ln10<7/3 follows from sum_{j=0}^8 (7/3)^j/j! >10, checked exactly. Thus (5+ln10)/ln2<11. If e=0 the queried test is irrelevant, and D=kappa=i=0; zero influence endpoints follow directly. No nonnegative lower bound on D-kappa is claimed.

## 4. All-order stopped theorem and growing-depth family

Take any finite private priority list of disjoint point tests selecting independent disjoint Boolean cores, with a final constant default. Tests and data may now be queried in ANY adaptive physical order. At every node the reduction in Section1 is valid: discarded failed tests and irrelevant suffix tests have zero selector mass; an already successful test becomes the actual suffix core. A queried unfinished test is exactly (1),(2), so (8) applies. Queries of irrelevant remaining controls have all three terms D,kappa,i zero.

Keep the original fine reserve and nonempty-core entropy

    U=sum_j q_j[H(u_j)-eta((Eu_j)^2)],
    R=sum_j eta(q_j)Var(u_j).

The independently accepted A059 signed data theorem gives, for a data query of core j with squared singleton beta_j^2,

    D_i H <= drop(U+R)+(3/ln2)q_j beta_j^2.

At control queries U is a martingale and drop R=kappa. Summing on the SAME finite actual tree, with physical visitation weights, proves

    H(F_root)<=U_root+R_root+(3/ln2)T_data
                   +K_ctrl Pi_ctrl
                   +E[H_leaf-U_leaf-R_leaf].      (9)

T_data is the spent weighted data-singleton bill; Pi_ctrl is spent actual controller influence. The same-tree influence identity is I_root=Pi_data+Pi_ctrl+E I_leaf, with T_data<=Pi_data. At controller-resolved leaves the profile is eta((Eu_leaf)^2)<=Var(u_leaf)/ln2<=I_leaf/ln2. Arbitrary unresolved profiles and inherited core entropy remain literal terms. R_root<=2I_ctrl(root) is a separate once-funded debit, not part of or renewed by (8).

For each d>=2, take d private point tests, each on d bits, and d private literal cores, with default +1. This actual Boolean family on d^2+d inputs is covered under any physical policy, including a policy exposing the last test first and interspersing data queries. Its natural binary priority expression has growing depth, and ordered control paths may have length d^2. No bounded-depth premise is used in (9). This class's ordinary FEI closure was already known; the new result is one fine-reserve rule valid throughout arbitrary mixed histories.

## 5. Exact universal frontier

The earlier two-test order extension from A091 and the shared-bit extension from A057 are consumed baselines, not claimed again. This stage removes the private order restriction for ANY number of private point tests, including a middle test with nonconstant later fallback and a last test with multiple undecided earlier tests. It also covers ANY-order exposure of one common activation bit X when every event has the SAME X orientation: write the gate as a priority list whose first point test is the opposite X value and whose first core is the constant +1. All subsequent private tests are unchanged. This is exactly the disjoint-test theorem with a constant initial core; no independent copies of X occur. Mixed X orientations among many events are not asserted here.

The first unsupported line is replacing the product failure guard E by a general OVERLAPPING guard while keeping the logarithmic moment (5) uniformly bounded, or replacing the CURRENT point query by an arbitrary non-point controller query. Independent non-point earlier events are already allowed by the prefix lemma above, but their own queries are not paid by (8). Neither an arbitrary controller payment nor universal inherited U/terminal payment follows from (9). Shared physical data between selected cores also invalidates the mismatch product formula. Full FEI remains OPEN.
