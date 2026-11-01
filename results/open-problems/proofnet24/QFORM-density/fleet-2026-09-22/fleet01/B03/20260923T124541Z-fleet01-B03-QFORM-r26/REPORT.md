SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T12:45:41Z.
attacking: the two-isolated-right-row Fresnel receiver — remove the nested deletion-leverage obstruction without a q<2 loss, while retaining the whole-copy decoupled time integral.

# fleet01/B03 r26 — two-right-row / q=2 deletion receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / NESTED-LEVERAGE COLLAR NARROWED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. The unrestricted continuity conclusion also remains **OPEN**. This report proves a new product-coordinate Fourier theorem that removes the `q<2` deletion-leverage loss from the preceding B03 one-row receiver by isolating two genuine right physical coordinates before the deletion-plane Brascamp--Lieb step. It then applies the theorem to the current fleet02/B03 one-sided packet and derives a whole-independent-copy weighted time integral. No sum/difference conjugate variables are declared independent or conditionally recapped.

## 1. Fresh control, corrections and exact dependencies

Fresh prepublication control was resolved at

`yspennstate/math-research-brain@091792e12e2fea4f0deeed6d8d6111e5617b0e55`,


The one-dimensional integrated Fourier input actually used is the completed e5/Claude package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For every cap-one probability density, including an arbitrary unit-modulus coordinatewise phase twist, its Fourier transform `Psi` obeys

`integral_R |Psi(s)|^r ds <= 4 pi/sqrt(r),  r>=2`.                  (1.1)

The designated partner theorem actually applied is fleet02/B03 r12:

`yspennstate/math-open-problems@9f2a751322a0351e12a855be56db1e78ea4a6154`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T101024Z-fleet02-B03-QFORM-r12/REPORT.md`.

Its current one-sided packet and notation are

`Q=a^(-1) H^2 + 2 sigma U V`,                                      (1.2)

`H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`, `||u||_2=||v||_2=1`,                         (1.3)

`h_R=beta_0 v+m q`, `q perp v`, `||q||_2=1`,
`m=rho y`, `rho^2=a^2+||k||^2`, `y^2>1/2`,                         (1.4)

and, with `gamma=rho^2/|a|`, `s=s_3(A)`,

`gamma |sigma| >= s^2`,
`gamma sigma^2 >= s^3`.                                             (1.5)

For a selected right row `r`, its theorem defines

`delta=|h_r|/rho`, `eta_r=v_r^2+q_r^2`, `zeta=1-eta_r`,             (1.6)

and proves a continuous-density receiver when the once-deleted two-plane has normalized leverage at most `3/4`:

`||p_Q||_infinity <18.2190565794241 s^(-1)[delta zeta]^(-2/7)`.     (1.7)

Against the common already-paid envelope `128 sqrt(15)/s`, this exits when

`delta zeta >=9.5158151888273e-6`.                                 (1.8)

The immediately preceding fleet01/B03 r25 theorem kept one left physical coordinate active and improved this threshold by a factor two when that left coefficient is large. It is source-pinned at

`yspennstate/math-open-problems@1db54d1fef9431919f1b8ddc39776b6a9be23679`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T121528Z-fleet01-B03-QFORM-r25/REPORT.md`.

In its left-concentrated branch one may choose `ell in L` with

`u_ell^2 > 0.994673971719684`.                                      (1.9)

The new theorem is designed for the remaining nested-deletion regime in which a right row still has leverage close to one after the first right row is removed.

## 2. General analytic theorem

Let `X,Y_1,...,Y_N` be mutually independent real variables with cap-one probability densities. Let `Omega` be independent of these active variables. Conditional on `Omega`, allow arbitrary affine one-coordinate phases on the active variables and an arbitrary outside phase; multiplication of a one-dimensional density by such a phase does not change its modulus.

Fix `A,d` with `A d !=0`, a real `alpha`, and rows

`r_k=(h_k,g_k) in R^2, 1<=k<=N`.                                   (2.1)

Consider

`T=A(alpha X+sum_k h_k Y_k+xi(Omega))^2`
`  +2d X sum_k g_k Y_k`
`  +(allowed one-coordinate phase terms)+F(Omega).`                 (2.2)

Choose distinct right physical indices `i,j`. Put

`Delta_ij=|det(r_i,r_j)|`,                                          (2.3)

and let the twice-deleted Gram matrix be

`G_ij=sum_(k notin {i,j}) r_k r_k^T`.                               (2.4)

### Theorem 2.1 — `QFORM-TWO-RIGHTROW-Q2-DELETION-v1`

Assume

`Delta_ij>0`, `G_ij>0`.                                             (2.5)

Then

`boxed:
 |phi_T(t)| <= min{1,
   sqrt(2) pi^(3/2) |A|^(-1/2)|d|^(-1)
   Delta_ij^(-1/2) det(G_ij)^(-1/4) |t|^(-3/2)}.
`                                                                     (2.6)

In particular `T` has a continuous `C_0` density and

`boxed:
 ||p_T||_infinity
 <=3*2^(1/3) |A|^(-1/3)|d|^(-2/3)
   Delta_ij^(-1/3) det(G_ij)^(-1/6).
`                                                                     (2.7)

Thus every interval `I` satisfies the genuine linear small-ball estimate

`P(T in I) <= RHS(2.7) |I|`.                                        (2.8)

Moreover, for an independent copy `T'`, with the whole copy difference retained,

`|phi_T(t)|^2=phi_(T-T')(t)`,                                       (2.9)

and if

`K=sqrt(2) pi^(3/2)|A|^(-1/2)|d|^(-1)
   Delta_ij^(-1/2)det(G_ij)^(-1/4)`,                                (2.10)

then

`boxed:
 integral_R |t|^(-1/2)|phi_T(t)|^2 dt <=(24/5) K^(1/3).
`                                                                     (2.11)

No normalized-leverage upper bound is assumed in Theorem 2.1. This is the key distinction from the preceding one-isolated-right-row `1<q<2` receiver.

## 3. Proof

Fix the outside state `Omega=omega`. Apply the damped Fresnel identity to the square in (2.2), remove the damping by dominated convergence as in the source package, and only afterward take absolute values. Integrate the original left physical coordinate `X=x` last. Set

`eta=2td x`.                                                        (3.1)

Exactly as in the preceding B03 argument,

`|phi_T(t)|`
` <=(4pi|tA|)^(-1/2)(2|td|)^(-1)`
`   integral_R2 f_X(eta/(2td)) prod_k |Psi_k(h_k s+g_k eta)| ds deta`, (3.2)

where the `Psi_k` are Fourier transforms of the cap-one densities after the allowed unit-modulus twists. Since `f_X<=1`, discard it. Write `z=(s,eta)` and split the integrand as

`F_ij(z)=|Psi_i(r_i.z) Psi_j(r_j.z)|`,                              (3.3)

`P_ij(z)=prod_(k notin {i,j}) |Psi_k(r_k.z)|`.                      (3.4)

### 3.1 The two isolated physical rows

The map `z -> (r_i.z,r_j.z)` has Jacobian `Delta_ij`. By Plancherel and the cap-one probability hypothesis,

`||Psi_k||_2^2=2pi ||f_k||_2^2 <=2pi`.                              (3.5)

Therefore

`||F_ij||_2^2`
` =Delta_ij^(-1)||Psi_i||_2^2||Psi_j||_2^2`
` <=4pi^2 Delta_ij^(-1)`,                                          (3.6)

so

`||F_ij||_2 <=2pi Delta_ij^(-1/2)`.                                (3.7)

### 3.2 The twice-deleted plane at the endpoint q=2

Normalize the residual rows by `G_ij^(-1/2)`. Their squared normalized leverages are

`ell_k=r_k^T G_ij^(-1)r_k`,                                        (3.8)

with `0<=ell_k<=1` and `sum ell_k=2`. Geometric rank-one Brascamp--Lieb applied to `P_ij^2` gives

`||P_ij||_2^2`
` <=det(G_ij)^(-1/2)
`   prod_k [ell_k^(-1/2) integral |Psi_k(s)|^(2/ell_k) ds]^ell_k`.  (3.9)

Every nonzero exponent `2/ell_k` is automatically at least two; **no leverage margin is required**. Applying (1.1),

`ell_k^(-1/2) integral |Psi_k|^(2/ell_k)`
` <=ell_k^(-1/2) * 4pi/sqrt(2/ell_k)`
` =2sqrt(2)pi`.                                                     (3.10)

Since the leverage sum is two,

`||P_ij||_2^2 <=8pi^2 det(G_ij)^(-1/2)`,                            (3.11)

and hence

`||P_ij||_2 <=2sqrt(2)pi det(G_ij)^(-1/4)`.                         (3.12)

Cauchy--Schwarz in the entire `(s,eta)` plane yields

`integral F_ij P_ij`
` <=4sqrt(2) pi^2 Delta_ij^(-1/2)det(G_ij)^(-1/4)`.                 (3.13)

Substitution in (3.2) proves (2.6): the time power is exactly

`|t|^(-1/2)|t|^(-1)=|t|^(-3/2)`.                                   (3.14)

This endpoint is the mechanism change: the preceding one-row proof could not set `q=2`, because its decay exponent `1/2+1/q` would become the nonintegrable value one. Isolating **two** right rows contributes enough genuine `L^2` structure that the residual deletion plane may be spent at `q=2` while the total time exponent remains `3/2`.

For any `K>0`,

`integral_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.                        (3.15)

Fourier inversion gives (2.7) and a continuous `C_0` density. Finally, splitting the whole-copy weighted integral at `t_0=K^(2/3)`,

`integral_R |t|^(-1/2) min(1,K^2|t|^(-3))dt`
` =4K^(1/3)+(4/5)K^(1/3)`
` =(24/5)K^(1/3)`,                                                  (3.16)

which proves (2.11). The negative-weight collision integral is **not** used as an abstract `L^infinity` criterion; the one-copy linear small-ball conclusion comes from the stronger integrable envelope (2.6).

## 4. Exact two-volume identities in the fleet02/B03 packet

Return to (1.2)-(1.5). For the right bank define

`r_k=(h_k,v_k)=(beta_0 v_k+m q_k,v_k)`.                             (4.1)

For `i<j` put

`w_ij=(q_i v_j-q_j v_i)^2`.                                        (4.2)

Because `v,q` are orthonormal,

`sum_(i<j) w_ij=||q wedge v||^2=1`.                                (4.3)

The physical two-row determinant is

`Delta_ij=|det(r_i,r_j)|=m sqrt(w_ij)`.                             (4.4)

Define its disjoint two-volume remainder

`delta_ij=sum_(k<l, {k,l} cap {i,j}=empty) w_kl`.                   (4.5)

Cauchy--Binet gives the exact twice-deleted determinant

`boxed: det G_ij=m^2 delta_ij.`                                     (4.6)

Thus Theorem 2.1 can be read directly in the right Pluecker two-volume law, with no local leverage restriction.

There is also a useful exact relation to the partner's once-deleted leverage. Fix its selected row `r`. The once-deleted Gram `G_r=sum_(k!=r)r_k r_k^T` satisfies

`det G_r=m^2 zeta`, `zeta=1-eta_r`.                                (4.7)

For a second row `j!=r`, let

`ell_j=r_j^T G_r^(-1)r_j`.                                         (4.8)

The matrix determinant lemma gives

`det(G_r-r_j r_j^T)=det G_r(1-ell_j)`.                              (4.9)

But the left side is exactly `det G_rj`. Consequently

`boxed: delta_rj=zeta(1-ell_j).`                                   (4.10)

So when the partner one-row theorem fails because a deletion row has leverage near one, the present theorem pays the same geometry unless either the selected pair area `w_rj`, the first deletion area `zeta`, or the second deletion factor `1-ell_j` is correspondingly tiny.

## 5. Actual target-homogeneous application

Use the preceding fleet01/B03 left-concentrated branch. Choose an original left coordinate `ell` and condition on all other left coordinates, `X_i`, and `X_K`; the active variables are the genuine physical coordinate `X=X_ell` and the full right original-coordinate bank. Then

`U=u_ell X+U_0(Omega)`.                                             (5.1)

The term `2sigma U_0 V` is only an outside-dependent sum of one-coordinate linear phases on the right bank and is therefore harmless in the Fourier estimate. Apply Theorem 2.1 with

`A=1/a`, `d=sigma u_ell`,                                          (5.2)

and the right rows (4.1). For every pair `i,j` with `w_ij delta_ij>0`, equations (2.7), (4.4), (4.6) give

`||p_Q||_infinity`
` <=3*2^(1/3)
`   [|a|/(sigma^2 u_ell^2 m^2)]^(1/3)
`   (w_ij delta_ij)^(-1/6).`                                       (5.3)

Now `m=rho y`, `gamma=rho^2/|a|`, `y^2>1/2`, and `gamma sigma^2>=s^3`; hence

`|a|/(sigma^2 m^2)=1/(gamma sigma^2 y^2)<2/s^3`.                   (5.4)

Therefore

`boxed:
 ||p_Q||_infinity
 <3*2^(2/3) s^(-1)
  [u_ell^4 w_ij delta_ij]^(-1/6).
}`                                                                   (5.5)

The scalar constant is

`3*2^(2/3)=4.762203155904598...`.                                   (5.6)

This density is continuous in the stated branch. Against the common envelope

`128 sqrt(15)/s=495.741868314549.../s`,                             (5.7)

the new receiver is already paid when

`boxed:
 u_ell^4 w_ij delta_ij >= 7.85803422331810e-13.
}`                                                                   (5.8)

In the preceding left-concentrated branch, (1.9) implies

`u_ell^4 >0.989376310016611`.                                       (5.9)

So failure of the common-envelope exit for a given pair forces the extremely narrow condition

`boxed:
 w_ij delta_ij <7.94241194554797e-13.
}`                                                                   (5.10)

### 5.1 Direct splice with fleet02/B03's nested-leverage obstruction

Take the partner-selected right row `r` and any second row `j` in its deletion plane. Combining (4.10) and (5.5),

`boxed:
 ||p_Q||_infinity
 <4.762203155904598 s^(-1)
 [u_ell^4 w_rj zeta(1-ell_j)]^(-1/6).
}`                                                                   (5.11)

This is the required actual use of the completed fleet02/B03 geometry. In particular, the partner theorem's difficult branch `ell_j>3/4` is **not** a failure mode for the new analytic estimate: no upper leverage hypothesis remains. Subject only to positive twice-deleted area, simultaneous failure of the common envelope now forces

`u_ell^4 w_rj zeta(1-ell_j)<7.85803422331810e-13`.                 (5.12)

Thus a surviving nested state must be almost a **second coloop**, have an exceptionally small selected pair area, have an exceptionally small first deletion area, or some combination of all three. Exact rank drop (`delta_rj=0`) is outside Theorem 2.1 and remains to be routed through the existing exact-coloop/grouped-bank branches; it is not silently treated by perturbation.

This is stronger than merely taking `q` closer to two in the preceding theorem: that route loses `L^1_t` integrability at `q=2`, while the two-isolated-row theorem stays at the fixed integrable decay `|t|^(-3/2)`.

## 6. Whole-copy decoupled time integral in target variables

From (2.11), (4.4)-(4.6), and the same spectral substitution,

`K^(1/3)`
` <2^(1/3) sqrt(pi) s^(-1/2)
   [u_ell^4 w_ij delta_ij]^(-1/12).`                                (6.1)

Therefore

`boxed:
 integral_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <10.719129200270824 s^(-1/2)
   [u_ell^4 w_ij delta_ij]^(-1/12).
}`                                                                   (6.2)

Here `|phi_Q(t)|^2=phi_(Q-Q')(t)` is used for the **whole independent copy**. The proof never conditions `X-X'` on `X+X'`, never assumes those conjugate variables are independent, and never gives one of them the original marginal density cap.

## 7. Deterministic checks

The run's exact/numerical checks verify:

- `3*2^(2/3)=4.762203155904598...`;
- the common-envelope threshold in (5.8) is `7.858034223318097867e-13`;
- the left-concentrated floor is `u_ell^4>0.989376310016611` and gives (5.10);
- the collision scalar in (6.2) is `10.719129200270824...`;
- for fixed-seed random orthonormal pairs `(v,q)`, the Cauchy--Binet identity `det G_ij=m^2 delta_ij` and determinant-lemma identity `det G_rj=m^2 zeta(1-ell_j)` agree to floating-point error (`max absolute error 5.684e-14` in the saved test sample).

The saved checker output terminates with `QFORM_B03_TWO_RIGHTROW_Q2_PASS`.

## 8. Exact status and next unpaid implication

This run proves a new supporting theorem and a strict target-level narrowing; it does **not** prove the unrestricted conjecture. The remaining structural debt is now concentrated further. In the current left-concentrated one-sided packet, after the partner and preceding B03 exits, a twice-deleted survivor must have vanishingly small `w_ij delta_ij` for every usable right pair, or exact rank drop. The next useful analytic/structural step is to aggregate the right pair law **before reciprocal pair selection**, or to exploit the exact/near-coloop core without treating a small matrix coefficient as a small random perturbation. Arbitrary fragmented unbounded supports prohibit that perturbative shortcut.

Branch status: **continuous bounded density proved** under Theorem 2.1's hypotheses.  
Full target essential boundedness: **OPEN**.  
Full target continuity: **OPEN**.  
Two independent end-to-end full-proof reviews: not applicable because no full candidate proof is claimed.
