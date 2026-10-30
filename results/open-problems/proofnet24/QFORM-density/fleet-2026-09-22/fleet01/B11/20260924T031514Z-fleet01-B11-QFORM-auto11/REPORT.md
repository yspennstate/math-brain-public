SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-24T03:15:14Z.
attacking: the nonzero physical-pivot near-coloop collar: absorb the surviving fresh-hub square while retaining same-bank leakage and rank-three determinant scale.

# fleet01/B11 auto11 — arbitrary-pivot low-residual-rank compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control read: revision `2026-09-22.15`; programme revision `2026-09-22.5`  
Status: **NEW SUPPORTING THEOREM / NONZERO-PIVOT LOW-RESIDUAL-RANK BRANCH CLOSED / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **not proved** by the theorem below; it proves absolute continuity and an essential density bound.

The unrestricted owner target remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, post-rotation independence, conditional-density-cap-as-independence, pointwise law-uniform van-der-Corput decay, or perturbative deletion of a small coefficient is used.

## 1. Fresh source state and first missing implication

Fresh `math-research-brain/main` still has QFORM as the sole target and `CLAIMS.json` still marks both `QFORM-FULL` and the full continuous-representative claim OPEN.

The immediately preceding fleet01/B11 run is

- `yspennstate/math-open-problems@22373d23a5a18f91627d8849017beb38a2169f23`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260924T025136Z-fleet01-B11-QFORM-auto11/REPORT.md`.

It pays the exact zero-pivot near-coloop same-bank puncture by preserving a literal hub, and leaves the nonzero physical-pivot double-aligned / punctured collar as the first B11 debt.

Two completed analytic inputs are used at their exact scopes.

1. `QFORM-SUBCRITICAL-HUB-PLANAR-CORE-v1`, this slot's earlier theorem at
   `yspennstate/math-open-problems@cedc867395f462e31df64232907480cea07db3d5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260923T191247Z-fleet01-B11-QFORM-auto11/REPORT.md`.
   If `H` is a cap-one scalar independent of a planar vector of joint density cap `M`, a `3 x 3` symmetric core `T` has `sigma_min(T)>=sigma`, and `|T_HH|<=r sigma` with `r<1`, then
   
   `||p_Q||_infinity <= B(r,M)/sigma`,
   
   where
   
   `B(r,M)=1+M[2/sqrt(1-r^2)+2+G0 sqrt(5+(1+2r)^2/(1-r^2))]`,
   
   `G0=(2 pi)^(3/2)e^(1/2) Gamma(1/4)/(4 sqrt(pi) Gamma(3/4))`.

2. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` and its scalar-pivot consequence at
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   For an exact-rank-three block `A=V M V^T`, a physical row of spectral leverage `c_i`, and nonzero physical pivot `a=A_ii`,
   
   `||p_Q||_infinity <=128 [c_i |a| |det M|]^(-1/4)`.

A source search found nearby zero-pivot residual-rank classification and small-hub three-variable theorems, but no source-matching statement that combines these two inputs into the arbitrary-pivot `rank(A_{-i,-i})<=2` theorem below. The zero-pivot aggregate theorem in fleet01/B05 is strictly narrower in the pivot variable.

## 2. Exact structural lemma: low residual rank forces an honest scalar-plus-plane core

Write, at a literal ORIGINAL coordinate `i`,

`A = [[a, l^T], [l, C]]`,

where `C=A[-i,-i]`. Assume

`rank A = 3`, `rank C <=2`.

### Lemma 2.1 — `QFORM-RANK3-LOWRESIDUAL-CORE-v1`

There is a two-dimensional deterministic subspace `W` of the residual ORIGINAL-coordinate space such that

`Ran A = span{e_i} direct_sum W`.

Consequently, if `u,v` are an orthonormal basis of `W` and

`B=[e_i,u,v]`,

then

`B^T B=I_3`, `A=B T B^T`, `T=B^T A B`,

and the three eigenvalues of `T` are exactly the three nonzero eigenvalues of `A`. In particular,

`sigma_min(T)=s_3(A)` and `|det T|=Delta_3(A)`.

Moreover the spectral leverage of the physical coordinate `i` is exactly one.

### Proof

Decompose the residual space orthogonally as

`R^(n-1)=Ran(C) direct_sum Ker(C)`

and write `l=l_R+l_K`.

**Case 1: `l_K !=0`.** By a congruence eliminating `l_R` against `C` on `Ran(C)`, the hub and the nonzero kernel component form a nonsingular `2 x 2` block. Hence

`rank A = rank C +2`.

Since `rank A=3`, necessarily `rank C=1`. Therefore

`W=Ran(C)+span{l}`

has dimension exactly two.

**Case 2: `l_K=0`.** Then `l in Ran(C)`. Put `kappa=l^T C^+ l`. The standard Schur congruence gives

`rank A = rank C + 1_{a-kappa !=0}`.

Rank three with `rank C<=2` forces `rank C=2` and `a-kappa !=0`. Again

`W=Ran(C)`

has dimension exactly two.

In both cases `C` vanishes on `W^perp` and `l` is orthogonal to `W^perp`, so `A` vanishes on `{0} direct_sum W^perp`. Thus

`Ran A subset span{e_i} direct_sum W`.

Both spaces have dimension three because `rank A=3`, so equality holds. In particular `e_i in Ran A`, proving leverage one. Choosing an orthonormal basis `B` of this range yields `A=B T B^T`; nonzero spectra are preserved by this orthonormal compression. QED.

This lemma is purely deterministic. It does not rotate the probability law.

## 3. New theorem: every arbitrary pivot is paid on the low-residual-rank branch

Let the three nonzero eigenvalues of `A` have absolute value at least `s>0`.

Let

`H=X_i`,
`Y=(u^T X_{-i}, v^T X_{-i})`.

The scalar `H` is a literal ORIGINAL input, hence is independent of the entire residual product bank. Since `u,v` are orthonormal coefficient vectors, the standard two-dimensional product-projection theorem gives

`||p_Y||_infinity <=2`.

No independence between the two coordinates of `Y` is asserted.

The quadratic is exactly

`Q=(H,Y)^T T(H,Y)`,

up to arbitrary deterministic affine terms if this theorem is used after outside-coordinate conditioning. By Lemma 2.1,

`sigma_min(T)>=s`, `|det T|>=s^3`, and `T_HH=a=A_ii`.

Fix the numerical threshold

`r0=0.848`.

### Theorem 3.1 — `QFORM-ARBITRARY-PIVOT-LOWRESIDUAL-RANK-v1`

Under the preceding hypotheses,

`Q` has an absolutely continuous law and

`boxed: ||p_Q||_(infinity,ess) < 134/s.`

The theorem is sign-free, so it covers both exact-rank-three indefinite signatures `(+,+,-)` and `(+,-,-)`.

### Proof

Split on the literal physical pivot.

**Subcritical pivot:** if `|a|<=r0 s`, apply `QFORM-SUBCRITICAL-HUB-PLANAR-CORE-v1` with planar cap `M=2`, core scale `sigma=s`, and ratio `r=r0`. Its explicit formula gives

`B(0.848,2)=132.97278587755545...`.

Therefore

`||p_Q||_infinity <132.973/s`.

**Large pivot:** if `|a|>r0 s`, use the orientation-free scalar-pivot theorem. Lemma 2.1 gives hub leverage `c_i=1`, while `|det T|>=s^3`; hence

`||p_Q||_infinity
 <=128 [|a| |det T|]^(-1/4)
 <128 r0^(-1/4) s^(-1)
 =133.38623266130324.../s`.

Taking the worse branch proves the claimed `<134/s`. QED.

The threshold can be optimized by solving

`B(r,2)=128 r^(-1/4)`.

The numerical crossing is `r=0.84893219108...`, giving `133.34960056.../s`; I retain the round constant `134/s` in the theorem.

### Three-original-coordinate corollary

If the whole matrix is a nonsingular `3 x 3` symmetric matrix on three ORIGINAL independent coordinates, the planar cap is actually one. The same argument with `M=1` gives an optimized numerical constant below `130/s`. The general ambient theorem uses `M=2` because `(u^T X,v^T X)` is a two-dimensional product projection rather than necessarily a literal coordinate pair.

## 4. Scope inside the B11 collar

This theorem closes the entire portion of the nonzero-pivot double-aligned collar for which deleting the selected physical hub leaves a residual principal block of rank at most two. Unlike a small-coefficient perturbation, no residual term is discarded: the rank hypothesis is used only to identify the exact two-dimensional residual support, after which the full quadratic is retained in the `3 x 3` core.

The surviving B11 branch is therefore sharper:

`QFORM-PUNCTURED-ULTRACOLOOP-RESIDUAL-RANK3-v1`:

> retain a genuinely rank-three complementary residual block together with the nonzero physical hub pivot and the small same-bank longitudinal puncture; either find a source-disjoint third smoothing packet or prove a dependence-safe receiver that remains uniform as the puncture tends to zero.

This is the regime in which the kernel direction of the rank-three spectral carrier has a nonzero physical-hub component, so it cannot be removed by a light-only deterministic change of coordinates without mixing the literal independent hub with its product leaf source.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate full-target bridge.

## 5. Designated fleet02/B11 result applied to an actual inequality

The freshest completed designated-partner result is fleet02/B11 r11:

- `yspennstate/math-open-problems@0df11ae7802a2f4cdbb07feaaef3dc443db588bf`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260924T031028Z-fleet02-B11-QFORM-r11/REPORT.md`,
- theorem `QFORM-SHARP-MIXED-FRAME-OPPOSITESIGN-CLOSURE-v1`.

For arbitrary independent cap-one `H,X_1,X_2,X_3,X_4`, put

`L=(X_1-X_3)/sqrt(2)`,
`P=(X_1+X_3)/sqrt(2)`,
`S=(X_2+X_4)/sqrt(2)`,

and

`Q_theta=theta H^2+2sqrt(2)HL+2P^2+4LS`.

The partner theorem conditions only on ORIGINAL coordinates `(H,X_4)` and reduces the remaining law to the zero-pivot scalar-plus-curved-pair trace

`2sqrt(2)YU+2V^2`,

with scalar cap one, pair cap one, and determinant magnitude four. It proves the actual full-line inequality

`boxed: ||p_(Q_theta)||_(infinity,ess) <=3 for every theta in R.`

Its deterministic carrier has at least three eigenvalues of modulus at least two for every `theta`, so this is a genuine target family in the nonzero-pivot regime. This application is retained as the designated-partner inequality for the present run; it also shows that an arbitrary hub-square coefficient can be harmless when a source-valid zero-pivot trace is exposed after conditioning.

## 6. Rank-two logarithmic control and the third direction

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`.

Thus a single opposite-sign hyperbolic pair is genuinely unbounded.

The new low-residual-rank theorem identifies how the third direction removes this singularity in its scope without invoking spectral-coordinate independence: the entire physical quadratic lives on

`literal independent hub H + one two-dimensional product projection Y`.

The compressed `3 x 3` Hessian has the exact three nonzero eigenvalues of `A`, so its third curvature is genuine. The coarea receiver spends all three curvatures when the hub pivot is subcritical; the scalar-pivot/half-Riesz receiver spends the hub square together with the exact rank-two residual determinant when the pivot is larger. Rank two lacks this third nonzero curvature and the logarithmic example remains untouched.

## 7. Verification

A deterministic numerical checker was run on 2,000 randomly generated exact-rank-three examples covering both structural cases in Lemma 2.1:

- `rank C=1`, `l notin Ran(C)`;
- `rank C=2`, `l in Ran(C)` with nonzero Schur scalar.

There were zero rank failures. The maximum absolute discrepancy between the three nonzero eigenvalues of the ambient matrix and the eigenvalues of the compressed `3 x 3` core was `6.22e-15`.

The constants were also checked directly:

`G0=10.836259466936783...`,
`B(0.848,2)=132.97278587755545...`,
`128*(0.848)^(-1/4)=133.38623266130324...`.

Thus the rounded theorem constant `134` is safe.

## 8. Integrity / status

This is a supporting theorem, not a proof of the full owner target. It closes a precise arbitrary-pivot exact-rank-three branch and does not claim that every current punctured near-coloop survivor has residual rank at most two.

Continuity is not proved by Theorem 3.1. The freshest owner claims still list full QFORM and full continuity as OPEN.
