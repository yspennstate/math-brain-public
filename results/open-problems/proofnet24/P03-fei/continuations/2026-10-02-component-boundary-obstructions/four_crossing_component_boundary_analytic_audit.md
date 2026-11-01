# Independent analytic audit of the four-crossing obstruction

Date: 2026-10-02. **PASS for the construction and formulas below.**

This audit is independent of the parent's finite checker and proof writeup.
It verifies the strengthened construction sent by the parent after the
five-crossing obstruction was found. The full general finite-crossing FEI
conjecture is not disproved, and novelty is unverified.

Let (k\ge2), (N\ge2) be even, (p=2^{-k}), (q=2^{-N}), and
(M_N=N\binom N{N/2}/2^N). Use (k) coarse coordinates with weights
(A2^j), (j=0,\ldots,k-1), and (N) fine coordinates with weights
(1+2^{-i}), (i=1,\ldots,N). The fine score range has radius
(R=N+1-2^{-N}). Take (A>R).

The coarse scores are the odd multiples of (A). The unique pattern
(c_*) with coarse score (A) has its highest coordinate positive and
all other coarse coordinates negative. The score interval ((0,2A))
contains exactly the fine cube attached to (c_*).

Let (v) be the largest-score central-layer fine point, with score (t),
and let (eta=2^{-N}). Define the score labels by four increasing
breakpoints
\[
 0,\quad A+t-\eta,\quad A+t+\eta,\quad 2A,
\]
and labels (+,-,+,-,+). Each of the five attained blocks is nonempty
when (k\ge2,N\ge2), and no endpoint is attained. The function is
\[
 f(c,x)=1-2\mathbf 1_{\{c=c_*,\,x\ne v\}}.
\]

For each coarse coordinate the influence is (2p(1-q)), and for each
fine coordinate it is (2pq). Therefore
\[
 I(f)=2kp(1-q)+2pNq.
 \tag{1}
\]

Let (L,U) be the fine-score sets below and above the isolated point,
as in the five-crossing proof. They satisfy
(\Pr(L)+\Pr(U)=1-q) and
(I(1-2\mathbf 1_L)=I(1-2\mathbf 1_U)=M_N).
For any fine set (B), the component event ({c=c_*,x\in B})
has influence
\[
 2kp\Pr(B)+pI(1-2\mathbf 1_B).
\]
Summing this for the two negative components yields exactly
\[
 B_-(f)=2kp(1-q)+2pM_N.
 \tag{2}
\]

The positive lower tail is the highest coarse coordinate's negative
halfspace, so its influence is (1). The positive upper tail is the
highest coarse coordinate's positive halfspace with (c_*) removed.
Its highest-coordinate influence is (1-2p), while each of its other
(k-1) coordinate influences is (2p). Hence its influence is
(1+2(k-2)p). The remaining positive component is the singleton
((c_*,v)) in dimension (k+N), whose influence is (2(k+N)pq).
Thus
\[
 B_+(f)=2+2(k-2)p+2(k+N)pq.
 \tag{3}
\]

All three claimed formulas pass the audit. Now set (N=2^{2k}).
The elementary central-binomial estimate gives
(M_N\ge\sqrt{N/2}), so (B_-(f)\ge\sqrt2), and (3) gives
(B_+(f)\ge2). Since (N2^{-N}\le1), (1) gives
(I(f)\le2p(k+1)). Consequently
\[
 \frac{\min\{B_+(f),B_-(f)\}}{I(f)}
 \ge\frac{2^k}{\sqrt2(k+1)}\longrightarrow\infty.
\]
This is a four-crossing obstruction to the proposed component-boundary
comparison. The audit uses no unproved comparison hypothesis.
