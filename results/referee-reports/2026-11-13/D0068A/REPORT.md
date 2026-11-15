PARTIAL

# D0068: the ordinary connective-constant limit on a Bernoulli cluster

For Bernoulli bond percolation on Z² with p>1/2, write I for its unique infinite cluster and σ_n(v) for the number of n-step self-avoiding walks from v in I. The problem asks whether

    μ(v) = lim_{n→∞} σ_n(v)^(1/n)

exists almost surely on {v∈I}, and whether μ(v)=μ(w) almost surely on {v,w∈I}. I read Question 1.4 in Grimmett–Li, *Self-avoiding walks and connective constants*, §1.3, printed/PDF p. 7; the setup begins on p. 6. The full page-labelled source is [saved as text](sources/grimmett_li_2017.txt). The mathematical statement above preserves both parts and the conditioning of the question.

The literature checked proves that the **limsup**, U(p), is deterministic and the same at every vertex of I. The ordinary limit is expressly conjectural in Lacoin's Remark 1.2, and no subsequent theorem resolving it was located in this audit through 13 November 2026. A 31 August 2026 primary seminar abstract still describes the Bernoulli case as ongoing work. This is a bounded negative literature finding, not a guarantee about every unindexed manuscript. Accordingly this report is PARTIAL, not RESOLVED_IN_LITERATURE.

The complete proofs below give, simultaneously for all v∈I,

    2p ≤ L(v) := liminf_n σ_n(v)^(1/n)
       ≤ limsup_n σ_n(v)^(1/n) = U(p) ≤ p μ₀,

where μ₀=μ(Z²). Lacoin's Theorem 1.4 strengthens the last inequality to U(p)<pμ₀ when p<1. The elementary 2p lower bound is obtained by thinning; no originality claim is made for it. The proofs also explain finite-change invariance, conditional annealed growth, bounds on conditional expected logarithms, and the geometry of possible oscillations. An explicit deterministic Z² example has no limit, but is **not translation invariant** and is not a counterexample to the question.

If ordinary limits exist at v and w in the same realization, they automatically agree, since both equal the already common limsup U(p). The outstanding part is existence. Individual constancy of L(v), convergence in probability, existence of lim_n E[log σ_n(0)|0∈I]/n, and existence for any interval p₀<p<1 are not proved here. The case p=1 is the classical full-lattice theorem.

## Why Fekete does not settle the question

On a fixed cluster, decomposing each (m+n)-step walk after m steps gives only

    σ_{m+n}(v) ≤ Σ_{γ: m-step SAW from v} σ_n(γ_m).

The continuation counts depend on the endpoint and on the same environment that selected the prefix. There is no replacement of σ_n(γ_m) by σ_n(v), and a continuation must also avoid the prefix. Already a leaf v next to a degree-four vertex has σ_1(v)=1 and σ_2(v)=3. Thus fixed-root submultiplicativity can fail even at m=n=1. Such finite local arrangements are compatible with a supercritical cluster.

Taking a supremum over **all** roots restores a submultiplicative bound, but gives the wrong constant: almost surely sup_{v∈I} σ_n(v)=s_n, the undiluted-lattice count, for every fixed n (proved below). Its limiting rate is μ₀, whereas U(p)<pμ₀<μ₀ for p<1. A random endpoint shift is not a fixed measure-preserving shift satisfying the hypotheses of Kingman's theorem. Conditioning the origin to lie in I does not restore independence.

Tail triviality and translation ergodicity answer whether a cluster-wide asymptotic quantity is random. They do not compare a liminf with a limsup. The convolution proof for the limsup below is precisely where taking a liminf would be invalid.

Possible failure would involve exponentially many finite walks available at some scales but inadequate growth at later scales. Long corridors and favorable distant regions are useful mechanisms to test, not established failure mechanisms for iid percolation. Part 6 below rules out macroscopic literal degree-two corridors near a root. A prescribed fully open ℓ-by-ℓ square has probability p^{2ℓ(ℓ+1)}; a union bound over O(R²) positions and Borel–Cantelli show that every such square whose lower-left corner lies within distance R has side O(sqrt(log R)) eventually. Its finite SAW capacity is O(log R) vertices. Thus arbitrarily large fully open squares somewhere in the plane are insufficient by themselves: one must account for distance, usable walk length, connecting paths, and the frequency of successive favorable regions. More general correlated path traps and anomalous growth regions are not excluded by these elementary bounds.

## Proofs

Standard inputs: the existence of the square-lattice connective constant μ₀;
the Bernoulli bond threshold p_c(Z²)=1/2; almost-sure uniqueness of the
supercritical infinite cluster; Harris association for independent Bernoulli
coordinates; and translation ergodicity of product measure. The proofs below
do not assume the unproved quenched ordinary limit. They are elementary
consequences, not claims of new literature priority.

### 1. Root-independent limsup on any bounded-degree connected graph

Write c_n(x) for rooted counts, c_0(x)=1, and U(x)=limsup c_n(x)^(1/n).
On an infinite locally finite connected graph there is an infinite simple ray
from each vertex (take a branch of the finitely branching tree of finite
simple paths), so c_n(x)≥1. If maximum degree is Δ, c_n(x)≤Δ(Δ−1)^(n−1).

For adjacent x,y split n-step paths from x into those avoiding y and those
first visiting y at time k. Prepending y gives an injection of the avoiding
paths into (n+1)-step paths from y. Reversal bounds the number of k-step
x-to-y prefixes by c_k(y). Ignoring mutual avoidance of prefix and suffix,

    c_n(x) ≤ c_{n+1}(y) + Σ_{k=1}^n c_k(y)c_{n−k}(y).             (1)

For any a>U(y), there is C<∞ with c_j(y)≤Ca^j for all j≥0.
The right-hand side of (1) is at most Ca^(n+1)+nC²a^n. Its nth-root
limsup is at most a. Let a↓U(y) and interchange x,y to obtain equality.
Connectedness extends equality to all vertices. Denote the common value U(G).

For the percolation cluster I, U(I) is translation invariant: translating
the environment translates the unique cluster and merely changes its root.
Ergodicity therefore makes U(I)=U(p) deterministic, simultaneously at all
v∈I. Measurability follows from local finite counts and a countable root
selection, e.g. the first cluster vertex in a fixed enumeration of Z².

The alternative tail proof uses finite changes. Adding a leaf preserves
U by counting at its attachment vertex for n≥2. Adding an edge (a,b)
inside a connected graph gives, when counting at a,

    c_n(a) ≤ c'_n(a) ≤ c_n(a)+c_{n−1}(b),

because a simple path can use the new edge only at its first step. Thus U
is unchanged. Every finite connected attachment can be built using leaves
and internal edges, so it also preserves U. For p∈(1/2,1), take the
probability-one set on which uniqueness holds after every finite edge flip;
it has probability one by finite energy and countability of finite flips.
A finite alteration then changes the infinite cluster by finitely many
edges/vertices: deletion produces only finitely many components, of which
one is infinite and all others finite; addition joins only finitely many
finite components. Compare both clusters through their union to use the
finite-attachment argument. U is consequently a tail variable and is
deterministic by Kolmogorov's zero-one law. At p=1 the graph is deterministic.

This establishes U, not any limit of c_n^(1/n). Inequality (1) is an upper
bound on a convolution; taking liminf does not turn it into an inequality
between the individual liminfs.

### 2. Simultaneous lower bound on liminf by thinning

Fix p>1/2 and a deterministic q∈(1/(2p),1). Sample ω at density p and,
independently, η at density q; retain an edge iff ω_eη_e=1. This is iid
bond percolation of density pq>1/2, hence has an infinite component a.s.
By Fubini, for almost every ω, independent q-thinning has some infinite
component with conditional probability one. All such infinite components
are subsets of the original unique I(ω).

For a fixed such ω, put t_q^ω(u)=P_η(u belongs to an infinite retained
component). Some u∈I has t_q^ω(u)>0, since the event that some vertex
percolates is the countable union of the events for individual vertices.
For any v∈I choose an open finite path π from v to u of length d.
The event that π is retained and the event that u percolates are increasing
in η. Harris association gives

    t_q^ω(v) ≥ q^d t_q^ω(u)>0.                                  (2)

Indeed, on their intersection v and u lie in the same infinite retained
component. The presence of any infinite retained path from v implies an
open retained simple path of each length n. A union bound, conditional
on ω, over the c_n(v) candidate paths gives

    0<t_q^ω(v) ≤ q^n c_n(v),  for every n≥1.                     (3)

Taking nth roots and liminf yields liminf c_n(v)^(1/n)≥1/q for every
v∈I on the same full-measure set. Intersect over a countable sequence
q↓1/(2p). Thus, simultaneously for every v∈I,

    liminf c_n(v)^(1/n) ≥ 2p.                                  (4)

The proof also identifies the independent bond-percolation threshold of
the fixed random graph I as 1/(2p), a.s.: for q below it, the product
configuration has no infinite component and the converse Fubini argument
applies. Use rational q on both sides; no claim at equality is needed.

Harris association here is for the *unconditioned thinning coordinates*
after ω is fixed. There is no assertion that conditioning on membership
in I leaves the original edges independent.

### 3. Annealed rate with the correct conditioning, and log-mean bounds

Let A={0∈I}, θ=P_p(A)>0, and let Z_n count open n-step SAWs from 0 in
the full percolation configuration, even when its cluster is finite.
Then E Z_n=p^n s_n, where s_n is the full-lattice count. Both Z_n and
1_A are increasing. By Harris and the trivial indicator bound,

    p^n s_n ≤ E[Z_n|A] ≤ p^n s_n/θ.                            (5)

Consequently (E[Z_n|A])^(1/n)→pμ₀. This is a conditional ANNEALED
statement, not convergence of the random nth roots.

Put X_n=(log Z_n)/n on the probability space conditioned on A.
Then 0≤X_n≤log 4. Part 2 gives liminf X_n≥log(2p), while Part 1
gives limsup X_n=log U(p). Fatou and reverse Fatou imply

    log(2p) ≤ liminf E[X_n|A] ≤ limsup E[X_n|A] ≤ log U(p).      (6)

In two dimensions Lacoin's strict-gap theorem gives U(p)<pμ₀ for p<1.
Hence the upper bound in (6) is strictly below log(pμ₀). Nothing in
(5) or (6) asserts that E[X_n|A] itself converges.

### 4. All subsequential values form an interval

On any infinite graph of maximum degree four, deleting the last edge
shows c_{n+1}(v)≤3c_n(v) for n≥1. Thus for X_n=log c_n(v)/n,

    X_{n+1}−X_n ≤ log 3/(n+1),

since X_n≥0. Let l=liminf X_n and u=limsup X_n. Each endpoint is a
subsequential limit by boundedness. For l<t<u there are arbitrarily late
indices with X_n<t and subsequent indices with X_n≥t. At the first
upward crossing j, t≤X_j≤t+log 3/j. Taking such crossings with j→∞
gives a subsequence converging to t. No other limit points can lie outside
[l,u]. Exponentiating, the limit-point set of c_n(v)^(1/n) is exactly
[liminf c_n(v)^(1/n), U(G)].

For a fixed environment and root, subsequences realizing either endpoint
can be selected as the first later index within 1/k of that endpoint;
these are measurable environment-dependent indices. This gives neither
a predetermined subsequence converging in probability to U(p) nor a
common subsequence for all roots. It is not a solution to D0068.

### 5. Uniform annealed upper bounds versus a supremum over all roots

For a fixed A₀>0 and b>pμ₀, choose ε>0 so p(μ₀+ε)<b.
For sufficiently large n, s_n≤(μ₀+ε)^n. A union bound and Markov give

 P(max_{x∈[−n^A₀,n^A₀]²} Z_n(x) ≥ b^n)
   ≤ (2 floor(n^A₀)+1)² [p(μ₀+ε)/b]^n.

This is summable. By Borel–Cantelli, the maximum over any polynomial
window has eventual nth-root upper bound b. Intersecting over rational
b>pμ₀ gives upper limsup at most pμ₀. This does not improve to U(p):
the latter would require a quantitative upper-deviation bound at that rate.

In contrast, for each fixed n, almost surely

    sup_{v∈I} c_n(v)=s_n.                                     (7)

To prove it, the event that all edges of a square [−n,n]² are open and
0∈I has positive probability by Harris. Translation ergodicity implies
that such an event occurs at some translate almost surely: the event that
it occurs somewhere is invariant and has positive probability, hence
probability one. At its center all lattice n-step SAWs are open. The
reverse inequality is automatic; intersect over n. Thus taking a supremum
over all roots restores submultiplicativity but yields μ₀, whereas the
typical-root limsup is U(p)<pμ₀<μ₀ for 1/2<p<1.

### 6. Literal degree-two corridors have only logarithmic length nearby

Fix p∈(1/2,1). A corridor of length L is an open simple path of L edges
whose L−1 internal vertices have open degree exactly two. For a fixed
candidate path, its internal vertices require 2(L−1) incidences of closed
off-path edges. Each edge is counted at most twice, so at least L−1
distinct closed edges are specified, disjoint from its L open edges.
The probability is at most p^L(1−p)^(L−1). There are at most
4·3^(L−1) candidate paths from each start. Therefore, writing
ρ=3p(1−p)<1,

 P(a corridor of length ≥m starts in [−R,R]²)
   ≤ (2R+1)² [4/(3(1−p))] ρ^m/(1−ρ).                       (8)

Choose K>3/|log ρ| and m=ceil(K log R). The bound is summable over
integer R≥2, so Borel–Cantelli gives the almost-sure eventual bound
L<K log R+1 for any such corridor starting in that box. Endpoints and
intermediate path vertices were not required to stay in the box.
This excludes length-proportional-to-distance literal degree-two corridors
as the simple explanation of a failure of convergence. It says nothing
about broader sparse regions, visited-vertex traps, or chemical detours.

### 7. A deterministic Z² example with no limit (not stationary)

Let a_k=(k,k), h_k=(k+1,k), t_k=(k,k+1), for k≥0. Always retain
the two edges a_k−h_k−a_{k+1}. If b_k=1 also retain the other two
edges a_k−t_k−a_{k+1}; if b_k=0 omit them. This is a connected,
one-ended, degree-at-most-four subgraph of Z², a series of squares and
two-edge corridors. Other lattice vertices can be left isolated.
Put B_m=Σ_{k=0}^{m−1}b_k, with b_{−1}=0. Direct classification gives

    c_{2m}(a_0)=2^B_m,
    c_{2m+1}(a_0)=2^B_m(1+b_m+b_{m−1}).                       (9)

Here a path crosses each completed cell along one of its retained arcs.
At an articulation it may move one edge backwards along the unused arc
of the preceding square, but it is then trapped at that arc's midpoint.
These are the only alternatives. Even paths end at a_m; odd paths
either take a forward half-arc (1+b_m choices) or the one unused backward
half-arc when b_{m−1}=1. This proves both formulas, including m=0.

Choose block endpoints N_j=2^(2^j), j≥0. Set b_k=1 on [0,N_0),
and on each [N_{j−1},N_j) set b_k=1 when j is even and 0 when j is
odd. At endpoints of zero blocks B_{N_j}/N_j≤N_{j−1}/N_j→0;
at endpoints of one blocks B_{N_j}/N_j≥1−N_{j−1}/N_j→1.
Since 0≤B_m/m≤1, (9) yields

    liminf c_n(a_0)^(1/n)=1,   limsup c_n(a_0)^(1/n)=sqrt(2).

This verifies an obstruction even for a one-ended planar graph with
polynomial ambient volume. It is NOT a translation-invariant random
graph and is NOT a counterexample to D0068 or to its stationary variant.
A uniform random integer translate of this exceptional sequence/strip is
not a probability distribution. No such stationarization is claimed.

### 8. What is still missing

No argument here proves that L(v)=liminf c_n(v)^(1/n) is constant across
vertices or deterministic individually. Ergodicity does make inf_{v∈I}L(v)
and sup_{v∈I}L(v) deterministic, since these are measurable invariant
quantities (test rational levels and use countability). It does not imply
equality. A stationary random field need not have constant value at all
its vertices. Nor has full convergence in probability, convergence of
E[log c_n(0)|0∈I]/n, a p<1 high-density interval of almost-sure convergence,
or a stationary random-subgraph counterexample been proved here.

## Exact enumeration: evidence only

The computation sampled bond configurations in [−128,128]². The origin component had to reach all four faces; three independently seeded configurations were accepted at each p, and counts were taken at (0,0), (8,0), and (0,8). All nine initial draws passed, so no seed was rejected. The program would otherwise record the rejection and choose the next seed. These root neighborhoods overlap, so the nine roots per density are not nine independent environments.

The four-face condition is a finite proxy for membership in I. It cannot certify infinite-cluster membership. Every root is at least 120 lattice steps from the boundary, exceeding the largest enumerated length 28. Consequently the counts are exact for every completion of the sampled edges outside the box, although the interpretation as walks on an actual infinite cluster remains a sampling proxy. There is no wraparound or truncation of walks at the enumerated lengths.

The table gives minimum / median / maximum of σ_n(v)^(1/n) over the nine roots for each density. It shows substantial finite-length corrections and root variation; it cannot distinguish equality from a strict gap between asymptotic liminf and limsup.

| p | n | Minimum | Median | Maximum |
|---:|---:|---:|---:|---:|
| 0.60 | 10 | 1.513331 | 1.761117 | 1.928626 |
| 0.60 | 15 | 1.439034 | 1.725638 | 1.820610 |
| 0.60 | 20 | 1.442942 | 1.702921 | 1.755027 |
| 0.60 | 28 | 1.485156 | 1.670633 | 1.709385 |
| 0.75 | 10 | 1.966307 | 2.122321 | 2.345588 |
| 0.75 | 15 | 1.984452 | 2.053168 | 2.216892 |
| 0.75 | 20 | 1.974344 | 2.030368 | 2.168805 |
| 0.75 | 24 | 1.956832 | 2.026851 | 2.151145 |
| 0.90 | 10 | 2.578780 | 2.659604 | 2.720906 |
| 0.90 | 15 | 2.531097 | 2.572456 | 2.621140 |
| 0.90 | 20 | 2.502474 | 2.533301 | 2.573107 |
| 0.90 | 21 | 2.497861 | 2.527920 | 2.567267 |

At p=.6 in sample 1, the n=28 counts are 670,457, 1,811,482, and 64,509 at the three respective roots: a maximum/minimum count ratio of 28.0811. Their nth roots are much closer, illustrating how a large finite-count discrepancy can coexist with a common asymptotic upper rate. No asymptotic rate is fitted. Finite nth roots can exceed the asymptotic upper bound pμ₀ without contradicting that bound.

[Standalone plot](data/growth.svg). The plot contains generated numerical results, not source-paper images.

The exact enumerator is [code/enumerate.cpp](code/enumerate.cpp); independent verification is [code/verify.py](code/verify.py); summaries and plotting are in [code/summarize.py](code/summarize.py). [Reproduction instructions](code/README.md) explain sampling and file encoding. All edge bits, seeds, exact integer counts and timings are retained in data/. Main outputs are [counts.csv](data/counts.csv), [samples.csv](data/samples.csv), [summary.csv](data/summary.csv), and [verification.json](data/verification.json).

Validation used a separate breadth-first implementation that stores explicit path tuples, compared with the C++ depth-first implementation through n=10 at all 27 roots: 297 count comparisons passed. The full-lattice fixture was independently checked against 1,4,12,36,100,284,780,2172,5916,16268,44100,120292,324932 through n=12. All 128 seven-cell square/corridor patterns were enumerated through n=12, giving 1,664 successful comparisons with formula (9). All component-face, root-margin, integer upper-bound, degree and floating nth-root checks passed. Large-n integer counts were not independently re-enumerated by a second algorithm; their low-n prefixes and algorithmic invariants were checked.

The enumerator used one thread, inherited nice=10 (checked in the program), 3,801,088 bytes peak RSS on macOS, and 13.736571 seconds total DFS wall time. Verification and plotting were also single-threaded with numerical thread environment variables set to one; their small working sets were not separately profiled. The largest n depends on p because enumeration grows exponentially. These are deliberately finite computations, with no claim that longer enumeration could settle the limit question.

## Literature results, theorem numbers, and pages

Page numbers are for the actual version inspected. In particular, the accepted arXiv versions of the Lacoin papers have different pagination from the journal articles; journal theorem pages have not been guessed. The [detailed audit](sources/literature_audit.txt) records search terms, citation coverage, and access limitations.

| Source | Exact location inspected | Bearing on D0068 |
|---|---|---|
| [Grimmett–Li, 2017 survey](https://arxiv.org/abs/1704.05884) | §1.3, Question 1.4, printed/PDF p. 7; setup p. 6 | The question asks for the ordinary limit. Theorem 1.1, p. 3, requires quasi-transitivity. |
| [Lacoin, PTRF 159 (2014), 777–808](https://doi.org/10.1007/s00440-013-0520-1), [accepted arXiv v3](https://arxiv.org/pdf/1203.6051v3) | Proposition 1.1 and Remark 1.2, PDF p. 3; Theorem 1.4, p. 4; Lemmas 2.1, 2.3 and proof of Proposition 1.1, pp. 6–7 | Common deterministic limsup; ordinary limit conjectured; strict planar quenched/annealed gap. |
| [Lacoin, JSP 154 (2014), 1461–1482](https://doi.org/10.1007/s10955-014-0926-x), [arXiv v2](https://arxiv.org/pdf/1212.4641v2) | Proposition 1.1, PDF pp. 2–3; Theorem 1.3, p. 4 | Repeats limsup theorem; proves a high-dimensional non-averaging regime. |
| [Chino–Sakai, JSP 163 (2016), 754–764](https://arxiv.org/abs/1508.01262) | Theorem 1.1, arXiv PDF p. 4; finite-integrable-energy assumptions pp. 2–3 and proof p. 7 | Deterministic root-independent critical point; not an ordinary-count limit. Closed edges require infinite energy. |
| [Grimmett–Li, Weighted self-avoiding walks](https://doi.org/10.1007/s10801-019-00895-6), J. Algebraic Combinatorics 52 (2020), 77–102 | Theorem 2.1, journal p. 81 / PDF p. 5; Theorem 2.5, journal p. 83 / PDF p. 7 | Positive invariant weights on quasi-transitive graphs; graph-height/bridge results. Typical iid cluster realizations do not satisfy these hypotheses. |
| [Garet–Gouéré–Marchand, Ann. Probab. 45 (2017), 4071–4100](https://doi.org/10.1214/16-AOP1158) | Theorem 1.1, journal p. 4074 / PDF p. 4; discussion of undirected problem p. 4072 / PDF p. 2 | Full limit in oriented percolation. Authors explicitly distinguish the unresolved nonoriented problem. |
| [Chen–Shao–Shi, 2026](https://arxiv.org/abs/2604.02746) | Theorems 1.2 and 1.3, PDF p. 4 | Hard-core zero-freeness; no percolation SAW-growth limit. This is the identifiable Chen–Shao search hit, not an assumed correction to the requested authors. |
| [Le Doussal–Machta, JSP 64 (1991), 541–578](https://doi.org/10.1007/BF01048306) | Publisher abstract only; full text inaccessible here | Renormalization/Flory arguments and hierarchical-lattice results. No unverified theorem/page is attributed to it. |
| [UFRJ probability seminar, 31 August 2026](https://ppge.im.ufrj.br/seminarios-de-probabilidade-segundo-semestre-de-2026/) | Abstract of Bruno Kimura, joint with Sakai, Chino, Kitagawa; no theorem numbering or pages | Announces normalized-log convergence for finite conductances under LSI; Bernoulli-cluster extension described as ongoing research. A seminar is not an in-print resolution. |

The author publication lists of [Sakai](https://www.math.sci.hokudai.ac.jp/~sakai/) (updated 5 November 2026), [Lacoin](https://w3.impa.br/~lacoin/research.html), and [Duminil-Copin](https://www.ihes.fr/~duminil/publi.html) were checked through available primary pages. Sakai and Duminil-Copin lists are saved. No resolving Bernoulli-limit paper was identified. An OpenAlex citation query returned 13 planar-paper citers in the requested 2014–2026 period; it is demonstrably incomplete, because it omitted the Chen–Shao–Shi citation found in that paper. Neither an incomplete citation index nor the absence of a title in an author's list proves nonexistence of a later theorem.

The finite-conductance/LSI announcement is particularly relevant but cannot be passed to Bernoulli dilution by simply taking weights to zero: that would require uniform control justifying an interchange with n→∞, precisely the missing step. The oriented result has a separate structural advantage: directed paths can be concatenated across time without creating a self-intersection with their past.

## Scope and remaining gap

The proven results here are consequences and bounds, with complete proofs above, not a resolution of the open problem. There is no proof of L(v)=U(p), no proof of separate individual liminf constancy, no convergence-in-probability theorem for the full sequence, no conditional log-mean limit, and no translation-invariant random-subgraph counterexample. The environment-dependent subsequences in Part 4 are elementary consequences of boundedness and one-sided increment control and should not be mistaken for a predetermined subsequence theorem.

The saved deterministic example makes clear that connectedness, bounded degree, planarity, one end, and ambient polynomial volume alone do not suffice. The iid cluster has additional structure, as the thinning and corridor bounds demonstrate, but an argument matching its lower and upper exponential rates is still required.

Only this directory was written. Source papers were downloaded into memory and converted directly to plain text; no PDFs, page images, scans, or source-paper screenshots were stored. No subagents were used, and nothing was published or pushed. The required shared mesh registration was attempted but its database is read-only in this sandbox; the supplied directory-only restriction also prevents shared checklist/memory writes. Progress and that limitation are recorded in LOG.md.

Task: “Open problem D0068” — request received 13 November 2026, approximately 09:52 +04 (first local clock observation; exact message timestamp unavailable).
