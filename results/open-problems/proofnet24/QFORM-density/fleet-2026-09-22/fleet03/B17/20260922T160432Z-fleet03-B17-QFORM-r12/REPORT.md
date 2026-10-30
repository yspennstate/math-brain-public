# fleet03/B17 — finite-m disjoint-bank closure and exact rotated witness

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T160432Z-fleet03-B17-QFORM-r12`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `PROVED_SUPPORTING_LEMMA / EXACT_ROTATED_WITNESS`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and delta from the preceding B17 run

The full target remains: for every dimension, every independent real input family with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a dimension-free essential-density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is a separate desired conclusion.

The preceding B17 run closed only the **weak-limit** rare-fragment branch for the exact block family

`A_m = diag(J_m/m, J_m/m, -J_m/m)`.

It explicitly left open the possibility that the finite-`m` laws could develop narrow density spikes invisible under weak convergence. The main theorem below closes that gap for every `m` and, in fact, for a larger arbitrary-law disjoint-bank class.

The designated partner `fleet04/B17` still has no completed QFORM handoff visible at the fresh partner scan. I therefore do not invent a partner result. I apply the compatible completed `fleet04/B18` Schur-pivot theorem to the same family and compare its exact inequality with the new aggregate-bank inequality.

No false pointwise oscillatory decay, rotated-coordinate independence, conditional-cap substitution, single-minor extraction, bounded-fragment-count reduction, or Monte Carlo histogram is used.

## 2. External sharp projection input

I use the one-dimensional case of the product-marginal theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949: if `X=(X_1,...,X_N)` has independent coordinates with probability densities bounded by one and `r` is a unit vector, then the one-dimensional projection

`Y=<r,X>`

has a density satisfying

`||p_Y||_infinity <= sqrt(2)`.                                      (2.1)

For `k=1` this is the sharp Rogozin/Ball cube-slicing constant. It applies to arbitrary measurable cap-one densities; no support or moment assumption is introduced.

## 3. A square-pushforward estimate with only an L-infinity cap

Let `Y` have density `f` with `||f||_infinity<=M`, and let `lambda != 0`. The variable `U=lambda Y^2` has an a.e. density on its supporting half-line satisfying

`g_U(u) <= M / sqrt(|lambda| |u|)`.                                (3.1)

For `lambda>0`, this follows from

`g_U(u)=[f(sqrt(u/lambda))+f(-sqrt(u/lambda))]/[2 sqrt(lambda u)]`,

and `lambda<0` is obtained by reflection.

If `U_1,U_2` are independent square terms with coefficients of the same sign, then after reflecting that common sign if necessary,

`||p_{U_1+U_2}||_infinity`
` <= (M_1 M_2)/sqrt(|lambda_1 lambda_2|)`
`    * integral_0^w [u(w-u)]^(-1/2) du`
` = pi M_1 M_2 / sqrt(|lambda_1 lambda_2|)`.                        (3.2)

The beta integral is exactly `pi` and is independent of `w>0`.

## 4. Main theorem: finite-m disjoint-three-bank closure

### Theorem `QFORM-DISJOINT-THREE-BANK-2PI-v1`

Let the physical coordinate set be partitioned into four disjoint sets

`I_1, I_2, I_3, I_0`.

For `j=1,2,3`, let `r_j` be a unit vector supported on `I_j` and let `|lambda_j|>=1`. Let `A_0` be an arbitrary real symmetric matrix supported on `I_0`. Define

`A = lambda_1 r_1 r_1^T + lambda_2 r_2 r_2^T + lambda_3 r_3 r_3^T + A_0`.

For arbitrary independent real `X_i` with probability densities bounded by one, `Q=X^T A X` has an absolutely continuous law with

`||p_Q||_infinity <= 2 pi`.                                       (4.1)

No compact support, moments, centering, log-concavity, or connected-support hypothesis is needed.

### Proof

Set

`Y_j=<r_j,X_{I_j}>`, `j=1,2,3`,

and

`R=X_{I_0}^T A_0 X_{I_0}`.

Because the physical supports are disjoint, `Y_1,Y_2,Y_3,R` are mutually independent. This is original-coordinate independence; no independence after a general spectral rotation is asserted.

By (2.1),

`||p_{Y_j}||_infinity <= sqrt(2)`                                  (4.2)

for every `j`. Among the three real numbers `lambda_1,lambda_2,lambda_3`, two have the same sign. Relabel them `lambda_1,lambda_2`. Applying (3.2) and `|lambda_1 lambda_2|>=1` gives

`||p_{lambda_1 Y_1^2 + lambda_2 Y_2^2}||_infinity <= 2 pi`.         (4.3)

The remaining random variable

`T=lambda_3 Y_3^2+R`

has some probability law `mu_T`, with no density assumption needed. Independence gives

`p_Q(x)=integral p_S(x-t) d mu_T(t)`,

where `S=lambda_1Y_1^2+lambda_2Y_2^2`. Hence

`||p_Q||_infinity <= ||p_S||_infinity <= 2 pi`.

This also proves absolute continuity. QED.

**Continuity status:** the argument proves an essentially bounded density but does **not** prove a continuous representative for arbitrary measurable input densities.

## 5. Immediate closure of the previous hidden-spike gap

For

`A_m=diag(J_m/m,J_m/m,-J_m/m)`,

let `r_1,r_2,r_3` be the three normalized block-constant vectors. They have pairwise disjoint physical supports and unit norm, and the active coefficients are `+1,+1,-1`. Therefore Theorem (4.1) yields, for **every finite m** and **every** cap-one independent physical input law,

`||p_{Q_m}||_infinity <= 2 pi`.                                    (5.1)

In particular, every fragmented triangular array from B17 run r11 is uniformly bounded at finite `m`; narrow finite-`m` spikes above `2 pi` are impossible. The previous weak-limit theorem gave a sharper limiting ceiling `3 sqrt(2)` for its finite-intensity compound-Poisson subclass, but weak convergence was not needed for (5.1).

The already established centered-uniform CLT sequence on this same block family gives the target-level necessary lower bound

`C >= 3 sqrt(2) = 4.242640687119...`,

so this block geometry is now rigorously trapped between the known lower-bound endpoint and the universal finite-m upper bound `2 pi = 6.28318...`. This does not identify the global sharp constant.

## 6. Applying a completed fleet04 result: why one physical triple loses the bank scale

The completed `fleet04/B18` result, canonical report

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

proves for a physical `3x3` principal block `B`, a nonzero scalar pivot `a`, and a definite Schur complement,

`||p_Q||_infinity <= 2 sqrt(pi) / |a det B|^(1/4)`.                 (6.1)

Apply it to `A_m` by selecting one physical coordinate from each bank. The principal block is

`B_m=diag(1/m,1/m,-1/m)`.

Choose the negative scalar pivot `a=-1/m`; its Schur complement is `diag(1/m,1/m)`, which is definite, and

`det B_m=-1/m^3`.

Thus the completed partner inequality gives exactly

`||p_{Q_m}||_infinity <= 2 sqrt(pi) m`.                             (6.2)

This diverges with `m`, whereas the aggregate-bank theorem gives `2 pi` uniformly. This is not a defect in the fleet04 theorem; it is an exact demonstration that the missing structural operation is **aggregation of a disjoint coordinate bank before paying reciprocal local curvature/minor factors**.

## 7. Exact rotated six-variable stress witness

The assignment also asks for exact rotated witnesses rather than only diagonal controls. Let

`X_1,...,X_6 iid Uniform[-1/2,1/2]`

and set

`Y_1=(X_1+X_2)/sqrt(2)`,
`Y_2=(X_3+X_4)/sqrt(2)`,
`Y_3=(X_5+X_6)/sqrt(2)`.

Each `Y_j` has the triangular density

`f(y)=sqrt(2)(1-sqrt(2)|y|)` for `|y|<=1/sqrt(2)`.

Consider

`Q_rot = Y_3^2 - 2 Y_1 Y_2`.                                      (7.1)

In the orthonormal active basis `(u_1,u_2,u_3)`, where each `u_j` is the normalized constant vector on the corresponding two-coordinate bank, the quadratic matrix is

`B=[[0,-1,0],[-1,0,0],[0,0,1]]`.

Hence the physical six-dimensional matrix

`A_rot=-u_1u_2^T-u_2u_1^T+u_3u_3^T`

has exact spectrum

`{+1,+1,-1,0,0,0}`.                                                (7.2)

Its eigenvectors in the first four physical coordinates mix the first two independent banks, so this is a genuinely rotated indefinite target stress rather than a diagonal square control.

### Exact density at the saddle value

Using the delta/coarea identity at zero,

`p_Qrot(0)=integral f(x) f(y) f(z) delta(z^2-2xy) dx dy dz`.

Only the two same-sign `(x,y)` quadrants contribute. Put

`x=u/sqrt(2)`, `y=v/sqrt(2)`, `0<=u,v<=1`.

The root `z=sqrt(2xy)=sqrt(uv)` lies in the support exactly when `uv<=1/2`. Thus, with

`D={(u,v) in [0,1]^2: uv<=1/2}`,

one obtains

`p_Qrot(0)=2 sqrt(2) integral_D (1-u)(1-v)[(uv)^(-1/2)-sqrt(2)] du dv`. (7.3)

The two elementary integrals are

`I_0=integral_D (1-u)(1-v) du dv`
`   = -3/16 + (5/8) log 2`,                                       (7.4)

and

`I_1=integral_D (1-u)(1-v)(uv)^(-1/2) du dv`
`   = (sqrt(2)/18)(8+21 log 2)`.                                  (7.5)

Therefore

`p_Qrot(0)=2 sqrt(2) I_1 - 4 I_0`
`          = 91/36 + (13/6) log 2`
`          = 4.0295966689909926...`.                               (7.6)

For comparison, the exact six-variable diagonal two-per-bank witness previously computed at the corresponding saddle has

`2 pi - 7/3 = 3.949851973846253...`.

Thus this exact rotation raises that finite witness by

`91/36+(13/6)log2-(2pi-7/3)`
`=0.0797446951447394...`,                                          (7.7)

although it remains below the known global lower bound `3 sqrt(2)` by about `0.2130440181`. Hence it does not improve the current universal lower bound, but it is an exact analytic demonstration that a nontrivial spectral rotation can increase the density peak even for a fixed six-input bank law.

## 8. Implication for the full target

Two concrete witness mechanisms are now excluded from being the missing obstruction:

1. The entire finite-`m` disjoint-three-bank rank-three geometry is uniformly bounded by `2 pi`, for arbitrary cap-one laws, so the previous rare-fragment hidden-spike possibility is closed.
2. A simple exact bank rotation does increase a density peak, so a proof cannot rely on the heuristic that diagonal orientation is always worst; nevertheless this witness remains below the established `3 sqrt(2)` lower bound.

The next B17 witness search should therefore leave the separable disjoint-bank geometry and test **shared-coordinate active frames**, where one physical coordinate has leverage in more than one active direction, preferably with multiscale fragmented extreme-product laws. That is the regime in which Rogozin/Ball projection aggregation no longer produces three independent projected coordinates and where a new sharp obstruction, if one exists, can still hide.

The full QFORM conjecture remains **OPEN / NOT PROVED**.

## 9. Source/status notes

- External projection theorem: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; one-dimensional marginal constant `sqrt(2)`.
- Compatible fleet04 result actually applied: fleet04/B18, `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.
- Designated fleet04/B17: no completed QFORM handoff visible at the fresh pre-publication scan.
- Full solution status: OPEN.
- Continuous density for the full target: OPEN. Theorem (4.1) only asserts an essentially bounded density.
