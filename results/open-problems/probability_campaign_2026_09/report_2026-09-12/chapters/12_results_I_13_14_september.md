## The results of 13 and 14 September: nine of Janson's problems, the sharp constants for free and classical Brownian unimodality, a Hadamard conjecture settled in 1983, and what a literature sweep did to the open count

This chapter records what changed after the 12 September state of the report. Two separate efforts ran.
On the afternoon and evening of 13 September a coordinator drove ten concurrent lanes for ten hours on the
owner's order, five of them on the open problems (percolation, random matrices, continuous-time processes,
particle systems, Markov chains); their memos are under
`12_cognitive_architecture/brain_improvement/campaign_2026-09-13_10h_10sub/lanes/`. Overnight, from 23:30
on 13 September, a single session worked the open problems for twenty hours.

What that session settled, in the order the sections come: nine of Janson's problems and one of Aldous and
Fill's; seven questions posed by preprints of the past two months; the sharp constant in Hasebe and Ueda's
Problem 3.3 on the unimodality of free Brownian motion, which is one rather than the four their theorem
gives, together with the classical companion, which is a quarter of the squared diameter against the
thirty-six times larger bound the same paper proves, and a criterion that gives the analogous constant for
any symmetric kernel; Conjecture 13 of the Randomstrasse 2024 list on the discrepancy of the Sylvester
Hadamard matrices, which turns out to be a solved question in Boolean analysis and is false for every odd
$k \ge 9$; the exact largest discrepancy of a sign matrix at every size to eleven, by reading that as a
covering-code question; a reduction of Aldous and Fill's Open Problem 7.31 on distance-regular graphs to
an identity in the intersection array, with Biggs's value confirmed as the maximum over all thirteen cubic
such graphs; the removal of the Cauchy laws, and of the free stable laws of index down to about $0.7$,
from the candidates for their Problem 3.11; and a dual for the congestion quantity in Sinclair's
inequality that answers the first half of Aldous and Fill's Open Problem 4.49 and reduces the second
half to a question about flow-cut gaps, settling it for two classes of graph.

It also opened a seventh ledger of 118 records, repaired ledger rows carried as open that had in fact been
answered, ran a literature sweep that withdrew fourteen more, corrected one of its own published claims,
and left fifty-five new problems, each arising from one of the proofs. Its memos are in the Downloads folder,
mirrored with their scripts to `06_math_research/probability_1000_attempts_I_20260914/`, and the ledgers
carry an appended status record for each row it touched. Verification words are as the memos state them:
author checked, no independent read, prior art searched but not cleared. Nothing here is certified.

### Seven problems from Janson's survey

All seven rows come from Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations
and condensation*, Probability Surveys 9 (2012), and concern the balls-in-boxes model $B_{m,n}$ with weight
sequence $w$: an allocation $(Y_1, \dots, Y_n)$ of $m$ balls has probability proportional to $\prod_i
w_{Y_i}$. The notation is the source's: $\Phi(t) = \sum_k w_k t^k$ with radius $\rho$, $\Psi(t) =
t\Phi'(t)/\Phi(t)$, $\nu = \Psi(\rho)$, $m/n \to \lambda$, the tilted law $\pi_k = w_k\tau^k/\Phi(\tau)$ with
$\Psi(\tau) = \lambda$ (or $\tau_n$ with $\Psi(\tau_n) = m/n$ for the $\xi^{(n)}$ version), and $Y_{(1)} \ge
Y_{(2)} \ge \dots$ the ordered box counts. Theorem 18.7 of the source compares the largest boxes with the
order statistics of $n$ independent copies of $\xi$ in six parts: (i) Poisson limits for the number of boxes
above a level, (ii) and (iii) the two one-sided consequences, (iv) a modified Kolmogorov distance for the
counts, (v) Kolmogorov distance for each $Y_{(j)}$, (vi) total variation for $Y_{(1)}$.

**F0056, Problem 18.9.** Is Theorem 18.7 true for $\lambda = 0 < \nu$? Answered: no in general, yes when
$w_1 > 0$. The question concerns $m \to \infty$ with $m/n \to 0$ (bounded $m$ fails for every $w$, since at
most $m$ boxes are nonempty while the independent count is Poisson). Theorem 1 of the memo: if $w_0 > 0$,
$w_1 > 0$, $\omega = \infty$, then all six parts hold in the $\xi^{(n)}$ version whenever $m \to \infty$ and
$m/n \to 0$. Theorem 2: if $w_1 = 0$ and the span is one, let $a = \min(\mathrm{supp}\,w \setminus \{0\})$
and $b$ the least element of the support not divisible by $a$; for $m \not\equiv 0 \pmod a$ and $n/m^{b/(b-a)}
\to \infty$, $Y_{(1)} \ge b$ surely while $n\,\mathbb{P}(\xi^{(n)} \ge b) \to 0$, so (i), (ii), (iv), (v), (vi)
all fail and the total variation distance tends to one. The ledger's parity example ($w = (1, 0, 1, 1,
\dots)$, $n = k^4$, $m = 2k+1$) is the case $a = 2$, $b = 3$, and both obligations the 12 September chapter
named for it (tilt existence, the assembled limit) are closed by Theorem 2's two-line computation
$\tau_n \sim (w_0\mu_n/(aw_a))^{1/a}$, $n\,\mathbb{P}(\xi^{(n)} \ge b) = O(n\mu_n^{b/a})$.

The proof of Theorem 1 is a local limit theorem for the triangular array $\xi^{(n)}$ in the regime where the
tilted law degenerates to a point mass at zero while $n\,\mathbb{E}\xi^{(n)} = m \to \infty$. The
characteristic function satisfies $|\varphi(t)|^2 \le 1 - 2\pi_0\pi_1(1 - \cos t)$, and $n\pi_1 \sim m$, so
$|\varphi(t)|^n \le \exp(-(1 + o(1))\,m\,(1 - \cos t))$; the third moment is $O(\mu_n)$, so the Edgeworth
error is $O(m^{-1/2})$. That gives $\mathbb{P}(S_{n-r} = m - K)/\mathbb{P}(S_n = m) \to 1$ uniformly for $K =
o(\sqrt m)$ and a uniform bound $\sup_j \mathbb{P}(S_{n-1} = j) \le C\,\mathbb{P}(S_n = m)$, which are the two
inputs Janson's proof takes from his Lemma 13.1 and Remark 13.2; the rest of his proof, including the
partition argument for (vi), runs verbatim. The hypothesis $w_1 > 0$ is used in exactly one place, the
characteristic-function bound, and Theorem 2 is what happens when it is lost: the sum lives on $a\mathbb{Z}$
to first order and $|\varphi(2\pi j/a)|^n \to 1$ precisely when $n\pi_b \to 0$. The intermediate range, $n\pi_b$
between order one and order $\log m$ for $w_1 = 0$, is not settled and is listed among the new problems below.

Numerical check, exact: for $w_k \equiv 1$ (uniform weak compositions) the first two factorial moments of the
number of boxes with at least two balls are $0.99701$ and $0.99005$ at $m = 1000$, $n = 10^6$, against the
Poisson prediction $0.99800$ and $0.99601$; for the parity sequence $n\,\mathbb{P}(\xi^{(n)} \ge 3) = 0.327,
0.101, 0.032$ at $k = 10, 100, 1000$ while $\mathbb{P}(Y_{(1)} \ge 3) = 1$ exactly. Memo:
`Probability_F0056_Janson_problem_18_9_complete_answer_2026-09-13.md`.

**F0062, Problem 18.42.** Does $w_{k+1}/w_k \to \infty$ force condensation to a single box? Answered: no.
Problems 18.41 and 18.42 ask whether two regularity hypotheses on $w$ force (18.106)-(18.107), that is
$Y_{(1)} = (\lambda - \nu)n + o_p(n)$ and $Y_{(2)} = o_p(n)$ when $\lambda > \nu$. Both hypotheses control the
first differences of $\log w_k$; single-box condensation is a statement about second differences, since one box
of size $a + b$ beats two boxes of sizes $a$ and $b$ exactly when $\log w_{a+b} + \log w_0$ exceeds $\log w_a +
\log w_b$ by more than the $O(\log n)$ entropy of placing a second box. Theorem A of the memo takes $d_j = j$
except $d_j = j^3$ at powers of two and $w_k = \exp(\sum_{j<k} d_j)$, so $w_{k+1}/w_k = e^{d_k} \to \infty$,
$\rho = 0$, $\nu = 0$. At $m = 2^{i+1}$ the configuration $(2^i + 1, 2^i - 1)$ collects the spike $8^i$ once
and every lower spike a second time, and an explicit count shows it beats every configuration with $Y_{(2)} \le
m/8$ by a factor $e^{m^3/128}$, against at most $2^{m+n}$ configurations. Hence $\mathbb{P}(Y_{(2)} > m/8) \to
1$ along $m = 2^{i+1}$, for every $\lambda \in (0, \infty)$, and both displayed statements fail. Exact
partition-function check: $\mathbb{P}(Y_{(2)} \le m/8) = e^{-4089}, e^{-37586}, e^{-311282}$ at $m = 64, 128,
256$ with $n = 2m$.

**F0061, Problem 18.41.** Do nonincreasing weights force condensation to a single box? Answered: no. Theorem
B takes dyadic plateaus, $w_k = e^{-g(\lfloor\log_2 k\rfloor)}$ with $g(j) = 3j$ except at sparse cliffs $J$
where $g$ jumps to $6J + 4$ and stays there until $3j$ catches up. The sequence is nonincreasing and pinched
between two power laws, so $\rho = 1$, $\nu < \infty$ and the tilted law has finite variance. At a cliff $J$,
with $B = 2^{J-1}$ and the excess $K = 3B$ placed in the middle of block $J$, one box holding $K$ has weight
$e^{-6J-4}$ while two boxes in block $J - 1$ have weight $e^{-6J+6}$ and about $n^3$ placements; everything
else is controlled by the Fuk and Nagaev truncated exponential bound for the fluid and the local limit
theorem for its sum. The result is $\mathbb{P}(Y_{(2)} \ge B/4) \to 1$ along the cliffs, with $B/4 \ge
(\lambda - \nu)n/13$, and Lemma 18.31 then forces $Y_{(1)} \le \tfrac{12}{13}(\lambda - \nu)n + o_p(n)$. Exact
check at $\lambda - \nu = 1$: $\mathbb{P}(Y_{(2)} \ge B/4) = 0.9999$, $1 - 8\cdot 10^{-8}$, $1 - 2\cdot
10^{-10}$ at $J = 8, 9, 10$ ($n = 384, 768, 1536$) with the cliff, against $0.002$, $0.0005$, $0.0001$ for the
same sequence without it.

Both ledger attempts on these rows had argued for a positive answer by a "shed $j$ balls" comparison, in which
a two-box configuration $(a, b)$ is beaten by $(a + b - j, j)$ with $j$ chosen to escape a local dip of $w$. The
constructions show where that fails: escaping the spike or the cliff needs $j$ of order $n$, so the shed box is
itself macroscopic. A dip in a weight sequence can be as wide as the condensate. Memo:
`Probability_F0061_F0062_Janson_problems_18_41_18_42_answered_no_2026-09-14.md`.

**F0058, Problem 18.30.** At $\lambda = \nu$ with $\sigma^2 = \infty$, do parts (ii) and (iii) hold? Answered:
no to both. The construction is a probability weight sequence with atoms at $0, 1, 2$ and
at two interleaved families of scales, $L_{2r} = \lceil e^{8r^3}\rceil$ and $L_{2r-1} = \lceil L_{2r}/r
\rceil$, with $\mathbb{P}(\xi = L_{2r}) = e^{4r^2}/L_{2r}^2$, so that $\nu = \mathbb{E}\xi < \infty$ and
$\sigma^2 = \infty$. Along $n_r = \lfloor 1/(r\,\mathbb{P}(\xi = L_{2r}))\rfloor$ and $m = \lfloor \nu n_r
\rfloor$, the atom $L_{2r}$ shifts the mean of $S_n$ by exactly $L_{2r-1}$ while appearing with probability
$1/r$, so the mean sits $\Lambda_r \approx e^{4r-2}/\sqrt r$ standard deviations above the bulk of $S_n$.
Conditioning on $S_n = m$ must supply the missing $L_{2r-1}$ balls; one atom of size $L_{2r-1}$, tuned to appear
with probability $\delta_r = 1/(10\Lambda_r)$, does it at polynomial cost, while a bulk fluctuation costs
$e^{-\Lambda_r^2/3}$. Hence $\mathbb{P}(Y_{(1)} \ge L_{2r-1}) \to 1$ while $n_r\,\mathbb{P}(\xi \ge L_{2r-1})
\le \delta_r + 1/r + o(1/r) \to 0$: Theorem 18.7(ii) fails, and with it (i), (iv), (v), (vi), and $Y_{(1)}/
\xi_{(1)} \to \infty$, so the two maxima are not even of the same order, which answers the informal question
preceding Problem 18.30 as well. The proof uses Bernstein's inequality for the bounded bulk and a local limit
theorem for the bulk's triangular array in three ranges of the Fourier variable. Where Janson's proof needs
finite variance is the bound $\sup_j \mathbb{P}(S_{n-1} = j) \le C\,\mathbb{P}(S_n = m)$, true when $m$ is at
the centre of $S_n$; here the centre and the mean are $\Lambda_r$ apart. Part (iii) fails by a twist of the same
mechanism: if the rare atom is sized to exceed the missing mass by exactly the total mass of a common scale
(a scale with a Poisson$(r)$ number of boxes, $r \to \infty$), the cheapest way to land on $m$ is one rare atom
and *no* box of that scale, since removing a whole Poisson$(r)$ count costs $e^{-r}$ while any partial
compensation through the rest costs a Gaussian factor in $(L_C/s)^2 = r^2$. So $Y_{(2)} < L_C$ w.h.p. while
$n\,\mathbb{P}(\xi \ge L_C) \ge r$, which is (iii) failing for $j = 2$; the memo's first draft had claimed the
opposite and records the retraction. Exact toy computations of both mechanisms: for (ii), bulk $\{0, 1, 2\}$,
an atom at $250$ with $n p = 0.05$ and an atom at $5000$ with $n p = 0.05$, $n = 4000$, gives $\mathbb{P}(Y_{(1)}
\ge 250 \mid S_n = m) = 0.9999$ against $n\,\mathbb{P}(\xi \ge 250) = 0.10$; for (iii), a common scale at $40$
with $n p = 6$, the rare atom at $2779$, $n = 4000$, gives zero boxes of size $40$ with conditional probability
$1.0000$ against the unconditional $e^{-6}$. Memo:
`Probability_F0058_Janson_problem_18_30_part_ii_fails_2026-09-14.md`.

A remark that covers all four. The failures are produced by weight sequences whose logarithm is irregular at
the second-difference level (Theorems A and B), by a missing lattice direction (Theorem 2 of F0056), or by a
mean that its own distribution does not visit (F0058). None of them is pathological in the sense of Janson's
Examples 18.36-18.38, which live on sparse supports: the F0062 sequence has full support with ratios tending to
infinity, the F0061 sequence is monotone and pinched between two power laws, and the F0058 sequence is a
perfectly ordinary heavy-tailed law with finite mean. What the survey's positive theorems use, and what these
sequences lack, is a single quantitative input in each case: superadditivity of $\log w$ at scale $n$, a
characteristic-function bound off the origin, and the coincidence of mean and centre.

**F0064, Problem 20.2.** Kolchin's asymptotic normality of the number $N_d$ of vertices of outdegree $d$ in the
simply generated tree $T_n$, with variance $\pi_d(1 - \pi_d - (d-1)^2\pi_d/\sigma^2)$: does it hold at $\nu = 1$,
$\sigma^2 < \infty$ without extra moment conditions, does it extend to $\sigma^2 = \infty$, and what happens for
$0 \le \nu < 1$? The first question was answered yes by the survey's author in 2016 (Random Structures and
Algorithms 48, Example 2.2 with Theorem 1.13 and Section 8, jointly in $d$ with the covariances), and the other
two were answered yes under regular variation by Thévenin (Electron. J. Probab. 25, 2020, Theorems 6.2 and 6.7),
who conjectured that the conclusion, with variance $\pi_d(1-\pi_d)$, holds for every critical law of infinite
variance and every subcritical law without exponential moment. The conjecture is false, so the second and third
questions are answered in the negative in general. The device is the two-branch form of the F0058 construction: a
law with two rare atoms at sizes $(1 - q - c)n_r \pm A\sqrt{n_r}$, straddling the size the condensate has to take,
each of probability $n_r^{-4}$, on a bulk $\{0, 1\}$ with $\pi_1 = q < 1/2$. Along $n = n_r$ the conditioned tree
contains exactly one of the two atoms, each with probability tending to one half, and since every other vertex
has outdegree $0$ or $1$ or a medium size, $N_1 = n\pi_1 \mp A\sqrt n + O_p(\sqrt{V n})$ with $V$ the medium
variance, which can be made as small as one likes: the law of $(N_1 - n\pi_1)/\sqrt n$ is, in the limit, as
close as desired to $\frac12\delta_{-A} + \frac12\delta_A$, although the tree has a unique vertex of macroscopic
degree throughout. The proof is elementary (a local limit theorem for triangular arrays, Hoeffding, Chernoff and
Chebyshev) and complete. At $\nu = 1$ with $\sigma^2 = \infty$ the same construction works with the rare pair
straddling the deficit left by an absent rarer atom, as in F0058; here the two branch weights are made exactly
equal by choosing the pair's probabilities in the ratio of the two local probabilities of the rest, a device
that removes every moderate-deviation estimate from the weights, and what remains at sketch level is the
conditional law of $N_1$ given the branch, which needs a lattice local moderate-deviation expansion because the
medium variance now diverges. Why Thévenin's theorems survive: for a regularly varying tail the giant's law is
locally flat at scale $\sqrt n$, so the giant absorbs the other vertices' Gaussian fluctuation for free and they
stay i.i.d.; with two atoms $2A\sqrt n$ apart it is the other vertices that must move. Exact toy ($n = 4000$, $q =
1/2$, $A = 3$): branch weights $0.4976$ and $0.5024$, all conditional mass in $z \in [-3.5, -3) \cup [2.5, 3)$, no
mass within one standard deviation of zero against $0.683$ for the conjectured Gaussian. Memo:
`Probability_F0064_Janson_problem_20_2_outdegree_counts_not_normal_in_general_2026-09-14.md`.

**F0060, Problem 18.40.** With $\lambda > \nu = 0$, that is $\rho = 0$, can the largest box satisfy
$Y_{(1)}/n \to_p 0$ along the whole sequence? Example 18.38 gives it along a subsequence. Answered: no. The
tool is a per-ball rate. Normalising $w_0 = 1$ and writing $f = \log w$, the configurations made of
$r = m/s$ boxes of size $s$ have total weight $\exp(mF(s) + o(m))$ with
$$F(s) = \frac{f(s) + \log(s/\lambda) + 1}{s},$$
the first term rewarding large boxes and the second, the entropy of choosing which boxes are occupied,
rewarding small ones. A mixed configuration cannot beat the best pure one, and the number of partitions of
$m$ is $e^{O(\sqrt m)}$, so everything reduces to maximising $F$ over the support below $m$. Now
$\rho = 0$ says exactly $f(s)/s \to \infty$, so $F \to \infty$ and $F$ has infinitely many records; at $m$
equal to a record the maximiser is $m$ itself, one box holding every ball. The one way the allocation could
fail to follow its maximiser is a record gap smaller than the partition entropy $C/\sqrt m$ per ball; but if
the increase of $F$ across every multiplicative block $(\varepsilon m, m]$ were at most $C/\sqrt m$, chaining
the blocks down the scales gives $F(s_j) - F(s_0) \le C\varepsilon^{-K/2}/\sqrt{s_j} \le C'/\sqrt{s_0}$,
because the geometric sum is dominated by its smallest scale, and a bounded $F$ contradicts $\rho = 0$. So at
infinitely many $n$ the single box wins outright, $\mathbb{P}(Y_{(1)} = m) \to 1$, and $Y_{(1)}/n \to \lambda$
there. The exact conditional law confirms it: on the source's own Example 18.38 the largest box is the largest
support point below $m$ with no visible fluctuation, and the ratio returns to $1.0000$ at every $n = i!$. The
memo also displays the pre-asymptotic case, a denser and slower sequence whose ratio instead falls to $0.043$
by $n = 256$ because the maximiser is still $s = 2$ until $s \approx 2^{19}$, since that is exactly the run
that would make a numerical study conclude the opposite. Memo:
`Probability_F0060_Janson_problem_18_40_answered_no_2026-09-14.md`.

**F0059, Problem 18.39.** The companion question at $0 < \nu < \lambda$, where condensation occurs, with
Janson conjecturing that $Y_{(1)}/n \to_p 0$ is impossible along the whole sequence. Not answered, but
reduced to a property of one explicit function. Tilting at $\rho$ and writing $M = (\lambda-\nu)n$ for the
excess, which cannot be absorbed by tilting further, the class of configurations carrying it in $r$ boxes of
size $a$ has log-probability $M\Lambda(a) + o(M)$ with $\Lambda(a) = [\log\pi_a + \log(a/(\lambda-\nu)) +
1]/a$; the rate is calibrated by the two known condensation regimes, since for $\pi_k \sim ck^{-\beta}$ and
for $\pi_a = e^{-a^\gamma}$ it is maximised at $a = M$, which is the one-big-box picture of Theorem 18.33.
Because $\pi$ has radius one, $\limsup\Lambda = 0$ while $\Lambda < 0$, so $\Lambda$ has infinitely many
records, and at $M$ equal to a record the deterministic optimum is again a single box holding the whole
excess. What is missing is the concentration: if the record gaps exceed the configurational entropy
$C/\sqrt M$ infinitely often, the conjecture follows with $\varepsilon = (\lambda - \nu)/2$. Here the
argument that settles Problem 18.40 does not transfer, and the reason is worth stating: there the rate
diverges, so assuming small gaps at every scale and chaining them forces the rate to be bounded, a
contradiction, whereas $\Lambda$ is bounded above by zero to begin with and no counting of that kind can
produce a contradiction. So the conjecture is equivalent to a question about probability laws that has
nothing to do with allocations: must $[\log\pi_a + \log a]/a$, for a law of radius one, have records whose
gap below them exceeds $a^{-1/2}$? Memo:
`Probability_F0059_Janson_problem_18_39_reduction_2026-09-14.md`.

**F0063, Conjecture 20.1.** For $\nu \ge 1$ and $\mathbb{E}\xi^{r+1} < \infty$, do the level widths satisfy
$\mathbb{E}\,\ell_k(T_n)^r \to \mathbb{E}\,\ell_k(\widehat T)^r$, for integer $r \ge 1$ and, the survey adds, for
non-integer $r > 0$? Proved for every real $r \ge 1$, hence for every integer $r$, and for $0 < r < 1$ whenever
$\sigma^2 < \infty$; open only for $0 < r < 1$ with $\sigma^2 = \infty$. The survey's own Lemma 14.9 says that the
conditioning multiplies the Galton--Watson weight of the first $k$ generations by $W = n\ell_k\,\mathbb{P}(S_{n-N} =
n - N - \ell_k)/((n-N)\,\mathbb{P}(S_n = n-1))$, where $N$ is the number of vertices of depth less than $k$. The local
limit theorem for a finite-variance lattice law gives $W \le C\ell_k(n/(n-N))^{3/2}$, and since $n - N \ge \ell_k$
also $W \le Cn^{3/2}\ell_k^{-1/2}$. When the first $k$ generations hold at most half the tree, the tail of
$\ell_k^r W$ is bounded by the tail of $Z_k^{r+1}$ for the unconditioned tree, finite because $\mathbb{E}\xi^{r+1} <
\infty$, and independent of $n$: the size-biasing costs exactly one moment, which is why $\mathbb{E}\xi^{r+1}$ is the
right hypothesis. When they hold more than half, some generation $j < k$ exceeds $n/2k$, and Markov's inequality with
the $(r+1)$-th moment of $Z_j$ pays for the $n^{3/2}$ with a factor $(2k/n)^{3/2}$ to spare. Uniform integrability
follows, and with (20.1) so does the conjecture. The remaining case is a matter of the local limit theorem, not of the
argument: with infinite variance there is no general lower bound on $\mathbb{P}(S_n = n-1)$, and the mean-versus-centre
laws of F0058 show the ratio in $W$ can be far from bounded. Memo:
`Probability_F0063_Janson_conjecture_20_1_level_widths_uniformly_integrable_2026-09-14.md`.

### Aldous and Fill, Open Problem 4.48: one half refuted, one half proved

**P0243.** The Notes to Chapter 4 of Aldous and Fill ask whether two of the chapter's basic inequalities hold
with constant one: (a) is the variation threshold $\tau_1 = \min\{t : \bar d(t) \le e^{-1}\}$ at most Kemeny's
constant $\tau_0 = \sum_{i,j}\pi_i\pi_j\mathbb{E}_iT_j$, and (b) is the relaxation time $\tau_2 = 1/\lambda_2$ at
most the stopping-rule mixing time $\tau_1^{(2)} = \max_i\min_U\mathbb{E}_iU$ over stopping times $U$ with
$\mathbb{P}_i(X_U \in \cdot) = \pi$? The known relations are $66\tau_0 \ge \tau_1 \ge \tau_2$. Answered: (a) no,
(b) yes.

For (a), the birth-and-death chain on $\{0, 1, 2\}$ with rate $1$ toward $0$ and rate $\varepsilon$ away from it
has $\tau_0 = 2(1+\varepsilon)/(1 + \varepsilon + \varepsilon^2) < 2$ exactly (Kemeny's constant is the sum of
the reciprocal nonzero eigenvalues), while $\tau_1 \to 2.14619$ as $\varepsilon \to 0$, the time at which the sum
of two unit exponentials exceeds $t$ with probability $e^{-1}$; at $\varepsilon = 1/10$ the values are $\tau_0 =
1.981982$ and $\tau_1 = 2.010072$ to nine digits. On the path of length $k$ the limiting ratio is $t_k/k$ with
$t_k$ the Gamma$(k,1)$ tail threshold, equal to $1.0731, 1.0861, 1.0880, 1.0868$ at $k = 2, 3, 4, 5$; the
two-state chain is the equality case. So $\sup\tau_1/\tau_0 \in [1.0880, 66]$. The example came out of a random
search over 20,000 small reversible chains whose best case was this path in disguise.

For (b), let $u$ be an eigenfunction of $-Q$ for $\lambda_2$ and $i^*$ a state where $|u|$ is largest. For any
stopping time $U$ from $i^*$ with $\mathbb{P}_{i^*}(X_U \in\cdot) = \pi$ and finite mean, Dynkin's formula with
the mean occupation measure $x_j = \mathbb{E}\int_0^U\mathbf 1\{X_t = j\}dt$ gives $-u_{i^*} = \sum_j x_j(Qu)_j =
-\lambda_2\sum_j x_ju_j$, hence $|u_{i^*}| \le \lambda_2\|u\|_\infty\,\mathbb{E}_{i^*}U$ and $\mathbb{E}_{i^*}U
\ge 1/\lambda_2$. So $\tau_1^{(2)} \ge \tau_2$, with equality for two-state chains; the random search found no
ratio above $0.99999$. The argument needs only a real eigenvalue with a real eigenfunction and gives the same
bound for stopping rules to any target law. A bound this simple may be in Lovász and Winkler's *Mixing times*
(DIMACS 1998), whose text could not be fetched; the counterexample in (a) has no antecedent I could find, and
the online edition of the book carries the problem without a note. Memo:
`Probability_P0243_Aldous_Fill_open_problem_4_48_2026-09-14.md`, scripts `p0243_search.py`, `p0243_verify.py`.

### Aldous and Fill, Open Problem 4.45: lumping can increase the stopping-rule mixing time

**P0242.** Section 4.6.1 of the same book defines the induced chain of a reversible chain under a map $f$ by
matching stationary flows between blocks, proves that $\tau^*, \tau_0, \tau_2, \tau_c$ can only decrease under
it, and asks (Open Problem 4.45) whether $\tau_1^{(2)}$ of the induced chain is at most $K$ times that of the
original for an absolute $K$, and whether $K = 1$ works. Answered for $K = 1$: no. The reversible chain on
$\{0,1,2,3\}$ with symmetric weights $W_{02} = 1$, $W_{12} = 1$, $W_{13} = 109$, $W_{23} = 54$ and holding weights
$W_{11} = 117$, $W_{33} = 10000$ (rates $q_{ij} = W_{ij}/w_i$, so $\pi = (1, 227, 56, 10163)/10447$) has
$\tau_1^{(2)} = 149731115/63193903 = 2.3694$; lumping states $2$ and $3$ gives a three-state chain with
$\tau_1^{(2)} = 346900/114917 = 3.0187$, ratio $1.2740$, both values exact rationals attained at the pair
$(1, 0)$. A finer set of weights gives ratio $1.4822$; a Nelder-Mead pass over every set partition reached $1.000$ on
three states, $1.432$ on four, $1.869$ on five and $1.955$ on six, and a pass restricted to one or two merged
pairs reached $1.862$ on seven. The values cluster just below $2$, and a hand-built family (two heavy states,
a light start state, a leaf) shows why a naive push fails: the original chain's maximum moves to a different
pair of states and grows faster than the induced one. Whether the supremum is $2$ is recorded as a new
problem. The mechanism is that the block $\{2, 3\}$ forgets whether the
walk sits next to the leaf $0$ or at the sticky state $3$, so the walk from $1$ loses the advantage of entering
the block at $2$. The $K$ question stays open, and the trend of the optimised ratios is the reason it is not
conjectured either way here; it does not follow from the contraction principle because $\tau_0$ can be much
larger than $\tau_1^{(2)}$. Memo:
`Probability_P0242_Aldous_Fill_open_problem_4_45_lumping_2026-09-14.md`, script `af445_exact.py`.

### Seven questions from intake H answered the same night

**H0024, the factor four on a frog model's critical line.** In the interval-activation frog model of
arXiv:2607.27082 the activated set is an interval, and the paper's Theorem 3.1 brackets the critical line
between two constants that differ by four: extinction if $\limsup n\mathbb{P}(D^*\ge n) < 1/(2\mathbb{E}\eta_0)$,
survival if $\liminf n\mathbb{P}(D^\to \ge n) > 1/\mathbb{E}\eta_0$, with $\mathbb{P}(D^*\ge n) \sim
2\mathbb{P}(D^\to\ge n)$. Remark 3.6 says the phase diagram on the critical line is not determined by that
argument. Both factors of two are artefacts of the comparisons, and the tool that shows it is worth stating on
its own. In a firework process only the sites added at the previous step can extend the interval, the earlier
ones being already known not to reach beyond its ends; so the number $g_k$ of sites added at step $k$ is a Markov
chain, and for reaches with $\mathbb{P}(R\ge m)\sim c/m$ its conditional law telescopes:
$\mathbb{P}(g_{k+1}\le ug \mid g_k = g) \to (u/(1+u))^c$. The growth is therefore asymptotically multiplicative,
and the drift of $\log g_k$ is
$$\mathbb{E}[\log U] = \int_0^\infty \log u\,d\Big(\frac{u}{1+u}\Big)^c = \psi(c)+\gamma,$$
which vanishes exactly at $c = 1$ because $\psi(1) = -\gamma$: the classical firework threshold, with an explicit
drift. The same representation gives the subcritical decay, $\mathbb{P}(\text{size}\ge n)\asymp n^{-(1-c)}$, from
$\mathbb{E}[U^\kappa] = \Gamma(\kappa+c)\Gamma(1-\kappa)/\Gamma(c) = 1$ whose root is $\kappa = 1-c$. For the
two-sided process the far end contributes an extra factor $((u+C)/(u+C+1))^c$ with $C$ the ratio of the interval
length to the recent growth; at criticality the growth walk is null recurrent with multiplicative steps of tail
index one, so that ratio diverges and the help is irrelevant, leaving the critical constant at $1$ again. A
first-moment count agrees: an interval of size $n$ containing the origin is closed with probability $n^{-2c}$,
there are $n$ of them, and $\sum_n n^{1-2c}$ converges exactly when $c>1$. Sampling the growth from its exact
conditional law, which is a ratio of Gamma functions, follows the interval to size $10^{12}$ in about forty steps;
the one-sided control reproduces all three predictions, and the two-sided process decays with exponent about
$(1-c)^2$, vanishing at $1$ and not at $1/2$ or $1/4$. So the critical line is decided by
$\mathbb{E}[\eta_0]\kappa\lim\ell(n^r)$ against $1$, the survival half of their theorem being sharp. What is left
is the two-sided firework criterion as a theorem, which is stated below as a new problem. Memo:
`Probability_H0024_frog_model_critical_line_factor_four_2026-09-14.md`.

**H0010, a conjecture stated backwards.** Conjecture 3.2 of arXiv:2608.21125 reads "the derivative martingale
$\partial W_n$ is uniformly integrable (equivalently, $\partial W_\infty > 0$ a.s. on survival)". The two are not
equivalent, they are incompatible. The root sits at $T = 0$ and the centring vanishes there, so $\partial W_0 = 0$
and $\mathbb{E}[\partial W_n] = 0$ for every $n$; uniform integrability would give $L^1$ convergence and hence
$\mathbb{E}[\partial W_\infty] = 0$, which with $\partial W_\infty\ge 0$ forces the limit to vanish, the degenerate
case the conjecture exists to exclude. In the boundary case the limit has a Cauchy tail and infinite mean, so the
martingale is as far from uniformly integrable as one can be. The repair is to read "nondegenerate" for
"uniformly integrable" throughout, after which the paper's own Programme 3.3(2) is correct as written, since
Chen's $x\log^2_+x$ condition is necessary and sufficient for nondegeneracy; and in the bounded-degree dissipative
regime, where that paper's Remark 3.4 notes all $\log^2$ moments are finite, the repaired martingale half becomes
a theorem, leaving only the decorated-point-process transcription. Memo:
`Probability_H0010_derivative_martingale_conjecture_is_inverted_2026-09-14.md`.

**H0013 and H0014, and with them the question the source's introduction raises.** A July 2026 paper
(arXiv:2607.07410) asks whether a random drift can destroy the compactness of a confining diffusion
semigroup. On the line, with $\mu^w(dx) = e^{-w}dx$ and the Dirichlet form $\tfrac12\int (u')^2e^{-w}$, the
deterministic potentials $\pm|x|^\delta$ give a compact semigroup exactly when $\delta > 1$. The paper
perturbs them by a two-sided semi-selfsimilar Lévy process $V$ of index $\alpha \in (0,2)$ and proves that for
$\delta \le 1/\alpha$ compactness fails almost surely; its Remark 5.3(ii) says twice that for $\delta > 1/\alpha$
the authors do not know, because the criterion they use becomes an indeterminate product and they have no decay
rate for the convergent factor. It fails there too, for every $\delta$. The criterion is a weighted Hardy
inequality, so what decides compactness at $+\infty$ is whether
$B(x) = (\int_{x_0}^x e^{u})(\int_x^\infty e^{-u}) \to 0$, with $u = y^\delta + V$; bounding each integral by its
part on one side of a point $\tau$ where $V$ jumps down by $m$ gives
$\log B(\tau) \ge m - (2\delta - 2)\log\tau - O(1)$. So a well of depth $m$ at distance $\tau$ costs only a
logarithm in $\tau$, while the Lévy measure supplies wells of depth up to $\tau^{1/\alpha}$ inside
$[\tau, 2\tau]$. Polynomial beats logarithm at every $\delta$, and a Borel--Cantelli argument over disjoint
blocks turns that into $\limsup_x B(x) = \infty$ almost surely, hence $\lambda_{\mathrm{ess}} = 0$ and
noncompactness. The two operators of the paper are broken by opposite jump signs, $-|x|^\delta$ by upward jumps
and $+|x|^\delta$ by downward ones, so a spectrally one-sided drift breaks one and, by an argument written here
only as a sketch, leaves the other compact; for $\alpha < 1$ the paper's own assumption that $V$ changes sign
forces jumps of both signs, because strict semi-selfsimilarity of index $1/\alpha > 1$ leaves no drift and a
driftless one-sided process of finite variation is monotone. What made the result checkable is that the criterion
reproduces the paper's deterministic benchmark, symbolically and numerically to three decimals; the same grid
computation confirms the local formula at the two largest downward jumps of a simulated path, and evaluating it
on the jump process alone gives $\log B$ reaching $+811$ by $x = 10^6$ at $\delta = 2$ and $+757$ at $\delta = 4$,
the larger exponent only moving the crossover from $x \approx 2\cdot10^3$ to $x \approx 2.6\cdot10^4$. Memo:
`Probability_H0013_H0014_random_drift_destroys_compactness_for_every_delta_2026-09-14.md`.

**H0019.** Stepanyants, Krapivsky, Hartle and Krioukov (arXiv:2608.04303) study the *layer* of a vertex of a
random recursive tree: strip the leaves, strip the leaves of what is left, and count the rounds until the vertex
is itself a leaf. They prove that the limiting fraction $\bar\ell_k$ of vertices at layer $k$ or more is
$\int_0^\infty s_k(y)e^{-y}dy$, where $s_0 \equiv 1$ and $s_i(y) = 1 - \exp(-\int_0^y s_{i-1})$, they show by
hand that $e^{-k} \lesssim \bar\ell_k \lesssim e^{-k/e}$, and they then treat the recursion as a travelling wave:
the front moves at the velocity $1/e$, which they say is "selected" and whose rigorous characterization they call
an open problem, with a correction $\tfrac{3}{2e}\log k$ quoted from the universal Bramson form. Their
Conjecture 1 is $\ell_k = \exp[-k/e - \tfrac3{2e}\log k - O(1)]$. It is a theorem, and the recursion is not merely
wave-like: it is exactly a branching random walk. Writing $u_i = 1 - s_i$ turns the recursion into
$u_i(y) = \exp(-\int_0^y(1 - u_{i-1}))$, which is the Poisson product formula for $\mathbb{P}(M_i > y)$, where
$M_i$ is the smallest position at generation $i$ of the Poisson-weighted infinite tree: the walk in which the
children of a particle at $x$ sit at the points of a rate-one Poisson process on $(x, \infty)$. So $s_k(y) =
\mathbb{P}(M_k \le y)$ and $\bar\ell_k = \mathbb{E}[e^{-M_k}]$. That walk is the one with exponential steps
treated by Addario-Berry and Ford (Ann. Appl. Probab. 23, 2013), whose Theorem 1.1 says the median of $M_n$ is
$n/e + \tfrac3{2e}\log n + O(1)$, velocity selection included, and whose Theorem 1.2 gives uniform exponential
tails, the left one with rate any $c < e$. Since $e > 1$, those tails make $e^{-(M_k - \mathrm{median})}$
uniformly integrable, so $\bar\ell_k e^{k/e}k^{3/(2e)}$ is bounded above and below, which is the conjecture; with
Aïdékon's convergence in law of the minimum the bound becomes a limit, $\bar\ell_k e^{k/e}k^{3/(2e)} \to
\mathbb{E}[e^{-M^*}] \approx 1.42$ and $\ell_k/\bar\ell_k \to 1 - e^{-1/e}$. Their Theorem 4's lower bound
$e^{-k}$ is, in this dictionary, the contribution of a single spine, which undershoots by $e^{-k(1 - 1/e)}$.
Their Conjecture 2 asks in addition for the largest layer in a tree on $n$ vertices; its layer half is also a
theorem, because the layer of a vertex is the second largest of the branch heights at it, so the largest layer is
$\lfloor\mathrm{diam}/2\rfloor$, at most the height and at least half the sum of the two largest branch heights at
the root, and both bounds give $e\log n - \tfrac32\log\log n + O_{\mathbb P}(1)$ by Addario-Berry and Ford's
Corollary 1.3. To that precision the root of a random recursive tree is a centre of it. The numerical work behind
this is worth one sentence, because it nearly produced a wrong claim: integrating the recursion to $k = 1000$ and
fitting the exponent of $\bar\ell_k e^{k/e}$ returns $0.50$, not $3/(2e) = 0.5518$, flat over two decades, and
what resolves it is measuring the front itself rather than the transformed quantity, together with the
observation that the fitted exponent is drifting down, at the rate a correction of order $(\log k)/\sqrt k$
predicts. Memo: `Probability_H0019_layer_distribution_of_random_recursive_trees_2026-09-14.md`.

**H0020.** Neri and Pinto (arXiv:2607.07309, Remark 3.7) ask whether the contractivity condition behind their
quantitative law of large numbers for generalized Pólya urns, $\lambda_{\max}(\mathrm{symm}(C_pJ_p(R^{\mathsf T} -
\lambda I)C_p^{\mathsf T})) < 0$ for $p = d$ or $d - 1$, holds for every tenable irreducible urn with balance
$\lambda$; if it did, Theorem 1.1 of their paper would follow with rates. It does not. For $p = d$ the all-ones
vector gives the value $0$ for every balanced urn. For $p = d - 1$ the five-colour urn with balance $6$ and rows
$(0,0,4,0,2)$, $(2,4,0,0,0)$, $(0,0,3,3,0)$, $(2,0,0,4,0)$, $(0,6,0,0,0)$, tenable and irreducible, has
$\sum_{i<5}\tilde w_i(\tilde w(R - 6I))_i = 6 > 0$ at the mean-zero vector $\tilde w = (-1, 1, -1, -1, 2)$, so
the symmetrised matrix has a positive eigenvalue ($1.978$). Found by random search over integer replacement
matrices; no three-colour violation was found under any ordering of the colours, and whether an urn can violate
the condition under every ordering is left as a question. Memo:
`Probability_H0020_Neri_Pinto_urn_contractivity_fails_2026-09-14.md`.

### The ten-lane campaign of 13 September

The coordinator's order was to keep ten Opus lanes live for ten hours, half on the mathematical brain and half
on the problems. The five problem lanes produced the following, each with its own memo, literature check and
exact-arithmetic controls; the verification words are the memos' own.

- **F0065-F0070, Janson Conjecture 20.5 and the Section 20 height and width family.** Already proved: Addario-Berry and Donderwinkel, *Random trees have height $O(\sqrt n)$*, arXiv:2201.11773, Ann. Probab. 52 (2024). Theorem 1 there is Conjecture 20.5 with Problem 20.7; Theorem 20 is Problem 20.9; the width rows 20.6 and 20.8 follow in one line from $n \le (H+1)W$. Five rows to relabel. The corpus missed it because the arXiv and journal versions of the survey number the conjecture 20.5 and 21.5. Verification word: resolved in literature.
- **P0016, Randomstrasse Open Problem 21, the worst square submatrix of a Gaussian frame.** Already solved, by the owner: arXiv:2607.06249, Corollary 1.2, $\omega(A_m) = 4^{-m + o_P(m)}$. The lane re-derived the method before checking. Two increments survive: a non-asymptotic bound $\mathbb{P}(\omega \le \eta 4^{-M}) \le \eta/(2\sqrt\pi)$ and a conjectured limit law $4^M\omega \Rightarrow \mathrm{Exp}(2\sqrt\pi)$ with numerics. Verification word: resolved in literature.
- **F0008, F0009, Vu's Conjectures 8.4 and 8.5 on the symmetric sign matrix.** Two disjoint support-two eigenvectors give $\mathbb{P}(\text{two eigenvalues sum to zero}) \ge (3/2 - o(1))n^4 4^{-n}$ and the same order for a repeated eigenvalue, exact per-template probability $3\cdot 4^{-n}$ verified exhaustively at $n = 4, 5, 6$. This refutes the ledger's claims that the 8.5 event is super-exponentially small and sharpens the survey's $n^3 4^{-n}$ lower bound to $n^4$. The conjectures themselves are untouched; the cheapest obstruction sits at eigenvalues of size $O(1)$, exactly where Han's 2025 theorem does not look. Verification word: proved (the bounds).
- **E0025, Hu and Sun, Question 5: pure-jump subordinators and Hunt's hypothesis.** An explicit driftless subordinator with infinite Levy measure ($x_m = 4^{-m^2}$, $a_m = 2^{-m}4^{m^2}$) whose Kanda-Forst ratio grows like $4m$, checked at 4000 digits. It rules out the classical route to (H) for this process; its points appear to be polar, so it is not a counterexample to (H). Question 5 is untouched. Verification word: proved (the ratio); (H) unknown.
- **C0146, Monotone coupling of FK measures with cluster weight below one.** The vector-parameter version is false: raising one edge parameter strictly lowers an increasing event, exact rational witness on the triangle at $q = 1/2$ ($62/95 \to 14/23 \to 26/45$). Scalar monotonicity in $p$: no violation on any graph with at most 6 vertices and 10 edges, the minimum over all increasing events computed exactly by one max-flow per instance. Verification word: refuted (vector form); open (scalar).
- **C0091, Pairwise negative correlation in FK with cluster weight below one.** Two edges are conditionally independent given the rest unless they close a common cycle; the coefficient certificate fails on the triangle. No counterexample on small graphs. Verification word: no progress on the conjecture.
- **P0001, Grimmett's Conjecture 4.2, negative correlation in uniform forests.** An exact identity for the covariance and its corollaries (parallel pair: exactly $-(1/9)\mathbb{E}[A_e]^2$); dense 9- and 10-vertex search, no counterexample; the general conjecture untouched. Verification word: partial.
- **P0037, BK inequality for the weighted uniform spanning tree.** Proved when one event is principal, 55,964 exact instances; the cited negative-association theorem covers only the uniform measure, a citation scar recorded. General case untouched. Verification word: partial.
- **P0177, Hasebe and Ueda, Problem 4.6: the mode of free Brownian motion at large time.** Asymptotic expansions of the mode for classical and free Brownian motion from a compactly supported initial law: the free displacement is exactly six times the classical one, both $O(1/t)$, far inside the source's $\sqrt t$ window. Verification word: proved.
- **P0025, Burdzy, Problem 5(ii): synchronous reflection outside a disk.** The separation is a pure local-time process whose sign is a tangent-line condition; a simulation that looked decisive was not. Verification word: not settled.
- **E0065, Rozikov's Problem 12, exact regularity thresholds for quadratic stochastic operators.** $\alpha_3 \ge 1/12$ by an explicit family with an exact rational 2-cycle at $L = 1/13$, so $1/12 \le \alpha_3 \le 1/6$; $\alpha_3 = 1/12$ conjectured from an exhaustive vertex-ansatz search. The $m = 2$ analysis reproduces the known $(3 - \sqrt 7)/2$. Verification word: proved (lower bound).
- **E0068, Rozikov's Problem 21, operators whose power returns to themselves.** Reduction: $V^r = V$ iff $V$ restricted to its image is a bijection of finite order dividing $r - 1$; the minimal exponent is that order plus one. Verification word: structural reduction.
- **P0245, Aldous and Fill Open Problem 6.30, minimal stationary cover time.** Proved for $n = 3$ symbolically, with equality only for the triangle; a correction to the monograph's Example 6.29 verified. Verification word: proved ($n = 3$).
- **P0253, Antivoter variance maximised by the complete graph.** Three exact identities, a spectral upper bound tight only at $K_n$, exhaustive verification over every admissible regular graph on $n \le 9$ vertices. Open. Verification word: verified to $n = 9$.

Two lessons from those lanes belong in the method chapter. First, the literature check runs before the attack
and includes the owner's own arXiv listing: P0016 was his theorem, and F0065 was a 2022 Annals paper hidden
behind a numbering change between the arXiv and journal versions of the survey. Search the statement, not the
label. Second, a census at the sizes a laptop reaches can point the wrong way: for Vu's conjectures the
normalised singularity probability is still rising monotonically at $n = 13$ and support-two kernel vectors
explain a fifth of the event, yet a first-moment count shows the conjectured mechanism wins only from $n \approx
30$; the asymptotic regime is a factor $4^{16}$ away in probability and no amount of compute closes it.

### Corrections to the record

- **E0052 is misstated.** The ledger row says "prove or disprove $\mathbb{P}(\sum X_i \le n + 1) \ge 1 - 1/e$"
  and describes the extremal example as giving $1 - (n/(n+1))^n$. Feige's conjecture is the lower bound
  $\mathbb{P}(\sum_i X_i < n + 1) \ge 1/e$ for independent nonnegative $X_i$ with $\mathbb{E}X_i \le 1$, and the
  extremal example $X_i = n + 1$ with probability $1/(n+1)$ gives exactly $(n/(n+1))^n \downarrow 1/e$ for the
  event that all $X_i$ vanish; the row's event and constant do not match the source. The row should be
  restated. Its status also needs re-checking: three 2026 postings claim or approach a proof (Nie and Wei,
  *On Feige's conjecture*, arXiv:2607.24528; arXiv:2508.07316; arXiv:2509.19949 for the identically distributed
  case), and the best constant before them was $0.1798$ (Guo, He, Zhang and Zhang).
- **E0044 is misstated, and half of its source is settled.** The ledger row says part (b) of Bandeira's Open
  Problem 0.2 is the reverse inequality, the norm of the symmetrised product average at least the norm of the
  full average. The source's (b), read on 14 September, puts the norms inside the sums: the average over
  permutations of $\|\prod_j A_{\sigma(j)}\|$ is at most the average over all $n$-tuples of $\|\prod_j A_{k_j}\|$.
  The row's inequality is false trivially (two orthogonal projections give a zero symmetrised product and a
  positive full average) and is not what anyone conjectured. As for the source's two parts: (a), the Recht and
  Re inequality with the norm outside, is false for $n \ge 5$ by Lai and Lim (ICML 2020, arXiv:2006.01510), who
  reduce it to a semidefinite programme through the noncommutative Positivstellensatz, and true for $n = 3$ by
  Zhang (arXiv:1411.5058); (b) is reported as proved for $n = 3$ by Israel, Krahmer and Ward (arXiv:1411.0333)
  and open beyond; both attributions come from the literature summaries read on 14 September, not from the
  papers. The row should be restated as (b) and cite these three papers.
- **Two conjectures tested numerically, no counterexample.** E0045 (Mallat and Zeitouni: the eigenbasis of
  $\Sigma$ maximises the expected largest $d$-dimensional coordinate projection of a Gaussian vector; known for
  $d = 1$): Monte Carlo with 60,000 common samples and a Nelder-Mead search over rotations of the eigenbasis at
  $(p,d) = (3,2), (4,2), (4,3), (5,2)$ with random and one-dominant spectra; every excess over the eigenbasis is
  below the sampling error and consistent with the optimiser fitting noise. C0033 (Lyons' Conjecture 2.6, midpoint
  concavity of the entropy of determinantal measures in the kernel): 12,000 random pairs of positive contractions
  on ground sets of two to five points, exact point probabilities; the smallest concavity gap is $0$, at the zero
  kernel. Both remain open; neither search is evidence of much.
- **D0039 re-admission** (Virag's Question 1) was recommended on 8 September and is still pending in the ledger.
- **The six unchecked intake-D exclusions are all correct.** Compared by name against the cited sources on 14
  September: D0001 (uniqueness of the centre of complete mixability) is answered in the negative by Puccetti,
  Rigo, Wang and Wang, J. Theoret. Probab. 32 (2019), whose Cauchy example has an interval of centres; D0013,
  D0014 and D0015 (the sine-trajectory, Archimedean-limit and great-circle conjectures of Angel, Holroyd, Romik
  and Virag) are the three theorems of Dauvergne, *The Archimedean limit of random sorting networks*, J. Amer.
  Math. Soc.; D0055 (the Derrida and Retaux free-energy exponent) is Chen, Dagard, Derrida, Hu, Lifshits and Shi,
  Ann. Probab. 49 (2021), under an integrability hypothesis the source's own statement allows; D0096 (the
  activated-random-walk critical density below one) is Asselah, Forien and Gaudilliere, Ann. Probab. 52 (2024),
  whose abstract states the bound for every dimension and every sleep rate, which covers the unbiased planar
  case the row asks about. With D0022 and D0039 checked on 8 September, all eight exclusions of intake D are now
  audited: seven hold, one (D0039) fails.
- **Two Aldous and Fill conjectures searched, not settled.** Open Problem 6.30 (P0245, the stationary cover
  time is at least $(n-1)h_{n-1}$): 120 Nelder-Mead runs over reversible chains with self-loops on $n = 3, 4, 5$
  states, exact subset dynamic programme, all converge to the complete graph, best values $3, 5.5, 8.3335$
  against targets $3, 5.5, 8.3333$. Conjecture 9.22 ($\mathrm{tr}\,Z^2(P^* - P) \ge 0$ for the fundamental
  matrix of a general chain): 150,000 random chains on three to six states, minimum $-4.6\cdot 10^{-10}$, which is
  rounding at reversible chains, where the quantity is zero; the control $\mathrm{tr}\,Z(P^* - P) \ge 0$
  (Proposition 9.21) held to $-3\cdot 10^{-13}$. Evidence, not proof, for both.
- **P0249, Aldous and Fill Conjecture 9.22, independently re-derived.** The Codex proof file for this row
  (excluded on 7 September as a consequence of Huang and Mao 2020, with a direct matrix proof of its own) was
  reached again from scratch on 14 September without reading it first: with $S = D^{1/2}PD^{-1/2}$, $N = S -
  \sqrt\pi\sqrt\pi^{\,T}$, $A, B$ its symmetric and skew parts and $M_s = I - sA$, the quantity
  $\tilde F(s) = \mathrm{tr}((I - sN)^{-1}(N^T - N))$ equals $(4/s)\sum_k \theta_k(s)^2/(1 + \theta_k(s)^2)$ over the
  eigenvalue pairs $\pm i\theta_k(s)$ of $sM_s^{-1/2}BM_s^{-1/2}$; each $\theta_k(s)$ is nondecreasing in $s$ by
  Loewner monotonicity of $s(I - sA)^{-1}$; and $\mathrm{tr}\,Z^2(P^* - P) = \frac{d}{ds}[s\tilde F(s)]_{s=1}
  \ge 0$, with $\tilde F(1) \ge 0$ recovering Proposition 9.21. This is the Codex file's argument in different
  coordinates (its $F(t) = \mathrm{tr}(H + tK)^{-1}$ is the same monotone function), so the row's proof now has
  the independent read it lacked; the three identities were also checked numerically on 2,500 random chains,
  periodic ones included (`af922_check.py`). The exclusion stands: the result is a consequence of Huang and
  Mao's Theorem 4.3, and the search over 150,000 chains reported above was made before the file was read.
- **Intake H, 21 rows admitted after a source check.** A lookup agent collected 25 statements from 14 arXiv
  papers posted July to September 2026 (`06_math_research/probability_1000_intake_H_20260914/`). Three duplicate
  existing rows (Flammant's Conjecture 2.2 is G0004, Cerf's Conjecture 1.1 is the $\theta(p_c) = 0$ rows, Tang and
  Zhang's pairwise negative correlation is C0091). A second agent then fetched every remaining paper (PDF text
  extracted locally where the HTML was truncated) and compared each row with the paper's own sentence: 21 of 22
  confirmed verbatim and called open by their authors; one (H0024, the frog model's critical-line gap) has the
  right statement under the wrong label, corrected to Theorem 3.5(ii) and Remark 3.6; one (H0025, the Radin,
  Ren and Sadun step-function conjecture for constrained graphons) is resolved in the non-extremal regime by the
  very paper that states it and is recorded as `resolved_in_source`, open only in the extremal regime. The 21
  confirmed rows are admitted with the verification file beside the ledger; the campaign's admitted count moves
  from 908 to 929, the distinct-id count from 1,025 to 1,050.
- **P0244 is partially resolved, and the corpus did not know it.** Aldous and Fill's Open Problem 6.14
  groups seven conjectured extremal asymptotics over regular $n$-vertex graphs. The last of them,
  $\max\tau_2 \sim \tfrac{3}{2\pi^2}n^2$, became a theorem on 30 August 2026: the paper recorded as intake I
  row I0015 proves $\lambda(G) \ge (1-\varepsilon)2\pi^2/(3n^2)$ for every connected simple $d$-regular graph
  of large order, uniformly in the degree, and shows every noncubic degree admits a uniformly larger
  constant, so cubic graphs are extremal. The other six conjectures stand. The row had been carried as
  unverified. It was found by cross-referencing the new intake's resolution rows against the old ledgers,
  which is the half of intake work that repairs a corpus rather than growing it: a list of open problems
  decays from the top as they are solved, and an intake that only adds never notices.
- **Status records appended** to intake F's `problems.jsonl` for F0056, F0058, F0061, F0062 (last records dated
  14 September), with the earlier heuristics on F0061 and F0062 marked superseded. The earlier copy is backed up
  beside the file.
- **The two-sided firework criterion, as first published here, was wrong.** The memo of 14 September on the
  frog-model critical line proposed that the two-sided firework on $\mathbb{Z}$ with reach tails $c_R/n$ and
  $c_L/n$ survives exactly when $c_R + c_L > 2$, reasoning from a first-moment count of closed intervals. The
  criterion is $\max(c_R,c_L) > 1$. Survival above it is a coupling needing no numerics: delete one side's
  reaches and the sites that side contributes, and what remains is a one-sided firework, whose threshold is
  classical. So $(c_R,c_L) = (1.5, 0.4)$ has sum $1.9$ and survives, which simulation confirms out to size
  $10^9$. The frog-model conclusion is unaffected, both sides there carrying the same constant, and the
  factor of four remains an artefact; what changed is the open problem published beside it, which now asks
  for the extinction half. The memo and the ledger row carry the corrected statement.

### A seventh ledger: intake I

The campaign's mandate is a thousand problems, and half of that is finding them. A seventh ledger was
opened on 14 September, `probability_1000_intake_I_20260914`, and it ended the day with a hundred and
seventeen records from thirty-four sources: a hundred and six open problems and eleven records of named
problems recently closed. They came from five sweeps. The first read nineteen records out of September 2026 arXiv
probability papers, fourteen open problems the sources pose and five records of problems those papers
close.

The difference from the earlier intakes is in the verification line. Intake H's statements were
gathered by a lookup agent from abstracts, and its rows say so: "NOT yet checked against the paper".
Every statement in intake I was read from the paper, with the PDF fetched, the text extracted, the
passage located, and the wording quoted from it, and the locator names the section, remark or problem
number it came from. What is still missing is a search for a later resolution, so the open status is
the source's own as of its posting date.

The fourteen open rows are: four from Bou-Rabee and Peres on the randomly oriented Manhattan lattice
(the order of the annealed mean-square displacement, a polynomial decay rate for the return
probability, which orientation fields give recurrence, and the walk whose horizontal orientations are
set by an irrational rotation); two from Bou-Rabee and Panagiotis on parking (the four-dimensional case
of the closer-to-a-car question, which their results leave between $d \le 3$ and $d \ge 5$, and the
odometer rate in high dimension for environments unbounded below); three from Adhikari, Gheissari and
Peled on sloped height functions (Sheffield's localization conjecture for a general slope, his
Conjectures 10.3.1 and 10.3.2, and the existence question in three dimensions and above); two on the
maximum relaxation time of a random walk on regular graphs; the boundary case of the collision
transition on comb graphs; and two on the central limit theorem for $\rho$-mixing sequences.

A second sweep went back to the campaign's most-mined source. Extracting every `Open Problem X.Y` label
in Aldous and Fill's monograph gives thirty-one distinct problems; the campaign carries twenty-one rows
for that source, and thirteen of the labels appear in none of them: 2.34, 3.44, 4.38, 4.49, 6.13, 6.35,
7.26, 7.30, 7.31, 8.23, 14.12, 14.29 and 14.31. Ten are added as open rows: a portmanteau theorem for
occupation times, an exact characterization of the relaxation time as an infimum over flows, a simple
proof and a diameter version of an eigentime inequality, the extremal $n^3/54$ conjectures for the
Kemeny constant and the relaxation time over all graphs, whether the expected cover time can be computed
in polynomial time, a stronger monotonicity for arc-transitive graphs, linear Kemeny constant for
distance-regular graphs, a characterization of the hypercontractivity time by the Dirichlet form, cover
time asymptotics for vertex-transitive graphs with a spectral gap, and relaxation-time bounds for the
charged-particle model.

The other three had been settled long before the campaign began, which is the more useful half of the
finding. Open Problem 4.38, whether $\tau_2 \le K\sup_A\pi(A)\mathbb{E}_\pi T_A/\pi(A^c)$ for reversible
chains, was resolved by Hermon in April 2023, whose abstract says in as many words that it "resolves a
conjecture of Aldous and Fill". Open Problem 7.26, the cover time of the two-dimensional torus, was
resolved by Dembo, Peres, Rosen and Zeitouni in the Annals in 2004; their $(2N\log N)^2/\pi$ is the
source's $(1/\pi)n\log^2n$ once $n = N^2$. And Open Problem 14.29, whether the interchange process has
the same relaxation time as the single-particle walk, is Aldous's spectral gap conjecture, proved by
Caputo, Liggett and Richthammer in 2010. A campaign that had recorded those three as open would have
spent time on them.

The same sweep then ran on four more sources with local text, and found numbered problems in all of
them that no row carried: nine from Schramm's collection of problems at the 2006 congress, on the
self-avoiding walk's scaling limit, speed of convergence to SLE, the Fourier spectrum of percolation
crossings, the scaling limit of dynamical percolation and which compact sets an SLE path hits; six from
van der Hofstad's Saint-Flour notes on preferential attachment and configuration models; four from the
beta-splitting overview; five from Lyons and Peres, including the conjecture that a transitive graph of
at least quadratic growth has $p_c < 1$; and three from the first-passage percolation survey. Of eight
sources checked, five had gaps.

At that point the sweep was worth making mechanical, and it was run over all 191 sources that have a
local copy of their text: extract every line beginning with a numbered `Open Problem`, `Problem`,
`Question` or `Conjecture`, compare with the locator numbers of the rows carried for that source, cut the
statement from the text at the label, and drop anything that reads like a citation, an index line or a
sentence that is not a problem. Twenty-nine sources had gaps, 122 labels in all, and the pass added
fifty-five more rows: fifteen from the Randomstrasse lists of 2024 and 2025, eleven from the Agresti and
Veraar problem lists on stochastic maximal regularity, seven from Salez's Markov notes, and the rest in
ones and twos across sixteen further sources. Two sources were excluded after looking at what the filter
produced: the recursive distributional equation survey, whose local text carries its index lines and not
its statements, and a 2026 note whose labelled conjectures are ones the note itself reports
counterexamples to. The intake closed the day at 117 records from thirty-four sources, 104 of them open problems. The
count is 104 rather than the 106 first recorded because a later pass over every row, looking for the
phrases with which a paper announces its own answer, caught two labels the sweep had cut from a
sentence the source itself resolves in the next line: Spencer's question on the at-least-two rule for
Poisson Galton-Watson trees, answered in the negative by the paper quoting it, and the motivating
question of the free Brownian unimodality paper, answered by its own Theorem 1.2. Both rows are kept
so that neither is attempted again.

Three of the five resolution rows from the first sweep close problems from lists the campaign already mines, which is
the reason to record them. Aldous and Fill's Open Problem 6.14, the spectral gap conjecture for regular
graphs, was proved on 30 August 2026: every connected simple $d$-regular graph of large order $n$ has
spectral gap at least $(1-o(1))2\pi^2/(3n^2)$, uniformly in the degree, with cubic graphs attaining it.
All seven of Häggström and Rosenthal's open problems on the variance in Markov chain central limit
theorems were resolved on 7 September 2026, and that paper records that one of the seven was worked out
over a week of interaction with a language model, with the authors taking responsibility for the
arguments. Tao's 2010 discrete entropy monotonicity conjecture was proved on 31 August 2026. The fourth
and fifth are the parking questions above and the transience of the Manhattan lattice, whose proof is
formalised in Lean 4 with no appeal to `sorry`.

### Three problems the corpus never recorded, two of them answered

Sweeping Janson's survey for every numbered problem or conjecture turns up nineteen. Intake F carries
sixteen, as rows F0055 to F0070, and none of the seven ledgers carries the other three: searching every
row's locator, title and statement for either the arXiv or the journal numbering returns nothing for
Problems 20.3, 20.4 and 20.11, while the same search returns the rows for Problems 20.2, 20.5 and 20.7,
which is the control that the search works. Two of the three sit one step from Problem 20.2, and the
answer to it settles them. They are now rows I0020 to I0022 of intake I.

**Problem 20.3** asks to extend the asymptotic normality of the counts $N_d$ of boxes with $d$ balls from
the tree case to the general allocation $B_{m,n}$ with $m/n \to \lambda$, and guesses that $0 < \lambda <
\nu$ is easy. The guess is right and the general answer is a four-way split. For $\lambda < \nu$ the
tilted law sits at $\tau < \rho$, so it has an exponential moment, the conditioning is at its mean, and
the conditioned multivariate local limit theorem gives
$$\frac{N_d - n\pi_d}{\sqrt n}\longrightarrow N\Big(0,\ \pi_d(1-\pi_d) - \frac{(d-\mu)^2\pi_d^2}{\sigma^2}\Big),
\qquad \mu = \min(\lambda,\nu),$$
jointly in $d$, with covariance $-\pi_d\pi_e - (d-\mu)(e-\mu)\pi_d\pi_e/\sigma^2$; at $\mu = 1$ this is
Kolchin's variance and Janson's covariance, so the tree case is the special case and the formula is its
own control. For $\lambda = \nu$ with $\sigma^2 < \infty$ the same argument works with the
finite-variance lattice local limit theorem. In the two remaining regimes the formula would read
$\pi_d(1-\pi_d)$, and it holds under regular variation and fails in general: at $\lambda = \nu$ with
$\sigma^2 = \infty$ by Theorem B of the F0064 memo, and at $\lambda > \nu$ by its Theorem A, which is
exactly a condensation case. So the counts are asymptotically normal precisely when the conditioning
sits at the mean of a finite-variance tilted law, and otherwise only under a regularity condition.

**Problem 20.4** asks the same for the fringe subtree counts of Theorem 7.12. For $\nu \ge 1$ with
$\sigma^2 < \infty$ the survey's own author answered it four years later, in his 2016 paper on the
asymptotic normality of fringe subtrees and additive functionals, whose Theorem 1.5 gives exactly that,
jointly, assuming only mean one and finite variance. Outside that regime it fails and the counterexample
needs no new work: the single-vertex fringe subtree is a leaf, so its count is $N_0$, and in both
constructions the bulk sits on the degrees $0$ and $1$, so the leaf count inherits the two-point
behaviour of $N_1$.

**Problem 20.11** asks whether the condensation regime $\nu < 1$ has a scaling limit object like the
continuum random tree. That is settled for non-generic power-law weights by Kortchemski (2015): a unique
vertex of macroscopic degree, a forest of subcritical trees around it, and a height that grows
logarithmically, so there is no $\sqrt n$ metric limit and the limiting object is the condensation
structure itself. The gap left is the general subcritical weight sequence without a regularly varying
tail, where, by the same mechanism as in F0058 and F0064, the size of the condensate is not
asymptotically determined. Memo:
`Probability_F0064b_Janson_problems_20_3_20_4_20_11_2026-09-14.md`.

### One of the new problems, attacked the same day

Among the thirteen Aldous and Fill problems the ledgers had never carried is Open Problem 4.49, and its
part (ii) turns out to be exactly computable at small sizes. Section 4.3.5 defines, for a family
$f = (f^{(a)})$ of unit flows from each state $a$ to $\pi$,
$$\psi(f) = \max_{(i,j)}\sum_a\frac{\pi_a|f^{(a)}_{ij}|}{\pi_ip_{ij}},$$
and records Sinclair's inequality $\inf_f\psi(f)\le K\tau_2\log n$, which comes from Leighton and Rao's
multicommodity flow theorem. Part (ii) asks whether the diameter may replace $\log n$.

The point is that $\inf_f\psi(f)$ is a linear program: the flows are free variables, conservation is
linear, and a maximum of sums of absolute values linearises with one auxiliary per source and edge. For
the simple random walk $\pi_ip_{ij} = 1/(2m)$ on every edge, so the objective is
$2m\max_e\sum_a\pi_a|f^{(a)}_e|$, and with $2nm+1$ variables the program is small enough to solve exactly
for a few dozen vertices. Over every connected graph on four to seven vertices, 992 of them, the ratio
$\inf_f\psi/(\tau_2\Delta)$ that part (ii) asks to be bounded has maximum exactly $2$, attained by the
complete graph and nothing else; for $K_n$ the program returns $\inf_f\psi = 2(n-1)/n$ against
$\tau_2 = (n-1)/n$ and $\Delta = 1$, confirmed again at $n = 8, 12, 16$. Across twenty-seven named
families up to twenty-five vertices nothing else came above $1.37$, the runner-up being the complete
bipartite graphs. The program passes its own checks, returning $n/2$ for the cycle, $n-1$ for the path
and $2$ in the limit for stars, all of which can be done by hand.

That is evidence and not a proof, and it cannot be one: the Leighton and Rao gap that makes the
inequality nontrivial only appears at sizes far beyond exact search. What the computation does give is a
sharper statement to aim at, namely $\inf_f\psi(f)\le2\tau_2\Delta$ with equality exactly for the complete
graphs, and a reading of why the ratio stays put. Routing every source along shortest paths spreads a
total flow volume of about $n$ times the mean distance over $m$ edges, so $\psi\approx2\times$ the mean
distance whenever the routing can be balanced, and $\tau_2 \ge 1/2$ always because the second eigenvalue
is at least $-1$; the families where balanced routing fails worst, expanders and barbells, both pay for it
in $\tau_2$ at the same rate. Memo:
`Probability_I0026_Aldous_Fill_open_problem_4_49_evidence_2026-09-14.md`.

### A sharp constant for free Brownian motion

Hasebe and Ueda ask, in *Unimodality for classical and free Brownian motions* (ALEA 15, 2018,
Problem 3.3), for the optimal universal constant $C$ such that $\mu \boxplus S(0,t)$ is unimodal for
every $t \ge C D_\mu^2$, where $D_\mu$ is the diameter of the support and $S(0,t)$ is the semicircle law
of variance $t$. Their Theorem 3.2 proves $C \le 4$. The answer is $C = 1$.

**Theorem.** For every compactly supported $\mu$ with support of diameter $D$, the measure
$\mu \boxplus S(0,t)$ is unimodal for every $t \ge D^2$; and the symmetric Bernoulli law on $\{-1,1\}$,
for which $D^2 = 4$, is not unimodal for any $t < 4$.

Their own Lemma 3.1 turns unimodality into a statement about level sets: the measure is unimodal exactly
when, for every $R > 0$, the equation $\xi_R(u) = 1/t$ has at most two solutions, where
$\xi_R(u) = \int d\mu(x)/((x-u)^2+R^2)$. Three solutions
force a local minimum of $\xi_R$ with a local maximum on each side and with value at most $1/t$, so
everything reduces to bounding such a minimum from below, and the claim is that it is at least $1/D^2$.

What makes that tractable is that the two conditions defining the minimum are linear in $\mu$. The set of
probability measures on the support whose $\xi_R$ is stationary at the point in question is convex and
compact, and its extreme points carry at most two atoms, so a Choquet decomposition reduces the whole
problem to a pair of atoms at $-a$ and $b$ with $a + b \le 1$, plus a single atom at the stationary point
itself. For a pair, stationarity fixes the weights, and with $D = a+b$ and $m = ab$ the curvature and the
value collapse to two quadratics,
$$3m^2 + s(6m - D^2) - s^2 \quad\text{and}\quad 3m^2 + m(1-D^2) + s(1-2m) - s^2, \qquad s = R^2,$$
whose signs are those of $\xi_R''$ and of $\xi_R - 1$. The first is increasing in $m$, so at
$m = D^2/4$ it is $(3D^2-4s)(D^2+4s)/16$, and its nonnegativity forces $s \le \tfrac34 D^2$. The second is
concave in $s$, is $m(1+3m-D^2) \ge 0$ at $s = 0$, and at $s = \tfrac34$ is least at $m = D^2/4$ where it
equals $(1-D^2)(D^2+3)/16 \ge 0$. So a nonnegative curvature anywhere forces $s \le \tfrac34$, and then
every extreme point has value at least one. Equality holds only for two equal atoms at $\pm\tfrac12$ with
$R^2 = \tfrac34$, which is the symmetric Bernoulli law at its critical radius: the extremal measure is
unique, which is why the constant it produces is the answer. The rigidity gives more than sharpness: writing $t^*(\mu)$ for the
least time from which $\mu\boxplus S(0,t)$ is unimodal, attaining $t^*(\mu) = D_\mu^2$ forces that same
equality, so the bound $t^*(\mu)\le D_\mu^2$ holds with equality only for the symmetric two-point law, and
every other measure of the same diameter settles strictly sooner.

Three checks agree. The criterion implemented from Lemma 3.1 reproduces the paper's own worked example,
giving the Bernoulli threshold as $3.985$ against the exact $4$. A separate computation of the density
itself, from Biane's description, counting modes rather than level sets, puts that threshold between
$3.95$ and $4.05$, an asymmetric pair between $0.55$ and $0.60$ against the criterion's $0.548$, and a
three-atom measure between $0.75$ and $0.80$ against the criterion's $0.774$, each comfortably inside the
guarantee. Both identities and both inequalities were confirmed symbolically, and the two-atom case
scanned over $1.2 \times 10^8$ parameter triples without a violation.

One correction rides along. The paper reports $2 \le C \le 4$ and attributes the lower bound to the
Bernoulli example, but that example gives $C \ge 1$, the comparison there being made against $D_\mu$
rather than $D_\mu^2$. The theorem closes the interval from below in any case. Memo:
`Probability_I0086_free_brownian_unimodality_sharp_constant_2026-09-14.md`.


### A conjecture on Hadamard discrepancy that was settled in 1983

The Randomstrasse 2024 problem list conjectures, as its Conjecture 13, that the Sylvester Hadamard
matrix $H_k$ of order $2^k$ has $\operatorname{disc}(H_k) = \sqrt2\,\sqrt{2^k}$ for every odd $k$, where
$\operatorname{disc}(A) = \min_{x\in\{\pm1\}^n}\|Ax\|_\infty$. It is false, and the answer is complete
rather than a bare counterexample: the equality holds exactly for $k \in \{1,3,5,7\}$ and fails for every
odd $k \ge 9$.

The list's own Remark 6.1 observes that $H_k$ is the Boolean Fourier transform and points the reader at
that literature without following the thread. Followed, it ends the question. Index the matrix by
$(H_k)_{a,u} = (-1)^{a\cdot u}$ and read a sign vector as the $\pm1$ truth table of a Boolean function
$f$ on $k$ variables; then $H_kx$ is the Walsh transform of $f$, and since the nonlinearity of $f$ is
$2^{k-1} - \tfrac12\max_a|W_f(a)|$,
$$\operatorname{disc}(H_k) = \min_f \max_a |W_f(a)| = 2^k - 2\max_f \operatorname{NL}(f),$$
which is the covering radius of the first-order Reed--Muller code $\mathrm{RM}(1,k)$. The conjectured
value is precisely the bent concatenation bound $\operatorname{NL} = 2^{k-1}-2^{(k-1)/2}$, and the
tensor construction the list uses for its upper bound is precisely the concatenation that achieves it.

Whether that bound is optimal for odd $k$ has been settled twice. Patterson and Wiedemann built a
function on fifteen variables of nonlinearity $16276$ against the bound's $16256$ in 1983, forty-one
years before the conjecture was posed, which gives $\operatorname{disc}(H_{15}) \le 216 < 256$. Kavut,
Maitra and Yücel closed the small cases in 2006, and their title states the answer in full: functions on
$k$ odd variables beating the bound exist if and only if $k > 7$. Their nine-variable functions reach
nonlinearity $241$, raised to $242$ the following year, so $\operatorname{disc}(H_9) \le 28$ against the
conjectured $32$.

Both halves were checked here rather than taken on trust. The three published nine-variable truth tables
were read and their Walsh spectra computed directly, giving $\max_a|W_f(a)| = 28$ in each case; since
nonlinearity is unchanged by permuting input coordinates or complementing the function, no ambiguity in
how the hexadecimal is laid out can affect that. The small cases were computed exhaustively over all
$2^n$ sign vectors, giving $\operatorname{disc}(H_k) = 2, 2, 4, 4$ for $k = 1,2,3,4$, which confirms the
conjecture where it holds and the list's even-$k$ theorem alongside it.

The consequence for the neighbouring Conjecture 12, that
$\limsup_n \sup_A \operatorname{disc}(A)/\sqrt n > 1$, is that its proposed route is gone but its
conclusion is untouched. For odd $k$ there is no bent function, so Parseval is strict and the Sylvester
ratio exceeds one for every odd $k$; the measured values are $1.237$ at $k=9$ and at most $1.193$ at
$k=15$, against the conjectured $\sqrt2$, and the known upper bounds on nonlinearity leave room for the
ratio to fall to one. Memo:
`Probability_I0092_sylvester_hadamard_discrepancy_conjecture_false_2026-09-14.md`.


### The largest discrepancy of a sign matrix, for small sizes

Open Problem 11 of the same 2024 list asks for
$\sup_n \sup_{A\in\{\pm1\}^{n\times n}} \operatorname{disc}(A)/\sqrt n$, where
$\operatorname{disc}(A) = \min_{x\in\{\pm1\}^n}\|Ax\|_\infty$, and records $\sqrt2$ from the
two-by-two Hadamard matrix as the lower bound it knows. Spencer's theorem makes the supremum finite,
with the constant now down to $4.1$.

The maximum is computable exactly for small $n$, and here it is:

| $n$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\max_A\operatorname{disc}(A)$ | 2 | 1 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 |
| ratio | 1.414 | 0.577 | 1.000 | 1.342 | 1.633 | 1.134 | 1.414 | 1.667 | 1.265 | 1.508 |

so the supremum is at least $5/3$, attained at $n=9$ by an explicit nine-by-nine matrix, and at $n=6$ by
a six-by-six one giving $4/\sqrt6$. Both are above the $\sqrt2$ the list records.

The reason the values can be computed at all, and the reason they look so ragged, is that this is a
covering-code question. Since $r\cdot x = n - 2d(r,x)$ in Hamming distance, $|r\cdot x| \ge v$ says $x$
is within distance $(n-v)/2$ of the row $r$ or of its complement, so $\operatorname{disc}(A)\ge v$ says
exactly that the $n$ rows and their complements cover the cube at that radius. Hence
$$\max_{A}\operatorname{disc}(A) = n - 2\min\{R : \text{a complement-closed binary code of length } n,\
\text{size } 2n,\ \text{has covering radius } R\},$$
and the answer can be read off the published tables of $K(n,R)$, the least size of a binary covering code
of length $n$ and radius $R$: $K(n,R)\le n$ makes $R$ achievable and $K(n,R)>2n$ rules it out. It does not
settle $n=12$, which the integer programme could not decide either: discrepancy $6$ there needs a
complement-closed covering code of length $12$, size $24$ and radius $3$, and the published bounds
$18 \le K(12,3) \le 28$ straddle $24$. The same straddling leaves several larger sizes open, and that is
where the room is. At $n=21$ a radius-six covering code of size $42$ would give discrepancy $9$ and a
ratio of $1.96$; the tables neither provide one nor rule it out.

Nothing in the table depends on trusting the solver. Each value in the top row is an explicit matrix
whose discrepancy was recomputed by brute force over all $2^{n-1}$ sign vectors, and each claim that no
matrix does better follows from counting alone, except at $n=10$, where the programme returned a proved
infeasibility and the tabulated $K(10,2)=30>20$ says the same thing independently. The distinction
mattered: a first version of the wrapper read a solver time limit as a proof of impossibility, which
would have put a wrong value in the table at $n=12$ with nothing to flag it.

Two neighbouring results are worth separating from this one. The stronger lower bound $1+\sqrt2$ of
Kunisky is for the Komlós constant, the same supremum over real matrices with columns of Euclidean norm
at most one, and his construction uses matrices with zero entries, so it says nothing about the $\pm1$
question; the unpublished numerical example at $n=15$ attributed to Spielman is in that same setting.
Memo: `Probability_I0095_sign_matrix_discrepancy_exact_small_values_2026-09-14.md`.


### Hitting times on distance-regular graphs

Aldous and Fill's Open Problem 7.31 asks for a proof that $\tau_0 = O(n)$ over distance-regular graphs
other than the cycles, where $\tau_0 = \max_{i,j}\mathbb{E}_iT_j$, and records that Biggs computed
$\tau_0/(n-1) = 195/101$ on a cubic graph with $102$ vertices and outlined an argument that this may be
the largest value over the known such graphs.

The problem is an identity in disguise. In a distance-regular graph $\mathbb{E}_iT_j$ depends only on
$d(i,j)$, so the distance to a fixed target is a birth-and-death chain on $\{0,\dots,d\}$ with down-rate
$c_i/k$, up-rate $b_i/k$ and stationary measure $k_i/n$. The birth-and-death formula for a downward step
gives
$$\tau_0 = \mathbb{E}_dT_0 = k\sum_{i=1}^{d}\frac{k_i+k_{i+1}+\dots+k_d}{k_i\,c_i},$$
so the question is about intersection arrays and no graph need be built. Two things follow immediately.
The $i=1$ term is $k(n-1)/(k c_1) = n-1$ exactly, so every distance-regular graph has
$\tau_0 \ge n-1$, with equality only for the complete graph, and the conjecture is that the remaining
terms add no more than a bounded multiple. And the excluded case shows what failure looks like: for the
$n$-cycle $k_ic_i = k$ for every $i$, so all $d\approx n/2$ terms are of order $n$ and $\tau_0 = n^2/4$.


The identity takes a better form still. Put $u_i = k/(k_ic_i)$, so that $\tau_0/n = \sum_i u_i(T_i/n)$ with
$T_i = k_i+\dots+k_d$. Because $k_{i+1}c_{i+1} = k_ib_i$, the $u_i$ obey a one-step recursion that mentions
no $k_i$ at all: $u_1 = 1$ and $u_{i+1} = u_i c_i/b_i$, so $u_i = \prod_{j<i}(c_j/b_j)$ and
$$\frac{\tau_0}{n} = \sum_{i\le d}\frac{T_i}{n}\prod_{j<i}\frac{c_j}{b_j} \ \le \ \sum_{i\le d}\prod_{j<i}\frac{c_j}{b_j}.$$
A sufficient condition for the conjecture is therefore purely arithmetical, with no graph and no hitting
time in it: is $\sum_{i\le d}\prod_{j<i}(c_j/b_j)$ bounded over distance-regular graphs other than the
cycles? For the thirteen cubic graphs it runs between $1$ and $3.5$, and Biggs--Smith has $2.25$; for the
Hamming and Johnson families it falls to $1$; for the $n$-cycle it is exactly $2d$, because every ratio
$c_j/b_j$ there is $1/1$. What makes the products collapse is that $b_j$ and $c_j$ are rarely both one:
if $c_j = 1$ and $b_j\ge2$ the ratio is at most a half, and if $c_j\ge2$ the intersection numbers are
growing instead. So the question is how long a run of $b_j = c_j = 1$ a distance-regular graph of valency
at least three can have, the cycle being the case where every index is such a one.
With the identity the cubic case can be finished. The cubic distance-regular graphs are classified and
there are thirteen; computing $\tau_0$ for each gives a maximum of exactly $195/101$ at the Biggs--Smith
graph, which both reproduces Biggs's number and upgrades his claim from the graphs he checked to all
cubic distance-regular graphs. The classical infinite families go the other way, every one of them
tending to the trivial value: Hamming $H(16,2)$ gives $\tau_0/n = 1.080$, $H(16,4)$ gives $1.023$,
Johnson $J(50,25)$ gives $1.002$, and the Odd graph $O_{15}$, the slowest of them, gives $1.078$.

A search over *feasible* intersection arrays, which is a larger set than the graphs known to exist, turns
up nothing above Biggs--Smith either. Imposing the usual monotonicity, non-negative $a_i$, integral $k_i$,
and the standard test that the eigenvalue multiplicities $m_j = n/\sum_i k_iu_i(\theta_j)^2$ be positive
integers, and running over valencies three to six and diameters to twelve, the cubic maximum is again
Biggs--Smith, which is the only feasible cubic array of diameter seven, and the rest sit near $1.3$ to
$1.5$.

Three errors were caught by controls here, and each would have survived a weaker check. The first version
of the identity used head sums where the formula needs tail sums, and reproduced $n^2/4$ on the cycle
perfectly, because a cycle's $k_i$ are symmetric and cannot tell the two apart; the complete graph, where
it returned $1$ instead of $n-1$, exposed it. The multiplicity test first used $u_i^2/k_i$ instead of
$k_iu_i^2$ and rejected all thirteen cubic graphs. And the array enumeration initially let the valency
fall below $k$, so the cycles themselves reappeared as the extreme cases; requiring the enumeration to
contain Biggs--Smith caught that. The identity itself was then checked against a direct solve of the
hitting-time linear system on twelve graphs, which agrees exactly in every case. Memo:
`Probability_I0031_distance_regular_hitting_times_2026-09-14.md`.


### The classical companion, with the same method

The argument that settles the free constant transfers to classical Brownian motion and settles that too,
with a constant the same paper leaves at thirty-six times its true value.

Hasebe and Ueda's Theorem 1.3(1) says that if $\int e^{\varepsilon x^2}d\mu = \alpha < \infty$ then
$\mu * N(0,t)$ is unimodal for every $t \ge 36\log(2\alpha)/\varepsilon$. For $\mu$ in an interval of
length $D$ one has $\alpha \le e^{\varepsilon D^2/4}$, and letting $\varepsilon$ grow turns their bound
into $t \ge 9D^2$. The truth is $D^2/4$.

**Theorem.** For $\mu$ supported in an interval of length $D$, $\mu * N(0,t)$ is unimodal for every
$t \ge D^2/4$, and the constant is optimal: their own Example 4.1 records that
$\tfrac12(\delta_{-1}+\delta_1)$, of diameter two, is not unimodal for any $t < 1$.

The proof is shorter than the free one because the Gaussian is easier to differentiate than Biane's
description is to invert. At a local minimum of the density with a local maximum on each side, translated
to the origin, the two conditions are $\int d\,\varphi_t(d)\,d\rho = 0$ and
$\int (d^2-t)\varphi_t(d)\,d\rho \ge 0$, both linear in $\rho$, where $\rho$ is the reflected measure and
is carried by an interval of length $D$ containing the origin in its hull. The measures obeying the first
form a convex compact set whose extreme points carry at most two atoms. A single atom must sit at the
origin, where the second quantity is $-t\varphi_t(0) < 0$. For a pair at $-a$ and $b$, the first
condition fixes the weights and the second becomes
$$\theta\,(a+b)\Big(1-\frac{t}{ab}\Big) \ \ge\ 0 \iff t \le ab,$$
and $a+b \le D$ forces $ab \le D^2/4$. So above $D^2/4$ no separating local minimum exists. At $D^2/4$
itself equality pins the configuration to two equal atoms at spacing $D$, which is unimodal there. The same rigidity gives uniqueness on the classical side too: the bound $t^*(\mu)\le D_\mu^2/4$ is attained only by the symmetric two-point law.

Eight measures of diameter one were run through a direct computation of the density and a bisection on
$t$: the symmetric pair gives $0.250000$, and the others, including three- and four-atom measures and one
with nine equally spaced atoms, come in between $0.011$ and $0.208$. The bound is attained only by the
symmetric pair, exactly as the proof says.

The argument used the Gaussian only twice, for symmetry and for being integrated against, so it gives a
criterion for any kernel. Let $p$ be a symmetric density, smooth and positive with $p'<0$ on
$(0,\infty)$, and set $\psi(x) = -(\log|p'(x)|)' = -p''(x)/p'(x)$. Then $\mu * p$ is unimodal for every
$\mu$ whose support has diameter at most $D$ provided
$$\sup\{\psi(a)+\psi(b) : a,b>0,\ a+b\le D\} < 0,$$
because the extreme pair's stationarity condition gives $w_1|p'(a)| = w_2|p'(b)|$ and the curvature
condition, divided by that, is exactly $\psi(a)+\psi(b)\ge0$. As $\psi$ scales, every kernel has a
constant $c(p)$ with unimodality guaranteed once $D < c(p)s$. Two cases confirm it against known answers:
the Gaussian gives $c = 2$, that is $D<2\sigma$; and the Cauchy, where $\psi(x) = -1/x + 4x/(1+x^2)$ and
the supremum at $a=b=D/2$ vanishes when $16D^2 = 4(4+D^2)$, gives $c = 2/\sqrt3$, the classical
bimodality threshold for an equal mixture of two Cauchy densities at $\pm a$.

The criterion is an equivalence, not just a sufficient condition: if $\psi(a)+\psi(b)>0$ for some
admissible pair, the two-atom measure that pair names has a strict local minimum at the origin and is a
counterexample. Two readings follow. The Laplace kernel has $\psi\equiv1$, so $c=0$ and a two-atom measure
convolved with it is bimodal however close the atoms are, each atom contributing a cusp; yet the Laplace
density is log-concave and so is strongly unimodal in Ibragimov's sense, which shows the diameter
statement and strong unimodality constrain different families. And $c(p)>0$ holds exactly when the kernel
is smooth and strictly concave at its mode, since then $|p'(x)|\sim|p''(0)|x$ near the origin and
$\psi(x)\sim-1/x$ runs to $-\infty$.

For the symmetric stable laws with characteristic function $e^{-|u|^\alpha}$ the constant is $2.813$,
$2.596$, $2.133$, $1.577$, $1.145$, $0.682$, $0.095$ at $\alpha = 2, 1.8, 1.5, 1.2, 1, 0.8, 0.5$: it falls
steeply as the tails get heavier, a heavy-tailed kernel being too peaked to fill the valley between two
distant lumps until its scale is large. That proves the compactly supported case of the same paper's
Conjecture 5.5, since a measure of diameter $D$ has $\mu * S_t$ unimodal once
$t > (D/c(\alpha))^{\alpha}$. What the conjecture is really about is unbounded support, where the
criterion says nothing because $a+b$ is unbounded, which is why it carries a moment condition.

The free side of the stable question has an answer of the same shape, and it runs the other way. Free
convolution with a symmetric free $\alpha$-stable law of scale $s$ scales as the classical one does, so a
measure of diameter $D$ becomes unimodal once $D < c_{\mathrm{free}}(\alpha)s$, which in the natural time
parameter $t = s^\alpha$ reads $t > (D/c_{\mathrm{free}})^\alpha$: the exponent two of the semicircle case
does become $\alpha$. Probing with the symmetric pair, which is extremal at $\alpha=2$, gives
$c_{\mathrm{free}} = 1.000, 1.024, 1.078, 1.160, 1.228, 1.435$ at $\alpha = 2, 1.8, 1.4, 1.0, 0.8, 0.5$,
the first entry being the theorem and recovered numerically as $1.0015$.

Setting that beside the classical column needs the two normalisations matched, and the peak density does
it: the free family as normalised has peak $1/\pi$ at every $\alpha$, because at the origin $K(w)=0$
forces $|w|=1$, while the classical family with characteristic function $e^{-|u|^\alpha}$ has peak
$\Gamma(1+1/\alpha)/\pi$. Dividing the classical constant by $\Gamma(1+1/\alpha)$ gives $3.174$, $2.920$,
$1.677$, $1.145$, $0.602$, $0.047$ at $\alpha = 2, 1.8, 1.2, 1.0, 0.8, 0.5$ against the free column above.
The classical constant collapses by a factor near seventy as the tails thicken; the free one climbs by
forty per cent; they cross near $\alpha\approx1.05$. A heavy-tailed classical kernel is too peaked to
fill the valley between two lumps, and a heavy-tailed free kernel is better at it than the semicircle.

Both free columns were computed twice by unrelated algorithms. The two subordination functions collapse:
with $\omega_2 = 1/G + R_\lambda(G)$ the second drops out of $\omega_1+\omega_2 = z+1/G$, leaving the
single implicit equation $G = G_\mu(z - R_\lambda(G))$. For the semicircle that is $G = G_\mu(z-tG)$, and
writing $G = a - i\pi f$ turns it into $\int d\mu(y)/((u-y)^2+v^2) = 1/t$ with $v = \pi tf$, which is
Lemma 3.1 with the density cancelled out. That cancellation is exactly why the semicircle is the one
kernel with a clean level-set criterion, and why the other indices needed numerics. Solving the implicit
equation by Newton rather than iterating the maps reproduces the constants to four parts in a thousand.

The two constants sit oddly together. Free Brownian motion needs $t \ge D^2$ and classical needs
$t \ge D^2/4$, a factor of four apart in the variance added, with the same extremal measure on both
sides. Memo: `Probability_classical_brownian_unimodality_sharp_constant_2026-09-14.md`.


### How many of the open problems are still open

Intake I was built by reading each source and quoting its own numbered problems, and its note said plainly
what was not done: no search for a later resolution, so every open status was the source's own, as of its
posting date. Forty-four rows, every one whose source predates 2025, were put through that search in
three batches. Fourteen of them are no longer open: nine resolved outright and five in part. Two more came
back with a resolution announced in a preprint only weeks old, and those were recorded as claims without
changing the row's status.

Nine are resolved outright. Van der Hofstad's Open Problems 2.1 and 2.2, on the local weak limit of the
preferential attachment model with self-loops and at negative fitness, are both settled by Garavaglia,
Hazra, van der Hofstad and Ray's universality theorem for the random Pólya point tree. His Open Problem
4.3 on the critical percolation threshold of that model is settled by Hazra, van der Hofstad and Ray, with
an explicit formula. His Open Problem 4.7 on the uniformly grown random graph is settled by Jorritsma,
Maillard and Mörters in December 2025, who give the critical window a width of order $(\log n)^{-2}$.
Aldous and Fill's Open Problem 6.35, on polynomial-time computation of the expected cover time, is settled
in the standard sense by Ding, Lee and Peres's constant-factor algorithm through the Gaussian free field.
Schramm's Problem 2.10 is settled by Garban, Pete and Schramm's construction of the near-critical scaling
limit. Lyons and Peres's Question 6.21 is settled by Oh's sharp isoperimetric inequality. And Aldous's own Open Problem 27, for a
mathematically natural scale-invariant random spatial network, is settled by Kahn's theorem that the
geodesic network of an improper Poisson line process is one, in every dimension.

And their Question 5.16, on whether the first-moment method identifies the percolation critical value on
every graph, has the answer no: Kahn gave a counterexample in 2003, and the corrected edition of the book
poses his modified version instead, which Tang answered affirmatively in 2023. That one had been sitting
in the intake as an open problem from a source that itself no longer asks it.

Four more are partly resolved: first-passage percolation on preferential attachment models, where
Jorritsma and Komjáthy handle the infinite-variance regime; the annealed configuration model, where the
comparison of critical values is settled and the non-classical limit theorem is not; the speed of
convergence to SLE, where rates are known for loop-erased walk and percolation but not in general; and the
sets an SLE path hits, where the boundary case is settled and the general question is not.

That is fourteen of forty-four, and it is the number worth carrying rather than any of the individual
citations. A corpus assembled by quoting each source's own numbered problems inherits each source's
publication date, and for sources a decade old a large fraction of what they call open has since been
closed. Intake I's count of genuine open problems falls from the 106 recorded at ingest to 95: nine
withdrawn as resolved, two withdrawn earlier as questions their own sources answer in the next sentence,
and the rest either still open or open in part. Twenty-two further rows now carry the note that a
resolution search was run and found nothing, a different state from never having been checked, and three
carry it with a warning that the search was thin.

The thirty-eight rows left unsearched all come from 2025 and 2026 sources, where a resolution in the
interim is unlikely enough that the search can wait.
Where else is the count soft? Every row carries a `status_search` field, and reading it across the whole
corpus says exactly which parts were resolution-checked at ingest and which were not. Intakes D, E, F and
G are complete: all 102, 113, 140 and 15 rows carry a search, most of them dated and naming the papers
found. Intake H's 25 rows carry none, intake I's carried none until today, 65 of the 160 rows of the
September 7 intake carry one, and of the codex campaign's 495 rows 170 do. So roughly 325 rows of the
largest ledger, 95 of another, and all of intake H have never been checked against the literature, while
the four intakes that were checked are in much better shape than the sentence above would suggest on its
own.

That is worth saying plainly, because the correction cuts both ways. Intake I was the fastest-built ledger
and the only one whose own note admitted skipping the search, and it is where the inflation was found. The
campaign's stated count of sourced open problems is still an upper bound on the number actually open, but
the margin is concentrated in the ledgers that skipped the check, not spread evenly across all seven.

Ten of the codex campaign's unsearched rows were then drawn at random and put through the same check, to
see how soft that ledger is. One is resolved: the maximum height of the critical beta-splitting tree,
divided by $(\log n)^2$, converges in probability, proved by Chorbadzhiyska, Minchev and Savov in August
2026, whose paper says in its abstract that at the critical parameter this resolves an open problem of
Aldous and Janson. Four more are resolved in part: a cube is ruled out as a first-passage limit shape in
high dimension by Auffinger and Tang but not in general; critical component universality is proved for
inhomogeneous random graphs with finitely many types but not for general kernels; the minimax rate for
optimal-transport regression is sharp on the line and only bounded above in higher dimension; and the
circular Riesz gas has its thermodynamic limit constructed by Boursier without the DLR equations that the
problem asks for. Five show nothing, among them the existence of bi-infinite geodesics in planar
first-passage percolation, where the integrable last-passage analogue was settled by Basu, Hoffman and
Sly but the first-passage question itself still rests on the conditional results of Damron and Hanson and
of Alexander.

That sample says the main ledger is soft in the same way but less so: one outright resolution in ten
against nine in forty-four, with four partial. It carries a caveat the searcher raised unprompted, that
its search engines were degraded that session and it worked almost entirely through one preprint server,
so its negatives are weaker than its positives. The two numbers should be read as a floor on how many
rows would move under a proper search, not as an estimate of the total.


### Free strong unimodality, and where the Cauchy law settles it

Call $\lambda$ freely strongly unimodal if $\lambda\boxplus\nu$ is unimodal for every unimodal $\nu$.
Hasebe and Ueda's Problem 3.11 asks whether any such measure exists other than a point mass. The quoted
problem hides a restriction the intake row did not carry: their own Theorem 1.4 disposes of every
$\lambda$ of finite variance, so the question is entirely about infinite variance.

The Cauchy laws can be removed from the field, by an identity special to them. Since
$G_{C_t}(z) = 1/(z+it)$, the $R$-transform of the Cauchy law of scale $t$ is the constant $-it$, so free
convolution with it acts as $G_{\mu\boxplus C_t}(z) = G_\mu(z+it)$. But the density of $\mu * C_t$ is the
Poisson integral of $\mu$ at height $t$, whose Cauchy transform is the same function. So
$$\mu\boxplus C_t \;=\; \mu * C_t \qquad \text{for every } \mu,$$
free and classical convolution with a Cauchy law being the same operation. The Cauchy density is not
log-concave, so Ibragimov's theorem gives a unimodal $\nu$ with $\nu * C_t$ not unimodal, and by the
identity $\nu\boxplus C_t$ is that same measure. Hence no Cauchy law is freely strongly unimodal. The
first sentence there is the one Hasebe and Ueda use to prove that semicircle laws are not freely strongly
unimodal; what the identity adds is that for the Cauchy it needs no intermediary.

Ibragimov's theorem can be replaced by a witness, which the source does not exhibit. The measure
$\nu = \tfrac1{10}U_{[0,0.05]} + \tfrac9{10}U_{[0,16]}$ is nonincreasing on $[0,\infty)$ and zero to the
left, hence unimodal with mode $0$, and its Cauchy convolution is the elementary
$\sum_i (w_i/\pi a_i)[\arctan x - \arctan(x-a_i)]$, which at $t=1$ has maxima $0.0618$ at $x=0.326$ and
$0.0524$ at $x=6.407$ with a minimum of $0.05227$ between. The dip is shallow, $1.15\times10^{-4}$ below
the lower mode, but the density is a combination of arctangents evaluated directly, so it is real. Each
term of the mixture puts a bump at $a_i/2$, so two separated scales give two bumps while the mixture
itself stays nonincreasing.

Their Theorem 3.10 then extends without change of argument. Finite variance enters its proof only through
the free central limit theorem, so running it with the Cauchy as the limit gives: no non-delta measure in
the free domain of attraction of a Cauchy law is freely strongly unimodal. Since finite variance is
exactly the free domain of attraction of the semicircle, the two results together say that a
counterexample to Problem 3.11 is attracted to neither the semicircle nor the Cauchy, and more generally
to no free stable law that is itself not freely strongly unimodal. What remains is the free stable laws of
index other than one and two, where neither the identity nor their Lemma 3.1 applies, and the measures
attracted to nothing at all.

The identity was confirmed numerically as well as derived: computing free convolutions by subordination,
$C_1\boxplus C_1$ has peak density $0.159154$ against the exact $1/(2\pi)$, and the semicircle free
convolved with $C_{0.7}$ matches the Poisson integral of the semicircle at height $0.7$ to $4\times
10^{-6}$. Memo: `Probability_I0082_free_strong_unimodality_cauchy_2026-09-14.md`.

The explicit witness also reaches most of the other stable laws, which is what the reduction leaves to
settle. Computing $\lambda_\alpha\boxplus\nu$ by subordination, with $G_{\lambda_\alpha}$ obtained from
$K(w) = 1/w - i(iw)^{\alpha-1}$, the density has two interior maxima at every index tested from $0.7$ to
$1.95$: at $\alpha = 1.95, 1.6, 1.2, 1.0, 0.8, 0.7$ they sit at $(-0.12, 6.36)$, $(0.01, 6.36)$,
$(0.13, 6.36)$, $(0.39, 6.36)$, $(0.77, 6.36)$ and $(1.15, 6.49)$. So none of those laws is freely
strongly unimodal, and by the corollary neither is anything attracted to them. At $\alpha=1$ that is a
theorem through the identity; elsewhere it is numerical, warranted by the same computation reproducing
the exact Cauchy convolution at $\alpha=1$, peak $0.061765$ against $0.0618096$. Below about $0.65$ the
witness stops working, giving one maximum robustly across three grids, and three other mixtures fail
there too: a heavier-tailed kernel smooths the two bumps together, and that range stays open.

The same subordination machinery was turned on their Conjecture 3.5, that the free convolution of two
symmetric unimodal measures is unimodal. Its classical analogue is a theorem of Wintner, and the classical
proof is two lines: a symmetric unimodal law is a mixture of uniform laws on symmetric intervals by
Khinchin, ordinary convolution is linear in each argument, and the convolution of two such uniforms is a
trapezoid. Free convolution is not linear, which is what makes the free version a conjecture, but
Khinchin's representation still says mixtures of uniforms are the family to test. Four hundred and nine
pairs were tested, nine chosen by hand to be awkward (widely separated scales, spikes of width $0.01$
carrying weight $0.95$, three-scale mixtures) and four hundred drawn at random with log-uniform scales.
Every one gave a unimodal free convolution.


### Sinclair's inequality, and what a diameter version would need

Open Problem 4.49 of Aldous and Fill has two halves. Sinclair's inequality bounds a congestion
quantity over families of flows,

$$\psi(f) \;=\; \max_{(i,j)} \; \frac{\sum_a \pi_a\,|f^{(a)}_{ij}|}{\pi_i p_{ij}},$$

in which $f^{(a)}$ is a unit flow from $a$ to $\pi$, by $K\tau_2\log n$. The book asks for a simple
proof, and asks whether $\log n$ can be replaced by the diameter.

The infimum over $f$ is a linear program, which is what made this tractable, but the useful form is its
dual. Shipping one unit from each $a$ to $\pi$, weighting $a$ by $\pi_a$, is the multicommodity flow
problem with demand $\pi_a\pi_b$ between $a$ and $b$, and $\psi$ is its congestion against the
capacities $\pi_ip_{ij}$. So by the standard duality between minimum congestion and fractional sparsest
cut,

$$\inf_f \psi(f) \;=\; \max\Big\{ \sum_{a,b} \pi_a \pi_b\, d(a,b) \;:\; d \text{ a metric on } V,\;
\sum_{e} \pi_i p_{ij}\, d(e) = 1 \Big\},$$

and the optimal $d$ may be taken to be the shortest-path metric generated by its own values on the
edges. Two feasible metrics are worth naming: twice the graph metric, whose value is twice the mean
$\pi$-weighted distance, and the cut metric of a set $A$, whose value is
$2\pi(A)\pi(A^c)/Q(A,A^c)$. Write $B(G)$ for the best cut metric and call
$\inf\psi/B(G) \ge 1$ the flow–cut gap of the instance.

Three elementary facts then do most of the work. First, a connected graph that is not complete has
$\tau_2 \ge 1$: for a non-adjacent pair $u,v$ the mean-zero function $\pi_v\mathbf 1_u - \pi_u\mathbf 1_v$
makes the quadratic form $\langle f,Pf\rangle_\pi$ vanish, because the only pairs contributing lie
inside $\{u,v\}$ and all three of $p_{uu}$, $p_{vv}$, $p_{uv}$ are zero; so $\lambda_2 \ge 0$. The
complete graph has $\tau_2 = (n-1)/n < 1$. So the complete graphs are exactly the graphs of relaxation
time below one, and they are also exactly the graphs of diameter one. Second, the Poincaré inequality
applied to $\mathbf 1_A/\pi(A) - \mathbf 1_{A^c}/\pi(A^c)$ gives $\pi(A)\pi(A^c)/Q(A,A^c) \le \tau_2$
for every $A$, so $B(G) \le 2\tau_2$. Third, combining these,

$$\frac{\inf_f\psi(f)}{\tau_2\,\Delta} \;\le\; \frac{2\,\mathrm{gap}(G)}{\Delta(G)}.$$

That is the reduction. The diameter version holds, with constant $2$, for any graph whose flow–cut gap
is at most its diameter; a counterexample has to be a graph whose flow–cut gap exceeds its diameter.
The first half of the problem falls out of the same picture: the Leighton–Rao theorem, in the
product-demand form of Linial, London and Rabinovich, bounds the gap by $O(\log n)$, and the cut bound
is elementary, so Sinclair's inequality follows in two lines and the $\log n$ is identified as the
$\ell_1$ distortion of the optimal dual metric and nothing else.

Two classes come out completely. If the uniform metric happens to be optimal, the ratio is
$2\bar d/(\tau_2\Delta) \le 2\bar d/\Delta$, and the mean distance is strictly below the diameter
because $d(a,a) = 0$ carries positive weight, so the ratio is strictly below $2$ for every non-complete
graph. If instead the graph has no $K_4$ minor, every shortest-path metric on it lies in the cut cone,
so the dual optimum is an average of cut values and $\inf\psi \le 2\tau_2$ with no diameter factor at
all. That second statement rests on the classical equality of the metric cone and the cut cone for
series-parallel graphs, which I have cited from memory rather than checked; the conclusion was verified
by exact computation on fifteen such graphs, where the program returned $\inf\psi = B(G)$ every time.

The computation was run three ways to guard it. The primal was written twice, densely and sparsely,
agreeing to zero relative error; the dual was written separately as a program in the pair variables
with the triangle inequalities, and agrees with the primal to $2\times10^{-15}$ on thirteen graphs.
Complete graphs return the hand value $2(n-1)/n$.

Over all $992$ connected graphs on four to seven vertices the optimal dual metric is a single cut in
$887$ cases, the uniform metric in $40$, and neither in the remaining $85$; even there the largest gap
is $1.219$. The ratio never exceeds $2$, and $2$ is attained by the complete graphs and by nothing
else, the largest value among non-complete graphs being $1.208$. Steepest-ascent search over single
edge additions and deletions, started both from random graphs and from complete graphs with a few edges
cut, settles near $1$ at eight, nine and ten vertices.

The family that comes closest is the polarity graph of the projective plane $PG(2,q)$: its $q^2+q+1$
points, joined when their dot product vanishes, with the absolute points losing their loops. These have
diameter two, adjacency eigenvalues $q$ and $\pm\sqrt q$, so $\lambda_2 = \sqrt q/(q+1)$ exactly, and
mean distance tending to two. The ratio reads $0.849$, $0.921$, $1.106$ and $1.225$ at
$q = 2,3,5,7$, and at least $1.372$ at $q = 11$ where the program is too large to finish, and it
approaches $2$ from below like $2 - 2q^{-1/2}$. Their flow–cut gap is negligible: $1.0024$ at $q = 7$.
So the bound is approached by sparse graphs of diameter two and attained only in the degenerate case of
diameter one.

What is not proved is that the gap never exceeds the diameter. The difficulty is visible: the dual
metric is built from arbitrary edge weights, so the graph's diameter constrains nothing about it, and
the worst known instances for the flow–cut gap are bounded-degree expanders, where gap and diameter are
both of order $\log n$. The conjecture is tight there up to constants, which rules out any argument
that discards the diameter.

### New open problems

The campaign's mandate was a thousand problems. The session adds the following, all arising directly from the
proofs above, each stated so that a yes or no is a theorem.

1. **The intermediate regime when the weight of one vanishes.** With $a, b$ as in Theorem 2 of F0056 and $m \not\equiv 0 \pmod a$,
   Theorem 18.7 fails when $n\pi_b \to 0$ and the characteristic-function argument proves it when $n\pi_b / \log m
   \to \infty$. What happens when $n\pi_b$ stays between order one and order $\log m$? Is there a sharp threshold,
   and is it $n\pi_b \to \infty$?
2. **The law of the split.** Along $m = 2^{i+1}$ in Theorem A, does $(Y_{(1)}, Y_{(2)})$ concentrate on $(2^i + 1,
   2^i - 1)$? Along the cliffs in Theorem B, does $(Y_{(1)} - K/2, Y_{(2)} - K/2)/\sqrt n$ converge to a Gaussian
   law, as the pair count in the proof suggests?
3. **Monotone weights with a sparser condition.** Theorem B uses cliffs of fixed relative depth $e^{10}$ and
   double-height steps. Is there a nonincreasing weight sequence that is also log-convex eventually, or that
   satisfies $w_k \sim ck^{-\beta}$ along a subsequence of density one, for which (18.106)-(18.107) fail? If
   $\log w_k$ is eventually convex in $k$, condensation to one box should follow; the question is whether any
   weaker second-difference condition suffices.
4. **Regularity that saves Problem 18.30.** Both parts of Theorem 18.7(ii)-(iii) fail at $\lambda = \nu$,
   $\sigma^2 = \infty$ for irregular laws, and hold for regularly varying tails (Example 18.27). What is the
   weakest tail condition under which the mean of $S_n$ stays inside its bulk, so that the ratio
   $\mathbb{P}(S_{n-1} = m - k)/\mathbb{P}(S_n = m)$ is bounded above and below uniformly for $k$ up to the
   relevant level? A one-sided Potter bound on $\mathbb{P}(\xi \ge 2x)/\mathbb{P}(\xi \ge x)$ is the natural
   candidate; the constructions above violate any such bound at every stage.
5. **Mean versus centre for sums of i.i.d. lattice variables.** The F0058 construction shows that $\mathbb{P}(S_n =
   \lfloor n\mathbb{E}\xi\rfloor)$ can be smaller than $\sup_j \mathbb{P}(S_n = j)$ by a factor tending to infinity
   for a nonnegative integer law with finite mean and span one. Characterise the laws for which the ratio stays
   bounded along the full sequence $n \to \infty$. Regular variation of the tail is sufficient; is a one-sided
   Potter-type bound on the tail ratio $\mathbb{P}(\xi \ge 2x)/\mathbb{P}(\xi \ge x)$ sufficient?
6. **Problem 18.40 for full-support sequences.** Janson's Example 18.38 gives $Y_{(1)}/n \to 0$ along a
   subsequence using a sparse support. Theorem A's construction has full support and ratios tending to infinity
   and produces two giant boxes. Can a full-support sequence with $w_{k+1}/w_k \to \infty$ produce $Y_{(1)}/n \to
   0$ along a subsequence, that is an unbounded number of boxes of size $o(n)$ sharing the excess?
7. **The sharp count for Vu's Conjecture 8.4** (from lane P2). The lower bound $(3/2 - o(1))n^4 4^{-n}$ for a
   repeated eigenvalue of the symmetric sign matrix comes from two disjoint support-two eigenvectors. Is
   $s_n = (c + o(1))n^4 4^{-n}$ with $c = 3/2$, or do other local structures contribute at the same order?
8. **Scalar monotonicity below cluster weight one** (from lane P1). For the random-cluster measure on a fixed finite graph
   with $0 < q < 1$, is $\mu_{p,q}(A)$ nondecreasing in $p$ for every increasing event $A$? The vector version is
   false; the scalar version survived an exact search over all increasing events on graphs with at most six
   vertices. A fixed small graph over the whole $(p, q)$ range is a real-algebraic decision problem and would be
   a first theorem either way.
9. **Normality of the outdegree counts and local flatness of the tail.** For $\nu < 1$, is asymptotic normality of
   $(N_d - n\pi_d)/\sqrt n$ with variance $\pi_d(1 - \pi_d)$ equivalent to $\pi_{k+j}/\pi_k \to 1$ uniformly for
   $|j| \le C\sqrt k$ along $k \approx (1 - \nu)n$? The direction from flatness to normality should follow the
   one-big-jump argument of Armendáriz and Loulakis; the converse is what F0064 suggests.
10. **A critical infinite-variance law outside every stable domain with normal outdegree counts.** Theorem B of
   F0064 needs a very lacunary law. Is there a law with $\nu = 1$, $\sigma^2 = \infty$, not in any stable domain of
   attraction, for which $N_d$ is nevertheless asymptotically normal for every $d$? A slowly varying but not
   regularly varying tail is the natural test.
11. **The outdegree counts at the endpoint.** At $\nu = 0$, with $\rho = 0$, there is no tilted law and $N_0 = n -
   o(n)$. What are the orders of magnitude and the fluctuations of $N_d$ for fixed $d \ge 1$? For $w_k = k!$
   (Example 18.35) the survey gives the size of the largest box; the counts of the small boxes are not addressed.
12. **Full-sequence failure with a unique condensate.** The constructions of F0058 and F0064 work along a
   subsequence and say nothing about $n$ between stages. Is there a law with $\nu < 1$ whose condensate is unique
   w.h.p. for every $n$ and for which $(N_1 - n\pi_1)/\sqrt n$ has no limit along the full sequence?
13. **The constant in the layer distribution.** Is there a closed form for $\mathbb{E}[e^{-M^*}]$, the exponential
   moment of the limiting minimum of the Poisson-weighted infinite tree, which by H0019 is the constant in
   $\ell_k \sim (1 - e^{-1/e})\mathbb{E}[e^{-M^*}]e^{-k/e}k^{-3/(2e)}$? Through Aïdékon's description of the limit
   it is a fractional moment of the derivative martingale of that walk. The numerics give $1.42$.
14. **The next correction to a branching random walk front with exponential steps.** The same numerics show
   $\bar\ell_k e^{k/e}k^{3/(2e)}$ approaching its limit at rate $(\log k)/\sqrt k$ with coefficient about $0.39$.
   Is that the true order, and what is the coefficient? The analogous refinement is classical for branching
   Brownian motion and I did not find it for this walk.
15. **The largest rank in a random recursive tree.** The rank of a vertex is its distance to the nearest leaf. The
   same paper proves $r_k = \exp[-2k\log k + 2(1 - \log 2)k + O(\log k)]$ for the rank distribution and conjectures
   that the largest rank is $\tfrac12\log n/\log\log n$. The first moment predicts exactly that; what is missing is
   a second-moment argument, and high-rank vertices are strongly dependent because they sit far from every leaf.
16. **Layers of other increasing trees.** The dictionary above turns leaf-stripping into a branching random walk
   with exponential steps. Preferential attachment trees give a different displacement law with a known height
   (Pain and Sénizergues). Does the layer distribution of the plane-oriented recursive tree obey
   $\bar\ell_k = \exp[-\gamma k - \tfrac{3}{2\lambda^*}\log k - O(1)]$ with $\gamma$ and $\lambda^*$ read off the
   same way?
17. **The exact confinement that resists a Lévy drift.** From H0013, the potential charges $(2\delta-2)\log x$ per
   unit of well depth and an $\alpha$-stable drift supplies depth $x^{1/\alpha}$, so the mechanism should die exactly
   for potentials growing like $\exp(x^{1/\alpha})$. Is the semigroup of $\tfrac12(\Delta - (g+V)'\partial)$ compact
   when $\log g'(x)/x^{1/\alpha} \to \infty$ and noncompact when that ratio tends to zero?
18. **Wells that are slabs.** In $\mathbb{R}^d$ the field of that paper is $W(x) = \sum_k V(x_k)$, so a jump of $V$
   creates a slab-shaped well rather than a box. Does a slab of depth $m$ and thickness $x^{1-\delta}$ still force
   $\lambda_{\mathrm{ess}} = 0$, or does the transverse direction cost enough to restore compactness for large
   $\delta$?
19. **The two-sided firework criterion.** Sites of $\mathbb{Z}$ carry independent reaches, an activated site at
   $x$ activates $[x - L_x, x + R_x]$, and the tails are $\mathbb{P}(R\ge n)\sim c_R/n$,
   $\mathbb{P}(L\ge n)\sim c_L/n$. Prove that the process started at the origin dies out almost surely when
   $\max(c_R,c_L) < 1$. Survival above that is a coupling: delete one side's reaches and the sites that side
   contributes, and what is left is exactly a one-sided firework, whose threshold is classical. The obstruction in
   the other direction is that the two ends do not decouple, since a site at one end whose reach crosses the whole
   interval revives the other end, often enough that an excursion reaching size $n$ expects of order $\log n$
   of them. This is what H0024's
   critical line needs, and I did not find it written down.
20. **The two-sided decay exponent.** For the symmetric two-sided firework the simulations of H0024 give
   $\mathbb{P}(\text{size}\ge n)\asymp n^{-(1-c)^2}$ against $n^{-(1-c)}$ one-sided, the second being the Cramer
   root of $\Gamma(\kappa+c)\Gamma(1-\kappa)/\Gamma(c) = 1$. Is the square exact, which equation is it the root of,
   and what replaces it when the two constants differ? A derivation has to price the revivals of item 19, since
   those are what separate the two exponents.
21. **Is the firework threshold universal in the joint law?** For a frog, $D^\to$ and $D^\leftarrow$ come from one
   walk and are strongly dependent, though their joint tail is negligible against the marginals. Is the critical
   constant the same for every joint law with given marginal tails, and does the survival probability depend on
   the joint law only through them?
22. **The quenched Bramson correction on a random tree.** From H0010: for cascades on a unimodular
   Galton--Watson tree, do the quenched and annealed logarithmic corrections to the front differ, and is the
   coefficient still $3/2$? The speeds already differ off boundary-homogeneous trees.
23. **The regularity that makes the box counts normal.** From I0020: the counts $N_d$ of an allocation are
   asymptotically normal exactly when the conditioning sits at the mean of a finite-variance tilted law, and
   otherwise only under a regularity condition on the tail. State and prove the necessary and sufficient
   condition. The candidate is local flatness at the scale the conditioning must supply, $\pi_{k+j}/\pi_k\to1$
   uniformly for $|j|\le C\sqrt k$ along $k \approx (\lambda-\nu)n$ when $\lambda>\nu$.
24. **Records of a rate function attached to any law of radius one.** From F0059: let $\pi$ be a probability
   law on the nonnegative integers with radius of convergence one and finite mean, and put $\Lambda(a) =
   [\log\pi_a + \log a]/a$, which has $\limsup\Lambda = 0$ and hence infinitely many records. Must infinitely
   many of those records have a gap $\Lambda(a_j) - \max_{a \le \varepsilon a_j}\Lambda(a)$ exceeding
   $a_j^{-1/2}$, for some fixed $\varepsilon > 0$? A yes turns Janson's Conjecture 18.39 into a theorem; a no
   is a candidate counterexample to it.
25. **The oscillation of the largest box at $\nu = 0$.** From F0060: there $\limsup Y_{(1)}/n = \lambda$ while
   Example 18.38 gives $\liminf = 0$. Which pairs of limits are achievable, and is the lower one determined by
   the gaps in the record sequence of the rate?
26. **The sharp constant in the flow inequality.** From I0026: is $\inf_f\psi(f)\le2\tau_2\Delta$ for every
   finite connected graph, with equality only for the complete graphs? That would answer Aldous and Fill's
   Open Problem 4.49(ii) in the strongest form, and the extremal case is where a proof should be tested.
27. **How far balanced routing fails.** With $B(G) = \inf_f\psi(f)/(2\times\text{mean distance})$, the
   factor by which balanced routing fails, the computation has $B$ close to one on every family tried except
   the barbell. Is $B$ the right object for a proof of 4.49(ii), and what bounds it?
28. **Fractional moments of the level widths with infinite variance.** For $\nu = 1$, $\sigma^2 = \infty$, $0 < r < 1$
   and $\mathbb{E}\xi^{r+1} < \infty$, is $\ell_k(T_n)^r$ uniformly integrable? For $k = 1$ this is the question
   whether $\sum_d d^{r+1}\pi_d\,\mathbb{P}(S_{n-1} = n-1-d)/\mathbb{P}(S_n = n-1)$ is bounded in $n$; the lacunary
   laws of F0058 are the natural test, and the size-biasing heuristic says they pass.

29. **Between classical and free.** The classical constant is now known (see the section below): for
   $\mu$ in an interval of length $D$, $\mu * N(0,t)$ is unimodal exactly from $t = D^2/4$ in the worst
   case, against $t = D^2$ on the free side. For the $q$-deformed convolutions interpolating between the
   two, is there a constant $C(q)$ of the same kind, running from $1/4$ at $q=1$ to $1$ at $q=0$, and is
   it monotone?
30. **The threshold as a functional.** Write $t^*(\mu)$ for the least time from which
   $\mu \boxplus S(0,t)$ is unimodal. The theorem gives $t^*(\mu) \le D_\mu^2$ with equality only for the
   symmetric Bernoulli. Is $t^*$ weakly continuous, and is the symmetric Bernoulli its only maximiser
   among measures of a given diameter?
31. **Free stable convolutions.** Replace the semicircle by a free stable law of index
   $\alpha \in (0,2)$. Is there a sharp constant of the same shape, and does the exponent $2$ on the
   diameter become $\alpha$?
32. **Variance in place of diameter.** The diameter is useless for unbounded support, the variance is not.
   Is there a constant $C'$ with $\mu \boxplus S(0,t)$ unimodal for every $t \ge C'\operatorname{Var}(\mu)$
   and every $\mu$ of finite variance? Some condition is needed: that paper's Section 3.2 produces measures
   that never become unimodal.

33. **The exact discrepancy of $H_9$.** The covering radius of $\mathrm{RM}(1,9)$ is known only to lie
   between $242$ and $244$, so $\operatorname{disc}(H_9)$ is one of $24$, $26$, $28$ and the value is
   open. This is the smallest Sylvester matrix whose discrepancy nobody knows.
34. **Does the odd-$k$ ratio stay away from one?** Is
   $\liminf_{k\ \mathrm{odd}} \operatorname{disc}(H_k)/\sqrt{2^k} > 1$? That is what the Sylvester family
   would have to supply to settle the list's Conjecture 12, and it is the question whether the maximum
   nonlinearity on $k$ odd variables is $2^{k-1} - c\,2^{k/2-1}(1+o(1))$ with $c$ bounded away from zero.
   The constructions give $c \approx 1.19$ at $k = 15$; the upper bounds allow $c \to 0$.
35. **A family with ratio above $\sqrt2$.** Every ratio known over all $\pm1$ matrices is at most
   $\sqrt2$, attained at the two-by-two Hadamard matrix. Is $\sqrt2$ the supremum asked for in that
   list's Open Problem 11?
36. **Other Hadamard families.** For a Paley Hadamard matrix of order $n$, is the discrepancy closer to
   $\sqrt n$ than the Sylvester value, and is there a family whose ratio tends to a limit above one?

37. **Is the discrepancy supremum approached or attained?** Through the covering identification the
   question is the behaviour of $n - 2\rho(n,2n)$, where $\rho(n,M)$ is the least covering radius of a
   complement-closed binary code of length $n$ with $M$ codewords. Does $(n-2\rho(n,2n))/\sqrt n$
   converge, and to what?
38. **How ragged is the table?** The values $4,3,4,5,4,5$ at $n=6,\dots,11$ do not increase. Is the
   maximum at $n+1$ at least the maximum at $n$ minus one, and is the sequence eventually
   non-decreasing?
39. **When is an optimal covering code complement-closed?** The complement-closed minimum lies between
   $K(n,R)$ and $2K(n,R)$. At $n=6$, $R=1$ the optimum has exactly $12=2n$ codewords and can be taken
   complement-closed. For which $n$ and $R$ does that happen?
40. **Structure behind the good sizes.** At $n=2$ the extremal matrix is Hadamard, at $n=4$ and $n=8$ the
   Hadamard matrix is not extremal, and $n=6$ and $n=9$ are the good cases. Is there a construction
   behind them, and does it continue?

41. **The sharp constant for distance-regular hitting times.** Is $\tau_0 \le 2(n-1)$ for every
   distance-regular graph other than a cycle, with the Biggs--Smith graph extremal? Nothing computed
   above exceeds $1.94(n-1)$.
42. **Where the second term lives.** With $\tau_0 = (n-1) + k\sum_{i\ge2}(k_i+\dots+k_d)/(k_ic_i)$, the
   conjecture says the sum is $O(n/k)$, and the cycle fails because $k_ic_i = k$ for every $i$. For
   valency at least three, is the number of indices $i$ with $k_ic_i = O(k)$ and
   $k_i+\dots+k_d = \Omega(n)$ bounded?
43. **Uniformity in the valency.** For each $k\ge3$ there are finitely many distance-regular graphs, by
   the theorem of Bang, Dubickas, Koolen and Moulton settling the Bannai--Ito conjecture, so
   $\sup \tau_0/n$ is finite at each fixed valency. Does that supremum stay bounded as $k\to\infty$?
   That, rather than any one family, is what the conjecture needs.
44. **The relaxation-time half.** Aldous and Fill ask in the same place whether $\tau_2 = O(\log n)$ over
   distance-regular graphs. The same reduction makes $\tau_2$ the relaxation time of a chain on $d+1$
   states; does that make the question tractable in the same way?

45. **Variance in place of diameter, classically.** The proof above uses only that an extreme pair of
   atoms lies in an interval of length $D$. For unbounded support Hasebe and Ueda show some condition is
   needed. Is there a constant $C'$ with $\mu * N(0,t)$ unimodal for every $t \ge C'\operatorname{Var}(\mu)$
   under a condition weaker than their Gaussian moment, and what is the sharp $C'$?
46. **Unimodality in higher dimensions.** In $\mathbb{R}^d$, reading unimodality as quasi-concavity of the
   density, is $\mu * N(0,tI)$ quasi-concave for $t \ge c_dD^2$, and how does $c_d$ grow?
47. **How the dip closes.** Just below $D^2/4$ the extremal density has two modes with a shallow dip
   between them. How fast does the dip vanish as $t$ rises to $D^2/4$, and is the exponent the same for
   every measure attaining the bound?

48. **Free stable laws and strong unimodality.** Is a free stable law of index $\alpha\in(0,2)$,
   $\alpha\ne1$, freely strongly unimodal? A negative answer for every such $\alpha$ would leave Hasebe
   and Ueda's Problem 3.11 open only for measures lying in no domain of attraction.
49. **When do the two convolutions agree?** The Cauchy family satisfies $\mu\boxplus C_t = \mu * C_t$ for
   every $\mu$. Is it the only family with that property, and can the pairs with
   $\mu\boxplus\nu = \mu*\nu$ be characterised?
50. **A free Ibragimov theorem.** Classically, strong unimodality is exactly log-concavity. Is there a
   property of $\lambda$ equivalent to "$\lambda\boxplus\nu$ is unimodal for every unimodal $\nu$", even
   if it turns out to single out the point masses?


51. **The flow–cut gap against the diameter.** Is the flow–cut gap of the instance with demand
   $\pi\otimes\pi$ and capacity $\pi_ip_{ij}$ at most the diameter of the graph? This implies Aldous
   and Fill's Open Problem 4.49(ii) with constant $2$, and by the expander examples it is tight up to
   constants.
52. **The value of the congestion against the relaxation time.** Is
   $\sup_G \inf_f\psi(f)/\tau_2$ over graphs of diameter $\Delta$ equal to $2\Delta$? At $\Delta = 1$
   it is $2$ and attained by the complete graphs; at $\Delta = 2$ the polarity graphs of projective
   planes drive it toward $4$, while the largest value found by exact computation is $2.6$, at
   $K_{5,5}$.
53. **Which graphs have the uniform dual.** For which graphs is twice the graph metric optimal in the
   dual above? It is enough for the ratio to be strictly below $2$. Vertex-transitivity does not
   suffice: the circulant $C_{12}(1,2,3)$ and the pentagonal prism both fail it, and in both the cut
   metric is optimal instead. Is every graph covered by one of the two?
54. **The constant in Sinclair's inequality.** Is $\inf_f\psi(f) \le 2\tau_2\log_2 n$, with the
   complete graph on two vertices extremal? The values computed here are far below it.
55. **The envelope near the complete graph.** The polarity graphs approach the value $2$ at rate
   $q^{-1/2}$, that is $n^{-1/4}$. Is there a family of non-complete graphs approaching it faster, and
   is $2 - cn^{-1/4}$ the true envelope?