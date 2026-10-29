# Audit of Theorem 3 (T354, general_A/THEOREM.md lines 114-175)

agent D, 21 Oct 2026 14:0x. Independent line-by-line pass, as owed to agent A. Commit audited: the file as of
d6d99a1a (Theorem 3 from 429bcc5f plus the author's second and third passes).

Verdict: PASS WITH CORRECTIONS. The argument is sound: the coupling at y = x_{tau-1} with l epochs of lookback gives the
frozen drift as an exact conditional mean, and the rate rho_* + O(T^(-1/4) polylog) follows. Three corrections are needed.
None of them changes the order of the rate or the residual: one is a missing condition on T, and two are dimension
factors in the explicit constants.

## Checked and holds

1. |mhat_kj| <= G (m_k is a convex combination of gradients with total weight 1 - b1^k), so |u_kj| <= U = G/eps. The
   descent lemma (1) with |u_k|_2^2 <= d U^2 holds.
2. The v floor. Any 2n - 1 consecutive slots contain a whole aligned epoch. Over that epoch the iterates move at most
   n sqrt(d) U eta (the proof uses 2n, which is conservative), so |g_ij(x_s)^2 - g_ij(x_ref)^2| <= 2G Lg |x_s - x_ref|.
   The epoch's squared gradients sum to at least n beta - 4 n^2 G Lg sqrt(d) U eta >= n beta/2 exactly when
   eta <= eta_0. v_k >= v_lo/2 and vhat >= v. The frozen filter at y has vt >= v_lo. Both hold. The floor also holds for
   n <= k < 2n, because epoch 1 is then wholly in the past with weight at least b2^(2n), so the case l = 0
   (eta_T >= 1, possible when eps is large) is covered too.
3. Lam is the Lipschitz constant of (m, v) -> m/(sqrt v + eps) on [-G, G] x [v_lo/2, inf): the partials are at most 1/eps
   and G/(2 eps^2 sqrt(v_lo/2)), and the domain is convex. Holds.
4. Early epochs (checked hardest, as asked). Take E_e = (e - 1) n + 1 and tau = E_{e-l}. For k in epoch e, k <= e n, and
   tau >= k/2 is equivalent to (e - 2l - 2) n + 2 >= 0, true for e >= 2l + 2. So eta_tau <= sqrt(2) eta_k exactly from
   e = 2l + 2 on. For l < e <= 2l + 1 the ratio is unbounded (e = l + 1 gives tau = 1), as the remark says. The crude bound
   on the first 2l + 2 epochs, |grad f . u| <= |grad f|_2 |u|_2 <= d G U and sum_{k <= N} k^(-1/2) <= 2 sqrt(N), gives
   2 eta d G U sqrt((2l + 2) n). Holds.
5. Measurability. y = x_{tau-1} is fixed by the permutations of epochs 1..e-l-1, since slot tau - 1 is the last slot of
   epoch e - l - 1. The permutations of epochs e-l..e are fresh and uniform. Holds.
6. The radius. For tau <= j <= k, |x_{j-1} - y| is at most k - tau <= (l + 1) n - 1 steps, each at most sqrt(d) U eta_tau,
   so r = sqrt(d) U (l + 1) n eta_tau. The filter differences (Lg r on the slots tau..k with total weight <= 1, 2G b1^(k-tau)
   and 2G^2 b2^(k-tau) on the earlier slots, and the bias-correction terms G b^k/(1 - b^k), G^2 b^k/(1 - b^k)) hold, with
   k - tau >= l n giving b^(ln).
7. The conditional mean (3). Once the slots before tau are replaced by an independent stationary past made of iid uniform
   permutations aligned to epoch starts (tau is an epoch start, so the alignment is right), ut_k is a function of y and of
   an iid permutation stream independent of F, read at phase p(k). Its conditional mean is h_{p(k)}(y), and the n phases
   of epoch e sum to n h(y). This is the step the averaging hypothesis of Theorem 2 lacked, and it is correct as written.
   It also removes the correlation between grad f(x_{k-1}) and u_k through slot k's own example, because that example is
   inside the fresh stream.
8. grad f . h >= W with rho_j := |h_j - d_j f phi_j|. Cauchy-Schwarz gives sum_j |d_j f| rho_j(y) <= a rho_*, so
   W + rho_*^2/4 >= (a - rho_*/2)^2 >= 0 even when W < 0. Then a <= rho_*/2 + sqrt(W + rho_*^2/4), concavity of sqrt over
   the weights n eta_e, and sqrt(x + y) <= sqrt x + sqrt y. The y_e are iterates, so the min is at most the weighted
   average. Holds.
9. Step-size variation inside a block: the drops eta_{E_e} - eta_e over the epochs telescope to at most eta_1, so the cost
   is n eta d G U. The choice of l: |log b| >= 1 - b gives (l + 1) n <= 2n + log(1/eta_T)/(1 - b). For eta_k = eta/sqrt(k),
   sum eta_k >= 2 eta (sqrt(T + 1) - 1) and sum eta_k^2 <= eta^2 (1 + log T). Hold.
10. Non-vacuity of (A1)-(A2): f_1 = x + cos x and f_2 = -x + cos x on R give B2 = 1 + sin^2 x >= 1, |g| <= 2, and f = cos x
    is bounded below, so the class is not empty in d = 1.

## Corrections

C1 (statement): "for every horizon T" is too strong. The proof divides by the coupled-epoch sum
sum_k eta_k - 2 eta sqrt((2l + 3) n), not by sum_k eta_k as B_T displays it. For T < (2l + 2) n there is no coupled epoch at
all, and the y_e over which the min is taken do not exist. Fix: state the bound for T >= T_0, where T_0 is the least T with
sqrt(T + 1) - 1 >= 2 sqrt((2l + 3) n), roughly 4 (2l + 3) n. There the coupled sum is at least half of sum_k eta_k, so B_T holds
with its denominator halved, that is with a factor 2. Alternatively, write B_T with the reduced denominator. T_0 grows only
like log T/(1 - b) through l, so it exists.

C2 (constant K_1): the sqrt(d) sits on the wrong term. From (2), the term sqrt(d) G |u_k - ut_k|_2 with
|u_k - ut_k|_2 <= sqrt(d) max_j |u_kj - ut_kj| is d G Lam [(1 + 2G) Lg r + ...]. With r = sqrt(d) U (l + 1) n eta_tau this
is d^(3/2) G U Lam Lg (1 + 2G) (l + 1) n eta_tau. K_1 has d U G Lam Lg (1 + 2G), which is short by sqrt(d). The same
answer comes from Hölder: |grad f(y) . (u - ut)| <= |grad f(y)|_1 |u - ut|_inf <= d G c. The other r term,
sqrt(d) U Lg r = d U^2 Lg (l + 1) n eta_tau, is over-covered by K_1's d^(3/2) U^2 Lg. That does not compensate, because
U^2 = U G/eps <= U G Lam. The explicit constant also leaves out the sqrt(2) from eta_tau <= sqrt(2) eta_k. Corrected:
    K_1 = sqrt(2) [ d U^2 Lg + d^(3/2) G U Lam Lg (1 + 2G) ] + Lg d U^2/2 + 4 d G Lam (G + G^2).
The last term comes from two b^(ln) pieces, one in (2) and one in the replacement in (3), each 2 d G Lam (G + G^2) eta_T eta_k
<= 2 d G Lam (G + G^2) eta_k^2. The statement has 2 sqrt(d), which is the same dimension slip.

C3 (constant K_0): for the same reason, the bias-correction piece is eta d G Lam (G + G^2) b/(1 - b)^2, not sqrt(d) times
that.

## Minor

- If T is not a multiple of n, the last partial epoch cannot use the phase sum. Bound it crudely by n eta_T d G U, which is
  lower order. Worth one clause.
- "The steps k < 2n contribute at most 2n eta d G U": this is already inside the first 2l + 2 epochs' crude bound and can go.
- K_0 depends on T through l. That is consistent with the O(.) form of B_T, but it is not a constant, as the name suggests.

## What this audit does not cover

Proposition 1 itself is taken as audited (the author's pass and kappa_exact.py). Theorem 2's tracking sketch is superseded by
Theorem 3 for the rate and was not re-audited. The empirical rate tests are falsification checks and agree with the theorem.
They do not bear on C1-C3.
