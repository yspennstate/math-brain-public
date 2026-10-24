SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-22T22:10:34Z.
attacking: the many-small-pair null-frame residual by aggregating determinant mass into projective null-ray banks and paying the designated partner's parabolic trace without conditional-cap shortcuts.

# account03/B11 QFORM r18 — zero-disjoint-Pluecker endpoint closes into at most five null-ray banks

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B11` — Indefinite signatures  
Run: `20260922T221034Z-account03-B11-QFORM-r18`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ENDPOINT / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report proves a new exact endpoint theorem for genuinely rotated exact-rank-three indefinite forms with zero physical diagonal: if their disjoint Pluecker mass vanishes, then the product source compresses exactly into at most five independent projective null-ray banks, hence has a universal bounded density. This removes the most singular endpoint of the previous B11 many-small-pair/null-frame residual. The remaining problem is a quantitative stability theorem for small positive disjoint Pluecker mass together with arbitrary additional spectrum.

No step uses post-rotation independence, arbitrary-joint coarea, a conditional-density cap as a substitute for independence, a fiber supremum, law-uniform pointwise Fresnel decay, moment/support assumptions, or perturbative deletion of small coefficients.

## 1. Source-pinned inputs

### 1.1 Exact null-graph identity from the designated partner account04/B11

Consumed completed partner result:

`yspennstate/math-open-problems@797dcde430e982a020d7642b54cadc281cbc9bc1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T191727Z-account04-B11-nullgraph-obstruction-r2/REPORT.md`.

For

`H0 = [[0,0,1],[0,1,0],[1,0,0]]`

and `T=Y^T H0 Y=2 Z W+V^2`, with joint density `h` of `Y=(Z,V,W)`, that report proves

`N(h):=sup_t integral_{w != 0} h((t-v^2)/(2w),v,w) dv dw/|w|`

satisfies

`N(h)=2 ||p_T||_infinity`.                                         (1.1)

It also gives a nonlinear dependent construction with bounded transverse density and bounded conditional scalar density but `N(h)=infinity`. Thus any positive result below must retain original-coordinate product-linear provenance.

### 1.2 Finite spectral-line bank compression

Consumed completed theorem:

`yspennstate/math-open-problems@091696c4b92a93950f1211593deafd16c0c26235`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T220011Z-account02-B16-QFORM-auto11/REPORT.md`.

For an exact-rank-three form

`A=R Lambda R^T`, `R^T R=I_3`, `min_j |lambda_j(Lambda)|>=1`,

if the nonzero physical spectral rows of `R` lie on at most `K` projective line directions, then

`||p_Q||_infinity <= 2 C3 binom(K,3)^(1/3)`,                    (1.2)

where

`C3=16 sqrt(30) 2^(1/4)=104.21688998922089...`.

The proof compresses each line direction into one normalized scalar projection of a disjoint set of ORIGINAL independent coordinates, and only afterward applies a translation-stable physical-triple determinant theorem. It therefore remains valid for arbitrary cap-one one-dimensional input laws.

## 2. Canonical indefinite null geometry

Let `Lambda` have signature `(2,1)` or `(1,2)`. Negating the form exchanges these signatures and does not affect the argument, so fix `(2,1)`.

For the canonical congruence form `H0`, a convenient affine chart of the projective null cone is

`r(t)=(1,t,-t^2/2)^T`.                                             (2.1)

Direct calculation gives the exact identities

`r(s)^T H0 r(t)=-(s-t)^2/2`,                                      (2.2)

and

`det[r(s),r(t),r(u)]
   = (s-t)(s-u)(t-u)/2`.                                          (2.3)

Thus two different null rays have a nonzero opposite-sign hyperbolic pairing, while three distinct null rays supply a Vandermonde triple volume. This is the projective version of the B11 theme: two opposite-sign directions retain the rank-two logarithmic saddle, whereas a genuinely third null direction creates nonzero three-dimensional curvature.

The argument below does not depend on this chart. The coordinate-free fact needed is:

**Null-plane fact.** If `W` is a vector subspace of dimension at most two, the `Lambda`-null vectors in `W` occupy at most two projective lines.

Proof: if `dim W<=1` it is immediate. If `dim W=2`, the restriction of the nondegenerate quadratic form `x^T Lambda x` to `W` is not identically zero, because a real quadratic space of signature `(2,1)` has maximal totally isotropic subspace dimension one. Its restriction is therefore a nonzero homogeneous quadratic polynomial on `P(W)=P^1`, and has at most two real projective zeros. QED.

## 3. Disjoint Pluecker mass

Write the physical rows of `R` as `r_i^T`. Since `A_ii=0`,

`r_i^T Lambda r_i=0`                                               (3.1)

for every nonzero row: every physical row is a null ray.

For each physical triple `S={i,j,k}`, put

`w_S=det(R_S)^2 >=0`.                                               (3.2)

Cauchy--Binet and `R^T R=I_3` give

`sum_{|S|=3} w_S=1`.                                               (3.3)

Define the ordered disjoint-basis mass

`D0=sum_{S cap T=empty} w_S w_T`.                                  (3.4)

The earlier disjoint-exterior theorem pays the branch `D0>0` with a bound depending on `D0`. The endpoint `D0=0` was not previously converted into an explicit product-bank certificate.

## 4. Main theorem: zero disjoint mass forces at most five null-ray banks

### Theorem 4.1 — `QFORM-NULL-D0ZERO-FIVE-RAY-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`,

have exact rank three, signature `(2,1)` or `(1,2)`, and

`min_j |lambda_j(Lambda)|>=1`.

Assume every physical diagonal vanishes,

`A_ii=0` for all `i`,                                               (4.1)

and the disjoint Pluecker mass (3.4) is zero:

`D0=0`.                                                            (4.2)

Then all nonzero rows of `R` lie on at most five projective line directions. Consequently, for arbitrary independent original-coordinate variables with densities bounded by one,

`boxed: ||p_(X^T A X)||_infinity
       <= 2 C3 10^(1/3)
       =449.0569661600281... .`                                    (4.3)

In particular the endpoint has a dimension-free essential density bound despite arbitrarily many physical coordinates and arbitrarily fragmented one-dimensional input laws.

### Proof

By (3.3), choose one basis triple

`B={i_1,i_2,i_3}` with `w_B>0`.                                    (4.4)

Because `D0=0`, there is no triple `T` disjoint from `B` with `w_T>0`. Equivalently, the rows indexed by the complement `B^c` cannot span all of `R^3`: if they did, three of them would form a basis `T` disjoint from `B`, contradicting (4.2). Hence

`dim span{r_j:j in B^c} <=2`.                                      (4.5)

Every one of those complement rows is `Lambda`-null by (4.1). The null-plane fact therefore places all rows in `B^c` on at most two projective null lines. The three rows in `B` contribute at most three additional projective lines. Hence the entire physical spectral frame occupies at most

`2+3=5`                                                           (4.6)

line directions.

Apply the finite spectral-line bank compression theorem (1.2) with `K<=5`; since `binom(5,3)=10`, (4.3) follows. The bank compression occurs before any reciprocal physical-minor payment, so within-bank multiplicity costs nothing. QED.

## 5. Direct application of the designated account04/B11 trace identity

Every real nonsingular form of signature `(2,1)` is congruent to `H0`. Choose an invertible `S` with

`Lambda=S^T H0 S`,                                                (5.1)

and put

`L=S R^T`, `Y=L X`.                                                (5.2)

Then

`X^T A X=Y^T H0Y`,                                                (5.3)

and (4.1) says each column of `L` is `H0`-null. Since `S` is invertible, projective collinearity of the rows of `R` is preserved as projective collinearity of the source columns of `L`; thus Theorem 4.1 supplies the bound (4.3) for the genuine product-linear null frame.

Apply the partner identity (1.1) to the joint density `h` of `Y`. We obtain the actual inequality

`boxed: N(h)=2||p_(Y^T H0Y)||_infinity
       <=4 C3 10^(1/3)
       =898.1139323200562... .`                                   (5.4)

This is precisely a dimension-free parabolic null-graph trace bound in a branch where the partner's generic marginal/conditional-cap counterexample gives no control. The missing ingredient is not an improved conditional cap: it is the exact product provenance plus the rank-three null-matroid constraint that compresses the source into at most five independent line banks.

## 6. Why this is a genuine endpoint closure rather than a fixed-minor argument

The theorem permits each of the at most five null rays to contain arbitrarily many original coordinates, with arbitrarily small individual spectral-row norms. No uniformly large physical coefficient or physical `3x3` determinant is selected. The finite-line theorem first normalizes and compresses every entire ray bank; only the resulting bank-level determinant is paid.

The result therefore covers the exact `D0=0` limit of a sequence in which physical Pluecker mass becomes increasingly concentrated around overlapping bases. It also explains why a rank-two logarithmic singularity does not survive this endpoint: rank three guarantees at least three line banks spanning spectral space, and conditioning all unused independent banks leaves a genuine three-bank quadratic core. The third bank is the independent averaging channel absent from the two-ray saddle.

## 7. Remaining implication

This does not yield a uniform theorem for arbitrarily small **positive** `D0`. For `D0>0`, the existing disjoint-exterior estimate is finite but deteriorates like a negative power of `D0`; at `D0=0`, Theorem 4.1 jumps to the fixed five-bank constant (4.3). Closing that apparent discontinuity requires a stability/aggregation theorem that uses small non-collinear residual banks without treating their small coefficients perturbatively; no support or moment bound allows those coefficients simply to be discarded.

The next B11 implication is therefore:

`QFORM-NULL-INTERSECTING-BASE-STABILITY-v1` — prove that a null Parseval frame with small disjoint-basis mass either enters an already paid pair/ridge certificate or admits a product-preserving grouped-bank reduction with a bank-level determinant bounded below independently of the number of physical coordinates.

Arbitrary additional spectrum remains a separate full-target debt. The theorem here establishes essential boundedness only; continuity is not claimed from the finite-line compression theorem used in (4.3).

**Full QFORM:** OPEN / NOT PROVED.  
**Continuity for Theorem 4.1:** NOT PROVED here.  
**Opposite-sign rank-two logarithmic control:** retained; the new bound begins only when true rank-three spanning/product-bank structure is present.

## 8. Exact checks

For `H0=[[0,0,1],[0,1,0],[1,0,0]]` and `r(t)=(1,t,-t^2/2)`, symbolic expansion gives

`r(s)^T H0 r(t)=-(s-t)^2/2`,

`det[r(s),r(t),r(u)]=(s-t)(s-u)(t-u)/2`.

The constants are

`C3=16 sqrt(30) 2^(1/4)=104.21688998922089...`,

`2 C3 10^(1/3)=449.0569661600281...`,

`4 C3 10^(1/3)=898.1139323200562...`.
