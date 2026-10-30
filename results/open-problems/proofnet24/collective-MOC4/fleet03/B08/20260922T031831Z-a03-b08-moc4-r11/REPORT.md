# MOC4 fleet03/B08 — one-cycle SU(2) ellipse/payment reduction

Run: `20260922T031831Z-a03-b08-moc4-r11`  
Programme: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Assignment: exact/rigorously enclosed true-unitary + complex-spectrum adversary search, with common-direction separation from all 24 spectral vertices.  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Exact inherited inputs actually used

1. Previous fleet03/B08 result `MOC4-ONE-CYCLE-CHORD-v1`: with
   `U0=R12(c1,s1)R23(c2,s2)R34(c3,s3)` and the real closing rotation `R14(c4,s4)`, the only one-cycle interference direction is the spectral chord

   `Delta = v_4123-v_1423 = (a1-a2)(a3+b2)(a4+b3)(b1-b4)`.

2. Named assigned partner fleet04/B09 `MOC4-FLAT-PAIR-TWIRL-LIFT-v1` (shared handoff blob `486d887f46b4647f58bc8754f6ebf01fed33594e`): the Haar average of a genuine row/column pair orbit has an exact probability lift to the 24 permutation vertices. Consequently a flat pair orbit cannot support a target violation; the only surviving global-maximizer branch is pair-strict.

The partner theorem is used below to interpret the escape criterion: strict failure of the payment inequality produces a strict pair-orbit maximizer, so it lands precisely in the branch not killed by pair-flat twirling. No arbitrary bistochastic array or negative formal determinant coefficient is treated as a counterexample.

## New theorem — `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`

Let

`U0 = R12(c1,s1) R23(c2,s2) R34(c3,s3)`, with `cj^2+sj^2=1`,

and vary the final embedded `SU(2)` gate on columns `1,4` as

`G14(c,s;zeta) = [[c, s zeta],[-s zeta^{-1},c]]`, `|zeta|=1`, `c^2+s^2=1`.

Put `U=U0 G14(c,s;zeta)`. Let

`D0 = det(diag(a)+U0 diag(b) U0*)`,

`D1 = det(diag(a)+U0 G14(0,1;1) diag(b) G14(0,1;1)* U0*)`,

and

`K = c1 s1 s2 s3 (v_4123-v_1423)`.

Then for **all complex spectra**, including singular/repeated cases,

`D(U) = c^2 D0 + s^2 D1 + 2 c s Re(zeta) K`.                                      (1)

Equivalently, as the full closing `SU(2)` gate varies, the determinant image is exactly the filled affine ellipse

`E = { (D0+D1)/2 + x (D0-D1)/2 + y K : x^2+y^2 <= 1 }`.                  (2)

In particular, complex closing phases cannot create a larger support excursion than a real orthogonal closing rotation: every support maximum of this entire `SU(2)` closing family occurs at `zeta=+1` or `-1`.

### Proof of (1)

Write the columns of `U0` as `u1,u2,u3,u4`. Explicitly,

```
U0 = [ c1,  c2 s1,      c3 s1 s2,  s1 s2 s3 ]
     [-s1,  c1 c2,      c1 c3 s2,  c1 s2 s3 ]
     [  0,    -s2,        c2 c3,      c2 s3 ]
     [  0,      0,           -s3,          c3 ].
```

Since `det U=1`,

`D(U)=det(diag(a)U+U diag(b))`.

For vectors `x,y`, define

`F(x,y)=det((A+b1 I)x,(A+b2 I)u2,(A+b3 I)u3,(A+b4 I)y)`, where `A=diag(a)`.

Right multiplication by `G14(c,s;zeta)` replaces

`u1 -> c u1 - s zeta^{-1} u4`, `u4 -> s zeta u1 + c u4`.

Bilinearity of the determinant in columns 1 and 4 therefore gives

`D(U)=c^2 F(u1,u4)-s^2 F(u4,u1)+cs[zeta F(u1,u1)-zeta^{-1}F(u4,u4)]`.

The first two terms are `c^2 D0+s^2 D1`. Direct 2-by-2 block expansion using the displayed triangular `U0` gives

`F(u1,u1)=c1 s1 s2 s3 (a1-a2)(a3+b2)(a4+b3)(b1-b4)=K`,

`F(u4,u4)=-c1 s1 s2 s3 (a1-a2)(a3+b2)(a4+b3)(b1-b4)=-K`;

the second identity uses only `c2^2+s2^2=c3^2+s3^2=1`. Thus the cross term is

`cs(zeta+zeta^{-1})K=2cs Re(zeta)K`, proving (1).

For (2), set `x=c^2-s^2` and `y=2cs Re(zeta)`. Then `x^2+y^2<=1`. Conversely every point of the unit disk is obtained by choosing `c^2=(1+x)/2`, `s^2=(1-x)/2`, and an appropriate `Re(zeta)=y/sqrt(1-x^2)` (with the endpoint cases interpreted continuously).

## Exact common-separating-direction criterion

Fix a real-linear support functional `L` and let

`M=max_{sigma in S4} L(v_sigma)`,
`A=L(D0)`, `B=L(D1)`, `C=L(K)`,
`delta0=M-A`, `delta1=M-B`.

Both endpoint deficits are nonnegative because `D0,D1` are one-use forest-Givens determinants and have explicit nonnegative permutation lifts. Taking the support of ellipse (2) gives

`max_{closing SU(2)} L(D) = (A+B)/2 + sqrt(((A-B)/2)^2 + C^2)`.

Hence the **entire genuine closing SU(2) orbit** is target-safe in this common direction if and only if

`C^2 <= delta0 delta1`.                                                     (3)

Indeed

`M-max L(D) = (delta0+delta1)/2 - sqrt(((delta0-delta1)/2)^2+C^2)`,

and squaring the two nonnegative sides reduces exactly to (3).

Conversely, if `C^2>delta0 delta1` for any actual spectra, first-three-gate parameters and common direction `L`, then the ellipse has a true-unitary point strictly beyond all 24 target vertices. Moreover the maximizing disk point lies on `x^2+y^2=1`, so it can be realized with `zeta=+1` or `-1`; **a payment failure would immediately give a genuine real-orthogonal MOC4 counterexample**, not merely a negative formal coefficient or a surrogate-array failure. Its pair-orbit maximum is strict, consistently with the assigned partner's theorem that flat pair orbits are safe.

Thus `MOC4-ONE-CYCLE-PAYMENT-v1` is now an exact scalar inequality problem, not a determinant-expansion problem.

## Exact generic near-saturation stress test

A reproducible all-rational/Gaussian-integer stress datum is:

`a=(10-13i, -18+17i, -20+5i, -20+11i)`,

`b=(17-18i, -22+3i, -19-7i, 2+7i)`,

`(c1,s1)=(3/5,4/5)`, `(c2,s2)=(c3,s3)=(7/25,24/25)`,

`L(z)=3 Re(z)-8 Im(z)`.

The two spectra are simple and every one of the 16 sums `ai+bj` is nonzero. Enumeration of all 24 genuine target vertices gives a unique support maximum

`M=-66900` at permutation `2143`.

The exact endpoint/chord support data are

`delta0 = 35784788989884 / 9765625`,

`delta1 = 55713312637364 / 9765625`,

`C = 14186271744 / 3125`.

The payment is positive but close to saturation:

`delta0 delta1 - C^2 = 28354117176867745556425776 / 95367431640625 > 0`,

and

`C^2/(delta0 delta1) = 40944479572471680000000000 / 41535190346989758032425537`

`= 0.98577806506764...`, so `|C|/sqrt(delta0 delta1)=0.9928635682...`.

Thus the dangerous axis reaches more than 99.28% of the geometric-mean payment threshold, yet the **entire closing SU(2) family is rigorously safe in this direction** by (3). A nearby exact real closing rotation

`(c4,s4)=(2849/3649,2280/3649)`

has exact target support gap

`4140288641104458684 / 130031259765625 > 0`.

The adjacent standard-library verifier `verify_one_cycle_ellipse.py` independently enumerates all 24 spectral vertices, checks the two forest probability lifts, simplicity/nonvanishing, the unique common-direction support maximum, the exact payment inequality, and the final rational true-unitary gap. Captured output is `VERIFICATION.txt`.

Exploratory true-unitary/Gaussian-spectrum sweeps were also used to search for `C^2>delta0 delta1`; none was promoted as evidence of truth. Search misses are not a proof. The exact near-saturation datum above is retained because it is useful for falsifying overly coarse payment bounds.

## What this changes and next exact obligation

This run removes an entire nuisance dimension from the first cyclic mechanism: arbitrary complex phase on the closing `SU(2)` gate is **not** a stronger adversary than the real orthogonal boundary. The one-use 4-cycle problem is exactly the ellipse-payment inequality (3).

Next target for B08 / partner handoff:

`MOC4-ONE-CYCLE-PAYMENT-v2`: either

1. prove `C^2<=delta0 delta1` for every complex spectrum, every real first-three Givens parameters and every real-linear support direction; this would close the full one-use 4-cycle `SU(2)` family including singular/repeated spectra; or
2. find exact data with strict reverse inequality; by the theorem above that data immediately gives a genuine true-unitary, common-separating-direction MOC4 counterexample.

If this same payment implication survives three substantive B08 runs unchanged, the owner control requires a materially different mechanism on MOC4 (e.g. repeated-edge/two-cycle or strict-interior Hessian adversary), preserving this reduction rather than repeating the same sweep.

No benchmark gold/keys, FEI proof material, arbitrary bistochastic proxy, paid model/API/Codex, email/Drive/public workflow, credentials or cross-account native action was used.
