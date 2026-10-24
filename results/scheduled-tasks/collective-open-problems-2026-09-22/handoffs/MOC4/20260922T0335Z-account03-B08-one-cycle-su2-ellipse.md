# MOC4 handoff — account03/B08 `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`

Run: `20260922T031831Z-a03-b08-moc4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific report: `proofnet24/collective-MOC4/account03/B08/20260922T031831Z-a03-b08-moc4-r11/REPORT.md` in `yspennstate/math-open-problems`, report creation commit `2527f18e3f2e2490719b31d5df5c6a17dbf38bea`, report blob `cd4264eb161c05fd44ff188490e4e0354295213c`. Exact standard-library verifier creation commit `3cc0ce5c29e4309dd38c4a408550644edddd738e`; captured verification creation commit `2bd19aaf71a5c9917982a85ef2d816b45a19fe63`.

## Named partner consumed and applied

Assigned partner **account04/B09**, `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`, shared handoff blob `486d887f46b4647f58bc8754f6ebf01fed33594e`: the Haar average of any genuine row/column pair orbit has an exact probability lift to the 24 permutation endpoints, so a flat pair orbit cannot support a target violation. This is used below to place any one-cycle escape on the surviving **pair-strict** branch rather than treating a flat/surrogate configuration as an adversary.

## New exact reduction

Let

`U0=R12(c1,s1)R23(c2,s2)R34(c3,s3)`

and close the cycle by an arbitrary embedded `SU(2)` gate on columns `1,4`,

`G14(c,s;zeta)=[[c,s zeta],[-s zeta^{-1},c]]`, `|zeta|=1`.

Put `D0=D(U0)`, let `D1` be the full-swap endpoint, and

`K=c1 s1 s2 s3 (v_4123-v_1423)`.

A direct determinant-bilinearity proof gives, for **all complex spectra** (singular/repeated included),

`D(U0 G14)=c^2 D0+s^2 D1+2cs Re(zeta) K`.

Therefore the complete closing-`SU(2)` determinant image is exactly the filled ellipse

`(D0+D1)/2 + x(D0-D1)/2 + yK`, `x^2+y^2<=1`.

For a common real-linear support `L`, let

`M=max_sigma L(v_sigma)`, `delta0=M-L(D0)`, `delta1=M-L(D1)`, `C=L(K)`.

Then the **whole genuine SU(2) closing orbit is target-safe in that direction iff**

`C^2 <= delta0 delta1`.

If the strict reverse inequality ever occurs, the support-maximizing ellipse point lies on the real orthogonal boundary (`zeta=+/-1`) and is immediately a genuine MOC4 counterexample in the same common direction. Thus complex closing phase is not a stronger adversary than the real one-cycle boundary.

## Exact generic near-saturation datum

Take

`a=(10-13i,-18+17i,-20+5i,-20+11i)`,
`b=(17-18i,-22+3i,-19-7i,2+7i)`,
`(c1,s1)=(3/5,4/5)`, `(c2,s2)=(c3,s3)=(7/25,24/25)`,
`L(z)=3 Re(z)-8 Im(z)`.

Both spectra are simple and every `ai+bj` is nonzero. The unique maximum over all 24 target vertices is `M=-66900` at permutation `2143`. Exact payment data:

`delta0=35784788989884/9765625`,
`delta1=55713312637364/9765625`,
`C=14186271744/3125`,

`delta0 delta1-C^2 = 28354117176867745556425776/95367431640625 > 0`,

`C^2/(delta0 delta1)=40944479572471680000000000/41535190346989758032425537 ~= 0.98577806506764`.

So the dangerous axis reaches about `99.286%` of the geometric-mean threshold but the entire closing SU(2) orbit is rigorously safe in this direction. This is retained as a hard falsification datum for coarse payment bounds; the search miss itself is not promoted as proof.

## Next exact implication

`MOC4-ONE-CYCLE-PAYMENT-v2`: prove `C^2<=delta0 delta1` for all spectra, first-three Givens parameters and common support directions, or find an exact strict reverse inequality. A reverse inequality is now automatically a true-unitary/common-direction target counterexample, not a formal-coefficient or arbitrary-bistochastic artifact.

Recommended recipients: account03/B07 lead; assigned partner account04/B09; account03/B20 pair-twirl/curvature line; account01/B07 strict-interior Hessian line. Preserve the three-run mechanism-change rule if this same payment implication remains unpaid.
