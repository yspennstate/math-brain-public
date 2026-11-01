# The layer distribution of a random recursive tree: the conjectured tail is a theorem about the Poisson-weighted infinite tree

Ledger row H0019 (intake H). Source: H. Stepanyants, P. L. Krapivsky, H. Hartle and D. Krioukov, *The rank and layer distributions in random recursive trees*, arXiv:2608.04303, Conjecture 1 (and Conjecture 2). Written 14 September 2026, between about 05:00 and 06:15.

## The conjecture

Strip the leaves off a tree, then strip the leaves off what is left, and so on. The *layer* of a vertex is the number of rounds after which it is a leaf. Let $\ell_k$ be the limiting fraction of vertices at layer $k$ in a random recursive tree, and $\bar\ell_k = \sum_{j \ge k}\ell_j$. The authors prove (their Theorem 2)
$$\bar\ell_k = \int_0^\infty s_k(y)\,e^{-y}\,dy, \qquad s_0 \equiv 1, \quad s_i(y) = 1 - \exp\Big(-\int_0^y s_{i-1}(y')\,dy'\Big), \tag{1}$$
and, by hand, that $e^{-k} \lesssim \bar\ell_k \lesssim e^{-k/e}$ (their Theorem 4). Appendix A then treats (1) as a travelling wave: the front $y_f(k)$ (defined there as the median level $s_k(y_f) = 1/2$) moves at the velocity $v$ solving $e^{av} = a$, which is bounded by $1/e$; they assert that the extremal velocity $v^* = 1/e$ is selected, remark that "its rigorous characterization remains an open problem", and, quoting the universal Bramson form $\tfrac{3}{2a^*}\log k$ with $a^* = e$, conjecture $y_f(k) = k/e + \tfrac{3}{2e}\log k + O(1)$, hence

**Conjecture 1.** $\ell_k = \exp\big[-\tfrac1e k - \tfrac{3}{2e}\log k - O(1)\big]$.

**Conjecture 2.** The maximum layer in a random recursive tree on $n$ vertices is $L \approx e\log n - \tfrac32\log\log n$ (and the maximum rank is $R \approx \tfrac12\log n/\log\log n$).

## What is really going on: the recursion is a branching random walk

Let $\mathcal T$ be the Poisson-weighted infinite tree: the root is at $0$, its children sit at the points of a rate-one Poisson process on $(0,\infty)$, and each child in turn has children at the points of an independent rate-one Poisson process on $(0,\infty)$ relative to itself. Let $M_k$ be the smallest position at generation $k$.

**Theorem 1.** For every $k \ge 0$ and $y \ge 0$, $s_k(y) = \mathbb{P}(M_k \le y)$. Consequently
$$\bar\ell_k = \mathbb{E}\big[e^{-M_k}\big], \qquad \ell_k = \mathbb{E}\big[e^{-M_k} - e^{-M_{k+1}}\big].$$

*Proof.* Put $u_i = 1 - s_i$, so that (1) reads $u_i(y) = \exp(-\int_0^y (1 - u_{i-1}(y'))dy')$ with $u_0 \equiv 0$. Let $F_i(y) = \mathbb{P}(M_i > y)$. Then $F_0(y) = 0$ for $y \ge 0$, and conditioning on the first generation $\xi_1, \xi_2, \dots$, which is a rate-one Poisson process on $(0,\infty)$, and on the independent copies of the tree hanging from each child,
$$F_i(y) = \mathbb{E}\Big[\prod_j F_{i-1}(y - \xi_j)\Big] = \exp\Big(-\int_0^\infty \big(1 - F_{i-1}(y-t)\big)dt\Big) = \exp\Big(-\int_0^y \big(1 - F_{i-1}(y')\big)dy'\Big),$$
by the Poisson product formula, the integral being over $(0,y)$ only because $F_{i-1}(z) = 1$ for $z < 0$ ($M_{i-1} \ge 0$). This is the recursion for $u_i$, and the two agree at $i = 0$, so $F_i = u_i$ for all $i$. The second display follows since $\int_0^\infty \mathbb{P}(M_k \le y)e^{-y}dy = \mathbb{E}\int_{M_k}^\infty e^{-y}dy = \mathbb{E}[e^{-M_k}]$; and $M_k < M_{k+1}$ always, because every vertex of generation $k+1$ lies strictly above its parent. $\square$

So the travelling wave of Appendix A is the front of a branching random walk, the waveform is the distribution function of $M_k$, and the "selected velocity" is the speed of its minimum. That walk is not a generic one. It is the walk whose displacement vector has *exponential steps* (the $j$-th child sits at the sum of $j$ independent exponentials), which is exactly the class treated by Addario-Berry and Ford, *Poisson–Dirichlet branching random walks*, Ann. Appl. Probab. 23 (2013) 283–307. Their Theorem 1.1 states, for this class,
$$\widetilde M_n := \mathrm{median}(M_n) = \frac ne + \frac{3}{2e}\log n + O(1), \tag{2}$$
uniformly over the class, and their Theorem 1.2 gives uniform exponential tails: for every $c_1 < e$ and $c_2 < 1$,
$$\mathbb{P}\big(M_n \le \widetilde M_n - x\big) \ll_{c_1} e^{-c_1 x}, \qquad \mathbb{P}\big(M_n \ge \widetilde M_n + x\big) \ll_{c_2} e^{-c_2 x} \qquad (n \ge 1,\ x \ge 0). \tag{3}$$
Equation (2) is precisely the conjectured (A12), velocity selection included.

## Conjecture 1 is a theorem

**Theorem 2.** There are absolute constants $0 < c < C < \infty$ with
$$c \le \bar\ell_k\,e^{k/e}\,k^{3/(2e)} \le C \qquad (k \ge 1),$$
that is, $\bar\ell_k = \exp[-k/e - \tfrac{3}{2e}\log k - O(1)]$. The same holds for $\ell_k$, so Conjecture 1 holds as stated.

*Proof.* Write $D_k = M_k - \widetilde M_k$, so $\bar\ell_k = e^{-\widetilde M_k}\,\mathbb{E}[e^{-D_k}]$ by Theorem 1. For the upper bound take $c_1 = 2$ in (3), which is legitimate since $2 < e$: with $K$ the implied constant,
$$\mathbb{E}[e^{-D_k}] \le 1 + \sum_{j\ge 0} e^{\,j+1}\,\mathbb{P}(D_k \le -j) \le 1 + eK\sum_{j \ge 0}e^{-j} < \infty,$$
uniformly in $k$. For the lower bound, $\mathbb{E}[e^{-D_k}] \ge \mathbb{P}(D_k \le 0) \ge 1/2$ by the definition of the median. Now insert (2). For $\ell_k$: the upper bound is immediate from $\ell_k \le \bar\ell_k$, and the lower bound follows from Theorem 3 below; unconditionally it already follows for a positive density of $k$, since summing the telescoping identity $\sum_{k=j}^{j+L-1}\ell_k = \bar\ell_j - \bar\ell_{j+L}$ and choosing $L$ with $e^{-L/e} \le c/(2C)$ gives some $k \in [j, j+L)$ with $\ell_k \ge (c/2L)\,e^{-j/e}j^{-3/(2e)}$. $\square$

**Theorem 3.** $\bar\ell_k\,e^{k/e}k^{3/(2e)} \to C^* \in (0,\infty)$ and $\ell_k\,e^{k/e}k^{3/(2e)} \to (1 - e^{-1/e})\,C^*$.

*Proof.* Aïdékon, *Convergence in law of the minimum of a branching random walk*, Ann. Probab. 41 (2013), gives $M_k - (k/e + \tfrac{3}{2e}\log k) \Rightarrow M^*$ for a class of walks that includes this one (Addario-Berry and Ford say so explicitly in their Remark 2). The family $e^{-(M_k - \widetilde M_k)}$ is uniformly integrable by the computation above with $c_1 = 2 > 1$, so the exponential moments converge: $\bar\ell_k e^{k/e}k^{3/(2e)} \to C^* := \mathbb{E}[e^{-M^*}] \in (0,\infty)$. Then $\bar\ell_{k+1}/\bar\ell_k \to e^{-1/e}$ and $\ell_k = \bar\ell_k - \bar\ell_{k+1}$. $\square$

This is stronger than the conjecture: the $O(1)$ is a genuine limit, and the constant is the exponential moment of the limiting minimum, $C^* = \mathbb{E}[e^{-M^*}]$, which numerically is about $1.4$ (see below). The constant in front of $\ell_k$ is $(1 - e^{-1/e})C^* \approx 0.44$.

Two remarks on the paper's Theorem 4, whose bounds were $e^{-k} \lesssim \bar\ell_k \lesssim e^{-k/e}$. Under the dictionary the upper bound is the first-moment bound on the branching random walk and is sharp to the exponential order; the lower bound $e^{-k}$ is the contribution of a single spine, which undershoots by the factor $e^{-k(1 - 1/e)}$.

## Conjecture 2, the layer half

Let $L_n$ be the largest layer in a random recursive tree $T_n$ on $n$ vertices.

**Theorem 4.** $L_n = e\log n - \tfrac32\log\log n + O_{\mathbb P}(1)$.

*Proof.* First, a deterministic identity: for a finite tree, the layer of $v$ is the second largest of the branch heights at $v$ (the branch at a neighbour $u$ needs $h$ rounds to vanish, where $h$ is its height counted with the single vertex as height one; $v$ becomes a leaf when all but one of its branches are gone), and therefore $L_n = \lfloor \mathrm{diam}(T_n)/2\rfloor$, the two maxima being attained at a centre of the tree.

Upper bound: any path has length at most twice the height $H_n$ measured from the root, so $L_n \le H_n$, and Addario-Berry and Ford's Corollary 1.3 gives $H_n = e\log n - \tfrac32\log\log n + O_{\mathbb P}(1)$ (their statement is for $\mathbb{E}H_n$ together with exponential concentration).

Lower bound: the subtree sizes at the root of a random recursive tree, normalised by $n$, converge to a stick-breaking sequence whose second largest term is almost surely positive, so for every $\delta > 0$ there is $\varepsilon > 0$ such that with probability at least $1 - \delta$ two of the root's subtrees have at least $\varepsilon n$ vertices each. Conditionally on its size, each such subtree is itself a random recursive tree, so each has height $e\log n - \tfrac32\log\log n + O_{\mathbb P}(1)$, and the path joining their two deepest vertices through the root gives $\mathrm{diam}(T_n) \ge 2e\log n - 3\log\log n - O_{\mathbb P}(1)$. $\square$

So the maximum layer has the same first two orders as the height: to this precision the root of a random recursive tree is a centre of it, because its two largest subtrees are both of linear size and a linear-size random recursive tree loses only $O(1)$ of height. The rank half of Conjecture 2 is a different mechanism (the distance to the nearest leaf) and is not settled here.

## Numerical check

`h0019_layers.py` and `h0019_front.py` integrate (1) on a grid, the second in a window that tracks the front (kept $45$ below it, where $s_k < e^{-100}$, so nothing is carried across the shifts) and uses $-\mathrm{expm1}$ to avoid the cancellation in $1 - e^{-S}$ at small $S$.

Positive control: the scheme returns $\bar\ell_1 = 0.500000$ and $\bar\ell_2 = 0.281718$ against the paper's exact $1/2$ and $3 - e = 0.2817181\ldots$, and $\bar\ell_{60}$ agrees to five digits at step sizes $0.002$, $0.001$ and $0.0005$.

| $k$ | $\bar\ell_k$ | median $M_k$ | $-\,k/e - \frac{3}{2e}\log k$ | $-\,k/e - \frac12\log k$ | $b_k$ |
|---|---|---|---|---|---|
| 50 | 1.34e-09 | 21.134 | 0.581 | 0.784 | 1.131 |
| 100 | 9.75e-18 | 39.890 | 0.561 | 0.799 | 1.174 |
| 330 | 9.61e-55 | 125.112 | 0.511 | 0.812 | 1.247 |
| 990 | 1.96e-160 | 368.478 | 0.471 | 0.829 | 1.303 |

Here $b_k = \bar\ell_k e^{k/e}k^{3/(2e)}$, which Theorem 2 says is bounded and Theorem 3 says converges. It is still climbing at $k = 990$, but its local exponent $d\log b_k/d\log k$ falls from $0.054$ near $k = 60$ to $0.036$ near $k = 800$, so $b_k$ is not a power of $k$; the decay of that exponent matches a correction of size $(\log k)/\sqrt k$, which is the usual finite-$k$ correction for these fronts, with coefficient about $0.39$, and extrapolating on it gives $C^* \approx 1.42$. The same slow correction means the front data at $k \le 1000$ do not by themselves separate the coefficient $3/(2e) = 0.5518$ from $1/2$: differencing the measured median gives a local coefficient of about $0.515$ at $k \approx 10^3$. The separation comes from (2), not from the numerics; what the numerics do is confirm the dictionary of Theorem 1 and show the two-sided bound of Theorem 2 holding with $c \approx 0.7$, $C \approx 1.5$ over three decades of $\bar\ell_k$ spanning $10^{-160}$.

The measured left tail supports $\lambda^* = e$: $-\log s_k(\widetilde M_k - x)/x$ is $1.932$ at $x = 5$ and $2.404$ at $x = 15$ for $k = 990$, rising with $x$ as it must for a tail $\asymp x e^{-ex}$, and already above $2$, which a tail $\asymp x e^{-2x}$ could not produce.

Those checks all run through the recursion, which is the paper's, so they cannot test Theorem 1. That test is a direct simulation of the tree with no recursion in it (`h0019_mc.py`): the Poisson-weighted infinite tree is grown generation by generation below a cutoff $Y = 10$, which loses nothing since displacements are positive and a particle above $Y$ has no descendant below it, and the minimum is read off; 4000 replicates.

| $k$ | $\mathbb{P}(M_k \le 3)$ simulated | $s_k(3)$ | $\mathbb{E}[e^{-M_k}]$ simulated | $\bar\ell_k$ |
|---|---|---|---|---|
| 2 | 0.8655 ± 0.0054 | 0.8712 | 0.281428 | 0.281718 |
| 5 | 0.4410 ± 0.0079 | 0.4388 | 0.064585 | 0.064579 |
| 10 | 0.0100 ± 0.0016 | 0.0090 | 0.007570 | 0.007382 |
| 12 | 0.0008 ± 0.0004 | 0.0007 | 0.003361 | 0.003232 |

Every entry agrees within about one and a half standard errors, and at $k = 5$ the exponential moment agrees to five digits.

The two combinatorial claims inside Theorem 4 were also checked by brute force (`h0019_layer_identity.py`), stripping leaves literally on 40 random recursive trees of sizes 6 to 120: the layer of a vertex equalled the second largest branch height at it in all 480 vertices tested, and the maximum layer equalled $\lfloor \mathrm{diam}/2\rfloor$ and was at most the height in all 40 trees, with the path on five vertices as a control (maximum layer 2, not 4). The convention for the last vertex left standing moves the maximum layer by at most one, which Theorem 4 absorbs.

## Status

Conjecture 1: proved, in the stronger form of Theorem 3. Conjecture 2: the layer half proved (Theorem 4), the rank half untouched. The mathematics is complete given the two cited theorems; everything else is written out. Verification: author checked; the recursion is integrated exactly against two published closed-form values as a control. Prior art: the paper cites Bramson and the physics travelling-wave literature but not Addario-Berry and Ford, Aïdékon or Devroye's height theorem in this connection, and states the velocity selection as open; a bounded search found no paper making the identification of Theorem 1. Not a clearance. Ledger row H0019 should move from `unverified` to `proved`.

## New open problems

1. **The constant.** Is there a closed form for $C^* = \mathbb{E}[e^{-M^*}]$, the exponential moment of the limiting minimum of the Poisson-weighted infinite tree? By Aïdékon's description of $M^*$ through the derivative martingale $\partial W$ of this walk, $C^*$ is $\mathbb{E}[(\partial W)^{1/e}]$ up to explicit factors; the numerics give $C^* \approx 1.42$ and $\ell_k \approx 0.44\,e^{-k/e}k^{-3/(2e)}$.
2. **The next correction.** The numerics show the approach to the limit is of order $(\log k)/\sqrt k$ with coefficient about $0.39$. Is $\bar\ell_k e^{k/e}k^{3/(2e)} = C^*(1 - \alpha(\log k)/\sqrt k + o(\log k/\sqrt k))$, and what is $\alpha$? The analogous refinement is known for branching Brownian motion but not, as far as I could find, for the minimum of a branching random walk with exponential steps.
3. **The maximum rank.** Prove the rank half of Conjecture 2, $R_n \sim \tfrac12\log n/\log\log n$. The paper's Theorem 3 gives the rank distribution $r_k = \exp[-2k\log k + 2(1-\log 2)k + O(\log k)]$; the first moment then predicts the answer, and what is missing is a second-moment or branching argument, complicated by the fact that high-rank vertices are far from independent.
4. **Layers of other increasing trees.** The dictionary of Theorem 1 turns a leaf-stripping question into a branching random walk with exponential steps. For preferential attachment trees the analogous walk has a different displacement law, and the height is known (Pain and Sénizergues, for weighted recursive trees and preferential attachment with additive fitness). Does the layer distribution of the plane-oriented recursive tree satisfy $\bar\ell_k = \exp[-\gamma k - \tfrac{3}{2\lambda^*}\log k - O(1)]$ with $\gamma$ and $\lambda^*$ read off the same way?
