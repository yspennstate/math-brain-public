SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-23T23:57:05Z.
attacking: the live small-diagonal overlap-one endpoint by a three-group triangle Plancherel estimate; in particular, pay the exact rank-one light-crossing star packet where every disjoint rank-three crossing receiver vanishes.

# fleet03/B03 r43 — triangle Plancherel closure of the exact rank-one anchored-star endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: decoupled time integral  
Classification: **NEW SUPPORTING THEOREM / LIVE FRONTIER SUBBRANCH PAID / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The branch proved below has a continuous `C_0` density.

## 1. Fresh source boundary and exact live debt


The newest fleet03/B20 operator-overlap compiler used here is

`yspennstate/math-open-problems@010ccf4cdc4f0b07d0a443eba99fd147e6feab65`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T234606Z-fleet03-B20-QFORM-r42/REPORT.md`,

plus its late frontier splice at `yspennstate/math-open-problems@eb50a2dc3acc7884f284a1f94847106c89bf5889`.

After the already-paid physical-diagonal, physical-principal-triple and disjoint-`E_3` exits, every remaining target state has small physical diagonals and a localized overlap-two or overlap-one packet. In the overlap-one branch there are one original coordinate `j` and disjoint original-coordinate banks `R,C` such that the anchored block

`M=A[{j} union R,{j} union C]=[[b,r^T],[c,N]]`                    (1.1)

has anchored third-volume

`J_sep := sum_{|P|=|Q|=2, P subset R, Q subset C}
             det A[{j} union P,{j} union Q]^2 >= 1/2304`.        (1.2)

The corrected fleet04/B20 anchor inequality further gives either `E_2(N)>4/9` or
`||r|| ||c|| ||N||_F >=1/96`; neither alone pays the exact rank-one `N` endpoint through a disjoint rank-three crossing, because all such augmented rank-three crossing volumes can vanish there.

The current interactive projected-crossing theorem is also consumed below at its exact scope:

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The designated B03 partner source is fleet04/B03 r1,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`,

whose collision lemma is applied in Section 6.

All live corrections are retained: no pointwise law-uniform quadratic-phase decay, no independence after rotation, no conditional cap for `X-X'` given `X+X'`, no arbitrary-joint coarea bound, and no deletion of small nonzero quadratic tails.

## 2. A three-group triangle Fourier theorem

The following is the main analytic result of this run.

### Theorem 2.1 — `QFORM-THREE-GROUP-TRIANGLE-PLANCHEREL-v1`

Let `Z` be a real random variable with density at most `M_0`. Let `X_R` and `X_C` be two further independent random banks, independent also of `Z`. Let

`Y=(Y_1,Y_2)` be a two-dimensional linear projection of `X_R`,
`W=(W_1,W_2)` be a two-dimensional linear projection of `X_C`,

and assume their joint densities satisfy

`||p_Y||_infinity <= M_R`,   `||p_W||_infinity <= M_C`.          (2.1)

No independence is assumed between `Y_1,Y_2` or between `W_1,W_2`.

Let `F_0,F_R,F_C` be arbitrary measurable real functions of their respective independent source banks. For arbitrary real `gamma,delta` and nonzero `sigma,alpha,beta`, set

`T = F_0(Z)+F_R(X_R)+F_C(X_C)
     +2 sigma Y_1 W_1
     +2 Z(gamma Y_1+alpha Y_2+delta W_1+beta W_2)`.               (2.2)

Then, with

`K := pi^(3/2) M_0 (M_R M_C)^(1/2) |sigma alpha beta|^(-1/2)`,   (2.3)

one has for every nonzero `t`

`boxed: |phi_T(t)| <= min{1, K |t|^(-3/2)}.`                    (2.4)

Consequently `T` has a continuous `C_0` density and

`boxed:
 ||p_T||_infinity
 <= 3 M_0^(2/3)(M_R M_C)^(1/3)|sigma alpha beta|^(-1/3).`        (2.5)

The whole-copy weighted time integral required by the B03 assignment obeys

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2 dt
 <= (24/5) K^(1/3).`                                             (2.6)

If `T'` is an independent copy of the whole variable `T`, then

`boxed:
 E|T-T'|^(-1/2)
 <= (24/(5 sqrt(2 pi))) K^(1/3).`                                (2.7)

Equation (2.7) uses `|phi_T(t)|^2=E exp(it(T-T'))` only for the whole copy difference. It never separates any conjugate coordinate sum from its difference.

### Proof

Push the complex measures `exp(itF_R)dP_R` and `exp(itF_C)dP_C` to the two-dimensional projections `Y,W`. Their Radon--Nikodym densities, denoted `b_t(y)` and `c_t(w)`, satisfy

`|b_t(y)|<=p_Y(y)`, `|c_t(w)|<=p_W(w)`.                          (2.8)

Likewise `a_t(z)=exp(itF_0(z))p_Z(z)` has `|a_t(z)|<=p_Z(z)<=M_0`.

Take partial Fourier transforms in the second coordinates,

`B_t(y_1,xi)=int b_t(y_1,y_2)e^(i xi y_2)dy_2`,
`C_t(w_1,eta)=int c_t(w_1,w_2)e^(i eta w_2)dw_2`,                (2.9)

and define

`G_R(xi)=int |B_t(y_1,xi)|^2dy_1`,
`G_C(eta)=int |C_t(w_1,eta)|^2dw_1`.                             (2.10)

Partial Plancherel and the density caps give

`int G_R(xi)dxi = 2pi int|b_t|^2 <=2pi M_R`,
`int G_C(eta)deta <=2pi M_C`.                                    (2.11)

For fixed `z`, the remaining `(y_1,w_1)` kernel is

`exp{i2t[sigma y_1w_1+gamma z y_1+delta z w_1]}`.               (2.12)

The two terms linear in `y_1,w_1` are unitary modulations. The operator

`Lf(y)=int exp(i2t sigma y w)f(w)dw`

has `L^2 -> L^2` norm `sqrt(pi/(|sigma t|))`. Hence

`|I_t(z)|
 <= sqrt(pi/(|sigma t|))
    [G_R(2t alpha z)G_C(2t beta z)]^(1/2).`                      (2.13)

Integrating against `|a_t(z)|<=p_Z(z)` and applying Cauchy--Schwarz with respect to the probability measure `p_Z(z)dz`,

`|phi_T(t)|
 <= sqrt(pi/(|sigma t|))
    [int p_Z(z)G_R(2t alpha z)dz]^(1/2)
    [int p_Z(z)G_C(2t beta z)dz]^(1/2).`                         (2.14)

Since `p_Z<=M_0`, (2.11) gives

`int p_Z(z)G_R(2t alpha z)dz <= pi M_0 M_R/(|t alpha|)`,
`int p_Z(z)G_C(2t beta z)dz <= pi M_0 M_C/(|t beta|)`.           (2.15)

Substitution into (2.14) proves (2.4).

Let `t_0=K^(2/3)`. Then

`int_R |phi_T(t)|dt
 <=2[t_0 + K int_(t_0)^infinity t^(-3/2)dt]
 =6K^(2/3).`                                                      (2.16)

Fourier inversion therefore gives a continuous `C_0` density and

`||p_T||_infinity <= (2pi)^(-1)6K^(2/3)`,

which is exactly (2.5).

Similarly,

`int_R |t|^(-1/2)|phi_T(t)|^2dt
 <=2 int_0^t0 t^(-1/2)dt
   +2K^2 int_t0^infinity t^(-7/2)dt
 =4K^(1/3)+(4/5)K^(1/3)
 =(24/5)K^(1/3)`,                                                 (2.17)

proving (2.6). The regularized one-dimensional Riesz identity

`int_R e^(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)`                  (2.18)

combined with the whole-copy identity gives (2.7). QED.

### Why this does not contradict the rank-one same-bank correction

The refuted interface `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1` allows a rank-one crossing plus arbitrary same-bank phases, which can collapse to `-(Y-Z)^2`. Theorem 2.1 has two additional **transverse physical edges** `Z--Y_2` and `Z--W_2`. They are exactly what supplies the two extra one-dimensional Plancherel factors in (2.15). No arbitrary phase is being called curvature.

## 3. Exact rank-one anchored-star determinant identity

Return to the live B20 anchored block (1.1). Suppose now that the light crossing has exact rank one,

`N=sigma u v^T`,                                                  (3.1)

with `u,v` unit and `sigma!=0`. Decompose the hub stars as

`c=c_parallel u+c_perp`, `c_perp perpendicular u`,
`r=r_parallel v+r_perp`, `r_perp perpendicular v`,               (3.2)

and put

`alpha=||c_perp||`, `beta=||r_perp||`.                           (3.3)

For every physical row pair `P subset R` and column pair `Q subset C`, direct determinant expansion gives

`det [[b,r_Q^T],[c_P,N_PQ]]
 = +/- sigma det[c_P,u_P] det[r_Q,v_Q]`.                          (3.4)

The `b` term vanishes because every `2x2` minor of rank-one `N` is zero. Summing squares and using Cauchy--Binet in the two exterior products yields the exact identity

`boxed: J_sep = sigma^2 ||c_perp||^2 ||r_perp||^2
                 = |sigma alpha beta|^2.`                        (3.5)

This identity is invariant under the signs of `sigma` and all affine data. In particular, (1.2) forces `sigma,alpha,beta` all nonzero.

## 4. Payment of the exact rank-one overlap-one endpoint

Define the genuine original-bank projections

`Y_1=<u,X_R>`, `Y_2=<c_perp/alpha,X_R>`,
`W_1=<v,X_C>`, `W_2=<r_perp/beta,X_C>`.                           (4.1)

Each pair is an orthonormal two-dimensional projection of a product of cap-one original coordinates, so the projection theorem used by the current projected-crossing source gives

`||p_Y||_infinity, ||p_W||_infinity <=2`.                        (4.2)

The three source groups `X_j`, `X_R`, `X_C` are genuinely independent. Every same-bank quadratic coefficient, every diagonal and every linear term can be absorbed into `F_0,F_R,F_C`. The full cross-bank part is exactly

`2 sigma Y_1W_1
 +2X_j(c_parallel Y_1+alpha Y_2+r_parallel W_1+beta W_2)`.        (4.3)

Therefore Theorem 2.1 applies with `M_0=1`, `M_R=M_C=2`, and by (3.5)

`boxed:
 ||p_Q||_infinity
 <=3*4^(1/3) J_sep^(-1/6).`                                      (4.4)

For the actual live packet `J_sep>=1/2304`,

`boxed: ||p_Q||_infinity <=17.3069948437.`                        (4.5)

Moreover this exact-rank-one branch has a continuous `C_0` density.

The assigned decoupled time estimate specializes to

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= (24/5)sqrt(pi)2^(1/3) J_sep^(-1/12).`                         (4.6)

At `J_sep=1/2304` its right side is `20.4346111767`. The whole-copy half-Riesz bound is at most `8.1522303819` at that threshold.

This is a genuine payment of a live full-ambient subbranch: no outside coordinate remains after the B20 split `{j} union R union C`, and no same-bank curvature is discarded.

## 5. Relation to the current projected-crossing theorem

The owner continuation asks B01--B04 to apply the new projected-crossing theorem to an actual surviving partition. On the same anchored block, assume `r!=0` and set

`C_r=N(I-Pi_r)`, `Z_2(r)=e_2(C_r C_r^T)`.                        (5.1)

If the two-volume row marginals of `C_r` are all at most `1/2`, the `k=1, ell=2` grouped-hub theorem applies literally to hub `j` and right bank `C`, giving

`||p_Q||_infinity
 <=3*2^(7/6) exp(1/3) (||r||^2 Z_2(r))^(-1/6).`                  (5.2)

This is an actual equation on the live B20 partition. There is also the exact exterior identity

`e_3([r^T;N][r^T;N]^T)
 = e_3(NN^T)+||r||^2 Z_2(r)`.                                    (5.3)

Thus the new projected theorem gives a slightly smaller constant when its marginal gate holds, while the newer marginal-free disjoint-`E_3` receiver pays whenever the total left side of (5.3) is quantitatively large. Crucially, both mechanisms are blind at the exact rank-one star endpoint: when `rank N=1`, the augmented block `[r^T;N]` has rank at most two and the left side of (5.3) vanishes. The triangle theorem in Sections 2--4 pays precisely that missing endpoint through the anchored volume (3.5).

A useful quantitative residual statement follows from the compound-tail identity. If both augmented disjoint crossings are small,

`e_3([r^T;N][r^T;N]^T)<=eta`,
`e_3([c^T;N^T][c^T;N^T]^T)<=eta`,                               (5.4)

then `e_3(NN^T)<=eta`. In the B20 alternative `E_2(N)>4/9`, if the squared singular values of `N` are `lambda_1>=lambda_2>=...` and `T_2=sum_(i>=3)lambda_i`, the exact compound-tail inequality

`T_2 E_2(N) <=3 e_3(NN^T)`                                      (5.5)

gives

`boxed: T_2 < (27/4) eta.`                                       (5.6)

So after the marginal-free `E_3` exits, the unpaid `E_2(N)>4/9` survivor is quantitatively close in Frobenius tail to rank at most two. Theorem 4.4 pays the exact rank-one endpoint of that low-rank collar. The near-rank-one/rank-two interpolation remains open.

## 6. Designated fleet04/B03 result applied

The completed fleet04/B03 collision report proves, for any density `p`,

`Pr(|Y-Y'|<=epsilon) <=2 epsilon ||p||_2^2`,                     (6.1)

while explicitly retaining the dependence inside the underlying sum/difference pairs.

Apply (6.1) to the actual variable `Q` in the rank-one anchored-star branch. Since `p_Q` is a probability density,

`||p_Q||_2^2 <=||p_Q||_infinity`.                               (6.2)

Combining (6.1), (6.2), and (4.4) gives the concrete partner-consumed inequality

`boxed:
 Pr(|Q-Q'|<=epsilon)
 <=6*4^(1/3) J_sep^(-1/6) epsilon.`                              (6.3)

At the live threshold `J_sep>=1/2304`,

`Pr(|Q-Q'|<=epsilon) <=34.6139896874 epsilon`.                   (6.4)

This is not used to infer the one-copy `L^infinity` bound; that direction would be invalid in general. The one-copy density bound was proved first by Theorem 2.1, and the partner theorem is then applied at an actual inequality as requested.

## 7. What remains

The unrestricted conjecture remains open. This run pays one previously singular endpoint of the newest local-overlap frontier:

- overlap-one anchored third-volume `J_sep>=1/2304`;
- exact rank-one light crossing `N`;
- arbitrary small/zero hub diagonal;
- arbitrary internal quadratic curvature in both light banks;
- arbitrary aligned components of both hub stars;
- arbitrary cap-one fragmented/unbounded original laws;
- all signs.

The first B03 debt after this run is the **near-rank-one / genuine-rank-two collar** of the same anchored packet. A source-valid next step is to interpolate (2.4) with the r41/r42 conjugate-pair receivers or to prove a triangle estimate stable under an additional small second crossing singular direction without treating that small matrix coefficient as a small random perturbation. Equation (5.6) gives a quantitative matrix tail to target, but by itself it cannot be discarded because the input laws have no moment or support bound.

Full-target continuity remains open. Continuity is proved only for the branch of Theorem 4.4 through `phi_Q in L^1`.
