# Independent audit of the general H3 shifted-response sum of squares

2 October 2026. heat_entropy independently read every step of
`H3_CONDITIONAL_WARD_DRAFT.md`, compared it with a separate derivation, and
found no gap. This is a partial high-fugacity coefficient result. It does not
solve the complete forest negative-correlation conjecture or its remaining
all-orders high-fugacity equality cases. Historical novelty is not certified.

## Analytic audit: PASS

The following dependencies were independently checked:

* The all-orders normalized forest identity follows from the rooted-forest
  feature bijection: vertices minus edges in each non-root component equals
  one. In particular the fourth forest ratio is the third Grassmann moment
  divided by 3!, without an additional component-size factor.
* The full response matrices have exactly the contrast ranges of their port
  sets. H2=0 makes these ranges Green-orthogonal, and two shared ports would
  contradict positive definiteness. The root can therefore be chosen in the
  e-port set outside the f-port set.
* The raw f-side integral is invariant under both odd transformations. The
  interior vertex measure cancels the odd derivative divergence. Marked
  variation of the local Dirichlet Schur complement is zero; the remaining
  determinant derivative is a boundary-field constant.
* The contraction sign is \(\bar Q_0Q_0=-D_{\mathbf1}\). The second score obeys
  \(D_{\mathbf1}u_{f,2}=-\bar\psi B_f\psi\). This yields the positive
  covariance correction \(k_g^2\operatorname{tr}(TB_f)\), which must then be
  subtracted from the unshifted wedge energy.
* The bilinear part of the first boundary tilt has zero triple cumulant
  because the whitened response matrices have product zero. Each uncontracted
  quartic edge term contributes the negative of a response-potential wedge
  square. There is no factor of two.
* The two response potentials have general zero-sum multiport charges. Their
  wedge flow has divergence minus the opposite-port constant times the
  f-charge. Subtracting the corresponding electrical energy completes the
  shifted wedge square, without assuming dipole sources.
* Activity derivatives introduce exactly two powers of common fugacity in
  the denominator. Lower-coefficient vanishing makes the partition-function
  prefactor irrelevant to H3.

The separate local Ward calculation is preserved in
`H3_WARD_IDENTITY_HEAT.md`. It records the grounded-port restriction explicitly.
The final draft chooses its root so this restriction is satisfied.

## Exact independent forest checks: PASS

`H3_response_wedge_heat.py/.json` compares complete acyclic-subset Rayleigh
coefficients with a separately constructed exact grounded Green response
formula. All seven cases have H0=H1=H2=0 and match the proposed H3:

| Graph | Exact H3 |
|---|---:|
| K4 chain with four layers | 64 |
| K4 chain with five layers | 0 |
| Asymmetric rank-one core, equal pair scalings | 2160000 |
| Same core, pair scalings (2,3,4,5) | 2916000000 |
| Same core, rational pair scalings | 195300 |
| Rank-one core with 3+2 boundary vertices | 171822643200 |
| Non-twin mirrored path active support | 34560000 |

`H3_positive_offdiag_audit_heat.py/.json` supplies an eighth, harder test with
11 vertices and 29 unmarked edges. Its e-response matrix has the verified
positive off-diagonal entry
\(268067/31510540800\), so it cannot be a nonnegative sum of ordinary edge
Laplacians. The candidate nonetheless matches the exact full forest value

\[
 H_3=42689908537165440000.
\]

All five common-zero roots and three marked-conductance pairs agree for that
case. Its forest coefficients use `forest_frontier_dp_heat.py`, a connectivity
dynamic program that rejects every cycle-closing edge and retains marked
endpoint connections. The entire polynomial from this routine was separately
compared with direct forest enumeration on each of the seven smaller cases;
all matched exactly. No Grassmann or Laplacian identity is used on the
coefficient side of these tests.

The K4 chain with five layers is a useful scope check: it has H3=0 and a later
positive leading coefficient. The proved H3 formula does not supply that later
coefficient, so an all-orders conclusion remains a separate task.
