# Aldous and Fill, Open Problem 4.48: the variation threshold can exceed Kemeny's constant, and the relaxation time never exceeds the stopping-rule mixing time

14 September 2026. Ledger row P0243 (Codex campaign). Source: Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 4, Notes (Section 4.7), Open Problem 4.48, PDF page 154 of the 2014 recompilation.

## The question

Chapter 4 studies five parameters of a finite irreducible reversible continuous-time chain with stationary law $\pi$: the maximal mean commute time $\tau^*$, the average hitting time (Kemeny's constant) $\tau_0 = \sum_{i,j}\pi_i\pi_j\,\mathbb{E}_iT_j$, the variation threshold $\tau_1 = \min\{t : \bar d(t) \le e^{-1}\}$ with $\bar d(t) = \max_{i,j}\|\mathbb{P}_i(X_t \in \cdot) - \mathbb{P}_j(X_t \in \cdot)\|$, the relaxation time $\tau_2 = 1/\lambda_2$, and $\tau_c$. Theorem 4.6 there shows $\tau_1$ is equivalent, up to universal constants, to a family $\tau_1^{(1)}, \dots, \tau_1^{(5)}$; the second member is the stopping-rule mixing time
$$\tau_1^{(2)} = \max_i \min_U \mathbb{E}_i U, \qquad U \text{ a (randomized) stopping time with } \mathbb{P}_i(X_U \in \cdot) = \pi(\cdot).$$
The chapter's summary inequalities are $\tfrac12\tau^* \ge \tau_0 \ge \tau_2 \ge \tau_c$ and $66\,\tau_0 \ge \tau_1 \ge \tau_2$, and the notes say the choice of $\tau_1$ was made so that the constant in $\tau_2 \le \tau_1$ is one. Then:

> **Open Problem 4.48.** (a) Is $\tau_1 \le \tau_0$? (b) Is $\tau_2 \le \tau_1^{(2)}$?

Answers: (a) no; (b) yes.

## (a) A three-state birth-and-death chain with $\tau_1 > \tau_0$

For $k \ge 1$ and $\varepsilon > 0$ let $P_k(\varepsilon)$ be the continuous-time birth-and-death chain on $\{0, 1, \dots, k\}$ with rate $1$ from $i$ to $i - 1$ ($i \ge 1$) and rate $\varepsilon$ from $i$ to $i + 1$ ($i < k$). It is reversible, with $\pi_i \propto \varepsilon^i$.

**Proposition 1.** For $k = 2$ and every $\varepsilon > 0$, $\tau_0 = \dfrac{2(1 + \varepsilon)}{1 + \varepsilon + \varepsilon^2} < 2$, while $\tau_1 \to t_2 = 2.14619\ldots$ as $\varepsilon \to 0$, where $t_2$ solves $e^{-t}(1 + t) = e^{-1}$. In particular $\tau_1 > \tau_0$ for all small $\varepsilon$; at $\varepsilon = 1/10$, $\tau_0 = 220/111 = 1.981982$ and $\tau_1 = 2.010072$.

*Proof.* Kemeny's constant of a continuous-time chain is $\sum_{\lambda > 0} 1/\lambda$ over the nonzero eigenvalues of $-Q$ (Aldous and Fill, Chapter 3). For $k = 2$, $-Q$ is $3 \times 3$ with trace $2 + 2\varepsilon$ and sum of principal $2\times 2$ minors $\varepsilon^2 + \varepsilon + 1$, so the two nonzero eigenvalues have sum $2 + 2\varepsilon$ and product $1 + \varepsilon + \varepsilon^2$, and $\tau_0 = (2 + 2\varepsilon)/(1 + \varepsilon + \varepsilon^2)$, which is below $2$ because $\varepsilon^2 > 0$. For $\tau_1$: as $\varepsilon \to 0$ the chain from $0$ stays at $0$ on any bounded time interval with probability tending to one, and the chain from $2$ descends through $1$ to $0$ after the sum of two independent unit exponentials, so uniformly on compact $t$-intervals
$$\|\mathbb{P}_2(X_t \in \cdot) - \mathbb{P}_0(X_t \in \cdot)\| \to \mathbb{P}(\Gamma(2,1) > t) = e^{-t}(1 + t),$$
and the other two pairs converge to smaller functions ($e^{-t}$ for the pair $(1,0)$, and $e^{-t}\,t$ for $(2,1)$). So $\bar d(t) \to e^{-t}(1 + t)$ uniformly on compacts; the limit is strictly decreasing, hence $\tau_1(\varepsilon) \to t_2$, the root of $e^{-t}(1+t) = e^{-1}$, which is $2.146193\ldots > 2$. $\square$

The same argument for general $k$ gives $\tau_0 \to k$ (the nonzero eigenvalues all tend to $1$) and $\tau_1 \to t_k$, the root of $e^{-t}\sum_{j<k}t^j/j! = e^{-1}$, i.e. the time at which a Gamma$(k,1)$ variable exceeds $t$ with probability $e^{-1}$. Since a Gamma$(k,1)$ variable exceeds its mean $k$ with probability more than $e^{-1}$ for every $k \ge 2$ (it is $e^{-2}\cdot 3 = 0.406$ at $k = 2$ and increases toward $1/2$), $t_k > k$ for all $k \ge 2$, with $t_1 = 1$: the two-state chain is the equality case of $\tau_1 \le \tau_0$, and every longer path breaks it.

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $t_k/k$ | 1 | 1.07310 | 1.08608 | 1.08800 | 1.08682 | 1.08467 | 1.07983 | 1.07532 |

So the ratio $\tau_1/\tau_0$ on this family reaches $1.0880$ at $k = 4$ and then returns to one, as it must, since $t_k = k + O(\sqrt k)$.

*Verification.* Thirty-digit computation of $\tau_0$ (trace of the fundamental matrix $Z = (\Pi - Q)^{-1} - \Pi$) and $\tau_1$ (bisection on $\bar d(t)$ computed from the matrix exponential), script `p0243_verify.py`:

| $k$ | $\varepsilon$ | $\tau_0$ | $\tau_1$ | $\tau_1/\tau_0$ |
| --- | --- | --- | --- | --- |
| 2 | 0.1 | 1.981981982 | 2.010071506 | 1.01417 |
| 2 | 0.001 | 1.999998002 | 2.144887095 | 1.07244 |
| 3 | 0.001 | 3.000998997 | 3.257319677 | 1.08541 |
| 4 | 0.001 | 4.001999998 | 4.351736415 | 1.08739 |
| 4 | $10^{-5}$ | 4.00002 | 4.351990156 | 1.08799 |
| 6 | 0.001 | 6.004002 | 6.509424619 | 1.08418 |

The example was found by a random search over reversible chains on three to six states (20,000 chains, `p0243_search.py`); its best chain was a three-state path with a heavy holding weight at one end, ratio $1.0657$, which is $P_2(\varepsilon)$ in disguise. A local optimisation over chains with up to six states (`p0243_opt.py`) did not improve on $1.088$ within its budget; whether $\sup \tau_1/\tau_0$ over all reversible chains is $t_4/4$ or larger is left open below. The source's Theorem 4.6 gives the upper bound $66$.

## (b) The relaxation time is at most the stopping-rule mixing time

**Proposition 2.** For every finite irreducible reversible continuous-time chain, $\tau_2 \le \tau_1^{(2)}$. More precisely, let $u$ be an eigenfunction of $-Q$ for the eigenvalue $\lambda_2$ (so $Qu = -\lambda_2 u$, $\sum_i \pi_i u_i = 0$), and let $i^*$ be a state at which $|u|$ is maximal. Then every stopping time $U$ (randomized or not) with $\mathbb{E}_{i^*}U < \infty$ and $\mathbb{P}_{i^*}(X_U \in \cdot) = \pi$ satisfies $\mathbb{E}_{i^*}U \ge 1/\lambda_2 = \tau_2$.

*Proof.* Fix $i$ and such a $U$, and let $x_j = \mathbb{E}_i\int_0^U \mathbf 1\{X_t = j\}\,dt$ be the mean occupation measure, so $\sum_j x_j = \mathbb{E}_iU < \infty$. For any function $h$ on the state space, $h(X_t) - \int_0^t (Qh)(X_s)\,ds$ is a martingale with increments bounded by $\|h\|_\infty + t\|Qh\|_\infty$, so optional stopping at $U$ is justified by $\mathbb{E}_iU < \infty$ (dominated convergence along $t \wedge U$), and
$$\mathbb{E}_i h(X_U) - h(i) = \sum_j x_j\,(Qh)(j).$$
Take $h = u$. The left side is $\sum_j \pi_j u_j - u_i = -u_i$, the right side is $-\lambda_2\sum_j x_j u_j$. Hence
$$u_i = \lambda_2 \sum_j x_j u_j, \qquad |u_i| \le \lambda_2\,\|u\|_\infty \sum_j x_j = \lambda_2\,\|u\|_\infty\,\mathbb{E}_iU .$$
At $i = i^*$ this reads $\mathbb{E}_{i^*}U \ge 1/\lambda_2$. Since $\tau_1^{(2)} \ge \min_U \mathbb{E}_{i^*}U$, the claim follows. $\square$

The argument uses only that $\lambda_2$ is a real eigenvalue with a real eigenfunction, so it applies to any finite chain with a real eigenvalue $\lambda$ of $-Q$: every stopping rule reaching $\pi$ from a state where the eigenfunction is largest in modulus takes mean time at least $1/\lambda$, and the same holds for a rule reaching any target law $\mu$, with $|u_i - \mu(u)|$ in place of $|u_i|$. The two-state chain is the equality case: there $u = (\sqrt{\pi_2/\pi_1}, -\sqrt{\pi_1/\pi_2})$, $\tau_2 = \tau_1^{(2)} = 1/(a + b)$. On the path family of part (a) the ratio $\tau_2/\tau_1^{(2)}$ is $0.50, 0.33, 0.25$ at $k = 2, 3, 4$ (small $\varepsilon$), and the random search over 20,000 chains found no ratio above $0.99999$, consistent with the proposition.

By Lovász and Winkler's halting-state theorem the minimum in $\tau_1^{(2)}$ equals $\max_j(\mathbb{E}_iT_j - \mathbb{E}_\pi T_j) = \max_j(-Z_{ij}/\pi_j)$, so Proposition 2 can also be read as the inequality $\max_{i,j}(-Z_{ij}/\pi_j) \ge 1/\lambda_2$ for the fundamental matrix of a reversible chain; the proof above does not need the halting-state theorem.

## What is answered and what is not

Open Problem 4.48 is settled as posed: the constant in $\tau_1 \le C\tau_0$ cannot be one (it is at least $t_4/4 = 1.0880$), and the constant in $\tau_2 \le C\tau_1^{(2)}$ can be one, with a proof that fits in a paragraph. Two things remain and are recorded as new problems: the exact value of $\sup\tau_1/\tau_0$ over reversible chains, which lies in $[1.0880, 66]$, and whether it is attained by a birth-and-death chain; and the discrete-time analogues, which the source does not ask about and where $\tau_1$ is defined differently.

Prior art: the online edition of the book (LaTeXML, `stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch4.S7.html`, fetched 14 September 2026) carries the problem without any note of a solution. Lovász and Winkler's *Mixing times* (DIMACS 41, 1998) studies $\tau_1^{(2)}$ for general chains; I could not obtain its text to check whether the eigenvalue bound of Proposition 2 appears there, and a bound of this simplicity may well be known. The counterexample in (a) I have not seen anywhere. Both parts: author checked, exact arithmetic where it matters, no independent read.
