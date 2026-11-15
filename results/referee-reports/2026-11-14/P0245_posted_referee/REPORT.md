# Referee report: the stationary cover time of reversible chains on three and four states

Paper: yspennstate/stationary-cover-time-four-states at 984b772 (paper/main.tex, 280 lines, 5 pages). Referee:
an agent, 14 Nov 2026. This is a second pass: the repo already carries "Referee corrections" (d634194, 12 Nov),
which narrowed the Lean scope sentence.

Claim: for n = 3 and n = 4, every irreducible reversible chain (holding allowed) has E_pi C >= (n-1)H_{n-1}, with
equality only for the simple random walk on K_n. This settles Aldous-Fill Open Problem 6.30 for n <= 4.

## Verdict

SOUND. No change made.

## Proofs re-derived by hand

- Eq. (maxmin): max = sum over nonempty J of (-1)^{|J|+1} min_J; with S = V \ J the sign is (-1)^{n-|S|+1}, and the
  J = V term is T_V = 0. Lemma 1 (L_S g_S = q_S) is right; L_S is positive definite for S a proper subset.
- Prop. 2 (holding):
  - The event {t < C} depends on the visited set, which reversal keeps, so q_x N_xy = q_y N_yx and K is symmetric.
  - Each jump-chain visit to y before C lasts a geometric time with mean m_y/q_y; no wait is counted at the last new
    state. So E_x C_h = (K m)_x, and m^T K m expands to the three terms of (holding).
  - Middle term: 2(n-1) - c0 = 1 for n = 3 and 1/2 for n = 4, as stated; it fails for n >= 5 since H_4 > 2.
- Section 4: Q equals the Schur bracket plus 3(sum a^3 - 3abc); AM-GM equality forces a = b = c, and connectivity
  forces them positive.
- Section 5:
  - 2x2 inverse gives B_ij = q_i q_j (q_i + q_j + 2 w_ij).
  - All four 3x3 principal minors equal tau (matrix-tree).
  - Signs for n = 4: + on |S| = 1, - on |S| = 2, + on |S| = 3. That gives E_pi C = 1 + (A/tau - sum B/Delta)/W and
    eq. (F). Every term of F has degree 16.
  - Orbits: S_4 acts faithfully on the six edges, so 720/24 = 30.
  - The equality argument via z_0^14 z_j^2 and z_j^16 is correct. When some edge vanishes, z_0 = ... = z_{j-1} = 0, so
    x_{o_j} = z_j > 0.

## Independent computation (referee_check.py, referee_check.out; own code, exact rationals)

- n = 3: (three) against an exact first-step solve on (state, visited set), 40 random weightings with some zero edges:
  0 mismatches. The Schur/AM-GM split is a sympy identity.
- Holding identity on random chains, n = 3, 4, 5:
  - K was computed from expected visit counts. It is symmetric, its entries are nonnegative, and Kq = E_x C.
  - The identity (holding) and E_x C_h = (Km)_x hold exactly: 0 mismatches.
- Remark 3: 100.0443 without holding, 85.0716 with h_3 = 1. The paper's 100.04 and 85.07 are right.
- F rebuilt from (maxmin) with a polynomial ring has 13,368 terms, 2,421 of them negative, all of degree 16. It is
  term-for-term identical to evidence/four_polynomial.json. E_pi C - 11/2 = F/(2 W tau R) holds exactly at 6 random
  integer points.
- Equality case: all 37 connected spanning proper subgraphs of K4 with unit weights have E_pi C > 11/2 (minimum 6) and
  F > 0.
- Cone files:
  - 30 files hold 577,620 coefficients, none negative.
  - G_o(z) = F(x(z)) at a random z in every cone.
  - z_0^14 z_j^2 is positive for every cone and every j.
  - z_j^16 is positive whenever the tail edges are connected and spanning.
  - The 30 representatives cover all 720 orderings under S_4.

## Citations checked against the sources

- Aldous-Fill, recompiled book (stat.berkeley.edu/~aldous/RWG/book.pdf, p. 230, read as a rendered page):
  - Open Problem 6.30 is "E_pi C >= (n-1)h_{n-1}" for any reversible chain, as quoted.
  - Theorem 6.31 (Feige) is min_v E_v C >= c_n ~ n log n for unweighted graphs, as the introduction says.
  - Matthews' method is Theorem 2.26.
- Crossref:
  - Aldous, J. Theoret. Probab. 2 (1989) 91-100.
  - Feige, RSA 6 (1995) 433-438.
  - Matthews, Ann. Probab. 16 (1988) 1215-1228.
  - Titles and authors match for all three.
- Prior-work search (web): nothing found that settles 6.30 for any n >= 3. The 2026 vertex-transitive paper
  (arXiv 2601.03864) is about stationary hitting times, not cover times.

## Build

Not rebuilt in this pass. The PDF was refreshed on 13 Nov (984b772), after the tex (d634194).

## Minor (not acted on)

- The paper writes H_{n-1} where AF write h_{n-1}. It is defined in (1), so this is fine.
- "Aldous gave lower bounds of the same order for reversible chains started from stationarity" is a fair one-line
  summary. Aldous's 1989 bounds carry hypotheses that the sentence leaves out, which is acceptable in an introduction.
