SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T16:23:45Z.
attacking: the exact-coloop endpoint left by r34 — replace the fragile cancelled physical pivot by the complementary one-dimensional product projection, prove a dependence-safe residual time integral, and splice the two possible square pivots into a uniform linear small-ball bound.

# fleet03/B03 r35 — exact-coloop aggregate compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM / EXACT-COLOOP ENDPOINT CLOSED INSIDE THE r32 ANGULAR PACKET / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


## 1. Source-valid packet and the remaining r34 endpoint

The immediate predecessor is

`yspennstate/math-open-problems@926549e6ace81816d0533164f35f548a4f84d508`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T125915Z-fleet03-B03-QFORM-r34/REPORT.md`.

It reduces the only unpaid collar **inside the exact r32 angular packet** to a high-leverage physical right-bank row. The packet is

`Q = a^(-1) H^2 + 2 sigma U V`,                                    (1.1)

with

`H = a X_i + h_L.X_L + h_R.X_R + h_K.X_K`,
`U = u.X_L`, `V = v.X_R`,                                          (1.2)

where the displayed banks are disjoint original-coordinate product banks,

`h_R = beta v + m q`, `q perpendicular v`, `||q||=||v||=1`,       (1.3)

and

`m = rho y`, `y^2>1/2`,
`(|sigma| rho^2/|a|) >= s_3(A)^2`.                                 (1.4)

For right-bank physical row `j`, put

`z_j=(v_j,q_j)`, `eta_j=||z_j||^2`.                                (1.5)

r34 pays the non-coloop alternative uniformly. The remaining endpoint is `eta_j` close to one together with angular cancellation of `h_j=beta v_j+m q_j`. The present run closes the **exact coloop** `eta_j=1` uniformly, including `h_j=0` and all signs of the packet coefficients.

The scalar projection input used below is the same source-valid one used in r32: every unit linear projection of an independent cap-one product bank has a density bounded by

`L0 = sqrt(e)`.                                                     (1.6)

The designated partner remains fleet04/B03, canonical

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`.

Only its elementary valid collision implication

`P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`                              (1.7)

is used. Its challenged stronger weighted-L2 compiler is not used.

## 2. Two scalar lemmas used by the coloop compiler

### Lemma 2.1 — cap-to-half-Riesz

If a real random variable `Y` has density at most `M`, then for every `s`,

`E |Y-s|^(-1/2) <= 2 sqrt(2M)`.                                    (2.1)

This is the one-dimensional bathtub/rearrangement bound: among probability densities bounded by `M`, the decreasing kernel `|y-s|^(-1/2)` is maximized by density `M` on the centered interval of length `1/M`. Hence

`M int_{-1/(2M)}^{1/(2M)} |x|^(-1/2) dx = 2 sqrt(2M)`.             (2.2)

### Lemma 2.2 — bilinear residual: one-copy half-Riesz and decoupled time integral

Let `Y` be independent of a background `B`, with density cap `M_Y`. Let `U=U(B)` have marginal density cap `M_U`; no independence between `U` and the remaining components of `B` is assumed. Let `S=S(B)` be arbitrary and

`R = S(B) + 2 b U(B) Y`, `b!=0`.                                  (2.3)

Then

`boxed:
 sup_s E|R-s|^(-1/2)
 <= 4 sqrt(2 M_Y M_U / |b|).
}`                                                                  (2.4)

Indeed, condition on the complete background. Lemma 2.1 and scaling give

`E_Y[|R-s|^(-1/2) | B]
 <=2 sqrt(2M_Y) / sqrt(2|bU|)
 =2 sqrt(M_Y/|b|) |U|^(-1/2).`                                    (2.5)

Average and apply Lemma 2.1 to the marginal law of `U` at the origin.

The same decomposition gives the assigned **independent-copy time estimate**. Let `F_Y(xi)=E exp(i xi Y)`. Conditioning on the whole `B` and applying Cauchy--Schwarz only across that whole background,

`|phi_R(t)|^2
 <= E |F_Y(2btU)|^2
 <= [M_U/(2|bt|)] int_R |F_Y(xi)|^2 dxi`.                          (2.6)

Plancherel and `p_Y<=M_Y` give

`int |F_Y|^2 <= 2 pi M_Y`,                                        (2.7)

therefore

`boxed:
 |phi_R(t)|^2 <= min{1, A/|t|},
 A = pi M_U M_Y/|b|.
}`                                                                  (2.8)

Consequently

`boxed:
 int_R |t|^(-1/2)|phi_R(t)|^2 dt <= 8 sqrt(A)
 =8 sqrt(pi M_U M_Y/|b|).
}`                                                                  (2.9)

The identity behind the left side is exactly

`|phi_R(t)|^2 = E exp(it(R-R'))`.                                  (2.10)

No coordinate difference is declared independent of its conjugate sum. The proof keeps the entire copy difference intact and uses original-product independence only for the genuine selector `Y` versus its background.

### Lemma 2.3 — square receiver

Let `Z` be independent of a background `B`, with density cap `M_Z`, and let

`T = d [Z+g(B)]^2 + R(B)`, `d!=0`.                                (2.11)

Conditionally on `B`, the square pushforward density is bounded by

`M_Z |d|^(-1/2) |y|^(-1/2)`.                                      (2.12)

Hence

`boxed:
 ||p_T||_infinity
 <= M_Z |d|^(-1/2) sup_s E|R-s|^(-1/2).
}`                                                                  (2.13)

This proves essential boundedness and linear small-ball scaling. By itself it does not prove continuity.

## 3. Exact coloop geometry aggregates the whole complementary bank

Assume now that one right-bank row is an exact coloop:

`eta_j=v_j^2+q_j^2=1`.                                             (3.1)

Because the rows `z_k=(v_k,q_k)` form a Parseval frame,

`sum_k z_k z_k^T = I_2`.                                          (3.2)

Put

`w_j=(-q_j,v_j)`.                                                  (3.3)

Then

`sum_{k!=j} z_k z_k^T = I_2-z_j z_j^T = w_j w_j^T`.               (3.4)

For the vector parallel to `z_j`, the left side of (3.4) has zero quadratic form, so each complementary row is orthogonal to `z_j`. Therefore there are scalars `c_k` with

`z_k=c_k w_j`, `sum_{k!=j} c_k^2=1`.                              (3.5)

Define the **aggregate complementary physical projection**

`W = sum_{k!=j} c_k X_k`.                                         (3.6)

It is independent of `X_j` and of all non-right banks, and by (1.6) its density is bounded by `L0`.

Define the two rotated coefficients

`h_j = beta v_j + m q_j`,
`h_c = -beta q_j + m v_j`.                                        (3.7)

The transform `(beta,m)->(h_j,h_c)` is orthogonal, so

`h_j^2+h_c^2=beta^2+m^2 >= m^2`.                                  (3.8)

Also

`q_j h_j + v_j h_c = m`.                                          (3.9)

Writing

`H_0=aX_i+h_L.X_L+h_K.X_K`,                                      (3.10)

we have the exact product-preserving reduction

`V = v_j X_j - q_j W`,
`h_R.X_R = h_j X_j + h_c W`,                                      (3.11)

so

`Q = a^(-1)(H_0+h_jX_j+h_cW)^2
     +2 sigma U(v_jX_j-q_jW).`                                    (3.12)

No rotation of the probability law has been made: `X_j` remains an original coordinate and `W` is an aggregate of a disjoint original-coordinate bank.

## 4. Pivot the aggregate when `|h_c|` is the larger coefficient

Assume `h_c!=0`. Complete the square in `W` in (3.12). Exact expansion gives

`Q = (h_c^2/a)[W+G_w]^2 + R_w`,                                   (4.1)

where `G_w` depends only on `X_j` and the non-right background, and

`R_w
 = 2 sigma (m/h_c) U X_j
   + 2 sigma (q_j/h_c) U H_0
   - a sigma^2 q_j^2 h_c^(-2) U^2`.                               (4.2)

The nontrivial identity in the coefficient of `X_j` is

`v_j + q_j h_j/h_c = m/h_c`,                                     (4.3)

which is exactly (3.9).

Thus (4.2) has the form of Lemma 2.2 with genuine selector `Y=X_j`,

`M_Y=1`, `M_U=L0`, `b=sigma m/h_c`.                               (4.4)

Therefore

`boxed:
 sup_s E|R_w-s|^(-1/2)
 <=4 sqrt(2L0) sqrt(|h_c|/(|sigma|m)).
}`                                                                  (4.5)

and the assigned dependence-safe time estimate is

`boxed:
 int |t|^(-1/2)|phi_{R_w}(t)|^2 dt
 <=8 sqrt(pi L0) sqrt(|h_c|/(|sigma|m)).
}`                                                                  (4.6)

Since the square variable `W` has cap `L0`, Lemma 2.3 yields

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2) L0^(3/2)
   sqrt(|a|/(|sigma|m|h_c|)).
}`                                                                  (4.7)

This bound is stable at the angular-cancellation endpoint `h_j=0`; there `|h_c|=sqrt(beta^2+m^2)>=m`.

## 5. Pivot the physical coordinate when `|h_j|` is the larger coefficient

Assume `h_j!=0`. Complete the square in the genuine physical coordinate `X_j`. One obtains

`Q = (h_j^2/a)[X_j+G_j]^2 + R_j`,                                 (5.1)

with

`R_j
 = -2 sigma (m/h_j) U W
   -2 sigma (v_j/h_j) U H_0
   -a sigma^2 v_j^2 h_j^(-2) U^2`.                                (5.2)

Here the coefficient identity is

`q_j + v_j h_c/h_j = m/h_j`,                                     (5.3)

again equivalent to (3.9).

Now the selector is the aggregate `W`, whose density cap is `L0`, while the coefficient `U` also has marginal cap `L0`. Lemma 2.2 with

`M_Y=L0`, `M_U=L0`, `b=-sigma m/h_j`                              (5.4)

gives

`boxed:
 sup_s E|R_j-s|^(-1/2)
 <=4 sqrt(2) L0 sqrt(|h_j|/(|sigma|m)).
}`                                                                  (5.5)

and the independent-copy time estimate

`boxed:
 int |t|^(-1/2)|phi_{R_j}(t)|^2 dt
 <=8 sqrt(pi) L0 sqrt(|h_j|/(|sigma|m)).
}`                                                                  (5.6)

The square selector `X_j` has cap one, so

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2) L0
   sqrt(|a|/(|sigma|m|h_j|)).
}`                                                                  (5.7)

This route is considerably sharper than importing the general rank-two Schur receiver because exact coloop geometry has already aggregated the complementary bank into one independent scalar projection.

## 6. Uniform exact-coloop compiler at the target scale

At least one of `|h_j|,|h_c|` is at least `m/sqrt(2)` by (3.8). Use (5.7) if `|h_j|>=|h_c|` and (4.7) otherwise. Since `L0=sqrt(e)>1`, both are bounded by

`4 sqrt(2) L0^(3/2)
 sqrt( |a| / (|sigma| m M) )`,                                    (6.1)

where

`M=max(|h_j|,|h_c|)>=m/sqrt(2)`.                                  (6.2)

The packet scale (1.4) and `m=rho y`, `y^2>1/2`, imply

`|a|/(|sigma|m^2)
 <= 1/[s_3(A)^2 y^2]
 < 2/s_3(A)^2`.                                                    (6.3)

Hence

`sqrt(|a|/(|sigma|mM))
 <=2^(3/4) s_3(A)^(-1)`.                                          (6.4)

Combining (6.1)-(6.4) proves the new endpoint theorem.

### Theorem 6.1 — `QFORM-EXACT-COLOOP-AGGREGATE-HALFRIESZ-v1`

Inside the exact r32 packet (1.1)-(1.4), if some physical right-bank row has `eta_j=1`, then the law of `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2^(13/4) e^(3/4) s_3(A)^(-1)
 =20.140411857733373... s_3(A)^(-1).
}`                                                                  (6.5)

Therefore for every interval `I`,

`P(Q in I)
 <=2^(13/4)e^(3/4)s_3(A)^(-1)|I|`.                                (6.6)

This covers **all** exact-coloop angles, including the previously singular physical-pivot case `h_j=0`. It also covers `h_c=0` by the physical-coordinate branch; `h_j` and `h_c` cannot vanish simultaneously because `m>0`.

Continuity is **not proved** by this compiler. The conclusion here is essential boundedness plus linear small-ball scaling.

## 7. Designated partner applied to an actual inequality

Let `Q'` be an independent copy. The density in (6.5) has mass one, so

`||p_Q||_2^2 <= ||p_Q||_infinity`.                                (7.1)

Applying only the valid fleet04/B03 collision lemma (1.7),

`boxed:
 P(|Q-Q'|<=eps)
 <=2^(17/4)e^(3/4)s_3(A)^(-1) eps
 =40.280823715466745... s_3(A)^(-1) eps.
}`                                                                  (7.2)

This is a genuine partner-consumed linear collision estimate. No challenged weighted-L2 assertion from that partner report is used.

## 8. What this changes and what remains

This run closes the **exact** endpoint of the near-coloop collar left by r34. The mechanism is qualitatively different from the earlier fragile local-pivot route: at leverage one the entire complementary physical bank is first aggregated into the normalized one-dimensional projection `W`, and only then is a square pivot selected. The two possible square coefficients `(h_j,h_c)` form an orthogonal pair, so at least one is always of order `m`; the corresponding residual is a bilinear product between a scalar projection of one product bank and a selector from a disjoint product bank. Both its one-copy half-Riesz norm and its independent-copy weighted time integral are dimension-free.

The unrestricted three-large-eigenvalue conjecture remains **OPEN**. Full-target continuity remains **OPEN**. Within the r32/r34 exact angular packet, the remaining B03 collar is now strictly the **near-but-not-exact coloop regime**

`2/3 < eta_j < 1`, `eta_j ->1`,                                   (8.1)

with simultaneous angular cancellation of the physical coefficient. In that regime the complementary frame has one unit-scale direction and one weak direction of energy `1-eta_j`; the next mechanism must retain that weak direction rather than delete it or impose a conditional density cap. A natural next step is a regularized two-direction version of the aggregate compiler, interpolating between the determinant-entropy estimate of r32 and the exact one-dimensional aggregate proved here.

No task/schedule state, notification/email setting, permission, public-release state, paid model/API/Codex action, installation, or cross-account authentication is changed by this report.
