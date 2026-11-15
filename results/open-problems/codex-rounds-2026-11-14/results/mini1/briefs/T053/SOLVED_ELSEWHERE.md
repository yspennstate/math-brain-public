# Substantial advances found; fixed-density T053 remains open

The filename follows the task's literature-stop instruction. Neither result below solves the stated fixed-density problem.

Karsten Matthies and Raphael Winter, *Improved geometric and recollision estimates for the invariance principle of the random Lorentz gas*, Nonlinearity **39** (2026), 035003; [arXiv:2506.18539v2](https://arxiv.org/abs/2506.18539v2); [published paper](https://orca.cardiff.ac.uk/id/eprint/185473/1/Matthies_2026_Nonlinearity_39_035003.pdf), [DOI](https://doi.org/10.1088/1361-6544/ae4602). Published 5 March 2026.

Theorem 3.1 extends the three-dimensional annealed invariance principle to
\[
T(r)\longrightarrow\infty,\qquad T(r)r^2|\log r|\longrightarrow0.
\]
In the paper's normalization, \(T(r)^{-1/2}X^r(T(r)\,\cdot)\) converges to its Wiener limit. The setting remains the simultaneous Boltzmann–Grad limit \(r\to0\), \(\rho\to\infty\), \(\rho r^2\to1\). The previous condition had \(|\log r|^2\) instead. The published theorem and [arXiv full text, §3](https://arxiv.org/html/2506.18539v2#S3) agree on the improved condition. “Averaged-quenched” in the theorem is not an almost-sure fixed-environment conclusion; the introduction explicitly describes averaging over scatterers and initial velocity.

Bálint Tóth, *Semi-Quenched Invariance Principle for the Random Lorentz Gas: Beyond the Boltzmann–Grad Limit*, Entropy **27** (2025), 397; [arXiv:2501.00519v2](https://arxiv.org/abs/2501.00519v2); [published paper](https://www.mdpi.com/1099-4300/27/4/397), [DOI](https://doi.org/10.3390/e27040397). Published 8 April 2025.

Here \(d=3\), \(r_\epsilon=\epsilon^{3/2}\), and the scatterer process is obtained by scaling an intensity-one Poisson process by \(\epsilon\), omitting centers covering the origin. Initial velocity is uniform in a spherical cap of angular radius \(\beta_\epsilon\in(0,1]\). Theorem 2 gives convergence of conditional path laws in probability over environments if
\[
T_\epsilon\to\infty,\qquad r_\epsilon(T_\epsilon+\beta_\epsilon^{-1})\to0.
\]
Theorem 3 gives almost-sure conditional convergence along sequences satisfying
\[
\sum_{n\ge2}\left[(\log n)r_nT_n+(\log n)^2(r_n/\beta_n)^{2/3}\right]<\infty.
\]
The environments vary with \(\epsilon_n\). This does not keep radius and intensity fixed. Its time condition is not the longer Matthies–Winter condition; these two improvements have not been combined here.

Both advances were missing from the supplied status paragraph. Neither proves recurrence in dimension two or the fixed-density CLT conditioned on the unbounded vacant component. No solution of those claims was found in this bounded search.
