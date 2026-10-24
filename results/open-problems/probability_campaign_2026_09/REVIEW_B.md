# Reviewer B: adversarial referee report on RANKING.md (probability campaign, September 2026)

Written 2026-09-14. Method: I read RANKING.md, INDEX.md, the ProofNet24 inventory, the memos of the top eight
ranked items and of five Tier-2 items, the three Lean cores (P0340, F0055, P0208) and the Codex proof P0341.
For every proof I tried to break it before rating it: re-deriving the load-bearing inequalities by hand, checking
that each cited theorem is used inside its hypotheses, running the campaign's own check scripts, and, where I could,
writing an independent check with a different method (not the memo's script). Verdict words: CLEAN = the argument
re-derives in full; SOUND = re-derives except for a source quotation or a cited theorem I could not open;
SKETCH = a real gap the author labels; DEFECT = a real gap the author does not label.

Scripts run (all under a minute, none in the background), with what they printed:

- `free_unimod_lemmas_sym.py`: both closed-form identities hold; Lemma A root s = 3D^2/4; Lemma B endpoint values
  m(3m+1-D^2) and (1-D^2)(D^2+3)/16 with slope (D^2-1)/2 at m = D^2/4. Matches the memo.
- `toy_202_bimodal.py sub 3.0`: branch weights 0.4976 / 0.5024, N_1 pinned at 2000 -/+ 190, P(|z| <= s0) = 0.000
  against 0.683 Gaussian. Matches.
- `h0019_layer_identity.py`: 0 failures on both combinatorial claims, P5 control returns 2. Matches.
- `af445_exact.py`: induced tau_1^(2) = 346900/114917, ratio 419679620/329408453 = 1.27404; second witness 1.48220. Matches.
- `p0243_verify.py`: k=4, eps=1e-5: tau_0 = 4.00002, tau_1 = 4.351990, ratio 1.08799; all rows match the memo table.
- `check_1841_np.py 1.0`: J=8 cliff P(Y2 >= 32) = 0.9999 against 0.0024 without the cliff; J=10: 1 against 9e-5. Matches.
- `toy_1830_iii.py` (default arguments, bulk 1/4,1/4): P(#C = 0..3 | S=m) = 0.074, 0.318, 0.390, 0.180 - this is the
  "comparable scale" regime the memo describes (3 top atoms, not 0). With the memo's stated parameters
  (`toy_1830_iii.py 40 0.02 0` and `60 0.02 0`): P(#C=0)=1.0000, P(one A box)=1.0000. Matches once the right
  arguments are used; the memo should record them.
- `toy_1830.py`: three rows, P(Y(1) >= L_A | S=m) = 0.9999, 1.0000, 1.0000 against n P(xi >= L_A) = 0.10, 0.10, 0.06. Matches.
- Neri-Pinto witness, my own numpy: row sums all 6, Q(w) = 6 > 0, lambda_max(G) = 1.9779, irreducible. Matches.
- Independent Hasebe-Ueda scan (my code, random 2-4 atom measures of diameter 1, 1500 x 8 radii): smallest
  separating local minimum of xi_R = 1.1285 >= 1. Consistent with the proposition.
- Independent RRT check (my own PWIT simulation, not the recursion): k=3,5,7, P(M_k <= y) and E e^{-M_k} agree with
  the paper's recursion within 1.5 standard errors (e.g. k=7: 0.1495 vs 0.1495; E e^{-M} 0.02651 vs 0.02616).
- Exact largest-box law for a dense-support rho = 0 sequence (my code, see item 7 / 18.40): P(Y(1) = m) = 0.0000 at
  m = n = 50, 100, 200, 300 while P(Y(1) >= m/2) -> 1. This is the one defect I found in a "PROVED" item.
  Positive control of the same code on the memo's own Example 18.38 (factorial support): E Y(1)/n = 0.240 at
  n = 100 and 1.000 (P(Y(1)=m) = 1.0000) at n = 120, exactly the memo's table, so the dense-support result is
  not an artefact of my convolution.

## Part 1. Attacks on the top eight

### 1. Kalai Conjecture 8 / GPS open problem 1 (F0090) - SOUND, already public

Attack points and what survived. (a) The coding bound (1): four bits per hit square at each dyadic scale, a bounded
number at the finest scale; the decoder always knows how many bits to read; Shannon gives H(A) <= expected length.
Clean. (b) The one-scale sum (2)-(4): the split of Lambda_B into a four-arm event in the disc of radius d/2 and a
three-arm event in the half-annulus 2d to D/2, bounded by the line of the nearest side. I checked the geometry: the
three arms to the far sides leave the half-disc of radius D/2 (D is the distance to the second nearest side, so
the half-disc is inside Q_R), their colours alternate (open, closed, open) so the polychromatic half-plane
three-arm exponent 2 applies, and the two regions are disjoint so the product bound holds. The dyadic count
C(d/r)(D/r) and the two geometric sums are right; the quasi-multiplicativity direction alpha_4(r,d) alpha_4(d,R) <=
C alpha_4(r,R) is the right one. (c) Step 3 uses alpha_4(1,R) >= c alpha_4(1,r) alpha_4(r,R) and r^2 alpha_4(1,r)
>= c r^eps, both GPS (2.6). Clean. What I could not open: the exact form of GPS Lemma 3.2 (the constant 4 and the
quad version); the memo's Codex reader confirmed it and the argument does not depend on the constant. The result is
stated for the square only, which is the honest scope. Status word PROVED is earned for the square. Not a paper
candidate here (posted by the author on 2026-09-13).

### 2. Janson Problem 20.2 (b),(c) and Thevenin's closing conjecture (F0064) - Theorem A CLEAN, Theorem B SKETCH

Theorem A (subcritical, nu < 1). I re-derived: the outdegree-multiset / allocation B_{n-1,n} identification
(survey Section 15); J <= 1 from 2 L_r^- > m (needs q < 1/2, which is assumed); the branch weights through the
lattice LLT for a triangular array (summands bounded by n_{r-1}, variance in [q(1-q), q(1-q)+V], Lyapunov ratio
n_{r-1}/sqrt(n_r) -> 0 by n_{r+1} >= n_r^4, characteristic function bounded away from 1 off the lattice by the
atoms 0 and 1); the J = 0 branch through Hoeffding on the bulk and a Chernoff bound on the medium stages with k >=
n_r^{1/2}; the conditional control of Delta by the sup_b P(B = b) <= C/sqrt(n) trick (I checked the inequality
P(B+M=c, |Delta|>t) <= sup_b P(B=b) P(|Delta|>t)); and V < eps by taking n_1 large. Every hypothesis of Thevenin's
conjecture is met: no exponential moment (rho = 1), finite variance, mean nu in (q,1), span one. One subsequence
suffices to refute convergence in law. The exact toy reproduces the two-point law. Status: (c) answered NO, and the
subcritical half of Thevenin's conjecture is refuted - earned.

Theorem B (critical, sigma^2 = infinity). Sketch only, and the sketch has a real dependence: a lattice local
moderate-deviation expansion with the remainder tracked in a triangular array, plus the "equal-weight device"
that fixes p_r^+ : p_r^- by the exact bulk probabilities. The toy for this case gives branch weights 0.986 : 0.014,
not 1 : 1, and the memo explains this by the cubic term and says the device removes it; that is plausible but
unverified. So Problem 20.2(b) - the more natural of the two questions - is NOT proved here. The ranking's
"NO in general ... 20.3 and 20.4 answered the same way" inherits this: the critical infinite-variance halves of
20.3(c) and 20.4 rest on Theorem B. Recommend the status line say "(c) refuted; (b) refuted at sketch level".

Importance: a stated conjecture in a well-read survey plus an explicit 2020 conjecture, but the refuting mechanism
(a lacunary law with two rare atoms) is of the kind specialists expect to break regularity-free statements
(Janson's own Examples 18.36-18.37 are in this spirit). I put importance at 3.5, not 4.

### 3. Hasebe-Ueda Problem 3.3 (I0086) - CLEAN

I re-derived everything. From G = 0 the pair weights are w_a : w_b = bA^2 : aB^2 (Delta = bA^2 + aB^2); then F - 1 =
[bA(1-A) + aB(1-B)]/Delta and H = [bB(3a^2-s) + aA(3b^2-s)]/(Delta A B) exactly as stated; the D, m collapses are
confirmed by sympy (run above). Lemma A: Psi/D increasing in m (derivative 6m+6s > 0), at m = D^2/4 equals
-(s - 3D^2/4)(s + D^2/4), so Psi >= 0 forces s <= 3D^2/4. Lemma B: concave in s, s = 0 gives m(3m+1-D^2) >= 0, s =
3/4 gives 3m^2 - m(D^2 + 1/2) + 3/16, convex in m with slope (D^2-1)/2 <= 0 at m = D^2/4, value (1-D^2)(D^2+3)/16 >= 0.
Choquet step: probability measures on a compact set with one linear constraint have extreme points on at most two
points (Winkler); single atoms must sit at 0 (G(delta_x) = 0 iff x = 0) and have H = -1/s^2 < 0; F, G, H are
continuous linear functionals so they integrate over the decomposition. The logic "some extreme point has H >= 0,
hence s <= 3/4, hence every extreme point has F >= 1, hence F(mu) >= 1" is right and I like that Lemma B does not
need the pair's own H. Equality rigidity: F(mu) = 1 with F(kappa) >= 1 for all kappa forces every kappa in the
decomposition to be the equality pair, so mu is a symmetric two-point law; and at that configuration H = 0 and
the point is a strict maximum, so unimodality holds at t = D^2 exactly, which is why "t >= D^2" (closed) is right.
My independent random scan found no separating minimum below 1.1285. The classical unimodality-criterion
positive control (Bernoulli threshold t = 4 reproduced from the criterion) covers the one thing I could not open,
the exact wording of their Lemma 3.1. Status PROVED earned; C = 1.

Two cautions for a paper. (i) The remark that the source prints "2 <= C <= 4" must be checked against the PDF
before it is repeated; the memo itself says the printed 2 might be a D_mu-versus-D_mu^2 slip. State it once,
neutrally. (ii) The classical companion (mu * N(0,t) unimodal for t >= D^2/4, sharp) is almost certainly KNOWN:
a location mixture of normals with common variance sigma^2 whose means lie in an interval of length 2 sigma is
unimodal is a classical statement in the mixture literature (Eisenberger 1964 for two components; Kakiuchi 1981
and later for general mixing laws). Do not present it as new; cite it as the classical analogue.

### 4. Aldous-Janson Ansatz 20 and Open Problem 14 (P0341, P0340) - OP14 CLEAN, Ansatz 20 SOUND WITH ONE OPEN READING

OP14. drawn(T) <= sum of leaf depths is kernel-checked (P0340.lean: height + 1 <= leaves, sumDepth shift, the
inequality, the exact decomposition; axioms standard). E[sum of leaf depths] = n E[depth of a uniform leaf]. Their
Theorem 3 gives E[depth] ~ (1/(2 zeta(2))) log^2 n; I re-derived the constant from the descent chain: the jump from
m to m-k has law 1/(h_{m-1} k), so E log(m/X) ~ zeta(2)/log m per step and d(log^2 m) = -2 zeta(2) per step,
hence D_n ~ log^2 n/(2 zeta(2)) = 3 pi^-2 log^2 n. So L_n = O(n log^2 n) = o(n log^4 n), and the simulation puts it
at Theta(n). The "log2 vs log^2" extraction trap is real and correctly resolved. REFUTED earned.

Ansatz 20. Both the Codex proof and the memo quote the Ansatz with the sum over i <= n, and the refutation is the
single fact a(n,n) = 1. That is so trivial that I want the range of summation verified against the PDF (v3,
pp. 39-40) before this is published: if the paper's sum runs over i < n, or over i in a fixed window, the
root-charging test functions do nothing (a(n, n-1) ~ 1/log n, a(n, n/2) = O(polylog/n)), and the refutation
collapses. The ledger's own statement_caveat ("the full source ansatz permits bounded sparse functions") argues
for the memo's reading but is not a quotation. This is the one item where the status word depends on a sentence
I could not see. If the reading holds, the refutation is CLEAN and a one-page note; the reviewer should also note
that Brandenberger-Chin-Mossel (arXiv:2505.24821) prove a decaying-test special case, which must be cited.

### 5. arXiv:2608.04303 Conjecture 1 and the layer half of Conjecture 2 (H0019) - CLEAN

Theorem 1 (recursion = PWIT minimum): the Poisson product formula gives F_i(y) = exp(-int_0^y (1 - F_{i-1})) with
F_{i-1} = 1 on the negative axis; this is the paper's recursion for 1 - s_i; F_0 = 0 = 1 - s_0. Clean, and my own
tree simulation (no recursion in it) agrees at k = 3, 5, 7. Theorem 2: Addario-Berry and Ford's class is exactly
"displacement vector (v_1, v_2, ...) with v_j the sum of j independent Exp(1)", and their abstract names the
Poisson-weighted infinite tree; Theorem 1.1 gives median = n/e + (3/(2e)) log n + O(1), Theorem 1.2 the uniform
tails. I checked the speed and the tail exponent from first principles: Lambda(theta) = -log theta gives theta* = e,
v = 1/e, so the left tail decays at rate e, and c_1 = 2 < e is legitimate for the exponential moment. Theorem 3:
Aidekon needs the boundary-case normalisation and X (log X)^2 moments for X = sum e^{-e xi_j}; with Poisson points
these are finite, the walk is non-lattice, and Addario-Berry-Ford's Remark 2 says the same. Uniform integrability
from the uniform tail is right. Theorem 4: layer(v) = second largest branch height and max layer = floor(diam/2)
are brute-force checked and I verified them on P5 by hand; the root's two largest subtrees are linear w.h.p. and
are RRTs given their sizes; the diameter lower bound follows. PROVED earned for Conjecture 1 (in the stronger
limit form) and the layer half of Conjecture 2; the rank half is untouched and the memo says so.

Prior-art risk: moderate. The RRT-height / PWIT dictionary is well known (Devroye; Addario-Berry-Ford), and
leaf-stripping ("peeling", "k-core" of recursive trees) has a literature; someone may have written the recursion
as a BRW before. The physics authors did not. Worth a targeted search before submission.

### 6. Janson Conjecture 20.1 (F0063) - CLEAN

I re-derived formula (2) directly (cycle lemma for the forest of ell subtrees, (ell/M) P(S_M = M - ell), against
(1/n) P(S_n = n-1) for the tree), the two bounds (3) and (4) (n - N >= ell is what turns (3) into (4)), the moment
bounds (5) by Minkowski and Jensen, and the split at N_k <= n/2: on the small side W_n <= 2^{3/2} C' Z_k gives a
K-tail of Z_k^{r+1} uniform in n; on the large side n^{3/2} Z_k^{r-1/2} with Z_j > n/(2k) for some j < k, and
Z_j^{r-1/2} <= (2k/n)^{3/2} Z_j^{r+1} cancels the n^{3/2}. The hypothesis E xi^{r+1} < infinity is used exactly once
per side. The one point a referee will raise: for n - N small the LLT bounds are used only in the trivial
direction, which the memo says. PROVED earned for real r >= 1 (and r in (0,1) with finite variance); the open
case is stated. Prior art to check: Addario-Berry, Devroye and Janson (2013) and Devroye-Janson (2011) give
width/profile tail bounds; the fixed-k moment convergence may be derivable from them.

### 7. Janson Problems 18.30, 18.41, 18.42, 18.40, 18.9, 18.4, 18.10, 18.39 - one DEFECT, the rest CLEAN/SOUND

18.30(ii) (F0058 Theorem 1): CLEAN. I checked (R1)-(R3) from the definitions, the three ranges of the
characteristic-function integral (the atom 0 with mass >= 1/3 and the atoms 0,1 give the off-lattice bounds), the
landing point m - L_A at s/10 from the mean via n p_{2r-1} L_A = delta L_A = s/10, and the ratio of routes
(a)+(c) to (b) through (R2). The h(n) = n^2 extension off the subsequence is right (Markov). Toy reproduced.
18.30(iii) (Theorem 2): SKETCH, exact toy reproduced with the memo's parameters. Both parts answered NO - earned
for (ii), sketch-level for (iii).

18.42 (Theorem A): CLEAN. I re-derived every constant: S(a*) = (8^{i+1}-1)/7, S(b*) = (8^i-1)/7, Q lower bound
m^2/4 - 5m/2 + 1, Case 1 total < 1.48 8^{i-1}, Case 2 dust <= (25/24) 8^{i-2} (t = 7 maximises 8t/7 + (8-t)/3),
the gap 1361/168 8^{i-2} > m^3/64, and m >= 64 suffices. Configuration count 2^{m+n}. The hypothesis
w_{k+1}/w_k -> infinity holds; m/n -> lambda for any fixed lambda. NO earned.
18.41 (Theorem B): CLEAN modulo the Fuk-Nagaev form, which I checked is the truncated Bennett bound. I verified
the three exponents: W(A_0) ~ n^{-11.9}, W(A_1) ~ n^{-7.65} + n^{-7.22}, W(A_2) >= c n^{-5.656}, using e^{3J} ~
n^{4.328}; the A_1 second part wins by only n^{-0.57}, which is enough. Numerical check reproduced. NO earned.

18.40 (F0060): DEFECT. Inequality (3) - "a mixed configuration cannot beat the best pure one, up to O(sqrt m)" -
is false as stated: the count of allocations with a given multiset of box sizes is n!/((n-r)! prod mult_j!) and,
while this is at most prod_j C(n, r_j), each factor C(n, r_j) w_{s_j}^{r_j} has per-ball rate F(s_j) + log(1/theta_j)/s_j
where theta_j is the fraction of balls in that size, not F(s_j). The extra log(1/theta)/s term is the entropy of
mixing, and for singletons (s = 1) it is Theta(m) when a positive fraction of balls are singletons. Concretely, a
giant of size m - j plus j singletons outweighs the single giant by about exp(j [log(en/j) + log w_1 - (f(m) -
f(m-j))/j]), which is maximised at j ~ n w_1 e^{-f'(m)} and gives a gain of that order - not O(sqrt m) unless
f'(m) >= (1/2) log m. The theorem's literal conclusion "P(Y(1) = m) -> 1 along records" therefore fails whenever the
support is dense and f(s)/s grows slowly. I checked this exactly: w_k = exp(k sqrt(ln k)) for k >= 2, w_0 = w_1 = 1,
m = n: P(Y(1) = m) = 0.0000 at m = 50, 100, 200, 300 (every large m is a record of F here), with the predicted dust
j ~ n e^{-f'(m)} = 5, 9, 16, 22 balls. The memo's own numerics never see this because its two test sequences have
sparse supports ({i!} and {2^j} with singletons), where the dust cannot form. The chaining step (4) needs the
per-ball error to be summable over multiplicative blocks (C/sqrt(x)); with the true error (of order e^{-F(x)} plus
log x / S) the chain gives only F(s_j) <= F(s_{j_0}) + C sum_k e^{-F(eps^k s_j)}, which is no contradiction for F
growing like log log s. The weaker conclusion that the ranking prints - Y(1)/n does not tend to 0, i.e. NO to
Problem 18.40 - may well be true (in my example P(Y(1) >= m/2) -> 1 and Y(1) sits near 0.8 m), but it is not
proved by this memo. Status should move from "answered: no" to "conjectured no; proof has a gap at (3)". This is
the one item whose PROVED/answered word is not earned.

18.9 (F0056): SOUND. Theorem 2 (w_1 = 0) is a parity triviality plus a tilt estimate, clean. Theorem 1 (w_1 > 0)
re-runs Janson's proof with a Poisson-regime LLT whose only new input is |phi(t)|^2 <= 1 - 2 pi_0 pi_1 (1 - cos t);
I checked the near-origin expansion and the eps_n = m^{-3/8} split; the rest is "verbatim from the source", which I
did not re-read line by line. Bounded m is correctly excluded. Answer earned.
18.4 (F0055): CLEAN; the comparison map (j balls of one box into j empty boxes) and its image/preimage counts are
right, the Lean core certifies the binomial ratio and the tail sum. PROVED earned; the argument is elementary
enough that it may be folklore for specific weights, as the memo says.
18.10 (F0057): SOUND. The sandwich inclusions and the inequality P(1 <= X < k, X + Y >= k) <= P(X >= 1) P(Y >= 1)
are right; the thin/fat/good/bad bookkeeping follows Janson's (vi). No numerics, no independent read; a careful
reader should re-walk Janson's pages 89-94 once more before this is cited as proved.
18.39 (F0059): reduction only, honestly labelled.

Group status: five CLEAN/SOUND answers, two sketches, one reduction, one DEFECT. Strength for the group 3.5, not 4.

### 8. Aldous-Fill 4.48, 4.45, 4.30, 7.27 (P0243, P0242, P0208, thirteen_settled sec. 5) - CLEAN

4.48(a): tau_0 = (2+2eps)/(1+eps+eps^2) < 2 from trace and minors; tau_1 -> root of e^{-t}(1+t) = e^{-1} = 2.146 by
the Gamma(2,1) limit; 30-digit verification reproduced (ratio 1.088 at k = 4). Uses Aldous-Fill's continuous-time
tau_1 with threshold e^{-1}, which is their definition. FALSE earned. 4.48(b): the eigenfunction/optional-stopping
argument is a paragraph and correct (E_i U < infinity justifies stopping; randomised U is fine in an enlarged
filtration). TRUE earned - but this is exactly the kind of bound that Lovasz-Winkler may already contain; treat
(b) as high prior-art risk. 4.45: exact rationals reproduced; K = 1 fails - earned; the K half is left open and
said so. 7.27: g(j) = j(m-j) + m solves the hitting system (I re-derived the twin value 2m and the fibre-average
boundary condition), tau_0 = (m^2-1)/6 + m by the cycle sum, tau_2 from A(C_m) tensor J_2; Lean core certifies the
algebra. REFUTED earned. 4.30: the compound-Poisson-with-vanishing-intensity mechanism is right and the identities
were checked to seven decimals; earned. Caveat for the group: C_m[K_2-bar] is a circulant that any expert would
write down in a minute, and 4.30 is the standard "a state of tiny mass breaks CLT rates" observation; importance 3
is generous but defensible because the questions are printed in a standard reference.

## Part 2. Tier-2 items I suspected were under-rated

- Lyons-Peres Question 17.18 (thirteen_settled sec. 10). The AND/OR colour: q_n is a bounded martingale by
  multilinearity (F(1/2) = 1/2), the second-moment recursion r_{n+1} = 3/10 + (3/5) r^2 + (2/5) r^3 has the exact
  factorisation and drives r_n to 1/2, so the colour is a genuine {0,1}-valued isomorphism-invariant function of
  the tree; every vertex has a same-coloured child; and the stationarity argument (the chosen subtree is GW
  conditioned on its own colour, mixed at 1/2 : 1/2 which is the GW colour law) is right. The stationary measure is
  GW itself, so equivalence holds trivially and ergodicity fails. This answers a question printed in the standard
  graduate text, with a construction that is short and checkable. Under-rated: importance 3, strength 4.
- Leskela Problems 1 and 3 (P0289, P0291). Problem 3's star-chain proof reduces to two finite inequalities with an
  exact rational certificate and LP controls; I checked the spectral reduction (two nonzero eigenvalues, the
  u -> 0 and u -> 1 conditions) and it is right. Problem 1 (Ross's second conjecture) now has a second reader's
  re-derivation of the light-traffic expansion with a rigorous uniform remainder (memo H_P0289 of 09-12), so the
  counterexample is no longer "mechanism verified, numbers unchecked". A stationary ergodic finite-state
  environment for which faster modulation raises the workload is a result queueing theorists would notice.
  Under-rated: importance 3, strength 4. Prior art (Heyman, Miyoshi-Rolski 2004) must be compared.
- Agresti-Veraar Problems 4, 5 (thirteen_settled sec. 4). I redid the Ito chain: Y = 1/U gives (-Y + 3/Y) dt -
  sqrt2 dW, V = e^t Y gives 3 e^{2t}/V, the time change s = (e^{2t}-1)/2 makes it (3/V) ds - sqrt2 dW-tilde, and
  R = V/sqrt2 has drift 3/(2R), i.e. BES(4). The tail P(sup U^2 > y) ~ 1/y follows from the x^2 small-ball
  probability of 4-dimensional Brownian motion. Clean, a manuscript and a partial Lean exist, the problem is from
  2025. Importance 3 is right; strength 4.5.
- Neri-Pinto Remark 3.7 (H0020): witness verified by my own arithmetic; p = d fails by the all-ones vector. Small
  but exact. Scores as drafted.
- Levy-drift compactness (H0013 Theorem 2): I checked Step 1's lower bound (the (tau+h)^delta - (tau-h)^delta
  <= 4 delta estimate) and Step 2's Borel-Cantelli over independent kept intervals. I also checked that the
  criterion is used only in the direction actually needed: a test function equal to the rho^{-1}-integral on
  [tau-h, tau], constant to a far cutoff N and decaying over [N, N+1] has Rayleigh quotient -> 1/B_l(tau) as N ->
  infinity because int_N^{N+1} rho -> 0, so Persson gives lambda_ess <= 1/B_l(tau_k) -> 0 without the Muckenhoupt
  "iff". Theorem 2 is CLEAN; Theorem 3 is a labelled sketch. Scores as drafted.

## Part 3. My scores for every row of RANKING.md (Importance / Strength, 1-5)

| Rank | Problem | Draft I/S | Mine I/S | Reason where I differ by >= 1 |
|---|---|---|---|---|
| 1 | Kalai Conj. 8 / GPS OP1 | 5 / 3 | 5 / 4 | The argument re-derives; one independent read exists; strength 3 undersells a complete proof. Already public, excluded from paper choice. |
| 2 | Janson 20.2 + Thevenin | 4 / 3.5 | 3.5 / 3.5 | Lacunary-law refutation is the expected mechanism; part (b) is a sketch. |
| 3 | Hasebe-Ueda 3.3 | 3.5 / 5 | 3.5 / 5 | Agree. Classical companion is likely known (see item 3). |
| 4 | Aldous-Janson Ansatz 20 + OP14 | 3.5 / 4.5 | 3.5 / 3.5 | OP14 alone is 4.5; the Ansatz refutation hinges on the unverified range of summation (i <= n), and it is too trivial not to check. |
| 5 | arXiv:2608.04303 Conj. 1, 2 (layers) | 3.5 / 4 | 3.5 / 4.5 | Every step re-derives; my independent simulation confirms the dictionary; cited theorems used inside their class. |
| 6 | Janson Conj. 20.1 | 3 / 4 | 3 / 4.5 | Complete and short; re-derives. |
| 7 | Janson 18.x group | 3 / 4 | 3 / 3.5 | 18.40's proof has a real gap ((3) ignores mixing entropy; literal statement false on a dense example); two sketches. |
| 8 | Aldous-Fill 4.48, 4.45, 4.30, 7.27 | 3 / 4.5 | 3 / 4.5 | Agree; 4.48(b) high prior-art risk. |
| 9 | Agresti-Veraar 4, 5 | 3 / 4 | 3 / 4.5 | Ito reduction re-derived; manuscript + Lean exist. |
| 10 | Salez 2.4 | 3 / 4 | 3 / 4 | Agree; retired. |
| 11 | Lyons-Peres 17.18 | 2.5 / 4 | 3 / 4 | Question in the standard text; construction re-derives. |
| 12 | Burdzy-Scheutzow 7.5 | 2.5 / 4 | 2 / 3.5 | Filling-scheme argument is classical (Thorisson); the L1 step is "checked by eye". Likely known. |
| 13 | Hasebe-Ueda-Wang 4.7 | 2.5 / 4.5 | 2.5 / 4.5 | Agree; I re-derived the four-root argument. |
| 14 | Leskela 1 and 3 | 2.5 / 4 | 3 / 4 | Ross's second conjecture is classical; Problem 1 now has a second reader. |
| 15 | Neri-Pinto 3.7 | 2 / 4.5 | 2 / 4.5 | Agree; witness verified. |
| 16 | Rozikov 3, 4, 10, 11 | 2 / 4 | 2 / 4 | Not re-read; no change. |
| 17 | Khoshnevisan OP 1, 3 | 2.5 / 3.5 | 2.5 / 3 | Only the night-report line was available to me; "audited line by line" by one agent, no memo with the mathematics in the archive I was given. |
| 18 | Kumar-Duddala 3.2; Levy drift 5.3(ii); frog 3.6 | 2 / 4 | 2 / 4 | Levy-drift Theorem 2 checked clean; the other two not re-read. |
| 19 | Pollett (ii); Bradley Q7; Konstantopoulos 2, 3 | 1.5 / 3.5 | 1.5 / 3.5 | Agree; Pollett probably known (Foley-McDonald), Bradley literal only. |

## Part 4. Top three candidates for a stand-alone paper (Kalai excluded)

1. Hasebe-Ueda Problem 3.3: the sharp constant C = 1 for unimodality of free Brownian motion started from a
compactly supported law, with the symmetric Bernoulli as the unique extremal. This is the strongest candidate on
every axis the brief names. Completeness: the whole proof is the source's own criterion, a two-atom extreme-point
reduction and two polynomial inequalities, and I re-derived each piece. Verifiability: Lemmas A and B are
statements about real polynomials in (s, m, D) on a box, which a proof assistant can certify outright
(polyrith/nlinarith or a Positivstellensatz certificate), and the Choquet step is a textbook theorem; so the Lean
core can be essentially the whole mathematics rather than an arithmetic fragment. Prior-art risk is low to
moderate (the 2018 source poses it as open, citing papers repeat 4). Importance is honest rather than large: a
sharp constant in a niche of free probability, but a clean, final answer with an identified extremiser. Two
things to fix before submission: check the printed lower bound against the PDF and state the correction once,
and present the classical D^2/4 companion as the known Gaussian-mixture fact it almost certainly is.

2. The layer distribution of random recursive trees (arXiv:2608.04303 Conjectures 1 and 2, H0019). The paper
would be short and its point is an identification rather than an estimate: the authors' leaf-stripping recursion
is the distribution function of the minimum of the Poisson-weighted infinite tree, so their travelling-wave
conjecture, velocity selection included, is Addario-Berry-Ford's theorem, and Aidekon upgrades the O(1) to a limit
with an explicit constant C* = E e^{-M*}. The layer half of Conjecture 2 follows with a two-line diameter argument.
Completeness is total given two published theorems, both used inside their stated classes (I checked the class and
the moment conditions). Verifiability is good but not Lean-shaped: the core is an integral recursion identity and
a Monte Carlo confirmation, and I reproduced the latter independently. Prior-art risk is moderate (peeling of
recursive trees has a literature and the PWIT dictionary is classical); a targeted search for "leaf stripping" /
"peeling" / "k-core" of random recursive trees is required and, if clear, the note is publishable and the authors
of the source would cite it. The rank half of Conjecture 2 is a natural follow-up to mention as open.

3. Agresti-Veraar Problems 4 and 5 (critical Allen-Cahn, Bessel-4 construction). A 2025 problem from active
authors, answered on the exact model they name as the one they cannot settle, by a reduction I re-derived: with
constant initial data the SPDE is a scalar SDE, and three changes of variable turn it into a BES(4), whose small-ball
probability x^2 gives E sup_t |u_t|^2 = infinity for every horizon and every positive constant datum. It is
complete, a manuscript and a partial Lean (EndpointCore.lean) already exist in publishability_20260910, and the SPDE
community would notice a negative answer to a stated energy-bound question at the critical exponent. Verifiability:
the Ito computations are mechanical and I confirmed them; the capacity estimate is textbook. Prior-art risk is the
main uncertainty - the scalar reduction is natural enough that a 2025-26 follow-up by the authors or others may
contain it - so a citation search of the 2025 journal version is the gating step. Runner-up, if the range-of-sum
check in item 4 passes: Aldous-Janson OP14 plus Ansatz 20, which is elementary, Lean-cored, and corrects a stated
rate in a paper by prominent authors; and, as a longer paper once 18.40 is repaired or excised, the Janson
condensation bundle (20.1, 18.30(ii), 18.41, 18.42, 18.4).

## Summary (10 lines)

1. Top eight re-read and attacked; scripts rerun where they exist, plus three independent checks of my own.
2. CLEAN: Hasebe-Ueda 3.3, RRT layers, Janson 20.1, Janson 18.30(ii), 18.41, 18.42, 18.4, Aldous-Fill group, Aldous-Janson OP14.
3. SOUND but with a source sentence I could not open: Kalai (already public) and Ansatz 20 (the sum's range must run to i = n).
4. SKETCH, honestly labelled: Janson 20.2 Theorem B (critical case), 18.30(iii), Levy-drift Theorem 3.
5. DEFECT: Janson 18.40 - inequality (3) ignores mixing entropy; the literal theorem fails on a dense-support example (P(Y(1)=m)=0.0000 at m=n=50..300); the answer NO is unproved.
6. Status words earned everywhere else; recommend 20.2 read "(c) refuted, (b) at sketch level" and 18.40 read "conjectured".
7. Scores: I lowered 20.2 (importance 3.5), the 18.x group (strength 3.5) and Ansatz 20 (strength 3.5); raised Kalai, RRT, 20.1, Agresti-Veraar, Lyons-Peres, Leskela.
8. Paper candidates: (1) Hasebe-Ueda 3.3 (polynomial core, Lean-certifiable in full); (2) RRT layers; (3) Agresti-Veraar critical Allen-Cahn.
9. Prior-art flags: the classical D^2/4 companion is likely known (Gaussian-mixture literature); Aldous-Fill 4.48(b) likely in Lovasz-Winkler; RRT peeling literature to search.
10. Nothing outside REVIEW_B.md was modified; no git was run.

(This was your ask: act as Reviewer B on RANKING.md - attack the top eight and three Tier-2 items, run the checks, rescore every row, name three paper candidates, and write REVIEW_B.md.)
