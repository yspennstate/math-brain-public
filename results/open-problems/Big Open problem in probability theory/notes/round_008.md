# Round 008 log

Date: 2026-06-08

## Focus

Stress-tested the global SAW \(L^2\) operator gap on amenable graphs.

## Result

For a connected transitive amenable graph of bounded degree,
\[
  \gamma_{\rm SAW,2}(G)=\mu(G),
\]
where \(\mu(G)\) is the ordinary connective constant.

Since the standard self-avoiding-path union bound gives
\[
  p_c(G)\ge 1/\mu(G),
\]
the strict gap
\[
  \gamma_{\rm SAW,2}(G)<1/p_c(G)
\]
cannot hold on amenable transitive graphs.

## Proof idea

For fixed \(n\), the length-\(n\) SAW kernel \(C_n\) has row and column sums
\(c_n\), so Schur's test gives
\[
  \|C_n\|_{2\to2}\le c_n.
\]
Amenability supplies finite sets \(F_k\) with \(n\)-interiors occupying
\((1-o(1))|F_k|\).  Testing \(C_n\) against \(\mathbf 1_{F_k}\) gives
\[
  \|C_n\|_{2\to2}\ge c_n(1-o(1)).
\]
Thus \(\|C_n\|_{2\to2}=c_n\) for every fixed \(n\), and taking \(n\)th roots
gives the result.

## Interpretation

This is a guardrail for Route A7.  On amenable graphs, Folner sets turn the
\(\ell^2\) SAW operator norm into ordinary row-sum growth, so the operator-gap
criterion cannot accidentally imply the false conclusion \(p_c<p_u\) in
amenable transitive settings.

## Next target

Stress-test Route A7 on \(T_d\times H\).  The key issue is whether the tree
factor enforces a tree-like \(L^2\) exponent, or whether mixed SAWs in the
amenable direction make \(\gamma_{\rm SAW,2}<1/p_c\) too strong for product
graphs.
