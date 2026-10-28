SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T22:28:55Z.
attacking: the source-shared puncture by a new physical-space conditional Lp/half-Riesz receiver; test whether a disjoint rough square carrier absorbs an arbitrary same-source shear without any b-loss.

# account01/B05 auto19 — shared remainder + disjoint square carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **SUPPORTING COAREA/LP THEOREM PROVED / PUNCTURE REMOVED ON A NEW PRODUCT-PRESERVING BRANCH / FULL QFORM OPEN**.  
Full-target continuity: **OPEN**. The theorem proved here has a canonical continuous `C_0` density.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target remains arbitrary independent ORIGINAL real coordinates with one-dimensional density caps at one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. Nothing below assumes Gaussianity, log-concavity, moments, compact support, connected support, identical laws, diagonal-basis independence, or post-rotation independence.


## 1. New theorem

### Theorem `QFORM-SHARED-REMAINDER-DISJOINT-SQUARE-v1`

Let `H,Y` be independent real random variables and independent of an arbitrary random object `Z`. Assume

`0 <= f_H <= m_H`, `0 <= f_Y <= m_Y`.

Let `A=A(Z)` be a real random variable having a density with

`||p_A||_infinity <= M_A`.

Let `R(Z),W(Z)` be arbitrary measurable real functions, with no independence required between `A,R,W`, and let `gamma != 0`. Put

`Q = 2 H A(Z) + R(Z) + gamma Y^2 + 2 W(Z)Y`.                     (1.1)

Then `Q` has a canonical density in `C_0(R)`. Two useful bounds hold.

First, the direct half-Riesz/coarea bound is

`boxed: ||p_Q||_infinity <= 4 sqrt(2) m_Y sqrt(m_H M_A) |gamma|^(-1/2).`    (1.2)

Second, for every `p>2`, writing `alpha=1-1/p`,

`boxed:
 ||p_Q||_infinity <=
 p 2^(1/p) ((p-1)/(p-2))^((p-1)/p)
 (m_H M_A)^alpha m_Y^(2/p) |gamma|^(-1/p).`                       (1.3)

In particular, at `p=3`,

`boxed: ||p_Q||_infinity <= 6 (m_H M_A)^(2/3) m_Y^(2/3) |gamma|^(-1/3).`   (1.4)

The essential point is that `R` and `W` may contain arbitrary same-source dependence on the scalar multiplier `A`. Only the genuine original scalar `Y`, carrying a nonzero square and absent from `A`, is separated.

### Proof of (1.2)

Fix `Z=z` outside a null set and abbreviate

`a=A(z)`, `r=R(z)`, `w=W(z)`.

The translated square

`S_z=gamma Y^2+2wY = gamma (Y+w/gamma)^2-w^2/gamma`

has a density satisfying, on its appropriate half-line,

`p_(S_z)(u) <= m_Y / sqrt(|gamma| |u+w^2/gamma|)`.                 (1.5)

For `a != 0`, convolving with `2aH+r` gives, for almost every `t`,

`p_(Q|Z=z)(t)
 <= (m_Y/sqrt(|gamma|))
    int f_H(h) |t-r+w^2/gamma-2ah|^(-1/2) dh`.                    (1.6)

For any probability density `0<=f<=m`, the one-dimensional bathtub/rearrangement estimate is

`sup_c int f(x)|x-c|^(-1/2) dx <= 2 sqrt(2m)`.                    (1.7)

Indeed the decreasing kernel is maximized by density `m` on the centered interval of length `1/m`, and its integral is exactly `2 sqrt(2m)`. Scaling (1.7) in (1.6) yields

`p_(Q|Z=z)(t) <= 2 m_Y sqrt(m_H) / (sqrt(|gamma|) sqrt(|a|)).`     (1.8)

Because `A` has an absolutely continuous law, `P(A=0)=0`. A second use of (1.7), now with the density `p_A<=M_A`, gives

`E |A|^(-1/2) <= 2 sqrt(2M_A)`.                                   (1.9)

Averaging (1.8) over `Z` proves (1.2). Notice that no conditional density of `A` is used and the arbitrary same-source pair `(R,W)` costs nothing: after `Z` is fixed it only shifts the linear and output centers of the disjoint square.

### Proof of the all-p estimate and continuity

Fix `p>2`, put `q=p/(p-1)` and `alpha=1-1/p`. For `a !=0`, the affine variable `2aH+r` has

`||p_(2aH+r)||_p <= m_H^alpha (2|a|)^(-alpha)`.                   (1.10)

For the translated square, let `g` be the shifted density of `Y`, so `g<=m_Y` and `int g=1`. Its square density obeys the exact two-branch formula. Writing `h(x)=g(x)+g(-x)`, one has `h<=2m_Y` and `int_0^infinity h=1`. Since `q<2`,

`||p_(S_z)||_q^q
 <= 2^(1-q)|gamma|^(1-q)
    int_0^infinity h(x)^q x^(1-q) dx`.                            (1.11)

Use `h^q <= (2m_Y)^(q-1)h`, then maximize the remaining decreasing weighted integral under `0<=h<=2m_Y`, `int h=1`. This gives

`||p_(S_z)||_q
 <= 2^(1/p) ((p-1)/(p-2))^((p-1)/p)
    m_Y^(2/p)|gamma|^(-1/p).`                                     (1.12)

Young-Hoelder convolution combines (1.10)-(1.12). Finally, another bathtub estimate gives the exact negative-moment budget

`E |A|^(-alpha)
 <= p 2^alpha M_A^alpha`.                                         (1.13)

The factors `2^-alpha` and `2^alpha` cancel, proving (1.3).

For almost every `z`, the conditional density is an `L^p*L^q` convolution and therefore belongs to `C_0(R)`. The product of its `L^p` and `L^q` norms is integrable by (1.13). The rough conditional-convolution compiler (`QFORM-ROUGH-CONDITIONAL-CONVOLUTION-C0-v1`, account04/B15) therefore applies directly: averaging the conditional convolution densities gives a canonical unconditional density in `C_0`, with the same norm budget. This continuity argument never evaluates an arbitrary density representative on a prescribed curve or surface.

## 2. Canonical B05 corollary: the source-shared shear costs zero if one square carrier misses the hub multiplier

Consider the exact null-hub normal form

`Q_b = 2HL + 2bLP + V^2`,                                        (2.1)

where `H` is an independent original scalar and `L,P,V` are simultaneous linear forms of the residual ORIGINAL independent coordinates. No independence among `L,P,V` is assumed.

Suppose there is one residual ORIGINAL coordinate `Y=X_j` such that its coefficient in `L` is zero but its coefficient `v_j` in `V` is nonzero. Condition on all residual coordinates other than `Y`; call them `Z`. Write

`L=L(Z)`, `P=p_jY+P_0(Z)`, `V=v_jY+V_0(Z)`.

Then

`2bLP+V^2
 = v_j^2 Y^2
 +2[v_jV_0+bLp_j]Y
 +[2bLP_0+V_0^2].`                                                (2.2)

Thus Theorem 1 applies with `A=L`, `gamma=v_j^2`, and arbitrary same-source functions `R,W`. If `H,Y` are cap one and `||p_L||_infinity<=M_L`, then for every real `b`, including `b=0`,

`boxed: ||p_(Q_b)||_infinity <= 4 sqrt(2) sqrt(M_L)/|v_j|,`        (2.3)

and the density is continuous and vanishes at infinity. The `p=3` companion is

`boxed: ||p_(Q_b)||_infinity <= 6 M_L^(2/3)|v_j|^(-2/3).`          (2.4)

This is uniform through the puncture `b->0`: all same-source dependence created by `2bLP` is absorbed into the random linear coefficient `W(Z)` of the genuinely disjoint square carrier.

## 3. Exact target-valid family and direct comparison with account02/B05

Take independent cap-one original variables

`H,X1,...,X6`,

and define

`L=(X1+X4)/sqrt(2)`,
`P=(X2+X5)/sqrt(2)`,
`V=(X3+X6)/sqrt(2)`.                                              (3.1)

The coefficient vectors of `L,P,V` are orthonormal, but no claim of independence is made because they are merely linear forms of the product source. In the orthonormal active basis `(H,L,P,V)`, the homogeneous matrix of (2.1) is

`B_b = [[0,1,0,0], [1,0,b,0], [0,b,0,0], [0,0,0,1]].`             (3.2)

Its characteristic polynomial is

`-lambda (lambda-1)(b^2-lambda^2+1)`,                             (3.3)

hence

`spec(B_b)={0,1,+sqrt(1+b^2),-sqrt(1+b^2)}.`                      (3.4)

So this is in the exact owner target for every `b`.

Choose the square carrier `Y=X3`. It is absent from `L`, and `v_j=1/sqrt(2)`. Also `L=(X1+X4)/sqrt(2)` has density cap at most `sqrt(2)` by elementary convolution of the two scaled cap-one marginals. Equation (2.3) therefore gives the explicit uniform target-valid estimate

`boxed: ||p_(Q_b)||_infinity <= 4 * 2^(5/4) < 9.514`              (3.5)

for every `b in R`, with a `C_0` density.

Now apply the designated partner account02/B05 theorem `QFORM-TWOBANK-HUB-PUNCTURED-COUPLING-v1` to this *same* family. Split the residual original coordinates into independent banks

`A=(X1,X2,X3)`, `B=(X4,X5,X6)`.

Each bank's `(L,V)` marginal has density cap at most `2`, and each `(L,V,P)` joint density cap is at most `2sqrt(2)`. Thus the partner currencies may be taken

`K_2=2`, `K_3=2sqrt(2)`, `K=2+2sqrt(2)`, `M_L<=sqrt(2)`, `m=1`.

With its `R=1` choice, for every `b!=0` the partner theorem gives the actual inequality

`boxed:
 ||p_(Q_b)||_(infinity,ess)
 <= 1/2 + sqrt(2)[2+sqrt(2)
      + log_2^+( C_T^2(2+2sqrt(2))^2/(32|b|) )].`                 (3.6)

The new physical-space receiver (3.5) removes that logarithmic puncture completely on this branch. Therefore the logarithm in the two-bank theorem is not forced by the mere presence of the source-shared shear `LP`; it is forced by the harder geometry in which every usable transverse square carrier also participates in the hub multiplier.

## 4. Relation to the newest Claude source and the precise remaining factor

The newest source commit `c4c23b784395630c094ba299a50712209921d1ae` rewrites a zero-diagonal hub with shear as a `hub that sees P` and isolates the adapted bathtub functional `(SP)`. The present theorem proves a concrete physical subcase of that philosophy without requiring a bound on the bad generic maximal functional: one first keeps a literal original square carrier `Y` out of `A`, conditions only the other original coordinates, and spends its square-root kernel against the honest one-dimensional marginal law of `A`.

The exact support condition `Y not in A` is essential to the argument. If the coefficient of `Y` in `A` is merely small but nonzero, conditioning on `Z` leaves a two-variable `(H,Y)` hyperbolic saddle. A rank-two saddle can have a logarithmically unbounded density, and under the owner's no-moment hypotheses a small coefficient cannot be treated as a small random perturbation. Thus this mechanism does **not** justify an `ell_j ->0` limiting argument.

The first unpaid implication is now

`QFORM-INFINITESIMAL-SQUARE-CARRIER-OVERLAP-GLUE-v1`:

> In the same-source punctured normal form, retain a transverse original square carrier whose coefficient in the hub multiplier is nonzero but arbitrarily small, and obtain a uniform interval/density bound by spending the third curvature before conditioning creates the rank-two saddle. The estimate must interpolate uniformly to Theorem 1 at zero overlap and to the existing punctured/two-bank receivers away from zero, without moments, conditional projection caps, arbitrary-joint coarea, or post-rotation independence.

This is the precise missing factor exposed by the present coarea calculation: **support incidence between the hub multiplier and the transverse square carrier**, not the size of the shear coefficient by itself.

## 5. Integrity / scope

- Full QFORM: `OPEN_NOT_PROVED_NOT_DISPROVED`.
- Full-target continuity: `OPEN`; continuity is proved here only on the stated branch.
- No Monte Carlo evidence is used.
- No input rotation is used to create independence.
- Conditioning is only on literal original coordinates.
- `R(Z),W(Z)` may be arbitrary same-source functions and may have no densities at all.
- The only residual-law input is the honest one-dimensional density cap of `A(Z)`.
- The theorem is homogeneous: the right side of (1.2) scales like inverse output scale.
- Repository transport was used; no authenticated native-brain receiver ingestion was observed, so execution remains `WITHOUT_VERIFIED_BRAIN`.

## Sources consumed

- Immediate B05 predecessor: `yspennstate/math-open-problems@8d747d7492ffa182d10810ea4493a17de687b6c8`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T221248Z-account01-B05-QFORM-auto18/REPORT.md`.
- Designated partner: `yspennstate/math-open-problems@3e2cfd317d73276f347d713292d5cba2ec0f3883`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T213321Z-account02-B05-QFORM-auto11e/REPORT.md`.
- Rough conditional-convolution compiler: account04/B15 `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T211918Z-account04-B15-rough-mixture-c0-r7/REPORT.md` on current master.
- Related physical pair precursor: account04/B15 `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T151702Z-account04-B15-pivoted-convolution-r6/REPORT.md`.
- Newest continuation source: `yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`.
