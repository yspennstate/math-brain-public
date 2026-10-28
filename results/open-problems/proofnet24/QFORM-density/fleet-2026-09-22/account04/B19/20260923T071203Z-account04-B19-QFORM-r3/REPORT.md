SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 04, slot B19, 2026-09-23T07:12:03Z.
attacking: end-to-end proof assembly and the heavy-hub incident-E2-to-L-infinity implication.

# account04/B19 — correction-safe proof graph and an exact no-interpolation obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `ESSENTIAL_STEP_APPLIED / PROOF_GRAPH_ASSEMBLED / CANDIDATE_SHORTCUT_REFUTED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved or disproved. This report assembles the current route without transferring incompatible hypotheses, applies account01/B19's newest compound-energy theorem at its actual quantitative outputs, and proves that those outputs cannot be upgraded to (L^infty) by functional interpolation alone. The remaining implication must use additional original-coordinate structure.

## 1. Source boundary

Fresh control was read from `math-research-brain` main at
2026-09-22.15. The correction inbox remains at
`c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

The Claude inputs are used at their proved scopes:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
  `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
  This contains Theorem D, D' (with marginal threshold (h<3/4)),
  the finite-dimensional estimates, mixed Fresnel/hub tools, and the
  ruled-side theorem. It explicitly says the conjecture is open.
- The corrected synthesis and Gaussian-padding/N3 reduction are at
  `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`.
  It does not prove N3.
- The one-sheet ruled estimate is independently realized at
  `math-open-problems@6cc61cf326bd672c2177cc0411a5ce7291eafe16`.
  For signature ((2,1)), it bounds only (sge0) by (pisqrt2);
  signs reverse for ((1,2)).
- The newest designated account01/B19 result is
  `math-open-problems@d037aee47f5f73abf078021e69478a2ebece1700`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T035138Z-account01-B19-QFORM-r11/REPORT.md`.

## 2. Compact noncircular proof graph

The current graph is a conditional reduction, not a full proof.

### G0. Full matrix to corrected finite-dimensional/N3 frontier

The Gaussian-padding reduction in the corrected Claude synthesis sends the
full theorem to the N3 statement while retaining all additional spectrum.
This edge is one-way: no exact-rank-three theorem may simply be convolved
with the remaining quadratic form, because rotation destroys product
independence and the tail need not be independent.

### G1. Volume/Fourier exits

For an original-coordinate cross block (M=A_{IJ}):

- Theorem D pays a quantitative third-volume packet
  (e_3(M^TM)>0) under its marginal gate.
- D' enlarges the permitted marginal threshold to any (h<3/4), with
  the explicit factor ((2h)^{-1/2}(3-4h)^{-1}).
- The D5/fifth-volume alternative applies only where its stated higher
  compound packet exists; it is not inferred from three large eigenvalues
  alone.
- Theorem F/full-basis estimates pay diffuse exact-rank-three frames.
  Account04/B18 gives, for example, the product-valid cap (3e) in its
  low-shear diffuse scope.

These branches retain arbitrary self blocks and outside couplings exactly
where the cited theorem says so.

### G2. Hub and finite-dimensional exits

Localized states are routed to genuine original-coordinate pivots or hubs.

- A quantitative physical diagonal is paid by the completed pivot theorem.
- Mixed-hub and mixed-Fresnel theorems pay a hub plus sufficiently spread
  residual directions.
- The account04/B10 three-bank split
  `afdea9634d9e3f5fb09659da436292cf7dbe5b20`
  pays (max(	au_J,	au_K)ge1/100) by (44.417), but leaves the
  punctured convex collar.
- The ruled theorem pays the one-sheet side only. The definite and
  two-sheet convex sides remain separate.
- The finite-dimensional spectral theorem supplies dimension-dependent
  or bounded-dimension closure at its stated scale, but no uniform
  bounded-dimensional theorem BD(m) is presently proved for arbitrary
  (m).

### G3. Schur/compound-energy frontier

Account01/B19's newest theorem applies to a co-heavy original coordinate
(i) in the exact-rank-three core. If (|A_{ii}|ge1/8), the branch is
paid by (<337). Otherwise its star (m=A[i,-i]) satisfies
[
|m|^2>rac{29}{192}. 	ag{2.1}
]
The arbitrary-hub theorem then gives
[
sup_zPr(|Q-z|learepsilon)<7.631sqrtarepsilon. 	ag{2.2}
]
The same source proves the compound-energy dichotomy
[
max(D_i,O_i)gerac{29}{384}. 	ag{2.3}
]
In the disjoint alternative a product-preserving partition captures
[
Delta_2(B_{JK})gerac{29}{3072}. 	ag{2.4}
]
When one cross-range side has leverage at most (2/3), the completed
fractional-E2 theorem yields
[
|p_Q|_3<12.511. 	ag{2.5}
]
Equations (2.2) and (2.5) are the actual account01/B19 outputs consumed
below. Neither is relabelled as an (L^infty) theorem.

## 3. The tempting interpolation edge is false

### Theorem 3.1 — `QFORM-L3-PLUS-HALF-HOLDER-NOT-LINFINITY-v1`

There is a sequence of probability densities (p_N), (Nge2), such that
[
|p_N|_3le2^{1/3}, 	ag{3.1}
]
[
sup_zint_{z-arepsilon}^{z+arepsilon}p_N(x),dx
le3sqrtarepsilonqquad(arepsilon>0), 	ag{3.2}
]
but
[
|p_N|_infty=Nlongrightarrowinfty. 	ag{3.3}
]

Thus even bounds strictly stronger than the numerical outputs
(2.2),(2.5) do not imply a universal density cap.

#### Proof

Define
[
p_N(x)=N,1_{[0,N^{-3}]}(x)
 +(1-N^{-2}),1_{[2,3]}(x). 	ag{3.4}
]
Its total mass is (N^{-2}+1-N^{-2}=1). Moreover
[
|p_N|_3^3
=N^3N^{-3}+(1-N^{-2})^3le2, 	ag{3.5}
]
while its essential supremum is (N).

For an interval (I=[z-arepsilon,z+arepsilon]), the baseline part
contributes at most (min(1,2arepsilon)). For
(0<arepsilonle1), this is at most (2sqrtarepsilon), and for
(arepsilonge1) the entire probability is at most
(1lesqrtarepsilon).

The spike contributes at most
[
min(N^{-2},2Narepsilon). 	ag{3.6}
]
Dividing (3.6) by (sqrtarepsilon), the maximum occurs where the two
arguments agree, at (arepsilon=(2N^3)^{-1}), and equals
(sqrt2,N^{-1/2}le1). Hence the spike contributes at most
(sqrtarepsilon). Combining the two parts proves (3.2). QED.

The same example may be mollified without changing the conclusion or the
constants by more than an absolute factor. Therefore discontinuity of
(3.4) is irrelevant to the obstruction.

## 4. Consequence for the live proof graph

The edge
[
igl[	ext{hub }sqrtarepsilon	ext{ bound}igr]
+igl[	ext{aggregate-E2 }L^3	ext{ bound}igr]
Longrightarrow L^infty 	ag{4.1}
]
is false as a purely analytic implication. Account01/B19 has supplied
real curvature and real anti-concentration, but the proof still needs a
structural mechanism forcing the two resources to act on the same scale
and the same original-coordinate decomposition.

Accordingly, the first missing implication is not generic interpolation.
It is the following narrower statement.

### `QFORM-HEAVY-HUB-COUPLED-SCALE-TRANSDUCER-v1` — OPEN

Under (2.1)--(2.4), use the common quadratic-form provenance to prove one
of:

1. a Fourier decay estimate in which the hub factor and aggregate E2
   factor multiply before absolute values are integrated;
2. a product-preserving decomposition into an independent square channel
   and a zero-self/Frobenius channel;
3. an exhaustive high-leverage localization exit to the already-paid
   physical-pivot, mixed-hub, ruled-side, or convex-chain branches.

The theorem must retain arbitrary self curvature, arbitrary extra
spectrum, and all signs. It cannot be replaced by (4.1), a worst
conditional-density supremum, or independence after rotation.

## 5. Completion status

The current graph covers substantial diffuse, volume, hub, pivot,
one-sheet, exact-graph, and special convex-chain branches. It still has
two genuine open interfaces:

- the coupled-scale heavy-hub transducer above, including the
  arbitrary-self matching-bank case;
- the punctured convex/two-sheet near-null collar and its interaction
  with additional spectrum.

Therefore there is no full candidate proof to submit for two end-to-end
reviews in this run. Requesting such reviews now would mislabel a
conditional graph as a completed theorem. Once both interfaces are
closed, two independent full reviews remain mandatory.

Continuity is not proved globally.
