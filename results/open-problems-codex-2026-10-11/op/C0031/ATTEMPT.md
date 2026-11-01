# C0031 — research record, 2026-10-11

## Target and source verification (in progress)

The intended target is the unrestricted almost-sure upgrade of the heavy-tailed circular law, without a bounded-density hypothesis. The survey was fetched directly from https://arxiv.org/pdf/1109.3343. The open remark is on printed page 39, immediately following Theorem 6.2. Section 6.6, containing the bounded-density upgrade proof, is on printed page 51.

**Exact model worked on:** an infinite iid complex array (X_ij), its upper-left n by n blocks, 0 < alpha < 2, t^alpha P(|X_11| >= t) -> 1, and weak convergence of the conditional angle law X_11/|X_11| given |X_11| >= t to a probability measure on the unit circle. Write A_n = n^{-1/alpha} X_n. The target is mu_(A_n) -> mu_alpha weakly almost surely, with no smoothness assumption. All conditional results below also apply to any other coupling of the blocks with the same iid law within each block.

**Normalization warning:** a generic stable domain of attraction has P(|X| >= t) = t^{-alpha} L(t), with slowly varying L, and uses the quantile scale a_n = n^{1/alpha} ell(n). It does not in general justify exactly n^{-1/alpha}. The source question uses the normalized tail above. This is a scope correction, not a counterexample to the intended upgrade.

The verified Section 6.6 already proves the upgrade under bounded density, using polynomial extreme-singular-value bounds and concentration of a clipped logarithm. Accordingly the unrestricted problem must not be declared solved merely by citing that section.

## A complete scalar concentration reduction

Here is a reduction that avoids claiming that a polynomial minimum singular value alone gives logarithmic uniform integrability.

**Proposition.** Let A_n(z) be random n by n complex matrices with independent rows (a deterministic shift is allowed). Write

L_n(z) = n^{-1} log |det A_n(z)|.

Fix z. Suppose (i) L_n(z) converges in probability to a finite deterministic number ell(z); (ii) for some constant b > 0, with probability one all singular values of A_n(z) belong to [n^{-b},n^b] for every sufficiently large n. Then L_n(z) converges almost surely to ell(z). No independence between different n is needed.

**Proof.** For n >= 2 let h_n(s) be log(s) clamped to [-b log n,b log n], with h_n(0) = -b log n. It is bounded, continuous and nondecreasing, with total variation V_n = 2b log n. Let S_n be the average of h_n over the n singular values. Assumption (ii) implies S_n = L_n eventually almost surely.

Changing one row of A changes S_n by at most V_n/n. Indeed, delete that row and let C be the common (n-1) by n matrix. The two Gram matrices have the form C* C + r* r and C* C + q* q. For a positive rank-one addition, the ordered eigenvalues interlace the eigenvalues of C* C; hence the numbers of eigenvalues below any fixed threshold differ by at most one between the two Gram matrices. Taking square roots gives the same bound for the singular values. Their normalized empirical distribution functions differ by at most 1/n. Integration by parts against the bounded monotone function h_n, whose boundary terms cancel because both measures have mass one, bounds the difference of their integrals by V_n/n.

The independent-row bounded-differences inequality therefore gives

P(|S_n - E S_n| >= t) <= 2 exp(-2 n t^2 / V_n^2).

For each fixed t > 0 this bound is summable. To see this explicitly, eventually (log n)^2 <= sqrt(n), so the bound is at most 2 exp(-c sqrt(n)); grouping n between k^2 and (k+1)^2 bounds its sum by a constant multiple of sum_k (2k+1) exp(-c k), which is finite. Borel-Cantelli for t = 1,1/2,1/3,... gives S_n - E S_n -> 0 almost surely.

Since S_n = L_n eventually almost surely, S_n -> ell(z) in probability. The deterministic sequence E S_n must therefore tend to ell(z): if |E S_n - ell(z)| >= epsilon along a subsequence, the simultaneous events |S_n - E S_n| < epsilon/3 and |S_n - ell(z)| < epsilon/3 have probability tending to one but have empty intersection, a contradiction. Consequently S_n, and then L_n, converge to ell(z) almost surely. This proves the proposition.

The interlacing step uses the min-max characterization: for H >= 0 and H' = H + v v*, ordered increasingly, lambda_j(H) <= lambda_j(H') <= lambda_{j+1}(H) for j < n; the upper bound follows by restricting trial subspaces to v-perp, which lowers dimension by at most one. This also covers repeated eigenvalues and zero singular values.

## What is still missing

This proposition is conditional. It does not prove the required almost-sure polynomial lower bound for the unrestricted entry law. The survey's Appendix A bound has a 1/sqrt(n) term and cannot itself give summability. Modern invertibility results are being checked for the exact hypotheses.

The scalar proposition alone is not a proof of the full problem. The following sections supply the missing potential compactness step and a proved special case.

## Power-law anti-concentration special case

**Theorem (proved here; no novelty claimed).** Under the exact source hypotheses above, suppose additionally that constants C, eta > 0 satisfy

Q_X(r) := sup_(w in C) P(|X_11-w| <= r) <= C r^eta, for 0 < r <= 1.

Then the empirical eigenvalue measures of A_n converge weakly to mu_alpha almost surely. This includes entry laws singular with respect to both real and complex Lebesgue measure, as the example below shows. It excludes every law having an atom.

We use the source's established, unrestricted convergence **in probability of logarithmic potentials**: for each fixed z, n^{-1} log|det(A_n-zI)| -> ell(z) in probability, with ell the logarithmic potential (positive-log convention) of mu_alpha. This is established by the Hermitization argument in Sections 6.2–6.5 and explicitly invoked at the start of Section 6.6. Merely weak convergence of the eigenvalue measures in probability would not imply this stronger input.

### 1. Smallest singular value, with the probability quantified

For any deterministic shift M of X_n and r > 0,

P(s_min(X_n+M) <= r) <= n Q_X(nr).

Here and below Q_X is defined for all positive radii; the power bound is invoked only when nr <= 1. To prove the estimate, let R_i be the rows and H_i the span of all other rows. Deterministically,

min_i dist(R_i,H_i) <= sqrt(n) s_min(X_n+M).

For an invertible matrix B, the squared Frobenius norm of B^{-1} equals sum_i dist(R_i,H_i)^{-2}. In detail, let c_i be its ith column and use the Hermitian inner product <x,y>=sum_j x_j conjugate(y_j). Then the vector conjugate(c_i) is perpendicular to all rows except R_i and <R_i,conjugate(c_i)>=1. Since H_i has codimension one, the orthogonal projection of R_i onto H_i-perp is a scalar multiple of conjugate(c_i), and its norm is 1/||c_i||. Hence ||c_i||=dist(R_i,H_i)^{-1}; summing squared column norms proves the identity. Thus ||B^{-1}|| <= sqrt(n)/min_i dist(R_i,H_i), which proves the inequality after inversion. For a singular square matrix some row is in the span of the others, so the left side is zero and the inequality remains valid.

Condition on all rows other than R_i and choose a measurable unit vector v perpendicular to H_i. Such a choice can be made by Gram-Schmidt with a fixed order of coordinate vectors, choosing the first nonzero projected vector. The choice depends only on those other rows. The event dist(R_i,H_i) <= sqrt(n) r implies |<R_i,v>| <= sqrt(n) r. Some coordinate of v has magnitude at least 1/sqrt(n); select the first such coordinate j. After also conditioning on all other coordinates of R_i, this last event puts X_ij into a disk of radius at most n r, with an arbitrary center. Independence bounds its conditional probability by Q_X(nr). A union bound over the n rows proves the estimate. The shift M is unrestricted and may be complex.

Apply this to M = -n^{1/alpha} zI and r = n^{1/alpha-b}. Then, eventually,

P(s_min(A_n-zI) <= n^{-b}) <= C n^{1+eta(1+1/alpha-b)}.

Choose b > 1 + 1/alpha + 2/eta. The exponent is strictly below -1, so Borel-Cantelli gives the desired polynomial lower bound eventually almost surely for each fixed z.

### 2. Polynomial upper bound

Choose 0 < kappa < alpha. The tail assumption gives E|X|^kappa < infinity by tail integration. For B > 3/kappa,

P(max_(i,j <= n) |X_ij| > n^B) <= E|X|^kappa n^{2-B kappa},

a summable bound. Since ||X_n|| <= ||X_n||_F <= n max|X_ij|, almost surely eventually ||A_n-zI|| <= n^{B+1-1/alpha}+|z|. Enlarging b makes this at most n^b eventually. The scalar proposition now proves convergence of the logarithmic potential almost surely for each fixed z. Fubini over probability times area measure, then a countable union of disks, makes this simultaneous for Lebesgue-almost every z on one event of probability one. Determinants and potentials are measurable; the finite limit ell(z) exists at almost every z, in fact the source limit has a continuous bounded density and stretched-exponential tail.

### 3. Uniform fractional moment bound, proved independently

The next bound needs only the source's tail assumptions. Fix 0 < p < alpha/4 and put q = p/2. Almost surely,

sup_n (1/n) sum_(i=1)^n s_i(A_n)^p < infinity.

To prove it, put beta = alpha/2 < 1 and W = |X|^2. There is C_0 such that P(W > u) <= C_0 u^{-beta} for all u >= 1. For each row let Y_(k,n) = n^{-1/beta} sum_(j=1)^n W_kj. For t >= 1, set u = t n^{1/beta}. Splitting off the event max_j W_kj > u, and then applying Markov to the sum of W_kj 1_(W_kj <= u), gives

P(Y_(k,n) > t) <= n P(W > u) + (n/u) E[W 1_(W <= u)] <= C_1 t^{-beta}.

The last inequality follows from E[W 1_(W <= u)] <= integral_0^u P(W > x) dx <= C_2 u^{1-beta}, with the bounded contribution from x <= 1 absorbed into C_2. Consequently sup_n E Y_(k,n)^r < infinity for every 0 < r < beta, by integrating the uniform tail bound. Since 4q = 2p < beta, the variables Z_(k,n) = Y_(k,n)^q have uniformly bounded fourth moments. For each n they are independent across rows. Expanding the fourth power of their centered sum, terms with an index occurring only once vanish by independence and centering, and the remaining terms are the n fourth moments and the 6 binomial(n,2) products of second moments. Thus

E |(1/n) sum_k (Z_(k,n)-E Z_(k,n))|^4 <= C_3/n^2.

Markov and Borel-Cantelli at each rational positive tolerance imply that this centered average tends to zero almost surely, without requiring independence across n. Its expectation is uniformly bounded. Hence the averages of Z are bounded almost surely.

Finally, Schur-Horn majorization for A_n A_n* and concavity of x -> x^q, 0 < q < 1, give

sum_i s_i(A_n)^p = Tr((A_n A_n*)^q) <= sum_k (sum_j |(A_n)_kj|^2)^q = sum_k Z_(k,n).

This proves the stated moment bound. Weyl's multiplicative eigenvalue/singular-value inequalities also give sum_i |lambda_i(A_n)|^p <= sum_i s_i(A_n)^p. Here are details of that implication, including zeros. Put a_i=|lambda_i(A_n)| and b_i=s_i(A_n), each in decreasing order. Weyl gives product_(i<=k) a_i <= product_(i<=k) b_i for each k. Set log(0)=-infinity. For each real t,

sum_i (log(a_i)-t)_+ = max_(0<=k<=n) [sum_(i<=k) log(a_i)-kt] <= max_(0<=k<=n) [sum_(i<=k) log(b_i)-kt] = sum_i (log(b_i)-t)_+,

where the k=0 term is zero and a partial sum containing log(0) is -infinity. Thus no undefined subtraction of infinities is needed. For a>0, direct integration gives p^2 integral_(-infinity)^infinity e^{pt}(log(a)-t)_+ dt=a^p; for a=0 both sides are zero by convention. Integrating the displayed finite-sum inequality proves sum_i a_i^p<=sum_i b_i^p. This uses Weyl's standard finite-matrix product theorem and does not assume normality.

### 4. Passage from potentials to measures

Here are details to avoid silently assuming almost-sure log uniform integrability near zero. For probability measures rho_n with uniformly bounded pth moments, their positive-log potentials

V_n(z) = integral log|z-w| rho_n(dw)

are uniformly bounded in L^2(K) for each bounded disk K. To prove this, split at |w| <= 2R+2 if K has radius R centered at zero. In this part the L^2(K) norm of log|z-w| is uniformly bounded in w: change variables u=z-w and bound the integral of |log|u||^2 on a fixed disk. It is finite because integral_0^1 r |log r|^2 dr is finite and the part away from zero is bounded. For |w| > 2R+2, we have |w|/2 <= |z-w| <= 3|w|/2, and thus |log|z-w|| <= log|w|+log 2 <= |w|^p/p+log 2. Minkowski's inequality now bounds ||V_n||_(L^2(K)) by a constant depending on R,p and the common moment bound.

On the probability-one event constructed above, V_n -> ell almost everywhere. Fatou gives the same L^2 bound for ell. Egorov's theorem on K, together with Cauchy-Schwarz on a set of arbitrarily small area, then proves V_n -> ell in L^1(K): outside the small set convergence is uniform, while the integral over the small set is at most a common L^2 bound times its square-root area.

The identity Delta log|z-w| = 2 pi delta_w in distributions follows by integration by parts outside a disk of radius epsilon about w and then taking epsilon down to zero: the inner boundary normal derivative contributes 2 pi phi(w), and the remaining boundary term is O(epsilon |log epsilon|). It follows that for each smooth compactly supported test function phi,

integral phi d rho_n = (1/(2 pi)) integral V_n Delta phi d area -> (1/(2 pi)) integral ell Delta phi d area = integral phi d mu_alpha.

Thus the eigenvalue measures converge vaguely to mu_alpha. The pth moment bound ensures tightness by rho_n(|w| > T) <= T^{-p} integral |w|^p rho_n(dw). Approximation of compactly supported continuous functions by smooth ones extends vague convergence to continuous compactly supported tests. For any bounded continuous function, cut off outside a large disk using tightness of both the sequence and mu_alpha; the tails have arbitrarily small contributions. This proves weak convergence. The special-case theorem is complete.

## A singular entry law covered by the theorem

Let K be an integer-valued positive variable with P(K >= k) = k^{-alpha}, k=1,2,..., and independently let U = sum_(j>=1) 2 B_j/3^j, where B_j are iid fair {0,1} bits. Set X = K+U. For t -> infinity, squeezing between P(K >= ceil(t)) and P(K >= ceil(t-1)) gives t^alpha P(X >= t) -> 1. The angle is identically 1.

The Cantor variable U has Q_U(r) <= C r^d, d=log(2)/log(3). Indeed, choose m with 3^{-(m+1)} < 2r <= 3^{-m}. An interval of length 2r meets at most two of the level-m Cantor intervals, each of mass 2^{-m}, so its probability is at most 2*2^{-m} <= 2*(6r)^d. Complex disks meet the real axis in intervals of length at most 2r. Conditioning on K and translating the center gives the same bound for X. For larger r the bound is obtained by enlarging C. The law of X is supported on the countable union of translates of the Cantor set, a real Lebesgue-null set; it has no density on either R or C. The special-case theorem therefore supplies almost-sure convergence for this law for every alpha in (0,2).

## Hostile-referee checkpoints

1. The source assumption t^alpha P(|X|>=t)->1, not generic regular variation with an unspecified scale, is essential to the formulation used here.
2. A polynomial minimum alone does not imply logarithmic uniform integrability; the reduction instead uses established in-probability potential convergence and concentration. A diagonal example in the numerical checks reproduces this distinction.
3. Real bounded-density estimates under a complex deterministic shift must condition on a complex linear coefficient; the small-ball proof uses disks, so it covers this without incorrectly treating the shifted law as having a planar density.
4. The n Q_X(nr) factor includes both the sqrt(n) row-distance factor and the sqrt(n) coordinate factor.
5. A power bound on Q excludes atoms; no claim has been made for atomic heavy tails.
6. Almost-sure convergence separately at every z is not asserted uniformly over all z; Fubini provides the required almost-everywhere simultaneous statement.
7. Interlacing and the clamped-log bounded-differences estimate are checked numerically on row replacements. Numerical tests are consistency checks only.
8. Lean formalizes only the algebraic contradiction used to identify the deterministic centering sequence. It does not formalize the probability theorem or the special-case theorem. The command `lake env lean ~/brain_workers/TRIO_1011/op/C0031/Centering.lean`, run from ~/lean_verify with an hour timeout, completed with exit code 0 and no diagnostics. See LEAN_CHECK.txt. Both declarations use ordinary kernel-checked proofs, with no sorry or native_decide.

**Negative control, fully proved.** For n>=3, let m_n=floor(n/log n) and let D_n have m_n diagonal entries 1/n and all remaining diagonal entries 1. Its singular empirical measures converge weakly to delta_1, since m_n/n <= 1/log n -> 0, while s_min(D_n)=1/n. Nevertheless for every fixed 0<epsilon<1, eventually the negative-log integral below epsilon is (m_n/n) log n, which tends to 1: its difference from 1 is between -log n/n and 0. Thus deterministic polynomial s_min bounds alone do not imply negative-log uniform integrability. This example is not iid and is not a counterexample to C0031. The numerical checks at n up to 100000 agree with the exact limit.

The row-replacement check used 200 trials of square complex matrices of sizes 2,3,5,10,20, each with one independently replaced row. The maximum difference of singular counts was 1 and the largest observed ratio to the clamped-log bounded-difference bound was 0.9467106547622932. Scripts and raw numbers are `checks.py` and `checks.json`. Memory use is small (largest dense matrix 20 by 20).

An additional exact-rational finite Cantor check enumerates 2^10 truncations and checks closed intervals of length 3^{-m} for 1<=m<=10. The bound checked is at most 2*2^{10-m} points per interval. All ten checks passed; see cantor_check.py and cantor_checks.json. This validates a finite geometric component of the example, not the infinite-law or probability theorem; its analytic proof is above.

## Remaining unrestricted gap

For an arbitrary entry law satisfying the exact source tail and angle hypotheses, especially atomic laws, prove a summable lower-tail bound for s_min(A_n-zI) at some polynomial threshold, for Lebesgue-almost every fixed z, or find another way to control the discrepancy between the actual and clipped log determinants almost surely. The source Appendix A bound has an unsummable n^{-1/2} term. The concentration and moment/potential arguments above would finish the upgrade given this missing input. No counterexample to the unrestricted model has been established.

## An independently checked atomic convolution subclass

The prior September handoff suggests a different subclass, which can be checked using a theorem already in the source. Assume the source entry X has the distribution H+sigma Z, where H and Z are independent, sigma>0, Z is centered with unit variance, and H satisfies the source's normalized tail and angular hypotheses. Assume iid copies of these pairs are used entrywise. Then the almost-sure conclusion holds, even if H and Z and hence X are purely atomic. No novelty is claimed; this verifies the prior hint rather than treating it as authority.

First, X retains the normalized tail and angular law. For fixed epsilon>0, Markov gives P(|sigma Z|>epsilon t)=O(t^{-2})=o(t^{-alpha}). The triangle inequality sandwiches P(|H+sigma Z|>=t) between P(|H|>=(1+epsilon)t)-o(t^{-alpha}) and P(|H|>=(1-epsilon)t)+o(t^{-alpha}). Taking t to infinity and then epsilon down to zero proves t^alpha P(|X|>=t)->1. For the angle, on the event |sigma Z|<=epsilon t and |X|>=t, we have |H|>=(1-epsilon)t and the two unit directions differ by at most O(epsilon). For any continuous test function on the unit circle, uniform continuity therefore bounds the difference of its values by a quantity tending to zero as epsilon decreases. The discrepancy between the tail events |X|>=t and |H|>=t is bounded by the probability that |H| lies in [(1-epsilon)t,(1+epsilon)t] plus o(t^{-alpha}); divided by P(|H|>=t), its limsup tends to zero with epsilon. This proves the same conditional angular weak limit for X.

Fix z and choose 0<kappa<alpha. Then E|H|^kappa<infinity. As in section 2 above, there is a deterministic d such that the event ||sigma^{-1}(H_n-n^{1/alpha}zI)||>n^d has summable probability. Set M_n=sigma^{-1}(H_n-n^{1/alpha}zI). Conditional on H_n, the matrix Z_n still has iid centered unit-variance entries, and

X_n-n^{1/alpha}zI = sigma (Z_n+M_n).

Apply the source's Lemma 4.12 (printed pages 20–21) to this finite-variance noise: for every a,d>0 there is beta>0 such that, uniformly over deterministic M with ||M||<=n^d,

P_Z(s_min(Z_n+M)<=n^{-beta}) <= n^{-a}

for all sufficiently large n. Choose a=3. Unconditioning and adding the summable core-norm failure probability gives a summable bound for the failure of s_min(Z_n+M_n)>=n^{-beta}. Hence Borel-Cantelli yields s_min(A_n-zI)>=sigma n^{-beta-1/alpha} eventually almost surely. This is at least n^{-b} eventually for some fixed b. The polynomial upper bound follows from the tail of X. The scalar concentration proposition, the established in-probability potential limit for X, and the complete moment/potential passage above prove the almost-sure weak convergence.

**Atomic example.** Let H=K with P(K>=k)=k^{-alpha} as in the Cantor example, let Z be an independent fair Rademacher sign, and let sigma=1. Then X=K+Z is integer-valued (it has, among others, an atom at zero), still has normalized tail constant one and angular limit at 1, and satisfies the theorem. This does not cover an arbitrary atomic heavy-tail law, because a nontrivial independent convolution factor is an additional structural hypothesis.

## A further extension: logarithmic anti-concentration

The polynomial threshold in the scalar proposition is a sufficient condition, not a necessary one. Repeating its proof with h_n(s) = log(s) clamped to [-a_n,a_n] works whenever the actual singular values eventually belong to [exp(-a_n),exp(a_n)] almost surely and, for each t>0,

sum_n exp(-n t^2/(2a_n^2)) < infinity.

All other steps of the proof are identical, because the total variation is 2a_n. This supplies a somewhat larger proved special case. Suppose instead of the power-law bound that

Q_X(r) <= C (log(1/r))^{-gamma}, for 0<r<=r_0<1, with gamma>4.

Choose 2/gamma < theta < 1/2 and a_n=n^theta. The row-distance bound gives

P(s_min(A_n-zI) <= exp(-n^theta)) <= n Q_X(n^{1+1/alpha} exp(-n^theta)) <= C' n^{1-theta gamma},

eventually, because log(n^{-(1+1/alpha)} exp(n^theta)) >= n^theta/2 for large n. This is summable since theta gamma>2. The polynomial operator-norm bound already proved is smaller than exp(n^theta) eventually. Borel-Cantelli gives the required spectral window. The concentration bound is 2 exp(-c n^{1-2theta}), summable since 1-2theta>0 (comparison with n^{-3}, using n^delta/log n -> infinity). The in-probability potential input and the exact same fractional-moment and local-L2 arguments therefore prove almost-sure weak convergence under this logarithmic small-ball hypothesis as well. The threshold gamma>4 comes from this argument only; it is not asserted sharp. It still excludes atoms and does not settle the unrestricted problem.


## Renewed serious attempt, 2026-10-11

The full proofs and theorem audits are saved in SECOND_ATTEMPT.md. Two previously unpursued routes here were considered: spatially integrated clipping defects, and a conditional atomic-mixture mask transfer to high-confidence invertibility. The latter was pursued first, giving a complete mixture decomposition and super-regularity proof, but Cook's applicable theorem retains the nonsummable error. The former yields a proved unrestricted theorem: almost surely (1/N) sum_{n<=N} mu_n converges weakly to mu_alpha, and (1/N) sum_{n<=N} d(mu_n,mu_alpha) tends to zero for every bounded compatible weak metric. Thus exceptional dimensions have density zero almost surely. This does not settle full-sequence convergence. A complete non-iid Jordan/cyclic counterexample in that file shows why the general potential inputs cannot eliminate sparse exceptions. No novelty is claimed. The remaining gap is precisely almost-sure decay of the spatial clipping defect, rather than its Cesaro average, or a summable invertibility estimate exploiting the iid-entry structure. Numerical checks are SECOND_CHECKS.json; the limited Lean check is tracked in CESARO_LEAN_CHECK.txt.

CesaroCore.lean passed with exit code 0 and no sorry or native_decide. The only formally checked claim is the algebraic dyadic-interpolation inequality; the random-matrix theorem is checked by the written proof, not formalized.
