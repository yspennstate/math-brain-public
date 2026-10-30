SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T22:46:49Z.
attacking: product-provenance-sensitive hyperbolic smoothing for the remaining one-strong-cross indefinite/overlapping-curvature branch.

# fleet03/B09 QFORM r19 — two independent hyperbolic products give a bounded density

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet03/B09` — Bilinear block mechanism  
Run: `20260922T224649Z-fleet03-B09-QFORM-r19`  
Outcome: **NEW SUPPORTING THEOREM / PRODUCT-PROVENANCE INDEFINITE BRANCH PAID / FULL TARGET OPEN**.  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture remains open. This run does not assume Gaussianity, moments, compact or connected support, log-concavity, or independence after a spectral rotation. It stays in original-coordinate product geometry. The new point is that the logarithmic singularity of one bilinear product is harmless in `L^2`; convolving two genuinely independent bilinear products therefore gives an `L^infinity` density directly. This is a linear-in-interval-length argument and does not square a probability or take a square root of the target interval length.

## 1. Source state and corrections used

The live source state still marks the full conjecture and global continuity as open. I enforced the current corrections: law-uniform pointwise quadratic-phase decay is false; arbitrary spectral-fiber suprema can lose dimension; post-rotation coordinates are not independent; arbitrary-joint coarea and conditional-density-moment replacements are false; and an arbitrary bounded projected joint density does not control an indefinite quadratic pushforward. The theorem below avoids all of these interfaces.

The designated partner `fleet04/B09` was checked in the current canonical QFORM handoff location and had no completed current-QFORM artifact. I therefore did not fabricate or await a partner theorem. A fresh completed same-role result from **fleet01/B09** is consumed in Section 5 at an actual inequality.

## 2. Analytic core: a product of two bounded-density variables is uniformly `L^2`

### Lemma 2.1 — `QFORM-PRODUCT-L2-v1`

Let `X,Y` be independent real random variables with probability densities bounded by `1`. Then `XY` has a density `p_XY` satisfying

`boxed: ||p_XY||_2 <= 4.`                                                   (2.1)

More generally, if the density caps are `N_X,N_Y`, then

`boxed: ||p_XY||_2 <= 4 sqrt(N_X N_Y).`                                    (2.2)

The estimate is translation-uniform in the sense that it applies unchanged after replacing either variable by an arbitrary deterministic translate, because such translation preserves the density cap.

#### Proof

Let `R=|X|`, `S=|Y|`. Their densities `F,G` on `(0,infinity)` satisfy

`0<=F<=2`, `0<=G<=2`, `integral F=integral G=1`.                            (2.3)

The positive random variable `P=RS` has density

`h(z)=integral_0^infinity F(x) G(z/x) dx/x`, `z>0`.                         (2.4)

Set, on the logarithmic line,

`a(s)=e^(s/2) F(e^s)`, `b(s)=e^(s/2) G(e^s)`.                              (2.5)

If `z=e^t`, then

`H(t):=e^(t/2) h(e^t)=(a*b)(t)`.                                           (2.6)

Moreover

`||H||_2^2=integral_R e^t h(e^t)^2 dt=integral_0^infinity h(z)^2 dz
          =||h||_2^2`.                                                      (2.7)

Young's convolution inequality gives

`||h||_2 <= ||a||_1 ||b||_2`.                                              (2.8)

The second factor obeys

`||b||_2^2=integral_0^infinity G(x)^2 dx <=2 integral G=2`.                 (2.9)

For the first factor,

`||a||_1=integral_0^infinity x^(-1/2) F(x) dx`.                            (2.10)

Among probability densities bounded by `2`, the integral against the decreasing weight `x^(-1/2)` is maximized by `F=2 1_[0,1/2]` (the elementary bathtub/rearrangement principle). Hence

`||a||_1 <=2 integral_0^(1/2) x^(-1/2) dx=2 sqrt(2)`.                      (2.11)

Combining (2.8)-(2.11) gives `||h||_2<=4`.

For `z>0`, the density of the signed product satisfies

`p_XY(z)+p_XY(-z)=h(z)`.                                                    (2.12)

Both summands are nonnegative, so

`p_XY(z)^2+p_XY(-z)^2 <= h(z)^2`.                                          (2.13)

Integrating over `z>0` yields (2.1).

For caps `N_X,N_Y`, scale to `X'=N_X X`, `Y'=N_Y Y`; both scaled variables have density cap at most one. Since `X'Y'=N_XN_Y XY` and an `L^2` density scales by the inverse square root of the dilation, (2.2) follows. `QED`

### Corollary 2.2 — scaled bilinear product

If `U,V` are independent with density caps `N_U,N_V`, then for `a!=0`,

`boxed: ||p_(2aUV)||_2 <= 2 sqrt(2) sqrt(N_U N_V/|a|).`                    (2.14)

The same estimate holds for

`2aUV+alpha U+beta V+delta`,                                               (2.15)

because

`2aUV+alpha U+beta V
 =2a(U+beta/(2a))(V+alpha/(2a))-alpha beta/(2a)`,                           (2.16)

and the deterministic translates remain independent with the same density caps.

## 3. Two hyperbolic blocks: direct `L^2 * L^2 -> L^infinity`

### Theorem 3.1 — `QFORM-FOUR-BANK-HYPERBOLIC-CONVOLUTION-v1`

Let `U,V,W,R` be mutually independent real random variables with density caps respectively

`N_U,N_V,N_W,N_R`.

Let `a,b` be nonzero and let all affine coefficients be arbitrary. Define

`T = 2aUV + 2bWR
     + alpha U+beta V+gamma W+eta R+delta`.                              (3.1)

Then `T` has a bounded continuous density and

`boxed: ||p_T||_infinity
 <= 8 sqrt( N_U N_V N_W N_R / |ab| ).`                                  (3.2)

Consequently every interval `L` obeys

`boxed: P{T in L}
 <= 8 sqrt( N_U N_V N_W N_R / |ab| ) |L|.`                              (3.3)

#### Proof

Complete the two bilinear rectangles separately using (2.16). Thus, up to a deterministic translation,

`T=T_1+T_2`,                                                             (3.4)

where `T_1=2a U'V'`, `T_2=2b W'R'`, and the primed variables preserve all four mutual independence relations and density caps. Corollary 2.2 gives

`||p_T1||_2 <=2sqrt(2) sqrt(N_U N_V/|a|)`,
`||p_T2||_2 <=2sqrt(2) sqrt(N_W N_R/|b|)`.                               (3.5)

The two blocks are independent, so `p_T=p_T1*p_T2`. Cauchy--Schwarz at every point gives

`||p_T||_infinity <=||p_T1||_2 ||p_T2||_2`,                              (3.6)

which is exactly (3.2). Since the convolution of two `L^2(R)` functions is bounded and continuous, the standalone density in (3.1) is continuous. Equation (3.3) follows by integrating the density over `L`. `QED`

This mechanism is qualitatively different from the false arbitrary-joint indefinite-shell shortcut. It uses four **genuinely independent source variables/banks** and never replaces their provenance by one joint `L^infinity` cap.

## 4. Original-coordinate bank form

Let `I,J,K,L` be four pairwise disjoint sets of original independent coordinates and define

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`, `R=<r,X_L>`.                       (4.1)

Use the already source-validated one-dimensional product-projection estimate

`||p_(<q,X_B>)||_infinity <= sqrt(2)/||q||_2`                              (4.2)

for every nonzero original-coordinate vector `q` on a bank `B`. Set the aggregate bilinear strengths

`s_1=|a| ||u||_2 ||v||_2`,
`s_2=|b| ||w||_2 ||r||_2`.                                                (4.3)

Substituting (4.2) into (3.2) gives

`boxed: ||p_T||_infinity <=16 / sqrt(s_1 s_2).`                            (4.4)

Therefore

`boxed: P{T in L} <=16 |L| / sqrt(s_1 s_2).`                              (4.5)

In particular, if both aggregate cross strengths are at least `tau`, then

`||p_T||_infinity <=16/tau`.                                               (4.6)

This is the desired aggregate-before-inversion behavior: a physical coefficient may be `O(1/m)`, while the whole bank strength remains order one.

### Conditional ambient use

The same essential bound survives conditioning on disjoint outside coordinates whenever the active four-bank quadratic part is exactly the two rank-one cross blocks above and the conditioned outside couplings enter the active variables only through the four scalar directions `u,v,w,r`. The resulting affine coefficients may depend arbitrarily on the outside realization; (3.2) is uniform in them, so averaging preserves the bound. This conditional statement establishes essential boundedness. Continuity of the resulting mixture is **not claimed** without an additional uniform-continuity argument. If outside coordinates contribute only an independent additive random shift, convolution preserves continuity.

## 5. Actual application of a fresh other-account theorem

I consumed fleet01/B09's fresh completed theorem `QFORM-PAIRLOG-LP-SCHUR-RESIDUAL-v1`, canonical source

`yspennstate/math-open-problems@77b5307b899cf99953a7b6c81bb41f94c92ff53d:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/B09-20260922T224934Z-r18/REPORT.md`.

For an invertible indefinite physical endpoint pair `E`, write

`D=|det E|`, `kappa=sigma_min(E)`.                                        (5.1)

If its exact Schur moving-critical-value residual `R_0` has an `L^3` density, the fleet01 theorem gives

`||p_Q||_infinity
 <=7 (pi/12)^(1/7) D^(-3/14) kappa^(-2/7) ||p_R0||_3^(3/7).`              (5.2)

Now suppose that this exact Schur residual is a four-bank hyperbolic block of Theorem 3.1 with original-coordinate strengths `s_1,s_2`. By (4.4),

`||p_R0||_infinity <=16 (s_1 s_2)^(-1/2)`.                                (5.3)

Since `p_R0` is a probability density,

`||p_R0||_3^3 <=||p_R0||_infinity^2`,

hence

`||p_R0||_3 <=16^(2/3)(s_1s_2)^(-1/3)`.                                  (5.4)

Substituting (5.4) into the **other-account** endpoint theorem (5.2) gives the new composite inequality

`boxed: ||p_Q||_infinity
 <= 7 (pi/12)^(1/7) 16^(2/7)
    D^(-3/14) kappa^(-2/7) (s_1s_2)^(-1/7)`                               (5.5)

and numerically

`boxed: ||p_Q||_infinity
 <12.764 D^(-3/14) kappa^(-2/7) (s_1s_2)^(-1/7).`                          (5.6)

Thus a controlled indefinite endpoint pair followed by two genuinely independent hyperbolic residual banks has a direct `O(|L|)` estimate, with no square-root decoupling. This is an actual use of the completed fleet01/B09 result, not merely a citation.

The designated partner `fleet04/B09` still had no completed current-QFORM artifact at publication-time checking; no result is attributed to it.

## 6. Diffuse target-valid stress family

Let `m>=1`. Take four disjoint original-coordinate banks `I,J,K,L`, each of size `m`, and normalized flat vectors

`u=v=w=r=m^(-1/2)(1,...,1)`                                               (6.1)

on their respective banks. Let the symmetric matrix have only the two cross blocks

`A[I,J]=uv^T`, `A[J,I]=vu^T`,
`A[K,L]=wr^T`, `A[L,K]=rw^T`.                                             (6.2)

On `span{u,v,w,r}`, the compressed matrix is

`[[0,1,0,0],
  [1,0,0,0],
  [0,0,0,1],
  [0,0,1,0]]`.                                                            (6.3)

Hence the nonzero spectrum is exactly

`{-1,-1,1,1}`.                                                            (6.4)

This is inside the owner's target (`at least three` eigenvalues of modulus at least one) for every `m`. Every nonzero physical matrix entry has magnitude `1/m`, so fixed local coefficients vanish with dimension. Nevertheless `s_1=s_2=1`, and (4.4) gives, for every admissible product input law,

`boxed: ||p_(X^T A X)||_infinity <=16`,                                   (6.5)

uniformly in `m`. The density is continuous in this pure four-bank form.

The finite checker in this run verifies the constants and spectrum; it is only an algebraic check, not a universal proof substitute.

## 7. Relation to the current one-strong-cross indefinite survivor

The previous B09 run showed that an arbitrary bounded joint density cap is insufficient for an indefinite transverse block: a thin hyperbolic shell can concentrate its quadratic image. Theorem 3.1 identifies a source-valid repair for one important subcase. If the indefinite transverse curvature can be realized before projection as a second rank-one cross interaction between two **disjoint original-coordinate subbanks**, then its product provenance gives an `L^2` density rather than a dangerous arbitrary joint cap. Convolution with the first bilinear interaction pays the logarithmic singularity and produces the linear interval bound (4.5).

This closes the `two independent hyperbolic packets` branch but not an arbitrary indefinite same-bank quadratic block. The exact next B09 implication is therefore:

`QFORM-INDEFINITE-CURVATURE-DISJOINT-SPLIT-OR-PAID-EXIT-v1` — starting from the remaining one-strong-cross geometry, prove that either a quantitatively strong part of the opposite-bank indefinite curvature splits across two disjoint original-coordinate subbanks (so Theorem 3.1 applies), or route the non-splitting structure to the existing ridge / physical-pair / rank-one aligned-bank mechanisms.

The difficult survivor is an indefinite curvature operator whose mass is strongly overlapping in the original coordinate support, so that no quantitative independent hyperbolic subpacket is immediately available. That is a structural extraction problem; it is not resolved here.

## 8. Status

- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- New result: `QFORM-PRODUCT-L2-v1` and `QFORM-FOUR-BANK-HYPERBOLIC-CONVOLUTION-v1`, proved above.
- Interval dependence: genuinely `O(|L|)`.
- Square-root decoupling: **not used**.
- Post-rotation independence: **not used**.
- Standalone four-bank density: **continuous and bounded**.
- General outside-conditioned application: **essential boundedness proved in the stated aligned scope; continuity not claimed**.
- Native brain ingestion: **not verified; WITHOUT_VERIFIED_BRAIN**.
