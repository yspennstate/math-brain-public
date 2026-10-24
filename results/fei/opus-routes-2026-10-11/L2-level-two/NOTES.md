# Route L2: the B-gap at level two and above (recovery stream s07, claude-6bb7036b-s07, 12 Oct 2026)

Full FEI is OPEN. Labels: PROVED (complete proof written here or verified line by line), CANDIDATE, REFUTED.
Every PROVED item below was written and checked in this stream (section 9 is this stream's own pass); until another
agent's adversarial pass it counts as a CANDIDATE for the campaign, and CLAIMS.json lists it that way. Sections 1 and 6
are this stream's checks of other agents' results (A096, B13).

## 0. Object
p(S) = fhat(S)^2 for Boolean f: {-1,1}^n -> {-1,1}; eps_i = Inf_i(f); I = sum_i eps_i.
phi(a,b) = (a+b) h2(b/(a+b)), phi(a,0) = phi(0,b) = 0, logs base 2, ln natural.
B(f) = sum over hypercube edges (U, U+i) of phi(p(U), p(U+i)) = sum_i H(S_i | S_-i), S ~ p.
B_k = edges with |U| = k. B_0 = root pairs (paid, 1.7501 I = 2/(sqrt(e) ln 2), B20). B_1 = A096's T12.
FEI <=> B <= K I for all Boolean f (campaign C018; uses J_i <= B_i, B13).
Per coordinate i and level j >= 0:
  B^(i)_j = sum_{|U| = j, i notin U} phi(p(U), p(U+i))      (direction-i edges at level j; B_j = sum_i B^(i)_j)
  d_{j,i} = sum_{|U| = j, i notin U} p(U+i) = W_j(D_i f)    (level-j weight of the derivative)
  a_{j,i} = sum_{|U| = j, i notin U} p(U)
  sum_j d_{j,i} = eps_i, sum_i d_{j,i} = (j+1) W_{j+1}, psi(x) = x log(e/x) (increasing on [0,1]).

## 1. Level one-to-two: A096 stage 2 (run 20261011T234252Z) -- independent referee verdict CONFIRMED (s07, by hand)
Claim: H2 := sum_{i<j} p(ij) log(1/p(ij)) <= K2 I, K2 = 8/(e^2 ln2) + 2/e + sqrt2/(e ln2) = 3.0484 (< 155600/50301);
       B_1 = T12 <= (2 K2 + 1/ln2) I = 7.540 I (< 16700/2187).
Checked: (1) h_i = D_i f in {0,+-1}, L_i its level-1 part, d_i = E L_i^2 = E h_i L_i <= eps_i E[|L_i| | h_i != 0];
Hoeffding + conditional Jensen give d_i <= 2 eps_i^2 ln(2/eps_i). (2) Q({i,j}) = 2 eps_i eps_j / I^2 has total
1 - sum eps_i^2/I^2 <= 1 and is positive on supp p (fhat(ij) != 0 forces eps_i, eps_j > 0); Gibbs with a
sub-probability reference is valid; the pair-endpoint terms regroup exactly into sum_i d_i log(1/eps_i).
(3) sup t^2 e^-t = 4/e^2, sup t e^-t = 1/e. (4) ln z <= 2 sqrt(z)/e, W2 <= 1. (6) phi(x,y) <= y log(1/y) + y/ln2
when x + y <= 1; each unordered pair appears twice in T12; 2 W2 <= I. (7) Rationals: e > 27/10, ln2 > 69/100,
sqrt2 < 71/50; 2(155600/50301) + 100/69 = 384100/50301 = 16700/2187 exactly, strict inequalities hold.
Numerical replication: section 7 (0 violations of the level-1 lemma, of H2 <= K2 I and of T12 <= 7.540 I).
As a constant it is superseded by Theorem 3 below: B_1 <= 3.578 I.

## 2. Literature: KKLMS Theorem 1.3 covers every fixed level of B (PROVED as a corollary; constant not explicit)
Kelman-Kindler-Lifshitz-Minzer-Safra, arXiv:1911.10579v2, Thm 1.3 (read 12 Oct 2026 from the v2 PDF, p. 3):
  H[g^{<=D}] <= K sum_{|S|<=D} |S| log(|S|+1) ghat(S)^2 + K I[g], absolute K, for g: {0,1}^n -> {0,1}.
KKLMS define I_i[g] as the probability that g changes when bit i flips (p. 1), and also write I[g] = sum |S| ghat(S)^2.
Transfer to +-1 functions (PROVED): put g = (1 - f)/2. Then ghat(S)^2 = p(S)/4 for S nonempty and g changes exactly when f
does, so under either reading I[g] <= I(f). The empty set's term is nonnegative and (p/4) log(4/p) >= (1/4) p log(1/p), so
  sum_{0<|S|<=D} p(S) log(1/p(S)) <= 4 H[g^{<=D}] <= K sum_{|S|<=D} |S| log(|S|+1) p(S) + 4K I(f).
Elementary: phi(a,b) <= b log(e/b) when a + b <= 1, so B_k <= sum_{|T|=k+1} |T| p(T) log(e/p(T)).
Hence B_{<D} := sum_{k<D} B_k <= D sum_{0<|T|<=D} p log(1/p) + (log e) I <= (4K D (1 + log(D+1)) + log e) I.
So no family can make B_1/I (or any fixed-level ratio) diverge. Campaign files (B20 SYNTHESIS route 1, U route)
cite KKLMS but never apply Thm 1.3 to the levels of B (Grep of FEI100, mop_fei100, fei_opus, 12 Oct).
Theorem 3 below makes the fixed-level statement explicit and self-contained.

## 3. Per-coordinate level bound and per-level theorem (PROVED; numeric constants certified in 3.6)

Lemma 1 (PROVED). For every coordinate i and level j,
  B^(i)_j <= phi(a_{j,i}, d_{j,i}) <= d_{j,i} log(e (a_{j,i} + d_{j,i}) / d_{j,i}) <= psi(d_{j,i}).
Proof. phi is the perspective (a+b) h2(b/(a+b)) of the concave function h2, so it is jointly concave and positively
homogeneous of degree one on [0,inf)^2; such a function is superadditive, phi(x + y) >= phi(x) + phi(y). Summing over the
edges of direction i at level j gives the first inequality. Next phi(a,d) = a log(1 + d/a) + d log((a+d)/d) and
a log(1 + d/a) <= d log e (ln(1+x) <= x), which gives the second. Finally the sets U and U+i (|U| = j, i notin U) are
pairwise distinct, so a_{j,i} + d_{j,i} <= sum_S p(S) = 1. QED.
Sharpness: B^(i)_j / psi(d_{j,i}) reaches 0.99971 (AND on 10 variables, level 0); B^(i)_j / phi(a,d) reaches 1 (a level
holding one edge). Checked on 68,148 and 68,078 functions with no violation (section 7).
Meaning: summing the first inequality over j gives
  B_i = H(S_i | S - i) <= sum_j phi(a_{j,i}, d_{j,i}) = H(S_i | |S - i|),   S ~ p.
A level method is exactly a method that conditions on the size of the rest of the set instead of the rest of the set.

Lemma 2 (derivative level weights; PROVED). Let h = D_i f, so h is {0,+-1}-valued, E h^2 = eps_i, d_{j,i} = W_j(h).
 (a) d_{0,i} = fhat(i)^2 <= eps_i^2, since fhat(i) = E h and |E h| <= P(h != 0) = eps_i.
 (b) d_{1,i} <= 2 eps_i^2 ln(2/eps_i) (A096 stage 1, checked in section 1).
 (c) d_{j,i} <= eps_i^{2 - 2/q} (q-1)^j for every q >= 2: W_j(h) = <h, h^{=j}> <= ||h||_{q'} ||h^{=j}||_q and Bonami gives
     ||h^{=j}||_q <= (q-1)^{j/2} W_j(h)^{1/2}, while ||h||_{q'} = eps_i^{1/q'} because |h| is an indicator.
 (d) d_{j,i} <= eps_i.
Let rho_k(eps) be the resulting bound on d_{k-1,i}/eps_i, capped at 1: rho_1 = eps, rho_2 = min(1, 2 eps ln(2/eps),
inf_q eps^{1-2/q} (q-1)), and rho_k = min(1, inf_{q>=2} eps^{1-2/q} (q-1)^{k-1}) for k >= 3.

Theorem 3 (per-level bound; PROVED). For every k >= 1 and every Boolean f, B_{k-1} <= b_k I, where
  b_k = sup_{0 < eps <= 1} g_k(eps),   g_k(eps) = rho_k log(e/rho_k) + rho_k log(1/eps),   rho_k = rho_k(eps).
Proof. B_{k-1} = sum_i B^(i)_{k-1} <= sum_i psi(d_{k-1,i}) (Lemma 1) <= sum_i psi(eps_i rho_k(eps_i)) (psi increasing,
d_{k-1,i} <= eps_i rho_k(eps_i) <= 1) = sum_i eps_i g_k(eps_i) <= b_k I. QED.
Constants:
 - b_1 = 2/(sqrt(e) ln 2) = 1.750078 exactly (maximiser eps = e^{-1/2}); this is B20's root constant.
 - b_2 <= 3.5777 (certified, 3.6; level-one branch, maximiser eps = 0.19303; the Bonami branch alone gives 4.5281).
   A096's T12 <= 7.540 I becomes B_1 <= 3.5777 I, a factor 2.1.
 - certified (3.6): b_3 <= 7.3278, b_4 <= 10.1773, b_5 <= 13.0437, b_6 <= 15.9174, b_7 <= 18.795, b_8 <= 21.6747,
   b_9 <= 24.5559, b_10 <= 27.4379. Grid values only (not certified): b_20 = 56.278, b_40 = 113.98. Maximiser near
   ln(1/eps) = 2k - 1.8; b_k/k decreases towards 2.885.
 - Analytic for every k >= 2: b_k <= 2k log e = 2.8854 k. Proof: with s = 1/(k-1), q = 2 + s and L = ln(1/eps),
   rho_k <= e^{-L s/(2+s)} (1+s)^{k-1}, so rho_k L <= ((2+s)/(s e)) (1+s)^{k-1} <= 2k - 1, by sup_L L e^{-aL} = 1/(ae) and
   (1 + 1/(k-1))^{k-1} <= e. Also x(1 + ln(1/x)) <= 1 on (0,1]. Hence (ln 2) g_k = rho(1 + ln(1/rho)) + rho L <= 2k.
   For k = 1, b_1 < 2 log e. QED.
Corollary 4 (PROVED). B_{<D} <= log(e) D (D+1) I = 1.4427 D(D+1) I for every D >= 1, with explicit sums
sum_{k<=D} b_k <= 5.3278 (D=2), 12.6556 (D=3), 35.8766 (D=5), 144.2575 (D=10), from the certified b_k.
Compare: section 2 gives O(D log D) with an unspecified constant; O1 below shows that any f-independent per-level
constants must satisfy c_k >= (2k/(k+1)) C(2k,k) 4^{-k} ~ 1.128/sqrt(k), so their sum diverges.
Superseded: the in-session candidate H3 <= 7.987 I, B_2 <= 25.41 I (never published; check_levels tested the slightly
stricter 7.985 and 25.40, with no violation). Theorem 3 gives B_2 <= 7.33 I.

### 3.6 Certificate for the numeric constants
Done 12 Oct 16:2x (code/certify_constants.py, data/certify_constants.json, logs data/certify_constants*.log); all 14 constants
certified. Each constant is sup_L F(L), L = ln(1/eps), F(L) = sum_j t(rho_j(L), L) with t(r, L) = r(1 + ln(1/r) + L)/ln 2
(eps t(rho, L) = psi(rho eps)). Every rho bound used is non-increasing in L (e^{-L}; min(1, 2e^{-L}(L + ln 2)), which is 1 for
L < 1.47 and decreasing after; the Bonami bound with any fixed q), and t increases in r on (0,1] and in L. So on a cell
[La, Lb), t(rho_j(L), L) <= t(rbar_j, Lb) with rbar_j = min(1, bound_j at La); for localized sums a level j that enters inside
the cell (at L = j/c) is evaluated at a rigorous lower bound for j/c. The Bonami q is chosen per cell by the closed form
q - 1 = ((L - j) + sqrt(L(L - 2j)))/j (any q is valid, so this choice needs no proof). Cells are bisected in float64 until
below a decimal target (grid maximum + 2e-5, rounded up to 4 places); then every final cell is re-evaluated in mpmath
interval arithmetic (80-bit, outward rounding) and compared with the target rounded down. Tails L >= Lmax: one fixed q,
closed forms decreasing past an explicit point (b_k: q = 4, rho <= 3^j e^{-L/2}; C(c): q - 1 = ((1-c) + sqrt(1-2c))/c,
every term <= e^{-sL}, at most cL + 1 terms, (cL+1) e^{-sL}(1 + (1+s)L)/ln 2 decreasing for L >= 2/s).
  constant   certified   grid value   maximiser L = ln(1/eps)   cells   tail bound
  b_2        3.5777      3.577657     1.6449                     2883    3.7e-11
  b_3        7.3278      7.327698     4.2323                     2387    1.3e-11
  b_4        10.1773     10.177229    6.1614                     2416    1.4e-11
  b_5        13.0437     13.043622    8.1228                     2364    1.4e-11
  b_6        15.9174     15.917357    10.0989                    2496    1.5e-11
  b_7        18.795      18.794893    12.0827                    2291    1.5e-11
  b_8        21.6747     21.674640    14.0710                    2381    1.5e-11
  b_9        24.5559     24.555781    16.0622                    2262    1.6e-11
  b_10       27.4379     27.437859    18.0554                    2442    1.6e-11
  C(0.2)     1.7501      1.750078     0.5                        2691    8.0e-13
  C(0.3)     4.0782      4.078084     20/3                       1976    2.6e-16
  C(0.4)     13.8404     13.840290    35/2                       2270    9.3e-17
  C(0.45)    46.9287     46.928644    440/9                      2756    1.8e-17
(b_2 with the level-one branch alone gives the same 3.5777.) The certificate corrected two grid values: see 4 and 9.4.

## 4. Localization below half the log-influence (PROVED; constants numeric, certified in 3.6)

Theorem 5 (PROVED). For 0 <= c < 1/2 let C(c) = sup_{0<eps<=1} sum_{j=0}^{floor(c ln(1/eps))} g_{j+1}(eps).
Then C(c) < inf, and every Boolean f satisfies
  Loc_c(f) := sum_i sum_{0 <= j <= c ln(1/eps_i)} B^(i)_j <= C(c) I(f).
Proof. Termwise, as in Theorem 3: B^(i)_j <= psi(d_{j,i}) <= eps_i g_{j+1}(eps_i); sum over j <= c ln(1/eps_i) and i.
Finiteness: choose s > 0 with delta := s/(2+s) - c ln(1+s) > 0 (possible because s/(2+s) - c ln(1+s) = s(1/2 - c) + O(s^2)).
For j <= cL, L = ln(1/eps), Lemma 2(c) with q = 2 + s gives rho_{j+1} <= e^{-L s/(2+s)} (1+s)^j <= e^{-delta L}. As
x(1 + ln(1/x)) increases on (0,1], (ln 2) g_{j+1} <= e^{-delta L}(1 + delta L) + L e^{-delta L}, and there are at most
cL + 1 terms; (cL + 1) e^{-delta L} (1 + (1 + delta) L) is bounded on L >= 0. QED.
Values (certified, 3.6): C(0.1) <= C(0.2) <= 1.7501 (level 0 at eps = e^{-1/2}, equal to b_1), C(0.3) <= 4.0782,
C(0.4) <= 13.8404, C(0.45) <= 46.9287. The supremum sits exactly at an entry point L = m/c (20/3, 35/2, 440/9), where level m
joins the sum; the majorant drops just after it. The first grid values (4.0720, 13.844, 46.80, data/check_lemma1.json) missed
those points or used a q grid; they are superseded.
Observed Loc_c / I on the 68,148 test functions: 1.1725 for every c <= 0.3, 1.2695 at c = 0.4, 1.3029 at c = 0.45.

The threshold 1/2 is exact for Bonami (PROVED). For c >= 1/2 and every q = 2 + s > 2,
c ln(1+s) >= (1/2) ln(1+s) >= s/(2+s) (the inequality ln(1+s) >= 2s/(2+s)), so the bound of Lemma 2(c) at j = floor(cL) does
not decay in L; then g_{j+1} is of order log(1/eps) and C(c) = inf.
No level inequality for {0,+-1} functions can raise it (PROVED: Proposition 6 and Corollary 7). f = 1 - 2 1{#(-1) <= t} on
n = N + 1 bits has D_i f = -1{|y| = t}, a Hamming slice of density rho = t/N, with W_k(D_i f) = C(N,t)^2 K_k(t)^2 / (4^N C(N,k)),
K_k Krawtchouk.

Proposition 6 (level law of a slice). Let g = 1{|y| = t} on {-1,1}^N, eps = E g = C(N,t) 2^-N, lambda_k = W_k(g)/eps. If
t/N -> rho in (0,1), the law of k/N under lambda converges weakly to the arcsine law A_rho on [x_-, x_+],
x_+- = 1/2 +- sqrt(rho(1-rho)).
Proof. ghat(U) = 2^-N K_t(|U|), so lambda_k = w(k) p_t(k)^2 with w(k) = C(N,k) 2^-N and p_t = K_t / sqrt(C(N,t)), the t-th
orthonormal polynomial of the Binomial(N, 1/2) law. In the basis p_0, ..., p_N (complete in L^2(w)) multiplication by x is the
Jacobi matrix J with diagonal N/2 and off-diagonal entries a_n = (1/2) sqrt(n(N - n + 1)) (from (n+1)K_{n+1} = (N - 2x)K_n -
(N - n + 1)K_{n-1}; signs do not matter below). Hence int (x/N - 1/2)^m dlambda = <e_t, (J/N - 1/2)^m e_t>, a sum over the
closed walks of length m from t on {0..N}, each weighted by the product of a_n^2/N^2 over its edges (every edge is crossed an
even number of times). For t >= m and N - t >= m no walk reaches the ends, and a_n^2/N^2 -> rho(1-rho)/4 uniformly for
|n - t| <= m. So the moment tends to C(m, m/2) (rho(1-rho)/4)^{m/2} for m even and 0 for m odd: the central moments of the
arcsine law on [1/2 - 2a, 1/2 + 2a], a^2 = rho(1-rho)/4, which is the spectral measure at a site of the constant Jacobi matrix
on Z. All the laws live on [0,1], so convergence of moments is weak convergence. QED.
(The argument is the standard moment method for orthogonal polynomials with slowly varying recurrence coefficients; no
novelty is claimed for Proposition 6.)

Corollary 7. For every c > 1/2 there are rho in (0, 1/2) and mu > 0 such that, for f = 1 - 2 1{#(-1) <= rho N} on N + 1 bits
and all large N, every D_i f carries at least mu eps of its mass at levels <= c ln(1/eps). Then
sum_{j <= c ln(1/eps_i)} psi(d_{j,i}) >= mu eps_i log(1/eps_i) for every i, and the Lemma 1 majorant of Loc_c(f) is at least
mu I log(1/eps), with log(1/eps) of order N.
Proof. ln(1/eps) = N(ln 2 - H_e(t/N)) + O(ln N), so the levels k <= c ln(1/eps) are k/N <= c(ln 2 - H_e(rho)) + o(1). The arcsine
law has a continuous distribution function, so by Proposition 6 the mass there tends to A_rho([x_-, c(ln 2 - H_e(rho))]), which is
positive exactly when c > c_min(rho) := (1/2 - sqrt(rho(1-rho))) / (ln 2 - H_e(rho)). With rho = 1/2 - delta,
c_min = (1/2)(1 + delta^2/3 + O(delta^4)) -> 1/2, so some rho has c_min(rho) < c; take mu as half the limit. psi is concave with
psi(0) = 0, hence subadditive, and increasing on [0,1], so sum_j psi(d_j) >= psi(mu eps) >= mu eps log(1/eps). QED.
Values: c_min = 0.570, 0.519, 0.504, 0.5004 at rho = 0.05, 0.2, 0.35, 0.45. At rho = 0.2 the limit mass at c <= 0.55 is 0.0552;
the exact Krawtchouk masses (code/slice_levels.py) are 0.0836, 0.0733, 0.0610, 0.0603, 0.0581 for N = 200, 800, 2000, 4000, 8000,
while the mass at c <= 0.5 falls 0.0345, 0.0075, 0.0014, 0.00014, 2.7e-6 (limit 0). Two independent exact paths for the moments
(direct Krawtchouk sums, walks on the integer matrix similar to 2(J - N/2)) agree on all 20 cases; code/slice_limit.py,
data/slice_limit.json.
Remark. Theorem 5 forces the slice mass below c ln(1/eps) to vanish for c < 1/2, so c_min(rho) >= 1/2 for every rho, that is
ln 2 - H_e(rho) <= 1 - 2 sqrt(rho(1-rho)) (the grid minimum is 0.5000002, at rho = 0.499).
These f are symmetric, a class covered by O'Donnell-Wright-Zhou (2011); the limit is the method's, not FEI's.

Where the gap is. For eps_i >= tau, B_i <= H(S_i) = h2(eps_i) <= eps_i log(e/tau). With Theorem 5:
  B <= (log(e/tau) + C(c)) I + B_gap(tau, c),   B_gap(tau, c) := sum_{i: eps_i < tau} sum_{j > c ln(1/eps_i)} B^(i)_j,
and B_gap <= B. So for any fixed tau in (0,1) and c < 1/2, FEI is equivalent to B_gap(tau, c) = O(I): only direction-i
edges of low-influence coordinates, at levels above c ln(1/Inf_i), are unpaid. (B01's localization in
brain_workers/FEI100_20261011/claude/B01/STREAM_NOTES.md line 14 restricts coordinates by influence only, not levels.)

## 5. Obstructions (all PROVED by exact computation; data/obstruction_tables.json, obstruction_tables2.json)

O1. Per-level bounds cannot be summed. f = x0 * bent_m (m even, n = m + 1): p(T) = 2^-m for every T containing 0, so
B_k = C(m, k-1)(m - k + 1) 2^{1-m}, B = m, I = 1 + m/2. At m = 2k, B_k / I = (2k/(k+1)) C(2k,k) 4^-k ~ 2/sqrt(pi k).
Table: k = 1, 2, 5, 10, 100, 500 -> 0.5000, 0.5000, 0.4102, 0.3204, 0.1116, 0.0504; sqrt(k) B_k/I -> 1.1258 at k = 500
(2/sqrt(pi) = 1.1284). Any valid f-independent constants c_k with B_k <= c_k I therefore have sum_k c_k = inf; a proof of
B20 must couple levels. Truth for c_k lies between 1.128/sqrt(k) and 2.885(k+1) (Theorem 3).

O2. Level-local budgets fail at every level. A = {x : #(-1) <= t}, f = 1 - 2 1_A: delta = P[Bin(n,1/2) <= t],
p0 = (1-2 delta)^2, fhat({i}) = -pmf(t; n-1, 1/2), Inf_i = pmf, I = n pmf, B_0 = n phi(p0, pmf^2), Var = 4 delta(1-delta).
With t = n/2 - sqrt(n)/4 (bias fixed): B_0/Var = 3.40, 5.48, 7.54, 9.47 and B_0/W_1 = 5.63, 9.25, 12.97, 16.29 for
n = 101, 1001, 10001, 100001 (exact). So B_0 <= C Var and B_0 <= C W_1 are false. The shift f' = chi_R g (R disjoint from
g's variables) has B_r(f') = B_0(g) and W_{>r}(f') = Var(g), so B_r <= C W_{>r}, and likewise B_k <= C (k W_k + (k+1) W_{k+1}),
fail at every level r. (B_0 itself stays O(log I) and below 1.7501 I; these refute budgets, not B20.)

O3. The product-reference template fails. Gibbs with Q(S) proportional to prod_{i in S} eps_i, level by level, gives
H <= Phi := sum_i eps_i log(1/eps_i) + sum_k W_k log(I^k / (k! W_k)), the A096 engine at all levels. On f = product of
M = 2^{a-2} disjoint copies of AND_a (I = a/2, W_0 -> 1/e): Phi/I = 4.27, 6.08, 7.97, 9.91, 11.87, 13.84 and
H/I = 3.40, 3.74, 3.84, 3.88, 3.91, 3.92 for a = 4, 6, 8, 10, 12, 14. Phi/I = a - 1 + O(1) while H/I < 4. On majority the two
parts of Phi are each about +-(1/2) I log n and cancel, so they cannot be bounded separately either.

O4. Charging an edge to its upper endpoint loses the factor k + 1. On x0 * bent_m,
sum_T |T| p(T) log(e/p(T)) = (1 + m/2)(m + log e) against B = m. Lemma 1 charges per direction and level and avoids this.

O5. Level coarse-graining, the exact obstruction for this route. B_i = H(S_i | S - i) = h2(eps_i) - I(S_i ; S - i), so
  FEI  <=>  sum_i I(S_i ; S - i) >= sum_i h2(eps_i) - K I,
and every level method (Lemma 1, Theorems 3 and 5, any bound through the derivative level profiles) replaces S - i by its size:
B_i <= H(S_i | |S - i|) = h2(eps_i) - I(S_i ; |S - i|). On balanced tribes (width w, s = round(2^w ln 2) blocks), computed
exactly from the level distribution:
  w                        = 4     6     8     10     12     13
  sum_i H(S_i | |S-i|) / I = 5.05  7.26  9.33  11.35  13.35  14.34    (log(1/eps) + 1.34 asymptotically)
  sum_i h2(eps_i) / I      = 5.33  7.41  9.43  11.44  13.44  14.44
  H / I                    = 3.68  3.92  3.98  3.996  3.999  3.9995
The size of the rest of the set carries I(S_i ; |S-i|) of about 0.1 eps_i bits (D(lambda_i || mu_i) = 0.09-0.20), while
I(S_i ; S-i) >= h2(eps_i) - 4 eps_i, about eps_i (log(1/eps_i) - 2.6) bits. The mechanism: conditioning on i in S forces the
block of i to be active in S - i (ratio 1/(2 eps_i) on sets that meet the block), so D(nu_i || m_i) is about
log(1/P_p(S meets block(i))) = log(1/eps_i) - O(1), and the size of S - i does not see which block is active.
Unrefined Lemma 1 summed over levels gives log(1/eps) + 6 per unit influence on the same family (two independent
computations, derivative generating function and level distribution, agree to the printed digits).
Consequence: at high levels, B20 is a statement about which coordinates co-occur with i in S, not how many. A proof has to
use a statistic of S - i finer than its size; the natural candidates are coordinate-local witnesses (the W and SEL routes).
The other side (PROVED, closed form; code/witness_tribes.py, data/witness_tribes.json): on tribes one block is enough. With
W_i = S cap (block(i) - i), a function of S - i, B_i = H(S_i | S - i) <= H(S_i | W_i), and the closed spectrum
(p(S) = 4 prod_t (alpha or beta), alpha = (1 - 2^-w)^2, beta = 4^-w) gives
  H(S_i | W_i) = (2^{w-1} - 1) 2y + phi(Z, y),  y = eps_i / 2^{w-1},  Z = P(S misses block(i)),
so H(S_i | W_i)/eps_i <= 2 - 2^{2-w} + 2^{1-w} (log e + w - 1 + log(1/eps_i)), which is 2 + O(w 2^{-w}) on balanced tribes:
  w                           = 4      6      8      10     13     16     20
  sum_i H(S_i | W_i) / I      = 2.774  2.324  2.113  2.036  2.006  2.001  2.000
  sum_i H(S_i | |S-i|) / I    = 5.054  7.260  9.333  11.35  14.34  (log(1/eps) + 1.34)
  B / I                       = 2.323  2.144  2.053  2.018  2.003  2.001  2.000
The closed forms of B_i and H(S_i | W_i) equal brute-force truth-table values to ten digits on tribes (2,3), (3,3), (2,5),
(3,4), (4,3), (2,6). So the whole gap of O5 on this family is the difference between knowing how many coordinates of S - i
are present and knowing whether i's own block is.

## 5b. Read-once formulas: the branch witness is exact, a bounded witness is not (s07, 12 Oct)
Setting. f a read-once formula over arbitrary gates, uniform inputs. At a gate v whose children have means mu_j, write
P_v(J) = gtilde_v(J)^2 for the mu-biased spectral law of the gate (gtilde in the basis prod (y_j - mu_j)/sigma_j). The spectral
sample is generated top-down: the root picks J with P_root(J) (J = empty is S = empty); each active child recurses with its
own law divided by 1 - P_c(empty) = Var(f_c). This is the two-stage sample behind O'Donnell and Tan's composition theorem.
For a leaf i with path v_0 = root, ..., v_{d-1}, v_d = i and path children c_t: alpha_t = P(S meets sub(v_t)) =
prod_{s<t} P(c_s in J_s), and rho_{>t} = prod_{t<t'<d} P_{t'}({c_{t'}}) (normalized laws below the root).

Lemma R (PROVED). Let tau be the deepest path node whose subtree meets S - i, and A the set of off-path children of v_tau whose
subtrees meet S. The conditional law of S_i given S - i depends only on (tau, A), and
  B_i = H(S_i | S - i) = H(S_i | tau, A) = phi(mu^2, fhat(i)^2) + sum_t alpha_t sum_{A nonempty} phi(P_t(A), P_t(A + c_t) rho_{>t}).
Proof. Take U = S - i with tau = t and pattern A. U and U + i make the same choices above v_t (the path child is active at every
v_s, s < t, and the off-path subsets coincide); at v_t the masks are A and A + c_t; below c_t the set U + i continues with the
single leaf i, of normalized probability rho_{>t}. Hence p(U) = F G P_t(A) and p(U + i) = F G P_t(A + c_t) rho_{>t}, with F the
factor above v_t and G the factor inside A. phi is homogeneous of degree one, so the edge at U contributes
F G phi(P_t(A), P_t(A + c_t) rho_{>t}); F summed over the configurations above v_t is alpha_t, and G summed over the nonempty
subsets inside A is 1. U = empty gives phi(mu^2, fhat(i)^2). []
Corollary R1 (PROVED). The branch witness W_i = (tau, A), a function of S - i, has H(S_i | W_i) = B_i. So does any witness that
refines it, e.g. "the smallest path subtree that S - i meets, and S on that subtree's children". Tribes (section 5, after O5)
is the depth-two case. The height-s witness W^(s) = S cap (sub(v_s) - i) sees (tau, A) exactly when tau >= s, so
  H(S_i | W^(s)) = sum_{t >= s} alpha_t sum_A phi(...) + phi(Z_s, y_s),  Z_s = 1 - alpha_s (s >= 1),  y_s = P(S cap sub(v_s) = {i}),
and its excess over B_i is at most phi(Z_s, y_s), about y_s log(e/y_s): the price of i being alone in its cell.

Checks (code/readonce_witness.py; data/readonce_witness.json, .log). B_i, H(S_i | |S - i|), eps_i, every height-s witness
cost and H equal brute-force Walsh transforms on seven trees (AND/OR depth 2-4, AND3/OR2, tribes 3x3, a 2-3-2 mixed tree;
n <= 16) to 4e-14. The symmetric families use closed-form gate laws (AND: gtilde(J)^2 = 4 q^2 prod_{j in J} qb_j/q_j; OR:
4 qb^2 prod_{j in J} q_j/qb_j; q = P(true) and qb = P(false) both carried), checked against the generic 2^k expansion in
80-digit arithmetic on 40 (family, depth) pairs to relative 4e-13; the AND-on-top and OR-on-top families agree to every
printed digit, as duality requires.

Evidence (EVIDENCE; fan-in 2 alternating AND/OR trees, I = n eps by symmetry; the AND2/OR3 family behaves the same way, each
parity of depth separately):
  d                        = 2      4      6      8      10     12     14     16     18     20     22
  log2(1/eps)              = 1.42   2.91   4.63   6.85   10.21  15.89  26.25  45.98  84.43  160.3  311.1
  B / I                    = 1.782  3.216  3.655  3.689  3.664  3.656  3.6557 3.6557 3.6557 3.6557 3.6557
  H / I                    = 2.217  3.684  4.592  5.078  5.271  5.319  5.332  5.339  5.342  5.343  5.344
  sum_i H(S_i||S-i|) / I   = 2.090  4.238  5.662  6.801  7.877  8.923  9.946  10.956  (computed for n <= 65536)
  smallest h with cost_h <= B + I: 4, 5, 6, 7, 7, 9, 9 at d = 10, 12, ..., 22; that cell has 2^h = 1.5 to 3.2 log2(1/eps) leaves.
  (cost_h - B) / (I log2(1/eps)) at d = 22: 0.495, 0.162, 0.045, 0.009 for h = 1, 3, 5, 7 (converged in d at every h).
Reading. (1) The level statistic fails here too, more slowly than on tribes: its excess over B grows by 1.00 per two levels
(increments 1.08, 1.04, 1.03, 1.01 from d = 8 to 16) while log2(1/eps) grows by a factor tending to 2 per two levels, so it is
unbounded and of order log log(1/eps), against log(1/eps) on tribes (O5). (2) No witness of bounded size works: at every fixed
height the excess is (kappa_h + o(1)) eps_i log2(1/eps_i) with kappa_h > 0, roughly 2^-h, i.e. the chance that i is alone in a
cell of 2^h leaves given i in S. The excess drops below I once the cell holds a few times log2(1/eps_i) coordinates, the same
scale as the block of tribes. The witness asked for in SYNTHESIS section 3 therefore has to be multi-scale: nested cells around
i, with the relevant cell size adapting to eps_i, about log(1/eps_i) coordinates. (3) Read-once formulas over bounded-arity gates
are a covered class (O'Donnell-Tan composition theorem, ICALP 2013, as credited by Chakraborty-Kulkarni-Lokam-Saurabh, TCS
2016); nothing here is new about FEI on them, and Lemma R is the composition structure written for B_i. (4) W-E5 quotes H/I =
2.23 (d = 2), 3.66 (d = 4), 5.29 (d = 12); the exact values are 2.2169, 3.6842, 5.3190, and the W referee's own exact script
(W-witness-cost/referee_code/check_andor.py) prints 2.2169, 3.6125, 3.6842 for d = 2, 3, 4, so the quoted figures, not the
code, are off. The qualitative W-E5 statement (H/I levels off near 5.3) stands; the limit is about 5.345.

## 5c. Which statistic of S - i is enough: a brute-force map (s07, 12 Oct; EVIDENCE, except Corollary R2)
Corollary R2 (PROVED). If every gate of a read-once formula is an AND, an OR or a parity of literals, of any fan-in, then
B_i = H(S_i | tau_i), where tau_i is the height of the lowest ancestor of i whose subtree meets S - i (tau_i = none when
S - i is empty). So one integer, the height at which S - i first reaches the branch of i, is an exact witness.
Proof. With q, qb the output probabilities of a gate and q_j, qb_j those of its children, the AND law is
P(J) = 4 q^2 prod_{j in J} qb_j/q_j and the OR law P(J) = 4 qb^2 prod_{j in J} q_j/qb_j (J nonempty); with mu_j, sigma_j the
children's means and deviations, the parity law is P(J) = prod_{j notin J} mu_j^2 prod_{j in J} sigma_j^2. So
P_t(A + c_t) = r_t P_t(A) with r_t free of A; below the root the normalization is a common factor. Each term of Lemma R is
then sum_A P_t(A) phi(1, r_t rho_{>t}) = phi(sum_A P_t(A), r_t rho_{>t} sum_A P_t(A)) by 1-homogeneity, and alpha_t times
this is the cost of the cell {tau_i = t} with A forgotten. Summing over t and adding the cell tau_i = none gives
H(S_i | tau_i) = H(S_i | tau_i, A) = B_i. A majority gate has no product form, and there the statement fails.
Check (code/audit_general_witness.py, data/audit_general_witness.log): H(S_i | tau_i)/I = B/I to 4e-16 on the AND/OR trees
of depth 3 and 4, AND2-OR3-AND2, OR2-XOR3-AND2 and XOR2-AND3-OR2 (parity gates with biased inputs); the same tau_i costs
1.38 I above B on OR3 of MAJ3 and 0.075 I on MAJ3 of AND4.

The bench (code/general_witness.py, data/general_witness.json, data/general_witness.log). For each i the other coordinates
are ordered by co-occurrence c_ij = P(S contains i and j) and grouped into classes of equal c_ij. Witnesses: the level
|S - i|; first, the rank of the nearest element of S - i in that order; eq+lev, the first class that S - i meets, its
pattern there (at most 2 log2(1/eps_i) coordinates shown) and |S - i|; the count profile, |S cap class| for every class;
geometric shells and cells of the c log2(1/eps_i) nearest coordinates as controls. 34 structured functions (tribes,
majority, Hamming balls, x0 times bent, AND/OR trees, recursive majority, ORs of majorities, MAJ3 of ANDs, the address
function, AND2-OR3-AND2, two weighted thresholds, the falsifiers X002, X003, X009) and 9 generic ones (six random DNFs on
12 variables, three random tables on 10), n = 6 to 16. B and I were recomputed on eight of them by an explicit Hadamard
product (equal to the ten printed digits), and the AND/OR rows equal section 5b's data to 1e-15.
Findings.
(i) eq+lev costs exactly B (to 2e-15) on 27 of the 28 structured functions outside the X-family; on that family it is
exact on X002 and within 0.027 I of B on X003 and X009. The exception, the depth-4 AND/OR tree (+0.0037 I), is an ordering
effect: co-occurrence is not monotone in tree distance (leaf 0 of that tree: c_0j = 0.0663, 0.0221, 0.0284, 0.0067 for
lowest common ancestors at heights 1, 2, 3, 4), so the first class met can be the height-3 class while S - i also meets
height 2, and |S - i| cannot tell height 2 from height 4. At depth 3 only one class is left over and the pair is exact.
The classes are the tree's distance classes; only their order is wrong.
(ii) The count profile is exact on every structured function except MAJ3 of AND_w, where it merges the two other blocks
(excess 0.0031, 0.035, 0.045, 0.037 I at w = 3, 4, 5, 6, with B/I = 2.84, 2.41, 2.18, 2.08, so bounded along the family),
X003 (+0.10 I) and X009 (+0.015 I at m = 6, shrinking with m).
(iii) Single-integer statistics fail in complementary ways. The level costs 0.46 to 1.81 I above B on tribes (growing;
O5) and 0.38, 1.02 I on the AND/OR trees of depth 3, 4. The first-contact rank is exact on tribes and within 0.009 I on
those trees, but costs 1.96, 2.18, 2.26 I on majority 9, 13, 15, where B = 0; that is 0.633, 0.639, 0.640 of the trivial
sum_i h2(eps_i), so it grows like the trivial bound. It loses 1.0 I on every OR of MAJ3 and 1.5, 1.8 I on OR3 of MAJ5 and
OR2 of MAJ7. A witness exact on tribes and on majority has to record where S - i lies (scale) and how much of it lies
there (count).
(iv) Generic functions say little. On the random DNFs and tables every witness tried costs 0.04 to 1.08 I above B, with B/I
between 1.1 and 2.4. The count profile comes closest because the classes there are almost singletons, where it is S - i
itself; exact ties among the integer-valued co-occurrences leave 7 to 9 distinct values among 9 coordinates on a random
table, and its excess can only come from those ties.
(v) No witness can be charged coordinate by coordinate. X009 (F(y, t) = g(y)(1 - 2t 1{y = 0}), g bent on m bits) has
eps_t = 2^-m for the selector bit and B_t/eps_t = 5.224, 7.387, 9.429, 11.439, 13.442, 15.442 at m = 4, 6, ..., 14, against
log2(1/eps_t) + 1/ln 2 = 5.443, 7.443, ..., 15.443 (the SEL referee's B_t/delta = log2(1/delta) + 1/ln 2 + O(delta),
re-checked here). D_t F is a point indicator, so B_t sits at levels near m/2 = 0.72 ln(1/eps_t), inside B_gap. Since
H(S_t | W_t) >= B_t for every witness, a bound H(S_i | W_i) <= K eps_i fails for every choice of W, and B_gap = O(I) can only
hold after summing over coordinates: the selector's excess is paid by the other coordinates' slack (its share of B is 0.082
at m = 4 and 7e-5 at m = 14).
(vi) Regime. Every function here has H/I <= 3.97, so the bench says which statistics are sufficient on structured families
and nothing about growth; growth is settled only on tribes (section 5) and read-once formulas (5b).
Reading. On every structured family tried, the sufficient statistic is a scale-and-count profile of S - i around i: classes
of equal co-occurrence give the scales (their order has to come from the structure; co-occurrence order is already wrong
on AND/OR trees), and the counts carry the parity-type information that odd components need. For a proof this states the
missing piece more sharply. A cell w of a witness costs (a_w + d_w) h2(pi_w), between d_w log2(1/pi_w) and
d_w log2(e/pi_w), where pi_w = P(i in S | W = w). A witness argument for B_gap therefore needs, on most of the mass of D_i f
above level c ln(1/eps_i), cells on which pi_w is bounded below, and by (v) only on average over i. Lemma 2 bounds level
weights from above and cannot give such a lower bound; we have no substitute. The scale-and-count profile is the
candidate witness on which that lower bound would have to be proved.

## 5d. Pivotal sets and the price of an unpredictable coordinate (s07, 12 Oct; P1-P4 PROVED and elementary, the rest EVIDENCE)
Notation. A_i = {x : f(x) != f(x^i)}, so P(A_i) = eps_i; s(x) = #{i : x in A_i}, the sensitivity at x; for a set A,
I(1_A) = sum_j P(1_A(x) != 1_A(x^j)). For i != j the {i,j}-face through x is odd (event E_ij) when it carries an odd number
of -1 values, and a parity face (event Par_ij) when f(x) = f(x^ij) != f(x^i) = f(x^j); every other face is constant or
depends on only one of its two coordinates.

Lemma P1 (PROVED; faces). (a) 1_{A_i}(x) xor 1_{A_i}(x^j) = 1_{E_ij}(x) = 1_{A_j}(x) xor 1_{A_j}(x^i), so
I(1_{A_i}) = sum_{j != i} P(E_ij). (b) P(E_ij) = 4 P(E_ij and A_i and A_j), and P(A_i and A_j) = P(E_ij)/4 + P(Par_ij).
Proof. Going round a face, f comes back to its starting value, so a face has an even number of pivotal edges: one i-edge is
pivotal without the other exactly when the same holds for the two j-edges, and exactly when the product of the four values
is -1. An odd face has one corner carrying the minority value; i and j are both pivotal there and nowhere else on the face.
On an even face, i and j are both pivotal at a corner only if all four edges are pivotal, which is the parity face. []

Lemma P2 (PROVED; Harper's inequality on pivotal sets). A set of measure mu in {-1,1}^n has at least mu 2^n log(1/mu)
boundary edges, so I(1_{A_i}) >= 2 eps_i log(1/eps_i). With P1(b), which gives I(1_{A_i}) <= 4 eps_i E[s - 1 | A_i]:
  E[s - 1 | A_i] >= (1/2) log(1/eps_i)                                   (equality for AND_n at every n)
  h2(eps_i) <= eps_i log e + I(1_{A_i})/2 <= eps_i (log e + 2 E[s - 1 | A_i]),
the second from (1 - eps) log(1/(1 - eps)) <= eps log e. []

Proposition P3 (PROVED; pricing a set of coordinates). For any set C of coordinates, with s_C(x) = #{t in C : x in A_t},
  sum_{t in C} B_t <= sum_{t in C} h2(eps_t) <= log e sum_{t in C} eps_t + 2 E[s_C (s - 1)].
If at most r coordinates of C are pivotal at any one point, the right side is at most (log e + 2r) I.
Proof. B_t <= H(S_t) = h2(eps_t); then P2, and sum_{t in C} eps_t E[s - 1 | A_t] = E[s_C (s - 1)]. If s_C <= r everywhere,
E[s_C (s - 1)] <= r E[s] = r I. []
With C = all coordinates and the identity E[s^2] = E[|S|^2] (below), H <= sum_i h2(eps_i) <= 2 E[|S|^2] - (2 - log e) I.
Chakraborty, Kulkarni, Lokam and Saurabh (TCS 2016; ECCC TR13-052) bound the Fourier entropy through the first two moments of
sensitivity; we have not compared constants and claim nothing new in this line.

Lemma P4 (PROVED; mean level of a derivative). sum_k k W_k(D_i f) = I(1_{A_i})/4 + sum_{j != i} P(Par_ij); for monotone f the
last sum is 0. With P2 the mean level of D_i f is at least (1/2) log(1/eps_i) = 0.72 ln(1/eps_i), with equality for X009's
selector, whose derivative is a point indicator.
Proof. D_i f takes the values 0 and +-1, and sum_S |S| (D_i f)^(S)^2 = (1/4) sum_j E[(D_i f(x) - D_i f(x^j))^2]. The j-th
term is 1 where exactly one of x, x^j lies in A_i, and 4 where both do with opposite signs of D_i f, which is a parity
face. A monotone f has no parity face. []
Summed over i, the left side of P4 is sum_S |S| (|S| - 1) p(S) and, by P1(b), the right side is E[s (s - 1)]: the known
identity E[s^2] = E[|S|^2] for Boolean f. The mean-level bound sits above the threshold of Theorem 5 but is a reading of
Harper's inequality, not a new constraint on the levels.
None of P1-P4 is claimed new: P1(b) is the pairwise form of E[s^2] = E[|S|^2], and P2 with P4 is the standard
consequence of the edge-isoperimetric inequality that a function supported on a set of measure eps has mean Fourier
level at least (1/2) log(1/eps).

What P3 does for B_gap, and what it does not. Section 5c(v): a witness bound cannot be charged coordinate by coordinate,
because X009's selector has B_t = eps_t (log(1/eps_t) + 1/ln 2 - o(1)). Such a coordinate can be paid by its trivial witness,
B_t <= h2(eps_t), whenever the trivial costs of all such coordinates sum to O(I); for X009 they do, because the bent
coordinates carry I = m/2. P3 bounds that trivial cost and gives nothing below it. By P1(b), P(A_t and A_j) =
||D_t D_j f||^2 = P(t, j in S), the pairwise form of E[s^2] = E[|S|^2] (code/audit_pivotal_faces.py, check 4), so
E[s_C (s - 1)] = E[|S cap C| (|S| - 1)] and P3 is the sum over C of
  h2(eps_t) <= eps_t (log e + 2 E[|S| - 1 | t in S]),
the inequality eps log(1/eps) <= 2 eps (mean level of D_t f) of P2 and P4. As a rule for leaving a set C out of a witness
argument, E[s_C (s - 1)] = O(I) is therefore never stronger than the trivial rule sum_C h2(eps_t) = O(I), which needs no
lemma (by P2 the first implies the second), and the bound of P3 can exceed the trivial cost by an unbounded factor: the
selector bit of a random set of measure 1/16 in the m-cube has E[s - 1 | A_t] = 5.98, 8.01, 10.00 at m = 12, 16, 20 against
(1/2) log(1/eps_t) = 2. What P3 adds is a combinatorial form of the trivial cost, 2 E[s_C (s - 1)] = (1/2) sum_C I(1_{A_t}) +
2 sum_{t in C, j != t} P(Par_tj): the boundaries of the pivotal sets plus their parity faces. For X009 and C = {t}, P3 gives
0.1163 against h2(eps_t) = 0.1161 and B_t = 0.1154 at m = 6 (1.0003 B_t at m = 10, 1.00001 B_t at m = 14): the pivotal set is
a point times the selector bit, and Harper's inequality is tight there.
The split. A proof of B = O(I) can leave out any set C whose trivial cost is O(I) and must give every coordinate outside C a
witness W_i with sum_{i notin C} H(S_i | W_i) = O(I). With C empty and W_i = S - i this is B = O(I) itself, so the split
organizes a proof and is not a reduction: the content is in the witnesses for the coordinates whose trivial cost is too
large. The trivial cost can be far above B_t: the address function's selected bits have B_t = 0, because S always contains
exactly one of them (there the bound of P3 is close to sum_C h2 alone, 4.35 against 4.44 on 11 bits).

Unpredictable coordinates and subcubes (EVIDENCE). A natural guess is that an unpredictable coordinate, B_t close to
h2(eps_t), has a pivotal set close to a subcube, the equality case of P2, so that the coordinates fixing the subcube pay for
it. That is false. For F(y, t) = g(y) (-1)^{t 1_A(y)}, g bent on m bits and A a uniformly random set of 2^{m/2} points:
  m                                     = 10      12      14      16      18      20
  B_t/eps_t - log(1/eps_t)              = 0.121   0.264   0.323   0.352   0.370   0.379
  u_t = B_t / h2(eps_t)                 = 0.798   0.843   0.868   0.885   0.897   0.907
  I(1_{A_t}) / (2 eps_t log(1/eps_t))   = 1.988   1.969   1.987   1.991   1.996   1.999
  E[s - 1 | A_t]                        = 4.97    6.00    6.98    8.00    9.01    10.00
The offset approaches log e - 1.05 = 0.39 (heuristic: given t in S, the law of S - t is p(U) times a chi-square weight with one
degree of freedom, at relative entropy E[Z log Z] = 1.05 bits), so u_t tends to 1 while the boundary of A_t stays twice the
Harper minimum. With A of measure 1/16 the Harper ratio grows like 0.23 m (2.81, 3.75, 4.69 at m = 12, 16, 20) at u_t = 0.71.
P3 bounds the trivial cost of these selectors through E[s - 1 | A_t], here about m/2, not through subcube structure; for one
selector that is O(I), and nothing here says what happens with many unpredictable coordinates at once
(section 5e answers this for blocks whose fibers are signed characters).

Checks (code/pivotal_faces.py, data/pivotal_faces.json, data/pivotal_faces.log; code/audit_pivotal_faces.py,
data/audit_pivotal_faces.log). P1(a) at every point, P1(b), P4, the summed identity and P2 hold with error 0 (every quantity
is dyadic) on 28 functions: tribes 3x3, 4x3, 3x5, majority 9 and 13, a Hamming ball, x0 times bent, AND/OR trees of depth 3
and 4, OR4 of MAJ3, MAJ3 of AND4, the address functions on 11 and 20 bits, X002, X003, X009 at m = 6, 10, 14, two cube and
three random selectors, three functions with 8 to 12 random selectors, a random DNF and a random table. Negative controls:
without its parity term P4 is off by 4.0 on x0 times bent (and exact on majority and tribes, which are monotone, as P4 says);
with 2 in place of 4, P1(b) is off by 0.19 to 0.50. The selector rows were recomputed from the closed form
p(U + t) = (g 1_A)^(U)^2, p(U) = (ghat(U) - (g 1_A)^(U))^2 with m-bit transforms, and I(1_{A_t}) by counting the edges of A in
the m-cube; they equal the brute-force values (difference 0) for m <= 14, and the rows m = 16, 18, 20 use the closed form only.
AND_n attains E[s - 1 | A_t] = (1/2) log(1/eps_t) at n = 4, 8, 12, 16.

## 5e. Blocks with signed-character fibers: the data block is paid by the address block (s07, 12 Oct; Lemma B, the identity and Corollary K PROVED and elementary, none claimed new; the rest EVIDENCE)
Setting. Split the coordinates into an address block X and a data block Y, and suppose every fiber is a signed character:
F(x, y) = s(x) chi_{tau(x)}(y) with s(x) = +-1 and tau(x) a subset of Y. Write A_T = tau^{-1}(T), R_T = P(tau(X) = T) and
I_X = sum_{j in X} Inf_j(F). Every Boolean function has this form with |Y| = 1 (a fiber is then a function of one bit, so
it is +-1 or +-chi_t). The selector functions of 5c and 5d (X009, the cube and random-set selectors, the many-selector
functions), the address function (tau(x) = {x}) and x0 times bent (Y = {x0}) have it with Y the selector or data block. It
is the class of A2's Corollary A'.

Lemma B. sum_{t in Y} B_t <= H(S_Y) = H(tau(X)) <= 2 I_X, and the constant 2 is attained.
Proof. (a) B_t = H(S_t | S - t) <= H(S_t | S_{Y - t}), and sum_t H(S_t | S_{Y - t}) <= H(S_Y) by the chain rule, each term
of which conditions on less. (b) Fhat(U, T) = E_x[s(x) 1{tau(x) = T} chi_U(x)] = Ghat_T(U) with G_T = s 1_{A_T}, so
P(S_Y = T) = ||G_T||^2 = R_T, and given S_Y = T the law of S_X is nu_T(U) = Ghat_T(U)^2 / R_T. (c) For G = s 1_A with
P(A) = R, sum_j ||D_j G||^2 = (1/2) sum_j P(x in A, x^j notin A) + sum_j P(x, x^j in A, s(x) != s(x^j)) >= (1/2) R log(1/R)
by the edge-isoperimetric inequality (Harper). So E[|S_X| | S_Y = T] >= (1/2) log(1/R_T), and averaging over T gives
I_X = E|S_X| >= (1/2) H(R). Attained: for AND2^N, F(y, t) = prod_k (-1)^{t_k (1 - y_k)} (N disjoint copies of a two-bit AND,
Y the t bits), tau(y) = {k : y_k = 0} is uniform, every fiber is a point, S_X and S_Y are independent and uniform, and
sum_Y B_t = N = 2 I_X. QED.

Identity. For any F and any split, B_X = sum_T R_T B(nu_T), where nu_T is the normalized spectral law of the slice
F_T(x) = E_y[F(x, y) chi_T(y)] (in the class above, of s 1_{A_T}): S - x contains S_Y, and B is 1-homogeneous. On the class
therefore
    sum_T R_T B(nu_T) <= B(F) <= sum_T R_T B(nu_T) + 2 I_X,   with I_X = sum_T R_T E_{nu_T} |U|.

What this settles, and what it does not.
(i) Within the class the data block is never the obstruction. Any number of selector coordinates, unpredictable or not, cost
at most 2 I_X together; if u_t = B_t / h2(eps_t) >= u for every t in Y, then sum_Y h2(eps_t) <= (2/u) I. This answers, for
this class, the question left at the end of 5d: with any number of unpredictable coordinates in the block, their trivial
costs still sum to O(I), so the trivial witness is affordable for the whole block.
(ii) The payment is of the kind 5c(v) asks for and is not made coordinate by coordinate: X009's selector bit sits in B_gap
and is paid by the address block's influence, through Harper on the fibers. On X009 it is very loose (B_Y / 2 I_X = 0.019,
0.0011, 0.0001 at m = 6, 10, 14); on AND2^N it is exact.
(iii) It does not touch the address part. The class contains every Boolean function (|Y| = 1), so it is as hard as FEI;
the average sum_T R_T B(nu_T) runs over normalized signed subset functions s 1_A. What Lemma B shows is that composing with a
signed-character data block adds at most 2 I_X to B.
(iv) Outside the class, (a) still holds, and H(S_Y) = avg_x H(F_x) + I(X; T) with I(X; T) <= (2/ln 2) I_X
(SEL-selector-interference NOTES 3.1 (i) and (ii), the BR theorem, KNOWN in the campaign), so
sum_Y B_t <= avg_x H(F_x) + (2/ln 2) I_X. Lemma B is the case avg_x H(F_x) = 0, with 2 in place of 2/ln 2. Without the fiber
hypothesis H(S_Y) <= 2 I_X is false: it fails on the depth-3 AND/OR tree with Y its left subtree (2.39 against 1.31), on X009
with Y the bent block (5.96 against 0.03) and on MAJ3 with three dummy address bits (2 against 0).
Novelty. None claimed. The chain is standard (erasure entropy is at most entropy; Harper). Its cell form H(p) <= 2D is the
step of SEL-7 (iv) taken from the paper's edge isoperimetry, and A2's Corollary A' bounds the full H by 4 (I - Inf_y) on the
same class when every row has a product law. The use is what is added here: with no hypothesis on the rows it disposes of
the data block for B.

Checks (code/selector_block.py, data/selector_block.json, data/selector_block.log; 25 functions, n = 6 to 20). On the 20
splits with signed-character fibers (verified fiber by fiber from Walsh transforms on Y) the law of S_Y, I_X, the spectrum
given S_Y = T and the identity were computed twice, from the full spectrum and from the slice functions s 1_{A_T}; the
largest difference is 3.6e-15 (B_Y and H(S_Y) are recomputed by the second path below). B_Y / 2 I_X: X009 0.019, 0.0011, 0.0001 (m = 6, 10, 14); cube selectors 0.026, 0.0031; random-set selectors
0.020, 0.0070; the three many-selector functions 0.37, 0.28, 0.26 (H(S_Y) = 5.18, 4.07, 3.65 against sum_Y h2 = 6.49,
4.35, 4.05: the selectors are dependent); two products of X009 0.073, 0.019; the address functions on 11 and 20 bits 0
(B_Y = 0 although H(S_Y) = 3, 4: exactly one data coordinate is in S, so S_{Y - t} decides S_t); AND2^4, AND2^6, AND2^8
exactly 1; tribes 3x3 with Y = {0} 0.16. The fiberwise Harper bound has slack 0 at every fiber that is a point, or a
subcube with no sign change inside. The five general splits satisfy sum_Y B_t <= H(S_Y) <= avg_x H(F_x) + (2/ln 2) I_X (on X009 with Y
the bent block 5.9561 against 5.9563, on MAJ3 with dummy address bits 2 against 2).
Second path (code/audit_selector_block.py, data/audit_selector_block.log; its own transform, entropy and B, no code
shared): all 65,536 functions of 4 bits with each coordinate as Y, all 4,096 pairs (tau, s) with m = N = 2, and 16,200
random ones under four schemes (uniform tau, few cells, subcube cells, one-hot; m = 3 to 7, N = 1 to 6, n <= 11). No
violation beyond 1e-12, H(S_Y) = H(tau) to 0, and both inequalities are attained in every family (for instance by a
bijective tau with m = N, which makes S_X and S_Y independent and uniform).

Corollary K (K-partite polynomials; PROVED and elementary, not claimed new). Split [n] into blocks
X_1, ..., X_K and suppose every monomial of the GF(2) polynomial P of f = (-1)^P uses at most one variable of each block
(equivalently, the K blocks properly colour the graph that joins two coordinates when some monomial contains both). Then
    B(f) <= H(f) <= sum_k H(S_{X_k}) <= 2 sum_k I_{X_{-k}} = 2 (K - 1) I(f).
Proof. Fixing the coordinates outside X_k leaves a polynomial of degree at most one in x_{X_k}, so every fiber over X_{-k}
is a signed character, and Lemma B gives H(S_{X_k}) = H(tau_k) <= 2 I_{X_{-k}} with I_{X_{-k}} = I - I_{X_k}. Entropy is
subadditive over the blocks, sum_k (I - I_{X_k}) = (K - 1) I, and B <= H. QED. Conversely a fiber is affine for every value
of the other coordinates exactly when no monomial has two variables in the block, so this is the whole class on which
Lemma B applies to every block at once.
In graph terms H <= 2 (chi - 1) I with chi the chromatic number of that graph; a greedy colouring gives chi <= Delta + 1,
so H <= 2 Delta I whenever every coordinate shares a monomial with at most Delta others.
Sharpness and limits. K = 2 is the bilinear-plus-affine case, and there H <= 2I with equality on inner product (H = 2n,
I = n) and on a single x_i y_j. That case is elementary and not claimed: a quadratic phase whose alternating form has rank 2h has a flat
spectrum on 2^{2h} sets, so H = 2h, while at least 2h coordinates have influence 1/2, so H <= 2I for every quadratic;
Potapov's plateaued theorem gives 4I. For K >= 3 the constant 2(K - 1) is not known to be attained. On the exhaustive shapes
(1,1,1), (2,1,1), (3,1,1), (2,2,1) and (1,1,1,1), on random members and in a greedy search, the largest H/I found is that of
one monomial with a variable in each block, the AND of K bits up to sign: 2.9559 = c* at K = 3 and 3.4025 at K = 4, against
the bounds 4 and 6. Simulated annealing (code/block_partite_search.py) on shapes up to (4,4,4) and (3,3,3,3), restarted
from random sets and from the AND of K bits, found nothing above these values either; from random starts it often stalls
lower, so beyond the exhaustive shapes this is weak evidence that D_3 = c*. Every f on n variables is n-partite (singleton blocks), so the constants D_K = sup H/I over K-partite f
form a nondecreasing ladder whose supremum is the FEI constant, as A2's address ladder does; the corollary gives D_2 = 2
and D_K <= 2(K - 1).
It does not reach the families behind the obstructions of sections 5 and 5b (balls in O2, tribes in O5, AND/OR
trees in 5b): the GF(2) polynomials of tribes, of AND/OR trees and of any symmetric
function containing some e_d with d >= 2 (Hamming balls among them) have a monomial through every pair of coordinates (for
tribes and AND/OR trees, the product of all variables), so their graphs are complete and K = n. The coefficient of
x_1...x_n is the parity of |P^{-1}(1)|, and a read-once AND/OR formula with any negations has an odd number of
satisfying inputs (by induction: ab and 2^m - (2^{m_1} - a)(2^{m_2} - b) are odd when a and b are); a symmetric P is a
sum of distinct e_d, and without some d >= 2 it would depend only on |x| mod 2, which no ball of radius 0..n-1 does for
n >= 2. Checked by Moebius transform (code/partite_reach.py, data/partite_reach.log): tribes to n = 10, alternating
trees, 300 random read-once formulas, 54 balls and majority all give complete graphs; inner products and 100 random
bilinear forms, the controls, never do.
Novelty. Not claimed. The class is outside the covered classes checked in the campaign (read-once, symmetric, tensor and
composition, finite, threshold, read-k, small density, bounded spectral support, plateaued; A2's K2 and Corollary A' need
product rows, and here the rows s 1_{tau_k = T} are cells of a multilinear map whose laws need not be product), but no
literature search has been done.
Checks. code/block_partite.py (data/block_partite.json, block_partite.log): 244,934 members (199,208 exhaustive on nine
shapes, 3,220 random on eight shapes with K = 2 to 5, 42,506 greedy-search evaluations), no violation of
B <= H <= sum_k H(S_{X_k}), of H(S_{X_k}) <= 2 (I - I_{X_k}) or of sum_k H(S_{X_k}) <= 2 (K - 1) I; as a control, the same
checks on 600 polynomials that break the block condition find 414 violated inequalities. code/audit_block_partite.py
(data/audit_block_partite.log) shares no code: members are built as sums of products of affine forms, one per block,
admitted only after a fiber-by-fiber Walsh test, with influences read off the truth table and the spectrum from an explicit
Hadamard matrix. 1,360 members on eight shapes, no rejection and no violation, the same maxima (2, 2.9559, 3.4025); adding
one monomial with two variables of one block makes the fiber test reject 400 of 400, and the block inequality then fails on
82 of them. A short greedy search over general polynomials of GF(2) degree at most 3 on 5 to 7 variables found nothing
above 2.9559, but at 6 and 7 variables it did not reach c* either (block_partite.log, part 4), so it says little; whether
the degree alone bounds H/I is not addressed here.

## 6. The G/KL sandwich, re-derived (independent confirmation of B13, BOARD.md line 103)
G_i := sum_{T contains i} p(T) log(1 + p(T - i)/p(T)) = eps_i [log(1/eps_i) - D(nu_i || m_i)], nu_i(U) = p(U + i)/eps_i,
m_i(U) = p(U) + p(U + i) (U not containing i; m_i is the law of S - i). G_i <= B_i <= G_i + eps_i log e, because the
lower-endpoint part of each edge is p(U) log(1 + p(U+i)/p(U)) <= p(U+i) log e. Lemma 1 summed with a_{j,i} is the same
bound after pushing nu_i and m_i forward to levels: sum_j d_j log(e (a_j + d_j)/d_j) = eps_i [log(e/eps_i) - D(lambda_i || mu_i)]
with D(lambda_i || mu_i) <= D(nu_i || m_i) by data processing. J_i <= B_i (B13, Maassen-Uffink form) holds with no
violation in every run of section 7; its proof is B13's and was not re-derived here.

## 7. Numerics
 - code/check_levels.py quick run (data/check_levels_20261012T151624_quick.json): 0 violations of A096_d1, HC_d1, HC_d2,
   B <= H, J <= B, G <= B <= G + log(e) I, H2 <= K2 I, B_1 <= 7.540 I, H3 <= 7.985 I, B_2 <= 25.40 I. Maxima: B/I 3.389
   (tribes 2x5), H/I 3.906 (AND-like, n = 12), B_0/I 1.1725, B_1/I 1.333, B_2/I 1.083, B_3/I 0.716, H2/I 1.667, H3/I 1.186,
   d_1 / A096 bound 0.721.
 - code/check_levels.py full run (data/check_levels_20261012T181724.json, data/check_levels_full.log; 70,253 functions,
   10,818 s, exit 0): 0 violations of the same eleven checks. Maxima: B/I 3.3892 and B_{>=1}/I 2.6030 (tribes 2x5), H/I 3.9060
   (AND on 12 bits), B_0/I 1.1725, B_1/I 1.3333, B_2/I 1.1816, B_3/I 1.0237, H2/I 1.6667, H3/I 1.6301 (the last five from
   hill climbs at n = 5 to 8), J_i/B_i at most 1, d_1 / A096 bound 0.7213, d_2 / HC bound 1 (equality, at the parity of
   3 bits). The climbs raise the quick run's B_2/I, B_3/I, H3/I from 1.083, 0.716, 1.186; all stay far inside the bounds.
 - code/check_lemma1.py: 68,148 functions, Lemma 1 (psi form) 0 violations, max ratio 0.99971; max B_j/I seen 1.172, 1.149,
   0.911, 0.625, 0.547, 0.492, 0.328, 0.221, 0.133, 0.085 for j = 0..9.
 - code/check_lemma1pp.py: 68,078 functions, 0 violations of B^(i)_j <= phi(a,d) <= d log(e(a+d)/d) <= psi(d) and of
   B_i <= sum_j phi(a_{j,i}, d_{j,i}).
 - Closed forms of O1 and O2 agree with truth-table transforms: Hamming balls n = 9, 11, 12, 13 (B_0 and I to 1e-10) and
   x0 * bent_m, m = 4, 6, 8 (every B_k exact).
 - code/per_level_constants.py, code/obstruction_tables*.py, code/slice_levels.py: the tables quoted above.
 - code/certify_constants.py (interval certificate, 3.6), code/adversarial_check.py (second code path, 9),
   code/witness_tribes.py (tribes witness closed form against brute force, section 5), code/slice_limit.py (Proposition 6 checks, section 4).
 - code/readonce_witness.py: Lemma R, the height-s witnesses and the level statistic on read-once AND/OR trees (section 5b).
 - code/general_witness.py: 43 functions, eleven witnesses (section 5c); data/general_witness.json, general_witness.log.
 - code/audit_general_witness.py: second path for B and I on eight bench functions, Corollary R2, co-occurrence against
   tree distance, MAJ3 of AND_w to w = 6, X009's selector bit (section 5c); data/audit_general_witness.log.
 - code/pivotal_faces.py: Lemmas P1, P2, P4 and Proposition P3 on 28 functions (section 5d); data/pivotal_faces.json,
   pivotal_faces.log. code/audit_pivotal_faces.py: negative controls, the selector bit by its closed form to m = 20, AND_n,
   and P(A_i and A_j) = P(i, j in S) from the truth table against the Fourier weights on eight functions (section 5d);
   data/audit_pivotal_faces.log.
 - code/selector_block.py: Lemma B, its sharpness on AND2^N and the identity for B_X on 20 signed-character splits,
   each quantity twice (full spectrum, slice functions); the general block bound on 5 other splits (section 5e);
   data/selector_block.json, selector_block.log. code/audit_selector_block.py: second path for Lemma B with no shared
   code, 278,440 cases (exhaustive on 4-bit functions and at m = N = 2, random to n = 11); data/audit_selector_block.log.
 - code/block_partite.py: Corollary K on 244,934 K-partite polynomials (nine exhaustive shapes, random shapes with
   K = 2 to 5, a greedy search) and a non-partite control; data/block_partite.json, block_partite.log.
   code/audit_block_partite.py: second path, no shared code (sums of products of affine forms, fiber test, influences
   from the truth table), 1,360 members and 400 controls; data/audit_block_partite.log.
 - code/block_partite_search.py: simulated annealing for the largest H/I on K-partite shapes up to n = 12 (section 5e);
   data/block_partite_search.json, block_partite_search.log.
 - code/partite_reach.py: GF(2) polynomials of tribes, AND/OR trees, read-once formulas, balls and majority have
   complete co-occurrence graphs, so Corollary K does not reach them (section 5e); data/partite_reach.log.

## 8. Status
PROVED: Lemma 1 (with the phi(a,d) form), Lemma 2 (level one by two independent arguments, 9.2), Theorem 3 with b_1 exact and
b_k <= 2k log e, Corollary 4, Theorem 5 (finiteness), the exact Bonami threshold 1/2, the KKLMS transfer, O1-O5, and the
tribes witness bound sum_i H(S_i | W_i) <= (2 + O(w 2^-w)) I (section 5, after O5), Proposition 6 (level law of a slice) and
Corollary 7 (no level inequality for {0,+-1} functions raises the threshold 1/2).
PROVED (section 5b): Lemma R (B_i of a read-once formula in closed form) and Corollary R1 (the branch witness is exact).
EVIDENCE (section 5b): on AND/OR trees no fixed-size witness has cost O(I); a cell of order log(1/eps_i) coordinates does.
PROVED (section 5c): Corollary R2 (on read-once AND/OR/parity formulas the height tau_i at which S - i first reaches the
branch of i is an exact witness).
EVIDENCE (section 5c): a scale-and-count profile of S - i is an exact witness on 27 of 28 structured functions outside
the X-family (the exception is an ordering effect); single-integer statistics fail on tribes (level) or on odd functions
(first contact); X009's selector bit rules out witness bounds charged coordinate by coordinate (re-checked).
PROVED (section 5d, elementary): Lemma P1 (odd and parity faces), Lemma P2 (Harper on pivotal sets, E[s - 1 | A_i] >=
(1/2) log(1/eps_i)), Proposition P3 (a set C of coordinates costs at most log e sum_C eps_t + 2 E[s_C (s - 1)]), Lemma P4
(mean level of D_i f), none claimed new; P3 bounds the trivial witness cost of a set C and gives nothing below it.
EVIDENCE (section 5d): an unpredictable coordinate need not have a subcube pivotal set (random-set selector: u_t -> 1 with
the boundary of A_t twice the Harper minimum).
PROVED (section 5e, elementary, none claimed new): Lemma B (a data block whose fibers are signed characters has
sum_Y B_t <= H(S_Y) <= 2 I_X, constant 2 attained by AND2^N) and the identity B_X = sum_T R_T B(nu_T). Within that class
the data block, with any number of unpredictable coordinates, is never the obstruction; the address part is as hard as FEI.
PROVED (section 5e, elementary, none claimed new): Corollary K (if every monomial of the GF(2) polynomial of f uses at
most one variable of each of K blocks, then B <= H <= 2(K - 1) I; sharp at K = 2, the quadratic case, which is elementary).
EVIDENCE (section 5e): on K-partite polynomials the largest H/I found is that of the AND of K bits (2.9559 at K = 3,
3.4025 at K = 4), against the bounds 4 and 6.
PROVED by interval certificate (3.6): b_2 <= 3.5777, b_3 <= 7.3278, ..., b_10 <= 27.4379; C(0.2) <= 1.7501, C(0.3) <= 4.0782,
C(0.4) <= 13.8404, C(0.45) <= 46.9287. Grid values only: b_20, b_40.
Adversarial pass: section 9 (no gap found in the proofs; two grid constants corrected).
OPEN: B_gap(tau, c) = O(I), equivalently FEI.

## 9. Adversarial pass (s07, 12 Oct, after sections 3-5 were written)
Each proof was re-derived from the definitions without the text above, each number recomputed by a second route, and a
search tried to push every ratio towards its constant.

9.1 Lemma 1. Re-derived: phi(x,y) = (x+y) h2(y/(x+y)) is h2's perspective composed with (x,y) -> (y, x+y), hence jointly
concave on the closed quadrant (phi(0,y) = phi(x,0) = 0); degree-one homogeneity gives superadditivity; ln(1+x) <= x gives
phi(a,d) <= d log(e(a+d)/d); a + d <= 1. Summed over levels it is an identity plus data processing:
B_i = H(S_i | S - i) and sum_j phi(a_j, d_j) = H(S_i | |S - i|). Second code path (code/adversarial_check.py: its own
transform, nothing imported from check_levels.py), 107 functions up to n = 12 (tribes, majority, thresholds, x0 * bent,
address functions, Hamming balls, random depth-6 trees, random tables): 0 violations; max B^(i)_j / psi(d) = 0.99987
(threshold n = 11, t = 1). On the object: B20 as stated omits the edges at U = empty; B = B20 + B_0 with B_0 <= 1.7501 I.
No gap found.

9.2 Lemma 2(b) has two independent proofs. (i) A096's: L the level-one part of h = D_i f, sigma^2 = E L^2 = d_{1,i} = E hL.
Hoeffding's lemma E e^{tL} <= e^{t^2 sigma^2/2} and Jensen under P( . | h != 0) give t E[hL | h != 0] <= ln(2/eps) +
t^2 sigma^2/2, so sigma^2 = eps E[hL | h != 0] <= eps sigma sqrt(2 ln(2/eps)). (ii) Entropy, after Impagliazzo, Moore and
Russell's proof of Chang's inequality: on A = {h != 0} the map x -> h(x) x is at most two-to-one (h(x)x = h(x')x' forces
x' = +-x), so the pushforward nu of the uniform law on A has D(nu || uniform) <= ln(2/eps); the coordinate means of nu are
hhat(k)/eps, and subadditivity of relative entropy over coordinates with D(Ber((1+m)/2) || Ber(1/2)) >= m^2/2 gives
sum_k hhat(k)^2 <= 2 eps^2 ln(2/eps). The plain tail-integration route, E[|L| 1_A] <= int min(eps, 2 e^{-t^2/(2 sigma^2)}) dt,
gives only eps^2 (2 ln(2/eps) + 2 + o(1)); the constant 2 needs (i) or (ii). Largest d_1 / (2 eps^2 ln(2/eps)) seen in the
second code path: 0.656. Lemma 2(c), second proof: ||T_r h||_2 <= ||h||_p with r^2 = p - 1 and ||h||_p = eps^{1/p} gives
W_j(h) r^{2j} <= eps^{2/p}, the same bound with 1/p + 1/q = 1.

9.3 Theorem 3, analytic constant, second derivation: with j = k - 1 and q = 2 + 1/j, (1 + 1/j)^j <= e gives
rho <= min(1, e^{1-u}), u = L/(2j+1); then t <= (1 + L)/ln 2 <= (2j+2)/ln 2 for u <= 1 and t = (2j+2) u e^{1-u}/ln 2 <=
(2j+2)/ln 2 for u >= 1. Same 2k log e. The b_2 maximiser satisfies its stationarity equation (L + ln 2 - 1)(ln(1/rho) + L)
= L + ln 2 at L = 1.6449 (2.3383 against 2.3381 at the printed digits). Indexing (level j = k - 1, exponent k - 1 in
per_level_constants.py) checked line by line.

9.4 Theorem 5: the proof stands; two stated numbers did not. C(0.3) was given as 4.0720 and is 4.0782 (certified): the
first L grid (step 0.005) stepped over the entry point 20/3 where level 2 joins, and the localized majorant is largest
exactly there. C(0.4) and C(0.45) move to 13.8404 and 46.9287. Corrected in place in section 4 and in data/check_lemma1.json.

9.5 O5, second code path: tribes(2,3) gives sum_i H(S_i | |S - i|)/I = 2.731158 and sum_i h2(eps_i)/I = 3.047639, equal to
data/obstruction_tables2.json at every printed digit; tribes (3,3), (2,5), (3,4), (4,3), (2,6) give 3.639/3.680,
3.877/3.982, 3.721/3.892, 4.104/4.547, 4.044/4.429, while B/I stays between 2.3 and 3.6.

9.6 Pushing the ratios. Maxima over the 107 functions: B_{k-1}/I = 0.937, 1.149, 0.848, 0.585 for k = 1..4 (constants 1.7501,
3.5777, 7.3278, 10.1773); Loc_c/I = 0.937, 1.021, 1.372, 1.372 for c = 0.2, 0.3, 0.4, 0.45 (constants 1.7501, 4.0782, 13.8404,
46.9287). A greedy bit-flip search over 8-variable tables (6 starts, 1500 flips each) reached B_0/I 1.007, B_1/I 1.246,
B_2/I 1.091, Loc_0.3/I 1.011, Loc_0.4/I 1.019, below the structured families. Nothing came near a constant; they are loose by
factors 2 to 34 on everything tried, as expected of a supremum over eps of a per-coordinate bound.

9.7 Taken as cited, not re-derived: the equivalence of FEI with B <= K I (campaign C018, through J_i <= B_i of B13; B <= H
is the chain rule and gives the easy direction) and the KKLMS theorem itself (only the transfer in section 2 was checked).
9.8 Proposition 6 and Corollary 7 (written after 9.1-9.7). The moment identity was checked by two exact paths that share no
code: direct Krawtchouk sums of (2k - N)^{2r} lambda_k and closed walks on the integer tridiagonal matrix T (T[n][n+1] = 1,
T[n+1][n] = (n+1)(N-n)), which is similar to 2(J - N/2); they agree as fractions on all 20 cases (N = 200..2000, r = 1..4).
The central moments approach the arcsine values with ratio 1 + O(r/N) (1.0000031 at N = 10^6, r = 1). The finite-N masses
below c ln(1/eps) approach the arcsine limit from above (rho = 0.2, c = 0.55: 0.0581 at N = 8000 against 0.0552). The
convention for the Krawtchouk transform of the slice was re-derived from the count of sets Y with |Y| = t, |U cap Y| = l.
No gap found.
9.9 Lemma R (written after 9.8). Re-derived from the composition formula fhat(T_1 + ... ) = gtilde(J) prod_j fhat_j(T_j)/sigma_j
(sum of a child's nonempty weights is sigma_j^2). Three code paths agree: brute-force transforms (n <= 16, 4e-14), the float
closed forms, and the generic expansion in 80 digits (4e-13 up to depth 14). The generic expansion in double precision is NOT
a valid check at large depth: at AND2/OR3 depth 9 the gate means are within 1e-12 of +-1 and sqrt(1 - mu^2) loses its digits
(0.8 percent error in B, 11 percent in a witness cost); that is why the families use the closed forms. Two slips were
fixed before the numbers above were taken: the empty mask must be dropped from the normalized law below the root (the
brute-force comparison of H(S_i | |S - i|) fails otherwise), and at a nearly constant root -P log P must be written as
-(1 - Var) log(1 - Var) (H/I came out 0.005 low at depth 17, and not monotone in d, before that). No gap found in the lemma.
