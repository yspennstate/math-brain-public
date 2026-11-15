# P6 derivations: erasure entropies of sparse linear DNFs

Source: FEIB21 PROOFS.md section 12 (fei_solve_2026_11_09/codex/workers/FEIB21), FLOW 12(s). Re-derived 11 Nov 00:5x.

Setting. F a monotone DNF in 0/1 variables, all terms of width w, any two terms share at most one variable (linear),
every variable in at most D terms. f = 1 - 2F (+-1). L = w - 1, a = 2^-L. Coordinate i in d >= 1 terms; mate sets
(the L other variables of each term through i) are pairwise disjoint by linearity. N = 1[no term avoiding i fires],
A_t = AND of the t-th mate set, M = N prod_t (1 - A_t). Then h = D_i f = N - M = N 1[OR_t A_t] (0/1 valued, so
Inf_i = delta = E h = P[N, OR A_t]) and g = E_i f = N + M - 1 = 2N - h - 1, so ghat(T) = 2 Nhat(T) - hhat(T) for T != 0.
A = E N.

Step 1 (Inf vs A). d a theta <= delta/A <= d a, theta = 1 - L(D-1)a - (d-1)a/2.
- Lower: R = 1[background terms not meeting mate set t fail]. N = R and (remaining background terms fail). Each
  remaining background term meets mate set t in exactly one mate (it avoids i; two mates would share 2 with term t),
  so there are at most L(D-1) of them, each with L further literals. Given A_t (independent of R), the event "one of
  them fires" is increasing, R decreasing; Harris: P[fires | R, A_t] <= L(D-1)a. So P[A_t, N] >= a P[R](1 - L(D-1)a)
  >= a A (1 - L(D-1)a). Pairs: P[A_s A_t | N] <= P[A_s A_t] = a^2 (Harris). Bonferroni:
  delta/A >= d a (1 - L(D-1)a) - C(d,2) a^2 = d a theta.  OK
- Upper: P[A_t | N] <= a (Harris), union bound.  OK

Step 2 (derivative spectrum). Order the d terms; h_t = N A_t prod_{s<t}(1 - A_s), disjoint supports, sum = h.
h_t vanishes off A_t, so h_t = A_t Psi_t with Psi_t = h_t(mates of t = 1, rest), a function of the other variables.
A_t = 2^-L sum_{S subset mates_t} chi_S (sign convention aside), so hhat_t(S u V) = +-2^-L Psihat_t(V): squared mass
uniform over the 2^L subsets S. Omega = {T: T contains >= k mates of some incident term}. Mass of h_t outside Omega
<= gamma_k ||h_t||^2, gamma_k = a sum_{j<k} C(L,j). Cauchy-Schwarz across d pieces:
sum_{T not in Omega} hhat(T)^2 <= d sum_t ... <= d gamma_k delta. With the trivial bound, <= eps delta, eps = min(1, d gamma_k). OK

Step 3 (background mass on Omega). J = k mates of one incident term. No background term contains two of J. So
N = R' prod_{j in J}(1 - z_j Q_j), R' = 1[background terms missing J fail], Q_j = OR of residual conjunctions (width L)
of the <= D-1 background terms through z_j; Q_j and R' do not depend on any z in J. D_J N = R' prod (-+Q_j/2), so
||D_J N||^2 = 4^-k P[R', all Q_j]. P[all Q_j | R'] <= P[all Q_j] (Harris) <= (D-1)^k 2^{C(k,2)} a^k: one residual term
per j, chosen terms distinct (each contains exactly one j), pairwise residual overlap <= 1, union >= kL - C(k,2).
A >= P[R'](1 - k(D-1)a/2): P[z_j Q_j | R'] = (1/2) P[Q_j | R'] <= (1/2)(D-1)a. Hence
||D_J N||^2 / A <= 2^{C(k,2)-2k} ((D-1)a)^k / (1 - k(D-1)a/2) (needs k(D-1)a < 2).
sum_{T in Omega} Nhat(T)^2 <= sum_t sum_{|J|=k} ||D_J N||^2 <= A d alpha_k <= delta alpha_k/(a theta) = kappa delta. OK

Step 4 (entropy).
- On Omega (T != 0): Phi(ghat^2, hhat^2) vs 2 hhat^2. Phi(v^2,u^2) = u^2 phi((v/u)^2), phi(t) = t log2(1+1/t) + log2(1+t),
  phi(1) = 2, d/ds phi(s^2) = 2s log2(1 + 1/s^2) <= 2.33 (max near s = 0.5: 2 * 0.805/ln 2). So
  |Phi - 2u^2| <= 2.33 u |v - u| <= 2.33 |hhat| |ghat + hhat| = 4.66 |hhat||Nhat| <= (8/ln 2)|hhat||Nhat| (FEIB21's
  constant 8/ln2 = 11.54 is generous; could state 5). Cauchy-Schwarz: sum_Omega |hhat||Nhat| <= delta sqrt(kappa).
- Missing h-mass outside Omega: 2 eps delta.
- Outside Omega, T != 0: Phi(p,q) <= q log2(e (p+q)/q), concave+homogeneous => sum <= Q log2(e (P+Q)/Q) with
  Q <= eps delta, P <= sum (2|Nhat| + |hhat|)^2 <= 8 Var N + 2 delta <= 8A + 2 delta; increasing in Q, so
  <= eps delta log2(e (3 + 8A/(eps delta))) <= eps delta log2(e[3 + 8/(eps d a theta)]).  OK
- T = 0: q = delta^2, p <= 1: <= delta^2 log2(e(1 + delta^-2)); x log2(e(1+x^-2)) increasing on (0, 1/4], delta <= da.
- Lower side: E >= sum_Omega Phi >= 2(1 - eps)delta - (8/ln2) delta sqrt(kappa).  OK
Theorem (LIN) as stated in FEIB21 holds.

Corollary check: k > 1/epsilon fixed, d <= D <= 2^{(1-epsilon)L}: d gamma_k <= poly(L) 2^{-epsilon L}; kappa <=
poly(L) D^k a^{k-1} <= poly(L) 2^{(1 - k epsilon)L}; L(D-1)a -> 0; eps log2(1/(eps d a)) <= poly(L) 2^{-epsilon L} O(L).
All -> 0 uniformly in the number of terms and in i.

Not FEI for the class: restrictions of a linear uniform DNF have mixed widths (P1 needs a good coordinate in every
restriction). Lower bound side says no coordinate is better than 2: sum_i E_i = (2 + o(1)) I(f) on the class.

Plan for P6 (to decide): Thm 1 = (LIN) with explicit bound + corollary; Prop 2 = general separation inequality
(derivative spectrum on Omega, restriction weight on Omega small); Prop 3 = mates-last nested witness >= log2 D + O(1)
(FEIB21 section 5, NOT yet re-derived) linking to P5; example: star of D terms (linear, any D); numerical check of
the explicit bound on small linear DNFs with exact Walsh-Hadamard (w = 4, D = 2 etc.).
