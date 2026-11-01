# E0092 - Diaconis, Question 1: an explicit generating set achieving Wilson's mixing bound

Written 2026-09-09. Status: partial. Two things are done and one is not. Done: (a) the
question is reduced, exactly, to a property of the binary code spanned by the linear
dependencies among the generators (a "smoothing" property of one weight shell), and (b)
for every fixed epsilon_0 > 0 a set of N = 2n generators that achieves Wilson's bound for
every epsilon >= epsilon_0 is constructed by a deterministic algorithm running in time
polynomial in n; a single family that achieves the bound for every epsilon at once is
constructed in time n^{O(log log n)}. Not done: a closed-form set (a formula for the
V_i). Section 5 says exactly what such a set would need.

## 1. The problem as the source states it

Diaconis, "Some things we've learned (about Markov chain Monte Carlo)", Bernoulli 19
(2013), arXiv:1309.7754, Section 4, Example 6 (Cooking potatoes), p. 9 of the PDF:

> Suppose we allow a larger generating set V_1, V_2, ..., V_N say with N > n. How should
> the {V_i}_{i=1}^N be chosen to get rapid mixing? David Wilson [50] developed some
> elegant theory for this question.
>
> Theorem (Wilson). For all sufficiently large n and N > n, and V_1, V_2, ..., V_N in
> C_2^n, the random walk based on repeatedly adding a uniformly chosen V_i satisfies
> 1. for any choice of V_1, ..., V_N, if k < (1 - eps)T(n, N) then ||Q^{*k} - U|| > 1 - eps;
> 2. for almost all choices of V_1, ..., V_N, if k > (1 + eps)T(N) then ||Q^{*k} - U|| < eps
>    provided the Markov chain is ergodic.
>
> Here T(n, N) = N/2 1/(1 - H^{-1}(n/N)), H(x) = x log_2 1/x + (1 - x) log_2 1/(1 - x),
> 0 <= x < 1. Note that almost all choices in item 2 of the theorem will be ergodic when
> N - n is sufficiently large. For example, when N = 2n, T(n, N) = 0.24853 n steps are
> required. Further details are in [50].
>
> 5. Open questions
> Question 1. In item 2 of Wilson's theorem (Example 6), the result holds for almost all
> choices V_1, V_2, ..., V_N. Can an explicit set be found, e.g., for N = 2n?

(The quote is from the pypdf extraction; the displayed formula for T is as extracted.)
The ledger row states the question faithfully.

One typographical point matters for what follows. The displayed T(n, N) = (N/2)/(1 -
H^{-1}(n/N)) gives 1.1236 n at N = 2n, not the 0.24853 n the text quotes two lines later.
Wilson's paper (Probab. Theory Related Fields 108 (1997) 441-457, doi
10.1007/s004400050116, obtained from Springer, p. 442) defines

    T(d, n) = (n/2) ln 1/(1 - 2 H^{-1}(d/n))        (his d = dimension, his n = number of vectors)

and that is (N/2) ln 1/(1 - 2H^{-1}(n/N)) in Diaconis's notation, which is 0.24853 n at
N = 2n (check_T.py; H^{-1}(1/2) = 0.1100279). Everything below uses Wilson's T. Write

    alpha* = H^{-1}(1/2) = 0.110028,   t* = ln 1/(1 - 2 alpha*) = 0.248533,   T(n, 2n) = n t*.

Wilson's Theorem 1 (p. 442) is exactly Diaconis's two items, with "for all sufficiently
large d and all n > d". His lower bound (item 1) is a support-counting argument on the
walk on the N-cube; his upper bound (item 2) is a second-moment argument on the map
M : Z_2^N -> Z_2^n treated as a universal hash function, applied shell by shell in the
Hamming weight.

## 2. Findings

Notation. V_1, ..., V_N in F_2^n are the columns of an n x N matrix M. The walk is
X_k = X_{k-1} + V_{I_k}, X_0 = 0, I_k iid uniform on [N]. U is uniform on F_2^n and TV is
total variation distance. S_w is the Hamming sphere of radius w in F_2^N and nu_w the
uniform law on it.

**Finding A (exact reduction).** X_k = M Z_k where Z_k is the nearest-neighbour walk
on the N-cube (flip a uniform coordinate) started at 0. Conditionally on wt(Z_k) = w the
vector Z_k is uniform on S_w. Consequently, with

    Q_w(M) := 2^n * P(M z = M z') - 1,    z, z' iid uniform on S_w,

one has, for every k and every window [w_0, w_1],

    TV(law X_k, U) <= P(wt Z_k not in [w_0, w_1]) + max_{w in [w_0, w_1]} sqrt(Q_w(M)) / 2 .   (R)

Q_w(M) depends on M only through the weight distribution (B_u) of the dependency code
D = ker M = {y in F_2^N : sum_i y_i V_i = 0}, a linear code of length N and dimension
N - rank M:

    Q_w(M) = 2^n [ 1/C(N,w) + sum_{u >= 1} B_u p_w(u) / C(N,u) ] - 1,
    p_w(u) = P(wt(z + z') = u) = C(u, u/2) C(N-u, w-u/2) C(N,u) / C(N,w)^2  (u even), 0 (u odd).

So a sufficient condition for a set to satisfy Wilson's item 2 is: for every fixed
alpha in (alpha*, 1/2), Q_w(M) -> 0 uniformly for w/N in a neighbourhood of alpha. In
words: the dependency code D must have, on each sqrt(N)-window of even weights u around
2 alpha (1 - alpha) N, no more than (1 + o(1)) times the binomial share 2^{-n} C(N,u) of
codewords, in the p_w-weighted average, with the low-weight tail controlled. This
sharpens the ledger's earlier attempt (which said "the weight enumerator of the dual
of the code they generate" and stopped): the exact quantity, the exact window and the
precise sense of "binomial" are the ones above, and the condition is a second-moment
one, so a minimum-distance hypothesis on D^perp cannot deliver it (Section 5).

**Finding B (a deterministic polynomial-time set with the sharp constant).** For every
epsilon_0 in (0, 1] there is a constant C = C(epsilon_0) = O(epsilon_0^{-2}) and a
deterministic algorithm that, on input n, outputs in time n^{O(C)} a list S_n of exactly
2n vectors in F_2^n such that for all n >= n_0(epsilon_0), for every epsilon >= epsilon_0
and every integer k >= (1 + epsilon) T(n, 2n):

    TV(law X_k, U) < 4/n < epsilon .

So S_n satisfies Wilson's item 2 (including ergodicity) for every epsilon >= epsilon_0.
Choosing the block size b(n) = ceil(ln n * ln ln n) instead of C ln n gives a single
sequence S_n satisfying item 2 for every epsilon > 0, at construction cost n^{O(ln ln n)}.

The construction: split the n coordinates into L = floor(n/b) blocks of size b or b+1
with b = ceil(C ln n); in each block put the 2 b_j columns of one fixed b_j x 2 b_j
Toeplitz matrix over F_2, padded with zeros outside the block. The Toeplitz block is
found once per block size by exhaustive search over the 2^{3 b_j - 1} Toeplitz matrices,
accepting the first one whose Q_w is at most eta_w := 2 (2 b_j + 1) 2^{b_j} / C(2 b_j, w)
for every w. The search is guaranteed to succeed (more than half the family qualifies)
and the check per candidate is a 2^{2 b_j} enumeration.

Wilson himself noted (p. 450) that his proof uses only P(M y = 0) = 2^{-d} for y != 0, so
a Toeplitz matrix with N - 1 random bits, or Wozencraft's ensemble with max(d, N - d)
random bits, already suffices. Finding B is the step from "few random bits" to "no
random bits": it exchanges a single n-dimensional block, where the search space
2^{O(n)} is exponential, for n / (C ln n) blocks of logarithmic size, where the same
search is polynomial, and it shows the sharp constant survives the product structure.
The sharp constant is why the block size must grow with n: with blocks of bounded
size the product chain mixes in order n log n steps (like the Ehrenfest walk), and a
logarithmic block size is exactly where the block error e^{-c b} beats the number of
blocks n/b.

## 3. Proof of Finding A

Lemma 1 (projection). Let Z_k in F_2^N be the walk Z_k = Z_{k-1} + e_{I_k}, Z_0 = 0. Then
X_k = M Z_k for all k, since M e_i = V_i and M is linear.

Lemma 2 (shells). Conditionally on wt(Z_k) = w, Z_k is uniform on S_w. Proof: the law
of Z_k is invariant under coordinate permutations (the step law is), and the orbits of
the permutation group on F_2^N are the spheres S_w.

Lemma 3 (collision bound; Lean-certified). For any probability vector f on a set of
size m, (sum_x |f(x) - 1/m|)^2 <= m sum_x f(x)^2 - 1. Applied to f = law(M z), z uniform on
S_w, m = 2^n: 2 TV(M nu_w, U) <= sqrt(Q_w(M)). Proof: Cauchy-Schwarz against the constant
function, plus sum_x (f(x) - 1/m)^2 = sum f^2 - 1/m when sum f = 1. This is theorem
tv_sq_le_collision in U_E0092.lean (compiled clean, axioms propext, Classical.choice,
Quot.sound only), together with the form tv_le_half_sqrt_collision.

Proof of (R). By Lemmas 1 and 2, law(X_k) = sum_w P(wt Z_k = w) M nu_w. TV is convex in
its first argument, so TV(law X_k, U) <= sum_w P(wt Z_k = w) TV(M nu_w, U); bound the
terms outside the window by 1 and those inside by Lemma 3.

The weight formula for Q_w. 2^n P(Mz = Mz') = 2^n sum_y P(z + z' = y) 1[y in D]. The law
of z + z' is invariant under permutations, so P(z + z' = y) = p_w(wt y) / C(N, wt y), and
summing over y in D by weight gives the formula. p_w(u) counts pairs: z + z' = y with
wt y = u forces z to have exactly u/2 ones inside the support of y and w - u/2 outside.
check_identity.py verifies, on a random 6 x 12 instance, that the two evaluations of
Q_w agree to machine precision for every w, that law(X_k) equals the shell mixture for
k <= 24 (assert), and that (R) holds against the exact TV.

## 4. Proof of Finding B

Throughout, a block has dimension d = b, length N = 2b, and the block matrix is a b x 2b
Toeplitz matrix M_t with (M_t)_{r,c} = t_{c - r + b - 1}, t in F_2^{3b-1}.

Lemma 4 (the Toeplitz family is 2-universal). For y != 0 in F_2^N and t uniform, M_t y is
uniform on F_2^b. Proof: t -> M_t y is linear. Let c_0 be the least index with y_{c_0} = 1
and consider the coordinates j_r = c_0 - r + b - 1, r = 0..b-1, of t. The coefficient of
t_{j_r} in row r' of M_t y is y_{c_0 - r + r'}, which is 1 for r' = r and 0 for r' < r
(the index is below c_0). So the b x b submatrix on these coordinates is lower
unitriangular, the map is onto F_2^b, and the image of a uniform t is uniform.

Corollary. E_t Q_w(M_t) = (2^b - 1)/C(N, w): indeed E_t 2^b P(M_t(z+z') = 0) =
2^b [P(z = z') + (1 - P(z = z')) 2^{-b}] and P(z = z') = 1/C(N,w).

Lemma 5 (a good block exists and is found by search). Put eta_w = 2 (N+1) 2^b / C(N,w).
By Markov, P_t(Q_w(M_t) > eta_w) <= (2^b - 1)/(C(N,w) eta_w) < 1/(2(N+1)); a union bound
over the N+1 values of w gives P_t(some w fails) < 1/2. So more than half of the 2^{3b-1}
Toeplitz matrices satisfy Q_w <= eta_w for all w. The algorithm enumerates t in a fixed
order, computes Q_w(M_t) for all w by bucketing the 2^N vectors of F_2^N by (weight,
image), and stops at the first matrix that passes; it runs in time 2^{3b-1} 2^{2b}
poly(b) = 2^{5b} poly(b). (block_search.py implements this; Section 6 says what it
shows and does not show at small b.)

Lemma 6 (the weight of the cube walk). Let W_K = wt(Z_K) on the N-cube. Then
E W_K = (N/2)(1 - (1 - 2/N)^K), and for t > 0, P(W_K <= E W_K - t) <= exp(-t^2/(2K)),
likewise for the upper tail. Proof: coordinate i is flipped c_i times with
c_i ~ Bin(K, 1/N), and P(c_i odd) = (1 - (1-2/N)^K)/2. W_K is a function of the K
independent choices I_1..I_K, and changing one choice moves W_K by at most 2, so
McDiarmid's inequality gives exp(-2 t^2/(4K)). (check_block_lemma.py verifies the mean
formula exactly for K <= 30.)

Lemma 7 (one block, exponentially small error). Let theta in (0, 1], alpha_theta =
(1 - (1 - 2 alpha*)^{1 + theta})/2, delta = (alpha_theta - alpha*)/2, and let M be a b x 2b
matrix with Q_w(M) <= eta_w for all w. If b >= 2/delta then for every integer
K >= (1 + theta) b t*,

    TV(law(M Z_K), U_b) <= 2 exp(-delta^2 b / 4) + (2b + 1) 2^{-2.4 delta b} <= (2b + 3) e^{-delta^2 b/4}.

Proof. By monotonicity of TV along a random walk on a group it suffices to take
K = ceil((1 + theta) b t*), and then K <= 0.5 b + 1 <= N. Since (1 - 2/N)^K <= e^{-2K/N}
<= e^{-(1 + theta) t*} = (1 - 2 alpha*)^{1 + theta}, Lemma 6 gives E W_K >= alpha_theta N.
Put w_0 = ceil((alpha* + delta) N). Then E W_K - w_0 >= delta N - 1 >= delta N / 2, and
Lemma 6 with t = delta N / 2 and K <= N gives P(W_K < w_0) <= exp(-delta^2 N/8) =
exp(-delta^2 b/4); the same for P(W_K > N - w_0), because E W_K <= N/2 and
N - w_0 - N/2 >= (1/2 - alpha* - delta) N - 1 >= delta N/2. Apply (R) with the window
[w_0, N - w_0]. Inside it C(N,w) >= C(N,w_0) >= 2^{N H(w_0/N)}/(N+1) >= 2^{N H(alpha* +
delta)}/(N+1), and by concavity of H on [alpha*, 0.2] (the chord slope from alpha* is
decreasing in delta and equals 2.466 at delta = 0.09; numerically the minimum over
delta in (0, 0.09] is 2.4665) H(alpha* + delta) >= 1/2 + 2.4 delta. Here alpha* + delta
<= 0.2 because theta <= 1 gives delta <= 0.0228. Hence for w in the window

    Q_w(M) <= eta_w <= 2 (N+1)^2 2^{b - N(1/2 + 2.4 delta)} = 2 (N+1)^2 2^{-4.8 delta b},

and sqrt(Q_w)/2 <= (N+1) 2^{-2.4 delta b} / sqrt 2 <= (2b + 1) 2^{-2.4 delta b}. Since
delta <= 0.0228, delta^2/4 <= 2.4 delta ln 2, which gives the final form.

Bounds on delta. From 1 - e^{-x} >= x e^{-x} and 1 - e^{-x} <= x: alpha_theta - alpha* =
(1 - 2 alpha*)(1 - e^{-theta t*})/2 lies between (1 - 2 alpha*)^2 theta t*/2 = 0.0756 theta
and (1 - 2 alpha*) theta t*/2 = 0.0969 theta, so 0.0378 theta <= delta(theta) <= 0.0485 theta.
For the main theorem theta = epsilon/2, so 0.0189 epsilon <= delta <= 0.0243 epsilon
(numerically delta = 0.00241 at epsilon = 0.1 and 0.0228 at epsilon = 1; check_T.py and
the run of 2026-09-09).

Theorem (Finding B). Fix epsilon in (0, 1], let delta = delta(epsilon/2), and put
b = ceil((8/delta^2) ln n). For n >= b(b+1) write n = sum_{j=1}^L b_j with L = floor(n/b)
and b_j in {b, b+1} (r = n - Lb < b <= L of the blocks get size b+1). Let M^{(j)} be the
block matrix of Lemma 5 for size b_j (two searches, sizes b and b+1). S_n is the list of
the 2 b_j columns of M^{(j)} embedded in block j's coordinates, over all j; it has
exactly 2n entries. Then for every integer k >= (1 + epsilon) n t*,
TV(law X_k, U) <= 4/n.

Proof. Let K_j be the number of steps up to time k that choose a generator of block j;
(K_1, ..., K_L) is multinomial with probabilities b_j/n. Conditionally on the K_j, the
blocks evolve independently, block j performing exactly K_j steps of its own walk (the
within-block choices are iid uniform on the block's 2 b_j generators). TV of a product
against a product is at most the sum of the marginal TVs (couple each coordinate
optimally and independently), so

    TV(law X_k, U) <= sum_j E[ TV(law Y^{(j)}_{K_j}, U_{b_j}) ]
                   <= sum_j [ P(K_j < (1 + epsilon/2) t* b_j) + sup_{K >= (1+epsilon/2) t* b_j} TV(law Y^{(j)}_K, U_{b_j}) ].

K_j ~ Bin(k, b_j/n) has mean mu >= (1 + epsilon) t* b_j; with gamma = 1 - (1 + epsilon/2)/
(1 + epsilon) >= epsilon/4, Chernoff gives P(K_j <= (1 - gamma) mu) <= exp(-gamma^2 mu/2)
<= exp(-epsilon^2 t* b/32). For the second term Lemma 7 with theta = epsilon/2 (its
hypothesis b_j >= 2/delta holds since b >= 8/delta^2) gives (2b + 5) e^{-delta^2 b/4}.
With b >= (8/delta^2) ln n, (n/b)(2b + 5) e^{-delta^2 b/4} <= 3 n * n^{-2} = 3/n. For the
first term, b = (8/delta^2) ln n gives exp(-epsilon^2 t* b/32) = n^{-epsilon^2 t*/(4 delta^2)},
and delta <= 0.0243 epsilon makes the exponent at least 0.2485/(4 * 0.00059) > 100, so
(n/b) exp(-epsilon^2 t* b/32) <= n * n^{-100} <= 1/n. Total <= 4/n.

Monotonicity gives the statement for all epsilon' >= epsilon: TV at time (1+epsilon')T
is at most TV at time (1+epsilon)T <= 4/n < epsilon <= epsilon'. The construction time is
dominated by the two block searches, 2^{5(b+1)} poly(b) = n^{40/delta^2 + o(1)}, i.e.
n^{O(epsilon^{-2})}. For a single family valid for all epsilon, take b(n) = ceil(ln n *
ln ln n): for each fixed epsilon the inequality b >= (8/delta^2) ln n holds for n large,
and the cost is n^{O(ln ln n)}.

Remark (the constant is sharp and it is Wilson's T). Wilson's item 1 already says no
set beats T(n,N). The same lemmas give it in two lines: at k <= (1 - epsilon) n t* the
mean weight of Z_k is at most (alpha* - c epsilon) N, Lemma 6 keeps W_k below (alpha* -
c epsilon/2) N with probability 1 - e^{-c' n}, the ball of that radius has at most
2^{N H(alpha* - c epsilon/2)} = 2^{n - c'' n} points, so X_k lives on a set of U-measure
2^{-c'' n} with probability 1 - e^{-c' n} and TV >= 1 - e^{-c' n} - 2^{-c'' n}. This is
independent of the typography in the Bernoulli paper: the threshold (N/2) ln 1/(1 -
2H^{-1}(n/N)) is forced from both sides.

## 5. What is not done, and what a closed-form set would need

A closed-form set (a formula for V_1, ..., V_{2n}) is not given. By Finding A it is the
same as a closed-form [2n, n] binary code D (the dependency code) with Q_w -> 0 on every
window w/N in (alpha* + delta, 1/2 - delta), and the concrete obstacle is this. Q_w is a
second moment: it asks that the p_w-weighted average of 2^n B_u / C(2n, u) be 1 + o(1),
where p_w is concentrated on even u within O(sqrt n) of 2 alpha (1 - alpha) 2n, so on
relative weights between 0.196 and 0.5. That is "the weight distribution of D is
binomial to first order on every sqrt(n)-window at every linear weight above 0.196",
plus a controlled low-weight tail (the tail is not negligible: at alpha near alpha*,
the trivial bound B_u <= C(N,u) already fails at u = 0.02 N, though D need not have
linear minimum distance; the allowance at weight beta N is 2^{N g(beta)} with g(0+) =
H(alpha) - 1/2 > 0). A first-moment (Fourier) bound cannot substitute: with all nonzero
weights of D^perp in [aN, (1-a)N] the Krawtchouk estimate gives 2 TV <= 2^{N(1 - H(alpha)/2
- H(a)/2)}, never small, so cancellation among the characters is genuinely needed. This
is also the conclusion of Debris-Alazard, Ducas, Resch and Tillich, "Smoothing codes and
lattices: systematic study and new bounds" (IEEE Trans. Inf. Theory 2023,
arXiv:2205.10552), who study exactly TV(M nu_w, U) (smoothing a code with spherically
uniform noise): the worst-case bound from the dual distance via the second linear
programming bound is strictly weaker than the average-case (random code) bound, which
is the one Wilson's constant needs. To my knowledge no explicit rate-1/2 binary family
has a proven (1 + o(1))-binomial weight distribution at linear weights away from N/2:
the Sidelnikov / Krasikov-Litsyn "range of binomiality" results for BCH codes and their
duals control weights within O(sqrt(N d^perp)) of N/2, which for a code whose dual
distance is sublinear (as it is for rate-1/2 BCH) does not reach 0.196 N to 0.5 N. So
the closed-form version of Question 1 sits on top of an open problem in coding theory,
and the ledger's earlier attempt was right to say so, though "meets the Gilbert-
Varshamov bound" is not the right target: what is needed is binomial weight
distribution in the window above, not minimum distance.

Whether the reduction is also necessary is not shown: (R) uses the L2 bound on each
shell, and a set could in principle have shells whose fibres are unbalanced in L2 but
balanced enough in L1, or shells that compensate each other in the mixture. I do not
expect this to matter for a structured set, but it is not proved.

## 6. Checks

check_T.py: the three readings of the T formula; only (N/2) ln 1/(1 - 2H^{-1}(n/N)) gives
0.24853 n, and Wilson's paper confirms that reading. Also alpha*, t*, delta(theta) and
the entropy chord slope (minimum 2.4665 over delta in (0, 0.09]).

check_identity.py (d = 6, N = 12, random M): the two evaluations of Q_w (direct
collision count, and the weight-distribution formula through ker M) agree for every w;
law(X_k) equals the shell mixture sum_w P(W_k = w) M nu_w for k <= 24 (assert); the
bound (R) holds against the exact TV. The first version of this script had the factor
C(N,u)/C(N,w) missing from p_w(u) and disagreed by a factor 2^d; the disagreement was
caught by the direct evaluation and fixed, and the fixed formula is the one in Section 3.

check_product.py (n = 12, three blocks of size 4, one full-rank Toeplitz block): the
exact TV of the walk on Z_2^12 is below the product bound L * E[TV_b(K)], K ~ Bin(k, 1/3),
at every k tested.

check_block_lemma.py (b = 10, N = 20, random Toeplitz block): Q_w <= eta_w for every w
(max ratio 0.024), the assembled Lemma 7 bound (truncation plus max over a window of
sqrt(Q_w)/2, best window) is never below the exact TV for K <= 30, and E W_K =
(N/2)(1 - (1 - 2/N)^K) is exact.

block_search.py: the deterministic search of Lemma 5 for b = 5..8. What it shows: the
algorithm runs and a passing full-rank matrix is found within the first few hundred
candidates. What it does not show: at these sizes eta_w >= 0.68 for all w, so the
acceptance test does not bite, and the lexicographically first passing matrix at b = 8
is the degenerate [0 | I] (half the generators are the zero vector). The threshold
eta_w becomes exponentially small only for b of order ten and larger in the window (it
needs C(N,w) >> N 2^b), which is the asymptotic regime the proof lives in and which a
laptop enumeration of 2^{2b} vectors per candidate does not reach at b = 20-30 within
the CPU budget of this session. Nothing in the proof depends on the small runs.

U_E0092.lean: Lemma 3 (the collision bound), compiled clean on Lean 4.33.1 / Mathlib,
axioms propext, Classical.choice, Quot.sound. One compile error on the first attempt (a
closing `ring` after `field_simp` had no goal left), fixed by deleting it.

The strongest case that this is wrong, and the check. The step most likely to hide an
error is the assembly of Lemma 7 (three inequalities and a window) and the claim that
the Toeplitz family's per-member Q_w bounds hold simultaneously for all w. Both were
tested directly at b = 10 against exact quantities (check_block_lemma.py), and the
union-bound arithmetic is the one-line Markov computation in Lemma 5. The second most
likely error is the value of T; Wilson's own definition settles it. What would break
Finding B is a flaw in the product decomposition (blocks independent given the counts),
which is a structural fact about the walk (the generator choice is a block label plus
an independent uniform index) and was also tested numerically (check_product.py). What
would break the interpretation is only the meaning of "explicit": if Diaconis wants a
formula, Finding B is a reduction, not an answer, and it is labelled so.

## 7. Prior art

Search conditions: the session's web-search budget was exhausted before this task
started, and WebFetch does not reach arXiv, so the search was done through the arXiv
API, Crossref, OpenCitations and Semantic Scholar (all rate-limited but usable), plus
Wilson's paper itself from Springer (open access) and the Debris-Alazard et al. abstract
from arxiv.org over curl.

- Wilson, D. B., Random random walks on Z_2^d, Probab. Theory Related Fields 108 (1997)
  441-457, doi 10.1007/s004400050116. Theorem 1 is the theorem Diaconis quotes; T is
  defined as (n/2) ln 1/(1 - 2H^{-1}(d/n)) (his notation). Page 450: the proof uses only
  P(Mz = 0) = 2^{-d} for z != 0; an upper-triangular Toeplitz matrix needs n - 1 random
  bits, Wozencraft's ensemble max(d, n - d) bits with a polynomial that Shoup's algorithm
  finds deterministically. No explicit (zero random bits) set is claimed, and Diaconis
  asks the question in 2013 with this paper as the reference.
- The 19 works citing Wilson 1997 listed by OpenCitations (resolved through Crossref):
  Dou and Hildebrand 1996; Pak 1999; Hildebrand 2001; Pak and Vu 2001; Saloff-Coste
  2004; Wilson 2004; Kirovski, Sinclair and Wilson 2007; Amir and Gurel-Gurevich 2010;
  Scoppola 2011; Diaconis 2013 (the source); Chen and Saloff-Coste 2015; Smith 2016;
  Hough 2017; Bordenave, Caputo and Salez 2018; Chatterjee and Diaconis 2020 (and its
  2021 correction); Levin and Tankala 2022; Debris-Alazard, Ducas, Resch and Tillich 2023;
  Hermon and Olesker-Taylor 2023 (Geometry of random Cayley graphs of Abelian groups,
  Ann. Appl. Probab.). None of the titles is about explicit generating sets on the
  hypercube, and none post-dates 2013 with Diaconis's Question 1 as its subject; the
  question is not marked solved anywhere reachable. Hermon and Olesker-Taylor study
  random generators; Debris-Alazard et al. study the smoothing quantity of Finding A
  for codes in general and give the worst-case versus average-case gap discussed in
  Section 5.
- The phrase that would have found a solution, had one been published, is "explicit"
  together with "random random walks" or "Wilson" and "hypercube"; no such title
  appears among the citing works. A free-text web search could not be run this
  session, so a paper that solves Question 1 without citing Wilson 1997 would have
  been missed; that seems unlikely for this question.

## Files

- memo.md (this file)
- U_E0092.lean (Lemma 3, compiled clean; also at ~/erdos_fc/Prob1000/U_E0092.lean)
- check_T.py, check_identity.py, check_product.py, check_block_lemma.py, block_search.py
