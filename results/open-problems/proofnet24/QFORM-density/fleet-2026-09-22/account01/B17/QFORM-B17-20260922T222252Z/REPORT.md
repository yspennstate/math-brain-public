SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-22T22:22:52Z.
attacking: all-angle two-heavy same-sign rotations, with account02/B17's exact fourth minority-sign Gaussian mode theorem applied to the resulting half-Riesz inequality.

# QFORM-B17: all-angle two-heavy positive-plane stress family stays below the 3sqrt(2) obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `QFORM-B17-20260922T222252Z`  
Assignment: `Sharp constant and witnesses`  
Classification: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`  
Full-target continuity: separately OPEN.  
Execution memory: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and source dependencies

The full target remains open: for arbitrary independent physical coordinates with one-dimensional densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of magnitude at least one, prove a dimension-free essential-density bound for `X^T A X`, or exhibit a valid counterexample.

This report proves a sharp-witness exclusion theorem for an exact original-coordinate family. It does **not** assume independence after a spectral rotation, and it does not use the corrected-false arbitrary-joint coarea bound, conditional-projection density moment, fiber-supremum reduction, or law-uniform pointwise stationary-phase estimate.

The designated partner theorem actually used is account02/B17 run `20260922T204449Z-account02-B17-QFORM-r19`, complete proof

`yspennstate/math-open-problems@50913ed00c5943aaf2772473cbf17ddcb5bed090:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T204449Z-account02-B17-QFORM-r19/REPORT.md`.

It proves, for iid standard Gaussians and every `delta>0`,

`T_delta^- = Z_1^2+Z_2^2-Z_3^2-delta Z_4^2`

has its global density maximum at zero and

`||p_{T_delta^-}||_infinity = 1/[2 sqrt(2(1+delta))]`,

using the decreasing density

`h_delta(u)=[1/(2sqrt(delta))] exp(-alpha u) I_0(beta u)`,

`alpha=(1+delta^(-1))/4`, `beta=|1-delta^(-1)|/4`.

I apply that exact Bessel/Laplace representation in Section 7, obtaining the same fourth-mode ceiling for a non-Gaussian two-heavy rotated family on a large angular regime. This is an actual inequality-level use of the partner result.

I also reuse the fixed-parameter BV/local-limit mechanism proved in account01/B17 run `20260922T204400Z-account01-B17-QFORM-r19`, canonical proof

`yspennstate/math-open-problems@bfc251e91668cd258a337a5207a53bd1167a48b9:proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T204400Z-account01-B17-QFORM-r19/REPORT.md`.

## 2. Exact finite source-valid rotated family

Let `c in [0,1]` be the absolute cosine of the angle between two macroscopic physical rows in the positive spectral plane. Put

`alpha^2=(1+c)/2`, `beta^2=(1-c)/2`.

For fixed `m`, define rows in `R^{4}`

`v_1=(alpha/sqrt(2), beta/sqrt(2),0,0)`,
`v_2=(alpha/sqrt(2),-beta/sqrt(2),0,0)`.

Add four disjoint diffuse banks:

- `m` copies of `(beta/sqrt(m),0,0,0)`,
- `m` copies of `(0,alpha/sqrt(m),0,0)`,
- `m` copies of `(0,0,1/sqrt(m),0)`,
- `m` copies of `(0,0,0,1/sqrt(m))`.

The two heavy rows contribute `diag(alpha^2,beta^2,0,0)` to the Gram matrix and the banks contribute `diag(beta^2,alpha^2,1,1)`. Therefore, exactly,

`R_{m,c}^T R_{m,c}=I_4`.

For `delta>=0`, put

`J_delta=diag(1,1,-1,-delta)`,
`A_{m,c,delta}=R_{m,c} J_delta R_{m,c}^T`.

For `delta>0` the nonzero spectrum is exactly `{1,1,-1,-delta}`; at `delta=0` the nonzero spectrum is `{1,1,-1}`. Thus every finite matrix satisfies the original three-large-eigenvalue hypothesis. No post-rotation independence is being asserted.

Put iid `Unif[-1/2,1/2]` laws on every physical coordinate. Their densities equal one. If `H_i=sqrt(12)X_i`, then `H_i` is uniform on `[-sqrt(3),sqrt(3)]`, with mean zero and variance one. For the two heavy coordinates set

`S=(H_1+H_2)/sqrt(2)`, `D=(H_1-H_2)/sqrt(2)`.

The exact joint density of `(S,D)` is

`rho(s,d)=1/12 * 1_{|s|+|d|<=sqrt(6)}`.                 (2.1)

As `m->infinity`, the four independent diffuse banks converge to iid standard Gaussians. Hence

`12 X^T A_{m,c,delta} X  ==>  T_{c,delta}`,               (2.2)

where

`Y_1=alpha S+beta G_1`,
`Y_2=beta D+alpha G_2`,

and

`T_{c,delta}=Y_1^2+Y_2^2-G_3^2-delta G_4^2`.             (2.3)

The variables `G_1,...,G_4` are iid standard Gaussians, independent of `(S,D)`.

This is a genuinely noncollinear family for `0<=c<1`; `c=1` is the parallel endpoint. It covers the full continuous angle interval rather than only a neighborhood of one endpoint.

## 3. The global mode is at zero

Let

`R_c^2=Y_1^2+Y_2^2`.

The joint law of `(S,D)` is uniform on a centrally symmetric convex diamond, hence log-concave and even. Linear images preserve log-concavity, and convolution with the independent Gaussian residual preserves log-concavity. Thus `(Y_1,Y_2)` has an even log-concave density `rho_c` (with the endpoint `c=1` obtained directly as the product of the triangular density of `S` and a Gaussian density).

Along every ray, `r -> rho_c(r omega)` is nonincreasing for `r>=0`. Therefore the density of `R_c^2`,

`k_c(u)=1/2 int_{S^1} rho_c(sqrt(u) omega) d omega`,       (3.1)

is nonincreasing on `u>=0`.

The density of `G_3^2` is also nonincreasing. More generally, account02/B17's partner theorem proves that the density `h_delta` of

`G_3^2+delta G_4^2`

is strictly decreasing for `delta>0`.

For independent nonnegative `U,V` with decreasing densities `k,h`, the density of `U-V` is maximized at zero: for `t>=0`,

`p(t)=int_0^infinity k(t+v)h(v)dv <= p(0)`,

and for `t=-x<=0`,

`p(-x)=int_0^infinity k(u)h(u+x)du <= p(0)`.              (3.2)

Consequently, for every `c in [0,1]` and every `delta>=0`,

`||p_{T_{c,delta}}||_infinity=p_{T_{c,delta}}(0)`.         (3.3)

Thus the stress calculation below is global in the output location, not merely a central-value calculation.

## 4. Exact half-Riesz reduction and a new negative-association inequality

First take `delta=0`. The density of `G_3^2` gives

`p_{T_{c,0}}(0)
 = 1/sqrt(2pi) E[(R_c^2)^(-1/2) exp(-R_c^2/2)]`
` = 1/(pi sqrt(2)) int_0^infinity s^(-1/2) L_{s+1/2}(c) ds`,             (4.1)

where

`L_a(c)=E exp[-a(Y_1^2+Y_2^2)]`.

Conditioning on `(S,D)` and integrating the two Gaussian residuals gives

`L_a(c)= [d_1 d_2]^(-1/2) E exp(-q_1 S^2-q_2 D^2)`,        (4.2)

with

`d_1=1+a(1-c)`,
`d_2=1+a(1+c)`,

`q_1=a(1+c)/[2(1+a(1-c))]`,
`q_2=a(1-c)/[2(1+a(1+c))]`.                              (4.3)

The absolute values `U=|S|`, `V=|D|` are uniform on the triangle

`U>=0`, `V>=0`, `U+V<=sqrt(6)`,

with density `1/3`. Conditional on `U=u`, `V` is uniform on `[0,sqrt(6)-u]`. If `g` is decreasing, its conditional average over that interval increases with `u`. Hence a decreasing function of `U` and a decreasing function of `V` have nonpositive covariance. Applying this to `exp(-q_1 U^2)` and `exp(-q_2 V^2)` gives the exact dependence-safe inequality

`E exp(-q_1 S^2-q_2 D^2) <= F(q_1)F(q_2)`,               (4.4)

where the common one-dimensional marginal transform is

`F(q)=E exp(-qS^2)`
`    = sqrt(6pi)/(6sqrt(q)) erf(sqrt(6q))-(1-exp(-6q))/(6q)`,           (4.5)

with `F(0)=1` by continuity.

Define

`r(q)=sqrt(1+2q) F(q)`.                                  (4.6)

The identities

`d_1(1+2q_1)=d_2(1+2q_2)=1+2a`                           (4.7)

turn (4.2)-(4.4) into

`boxed( L_a(c) <= r(q_1)r(q_2)/(1+2a) ).`                 (4.8)

The rest of the proof is a quantitative scalar estimate on `r`.

## 5. Scalar transform lemma

### Lemma 5.1

For `r` in (4.6):

1. `r(q)<1` for `0<q<=70`;
2. `r(q)<0.99` for `49/100<=q<=21/2`;
3. `r(q)<1.03` for every `q>=0`.

The inequalities may be taken non-strict at `q=0`.

### Proof

Let `H` be uniform on `[-sqrt(3),sqrt(3)]` and `S=(H_1+H_2)/sqrt(2)`. Exact moments are

`E H^(2j)=3^j/(2j+1)`,

`E S^(2k)=2^(-k) sum_{j=0}^k binom(2k,2j) E H^(2j) E H^(2k-2j)`.        (5.1)

For `z>=0`, the even Taylor truncation of `exp(-z)` is an upper bound. Let

`U_N(q)=sum_{k=0}^N (-q)^k E S^(2k)/k!`, with even `N`.                (5.2)

For `0<q<=1/2`, use `N=6`. Exact expansion gives

`(1+2q)U_6(q)^2-1 = q^2 P_6(q)/25050025`,              (5.3)

where

`P_6(q)=25404192 q^11-57351888 q^10+98889336 q^9-142833132 q^8`
`       +179356320 q^7-201873672 q^6+224836326 q^5-174794763 q^4`
`       +134606472 q^3-88462374 q^2+45805760 q-15030015.`

An exact rational Sturm sequence has zero roots on `[0,1/2]`, and `P_6(0)<0`, `P_6(1/2)<0`. Therefore `r(q)<1` there.

For `49/100<=q<=1`, use `N=12`. The exact rational Sturm computation for

`(1+2q)U_12(q)^2-(99/100)^2`                            (5.4)

has zero roots on `[49/100,1]` and is negative at both endpoints. Hence `r(q)<0.99` on that interval.

For `q>=1`, write `x=sqrt(q)`. From (4.5), `erf<=1`, `e^6>400`, and `pi<22/7`,

`F(q) < 181/(250x)-133/(800x^2)`.                        (5.5)

Here `e^6>400` follows already from the Taylor partial sum through order 13,

`sum_{k=0}^{13}6^k/k! = 10059173/25025 >400`,

and `sqrt(pi/6)<181/250` follows from `11/21<(181/250)^2`.

The inequality `r(q)<1` resulting from (5.5) is equivalent, after clearing the positive denominator, to negativity of

`P_1(x)=773632x^4-7703360x^3+9271266x^2-3851680x+442225`.             (5.6)

An exact Sturm sequence has zero roots on `[1,17/2]`, and the polynomial is negative at both endpoints. Since `sqrt(70)<17/2`, this proves `r(q)<1` on `[1,70]`.

Similarly, `r(q)<0.99` follows from negativity of

`P_.99(x)=1092032x^4-7703360x^3+9271266x^2-3851680x+442225`           (5.7)

on `[1,13/4]`. Exact Sturm count is zero and both endpoint values are negative. Since `sqrt(21/2)<13/4`, this completes item 2.

Finally the triangular marginal density of `S` is at most `1/sqrt(6)`, so

`F(q)<=sqrt(pi/(6q))`.                                   (5.8)

For `q>=70`,

`r(q)^2 <= pi/3+pi/(6q) <=47pi/140 <517/490 <(1.03)^2`.   (5.9)

Together with item 1 below 70, this gives the global `1.03` bound. QED.

The accompanying standard-library checker reproduces every polynomial, exact Sturm root count, and rational comparison used above.

## 6. All rotation angles: no escape above 3sqrt(2)

Set

`c_0=139/141`.                                            (6.1)

### Low/intermediate angles: `0<=c<=c_0`

From (4.3), `q_1` increases with both `a` and `c`, and

`q_1 <= (1+c)/[2(1-c)] <=70`.                            (6.2)

Also `0<=q_2<=q_1`. Therefore Lemma 5.1 and (4.8) give

`L_a(c)<=1/(1+2a)`.                                      (6.3)

For `c<c_0` (and also at `c=c_0`) the inequality is strict for every `a>0` because both relevant positive `q` values lie in the strict range. Substituting `a=s+1/2` into (4.1),

`p_{T_{c,0}}(0)
 <= 1/(pi sqrt(2)) int_0^infinity s^(-1/2)/[2(1+s)] ds
 =1/(2sqrt(2))`.                                         (6.4)

Thus the physical-scale limiting peak is at most `3sqrt(2)`, and in fact is strictly smaller for every fixed `c<=c_0`.

### Near-parallel angles: `c_0<=c<=1`

On `0<=s<=10`, put `a=s+1/2`. Then

`q_1 >= q_1(1/2,c_0)=35/71>49/100`,
`q_1 <= q_1(21/2,1)=21/2`.                               (6.5)

Moreover

`q_2 <= (1-c)/[2(1+c)] <=1/280`.                         (6.6)

Hence Lemma 5.1 gives

`r(q_1)r(q_2)<0.99` for `0<=s<=10`,                      (6.7)

while globally

`r(q_1)r(q_2)<1.03` for `s>10`.                          (6.8)

Relative to the baseline weight

`w(s)=s^(-1/2)/(1+s)`, `int_0^infinity w(s)ds=pi`,

the tail beyond ten has fraction

`tau=1-(2/pi)atan(sqrt(10))<1/5`.                         (6.9)

Indeed `sqrt(10)>tan(2pi/5)=sqrt(5+2sqrt(5))`, since `25>20` after the elementary squaring step.

Therefore (4.1) and (4.8) imply the explicit strict global bound

`boxed( ||p_{T_{c,0}}||_infinity < (499/500)/(2sqrt(2)) )`             (6.10)

for every `c in [139/141,1]`.

Returning to the original physical scale,

`boxed( ||p_Q||_infinity < (499/500) 3sqrt(2)
       =4.2341554057... )`                               (6.11)

for these limiting stress laws.

Combining the two angle regimes proves:

### Theorem 6.2 — all-angle two-heavy no-escape

For the exact source-valid two-heavy frame family above, its Gaussian-completion limit with signature `(1,1,-1)` satisfies

`boxed( ||p_{T_{c,0}}||_infinity <1/(2sqrt(2)) )`

for every `c in [0,1]`. Thus **no angle between the two macroscopic centered-interval physical rows can raise the limiting physical density peak to or above `3sqrt(2)`**. The near-parallel region has the explicit uniform factor `499/500`.

This replaces the previous B17 result, which only excluded an existential open wedge near one endpoint, by a complete continuous-angle exclusion for this symmetric two-heavy architecture.

## 7. Applying account02/B17: a fourth minority-sign mode

Now take `delta>0`. The exact partner formula admits the integral representation

`h_delta(u)=1/(2pi sqrt(delta)) int_0^pi exp[-a_theta u] dtheta`,        (7.1)

where

`a_theta=alpha_delta-beta_delta cos(theta)`,
`alpha_delta=(1+delta^(-1))/4`,
`beta_delta=|1-delta^(-1)|/4`.                            (7.2)

This is the partner theorem's Bessel identity `I_0(z)=pi^(-1)int_0^pi exp(z cos theta)dtheta` written as a positive mixture of exponential kernels.

For `c<=c_0`, (6.3) applies to every `a_theta>0`. Thus

`p_{T_{c,delta}}(0)
 =1/(2pi sqrt(delta)) int_0^pi L_{a_theta}(c)dtheta`
` <=1/(2pi sqrt(delta)) int_0^pi dtheta/[1+2a_theta]`.     (7.3)

Set

`A=(3delta+1)/(2delta)`, `B=|delta-1|/(2delta)`.

The classical integral `int_0^pi (A-B cos theta)^(-1)dtheta=pi/sqrt(A^2-B^2)` and

`A^2-B^2=2(1+delta)/delta`

give

`boxed( ||p_{T_{c,delta}}||_infinity
       <=1/[2sqrt(2(1+delta))] ),  0<=c<=139/141.`         (7.4)

This is **exactly the same ceiling as account02/B17's all-Gaussian four-mode theorem**, now proved for a non-Gaussian dependent two-heavy positive pair. At physical variance scale `1/12`,

`||p_Q||_infinity <=3sqrt(2)/sqrt(1+delta)`.              (7.5)

In particular, `delta=1` gives `<=3`.

For `c>=c_0`, the added term `-delta G_4^2` is an independent convolution. Hence Young's inequality and (6.10) give

`||p_{T_{c,delta}}||_infinity
 <=||p_{T_{c,0}}||_infinity
 <(499/500)/(2sqrt(2))`.                                  (7.6)

Therefore an independent Gaussianized fourth minority-sign mode cannot create an escape at **any** heavy-row angle. The partner result is used quantitatively in (7.1)-(7.5), not merely cited.

## 8. Transfer to exact finite product-source matrices

For fixed `c in (0,1)` and fixed `delta>=0`, the normalized Irwin-Hall diffuse-bank densities have uniformly bounded sup norm and bounded variation. The BV stationary-phase estimate proved in the previous B17 run gives, after conditioning on the two heavy variables, an integrable characteristic-function envelope of order

`C_{c,delta} min(1,|t|^(-3/2))`                          (8.1)

from three nondegenerate square factors. Pointwise CLT convergence plus dominated Fourier inversion therefore gives

`||p_{12Q_{m,c,delta}}-p_{T_{c,delta}}||_infinity ->0`    (8.2)

for each fixed interior `c`. At `c=1`, the triangular heavy sum supplies the missing BV square factor and the same conclusion follows; at `c=0`, both residual positive factors are nondegenerate and the argument is immediate.

Hence every fixed parameter point with a strict limiting gap transfers to all sufficiently large finite members of the exact original-coordinate family. In particular:

- for every fixed `c in [139/141,1]` and every `delta>=0`, sufficiently large `m` obey `||p_{Q_{m,c,delta}}||_infinity<3sqrt(2)`;
- for every fixed `c<=139/141` and every `delta>0`, the partner factor `(1+delta)^(-1/2)` gives a strict quantitative margin and the same finite conclusion;
- for `delta=0` and fixed `c<=139/141`, Section 6 already gives a strict limiting inequality; uniform local convergence again transfers it for that fixed `c`.

Thus the theorem constrains actual finite target matrices, not only an arbitrary Gaussian relaxation.

## 9. What has been eliminated and what remains

The current lower obstruction `C>=3sqrt(2)` is now more rigid. This run rules out, in the centered-interval/diffuse-completion architecture:

1. **every angle** between two equal-leverage macroscopic physical rows in the same-sign spectral plane;
2. all corresponding exact finite large-bank approximants;
3. an additional independent Gaussianized minority-sign spectral mode of any fixed strength `delta>0`.

The result does **not** prove that `3sqrt(2)` is the sharp universal constant and does not prove full QFORM. Plausible remaining witness mechanisms include unequal heavy-row leverages, three or more interacting macroscopic physical rows, arbitrary fragmented cap-one heavy laws, genuinely non-Gaussian/mesoscopic residual banks, coupled extra spectral directions, or finite-dimensional/off-center spikes outside this architecture.

A natural next B17 target is the unequal-leverage two-heavy family. The negative-association step survives, but the scalar Gaussian-completion identities no longer collapse to the same `r(q_1)r(q_2)/(1+2a)` denominator; a weighted version is needed. A second target is to combine the present all-angle theorem with the partner variance-rigidity estimate to quantify how much spectral tail or leverage asymmetry a hypothetical witness above `3sqrt(2)` must carry.

Full QFORM status: `OPEN / NOT PROVED`. Full-target continuity: separately `OPEN`.

## 10. Exact checker

`CHECK.py` is standard-library only. It verifies the exact moment identities, reconstructs the Taylor polynomials, executes rational Sturm root counts for (5.3)-(5.7), verifies the elementary rational bounds used in (5.5), and checks the angle-split arithmetic. Saved output is `PASS`.
