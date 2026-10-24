# Independent analytic reconstruction of A053's packed-surgery exclusion

Source: A053/runs/20261014T052310Z-account05-A053-near-tensor-perturbations/
PACKING_CRITICAL_EXCLUSION.md sections1--4, and bundled claim
A053-PACKED-POINT-SURGERY-PAID-SINGLETON@1. Reviewer A054 supplies no
repair. Verdict: ACCEPT_AT_STATED_ANALYTIC_SCOPE for the complete bundled
statement; the source's finite census is not adopted. Shared registry
adoption and a second independent reconstruction remain pending.

Let N=2^n, p=1/N, e=2p, seed support size s and one edited vertex v.
Radius-one balls about distance-three support indices are disjoint,
giving s(n+1)<=N. At n>=3 at least one Walsh sum is zero. For n>=2,
all Walsh sums are congruent modulo4 to -2 times the negative count:
subtracting the zero-index sum changes it by twice a sum of N/2 odd
integers, an even sum. Thus the negative count is even and nonzero
seed amplitudes have magnitude at least4p. The edit adds amplitudes
of magnitude e everywhere. Every singleton and pair row contains at
most one old coefficient. Its occupied amplitude remains at least e;
all its other amplitudes have magnitude e.

There are N/2 singleton rows, each with minority squared mass e^2.
Therefore beta_i=2p exactly. The physical incident-edge change is
Inf_i(G)-Inf_i(F)=2p F(v)F(v^i). Subtract beta and sum to recover
sum O_i=I(F)-4p d_v. This also gives
T=I(G)-2np+R_sum exactly. For an occupied singleton row, its weighted
collision 4a^2b^2/(a^2+b^2)<=4e^2; summing occupied and new rows gives
C_i<=8p. Each pair's two nonnegative merging refunds are bounded by
its two pre-merging singleton collisions, hence their sum<=16p.
Consequently |T-I(F)|<=4np+16 binom(n,2)p, including signs of edits.

For singleton entropy, newly created rows have total mass
W=4p-8sp^2 and each costs exactly two bits for B+J. Occupied rows
have total minority mass b=4sp^2. Weighted concavity bounds their B by
b log2(1/b)+b/ln2; two-point logarithmic Sobolev, recentered to the
larger amplitude, bounds J by2b/ln2. Hence
L_i<=2W+b[log2(1/b)+3/ln2]. The scalar bracket times b increases;
b<=4p/(n+1), ln2>2/3 and log2(n+1)<=(n+1)/2 yield
L_i<(14+6/(n+1))p<=15.5p<16p.
For the collision upper price V_i, its occupied channel is at most
4b/ln2, giving V_i<19p by the same scalar substitutions.

The pair calculation is independently checked as follows. Normalize a
quartet to squared norm1, with one anchor a and off-anchor squared mass
epsilon=b^2+c^2+d^2. Its physical collision is
4[(ab+cd)^2+(ac+bd)^2+(ad+bc)^2]. AM-GM on the three off-anchor
squares bounds this by
4epsilon-(8/3)epsilon^2+(8/sqrt3)epsilon sqrt(epsilon(1-epsilon)).
This is <=(16/3)epsilon: after rearranging and squaring, the needed
inequality is (4epsilon-1)^2>=0. Thus occupied pair collision is at
most(16/3) of its off-anchor mass. The new pair rows each cost four
bits for B+Gamma. Their total mass is4p-16sp^2; occupied off-anchor
mass is3se^2<=12p/(n+1). Concavity bounds the occupied entropy by
epsilon[log2(1/epsilon)+log2 3+1/ln2]. Since Gamma<=collision/ln2
(log(1+t)<=t), the resulting total is exactly the source's bracket
with19/(3ln2). The scalar upper substitution yields a coefficient
below16+18+78/(n+1)<=53.5<54. This verifies the pair price too.

For physical influence, each sign indicator of a nonconstant seed has
Fourier support at most s+1. Fourier inversion at an occupied vertex
and Cauchy--Schwarz give each sign mass>=1/(s+1). After one edit and
N>=3(n+1), both masses are >=a_n=(3n-1)p/4 for n>=4. Boolean Poincare
gives I(G)>=4a_n(1-a_n)>=(53/64)(3n-1)p>2np. Monotonicity of a_n
and a_4=11/64 justify the53/64. At n3, packing s<=2 and squaring a
two-coefficient sign excludes s=2; the seed is a character. Direct
point-edit averaging gives I(G)>=3/4=2np. Constant seeds give
I(G)=2np and the usual exact point-defect spectrum. These are all
cases, and the edited spectrum is full, so its named cube is essential.

Select a coordinate of maximum influence, hence Inf_i>=2p. The proved
row bounds give L_i<8Inf_i and V_i<(19/2)Inf_i without any influence
floor hypothesis. At K>=8 the EXACT physical identity
D_K(G)-E_child D_K(G_child)=L_i-KInf_i is strictly negative.
Thus a violating root passes a still larger positive average deficit
to actual children, so at least one smaller-dimensional child violates.
This proves the advertised criticality exclusion. It proves neither a
closed descendant class nor unrestricted FEI(8) for edited roots with
uncertified terminals. The constant and n3 character cases also have
root H/I<4 or <=4, respectively, consistent with the statement.

No A052 or A055 universal claim is needed: the row collisions, refunds,
logarithmic Sobolev, packing, inversion, Poincare and physical telescope
have all been reconstructed here. Source helper was inspected for its
representation and domain, not rerun or accepted as independent finite
validation. No files in A053 or shared indices were modified.
