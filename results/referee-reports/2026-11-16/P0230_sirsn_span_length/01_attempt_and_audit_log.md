# P0230 attempt: total length of the SIRSN on k uniform points (Aldous, SIRSN paper, Open Problem 35)

agent A, 16 Nov 2026. Status: SKETCH, provisional. Reduces the missing upper bound to an excursion
tail; the axioms used must be checked word for word against Aldous, EJP 2014 (arXiv 1204.0817), Sec. 2.

Notation: Q_k = square of area k, X_k = k uniform points in Q_k, L_k = length of the union of the routes
between pairs of X_k. Claim: E L_k ~ ell* k, with ell* the length per unit area of the network on a unit-rate
Poisson process (finite: Lemma 20 of Aldous gives ell <= 2 p(1)). Lower bound liminf E L_k / k >= ell*: P0230-A001 (6 Sep).

## Upper bound, split by distance from Q_k
(a) Inside Q_k. Couple X_k inside a Poisson process of rate 1+eps on Q_k (fails with prob. exp(-c eps^2 k)).
Routes among a subset lie in the union for the superset, and the superset's routes lie in the whole-plane
network on rate-(1+eps) Poisson points, whose length density is ell* (1+eps)^(1/2) by scaling. So
E[length inside] <= ell* (1+eps)^(1/2) k + (failure term; needs a moment bound for L_k, e.g. E L_k^2 = O(k^C)).
(b) Within distance delta sqrt(k) outside Q_k: bounded the same way by ell* times the area, O(delta k).
(c) Beyond distance delta sqrt(k). A point of a route between two points of Q_k at distance > delta sqrt(k) from
Q_k is at distance > delta sqrt(k) from both endpoints, so it lies in the "r-far" network of the whole-plane
process, r = delta sqrt(k), whose length density is p(1)/r by scaling (the weak-SIRSN axiom p(1) < inf).
In the annulus A_j at distance between 2^j delta sqrt(k) and 2^(j+1) delta sqrt(k), area ~ 4^j k, so the far
network there has mean length ~ 2^j sqrt(k) p(1)/delta. Taken alone this sum over j diverges; the Q_k routes reach A_j only
on the event E_j = {some route between two points of Q_k leaves the 2^j delta sqrt(k) neighbourhood}. By scale
invariance P(E_j) <= q_j := P(some route between two points of the unit square exits the 2^j delta neighbourhood),
uniformly in k (monotone in the point set). Cauchy-Schwarz: contribution of (c) <= sqrt(k) * sum_j 2^j sqrt(q_j)
* C(delta), which is o(k) as soon as sum_j 2^j sqrt(q_j) < inf (and the second moment of the far length in A_j
is O(4^j k) up to constants: a Poisson-type variance bound, to be checked).

## What is left
1. EXCURSION TAIL (the real gap, as A001 says): q_j = o(4^(-j)) with some room, i.e. routes between points of a
   unit square rarely leave a ball of radius R; need P <= R^(-2-eps). Not an Aldous axiom as far as recalled.
   For the Kendall/Kahn Poisson-line SIRSN (Kendall, AoP 45 (2017); Kahn, arXiv 1503.03976) the fast lines
   needed to make a long detour have Poisson counts with explicit scaling; this tail looks provable there.
2. The moment bounds in (a) and (c).
3. Check the axioms used. Read 16 Nov in the arXiv text: a SIRSN requires p(1) < inf, display (20), with p(r) = p(1)/r by (37); a WEAK SIRSN requires only (16), and Lemma 20 gives ell <= 2 p(1). So (c) needs the full SIRSN axiom. E(inf, r) is defined over pairs of Xi(lambda), lambda -> inf, so placing a route between two of OUR points inside it needs a continuity step. Also scaling of ell, routes as unions over
   pairs, monotonicity of the union in the point set.
If 1-3 hold, E L_k / k -> ell* follows for that network: the general-SIRSN statement needs the tail as an axiom
or a proof from the existing axioms.

Aldous names this exact obstacle above Open Problem 35 (p. 49): the difficulty is showing the spanning subnetwork
does not have, with low probability, huge length far from the square. So this note restates the problem as a tail
bound on excursions (item 1); it is not progress on that bound.

## Addendum 16 Nov: the tail needed is weaker, and the Poisson-line SIRSN meets it for gamma > 3 (conditional)
(i) Hoelder instead of Cauchy-Schwarz: points of A_j are at distance >= 2^j delta sqrt(k) from Q_k, so they lie in
E(inf, 2^j delta sqrt(k)); mean far length in A_j is ~ 2^j sqrt(k) p(1)/delta. If that length has a bounded p-th
moment at the same scale, contribution (c) <= C sqrt(k) sum_j 2^j q_j^(1-1/p). So a tail q(R) <= R^(-1-eps)
(not R^(-2-eps)) gives (c) = O(sqrt(k)), and E L_k / k -> ell* follows with (a), (b), delta -> 0.
(ii) Poisson-line SIRSN (Kendall; Kahn): lines with speed marks, intensity prop. to v^(-gamma) dv x (line measure),
gamma > 2 in the plane (PARAMETERISATION TO CHECK against Kendall AoP 2017). Let T* = sup of the travel time
between two points of the unit square. A route that leaves B(0,R) covers Euclidean length >= 2(R-2) inside B(0,R)
in time <= T*. On lines of speed < s it covers at most s T*. Taking s = R/(2 tau), on {T* <= tau} the route must use
a line of speed >= R/(2 tau) meeting B(0,R); the number of such lines is Poisson with mean c R s^(1-gamma). So
    q(R) <= P(T* > tau) + c' R^(2-gamma) tau^(gamma-1).
With tau = R^d0: q(R) <= R^(-1-eps) if gamma > 3 + d0 (gamma-1) and T* has moments of order > (1+eps)/d0. So: for
gamma > 3, if T* has all moments and the far length has the moment in (i), Open Problem 35 holds for that network.
Gaps: moments of T* (look in Kendall 2017 / Kahn for the travel-time bounds); moment of the far length in an
annulus; the continuity step of item 3; and 2 < gamma <= 3, where a single fast line far away is too likely and
one must show the route does not take it (needs the geometry, not a count).

## Addendum 2 (16 Nov, after reading Kahn arXiv 1503.03976): CANDIDATE for the Poisson-line SIRSN, every gamma > 2
Kahn's intensity is d mu(l) (gamma-1) v^(-gamma) dv, gamma > d (matches (ii)). Three of his results close the gaps above
in d = 2, for every gamma > 2, not only gamma > 3:
- T*: Theorem 3.1 bounds the time-diameter T_{A,F} = sup over x,y in A; it has all exponential moments (4). A = unit square.
- Exit tail: the proof of Theorem 5.1 (pp. 25-27) uses only constraint (15), vmax(B(x,r)) >= r/T for every r <= L, plus the
  tail of T, and runs a multiscale Poisson count over radii r_l = 2^l r0 with the filtration of lines meeting B(x,r).
  It gives P(L_xy > R) <= C R^(-a) for every a < gamma - 1. For our event: a route from x in the unit square that leaves
  B(0,R) has, for every r <= R - 2, Euclidean length >= r inside B(x,r), which is inside B(0, r+2). So
  vmax(B(0, r+2)) >= r/T* for all such r, and Kahn's computation with the centre 0 (constants change by 2^(d-1) once
  r0 >= 2) gives q(R) <= C R^(-a) for every a < gamma - 1, UNIFORMLY over pairs of the square. gamma - 1 > 1, so
  a = 1 + eps is available. My single-scale count in (ii) lost a factor R: one fast line passing close to x is what costs
  R^(1-gamma); Kahn's Remark 5.1 says this is the dominant scenario.
- Far length moments: Theorem 6.1 gives exponential moments for the length of the long-distance network in B(0,1/3);
  by scaling the far network beyond rho in a ball of radius rho/3 has law rho * Lambda. A_j is covered by C/delta^2 such
  balls (rho = 2^j delta sqrt(k) >= delta sqrt(k)), so ||L(A_j)||_p <= C(p, delta) 2^j sqrt(k) for every p.
Then (c) <= C sqrt(k) sum_j 2^j (2^j delta)^(-a(1-1/p)), finite once a(1-1/p) > 1. With (a), (b) and delta -> 0:
    E len span(Z_1..Z_k) / k -> ell   for the Poisson-line SIRSN in the plane, every gamma > 2.
REMAINING CHECKS before this counts (two audits, then the ledger):
1. Theorem 6.1's proof uses only a countable point set with unique geodesics (Theorem 4.8 gives uniqueness for each fixed
   pair, hence for countably many); confirm, so that F built on Xi plus our k points has the same bound.
2. The coupling failure term in (a): needs E[L_k^2] <= k^C, or a different coupling (Poisson-ize k).
3. Kahn's bound on P(L > r_m | T <= T_n) with ball centre 0 instead of x: redo (17)-(22) line by line.
4. Literature: Kendall, AoP 45 (2017) and later SIRSN papers (Kendall-Kahn?) may already contain this; search before
   any claim. Aldous's problem is for a general SIRSN; this would settle it only for the line-process example.

## Audit 1 of the candidate (agent A, 16 Nov ~02:5x; a second, independent audit is still required)
- Check 3 (recentring Kahn (17)-(22) at 0): for r_l >= r0 >= 4, B(x, r_l - 2) is inside B(0, r_l); use v_l = r_l/(2 T_n).
  P[A_i] = c r_{l_i}^(d-1) v_{l_(i+1)-1}^(-(gamma-1)) <= [2^(gamma-1) c (2 T_n)^(gamma-1) r0^(d-gamma)] 2^(-(gamma-1)(l_(i+1)-l_i)):
  Kahn's p(r0) times a constant, so the same choice of r0 (larger by a constant) gives 2^(-a(m+1)). The filtration and
  the independence of D_i only use nested balls with a common centre, so they hold at 0. T* replaces T_xy through
  Theorem 3.1 with A = the unit square. PASSES.
- Check 2 (coupling failure term): not needed. Let N ~ Poisson((1+eps)k) be independent of the iid sequence Z_1, Z_2, ...
  Span is monotone, so E L_k P(N >= k) = E[L_k; N >= k] <= E L_N, and E L_k <= E L_N / P(N >= k) with P(N >= k) -> 1.
  For Poisson points, span(Pi on Q_k) is inside span(Pi on the plane), whose length per unit area is ell (1+eps)^(1/2).
  This handles (a) and (b), and (c) was uniform over point sets in Q_k. PASSES, with no moment condition.
- Check 1 (Theorem 6.1 for Xi plus our points): the proof (pp. 29-31) fixes the geometry of a contributing geodesic
  (first and last hits s, u, v, z of the spheres of radius 2/3 and 1/3) and bounds its time "uniformly on x and y" by the
  time diameter of B(0, 2/3), then counts fast lines. It uses only uniqueness of geodesics between the points used,
  which holds a.s. for any countable set independent of the lines (Theorem 4.8). PASSES on reading; the mangled glyphs
  in the text extraction leave constants unread.
- Literature, 16 Nov: a search for SIRSN spanning length on k points finds nothing; Kendall 1908.08481 (Rayleigh random
  flights on the Poisson-line SIRSN) is unrelated. Aldous's later talks (2022, 2023) still list SIRSN questions as open.
  Not yet read: Kendall AoP 45 (2017), arXiv 1403.1156, in full.
Status: CANDIDATE for the Poisson-line SIRSN case of Open Problem 35 (d = 2, every gamma > 2). Not for a general SIRSN.
Next: an independent audit (another agent or a referee pass), then a short paper if it holds.

## Audit 2 (16 Nov, ~03:05-03:10): four independent referees, all PASS for the Poisson-line SIRSN, d = 2, every gamma > 2
agent E (read against Kahn's text), agent F, agent G,
agent D (logic only). Fixes to carry into the write-up:
- Cite the tail as the final display of the PROOF of Kahn Thm 5.1 (P[L > r_m | T <= T_n] <= 2^-(n+1)), not the theorem,
  which states only E L < inf. State the exit event as one sup-event over all pairs (depends on lines and T* only).
- T_n must grow like C log R (exponential moments of T*); then r0 ~ (log R)^((gamma-1)/(gamma-2)): a polylog loss, absorbed
  by a slightly smaller a. The events A_i must use disjoint (line, speed) sets; say so.
- Far-length covering: use balls of radius rho/4 centred in A_j (endpoints outside B(c, 3rho/4)), count <= C/delta^2;
  area(A_j) ~ 4^j delta^2 k for large j. The j with 2^j delta < r0 + 2 take q_j = 1 and cost O_delta(sqrt k).
- Whole-plane Poissonization (agent G): extend the N points to a rate-(1+eps) Poisson process of the plane; then the
  continuity step disappears.
- LOWER BOUND (agent D's doubt, answered here): A001 keeps, in each bulk unit cell, routes between endpoints within
  distance R of the cell. For bulk cells and fixed R those endpoints lie in Q_k, so their routes are in the span. As
  R -> inf the union of routes over pairs within R increases to the whole network, so its length in the cell increases
  to ell (monotone convergence for the length of an increasing union). A route from a bulk x to a far y is counted in
  the limit R -> inf, not at fixed R. A001's binomial-to-Poisson step was author-checked only; read it before the paper.
STATUS: two audits passed (upper bound). Ledger entry next; the paper waits on (1) a full read of Kendall AoP 45 (2017) /
arXiv 1403.1156 and Guillaume Blanc's papers on the Aldous-Kendall random metric for prior art, (2) a re-check of A001.
- Further audit-2 passes (03:1x): agent H (no new gap) and agent B (P0230_audit2_2026_11_16.md). Citation: Kahn, Ann. Probab. 44 (2016) 2694-2725
  (arXiv 1503.03976) proves the SIRSN axioms for gamma > d; Kendall, Ann. Probab. 45 (2017) (arXiv 1403.1156) is the
  construction (the pre-SIRSN). Cite both. In the paper, say in one line that Thm 6.1 is applied to E(inf, rho) in B(c, rho/4)
  with c in A_j, so the endpoints in Q_k lie outside B(c, rho). Two referees flag A001's lower bound as unaudited.

## Lower bound (agent B's proof, Addendum 03:2x of P0230_audit2_2026_11_16.md),
## checked by agent A 16 Nov 03:21: PASSES with one repair
Poissonize down: N ~ Poisson((1-eps)k) independent of Z_1, Z_2, ...; on {N <= k} span(Z_1..Z_N) is inside span(Z_1..Z_k).
For a bulk unit ball B(z,1) with dist(z, boundary of Q_k) >= D, span(Pi cap Q_k) contains span(Pi cap B(z,D)), and
E len(span(Pi cap B(z,D)) cap B(z,1)) = h(D) increases to ell_(1-eps) |B(0,1)| as D -> inf (the whole network is the increasing
union over D; monotone convergence). REPAIR: the step E[L_N; N <= k] >= E L_N - E[L_N; N > k] needs a moment of L_N, which is not
available. Instead work with the truncated local lengths min(len(. cap B(z,1)), M): they are bounded, so their sum over the
O(k) bulk balls loses at most O(k) M P(N > k) = o(k) on {N > k}; let k -> inf, then M -> inf, D -> inf, eps -> 0.
Overlaps: use a disjoint family of unit cells instead of balls, or divide by the bounded overlap number. Result:
liminf E L_k / k >= ell for ANY SIRSN with ell < inf. With the upper bound: E L_k / k -> ell for the planar Poisson-line SIRSN,
every gamma > 2. The 6 Sep A001 sketch reaches the same bound by a binomial-to-Poisson total-variation step; this proof
replaces it.

## Prior art, read 16 Nov 03:24
Kendall arXiv 1403.1156 (Ann. Probab. 45, 2017), Section 7 (Conclusion): lists the SIRSN property as the major open
question; nothing on spans of k points. Kahn 1503.03976: the axioms, no k-point span. Blanc arXiv 2207.03349 (Hausdorff
dimension (gamma-1)d/(gamma-d)) and Blanc-Curien-Kahn arXiv 2407.07887 (geodesics do not pause): neither treats total length
on k points. Aldous-Kendall math/0701140 (2008) is network DESIGN for prescribed points (near-Steiner length), a different
question. Nothing found that settles Open Problem 35 for any SIRSN.
STATUS 16 Nov 03:24 (revised 04:45): CANDIDATE. Upper bound audited (6 passes); lower bound PASSED by four independent readers (agent E, agent I, agent B, agent C). Paper draft: P0230_paper_main_2026_11_16.tex. For the planar Poisson-line SIRSN, every gamma > 2: E len span(Z_1..Z_k) / k -> ell.
Upper bound: this note, 6 independent passes. Lower bound: agent B's proof, checked here with the truncation repair.
Next: paper (CREDITS.md first: Aldous for the problem, Kendall for the construction, Kahn for Thms 3.1/5.1/6.1, the
referees by role in the AI declaration).
