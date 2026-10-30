# Addendum — exact parent-mask / ordered-flag identification

**Status:** proved compatibility statement; full FEI remains OPEN / NOT PROVED. This addendum was written after reading the fresh fleet03/B16 `ordered-flag-physical-resolvent` report and does not modify the theorem in `REPORT.md`.

Fix the same physical coordinate order `pi` used by the ordered-min q-flip basis. Let coordinate `i` have rank `r`, let

\[
L_i^\pi=\{j:\pi(j)>\pi(i)\},\qquad m_i=|L_i^\pi|,
\]

and let an actual ordered-min generator be indexed by nonempty `w subseteq L_i^pi`. Fleet03's exact flag law is

\[
\nu_i^\pi(w)=2^{-m_i}.
\tag{A.1}
\]

The ordered-min dual-mask theorem says that the corresponding coarse parent mask `g_{i,w}` is a one-subcube defect of codimension

\[
c_i=n-r+1=m_i+1,
\tag{A.2}
\]

whose defining physical-coordinate set is exactly the pivot together with all coordinates later than it. Therefore the projective coordinate influence proved in the main report becomes

\[
\boxed{
\beta_{g_{i,w}}(e_\ell)
=\begin{cases}
\nu_i^\pi(w),&\ell\in\{i\}\cup L_i^\pi,\\
0,&\text{otherwise},
\end{cases}
}
\tag{A.3}
\]

for `c_i>=2`, while the codimension-one endpoint is projectively trivial. Summing (A.3),

\[
\boxed{
J(g_{i,w})=c_i\nu_i^\pi(w)=c_i2^{1-c_i}\le1.
}
\tag{A.4}
\]

Thus the actual central parent coefficients `mu_{i,w}` from the main report satisfy the exact flag-form mask bank

\[
\boxed{
\sum_{i,w}\mu_{i,w}J(g_{i,w})
=\sum_i c_i\,\mathbb E_{W\sim\nu_i^\pi}
\bigl[\mu_{i,W}\,1_{\{W\ne0\}}\bigr].
}
\tag{A.5}
\]

This identifies the **same** physical flag appearing in fleet03's oriented payment; no abstract arbitrary-translation frame is needed. It also exposes the precise remaining mismatch. Fleet03 pays a local physical source square under the unweighted flag expectation `E_{nu_i} q_{i,W}`, while the mask-resolvent interface sees the coefficient-weighted expression (A.5). Therefore the next compiler theorem must show that the source-curvature pushforward sends the exact per-parent density from the signed current to fleet03's local physical square with an absolute no-reuse density bound, or else exhibit a genuine Boolean obstruction. Merely observing bounded raw support incidence is no longer the target.

The main report's dimension-free estimate remains valid and is recovered immediately from `c_i 2^{1-c_i}<=1`:

\[
\sum_{i,w}\mu_{i,w}J(g_{i,w})
\le \sum_{i,w}\mu_{i,w}
=E_{\rm cen}
\le\frac{11}{192}W.
\tag{A.6}
\]

No R32/R16 coefficient is absolute-valued in this identification, and terminal, negative-credit, moment-refund and resolvent-boundary ledgers are untouched.
