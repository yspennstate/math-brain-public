SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T22:50:09Z.
attacking: QFORM-EPSILON-UNIFORM-PHASEWEIGHTED-TTSTAR-v1 — stabilize the punctured two-bank Fourier receiver under arbitrary same-bank phases, then test whether the remaining epsilon bridge can possibly be perturbative.

# fleet02/B16 r37 — phase-weighted punctured receiver + nonperturbative epsilon obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** projection-product interaction / complementary source-valid constructions  
**Status:** `NEW SUPPORTING THEOREM + NEW SOURCE-VALID MECHANISM OBSTRUCTION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Regularity:** the punctured theorem below gives a continuous `C_0` density on its scope; global continuity remains open.

## 1. First unpaid implication

**`QFORM-EPSILON-UNIFORM-PHASEWEIGHTED-TTSTAR-v1` (OPEN).** In the canonical shared-hub two-bank packet, prove an estimate uniform through `epsilon=0` while keeping a common `P`-frequency/Hilbert pairing across both original-product banks. The newest fleet03/B16 fragmented-slice construction has already ruled out freezing physical `P` and using Minkowski. The present run pays a second issue: arbitrary same-bank quadratic phases do not obstruct the punctured receiver. It also rules out a different tempting bridge: law-uniform perturbative continuity in the small coefficient `epsilon`.

The remaining mechanism must therefore be genuinely nonperturbative in `epsilon` and dependence-preserving.

## 2. Phase-weighted source pushforwards preserve the projection-product energy

Let one original-coordinate source bank be `X`, and let

`Y=(L,V,P)=T X`

have density `g(l,v,p)`. Let `R(X)` be any real measurable function, including an arbitrary quadratic form on that same bank. For fixed Fourier time `t`, define the complex pushforward

`mu_t(E)=E[ exp(i t R(X)) 1_{Y in E} ]`.

Disintegrating over `Y` gives an absolutely continuous complex measure with density

`h_t(y)=g(y) E[exp(i t R(X)) | Y=y]`,

and therefore the pointwise domination

`boxed: |h_t(y)| <= g(y).`                                          (2.1)

For the partial `P`-Fourier slice

`h_(t,zeta)(l,v)= integral_R exp(i zeta p) h_t(l,v,p) dp`

and the genuine `(L,V)` marginal

`m(l,v)=integral_R g(l,v,p) dp`,

we have

`|h_(t,zeta)(l,v)| <= m(l,v)`.                                     (2.2)

Thus if `||m||_infinity<=M_2`,

`boxed: ||h_(t,zeta)||_2^2 <= M_2`                                 (2.3)

uniformly in both `t` and `zeta`. With Fourier convention

`hat f(xi)=integral exp(-i xi x)f(x)dx`,

two-dimensional Plancherel gives

`boxed: integral_R2 |Phi_t(xi,nu,zeta)|^2 dxi dnu <= (2pi)^2 M_2`,  (2.4)

where `Phi_t` is the full Fourier transform of `h_t`. Likewise, if `||g||_infinity<=M_3`, then

`boxed: integral_R3 |Phi_t|^2 <= (2pi)^3 M_3`.                      (2.5)

No coordinate of `(L,V,P)` is declared independent. The only independence used later is between disjoint original source banks. In particular, adding an arbitrary same-bank phase does not destroy the exact Hilbert energy furnished by the product-projection density bounds.

The required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` supplies the completed two-dimensional bounded-density projection bound used here. For an orthonormal two-dimensional projection of independent cap-one originals,

`||m||_infinity <= 2`,

so (2.3) becomes the actual inequality

`boxed: sup_(t,zeta) ||h_(t,zeta)||_2 <= sqrt(2).`                   (2.6)

This is exactly the safe frequency-side interface that survives the latest partner obstruction: fleet03/B16 r34 showed that the corresponding physical-slice mixed norm `L^1_P L^2_(L,V)` can grow like `sqrt(N)` even for an orthogonal image of independent cap-one sources.

## 3. The punctured two-bank Fourier theorem is stable under arbitrary same-bank phases

Let `H`, source bank `A`, and source bank `B` be mutually independent. Let

`Y_i=(L_i,V_i,P_i)`

have density `g_i`, with `(L_i,V_i)` marginal `m_i`. Let `R_i` be an arbitrary real measurable function of the original coordinates in bank `i`. Put

`L=L_A+L_B`, `V=V_A+V_B`, `P=P_A+P_B`,

`K_2=(M_(2,A) M_(2,B))^(1/2)`, `K_3=(M_(3,A) M_(3,B))^(1/2)`,

where

`||m_i||_infinity<=M_(2,i)`, `||g_i||_infinity<=M_(3,i)`.

Assume the independent hub has density cap `L_H`. Consider

`Q = 2 alpha H L + beta L^2 + 2 delta L V + lambda V^2 + 2 epsilon L P`
`    + R_A + R_B + affine`,                                         (3.1)

with

`alpha*epsilon*lambda != 0`.

### `QFORM-PHASEWEIGHTED-PUNCTURED-TWOBANK-v1`

The law of `Q` has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= 3 [ L_H K_2 K_3 / |alpha epsilon lambda| ]^(1/3).` (3.2)

### Proof

The fleet03/B16 r30 punctured proof starts by pushing each bank to `(L_i,V_i,P_i)` and then using the product of their bank Fourier transforms. With the added phases `R_A,R_B`, replace the positive pushforwards `g_i dy` by the complex phase-weighted pushforwards `h_(i,t)dy` from Section 2. Because the original banks are disjoint and independent, the two complex measures still convolve exactly; no projected independence is used.

For fixed common `P` frequency `zeta`, define the phase-weighted bank transforms `Phi_(i,t)(xi,nu,zeta)` and

`S_t(zeta)=integral_R2 |Phi_(A,t)(xi,nu,zeta) Phi_(B,t)(xi,nu,zeta)| dxi dnu`.

By (2.4) and Cauchy--Schwarz,

`||S_t||_infinity <= (2pi)^2 K_2`.                                 (3.3)

By (2.5), three-dimensional Plancherel, and Cauchy--Schwarz,

`integral_R S_t(zeta) dzeta <= (2pi)^3 K_3`.                       (3.4)

Hence

`||S_t||_2 <= (2pi)^(5/2) (K_2 K_3)^(1/2)`.                        (3.5)

Those are exactly the two bank-energy inputs of r30 and they are uniform in the arbitrary same-bank phases. The independent hub Plancherel estimate is unchanged:

`||hat f_H||_2^2 <= 2pi L_H`.                                      (3.6)

After exact integration of the `P` phase and the one-dimensional Fresnel integral in `V`, the r30 calculation therefore again gives

`|phi_Q(t)| <= pi^(3/2) sqrt(L_H K_2 K_3)`
`              * |alpha epsilon lambda|^(-1/2) |t|^(-3/2)`.        (3.7)

Combining with `|phi_Q(t)|<=1` yields

`integral_R |phi_Q(t)| dt <= 6 [pi^(3/2) sqrt(L_H K_2 K_3)`
`                                 * |alpha epsilon lambda|^(-1/2)]^(2/3)`,

and Fourier inversion simplifies exactly to (3.2). Integrability of `phi_Q` gives the stated `C_0` density. QED.

Thus the punctured theorem already tolerates arbitrary within-bank quadratic curvature: phase-weighting cannot be blamed for the remaining `epsilon -> 0` gap.

For authentic product banks whose three-row coefficient Gram is at least `kappa I_3`, the bounded-density projection theorem gives

`M_(2,i)<=2/kappa`, `M_(3,i)<=2^(3/2) kappa^(-3/2)`,

and therefore

`boxed: ||p_Q||_infinity <= 3*2^(5/6) kappa^(-5/6)`
`                           * |alpha epsilon lambda|^(-1/3).`       (3.8)

## 4. A strict target family with genuinely nontrivial same-bank quadratic phases

Take seven independent cap-one physical sources

`H, X_1,X_2,X_3, Y_1,Y_2,Y_3`.

Set

`L=X_1+Y_1`, `V=X_2+Y_2`, `P=X_3+Y_3`,

and, for `theta=1/4`,

`R_A=theta(X_1^2+X_2^2+X_3^2)`,
`R_B=-theta(Y_1^2+Y_2^2+Y_3^2)`.

For `epsilon != 0` define

`Q_(epsilon,theta)=2HL+V^2+2epsilon LP+R_A+R_B`.                    (4.1)

Each bank density and each `(L_i,V_i)` marginal is a literal product of cap-one scalar densities, so here

`L_H<=1`, `M_(2,A),M_(2,B),M_(3,A),M_(3,B)<=1`.

The theorem gives the concrete target inequality

`boxed: ||p_(Q_(epsilon,1/4))||_infinity <= 3 |epsilon|^(-1/3).`    (4.2)

This family is genuinely inside the owner target. At `theta=0`, pass to symmetric/antisymmetric coordinates for the two banks. The only nonzero carrier block has eigenvalues

`2`, `+sqrt(2+4epsilon^2)`, `-sqrt(2+4epsilon^2)`.

The same-bank perturbation `R_A+R_B` has operator norm `|theta|=1/4`. Weyl therefore leaves two positive eigenvalues and one negative eigenvalue with modulus at least

`sqrt(2)-1/4 = 1.1642135623... > 1`.                                (4.3)

So (4.2) is a source-valid density estimate on a strict three-large-eigenvalue family carrying nontrivial same-bank quadratic phases. Continuity follows on every punctured member.

## 5. A source-valid exact-target obstruction to perturbative epsilon comparison

The remaining bridge cannot be obtained by proving that the `epsilon LP` operator is uniformly close to the `epsilon=0` operator as `epsilon -> 0`. The obstruction already occurs with four independent physical coordinates.

For `epsilon>0`, put

`R_epsilon=pi/(2epsilon)`

and take independent cap-one variables

`H,V ~ Unif[0,1]`,
`L,P ~ Unif[R_epsilon,R_epsilon+1]`.

Using the SAME source laws for both forms, define

`Q_epsilon = 2HL + V^2 + 2epsilon LP`,
`Q_0       = 2HL + V^2`,                                            (5.1)

and choose

`t_epsilon=1/R_epsilon=2epsilon/pi`.

Uniformly on the product support,

`2t_epsilon HL = 2H(1+O(R_epsilon^(-1))) -> 2H`,
`t_epsilon V^2 -> 0`,
`2epsilon t_epsilon LP = pi + O(epsilon)`.                          (5.2)

Dominated convergence therefore gives

`phi_epsilon(t_epsilon) -> -e^i sin(1)`,
`phi_0(t_epsilon)       -> +e^i sin(1)`,

and hence

`boxed: lim_(epsilon downarrow0) |phi_epsilon(t_epsilon)-phi_0(t_epsilon)|`
`       = 2 sin(1) = 1.6829419696...`.                              (5.3)

In particular

`boxed: liminf_(epsilon downarrow0) sup_t |phi_epsilon(t)-phi_0(t)| >= 2 sin(1).` (5.4)

### `QFORM-EPSILON-NONPERTURBATIVE-CHARACTERISTIC-OBSTRUCTION-v1`

There is no law-uniform sup-in-time perturbative continuity of the canonical `LP` coupling at `epsilon=0`, even over exact-rank-three QFORM instances with independent cap-one physical sources.

Indeed the matrix of `Q_epsilon` in `(H,L,V,P)` is

`[[0,1,0,0], [1,0,0,epsilon], [0,0,1,0], [0,epsilon,0,0]]`,

whose nonzero spectrum is exactly

`boxed: {1, +sqrt(1+epsilon^2), -sqrt(1+epsilon^2)}.`               (5.5)

Every member is therefore a strict owner-target instance. The mechanism behind (5.3) is simply an allowed translation of the source laws: with no centering, support-diameter, moment, or tail assumption, a coefficient of size `epsilon` can be compensated by sources centered at scale `epsilon^(-1)` and Fourier time of scale `epsilon`.

This is not a counterexample to QFORM. In fact the required pinned `COUNTEREXAMPLE_SEARCH.md` supplies a completed result at the exact same family: its ruled one-sheet theorem for signature `(+,+,-)` gives

`boxed: p_(Q_epsilon)(s) <= pi sqrt(2) = 4.4428829381...`

for a.e. `s>=0`.                                                     (5.6)

Thus the density remains uniformly bounded on the one-sheet side even though the characteristic functions are not uniformly perturbatively close to the zero-coupling endpoint.

## 6. Latest designated partner applied

The newest compatible fleet03/B16 handoff read before publication is r34, canonical report `math-open-problems@a76d586c873087ec72d884368b5093eb24fc03c9`. It proves the authentic fragmented obstruction

`B(g)=int ||g(.,.,p)||_(L2(dl dv)) dp -> infinity`

like `sqrt(N)` for an exact orthogonal image of three independent cap-one laws. Hence physical `P` slicing plus Minkowski is not available.

The present theorem applies directly to r34's stated successor packet. Its open form includes arbitrary within-bank quadratic phases; Section 3 shows those phases can be absorbed into the complex source pushforwards without changing either bank-energy estimate. The punctured branch therefore retains r30's density bound with exactly the same constant. What remains is only the genuinely uniform bridge through `epsilon=0`.

Section 5 then removes a second naive route from that bridge: one cannot compare the `epsilon` and zero operators in a law-uniform sup-characteristic-function norm. The successful vector TT* argument must exploit the common `P` frequency nonperturbatively at each `epsilon`, while preserving source-bank independence and never upgrading a projected joint density to independence or a worst-fiber cap.

## 7. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The results here are a supporting punctured theorem and a proof-mechanism obstruction. Arbitrary additional spectrum beyond the exact-rank-three structural packets remains a separate global interface; global continuity remains open.

Required pinned source read and used: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.
