# A canonical reset can have a positive signed cost

All information is in bits. The counterexample concerns a proposed strengthening of A096's supplied-reference theorem. A096 pays its resets from one original bank; it does not assert that each reset is free. Its report explicitly leaves that stronger sign question open.

## 1. Exact reset and original-bank identities

Let f be a Boolean sign, P its squared Fourier law and Q a normalized reference positive on the support of P. Write CE(P,Q)=-sum P log2 Q. Query physical coordinate j and give both actual children the marginal Q_-j. If B_j=H(S_j|S_-j), then

    CE(P,Q)=B_j+mean CE(P_child,Q_-j)+rho,
    rho=sum_T P_-j(T) D(P(S_j|T)||Q(S_j|T)) >=0.

This is the ordinary cross-entropy chain rule: the average of the two actual restricted Fourier laws is P_-j. Every reference-only atom is retained in Q_-j. Conditional probabilities need only be defined on positive P_-j fibers; Q_-j is positive there. No spectral conditioning is substituted for the physical query.

If prescribed normalized child references replace Q_-j, put

    Z=mean [CE(P_child,Q_new)-CE(P_child,Q_-j)].

For initial quota M, previously booked erasure debit d, and all current complete terminal costs T, the remaining reserve U=M-d-T changes by

    U_new=U+w(rho-Z)

at a queried leaf of reach w. Other leaves and all their full costs stay in T. Thus the exact admissibility condition is w Z<=U+w rho (plus any additional independently specified channel bill). Requiring Z<=0 at every prescribed query is stronger and unnecessary. The construction below refutes that stronger condition even for a paid, calibrated source and the canonical A096 reset.

## 2. The actual Boolean family and its paid source

Use binary physical coordinates; Walsh characters are (-1) to the corresponding parity. Let A_l be the event that its l specified coordinates are zero. Set a=4, b=1, r>=1, n=5+r and

    g=1-2 A_4,
    F_r=1-2 A_4+2 A_(5+r),
    s=1/16, t=1/32, e=2^(-r-4), L=2^r, mu=7/8, v=15/64.

The source lives on five data coordinates, its fifth being a dummy. Query active coordinate j=0; label its Fourier singleton 1 and the dummy singleton 16. The source law is P_g(0)=49/64, P_g(T)=1/64 for 1<=T<=15, and zero otherwise. Give it the normalized reference

    R(0)=49/64,
    R(T)=e^3 P_g(T) for T!=0,
    R(1) += v(1-e-e^3),
    R(16) += v e.

Here += means add to the preceding baseline. Since e<=1/32, all coefficients are nonnegative, 1-e-e^3>0, and every positive source atom receives positive reference mass. R is calibrated at the empty atom, normalized, and has finite source CE. R need not be positive where the true source law is zero; the completed root floor below is positive everywhere.

For r=3 the independent exact certificate proves CE(P_g,R)<14 I(g), with I(g)=1/2. Consequently the supplied source has the explicit finite influence price C0=14. The source-priced A096 envelope uses K=2C0+10=38. The r=8 verification uses the conservative C0=32 and K=74. These are different supplied references and conservative certificates, not two asserted values of the same optimum.

## 3. Incoming complete floor and the prescribed child reset

For the source reference R define k=1-e/s and its completed data marginal

    Rprime(T)=k R(T)+(e/s)mu 1[T=0]+2et.

Let P=P_F and M(T)=sum_U P(T,U), with U a control Fourier set. The joint incoming reference is

    Q(T,U)=Rprime(T) P(T,U)/M(T).

Every M(T)>0 and Rprime(T)>0, so Q is a normalized complete law. At data vacuum Rprime(0)=M(0); hence the reference agrees with the true joint law on every atom of that data row. The root coefficients are ghat(T)+e when U is empty and e otherwise. These formulas are also checked by literal integer Walsh transforms.

Query j. Its zero child is F_(3,1,r)=1-2 A_3+2 A_(4+r); its other child is the constant +1. The latter retains its FULL inherited marginal Q_-j, with cost -log2 Q_-j(0), rather than a newly substituted point reference. Let V=R_-j. Calibrate V to the actual child source g'=1-2 A_3:

    Rchild(0)=9/16,
    Rchild(T)=beta V(T), T!=0,
    beta=(7/16)/(1-V(0)).

The on-child gets exactly the same completed-floor construction, now with parameters (3,1,r), e'=2e, t'=2t and source Rchild. This is precisely the canonical active reset prescribed by A096. Denote that complete law Qnew. The inherited on-child reference is Qold=Q_-j. The signed expected reset bill is

    Z_r=(1/2)sum_(T,U) P_child(T,U) log2(Qold(T,U)/Qnew(T,U)).

The constant child's reset bill is zero because it retains its full old law. No terminal is dropped.

## 4. A five-group exact formula and a positive limit

The source marginal satisfies

    1-V(0)=e(15+14e^2)/64,
    beta=28/[e(15+14e^2)],
    V(T)=e^3/32 for active nonempty T=1,...,7,
    V(8)=15e/64, V(T)=0 for T=9,...,15.

All denominators are strictly positive for every r>=1. Put

    qj=(2s-e)^2+(L-1)e^2=(1-12e)/64,
    Rj=(15-15e-14e^3)/64, u=k Rj+e/16,
    p0=(3/4+2e)^2,
    o0=(7/8+e)^2+u(1/8-e)^2/qj.

After summing identical control atoms, twice Z_r is exactly

    p0 log2(o0/p0)
    +(L-1)4e^2 log2((1+u/qj)/4)
    +7(4qj) log2[(k e^3/32+e/8)/(k beta e^3/32+e/4)]
    +(e/4) log2[(k 15e/64+e/8)/(k beta 15e/64+e/4)]
    +(7e/4) log2(1/2).

The five group masses sum to one. The first two correspond to data vacuum with control empty/nonempty; the third is the seven active nonempty rows; the last two are the dummy singleton row and the seven other dummy rows. These formulas agree atom by atom with independently reconstructed literal child references.

As r tends to infinity, e tends to zero. The first term tends to (9/16)log2(16/9). The third tends to -7/16. The second and last terms tend to zero. In the fourth, its ratio is bounded above and below by positive constants times e for all sufficiently small e, because its numerator divided by e tends to 23/64 and its denominator tends to 7/16. Thus that term also tends to zero by e log(e)->0. There is only this fixed five-term expression; no exchange of an infinite sum and a limit occurs. Therefore

    lim Z_r=(29-18log2 3)/32 >0.

The strict inequality is equivalent to 3^18<2^29, namely 387420489<536870912. The exact interval checker encloses the limit between 0.014 and 0.015 bits. It follows that infinitely many members have positive reset cost. This is not a family with unbounded H/I; it refutes only the individually-free reset rule. The supplied source reference becomes more expensive as r grows, so this limit is not asserted to refute a uniformly source-priced positive-reset allowance.

## 5. Explicit finite certificate, old debit, and complete terminals

The finite certificates give

    0.005 < Z_3 < 0.0053,
    0.014 < Z_8 < 0.015.

The complete root floor, actual erasure, full complementary CE, new complete on-child CE and original source envelope all pass exact rational interval checks. In particular, with W=CE(P_g,R)+10e(5+r),

    CE(P_F,Q) <= W <= K I(F),
    B_j(F)+[CE(P_child,Qnew)-log2 Qold(0)]/2 <= W.

Thus Z>0 does not contradict A096's paid-reset theorem or exhaust the original bank. The actual queried influence is 1/8-e. Exact likelihood subtraction and direct CE subtraction agree; no total-variation proxy is used.

An actual prior positive debit can be retained without manufacturing a history. Tensor F with the independent two-bit sign h=-1+2*1[not all zero], namely values (-1,1,1,1). It has uniform four-atom spectrum, H=2 and I=1. Query its first coordinate using the matching tensor reference. This books exactly B=1 and leaves complete inherited CE=1 in each tensor child (one true child is constant and one a dictator). Reserve those original two tensor bits outside the core quota. Before the core query the same remaining core bank is K I(F)-CE(P_F,Q); after it the remaining bank is K I(F) minus the displayed new whole core bill. The old one-bit debit and the one-bit complete tensor frontier remain present exactly once. The checker reconstructs the entire ten-bit tensor spectrum for r=3. If every terminal function is required to be nonconstant, an additional independent dictator tensor makes it so and adds zero CE; the same formulas remain exact. No tensor reserve funds the core reset.

## 6. First unsupported universal line

For arbitrary Boolean cores, construct a complete admitted reference with a fixed influence price, and select a useful physical continuation/reset for which its POSITIVE weighted likelihood bill, every prior debit and both complete terminal costs fit the SAME unused ancestor bank. The condition is U+w rho-w Z>=0, not Z<=0. Neither the counterexample nor A096's special active-pair geometry provides that universal selection theorem. Full FEI remains OPEN.
