# Immediate analytic result: erase the physical comb label

Uniform selectors x1,...,xa are tested in order. Stop at the first +1,
or at terminal a+1. Each leaf chooses one of two distinct nonempty
unsigned data characters chi_A, chi_B. The two supports can overlap and
each label can repeat. This is the prior A011 comb representation without
its boundary-retention admission. Let sigma_j in {+1,-1} specify the label.

Set m_(a+1)=sigma_(a+1), m_j=(sigma_j+m_(j+1))/2,
r_j=(1-sigma_j*m_(j+1))/2, and p=(1+m_1)/2, q=1-p.
All these are physical suffix probabilities, fixed before the Fourier
sample, and computable from the finite labelled tree.

For a nonempty selector set T with max(T)=j, the signed Fourier coefficient
of the selector label function is 2^(1-j) sigma_j r_j
times (-1)^(|T|-1). Thus F has empty-selector spectral masses p^2 at
data set A and q^2 at B. At each max-index j it has 2^j output atoms
(two data labels times 2^(j-1) predecessor subsets), each of mass
2^(-2j) r_j^2. Write v_j=2^(-j)r_j^2 for the total group mass.

This defines a normalized output reference directly:
Q(empty,A)=p^2, Q(empty,B)=q^2,
Q(T,A)=Q(T,B)=2^(-2 max T)r_(max T)^2 for T nonempty.
The normalization identity is p^2+q^2+sum_j v_j=1. It is an exact
Fourier-law calculation, not a free reference selected after observing T.
Equivalently choose an empty atom or max-index group with those fixed
masses; inside group j choose a data label and predecessor subset uniformly.
No physical stopping leaf is transmitted. All output preimages were
already aggregated by the signed Fourier calculation.

Physical data influence is p|A|+q|B|. Selector influence J obeys two exact
expressions:

    J=sum_j 2^(-j) r_j
     =(1/2) sum_j (j+1) v_j.

The first follows by conditioning on reaching query j; distinct characters
disagree on half the data cube. The second follows from the uniform
predecessor subsets in each group. In particular V=sum v_j=2pq<=J.

The complete output-reference expectation is exactly

    CE(P_F,Q)=L(p^2)+L(q^2)+sum_j v_j(2j+2log2(1/r_j)),

where L(t)=t log2(1/t) and zero groups are omitted. It equals H(F),
but its bounded cost is proved from the physical suffix probabilities
and exact influence identities, not assumed from FEI.

The binary quadratic correction gives L(p^2)+L(q^2)<=4pq=2V.
Also 2 sum j v_j=4J-2V. These two terms cancel their full V cost. Finally
r log2(1/r)<=log2(e)/e, so
2 sum 2^-j r_j^2 log2(1/r_j)<=2log2(e) J/e.
Therefore the entire normalized cost, including both empty selector
atoms, all group labels and predecessor subsets, is

    CE <= C_* J,   C_*=4+2log2(e)/e < 41/8.

The last rational bound uses e>8/3 and ln 2>2/3, so
log2(e)/e=1/(e ln 2)<9/16. A complete Shannon prefix code with lengths
ceil(log2(1/Q(S))) has expected length <CE+1 unless Q is a point mass
(then use the empty word). Since I_data>=1, this physical OUTPUT code
has expected length <=(41/8) I(F). It does not decode the original
physical leaf; subtracting posterior entropy from that transmitted
leaf code would be invalid.

This repairs the low-boundary comb code, not arbitrary selector trees.
The broader arbitrary-leaf transcript from stage 1 remains valid at its
original scope; this reference does not supersede its general theorem.
Literature novelty is not asserted.

Do not count this as a new FEI class or better total H/I bound: the raw
comb already has 2D<4 and I_data>=1, so its old transcript trivially
costs <=4 I(F) even without boundary admission. The gain is the full
IDEAL reference cost paid solely by I_sel, tending to zero when the
selector boundary does. This is the stronger compositional interface
needed before reusing shared data; integer output rounding is separate.

Failed cheaper repair: merely push forward the old uniform-mask Kraft
law while suppressing its physical leaf. On the terminal-only switch,
Q_raw({A})=sum_(j=1)^a 4^-j=(1-4^-a)/3 whereas the true mass is
(1-2^-a)^2. Hence its full cross-entropy is at least
(1-2^-a)^2 log2[3/(1-4^-a)], tending to log2(3), while
I_sel=a2^-a tends to zero. Passive marginalization of that old reference
does not repair its selector cost. The new output generator uses the
coherent, signed suffix probabilities squared, not the old codeword
Kraft weights. Posterior erasure of the TRUE witness law and erasure of
the uniform-Kraft reference are distinct operations.

Tensor guard: for any Boolean seed h on disjoint physical coordinates,
and any complete fixed seed reference Q_h, Q_F tensor Q_h is a complete
reference for F*h with CE=c_F+CE(P_h,Q_h), exactly. For h^t the seed cost
is t CE(P_h,Q_h) and influence is I(F)+t I(h). Erasing the comb's physical
label does not erase, bound, or normalize away that arbitrary seed cost.

Exact universal gap in the two-label selector alone: for arbitrary Boolean
g, define F_g=(1+g)chi_A/2+(1-g)chi_B/2. Write mu=Eg,
p=(1+mu)/2, q=1-p and V_g=1-mu^2. Then

    H(F_g)=L(p^2)+L(q^2)+V_g+(1/2)H_nonempty(g),
    I_sel(F_g)=I(g)/2.

The comb proof controls H_nonempty by its suffix/max-index structure.
An arbitrary selector has no proved uniform predecessor distribution
or equivalent cheap reference inside a max-index group. For balanced g,
this recovers H(F_g)=2+H(g)/2. A universal replacement at this step is
full-FEI strength; the seed entropy cannot be treated as an empty label.
