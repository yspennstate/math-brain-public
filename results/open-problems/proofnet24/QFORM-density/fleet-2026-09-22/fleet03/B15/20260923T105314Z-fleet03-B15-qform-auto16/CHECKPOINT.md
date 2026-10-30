SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T10:53:14Z.
attacking: weak-limit/trace closure for density estimates, with no moment assumption and continuity kept separate.

# Early substantive checkpoint

Let \(\mathcal H(\mu)\) denote the optimal essential density height of a probability law \(\mu\) on \(\mathbb R\), with value \(+\infty\) if \(\mu\) has no bounded density. The completed fleet04/B15 heat-height theorem gives
\[
\mathcal H(\mu)=\sup_{\varepsilon>0,\,y\in\mathbb R}\int \gamma_\varepsilon(z-y)\,d\mu(z).
\]
For every fixed \((\varepsilon,y)\), the Gaussian kernel is bounded and continuous. Hence if \(\mu_m\Rightarrow\mu\) weakly,
\[
\int \gamma_\varepsilon(z-y)\,d\mu_m(z)\to
\int \gamma_\varepsilon(z-y)\,d\mu(z).
\]
Taking the supremum after the limit gives the exact lower-semicontinuity inequality
\[
\boxed{\mathcal H(\mu)\le \liminf_{m\to\infty}\mathcal H(\mu_m).}
\]
Thus a uniform density-height estimate is closed under arbitrary weak limits of output laws. No moments, support bounds, or input smoothness are needed.

For a fixed random vector \(X\in\mathbb R^n\) finite almost surely and coefficients \(A_m\to A\), \(b_m\to b\), \(c_m\to c\),
\[
Q_m=X^T A_mX+b_m^TX+c_m\to X^TAX+b^TX+c=:Q
\]
almost surely, because the convergence is pointwise for every finite sample \(X(\omega)\). Consequently
\[
\boxed{\mathcal H(\mathcal L(Q))\le \liminf_m \mathcal H(\mathcal L(Q_m)).}
\]
This is the intended no-moment coefficient-limit/trace compiler. It is one-way: it permits proving a uniform estimate on nondegenerate approximants and passing to a degenerate endpoint, but it does not infer a near-null estimate from an exact-null bound.

Continuity is logically stronger and is not supplied by this weak-limit closure: smooth bounded densities can converge in total variation to a bounded discontinuous density. The full report will make this separation precise and apply the fleet04/B15 theorem at an actual QFORM inequality.
