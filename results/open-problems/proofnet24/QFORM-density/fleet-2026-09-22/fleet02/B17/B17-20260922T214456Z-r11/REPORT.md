SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-22T21:44:56Z.
attacking: shared-coordinate non-collinear heavy-row stress families and exact finite/mesoscopic overshoot above the 3*sqrt(2) diffuse scale.

# fleet02/B17 — saturated opposite-sign heavy plane: a zero-peak no-escape theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B17-20260922T214456Z-r11`  
Assignment: Sharp constant and witnesses  
Status: `NEW SUPPORTING SHARP-WITNESS THEOREM / FULL QFORM OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope, controls, and source pins

The full target is unchanged: for arbitrary independent real coordinates with densities at most one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a dimension-free essential-density bound for `X^T A X`, or give a valid counterexample. Nothing below proves the full target or the full continuity conclusion.


The live correction state was reread before publication. This argument does not use the refuted arbitrary-joint coarea bound, conditional-projection positive moments, worst scalar conditional supremum, law-uniform pointwise stationary phase, post-rotation independence, or a law-uniform integrable radial envelope. In particular, the recent event `QFORM-NO-UNIVERSAL-INTEGRABLE-RADIAL-ENVELOPE-v1` does not conflict with the calculation below: here the source is one explicit compact product law and the radial integral is evaluated before any universal supremum.

## 2. Completed designated-partner result actually applied

The designated partner `fleet03/B17` completed `QFORM-FINITE-PERIOD-EDGEWORTH-OPT-v1`:

- brain handoff commit `60122fb4adcad036db3e1953b6ecc5afd7ff20ce`;
- canonical proof `yspennstate/math-open-problems@1814cc179646bd88950581be1297ee5c3cbb43b2`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260922T211144Z-fleet03-B17-QFORM-r17/REPORT.md`.

For a fixed repeated tight-frame pattern with iid centered unit-interval inputs, it proves

`p_Qm(0)=3 sqrt(2)[1-(20m)^(-1) sum_j E(s_j,t_j)+O(m^-2)]`,

`E(s,t)=57 s^2/32+15 st/4+3 t^2/4`,

and solves the finite-period minimization exactly. Every first-order optimizer is sign-segregated; a genuinely sign-mixing physical row is never first-order optimal. Thus another fixed-period diffuse Edgeworth perturbation is not the next credible route above `3sqrt(2)`.

I apply that conclusion by moving to the complementary **maximal-leverage** regime: two macroscopic physical rows spanning the positive/negative spectral plane, with only the third direction diffuse. The rows are not `m^-1/2` perturbations, so this branch is outside the partner theorem rather than a repetition of it.

## 3. Exact finite source-valid stress family

Let

`J=diag(1,1,-1)`

and, for an arbitrary angle `theta`, put

`v1=(cos(theta),0,sin(theta))`,

`v2=(-sin(theta),0,cos(theta))`,

`w=(0,1,0)`.

These three vectors are orthonormal. For every integer `m>=1`, form an `(m+2) x 3` physical-to-spectral frame `R_m` whose rows are

`v1, v2, w/sqrt(m),...,w/sqrt(m)`

with `m` copies of the last row. Then exactly

`R_m^T R_m=I_3`.

Hence

`A_m=R_m J R_m^T`

has exact nonzero spectrum `{1,1,-1}` for every finite `m`; in particular it satisfies the original target hypothesis without asymptotic spectral error.

Put independent `Uniform[-1/2,1/2]` laws on all `m+2` physical coordinates. Their densities are exactly one. If the two heavy coordinates are called `X,Y` and

`S_m=m^(-1/2) sum_{k=1}^m U_k`,

then

`Q_m = q_theta(X,Y)+S_m^2`,

where

`q_theta(x,y)=cos(2 theta)(x^2-y^2)-2 sin(2 theta)xy`.          (3.1)

Thus this is an actual finite product-source family with two fully macroscopic, generally sign-mixing physical rows.

The normalized uniform sum obeys a local CLT. One elementary Fourier proof uses

`phi_m(t)=sinc(t/(2 sqrt(m)))^m`.

For `|t|<=2 sqrt(m)`, `|sinc(t/(2sqrt(m)))|^m <= exp(-t^2/24)`; outside that window, `|sinc u|<=1/|u|` gives an integrable power tail whose `L^1` mass is `O(m^-1/2)`. Fourier inversion therefore gives uniform convergence of the density of `S_m` to the `N(0,1/12)` density. The same estimates give a dimension-free density cap for the `S_m` once `m` is bounded away from one.

Consequently, for each fixed `theta`, the zero-density of `Q_m` converges to that of

`Q_theta=q_theta(X,Y)+G^2`,                                  (3.2)

where `G~N(0,1/12)` is independent of the two centered unit intervals. Indeed the density of `G^2` is

`h(t)=sqrt(6/pi) t^(-1/2) exp(-6t) 1_{t>0}`,                 (3.3)

and the corresponding square-density kernels for `S_m^2` are uniformly bounded by `C t^-1/2`. Since a nondegenerate indefinite binary quadratic form is a nonsingular linear image of a product `ab`, the function `(-q_theta)^-1/2` is locally integrable on the square. Dominated convergence applies at output zero.

## 4. Uniform zero-peak theorem for the entire saturated heavy plane

### Theorem 4.1 — saturated opposite-sign heavy zero peak stays below `3sqrt(2)`

For every real `theta`, the limiting density in (3.2) satisfies

`p_theta(0) <= C_sat < 3 sqrt(2)`,                            (4.1)

where an explicit analytic upper bound is

`C_sat = sqrt(3)/(140 sqrt(pi)) [389 A - 388 B]`,             (4.2)

`A=int_0^(pi/2) cos(x)^(-1/2) dx`,

`B=int_0^(pi/2) cos(x)^(1/2) dx`.

Numerically, only as a sanity check,

`C_sat = 3.87463172270584706277...`,

leaving a margin `0.36800896441343808...` below `3sqrt(2)`.

### Proof

Write `x=r cos(phi)`, `y=r sin(phi)`. Equation (3.1) becomes

`q_theta=r^2 c_theta(phi)`,

`c_theta(phi)=cos(2phi+2theta)`.

On the square `[-1/2,1/2]^2`, the radial endpoint is

`R(phi)=1/[2 max(|cos phi|,|sin phi|)] <= 1/sqrt(2)`.          (4.3)

By (3.3),

`p_theta(0)
 =sqrt(6/pi) int_{c_theta<0} (-c_theta(phi))^-1/2
      int_0^{R(phi)} exp(6 c_theta(phi) r^2) dr dphi`.        (4.4)

The negative set consists of two congruent sectors. Translating each sector in angle, and using (4.3), gives

`p_theta(0)
 <=2 sqrt(6/pi) int_{-pi/4}^{pi/4} a(u)^-1/2
      int_0^{1/sqrt(2)} exp(-6 a(u) r^2) dr du`,              (4.5)

where `a(u)=cos(2u)`.

For every `z>=0`, Taylor's theorem with its signed fifth-order remainder gives the global upper bound

`exp(-z) <= 1-z+z^2/2-z^3/6+z^4/24`.                         (4.6)

Insert (4.6) into (4.5), integrate powers of `r`, and write

`J_p=int_{-pi/4}^{pi/4} cos(2u)^p du
    =int_0^(pi/2) cos(x)^p dx`.

The standard beta recurrence gives

`J_(3/2)=J_(-1/2)/3`,
`J_(5/2)=3 J_(1/2)/5`,
`J_(7/2)=5 J_(-1/2)/21`.

Putting `A=J_(-1/2)` and `B=J_(1/2)` reduces the entire fourth-order upper polynomial exactly to (4.2). The beta-function formulas also give

`A B = pi`.                                                   (4.7)

It remains to compare (4.2) to `3sqrt(2)` without relying on floating-point numerics.

Use `t=tan x` and invert the part `t>=1` to obtain

`A=int_0^1 (1+t^-1/2)(1+t^2)^(-3/4) dt`.                     (4.8)

The function `f(z)=(1+z)^(-3/4)` is convex on `[0,1]`, hence it lies below its endpoint chord:

`f(z) <= 1-(1-2^-3/4)z`.

Since `(5/3)^4=625/81<8`, one has `2^-3/4<3/5`; therefore

`A < int_0^1 (1+t^-1/2)(1-(2/5)t^2) dt
   = 3-22/75
   = 203/75`.                                                 (4.9)

Also `pi>157/50`. The expression

`F(A,pi)=sqrt(3)/(140sqrt(pi)) [389 A-388 pi/A]`

is increasing in `A` and decreasing in `pi`, so (4.7)-(4.9) imply

`C_sat < F(203/75,157/50)`.

Let `a=203/75`, `p=157/50`. Since `389a^2-388p>0`, the inequality

`F(a,p)<3sqrt(2)`

is equivalent after squaring to

`(389a^2-388p)^2 < (140a)^2 6p`.

The exact rational gap is

`(140a)^2 6p-(389a^2-388p)^2
 = 1373690072999/31640625 >0`.                                (4.10)

This proves (4.1) for every angle `theta`. `QED`

## 5. Aligned endpoint: the entire limiting density is maximized at zero

The preceding theorem controls only output zero for a general orientation. At the aligned endpoint `theta=0`, one can prove a full `L^infinity` statement for the limiting law.

Here

`Q_0=X^2+G^2-Y^2`.

Let `A_+=X^2+G^2`. The square density of a centered unit interval is

`g(u)=u^-1/2 1_{0<u<1/4}`.

For `0<t<=1/4`, convolution with (3.3) gives exactly

`f_{A_+}(t)=sqrt(6 pi) exp(-3t) I_0(3t)`,                     (5.1)

where `I_0` is the modified Bessel function. Since `I_1(z)<I_0(z)` for `z>0`, (5.1) is decreasing. For `t>1/4`, the convolution integral is over the fixed interval `0<u<1/4`, and each factor `(t-u)^-1/2 exp[-6(t-u)]` decreases in `t`; hence `f_{A_+}` is decreasing on all of `(0,infinity)`.

The density of `Q_0=A_+-Y^2` is

`p_0(t)=int_0^infinity f_{A_+}(t+s) g(s) ds`

with `f_{A_+}=0` on the negative half-line. For `t>=0`, monotonicity of `f_{A_+}` gives `p_0(t)<=p_0(0)`. For `t=-a<0`, substituting `u=s-a` gives

`p_0(-a)=int_0^infinity f_{A_+}(u) g(u+a) du <= p_0(0)`

because `g` is decreasing. Therefore

`||p_0||_infinity=p_0(0)`.                                   (5.2)

Using (5.1) and `t=r^2`,

`p_0(0)
 =2 sqrt(6 pi) int_0^(1/2) exp(-3r^2) I_0(3r^2) dr`.          (5.3)

The deterministic check evaluates (5.3) as

`3.53619573328141858328...`.

The strict inequality `p_0(0)<3sqrt(2)` is already rigorously implied by Theorem 4.1; the decimal in (5.3) is not part of the proof.

## 6. Target-level implication and what remains unpaid

This run gives a new exact stress-family exclusion, not a proof of the conjecture and not a proof that `3sqrt(2)` is globally sharp.

The known lower obstruction `C>=3sqrt(2)` is still supplied by the diffuse three-bank uniform family. The designated partner now proves that every fixed-period iid uniform-cube Edgeworth perturbation approaches that obstruction from below at first order, with sign-segregated rows optimal. The present theorem attacks a complementary extreme in which two physical rows have leverage one and rotate through the opposite-sign spectral plane. Even there, **every orientation has limiting zero density strictly below `3sqrt(2)`**, with a fully explicit uniform analytic margin; the aligned endpoint has its entire limiting density below `3sqrt(2)`.

Therefore a source-valid witness above `3sqrt(2)`, if one exists, cannot be obtained merely by taking two centered-interval macroscopic rows spanning the opposite-sign plane and looking at the central peak. Inside this branch an escape would have to be genuinely off-zero and non-aligned. More broadly, the remaining plausible mechanisms are arbitrary fragmented heavy laws, three or more interacting macroscopic rows, finite/mesoscopic overshoot that disappears in the Gaussian-completion limit, growing/nonperiodic geometry, non-Gaussian residual banks, or extra spectral directions.

The immediate B17 successor is to attack the **off-zero maximum for general theta** in this exact saturated two-heavy family. A positive result there would close the whole family at `3sqrt(2)`; a negative result would supply a sharply localized source-valid candidate witness.

## 7. Deterministic check

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify the exact rational comparison (4.10), the beta-constant identities numerically to high precision, representative frame spectra, and the endpoint integral. The output is

`PASS QFORM-SATURATED-OPPOSITE-HEAVY-ZERO-v1`.

The rational-square assertion is the proof certificate for the only delicate constant comparison. The high-precision values and sampled spectra are sanity checks only; no histogram or Monte Carlo conclusion is used.
