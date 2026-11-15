PARTIAL

# C0083: Hamming-graph critical-point expansion

The intended statement is proved in the literature for dimensions 1–6. I did
not find a proof for general fixed dimension, a proved third coefficient for
fixed-dimensional Hamming graphs, or a theorem making all the coefficients
rational functions of the dimension. This investigation does not close those
gaps. It gives the normalization in powers of n, a precise obstruction to
transplanting the hypercube proof, a rigorous resummation of one class of local
cycles to the next order, and numerical checks. The resummation is not a
calculation of the third critical-point coefficient.

## Statement and conventions

Write H(d,n)=K_n^d for the Cartesian product, with vertex set {0,...,n−1}^d.
An unordered pair is an edge when its endpoints differ in exactly one
coordinate. Set

\[
 V=n^d,\qquad m=d(n-1),\qquad
 \chi(p)=\mathbb E_p|C(0)|=\sum_x\mathbb P_p(0\leftrightarrow x).
\]

The finite-graph definition in the lecture notes, equation (13.3.1), is

\[
 \chi(p_c(H(d,n);\lambda))=\lambda V^{1/3}.
 \tag{1}
\]

Here lambda is fixed and positive; it is the multiplier of susceptibility,
not the expected open degree or the additive parameter in an Erdős–Rényi
scaling window. Existence in (0,1) requires 1<lambda V^(1/3)<V, which holds
eventually for fixed lambda. The solution is unique: chi is a polynomial,
continuous and strictly increasing from 1 to V. Strict increase follows,
for example, by coupling all edge states with uniforms and considering the
positive-probability event that a particular edge incident to 0 changes state
while all other edges are closed. The triangle-condition arguments use a
small positive lambda; Theorem 1.1 of the expansion paper is stated for every
fixed positive susceptibility multiplier, denoted theta there.

There are two source issues that matter mathematically. The supplied
[arXiv:1510.03221](https://arxiv.org/abs/1510.03221) is a CR geometry paper,
not the lecture notes. I read the relevant text of the
[author's lecture-notes version](https://www.win.tue.nl/~rhofstad/survey-high-d-percolation.pdf)
through text extraction, including Open Problem 15.10, (15.5.7), and its
surrounding discussion. I did not download a local book PDF or request any
page rendering. The lecture-notes pagination differs from the published
book's p. 233.

The displayed upper summation index in (15.5.7) is d/3. Its surrounding prose
says that two terms settle d=4,5,6 and that the third term matters from d=7.
The precise summation range consistent with that prose and the specified
error is

\[
 J(d)=\lceil d/3\rceil,\qquad
 p_c=\sum_{i=1}^{J(d)}a_i(d)n^{-i}+O(n^{-1-d/3}).
 \tag{2}
\]

Indeed the retained integers satisfy i<1+d/3. If the displayed d/3 is instead
interpreted literally as floor(d/3), the formula is false for d=4,5: the
nonzero second-order term is then missing. For d=4, the result below implies

\[
 n^2\left(p_c-\frac1{4n}\right)\longrightarrow\frac{103}{288}>0,
\]

whereas a one-term expansion with O(n^(−7/3)) would force this limit to zero.
This is a counterexample to that literal truncation, not a resolution of the
intended open problem. The source also writes the degree-expansion second
coefficient beside an expansion in n; the conversion below fixes this. Neither
typographical issue is being used to claim a new solution.

## What is proved in print

Federico, van der Hofstad, den Hollander and Hulshof,
*Expansion of percolation critical points for Hamming graphs*,
Combinatorics, Probability and Computing **29** (2020), 68–100,
[DOI 10.1017/S0963548319000208](https://doi.org/10.1017/S0963548319000208),
[arXiv:1701.02099](https://arxiv.org/abs/1701.02099), **Theorem 1.1**, prove

\[
 p_c(H(d,n);\lambda)
 =\frac1m+\frac{A(d)}{m^2}
   +O(m^{-3})+O(m^{-1}V^{-1/3}),\qquad
 A(d)=\frac{2d^2-1}{2(d-1)^2},\quad d\ge2.
 \tag{3}
\]

Only two nonzero coefficients are established. The remainder has two parts;
dropping O(m^(−3)) for d>6 would strengthen the theorem without justification.
The paper's **Proposition 5.1** estimates the lace coefficients to the order
needed for (3). Its **Theorem 1.2** gives a refined subcritical Erdős–Rényi
susceptibility expansion. Section 1.4 explicitly discusses the higher-order
Hamming expansion as conjectural and explains why the fixed-subgraph argument
from the hypercube is unavailable. It does not prove rationality of higher
Hamming coefficients, even as numbers at each fixed integer d. Rational
functions of d would be a stronger claim still.

Here are the other load-bearing references, with their roles kept separate.

| Reference | Exact result used or checked | Scope |
|---|---|---|
| Borgs, Chayes, van der Hofstad, Slade, Spencer, *Random subgraphs of finite graphs I*, RSA **27** (2005), 137–184, [arXiv:math/0401069](https://arxiv.org/abs/math/0401069) | Theorem 1.1, threshold and comparison of susceptibility parameters; Theorems 1.2–1.3, subcritical/window behavior | Baseline location and finite-size window, not higher Hamming coefficients |
| Same authors, *II. The lace expansion and the triangle condition*, Ann. Probab. **33** (2005), 1886–1944, [arXiv:math/0401070](https://arxiv.org/abs/math/0401070) | Theorem 1.3, triangle condition for the graph examples | Applies to Hamming graphs; supports the baseline expansion |
| van der Hofstad–Slade, *Asymptotic expansions in n^(−1) for percolation critical values on the n-cube and Z^n*, RSA **27** (2005), 331–357, [arXiv:math/0401073](https://arxiv.org/abs/math/0401073) | Published Theorems 1.1 and 1.2, respectively lattice and hypercube; Proposition 2.1, polynomial approximation of Pi | All orders with rational numerical coefficients as dimension tends to infinity |
| van der Hofstad–Slade, *Expansion in n^(−1) ...: the first three terms*, CPC **15** (2006), 695–713, [arXiv:math/0401072](https://arxiv.org/abs/math/0401072) | Theorem 1.1 | Omega^(−1)+Omega^(−2)+(7/2)Omega^(−3)+O(Omega^(−4)), for hypercube and lattice |
| van der Hofstad–Łuczak, *Random subgraphs of the 2D Hamming graph: the supercritical phase*, PTRF **147** (2010), 1–41, [arXiv:0801.1607](https://arxiv.org/abs/0801.1607) | Theorem 1.1 | Barely supercritical giant, not a third critical-point coefficient |

The all-orders paper's arXiv v1 combines its two main claims as Theorem
1.1(i),(ii). The published numbering above was checked against the author's
revised text. Its polynomial approximation is
Pi=sum alpha_(j,i,M) Omega^j p^i+O(Omega^(−M−1)), with a finite sum and
rational alpha independent of dimension. This is the part that cannot simply
be asserted for a fixed-dimensional Hamming graph with growing alphabet.

The four-author companion *The scaling limit for critical percolation on
the Hamming graph* is cited as in preparation (2016) in the expansion paper
and remains in preparation in Federico's 2020 thesis bibliography. I found
announcements for dimensions 2,3,4, but no published theorem to cite. The
suggested [arXiv:1512.00807](https://arxiv.org/abs/1512.00807) is an unrelated
string theory paper. The three-author connectivity-threshold paper,
[arXiv:1504.05350](https://arxiv.org/abs/1504.05350), ECP **21** (2016),
paper 27, studies a different threshold.

For 2017–2026 follow-up, I searched the titles, authors, citations, and
third-order/rational-coefficient variants, and inspected the eight records
returned by an OpenAlex DOI citation query, including duplicate
preprint/journal records. This is a documented search, not proof that no
unindexed paper exists. The relevant later primary papers checked were:

- Ráth, [arXiv:1707.05169](https://arxiv.org/abs/1707.05169), ECP **23**
  (2018), paper 24, Theorem 1.4: another derivation of the subcritical
  Erdős–Rényi susceptibility expansion; no higher Hamming coefficient.
- Heydenreich–Matzke, [arXiv:1912.04584](https://arxiv.org/abs/1912.04584),
  CPC **31** (2022), 430–454, Theorem 1.1: three terms for **site**
  percolation on Z^d, a different model and limiting regime.
- Eslava–Penington–Skerman, [arXiv:2104.04407](https://arxiv.org/abs/2104.04407),
  AIHP **60** (2024), 1418–1457, Theorem 1.1: survival/extinction of an
  auxiliary deletion/merger process. Their discussion refers to three Hamming
  terms while citing the same paper (3); the cited theorem only supplies two
  nonzero coefficients. That wording supplies no new expansion theorem.
- Blanc-Renaudie–Broutin–Nachmias,
  [arXiv:2401.16365](https://arxiv.org/abs/2401.16365), Theorems 1.1–1.2:
  hypercube component-size and metric scaling limits.
- Diskin–Erde–Kang–Krivelevich,
  [arXiv:2209.03722](https://arxiv.org/abs/2209.03722), RSA **66** (2025),
  e21268: products of bounded-order factors with the number of factors growing.
  This does not treat fixed d with n tending to infinity.

The remaining citing records concern parking on trees/frozen random graphs
or configuration-model percolation. Discovery metadata and further details
are saved in data/literature/. No full resolution was found, so the
RESOLVED_IN_LITERATURE stopping rule does not apply.

## Rigorous deductions and the remaining proof gap

### 1. Conversion to n and the settled small dimensions

For fixed d, expanding (n−1)^(−1) and (n−1)^(−2) in (3) gives

\[
 p_c=\frac1{dn}+\frac{a_2(d)}{n^2}
       +O(n^{-3})+O(n^{-1-d/3}),
 \quad
 a_2(d)=\frac1d+\frac{A(d)}{d^2}
       =\frac{2d^3-2d^2+2d-1}{2d^2(d-1)^2}.
 \tag{4}
\]

This is a direct corollary, not a new critical-point theorem. For d=3,
O(n^(−2)) is already the requested error, so the first term suffices.
For d=4,5,6, O(n^(−3)) is contained in O(n^(−1−d/3)), so (4) has the full
requested precision, with the intended truncation (2).

| d | Terms needed outside the error | Coefficient of n^(−2) | Final error |
|---:|---|---:|---|
| 3 | 1/(3n) | not identifiable at this precision | O(n^(−2)) |
| 4 | 1/(4n)+a2/n² | 103/288 | O(n^(−7/3)) |
| 5 | 1/(5n)+a2/n² | 209/800 | O(n^(−8/3)) |
| 6 | 1/(6n)+a2/n² | 371/1800 | O(n^(−3)) |

The baseline result p_c=m^(−1)+O(m^(−2))+O(m^(−1)V^(−1/3)) also settles
d=1,2,3, using the complete-graph case for d=1. At d=2,3, including A(d)
in (3) does not make it a uniquely determined correction: it lies inside
the allowed error. At d>=4 it is a genuine coefficient independent of
lambda. No third coefficient independent of lambda is identifiable at the
requested precision when d=6.

### 2. What the d/3 boundary actually encodes

The absolute scaling-window width is m^(−1)V^(−1/3), which for fixed d is
of order n^(−1−d/3). Matching integer powers against this width gives J(d)
in (2). The number three here comes from the mean-field finite-size
susceptibility exponent, not directly from counting triangles in K_n.
Triangles and longer cycles affect the coefficients, rather than setting
this exponent.

There is also a simple lower bound showing why dependence on lambda cannot
be ignored at the window scale. Russo's formula and the BK inequality give

\[
 \chi'(p)\le m\chi(p)^2.
\]

For completeness, sum the pivotal-edge formula for each event {0↔x} over
x. Orient each pivotal edge toward x. Its two endpoint connections occur
disjointly in the graph with that edge deleted; BK bounds their joint
probability by the product of two connection probabilities on the original
graph. Summing x and the oriented edges yields m chi². Consequently, for
fixed 0<lambda1<lambda2 and their two roots in (1), integration gives

\[
 p_c(\lambda_2)-p_c(\lambda_1)
 \ge\frac{\lambda_1^{-1}-\lambda_2^{-1}}{mV^{1/3}}.
 \tag{5}
\]

The literature supplies the corresponding window-scale upper comparison
in the mean-field setting. In particular, a coefficient at exactly this
scale cannot be universal in lambda. Below the window exponent, coefficients
in an expansion such as (2) are unique and unchanged by varying lambda.

### 3. A fixed cycle-length cutoff fails

Let X_k count open, unoriented, vertex-simple cycles of length k containing
0 and contained in one coordinate line. For 3<=k<=n, exact counting gives

\[
 \mathbb E_p X_k=\frac d2(n-1)_{k-1}p^k,
 \quad (n-1)_{k-1}=(n-1)(n-2)\cdots(n-k+1).
 \tag{6}
\]

Proof: choose the coordinate, order k−1 distinct nonzero values in it, and
divide by the two traversal directions. Each cycle uses k distinct edges,
so its open probability is p^k. This counts cycles without any assumption
of independence between different cycles.

For every fixed k>=3 and p_n~1/(dn), (6) implies

\[
 n\mathbb E_{p_n}X_k\longrightarrow\frac1{2d^{k-1}}>0.
 \tag{7}
\]

These cycles are nonbacktracking. Thus removing immediate backtracks does
not fix the problem. For any fixed L, even the length L+1 term is of order
n^(−1); the contribution from all lengths above L cannot be O(n^(−2)).
A fixed path/cycle-length truncation therefore cannot give the finite
polynomial approximation of Pi used in the hypercube argument. In a
coordinate subspace of fixed dimension the hypercube has fixed alphabet,
whereas the corresponding Hamming subspace contains n^r vertices. This
is the concrete manifestation of the fixed-subgraph obstruction identified
in the expansion paper's Section 1.4.

This does not rule out resummation or a different proof. It identifies the
failure of a particular transfer of the hypercube proof. All one-line
cycle lengths can be resummed since np stays near 1/d<1. A logarithmic,
rather than fixed, length cutoff controls this particular tail to arbitrary
polynomial accuracy: if np<=q0<1, then

\[
 \sum_{k>L}(k-1)\mathbb E_p X_k
 \le\frac d{2n}\sum_{k>L}(k-1)q_0^k.
 \tag{8}
\]

Taking L=C log n with C sufficiently large makes (8) O(n^(−M)) for any
specified M. Uniform treatment of overlapping cycles and the other lace
diagrams is still needed.

### 4. A rigorous next-order local calculation

Here is a calculation that can be completed without that unproved uniform
diagram estimate. Fix d>=2 and suppose
p_n=q/n+b/n²+O(n^(−3)), with q=1/d and fixed b. Define

\[
 W_n=\sum_{k=3}^n(k-1)X_k,\qquad
 F(x)=\sum_{k=3}^\infty(k-1)x^k
      =\frac{x^3(2-x)}{(1-x)^2}.
\]

Then

\[
 \mathbb E W_n
 =\frac d{2n}F(q)
 +\frac d{2n^2}\left[bF'(q)-\frac{q^2}{2}F''(q)\right]
 +O(n^{-3}).
 \tag{9}
\]

Proof: in (6), expand

\[
 (n-1)_{k-1}
 =n^{k-1}\left[1-\frac{k(k-1)}{2n}
                 +O(k^4/n^2)\right].
\]

For k<=C log n the remainder is uniform. Expand (np_n)^k to first
order in n^(−1) as well. Summing the remainders is valid because the
polynomial factors in k are summable against q0^k for q<q0<1. Equation
(8) handles the tail after choosing C sufficiently large. The first-order
correction from p is bF'(q); the falling-factorial correction is
−q²F''(q)/2. This proves (9) with an actual O(n^(−3)) remainder.

In particular the leading coefficient is (2d−1)/(2d(d−1)²). At the
two-term deterministic approximation b=a2(d), the coefficient of n^(−2)
in (9) simplifies to

\[
 \frac{(2d-1)(2d^2-2d+1)}{2d^2(d-1)^5}.
 \tag{10}
\]

The identities were checked independently by symbolic differentiation and
series expansion in code/algebra.py. This result concerns an expected
cycle count. The lace term Pi^(0) is a double-connection probability summed
over vertices. Distinct cycles can overlap or share endpoints, and cycles
using several coordinate lines also contribute. Those differences already
matter at order n^(−2). Substituting (10) for a lace coefficient would be
invalid. For d<6, (3) also does not give the O(n^(−3)) premise for p_c:
the window error is larger. In d=3 even b need not be independent of
lambda. Equations (9)–(10) apply to the stated deterministic approximation.

### 5. What would determine a3

Summing the lace equation over space gives the exact algebraic identity

\[
 \chi(p)=\frac{1+\widehat\Pi_p}
                  {1-mp(1+\widehat\Pi_p)},\qquad
 mp_c=\frac1{1+\widehat\Pi_{p_c}}-\lambda^{-1}V^{-1/3}.
 \tag{11}
\]

The minus sign follows by rearrangement. The retained arXiv source's
critical-point display has a plus sign; the argument here uses (11),
which also agrees with the hypercube paper's equation (2.2).

For d>=7, suppose one could establish

\[
 \widehat\Pi_{p_c}=-\frac{A(d)}m+\frac{B(d)}{m^2}
                       +O(m^{-3}+V^{-1/3}).
 \tag{12}
\]

Expansion of the reciprocal in (11) would then prove

\[
 p_c=m^{-1}+A(d)m^{-2}+[A(d)^2-B(d)]m^{-3}
               +O(m^{-4}+m^{-1}V^{-1/3}),
\]

and hence

\[
 a_3(d)=\frac1d+\frac{2A(d)}{d^2}
                      +\frac{A(d)^2-B(d)}{d^3}.
 \tag{13}
\]

This would settle the intended expansion for d=7,8,9. It is a conditional
reduction, not a proof of (12). Proposition 5.1 currently provides only
one-sided estimates for the first two lace terms and an
O(m^(−2)+V^(−1/3)) bound for their remaining sum. That bound is precisely
too large to extract B(d). A calculation of one-line susceptibility alone
also omits collisions between explorations of different lines. I have not
controlled those terms to the precision in (12), and do not have a value
or existence proof for B(d).

## Computation

The implementation and data are in code/ and data/. No numerical result is
used as a proof. Every simulation used one CPU worker at inherited nice 15,
with numerical-library threads restricted to one. The largest graph had
331776 vertices. Recorded per-process peaks were under 32 MiB for the
Python driver and under 5 MiB for the C++ child; the selected runs are far
below 4 GB. No GPU, subagents, publication, or push was used. No PDF, page
image, or scan was saved in this directory.

### Exact enumeration and sampler audit

For graphs with at most 22 edges, code/percolation.cpp enumerates every
edge subset and accumulates the root-cluster size by number of open edges.
If R_k is that sum and E the number of edges, the exact susceptibility
polynomial in Bernstein form is

\[
 \chi(p)=\sum_{k=0}^{E} R_k p^k(1-p)^{E-k}.
\]

There is no extra binomial factor: R_k already sums over all configurations
with k open edges. Independently, for every configuration the code computes
the sum of squared component sizes. At each k its accumulated value is
exactly V R_k, as required by transitivity. Configuration counts are also
checked against binomial(E,k). For K_3, the resulting polynomial agrees
with the hand calculation 1+2p+2p²−2p³.

| n | d | Edges | Configurations | Exact-polynomial root, lambda=1 |
|---:|---:|---:|---:|---:|
| 3 | 1 | 3 | 8 | 0.1914805739 |
| 2 | 2 | 4 | 16 | 0.2318290006 |
| 2 | 3 | 12 | 4096 | 0.2072088714 |
| 3 | 2 | 18 | 262144 | 0.1595776530 |

The polynomials are exact integer enumerations; the displayed roots are
floating-point bisections of them. Data/exact_n*_d*.json also retains roots
for other feasible multipliers. A multiplier with target susceptibility
below 1 has no root and is recorded as null.

For larger graphs, the C++ sampler explores C(0) by breadth-first search.
In each coordinate it uses geometric skips to generate Bernoulli(p) open
edges. Edges to already discovered vertices are ignored; any draws for
them are discarded. An edge relevant to discovery is therefore tested
only while its other endpoint is undiscovered, with the correct independent
law. The sample is the entire root cluster, with no size cutoff. The
sampler was checked at p=0.1,0.2,0.3 against each of the four exact graphs,
with 200000 samples per point. All twelve mean discrepancies were within
1.60 estimated standard errors.

### Locating the susceptibility roots

The simulation grid was:

| d | n values |
|---:|---|
| 3 | 8,16,32,64 |
| 4 | 4,8,12,16,24 |
| 5 | 3,4,6,8,10 |
| 6 | 3,4,5,6,8 |

Both lambda=1 and lambda=0.5 were used at every size. These are parameters
in definition (1); they are not asserted to satisfy any small-constant
triangle-condition hypothesis at these finite sizes. The definition and
the expansion paper's theorem allow fixed positive multipliers.

For each of the 38 roots, thirteen pilot bisection steps used 4000 fresh
samples each. Seven fixed p values around that estimate then used 20000
fresh samples each. A weighted quadratic in 1/chi, using the five points
nearest the crossing, supplied the reported root. Its standard error uses
the sample variances and the local derivative. A quadratic and cubic on
all seven points supply an interpolation-sensitivity diagnostic. These
errors are approximate, not rigorous confidence intervals; polynomial
interpolation, inverse-mean bias, and finite-size effects remain possible.
Across all roots the largest interpolation spread was 2.13 times the
reported sampling error. Raw curves are retained so the interpolation can
be changed without rerunning the sampler.

The main Monte Carlo runs used 5320000 fixed-grid explorations plus
1976000 pilot explorations. Sampler validation added 2400000 explorations.
The largest-size estimates for lambda=1 are:

| d | n | Estimated p_c | Sampling s.e. | Interpolation spread | Two-term n benchmark |
|---:|---:|---:|---:|---:|---:|
| 3 | 64 | 0.00528845 | 0.0000037 | 0.0000028 | 0.00534736 |
| 4 | 24 | 0.01096189 | 0.0000064 | 0.0000005 | 0.01103757 |
| 5 | 10 | 0.02264522 | 0.000018 | 0.000001 | 0.02261250 |
| 6 | 8 | 0.02436706 | 0.000018 | 0.000003 | 0.02405382 |

For d=3 the benchmark's second term is inside the window and is not a
lambda-independent coefficient at this precision. At these largest sizes,
the residuals from the displayed two-term benchmark, divided by
m^(−1)V^(−1/3), are respectively −0.713, −0.482, 0.068, and 0.842.
These are finite-size observations, not a test establishing a big-O bound.
As another sign/scale check, all nineteen observed differences
p_c(1)−p_c(0.5) exceed the lower bound (5), with ratios 1.17–1.44.

### Fits with known coefficients held fixed

For d=4,5, code/summarize.py fits

\[
 n^2\left(p_c-\frac1{dn}-\frac{a_2(d)}{n^2}\right)
     =b_\lambda n^{1-d/3}+c_\lambda n^{-1}.
 \tag{14}
\]

The first fitted term accounts for movement within the scaling window.
The second is a descriptive analytic correction, not an estimate that
can be called a3(d). Combining sampling error and interpolation spread
in quadrature supplies regression weights; it does not turn systematic
errors into proven random errors. Both full-size fits and fits omitting
the smallest n are saved in data/fits.json.

| d, lambda | b using all sizes | c using all sizes | b omitting smallest n | c omitting smallest n |
|---|---:|---:|---:|---:|
| 4, 1 | −0.122 | 0.048 | −0.148 | 0.184 |
| 4, 0.5 | −0.368 | −0.496 | −0.409 | −0.248 |
| 5, 1 | −0.014 | 0.078 | −0.050 | 0.146 |
| 5, 0.5 | −0.002 | −0.544 | −0.071 | −0.414 |

These changes are large relative to the fitted corrections. Recovering a
third coefficient from these sizes would be unjustified. For d=3 the fit
uses a lambda-dependent constant in the n²-scaled residual, because the
window itself is n^(−2). For d=6 the window and an n^(−3) analytic term
have identical powers, so they cannot be separated; the saved fit uses a
combined n^(−3) term and an n^(−4) correction. In particular its fitted
coefficient cannot be a universal a3.

As a separate algebra audit, code/cycle_checks.py sums the exact finite-n
expectation in (6) directly for d=2,3,4,6,9 and n=20,...,640 at the
deterministic two-term p. After subtracting (9), the n³-scaled remainders
stay bounded and approach finite values. This checks the normalization
and sign in (9)–(10); the proof of its remainder is the geometric-tail
argument, not these evaluations.

To reproduce the saved numerical runs, with NumPy and SymPy available:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
clang++ -O3 -std=c++17 -Wall -Wextra code/percolation.cpp -o code/percolation
python3 code/algebra.py
python3 code/cycle_checks.py
python3 code/compute.py --mode exact
for d in 3 4 5 6; do
  python3 code/compute.py --mode mc --dimension "$d" --count 20000
done
python3 code/summarize.py
```

The C++ executable and Python driver require process nice>=10 and keep
the inherited nice 15 here. Each separate dimension invocation starts
from the recorded deterministic seed. The computation is sequential.

## Unresolved result

The existence and value of the second-order term B(d) in the lace sum
(12), including all overlap and multi-line contributions with the stated
uniform remainder, remain unproved here. The full expansion for d>=7
and rational-function formulas for its higher coefficients therefore
remain open in this report. The small-dimensional conclusion comes from
the cited literature; the added rigorous results are the deductions and
local cycle calculation above.

Task: “Open problem C0083” — received 2026-11-13, approximately 06:23
Asia/Tbilisi (UTC+04).
