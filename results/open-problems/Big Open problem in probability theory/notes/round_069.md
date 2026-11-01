# Round 069 log

## Goal

Make the bounded-degree finite-state detour certificate exact-checkable, in
parallel with the regular bridge certificate.

## Manuscript

Added Corollary `collatz-bounded-degree-detour`.  If the bounded-degree
detour-count finite-state bound holds, \(M v\le\lambda v\), and
\[
  (q\lambda)^2R<1,
\]
where \(R\ge\rho_{\mathrm{sph},2}(G)^2\), then
\[
  p_c(G)<p_{2\to2}(G).
\]

## Verifier

Extended `scripts/bridge_certificate_verify.py` with an explicit `criterion`
field:

- `regular_bridge`: checks \(\bigl(q(D-1)\lambda\bigr)^2R<1\).
- `bounded_degree_detour`: checks \((q\lambda)^2R<1\).

The default remains `regular_bridge`, so existing certificates keep their old
meaning.  Added a second tree certificate,
`research/certificates/regular_tree_D3_detour.json`, using
`criterion = "bounded_degree_detour"`.

## Calibrated majorization

Added the built-in `regular_tree_count_one_state` detour majorization check.
For a \(D\)-regular tree,
\[
  \sup_{\operatorname{dist}(x,y)=n}\sum_{k\ge0}q^kN_{n+k}(x,y)=1
\]
for every \(n\ge0\), because only the geodesic contributes.  The checker
verifies this against a one-state bound \(aM^nb\).
