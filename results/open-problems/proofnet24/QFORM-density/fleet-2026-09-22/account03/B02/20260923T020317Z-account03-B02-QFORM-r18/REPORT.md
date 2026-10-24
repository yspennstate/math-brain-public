SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T02:03:17Z.
attacking: the exact span-aligned two-sided square/rank-two packet left by the previous B02 Fourier theorem; close the final double-null local survivor by outside-coordinate Fourier smoothing or identify a genuine global kernel.

# account03/B02 QFORM r18 — outside-linear smoothing closes the final local double-null survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T020317Z-account03-B02-QFORM-r18`  
**Assignment:** Integrated Fourier estimate  
**Fresh owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** proved on the new branch below because the global characteristic function is in `L^1`; full-target continuity remains open.

## 1. Target and first unpaid implication

The exact target remains: for every finite `n`, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal bound for the density of `X^T A X`, or give a target-valid counterexample. No moments, Gaussianity, log-concavity, support regularity, or post-rotation independence are assumed.

The preceding B02 run proved a continuous-density theorem whenever a physical original-coordinate cross block has exact rank three. Applied to the unresolved two-sided rank-two packet, it closed every *transverse* scalar coupling and left only the exact span-aligned residue. Independently, account03/B09 then proved that for a physical scalar plus an invertible physical `2 x 2` cross packet, nonzero residual shear curvature is paid by account01/B11, and zero residual curvature with nonzero residual linear coefficient is paid by a mass-sensitive slice Hausdorff--Young argument. Its only local survivor was a shear direction that is a kernel of the active five-coordinate quadratic block.

This run attacks that survivor **before conditioning away the outside coordinates**. The key observation is that the same would-be kernel direction either couples linearly to the outside product bank, which supplies the missing Fourier integrability after averaging, or it is an exact kernel vector of the **full** matrix. This is a product-preserving statement and does not use the false arbitrary-joint coarea or conditional-density-moment interfaces.

## 2. Full physical block notation

Choose five distinct original coordinates and call them

`x, u_1, u_2, v_1, v_2`,

with `u=(u_1,u_2)` and `v=(v_1,v_2)`. Let `w` denote the vector of all remaining original coordinates; `w` may be empty. Because these are original coordinates, `x,u,v,w` are mutually independent product banks before any change of variables.

Write the full symmetric quadratic matrix in the block order `(x,u,v,w)` as

```
A = [ a     r^T   s^T   t^T
      r      C     B      E
      s     B^T    D      F
      t     E^T    F^T    G ],
```

where `C,D` are symmetric `2 x 2`, `B` is `2 x 2`, `E,F` have two rows, and `G` is symmetric. Assume throughout this theorem that

`det B != 0`.

Set

`kappa = B^(-T) s`, so that `B^T kappa=s`,

and define the left-shear coefficients

`a_L = a - 2 r^T kappa + kappa^T C kappa`,

`r_L = r - C kappa`,

`t_L = t - E^T kappa`.

Make the volume-preserving integration-variable change

`u' = u + kappa x`, equivalently `u=u'-kappa x`.

A direct expansion, with no probabilistic assumption on the sheared variables, gives

```
Q = a_L x^2 + 2x(r_L^T u' + t_L^T w)
    + u'^T C u' + 2u'^T Bv + 2u'^T Ew
    + v^T Dv + 2v^T Fw + w^T Gw.                 (2.1)
```

The `x-v` term cancels exactly because `B^T kappa=s`.

The transformed `(x,u')` density is not a product density. Its exact provenance is nevertheless explicit:

`h(x,u') = f_x(x) f_{u_1}(u'_1-kappa_1 x) f_{u_2}(u'_2-kappa_2 x)`.   (2.2)

Hence

`0 <= h <= 1`,

`m(u') := integral h(x,u') dx <= 1`,

and

`integral m(u') du' = 1`.                                            (2.3)

These are the only sheared-density facts used below.

## 3. Constant-affine double-null Fourier endpoint

First isolate the exact analytic estimate needed after conditioning `w`.

### Lemma 3.1 — `QFORM-DOUBLE-NULL-CONSTANT-AFFINE-FOURIER-v1`

Suppose `a_L=0`, `r_L=0`, and after fixing all outside coordinates the coefficient

`b != 0`

appears as `2 b x`. Keep arbitrary real quadratic-plus-affine terms in `u'` and `v`, and keep the invertible physical cross block `B`. Then the conditional characteristic function is in `L^1`, the conditional law has a continuous density, and

`||p||_infinity <= C_aff |b|^(-1/5) |det B|^(-2/5)`,                 (3.1)

where

`C_aff = 5 * 3^(3/5) / 2^(9/5) = 2.7758037936536497...`.             (3.2)

#### Proof

For fixed `u'`, let

`K_{u'}(tau) = integral h(x,u') exp(2 i tau b x) dx`.                 (3.3)

With Fourier convention `hat g(xi)=integral g(x)e^(i xi x) dx`, Hausdorff--Young `L^(4/3) -> L^4`, followed by `xi=2b tau`, gives

`||K_{u'}||_4 <= pi^(1/4) |b|^(-1/4) ||h(.,u')||_(4/3)`.             (3.4)

Since `0<=h<=1`,

`||h(.,u')||_(4/3) <= m(u')^(3/4)`.                                 (3.5)

Define

`H(tau)^2 = integral |K_{u'}(tau)|^2 du'`.                           (3.6)

Minkowski in `L^2(d tau)` gives

`||H||_4^2
 = || integral |K_{u'}|^2 du' ||_2
 <= integral ||K_{u'}||_4^2 du'
 <= pi^(1/2)|b|^(-1/2) integral m(u')^(3/2) du'
 <= pi^(1/2)|b|^(-1/2)`.                                             (3.7)

Therefore

`||H||_4 <= pi^(1/4)|b|^(-1/4)`.                                    (3.8)

The right physical bank `v` still has product density at most one. Multiplication by any within-bank unit-modulus quadratic/affine phase does not increase its `L^2` norm. The rank-two bilinear Plancherel estimate therefore gives, for `tau!=0`,

`|phi(tau)| <= pi |tau|^(-1) |det B|^(-1/2) H(tau)`.                 (3.9)

For every `T>0`, Holder with exponents `4/3` and `4`, using

`integral_(|tau|>T) |tau|^(-4/3) d tau = 6 T^(-1/3)`,                (3.10)

yields

`integral_(|tau|>T) |phi(tau)| d tau <= D_b T^(-1/4)`,               (3.11)

where

`D_b = pi^(5/4) 6^(3/4) |det B|^(-1/2)|b|^(-1/4)`.                  (3.12)

On `|tau|<=T`, use only `|phi|<=1`, so

`||phi||_1 <= 2T + D_b T^(-1/4)`.                                   (3.13)

The exact minimizer is `T=(D_b/8)^(4/5)`, and hence

`||phi||_1 <= 10 (D_b/8)^(4/5)`.                                    (3.14)

Fourier inversion gives a bounded continuous density, and dividing (3.14) by `2 pi` simplifies exactly to (3.1)--(3.2). QED.

This is a genuine integrated-Fourier statement. No pointwise decay is asserted for the one-dimensional quadratic phases; indeed the phase-aligned-support correction forbids such an assertion.

## 4. The full outside-linear theorem

Now impose the exact double-null conditions

`a_L=0`, `r_L=0`.                                                     (4.1)

Equation (2.1) becomes

`Q = 2x t_L^T w + R(u',v,w)`,                                        (4.2)

where `R` is independent of `x` as a polynomial, although the sheared density (2.2) keeps the exact `x-u'` dependence.

### Theorem 4.1 — `QFORM-DOUBLE-NULL-OUTSIDE-LINEAR-OR-GLOBAL-KERNEL-v1`

Under the full physical block setup of Section 2 and the double-null conditions (4.1):

1. If `t_L != 0`, then `Q` has a bounded **continuous** density and

`boxed( ||p_Q||_infinity
        <= C_out [ ||t_L||_2 |det B|^2 ]^(-1/5) )`,                  (4.3)

with

`C_out = 25 * 3^(3/5) / 2^(7/2)
       = 4.271769166372894...`.                                      (4.4)

Equivalently, the full characteristic function belongs to `L^1` with

`||phi_Q||_1 <= 2 pi C_out [ ||t_L||_2 |det B|^2 ]^(-1/5)`.          (4.5)

2. If `t_L=0`, then the nonzero vector

`h_0 = (1,-kappa,0,0)`                                               (4.6)

is an exact kernel vector of the **full** matrix `A`:

`A h_0 = 0`.                                                         (4.7)

Thus the final local double-null survivor is not an additional hidden quadratic direction: it is either paid by outside-product linear smoothing, or it extends to a genuine global quadratic kernel.

#### Proof of the smoothing branch

Condition on `W=w`. The conditional polynomial has exactly the form of Lemma 3.1 with

`b = t_L^T w`,                                                       (4.8)

while every `w`-dependent term in `u'` or `v` is an arbitrary within-bank affine phase already allowed by that lemma. The exceptional set `b=0` has probability zero when `t_L!=0`, because `t_L^T W` has an absolutely continuous law.

Therefore Tonelli/Minkowski and (3.14) give

`||phi_Q||_1
 <= E_W ||phi_(Q|W)||_1
 <= 2 pi C_aff |det B|^(-2/5) E |t_L^T W|^(-1/5)`.                  (4.9)

We now use product provenance exactly once. Normalize `theta=t_L/||t_L||_2`. The one-dimensional marginal theorem for product measures (Livshyts--Paouris--Pivovarov, Theorem 1.1, the same source used in B02 r17) gives

`||p_(theta^T W)||_infinity <= sqrt(2)`.                             (4.10)

After scaling,

`||p_(t_L^T W)||_infinity <= sqrt(2)/||t_L||_2 =: L`.                (4.11)

For any probability density `g<=L`, the one-dimensional bathtub principle gives, for `0<alpha<1`,

`integral |z|^(-alpha) g(z) dz
 <= [2^alpha/(1-alpha)] L^alpha`.                                    (4.12)

At `alpha=1/5`,

`E |t_L^T W|^(-1/5)
 <= 5 * 2^(-9/5) L^(1/5)
 <= 5 * 2^(-17/10) ||t_L||_2^(-1/5)`.                               (4.13)

Substitution into (4.9) yields

`||p_Q||_infinity
 <= C_aff * 5 * 2^(-17/10)
    |det B|^(-2/5)||t_L||_2^(-1/5)`.

Using (3.2), the constant is

`C_aff * 5 * 2^(-17/10)
 =25 * 3^(3/5) * 2^(-7/2)=C_out`,                                   (4.14)

which proves (4.3)--(4.5). In particular `phi_Q in L^1`, so the density is continuous and vanishes at infinity. QED for branch 1.

#### Proof of the global-kernel branch

Assume `t_L=0` in addition to (4.1). Since `r_L=0`,

`r=C kappa`.                                                         (4.15)

Since `a_L=0`,

`a - 2 kappa^T C kappa + kappa^T C kappa=0`,

so

`a=kappa^T C kappa=r^T kappa`.                                      (4.16)

Now multiply the block matrix `A` by `h_0=(1,-kappa,0,0)`.

The four block rows are respectively

`a-r^T kappa=0`,

`r-C kappa=0`,

`s-B^T kappa=0`,

`t-E^T kappa=t_L=0`.                                                 (4.17)

Thus `A h_0=0`. QED.

## 5. Why this is a genuine advance over the previous local routing

The account03/B09 theorem had already shown, for the active five-variable chart, that a nonzero residual scalar square is paid, and that exact-zero square curvature with nonzero residual `u'` coefficient is paid. It then identified `a_L=r_L=0` as an exact kernel direction of the **five-coordinate principal block**.

Theorem 4.1 does not stop there. It keeps every outside original coordinate and proves that the five-block kernel direction either:

- has nonzero coupling `t_L` to the outside product bank, in which case the missing third Fourier resource is the scalar linear projection `t_L^T W` and the entire ambient form is paid by the explicit continuous-density bound (4.3); or
- has zero coupling to every outside coordinate, in which case the same vector is a kernel vector of the full matrix, not merely of the local principal block.

This is precisely the aggregate-before-conditioning repair suggested by the current corrections: conditioning away `W` first turns `t_L^T W` into a possibly tiny scalar and hides its product-law averaging. Retaining `W` until after the mass-sensitive Fourier estimate converts that apparent singularity into the integrable negative moment (4.13).

The theorem is still **not** the full conjecture. The bare three-large-eigenvalue hypothesis does not force a single physical invertible `2 x 2` packet with the scale product `||t_L|| |det B|^2` bounded below. Known diffuse/star examples rule out a naive fixed-minor extraction. The remaining global debt is therefore structural/aggregate: either extract enough total mass of such paid packets before reciprocal determinant payment, or route the matrix into the already completed diffuse/ridge/grouped-hyperbolic branches.

## 6. Designated partner account04/B02 applied to an actual Fourier inequality

The designated partner completed `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`, canonical proof

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

If a nonsingular physical `3 x 3` block `P` has a zero diagonal entry, it supplies the genuine global Fourier estimate

`A_2 := integral |phi_Q(tau)|^2 d tau
 <= 6 pi 2^(2/3) |det P|^(-1/3)`.                                   (6.1)

I now apply (6.1) to the overlap with Theorem 4.1.

Before optimizing the conditional low-frequency part, Lemma 3.1 gives for every fixed `w`

`integral_(|tau|>T)|phi_(Q|W=w)(tau)| d tau
 <= pi^(5/4)6^(3/4)|det B|^(-1/2)
    |t_L^T w|^(-1/4) T^(-1/4)`.                                    (6.2)

For a density cap `L`, (4.12) at `alpha=1/4` gives

`E |t_L^T W|^(-1/4)
 <= [2^(9/4)/3] L^(1/4)
 <= [2^(19/8)/3] ||t_L||_2^(-1/4)`.                                 (6.3)

Hence the global high-frequency tail obeys

`integral_(|tau|>T)|phi_Q(tau)| d tau <= K T^(-1/4)`,                (6.4)

where

`K = pi^(5/4)6^(3/4) [2^(19/8)/3]
     |det B|^(-1/2)||t_L||_2^(-1/4)`.                               (6.5)

On low frequencies, the *partner* estimate (6.1), not the trivial bound, gives

`integral_(|tau|<=T)|phi_Q(tau)| d tau
 <= sqrt(2 A_2 T)`.                                                   (6.6)

Let `A0=sqrt(2A_2)`. Optimizing

`A0 T^(1/2)+K T^(-1/4)`                                              (6.7)

at

`T=(K/(2A0))^(4/3)`                                                  (6.8)

gives

`||phi_Q||_1 <= 3*2^(-2/3) A0^(1/3)K^(2/3)`.                        (6.9)

Substituting (6.1) and (6.5), then dividing by `2 pi`, all powers simplify to the explicit overlap estimate

`boxed(
 ||p_Q||_infinity
 <= 3 * 2^(31/36)
    |det P|^(-1/18)
    |det B|^(-1/3)
    ||t_L||_2^(-1/6)
 )`,                                                                 (6.10)

whose numerical constant is

`3 * 2^(31/36)=5.449310176166419...`.                                (6.11)

This is an actual use of the designated partner result in a new inequality. The direct bound (4.3) may be numerically smaller in some coefficient regimes; (6.10) is useful because it explicitly combines a low-frequency `L^2` credit with the new high-frequency `L^1` tail and changes the exponents.

## 7. Relation to the assigned target-wide integrated Fourier question

This run still does **not** prove or refute the target-wide universal estimate

`sup_(A, laws) integral |E exp(i t X^T A X)| dt < infinity`

under only the three-large-eigenvalue hypothesis. I found no valid exact-target counterexample to that stronger criterion and therefore do not label it false.

What is proved is a new exact branchwise `L^1` theorem that pays the last local double-null survivor whenever its would-be kernel direction has any outside quadratic coupling. The proof is explicitly integrated in frequency and is compatible with the source correction that law-uniform pointwise one-dimensional quadratic-phase decay is false.

The first unpaid B02 implication is now sharper:

`QFORM-PAID-PACKET-OR-DIFFUSE-AGGREGATION-v1` — from `s_3(A)>=1`, produce a dimension-free aggregate certificate that either (i) carries enough total weight of physical invertible `2 x 2` packets with nontrivial outside coupling to use Theorem 4.1 before reciprocal-minor payment, or (ii) enters one of the completed diffuse/ridge/grouped-hyperbolic branches. A single uniformly good fixed minor is known not to be forced.

## 8. Status and correction compatibility

- Full QFORM conjecture: **OPEN**.
- Full target-wide unweighted `L^1` characteristic-function estimate: **OPEN / neither proved nor refuted here**.
- New Theorem 4.1: **proved supporting theorem**, arbitrary admissible input laws, no moments/support/log-concavity assumptions.
- Density regularity on branch `t_L!=0`: **continuous**, because the full characteristic function is `L^1`.
- Kernel branch `t_L=0`: exact algebraic statement only; it is not promoted to a density theorem.
- No post-rotation independence is used.
- No arbitrary-joint coarea lemma, conditional spectral density cap, fiber supremum, or law-uniform pointwise Fresnel decay is used.
- The current correction inbox and owner control were refreshed before publication; no later stop or target change was observed.

The constants and optimizer identities are checked separately in `check_r18.py` / `CHECK_RESULTS.txt`; those finite computations support arithmetic only, while the proof above is analytic.
