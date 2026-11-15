# Worker FEIB30 (account acc2)

disk: small

# FEIB30 - adversary and referee for the thinning predictor: is its overhead bounded on every Boolean function?

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Everything you need is in this brief; background is ~/fei_solve_agent/FLOW.md section 12(z) items
3-5 (the last section). Code: ~/fei_solve_agent/code/predictor.py (exact, any f with n <= 14) and
predictor_sym.py (majority by closed form). `export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`; python3 has numpy.
There is no math store on this machine; do not look for one.

Setting. f Boolean on n bits, mu(S) = fhat(S)^2, U ~ mu, I = E|U|, H = H(mu).
Q(T, i) = mu(T+i)/I on pairs (T, i) with i not in T (delete a uniformly chosen element of U).
    L(f) = E_Q log2(1 + mu(T)/mu(T+i)).        FEI <=> L <= C for all f   (H - (2/ln 2) I <= I L <= H).
Predictor principle (proved, Gibbs' inequality): for ANY p_i(T) >= 0, with
    K = (1/I) sum_i sum_{T without i} (mu(T) + mu(T+i)) p_i(T):       L <= log2 K + E_Q log2(1/p_i(T)).
Thinning. Fix lam in (0,1). up_lam(T) = sum_{U >= T} mu(U) lam^|U-T| = || T_sqrt(lam) D_T f ||_2^2.
nu_lam(T) = (1-lam)^|T| up_lam(T) is the law of the sample U after deleting each element independently with
probability lam. The "thin" predictor is the conditional law of nu_lam:
    p_i(T) = nu(T+i)/(nu(T) + nu(T+i)) = (1-lam) r/(1 + (1-lam) r),   r = up_lam(T+i)/up_lam(T).
Also "ratio" p = min(1, r) and "lrat" p = lam r. Define the overhead
    Ov_lam(f) = log2 K + E_Q log2(1/p) - L(f)  >= 0.
CONJECTURE P: for some fixed lam (say 0.1 or 0.25) and one of these predictors, sup_f Ov_lam(f) < infinity.
P does not prove FEI (it bounds the gap, not L), but together with a bound on the predictor's own bound it would,
and a COUNTEREXAMPLE to "log2 K + cost <= C" with L bounded tells us the noise scale must depend on T.
Measured so far: Ov at most 0.2 on AND, tribes, PM(K33), address, random functions n <= 14; majority (L = 0):
0.22, 0.29, 0.37, 0.97, 1.45, 1.72 bits at n = 5, 9, 13, 51, 201, 801, increments shrinking.
Useful exact facts (proved): sum_{i not in T} lam up_lam(T+i)/up_lam(T) = m_lam(T) := E[|U - T| : U drawn from the
supersets of T with weight mu(U) lam^|U-T|] = posterior mean number of deleted elements given the thinned sample
is T. E_{T ~ nu_lam} m_lam(T) = lam I exactly; what matters is E_{T ~ mu} m_lam(T). Identity:
    E_mu log2(up_1(S)/mu(S)) = (1/ln 2) int_0^1 E_{T~mu} m_t(T) dt/t,   and   FEI <=> int_{1/2}^1 E_{T~mu} m_t(T) dt <= C I.
Composition law: f = F(psi,...,psi), psi balanced, T with blocks T_j, J = {j: T_j nonempty}:
    up_lam^f(T) = up_theta^F(J) prod_{j in J} up_lam^psi(T_j),    theta = sum_{S nonempty} mu_psi(S) lam^|S|.

The job, in order.
1. Referee the three displayed facts (predictor principle, m_lam identity, composition law): prove or refute each;
   check numerically on random f (n = 8) and one composed f.
2. Towers by the composition law, no brute force: compute log2 K, cost and L exactly for depth-d self-towers of
   MAJ3, AND_2 alternating with OR_2, the 2x2 and 3x3 tribes, PM(K33) (9 variables), and the balanced 4-variable
   monotone functions, d = 1..6 or until the three predictors' overheads visibly converge or diverge. This is the
   decisive test: does Ov stay bounded in depth? Give the recursion you derive (K and cost decompose over the
   level at which the deleted element's block empties).
3. Adversary. Hill-climb Ov_lam(f) (and separately the full bound log2 K + cost, and E_{T~mu} m_lam(T)/I) by
   truth-table flips at n = 8..12 from random, sparse, monotone, threshold and bent-type starts, lam in
   {0.1, 0.25, 0.5}. Then structured families at larger n by closed forms: thresholds with weights (1,..,1,m),
   recursive majority, "hidden coordinate" functions f = x_0 on a bent function's level set (quadratic bent
   g(y) = y_1 y_2 + ... + y_{2k-1} y_2k: f = x_0 if g = 1 else AND-type), tribes with unequal widths, and the
   lexicographic / threshold-of-ANDs functions that give the record H/I. Report the largest values with n and the
   function.
4. Majority exactly: prove that Ov_lam(Maj_n) converges as n -> infinity and identify the limit (use
   mu_k ~ c k^(-3/2)/C(n,k) weights; the predictor is about (k+1)/((1-lam) n)).
5. Literature check before any novelty claim: pseudo-likelihood / erasure entropy (Verdu-Weissman), spectral
   sample thinning (Garban-Pete-Schramm), noise sensitivity and D_T f norms (Keller-Kindler, Kelman-Kindler-
   Lifshitz-Minzer-Safra arXiv:1911.10579), FEI via random restrictions. Say what is already there.

Rules: one compute process at a time, at most 2 threads, nice 10, under 3 GiB; before any run longer than a
minute read `uptime` and use 1 thread if the 1-minute load is above 9. Folder under 60 MB (this disk is at its
floor: keep tables in memory, delete scratch as you go). Mark each statement PROVED, CHECKED NUMERICALLY (with
the command) or HEURISTIC. RESULTS.md as you go; REPORT.md at the end, verdict first (P broken by which function /
unbroken with the largest overhead seen / tower recursion and its limit).

