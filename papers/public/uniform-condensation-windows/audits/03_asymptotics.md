# Audit 3: record sums, margins, and the uniform limit

**Outcome: no unresolved step identified in the asymptotic argument.**

This pass rederived the deterministic summations and followed all constants through the probability estimate. It was performed by the same assistant as the other passes and is not independent certification.

## Record envelope and plateaus

Zero radius implies that the corrected slopes $(\log w_s+b\log s)/s$ are unbounded. Their geometric prefix maxima $B_i$ therefore increase without bound, and the least maximizing supported sizes $s_i$ tend to infinity. At an active scale $J$, $a^{J-1}<s_J\le a^J$. On an inactive scale the least maximizer cannot change: any newly available tied index is larger than the previous least maximizer. Thus the penalty $p_i=b\log(s_i)/s_i$ really is constant on each plateau.

For a plateau beginning at $\ell$ and ending just before the next active scale $v$, only active $J\ge v$ can receive a charge from that plateau. Bounding their total by

$$
p_\ell\left(\sum_{i=\ell}^{v-1}a^i\right)
\left(\sum_{J=v}^{\infty}a^{-J}\right)
\le \frac{a}{(a-1)^2}p_\ell
$$

is valid even for arbitrarily long plateaus. At active $\ell$, the bound $p_\ell\le ba\ell(\log a)a^{-\ell}$ is summable. The initial plateau contributes one finite term. Charging at all scales instead of active scales would lose this reasoning; the manuscript retains the active-scale restriction.

## Kernel and finite prefix

Expanding $B_{J-1}-B_i$ into nonnegative increments allows rearrangement. At lag $t=J-\ell$, the coefficient of one increment before multiplication by $2a^2$ is $a^{1-D}/(a-1)$ for $1\le t\le D-1$, and $a^{-t}/(a-1)$ for $t\ge D$. Summing gives exactly the manuscript's $\Theta(a,D)$, which tends to zero as $D$ grows for each fixed $a>1$.

The terminal term is not discarded. Beyond a fixed $J_0$, its contribution from later increments is at most $\kappa\sum d_\ell$, with $\kappa=Ma^{1-J_0}/(a-1)$. The earlier increments contribute only a fixed finite constant. Choosing $D$ first and $J_0$ later makes both coefficients less than $1/4$. This forces bounded record growth if the favorable margins were eventually bounded above, contradicting zero radius.

The finite-prefix inequality was also rederived from $G_J/s_J=d_J-(b\log s_J+E_J)/s_J$. The negative margins are retained in the weighted sum; they are not silently dropped. The error terms have the displayed geometric upper bounds. Bounding the positive maximum using the finite total $\sum s_J^{-1}\le T_{J_0}$ gives the stated quantitative consequence.

## Uniform probability estimate

The auxiliary probabilities use only sizes up to the preceding record cutoff. The bound $q_j\le j^{-b}$ and $b>2$ supply a summable first-moment majorant. For each fixed positive $j$, $w_j e^{-B_{J-1}j}$ tends to zero, so the auxiliary mean tends to zero by dominated convergence. No asymptotic equivalence of the original and truncated models is assumed.

The upper density and lower density bounds ensure that all relevant box counts are of order $k$, uniformly. A Markov bound and a finite pigeonhole argument select a background mass $t\le\delta k$ with probability at least $1/(2(\lfloor\delta k\rfloor+1))$. The exact residual satisfies $2\delta k\le r\le5\delta k$ and is represented by the greedy construction. The insertion conditions are guaranteed by the explicitly fixed $K$ and $\delta$.

Both the numerator upper bound and the inserted denominator contain the *same* factor $A_J^n$. They cancel exactly. The leftover prefactor is bounded by the displayed constant independent of both $m$ and $n$ in the window. The entire failure probability is therefore bounded by $Ce^{-G_J}$. Selecting margins tending to infinity proves the uniform theorem. The gcd reduction preserves the ratio of maximum to total and rescales the density interval correctly.

## Quantifiers and tests

The order is: fix the law, accuracy and density interval; then fix $a,b,D,\delta,K$ and the finite terminal data; only then select record scales. The final diagonal selection over accuracies is separate. No law varies with the selected size, and no almost-sure assertion is inferred from convergence in probability.

All 412 prior finite-prefix inequalities were reproduced. The new checker verified 84 exact geometric and tail identities, including bases $101/100$ and lag boundaries $D=2,3,11$. The prior long-plateau and convolution tests also passed. No numerical tail truncation is used to justify an infinite sum.
