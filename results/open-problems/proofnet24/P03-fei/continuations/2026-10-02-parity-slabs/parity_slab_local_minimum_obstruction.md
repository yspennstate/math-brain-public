# A two-crossing slab obstructs a local minimum-influence split criterion

2 October 2026. Complete analytic consequence of the already proved
[three-crossing obstruction](../2026-10-02-parallel-slabs/three_crossing_largest_weight_obstruction.md).
The obstruction below is local. It does not refute spectral-center FEI,
ordinary slab FEI, or the general Boolean FEI conjecture.

Let N=2d+1≥3, x in the N-cube, z a further sign, M(x)=sign(Σ_j x_j),
D(x)=1{x is all minus}, and ε=2^(−N). Define

g_N(x,z)=1−2·1{−N+1/2<Nz+2Σ_j x_j<N+1/2}.

This is exactly one parallel interval with two endpoints. All input
weights are integers and all attained scores are integers, so the
half-integer endpoints cause no ties. The pivot weight N is uniquely
largest because all other weights are two and N≥3.

For z=−1 the interval condition holds precisely when Σx_j≥1. For
z=+1 it holds precisely when −N<Σx_j≤−1. Thus

g_N^- = −M,   g_N^+ = M+2D.

The only pair with equal restricted labels is the all-minus point, so
I_z(g_N)=1−ε and min(I_z(g_N),1−I_z(g_N))=ε.

The previously derived three-crossing function f_N has restrictions
f_N^-=M, f_N^+=M+2D. Hence g_N=z f_N exactly. Character multiplication
permutes the full squared Fourier spectrum and output signs preserve
the restricted entropy, so

Δ_z H(g_N)=Δ_z H(f_N).

For completeness the analytic coefficient argument is reproduced here.
Write g_N=A+zB with A=D and B=M+D. Every Fourier coefficient of D is
ε(−1)^|S|. Majority has zero coefficient at even degrees and, for
|S|=2ell+1,

Mhat(S)=(−1)^ell [binom(2d,d)/4^d]
                       [binom(d,ell)/binom(2d,2ell)].

Its derivative in any selected coordinate is the central-layer indicator
on the remaining 2d inputs. On that layer, the character generating
polynomial is (1+t)^d(1−t)^d=(1−t²)^d, which proves this formula.
The central-binomial maximum gives binom(2d,d)/4^d≥1/(2d+1).
Vandermonde and log-concavity give
binom(2d,2ell)≤(d+1)binom(d,ell)², and binom(d,ell)≤2^d. Thus

|Mhat(S)|≥2^(−d)/[(2d+1)(d+1)]
=2^(−(N−1)/2)/[N(N+1)/2].

For N≥15 this is at least 2ε. The ratio to ε is already greater
than two at d=7 and increases thereafter.

For each spectral pair a=Ahat(S), b=Bhat(S), P=a²+b², the exact
split increment is P[1+h₂(a²/P)−h₂((a+b)²/(2P))]. The version using
a²/P is valid because binary entropy is symmetric. It is at least
P h₂(a²/P). At every even subset a=b, and the full contribution is
4ε². The 2^(N−1) even subsets therefore give 2ε in total.

At every odd subset, |b|≥|Mhat(S)|−ε≥|Mhat(S)|/2. Its contribution
is at least ε² log₂(P/ε²), hence at least

ε²[N−1−2log₂(N(N+1)/2)].

Adding the 2^(N−1) odd subsets and the exact even contribution yields

Δ_z H(g_N)/min(I_z(g_N),1−I_z(g_N))
≥(N+3)/2−log₂[N(N+1)/2] → infinity.

Therefore no universal local largest-weight inequality
Δ_z H≤C min(I_z,1−I_z) can hold even for genuine parallel slabs.
The successful spectral-center argument instead charges each peeled
coordinate to the *total* influence of the centered function and peels
only a uniformly bounded number of coordinates. It never invokes this
false stronger local statement.

The family is also included in the arbitrary-character slab class:
f_N=z g_N. Thus the new global theorem covers the prior three-crossing
local obstruction without claiming a theorem for all three-crossing
functions. The finite probe in verify_parity_slab_center_heat.py checks
the exact pivot influence and records numerical entropy increments for
N=3,5,...,19; the dimension-independent failure is proved above.
