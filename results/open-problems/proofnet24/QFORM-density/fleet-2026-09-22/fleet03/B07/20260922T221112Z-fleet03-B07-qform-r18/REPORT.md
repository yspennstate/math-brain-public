SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-22T22:11:12Z.
attacking: the two-star S0 survivor — prove a source-valid L2 smoothing theorem for two disjoint physical product stars, apply the sharp product-projection cap, and isolate exactly what arbitrary same-bank curvature still costs.

# fleet03/B07 — two-product L2 smoothing and a paid clean two-star endpoint

**Run:** `20260922T221112Z-fleet03-B07-qform-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `PROVED_SUPPORTING_THEOREM + ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN`.

## 1. Incoming state and correction discipline

The exact target is unchanged: for arbitrary finite `n`, independent real coordinates having one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. Continuity is a separate stronger requested conclusion.

This run uses no Gaussian, moment, compact-support, log-concavity, post-rotation independence, arbitrary-joint rank-three coarea bound, positive conditional projection-height moment, pointwise Fresnel decay, fiber-supremum integration, or one-good-minor selector.

The immediate B07 state comes from the preceding run:

`yspennstate/math-open-problems@a20d669ff2c433cc70cb70234f49431da4518fa5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T203738Z-fleet03-B07-qform-r17/REPORT.md`.

In the high-leverage S0 branch, an original-coordinate row/column anchor forces either

`b^2 ||C||_F^2 > E_2(B)/8`

or

`||r||_2^2 ||c||_2^2 > E_2(B)/8`.

For the completed fleet02/B19 S0 source, `E_2(B)>=1/48`, so the second alternative gives the explicit two-star reserve

`||r||_2^2 ||c||_2^2 >1/384`.                                  (1.1)

The designated `fleet04/B07` still has no completed current-QFORM handoff directory at the fresh source check. I therefore do not invent one. The compatible completed fleet04 result actually applied below is fleet04/B18's sharp product-projection transfer, whose source is

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

That report applies Juškevičius--Lee sharp Rogozin rearrangement and the standard Ball cube-slicing endpoint: a normalized linear combination of independent cap-one variables has density at most `sqrt(2)`. I use exactly that original-coordinate product-projection fact; no rotated independence is asserted.

## 2. A universal L2 theorem for one product

### Theorem 2.1 — `QFORM-PRODUCT-L2-v1`

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying

`||f||_infinity<=M`, `||g||_infinity<=N`,

and let `kappa!=0`. Then `W=kappa X Y` has an `L^2` density and

`boxed(||p_W||_2 <=2 sqrt(MN/|kappa|).)`                         (2.1)

No moments or support assumptions are required.

### Proof

First reduce to `M=N=1` and `kappa=1`. Indeed `X'=MX` and `Y'=NY` have density caps at most one, while

`XY=(X'Y')/(MN)`.

The final `kappa` scaling contributes `|kappa|^{-1/2}` to the `L^2` norm.

For cap-one inputs the product density is, for almost every `z`,

`h(z)=int_R f(x) g(z/x) dx/|x|`.                                (2.2)

By Tonelli,

`||h||_2^2
 =int int f(x)f(y) K(x,y) dxdy`,                               (2.3)

where for nonzero `x,y`

`K(x,y)=1/(|xy|) int_R g(z/x)g(z/y) dz`.                         (2.4)

With `z=xu`,

`K(x,y)=1/|y| int g(u) g((x/y)u)du <=1/|y|`,                    (2.5)

because `g<=1` and `int g=1`. Interchanging `x,y` also gives `K<=1/|x|`. Hence

`K(x,y)<=1/max(|x|,|y|)`.                                       (2.6)

Put

`F(t)=int_{|x|<=t} f(x)dx`.

Since `f<=1` and `int f=1`,

`F(t)<=min(1,2t)`.                                               (2.7)

Using

`1/max(a,b)=int_{max(a,b)}^infinity s^{-2}ds`,

we obtain

`int int f(x)f(y)/max(|x|,|y|) dxdy
 =int_0^infinity F(s)^2 s^{-2}ds`
` <=int_0^(1/2)4 ds + int_(1/2)^infinity s^{-2}ds`
` =2+2=4`.                                                       (2.8)

Therefore `||h||_2<=2`. Rescaling gives (2.1). QED.

The important feature is that arbitrary fragmented supports are allowed. The proof uses only the density cap and mass one.

## 3. Two disjoint products give a bounded continuous density

### Corollary 3.1 — `QFORM-TWO-DISJOINT-PRODUCT-DENSITY-v1`

Let `X_1,Y_1,X_2,Y_2` be mutually independent, with density caps `M_1,N_1,M_2,N_2`. For `kappa_1 kappa_2!=0`,

`Z=kappa_1 X_1Y_1+kappa_2 X_2Y_2+c`

has a bounded continuous density satisfying

`boxed(
||p_Z||_infinity
 <=4 sqrt(M_1N_1M_2N_2/|kappa_1kappa_2|).
)`                                                               (3.1)

The same conclusion holds after translating either factor in either product, because

`kappa XY+alpha X+beta Y
 =kappa (X+beta/kappa)(Y+alpha/kappa)-alpha beta/kappa`.          (3.2)

### Proof

The two product variables are independent. By Theorem 2.1 their densities lie in `L^2`, and Young/Cauchy--Schwarz gives

`||p_1*p_2||_infinity<=||p_1||_2||p_2||_2`,                     (3.3)

which is (3.1). Continuity follows from the standard `L^2*L^2 subset C_0` fact: translation is continuous in `L^2`, and

`||p_1*(tau_h p_2-p_2)||_infinity
 <=||p_1||_2 ||tau_h p_2-p_2||_2 ->0`.                          (3.4)

QED.

This is stronger than a half-Riesz estimate on its exact scope.

## 4. Actual application to the current B07 two-star reserve

Assume the source-valid two-star alternative (1.1), and assume the residual quadratic expression reaches the **clean four-bank endpoint**: after conditioning only on genuinely disjoint outside original-coordinate blocks, the variables participating in the two stars occur through

`2 X_i <r,Y> + 2 X_j <c,Z>`                                     (4.1)

up to additive constants and affine terms that can be absorbed by (3.2), with no remaining quadratic/self/cross curvature involving the four displayed groups. Here

- `X_i` and `X_j` are distinct cap-one physical coordinates;
- `Y` and `Z` are disjoint original-coordinate banks, disjoint also from `i,j`;
- all four groups are genuinely independent.

Normalize

`U=<r,Y>/||r||_2`, `V=<c,Z>/||c||_2`.                           (4.2)

By the completed Ball--Rogozin product-projection theorem used in fleet04/B18,

`||p_U||_infinity<=sqrt(2)`,
`||p_V||_infinity<=sqrt(2)`.                                    (4.3)

Apply Corollary 3.1 with

`kappa_1=2||r||_2`, `kappa_2=2||c||_2`,
`M_1=M_2=1`, `N_1=N_2=sqrt(2)`.

Then

`||p_R||_infinity
 <= 2sqrt(2) [||r||_2||c||_2]^(-1/2)`.                          (4.4)

By (1.1),

`||r||_2||c||_2 >1/sqrt(384)`,

so

`boxed(
||p_R||_infinity
 <2sqrt(2) 384^(1/4)
 =12.520676640586299... .
)`                                                               (4.5)

Thus the clean two-star endpoint is completely paid, with a continuous density, uniformly in the sizes and laws of the two banks.

### Half-Riesz consequence for the outer scalar-pivot route

Any probability density bounded by `M` satisfies

`sup_y E|R-y|^(-1/2)<=4 sqrt(M)`.                               (4.6)

Indeed split at radius `rho`:

`int_{|u|<=rho}|u|^(-1/2)p(y+u)du + rho^(-1/2)
 <=4M sqrt(rho)+rho^(-1/2)`,                                    (4.7)

and optimize at `rho=1/(4M)`.

Using (4.5),

`boxed(H_(1/2)(R)<14.153827265067946... .)`                     (4.8)

Therefore, whenever this clean endpoint occurs inside the completed physical scalar-square transducer

`Q=a(X_0+h)^2+R`,

one gets the actual density estimate

`boxed(||p_Q||_infinity<14.154 |a|^(-1/2).)`                    (4.9)

No lower bound on `|a|` is claimed here; the inequality is recorded at its exact pivot scope.

## 5. What this proves, and the first unpaid implication

The two-star reserve itself was not previously converted into an analytic bound. This run proves that **the product geometry is already sufficient once the two stars are genuinely separated from same-bank curvature**. The obstruction is therefore not the small individual coefficients or the diffuse bank size: the aggregate reserve (1.1), product projection, and `L^2` convolution pay those losses dimension-free.

What remains is exactly the curvature/core issue. In the general S0 survivor the same original-coordinate banks may still carry:

1. quadratic curvature inside the `Y` bank or inside the `Z` bank;
2. additional couplings between `Y` and `Z` through the residual core `C`;
3. couplings from the anchors to variables in their own-side banks.

Those terms cannot simply be discarded or conditioned through a rotated complement. The live same-square correction shows why: arbitrary same-bank curvature can turn a product-looking term into a square-type degeneracy. The present theorem therefore does **not** claim to pay the full two-star branch.

The first unpaid implication is now

`QFORM-S0-TWOSTAR-CURVATURE-ABSORPTION-v1` (OPEN):

> Starting from the genuine original-coordinate two-star reserve `||r||^2||c||^2>1/384`, prove a translation-uniform half-Riesz estimate that allows arbitrary same-bank quadratic terms and the residual cross core, or show that failure forces an already-paid physical pair/ridge/second-pivot/zero-pivot/grouped-square branch.

A useful next mechanism is to keep the product `L^2` estimate intact and treat curvature as a perturbation only after an exact physical Schur or grouped-coordinate decomposition; taking a conditional density supremum over a rotated bank is forbidden by the current corrections.

The edge-times-bank alternative `b^2||C||_F^2>1/384`, S1/S2, no-usable-scalar-pivot parents, and the arbitrary-small-pivot splice remain separate debts. Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Global continuity remains open; continuity is proved only for the clean two-star endpoint above.

## 6. Verification

The deterministic constants are

`2sqrt(2)384^(1/4)=12.520676640586299...`,

`4sqrt(12.520676640586299...)=14.153827265067946...`.

The layer-cake bound (2.8) splits exactly as `2+2=4`. These are exact consequences of the displayed formulas, not simulations.

**Native brain ingestion:** not verified. Repository reads/writes are not authenticated learned-memory receiver use, so this run remains `WITHOUT_VERIFIED_BRAIN`.
