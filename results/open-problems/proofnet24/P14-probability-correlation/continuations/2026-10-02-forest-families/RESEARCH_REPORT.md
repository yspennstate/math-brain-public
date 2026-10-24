# Random forests and the q<1 random-cluster conjecture: exact partial results

Research checkpoint, 2 October 2026. These notes record proved restricted results,
computational observations, primary-source boundaries, and the unresolved step.
They do **not** claim a solution of the general conjecture or certified novelty.

## The open conjectures

For a finite graph G, write

\[
 Z_G(\mathbf z)=\sum_{F\subseteq E(G)\;\mathrm{acyclic}}\prod_{e\in F}z_e.
\]

The arboreal gas samples a forest proportionally to the product of its positive
edge activities. The forest negative-correlation conjecture asks whether, for
all distinct edges e,f,

\[
 \mathcal R_{ef}(\mathbf z):=(\partial_eZ)(\partial_fZ)-Z\partial_e\partial_fZ\ge0.
\]

Indeed
\(\operatorname{Cov}(1_{e\in F},1_{f\in F})=-z_ez_f\mathcal R_{ef}/Z^2\).
The uniform forest version is the specialization z_e=1.

The more general random-cluster measure assigns weight
\(q^{k(A)}\prod_{e\in A}v_e\), with q in (0,1). Pairwise negative correlation
for all finite graphs and positive activities remains conjectural. Here k(A)
is the number of connected components, including isolated vertices.

The current primary paper Çiçeksiz–Ravichandran,
*Negative Correlations for Forests and the q<1 Random Cluster Model*,
https://arxiv.org/html/2610.00549v1 (submitted 30 September 2026), states these
conjectures, proves high-fugacity forest inequalities under a nonvanishing
condition, and proves a q<1 complete-graph result for sufficiently large edge
activities. Its crossing-minus-connectivity-covariance identity is prior art;
our independent derivation of that identity is not a new result.

Tang–Zhang https://arxiv.org/html/2609.11578v1 supplies another current statement
of the general random-cluster conjecture. Neither source gives the full result
proved below for all positive fugacities on the indicated bipartite families.

## Proved result A: homogeneous complete bipartite graphs of bounded width

**Theorem.** Let G=K_{m,s}, where 1<=m<=8 and s is any positive integer. Give
every edge a common activity lambda>0. Every pair of distinct forest edge
indicators is negatively correlated. The correlation is strict when m,s>=2;
it is zero for m=1 or s=1, since then G is a tree.

This is a finite exact symbolic certificate proving infinitely many graphs and
all positive real lambda, not a finite numerical parameter check. Its restriction
m<=8 is essential to the present proof.

### The transfer argument

Call the m-side vertices terminals, and process the s other vertices as hubs.
A state is a partition pi of the terminals by forest connectivity. The initial
partition consists of m singletons. A new hub selects a subset S of terminals.
It produces a forest exactly when S meets each block of pi at most once. Its
weight is lambda^{|S|}, and the new partition merges the blocks met by S.
The rule remains valid for the empty subset, which creates an isolated hub.

Let T be the exact matrix of this transition. All states have the same diagonal
contribution
\(a=1+m\lambda\), coming from |S|=0 or 1. Thus T=aI+N, where N strictly
coarsens partitions and N^m=0. For an initial singleton row vector r and the
all-ones column vector 1,

\[
 Z=rT^s1=\sum_{k=0}^{m-1}\binom{s}{k}a^{s-k}rN^k1.
\]

For a marked edge joining terminal i to a distinguished hub, let U_i be the
transition sum over allowed S containing i, with weight lambda^{|S|-1}.
For two marked edges joining terminals i,j to the same hub, let V_{ij} have
weight lambda^{|S|-2} over allowed S containing both. These are exact edge
partial derivatives, rather than derivatives with respect to the common lambda.
One may process all unmarked hubs first and the distinguished hubs last, so

\[
\begin{aligned}
 A&=rT^{s-1}U_0 1,\\
 B_h&=rT^{s-1}V_{01}1,\\
 B_t&=rT^{s-2}U_0U_0 1,\\
 B_d&=rT^{s-2}U_0U_1 1.
\end{aligned}
\]

The three edge-pair types are: same hub; same terminal on different hubs; and
four distinct endpoints. By graph symmetry both single-edge derivatives equal
A, and their Rayleigh differences are A^2-ZB_h, A^2-ZB_t, A^2-ZB_d.
No assumption that the marked operators commute is needed.

Set t=s-2. For an operator O and shift c define

\[
 P_{O,c}(t,\lambda)=\sum_{k=0}^{m-1}
 \binom{t+c}{k}a^{m-1-k}rN^kO1.
\]

For Z use (O,c)=(I,2); for A use (U_0,1); for B_h use (V_{01},1);
and for B_t,B_d use (U_0U_0,0),(U_0U_1,0). Then all three Rayleigh
differences have the common positive normalization

\[
 \mathcal R_{\mathrm{type}}=a^{2s-2m}P_{\mathrm{type}}(t,\lambda),
\]

where

\[
\begin{aligned}
 P_h&=P_{U_0,1}^2-aP_{I,2}P_{V_{01},1},\\
 P_t&=P_{U_0,1}^2-P_{I,2}P_{U_0U_0,0},\\
 P_d&=P_{U_0,1}^2-P_{I,2}P_{U_0U_1,0}.
\end{aligned}
\]

These are finite polynomials with rational coefficients. Expanding them in the
Newton basis gives

\[
 P_{\mathrm{type}}(t,\lambda)=\sum_{k,j}c_{k,j}\binom{t}{k}\lambda^j.
\]

The saved exact certificates show c_{k,j}>=0 for every type and 2<=m<=8, and
at least one coefficient c_{0,j} is strictly positive for every type. Since
t is a nonnegative integer, binomial(t,k)>=0. Thus P_type>0 for every lambda>0.
This proves the theorem for m,s>=2. The two tree cases follow separately.

The normalization is allowed to have a negative integer exponent when s<m;
it is strictly positive, and the exact formula is still valid.

### Certificate inventory

| m | Partition states | Degree in t, same hub | Degree in t, other types | Maximum lambda degree |
|---|---:|---:|---:|---:|
|2|2|2|0|4|
|3|5|4|2|8|
|4|15|6|4|12|
|5|52|8|6|16|
|6|203|10|8|20|
|7|877|12|10|24|
|8|4140|14|12|28|

`complete_bipartite_symbolic.py` implements the preceding derivation using only
Python integer and Fraction arithmetic. The data files
`complete_bipartite_symbolic_results_2.json`,
`complete_bipartite_symbolic_results.json` (m=3,...,6), and
`complete_bipartite_symbolic_results_7_8.json` contain every nonzero coefficient.
All coefficients are represented as exact rational strings.

`complete_bipartite_direct_audit.py` is independent of the transfer construction:
it directly enumerates edge subsets, rejects cycles using union-find, evaluates
the three edge partial derivatives, and compares Rayleigh differences with the
saved certificates. It passed 20 graph/activity cases, hence 60 pair-type
comparisons, on (m,s)=(3,2),(3,3),(4,2),(4,3),(5,2),(5,3),(6,2),(6,3),(7,2),(8,2)
at lambda=1,2. The associated JSON records every exact value. The coefficient
checks cover all 18 saved certificates for m=3,...,8. The additional m=2
certificate has been derived separately and contains only 13 positive terms.

### Prior art and the unproved extension

Dudley Stark, *The asymptotic number of spanning forests of complete bipartite
labelled graphs*, Discrete Mathematics 313 (2013), 1256–1261,
DOI https://doi.org/10.1016/j.disc.2012.10.026,
https://www.researchgate.net/publication/256694176_The_asymptotic_number_of_spanning_forests_of_complete_bipartite_labelled_graphs
(author-uploaded primary full text), proves adjacent-edge negative correlation
for uniform forests in an asymptotic range with both sides growing. Theorem 3
requires m→infinity, m<=n, and n=o(m^{8/7}), and the article explicitly leaves
nonadjacent edge pairs unverified. This does not subsume fixed m<=8, unbounded s,
all positive lambda, or all edge-pair types.

Targeted literature searches did not locate the all-fugacity finite-width
statement. That is not a certificate of novelty. The proof may overlap older
results on Rayleigh matroids or graph decompositions; in particular m=2 is a
known series-parallel case. No novelty claim should be made without additional
specialist or literature review.

The conjectural extension is that the same Newton coefficients are nonnegative
for every m>=2. The present argument has **not** proved that assertion. A formula
or combinatorial interpretation for c_{k,j} valid in arbitrary m would turn this
certificate method into a theorem for every homogeneous complete bipartite graph.
Merely running larger values of m would extend a bound, not solve the infinite
case or the general graph conjecture.

## Proved result B: a short heterogeneous positive formula

Let G_s have four terminals 0,1,2,3 and s hubs joined to every terminal. Add
marked matching edges e=01 and f=23. At hub j, all four incident edges have a
common activity x_j>=0, with no requirement that different hubs have the same
activity. The marked edge activities are arbitrary.

Put a_j=1+4x_j. The forest polynomial has the form
\(Z=A+z_eB+z_fB+z_ez_fD\). Its Rayleigh difference is independent of the
marked activities and satisfies the exact identity

\[
\begin{aligned}
\mathcal R_{ef}={}&\sum_{i<j}4x_i^2x_j^2(1+x_i+x_j)^2
 \prod_{\ell\notin\{i,j\}}a_\ell^2\\
&+\sum_{i<j<k}8x_i^2x_j^2x_k^2
 (a_ia_j+a_ia_k+a_ja_k)
 \prod_{\ell\notin\{i,j,k\}}a_\ell^2.
\end{aligned}
\]

Every coefficient is nonnegative. The marked indicators are strictly negatively
correlated if their activities are positive and at least two x_j are positive.
For x_j=lambda and s>=2 this simplifies to

\[
 \mathcal R_{ef}=2s(s-1)\lambda^4(1+4\lambda)^{2s-4}
 (1+4\lambda+2s\lambda^2).
\]

A full short symbolic proof, based on the five terminal-partition shapes, is in
`../forest_twin_matching_proof.md`. The child derivation has been independently
checked by `twin_matching_independent_audit.py`, which enumerates hub-edge subsets
and tests whether adding e, f, or both creates a cycle. Nine exact tests passed,
including unequal rational x_j, zero activities, and s=0,...,4. The corresponding
JSON contains exact values. A separate child implementation also passed 14 checks.

For s>=3 the graph is 3-connected. With common activities, the leading two
high-fugacity coefficients H_0,H_1 vanish by the equipotential equality criterion
in the September 30 paper, but this identity gives
\(H_2=4^{2s-3}s^2(s-1)>0\). Thus it proves a concrete infinite family of cases
outside that paper's nonvanishing hypothesis. It still does not prove the
high-fugacity conjecture on every graph.

## Random-cluster coefficient searches: observations, not proofs

`coefficient_search.py` tests a stronger coefficient-sign route for a common
edge activity. Using the convention q^{k(A)}lambda^{|A|}, form the indicator-mass difference M_e M_f-Z M_{ef} as a polynomial in q
(this is lambda^2 times the edge-derivative Rayleigh difference), divide out its
known (1-q) factor, and inspect
coefficient signs. Exact tests on 83 graphs (K_5,K_6,K_{3,3}, and 80 seeded
random graphs on 7–10 vertices with 12–15 edges) at lambda=1/10,1/2,1,2,10
covered 34,930 edge-pair/activity combinations; no negative coefficient was found.
The saved JSON records graph parameters and results.

This is suggestive only. It does not establish coefficient positivity for all
lambda, all graphs, or arbitrary edge activities. Nor is it a disproof search
with any meaningful exhaustive coverage of the general conjecture. Earlier
exact numerical checks at three (p,q) points on 32 graphs likewise found no
counterexample and supply no universal conclusion.

## Honest completion boundary

The two partial forest theorems above have exact derivations and independent
finite checks. The general forest negative-correlation conjecture and the
q<1 random-cluster negative-correlation conjecture remain unsolved by this work.
The finite-width family, heterogeneous exceptional family, and stronger
coefficient conjecture are concrete research leads, not a substitute for a
complete solution of a famous open problem.
