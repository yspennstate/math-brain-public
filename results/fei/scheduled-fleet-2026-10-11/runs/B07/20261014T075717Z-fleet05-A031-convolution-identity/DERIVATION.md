# Signed union-containment trace on a genuine overlap cycle

All signs are Boolean on finite uniform cubes. Entropy and KL are in bits.
M denotes oriented erasure, NOT marginal entropy or spectral-sector MI.
For a physical coordinate i, e_i=Inf_i, mu_i(T)=p_(T+i)/e_i,
r_i(T)=p_T+p_(T+i), and M_i=e_i[log2(1/e_i)-D(mu_i||r_i)].
Both row laws normalize to one; constant/irrelevant rows have M_i=0.

## 1. Signed admission before the cost is squared

Let E1=X1 union{a,c}, E2=X2 union{a,b}, E3=X3 union{b,c}, where
X1,X2,X3 are disjoint private blocks, r_j=|Xj|>=1. Put A_E=1_(x_E=0)
and f=2 product_(j=1..3)(1-A_Ej)-1. No coordinate belongs to all clauses.
For J subset{1,2,3}, U_J=union_(j in J)Ej. Expansion is SIGNED:

 a_S=2 sum_(J subset{1,2,3}) (-1)^|J| 2^-|U_J| 1_(S subset U_J)
       -1_(S=empty).                                           (1)

The empty union is retained. Terms can cancel and are added before any
absolute value or square; replacing this with unsigned witness counts is
not licensed. The pointwise sign f^2=1 implies every signed convolution
sum_S a_S a_(S xor V)=1_(V=empty), not only a fixed prefix.

More generally (1) holds for ANY finite family of zero-point clauses.
This elementary inclusion-exclusion is not claimed novel; its use here
is to certify the ENTIRE normalized conditional-edge likelihood trace.

## 2. A structural lossless trace and its exact masses

Define paired union-containment signatures
C_i(T)=( {J:T subset U_J}, {J:T+i subset U_J} ).
By (1), both a_T and a_(T+i) are fixed by C_i, including their signs.
Therefore mu_i(T)/r_i(T) is constant on every occupied trace cell, and

 D(mu_i||r_i)=D(mu_(C_i)||r_(C_i)).                              (2)

The generic KL equality criterion is not Boolean-specific; its STRUCTURAL
admission by the signed actual function is. For this triangle a convenient
refinement records which of the three retained private blocks are hit and
the retained shared frequency mask. It has at most64 states for a private
query and32 for a shared query, independently of all r_j. A private-hit
state has exact multiplicity product_(j hit)(2^r'_j-1), where r'_j is the
remaining private width after deleting the queried coordinate. In each
cell let signed lower/upper amplitudes be u_z,v_z and multiplicity n_z.
Then mu_z=n_z v_z^2/e_i, r_z=n_z(u_z^2+v_z^2). Every cell, including those
with mu_z=0 but r_z>0, remains in the complete reference.
One global pair P(i,z)=(e_i/I)mu_z,Q(i,z)=(e_i/I)r_z has total mass1
and identical physical coordinate marginals. Thus this quotient spends
one original influence ledger, never a full I per state or width.

## 3. A tempting smaller clause-hit trace really loses refund

For r1=r2=r3=1, query shared a. Two retained rows have the SAME set of
clauses they intersect: T1={b,c}, T2=X1 union X2 union X3, both hit all3.
Signed expansion gives (a_T1,a_(T1+a))=(-3/32,5/32),
(a_T2,a_(T2+a))=(-1/32,-1/32), while e_a=11/32.
Hence their upper-sector fractions are25/34 and1/2, and their mu/r ratios
are25/(34e_a) and1/(2e_a), UNEQUAL. Both derivative masses are positive.
Strict KL equality characterization proves the clause-hit quotient drops
positive conditional refund. The exact complete lost divergence is also
certified by rational-log intervals in out/CERTIFICATES.json.
This settles failure of the proposed cheaper trace, not failure of FEI.

## 4. A single private influence reserve pays this collision fixture

Write q_j=2^-r_j. For private i in Xj its physical derivative is a point
indicator on the other r_j-1 private bits times a residual Boolean-valued
0,+1,-1 function. Its support density in the remaining variables is

 gamma_j=[1+(1-q_k)(1-q_l)]/8 in[1/8,1/4],
 e_i=alpha_j gamma_j, alpha_j=2^-(r_j-1)=2q_j.                   (3)

The derivative's Fourier law is uniform on those retained private labels,
tensored with its residual normalized law. Thus it gives mass1-alpha_j
to rows hitting the retained queried private block. On those rows the
paired containments agree, u=v, so the oriented log ratio is exactly1.
All remaining rows satisfy log2(r/p_upper)<=log2(1/e_i). Consequently

 M_i/e_i <=1-alpha_j+alpha_j log2(1/e_i)
          <=1+alpha_j(r_j+1)<=3.                              (4)

The last uses (r+1)/2^(r-1)<=2 for all integer r>=1. This retains signed
cancellation and actual derivative support, rather than pricing states by
their count. It fails for a norm-one Bernoulli(1/16) product spectral law,
whose per-coordinate M_i/e_i=4.

Let I_priv=sum_j r_j e_(private j). A shared coordinate incident to clauses
j,k has e_shared<=(q_j+q_k)/2. The exact physical value is
(q_j+q_k)/2 -q_j q_k/4 -q_l(q_j+q_k-q_j q_k)/4.
Use M_i<=B_i<=h2(e_i)<=e_i log2(euler/e_i).
The last scalar function is increasing on[0,1] and subadditive, so summing
the three shared coordinates yields

 M_shared <=sum_j q_j(r_j+1+log2(euler))
           <=(2+log2(euler))sum_j r_j q_j
           <=4(2+log2(euler)) I_priv.                         (5)

This is a single allocation: private rows spend at most3 I_priv, shared
rows at most4(2+log2(euler)) I_priv, on the SAME original private ledger.
Thus

 M(f)<17 I_priv(f)<=17 I(f),                                   (6)

using log2(euler)<3/2, proved by ln2>2/3. No optimality or literature-priority
claim is made for this three-clause class bound. The contribution is an
influence-paid LOSSLESS reference on a genuine overlap, not a universal
FEI constant. M<=B<=M+I/ln2 is only a routing consequence, not a new proof.

## 5. Guards and what happens to an actual restriction

The coarse-trace equality itself fails for a normalized non-Boolean vector:
at widths(2,1,1), query a, put a_(x1+a)=3/5, a_(x2)=4/5, all other
amplitudes0, where x1,x2 are the two coordinates of X1. The refined trace
merges residual rows{x1},{x2}. Full D=log2(25/9), trace D=0, and the
nonempty convolution at x1+a+x2 equals24/25, violating admission.
The bound(6) also fails for Bernoulli(1/n)^tensor n with n=2^18 and
private widths(n-5,1,1): I=1,M=18, I_priv=(n-3)/n, so M>17 I_priv.
These are normalized real controls, never Boolean FEI counterexamples.

Tensoring by ANY Boolean terminal g on fresh coordinates preserves old
row likelihoods and old local M/e; the triangle trace ignores spectator
frequencies. The complete result is M(fg)=M(f)+M(g)<17 I_priv(f)+M(g).
Terminal H(g),I(g),M(g) are not discarded or paid by the triangle reserve.
The general signed-containment interface is checked on the three-bit
point defect (one clause of width3); no vacuous conditional-product
hypothesis is used. The bound17 is specifically for the positive-private
triangle and is not extrapolated to unrelated one-clause admissions.

Any actual physical restriction of the clause formula remains a signed
zero-point clause formula after deleting satisfied literals and killing
contradicted clauses, so a fresh paired-containment trace is lossless for
the CHILD's own row pair. More strongly, the same parent-defined private
hit/shared-mask refinement remains sufficient for every child local row:
the restricted clause unions still comprise whole remaining private blocks
and shared singletons. Tests exhaust both outcomes of every single query
for two fixed roots, including children whose private width becomes zero.
This proves LOCAL child likelihood sufficiency, not inherited-reference
payment. The bound(6) required positive private widths and a lower support
density, and is not asserted for those descendants.

First unsupported universal line: transport the incoming complete reference
through an active physical query and pay both its normalizer/reset cost
and retained conditional KL from the SAME remaining private/terminal bank.
Creating a fresh sufficient child reference does not license a bank reset.
Growing clause counts can make containment traces unbounded, so a state
count alone cannot yield the universal signed-core refund either.
