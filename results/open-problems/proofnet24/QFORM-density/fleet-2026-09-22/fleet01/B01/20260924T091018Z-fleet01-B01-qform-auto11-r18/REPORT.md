SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-24T09:10:18Z.
attacking: a decoupled mixed-frequency replacement for the false scalar pointwise quadratic-phase decay, with the conditional-density blowup absorbed before inversion.

# fleet01/B01 r18 — sharp sum/difference phase-space estimate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T091018Z-fleet01-B01-qform-auto11-r18`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING AVERAGED-FREQUENCY THEOREMS + SHARP OBSTRUCTION / FULL QFORM OPEN**

## 1. Scope and correction boundary

All scalar sources below are ORIGINAL independent coordinates with probability densities bounded by one. No Gaussian, moment, iid-across-coordinates, compact-support, connected-support, log-concavity, smoothness, or post-rotation independence assumption is used.

The phase-aligned fragmented-support obstruction is preserved. For every prescribed nonzero `tau` and every `eta>0`, one may choose a finite union `E` of intervals of total length one inside

`{x : dist(tau x^2,2 pi Z)<eta}`

and take `f=1_E`. Then

`Re E exp(i tau X^2) >= cos eta`.

Thus no law-uniform positive-power pointwise decay of `E exp(i t X^2)` is used or recovered below. The new estimate is genuinely averaged in the joint difference/frequency variables.

Fresh programme state at the start of this run still records the full conjecture and the full continuity conclusion as OPEN, and still forbids arbitrary-joint coarea, conditional-cap, fiber-supremum, and rotation-independence shortcuts.

## 2. The sharp unnormalized sum/difference transform

Let `X,X'` be iid with a probability density `f`, `0<=f<=1`. Put

`U=X-X'`, `V=X+X'`.

The joint density of `(U,V)` is

`h(u,v)=(1/2) f((v+u)/2) f((v-u)/2)`.                    (2.1)

Define the UNNORMALIZED conditional Fourier kernel

`Psi_f(u,s)=int_R exp(i s v) h(u,v) dv`.                  (2.2)

Also put

`r(u)=int h(u,v)dv=int f(x)f(x-u)dx`.                    (2.3)

Then `r` is the density of `U`, `0<=r<=1`, and `int r=1`.

### Theorem 2.1 — `QFORM-SUMDIFF-UNNORMALIZED-MIXED-LP-v1`

For every `p>=2`,

`boxed: int_R int_R |Psi_f(u,s)|^p ds du <= pi.`          (2.4)

At `p=2` there is the exact identity

`boxed: int int |Psi_f(u,s)|^2 ds du = pi ||f||_2^4.`      (2.5)

Hence the constant `pi` in (2.4) is sharp already at `p=2`: every indicator density `f=1_E` with `|E|=1` has `||f||_2=1` and attains equality in (2.5), including arbitrarily fragmented sets.

#### Proof

For each fixed `u`, Plancherel in the `v` variable, with Fourier convention `hat g(s)=int exp(i s v)g(v)dv`, gives

`int |Psi_f(u,s)|^2 ds = 2 pi int h(u,v)^2 dv`.             (2.6)

Integrating in `u` and changing from `(u,v)` to

`x=(v+u)/2`, `y=(v-u)/2`,

whose Jacobian satisfies `du dv=2 dx dy`, yields

`int int h(u,v)^2 du dv
 = (1/2)(int f(x)^2 dx)^2`.                                   (2.7)

Equations (2.6)-(2.7) give (2.5). Since `f<=1` and `int f=1`, `||f||_2^2<=1`.

Moreover

`|Psi_f(u,s)| <= int h(u,v)dv=r(u)<=1`.                       (2.8)

Therefore for every `p>=2`, `|Psi|^p<=|Psi|^2`, and (2.4) follows from (2.5). QED.

### Corollary 2.2 — arbitrary coefficient pullback, with the correct Jacobian

For every measurable real function `a(u)` and every `p>=2`,

`boxed: int_R int_R |a(u)| |Psi_f(u,t a(u))|^p dt du <= pi.`  (2.9)

At points where `a(u)=0` the integrand is defined to be zero. For every other fixed `u`, use `s=t a(u)` and then apply (2.4).

This is the useful replacement for pointwise van der Corput: no decay is demanded at a fixed frequency; instead, the complete phase-space occupation of large Fourier values is bounded after the exact coefficient Jacobian is retained.

One immediate distribution-in-frequency formulation is

`int |a(u)| |{t: |Psi_f(u,t a(u))|>lambda}| du
 <= pi lambda^(-p)`                                           (2.10)

for every `lambda>0` and `p>=2`.

## 3. Exact quadratic decoupling and a coupled weighted estimate

Now let `X=(X_1,...,X_n)` have independent cap-one coordinates, let `X'` be an independent copy, and let `A=A^T`. Put coordinatewise

`U_j=X_j-X'_j`, `V_j=X_j+X'_j`,

and let `Psi_j,r_j` be the kernels and difference densities from Section 2.

For

`Q=X^T A X`, `phi_Q(t)=E exp(i t Q)`,

symmetry of `A` gives the exact identity

`Q(X)-Q(X')=U^T A V`.                                         (3.1)

Because the PAIRS `(U_j,V_j)` remain independent across original coordinates before conditioning,

`boxed:
 |phi_Q(t)|^2
 = int_(R^n) product_j Psi_j(u_j,t(Au)_j) du.`                 (3.2)

This identity uses no independence after a rotation.

Fix one physical coordinate `j`. For each frozen `u_-j`, apply (2.9) with

`a(u_j)=(Au)_j=A_jj u_j + sum_(k!=j) A_jk u_k`,

multiply by the probability density `product_(k!=j) r_k(u_k)`, and integrate `u_-j`. This proves:

### Theorem 3.1 — `QFORM-DECOUPLED-WEIGHTED-COORDINATE-v1`

For every physical coordinate `j` and every `p>=2`,

`boxed:
 int_R int_(R^n) |(Au)_j| |Psi_j(u_j,t(Au)_j)|^p
                   product_(k!=j) r_k(u_k) du dt <= pi.`       (3.3)

This is already a genuinely COUPLED averaged-frequency estimate: `(Au)_j` may contain every other difference coordinate, and no conditional density cap is inverted.

Equivalently, on the probability space

`dmu(u)=product_k r_k(u_k)du`,

write `psi_j(u_j,s)=Psi_j(u_j,s)/r_j(u_j)` when `r_j>0` (and zero otherwise). Then

`int dt dmu(u) |(Au)_j| r_j(u_j)^(p-1)
                |psi_j(u_j,t(Au)_j)|^p <= pi.`                 (3.4)

This equation displays exactly where the dangerous conditional-cap factor went: the UNNORMALIZED kernel contributes a positive power of the difference density rather than a reciprocal power.

## 4. Three-coordinate Holder and the exact remaining weight

Take three distinct physical coordinates `S={j_1,j_2,j_3}` and use (3.4) at `p=3`. Holder on the common measure `dt dmu(u)` gives

`boxed:
 int dt dmu(u)
   [product_(j in S)|(Au)_j|]^(1/3)
   [product_(j in S)r_j(u_j)]^(2/3)
   product_(j in S)|psi_j(u_j,t(Au)_j|
 <= pi.`                                                       (4.1)

(The final parenthesis in the last factor is `psi_j(u_j,t(Au)_j)`.)

By contrast, taking absolute values in the decoupling identity (3.2), and bounding all unselected normalized conditional characteristic functions by one, leaves

`|phi_Q(t)|^2
 <= int dmu(u) product_(j in S)|psi_j(u_j,t(Au)_j)|`.          (4.2)

Thus the exact unpaid multiplier between the new theorem and the full absolute decoupled integrand is

`W_S(u)= [product_(j in S)|(Au)_j|]^(1/3)
          [product_(j in S)r_j(u_j)]^(2/3).`                   (4.3)

Equation (4.1) controls `W_S` times the desired product, not the unweighted product. A full proof by this route therefore needs a product-preserving way to control the small-`W_S` region, or must combine (4.1) with a grouped physical-crossing receiver before reciprocals are taken. This is consistent with the live correction that positive conditional-density moments can blow up; simply dividing by the `r_j` powers is not legitimate.

This isolates a concrete first missing implication rather than hiding it inside an asserted conditional cap.

## 5. Sharp obstruction: the Jacobian weight cannot simply be dropped

The weight `|a(u)|` in (2.9) is not an artifact.

### Proposition 5.1 — `QFORM-UNWEIGHTED-DECOUPLED-PULLBACK-DIVERGES-v1`

Let `f=1_[0,1]`, let `lambda!=0`, and define `Psi` by (2.2). Then for every `p>0`,

`boxed:
 int_(-1/2)^(1/2) int_R |Psi(u,t lambda u)|^p dt du = infinity.` (5.1)

#### Proof

For `|u|<1`, the joint density (2.1) equals `1/2` on

`|u| <= v <= 2-|u|`,

and vanishes otherwise. Hence `r(u)=1-|u|`. If `|u|<=1/2` and `|s|<=1/4`, then throughout this interval `0<=v<=2`, so

`Re exp(i s v) >= cos(1/2)`.

Therefore

`|Psi(u,s)| >= Re Psi(u,s)
 >= cos(1/2) r(u)
 >= (1/2) cos(1/2)=:c_0>0.`                                   (5.2)

For every nonzero `u` with `|u|<=1/2`, all

`|t| <= 1/(4|lambda u|)`

satisfy `|t lambda u|<=1/4`. Thus

`int_R |Psi(u,t lambda u)|^p dt
 >= c_0^p/(2|lambda u|)`.                                      (5.3)

Integration in `u` diverges logarithmically at zero. QED.

So even for a single UNIFORM input and a diagonal scalar square, an argument that pulls the mixed estimate onto the quadratic coefficient surface and takes absolute values before retaining the coefficient Jacobian is impossible. The underlying square law is not a counterexample to bounded-density QFORM; this proposition refutes only that proof interface.

This also explains why the exact cancellation in `int Psi(u,t lambda u)du`, or an additional independent/grouped smoothing resource, is mathematically essential.

## 6. Designated partner result applied to a full-target family

The freshest completed fleet02/B01 result read in this run is

`QFORM-RANK1-TWOHUB-ARROWHEAD-UNIFORM-v1`,

source-pinned at

`yspennstate/math-open-problems@dd3593b63057f5a9bd01fac32cf4e1d2ffb4848a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/fleet02-B01-20260924T080657Z-4542a979/REPORT.md`.

It proves: if a quadratic-plus-affine residual has ORIGINAL-coordinate coefficient

`S=[[B,w c^T],[c w^T,D]]`,

with two hubs, diagonal leaf bank `D`, rank-one hub/leaf crossing, and `s_2(S)>=1`, then

`H_(1/2)(R)<240`.                                               (6.1)

If an additional ORIGINAL coordinate is completed with coefficient `a_0`, this gives

`||p_Q||_infinity <240 |a_0|^(-1/2)`.                         (6.2)

Apply it to the strict vanishing-tail family

`Q_epsilon = X_0^2 + Z^T S_epsilon Z`,

`Z=(H_1,H_2,Y_1,Y_2)`, and

`S_epsilon =
 [[1,1, 1, epsilon],
  [1,1,-1,-epsilon],
  [1,-1,1,0],
  [epsilon,-epsilon,0,0]],`                                    (6.3)

for `0<=epsilon<=1/4`. This is exactly the partner arrowhead form with

`B=[[1,1],[1,1]]`, `w=(1,-1)`, `c=(1,epsilon)`, `D=diag(1,0)`.

The characteristic polynomial of `S_epsilon` is

`(lambda-2)
 [lambda^3-lambda^2-(2+2 epsilon^2)lambda+2 epsilon^2]`.        (6.4)

The cubic factor at `lambda=-1` equals `4 epsilon^2>=0`, while it tends to `-infinity` as `lambda->-infinity`; hence it has a root `<=-1`. Together with the exact eigenvalue `2`, this proves `s_2(S_epsilon)>=1`. Therefore the full coefficient `diag(1,S_epsilon)` has at least three eigenvalues of absolute value at least one.

The partner theorem and the outer square peel give the actual full-target inequality

`boxed: ||p_(Q_epsilon)||_infinity <240,
        uniformly for 0<=epsilon<=1/4.`                        (6.5)

The old heavy-leaf/tail estimate deteriorated as the tail slope `sqrt(2) epsilon` vanished; (6.5) does not. This is an equation-level use of the designated partner result.

## 7. What this run changes, and what it does not

The new theorem (2.4) is a sharp law-uniform phase-space estimate that survives arbitrary fragmented cap-one densities and therefore is a valid replacement for the false scalar pointwise-decay premise. The exact quadratic identity (3.2) transports it into the coupled form without rotating the independent sources. The weighted coordinate estimate (3.3) is uniform for arbitrary symmetric `A` and arbitrary dimension.

However, Proposition 5.1 proves that the coefficient Jacobian cannot be removed by absolute-value/Fubini arguments, even in the easiest scalar-square example. The three-factor synthesis (4.1)-(4.3) identifies the precise small-weight region that remains. Therefore this run does NOT claim the unrestricted conjecture.

The first unpaid implication is now:

`QFORM-SUMDIFF-SMALL-WEIGHT-AGGREGATION-v1`:
under `s_3(A)>=1`, combine the sharp weighted decoupled estimate (4.1) with an ORIGINAL-coordinate grouped/crossing receiver on the region where

`[product_(j in S)|(Au)_j|]^(1/3)
 [product_(j in S)r_j(u_j)]^(2/3)`

is small, without dividing by conditional-density factors and without selecting a uniformly good single minor.

The projected-crossing theorem in the current interactive package is a natural receiver when the small-weight state exposes two projected crossing directions with its stated row-volume marginal gate; the theorem itself does not show that such a split always exists.

Full QFORM status: **OPEN**.  
Full continuity status: **OPEN**.  
The present theorems establish averaged Fourier control and scoped essential-boundedness consequences only.

## 8. Source pins

Fresh control source at run start:

`yspennstate/math-research-brain@508e080ef479f541bb183c9f8c63237933127dea`.

Relevant current projected-crossing package consumed for scope comparison:

`yspennstate/math-open-problems@43beacb57eba0134d9b4b4cf8b7843a4f119049c`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Designated partner theorem actually applied:

`yspennstate/math-open-problems@dd3593b63057f5a9bd01fac32cf4e1d2ffb4848a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/fleet02-B01-20260924T080657Z-4542a979/REPORT.md`.

No literature novelty claim is made for the elementary Fourier identities in this report; the contribution here is their correction-aware formulation and their exact placement in the current proof graph.
