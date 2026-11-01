# Arbitrary-controller face exposure and overlapping-control obstruction

All probabilities refer to actual uniform physical cubes. H and B are in bits.
For a Boolean sign h and physical split i, write d_i=Pr(h_+!=h_-),
B_i=H(S_i|S_-i), and c_i=I(h_+h_-)/2. J(A)=I(1-2A)/2 for an indicator
A on independent control coordinates; p=EA. Constant indicators are allowed.

## Balanced data-split identity

Let g_+,g_- be Boolean signs with BOTH means zero, independent of A. Put
F_+=1+A(g_+-1), F_-=1+A(g_--1), delta=Pr(g_+!=g_-),
and c_g=I(g_+g_-)/2. Then exactly

    B_i(F)=p B_i(g), d_i(F)=p delta,
    c_i(F)=p c_g+delta J(A).                         (1)

For child coefficients x,y, the parent's row mass is (x^2+y^2)/2 and
its row entropy is that mass times h2((x+y)^2/[2(x^2+y^2)]). Call this
homogeneous degree-two kernel K(x,y). Pure-control child coefficients
are identical, so their K is zero. A core-bearing label (U,T) has child
coefficients Ahat(U) ghat_+(T), Ahat(U) ghat_-(T). Sum K over U and use
sum_U Ahat(U)^2=EA^2=p. This proves B scaling, without approximating logs.
The disagreement event is A=1 and g_+!=g_-, proving d scaling.
The product children equal 1+A(g_+g_--1). Its data influence is
p I(g_+g_-); its control influence is delta I(1-2A). Divide by two.

Both-child balance is essential in the entropy identity. If either mean
is nonzero, the shifted pure-control Fourier rows need their own account;
(1) does not claim to bound them. A027's partial-core signed-bias transport
addresses that different situation.

## Exact exposure ledger and the nonreuse obstruction

Use t independent copies of the established balanced seed b=z times the
selector between bent_m and its zero flip, for fixed even m>=4. Let
delta=2^-m and i_m=1+m/2+(m+1)delta. Query only selectors and control
coordinates during a finite adaptive prefix. Keep all bent data and all
balancing signs unqueried. The prefix processes all t selectors on every
path except paths where A is identically zero. Decisions may depend on
all previously observed control and selector values. Each physical
coordinate is queried at most once per path.

At every selector, both tensor children remain balanced, selector
disagreement is delta, and the core child product is the bent point-flip
disagreement sign, of influence 2m delta. For any K with this seed's
B_selector>K delta (in particular m=4,K=4, by the prior exact certificate),
every reached selector with p_v>0 is strictly K-bad. Formula (1) gives

    Q_selector = delta [m t p + E_T],
    E_T = sum_{selector nodes v} w_v J(A_v),
    I(F)=p t i_m+J(A).                               (2)

Here Q_selector is just the bad-selector charge, not necessarily the
entire tree's bad charge. For each named selector, the stopping histories
partition the uniform input; its reached densities sum to p by conditional
expectation. Histories omitted because A=0 contribute zero. Thus their
total over all t selectors is tp, proving (2) also for adaptive policies.
The prefix retains the actual residual functions and their terminal entropy.

A claimed full-tree payment Q_bad<=L I(F) necessarily requires

    E_T <= (L/delta)[p t i_m+J(A)]-m t p.              (3)

Equation (3) is sufficient ONLY for the selector contribution. Control
bad-node charges, later data charges and terminal entropy remain separate.

At a control split j, ordinary influence decomposition gives

    J(A_v)=Inf_j(1-2A_v)/2 + (J(A_v,+)+J(A_v,-))/2.   (4)

Because the core stays balanced, its F control-query influence equals the
first term. At a selector split, A is unchanged and its average J is
unchanged. Consequently the expected spent control budget is
J(A_root)-sum_leaves w_l J(A_l), while E_T may charge the same reserve
many times. Selectors-first gives E_T=tJ(A), controls-first E_T=0. A reserve
linear in J cannot telescope away the selector amplifier on its own.
For A a k-control point event, p=2^-k and J=kp, recovering the earlier
point-control ledger exactly. This is a refinement of that mechanism,
not a new universal positive candidate.

## Correct overlap ownership

For positive point-subcube events E_e with required-coordinate sets R_e,
let A=OR_e E_e. Inclusion-exclusion and the exact boundary of a point
event give

    p=sum_{nonempty S} (-1)^(|S|+1) 2^(-|union_{e in S} R_e|),
    J(A)=sum_{nonempty S} (-1)^(|S|+1)
                  |union_{e in S} R_e| 2^(-|union_{e in S} R_e|). (5)

To prove the second equation, positive events make A monotone. For each
coordinate j, Inf_j(1-2A)=EA|j=1-EA|j=0. Apply inclusion-exclusion to both
conditional expectations. Terms whose union contains j contribute
2^(1-|union|); other terms cancel. Sum over j and divide by two.
Equation (5) remains valid with duplicated events. Crediting each event's
raw boundary separately is not physical ownership: OR of three single
bits has naive boundary 3/2 and actual J=3/8, a factor four. Repeating one
event M times gives an arbitrarily large naive factor M with the function
unchanged. More generally OR of M singleton events has p=1-2^-M,
J=M2^-M and naive J=M/2, a factor 2^(M-1). These are exact Boolean facts,
not numerical evidence of an FEI counterexample.

## A five-bit counterexample to automatic three-event control goodness

Use control bits x0,x1,x2,x3 in {0,1}, independent balanced core g, and

    A=(x1 x2) OR (x1 x3) OR (x0 x2 x3),
    F=1+A(g-1).                                      (6)

The event masks are (6,10,13), p=7/16, J=3/4. At the root query x0,
d=1/16 and the exact Fourier row calculation yields

    256 ln2 (B_x0-4d)
      =192 ln2-432 ln3+60 ln5-98 ln7+52 ln13+82 ln41 >0. (7)

The prime-log certificate in out/three_event_control_certificates.json
has numerator 4096 times the right side of (7) and denominator
1024^2 ln2, for the initial six-bit core implementation. Its outward
rational sixteen-term atanh lower endpoint is strictly positive.
out/reroute_certificates.json independently reproduces the sign with
one-bit core g=z, using h2-rational atoms instead of prime factorization.
Thus (6) is an actual five-bit counterexample to the automatic-goodness
extension; it does not refute A023's stated two-event theorem or FEI.

The conclusion is independent of which balanced g is used. For a control
split, with other-control label U, put a=hat(A_+)(U), b=hat(A_-)(U).
All nonempty-core rows contribute K(a,b) times sum_T ghat(T)^2=K(a,b).
The pure-control row contributes K(1_{U=empty}-a,1_{U=empty}-b). Thus B
depends only on A. Likewise d=Pr(A_+!=A_-)/2. This proves the exact
transfer from the enumerated seed to ANY balanced core.

The obstruction is overlap among the remaining controls: the third event
shares x2 and x3 with the residual union. It is not an instance of the
fresh-independent-point exposure hypothesis in A023's sufficient lemma.
The other two critical triples are masks (6,11,12) and (7,10,12).
Their bad-root prime-log vectors agree. Each has exactly 18 of the 24
fixed physical control orders with no strictly 4-bad control node.
Order (1,0,2,3) repairs all three. Their x0 query has d=1/16, while the
other root queries have d in {3/16,5/16} and are good. This observation
does not prove a maximum-influence policy in unbounded dimension.
Permuting the four control labels places this witness's bad root first
in any prechosen fixed order. Hence no function-independent control order
can make all three-event unions on four controls zero-bad at K=4.

## Exact finite closure and its universal boundary

All 680 multisets of three nonempty positive point events on four controls
were exhaustively checked, without coordinate reduction. A fixed order
(0,1,2,3) has zero bad controls in 677 cases. The three exceptions above
are repaired by (1,0,2,3), checked at all reachable nonconstant nodes.
By balanced-core transfer, every function in this finite controller
domain and EVERY independent balanced Boolean core has a control-only
stopping tree with no bad-control credit. The core terminal is retained.
The source entropy decrement identity B+JS, JS<=2d/ln2, therefore gives

    H(F) <= (4+2/ln2) J(A)+p H(g).                   (8)

For completeness the balanced activation identity itself is
H(F)=pH(g)+2 sum_U E(Ahat(U))-E(p)+E(1-p),
where E(a)=a^2 log2(1/a^2), and I(F)=pI(g)+J(A). The nonempty-core
coefficients give pH(g)+sum_U E(Ahat(U)); nonempty pure-control labels
give the same sum minus E(p); the constant coefficient gives E(1-p).
Thus the retained pH(g) in (8) cannot be silently discarded.

First unsupported line: a restriction-stable policy for arbitrary Boolean
controllers and cores that simultaneously pays the bad-control nodes,
enforces the nonreuse bound (3), and pays all terminal core entropy with
one absolute multiple of actual influence. No all-dimensional three-event
control-goodness theorem, universal potential, or full FEI solution follows
from the four-control certificate domain.
