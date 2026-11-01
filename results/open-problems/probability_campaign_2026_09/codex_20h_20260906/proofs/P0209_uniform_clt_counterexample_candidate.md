# P0209: a four-state obstruction to the proposed uniform normal approximation

Status: complete negative-answer candidate, author checked by spectral covariance and a direct rare-event argument. No independent review or novelty certificate. The construction responds to the literal historical question, whose current status is unverified.

Source: Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, 2002 unfinished monograph, 2014 recompilation, Open Problem 4.30, PDF p.137, https://www.stat.berkeley.edu/~aldous/RWG/book.pdf . The chapter is internally dated October 11, 1994. With a stationary finite reversible continuous-time chain and a function g satisfying Eπg=0 and Eπg²=1, the source asks for a universal bound

\[
 \sup_x\left|\mathbb P_\pi\left\{\frac{\int_0^t g(X_u)\,du}
 {\sigma\sqrt t}\le x\right\}-\Phi(x)\right|
 \le\psi(\|g\|_\infty,t/\tau_2),
 \qquad \psi(b,s)\longrightarrow0\quad(s\longrightarrow\infty).
\]

Here σ² is the asymptotic variance rate and τ2 is the relaxation time. We keep the first argument exactly equal to two, so there is no hidden assumption of uniformity or continuity in b.

## Four-state reversible family

For an integer s at least three, set ε=s^{-2} and R=s^4. Let Y be a stationary two-state chain on {0,1}, with rates 0→1 equal to ε and 1→0 equal to 1-ε. Its stationary success probability is ε and its nonzero generator eigenvalue is -1. Independently let Z be a fair stationary sign chain, flipping at rate R/2, with nonzero generator eigenvalue -R. The product X=(Y,Z) has four states, is irreducible and reversible, and has generator eigenvalues 0,-1,-R,-(R+1). Thus τ2=1.

Define

\[
 A=2\varepsilon+\sqrt{(1-\varepsilon)(1-4\varepsilon)},\qquad
 B=\frac{2-A}{1-\varepsilon},\qquad
 g(Y,Z)=AZ+B(Y-\varepsilon).
\]

For 0<ε≤1/9, A and B are positive. The positive root A solves

\[
 A^2-4\varepsilon A+5\varepsilon-1=0,
\]

which is equivalent to A²+B²ε(1-ε)=1. Independence and centering therefore give Eπg=0 and Eπg²=1. Also A+B(1-ε)=2. Every possible absolute value of g is at most max{A+Bε,A+B(1-ε)}=2 because ε<1/2, and the value 2 occurs when Y=1,Z=1. Hence ||g||∞=2 exactly for every s. Finally A→1 and B→1.

## Exact variance rate

The stationary autocovariance is

\[
 \mathbb E[g(X_0)g(X_u)]
 =A^2e^{-Ru}+B^2\varepsilon(1-\varepsilon)e^{-u}.
\]

This follows directly from the two nonconstant coordinate eigenfunctions. Integrating twice over the covariance triangle gives

\[
 \sigma^2=2\int_0^\infty\mathbb E[g(X_0)g(X_u)]\,du
 =\frac{2A^2}{R}+2B^2\varepsilon(1-\varepsilon)>0.
\]

Each fixed member of the family has the ordinary asymptotic normal limit. The issue is uniformity over chains at a time depending on the member.

## Collapse at time t=s

Observe the chain until t=s. Write F=A∫₀ˢZ_u du and H=B∫₀ˢ(Y_u-ε)du. The probability that Y is ever one on this interval is at most

\[
 \mathbb P(Y_0=1)+\mathbb E[\#\{0\to1\hbox{ transitions in }[0,s]\}]
 \le\varepsilon+s\varepsilon=\frac1{s^2}+\frac1s.
\]

On the complementary event, H=-Bεs, and

\[
 \left|\frac{H}{\sigma\sqrt s}\right|
 \le\sqrt{\frac{\varepsilon s}{2(1-\varepsilon)}}\longrightarrow0.
\]

The fast component is negligible in L²:

\[
 \mathbb E F^2
 =2A^2\int_0^s(s-u)e^{-Ru}\,du
 \le\frac{2A^2s}{R},
\qquad
 \mathbb E\left(\frac F{\sigma\sqrt s}\right)^2
 \le\frac{A^2}{RB^2\varepsilon(1-\varepsilon)}\longrightarrow0.
\]

Here Rε=s². Combining the rare-event bound with Chebyshev yields

\[
 \frac{\int_0^s g(X_u)\,du}{\sigma\sqrt s}
 \longrightarrow0\quad\hbox{in probability}.
\]

For any fixed x>0 its distribution function thus tends to one. The limiting inferior of its Kolmogorov distance from a standard normal is at least 1-Φ(x). Letting x decrease to zero shows that this limiting inferior is at least one half. Yet ||g||∞=2 and t/τ2=s→∞. No function ψ of the stated kind can therefore exist.

## Second checks and rate normalization

The apparent conflict with variance convergence is illusory. For a coordinate with covariance c e^{-λu}, the exact finite-time variance is 2c[t/λ-(1-e^{-λt})/λ²]. Substitution shows Var(∫g)/(σ²s)→1. Rare visits carry the variance while their probability tends to zero; the normalized squares are not uniformly integrable. Variance convergence alone cannot force a central limit theorem.

Page 26 explicitly permits nonnegative transition rates with no constraint on their sums. Even imposing total jump rate at most one would not rescue the proposed bound. Replace the generator Q by Q/R and observe for time Rs. Every outgoing rate is at most (R/2+1)/R≤1. The relaxation time becomes R, the variance rate becomes Rσ², and the time integral has the same law as R times the old integral. Both the standardized law and the ratio t/τ2=s are unchanged.

The independent coordinate construction also makes clear the missing quantity: an asymptotic variance scale relative to the function and the slow rare-event mode. A gap and a bounded instantaneous variance do not prevent the asymptotic variance from concentrating in rare excursions. This observation is explanatory, not a claim that any particular modified bound has been proved here.

Focused primary-source searches on September 6, 2026 found the original statement and the author's chapter notes, which discuss fixed-chain Berry–Esseen constants. No later resolution of this precise uniform question was verified. This is not a novelty certificate. A future reviewer should recheck the exact fixed L∞ normalization, stationary initialization, spectral gap, covariance integral, and uniform-limit quantifiers.


## Scoped parent review receipt

The parent independently reviewed the historical question and the checked construction. Its report is at `~/<private-repo>/12_cognitive_architecture/audits/reports/2026/09/06/last200-implementation/P0209_historical_question_candidate_review.md`, SHA256 `d0a58ea91383b4abcbff6b4d85c2515ce723250e2794cee4b76f2b7684d70f14`. The report found no gap in its checked scope. Structural validation is not mathematical certification. Present openness, novelty, human review, and unique canonical audit-node binding remain unverified. This receipt does not promote the result to an original solution.
