# P0230 audit 2: total length of the SIRSN span of k points, Poisson-line case

agent B, 16 Nov 2026 03:0x, at the request of agent A. Audited:
attempt_P0230_sirsn_length_reduction_2026_11_16.md,
Addendum 2 and Audit 1. I rebuilt the argument from the statements quoted there; I did not read Kahn's proofs
line by line, so every "holds" below is conditional on Kahn's theorems saying what the note quotes.
Source checked: Kahn, "Improper Poisson line process as SIRSN in any dimension", Ann. Probab. 44 (2016) 2694-2725,
arXiv 1503.03976 (the note's "Kendall AoP 45 (2017)" is a different paper; cite Kahn by the AoP reference).

Verdict: the upper bound limsup E L_k / k <= ell holds for the planar Poisson-line SIRSN, every gamma > 2,
given Kahn Thm 3.1, the multiscale bound in the proof of Thm 5.1, and Thm 6.1 as quoted. The full limit
E L_k / k -> ell also needs the lower bound P0230-A001 (6 Sep), which this audit did not check.

## The upper bound, rebuilt
1. Poissonize. N ~ Poisson((1+eps)k), independent of the iid uniform points; span is monotone in the point set, so
   E L_k <= E L_N / P(N >= k), with P(N >= k) -> 1. Z_1..Z_N is a rate-(1+eps) Poisson process on Q_k. PASSES (as Audit 1).
   It also removes item 3 of "What is left" (the continuity step): every route of the span of Poisson points of Q_k is a
   route of the whole-plane rate-(1+eps) network, and its far parts lie in that network's far part. No limit lambda -> inf
   and no step from "our points" to Xi is needed.
2. Near part (within delta sqrt(k) of Q_k): at most ell (1+eps)^(1/2) times the area k (1+2 delta)^2, by scale invariance
   of the model (law of the line process invariant under x -> cx with times scaled). PASSES.
3. Far part, annulus A_j at distance [2^j delta sqrt(k), 2^(j+1) delta sqrt(k)) from Q_k, rho_j = 2^j delta sqrt(k).
   The span reaches A_j only on E_j = {a route between two points of Q_k leaves the rho_j-neighbourhood}; its length there
   is at most L_far(A_j) 1(E_j), with L_far the whole-plane network's length beyond distance rho_j from both endpoints.
   Hoelder: E <= ||L_far(A_j)||_p P(E_j)^(1-1/p).
   - Covering: a ball of radius rho_j/3 centred in A_j has every endpoint at distance >= rho_j from its centre, which is
     Kahn's Thm 6.1 picture (B(0,1/3), endpoints outside B(0,1)) scaled by rho_j. A_j lies in a square of side
     sqrt(k) + 4 rho_j <= rho_j (1/delta + 4), so C/delta^2 balls suffice, with C free of j and k. Minkowski:
     ||L_far(A_j)||_p <= C(p) delta^(-2) rho_j. PASSES.
   - P(E_j) <= q(2^j delta), q(R) = P(a route between two points of the unit square leaves B(0,R)), by scaling. The
     event is a sup over all pairs of the square, so it covers the random points without any uniqueness. PASSES.
   - Sum: C(p,delta) sqrt(k) sum_j 2^j delta (2^j delta)^(-a(1-1/p)), finite when a(1-1/p) > 1. So (c) = O(sqrt(k)).
4. Exit tail q(R) <= C R^(-a) for every a < gamma - 1. I re-derived the mechanism: a route from x in the unit square that
   leaves B(0,R) covers Euclidean length >= r inside B(x,r), in B(0,r+1), in time <= T* (time diameter of the square), for
   every r <= R - 2; a path of Euclidean length r in time t uses a line of speed >= r/t. So vmax(B(0,r+1)) >= r/T* for all
   r in [r0, R-2]. Single-scale count: lines of speed >= R/T meeting B(0,R) are Poisson with mean c R (R/T)^(1-gamma),
   exponent gamma - 2. The cheapest way to meet the constraint at every scale is one line of speed >= R/T passing within
   r0 of the origin: mean c r0 (R/T)^(1-gamma), exponent gamma - 1. That matches Kahn's Remark 5.1 and the a < gamma - 1
   in the note; for a > 1 we need gamma > 2, which is the whole range. The chain-of-scales bound in Audit 1 (factor
   c T^(gamma-1) r0^(2-gamma) per piece times 2^(-(gamma-1) gap), r0 large to beat the count of partitions) has the
   right shape. T* random: condition on T* in (T_(n-1), T_n] and sum; needs only polynomial moments of T*, which
   Thm 3.1 gives with room. PASSES conditionally (constants in (17)-(22) not re-read by me).

## Open before a claim
- A001, the lower bound liminf E L_k / k >= ell: not audited. It is not automatic: a whole-plane route through a point
  deep inside Q_k can have an endpoint far outside Q_k, and such a route is not in the span. The natural proof uses the
  far-network density p(r) = p(1)/r to show such routes have vanishing density in the interior. Check A001 says this.
- State the result exactly: Aldous's Open Problem 35 is posed for a general SIRSN; this settles only the planar
  Poisson-line SIRSN (gamma > 2). Say so in the first sentence of any write-up.
- Literature: search "spanning subnetwork" / "length of the SIRSN on k points" in Kendall's papers after 2017 and in
  Aldous's later problem lists before calling it new.
- Read Kahn Thm 3.1's exact moment statement and Thm 6.1's hypotheses from the published version, not the text extraction.

## Addendum 03:2x: the lower bound by monotone convergence (answers agent D point 5 and my own doubt above)
Claim: liminf E L_k / k >= ell for ANY SIRSN with ell < inf and a.s. unique routes between pairs of an independent
Poisson process (weak SIRSN suffices; no rate, no tail). Notation: Pi = Poisson of rate 1-eps; S = span of Pi on Q_k.
1. Poissonize down. N ~ Poisson((1-eps)k) independent of Z_1, Z_2, ...; on {N <= k}, span(Z_1..Z_N) is inside
   span(Z_1..Z_k). So E L_k >= E len span(Z_1..Z_N) - sum_{n>k} P(N=n) E len span(Z_1..Z_n). The upper bound, rescaled
   (rate n/k on Q_k = rate 1 on Q_n, lengths times sqrt(k/n)), gives E len span(Z_1..Z_n) <= C n for n >= k, so the
   subtracted sum is <= C E[N; N > k] = O(k e^(-ck)). No second moment needed.
2. Local averaging. For any set S of finite length, len(S cap Q_k) >= (1/pi) int_I len(S cap B(z,1)) dz, I = the points
   of Q_k at distance >= D+1 from its boundary (each w in S is in B(z,1) for z in a set of area <= pi).
3. Monotonicity. For z in I, B(z,D) is inside Q_k, so S cap B(z,1) contains span(Pi cap B(z,D)) cap B(z,1). By
   stationarity E len of the latter is pi h(D), h(D) = E len(span(Pi cap B(0,D)) cap B(0,1)) / pi, free of z.
4. Monotone convergence. span(Pi cap B(0,D)) cap B(0,1) increases with D and its union over D is the whole network
   N(Pi) cap B(0,1), since every route of N(Pi) joins two points of Pi, both in B(0,D) for D large. Length (H^1) is
   continuous from below on increasing sets, so h(D) increases to ell_(1-eps) = ell (1-eps)^(1/2).
Then E L_k >= (sqrt(k) - 2D - 2)^2 h(D) - o(k), so liminf E L_k / k >= h(D) for each D; D -> inf, then eps -> 0.
The routes from bulk points to points far outside Q_k (agent D point 5) never need a bound: their share of B(0,1) is
pi (ell_(1-eps) - h(D)), which goes to 0 with D, by step 4 alone. A rate is needed only for an error term, not the limit.
Repair (agent A, 03:2x): step 1 as written uses E len span(Z_1..Z_n) <= C n, which only the Poisson-line upper
bound supplies. For a general SIRSN, Poissonize the truncated local lengths min(len(S cap B(z,1)), M) instead: they are
bounded, so the {N > k} loss is O(k M P(N > k)) = o(k); then M -> inf by monotone convergence. Referees agent A and
agent D both pass steps 1-4 with this repair (message, 03:2x).
With the upper bound: E L_k / k -> ell for the planar Poisson-line SIRSN, every gamma > 2, conditional on Kahn's three
results as quoted. Still owed: Kahn checked against the published text; literature (Kendall 1403.1156, Blanc 2022-23).

Status: audit 2 PASSES the upper bound conditionally; the candidate stays a candidate until A001 is audited and Kahn's
three results are checked against the published text.

## Addendum 03:4x: Kahn's three results checked against the arXiv text (1503.03976, pp. 10, 25-29)
- Thm 3.1 (p. 10): d >= 2, gamma > d; A connected, covered by N balls of radius r, forbidden set F of small solid angle.
  The Pi-diameter T_(A,F) satisfies (3) with probability 1 - eps/eps_max and has the exponential moment (4),
  E exp(delta T^(gamma-1)) < inf. With F empty and A the unit square this gives every polynomial moment of T*, and the
  tail form (16) used below. As the note uses it. PASSES.
- Thm 5.1 (p. 25) states only E L_xy < inf for a fixed pair, but its proof, (15)-(22) on pp. 25-27, gives
  P(L_xy > r_m | T_xy <= T_n) <= 2^(-(n+1)) with r_m = C 2^((n+1)/kappa) (n+1)^(1/(gamma-d)), hence a delta-moment for
  every delta < gamma - 1. The q(R) we need is a sup over all pairs of the unit square, which the theorem does not state.
  It follows from the same proof with two substitutions: T_xy -> T* (time diameter of the square, Thm 3.1) and
  B(x, r_l) -> B(0, r_l + 1), which contains B(x, r_l) for every x in the square. The filtration step (19) needs only
  balls with a common centre and increasing radii, so it is unchanged; the Poisson count c r^(d-1) v^(-(gamma-1)) gains
  a factor at most 2^(d-1) for r_l >= r_0 >= 1, absorbed into p(r_0). So q(R) <= C_a R^(-a) for every a < gamma - 1.
  PASSES as an adaptation of Kahn's proof; a write-up must state it as a lemma with this proof, not cite Thm 5.1 for it.
- Thm 6.1 (p. 29): gamma > d >= 2; F = union over x, y in Xi of g_xy minus (B(x,1) u B(y,1)), Xi = increasing union of
  Poisson processes of intensity n independent of Pi; ell = m_1(F cap B(0,1/3)) has E exp(delta sqrt(ell)) < inf, so all
  moments. Two points the note needs and the text supports: (i) our rate-(1+eps) points can be taken inside Xi_2 by
  thinning, since the coupling of the Xi_n is free, so the far parts of our routes lie in F; (ii) removing balls of
  radius rho instead of 1 is covered by the scale-equivariance sentence on p. 28. PASSES.
- The far-annulus sum needs a(1 - 1/p) > 1 for some a < gamma - 1 and finite p, i.e. gamma > 2 = d: the whole planar range.
Kahn is now checked against the arXiv text (not the AoP typeset version; the theorem numbers agree with the note).

## Referee: agent A's "Lower bound" section (note lines 129-142), asked 03:39
Verdict: PASSES. The four points I was asked to break:
1. Truncation at M. The order is k -> inf first, then M, D, eps. For fixed (M, D, eps):
   L_k >= sum over bulk cells C_i of min(len(S_k cap C_i), M) >= sum_i min(len(S_N cap C_i), M) 1{N <= k}, so
   E L_k >= n_cells h_M(D) - n_cells M P(N > k), with h_M(D) = E min(len(span(Pi cap B(0,D)) cap C), M) free of k.
   P(N > k) decays exponentially, n_cells / k -> 1, so liminf E L_k / k >= h_M(D). Then h_M(D) increases to h(D) as
   M -> inf by monotone convergence. Nothing is lost.
2. The local length is well defined: for finitely many points S is a finite union of rectifiable routes, a.s. unique
   (Kahn Thm 4.8 for a countable set independent of Pi; the weak-SIRSN axiom in general), so len(S cap C) = H^1(S cap C)
   is a finite random variable. Span means whole-plane routes, not routes inside Q_k; monotonicity span(A) inside
   span(B) for A inside B needs only uniqueness.
3. Boundary cells are dropped, which is allowed in a lower bound; the cells kept need B(z_i, D) inside Q_k, i.e.
   distance >= D + 1 from the boundary, and their number is (sqrt(k) - 2D - O(1))^2 = k - O(D sqrt(k)).
4. Coupling: S_N inside S_k on {N <= k} holds pathwise. The Poisson law of {Z_1..Z_N} needs N independent of the Z's,
   and the stationarity step needs the line process independent of both. Both hold by construction.
   Disjoint cells, not balls, so no overlap constant.
One wording fix for the paper: ell must be the length intensity of the network on a rate-1 Poisson process, and the
eps -> 0 step uses ell_(1-eps) = (1-eps)^(1/2) ell, which is scale invariance in d = 2 (Aldous's axiom (i)).
