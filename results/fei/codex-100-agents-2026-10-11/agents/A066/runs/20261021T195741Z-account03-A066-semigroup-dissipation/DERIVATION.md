# One nonflat data query: an unbounded local deficit and an explicit source payment

All entropy is in bits. Let m>=2, N=2^(2m), delta=1/N and s=2^-m. Binary inputs carry the uniform measure; Fourier characters are (-1)^(T dot x). Put

    b(x)=(-1)^(x_1*x_2+...+x_(2m-1)*x_(2m)),
    c(x,j)=b(x)-2*1_(x=0,j=1),  q(z)=(-1)^z,
    F(x,j,z)=c(x,j)+1_(x=0,j=0)(q(z)-1).

These are actual Boolean signs. Equivalently F=b+1_(x=0)(r(j,z)-1), where r=+1 only at j=z=0. The nonflat core in the incoming A066 representation is c on d=2m+1 data coordinates. Its marked-point value is +1. Query DATA coordinate j, with both physical outcomes retained. The actual children are

    F_0(x,z)=b(x)+1_(x=0)(q(z)-1),
    F_1(x,z)=b(x)-2*1_(x=0).

The z input in F_1 remains a physical dummy; no terminal function or Fourier atom is discarded. Let e=Inf_j(F)=delta/2. The carried accounts from A066 complete-control v1 are G=delta_core H(q)=0 and R=delta_core*d*Var(q)=(2m+1)delta/2. Their actual children have G_0=G_1=0, R_0=2m*delta, R_1=0. Thus E R_child=m delta and D_R=R-E R_child=delta/2=e. These are the same incoming accounts, not fresh descendant accounts.

## Exact spectrum and true data debit

The bent coefficients a_T=hat b(T) are +/-s, with (N+2^m)/2 positive signs and (N-2^m)/2 negative signs. This follows either by tensoring the two-bit Walsh transform (1,1,1,-1)/2, or by its direct character sum. In particular sum_T a_T=b(0)=1. Define

    h(u)=-u^2 log2(u^2), h(0)=0,
    E(v)=sum_T h(a_T-v).

The complete Fourier coefficients, for U a subset of {j,z}, are

    hat F(T,empty)=a_T-3delta/2,
    hat F(T,U)=delta/2 (U nonempty),
    hat F_0(T,empty)=a_T-delta, hat F_0(T,{z})=delta,
    hat F_1(T,empty)=a_T-2delta, hat F_1(T,{z})=0.

Every atom, including empty residual sets, is present in these formulas. Consequently the actual entropy decrement, subtracting BOTH complete child entropies, is

    DeltaH = H(F) - [H(F_0)+H(F_1)]/2
           = E(3delta/2)-[E(delta)+E(2delta)]/2 +delta*(m+3/2).       (1)

No normalized conditional spectrum replaces a physical child. Formula (1) retains the exact rare-row logarithms.

## A uniform curvature bound and an all-width obstruction

On v in [delta,2delta], every |a_T-v| lies between s/2 and 3s/2, since 2delta/s=2s<=1/2. None is zero. Direct differentiation gives

    h''(a_T-v)=4m-[4 ln(|a_T-v|/s)+6]/ln2.

The upper bound h''<=4m follows from ln(|a_T-v|/s)>=-ln2 and 6-4ln2>0. For the lower bound use ln(|a_T-v|/s)<=ln(3/2)<=1/2 and ln2>=1/2; hence h''>=4m-16>=-4m for m>=2. Thus |E''|<=4mN on the whole interval.

The elementary midpoint remainder (Taylor's integral remainder on each side of the midpoint) has magnitude at most M*(b-a)^2/8 when |E''|<=M. Here its magnitude is at most (4mN)*delta^2/8=m delta/2. Substitution into (1) proves

    delta*(m/2+3/2) <= DeltaH <= delta*(3m/2+3/2),
    m+3 <= DeltaH/e <= 3m+3,
    (DeltaH-D_R)/e >= m+2.                                    (2)

Thus NO fixed K bounds DeltaH by D_R+K*e for every nonflat data query in the incoming attachment representation, even though G drops by zero and both true child entropies have already been subtracted. Given any finite real K choose an integer m>=2 with m+2>K. This is a local-payment obstruction, not a Boolean family with unbounded H/I. In particular it rules out replacing the unpaid data step in the previous ledger by a constant query charge plus its released reserve alone.

Boundary checks: m=2 satisfies every bound; m=1 is deliberately excluded because 2s<=1/2 fails. All logarithm arguments above are strictly positive. The finite Fourier sums permit differentiation and integration without interchanging any infinite family or limit.

## The same actual child bank pays this specified query

For this family the missing source is available. Define ONE source account before the query by

    B=4*[I(F_0)+I(F_1)]/2 - [H(F_0)+H(F_1)]/2.

This is the actual unused rate-four surplus after retaining the full prescribed entropy of both terminals. It is not 4I(F) and not an automatically available reserve for an arbitrary core. Its two summands are the source certificates explicitly used here. No earlier debit is assumed; an incoming already-spent account cannot be substituted for B.

Independent physical edge counting gives

    I(F_0)=m+(2m+1)delta, I(F_1)=m+4m delta,
    I(F)=m+(3m+1)delta, E I_child=m+(3m+1/2)delta.

For F_0 the empty-control sector has mass 1-delta on N atoms. Entropy maximization on those N atoms gives its entropy at most (1-delta)*[2m-log2(1-delta)]. The other sector contributes 4m delta. Since -(1-delta)log2(1-delta)<=delta/ln2,

    H(F_0)<=2m+delta*(2m+1/ln2), H(F_1)<=log2 N=2m,
    B>=2m+delta*(11m+2-1/(2ln2))>=2m.                         (3)

Each child individually satisfies its rate-four certificate by these same bounds. In the last inequality ln2>=1/2. The prescribed whole-terminal debt is retained before any bank allocation.

Book the incoming R from B ONCE. Define the additional positive data debit

    L=max(DeltaH-4e-D_R,0).

Equation (2) yields L<=delta*(3m/2-1), so

    R+L<=delta*(5m/2-1/2)<2m<=B.                            (4)

The physical query contribution 4e, the released D_R=e, and at most L from the unused original B-R now pay the entire actual data debit. After paying, the SAME reserve left is E R_child=m delta and the unspent source bank is B-R-L. Nothing is reset: R splits into spent D_R and the inherited child reserve; L has its own disjoint owner. In fact B-R-L >=(59m+1)/32, since delta<=1/16. Full terminal entropies were already withheld in the definition of B, so they fund none of these payments.

This is a complete one-query source payment at fixed physical rate four on the specified nonflat family, together with an all-width obstruction to removing that source. It does not establish that the required B is available after arbitrary prior histories or for an arbitrary core.

## Noise-semigroup translation and both time boundaries

For any one of these finite Boolean functions g, L chi_S=|S|chi_S, T_t=exp(-tL), p_S=hat g(S)^2 and q_t(S)=p_S exp(-2t|S|). The evolving q_t is unnormalized. Define

    J_g(t)=sum_(S nonempty)|S|p_S exp(-2t|S|) ln(1/p_S),
    K(g)=integral_0^infinity J_g(t)dt,
    b_empty(g)=p_empty ln(1/p_empty).

The finite sum obeys J_g(t)<=J_g(0) for t>=0 and J_g(t)<=exp(-2t)J_g(0). Hence both endpoints are integrable, and termwise integration gives 2K(g)=ln2*H(g)-b_empty(g). Equivalently, differentiating the corrected raw entropy sum q_t ln(1/q_t)-2t sum |S|q_t gives derivative -2J_g. The uncorrected raw entropy has no required monotonicity. Since b_empty<=1-p_empty=Var(g)<=I(g), a universal 2K(g)<=A I(g) would imply H(g)<=(A+1)I(g)/ln2. Conversely FEI at C implies 2K(g)<=C ln2 I(g). That all-dimensional integrated payment remains unproved.

For the SAME physical j query,

    2 DeltaK=ln2*DeltaH-Delta b_empty.                       (5)

Here Delta b_empty/ln2 is exactly

    h(s-3delta/2)-[h(s-delta)+h(s-2delta)]/2.

On [s-2delta,s-delta], h''>0: for m>=2, the largest amplitude s-s^2 is at most 3/16. Now 3/16<1/5 and ln5>3/2, with the latter following from ln5>=2*(2/3+(2/3)^3/3)>3/2 by the positive atanh series. Thus the displayed midpoint difference is strictly negative. Consequently 2DeltaK/ln2>=DeltaH. The local obstruction also survives the exact signed heat boundary; dropping or silently renewing that boundary cannot fix it. The entropy source payment translates through (5) with this SAME boundary retained as a signed term; no separate influence payment of its absolute magnitude is claimed.

## Proof status and the remaining universal line

Rung: analytic author proof with exact finite validation; independent review pending. A core Lean check is confined to the width-growth arithmetic after (2); it does not certify the logarithmic curvature or Fourier-to-prose translation. Those are fully specified above for independent reconstruction. No full Mathlib compiler is admitted under the 1.5GB job limit.

First unsupported universal line: for arbitrary inherited nonflat core and an actual selected data continuation, pay its complete positive signed entropy/reference profile from a named unused original source account after old debits, retaining both terminal references and the same R. The source B in (3) is certified here by bent coefficients; that argument does not apply to an arbitrary Boolean spectrum. A universally cheap initial complete reference remains separately unpaid. Full FEI stays OPEN.
