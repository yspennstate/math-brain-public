# Independent reconstruction of the active-reset account

Verdict: A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR@1 holds with its stated external floor premise and its active-query restriction. No repair to that version is needed. The result concerns supplied references on a particular Boolean family. It supplies no reference construction for arbitrary Boolean functions.

## Exact objects and dependency boundary

Put N=a+b+r, s=2^-a, t=2^-(a+b), e=2^(1-N), mu=1-2s. The Boolean sign is F=1-2A_a+2A_N. Supply a finite-cost normalized source reference R for g=1-2A_a, calibrated to R(empty)=mu^2; write c=CE(P_g,R). All logs are in bits. The full reference is

    R'(T)=(1-e/s)R(T)+(e/s)mu 1_(T=empty)+2e*2^-(a+b),
    Q(T,U)=R'(T) P_F(T,U)/sum_V P_F(T,V).

Both numerator and denominator are actual spectral probabilities. The positive uniform floor makes every data denominator positive, and sum Q=1. This formula includes reference mass outside the source support. A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 supplies CE(P_F,Q)<=c+10eN and the original quota (2C0+10)I(F) when c_raw<=C0 I(g). This review retains that explicit previously established premise; it does not independently accept the whole A097 theorem. A096's old no-reset identity is also rederived below, rather than treated as an oracle.

## Physical erasure and the necessary a>=2 boundary

An active coordinate pairs the joint vacuum amplitude mu+e with -2s+e, then pairs two equal amplitudes -2s+e on each nonvacuum active-only fiber, and two equal amplitudes e on all other fibers. Thus, for phi(x,y)=(x+y)log(x+y)-x log x-y log y,

    B_j(F)=phi((mu+e)^2,(2s-e)^2)
           +(2^a-2)(2s-e)^2+2^a(2^(b+r)-1)e^2.

The corresponding source expression replaces e by zero. The difference of its nonvacuum terms is -2e(1-4s+e), nonpositive since s<=1/4. For x>=y>0, transferring h from y to x decreases phi(x^2,y^2). To verify the sign, divide its derivative by a positive factor and set z=x/y>=1. The needed inequality is

    L(z)=ln(1+z^2)-z ln(1+z^-2)>=0.

Here L(1)=0 and L'(z)>=2(z+1)/(1+z^2)-z^-2>0: after multiplication by the positive denominator the numerator is 2z^3+z^2-1>=2. For a>=2, mu>=2s and 0<e<=s, so the full amplitude-transfer segment has x>=y>0. Therefore B_j(F)<=B_j(g).

This cannot be extended to a=1. At a=1,b=0,r=1, g is a dictator, with B_j(g)=0, while F has four equal spectral atoms and B_j(F)=1. The final active query must use the separate point-spectrum rule.

## Exact reduction of arbitrary reference profiles

Let V=R marginalized over j and v=R({j}). The off-cell source is constant and costs c_const=-log V(empty)=-log(mu^2+v). The edited off-cell is also constant, but keeps its entire inherited Q marginal and costs k=-log qstar, where direct joint-fiber enumeration gives

    q_j=4s^2-4se+2et,
    kappa=(2s-e)^2/q_j,
    qstar=(mu+e)^2+kappa[(1-e/s)v+2et].

All other source-reference entries have disappeared from this signed complementary excess. They remain in c and in the on-cell reference. In particular the reduction does not delete their costs. Since e<=t<=s,

    q_j>=2s^2+2(s-e)^2>0,
    0<=1-kappa=(2t-e)e/q_j<=e/s.

Writing qstar=A+Bv gives A>=mu^2 and 0<=B<=1. Hence the derivative of (mu^2+v)/(A+Bv) has nonnegative numerator A-Bmu^2. Normalization gives 0<=v<=vmax=1-mu^2. Consequently

    k-c_const=log[(mu^2+v)/qstar]<=-log qmax,
    qmax=(mu+e)^2+kappa[(1-e/s)vmax+2et].

At vmax the source reference may have zero occupied atoms. It is used only as the limit of this one-dimensional rational expression, never as a finite-cost reference supplied to a child. The full Q formula remains normalized even at that algebraic endpoint, so qmax<=1.

## Rational symbolic certificate on the whole parameter domain

Set h=e/s in [0,1]. The bounds above imply

    1-qmax<=2h*vmax-2mu e=6e-4se<=6e,
    qmax>=(1-2s+sh)^2+(1-h)^2*4s(1-s)=L(s,h).

Two exact polynomial identities certify the continuous lower bound:

    L(s,h)-L(1/4,h)
      =(1/4-s)h[(6-4h)-(s+1/4)(4-3h)],
    L(1/4,h)=27/52+(13/16)(h-10/13)^2.

Every factor in the first line is nonnegative for 0<=s<=1/4 and 0<=h<=1: the bracket is at least 4-5h/2>=3/2. Thus qmax>=27/52>1/2. Since ln x<=x-1 and ln2>2/3,

    k-c_const<=-log2 qmax
       <=(1-qmax)/(qmax ln2)<18e.

The strict bound uses e>0 in the actual Boolean family. At the algebraic boundary e=0 both sides of the non-strict bound are zero. No logarithm is evaluated at zero; qstar>=mu^2>=1/4 when a>=2.

## One unchanged account and both terminals

For any physical query the signed child amplitudes are u+v and u-v, so their mean squared law is the parent spectral marginal. If Q is a normalized finite-cost reference, expansion of CE on each spectral fiber yields

    CE(P,Q)=B_j+mean_s CE(P_s,Q_-j)+R_j,

where R_j is the nonnegative conditional occupancy KL, including all reference-only mass in the conditional normalizers. Applying this to the source and then calibrating the on-cell source marginal gives

    B_j(g)+(c_child+c_const)/2<=c.

The specified on-cell reset has envelope W_child=c_child+20e(N-1). Its off-cell sibling retains cost k, not zero. Combining the erasure comparison and signed complementary bound gives

    B_j(F)+(W_child+k)/2<=c+10eN-e=W-e.

At a stopping node the original floor premise pays its full CE by W. At a=1 the on-cell child is -1+2A_(b+r), whose explicit point spectrum is Q_h(empty)=(1-2u)^2 and Q_h(T)=4u^2 for T nonempty, u=2^-(b+r). These masses sum to one. Its new CE equals H(P_h), so the signed reset difference is minus its actual inherited KL and is nonpositive. The off-cell sibling again keeps full inherited CE. The ordinary chain rule therefore pays the last query by W without using the false erasure comparison.

Induct on the remaining active dimension. Every allowed choice of coordinate and stopping point satisfies one of these inequalities; average with the actual physical probabilities 1/2. This proves payment for every finite adaptive active-query tree, including every full set of terminals and every old erasure debit on that tree. An additional unrecorded old debit is not covered. The original root quota is never renewed. Product references for untouched independent terminals retain their full additive costs and fund none of these withdrawals.

Finally I(g)=2as and I(F)=I(g)+e(b-a+r). For K=2C0+10, E=ea<=I(g)/2 and C=eb,J=er imply

    K I(F)-[c+10(C+E+J)]
      >=(K-C0)I(g)-(K+10)E+(K-10)(C+J)>=0.

The original C0 source hypothesis is used here only. It is never reasserted at a child. With the structural source price C0=4 the unchanged rate is 18.

## Exhaustiveness theorem and validation limits

The finite physical checks do not exhaust all a,b,r or all references. The theorem making the reference reduction exhaustive is the exact affine formula for qstar and the monotonicity in v on [0,1-mu^2]; the two polynomial identities and their sign conditions cover the entire continuous domain, and induction covers every allowed active tree in every dimension. Those are proved above independently of the 507 sampled rational scalar fixtures. The fixtures check implementation and endpoints only. There is no reduction of arbitrary Boolean functions to this family.

The exact physical replay uses direct character sums rather than the producer's transform helper. It checks normalized joint references, exact erasure-pair multiplicities, direct physical edge influences, actual restricted children, the full constant-sibling likelihood formula, and all on-cell active-coordinate orders in its frozen domain. Spiked references give 16 strictly positive complementary debts, so retaining that cost is exercised rather than vacuous. No producer checker is imported. Signs use rational 30-term range-reduced atanh intervals. The first unproved universal step remains a prescribed reset after a genuinely non-active query, or arbitrary influence-priced source-reference construction. The rung is a mathematical proof conditional on the stated baseline floor, with independent exact finite validation; any narrow Lean result is reported separately.
