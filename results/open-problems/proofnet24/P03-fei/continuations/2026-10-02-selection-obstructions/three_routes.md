# Independent FEI routes and audited obstacles

Status: no full FEI proof, no full FEI disproof, and no claimed resolution
of the deterministic linear-threshold-function case. The statements below
separate proved identities from missing conjectural steps.

## Route 1: adaptive split induction and bias potentials

The exact increment formula in `split_identity_and_obstructions.md` implies

Δ_iH(f)≤2Σ_S w_Sh₂(q_S)≤2h₂(I_i(f))

by concavity of binary entropy and Σ_Sw_S=1. Thus the elementary bound has
a logarithmic penalty when I_i is small. Removing that penalty for some
adaptively selected coordinate would suffice for full FEI, but is unproved.

The new monotone family disproves three stronger conditions:

1. Bounded increment/influence for every prescribed coordinate.
2. Bounded increment/influence for a maximum-influence coordinate.
3. Existence of a bounded-ratio coordinate within any fixed factor η of
   maximum influence.

The unmodified family also disproves the minimum-positive-influence rule.
None of these defeats the unrestricted existence of a good coordinate.

An attempted repair is to add a potential depending only on the mean:

Δ_iH(f)≤C I_i(f)+Ψ(Ef)−[Ψ(Ef⁺)+Ψ(Ef⁻)]/2,

or the same inequality with the opposite potential sign. For the bad
coordinate of F_k, the restriction means are m±ε, where

m=1−2(7/8)^k−ε.

Take the natural physical binary entropy potential
Ψ(m)=h₂((1+m)/2). Its second derivative is

Ψ''(m)=−1/[ln(2)(1−m²)].

Taylor's theorem on [m−ε,m+ε] bounds the absolute potential difference by
O(ε²/(1−m)), uniformly for large k. After division by I_z=ε this is

O(ε/(1−m))=O(7^(−k)),

whereas Δ_zH/I_z grows linearly in k. Balanced-majority substitution leaves
all three relevant means unchanged and makes z the unique maximum-influence
coordinate. Thus this bias potential cannot salvage maximum-influence
selection. This is a specific audited failure, not a proof that every
possible potential or adaptive strategy fails.

A further identity clarifies a limitation of averaging. The surrogate
Σ_Sw_Sh₂(q_S) is exactly the conditional entropy of the spectral inclusion
bit i given all other inclusion bits. Hence

Σ_iΔ_iH(f)≤2Σ_iH(X_i|X_{−i})≤2H(X)=2H(f).

This gives min_iΔ_iH/I_i≤2H(f)/I(f), which is circular for FEI. There is no
useful reverse bound: any globally odd f, satisfying f(−x)=−f(x), has
Δ_iH(f)=0 for every coordinate i. Indeed its spectrum has only odd levels,
so one coefficient in each S,S∪{i} pair is zero and the restrictions have
identical squared spectra. Entropy can therefore be generated later in a
restriction tree even when all first-step increments vanish.

**Remaining step:** prove a universal constant for unrestricted adaptive
selection, or find a family whose minimum relevant-coordinate ratio diverges.
The explicit family and exhaustive four-bit computation do neither.

## Route 2: ternary derivatives and pivotal-set entropy

For g_i=(f⁺−f⁻)/2, the function g_i takes values in {−1,0,+1}; put
α_i=||g_i||₂²=I_i(f). Its normalized Fourier distribution is

p_i(T)=hat(g_i)(T)²/α_i
      =hat(f)(T∪{i})²/α_i.

Direct summation proves the weighted derivative-entropy identity

Σ_i α_i H(p_i)
=Σ_{S≠empty}|S|hat(f)(S)²log₂(1/hat(f)(S)²)
 −Σ_i α_i log₂(1/α_i).                 (2.1)

For monotone f, g_i is the indicator of its pivotal cross-section. This
suggests applying an entropy bound to those indicators. The obstacle is
that the natural derivative-energy sum is a second degree moment:

Σ_i I(g_i)
=Σ_S |S|(|S|−1)hat(f)(S)².            (2.2)

Consequently, even a strong bound of derivative entropy by derivative
energy naturally produces a quadratic-moment bound, not the desired first
moment I(f). This prevents the naive derivative induction from closing.

The general ternary-derivative class is no smaller than the original problem:
for any Boolean h, f(x,z)=z h(x) has g_z=h. Thus an asserted universal
entropy bound for arbitrary normalized derivatives must confront arbitrary
Boolean Fourier spectra, rather than bypass them.

For an indicator g=1_A of mean α and f=1−2g, an exact normalization identity is

H(f)=4·Σ_Shat(g)(S)²log₂(1/hat(g)(S)²)
 −4α²log₂(1/α²)−8α(1−α)
 +(1−2α)²log₂(1/(1−2α)²),

with continuous interpretation at α=1/2. This shows why unnormalized
indicator entropy cannot be casually identified with Boolean spectral
entropy. Any proposed induction must retain these mean terms.

**Remaining step:** use special joint geometry of pivotal cross-sections to
amortize (2.1) against I(f), without invoking (2.2) as the main budget.
No such estimate was established.

## Route 3: finite-order autocorrelation and dyadic coefficient levels

Booleanity f²=1 imposes the exact Fourier autocorrelation constraints

Σ_T a_T a_{T△U}=1_{U=empty},

in addition to Parseval and dyadic rational coefficients. Ordinary entropy
subadditivity uses none of these constraints and gives only

H(f)≤Σ_i h₂(I_i(f))
≤Σ_i I_i(f)log₂(1/I_i(f))+log₂e·I(f).

This inequality holds for every real function of unit L² norm, and therefore
cannot by itself explain FEI. In particular, a unit vector with singleton
Fourier coefficients 1/√n has entropy log₂n and influence 1, while its
inverse Fourier transform is not Boolean. A proof must use the finite-order
constraints at an essential step.

An attractive candidate was an amplitude-level statement: within a bin of
coefficients of magnitude approximately 2^(−j), the mean Fourier degree
should be Ω(j). This is false. For majority on an odd number n of bits, each
singleton coefficient has magnitude binom(n−1,(n−1)/2)/2^(n−1)=Θ(n^(−1/2)),
so those coefficients have amplitude scale j≈(1/2)log₂n but degree exactly
one. Higher-degree spectral mass must pay for the entropy of this low-degree
bin; a bin-by-bin inequality cannot suffice.

A related attempt decomposes the squared integer Walsh coefficients into
binary digits and seeks low algebraic degree of each digit indicator. This
also cannot be used without cross-digit transfer. For AND_3, the integer
Walsh coefficient at the empty index is −6 and the other seven magnitudes
are 2. The bit-5 indicator of Walsh-square is therefore the singleton empty
index (because 36 has bit 5 and 4 does not). That indicator has algebraic
degree three and mean Hamming weight zero, although it accounts for a large
positive mass. The lower bits must compensate. A claim that each squared
amplitude digit individually supplies its needed entropy budget is false.

**Remaining step:** a cross-level or cross-digit entropy-transfer estimate
using the full autocorrelation system. None was proved.

## Route 4: deterministic LTF via a Gaussian entropy calculation

This additional route seeks a genuinely major restricted case: FEI for all
linear threshold functions. The primary random-LTF paper arXiv:1903.11635
explicitly distinguishes its random result from the unresolved deterministic
case. No resolution of that case is asserted here.

There is a clean auxiliary Gaussian calculation. Let X_i be independent
standard Gaussian variables, Σ_iw_i²=1, and F(X)=sign(Σ_iw_iX_i). Expand in
the normalized multivariate Hermite basis. If K is total Hermite degree,
its distribution has masses

q_(2m+1)=(2/π)·binom(2m,m)/[4^m(2m+1)],   q_(2m)=0.

Conditioned on K=k, the multi-index has multinomial law with k trials and
cell probabilities p_i=w_i². This follows by expanding the normalized
Hermite polynomial of Σ_iw_iX_i with the multinomial identity.

The central-binomial product bound gives q_k≤(2√2/π)k^(−3/2). Therefore
H(K) is bounded by an absolute constant. For any nonnegative integer-valued
random variable of mean λ, its entropy is at most

g(λ)=[(1+λ)ln(1+λ)−λ ln λ]/ln 2,

the entropy of the geometric law of that mean (proved by nonnegativity of
relative entropy). Entropy subadditivity on the multinomial coordinates gives

H(multi-index|K=k)≤Σ_i g(kp_i).

The convergent integral

∫_0^∞u^(−3/2)[(1+u)ln(1+u)−u ln u]du=4π

follows by integration by parts and u=v². Monotonicity of g on each interval
[k,k+1] then bounds Σ_{k≥1}k^(−3/2)g(kp) by an absolute constant times √p.
Here are explicit constants. Write A=2√2/π. The degree law obeys
q_k≤A k^(−3/2). Compare q to r_k=k^(−3/2)/ζ(3/2) using relative entropy:

H(K)≤[ln ζ(3/2)+(3/2) E ln K]/ln 2.

The interval bound

Σ_{k≥1}k^(−3/2)ln k
≤2√2∫_1^∞x^(−3/2)ln x dx=8√2

gives E ln K≤32/π. Also ζ(3/2)≤3, so

H(K)≤[ln 3+48/π]/ln 2.

On each [k,k+1], monotonicity of g and x^(−3/2) imply

k^(−3/2)g(kp)≤2√2∫_k^{k+1}x^(−3/2)g(px)dx.

Summing and substituting u=px yields

Σ_kq_k g(kp)≤(32/ln 2)√p.

Thus the Hermite spectral entropy satisfies the proved auxiliary estimate

H_Hermite(F)
≤[ln 3+48/π]/ln 2+(32/ln 2)Σ_i|w_i|
≤70 Σ_i|w_i|.                        (4.1)

The last inequality uses Σ_i|w_i|≥1 and
[32+ln3+48/π]/ln2<70. We do not claim this Gaussian statement is new.

For a regular unbiased Rademacher LTF, total Boolean influence is comparable
to Σ_i|w_i|, so (4.1) is suggestive. The missing step is transferring the full
spectral entropy from the Gaussian Hermite distribution to the deterministic
Rademacher Fourier distribution. Low-degree invariance alone is inadequate:
entropy continuity costs dimension-dependent logarithms and does not control
the contribution of the whole high-degree tail. Gaussian random scaling of
the weights only gives an average statement, not one for the original weights.

For biased Gaussian halfspaces, an additional threshold contribution is
necessary: already one Gaussian coordinate at a very large threshold has
entropy/influence ratio growing with the threshold. In a nonconstant Boolean
LTF one has |threshold|≤Σ_i|w_i|, suggesting a possible repair after a valid
transfer theorem, but that transfer and the required uniform biased estimate
remain unproved.

**Remaining step:** a dimension-free, whole-spectrum entropy comparison for
deterministic weighted Rademacher halfspaces, including biased and irregular
weights. This route currently stops at the auxiliary Gaussian calculation.

### Audited failure of a geometric sufficient condition

Splitting a monotone LTF on a largest weight gives F=A+zB with monotone
ternary A, B=1_{A=0}, and no hypercube edge joining A=+1 to A=−1. On every
edge, (A(u)−A(v))²=(B(u)−B(v))², hence I_j(A)=I_j(B) for every j. These
strong-looking geometric and energy conditions suggested a universal
increment bound Δ_zH≤C E B.

The condition is nevertheless false, even for monotone A. Section 6 of
`split_identity_and_obstructions.md` gives a full constructive counterexample:
balanced-majority substitution plus one-step erosion makes a zero buffer
between signs while adding only δ<ε⁶ zero mass. Conditional binary entropy
continuity controls the change in the exact increment independently of the
enormous ambient dimension, leaving Δ_zH/E B=(log₂7/4)k+O(1).

The finite probe checked all 741 admissible ternary separators on three
base bits and sampled 3,000 weighted LTFs in dimensions 8 and 12. The largest
observed ratios were approximately 4.868, 4.914, and 4.871, respectively.
Those encouraging numbers did not establish the candidate lemma; the
general construction disproves it. The counterexample is not an LTF, so
the deterministic LTF target remains unrefuted and unsolved.

## Verified scope

The strongest fully proved new-in-this-work result is the quantified monotone
obstruction to approximately maximum-influence selection, together with the
monotone zero-separator counterexample. The full adaptive
criterion, full FEI, and deterministic LTF case remain explicitly open in
this checkpoint. Mathematical novelty of the obstruction has not been
established by a comprehensive literature audit.
