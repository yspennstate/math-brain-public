# A private priority list inside one frequent repeated fallback

Rung: analytic proof, author checked; independent review pending. Entropy is in bits. Full FEI remains OPEN.

Let C be an indicator on an exterior finite cube Z, with c=E C>=1/2. Let K0 be zero where C=1 and take values in {-1,1} where C=0. On a disjoint cube W let g be an arbitrary finite private priority list of point tests, with mutually disjoint Boolean selected-core cubes and a constant default. The actual Boolean function is F=K0+Cg. There is one physical copy of g. At an internal unfinished point-test coordinate i, let kappa be the drop of the ORIGINAL merged fine reserve R=sum_h eta(pi_h) Var(h), where the internal fine-label probabilities are c times their actual probabilities in g. Exterior fine labels, when present, are retained. Then

    D_i H(F)-kappa <= K_* Inf_i(F),
    K_*=6+(5+2/exp(1)+ln 57)/ln 2 <21.             (T)

Every finite number of private tests, every finite width, every priority position, arbitrary biases of actual restricted cores and arbitrary internal data-query history are allowed. The exterior K0 may be correlated arbitrarily with C. Its variables must be disjoint from ALL internal variables. The density condition is imposed at the actual node. This is a local fine-profile payment, not payment of arbitrary initial or terminal core entropy.

## 1. Exact coherent decomposition

Use eta(t)=-t log2 t and Phi(a,b)=eta(a)+eta(b)-eta(a+b), with zero conventions. At the queried internal test write q=2^-r, r>=1, u for its core and v for its SAME later fallback. Let m=E u, n=E v, delta=m-n, V=Var(v). Let E be the failure indicator of earlier live private tests, e=E E>0, and K=sum_h m_h A_h prod_{l<h}(1-A_l) their mean profile. Put M=n+q delta, x=q|delta|<=1. Let Z_v be the later fine variance average. A059 v2's direct paired Fourier decomposition, now tensoring each internal row with C and adding K0 only on the completely empty internal row, gives

    d=Inf_i(F)=ceq(1-mn),
    kappa=ce[q Var(u)+k(q) Z_v],
    k(q)=eta(1-q)-eta(1-2q)/2>=0,
    B_i(F)-kappa
      =ce(q-2q^2)(V+delta^2)
       +ce V Phi((1-q)^2,q^2)-ce k(q) Z_v+S,
    S=sum_{s,T} Phi((K0hat(s)1_{T=empty}
                         +Chat(s)(Khat(T)+M Ehat(T)))^2,
                         x^2 Chat(s)^2 Ehat(T)^2).             (1)

Here s ranges over all exterior frequencies, including exterior data, and T over earlier private controller frequencies. Nonempty current/fallback data rows never meet K0. Nonempty earlier internal data rows have zero queried amplitude. Thus (1) includes the repeated-fallback interference rather than deleting it. Since every internal fine-label probability is c times its probability before the wrapper, eta(c r)=c eta(r)+r eta(c); the second term has zero fair drift at a control query. This proves the asserted scaling of the SAME reserve, without resetting it.

## 2. The added exterior logarithm

Normalize mu(s)=Chat(s)^2/c and nu(T)=Ehat(T)^2/e; rows with zero denominator have zero queried squared amplitude and contribute zero to S. The internal last-frequency argument from A059 v2 applies under nu: for J the last nonempty private earlier block, with tail failure product t_J,

    |Khat/Ehat+M|<=3/t_J,   E_nu ln(1/t_J)<=1-e<=1.

Also nu(T=empty)=e, since Ehat(empty)=e. Set U_s=K0hat(s)/Chat(s) on positive mu rows. Parseval and the physical supports give

    E_mu U_s^2 <= ||K0||_2^2/c=(1-c)/c=rho<=1.             (2)

No independence between K0 and C is assumed in (2); the inequality merely omits zero-Chat rows. On a positive queried row the amplitude ratio, before division by x, is

    A_T+1_{T=empty} U_s/e,    A_T=Khat/Ehat+M.

The inequalities (a+b)^2<=2a^2+2b^2 and 1+a+b<=(1+a)(1+b), followed by Jensen only in the exterior probability law mu, imply for x>0

    E_{mu nu} ln(1+(A_T+1_empty U_s/e)^2/x^2)
     <=ln(1+18/x^2)+2
        +e ln(1+2rho/(x^2 e^2))
     <=ln(1+18/x^2)+ln(1+2/x^2)+2+2/exp(1).       (3)

The last line uses 0<e<=1, 1+a/e^2<=(1+a)/e^2, e<=1, and e ln(1/e)<=1/exp(1). This is the additional cost caused by the exterior branch, including the internal empty-frequency mass; no unbounded 1/e is discarded.

The elementary packet inequality Phi(a,b)<=b[1+ln(1+a/b)]/ln2 gives

    S <=ce x^2/ln2 [3+2/exp(1)+ln(1+18/x^2)+ln(1+2/x^2)]
      <=ce x/ln2 [3+2/exp(1)+ln57].                       (4)

For the second step use both log bounds ln(1+a/x^2)<=ln(1+a)+2ln(1/x), x<=1. With A=3+2/exp(1)+ln57>4, x[A+4ln(1/x)]<=A on (0,1], because its derivative is A-4+4ln(1/x)>0. At x=0, S=0 directly. Finally |m-n|<=1-mn, so ce x<=d.

The other two positive sectors in (1) cost at most 6d: V+delta^2<=2(1-mn), Phi((1-q)^2,q^2)<=2q(1-q), and V<=2(1-mn). The negative sector is retained or dropped in the correct direction. The full physical child-channel term obeys JS_i<=2d/ln2. This proves (T).

For the rational upper constant21, 2/exp(1)<1, ln57<25/6 and ln2>56/81 suffice, giving K_*<6+(61/6)(81/56)<21. The exponential bound is certified by a finite positive Taylor partial sum exp(25/6)>57; the ln2 bound is the first two positive atanh terms. A>4 follows already from ln57>1. If d=0 then m=n=+1 or m=n=-1 at a positive guard, so every positive sector vanishes. If an earlier test has already succeeded, reduce to that actual core as suffix; if a guard is identically zero the query is irrelevant. Empty lists, q=1/2, c=1 and constant cores all satisfy the same formulas without canceling zero quantities.

## 3. Shared-selector stopping consequence

Consider the actual shared-selector function

    F=(1-Y)g+Y[A u+(1-A)(B v+(1-B)g)],

where Y is fair and A,B are private point tests, and g is the above private priority list on disjoint variables. Its fallback mask is C=1-Y[A+(1-A)B], so c=[1+(1-a)(1-b)]/2>=1/2 while Y is unqueried. The exterior K0=Y[A u+(1-A)B v] has the exact support required above, even after actual data exposure of u or v. Internal queries are paid by (T) with the SAME fine labels for g, rather than using its unpaid coarse entropy as a substitute.

A091 stage17 pays A queries at 12+2/ln2; A057 stage17 pays B queries at at most12+2/ln2 whenever A is a live point test (a<=1/2), and zero if A is certain. These are direct full-erasure bounds for an arbitrary single physical g, so subtracting the nonnegative ORIGINAL fine R release remains valid; no coarse-to-fine reserve conversion is needed. Exterior A,B queries may therefore be interleaved arbitrarily with the internal queries while Y stays unqueried. The earlier signed data theorem applies to all disjoint fine-core data queries. With

    U=sum_h pi_h[H(h)-eta((E h)^2)],
    R=sum_h eta(pi_h)Var(h),

the original fine U is harmonic at every controller query, and controller R releases are nonnegative. On EVERY finite such adaptive stopping tree, stopping before any Y query,

    H_root<=U_root+R_root+(3/ln2) Pi_data+21 Pi_ctrl
                 +E[H_leaf-U_leaf-R_leaf].                    (5)

Both actual child profiles remain in this expectation, with all earlier debits. Influence has the same-tree identity I_root=Pi_data+Pi_ctrl+E I_leaf. This proof does not allow Y to be queried while retaining the rate for all subsequent nodes without a further argument. If Y is exposed, the present statement stops at its parent. The local exterior-density theorem itself also applies to any other wrapper satisfying c>=1/2, regardless of the number of exterior control coordinates.

An explicit growing-depth family: let A and B each be one private bit, u and v fresh literals, and g_d a priority list of d private d-bit point tests selecting d fresh literals with constant default +1. There are d^2+d+5 variables. Formula (5) covers arbitrary interleavings of its d+2 private tests and all core data, with Y left unqueried. Its priority expression depth grows with d, and actual queried paths may have length d^2+d+4. At a frontier where every variable except Y has been exposed, each leaf is a constant or signed Y, hence H_leaf=U_leaf=R_leaf=0. Here U_root=0. The once-only funding R_root<=2 I_ctrl(root) follows from cube edge isoperimetry on each fine label and Var(h_j)+Var(h_k)<=2(1-m_j m_k) for disjoint sign cores. Consequently this explicit family obeys H<=23 I, although ordinary FEI for the family is not asserted to be new. The new content is the same fine-reserve payment of internal fallback controllers under unresolved shared Y and exterior tests.

## 4. Exact open frontier

The proof requires an exterior fallback mass bounded below at each paid node, and private disjoint internal control blocks. When c tends to zero, (2) supplies rho=(1-c)/c and the present proof costs ln(1+2rho); it does not show that this dependence is necessary, nor provide a counterexample. A source-dependent exterior query that lowers c below1/2 must carry the remaining SAME bank or be stopped before that query. Arbitrary overlapping internal guards, selected cores sharing physical data, generic inherited U and unrestricted terminal profiles remain unpaid. The full FEI conjecture is OPEN.
