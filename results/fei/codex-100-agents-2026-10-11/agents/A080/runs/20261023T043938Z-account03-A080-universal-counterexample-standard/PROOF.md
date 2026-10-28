# Full physical stopping credit, supplied accounts, and disjoint products

All entropy is in bits, inputs uniform, and functions take values in {-1,+1}.
Let S_K(f)=K I(f)-H(f). Numerical claims below require the exact saved
certificate; floating discovery is not a premise. Full FEI remains OPEN.

## 1. Independent finite spectrum

Let g be negative on {0,1,2} in six bits and h negative on
{0,1,2,4,8,16,32,6,17,40}. Set J(x)=-h(x xor1) and
F=J(-1,+1,g,g,g,g). Its four-input outer truth table is
K(z)=-h(4z), z in F_2^4. No physical coordinate is shared between cores.

For a core restriction g_i let mu_i=E g_i, v_i=1-mu_i^2,
and a_{i,A} its uniform Fourier coefficients. If W_T are the ordinary
Fourier coefficients of K, the coefficient with nonempty core-support B is

    L_B product_{i in B} a_{i,A_i},
    L_B=sum_{T superset B} W_T product_{i in T\B} mu_i.

This follows by substituting each core Fourier series into K's multilinear
expansion, so it is an actual Boolean spectrum, including B=empty. Its
occupied-block mass is P_B=L_B^2 product_{i in B}v_i. Pivotal probability
q_i is computed independently by summing product input probabilities over
outer edges where K changes. Orthogonality gives sum_{B contains i}P_B=q_i v_i.
Consequently

    I(F_restricted)=sum_i q_i I(g_i),
    H(F_restricted)=H(P)+sum_i q_i[H(g_i)-h2(v_i)].

This includes deterministic faces by continuity/direct substitution; their
physical influence and nonempty spectrum vanish. The certificate verifies
both the outer occupied masses and independent pivotal probabilities exactly.
It also compares explicit nonempty atom multiplicities with the displayed
entropy formula in the pilot and selected full-block cases.

Deleting a coordinate on which a truth table is pointwise independent leaves
12 profiles: P=+1, A_m negative just at0 (0<=m<=5), and L_m negative at
{0,1,2} (2<=m<=6). For A_m the single representative query yields A_{m-1},P.
For L_m, a special-bit query yields A_{m-2},A_{m-1}, and a tail-bit query
yields L_{m-1},P. Every one of729 labelled restrictions and1458 physical rows
is checked against these rows, including deleted dummy coordinates and both
answer orders. Thus the full four-core physical DAG is exactly the 12^4
profile product. It is not an extrapolation to a higher-dimensional family.

## 2. Exact logarithmic enclosure

For 0<=z<=1/3 use ln((1+z)/(1-z))=2 sum_{j>=0}z^{2j+1}/(2j+1).
After48 terms the positive tail is at most
2 z^97/[97(1-z^2)] <=3^-96. Integer interval multiplication and division
at grid2^192 enclose every partial power and term. Apply the same series
to ln2. For any rational x>0, write x=2^k y, 1<=y<2, and use
z=(y-1)/(y+1). Positive division by the enclosed ln2 gives an outward
interval for log2 x; powers of two are exact. Rational multiplication and
outward rounding then enclose -x log2 x. There are no floating sign decisions.

## 3. Full physical stopping envelope

For any finite allowed-query DAG, its exact least nonnegative credit is

    R(v)=max(0,-S(v),max_query average_b R(v_b)).

Necessity follows by stopping immediately or conserving mean credit after a
query. Sufficiency follows by induction: with supplied a>=R(v), give child b
credit a_b=R(v_b)+a-average R(v_b). Then a_b>=R(v_b), average a_b=a,
and d_b=S(v_b)+a_b>=0. In particular the hull also equals the largest expected
negative terminal slack over stopping policies; a finite maximizing policy
attains the Bellman choices. This reconstructs the scalar source theorem.

The saved rational upper envelope rho uses the rounded upper Bellman values
at every nonroot state and the exact real -S(F) at the root. At nonroot
states, rho>=(-S)_+ and rho>=average child rho follow from integer inequalities.
At the root the certificate must prove every mean child rho strictly below
the lower bound for -S(F). Stopping proves the matching lower bound, so

    R(F)=-S_4(F),

with queries allowed on ALL FOUR remaining physical cores in any adaptive
order, with arbitrary stopping. This is stronger than the source's restriction
to at most two cores; it is conditional on the supplied initial credit.

## 4. Compatibility with actual previous two-core allocations

For each of the six pairs P, independently recompute its restricted hull R_P
on144 states, holding the other two cores intact. Starting with a_root=-S(F),
the SOURCE allocation, rather than a new optimization, is

    a_child=R_P(child)+a_parent-average R_P(children).

Propagate a lower interval bound for the minimum possible credit at each
state over every path in that pair DAG. This is valid because the update
has coefficient1 on the parent credit. For a candidate path, round lower
R_child minus upper mean R_children; take the minimum over incoming paths.
The final test compares that lower bound with the full four-core rho.
It must succeed at every tested nonroot state. A root equality is proved
separately by the strict root-continuation test, never by interval overlap.

This proves an actual inherited two-core account can switch to the full
four-core envelope without new donor flow. Raising the initial supplied
credit by any real D>=0 shifts every descendant credit by D, so all old
nonnegative total debits are covered. No arbitrary past allocator is assumed
anticipatory. Independent comparison with A084's unchanged exact prime-log
S/R and saved allocation rows supplies only the scope stated in REVIEW.json.

For completeness retain signed booked labels. Write e=average S_child-S,
T=D+e=average d_child>=0. If T>0, transport each old label and the signed new
label e using the common kernel d_child/T, of mean1. Their sum is exactly
d_child. If T=0, nonnegativity forces both d_child=0 and kernel1 conserves
all labels, whose sum is zero. Original credit-owner labels use a_child/a
when a>0; if a=0 every child credit is zero. The previously spent donor and
its booked balance, stopped siblings, and parked reserves stay fixed.

## 5. Tensorization without a counterexample amplification claim

For ANY disjoint uniform Boolean factors f_i and any fixed rate K,

    R_K(product_i f_i) <= sum_i R_K(f_i).

Indeed H and I add for disjoint sign products, hence S adds at every physical
restriction. The sum of the individual nonnegative superharmonic hulls
dominates (-sum S_i)_+ and is superharmonic under every physical query, even
if the chosen factor depends on all previous answers. It is an admissible
whole-product envelope. If each S_i<=0 and R_K(f_i)=-S_i, stopping at the
product root gives equality. In particular for every integer t>=1,

    R_4(F^{tensor t})=t[-S_4(F)],
    H(F^{tensor t})/I(F^{tensor t})=H(F)/I(F)<infinity.

Thus all adaptive physical interleavings of any number of copies are paid
from their ORIGINAL additive supplied credits. Their negative rate4 slack
does not grow into an unbounded FEI ratio. Fresh point activation of these
products remains bounded by A080's preceding uniform bound
max{H(F)/I(F),4+5/k}; that earlier theorem is context, not a premise of the
new stopping certificate. Shared-coordinate products are excluded: e.g.
g(x)^2=1 has I=0 and would invalidate tensor influence additivity.

## 6. Honest universal boundary

The finite certificate and its tensorization derive no credit from a
dimension-independent influence resource for arbitrary Boolean seeds.
The first unsupported line is an inequality bounding the full physical
stopping hull by such a resource, or an actual Boolean seed sequence with
unbounded ordinary H/I. Supplied initial negative slack cannot be renamed
a free initial bank. The next useful admission must change the arbitrary
seed profile or initial supplier while retaining the original spent donor,
old signed labels and both complete terminal functions. Repeating a third
or fourth query in this now-certified fixed fixture would not address that
unpaid universal line.
