SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-22T20:44:00Z.
attacking: a symmetric noncollinear two-heavy rotation away from the saturated minority-sign collinear stress family, with exact finite source-valid frames and a uniform local-limit transfer.

# QFORM-B17: an open noncollinear two-heavy wedge cannot beat the 3sqrt(2) Gaussian obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`
Assignment: `Sharp constant and witnesses`
Classification: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`
Continuity of the full target: separately OPEN.
Execution memory: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact dependency actually applied

The designated partner input is fleet02/B17 run `20260922T194544Z-fleet02-B17-QFORM-r18`, complete proof

`yspennstate/math-open-problems@97c8874b48c663a7ae131cb3899dbafdb5a31d1c:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260922T194544Z-fleet02-B17-QFORM-r18/REPORT.md`.

For two arbitrary cap-one heavy laws loaded collinearly on the minority-sign direction and two diffuse majority-sign Gaussian banks, it proves the exact global limiting ceiling

`B0 = int_0^1 (1-u) exp(-3u^2) du`

in standardized scale, attained at output zero by two centered unit intervals. Hence the physical branch constant is

`C_col = 12 B0 = 2 sqrt(3 pi) erf(sqrt(3)) - 2 + 2 exp(-3)`
`      = 4.1516968595129935... < 3 sqrt(2)`.

I apply this exact strict gap below. I do not use the refuted law-uniform pointwise quadratic stationary-phase bound, the false arbitrary-joint coarea inequality, the false conditional-projection positive-moment gate, or the corrected-false pointwise nonorthogonal two-heavy radial-Laplace domination.

## 2. Exact finite rotated stress family

Fix `eta in [0,1]` and an integer `m>=1`. Let `J=diag(1,1,-1)`. Define an `(2+3m) x 3` physical-to-spectral frame `R_{m,eta}` by the two heavy rows

`v_1=(sqrt(eta/2), 0, sqrt((1-eta)/2))`,
`v_2=(-sqrt(eta/2),0, sqrt((1-eta)/2))`,

and three diffuse banks:

- `m` copies of `sqrt((1-eta)/m) e_1`,
- `m` copies of `m^(-1/2) e_2`,
- `m` copies of `sqrt(eta/m) e_3`.

The heavy contribution to the Gram matrix is `diag(eta,0,1-eta)` and the diffuse contribution is `diag(1-eta,1,eta)`. Therefore exactly

`R_{m,eta}^T R_{m,eta}=I_3`.

Consequently

`A_{m,eta}=R_{m,eta} J R_{m,eta}^T`

has nonzero spectrum exactly `{1,1,-1}` for every finite `m` and every `eta`. Thus every member is an original-coordinate target matrix, not a post-rotation independence model.

Put independent `Unif[-1/2,1/2]` laws on every physical coordinate. Let `H=sqrt(12)X`, so each standardized physical input has mean zero, variance one and support `[-sqrt(3),sqrt(3)]`. For the two heavy variables define

`S=(H_1+H_2)/sqrt(2)`, `D=(H_1-H_2)/sqrt(2)`.

Their joint density is exactly

`rho_0(s,d)=1/12 * 1_{|s|+|d|<=sqrt(6)}`.                    (2.1)

For each diffuse bank let

`Z_{j,m}=m^(-1/2) sum_{k=1}^m H_{j,k}`.

Then

`12 Q_{m,eta}=T_{m,eta}`
` = (sqrt(eta)D+sqrt(1-eta)Z_{1,m})^2`
`   + Z_{2,m}^2`
`   - (sqrt(1-eta)S+sqrt(eta)Z_{3,m})^2`.                 (2.2)

As `m->infinity`, the three banks converge jointly to independent standard Gaussians, giving

`T_eta=(sqrt(eta)D+sqrt(1-eta)G_1)^2 + G_2^2`
`      -(sqrt(1-eta)S+sqrt(eta)G_3)^2`.                   (2.3)

At `eta=0`, this is exactly the centered-interval extremizer in the partner theorem:

`T_0=G_1^2+G_2^2-S^2`,

and hence

`||p_0||_infinity=B0 < 1/(2 sqrt(2))`.                    (2.4)

## 3. Global density continuity in the rotation parameter at eta=0

The following is the main new analytic step.

### Theorem 3.1

The limiting output densities satisfy

`||p_eta-p_0||_infinity -> 0` as `eta downarrow 0`.         (3.1)

Therefore there exists `eta_0>0` such that for every `0<eta<eta_0`,

`||p_eta||_infinity < 1/(2 sqrt(2))`.                      (3.2)

Thus the entire limiting two-heavy family in a genuine open noncollinear wedge adjacent to the saturated collinear minority-sign branch stays strictly below the `3sqrt(2)` physical obstruction, globally in the output location.

### Proof

Put

`Y_eta=sqrt(1-eta)S+sqrt(eta)G_3`.

Let `rho_eta(d,y)` be the joint density of `(D,Y_eta)`. If

`tilde rho_eta(d,y)=(1-eta)^(-1/2) rho_0(d,y/sqrt(1-eta))`,

then `rho_eta` is the convolution of `tilde rho_eta` in the second variable with the centered Gaussian kernel of variance `eta`. Standard `L^1` continuity of dilations and the Gaussian approximate identity give

`||rho_eta-rho_0||_1 ->0`.                                (3.3)

For fixed `D=d`, let `k_eta(r,d)` be the density at `r>=0` of

`R_eta=(sqrt(eta)d+sqrt(1-eta)G_1)^2+G_2^2`.

The two-dimensional Gaussian density before taking the squared radius is

`q_{eta,d}(x,y)=phi_{1-eta}(x-sqrt(eta)d) phi_1(y)`.

Because `|d|<=sqrt(6)` on the support of (2.1),

`sup_{x,y,|d|<=sqrt(6)} |q_{eta,d}(x,y)-phi_1(x)phi_1(y)| ->0`.          (3.4)

The squared-radius density has the exact polar representation

`k_eta(r,d)=1/2 int_0^{2pi} q_{eta,d}(sqrt(r)cos theta,sqrt(r)sin theta) dtheta`.

Hence

`sup_{r>=0,|d|<=sqrt(6)} |k_eta(r,d)-k_0(r)| ->0`,          (3.5)

where

`k_0(r)=1/2 exp(-r/2)` and `||k_0||_infinity=1/2`.

Conditioning only on `(D,Y_eta)` is legitimate here because `G_1,G_2` are independent of `(S,D,G_3)`. Therefore

`p_eta(t)=int rho_eta(d,y) k_eta(t+y^2,d) 1_{t+y^2>=0} dd dy`.            (3.6)

Subtract the corresponding formula at `eta=0`. Uniformly in `t`,

`|p_eta(t)-p_0(t)|`
` <= sup_{r,d}|k_eta(r,d)-k_0(r)| + (1/2)||rho_eta-rho_0||_1`,           (3.7)

which tends to zero by (3.3)-(3.5). This proves (3.1).

Now use the strict partner gap (2.4). Let

`Delta=1/(2sqrt(2))-B0>0`.

Choose `eta_0` so that the left side of (3.1) is `<Delta/2`. Then (3.2) follows. QED.

## 4. Transfer back to exact finite target matrices

The preceding theorem is not merely a formal Gaussian relaxation. For every fixed `eta in (0,1)`, the densities of the exact finite target family (2.2) converge uniformly to `p_eta`.

### Theorem 4.1

For each fixed `eta in (0,1)`, if `p_{m,eta}` denotes the density of `T_{m,eta}`, then

`||p_{m,eta}-p_eta||_infinity ->0`.                       (4.1)

Consequently, for each fixed `eta in (0,eta_0)`, there is `m_0(eta)` such that all `m>=m_0(eta)` satisfy

`||p_{Q_{m,eta}}||_infinity < 3sqrt(2)`.                  (4.2)

### Proof

Let `g_m` be the density of `Z_{j,m}`. It is symmetric unimodal. Moreover its sup norm is bounded uniformly in `m`. One elementary proof uses

`hat g_m(t)=[sinc(sqrt(3)t/sqrt(m))]^m`

and the estimates `|sinc u|<=exp(-u^2/7)` for `|u|<=1` and `|sinc u|<=|u|^{-1}` for `|u|>=1`, which give `sup_m ||g_m||_infinity<1` (with `m=1` checked directly). Symmetric unimodality then gives `Var_BV(g_m)=2||g_m||_infinity`, also uniformly bounded.

For a one-dimensional bounded-variation density `g`, a shift `a`, a scale `sigma>0`, and `|t|>=1`, splitting at distance `|t|^{-1/2}` from the stationary point and integrating by parts on the two tails gives the elementary van-der-Corput/BV estimate

`|int exp(it(a+sigma x)^2)g(x) dx|`
` <= C (||g||_infinity+Var_BV(g))/(sigma sqrt(|t|))`.       (4.3)

This is used only for the fixed Irwin-Hall bank densities, not as a law-uniform cap-one statement.

Condition on `(S,D)`. The three diffuse banks in (2.2) are independent, so its conditional characteristic function is a product of three factors of the form (4.3), with scales

`sqrt(1-eta), 1, sqrt(eta)`.

Thus, for fixed `eta in (0,1)`,

`|phi_{m,eta}(t)| <= C_eta min(1,|t|^{-3/2})`              (4.4)

uniformly in `m,S,D`. The right side is integrable. The ordinary CLT gives pointwise convergence of each bank factor, hence `phi_{m,eta}(t)->phi_eta(t)` for every `t`. Dominated convergence in (4.4) yields

`||phi_{m,eta}-phi_eta||_1 ->0`.                           (4.5)

Fourier inversion therefore gives (4.1):

`||p_{m,eta}-p_eta||_infinity <=(2pi)^(-1)||phi_{m,eta}-phi_eta||_1`.

Finally, density scaling from `12Q_{m,eta}=T_{m,eta}` gives

`||p_{Q_{m,eta}}||_infinity=12||p_{m,eta}||_infinity`.

Combine (3.2) and (4.1) to obtain (4.2). QED.

This argument also supplies continuous densities for this specific finite family; it does not settle the separately open continuity conclusion for arbitrary QFORM inputs.

## 5. Exact first variation of the central peak

The global open-wedge theorem needs only continuity and the partner gap. In addition, the central density has an exact first derivative at the collinear endpoint, and its sign is strictly negative.

### Proposition 5.1

As `eta downarrow0`,

`p_eta(0)=B0+c_1 eta+o(eta)`,                              (5.1)

where

`c_1 = -11/36 + (2/9)e^{-3} + [sqrt(3pi)/12] erf(sqrt(3))`
`    = -0.0423199824691997... <0`.                         (5.2)

Equivalently in physical scale,

`p_{Q_infty,eta}(0)=C_col + 12 c_1 eta+o(eta)`,             (5.3)

with

`12c_1=-0.507839789630397...`.

Thus splitting the two collinear minority-sign heavy rows symmetrically into a genuinely noncollinear pair initially lowers the central peak.

### Derivation

At `eta=0`, the positive part `G_1^2+G_2^2` has density

`k_0(r)=1/2 e^{-r/2}`.

For fixed `D`, the perturbed first positive coordinate is

`sqrt(eta)D+sqrt(1-eta)G_1`.

Expanding its Gaussian density through order `eta`, the order-`sqrt(eta)` term is odd and vanishes after the circle integral. The order-`eta` radial-square correction is

`partial_eta k_eta(r,D)|_0`
` = [(D^2-1)/2] (r/2-1) k_0(r)`.                          (5.4)

The negative coordinate is

`Y_eta=sqrt(1-eta)S+sqrt(eta)G_3`.

Since

`E exp(-Y_eta^2/2)`
`=(1+eta)^(-1/2) exp[-(1-eta)S^2/(2(1+eta))]`,             (5.5)

its derivative at zero contributes

`(1/2)e^{-S^2/2}(S^2-1/2)`.                               (5.6)

From (2.1), conditional on `S=s`, the variable `D` is uniform on

`[-a,a]`, `a=sqrt(6)-|s|`,

so

`E[D^2|S=s]=a^2/3`,

while

`f_S(s)=a/6`, `|s|<=sqrt(6)`.                              (5.7)

Combining (5.4)-(5.7) gives

`c_1 = int f_S(s)e^{-s^2/2}`
` [1/4((sqrt(6)-|s|)^2/3-1)(s^2/2-1) + 1/2(s^2-1/2)] ds`. (5.8)

Elementary Gaussian integration reduces (5.8) exactly to (5.2).

The sign can be certified without decimals: `erf(sqrt(3))<1`, `e^{-3}<1/20`, and `sqrt(3pi)<31/10` (for example from `pi<22/7`). Therefore

`c_1 < -11/36 + 1/90 + 31/120 = -13/360 <0`.              (5.9)

## 6. What this eliminates, and what remains

This is a strict extension of the partner's exact collinear minority-sign theorem. It rules out not just the collinear endpoint but a genuine open set of noncollinear two-heavy rotations around it, globally in the output location, and transfers that exclusion back to exact finite-dimensional original-coordinate target matrices for all sufficiently large diffuse-bank sizes.

It does NOT prove the full QFORM conjecture and does NOT prove that `3sqrt(2)` is globally sharp. The parameter neighborhood is existential rather than an explicit optimal angle, the heavy laws in the rotated extension are centered unit intervals, and finite/mesoscopic overshoots outside the eventual large-`m` regime are not excluded.

Credible remaining sharp-witness mechanisms include: larger noncollinear rotation away from this wedge; arbitrary fragmented heavy laws after rotation; three or more interacting macroscopic rows; off-center finite-dimensional spikes; non-Gaussian residual banks at a mesoscopic scale; or additional spectral directions.

For the proof-first programme, the full arbitrary-matrix implication remains unpaid. This result is a sharp-witness exclusion and source-valid stress constraint, not an exhaustive structural reduction.

## 7. Corrections respected

This proof preserves original-coordinate independence and never rotates the physical product law into independent spectral coordinates. It does not use the false arbitrary-joint coarea bound, the false conditional projection-density positive moment, a universal pointwise stationary-phase estimate, or the refuted pointwise nonorthogonal radial-Laplace comparison. The BV oscillatory estimate in Section 4 is applied only to the explicit normalized Irwin-Hall diffuse-bank densities, whose uniform BV control is proved inside the argument.

## 8. Verification status

A deterministic checker accompanying this report verifies the frame identity for representative parameters, evaluates `C_col`, the strict `3sqrt(2)` gap, and the exact coefficient `c_1`, and checks the rational sign certificate (5.9). These computations are sanity checks only; the theorem is the analytic argument above.
