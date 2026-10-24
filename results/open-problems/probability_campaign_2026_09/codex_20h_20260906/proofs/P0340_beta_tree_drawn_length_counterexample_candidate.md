# P0340: The proposed drawn-length growth is incompatible with an exact tree bound

Status: author-checked candidate counterexample to the literal proposed rate, not a certified original result. No independent reviewer has checked this packet. Later-literature search is bounded, not a novelty certificate. The argument below also derives a positive finite linear-order expectation limit. Its constant is an explicit convergent series of finite-tree mean heights, not a closed-form numerical value.

Primary source: Aldous and Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, manuscript dated April 17, 2025; PDF pages 4, 12, 28-29, 54-56. Source PDF SHA256: a93a520bc7e7f1579802bfb87ac8888712aadd5906c0980ca15d2efd4fa7735d. URL: https://arxiv.org/abs/2303.02529v3.

Open Problem 14 proposes that the expected drawn length grows on the scale $n(\log n)^4$. This packet disproves that scale under the exact drawing convention and recursion in source equations (72)-(73). The paper's ordinary random-leaf depth and its expected drawn length both use variants of the symbol L; we distinguish them throughout.

## Definitions and deterministic inequality

For a finite full rooted binary tree $T$, let $n(T)$ be its number of leaves, $h(T)$ its graph height with leaf height zero, $S(T)$ the sum of graph depths of its leaves, and $\ell(T)$ the total vertical length in the source's minimal integer-height drawing. For children $A,B$, the source definition is

$$h(T)=1+\max(h(A),h(B)),\qquad
\ell(T)=\ell(A)+\ell(B)+2+|h(A)-h(B)|.$$

Also $S(T)=S(A)+S(B)+n(T)$ and all three functionals vanish on a single leaf. Since a full binary tree with $i$ leaves has height at most $i-1$, if the children have $i$ and $n-i$ leaves,

$$2+|h(A)-h(B)|\le 2+\max(i-1,n-i-1)\le n.$$

Induction therefore proves the exact, distribution-free inequality

$$2(n-1)\le \ell(T)\le S(T). \tag{1}$$

The lower bound follows from the same recursion. An independent telescoping derivation gives

$$\ell(T)=\sum_{v\text{ internal}}h(T_v)+h(T),\qquad
S(T)=\sum_{v\text{ internal}}n(T_v).$$

Indeed each child height is subtracted once and each internal parent height added twice when the drawn edge differences are summed; leaves contribute zero. Since $h(T_v)\le n(T_v)-1$ and there are $n-1$ internal vertices, the second derivation again gives $\ell(T)\le S(T)$ using $h(T)\le n-1$. For a comb the upper bound is attained; for a balanced four-leaf tree the two quantities are six and eight. Thus neither an inequality reversal nor confusion with ordinary total edge count is hidden in (1).

## Consequence for the source random tree

Let $T_n=\mathrm{DTCS}(n)$ and let $D_n$ denote the graph depth of a uniformly selected leaf, conditional on the realized tree. Then $\mathbb E S(T_n)=n\mathbb E D_n$ by conditional averaging. Source Theorem 3 on PDF page 12, an established Aldous-Pittel/Aldous-Janson theorem, states

$$\mathbb E D_n\sim\frac{3}{\pi^2}(\log n)^2.$$

Consequently

$$2(n-1)\le\mathbb E\ell(T_n)
\le\left(\frac{3}{\pi^2}+o(1)\right)n(\log n)^2,
\qquad
\frac{\mathbb E\ell(T_n)}{n(\log n)^4}\longrightarrow0. \tag{2}$$

This rules out any positive constant asymptotic or two-sided comparability with $n(\log n)^4$. It also gives $\ell(T_n)/[n(\log n)^4]\to0$ in probability by Markov's inequality. The published random-leaf theorem is credited, not claimed as a new solution.

## Self-contained bound without the published asymptotic

Even without that theorem, the required upper order follows directly from the split law. The clade size $M$ seen along a uniformly chosen leaf has transition law

$$\mathbb P(M_{t+1}=j\mid M_t=m)=\frac{1}{H_{m-1}(m-j)},\quad 1\le j<m,$$

where $H_k=\sum_{r=1}^k1/r$. This follows by multiplying the source split probability $m/[2H_{m-1}j(m-j)]$ by the size-bias factor $2j/m$. The next clade has size at most $m/2$ with probability at least $1/(2H_{m-1})$, since there are $\lfloor m/2\rfloor$ terms, each at least $1/[H_{m-1}(m-1)]$.

Use the nonnegative potential $V(m)=(\log m)^2$, with $V(1)=0$. On that event,

$$V(m)-V(M_{t+1})\ge2\log 2\log m-(\log2)^2\ge\log2\log m.$$

The decrease is nonnegative otherwise. Also $H_{m-1}\le1+\log(m-1)\le(1+1/\log2)\log m$ for $m\ge2$. Hence the expected potential drop before absorption is at least

$$c_0=\frac{(\log2)^2}{2(1+\log2)}>0.$$

The chain strictly decreases, so its absorption time is at most $n-1$. Summing conditional expected drops through that bounded time gives $c_0\mathbb E D_n\le(\log n)^2$. Together with (1), this independently proves the upper order needed to refute the proposed growth. It avoids deriving an expectation bound from a probability-only maximum-height bound.

## The apparent source error and remaining question

The source occupation identity on PDF page 29 is $\mathbb E N_n(m)=na(n,m)/m$. For any additive split toll $b(m)$, the exact expected total divided by n is therefore $\sum_m a(n,m)b(m)/m$. The first heuristic line of equation (75) on PDF page 55 omits this factor $1/m$. Further approximations of absolute height differences are also unproved, so inserting the factor alone does not establish a corrected sharp asymptotic. The following separate argument establishes a linear-order expectation limit, without relying on the heuristic replacement of an absolute difference by a difference of expectations.

Search on September 7, 2026 opened the current arXiv abstract and the author's publication/home pages, and queried drawn length, cladogram length, and critical beta-splitting corrections. The author page still identifies overview version 3 and mentions an intended 2026 update. No matching correction was found in that bounded search. This does not establish that the observation is unpublished or that every newer source has been checked.


## Stronger conclusion: the expected drawn length is asymptotically linear

Put $H_m=\mathbb E h(T_m)$, with $H_1=0$. We prove

$$\frac{\mathbb E\ell(T_n)}{n}\longrightarrow
c_{\ell}:=\sum_{m=2}^{\infty}\frac{a(m)H_m}{m}
=\frac6{\pi^2}\sum_{m=2}^{\infty}\frac{H_{m-1}^{\mathrm{harm}}H_m}{m(m-1)},
\qquad 2\le c_{\ell}<\infty. \tag{3}$$

Here $H_k^{\mathrm{harm}}=\sum_{j=1}^k1/j$ distinguishes harmonic numbers from the mean tree height. The proof has three steps.

First, $H_m=O((\log m)^2)$. For the tagged chain begun at m, at each unabsorbed step the conditional probability of reducing the current size by at least half is at least $p_m=1/(2H_{m-1}^{\mathrm{harm}})$. Use fresh uniform variables at successive transitions to couple successful halvings from below by independent Bernoulli variables of probability $p_m$. The absorption time is then bounded by the waiting time for $b_m=\lceil\log_2 m\rceil$ successes. This is a sum of $b_m$ independent geometric variables G supported on the positive integers, with success probability $p_m$.

For $0<p\le1$, convexity gives $e^{p/4}\le1+p/2$. Thus

$$\mathbb E e^{pG/4}=\frac{p e^{p/4}}{1-(1-p)e^{p/4}}\le3.$$

A union bound over all m leaves therefore yields, with no independence assumption among their depths,

$$\mathbb P(h(T_m)>t)\le\min\{1,m3^{b_m}e^{-p_m t/4}\}.$$

Integrating this bound proves

$$H_m\le\frac4{p_m}\bigl(\log m+b_m\log3+1\bigr)=O((\log m)^2). \tag{4}$$

Second, the tagged occupation measures obey a uniform dyadic-block bound. Once the decreasing chain enters the integer block $(b,2b]$, at each subsequent step in that block it exits to a size at most b with conditional probability at least $1/(2H_{2b-1}^{\mathrm{harm}})$. It cannot return after exiting. Its expected number of visits is consequently at most $2H_{2b-1}^{\mathrm{harm}}$, uniformly in its starting state n:

$$\sum_{j=b+1}^{2b}a(n,j)\le2H_{2b-1}^{\mathrm{harm}}. \tag{5}$$

This remains true if the chain skips the block. Combining (4) and (5), for dyadic b at least two,

$$\sum_{j=b+1}^{2b}a(n,j)\frac{H_j}{j}
\le C\frac{(1+\log b)^3}{b}.$$

The sum of these bounds over dyadic blocks above any cutoff tends to zero as the cutoff tends to infinity, uniformly in n. This supplies precisely the tail control missing from a bare pointwise limit. Since $a(n,j)\to a(j)$ for each fixed j, finite-sum convergence followed by this uniform tail bound proves

$$\sum_{j=2}^n a(n,j)\frac{H_j}{j}\longrightarrow\sum_{j=2}^{\infty}a(j)\frac{H_j}{j}.$$

Third, the exact telescoping identity already proved and the branching property give

$$\mathbb E\ell(T_n)=n\sum_{j=2}^n\frac{a(n,j)H_j}{j}+H_n. \tag{6}$$

To justify the expectation identity, reveal the ancestors of any clade until its size j is known; its internal random tree is an independent copy of DTCS(j). Sum the conditional mean height $H_j$ over all clades, using the exact source identity $\mathbb E N_n(j)=na(n,j)/j$. Equation (4) gives $H_n/n\to0$, proving (3). The deterministic lower bound in (1) gives $c_{\ell}\ge2$; the convergent positive series also makes its finiteness explicit.

This establishes an expectation asymptotic, not a law of large numbers for $\ell(T_n)/n$, a variance formula, or a CLT. Those stronger statements are not claimed. The pointwise occupation formula is established literature; the dyadic uniform-tail argument and its application are checked here but lack independent review. A later paper, Brandenberger-Chin-Mossel arXiv:2505.24821v2 (July 2025), states an appropriate weighted-convergence result for all polynomially decreasing test functions on PDF page 3. Together with (4), that provides a second literature-supported route to (3); the self-contained block argument above avoids assuming that general weighted theorem.
