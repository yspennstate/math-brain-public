VERDICT: PARTIAL a boundary-exclusion theorem and upper bound for the first Hoeffding projection

The variance-limit conjecture remains unresolved. The three earlier
results check out. The new piece addresses their suggested next target,
V_{n,1}=n Var(E[L_n|X_1]), including the boundary.

For a deleted (n-1)-point sample S, define

\[
 U_n(x)=\sqrt n\,\mathbb E_S[T(S\cup\{x\})-T(S)],
 \qquad \mu_n=\int_{[0,1]^2}U_n(x)\,dx.
\]

PROOF.md establishes the exact identity V_{n,1}=Var(U_n(X)) and

\[
 V_{n,1}\le\mu_n(1-\mu_n)+\varepsilon_n,
 \qquad
 \varepsilon_n=2\sqrt2\left(
 \sqrt{\frac n{n-1}}-1+\frac{8\sqrt n}{n-1}\right)
 =O(n^{-1/2}).
\]

In particular, limsup V_{n,1}<=1/4. For every 0<a<1/2, deleting
the boundary strip outside I_a=[a,1-a]^2 changes the variance of U_n
by at most 8(4a-4a^2), when the remaining square is given its uniform
probability distribution. The integral of (U_n-mu_n)^2 on that strip
has the same upper bound. Thus every shrinking boundary strip contributes
o(1) to the normalized first-order energy. These claims require no
localization theorem for optimal tours.

The geometric input is 0<=insertion cost<=2R. Uniformly on the whole
square, U_n<=2sqrt(2); away from its boundary, nearest-distance tails
give U_n<=1+o(1). Integrating the tail correction over distance to the
four sides gives the stated O(n^{-1/2}) error. The interior profile is
not proved to converge or to become constant.

There is an immediate improvement of the earlier total-variance bound.
Let E_n=sum_j j V_{n,j} and let K be round 4's verified constant,

\[
 K=F(c_*)-\frac{\pi c_*^4}{256}e^{-9\pi c_*^2},\qquad
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
                -2c\operatorname{erfc}(\sqrt\pi c),\qquad
 c_*=\arg\min_{c\ge0}F(c).
\]

Since 2 Var(L_n)<=E_n+V_{n,1}, the new result gives

\[
 \limsup_n\operatorname{Var}(L_n)\le\frac{K+1/4}{2}<K.
\]

The strict comparison K>1/4 is proved by exact inequalities. No decimal
optimization, comparison with the best published upper bound, or value
for the conjectured limiting variance is claimed.

AUDIT.md checks the projection normalization with replacement pairs,
the global bound with homothety order statistics, and the constant 1/4
by a separate pointwise nearest-distance limit and Fatou argument. It
checks the integrated error by summing contributions from the four sides,
the boundary comparison with distinct conditional means, the n=2 case,
and the spectral factor two by exact subtraction. The earlier disk deficit
was independently re-derived by translation, validating its conservative
constant. No mathematical error was found.

The bounded literature check ended within five minutes. Opened Sourav
Chatterjee, *A general method for lower bounds on fluctuations of random
variables*, [arXiv:1706.04290v3](https://arxiv.org/html/1706.04290v3),
Section 3, problem (2). No closing theorem was found in the recorded
searches. A Dagstuhl PDF open failed because of the web tool's size
limit and is not used as evidence. This was not an exhaustive review;
no SOLVED_ELSEWHERE.md was warranted.

All mathematical checks are analytic. No simulation, mathematical script,
or numerical variance estimate was run. Reproduce the document checks:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat PROOF.md AUDIT.md REPORT.md
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

The sandbox prints `nice: setpriority: Operation not permitted`; no
successful priority adjustment is claimed. Only brief file reads ran.
All writes stayed in this folder; no git, subagents, shared-store writes,
or external messages were used. LOG.md records the commands and outcomes.

What failed or remains uncertain: no convergence of V_{n,1}, any other
fixed-order energy, fixed-noise covariance, or Var(L_n) is established.
The boundary estimate removes one possible source of difficulty for the
first projection; it does not control variation throughout the interior.
The leading asymptotic for E L_n does not by itself imply convergence of
mu_n=sqrt(n)(E L_n-E L_{n-1}). AUDIT.md gives explicit sequence and
profile examples that invalidate those tempting inferences. Novelty
relative to the full literature has not been established.

Next worker: prove an interior comparison, for example
E|U_n(X_a)-U_n(X_a')|^2->0 for independent uniform points in I_a at
each fixed a>0. Together with the boundary comparison this would prove
V_{n,1}->0. Such a comparison is currently a missing lemma, not a
consequence of local point-process convergence. Even that result would
leave higher-order energies or fixed-noise covariance to be controlled.

Task: "take the NEXT checkable step on this problem, building on that work"
— T222, 2026-11-15 08:41:50 Asia/Tbilisi.
