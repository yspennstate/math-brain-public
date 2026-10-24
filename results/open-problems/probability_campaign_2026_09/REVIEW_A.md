# Reviewer A: referee report on RANKING.md (probability campaign, September 2026)

Written 2026-09-14. I read RANKING.md and INDEX.md in full, the memos for the top eight ranked items and
for every Tier 2 row whose memo is in `downloads_memos/`, the seven Lean files in `prob1000_lean_20260908/`,
the Codex proof file P0341, and the ProofNet24 inventory. For each of the top items I re-derived the
load-bearing step by hand and, where the object is finite, recomputed it independently
(`review_checks.py` in this directory: Aldous-Fill 4.48 and 4.45 to the printed digits, the two
Hasebe-Ueda polynomial lemmas symbolically plus a scan of 430,000 pairs, a random-chain control of
tau_2 <= tau_1^(2), and the growth-condition arithmetic of Janson 20.2 Theorem B). Sources I could not
open (the Janson survey, the Hasebe-Ueda paper, Aldous-Fill's text, Addario-Berry-Ford, GPS) are taken
as quoted by the memos; where a verdict depends on such a quotation I say so.

The word CLEAN below means: I re-derived the key step and found it correct as written. A gap is listed
as a gap even when it is repairable.

## 1. Scores

Importance and strength are on the ranking's 1-5 scales. "Draft" is the first-pass score; "A" is mine.
A reason is given wherever I differ by a point or more; smaller moves are explained in section 2.

| Rank | Problem | Draft imp / str | A imp / str | Reason where I move a point or more |
|---|---|---|---|---|
| 1 | Kalai Conj. 8 = GPS open problem 1 (Ent(f_R) = O(R^2 alpha_4(R))) | 5 / 3 | 4 / 4 | Importance: this is the FEI conjecture for one function, posed as a test case; the general conjecture is untouched and the proof shows the percolation case is easy in hindsight (first moments of the hit-square counts, which GPS already control, plus a quadtree code). A broad audience will find it a nice observation, not a breakthrough. Strength up: every step re-derives (section 2.1); the only thing missing is a referee, and the author has posted it. |
| 2 | Janson Problem 20.2 (b),(c) + Thevenin's conjecture | 4 / 3.5 | 3.5 / 3 | Strength: Theorem A (subcritical, part (c)) is complete and CLEAN, but part (b) rests entirely on Theorem B, which is a sketch whose stated growth condition is insufficient (section 2.2; repairable). The ranking's "NO in general" for (b) is stronger than the record. |
| 3 | Hasebe-Ueda Problem 3.3 (C = 1) with the classical companion D^2/4 | 3.5 / 5 | 3 / 4.5 | Importance: a sharp constant in a free-probability unimodality theorem; small community. Strength: the argument is CLEAN and doubly proved, but two inputs I could not check against the source (their Lemma 3.1 as the criterion, and whether the printed "2 <= C" is a slip or a different normalisation of D_mu). |
| 4 | Aldous-Janson Ansatz 20 and Open Problem 14 | 3.5 / 4.5 | 3 / 4.5 | OP14: what is proved is L_n = O(n log^2 n), which refutes the conjectured rate; Theta(n) is simulation only (the lower bound Omega(n) is trivial, the matching upper bound is not proved). The Ansatz refutation exploits the diagonal term a(n,n) = 1; the authors will call it a missing regularity hypothesis rather than a wrong Ansatz. |
| 5 | arXiv:2608.04303 Conjecture 1 and the layer half of Conjecture 2 (RRT layers) | 3.5 / 4 | 3 / 4.5 | Importance down half a point: the posers are a physics group and the paper is a 2026 preprint. Strength up: the dictionary is CLEAN and transparent (the PWIT is the Yule-tree embedding of the RRT, so M_k is the birth time of the first generation-k vertex); the rest is two citations. |
| 6 | Janson Conjecture 20.1 (level widths UI) | 3 / 4 | 3 / 4 | Agree. CLEAN (section 2.6). |
| 7 | Janson 18.30, 18.41, 18.42, 18.40, 18.9, 18.4, 18.10, 18.39 (group) | 3 / 4 | 3 / 3.5 | 18.4 CLEAN and elementary; 18.41/18.42 Theorem A CLEAN; 18.30 (ii) CLEAN but (iii) a sketch; 18.40's answer NO stands but its theorem's clause P(Y_(1) = m) -> 1 is not justified (section 2.7). 18.9, 18.10, 18.39 not read. |
| 8 | Aldous-Fill 4.48 (a),(b), 4.45, 4.30, 7.27 | 3 / 4.5 | 2.5 / 4.5 | Importance: these are questions about constants and small witnesses in a manuscript's notes; the book is a standard reference but the questions are peripheral. 4.48(b)'s eigenfunction proof is so short that a literature hit (Lovasz-Winkler) is a real risk. Strength: exact rationals, Lean core for 7.27, my recomputation agrees to all printed digits. |
| 9 | Agresti-Veraar Problems 4, 5 | 3 / 4 | 3 / 4 | Agree. The Ito reduction to BES(4) re-derives (section 2.9); the one thing I could not check is that the spatially constant solution is within the scope of their Theorem 6.4. |
| 10 | Salez Problem 2.4 | 3 / 4 | 2.5 / 4 | Retired by the campaign itself; the literal-statement refutation with unbounded degree is not what the community means by the conjecture. |
| 11 | Lyons-Peres Question 17.18 | 2.5 / 4 | 3 / 4.5 | Up: the AND/OR colouring is a genuinely nice construction, the stationarity step re-derives (section 2.11), and the question sits in a standard text still listing it open in its August 2026 version. |
| 12 | Burdzy-Scheutzow Problem 7.5 | 2.5 / 4 | 2 / 3.5 | The filling-scheme argument is the Thorisson / Last-Morters-Thorisson shift-coupling circle; the campaign's own memo expects it to be a known consequence. |
| 13 | Hasebe-Ueda-Wang Problem 4.7 | 2.5 / 4.5 | 2.5 / 4.5 | Agree. CLEAN (section 2.13). |
| 14 | Leskela Problems 1 and 3 | 2.5 / 4 | 2.5 / 3.5 | Problem 1 rests on a workload expansion with a uniform remainder that the memo itself says it did not re-derive. |
| 15 | Neri-Pinto Remark 3.7 | 2 / 4.5 | 1.5 / 4.5 | Arithmetic of the witness verified by hand; a remark in a 2026 preprint, low reach. |
| 16 | Rozikov Problems 3, 4, 10, 11 | 2 / 4 | 1.5 / 4 | Not read in detail; the Lean cores (E0061, E0063) certify only the elementary inequalities. Small subfield. |
| 17 | Khoshnevisan Open Problems 1, 3 (d = 3, 5) | 2.5 / 3.5 | 2.5 / 3 | No memo in the archive; the night report alone is not a record I can re-derive from. |
| 18 | Corrections to 2026 preprints (Kumar-Duddala 3.2; Levy-drift 5.3(ii); frog model 3.6) | 2 / 4 | 2 / 3.5 | H0010 trivially correct; H0013 Theorem 2 CLEAN, Theorem 3 a sketch; H0024 is NOT settled: its Proposition 2's extinction half is open by the memo's own account, so "artefact; growth is multiplicative" overstates it. |
| 19 | Pollett (ii); Bradley Q7; Konstantopoulos OP 2, 3 | 1.5 / 3.5 | 1.5 / 3.5 | Agree. Pollett probably known (Foley-McDonald), Bradley refuted from the survey's own material. |
| -- | (missing from the table) Asanjarani-Nazarathy Conjecture 4.2 (T^pi >=_st T^alpha) REFUTED, memo E0078 | not ranked | 2.5 / 4.5 | The ranking's "not candidates" line retires only 4.1 (known, He 2021). 4.2's refutation is separate: a two-line theorem for periodic Cox processes (g = e^{lambda* t} S has g(0) = g(T) = 1 and g > 1 between, so it must decrease somewhere) and a 24-state MMPP with an exact rational certificate. It belongs in Tier 2. |

## 2. Findings from the re-derivations

### 2.1 Kalai Conjecture 8 / F0090 -- CLEAN

Re-derived: (a) the quadtree code is prefix-free and Shannon gives H(A) <= 1 + 4 sum_k E|A_{2^k}| + C_0 E|A_1|;
(b) the geometric split of Lambda_B into a four-arm event in the disc of radius d/2 and a half-plane three-arm
event in the annulus (2d, D/2) -- the two regions are disjoint, both lie in Q_R because d is the distance to the
nearest side and D/2 is at most half the distance to the second-nearest, and the three far arms are two of one
colour and one of the other so the polychromatic half-plane exponent 2 applies (the weaker two-arm exponent 1
already suffices, as the memo notes); (c) the dyadic count C(d/r)(D/r) and the two geometric sums; (d)
quasi-multiplicativity turning sum_d (d^2/r^2) alpha_4(r,d) into C alpha_4(r,R) R^2/r^2 with a d^epsilon sum
dominated at d ~ R; (e) the scale sum sum_r r^{-epsilon}; (f) absorption of the C log R boundary term by
I(f_R) >= c R^epsilon. Nothing is used beyond GPS Lemma 3.2 (their (3.4), (3.6)), GPS (2.6), the half-plane arm
bound, and the standard first moment E|S| = E|P| ~ R^2 alpha_4(R). Two remarks for a referee: the proof never
distinguishes S from P, which is why both halves of the conjecture fall together; and GPS Section 4 already
proves the first-moment estimate for the hit r-squares, so the entire novelty is the coding inequality. That
is a genuine contribution but a small one. The memo's own Monte Carlo of E|P_r|/E|P| ~ r^{-0.74} is the right
control and agrees with 5/4.

### 2.2 Janson Problem 20.2 / F0064 -- Theorem A CLEAN; Theorem B sketch has a gap

Theorem A (nu < 1, refutes part (c) and Thevenin's subcritical conjecture). Re-derived: two rare atoms cannot
both fit (2L^- > m needs only q < 1/2); huge atoms exceed m; the J = 1 branch has probability
n p_r phi(A/sigma_r)/(sigma_r sqrt n) (1 + o(1)) for each sign, the O(1) bookkeeping in m - L^{+-} - (n-1)mu_r
being correct; the J = 0 branch is exponentially small by Hoeffding on the Bernoulli part and Chernoff on each
medium stage's count; given the branch, N_1 - nq = -+ A sqrt n - Delta + O(1) with Delta controlled by the
independence of B and M, Chebyshev, sup_b P(B = b) <= C/sqrt n and the LLT in the denominator. The triangular
LLT is justified by the atoms 0 and 1 carrying mass bounded below in every row. The law has rho = 1, no
exponential moment, finite variance, span one: it is inside the survey's framework and inside the hypothesis
of Thevenin's conjecture. With A = sqrt(q(1-q)) and eta < 0.38 the Gaussian N(0, pi_1(1-pi_1)) is excluded, and
letting eta -> 0 excludes every Gaussian. CLEAN.

Theorem B (nu = 1, sigma^2 = infinity, part (b)). The memo labels it a sketch; the label is right, and one
of its stated conditions is wrong. The rare route (one rare atom, bulk deviating by t_r = x_r sigma_r sqrt n)
costs about e^{-x_r^2/2} with x_r ~ a sigma_r/(pi_1(1-pi_1)) and sigma_r^2 ~ V_{r-1} ~ (log n_{r-1})^2/epsilon,
so its exponent is of order (log n_{r-1})^2. The bulk-and-medium route (supplying Sigma_r = sqrt n log n_r
outright) costs e^{-(log n_r)^2/(2 sigma_r^2)}, exponent epsilon (log n_r)^2 / (2 (log n_{r-1})^2). The memo
says the rare route dominates "as soon as log n_r >> log n_{r-1}, e.g. n_r = n_{r-1}^r". With that choice the
bulk exponent is epsilon r^2/2 against a rare exponent of order (log n_{r-1})^2: the bulk route wins by a huge
margin (checked numerically: at log n_{r-1} = 100, epsilon = 0.1, the bulk exponent is 1.2 to 20 for r = 5 to
20 against 10^4). The correct requirement is log n_r >> (log n_{r-1})^2, e.g. n_r = exp((log n_{r-1})^3); the
same fix is needed for the B_r-present and two-rare-atom routes. The construction is free to grow n_r that
fast and nothing else in the sketch is hurt (the cubic Cramer term only improves), so the gap is repairable,
but as written the sketch does not establish (b). The same remark applies to 20.3 (c) and 20.4's critical
infinite-variance clause, which cite Theorem B.

### 2.3 Hasebe-Ueda Problem 3.3 / I0086 and thirteen_settled sec. 11 -- CLEAN (given Lemma 3.1)

Re-derived: the level-set argument (three solutions of xi_R = 1/t force a separating local minimum with
xi_R(u_0) <= 1/t, including the tangential case); the sign of the second-derivative functional H (I first got
it wrong and the memo is right: xi_R''(0)/2 = int (3x^2 - s)/(x^2+s)^3 dmu); the pair weights p = bA^2/Delta,
q = aB^2/Delta from G = 0; the closed forms Phi and Psi by direct expansion; both reductions to (D, m); Lemma A
(Psi/D increasing in m, value (3D^2 - 4s)(D^2 + 4s)/16 at m = D^2/4); Lemma B (concave in s, endpoint values
m(1 + 3m - D^2) and (1 - D^2)(D^2 + 3)/16, the derivative (D^2 - 1)/2 at m = D^2/4); the Choquet step
(extreme points of {G = 0} carry at most two atoms, a single atom must be delta_0 with H < 0, straddling is
forced by the sign of G); and the equality case. Confirmed in sympy and by an independent scan
(min F = 1.0000 over 430,000 admissible pairs). The classical companion (t <= ab for a pair, ab <= D^2/4) is
four lines and also CLEAN; its kernel criterion psi(a) + psi(b) <= 0 is a pleasant general statement, with the
Cauchy value 2/sqrt 3 as a control.

Two things I could not check. (i) The whole argument runs through the source's Lemma 3.1 (unimodality iff
every level set of xi_R has at most two points); the memo validates it by reproducing Example 2.1 numerically,
which is good evidence but not a reading of the lemma. (ii) The claim that the printed "2 <= C" is a slip: the
Bernoulli example gives C >= 1 under D = diameter, but I cannot exclude that the paper normalises D_mu
differently. A paper should state C = 1 with D the diameter, cite Example 2.1 for the lower bound, and not
argue with the printed number. Prior-art risk: moderate-low; the constant 4 is repeated by the citing papers
the memo could reach.

### 2.4 Aldous-Janson Ansatz 20 and Open Problem 14 -- CLEAN as scoped, status word slightly strong

OP14: drawn(T) <= total leaf depth follows from h <= leaves - 1 (2 + |h_R - h_L| <= max(n_L, n_R) + 1
<= n_L + n_R), Lean-checked; then E[drawn] <= n E[depth of a uniform leaf] ~ (3/pi^2) n log^2 n by the
authors' Theorem 3. That refutes "roughly n log^4 n" provided Theorem 3 says what the memo says (it does:
E D_n ~ (1/(2 zeta(2))) log^2 n). The ranking's answer "Theta(n)" is not proved; O(n log^2 n) is. The
identified slip in heuristic (75) (a clade count n a(n,m) in place of (n/m) a(n,m)) is a convincing
diagnosis. Ansatz 20: both counterexamples are one line from a(n,n) = 1 and a(j) ~ (6/pi^2) log j / j,
provided the source's a(n,j) counts the starting state as visited; the five-problems memo's recursion
reproduces a(2) = 6/pi^2 and a(5) = 0.3166 from that convention, which is reassuring but not a reading of the
definition.

### 2.5 RRT layers / H0019 -- CLEAN

Theorem 1 re-derived: F_i(y) = P(M_i > y) satisfies F_i(y) = exp(-int_0^y (1 - F_{i-1})) by the Poisson
product formula, with the integral cut at y because M_{i-1} >= 0, and F_0 = 0 on [0, infinity); this is the
paper's recursion with u_i = 1 - s_i, so s_k(y) = P(M_k <= y) and l-bar_k = E e^{-M_k}. Sanity: s_1 = 1 - e^{-y},
l-bar_1 = 1/2. The dictionary is even more transparent than the memo makes it: the PWIT is the Yule-tree
embedding of the RRT (each vertex's children are born at a rate-one Poisson process after its own birth), so
M_k is the birth time of the first generation-k vertex and the RRT height at time t is max{k : M_k <= t}. The
exponent bookkeeping checks: the many-to-one function is 1/theta, the velocity 1/e is attained at theta* = e,
so the Bramson term is (3/(2e)) log k and the left tail has rate e, which is why c_1 = 2 < e gives the uniform
exponential moment and hence both the two-sided bound (Theorem 2) and, with Aidekon's convergence in law, the
genuine limit constant (Theorem 3). Theorem 4's combinatorial half (layer = second-largest branch height, max
layer = floor(diam/2)) is standard and brute-force checked. The proof is complete given Addario-Berry-Ford
Theorems 1.1-1.2 and Aidekon 2013 as quoted; I did not open either paper. The maximum-rank half of Conjecture 2
is untouched, as the memo says.

### 2.6 Janson Conjecture 20.1 / F0063 -- CLEAN

Re-derived formula (2) from the Dwass cycle lemma (a forest of l GW trees has total size M with probability
(l/M) P(S_M = M - l)), the two bounds (3) and (4), Minkowski / Jensen for the generation moments, and the
split at N_k <= n/2. The one-moment cost of size-biasing by l_k is exactly E xi^{r+1}, and the tail
E[Z_j^{r+1}; Z_j > n/(2k)] -> 0 handles the other half. Together with the survey's Fatou cases this proves
the conjecture for every real r >= 1 and for r in (0,1) with finite variance. The remaining case (r < 1,
sigma^2 = infinity) is correctly identified.

### 2.7 Janson 18.x group

18.4 / F0055 -- CLEAN. The comparison relation (turn j empty boxes into singletons, append an empty box)
gives Z_{m-j,n-1}/Z_{m,n} <= (1/w_0)(w_0/w_1)^j (2m/n)^j for m <= n/4; with w_j <= Phi(r) r^{-j} the tail
P(Y_(1) >= k) <= n C q_n^k/(1 - q_n), q_n = 2m/(gamma r n) -> 0, so Y_(1) = O_p(log n / log(n/m)). Elementary,
Lean core for the binomial ratio, exact numerics. The w_1 = 0 extension is only outlined.

18.30 / F0058 -- (ii) CLEAN: the three size relations, the three-range LLT, Bernstein, and the route
comparison (rare-A route c/(20 Lambda s) against e^{-Lambda^2/3} and e^{-Lambda^2/12}) all check, and the
double-exponential-versus-exponential balance (R2) is real. (iii) is a sketch with one more Poisson factor;
its Bernstein step needs the bulk atoms (bounded by about 10 r^3 s_{r-1}, not n_{r-1} as the memo loosely
says) to satisfy b k r << s, which the growth condition n_r >= r^12 n_{r-1} delivers. The exact toy is the
right control. Status "complete at sketch level" is fair.

18.41 / 18.42 / F0061-F0062 -- Theorem A CLEAN (case 1 and case 2 bounds and the final 2^{m+n} e^{-m^3/128}
comparison re-derived; the exact partition-function check at m = 64, 128, 256 corroborates). Theorem B
(monotone weights, cliff staircase) is plausible and numerically confirmed; I did not re-derive the Fuk-Nagaev
bookkeeping.

18.40 / F0060 -- the answer NO stands, the theorem overclaims. The per-ball rate F, the multinomial
count (I checked that the entropy term is favourable: r_k log(n/r_k) <= r_k log(nk/m) since r_k k <= m), and
the chaining of (4) across multiplicative blocks all work (the chaining is cleaner stated for
M(t) = max_{s <= t} F(s): M(t) - M(epsilon t) <= C/sqrt(epsilon t) for all large t, whose geometric sum is
bounded). So for every epsilon there are infinitely many records m at which the single-box configuration beats
every configuration with all boxes <= epsilon m, hence P(Y_(1) > epsilon m) -> 1 along a subsequence and
Y_(1)/n does not tend to 0 in probability. But the clause "P(Y_(1) = m) -> 1" needs the single box to beat
configurations with largest box in (epsilon m, m), and "m is a record" gives only F(m) > F(s), not a gap of
order 1/sqrt m: the configuration (m - 1, 1) has weight n(n-1) w_{m-1} w_1 against n w_m, and a record
guarantees f(m) - f(m-1) -> infinity but not f(m) - f(m-1) >> log n. So the theorem should read
"P(Y_(1) > epsilon m) -> 1 along a subsequence", which is what the problem needs; the remark that Y_(1)/n -> lambda
along that subsequence is not established. Also (4) and (3) share a constant C, so the violation of (4) gives
only e^{(C - C) sqrt m}; take 2C in (4). Cosmetic.

### 2.8 Aldous-Fill 4.48 / P0243 and 4.45 / P0242 -- CLEAN, exact

4.48(a): trace 2 + 2 epsilon and minor sum 1 + epsilon + epsilon^2 give tau_0 = (2 + 2 epsilon)/(1 + epsilon
+ epsilon^2) < 2; as epsilon -> 0, d-bar(t) -> P(Gamma(2,1) > t) = e^{-t}(1+t) uniformly on compacts and
tau_1 -> 2.1462. My recomputation (30-digit-free, plain expm and bisection) reproduces every printed value:
1.981982 / 2.010072 at epsilon = 0.1, ratio 1.08739 at k = 4. 4.48(b): the eigenfunction identity
u_i = lambda_2 sum_j x_j u_j from optional stopping (justified by E U < infinity and bounded u, Qu) gives
E_{i*} U >= 1/lambda_2 at a maximiser of |u|. CLEAN, and a random-chain control gave max tau_2/tau_1^(2) =
0.99993. 4.45: my sympy recomputation returns 149731115/63193903 and 346900/114917 exactly, ratio 1.27404, and
the induced rates 1, 110/227, 1/10219, 10/929 as printed. Literature risk: the 4.48(b) argument is a
one-paragraph eigenfunction bound and Lovasz-Winkler's DIMACS survey is exactly where it would live; check it
before claiming.

### 2.9 Agresti-Veraar / thirteen_settled sec. 4 -- CLEAN mechanism

Re-derived by Ito: Y = 1/U gives dY = (-Y + 3/Y) dt - sqrt2 dW; V = e^t Y gives dV = (3 e^{2t}/V) dt - sqrt2 e^t dW;
s = (e^{2t} - 1)/2 and R = V/sqrt2 give dR = (3/(2R)) ds - dW-tilde, a BES(4). Then sup_{t <= T} U_t^2 >=
1/(2 inf_{s <= S} R_s^2) and P(inf R <= x) >= c_S x^2 (4-d Brownian motion hitting a ball, capacity scaling), so
E sup U^2 = infinity for every T. Problem 5 follows. What I cannot check is scope: that the constant-in-space
solution of du = (Delta u + u - u^3) dt + gamma u^2 dW at gamma^2 = 2 is the variational solution of their
Theorem 6.4 with u_0 = a in L^2(Omega; H). The authors' own words quoted in the memo suggest it is.

### 2.11 Lyons-Peres 17.18 -- CLEAN

The stationarity step, which the campaign's proof left implicit, re-derives: given the children's colour
vector the child subtrees are independent GW(. | colour = c_k), the uniform choice among the children of the
root's colour returns GW(. | colour = c), and mixing over c with P(c) = 1/2 = P_GW(colour = c) returns GW.
The colour exists because q_n is a bounded martingale with E q_n^2 = r_n -> 1/2 (the recursion
r_{n+1} = 3/10 + (3/5) r^2 + (2/5) r^3 increases from 1/4 to the fixed point 1/2). Unanimity is preserved by
AND and OR, so every vertex has a child of its own colour. The root colour is invariant along the chain and
non-constant: no ergodicity. The stationary measure is GW itself, so "equivalent" is met trivially. A genuinely
nice construction; the literature to check is tail-measurable colourings of GW trees.

### 2.13 Hasebe-Ueda-Wang 4.7 -- CLEAN

With r = e^u and atoms e^{+-a} the integrand is exactly K_R(u -+ a) = 1/(2(cosh(u -+ a) - cos R)); choosing R in
[pi/2, pi) with R / sin R = t/10 (possible iff t >= 5 pi) makes the right side 1/10; F_R(0) <= 1/(2 cosh a) =
10/101 < 1/10 and F_R(+-a) >= 1/(4(1 - cos R)) >= 1/8 > 1/10, with decay at infinity: four roots. Uniform in R.
Correct given their Lemma 4.1(3). A two-atom law is the first thing anyone would try, so the prior-art risk is
the highest of the CLEAN items.

### 2.15, 2.18 Smaller items

Neri-Pinto: the witness arithmetic (w-tilde R = (0, 16, -7, -7, -2), Q = 6) checks by hand; p = d never works
because the all-ones vector is annihilated by the row-sum constraint. Kumar-Duddala: the inversion is real
(a mean-zero martingale with a nonnegative limit cannot be UI unless the limit vanishes). Levy drift H0013:
Theorem 2's local lower bound B_l(tau) >= e^{-4 delta} tau^{2 - 2 delta} e^{m - O_1 - O_2} and the Borel-Cantelli
count of good intervals (expected number ~ 2^k m_k^{-alpha}, geometric) re-derive; its use of the "min(B_l, B_r)"
criterion is imprecise in general (the two-sided Hardy condition is a split-point condition, not a pointwise
minimum) but immaterial here because B_r is identically infinite for w_1. Theorem 3 is a sketch. Frog model
H0024: Proposition 1 is fine; Proposition 2's extinction half is open by the memo's own statement and the
numerics cannot separate critical from supercritical at c = 1, so this row is a reduction with strong evidence,
not a correction. MMPP 4.2 (E0078): the periodic-Cox theorem is a three-line argument I re-derived (g(0) = g(T)
= 1, g > 1 in between by strict Jensen, hence g' < 0 somewhere, hence the order fails there); the 24-state
witness carries an exact rational certificate. It should be in the table.

### Items not re-derived

Janson 18.9, 18.10, 18.39; Aldous-Fill 4.30 and 7.27 (Lean file read, arithmetic core certified; the
arc-transitivity of C_m[K-bar_2] is immediate: D_m on the base times independent twin swaps acts transitively
on arcs); Rozikov; Khoshnevisan; Leskela Problem 3; Salez (retired); Konstantopoulos; Pollett; Bradley. The
ProofNet24 tracks claim no closed problem and I concur with the ranking's treatment.

## 3. Top three candidates for a stand-alone paper (Kalai excluded)

**1. Sharp constants for unimodality of free and classical Brownian motion with a compactly supported initial
law (Hasebe-Ueda 3.3, C = 1, and the classical D^2/4; memos I0086 and the classical companion).** Importance
moderate, completeness the best in the campaign: two independent proofs of the free bound (moment inequalities
with the Jensen step, and the Choquet two-atom reduction with Lemmas A and B), the classical companion by the
same reduction, the extremal measure identified with a rigidity statement, and a kernel criterion
psi(a) + psi(b) <= 0 that recovers the classical two-Gaussian and two-Cauchy thresholds as controls. The
Lean-checkable core is unusually clean: Lemmas A and B are real-polynomial inequalities in (D, m, s) on a box,
within reach of `nlinarith`/`polyrith`, and the classical pair inequality t <= ab <= D^2/4 is trivial to
formalise; the Choquet reduction and Biane's criterion would remain as cited inputs. Verifiability is high (the
end-to-end density computations sit far below the bound except at the extremal law, which sits on it to five
places). Risks: the criterion is the source's Lemma 3.1, which should be re-read from the paper before
submission, and the paper should state the sharp constant and cite Example 2.1 for the lower bound without
discussing the printed "2 <= C". A short paper for a free-probability venue.

**2. Conditioning at a point where the mean sits outside the bulk: lacunary offspring laws and the
non-normality of outdegree counts (Janson 20.2 Theorem A, with 20.3(d), 20.4's subcritical clause, 18.30(ii),
18.41-18.42, 18.4 as the surrounding material).** This is the package with the most importance: it refutes the
closing conjecture of Thevenin (EJP 2020) in its subcritical half with a complete elementary proof, answers
Problem 20.2(c) and two of the survey's condensation problems by the same mechanism, and adds a proof of
Conjecture 18.4. Completeness is uneven and the paper must be honest about it: Theorem A, 18.30(ii), 18.41 A,
18.42 A and 18.4 are complete; Theorem B (the critical infinite-variance half, i.e. 20.2(b)) needs its growth
condition corrected to log n_r >> (log n_{r-1})^2 and its lattice moderate-deviation expansion written out, and
18.30(iii) needs the same treatment or should be presented as a conjecture with the exact toy. Verifiability is
medium: the tools are a triangular-array LLT, Hoeffding, Chernoff and Bernstein, all standard but with
bookkeeping a referee will want to see; Lean can certify only the finite parts (the 18.4 binomial ratio is
already done; 18.42's explicit configuration inequality is finite arithmetic and could be). Prior-art risk is
moderate: lacunary constructions are in the spirit of Janson's Examples 18.36-18.37 and someone may have
noticed the two-atom mechanism, but the Thevenin conjecture is stated as open and I found no refutation cited
anywhere in the record. If only one of the three is to be written, this is the one with reach; if the aim is a
paper that can go out this month, it is the third.

**3. The layer distribution of random recursive trees is the minimum of a branching random walk with
exponential steps (arXiv:2608.04303 Conjecture 1 and the layer half of Conjecture 2; memo H0019).** A short
note with one idea, and the idea is decisive: the leaf-stripping recursion of the source is the distribution
function of the minimum of the Poisson-weighted infinite tree (equivalently, the birth time of the first
generation-k vertex in the Yule embedding), after which Addario-Berry-Ford give the conjectured front with
velocity selection included and Aidekon gives a genuine limit constant, which is more than was conjectured;
the maximum layer follows from the height via layer = floor(diam/2) and the two linear-size root subtrees.
Completeness is high given two published theorems; verifiability is high (recursion integrated against two
exact values, a recursion-free Monte Carlo of the tree agreeing at five digits on the exponential moment);
the combinatorial half (layer = second-largest branch height, max layer = floor(diam/2), drawn from the
literal stripping) is Lean-formalisable. Importance to the random-trees community is moderate and to the
posers, who state velocity selection as open, direct. Prior-art risk is low-moderate: the Yule/BRW dictionary
for RRT heights is classical, so a referee may ask whether the layer identification was noticed before; a
search of the "leaf-stripping / k-core of random trees" literature is the remaining step. The rank half of
Conjecture 2 should be stated as open.

Runners-up: the Agresti-Veraar refutation (already packaged with a partial Lean file; its one risk is scope,
section 2.9) and the Aldous-Fill quartet (exact, Lean core, but peripheral questions and a literature risk on
4.48(b)). The MMPP 4.2 refutation would fit as a section of a queueing note rather than a paper.

## 4. Summary of disagreements with the draft

The draft's conclusion (Hasebe-Ueda 3.3 for strength, Janson 20.2 for importance) survives review, with one
correction each: the Janson 20.2 record proves part (c) and only sketches part (b), and the sketch's growth
condition is wrong as stated; the Hasebe-Ueda record depends on the source's Lemma 3.1 and should not lean on
the "printed slip". Kalai should be 4/4 rather than 5/3. The 18.40 theorem and the frog-model row overstate
what is proved. The MMPP 4.2 refutation is missing from the table. Lyons-Peres 17.18 is under-rated.
