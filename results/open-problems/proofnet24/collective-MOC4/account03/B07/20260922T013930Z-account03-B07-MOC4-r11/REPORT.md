# MOC4 account03/B07 — exact zero-entry common-lift no-go

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account03/B07, campaign lead  
**Outcome:** `CANDIDATE_REFUTED` for a proposed zero-entry common-permutation-lift mechanism; **MOC4 remains OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and current chain

For all complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

`det(A+B) in conv{ product_i (a_i+b_sigma(i)) : sigma in S_4 }`.

This run starts from two exact completed inputs.

1. **account03/B07 r12, `MOC4-PARITY-SLACK-v1` reduction.** The exact mixed `(P,R)` support inequality was compressed through the three-dimensional standard representation of `S_4` to six `S_3` fibers. The unrestricted common `(P,R)` permutation lift is already known false; the exact fallback is the six-fiber signed support inequality.
2. **Assigned partner account04/B08, `MOC4-PAIR-FLAT-BOUNDARY-v1`, report blob `3c71dc6a046f699b3248957d660b2c02fe968efb`.** At a global support maximizer, a tied row/column pair orbit is completely flat, and a flat pair can be rotated to an equal-support unitary with a zero entry. Hence a support-violating maximizer either lies on a zero-entry boundary representative or is strict on all twelve row/column pair spheres.

The natural question was whether the partner's zero-entry branch restores the permutation-lift mechanism that fails in the unrestricted interior. This report answers **no**, by an exact rational orthogonal witness.

## 2. The proposed zero-entry lift and a necessary cut

For a real orthogonal `U`, define for two-subsets `I,J subset {0,1,2,3}`

`R_{I,J} = det(U[I,J])^2`.

A strong candidate mechanism would assert that, whenever `U` has a zero entry, there is a probability law `lambda` on `S_4` such that

`R_{I,J} = Pr_{sigma~lambda}[ sigma(I)=J ]`

simultaneously for every pair of two-subsets. Such a law would synchronize the second-compound marginals with actual permutation vertices and would be much stronger than the exact support statement needed for MOC4.

Every such law must satisfy

`R_{02,23} <= R_{01,02} + R_{01,03} + R_{01,13} + R_{03,02}`.  (CUT)

This follows pointwise for each individual permutation. If `sigma({0,2})={2,3}`, then either:

- `sigma(0)=2, sigma(2)=3`. The remaining images of rows 1 and 3 are `{0,1}`. If `sigma(1)=0`, event `(01 -> 02)` occurs; otherwise `sigma(3)=0`, event `(03 -> 02)` occurs.
- `sigma(0)=3, sigma(2)=2`. If `sigma(1)=0`, event `(01 -> 03)` occurs; otherwise `sigma(1)=1`, event `(01 -> 13)` occurs.

Thus the indicator of the left event is at most the sum of the four right indicators for every `sigma`; averaging proves `(CUT)`.

## 3. Exact rational zero-entry orthogonal witness

Consider

```
U = [
 [       0,       3/5,     16/25,    -12/25],
 [ -69/325,  -192/325,     48/65,      16/65],
 [    48/65,     16/65,    69/325,    192/325],
 [    16/25,    -12/25,         0,       -3/5],
].
```

Exact rational arithmetic gives `U U^T = I`; in particular this is a genuine orthogonal, hence unitary, matrix and it has zero entries.

Its relevant squared two-minors are

`R_{02,23} = 144/625`,

`R_{01,02} = 1218816/66015625`,

`R_{01,03} = 685584/66015625`,

`R_{01,13} = 1218816/66015625`,

`R_{03,02} = 65536/390625`.

Therefore

`R_{02,23} - (R_{01,02}+R_{01,03}+R_{01,13}+R_{03,02})`

`= 40448/2640625 > 0`.

This contradicts `(CUT)`. Hence **no probability law on `S_4` can realize all the two-subset squared-minor marginals of this zero-entry true unitary**.

The accompanying standard-library verifier checks exact orthogonality, the pointwise cut over all 24 permutations, every displayed rational minor value, and the positive rational gap using `fractions.Fraction` only.

## 4. A useful positive identity that survives

The failure is not because the zero-entry face has no additional structure. If `u_00=0`, then for `i,j in {1,2,3}`,

`|det U[{0,i},{0,j}]|^2 = |u_0j|^2 |u_i0|^2`.  (ZF)

Indeed the relevant determinant is `-u_0j u_i0`. Thus the 3-by-3 corner-to-corner block of second-compound squared minors factorizes as an outer product. The exact verifier checks `(ZF)` for the displayed witness.

What the witness proves is that this rank-one boundary factorization still does **not** extend to a globally consistent `S_4` subset-permutation law.

## 5. Consequence for the shared proof architecture

The partner's pair-flat theorem remains fully useful: a flat pair transfers a hypothetical violation to a zero-entry unitary. But the zero-entry branch cannot then be closed merely by resurrecting the already-refuted common permutation-lift idea.

The smallest surviving conditional chain is now:

1. Reduce a hypothetical failure to the generic support-maximization setup already established by the team.
2. By account04/B08, split into a zero-entry boundary branch and a pair-strict interior branch.
3. On the interior branch, continue the exact six-fiber / parity-slack route from account03/B07 r12 or an equally structured true-unitary argument.
4. On the zero-entry branch, exploit identities such as `(ZF)` **directly inside the exact support functional**; do not demand a common law reproducing all compound marginals.

A concrete next lemma is therefore:

> **`MOC4-ZERO-FACE-SUPPORT-v1`.** For a support-maximizing unitary with one zero entry, prove the exact six-fiber support inequality using the boundary factorization `(ZF)` together with the actual structured spectral coefficients. No common permutation lift is assumed.

If this zero-face lemma is proved, account04/B08's dichotomy leaves only the bi-pair-strict interior branch. If it fails, the failure must be tested at the actual MOC4 support level; the present witness is **not** a target counterexample because it only refutes an auxiliary representation.

## 6. Status and non-claims

- `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`: **REFUTED** by an exact true-unitary zero-entry witness.
- `MOC4-PAIR-FLAT-BOUNDARY-v1`: consumed and not challenged by this result.
- `MOC4-PARITY-SLACK-v1`: remains an open sufficient gate for the structured interior support problem.
- Full MOC4: **OPEN**.
- No numerical tolerance, arbitrary bistochastic surrogate, or non-unitary witness is used in the new refutation.
- No benchmark material, held-out answers, credentials, scheduler identifiers, machine paths, email/Drive data, public posting, paid model/API, Codex, or remote workflow was used.

## 7. Next recipients

Primary recipient: **account04/B08**, because this closes the most obvious false shortcut after its pair-flat reduction. Also useful to account01/B07 and account03/B20 for integration, and to account04/B09/account02/B07 because their structured coefficient and pair-orbit mechanisms must now be applied without a common subset-permutation lift.
