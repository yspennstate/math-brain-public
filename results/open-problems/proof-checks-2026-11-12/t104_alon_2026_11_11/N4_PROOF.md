# The 2/3 conjecture for n = 4, and a dual form for every n

Status: read by two independent readers, no gap found; not yet submitted anywhere. One author, checked numerically (n4_check.py, n4_check.out). Read once by an independent reader (an agent, 11 Nov 01:28Z): Proposition 1, Lemma 2 and Theorem 3 line by line, no gap; the case analysis of Theorem 3 compiles in Lean 4 with Mathlib (06_math_research/lean_checks_agent/t104_alon_n4/, brain main 98b53434). Not re-derived there: the Caputo-Liggett-Richthammer reduction for [3,1]. A second independent audit is owed. Second reader (Codex gpt-6.1-sol, high, on Mac mini 1, 11 Nov 07:25-07:4x Mac time, session 01a1c8a3-4c5b-7702-98d1-e9bc867b30b6): every numbered statement CORRECT, overall SOUND; its own Young-orthogonal-form code on 32,000 random weighted graphs plus the 64 supports found no ratio below 2/3 and the star as the only minimiser of the pair (22, 211); it states the Caputo-Liggett-Richthammer theorem as equality of the interchange and random-walk gaps on connected support and confirms the use made of it; it finds that the paper does not prove the weighted n = 4 case (Theorem 1.4 gives 1/64, Theorem 4.4 covers quasi-complete graphs only, and the path is not one), while the equality example is the paper's Theorem 4.5 with m = 2. Report and log: AUDIT2_CODEX_N4_REPORT.md, AUDIT2_CODEX_N4_LOG.md. Wording points it raised, still to be applied: treat n = 1 separately in the minimax step; allow an infinite optimum when sigma = [n]. The reader ran with the Mac profile's hooks on, so it was not shielded from the brain; it was told nothing of the first reading.

Notation as in G. Alon, arXiv 2610.22151. For a weighted graph G = ([n], w), w_ij >= 0, and a partition nu of n,
L(G, nu) = sum_{i<j} w_ij (I - rho_nu((i j))) on the Specht module V_nu, and lambda_min(G, nu) is its smallest
eigenvalue. W = sum_{i<j} w_ij. Conjecture 1.5 there: lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) whenever
sigma != [n] and sigma dominates tau.

## 1. A dual form

Proposition 1. Let tau, sigma be partitions of n and c > 0. The following are equivalent.

(a) lambda_min(G, tau) >= c lambda_min(G, sigma) for every weighted graph G on [n].

(b) For every unit vector psi in V_tau there is a density matrix rho on V_sigma (positive semidefinite, trace 1)
    with
        1 - <psi, rho_tau((i j)) psi>  >=  c (1 - tr(rho rho_sigma((i j))))     for all i < j.

Proof. (b) => (a). Given w, let psi be a unit eigenvector of L(G, tau) for lambda_min(G, tau) and take rho as in (b).
Multiply the inequality for the pair ij by w_ij and add:
lambda_min(G, tau) >= c tr(rho L(G, sigma)) >= c lambda_min(G, sigma).

(a) => (b). Fix psi. On (the simplex of weights w with W = 1) x (density matrices on V_sigma) put
    f(w, rho) = sum_{i<j} w_ij [ c (1 - tr(rho rho_sigma((i j)))) - (1 - <psi, rho_tau((i j)) psi>) ].
f is bilinear and both sets are compact and convex, so min_rho max_w f = max_w min_rho f. For fixed w,
min_rho f = c lambda_min(G, sigma) - <psi, L(G, tau) psi> <= c lambda_min(G, sigma) - lambda_min(G, tau) <= 0 by (a).
Hence some rho has f(w, rho) <= 0 for all w, and the vertices of the simplex give (b). QED

So the best constant C(tau, sigma) is the largest c for which every pure state of V_tau is matched, pair by pair,
by a state of V_sigma. For each psi, (b) is a semidefinite feasibility problem in rho.

## 2. Two families of pairs that need no work

(i) tau = [1^n]. Then L(G, tau) = 2W, and I - rho_sigma((i j)) <= 2I gives lambda_min(G, sigma) <= 2W. Ratio >= 1.

(ii) sigma = [n-1, 1]. By the theorem of Caputo, Liggett and Richthammer, lambda_min(G, tau) >= lambda_min(G, [n-1,1])
for every tau != [n]. Ratio >= 1.

## 3. n = 4

The partitions of 4 other than [4] are 31, 22, 211, 1111. By (i) and (ii) the only dominating pair left is
tau = 211, sigma = 22.

Lemma 2. Let L_G be the graph Laplacian of G on R^4 and a = w_12 + w_34, b = w_13 + w_24, c = w_14 + w_23
(the weights of the three perfect matchings), D = sqrt(a^2 + b^2 + c^2 - ab - bc - ca). Then
    lambda_min(G, 211) = 2W - lambda_max(L_G),        lambda_min(G, 22) = W - D.

Proof. V_211 = V_31 tensor sign, so I - rho_211((i j)) = 2I - (I - rho_31((i j))) and L(G, 211) = 2W - L(G, 31);
L(G, 31) is L_G on the orthogonal complement of the constants. V_22 is the two-dimensional representation of S_3
pulled back along S_4 -> S_4/V_4 = S_3, under which (12), (34) go to one transposition, (13), (24) to a second and
(14), (23) to the third. So L(G, 22) is the Laplacian of the triangle with edge weights a, b, c on the complement of
the constants in R^3, with eigenvalues (a + b + c) +- D. QED

Theorem 3. For every weighted graph G on four vertices,
    lambda_max(L_G) <= (4/3) W + (2/3) D,
that is, lambda_min(G, 211) >= (2/3) lambda_min(G, 22). Equality holds for the star K_{1,3} with equal weights.
Hence Conjecture 1.5 holds for n = 4, and C(211, 22) = 2/3 there.

Proof. Write v = (a, b, c) and let P be the orthogonal projection of R^3 onto {u : u_a + u_b + u_c = 0}. Then
|Pv|^2 = (2/3) D^2, so
    (2/3) D = sqrt(2/3) |Pv| = max { sqrt(2/3) <u, v> : u_a + u_b + u_c = 0, |u| <= 1 }.
For an edge ij let m(ij) be the perfect matching that contains it. For such u,
    (4/3) W + sqrt(2/3) <u, v> = sum_{i<j} w_ij (4/3 + sqrt(2/3) u_{m(ij)}),
and lambda_max(L_G) = max over unit x orthogonal to (1,1,1,1) of sum w_ij (x_i - x_j)^2. So it is enough to show:

(*) for every unit x orthogonal to (1,1,1,1) there is u with u_a + u_b + u_c = 0, |u| <= 1 and
    (x_i - x_j)^2 <= 4/3 + sqrt(2/3) u_{m(ij)} for all six edges.

Put e_a = (1,1,-1,-1)/2, e_b = (1,-1,1,-1)/2, e_c = (1,-1,-1,1)/2, an orthonormal basis of the complement of the
constants, and x = p e_a + q e_b + r e_c, p^2 + q^2 + r^2 = 1. Then
    x_1 - x_2 = q + r,  x_3 - x_4 = q - r,  x_1 - x_3 = p + r,  x_2 - x_4 = p - r,  x_1 - x_4 = p + q,  x_2 - x_3 = p - q.
The larger of the two squares in each matching is (|q|+|r|)^2, (|p|+|r|)^2, (|p|+|q|)^2, so we may take
p, q, r >= 0 and, by the symmetry in the three matchings, p >= q >= r. Set
    t_a = (q + r)^2 - 4/3,   t_b = (p + r)^2 - 4/3,   t_c = (p + q)^2 - 4/3,
so t_a <= t_b <= t_c, and (*) asks for u with sum zero, |u| <= 1 and sqrt(3/2) t_m <= u_m for m = a, b, c. Two facts:

    t_a + t_b + t_c = 2(pq + qr + rp) - 2 <= 0,                                   (1)
    t_c <= 2/3  (since (p + q)^2 <= 2(p^2 + q^2) <= 2),                            (2)
    t_b + t_c <= 1/3.                                                              (3)

For (3): (p + r)^2 + (p + q)^2 = 1 + p^2 + 2p(q + r) <= 1 + p^2 + 2 sqrt(2) p sqrt(1 - p^2), and with p = cos(theta)
the right side is 3/2 + (1/2) cos(2 theta) + sqrt(2) sin(2 theta) <= 3/2 + sqrt(1/4 + 2) = 3. So t_b + t_c <= 3 - 8/3.

Case 1: t_c <= 0. Take u = 0.

Case 2: t_c > 0 and t_b <= -t_c/2. Take u = sqrt(3/2) (-t_c/2, -t_c/2, t_c). The sum is zero, u dominates
sqrt(3/2) t because t_a <= t_b <= -t_c/2, and |u|^2 = (9/4) t_c^2 <= 1 by (2).

Case 3: t_c > 0 and t_b > -t_c/2. Take u = sqrt(3/2) (-t_b - t_c, t_b, t_c). The sum is zero and
-t_b - t_c >= t_a by (1). Further
    |u|^2 = 3 (t_b^2 + t_b t_c + t_c^2) = (9/4)(t_b + t_c)^2 + (3/4)(t_c - t_b)^2.
Here 0 < t_c/2 < t_b + t_c <= 1/3 by (3), and 0 <= t_c - t_b < (3/2) t_c <= 1 by (2). So
|u|^2 <= (9/4)(1/9) + 3/4 = 1.

For the star with centre 1 and unit weights, lambda_max(L_G) = 4, W = 3, a = b = c = 1, D = 0: equality. QED

In the language of Proposition 1: a state on V_22 is a point of the unit disc (Bloch disc of the real
two-dimensional representation), its three numbers tr(rho rho_22(m)) sum to zero with squares summing to at most 3/2,
and u = sqrt(2/3) (tr(rho rho_22(m)))_m. The map psi -> rho of the proof is piecewise linear in
((x_i - x_j)^2), not linear: the single edge (p, q, r) = (0, 1, 1)/sqrt(2) forces |u| = 1 in Case 2, and the centred
vector of t has squared norm 3/2 there.

## 4. Numerical check (n4_check.py 200000 5)

- Lemma 2 against the Specht-module matrices of alon_search.py: largest deviation 1.7e-13 over 200,000 weights.
- Theorem 3: the smallest value of (4/3)W + (2/3)D - lambda_max over those weights is 0 to rounding, never negative.
- (*): the u of the proof on 200,000 unit vectors (random, near the star eigenvector, near a single edge):
  largest |u| = 0.9999995, smallest edge slack -9e-16 (rounding at equality), no failures.

## 5. What this does not do

n >= 5 is open here. At n = 5 the pairs left after section 2 are (32; 311, 221, 2111), (311; 221, 2111),
(221; 2111); the search finds a smallest ratio of 0.75, at (2111, 221). For tau = [2, 1^{n-2}] the left side is again
2W - lambda_max(L_G), so the pairs (tau, sigma) = ([2, 1^{n-2}], sigma) ask for an upper bound on the largest
Laplacian eigenvalue by (4/3)-ish W plus a correction read off V_sigma, as in Theorem 3.
