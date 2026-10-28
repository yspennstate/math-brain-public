SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T04:57:46Z.
attacking: the two-sided hub-edge entanglement with arbitrary same-bank nonlinear phase; seek an averaged-frequency L^r budget that keeps both hub-slope couplings and the hyperbolic pair.

# account03/B01 r44 — two-sided hub-entangled residuals at no extra Fourier cost

Run: `20260924T045746Z-account03-B01-qform-auto11-r44`.

Status: **NEW SUPPORTING THEOREMS / PREVIOUS B01 TWO-SIDED-NONLINEAR-PHASE INTERFACE CLOSED / FULL QFORM OPEN**.

The unrestricted theorem is not claimed. All variables below are original-coordinate groups; no rotation of the independent input coordinates is used. No moment, compact-support, Gaussian, log-concavity, connected-support, or regularity assumption is added. The argument uses averaged frequency norms and never invokes a law-uniform pointwise quadratic-phase decay estimate.

## 1. Preserved obstruction: pointwise quadratic decay is still false

For any prescribed `s != 0` and any `0<eta<pi/2`,

`E_{s,eta}={x: dist(s x^2,2 pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite union `F` of intervals in `E_{s,eta}` with total length one and put `f=1_F`. Then `0<=f<=1`, `int f=1`, and

`Re E exp(i s X^2) >= cos(eta)`.

Thus no estimate `|E exp(i s X^2)| <= C |s|^{-eps}` with `eps>0` can hold uniformly over all cap-one laws. The theorem below replaces pointwise decay by a vector-valued `L^{r'}` frequency budget.

## 2. Base two-hub packet

Let `H=(H1,H2)` be two independent real random variables with densities at most one. Let `Y` be a source-disjoint product bank, and let

`S(Y)=B Y+d in R^2`,

where `B` has row rank two. Let `R(Y)` be arbitrary measurable. Write

`P=||p_S||_2`.

For every `t`, push the complex measure

`exp(i t R(Y)) dP_Y`

through `S`. Its density `a_t(s)` exists and satisfies `|a_t(s)|<=p_S(s)` almost everywhere, hence `||a_t||_2<=P`. Therefore

`A_t(h):=E_Y exp(i t(2 h^T S(Y)+R(Y)))`

is the Fourier transform of `a_t` at `2 t h`, and Plancherel gives

`int_{R^2} |A_t(h)|^2 dh <= pi^2 P^2 / t^2`  for `t != 0`.  (2.1)

Since the joint density of `H` is at most one,

`(E_H |A_t(H)|^2)^(1/2) <= pi P / |t|`.  (2.2)

This is the critical two-hub `|t|^{-1}` estimate. By itself it is not integrable.

## 3. Main theorem: a residual may depend arbitrarily on both hubs

### Theorem `QFORM-TWO-HUB-HUB-CONDITIONAL-LR-v1`

Let `W` be source-disjoint from `(H,Y)`. For almost every `h`, assume the scalar random variable

`Z_h = Z(h,W)`

has a density `q_h` and, for some `1<r<=2`,

`ess sup_h ||q_h||_r <= M_r`.  (3.1)

No independence between `Z_h` and `H` is required after inserting `h`; the dependence on `h` may be arbitrary. Define

`Q = H^T C H + 2 H^T S(Y) + R(Y) + Z(H,W)`,  (3.2)

with arbitrary symmetric `2x2` matrix `C`.

Put

`r'=r/(r-1)`, `alpha=(r-1)/r`, `theta=r/(2r-1)=1/(1+alpha)`.

Then `phi_Q in L^1(R)`. Hence `Q` has a continuous `C_0` density and

`||p_Q||_inf <= K_r (P M_r)^theta`,  (3.3)

where

`K_r = ((1+alpha)/(pi alpha)) * [ (alpha pi/2) * (2/(r-1))^(1/r) * (2 pi)^alpha ]^theta`.  (3.4)

At `r=2`,

`||p_Q||_inf <= 3 * 2^(-2/3) * (P M_2)^(2/3)`.  (3.5)

This is exactly the constant of the source-disjoint independent-residual compiler; arbitrary dependence of the residual on the two hubs costs no extra constant.

### Proof

For fixed `h`, define

`psi_h(t)=E_W exp(i t Z(h,W))`.

The characteristic function factorizes only conditionally on the hubs:

`phi_Q(t)=E_H[ exp(i t H^T C H) A_t(H) psi_H(t) ]`.  (3.6)

Cauchy-Schwarz in the *original two-hub law* and (2.2) give

`|phi_Q(t)| <= pi P |t|^(-1) G(t)`,  (3.7)

where

`G(t)=(E_H |psi_H(t)|^2)^(1/2)`.  (3.8)

The essential step is to average the residual in frequency before taking any supremum over `h`. Since `r'>=2`, Minkowski with exponent `r'/2>=1` gives

`||G||_{r'}^2
 = || E_H |psi_H|^2 ||_{r'/2}
 <= E_H || |psi_H|^2 ||_{r'/2}
 = E_H ||psi_H||_{r'}^2`.  (3.9)

Hausdorff-Young in the convention `hat f(t)=int exp(i t x) f(x) dx` gives, uniformly in `h`,

`||psi_h||_{r'} <= (2 pi)^alpha ||q_h||_r <= (2 pi)^alpha M_r`.  (3.10)

Therefore

`||G||_{r'} <= (2 pi)^alpha M_r`.  (3.11)

For `T>0`, use `|phi_Q|<=1` on `|t|<=T` and Holder with exponents `r,r'` on the tail:

`int_R |phi_Q(t)| dt
 <= 2T + pi P int_{|t|>T} |t|^(-1) G(t) dt`

`<= 2T + pi P (2/(r-1))^(1/r) T^(-alpha) (2 pi)^alpha M_r`.  (3.12)

Set

`K = pi P (2/(r-1))^(1/r) (2 pi)^alpha M_r`.

The right side is `2T+K T^(-alpha)`. It is minimized at

`T_*=(alpha K/2)^theta`.

At the minimizer, `K T_*^(-alpha)=2T_*/alpha`, so Fourier inversion yields exactly (3.3)-(3.4). Since `phi_Q in L^1`, the density is continuous and vanishes at infinity. QED.

## 4. Designated partner result applied at the actual equation

The designated completed account04/B01 result is:

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

It proves for independent cap-one `U,V`, every `c!=0`, and all real affine coefficients,

`Z=2cUV+beta U+gamma V+delta`,

that for every `1<r<=2`,

`||p_Z||_r <= 2^alpha |c|^(-alpha)`, `alpha=(r-1)/r`.  (4.1)

Now let the affine coefficients be arbitrary measurable functions of the two hubs:

`Z_h = 2cUV + beta(h) U + gamma(h) V + delta(h)`.  (4.2)

For every fixed `h`, (4.1) applies with the *same* constant. Thus (3.1) holds with

`M_r=2^alpha |c|^(-alpha)`.  (4.3)

This is the partner theorem applied to the actual conditional density entering (3.9)-(3.12), not merely cited as background.

In the literal quadratic-form specialization

`beta(h)=2 a^T h+beta_0`,
`gamma(h)=2 b^T h+gamma_0`,

both smoothing variables may shift both hubs through arbitrary vectors `a,b in R^2`. No extra factor depending on `a` or `b` appears.

## 5. Two-sided hub-entangled hyperbolic corollary

### Corollary `QFORM-TWO-HUB-TWO-SIDED-ENTANGLED-NONLINEAR-PHASE-v1`

Let `H=(H1,H2)`, `Y`, `U`, `V` be mutually source-disjoint original-coordinate groups, with `H1,H2,U,V` cap-one and `Y` a cap-one product bank. Let `B` have row rank two, `c!=0`, and let `R(Y)` be arbitrary measurable. For

`Q = H^T C H
   + 2 H^T(BY+d+aU+bV)
   + R(Y)
   + 2cUV + beta U + gamma V + delta`,  (5.1)

set `D=det(BB^T)>0`. Then, for every `1<r<=2`,

`||p_Q||_inf <= C_r D^(-r/[4(2r-1)]) |c|^(-(r-1)/(2r-1))`,  (5.2)

with the same `C_r` as in the completed account04/B01 source-disjoint theorem:

`C_r = ((1+alpha)/(pi alpha))
       * [ (alpha pi/2) (2/(r-1))^(1/r) (2 pi)^alpha 2^(alpha+1/2) ]^theta`.  (5.3)

The only additional input is the completed two-dimensional product-projection estimate

`P <= sqrt(2) D^(-1/4)`.  (5.4)

At `r=2`, all constants cancel exactly:

`boxed: ||p_Q||_inf <= 3 D^(-1/6) |c|^(-1/3)`.  (5.5)

Thus **two-sided direct hub coupling and an arbitrary nonlinear same-bank phase cost exactly zero additional constant or scale exponent** relative to the formerly independent hyperbolic residual theorem.

This closes the previous B01 interface `QFORM-TWO-HUB-TWO-SIDED-ENTANGLED-NONLINEAR-PHASE-v1` in the precise chamber (5.1).

## 6. Complementary theorem: the residual may instead depend arbitrarily on the slope bank

There is a second, dual-looking extension that is useful for routing dense matrices.

### Theorem `QFORM-TWO-HUB-BANK-CONDITIONAL-LR-v1`

Keep the base packet of Section 2. Let `W` be source-disjoint from `(H,Y)`, and suppose that conditional on `Y=y`, the scalar residual `Z(y,W)` has density `q_y` with

`ess sup_y ||q_y||_r <= M_r`.  (6.1)

Then the same conclusion (3.3)-(3.4) holds:

`||p_Q||_inf <= K_r (P M_r)^theta`,  (6.2)

and the density is continuous `C_0`.

### Proof

Let `psi_y(t)=E_W exp(i t Z(y,W))`. Push the complex measure

`exp(i t R(y)) psi_y(t) dP_Y(y)`

through `S`. Its density is

`a_t(s)=p_S(s) E[exp(i t R(Y)) psi_Y(t) | S=s]`.  (6.3)

Jensen gives

`||a_t||_2^2
 <= int p_S(s)^2 E[|psi_Y(t)|^2 | S=s] ds
 = E[p_S(S(Y)) |psi_Y(t)|^2]`.  (6.4)

Let `G(t)=||a_t||_2`. Since `E[p_S(S(Y))]=int p_S^2=P^2`, Minkowski again yields

`||G||_{r'} <= P (2 pi)^alpha M_r`.  (6.5)

The hub Plancherel step now gives `|phi_Q(t)|<=pi |t|^(-1)G(t)`, and the tail optimization is identical to Section 3. QED.

Consequently the hyperbolic pair may have arbitrary `Y`-dependent affine coefficients while retaining the same bound, provided it does **not simultaneously** depend on the hubs.

## 7. Exact remaining analytic obstruction after this run

Sections 3 and 6 now pay both one-sided dependence patterns at the same sharp compiler constant:

- residual coefficients depending arbitrarily on the two hubs `H`, with arbitrary nonlinear `R(Y)`;
- residual coefficients depending arbitrarily on the slope bank `Y`.

The first still-unpaid mixed interface is when the same hyperbolic pair has affine coefficients depending simultaneously on both sides, e.g.

`2cUV + [2a^T H + ell^T Y + beta] U
       + [2b^T H + m^T Y + gamma] V`.  (7.1)

Then the hyperbolic multiplier depends on both `h` and `y`; it can no longer be placed outside the `Y -> S` Fourier transform (Section 3), and the complex projected density itself becomes `h`-dependent (blocking Section 6's Plancherel step). A generic conditional-density supremum is not permitted by the live corrections.

This precise next interface is named

`QFORM-TWO-HUB-HYPERBOLIC-PAIR-BOTH-SIDES-ENTANGLED-v1`.

A promising structural interpretation is the physical cross block between banks `(H1,H2,V)` and `(Y,U)`,

`M = [[B,a],[m^T,c]]`  (schematically),

whose rank-three/transversality branch should be payable by an existing grouped cross-volume theorem. The near-rank-two branch should be tested for an algebraic reduction to one of Sections 3 or 6. That reduction is not proved here.

## 8. Scale cancellation is preserved

If

`BB^T=k^2 I_2`, so `D=k^4`, and `c=k^(-q)` with fixed `q>=2`, choose

`r=q/(q-1)`.

Then

`-r/(2r-1) + q(r-1)/(2r-1)=0`,

so every power of `k` cancels in (5.2). The constants are exactly the same as in account04/B01's source-disjoint theorem:

- `q=2`: `C_2=3`;
- `q=3`: `C_{3/2}=3.8271703676919717...`;
- `q=4`: `C_{4/3}=4.832955112329408...`.

Thus the direct two-sided hub entanglement does not shrink the strict-N3 scale range previously obtained by the partner.

## 9. Target-valid deterministic stress example

Take variables ordered as `(H1,H2,Y1,Y2,U,V)` and

`Q = 2H1Y1 + 2H2Y2 + Y1^2 + 2H1U + 2H2V + 2UV`.

The symmetric matrix is

`A = [[0,0,1,0,1,0],
      [0,0,0,1,0,1],
      [1,0,1,0,0,0],
      [0,1,0,0,0,0],
      [1,0,0,0,0,1],
      [0,1,0,0,1,0]]`.

Its characteristic polynomial is

`x^6 - x^5 - 5x^4 + 4x^3 + 6x^2 - 3x - 1`,

and its eigenvalues are approximately

`-1.77091205, -1.13612949, -0.24107336, 0.70920977, 1.49702150, 1.94188363`.

Hence four eigenvalues have modulus at least one. Here `B=I_2`, `D=1`, `c=1`, `R(Y)=Y1^2` is genuinely nonlinear, and **both** `U` and `V` shift the hubs. The new corollary gives

`boxed: ||p_Q||_inf <= 3`

for every admissible product input law, and the density is continuous.

This is an exact theorem application, not a histogram or numerical proof.

## 10. Signed Fejer / averaged-frequency consequence

Because the theorem proves `phi_Q in L^1`, Fourier inversion gives the continuous bounded density directly. In particular every normalized triangular Fejer average satisfies

`sup_{T>0,y} D_T law(Q)(y) <= ||p_Q||_inf`,

so (5.2) and (5.5) are also valid averaged-frequency bounds. This is stronger than the requested signed-Fejer replacement and does not assert absolute `L^1` control for scalar quadratic factors individually.

## 11. Scope and continuity

- Full unrestricted QFORM: **OPEN**.
- New hub-conditional and bank-conditional compilers: complete supporting arguments in the stated source-disjoint groupings; independent review still requested.
- Two-sided hub-entangled hyperbolic corollary: complete within (5.1); independent review still requested.
- Continuity: **proved** for the new scoped theorems because their characteristic functions are integrable.
- Global continuity: OPEN.
- Repository transport is not native learned-memory ingestion: execution status remains `WITHOUT_VERIFIED_BRAIN`.

## 12. Source pins consumed

- Live corrections: pointwise quadratic decay false; arbitrary-joint coarea false; conditional projection moments/caps false; no post-rotation independence; no moment-based small-error disposal.
- Designated partner actually applied: `yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425:proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

No task/schedule, notification, permission, public-release, cross-account-authentication, or paid-model/API state is changed by this run.
