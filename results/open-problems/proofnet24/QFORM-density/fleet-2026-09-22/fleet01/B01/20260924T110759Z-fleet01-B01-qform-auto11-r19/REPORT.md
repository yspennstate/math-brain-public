SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-24T11:07:59.362602Z.
attacking: QFORM-SIGNED-PUNCTURE-INTERPOLATION-v1 by averaging the scalar quadratic phase over the full random row modulation before taking any reciprocal coefficient.

# fleet01/B01 — random-modulation smoothing through the zero-curvature puncture

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T110759Z-fleet01-B01-qform-auto11-r19`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING AVERAGED-FREQUENCY THEOREMS / FULL QFORM OPEN**

## 1. Scope and correction boundary

All displayed source coordinates are ORIGINAL independent real random variables with probability densities bounded by one unless a different density cap is stated explicitly. No Gaussianity, moment bound, log-concavity, compact/connected support, smoothness, post-rotation independence, or diagonal-basis assumption is used.

The phase-aligned fragmented-support obstruction is preserved. For every prescribed nonzero frequency `tau` and every `eta>0`, one can choose a finite union `E` of intervals of total length one inside

`{x: dist(tau x^2,2 pi Z)<eta}`

and take `f=1_E`, giving `Re E exp(i tau X^2)>=cos eta`. Hence no law-uniform pointwise positive-power decay for a bare scalar quadratic phase is used below.

The new mechanism is different: a genuinely random linear modulation of the scalar phase is integrated *before* any absolute reciprocal is taken. The resulting Plancherel estimate is uniform in the scalar quadratic curvature, including at curvature zero.

The unrestricted three-large-eigenvalue conjecture remains OPEN. The general continuous-density conclusion remains OPEN.

## 2. Random modulation gives a curvature-uniform `t^{-1/2}` envelope

Let `H` be independent of a random vector `Y`. Assume `H` has density `0<=f<=1`. Let `L=L(Y)` be a real random variable having a density `p_L` with

`||p_L||_infinity <= M < infinity`,

and let `T=T(Y)` be arbitrary measurable; in particular, `T` may be fully correlated with `L`. For an arbitrary real number `a`, define

`R = a H^2 + 2 H L + T`.                                           (2.1)

For `t!=0` and real `w`, put

`G_(a,w)(t)=int_R f(h) exp(i t(a h^2+2 w h)) dh`.                  (2.2)

### Theorem 2.1 — `QFORM-RANDOM-MODULATION-FOURIER-v1`

For every real `a`, every `t!=0`, and every admissible law above,

`boxed: |phi_R(t)| <= min{1, sqrt(pi M/|t|)}.`                      (2.3)

The estimate is completely uniform as `a` passes through zero.

#### Proof

Condition on `Y`:

`phi_R(t)=E_Y [ exp(i t T(Y)) G_(a,L(Y))(t) ].`                    (2.4)

For fixed `t`, define

`g_t(h)=f(h) exp(i t a h^2)`.

As a function of the modulation variable `w`,

`G_(a,w)(t)=hat g_t(2 t w)`                                      (2.5)

for the Fourier convention `hat g(s)=int exp(i s h)g(h)dh`. By Plancherel and the change of variables `s=2tw`,

`int_R |G_(a,w)(t)|^2 dw
 = (1/(2|t|)) int_R |hat g_t(s)|^2 ds
 = (pi/|t|) int_R f(h)^2 dh
 <= pi/|t|`,                                                     (2.6)

because `0<=f<=1` and `int f=1`. Cauchy--Schwarz in (2.4), followed by the density cap for `L`, gives

`|phi_R(t)|^2
 <= E |G_(a,L)(t)|^2
 <= M int |G_(a,w)(t)|^2 dw
 <= pi M/|t|`.                                                   (2.7)

Together with `|phi_R(t)|<=1`, this proves (2.3). QED.

### Why this does not contradict the phase-aligned counterexample

For a fixed deterministic `w`, the factor `G_(a,w)(t)` can be close to one at an arbitrarily prescribed large frequency under a fragmented cap-one density. Theorem 2.1 does not prohibit that. It averages the *whole modulation parameter* `w=L(Y)` against a bounded density and uses the exact Plancherel identity (2.6). Thus the smoothing is joint in the scalar source and its random row modulation, not a scalar van-der-Corput assertion.

## 3. Uniform sub-half-Riesz potential through `a=0`

For a real random variable `Z`, write

`H_gamma(Z)=sup_s E |Z-s|^(-gamma)`.

### Theorem 3.1 — `QFORM-RANDOM-MODULATION-SUBHALF-RIESZ-v1`

Under the assumptions of Theorem 2.1, for every `0<gamma<1/2`,

`boxed:
 H_gamma(R)
 <= C_gamma M^gamma,`                                            (3.1)

where

`C_gamma = pi^gamma /
 [2 Gamma(gamma) cos(pi gamma/2) gamma(1/2-gamma)].`             (3.2)

At `gamma=1/4`,

`boxed: H_(1/4)(R)
 <= 3.179662567631707 M^(1/4).`                                  (3.3)

#### Proof

For `0<gamma<1`, the one-dimensional Riesz kernel has the Fourier representation, in the Abel-regularized sense,

`|x|^(-gamma)
 = [2 Gamma(gamma) cos(pi gamma/2)]^(-1)
   int_R exp(i t x)|t|^(gamma-1) dt`.                            (3.4)

The bound (2.3) makes the corresponding frequency integral absolutely convergent both at zero and infinity whenever `0<gamma<1/2`; therefore Abel regularization and dominated convergence give, uniformly in `s`,

`E|R-s|^(-gamma)
 <= [2 Gamma(gamma) cos(pi gamma/2)]^(-1)
    int_R |t|^(gamma-1)
    min{1,sqrt(pi M/|t|)} dt`.                                  (3.5)

Put `B=sqrt(pi M)`. Splitting at `|t|=B^2` gives exactly

`int_R |t|^(gamma-1) min{1,B|t|^(-1/2)} dt
 = B^(2gamma)/[gamma(1/2-gamma)].`                              (3.6)

Substitution into (3.5) proves (3.1)-(3.2). At `gamma=1/4`, evaluation gives the constant in (3.3). QED.

### Original-coordinate row corollary

Suppose

`L = sum_j c_j Y_j + ell`,

where the `Y_j` are independent ORIGINAL coordinates with density caps one, and put

`c=(sum_j c_j^2)^(1/2)>0`.                                     (3.7)

The completed product-projection estimate used in fleet02/B01's zero-diagonal row theorem gives

`||p_L||_infinity <= sqrt(2)/c`.                               (3.8)

Hence, for arbitrary real `a` and arbitrary quadratic-plus-affine `T(Y)`, including arbitrary correlation between `T` and `L`,

`boxed:
 H_(1/4)(aH^2+2HL+T)
 <=3.179662567631707 (sqrt(2)/c)^(1/4).`                        (3.9)

In the partner's current diffuse-row survivor, `c>=31/64`, so (3.9) gives the explicit uniform estimate

`H_(1/4)(R) <= 4.156371456630196`,                              (3.10)

with no deterioration as `a` passes through `0` and no dependence on the largest individual edge.

This does **not** by itself close the partner's one-outer-square punctured branch, because the target interface there needs a half-Riesz potential rather than a quarter-Riesz potential.

## 4. The exponent `1/2` is genuinely critical under only random modulation

The restriction `gamma<1/2` in Theorem 3.1 cannot be removed without spending additional structure.

Take independent `H,Y ~ Uniform[-1/2,1/2]` and let

`a=1`, `L=Y`, `T=Y^2`.

Then

`R=H^2+2HY+Y^2=(H+Y)^2`.                                      (4.1)

The sum `W=H+Y` has triangular density `p_W(w)=1-|w|` for `|w|<=1`. Therefore

`H_(1/2)(R) >= E|R|^(-1/2)
 = E|W|^(-1)
 = infinity`.                                                   (4.2)

Thus the logarithmic endpoint divergence is real even though `L` has density cap one. This example is **not** a counterexample to QFORM: its two-coordinate quadratic coefficient has rank one, with only one nonzero eigenvalue. It identifies exactly why the inherited second spectral direction must be spent to reach the half-Riesz endpoint.

## 5. One further original square converts the uniform quarter-Riesz budget to `L^infinity`

The preceding endpoint obstruction suggests spending a second literal scalar square rather than trying to force Theorem 3.1 to the false endpoint.

We first record the elementary square-fractional upgrade. Let `X` have density at most one and be independent of all later variables. If `m` is measurable in the later variables, `b!=0`, `Z` is any later random variable, and `0<beta<1/2`, then

`boxed:
 H_(beta+1/2)( b(X+m)^2+Z )
 <= |b|^(-1/2) J_beta H_beta(Z),`                              (5.1)

where

`J_beta = max{
 B(1/2,beta),
 B(1/2,1/2-beta)+B(1/2-beta,beta)
}.`                                                             (5.2)

Indeed, condition on the later variables and bound the scalar density by one. After translation and scaling, the required integral is

`int_R |y^2-delta|^(-(beta+1/2))dy`

or its no-real-root analogue. Scaling by `|delta|^(1/2)` gives `|delta|^(-beta)`, and the two beta integrals in (5.2) are exactly the root and no-root cases.

At `beta=1/4`,

`J_(1/4)=12.660413817789728`.                                  (5.3)

### Theorem 5.1 — `QFORM-TWOPIVOT-DIFFUSEROW-LINF-v1`

Let `X_0,X_1,H,Y` be source-disjoint ORIGINAL product banks. Allow triangular shifts `m_1=m_1(H,Y)` and `m_0=m_0(X_1,H,Y)`. Let

`Q = b_0 (X_0+m_0)^2
   + b_1 (X_1+m_1)^2
   + a H^2 + 2 H L(Y) + T(Y)`,                                (5.4)

where `b_0 b_1 !=0`, `a` is arbitrary, `T` is arbitrary measurable, and `L(Y)` has density cap `M`. Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 11.745890746379832
    |b_0|^(-1/2)|b_1|^(-1/3) M^(1/6).`                        (5.5)

If `L=sum c_jY_j+ell` with independent cap-one ORIGINAL `Y_j` and row norm `c=(sum c_j^2)^(1/2)`, then

`boxed:
 ||p_Q||_infinity
 <= 12.444337756165789
    |b_0|^(-1/2)|b_1|^(-1/3)c^(-1/6).`                        (5.6)

#### Proof

Apply Theorem 3.1 with `gamma=1/4` to the last three terms in (5.4). Then (5.1) with `beta=1/4` gives an `H_(3/4)` bound after the `X_1` square. Lyapunov's inequality gives

`H_(1/2)(Y_*) <= H_(3/4)(Y_*)^(2/3)`.                         (5.7)

Finally, conditional on all later variables, the translated scalar square `b_0(X_0+m_0)^2` has density envelope

`|b_0|^(-1/2)|q-Y_*|^(-1/2)`,                                  (5.8)

so averaging yields

`||p_Q||_infinity <= |b_0|^(-1/2) H_(1/2)(Y_*)`.               (5.9)

Combining (3.3), (5.1), (5.3), (5.7), and (5.9) gives

`[12.660413817789728 * 3.179662567631707]^(2/3)
 =11.745890746379832`,                                         (5.10)

which is (5.5). Substituting `M<=sqrt(2)/c` gives (5.6). QED.

The coefficient exponents in (5.6) have total homogeneity

`1/2+1/3+1/6=1`,

so the estimate has the correct quadratic scaling. For example, if `|b_0|,|b_1|,c>=1/64`, then (5.6) is `<796.438`.

## 6. Strict full-target stress family crossing the puncture

For every `m>=1` and every real `epsilon`, let all displayed variables be independent cap-one coordinates and define

`Q_(epsilon,m)
 = X_0^2 + Z^2 + epsilon H^2
   + 2 H m^(-1/2) sum_(j=1)^m Y_j`.                            (6.1)

The star slope vector has Euclidean norm one. On the two-dimensional span of `H` and the normalized bank direction, the coefficient matrix is

`[[epsilon,1],[1,0]]`,                                         (6.2)

with eigenvalues

`lambda_+/-=(epsilon +/- sqrt(epsilon^2+4))/2`,
`lambda_+ lambda_-=-1`.                                        (6.3)

Hence at least one of `|lambda_+|,|lambda_-|` is at least one. Together with the two literal eigenvalues `1` from `X_0^2` and `Z^2`, the full coefficient has at least three eigenvalues of modulus at least one for **every** `epsilon`, including `epsilon=0`.

Here

`L=m^(-1/2) sum_j Y_j`, `c=1`.                                 (6.4)

Theorem 5.1 therefore gives the target-valid uniform inequality

`boxed:
 ||p_(Q_(epsilon,m))||_infinity
 < 12.445`                                                     (6.5)

for every `m`, every real `epsilon`, and every admissible product law. The estimate is completely insensitive to the passage of the hub diagonal through zero.

## 7. Designated partner applied to an actual inequality

The freshest completed designated-partner report available before publication is fleet02/B01

`QFORM-TWOLEVEL-PIVOT-HALFRIESZ-v1`

inside

`yspennstate/math-open-problems@f2bb4e5d3f65c19715e6cbad2e79d7c071d6b174`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260924T091804Z-fleet02-B01-qform-auto11/REPORT.md`.

It states: if a residual quadratic-plus-affine coefficient `S` has `s_2(S)>=rho>0` and a literal physical diagonal `d!=0`, then

`H_(1/2)(R)
 <=8|d|^(-1/2)
   +32 sqrt(5) 4^(-1/8) rho^(-1/8)|d|^(-3/8).`                 (7.1)

Apply this to the strict target family (6.1) after peeling the outer square `X_0^2`. The residual contains the literal `Z^2` pivot `d=1`. Its singular spectrum contains `1` from `Z` and at least one star singular value at least one by (6.3), so

`s_2(S)>=1`.                                                    (7.2)

Thus the partner theorem gives the actual inequality

`boxed:
 ||p_(Q_(epsilon,m))||_infinity
 <= 8+32 sqrt(5) 4^(-1/8)
 =68.1696494893823...`                                         (7.3)

uniformly in `m`, `epsilon`, and all admissible input laws. The new theorem (6.5) then improves this same target family to `<12.445` by spending the aggregate row modulation directly.

This is equation-level use of the designated partner result, not merely a citation.

## 8. What is paid and what remains

The run establishes a useful replacement for the false pointwise scalar bound:

- a random original-coordinate row modulation with density cap `M` yields the curvature-uniform envelope `|phi(t)|<=sqrt(pi M/|t|)`;
- therefore every fractional potential `H_gamma`, `gamma<1/2`, is uniformly controlled through the zero-curvature puncture;
- a further literal original scalar square converts the `gamma=1/4` budget into a half-Riesz estimate, and one outer square into an `L^infinity` density bound;
- the mechanism aggregates the whole row norm before inversion and is stable as the row diagonal passes through zero.

The sharp example (4.1) shows that random modulation alone cannot universally supply the missing half-Riesz endpoint. Therefore the first unpaid implication is now

`QFORM-PUNCTURE-SECOND-SPECTRAL-DIRECTION-TO-HALFRIESZ-v2`:

in the partner's exact one-outer-pivot diffuse-row survivor (`0<|S_ii|<1/64`, row norm at least `31/64`, `s_2(S)>=1`), spend the inherited second spectral direction *without requiring an additional literal square*, so as to upgrade the curvature-uniform sub-half-Riesz budget to `H_(1/2)` while retaining arbitrary leaf curvature and product provenance.

A solution of that implication would close the partner's punctured diffuse-row branch. Structural routing of every full target matrix to a paid branch would still have to be checked separately.

Full QFORM status: **OPEN**.  
Full-target continuity status: **OPEN**.

## 9. Source pins and integrity


Previous B01 signed-cell theorem:
`yspennstate/math-open-problems@de33e9a351f65e5ccb6ef40115b148de1a1214f8`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260924T101817Z-fleet01-B01-qform-auto11-r19/REPORT.md`.

Designated partner theorem actually applied:
`yspennstate/math-open-problems@f2bb4e5d3f65c19715e6cbad2e79d7c071d6b174`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260924T091804Z-fleet02-B01-qform-auto11/REPORT.md`.

A narrow changed-file review found only mathematical text, logical account/slot identifiers, and source commit/path pins; no credentials, tokens, private personal material, machine paths, notification changes, scheduler mutations, or public-release action are present.
