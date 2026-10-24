# Round 070 log

## Goal

Add the path-decomposition template for the bounded-degree raw-count
certificate, not only the regular bridge-probability certificate.

## Bounded-degree path-sum detour certificate

Added Proposition `bounded-degree-path-sum-detour`.  For each endpoint pair
\(\operatorname{dist}(x,y)=n\), a graph-specific computation may injectively
encode every nonbacktracking walk \(\gamma:x\to y\) of length \(n+k\) as
\[
  \sigma_0,f_1,\sigma_1,\ldots,f_n,\sigma_n,
\]
with the convention that for \(n=0\) the data is just \(\sigma_0\).  If
\[
  q^k
  \le
  \mu_{x,y}(\sigma_0)\prod_{r=1}^n w_{r,x,y}(f_r)h_{x,y}(\sigma_n),
\]
and the phase transfer sums satisfy \(K_{r,x,y}\le M\), then
\[
  \sum_{k\ge0}q^kN_{n+k}(x,y)\le a^TM^nb.
\]
The bounded-degree finite-state detour certificate then gives
\[
  q\rho(M)\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c(G)<p_{2\to2}(G).
\]

## Role

This is the graph-specific proof template closest to the full target: it uses
raw nonbacktracking counts and does not require regularity or normalized
nonbacktracking transition probabilities.
