# Independent review of route A2-two-addresses

Reviewer: workflow claude-51330238, 2026-10-12. Scope: every claim in `CLAIMS.json` marked PROVED or REFUTED,
and spot checks of the three EVIDENCE claims. Full FEI remains OPEN; nothing here bears on it beyond the class K2.
All code written for this review is in `referee_code/` (outputs as `*.json` beside the scripts). No file of the
route author was edited, and none of the route's scripts was run in a way that writes files.

## Verdicts

| Claim | Route status | Verdict | In one line |
|---|---|---|---|
| A2-L3 | PROVED | CONFIRMED | every step checked from the definitions; asserted exactly on all 2,208 nonzero product rows at \|C\| = 3 and on rows with \|C\| = 4..6 |
| A2-L3k | PROVED | CONFIRMED for k >= 1 | identity checked exactly on 14,769 product rows with k = 1..4; the integrality part is false at k = 0, so the claim needs k >= 1 (implicit in "addresses") |
| A2-T-A | PROVED | CONFIRMED | each step checked against the definitions; every numeric bound certified again with intervals |
| A2-T-S | PROVED | CONFIRMED | case split exhaustive, analytic steps checked, the computer step (rho in {2,3}) certified again by a different rigorous algorithm; exact exhaustive check for n <= 5 |
| A2-C-sel | PROVED | CONFIRMED | proof checked; 991 random members with \|y\| = 2..4 tested exactly; the addressing function attains equality |
| A2-H-ladder | PROVED | CONFIRMED | elementary; C_2 rests on A2-T-S |
| A2-R-lagr1 | REFUTED | CONFIRMED | single-multiplier bound recomputed: +0.021828, positive on every menu containing the fair rows with f <= 6 |
| A2-R-even-weights | REFUTED | CONFIRMED, value misstated | the shortcut does fail, but the bound is not "+0.0295 for every rho >= 3": it is +0.0320 at rho = 3 (e odd), varies with rho, and for e even it is negative (the shortcut works) at rho = 3, 4, 5 |
| A2-E-exh | EVIDENCE | reproduced for n <= 5 with exact signs | n = 6 not redone here; an independent Codex run (A032) reports the same sharp constant at n = 6 |
| A2-E-relax | EVIDENCE | partly reproduced | my certificate changes sign at c = 2.914374 for rho = 3, e odd, the route's relaxation value |
| A2-E-k3 | EVIDENCE | reproduced | count 2,634,528 and max H/I = H/I(AND_4), found by a different method |

Errata (none affects a verdict): (i) NOTES 5.2 states kappa(log2 10 - 2) - psi = 0.456918; the value is 0.4569154
(the proof only uses 0.4569). (ii) The closing sentence of NOTES 5.7 attaches the equality conditions (alpha on the
small side, D1 empty) to Phi, but Phi does not see alpha or D1: at n = 5, Phi = 0 exactly for 6,158 K2 functions
while H = c* I for only 48. The conditions are right for equality in H <= c* I, which is what the theorem states.
(iii) NOTES 5.2 says "In all cases Phi < 0"; this needs w_0 < 1. At w_0 = 1, Phi = -P_0 <= 0, with equality only for
constant f. (iv) Three rounded constants in NOTES (0.029464, 0.116664, 0.474039) are slightly above the true values
(0.0294597, 0.1166067, 0.4740378), so they are conservative.

## 1. Method

Every lemma and every inequality was derived again from the definitions, without reading the route's code first.
The computations use my own conventions (`refk2.py`): exact integer Walsh transforms; exact product-law tests by
cross-multiplication; and exact signs of quantities of the form H - c* I, written as q0 + sum_l q_l log2 l with
rational q's. Since log2 of distinct odd primes and 1 are linearly independent over Q, the sign is decided exactly:
symbolically when all q_l vanish, otherwise by interval evaluation at rising precision. The scenario-B certificate was
rebuilt with a different algorithm (closed-form maximisation on each linear piece instead of subdivision), in
mpmath interval arithmetic.

## 2. Lemmas 1-6, A2-L3 and A2-L3k

Checks. Lemma 1: the 16 sign vectors on two bits are 8 signed characters (one-hot transform) and 8 functions with
one or three -1's, whose transforms are all +-1/2 with sign product -1. Lemma 2: alpha_i = 0 kills every set
containing i, alpha_i = 1 every set missing i, so g_T = chi_{D1} phi(x_R); on the face every coefficient is nonzero;
the ratio along coordinate i is a ratio of nonzero dyadic rationals, hence rational. Lemma 3(a): phi takes values
in (1/2)Z, so phihat lies in 2^{-r-1}Z; for a prime l and J = {i : l | q_i}, prod_{J} p_i is prime to l, which gives
v_l(nu) >= v_l(prod q_i). Parts (b) and (c) are direct. Part (d): 2^{r+1} phihat(U) = sum_x 2 phi(x) chi_U(x) is
congruent mod 2 to the number of x with |phi(x)| = 1/2, independent of U, and the even and odd class statements
follow as written. Lemma 4: Ft <= 3 - log2(p^2+q^2) < 0 once p^2 + q^2 > 8, and the only coprime pairs below that
are (1,1) and (2,1); Ft(2,1) = 2/5 exactly. Lemma 5: |g_T| = |phi_T(x_R)| and |g_T| = 1/2 exactly on E_*; a set
that depends only on x_{R1} and only on x_{R2} depends only on x_{R1 cap R2}. Lemma 6: 4 w 2^r = sum (2 phi)^2 is an
integer of 2-adic valuation 2 v2(nu') - e_c, because v2(p^2+q^2) = 1 for odd-odd pairs and 0 otherwise.

Exact checks (`ref_rows.py`, which asserts every statement, including the identity of Lemma 3(c) as an exact
equality in Q[log2 primes]): all 2,208 nonzero product rows at |C| = 3; all rows of every K2 function at n <= 4; the
four rows of X008 (|C| = 4); the rows of 60 structured K2 functions with |C| = 4, 5, 6. No assertion failed.

A2-L3k (`ref_lemma3k.py`): rows of a Boolean f with k addresses take values in 2^{1-k}Z because a sum of 2^k signs
is even when k >= 1; the rest of the proof is unchanged. Checked exactly on 14,769 product rows with k = 1..4. At
k = 0 the claim is false as stated (f = 1 has kappa = 1, r = 0, so nu = 1/2; 75 such rows in the same run). The claim
is about address sets, so k >= 1 is the natural reading; I record it as a scope note.

## 3. Theorem A (A2-T-A)

The decomposition H - 4I = sum_T w_T [2 - 2 log2 nu'_T + sum_{R_T} (Ft_i - 4 alpha_{T,i}) - 4|T| - 4|D1_T|] is
exact. Every Ft_i - 4 alpha_i <= Ft_i - 4 m_i <= 0. Rows with T nonempty contribute at most -2 w_T; the empty row
contributes at most 0 unless nu'_0 = 1. Lemma E: nu'_0 = 1 forces the odd class, every pair odd-odd,
w_0 = 2^{-r-2} N with N = prod n_i, n_i = (p_i^2 + q_i^2)/2 >= 5 odd for unfair pairs, and w_0 <= 1 - (3/4) 2^{-r} by
Lemma 5. Each case checks out: u = 0 gives 4 w_0 <= 1; u >= 1 with x = log2 w_0 gives the factor
2^x (2 + u beta - f0 - x) and f0 >= u(log2 5 - 1) - 2 - x; u = 1, f0 = 0 forces (p,q) = (3,1). Interval checks
(`ref_constants.py`): beta = log2(17/16) < 0.0875; log2 5 - 1 - beta > 1.2344; for u >= 4 the factor is at most
-0.94 (negative); in the cases u = 2,3, (u = 1, f0 = 0) and (u = 1, f0 >= 1) the bound stays below 2 by 0.47, 0.28
and 0.87. Exact exhaustive check: no K2 function with H > 4I for n <= 5.

## 4. Theorem S (A2-T-S)

Case split. E_* empty (scenario A); E_* the whole cube (each row is (1/2) sigma_T with sigma_T Boolean with product
law, so H = 2 + avg H(sigma) <= 2I); otherwise rho = |R_cap| >= 1 because E_* is a cylinder over R_cap. Then
rho >= 4 (5.5), rho in {2,3} (5.6), rho = 1 with e = 1 (5.7; e = 2 is the whole cube). The split is exhaustive. The
single-row case falls under scenario A and is also covered there.

5.1. With e_T = L_T + H(q_T) - c(|T| + I(q_T)), H - cI = sum w_T e_T exactly; e_T <= ebar_T uses only alpha >= m,
alpha = 1/2 for fair coordinates and dropping -c|D1|. Eliminating f_T through L_T = 2 + f_T - sum_unf (s_i - 2) -
2 log2 nu'_T gives ebar_T = delta L_T + 2 kappa (1 - log2 nu'_T) - sum G_i - c|T|, as stated.

5.2 (scenario A). P_T >= 0 since nu' >= 2 and G >= 0 for every pair ((G1), (G2)). For u_0 = 0, P_0 = kappa (f_0 - L_0)
with f_0 an integer >= L_0; for u_0 >= 1, P_0 >= kappa e_c + sum G >= 0.4569. The Gibbs step is the exact maximum of
delta H(w') - c E|T| over laws on {1, 2, 12}. Interval values: K = 2.4264334; delta log2(1 + 2^{-K/delta}) =
0.0294597 < 0.4569 * 0.55 * (1 + log2 0.55) = 0.0345539; delta - K/2 < 0 and delta - 0.45 K < 0. Correct, with
erratum (iii).

5.3-5.4. Odd rows are exactly the rows with r_T = rho when e is odd, with nu' odd and odd-odd pairs; even rows have
r_T >= rmin and 2 v2(nu') >= e_c. The odd envelope uses G >= GB (s - 1) for odd-odd pairs (s >= log2 10, and the ratio
(kappa(s-2) - psi)/(s-1) has derivative (kappa + psi)/(s-1)^2 > 0). The even envelope: the LP lower bound
Gmin(X, E) = GA min(X_+, SA E) + GB (X_+ - SA E)_+ is valid because GA < GB and only the (2,1) pairs, at most
e_c <= 2j of them, have s - 1 = SA; an odd factor o of nu' costs 2 kappa log2 o and saves at most 2 GB log2 o. The
j-coefficient 2GB - 2 kappa + 2(GB - GA) SA = -0.0882862 < 0, so j = 1 is the worst case, and
2(GB - GA) SA = 0.4740378 <= K0 = 0.5623241.

5.5 (rho >= 4). 2a log2(1 + 2^{-c/a}) + K0 - 4 GB = -0.108200 < 0 (interval).

5.6 (rho in {2,3}), certified again by a separate method (`ref_certificate.py`). The Lagrangian step
Phi = mu + sum w_T (ebar_T - mu) <= mu + M_0 + 2 M_1 + M_2 is valid because all four rows are present in scenario B.
For each j the even envelope T_j(L) is the minimum of three linear functions of L (slopes GB, GA, 0), so on each
piece the target is 2^{-L}(A + BL) with B > 0, maximised at clamp(1/ln 2 - A/B). Extending a piece past its end only
raises the bound, so covering with overlapping pieces is rigorous. Odd rows were enumerated afresh over every
odd-odd coprime pair (not only the minimal G per norm): 4 rows for rho = 2 and 9 for rho = 3, which I also counted
by hand. Rigorous upper bounds of the minimum over mu:

| case | this review (closed form) | route K = 4000 | route K = 20000 |
|---|---|---|---|
| rho = 2, e odd | -0.087744 | -0.087204 | -0.087636 |
| rho = 2, e even | -0.683834 | -0.683607 | -0.683789 |
| rho = 3, e odd | -0.044105 | -0.044105 | -0.044105 |
| rho = 3, e even | -0.266973 | -0.266383 | -0.266855 |
| rho = 4 (odd / even) | -0.372869 / -0.315103 | -0.371986 / -0.314275 | |
| rho = 5 (odd / even) | -0.350346 / -0.452532 | -0.349841 / -0.451507 | |

The subdivision values converge to the closed-form ones from above, as they should. Non-vacuity
(`ref_cert_sensitivity.py`, `ref_cert_crossing.py`): with all constants recomputed from c, the rho = 3 (e odd)
certificate is +0.0153 at c = 2.90 and -0.0060 at c = 2.92, and changes sign at c = 2.914374, the route's relaxation
value for that scenario; for rho = 2 (e odd) it changes sign at 2.880324 and for rho = 3 (e even) at 2.757948, both
above the relaxation values 2.786517 and 2.752688, as a dual bound must be. All are below c*, so the margin at c* is
genuine, not a rounding effect.

5.7 (rho = 1, e = 1). w_T = 1/8 + mu(E_T) and odd rows have N in {1, 5}. In (i), a (3,1) row has weight 5/8, so the
other rows vanish off E_*, sigma_T has product law (a marginal of a product law), and e_T <= 4 - c(|T| + 1/2) by
product rigidity (RIG Th. 1). The T0 = empty bound is exactly 0, symbolically:
(5/8)(log2(8/5) + h(1/10) - c/10) + (1/8)(12 - 5.5c) = 4 - (9/8) log2 3 - (3/4)c = 0. For T0 nonempty the bound is
-c|T0|/2. In (ii) the numbers are 0.31526 - 0.86858 < 0 and 0.27708 - 0.53217 < 0 (intervals).

Exact exhaustive tests. n <= 4 (`ref_exhaust_n4.py`): all 65,808 Boolean functions on 2-4 variables and all address
pairs; K2 sizes 16, 256 and 23,040 (the route's 23,038 excludes the two constants); max H/I = c* at n = 3, 4;
equality for exactly 16 (n = 3) and 64 (n = 4) functions, the one-point functions of three variables; no function
with H > c* I or H > 4I; the chain H - c* I <= Phi <= 0 holds exactly for every K2 function. n = 5
(`ref_enum_n5.py`): an independent row-based enumeration (2,209 candidate rows including zero, quadruples grouped by
half-set, one-set and sign pattern) finds 1,564,928 K2 functions with address pair (0,1), the route's count; by
coordinate permutation this is all of K2 at n = 5. Max H/I = c*; the 48 functions with float H - c* I > -1e-9 are
all exact equalities; e_T <= ebar_T holds exactly for all 2,208 rows; among the 6,158 functions with float
Phi > -1e-9 none has exact Phi > 0. Functions were rebuilt from their rows and tested again with the generic
membership test.

Strongest case against the theorem, and why it fails. (1) A configuration missing from the case split: the split is
by E_* (empty, whole, proper) and then by rho and e, which is exhaustive. (2) An error in the computer-assisted
step: a different algorithm agrees to 6 digits, and the certificate turns positive exactly at the rho = 3
relaxation value, so it is tight where it matters and the 0.044 margin at c* is not an artifact. (3) A relaxation
constraint that genuine K2 functions violate: every constraint was proved again and asserted exactly on all K2 rows
with |C| <= 3 and on 60 functions with |C| = 4..6. The check that would refute the theorem is a K2 function with
H > c* I; none exists for n <= 5 (exact), none appeared in the families of Section 9, and the n = 6 searches of the
route and of A032 report none.

## 5. Corollary A' (A2-C-sel)

Rows s 1_{tau = T} are {0,+-1}-valued, so Lemma 3 applies with the same proof (it uses only phi in (1/2)Z) and gives
the even class, nu' >= 2, hence L_T + H(q_T) <= sum Ft_i <= 4 sum m_i <= 4 I(q_T); summing with weights w_T gives
H <= 4 (I - sum_T w_T |T|) = 4 (I - Inf_y). The number of address coordinates plays no role. Sharpness: y_x with a
address bits has rows 1_{x = u}, all fair, H = 2a, I = 1 + a/2 and I - Inf_y = a/2. Exact random test
(`ref_adversarial.py`, part 6): 991 members with |y| = 2, 3, 4 and |x| = 3, 4, 5; no violation; the maximum of
H - 4(I - Inf_y) is exactly 0.

## 6. The ladder (A2-H-ladder)

C_k is nondecreasing because the class is defined by an address set of size at most k. With |C| = 1 every law on
one bit is product, so K_k contains every function of k + 1 variables (and every function with k + 1 relevant
variables), which gives sup_k C_k = C_FEI, also when C_FEI is infinite. C_0 = C_1 = 2 by RIG Th. 1 / Cor. 1.1 and
ONE Th. 2.1, read in the sources; C_0 = 2 is also a special case of Potapov, arXiv:2609.21563, Theorem 1 (partially
bent functions satisfy H <= 2I), since a Boolean function with product spectral law is a character times a bent
function on a coordinate subset. C_2 = c* is Theorem S. C_3 >= H/I(AND_4) = 3.4024756 holds trivially.

## 7. The refuted shortcuts

A2-R-lagr1 (`ref_refutations.py`). In scenario A with absent rows allowed, the minimum over mu of
mu + M_0 + 2 M_1 + M_2 is computed exactly (B is convex and piecewise linear; all kinks enumerated) on four menus, from
(r <= 6, no unfair pair, nu' <= 8) to the route's (r <= 10, u <= 3, p <= 9, nu' <= 64): +0.021828 at mu = -delta in
every case. The fair rows explain it: at mu = -delta, M_0 = delta and M_1 = (7 delta - c)/64 from f = 6, so
B = 2 (7 delta - c)/64. A rigorous grid evaluation (Lipschitz constant 3) on the fair menu with f <= 14 gives
min B >= +0.021893 (larger, because rows with f = 11..13 enter M_2). A larger menu only raises the bound, so the
shortcut fails. CONFIRMED.

A2-R-even-weights (`ref_refutations.py`, `ref_refutation_witness.py`). My values agree digit for digit with the
route's own `lagr_simple.py` output, and they contradict the claim's wording:

| rho | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| e odd | +0.032033 | +0.041356 | +0.050428 | +0.048373 | +0.035580 | +0.030931 | +0.029915 | +0.029673 | +0.029606 |
| e even | -0.220367 | -0.057582 | -0.003032 | +0.017174 | +0.025221 | +0.028220 | +0.029209 | +0.029448 | +0.029460 |

The Gibbs gap 2 delta log2(1 + 2^{-c/delta}) = 0.0294597 is only the limit as rho grows. Rigorous primal witnesses
(exact rational weights summing to 1, interval values; by weak duality each makes the bound positive for every mu):
rho = 3, e odd: +0.002161 (rows empty and {1,2} even with weights 29/32 and 1/32, rows {1}, {2} odd fair with
weight 1/32); rho = 4, e odd: +0.026420; rho = 5, e odd: +0.042960; rho = 6, e even: +0.017174. So the shortcut fails
for e odd at every rho >= 3 and for e even from rho = 6 on; for e even and rho = 3, 4, 5 it would in fact certify.
The refutation stands; the stated value and the range "every rho >= 3" should be corrected as above.

## 8. EVIDENCE claims

A2-E-exh: reproduced exactly for n <= 5 (Section 4). Not redone at n = 6. The Codex run
`brain_workers/FEI100_20261011/agents/A032/runs/20261011T234647Z-fleet05-A032-boolean-phase-realizability/REPORT.md`
reports an exact n = 6 closure with the same constant by a different method (common-phase mask catalogue with
rational logarithm bounds); I read its report but did not replay it.

A2-E-relax: the sign changes of my certificate (Section 4, 5.6) match the route's relaxation value 2.914374 for
rho = 3, e odd, and lie above the values for rho = 2 and for rho = 3, e even. The rest of the relaxation table was
not reproduced.

A2-E-k3 (`ref_k3_n5.py`), by a different method. For |C| = 2 a row's squared law is product iff
(g00 g11 - g01 g10)(g00^2 + g11^2 - g01^2 - g10^2) = 0: the condition is A^2 = B^2 with A - B = 4(g00 g11 - g01 g10) and
A + B = 2(g00^2 + g11^2 - g01^2 - g10^2), and it splits over the fibre pairs (F00, F11) and (F01, F10). With F00
reduced to its 14 orbit representatives under y-translations, y-permutations and negation (a group acting on the
whole function, so the reduction is valid for the maximum and for the count per representative), I get 2,634,528
functions, the route's count, and max H/I = 3.402475551 = H/I(AND_4); the 19 near-maximisers were rebuilt, tested
again for membership, and are exact equalities. The conjecture C_3 = H/I(AND_4) remains open.

## 9. Adversarial families (`ref_adversarial.py`)

- X008, rebuilt from ONE_BIT_ENDPOINT section 3: Boolean, H = 5, I = 17/8, influences (1/4, 1/4, 1/2, 1/2, 1/2, 1/8),
  in K2, H < c* I. The empty row has w = 5/8, pairs three (1,1) and one (2,1), nu' = 4, e_c = 1, values in {0,+-1};
  the other rows have w = 1/8, three fair coordinates and nu' = 2. X008 is a scenario-A function and a
  signed-character selector, so Corollary A' also applies (5 <= 6.5).
- X001 parity lifts of every g on 2-4 variables (65,802 nonconstant lifts): 1,290 lie in K2, max H/I = 4/3, no
  violation.
- X002 selector splice, m = 3, 5: product spectrum, in K2, H/I = 2.
- X009 sparse bent perturbation: in K2 for m = 2 (H/I = 1.2668), not in K2 for m = 4, 6. One- to three-point flips of
  a 4-bit bent function with up to two dummy coordinates: 8,304 tested, 112 in K2, max H/I = 2.347691, no violation.
- X004 overlapping supports: F = zy is a character, H = 0. X006 and X013 are not Boolean and lie outside K2 by
  definition; the proof uses Booleanity through Lemma 1 (pointwise fibres), Lemma 5 (weights forced by E_*) and
  sum w_T = 1, and nowhere treats a row as a Boolean function on its own.
- Structured random selectors with character and bent cells on decision-tree partitions, n = 6..10: 474 members,
  max H/I = 2.0, no violation; the exact chain H - c* I <= Phi <= 0 on 60 of them with |C| = 4..6.

## 10. Literature

Web search was unavailable (the session's search budget was exhausted). I fetched the arXiv listing for "Fourier
entropy influence conjecture" (18 papers, 1105.2651 to 2609.21563, abstracts, read 2026-10-12): none treats product
spectral laws, spectral address coordinates, or the 3-variable AND as extremal. The closest result is
V. N. Potapov, "On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions", arXiv:2609.21563
(18 Sep 2026): Theorem 1, partially bent functions satisfy H <= 2I; Theorem 2, plateaued functions satisfy
H <= 4I, with 4 sharp. It contains the zero-address endpoint C_0 = 2 as a special case. It does not contain
Theorem S (AND_3 is not plateaued) or Corollary A' (X008 is a signed-character selector with product rows whose
squared spectrum takes the two values 1/16 and 1/64, so it is not plateaued); the addressing functions lie in both
classes. A full-text novelty check was not possible, so novelty of Theorems A and S and of the row identity remains
unverified.

## 11. Files

`referee_code/`: `refk2.py` (exact Walsh, membership, exact signs), `ref_rows.py` (row analysis, Lemmas 1-6),
`ref_exhaust_n4.py`, `ref_enum_n5.py`, `ref_certificate.py`, `ref_cert_sensitivity.py`, `ref_cert_crossing.py`,
`ref_constants.py`, `ref_refutations.py`, `ref_refutation_witness.py`, `ref_adversarial.py`, `ref_lemma3k.py`,
`ref_k3_n5.py`, and the JSON outputs of the scripts that write one.
