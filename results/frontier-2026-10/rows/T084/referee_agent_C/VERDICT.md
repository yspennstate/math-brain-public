T084 referee, agent C, 17 Oct 22:4x. Own code written before reading yours (brute.py, rec.py, c4.py; to go in rows/T084/referee_agent_C/ once the dream releases its lock).

C1 PASS. Own subset enumeration of lam^|A| q^k(A) (union-find, every edge subset) for K_3..K_6 adjacent and K_4..K_6 disjoint, and an independent recursion (connected-cluster weights with up to 4 marked vertices and deleted marked edges, N by inclusion-exclusion on the deletions, flint polynomials) agree term by term; the recursion then equals your kn_poly_adjacent / kn_poly_disjoint numerator term by term for n = 3..11 (adj) and 4..11 (dis).

C2 PASS, and further. N/u Bernstein coefficients on [0,1] at degree 2n-3 (adj) and 2n-4 (dis), no elevation: zero negative lam-coefficients for every n = 3..30 adj and 4..30 dis (recomputed by my recursion, not yours). Structure: b_0 is nonzero (lowest lam power 3 adj, 4 dis); the top two Bernstein coefficients b_{d-1}, b_d vanish identically for every n.

C3 PASS. Cov(X_e,X_f) = (Z Z_ef - Z_e Z_f)/Z^2 = -N/Z^2. For q in (0,1), u in (0,1), every Bernstein basis term is positive, each b_j(lam) >= 0 for lam > 0, and b_0(lam) > 0, so N = u * sum_j b_j C(d,j) u^j (1-u)^(d-j) > 0 strictly. Worth one sentence in the write-up: strictness comes from b_0 != 0, since b_{d-1} = b_d = 0.

C4 PASS, with a proof. q^k = 1 - k u + O(u^2); write K_S = sum_{A ⊇ S} lam^|A| k(A). The u^0 term of N vanishes, and the u^1 term is (1+lam)^(m-2) [ (1+lam)^2 K_ef - lam(1+lam)(K_e + K_f) + lam^2 K ]. Splitting each A as B plus a subset of {e,f}, the bracket's coefficient on k(B+e+f), k(B+e), k(B+f), k(B) is lam^2 times (+1, -1, -1, +1), so the u^1 coefficient is lam^2 (1+lam)^(m-2) sum_B lam^|B| [k(B) - k(B+e) - k(B+f) + k(B+e+f)], B over subsets of E \ {e,f}. The bracket is >= 0 because rank n - k is submodular. Also checked by enumeration on 60 random graphs (n = 4..7, up to 15 edges): 60/60 equal, the second difference never negative.

Scope note: C2 is a finite computation (n <= 16 claimed, <= 30 checked here); it is not a proof for every K_n.

Structure notes (22:44, local, not sent; checked n = 4..12 adj, 5..12 dis):
- adjacent pair: in every b_j (j <= d-2) the highest-lam coefficient equals C(d-2,j). This does NOT hold for the
  disjoint pair.
- adjacent pair: the lowest-lam coefficient of b_{d-2} is n^(2n-6) = (n^(n-3))^2, i.e. the square of half the number
  of spanning trees of K_n that contain a fixed edge (2 n^(n-3)).
Possible handles for an all-n argument; unproved.
