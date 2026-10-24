SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T16:02:42Z.
attacking: the genuinely coupled two-heavy/one-diffuse cone-tip frontier; obtain a rotation-uniform analytic ceiling below the 3sqrt(2) obstruction and transfer it to exact cap-one finite families.

# QFORM B17 — two heavy coordinates plus one diffuse bank cannot reach 3sqrt(2) at the cone tip

Run: `20260923T160242Z-account03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC STRESS-FAMILY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Full-target continuity remains OPEN separately. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. The theorem

Let

- `X,Y ~ Uniform[-1/2,1/2]` independently;
- `G ~ N(0,1/12)` independently of `(X,Y)`;
- `M` be any real symmetric `3 x 3` matrix with spectrum `{1,1,-1}`.

Put

`Q = (X,Y,G) M (X,Y,G)^T`.

Then the cone-tip density exists and obeys the **rotation-uniform** bound

`p_Q(0) <= C_2H1G`,

where the following completely explicit certificate is valid:

`C_2H1G <= (22 sqrt(2)/7) * (1595634387/1677721600)`

`             = 4.227203249510199... < 3 sqrt(2) = 4.242640687119286... .`      (1.1)

The same statement holds for spectrum `{1,-1,-1}` after replacing `Q` by `-Q`.

Thus a cone-tip witness at or above the known `3sqrt(2)` obstruction cannot have the architecture “two centered unit-interval macroscopic coordinates plus one minimum-variance Gaussian diffuse coordinate”, even when the signature is mixed by an arbitrary orthogonal rotation.

This is not a theorem for arbitrary heavy marginals and not a global-in-output theorem. It is a source-relevant stress-family exclusion theorem.

## 2. Cone formula

Write

`M = I - 2 n n^T`, `|n|=1`,

so `n` is the negative unit eigenvector. Choose an orthonormal basis `p_1,p_2` of `n^perp`, and set

`p(theta)=p_1 cos(theta)+p_2 sin(theta)`.

The two circles of unit null directions are

`omega_+(theta)=( n+p(theta))/sqrt(2)`,
`omega_-(theta)=(-n+p(theta))/sqrt(2)`.

For a Euclidean radial parameter `rho`, the null cone is `z=rho omega_±(theta)`. Since `M^2=I`,

`|grad(z^T M z)|=2|z|=2rho`.

Also `|partial_theta omega_±|=1/sqrt(2)`, so the cone surface quotient is exactly

`dH^2/|grad q| = (1/(2sqrt(2))) d rho d theta`.                           (2.1)

Along a null ray, the two heavy interval constraints impose

`0 <= rho <= R(omega):=1/[2 max(|omega_1|,|omega_2|)]`.                     (2.2)

With

`gamma(t)=sqrt(6/pi) exp(-6t^2)`

the Gaussian density of `G`, (2.1)-(2.2) give the exact cone-tip formula

`p_Q(0) = (1/(2sqrt(2))) sum_{eps=±1} int_0^{2pi} int_0^{R(omega_eps(theta))}`
`              gamma(rho omega_{eps,3}(theta)) d rho d theta`.              (2.3)

No post-rotation independence is used: the rotation appears only in the null directions of the fixed physical product density.

## 3. An orientation-free radial envelope

Put `z=|omega_3|` and `u=z^2`. Since

`max(|omega_1|,|omega_2|) >= sqrt((1-z^2)/2)`,

(2.2) yields

`R(omega) <= 1/sqrt(2(1-z^2))`.                                             (3.1)

The radial Gaussian integral has two independent elementary bounds:

`int_0^R gamma(rho z) d rho <= sqrt(6/pi) R`,

and, for `z>0`,

`int_0^R gamma(rho z) d rho <= int_0^infty gamma(rho z)d rho = 1/(2z)`.

Therefore

`int_0^R gamma(rho z)d rho <= F(u)`,                                        (3.2)

where

`F(u) := min( sqrt(3/[pi(1-u)]), 1/(2sqrt(u)) )`, `0<u<1`,                  (3.3)

with the obvious endpoint limits.

Let

`r=|n_3|`, `A=sqrt(1-r^2)`.

After a harmless angular phase shift,

`omega_{+,3}(theta)=(r+A cos theta)/sqrt(2)`.

The `-` nappe has the same squared-coordinate distribution. If `Theta` is uniform on `[0,2pi]`, define

`U_r := (r+sqrt(1-r^2) cos Theta)^2/2`.                                     (3.4)

Combining (2.3) and (3.2),

`p_Q(0) <= sqrt(2) pi E F(U_r)`.                                             (3.5)

It remains only to bound a one-parameter arcsine average.

## 4. Exact polynomial majorant

Define

`P(u) = 197/200 - 9u/50 + 533u^2/25 -141u^3 +330u^4`
`       -3353u^5/10 +2517u^6/20`.                                           (4.1)

The checker supplies exact Bernstein-basis certificates for the following four rational polynomial inequalities.

First,

`P(u) > 1/2` on `[0,1]`.                                                     (4.2)

Second, using the elementary Archimedean inequality `pi>157/50=3.14`,

`(157/50)(1-u)P(u)^2 -3 >0` on `[0,26/125]`.                                (4.3)

Because `P>0`, (4.3) implies

`P(u) > sqrt(3/[pi(1-u)])` on `[0,26/125]`.                                 (4.4)

Third,

`4uP(u)^2-1>0` on `[207/1000,1]`,                                           (4.5)

hence

`P(u)>1/(2sqrt u)` there.                                                    (4.6)

The intervals in (4.4) and (4.6) overlap, since `207/1000 < 26/125`. Thus for **every** `u in [0,1]`, at least one of the two branches in (3.3) is dominated, and consequently

`F(u) <= P(u)`.                                                              (4.7)

The positivity certificates are exact: each polynomial is converted to Bernstein form on four equal rational subintervals, and every Bernstein coefficient is positive. The minimum certified coefficients are recorded in `CHECK_OUTPUT.txt`.

## 5. Averaging the majorant

Set `q=r^2 in [0,1]`. From (3.4), for every integer `k>=0`,

`E U_r^k`
` = 2^{-k} sum_{j=0}^k binom(2k,2j) q^{k-j}(1-q)^j binom(2j,j)/4^j`.          (5.1)

Substituting (5.1) into (4.1) gives the exact degree-six polynomial

`A(q):=E P(U_r)`

`=[6131407 +3149646 q -64418143 q^2 +323352900 q^3`
`  -663462975 q^4 +603408590 q^5 -203486865 q^6]/6553600`.                  (5.2)

A second exact Bernstein certificate, now on eight equal subintervals of `[0,1]`, proves

`21/22 - A(q) >= 64098543/18454937600 >0`.                                  (5.3)

Equivalently,

`E F(U_r) <= E P(U_r)`
`             <= 1595634387/1677721600`
`             = 0.9510722082853317... < 21/22`.                             (5.4)

Insert (5.4) into (3.5), and use the elementary `pi<22/7`:

`p_Q(0)`
` < sqrt(2) * (22/7) * 1595634387/1677721600`
` = (17551978257/5872025600) sqrt(2)`
` = 4.227203249510199...`.                                                   (5.5)

Finally

`3 - 17551978257/5872025600 = 64098543/5872025600 >0`,                      (5.6)

so (5.5) is strictly below `3sqrt(2)`. This proves (1.1).

## 6. Exact finite cap-one stress families

The Gaussian coordinate above is only the limiting analytic model. The same architecture has exact target-admissible finite approximants.

Let

`G_m = m^{-1/2} sum_{k=1}^m Z_k`,

where `Z_k ~ Uniform[-1/2,1/2]` independently, and retain independent centered unit-interval `X,Y`. Let `L_m` be the `3 x (m+2)` matrix mapping the physical coordinates to `(X,Y,G_m)`. Its rows are orthonormal, so

`L_m L_m^T=I_3`.                                                            (6.1)

For any fixed signature matrix `M` as above, put

`A_m=L_m^T M L_m`.                                                          (6.2)

Then every physical input has density exactly one on an interval of length one, and the nonzero spectrum of `A_m` is **exactly** `{1,1,-1}` for every finite `m`.

A concrete genuinely coupled choice is the Householder matrix

`M_H=(1/3)[[1,-2,-2],[-2,1,-2],[-2,-2,1]]`,                                (6.3)

for which every effective entry is nonzero, `M_H^2=I`, and `tr M_H=1`.

The completed account04/B17 weighted local Edgeworth lemma gives for the density `g_m` of `G_m`

`g_m(y)=gamma(y)[1-H_4(y/sigma)/(20m)] + O(m^{-2})(1+|y|)^{-8}`,            (6.4)

with `sigma^2=1/12`. Substitution of (6.4) into the same cone formula (2.3) is justified by the polynomially weighted remainder. Hence, for every fixed rotation `M`,

`p_{Q_m}(0)=p_Q(0)+O_M(1/m)`.                                                (6.5)

Therefore every fixed two-heavy/one-diffuse exact cap-one family of the form (6.2) is eventually separated from `3sqrt(2)` at the cone tip. The present report does not claim a uniform-in-`M,m` error constant as `M` degenerates with `m`.

## 7. Designated partner result applied to an actual inequality

The completed designated partner `account04/B17` constructed a different exact finite cap-one family with nonzero spectrum `{1,1,-1}` and proved

`p_{Q_m^partner}(0)`
` = 3sqrt(2) [1 - 5295/(21952m) + O(m^{-2})]`.                              (7.1)

Thus any universal constant `C_*` for the owner target must satisfy

`C_* >= 3sqrt(2)`.                                                          (7.2)

Combining the new theorem with the partner result gives the actual structural inequality

`sup_{M: spec(M)={1,1,-1}} p_{(X,Y,G)^T M (X,Y,G)}(0)`
` <= (17551978257/5872025600)sqrt(2)`
` < 3sqrt(2) <= C_*`.                                                        (7.3)

So the source-valid obstruction at `3sqrt(2)` cannot be reproduced, even asymptotically, by keeping **two** centered unit-interval coordinates macroscopic and diffusing only the third direction. This sharpens the witness-side structural picture: the known obstruction is genuinely more diffuse than this entire rotation-uniform two-heavy boundary.

Partner source actually applied:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

## 8. Scope and next mechanism

What is proved:

- exact cone-tip bound uniform over **all rotations** of the equal-magnitude `(2,1)` signature;
- two centered unit-interval heavy coordinates and one minimum-variance Gaussian diffuse coordinate;
- exact cap-one finite approximants with exact nonzero spectrum `{1,1,-1}`;
- strict separation from the source-valid lower obstruction `3sqrt(2)`.

What is not proved:

- arbitrary cap-one heavy laws instead of centered intervals;
- off-zero/global density peaks for this two-heavy coupled class;
- rotations or coefficients with additional large spectrum outside this rank-three stress model;
- a universal upper bound for the full QFORM target;
- full-target continuity.

The next nonredundant B17 witness mechanism is therefore either (i) fragmented/asymmetric heavy marginals in this two-heavy coupled geometry, especially off-tip levels, or (ii) several mesoscopic shared rows whose surviving non-Gaussian component remains coupled to a diffuse core. A witness above `3sqrt(2)` cannot be explained by the centered two-heavy/one-diffuse cone-tip architecture proved here.

No refuted law-uniform pointwise oscillatory decay, post-rotation independence, arbitrary-joint coarea bound, fiber-supremum dimension-free claim, positive conditional-cap moment, or interval-extremality claim for arbitrary target inputs is used.

Dependencies consumed:

- fresh owner/control programme state from `yspennstate/math-research-brain`, revision `2026-09-22.15`;
- account04/B17 weighted local Edgeworth and exact lower-obstruction witness: `math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`;
- account01/B17 cone-tip closure for the complementary one-heavy/two-diffuse N3 family: `math-open-problems@9ba7adec3f1f7907e3e05cfce6acabb3beedb441`.

Checker: `verify_two_heavy_one_diffuse.py`; exact-arithmetic terminal result: `PASS QFORM_TWO_HEAVY_ONE_DIFFUSE_CONE`.
