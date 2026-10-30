# r26 addendum — genuine new contribution after duplicate-scope detection

During the mandatory final memory refresh I found that the immediately preceding fleet03/B18 run `20260923T092851Z-fleet03-B18-QFORM-r26` had already proved the base rank-two cross-block half-Riesz theorem with the same sharp constant `8` at rank two, and its one-pivot Schur consequence. Those statements in this run's `REPORT.md` are therefore **independent rederivations, not new fleet results**. They are preserved immutably rather than hidden or rewritten.

The genuinely new result of the present run is the partner-compiled iteration below, which goes beyond the preceding handoff.

## Theorem — `QFORM-NESTED-PIVOT-RANK2-CROSS-COMPILER-v1`

Let `Y` consist of disjoint original-coordinate blocks `I,J` and suppose

`R(Y)=F(X_I)+G(X_J)+2 X_I^T B X_J`,

where `F,G` are arbitrary real measurable functions and `B` has rank two with nonzero singular-value product

`Delta=sigma_1 sigma_2>0`.

Let `Z_1,...,Z_m` be further distinct original coordinates, disjoint from `I union J`, hence mutually independent and independent of `Y`, each with density cap one. Suppose successive scalar Schur completion writes the quadratic form recursively as

`T_0=R(Y)`,

`T_j=a_j (Z_j+h_j(Z_1,...,Z_{j-1},Y))^2 + T_{j-1}`,

for `j=1,...,m`, where every `a_j!=0` and every `h_j` is the affine/linear shift produced by the corresponding Schur completion. Equivalently, one may start with the outermost physical pivot `Z_m`, take its Schur complement, then pivot `Z_{m-1}`, and continue until the terminal Schur residual has the stated rank-two physical cross cut.

Then `T_m` is absolutely continuous and

`boxed(
 ||p_{T_m}||_infinity
 <= 2^(2+2^(1-m))
    Delta^(-1/2^(m+1))
    prod_{j=1}^m |a_j|^(-1/2^(m-j+1)).
)`  (A.1)

Continuity is not asserted.

### Proof

The already completed rank-two cross half-Riesz endpoint gives the first-pivot density cap

`M_1 <= 8 |a_1|^(-1/2) Delta^(-1/4).`  (A.2)

For every `j>=2`, condition on `T_{j-1}=t`. Since `Z_j` is an original coordinate independent of all inner variables, the conditional law of

`V_j=Z_j+h_j(Z_1,...,Z_{j-1},Y)`

is a mixture of translations of the original density of `Z_j`; consequently its conditional density cap is at most one. The completed fleet04/B18 result

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

therefore applies literally at every outer layer and gives the recurrence

`M_j <= 2 |a_j|^(-1/2) M_{j-1}^(1/2).`  (A.3)

Write the power of two in `M_j` as `2^(e_j)`. From (A.2), `e_1=3`, and (A.3) gives

`e_j=1+e_{j-1}/2`.

Hence

`e_m=2+2^(1-m).`  (A.4)

The exponent of `Delta` starts at `-1/4` and is halved at each of the remaining `m-1` smoothing steps, giving

`-1/[4*2^(m-1)]=-1/2^(m+1).`  (A.5)

The exponent of pivot `a_j` is `-1/2` when that pivot is introduced and is halved once for each later outer pivot. It is therefore

`-1/2^(m-j+1).`  (A.6)

Combining (A.4)--(A.6) proves (A.1). Absolute continuity follows inductively from the partner theorem. QED.

## First cases

For one pivot (`m=1`), (A.1) is the already known endpoint

`||p||_infinity <=8 |a_1|^(-1/2) Delta^(-1/4).`

For two pivots,

`boxed(
 ||p||_infinity
 <=4 sqrt(2) |a_2|^(-1/2)|a_1|^(-1/4)Delta^(-1/8).
)`  (A.7)

For three pivots,

`||p||_infinity
 <=4*2^(1/4)
 |a_3|^(-1/2)|a_2|^(-1/4)|a_1|^(-1/8)Delta^(-1/16).`  (A.8)

If all successive pivot magnitudes and `Delta` are at least one, the dimension-free constant is at most `8` for every `m` and decreases monotonically toward `4` as more outer square-smoothing layers are available. No claim is made that the bare three-large-eigenvalue hypothesis forces these quantitative Schur parameters.

## Exact three-large-eigenvalue partner application

For independent cap-one variables `(W,Z,X1,Y1,X2,Y2)`, take

`Q=(W+Z)^2 +(1/4)Z^2 +2X1Y1 +(1/2)X2Y2.`

The exact spectrum is

`{(9+sqrt(65))/8, (9-sqrt(65))/8, 1, -1, 1/4, -1/4}`,

so exactly three eigenvalues have modulus at least one.

The outer pivot is `a_2=1`; after its Schur completion the inner pivot is `a_1=1/4`; after the second completion the terminal cross block is `diag(1,1/4)`, so `Delta=1/4`. Formula (A.7) gives

`||p_Q||_infinity
 <=4sqrt(2)(1/4)^(-1/4)(1/4)^(-1/8)
 =8*2^(1/4)
 =9.513656920021768... .`

The outer square is `(W+Z)^2`, so this is not merely an independent convolution: the dependence-safe fleet04/B18 interface is used at its actual hypothesis. The direct one-pivot rank-two-cross estimate at the outer level would give `8sqrt(2)=11.3137...`, so the nested partner compiler strictly improves the quantitative certificate here.

## Scope boundary

This theorem is an analytic compiler, not the missing structural theorem. The live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` remains binding: `s_3(A)>=1` does not force even one nonzero physical pivot whose Schur complement has a rank-two cross cut, much less a full nested chain with quantitative pivots. The unresolved full-target step is still an exhaustive product-preserving routing of the rank-one-star/no-good-cross-cut states into grouped, hub, ridge, or zero-pivot mechanisms.

**Full QFORM remains OPEN / NOT PROVED.**
