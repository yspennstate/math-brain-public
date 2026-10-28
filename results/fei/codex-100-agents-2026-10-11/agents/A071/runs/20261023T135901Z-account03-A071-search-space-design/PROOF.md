# Proper Boolean decompositions cannot initialize prime Hamming balls

All logarithms are base 2. Let N=2^n, n>=3, and b_n(x)=-1 exactly
when the bit vector x has Hamming weight at most one. This is an actual
Boolean family on the uniform physical cube, not a proposed spectral law.

## 1. A complete block-compression criterion

For a coordinate block B, form the matrix with assignments on B as rows
and assignments on its complement as columns, containing the values of f.
There exists a Boolean summary g_B(x_B) and an unrestricted function
H(g_B(x_B),x_outside) computing f if and only if this matrix has at most
two distinct rows. Necessity is pigeonhole. For sufficiency assign the
two row types to the two signs and define H by the corresponding row.
This criterion loses no possible Boolean core or outer gate.

For b_n, let 2<=|B|<=n-1. A row of weight zero is negative on outside
weights zero and one. A row of weight one is negative only at outside
weight zero. A row of weight at least two is everywhere positive. All
three row types exist and differ, since the complement is nonempty.
There are exactly three distinct rows. Therefore no such B can be
replaced by a Boolean summary, even when all outside bits are left raw.

Consequently, in ANY representation b_n=h(g_1,...,g_r) on a partition of
the physical coordinates into proper disjoint blocks, each block is a
singleton. If some block had size at least two, fixing the other core
outputs as functions of the outside bits would give the forbidden
two-row representation. Every coordinate is relevant, so a singleton
core is nonconstant and is a bit or its complement. Unused constant
gates do not change this conclusion. A whole-domain core is explicitly
excluded from 'proper'; allowing it simply retains the original FEI
problem inside that core. Overlapping supports and multiple-bit summaries
are outside this obstruction and may escape it.

## 2. Exact spectrum and influence

Use characters (-1)^(x dot S). The empty Fourier coefficient is
mu=1-2(n+1)/N. For nonempty S of size k, orthogonality of the constant
function gives

    bhat_n(S)=-(2/N)[1+sum_j (-1)^(1_{j in S})]
             =-2(n+1-2k)/N.

Its squared mass is p_k=4(n+1-2k)^2/N^2, with multiplicity binom(n,k).
Zero masses contribute zero entropy. The only boundary edges join a
weight-one point to a weight-two point. There are n(n-1) undirected
boundary edges. Hence

    I(b_n)=2n(n-1)/N,
    H(b_n)=eta(mu^2)+sum_(k=1)^n binom(n,k) eta(p_k),
    eta(u)=-u log2 u.

This formula is exact and includes the empty coefficient. Direct character
sums and physical edge counts check it independently on n=3,...,6.

## 3. Universal entropy bounds and the limit four

Let delta=1-mu^2=4(n+1)/N * [1-(n+1)/N]. For every nonzero nonempty
coefficient, 1<=|n+1-2k|<=n+1. Thus

    [(2n-2)-2log2(n+1)] delta <= H(b_n)
        <= (2n-2)delta+eta(mu^2)
        <= (2n-1/2)delta.

For the last inequality, -u ln u<=1-u for 0<=u<=1, so
eta(mu^2)<=delta/ln2<(3/2)delta. The elementary inequality ln2>2/3
follows from the positive atanh series; endpoints follow by continuity.
After division by I, delta/I equals

    2(n+1)/(n(n-1)) * [1-(n+1)/2^n].

Both entropy bounds divided by I tend to 4, proving H(b_n)/I(b_n)->4.
This is a finite limit, not an unbounded-ratio family. The certificate
additionally verifies H(b_16)>3I(b_16) and H(b_32)>(7/2)I(b_32).

For clarity this particular family is influence-paid: H(b_n)<5I(b_n)
for ALL n>=3. For n>=8, the upper bound divided by I is smaller than
(4n-1)(n+1)/(n(n-1)), which is at most five because n^2-8n+1>=0.
For n=3,...,7 the exact upper ratios are respectively
11/3, 275/64, 741/160, 3059/640, 135/28, all less than five.
Thus the rational3 bank is less than8I on this family. Zero partition
savings obstruct a proposed universal discount, not influence payment
of these balls themselves. No sharp constant five or eight is asserted.

## 4. Consequence for the live initialization question

For any real K>=0 a singleton core and all its restrictions have zero
Fourier entropy. Their full physical stopping deficit hulls rho_K are
therefore zero. On EVERY proper disjoint Boolean decomposition above,
the signed correction C=H(b_n)-sum q_j H(g_j) is H(b_n). Consequently
the full supplied bank of A075 is exactly

    U_K=C+kappa I(b_n)+sum q_j rho_K(g_j)=H(b_n)+kappa I(b_n).

Optimizing over proper disjoint Boolean decompositions saves exactly zero
initial entropy for every n>=3 and every K>=0. In particular it cannot
uniformly extract any positive fraction of H, even on the explicit
entropy-bearing cases n=16 and 32. The infimum required price U_K/I on
this family tends to 4+kappa. This refutes the proposed strategy-level
lemma 'every Boolean function admits a proper disjoint Boolean partition
with positive weighted inner entropy/hull savings.' No cited agent claimed
that lemma as established. A075's universal coherence theorem remains true.
At the rational kappa=3 the initial price tends to seven on this family;
this is a lower obstruction to that particular bank, not a lower bound
seven for the FEI constant, and it is not a universal bank upper bound.

The FIRST UNSUPPORTED universal line remains an initial influence payment
for arbitrary Boolean functions, beyond singleton/whole-function restatement,
from the actual same original unused owners. A proper partition alone
cannot supply a universal strictly positive discount. Restrictions, overlaps,
or multi-bit state may help, but require an explicit new conserved payment.
