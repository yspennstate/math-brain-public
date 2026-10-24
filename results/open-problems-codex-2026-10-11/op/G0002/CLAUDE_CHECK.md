# G0002: third check (claude-322bc92e, 12 Oct 2026 02:2x)

Verdict: PASS. Conjecture 53.1 of arXiv:2608.23661 is refuted for both objectives, phi_2 and phi_{2\1}, summed over w in A as the source writes them. Every global maximizer at n = 10^14 leaves the conjectured band. Novelty is not verified.

What I re-derived, independently of the attempt and the audits:

1. The band bound. If the conjectured inclusions hold and |w| >= d + 3, every deletion of at most two coordinates stays in A. So w has no pivot of order at most two, under the literal formula (49.1) and under the occupied-coordinate reading alike. Only the five levels d-2..d+2 contribute, each with at most binom(2d,d) configurations and at most n pivots apiece. Together with binom(2d,d)/4^d <= 1/sqrt(d+1) (induction margin 4(d+1)^3 - (2d+1)^2(d+2) = 3d + 2), this gives at most 10 sqrt(n) = 10^8.
2. The pair witness. For w in A, i in w and j in w - {i} with w - j in A and w - {i,j} not in A, the index i is in P_2^+ under both readings: (w - j) union {i} = w - j. If i is also outside S, then w - i is in A, so i is not a first pivot. In the clause graph, an edge {i,j} with neither endpoint in S gives exactly this: removing j kills no clause, and removing both empties the edge clause.
3. The estimates, at n = 10^14, h = 10^7, r = 10^6:
   - |2z - 1| <= 2/h and r(2/h) = 1/5 give (2z)^r <= 5/4 and (2z)^(r-2) >= 4/5.
   - M a_i >= (8/15) r^2/n, M t_i <= (32/3) r^2/n, about 0.107 < 1.
   - Bonferroni gives P(i in C | w in A) >= r^2/(4n), so E|C| >= r^2/12.
   - The singleton probability at a fixed coordinate is Q_S/s by symmetry, so E B <= (4 r^2)(2)(6r)/(n/3) = 144 r^3/n, which is 2.88e6 against r^2/12 = 8.3e10.
   - Chebyshev gives P(central) >= 3/4 because h^2 = n.
   - The lower bound is (3/4)(1/81)(r^2/24) = r^2/2592 = 3.86e8 > 10^8.
4. Scope. The same construction works for every n = h^2 with h a multiple of 10 and h > 2.6 million. So it refutes the conjecture also under a "for all large n" reading, not only at one dimension.

The audits: o09 PASS. o07 PASS_WITH_GAPS. Its gap concerns the task prompt's whole-cube sums, which differ from the source. With the source's sums over A (o07 confirmed pages 391, 394 and 398), the proof stands as written. Under the whole-cube reading a sixth level gives 12 sqrt(n) = 1.2e8, and 3.86e8 still clears it.

Not checked here: the small-cube scripts and the Lean file, beyond reading their logs.
