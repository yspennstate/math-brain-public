# Independent referee report: route U-universal

Referee: an Opus agent independent of the route's author, 12 October 2026.
Scope: every claim in `CLAIMS.json` marked PROVED or KNOWN, plus spot checks of the EVIDENCE claims that the
summary leans on. Verdicts: CONFIRMED, REFUTED (failing case), GAP (the step that does not follow),
UNCHECKED (reason). Full FEI remains OPEN; nothing in this route claims otherwise, and nothing below changes that.

My code is in `referee_code/` and imports nothing from the author's `code/`. Integer Walsh transforms are exact;
logarithms are float64 except in `mp_identities.py` (mpmath, 50 digits). Result files are the `*_results.json`
beside each script.

Status: FINAL for this pass (12 Oct 2026). Every PROVED and KNOWN claim is confirmed. No claim is refuted;
one statement needs n >= 2, and a few remarks need rewording (Sec. 5). Two new findings are in Sec. 4.3 and 4.4.

## 1. Verdict table

| id | claimed | verdict | one-line reason |
|---|---|---|---|
| U-Gkey | PROVED | CONFIRMED | parity of a sum of 2^{\|S\|} signs; exact check, 984,884 pairs n<=4, 0 violations; fails, as it must, on non-Boolean psi_n |
| U-G | PROVED | CONFIRMED | termwise consequence of U-Gkey plus H = E log2(1/pi) + U; exact equality on point defects (stronger than stated) |
| U-loc | PROVED | CONFIRMED | re-derived term by term; 50-digit check error < 1e-50; chain rules hold for arbitrary laws |
| U-comp | PROVED | CONFIRMED | upper sets factor through the composition law; 110 brute-force compositions, error < 2e-15 |
| U-G1G2 | PROVED | CONFIRMED | per-level Jensen and Gibbs with weights pi(S) lam^{\|S\|}; no violation n<=4; G1 exact on all symmetric f, n<=9 |
| U-GU-implies-FEI | PROVED | CONFIRMED | induction checked, including negative Delta_i U and b<0 |
| U-A | PROVED | CONFIRMED | each link re-derived; depends only on ER (E1, E3), both re-checked n<=4 |
| U-C | PROVED | CONFIRMED for n>=2 | item (ii) is false at n=1 (f=x_1, c_1=0); (vi) is conditional on RM sec. 2.2; all items tested on the 1,358 ratio-critical f at n=4 |
| U-C1 | PROVED | CONFIRMED | from C(iv) |
| U-C2 | PROVED | CONFIRMED | "a coordinate" must mean a relevant one; harmless because the class is closed under dropping dummy variables |
| U-C019-C024 | PROVED | CONFIRMED (as reformulations) | the C024 half is RM sec. 11.13 restated, not re-proved here |
| U-Han | PROVED | CONFIRMED | Han-type concavity of psi plus the BR channel bound; no violation n<=4, seven values of t |
| U-Q | PROVED | CONFIRMED with two caveats | mechanism identity and Slote's theorem verified; the side remark "U = 0 for Slote's operators" depends on an unstated quantum definition of pi |
| U-B | KNOWN | CONFIRMED | correct; precise prior art is O'Donnell-Wright-Zhou as recorded in Keller-Mossel-Schlank 2011, Sec. 3 |
| U-LIT | KNOWN | CONFIRMED | every cited statement checked against the source (details Sec. 2.13) |

EVIDENCE spot checks (Sec. 3): the n<=4 numbers in U-num reproduce exactly; the U-X003 numbers reproduce but
belong to the variant with r = k, not the campaign's X003 (r = 2k); on the true X003 the values are almost the same.

## 2. Claim-by-claim

### 2.1 U-Gkey (Lemma G-key) - CONFIRMED

Statement: for Boolean f and nonempty S, |fhat(S)| <= 2^{|S|-1} I_S(f), I_S = sum_{T sup S} fhat(T)^2.

Re-derivation. For z in {-1,1}^{S^c}, v(z) := d_S f(z) = 2^{-|S|} sum_{y in {-1,1}^S} f(y,z) chi_S(y). The sum has
2^{|S|} terms, each +-1, and 2^{|S|} is even for |S| >= 1, so the sum is an even integer and v(z) lies in
2^{1-|S|} Z. Hence |v| <= 2^{|S|-1} v^2 pointwise (trivial at v = 0, and |v| >= 2^{1-|S|} otherwise).
Averaging z gives E_z v = fhat(S); Parseval in z gives E_z v^2 = sum_{T subset S^c} fhat(S cup T)^2 = I_S(f).
So |fhat(S)| <= E|v| <= 2^{|S|-1} I_S(f). Every step holds for every Boolean f; nothing else is used.

Checks (`ex_n4.py`, `falsifiers.py`): exact integers W_S^2 4^n <= 4^{|S|-1} Pi_S^2 over all 984,884 pairs (f,S)
with n <= 4, 0 violations and 266,492 equalities (the author's counts, reproduced independently); 0 violations on
parity lifts (X001, n=4..8), the selector splice X002 (m=3..11), X003 (k=4, n=13), X004, X005, X009 (m=4..10),
activations X011, addressing X012 (a=1,2,3), point defects r<=10 (every S is an equality), the rebuilt X008
two-address witness (`x008_check.py`: H = 5 and I = 17/8 and the influence vector reproduced; 0 violations,
8 of 40 support sets equal; Theorem G slack 1.625), and 60 random and sparse-bent-perturbed functions with n<=11.
Control: on the normalized non-Boolean vector psi_n = n^{-1/2} sum x_i (X006) the same check fails at every
singleton, so the checker can disagree. Not replayed: X007 (its seven-variable table is not in the bundle, and it
concerns products of two functions, not a single spectrum) and X013 (a real-vector obstruction to which a lemma
about Boolean functions does not apply).

Novelty: not found in Kelman-Kindler-Lifshitz-Minzer-Safra (arXiv:1911.10579v2), which defines I_S and uses the
{0,+-1/2}-valuedness of first derivatives but states no such lemma. The |S| = 1 case is classical, and so is
|fhat(S)| <= min_{i in S} Inf_i. That bound is incomparable with the lemma: on a character chi_S with |S| = k the
lemma gives 2^{k-1}, the classical bound gives 1. The author already marks novelty as unverified; I agree.

### 2.2 U-G (Theorem G and Corollary G0) - CONFIRMED

H = sum_S p_S log2(1/pi(S)) + U holds by splitting log2(1/p_S) (pi(S) >= p_S > 0 on the support). For S nonempty,
U-Gkey squared gives log2(1/pi(S)) <= (|S|-1) + (1/2) log2(1/p_S); the empty set has pi = 1. Summing,
sum_S p_S log2(1/pi(S)) <= (I - Var) + (1/2)(H - p_0 log2(1/p_0)), which rearranges to
H <= 2(I - Var) + 2U - p_0 log2(1/p_0) with p_0 = 1 - Var. Both subtracted terms are nonnegative, so H <= 2I + 2U.
U <= H because pi <= 1. Corollary G0 follows: U <= KI gives H <= (2+2K)I; H <= CI gives U <= CI; and Hod's
C_FEI > 6.454784 forces sup U/I >= 2.2274. All correct.

Checks: minimum slack over all nonconstant f with n <= 4 is 0 up to rounding (-8.9e-16), with 2,640 equality
cases at n = 4; no negative slack on any family in Sec. 2.1; slack exactly 0 on addressing a = 1,2,3 (H = 2a,
I = 1 + a/2 reproduced) and on the 2-bit bent function; the bound fails, as it must, for psi_n (H = log2 n, right
side 0).

One correction in the author's favour: on point defects Theorem G is an exact identity, not only tight to leading
order. With p = 2^{-r}, Lemma G-key is an equality at every nonempty S, so the summed inequality is an equality;
directly, U = p_0 log2(1/p_0) + I - 4rp^2 and the right side minus H equals 8p - 8p^2 - 2Var = 0. Verified for
r = 2..41 by formula and r <= 10 by brute force. The ratios 1.06-1.17 quoted in NOTES Sec. 5 use the weaker
denominator 2(I - Var) + 2U (without the p_0 term); the same weaker form is used for the 0.986 read-once figure.

### 2.3 U-loc (exact restriction identity, chain rules, Lambda structure) - CONFIRMED

Re-derivation (notation as in the author's NOTES Sec. 5.1). With p_T = m(1-s), p_{T+i} = ms, pi(T+i) = r pi(T):
p_T log2(pi/p_T) + p_{T+i} log2(pi(T+i)/p_{T+i}) = m log2(pi/m) + m[(1-s) log2(1/(1-s)) + s log2(r/s)].
For the restrictions, p^+-_T = m(1 +- eta) and pi^+-(T) = pi(T)(1 +- x) (the upper sets of the merged law are the
upper sets of P), and the average of the two restriction terms is m log2(pi/m) - m D2((1+eta)/2 || (1+x)/2).
Subtracting gives the stated per-T term. The T = empty term is consistent because C(empty) = sum_T u_T v_T = 0 by
Booleanity (the U = {i} convolution identity). Delta_i U = B_i - Gamma_i + K_i and U(P) = B_i - Gamma_i + U(m) are the
same computation; the chain rules follow by iteration and U(point mass at empty) = 0. Jensen gives the lift bound;
E_m R = 1, Lambda_i = E_m[s R], B_i - Gamma_i <= log2(e) Lambda_i (from s ln(r/s) <= r - s and (1-s)ln(1/(1-s)) <= s)
and sum_T m_T x_T^2 <= sum_T m_T eta_T^2 R(T) <= 4 Lambda_i (x_T is an m-weighted average of eta over the cone of T,
and eta^2 = 4s(1-s) <= 4s) all check.

Checks: n <= 4 exhaustive, |Delta_i U - formula| <= 4.4e-16 and K_i >= 0 always (`ex_n4.py`); 50-digit checks
(`mp_identities.py`): one-step and full chain rules on 25 random non-Boolean laws, error < 1.1e-50; the U-loc
identity on 12 random Boolean f with n = 4..6 at every coordinate, error < 6.7e-51; E_m R = 1 and Lambda = E[sR] to
2.7e-51; the two Lambda inequalities never violated.

The "small-asymmetry regime" approximation K_i ~ (log2 e/2) sum m (eta - x)^2 is heuristic and the author does not
claim it as proved; fine.

### 2.4 U-comp (composition formula for U) - CONFIRMED

For f = g(h_1..h_k) on disjoint blocks, p_f(cup_j T_j) = P_g^mu(J) prod_{j in J} q_j(T_j) (J = {j : T_j nonempty}).
A superset of cup T_j has J' containing J, arbitrary blocks outside J, and supersets T'_j of T_j inside J; the q_j
are normalized on nonempty sets, so pi_f = pi_{P_g}(J) prod_{j in J} pi_{q_j}(T_j). Taking expectations of the log
ratio gives the formula. Brute-force check (`g1g2_comp_check.py`): 110 random compositions (k = 2,3 outer inputs,
blocks of 1-3 bits, n <= 11), my own mu-biased transform; max error 8.9e-16 for U, 1.8e-15 for H, 8.9e-16 for I.

### 2.5 U-G1G2 (level-only bounds) - CONFIRMED

G1: Jensen inside each level k gives U <= sum_k W_k log2(m_k/W_k) with m_k = sum_{|S|=k} pi(S) = E binom(|S|,k);
the k = 0 term has m_0 = 1. Equality when the ratio pi/p is constant on each level, in particular for symmetric
f. G2: sum_S pi(S) lam^{|S|} = E(1+lam)^{|S|}, and Gibbs against the normalized weights gives
U + I log2 lam <= log2 E(1+lam)^{|S|}. Checks: no violation of either at n <= 4 (G2 for lam in {0.01..100});
G1 equal to U to 2.7e-15 on all 2^{n+1} symmetric functions for every n <= 9. The "not tensor-stable" remark (F8)
is a heuristic example, not claimed as proved.

### 2.6 U-GU-implies-FEI - CONFIRMED

Let K = a/(1-b). If G(f) <= aI + bU, pigeonhole over relevant coordinates (irrelevant ones have Delta_i U = 0; the
argument does not need Delta_i U >= 0) gives i with Inf_i > 0 and Delta_i U <= (a + bU/I) Inf_i. With u = U/I and
x = Inf_i/I in (0,1], the induction hypothesis gives u - K <= (a + bu - K)x = b(u - K)x, which forces u <= K for
every b < 1 (b may be negative). Characters force a >= 0. Then Theorem G gives H <= (2 + 2K)I. The H-version
threshold b < 1/2 is also right.

### 2.7 U-A (Theorem A, constant sandwich) - CONFIRMED

(a) min_i B_i/Inf_i <= B/I (mediant); (b) B <= H; (c) restriction induction using (E1); (d) Delta_i = B_i + JS_i
with JS_i <= (2/ln2) min(Inf_i, 1-Inf_i); (e) L <= B <= L + I log2 e (ER eq. (7)). Each is correct in the extended
reals. Dependencies (E1), (E3) re-checked exhaustively at n <= 4: |Delta_i H - B_i - JS_i| <= 5.6e-16, no JS bound
violation, no (E3) violation. Prior art: the restriction induction is the ER sec. 4 argument and appears in
Gonzalez-MacManus-Pereyra (arXiv:2606.00246v2, stopping binary trees); the local forms (LEI), (LDI) as FEI
equivalents are immediate corollaries. The n <= 4 constants 3.4025, 2.7042, 2.6725, 4.8677 reproduce exactly.

### 2.8 U-C (Theorem C, criticality) - CONFIRMED for n >= 2, with one edge correction

Each item re-derived: (i) restrictions live on fewer bits and c_n is nondecreasing; (ii) f chi_i has the same
entropy and influence I + 1 - 2Inf_i; (iii) from (i) and (E1); (iv) by summing (iii); (v) from BR's identity
H(f) - E H(f_X) = H(S_A|S_C) + I(X;D), the channel bound and E_X I(f_X) = I - I_A; (vi) from (iii) and the
variance-local bound of RM sec. 2.2; (vii) granularity; (viii) psi is a polynomial with psi' = beta (Russo-Margulis),
beta nonincreasing by coupling, then the two integral estimates; (ix) concavity psi(t) >= tH and the lower channel
inequality E H(f_X) >= H(S_C) - (2/ln2) I_A.

Edge case: (ii) uses c_n > 0, i.e. n >= 2. At n = 1 the nonconstant functions are +-x_1, c_1 = 0, and x_1 attains
c_1 with Inf_1 = 1 > 1/2. Harmless for every use in the route, but the statement should say n >= 2.
Dependency: (vi) rests on RM sec. 2.2 (campaign source, proved there; not re-proved here). I tested that bound
exhaustively at n <= 4: no violation, max ratio of Delta_i H to the bound 0.708.

Checks (`thmC_check.py`): extremizers of c_n for n = 2,3,4 (8, 16, 32 functions; c_4 = 3.40248 the 4-bit point
defect); (ii), (vi) hold on all of them. Items (iii), (iv), (v) for every block, (viii) at t in {0.05..0.99, 1},
(ix), use only ratio-criticality, so I tested them on every ratio-critical f: 14, 54 and 1,358 functions at
n = 2, 3, 4. No violation; beta(1) = B to 1.3e-15. (vii) and H <= 2(deg - 1) hold for all f with n <= 4.

### 2.9 U-C1 and U-C2 - CONFIRMED

C1: apply H <= A(I + DTC) to an extremizer and use (iv): c_n <= A(1 + 2/ln2). The rewriting
B <= (A-1)DTC + AI and the identity DTC = sum_i I(S_i;S_-i) - TC are correct; DTC = 0 iff product (Han).
C2: if FEI fails, take an extremizer with c_n > K + 2/ln2, drop its dummy variables (this keeps ratio-criticality
and all Inf_i <= 1/2), get a relevant coordinate with B_i <= K Inf_i from the hypothesis, contradicting (iii).
Note: read literally, "has a coordinate with B_i <= K Inf_i" is satisfied by any dummy coordinate (0 <= 0); the
equivalence is still true because the hypothesis quantifies over all f, including the dummy-free version.

### 2.10 U-C019-C024 - CONFIRMED as reformulations

The tree telescoping identity is exact; the mediant bound needs I > 0 and treats nodes with Inf_v = 0 as
Delta_v = 0, which holds. FEI with constant C gives such a tree with constant C + 2/ln2 by Theorem A. The C024
half restates RM sec. 11.13 (H_nat - 3I <= C_path <= H_nat + I) and is only as strong as that source; the
sentence "they carry no extra information beyond (M)" is a heuristic remark, not a proved statement.

### 2.11 U-Han - CONFIRMED

psi(t) = E H(S_{A_t}) is concave with psi(0) = 0, psi(1) = H, so psi(t) >= tH; the BR identity gives
E H(f_{J,X}) >= psi(t) - (2/ln2)(1-t)I. Rearranging gives the claim, and also the deficit form
E[cI(f_X) - H(f_X)] <= t(cI - H) + (2/ln2)(1-t)I for every real c. Exhaustive n <= 4, seven values of t: no
violation (worst H - right side = 0, attained by constants); E I(f_{J,X}) = tI to 4.4e-16.

### 2.12 U-Q (quantum meta-obstruction) - CONFIRMED with two caveats

Slote, arXiv:2608.01424 (2 Aug 2026), Theorem 1: a homogeneous Pauli-degree-d Hermitian unitary with
N(d) = L^{floor(d/2)+1} = 3^{d^2/4 + Theta(d)} nonzero Pauli coefficients of magnitude N(d)^{-1/2} on
Theta(d 3^{d/2}) qubits, built as sum_l P_l (x) B_l with pairwise anticommuting Pauli monomials P_l of degree
ceil(d/2) and commuting diagonal B_l of degree floor(d/2) with sum B_l^2 = L^{k+1} I; Theorem 5 refutes the
quantum FEI conjecture of Bu et al. All of this matches the author's description. The mechanism identity
(A^2 = I for anticommuting P_l and commuting B_l with sum B_l^2 = I) is a two-line computation, correct.
The meta-statement is a valid logical consequence. The bound class can be widened: any psi(d) = o(d^2) fails,
not only o(d). KKLMS Theorem 1.3 does use a classical-only fact: p. 14 of 1911.10579v2 bounds ||d_i f||_{4/3} by
2 I_i[f]^{3/4} "as d_i f is {0,1/2,-1/2}-valued", which matches the author's description.

Caveat 1: the remark (summary, NOTES Sec. 5 and 5.4) that U = 0 for Slote's operators and that (M_U) is therefore
"not contradicted quantumly" needs a quantum definition of pi that the notes never give. With the letter-agreement
order (Q above P iff Q restricted to supp P equals P), a homogeneous spectrum is an antichain and U = 0. With the
support order (supp Q containing supp P), which is how quantum influences of qubit sets are normally defined,
pi(P) is the mass of all Paulis with the same support. In the author's own d = 2 example
(code/slote_check.py: XZI, XIZ, ZZI, ZIZ, coefficients of magnitude 1/2) that gives U = 1 bit, not 0
(`slote_mech.py`). Neither choice affects anything classical.
Caveat 2: "soft tools are not excluded for (M_U)" only means that this one example does not exclude them.

### 2.13 U-B and U-LIT (KNOWN) - CONFIRMED

* Tensor trick (U-B): mathematically correct as stated. The specific "H <= CI + o(n) suffices" observation is
  attributed by Keller-Mossel-Schlank (arXiv:1105.2651, end of Sec. 3) to O'Donnell-Wright-Zhou (ICALP 2011).
  The author cites it only as a standard trick; the precise citation should be added.
* H <= sum_i h(Inf_i): Keller-Mossel-Schlank, Claim 4.1 (stated for all real f). Han, arXiv:2312.08271
  (v2, 10 Dec 2025), abstract: H <= O(I + sum_k I_k log(1/I_k)). Both correct as cited.
* KKLMS, arXiv:1911.10579v2 (7 May 2020), Theorem 1.3 verbatim: "There exists an absolute constant K > 0, such that
  for any D in N and f:{0,1}^n -> {0,1} we have H[f^{<=D}] <= K sum_{|S|<=D} |S| log(|S|+1) fhat(S)^2 + K I[f]."
  Theorems 1.1, 1.2 are as described. Correct.
* Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf, arXiv:1809.09819, ToCT 13(4) 2021: H <= 2 aUC^parity and
  H_inf <= 2 C^parity_min. Correct.
* Granularity H <= 2(deg - 1): proof in NOTES Sec. 3 re-checked (Moebius inversion gives integer 0/1-basis
  coefficients); KMS Prop. 1.7 states the slightly weaker 2^{-k} lattice and Ent <= 2k. Verified numerically n <= 4.
* Potapov, arXiv:2609.21563 (18 Sep 2026): FEI for plateaued functions with sharp constant 4, partially bent with
  sharp constant 2. Correct.
* Hod, arXiv:1711.00762 (2 Nov 2017), title "Improved lower bounds for the Fourier entropy/influence conjecture via
  lexicographic functions": C > 6.454784. O'Donnell-Tan, arXiv:1304.1347: C >= 6.278. Correct.
* Gonzalez-MacManus-Pereyra, arXiv:2606.00246 (v2 9 Jun 2026): stopping binary trees, delta-tribes, as described.
* Not re-read by me: Chakraborty-Kulkarni-Lokam-Saurabh TCS 654 (the author also did not), Wan-Wright-Wu,
  Shalev, Chakraborty et al. 1903.11635 (these appear only in NOTES Sec. 3, not in a claim).

## 3. EVIDENCE claims spot-checked

* U-num (n <= 4): max H/I = 3.402476 (4-bit point defect), max B/I = 2.704153, K_loc at n <= 4 = 2.672489,
  K_Delta at n <= 4 = 4.867669, max U/I = 1.464976, max G/I = 2.75, and the four GU' combinations hold with
  maximum exactly 0 (they are tight at n = 4, so the constants were fitted to that data). All reproduced.
* U-X003: the author's script builds the activation with r = k, not the campaign's r = 2k, so the quoted numbers
  belong to a variant. My recomputation of the variant reproduces them (dU/Inf = 3.690, 4.101, 4.245, 4.296 and
  dH/Inf = 8.329, 10.354, 12.342, 14.333 at k = 4, 6, 8, 10). On the true X003 (r = 2k): k = 4 gives 3.664 and
  8.300, k = 6 gives 4.099 and 10.351. The conclusion is unchanged, but the label should read "X003 with r = k".
  X009 (m = 4..12: 3.574 ... 4.314 against 8.03 ... 16.33) and X002 (2.75 -> 3.0 against 4) reproduce.
* U-G-tight: equality on addressing and bent2 reproduced; exact equality on point defects (Sec. 2.2).

## 4. Further adversarial checks and two findings

### 4.1 Negative controls (the checks can fail)

`controls.py`, n = 4: Theorem C(iii) evaluated on the 64,176 non-ratio-critical functions fails at 62,080
(f, i) pairs and at none of the ratio-critical ones. U-Han with the channel constant halved fails (worst excess
+0.074 bits), with it quartered fails by +0.557. Theorem G with 1.9(I - Var) in place of 2(I - Var) fails on 3,400
functions, with 1.8U in place of 2U on 4,608. So the exhaustive passes above are not vacuous. Both coefficients
in Theorem G are attained (equality cases exist); the channel constant 2/ln2 in U-Han is not shown to be sharp,
but halving it already fails at n = 4.

### 4.2 Dependencies at larger n

`deps_larger_n.py`, 24 functions with n = 5..8 (random, two-point defects, bent plus one flip, integer LTFs):
the RM sec. 2.2 variance-local bound holds (largest ratio of Delta_i H to the bound 0.850, closer to 1 than at
n <= 4); the BR channel bound I(X;D) <= (2/ln2) I_A holds on random blocks (largest excess -0.027); E_X I(f_X) =
I - I_A exactly; U-Han holds for t in {1/4, 1/2, 3/4} with the expectation over all (J, X) computed exactly.

### 4.3 Finding: Theorem G is an identity on every read-once AND/OR formula

The author reports Theorem G as "asymptotically tight (ratio 0.986)" on the near-extremal read-once AND/OR
formulas. That ratio uses the weak denominator 2(I - Var) + 2U. With the full right side the bound is an
equality on every such formula, for a structural reason.

Proposition (referee). Let f be computed by a read-once formula whose gates are two-input gates of AND type
(g(a,b) = s0 AND(s1 a, s2 b), signs s_i, which covers AND, OR and all negations), with every variable used at most
once and literals possibly negated. Then for every S there is a sign e_S such that d_S f takes only the values
0 and e_S 2^{1-|S|}. Consequently |fhat(S)| = 2^{|S|-1} I_S(f) for every nonempty S, and
H(f) = 2(I - Var) + 2U - p_0 log2(1/p_0).

Proof. Fix S and z. The restriction g_z = f(., z) is computed by the same tree with the leaves outside S set to
constants. If some variable of S is irrelevant for g_z, its top coefficient d_S f(z) is 0. Otherwise every gate on
the subtree spanning S whose other input carries no S-leaf receives the non-killing constant (else the S-leaves
below it would be irrelevant), and an AND-type gate with its non-killing constant passes the other input through
with a sign fixed by the gate's negation pattern, not by z. The gates whose two inputs both carry S-leaves keep
their type. So g_z is, for every such z, the same read-once AND-type formula on S, and the top Walsh coefficient
of a read-once AND-type formula on k relevant variables is +-2^{1-k} (an AND-type gate has top coefficient +-1/2;
induct on the tree). Hence d_S f(z) is in {0, e_S 2^{1-|S|}}, so |E d_S f| = E|d_S f| = 2^{|S|-1} E(d_S f)^2.
Every inequality in the proof of Theorem G is then an equality. QED

Checks: `readonce_equality.py`, 200 random read-once AND/OR formulas with random negations and n <= 12: every
Walsh set in the support is an exact integer equality, and the Theorem G slack is 0 to 2.2e-15. Control: with XOR
gates allowed, 167 of 200 formulas have strict sets and the slack reaches 10.6. `beam.py` (my own beam search
on my own composition engine, validated against brute force to 2.4e-15) reproduces the author's sequence
H/I = 3.40, 3.89, 4.40, 4.74, 5.08, 5.29, 5.51, 5.66, 5.81, 5.91, U/I up to 2.06, weak ratio 0.852 ... 0.986 and
G/I 1.94 ... 2.284; the full Theorem G ratio is 1.000000 on the best formula of every round. Gates of larger
fan-in are trees of two-input AND-type gates, so they are covered. Lexicographic functions are read-once AND/OR
chains (decision lists), so the identity holds for them; I did not check whether every function in Hod's three
constructions is of this form. Point defects and addressing satisfy the same equality condition. On all of these
families FEI is exactly the statement sup U/I < infinity.

### 4.4 Finding: the GU evidence is weaker than stated (CONJECTURE, not a verdict item)

With the validated engine (`rec.py`, `rec_fast.py`; `explore_gu.py`, `anneal_gu.py`): maj5(g5,...,g5) gives
G/I = 3.2157, maj3(maj3(g5)) gives 3.1581, and a 6-bit inner function found by annealing under maj5 gives
3.2265. The author's maximum 3.090 is not the maximum; any constant in GU is at least 3.2265, so GU would give
C_FEI <= 2 + 2K with 2 + 2K >= 8.45. No family I tried grows: iterated maj3 over g5 settles near 3.11, iterated
g5 over itself near 3.04, majorities of larger arity fall (maj7 3.00, maj9 2.70).
The n <= 4 fit "G <= 2.25 I + 0.5 U", the only quoted GU' instance with b < 1, fails off n <= 4: maj3(g5) has
G/I = 3.0905 > 2.25 + 0.5 x 1.5163 = 3.008, and maj5(g5) has 3.216 > 3.092. The fit "G <= 1.75 I + U" survives every
case I computed, but b = 1 is outside GU' and gives no induction. The author labels both fits as n <= 4 evidence,
so nothing is misstated; the point is that the fits do not extend.
The selector-pair values behind U-locfail reproduce from the author's data (4.778, 5.112, 5.481, 6.147 at
n = 6..9).

## 5. Corrections the route should carry

1. Theorem C(ii) holds for n >= 2 only (n = 1: f = x_1 attains c_1 = 0 with Inf_1 = 1).
2. U-X003 is computed on the activation size r = k; the campaign's X003 has r = 2k. Relabel, or quote the r = 2k
   values (k = 4: 3.664 / 8.300; k = 6: 4.099 / 10.351).
3. U-G-tight understates the result: Theorem G is an exact identity on point defects, addressing, bent2 and every
   read-once AND/OR formula (Sec. 4.3). The ratios 1.06-1.17 and 0.986 refer to the weak form without the p_0 term.
4. "U = 0 for Slote's operators" needs the letter-agreement definition of the quantum upper set; with the
   support order the author's own d = 2 example has U = 1 bit. "(M_U) is not contradicted quantumly, so soft tools
   are not excluded" should read "is not contradicted by this example".
5. NOTES Sec. 5 says Theorem G "exactly kills the obstruction that Corollary C1 isolated". It kills small-U laws
   (exact product laws with small marginals among them). C1's obstruction is small DTC, which allows mixtures of
   product laws. If small DTC forced small U, then by C1 and Theorem G, FEI would follow. Read the sentence as
   "kills the exact product-law case".
6. "The classical-only content of FEI is exactly Lemma G-key" (NOTES Sec. 5.4) is a heuristic. Whether (M_U)
   has a proof that uses no classical-only ingredient is open.
7. U-B: add the citation (O'Donnell-Wright-Zhou, via Keller-Mossel-Schlank arXiv:1105.2651 Sec. 3).
8. GU: the observed maximum is at least 3.2265, not 3.09 (Sec. 4.4); the n <= 4 GU' fit with b = 1/2 fails at n = 15.

None of these touches the correctness of a PROVED or KNOWN claim, except the n = 1 edge in item 1.

## 6. Files

| file | what it checks | result file |
|---|---|---|
| `rlib.py` | my Walsh/upper-set/entropy library | - |
| `ex_n4.py` | U-Gkey exact, Theorem G, U-loc, chain rules, (E1), (E3), RM 2.2, the n<=4 maxima, GU' fits | `ex_n4_results.json` |
| `thmC_check.py` | Theorem C on all ratio-critical f (n<=4), extremizers, U-Han, granularity | `thmC_results.json` |
| `g1g2_comp_check.py` | G1, G2, symmetric equality, product laws, composition formula | `g1g2_comp_results.json` |
| `falsifiers.py` | X001-X012 families, addressing, bent2, point defects, psi_n control, X002/X003/X009 ratios | `falsifiers_results.json` |
| `x003_variants.py` | X003 with r = k and r = 2k | `x003_variants_results.json` |
| `mp_identities.py` | 50-digit identities on random laws and Boolean f | `mp_identities_results.json` |
| `slote_mech.py` | A^2 = I mechanism; U of the d = 2 example under both orders | `slote_mech_results.json` |
| `controls.py` | negative controls | `controls_results.json` |
| `deps_larger_n.py` | RM 2.2, BR channel bound, U-Han at n = 5..8 | `deps_larger_n_results.json` |
| `gu_values.py`, `rec.py`, `rec_validate.py`, `rec_fast.py` | composition engine and its validation | `gu_values_results.json`, `rec_validate_results.json` |
| `beam.py` | read-once beam replication | `beam_results.json` |
| `readonce_equality.py` | equality case of Theorem G | `readonce_equality_results.json` |
| `explore_gu.py`, `anneal_gu.py` | GU stress tests | `explore_gu_results.json`, `anneal_gu_results_7.json` |

External sources read for the KNOWN checks (12 Oct 2026): arXiv abstracts or full text of 2608.01424 (Slote, HTML
version, Theorems 1 and 5), 1711.00762, 1911.10579v2 (pp. 1-4, 6-7, 11-14, 31 of the PDF), 1105.2651 (full text),
2312.08271, 1809.09819, 2609.21563, 1304.1347, 2606.00246.
