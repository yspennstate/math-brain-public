# account02/B03 — finite-coordinate TT* Hölder closure is nonuniform

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control read: `2026-09-22.11`  
Assignment: Decoupled time integral  
Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL TARGET OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and dependency

The target is the universal essential-density bound for `Q=X^T A X` under independent real input densities `f_i<=1` when `A` has at least three eigenvalues of modulus at least one. This report does not claim the full theorem.

The designated partner result is account03/B03 run `20260922T165635Z-account03-B03-QFORM-r16`, canonical source `yspennstate/math-open-problems@16849154c191385e444059bd0a43a2c8a2bba674`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T165635Z-account03-B03-QFORM-r16/REPORT.md`, blob `ccff06141088ee91b459276139554a340b62b1a0`. Its exact pair-law identity is used below, including the dependence between `U=X+X'` and `V=X-X'`.

The live corrections consumed include at least `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-ONEPAIR-NORMALIZED-TTSTAR-FALSE-v1`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, and `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`. No arbitrary-joint coarea, post-rotation independence, or conditional-cap premise is used.

## 2. Partner identity and the natural multi-pair closure

For one cap-one density `f`, let `X,X'` be iid, `U=X+X'`, `V=X-X'`,

`h_u(v)=(1/2)f((u+v)/2)f((u-v)/2)`, `m(u)=int h_u(v)dv=(f*f)(u)`,

and `H_u(s)=int exp(isv)h_u(v)dv`. The partner proves

`|H_u(s)|<=m(u)`

and, for `a!=0`,

`int |H_u(a t)|^2 dt <= pi m(u)/|a|`.                    (2.1)

Interpolating (2.1) with the `L^infinity` bound gives, for every `2<=p<infinity`,

`||H_u(a .)||_p <= pi^(1/p) m(u)^(1-1/p) |a|^(-1/p)`.    (2.2)

For the diagonal control form `A=I_d`, `(Au)_j=u_j`. If a set `S` of `r>=2` coordinates is assigned exponents `p_j>=2` with

`sum_{j in S} 1/p_j = 1`,

then taking absolute values in the partner identity, applying Tonelli, time-Hölder to the coordinates in `S`, and only `|H|<=m` to the remaining coordinates produces

`int |phi(t)|^2 dt <= B_S(f):=pi prod_{j in S} T_{p_j}(f)`,                (2.3)

where

`T_p(f)=int_0^infinity (f*f)(u)^(1-1/p) u^(-1/p) du`.                    (2.4)

This is the most direct fixed-coordinate extension of the one-pair TT* step: it does not normalize a conditional law, and it can use two, three, or any fixed number of pair variables before time-Hölder.

## 3. A cap-one scale-mixture making every such certificate diverge

Fix `L>=4`, put `R_k=L^k`, `I_k=[R_k,2R_k]`, and for integer `N>=2` define

`f_N(x)=(1/N) sum_{k=1}^N R_k^(-1) 1_{I_k}(x)`.                         (3.1)

The intervals are disjoint, every component has mass `1/N`, hence `int f_N=1`, and `||f_N||_infinity<=1/(N R_1)<=1`. Thus (3.1) is a source-valid input density.

Write `m_N=f_N*f_N`. For `2<=ell<=N`, set

`J_ell=[R_ell+2R_{ell-1}, 2R_ell+R_1]`.                                 (3.2)

For every `k<ell`, the convolution of the `k`th and `ell`th interval components has its constant plateau on

`[R_ell+2R_k, 2R_ell+R_k]`.

Hence all these plateaux contain `J_ell`. Each ordered cross term contributes `1/(N^2 R_ell)` there, so both orders together give

`m_N(u) >= 2(ell-1)/(N^2 R_ell)` for every `u in J_ell`.                (3.3)

Also

`|J_ell|=R_ell-2R_{ell-1}+R_1 >= R_ell/2`,

and `u<=3R_ell` on `J_ell`. The `J_ell` are mutually disjoint because `L>=4`.

Therefore, for every `p>=2`,

`T_p(f_N)`
` >= sum_{ell=2}^N |J_ell| [2(ell-1)/(N^2 R_ell)]^(1-1/p) (3R_ell)^(-1/p)`
` >= 6^(-1/p) N^(-2+2/p) sum_{r=1}^{N-1} r^(1-1/p)`
` >= [6^(-1/p)/(2-1/p)] N^(-2+2/p) (N-1)^(2-1/p)`.                    (3.4)

In particular

`T_p(f_N) >= c_p N^(1/p)(1-o(1))`, `c_p=6^(-1/p)/(2-1/p)>0`.           (3.5)

Now let `S` and `p_j` obey the Hölder relation in Section 2. Multiplying (3.4) and using `sum 1/p_j=1` gives

`B_S(f_N) >= pi C_(p_j) N (1-o(1))`,                                   (3.6)

with an explicit positive constant `C_(p_j)=prod_j c_{p_j}`. Thus *every finite-coordinate closure obtained by taking absolute values in the `u`-integral and then combining the partner's per-coordinate `L^2/L^infinity` bounds through time-Hölder has a law-dependent certificate growing at least linearly in `N`.*

This includes the two-pair choice `(p_1,p_2)=(2,2)` and the three-pair symmetric choice `(3,3,3)`. It is strictly stronger than the partner's one-pair normalized-sumset obstruction: simply using several pair variables coordinatewise does not repair the fragmentation loss.

## 4. The divergence is entirely an artifact of the closure

Take `d=3`, `A=I_3`, and iid inputs with density `f_N`. This is already inside the target. The proved diagonal theorem gives

`||p_Q||_infinity <= pi`, `Q=X_1^2+X_2^2+X_3^2`.                       (4.1)

Hence `||p_Q||_2^2<=pi`, and by Plancherel

`int |phi(t)|^2 dt = 2pi ||p_Q||_2^2 <= 2pi^2`.                         (4.2)

So the true integrated collision quantity stays uniformly bounded while the coordinatewise TT* Hölder certificate (3.6) tends to infinity. The loss comes from moving the absolute value through the `u`-integral and paying the scale-fragmented Renyi factors separately, not from the QFORM law itself.

Equivalently, in the exact formula

`H_u(tu)=exp(-it u^2) int exp(2itu x) f(x)f(u-x) dx`,                    (4.3)

the phase `exp(-it u^2)` and the remaining `u`-oscillation carry cancellations that (2.3) destroys. Any successful bank TT* argument must retain this joint `u`-oscillation (or switch to a different product-preserving scalar-conditioning mechanism) before applying absolute values.

## 5. Classification and corrected next implication

**Refuted mechanism:** `FINITE-PAIR-COORDINATEWISE-HOLDER-PLANCHEREL-TTSTAR` as a law-uniform route under only `f_i<=1`.

This is not a counterexample to QFORM. It is a source-valid adversary already on the solved diagonal form.

**Corrected next implication:** derive a genuinely bank-level identity/estimate in which the `u` variables are aggregated *before* absolute value or normalization. A sufficient future decoupled-time step must exploit cancellation in the joint `u` integral, or couple the pair-law identity to a valid scalar-pivot/half-Riesz argument. Merely selecting any fixed finite number of pair variables and interpolating their one-coordinate Plancherel bounds cannot be dimension/law uniform.

No numerical computation is used in this report; all bounds above are exact analytic inequalities.

Full target status: **OPEN**. Continuity: **not proved here**.
