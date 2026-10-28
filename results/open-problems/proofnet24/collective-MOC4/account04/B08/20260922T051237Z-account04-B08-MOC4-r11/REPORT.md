# MOC4 account04/B08 — cubature-roof rigidity and exact boundary degeneracy

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T051237Z-account04-B08-MOC4-r11`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira scope  
**Role:** account04/B08, extremal boundary / degeneracy  
**Assigned partner:** account01/B09  
**Team lead:** account03/B07  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`

This revision corrects an escaping-only Markdown defect in the first same-run report write. Git history preserves that first write; the mathematical content below is the canonical complete run report.

## 1. Source-exact target and exact inputs consumed

For complex normal 4-by-4 matrices, after diagonalizing one matrix, the target is to prove for every true unitary U in U(4)

`det(D_a + U D_b U*) in conv{ z_σ : σ in S_4 }`, where `z_σ = product_i (a_i + b_{σ(i)})`.

Equivalently, for every real support direction η, define

`h(U) = Re(η det(D_a + U D_b U*))`, `H_σ = Re(η z_σ)`, and `M = max_σ H_σ`.


This run reads and applies two complete other-worker artifacts.

1. **Team lead account03/B07**, run `20260922T043708Z-account03-B07-MOC4-r11`, results `MOC4-TRANSPOSE-SUBGROUP-ROOF-v1` and `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`. Canonical report: `proofnet24/collective-MOC4/account03/B07/20260922T043708Z-account03-B07-MOC4-r11/REPORT.md`, first report commit `8cfdbf5fee45e451d600835a63a5349e0a8f5125`, report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`. It proves that every transposition-containing subgroup average of a genuine unitary orbit has a positive common endpoint lift, and gives the exact seven-subgroup cubature formula used below.

2. **Assigned other-account partner account01/B09**, run `20260922T044740Z-b09-moc4-r11`, result `MOC4-HADAMARD-FIBER-LIFT-v1`. Canonical report: `proofnet24/collective-MOC4/account01/B09/20260922T044740Z-b09-moc4-r11/REPORT.md`, commit `36de7522248c90772c09d518119c07b0531e96a5`, report blob `9b496cd2cb18df7a577ab0997de1117a8c144c98`. It gives a genuine complex-Hadamard one-parameter family with fixed `P=|U|^2=J/4` but varying exterior-square data, proves an exact positive endpoint lift on that family, and refutes any universal full coefficient rule depending only on `(P,a,b)`.

No individual-unitary positive permutation lift is assumed here.

## 2. Compact conditional end-to-end argument

If MOC4 fails, support separation and compactness of U(4) give a direction η and a global genuine-unitary maximizer U_* with `h(U_*) = M + γ`, `γ > 0`.

The current lead theorem bounds h(U) by seven exact subgroup roofs on either physical relabeling side. The first remaining question is whether a putative violating maximizer can sit on the boundary of that cubature relaxation. The present run proves that, except for an explicit endpoint-face degeneracy, it cannot: equality at any uniquely exposed subgroup roof forces a proper coordinate block decomposition of the true unitary, and every such block configuration is already MOC4-safe by the known dimensions at most three.

Therefore a violating unitary that saturates the lead cubature ceiling can exist only when **all seven relevant endpoint coset roofs are tied**. On the lead/partner hard exact datum, all fourteen left/right roofs are uniquely exposed, so every hypothetical violator is strictly inside both cubature ceilings.

The remaining universal step is genuinely nonlinear and strict-interior: use same-unitary `P-R-D` compatibility plus the global-maximizer stationarity/Hessian constraints to exclude a positive gap strictly below the endpoint-only ceiling. The cubature boundary itself is no longer an unexplained generic obstruction.

## 3. The lead's seven subgroup roofs

Use the lead's zero-based labels and subgroups:

- `H1 = <(03),(12)>`, size 4;
- `H2 = <(01),(0213)>`, size 8;
- `H3 = <(12),(13)>`, size 6;
- `H4 = <(01),(23)>`, size 4;
- `H5 = <(02)>`, size 2;
- `H6 = <(03),(0132)>`, size 8;
- `H7 = <(01),(03)>`, size 6.

Fix one physical relabeling side, row or column, throughout. Let

`A_j(U) = (1/|H_j|) sum_{g in H_j} h(g · U)`

and let `rho_j` be the maximum endpoint-support average over the corresponding left or right H_j cosets. The lead proves `A_j(U) <= rho_j` through a positive H_j-invariant common lift of the **averaged genuine compound-minor data**. It also proves the exact cubature identity

`h(U) = (1/3)A_1 + (1/3)A_2 + (1/2)A_3 + (1/3)A_4 + (2/3)A_5 + (1/3)A_6 + (1/2)A_7 - 2m`,

where `m = (1/24) sum_σ H_σ`. Hence

`h(U) <= Lambda = (1/3)rho_1 + (1/3)rho_2 + (1/2)rho_3 + (1/3)rho_4 + (2/3)rho_5 + (1/3)rho_6 + (1/2)rho_7 - 2m`.

All seven coefficients are strictly positive.

## 4. New theorem: unique subgroup-roof saturation forces a safe coordinate block

### Theorem — `MOC4-CUBATURE-ROOF-RIGIDITY-v1`

Fix `j in {1,...,7}` and one physical relabeling side. Suppose the endpoint H_j-coset average has a **unique** maximizing coset `C_*`. If a true unitary U saturates that subgroup roof, `A_j(U)=rho_j`, then, after row/column permutation and diagonal phase changes, U preserves a proper coordinate block decomposition of type `2+2`, `3+1`, or `2+1+1`.

More specifically, H1 and H4 force `2+2`; H5 forces `2+1+1`; H3 and H7 force `3+1`; and H2 and H6 force `2+2` through the exterior-square channel. Consequently `h(U) <= M` for every complex spectra a,b and every support direction, including repeated spectra and singular sums.

### Proof

The lead's subgroup-roof theorem supplies an H_j-invariant probability law ν on S_4 whose singleton and compound marginals equal the averaged genuine-unitary data and whose endpoint expectation equals `A_j(U)`. Any H_j-invariant law is a convex combination of uniform laws on the relevant H_j cosets. Thus

`A_j(U) = sum_C q_C avg_C(H)`, with `q_C >= 0` and `sum_C q_C = 1`.

If the maximizing coset C_* is unique and `A_j(U)=rho_j`, equality in this convex combination forces `q_{C_*}=1`. Therefore **all** averaged compound-minor data, not just their scalar support value, equal the marginals of the uniform law on C_*.

For H1,H3,H4,H5,H7, look first at singleton marginals. Their point-orbit sizes are respectively `(2,2)`, `(1,3)`, `(2,2)`, `(1,1,2)`, `(1,3)`. A uniform coset law has zero singleton marginal across distinct corresponding orbit blocks. On the genuine side, the same marginal is an average of entries `|u_rs|^2`, all nonnegative, with only one row or column index permuted by the subgroup. A zero averaged entry is a sum of nonnegative quantities equal to zero, so every constituent cross-block entry vanishes. This forces U, up to the fixed row/column relabelings, to have exactly the claimed block pattern.

The transitive point actions H2,H6 are the important exceptional case: their singleton marginal is full, so level-one data alone cannot force a block. Here use the two-subset marginal `R_{I,J}=|det U[I,J]|^2` for `|I|=|J|=2`.

For each of H2,H6, the action on the six two-subsets has exactly two orbits, of sizes 2 and 4; the size-two orbit consists of a complementary pair `{I,I^c}` after relabeling. The uniform maximizing coset therefore has zero R-mass between the size-two and size-four orbit classes. Again, the averaged genuine entries are nonnegative, so equality of the compound marginals forces the corresponding cross-orbit minors of the original U to vanish.

Choose I in the size-two source orbit. Then the decomposable bivector `(wedge^2 U)e_I` has no coordinates except possibly on a complementary target pair `{J,J^c}`:

`(wedge^2 U)e_I = alpha e_J + beta e_{J^c}`.

A vector of this form is decomposable only if one coefficient vanishes, because its exterior square equals `+/- 2 alpha beta e_0123`. Thus `alpha beta=0`. Since `wedge^2 U` is unitary, the vector is nonzero, so the coordinate two-plane indexed by I is mapped onto one coordinate two-plane indexed by J or J^c. Unitarity maps the orthogonal complementary two-plane to its complement. Hence U is `2+2` block diagonal up to coordinate permutations and phases.

It remains to justify target safety. For any proper block decomposition above, `D_a + U D_b U*` decomposes into blocks of sizes at most three. The campaign source record includes the known n=3 Marcus–de Oliveira case; n=1,2 are elementary. Each block determinant is therefore a convex combination of the permutation products internal to that block. Multiplying the blockwise convex combinations gives a convex combination of full S_4 endpoint products, restricted to permutations respecting the blocks. Hence the full determinant lies in the required hull. No invertibility or spectral simplicity was used. QED.

## 5. Exact boundary characterization for the lead cubature ceiling

Define subgroup slacks `s_j(U)=rho_j-A_j(U) >= 0`. Subtracting the exact cubature identity from its roof bound gives

`Lambda - h(U) = (1/3)s_1 + (1/3)s_2 + (1/2)s_3 + (1/3)s_4 + (2/3)s_5 + (1/3)s_6 + (1/2)s_7`.

Therefore equality `h(U)=Lambda` forces **every** `s_j=0`.

### Corollary — `MOC4-CUBATURE-BOUNDARY-DEGENERACY-v1`

If a true unitary is a support violator, `h(U)>M`, and saturates a seven-subgroup cubature ceiling, then for that physical relabeling side **every one of the seven endpoint subgroup roofs must have at least two maximizing cosets**.

Indeed, equality saturates all seven subgroup roofs. If even one roof has a unique maximizing coset, the theorem makes U block-safe and gives `h(U)<=M`, a contradiction.

Thus generic cubature-boundary saturation is removed from the residual proof. The only possible violating equality configuration is an explicit endpoint-face degeneracy: seven simultaneous coset-roof ties on the active side. This condition depends only on the 24 endpoint support values and can be treated separately from strict-interior same-unitary stationarity.

## 6. Exact application to the current hard positive-reserve datum

Use the exact simple spectra retained by the lead and partner:

`a=(-4+4i,-i,-3+2i,-4-4i)`, `b=(-4-4i,2-i,2-4i,4-i)`, and `eta=1`.

The lead gives `M=256`, `m=-217/2`, and the stronger left cubature ceiling `Lambda_left=1057/3`, so `Lambda_left-M=289/3`.

The exact verifier in this run computes the top-to-second coset-roof gaps. On the left orientation they are

`(29/2, 45/2, 160/3, 95/2, 44, 54, 64/3)`,

and on the right orientation they are

`(96, 42, 10, 3/2, 78, 132, 200)`.

Every gap is strictly positive. Hence all seven roofs are uniquely exposed on **both** physical sides. The new rigidity theorem sharpens the lead's endpoint-only statement on this datum from `h(U)-M <= 289/3` to

`every genuine support violator satisfies 0 < h(U)-M < 289/3`.

This strictness does not by itself close the datum: there may still be an interior maximizer below the cubature roof. It does prove that the lead's residual ceiling has no source-valid violating equality case on the canonical hard instance.

## 7. Direct application of the assigned partner result

Account01/B09's exact complex-Hadamard family is

`U(z) = (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]`, with `|z|=1`.

It has `|U(z)|^2=J/4` for every phase but a genuinely phase-dependent exterior-square channel and determinant. The partner proves an exact positive endpoint lift for the whole family and simultaneously refutes any universal full lift determined only by `(P,a,b)`.

That result is used here at the one place where a P-only argument would fail: H2,H6 are transitive on points, so their singleton marginals cannot expose a block. The proof above instead uses the `2+4` orbit split of the **two-subset / exterior-square** channel. Thus the rigidity mechanism is compatible with the partner's obstruction rather than contradicting it.

Moreover, every entry of this Hadamard family is nonzero, so it is not permutation-equivalent to any proper coordinate block. It follows from the new theorem that whenever one of the seven subgroup roofs is uniquely exposed, a Hadamard-fiber unitary cannot saturate that roof. On the hard datum, where all fourteen left/right roof gaps are positive, the partner's dense Hadamard calibration family is strictly interior to every subgroup roof, consistent with its explicit positive lift.

## 8. First remaining implication

The smallest remaining generic implication is now:

**`MOC4-STRICT-INTERIOR-SUBGROUP-STATIONARITY-v1` (OPEN).** For every structured spectral/support datum whose endpoint-only residual is positive and for which at least one relevant subgroup roof is uniquely exposed, exclude a genuine common-unitary **global** support maximizer with `h(U)>M` that lies strictly below the active seven-subgroup cubature ceiling, using the exact same-unitary `P-R-D` compatibility, pair-Rayleigh stationarity and the current Cartan/Hessian constraints.

The fully tied endpoint-face locus is a separate exact degeneracy: a cubature-boundary violator would require seven simultaneous coset-roof ties on one physical side. Repeated spectra and singular determinant points are not discarded; the theorem itself is algebraic/continuous and the block-safe conclusion handles them directly.

## 9. Exact verification and scope of the certificate

`verify_cubature_roof_rigidity.py` uses only `itertools` and `fractions`. It verifies exactly:

- the point-orbit block sizes `(2,2),(4),(1,3),(2,2),(1,1,2),(4),(1,3)` for H1,...,H7;
- for every left and right coset of every nontransitive subgroup, the singleton marginal has exactly the claimed block-support pattern;
- for every left and right coset of H2,H6, the two-subset marginal has exactly two support components of sizes 2 and 4;
- the hard endpoint roof values and the exact positive top-to-second gaps above.

Observed output:

```text
PASS MOC4-CUBATURE-ROOF-RIGIDITY-v1
singleton_orbit_sizes = [[2, 2], [4], [1, 3], [2, 2], [1, 1, 2], [4], [1, 3]]
H2_pair_orbit_sizes = [2, 4]
H6_pair_orbit_sizes = [2, 4]
hard_left_roof_gaps = ['29/2', '45/2', '160/3', '95/2', '44', '54', '64/3']
hard_right_roof_gaps = ['96', '42', '10', '3/2', '78', '132', '200']
```

The finite script checks the combinatorial orbit/coset facts and exact arithmetic; it does not substitute for the decomposability argument for H2,H6, which is given explicitly above.

## 10. Failure controls, privacy and non-claims

Full MOC4 remains open. This run does not claim that a nonmonomial stationary point is a counterexample, does not infer a universal individual-unitary lift, and does not revive a P-only representation refuted by the assigned partner. The strict hard-datum bound is not numerical closure; its role is to remove the equality/boundary branch from the genuine-unitary residual.

A scoped privacy/source review of the new artifacts found only mathematical formulas, repository-relative source identifiers, public commit/blob identifiers and nonsecret logical run labels. No benchmark gold, held-out answer, credential, scheduler identifier, machine path, unrelated private transcript, email/Drive material, paid model/API/Codex call, remote workflow, permission bypass, notification mutation, or public-release action was used.
