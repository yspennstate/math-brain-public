# A2 two spectral addresses (ledger C016, C022, C031)

Route owner: Opus agent A2, workflow claude-51330238, started 2026-10-12 (local clock).
Full FEI remains OPEN. Everything below is about the proper class defined in Section 1.

## 0. Status summary (kept current; details in later sections)

- THEOREM A (Section 3, complete analytic proof): every f in K2 satisfies H(f) <= 4 I(f).
- THEOREM S (Section 5): sup over K2 of H/I equals c* = 16/3 - (3/2) log2 3 = 2.95588958..., attained by the
  3-variable AND. Proof is analytic except Section 5.6 (rho = 2, 3), which is a rigorous interval-arithmetic
  certificate (code/verify_rho23.py). C = 2 (refuted by X008, 40/17) is replaced by the sharp c*.
- Key tool (Lemma 3): for a product row, L_T + H(q_T) = 2 - 2 log2 nu'_T + sum_i Ft(p_i,q_i) exactly, where nu' is
  the row's minimal Walsh coefficient in units of 2^{-r-1} divided by prod q_i. The address entropy is paid by the
  arithmetic of the minimal coefficient; Ft(p,q) <= 4 q^2/(p^2+q^2) with equality only for fair coordinates.
- Corollary A': signed-character selectors with product rows and ANY number of addresses: H <= 4 (I - Inf_y),
  sharp (addressing functions).
- Evidence: exhaustive K2 for n <= 6 (corrected symmetry use) gives max H/I = c* (AND_3); arithmetic relaxation;
  H - c*I <= Phi <= 0 checked on ~98,000 sampled K2 functions.

## 1. Definitions and the exact target

f : {-1,1}^n -> {-1,1}, uniform measure, fhat(S) = E[f chi_S], p(S) = fhat(S)^2, H(f) = sum p log2(1/p),
I(f) = sum |S| p(S). Logs base 2 unless written ln. h(t) = binary entropy in bits.

Spectral addresses. Fix A subset [n] with |A| = 2 (coordinates a1, a2) and C = [n] \ A, m = |C|.
Write a spectral set as S = T u U with T subset A, U subset C. Partial Walsh rows

    g_T(x) = E_y[ f(y,x) chi_T(y) ],   x in {-1,1}^C, y in {-1,1}^A,

so f(y,x) = sum_T g_T(x) chi_T(y) and fhat(T u U) = ghat_T(U). Row weights w_T = ||g_T||_2^2 = P(S_A = T);
conditional laws q_T(U) = ghat_T(U)^2 / w_T (for w_T > 0).

CLASS K2 (the target class). f is in K2 when some A with |A| <= 2 has: for every T with w_T > 0, q_T is a
product law on {0,1}^C. (|A| = 0: the whole law is product; |A| = 1: one address.)

EXACT TARGET. Find an explicit finite C2 with H(f) <= C2 I(f) for all f in K2 (all n), and as much as
possible about the optimal constant c* = sup_{f in K2, f nonconstant} H(f)/I(f).
Known before this route: |A| <= 1 gives H <= 2I (RIG Th.1/Cor 1.1, ONE Th.2.1); X008 gives a genuine
two-address f with H/I = 40/17 > 2 (C031).

Notation used throughout:
- L_T = log2(1/w_T); H(f) = H(w) + sum_T w_T H(q_T) = sum_T w_T [L_T + H(q_T)].
- I(f) = Inf_A + sum_T w_T I(q_T), with Inf_A = sum_T w_T |T| = Inf_{a1}(f) + Inf_{a2}(f) and
  I(q_T) = sum_U q_T(U)|U|. (Physical influence of x_i in C equals sum_T w_T alpha_{T,i}.)
- For a product row: alpha_{T,i} = q_T(i in U); D0_T = {alpha=0}, D1_T = {alpha=1}, R_T = active set
  (0<alpha<1), r_T = |R_T|; m_{T,i} = min(alpha_{T,i}, 1-alpha_{T,i}).

## 2. Work log (attempts in order, including failures)

### 2.1 First computations (exact Walsh, float logs = evidence)

- code/exhaust_small.py: every Boolean f on n <= 4 variables, every address set |A| <= 2.
  n=3: all 256 functions are in K2 (|C| = 1, a law on one bit is always product). n=4: 23,038 functions in K2.
  Max H/I in K2 for n <= 4 is 2.955889582... attained by the 3-bit AND (one-point function) and its images.
- AND_3 is in K2: f(y1,y2,x) = -1 iff y1=y2=x=-1. Spectrum 9/16 at the empty set, 1/16 on each of the
  7 nonempty sets. H = 4 - (9/8)log2 3, I = 3/4, H/I = 16/3 - (3/2) log2 3 = 2.95588958... > 40/17 = 2.3529.
  So X008 is NOT the worst two-address example; the extremal candidate is the 3-variable AND.
- code/rows_search.py (rows enumerated, then compatible quadruples): |C| = 1, 2, 3 with the address pair fixed.
  |C|=3 (n=5): 2,209 product rows, 1,564,928 functions in K2 with that address pair; max H/I = 2.955889582 (AND_3
  with dummy variables). (An earlier direct 16^7 fiber brute force was stopped: over the 10-minute budget.)
- code/prod3_wide.py + code/rows4.py + code/rows4_fast.py: |C| = 4 (n = 6). All 90,177 product rows on 4 bits
  (76,032 with full support), row 0 reduced to 93 orbit representatives (x-translations, x-characters,
  x-permutations, negation; heaviest row moved to T=empty by y-characters). Dinkelbach maximisation of
  sum_T[a_T - lam b_T] (H and I are additive over rows). Max H/I at n = 6 is again 2.955889582 (AND_3).
  Spot check: all four X008 rows are in the enumerated row set.
- BUG FOUND AND FIXED (same session): rows4/rows4_fast reduced row 0 by x-character multiplication and moved the
  heaviest row to T = empty by y-character multiplication. Both preserve H but NOT I (multiplying by chi_V shifts
  every spectral set by V). Those runs are void. code/rows_v2.py uses only x-translations, x-permutations and
  negation (each preserves H and I), lets row 0 range over orbit representatives of ALL product rows (287 at m=4),
  and enumerates rows 1,2,12 completely. Cross-check: at m = 3 its exact count of K2 functions with the fixed
  address pair is 1,564,928, equal to the independent count of rows_search.py. Corrected n = 6 result
  (data/v2_m4.json): max H/I = 2.955889582 (AND_3 with dummies); at lam = 2.955889582 the maximum of
  sum_T [a_T - lam b_T] is 1.1e-16 (float zero). Evidence only (float logs).
- code/check_identity.py verifies, on every nonzero product row at m = 3 (2,208 rows) and m = 4 (90,176 rows),
  the exact identities of Lemma 3 below (integrality of nu', the weight formula as exact rationals, the
  entropy identity to 1e-9, the parity statements). Only (p,q) in {(1,1),(2,1),(3,1),(4,1)} occur at m <= 4;
  nu' in {1 (odd class), 2, 4, 8 (even class)}.

## 3. Proved results

Throughout f is Boolean, A = {a1,a2}, rows g_T as in Section 1, and every row with w_T > 0 has a product law.

### Lemma 1 (pointwise structure). For every x in {-1,1}^C the vector (g_T(x))_T is the normalized Walsh
transform of the sign vector (f(y,x))_y in {-1,1}^4. Hence either
 (type 1) exactly one g_T(x) = +-1 and the other three vanish (f(.,x) = +-chi_T), or
 (type 2) all four g_T(x) = +-1/2 and the product of the four signs is -1 (f(.,x) is a 2-bit bent function).
Proof: the 16 sign vectors on two bits are the 8 signed characters and the 8 signed 2-bit bent functions; the
Walsh transform of a signed character is one-hot, that of a bent function has all entries +-1/2, and the U = {a1}
convolution identity 2(g_0 g_1 + g_2 g_12) = 0 forces the sign product -1. QED.
Let E_* be the set of type-2 points. Then |g_T| = 1/2 on E_* for every T, and |g_T| in {0,1} off E_*.

### Lemma 2 (shape of a product row). Let w_T > 0 and let q_T be product with marginals alpha_i. Put
D0 = {alpha_i = 0}, D1 = {alpha_i = 1}, R = R_T = the rest, r = |R|. Then g_T(x) = chi_{D1}(x) phi(x_R) where phi
is a function on {-1,1}^R with values in {0,+-1/2,+-1} whose Walsh coefficients are all nonzero, and
|phihat(U)| = kappa * prod_{i in U xor U*} k_i for U subset R, where U* is a fixed minimiser of |phihat|,
kappa = min |phihat| > 0, and k_i = sqrt((1-m_i)/m_i) >= 1 with m_i = min(alpha_i, 1-alpha_i).
Each k_i is rational; write k_i = p_i/q_i in lowest terms (p_i >= q_i >= 1).
Proof: alpha_i = 0 kills every coefficient containing i; alpha_i = 1 kills every coefficient missing i, so
g_T = x_i * (function free of x_i). On the remaining face every coefficient is nonzero because the product law has
all factors positive. The ratio |phihat(J + i)| / |phihat(J)| equals sqrt(alpha_i/(1-alpha_i)) or its inverse for
every J, and it is a ratio of two dyadic rationals, hence rational. QED.

### Lemma 3 (granularity identity). In Lemma 2 write kappa = nu 2^{-r-1}. Then:
 (a) nu is a positive integer and prod_i q_i divides nu; put nu' = nu / prod_i q_i (a positive integer).
 (b) w_T = nu'^2 4^{-(r+1)} prod_{i in R} (p_i^2 + q_i^2).
 (c) L_T + H(q_T) = 2 - 2 log2 nu' + sum_{i in R} Ft(p_i, q_i),
     Ft(p,q) := 2 - log2(p^2+q^2) + h(q^2/(p^2+q^2)).
 (d) All coefficients of phi lie in one class mod 2^{-r}: either all are in 2^{-r} Z ("even class") or all are odd
     multiples of 2^{-r-1} ("odd class"). The odd class holds iff the number of points of {-1,1}^R where |phi| = 1/2
     is odd. In the even class nu' is even. In the odd class nu' is odd and every p_i, q_i is odd.
Proof. (a) phi takes values in (1/2)Z, so phihat(U) = 2^{-r} sum_x phi(x) chi_U(x) lies in 2^{-r-1} Z; kappa is a
nonzero element, so nu is a positive integer. For every J subset R the coefficient at U* xor J has modulus
2^{-r-1} nu prod_{i in J} p_i/q_i, which must be an integer multiple of 2^{-r-1}. Fix a prime l and take
J = {i : l | q_i}; since gcd(p_i,q_i) = 1 the numerator prod_{i in J} p_i is prime to l, so
v_l(nu) >= sum_{i in J} v_l(q_i) = v_l(prod_i q_i). Hence prod_i q_i | nu.
(b) w_T = sum_U phihat(U)^2 = kappa^2 prod_i (1 + k_i^2) = nu^2 4^{-r-1} prod_i (p_i^2+q_i^2)/q_i^2.
(c) H(q_T) = sum_i h(m_i) with m_i = q_i^2/(p_i^2+q_i^2); L_T = log2(1/w_T) = 2(r+1) - 2 log2 nu'
- sum_i log2(p_i^2+q_i^2); add.
(d) 2^{r+1} phihat(U) = sum_x 2phi(x) chi_U(x) is congruent mod 2 to the number of x with 2phi(x) odd, which
does not depend on U. Even class: every nu prod_{i in J} p_i/q_i is even; with l = 2 and J = {i : q_i even} as in
(a), v_2(nu) >= 1 + v_2(prod q_i), so nu' is even. Odd class: every nu prod_{i in J} p_i/q_i is an odd integer.
J = empty gives nu odd; as prod q_i | nu, every q_i is odd and nu' = nu/prod q_i is odd; J = {i} gives
(nu/q_i) p_i odd with nu/q_i an odd integer, so p_i is odd. QED.
(Checked exactly on every product row for |C| <= 4: code/check_identity.py.)

### Lemma 4 (the per-coordinate function). Ft(1,1) = 2, Ft(2,1) = 2/5, and Ft(p,q) < 0 for every other coprime
p > q >= 1. Consequently Ft(p,q) <= 4 m with m = q^2/(p^2+q^2), with equality iff p = q = 1.
Proof: h <= 1, so Ft <= 3 - log2(p^2+q^2) < 0 once p^2+q^2 > 8; the only coprime pairs with p^2+q^2 <= 8 are
(1,1) and (2,1). Ft(2,1) = 2 - log2 5 + [ (1/5)log2 5 + (4/5)log2(5/4) ] = 2 - 8/5 = 2/5 <= 4/5. QED.

### Lemma 5 (the type-2 set). If w_T > 0 then E_* = {x : |g_T(x)| = 1/2} is a cylinder over R_T. If row T is of odd
class then |E_* restricted to the R_T-cube| is odd, so mu(E_*) >= 2^{-r_T}, and since every row has |g_{T'}| = 1/2 on
E_*, w_{T'} >= mu(E_*)/4 >= 2^{-r_T - 2} for all four T'. In particular sum_{T' != T} w_{T'} >= (3/4) 2^{-r_T}.
Proof: |g_T(x)| = |phi_T(x_{R_T})| and Lemma 1; the parity statement is Lemma 3(d). QED.

### THEOREM A. Every f in K2 satisfies H(f) <= 4 I(f).
Proof. Lemma 3(c) gives the exact decomposition
   H(f) - 4 I(f) = sum_T w_T [ 2 - 2 log2 nu'_T + sum_{i in R_T} (Ft_i - 4 alpha_{T,i}) - 4|T| - 4|D1_T| ].
By Lemma 4 and alpha >= m, every Ft_i - 4 alpha_{T,i} <= 0, and equals 0 for fair coordinates (alpha = 1/2).
For T != empty the bracket is <= 2 - 4 = -2. For T = empty with nu'_0 >= 2 the bracket is <= 0. Hence
   H - 4I <= [nu'_0 = 1] w_0 (2 + sum_{i in R_0} (Ft_i - 4 alpha_{0,i})) - 2 (1 - w_0)          (*)
(writing 0 for the empty address value). If nu'_0 >= 2 we are done. Let nu'_0 = 1 (Lemma E below). QED.

Lemma E. If nu'_0 = 1 then w_0 (4 + sum_{i in R_0} (Ft_i - 4 alpha_{0,i})) <= 2, which is (*) <= 0.
Proof. nu'_0 = 1 is odd, so row 0 is of odd class (Lemma 3(d)); all its p_i,q_i are odd. Fair coordinates contribute
0 to the sum. An unfair odd pair has p >= 3, so p^2+q^2 = 2n with n odd >= 5; then Ft = 1 + h(m) - log2 n and
Ft - 4 alpha <= 1 + (h(m) - 4m) - log2 n <= 1 + beta - log2 n, beta := max_t (h(t) - 4t) = log2(17/16) < 0.0875.
Let f0 = # fair, u = # unfair coordinates of row 0, r = f0 + u, N = prod n_i >= 5^u. By Lemma 3(b),
w_0 = 2^{-2r-2} 2^{r} N = 2^{-r-2} N, and by Lemma 5, w_0 <= 1 - (3/4) 2^{-r}.
 u = 0: w_0 = 2^{-r-2} <= 1/4, so the left side is <= 1.
 u >= 1: with x = log2 w_0 = log2 N - r - 2 <= 0 the left side is <= 2^x (4 + u(1+beta) - log2 N)
   = 2^x (2 + u beta - f0 - x). From N >= 5^u, f0 >= u(log2 5 - 1) - 2 - x, so 2 + u beta - f0 - x
   <= 4 - u(log2 5 - 1 - beta) <= 4 - 1.2344 u. For u >= 4 this is negative; for u = 2, 3 the left side is
   <= 4 - 1.2344u <= 1.54 (as 2^x <= 1).
 u = 1, f0 = 0: r = 1, w_0 = n/8 <= 5/8 forces n = 5, (p,q) = (3,1), m = 1/10; left side
   <= (5/8)(4 + 1 + h(1/10) - 4/10 - log2 5) = (5/8)(2.7469...) < 1.72.
 u = 1, f0 >= 1: the left side is <= 2^x(2 + beta - f0 - x) <= max_{x<=0} 2^x (1 + beta - x) = 2^{x*}/ln 2
   with x* = 1 + beta - 1/ln 2, which is < 1.13.
In all cases the left side is < 2. QED.

### Corollary A' (signed-character selectors, any number of addresses). Let y be any block of coordinates and
f(y,x) = s(x) chi_{tau(x)}(y) (every fiber is a signed character). If every row s 1_{tau = T} has a product law
then H(f) <= 4 (I(f) - Inf_y(f)) <= 4 I(f), and the constant 4 is sharp.
Proof: rows are {0,+-1}-valued, hence of even class, so nu' >= 2 and L_T + H(q_T) <= sum_i Ft_i <= 4 I(q_T);
sum over T with weights w_T. Sharpness: the addressing function f(y,x) = y_x with a address bits x and 2^a data
bits y has rows 1_{x = u} (product, all fair), H = 2a, I = 1 + a/2, I - Inf_y = a/2; H/I -> 4. QED.
(For two addresses the type-1-only case is exactly the case E_* = empty.)

### Lemma 6 (integrality). 4 w_T 2^{r_T} = sum_{x in R-cube} (2 phi(x))^2 is an integer, divisible by 4 when the row
is {0,+-1}-valued. With e_c(T) = #{i in R_T : p_i^2 + q_i^2 odd}: 2 v_2(nu'_T) >= e_c(T), and >= e_c(T) + 2 for
{0,+-1}-valued rows. Proof: by Lemma 3(b), 4 w 2^r = nu'^2 2^{-r} prod(p_i^2+q_i^2), and v_2(p^2+q^2) = 1 when p,q are
both odd (they are coprime, so not both even), 0 otherwise; so v_2(4 w 2^r) = 2 v_2(nu') - e_c. QED.
Lemma 5 refined: let rho = |R_cap|, R_cap = intersection of all R_T, and e = size of the base of E_* in the R_cap-cube.
Row T is of odd class iff e is odd and r_T = rho. If E_* is nonempty, every row is half-valued (none is {0,+-1}),
all four rows are present and w_T >= e 2^{-rho}/4. If E_* is empty every row is {0,+-1}-valued.
Proof: E_* is a cylinder over every R_T (Lemma 5), hence over R_cap (a set depending only on x_{R1} and only on
x_{R2} depends only on x_{R1 cap R2}); its trace on the R_T-cube has e 2^{r_T - rho} points, odd iff e is odd and
r_T = rho; apply Lemma 3(d). mu(E_*) = e 2^{-rho} and |g_T| = 1/2 on E_* give the weight bound. QED.

## 4. Toward the sharp constant c* = 16/3 - (3/2) log2 3 (AND_3)

### 4.1 The arithmetic relaxation (code/relax.py; evidence)
Replace each row by its type (f fair coordinates, unfair pairs (p,q), nu', class), constrained only by Lemmas 3, 5, 6,
with b_T = f/2 + sum m (smallest possible), and maximise H/I over four types with total weight exactly 1.
Scenario A: E_* empty (all rows {0,+-1}). Scenario B(rho, e odd/even): E_* nonempty.
Results (all four positions, Dinkelbach, exact weights):
  (r<=6,u<=2,p<=5,nu'<=16) and (r<=9,u<=3,p<=7,nu'<=64):  overall sup = 2.9558895822515994 = AND_3 (B, rho=1, e odd).
  Next: B rho=3 e odd 2.914374 (weights 25/32,1/32,5/32,1/32: row 0 odd with f=1 and two (3,1) coordinates;
  rows {1},{12} odd fair r=3; row {2} odd f=2 + one (3,1)), B rho=2 e odd 2.786517, B rho=3 e even 2.752688,
  scenario A 2.505329, others lower; rho=0 gives 2.
So the relaxation, which uses only proven constraints, appears to have sup c* exactly. A proof that the relaxation's
sup is c* (for unbounded parameters) would prove that c* is the optimal constant on K2. Section 5 gives that proof.
code/validate_relax.py checked every relaxation constraint (cylinder structure of E_*, the odd-class rule, the
weight lower bound, both integrality forms) on ~180,000 sampled K2 functions with |C| = 3, 4: all hold.

### 4.2 Failed or insufficient attempts (kept as witnesses)
- Single-multiplier Lagrangian over the full relaxation (code/lagr.py): certifies every scenario-B case
  (rho = 1 exactly 0, others negative) but gives +0.0218 in scenario A: tiny rows exploit the free weight. Fixed by
  the direct scenario-A argument of 5.2 (the heavy row must pay).
- Simplified bound that keeps only the weights of even-class rows (code/lagr_simple.py): fails for rho >= 3 with
  +0.0295 = 2 delta log2(1 + 2^{-c/delta}), the Gibbs gap of delta H(w) - c Inf_A. Lesson: heavy even rows must be
  charged (they need many unfair coordinates or a large nu'); the envelopes of 5.4 do this.
- Crude per-coordinate bound F(m) <= C0 m with C0 = 2 + 4/(e ln 2) = 4.12295 (from the cruder identity
  L + H = 2 - 2 log2 nu + sum F(m_i), F(m) = 2 - log2(1/m) + h(m)): valid but weaker than Lemma 4's Ft <= 4m.

## 5. THEOREM S (sharp constant). For every f in K2, H(f) <= c* I(f), c* = 16/3 - (3/2) log2 3 = 2.9558895822...
Equality holds for AND_3 (f = -1 iff y1 = y2 = x = -1), so c* = sup_{K2} H/I.

Notation: c = c*, kappa = c/2 - 1 = 0.4779448, delta = 2 - c/2 = 1 - kappa = 0.5220552. For an unfair pair (p,q):
s = log2(p^2+q^2), m = q^2/(p^2+q^2), G(p,q) = kappa (s - 2) + c m - h(m). psi := max_t (h(t) - c t) = log2(1+2^{-c}).
Facts on G (code: inline table in this session; verify_rho23.py recomputes with intervals):
 (G1) G >= kappa (s-2) - psi; for s >= log2 10 the ratio (kappa(s-2) - psi)/(s-1) increases with s, so
      G >= GB (s - 1) with GB := (kappa(log2 10 - 2) - psi)/(log2 10 - 1) = 0.1967827.
 (G2) The only coprime pairs with s < log2 10 are (1,1) (fair) and (2,1); G(2,1) = 0.0231137 = GA (s-1),
      GA = 0.0174848, s(2,1) - 1 = SA := log2 5 - 1. Exact: G(3,1) = 0.4584020 (the minimum over odd-odd pairs
      is >= kappa(log2 10 - 2) - psi = 0.456918).

### 5.1 Exact reduction
For a row T with w_T > 0 put e_T = L_T + H(q_T) - c(|T| + I(q_T)); then H - cI = sum_T w_T e_T. By Lemma 3(c),
with f_T fair and u_T unfair active coordinates, e_T <= ebar_T := 2 - 2 log2 nu'_T + delta f_T
+ sum_unf (Ft_i - c m_i) - c|T| (alpha_i >= m_i and D1 only lower e_T). Using L_T = 2 + f_T - sum_unf (s_i - 2)
- 2 log2 nu'_T (Lemma 3b) to eliminate f_T:
      ebar_T = delta L_T + 2 kappa (1 - log2 nu'_T) - sum_unf G_i - c|T|.                         (5.1)
Write Phi = sum_T w_T ebar_T >= H - cI. It suffices to show Phi <= 0.
Trivial cases: if only one row is present, f = chi_T(y) g(x) with g Boolean and product spectrum, so H <= 2I by
product rigidity (RIG Th.1, Cor.1.1; KNOWN). If E_* is the whole cube, every row is (1/2) sigma_T with sigma_T
Boolean and product, so H = 2 + (1/4) sum H(sigma_T) <= 2(1 + (1/4) sum I(sigma_T)) = 2I.

### 5.2 Scenario A (E_* empty: every row {0,+-1}-valued). Phi < 0.
Here nu'_T is even and 2 log2 nu'_T >= e_c + 2 (Lemma 6). Write ebar_T = delta L_T - P_T - c|T| with
P_T = 2 kappa (log2 nu'_T - 1) + sum G_i >= 0 (G_i >= 0 for every pair: G(2,1) > 0 and (G1) otherwise).
So Phi <= delta H(w) - c Inf_A - w_0 P_0. Claim: if w_0 < 1 then P_0 >= 0.4569 (1 - L_0)_+.
 u_0 = 0: f_0 = L_0 - 2 + 2 log2 nu'_0 >= L_0 is a nonnegative integer and P_0 = kappa (f_0 - L_0); for
   L_0 in (0,1) this forces f_0 >= 1, so P_0 >= kappa (1 - L_0).
 u_0 >= 1: P_0 >= kappa e_c + sum G_i = sum_i (kappa o_i + G_i) (o_i = 1 for odd p^2+q^2); each term is
   >= min(kappa + G(2,1), kappa, kappa(log2 10 - 2) - psi) = 0.456918, so P_0 >= 0.4569.
With eps = 1 - w_0 and the Gibbs bound over the conditional address law on {1,2,12},
 delta H(w) - c Inf_A <= delta h(eps) - K eps,  K = -delta log2(2^{1-c/delta} + 2^{-2c/delta}) = 2.42643.
 eps >= 1/2: delta h(eps) - K eps <= delta - K/2 < 0.
 eps <= 0.45: delta h(eps) - K eps <= delta log2(1 + 2^{-K/delta}) = 0.029464, while
   0.4569 (1-eps)(1 + log2(1-eps)) >= 0.4569 * 0.55 * (1 + log2 0.55) = 0.03455 (the left factor decreases in eps).
 0.45 <= eps <= 1/2: delta h(eps) - K eps <= delta - 0.45 K < 0.
In all cases Phi < 0.

### 5.3 Scenario B, structure. E_* nonempty, not the whole cube. Then all four rows are present and half-valued;
rho = |R_cap| >= 1 (rho = 0 would make E_* the whole cube); e = base size of E_* (odd or even); w_T >= e 2^{-rho-2}
and so w_T <= 1 - 3 e 2^{-rho-2}. Odd-class rows are exactly the rows with r_T = rho when e is odd; they have
nu' odd and only odd-odd pairs, and w = N 2^{-rho-2} with N = nu'^2 prod n_i, n_i = (p_i^2+q_i^2)/2 >= 5.
Even rows have nu' even, 2 v2(nu') >= e_c, and r_T >= rmin (rmin = rho + 1 if e odd, rho if e even).

### 5.4 Envelopes (any rho >= 1).
 (Odd) For an odd row, f = rho - u gives sum_unf (s_i - 1) = rho + 2 - L - 2 log2 nu' and, by (G1),
   ebar <= a L - GB rho + (2 kappa - 2 GB) - c t,   a := delta + GB = 0.7188379.
 (Even) For an even row with nu' = 2^j o (o odd): r >= rmin gives sum_unf (s_i - 1) >= X_j := rmin + 2 - L - 2 log2 nu';
   the pairs (2,1) have odd norm and number at most e_c <= 2j, so by (G1)-(G2) and an LP bound,
   sum G >= Gmin(X_j, 2j), Gmin(X,E) = GA min(X, SA E) + GB (X - SA E)_+  (X_+ in place of X).
   An odd factor o costs 2 kappa log2 o and saves at most 2 GB log2 o < 2 kappa log2 o, so
   ebar <= Eeven_t(L) := delta L + max_{j>=1} [2 kappa (1-j) - Gmin((rmin + 2 - L - 2j)_+, 2j)] - c t.
   From Gmin(X,E) >= GB X - (GB-GA) SA E and 2 GB - 2 kappa + 2 (GB-GA) SA = -0.0882864 < 0 (maximum at j = 1):
   Eeven_t(L) <= a L - GB rho + 0.474039 - c t   (using rmin >= rho).
 Hence every row satisfies ebar_T <= a L_T - GB rho + K0 - c|T|, K0 = 2 kappa - 2 GB = 0.562325.

### 5.5 rho >= 4 (tail, analytic). Summing, Phi <= a H(w) - c Inf_A - GB rho + K0
 <= 2 a log2(1 + 2^{-c/a}) - GB rho + K0 = 0.116664 + 0.562325 - 0.196783 rho < 0 for rho >= 4.

### 5.6 rho in {2,3} (computer-assisted, rigorous intervals: code/verify_rho23.py, mpmath.iv at 40 digits).
Since sum_T w_T = 1, for any mu: Phi = mu + sum_T w_T (ebar_T - mu) <= mu + M_0 + 2 M_1 + M_2,
M_t = max( max over the finitely many odd rows of w (ebar_t - mu) [exact (5.1), N <= 2^{rho+2} - 3],
           sup_{L in [Lmin, Lmax]} 2^{-L} (Eeven_t(L) - mu) ),  Lmin = -log2(1 - 3 e_min 2^{-rho-2}),
           Lmax = rho + 2 - log2 e_min (e_min = 1 for e odd, 2 for e even).
The sup over L is bounded by 4000 interval pieces. Certified upper bounds (all < 0):
   rho=2 e odd (mu=-1.7668): -0.087204    rho=2 e even (mu=-1.7058): -0.683607
   rho=3 e odd (mu=-1.4779): -0.044105    rho=3 e even (mu=-1.4921): -0.266383
   (cross-checks of 5.5: rho=4: -0.371986 / -0.314275; rho=5: -0.349841 / -0.451507).

### 5.7 rho = 1 (structural; this is where AND_3 lives). If e = 2 then E_* is the whole cube (5.1). Let e = 1:
R_cap = {j}, E_* = {x_j = a0}, w_T = 1/8 + mu(E_T) with sum_T mu(E_T) = 1/2, every w_T in [1/8, 5/8].
Odd rows have r = 1 and N <= 5: fair (w = 1/8, |g| = (1/2) 1_{E_*}) or (3,1) (w = 5/8).
 (i) Some row T0 is (3,1). Then mu(E_T0) = 1/2, so the other three rows vanish off E_*:
   g_T = (1/2)1_{x_j = a0} sigma(x_{-j}) = (1/4)(1 + a0 x_j) sigma(x_{-j}), sigma Boolean with product law
   (tensor factor), so by product rigidity H(sigma) <= 2 I(sigma), and e_T <= 4 - c(|T| + 1/2) exactly.
   e_T0 <= log2(8/5) + h(1/10) - c(|T0| + 1/10). If T0 = empty the bound is exactly
   H(AND_3) - c I(AND_3) = 0. If T0 != empty, swapping the roles of T0 and empty lowers the bound by c|T0|/2.
 (ii) No (3,1) row: odd rows are fair with w = 1/8 and ebar = 3 delta + 2 kappa - c t = 2.52206 - c t; even rows
   satisfy ebar <= delta L - c t <= 3 delta - c t. If the empty row is odd: Phi <= 2.52206/8 - (c - 3 delta)(5/8)
   = 0.3153 - 0.8687 < 0 (at most three odd rows, so even weight >= 5/8, all at |T| >= 1). If the empty row is
   even: w_0 delta L_0 <= delta/(e ln 2) = 0.27705, and the rows {1},{2},{12} (each >= 1/8) contribute at most
   -0.43383 (w_1 + w_2) - 3.38972 w_12 <= -0.5321; Phi < 0.

Conclusion: Phi <= 0 in every case, with equality only in 5.7(i) with T0 = empty, alpha on the small side,
D1 empty and every sigma constant. QED (computer-assisted only in 5.6, and only through rigorous interval bounds).

### 5.8 Checks of the proof itself
- code/check_phi.py: on ~98,000 sampled K2 functions (|C| = 3: 10,300; |C| = 4: 87,446) the chain
  H - c*I <= Phi <= 0 holds with Phi computed from each row's exact (nu', p_i, q_i): max (H - c*I) - Phi = 9e-16,
  max Phi = 0 (attained by AND_3-type functions).
- code/verify_sensitivity.py: the same interval certificate, recomputed with c = 2.90 (below the rho = 3 relaxation
  value 2.914374), FAILS (+0.01729 at the best mu of a grid), and passes at c = 2.92 (-0.00521). So the check can
  fail on exactly the axis that matters; it is not vacuous.
- code/verify_constants.py: every numeric constant used in the analytic steps (Lemma E cases, 5.2 constants K,
  0.029464 vs 0.03455, 0.4569, 5.4 j-coefficient -0.0883 and the even constant 0.4740 <= K0, 5.5 tail value at
  rho = 4 = -0.108200..., 5.7 bounds, and H(AND_3) - c* I(AND_3) = 0) re-evaluated with 40-digit intervals: all PASS.
  The rho in {2,3} certificates with K = 20000 pieces: -0.087636, -0.044105 (e odd), -0.683789, -0.266855 (e even).
- Strongest case that the theorem is wrong, and why it does not apply: (a) a K2 function whose rows violate a
  relaxation constraint - every constraint is proved (Lemmas 1-6) and was also checked on sampled functions;
  (b) an error in the envelope for even rows (5.4) - the envelope only uses (G1), (G2) and Lemma 6, each proved,
  and the full row-type relaxation without envelopes (relax.py, lagr.py) gives the same or smaller values;
  (c) an implementation error in verify_rho23.py - its float twin (envelope.py) and the exact-row Lagrangian
  (lagr.py, bounded parameters) agree (-0.0877 / -0.0441 vs -0.0872 / -0.0441), and the sensitivity test fails
  where it should.

### 5.9 The k-address hierarchy (context for the fleet)
Let C_k = sup H/I over Boolean f having an address set of size <= k with all conditional laws product. Adding an
address keeps conditional laws product, so C_k is nondecreasing. With |C| = 1 every law is product, so K_k contains
every Boolean function on k+1 variables, and sup_k C_k = C_FEI (the optimal FEI constant). Known values:
C_0 = C_1 = 2 (product rigidity; ONE Th. 2.1), C_2 = c* = H/I(AND_3) (Theorem S). Lemma 3 holds verbatim for k
addresses with rows in 2^{1-k} Z (a sum of 2^k signs is even), unit 2^{1-k-r} and identity
L_T + H(q_T) = 2(k-1) - 2 log2 nu'_T + sum_i Ft(p_i,q_i).
Evidence for k = 3 (code/k3_n5.py, data/k3_n5.json): exhaustive at n = 5 (|C| = 2; fiber at x = 0 reduced by
y-translations, y-permutations, negation; 2,634,528 functions) gives max H/I = 3.402475551 = H/I(AND_4); the
maximum over all 4-variable functions is the same value. Pattern so far: C_k = H/I(AND_{k+1}) for k = 1, 2 (proved)
and k = 3 (evidence). H/I(AND_n) -> 4 while the FEI constant is known to exceed 6 (the math brain records a lower bound 6.5218;
not re-checked here), so the pattern must break at
some k; locating the first break is a concrete search target.

## 6. Literature and novelty
Web search was unavailable in this session (the session's search budget was exhausted), so no external novelty
check was done. Within the campaign sources: product rigidity (zero addresses) is prior campaign work (RIG Th.1,
RM 9.1, cited as Sept 21); the one-address constant 2 is ONE Th. 2.1; the two-address class, X008 and the open
target C022 are campaign-internal. The value H/I(AND_3) = 16/3 - (3/2) log2 3 is an elementary computation. Theorem A,
Lemma 3 (the minimal-coefficient identity), Theorem S and Corollary A' are, as far as these sources show, new here;
publication priority is unverified.

## 7. Final summary for the fleet
Results (statuses as in CLAIMS.json):
- PROVED: H <= 4I on K2 (Theorem A, short analytic proof).
- PROVED (one rigorous interval-arithmetic step): the optimal constant on K2 is c* = 16/3 - (3/2) log2 3 = 2.9558896,
  attained by AND_3 (Theorem S). This closes C022 with the sharp value; C031's refutation of 2 is subsumed (X008's
  40/17 is not extremal).
- PROVED: signed-character selectors with product rows, any number of addresses: H <= 4 (I - Inf_y), sharp.
- EVIDENCE: exhaustive K2 for n <= 6; K_3 at n = 5 tops out at H/I(AND_4) = 3.402475551.
How the proof pays the address entropy: the address entropy L_T of a product row is not paid by influence directly;
Lemma 3 shows L_T + H(q_T) = 2 - 2 log2 nu'_T + sum Ft, i.e. it is paid by how far the row's smallest Walsh coefficient
sits above the dyadic granularity. Only fair coordinates have Ft/m = 4; the free "+2" (nu' = 1) exists only for rows
of odd class, which forces 2-bit bent fibers on a cylinder E_*, and those fibers carry address influence. The three
ingredients (exact row identity, pointwise fiber classification, Lagrangian over rows with sum w = 1 plus envelopes)
are a template for the next rung.

SINGLE MOST PROMISING NEXT STEP: prove C_3 = H/I(AND_4) = 3.4024756 for three spectral addresses with the same
template. Lemma 3 already holds with additive term 2(k-1) - 2 log2 nu' (k = 3); what is needed is (i) the classification
of 3-bit fibers by the 2-adic pattern of their Walsh coefficients (replacing Lemma 1/Lemma 5: which rows can have
nu' < 2^{k-1} and where), (ii) the analogue of the weight lower bound w_T >= mu(E)/4, and (iii) envelopes plus an
interval certificate for the finitely many small cases. Since K_k increases with k and sup_k C_k = C_FEI, this ladder
reaches full FEI; the first k where C_k exceeds H/I(AND_{k+1}) (which tends to 4, below the known FEI lower bounds,
above 6) will exhibit the first extremal structure beyond one-point functions, which both the upper-bound and the
lower-bound programmes need.
