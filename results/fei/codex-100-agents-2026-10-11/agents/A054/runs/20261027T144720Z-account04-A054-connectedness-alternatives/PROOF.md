# An isolated spectral bit has an exact price

At a genuine fixed-K critical source with K>=4, every essential spectral
bit depends on the other spectral bits. The statement concerns exact
independence from the whole complement, not pairwise covariance.

All cubes are finite and uniform. A Boolean sign has normalized real
Walsh coefficients fhat(S), squared spectral law P(S)=fhat(S)^2,
entropy H in bits, and total influence I. Let Z_i=1_{i in S} and
p=P(Z_i=1)=Inf_i(f). The Fourier coefficients are integer multiples
of 2^-n; p is a dyadic rational. Independence means
P(Z_i=z,S_without_i=T)=P(Z_i=z)P(S_without_i=T) for EVERY T,z.
Zero rows are retained as zero; no division by them is made.

1. Arithmetic rigidity. If 0<p<1, choose a row with positive exterior
mass. Independence makes both Fourier coefficients on that row nonzero,
and their squared ratio is p/(1-p). Thus p/(1-p) is the square of a
nonzero rational number. Write the reduced dyadic p=k/2^m, m>=1,
k odd and 0<k<2^m. The integers k and 2^m-k are coprime and odd.
A reduced positive rational square has square numerator and denominator
(compare prime exponents). Hence k=a^2 and 2^m-k=b^2 for odd integers
a,b. Odd squares equal1 modulo8, so 2^m equals2 modulo8. The only
nonnegative exponent with that residue is m=1. Therefore p=1/2.
The boundary cases are p=0 or1. Booleanity is used through dyadic
Fourier arithmetic and dyadic p; this is not a statement about arbitrary
normalized real Fourier vectors.

2. Exact entropy decrement at p=1/2. Write the root Fourier rows as
a_T=fhat(T), b_T=fhat(T+i). Independence gives a_T^2=b_T^2. The two
COMPLETE physical children have Fourier coefficients a_T+b_T and
a_T-b_T. Since a_T,b_T are real, one of these coefficients is zero
on every nonzero row and the other has squared magnitude4a_T^2.
Thus the child spectra have disjoint supports. With mu_T=2a_T^2,
Parseval gives mass1/2 for each child's support in mu. Entropy of this
disjoint mixture is H(mu)=1+[H(g_0)+H(g_1)]/2. The root entropy is
1+H(mu), so EXACTLY

    H(f)=2+[H(g_0)+H(g_1)]/2,
    I(f)=1/2+[I(g_0)+I(g_1)]/2.                  (1)

Conversely a_T^2=b_T^2 follows from disjoint complete child spectra,
and their normalized masses force p=1/2 and independence. Thus
nontrivial independence is equivalent to disjoint child spectra. The
two child means cannot both be nonzero. All Fourier rows are included.

3. Full critical account. For the two complete children set
t=E a(g), R=E I(g)-t>=0, S*=E[K a(g)-H(g)], and D=H(f)-K I(f).
Here a is the exact minimum influence under affine input maps and
output characters; H is preserved by these operations. Equation(1)
gives the exact original-source identity

    D+S*+K R = 2-K/2.                            (2)

This pays the full selector entropy price2 and the retained child-reset
interface K R from the SAME original account at rate4. No phase price
Pi from a rematched function or old debit is erased; equation(2) is
applied to the original physical root and complete children.

Suppose f is represented on its n essential coordinates, D>0, and has
least essential dimension among positive-D Boolean signs at the SAME
K. Then each complete child and its affine/character representatives
has smaller essential dimension. Hence S*>=0 and R>=0. For K>=4,
the left side of(2) is positive and the right side nonpositive, an
impossibility. At p=0 the coordinate is inessential. At p=1 the root
is x_i times a smaller sign, H is unchanged by restriction and I falls
by1, immediately contradicting least dimension and D>0 for K>0.
Therefore every coordinate of a genuine critical witness with K>=4
has 0<p<1 and strictly positive I(Z_i;Z_without_i).

4. Connectedness alternative. If ALL spectral bits are independent,
each marginal is0,1/2 or1. Product entropy then gives

    H(f)=number of half-biased bits <=2 I(f).

This does NOT imply f is an input tensor product. The two-bit quadratic
sign (-1)^(x_1 x_2) has a product uniform squared spectrum and is not a
product of one-bit Boolean signs. In particular one cannot equate
spectral independence with a factorization of signs or delete phases.

For a critical root K>=4 the preceding stage's capacity and the full
Gibbs remainder give, for every singleton,

    0<I(Z_i;Z_without_i)<log2(1+exp(2)2^-K).

Indeed the complete Gibbs divergence W equals that mutual information
plus D_2(Ber(p)||Ber(theta)), theta=1/(1+2^(K-2/ln2)); the full
identity D+S*+K R+W+G=capacity has D>0 and all other terms nonnegative.
This uses A051's exact full-child Gibbs identity, reconstructed by
expanding its relative entropy (and requiring 0<theta<1). Tiny positive
dependence is not ruled out. No uniform lower bound on it is claimed.

5. Independent review of A052 stage22. For g on d>=2 bits and negative
set M, a nonzero translation v pairs M intersect(M+v), so its cardinality
is even. The directional disagreement count equals
2|M|-2|M intersect(M+v)|, thus is2|M| modulo4. The count after an output
character complement is N-b(v), with the same residue since N=2^d
is divisible by4 and b(v) is even. Every affine basis has d nonzero
directions. Its total count therefore has a common residue modulo4.
All full affine/character influence savings are nonnegative multiples
of q_d=2^(2-d); for d1 use q_1=1, and d0 release0. Averaging actual
complete children gives R>=2^-r q_d m for m improving children.
Substituting into the full critical bank yields A052's strict count
m<2^r capacity/(K q_d), with D>0 supplying strictness. If capacity is
at most K2^-r q_d then m=0. The source's rational sufficient exponents
K2^(K-n-2)>=r for d>=2 and K2^(K-n-3)>=r for d1 follow by inserting
capacity_3<r2^(4-K). This reconstruction HOLDS without repair at its
stated dimension-dependent scope. It grants no descendant stationarity
and does not quantify nonlinear phase prices.

First unsupported universal line: when dependence is positive but
exponentially small and n>>K, prove a Boolean lower payment sufficient
to select one ORIGINAL block including Pi, old debits and all complete
child reserves. Exact independence rigidity supplies no such stability
bound and gives no universal FEI constant improvement.
