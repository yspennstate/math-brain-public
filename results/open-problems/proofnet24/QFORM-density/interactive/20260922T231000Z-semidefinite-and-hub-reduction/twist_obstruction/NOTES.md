# NOTES - twist lemma (04_twist_lemma)

Notation. P is n x k, rows rho_i, G = P^T P, leverages c_i = rho_i^T G^{-1} rho_i. For symmetric E put
  T_E(u) = E exp(i <Pu, X> + i X^T E X),   J(E) = int_{R^k} |T_E(u)| du.
Z = P^T X in R^k, so <Pu, X> = <u, Z>.

## N1. Chirp identity for a rank-one twist along the integrated direction (k = 1)   [PROVED]
k = 1, P = v unit, L = <v, X>, E = kappa v v^T. Then T_E(u) = int e^{iuy + i kappa y^2} p_L(y) dy and
e^{iuy + i kappa y^2} = e^{-iu^2/(4 kappa)} e^{i kappa (y + u/(2kappa))^2}, so
  |T_E(u)| = |(p_L * c)(-u/(2 kappa))|,  c(z) = e^{i kappa z^2},
  J(kappa v v^T) = 2|kappa| int_R |(p_L * c)(x)| dx.
Twist along the integrated direction = Schroedinger evolution of p_L; L^1 is not preserved by it.

## N2. COUNTEREXAMPLE: every nonzero compression twist is fatal   [PROVED - write-up in REPORT; numerics pending]
Claim: for every kappa != 0, every n >= 2 and every unit v with v_i^2 <= 1/2,
  sup over independent laws with densities <= 1 of J(kappa v v^T) = +infinity.
So ||E||_op <= delta, ||E P|| <= delta, ||P^T E P|| <= delta are all insufficient, for every delta > 0.
Construction (n = 2 first, v = (1,1)/sqrt2): f_1 = sum_{p<N} exp(-pi N^2 (x - a_p)^2), f_2 = same with b_q
(Gaussian bumps of mass 1/N, height 1, width ~1/N; bumps unit-separated so f <= 1 + tiny; rescale by 1+tiny).
Then p_L = N^{-2} sum_{p,q} gamma_sigma(y - y_pq), sigma^2 = 1/(2 pi N^2), y_pq = (a_p + b_q)/sqrt 2.
Exact Gaussian integral (alpha = 1/(2 sigma^2) = pi N^2):
  |int e^{i kappa y^2 + i u y} gamma_sigma(y - c) dy| = (alpha/sqrt(alpha^2+kappa^2))^{1/2} exp(-alpha (u + 2 kappa c)^2 / (4(alpha^2+kappa^2))).
Each piece: Gaussian in u centred at -2 kappa y_pq, L^1 norm sqrt(4 pi) (alpha^2+kappa^2)^{1/4} >= 2 pi N.
Centres separated by Delta >> tau = sqrt(2(alpha^2+kappa^2)/alpha) (choose a_p = p D, b_q = q N D, D = C N/|kappa|):
disjoint windows U_pq of width Delta around the centres and the triangle inequality give
  J >= N^{-2} sum_pq (||G_pq||_1 - 2 int_{U_pq^c} G_pq) >= 2 pi N (1 - 2 P(|g| > Delta/(2 tau))).
So J >= c N -> infinity. General spread v (any n): X_i = N Gaussian bumps each, base-N positions; the bumps of L have
variance sum v_i^2 /(2 pi N^2) = 1/(2 pi N^2) whatever n is, so the same bound holds: small leverages do not help.
Mechanism: the twist moves the Fourier transform of each narrow piece of p_L to its own place (-2 kappa y_j),
so the cancellation that makes int |psi_L| small disappears. L^2 is preserved (Plancherel), L^1 is not.

## N3. L^2 twist lemma: the L^2 norm does not see the twist at all   [PROVED]
For ANY real measurable phi(X): u -> E exp(i<u, Z> + i phi(X)) is the Fourier transform of the complex density
m(z) = E[e^{i phi(X)} | Z = z] p_Z(z), |m| <= p_Z. Plancherel:
  int_{R^k} |E e^{i<Pu,X> + i phi(X)}|^2 du = (2 pi)^k ||m||_2^2 <= (2 pi)^k ||p_Z||_inf <= (2 pi)^k 2^{k/2} det(G)^{-1/2}
(Z = G^{1/2} Y, Y = orthogonal projection coordinates of a product measure, density <= 2^{k/2} by Ball/LPP).
No leverage condition, no condition on phi.

## N4. Block lemma (positive result, new)   [PROVED - check twice]
Partition [n] = K u I u J (disjoint). If E_{KI} = 0, then
  J(E) <= (2 pi)^k 2^{k/2} (det G_K det G_I)^{-1/4},   G_K = P_K^T P_K, G_I = P_I^T P_I,
for ALL E_KK, E_II, E_KJ, E_IJ, E_JJ and all laws; no leverage condition.
Proof: condition on X_J (Fubini, |E| <= E_{X_J}|E_{X_K,X_I}|). Given X_J the phase is
 <P_K u, X_K> + X_K^T E_KK X_K + 2<E_KJ x_J, X_K>  +  (same with I)  + (function of x_J),
and X_K, X_I are independent with no coupling, so |E_{X_K,X_I}[..]| = |A_K(u)| |A_I(u)| with A_K(u) =
E exp(i<u, P_K^T X_K> + i phi_K(X_K)), phi_K = X_K^T E_KK X_K + 2<E_KJ x_J, X_K>. Cauchy-Schwarz in u and N3 for
each factor (projection densities of the product measures on K and on I).
Check (n = 3, K={1}, I={2}, J={3}, E = kappa(e2e3+e3e2) + kappa'(e1e3+e3e1)): direct computation gives
 J <= E_{X_3} ||psi_1(./sqrt3)||_2 ||psi_2(./sqrt3)||_2 = 2 pi sqrt3 ||f_1||_2||f_2||_2, consistent.
Comparison with Theorem F: TF needs E_II diagonal + leverages <= 1/2 on I, allows E_IJ, E_JJ arbitrary.
N4 allows ANY twist inside K and inside I but no coupling K-I; it needs no leverage condition.
Counterexample N2 is consistent: E = kappa vv^T couples every pair of coordinates in supp v.

## N5. Two proposed reductions, checked against N2
(a) "Theorem D covers |t| >= 1/||eps E||_F; the twist lemma is needed only for |theta| ||E||_F <= 1, small diagonal."
The reduction itself is right (hub in J: A_IJ has s_1 ~ |w_I|, s_2 ~ |lambda| |v_I||v_J|, the rest from eps E_IJ, so
Z = e_3 >~ eps^2 ||E_IJ||_F^2 and int_{|t|>T} |t|^{-3/2} Z^{-1/4} dt = 4 T^{-1/2} Z^{-1/4} = O(1) at T = 1/(eps||E||_F);
needs the volume-sampling marginals <= 1/2 on I, plausible for spread data, not checked here).
BUT the lemma asked in that regime is FALSE: E = kappa v v^T with |kappa| tiny has ||E||_F = |kappa|, diagonal
<= |kappa|/2, and sup_laws J = infinity (N2). Frobenius-mildness does not help because spread laws turn any fixed
kappa into an effectively large twist (the construction needs positions spread at scale >> N/|kappa|).
The Gaussian model is misleading here: for X ~ N(0, s^2 I), J(kappa v v^T) = sqrt(2pi)/s * (1+4 s^4 kappa^2)^{1/4},
bounded by sqrt(2pi)/s + sqrt(4 pi |kappa|) UNIFORMLY in s. Bumpy laws, not large variance, are what inflate J.
(b) "Condition on X_K; cross terms are shifts (BL translation invariant); only E_II matters, random p-fraction."
Correct, and it is exactly the mechanism of Theorem F. N4 pushes it further: inside the conditioned picture a twist
E_II is harmless if I splits into two pieces with no coupling (L^2 for each piece, Cauchy-Schwarz). N2 shows what
cannot be handled: a coupling between the pieces that is ALIGNED with the frame (kappa (v_1.X_1)(v_2.X_2)).
Consequence for the canonical hub case (a): absorbing the compression of eps W onto span(v, w) into the structured part
leaves eps c' L^2 along the HUB direction w (c' ~ w^T W w). Theorem H cannot linearize it (frame (v, w, w) singular),
and as a twist it is of the fatal type N2. So the twist lemma, even in the Frobenius-mild regime, must use the dense
bulk of W (which kills the bumps of N2 at spread positions) or the hub step must keep L^2 (2D indefinite pair
(X_h, L), matrix [[0,1],[1,kappa]]) - a real-variable step like GEOM Prop 5.4.

## N6. Counterexample numerics (counterexample_run.py, output counterexample_run_output.txt)   [NUMERICAL, matches N2]
Exact evaluation (gmix.py: every twisted CF of a Gaussian-mixture product law is a finite sum of explicit complex
Gaussians; self-test against 2D quadrature, error 1e-14). n = 2, v = (1,1)/sqrt2, kappa = 1:
 C = 8: J(kappa vv^T) = 12.57, 25.11, 37.65, 50.20, 75.30 for N = 2, 4, 6, 8, 12, i.e. J/(2 pi N) = 1.000 .. 0.999,
 against the untwisted J(0) <= 2 pi (Cauchy-Schwarz, same laws) and max density 1.000000. C = 4: J/(2 pi N) = 0.90.
 n = 4, v = (1,1,1,1)/2 (leverages 1/4): J/(2 pi N) = 1.000, 0.999, 0.999 for N = 2, 3, 4 (16, 81, 256 components).
 The rigorous envelope lower bound is within 0.2 pct of the exact value at C = 8, and is kappa-free.

## N7. General form of the counterexample: growth N^k   [PROVED, write-up in REPORT]
P of rank k, p = P e in range(P) a unit vector with every p_i != 0 (generic direction), kappa != 0. Laws: N bumps of
height 1 (sd s0 = 1/(N sqrt(2 pi))) per coordinate at a_{i,q} = q N^{i-1} D / p_i, D = C N/|kappa|. Component c
(product Gaussian N(mu_c, s0^2 I)): with y_c = <p, mu_c> in D*{0..N^n-1} and w = u + 2 kappa y_c e,
 |T_c(u)| = (1+4 kappa^2 s0^4)^{-1/4} exp(-w^T M w / 2),  M = P^T [s0^2 (I - pp^T) + gamma pp^T] P,
 gamma = s0^{-2}/(s0^{-4} + 4 kappa^2)  (from Re (s0^{-2} I - 2 i kappa pp^T)^{-1}).
Slabs {|<P^T p, u> + 2 kappa y_c| < kappa D} are disjoint; along the functional <P^T p, .> the component has variance
(P^T p)^T M^{-1} (P^T p) <= 1/min(s0^2, gamma) ~ 2 pi N^2. Disjoint-window argument:
 J(kappa pp^T) >= (1 - 2 eps_C) (1+4kappa^2 s0^4)^{-1/4} (2 pi)^{k/2} det(M)^{-1/2} ~ (2 pi N)^k det(G)^{-1/2},
eps_C = P(|g| > kappa D sqrt(min(s0^2,gamma))) -> 0 as C grows. Diagonal-twist bound is (4 pi)^k det(G)^{-1/2}:
ratio (N/2)^k -> infinity.

## N8. Theorem H' (hub version of the block lemma)   [PROVED]
Coordinates H u K u I u J. A_MM = sum_{k<=r} lambda_k v_k v_k^T + B on M = K u I, with B_KI = 0. Rows
rho~_i = ((v_k)_i, A_ih) in R^m, m = r + |H|, G~_K = sum_{i in K} rho~_i rho~_i^T, G~_I likewise, both invertible. Then
 |phi(t)| <= (2|t|)^{-|H|} prod_k (4 pi |t lambda_k|)^{-1/2} (2 pi)^m 2^{m/2} (det G~_K det G~_I)^{-1/4},
for ALL B_KK, B_II (dense allowed), A_HH, A_{H,J}, A_{M,J}, A_JJ, and all linear terms; no leverage condition.
Proof = Theorem H's proof up to the (u, y)-integral, then N4 with P~ = [V, A_MH] and twist t B.
Special case B = D diagonal: Theorem F/H without the leverage condition, for any split with both halves nondegenerate.

## N9. Coupling-gain lemma (large non-aligned coupling helps)   [PROVED]
Condition on X_J; suppose E_KI = sum_{l<=r} sigma_l a_l b_l^T (sigma_l > 0, a_l orthonormal in R^K, b_l in R^I).
T(u) = int_{range M} Psi_K(P_K u + w) n_u(w) dw, where Psi_K(xi) = E exp(i<xi, X_K> + i phi_K) on R^K and
n_u = density of the complex measure E[a_I(u, X_I); 2 E_KI X_I in dw]. Cauchy-Schwarz in w, then in u, Plancherel:
 J <= (2 pi)^{k + r/2} 2^{(k+r)/2} (det Gram[P_K, a] det Gram[P_I, b])^{-1/4} prod_l (2 sigma_l)^{-1/2}.
Needs a_l not in range(P_K), b_l not in range(P_I) (non-aligned). Aligned coupling (N2) makes the Gram singular.
Small non-aligned coupling: OPEN (heuristically harmless: the orthogonal frequency shifts kill Gaussian bumps).

## N10. Numerical checks of N4/N9 and zero-compression twists (block_lemma_check.py, zero_compression_check.py)
On the adversarial laws of N2 (n = 4, v = (1,1,1,1)/2): aligned kappa vv^T gives J = 12.57, 18.83, 25.10 (N = 2,3,4);
the same twist cut into blocks, kappa(v_K v_K^T + v_I v_I^T), K = {0,1}, I = {2,3}, gives 0.79, 0.24, 0.10 (block
lemma bound 4 pi); adding a non-aligned coupling sigma(ab^T + ba^T), sigma = 0.1, 1, 10, changes nothing (<= 0.79).
Zero-diagonal kappa(vv^T - diag v o v), random dense zero-compression R, and the cross twist kappa(vw^T + wv^T) are all
<= 2.1 on these laws (these laws are tuned against the aligned twist only - not an adversarial test of those twists).
Cross twist with w = (1,-1,1,-1)/2 is the block lemma in disguise: 2 kappa L D = kappa (A^2 - B^2)/2 with
A = X_1 + X_3, B = X_2 + X_4 independent, so K = {1,3}, I = {2,4} has E_KI = 0 and J <= 4 pi exactly.
## N11. Corollaries with constants (checked twice)
F' (rank three + B, B_KI = 0): |phi(t)| <= (2 pi)^{3/2} |l1 l2 l3|^{-1/2} (det G_K det G_I)^{-1/4} |t|^{-3/2},
  ||p_Q|| <= 6 |l1 l2 l3|^{-1/3} (det G_K det G_I)^{-1/6}   [(4pi)^{-3/2}(2pi)^3 2^{3/2} = (2 pi)^{3/2}; int min(1,K|t|^{-3/2}) = 6K^{2/3}]
H' (one hub, one square, B_KI = 0): |phi(t)| <= 2 pi^{3/2} |lambda|^{-1/2} (det G~_K det G~_I)^{-1/4} |t|^{-3/2},
  ||p_Q|| <= 3 * 2^{2/3} |lambda|^{-1/3} (det G~_K det G~_I)^{-1/6}  (~ 7.6 for a balanced split of orthonormal v, w).
## N12. Why the hub-direction compression cannot be linearized by any of the Fourier tools
Pair (X_h, L), matrix [[a_hh, 1],[1, c]], det ~ -1. Linearizing both squares of the pair gives frame rows a (hub) and
w_i b (leaves) with G = a a^T + |w|^2 b b^T, so the hub coordinate has normalized leverage exactly 1 (BL needs <= 1/2), and
in any split the block without h sees only span(b) (block lemma needs both halves nondegenerate). Linearizing only via the
hub substitution y = 2 t x_h (Theorem H) uses the direction w once; the L^2 term needs it a second time -> twist of the
N2 type along w. So in case (a) the Fourier tools must be combined with a real-variable step for the pair, or with a
twist lemma that uses the non-aligned bulk of W.

## N13. FULL PROOF of Theorem 1 (obstruction), as audited
Statement. P n x k of rank k, p = Pe unit with all p_i != 0, kappa != 0, N >= 1, s0 = 1/(N sqrt(2 pi)). There are laws with
densities <= 1 + 4exp(-D^2/(8 s0^2)) (rescale by that factor to get <= 1) such that
  J(kappa pp^T) >= (1 - 2 eta)(1 + 4 kappa^2 s0^4)^{-1/4} (2 pi N)^k det(G)^{-1/2},  eta = P(|g| >= 10 (1+4kappa^2 s0^4)^{-1/2}).
(eta <= 2e-12 once N^4 >= kappa^2/pi^2, since 4 kappa^2 s0^4 = kappa^2/(pi^2 N^4); eta -> 1.5e-23 as N -> inf.)
Proof. D = 10 sqrt(2pi) N/|kappa|, f_i = N^{-1} sum_{q<N} gamma_{s0}(x - a_iq), a_iq = q N^{i-1} D/p_i. Bump height 1;
same-coordinate bumps >= D apart (|p_i| <= 1), D/s0 = 20 pi N^2/|kappa|, so f_i <= 1 + 4 exp(-D^2/(8 s0^2)).
Rescaling X -> lambda X (lambda = 1+delta): J_{lambda X}(E) = lambda^{-k} J_X(lambda^2 E); construction is for every
kappa, so rescaling costs only lambda^{-k}.
Mixture over multi-indices c, weights N^{-n}, components N(mu_c, s0^2 I), y_c = <p, mu_c> = D sum_i c_i N^{i-1} distinct.
Component: E e^{i<Pu,X> + i kappa <p,X>^2} = (1 - 2 i kappa s0^2)^{-1/2} exp(i<Pu,mu_c> + i kappa y_c^2 - beta^T C beta/2),
beta = P(u + 2 kappa y_c e), C = (s0^{-2} I - 2 i kappa pp^T)^{-1} = s0^2 (I - pp^T) + pp^T/(s0^{-2} - 2 i kappa),
Re C = s0^2 (I - pp^T) + gamma0 pp^T, gamma0 = s0^2/(1+4kappa^2 s0^4) <= s0^2  =>  gamma0 G <= M := P^T Re C P <= s0^2 G.
|component| = G_c(u) = (1+4kappa^2 s0^4)^{-1/4} exp(-w^T M w/2), w = u + 2 kappa y_c e.
||G_c||_1 = (1+..)^{-1/4} (2pi)^{k/2} det(M)^{-1/2} >= (1+..)^{-1/4} (2 pi)^{k/2} s0^{-k} det(G)^{-1/2} = (1+..)^{-1/4} (2 pi N)^k det G^{-1/2}.
l(u) = <P^T p, u>, <P^T p, e> = <p, Pe> = 1 so l(u) = l(w) - 2 kappa y_c. U_c = {|l(u) + 2kappa y_c| < |kappa| D} disjoint.
Var of l(w) under the weight: (P^T p)^T M^{-1} (P^T p) <= gamma0^{-1} p^T P G^{-1} P^T p = gamma0^{-1}.
|kappa| D gamma0^{1/2} = |kappa| D s0 (1+..)^{-1/2} = 10 (1+..)^{-1/2}  => int_{U_c^c} G_c <= eta ||G_c||_1.
J = int |sum_c N^{-n} T_c| >= sum_c int_{U_c} |.| >= sum_c N^{-n}(int_{U_c} G_c - sum_{c'!=c} int_{U_c} G_c')
  >= sum_c N^{-n}(int_{U_c} G_c - int_{U_c^c} G_c) >= (1 - 2 eta) min_c ||G_c||_1.  []
Audit: k = 1 exact value ||G_c||_1 = (1+..)^{+1/4} 2 pi N (M = gamma0 exactly), the theorem uses the weaker (1+..)^{-1/4};
envelope script used tau^2 = 1/gamma0, same thing; exact grid J agrees with the LB to 0.2 pct (C = 8).
CORRECTION to an earlier line: eta is NOT < 1e-20 at 4 kappa^2 s0^4 = 1 (threshold 7.07, eta ~ 1.5e-12); state 2e-12.

## N14. FULL PROOF of Theorem 3 (block lemma) and Proposition 4 - see N3, N4, N9 (complete as written there).
Extra audit: n = 2, k = 1, P = (1,1)/sqrt2, K = {1}, I = {2}: Theorem 3 gives 4 pi, the direct Cauchy-Schwarz gives
2 sqrt2 pi; the factor sqrt2 is the 2^{k/2} of Ball's bound, not needed for a single coordinate. Consistent (not tight).
Prop 4 check of the identity T(u|x) = E_{X_I}[a_I Psi_K(P_K u + 2 E_KI X_I)], 2 E_KI X_I = sum_l omega_l a_l,
omega_l = 2 sigma_l <b_l, X_I>: correct. Needs Gram[P_K, a], Gram[P_I, b] invertible (b_l need not be orthonormal).

## N15. Final checks
- Rudelson-Vershynin pointwise form: NOT used anywhere here. Inputs are only Lemma 1 of RESULTS (through Theorem F's
  bound (0.1) and Theorem D, both via L^p norms), Plancherel, Ball/LPP projection-density bounds, explicit Gaussian integrals.
- Refinement of Section 5: for W with W_KI = 0 the hub-direction compression w^T W w = w_K^T W_KK w_K + w_I^T W_II w_I sits
  INSIDE the blocks and Corollary 3.2 absorbs it. The obstruction of Theorem 1 is exactly the ALIGNED CROSS-BLOCK coupling
  P~_K^T W_KI P~_I (m x m). For a random split of dense W it is about (1/4) P~^T W P~ plus fluctuations: small, not zero,
  so a proof for dense W must let the non-aligned coupling control the aligned one (conjecture (c)).
- Report text is delivered in the final message (the environment does not allow REPORT.md from this process).
