SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T10:10:24Z.
attacking: the strict near-coloop collar by extracting the selected heavy physical row before the decoupled Fresnel integral, then pairing its true L^p receiver with an L^q Brascamp-Lieb norm of the deletion plane.

# fleet02/B03 r12 — physical-row L^p / deletion-plane L^q splice

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / STRICT-COLLAR NARROWED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN and global continuity remains separate.  This report proves a one-copy L-infinity receiver for a nonzero heavy physical row whose deletion plane has a strict leverage margin.  It is complementary to the designated fleet03/B03 exact-cancellation L2 theorem.  No sum/difference coordinate is conditioned on or declared independent of its conjugate; no spectral rotation is used as a probabilistic change of coordinates; and no conditional projection-density supremum appears.

## 1. Exact source inputs actually used

### 1.1 Required newest Claude/e5 input

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

and `FOURIER_ROUTE_REPORT.md`.

I use its damped Fresnel linearisation and, at the displayed deletion-plane inequality (3.6), its proved twisted characteristic-function estimate

`integral |Psi(s)|^r ds <= 4 pi/sqrt(r),  r>=2`.                    (1.1)

This is an actual use of the required package, not a bibliography-only citation.

### 1.2 Designated partner fleet03/B03

Latest compatible designated-partner result read before this run:

`yspennstate/math-open-problems@f7c9ef92371b6602f9a432a16555c48c2ed45a51`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T090012Z-fleet03-B03-QFORM-r29/REPORT.md`.

Its theorem `QFORM-CANCELLED-ROW-RIGHTBANK-L2-v1` proves, at the exact selected-row angular cancellation `h_r=0`,

`integral |phi_Q(t)|^2 dt <54.27326850232713/s`,                    (1.2)

`integral |t|^(-1/2)|phi_Q(t)|^2 dt <19.64543821560657/sqrt(s)`,   (1.3)

and, by its valid collision transducer,

`P(|Q-Q'|<=eps)<17.27571791979806 s^(-1) eps`,                     (1.4)

where `s=s_3(A)`.  Section 5 below uses (1.2)-(1.4) as the exact-cancellation side of the new splice.  It is still an L2/collision endpoint there, not a one-copy L-infinity theorem.

### 1.3 Current one-sided geometry and exact-coloop boundary

The current strict-collar geometry is source-pinned through the fleet02/B03 augmented-BL report and the fleet01/B03 splice as read at

`yspennstate/math-open-problems@ba000d70d1d4f523a2396155a24d5088d5c94802`

paths

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T061506Z-fleet02-B03-QFORM-auto11/REPORT.md`

and

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T092010Z-fleet01-B03-QFORM-auto11/REPORT.md`.

The exact-coloop endpoint is already paid by

`yspennstate/math-open-problems@ba66d82dd8e99e4b651a0442ef3a1175a953bf90`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T053308Z-fleet03-B14-QFORM-r27/REPORT.md`.

For a unit original-product projection I use the standard sharp cap `sqrt(2)`, recorded with source in

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

## 2. The analytic packet

Let

- `X` be a real random variable with density at most one;
- `Y=(Y_1,...,Y_m)` have independent cap-one coordinates and be independent of `X`;
- `Omega` be independent of `(X,Y)`;
- `U=U(Omega)` have density bounded by `L`;
- `xi(Omega),F(Omega)` be arbitrary and allowed to depend on `U`;
- `A,d,alpha` be nonzero real constants;
- `b` be real and `h,g in R^m`.

Allow arbitrary coordinatewise unit-modulus phases on the active physical variables.  Define

`T=A(alpha X+h.Y+xi(Omega))^2
   +2d U(Omega)(bX+g.Y)+F(Omega).`                                  (2.1)

Put row vectors

`r_j=(h_j,g_j) in R^2`,
`G=sum_j r_j r_j^T`,                                                 (2.2)

and assume `G` is positive definite.  Let

`ell_j=r_j^T G^(-1)r_j`.                                             (2.3)

Thus `0<=ell_j<=1` and `sum ell_j=2`.

The new point is to isolate the physical row `X` into an honest two-dimensional `L^p` factor and spend only the remaining deletion plane with Brascamp-Lieb.  This is different from requiring the selected physical row itself to have BL leverage at most `1/2`.

## 3. Main theorem

### Theorem 3.1 — `QFORM-PHYSICALROW-LP-DELETIONPLANE-LQ-v1`

Let `1<q<2`, set

`p=q/(q-1)`,
`beta=1/2+1/q>1`,                                                    (3.1)

and assume

`max_j ell_j <= q/2`.                                                (3.2)

Then

`|phi_T(t)| <= min(1,K_q |t|^(-beta))`,                             (3.3)

with

`K_q=(4pi)^(-1/2) 2^(-1/q) (2pi)^(1/p)
      (16pi^2/q)^(1/q)
      L^(1/q)|A|^(-1/2)|d|^(-1/q)
      |alpha|^(-1/p) det(G)^(-1/(2q)).`                             (3.4)

Consequently `T` has a continuous bounded density and

`||p_T||_infinity
 <= [beta/(pi(beta-1))] K_q^(1/beta).`                              (3.5)

No conditional density of a sum/difference variable is used.

### Proof

Fix `t!=0`.  Apply the e5 damped Fresnel identity to the square in (2.1), remove the damping by dominated convergence as in that source, and only then take absolute values.  With `chi_t` the possibly twisted characteristic function of `X`, and `Psi_j,t` the corresponding twisted characteristic functions of the `Y_j`,

`|phi_T(t)|
 <=(4pi|tA|)^(-1/2)
   int ds int p_U(u)
   |chi_t(alpha s+2tdbu)|
   prod_j |Psi_j,t(h_j s+2tdg_j u)| du.`                            (3.6)

Set `T0=2|td|` and `eta=2td u`.  The last double integral, including the Jacobian, is

`T0^(-1) int_R2 F_t(s,eta) P_t(s,eta) ds deta`,                     (3.7)

where

`F_t=p_U(eta/(2td)) |chi_t(alpha s+b eta)|`,
`P_t=prod_j |Psi_j,t(h_j s+g_j eta)|`.                              (3.8)

First bound the genuine physical-row factor.  Since `|chi_t|<=1`, Plancherel and `f_X<=1` imply, for every `p>=2`,

`int |chi_t(r)|^p dr <= int |chi_t(r)|^2 dr <=2pi`.                 (3.9)

Also `int p_U^p <=L^(p-1)`.  Therefore

`||F_t||_p^p
 <= [2pi T0 L^(p-1)]/|alpha|.`                                    (3.10)

Now handle the deletion plane.  Normalize by `G^(-1/2)`.  The rows `G^(-1/2)r_j` form a tight frame in `R^2` with squared lengths `ell_j`.  Geometric rank-one Brascamp-Lieb applied to `|P_t|^q` gives

`||P_t||_q^q
 <=det(G)^(-1/2)
   prod_j [ell_j^(-1/2)
      int |Psi_j,t(s)|^(q/ell_j) ds]^ell_j.`                         (3.11)

By (3.2), `q/ell_j>=2`.  The required e5 estimate (1.1) therefore gives

`ell_j^(-1/2) int |Psi_j,t|^(q/ell_j)
 <=4pi/sqrt(q)`                                                     (3.12)

for every nonzero row.  Since `sum ell_j=2`,

`boxed:
 ||P_t||_q^q <=(16pi^2/q) det(G)^(-1/2).
}`                                                                   (3.13)

Holder in `(s,eta)`, followed by (3.10)-(3.13), yields (3.3)-(3.4).  Indeed the time power is

`|t|^(-1/2) T0^(-1+1/p)
 =const*|t|^(-1/2-1/q)=const*|t|^(-beta).`                           (3.14)

Because `beta>1`,

`int_R min(1,K|t|^(-beta))dt
 =2 beta/(beta-1) K^(1/beta).`                                     (3.15)

Fourier inversion proves (3.5) and continuity. `QED`

### Clean q=3/2 form

Take `q=3/2`, `p=3`.  The leverage hypothesis is simply

`max_j ell_j<=3/4`.                                                  (3.16)

Then `beta=7/6` and the constants simplify exactly to

`|phi_T(t)|
 <=min(1,
   [4 pi^(7/6)/3^(2/3)]
   L^(2/3)|A|^(-1/2)|d|^(-2/3)|alpha|^(-1/3)
   det(G)^(-1/3)|t|^(-7/6)).`                                      (3.17)

Hence

`boxed:
 ||p_T||_infinity
 <=7*2^(12/7)*3^(-4/7)
   L^(4/7)|A|^(-3/7)|d|^(-4/7)|alpha|^(-2/7)
   det(G)^(-2/7).
}`                                                                   (3.18)

This is a true one-copy linear-small-ball estimate, not merely an L2 collision certificate.

## 4. Application to the current one-sided heavy-row packet

The current source-valid packet is

`Q=a^(-1)H^2+2sigma U V`,                                           (4.1)

`H=aX_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                               (4.2)

with

`h_R=beta0 v+m q0`, `q0 perp v`, `||q0||=||v||=1`,
`m=rho y`, `rho^2=a^2+||k||^2`, `y^2>1/2`,                         (4.3)

and

`gamma=rho^2/|a|`,
`gamma|sigma|>=s^2`,
`gamma sigma^2>=s^3`,                                               (4.4)

where `s=s_3(A)`.

Choose the heavy physical right row `r` from the current collar and write

`alpha=h_r`, `eta_r=v_r^2+q0_r^2`,
`delta=|h_r|/rho`, `zeta=1-eta_r`.                                  (4.5)

Condition only on the original coordinates outside the right bank.  This makes the right-bank variables stay independent cap-one variables and makes `U`, the square centre and the outside scalar term arbitrary fixed functions of the outside state.  Isolate `X_r` as the physical row in Theorem 3.1 and take the deletion-bank rows

`r_j=(h_j,v_j),  j in R\{r}.`                                      (4.6)

The exact two-plane deletion identity from the current geometry is

`boxed: det G=m^2(1-eta_r)=m^2 zeta.`                              (4.7)

Let `ell_*` be the largest normalized leverage of this deletion plane.  If

`alpha!=0`, `G>0`, and `ell_*<=3/4`,                                (4.8)

then (3.18) applies with

`A=1/a`, `d=sigma`, `L<=sqrt(2)`.                                  (4.9)

After substituting `m=rho y`, `|h_r|=rho delta`, and `|a|=rho^2/gamma`, all powers of `rho` cancel.  The spectral inequalities (4.4) combine at the *exact exponents needed*:

`gamma^(3/7)|sigma|^(4/7)
 =(gamma|sigma|)^(2/7)(gamma sigma^2)^(1/7)
 >=s.`                                                              (4.10)

Therefore

`||p_Q||_infinity
 <=7*2^(12/7)*3^(-4/7)
   L^(4/7) s^(-1)
   delta^(-2/7)y^(-4/7)zeta^(-2/7).`                               (4.11)

Using `L<=sqrt(2)` and `y>1/sqrt(2)` gives the clean target-homogeneous form

`boxed:
 ||p_Q||_infinity
 < C_* s^(-1)[delta zeta]^(-2/7),
 C_*=7*2^(16/7)*3^(-4/7)
    =18.2190565794241... .
}`                                                                   (4.12)

Thus every interval `I` obeys

`P(Q in I)
 <18.21905658 s^(-1)[delta(1-eta_r)]^(-2/7)|I|`                     (4.13)

whenever (4.8) holds.  This is the requested linear small-ball scale on an actual still-live nonzero-row collar, with all original-coordinate dependence preserved.

### Same-envelope quantitative exit

The preceding fleet02/fleet01 splice already uses the common paid envelope

`128 sqrt(15)/s=495.7418683145.../s`.                               (4.14)

The new theorem costs no more than that envelope whenever

`delta(1-eta_r) >= delta_*`,                                        (4.15)

where

`delta_*=(C_*/(128sqrt(15)))^(7/2)
        =9.5158151888273e-6.`                                       (4.16)

Consequently, subject to deletion-plane leverage `ell_*<=3/4`, the previously surviving strict collar is narrowed further to the simultaneous product degeneracy

`delta(1-eta_r)<9.516e-6`.                                         (4.17)

This is not a perturbative deletion of a small coefficient: every term in (4.1) remains present, and the estimate is uniform over arbitrary fragmented/unbounded input laws.

## 5. Exact-cancellation partner splice and the real remaining gap

At `h_r=0`, Theorem 3.1 is intentionally not invoked: its physical-row `L^p` factor uses `alpha!=0`.  Instead apply the designated partner theorem (1.2)-(1.4) to this exact same packet.  It gives the target-scale whole-copy estimates

`integral |phi_Q|^2 <54.27327/s`,
`integral |t|^(-1/2)|phi_Q|^2 <19.64544/sqrt(s)`,                   (5.1)

and

`P(|Q-Q'|<=eps)<17.27572 s^(-1)eps`.                               (5.2)

This is a direct application of the partner result to the endpoint of the new classification.  It also makes the remaining debt precise: collision control is already target-scale at exact angular cancellation, but no abstract implication from that critical collision energy to `||p_Q||_infinity` is valid.

At the other boundary, if `G` is singular then deleting `r` leaves the right-plane coefficient vectors collinear; the exact-coloop theorem cited in Section 1.3 already gives a one-copy universal density bound.  Therefore the genuinely unpaid interpolation is now confined to a **second-order collar** in which at least one of the following occurs:

1. `h_r=0` with a non-coloop deletion plane: partner target-scale L2/collision is available but one-copy L-infinity is still unpaid;
2. `0<delta(1-eta_r)<9.516e-6`: both the selected square coefficient and deletion area are simultaneously tiny;
3. the deletion plane has a nested heavy leverage row, `ell_*>3/4`.

The third item is a structural statement: after the first heavy row is removed, more than three quarters of the normalized *remaining two-dimensional frequency plane* is again carried by one original coordinate.  A useful next receiver should treat these two physical rows jointly or splice the exact-coloop square-linear kernel with this nested row; it should not condition on the dependent projected pair.

## 6. Why this changes the proof map

The previous augmented-BL receiver spends the grouped-hub density inside a two-dimensional BL integral and needs a strict augmented leverage margin.  The designated partner exact-cancellation receiver instead spends the cancelled physical row by Plancherel and yields a critical `1/|t|` envelope.  The present theorem inserts a third mechanism between them:

- keep the selected physical row plus the true `U` density together as an `L^p(R^2)` factor;
- spend the *deletion plane* as an `L^q(R^2)` product by e5 Brascamp-Lieb;
- choose `p=3,q=3/2` to obtain the integrable exponent `7/6`.

The leverage threshold is thereby moved from the selected heavy row to the deletion plane.  This is exactly why a row that is heavy in the full right plane can now be used rather than rejected.

The full QFORM theorem remains OPEN.  No counterexample to the owner target is produced.  Continuity is proved only in the scope of Theorem 3.1; the global continuity question remains separate.
