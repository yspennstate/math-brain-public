SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B16, 2026-09-22T19:04:33Z.
attacking: aggregate singular-pair determinant mass before reciprocal local-minor payment.

# Control-15 addendum: diffuse star bank paid before local-minor inversion

Run: `20260922T190433Z-fleet01-B16-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING FAMILY CLOSED / FULL QFORM OPEN**. Continuity remains separate.

This addendum applies the run's proved theorem `QFORM-RANK1-PAIR-AGGREGATE-SMOOTHER-v1` and the completed designated-partner theorem `QFORM-INDEFINITE-BINARY-FROSTMAN-v1` to the same exact target family. The comparison isolates the benefit of aggregating an original-coordinate bank before paying a reciprocal principal-minor cost.

## 1. An exact three-large-eigenvalue diffuse-star family

For `m>=1`, use physical coordinates `(X_0,X_h,X_1,...,X_m)` and put

`b_m=(1,...,1)/sqrt(m)`.

Let

`A_m = [1] direct_sum S_m`,

where, in the `(h,1,...,m)` coordinates,

`S_m = [[0,b_m^T],[b_m,0_m]]`.

Because `||b_m||_2=1`, the star matrix `S_m` has eigenvalues `+1,-1,0,...,0`. Hence

`spec(A_m)={1,1,-1,0,...,0}`,

so every `A_m` belongs to the exact target class.

The quadratic form is

`Q_m=X_0^2+2 X_h L_m`,

with

`L_m=m^(-1/2) sum_(j=1)^m X_j`.

All physical inputs remain arbitrary independent probability laws with densities at most one.

## 2. The new B16 aggregate payment is uniform in m

Choose the original-coordinate pair `I={0,h}`. Its physical block is

`P=A_m[I,I]=diag(1,0)`,

so `P` has rank one with nonzero eigenvalue `lambda=1`; its null direction is the hub coordinate. The cross block from that null direction to the leaves is exactly `b_m`, and therefore

`eta=||b_m||_2=1`.

The proved B16 theorem gives directly

`||p_(Q_m)||_infinity <= 18*2^(1/3)=22.6785788981077...`,

uniformly in `m` and uniformly over all admissible independent input laws.

Equivalently, the aggregate determinant mass from the run's identity is

`M_I=sum_(j=1)^m |det A_m[{0,h,j}]|`.

Each triple has matrix

`[[1,0,0],[0,0,m^(-1/2)],[0,m^(-1/2),0]]`

and determinant `-1/m`. Thus

`M_I=m*(1/m)=1`,

and the theorem is precisely the payment `18*2^(1/3) M_I^(-1/3)` made after summing all `m` tiny triple determinants.

## 3. Direct application of the completed fleet02/B16 partner theorem

The completed designated-partner theorem `QFORM-INDEFINITE-BINARY-FROSTMAN-v1` gives a local physical-triple bound of the form

`||p_Q||_infinity <= C_ind |det A[J,J]|^(-1/4)`

in the present scalar-pivot normalization, with

`C_ind=8*3^(3/4)*5^(1/4)/sqrt(e)=16.5396451661233...`.

Applied separately to any one triple `{0,h,j}`, this yields only

`||p_(Q_m)||_infinity <= C_ind m^(1/4)`,

which diverges with `m`. Thus no selection of a single one of these principal triples gives a dimension-free partner bound.

The same partner theorem becomes uniform once the diffuse leaf bank is compressed *before* the reciprocal payment. The normalized linear form `L_m` has density cap at most `sqrt(2)` by the bounded-density linear projection theorem, and it is independent of `X_h`. Put `Z=sqrt(2)L_m`; then `Z` has density cap at most one and

`2X_h L_m = sqrt(2) X_h Z`.

The corresponding binary quadratic matrix has determinant magnitude `1/2`. Therefore the partner half-Riesz theorem, followed by the independent square `X_0^2`, gives

`||p_(Q_m)||_infinity <= C_ind*2^(1/4)=19.6690637111741...`,

again uniformly in `m`.

This is an actual application of the completed partner result, not merely a citation. It independently confirms the structural lesson of the new B16 theorem: in diffuse families, an entire original-coordinate bank must be aggregated into a bounded-density innovation before a reciprocal determinant/minor cost is paid.

## 4. What this changes and what remains

The family `A_m` is a concrete exact-target witness against any proof architecture that first selects one physical triple and then pays an inverse power of its determinant: every available `{0,h,j}` determinant is `1/m`, although the full form is uniformly controlled. The run's determinant-mass identity repairs this family by summing `m` contributions before inversion.

This does **not** prove the universal conjecture. The remaining B16 implication is still `QFORM-SINGULAR-O2-AGGREGATE-BEFORE-RECIPROCAL-v1`: from the fleet's aggregate singular O2 packet mass, derive either one dimension-free aggregate smoother without selecting a largest packet, or prove that sufficiently dispersed packet mass forces an already-paid ridge/diffuse/grouped branch. The analogous overlapping-innovation endpoint for invertible physical pairs is also unpaid.

Corrections respected: no arbitrary-joint rank-three coarea bound, no normalized scalar-`Q_rest` conditional supremum, no post-rotation independence, no near-zero half-Riesz continuity from an exact-zero Schur row, and no pointwise law-uniform oscillatory decay are used.