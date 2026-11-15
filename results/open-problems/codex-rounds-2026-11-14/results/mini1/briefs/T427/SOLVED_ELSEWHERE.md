# T427: existence addressed in a new preprint

Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*, [arXiv:2610.40509v1](https://arxiv.org/abs/2610.40509v1), submitted 29 October 2026. See [Corollary 2, Section 5.1](https://arxiv.org/html/2610.40509v1#S5.SS1), PDF printed page 17.

For the unit square Q with uniform probability measure, that corollary gives

\[
n\mathbb E W_2^2(\mu_n,\lambda)
=\frac{\log n}{4\pi}+\beta_{\mathrm{sd}}+h_Q
+O(n^{-1/120}\log(en)).
\]

Here \(\beta_{\mathrm{sd}}\in\mathbb R\) is universal, and, in the paper's convention,

\[
h_Q=\lim_{t\downarrow0}\left[
\sum_{\substack{k,l\geq0\\k+l>0}}
\frac{e^{-\pi^2(k^2+l^2)t}}{\pi^2(k^2+l^2)}
-\frac{\log(1/t)}{4\pi}\right].
\]

Thus its result implies \(c_{\square}=\beta_{\mathrm{sd}}+h_Q\) exists and is finite. It does not supply an evaluated numerical value for the universal semidiscrete constant.

The empirical masses are exactly 1/n. The square's right-angle corners are allowed; its intrinsic distance equals Euclidean distance by convexity. The density is 1 and its logarithmic correction vanishes. These checks distinguish the result from the two-empirical-sample formula.

This is a report of a preprint theorem. The full proof has not been independently certified here. Its date precedes the brief's November 2026 status date, so it is a missed update rather than a later-dated result.
