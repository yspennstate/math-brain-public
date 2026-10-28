# P0208: the wreath graph and Aldous–Fill Problem 7.27

Scope: the graph is an established construction. The question is from 1994 and whether it is still open has not been verified.

Primary question: Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, 2002 unfinished monograph, 2014 recompilation, Open Problem 7.27, PDF p.259, https://www.stat.berkeley.edu/~aldous/RWG/book.pdf . Section 7.2 is internally dated January 31, 1994. It asks, for arc-transitive graphs other than cycles on n vertices, whether maximal mean commute time is O(n log n), relaxation time is O(n), and the ratio of maximal commute time to twice stationary-average hitting time tends to one. The three assertions are counted as one related question.

## Source scope and a printed definition error

Page 254 prints an inconsistent variable assignment in the definition of arc-transitivity: the images of two possible identical starting vertices would be allowed to be distinct. Read literally, that formula excludes any graph with a vertex having two neighbors. The surrounding discussion, examples of tori and Cayley graphs, and Lemma 7.19 unmistakably use the usual definition: the automorphism group is transitive on ordered adjacent pairs. Our result concerns that intended standard definition, and does not silently claim to satisfy the misprinted formula.

Conder's 2013 Rogla summer-school notes, p.8, independently describe the same established wreath/necklace graph and its arc-transitivity: https://www.famnit.upr.si/sl/resources/files/konference/rogla2013/conderlecturenotes.pdf . This is evidence that the construction is prior art. It does not establish when the probability question was answered.

## Construction and symmetry

Let m be an odd integer at least five, and put

\[
 V_m=(\mathbb Z/m\mathbb Z)\times\{0,1\},\qquad
 (i,b)\sim(i+1,c),\ (i,b)\sim(i-1,c)\quad(c=0,1).
\]

This is the lexicographic product of a cycle with an edgeless two-vertex graph. It is connected, simple, 4-regular, and has n=2m vertices, so it is not an n-cycle. Dihedral symmetries act on the first coordinate. Independently swapping the two vertices in any fiber preserves every edge. Given two directed edges, a dihedral symmetry sends their ordered base edges to each other, after which independent swaps in the two distinct endpoint fibers match both second coordinates. Thus the graph is arc-transitive.

Use discrete-time simple random walk, or its rate-one continuization. The book states on p.115 that the parameters at issue are unchanged by this continuization. The first-coordinate projection is simple random walk on the m-cycle, and the second coordinate is replaced at each step by a fresh fair bit independent of the base step.

## Exact hitting times

Write h(v,w) for the mean first hitting time, with h(w,w)=0. From a base position at cyclic distance j in {1,...,m-1}, the mean first arrival at base fiber zero is

\[
 H_j=j(m-j).
\]

Indeed H_0=H_m=0 and H_j=1+(H_{j-1}+H_{j+1})/2. At the first fiber arrival, the fair bit hits a specified vertex with probability one half.

Let h be the mean hitting time from its twin to the specified vertex. Starting in that fiber, the first positive return of the base walk has mean m. The arrival bit succeeds with probability one half; on failure the same twin state recurs. Hence h=m+h/2, giving h=2m. Therefore

\[
 h((j,b),(0,0))=j(m-j)+m\quad(j\ne0),\qquad
 h((0,1),(0,0))=2m.
\]

The formula is symmetric in source and target and gives 2m-1=n-1 for neighboring vertices, exactly as Lemma 7.19 requires. Its maximum is floor(m²/4)+m for m at least five. Thus

\[
 \tau^*=2\lfloor m^2/4\rfloor+2m.
\]

The stationary law is uniform. Summing the same hitting-time formula gives

\[
 \tau_0=\frac1{2m}\left[2m+2\sum_{j=1}^{m-1}
          \{j(m-j)+m\}\right]
       =\frac{m^2-1}{6}+m.
\]

On a vertex-transitive graph the stationary mean to a fixed target equals the source's stationary-average target parameter, so either equivalent convention yields this value.

## Independent spectral route

For functions constant on each two-vertex fiber, the transition operator is the cycle operator, with eigenvalues cos(2πk/m), k=0,...,m-1. For functions antisymmetric within every fiber it is zero. These orthogonal invariant subspaces both have dimension m and exhaust the state space. Consequently

\[
 \tau_2=\frac1{1-\cos(2\pi/m)}\sim\frac{m^2}{2\pi^2}.
\]

The fundamental-matrix trace is

\[
 \sum_{k=1}^{m-1}\frac1{1-\cos(2\pi k/m)}+m
 =\frac{m^2-1}{6}+m,
\]

which agrees with the direct hitting-time sum. The trigonometric sum can also be recovered from the already derived cycle hitting-time formula by stationary averaging; it is not needed as an unproved numerical identity for the counterexample.

## Consequences and limitations

Since n=2m, both τ* and τ2 are of order n². They violate the proposed n log n and n upper bounds. Moreover

\[
 \frac{\tau^*}{2\tau_0}
 =\frac{\lfloor m^2/4\rfloor+m}{(m^2-1)/6+m}
 \longrightarrow\frac32,
\]

which violates the third assertion. These are exact formulas, not simulation estimates.

The strongest reasons for caution are the old unfinished source, its definition typo, and the fact that wreath graphs have long been standard. Focused searches on September 6, 2026 located the original question and primary graph-theory descriptions but no verified later disposition of Problem 7.27. Absence from that search is not evidence of novelty. A future reviewer should check the intended arc-transitivity convention, rate-one normalization, and prior probability literature before any promotion.
