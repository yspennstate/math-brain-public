SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-24T07:40:41Z.
attacking: the nonzero-pivot volume-one LDL two-sheet collar by separating its finite and escaping physical-H roots, and stress-testing the predecessor two-Jacobian budget against the partner's exact dependent-shell obstruction.

# fleet01/B11 — LDL sheet separation and a sharp two-Jacobian obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260924T074041Z-fleet01-B11-QFORM-auto11`.
Owner control: revision `2026-09-22.15`; programme control revision `2026-09-22.5`.
Publication-refresh brain main: `650c69a0756911a61c48cdcf30a9be26bb3dc471`.
Status: **NEW EXACT ROOT-SHEET IDENTITY / NEW SOURCE-SCOPE CORRECTION / DESIGNATED fleet02/B11 RESULT APPLIED / FULL QFORM OPEN**.
Regularity: neither new statement proves continuity for the remaining LDL branch; the full continuous-density conclusion remains open.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, law-uniform pointwise van-der-Corput estimate, arbitrary-joint coarea theorem, or worst-fiber density principle is used.

## 1. Fresh source boundary


The immediate own predecessor is

- `yspennstate/math-open-problems@0d074396abdd021a817f0b8dc104b826f2d7154d` (same report content already visible at the earlier source pin `df6d00a11422f16763e8bccccc6bada6e4949a83`),
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260924T064232Z-fleet01-B11-QFORM-auto11/REPORT.md`,
- theorem `QFORM-LDL-FULL-TWOJACOBIAN-NONZERO-v1`.

It proves in the nonzero-pivot volume-one LDL normal form

`J_2(Y,Q)=2 sqrt(a^2 U^2+d^2 V^2)`,

`P{J_2<=tau}<=min(1,pi tau^2/(2s^2))`,

and, for `0<p<2`,

`E J_2^{-p} <= [2^(1-p)/(2-p)](2pi)^(p/2)s^{-p}`.

Those are integrated transversality statements, not a density theorem.

The exact structural input remains fleet03/B11 r50, theorem `QFORM-PUNCTURED-VOLUME1-LDL-v1`, at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T051120Z-fleet03-B11-QFORM-r50/REPORT.md`.

The designated partner result consumed below is fleet02/B11 r13,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260924T055712Z-fleet02-B11-QFORM-r13/REPORT.md`,

theorem `QFORM-LDL-MARGINAL-CAPS-SUFFICIENT-FALSE-v1`.

A fresh repository search before this write found the predecessor warning that a reciprocal two-Jacobian moment does not by itself control fiber mass, but no source-matching quantitative theorem below showing that **all negative two-Jacobian moments may tend to zero while the output density tends to infinity**.

## 2. The live r50 normal form

Let

`A=R M R^T`, `R^T R=I_3`,

with `M` symmetric invertible and

`s=min_j |lambda_j(M)|>0`.

Fix an ORIGINAL physical hub coordinate `h` of leverage `q in (0,1)`. In the r50 deterministic spectral bookkeeping basis,

`M=[[a,r,0],
    [r,b,c],
    [0,c,d]]`,                                                   (2.1)

and, for the ORIGINAL independent input `H=X_h` and residual linear forms `(T,Y,W)`,

`Q=a(sqrt(q)H+T)^2
  +2r(sqrt(q)H+T)Y
  +bY^2+2cYW+dW^2`.                                             (2.2)

Only `H` is literally source-separated from the residual product bank. No independence among `(T,Y,W)` is asserted.

For `a d !=0`, r50 completes squares via

`U=sqrt(q)H+T+(r/a)Y`,
`V=W+(c/d)Y`,
`gamma=det(M)/(a d)`,

so

`Q=aU^2+gamma Y^2+dV^2`,                                       (2.3)

and the coefficient vectors of `(U,Y,V)` have determinant-one Gram volume.

## 3. New exact theorem: conditional discriminant cancellation and root-sheet split

### Theorem `QFORM-LDL-PHYSICAL-ROOT-SPLIT-v1`

Fix a target value `zeta`. Regard (2.2) as a quadratic equation in the genuine ORIGINAL scalar `H`, conditionally on the residual source. Its discriminant divided by `4q` is

`D_zeta(Y,W)
 =(r^2-ab)Y^2-2acYW-adW^2+a zeta`.                              (3.1)

In particular, **the residual coordinate `T` cancels identically from the discriminant**.

The quadratic part of `D_zeta` in `(Y,W)` is

`K_a=[[r^2-ab,-ac],
      [-ac,-ad]]`,                                               (3.2)

and satisfies the exact determinant identity

`boxed: det K_a = a det M.`                                     (3.3)

Whenever `D_zeta>=0`, the two physical-H roots are

`H_+ = -T/sqrt(q)+[-rY+sqrt(D_zeta)]/(a sqrt(q))`,
`H_- = -T/sqrt(q)+[-rY-sqrt(D_zeta)]/(a sqrt(q))`.               (3.4)

For `rY!=0`, set `sigma=sgn(rY)`. Relabel these roots as

`H_fin=-T/sqrt(q)+[-rY+sigma sqrt(D_zeta)]/(a sqrt(q))`,
`H_far=-T/sqrt(q)+[-rY-sigma sqrt(D_zeta)]/(a sqrt(q))`.         (3.5)

Then the finite root has the exact rationalized form

`boxed:
 H_fin=-T/sqrt(q)
       +[zeta-bY^2-2cYW-dW^2]
        /[sqrt(q)(rY+sigma sqrt(D_zeta))].
`                                                                    (3.6)

The far root is

`boxed:
 H_far=-T/sqrt(q)
       -[rY+sigma sqrt(D_zeta)]/(a sqrt(q)).
`                                                                    (3.7)

Because `sigma sqrt(D_zeta)` has the same sign as `rY`,

`|rY+sigma sqrt(D_zeta)|=|rY|+sqrt(D_zeta)`.                     (3.8)

Consequently

`|H_fin+T/sqrt(q)|
 <= |zeta-bY^2-2cYW-dW^2|/(sqrt(q)|rY|)`,                        (3.9)

and

`|H_far+T/sqrt(q)|
 >= |rY|/(|a|sqrt(q)).`                                         (3.10)

Finally, for every fixed `(T,Y,W,zeta)` with `rY!=0`, as `a->0` through values for which the live r50 representation is defined,

`H_fin -> -T/sqrt(q)
          +[zeta-bY^2-2cYW-dW^2]/(2r sqrt(q)Y)`,                 (3.11)

which is exactly the unique physical-H root of the **null-pivot** equation obtained from (2.2) by setting `a=0`; while

`H_far = -T/sqrt(q)-2rY/(a sqrt(q))+o(a^{-1})`.                  (3.12)

#### Proof

Expanding (2.2)-`zeta` as a polynomial in `H` gives

`a q H^2 +2 sqrt(q)(aT+rY)H
 +[aT^2+2rTY+bY^2+2cYW+dW^2-zeta]`.

Therefore the discriminant divided by four is

`q[(aT+rY)^2
   -a(aT^2+2rTY+bY^2+2cYW+dW^2-zeta)]`,

and the `a^2T^2` and `2arTY` terms cancel, yielding `q D_zeta` and (3.1).

A direct two-by-two determinant calculation gives

`det K_a
 =(r^2-ab)(-ad)-a^2c^2
 =a[abd-ac^2-r^2d]
 =a det M`,

proving (3.3). Formula (3.4) is the quadratic formula. For the branch selected in (3.5), multiply

`(-rY+sigma sqrt(D_zeta))(rY+sigma sqrt(D_zeta))
 =D_zeta-r^2Y^2
 =a[zeta-bY^2-2cYW-dW^2]`.

Division by `a sqrt(q)` gives (3.6); (3.7)-(3.10) are immediate. At fixed nonzero `rY`, `D_zeta->r^2Y^2`, so `sigma sqrt(D_zeta)->rY`; (3.11)-(3.12) follow. QED.

### Meaning for the puncture

The `a^{-1/4}` loss in the predecessor determinant-only half-Riesz estimate does not mean both physical sheets become singular. Algebraically one sheet converges exactly to the already-understood null-pivot root; the other sheet is forced to escape in the ORIGINAL `H` coordinate at rate at least `|rY|/(|a|sqrt(q))` away from the merge collar `Y≈0`.

This is not yet a density theorem because the admissible one-dimensional input density of `H` may place unit-height fragments arbitrarily far away. Mere root distance cannot be converted to probability decay without an illicit moment/tail assumption. The exact product factorization must therefore be used jointly with the far sheet and the `Y≈0` merger collar.

## 4. New correction: even arbitrarily strong two-Jacobian transversality is insufficient after product provenance is forgotten

### Theorem `QFORM-TWOJACOBIAN-TRANSVERSALITY-ONLY-FALSE-v1`

For every `0<epsilon<1`, `0<delta<=1`, and `R>=2`, the fleet02/B11 r13 shell construction supplies an **arbitrary dependent** probability density `rho` on `(U,Y,V)` with

`||rho||_infinity=1`,
`||p_(Y,V)||_infinity <= delta/(2R sqrt(epsilon))`,
`||p_U||_infinity <= sqrt(epsilon) delta/(2R)`,                  (4.1)

such that for

`F_epsilon(U,Y,V)=epsilon U^2-epsilon^(-1)Y^2+V^2`,              (4.2)

its output density obeys

`p_(F_epsilon)(s)>=sqrt(2/3)/delta`, `-delta<=s<=0`.              (4.3)

Let

`G(U,Y,V)=(Y,F_epsilon(U,Y,V))`.

On the support of the same shell,

`boxed: J_2 G >= 2 sqrt(epsilon) R.`                             (4.4)

Hence, for **every** `p>0`,

`boxed: E (J_2 G)^(-p) <= (2 sqrt(epsilon)R)^(-p),`              (4.5)

and

`P{J_2G<=tau}=0` for every `tau<2 sqrt(epsilon)R`.               (4.6)

Thus no theorem for arbitrary dependent three-dimensional laws can bound the quadratic output density using only a joint density cap, pair/scalar marginal caps, and even arbitrarily strong lower-tail or negative-moment control of the full two-Jacobian.

#### Proof

The partner shell is obtained from variables `(x,v,z)` by

`x=sqrt(epsilon)U`, `v=V`, `z=Y/sqrt(epsilon)`,

and its support satisfies `x>=R`. For (4.2),

`grad Y=(0,1,0)`,
`grad F_epsilon=(2epsilon U,-2epsilon^(-1)Y,2V)`.

Therefore

`J_2G=|grad Y wedge grad F_epsilon|
    =2 sqrt(epsilon^2U^2+V^2)
    =2 sqrt(epsilon x^2+v^2)
    >=2 sqrt(epsilon)R`,

which proves (4.4)-(4.6). The output lower bound and marginal caps are exactly the completed fleet02/B11 r13 theorem. QED.

### Quantitative specialization

Take

`epsilon=1/4`, `R=2 delta^(-2)`, `0<delta<=1`.

Then

`||rho||_infinity=1`,
`||p_(Y,V)||_infinity <= delta^3/2`,
`||p_U||_infinity <= delta^3/8`,                                (4.7)

while

`J_2G>=2 delta^(-2)`,
`E(J_2G)^(-p) <= (delta^2/2)^p` for every `p>0`,                 (4.8)

but still

`boxed: ||p_(F_epsilon)||_infinity
        >=sqrt(2/3) delta^(-1) -> infinity.`                    (4.9)

So the bad output can coexist not merely with a bounded reciprocal-Jacobian moment, but with reciprocal-Jacobian moments tending to zero at every fixed order and with pair/scalar caps tending to zero.

### Scope warning

This is **not a counterexample to QFORM**. The partner shell is an arbitrary dependent density and is not asserted to be a linear projection of independent cap-one original coordinates. The theorem instead makes the live proof requirement sharper: product provenance is not a technical decoration; it is the only remaining resource that can distinguish the true LDL law from this transversality-perfect fake.

## 5. Mandatory rank-two control and the third direction

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                        (5.1)

so the opposite-sign rank-two saddle is genuinely unbounded.

The predecessor theorem identified the geometric third-direction gain in the true punctured LDL law:

`J_2(Y,Q)=2 sqrt(a^2U^2+d^2V^2)`,                               (5.2)

which converts the one-dimensional reciprocal singularity into a codimension-two planar Riesz kernel and gives a puncture-uniform negative-moment budget. The new correction shows exactly what this gain does **not** prove: codimension-two transversality alone does not control the length/mass of two-sheet fibers. The true third-direction repair must combine (5.2) with the ORIGINAL-coordinate product factorization before taking absolute fiber envelopes.

The new root split (3.6)-(3.12) further localizes where that factorization is needed: the finite sheet has the exact null-pivot limit, while the far sheet and the `Y≈0` merger collar carry the genuinely punctured difficulty.

## 6. First unpaid B11 implication

The first unpaid implication is now refined to

`QFORM-LDL-FAR-SHEET-PRODUCT-FACTOR-v1`:

> In the r50 exact-rank-three majority-sign volume-one LDL collar, use the exact ORIGINAL-coordinate product characteristic-function/fiber factorization to control the contribution of the escaping physical-H root (3.7) jointly with the merger collar `Y≈0`, while using the finite-root identity (3.6) to connect the other sheet to the completed null-pivot receiver. No proof may replace the projected product law by joint/pair/scalar caps or by any finite collection of two-Jacobian negative moments, because Theorem 4 rules that interface out.

A successful estimate must be uniform through `a->0`, retain every nonzero coefficient, and preserve arbitrary fragmented cap-one input laws. Separately unpaid: arbitrary additional nonseparable spectrum beyond exact rank three, and the full continuity conclusion.

## 7. Verification

A deterministic 20,000-case floating regression checked the conditional-discriminant cancellation, `det K_a=a det M`, and the rationalized finite-root identity. Maximum observed errors were

`max_discriminant_error = 1.7763568394002505e-14`,
`max_det_error          = 7.105427357601002e-15`,
`max_finite_root_error  = 1.5987211554602254e-14`,

with 13,030 random cases falling in the real-root / `rY!=0` branch used for the root comparison. The identities themselves are proved algebraically above; this regression is only a check.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
Full-target continuity: **OPEN**.
