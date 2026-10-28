SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T12:15:28Z.
attacking: the almost-single-coordinate left survivor by isolating one left physical coordinate and one right physical row before the deletion-plane Fourier/Brascamp--Lieb integral.

# account01/B03 r25 — two-physical-row / deletion-plane Fourier receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / LEFT-CONCENTRATED COLLAR NARROWED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN and the unrestricted continuity conclusion remains OPEN. This report proves a new product-coordinate Fourier theorem, applies it to the current one-sided QFORM packet, gives a dependence-safe whole-copy collision integral, and strictly shrinks one of the remaining near-coloop collars. It uses neither post-rotation independence nor a conditional density cap for a sum/difference variable.

## 1. Source state and exact inputs actually used

Fresh prepublication control was resolved at

`yspennstate/math-research-brain@763726107461c2d17900102bcd9b35026da01eb3`,


### 1.1 Required newest Claude/e5 input

I use the integrated one-coordinate Fourier estimate from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For every cap-one probability density `f`, every measurable complex `g` with `|g|<=f`, and every `r>=2`,

`integral_R |g^(hat)(s)|^r ds <= 4 pi/sqrt(r)`.                    (1.1)

I use (1.1) in the deletion-plane Brascamp--Lieb integral below. The same source supplies the damped Fresnel linearisation used before taking absolute values.

### 1.2 Designated partner account02/B03 actually applied

The completed partner result is

`yspennstate/math-open-problems@9f2a751322a0351e12a855be56db1e78ea4a6154`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T101024Z-account02-B03-QFORM-r12/REPORT.md`,

with its source-scope supplement at

`yspennstate/math-open-problems@af2202db60286d57da95dd3f2aee934ed153f3e7`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T101024Z-account02-B03-QFORM-r12/SUPPLEMENT.md`.

Its current one-sided packet is

`Q=a^(-1)H^2+2 sigma U V`,                                          (1.2)

`H=aX_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`, `||u||_2=||v||_2=1`,                         (1.3)

with

`h_R=beta_0 v+m q`, `q perp v`, `||q||=1`,
`m=rho y`, `rho^2=a^2+||k||^2`, `y^2>1/2`,                         (1.4)

and, writing `gamma=rho^2/|a|` and `s=s_3(A)`,

`gamma |sigma| >= s^2`,
`gamma sigma^2 >= s^3`.                                             (1.5)

For a chosen physical right row `r`, let

`delta=|h_r|/rho`, `eta_r=v_r^2+q_r^2`, `zeta=1-eta_r`.             (1.6)

If `h_r!=0`, the deletion-plane Gram matrix is positive definite, and its maximum normalized leverage is at most `3/4`, the partner theorem proves

`||p_Q||_infinity
 < C_partner s^(-1)[delta zeta]^(-2/7)`,                            (1.7)

where

`C_partner=7*2^(16/7)*3^(-4/7)=18.2190565794241...`.               (1.8)

Against the common already-paid envelope `128sqrt(15)/s`, this exits whenever

`delta zeta >= 9.5158151888273e-6`.                                (1.9)

I use (1.2)-(1.6) below at actual equations, and compare the new exit with (1.7)-(1.9). The supplement is respected: I never freeze the projected scalar `U` and then assign it a conditional density cap.

### 1.3 Previous account01/B03 structural input

The immediately preceding B03 result is source-pinned at

`yspennstate/math-open-problems@3e0f2eab95c45d446044d6a8de29464294fc8a0a`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T111508Z-account01-B03-QFORM-auto11/REPORT.md`.

Its mixed-basis theorem implies that failure of its common-envelope exit forces either a right two-volume disjointness degeneration or an almost-single-coordinate left projection. In the latter branch one may choose `ell in L` with

`u_ell^2 > 0.994673971719684`.                                      (1.10)

The new receiver is designed precisely for this left-concentrated branch.

## 2. New analytic theorem

Let `X,Y_0,Y_1,...,Y_m` be mutually independent real random variables with probability densities bounded by one. Let `Omega` be independent of these active variables. Conditional on `Omega`, allow arbitrary real one-coordinate phases on all active variables and an arbitrary outside phase; they only twist the one-dimensional densities by factors of modulus one.

Fix real `A,d` with `A d !=0`, real `alpha,h_0,g_0`, and vectors `h=(h_j)`, `g=(g_j)`. Consider

`T=A(alpha X+h_0Y_0+sum_j h_jY_j+xi(Omega))^2
   +2d X(g_0Y_0+sum_j g_jY_j)
   +(allowed one-coordinate phases)+F(Omega).`                       (2.1)

For the deletion bank put

`r_j=(h_j,g_j) in R^2`,
`G=sum_j r_j r_j^T`,                                                 (2.2)

assume `G>0`, and define normalized deletion leverages

`ell_j=r_j^T G^(-1)r_j`.                                            (2.3)

Thus `0<=ell_j<=1` and `sum_j ell_j=2`.

### Theorem 2.1 — `QFORM-TWO-PHYSICALROW-DELETION-LQ-v1`

Let `1<q<2`, `p=q/(q-1)`, and

`beta=1/2+1/q=(q+2)/(2q)>1`.                                       (2.4)

Assume

`h_0!=0`,
`max_j ell_j <= q/2`.                                                (2.5)

Then

`|phi_T(t)| <= min(1,K_q |t|^(-beta))`,                             (2.6)

where

`K_q=(4pi)^(-1/2) 2^(-1/q) (2pi)^(1/p)
      (16pi^2/q)^(1/q)
      |A|^(-1/2)|d|^(-1/q)|h_0|^(-1/p)
      det(G)^(-1/(2q)).`                                             (2.7)

Consequently `T` has a continuous `C_0` density and

`||p_T||_infinity
 <= D_q |A|^(-q/(q+2)) |d|^(-2/(q+2))
       |h_0|^(-2(q-1)/(q+2)) det(G)^(-1/(q+2)),`                    (2.8)

with

`D_q=(q+2)/(2-q) * 2^(4/(q+2)) * q^(-2/(q+2)).`                    (2.9)

For an independent copy `T'`, retaining the whole difference law,

`|phi_T(t)|^2=phi_(T-T')(t)`,                                       (2.10)

and

`integral_R |t|^(-1/2)|phi_T(t)|^2 dt
 <= J_beta K_q^(1/(2beta)),`                                        (2.11)

where

`J_beta=4+2/(2beta-1/2).`                                           (2.12)

No member of a dependent sum/difference coordinate pair is isolated or recapped conditionally in (2.10)-(2.11).

### Endpoint `q=1`

There is a stronger endpoint not present in the partner theorem. If

`max_j ell_j<=1/2`,                                                  (2.13)

then no nonzero hypothesis on `h_0` is needed. With `beta=3/2`,

`K_1=4 pi^(3/2)|A|^(-1/2)|d|^(-1)det(G)^(-1/2)`,                   (2.14)

and (2.6), (2.8), (2.10)-(2.12) remain valid with

`D_1=3*2^(4/3)=7.55952629936924...`.                               (2.15)

In particular the endpoint can give a one-copy `L^infinity` density even when the isolated right square coefficient `h_0` is **exactly zero**, provided the deletion plane is diffuse enough.

## 3. Proof of Theorem 2.1

Fix the outside state `Omega=omega`; all estimates below are uniform in it. Apply the damped Fresnel identity to the square in (2.1), remove the damping by dominated convergence as in the e5 source, and only then take absolute values. Integrate the physical left variable `X=x` last among the active one-dimensional expectations. Put `T_0=2|td|`. After the change of variables

`eta=2td x`,                                                        (3.1)

we obtain

`|phi_T(t)|
 <=(4pi|tA|)^(-1/2) T_0^(-1)
   integral_R2 F_t(s,eta) P_t(s,eta) ds deta`,                      (3.2)

where

`F_t(s,eta)
 =f_X(eta/(2td)) |chi_0(h_0s+g_0eta)|`,                             (3.3)

and

`P_t(s,eta)=prod_j |Psi_j(h_js+g_jeta)|`.                           (3.4)

Here `chi_0` and `Psi_j` are the characteristic functions of the corresponding cap-one densities after multiplication by all `omega`-dependent unit-modulus one-coordinate phases. The Fresnel factor `exp(i alpha s x)` also has modulus one. This is the key point: the coefficient `alpha` of the selected left physical coordinate in the square is **not paid at all**.

### 3.1 The honest two-physical-coordinate `L^p` factor

For `p>=2`, `|chi_0|<=1` and Plancherel give

`integral |chi_0(r)|^p dr
 <= integral |chi_0(r)|^2 dr
 <=2pi`.                                                            (3.5)

Also, because `0<=f_X<=1` and `integral f_X=1`,

`integral f_X(x)^p dx<=1`.                                          (3.6)

If `h_0!=0`, Fubini and the substitution `r=h_0s+g_0eta` yield

`||F_t||_p^p
 <=(2pi T_0)/|h_0|.`                                                (3.7)

This uses the genuine original-coordinate densities of `X` and `Y_0`; no projected or conditional density enters.

At `q=1`, `p=infinity`, and the only needed fact is instead

`||F_t||_infinity<=1`,                                               (3.8)

which remains true even for `h_0=0`.

### 3.2 Deletion-plane Brascamp--Lieb

Normalize by `G^(-1/2)`. The vectors `G^(-1/2)r_j` form a tight frame in `R^2` with squared lengths `ell_j`. Geometric rank-one Brascamp--Lieb applied to `|P_t|^q` gives

`||P_t||_q^q
 <=det(G)^(-1/2)
   prod_j [ell_j^(-1/2)
      integral |Psi_j(r)|^(q/ell_j) dr]^ell_j.`                    (3.9)

Zero rows are omitted. Under `ell_j<=q/2`, every exponent `q/ell_j` is at least two. The e5 estimate (1.1) gives

`ell_j^(-1/2) integral |Psi_j|^(q/ell_j)
 <=4pi/sqrt(q).`                                                     (3.10)

Since `sum ell_j=2`,

`boxed:
 ||P_t||_q^q <=(16pi^2/q) det(G)^(-1/2).
}`                                                                   (3.11)

At `q=1`, the same calculation is valid exactly under `ell_j<=1/2` and gives

`||P_t||_1<=16pi^2 det(G)^(-1/2).`                                  (3.12)

### 3.3 Time decay, density and collision energy

For `1<q<2`, Holder in `(s,eta)` with `(p,q)`, followed by (3.7) and (3.11), turns (3.2) into

`|phi_T(t)|<=K_q |t|^(-1/2-1/q)`,                                  (3.13)

which is (2.6)-(2.7). At `q=1`, combine (3.8) and (3.12) directly to get (2.14) and the `|t|^(-3/2)` envelope.

For every `beta>1`,

`integral_R min(1,K|t|^(-beta)) dt
 =2beta/(beta-1) K^(1/beta).`                                      (3.14)

Fourier inversion therefore gives a continuous `C_0` density and

`||p_T||_infinity
 <=beta/[pi(beta-1)] K_q^(1/beta).`                                 (3.15)

Using

`K_q`'s scalar constant
`=2^(2/q) pi^beta q^(-1/q)`                                        (3.16)

reduces (3.15) exactly to (2.8)-(2.9).

For the assignment's whole-copy collision integral, split at `t_0=K_q^(1/beta)`:

`integral_R |t|^(-1/2) min(1,K_q^2|t|^(-2beta)) dt
 =[4+2/(2beta-1/2)]K_q^(1/(2beta)).`                               (3.17)

Together with the exact identity (2.10), this proves (2.11). Importantly, (3.17) is not being used as an abstract `L^infinity` criterion; the linear small-ball estimate comes from the stronger `L^1_t` bound (3.14).

This proves Theorem 2.1.

## 4. Clean `q=3/2` form

Take `q=3/2`, `p=3`, `beta=7/6`. If `h_0!=0` and the deletion-plane maximum leverage is at most `3/4`, then

`K_(3/2)=4 pi^(7/6) 3^(-2/3)
          |A|^(-1/2)|d|^(-2/3)|h_0|^(-1/3)
          det(G)^(-1/3)`,                                           (4.1)

and

`boxed:
 ||p_T||_infinity
 <=7*2^(12/7)*3^(-4/7)
   |A|^(-3/7)|d|^(-4/7)|h_0|^(-2/7)det(G)^(-2/7).
}`                                                                   (4.2)

Also

`boxed:
 integral_R |t|^(-1/2)|phi_T(t)|^2dt
 <=(56/11) K_(3/2)^(3/7).
}`                                                                   (4.3)

This is the dependence-safe decoupled time integral requested by the B03 assignment.

## 5. Application to the current one-sided QFORM packet

Choose an original left-bank coordinate `ell` with `u_ell!=0`. Keep `X=X_ell` active and put all other left-bank coordinates, together with `X_i` and `X_K`, into the outside state `Omega`. This is legitimate original-coordinate conditioning: `X_ell` and the entire right bank remain mutually independent cap-one variables.

Write

`U=u_ell X_ell+U_0(Omega).`                                         (5.1)

Then

`2sigma U_0(Omega)V
 =sum_(j in R) [2sigma U_0(Omega)v_j X_j]`                          (5.2)

is merely an `Omega`-dependent sum of one-coordinate linear phases on the right bank. It is therefore covered by the twists allowed in Theorem 2.1. The square centre may depend arbitrarily on `Omega`.

Choose a right physical row `r` and set

`Y_0=X_r`,
`A=1/a`,
`d=sigma u_ell`,
`alpha=h_ell`,
`h_0=h_r`,
`g_0=v_r`,                                                          (5.3)

with deletion rows

`(h_j,v_j), j in R\{r}.`                                            (5.4)

The partner geometry gives the exact determinant identity

`det G=m^2 zeta`, `zeta=1-eta_r`.                                  (5.5)

Let `ell_*` be the maximum normalized leverage in this deletion plane.

For `1<q<2`, if `h_r!=0` and `ell_*<=q/2`, substitute (1.4)-(1.6) and (5.3)-(5.5) into (2.8). All powers of `rho` cancel. The spectral factors combine exactly because

`gamma^(q/(q+2)) |sigma|^(2/(q+2))
 =(gamma|sigma|)^[2(q-1)/(q+2)]
  (gamma sigma^2)^[(2-q)/(q+2)]
 >=s.`                                                              (5.6)

Both exponents on the right are nonnegative for `1<=q<=2`. Since `y>1/sqrt(2)`, we obtain the target-homogeneous bound

`boxed:
 ||p_Q||_infinity
 < C(q) s^(-1)
   [u_ell^2 delta^(2(q-1)) zeta]^(-1/(q+2)),
}`                                                                   (5.7)

where

`C(q)=(q+2)/(2-q) *2^(5/(q+2))*q^(-2/(q+2)).`                      (5.8)

Thus every strict deletion leverage `ell_*<1` has a finite one-copy continuous-density receiver after choosing any `q` with `max(1,2ell_*)<q<2`, provided `h_r!=0`. The bound is not uniform as the geometric collar degenerates; this is a supporting theorem, not full QFORM.

### 5.1 The `q=3/2` target branch and exact partner improvement

If `ell_*<=3/4`, (5.7) gives

`boxed:
 ||p_Q||_infinity
 <14.9457362652052 s^(-1)
  [u_ell^2 delta zeta]^(-2/7).
}`                                                                   (5.9)

The scalar constant is exactly

`28*3^(-4/7)=14.9457362652052...`.                                  (5.10)

Against the same common envelope `128sqrt(15)/s`, the new branch is paid whenever

`boxed:
 u_ell^2 delta zeta
 >=4.75790759441365e-6.
}`                                                                   (5.11)

This is an actual quantitative splice with the designated partner theorem. Its threshold (1.9) is exactly twice (5.11):

`9.5158151888273e-6
 =2*(4.75790759441365e-6).`                                         (5.12)

Equivalently, for a fixed selected left coefficient, the new receiver pays whenever

`delta zeta
 >=4.75790759441365e-6/u_ell^2.`                                   (5.13)

It strictly improves the partner branch whenever `u_ell^2>1/2`, precisely the regime for which this mechanism was designed.

Now apply the previous account01/B03 left-concentration alternative (1.10). In that branch, simultaneous failure of the new common-envelope exit forces

`boxed:
 delta zeta <4.78338403304930e-6.
}`                                                                   (5.14)

So, under the same deletion leverage hypothesis `ell_*<=3/4`, the already tiny partner collar is cut essentially in half.

### 5.2 The `q=1` exact-cancellation endpoint

If the deletion-plane maximum leverage is at most `1/2`, the endpoint theorem applies **without any condition on `h_r`**, including `h_r=0`. The target bound is

`boxed:
 ||p_Q||_infinity
 <9.52440631180920 s^(-1)
   [u_ell^2 zeta]^(-1/3).
}`                                                                   (5.15)

Against `128sqrt(15)/s`, this is paid whenever

`u_ell^2 zeta >=7.09164431068253e-6.`                               (5.16)

Therefore part of the partner report's exact-angular-cancellation state, which previously had only a target-scale `L^2`/collision certificate, now has a genuine one-copy continuous bounded density. The remaining exact-cancellation debt is confined to deletion planes with maximum leverage `>1/2` (or the already-paid exact-coloop endpoint), together with the broader full-matrix structural debt.

## 6. Whole-copy integrated estimate in the target variables

At `q=3/2`, (4.3) and the same substitutions give another exact use of the source spectral identities:

`gamma^(3/14)|sigma|^(2/7)
 =(gamma|sigma|)^(1/7)(gamma sigma^2)^(1/14)
 >=s^(1/2).`                                                        (6.1)

Hence

`boxed:
 integral_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <13.1849933584855 s^(-1/2)
   [u_ell^2 delta zeta]^(-1/7),
}`                                                                   (6.2)

whenever `h_r!=0` and `ell_*<=3/4`.

At the diffuse endpoint `q=1`,

`boxed:
 integral_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <15.1591378918525 s^(-1/2)
   [u_ell^2 zeta]^(-1/6),
}`                                                                   (6.3)

with no nonzero condition on `h_r`.

Equations (6.2)-(6.3) are statements about the characteristic function of the **whole independent-copy difference** `Q-Q'`; they do not condition `X-X'` on `X+X'`, or vice versa. The actual linear small-ball scaling for `Q` is supplied by (5.7), not inferred from the negative-weight collision integral alone.

## 7. What this does and does not close

This run changes the live one-sided proof map in three ways.

1. In the almost-single-coordinate left branch produced by the preceding B03 mixed-basis theorem, the same `q=3/2` deletion-plane condition used by account02/B03 now has a common-envelope threshold exactly one half as large after the left physical coordinate is kept active.
2. The endpoint `q=1` pays a genuine one-copy `L^infinity` density even at exact selected-row angular cancellation whenever the deletion plane has leverage at most `1/2`.
3. The general `1<q<2` theorem gives a continuous-density receiver for every **strict** deletion leverage below one, with an explicit geometry-dependent constant.

It does **not** solve the unrestricted conjecture. In the current packet the remaining hard states include nested deletion leverage approaching one, simultaneous very small deletion area and square coefficient, and the right near-coloop/near-triangle alternative from the preceding mixed-basis classification. Outside this one-sided packet one still needs an exhaustive product-preserving structural compiler from the bare three-large-eigenvalue hypothesis into one of the paid analytic geometries.

The full QFORM claim therefore remains `OPEN`. The theorem proved here gives a continuous density in its stated scope; **global continuity remains OPEN**. Independent end-to-end review of this new theorem has not yet occurred.

## 8. Deterministic algebra check

The run-local `check_constants.py` was executed. Its output is saved in `CHECK_OUTPUT.txt` and terminates with

`QFORM_B03_TWO_PHYSICAL_ROW_PASS`.

It verifies the simplification of `K_q`, the density constant `C(q)`, the `q=3/2` target constant, the exact factor-two partner-threshold improvement, the left-concentrated numerical collar, the `q=1` endpoint constant, and the target collision constant in (6.2).
