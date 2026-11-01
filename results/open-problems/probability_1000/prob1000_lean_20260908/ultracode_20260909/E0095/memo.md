# E0095 - Diaconis, Question 4: which matching (or edge) to add to a regular graph to speed up the walk

Attempt of 2026-09-09. Source: P. Diaconis, "Some things we've learned (about Markov chain Monte
Carlo)", Bernoulli 19 (2013), arXiv 1309.7754, Section 5, Question 4 (PDF pp. 9-10).

## 1. The problem as the source states it

Verbatim (the PDF text; line breaks removed):

> Question 4. One may ask a similar question for random walk on any graph. To be specific,
> consider a connected d regular graph with n even. Thus, nearest neighbor random walk has a
> uniform stationary distribution. Add in n/2 edges forming a perfect matching. This gives a
> (d+1) regular graph. What choice of edges give fastest mixing? If the original graph is an
> n-cycle and thus 2-regular, [15] shows that a random matching improves the diameter to
> log_2 n + o(1). She gives an explicit construction of a matching that has diameter
> 2 log_2 n + o(1). These diameter bounds translate into eigenvalue bounds and so bounds on rates
> of convergence using standard tools. However, something is lost in these translations and it
> would be worthwhile to know accurate rates of convergence to the uniform distribution.
>
> An important variation: consider a reversible Markov chain K(x,y) on a finite set X with
> stationary distribution pi(x). Suppose a weighted edge is to be added to the underlying graph
> and the resulting Markov chain is "Metropolized" so that it still has stationary distribution
> pi(x). What edges best improve mixing, or best improve the spectral gap?

"The similar question" is Question 3, which asks which single generator to add to a generating
set of a group. Two remarks on the ledger row. (i) The row says "which edge (or perfect
matching) should be added"; the source's graph question is about a perfect matching only, and
the single-edge form comes from Question 3 and from the "important variation" (one weighted
edge, Metropolized). Both forms are treated below, but they behave very differently and should
not be conflated. (ii) The [15] diameter claim is quoted loosely by the source: Bollobas-Chung
(1988) prove diameter log_2 n + log_2 log n + O(1) for the cycle plus a random matching, not
log_2 n + o(1). Neither remark changes the direction of any inequality in the problem.

## 2. Findings

There are three kinds of result, and it matters which is which.

**(A) Literature (asymptotics for the cycle, and the "accurate rates" sub-question).** For the
n-cycle plus a uniformly random perfect matching (new edges only), the simple random walk has
cutoff at 3 log_2 n with a window of order sqrt(log n), and no matching can do better than
3 log_2 n (1 - o(1)). The second adjacency eigenvalue of the cycle plus a random matching is
2 sqrt 2 + o(1) with high probability, and no cubic graph has second eigenvalue below
2 sqrt 2 - o(1). So, to leading order, the random matching is an optimal answer for the cycle,
both in mixing time and in spectral gap, and the rates Diaconis asked for are known. This is a
chain of published results (Section 6); I did not find the chain written out for this question
anywhere, but every link is in print.

**(B) New exact results for a single added edge (the Question 3 analogue and the
"important variation").**

Theorem 1 (degenerate Fiedler value: few edges never help). Let G be a connected d-regular
graph on n vertices whose Laplacian algebraic connectivity lambda_2 has multiplicity m >= 2.
Add any r <= m - 1 edges (weights w_i > 0 allowed, multi-edges allowed) to obtain G'. Then
  (a) lambda_2(L(G')) = lambda_2(L(G));
  (b) the spectral gap of the simple random walk satisfies gap(G') <= gap(G) = lambda_2/d,
      with strict inequality unless every Fiedler vector that is constant across each added
      edge vanishes at all endpoints of the added edges;
  (c) the uniform-stationary "max-degree" chain K' = I - L(G')/d_max(G') has gap
      lambda_2/d_max(G') < lambda_2/d.
Corollaries. On the cycle C_n (m = 2): no single chord raises the algebraic connectivity, and
every chord weakly lowers the walk's spectral gap; the only chord that does not strictly lower
it is the antipodal chord for even n (numerically, that one leaves it exactly unchanged). On the
hypercube Q_d (lambda_2 = 2 with multiplicity d): any d - 1 added edges leave both the
algebraic connectivity and the walk's gap unchanged. On a Cayley graph of an abelian group the
Fiedler value is degenerate unless its character is real, so the same applies.

Theorem 2 (simple Fiedler value: the first-order answer made rigorous). Let lambda_2 be simple
with unit Fiedler vector phi, let Delta = lambda_3 - lambda_2 > 0, and add the edge {u,v} with
weight w > 0. Put c = phi(u) - phi(v) and g = lambda_2(L + w e e^T) - lambda_2, e = e_u - e_v.
Then

        w c^2 Delta / (Delta + 2w + w c^2)  <=  g  <=  min(w c^2, Delta).

So the first-order Fiedler-vector gain w c^2 is always an upper bound on the true gain, the
interlacing cap Delta is the other upper bound, and the gain is at least the expression on the
left. When w c^2 << Delta the two sides agree to first order and the best edge is the one
joining the extremes of the Fiedler vector; when w c^2 >> Delta (paths, any bottleneck graph
with a gap of order 1/n^2) the cap binds and the Fiedler extremes are not the right guide.

Theorem 3 (the path, exactly). For P_n plus one edge, lambda_2(L) <= lambda_3(P_n) =
2 - 2 cos(2 pi/n), with equality for the end-to-end edge (which makes the cycle). So the
end-to-end edge is optimal for the algebraic connectivity and for the uniform-stationary chain,
but not uniquely: numerically the symmetric chords {j, n-1-j} with 4(j+1) <= n all tie (all n
from 6 to 129, and n = 150, 151, 200, 201, 300, 301, 400). For the simple random walk on the path
the best single edge is not the end-to-end edge but the last of the tying chords, j* =
floor(n/4) - 1 (exhaustive over all chords for n <= 80; symmetric chords to n = 400): it folds
the path into a cycle of length about n/2 with two tails of length about n/4. Its gap is
1 - cos(2 pi/n) times (1 + O(1/n)), which is 4 (1 + o(1)) times the path's gap.

**(C) Exact small cases for the matching question on the cycle (brute force over all
perfect matchings of new edges).** Fastest simple random walk, by spectral gap 1 - lambda_2(A)/3:
n = 6: K_{3,3} (gap 1, but bipartite, so the non-lazy walk is periodic); n = 8: the cube and one
other matching (gap 2/3); n = 10: gap 0.4795, adjacency lambda_2 = 1.5616 (the Petersen graph,
the best cubic graph on 10 vertices with lambda_2 = 1, is not Hamiltonian and so is unattainable
from any cycle); n = 12: gap 0.4893; n = 14: the Heawood graph (lambda_2 = sqrt 2, gap 0.5286).
The random matching's mean gap is far below the optimum at these sizes (0.23 vs 0.53 at
n = 14): the leading-order optimality in (A) says nothing about small n.

## 3. Proofs

Notation. L = D - A is the Laplacian, 0 = lambda_1 < lambda_2 <= ... its eigenvalues, phi_k
orthonormal eigenvectors. Adding the edge {u,v} with weight w adds w e e^T, e = e_u - e_v, to
L. For a graph with degree vector d' the simple random walk P' = D'^{-1} A' is reversible with
stationary pi' proportional to d', and its spectral gap is

    gap = min { <psi, L' psi> / <psi, D' psi> : psi != 0, <psi, d'> = 0 },

the Dirichlet form over the pi'-variance (standard min-max for the self-adjoint operator
D'^{-1/2} A' D'^{-1/2}).

Proof of Theorem 1. Let E be the m-dimensional lambda_2-eigenspace of L. The r conditions
phi(u_i) = phi(v_i) cut out a subspace of E of dimension at least m - r >= 1; take phi there and
put a_i = phi(u_i) = phi(v_i). Then L' phi = L phi + sum_i w_i (phi(u_i) - phi(v_i))(e_{u_i} -
e_{v_i}) = lambda_2 phi, and phi is orthogonal to the constants, so lambda_2(L') <= lambda_2 by
min-max, while lambda_2(L') >= lambda_2 because L' - L is positive semidefinite. That is (a).
For (b) let N = <1, d'> = nd + 2 sum_i w_i, shift psi = phi - (<phi, d'>/N) 1 so that
<psi, d'> = 0. The Dirichlet form is unchanged, <psi, L' psi> = <phi, L' phi> = lambda_2 |phi|^2.
The variance is <phi, D' phi> - <phi, d'>^2/N = d|phi|^2 + 2 sum_i w_i a_i^2 - 4 (sum_i w_i a_i)^2/N,
using <phi, 1> = 0. By Cauchy-Schwarz (sum w_i a_i)^2 <= (sum w_i)(sum w_i a_i^2), and
4 sum w_i / N <= 2, so the variance is at least d|phi|^2, with equality only if all a_i = 0
(since N > 2 sum w_i). Hence gap(G') <= lambda_2 |phi|^2 / (d |phi|^2) = lambda_2/d = gap(G),
strictly unless every admissible phi has all a_i = 0. The unit-weight form of the variance step
is certified in Lean (U_E0095.lean: E0095_variance_step, E0095_variance_dominates, axioms
propext, Classical.choice, Quot.sound only). For (c), K' = I - L'/d_max(G') has gap
lambda_2(L')/d_max(G') = lambda_2/d_max(G') by (a), and d_max(G') > d.

For the hypercube corollary: the Laplacian of Q_d has eigenvalue 2 with multiplicity d (the d
weight-one characters), so r <= d - 1 applies. For abelian Cayley graphs: the eigenvalues are
d - sum_{s in S} chi(s) over characters chi; a non-real chi and its conjugate give the same
eigenvalue, so a simple nonzero eigenvalue needs a real (+-1-valued) character.

Proof of Theorem 2. By interlacing for a rank-one positive semidefinite update, lambda_2 <=
lambda_2' <= lambda_3. Write c_k = <phi_k, e>, so c_1 = 0, c_2^2 = c^2 and sum_k c_k^2 = |e|^2
= 2. An eigenvalue of L' that is not an eigenvalue of L is a root of

    f(lambda) = 1 + w sum_k c_k^2 / (lambda_k - lambda).

If c = 0 then phi_2 survives and g = 0, consistent with both bounds. If c != 0 then lambda_2 is
not an eigenvalue of L' (if L' psi = lambda_2 psi then either <e, psi> = 0, forcing psi in
span(phi_2) and <e, psi> = +-c|psi| != 0, or e lies in the range of L - lambda_2 = phi_2-perp,
contradicting c != 0), so g > 0. Case g < Delta: then lambda_2' is a root of f in (lambda_2,
lambda_3), and rearranging f = 0,

    w c^2 / g = 1 + w sum_{k>=3} c_k^2 / (lambda_k - lambda_2') .

The right side is at least 1, giving g <= w c^2, and at most 1 + 2w/(Delta - g) because each
lambda_k - lambda_2' >= Delta - g and the c_k^2 sum to at most 2; this gives
g (Delta - g + 2w) >= w c^2 (Delta - g), and dropping the g^2 term, g >= w c^2 Delta /
(Delta + 2w + w c^2). Case g = Delta: the upper bound min(w c^2, Delta) needs w c^2 >= Delta.
If lambda_2' = lambda_3 then either f has a root at lambda_3 or lambda_3 survives with c_3 = 0
and f(lambda_3) <= 0 (otherwise the root of f in (lambda_2, lambda_3) would exist by the
intermediate value theorem, f being -infinity at lambda_2^+ and continuous on (lambda_2,
lambda_3) when c_3 = 0, and would be a smaller eigenvalue). In both sub-cases w c^2 / Delta >=
1 + w sum_{k>=4} c_k^2/(lambda_k - lambda_3) >= 1. The lower bound at g = Delta reads
Delta >= w c^2 Delta/(Delta + 2w + w c^2), which is w c^2 <= Delta + 2w + w c^2, trivially
true. This proves Theorem 2.

Proof of Theorem 3 (the proven parts). The upper bound is interlacing. The end-to-end edge
produces C_n, whose algebraic connectivity is 2 - 2 cos(2 pi/n) = lambda_3(P_n) (the path's
eigenvalues are 2 - 2 cos(pi k/n), k = 0..n-1, the cycle's 2 - 2cos(2 pi k/n)). Why symmetric
chords can tie: the path's eigenvectors phi_k(x) = cos(pi k (x + 1/2)/n) are symmetric under
x -> n-1-x for even k and antisymmetric for odd k; the chord {j, n-1-j} has e = e_j - e_{n-1-j}
antisymmetric, so it perturbs only the odd-k sector, and lambda_3 (k = 2) survives in the even
sector untouched. The tie holds exactly when the lowest odd-sector eigenvalue is pushed up to
lambda_3 or beyond; the threshold 4(j+1) <= n is numerical (Section 5), not proven.

## 4. What is not done

- The finite-n optimum over perfect matchings is not characterised for any base graph; only
  the brute-force cases n <= 14 on the cycle are exact. Deciding the optimal matching is a
  combinatorial optimisation of a rank-n/2 perturbation and nothing here reduces it.
- For a general d-regular base graph G the random matching need not be optimal to leading
  order. Hermon-Sly-Sousi give cutoff at (1/h) log n where h is the entropy of the walk on the
  local "quasi-tree" limit; this equals the universal lower bound (d+1)/(d-1) log_d n of
  Lubetzky-Peres only when G is locally tree-like. For a base graph with many short cycles
  the random matching is strictly slower than that bound, and whether some other matching
  attains the bound is the residual open content of the question. I did not attack it.
- The path tie threshold 4(j+1) <= n and the SRW-optimal chord j* = floor(n/4) - 1 are
  numerical, with an exact sector-reduction argument but no closed-form proof.
- Equality gap(C_n + antipodal chord) = gap(C_n) is only shown numerically (to 1e-16 for
  n = 8..200); Theorem 1 gives only <=.
- The "important variation" for a general reversible chain with a Metropolized weighted edge is
  covered only through Theorem 2 (the algebraic-connectivity part) and Theorem 1(c); I did not
  derive the analogue of Theorem 1(b) for a non-uniform pi.

## 5. Checks

All scripts are in this directory with their outputs (*.out).

- single_edge_cycle_path.py: every chord of C_n, n in {8, 9, 12, 13, 20, 21, 40, 41, 80}: the
  Laplacian lambda_2 is unchanged to 1e-10 and the SRW gap never exceeds the cycle's (assertion
  passed). For odd n every chord strictly lowers the gap; for even n only the antipodal chord ties.
  Every chord of P_n: lambda_2 <= lambda_3(P_n), attained by the end edge and by the symmetric
  chords listed; the SRW-optimal chord is symmetric with j* = floor(n/4) - 1 in every case.
- cycle_chord_secular.py (second, independent method): the SRW second eigenvalue of C_n plus the
  chord {0,m} is cos(theta) with theta the smallest positive solution of
  tan(theta m/2) + tan(theta (n-m)/2) + tan(theta/2) = 0 (sector phi(0) = phi(m)) or of
  cot(theta m/2) + cot(theta (n-m)/2) + cot(theta/2) = 0 (sector phi(0) = -phi(m)) or of the
  Dirichlet family theta = pi k/m = pi k'/(n-m). Derived from the transfer-matrix ansatz on the
  two arcs; agrees with dense eigenvalues to 1.3e-15 over 11 values of n and up to 7 chords each.
- path_tie_threshold.py: the tie rule 4(j+1) <= n matched for every n from 6 to 129 and for
  n = 150, 151, 200, 201, 300, 301, 400 (a first guess, 4j < n-1, failed from n = 22 on and was
  corrected; the output records the corrected rule).
- first_order_bounds_check.py: Theorem 2's two bounds on 33,893 (edge, weight) pairs across six
  random regular graphs (d = 3, 4, 5; weights 0.05, 0.3, 1, 3) and three paths: maximum violation
  1.8e-15 (upper), 0 (lower). Hypercube Q_4 plus 3 random edges, 3000 samples: SRW gap never
  above the base 0.5 and lambda_2(L) never above 2; with 4 edges both rise (0.532, 2.248).
- cycle_matching_bruteforce.py: all perfect matchings of new edges on C_n, n = 6..14 (up to
  44,189 matchings at n = 14), gap, absolute gap, and the lazy walk's TV mixing time.
- random_matching_srw_tmix.py: non-lazy SRW on C_n plus a random matching, TV mixing time from
  a vertex: t_mix(1/4)/(3 log_2 n) = 0.937, 0.947, 0.955, 0.981, 1.002 for n = 1000, 4000, 16000,
  64000, 256000. random_matching_asymptotics.py: lambda_2(A) = 2.824, 2.825, 2.829, 2.828 for
  n = 1000..64000 against 2 sqrt 2 = 2.8284. Both are consistent with (A); neither proves it.
- Lean: U_E0095.lean compiled clean at the first attempt (lake env lean), both theorems depend
  on propext, Classical.choice, Quot.sound only.

The strongest case that I am wrong, and the check. Theorem 1(b) is the claim most likely to
hide an error, because it says an added edge can make a walk slower in the spectral sense,
which sounds paradoxical. The mechanism is that the stationary measure moves mass onto the
endpoints, so the variance denominator grows while the surviving slow mode keeps its Dirichlet
energy. The check that would expose an error is an exhaustive search for a chord of some cycle
whose SRW gap exceeds the cycle's; single_edge_cycle_path.py did that for nine values of n and
found none, and the secular-equation method confirms the same eigenvalues independently. The
second most likely error is a misattribution in (A); Section 6 says exactly what was verified
from the sources tonight and what is from memory.

## 6. Prior art

Web search was exhausted for the session before this task started; the checks below were made
by fetching arXiv abstract pages, the Semantic Scholar citation graph of Hermon-Sly-Sousi, and
the text of Wormald's survey.

- J. Hermon, A. Sly, P. Sousi, "Universality of cutoff for graphs with an added random
  matching", arXiv 2008.08564 (Ann. Probab. 2022). Abstract verified: for any sequence of
  bounded-degree graphs G_n with all components of size at least 3, the simple random walk on G_n
  plus a uniformly random perfect matching has cutoff w.h.p. This is the general form of
  Diaconis's random-matching question. The 16 papers citing it on Semantic Scholar include none
  on the optimal (rather than random) matching; two (Gerencser-Hendrickx 2023, arXiv 2307.09949;
  Feng-Gerencser 2024, arXiv 2411.07125) speed up the cycle with a few extra edges but only for
  non-reversible walks, which is a different question.
- E. Lubetzky, Y. Peres, "Cutoff on all Ramanujan graphs", arXiv 1507.04725 (GAFA 2016).
  Abstract verified: cutoff at (d/(d-2)) log_{d-1} n + s sqrt(log n) on every d-regular Ramanujan
  graph, and "d-regular Ramanujan graphs minimize the asymptotic L^p-mixing time for SRW among
  all d-regular graphs". For d = 3 this is the 3 log_2 n (1 - o(1)) lower bound for every cubic
  graph, hence for every matching on the cycle.
- E. Lubetzky, A. Sly, "Cutoff phenomena for random walks on random regular graphs", Duke Math.
  J. 153 (2010): cutoff for G(n,d) at (d/(d-2)) log_{d-1} n with window sqrt(log n). Cited from
  memory; not re-fetched tonight.
- Transfer to the cycle plus a random matching: N. Wormald, "Models of random regular graphs"
  (1999 survey), Section 4, text verified: Theorem 4.5 (Robinson-Wormald) gives G(n,3) contiguous
  to the Hamilton-cycle-weighted model, Corollary 4.21 uses the model "Hamilton cycle plus random
  matching" (H_n + G_{n,1}) to transfer the diameter of G(n,3), and the text credits Janson
  (1995) with the first explicit contiguity statement for perfect matchings. A fixed cycle plus a
  random matching (new edges only) has the same isomorphism-class distribution, so every a.a.s.
  isomorphism-invariant property of G(n,3) - Friedman's lambda_2 <= 2 sqrt 2 + eps, Lubetzky-Sly's
  cutoff window - holds a.a.s. for it.
- Alon-Boppana (Alon 1986; Nilli 1991): lambda_2(A) >= 2 sqrt(d-1) - o(1) for every d-regular
  graph. J. Friedman, "A proof of Alon's second eigenvalue conjecture" (Mem. AMS 2008):
  lambda_2 <= 2 sqrt(d-1) + eps a.a.s. for G(n,d). Both from memory; standard.
- B. Bollobas, F. Chung, "The diameter of a cycle plus a random matching", SIAM J. Discrete
  Math. 1 (1988): this is the source's [15]; Wormald's survey quotes their bounds as log_2 n - 10
  and log_2 n + log_2 log n + 10.
- The algebraic-connectivity facts used in Theorem 1(a) (monotonicity under edge addition,
  interlacing under a rank-one update) are classical (Fiedler 1973). I did not find the walk
  version 1(b) with the degree correction, nor the explicit two-sided bound of Theorem 2, in
  print, but both are elementary and may exist somewhere; I make no priority claim.

Nothing found settles the finite-n optimisation, and nothing found states the leading-order
answer for the cycle as an answer to Question 4, though every ingredient of it is published.
