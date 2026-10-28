# Conditional reference normalization changes the target weight

Bits throughout. Actual functions are Boolean signs on finite uniform cubes.
References are complete subprobabilities of mass s in (0,1], positive on
actual support; their CE retains the penalty -log2(s). Author result is
pending independent review. Full FEI remains OPEN. The mixture formula is ordinary Bayes normalization; the campaign contribution is its precise source-policy application and Boolean failure certificate, not a claim of literature priority.

## 1. Independently reviewed inputs and precise scope

A001's one-frontier quarter-profile tariff is correct at its stated
conditional scope. Preserve the current reference mass s and empty mass,
and replace its nonempty part Q+ by (3/4)Q+ +(1/4)t_Q T, t_Q=s-Q(0).
The full reference still has mass s. Only actual nonempty mass is charged,
so signed CE increase <=Var(f) log2(4/3). A constant terminal retains its
old -log2 Q(0); t_Q=0 forces zero actual tail and gives the identity.
For any adaptive frontier, total reached variance <=root variance by
E(E[f|history]^2)>=(Ef)^2. For A001's point edit, mean perturbation has
size2delta, hence Var(F)<=Var(g)+4delta<=I_g+4delta. The nontrivial a-cube
edge boundary gives I_g>=2a2^-a; for a>=2 and q=b+r>=3,
4delta/I_g<=2/(a2^q)<=1/8. At a=1 use Var(F)<=1=I_g.
For clarity, the boundary fact follows by induction on cube sections: two nonconstant sections contribute at least2(a-1)>=a internal edges; one nonconstant section contributes a-1 internal edges and at least one crossing edge; opposite constant sections contribute2^(a-1)>=a. Base a1 is direct. No relevance assumption is needed.
Thus Var(F)<=9I_g/8. Integer 4^12<2^5 3^12 gives log2(4/3)<5/12.
The ONE-frontier tariff is <15I_g/32 and a SUPPLIED original reserve
>=7I_g/8 leaves >13I_g/32. This does not certify A094's upstream chain
independently, renew the source, or fund every later conversion.

A001's SOURCE(C) audit is also correct at IDENTICAL constants:
CE(P,R)=H(P)+D(P||R/s)-log2(s)>=H(P); conversely use R=P under FEI(C).
Constants have H=I=0 and their exact point source. Existential references
without an additional construction restriction therefore do not weaken FEI.

A003's deferral/compression distinction reconstructs coefficientwise.
Replace each core input by a parity block of length L, retaining at least
one coordinate per block. Squared Fourier coefficients and H are exactly
those of the core under injective support relabeling. Each remaining bit
in block j has influence alpha_j. Before a block collapses, each query
has B=JS=occupancy KL=0 and both full inherited matched references stay
exact. At every adaptive frontier J_F=E sum ell_j alpha_j, erasure-payment
residual K L I_g-H_g is unchanged; a DIFFERENT invoice earmarking K Inf
per query leaves K J_F-H_g. At full unwrapping the latter is K I_g-H_g.
Unconditional cheap admission follows from H_g<=n, I_g>=2^(1-n), and
L>=max(2,ceil(n2^(n-1)/K)); no FEI is used. Demanding nonnegative current-
influence residual for all such cores is exactly FEI(K). The fractional
version H<=K I+lambda H, lambda<1, has exact constant K/(1-lambda), with
no 2/ln2 term along this zero-JS history. These reviews supply no repair
and make no claim of new parity-lifting identities.

## 2. Exact actual inheritance, including true-zero fibers

For a physical query i let p be its actual parent spectral law,
p_b the two actual restricted laws, m=M_i p=(p_0+p_1)/2. For ANY current
reference q of mass s define a POSITIVE LINEAR raw map T_b(q):

    raw_b(t)=(M_i q)(t) p_b(t)/m(t), if m(t)>0;
    raw_b(t)=(M_i q)(t),                  if m(t)=0.

The second line is the fair posterior allocation on true-zero fibers.
It keeps all reference-only mass; it is not silently discarded. Let
Z_b=sum raw_b. Finite support gives Z_b>0, and Z_0+Z_1=2s. The inherited
child reference q_b=s raw_b/Z_b again has the ORIGINAL mass s.

With D(p||q)=CE(p,q)-H(p), including subprobability mass penalties, direct
substitution on occupied child labels gives

    mean D(p_b||q_b)=D(m||M_i q)+mean log2(Z_b/s).

Consequently the exact FULL-entropy ledger increment is

    DeltaH_i+mean CE(p_b,q_b)-CE(p,q)
      =-rho+mean log2(Z_b/s)<=0,                           (1)
    rho=D(p||q)-D(m||M_i q)>=0.

The last sign uses conditional KL and Jensen with mean Z_b=s. This is the
FULL entropy decrement DeltaH=H(parent)-mean H(child), not B alone;
DeltaH=B+JS. Reference normalizers and the true-zero mass are essential.
This reconstructs A094's inheritance interface locally, not its other
point-edit price bounds. Any finite adaptive continuation using ONLY this
inheritance is paid by its incoming complete CE, with all physical reaches
and both terminals, even when its mixture weights change.

## 3. New mixture transport formula and the unpaid policy condition

Let q^0,q^1 have the SAME mass s and finite CE. At the parent put
q^lambda=(1-lambda)q^0+lambda q^1, 0<lambda<1. True-vacuum equality at
this initial node is permitted but not required for this formula. Because
the raw maps above are linear, the EXACT normalized child law is

    (q^lambda)_b=(1-lambda_b)(q^0)_b+lambda_b(q^1)_b,
    lambda_b=lambda Z_b^1/[(1-lambda)Z_b^0+lambda Z_b^1].   (2)

In particular the full child dominates lambda_b times the target child.
The stronger fixed component guarantee lambda_b>=lambda holds if and only
if Z_b^1>=Z_b^0. It cannot be assumed merely because total masses and parent
vacua agree. A smaller lambda_b does not by itself force a pointwise floor
failure if the old component covers the same atoms; section4 gives a true
pointwise counterexample, not just a weight change.

For an adaptive history v chosen on the ACTUAL physical outcomes, let
L_k(v)=product over its edges of Z_edge^k/s for k=0,1. Recursively applying
(2),

    lambda_v=lambda L_1(v)/[(1-lambda)L_0(v)+lambda L_1(v)]. (3)

Thus a target-policy admission demanding component floor c at EVERY node
needs the explicit likelihood-ratio corridor

    L_1(v)/L_0(v)>=c(1-lambda)/[lambda(1-c)].              (4)

This is the exact condition for the component-weight guarantee; it is
sufficient, but not necessary, for a pointwise floor because the old
component can provide additional overlap. With c=lambda=1/4, it is L1>=L0.
At a ONE-step query, both children cannot have strict Z^1>Z^0 since each
pair of Z's sums to2s; both weights can stay >=lambda only if both equal.
No claim that every full pointwise floor must fail follows from this fact.

The distinction resolves the handoff: ordinary inherited continuation is
paid by(1); a later theorem requiring the SAME fixed target floor or exact
target model needs(4), extra overlap, or an ACTUALLY priced repair. A001's
root tariff does not by itself provide that corridor. No FEI contradiction
or refutation of A001's one-frontier statement is asserted.

## 4. Actual Boolean finite counterexample to fixed-floor inheritance

Take f=+1 only at truth index0 on three bits and -1 elsewhere (bit0 fastest).
Its spectrum is p(0)=9/16 and p(t)=1/16 for t=1,...,7. Query physical bit0.
The bit0=0 child has all four spectral probabilities1/4; bit0=1 is constant.
Supply two NORMALIZED, everywhere positive references with identical
parent vacuum9/16:

    256 q^0=(144,1,1,1,106,1,1,1),
    256 q^1=(144,80,15,13,1,1,1,1),
    lambda=1/4.

The parent mixture has EXACTLY the original mass/vacuum and is the actual
quarter-tail mixture toward the normalized tail of q^1. On the nonconstant
physical child, the raw normalizers are

    Z^0=35/32, Z^1=3/5, Z^lambda=621/640,
    lambda_child=32/207<1/4.

At its remaining frequency mask1, exact normalized child references obey

    q^lambda_child(1)=85/1242 < (1/4)q^1_child(1)=35/384,
    q^lambda_child(1)/q^1_child(1)=272/1449<1/4.           (5)

After normalizing each nonempty tail separately, this atom has mass34/365 in the mixture tail and7/8 in the target tail: their ratio272/2555 is also below1/4. Calibrating both vacua to the true child vacuum1/4 preserves that conditional ratio and therefore does not repair the lost shape floor. The atom has ACTUAL probability1/4. All denominators and all actual CE are
finite. Both complete physical children, including the constant child,
are retained in the exact(1) test. The full budget contracts even though
the advertised target floor fails. This refutes only the tempting NEW
universal inference 'a quarter target floor survives mass-preserving
normalized physical inheritance'; that inference is NOT an A001 claim.

## 5. Units, endpoints and exact remaining universal line

For f a sign, p=hat f^2 is a probability; I_i=P(i in S), I=sum I_i.
For indicator (1+f)/2 the nonempty squared coefficients are p/4, while its
flip probability is still I_i. Nonempty unnormalized entropy excludes only
the vacuum term; it is not conditional entropy divided by Var(f).
Natural-log costs multiply all information quantities, including the
subprobability mass penalty, by ln2. Directional half-edge counts must not
replace the full flip probability. The checker includes constants,
dictators, parity, nearly constant functions, sparse spectral supports,
reference-only fibers, and mass1/2 so the mass penalty is not invisible.

This stage's new all-dimensional statement is the exact normalizer-aware
mixture law(2)--(4), with a Boolean counterexample(5) to a stronger handoff.
It does not supply a reference of cost O(I) for arbitrary roots, a
contraction coefficient below1 on core entropy, or a universal floor-
compatible policy. Those are the first unsupported lines. NEXT should
prove a required policy accepts the changing likelihood floor or pays its
repair from the already diminished owner, while demanding a noncircular
source estimate; repeated zero-cost deferral cannot compress that source.
