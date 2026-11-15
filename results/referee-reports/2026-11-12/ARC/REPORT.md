Overall verdict: SOUND WITH GAPS

The main heat-kernel theorem, the lazy-walk theorem, the corollary, the constant-entry lemma, the neighbour-average proposition, and the ten-vertex counterexample are mathematically sound under the standing assumptions. I found no gap in their proofs. The qualification concerns the scope discussion: **conditional on the paper's description of the weighted Regev–Shinkar example, the first question at line 173 already has a negative answer**, by the clique-lift argument below. The observation that one particular lifted pair is nonadjacent overlooks counterexamples on actual edges of the lift. There are also two points of potentially misleading terminology or comparison with earlier work.

Line numbers refer to the supplied `PAPER.tex`. I did not browse or retrieve external sources. Thus a literature attribution below is distinguished from a mathematical implication of the statements quoted in this paper. I read the authors' scripts and saved outputs but did not execute their scripts or use their functions in the independent programs.

## 1. Definition of 1-walk-regularity — SOUND

Lines 60–66 give the needed definition: for every nonnegative integer power, entries are constant separately on the diagonal and on all edges. This is global edge constancy, not just constancy on each automorphism orbit or among some neighbours. In fact, constancy of the diagonal of `A^2` already implies regularity. Connectedness and `n >= 2` give `d >= 1`.

Arc-transitivity implies vertex-transitivity and constancy on directed edges; automorphisms preserve every `A^k`. This establishes both requirements. Undirectedness also gives symmetry of every power.

For distance-regular graphs the implication can be established without appealing to a citation. If `w_k(h)` denotes the number of length-`k` walks between vertices at distance `h`, the intersection-number recurrence is

\[
w_{k+1}(h)=c_h w_k(h-1)+a_h w_k(h)+b_h w_k(h+1),
\qquad w_0(h)=\mathbf 1_{h=0}.
\]

Terms outside the distance range are omitted. The intersection numbers depend only on `h`, so induction gives dependence only on distance, including distances zero and one. The ambient assumptions exclude a one-vertex graph.

The spectral measure in line 66 is also correctly normalized: the orthogonal spectral projections are positive semidefinite and sum to the identity, the normalized Laplacian spectrum lies in `[0,2]`, and connected regularity gives `E_0=J/n`.

## 2. Lemma (constant), lines 92–104 — SOUND

The absolutely convergent exponential series preserves diagonal constancy and edge constancy. In the heat equation,

\[
a'(t)=\frac1d\sum_{z\sim x}H_t(x,z)-a(t)=b(t)-a(t),
\]

there are exactly `d` equal summands. There is no missing factor of `d`, time rescaling, or requirement that an automorphism actually interchange two particular edges.

The local observation at lines 136–138 is correct. For a fixed vertex `x`, equality of `H_t(x,z)` over its neighbours for every time is sufficient for the mean/variance identities at that vertex. Global diagonal constancy is needed to state a common `a`, not to differentiate the local spectral representation.

## 3. Theorem 1 (main), lines 68–78 and 106–118 — SOUND

**The essential edge-to-spectral-measure step is justified.** The lemma gives

\[
\frac{H_t(x,y)}{H_t(x,x)}
=\frac{b(t)}{a(t)}=1+\frac{a'(t)}{a(t)}
=1-\mathbb E_{\nu_{x,t}}\lambda.
\]

As a separate check of that load-bearing step, every spectral projector `E_lambda` is a polynomial in `A`, by interpolation on the distinct eigenvalues. Its diagonal entries and its edge entries therefore have the required constancies. Since `PE_lambda=(1-lambda)E_lambda`,

\[
E_\lambda(x,y)
=\frac1d\sum_{z\sim x}E_\lambda(x,z)
=(1-\lambda)E_\lambda(x,x) \quad (x\sim y).
\]

Summing this identity with weights `exp(-t lambda)` gives the same formula directly. It identifies exactly why a single edge entry is expressible through the diagonal spectral measure. Regularity or vertex-transitivity alone would only identify the neighbour average.

Differentiation of the finite exponential sum gives

\[
r'=(\log a)''
=\frac{a''a-(a')^2}{a^2}
=\mathbb E_\nu\lambda^2-(\mathbb E_\nu\lambda)^2.
\]

This variance is strictly positive at every **finite** `t >= 0`: the tilted measure has positive mass at zero and positive total mass at positive eigenvalues. Exponential tilting never removes either part at a finite time. Only its limiting measure at infinity is a point mass. There is no endpoint exception at zero.

At zero, `L_xx=1` and `(L^2)_xx=1+1/d`, so the derivative is exactly `1/d`. The limiting ratio is one because `H_t -> J/n`. The lemma's global `a,b` also proves equality of the ratio on every edge, including both orientations.

**Both sides of (eq:bounds) hold.** Put

\[
p_t=1-\frac{1}{nH_t(x,x)}=\nu_{x,t}((0,2]).
\]

This number is nonnegative, and the positive part of the measure is supported in `[lambda_2,lambda_n]`. Thus `lambda_2 p_t <= E_nu lambda <= lambda_n p_t`.

At `t=0` the inequality becomes

\[
\lambda_2(1-1/n)\le 1\le\lambda_n(1-1/n).
\]

An independent endpoint check is `sum_{i=2}^n lambda_i = tr L = n`: the least and greatest positive eigenvalues bracket their average `n/(n-1)`. At infinity, `p_t -> 0` and `1-r -> 0`; neither the lower bound nor the upper bound has a sign problem. In a walk-regular graph every occurring eigenvalue has diagonal spectral weight equal to its multiplicity divided by `n`, so `(1-r)/p_t -> lambda_2` as well. For `K_2`, the two bounds agree for every time.

## 4. Theorem 2 (lazy walk), lines 80–82 and 120–130 — SOUND

Polynomial functional calculus gives common values `alpha_k` on the diagonal and `beta_k` on edges. Matrix multiplication gives precisely

\[
\alpha_{k+1}=\tfrac12(\alpha_k+\beta_k),
\qquad R_k:=\frac{\beta_k}{\alpha_k}=2\frac{\alpha_{k+1}}{\alpha_k}-1.
\]

The correct tilt is the pushforward of `mu_x` to `theta=1-lambda/2`, weighted by `theta^k` and normalized by `alpha_k`. Call this probability measure `eta_k`. In particular,

\[
R_{k+1}-R_k
=\frac{2\operatorname{Var}_{\eta_k}(\theta)}{\mathbb E_{\eta_k}\theta}.
\]

The denominator is positive because of the mass at `theta=1`. This is the explicit variance version of the Cauchy–Schwarz calculation in the paper. At `k=0`, `theta^0` means the constant polynomial one, including at `theta=0`.

For `n >= 3` the measure has positive mass at some `theta` in `(0,1)`. Otherwise its Laplacian support would be just `{0,2}`, and

\[
1=L_{xx}=2(1-1/n)
\]

would force `n=2`. The interior mass survives every finite power tilt. Thus **every** increment, including the increment from zero to one, is strictly positive. Bipartite graphs introduce a mass at `theta=0`, which is removed after the first step; the interior mass still ensures strictness. This is why the lazy walk is important. For example, nonlazy simple random walk on `C_4` has edge ratio zero at even times and a positive ratio at odd times.

For `n=2`, connected simplicity forces `K_2`; `Q=J/2`, giving the stated sequence `0,1,1,...`. Irreducibility and the positive holding probability give `Q^k -> J/n` in all cases.

## 5. Corollary and comparisons, lines 84–88 — SOUND; comparison needs a scope fix

The corollary follows from Section 1 of this report and the two theorems. Its continuous-time and discrete-time assertions are both sound under the ambient assumptions.

On the description of Aldous–Fill Proposition 7.29 supplied at line 52, its distance-one **continuous-time** ratio assertion is exactly the relevant specialization. Their nondecreasing assertion also implies strict increase here using analyticity and the different endpoint values: equality at two times would force constancy on an interval, hence everywhere. The lazy discrete-time assertion is not an immediate specialization of the continuous-time statement as quoted. Line 88 should specify which part is being compared.

The inclusion of the adjacent-vertex case of Liu–Zhang is mathematically correct on the stated description: distance-regular graphs with classical parameters of diameter three are a subclass, and adjacent pairs are among all pairs. This is not an assertion that the present proof contains their claims for larger distances.

I could not independently check the wording, numbering, or source proofs of either reference: neither source is supplied locally, and browsing was prohibited. This is a limitation of the attribution check, not a missing step in the present corollary.

## 6. Proposition (average), lines 142–158 — SOUND

For every regular graph and each vertex separately,

\[
\frac1d\sum_{z\sim x}\frac{H_t(x,z)}{H_t(x,x)}
=1+\frac{\partial_tH_t(x,x)}{H_t(x,x)}
=1-\mathbb E_{\nu_{x,t}}\lambda.
\]

All denominators in this average are the same. Differentiating therefore gives precisely the same variance, strictly positive by the zero/positive support argument. No vertex-transitivity, walk-regularity, or constancy of the diagonal across vertices enters. The proof is sufficient as written. The spectral bounds also apply to this average, though that strengthening is not needed for the proposition.

The independent search below found many decreasing individual edge ratios and no violation of this proposition.

## 7. Example (regular), lines 162–168 — SOUND

The construction gives ten vertices of degree four: each cube vertex gets one apex neighbour, and each apex has the four vertices of its face as neighbours. It is simple and connected. My independent adjacency characteristic polynomial is

\[
(z-4)(z-1)^2(z+1)^4(z+3)(z^2-z-4).
\]

Consequently the second normalized Laplacian eigenvalue is simple and equals

\[
\lambda_2=\frac{7-\sqrt{17}}8=0.3596117967977924\ldots.
\]

Take a second adjacency eigenvector to have value `+1` on the first face, `-1` on the opposite face, and respective apex values `+(sqrt(17)-1)/2` and its negative. Its positive apex value exceeds one. For a vertex `x` of that face and its apex `y`, the leading term of `H_t(x,y)-H_t(x,x)` is

\[
e^{-\lambda_2t}\frac{f_2(x)(f_2(y)-f_2(x))}{\lVert f_2\rVert^2}>0.
\]

The next eigenvalue is larger. Thus overshoot and eventual decrease also follow independently from spectral asymptotics, without using the cited proposition.

At time seven, a separate exact rational certificate, using the **positive** series for `exp(tP)` rather than the authors' alternating series, proves

\[
r_{xy}(7)=1.01966322535501697143527092040686144065\ldots>1,
\]

\[
r'_{xy}(7)=-0.00094785788801719938495442323614873570\ldots<-9\cdot10^{-4}.
\]

The exact assertions use rational interval endpoints and rational comparisons, not these printed decimals. Independent 70-digit `mpmath` matrix exponentiation agrees. Numerically the crossing of one is near `4.94217770464`, and the maximum is about `1.01975895794` at `6.80531144`, agreeing with the paper. These numerical locations are not claimed as exact uniqueness certificates.

The authors' own Taylor tail formula is valid for truncation through degree 120: successive omitted scalar terms have ratio at most `14/122 < 1/2`. Its stated bound is `1.186705882573337e-62 < 1e-61`. A derivative entry needs twice that bound, as the authors' code correctly accounts for. “120 terms” should read “through degree 120,” since terms indexed zero through 120 number 121.

The neighbour average on this graph is increasing: on the independent `[0,40]` grid its smallest increment was `5.6956e-10`, and its smallest tilted variance was `5.6854e-8`.

## 8. Scope and the open questions — GAP

### The first scope question has a negative answer under line 170's premise

Line 170 says the weighted Regev–Shinkar Cayley counterexample fails across a toggle **edge**. Merely observing that their selected pair `(u,0),(v,0)` becomes a nonedge in one unweighting construction does not show that edge monotonicity survives unweighting. The following transfer argument fills this gap and answers the first question at line 173 negatively, if that weighted-edge description is correct.

Let the weighted counterexample be a Cayley graph on a finite group `Gamma`, with inverse-symmetric generating set `S` and positive weights `m_s=m_{s^{-1}}`. Choose times `0 < tau_1 < tau_2` at which its ratio across an edge `e,s_0` decreases. Small perturbations of the weights preserve this strict inequality, so weights may be taken rational. Multiplying all rates and rescaling time lets us assume that every `m_s` is a positive even integer. Write

\[
B=\sum_{s\in S}m_s(I-R_s),\qquad D=\sum_{s\in S}m_s,
\]

where `R_s` is right translation. We use the unnormalized weighted Laplacian `B`; changing to the paper's rate-one convention only rescales time.

For an integer `N > 1+max_s m_s`, form the simple Cayley graph on `Gamma x Z_N` with generators

\[
\{(e,j):j\ne0\}
\ \cup\ 
\bigcup_{s\in S}\{(s,j):j\in J_s\},
\qquad J_s=\{\pm1,\ldots,\pm(m_s/2)\}.
\]

The generator set is inverse closed, has no identity or repetitions, and gives degree `D+N-1`. Each fibre is a clique. In particular **`(e,0)` and `(s_0,1)` are adjacent**. The graph is connected and vertex-transitive by its Cayley construction.

Let `B_N` be its unnormalized Laplacian. The subspace `U` of functions constant on each fibre is invariant, and `B_N` restricted to `U` is exactly `B`. On `U^perp`, the clique Laplacian is `N I`; the external-edge Laplacian is positive semidefinite and preserves this subspace. Thus `B_N >= N I` on `U^perp`. Orthogonal decomposition gives, for every pair of fibre indices,

\[
e^{-\tau B_N}((g,i),(h,j))
=\frac1N e^{-\tau B}(g,h)+R_N(\tau)_{(g,i),(h,j)},
\qquad |R_N(\tau)_{a,b}|\le e^{-N\tau}.
\]

For each fixed positive `tau`, multiplying numerator and denominator by `N` proves

\[
\frac{e^{-\tau B_N}((e,0),(s_0,1))}
{e^{-\tau B_N}((e,0),(e,0))}
\longrightarrow
\frac{e^{-\tau B}(e,s_0)}{e^{-\tau B}(e,e)}.
\]

The denominator has a positive limit. Therefore the strict decrease between `tau_1` and `tau_2` persists for all sufficiently large `N`, **on an actual edge of a finite simple Cayley graph**. For normalized heat time, use `t_i=(D+N-1)tau_i`; their ordering is unchanged.

This is an existence proof, not an explicit numerical RS graph under the resource limit. Its only external premise is precisely the weighted-edge counterexample already asserted in the paper. I have not independently verified that premise against the unavailable RS source. Accordingly, either that factual description must be corrected, or the first scope question should be replaced by the negative consequence above. A small numerical mechanism check of the decomposition is supplied below; that toy weighted graph is not presented as the RS counterexample.

This observation does not contradict Theorem 1: Cayley graphs need not be arc-transitive or 1-walk-regular.

### “Symmetric chain” needs an explicit meaning

Lines 35 and 52 are **ambiguous**, and are **ERROR if “symmetric” means only a symmetric transition matrix**. A symmetric stochastic matrix need not make its diagonal entry the largest entry of every even power. For example,

\[
M=\begin{pmatrix}
3/10&3/10&2/5\\
3/10&1/5&1/2\\
2/5&1/2&1/10
\end{pmatrix},
\qquad M^2(0,0)=17/50<7/20=M^2(0,1).
\]

Every entry is positive; the matrix is symmetric, stochastic, irreducible and reversible with uniform stationary distribution. Even within the graph setting, the lazy kernel on the ten-vertex example satisfies

\[
Q^8(0,8)=2093590/8^8>2044896/8^8=Q^8(0,0).
\]

If “symmetric” is intended in the automorphism/transitivity sense used in some Markov-chain terminology, the intended statement is valid. State that sense, or simply say “vertex-transitive reversible chain.” The vertex-transitive continuous-time inequality follows from semigroup symmetry and Cauchy–Schwarz, using equal diagonal entries. There is no such issue with the paper's explicitly vertex-transitive sentence at the end of line 52.

### What is claimed about Open Problem 7.30

As quoted here, 7.30 asks for **some** stronger monotonicity property. The paper gives one, for adjacent vertices, and consistently describes that scope. It does not claim or prove monotonicity for every pair in every arc-transitive graph. Its second question at line 173 asks for that stronger all-pairs property. The first new question at that line concerns a different class, all simple vertex-transitive graphs, and is subject to the transfer argument above.

The mathematical relationship to the statements of 7.29 and Liu–Zhang quoted in this text is as described in Section 5 of this report. Exact source attribution remains unverified offline. In particular, I do not infer from this paper alone that the cited monograph literally calls every matrix-symmetric chain “symmetric,” or that it proves a lazy discrete-time statement.

## 9. Lean file — SOUND for its stated algebraic inequality; limited formal scope

`lean/TiltedVariance.lean`, lines 5–8, states the following over an arbitrary finite index set, for real `l_i` and nonnegative real `m_i,x_i`:

\[
\left(\sum_i m_i l_i x_i\right)^2
\le \left(\sum_i m_i x_i\right)
\left(\sum_i m_i l_i^2 x_i\right).
\]

Its proof applies finite Cauchy–Schwarz to `sqrt(m_i x_i)` and `l_i sqrt(m_i x_i)`, then rewrites squared square roots using nonnegativity and rearranges products. No hypothesis `l_i >= 0` is needed. There are no `sorry`, `admit`, or added axioms in this file.

This is the finite weighted inequality `a a''-(a')^2 >= 0`. With separately proved `a>0` it implies nonnegative variance/logarithmic second derivative. It permits all weights to be zero and proves no strict inequality by itself.

It does **not** formalize exponential differentiation, the heat equation, the edge identity, graph hypotheses, spectral projections, strict positivity, the spectral bounds, convergence, the lazy theorem, or the counterexample. The informal proofs supply those parts. Line 179 accurately describes the limited inequality being checked, rather than claiming full formalization of the paper.

Neither `lean` nor `lake` is installed on the executable path in this environment, and no pinned Mathlib project is supplied. I therefore checked the source and its mathematical content, but did not independently reproduce Lean elaboration or kernel checking. Absence of proof holes in the source is not a substitute for reporting that limitation.

## Independent computations: programs, outputs and limits

All programs and outputs are in this directory. No author program was run. BLAS/OpenMP thread counts were set to one before importing numerical libraries; each computational program has a 240-second alarm. At most two computational processes ran simultaneously. The largest measured peak resident memory was about 226 MB, and the longest individual run was under four seconds. No external write, push, agent, or visible window was used.

### `referee_checks.py`

Outputs: `referee_checks_output.txt`, `referee_checks_results.json`, `referee_heat_grid.csv`.

The program checks every directed edge on 39 graphs at 1,036 times, from zero to 200: a logarithmic grid near zero, a uniform grid through 20, and additional larger times. The CSV saves the ratios, analytic derivatives, and both bounds for edges from vertex zero. Full-edge checks and their extrema are saved in JSON.

The families are:

| Family | Graphs |
|---|---|
| Cycles | `C_n`, n = 3,4,5,6,7,8,9,10,12,20 |
| Complete graphs | `K_n`, n = 2,3,4,5,8,10 |
| Complete bipartite graphs | `K_(m,m)`, m = 2,3,4,5 |
| Named distance-regular graphs | Petersen, Heawood, icosahedron, dodecahedron |
| Hamming graphs | `Q_3`, `Q_4`, `H(2,3)`, `H(3,3)` |
| Johnson graphs | `J(6,2)`, `J(7,3)` |
| Other graphs satisfying 1-walk-regularity | `C_13(1,5)`, doubled `C_7`, `GP(8,3)`, `GP(12,5)` |
| Vertex-transitive, non-arc-transitive Cayley graphs | `Z_8`, `Z_10`, `Z_12` with generators `±1,±2`; pentagonal prism times `K_2`; `S_4` with adjacent transpositions |

For the first 34 graphs, global diagonal and edge constancy were checked with unbounded **integer** powers `A^0,...,A^(n-1)`. Cayley–Hamilton then covers every power. Thirty of these graphs also pass NetworkX's distance-regularity check. The five non-arc-transitive Cayley graphs fail exact 1-walk-regularity; since each is vertex-transitive by its Cayley construction, this also rules out arc-transitivity. For the three circulants an even simpler certificate is that the two edge types have two versus one common neighbours.

Heat kernels were computed by symmetric spectral decomposition, with a separate SciPy matrix exponential check at times 0, 20 and 40. On the claimed 1-walk-regular graphs:

```text
graphs in theorem's scope:                 34
maximum |r - (1-E lambda)|:                3.775e-15
maximum |r' - Var(lambda)|:                1.332e-15
maximum independent expm discrepancy:      2.609e-15
maximum lower-bound residual violation:    3.592e-15
maximum upper-bound residual violation:    4.663e-15
maximum spread between edge ratios:        7.328e-15
minimum floating-point grid increment:     0
```

The tiny residuals are numerical error. A zero floating-point increment at a late time is not evidence against mathematical strictness and is not advertised as an exact strictness check.

For the lazy walk, the program independently forms integer row counts for `(dI+A)^k`. The common factor `(2d)^(-k)` cancels in the ratio. Every consecutive comparison, on every directed edge, is by exact integer cross-multiplication for `k=0,...,199`, thus covering ratios through `k=200`. All 34 graphs in the theorem's scope pass; `K_2` has exactly the expected equalities after the first step. The other 33 have strictly positive increments throughout. The five additional Cayley graphs also pass these finite lazy checks. For example, the minimum increment on `C_3` is about `3.485e-120`, which ordinary floating-point ratio subtraction would lose entirely.

The non-arc-transitive examples have unequal edge ratios. Separate matrix exponentiation at time one gives:

| Cayley graph | `r_(0,1)(1)` | `r_(0,2)(1)` |
|---|---:|---:|
| `Z_8`, generators `±1,±2` | 0.298264179976 | 0.272782220622 |
| `Z_10`, generators `±1,±2` | 0.297689942772 | 0.269740035903 |
| `Z_12`, generators `±1,±2` | 0.297651988319 | 0.269527400113 |

All five small Cayley examples show no significant decrease on the heat grid; the worst negative increment is only `-1.11e-16`. This is a bounded numerical observation, not an answer for all vertex-transitive graphs. The bounds and edge spectral identity can fail outside 1-walk-regularity: the observed bound residuals on these examples reach approximately `0.037`, far above rounding error.

### `referee_counterexample.py`

Outputs: `referee_counterexample_output.txt`, `referee_counterexample_results.json`.

The graph is built from binary cube coordinates and face membership. Symbolic characteristic-polynomial factorization and an exact eigenvector identity check establish the spectral assertions above. For the rational certificate, write `H_t=e^(-t) exp(tP)`. The common scalar factor cancels from the ratio and its derivative. Summing the positive series through degree 100 at time seven bounds each omitted entry, and each omitted entry of `P exp(tP)`, by

\[
\frac{7^{101}}{101!}\frac1{1-7/102}<2.580\cdot10^{-75}.
\]

Rational interval arithmetic then certifies both inequalities in the example. The exact interval endpoints and exact derivative upper bound are saved in JSON; the printed coincident decimal endpoints are just rounded output. A second computation uses a 70-digit matrix exponential.

Selected output:

```text
r(7) = 1.0196632253550169714352709204068614406538193950400505122304
r'(7) = -0.000947857888017199384954423236148735703056073881668317713167651
neighbour_average minimum_grid_increment = 5.695627303126116e-10
neighbour_average minimum_variance = 5.685394315826467e-08
PASS
```

### `referee_search.py`

Outputs: `referee_search_output.txt`, `referee_search_results.json`.

This scans all 15 connected regular graphs with `2 <= n <= 7` in the NetworkX graph atlas, plus 818 connected random-regular samples on orders 8, 9 and 10. For those orders, each admissible degree from 2 to `n-2` uses seeds 0 through 59, retaining connected samples. The random sample is not an exhaustive census and may include isomorphic repeats. Heat ratios, analytic derivatives, and all neighbour averages are checked at 304 times from zero through 100. The threshold for counting an edge decrease is a derivative below `-1e-8`.

```text
atlas samples:                       15
random samples:                     818
samples with an edge decrease:      368
neighbour-average failures:           0
neighbour-average identity failures:  0
maximum average identity/variance residual: 2.554e-15
minimum average grid increment:             -2.220e-16
PASS
```

One witness per order 8, 9 and 10 is separately certified by exact rational positive-series bounds, not just by the floating-point scan:

| Reconstructible sample | Directed edge | Time | Ratio, approximately | Certified derivative upper bound, approximately |
|---|---|---:|---:|---:|
| `n=8,d=3,seed=0` | `(2,4)` | `57/5` | 1.001487232864 | -0.000380464408104 |
| `n=9,d=4,seed=0` | `(6,3)` | `21/2` | 1.000459618498 | -0.000170047698185 |
| `n=10,d=3,seed=0` | `(8,5)` | `51/5` | 1.040473011200 | -0.005785109145118 |

Explicit edge lists and exact rational bounds are in the output/JSON, so reconstruction does not depend on a future NetworkX random-generator implementation. For example the eight-vertex cubic witness has edges

```text
(0,1),(0,6),(0,7),(1,3),(1,7),(2,4),
(2,5),(2,7),(3,4),(3,6),(4,5),(5,6).
```

No average failure was found. Its proof, rather than the finite scan, establishes the general claim.

### `referee_lift_check.py`

Output: `referee_lift_check_output.txt`.

This tests the scope argument's clique decomposition on a small weighted Cayley graph on `Z_5`, with weights two on `±1` and four on `±2`. It constructs simple lifts with fibre sizes 11, 21 and 31 and checks degree, symmetry, an actual cross-fibre edge, the restriction to fibre-constant functions, positive semidefiniteness of the external Laplacian, and the exponential error bound. This base graph is a mechanism check, not a nonmonotone example.

For `N=31`, at unnormalized time `0.7`, the maximum entry error from `H_base/N` is about `5.261e-12`, below the bound `exp(-31*0.7)=3.765e-10`; the base ratio is `0.999515573034`, and the ratio on the actual lifted edge is `0.999515572974`. All checks pass. The general transfer result rests on the proof in Section 8, not on this toy computation.

### `referee_audit.py`

Output: `referee_audit_output.txt`.

This rereads the independent JSON artifacts, recomputes aggregate discrepancies, compares the saved rational certificate endpoints exactly, independently recomputes the authors' scalar Taylor bound, and finds the exact three-state symmetric stochastic-matrix counterexample given above. Its final output is `ALL_ARTIFACT_ASSERTIONS_PASS`.

## Corrections required

1. **Lines 170–173, first scope question:** the nonadjacency of `(u,0),(v,0)` is insufficient to leave edge monotonicity open. If the weighted RS example really fails on a toggle edge, replace the first question with the negative unweighting consequence proved in Section 8. Alternatively correct the weighted-edge premise if it misdescribes the source. No change to the main theorems is needed.

2. **Lines 35 and 52, “every symmetric chain” / “symmetric reversible chain”:** define symmetry in the automorphism/transitivity sense, or say “vertex-transitive reversible chain.” Read merely as matrix symmetry, the assertion is false, with exact counterexamples above. Equal diagonal heat entries are the additional ingredient used in the intended inequality.

3. **Line 88, comparison with Proposition 7.29(ii):** specify “the continuous-time distance-regular assertion is its distance-one case.” Do not present the lazy discrete-time assertion as a direct specialization of the continuous-time result quoted at line 52. Strictness in continuous time is recoverable by analyticity, and is also proved directly here.

4. **Line 170, matching indices in the lift:** when asserting that zero-offset pairs are nonedges, state the choice `N > max m`, so no index in `1,...,m` wraps to zero. A standalone Cayley construction should also specify inverse closure, especially for involutory generators; the even-weight, symmetric-offset construction above supplies one.

5. **Line 167, Taylor truncation:** replace “to 120 terms” with “through degree 120 (121 terms).” The displayed tail and the authors' implementation already correspond to the latter, so the certificate's validity is unchanged.

Task: “You are refereeing a mathematical paper that has been posted.” First recorded task clock: 12 November 2026, 19:55:38 (+04).
