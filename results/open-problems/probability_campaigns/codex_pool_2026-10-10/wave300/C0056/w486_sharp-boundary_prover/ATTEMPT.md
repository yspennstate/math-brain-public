# C0056: sharp boundary of the unrenormalized Born route

Author: native worker w486, 2026-10-10. Author proof only; independent referee w488 pending. Served-model identity is not established by the requested settings. No originality, parent-problem solution, or formal-verification claim is made.

## Exact target and sources

The intake, problems.jsonl:56, asks for both a.c. spectrum of the weak-disorder Anderson operator on Z^3 and GOE local statistics for its finite-volume restriction. Its primary source is Paul Bourgade, *Random band matrices*, ICM 2018, arXiv:1807.03031, Section 2.1, printed p. 7: https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf . The source uses centered iid site potentials with variance one, nearest-neighbor hopping with free band [-2d,2d], and periodic finite-volume boxes. It discusses GOE statistics at the microscopic volume scale separately from infinite-volume spectral type; it does not provide a theorem transferring one to the other.

A precise spectral subtarget for this lane is: for the specified uniform law on [-sqrt(3),sqrt(3)] (mean zero, variance one), find lambda_0 > 0 and a deterministic nonempty open interval I in (-6,6) such that, for every fixed 0 < lambda < lambda_0, almost surely the a.c. part of H_lambda restricted to I is nonzero. Pure a.c. spectrum on I is a stronger possible conclusion. Probability-one events may depend on the fixed coupling. An operational GOE target would require the periodic-box bulk eigenvalue process, unfolded by volume times the density of states, to approach the unit-density GOE bulk process as volume increases at fixed disorder; the source's qualitative discussion does not specify all the needed density/energy quantifiers. This proof attempts neither that convergence nor a theorem relating it to a.c. spectrum.

The primary September 23, 2026 OpenAI manuscript at https://github.com/openai/math/tree/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026 claims pure a.c. spectrum for iid uniform [-1,1] potentials on a fixed interval above the lower free band edge, for each sufficiently small fixed positive coupling. Changing to variance-one uniforms rescales coupling by sqrt(3). Its main theorem is a primary proof claim, not a mathematical verdict in this packet. Its repository README says verification varies across manuscripts. Current openness is UNKNOWN; the GOE clause is not covered by that claimed theorem.

## Prior-attempt digest and brain scars

C0056-A001, attempts.jsonl:45, explored tree transfer. Its stated gap is that the lattice Green-function recursion is not closed, and deleting edges to obtain a tree changes the operator. It gave no theorem for Z^3. Its finite-time comparison is not used as a checked quantitative fact here. Targeted C0056 searches in attempts_H_20260912, attempts_I_20260914 and the Lean intake found no additional matching proof artifact. The named Team O board has no C0056 row.

The bounded brain recall completed. Its relevant math memories were openproblem_recon_fpp_chi_target_2026_08_09 (an older openness check, superseded by the September claim) and rank_lane_the_support_rank_deficit_is_theta_log_n_2026_08_19 (the object controlled by a lemma must match the target). The explicitly requested perceptron_proof_open_gaps_fleet_2026_07_12 scar warns that a green pipeline does not close unchecked mathematical gaps. These are hints, not proof premises.

## L1. Rare coherent cubes, with a universal probability-one event

Let d >= 1. Let V_x be iid real variables with a compactly supported law mu and M = ess sup |V_x| > 0. Choose a fixed m in supp(mu) with |m| = M. For each integer L >= 1, put p_L = mu({v: |v-m| < 1/L}) > 0. On a cube of L^d distinct sites, the event that every potential lies within 1/L of m has probability p_L^(L^d), by independence of those sites. For infinitely many pairwise disjoint translates of that cube, these events are independent. The probability of no success after the first J translates is (1-p_L^(L^d))^J -> 0. The same calculation after every finite starting index proves infinitely many successes almost surely. Intersect over the countably many L. This gives one probability-one event on which suitable cubes exist for every L and can be chosen to escape every finite set. No conditional bounds or adaptively exposed rows have been multiplied.

Let H0 psi(x) = -sum_j(psi(x+e_j)+psi(x-e_j)). For any E in [-2d,2d], choose k in [-pi,pi]^d with -2 sum_j cos(k_j) = E. On a successful cube Q_L define psi_L(x) = L^(-d/2) exp(i k.x) 1_{Q_L}(x). Then ||psi_L|| = 1 and ||(V-m)psi_L|| <= 1/L. Each of the 2d shift directions has cutoff defect with squared norm 2/L. The triangle inequality therefore gives

    ||(H0-E)psi_L|| <= 2d sqrt(2/L) -> 0.

The event is independent of E, k, lambda and eta; only the chosen vectors depend on them. Thus this construction holds simultaneously for all E in the closed free band, including the endpoints.

Also intersect the L1 event with the probability-one event |V_x|<=M for every x in Z^d. Each individual site has this bound almost surely, and the lattice is countable. All subsequent operator estimates are on this intersection, so ||V||<=M is available simultaneously with every coherent cube. This makes explicit the support-bound step requested by w487's scoped KEEP receipt.

## L2. Exact power norms and convergence threshold

On the event in L1, fix any lambda > 0, eta > 0 and E in [-2d,2d]. Define

    z = E+i eta, R0 = (H0-z)^(-1), K = lambda V R0,
    a = (E-z)^(-1) = i/eta, b = lambda m a, c = lambda M/eta.

The free Fourier symbol has full range [-2d,2d], so the self-adjoint resolvent has ||R0|| = 1/eta. In particular ||K|| <= c. With r_L = (H0-E)psi_L, the exact resolvent identity on psi_L is

    R0 psi_L - a psi_L = -a R0 r_L.

Hence ||R0 psi_L-a psi_L|| <= ||r_L||/eta^2, and

    ||K psi_L-b psi_L|| <= lambda M ||r_L||/eta^2 + lambda/(eta L) -> 0.

Thus b is an approximate eigenvalue of K, even though K need not be normal. Since |b| = c, this already proves ||K|| = c and spectral radius r(K) = c: the upper bound is r(K) <= ||K|| <= c, while approximate eigenvalues belong to the spectrum.

For every fixed integer n >= 1, the telescoping identity

    (K^n-b^n)psi_L = sum_{j=0}^{n-1} b^j K^(n-1-j)(K-b)psi_L

implies ||(K^n-b^n)psi_L|| <= n c^(n-1) ||(K-b)psi_L|| -> 0. Comparing lower and upper norm bounds gives, for all n >= 0,

    ||K^n|| = c^n,
    ||R0 K^n|| = eta^(-1) c^n.

For the second equality, apply R0 to the preceding approximate-eigenvector identity and use R0 psi_L -> a psi_L; the upper bound is ||R0|| ||K^n||. These claims hold for all parameters on the same probability-one event.

The factorization H_lambda-z = (I+K)(H0-z) is exact. If c < 1, the operator-norm Neumann series sum_n (-K)^n converges, and H_lambda's resolvent equals R0 sum_n (-K)^n. If c >= 1, the terms R0(-K)^n have norms eta^(-1)c^n which do not tend to zero. The Born resolvent series therefore fails to converge in operator norm. The exact threshold is

    eta > lambda M.

At eta = lambda M, failure is already forced by nonvanishing terms. At eta < lambda M, their norms grow exponentially. This is stronger than merely observing that a sufficient norm bound fails; the proof establishes necessity using genuine approximate eigenvectors.

## L3. Centering and disorder averaging do not remove this obstruction

If E[V_x]=0, then E[K]=0 in the weak-operator sense. Nevertheless L2 gives, for every n >= 0,

    E[||R0 K^n||] = eta^(-1)(lambda M/eta)^n.

Uniform [-1,1] disorder has M=1; variance-one uniform [-sqrt(3),sqrt(3)] disorder has M=sqrt(3). Thus centering alone cannot justify a disorder-averaged operator-norm contraction as eta -> 0 at fixed lambda. This makes no claim about cancellation in individual matrix elements, fractional moments, renormalized expansions, or spectral type.

## Single hardest gap and scope

No lemma here proves or disproves Anderson delocalization. The original spectral gap is still to establish nonzero a.c. mass by a valid fixed-disorder, infinite-volume boundary-limit argument. The GOE clause remains an additional unsolved obligation in this packet. The result rules out only a bridge asserting that sufficiently small fixed disorder makes the unrenormalized Born series converge in operator norm down to eta=0. It does not attack the new manuscript's adaptive resolvent method.

NEXT: Have w488 check L1's independence and universal event, L2's approximate-eigenvalue and full-series necessity, and the separation from a.c./GOE conclusions.
