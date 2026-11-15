# Substantial advance elsewhere; T076 is not fully solved

Xujie Lai and Fan Yang, *Localization Lengths for Two-Dimensional Random Band
Matrices: Exponential Lower Bounds*, [arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4),
8 November 2026. The supplied seventh-power bound belongs to
[v2, 6 October 2026](https://arxiv.org/abs/2609.24426v2).

## Precise result

[Section 1.1, Theorem 1.2](https://arxiv.org/html/2609.24426v4)
concerns complex Gaussian Hermitian block matrices on a two-dimensional torus.
There are \(M^2\) blocks of \(W^2\) sites, \(N=(WM)^2\), and

\[
S_{xy}=\frac{1}{5W^2}\bigl(\mathbf1_{a=b}+\mathbf1_{a\sim b}\bigr),
\qquad x\in[a],\ y\in[b].
\]

Here adjacency is nearest-neighbor adjacency on the block torus; \(M\ge100\).
Put \(\ell=10+\log N\). For fixed \(\kappa\in(0,2)\), \(A>1\),
\(C>A+100\), and \(\ell^A\le W\le\ell^C\), every fixed \(D>0\) gives, for
sufficiently large \(N\),

\[
\mathbb P\left(\max_{k:\,|\lambda_k|\le2-\kappa}
\|\psi_k\|_\infty^2\le\frac{(\log W)^{10}\ell^2}{N}\right)
\ge1-N^{-D}.
\]

The abstract summarizes the threshold as \(W\ge(\log N)^{1+\varepsilon}\)
and the localization-length lower bound as \(\exp(W^{1-\varepsilon})\).
Remark 1.3 addresses larger bandwidths using earlier results.
This is a substantial improvement over the brief, but does not reach
\(\exp(cW^2)\), bounded bandwidth in dimension three, or establish the requested
generality and local statistics at the new threshold.

## Checks

The [PDF, printed page 4](https://arxiv.org/pdf/2609.24426v4#page=4)
and HTML agree on the assumptions and exponents. General-profile extensions
are not proved here (Remark 1.1).

Independent scale check: \(W\ge(\log N)^A\) implies
\(\log N\le W^{1/A}\). Setting \(A=1/(1-\delta)>1\) gives
\(\sqrt N\le\exp(\tfrac12W^{1-\delta})\), for \(0<\delta<1\).
Thus the abstract uses a reparameterized epsilon; keeping the same epsilon
would instead give \(1/(1+\varepsilon)\). The factor \(1/2\) converts volume
to physical side length. This is a finite-volume scale interpretation, not
a separate infinite-volume localization theorem. Additive 10 in \(\ell\)
does not change these exponents.
