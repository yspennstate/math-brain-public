VERDICT: PARTIAL a joint bound for insertion energy and the first Hoeffding projection

The variance-limit conjecture remains unresolved. The earlier results
check out. The new piece couples two quantities that round 5 bounded
separately, and gives a strictly smaller upper bound for the variance.

Use the earlier notation E_n=sum_j j V[n,j] and
U_n(x)=sqrt(n) E[T(S union {x})-T(S)], with S a deleted (n-1)-point
sample. Let mu_n=integral_Q U_n and
W_n=Var_S(integral_Q sqrt(n)[T(S union {x})-T(S)] dx).
With alpha=e/4 and round 3's c_* and kappa=min F, PROOF.md proves

\[
 \limsup_n\left\{E_n+W_n+\alpha V_{n,1}
                     +(1+\alpha)(\mu_n-c_*)^2\right\}\le\kappa.
\]

Here

\[
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
                   -2c\operatorname{erfc}(\sqrt\pi c),\qquad c\ge0.
\]

Combining the tradeoff with round 5's verified projection bound gives

\[
 \limsup_n\operatorname{Var}(L_n)
 \le\frac\kappa2+\frac{1-e/4}{8}
       -\frac{1-e^2/16}{4}(c_*-1/2)^2.
\]

Even after dropping the last term, this strictly improves the preceding
bound (K+1/4)/2. The difference is
e/32-eta(c_*)/2>0, where eta(c)=pi c^4 exp(-9pi c^2)/256 and
K=kappa-eta(c_*). These are upper bounds, not candidate values for
a limiting variance. No comparison with the best published upper
variance bound or claim of literature-wide novelty is made.

The new ingredient is an envelope center depending on query position:
c_n(x)=c_*-(e/4)(U_n(x)-c_*). The curvature bound F''<=2+8/e
makes variation in U_n incur an explicit penalty. An integrated
nearest-distance tail error controls these n-dependent centers uniformly,
including the boundary. No optimal-tour localization is assumed.

AUDIT.md independently derives e/4 from the scalar second-moment
maximum at prescribed mean: its second derivative is at most -e/2.
A second calculation through F(c)-c^2 checks the adaptive-center
algebra. Replacement pairs, weighted quadratic minimization, negative
centers, boundary domination, and n=2 all pass. No mathematical error
was found in the earlier results or the new theorem.

The bounded web-tool check found no closing theorem. The source opened
was Sourav Chatterjee, *A general method for lower bounds on fluctuations
of random variables*, [arXiv:1706.04290v3](https://arxiv.org/html/1706.04290v3),
Section 3, problem (2). This was not an exhaustive search.

All verification is analytic. No simulation or numerical optimization
was run. Commands and outcomes are recorded in LOG.md. Read back with:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat PROOF.md AUDIT.md REPORT.md
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

The sandbox prints `nice: setpriority: Operation not permitted`; no
successful priority adjustment is claimed. Only brief reads ran.
All writes stayed here; no git, subagents, or shared-store updates.

What failed or remains uncertain: no first-projection decay, convergence
of E_n, fixed-order energies, fixed-noise covariance, or Var(L_n) is
proved. Alternating order-two spectra satisfy the new inequalities,
so the tradeoff alone cannot establish convergence. The preceding
interior-comparison lemma is still missing.

Next worker: target that interior comparison or a fixed-noise covariance
limit. The new W_n term also records a precise sample-size comparison:
it is n times the variance of E_X[L_n(S,X)]-L_{n-1}(S). Controlling
this term across n is a possible route, but no summability or convergence
claim for it is established here. Further bound optimization would still
leave the original variance-limit question open.

Task: "take the NEXT checkable step on this problem, building on that work"
— T222, 2026-11-15 approximately 11:15 Asia/Tbilisi.
