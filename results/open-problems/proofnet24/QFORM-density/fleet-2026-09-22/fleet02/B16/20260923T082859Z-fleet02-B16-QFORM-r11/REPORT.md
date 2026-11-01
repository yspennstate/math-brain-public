SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T08:28:59Z.
attacking: a nonzero near-null semi-aligned coloop by keeping the original hub scalar inside the curved half-Riesz integral, rather than conditioning away its product provenance.

# fleet02/B16 r11 — nonzero near-null source-scalar / square transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Projection-product interaction / complementary source-valid constructions  
**Status:** NEW SUPPORTING THEOREM / FULL QFORM OPEN  
**Continuity:** not asserted globally; the theorem below proves an essential density bound.  

## 1. First unpaid implication and exact scope

The full target remains open: arbitrary independent original-coordinate densities `0<=f_i<=1`, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one.

The immediate designated-partner input is fleet03/B16 r26, canonical report

`yspennstate/math-open-problems@a398a1c2e6e97683e3fe594fa19476929a882be6`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T045948Z-fleet03-B16-QFORM-r26/REPORT.md`.

Its exact-rank-three reduction pays the non-coloop branch and leaves only a genuine near-coloop,

`c>63/64`,                                                        (1.1)

for the remaining B16 transition. The immediately preceding fleet02/B16 r27 then disproves a generic arbitrary-nonaligned slice-Wiener route, leaving `QFORM-NEAR-COLOOP-SEMI-ALIGNED-TRANSDUCER-v1` as the first local debt.

This report pays a real **nonzero-pivot** semi-aligned subclass of (1.1). The new point is uniformity as the pivot tends to zero while the weak leakage and the transverse projected coordinate may remain dependent. The still-unpaid generic case is where the final smoothing square shares the same original-coordinate bank as that dependent pair.

## 2. Main lemma: retain the source scalar through the curved kernel

### Theorem 2.1 — `QFORM-SEMI-ALIGNED-NEAR-NULL-SQUARE-TRANSDUCER-v1`

Let `(H,U)` be an arbitrary real random pair; no independence between `H` and `U` is assumed. Let `X,V` be real random variables such that

- `X`, `V`, and `(H,U)` are mutually independent as these three source objects;
- `X,U,V` have densities with caps

`||p_X||_infinity <= L_X`, `||p_U||_infinity <= L_U`, `||p_V||_infinity <= L_V`.

Let `gamma,k,beta` be nonzero, let `delta` be real with

`delta beta >= 0`,                                                (2.1)

and define

`Y=gamma X+H`,
`Q=delta Y^2+2k UY+beta V^2`.                                    (2.2)

Then `Q` is absolutely continuous and

`boxed: ||p_Q||_infinity <= 8 L_V sqrt( L_X L_U / |beta gamma k| ).`   (2.3)

At the exact-null endpoint `delta=0`, the constant improves from `8` to `4`:

`||p_Q||_infinity <= 4 L_V sqrt( L_X L_U / |beta gamma k| ).`       (2.4)

The estimates are uniform in the joint law of `(H,U)`, so in particular they do **not** require a conditional density bound for `U|H` and do not infer independence of projected coordinates.

### Proof

Reflect `Q` if necessary. Because `||p_Q||_infinity=||p_{-Q}||_infinity`, condition (2.1) lets us assume

`beta>0`, `delta>=0`.                                             (2.5)

The variable `Z=beta V^2` has a density `g_Z` satisfying

`g_Z(z) <= L_V /(sqrt(beta) sqrt(z)) 1_{z>0}`.                    (2.6)

Indeed, at the two roots `v=+-sqrt(z/beta)`, the Jacobian is `2 sqrt(beta z)` and each root density is at most `L_V`.

Since `V` is independent of `(X,H,U)`, writing

`W=delta Y^2+2kUY`,                                               (2.7)

convolution with (2.6) gives for almost every `s`

`p_Q(s) <= L_V beta^(-1/2) E[(s-W)_+^(-1/2)].`                   (2.8)

The whole issue is therefore to bound the one-sided half-Riesz integral **before** discarding the original scalar `X`.

Condition on `(H,U)=(h,u)`. The conditional law of

`Y=gamma X+h`

has a probability density `g_h` with the translation-uniform cap

`||g_h||_infinity <= L_Y:=L_X/|gamma|`.                           (2.9)

This is legitimate source conditioning: `X` is still an original independent scalar. No assertion is made about the conditional law of `U`.

Assume first `delta>0`. Put

`K_{s,u}(y)=(s-delta y^2-2kuy)_+^(-1/2)`.                         (2.10)

Completing the deterministic quadratic polynomial only for the purpose of measuring its level sets,

`s-delta y^2-2kuy
 = (delta s+k^2u^2)/delta
   -delta (y+ku/delta)^2.`                                       (2.11)

Write

`D=delta s+k^2u^2`.                                               (2.12)

If `D<=0`, the positive set in (2.10) is empty up to a null point. If `D>0`, then for every `lambda>0`, direct solution of `K_{s,u}(y)>lambda` gives

`|{y:K_{s,u}(y)>lambda}| <= 2 /( sqrt(D) lambda^2 ).`             (2.13)

To see this when `lambda^(-2)<D/delta`, subtract the two square roots at the ends of the two boundary layers; when `lambda^(-2)>=D/delta`, the whole interval has length `2sqrt(D)/delta`, which obeys the same upper bound. Thus (2.13) is valid for all `lambda>0`.

Using layer cake, the probability normalization of `g_h`, and the cap (2.9),

`int g_h(y) K_{s,u}(y) dy
 <= int_0^infinity min(1, 2L_Y/(sqrt(D) lambda^2)) d lambda
 = 2 sqrt(2L_Y) D^(-1/4).`                                      (2.14)

Now average only over the **unconditional marginal** of `U`. For any real `a` define

`F_a(u)=(a+k^2u^2)_+^(-1/4)`.                                   (2.15)

A second elementary level-set calculation yields, for every `lambda>0`,

`|{u:F_a(u)>lambda}| <= 2/(|k| lambda^2).`                       (2.16)

If `a>=0`, this is the centered interval estimate. If `a<0`, the superlevel set consists of two shells outside `|ku|=sqrt(-a)`, whose total length is

`2|k|^(-1)( sqrt(-a+lambda^(-4))-sqrt(-a) ) <=2/(|k|lambda^2).`

Since `p_U<=L_U`, layer cake again gives

`E F_a(U)
 <= int_0^infinity min(1,2L_U/(|k|lambda^2))d lambda
 =2 sqrt(2L_U/|k|).`                                             (2.17)

Take `a=delta s` in (2.14)-(2.17). The bound is uniform in `h`, so averaging the joint law of `(H,U)` is harmless and gives

`E[(s-W)_+^(-1/2)]
 <= 8 sqrt(L_Y L_U/|k|).`                                       (2.18)

Substituting `L_Y=L_X/|gamma|` into (2.8) proves (2.3).

For `delta=0`, fix `(h,u)` and apply the same layer-cake argument directly to the affine kernel

`(s-2ku(gamma x+h))_+^(-1/2)`.

Its superlevel set in `x` has length `lambda^(-2)/(2|k gamma u|)`, giving

`E_X[(s-2kU(gamma X+H))_+^(-1/2)|H,U]
 <= sqrt(2L_X/(|k gamma U|)).`                                  (2.19)

The cap `p_U<=L_U` implies the sharp bathtub estimate

`E|U|^(-1/2) <= 2sqrt(2L_U)`.                                   (2.20)

Equations (2.8), (2.19), and (2.20) give (2.4). QED.

### Why this is a product-provenance statement

A tempting proof would condition on the weak leakage `H` and demand a uniform conditional cap for `U|H`; that is invalid in the live correction state and is explicitly false in source-valid sum/difference models. Theorem 2.1 never does this. It conditions on `(H,U)` only after isolating the genuinely independent source scalar `X`, obtains a bound depending on `u` but not on `h`, and only then integrates against the unconditional marginal density of `U`.

Thus dependence inside the projected pair is retained all the way through the curved half-Riesz kernel.

## 3. A nonzero near-coloop target family paid uniformly

Fix even `m`, balanced signs `epsilon_j in {+1,-1}`, and `c in (0,1)`; write

`a=1-c`.                                                         (3.1)

Take arbitrary independent original-coordinate variables

`X_0,X_1,...,X_m,Z_1,...,Z_m`

with density caps at most one, and define

`T=m^(-1/2) sum_j X_j`,
`U=m^(-1/2) sum_j epsilon_j X_j`,
`V=m^(-1/2) sum_j Z_j`.                                         (3.2)

The variables `T` and `U` are two projections of the **same** leaf product bank and may be dependent. In contrast, `X_0`, the whole first leaf bank `(T,U)`, and `V` come from disjoint original-coordinate source objects.

Let `delta>=0`, put

`k_delta=sqrt(1+delta)`,                                        (3.3)

and set

`Q_{c,delta}
 = delta( sqrt(c)X_0+sqrt(a)T )^2
   +2 k_delta( sqrt(c)X_0+sqrt(a)T )U
   +V^2.`                                                        (3.4)

### 3.1 Exact target spectrum

Define physical frame rows

`r_0=(sqrt(c),0,0)`,
`r_j=(sqrt(a)/sqrt(m),epsilon_j/sqrt(m),0)`,
`r_{m+j}=(0,0,1/sqrt(m))`.                                      (3.5)

Balanced signs give `R^T R=I_3`. With

`B_delta=[[delta,k_delta,0],[k_delta,0,0],[0,0,1]]`,             (3.6)

we have exactly

`Q_{c,delta}=X^T R B_delta R^T X`.                              (3.7)

The eigenvalues of `B_delta` are

`boxed: {1+delta,-1,1}.`                                        (3.8)

Hence every `delta>=0` is a genuine three-large-eigenvalue target instance.

### 3.2 Uniform product-provenance bound across the nonzero pivot

The coefficient vectors defining `U` and `V` have Euclidean norm one. The source-valid one-dimensional Rogozin--Ball projection estimate therefore gives

`||p_U||_infinity <=sqrt(2)`,
`||p_V||_infinity <=sqrt(2)`.                                  (3.9)

Apply Theorem 2.1 with

`X=X_0`, `H=sqrt(a)T`, `gamma=sqrt(c)`,
`k=k_delta`, `beta=1`,
`L_X=1`, `L_U=L_V=sqrt(2)`.                                    (3.10)

No conditional law of `U` given `T` appears. We obtain

`boxed:
 ||p_{Q_{c,delta}}||_infinity
 <=2^(15/4) [c(1+delta)]^(-1/4).`                               (3.11)

In the designated-partner residual chamber `c>63/64`,

`||p_{Q_{c,delta}}||_infinity
 <2^(15/4)(64/63)^(1/4)
 =13.5074180044... .`                                           (3.12)

This is uniform as the physical pivot tends to zero through **nonzero** values `delta downarrow0`.

At the exact endpoint `delta=0`, the sharper part (2.4) gives

`||p_{Q_{c,0}}||_infinity
 <=2^(11/4)c^(-1/4)
 <6.7537090022...`                                               (3.13)

for `c>63/64`.

### 3.3 It lies arbitrarily deep in the physical no-pivot regime

The hub physical diagonal is

`A_00=c delta`.                                                  (3.14)

For a first-bank leaf `j`, direct two-by-two determinant calculation gives the exact identity

`det A_{ {0,j},{0,j} }=-c(1+delta)/m`.                           (3.15)

All first-bank physical diagonals are

`A_jj=[delta a+2sqrt(1+delta)sqrt(a) epsilon_j]/m`,              (3.16)

all second-bank diagonals are `1/m`, first-first pair determinants have modulus at most

`4a(1+delta)/m^2`,                                               (3.17)

and every remaining pair determinant is `O(delta/m)+O(m^(-2))` (indeed hub-second equals `c delta/m`, second-second is zero, and first-second is the product of the corresponding diagonals).

Consequently, for every fixed no-pivot threshold `tau>0`, choose `delta>0` sufficiently small and then even `m` sufficiently large. Every physical diagonal and every physical `2x2` principal determinant then has modulus below `tau`, while (3.8) remains exactly in the target spectral class and the density stays bounded by (3.12).

So (3.11) is not a localized-pivot result in disguise.

## 4. Required pinned-source result applied at an actual level-set inequality

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read at its `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` scopes. The completed result used here is Theorem C from `COUNTEREXAMPLE_SEARCH.md`: for a rank-three signature `(+, +, -)` product projection, the one-sheet side has the source-valid ruled-hyperboloid bound

`p_Q(s)<=pi sqrt(2)`                                              (4.1)

when all three spectral moduli are at least one. Its proof uses line integrals that are values of **two-dimensional marginals of the original product law**, bounded by the completed product-projection theorem; it does not make the three spectral coordinates independent.

Diagonalizing only the deterministic matrix `B_delta` in (3.6) gives signature

`(1+delta,1,-1)`.                                                (4.2)

Therefore the actual family (3.4) satisfies the sharper level-side estimate

`boxed: p_{Q_{c,delta}}(s)<=pi sqrt(2)=4.4428829381... for s>=0.` (4.3)

Together with (3.12), the only side needing the new semi-aligned transducer in this family is the two-sheet/minority-sign side `s<0`.

This is also an exact interface check: the pair

`(sqrt(c)X_0+sqrt(a)T, U)`                                      (4.4)

is an orthogonal two-dimensional projection of the original product law and consequently has a bounded joint density, but it is generally dependent. Theorem C can exploit its two-dimensional product marginals on the ruled side; Theorem 2.1 handles the opposite side by keeping the original scalar `X_0` until after the curved kernel is paid. Neither step invents projected independence.

## 5. Relation to the designated partner and what remains

Fleet03/B16 r26 proves its two-bank cocircuit theorem and reduces the exact-rank-three B16 residual to the genuine near-coloop (1.1). In the notation of that report, the present family has

`a=1-c<1/64`,                                                    (5.1)

so it lies precisely beyond the r26 `a>=1/64` cocircuit closure. Equations (3.14)-(3.17) additionally place it inside the nonzero no-pivot stress regime.

Theorem 2.1 therefore closes a **real nonzero near-coloop semi-aligned subclass** of the partner residual with a bound below `13.51`, uniformly through the null transition.

It does **not** close the generic partner chamber. The decisive hypothesis still used is that the smoothing square `V^2` comes from an original-coordinate bank independent of the source scalar `X` and the overlapping pair `(H,U)`. In a generic exact-rank-three near-coloop frame, the two transverse spectral directions can both be supported on the same leaf coordinates. The preceding r27 result shows that simply replacing this source separation by an arbitrary nonaligned slice-Wiener norm is false even under arbitrarily weak nonalignment.

The next unpaid implication is therefore

`QFORM-NEAR-COLOOP-OVERLAPPING-SQUARE-TRANSDUCER-v1`:

retain the original product factors when the smoothing transverse square and the hyperbolic projected coordinate share source coordinates, or prove a deterministic bank extraction that produces finitely many source-separated receivers of the form in Theorem 2.1 with uniform constants. The passage to arbitrary additional spectrum remains a separate full-target debt.

## 6. Source pins and integrity

Required pinned Claude/source package actually used:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`;
- `COUNTEREXAMPLE_SEARCH.md`, Theorem C, used in (4.3);
- `RESULTS.md` and `FOURIER_ROUTE_REPORT.md` reread for the live product/Fresnel scope and corrections.

Designated partner proof actually read and used:

- fleet03/B16 r26, `yspennstate/math-open-problems@a398a1c2e6e97683e3fe594fa19476929a882be6`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T045948Z-fleet03-B16-QFORM-r26/REPORT.md`.

Immediate own predecessor sharpening the current interface:

- fleet02/B16 r27, report commit `60079077a1035516fb0f88477c4eda71fbad8ca1`, proving the generic arbitrary-nonaligned slice-Wiener continuation false.

No moment, compact-support, log-concavity, post-rotation independence, worst conditional-density supremum, arbitrary-joint coarea theorem, or small-random-error deletion is used. The compact balanced-sign frame is only a deterministic target-class stress family; the input laws in (3.4) remain arbitrary independent cap-one densities.

**FULL TARGET CHANGE: NONE.** The unrestricted conjecture remains open.
