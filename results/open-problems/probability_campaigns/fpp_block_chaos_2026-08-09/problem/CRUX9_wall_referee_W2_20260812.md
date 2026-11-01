# REFEREE REPORT (REF-W2, 2026-08-12): CRUX 9.10 far-remainder closure and the D1 repair in 9.5 [REF-W1]

Independent re-deriving counter-check, discharging the two OWED items from REF-W1 (report
CRUX9_wall_referee_20260812.md; LOG 1185). Derive-first discipline: the CHECK A derivation
was written before reading CRUX lines 973-995 or report D4. Referee: a fresh-context agent
of a separate session, independent of both the 9.10 author (REF-W1 session) and the
author. Repairs below were applied in place with [REF-W2 2026-08-12] tags the same
day (CRUX 967 heading, CRUX SCOPE block, RPT D4 heading).

## CHECK A - CRUX 9.10, the (M2) far-remainder closure

Statement checked: A4's far remainder closes on the localization tail alone, mirroring
9.9's (M1) closure, at unified radius sqrt(5 log n).

Independent derivation (matches the author's body line for line once compared):
1. Deterministic cap: on U_L the positive part is capped by the OLD geodesic's occupation,
   (Delta_L)^+ <= (b-a_w)(b/a_w)(n+W) <= Cn, so per-block m4-mass <= C^4 n^4 p_L - TWO
   powers of n above the m2 cap C^2 n^2.
2. Form A at top scale r = R = Mn (single fixed endpoint pair; no boundary-pair union, so
   G-f's n_0 threshold does not enter): P(dev >= sigma W_R) <= 12 C1 (b/a_w) R
   exp(-c'' c_- sigma^2), valid for sigma^2 <= (delta^2/4) sqrt(R) and r >= r_0.
3. Level structure: levels spaced W = n^{3/4} sqrt(log(Mn)), ~M blocks/level; the Gaussian
   level sum over d >= sigma_1 W_R collapses to C M^{3/4} exp(-c'' c_- sigma_1^2)
   (verified twice: geometric collapse and the integral route).

Far band: Sum_far E[1(U)Delta^4] <= C' n^5 M^{11/4} exp(-c'' c_- sigma_1^2)
(n^5 = n^4 cap + n^1 linear-in-r prefactor; M^{11/4} = M^{1+3/4+1}; 9.9's analogue n^3).
Against the budget C2 M D^2 with D >= c log n:
   sigma_1^2 >= (5 log n + (7/4) log M + O(1)) / (c'' c_-).
The 5 is forced as 4+1 within the method. Mid-band: containment at the corrected range
endpoint (delta^2/4) sqrt(R) kills n^{21/4} M^3 (9.9's analogue 13/4). Near band:
O(M^{7/4}) blocks, n-independent, constant sqrt(5/3) larger than 9.9's.

VERDICT A: CONFIRMED-WITH-REPAIRS.
- A-R1 (applied): headings said "one power of n later" at CRUX 967 and RPT D4 107; it is
  TWO powers everywhere in the bodies' own arithmetic (cap n^2->n^4, far sum n^3->n^5,
  quantile 3->5). Likely an echo of 9.5's "(L3) is worth exactly one power of n".
- A-R2 (applied): the SCOPE block (CRUX 990-995) was INVERTED. The binding constraint is
  NOT REF3's emptiness floor r_0 but the quantile-in-range condition
  (delta^2/4) sqrt(Mn) >= (q log n + (7/4) log M + O(1)) / (c'' c_-), q = 3 (9.9) /
  5 (9.10). Its coefficient exceeds the floor's governing clause (delta^2 sqrt(r) >=
  (2/(c'' c_-)) log(12 C1 rho r), REF3 176) by the factor 2q regardless of constants, so
  the in-range threshold r_1 ~ (2q)^2 r_0 - measured 40-60x (q=3) and 100-160x (q=5)
  across REF3's three constant sets (friendly set: r_0 ~ 1.3e5, r_1(q=5) ~ 2e7). Closures
  hold for Mn >= r_1. Companion caveat noted at localization_lemma_STATEMENT_iter130:101-103.
- A-R3 (note, not applied as an edit): when the far closures substitute for (L1')/(L2')
  off the near band, the composed constants are C1 = beta C_occ + O(1),
  C2 = kappa4 beta^2 C_occ + O(1); the bare 1/(16 kappa4 beta^2 C_occ) is exact for the
  all-blocks hypothesis form. RPT 195-201 juxtaposes the two without saying so.

## CHECK B - the D1 repair in 9.5's [REF-W1] bracket

(i) E[Delta^k] = 2 E[1(U_L)((Delta^+)^k)], k = 2, 4: CONFIRMED by two independent routes
(swap-map S with Delta o S = -Delta + even-k split + Lemma 4.3's pointwise identity (4.1);
and raw exchangeability 4.1(iii) with f(x,y) = ((y-x)^+)^k). Remark 4.4 is needed only to
refute the OLD support claim; the repair never uses it. Degenerate note: p_L = 0 blocks
have both sides 0 and m_k undefined.
(ii) p m_k <= E[Delta^k] <= 2 p m_k: CONFIRMED (lower: drop the off-U mass; upper:
(Delta^+)^k <= Delta^k on U). Both can be strict - consistent with the measured ratios
1.16-1.25 in [1, 2].
(iii) A4 <= Sum p_L m4_L with NO 1/2: CONFIRMED pointwise, no symmetry needed; the old 1/2
was the false identity's residue (the TRUE symmetric identity A4 = (1/2) Sum E[Delta^4]
composed with E[Delta^4] <= 2 p m4 lands at the same constant). C2 = kappa4 beta^2 C_occ.
(iv) 9.2 arithmetic re-run: quarter-splitting is exact on substitution; kappa <=
1/(4 beta C_occ) unchanged and eps <= 1/(16 kappa4 beta^2 C_occ) exactly. Kurtosis forcing
p >= 1/(4 kappa4) sound via conditional Jensen. Downstream sweep: every live quote reads
16 (ledger 430/440, STATE 231, LOG 1168); the 1/(8...) prints at CRUX 588/660 are the
superseded originals corrected in place.

VERDICT B: CONFIRMED on all four items, no repairs. (Notes: the p_L = 0 case; "(4.1)" in
the bracket is MG2B's equation label inside Lemma 4.3, not Lemma 4.1.)

## Net

The extent-shrink of the wall to O(M^{7/4}) axis-hugging blocks stands at unified radius
sqrt(5 log n), c_--conditional, for Mn above the corrected threshold r_1 (not r_0).
Nothing here moves (L1') or chi = 1/3. Both REF-W1 debts (9.10 counter-check, D1 repair
verification) are DISCHARGED.
