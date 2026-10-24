# Janson's Problem 18.30: at the critical ratio with infinite variance, conditioning can force a box the independent model never produces

14 September 2026. Ledger row F0058 (intake F). Source: Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Problem 18.30, Section 18.5, PDF page 112.

## The question

Theorem 18.7 of the source compares the largest boxes of the allocation $B_{m,n}$ with the largest of $n$ independent copies of the tilted variable $\xi$. Two of its parts need only the first-order picture:

(ii) if $n\,\mathbb{P}(\xi \ge h(n)) \to 0$ then w.h.p. $Y_{(1)} < h(n)$;
(iii) if $n\,\mathbb{P}(\xi \ge h(n)) \to \infty$ then, for every fixed $j$, w.h.p. $Y_{(j)} \ge h(n)$.

The theorem assumes $\sigma^2 = \mathrm{Var}\,\xi < \infty$. Example 18.27 shows that at $\lambda = \nu$ with $\sigma^2 = \infty$ (weights $w_k \sim ck^{-\alpha-1}$, $1 < \alpha < 2$) the laws of $Y_{(1)}$ and $\xi_{(1)}$ differ in the limit but stay of the same order, and the source asks:

> **Problem 18.30.** In the case $\lambda = \nu$, do Theorem 18.7(ii)-(iii) hold also when $\sigma^2 = \infty$?

The answer is no for both parts. For (ii): there is a probability weight sequence with $\rho = 1$, $\nu = \mathbb{E}\xi < \infty$, $\sigma^2 = \infty$, and a sequence $n_r \to \infty$ with $m_r = \lfloor \nu n_r \rfloor$, along which the allocation has a box of a size $h_r$ with probability tending to one while $n_r\,\mathbb{P}(\xi \ge h_r) \to 0$. So $Y_{(1)}$ and $\xi_{(1)}$ are not even of the same order of magnitude in general. For (iii): a second sequence, built by the same method with one more scale, has a level $h_r$ with $n_r\,\mathbb{P}(\xi \ge h_r) \to \infty$ such that $Y_{(2)} < h_r$ with probability tending to one (Theorem 2 below). The first version of this memo, written a few hours earlier, claimed that (iii) could not fail by this mechanism; the exact toy computation in Remark 3 showed that claim wrong, and Theorem 2 is the corrected statement.

The mechanism is the following. With $\sigma^2 = \infty$ the mean of $S_n$ can sit far outside the bulk of its distribution: a rare large atom of $\xi$ contributes to $\mathbb{E}S_n$ but is almost never present. Conditioning on $S_n = m \approx \mathbb{E}S_n$ then has to find the missing mass somewhere, and if another rare atom has exactly the missing size, one copy of it is the cheapest way to pay. Its cost is polynomial (the probability of one rare atom among $n$ summands) while the alternative, a fluctuation of the bulk, costs a Gaussian factor. In the independent model that atom appears with probability tending to zero.

## The weight sequence

Let $a = b = 1/4$. For $r \ge 1$ put
$$c_{2r} = e^{4r^2}, \qquad L_{2r} = \lceil e^{8r^3} \rceil, \qquad L_{2r-1} = \lceil L_{2r}/r \rceil, \qquad p_{2r} = \frac{c_{2r}}{L_{2r}^2}, \qquad n_r = \Big\lfloor \frac{1}{r\,p_{2r}} \Big\rfloor,$$
so that $n_r p_{2r} = 1/r$ (up to rounding) and the "shift" $n_r p_{2r} L_{2r}$ equals $L_{2r-1}$ up to rounding. The bulk at stage $r$ consists of the atoms $0, 1, 2$ and the scales $L_j$, $j \le 2r-2$; its per-summand variance is
$$C_r = a + 4b - (a + 2b)^2 + \sum_{j \le 2r-2} p_j L_j^2 = e^{4(r-1)^2}(1 + o(1)),$$
and its standard deviation over $n_r$ summands is $s_r = \sqrt{n_r C_r} = e^{8r^3 - 4r + 2}\,r^{-1/2}(1 + o(1))$. Put
$$\Lambda_r = \frac{L_{2r-1}}{s_r} = \frac{e^{4r-2}}{\sqrt r}(1 + o(1)) \to \infty, \qquad \delta_r = \frac{1}{10\Lambda_r}, \qquad p_{2r-1} = \frac{\delta_r}{n_r}.$$
Finally let $\xi$ have the law $\mathbb{P}(\xi = 1) = a$, $\mathbb{P}(\xi = 2) = b$, $\mathbb{P}(\xi = L_j) = p_j$ for $j \ge 1$, and $\mathbb{P}(\xi = 0) = 1 - a - b - \sum_j p_j$, and let $w_k = \mathbb{P}(\xi = k)$. The $p_j$ are summable and tiny ($p_{2r} \le e^{4r^2 - 16r^3}$), so this is a probability weight sequence with $w_0 > 0$, $\mathrm{span}(w) = 1$, $\omega = \infty$; $\rho = 1$ because $w_{L_j}^{1/L_j} \to 1$; $\nu = \Phi'(1) = \mathbb{E}\xi = a + 2b + \sum_j p_j L_j < \infty$ because $p_{2r}L_{2r} = c_{2r}/L_{2r}$ and $p_{2r-1}L_{2r-1} \le 1/(r n_r)\cdot L_{2r-1} \le 2 c_{2r}/L_{2r}$ are summable; and $\sigma^2 = \infty$ because $\sum_r p_{2r}L_{2r}^2 = \sum_r c_{2r} = \infty$. Take $m_r = \lfloor \nu n_r \rfloor$, so $m_r = \nu n_r + O(1)$ and $\lambda = \nu$.

Three size relations drive the proof; all follow from the definitions and hold for $r \ge 2$:
$$L_{2r-2} \Lambda_r / s_r \to 0 \qquad (\text{the bulk summands are tiny on the scale of } s_r), \tag{R1}$$
$$s_r\,\Lambda_r\,e^{-\Lambda_r^2/4} \to 0 \qquad (\text{double exponential beats exponential: } \log s_r \approx 8r^3,\ \Lambda_r^2 \approx e^{8r-4}/r), \tag{R2}$$
$$n_r \sum_{j > 2r} p_j L_j \le 2 n_r \frac{c_{2r+1}}{L_{2r+1}} = O\big(e^{-12r^2}\big) L_{2r-1} = o(s_r), \qquad n_r \sum_{j > 2r} p_j = o(1/r). \tag{R3}$$

## Theorem

Along $n = n_r$, $m = m_r$, with $h_r = L_{2r-1}$:
$$\mathbb{P}\big(Y_{(1)} \ge h_r\big) \to 1 \qquad\text{while}\qquad n_r\,\mathbb{P}(\xi \ge h_r) \le \delta_r + \tfrac1r + o(1/r) \to 0 .$$
Define $h(n) = h_r$ for $n = n_r$ and $h(n) = n^2$ otherwise; then $n\,\mathbb{P}(\xi \ge h(n)) \to 0$ along the full sequence (for $n \notin \{n_r\}$ by Markov's inequality) while $\mathbb{P}(Y_{(1)} < h(n)) \to 0$ along $n_r$. Hence Theorem 18.7(ii) fails at $\lambda = \nu$, $\sigma^2 = \infty$, $m = \nu n + O(1)$. The same computation shows that parts (i), (iv), (v) and (vi) fail along this subsequence as well (the count of boxes of size $\ge h_r$ is $1$ w.h.p. against a Poisson$(0)$ prediction), and that $Y_{(1)}/\xi_{(1)} \ge L_{2r-1}/L_{2r-2} \to \infty$ w.h.p., so the two maxima are of different orders.

## Proof

Fix $r$ and write $n, m, L_A = L_{2r-1}, L_B = L_{2r}, s = s_r, \Lambda = \Lambda_r, \delta = \delta_r$. Call a summand *rare* if it takes a value $L_j$ with $j \ge 2r-1$, and let $q = \sum_{j \ge 2r-1} p_j$ be the probability of being rare; $nq = \delta + 1/r + o(1/r) \to 0$. The *bulk law* is the law of $\xi$ conditioned on not being rare; it is supported on $\{0,1,2\} \cup \{L_j : j \le 2r-2\}$, so its summands are bounded by $L_{2r-2}$, and its mean is
$$\mu' = \frac{\nu - \sum_{j \ge 2r-1} p_j L_j}{1 - q}, \qquad\text{so that, by } n p_{2r} L_B = L_A + O(1),\ n p_{2r-1} L_A = \delta L_A = s/10 \text{ and (R3)},$$
$$N\mu' = \nu N - L_A - \tfrac{s}{10} + o(s) \qquad\text{for every } N \in [n - L_A, n]. \tag{1}$$
Let $T_N$ denote a sum of $N$ independent bulk-law variables; its variance is $N C'_r$ with $C'_r = C_r(1 + o(1))$, so for $N \in [n - L_A, n]$ its standard deviation is $s(1 + o(1))$.

*Local limit theorem for $T_N$.* Let $\varphi$ be the characteristic function of a centred bulk summand $X$; $|X| \le 2L_{2r-2}$. Three ranges of $t$. (i) $|t| \le A/s$ with $A = A_r = \Lambda^{1/3}$: since $\mathbb{E}|X|^3 \le 2L_{2r-2}\,\mathbb{E}X^2$, the usual expansion gives $|N\log\varphi(t) + \tfrac12 N\mathbb{E}X^2 t^2| \le C N\mathbb{E}|X|^3|t|^3 \le C L_{2r-2}A^3/s \to 0$ by (R1). (ii) $A/s \le |t| \le 1/L_{2r-2}$: the bulk law has the atom $L_{2r-2}$ with mass $p_{2r-2}$ and the atom $0$ with mass at least $1/3$, so $|\varphi(t)|^2 = \mathbb{E}\cos(t(X - X')) \le 1 - \tfrac23 p_{2r-2}(1 - \cos(tL_{2r-2})) \le 1 - 0.3\,p_{2r-2}L_{2r-2}^2 t^2$ (using $1 - \cos x \ge 0.45x^2$ on $|x| \le 1$), whence $|\varphi(t)|^N \le \exp(-0.15\,N c_{2r-2} t^2) \le \exp(-0.1\,s^2 t^2)$ and $\int_{A/s \le |t| \le 1/L_{2r-2}} |\varphi|^N \le C e^{-0.1A^2}/s = o(1/s)$. (iii) $1/L_{2r-2} \le |t| \le \pi$: the atoms $0$ and $1$ give $|\varphi(t)|^2 \le 1 - \tfrac16(1 - \cos t) \le 1 - t^2/(3\pi^2)$, so $|\varphi|^N \le \exp(-N t^2/(6\pi^2)) \le \exp(-N/(6\pi^2 L_{2r-2}^2))$, and $N/L_{2r-2}^2 \ge e^{40r^2}$ while $\log s \approx 8r^3$, so this range contributes $o(1/s)$ too. Inversion then gives, uniformly in $j$,
$$\mathbb{P}(T_N = j) = \frac{1}{\sqrt{2\pi N C'_r}}\exp\Big(-\frac{(j - N\mu')^2}{2NC'_r}\Big) + o(1/s), \qquad N \in [n - L_A, n]. \tag{2}$$

*Bernstein.* For $N \le n$ and $x > 0$, since the centred summands are bounded by $2L_{2r-2}$ and by (R1) $L_{2r-2}\Lambda/s \to 0$,
$$\mathbb{P}\big(\pm(T_N - N\mu') \ge x\big) \le \exp\Big(-\frac{x^2}{2(NC'_r + 2L_{2r-2}x/3)}\Big) \le e^{-x^2/(3s^2)} \qquad (x \le 2\Lambda s). \tag{3}$$

Now condition on the set $R$ of rare indices and on their values, and decompose $\mathbb{P}(S_n = m)$.

*(a) $R = \emptyset$.* $\mathbb{P}(S_n = m, R = \emptyset) \le \mathbb{P}(T_n = m) \le \mathbb{P}(T_n - n\mu' \ge L_A)$ by (1), which is at most $e^{-\Lambda^2/3}$ by (3).

*(b) $|R| = 1$ and the rare value is $L_A$.* Then $\mathbb{P} = n p_{2r-1}(1-q)^{n-1}\,\mathbb{P}(T_{n-1} = m - L_A)$, and by (1) the point $m - L_A$ lies at distance $s/10 + o(s)$ from $(n-1)\mu'$, so (2) gives $\mathbb{P}(T_{n-1} = m - L_A) \ge c/s$ and
$$\mathbb{P}(S_n = m,\ R = \{i\},\ \xi_i = L_A \text{ for some } i) \ge \delta\,e^{-2nq}\,\frac{c}{s} \ge \frac{c}{20\,\Lambda s}.$$

*(c) Everything else with $R \ne \emptyset$.* Either $|R| \ge 2$, or $|R| = 1$ with value $\ge L_B = rL_A \ge 2L_A$; in both cases the rare summands total at least $2L_A$, so $T_{n-k} = m - (\text{rare total}) \le m - 2L_A$ where $k = |R|$. For $1 \le k \le L_A/(4\nu)$, (1) applies to $N = n - k$ and $m - 2L_A - (n-k)\mu' \le s/10 + o(s) - L_A + k\mu' \le -\tfrac12 L_A$, so by (3) the conditional probability is at most $e^{-\Lambda^2/12}$. For $k > L_A/(4\nu)$, $\mathbb{P}(|R| = k) \le (e\,nq/k)^k \le e^{-k}$, which summed over such $k$ is at most $2e^{-L_A/(4\nu)}$, negligible against everything in sight. Hence the whole of (c) is at most $e^{-\Lambda^2/12} + 2e^{-L_A/(4\nu)}$.

Comparing, the ratio of (a)+(c) to (b) is at most $C\,\Lambda s\,e^{-\Lambda^2/12} + C\Lambda s e^{-L_A/(4\nu)} \to 0$: the first term by (R2) (the exponent $\Lambda^2/12 \approx e^{8r-4}/(12r)$ still beats $\log s \approx 8r^3$ for $r \ge 2$), the second trivially. Therefore, conditionally on $S_n = m$, with probability tending to one there is exactly one rare summand and its size is $L_A = h_r$: $\mathbb{P}(Y_{(1)} \ge h_r) \to 1$. On the independent side, $n\,\mathbb{P}(\xi \ge h_r) = n(p_{2r-1} + p_{2r} + \sum_{j>2r}p_j) = \delta + 1/r + o(1/r) \to 0$ by (R3). $\square$

## Theorem 2: part (iii) fails as well

The mechanism of Theorem 1 supplies mass through a rare atom of exactly the missing size. If instead the rare atom is made slightly too large, by exactly the total mass of a common scale, then the cheapest way to land at $m$ is to have that one rare atom and *no* atom of the common scale at all, since removing a Poisson$(N)$ count entirely costs only $e^{-N}$ while any partial compensation through the remaining bulk costs a Gaussian factor. The conditioned allocation then has no box at a level that the independent model populates with a Poisson$(N)$, $N \to \infty$, number of boxes.

**Construction.** Stages $r = 1, 2, \dots$ are built recursively; the law of $\xi$ is the union of all stages' atoms together with atoms at $1$ and $2$ of masses $a = b = 1/4$. Suppose the atoms of stages $< r$ are fixed and let $V_{r-1}$ be the variance of $\xi$ restricted to those atoms and to $\{0,1,2\}$ (a finite number). Choose $n_r$ so large that $n_r \ge r^6 4^r V_{r-1}$ and $n_r \ge r^{12} n_{r-1}$ (the second condition makes the mean contribution of all later stages to $S_{n_r}$, and the size gap between stage $r$'s atoms and stage $r+1$'s, both negligible at the scale $s_r$ below; since $V_r/V_{r-1}$ is of order $r^5$ through the $B_r$ atom, a weaker power would not do), and put
$$s_r = \sqrt{n_r V_{r-1}}, \quad L_{C,r} = \lceil r\,s_r\rceil, \quad N_r = r, \quad p_{C,r} = N_r/n_r, \quad \Sigma_r = 10\,N_rL_{C,r}, \quad \varepsilon_r = \delta_r = 1/r,$$
$$L_{B,r} = \Sigma_r/\varepsilon_r, \quad p_{B,r} = \varepsilon_r/n_r, \quad L_{A,r} = \Big\lceil \frac{\Sigma_r + N_rL_{C,r}}{1 - \delta_r}\Big\rceil, \quad p_{A,r} = \delta_r/n_r .$$
So at stage $r$ the common top scale $C_r$ appears $N_r = r$ times on average among $n_r$ draws, the rare atom $B_r$ shifts the mean by $\Sigma_r$ and appears with probability about $1/r$, and the rare atom $A_r$ has size $\Sigma_r + N_rL_{C,r} + \delta_rL_{A,r}$ up to rounding, which is exactly the missing mass when no $C_r$ atom is present. The masses $p_{C,r}L_{C,r} \approx r^2\sqrt{V_{r-1}/n_r}$, $p_{A,r}L_{A,r}$ and $p_{B,r}L_{B,r} = \Sigma_r/n_r$ are summable by the growth of $n_r$, so $\nu < \infty$, while $\sum_r p_{C,r}L_{C,r}^2 \ge \sum_r r^3 V_{r-1} = \infty$. Put $m_r = \lfloor \nu n_r\rfloor$ and $h_r = L_{C,r}$.

**Theorem 2.** Along $n = n_r$, $m = m_r$: $n_r\,\mathbb{P}(\xi \ge h_r) \ge N_r = r \to \infty$, while $\mathbb{P}(Y_{(2)} \ge h_r) \to 0$. So Theorem 18.7(iii) fails for $j = 2$, and with it (i) and (iv) (the count of boxes of size at least $h_r$ is $1$ w.h.p. against a Poisson prediction with mean $\ge r$).

*Proof sketch, at the level of detail of Theorem 1.* Fix $r$; call an atom *low* if it belongs to $\{0,1,2\}$ or a stage $< r$ (these form the bulk, $T_N$ a sum of $N$ bulk summands, mean $N\mu'$, standard deviation $s(1+o(1))$ with $s = s_r$), *top* if it is $C_r$, *rare* if it is $A_r$, $B_r$ or belongs to a stage $> r$. As in (1), the mean of $S_n$ splits as $m = n\mu' + N_rL_{C,r} + \Sigma_r + \delta_rL_{A,r} + o(s)$, the $o(s)$ absorbing the later stages by the growth condition on $n_{r+1}$. Condition on the number $k$ of top atoms and on the rare atoms present.

(a) Exactly one $A_r$, no other rare atom, $k = 0$: probability $\ge \delta_r e^{-2/r}\,\mathbb{P}(\mathrm{Poisson}(N_r) = 0)(1 + o(1))\,\mathbb{P}(T_{n-1} = m - L_{A,r})$, and $m - L_{A,r} - (n-1)\mu' = O(1) + o(s)$ lies in the bulk, so by the local limit theorem this is at least $c\,\delta_r e^{-r}/s$.

(b) Exactly one $A_r$, no other rare atom, $k \ge 1$: the bulk must sit at $m - L_{A,r} - kL_{C,r} \le (n-1)\mu' - kL_{C,r} + o(s)$, a downward deviation of $k\,r\,s(1 + o(1))$, so by (3) the probability is at most $\delta_r e^{-r}\sum_{k \ge 1}\frac{r^k}{k!}e^{-k^2r^2/4} \le \delta_r e^{-r}\cdot 2r e^{-r^2/4}$, which is $o$ of (a) times $s$: the ratio to (a) is $O(r s\,e^{-r^2/4}) \to 0$ because $\log s \le \tfrac12\log n_r$ grows only polynomially in $r$ once $n_r$ is chosen as a tower of the stated form, while $e^{-r^2/4}$ does not. (Choosing $n_r$ larger only helps (a) relative to (b) through $\delta_r$, so the growth conditions are compatible.)

(c) No rare atom: the top scale and the bulk must supply $\Sigma_r + \delta_rL_{A,r} \ge 10rL_{C,r}$ above their means; $k$ top atoms supply $(k - r)L_{C,r}$ and the bulk the rest, so either $k \ge 9r$, of probability $\mathbb{P}(\mathrm{Poisson}(r) \ge 9r) \le e^{-r(9\log 9 - 8)}$, or the bulk rises by at least $rL_{C,r}/2 = r^2 s/2$, of probability at most $e^{-r^4/12}$. Both are $o(\delta_r e^{-r}/s)$.

(d) Any $B_r$ atom, any atom of a later stage, or two or more $A_r$ atoms: the overshoot is at least $\Sigma_r(1/\varepsilon_r - 1) \ge 9\Sigma_r$ or at least $L_{A,r} - o(s) \ge 10rL_{C,r}$; the top scale can remove at most $rL_{C,r}$ (all its atoms), so the bulk must fall by at least $8r^2 s$, of probability at most $e^{-64r^4/3}$, times the probability of the rare atoms, again $o(\delta_re^{-r}/s)$.

Summing, conditionally on $S_n = m$ the event "exactly one $A_r$ atom, no top atom, no other rare atom" has probability tending to one; on it $Y_{(1)} = L_{A,r}$ and $Y_{(2)} < L_{C,r} = h_r$. On the independent side $n_r\mathbb{P}(\xi \ge h_r) \ge n_rp_{C,r} = r$. $\square$

The proof is written as a sketch because every step is the same estimate as in Theorem 1 with one more Poisson factor; the exact toy computation of Remark 3 is the check that the bookkeeping of the landing point (in particular the term $\delta_rL_{A,r}$ in the mean, which the first draft omitted and which alone shifts the conditioned count of top atoms from $0$ to about $\delta_rL_{A,r}/L_{C,r}$) is right.

## Remarks

1. **What fails and why it does not contradict the source.** Janson's proof of (ii) runs through $\mathbb{P}(Y_1 = k) = \pi_k\,\mathbb{P}(S_{n-1} = m-k)/\mathbb{P}(S_n = m)$ and the uniform bound $\sup_j \mathbb{P}(S_{n-1} = j) \le C\,\mathbb{P}(S_n = m)$, which is where finite variance is used: with $\sigma^2 < \infty$ the point $m = \nu n + o(\sqrt n)$ is at the centre of $S_n$'s distribution. With $\sigma^2 = \infty$ the mean of $S_n$ can be $\Lambda_r$ standard deviations of the bulk away from the bulk's centre, and $\mathbb{P}(S_n = m)$ is then smaller than $\sup_j \mathbb{P}(S_{n-1} = j)$ by an unbounded factor. Example 18.27 avoids this because regular variation keeps the mean inside the stable bulk.

2. **Part (iii), and a retraction.** The first draft of this memo said that the mechanism could not suppress a common scale, because "the missing mass has to be supplied, not removed". That was wrong: a rare atom that supplies slightly more than the missing mass makes removal necessary, and removing a whole Poisson$(N)$ scale costs $e^{-N}$, which is cheap next to any Gaussian compensation. Theorem 2 is the result; the toy in Remark 3 is what exposed the error, and it also exposed a second one, an omitted $\delta L_A$ in the landing point, which the first run of the toy reported as a conditioned count of three top atoms instead of zero.

3. **A toy version of the mechanism, exact.** For (iii) (`toy_1830_iii.py`): bulk atoms $1$ with mass $0.02$ (and $0$), a common scale $C$ at $L_C = 40$ with $n p_C = 6$, a rare atom $A$ at $L_A = \lceil(\Sigma + 6L_C)/(1 - \delta)\rceil = 2779$ with $n p_A = \delta = 0.05$, a rarer atom $B$ at $L_B = \Sigma/\varepsilon = 48000$ with $n p_B = \varepsilon = 0.05$, $\Sigma = 2400$, $n = 4000$, $m = \lfloor \nu n\rfloor = 2859$. Conditioned on $S_n = m$: exactly one $A$ box with probability $1.0000$ and zero $C$ boxes with probability $1.0000$ (four digits), against the unconditional $\mathbb{P}(\text{no } C\text{ box}) = e^{-6} = 0.0025$ and $\mathbb{E}\,\#C = 6$. The same at $L_C = 60$. With the bulk atoms at $1$ and $2$ of mass $1/4$ each, whose standard deviation $52$ is comparable to $L_C$, the conditioned count of $C$ boxes is $3$ instead of $0$, exactly as the partial-compensation term (b) predicts when $L_C/s$ is not large: the separation $L_C \gg s$ in the construction is what makes the full kill the cheapest route. For (ii), the earlier toy (`toy_1830.py`): Bulk atoms $0,1,2$ with masses $1/2, 1/4, 1/4$ (minus the rare mass), one rare atom $A$ at $L_A$ with $n p_A = \delta$, one rarer atom $B$ at $L_B = L_A/\varepsilon$ with $n p_B = \varepsilon$ (so $B$ shifts the mean by exactly $L_A$), $m = \lfloor \nu n\rfloor$, computed by convolution powers in double precision (`toy_1830.py`):

| $n$ | $L_A$ | $L_B$ | $\delta$ | $\varepsilon$ | $\Lambda = L_A/s$ | $\mathbb{P}(Y_{(1)} \ge L_A \mid S_n = m)$ | $n\,\mathbb{P}(\xi \ge L_A)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4000 | 250 | 5000 | 0.05 | 0.05 | 4.8 | 0.9999 | 0.100 |
| 4000 | 400 | 8000 | 0.05 | 0.05 | 7.6 | 1.0000 | 0.100 |
| 8000 | 600 | 20000 | 0.03 | 0.03 | 8.1 | 1.0000 | 0.060 |

In every row the conditional probability of the $A$-box is carried entirely by the "exactly one $A$" term, as in step (b) of the proof. A fixed $n$ is not a sequence; the table shows the mechanism, and the theorem is proved above.

## Status

Mathematics: complete for (ii) (Theorem 1, every step written out) and complete at sketch level for (iii) (Theorem 2, the same estimates with one more Poisson factor, checked exactly on a toy), author checked; inputs are Bernstein's inequality for bounded summands and a local limit theorem for a triangular array with vanishing Lyapunov ratio, both classical. Verification word: author checked, no independent read, one retracted claim recorded in place. Prior art: none found in a bounded search; not a clearance. Ledger row F0058 should move from `attempted_unsolved` to `refuted: both (ii) and (iii) fail`.
