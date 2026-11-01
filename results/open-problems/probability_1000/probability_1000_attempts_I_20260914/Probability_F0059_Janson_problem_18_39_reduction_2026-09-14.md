# Janson's Problem 18.39 reduced to a property of one explicit rate function

Ledger row F0059 (intake F). Source: S. Janson, Probability Surveys 9 (2012), Problem 18.39. Written 14 September 2026, about 09:30. This is a reduction and a partial result, not an answer.

## The problem

With $0 < \nu < \lambda$, so that condensation occurs, Problem 18.39 asks whether $Y_{(1)}/n \to_p 0$ is possible, and conjectures not: *"we conjecture that it is not possible for the full sequence, and, a little stronger, that there always is some $\varepsilon > 0$ and some subsequence along which $Y_{(1)} \ge \varepsilon n$ w.h.p."* Example 18.36 gives $Y_{(1)}/n\to_p0$ along a subsequence.

## The rate

Tilt at $\tau = \rho$, so $\pi_k = w_k\rho^k/\Phi(\rho)$ has mean $\nu$, and the allocation is $n$ i.i.d. copies of $\pi$ conditioned on their sum being $m$. The excess is $M = (\lambda-\nu)n$, and it cannot be absorbed by tilting further, since $\tau$ is capped at $\rho$: that is what condensation means. Suppose it is carried by $r$ boxes of size $a$, $ra = M$. The probability of that class is $\binom nr \pi_a^{\,r}$ up to the bulk's own fluctuation, so
$$\log \mathbb{P} = M\,\Lambda(a) + o(M), \qquad \Lambda(a) := \frac{\log \pi_a + \log\big(a/(\lambda-\nu)\big) + 1}{a}. \tag{1}$$
Two checks. For $\pi_k \sim ck^{-\beta}$, $\Lambda(a) = [\log c' - (\beta-1)\log a]/a$, which increases to $0$, so the maximiser is $a = M$: one box takes the whole excess, which is Theorem 18.33. For $\pi_a = e^{-a^\gamma}$ with $\gamma \in (0,1)$, $\frac{d}{da}\big[(-a^\gamma+\log a + c)/a\big]$ has the sign of $(1-\gamma)a^\gamma - \log a + O(1) > 0$, so again the maximiser is $a = M$. Both are the known condensation picture, so (1) is calibrated.

The maximiser must diverge. If it were bounded, a positive fraction of the boxes would sit at one fixed size and $N_k/n$ would exceed $\pi_k$ by a constant for that $k$, contradicting Theorem 10.4.

## What follows, and what does not

Since $\pi$ has radius of convergence one, $\limsup_a \pi_a^{1/a} = 1$, so $\limsup_a \Lambda(a) = 0$ while $\Lambda < 0$ for large $a$. Hence $\Lambda$ has infinitely many **records**: sizes $a_1 < a_2 < \cdots$ with $\Lambda(a_j) > \Lambda(a)$ for every $a < a_j$. At $M = a_j$ the maximiser of $\Lambda$ over $a \le M$ is $M$ itself, so the deterministic optimum puts the whole excess in a single box, and $Y_{(1)} = (\lambda-\nu)n$ there.

**Proposition.** If along infinitely many records the gap $\Lambda(a_j) - \max_{a \le \varepsilon a_j}\Lambda(a)$ exceeds $C\sqrt{a_j}/a_j$ for some $\varepsilon>0$ and every $C$, then Conjecture 18.39 holds, with $\varepsilon = (\lambda-\nu)/2$: along $n_j = a_j/(\lambda-\nu)$, $\mathbb{P}(Y_{(1)} \ge \varepsilon n_j) \to 1$.

This is the same step that settles Problem 18.40 in the companion memo, where the corresponding rate diverges. Here is the difference, and it is the whole difficulty. In Problem 18.40 the rate is unbounded, $F(s)\to\infty$, so assuming small gaps at every scale and chaining them over multiplicative blocks forces $F$ to be bounded, a contradiction. Here $\Lambda$ is bounded above by $0$ by construction, so the same chaining produces no contradiction: a weight sequence whose $\Lambda$ climbs to $0$ in increments smaller than $a^{-1/2}$ is not excluded by any counting of that kind, and for such a sequence the near-optimal configurations at a record include much smaller box sizes, which is exactly the regime where the allocation could spread and $Y_{(1)}$ be $o(n)$.

So Conjecture 18.39 is equivalent, given the Proposition, to the following question about one explicit function.

**Question.** Let $\pi$ be a probability law on $\mathbb{Z}_{\ge0}$ with radius of convergence one and finite mean, and let $\Lambda(a) = [\log\pi_a + \log a]/a$. Must $\Lambda$ have infinitely many records whose gap below them, $\Lambda(a_j) - \max_{a\le\varepsilon a_j}\Lambda(a)$, exceeds $a_j^{-1/2}$ for some fixed $\varepsilon > 0$?

If yes, the conjecture is a theorem. If no, the law realising it is a candidate counterexample and the remaining work is to show the allocation really does spread there, rather than merely failing to be forced into one box.

## Status

A reduction with a proved conditional statement, not an answer; the row stays open. The calibration of (1) against the two known condensation regimes is the check that the rate is the right object. Verification: author checked. Prior art: a bounded search found nothing on Problem 18.39 since 2012; not a clearance. Ledger row F0059 should keep `unverified` with the reduction recorded.

## New open problem

The Question above, which is a statement about probability laws of radius one and has nothing to do with allocations: does $[\log\pi_a + \log a]/a$ always have records with gaps wider than $a^{-1/2}$? It is the kind of thing that should have an answer in the theory of subexponential and lacunary laws, and it is worth asking on its own.
