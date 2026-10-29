# Second review: T084-C015, C016, C017, C018 v1 (forests on K_n at every fugacity)

Reviewer: agent B (Claude, interactive session on this PC). Not the author
(worker T, Codex account 4) and not the first reviewer (agent P, whose PASS of
15 Oct 05:06 is the only one on record; moves.jsonl line 8 recorded the move on it
with "worker S second audit wanted"). I did not read the first review or its scripts
before writing this verdict.

Frozen sources, (local file), SHA256:

    T084-C015_v1.md  893ad283dff3c90bf547...   (full hash in RECEIPT_C015_C018.json)
    T084-C016_v1.md  1c432ac6cc3fc37df103...
    T084-C017_v1.md  86fb8aa30b0427cf4f7f...
    T084-C018_v1.md  39234bbfb60d3f0878cd...

Claim under review (C018): for every n >= 1 and every t > 0, two distinct edges of
K_n have nonpositive covariance under the forest law proportional to t^|F|, strictly
negative when two distinct edges exist.

Verdict: PASS for all four, correctness only. Novelty is not judged here.

## C015 (adjacent pairs)

Read line by line and re-derived. The exponential formula over the components of
F - v is right (a component is unattached, weight a U, or attached at exactly one
chosen vertex, weight z T; two attachments would close a cycle). The Lagrange step:
T(u e^-u) = u, so [w^N] g(T) = [u^N] g(u) e^{Nu}(1-u) with g = exp(a(u - u^2/2) + zu),
which is C015 (2). The Hermite recurrence and the bordered tridiagonal determinant
are standard and correct; the zeros of H are real, negative, and not all equal for
N >= 2; the factorial-moment identity and strict Cauchy-Schwarz give eta < rho^2.

## C016 (exact counts, Riccati, endpoint signs)

Checked by a method the proof does not use: H(z) computed directly by the
exponential formula with k^(k-2) trees per component (no substitution, no
recurrence), Z = H(1), E = H'(1)/N, L = H''(1)/(N(N-1)), D from the edge-count
derivative t E' - E = 2(n-2)L + hD/2; and, for n = 4..7, every edge subset of K_n
enumerated with union-find. Results (check_c016.py, check_c016.log):

- brute force = direct count for Z, E, L, D at n = 4, 5, 6, 7;
- C016 (1) (all four Hermite closed forms), C015 (4) (the whole degree polynomial),
  (4), (5), t Z' = M E, and the Riccati equation (8): exact for n = 4..10 (the run to 12 hit its 25-minute timeout after n = 10);
- (11): E^2 - ZL = t^3 + O(t^4), E^2 - ZD = 2t^4 + O(t^5), rho = t - t^2 + (3-n)t^3;
  (12) lim f/t^5 = 2h; (13) rho -> 2/n, r1 = -(n+6)/n^3, lim f = 4h/n^4: exact for
  n = 4..10 (the run to 12 hit its 25-minute timeout after n = 10).

The finite checks confirm the implementation; the all-n derivations in Sections 1,
3, 4, 5 were read and agree (I recounted the D_4 exclusions: n-2 triangles on each
forced edge completed by the other, and the two 4-cycles 0-1-2-3 and 0-1-3-2).

## C017 (polynomial identities)

Checked symbolically in arbitrary n, t, r with SymPy (check_c017.py,
check_c017.json): identities (1) and (2); the Vieta product (3) = -4t^4 J/h; J'
in (4); J(t_a) and J(t_b); the expansion (6) of the discriminant; all five
coefficients of both substitutions (7) and (8); the two x = c - 4 rewritings;
Dscr(t_c). All true. Each sign pattern has exactly one sign change for c >= 4, as
stated. A numerical picture at n = 7, 8, 12, 30, 200 shows the root order
tau_1 < t_c < tau_2 < beta claimed downstream (not used as proof).

## C018 (the global sign)

Re-derived by hand:

- f' = G(t, rho)/(2t^2) holds at every t, not only at zeros, because the Riccati
  right side of C016 (8) is exactly phi. At a zero of f, G = ell rho + c0 by C017 (1).
- (3): at a discriminant zero, partial_t F at fixed r* is -Dscr'/(4 delta), so
  G = -tau^2 Dscr'/(2 delta): positive at tau_1, negative at tau_2 (simple zeros).
- (4): G(tau_2, r*)^2 > 0 equals -4 tau_2^4 J(tau_2)/h, so J(tau_2) < 0 and
  tau_2 < beta. Also tau_1 < t_c < beta from C017 (5).
- Section 2: on (0, tau_1] both root evaluations have positive product and the
  common positive limit at tau_1, so both are positive.
- Section 3: on [tau_2, beta) both are negative; for t > beta the product is
  negative, ell cannot vanish (that would make the product a square) and is
  eventually positive, so ell > 0; at beta, ell(beta) = 0 would force both factors to
  vanish and P'(beta) = 0, contradicting P'(beta) = -4 beta^4 J'(beta)/h < 0; hence
  g_-(beta) < 0 = g_+(beta), and g_- < 0 < g_+ beyond. So G(t, r_-) < 0 on [tau_2, oo).
- Section 4: first-zero barrier on (0, tau_1]; F > 0 on (tau_1, tau_2); on
  [tau_2, oo), rho stays below r_- to the right of the largest zero (r_+ grows like
  n(n-4)t/h, r_- tends to 2/n, rho <= 2/n), so the largest zero would have
  rho = r_- and f' < 0 there, contradicting positivity to its right.
- Base cases n = 4, 5, 6: the three Rayleigh polynomials match both my direct count
  and full subset enumeration (check_base.py); n = 3 is all adjacent (C015).

No gap found. The argument covers every t > 0 for each fixed n >= 7 without any
uniform-in-n limit, as it says.

## Not judged

Novelty and priority. The dossier lists Gupta 2609.26134 (t = 1, all n) and notes
that 2610.00549 calls K_n open in general; reading Gupta and Huang whole before any
novelty claim remains the open step.
