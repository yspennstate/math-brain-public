# Full terminal surplus pays a negative endpoint refund

Author analytic proof; exact checks and external review recorded separately. Entropy is in bits. Full FEI remains OPEN.

Let C=21/4 and d_*=(1-1/sqrt(2))/2. Let u be any uniform Boolean core with t=Pr(u=-1)<=d_*, and let F=1+A_r(u-1), where r>=1 independent fair point controls all pass on A_r=1. Consider ANY finite physical adaptive core/control tree, stopped on a failed control. Project by conditioning ORIGINAL input on all controls passing. No restriction is placed on any descendant core bias, including 1. Both complete physical terminals are retained at every query.

For s controls left write p_s=2^-s, H(F_s(v))=p_s H(v)+G_s(d), d=Pr(v=-1), G_0=0. Put A=G_1. The exact activation identity gives

    G_s(d)-G_(s-1)(d)/2 = A(2p_s d),
    G_s(d)=sum_(j=1)^s 2^(j-s) A(2^(1-j)d).

At the SAME original root t set T_s(d)=G_s(t)+(d-t)G_s'(t), U_s(d)=G_s(d)-T_s(d), and T_0=U_0=0. U may now be NEGATIVE. This explicitly abandons the nonnegative-bank hypothesis of version7; no renewed account is issued. t=0 means the whole function is constant and is handled separately.

## One scalar certificate, unchanged rate

A''(z)=4 log2((1-2z)^2/[4z(1-z)]). Thus A is convex on [0,d_*]. On (0,1/2), A'''<0, so A' is maximized on [0,d_*] at d_*. Since 1/8<d_*<1/6,

    max A' <= A'(1/8)+(1/24)A''(1/8)
           = A'(1/8)+(1/6)log2(9/7) <21/4.

The last strict sign is the exact rational prime-log certificate from version7, reproduced here. Only arguments <=d_* enter derivatives and intercepts in this proof. Nothing is asserted about convexity beyond d_*.

For each j, z_j=2^(1-j)t<=d_*. Convexity and A(0)=0 give A(z_j)-z_j A'(z_j)<=0. Differentiating the finite G_s sum therefore gives

    T_s(0)<=0,       G_s'(t)<=2 C s p_s.

It follows for EVERY d in [0,1], including out-of-band endpoint d=1, that

    D_s(t,d):=2 C s p_s d-T_s(d)>=0.             (1)

For a control query, a_s(d)=T_s(d)-T_(s-1)(d)/2 is the tangent to A(2p_s d) at original t. Its intercept is A(2p_s t)-2p_s t A'(2p_s t)<=0, and its slope is <=2 C p_s. Hence

    a_s(d)<=C q_s(d), q_s(d)=2p_s d,             (2)

on the WHOLE bias interval [0,1]. The actual control decrement h_s can exceed a_s; the signed release U_s-U_(s-1)/2 is retained whether positive or negative. No positivity of that release is needed.

## Exact same-account terminal payment

For an active physical terminal carrying core v and s unqueried controls define the actual FULL signed surplus S_C(F_s(v))=C I(F_s(v))-H(F_s(v)). The exact physical influence is p_s I(v)+2s p_s d. Direct substitution, with no entropy discarded, yields

    S_C(F_s(v))+U_s(d)
       =p_s [C I(v)-H(v)]+D_s(t,d).              (3)

Consequently an independently certified core terminal H(v)<=C I(v) makes the left side nonnegative. More generally the exact sufficient terminal admission is H(v)-C I(v)<=D_s(t,d)/p_s; the residual D may pay some actual core deficit, and need not be discarded. If U_s(d)<0, its ENTIRE debit is paid by this same terminal's positive FULL surplus: S_C(F_s(v))>=-U_s(d). This is a signed pairing, not a second allocation of the terminal influence. If U>=0, the exact combined obligation (3) remains the correct one; no separate FEI assertion about that terminal is silently added.

Let w be actual physical reach and v_weight=w p_s/p_root the original-input projected reach. For any corresponding frontier, the purely algebraic telescope from version7 remains valid without its endpoint hypothesis:

    Pi_H(F)-p_root Pi_H(u)=sum_CONTROL w a_s(d)-sum_ACTIVE_LEAVES w U_s(d).

Combining this with the exact influence telescope gives

    C I(F)-H(F)
      = p_root [C Pi_I(u)-Pi_H(u)]
        +sum_CONTROL w [C q_s-a_s]
        +sum_ACTIVE_LEAVES w [S_C(F_leaf)+U_s(d_leaf)].       (4)

Failed-control leaves are constant and contribute zero. Exhausted controls have U_0=D_0=0. Formula (4) holds at every finite frontier, including partial ones, without sign assumptions. Equation (2) prices every earlier control bill using its OWN queried influence. Equation (3) uses only the actual retained terminal account, once.

If the ACTUAL projected core decrement is independently paid at C and EVERY active projected core terminal has its own independently certified FEI bound at C, (1)-(4) prove H(F)<=C I(F), for ANY interleaving, with no endpoint-bias condition. More generally replace C by any larger fixed rate; same proof. No paid core decomposition is supplied universally. Indeed the conjunction of those two core hypotheses already implies H(u)<=C I(u) by the core telescope, so this conditional closure is explicitly NOT a new universal reduction.

## Actual endpoint witness and limits

Take u=D4 (negative on one of16 inputs), one point control, and reveal all four core bits while leaving the control untouched. The old version7 zero-surcharge helper fails: Pi_H(F)-p Pi_H(u)=G_1(1/16)>0 with Q_control=0. The occupied terminal has d=1, U_1(1)=-T_1(1)<0, and actual terminal F_1(-1) is a dictator with H=0, I=1. At C=21/4 its own surplus C pays -U_1(1), leaving D_1(t,1)>0. All other actual core terminals have d=0 and remain in the exact sum. There is no borrowed sibling allocation. This closes the precise stage18 negative-endpoint guard, rather than withdrawing that guard's refutation of the old zero-surcharge statement.

The root range expands from1/16 in version7 to d_* because the proof now uses only convexity between 0 and the ORIGINAL root. This is a changed hypothesis/payment mechanism, not a change in the quoted rate21/4. Complete terminal cores may be arbitrary Boolean functions; their rate certificates remain hypotheses.

## First unsupported universal line

Find, for an arbitrary core, a genuinely useful proper physical projected partition with a paid core decrement and paid complete core terminals, or independently pay their aggregate signed deficit from an UNUSED original source. The two assumptions above are already a core FEI certificate. Low root bias can encode arbitrary core difficulty by gating; scalar activation control and repeated point-defect examples do not settle that missing source payment. General controller interleavings and root biases above d_* are outside this theorem.
