# B12 / A058 — signed collision cocycle under adaptive activation

## Outcome

**PROVED, pending independent review:** the complete signed `U` collision
along any adaptive physical restriction tree telescopes exactly with its
actual changing reach weights.  Fixed coordinate order, uniform terminal
depth, and a positive activation lower bound are unnecessary.  The terminal
collision reserve is explicit.

**REFUTED:** the stronger local product-closure condition that would pay every
overlap node independently.  A certified three-bit pair has positive root
collision, zero collision in every one-coordinate child, and
`R_{a,b}=(3-b)C+a>0` for every `a>=0, 0<=b<1`.

**OPEN:** a global companion-sign/posterior/terminal allocation that pays all
simultaneous coordinate drifts once.  Universal GU and full FEI remain open.

## Frozen candidate and prior bound

Primary packet: `A058`; stable gap:
`B12-A058-SHARED-COORDINATE-OVERLAP`; attempt
`A058-GU-COLLISION-COCYCLE-09`.

The frozen candidate was the exact cocycle

\[
\Delta_iU(gh)-\Delta_iU(g)-\Delta_iU(h)
=C(g,h)-\tfrac12(C(g_{i,+},h_{i,+})+C(g_{i,-},h_{i,-})),
\]

followed by a weighted adaptive-tree telescope.  Previously, B12 had exact
GU closure only for reused deterministic character cores with disjoint
residual blocks.  Non-character posterior overlap and changing activation
were unpaid.

## Mathematical delta

For any branch-dependent adaptive restriction tree with reach weights `w_v`,

\[
\sum_{v\rm\ internal}w_v\delta_vC
=C_{\rm root}-\sum_{\ell\rm\ leaf}w_\ell C_\ell.
\]

This is dimension-, depth-, bias-, address-count-, overlap-count-, and
activation-gap-free.  It extends the zero-collision terminal class to all
trees whose leaves are disjoint-factorized or reused-character-core products.
No absolute values are inserted, and terminal terms are not discarded.

For `D_{a,b}=G-aI-bU`, the complete product identity is

\[
D_{a,b}(gh)=D_{a,b}(g)+D_{a,b}(h)
+LC(g,h)+2aJ(g,h)-bC(g,h).
\]

Iterating it displays the exact universal GU implication: if every Boolean
function has a composition forest with nonpositive leaf defects and
nonpositive **total signed** remainder for one fixed `a,b` with `b<1`, then
universal GU holds and the reviewed reduction yields
`H <= (2+2a/(1-b)) I`.

## Certified obstruction and why it matters

The truth tables

`g=(-1,-1,-1,-1,-1,1,1,1)` and
`h=(-1,1,1,-1,-1,1,1,-1)`

give

\[
C=\frac1{16}\log_2\frac{120^3 3^9}{2^{25}}>0,
\qquad LC=3C,\qquad J=\frac12.
\]

All one-coordinate child collisions vanish.  Therefore
`R_{a,b}=(3-b)C+a>0` for every admissible pair.  This removes the local
termwise-product route from the attack list.  It does not refute GU or FEI.
It forces the next proof to preserve companion signs and use a global
single-ownership reserve rather than paying each coordinate drift separately.

## Verification

`python3 CHECK.py` passed:

- all 65,808 ordered Boolean pairs in dimensions 1–3;
- 197,136 coordinate cocycle checks;
- 65,808 branch-data-dependent adaptive-tree telescopes;
- 2,000 additional random pairs through dimension 8 (up to 511 tree nodes);
- three frozen `(a,b)` defect identities;
- exact rational influence identities and the integer sign certificate for
  the three-bit witness.

Maximum observed errors were `2.23e-16` for the local cocycle, `8.89e-16`
for the global `G` identity, `3.56e-15` for the defect identity, and
`4.45e-16` for the adaptive telescope.

Finite verification is supporting evidence only; the proof is algebraic and
given in `PROOF.md`.

## Guard compliance

- No fixed-sign projection from an ensemble is used.
- No unsigned coefficient-four or larger-coefficient shortcut is assumed.
- Collision is proved sign-indefinite and kept signed throughout.
- The adaptive telescope pays one root collision only; it is not conflated
  with the all-coordinate `G` Laplacian.
- The positive local remainder is a helper falsifier, not an FEI
  counterexample.
- Normalized Boolean spectral laws, zero-mass convention, actual reach
  weights, joint-pivotal overlap, and terminal collision terms are explicit.

## Next unpaid step

Replace nodewise closure by a grouped-root mechanism: collect all coordinate
drifts incident to one posterior collision before spending its reserve, and
derive a companion-sign potential whose child terms cancel the multiplicity
`LC/C` while the `2aJ` cost is charged once.  The first mandatory test is the
certified three-bit witness above; the mechanism must also preserve negative
collisions instead of taking absolute values.

No independent review or native ingestion was observed.  Universal GU and
full FEI remain **OPEN**.
