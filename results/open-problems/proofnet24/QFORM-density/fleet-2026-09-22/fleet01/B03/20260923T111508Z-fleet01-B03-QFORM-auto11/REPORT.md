SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T11:15:08Z.
attacking: the cancelled near-coloop collision geometry by aggregating one left physical row and a right two-volume basis before any reciprocal pivot payment.

# fleet01/B03 auto11 — mixed-basis triple-Fresnel determinant-entropy receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. The theorem below is a product-coordinate analytic packet: it keeps all active variables in their original independent coordinates, never treats a sum and difference from one coordinate pair as independent, never assigns either member of such a pair a conditional density cap, and uses only integrated one-dimensional Fourier estimates. In the stated packet it yields a one-copy `L^1` Fourier bound, a continuous density, a linear one-copy small-ball bound, and the requested independent-copy weighted time integral.

## 1. Source inputs actually used


The one-dimensional integrated Fourier input is from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For every cap-one probability density `f`, every measurable complex `g` with `|g|<=f`, and every `p>=2`,

`int_R |g^(hat)(s)|^p ds <= 4 pi/sqrt(p)`.                         (1.1)

The same source supplies the damped Fresnel linearisation and the rank-one Brascamp--Lieb Gaussian variational formula used below.

The designated partner result actually applied is fleet02/B03 r12:

`yspennstate/math-open-problems@9f2a751322a0351e12a855be56db1e78ea4a6154`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T101024Z-fleet02-B03-QFORM-r12/REPORT.md`,

with its source-scope correction

`yspennstate/math-open-problems@af2202db60286d57da95dd3f2aee934ed153f3e7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T101024Z-fleet02-B03-QFORM-r12/SUPPLEMENT.md`.

Its current one-sided packet has

`Q=a^(-1)H^2+2 sigma U V`,                                          (1.2)

`H=aX_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                               (1.3)

with `||u||_2=||v||_2=1`,

`h_R=beta0 v+m q`, `q perp v`, `||q||=1`,
`m=rho y`, `rho^2=a^2+||k||^2`, `y^2>1/2`,                         (1.4)

and, with `gamma=rho^2/|a|` and `s=s_3(A)`,

`gamma |sigma| >= s^2`, `gamma sigma^2 >= s^3`.                    (1.5)

For a selected heavy right row `r`, writing

`delta_h=|h_r|/rho`, `eta_r=v_r^2+q_r^2`, `zeta=1-eta_r`,           (1.6)

the partner proves under `h_r!=0`, positive deletion Gram matrix and deletion-plane maximum leverage at most `3/4` that

`||p_Q||_infinity
 < C_partner s^(-1)[delta_h zeta]^(-2/7),`

`C_partner=7*2^(16/7)*3^(-4/7)=18.2190565794241...`.               (1.7)

Against the common envelope `128 sqrt(15)/s`, that branch is paid whenever

`delta_h zeta >= 9.5158151888273e-6`.                              (1.8)

The supplement is essential: `U` remains a genuine random marginal and is not frozen or conditionally recapped.

## 2. Product-coordinate mixed-basis packet

Let `L,R` be disjoint index sets. Let `X_L,X_R` have mutually independent coordinates, each with density at most one. Let `Omega` be independent of those active coordinates. Let

`U=u.X_L`, `V=v.X_R`, `||u||_2=1`,                                (2.1)

and

`H=h_L.X_L+h_R.X_R+xi(Omega)`.                                     (2.2)

Fix nonzero `a,sigma`. Allow arbitrary coordinatewise real phases on the active coordinates and an arbitrary outside phase depending on `Omega`; these only twist the one-dimensional densities by unit-modulus factors. Consider

`T=a^(-1)H^2+2 sigma U V + (coordinatewise active phases) + F(Omega).` (2.3)

For `j in R` put

`r_j=(h_j,v_j) in R^2`,
`D_ij=det(r_i,r_j)`,
`E2=sum_{i<j}D_ij^2=det(sum_{j in R} r_j r_j^T).`                   (2.4)

Assume `E2>0`.

For each mixed triple `B=(l,{i,j})`, `l in L`, `i<j in R`, define

`w_B=u_l^2 D_ij^2`, `p_B=w_B/E2`.                                  (2.5)

Because `sum_l u_l^2=1`, `p` is a probability law on mixed three-coordinate bases. Let `B,B'` be iid with law `p` and define

`delta_mix=P(B cap B'=emptyset)`.                                  (2.6)

### Theorem 2.1 — `QFORM-MIXED-BASIS-TRIPLE-FRESNEL-v1`

If `delta_mix>0`, then

`|phi_T(t)| <= min(1,K |t|^(-3/2)),`                               (2.7)

where

`K=8 pi^(3/2) sqrt(|a|)/(|sigma| sqrt(E2 delta_mix)).`             (2.8)

Consequently `T` has a continuous `C_0` density and

`boxed:
 ||p_T||_infinity
 <=12 [ |a|/(sigma^2 E2 delta_mix) ]^(1/3).
}`                                                                  (2.9)

In particular every interval `I` satisfies

`P(T in I)
 <=12 [ |a|/(sigma^2 E2 delta_mix) ]^(1/3) |I|.`                   (2.10)

The same packet has the dependence-safe independent-copy estimates

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2 dt
 <=(48/5)sqrt(pi)
   [ |a|/(sigma^2 E2 delta_mix) ]^(1/6),
}`                                                                  (2.11)

and

`boxed:
 P(|T-T'|<=eps)
 <=12 [ |a|/(sigma^2 E2 delta_mix) ]^(1/3) eps,
}`                                                                  (2.12)

for an independent copy `T'`.

### Proof

For every `l in L` introduce the row in `R^3`

`R_l=(h_l,u_l,0)`,                                                  (2.13)

and for every `j in R`

`R_j=(h_j,0,v_j)`.                                                  (2.14)

For a mixed triple `B=(l,{i,j})`,

`det(R_l,R_i,R_j)=u_l D_ij`,                                       (2.15)

hence `det(R_B)^2=w_B` and

`sum_B det(R_B)^2=E2`.                                              (2.16)

Condition the iid pair `(B,B')` on disjointness and call the resulting joint law `mu`; let `q` be either marginal. Put

`alpha_k=P_{B~q}(k in B)`.                                         (2.17)

The conditioned joint law is symmetric, and the two triples are disjoint. Therefore

`2 alpha_k=P(k in B)+P(k in B')<=1`,
`sum_k alpha_k=3`.                                                   (2.18)

Define

`Z_q=exp(H(q)+sum_B q_B log det(R_B)^2)`.                           (2.19)

Since `p_B=det(R_B)^2/E2`,

`D_KL(mu || p tensor p)=log(1/delta_mix)`.                          (2.20)

Data processing under `(B,B')->B` gives

`D_KL(q||p)<=log(1/delta_mix)`.                                    (2.21)

But

`D_KL(q||p)=log(E2/Z_q)`,                                          (2.22)

so

`boxed: Z_q>=E2 delta_mix.`                                        (2.23)

Now let `d_k>0`. Cauchy--Binet and weighted AM--GM give

`det(sum_k d_k R_k R_k^T)
 >=sum_B det(R_B)^2 prod_{k in B}d_k
 >=Z_q prod_k d_k^(alpha_k).`                                      (2.24)

The rank-one Brascamp--Lieb Gaussian variational formula therefore gives for the data `(R_k,alpha_k)` the constant

`C_BL<=Z_q^(-1/2) prod_k alpha_k^(-alpha_k/2).`                    (2.25)

Let `Psi_k` be any one-dimensional twisted characteristic functions supplied by the active product coordinates. For `alpha_k>0` set `F_k=|Psi_k|^(1/alpha_k)`. By (2.18), `1/alpha_k>=2`, so (1.1) yields

`int F_k <=4 pi sqrt(alpha_k).`                                    (2.26)

The powers of `alpha_k` cancel exactly between (2.25) and (2.26), while `sum alpha_k=3`. Coordinates with `alpha_k=0` are discarded using `|Psi_k|<=1`. Translation invariance of rank-one Brascamp--Lieb therefore gives, uniformly in all coordinatewise translations,

`boxed:
 int_R3 prod_k |Psi_k(R_k.z+c_k)| dz
 <=(4pi)^3 Z_q^(-1/2)
 <=64 pi^3 (E2 delta_mix)^(-1/2).
}`                                                                  (2.27)

It remains to put the three quadratic channels into exactly this three-dimensional integral. Use the algebraic identity

`2 sigma U V=(sigma/2)(U+V)^2-(sigma/2)(U-V)^2`.                  (2.28)

Apply the damped Fresnel representation to the three squares

`a^(-1)H^2`, `(sigma/2)(U+V)^2`, `-(sigma/2)(U-V)^2`,              (2.29)

and remove damping by dominated convergence before taking absolute values, exactly as in the cited Fresnel source. The product of the three Fresnel prefactors is

`sqrt(|a|)/(4 pi^(3/2)|sigma||t|^(3/2)).`                          (2.30)

If the two bilinear auxiliary variables are changed from `(x,y)` to

`r=x+y`, `q=x-y`,                                                   (2.31)

the Jacobian contributes another factor `1/2`. The left active coordinates then see the linear arguments `h_l s+u_l r`, while the right active coordinates see `h_j s+v_j q`; these are exactly the rows (2.13)-(2.14). Thus (2.27) gives

`|phi_T(t)|
 <= [sqrt(|a|)/(8 pi^(3/2)|sigma||t|^(3/2))]
    [64 pi^3/sqrt(E2 delta_mix)]
 =K |t|^(-3/2),`                                                    (2.32)

which proves (2.7)-(2.8).

With crossover `T0=K^(2/3)`, direct integration gives

`int_R min(1,K|t|^(-3/2)) dt=6K^(2/3)`,                           (2.33)

so Fourier inversion yields a continuous density and

`||p_T||_infinity <=(3/pi)K^(2/3)
 =12 [|a|/(sigma^2E2delta_mix)]^(1/3)`.                            (2.34)

Similarly

`int_R |phi_T(t)|^2 dt<=3K^(2/3)`,                                (2.35)

and

`int_R |t|^(-1/2)|phi_T(t)|^2 dt<=(24/5)K^(1/3)`,                 (2.36)

which is (2.11). Here

`|phi_T(t)|^2=E exp(it(T-T'))`                                     (2.37)

is kept as the characteristic function of the whole copy difference. No coordinate sum/difference decomposition is invoked. By Plancherel,

`||p_T||_2^2<=(3/(2pi))K^(2/3)
 =6[|a|/(sigma^2E2delta_mix)]^(1/3)`.                              (2.38)

Since the density of `T-T'` is `p_T*p_{-T}` and has supremum at most `||p_T||_2^2`, (2.12) follows. QED.

## 3. Application to the current one-sided target packet

In the partner packet (1.2)-(1.5), the right frame is

`h_R=beta0 v+m q`, `q perp v`,                                     (3.1)

so

`E2=det([h_R,v]^T[h_R,v])=m^2`.                                   (3.2)

Moreover

`sigma^2 E2/|a|
 =sigma^2 m^2/|a|
 =gamma sigma^2 y^2
 >s^3/2`                                                            (3.3)

by (1.4)-(1.5). Therefore Theorem 2.1 gives, whenever `delta_mix>0`,

`boxed:
 ||p_Q||_infinity
 <12*2^(1/3) s^(-1) delta_mix^(-1/3)
 =15.1190525987385... s^(-1) delta_mix^(-1/3).
}`                                                                  (3.4)

This density is continuous. The dependence-safe time integral becomes

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <(48/5)sqrt(pi)2^(1/6)
   s^(-1/2)delta_mix^(-1/6)
 =19.0993169282039...
   s^(-1/2)delta_mix^(-1/6).
}`                                                                  (3.5)

Against the existing common envelope

`C_env/s=128sqrt(15)/s=495.741868314549.../s`,                      (3.6)

the new branch is paid whenever

`boxed:
 delta_mix>=delta_mix,*
 :=(12*2^(1/3)/(128sqrt(15)))^3
 =2.83665772427301e-5.
}`                                                                  (3.7)

This is independent of the partner deletion-plane leverage condition.

## 4. Exact factorisation of the new structural collar

The mixed-basis law (2.5) factorises exactly:

`p_(l,{i,j})=u_l^2 [D_ij^2/E2].`                                  (4.1)

Let

`delta_L=P(l!=l')=1-sum_l u_l^4`,                                  (4.2)

and let `delta_R` be the probability that two iid right two-volume bases, sampled with probabilities `D_ij^2/E2`, are disjoint. Because the left and right banks are disjoint and the mixed law is a product,

`boxed: delta_mix=delta_L delta_R.`                                (4.3)

Hence a survivor of (3.7) must satisfy

`delta_L delta_R<2.83665772427301e-5`.                             (4.4)

Put

`eta=sqrt(delta_mix,*)=0.00532602828031640...`.                     (4.5)

Then at least one of the following holds:

1. `delta_L<eta`. In that case

   `max_l u_l^2 >= sum_l u_l^4=1-delta_L>0.994673971719684`,        (4.6)

   so the left projection is an extremely concentrated physical-row direction.

2. `delta_R<eta`. The completed weighted-two-edge stability theorem in fleet03/B03 r32 then forces the right two-volume law to be near-coloop or near-triangle: there is either a vertex of inclusion probability, or three vertices carrying edge mass, at least

   `1-eta-(3/2)^(1/3)eta^(1/3)
    =0.794765326604617...`.                                        (4.7)

The second structural statement is source-pinned to

`yspennstate/math-open-problems@ba06ed6272b1929f19f39deaf99691f77a096d22`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/.../REPORT.md`.

Thus the new Fourier route fails only when the product geometry itself is strongly concentrated, not because of a pointwise oscillatory-decay failure.

## 5. Required partner splice at an actual inequality

Now combine the new receiver with the designated fleet02/B03 r12 theorem, not just as a citation.

The common envelope `128sqrt(15)/s` is proved if **either**

`delta_mix>=2.83665772427301e-5`,                                  (5.1)

by (3.4), **or**, for a selected heavy right row satisfying the partner's nonzero-row, positive-deletion-Gram and deletion-leverage `<=3/4` hypotheses,

`delta_h(1-eta_r)>=9.5158151888273e-6`,                            (5.2)

by (1.7)-(1.8).

Therefore, inside the overlap of the partner's strict-collar hypotheses, any state still unpaid by this common envelope must satisfy the simultaneous degeneracy

`boxed:
 delta_mix<2.83665772427301e-5,
 delta_h(1-eta_r)<9.5158151888273e-6.
}`                                                                  (5.3)

Without the partner leverage hypothesis, the first inequality remains a valid necessary condition for escaping the new theorem. This is a genuine narrowing of the remaining packet: the new aggregate three-channel Fourier estimate is insensitive to the deletion-plane maximum leverage, while the partner theorem pays a complementary nonzero physical-row branch.

## 6. What this proves and what remains

This run does **not** prove full QFORM. It proves a continuous bounded density, a linear small-ball estimate, and a dependence-safe weighted collision-time integral for the stated one-sided product packet whenever the mixed disjoint-basis probability is positive, with a target-homogeneous constant depending only on `delta_mix`.

At the common fleet envelope, the only unhandled part of this packet has the quantitative concentrated structure (5.3), and by (4.3)-(4.7) additionally has either a nearly single-coordinate left projection or a near-coloop/near-triangle right two-volume law.

The first essential missing implication is now structural: pay those concentrated alternatives directly in original coordinates without declaring a small coefficient to be a small random perturbation. The natural next mechanisms are (i) use the dominant left coordinate as a true physical pivot while preserving the full right-bank aggregate, or (ii) use the right near-triangle to create a finite physical three-coordinate core while retaining the residual product-bank averaging. Full continuity remains OPEN outside the paid branches.

## 7. Integrity notes

Consumed live corrections include the refutation of law-uniform pointwise quadratic-phase decay, the false conditional cap for conjugate sum/difference variables, the false arbitrary-joint rank-three coarea lemma, and the failure of naive local-minor selection. None is used here.

No Gaussianity, moments, log-concavity, compact support, connected support, diagonal-basis independence, or conditional projection-density cap is assumed. No numerical histogram is used as proof.
