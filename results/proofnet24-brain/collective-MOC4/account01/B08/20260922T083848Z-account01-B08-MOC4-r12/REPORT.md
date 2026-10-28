# account01/B08 MOC4 report — a zero-entry true-unitary facet obstruction to the universal common-compound lift

Run: `20260922T083848Z-account01-B08-MOC4-r12`  
Outcome: `CANDIDATE_REFUTED`; full MOC4 remains **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Source-exact target

For complex normal `4 x 4` matrices `A,B` with spectra `a_i,b_i`, prove

`det(A+B) in conv{ prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`.


## Exact current team state consumed

Latest complete campaign-lead snapshot read:
- account03/B07 run `20260922T060726Z-account03-B07-MOC4-r11`, theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`. At a global support maximizer, saturation `T=|C|` of one mixed-conformal Spin(4) gate gives a genuine flat coordinate `SU(2)` pair orbit and hence an equal-support zero-entry representative.

Named assigned OTHER-account result consumed and applied:
- account02/B09 run `20260922T064517Z-account02-B09-MOC4-r17`, theorem `MOC4-TRANSPOSE-TIE-SAFE-v1` and consequence `MOC4-SPIN4-SATURATION-EXCLUSION-v1`. It proves that a row/column transposition tie is target-safe; therefore every genuine positive-gap support maximizer has all twelve row/column pair drops strictly positive and every mixed-conformal gate strict `T>|C|`. Its first remaining zero-face target step is `MOC4-ZERO-FACE-STRICT-PAIR-RESERVE-v3`.

The present run attacks the B08 representation mechanism on that zero-entry branch. In particular it tests whether the partner's Haar-average zero-face lift can be upgraded to a pointwise positive law reproducing the same unitary's compound minors.

## Compound-minor notation

For `I,J subset {0,1,2,3}`, `|I|=|J|`, put

`Q_{I,J}(U)=|det U[I,J]|^2`,

and write `P_{ij}=Q_{{i},{j}}=|u_ij|^2`.

For a permutation `sigma`, viewed as mapping columns to rows, define

`P^sigma_ij = 1_{sigma(j)=i}`,

`Q^sigma_{I,J}=1_{sigma(J)=I}`.

A **positive common-compound lift** is a probability law `lambda_sigma>=0`, `sum lambda_sigma=1`, such that

`Q_{I,J}(U)=sum_sigma lambda_sigma Q^sigma_{I,J}`

for every equal-size pair `(I,J)` simultaneously. Such a law would give the desired determinant convex representation for every spectra pair by Cauchy-Binet.

## New exact theorem

### `MOC4-ZERO-FACE-COMMON-LIFT-FACET-NOGO-v1`

There exists a real orthogonal `4 x 4` matrix `U` with exactly one zero entry, `u_00=0`, and with all 36 two-by-two minors nonzero, for which no positive common-compound lift exists.

An exact witness is

```text
U = [
 [       0,    16/25,   -48/65,      69/325],
 [   16/25,  -72/125,   -33/65,    -48/1625],
 [ -69/325, 48/1625,    -16/65, -1536/1625],
 [   48/65,    33/65,    24/65,      -16/65]
].
```

It satisfies `U^T U=I` exactly. The only zero entry is `u_00`; every `2 x 2` minor is nonzero.

Define the linear functional, using zero-based pair labels,

`F(P,Q) = -P_01 + P_12 - P_20 - P_21`

`           + Q_{01,01} + Q_{02,01} + Q_{02,02}`.

Then every positive common lift on the zero face must satisfy

`F(P,Q) <= 0`,

but the displayed true orthogonal matrix has

`F(P(U),Q(U)) = 5810112/446265625 > 0`.

Therefore no positive law on the 24 permutations can reproduce even the degree-one and degree-two compound marginals of this true zero-entry unitary, hence no all-degree common-compound law exists.

### Proof of the facet inequality

If a positive common law reproduces `P_00=|u_00|^2=0`, then

`0=P_00=sum_{sigma: sigma(0)=0} lambda_sigma`.

By nonnegativity, every permutation with `sigma(0)=0` has zero weight. Only the 18 permutations with `sigma(0)!=0` may occur.

On each of those 18 permutation vertices, direct exact evaluation gives

`F(P^sigma,Q^sigma) in {0,-1}`.

The 12 tight permutations, in one-based image notation, are

`2134, 2143, 2413, 2431, 3124, 3214, 3412, 3421, 4123, 4213, 4231, 4321`,

and the six value `-1` permutations are

`2314, 2341, 3142, 3241, 4132, 4312`.

Hence every convex combination supported on the allowed 18 vertices has `F<=0`.

For the displayed exact rational orthogonal matrix, substitution into the same functional gives

`F=5810112/446265625 = 0.013019402962081159... >0`.

This is already a complete Farkas separation certificate.

Moreover the allowed joint `(P,Q)` permutation polytope has affine dimension 12 in the exact coordinate system used by `verify.py`, while the 12 tight vertices have affine dimension 11. Thus `F<=0` is genuinely facet-defining for this zero-face common-lift polytope, not an accidental redundant inequality.

Because the violation is strict, and all other entries and all 36 two-minors of the witness are nonzero, the failure persists on a relative open neighborhood inside the true-unitary hypersurface `u_00=0`.

## Exact verification

`verify.py` uses only Python standard-library exact `Fraction` arithmetic. It checks:

- exact orthogonality;
- the unique prescribed zero entry;
- nonvanishing of all 36 two-minors;
- all 18 allowed permutation-facet values;
- exact affine ranks 12 and 11;
- the exact positive facet gap.

Recorded output:

```text
orthogonal_exact=PASS
only_forced_zero_entry=PASS
all_36_two_minors_nonzero=PASS
allowed_vertex_values: zero=12 minus_one=6
joint_polytope_affine_dimension=12
tight_face_affine_dimension=11
facet_gap = 5810112/446265625
facet_gap_decimal = 0.013019402962081159
common_positive_all_compound_law=IMPOSSIBLE
```

## What this does and does not refute

This refutes the **universal pointwise same-unitary common-compound representation**, even on the zero-entry branch. It does **not** refute MOC4. A separating functional in the full joint `(P,Q)` space need not be realizable by the highly structured spectral coefficients coming from one determinant support direction.

It also explains why account02/B09's `MOC4-ZERO-FIBER-HAAR-LIFT-v1` must remain an averaged statement: Haar averaging a residual zero-face `U(2)` fiber can create a positive common lift although an individual true unitary in that same geometric regime need not possess one.

## A strictly weaker representation that is still sufficient

The failed common lift is stronger than MOC4 actually needs. Cauchy-Binet gives

`det(D_a+U D_b U*)`

` = sum_{k=0}^4 sum_{|I|=|J|=k} a_{I^c} b_J Q_{I,J}(U)`.

Suppose `lambda` is merely a Birkhoff decomposition of the degree-one matrix `P=|U|^2`, i.e.

`P_ij=sum_sigma lambda_sigma P^sigma_ij`.

Then degrees `k=0,1,3,4` already match automatically:

- `k=0,4` are constants;
- `k=1` matches by definition;
- for `k=3`, Jacobi complementary-minor duality for a unitary gives `Q_{I,J}(U)=Q_{I^c,J^c}(U)`, whose complements are singletons, and the same complement-event identity holds for every permutation law.

Thus only the **spectrally weighted degree-two term** remains.

For a unit-modulus support direction `eta`, define

`c_{I,J}=Re(conj(eta) a_{I^c} b_J)`, for `|I|=|J|=2`,

and let

`R_c(P)=max_{lambda>=0, sum lambda=1, sum lambda P^sigma=P}`

`           sum_sigma lambda_sigma sum_{|I|=|J|=2} c_{I,J} Q^sigma_{I,J}`.

Then the single inequality

`sum_{|I|=|J|=2} c_{I,J} Q_{I,J}(U) <= R_c(P(U))`

implies

`h_eta(U)<=sum_sigma lambda_sigma H_sigma<=M_eta`

for a maximizing Birkhoff decomposition. Therefore this weighted roof is enough for the target support inequality while requiring no simultaneous reproduction of the full `Q` array.

Its finite LP dual is

`R_c(P)=min_alpha sum_ij alpha_ij P_ij`

subject to

`sum_j alpha_{sigma(j),j} >= C_sigma`

for every `sigma in S_4`, where

`C_sigma=sum_{|I|=|J|=2} c_{I,J}Q^sigma_{I,J}`.

The new facet counterexample shows that this roof inequality is false for arbitrary coefficient arrays `c`; the missing proof must use the actual spectral product structure of `c`, not merely bistochasticity or a generic low-rank surrogate.

## Compact conditional end-to-end argument after applying the partner result

Assume a zero-entry support maximizer `U_*` were target-violating.

1. By account02/B09 `MOC4-TRANSPOSE-TIE-SAFE-v1`, all row/column pair drops are strict; a flat/tied pair is already MOC-safe.
2. By its `MOC4-SPIN4-SATURATION-EXCLUSION-v1`, every mixed-conformal gate is strict `T>|C|`.
3. A universal pointwise common-compound lift cannot be invoked: the exact theorem above disproves that route on the true zero face.
4. It is nevertheless sufficient to prove the **spectral weighted degree-two roof inequality** above for zero-entry global maximizers satisfying the strict-pair conditions. The remaining determinant degrees then match from the same Birkhoff law automatically, giving `h_eta(U_*)<=M_eta`, contradiction.

This isolates the first representation-theoretic missing implication without replacing the target by an arbitrary stochastic surrogate.

## First essential missing implication

### `MOC4-ZERO-FACE-SPECTRAL-ROOF-v1`

For every true unitary `U_* in U(4)` with at least one zero entry, every complex spectra pair `(a,b)`, and every support direction `eta`, assume `U_*` is a global maximizer of the corresponding determinant support functional and that all coordinate row/column pair orbits are strictly curved (equivalently, on a hypothetical positive-gap branch, the strict pair conclusions of account02/B09 r17 hold). Then

`<c,Q^(2)(U_*)> <= R_c(P(U_*))`

for the actual spectral coefficients

`c_{I,J}=Re(conj(eta) a_{I^c}b_J)`.

A proof closes the strict zero-entry representation branch. A disproof must use an actual zero-entry unitary, actual complex spectra, one common support direction, and the exact maximizing condition; a generic joint-polytope separating normal such as the facet above is no longer sufficient.

## Status

`CANDIDATE_REFUTED` for the universal pointwise common-compound lift. The parent MOC4 statement remains **OPEN**. The useful surviving representation route is now the strictly weaker spectral weighted Birkhoff roof, to be combined with the partner's strict-pair reserve and the lead's mixed-Hessian/strict-interior analysis.
