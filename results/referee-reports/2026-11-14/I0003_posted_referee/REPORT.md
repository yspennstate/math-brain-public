VERDICT: ACCEPT (no correction needed; two optional remarks)

Independent post-posting referee pass on "Recurrence and transience of the Manhattan walk for deterministic
orientation fields", https://github.com/yspennstate/manhattan-orientation-fields-recurrence (main.tex as cloned
14 Nov 2026 01:3x laptop time). Referee: an agent (Claude Opus 5.5), not the writer of the proofs (Codex
GPT-6.1 wrote them; an earlier GPT-6.1 referee pass I0003AR preceded posting). Lane: T-20261112-017 independent
referee passes on posted papers.

What was checked, line by line, by hand:
- Lemma 2.1 (one recurrent site implies irreducible and all recurrent): the P-transpose argument is right
  (doubly stochastic P, (P^T)^n(z,z)=P^n(z,z), incoming neighbours communicate via P^T).
- (3.1)-(3.2): symmetric part is half the lattice Laplacian for every field; antisymmetric part
  (e_y/2) d_x + (f_x/2) d_y. Energy identity (3.3) verified by pairing translations.
- Lemma 3.1: (H-A)^{-1} = H^{-1/2}(I-B)^{-1}H^{-1/2}, the identity (1/2)((I-B)^{-1}+(I+B)^{-1}) = (I-B^2)^{-1},
  and <u,K u> = <u,Hu> + <Au,H^{-1}Au> by A* = -A. Diagonal of (lambda-L)^{-1} equals diagonal of its symmetric
  part. Correct.
- Face stream h=(S(y)-T(x))/2: upper-minus-lower face value on a positive horizontal edge is e_y/2, left-minus-
  right on a positive vertical edge is f_x/2. The face identity (3.6) and the inner sum
  (u0-u2)(v1-v3)-(u1-u3)(v0-v2) expand correctly. Each diagonal difference squared is at most E_q (average of the
  two two-edge paths), so the pair is at most 2E_q; sum_q E_q = 4 E. Constant 4 in (3.7) and sup_t(8 sqrt(Wt)-t)
  = 16W both check.
- Theorem 1.1: W_{h_D} <= 4|h_D|^2 E gives K = 64|h_D|^2; squared triangle inequality in the H^{-1} norm gives
  C = 2+2K, uniform in site and lambda.
- Theorem 1.2: 8k+4 edges from sup-radius k to k+1; sum over the m-th annulus = 12*4^m exactly; energy 6 d_m^2;
  face weights h^2 <= M(2^{m+3})^2/2 and two faces per edge give 16W <= 192 M^2 d_m^2. Optimal d_m = w_m^{-1}/D_N
  gives 192/D_N; the shift by three dyadic levels does not change divergence. Example 4.1 primitive count
  S(2J)=2#{l: 2^{l^2}<=J} ~ sqrt(log J) correct.
- Lemma 6.1 (circulating field): level sets of R=|x+1/2|+|y+1/2| have 4r vertices and 8r edges to the next
  level (edges crossing the central lines stay on a level), so E(u)=4 sum r a_r^2. Recomputed the dipole
  coefficients at (r-1,0), (r-1,-1), (-1,r-1), (0,r-1) and at the four level-one sites: all as in (6.3). The
  bound <Au,H^{-1}Au> <= 2 sum a_r^2 and the harmonic profile a_r = -1/(r h_N) give E = 4/h_N and the dipole
  term <= pi^2/(3h_N^2). Correct.
- Theorem 1.3: reduction to sixteen canonical fields by Theorem 1.1; constant e or f gives P^n(z,z)=0;
  (g,g) quadrant monotonicity; reflections x -> -1-x map (g,-g) to (-g,g) and (g,g) to (-g,-g). The recurrent
  set is exactly sigma*tau = -1, i.e. (1.6). Example 6.2: S_g(n)=n, S_g(-n)=n-2, M(r)^2=2r^2. Correct.
- Theorem 1.4 and Corollary 1.5: measurability of E_0 via cylinder partial sums; comparison with the alternating
  field for every bounded-primitive f; the replacement-model variance bound, Kolmogorov maximal inequality with
  threshold 2^{ma}, summability iff beta > 1-2a, alternating-series control of the mean sums on both tails.
  Correct given Bosi's Theorem 9(i),(iii), which I did not re-read (the thesis was checked by I0003AR).

Optional remarks (no change required):
1. Section 7, translation paragraph: by Lemma 2.1, transience at one site already gives transience at every site
   (one recurrent site would make the origin recurrent), so the translation argument can be replaced by one
   sentence. As written it is correct.
2. Open case worth a sentence in a v2: e = g with f alternating (one primitive linear, the other bounded) is
   outside all four theorems (f has no constant tails, the dyadic series converges, and Theorem 1.1 compares it
   with nothing known). Its type is not decided by the paper.
   It is very likely transient, by the Campanino-Petritis route. Sketch (not audited twice, so not a claim):
   look at the walk at its horizontal steps. Between the j-th and (j+1)-th horizontal step it runs G_j >= 0
   vertical steps (iid Geometric(1/2)) in one column; that column has parity j, so the run goes in direction
   (-1)^j. Hence the height after the j-th run is W_j = sum_{i<=j} (-1)^i G_i, an autonomous walk (iid
   symmetric increments in pairs) not depending on x. The column is x_j = sum_{i<j} s(W_i) with s(w) = +1
   for w >= 0, -1 otherwise, so x_j = 2A_j - j, where A_j is the time the height walk spends in [0, inf).
   A run is monotone, so it visits (0,0) at most once, and only when x_j = 0 (j even) and the run crosses
   height 0. By Sparre Andersen's equivalence principle (occupation time of a half-line equals the arg-max
   in law for exchangeable increments, also under a bridge condition) together with the local estimate
   P(walk stays positive for m steps and ends at h) ~ h m^{-3/2}, one gets
   P(x_{2m} = 0, |W_{2m-1}| = a) <= C(1+a)^2 m^{-3/2}, and the geometric weight P(G >= a) makes the sum
   over a finite. So the expected number of visits to the origin is finite, and the walk is transient.
   The step that a full proof must write out is the lattice one: the count uses vertices with W_i >= 0, so ties
   at level 0 need a convention under which the equivalence principle (or a local limit theorem for the pair
   occupation time, endpoint) still gives O(1/m) per value of the occupation time.
   The run decomposition itself was checked by a second, independent computation (embedded_green.py: dynamic
   programming over the joint law of column and height at run boundaries): after 100 runs, about 200 steps, it
   gives a partial Green sum of 1.30070 against 1.30059 from the full-lattice evolution at n = 200, and its run
   terms also decay like j^{-3/2} (j^{3/2} times the term stays near 0.56).
   Carried to 6000 runs (rerun 14 Nov, laptop CPU): partial sums 1.33882, 1.34403, 1.34773, 1.34936 at j = 1000,
   2000, 4000, 6000, with j^{3/2} times the (even-j) term at 0.5636, 0.5639, 0.5640, 0.5641. The tail over even
   j > J is about 0.564 J^{-1/2}, which gives 1.35665 from J = 4000 and 1.35664 from J = 6000. This matches the
   1.357 from the lattice evolution below to three decimals.
   The exact evolution in mixed_check.py / mixed_check.out agrees: n^{3/2} P^n(0,0) is 0.756, 0.778, 0.788,
   0.793, 0.795, 0.796, 0.796 at n = 50, 100, 200, 400, 600, 800, 1000 (total mass 1.0 kept on the grid), and
   the partial Green sum is 1.33145 at n = 1000; adding the tail 0.796 n^{-3/2} over even n > 1000 gives a
   total of about 1.357. The mechanism (horizontal displacement as an
   occupation-time functional of an autonomous vertical walk) is the one Campanino and Petritis used for
   horizontally oriented lattices (arXiv:math/0111305, Markov Process. Related Fields 2003). There the vertical
   moves are two-way simple random walk steps, and they prove that the half-plane one-way lattice (horizontal
   orientation +1 for y >= 0, -1 below) is transient. The present case is its Manhattan analogue: the vertical
   lines are one-way and alternate, which replaces the simple vertical walk by the alternating-run walk W. A v2
   could state it as a remark citing them, with the adaptation above, once that adaptation has had a second
   audit. Before that, check Bosi's thesis (amsdottorato.unibo.it/8914, Appendix A, Theorem 9): the paper uses
   parts (i) and (iii), which already have alternating vertical lines, and a part on deterministic half-plane
   horizontal signs would settle this case outright. I did not re-read the thesis.

Numerical sanity check (laptop CPU, exact evolution, file circ_check.py / circ_check.out in this folder):
n P^n(0,0) for the circulating field is 0.4935, 0.4967, 0.4983, 0.4992, 0.4993 at n = 100, 200, 400, 800, 1000,
and for the alternating field 0.6303, 0.6334, 0.6350, 0.6358, 0.6360; the partial Green sums grow like log n
(2.334 and 1.912 at n = 1000), as recurrence requires. The saddle field (g,g) returns with probability 0 at every
n > 0 (Green sum 1). Total mass 1.0 kept on the grid in all three runs. This agrees with Theorem 1.3 and
Lemma 6.1.
