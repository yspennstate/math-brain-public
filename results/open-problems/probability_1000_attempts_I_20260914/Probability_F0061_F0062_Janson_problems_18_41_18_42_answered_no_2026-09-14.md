# Janson's Problems 18.41 and 18.42: monotone weights and exploding ratios do not force a single condensate

14 September 2026. Ledger rows F0061 and F0062 (intake F). Source: Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Section 18.6, PDF page 122.

## The questions

In the balls-in-boxes model $B_{m,n}$ with weight sequence $w$, when $m/n \to \lambda > \nu$ the small boxes carry $\nu n + o_p(n)$ balls and the remaining $(\lambda - \nu)n$ are "missing" (Lemma 18.31). Condensation to a single box means
$$Y_{(1)} = (\lambda - \nu)n + o_p(n), \tag{18.106}$$
$$Y_{(2)} = o_p(n). \tag{18.107}$$
Theorem 18.33 proves this for $w_k \sim ck^{-\beta}$, $\beta > 2$. Examples 18.36 and 18.37 show that for "very irregular" weight sequences the missing balls can split into two or more giant boxes, or into many boxes of size $o(n)$. The source then asks:

> **Problem 18.41.** Suppose that $w_k \ge w_{k+1}$ for all (large) $k$. Does this imply that (18.106)-(18.107) hold when $\lambda > \nu$?
>
> **Problem 18.42.** Suppose that $w_{k+1}/w_k \to \infty$ as $k \to \infty$ (hence $\rho = 0$ and $\nu = 0$). Does this imply that (18.106)-(18.107) hold when $\lambda > \nu$?

Both answers are no. Each regularity hypothesis controls the first differences of $\log w_k$ and says nothing about the second differences, and condensation to a single box is a statement about second differences: one box of size $a + b$ beats two boxes of sizes $a$ and $b$ exactly when $\log w_{a+b} + \log w_0 > \log w_a + \log w_b$ by more than the entropy of placing a second box, which is $O(\log n)$. A weight sequence can satisfy either hypothesis and still have $\log w$ fail that superadditivity at a scale of order $n$, along a subsequence of $m$. The two constructions below are explicit and the proofs are elementary. Both ledger attempts (F0061-A001, F0062-A001) had guessed yes by a "shed $j$ balls" argument; the constructions show where that argument breaks, and that is recorded at the end.

Throughout, $Y_{(1)} \ge Y_{(2)} \ge \dots$ are the ordered box counts of $B_{m,n}$, and "w.h.p." means with probability tending to one along the stated subsequence.

## Theorem A (Problem 18.42)

Let $d_j = j^3$ if $j \in \{1, 2, 4, 8, \dots\}$ is a power of two and $d_j = j$ otherwise ($d_0 = 0$). Put $w_0 = 1$ and $w_k = \exp\big(\sum_{j < k} d_j\big)$ for $k \ge 1$. Then $w_{k+1}/w_k = e^{d_k} \to \infty$, so $\rho = 0$, $\nu = 0$, $\omega = \infty$, $\mathrm{span}(w) = 1$. Let $m = 2^{i+1}$ and let $n = n(m) \ge 2$ with $n = O(m)$ (for instance $n = \lfloor m/\lambda \rfloor$ for any fixed $\lambda \in (0, \infty)$). Then
$$\mathbb{P}\big(Y_{(2)} > m/8\big) \to 1 \qquad (i \to \infty).$$
Consequently, along this subsequence $Y_{(2)}/n$ is bounded away from zero and $Y_{(1)} \le 7m/8$, so neither (18.106) nor (18.107) holds, for any $\lambda > 0 = \nu$.

*Proof.* Write $L(y) = \log w_y = \sum_{j < y} d_j = Q(y) + S(y)$ with
$$Q(y) = \sum_{j < y,\ j \notin \{1,2,4,\dots\}} j, \qquad S(y) = \sum_{l \ge 0:\ 2^l < y} 8^l .$$
Since the powers of two below $y$ sum to less than $2y$, $\tfrac12 y(y-1) - 2y < Q(y) \le \tfrac12 y(y-1)$; and for $2^l < y \le 2^{l+1}$, $S(y) = (8^{l+1} - 1)/7$, with $S(1) = 0$.

The reference configuration $C^*$ puts $a^* = 2^i + 1$ balls in box 1, $b^* = 2^i - 1$ in box 2 and none elsewhere. Its log-weight is $L^* = L(a^*) + L(b^*)$, where $S(a^*) = (8^{i+1} - 1)/7$ (because $2^i < a^* \le 2^{i+1}$) and $S(b^*) = (8^i - 1)/7$ (because $2^{i-1} < 2^i - 1 \le 2^i$ for $i \ge 2$), and
$$Q(a^*) + Q(b^*) \ge \tfrac12\big(a^{*2} + b^{*2} - m\big) - 2m = \tfrac14 m^2 - \tfrac52 m + 1 .$$

Let $\mathcal{B} = \{Y_{(2)} \le D\}$ with $D = 2^{i-2} = m/8$. Take a configuration $(y_1, \dots, y_n) \in \mathcal{B}$ with $y_1 = Y_{(1)}$, call the other boxes the dust, and let $r = m - y_1$ be the number of balls in the dust. Since $\sum_j \tfrac12 y_j(y_j - 1) \le \tfrac12 m^2$,
$$\sum_j L(y_j) \le \tfrac12 m^2 + S(y_1) + \sum_{\text{dust}} S(y_j).$$
The dust sum is $\sum_{l \ge 0} 8^l N_l$ with $N_l$ the number of dust boxes holding more than $2^l$ balls; $N_l = 0$ for $l \ge i - 2$, and $N_l \le r/(2^l + 1)$.

*Case 1, $y_1 \le 2^i$.* Then $S(y_1) \le (8^i - 1)/7$, $r \le m$, and $\sum_{\text{dust}} S \le m\sum_{l \le i-3} 4^l < m\,4^{i-2}/3 = 8^{i-1}/3$. Total: $S(y_1) + \sum_{\text{dust}} S < (8/7 + 1/3)\,8^{i-1} < 1.48 \cdot 8^{i-1}$.

*Case 2, $y_1 > 2^i$.* Then $S(y_1) \le (8^{i+1} - 1)/7$ and $r \le 2^i - 1$. Let $t = N_{i-3}$ be the number of dust boxes holding more than $2^{i-3}$ balls. They hold at least $t(2^{i-3} + 1)$ balls, so $t \le 7$. These $t$ boxes are counted in $N_l$ for every $l \le i-3$ and contribute less than $t\,8^{i-2}/7$. The remaining dust boxes hold at most $2^{i-3}$ balls each and at most $(8 - t)2^{i-3}$ balls in total, so they contribute less than $(8-t)2^{i-3}\sum_{l \le i-4} 4^l < (8-t)\,8^{i-3}/3$. Hence
$$\sum_{\text{dust}} S < 8^{i-3}\Big(\frac{8t}{7} + \frac{8-t}{3}\Big) \le 8^{i-3}\cdot\frac{25}{3} = \frac{25}{24}\,8^{i-2}.$$

In both cases $S(y_1) + \sum_{\text{dust}} S \le (8^{i+1}-1)/7 + \tfrac{25}{24}8^{i-2}$, while $S(a^*) + S(b^*) = (8^{i+1} - 1)/7 + (8^i - 1)/7$. Therefore, for every configuration in $\mathcal{B}$,
$$\sum_j L(y_j) - L^* \le \Big(\tfrac12 m^2 - \tfrac14 m^2 + \tfrac52 m\Big) - \Big(\frac{8^i - 1}{7} - \frac{25}{24}8^{i-2}\Big) \le \tfrac14 m^2 + \tfrac52 m - \frac{1361}{168}\,8^{i-2} + \tfrac17 < \tfrac14 m^2 + \tfrac52 m - \frac{m^3}{64},$$
using $8^{i-2} = m^3/512$ and $1361/168 > 8.1$. For $m \ge 64$ the right side is below $-m^3/128$ (this needs $m^2 \ge 32m + 320$).

The number of configurations of $m$ balls in $n$ boxes is $\binom{m+n-1}{n-1} \le 2^{m+n}$, and $Z(m,n) \ge e^{L^*}$ (the weight of $C^*$ alone). Hence
$$\mathbb{P}(\mathcal{B}) \le \frac{2^{m+n}\,e^{L^* - m^3/128}}{e^{L^*}} = 2^{m+n} e^{-m^3/128} \to 0$$
whenever $n = O(m)$ (indeed whenever $n \le e^{m^3/256}$). Since $\mathcal{B}^c = \{Y_{(2)} > m/8\}$ and then $Y_{(1)} \le m - Y_{(2)} < 7m/8$, both displayed statements fail along $m = 2^{i+1}$. $\square$

*Exact check.* With $n = 2m$: $\mathbb{P}(Y_{(2)} \le m/8)$ equals $e^{-4088.7}$, $e^{-37586}$, $e^{-311282}$ at $m = 64, 128, 256$, computed from the partition functions $[t^m](\sum_{k \le D} w_k t^k)^n$ and $n\sum_{y > D} w_y [t^{m-y}](\sum_{k \le D} w_k t^k)^{n-1}$ against $[t^m](\sum_k w_k t^k)^n$ in 25-digit arithmetic (`janson_cond_check.py`). The bound in the proof gives $\log\mathbb{P} \le (m+n)\log 2 - m^3/128 = -1915$ at $m = 64$; the truth is smaller, as it should be.

## Theorem B (Problem 18.41)

Fix integers $J_1 < J_2 < \dots$ with $J_{r+1} \ge 2J_r + 6$ (the cliffs). For $j \ge 0$ put
$$g(j) = \max\Big(3j,\ \max\{6J_r + 4 : J_r \le j\}\Big),$$
and let $w_0 = 1$, $w_k = e^{-g(\lfloor \log_2 k \rfloor)}$ for $k \ge 1$. Then $g$ is nondecreasing, so $w_k \ge w_{k+1}$ for every $k$; and $3j \le g(j) \le 6j + 4$ gives $e^{-4}k^{-6/\ln 2} \le w_k \le e^3 k^{-3/\ln 2}$, where $3/\ln 2 = 4.328$ and $6/\ln 2 = 8.656$. So $\rho = 1$, $\Phi(1) < \infty$, $\sum_k k^2 w_k < \infty$, $\nu = \Phi'(1)/\Phi(1) \in (0, \infty)$, and the law $\pi_k = w_k/\Phi(1)$ has span one, mean $\nu$ and finite positive variance $\sigma^2$. Fix $\lambda > \nu$. For each cliff $J$ let
$$B = 2^{J-1}, \qquad K = 3B, \qquad n = \lceil K/(\lambda - \nu)\rceil, \qquad m = K + \lfloor \nu n \rfloor,$$
so $m/n \to \lambda$. Then
$$\mathbb{P}\big(Y_{(2)} \ge B/4\big) \to 1 \qquad (J \to \infty \text{ through the cliffs}).$$
Since $B/4 \ge (\lambda - \nu)n/13$ for large $J$, (18.107) fails. By Lemma 18.31(i) the boxes above any level $K_n \to \infty$, $K_n = o(n)$, hold at most $(\lambda - \nu)n + o_p(n)$ balls, so $Y_{(1)} + Y_{(2)} \le (\lambda - \nu)n + o_p(n)$ and $Y_{(1)} \le \tfrac{12}{13}(\lambda - \nu)n + o_p(n)$ w.h.p.; (18.106) fails too.

The idea: in block $J-1 = [2^{J-1}, 2^J)$ the weights are $e^{-3(J-1)}$, while at the cliff the weights in block $J$ drop to $e^{-6J-4}$, which is $e^{-10}$ times the product of two block-$(J-1)$ weights. One box holding the $K = 3B$ missing balls sits in block $J$; two boxes each in block $J-1$ can hold them, and there are about $n$ ways to split $K$ between two such boxes and $n^2$ ways to place them. So the two-box configurations outweigh the one-box ones by about $n^2 e^{10}$, and everything else is rarer still.

*Proof.* The sparseness condition puts the end of the previous plateau, $2J_r + 1$, at or before $J - 5$, so $g(j) = 3j$ for $J - 4 \le j \le J - 1$ and $g(J) = 6J + 4$. Let $\xi, \xi_1, \xi_2, \dots$ be i.i.d. with law $\pi$, $S_N = \xi_1 + \dots + \xi_N$, and $X_i = \xi_i - \nu$. For any property of configurations, the weight of the configurations of $B_{m,n}$ with that property is $\Phi(1)^n\,\mathbb{P}(S_n = m,\ (\xi_1,\dots,\xi_n) \text{ has the property})$, because $\prod_i w_{y_i} = \Phi(1)^n \prod_i \pi_{y_i}$.

Two standard tools. First, the truncated exponential bound (Fuk and Nagaev; Nagaev 1979, inequality (1.56); the proof is the Bernstein argument applied to $X_i\mathbf 1\{X_i \le h\}$): for independent centred $X_i$ with $\sum_i \mathbb{E}X_i^2 = N\sigma^2$ and $x, h > 0$,
$$\mathbb{P}\Big(\sum_{i \le N} X_i \ge x,\ \max_i X_i \le h\Big) \le \Big(\frac{e}{1 + xh/(N\sigma^2)}\Big)^{x/h}. \tag{FN}$$
Second, Gnedenko's local limit theorem (Janson's Lemma 13.1 with $\xi^{(n)} \equiv \xi$): $\mathbb{P}(S_N = j) = (1 + o(1))(2\pi\sigma^2 N)^{-1/2}$ uniformly for $|j - \nu N| \le \sqrt N$.

Let $y = 2^{J-3} = B/4$ and classify configurations by the number of boxes holding at least $y$ balls: $A_0$ (none), $A_1$ (exactly one), $A_2$ (two or more). Then $\mathbb{P}(Y_{(2)} < y) = (W(A_0) + W(A_1))/Z(m,n) \le (W(A_0) + W(A_1))/W(A_2)$. Note $2^J = 2B \asymp n$, so $e^{-3J} \asymp n^{-4.328}$ and $e^{-6J} \asymp n^{-8.656}$, and $y^2/n \asymp n$.

*$A_0$.* On $A_0 \cap \{S_n = m\}$, $\sum_i X_i = m - \nu n \ge K - 1 = 12y - 1 =: x_0$ and $X_i < y$. By (FN) with $h = y$: $x_0/y \ge 11.9$ and $x_0 y/(n\sigma^2) \ge c_1 n$ for large $J$, so $W(A_0)/\Phi(1)^n \le (e/(c_1 n))^{11.9} \le C n^{-11.9}$.

*$A_1$.* $W(A_1) = n\sum_{k \ge y} w_k\,\Phi(1)^{n-1}\,\mathbb{P}(S_{n-1} = m - k,\ \max_{i \le n-1}\xi_i < y)$. For $k \ge 2^J$, $w_k \le e^{-g(J)} = e^{-6J-4}$ since $g$ is nondecreasing, and the probabilities sum to at most one: contribution at most $n\,e^{-6J-4}\,\Phi(1)^{n-1}$. For $y \le k < 2^J$, $w_k \le w_y = e^{-g(J-3)} = e^{-3J+9}$, and $S_{n-1} = m - k$ forces $\sum_{i \le n-1} X_i \ge K - 2^J + \nu - 1 \ge 4y - 1 =: x_1$ with $\max X_i < y$; summing the probabilities over $k$ and applying (FN) with $x_1/y \ge 3.9$ gives at most $e^{-3J+9}\,C n^{-3.9}$. Altogether
$$W(A_1)/\Phi(1)^n \le C\big(n\,e^{-6J} + n^{-2.9}e^{-3J}\big) \le C\big(n^{-7.65} + n^{-7.22}\big).$$

*$A_2$, a lower bound.* Let $I = [B, 2B)$ (block $J - 1$), on which $w_a = e^{-3(J-1)}$. Count only configurations in which two boxes $i < j$ hold $a, b \in I$ and every other box holds fewer than $B$ balls; each such configuration lies in $A_2$ and is counted once. Thus
$$W(A_2) \ge \binom n2 \sum_{a, b \in I} e^{-6J+6}\,\Phi(1)^{n-2}\,\mathbb{P}\big(S_{n-2} = m - a - b,\ \max_{i \le n-2}\xi_i < B\big).$$
Restrict to $a + b = K + s$ with $|s| \le \sqrt n/2$. Then $m - a - b - \nu(n-2) = \lfloor \nu n\rfloor - \nu n - s + 2\nu$, which is at most $\sqrt{n-2}$ in absolute value for large $n$, so by the local limit theorem $\mathbb{P}(S_{n-2} = m - a - b) \ge c/\sqrt n$; and $\mathbb{P}(\max_{i \le n-2}\xi_i \ge B) \le n\,\mathbb{P}(\xi \ge B) \le C n B^{-3.328} \le C n^{-2.3} = o(n^{-1/2})$, so the joint probability is at least $c/(2\sqrt n)$. For each such $s$ the number of pairs $(a, b) \in I^2$ with $a + b = K + s$ is the number of $a \in [B, 2B) \cap (B + s, 2B + s]$, at least $B - |s| - 1 \ge B/2$; and there are at least $\sqrt n$ admissible $s$. Hence
$$W(A_2)/\Phi(1)^n \ge \binom n2\cdot\frac B2\cdot\sqrt n\cdot e^{-6J+6}\cdot\frac{c}{2\sqrt n} \ge c'\,n^2 B\,e^{-6J} \ge c''\,n^{3 - 8.656} = c''\,n^{-5.656}.$$

*Conclusion.* $\mathbb{P}(Y_{(2)} < y) \le C(n^{-11.9} + n^{-7.22})/(c'' n^{-5.656}) \to 0$. $\square$

## Remarks

1. **What each hypothesis controls.** $w_{k+1}/w_k \to \infty$ says the increments $d_k$ of $\log w_k$ tend to infinity; monotonicity says they are nonpositive. Condensation to one box needs $\log w$ to be superadditive at the relevant scale, $\log w_{a+b} + \log w_0 \ge \log w_a + \log w_b - O(\log n)$ for $a, b \asymp n$, and that is a condition on second differences. In Theorem A the increments are $j$ except for a spike of size $j^3$ at every power of two; the spikes make $\log w$ concave across each dyadic scale, so at $m = 2^{i+1}$ a box just above $2^i$ collects the top spike and a second box of size $2^i - 1$ collects every lower spike, which one box of size $m$ cannot do twice. In Theorem B the sequence is a staircase of dyadic plateaus descending like a power law, with an occasional double-height step; at such a step the two boxes in the block above the step are worth $e^{10}$ times the one box below it, and entropy pays the rest.

2. **Why the "shed $j$ balls" heuristic fails.** Both recorded attempts argued that a configuration with two big boxes $a, b$ is beaten by one box of size $a + b - j$ plus a small box of size $j$, the small box chosen so that $w_{a+b-j}$ escapes any local dip of $w$. In Theorem A, escaping the spike requires $a + b - j \le 2^i$, that is $j \ge m/2$, so the "small" box is macroscopic and the pair $(a+b-j, j)$ is itself an oligopoly. In Theorem B, escaping the cliff requires $a + b - j < 2^J$, that is $j > K/3$, with the same consequence. A dip in a weight sequence can be as wide as the condensate.

3. **What is not claimed.** Neither theorem identifies the law of $(Y_{(1)}, Y_{(2)})$ along the subsequence; in Theorem A the configuration $(2^i + 1, 2^i - 1)$ presumably dominates, and in Theorem B the two boxes presumably split $K$ roughly evenly with a spread of order $\sqrt n$, but only the lower bounds needed for the refutation are proved. Along other subsequences of $m$ (Theorem A) or away from the cliffs (Theorem B) the behaviour may well be single-box condensation; the problems ask about the full sequence, and one bad subsequence suffices. Neither construction bears on Problems 18.39 and 18.40 (whether $Y_{(1)}/n \to 0$ is possible along the full sequence): in both, $Y_{(1)}$ is of order $n$.

4. **Both answers extend to trees.** Lemma 16.1 of the source transfers allocation statements with $m = n - 1$ to simply generated trees $\mathcal T_n$ via the outdegree sequence. Theorem A with $\lambda = 1$ (take $m = n - 1 = 2^{i+1}$, so $n = 2^{i+1} + 1$) gives a weight sequence with $w_{k+1}/w_k \to \infty$ whose simply generated trees have, along a subsequence, two nodes of outdegree at least $n/8$ w.h.p. For Theorem B one needs $\lambda = 1 > \nu$, which holds after scaling $w_k$ by $c^k$ if necessary (this changes neither the monotonicity for $c \le 1$ nor the model, by the equivalence of weight sequences), provided $\nu < 1$; I have not checked the bookkeeping for the tree case and do not claim it.

## Numerical check of Theorem B

Exact (double precision, positive terms only, so no cancellation) computation of $\mathbb{P}(Y_{(2)} \ge y)$ from the convolution powers of the law $\pi$, for the cliff sequence with a single cliff at $J$ against the same sequence with the cliff removed ($g(j) = 3j$ throughout), at $\lambda - \nu = 1$ ($\nu = 0.6243$); script `check_1841_np.py`.

| $J$ | $n$ | $m$ | $K = 3B$ | $y = B/4$ | $\mathbb{P}(Y_{(2)} \ge y)$, cliff | no cliff | $y = B/2$, cliff | no cliff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 384 | 623 | 384 | 32 | 0.9999 | 0.0024 | 0.9946 | 0.0006 |
| 9 | 768 | 1247 | 768 | 64 | 1 − 8·10⁻⁸ | 0.0005 | 0.9995 | 0.0001 |
| 10 | 1536 | 2494 | 1536 | 128 | 1 − 2·10⁻¹⁰ | 0.0001 | 0.9999 | 0.00002 |

With the cliff the second box is already macroscopic at $n = 384$; without it the same sequence condenses to one box, as Theorem 18.33's mechanism predicts for a power-law staircase. The convergence is fast here because $\lambda - \nu = 1$; at $\lambda - \nu = 0.15$ the same computation at $J = 8$ ($n = 2560$) gives only $0.38$ against $0.024$, because the truncated-deviation bound (FN) needs $B^2/n \gg \sigma^2$ and $B^2/n = (\lambda-\nu)^2 n/36$ is still small there. The proof is asymptotic; the table shows the mechanism, not the theorem.

## Status

Mathematics: complete for both problems, author checked; each proof is an explicit configuration count against an explicit reference configuration, plus, for Theorem B, the classical truncated exponential bound and the local limit theorem for a fixed finite-variance lattice law. Verification word: author checked, no independent read. Prior art: the constructions are in the spirit of Janson's own Examples 18.36-18.37, and I found no paper addressing Problems 18.41 or 18.42 in a bounded search; not a clearance. Ledger rows F0061 and F0062 should move from `attempted_unsolved` (heuristic yes) to `refuted`, with the recorded heuristics marked as superseded by the constructions above.
