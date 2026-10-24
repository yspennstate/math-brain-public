# account02/B10 early checkpoint — a clean-reservoir receiver for bidirectional leakage

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting calculation; full QFORM remains OPEN.

The first unpaid implication is the exact-null bidirectional mixed-bank endpoint left by my preceding run: in the partner near-coloop state, both transverse coordinates may share ORIGINAL leaves with the longitudinal leakage. I am testing whether a genuinely clean transverse reservoir, rather than a fully clean square bank, is enough.

Let the partner exact-null state be

\[
Q=2r(\sqrt c H+T)Y+aY^2+2bYW+dW^2,
\]
where `H` is one ORIGINAL coordinate, the leaf coefficient vectors `t,y,w` satisfy
\[
\|t\|_2^2=\rho=1-c,\quad \|y\|_2=\|w\|_2=1,\quad t\perp y,w,\quad y\perp w,
\]
`c>63/64`, and the adapted spectral matrix is `[[0,r,0],[r,a,b],[0,b,d]]` with `sigma_min>=1`. Hence `r>=1` and `|d|>=1`.

Put `T0={i:t_i!=0}` and suppose the complement `I=T0^c` retains transverse Gram
\[
G_I=\sum_{i\in I}(y_i,w_i)(y_i,w_i)^T,\qquad \det G_I=\delta>0.
\]
Normalize `P=T/sqrt(rho)` when `rho>0`. Because `P` is supported on `T0`, while the ORIGINAL sources in `I` contribute only to `(Y,W)`, the two-dimensional product-marginal theorem on `I` gives the source-valid domination
\[
\rho_{Y,W,P}(y,w,p)\le {2\over\sqrt\delta}\,p_P(p).
\]
Indeed condition on the `T0` variables; the `(Y_I,W_I)` density is at most `2/sqrt(det G_I)`, and then disintegrate by `P`. Consequently the maximal quantity of the proved single-hub theorem satisfies
\[
M_1:=\sup_y\int \sup_w\rho_{Y,W,P}(y,w,p)\,dp\le {2\over\sqrt\delta}.
\]

Now divide by `kappa=r sqrt(c)`. Then
\[
Q/\kappa=2HY+\lambda W^2+2W g(Y,P)+F(Y,P),\qquad \lambda={d\over\kappa},
\]
with explicit linear/quadratic `g,F`; no independence of `T,Y,W` is asserted. The proved `single_hub_core` Theorem 3.2 therefore yields
\[
\|p_{Q/\kappa}\|_\infty\le {1\over2}+8M_1|\lambda|^{-1/2},
\]
and scaling back gives
\[
\boxed{\ \|p_Q\|_\infty\le {1\over2r\sqrt c}+{16\over\sqrt\delta}\,(r\sqrt c)^{-1/2}|d|^{-1/2}
\le {1\over2\sqrt c}+16\delta^{-1/2}c^{-1/4}.\ }
\]
Thus bidirectional same-bank contamination is uniformly paid whenever some ORIGINAL-coordinate complement of the leakage support retains a quantitatively nondegenerate transverse Gram. This does not use post-rotation independence.

In particular, if all unpaid transverse leaf leverages are `<1/61` and the leakage-support transverse trace is at most `1/2`, then `G_I=I_2-G_{T0}` has `lambda_min>=1/2`, hence `delta>=1/4`, and
\[
\|p_Q\|_\infty< {1\over2}\sqrt{64/63}+32(64/63)^{1/4}<32.64.
\]
The remaining exact-null debt is therefore narrower: leakage must touch enough ORIGINAL coordinates to carry more than one half of the total transverse trace (and, in the fully overlapping case, no clean transverse reservoir exists at all).

This checkpoint will be audited against the current single-hub theorem and the required pinned ruled-side theorem before the final report.
