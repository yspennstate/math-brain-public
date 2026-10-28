SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T00:31:41Z.
attacking: two-sided contaminated hyperbolic packets: derive a joint product-space small-ball/logarithmic estimate and splice it with a disjoint clean hyperbolic pair without taking a divergent half-Riesz norm

# account01/B04 r22 — two-sided contamination: joint small-ball/log potential and clean-pair splice

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository retrieval was used; no native learned-memory receiver/ingestion was observed.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`.

The full conjecture is not proved. The new result below pays a specific obstruction identified by the designated partner: arbitrary contamination on both scalar sides of a hyperbolic packet destroys the standalone half-Riesz bridge, but it can still be smoothed uniformly if one disjoint clean hyperbolic pair is retained. The proof is a product-space Cauchy--Schwarz/difference argument followed by decreasing rearrangement. It uses no pointwise quadratic-phase decay, no post-rotation independence, no moments, and no arbitrary-joint coarea bound.

## 1. Current source boundary

The newest owner-directed synthesis used here is

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/`,

with the newest Claude path-specific source still

`yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The synthesis reduces the full theorem to the no-pivot statement N3 and explicitly leaves N3 open. Its determinant-only physical-pair and logarithmic auxiliary bounds are compatible with the present argument but are not enough to force the product packet used below.

The designated OTHER-account result actually consumed is account02/B04 r20:

`yspennstate/math-open-problems@63c72a057b0dfcaa747ba70e287eef8f62305687:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T222038Z-r20/REPORT.md`.

It proves `QFORM-SQUARE-OVERLAP-ONE-SIDED-CONTAMINATION-v1`, and also gives the decisive counterexample `QFORM-HYPERBOLIC-TWOSIDED-HALFRIESZ-UNIFORM-FALSE-v1`: for independent uniform `U,V` on `[-1/2,1/2]`,

`2UV+U^2+V^2=(U+V)^2`

has infinite half-Riesz quantity at zero. Therefore the new argument below deliberately does **not** attempt a uniform `E|T-t|^{-1/2}` estimate for an arbitrarily two-sided contaminated hyperbolic defect.

## 2. New theorem: two-sided contamination has a universal square-root-log small-ball bound

### Theorem 2.1 — `QFORM-TWOSIDED-CONTAMINATION-SMALLBALL-v1`

Let `U,V` be independent real random variables with probability densities bounded by `M_U,M_V`, respectively. Let `c != 0`, and let `F,G` be arbitrary measurable real functions. Put

`T = 2c U V + F(U) + G(V)`.

Translations `U+alpha`, `V+beta` are included after absorbing their linear terms into `F,G`. Then for every `t in R` and every `epsilon>0`, with

`x = 4 M_U M_V epsilon / |c|`,

we have

`P(|T-t| <= epsilon)^2 <= 1`,

and, when `0 < x < 1`,

`boxed: P(|T-t| <= epsilon)^2 <= x [1 + log(1/x)].`        (2.1)

Equivalently,

`boxed: P(|T-t| <= epsilon) <= min(1, sqrt(x[1+log_+(1/x)]))`,      (2.2)

where in (2.2) the expression inside the square root is used only for `x<1` and the cap `1` otherwise.

#### Proof

For fixed `v`, define

`r(v) = P_U(|2cUv+F(U)+G(v)-t| <= epsilon)`.

Then `P(|T-t|<=epsilon)=E_V r(V)`. Cauchy--Schwarz with respect to the **same** variable `V` gives

`P(|T-t|<=epsilon)^2 <= E_V r(V)^2`

`= E_{U,U'} P_V(V in E_U intersection E_U')`,                    (2.3)

where `U'` is an independent copy of `U`, and

`E_u={v: |2cuv+F(u)+G(v)-t|<=epsilon}`.

If `u != u'` and `v in E_u intersection E_u'`, subtracting the two inequalities cancels the arbitrary `G(v)` exactly and yields

`|2c(u-u')v + F(u)-F(u')| <= 2 epsilon`.

Hence `E_u intersection E_u'` lies in an interval of length

`2 epsilon/(|c| |u-u'|)`.

Since `p_V<=M_V`, (2.3) implies

`P(|T-t|<=epsilon)^2
 <= E min(1, 2 M_V epsilon/(|c| |U-U'|)).`                       (2.4)

The difference `D=U-U'` has a probability density `h_D` satisfying `h_D<=M_U`, because

`h_D(d)=int f_U(y) f_U(y-d) dy <= M_U int f_U(y-d)dy=M_U`.

The kernel `k_A(d)=min(1,A/|d|)`, `A=2M_V epsilon/|c|`, is symmetric decreasing. By decreasing rearrangement / the bathtub principle, among all probability densities bounded by `M_U`, its integral is maximized by density `M_U` on the centered interval of length `1/M_U`. Put `L=1/(2M_U)`. If `A<L`,

`E k_A(D)
 <= M_U [2A + 2A log(L/A)]
 = x[1+log(1/x)]`,

because `x=A/L=4M_U M_V epsilon/|c|`. If `A>=L`, the trivial bound `1` applies. This proves (2.1)-(2.2). QED.

### Sanity check against the partner obstruction

For `c=1`, `F(u)=u^2`, `G(v)=v^2`, the defect is `(U+V)^2`. Its small-ball probability near zero is naturally of order `sqrt(epsilon)`, so the theorem is consistent with the fact that the half-Riesz integral at exponent `1/2` can diverge. The theorem therefore repairs the useful part of the two-sided route without contradicting the partner's exact counterexample.

## 3. New theorem: universal logarithmic potential for the same contaminated packet

### Theorem 3.1 — `QFORM-TWOSIDED-CONTAMINATION-LOG-v1`

Under Theorem 2.1, for every `K>0`,

`boxed: sup_t E log_+(K/|T-t|)
 <= 4 + log_+(4 M_U M_V K/|c|).`                                (3.1)

#### Proof

Use nonnegative layer cake:

`E log_+(K/|T-t|)
 = int_0^infinity P(|T-t| < K exp(-s)) ds.`                      (3.2)

Set `A_0=4M_U M_V K/|c|`. If `A_0>=1`, the interval `0<=s<=log A_0` contributes at most `log A_0`. For `s=log A_0+r`, Theorem 2.1 gives

`P(...) <= exp(-r/2) sqrt(1+r)`.

If `A_0<1`, the same tail estimate starts later and is smaller. Finally

`int_0^infinity exp(-r/2) sqrt(1+r) dr
 <= int_0^infinity exp(-r/2)(1+r/2)dr
 =4.`

This proves (3.1). QED.

This is the finite potential that survives exactly where the standalone half-Riesz potential fails.

## 4. New theorem: one clean hyperbolic pair smooths arbitrary contamination on both active sides

### Theorem 4.1 — `QFORM-TWOSIDED-CONTAMINATION-CLEAN-PAIR-SPLICE-v1`

Let `U,V,Z,W` be mutually independent real variables with density caps

`M_U,M_V,M_Z,M_W`.

Let `c,d != 0`; let `F,G` be arbitrary measurable functions. Arbitrary deterministic translations of all four variables are allowed. Let

`T=2cUV+F(U)+G(V)`,
`H=2dZW`,

and suppose `T,H` are independent (as they are for disjoint original-coordinate packets). Put

`R=M_U M_V`, `P=M_Z M_W`.

Then `T+H` is absolutely continuous and

`boxed:
 ||p_(T+H)||_infinity
 <= (2P/|d|) [2+log 2 + (1/2)log_+(2R|d|/(P|c|))].`             (4.1)

The same bound holds conditionally and hence after averaging if translations, `F`, `G`, and an additive remainder depend on disjoint outside original coordinates.

#### Proof

The completed coordinate-product rearrangement from the current Fourier source (Lemma 4.3 there) rescales to density caps `M_Z,M_W` as

`p_H(s)
 <= (2P/|d|) log(1 + sqrt(|d|/(2P|s|))).`                       (4.2)

For `y>0`,

`log(1+sqrt(y)) <= log 2 + (1/2) log_+ y.`                       (4.3)

Condition on `T`. With `K=|d|/(2P)`, (4.2)-(4.3) and Theorem 3.1 give

`p_(T+H)(q)
 <= (2P/|d|)[log2 + (1/2) E log_+(K/|q-T|)]`

`<= (2P/|d|)[log2 + 2 + (1/2)log_+(4RK/|c|)]`

`= (2P/|d|)[2+log2+(1/2)log_+(2R|d|/(P|c|))].`

This proves (4.1). Because `H` has a density and is independent of `T`, the sum is absolutely continuous. QED.

### Interpretation

This theorem directly pays a nontrivial part of account02/B04 r20's first unpaid implication `QFORM-TWOSIDED-CONTAMINATION-JOINT-SPLICE-v1`: arbitrary `F(U)` and `G(V)` may coexist, provided one disjoint clean hyperbolic pair is preserved until the smoothing step. No reciprocal individual physical minor is selected inside either contaminated side.

It does **not** prove that every N3 matrix contains such a clean pair. That is now the structural debt.

## 5. Square-overlap lift: the square shift may reuse every active packet

### Corollary 5.1 — `QFORM-SQUARE-OVERLAP-TWOSIDED-WITH-CLEAN-PAIR-v1`

Let `S` be independent of `U,V,Z,W` with density cap `M_S`, let `a!=0`, and let `m=m(U,V,Z,W,Omega)` be an arbitrary measurable shift; `Omega` denotes any disjoint outside original coordinates. Let

`Y=T+H+R(Omega)`

be as in Theorem 4.1 conditionally on `Omega`, with uniform density cap `B` equal to the right side of (4.1). Then

`Q=a[S+m(U,V,Z,W,Omega)]^2 + Y`

is absolutely continuous and

`boxed: ||p_Q||_infinity <= 2 sqrt(2) M_S |a|^(-1/2) sqrt(B).`     (5.1)

#### Proof

Condition on all variables except `S`. The translated-square density is bounded by

`M_S |a|^(-1/2) |q-Y|^(-1/2)`.

A probability density bounded by `B` satisfies, by the same centered-interval rearrangement,

`sup_q E|q-Y|^(-1/2) <= 2 sqrt(2B).`

Average the conditional square bound and obtain (5.1). QED.

This is exactly the mechanism suggested by the partner's counterexample: do not demand a half-Riesz bound from the collapsed two-sided defect; retain another genuinely independent smoothing packet first, and only then spend the square singularity.

## 6. Designated partner result applied to an actual target-valid inequality

Apply account02/B04 r20 Theorem 3.1 (`QFORM-SQUARE-OVERLAP-ONE-SIDED-CONTAMINATION-v1`) to three independent original cap-one variables `S,U,V`:

`Q_partner=2(S+U-V)^2+8UV+U^2.`

Here `a=2`, `c=4`, `M_S=M_U=M_V=1`, the square shift reuses both active variables, and `F(U)=U^2`. The partner theorem gives the actual inequality

`boxed: ||p_(Q_partner)||_infinity <= 4.`                          (6.1)

Its active matrix has characteristic polynomial

`-(lambda-4)(lambda-lambda^2+2lambda+8)`,

hence eigenvalues

`4, (3+sqrt(41))/2, (3-sqrt(41))/2`;

the negative eigenvalue has modulus `(sqrt(41)-3)/2>1`. Thus (6.1) is already an all-law target-valid rotated-indefinite application of the designated partner theorem.

The next section adds the opposite-side contamination that the partner theorem cannot absorb by itself.

## 7. Explicit genuinely rotated indefinite example with arbitrary-side mechanism active

Let `S,U,V,Z,W` be five independent arbitrary input variables, each with density at most one. Define

`Q_sharp = 2(S+U-V+Z+W)^2 + U^2 + 8UV + V^2 + 2ZW.`              (7.1)

Every off-diagonal coefficient of its physical 5-by-5 matrix is nonzero, so this is genuinely nonseparable in the original product coordinates.

For the residual contaminated pair,

`T=8UV+U^2+V^2`

has `c=4`, `R=M_UM_V=1`. The clean pair `H=2ZW` has `d=1`, `P=1`. Theorem 4.1 gives

`B=2[2+log2+(1/2)log_+(1/2)] = 4+2log2.`

The outer square has `a=2`, `M_S=1`, so Corollary 5.1 gives

`boxed: ||p_(Q_sharp)||_infinity
 <= 2 sqrt(4+2log2)
 = 4.641678300408115... .`                                        (7.2)

This bound holds for **every** choice of the five independent cap-one input laws.

To certify the target spectrum without numerical diagonalization, write

`A=B_0+2vv^T`,

with `v=(1,1,-1,1,1)` in coordinates `(S,U,V,Z,W)`, and `B_0` equal to zero on `S`, the `UV` block `[[1,4],[4,1]]`, and the `ZW` block `[[0,1],[1,0]]`. Thus

`spec(B_0)={-3,-1,0,1,5}`.

Since `2vv^T` is positive semidefinite, Weyl monotonicity gives the two largest eigenvalues of `A` at least `1` and `5`. Moreover `(0,0,0,1,-1)` is orthogonal to `v` and is an exact `-1` eigenvector of `B_0`, hence remains an exact `-1` eigenvector of `A`. Therefore `A` has at least three eigenvalues of absolute value at least one. It is indefinite and fully coupled.

The result proves essential boundedness for this family. **Continuity is not claimed** by the present argument.

## 8. Compact conditional end-to-end argument and remaining implication

The newest synthesis reduces the full theorem to N3: fixed `tau`, three large eigenvalues, all physical scalar pivots and all physical 2-by-2 determinant pivots small. For B04's product route, the following conditional closure is now available:

1. if a product-preserving decomposition leaves a one-sided contaminated hyperbolic packet under an overlapping square, apply account02/B04 r20;
2. if both active sides are contaminated but a disjoint clean hyperbolic packet survives, apply Theorem 4.1 and, if needed, Corollary 5.1;
3. if a determinant pair, D'/D5 volume certificate, ridge window, mixed-Fresnel hub, or localized finite core is present, use the already completed corresponding branch.

Therefore the first unpaid implication for this route is

`QFORM-N3-CONTAMINATION-PACKET-EXTRACTION-v1`:

> In the N3 no-pivot class, after the existing D'/D5, ridge, determinant-pair, and localized-core exits fail, prove a product-preserving routing that either makes one active hyperbolic side one-sided-contaminated, or preserves a disjoint clean hyperbolic smoothing packet while the remaining two-sided contamination is kept intact; otherwise route the same aggregate currency into an already paid mixed-hub/grouped-coordinate branch.

The latest account02/B19 correction is respected: positive low-order volume currency does not freely force two singular directions, and the N3 mixed-hub geometry cannot be localized to one physical square/pair collision certificate before aggregation. The present theorem assumes an actual disjoint clean packet; it does not infer one from aggregate currency.

## 9. Status and safeguards

- Full QFORM conjecture: **OPEN**.
- Full-target continuous density: **OPEN**.
- `QFORM-TWOSIDED-CONTAMINATION-SMALLBALL-v1`: **PROVED here**.
- `QFORM-TWOSIDED-CONTAMINATION-LOG-v1`: **PROVED here**.
- `QFORM-TWOSIDED-CONTAMINATION-CLEAN-PAIR-SPLICE-v1`: **PROVED here**.
- `QFORM-SQUARE-OVERLAP-TWOSIDED-WITH-CLEAN-PAIR-v1`: **PROVED here**.
- account02/B04 r20 result: **read from immutable source and applied to (6.1)**.
- Refuted pointwise-decay, arbitrary-joint-coarea, conditional-moment, fiber-sup, fixed-good-minor, and two-sided-half-Riesz shortcuts are not used.
- No scheduler, notification, email, Drive, public-release, paid-model/API, remote-workflow, cross-account-authentication, or permission mutation was performed.
