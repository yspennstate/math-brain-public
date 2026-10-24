# E0066 - Rozikov Problem 13: trajectories of quadratic bistochastic operators

Date: 2026-09-09. Worker: claude ultracode E0066. Budget used: about two hours.

## 1. The problem as the source states it

Rozikov, "Quadratic stochastic operators: results and open problems", arXiv 0902.4207, Section 10, p. 7-8
(source_id qso_open_2009). Verbatim from the PDF text:

> Let x in S^{m-1}. Denote by x_down the point x_down = (x[1], ..., x[m]) in S^{m-1}, where x[1] >= ... >= x[m]
> are the coordinates of x in non-increasing order. If x, y in S^{m-1} and sum_{i=1}^k x[i] <= sum_{i=1}^k y[i],
> k = 1, ..., m, then we say that y majorizes x and write x < y. [...]
> Definition 4. An arbitrary continuous operator V : S^{m-1} -> S^{m-1} satisfying the condition
> V(x) < x, x in S^{m-1} (16) is called a bistochastic operator.
> Theorem 8. [21],[22] 1) If V : S^{m-1} -> S^{m-1} is a bistochastic operator, then the coefficients P_{ij,k}
> satisfy the conditions sum_{i,j=1}^m P_{ij,k} = m for all k (a); sum_{j=1}^m P_{ij,k} >= 1/2 for all i, k (b);
> sum_{i,j in I} P_{ij,k} <= t for all t, k (c), where I = {i_1, ..., i_t} is an arbitrary subset of {1, ..., m}
> containing t elements. 2) If (c) holds for a QSO V then it is a bistochastic.
> [...]
> Problem 13. Investigate the behavior of trajectories of the bistochastic quadratic operators.

Here "<" is the majorization order (partial sums of the decreasing rearrangement of V(x) are at most those of
x, for every k), so a bistochastic operator moves every point toward the barycenter in the majorization
sense. The ledger row states the problem correctly. It is an open-ended "investigate", not a yes/no question.

## 2. Finding

Two things.

(i) The basic convergence theorem the integrator's hint asks for is already in the literature, with the
permutation operators as the periodic examples: for every continuous bistochastic operator (quadratic or not)
every trajectory converges to a periodic orbit whose points are coordinate permutations of one vector; the
omega-limit set is finite (at most m! points); V is regular (all trajectories converge) if and only if it
has no periodic points other than fixed points; strictly regular operators (unique fixed point, the
barycenter) form a dense set containing the relative interior of the polytope of quadratic bistochastic
operators. See Section 6 for the citations. The earlier attempt A001 (entropy is a Lyapunov function) is a
weaker form of the same observation.

(ii) One statement that I did not find in the accessible literature, proved below (Theorem 2):

> **Rigidity of interior periodic points.** Let V be a quadratic bistochastic operator on S^{m-1}. If V has a
> periodic point (in particular a fixed point) in the interior of the simplex whose coordinates are pairwise
> distinct, then V is a coordinate permutation operator (the identity, in the fixed-point case).

So for a quadratic bistochastic operator that is not a coordinate permutation, every interior periodic point
has at least two equal coordinates, and a trajectory whose limit cycle lies in the interior of the simplex
either converges or converges to a cycle of permutations of a vector with a repeated coordinate. This sharpens
the m = 3 theorem of Abdulghafor, Shahidi, Zeki and Turaev (2016), who show that a non-permutation doubly
stochastic quadratic operator on S^2 has no interior periodic points and remark that this fails in higher
dimensions; the rigidity theorem says exactly where it fails: at vectors with repeated coordinates. Their
higher-dimensional failure is illustrated by the linear operator V(x) = ((x1+x2)/2, (x1+x2)/2, x4, x3) on S^3,
which has the interior 2-cycle (0.3, 0.3, 0.1, 0.3) <-> (0.3, 0.3, 0.3, 0.1).

Status I claim: partial. The trajectory theorem is literature; the rigidity theorem is new as far as my search
could tell, and its proof is complete and elementary. Since I could not read Ganikhodzhaev's 1993 thesis or the
Uzbek Mathematical Journal papers, the rigidity theorem may be known there.

## 3. The trajectory theorem (literature), with a self-contained proof

Notation: S_k(x) = x[1] + ... + x[k], the sum of the k largest coordinates. V(x) < x means S_k(V(x)) <= S_k(x)
for k = 1, ..., m (with S_m = 1 always).

**Theorem 1** (Ganikhodzhaev 1993 thesis, as quoted by Makhmudov 2021, Theorem 2.1; the argument is Shahidi
2007, proof of Theorem 4.1, written there for the reverse order). Let V : S^{m-1} -> S^{m-1} be continuous
with V(x) < x for all x. For every x0 there are a vector y in S^{m-1} and an integer p >= 1 with p <= m!/(product
of the factorials of the multiplicities of the distinct values of y) such that the omega-limit set of x0 is a
periodic orbit {z_0, ..., z_{p-1}} of V, every z_r is a coordinate permutation of y, V(z_r) = z_{r+1 mod p}, and
x(kp + r) -> z_r as k -> infinity for each r. In particular V is regular iff it has no periodic points other
than fixed points, and every periodic orbit of a bistochastic operator consists of coordinate permutations of a
single vector.

Proof. Step 1. Since x(n+1) < x(n), each S_k(x(n)) is nonincreasing in n and nonnegative, hence converges to
some s_k. Therefore x(n)[k] = S_k(x(n)) - S_{k-1}(x(n)) converges to y_k := s_k - s_{k-1}; y is nonincreasing,
nonnegative, sums to s_m = 1. So the sorted vector x(n)_down converges to y.

Step 2. Sorting is continuous (the k-th largest coordinate is a continuous function). If x(n_j) -> z then
x(n_j)_down -> z_down, so z_down = y: every omega-limit point is a coordinate permutation of y. The set of
coordinate permutations of y has m!/prod(multiplicities!) elements, so the omega-limit set is finite (and
nonempty by compactness).

Step 3 (a finite omega-limit set of a continuous map on a compact metric space is a periodic orbit, and the
trajectory converges to it). Write omega = {z_1, ..., z_q}. V(omega) is contained in omega (if x(n_j) -> z then
x(n_j + 1) -> V(z)). Let 3 delta be the minimum distance between distinct points of omega (if q = 1 the whole
sequence converges to z_1, since a sequence in a compact space with a single limit point converges). By
uniform continuity choose epsilon in (0, delta] with d(u, v) < epsilon implying d(V u, V v) < delta. The
distance from x(n) to omega tends to 0 (otherwise a subsequence stays at distance >= eta from omega and has a
limit point outside omega). Fix N with dist(x(n), omega) < epsilon for n >= N and let a(n) be the index of the
unique point of omega within epsilon of x(n). Then d(x(n+1), V(z_{a(n)})) < delta and d(x(n+1), z_{a(n+1)}) <
epsilon <= delta, so d(V(z_{a(n)}), z_{a(n+1)}) < 2 delta < 3 delta and hence V(z_{a(n)}) = z_{a(n+1)}. So from N
on, the index sequence follows the map V restricted to omega. That sequence in a finite set is eventually
periodic; every point of omega is a limit point of the trajectory, hence is visited infinitely often, hence
lies on the eventual cycle; in particular z_{a(N)} itself lies on the cycle. So V permutes omega cyclically,
p = q, and after relabelling a(N + kp + r) = r for all k. Thus x(N + kp + r) lies in the epsilon-ball of z_r for
all k, all its limit points lie in omega intersected with that closed ball, which is {z_r}, and by compactness
x(N + kp + r) -> z_r. QED.

Remarks. The permutation of coordinates taking z_r to z_{r+1} may depend on r (V is nonlinear), so p is not a
priori bounded by the maximal order of an element of the symmetric group, only by the number of distinct
permutation vectors of y. For the coordinate permutation operator V(x)_k = x_{sigma(k)} (a quadratic
bistochastic operator, P_{ij,k} = (delta_{i,sigma(k)} + delta_{j,sigma(k)})/2), a point with distinct coordinates
has period equal to the order of sigma; these are the periodic examples, and they show that trajectories of
bistochastic quadratic operators need not converge.

## 4. The rigidity theorem (new, as far as the search shows)

**Theorem 2.** Let V be a quadratic stochastic operator on S^{m-1} (coefficients P_{ij,k} >= 0, P_{ij,k} =
P_{ji,k}, sum_k P_{ij,k} = 1) with V(x) < x for every x. If V(y) = y for some y in the interior of the simplex with
pairwise distinct coordinates, then V is the identity, P_{ij,k} = (delta_{ik} + delta_{jk})/2.

**Corollary 3.** If a quadratic bistochastic operator V has a periodic point y in the interior of the simplex
with pairwise distinct coordinates, then V is a coordinate permutation operator.

Proof of the corollary from the theorem. By Theorem 1 the orbit of y consists of coordinate permutations of y,
so V(y) = sigma(y) for a coordinate permutation sigma, unique because the coordinates of y are distinct. The
operator W = sigma^{-1} o V is again a quadratic stochastic operator (its coefficients are P_{ij,sigma(k)}), and
W(x) has the same sorted vector as V(x), so W(x) < x for all x. W fixes y, so W is the identity by Theorem 2
and V = sigma. QED.

Proof of Theorem 2, by induction on m. For m = 1 the simplex is a point and the only operator is the identity.
Let m >= 2. Relabel the coordinates so that y_1 > y_2 > ... > y_m > 0 (conjugating by a coordinate permutation
preserves bistochasticity and fixes the identity operator).

Step A: first-order condition at the fixed point. Near y the largest coordinate of x is x_1 (strict inequality
y_1 > y_2), and V(x) < x gives V_1(x) <= x[1] = x_1. So g(x) = x_1 - V_1(x) is a smooth function which is
nonnegative on a neighbourhood of y in the simplex and vanishes at y. Since y is an interior point, for every
tangent direction d = e_j - e_i both y + t d and y - t d are admissible for small t, so d . grad g(y) = 0: all
partial derivatives of g at y are equal, i.e. d_j V_1(y) = delta_{j1} - c for a constant c. Euler's identity for
the degree-2 form V_1 gives sum_j y_j d_j V_1(y) = 2 V_1(y) = 2 y_1, so y_1 - c = 2 y_1 and c = -y_1. Since
d_j V_1(y) = 2 sum_i P_{ij,1} y_i, we get

    (F)   sum_i P_{ij,1} y_i = (delta_{j1} + y_1)/2   for every j.

Step B: the first slice is the identity's. (Condition (c) is used below as a necessary condition; it follows
in one line from V(x) < x: at the point x uniform on I, x_i = 1/t for i in I, one has V_k(x) = t^{-2} sum_{i,j in I}
P_{ij,k} <= x[1] = 1/t.) Put p = P_{11,1} and a_i = P_{i1,1} for i >= 2. Condition (c) of
Theorem 8 with I = {1} union J, J a subset of {2, ..., m} of size s, reads p + 2 sum_{i in J} a_i + sum_{i,j in J}
P_{ij,1} <= s + 1, hence sum_{i in J} a_i <= (s + 1 - p)/2; for J = {i} this is a_i <= 1 - p/2. The bound
f(s) = (s + 1 - p)/2 is concave in s, so by Abel summation against the decreasing weights y_2 > ... > y_m the
greedy allocation is extremal: sum_{i >= 2} a_i y_i <= (1 - p/2) y_2 + (1/2)(y_3 + ... + y_m) = (1 - p/2) y_2 +
(1 - y_1 - y_2)/2. Now (F) at j = 1 says p y_1 + sum_{i >= 2} a_i y_i = (1 + y_1)/2. Combining,

    (1 + y_1)/2 <= p y_1 + (1 - p/2) y_2 + (1 - y_1 - y_2)/2,  i.e.  (1 - p)(y_1 - y_2/2) <= 0.

Since y_1 > y_2 > 0 we have y_1 - y_2/2 > 0, so p >= 1, so P_{11,1} = 1. Then a_i <= 1/2 for all i >= 2, and (F) at
j = 1 becomes sum_{i >= 2} a_i y_i = (1 - y_1)/2 = sum_{i >= 2} y_i / 2 with all y_i > 0, which forces a_i = 1/2 for
every i >= 2. Condition (c) with I = {1, i} gives 1 + 1 + P_{ii,1} <= 2, so P_{ii,1} = 0. Finally (F) at j >= 2
reads (1/2) y_1 + sum_{i >= 2} P_{ij,1} y_i = y_1/2, so P_{ij,1} = 0 for all i, j >= 2. Hence P_{ij,1} = (delta_{i1}
+ delta_{j1})/2 and V_1(x) = x_1 identically. Also P_{11,k} = 0 for k >= 2 and sum_{k >= 2} P_{1j,k} = 1/2 for j >= 2.

Step C: reduction to the face. Write x = (x_1, (1 - x_1) z) with z in S^{m-2} and x_1 < 1. For k >= 2,

    V_k(x) = (1 - x_1) [ x_1 (B z)_k + (1 - x_1) U_k(z) ],   B_{kj} = 2 P_{1j,k},   U_k(z) = sum_{i,j >= 2} P_{ij,k} z_i z_j,

where B is a column-stochastic nonnegative matrix on {2, ..., m} (sum_k B_{kj} = 1 by Step B) and U is a quadratic
stochastic operator on S^{m-2} (its coefficients are symmetric, nonnegative, and sum to 1 over k >= 2 because
P_{ij,1} = 0 for i, j >= 2). So V(x) = (x_1, (1 - x_1) W(z)) with W(z) = x_1 B z + (1 - x_1) U(z).
Majorization passes to the reduced vectors: by the Hardy-Littlewood-Polya characterization, for vectors of
equal sum u < v iff sum phi(u_i) <= sum phi(v_i) for every convex phi; applying it to V(x) < x, the common
coordinate x_1 cancels and the factor (1 - x_1) > 0 is absorbed into phi, giving W(z) < z for every z in S^{m-2}
and every x_1 in [0, 1). Taking x_1 = 0 shows U is bistochastic on S^{m-2}; letting x_1 -> 1 (the set {u : u < z}
is closed) shows B z < z for every z, and a column-stochastic matrix with this property is doubly stochastic
(B applied to the barycenter u must be majorized by u, and only u is, so B u = u, i.e. the rows of B sum to 1).

Step D: the fixed point splits. Put z* = (y_2, ..., y_m)/(1 - y_1), an interior point of S^{m-2} with pairwise
distinct coordinates. V(y) = y gives y_1 B z* + (1 - y_1) U(z*) = z*, with B z* < z* and U(z*) < z*. The function
Phi(v) = sum v_i^2 is strictly convex and Schur-convex, so Phi(B z*) <= Phi(z*), Phi(U z*) <= Phi(z*) and
Phi(z*) <= y_1 Phi(B z*) + (1 - y_1) Phi(U z*) <= Phi(z*). Equality in Jensen with 0 < y_1 < 1 forces B z* = U(z*),
and then both equal z*.

Step E: conclusion. U is a quadratic bistochastic operator on S^{m-2} fixing the interior point z* with distinct
coordinates, so U is the identity by the induction hypothesis: P_{ij,k} = (delta_{ik} + delta_{jk})/2 for i, j, k
>= 2. B is doubly stochastic with B z* = z* and z* has distinct coordinates, so B is the identity matrix (the
classical argument: the largest coordinate of z* is reproduced only if the corresponding row of B is a unit
vector, then that column is a unit vector, and one recurses): P_{1j,k} = delta_{jk}/2 for j, k >= 2. Together
with Step B every coefficient agrees with the identity operator's. QED.

Where the hypotheses are used. "Pairwise distinct" is needed twice: y_1 > y_2 in Step B (the inequality
y_1 - y_2/2 > 0 only needs y_1 > y_2/2, but the induction needs z* to have distinct coordinates) and in Step E.
"Interior" is needed for the two-sided perturbation in Step A and for y_i > 0 in Step B. Both are necessary:
the linear averaging operator ((x1+x2)/2, (x1+x2)/2, x3) on S^2 is bistochastic, not the identity, and fixes
every interior point with x1 = x2; and on the boundary the LP below finds non-identity operators fixing (a, b, 0).
Quadraticity is necessary too: a continuous bistochastic map can be the identity near y and not globally.

## 5. Checks

All scripts are in this directory; they ran single-process on this laptop.

qbo_trajectories.py (output qbo_trajectories.out). 191 quadratic bistochastic operators on S^1, S^2, S^3:
the explicit examples of Sections 3-4, plus random boundary points of the polytope B_m (a random balanced
cubic matrix pushed toward the centre operator until condition (c) is tight), their compositions with random
coordinate permutations, and their convex mixtures with permutation operators. For each operator: (a) the
worst slack in condition (c) is -1.8e-15 (all satisfy (c)); (b) V(x) < x on 600 random x per operator and on the
vertices, zero failures - an independent check of Theorem 8 part 2, since the operators were built from (c) and
the majorization is tested directly; (c) along 6-8 trajectories of 3000 steps per operator the partial sums
S_k are nonincreasing at every step, zero failures; (d) the sorted vector over the last 400 iterates has spread
at most 1.6e-5 (parabolic convergence toward the barycenter is slow); (e) every tail locked to a period.
Periods observed: m = 2 only 1; m = 3 only 1 and 3 (the 3-cycle permutation operator); m = 4 only 1 and 2 (the
permutation operator and the linear averaging example, whose interior 2-cycle has a repeated coordinate,
as Corollary 3 requires). Every random non-permutation operator was regular (all trajectories converged).
A first version of this script iterated the raw quadratic form without renormalising; the mass sum V(x) =
(sum x)^2 then drifts doubly-exponentially under rounding and every trajectory collapsed to 0 after ~60 steps.
The published run renormalises each iterate (V is homogeneous of degree 2, so this is the same map on the
simplex).

qbo_periodic_lp.py and qbo_period_sweep.py (outputs *.out). Realisability of a prescribed cycle of permutation
vectors of y as a periodic orbit of some quadratic bistochastic operator is a linear-programming feasibility
problem (V(y) is linear in P, and B_m is cut out by (5) and (c)); each feasible P is re-verified by direct
iteration and a random majorization test, and two random objectives are optimised so that a non-permutation
solution is found whenever the feasible polytope is more than one point. Results: m = 3, 24 random base vectors
(12 interior with distinct coordinates, 12 boundary (a, b, 0)), all cyclic orders: the realisable 2-cycles and
3-cycles are exactly those of the 3 transpositions and 2 three-cycles, realised in the interior only by the
permutation operators (0 non-permutation solutions in 60 + 240 cycles) and on the boundary also by
non-permutation operators for the 2-cycles; no cycle of length 4, 5 or 6 is realisable at all (720 + 1440 +
1440 cyclic orders per kind, all infeasible). m = 4, 10 random base vectors, all 23 two-cycles exhaustively
and 60 sampled 3- and 4-cycles each: in the interior every realisable cycle is realised only by the
permutation operator; on the boundary non-permutation solutions appear. This is consistent with Corollary 3
and was the observation that led to it.

qbo_fixed_point_rigidity.py (output qbo_fixed_point_rigidity.out). Direct LP test of Theorem 2: for m = 3, 4, 5
and 20 random interior points with pairwise distinct coordinates each, twelve LP vertices of the set of
quadratic bistochastic operators fixing the point all coincide with the identity to 2.5e-13. Controls: a point
with repeated coordinates and a boundary point give operators at distance 1.000 from the identity, as the
theorem's hypotheses predict.

Lean (U_E0066.lean, compiled clean on the first attempt, log lean_compile1.log, axioms propext,
Classical.choice, Quot.sound only): (i) a nonincreasing real sequence bounded below converges (Step 1 of
Theorem 1); (ii) the coordinate permutations of a vector in R^m form a set of at most m! points (the bound on
the omega-limit set); (iii) |2x(1-x) - 1/2| <= |x - 1/2| on [0,1], i.e. the genuinely quadratic operator
V(x1, x2) = (2 x1 x2, x1^2 + x2^2) is bistochastic. The rigidity proof itself is not formalised.

## 6. Prior art

Search route: the session's WebSearch budget was exhausted before this task, and Semantic Scholar and the
arXiv API returned HTTP 429, so the search ran through the OpenAlex API (three queries, 90 records, saved in
prior_art/openalex_search.txt) and the arXiv PDFs it pointed to (texts in prior_art/). The phrases that found
the relevant items were "doubly stochastic quadratic operators", "dissipative quadratic stochastic operators"
and "bistochastic quadratic operators".

- R. Ganikhodzhaev, On the definition of bistochastic quadratic operators, Russian Math. Surveys 48:4 (1993),
  and his 1993 doctoral thesis, cited by Makhmudov (below) for Theorem 2.1: for a quadratic bistochastic
  operator the omega-limit set of every point is finite; P o V is bistochastic for every coordinate
  permutation P; the polytope has finitely many extreme points.
- F. Shahidi, On dissipative quadratic stochastic operators, arXiv 0708.1813 (2007), Appl. Math. Inf. Sci.
  2008. Theorem 4.1 and its proof: for V x > x (the reverse order) the partial sums of the sorted vector are
  monotone, the sorted vector converges, every omega-limit point is a rearrangement of the limit, the
  omega-limit set has at most m! points and the trajectory splits into p convergent subsequences cyclically
  permuted by V. The argument applies verbatim to V x < x; this is Steps 1-2 of Theorem 1 above (Step 3 is
  asserted there without proof).
- R. Ganikhodzhaev, F. Shahidi, Doubly stochastic quadratic operators and Birkhoff's problem, Linear Algebra
  Appl. 432 (2010) 24-35, arXiv 0802.1100: criterion (c), the polytope, extreme points, Birkhoff analogue.
- F. Shahidi, Doubly stochastic operators on a finite-dimensional simplex, Siberian Math. J. 50 (2009); and
  arXiv 1211.5639 (2012), "except for certain points the trajectory tends to the center of the simplex".
- R. Abdulghafor, F. Shahidi, A. Zeki, S. Turaev, Dynamics of doubly stochastic quadratic operators on a
  finite-dimensional simplex, Open Math. 14 (2016) 509-519: if a d.s.q.o. has no periodic points then every
  trajectory converges; a non-permutation d.s.q.o. has no periodic points in the interior of S^2, and this
  fails in higher dimensions; classification of the dynamics of the extreme points on S^2. (Only the abstract
  was accessible; the De Gruyter PDF download returned an empty file.)
- M. Saburov, Dynamics of double stochastic operators, J. Phys. Conf. Ser. 697 (2016); On regularity of
  diagonally positive quadratic doubly stochastic operators, Results Math. 72 (2017); On regularity of positive
  quadratic doubly stochastic operators, Math. Notes 103 (2018): sufficient conditions for regularity.
- M. Makhmudov, Description of the set of strictly regular quadratic bistochastic operators and examples,
  Discontinuity, Nonlinearity, and Complexity 10 (2021), arXiv 2001.10444: "the trajectory of any initial point
  converges to a periodic orbit"; Theorem 2.2 ([Saburov 2016], [Abdulghafor et al. 2016]): a bistochastic
  operator is regular iff it has no periodic points except fixed points; all operators in the relative
  interior of the polytope are strictly regular and the strictly regular ones are dense.
- Related but different order: Mukhamedov and Embong, On b-bistochastic quadratic stochastic operators, J.
  Inequal. Appl. 2015, and sequels (b-order on unsorted partial sums; those operators are regular).

Not found in any of these: the rigidity statement of Theorem 2 / Corollary 3. Abdulghafor et al.'s m = 3
theorem is its m = 3 case (for distinct coordinates), and their remark that it fails for m >= 4 is explained
by the repeated-coordinate examples.

## 7. What is not done

- The rigidity theorem is proved for quadratic operators only; the natural generalisation to polynomial
  stochastic operators of any fixed degree is untested.
- Periodic points with repeated coordinates are not classified; the LP evidence for m = 3 suggests that no
  quadratic bistochastic operator on S^2 has a periodic orbit of length 4, 5 or 6 (interior or boundary),
  which would make 3 the maximal period on S^2. Not proved.
- Whether a quadratic bistochastic operator can have a periodic orbit whose period exceeds the maximal order
  of an element of the symmetric group (i.e. visits permutations not generated by one permutation) is open;
  by Corollary 3 such an orbit cannot be interior with distinct coordinates.
- Ganikhodzhaev's thesis and the Uzbek Math. J. papers could not be read; the rigidity theorem may be there.

## 8. The strongest case that I am wrong, and the check

The weak points of the rigidity proof are Step A (the two-sided first-order condition needs V_1(x) <= x_1 on
a full neighbourhood of y in the simplex, which holds because y_1 > y_2 strictly and y is interior) and Step C
(majorization of (x_1, (1-x_1) u) against (x_1, (1-x_1) v) is equivalent to u < v; this is the
convex-function characterization with the common coordinate cancelled). If either failed, the LP in
qbo_fixed_point_rigidity.py would have produced a non-identity bistochastic operator fixing a generic interior
point at m = 3, 4 or 5; over 60 base points and 720 LP vertices the maximal deviation from the identity is
2.5e-13, while the two controls (repeated coordinate, boundary point) produce deviation 1.0. The LP encodes
bistochasticity through condition (c), and (c) was independently confirmed to imply V(x) < x on 600 random
points for each of 191 operators. I also re-derived Step B's inequality by hand a second time: the Abel-summation
bound reduces to (1 - p)(y_1 - y_2/2) <= 0, which needs only y_1 > y_2/2, weaker than what is assumed.
