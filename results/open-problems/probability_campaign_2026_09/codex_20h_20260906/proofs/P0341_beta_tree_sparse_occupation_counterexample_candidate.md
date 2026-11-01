# P0341: Sparse root-sensitive tests refute both parts of the occupation ansatz

Status: author-checked partial counterexample to Open Problem 8, specifically its displayed Ansatz 20. Explicit useful bounds for the occupation probabilities remain unresolved here. No independent review or originality certificate.

Source: Aldous-Janson, arXiv:2303.02529v3, PDF pages 28-30 and 39-40, April 2025. https://arxiv.org/abs/2303.02529v3. The PDF is pinned by the source registry. Write $a(n,j)$ for the probability that the tagged harmonic descent chain starting at n visits j, and $a(j)=6H_{j-1}/[\pi^2(j-1)]$ for its established fixed-j limit. Thus $a(n,n)=1$ exactly and $a(n,j)\to a(j)$ for fixed j.

The source's ansatz quantifies over every nonnegative sequence with at most polynomial growth. Part (i) asserts convergence of weighted sums whenever the limiting weighted series is finite. Part (ii) asserts equivalence with the corresponding truncated limiting sum when the series is infinite.

## Counterexample to the summable case

Choose the bounded function $f(j)=\mathbf1_{\{j=2^r\text{ for some integer }r\ge1\}}$. Since $a(2^r)=O(r2^{-r})$, the series $S=\sum_{r\ge1}a(2^r)$ is finite. For n equal to $2^K$, nonnegativity and the certain root visit give, for every fixed M<K,

$$\sum_{j=2}^{2^K}a(2^K,j)f(j)
\ge1+\sum_{r=1}^{M}a(2^K,2^r).$$

Let K tend to infinity and then M tend to infinity. Pointwise occupation convergence and monotone convergence of the positive series yield

$$\liminf_{K\to\infty}\sum_{j=2}^{2^K}a(2^K,j)f(j)\ge1+S.$$

The proposed limit is S, so part (i) is false even for a bounded nonnegative test function. No rate of occupation convergence or numerical calculation is used.

## Counterexample to the divergent case

Choose $g(j)=j\mathbf1_{\{j=2^r\text{ for some integer }r\ge1\}}$. This satisfies $g(j)\le j$. The limiting weighted series diverges, and its truncation at $n=2^K$ is

$$\sum_{j=2}^{2^K}a(j)g(j)=\sum_{r=1}^K\frac{6\,2^r H_{2^r-1}}{\pi^2(2^r-1)}\asymp K^2.$$

The actual finite-chain weighted sum is at least its root contribution $a(2^K,2^K)2^K=2^K$. Hence the ratio of actual to proposed sums tends to infinity along powers of two, refuting part (ii).

## Why this does not solve every occupation question

The obstruction is a moving root contribution invisible to every fixed-j limit. Restricting the test functions to appropriately regular, non-sparse classes may lead to valid theorems; this argument decides none of those refined classes or useful two-parameter error bounds. It also does not contradict the published special cases already proved by separate methods. The requested general ansatz is false, while the broader numbered question is only partially answered.

Searches on September 7, 2026 for the exact ansatz, occupation asymptotics and newer critical beta-splitting papers were recorded as bounded checks. New 2025 and August 2026 papers are being read for precise scope; no priority claim is made.
