# The canonical reset is positive; its actual query pays it asymptotically

All logarithms use base two unless ln is written. Inputs are independent fair
bits; Fourier character chi_S(x)=(-1)^{popcount(S&x)}. A physical query has two
fair outcomes. Every terminal CE includes the full normalized reference,
including reference-only atoms. The root source is supplied once.

## 1. Exact target and original Boolean reconstruction

For every integer m>=4 let s=2^-m and e=s^2. On n=2m+1 physical coordinates
take m active data bits, one dummy data bit and m control bits. Let A_l mean
that its specified l coordinates are all zero, and set

    g=1-2 A_m,             F=1-2 A_m+2 A_(2m+1).

These are actual signs: F is negative on the active-zero cell except at the
single all-zero vertex. The source ignores the dummy and controls. On its
m+1 data coordinates its Fourier law has mean-square mu^2=(1-2s)^2 at empty,
mass4s^2 on each nonempty all-active frequency and zero elsewhere. Thus
I(g)=2ms. In F each active coordinate has influence2s-e; each of its m+1
dummy/control coordinates has influence e. Therefore

    Inf_j(F)=2s-s^2,          I(F)=2ms+s^2.

An active j query produces an on-child with a=m-1,b=1,r=m, and a constant
off-child. The off-child keeps its whole inherited reference; it is not reset
to a free point law. No spectral conditioning replaces this physical query.

Write v=4s(1-s), choose the j singleton and the dummy singleton d. Define
the normalized supplied source reference

    R(empty)=mu^2,
    R(T)=4s^8 on every nonempty active T,
    R(j) additionally receives v(1-s^2-s^6),
    R(d)=v s^2,
    R(T)=0 on other dummy-containing T.

Its mass is mu^2+s^6 v+v(1-s^2-s^6)+v s^2=1. All occupied true source
atoms receive positive reference mass; reference ghosts remain in R.
For s<=1/16, R(j)>=s because v>=15s/4 and 1-s^2-s^6>3/4. The vacuum
CE is at most4s/ln2<6s, using ln2>2/3. The j atom costs at most4ms^2;
all other occupied nonvacuum atoms have exact code length8m-2. Hence

    c=CE(P_g,R)<=6s+4ms^2+4s(8m-2)
                 =32ms-2s+4ms^2<=34ms=17 I(g).

The last inequality uses s<=1/2. A SINGLE source price17 applies to every
integer m>=4; source cost is not silently allowed to grow relative to I(g).

## 2. Complete incoming floor and the prescribed canonical reset

For general parameters a,b,r put s0=2^-a, t0=2^-(a+b), e0=2^(1-a-b-r)
and mu0=1-2s0. With a normalized source R calibrated to mu0^2, define

    Rprime(T)=(1-e0/s0)R(T)+(e0/s0)mu0 1[T=empty]+2e0 t0.

For this actual point edit the root Fourier coefficient is ghat(T)+e0 on
control vacuum and e0 on every nonempty control frequency. Let P be its
squared law and M(T)=sum_U P(T,U). Give it the complete normalized law

    Q(T,U)=Rprime(T) P(T,U)/M(T).

Every M(T) and Rprime(T) is positive here. Normalization follows by summing
over U then T; at T=empty, Rprime(T)=M(T), so that data row matches the true
joint spectrum exactly. No reference-only source atom is removed.

At our root a=r=m,b=1, k=1-s and Rprime(T)=kR(T)+s mu 1[T=empty]+s^3.
After querying j, let V be the frequency deletion marginal of R. Its
nonempty mass is4s^3[1-s+s^4(1-2s)]>0. Calibrate V once to source mean-square
(1-4s)^2:

    Rchild(empty)=(1-4s)^2,
    Rchild(T)=beta V(T), T nonempty,
    beta=2(1-2s)/[s^2(1-s+s^4(1-2s))].

Apply the SAME completion formula to the actual on-child, now with s0=2s,
e0=2s^2,t0=s. This gives Qnew. Let Qold be deletion of j from the entire
incoming Q, used at BOTH physical children. Only the on-child is reset.

## 3. Independent five-group reconstruction and A003 verdict

Put L=1/s and define

    Rj=v(1-s^2-s^6)+4s^8,
    qj=s^2(4-3s),       u=(1-s)Rj+s^3,
    p0=(1-4s+2s^2)^2,
    A=(1-2s+s^2)^2,    B=(2s-s^2)^2,
    o0=A+u B/qj.

The on-child's true mass and old/new reference ratio split into five groups:

| True mass | Old/new reference ratio |
| --- | --- |
| p0 | o0/p0 |
| 4s^3(1-s) | (1+u/qj)/4 |
| (1/(2s)-1)4qj | ((1-s)8s^8+2s^3)/((1-s)beta8s^8+4s^3) |
| 4s^3 | ((1-s)v s^2+2s^3)/((1-s)beta v s^2+4s^3) |
| (1/(2s)-1)4s^3 | 1/2 |

Their masses sum exactly to one. The first two are data vacuum with control
vacuum/nonvacuum, the third consists of the remaining active rows, and the
last two are the dummy singleton row and the other dummy-containing rows.
The fixed five-term expression gives

    Z=(1/2) sum_groups mass log2(ratio).

The factor1/2 is the physical on-child reach. The complementary child's
reset is exactly zero, but its inherited CE is fully retained.

Here p0=1-8s+O(s^2), o0=1+O(s^2). Group1 divided by s tends to8/ln2.
Group3 has mass/s->8 and ratio->1/2, giving -8. Group2 has mass O(s^3)
and ratio comparable to1/s; group4 has mass4s^3 and ratio comparable to
s^2; their contributions divided by s vanish by s^2 log(s)->0. Group5
has mass O(s^2) and fixed log ratio. Positivity of every denominator holds
throughout0<s<=1/16. Rational functions after their explicit powers of s
are removed extend smoothly to s=0; their nonzero leading coefficients
justify all comparisons. Thus, with NO growing sum/limit exchange,

    Z/s ->4/ln2-4>0,
    Z/Inf_j(F) ->2/ln2-2>0,
    Z/e ->+infinity.

The strict sign uses0<ln2<1. For every fixed edit-price constant A0>=0,
some actual integer m has Z>A0 e while c<=17 I(g). This independently
accepts A003-CANONICAL-RESET-NO-EDIT-MASS-PRICE@1 unchanged. Its claim concerns
positive reset cost, not the signed query transaction and not FEI.

## 4. NEW: one actual conditional-KL fiber asymptotically pays the reset

The query's conditional occupancy refund is

    rho=sum_frequency_fibers p_fiber KL(p(.|fiber)||Q(.|fiber))>=0.

Every summand is nonnegative because it is a KL divergence between two
normalized conditional laws on that occupied fiber. Its data-and-control
vacuum fiber consists of the root frequencies empty and {j}. Their true
masses are A,B; their reference masses are A,u B/qj. Therefore this ONE
fiber contributes exactly

    rho0=(A+B) log2(o0/(A+B)) + B log2(qj/u).

Although the second displayed term is negative, their sum is the complete
weighted KL for the fiber, so rho>=rho0>=0. It is not valid to treat the
second term as a separate refund or delete it from the expression.

Expanding from the definitions,

    A+B=1-4s+10s^2+O(s^3),
    u=4s-8s^2+O(s^3),
    qj=4s^2-3s^3,
    o0=1-3s^2+O(s^3).

Hence [log2(o0)-log2(A+B)]/s->4/ln2. Also qj/u=s(1+O(s)), B=O(s^2),
so B log2(qj/u)/s->0. The ordinary derivative of ln at1 and
s log(s)->0 suffice; no limit is passed through an unbounded sum. Therefore

    rho0/s ->4/ln2,
    (Z-rho0)/s ->-4,
    limsup_(m->infinity) (Z-rho)/Inf_j(F) <= -2.

In explicit quantifiers: for every eta>0 there exists an integer M_eta
such that for every m>=max(4,M_eta),

    Z_m-rho_m <=(-2+eta) Inf_j(F_m).

In particular the same query earns at least Inf_j(F_m) of net credit for
all sufficiently large m (take eta=1). The six finite certified members
also have Z-rho0<0; their signs are separate finite results, not a claim
that the eventual cutoff in this theorem is exactly m=4.

## 5. Whole original account, a genuine old debit and both terminals

For the physical query, erasure B_j=H(S_j|S_-j) obeys the exact complete
reference identity

    CE(P_F,Q)=B_j+E_child CE(P_child,Qold)+rho.

This follows by CE chain rule and the identity that the average ACTUAL
squared child spectra is the frequency deletion marginal of P_F.
Conditional reference distributions are normalized on every positive true
fiber; Q is positive there. No entropy-decrement JS term is mistaken for
erasure. Including the prescribed on-child reset yields

    B_j+E_child CE(P_child,Qfinal)-CE(P_F,Q)=Z-rho.

Thus for any ORIGINAL unused reserve U at a reached node of physical weight w,

    U_new=U+w(rho-Z).

All other old terminals and booked debits remain in U. The preceding theorem
shows this transaction increases that SAME reserve for all sufficiently
large m; it does not demand an additional O(e) source allowance.

A genuine old debit can be retained by tensoring the independent AND2 sign
(-1,1,1,1), whose spectrum is uniform on four atoms, H=2,I=1. Query one of
its physical coordinates with its matching reference. Its erasure is exactly
one bit, its conditional refund zero, and EACH child retains complete inherited
CE=1, even though one child is constant. Reserve its original2-bit cost:
one bit booked and one bit remaining. There is NO donation to the core
reset. Disjoint Fourier tensor factorization leaves the core identity and
all its signs unchanged. This is an actual prior history, not an invented
entry in the account.

## 6. Checks, scope and first unpaid line

check.py independently reconstructs the actual truth tables at m4 and m5,
their complete root and on-child Fourier spectra by direct character sums,
physical edges, normalized R/Q/Qnew and full retained off-child costs.
It checks the five-group likelihood formula against the literal reference
ratios, computes the FULL conditional refund and the single-fiber lower bound,
and reconstructs the signed account in two ways. The other fixed values
m6,8,16,32 use the derived rational group formulas only. The separate rational
leading-term audit verifies the expansions, not just a numerical extrapolation.

Outward logs reuse A092's stage17 elementary arithmetic:100-bit mantissa
enclosures,44 positive atanh terms,112-bit directed term rounding and the
proved tail9/[4*89*3^89]. Negative weights reverse endpoints correctly.
Interval overlap checks consistency only; the identities above are algebraic.
The finite signs use strict outward lower/upper bounds. A pilot, frozen fixed
domain and exact source hashes precede execution. No producer helper is run.

The source price17 and positive-Z obstruction are independently accepted.
The new refund theorem is an analytic proof with exact finite checks,
pending a second independent review. It does not supply a universal source
reference or prove that every interleaved original-source reset is paid.
A096's supplied-likelihood selective-frontier theorem is consumed only for
scope/context; its whole theorem and negative-cell rate18 corollary are not
independently accepted in this run. Source price17 here corresponds to the
producer's rate44 envelope, not its distinct structural-source rate18 case.

The first unpaid universal line remains an influence-priced source and an
actual selected mixed-history reset for which Z-rho and every separate channel
bill fit the SAME unused ancestor account with both complete terminals. This
family refutes an edit-only price for Z but does NOT obstruct that signed net
payment: its large reset bill has an even larger honest query refund.
