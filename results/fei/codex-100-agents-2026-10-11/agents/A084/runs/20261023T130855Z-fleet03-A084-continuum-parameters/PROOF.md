# The sharp scalar price of a distinct fresh AND influence

Uniform independent physical bits, Boolean outputs in{-1,+1}, entropy in bits. Let g be ANY finite-dimensional Boolean core and y a DISTINCT previously uncharged balanced bit. Define

    F=AND_minus(g,y)=(1+g+y-g*y)/2,
    p=Pr(g=-1), mu=1-2p, eta(t)=-t log2 t, eta(0)=0.

This stage sharpens the source K>=8 fresh-coordinate payment. It does not supply the initial influence price of an arbitrary inner stopping hull and does not assert FEI.

## 1. The complete correction, including empty atoms

The empty and y-only coefficients of F are respectively1-p and p. For every nonempty core frequency B the coefficients with and without y are respectively -ghat(B)/2 and ghat(B)/2. Their inverse is the displayed Boolean polynomial; Parseval and physical edges give

    H(F)=H(g)/2+c(p),  I(F)=I(g)/2+p,
    c(p)=eta((1-p)^2)+eta(p^2)-eta((1-2p)^2)/2+4p(1-p).

The last term is the entropy contribution from duplicating all nonempty core frequencies. The equivalent compact form is

    c(p)=2h2(p)-h2((1-2p)^2)/2.                   (1)

All empty/control-only masses are retained. These are exact identities for every physical core, not a fit to special gates. The fresh coordinate influence is EXACTLY p; no influence of g is charged again.

## 2. One critical point covers the entire real bias interval

c(0)=c(1)=0, c(1/2)=2, and c(1-p)=c(p). On0<p<1/2 direct differentiation of the complete formula yields

    c'(p)=4[(1-p)ln(1-p)-p ln p
                   -(1-2p)ln(1-2p)]/ln2+4-8p,
    c''(p)=4log2((1-2p)^2/[p(1-p)])-8,
    c'''(p)=-4/[ln2*p*(1-p)*(1-2p)]<0.           (2)

Thus c'' has exactly one zero

    alpha=(1-1/sqrt2)/2,

is positive before alpha and negative after. Since c'(0+)=4 and c'(1/2-)=0, c' is strictly positive throughout(0,1/2), so c is strictly increasing there.

For r(p)=c(p)/p put N(p)=p c'(p)-c(p). Then N'(p)=p c''(p). Also N(0+)=0 and N(1/2-)=-2. Hence N is positive on(0,alpha], strictly decreasing after alpha, and has EXACTLY ONE zero p_star in(alpha,1/2). The ratio r increases before p_star and decreases afterwards on(0,1/2]. For p>1/2, symmetry gives c(p)/p<=c(1-p)/(1-p). Therefore

    lambda_star=c(p_star)/p_star                (3)

is the unique global positive-bias maximum of c(p)/p over(0,1]. The ratio extends continuously at0 with value4; its value at1 is0. The zero-mean face p=1/2 is evaluated directly, without dividing by1-2p or taking a logarithm of0.

The certificate isolates p_star by STRICT interval signs N(a)>0>N(b). Since c increases, its exact maximum satisfies

    c(a)/b <= lambda_star <= c(b)/a.             (4)

Thus a finite pair of root endpoints, together with the monotonicity proof, certifies ALL REAL p. A bias grid alone would not establish this. The exact root endpoints in out/CRITICAL_POINT.json are

    a=1009093403773/4398046511104,
    b=504546701887/2199023255552.

They give the rigorous rational enclosure lambda_star in[L/2^192,U/2^192], where

    L=30584055055028322852087698960989038591318835091956761954056,
    U=30584055055088939748285197017141356427055783894288514438176.

In particular487/100<lambda_star<39/8. For readable outward decimal bounds,4.8723210717795<lambda_star<4.8723210717892. The exact integer endpoints, not displayed decimals, decide every verdict. A separate48-term exact Fraction logarithm implementation independently checks both root signs and the price enclosure.

## 3. Sharpness of the scalar owner charge, and its exact scope

For every real p in[0,1], c(p)<=lambda_star p. Consequently the DISTINCT original fresh-coordinate influence Kp already pays the whole correction whenever K>=lambda_star. This is sharp as a universal SCALAR inequality: if lambda<lambda_star, continuity supplies a dyadic p with c(p)>lambda p, and a finite Boolean core with exactly that negative bias is realized by taking the corresponding number of negative truth-table values. The fixed5-bit core negative on masks0..6 is a concrete lower-charge control.

This does NOT establish that lambda_star is the smallest rate for the full deficit-hull identity below. A scalar upper-bound failure may be absorbed by slack in an inner hull; no counterexample to that stronger identity is inferred from c(p)>Kp.

## 4. Exact full-hull contraction for arbitrary cores and histories

For K>=0 let R_K(g) be the least nonnegative physical superharmonic envelope majorizing(H(g)-K I(g))_+. It is the full finite stopping hull, so it covers every physical reveal/stopping policy. Fix ANY real K>=lambda_star. While y is unrevealed set

    W(F)=R_K(g)/2;

after revealing y set W=R_K(g) on the live g branch and0 on the constant+1 branch. Formula(1) and the distinct-coordinate payment give

    H(F)-K I(F)
      =[H(g)-K I(g)]/2+c(p)-Kp
      <=[H(g)-K I(g)]/2<=R_K(g)/2.

This holds at EVERY still-free restriction of g, because the scalar inequality covers its actual bias, including deterministic faces. Under a core query, W is superharmonic by the defining hull property. Under the y query, its child mean is EXACTLY R_K(g)/2. All full outcomes are retained. Hence W is a valid full-composition envelope and

    R_K(AND_minus(g,y))<=R_K(g)/2.

Conversely revealing y first and using an attaining optimal core stopping policy on its probability1/2 live branch gives the reverse inequality. Therefore

    R_K(AND_minus(g,y))=R_K(g)/2,
                    EVERY Boolean g, EVERY real K>=lambda_star. (5)

Iteration proves the exact2^-m contraction for every integer number m>=0 of fresh independent balanced AND guards, including arbitrary adaptive interleavings with every core coordinate. In the FINAL full function each of its m guard coordinates has influence2^{-(m-1)}p. Iterating the entropy identity/inequality gives

    H(F_m)<=2^-m H(g)+lambda_star*m*2^{-(m-1)}p,
    I(F_m)=2^-m I(g)+m*2^{-(m-1)}p.

Thus the complete accumulated new correction is paid by lambda_star times the SUM OF DISTINCT guard influences in the original full function; the scaling of earlier guards is retained. This is not a per-level recharge of all core influence. All guard coordinates are present in the original function, with their designated influence owners initially unused. No old core influence, spent donor, or already booked source is reused.

## 5. Real credits and boundary reductions

The claim is conditional on an inner hull credit being supplied. Given any already supplied a>=W(parent), allocate

    a_b=W(child_b)+a-mean W(children).

All credits and full booked debits S_K(child_b)+a_b are nonnegative; child credit has mean a. Every extra real initial credit D>=0 shifts every descendant credit by exactly D. Thus the entire real half-line of supplied surplus, including equality, is covered algebraically.

Nonnegative credit-owner labels follow kernel a_b/a for a>0. If a=0 all outgoing credits vanish. Old signed debit labels and the new signed query label e=mean S_child-S_parent follow kernel d_b/(D_parent+e) when that total is positive; when it is0, nonnegative child debits are0 and kernel1 retains the zero-total signed labels. Stopped siblings and both full terminal functions are kept. The source is the fresh coordinate's ORIGINAL influence term, not a renewed outside bank.

At p=0 the core and full F are constant+1; both hulls0 and fresh influence0. At p=1, F=y is a character, the core is constant-1, and both hulls0 despite fresh influence1. At p=1/2 the complete formula c=2 is finite. The rate boundary K=lambda_star is included by the non-strict inequality, not inferred from numerical sampling. Physical uniform biases are dyadic; the scalar proof deliberately certifies the whole real interval.

## 6. Hardest audit and first unpaid universal line

The hardest audit is to make sure that the constant/empty coefficient and the y-only coefficient have both been charged; omitting either can falsely lower the maximum. Literal Walsh/direct-character/inverse/edge checks of both complete children and the parent are required. Another control below the rate hypothesis must reject automatic hull contraction, while an underpriced scalar control must not be called an FEI or full-hull counterexample.

This closes the sharp scalar initial price for this fresh owner and improves the source sufficient K>=8 boundary to the certified upper bound for lambda_star. General outer gates or TWO arbitrary active cores still require allocation of their correction to distinct unused original influence owners. The initial influence price of an arbitrary R_K(g) remains open. No universal FEI constant or all-dimensional unbounded H/I family is obtained.
