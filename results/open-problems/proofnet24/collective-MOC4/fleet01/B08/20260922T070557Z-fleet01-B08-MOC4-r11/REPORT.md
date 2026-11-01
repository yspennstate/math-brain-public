# MOC4 — canonical same-unitary P/R common-compound lift

Run: `20260922T070557Z-fleet01-B08-MOC4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**.  
Parent target: **OPEN / not proved / not disproved**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Source / dependency binding

Target is the n=4 Marcus–de Oliveira statement from the active collective package: for arbitrary complex normal 4-by-4 A,B, prove `det(A+B)` belongs to the convex hull of the 24 permutation products. Singular and repeated spectra are included.

Latest complete campaign-lead result consumed: fleet03/B07 run `20260922T064004Z-fleet03-B07-MOC4-r12`, `MOC4-KERNEL-QUARTIC-RESERVE-v1` / `MOC4-MIXED-SCHUR-LS-GATE-v1`. It reduces a hypothetical positive-gap maximizer to the mixed-Schur or all-negative-definite branches and supplies the quartic least-squares reserve on a mixed-Schur kernel.

Named assigned OTHER-account result consumed and applied: fleet02/B09 run `20260922T064517Z-fleet02-B09-MOC4-r17`, `MOC4-TRANSPOSE-TIE-SAFE-v1`. It proves a positive-gap maximizer has no row/column transposition tie; all physical pair gaps are strict.

This run also preserves fleet01/B08's earlier exact no-go: an unconditional positive common-compound law is false for true unitaries already at the joint `(P,R)` projection. The result below therefore constructs an **exact canonical signed section for every true unitary**, identifies its precise positivity gate, and proves a substantially larger spectra-independent region where that section is positive.

## 1. True-unitary channels P and R

Fix `U in U(4)`. Put

`P_ij = |u_ij|^2`.

Let the three complementary-pair partitions of `{1,2,3,4}` be

`C0={12,34}`, `C1={13,24}`, `C2={14,23}`.

For `alpha={S,S^c}` and `beta={T,T^c}`, where `|S|=|T|=2`, define

`R_{alpha,beta} = |det U[S,T]|^2 + |det U[S,T^c]|^2`.

Jacobi complementary-minor equality makes this independent of the choices of the member `S` of `alpha` and member `T` of `beta`. Cauchy–Binet gives every row and column sum equal to one, so `R` is a genuine nonnegative `3 x 3` doubly stochastic matrix.

Let

`rho:S4 -> S3`

be the quotient action of `S4` on the three complementary-pair partitions; its kernel is `V4`.

Choose **any** Birkhoff decomposition

`R = sum_{r in S3} mu_r P_r`, `mu_r>=0`, `sum_r mu_r=1`.

## 2. Exact reconstruction of every individual 2-minor from (P,R)

This is the first key point. For any two-subsets `S,T`, set

`N_ST = sum_{i in S, j in T} P_ij`.

Let `G=U[S,T]U[S,T]^*`. Because the two selected rows of `U` are orthonormal,

`U[S,T^c]U[S,T^c]^* = I_2-G`.

Therefore

`|det U[S,T]|^2 = det G`,

`|det U[S,T^c]|^2 = det(I_2-G) = 1-tr(G)+det(G)`.

Since `tr(G)=N_ST`, adding the two expressions through the definition of `R` gives

**(2.1)**

`|det U[S,T]|^2 = (N_ST - 1 + R_{alpha,beta})/2`.

Thus `(P,R)` does not merely contain determinant-relevant aggregated information: in dimension four it determines **every individual degree-two squared compound minor**.

There is an equivalent permutation-law identity. For any (possibly signed) mass `w` on `S4` with total mass one, define its one-point channel `P^w` and quotient channel `R^w`. Pointwise, the number of images of `S` landing in `T` is 2 when `sigma(S)=T`, 0 when `sigma(S)=T^c`, and 1 otherwise; the quotient event says exactly that `sigma(S)` is either `T` or `T^c`. Hence

`sum_{sigma:sigma(S)=T} w_sigma = (sum_{i in S,j in T}P^w_ij -1 + R^w_{alpha,beta})/2`.

So **any** mass matching `P` and `R` automatically matches every individual two-subset event.

## 3. Canonical affine section on the 24 permutations

For each `sigma in S4` define

**(3.1)**

`nu_sigma = (1/8) sum_i P_{i,sigma(i)} + (1/4) mu_{rho(sigma)} - 1/8`.

### Theorem 3.1 — `MOC4-CANONICAL-PR-COMMON-LIFT-v1`

For every true unitary `U` and every Birkhoff coefficient vector `mu` of its true quotient channel `R`, the 24 real numbers (3.1) satisfy:

1. `sum_sigma nu_sigma=1`;
2. `sum_{sigma:sigma(i)=j} nu_sigma=P_ij` for every `i,j`;
3. `sum_{sigma:rho(sigma)(alpha)=beta} nu_sigma=R_{alpha,beta}` for every `alpha,beta`;
4. for **every** equal-cardinality `I,J subset {1,2,3,4}` and every `k=|I|=|J|` from 0 through 4,

   `sum_{sigma:sigma(I)=J} nu_sigma = |det U[I,J]|^2`.

Consequently, for arbitrary complex spectra `a,b`, with no simplicity or nonsingularity assumption,

**(3.2)**

`det(D_a + U D_b U*) = sum_{sigma in S4} nu_sigma prod_i(a_i+b_{sigma(i)})`.

If all `nu_sigma>=0`, (3.2) is the desired convex representation in the 24 permutation products, using one and the same probability law for **all** compound minors.

### Proof

For normalization, write `A_sigma=sum_i P_{i,sigma(i)}`. Since each matrix entry `P_ij` occurs in six permutations,

`sum_sigma A_sigma=6 sum_ij P_ij=24`.

Each quotient permutation `r` has four lifts to `S4`, so

`sum_sigma mu_{rho(sigma)}=4`.

Thus (3.1) sums to `24/8+4/4-24/8=1`.

Fix `i,j`. Among the six permutations with `sigma(i)=j`, for each `k!=i` every column `l!=j` occurs twice. Hence

`sum_{sigma:sigma(i)=j} A_sigma = 6P_ij + 2 sum_{k!=i,l!=j}P_kl = 8P_ij+4`,

using the doubly stochastic row/column sums of `P`. In each `V4` coset exactly one permutation sends `i` to `j`, so the `mu` term contributes `(1/4)sum_r mu_r=1/4`, while the constant contributes `-6/8=-3/4`. This proves item 2.

Fix `alpha,beta`. There are exactly two quotient permutations `r in S3` with `r(alpha)=beta`, hence eight lifts in `S4`. Within those eight lifts each ordered pair `(i,j)` occurs exactly twice. Therefore

`sum_{sigma:rho(sigma)(alpha)=beta} A_sigma = 2 sum_ij P_ij=8`.

The first and constant terms of (3.1) cancel (`8/8-8/8=0`), and the `mu` term equals

`sum_{r:r(alpha)=beta} mu_r = R_{alpha,beta}`.

This proves item 3.

Item 4 for `k=2` follows immediately from item 2, item 3 and identity (2.1). For `k=1` it is item 2. For `k=3`, the event `sigma(I)=J` is equivalent to the one-point event `sigma(I^c)=J^c`, while Jacobi's unitary complementary-minor identity gives

`|det U[I,J]|^2=|det U[I^c,J^c]|^2`.

The cases `k=0,4` are normalization.

Finally the mixed diagonal/unitary Cauchy–Binet expansion is

`det(D_a+UD_bU*) = sum_{S,T:|S|=|T|} a_{S^c} b_T |det U[S,T]|^2`.

Insert item 4 and interchange the finite sums:

`= sum_sigma nu_sigma sum_S a_{S^c} b_{sigma(S)}`

`= sum_sigma nu_sigma prod_i(a_i+b_{sigma(i)})`.

This proves (3.2). If `nu>=0`, normalization makes it a convex combination. QED.

## 4. A stronger spectra-independent safe region

Let

`p=min_ij P_ij`, `q=min_{alpha,beta} R_{alpha,beta}`.

Because `R` is `3 x 3` doubly stochastic,

`R = 3q (J_3/3) + (1-3q)R'`

for another doubly stochastic `R'` (with the trivial interpretation at `q=1/3`). Decompose `J_3/3` uniformly over the six permutation matrices and decompose `R'` arbitrarily. This gives a Birkhoff vector with

`mu_r >= q/2` for every `r in S3`.

Also `sum_i P_{i,sigma(i)}>=4p`. Therefore the canonical coefficients obey

`nu_sigma >= 4p/8 + (q/2)/4 -1/8 = (4p+q-1)/8`.

Hence:

### Corollary 4.1 — `MOC4-4PPLUSQ-CERTIFICATE-v1`

**(4.1)**

`4 min_ij |u_ij|^2 + min_{alpha,beta} R_{alpha,beta} >= 1`

implies a nonnegative common-compound law `nu` and therefore proves MOC4 for this relative unitary `U` for **every pair of complex spectra**, including repeated and singular spectra.

This strictly strengthens the previous B08 easy certificate `8p+q>=2`. The exact Hadamard point has `p=1/4` and therefore satisfies (4.1) at equality even when `q=0`.

Consequently any actual MOC4 counterexample must satisfy the new unitary-only necessary condition

**(4.2)**

`4 min_ij |u_ij|^2 + min_{alpha,beta} R_{alpha,beta} < 1`.

This does not contradict the earlier true-unitary joint-lift counterexample: there the canonical coefficients necessarily become negative. The theorem gives an affine common lift universally and a positive one only under an explicit feasibility condition.

## 5. Exact finite positivity gate beyond 4p+q>=1

The sufficient bound (4.1) is deliberately coarse. For a fixed true unitary define

`A_sigma=sum_i P_{i,sigma(i)}`

and for each quotient fiber `r` define

**(5.1)**

`t_r = (1/2) max(0, 1 - min_{sigma:rho(sigma)=r} A_sigma)`.

By (3.1), the canonical section is nonnegative exactly when one can choose a Birkhoff decomposition of `R` satisfying

**(5.2)** `mu_r >= t_r` for all six `r`.

For `3 x 3` doubly stochastic `R`, its six Birkhoff coefficients have one affine degree of freedom, so (5.2) is an exact finite interval-feasibility test. This is a useful maximizer-local replacement for the false universal-positive-lift hope.

## 6. Direct application of assigned partner result

Fleet02/B09's `MOC4-TRANSPOSE-TIE-SAFE-v1` says a hypothetical positive support gap `gamma=h(U*)-M>0` forces strict row and column transposition gaps; no physical pair orbit can tie its transposed endpoint.

Combining that result with Theorem 3.1 yields the following sharpened residual statement:

### `MOC4-MAXIMIZER-CANONICAL-FEASIBILITY-v2`

A positive-gap global maximizer `U*`, if one exists, must simultaneously satisfy:

- all fleet02/B09 strict row/column transposition-gap inequalities;
- the campaign lead's surviving `MSQR` or `NDI` local-maximizer conditions;
- the strict interior obstruction (4.2); and
- **failure** of the exact six lower-bound feasibility system (5.2) for its genuine same-unitary `(P,R)`.

Indeed, if (5.2) were feasible, Theorem 3.1 would give a nonnegative common-compound law and immediately force `h(U*)<=M`, contradicting the positive gap.

This applies the partner's theorem rather than replacing it: the remaining branch is now the intersection of continuous strict-maximizer geometry with a concrete finite same-unitary transportation obstruction.

The first unpaid implication is to prove that this intersection is empty (using the lead's mixed-Schur/NDI constraints and the pair-roof inequalities), or construct actual spectra, support direction and a true unitary in it whose determinant support exceeds all 24 endpoints. A negative canonical coefficient by itself is not a target counterexample.

## 7. Exact verification

Adjacent `verify_pr_common_lift.py` uses only the Python standard library and exact rational arithmetic. It checks:

- the group-combinatorial coset counts used in Theorem 3.1;
- a dense exact rational `SO(4)` unitary with every entry and every `2 x 2` minor nonzero;
- exact doubly stochastic `P,R` and an exact Birkhoff decomposition `mu`;
- normalization and exact reproduction of `P` and `R` by (3.1);
- **all** compound events for `k=0,1,2,3,4` against exact squared minors;
- the pointwise reconstruction formula (2.1);
- the nonnegative `4p+q>=1` certificate at an exact Hadamard point.

Captured output:

`PASS MOC4-CANONICAL-PR-COMMON-LIFT-v1`

The dense test intentionally has a negative canonical coefficient, confirming that this theorem is not silently reviving the already-refuted universal-positive-lift claim.

## Claim limits

- This is not a proof or disproof of full MOC4.
- The universal positive common-compound representation remains false.
- The new result is an exact universal affine section plus an exact positivity gate and a stronger spectra-independent positive region.
- No arbitrary independent bistochastic arrays are substituted: both `P` and `R` come from the same true unitary.
- No simplicity, nonsingularity or genericity is used in Theorem 3.1 or Corollary 4.1.
