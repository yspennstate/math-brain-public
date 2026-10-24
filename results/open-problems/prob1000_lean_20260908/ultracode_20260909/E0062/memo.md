# E0062: Rozikov's Problem 5 (ergodic theorem for Volterra operators on S^{m-1})

Written 2026-09-09. Ledger id E0062, source `qso_open_2009` (Rozikov, *Quadratic stochastic operators:
results and open problems*, arXiv:0902.4207), Problem 5, PDF p. 4.

## The problem as the source states it

Verbatim from the extracted text (p. 4; the `1/n` in the Cesaro mean is a displayed fraction that the
extractor dropped, the PDF shows it):

> On the basis of numerical calculations Ulam [44] conjectured that ergodic theorem holds for any QSO V,
> that is, the limit lim_{n→∞} (1/n) ∑_{k=0}^{n} V^k(x) exists for any x ∈ S^{m−1}. In [45] Zakharevich
> proved that this conjecture is false in general. In [3] the authors established a necessary condition
> for the ergodic theorem to hold for the following class of Volterra QSOs V : S^2 → S^2
> x' = x(1 + ay − bz), y' = y(1 − ax + cz), z' = z(1 + bx − cy), (9) where a, b, c ∈ [−1, 1].
> Theorem 3. [3] If the parameters a, b, c for the Volterra QSO (9) have the same sign and each is
> non-zero, then the ergodic theorem will fail for this operator.
> Problem 4. Is the condition of Theorem 3 sufficient for the ergodic theorem to hold?
> Problem 5. Find necessary and sufficient conditions on matrix A of Volterra QSO under which the ergodic
> theorem is true for the Volterra QSO on S^{m−1}, m ≥ 2.

The Volterra QSO is (7)-(8) of the source: (Vx)_k = x_k (1 + ∑_i a_ki x_i) with A = (a_ij) skew-symmetric
and |a_ij| ≤ 1. Zero entries are allowed. Two readings of "the ergodic theorem is true" are in use:

* (E) every initial point x ∈ S^{m-1} has a convergent Cesaro mean. This is the source's own wording
  ("for any x ∈ S^{m−1}") and the one Problem 5 inherits; I use it below.
* (G) the Cesaro mean converges for generic x (a.e., or a residual set). This is Ulam's original and the
  one used by Ganikhodjaev-Zanin in their 2012/2025 classification for m = 4.

The two readings differ on Volterra operators because every face of the simplex is invariant: under (E)
the operator is ergodic only if every face restriction is, under (G) a cyclic face of measure zero does
not count. The ledger row's statement ("for every initial point") is the source's, so the row is not
misstated.

## Findings

1. **Theorem (nondegenerate A, every m).** Suppose a_ij ≠ 0 for all i ≠ j and read the signs as a
   tournament T_A on {1,...,m} (i → j when a_ij > 0). Then the ergodic theorem in sense (E) holds for V
   if and only if T_A is transitive, i.e. after a permutation of the indices a_ij > 0 for all i < j.
   In that case every trajectory converges to a vertex. Equivalently: the ergodic theorem fails iff A has
   a 3×3 principal submatrix of the form (0, a, -b; -a, 0, c; b, -c, 0) with a, b, c nonzero of one sign.
   Proof below; the load-bearing analytic step is certified in Lean (`U_E0062.lean`, compiles clean,
   axioms propext / Classical.choice / Quot.sound only). The failure direction is the 2004
   Ganikhodjaev-Zanin theorem (the source's Theorem 3) applied to a face. Novelty is modest: both halves
   are the natural reading of R. Ganikhodzhaev's tournament theory, but I did not find the iff written
   down for general m in sense (E).

2. **Degenerate A: the sign pattern does not decide.** With zero entries allowed the necessary condition
   from 1 (no face carrying a nonzero same-sign 3-cycle) is not sufficient, and the answer to Problem 5
   cannot be a condition on the sign pattern of A alone. The witness is m = 4 with the 4-cycle-with-ties
   matrix

       A(a,b,c,d) = [[0, a, 0, -d], [-a, 0, b, 0], [0, -b, 0, c], [d, 0, -c, 0]],  a,b,c,d in (0,1],

   i.e. x1' = x1(1 + a x2 − d x4), x2' = x2(1 − a x1 + b x3), x3' = x3(1 − b x2 + c x4),
   x4' = x4(1 + d x1 − c x3). Its tournament is the directed 4-cycle 1 → 2 → 3 → 4 → 1 with the two
   diagonals tied; it has no 3-cycle, and every proper face of S^3 is ergodic (each 3-face has a zero
   coefficient, so E0061's Case 1 gives convergence there; every edge is a two-species map or a segment
   of fixed points). Numerically (two independent checks, section "Checks"):
   * for a = b = c = d = 0.5 the interior orbit runs round the heteroclinic cycle e1 → e4 → e3 → e2 → e1
     with visit lengths growing by the factor 2.922 per turn, and the Cesaro means oscillate without
     settling: the ergodic theorem fails in sense (E) and, on the evidence of the batch of starting
     points, in sense (G) as well;
   * for a = c = 0.9, b = d = 0.1, the same sign pattern, every orbit tried converges to a fixed point on
     the tied edge {1,3}, and the Cesaro means converge.
   So both behaviours occur inside one sign pattern. This is the "counterexample to a naive
   no-cyclic-subtournament conjecture" the integrator asked for, in the tie-allowed setting; in the strict
   setting no such counterexample exists (finding 1).

3. **Mechanism, and why the discrete map differs from replicator dynamics.** Near the vertex e1 the map
   multiplies x4 by (1+d), x2 by (1−a), and leaves x3 alone (the tie). Writing L_i = −log x_i and following
   one turn of the cycle, the two interleaved log-sizes obey

       L4 -> r1 L4,  r1 = log(1/(1−a)) log(1/(1−c)) / (log(1+b) log(1+d)),
       L3 -> r2 L3,  r2 = log(1/(1−b)) log(1/(1−d)) / (log(1+a) log(1+c)),

   plus O(1) corrections. The cycle sustains itself (visit lengths grow geometrically, Cesaro means
   diverge) when both ratios exceed 1; when one is below 1 the corresponding pair of species does not get
   crushed, the orbit leaves the cycle and lands on the attracting segment of the tied edge (for ac > bd
   the segment is {x1 e1 + x3 e3 : d/c < x3/x1 < a/b}, where both transversal multipliers are < 1). In
   continuous time the ratios would be ac/(bd) and bd/(ac), reciprocal, so at most one exceeds 1 and the
   time average converges to the game's optimal strategies; in discrete time the contraction rate
   −log(1−a) exceeds the expansion rate log(1+a), so both ratios can exceed 1 at once. The symmetric case
   has r1 = r2 = (log 2 / log 1.5)^2 = 2.922, which is the measured growth factor.

## Proof of finding 1

Notation: x(n) = V^n x, coordinates x_i(n) in [0,1], ∑_i x_i(n) = 1. Faces are invariant: if x_i = 0 then
(Vx)_i = 0, and if x_i > 0 then (Vx)_i ≥ 0 since |∑_j a_ij x_j| ≤ 1.

**Sufficiency (transitive ⇒ every trajectory converges).** Induct on m; m = 1 is trivial. Order the
indices so that a_1j > 0 for all j ≥ 2 (vertex 1 is the source of the transitive tournament). Then

    x_1(n+1) = x_1(n) (1 + f(n)),   f(n) = ∑_{j≥2} a_1j x_j(n) ≥ 0,

so x_1(n) is nondecreasing and bounded by 1. If x_1(0) > 0, then ∏_{k<n}(1 + f(k)) = x_1(n)/x_1(0) ≤
1/x_1(0), and ∏(1+f(k)) ≥ 1 + ∑ f(k) for nonnegative f, so ∑_k f(k) ≤ (1 − x_1(0))/x_1(0) < ∞
(Lean: `sum_le_of_prod`, `summable_of_prod`). Since a_1j x_j(n) ≤ f(n) and a_1j > 0, each x_j(n) → 0 for
j ≥ 2 (Lean: `dominated_tendsto_zero`), hence x(n) → e_1. If x_1(0) = 0 the trajectory lies in the face
{x_1 = 0}, where V restricts to the Volterra operator of the principal submatrix on {2,...,m}, whose
tournament is again transitive; apply the induction hypothesis. Every trajectory converges, so every
Cesaro mean converges.

**Necessity (a 3-cycle ⇒ failure).** A tournament that is not transitive contains a directed 3-cycle
i → j → k → i (standard: a tournament is transitive iff it is acyclic iff it has no 3-cycle). The face
F = {x : x_l = 0 for l not in {i,j,k}} is invariant and V|_F is the three-species Volterra operator of the
principal submatrix on {i,j,k}; in the source's parametrisation (9) this is (a,b,c) = (a_ij, a_ki, a_jk),
all nonzero and of one sign. By the source's Theorem 3 (Ganikhodjaev-Zanin 2004) the ergodic theorem
fails for V|_F: there is a point y in F whose Cesaro means under V|_F diverge. Since V|_F = V on F, the
Cesaro means of y under V diverge, so the ergodic theorem fails for V in sense (E). QED.

Remarks. (i) The theorem does not need |a_ij| < 1; a_ij = ±1 is allowed (a coordinate may then become
exactly 0 in one step, which only moves the orbit to a face). (ii) In sense (G) the necessity half is
false: if the tournament has a source (a row with all entries positive) the sufficiency argument shows
every interior orbit converges to that vertex, whatever the sub-tournament on the other vertices does;
this is class 1 of Ganikhodjaev-Zanin 2012 and it holds for every m by the same product argument. Sense
(G) for a strong tournament is a different problem (see "Prior art").

## What is not done

* Finding 2 is numerical. A proof that the symmetric 4-cycle-with-ties operator is non-ergodic would
  follow the 2004 note's pattern (boundary omega-limit set, itinerary, geometric growth of visit times)
  and needs the return-map estimates of finding 3 made rigorous, including control of the tied coordinate
  during a visit (it changes by O(1) on the log scale, not proportionally to the visit length). A proof
  that the (0.9, 0.1, 0.9, 0.1) operator is ergodic for every point is harder still: all fixed points off
  the segment are unstable, but ruling out exceptional orbits along the boundary network is open.
* A necessary and sufficient condition for degenerate A, sense (E), is therefore still open; finding 2
  says it must involve magnitudes, not just signs. The natural conjecture from finding 3 is that, for a
  degenerate pattern with no strict 3-cycle, the ergodic theorem fails iff some heteroclinic cycle of the
  boundary network has all its return-map ratios > 1; I have not tested this beyond the 4-cycle.
* Sense (G) for general m (Ulam's original question) is not touched: the 2012/2025 Ganikhodjaev-Zanin
  classification for m = 4 with nonzero entries is the state of the art, and its strong-tournament case
  rests on visit times tending to infinity rather than growing geometrically, which is not by itself
  enough for Cesaro divergence.

## Checks

Scripts in this directory; every run was a single process on this PC.

1. `e0062_fourcycle.py` (single orbits, 2,000,000 steps, log coordinates, renormalised each step).
   Symmetric a = b = c = d = 0.5 from (0.3, 0.2, 0.25, 0.25): Cesaro means at n = 2^13 ... 2^20 keep
   moving by 0.1 to 0.2 per doubling with no decay (e.g. (0.375, 0.208, 0.219, 0.198) at 2^19 and
   (0.198, 0.304, 0.320, 0.178) at 2^20); vertex visits in the order 1, 4, 3, 2 repeat, and the visit
   durations grow by 2.922, 2.922, 2.922, 2.922 over the last four turns. The same script at
   (0.9, 0.1, 0.9, 0.1) from two starting points converges: Cesaro means (0.488, 0, 0.512, 0) and
   (0.5172, 0, 0.4828, 0) fixed to four decimals from n = 2^17 on, x2 and x4 at log-size -1e6.
2. `e0062_batch2.py` (80 starting points: Dirichlet(1), Dirichlet(0.2) near the boundary,
   Dirichlet(5) central; 100,000 and 400,000 steps; outputs `batch2.out`, `batch2_400k.out`).
   At 400,000 steps: symmetric 0.5 and 0.3: 80/80 orbits cycling, Cesaro drift between 3n/4 and n
   between 0.003 and 0.20, measured duration growth per turn median 2.922 (predicted 2.922) and 1.848
   (predicted 1.848). (0.5, 0.4, 0.5, 0.4), both ratios > 1: 44 orbits converge onto the segment
   x3/x1 in [0.803, 1.241] of the tied edge (predicted (0.8, 1.25)), 31 cycle, 5 undecided; the two
   attractors coexist. (0.9, 0.1, 0.9, 0.1): 80/80 converge, limits x3/x1 in [0.13, 6.78] inside the
   predicted (1/9, 9), drift at most 4e-4 and median 2e-6. (0.6, 0.2, 0.6, 0.2): 78/80 converge, 2 still
   drifting at 2e-3, none cycling.
3. `e0062_mpcheck.py`: the symmetric map iterated directly in mpmath at 800 decimal digits (no log
   trick, no renormalisation) for 20,000 steps against the float log-coordinate iteration: maximum
   relative difference of the log-coordinates 4.2e-10, identical vertex-visit schedule (20 visits, the
   last at step 19,612), coordinates summing to 1 within 1e-799. So the log method is faithful, and the
   growth of the visit durations (238, 284, 328, 403, 475, 601, 721, 932, ..., 14431, 19612) is a
   property of the map, not of floating point.
4. `U_E0062.lean` compiles in the erdos_fc project (Mathlib) with axioms propext, Classical.choice,
   Quot.sound only; it certifies the product-to-sum step and the "dominated coordinate tends to zero"
   step of the sufficiency proof. Copy in this directory.

Second-independent-way status: the non-ergodicity of the symmetric operator is supported by (1) direct
simulation of the Cesaro means, (2) the return-map ratio computed from the coefficients alone matching
the measured growth factor to three decimals, and (3) an arbitrary-precision replication of the visit
schedule. The convergence of the (0.9, 0.1) operator is supported by (1) and (2) (limits land inside the
predicted segment).

## The strongest case that I am wrong

The theorem (finding 1) leans on the 2004 note through the source's Theorem 3, and on the standard fact
that a non-transitive tournament has a 3-cycle; both were checked (E0061-A003 read the note in full). The
weak point is finding 2. A cycling orbit whose visit lengths grow geometrically has coordinates of size
exp(-10^5) and beyond; a sceptic would say the float log iteration is manufacturing the cycle. The one
check that would confirm that: iterate the same orbit exactly, without logs, at a precision that covers
the coordinates. That is check 3 above (800 digits, 20,000 steps, identical schedule to the step), and it
did not confirm the doubt. The remaining gap is logical, not numerical: the cycle is observed and its
growth factor explained, but the persistence of the cycle for all n is not proved.

## Prior art

Search phrases used (WebSearch, 2026-09-09): "Volterra quadratic stochastic operator" "ergodic theorem"
necessary and sufficient; Ganikhodzhaev Zanin ergodic Volterra non-ergodic tournament; "Volterra"
quadratic stochastic operator "non-ergodic" S^3; Saburov ergodicity Volterra Ulam Zakharevich; Rozikov
Volterra ergodic tournament 2020-2025; Jamilov Mukhamedov Volterra ergodic Cesaro.

* N. Ganikhodjaev, D. Zanin, *Ergodic Volterra quadratic transformations of symplex*, arXiv:1205.3841
  (2012, Russian), republished in English as *Ergodic Volterra Quadratic Mappings of the Simplex*, in
  Networks, Games, and Dynamics (Trends in Mathematics), Springer 2025, doi 10.1007/978-3-032-09176-5_9.
  The "three-dimensional simplex" there is S^3, i.e. m = 4. With nonzero entries and the generic-point
  definition (G) they split A into: a nonnegative row (ergodic, every interior orbit converges to that
  vertex), a nonpositive row with a cyclic face (non-ergodic, reduced to the 2004 note), and the strong
  tournament (Theorem 3: non-ergodic). Read in full (text in `gz2012.txt`). The strong-tournament proof
  shows the time per visit of the vertex e1 tends to infinity (their Theorem 4) and that the average time
  away from the vertices is zero (Theorem 5); it does not show geometric growth of the visits, which is
  what Cesaro divergence needs, so I record it as claimed. Zero entries are excluded by their standing
  assumption ("for simplicity the a_ij are different from 0 and 1"), so the 4-cycle-with-ties operator
  is outside their classification, and under sense (E) their class 1 is not ergodic when a face carries a
  cycle. Neither paper addresses Problem 5 for general m.
* N. Ganikhodjaev, U. Jamilov, R. Mukhitdinov, *Hamiltonian cycle on the set of genotypes and
  non-ergodic quadratic stochastic operators*, arXiv:1204.1809 (2012): extremal Volterra operators
  (entries +-1), m = 2, 3, 4, sense (G): non-ergodic if the tournament has a Hamiltonian cycle or a source
  vertex over a non-ergodic face; ergodic for the acyclic class and for a sink vertex over a 3-cycle.
  Consistent with finding 1 (all four classes are strict tournaments; in sense (E) the sink-over-3-cycle
  class is non-ergodic through its face) and with remark (ii). General m is announced as future work.
* M. Saburov, *On divergence of any order Cesaro mean of Lotka-Volterra operators*, Ann. Funct. Anal.
  6 (2015): a class of non-ergodic Volterra operators in every dimension containing Zakharevich's and
  Ganikhodjaev-Zanin's; a sufficient condition for failure, not a characterisation.
* Ganikhodjaev-Zanin 2004 (Russian Math. Surveys 59:3), the source's [3]: the failure theorem for the
  3-species cyclic case, used above.
* Jamilov, Scheutzow, Wilke-Berenguer, *On the random dynamics of Volterra quadratic operators*, ETDS
  2017; Ganikhodjaev, Ganikhodjaev, Jamilov, *Quadratic stochastic operators and zero-sum game
  dynamics*, ETDS 2015: related, not on Problem 5.

Nothing found states a necessary and sufficient condition for general m, in either sense, and nothing
found treats zero entries. The nondegenerate every-point theorem may be folklore in the Tashkent school
(it is the obvious combination of the 1993 tournament theory with the 2004 note) but I did not find it
written. The web-search budget of the session ran out after the six searches above, before a search for
a 2025-2026 follow-up to the Springer chapter; that is the one search left undone.
