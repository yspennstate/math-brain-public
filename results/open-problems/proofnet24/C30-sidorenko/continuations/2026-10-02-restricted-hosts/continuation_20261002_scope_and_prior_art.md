# Scope and prior-art audit of the restricted ML10 host results

2 October 2026. This addendum leaves the original proof checkpoints unchanged.
It separates certified mathematics from historical novelty.

## The four-state matrix assertion

Suppose a symmetric nonnegative four-by-four matrix has identical diagonal
entries d and identical row sums. Write its off-diagonal entries as

    [[d,a,b,c],
     [a,d,e,f],
     [b,e,d,g],
     [c,f,g,d]].

The four off-diagonal row sums are equal, so

    b+c=e+f,   a+c=e+g,   a+b=f+g.

Adding the first two equations and subtracting the third gives 2c=2e;
then the first gives b=f and the second gives a=g. Hence the matrix is

    [[d,a,b,c], [a,d,c,b], [b,c,d,a], [c,b,a,d]],

which is exactly the Klein-group form. Conversely this form is symmetric,
has diagonal d, and every row sum is d+a+b+c. Thus the four-state theorem
covers all equal-measure, equal-diagonal, regular symmetric four-state
hosts, and makes no assertion about arbitrary regular four-state hosts.

## The rank-one qualitative conclusion is already known

Primary source: Péter Csikvári, Nicholas Ruozzi, Shahab Shams,
"Markov Random Fields, Homomorphism Counting, and Sidorenko's Conjecture,"
IEEE Transactions on Information Theory 68(9), 6052–6062 (2022).
The introduction explicitly records the known Sidorenko conclusion for
arbitrary nonnegative two-by-two weight matrices, crediting Ruozzi's 2012
log-supermodular Bethe partition function theorem. Author manuscript:
https://real.mtak.hu/162333/1/Markov_random_fields_Sidorenko.pdf

Underlying primary theorem: Nicholas Ruozzi, "The Bethe Partition Function
of Log-supermodular Graphical Models," NeurIPS 2012, arXiv:1202.6035.
https://arxiv.org/pdf/1202.6035
It permits unary potentials. A nonnegative two-spin edge matrix is
log-supermodular if its determinant is nonnegative; if the determinant is
negative, exchanging the two spin labels on one entire bipartition makes
it log-supermodular. This relabeling also relabels the unary potentials,
and changes neither the partition function nor its Bethe variational
bound. Zero entries follow by continuity.

Here is the precise implication for an unequal-measure regular two-state
host. Let its atom measure be mu and its edge kernel K satisfy
sum_j mu_j K_ij=s for both atoms. Use unary potential mu_i at every source
vertex, node belief mu_i, and edge belief

    b_ij=mu_i mu_j K_ij/s.

These beliefs are locally consistent. In the Bethe free energy, the edge
energy minus edge entropy contribution is

    log s - 2 sum_i mu_i log mu_i,

and the unary energy plus node entropy correction at a degree-d vertex is
d sum_i mu_i log mu_i. The degree sum cancels the edge terms, leaving
e(H) log s. Therefore the known Bethe lower bound proves
t(H,K)>=s^e(H) for every bipartite source H. This is a deduction from prior
theorems, not a new qualitative result.

For the negative rank-one ML10 kernel K=1-z f(x)f(y), with E f=0,
E f^2=1, write m=E f^3. Since ML10 is cubic, its edge-subset expansion uses
only these first three moments. Choose a>0 with a-1/a=m and replace f by
the two-point variable taking a with probability 1/(1+a^2) and -1/a with
probability a^2/(1+a^2). The replacement has exactly the same first three
moments, hence exactly the same ML10 density.

The original kernel's nonnegativity implies
|m|<=z^(-1/2)-z^(1/2), as proved in the quantitative checkpoint. Since
a -> a-1/a is increasing, this is equivalent to
sqrt(z)<=a<=1/sqrt(z). Both replacement diagonal entries are consequently
nonnegative, and its off-diagonal entry is 1+z. It is a regular two-state
kernel with degree one. The preceding known theorem therefore implies
the qualitative rank-one inequality. Positive rank-one perturbations are
already handled directly by the nonnegative edge-subset expansion.

The displayed quantitative surplus

    t(ML10,1+lambda f tensor f) >= 1+5 lambda^4+2 lambda^6

is more specific than the qualitative Bethe implication just described.
A bounded primary search did not locate that exact surplus. This is not
evidence sufficient to claim historical novelty; it should be described
as an explicit quantitative sharpening with novelty unverified.

## Four-state Schur certificate and its source boundary

The Klein-group Schur-convexity certificate is not implied by merely
applying the two-state theorem: it permits all three centered eigenvalues.
The fully general group-correlation host theorem in Yuqi Zhao,
"Sidorenko Inequalities for Two-Sided Group Correlation Kernels,"
arXiv:2606.23018, only covers correlation kernels. On an abelian group
those have nonnegative Fourier coefficients; arbitrary nonnegative
Klein-group weights can have negative centered Fourier coefficients and
need not be a correlation kernel. Thus that theorem does not directly
give the present all-weight family or its Schur-convexity assertion.
https://arxiv.org/abs/2606.23018

Rossman's 2025 ladder transfer identity is used as an independent
regenerator and is explicitly prior art, not part of a novelty claim.
The exact polynomial certificate proves the restricted theorem without
a general spectral assertion. No claimed implication to arbitrary
regular hosts or graphons is available.

The full ML10 Sidorenko problem remains open in this work. Primary status
check: Fox–Himwich–Mani–Zhou, Electronic Journal of Combinatorics 32(3)
(September 2025), paper 38, explicitly lists it as a small unresolved
case. More recent 2026 tensor amplification and group-correlation papers
retrieved in this continuation do not give a general ML10 proof.
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/

