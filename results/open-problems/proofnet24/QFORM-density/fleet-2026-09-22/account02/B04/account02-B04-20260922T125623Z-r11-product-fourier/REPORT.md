# account02/B04 — aggregate-before-invert product rearrangement

Run: `account02-B04-20260922T125623Z-r11-product-fourier`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED_SUBSTEP / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, conditional chain, and first unpaid implication

The target remains: for every dimension, every independent real input family with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove

`P(X^T A X in [t,t+h]) <= C h`

for one universal finite `C`, every real `t` and every `h>0`, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence hypothesis is added.

The most useful current conditional end-to-end route is the product-preserving hard-branch route in account01/B19 (`math-open-problems@072cf685a12893b44d555f14e4e610bcf2154037`, report blob `2530c90971b43a49cf9da35be03919868719abb9`). Its near-coordinate-diagonal basin already gives a target-level bound when `||A-diag(A)||_op<1/2`. In the complementary strongly coupled branch it isolates a product-origin elliptic graph trace as the missing global implication; critically, its hard family shows that one cannot insist on one well-conditioned physical triple or a rank-three disjoint cross block.

My previous B04 run (`math-open-problems@b7168a1b0b52fbf69705170ff9795435efeb849f`, blob `fa94d255369a9ad6475ebc66b2f158066e588a8b`) proposed a more specific next step for exact rank three: exploit the fixed-row wedge budget

`sum_{j<k, j,k!=i} det[u_i,u_j,u_k]^2 = ||u_i||_2^2`

and convert that aggregate determinant mass into an averaged conditional-density estimate.

**The first unpaid implication attacked here is that proposed conversion.** The result is negative for every scheme which first selects/averages physical triples and then pays a determinant-scale inverse bound. A high-leverage wedge-spread target family has total wedge budget one while every nonzero local determinant is of order `m^-2`; every convex average of local `|det|^-1/3` bounds therefore grows like `m^(2/3)`. The same family nevertheless has a uniform global density bound `4 sqrt(2)` after aggregating coordinates *before* applying rearrangement. Thus the correct mechanism is aggregate-before-invert, not inverse-minor averaging.

This is an intermediate-candidate refutation, not a counterexample to QFORM.

## 2. Corrections and source dependencies consumed

Fresh owner controls and the live correction inbox were read immediately before publication. In particular this report does not use:

- law-uniform pointwise quadratic-phase decay (`QFORM-POINTWISE-DECAY-FALSE`);
- generic fiber suprema (`QFORM-FIBER-SUP-DIMENSION-LOSS`);
- independence of rotated spectral coordinates (`QFORM-NO-INDEPENDENCE-AFTER-ROTATION`);
- a fixed cross minor alone (`QFORM-CROSSMINOR-ALONE-FALSE`);
- conditional sum/difference density caps (`QFORM-UV-CONDITIONAL-CAP-FALSE`);
- one scalar Schur pivot forcing a disjoint rank-two cross block (`QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`).

The last correction is especially relevant: account02/B09's event at brain blob `5cefcece479c6a6a94024155dddf3bf4a91f4c5d` source-pins account01/B19's exact spectrum-`{1,1,-1}` aggregation family and warns against local Schur extraction. The construction below is a separate but compatible wedge-spread stress family and is used only to test the B04 averaging mechanism.

### Named partner actually applied

The named partner account03/B04 canonical report is

- repository `yspennstate/math-open-problems`;
- commit `f824ded997ee16c741468bb49860e1ccaf18d8bd`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/a03-b04-20260922T115126Z-qform-r11/REPORT.md`;
- blob `2438594f82b064359483972f59f4d061a6814ce0`.

It proves, for a real `Y` with density cap `M` and nonzero `lambda`,

`|| E exp(i t lambda Y^2) ||_{L^3(dt)} <= 2 (2 pi)^(1/3) M^(2/3) |lambda|^(-1/3)`.

I apply this below to an actual square factor after a high-cardinality aggregation; it yields a uniform Fourier inequality, while the final `L^infinity` density estimate uses product rearrangement rather than an invalid `L^3 -> L^1` leap.

### External density-of-sums input

I also use the sharp one-dimensional min-entropy-power inequality of Bobkov–Chistyakov (2014, *Journal of Mathematical Sciences* 199(2), 100–106, DOI `10.1007/s10958-014-1836-9`). In the notation `M(W)=||p_W||_infinity`, for independent bounded-density variables,

`M(W_1+...+W_r)^(-2) >= (1/2) sum_j M(W_j)^(-2)`.   (2.1)

The sharp `1/2` form is equivalently obtained from Rogozin comparison plus Ball cube slicing; Nayar–Tkocz's 2022 survey states this as its Theorems 47–48. This theorem has exactly the arbitrary-density hypotheses needed here and uses no moments or support assumptions.

## 3. New linear-form density cap: spend product structure before rotation

### Lemma 3.1 — `QFORM-LINEAR-FORM-L2-CAP-v1`

Let `X_1,...,X_r` be independent real variables with densities bounded by one and let `c=(c_1,...,c_r)` be nonzero. Then

`M(sum_j c_j X_j) <= sqrt(2)/||c||_2`.   (3.1)

### Proof

Ignore zero coefficients. Each `c_j X_j` has density cap at most `|c_j|^-1`, hence

`M(c_j X_j)^(-2) >= c_j^2`.

Apply (2.1):

`M(sum_j c_j X_j)^(-2) >= (1/2) sum_j c_j^2 = ||c||_2^2/2`.

Taking inverse square roots proves (3.1). QED.

This is the key aggregate-before-invert resource: a linear form with many coefficients of size `m^-1/2` still has a dimension-free density cap. A max-coordinate bound would lose `sqrt(m)` here.

## 4. General cap-sensitive shifted-square rearrangement

My previous run proved the density-`<=1` case. The exact cap dependence is needed for aggregated block variables.

### Theorem 4.1 — `QFORM-SHIFTED-SQUARE-CAPS-v2`

Let `X,Y,Z` be independent real variables with density caps `M_X,M_Y,M_Z<infinity`. Let `a gamma !=0` and `alpha,beta` be arbitrary. Put

`Q = a (Z-alpha X-beta Y)^2 - gamma X Y`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 4 sqrt(2) M_Z sqrt(M_X M_Y) / sqrt(|a gamma|)`.   (4.1)

No independence is asserted after diagonalizing the associated quadratic matrix.

### Proof

Reflect the output if necessary, so the square coefficient may be treated through `|a|`. Conditional on `X=x,Y=y`, translation preserves the density cap of `Z`, and the pushforward by `z -> a z^2` has a density bounded by

`M_Z |a|^(-1/2) s^(-1/2) 1_{s>0}`.

Therefore for every real `t`,

`p_Q(t) <= M_Z |a|^(-1/2) int f_X(x)f_Y(y) (t+gamma x y)_+^(-1/2) dx dy`.   (4.2)

For fixed `x!=0`, the variable `t+gamma xY` has a density cap at most

`M_Y/(|gamma x|)`.

If a probability density `h` satisfies `0<=h<=M`, the decreasing-rearrangement/bathtub inequality gives

`int_0^infinity s^(-1/2) h(s) ds <= 2 sqrt(M)`,   (4.3)

because the maximizer fills `(0,1/M)` at height `M`. Thus the inner `y` integral in (4.2) is at most

`2 sqrt(M_Y/(|gamma x|))`.

A second bathtub bound on the real line gives

`int f_X(x)|x|^(-1/2) dx <= 2 sqrt(2 M_X)`,   (4.4)

since the maximizing density fills `[-1/(2M_X),1/(2M_X)]` at height `M_X`.

Multiplying (4.2)–(4.4) yields (4.1). The null point `x=0` causes no issue because `X` has a density. QED.

### Disjoint-block corollary

Let `L_X=<u,X_{S_X}>`, `L_Y=<v,X_{S_Y}>`, `L_Z=<w,X_{S_Z}>` use pairwise disjoint original-coordinate sets. By Lemma 3.1 the three linear forms are independent and

`M(L_X)<=sqrt(2)/||u||_2`, etc.

Hence

`||p_{a(L_Z-alpha L_X-beta L_Y)^2-gamma L_X L_Y}||_infinity`
` <= 8 sqrt(2) / [ sqrt(|a gamma|) ||w||_2 sqrt(||u||_2 ||v||_2) ]`.   (4.5)

The bound depends on block `l2` mass, not the largest coefficient. Thus it remains dimension-free for diffuse normalized block sums.

## 5. High-leverage wedge-spread family refutes inverse-minor averaging

Fix `m>=1`. Use coordinates

`x_0, y_1,...,y_m, z_1,...,z_m`

and define normalized block sums

`Y_m=m^(-1/2) sum_j y_j`, `Z_m=m^(-1/2) sum_k z_k`.

Consider

`Q_m = x_0^2 + 2 Y_m Z_m`.   (5.1)

Its physical matrix is

`A_m = [1] direct_sum [[0, J_m/m],[J_m/m,0]]`,

where `J_m` is the all-ones `m x m` matrix. The nonzero eigenvalues are exactly

`1,1,-1`; all others are zero. Therefore `A_m` satisfies the exact target spectral hypothesis for every `m`.

An orthonormal eigenframe may be taken with columns

`u_1=e_0`,
`u_2=(1_Y+1_Z)/sqrt(2m)`,
`u_3=(1_Y-1_Z)/sqrt(2m)`.

The distinguished physical row `0` has leverage `||u_0||^2=1`. For a triple containing row `0`, one `Y` row and one `Z` row,

`|det U_I|=1/m`, hence `det(U_I)^2=1/m^2`.

There are exactly `m^2` such nonzero minors, so

`sum_{I contains 0} det(U_I)^2 = m^2 * m^(-2) = 1`,

which is precisely the fixed-row wedge budget. Yet

`det A_m[I,I] = det(diag(1,1,-1)) det(U_I)^2 = -1/m^2`.   (5.2)

All other triples containing row `0` are singular.

Consequently every nonzero local determinant-scale estimate of the form

`C |det A_m[I,I]|^(-1/3)`

costs exactly

`C m^(2/3)`.   (5.3)

Because all nonzero triples have the same cost, **every convex average over those local inverse-determinant bounds also equals `C m^(2/3)`**, regardless of the weights. In particular, determinant-mass weights `w_I=det(U_I)^2` do not help:

`sum_I w_I |det A_m[I,I]|^(-1/3) = m^(2/3)`.   (5.4)

Thus the fixed-row identity by itself cannot be converted into a dimension-free bound by selecting or averaging determinant-scale conditional triple estimates. This refutes the concrete averaging mechanism proposed at the end of my previous run.

It does **not** refute QFORM.

## 6. The same family has a uniform density cap after aggregation

Let the actual inputs be independent with density caps at most one. Lemma 3.1 gives

`M(Y_m)<=sqrt(2)`, `M(Z_m)<=sqrt(2)`

uniformly in `m`, while `M(X_0)<=1`. Apply Theorem 4.1 to

`Q_m = X_0^2 + 2 Y_m Z_m`

with square variable `X_0`, product variables `Y_m,Z_m`, `a=1`, `gamma=-2`, and `alpha=beta=0`. We obtain

`||p_{Q_m}||_infinity <= 4 sqrt(2)`.   (6.1)

The local determinant route loses `m^(2/3)` while the product-aggregation route is uniformly bounded. This is an exact source-valid separation between the two mechanisms.

### Named-partner Fourier inequality on the same family

Write

`F_0(t)=E exp(i t X_0^2)`,
`G_m(t)=E exp(i 2t Y_m Z_m)`.

The three aggregate variables are independent, so

`phi_{Q_m}(t)=F_0(t) G_m(t)`.

The named partner account03/B04 theorem applies directly to `X_0` and yields

`||F_0||_3 <= 2(2 pi)^(1/3)`.   (6.2)

For completeness, the bilinear factor itself has a dimension-free `L^3` bound. If independent `V,W` have density caps `M_V,M_W`, Hausdorff–Young plus Minkowski and the bathtub bound for `|v|^(-1/3)` give

`||E exp(i t c V W)||_3`
` <= 3 (pi/2)^(1/3) (M_V M_W/|c|)^(1/3)`.   (6.3)

Indeed condition on `V=v`, use

`||hat f_W(c v .)||_3 = |cv|^(-1/3)||hat f_W||_3`,
`||hat f_W||_3 <= (2pi)^(1/3)||f_W||_(3/2) <= (2pi)^(1/3)M_W^(1/3)`,

and

`int f_V(v)|v|^(-1/3)dv <= 3*2^(-2/3) M_V^(1/3)`.

For `c=2` and `M(Y_m),M(Z_m)<=sqrt(2)`, (6.3) gives

`||G_m||_3 <= 3(pi/2)^(1/3)`.   (6.4)

Holder on the product therefore gives the genuinely integrated-frequency estimate

`||phi_{Q_m}||_(3/2) <= 6 pi^(2/3)`,   (6.5)

uniformly in `m` and all admissible input laws.

Equation (6.5) is deliberately **not** promoted to an `L^1` bound. The actual density cap (6.1) comes from product-space rearrangement. This keeps the Fourier result compatible with the known pointwise-decay correction.

## 7. Fully diffuse genuinely rotated indefinite family

The same aggregate-before-invert mechanism gives an explicit family in which all three relevant block variables are diffuse. Split `3m` original coordinates into disjoint blocks and put

`X_m=m^(-1/2)sum_{i=1}^m X_i`,
`Y_m=m^(-1/2)sum_{i=m+1}^{2m} X_i`,
`Z_m=m^(-1/2)sum_{i=2m+1}^{3m} X_i`.

Consider

`R_m=(Z_m-X_m-Y_m)^2-4 X_m Y_m`.   (7.1)

On the three normalized block coordinates its matrix is

`B=2I_3-J_3`,

whose eigenvalues are `2,2,-1`. Hence the physical `3m x 3m` matrix has nonzero spectrum exactly `2,2,-1`, with rotated eigendirections spread over the blocks.

Lemma 3.1 gives

`M(X_m),M(Y_m),M(Z_m)<=sqrt(2)`.

Apply Theorem 4.1 with `a=1`, `gamma=4`, `alpha=beta=1`:

`||p_{R_m}||_infinity <= 4 sqrt(2)`.   (7.2)

For fixed aggregate values `(x,y)`, the named partner theorem also gives the actual conditional Fourier budget

`|| E_{Z_m} exp(i t (Z_m-x-y)^2) ||_3`
` <= 2(2pi)^(1/3)(sqrt(2))^(2/3)`
` = 2(4pi)^(1/3)`,   (7.3)

and Minkowski preserves the same bound for `||phi_{R_m}||_3`.

This family makes the localization loss even more explicit. A nonzero physical `3x3` principal minor must select one coordinate from each block, and then

`A_m[I,I]=(1/m)B`,
`det A_m[I,I]=-4/m^3`.   (7.4)

There are `m^3` such triples; every other physical triple is singular. Thus every local determinant-scale `|det|^(-1/3)` estimate costs `m/4^(1/3)`, while the exact global product-rearrangement cap (7.2) is independent of `m`.

This is a genuinely rotated indefinite target family, not an edge-disjoint, diagonal, same-sign, or post-rotation-independent substitute.

## 8. Sharpening the compatible account01/B19 hard family

Account01/B19 studies the exact target family

`Q=2 X_0 Y_m + Z_m^2`

with normalized aggregate variables and proves a uniform bound `<19.1` using a coarser aggregate-density cap `K=2sqrt(2)` followed by account02/B10's hyperbolic-square theorem.

Lemma 3.1 improves the aggregate cap to the sharp universal value

`M(Y_m),M(Z_m)<=sqrt(2)`.

Using the same hyperbolic-square scaling with `K=sqrt(2)` immediately sharpens that source-bound family estimate to

`||p_Q||_infinity <= 4 K^(3/2)`
` = 4*2^(3/4) = 2^(11/4) < 6.73`.   (8.1)

The same constant follows directly from Theorem 4.1 with square variable `Z_m`, product variables `X_0,Y_m`, `a=1`, `|gamma|=2`, caps `sqrt(2),1,sqrt(2)` in the appropriate slots.

This does not change the full target status, but it confirms quantitatively that high-cardinality aggregation repairs a family on which all fixed-local mechanisms degenerate.

## 9. Updated first universal obstruction

The previous proposal — average inverse determinant costs using the fixed-row wedge budget — is now ruled out by (5.2)–(5.4). The viable replacement has to **aggregate original coordinates before paying a singular inverse weight**.

A precise sufficient structural interface is now available: whenever a hard quadratic form can be represented on three independent original-coordinate blocks as

`a(L_Z-alpha L_X-beta L_Y)^2-gamma L_X L_Y`

with block coefficient vectors `w,u,v`, Theorem 4.1 and Lemma 3.1 give the explicit dimension-free resource (4.5). What is still unpaid is a universal extraction/trace theorem showing that every strongly coupled three-large-eigenvalue matrix either enters an already proved basin or exposes enough product-preserving aggregate mass to reach such a normal form (or an equally strong alternative) **without first selecting one tiny physical minor**.

Equivalently, in the account01/B19 conditional proof, the first unpaid global statement remains `QFORM-PRODUCT-ELLIPTIC-TRACE-AGGREGATE-v2`, now with an additional necessary design constraint supplied by this run: the proof must spend `l2` block mass through a Rogozin/Bobkov-type aggregate cap before any inverse determinant/singular-value factor. The high-leverage family (5.1) and diffuse family (7.1) are exact controls any candidate trace inequality must pass.

## 10. Honest status

- `QFORM-LINEAR-FORM-L2-CAP-v1`: proved from the source-matching Bobkov–Chistyakov min-entropy inequality.
- `QFORM-SHIFTED-SQUARE-CAPS-v2`: proved.
- Fixed-row inverse-minor averaging as proposed in the previous B04 run: `CANDIDATE_REFUTED` by the exact target family (5.1).
- High-leverage wedge-spread family: exact target spectrum `{1,1,-1}` and uniform density cap `4sqrt(2)`.
- Fully diffuse rotated family: exact target spectrum `{2,2,-1}` and uniform density cap `4sqrt(2)`.
- account01/B19 hard-family bound sharpened from `<19.1` to `<6.73` using the sharp aggregate cap.
- Full conjecture: **OPEN / NOT PROVED**.
- Continuity: not claimed beyond branches where an independent Fourier `L^1` argument is already available.

No decisive numerical computation is used in any theorem above; all constants are analytic.
