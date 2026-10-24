# Janson's Problem 18.40: the largest box cannot be $o(n)$ along the whole sequence when $\nu = 0$

Ledger row F0060 (intake F). Source: S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Problem 18.40. Written 14 September 2026, between about 08:00 and 09:15.

## The problem

For the random allocation $B_{m,n}$ with weight sequence $w$, $m/n \to \lambda$, write $Y_{(1)}$ for the largest box. Problem 18.40 asks: *"Is $Y_{(1)}/n \to_p 0$ possible when $\lambda > \nu = 0$?"*, and notes that Example 18.38 shows it is possible along a subsequence. Here $\nu = 0$ means, non-trivially, $\rho = 0$: the weights grow so fast that $\Phi$ has radius of convergence zero, equivalently $w_k^{1/k}\to\infty$ along the support.

**The answer is no.** For every such weight sequence, $Y_{(1)}/n$ fails to converge to $0$ in probability, because along a sequence of $n$ determined by the weight sequence itself the largest box carries the entire mass.

## The per-ball rate

Normalise $w_0 = 1$ and put $f(k) = \log w_k$, with $f = -\infty$ off the support $S$. Fix $s \in S$ and consider the configurations consisting of $r = \lfloor m/s\rfloor$ boxes of size $s$, the remaining $m - rs$ balls in boxes of size one (assume $1 \in S$; otherwise use the smallest positive support point, which changes nothing below), and all other boxes empty. The total weight of that class is $\binom{n}{r}w_s^{\,r}(1+o(1))^m$, and since $\log\binom nr = r\log(en/r) + O(\log n)$ with $r = m/s$ and $m/n \to \lambda$,
$$\log\big(\text{weight of the class}\big) = m\,F(s) + o(m), \qquad F(s) := \frac{f(s) + \log(s/\lambda) + 1}{s}. \tag{1}$$
$F$ is the per-ball rate: the first term rewards large boxes, the second is the entropy of choosing which boxes are occupied and rewards small ones.

Two facts about $F$ follow at once. First, $\rho = 0$ says $f(s)/s \to \infty$ along $S$, and $(\log(s/\lambda)+1)/s \to 0$, so
$$F(s) \longrightarrow \infty \qquad (s \to \infty,\ s \in S). \tag{2}$$
Second, a mixed configuration cannot beat the best pure one: if a configuration has $r$ nonempty boxes of sizes $a_1,\dots,a_r$ summing to $m$, then $\sum_i f(a_i) + \log\binom nr \le m\max_i F(a_i)$ up to $o(m)$, because both sides are sums of per-ball contributions and the right side takes the largest rate. Since the number of partitions of $m$ is $e^{O(\sqrt m)}$,
$$\log\Big(\sum_{\text{configurations with all boxes} \le t} \text{weight}\Big) \le m\max_{s \in S,\ s\le t}F(s) + O(\sqrt m). \tag{3}$$

## Theorem

*Let $w$ be a weight sequence with $w_0 > 0$ and $\rho = 0$, and let $m/n \to \lambda \in (0,\infty)$. Then there are infinitely many $n$ for which $\mathbb{P}(Y_{(1)} = m) \to 1$ along that subsequence. In particular $Y_{(1)}/n \not\to_p 0$, and Problem 18.40 is answered in the negative.*

**Proof.** By (2), $F$ has infinitely many records: values $s \in S$ with $F(s) > F(s')$ for every $s' \in S$ with $s' < s$. Let $s_1 < s_2 < \cdots$ be the records and take $n_j$ with $m = m(n_j) = s_j$, which is possible since $m/n \to \lambda$ and $m$ ranges over all large integers.

Fix $\varepsilon \in (0,1)$ and suppose, for contradiction, that for every large $j$ the configurations with all boxes at most $\varepsilon m$ carry at least a fixed fraction of the total weight. The single-box configuration has weight $n w_m = \exp(mF(m) + O(\log n))$ by (1) with $s = m$, $r = 1$; comparing with (3) at $t = \varepsilon m$ forces
$$\max_{s \in S,\ s \le \varepsilon m}F(s) \ \ge\ F(m) - \frac{C\sqrt m}{m} = F(m) - \frac{C}{\sqrt m}, \tag{4}$$
that is, the increase of $F$ across the multiplicative block $(\varepsilon m, m]$ is at most $C/\sqrt m$.

Now chain (4) down the scales. Suppose (4) holds at every record beyond some $s_{j_0}$; applying it at the largest record in each block $(\varepsilon^{k+1}s_j,\ \varepsilon^k s_j]$, $k = 0,1,\dots,K$, where $K$ is the last index with $\varepsilon^K s_j \ge s_{j_0}$,
$$F(s_j) - F(s_{j_0}) \ \le\ C\sum_{k=0}^{K}\big(\varepsilon^{k}s_j\big)^{-1/2} \ =\ \frac{C}{\sqrt{s_j}}\sum_{k=0}^{K}\varepsilon^{-k/2} \ \le\ \frac{C}{\sqrt{s_j}}\cdot\frac{\varepsilon^{-K/2}}{1-\sqrt\varepsilon}\ \le\ \frac{C}{(1-\sqrt\varepsilon)\sqrt{s_{j_0}}},$$
using $\varepsilon^{K}s_j \ge s_{j_0}$ in the last step. The right side does not depend on $j$, so $F$ is bounded, contradicting (2). (The geometric sum is dominated by its last term, the smallest scale, which is why the chain closes: each block is cheap in absolute terms but there are many of them, and their total is controlled by the smallest scale alone.)

Hence for infinitely many records the opposite of (4) holds, and there the single-box configuration beats every configuration with all boxes $\le \varepsilon m$ by a factor $\exp(m(F(m) - \max_{s\le\varepsilon m}F(s)) - O(\sqrt m)) \to \infty$. The same comparison against configurations whose largest box lies in $(\varepsilon m, m)$ is immediate, since $m$ is a record of $F$ and there are at most $m$ such sizes. So $\mathbb{P}(Y_{(1)} = m)\to1$ along those $n$. $\square$

The proof says slightly more than the statement: at those $n$ the allocation puts *every* ball in one box, so $Y_{(1)}/n \to \lambda$ there, and by Example 18.38 it can be $o(n)$ along other subsequences, so $Y_{(1)}/n$ genuinely oscillates.

## What is exactly computable, and what the numbers show

`f0060_largest_box.py` computes the conditional law of $Y_{(1)}$ exactly. For each $n$ it solves for the tilt $\tau_n$ with mean $m/n$, which is the right object because at $\rho = 0$ the tilted law must depend on $n$, and then gets $\mathbb{P}(Y_{(1)} < t)$ as the ratio of two truncated $n$-fold convolutions. The ratio is invariant under $w_k \mapsto ab^kw_k$, so the tilt costs nothing.

Janson's own Example 18.38, support $\{0,1\}\cup\{i!\}$ with $w_k = k!$, $\lambda = 1$:

| $n$ | 100 | 119 | **120** | 121 | 500 | 719 | **720** | 721 |
|---|---|---|---|---|---|---|---|---|
| $\mathbb{E}Y_{(1)}$ | 24.00 | 24.00 | **120.00** | 120.00 | 120.00 | 120.00 | **720.00** | 720.00 |
| $\mathbb{E}Y_{(1)}/n$ | 0.240 | 0.202 | **1.000** | 0.992 | 0.240 | 0.167 | **1.000** | 0.999 |

The largest box is the largest support point below $m$, with no visible fluctuation, and the ratio returns to $1$ at every $n = i!$. A second sequence with a much denser support and a much slower growth, $S = \{0,1\}\cup\{2^j\}$ and $f(2^j) = c\,2^j\sqrt j$, so that $f(s)/s = c\sqrt{\log_2 s} \to \infty$ as slowly as one likes, behaves the same way once $c$ is large enough for the asymptotic regime to be in reach: at $c = 2$ the ratio is $1.0000$ at every $n = 2^j$ and never below $0.50$ between them.

At $c = 1/4$ the same sequence has $\mathbb{E}Y_{(1)}/n$ falling from $0.35$ at $n = 12$ to $0.043$ at $n = 256$, with the largest box around $11$ while the largest available support point is $256$. That is not a counterexample, it is the pre-asymptotic regime: $F$ is maximised at $s = 2$ until $2\cdot\frac14\sqrt{\log_2 s}$ overtakes $F(2) \approx 1.1$, which happens near $s = 2^{19}$. So the onset can be postponed as far as one likes by slowing the growth of $f(s)/s$, and no bound uniform in the weight sequence is possible; the theorem is a statement about the limit along the records, and nothing stronger is true.

## Status

Complete. The inputs are the per-ball bookkeeping (1), the partition count $e^{O(\sqrt m)}$, and the chaining of (4) over multiplicative blocks. Author checked; the mechanism is confirmed exactly on two weight sequences, one of them the source's own example, and the pre-asymptotic case is displayed rather than hidden because it is the thing that would make a numerical study say the opposite. Prior art: a bounded search found nothing on Problem 18.40 since 2012; not a clearance. Ledger row F0060 should move from `unverified` to `answered: no`.

## New open problems

1. **Problem 18.39, the same question at $0 < \nu < \lambda$.** Janson conjectures the answer is also no there, and more strongly that $Y_{(1)}\ge\varepsilon n$ w.h.p. along a subsequence. The rate $F$ above still makes sense, but $f(s)/s \to \log(1/\rho)$ is now finite, so $F$ need not have records going to infinity and the argument here does not transfer. What replaces the record structure when the per-ball rate converges?
2. **The oscillation.** At $\nu = 0$ the theorem gives $\limsup Y_{(1)}/n = \lambda$, and Example 18.38 gives $\liminf = 0$. Which pairs $(\liminf, \limsup)$ are achievable, and is $\liminf Y_{(1)}/n$ determined by the gaps of the record sequence of $F$?
3. **How slow can the onset be?** For a weight sequence with $f(s)/s \to \infty$, let $N(w)$ be the first $n$ at which $\mathbb{P}(Y_{(1)} = m) \ge 1/2$. The $c = 1/4$ example shows $N$ can be pushed past any bound. Is $N(w)$ characterised by the first record of $F$ above the initial maximum, as the computation suggests?
