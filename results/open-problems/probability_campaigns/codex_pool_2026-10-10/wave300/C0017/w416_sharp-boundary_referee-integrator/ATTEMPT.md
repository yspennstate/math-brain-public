# C0017 referee attempt — exact symmetric crossing and boundary scope

## Source target

The intake asks for critical independent **bond** percolation on `Z^2` at `p=1/2`: Cardy's scaling limit for crossing probabilities and exploration-interface convergence to `SLE(6)`. Its source is Garban–Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Chapter II §4. Neither target clause is proved here. Current status remains UNKNOWN pending assessment of later claimed proofs.

## Exact symmetric crossing (known self-duality case)

Let `R_n` have vertices `(i,j)` with `0 <= i <= n` and `0 <= j <= n-1`, and every nearest-neighbor edge. Let `H_n` be an open path joining its left and right vertex sides under independent bond percolation with `p=1/2`. Then for every `n >= 1`, `P(H_n)=1/2`.

Proof: A planar primal/dual crossing alternative says exactly one of `H_n` and a top-to-bottom path of dual edges crossing closed primal edges occurs. Give the latter path dual vertices at the centers of the `(n)(n-1)` interior faces plus vertices just beyond the top and bottom sides. Each dual edge crosses exactly one primal edge relevant to the separating path. Rotating the dual graph by a quarter turn makes its left-to-right crossing event the same as an open crossing of `R_n`, except that vertical edges *along* the left and right vertex sides of `R_n` are absent. Such side edges cannot change a left-to-right crossing: trim any initial path segment along the starting side and any final path segment along the ending side. At `p=1/2`, the indicators that primal edges are closed are independent fair bits, so the dual crossing has the law of `H_n`. The two complementary events therefore have equal probability, both `1/2`.

After scaling by `1/n`, the rectangles tend to the unit square and their crossing probabilities are already `1/2`, agreeing with Cardy's symmetric value for that one conformal quadrilateral. This is a special case only; it gives no convergence for other shapes and no interface law.

## Boundary-scope counterexample

Let `S_n` be the induced subgraph obtained from `R_n` by deleting the entire vertex column `i=floor(n/2)` for `n>=2`. The rescaled vertex sets of `S_n` and `R_n` have Hausdorff distance exactly `1/n` (away from the tiny `n=2` edge convention the same bound suffices), and the left/right marked vertex sides are unchanged. Yet `S_n` is disconnected between left and right, hence its critical crossing probability is `0`, while `P(H_n)=1/2` on `R_n`. Thus Hausdorff convergence of embedded vertex sets and marked sides alone does not transfer crossing limits. Any bridge using such a limit must control graph connectivity/topology of its approximations. This refutes that auxiliary bridge, not C0017, because `S_n` is not the canonical induced approximation of the fixed unit square.

## Hardest open piece

Obtain a conformally covariant crossing law for general Jordan quadrilaterals for canonical square-lattice bond approximations, with boundary-arm control sufficient to pass to interfaces. Exact symmetry in one square does not determine the continuum law. A claimed interface proof must independently justify its observable identity and boundary convergence.
