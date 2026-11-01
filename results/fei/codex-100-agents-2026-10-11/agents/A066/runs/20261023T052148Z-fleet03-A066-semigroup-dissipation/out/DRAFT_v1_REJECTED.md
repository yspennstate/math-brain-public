# Unchanged complete references after the paid DATA query

Units: H and CE are bits; b and K are natural-log quantities. This is a narrow continuation of A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT v2, not a new source construction. The universal projection principle is already present in the campaign, notably A014 v6. Here its literal FULL-reference form is reconstructed and attached to the already-spent A066 ledger; A014 instead also calibrates each child's empty mass. No novelty is claimed for projection itself.

## 1. Exact physical split and the literal inherited reference

Let g be ANY Boolean sign on a finite uniform cube, with Fourier probability p. Fix a normalized reference Q with finite CE(p,Q). Query physical coordinate i and KEEP both children g_+,g_- including all dummy coordinates. For residual T put a=ghat(T), c=ghat(T+i). Then

    pbar(T)=a^2+c^2=(p_+(T)+p_-(T))/2,
    Qbar(T)=Q(T)+Q(T+i).                                      (1)

Both children receive the SAME Qbar, literally the pushforward of the old full Q. Positive child mass implies positive pbar, hence positive Qbar. Thus normalization and finite CE are inherited even if Q has zeros away from actual support. There is no changed empty/nonempty calibration, no child-spectrum replacement, and no fresh reference cost hidden here.

Let C=CE(p,Q)-E_s CE(p_s,Qbar). By (1),

    C=sum_(T,v) p(T,v) log2[Qbar(T)/Q(T,v)] >=0.                (2)

Zero actual terms are omitted. C is exactly the old reference's conditional code length, NOT a refunded KL chosen independently. Let B=H(p)-H(pbar), J=H(pbar)-E_s H(p_s), and D=sum_T pbar(T) KL(p(v|T)||Q(v|T)). The entropy and cross-entropy chain rules give

    DeltaH=B-J,   C=B+D,
    C-DeltaH=J+D >=0.                                         (3)

In particular C>=max(DeltaH,0). This is stronger than merely observing CE decreases: it identifies the payment for the TRUE positive entropy debit and retains both full terminal bills. D is conditional KL; J is the actual children-to-mixture JS. They cannot be booked again after their contribution to C is spent. One can add a prescribed later reset, but its cost is NOT covered by this assertion.

## 2. Original A066 source, prior debit and actually spent L

Retain all hypotheses and notation of v2: d>=0, delta=2^-d, b(0)=1, the physical two-control wrapper, first DATA query j, e=delta/2, R=(d+1)e, fixed original source quota A, old debit tau, fixed full references Q_0,Q_1 at the j children. Let

    U=A-E_s CE(F_s,Q_s)-tau >=3R/2-e/4,
    L=max(Delta_j H-5e,0), S=U-R-L >=0.                       (4)

The amount L is ALREADY spent and stays spent. No argument below redefines A, removes tau, replaces Q_s with an actual spectrum, or allocates R a second time. Write r_0=d delta, r_1=0. The same post-j expected reserve is E_s r_s=R-e. The opening ledger is

    max(Delta_j H,0)+E_s CE(F_s,Q_s)+tau+E_s r_s+S
        <= A+4e.                                             (5)

This follows directly from Delta_j H<=5e+L and
E CE+tau+(R-e)+S=A-e-L. It is the positive-debit version of v2's signed ledger, not a new budget.

Now allow ANY finite adaptive restriction forest below the two j children, stopping at arbitrary cuts. Each child reference is always the literal pushforward of its actual incoming Q. At node h, let w_h be its ORIGINAL reach (including the first factor 1/2 from j), C_h its (2), and P_h=max(Delta_h H,0). Book P_h ONCE from the decrease C_h. The new unspent account increases only by the actual surplus C_h-P_h and by any physically released reserve. Old tau and L are untouched. It is enough, and more conservative, to leave all of those surpluses unspent. Telescoping (2)-(3) gives

    sum_h w_h P_h + E_leaf CE(g_leaf,Q_leaf)
       <= E_s CE(F_s,Q_s).                                   (6)

The references at leaves are precisely each branch's ORIGINAL Q_s projected off its queried coordinate set. Adaptivity causes no renewal. Formula (6) permits queries on genuine seed coordinates, the remaining control z, or physical dummies; it does not require flatness or the wrapper form at later nodes.

## 3. The old reserve survives every physical continuation

Track r only on the F_0 branch while its marked seed cylinder and unqueried literal z survive. If k seed coordinates remain and the revealed seed coordinates are all zero, r=k*2^-k. On F_1, off the marked cylinder, or after z is queried, set r=0. This is the SAME v2 reserve specialized to its current physical attachment.

A seed query in an active node has mean daughter reserve (k-1)*2^-k, so releases 2^-k. A z query releases the entire k*2^-k. Every query elsewhere releases zero. All releases are nonnegative, including k=0 where r=0. Consequently E_leaf r_leaf<=R-e for every adaptive stopping forest. Keeping the opening S unchanged, (5)-(6) imply

    max(Delta_j H,0)+sum_h w_h P_h+E_leaf CE
       +tau+E_leaf r_leaf+S <= A+4e.                         (7)

Thus EVERY unchanged-reference continuation after an admitted j query is paid at ZERO additional source debit, retaining the actual spent L, old tau, and both complete terminal CE/KL bills. The proof even keeps positive entropy debits separately, so it does not undo an earlier spend using a negative later entropy decrement. If A<=K Ibar was genuinely supplied at K>=4, (7)<=K I(F), as before. Supplying such an A cheaply remains an extra hypothesis.

## 4. Signed empty boundary and exact heat-reference transport

For any Boolean g, let m=E g, phi(m)=-m^2 ln(m^2), with phi(0)=0, and b(g)=phi(m). The derivative phi'(m)=-2m(ln(m^2)+1) extends continuously at0. On [-1,1], |phi'|<=2: with |m|=exp(-r), r>=0, this is exp(-r)|2r-1|<=1; the positive branch has maximum 2exp(-3/2)<1, and the negative branch is bounded by1. Hence phi is 2-Lipschitz.

For a physical query put m_+=m+a,m_-=m-a and e_i=Pr[g_+!=g_-]. Booleanity gives |a|=|E(g_+-g_-)|/2<=e_i. Therefore the signed boundary drop satisfies

    |Delta_i b|=|phi(m)-[phi(m+a)+phi(m-a)]/2|<=2e_i.          (8)

The sign can still be either. This explicit dimension-free absolute estimate was NOT asserted in v2; it is added here using the Boolean physical mismatch, not only the spectral inequality a^2<=e_i. The weaker spectral inequality alone would lose the logarithm near a=0. Summing (8) over ANY adaptive tree costs at most2 sum_h w_h e_h<=2I(g); influence telescopes even when dummy coordinates remain.

For q_t(S)=p(S)exp(-2t|S|), J_g(t)=sum_nonempty |S|q_t(S)ln(1/p(S)), K(g)=integral J_g, the corrected heat identity is 2K=ln2 H-b. Each finite g has J_g<=J_g(0) near0 and J_g<=exp(-2t)J_g(0) at infinity. Both endpoints remain integrable; no supremum across functions is exchanged with the integral.

Define the COMPLETE heat reference cost Psi(g,Q)=ln2 CE(g,Q)-b(g)=2K(g)+ln2 KL(p||Q), which is nonnegative. From (3),

    2Delta K + E_s Psi(g_s,Qbar)-Psi(g,Q)
          =-ln2*(J+D) <=0.                                  (9)

The signed boundary cancels EXACTLY because it is retained at both parent and children. Thus heat transport under the same projected reference needs no extra boundary allowance. If one instead leaves terminal CE in bits and only translates the query bill, the safe bound is

    2Delta K + ln2 E_s CE(g_s,Qbar) <=ln2 CE(g,Q)+2e_i,        (10)

by (8). These are two distinct ledgers; their refunds cannot be summed. Equation(9) is the preferred exact continuation. Initial universal heat area, a cheap initial full reference, and any fresh profile-reset cost are still unpaid.

## 5. Adversarial controls and first unsupported line

A literal projection is indispensable to the above refund. Replacing it by a prescribed new normalized full reference Qnew costs the TRUE conversion

    sigma=E_s[CE(p_s,Qnew_s)-CE(p_s,Qbar)].                   (11)

This can be strictly positive even at a zero-influence dummy query. Take g=+1 on TWO dummy bits, incoming Q uniform on all four spectral sets. Query one bit: Qbar=(1/2,1/2), CE before=2, CE after projection=1, C=1, DeltaH=0. On each one-bit child prescribe Qnew=(1/4,3/4): new CE=2, sigma=1. The old release pays that one reset exactly. The alternative target Qnew=(1/8,7/8) costs sigma=2 and exceeds the same C. All actual spectra are empty point masses, all physical influences zero, and no physical-rate charge pays the extra1. This is a reset-owner obstruction, not FEI. The old reference cost is retained; unlimited free resets are not admitted.

FIRST UNSUPPORTED UNIVERSAL LINE: obtain the opening complete references and unused source margin (4) cheaply for arbitrary seeds, OR pay a genuinely changed conditional-nonempty profile after history from the SAME diminished original account. Unchanged-reference adaptive continuation is now closed conditionally on (4); it was too broad to continue listing all arbitrary DATA histories as unpaid. No cheap universal source, arbitrary reset theorem, or full FEI proof follows.
