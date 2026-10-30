SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B01, 2026-09-22T18:08:07Z.
attacking: refute or prove the owner-proposed conditional three-dimensional projection-density moment, then splice the surviving oscillatory replacement into the newest O0 heavy-packet collar.

# fleet01/B01 — conditional-density moment obstruction and rank-three cross-collar payment

**Run:** `20260922T180807Z-b01-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Final control intended for publication refresh:** owner revision `2026-09-22.10`; exact refreshed commit recorded in the handoff/receipt.  
**Assignment:** Oscillatory replacement.  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL TARGET OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and source state

The full target remains open: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal essential-supremum bound, or produce a valid counterexample. Continuity is a separate desired conclusion.

This run preserves all current corrections: no law-uniform pointwise quadratic-phase decay, no rotation-based independence, no raw fiber-supremum argument, no conditional-cap-as-independence surrogate, and no claim that a single small minor must be uniformly good.

The current owner message proposes, as a possible route for the full-rank case, bounding

`E_Z ||rho_{Y|Z}||_infinity^(2/3)`

uniformly when `Y` is the three-dimensional large-eigenspace projection and `Z` is the orthogonal complement. The first theorem below shows this intermediate statement is false even for an exact-rank-three target matrix and iid uniform physical coordinates. The failure is quantitative: the moment grows linearly with block size.

The second theorem applies the already completed B01 random-slope Plancherel estimate to fleet03/B07's newest six-coordinate O0 collar. It closes that collar with a continuous-density bound `<19.05`. The live `QFORM-CROSSMINOR-ALONE-FALSE` event is not violated: that correction concerns the curved **2x2** cross-block claim, whereas the random-slope theorem has an integrable threshold only at cross dimension three.

## 2. A target-valid family

Fix an integer `m>=2` and set `n=3m`. Partition the physical coordinates into three disjoint blocks `B_1,B_2,B_3`, each of size `m`, and take all `X_i` iid `Uniform[-1/2,1/2]`.

For `b=1,2,3`, let

`u_b = m^(-1/2) 1_{B_b}`

and define

`A_m = u_1u_1^T + u_2u_2^T - u_3u_3^T`.

Then `A_m` has exactly the three nonzero eigenvalues `1,1,-1`. Put

`Y_b=<u_b,X>`.

The target quadratic form is

`Q_m=Y_1^2+Y_2^2-Y_3^2`.

The three random variables `Y_b` are independent because they use disjoint physical coordinate blocks.

## 3. Exact conditional-fiber geometry inside one block

Consider one block of `m` coordinates. Let

`u=m^(-1/2)(1,...,1)`,
`Y=<u,X>`,
`Z=X-Yu`,

so `Z` lies in the mean-zero hyperplane `u^perp`. Orthogonal change of variables preserves Lebesgue measure, and the transformed cube density is still the indicator of a rotated cube.

For fixed `z in u^perp`, the fiber line `z+yu` intersects `[-1/2,1/2]^m` in an interval. The coordinate constraints are

`-1/2 <= z_i + y/sqrt(m) <= 1/2`,

so the allowed `y`-interval has exact length

`L(z)=sqrt(m) [1-(max_i z_i-min_i z_i)]`.

On every nonempty fiber, the conditional law of `Y` given `Z=z` is uniform on that interval. Hence

`||rho_{Y|Z=z}||_infinity = 1/L(z)`.

If `X` itself is uniform on the cube, subtracting the block mean does not change the coordinate range, so

`max_i Z_i-min_i Z_i = max_i X_i-min_i X_i`.

Let `R=max_i X_i-min_i X_i`. For `m` iid uniforms on an interval of length one,

`f_R(r)=m(m-1) r^(m-2)(1-r), 0<r<1`.

Therefore

`E L(Z)^(-2/3)`
`= m^(-1/3) E(1-R)^(-2/3)`
`= m^(-1/3) m(m-1) B(4/3,m-1)`
`= m^(-1/3) Gamma(m+1) Gamma(4/3) / Gamma(m+1/3).`          (3.1)

By the standard gamma-ratio asymptotic,

`Gamma(m+1)/Gamma(m+1/3) ~ m^(2/3)`,

so

`E L(Z)^(-2/3) ~ Gamma(4/3) m^(1/3)`.                        (3.2)

## 4. Refutation of the proposed conditional 3-D moment bound

Apply the preceding block decomposition independently in the three blocks. Write

`Y=(Y_1,Y_2,Y_3)`, `Z=(Z_1,Z_2,Z_3)`.

Because the three blocks are independent, conditional on `Z` the three `Y_b` are independent uniforms on intervals of lengths `L_b=L(Z_b)`. Hence

`||rho_{Y|Z}||_infinity = (L_1L_2L_3)^(-1)`.

Consequently

`M_m := E_Z ||rho_{Y|Z}||_infinity^(2/3)`
`= [E L(Z)^(-2/3)]^3`
`= Gamma(4/3)^3 Gamma(m+1)^3 / [m Gamma(m+1/3)^3].`           (4.1)

In particular,

`boxed( M_m ~ Gamma(4/3)^3 m )`,

with

`Gamma(4/3)^3 = 0.7120729426887296...`.

Thus

`sup_m E_Z ||rho_{Y|Z}||_infinity^(2/3) = infinity`.           (4.2)

This is an exact counterexample to the proposed **intermediate conditional-moment bound**. It is not a counterexample to QFORM: `A_m` itself is exact rank three and the target output remains uniformly bounded.

The mechanism of failure is transparent. Normalizing each thin physical fiber before applying the rank-three coarea theorem costs the reciprocal fiber volume. The `2/3` exponent is not enough to make that normalization integrable uniformly over high-dimensional complements. Product aggregation must occur before, or jointly with, the curved trace.

### 4.1 The output law is nevertheless uniformly bounded

For completeness, each normalized block sum `Y_b=m^(-1/2) sum_{i in B_b} X_i` is a one-dimensional orthogonal projection of the unit cube. The standard one-dimensional cube-slicing bound gives

`||p_{Y_b}||_infinity <= sqrt(2)`.

If a real random variable `W` has density at most `K`, then `W^2` has density at most `K y^(-1/2)` on `y>0`. Therefore the two independent same-sign terms `Y_1^2,Y_2^2` have convolution density at most

`2 * B(1/2,1/2) = 2 pi`.

Convolution with the independent law of `-Y_3^2` cannot increase `L^infinity`, so

`||p_{Q_m}||_infinity <= 2 pi`                                           (4.3)

for every `m`. Thus the conditional moment in (4.1) diverges linearly while the actual quadratic-form density stays uniformly bounded.

## 5. Application of the designated partner fleet02/B01 result

The newest completed designated-partner theorem is fleet02/B01 r25, canonical

`yspennstate/math-open-problems@bf4ba08b75ab774aef671c62ba4898a371059c0d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T170850Z-fleet02-B01-qform-r25/REPORT.md`.

It proves that every invertible physical principal `3x3` block `B` gives

`||p_Q||_infinity <=216 |det B|^(-1/3)`                                (5.1)

with arbitrary affine leakage from outside coordinates retained.

For the family `A_m`, every nonsingular physical principal triple contains exactly one coordinate from each block and has

`|det A_m[I,I]| = m^(-3)`.

Thus the partner theorem gives the actual inequality

`||p_{Q_m}||_infinity <=216 m`.                                        (5.2)

Comparison with (4.3) is informative: the local principal-triple theorem is correct, but this diffuse rank-three family makes every physical principal determinant shrink like `m^-3`, so local triple selection alone loses a factor `m`. The same scale appears in the false normalized conditional-moment route (4.1). This is direct evidence that the missing full-target mechanism must aggregate coordinate mass before reciprocal local determinant/fiber payment.

## 6. New synthesis: fleet03/B07's six-coordinate collar is already paid

The newest completed fleet03/B07 theorem is canonical

`yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T173711Z-fleet03-B07-qform-r13/REPORT.md`.

In its O0 branch, when both the row packet and transpose packet are sufficiently localized, it produces disjoint physical triples `H subset L`, `T subset R` with

`|det A[H,T]| >= 1/256`.                                               (6.1)

That report leaves this as an unpaid six-coordinate collar because it conservatively cites `QFORM-CROSSMINOR-ALONE-FALSE`.

However B01's earlier completed random-slope theorem, canonical

`yspennstate/math-open-problems@508b0985ba8bb658a7f6a935af5138a195cb89de`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T124907Z-b01-qform-auto11/REPORT.md`,

proves for every disjoint `k x k` physical cross block `C=A[I,J]`, with arbitrary self blocks and outside couplings,

`|phi_Q(t)| <= min(1, pi^(k/2)|det C|^(-1/2)|t|^(-k/2))`,              (6.2)

and therefore for `k>=3`,

`||p_Q||_infinity <= [k/(k-2)] |det C|^(-1/k)`.                       (6.3)

For `k=3`, inserting (6.1) gives

`boxed( ||p_Q||_infinity <= 3 * 256^(1/3) < 19.049 )`.                (6.4)

Moreover (6.2) is integrable, so this collar branch has a **continuous density vanishing at infinity**.

This does not conflict with the correction `QFORM-CROSSMINOR-ALONE-FALSE`: that event refutes the analogous curved `2x2` claim, where random-slope Plancherel gives only the borderline tail `|t|^-1`. At cross dimension three the tail is `|t|^-3/2` and is integrable.

Thus the B07 branch

`three 3/4-heavy rows + at least three 11/16-heavy transpose coordinates`

is no longer unpaid. It closes directly by (6.4).

### 6.1 Combined partner/cross-packet certificate on the same collar

On any such disjoint collar `(H,T)`, fleet02/B01 r25 and B01 random-slope Plancherel give the simultaneous valid estimate

`||p_Q||_infinity <= min{`
`  3 |det A[H,T]|^(-1/3),`
`  216 |det A[H,H]|^(-1/3)  if det A[H,H]!=0,`
`  216 |det A[T,T]|^(-1/3)  if det A[T,T]!=0`
`}`.                                                                      (6.5)

The cross term supplies the universal `<19.049` bound in B07's collar; the partner terms can only improve it when a self-block determinant is very large.

## 7. Updated first unpaid implication

Two points should be propagated to proof assembly.

1. **Delete the normalized conditional-density-moment route.** The bound

   `E ||rho_{Y|Z}||_infinity^(2/3) <= C`

   is false, even for iid cube inputs and an exact-rank-three matrix with spectrum `{1,1,-1}`. Any coarea/fiber proof must keep the unnormalized product slice and integrate the complement before or jointly with the curved trace.

2. **Delete the six-coordinate 3x3 cross-collar from the unpaid O0 list.** Fleet03/B07's collar (6.1) is paid by B01 random-slope Plancherel with the continuous-density constant `<19.049`.

The O0 residue is therefore narrower: one/two heavy coordinates on at least one side of the effective-dimension-three packet, with aggregate third-volume still retained. O1/O2/O3 overlap classes also remain to be paid globally. The full QFORM conjecture remains open.

## 8. Verification

The exact formula (4.1) was checked numerically against direct beta/gamma evaluation for `m=2,3,5,10,20,50,100,500`. The ratio `M_m/m` decreases toward `Gamma(4/3)^3=0.7120729426887296...`; at `m=500`, `M_m=356.27393448431...`.

The B07 collar constant is

`3*256^(1/3)=19.048812623618392...`.

A compact checker and captured output are saved beside this report. Numerical checks are regression evidence only; the proofs above are exact.

## 9. Status

- `QFORM-CONDITIONAL-3D-CAP-MOMENT-UNIFORM-v1`: **REFUTED** by (4.1)-(4.2).
- `QFORM-O0-THREE-BY-THREE-CROSS-COLLAR-PAYMENT-v1`: **PROVED**, continuous density `<19.049` under B07's collar.
- Full QFORM: **OPEN**.
- Full continuity: **OPEN**.
