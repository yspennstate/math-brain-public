# Strengthening — spend the source Frobenius tail collectively, not blockwise

Status: **PROVED STRENGTHENING** of the physical localization constants in `FINITE_COLLAR_BRIDGE.md`; full QFORM remains OPEN.

The preceding localization used the valid but crude estimate `sqrt(12)*epsilon` for the six strong-arm contribution. The source actually gives the collective Frobenius budget

`||E_1||_F^2+||E_2||_F^2 < epsilon^2`,
`epsilon=0.0023595307563857772`.

This budget can be spent before block localization.

For fixed `r in {1,2}`, the three physical `Q_(K_b)` are pairwise orthogonal domain projections and the three canonical `P_(K_b)` are pairwise orthogonal domain projections. The source identities used in the previous run give

`P_(D_r) A Q_(K_b)=P_(D_r)E_r Q_(K_b)`,
`Q_(D_r) A P_(K_b)=Q_(D_r)E_r P_(K_b)`,
`Q_(D_r) A Q_(K_b)=Q_(D_r)E_r Q_(K_b)`.

Therefore

`sum_b ||P_(D_r) A Q_(K_b)||_op^2
 <= sum_b ||P_(D_r)E_r Q_(K_b)||_F^2
 <= ||E_r||_F^2`,

and similarly

`sum_b ||Q_(D_r) A P_(K_b)||_op^2 <= ||E_r||_F^2`,
`sum_b ||Q_(D_r) A Q_(K_b)||_op^2 <= ||E_r||_F^2`.

By symmetry the reverse-oriented blocks have the same operator norms. Hence the total sum of squared operator norms over **all twelve oriented strong-arm blocks** is at most

`2(||E_1||_F^2+||E_2||_F^2) < 2 epsilon^2`

both in the `PAQ` localization and in the `QAQ` localization. The block-Frobenius comparison then gives the sharper collective arm bound

`boxed: ||T_arm||_op < sqrt(2) epsilon
       =0.00333688039651721... .`

Consequently the robust `3/8` escape from `QFORM-R37-FINITE-COLLAR-ABSOLUTE-BRIDGE-v1` localizes to

`delta_PQ^(rob,sharp)
 =(3/8-sqrt(2)epsilon)/sqrt(18)
 =0.0876018373961899...`,

and

`delta_QQ^(rob,sharp)
 =(3/8-sqrt(2)epsilon)/sqrt(24)
 =0.0758654166032941... .`

Thus in the moderate-scale nondegenerate finite collar, after the E3 Schur-defect payment, at least one of the following is forced:

1. a same-node common-Gram self defect `>3/8`;
2. a NON-ARM physical plane/complement interaction `>0.08760`;
3. a NON-ARM physical complement/complement interaction `>0.07586`.

No tail is dropped from the random polynomial; the improvement comes from using the complete source Frobenius budget before choosing a physical block.
