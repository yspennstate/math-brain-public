# Correlated summaries retain an outer-row entropy bill

A summary cannot pay for an arbitrary retained outer seed. The correct bound
keeps that seed's row entropy with coefficient one and charges a separate
state dictionary. No independence of summary outputs is required. Full FEI
and initial payment from the original influence account remain OPEN.

## 1. The failed statement and the exact Boolean witness

The strategy-level statement is

    H(F) <= C sum_j I(E_j)

for an absolute C, when E is an optimally encoded decodable summary of the
entire fresh block. This is a proposed shortcut tested by A092, not a claim
attributed to an agent. A092-EXACT-ORIGINAL-INFLUENCE-AND-SUMMARY-ONLY-NOGO@1
gives a literal counterfamily. Take g on two bits negative only at 00. For
k>=2 set N=k+2 and F_k(x,z)=g(x)(-1)^[|x|+|z|<=1]. Then

    I(F_k)=1+(k^2-k+2)2^(-k-1),
    inf_E sum_j I(E_j)=k^2 2^(1-k),
    H(F_k)>1 for k>=32,        H(F_k)->2.

The infimum permits any finite number of Boolean summary outputs, including
encodings splitting a residual-row class. Thus H(F_k) divided by that
summary influence diverges, while H(F_k)/I(F_k)->2. This does not refute FEI.

There are exactly three residual rows on x, indexed by |z|=0, |z|=1 and
|z|>=2. Any decodable code must change at least one output on a physical
edge crossing distinct rows. There are k edges from weight zero to one and
k(k-1) from weight one to two. Their sum, divided by 2^(k-1), is the stated
lower bound. The chain code 00,10,11 attains it, with constant extra outputs
if desired; one output cannot encode three rows. Distinctness follows by
testing x=0 and a weight-one x, irrespective of the seed's signs.

For an arbitrary n-bit seed the exact influence identity is

    I(F)=I(g)+2^(1-n-k)[(n+k)(n+k-1)-2k D0-2 D1],
    D0=sum_i 1[g(0)!=g(e_i)],
    D1=sum_(i!=j) 1[g(e_j)!=g(e_i+e_j)].

On an old-coordinate edge the seed derivative toggles precisely when the
remaining bits have weight one. Each toggle changes an indicator d to 1-d.
Fresh weight one contributes k copies of each d_i(0); old weight one
contributes the ordered D1 terms. Each undirected edge has mass 2^(1-N).
Fresh coordinates have exactly N-1 pivotal edges each. Summing gives the
formula, including constants and dummy seed coordinates. In the two-bit
witness D0=2,D1=0,I(g)=1, yielding the displayed specialization.

The edit density is epsilon=(N+1)2^-N. Parseval and Cauchy-Schwarz give
total variation d<=2 sqrt(epsilon) between the complete squared Fourier laws.
Finite coupling gives |H(F)-H(g)|<=h2(d)+Nd. Since N+1<=2^(N/2) for N>=6,
d<=delta=2^(1-N/4); for N>=34 the entropy error is below 2Ndelta<1.
The last strict inequality follows at N=34 from (4N)^4<2^N; the successive
fourth-power ratio is ((N+1)/N)^4/2<1, using 35^4<2*34^4. Fixed-seed
entropy convergence follows from Ndelta->0. The same edits change total
influence by at most 2N epsilon, proving its convergence. No growing sum is
interchanged with a limit. These derivations independently accept A092's
statement unchanged, rather than modifying its source version.

## 2. A normalized reference for any correlated finite summary

Let x in {0,1}^n and z in {0,1}^k be independent uniform physical blocks.
Let S(z) take r active states, each of probability p_s>0. Write

    F(x,z)=h_(S(z))(x),   h_s in {-1,+1},
    b_s(z)=1[S(z)=s],     e_s=b_s/sqrt(p_s).

The e_s are orthonormal real functions on the physical z cube because their
supports are disjoint; they need not be Boolean. Define their complete
squared-Fourier entropy by E_s=H(e_s). This is the entropy of a normalized
probability law. In particular it is not H of a summary output or the input
entropy of S. Denote the latter by H(p).

Let a_s(A)=hhat_s(A), and v_s(B)=bhat_s(B). Fourier inversion gives

    Fhat(A,B)=sum_s a_s(A) v_s(B).

Disjoint physical supports and Parseval give the exact old spectral marginal

    m_A=sum_B Fhat(A,B)^2=sum_s p_s a_s(A)^2.

The joint mixture reference

    Q(A,B)=sum_s a_s(A)^2 v_s(B)^2

is normalized: its sum is sum_s p_s=1 and its A marginal is m_A. In a row
with m_A>0 define w_s(A)=p_s a_s(A)^2/m_A and
q_A(B)=Q(A,B)/m_A. Then q_A is the mixture of the normalized e_s spectral
laws with weights w_s(A). If r_A counts nonzero a_s(A), Cauchy-Schwarz gives

    P_A(B)=Fhat(A,B)^2/m_A <= r_A q_A(B) <= r q_A(B).

This is an amplitude estimate proved from the sum, not a product of
conditional-probability estimates. Rows with m_A=0 are omitted; all their
full coefficients vanish. When q_A(B)=0, P_A(B)=0 too.

For normalized finite laws P<=r q, nonnegative relative entropy gives
H(P)<=sum P log2(1/q)<=r H(q), since q<=1. Zero masses are interpreted by
continuity. Consequently the stronger conditional reference bound is

    H(F) <= H(m)+sum_A m_A r_A H(q_A)
          <= H(m)+r sum_A m_A H(q_A).                    (1)

The first inequality retains the actual row rank; it is often stronger than
the uniform-r simplification. All conditional sums are finite.

## 3. The retained-row source bound, with a sharp seed coefficient

Introduce a classical joint law on (s,A) with mass p_s a_s(A)^2. Let
T=H(s|A) under this law, and R=sum_s p_s H(h_s). Then

    H(m)=H(p)+R-T,       0<=T<=H(p),
    sum_A m_A H(q_A) <= T+sum_s p_s E_s.

The second statement is just mixture entropy bounded by the entropy before
discarding its mixture label. Substituting into (1) proves

    H(F) <= R+H(p)+(r-1)T+r sum_s p_s E_s
          <= R+r H(p)+r sum_s p_s E_s.                 (2)

This is the repaired source inequality. The retained outer-row entropy R
has coefficient ONE. The state dictionary and interference cost remain
explicit. No product law for Boolean summary bits is used. For r=1 the
indicator is constant and (2) reduces to H(F)=H(h_1); k=0 and n=0 are also
covered with their evident single-atom spectra. No universal optimality of
the factors r is asserted.

The empty Fourier coefficient of e_s has squared mass p_s. The remaining
mass is 1-p_s on at most 2^k-1 atoms, so

    E_s <= h2(p_s)+(1-p_s)k.

If one state has probability 1-epsilon, then

    sum_s p_s E_s <= H(p)+k(1-sum_s p_s^2)
                  <= H(p)+2k epsilon.

Here h2(p_s)<=H(p), since knowing S determines the event S=s; averaging
these inequalities proves the first entropy term. The collision bound uses
sum_s p_s^2>=(1-epsilon)^2. Thus an explicit concentration version is

    H(F) <= R+2r H(p)+2rk epsilon,                     (3)
    H(p)<=h2(epsilon)+epsilon log2(r-1)  (r>=2).

For the A092 three-state family, epsilon=(k+1)2^-k and r=3. Its dictionary
overhead in (3) is at most 6[h2(epsilon)+epsilon]+6k epsilon, which tends
to zero. Its dominant row is g. The other two rows are fixed functions on
the same n old bits, so R->H(g). Section 1 gives H(F)->H(g) as well.
Taking the seed with H(g)=2 proves that coefficient one on R cannot be
replaced by any smaller absolute coefficient while retaining the overhead
in (2) or (3). A dimension-independent multiple of that overhead would
still tend to zero and cannot change this sharpness conclusion.

This is a nontrivial repair of summary-only payment: it retains exactly the
arbitrary seed entropy the summary misses, rather than putting a factor r
on it. It does not price that retained entropy from original influence.

## 4. The exact physical influence ledger and a useful conditional supplier

Let d_st=Pr_x[h_s(x)!=h_t(x)]. Conditioning on z gives exactly

    I_x(F)=sum_s p_s I(h_s).

For each undirected physical z edge (z,z'), conditional disagreement is
d_(S(z),S(z')). Hence

    I_z(F)=2^(1-k) sum_(z,z' physical undirected edge) d_(S(z),S(z')). (4)

This formula uses the actual correlated state transition, including
simultaneous output flips and their cancellation. Arbitrary codes of the
states leave it unchanged. A sum of independent scalar activities need not
equal it. Disjoint physical coordinates give I(F)=I_x(F)+I_z(F).

If row suppliers H(h_s)<=C I(h_s) are actually available at one fixed rate,
(2) yields the conditional complete source

    H(F)<=C I_x(F)+r H(p)+r sum_s p_s E_s.              (5)

This is useful for a correlated-output source interface without charging
the retained rows more than once. It is a static source inequality, not a
stopping-tree payment theorem or permission to recharge prior donors. To
convert (5) into FEI one must pay its dictionary term from unused original
capacity, possibly using cancellation in (4), AND supply the row sources
without circularly assuming FEI for arbitrary h_s. The A092 family retains
an arbitrary g with order-one original influence and near-zero summary
influence, so that row supplier is still a universal unpaid obligation.

## 5. Verification scope

The original frozen domain planned 9280 circuits; its main run stopped at the
55-second runtime guard and is INCOMPLETE, not an accepted finite certificate.
Its source and failure receipt are preserved. A revised spec freezes all 81
three-state maps with eight selected one-bit row dictionaries and 64 selected
two-bit dictionaries at the weight-state map, for 712 circuits. The revised
main passes 19494 exact predicates, including 712 runtime guards, plus 56
source cases; the separate direct-integer verifier checks 32 cases. Constants,
unused states, repeated rows and dummies occur. These are specified finite
subdomains, not all functions at larger dimensions. General normalized
references and the sharp coefficient are proved in sections 2-4; the finite
checks validate their formulas and implementation. Formal work is held by
memok exit1; no compiler was launched and no Lean certificate is claimed.
Independent review of the new static source proof and full FEI remain open.
