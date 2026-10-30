SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-24T06:42:32Z.
attacking: the nonzero-pivot volume-one LDL two-sheet collar; aggregate the full two-Jacobian in a source-valid way and show that the small physical pivot is exactly compensated by the shear volume.

# fleet01/B11 — nonzero-pivot LDL full two-Jacobian currency

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260924T064232Z-fleet01-B11-QFORM-auto11`.
Owner control: revision `2026-09-22.15`; programme control revision `2026-09-22.5`.
Status: **NEW EXACT STRUCTURAL THEOREM / PUNCTURE-UNIFORM NEGATIVE-JACOBIAN BUDGET / DESIGNATED fleet02/B11 RESULT APPLIED / FULL QFORM OPEN**.
Regularity: the new theorem is an integrated Jacobian/small-Jacobian statement; it does **not** by itself prove an essential density bound or continuity on the remaining two-sheet branch.

The unrestricted owner target remains OPEN. No Gaussian, log-concavity, moment, bounded-support, connected-support, iid, spectral-coordinate independence, conditional projection cap as independence, arbitrary-joint coarea theorem, pointwise law-uniform van-der-Corput decay, or perturbative deletion of a small coefficient is used.

## 1. Fresh source boundary

Fresh `math-research-brain/main` was resolved during this run. The live `CLAIMS.json` still marks `QFORM-FULL` and the full continuous-representative claim OPEN. The historical source owner message was also read at the exact owner-supplied commit `0dc369ddf8b860648dd780d8f92c62994dc53ecf`; later control wins and leaves QFORM as the sole target.

The immediate own predecessor is

- `yspennstate/math-open-problems@<master source before this run>`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260924T031514Z-fleet01-B11-QFORM-auto11/REPORT.md`;
- theorem `QFORM-ARBITRARY-PIVOT-LOWRESIDUAL-RANK-v1`, which pays every exact-rank-three branch with a literal physical hub whose complementary principal block has rank at most two, by `<134/s`.

Thus the live exact-rank-three B11 debt is the genuinely rank-three complementary residual / ultra-coloop collar.

The structural input consumed in full is fleet03/B11 r50:

- report-introducing source `yspennstate/math-open-problems@85cef4be19e5e356fa4e4feff11b250e0c2fe0ed`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T051120Z-fleet03-B11-QFORM-r50/REPORT.md`;
- theorem `QFORM-PUNCTURED-VOLUME1-LDL-v1`.

Its exact nonzero-pivot normal form is recalled below. A fresh repository search before publication found no source-matching statement of the new nonzero-pivot two-Jacobian identity proved here. The chronologically newer fleet03/B11 full-two-Jacobian theorem treats the exact **null-pivot** punctured normal form, not the LDL nonzero-pivot identity below; the two statements are complementary.

## 2. Source-valid LDL normal form

Write the exact-rank-three matrix as

`A = R M R^T`, `R^T R=I_3`,

with `M` symmetric invertible and

`s := min_j |lambda_j(M)| >0`.

Fix a literal ORIGINAL physical coordinate `h` of leverage `q in (0,1)`. In deterministic spectral bookkeeping coordinates the r50 form is

`M = [[a,r,0],
      [r,b,c],
      [0,c,d]],`                                                   (2.1)

and the residual source has mutually orthogonal coefficient vectors `t,y,w` with

`||t||^2=1-q`, `||y||=||w||=1`.

Put

`H=X_h`, `T=t.X_-`, `Y=y.X_-`, `W=w.X_-`.

Only `H` is literally source-separated from the residual product bank; no independence among `(T,Y,W)` is asserted. The quadratic is

`Q=a(sqrt(q)H+T)^2+2r(sqrt(q)H+T)Y+bY^2+2cYW+dW^2`.             (2.2)

Assume `a d !=0`, as in the punctured r50 branch. Define

`Z=sqrt(q)H+T`,
`U=Z+(r/a)Y`,
`V=W+(c/d)Y`,
`gamma=det(M)/(a d)`.

Then r50 gives the exact identity

`Q=aU^2+gamma Y^2+dV^2`,                                          (2.3)

with `a gamma d=det M` and determinant-one three-volume for the coefficient vectors of `(U,Y,V)`.

For what follows it is useful to normalize the residual `t` direction. If `q<1`, put `t_0=t/sqrt(1-q)` and define the full physical coefficient vector

`z=sqrt(q)e_h+sqrt(1-q)t_0`.

At `q=1`, take `z=e_h`. In either case

`||z||=1`, `z perpendicular y,w`.

The coefficient vectors of `U,Y,V` are therefore

`u=z+(r/a)y`, `y`, `v=w+(c/d)y`.                                  (2.4)

This representation is purely deterministic coefficient geometry and does not rotate the product law.

## 3. New theorem: nonzero-pivot full two-Jacobian identity

### Theorem `QFORM-LDL-FULL-TWOJACOBIAN-NONZERO-v1`

Let

`F(X)=(Y(X),Q(X))`.

Then its Euclidean two-Jacobian satisfies the exact pointwise identity

`boxed: (J_2 F)^2 = 4[a^2 U^2+d^2 V^2]`,                            (3.1)

or equivalently

`boxed: J_2F=2 sqrt(a^2U^2+d^2V^2).`                               (3.2)

#### Proof

The gradient of the first component is the fixed unit vector `y`. From (2.3),

`grad Q = 2aU u + 2gamma Y y + 2dV v`.

Wedge with `y`. By (2.4),

`y wedge u = y wedge z`,
`y wedge v = y wedge w`.

Because `z,y,w` are orthonormal, the two exterior vectors `y wedge z` and `y wedge w` are orthonormal. Therefore

`|y wedge grad Q|^2
 =4a^2U^2 |y wedge z|^2 +4d^2V^2 |y wedge w|^2
 =4(a^2U^2+d^2V^2)`.

This is (3.1). QED.

The identity is noteworthy because the potentially huge shear coefficients `r/a` and `c/d` disappear from the polynomial expression for the Jacobian, while they reappear beneficially in the product-projection density cap below.

## 4. Exact shear-volume compensation

The coefficient parallelogram of `(U,V)` has area

`A_UV := sqrt(det Gram(u,v))`.

Using the orthonormal basis `(z,y,w)`,

`u=(1,r/a,0)`, `v=(0,c/d,1)`,

so

`boxed:
 A_UV = sqrt(1+(r/a)^2+(c/d)^2).
`                                                                    (4.1)

Consequently

`boxed:
 |ad| A_UV
 = sqrt(a^2d^2+r^2d^2+a^2c^2)
 = |M e_1 wedge M e_3|.
`                                                                    (4.2)

Since every singular value of `M` is at least `s`, the second exterior power satisfies

`boxed: |M e_1 wedge M e_3| >= s^2.`                               (4.3)

Thus

`boxed: |ad| A_UV >= s^2.`                                          (4.4)

This is the exact puncture compensation: as `a ->0`, the `U` coefficient shear `r/a` expands the source parallelogram at exactly the rate needed to keep the product `|ad| A_UV` bounded below by the two-curvature scale `s^2`.

## 5. Product-law small-Jacobian tail and all negative moments below order two

Because `(U,V)` is a rank-two linear image of the ORIGINAL independent cap-one product source, orthonormalize its two coefficient vectors and apply the completed two-dimensional product-projection theorem. Scaling back by the coefficient area gives

`||p_(U,V)||_infinity <= 2/A_UV.`                                  (5.1)

No independence between `U` and `V` is claimed.

The event `J_2F<=tau` is the ellipse

`a^2U^2+d^2V^2 <= tau^2/4`.

Its planar area is `pi tau^2/(4|ad|)`. Hence, using (5.1) and then (4.4),

`boxed:
 P{J_2F<=tau}
 <= min(1, pi tau^2/(2|ad|A_UV))
 <= min(1, pi tau^2/(2s^2)).
`                                                                    (5.2)

More generally, for every `0<p<2`, the capped-planar layer-cake estimate yields

`E (a^2U^2+d^2V^2)^(-p/2)
 <= [2/(2-p)] [pi ||p_(U,V)||_infinity/|ad|]^(p/2)`.

Since `J_2F=2 sqrt(a^2U^2+d^2V^2)`, (5.1) and (4.4) give

`boxed:
 E (J_2F)^(-p)
 <= [2^(1-p)/(2-p)] (2pi)^(p/2) s^(-p),
 0<p<2.
`                                                                    (5.3)

In particular

`boxed:
 E 1/J_2F <= sqrt(2pi)/s
 =2.5066282746310002.../s.
`                                                                    (5.4)

The estimate is uniform in the physical pivot, in the near-coloop leverage, and in the shear sizes. It remains finite as `a->0` inside the punctured branch.

### Scope warning

Equations (5.2)-(5.4) are **not** promoted to a density theorem. A reciprocal full-Jacobian moment does not by itself control fiber mass, and the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` / arbitrary-dependent-shell corrections forbid a dependence-blind coarea shortcut. The remaining step must use the original-coordinate product factorization before any worst-fiber envelope.

## 6. Partner fleet02/B11 applied at an actual inequality

The completed fleet02/B11 r12 endpoint theorem is

`QFORM-PURE-NULL-COLOOP-PAIRCAP-v1`,

source `yspennstate/math-open-problems@5117e9ec45221d02dfa74cedf6c4dcee9fae60c7`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260924T040707Z-fleet02-B11-QFORM-r12/R49_REFRESH.md`.

Apply it to the literal three-coordinate matrix

`M_+=[[0,1,0],[1,0,0],[0,0,1]]`,

whose nonzero spectrum is `{1,1,-1}` and whose first coordinate is a pure null coloop of leverage one. For **every** three independent cap-one inputs,

`boxed:
 ||p_(X^T M_+ X)||_(infinity,ess)
 <=3*2^(4/3)
 =7.559526299369239... .
`                                                                    (6.1)

Negating `M_+` gives the `(1,2)` signature with the same bound. This is an actual full-line target inequality in both indefinite signatures. It is not counted as new B11 progress here; it is a direct application of the designated partner theorem.

The chronologically newer fleet02/B11 r13 obstruction was also consumed. Its theorem `QFORM-LDL-MARGINAL-CAPS-SUFFICIENT-FALSE-v1` shows that even joint, pair and scalar density caps strictly better than the product-projection caps can coexist with arbitrarily large two-sheet output density for an **arbitrary dependent** LDL law. That construction is not a QFORM counterexample. It is precisely why (5.1), (5.2) or (5.4) alone cannot finish the present branch.

For example, setting the r13 parameters `epsilon=1/4`, `delta=1/100`, `R=10` gives its explicit dependent shell inequality

`p_F(s) >= sqrt(2/3)/delta >81.64`, `-0.01<=s<=0`,

while its coarse pair/scalar caps are tiny. This numerical specialization is only a mechanism obstruction, not a target counterexample.

## 7. Rank-two logarithmic control and the third direction

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`,                              (7.1)

so the opposite-sign rank-two saddle remains genuinely unbounded.

The new identity gives a source-valid geometric explanation for the third-direction repair in the nonzero-pivot LDL collar. If the third square is absent, the relevant two-Jacobian collapses to a one-dimensional factor proportional to `|U|`; reciprocal first moments can have the same logarithmic divergence as (7.1). With the third direction present,

`J_2F=2 sqrt(a^2U^2+d^2V^2)`,

so the singular set is codimension two in the authentic product projection `(U,V)`. The two-dimensional cap and exact exterior-area identity turn the reciprocal kernel into the locally integrable planar Riesz kernel, uniformly even when the physical pivot tends to zero.

This identifies the third direction without ever declaring LDL/eigen coordinates independent.

## 8. First unpaid implication

The live B11 implication is now

`QFORM-LDL-TWOJACOBIAN-TO-TWOSHEET-DENSITY-v1`:

> In the r50 volume-one LDL normal form, combine the puncture-uniform full two-Jacobian budget (5.2)-(5.4) with the exact original-coordinate product characteristic-function factorization to obtain a uniform opposite-two-sheet density bound, or force an already-paid physical-pair, cross-volume, pure-coloop, or low-residual-rank exit.

The fleet02/B11 r13 shell theorem proves that any argument which first forgets product provenance and retains only joint/pair/scalar density caps cannot close this implication. The next step must therefore be a factorization-aware coarea/Fourier argument, not another marginal-cap compiler.

Separately unpaid: passage from exact rank three to arbitrary additional nonseparable spectrum, and the full continuity conclusion.

## 9. Verification

A deterministic checker generated 20,000 random invertible symmetric `3x3` matrices, aligned the transverse bookkeeping so `M_13=0`, and checked:

1. the LDL identity (2.3);
2. the two-Jacobian identity (3.1);
3. `A_UV=sqrt(1+(r/a)^2+(c/d)^2)`;
4. `|ad|A_UV=|Me_1 wedge Me_3|`;
5. `|Me_1 wedge Me_3|/s^2 >=1`.

Recorded maximum discrepancies were

`max_factorization_error = 1.531219595563016e-12`,
`max_twojacobian_error = 8.526512829121202e-14`,
`max_area_identity_error = 7.275957614183426e-11`,
`min_exterior_ratio = 1.0264067401656531`.

The checker ends `QFORM_B11_LDL_TWOJACOBIAN_CHECK_PASS`.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
Full-target continuity: **OPEN**.
