# A053 stage 2: proper-block descent under point surgery

Work on the uniform physical cube, entropy in bits. For n>=2 and a nonconstant Boolean sign f, define L_A=H(f)-2^(-|A|)sum_a H(f_a), I_A=sum_(i in A)Inf_i(f), and phi(f)=min_(empty != A proper subset [n], I_A>0) L_A/I_A. All dimensions refer to the named ambient physical coordinates; deleting dummies is a separate convention and changes the admissible proper-block family. Independent review of the stage's new result is pending.

## Exact inheritance at equality is false

The stream lead requests continuity so that near-tensors inherit phi<=H/I. The additive continuity theorem can transfer a strict margin but cannot transfer equality with no margin. The exact boundary family is F_n=chi_[n] (a tensor of nonconstant parity factors) and G_n=chi_[n](1-2*1_0), which differs at one physical point. G_n has the same entropy as the n-bit point defect d_n=1-2*1_0 but every influence equals 1-2^(1-n). For a block of size a, only its zero restriction retains an edit; hence L_A(G_n)=H(d_n)-2^-a H(d_(n-a)). Sections 4--5 below prove strict increase of the point-defect ratio and every proper block's strict inequality L_A(G_n)>(H(G_n)/I(G_n)) I_A(G_n). This challenges exact own-ratio inheritance after surgery, not the exact tensor theorem R6 or a fixed absolute FEI bound.

## 1. Uniform block-numerator continuity

Let g=f-2f(v)1_v, p=2^-n, and a=|A|, m=n-a. Exactly one of the 2^a restrictions changes, itself by a one-point flip on m coordinates. For every such child the Boolean entropy difference has the following dimension-only envelope:

    E_0=E_1=0; E_2=2; E_3=3;
    E_m=h2(u_m)+m u_m for m>=4, u_m=2^(1-floor(m/2)).

In dimensions zero and one every Boolean sign has spectral entropy zero. In dimensions two and three, H lies in [0,m]. For m>=4, signed Fourier vectors alpha,beta have ||alpha-beta||_2=2sqrt(2^-m), ||alpha+beta||_2=2sqrt(1-2^-m), so their squared-law TV is at most 2sqrt(2^-m(1-2^-m))<=u_m<=1/2. A maximal common-mass coupling gives |H(P)-H(Q)|<=h2(delta)+delta log2(2^m-1)<=E_m. This recovers the independently accepted stage-1 continuity proof, including zero old coefficients.

Subtract parent and mean-child entropies to obtain the block-specific bound

    |L_A(g)-L_A(f)|<=eta_(n,a):=E_n+2^-a E_(n-a).           (1)

This weighting is essential: the child entropy error is not E_(n-a) at every restriction. Simultaneously physical edge counting gives

    |I_A(g)-I_A(f)|<=2a p.                                 (2)

All estimates are uniform in f, factor count, cut and edited vertex. For all m>=1, E_m<=8m*2^(-m/2), with E_0=0. To verify this for m>=4 use h2(u)<=u[log2(1/u)+log2(e)], u_m<=2sqrt(2)*2^(-m/2), log2(1/u_m)<=m/2-1 and log2(e)<3/2. The resulting coefficient 2sqrt(2)(3m/2+1/2) is <=8m; m=1,2,3 follows directly. Therefore eta_(n,a)<=16n*2^(-n/2). This deliberately coarse uniform remainder is enough for fixed-core tensor limits.

## 2. A second bound retaining the whole joint channel

For any two joint classical laws P,Q on U,V with finite |U|=M and TV delta, one has

    |H_P(U|V)-H_Q(U|V)|<=delta log2 M+h2(delta).             (3)

Proof: match common mass to write P=(1-delta)R+delta P' and Q=(1-delta)R+delta Q'. The conditional entropy of either mixture is its averaged conditional entropy plus I(K;U|V), where K selects the mixture component. The latter term lies in [0,h2(delta)]; the conditional entropies of P',Q' lie in [0,log2 M]. Subtract the two representations. Boundary delta=0 or1 follows directly. This argument is independent of the cardinality of V.

For each sign define the actual child channel law Q_f(x_A,T)=2^-a*f_xhat(T)^2, and the joint parent spectral law P_f(S_A,S_C)=fhat(S)^2. Child Parseval gives the same retained spectral marginal in both experiments. Their chain rules give L_A=M_A+J_A, where M_A=H_P(S_A|S_C) and J_A=a-H_Q(X_A|T). Let delta_P=TV(P_f,P_g) and delta_Q=TV(Q_f,Q_g). Only one child changes, so exactly

    delta_Q=2^-a TV(P_(f_vA),P_(g_vA)).

Applying (3) twice yields

    |L_A(g)-L_A(f)|
      <=a(delta_P+delta_Q)+h2(delta_P)+h2(delta_Q).          (4)

This is a continuity statement for the full joint channel, not a sum of recentred one-coordinate upper prices. For n>=4 it has a dimension-only envelope gamma_(n,a) by replacing delta_P with u_n and delta_Q with v_(n,a)=2^-a w_(n-a), where w_0=0, w_m=1 for 1<=m<=3, and w_m=u_m for m>=4. Both replacing values are <=1/2 and bound the corresponding actual TV, so binary-entropy monotonicity justifies the substitution. Either eta or gamma may be smaller; define b_(n,a)=min(eta_(n,a),gamma_(n,a)). Formula (1) alone remains sufficient for every theorem below. No Gross or log-Sobolev premise is used.

## 3. Denominator-aware phi continuity and strict-slack transfer

For any particular proper block with I_A(f)>2ap, equations (1)--(2) give the one-sided transfer

    phi(g)<=L_A(g)/I_A(g)
      <=[L_A(f)+eta_(n,a)]/[I_A(f)-2ap].                   (5)

Thus selecting a minimizing block A for f proves an upper bound on phi(g) without any lower bound for other coordinates. The additive quotient error for this block is at most

    [eta_(n,a)+(L_A(f)/I_A(f))*2ap]/[I_A(f)-2ap].           (6)

A positive denominator condition cannot be dropped: surgery may create or remove relevance, and the admissible block family then changes. These are fixed-ambient statements; essential-dimension contraction is not silently performed.

Suppose now every coordinate of f has influence >=kappa>2p. Every coordinate of g remains relevant and the proper-block families agree. Both the parent spectral block entropy and actual physical channel information are <=a, so 0<=L_A(f)<=2a. Consequently I_A(f)>=a*kappa and L_A(f)/I_A(f)<=2/kappa. Applying (6) in absolute value to each quotient and then taking minima proves

    |phi(g)-phi(f)|<=eps_phi(n,kappa)
      :=max_(1<=a<n) eta_(n,a)/[a(kappa-2p)]
                       +4p/[kappa(kappa-2p)].              (7)

The same formula with eta replaced by b_(n,a) is valid. For fixed positive kappa the bound tends to zero, and explicitly

    eps_phi<=16n*2^(-n/2)/(kappa-2p)
                       +4p/[kappa(kappa-2p)].

For the ordinary ratio R=H/I, H(f)<=n and I(f)>=n*kappa give similarly

    |R(g)-R(f)|<=eps_R(n,kappa)
      :=E_n/[n(kappa-2p)]+2p/[kappa(kappa-2p)].             (8)

Hence a strict slack s=R(f)-phi(f)>eps_phi+eps_R guarantees phi(g)<R(g). Equality s=0 has no such implication, as the exact family below shows. For a tensor product whose factor-block ratio is strictly below the root ratio, (5) supplies a cut-specific sufficient slack condition. For a fixed nonconstant core h with H(h)>0, F_t=z*h^tensor t has kappa=min(1,min_i Inf_i(h))>0 after deleting seed dummies, phi(F_t)=0 by querying z, and R(F_t)->R(h)>0. Its surgeries therefore eventually satisfy phi(G_t)<R(G_t) and phi(G_t)->0. This follows uniformly in edited vertex. A fixed constant C>0 is eventually larger than phi(G_t), so such surgeries cannot be dimension-critical C-witnesses. This is a scoped quantitative refinement of the admission ledger, not an all-source bound.

The entropy-positive hypothesis matters: a parity core has R(h)=0 and its near-tensor surgeries furnish the next counterfamily.

## 4. Strict point-defect ratio monotonicity: all dimensions

Let d_n=1-2*1_0 and p_n=2^-n. Its exact spectrum is P_empty=(1-2p_n)^2 and P_S=4p_n^2 for S!=empty. Therefore I(d_n)=2n p_n and

    H_n:=H(d_n)=-(1-2p_n)^2 log2((1-2p_n)^2)
                         +8p_n(1-p_n)(n-1).

Define R_n=H_n/(2n p_n). One has R_1=0, R_2=2 and, for n>=2,

    R_n=4-B_n/n,
    B_n=4+4(n-1)p_n-A_n,
    A_n=-(1-2p_n)^2 log2(1-2p_n)/p_n.

Put s_n=1-2p_n and a(s)=-s^2 ln(s)/(1-s), so A_n=(2/ln2)a(s_n). Its derivative on (0,1) is

    a'(s)=s[(2-s)(-ln s)-(1-s)]/(1-s)^2>0,

since -ln s>=1-s and 2-s>1. Thus A_n strictly increases. Also a(s)<=1: the bound -ln s<=1/s-1 gives a(s)<=s<=1. Hence 0<A_n<2/ln2<3 and B_n>1. For n>=2, 4(n-1)p_n is nonincreasing because the next/current ratio is n/[2(n-1)]<=1. Therefore B_n is strictly decreasing and positive; B_n/n is strictly decreasing. This proves R_(n+1)>R_n for every n>=2, and the explicit n=1,2 values complete the result. Since A_n tends to 2/ln2 and n p_n tends to zero, R_n tends to 4. The monotonicity proof is not inferred from the finite orbit certificates.

## 5. One-point surgery breaks exact own-ratio tensor descent

For every n>=2 take the all-coordinate character F_n=chi_[n], an exact product across every cut into two nonempty coordinate sets. H(F_n)=0, I(F_n)=n and phi(F_n)=R(F_n)=0. Flip its value at zero to get G_n=chi_[n] d_n. Character multiplication translates the Fourier law, hence H(G_n)=H_n. It reverses each edge's pivotal status, giving Inf_i(G_n)=1-2p_n and I(G_n)=n(1-2p_n).

For any proper nonempty A of size a, the zero assignment leaves chi_(A^c)d_(n-a), up to output sign; every other assignment leaves a character. Thus

    L_A(G_n)=H_n-2^-a H_(n-a),
    I_A(G_n)=a(1-2p_n).

Writing m=n-a and applying section 4 gives the exact positive own-ratio residual

    L_A(G_n)-R(G_n) I_A(G_n)
       =(m/n)H_n-2^-a H_m
       =2m p_n(R_n-R_m)>0.                                (9)

There are finitely many proper blocks, so phi(G_n)>R(G_n). This is true in every dimension, even though the physical defect mass 2^-n tends to zero and the seed's minimum influence is one. Full Fourier support and tensor primitivity also hold by the stage-1 parity argument. Revealing n-1 coordinates leaves one-bit children of entropy zero, so

    1<phi(G_n)/R(G_n)<=n/(n-1),
    R(G_n)=(2p_n/(1-2p_n))R_n ~8p_n,
    phi(G_n)~8p_n.

Thus continuity remains true, and even relative discrepancy tends to zero, but the exact inequality stays reversed. No unbounded H/I ratio or violation of a fixed positive universal descent constant is obtained. The stream lead's R6 on exact products remains valid; the unsupported transition from exact products to their surgeries must include an additive error or a strict slack.

For n>=3, fix n-2 coordinates to zero. The edited child is the two-bit sign chi_[2]d_2 with ratio 2; meanwhile R(G_n)<=1/(1-2p_n)<=4/3<2 by H_n<=n. All averaged proper-block deficit tests at C=R(G_n) pass strictly by (9), yet this individual child violates that threshold. Passing all averaged block tests does not imply descendant-criticality. This is a concrete all-dimensional refinement of A055's warning about averaged tests. It is not a counterexample to true dimension-critical structure.

## 6. Checked proof boundary and independent validation

The analytic package proves numerator continuity, healthy-denominator quotient continuity, strict-slack transfer, and the exact parity-surgery counterfamily. It does not prove that every high-ratio source has a healthy cut with positive uniform slack; nor does it bound sup_n K_desc(n). A growing-dimension core can have influence denominators tending to zero, outside the fixed-kappa limit. The first unsupported universal line is a finite absolute proper-block descent bound on all genuine dimension-critical violating sources, with full child/terminal entropy retained.

The independent helper checks every product of two arbitrary two-bit signs at one-point surgery zero (translation covers every point in that exhaustive family), all 14 proper blocks, direct physical influences, exact spectral/actual-child marginals, full-channel TV continuity, parent/weighted-child continuity, quotient bounds where denominators qualify, and healthy-kappa phi continuity. It also certifies every block-cardinality orbit of G_n for n=2,...,12 by rational logarithm intervals; dimensions <=8 have direct truth-table/child-Walsh replay. Six strict-slack inequalities for balanced pd_2 powers at t=3,...,8 use explicit certified endpoint constants and no large truth-table job. These are validation, not the source of the all-dimensional implication.
