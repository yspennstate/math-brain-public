# Whole-row cancellation halves the signed composition drift

A075 stage10. Entropy is in bits, all inputs are uniform physical bits. Full
FEI remains OPEN. The new universal lemma improves a conditional payment
reserve; it does not pay the initial Fourier entropy bill.

## 1. Exact target and the new cancellation

Let h be any finite Boolean gate and g_1,...,g_r arbitrary Boolean functions
on disjoint finite uniform physical cubes. Constants and dummy coordinates
are allowed. Keep this same decomposition under every restriction. Write
F=h(g_1,...,g_r), q_j for the true pivotal probability under the other
independent core outputs, and

    C=H(F)-sum_j q_j H(g_j).

For every physical coordinate i of core j, the new bound is

    mean C(F|i=b)-C(F) <= (2/ln2) Inf_i(F) <= 3 Inf_i(F),        (1)

with strict second inequality if Inf_i(F)>0. This halves A072's bound
4/ln2 and its convenient rational reserve6. The improvement uses cancellation
of the ENTIRE nonexceptional entropy decrement, including its Jensen-Shannon
part, followed by the Boolean constraint on the exceptional coefficient pair.
No bound on gate arity, number of physical bits or bias is imposed.

For real x,y define the whole entropy-row decrement

    L(x,y)=eta(x^2)+eta(y^2)
           -[eta((x+y)^2)+eta((x-y)^2)]/2,
    eta(t)=-t log2 t, eta(0)=0.

If a_L,b_L pair Fourier coefficients differing by i, direct restriction
Fourier inversion gives

    H(u)-mean H(u|i=b)=sum_L L(a_L,b_L).                      (2)

Unlike separate erasure and JS bookkeeping, this representation cancels
all nonexceptional rows in one step. Because squared masses have the same
sum on both sides, L(lambda x,lambda y)=lambda^2 L(x,y).

## 2. Elementary pointwise estimates, with no FEI premise

Put s=x^2+y^2. Then L(x,y)=Phi(x^2,y^2)+Jrow(x,y), where

    Phi(A,B)=(A+B)log2(A+B)-Alog2 A-Blog2 B,
    Jrow=eta(s)-[eta((x+y)^2)+eta((x-y)^2)]/2.

Both terms are nonnegative by the Shannon chain identity and concavity
of eta (or directly by their displayed formulas). Both are defined without
normalizing the row to probability1. We will use

    Phi(x^2,y^2) <= (2/ln2)|xy|,
    Jrow(x,y) <= (2/ln2)min(x^2,y^2).                        (3)

For the first, t-ln(1+t^2) has derivative (t-1)^2/(1+t^2)>=0 and
vanishes at0. Apply ln(1+t^2)<=t to each of the two logarithms in Phi.
For the second, when s>0 set z=2xy/s. Then
Jrow=s G(z)/ln2 with G(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2.
The functions are even, and

    G(z)<=1-sqrt(1-z^2), |z|<=1.

For0<=z<1 their derivative comparison is atanh(z)<=z/sqrt(1-z^2).
Differentiate again and use (1-z^2)^(-1)<=(1-z^2)^(-3/2), with equality
of values at0. Endpoints and s=0 follow by continuity. Multiplication by
s gives s-sqrt(s^2-4x^2y^2)=2min(x^2,y^2), proving (3).

Consequently

    0<=L(x,y)<=(2/ln2)min(|x|,|y|)(|x|+|y|).               (4)

For an actual Boolean inner function let mu=E g_j and t=ghat_j({i}).
The two conditional means are mu+t and mu-t, each in[-1,1]. Thus

    |mu|+|t|=max(|mu+t|,|mu-t|)<=1.

Also |t|<=d=Inf_i(g_j): the singleton coefficient is the signed mean
of the Boolean derivative, whose absolute mean is d. Formula (4) now gives

    L(mu,t)<=(2/ln2)min(|mu|,|t|)<=(2/ln2)d.                (5)

This combines the two formerly separately bounded terms. It does not
assume a product law for occupied Fourier subsets or any independence
between query histories.

## 3. Exact whole-row composition identity

Split h in input j as h(z)=A(z_-j)+z_j D(z_-j), with A,D the half-sum
and half-difference of its two restrictions. On the other physical cores,
F=A(g_-j)+g_j D(g_-j). Since D is0 or+/-1,

    sum_W Dhat(W)^2=E D(g_-j)^2=q_j.

For every inner remaining frequency L NOT empty after removing i, the
full coefficient pair is exactly Dhat(W) times the corresponding pair
of g_j. Homogeneity of L therefore makes the sum of ALL those full row
decrements equal to q_j times the corresponding inner sum. The only
exception is the inner empty remaining frequency: its pair in F is

    ( Ahat(W)+mu Dhat(W), t Dhat(W) ).

For k!=j the unchanged H(g_k) is weighted by q_k. This pivotal probability
is affine in the sign law of g_j; hence its mean over the physical query
children equals the parent q_k. The queried core's q_j itself is unchanged.
Subtracting the complete identities (2), without dropping any nonempty JS
row, proves the exact formula

    mean C_child-C_parent
      =q_j L(mu,t)
       -sum_W L(Ahat(W)+mu Dhat(W),t Dhat(W)).              (6)

Every term subtracted is nonnegative by (4). By (5) the right side is at
most (2/ln2)q_j d. Physical edges independently give Inf_i(F)=q_j d.
This proves (1), including q_j d=0 and constant other cores, without
division by any variance or bias. Finally
ln2=2 sum_(k>=0)(1/3)^(2k+1)/(2k+1)>2/3, so2/ln2<3.

The source A072 proof remains valid unchanged: its exact decomposition
and bound follow from (2)-(3), with its more conservative treatment of
the JS part. The new cancellation is an improvement, not a repair needed
for that source statement to hold.

More explicitly, the same nonempty-row factorization gives separately
B_i(F)=q_j[B_i(g_j)-Phi(mu^2,t^2)]+B_special and
J_i(F)=q_j[J_i(g_j)-Jrow(mu,t)]+J_special. Combining either pair of
identities recovers the source's stated exact formula
q_j[Phi(mu^2,t^2)+J_i(g_j)]-B_special-J_i(F) for the signed drift.

## 4. Improved coherent full-universe envelope

Fix ANY real K>=0. Let rho_j be the full finite physical stopping hull
of (H(g_j)-K I(g_j))_+, evaluated on every actual inner restriction. Put

    U_K=C+kappa I(F)+sum_j q_j rho_j,
    kappa=2/ln2 or the convenient rational value3.          (7)

Physical influence telescopes exactly:
I(parent)-mean I(children)=Inf_i(F). Thus (1) makes C+kappa I
superharmonic. At complete physical revelation it is0, so finite backward
induction also proves C+kappa I>=0 at every state. The sum q_j rho_j is
nonnegative and superharmonic: for the queried core q_j is unchanged and
rho_j is superharmonic; every other rho_k is unchanged and mean q_k is
conserved. Consequently U_K is nonnegative and superharmonic for every
physical query. Since rho_j>=H(g_j)-K I(g_j), the exact composition and
influence identities give

    C+sum_j q_j rho_j>=H(F)-K I(F).

Therefore U_K majorizes (H(F)-K I(F))_+. The same original decomposition
is present from the start, so mere admission of existing cores does not
change (7). Changes of decomposition still require a separate comparison.

If a>=U_K(parent) is ALREADY SUPPLIED actual credit, send

    a_b=U_K(child_b)+a-mean U_K(children).

Both children have a_b>=U_K(child_b)>=0 and mean a_b=a. Nonnegative
credit owners use the mean-one kernel a_b/a if a>0; when a=0 both
outgoing credits are0. Write d_b=K I(child_b)-H(child_b)+a_b>=0.
Old signed debit labels plus the new signed query label have total
T=mean d_b. For T>0 use their common kernel d_b/T; for T=0 both
debits vanish and kernel1 preserves cancelling signed labels. Hence
actual reaches, both full terminals, old credit owners, signed old
debits and already spent donors are retained. No fresh source is created.

For the same fixed partition and same K, the old rational6 potential
minus the new rational3 potential is EXACTLY3 I(F). If old credit was
actually supplied and still dominates the old potential at the current
history, it also dominates the new one. Switching future allocation
retains the ACTUAL arriving credit, rather than replacing the past.
This is3 I of reduced required headroom, not permission to draw a spent
owner again. The conditional mean release of the difference is3 Inf_i(F).

## 5. Exact finite audits and independent source acceptance

The frozen pilot checks64 complete two-core circuits and128 physical
query rows. The main fixed domain is every16 two-input outer gate, every16
two-bit first core, every4 one-bit second core:1024 circuits and3072 rows,
including all constants, complements and pointwise dummies. There is no
symmetry quotient. Each whole physical Fourier coefficient is recomputed
by direct characters as well as FWHT; every inverse, Parseval identity,
physical edge influence, pivotal influence factor, conditional-mean q
identity, exact (6) and rational3 drift inequality is checked. The stricter
bound (5) is checked using exact products of outward rational log intervals.
These finite checks validate implementation; Sections1-4 prove all dimensions.

An additional separately frozen actual4-bit core is+1 whenever its last bit
is0 and, when that bit is1, is negative at the first three three-bit points.
It has mu=5/8,t=d=3/8 for the last-bit query. Exactly
L(mu,t)-2d=37/16-(9/32)log2(3)-(25/32)log2(5)>0, certified by
2^74>3^9*5^25. Thus simply substituting2d in the exceptional-row estimate
would be false. This does NOT refute a possibly sharper2 Inf bound for the
FULL signed drift, which also subtracts the full exceptional rows.

A separate control uses A071's AND-of-OR(3,2,2) on7 bits and all7 physical
queries, preserving both complete children and their dummy variables. Its
first positive C drift is retained; the new3 Inf reserve pays it. Complete
per-circuit outputs and execution counts are in out/, immediately saved.
No peer executable is imported. Own prior192-bit80-term positive-atanh
log enclosure helper has a proved remainder; exact prime-log cancellation
decides identities and directed rational bounds decide strict signs.

An unchanged independent review of A072-SIGNED-COMPOSITION-DRIFT-COHERENT-
ENVELOPE@1 follows from the reconstructed complete coefficient factorization,
the source's separate estimates (3), and the envelope/owner argument above.
The source's4/ln2 and6 constants, all-real K>=0 scope, and explicit initial
price qualification remain true. No source repair or source contributor
change is needed. The improved2/ln2 and3 theorem is A075's new author result
and awaits external independent review; our own finite audit is not that review.

## 6. First unpaid universal line

For singleton physical-bit cores every rho_j=0 and C=H(F). The new
initial envelope is H(F)+kappa I(F), just as the source's larger one
was H(F)+6I(F). Thus coherence and a factor-two reserve reduction do NOT
provide a dimension-independent initial influence price. In particular
this proof does not establish FEI(K), or an actual Boolean unbounded H/I
family. The next unpaid line is to fund the INITIAL signed outer correction
and weighted inner hulls from ACTUAL unused original influence owners,
using a decomposition or invariant that cannot simply hide H(F) in C.
