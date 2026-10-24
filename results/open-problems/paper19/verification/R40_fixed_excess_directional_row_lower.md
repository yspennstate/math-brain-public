# R40 verification - fixed-excess directional-row lower side

Date: 2026-06-28.

Scope: fixed \(r\ge0\), \(p=r+1\), independent rows over \(\mathbb R\) or
\(\mathbb C\) with affine one-dimensional directional small-ball bounds.
Target result:
`rect:row-block-certificate` and `rect:directional-row-fixed-excess`.

## Five-agent audit

Exactly five read-only agents were launched.

- Avicenna (`019f0d59-0161-7ba1-955d-e047dc30288f`) found that the naive tall-row
  negative-second-moment argument is invalid: after deleting one row from an
  \((m+r)\times m\) matrix, the remaining rows usually still span all of
  \(\mathbb F^m\).  This killed the rank-\(p\) one-row projection version.
- Ramanujan (`019f0d59-0241-77f1-810c-4a558ad9f534`) identified the correct
  pair-sum row budget:
  \[
    \sum_{|T|=m+r}\sum_{S\subset T,\ |S|=p}\prod_{i\in S}L_i
    =
    \binom{N-p}{m-1}\sum_{|S|=p}\prod_{i\in S}L_i,
  \]
  with the \((d_\mathbb F p/2)\log m\) slack coming from the
  \(\sqrt m\) singular-vector certificate.
- Parfit (`019f0d59-031e-7161-aa10-3048e8290d37`) checked placement against the
  existing fixed-excess heterogeneous density material and warned against
  conflating this lower-side result with the two-projection pair-correlation
  machinery.
- Gibbs (`019f0d59-03f9-7a01-ae94-83344c305c16`) supplied the safe row-block
  formulation: condition on \(m-1\) rows, take their complex- or real-linear
  unit normal, and use the \(p=r+1\) remaining independent scalar projections.
- Socrates (`019f0d59-04d3-7e02-85b7-fd8cd9f3d405`) checked downstream wording:
  fixed-excess lower side only, log-concave corollary allowed for fixed \(r\),
  no exact law or supercritical Balan--Wang theorem.

## Main deterministic check

For \(B\in\mathbb F^{(m+r)\times m}\), set \(n=m+r\).  For every
\((m-1)\)-row block \(U\), let
\[
  \Delta_U=\det(B_U B_U^*).
\]
If \(\Delta_U>0\), let \(u_U\) be a unit normal to the span of the rows in
\(U\).  The cofactor identity gives
\[
  \Delta_U |\langle R_i,u_U\rangle|^2
  =
  \det(B_{U\cup\{i\}}B_{U\cup\{i\}}^*),\qquad i\notin U .
\]
Summing over \(U\) and \(i\notin U\), each \(m\)-row minor is counted \(m\)
times:
\[
  \sum_U \Delta_U \sum_{i\notin U}|\langle R_i,u_U\rangle|^2
  =
  m\det(B^*B).
\]
Also
\[
  \sum_U\Delta_U
  =
  e_{m-1}(\sigma_1(B)^2,\ldots,\sigma_m(B)^2)
  =
  \det(B^*B)\sum_{j=1}^m\sigma_j(B)^{-2}.
\]
Thus the weighted average of the displayed squared row-block projections is at
most \(m\sigma_{\min}(B)^2\).  This proves the certificate with loss \(\sqrt m\).

## Probabilistic budget

For a fixed selected row set \(T\), the certificate plus row independence gives
\[
  \mathbb P\{\sigma_{\min}(A_T)\le t\}
  \le
  m^{d_\mathbb F p/2}t^{d_\mathbb F p}
  \sum_{S\subset T,\ |S|=p}\prod_{i\in S}L_{m,i}.
\]
Summing over \(T\) and applying the nonuniform finite-budget principle gives
the finite-budget threshold in `rect:directional-row-fixed-excess`.  The
summable almost-sure lower envelope is first Borel--Cantelli only.

## Guardrails

- This is not a rank-\(p\) one-row projection theorem.
- This is not an upper-side or exact fixed-excess law.
- The complex case uses complex-linear normals and scalar projections, with
  real exponent \(2p\).
- The log-concave application is fixed-\(r\) only; no uniform-in-\(r\) marginal
  constant is asserted.
