SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T07:30:34Z.
attacking: aggregate disjoint-tetrad half-Riesz currency; after a fresh source-match ended duplication, pivot to a Frostman/Riesz-to-Fejer averaged-frequency compiler and apply it to the full coupled quadratic form.

# account03/B01 r47 — critical Fejer replacement after source-match

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Oscillatory replacement / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW UNIVERSAL SIGNED-FREQUENCY ESTIMATE + NEW RIESZ-TO-FEJER COMPILER / FULL QFORM OPEN**

## 1. Fresh scope and source-match

The owner target remains: for every finite `n`, independent real original-coordinate variables with densities bounded by one, and every real symmetric `A` with `s_3(A)>=1`, prove a dimension- and law-independent `L^infinity` density bound for `X^TAX`, or give a counterexample. No moment, Gaussian, iid, compact-support, connected-support, log-concavity, or post-rotation independence assumption is made.

Fresh prepublication control was resolved on `yspennstate/math-research-brain/main` through `27f2bf73653e285eb2972f8e9ab69b3e667b8e07`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no pause for this slot. The live correction inbox was refreshed. In particular, this run does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, conditional projected-density caps, or a fixed-good-minor assertion.

The run began by targeting aggregate disjoint-tetrad half-Riesz currency. Fresh source resolution found that account01/B01 had already completed exactly that scope before this proof was written:

`yspennstate/math-open-problems@0d074396abdd021a817f0b8dc104b826f2d7154d`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260924T072033Z-account01-B01-qform-auto11-r15/REPORT.md`.

Its theorem `QFORM-DISJOINT-TETRAD-AGGREGATE-HALFRIESZ-v1` states that, for

`R=X^T B X+ell^T X+c`

and the ordered disjoint-tetrad energy

`W_2^dis(B)=sum_{|I|=|J|=2, I cap J=empty} det B[I,J]^2`,

one has

`H_(1/2)(R):=sup_y E|R-y|^(-1/2)
 <=8 sqrt(2) e^(1/4) [W_2^dis(B)]^(-1/8)`.                         (1.1)

It also proves the exact scalar-Schur transfer to rooted overlap-one physical `3x3` determinant energy. Per the owner rule, I do not duplicate that proof. The successor below converts this new half-Riesz currency into an explicit signed-frequency estimate, and then obtains a stronger near-critical estimate directly for every nonzero coupled quadratic form.

A second input is the preceding account03/B01 theorem

`yspennstate/math-open-problems@7b617d334690a672477a5cd834bf27731d262ef4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T063007Z-account03-B01-qform-auto11-r46/REPORT.md`.

For every nonzero symmetric `S`, arbitrary affine term, `s=||S||_op`, and

`R=X^T S X+b^T X+gamma`,

it proves for every interval of length `h<=s/12`

`P(R in I)
 <=sqrt(12(h/s)[1+log(s/(12h))]).`                                (1.2)

All variables in (1.1)-(1.2) are original product coordinates.

## 2. Preserve the phase-aligned obstruction

Fix a prescribed nonzero frequency `tau` and `eta in (0,pi/2)`. The set

`E={x:dist(tau x^2,2pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite union `E_0 subset E` of total measure one and put `f=1_(E_0)`. Then `f` is an admissible cap-one probability density and

`Re E exp(i tau X^2)>=cos(eta)`.                                  (2.1)

Thus no positive law-uniform pointwise power decay in `|tau|` is available, even before coupling. Every result below is an averaged-frequency/distributional statement.

## 3. General Riesz-to-Fejer compiler

For a probability measure `mu` on `R`, use the standard triangular signed-frequency average

`D_T mu(y)
 =(1/(2pi)) int_{-T}^T (1-|t|/T) e^(-ity) phi_mu(t) dt`,            (3.1)

`T>0`. Fourier inversion of the triangular multiplier gives the positive Fejer kernel

`K_T(u)=(1-cos(Tu))/(pi T u^2)`,
`K_T(0)=T/(2pi)`,                                                   (3.2)

so `D_T mu=K_T*mu` and `int K_T=1`.

### Theorem 3.1 — `QFORM-RIESZ-TO-FEJER-v1`

For `0<beta<2`, define

`H_beta(mu)=sup_y int |x-y|^(-beta) dmu(x)`.

Then

`boxed:
 sup_y D_T mu(y)
 <=(2^(beta-1)/pi) T^(1-beta) H_beta(mu).
}`                                                                  (3.3)

#### Proof

Put `z=T|u|`. The elementary inequality

`1-cos z <= min(z^2/2,2)`                                         (3.4)

implies

`(1-cos z) z^(beta-2) <=2^(beta-1)`                               (3.5)

for every `z>0`: for `z<=2` use the first term in (3.4), and for `z>=2` use the second. Hence

`K_T(u)
 <=(2^(beta-1)/pi) T^(1-beta)|u|^(-beta)`.                        (3.6)

Integrate (3.6) against `mu` and take the supremum in the center. QED.

At the critical half-power,

`boxed:
 sup_y D_T mu(y)
 <= [sqrt(T)/(pi sqrt(2))] H_(1/2)(mu).
}`                                                                  (3.7)

### Corollary 3.2 — disjoint-tetrad signed-frequency payment

Applying (3.7) to the fresh account01/B01 theorem (1.1) gives

`boxed:
 sup_y D_T law(R)(y)
 <= (8 e^(1/4)/pi) sqrt(T) [W_2^dis(B)]^(-1/8).
}`                                                                  (3.8)

Numerically,

`8 e^(1/4)/pi = 3.2697438739437548...`.                            (3.9)

This is an equation-level averaged-frequency use of the newly completed aggregate-before-inversion currency. No individual tetrad minor is reciprocated.

## 4. Main new theorem: universal `sqrt(T log T)` Fejer control for every coupled quadratic

The half-Riesz compiler is useful when a two-volume currency is present, but (1.2) yields a result with no structural hypothesis beyond `S!=0`.

### Theorem 4.1 — `QFORM-UNIVERSAL-QUADRATIC-FEJER-SQRTLOG-v1`

Let

`R=X^T S X+b^T X+gamma`, `S=S^T!=0`, `s=||S||_op`,                (4.1)

with arbitrary independent cap-one original coordinates. Then, for every `T>0`,

`boxed:
 sup_y D_T law(R)(y)
 <= C_F sqrt(T/s) sqrt(1+log_+(Ts/24)),
}`                                                                  (4.2)

where one may take

`C_F = sqrt(24)/(2pi)
      +(2sqrt(48)/pi)/(1-2^(-3/2))
      =7.602582247909892... <7.603.`                               (4.3)

This keeps all signs, all ranks, arbitrary affine terms, arbitrary fragmented/unbounded supports, and every same-bank/cross coupling in `S`.

#### Proof

For fixed center `y`, let

`F_y(r)=P(|R-y|<r)`.                                                (4.4)

Equation (1.2), applied to the symmetric interval of length `2r`, gives for `0<r<=s/24`

`F_y(r)
 <=sqrt[(24r/s)(1+log(s/(24r)))].`                                (4.5)

First assume `z:=Ts>=24`. Split the Fejer convolution into the center

`A_-1={|R-y|<1/T}`

and dyadic shells

`A_k={2^k/T <=|R-y|<2^(k+1)/T}`,  k>=0.                            (4.6)

On the center, (3.2) and (4.5) give

`int_(A_-1) K_T(y-R)dP
 <= [sqrt(24)/(2pi)] sqrt(T/s)
    sqrt(1+log(z/24)).`                                            (4.7)

On `A_k`,

`K_T(y-R)<=2T/(pi 4^k).`                                          (4.8)

If `2^(k+1)/T<=s/24`, (4.5) gives

`P(A_k)
 <=sqrt(48/z) 2^(k/2) sqrt(1+log(z/24)).`                          (4.9)

If instead `2^(k+1)/T>s/24`, the right side of (4.9) is already at least one, because

`48*2^k/z = 24*2^(k+1)/z >1`;                                     (4.10)

therefore (4.9) remains valid simply by the trivial mass bound. Hence (4.9) holds for every `k>=0`. Summing (4.8)-(4.9),

`sum_(k>=0) int_(A_k)K_T dP
 <=[(2sqrt(48)/pi)/(1-2^(-3/2))]
   sqrt(T/s) sqrt(1+log(z/24)).`                                  (4.11)

Equations (4.7) and (4.11) prove (4.2) when `Ts>=24`.

If `Ts<24`, positivity and `sup K_T=T/(2pi)` give

`D_T law(R)(y)<=T/(2pi)
 <=[sqrt(24)/(2pi)] sqrt(T/s)
 <C_F sqrt(T/s),`                                                  (4.12)

which is (4.2) because `log_+(Ts/24)=0`. QED.

### Interpretation

The previous B01 global averaged-frequency estimate in this branch grew like a much larger positive power of `T`. Equation (4.2) reaches the critical quadratic scale up to only a square-root logarithm:

`D_T = O(sqrt((T/s) log(2+Ts))).`                                  (4.13)

This still grows with `T`, so it is **not** an `L^infinity` density proof. Its value is that the precise remaining loss is now near the rank-one square singularity scale rather than an artifact of a coarse fixed-power small-ball estimate.

## 5. Designated partner account04/B01 applied at an actual inequality

The completed account04/B01 theorem used here is

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

At `r=2`, for independent cap-one original coordinates `U,V`, arbitrary affine coefficients, and `c!=0`,

`Z=2cUV+beta U+gamma V+delta`

has a density satisfying

`||p_Z||_2 <=sqrt(2)|c|^(-1/2).`                                  (5.1)

Apply this to an actual source-disjoint sum

`Q=R(X)+Z(U,V)`,                                                   (5.2)

where `R(X)` may be an arbitrary probability-valued quadratic/affine form on a disjoint original product bank. Young's inequality against the probability law of `R` gives

`||p_Q||_2<=||p_Z||_2<=sqrt(2)|c|^(-1/2).`                        (5.3)

By Plancherel for the Fejer kernel,

`||K_T||_2^2
 =(1/(2pi)) int_{-T}^T (1-|t|/T)^2 dt
 =T/(3pi).`                                                       (5.4)

Therefore Cauchy-Schwarz gives the explicit partner-fed signed-frequency inequality

`boxed:
 sup_y D_T law(Q)(y)
 <=sqrt[2T/(3pi|c|)].
}`                                                                  (5.5)

If the disjoint `R` also has nonzero quadratic Hessian of norm `s`, positivity/convolution of the Fejer kernel transfers (4.2) through the independent `Z`; hence

`boxed:
 sup_y D_T law(Q)(y)
 <=min{
   sqrt[2T/(3pi|c|)],
   C_F sqrt(T/s) sqrt(1+log_+(Ts/24))
 }.
}`                                                                  (5.6)

If instead `R` has disjoint-tetrad energy `W>0`, (3.8) gives the further alternative

`sup_y D_T law(Q)(y)
 <=(8e^(1/4)/pi) sqrt(T) W^(-1/8).`                               (5.7)

Equations (5.5)-(5.7) are actual equation-level uses of the designated partner result and the fresh aggregate half-Riesz result; they are not pointwise characteristic-function statements.

## 6. What remains

The full conjecture is not proved. The new theorem gives a universal near-critical signed-frequency budget for every nonzero coupled quadratic, but it still grows as `sqrt(T log T)` and therefore cannot by itself yield a uniform density cap as `T->infinity`.

The freshest third-compound funnel in the fleet reduces unpaid target states to localized overlap-one/overlap-two packets after the principal and disjoint branches are paid. The source-matched account01/B01 result pays overlap-one only after a nonzero scalar pivot, with a residual pivot factor. The first B01 successor is therefore:

`QFORM-PIVOTFREE-OVERLAP1-FEJER-SATURATION-v1`:

> use the fixed anchored overlap-one third-compound packet in the all-small/possibly-zero diagonal chamber to replace the `sqrt(T log T)` growth in (4.2) by an `O(1)` signed-Fejer bound, without selecting one tiny minor or assuming a nonzero scalar pivot.

A second possible route is to combine the coherent low-tetrad Schur-numerator chamber with the kernel-star/ridge/grouped-square receivers already present in the fleet. No claim is made that this structural reduction is complete.

## 7. Regularity status

Theorems 3.1 and 4.1 are statements about Fejer-smoothed measures and do not establish a density or continuity on their own. The partner-fed sum (5.2) has an `L^2` density by (5.3), but continuity is not asserted. Full-target essential boundedness and continuity remain open.

## 8. Deterministic checks

The following constants were independently recomputed in the run:

- `sqrt(24)/(2pi)=0.779696801233676...`;
- `(2sqrt(48)/pi)/(1-2^(-3/2))=6.822885446676215...`;
- their sum is `7.602582247909892...`;
- `8e^(1/4)/pi=3.2697438739437548...`;
- `||K_T||_2^2=T/(3pi)` follows exactly from the triangular multiplier.

The proof is analytic; the numerical evaluations only verify displayed constants.
