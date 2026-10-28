# Independent analysis of the Abelian reset construction

Status: scoped mathematical analysis, not an originality certificate.

I read the entire candidate and the primary survey's graph and group definitions
on PDF pages 24 through 27. The numbered question has no degree restriction.
The adjacent expander paragraph explicitly has a degree restriction, but that is
a separate model. The following weighted-walk paragraph is also separate.
The candidate gives a simple undirected graph and uniform choice from a set,
so it does not merely apply a weighted counterexample outside the question.

Let N=2^d and let M=m-1. Counting the two disjoint sets of generators gives
D=dM+N-1. For a nonzero cube increment y, its actual projected rate is
(1+M 1_{y is a basis vector})/D. Hence the projected generator, directly from
its off-diagonal entries, is a rate alpha=dM/D cube walk plus uniform-reset
generator beta(Pi-I), with beta=N/D. The actual nonzero global jump rate
theta=(N-1)/D is different. Comparing the diagonal then gives the same
identity on every entry. The exact checker independently enumerated 2,720
entries on eight small graphs and rejected eight substitutions of theta.

The reset generator commutes with the cube generator and annihilates uniform
measure. On mean-zero signed measures its semigroup is scalar exp(-beta t).
Consequently the projected total variation distance is exactly the cube
distance at alpha t times exp(-beta t), not just an upper bound.

For the auxiliary factor, conditional on the complete cube path and event
types, each local event still carries an independent uniform nonzero increment.
The first such increment differs from uniform by exactly 1/m in total
variation. Further convolutions contract that distance. Replacing the
conditional auxiliary law by uniform changes the joint law by at most
Pr(no local event)+1/m. The resulting joint law is the cube marginal times
uniform. Triangle inequality and projection therefore trap full-state total
variation between q(t) and q(t)+exp(-alpha t)+1/m. This checks the dependence
through the shared event count rather than assuming unconditional independence.
Sixteen exact finite convolutions independently check the conditional bound.

For a cube character of degree a and an auxiliary character l, the direct sum
over generators is (d-2a)c_l+b_a, where c_0=M and c_l=-1 otherwise,
and b_0=N-1 with b_a=-1 otherwise. This follows separately from the basis
sum and the full nonzero-cube sum. The checker evaluates these sums using
integer Gaussian roots for all 360 characters on the eight exact graphs.
Actual breadth-first traversal verifies connectivity in those cases.

The nonconstant auxiliary sectors have gaps dm/D and at least (D-d+1)/D,
both tending to one for the proposed m. The slow cube sector has smallest
gap gamma=(2M+N)/D. With M=ceil(N log(d)/4), alpha tends to one,
beta T tends to one for T=d log(d)/(4 alpha), and gamma is asymptotic to
2/d. The full-spectrum calculation rules out an omitted auxiliary bottleneck.

An independent direct product-mass calculation gives the cube chi-square
divergence (1+r^2)^d-1 for coordinate sign bias r. Ten exact rational-bias
cases verify it and reject ten incorrect bias-power formulas. At time
s d log(d)/4 the bias is d^(-s/2), so the divergence tends to zero for
s>1. For s<1 the sum of signs has mean d^(1-s/2), variance at most d,
whereas its stationary mean is zero with variance d. Using the midpoint
threshold and Chebyshev under both laws gives separation at least
1-8 d^(s-1), which tends to one.

The full-state profile at sT is therefore exp(-s) for 0<s<1 and zero for
s>1. Its jump at one is not sufficient for cutoff: the distance already
decays by a nonvanishing amount at earlier proportional times. Monotone
bracketing gives t(1/4)/T tending to one and t(3/4)/T tending to
log(4/3). Thus gamma t(1/4) is asymptotic to log(d)/2, while the ratio
of those two mixing times stays away from one. The graph is transitive,
so a hidden worse initial state cannot rescue the cutoff claim.

The strongest counter-case is an omitted restriction on degree, generating
sets, or time normalization. The exact numbered source imposes no degree
bound; the generator convention is rate-one continuization. The construction
has deliberately chosen generators and extremely large degree. It therefore
does not answer the bounded-degree expander or uniformly random-generator
versions. No statement about those narrower questions is warranted.

I also read the first five pages of Pedrotti and Salez's July 2026 paper,
archived with SHA256 add7dba482e5f8d70daee76d8279c33802442ba22f7d36c7f73d5b4f8bb0dbf6.
It explicitly discusses the known weighted-reset obstruction and replaces
the stationary Poincare constant by a stronger non-equilibrium constant.
It does not identify a resolution of this unweighted realization in those
pages. Only those pages were read. Related primary searches found older
unrestricted nilpotent conjecture formulations and random-generator theorems;
this is not a complete later-literature or priority investigation.

Eight graph cases, 360 characters, 2,720 projected entries, sixteen convolutions and ten
product-mass cases passed; eighteen deliberately wrong rate/power controls were
rejected. These finite checks support the formulas; the asymptotic proof is the separate
argument above. No gap was found in that checked scope.
