SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T03:12:16Z.
attacking: decoupled time integral — remove the exact-zero hub restriction by a parabolic-fiber small-ball bound uniform in the hub diagonal, then convert it to a quarter-Riesz independent-copy time estimate and splice it into an indefinite physical pair.

# account03/B03 r25 — arbitrary hub diagonal via parabolic fibers and quarter-Riesz energy

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING THEOREM PROVED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact unrestricted conjecture remains open. This report proves an analytic bridge that is uniform as a physical hub diagonal passes through zero. It uses only original-coordinate independence and a genuine projection-density theorem. No Gaussian, log-concave, moment, compact-support, connected-support, or post-rotation-independence assumption is introduced.

## 1. Inputs and source pins

1. Completed one-dimensional product-projection density bound used below: for independent original coordinates with densities at most one,
   `||p_(m^T Y)||_infinity <= sqrt(2)/||m||_2` for `m != 0`. The source used by the current QFORM fleet is pinned through `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7` and the completed projection result cited by the account01/B03 zero-hub theorem.
2. Completed indefinite-pair quarter-small-ball transducer: `yspennstate/math-open-problems@fab77e73a6163b18eea08d2807aa1a38166279ff:proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T021907Z-account02-B03-QFORM-auto11/REPORT.md`. If an invertible indefinite original-coordinate pair has `D=|det B|`, `kappa=sigma_min(B)`, and its residual `H` obeys `sup_t P(|H-t|<rho)<=K rho^(1/4)`, then
   `||p_Q||_infinity <= 3*2^(4/3) K^(2/3) D^(-1/3) kappa^(-1/6)`.
3. Designated partner account04/B03: `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38:proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260922T193150Z-account04-B03-collision-l2-r1/REPORT.md`. Only its valid elementary collision identity/inequality is used here:
   `P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`.
   Its previously challenged weighted-L2 compiler is not used.

Live corrections consumed include the false conditional sum/difference cap, false post-rotation independence, false uniform scalar pointwise Fresnel decay, false one-Schur rank-two extraction, and the requirement to aggregate before reciprocal local-minor payment.

## 2. New parabolic hub small-ball theorem

### Theorem 2.1 — `QFORM-PARABOLIC-HUB-FROSTMAN-v1`

Let `X` be a real random variable with density at most one. Let `Y` be independent of `X`. Let

`L=L(Y)`

have a density bounded by `M<infinity`, and let `S=S(Y)` be arbitrary measurable and finite almost surely; no independence between `L` and `S` is assumed. For arbitrary `a,beta,z in R` (absorbing `beta` into `L` if desired), set

`R = a X^2 + L X + S`.

Then for every `epsilon>0`,

`sup_z P(|R-z|<=epsilon) <= C_par sqrt(M epsilon)`,              (2.1)

where

`C_par = 4(1+sqrt(3)) = 10.928203230275509...`.

The bound is uniform in `a`, including `a=0` and arbitrarily small nonzero `a`.

### Proof

First suppose `a=0`. Conditional on `Y`, the cap on the density of `X` gives

`P_X(|LX+S-z|<=epsilon | Y) <= min(1, 2epsilon/|L|)`.

For any `tau>0`, use only the marginal density cap for `L`:

`P(|L|<=tau) <= 2M tau`.

Therefore

`P(|R-z|<=epsilon) <= 2M tau + 2epsilon/tau`.

Taking `tau=sqrt(epsilon/M)` gives

`P(|R-z|<=epsilon) <= 4 sqrt(M epsilon)`, which is stronger than (2.1).

Now suppose `a!=0`. Conditional on `Y`, complete the square:

`R-z = a (X+L/(2a))^2 - d(Y)`,

where `d(Y)=z-S+L^2/(4a)`. Put `A=|a|`; after multiplying by `sign(a)` the sublevel set is of the form

`| A (X+L/(2a))^2 - d_*(Y) | <= epsilon`.

Fix `K>1` and split into `|d_*|<=K epsilon` and its complement.

On the near-critical part, the sublevel condition implies

`|X+L/(2a)| <= sqrt((K+1)epsilon/A)`.

For every fixed value `X=x`, this restricts `L` to an interval of length

`4 A sqrt((K+1)epsilon/A)=4 sqrt(A(K+1)epsilon)`.

Since `X` is independent of `L` and `p_L<=M`, after discarding the condition on `S` we obtain

`P(near and sublevel) <= 4M sqrt(A(K+1)epsilon)`.                 (2.2)

On the far-critical part, a nonempty sublevel forces `d_*>K epsilon`. For fixed `Y`, its total `X`-length is

`2/sqrt(A) [sqrt(d_*+epsilon)-sqrt(d_*-epsilon)]`
`=4epsilon/[sqrt(A)(sqrt(d_*+epsilon)+sqrt(d_*-epsilon))]`
`<=4 sqrt(epsilon)/(sqrt(A) sqrt(K-1))`.

Because `p_X<=1`,

`P(far and sublevel) <= 4 sqrt(epsilon)/(sqrt(A) sqrt(K-1))`.    (2.3)

If `AM<=1`, choose `K-1=1/(AM)`. Combining (2.2)-(2.3) yields

`P(|R-z|<=epsilon)`
`<=4 sqrt(Mepsilon) [sqrt(1+2AM)+1]`
`<=4(1+sqrt(3)) sqrt(Mepsilon)`.

If `AM>1`, use the unconditional scalar quadratic sublevel estimate: for every fixed `Y`,

`Leb{x: |a x^2+Lx+S-z|<=epsilon} <= 2 sqrt(2epsilon/A)`.

Thus

`P(|R-z|<=epsilon) <= 2sqrt(2) sqrt(epsilon/A)`
`< 2sqrt(2) sqrt(Mepsilon)`.

This is again bounded by the right side of (2.1). The theorem follows. QED.

### Why this is dependence-safe

The proof never conditions `X-X'` on `X+X'`, never treats them as independent, and never rotates the physical coordinates. The potentially adversarial dependence between the linear coefficient `L(Y)` and the remainder `S(Y)` is retained throughout. The only averaging is over the genuine independent physical hub coordinate `X` and the true marginal law of `L`.

## 3. Product-source specialization and the requested independent-copy time estimate

Let `Y=(Y_1,...,Y_m)` have independent coordinate densities bounded by one and let `m != 0`. Put

`L=2 m^T Y + beta`.

The completed projection theorem gives

`M=||p_L||_infinity <= 1/(sqrt(2)||m||_2)`.                    (3.1)

Thus every

`R = aX^2 + X(2m^T Y+beta) + S(Y)`                            (3.2)

satisfies

`sup_z P(|R-z|<=epsilon)`
`<= C_par 2^(-1/4) ||m||_2^(-1/2) epsilon^(1/2)`.             (3.3)

The standard layer-cake identity implies that if `P(|R-z|<=rho)<=min(1,A rho^(1/2))`, then for every `0<alpha<1/2`,

`sup_z E|R-z|^(-alpha) <= A^(2alpha)/(1-2alpha)`.              (3.4)

At `alpha=1/4`, (3.1)-(3.4) give

`sup_z E|R-z|^(-1/4)`
`<= 2 sqrt(C_par) 2^(-1/8) ||m||_2^(-1/4)`
`= 6.062833305147929... ||m||_2^(-1/4)`.                      (3.5)

Now let `R'` be an independent copy and `phi_R(t)=E exp(itR)`. The exact independent-copy identity is

`|phi_R(t)|^2 = E exp(it(R-R'))`.

Using the one-dimensional Riesz-energy identity,

`int_R |t|^(-3/4)|phi_R(t)|^2 dt`
`=2 Gamma(1/4) cos(pi/8) E|R-R'|^(-1/4)`.

Conditioning on `R'` and using (3.5) yields the explicit integrated estimate

`boxed: int_R |t|^(-3/4)|phi_R(t)|^2 dt`
`<=40.61645768900424... ||m||_2^(-1/4).`                      (3.6)

This is the assigned decoupled-time quantity. It keeps the entire dependent sum/difference geometry inside `R-R'`; no conditional cap for a conjugate sum/difference variable appears.

## 4. Linear small-ball recovery by a completed indefinite-pair transducer

The half-power estimate (3.3) implies the quarter-power small-ball estimate

`sup_z P(|R-z|<=rho) <= H rho^(1/4)`,

with

`H = sqrt(C_par) M^(1/4)`,

because `min(1,x)<=sqrt(x)`. Apply the completed account02/B03 indefinite-pair theorem to a disjoint invertible indefinite original-coordinate pair with

`D=|det B|`, `kappa=sigma_min(B)`.

Using (3.1),

`||p_Q||_infinity`
`<= 3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6)`
`<= C_pair D^(-1/3) kappa^(-1/6) ||m||_2^(-1/6)`,             (4.1)

where

`C_pair = 3*2^(5/4) [4(1+sqrt(3))]^(1/3)`
`=15.834037540973641...`.

Hence every interval `I` obeys the linear small-ball estimate

`P(Q in I) <= C_pair D^(-1/3) kappa^(-1/6) ||m||_2^(-1/6) |I|`.

This is an essential bounded-density conclusion in the stated packet. Continuity is not proved here.

## 5. Designated account04/B03 partner applied to an actual inequality

For the `Q` in Section 4, `p_Q in L^1 cap L^infinity`, hence

`||p_Q||_2^2 <= ||p_Q||_infinity`.

Apply the valid account04/B03 collision lemma to an independent copy `Q'`:

`P(|Q-Q'|<=epsilon) <=2epsilon ||p_Q||_2^2`
`<= 31.668075081947283... D^(-1/3) kappa^(-1/6) ||m||_2^(-1/6) epsilon`.   (5.1)

This is a literal use of the designated partner result. No use is made of that run's separately refuted weighted-L2 compiler.

## 6. Concrete target-family control

Let

`B0=[[0,1],[1,0]]`,
`H_a=[[a,1],[1,0]]`,
`A_a=B0 direct_sum H_a`.

The eigenvalues of `B0` are `+1,-1`; the eigenvalues of `H_a` have product `-1`, so at least one has modulus at least one for every real `a`. Thus `A_a` always has at least three eigenvalues of modulus at least one. Taking the first block as the indefinite pair and the second as the hub-star residual gives `D=kappa=||m||=1`, hence

`||p_(X^T A_a X)||_infinity <=15.834037540973641...`

for every real `a` and every independent cap-one input law. The estimate does not deteriorate as `a -> 0`, which is the point of the new bridge.

This family is only a control/application, not a claim that the unrestricted spectral hypothesis forces the packet.

## 7. What changed and what remains

The previous exact-zero-hub theorem required `a=0`; the present parabolic-fiber argument is uniform for all `a`, including arbitrarily small nonzero values, and supplies a dependence-safe weighted `|phi|^2` estimate. Therefore the analytic **near-zero hub bridge** is paid whenever that hub sits in a residual disjoint from an indefinite physical pair.

The full conjecture is still OPEN. The first target-level structural debt is to show that the bare three-large-eigenvalue hypothesis forces either this packet or one of the already-paid ridge/volume/augmented-screen/grouped-square/exact-coloop exits. The recent account03/B10 near-null-hub-star reduction has a large aggregate star but does not by itself guarantee a disjoint uniformly conditioned indefinite pair, so this report does not declare that branch closed.

Continuity for the unrestricted target remains OPEN; this report proves essential boundedness only in the stated splice scope.
