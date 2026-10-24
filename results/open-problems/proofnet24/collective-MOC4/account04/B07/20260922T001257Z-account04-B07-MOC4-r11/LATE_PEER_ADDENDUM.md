# Late peer addendum — generic strict-support locus and SO(6) stationarity

After the main r11 report was frozen, account04/B08 published `MOC4-GENERIC-STRICT-SUPPORT-v1` (scientific commit `61aba8fc1d9eb46d6ae05b3f61a2706aad194a7f`). Its proved reduction says that if MOC4 fails, then arbitrarily near a failure there is a failure with simple nonzero spectra, a unique maximizing permutation vertex and strict compound-block inequalities

\[
|d_{\alpha\beta}|<r_{\alpha\beta}<\frac{1+d_{\alpha\beta}^2}{2}
\]

for every complement block, together with nonzero 1x1/2x2 minors and no common nontrivial reducing subspace.

In the Spin(6) normal form of the r11 report, this means the unpaid Weyl inequality may be attacked on a generic open locus of `SO(6)` with a unique Weyl comparator. In particular, one does not need to manufacture the global proof from degenerate block strata.

For

\[
Q(O)=\sum_{\alpha,\beta}\left(G_{\alpha\beta}\det O_{\alpha\beta}+\frac{X_{\alpha\beta}}4\|O_{\alpha\beta}\|_F^2\right)
\]

(ignore the constant `g_0`), define the block gradient

\[
N_{\alpha\beta}=G_{\alpha\beta}\operatorname{cof}(O_{\alpha\beta})+\frac{X_{\alpha\beta}}2O_{\alpha\beta}.
\]

If a non-Weyl `O_* in SO(6)` is a local maximizer, then for every skew-symmetric `K` the curve `O(t)=O_* exp(tK)` gives the exact first-order condition

\[
O_*^T N\ \text{is symmetric},
\]

and the second-order necessary inequality

\[
\langle N,O_*K^2\rangle
+\sum_{\alpha,\beta}
\left[
\frac{X_{\alpha\beta}}2\|(O_*K)_{\alpha\beta}\|_F^2
+2G_{\alpha\beta}\det((O_*K)_{\alpha\beta})
\right]\le0.
\]

The formula uses only that each block contribution is quadratic and `d^2/dt^2 det(A+tB)|_{t=0}=2 det B`.

Thus a concrete next route is: on the B08 generic locus, combine these Lie-algebra stationarity/Hessian equations with the spectral rank decomposition of `(G,X)` from the main r11 report and rule out a non-Weyl maximizer above the unique Weyl vertex. This is still an unpaid implication, not a proof of MOC4.
