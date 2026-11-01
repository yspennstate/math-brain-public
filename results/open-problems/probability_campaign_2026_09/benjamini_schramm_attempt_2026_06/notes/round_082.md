# Round 082 log

## Goal

Calibrate the local separator-convolution property on the simplest
nonamenable model, the \(d\)-regular tree.

## Construction

Root \(T_d\) at \(o\).  Given \(\delta>0\), choose \(L\) large.  For a residue
\(r\pmod L\), let
\[
  S_r=\{x:\operatorname{dist}(o,x)\equiv r\pmod L\}.
\]
For any finite \(K\), choose \(r\) so that \(|K\cap S_r|\le |K|/L\), set
\[
  K_0=K\cap S_r,
\]
and take the non-buffer pieces to be intersections of \(K\setminus K_0\) with
the components of \(T_d\setminus S_r\).  These pieces have diameter at most
\(2L\).  For distinct pieces use \(W_{ij}=S_r\), which is a proper path
separator.

## Estimates

The buffer mass satisfies
\[
  \mathcal B_p(K_0;K)\le 2|K_0|/|K|\le2/L.
\]

For the separator-convolution term, use the uniform critical \(L^2\) bound on
the tree two-point kernel:
\[
  M_d=\sup_{p\le p_c}\|T_p\|_{2\to2}<\infty.
\]
If \(f=\mathbf 1_{K\setminus K_0}\), then
\[
  \chi_p|K|\mathcal C_p
  \le
  \sum_{z\in S_r}(T_pf(z))^2
  \le
  M_d^2|K|.
\]
Since \(\chi_p\to\infty\) as \(p\uparrow p_c\), the convolution term is
uniformly small near criticality.

## Result

Added `prop:tree-local-separator-convolution`: regular trees satisfy the local
separator-convolution property near criticality.

This proves that the corrected local separator abstraction is calibrated on the
basic nonamenable model.  The proof uses a feature the general case lacks:
uniform \(L^2\)-boundedness of \(T_p\) up to \(p_c\).
