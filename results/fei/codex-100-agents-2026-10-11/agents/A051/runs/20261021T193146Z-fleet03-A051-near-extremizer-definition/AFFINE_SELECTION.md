# Affine variations of a finite critical witness

All cubes are finite and uniform. The cube is written F_2^n, Boolean outputs
are signs, entropy is in bits, and Fourier coefficients use uniform averaging.
Let S have law fhat(s)^2. Put p_i=P(S_i=1), w(v)=P(v dot S=1),
m(v)=min(w(v),1-w(v)), I=sum_i p_i and D_K=H-KI.

## 1. The admissible selector and its extra variations

Fix K>0. If a Boolean K-violation exists, choose the least essential
dimension n having one, then a D_K maximum among the finitely many n-bit
truth tables. This is the existing finite selector, not an optimizer in
unbounded dimension. Every lower-dimensional Boolean function is
nonviolating. Every same-dimensional edit is nonimproving. In particular,
every invertible affine permutation s -> M s+b of Fourier labels is an
admissible comparison: it is implemented by an invertible linear change
of input variables followed by multiplication by a character. Its Fourier
coefficients are merely permuted, so H is unchanged and Booleanity is
preserved. Maximality and K>0 therefore imply I(MS+b)>=I(S).

These maps change the physical coordinate system. Their transformed
restriction banks must not be silently identified with the old banks.
All subsequent comparisons with a physical pair refer to the ORIGINAL f.

## 2. Exact characterization of affine influence minimality

For any probability law on F_2^n the following conditions are equivalent:

(A) I(MS+b)>=I(S) for every invertible M and every b.

(B) p_i<=1/2 for every i, and, for every nonzero v,
    m(v)>=max_{i:v_i=1} p_i.

Necessity: flipping spectral coordinate i changes I by 1-2p_i, giving the
first assertion. Replace row i of the identity matrix by v with v_i=1;
this matrix is invertible. Choose its output translation so its new i-th
marginal is m(v), and leave the other rows and translations unchanged.
Its influence change is exactly m(v)-p_i. This proves the second assertion
for every i in the support of v. The empty maximum is never used.

Sufficiency: let v_1,...,v_n be any basis of linear forms. Sort their costs
m(v_j) increasingly, and sort the coordinate costs p_i increasingly.
For any real t, condition (B) implies that every form of cost <t is
supported on {i:p_i<t}. Independent such forms number at most the size of
this set. If the k-th sorted basis cost were smaller than the k-th sorted
coordinate cost, take t equal to that coordinate cost: there would be
at least k independent cheap forms but at most k-1 cheap coordinates.
This contradiction proves the componentwise sorted comparison. Summing
gives sum_j m(v_j)>=sum_i p_i. Each translated marginal of v_j dot S is
at least m(v_j), proving (A). This proof includes ties, p_i=0, and n=0
(where the assertion is vacuous); no matroid theorem is imported.

Thus an actual selected critical witness obeys ALL of (B), simultaneously
with the existing physical child and exact vertex-edit conditions.

Quantified tolerance: if D_K(f)>=max_{n-bit g}D_K(g)-epsilon, epsilon>=0,
then the same comparisons give p_i<=1/2+epsilon/(2K) and
m(v)>=p_i-epsilon/K for every v_i=1. These are necessary inequalities;
no approximate converse or tolerance uniform after summing n terms is
asserted. Their epsilon scale has no 2^n factor because these edits act
globally and preserve entropy exactly. This differs from singleton vertex
stationarity, whose previous tolerance was 2^n epsilon/4.

## 3. Compression by the affine span of the actual spectrum

Let A={s:fhat(s)!=0}, choose a in A, and let V=span(A+a), of dimension d.
Choose d original coordinate projections J forming a basis of V*. Their
joint projection P:V->F_2^d is an isomorphism. Choose a0 in a+V so that
(a0)_j is a majority value of S_j for each j in J; this is possible
because P maps V onto all F_2^d. The choice need not belong to A.

Multiplication by character a0 moves the Fourier support into V. Complete
the selected coordinate projections on V to an invertible linear map on
F_2^n which sends V onto the first d-coordinate subspace. This completion
exists by extending a basis of V and its dual. Its restriction to V has
first d outputs P. The associated Boolean transform depends on only d
input bits: all other Fourier labels vanish. Call the resulting Boolean
function g. Its squared spectrum is the bijective pushforward of the old
spectrum, hence

    H(g)=H(f),
    I(g)=sum_{j in J} min(p_j,1-p_j)<=I(f).

For d=0 it is a constant after modulation and H=0. The original single
Fourier coefficient is a character, not necessarily a constant.

Consequently every least-essential-dimension positive K-witness (K>=0)
has full affine spectral dimension n: otherwise this actual d<n Boolean
g would still have D_K(g)>=D_K(f)>0. This argument does NOT require a
global affine minimizer or assume that modulated physical children are
old physical children. It uses only lower-dimensional nonviolation.

There is also a SAME-CONSTANT universal reduction. Let R_d consist of
d-bit Boolean signs with full affine spectral dimension d and satisfying
(B), and include the two constants in R_0. After the preceding compression,
minimize I over the finite affine spectral orbit of g. This preserves
full affine dimension d and H, and decreases I. Section2 proves that its
minimum satisfies (B). Thus every Boolean f has some g in R_d, d<=n,
with H(g)=H(f), I(g)<=I(f). For K>=0,

    FEI(K) on all Boolean functions iff FEI(K) on union_d R_d.

Writing b_K(n)=max over all n-bit tables of D_K, finiteness and dummy
padding give the exact cap identity

    b_K(n)=max {D_K(g): g in the disjoint union of R_d, 0<=d<=n}.
Some R_d can be empty: R_1 is empty because every one-bit Boolean sign has a single Fourier coefficient. No maximum over an empty individual class is asserted. The displayed union contains R_0 and is nonempty.


No supremum over dimension is attained or assigned a rate here. Also,
if an n-bit f is epsilon-near b_K(n) and a compression or affine
reduction to d bits increases D_K, then D_K(g)>=b_K(d)-epsilon, since
b_K(d)<=b_K(n). This proves finite-cap near-extremality is stable under
these NONDECREASING-deficit reductions. Arbitrary physical restrictions
are not asserted to preserve it; they retain the signed bank in Section4.

## 4. Original physical-pair consequences and the bank

For distinct i,j write q_ij=P(S_i=S_j=1). Applying (B) to e_i+e_j yields

    max(p_i,p_j)<=p_i+p_j-2q_ij<=1-max(p_i,p_j),
    q_ij<=min(p_i,p_j)/2.

In particular, if p_i,p_j>0, both conditional pair occupancies are <=1/2.
No conditional probability is used when its denominator is zero. For an
epsilon selector the upper occupancy bound becomes
q_ij<=min(p_i,p_j)/2+epsilon/(2K).

The same-dimension shear gain has been used only as a VARIATIONAL
constraint. It is not unused entropy credit and adds no second influence
account. For a proper physical block A at a minimal positive witness,
S_A= -E D_K(f restricted to A)>=0 and

    D_K(f)+S_A = H(f)-E H(f restricted to A)-K I_A.

This follows from I(f)=I_A+E I(child). All actual child entropies remain.
The affine inequalities do not yet upper-bound the right side at a pair,
nor supply a bound on its signed phase/refund interaction.

## 5. Sharp limits of this mechanism

Three-bit majority has squared spectrum uniform on {100,010,001,111}.
The affine spectral dimension is two. Here p_i=1/2, while
m(111)=0. Thus it fails (B). Compression gives a two-bit Boolean bent
function with H=2,I=1, compared with H=2,I=3/2 at majority. This is an
actual Boolean boundary test of the admissibility hypothesis.

For contrast, consider the PROBABILITY LAW uniform on {0,e_1,...,e_n},
n>=2. It has full affine span, p_i=1/(n+1), and for a nonzero v of weight k,
m(v)=min(k,n+1-k)/(n+1)>=1/(n+1). It satisfies every affine minimality
inequality, yet H/I=((n+1)/n)log2(n+1) is unbounded. It is NOT a Boolean
spectrum: any coefficients with exactly this support have nonzero
coefficient 2*a_ei*a_ej at ei+ej in f^2 for i!=j, contradicting f^2=1.
This is an obstruction to the affine probability-law relaxation, never
a counterexample to FEI or an admitted critical witness.

FIRST UNSUPPORTED LINE: combine affine minimum-basis inequalities AND
the signed Boolean convolution/refund structure to pay a proper pair
from the SAME unused D+S_A bank. Neither affine span nor minimum-basis
optimality alone supplies a dimension-independent entropy payment.

## 6. Checks and proof rung

The checks that could fail are: matrix orientation in Fourier pushforward;
Booleanity of modulation/compression; independence of the replaced row;
ties in the sorted-cost argument; zero-dimensional spectra; division by
K or a marginal; and confusing spectral reparameterization with physical
restriction. The checker enumerates every n<=3 truth table, every GL(n,2)
matrix and every translation, compares local and full orbit minima, and
independently constructs compressed truth tables by inverse characters.
It checks pair and tolerance statements using rational influence only.
Entropy invariance is checked by the multiset of squared integer Walsh
numerators, avoiding logarithm decisions. Separate physical edge and
direct-character replay checks the named majority and point witnesses.
The analytic proof above is author-checked; independent review is pending.
A Lean scalar attempt checks only the displayed pair algebra if it returns
a verified receipt; the whole theorem is not claimed Lean-checked.
