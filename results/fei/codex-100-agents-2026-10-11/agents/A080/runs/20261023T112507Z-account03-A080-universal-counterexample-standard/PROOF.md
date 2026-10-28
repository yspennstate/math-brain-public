# Pivotal transport is coherent; the proposed outer correction is not

All entropy is in bits and functions are actual uniform Boolean signs on
disjoint physical inputs. Full FEI remains OPEN. Exact finite sign receipts
must accompany the analytic argument below; no floating search is a proof.

## 1. Universal transport of inner coherent envelopes

Let B be ANY Boolean outer gate with independent inner Boolean functions
g_1,...,g_m. At a physical restriction let mu_i=E g_i and let q_i be the
probability that outer input i is pivotal under the independent product
biases mu. Let u_i>=0 be an inner credit envelope satisfying
u_i>=(-S_K(g_i))_+ and E_b u_i(g_i|x=b)<=u_i(g_i) for every eligible
physical query of that inner core. The full inner hull is one possible
supplied u_i, but its influence price is not assumed proved.

The inner potential W=sum_i q_i u_i is nonnegative and superharmonic under
EVERY physical query of any core. For a query in core j, q_j does not depend
on mu_j and is unchanged. For i!=j, q_i is affine in mu_j (it is a product-
measure pivotal probability), so E_b q_i(child)=q_i(parent). Other u_i
are unchanged. Thus exactly

    W_parent-E W_child=q_j[u_j(parent)-E u_j(child)]>=0.       (T)

This includes deterministic core faces and zero pivotal probabilities: no
division by a variance occurs. It permits arbitrary different inner cores
and every physical continuation, not just identical substitutions.

Define the exact composition correction

    C(mu)=H(B(g))-sum_i q_i H(g_i).

For nondegenerate biases let beta_T be the squared biased-orthonormal outer
coefficients. Full-spectrum substitution gives
C=H(beta)-sum_i q_i h2(mu_i^2): the within-core conditional spectral
entropies cancel since sum_(T contains i) beta_T=(1-mu_i^2)q_i.
Deterministic faces follow by deleting constant inputs, equivalently by
continuous extension. Thus C depends only on mu, with all constant and
control-only atoms included. Also

    S_K(B(g))=sum_i q_i S_K(g_i)-C.

Hence U=C_+ + W dominates the full negative slack. This is only a stopping
majorant; it is NOT automatically superharmonic. Its exact physical drift is

    E U_child-U_parent
       = E(C_child)_+-(C_parent)_+
         -q_j[u_j(parent)-E u_j(child)].                       (D)

Formula(T) closes the inner transport part of the proposed envelope. The
remaining line is payment of the positive part of(D) from an actual unused
original source. A counterexample to C_+ coherence cannot be repaired by
the inner term when its decrease is zero.

## 2. Actual Boolean family and full rate4 guard

Let G_n(x)=1-2*1{x=0}, n>=1, with G_0=-1. Its Walsh coefficients are
1-2^(1-n) at empty and -2^(1-n) elsewhere, so

    E_n=H(G_n)=ell((1-2p)^2)+8(n-1)p(1-p),
    I(G_n)=2np,                 p=2^-n, ell(z)=-z log2 z.

Take E_0=E_1=0. Independently, every physical coordinate has influence2p.
All restrictions are a smaller point defect or the constant+1. Since
ell(x)<=(1-x)/ln2 and ln2>2/3,

    ell((1-2p)^2) <=6p(1-p),
    4I(G_n)-E_n >=2p+(8n-2)p^2>0.

Therefore the FULL stopping hull R_K(G_n)=0 for EVERY real K>=4 and every
n, including all descendants. These inner envelopes have exactly zero
decrease in(T). Nothing here assumes FEI for arbitrary functions.

Use the two-input gate A(a,b), negative exactly when a=b=-1, and a fresh
balanced bit y. Then F_n=A(G_n,y) is an actual one-vertex defect in n+1
bits. In the bit1=sign-1 convention its negative vertex is mask2^n; flipping
that fresh coordinate gives the canonical G_{n+1} negative at mask0.
This physical cube isometry preserves every H,I, restriction edge and full
stopping hull, not just the multiset of spectral squares. The final direct
fixtures use the ACTUAL AND orientation, with Walsh signs checked there.
The outer pivotal probabilities are q_G=1/2 and q_y=p. Its correction is

    C_n=E_{n+1}-(1/2)E_n.

For all n the candidate U_n=(C_n)_+ has no inner-hull contribution. A query
in G_n gives G_{n-1} on answer0 and constant+1 on answer1, with corrections
C_{n-1},0. A query in y makes the outer correction0 on BOTH outcomes.

## 3. Strict actual physical-query failure at every n>=3

Exactly C_1=2 and C_2=3-(9/8)log2 3>1. At n=3,

    delta_3=(1/2)C_2-C_3
            =(49/32)log2 7-(9/8)log2 3-5/2>0,

and the sign is equivalent to the integer inequality

    7^49 > 2^80 * 3^36.                                    (I)

For the all-n bridge let the biased G mean be t, keep y balanced, and write
C(t) for this SAME outer correction. The outer two Fourier packets give

    C''(t)=-log2|1-1/t^2|,

for0<t<1. Independently, its four packet masses are
(1+t)^2/4,(1-t)^2/4,(1-t^2)/4,(1-t^2)/4. These are the product masses
of two biased bits, giving the elementary identity

    C(t)=2h2((1+t)/2)-(1/2)h2(t^2).

Differentiating this twice gives the displayed derivative, since the two
rational 1/ln2 terms cancel exactly. On1/sqrt2<t<1 it is STRICTLY POSITIVE.
For n>=4, the child means are t_{n-1}=1-2^(2-n)>=3/4 and1, with midpoint
t_n=1-2^(1-n). Continuous endpoint extension and strict convexity imply

    delta_n=(1/2)C_{n-1}-C_n>0,             every n>=4.

Together with(I), this proves failure for EVERY n>=3 and EVERY K>=4.
The failure is a positive MEAN deficit, not merely unequal sibling needs.
Multiplying this proposed U by any positive constant preserves the failure.
It does not invalidate A089's conditional rerouting theorem: that theorem
requires a coherent supplied envelope, precisely the premise failing here.

## 4. Sharp coherent correction for all histories of this family

The correction is continuous at t=1 with value0. The point spectrum gives

    E_n =8n p+(4/ln2-8)p+O(n p^2),
    C_n =4p+O(n p^2),       hence 2^n C_n ->4.

An explicit sufficient estimate for n>=3 is

    |2^n C_n-4| <=(6n+25)2^-n.                              (L)

To derive it, put s=4p(1-p)<=1/2 and use the positive remainder identity
ell(1-s)=[s-sum_{r>=2}s^r/(r(r-1))]/ln2. Its distance from s/ln2 is at
most s^2/[2(1-s)ln2]. Therefore
|ell((1-2p)^2)-4p/ln2|<=30p^2 and the two point-entropy residuals give(L).

Since delta_n>0 for n>=3, 2^n C_n strictly decreases for n>=2 to4.
Thus C_n>0, so the preceding positive-part calculations are exact. Define
the least nonnegative superharmonic MAJORANT OF THIS CORRECTION PAYOFF,
not the full deficit hull of F_n, by

    V_0=0, V_1=2,
    V_n=2^(2-n) C_2,                   every n>=2.            (M)

The exact Bellman recurrence is V_n=max(C_n,(1/2)V_{n-1},0); a y query
kills the correction, and every G query has the same two actual outcomes.
At n=2, C_2>1=(1/2)V_1. For n>=3 the strict delta inequalities prove(M).
Query the G bits along the allzero branch until n=2 to attain it, with
true reach2^{-(n-2)}; stop there. Every other terminal correction is0.
Thus(M) is sharp over EVERY physical adaptive reveal/stopping policy,
including y-first and arbitrarily interleaved y exposure.

The additional initial collateral V_n-C_n is necessary if one insists on
retaining this correction as an active liability. In particular its mean
query deficiency cannot be fixed by internal sibling rerouting alone.

## 5. Normalization and the exact universal boundary

Here I(F_n)=(n+1)2^-n, H(F_n)/I(F_n)<4 and H(F_n)/I(F_n)->4.
Meanwhile

    V_n/I(F_n)=4 C_2/(n+1)->0,
    V_n/C_n -> C_2 =3-(9/8)log2 3<infinity.

So the sharp correction repair is influence-small, and its relative factor
remains finite. The actual full deficit hull R_K(F_n) is0 for K>=4, while
V_n is the hull of an unnecessarily positive component collateral. These
two different quantities must never be identified. The family refutes the
proposed component envelope, NOT FEI and NOT an influence-paid coherent
envelope in general. Disjoint tensoring retains the same finite ordinary
ratio; a spectator gives the influence-weighted average of the two ratios.
Changing from bits to nats multiplies every entropy ratio by ln2. Adding
dummy bits leaves both quantities unchanged. If v is nonempty spectral mass,
H=h2(v)+v*H_cond and conditional mean spectral size is I/v. Thus the matched
conditional ratio H_cond/(I/v)<=H/I. For F_n=G_m, m=n+1, its nonempty
spectrum is exactly uniform on2^m-1 sets, so that ratio equals
2(2^m-1)log2(2^m-1)/(m*2^m)<2 and tends to2. Conditioning the entropy
while leaving influence unconditioned mixes two normalizations and cannot
serve as a uniform-cube FEI disproof.

The first unproved universal line beyond the AND correction repair below
remains: control the positive outer drift
in(D), and its cumulative coherent majorant, using actual unused original
influence-owned resources for arbitrary Boolean cores and outer gates,
with all old credit/debit owners and both complete terminals retained.
Reusing the raw C_+ or assuming a supplied full hull is influence-paid
would reinstate the failed premise. Formula(T) isolates the remaining bill
without restating the entire FEI-equivalent stopping-hull bound.

## 6. Universal arbitrary-core repair for AND with one fresh bit

The failed raw correction has a simple, fully explicit coherent replacement
for ANY Boolean first core g, of ANY dimension. While the fresh balanced
bit y is unrevealed set P=2Var(g)=2(1-(E g)^2); after y is revealed set P=0.
Then P>=C_+, P is superharmonic for EVERY physical query, and P<=2I(g).
Thus this stage also pays this gate's outer correction uniformly in the core,
conditional on whatever coherent inner envelope is supplied.

Here is an elementary all-real-bias proof, independent of the dyadic checks.
C(t)=2h2((1+t)/2)-(1/2)h2(t^2) is even. Let
D(t)=2(1-t^2)-C(t), for0<=t<=1. D(0)=D(1)=0, D'(0)=0 by continuity,
and D''(t)=log2((1-t^2)/t^2)-4. This is positive before1/sqrt17 and negative
after. Hence D is nonnegative on the first interval by convexity and its
initial derivative; on the remaining interval it lies above the chord
joining its nonnegative initial value and its zero final value, by concavity.
In fact D>0 inside except t=0. This proves C<=2(1-t^2); nonnegative P
then also majorizes C_+. No finite grid establishes this continuum claim.

At a core physical query with child means t0,t1 and parent mean(t0+t1)/2,

    P_parent-E P_child=(t0-t1)^2/2>=0.

A y query kills the correction and P on both complete outcomes. These
two facts include all interleavings and constants. Fourier Poincare gives
Var(g)=sum_(S nonempty) ghat(S)^2<=sum_S |S| ghat(S)^2=I(g).
The coefficient2 is optimal among universal envelopes a*Var(g): at t=0
the correction is2 and variance1, realized already by a physical dictator.
This is optimal for that payoff ansatz, not the actual full deficit hull.

For any K>=0 and supplied coherent inner u>=(-S_K(g))_+, the full function
F=AND_minus(g,y) therefore has the coherent full envelope

    U=P+(1/2)u(g)        while y is free,
    U=u(g) or0           on the two y-fixed full outcomes.

It follows that R_K(F)<=2Var(g)+(1/2)u(g). In particular the AND correction
itself costs at most2I(g)<=4I(F), since I(F)=I(g)/2+Pr(g=-1).
On our point sequence this replacement has P/I(F)=8(1-2^-n)/(n+1)->0.
This is a genuine arbitrary-core outer-payment lemma, not an assumption
that the full inner hull is influence-paid. It does NOT show that the
same influence resources remain unused after earlier gates or donors.
Repeatedly charging4I at each composition level could still grow with
depth. The unpaid universal line is a summable original-owner budget for
general outer gates and arbitrary cores, together with initial inner pricing.

## 7. Fresh physical influence pays the correction: exact all-guard hull

The preceding variance envelope can be paid by an ACTUAL DISTINCT original
physical source, without adding another bank. Write p=Pr(g=-1). Then
P=8p(1-p)<=8p, and p is exactly the influence of the fresh physical bit y
in F=AND_minus(g,y). Hence for EVERY real K>=8,

    S_K(F)=(1/2)S_K(g)+Kp-C >=(1/2)S_K(g).

Take u=R_K(g). While y is free define W=u/2, and on its two fixed outcomes
define W=u or0 according as F=g or F=+1. W is nonnegative, superharmonic
for all physical queries (section1), and the displayed inequality proves
W>=(-S_K(F))_+ at EVERY still-free restriction of g. The y-fixed states
are covered by u itself. Thus R_K(F)<=R_K(g)/2. Conversely query y first
and, on its probability1/2 live branch, use an optimal full inner stopping
policy; this yields R_K(F)>=R_K(g)/2. Therefore exactly

    R_K(AND_minus(g,y))=(1/2)R_K(g),       every Boolean g, every K>=8.

This is not a finite extrapolation, nor a claim that an arbitrary full
inner hull is initially influence-paid. It identifies the new correction's
source inside the ORIGINAL K*I decomposition: the fresh physical coordinate
contributes Kp and pays C<=8p. Core influence resources are not charged
again. The finite supplied-envelope induction in REVIEW.md then conserves
all old owner means and signed debit labels, for any reveal order and any
extra retained surplus. No outside donor is renewed.

For ANY integer m>=0 append m fresh balanced AND guards to any fixed
Boolean core g. Iteration gives R_K(F_m)=2^-m R_K(g) for all K>=8, with
all adaptive histories covered, not merely the strategy revealing guards
first. Also p_m=2^-m p, and direct pivotal influence gives

    I(F_m)=2^-m[I(g)+2mp].

The entropy inequality H(F)<=H(g)/2+8p iterates to
H(F_m)<=2^-m[H(g)+16mp]. For nonconstant g, consequently

    H(F_m)/I(F_m)<=max(H(g)/I(g),8).

Constants are harmless and can be handled directly. Thus guards of this
kind cannot turn a bounded-ratio seed family into an FEI disproof, even
when m varies with the seed. Earlier A080 stages already closed stronger
activation-ratio bounds; the NEW conclusion here is exact all-policy
full-hull contraction and its distinct physical-coordinate payment.

The universal remaining obstruction is now sharply located beyond this
fresh-bit case: general outer gates or multiple arbitrary active cores
need a coherent correction funded from disjoint, still-unused ORIGINAL
physical-influence resources. Neither repeated per-level4I charges nor
an assumed influence price for the full inner hull supplies that bridge.
