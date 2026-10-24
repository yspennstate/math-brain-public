# Round 230

Round 230 packages the finite far-tail ladder together with the Round 229
token splits.

For a ladder
\[
  \lambda_0<\lambda_1<\cdots<\lambda_N,
  \qquad \sigma_i=\lambda_{i+1}/2,
\]
and fixed slab widths \(\beta_i\) and congestion thresholds \(K_i\), the
initial far tail satisfies
\[
\begin{aligned}
  \mathfrak Y_{\lambda_0}
  \le
  \mathfrak Y_{\lambda_N}
  &+
  \sum_{i,j}\mathfrak V_{i,j}^{\rm hor}
  +
  \sum_{i,j}\mathfrak V_{i,j,K_i}^{\rm in,spr}
  +
  \sum_{i,j}\mathfrak V_{i,j,K_i}^{\rm in,con}.
\end{aligned}
\]

Thus the current far-tail obstruction has four explicit pieces:

1. a terminal deeper far tail;
2. horizontal-heavy slabs;
3. inward-heavy slabs spread over many levels;
4. inward-heavy slabs congested through one level, equivalently many exterior
   return segments through that level.

The next real mathematical task is to prove an exponential saving for one of
these pieces, most plausibly by turning the spread/congested alternatives into
annular boundary-energy information.
