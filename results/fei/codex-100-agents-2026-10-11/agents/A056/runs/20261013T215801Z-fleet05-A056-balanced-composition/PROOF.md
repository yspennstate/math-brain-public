# Two-branch controller transport and shared-bit priority ownership

All physical inputs are independent uniform signs. Entropy is in bits. Hplus(f) is the raw **nonempty** sum of squared coefficients times log2 of their reciprocals; it is not conditional entropy. Write b=1/ln2 and

    C0=2+2b+b/sqrt(e)<6.

## Selector theorem

Let c be any Boolean indicator on a finite controller block, a=1-2c its Boolean sign, p=E c, Va=4p(1-p). Let u and v be arbitrary Boolean signs on two mutually disjoint data blocks, both disjoint from the controller. Put F=c u+(1-c)v, m=E u, n=E v, Vu=1-m^2, Vv=1-n^2, and

    d=(1-mn)/2=P(u!=v), z=(m-n)^2/4, M=p m+(1-p)n.

A physical controller-only tree determining c has terminal entropy pH(u)+(1-p)H(v) and consumed controller influence Q=d I(a). For every such tree its full entropy path cost obeys

    Pi_H=H(F)-pH(u)-(1-p)H(v)
         <=d Hplus(a)+C0 d Va.                                 (S)

If Hplus(a)<=T[I(a)-Va], then Pi_H<=max(T,C0)Q. If only H(a)<=K I(a) is certified, Pi_H<=(K+C0)Q. Both terminal entropies are retained. Constants, p=0 or 1, d=0, and z=0 are included.

### Exact spectrum, with the mean collision retained

Write eta(t)=t log2(1/t), eta(0)=0. For nonempty u-Fourier set U and any controller set T, Fhat(T,U,empty)=chat(T) uhat(U). For nonempty v-set V, Fhat(T,empty,V)=(1-c)hat(T) vhat(V). There are no coefficients with both U,V nonempty. These nonempty data rows are distinguishable because the data blocks are disjoint. At empty data, nonempty controller T contributes -(m-n)ahat(T)/2; the completely empty coefficient is M. This exceptional row is the coherent mean collision, and is never discarded.

The controller indicator has

    sum_T chat(T)^2=p,
    sum_T eta(chat(T)^2)=eta(p^2)+Hplus(a)/4+Va/2,

with the corresponding formulas for 1-c replacing p by 1-p. Hence

    Hplus(F)=p Hplus(u)+(1-p)Hplus(v)+d Hplus(a)+G,
    G=Vu eta(p^2)+Vv eta((1-p)^2)
       +(Va/2)(Vu+Vv)+Va z log2(1/z).                          (E)

The coefficient d is exact: [Vu+Vv+(m-n)^2]/4=(1-mn)/2. Therefore

    Pi_H=d Hplus(a)+G+eta(M^2)-p eta(m^2)-(1-p)eta(n^2).        (P)

The negative terminal-empty terms in (P) are necessary. Edge counting proves

    I(F)=d I(a)+pI(u)+(1-p)I(v).                               (I)

Each control edge changes c iff a changes; on such an edge F changes iff u!=v, independently. Data edges of u survive with probability p and those of v with probability 1-p. A control-only stopping tree determining c has exactly these branches and this queried influence, by the physical influence telescope.

### Uniform scalar bound: the same C0 as one-core activation

For w in [-1,1], f(w)=eta(w^2) has f''(w)=-4log2|w|-6b>=-6b away from zero. Its derivative extends continuously through zero. Thus f(w)+3b w^2 is convex across the interval, and

    eta(M^2)-p eta(m^2)-(1-p)eta(n^2)
        <=3b p(1-p)(m-n)^2=3b Va z.                           (C)

The bound -ln p<=(1-p)/p gives eta(p^2)<=b Va/2, and the same bound holds with p replaced by 1-p. Using

    Vu+Vv=4(d-z), 0<=d<=1, 0<=sqrt(z)=|m-n|/2<=d,             (A)

the correction in (P) is at most

    Va[(2+2b)d+(b-2)z+z log2(1/z)].                           (B)

For completeness, write m=1-2alpha,n=1-2beta. Then d=alpha+beta-2alpha beta>=|alpha-beta|=sqrt(z), which proves the last inequality in (A). If z=0, the last correction term vanishes. Otherwise set w=sqrt(z). If b-2+2log2(1/w) is negative, its contribution is already nonpositive. If it is nonnegative, w<=d implies

    [(b-2)z+z log2(1/z)]/d
        <=w[b-2+2log2(1/w)]<=b/sqrt(e).

The final maximum occurs at w=1/(2sqrt(e)), by differentiation; its value is b/sqrt(e). This proves (S) including its continuous endpoints. A rational certificate for C0<6 is ln2>=56/81 and e>8/3>(8/5)^2, giving C0<2+(81/56)(21/8)=2597/448<6. These follow from the first two positive atanh-series terms for ln2 and four exponential-series terms for e. No decimal inequality is used.

If Hplus(a)<=T(I(a)-Va), combine the two independent nonnegative controller resources I(a)-Va and Va to get max(T,C0)d I(a). An ordinary bound pays Kd I(a) plus C0d Va<=C0d I(a). Neither case assumes a bound on u or v; their terminal entropies remain explicit.

## Shared-bit, two-core priority activation

Let s be one fair physical sign. Let A and B be arbitrary indicators on two private finite control blocks, and u,v arbitrary Boolean cores on two further disjoint finite blocks. All five physical blocks are independent. The actual control events are E1={s=+1,A=1}, E2={s=+1,B=1}; both contain the same physical s bit, and their intersection has probability pq/2 when p=E A,q=E B. Priority goes to E1:

    F=1 when s=-1;
    F=u when s=+1,A=1;
    F=v when s=+1,A=0,B=1;
    F=1 otherwise.

This is the first compatible shared-control case with **distinct** cores; it is not the shared-core union already treated by A023. Write delta_u=(1-Eu)/2, delta_v=(1-Ev)/2, a=1-2A, bsign=1-2B, G=1+B(v-1), P=A u+(1-A)G. Define

    d_s=P(P=-1)=p delta_u+(1-p)q delta_v,
    d_A=P(u!=G)=delta_u+q delta_v-2delta_u q delta_v.

Use the actual tree: reveal s first; at s=+1 determine A from its physical coordinates; if A=0 determine B; then stop at u or v or the constant. Its one-time physical accounts are

    Q_s=d_s,
    Q_A=(1/2)d_A I(a),
    Q_B=(1/2)(1-p)delta_v I(bsign),
    I_terminal=(1/2)p I(u)+(1/2)(1-p)q I(v),
    H_terminal=(1/2)p H(u)+(1/2)(1-p)q H(v).                   (O)

The exact root influence is Q_s+Q_A+Q_B+I_terminal. The core-terminal distributions contain no bias conditioning: selection depends only on the physically disjoint controls. The entropy path is exactly the shared-s cost plus half the A-selector cost plus (1-p)/2 times the B-activation cost, which follows directly from the actual leaf partition, or from (P) at the three selectors.

Apply (S) to the shared literal controller selecting P or constant 1 (Hplus=0,Va=I=1), to the A-controller selecting disjoint u and G, and to the B-controller selecting v or constant 1. Then

    Pi_H <= C0 Q_s
          +(1/2)d_A[Hplus(a)+C0 Var(a)]
          +(1/2)(1-p)delta_v[Hplus(bsign)+C0 Var(bsign)].       (T)

The term Q_s occurs exactly once. In particular, a copy of s is not charged to each event's private account. If both private controller signs have strengthened certificates T_A,T_B, then Pi_H<=max(C0,T_A,T_B)(Q_s+Q_A+Q_B). With certified terminal constants L_u,L_v, the complete **path plus terminal** bound has constant max(C0,T_A,T_B,L_u,L_v). If private controllers only have ordinary constants K_A,K_B, use max(C0,K_A+C0,K_B+C0,L_u,L_v). All constants are independent of control widths, core dimensions, overlap probability, and priority event bias, subject to the disjoint private/core block hypotheses.

No core FEI is inferred: H_terminal is retained when L_u or L_v is not known. Formula (T) pays the overlap-owned path but does not provide a universal choice of terminals. A one-bit shared selector was chosen for the ownership test, not as a universal representation requirement.

## First unsupported line and collision frontier

To extend (S) when u,v share actual data, their nonempty row coefficients add before squaring, so the disjoint U/V separation used in (E) fails. There is no proved bound here for that signed nonempty collision by the same controller influence. To reach full FEI, one must price that collision and retain both terminal contributions under a universally admitted physical stopping rule; replacing arbitrary terminal H by an assumed constant times I is the other unsupported line. These are the remaining obligations, rather than the already paid shared control bit.
