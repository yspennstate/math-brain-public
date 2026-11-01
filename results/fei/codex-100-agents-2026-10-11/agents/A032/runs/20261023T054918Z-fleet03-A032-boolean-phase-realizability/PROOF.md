# A third prescribed tail change with an arbitrary retained Boolean core

All logarithms and costs are in bits. This is a conditional, complete-reference
history theorem; the incoming source reference and earlier debits must already
be paid. It supplies no universal influence price and no new Booleanity
admission inequality. Actual truth tables, not normalized surrogate vectors,
are used throughout.

## Construction and first retained mixture

Use the original four-bit A079 rows

    a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1], b=1-a^2.

Put A=ahat, B=bhat, beta=3/8. For U=0,...,7, A_U=1/8;
B_0=B_4=3/8 and the other six B_U=-1/8. For U=8,...,15,
B_U=0. The rows satisfy ab=0 and a^2+b^2=1 pointwise.

Let k be ANY Boolean core on d>=1 independent bits x, possibly constant
or depending on fewer than d bits. Add physical bits i,j and set

    h(i,j,x)=1 if i=+1, and j*k(x) if i=-1;
    F(z,u,i,j,x)=a(u)+z*b(u)*h(i,j,x).

These are Boolean at every input. All physical restrictions remain Boolean,
so every signed convolution identity is satisfied, not just a fixed prefix.
Write p_k=khat^2, mu=E k, r=mu^2. The seed h has mean1/2 and spectrum
p_h(empty)=p_h({i})=1/4, and p_h({j}+T)=p_h({i,j}+T)=p_k(T)/4.
The four label types are disjoint. Supply R(empty)=1/2 and
R_tail=p_h_tail, with every reference-only atom carried explicitly.

Choose ANY normalized positive law U on the nonempty (j,x)-frequency labels
with U({j})=1/7. Such a law exists because d>=1. Define the FIRST target S1
on nonempty (i,j,x) labels by

    S1({i})=1/15;
    S1(V)=S1(V+{i})=(7/15)U(V), V nonempty in (j,x).

It is normalized. A032's signed tag reset uses the ACTUAL mixture
M=(7/8)p_h_tail+(1/8)S1. Its two complete references are
Q_sigma(U0,empty)=(A_U0+sigma*(1/2)*B_U0)^2 and
Q_sigma(U0,T)=B_U0^2*(3/4)*M(T) for nonempty T. Here U0 is a controller
frequency; it is distinct from the probability law U. Its complete physical
tag-query plus fresh-reference increment is <-1/64, using
21^18>2^79, as in the prior A032 theorem. No earlier debit is removed.

## Second query and prescribed second mixture

Query i at BOTH tag children, carrying their current full marginalized
references first. M({i})=3/10. The inherited total vacuum mass is
1-beta*(3/4)*(7/10)=257/320. The two actual seed children are 1 and j*k.
The latter is balanced, including when k is constant. The current conditional
nonempty seed law after the marginalization is EXACTLY

    L=(5/6) embed_j(p_k)+(1/6)U,

where embed_j puts p_k(T) at {j}+T. Calibrate to every actual signed vacuum
atom and the actual tail mass; use the prescribed SECOND tail

    N=(7/8)L+(1/8)delta_{j}.

The constant i-child stops with its full actual controller spectrum. Both
signed nonconstant i-children retain this same N. Finite incoming CE ensures
the inherited reference supports every occupied child. Calibration refunds
the KL of the full coarse law consisting of each controller-vacuum atom and
one complete tail atom. On the constant child this refund is at least
log2(320/257); on the balanced child it is nonnegative. The second mixture
cost is at most beta*log2(8/7) on that latter child. Thus the COMPLETE
i-query/reset increment, at EACH signed tag child, is at most

    -(1/2)log2(320/257)+(3/16)log2(8/7) < -1/10.

The exact integer guard is 320^40*7^15 > 2^8*257^40*8^15.
This uses the actual first target component, not the original unmodified
source tail. This is the A033 post-tag identity applied to a new arbitrary-core
selector, not a claim that physical erasure is bounded by influence.

## Third query: uniform refund from the signed vacuum

Now at each nonconstant i-child query the ACTUAL bit j, from its CURRENT
coherent reference with seed j*k and tail N. Let t=N({j}). Since U({j})=1/7,

    t=(35*r+7)/48,   r=mu^2.

Before a fresh reset, its inherited controller-vacuum atoms are
q_v(U0)=A_U0^2+B_U0^2*t and its total tail mass is beta*(1-t).
The actual j-child has seed +/-k, signed mean v=+/-mu and complete coarse law

    Pco=((A_U0+sigma*v*B_U0)^2 for all U0, beta*(1-r));
    Qco=(A_U0^2+B_U0^2*t for all U0, beta*(1-t)).

Both are normalized. Write Rco=D(Pco||Qco) and d0=r-t.
At the two vacuum labels {0,4}, the sum of Pco-Qco is
Delta_L=3*sigma*v/16+9*d0/32. At the other six labels below8 it is
Delta_S=-3*sigma*v/16+3*d0/32. The remaining eight vacuum differences are0;
the tail difference is -3*d0/8. Therefore, for the FULL L1 distance ell,

    ell >= |Delta_L|+|Delta_S| >= |mu|/4,
    ell >= 2*beta*|d0| = (3/4)|d0|.

Indeed Delta_L-3*Delta_S=3*sigma*v/4 and the triangle inequality gives
the first bound; total vacuum difference beta*d0 gives the second.
If |mu|>=1/4, ell>=1/16. Otherwise r<1/16 and
|d0|=(7-13*r)/48>33/256, hence ell>99/1024>1/16.
Thus ell>=1/16 for EVERY Boolean core mean (in fact every real mean in[-1,1]).

Pinsker in bits gives Rco>=ell^2/(2*ln2)>1/512. For completeness, coarsen
Pco,Qco to the set where Pco>=Qco using log-sum; the binary probability
difference is ell/2. For fixed binary q, the binary KL as a function of p
has second derivative 1/[ln2*p*(1-p)]>=4/ln2 and has value and first
derivative0 at p=q. Integration gives D>=2*(p-q)^2/ln2. Endpoint cases
follow by continuity or infinite KL. Finally ln2<1, for example by integrating
1/x<1 on (1,2). This proves the asserted strict constant without a
numerical approximation or an unproved estimate.

The signed profile matters: scalar occupancy alone is ZERO at r=7/13,
where d0=0. The uniform bound still holds from the nonzero signed mean.
The lemma is a probability calculation on this actual Boolean mask, not
a Booleanity test excluding every non-Boolean normalized vector.

## Third prescribed change and complete same-account history

Let L3 be the CURRENT conditional nonempty core-frequency law obtained by
marginalizing N over j and normalizing away its mass t at {j}:

    L3(T)=[N(T)+N(T+{j})]/(1-t), T nonempty in x.

Choose ANY normalized nonempty core-frequency target S3, separately in
each of the four signed j-children if desired. Prescribe

    T3=(511/512)L3+(1/512)S3.

The fresh COMPLETE reference matches every true signed vacuum atom
(A_U0+sigma*v*B_U0)^2 and assigns B_U0^2*(1-r)*T3(T) to each nonempty
core frequency. Every old positive tail atom survives through the511/512
floor. Calibration first reduces CE by Rco. The subsequent mixture costs
at most beta*(1-r)*log2(512/511)<3/2048, since
512^256<2*511^256. Consequently the fresh-reference change at EVERY
j-child is <-1/2048. Adding the physical j erasure changes the bound only
by subtracting the nonnegative conditional occupancy KL of the current
reference. The complete j-query plus both mean terminal CEs is therefore
<-1/2048 at EACH of the two signed nonconstant i-parents.

If k is constant (r=1), the terminal tail mass is0 and the actual vacuum
law is used; no conditional actual tail is formed. L3 itself is still
well-defined because the chosen U is positive away from j and t<=7/8.
If k is nonconstant, all statements above concern a genuine changed
conditional nonempty profile whenever S3 differs from L3. A reference-only
atom may be removed when its entire actual sector is0; that removal is the
explicit calibration whose complete CE change is included. There is no
division by0 and no missing terminal.

The whole finite tree retains two constant i-terminals and four +/-k
terminals, with their actual reach weights1/4 and1/8 respectively. Earlier
controller/source debits and all three complete transactions are retained.
Their increments telescope in CE and physical erasure at the SAME incoming
source account, leaving strictly more than

    1/64 + 1/10 + 1/4096

of new release relative to its supplied incoming CE. Here the last term
uses the total1/2 probability of reaching the nonconstant i-branch. No
ancestor reserve is renewed, and subsequent ordinary no-reset queries
are paid only by the usual current-reference CE chain.

## Exact first unsupported line

The source CE for arbitrary k has not been bounded by an absolute constant
times the original physical influence. The construction still retains the
arbitrary core: I(h)=1+I(k)/2 and H(h)=2+H(k)/2, so
I(F)=5/2+3*I(k)/16 and H(F)=23/4-(9/16)log2(3)+3*H(k)/16.
Derivation: Inf_i(h)=Inf_j(h)=1/2, remaining influences halve, and the
displayed four-block seed spectrum gives H(h). The earlier wrapper
identities then give the stated F formulas. Thus proving universal FEI by
asserting an initial price for this family would already require control
of H(k). Neither the fixed refunds nor the three chosen target mixtures
settle arbitrary future histories or full FEI. Universal C018/C019/C020/C024
remain OPEN. Independent external review of this new proof is pending;
finite exact certificates validate its stated finite domain, not its
all-dimensional quantifier.
