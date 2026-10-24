SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T02:32:24Z.
attacking: direct hub-edge entanglement in the critical two-hub packet by a joint mixed-norm Fourier compiler; preserve the phase-aligned pointwise-decay counterexample.

# account03/B01 — direct hub-edge entanglement via a joint mixed-norm compiler

Run: `20260924T023224Z-account03-B01-qform-auto11-r41`.

Status: **NEW AVERAGED-FREQUENCY THEOREM / DIRECT HUB-EDGE COUPLING PAID IN THE AFFINE-BASE-PHASE CHAMBER / FULL QFORM OPEN**.

Execution: `WITHOUT_VERIFIED_BRAIN`.

Continuity: **proved for the scoped theorem below; unrestricted target continuity remains OPEN.**

## 1. Control, scope, and correction boundary

Fresh `yspennstate/math-research-brain` main was read, including `AGENTS.md`, the full scheduled-task owner control/message, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, the QFORM manifest/current-research/claims/correction inbox/memory protocol, and this worker's assignment. OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole target and the full conjecture is still open.

No step below assumes Gaussianity, log-concavity, moments, compact or connected support, smooth densities, or independence after a spectral rotation. Every random coordinate used below is an original coordinate or a source-disjoint block of original coordinates. No uniform pointwise van-der-Corput/Fresnel estimate is used.

The phase-aligned obstruction is retained: for every prescribed `s>0` and every small `eta>0`, the set

`E={x: dist(s x^2,2 pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite union of intervals `F subset E` with total length one and set `f=1_F`. Then `f` is an admissible probability density and

`Re E exp(i s X^2) >= cos(eta)`.

Thus no law-uniform positive-power pointwise quadratic-phase decay follows from `f<=1`.

## 2. Source-valid inputs

### 2.1 Two-original-hub Plancherel envelope

The completed account01/B01 critical two-hub theorem used by account04/B01 and by the preceding account03/B01 run proves the following original-coordinate statement. If `H=(H1,H2)` are two independent cap-one hub variables, `a_t(s)` is a complex density on `R^2`, and

`Phi(t)=int f_H(h) exp(i t h^T C h) [int exp(i 2t h.s) a_t(s) ds] dh`,

then for `t!=0`,

`|Phi(t)| <= pi |t|^(-1) ||a_t||_2`.                                      (2.1)

The proof is ordinary two-dimensional Plancherel in the original hub coordinates. It tolerates arbitrary same-hub quadratic curvature `C` and complex `a_t`.

### 2.2 Fresh designated partner account04/B01

The newest completed designated partner source is

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

For every `1<r<=2`, put

`alpha=(r-1)/r`, `r'=r/(r-1)`.

For two independent cap-one original coordinates `U,V` and

`Z=2cUV+beta U+gamma V+delta`, `c!=0`,

account04/B01 proves

`||p_Z||_r <= 2^alpha |c|^(-alpha)`.                                (2.2)

The estimate is uniform in all affine coefficients. This run applies (2.2) after an explicit slope-residual shear; it is not merely cited.

## 3. New mixed-norm joint-density compiler

### Theorem `QFORM-TWO-HUB-JOINT-MIXED-LR-v1`

Let `H=(H1,H2)` be two independent cap-one original coordinates. Let `(S,Z)` be an `R^2 x R` random vector independent of `H`, with joint density `rho(s,z)`. Fix `1<r<=2` and write `r'=r/(r-1)` and `alpha=(r-1)/r`. Assume

`M_r := ||rho||_{L_z^r L_s^2}
      = [ int_R ( int_R2 rho(s,z)^2 ds )^(r/2) dz ]^(1/r) < infinity`.   (3.1)

Let `C` be an arbitrary real symmetric `2x2` matrix and put

`Q=H^T C H+2 H^T S+Z`.                                                (3.2)

Then `phi_Q in L^1(R)`, so `Q` has a continuous `C_0` density. More explicitly,

`||p_Q||_infinity <= C_joint(r) M_r^theta`,                            (3.3)

where

`theta=1/(1+alpha)=r/(2r-1)`,                                         (3.4)

and

`C_joint(r)
 = (1+alpha)/(pi alpha)
   [ (alpha pi/2) (2/(r-1))^(1/r) (2pi)^alpha ]^theta`.               (3.5)

At `r=2`,

`||p_Q||_infinity <= 3*2^(-2/3) ||rho||_2^(2/3)`.                     (3.6)

#### Proof

For fixed `t`, Fourier transform the joint density only in its scalar coordinate:

`a_t(s)=int_R exp(i t z) rho(s,z) dz`.                                 (3.7)

Hausdorff--Young in `z`, with Fourier convention `hat f(t)=int exp(itx)f(x)dx`, gives for each fixed `s`

`||a_.(s)||_(r') <= (2pi)^alpha ||rho(s,.)||_r`.                       (3.8)

Because `r<=2`, Minkowski's integral inequality gives

`||rho||_{L_s^2 L_z^r} <= ||rho||_{L_z^r L_s^2}=M_r`.                 (3.9)

Because `r'>=2`, Minkowski in the opposite order gives

`|| ||a_t||_(L_s^2) ||_(L_t^(r'))
 <= ||a||_(L_s^2 L_t^(r'))
 <= (2pi)^alpha M_r`.                                                  (3.10)

Applying the two-hub envelope (2.1),

`|phi_Q(t)| <= pi |t|^(-1) ||a_t||_2`.                                (3.11)

For any `T>0`, Holder in frequency with conjugate exponents `r` and `r'` yields

`int_R |phi_Q(t)| dt
 <= 2T + pi (2/(r-1))^(1/r) (2pi)^alpha M_r T^(-alpha)`.              (3.12)

Set

`L=pi (2/(r-1))^(1/r) (2pi)^alpha M_r`.                               (3.13)

The minimum of `2T+L T^(-alpha)` occurs at

`T_*=(alpha L/2)^theta`.                                               (3.14)

At the minimizer, `L T_*^(-alpha)=2T_*/alpha`. Fourier inversion then gives exactly (3.3)-(3.5). In particular the characteristic function is integrable, so the density is continuous and vanishes at infinity. QED.

## 4. Random slope shifts cost nothing if the base phase is affine in the base slope

The preceding theorem becomes useful because the required mixed norm survives an arbitrary random **slope shift** correlated with the smoothing residual.

### Lemma `QFORM-SLOPE-SHIFT-MIXED-NORM-v1`

Let `S0 in R^2` have probability density `p0` with

`K=||p0||_infinity`.                                                   (4.1)

Let `(T,Z')`, with `T in R^2`, be any random vector independent of `S0`; no density of `T` or joint density of `(T,Z')` is assumed. Suppose only that `Z'` has density `q in L^r(R)`, `1<r<=2`. Put

`S=S0+T`.                                                              (4.2)

Then `(S,Z')` has a joint density `rho`, and

`||rho||_{L_z^r L_s^2} <= K^(1/2) ||q||_r`.                           (4.3)

#### Proof

Disintegrate the law of `T` conditional on `Z'=z`; call the conditional probability measure `nu_z`. For almost every `z`,

`rho(s,z)=q(z) int_R2 p0(s-t) nu_z(dt)`.                              (4.4)

A probability mixture of translates cannot increase the `L^2` norm, hence

`||rho(.,z)||_2 <= q(z)||p0||_2 <= q(z) K^(1/2)`,                     (4.5)

because `int p0=1` and `p0<=K`. Taking the `L^r` norm in `z` proves (4.3). QED.

Now allow a scalar base phase affine in the base slope:

`R0(Y)=ell.S0(Y)+r0`.                                                  (4.6)

If a source-disjoint bank `W` produces `(T(W),Z(W))`, define

`Z'=Z-ell.T`.                                                         (4.7)

Then

`R0+Z = ell.(S0+T)+r0+Z' = ell.S+r0+Z'`.                              (4.8)

The shear `(s,z')->(s,ell.s+r0+z')` preserves every mixed norm appearing above. Therefore Theorem 3 and Lemma 4 give

`||p_Q||_infinity
 <= C_joint(r) [K^(1/2)||p_(Z-ell.T)||_r]^theta`                      (4.9)

for

`Q=H^T C H+2H^T(S0+T)+ell.S0+r0+Z`.                                 (4.10)

This is the first B01 payment that permits the smoothing variables themselves to couple directly back into **both** hub slopes through an arbitrary random two-vector `T`.

## 5. Fresh partner result applied: fully hub-coupled hyperbolic edge

Let the source split be `H | Y | U | V`, all original-coordinate groups independent. Let

`S0(Y)=BY+d`, `rank(B)=2`, `D=det(BB^T)>0`,                            (5.1)

and suppose the same-bank scalar phase is affine in this slope,

`R0(Y)=ell.S0(Y)+r0`.                                                  (5.2)

Allow the two smoothing coordinates to couple arbitrarily back into the two hubs:

`T(U,V)=a U+b V`, with arbitrary `a,b in R^2`.                        (5.3)

Let

`Z(U,V)=2cUV+beta U+gamma V+delta`, `c!=0`.                           (5.4)

Thus

`Q=H^T C H+2H^T(BY+d+aU+bV)+ell.(BY+d)+r0
   +2cUV+beta U+gamma V+delta`.                                      (5.5)

After the shear (4.7),

`Z'=2cUV+(beta-ell.a)U+(gamma-ell.b)V+delta`.                         (5.6)

This is exactly the affine hyperbolic form in the fresh account04/B01 theorem. Applying the partner result (2.2) at the actual inequality gives

`||p_Z'||_r <= 2^alpha |c|^(-alpha)`.                                (5.7)

The completed two-dimensional product projection estimate gives

`K<=2 D^(-1/2)`.                                                       (5.8)

Substitution into (4.9) yields the new theorem

### `QFORM-TWO-HUB-FULL-SLOPE-ENTANGLED-HYPERBOLIC-v1`

For every `1<r<=2`,

`||p_Q||_infinity
 <= C_r D^(-r/[4(2r-1)]) |c|^(-(r-1)/(2r-1))`,                      (5.9)

where

`C_r=(1+alpha)/(pi alpha)
    [ (alpha pi/2) (2/(r-1))^(1/r)
      (2pi)^alpha 2^(alpha+1/2) ]^(r/(2r-1))`.                       (5.10)

The density is continuous and belongs to `C_0`.

At `r=2`, all constants collapse exactly to

`boxed: ||p_Q||_infinity <= 3 D^(-1/6)|c|^(-1/3).`                   (5.11)

Thus arbitrary direct hub couplings `2H^T(aU+bV)` cost **no constant and no scale exponent** relative to the source-disjoint account04/B01 hyperbolic-edge theorem, provided the base same-bank phase is affine in the base two-dimensional slope.

The scaling is exact: under `A -> lambda A`, `D -> lambda^4 D` and `c -> lambda c`, and

`4*r/[4(2r-1)] + (r-1)/(2r-1)=1`.                                   (5.12)

## 6. Reciprocal-power scale cancellation survives the direct hub coupling

Suppose

`BB^T=k^2 I_2`, hence `D=k^4`, and `c=k^(-q0)` for fixed `q0>=2`.      (6.1)

Choose

`r=q0/(q0-1)`.                                                        (6.2)

Then the exponent of `k` in (5.9) is

`-r/(2r-1)+q0(r-1)/(2r-1)=0`.                                       (6.3)

Therefore the density is uniformly bounded in `k`, even though the same hyperbolic variables also enter both hub slopes. The exact constants from (5.10) are

- `q0=2`, `r=2`: `C_r=3`;
- `q0=3`, `r=3/2`: `C_r=3.82717036769197...`;
- `q0=4`, `r=4/3`: `C_r=4.83295511232941...`.

This extends the partner's strict-N3 scale-cancellation mechanism to a genuinely hub-entangled packet.

## 7. Concrete target-valid coupled stress family

Take six original coordinates ordered `(H1,H2,Y1,Y2,U,V)` and the coefficient matrix

```
A = [[0,0,1,0,1,0],
     [0,0,0,1,0,1],
     [1,0,0,0,0,0],
     [0,1,0,0,0,0],
     [1,0,0,0,0,1],
     [0,1,0,0,1,0]].
```

Then `B=I_2`, `a=e1`, `b=e2`, `c=1`, and the base same-bank phase is zero, so (5.11) gives

`||p_(X^T A X)||_infinity <=3`                                       (7.1)

for **every** independent cap-one input law, with a continuous density. The numerical spectrum is

`-1.801937735805, -1.246979603717, -0.445041867913,
  0.445041867913,  1.246979603717,  1.801937735805`,                 (7.2)

so four eigenvalues have absolute value at least one. This is therefore a genuine target-valid nonseparable, directly hub-entangled example, not an easy diagonal control.

## 8. Averaged-frequency interpretation

The proof gives an actual `L^1` characteristic-function bound, stronger than merely a signed Fejer estimate. Equation (3.12), optimized at (3.14), is the replacement for false pointwise quadratic decay. In particular every triangular/signed Fejer average is bounded by the same density constant in (5.9). The gain occurs by integrating the scalar residual frequency in a mixed norm **before** the critical two-hub `|t|^-1` envelope is integrated.

No claim of an absolute pointwise `|t|^-3/2` envelope is made.

## 9. Exact remaining implication

The preceding account03/B01 run identified direct terms `2H^T(aU+bV)` as the next analytic obstruction. This run shows that those terms themselves are not the obstruction: they are free under the slope-residual mixed norm once the base same-bank phase is affine in the two-dimensional base slope.

The still-unpaid interface is now simultaneous

1. nonlinear/quadratic same-bank curvature `R(Y)` not affine in `S0=BY+d`, **and**
2. direct random hub-slope shift `T(W)` correlated with the scalar smoothing residual.

In Fourier language, the two independent source blocks then contribute two graph measures in `R^3`; the available bounds are transverse mixed norms, and a naive product of their separate `L^2` slice estimates can concentrate along the same frequency-slope diagonal. The next B01 target is therefore

`QFORM-TWO-GRAPH-MIXED-NORM-TRANSVERSALITY-v1`:

prove a dimension-free convolution/mixed-norm estimate for

`(S0(Y),R(Y)) + (T(W),Z(W))`

under the actual quadratic structure, or route the simultaneous nonlinear/entangled case to an existing rank-three cross-volume receiver. A generic arbitrary-graph convolution estimate is not asserted here.

Full QFORM remains OPEN.

## 10. Deterministic checks

The sibling `CHECKS.txt` records the actual numerical/algebraic check output. It verifies the endpoint constant, partner/projection constant cancellation to exactly three, the scale exponent for `q0=2,3,4`, and the target-valid stress spectrum. It ends `STATUS=PASS`.

## 11. Source pins

- Fresh owner/control source: `yspennstate/math-research-brain`, OWNER CONTROL revision `2026-09-22.15`; QFORM-only.
- Fresh designated partner: `yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`, account04/B01 L^r residual theorem.
- Previous account03/B01 conditional-L^r source: `yspennstate/math-open-problems@02fc25c9017e7ff987ca1726cd542bd83cc1f103`.
- Pointwise phase-aligned correction retained; no refuted conditional-cap/coarea or post-rotation independence premise is used.

Repository transport is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
