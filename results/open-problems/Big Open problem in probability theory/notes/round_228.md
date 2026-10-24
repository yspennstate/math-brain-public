# Round 228

Round 228 packages the overshoot amplification into a finite far-tail ladder.

Choose cutoffs
\[
  \lambda_0<\lambda_1<\cdots<\lambda_N,
  \qquad \lambda_0>\rho/2,
\]
and set
\[
  \sigma_i=\lambda_{i+1}/2.
\]
At level \(\lambda_i\), Round 226 gives
\[
  \mathfrak Y_{Q,\lambda_i}
  \le
  \mathfrak O_{Q,\lambda_i,\sigma_i}
  +
  \sum_j\mathfrak V_{Q,\lambda_i,\sigma_i,\beta_i,j}.
\]
Round 227 absorbs the overshoot term into the next far tail:
\[
  \mathfrak O_{Q,\lambda_i,\sigma_i}
  \le
  \mathfrak Y_{Q,\lambda_{i+1}}.
\]
Iterating yields
\[
  \mathfrak Y_{Q,\lambda_0}
  \le
  \mathfrak Y_{Q,\lambda_N}
  +
  \sum_{i<N}\sum_j
  \mathfrak V_{Q,\lambda_i,\lambda_{i+1}/2,\beta_i,j}.
\]

Thus an initial far-tail estimate is reduced to a terminal deeper far tail
and finitely many heavy-slab estimates.
