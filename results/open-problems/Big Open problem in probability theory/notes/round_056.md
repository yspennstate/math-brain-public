# Round 056 log

## Goal

Calibrate the nonbacktracking bridge criterion from Round 055 against standard
directed-edge spectral control and against the regular tree.

## Directed-edge spectral sufficient condition

Added Corollary `cor:directed-edge-spectral-bridge`.  For a \(D\)-regular graph,
let \(\mathcal P_{\mathrm{NB}}\) be the nonbacktracking transition operator on
directed edges and define
\[
  \sigma_{\mathrm{NB},2}
  =
  \limsup_{m\to\infty}
  \|\mathcal P_{\mathrm{NB}}^m\|_{2\to2}^{1/m}.
\]
If
\[
  p_c(D-1)\sigma_{\mathrm{NB},2}<1,
  \qquad
  p_c(D-1)\sigma_{\mathrm{NB},2}\rho_{\mathrm{sph},2}<1,
\]
then \(p_c<p_{2\to2}\).

The proof bounds
\[
  \mathbb P_x^{\mathrm{NB}}(X_m=y)
  \le
  \|\mathcal P_{\mathrm{NB}}^{m-1}\|_{2\to2}
\]
using the initial uniform directed edge out of \(x\) and the indicator of
directed edges entering \(y\).  This gives an exponential bound on
\(B_n^{\mathrm{NB}}(p_c(D-1))\), and Round 055 applies.

## Tree calibration

Added Example `ex:regular-tree-bridge-calibration`.  On the \(D\)-regular tree,
a nonbacktracking walk from \(x\) can hit a vertex \(y\) at distance \(n\) only
by following the unique geodesic, and it hits at time exactly \(n\).  Therefore
\[
  B_n^{\mathrm{NB}}(s)=\frac1{D(D-1)^{n-1}},
  \qquad
  \lambda_c^{\mathrm{NB,br}}(T_D)=\frac1{D-1}.
\]
Since \(p_c(T_D)=1/(D-1)\) and
\(\rho_{\mathrm{sph},2}(T_D)=\sqrt{D-1}\), the bridge criterion gives the
strict factor \(1/\sqrt{D-1}<1\).

## Lesson

Global directed-edge spectral control is a useful sufficient condition, but
the regular tree confirms that the sharper object is the fixed-endpoint bridge
exponent \(\lambda_c^{\mathrm{NB,br}}\), not merely a global operator norm.
