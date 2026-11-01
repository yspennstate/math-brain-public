# Janson's Conjecture 20.1: the level widths of a conditioned Galton–Watson tree are uniformly integrable of every order the offspring law allows

Ledger row F0063 (intake F). Source: S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Section 20.1. Written 14 September 2026, 03:35 to about 04:10.

## The conjecture

Let $T_n$ be the simply generated tree with $n$ vertices for a weight sequence $w$ with $\rho > 0$, $\nu = \Psi(\rho)$, $\pi$ the tilted law with mean $\min(\nu, 1)$, $\sigma^2$ its variance, $\widehat T$ the limit tree of Theorem 7.1, and $\ell_k(T)$ the number of vertices at depth $k$. Section 20.1 shows $\ell_k(T_n) \to_d \ell_k(\widehat T) \le \infty$ for every $k$ and, by Fatou, $\mathbb{E}\,\ell_k(T_n)^r \to \mathbb{E}\,\ell_k(\widehat T)^r = \infty$ whenever the right side is infinite, which is the case if $0 < \nu < 1$ or (for $\nu \ge 1$) $\mathbb{E}\xi^{r+1} = \infty$. The only case at issue is therefore $\nu \ge 1$ with $\mathbb{E}\xi^{r+1} < \infty$, where [59, Theorem 1.13] gives that the moments $\mathbb{E}\,\ell_k(T_n)^r$ are uniformly bounded for integer $r$.

**Conjecture 20.1.** For every integer $r \ge 1$ and every $k \ge 1$, if $\nu > 0$ then $\mathbb{E}\,\ell_k(T_n)^r \to \mathbb{E}\,\ell_k(\widehat T)^r \le \infty$; and the same for non-integer $r > 0$.

## Result

**Theorem.** Let $\nu \ge 1$, $k \ge 1$ and $r \ge 1$ real, and suppose $\mathbb{E}\xi^{r+1} < \infty$. Then $\{\ell_k(T_n)^r\}_n$ is uniformly integrable, and hence $\mathbb{E}\,\ell_k(T_n)^r \to \mathbb{E}\,\ell_k(\widehat T)^r < \infty$.

Consequently Conjecture 20.1 holds for every integer $r \ge 1$ and, more generally, for every real $r \ge 1$; for $0 < r < 1$ it holds whenever $\sigma^2 < \infty$ (then $\ell_k(T_n)$ itself is uniformly integrable by the case $r = 1$, and so is any smaller power). The one case the theorem leaves open is $0 < r < 1$, $\nu = 1$, $\sigma^2 = \infty$, $\mathbb{E}\xi^{r+1} < \infty$.

Note that for real $r \ge 1$ the hypothesis $\mathbb{E}\xi^{r+1} < \infty$ forces $\sigma^2 < \infty$, and that for $\nu > 1$ the tilted law has exponential moments, so $\sigma^2 < \infty$ throughout the theorem.

## Proof

Write $n$ for the tree sizes along which $T_n$ is defined ($n \equiv 1 \pmod{\text{span}}$) and $S_M$ for the sum of $M$ i.i.d. copies of $\xi \sim \pi$, so $\mathbb{E}\xi = 1$ and $\sigma^2 < \infty$. Two facts about $S_M$: by the local limit theorem for lattice laws with finite variance,
$$\mathbb{P}(S_n = n - 1) \ge c\,n^{-1/2} \quad\text{for all admissible } n, \qquad \sup_j \mathbb{P}(S_M = j) \le C\,M^{-1/2} \quad\text{for all } M \ge 1, \tag{1}$$
with $c, C > 0$ depending on $\pi$ only (the second holds for large $M$ by the same theorem and for the remaining $M$ trivially).

*The weight of a truncated tree.* Let $t$ be a finite plane tree whose vertices of depth less than $k$ have prescribed outdegrees and whose vertices at depth $k$ are leaves of $t$ with unspecified subtrees; call the former the interior $I(t)$, put $N = |I(t)| = 1 + \ell_1(t) + \dots + \ell_{k-1}(t)$ and $\ell = \ell_k(t)$. Let $T^{(k)}$ denote a tree truncated at depth $k$. For $\ell \ge 1$ and $n > N$, Lemma 14.9 of the survey (with the interior vertices as $v_1, \dots, v_N$ in depth-first order, $\sum_{i \le N} d_i = N - 1 + \ell$) gives
$$\mathbb{P}\big(T_n^{(k)} = t\big) = \ell\,\frac{n}{n - N}\,\mathbb{P}(Y_i = d_i,\ i \le N),$$
where $(Y_1, \dots, Y_n)$ is the allocation $B_{n-1,n}$, i.e. $n$ i.i.d. copies of $\xi$ conditioned on $S_n = n - 1$; so
$$\mathbb{P}\big(T_n^{(k)} = t\big) = \mathbb{P}_{\mathrm{GW}}\big(T^{(k)} = t\big)\;W_n(t), \qquad W_n(t) := \frac{n\,\ell\;\mathbb{P}(S_{n-N} = n - N - \ell)}{(n - N)\;\mathbb{P}(S_n = n - 1)}, \tag{2}$$
with $\mathbb{P}_{\mathrm{GW}}(T^{(k)} = t) = \prod_{v \in I(t)}\pi_{d(v)}$ the probability that the first $k$ generations of the unconditioned Galton–Watson tree $T$ are $t$. (The formula is also the cycle lemma applied to the forest of $\ell$ subtrees with $n - N$ vertices in total; the survey proves it from Lemma 14.3.) If $\ell = 0$ then $t$ is a whole tree and contributes nothing to any expectation of $\ell_k^r$ on $\{\ell_k \ge 1\}$, so it can be ignored.

Two bounds follow from (1) and (2). First,
$$W_n(t) \le \frac{n\,\ell\,C (n-N)^{-1/2}}{(n-N)\,c\,n^{-1/2}} = C'\,\ell\Big(\frac{n}{n-N}\Big)^{3/2}, \qquad C' = C/c. \tag{3}$$
Second, since the $\ell$ vertices at depth $k$ are among the $n - N$ vertices outside the interior, $n - N \ge \ell$, and so
$$W_n(t) \le C'\,n^{3/2}\,\ell^{-1/2}. \tag{4}$$

*Moments of generation sizes of the unconditioned tree.* For $s \ge 1$ and $Z_j := \ell_j(T)$: given $Z_{j-1} = m$, $Z_j$ is a sum of $m$ i.i.d. copies of $\xi$, so by Minkowski $\mathbb{E}[Z_j^s \mid Z_{j-1} = m] \le m^s\,\mathbb{E}\xi^s$, hence $\mathbb{E} Z_j^s \le (\mathbb{E}\xi^s)^j < \infty$ when $\mathbb{E}\xi^s < \infty$. Likewise $\mathbb{E}[Z_k^s \mid Z_j = m] \le m^s(\mathbb{E}\xi^s)^{k-j}$ for $s \ge 1$, and for $0 < s < 1$ by Jensen $\mathbb{E}[Z_k^s \mid Z_j = m] \le (\mathbb{E}[Z_k \mid Z_j = m])^s = m^s$ (mean one). So in all cases, for $0 < s \le r + 1$,
$$\mathbb{E}[Z_k^s \mid Z_j = m] \le C_s\,m^s. \tag{5}$$

*Uniform integrability.* Fix $K > 1$. By (2),
$$\mathbb{E}\big[\ell_k(T_n)^r;\ \ell_k(T_n) > K\big] = \mathbb{E}_{\mathrm{GW}}\big[Z_k^r\,W_n(T^{(k)});\ Z_k > K\big],$$
where on the right $N = N_k := 1 + Z_1 + \dots + Z_{k-1}$ is the number of vertices of $T$ of depth less than $k$. Split according to $N_k \le n/2$ or $N_k > n/2$.

On $\{N_k \le n/2\}$, (3) gives $W_n \le 2^{3/2}C' Z_k$, so this part is at most
$$2^{3/2}C'\;\mathbb{E}_{\mathrm{GW}}\big[Z_k^{r+1};\ Z_k > K\big],$$
which does not depend on $n$ and tends to $0$ as $K \to \infty$ because $\mathbb{E} Z_k^{r+1} \le (\mathbb{E}\xi^{r+1})^k < \infty$.

On $\{N_k > n/2\}$, (4) gives $Z_k^r W_n \le C' n^{3/2} Z_k^{r - 1/2}$, and $N_k > n/2$ forces $Z_j > n/(2k)$ for some $1 \le j \le k - 1$ when $n > 2k$ (the root alone cannot do it). So this part is at most
$$C' n^{3/2}\sum_{j=1}^{k-1}\mathbb{E}_{\mathrm{GW}}\big[Z_k^{r-1/2};\ Z_j > n/(2k)\big] \le C' C_{r-1/2}\,n^{3/2}\sum_{j=1}^{k-1}\mathbb{E}_{\mathrm{GW}}\big[Z_j^{r-1/2};\ Z_j > n/(2k)\big]$$
by (5) with $s = r - 1/2 \in [1/2, r+1]$, and on $\{Z_j > n/(2k)\}$ we have $Z_j^{r-1/2} \le (2k/n)^{3/2} Z_j^{r+1}$, so the whole thing is at most
$$C' C_{r-1/2}\,(2k)^{3/2}\sum_{j=1}^{k-1}\mathbb{E}_{\mathrm{GW}}\big[Z_j^{r+1};\ Z_j > n/(2k)\big] \longrightarrow 0 \quad (n \to \infty),$$
again because $\mathbb{E} Z_j^{r+1} < \infty$. This part does not depend on $K$ at all.

Hence $\limsup_{n}\mathbb{E}[\ell_k(T_n)^r; \ell_k(T_n) > K] \le 2^{3/2}C'\,\mathbb{E}_{\mathrm{GW}}[Z_k^{r+1}; Z_k > K] \to 0$ as $K \to \infty$, and since each $\mathbb{E}\,\ell_k(T_n)^r$ is finite (a finite tree), the family $\{\ell_k(T_n)^r\}$ is uniformly integrable. Together with $\ell_k(T_n) \to_d \ell_k(\widehat T)$, (20.1) of the survey, this gives $\mathbb{E}\,\ell_k(T_n)^r \to \mathbb{E}\,\ell_k(\widehat T)^r$, and the limit is finite because the moments are bounded. $\square$

## Remarks

1. The proof is the root-degree argument of Theorem 7.10 pushed down $k$ levels: the conditioning multiplies the Galton–Watson weight of the first $k$ generations by $W_n$, and $W_n$ is at most a constant times $\ell_k$ as long as the first $k$ generations do not contain a positive fraction of the tree, which happens with probability $O(n^{-(r+1)})$ by the $(r+1)$-th moment. The same $W_n \le C'\ell_k(n/(n-N))^{3/2}$ shows why $\mathbb{E}\xi^{r+1}$ is the right condition: the size-biasing by $\ell_k$ costs exactly one moment, and nothing else is lost.
2. The open case $0 < r < 1$, $\nu = 1$, $\sigma^2 = \infty$ is not a matter of the argument but of (1): with infinite variance there is no general lower bound on $\mathbb{P}(S_n = n - 1)$ in terms of $\sup_j \mathbb{P}(S_{M} = j)$ for $M$ between $n/2$ and $n$; the mean-versus-centre phenomenon of the F0058 memo shows the ratio can be far from bounded for lacunary laws, and it is exactly for such laws that the question is not settled here. The size-biasing heuristic suggests the conjecture still holds: for the F0058-type law with a rare atom of size $\Lambda_n = n^a$ and mass $n^{-1}$ at stage $n$, $\mathbb{E}\,\ell_1(T_n)^r \gtrsim \Lambda_n^{r+1}/n = n^{a(r+1)-1}$ diverges exactly when $a(r+1) > 1$, which is exactly when $\mathbb{E}\xi^{r+1} = \infty$.
3. The conjecture's integer-$r$ case, which is the one the survey states first, is covered in full, without the extra moment $\mathbb{E}\xi^{r+2} < \infty$ that the survey notes would suffice by [59].

## Status

Mathematics: complete for all real $r \ge 1$ and for $r \in (0,1)$ with $\sigma^2 < \infty$; author checked; the inputs are Lemma 14.9 of the survey, the local limit theorem for lattice laws with finite variance, and Minkowski's and Jensen's inequalities. The case $0 < r < 1$, $\sigma^2 = \infty$ is open. Verification word: author checked, no independent read. Prior art: a bounded search ("Conjecture 20.1", level widths, uniformly integrable, conditioned Galton–Watson) found nothing; not a clearance. Ledger row F0063 should move from `unverified` to `proved (r >= 1; and r in (0,1) when the variance is finite)`.

## New open problem

For $\nu = 1$, $\sigma^2 = \infty$, $0 < r < 1$ and $\mathbb{E}\xi^{r+1} < \infty$: is $\ell_k(T_n)^r$ uniformly integrable? Equivalently, is $\sup_n\sum_{d} d^{r+1}\pi_d\,\mathbb{P}(S_{n-1} = n - 1 - d)/\mathbb{P}(S_n = n - 1) < \infty$ for $k = 1$? A lacunary law of the F0058 type with the rare atom's size tuned to $\mathbb{E}\xi^{r+1} < \infty$ is the natural test, and the heuristic of Remark 2 says it passes.
