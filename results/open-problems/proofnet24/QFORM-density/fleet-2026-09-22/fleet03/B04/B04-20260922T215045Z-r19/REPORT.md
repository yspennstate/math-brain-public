SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-22T21:50:45Z.
attacking: an L^6 decreasing-rearrangement bound for translated hyperbolic products, its half-Riesz consequence, and a three-disjoint-bank rank-one-completion plus defect packet.

# fleet03/B04 r19 — hyperbolic-product L6 rearrangement and overlap-safe square/defect closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Run:** `B04-20260922T215045Z-r19`  
**Fresh control at start:** QFORM-only, owner revision `2026-09-22.15`; control branch observed at `52cb2725682f68daf07e9e1583c12d8e641f0344` before the substantive write.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository access is not native brain ingestion.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL QFORM OPEN`.

## 1. Scope and corrections

The full target remains open. Inputs are independent original real coordinates with density caps at most one. No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, arbitrary-joint coarea, positive conditional-projection-moment, or law-uniform pointwise oscillatory-decay assumption is used.

This run changes mechanism from r18's direct moving-log trace of a pure cross triangle. The new route first obtains a high-integrability physical-density estimate for a translated hyperbolic product by decreasing rearrangement, then converts that estimate into a half-Riesz bound. This permits a completed scalar square to overlap arbitrarily with both variables supporting the hyperbolic defect. It therefore pays a concrete part of r18's `QFORM-TRIBANK-DEFECT-REARRANGEMENT-ROUTING-v1` obligation rather than pretending arbitrary same-bank quadratic leakage is harmless.

### Completed peer mathematics actually consumed

The completed fleet02/B04 report

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T181702Z-dac07509/REPORT.md`

supplies two source-valid inputs used in actual inequalities below:

1. for independent cap-one `U,V` and `c!=0`, including arbitrary deterministic translations,

`p_(2cUV)(s) <= |c|^(-1)[1+log_+(2|c|/|s|)]`;                 (1.1)

2. for a linear form over an original-coordinate bank,

`U=u^T X_I`, `s=||u||_2>0`,

`||p_U||_infinity <= sqrt(2)/s`.                              (1.2)

The designated partner is fleet04/B04. A fresh lookup of its current QFORM handoff directory still returned no completed artifact, so no exact-partner result is fabricated. The fleet02/B04 same-role theorem above is the completed compatible result actually applied.

## 2. A mass-filling L6 theorem for a translated hyperbolic product

Let `z_*` be the unique root `z>2` of

`4 z exp(-(z-2)) = 1`.                                       (2.1)

Numerically,

`z_* = 4.994664629781440392391150218754047...`.              (2.2)

Set

`K_6 = z_*^5 + 15 z_*^3 + 40 z_*^2 + 135 z_* + 264 + 265/z_*`

`    = 6966.56995486964376752519449299628...`.                (2.3)

### Theorem 2.1 — `QFORM-HYPERBOLIC-PRODUCT-L6-v1`

Let `U,V` be independent real random variables with probability densities bounded by one. Let `c!=0`, and let `alpha,beta` be arbitrary deterministic translations. If

`T=2c(U+alpha)(V+beta)`,

then `T` has a density `g` satisfying

`||g||_6^6 <= K_6 |c|^(-5)`,                                 (2.4)

hence

`||g||_6 <= K_6^(1/6)|c|^(-5/6)`.                            (2.5)

#### Proof

Translations preserve the density caps, so (1.1) gives

`0<=g(s)<=k_c(s):=|c|^(-1)[1+log_+(2|c|/|s|)]`.              (2.6)

Also `integral g=1`. Put

`L=z_*-2`, `a=e^(-L)`, `r=2|c|a`.

By (2.1), `4a(L+2)=1`. Direct integration gives

`integral_(|s|<=r) k_c(s) ds`
` =4 integral_0^a (1+log(1/u))du`
` =4a(L+2)=1`.                                                (2.7)

Let `g^*,k_c^*` be decreasing rearrangements. Since `g<=k_c`, one has `g^*<=k_c^*`; since both `g` and `h:=k_c 1_(|s|<=r)` have mass one,

`integral_0^x g^* <= integral_0^x h^*` for every `x>=0`.     (2.8)

Thus `h` majorizes `g`. Convexity of `x -> x^6` gives

`integral g^6 <= integral h^6`
` =4|c|^(-5) integral_0^a (1+log(1/u))^6 du`.                (2.9)

With `v=log(1/u)` and then `w=v+1`,

`4 integral_0^a (1+log(1/u))^6 du`
` =4e Gamma(7,z_*-1)`.                                       (2.10)

For the integer exponent six this equals

`4a[(z_*-1)^6+6(z_*-1)^5+30(z_*-1)^4+120(z_*-1)^3`
`    +360(z_*-1)^2+720(z_*-1)+720]`.                         (2.11)

Using `4az_*=1`, (2.11) simplifies exactly to the expression `K_6` in (2.3). This proves (2.4). QED.

This is a physical-density rearrangement theorem. It does not assert any pointwise Fourier decay.

## 3. New half-Riesz estimate for a hyperbolic product

Define

`H_6 := sqrt(5)[(3/2)^(2/5)+(2/3)^(3/5)] K_6^(1/10)`

`     = 10.6187196675779193598881105947637...`.              (3.1)

### Theorem 3.1 — `QFORM-HYPERBOLIC-HALFRIESZ-v1`

Under Theorem 2.1,

`sup_(t in R) E |t-T|^(-1/2) <= H_6 |c|^(-1/2)`.             (3.2)

#### Proof

Write `G=||g||_6`. For every `R>0`, split the half-Riesz integral into `|t-s|<=R` and its complement. Hölder with exponents `6` and `6/5` gives

`int_(|t-s|<=R) g(s)|t-s|^(-1/2) ds`
` <= G [int_(|x|<=R)|x|^(-3/5)dx]^(5/6)`
` =5^(5/6) G R^(1/3)`.                                      (3.3)

The complementary part is at most `R^(-1/2)` because `g` has mass one. Therefore

`E|t-T|^(-1/2) <= A R^(1/3)+R^(-1/2)`,
`A=5^(5/6)G`.                                                (3.4)

The minimum occurs at

`R^(5/6)=3/(2A)`.                                            (3.5)

Substitution yields

`min_R [A R^(1/3)+R^(-1/2)]`
` =sqrt(5)[(3/2)^(2/5)+(2/3)^(3/5)] G^(3/5)`.                (3.6)

By (2.5),

`G^(3/5) <= K_6^(1/10)|c|^(-1/2)`.                          (3.7)

Equations (3.6)-(3.7) prove (3.2). QED.

A numerical optimization over the same general `L^p`, `p>2`, family gives a slightly smaller constant near `p=5.733`, but the integer choice `p=6` is retained here because (2.3) is exact and the proof is fully elementary once the source envelope is accepted.

## 4. Overlap-safe completed square plus hyperbolic defect

### Theorem 4.1 — `QFORM-SQUARE-OVERLAP-HYPERBOLIC-v1`

Let `Z,U,V` and an outside variable/group `W` be mutually independent. Suppose `Z,U,V` have densities bounded by one. Let `a,c!=0`. Allow arbitrary measurable functions

`m=m(U,V,W)`, `alpha=alpha(W)`, `beta=beta(W)`, `R=R(W)`.

Define

`Q = a[Z+m(U,V,W)]^2`
`    +2c[U+alpha(W)][V+beta(W)] + R(W)`.                     (4.1)

Then `Q` is absolutely continuous and

`boxed: ||p_Q||_infinity <= H_6 / sqrt(|a c|)`.              (4.2)

No independence between the completed-square shift `m(U,V,W)` and the hyperbolic variables is required.

#### Proof

Condition on `(U,V,W)=(u,v,w)`. The variable `Z+m(u,v,w)` is a translate of the original cap-one variable `Z`. Therefore the conditional density of the square term obeys

`p_(a[Z+m]^2 | U,V,W)(s) <= |a|^(-1/2)|s|^(-1/2)`           (4.3)

on its appropriate half-line, and the same upper bound with an indicator removed is valid for all `s!=0`.

Let

`T_w=2c[U+alpha(w)][V+beta(w)]`.

Averaging (4.3) first over `U,V` gives, for a.e. `q`,

`p_(Q|W=w)(q)`
` <= |a|^(-1/2) E_(U,V)|q-R(w)-T_w|^(-1/2)`.                (4.4)

Theorem 3.1 is uniform in the translated inputs and in the output center, so the right side is at most `H_6/sqrt(|ac|)`. Averaging over `W` preserves the same bound. Since every conditional square law is absolutely continuous, their mixture is absolutely continuous. QED.

The theorem establishes essential boundedness, not a continuous representative for arbitrary merely measurable input densities.

## 5. Aggregate original-coordinate bank lift

Let `I_0,I_1,I_2,W` be mutually disjoint original-coordinate groups and define

`Z=z^T X_(I_0)`, `U=u^T X_(I_1)`, `V=v^T X_(I_2)`,

`s_0=||z||_2`, `s_1=||u||_2`, `s_2=||v||_2`, all positive. (5.1)

By the completed fleet02/B04 bank theorem (1.2),

`||p_Z||_infinity <= sqrt(2)/s_0`,
`||p_U||_infinity <= sqrt(2)/s_1`,
`||p_V||_infinity <= sqrt(2)/s_2`.                           (5.2)

### Corollary 5.1 — `QFORM-SQUARE-HYPERBOLIC-THREEBANK-v1`

For a quadratic-form packet of the form (4.1) built from these bank variables,

`boxed: ||p_Q||_infinity`
` <= 2 H_6 / [s_0 sqrt(s_1 s_2) sqrt(|a c|)]`.              (5.3)

#### Proof

Set

`Z'=(sqrt(2)/s_0)Z`, `U'=(sqrt(2)/s_1)U`, `V'=(sqrt(2)/s_2)V`.

The primed variables are independent and cap-one. In primed variables the square coefficient is `a s_0^2/2`, while the hyperbolic coefficient is `c s_1 s_2/2`. Applying Theorem 4.1 gives

`H_6 / sqrt(|a c| s_0^2 s_1 s_2/4)`,

which is exactly (5.3). QED.

This is the promised actual application of the completed peer bank-projection result. The bound pays aggregate Euclidean bank scales before any individual matrix entry is inverted.

## 6. Genuinely rotated indefinite target family with nonzero same-bank curvature

For every integer `m>=2`, split `3m` original coordinates into three disjoint banks and let `r_0,r_1,r_2` be the corresponding flat unit vectors, each equal to `m^(-1/2)(1,...,1)` on its bank and zero elsewhere. Put

`Z=r_0^T X`, `U=r_1^T X`, `V=r_2^T X`.                      (6.1)

Let

`B = [[1,1,-1],[1,1,1],[-1,1,1]]`.                          (6.2)

Its characteristic polynomial is

`(lambda-2)^2(lambda+1)`,                                   (6.3)

so its spectrum is `{-1,2,2}`. Define the full physical matrix

`A_m = [r_0 r_1 r_2] (2B) [r_0 r_1 r_2]^T`.                 (6.4)

Because the three bank vectors are orthonormal, the nonzero spectrum of `A_m` is exactly

`{-2,4,4}`.                                                  (6.5)

Thus every `A_m` is a genuinely rotated indefinite target matrix with three eigenvalues of modulus at least one. Moreover every nonzero physical entry of `A_m` has magnitude exactly `2/m`, including the same-bank blocks, so no fixed local coefficient survives as `m->infinity`.

The quadratic form is

`Q_m = 2(Z+U-V)^2 + 8UV`.                                    (6.6)

This is precisely a rank-one square completion plus a hyperbolic defect. Apply Corollary 5.1 with

`s_0=s_1=s_2=1`, `a=2`, `c=4`, `m(U,V)=U-V`.

Then for every admissible product input law,

`boxed: ||p_(Q_m)||_infinity <= H_6/sqrt(2)`
`       = 7.50856868446330849154128024801465...`.            (6.7)

The estimate is independent of `m` although every physical coefficient tends to zero. Essential boundedness and absolute continuity are proved. Continuity is not claimed by this argument.

This family lies exactly in the leakage geometry that r18 could not cover by the pure-cross theorem: the same-bank rank-one blocks are nonzero and participate in a rank-one completion. The new half-Riesz mechanism pays the remaining hyperbolic defect without requiring the square shift to be independent of that defect.

## 7. First unpaid implication after this run

`QFORM-MULTIDEFECT-BANK-ROUTING-v1`:

Starting from an arbitrary three-bank packet after the unique rank-one completion of its cross triangle, show that the forced rank-at-least-two defect matrix can be routed, with dimension-free aggregate currency, into either

1. one overlap-safe square plus one hyperbolic defect of Theorem 4.1 / Corollary 5.1; or
2. an already-paid rank-two/ridge/multi-bank endpoint,

without choosing a vanishing physical entry, conditioning on orthogonal coordinates inside an active bank, or discarding additional quadratic leakage. The new theorem pays the analytic endpoint when the defect is rank-one hyperbolic after completion; the remaining issue is the exhaustive product-preserving structural routing from the bare spectral hypothesis.

## 8. Status

- Full QFORM conjecture: **OPEN**.
- `QFORM-HYPERBOLIC-PRODUCT-L6-v1`: **PROVED**.
- `QFORM-HYPERBOLIC-HALFRIESZ-v1`: **PROVED**.
- `QFORM-SQUARE-OVERLAP-HYPERBOLIC-v1`: **PROVED**, essential boundedness/absolute continuity; continuity not claimed.
- `QFORM-SQUARE-HYPERBOLIC-THREEBANK-v1`: **PROVED** using the completed fleet02/B04 bank projection theorem.
- Flat three-bank target family (6.4): **all-input-law bound `<=7.5085686845` proved**; three large eigenvalues `{-2,4,4}`; all physical entries `2/m` in magnitude.
- Designated fleet04/B04 current-QFORM completion: **not found at fresh lookup**; none fabricated.
- Native brain ingestion: **not verified**.
