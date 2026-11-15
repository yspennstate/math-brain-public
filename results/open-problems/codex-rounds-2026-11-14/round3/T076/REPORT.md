VERDICT: PARTIAL exact deterministic return-kernel asymptotic for the two-dimensional block profile

The earlier report's Lai–Yang theorem and scale conversion hold. A literature
search lasting under five minutes found no later solution to T076. The
latest inspected revision remains Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds*, [arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4),
8 November 2026. Its Gaussian periodic block model remains a restriction.

New beyond the earlier report: [PROOF.md](PROOF.md) proves, for its block
variance matrix \(B=(I+\mathrm{adjacency})/5\) on an \(M\)-by-\(M\) torus,
\[
[(I-(1-\mu)B)^{-1}]_{00}-\frac1{\mu M^2}
=\frac5{4\pi}\log\frac1{\mu+M^{-2}}+O(1),
\]
uniformly for \(M\geq3\), \(0<\mu\leq1/2\), with an absolute error
constant. After the physical normalization \(W^{-2}\), the centered
diagonal for \(\mu\leq M^{-2}\) is
\[
\frac5{2\pi}\frac{\log M}{W^2}+O(W^{-2}).
\]
The proof includes the precise site-level identity and a second derivation
of the coefficient from \(n p_n(0)\to5/(4\pi)\) for the associated walk.
It checks the smallest allowed torus explicitly, handles both parities,
and shows why negative Fourier eigenvalues cause no extra singularity.

This is a deterministic sublemma, not a new bandwidth threshold for random
matrices. The logarithmic order is standard; Lai–Yang already give propagator
upper bounds in Lemma 2.7. No claim of novelty in random-walk theory is made.
No localization-length, eigenvector, universality, or dimension-three
theorem has been proved here.

The failed shortcut is to use smallness of this centered kernel as smallness
of the full kernel. The latter also contains exactly \(1/(\mu N)\),
\(N=W^2M^2\). With \(M=\lfloor e^W\rfloor\), \(\mu=N^{-1}\), the
centered part tends to zero while the full diagonal tends to one. Moreover,
even the centered estimate supplies no control of the stochastic resolvent
error. That missing step prevents any conclusion for T076.

Commands and sources are recorded in [LOG.md](LOG.md). Verification used
`rg --files`, `cat`, the web search tool, and independent analytic
derivations. No numerical experiment ran. The priority probe
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 /usr/bin/true`
reported `nice: setpriority: Operation not permitted`; no simulation was
launched at default priority. No git commands, external writes, or subagents.

Next worker: take one quadratic drift term in the alternating two-loop
equation, Lai–Yang (2.33)–(2.34), and test whether its time-integrated estimate
can use \((\log M)/W^2\) without an additional logarithmic loss. Separate
the constant mode before estimating it. The present diagonal lemma alone
does not establish such an estimate.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 01:12 Asia/Tbilisi.
