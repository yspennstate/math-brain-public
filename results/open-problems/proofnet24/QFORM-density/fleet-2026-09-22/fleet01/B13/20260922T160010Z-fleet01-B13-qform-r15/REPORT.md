# fleet01/B13 — full-planar star forcing from cross Pluecker edge laws

**Run:** `20260922T160010Z-fleet01-B13-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full owner conjecture remains **OPEN / NOT PROVED**. Everything proved below concerns the exact-rank-three nested-heavy obstruction. Arbitrary additional spectral directions remain a separate debt.

## 1. Exact sources used

Fresh control was read from `yspennstate/math-research-brain`; the owner programme remained `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`. The live corrections used here exclude law-uniform pointwise quadratic oscillatory decay, post-rotation independence, single-cross-minor closure, bounded-diameter/fixed-fragment localization, and conditional-cap substitutes for independence.

The assigned partner result actually consumed is:

`fleet02/B13`, `yspennstate/math-open-problems@93bed74b07afe996a4aa08eaeb88f35060653134`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T152225Z-fleet02-B13-productset-7f3c9a/REPORT.md`.

It supplies the exact residual Pluecker pair laws, their cross-disjoint lower bound, and the normalized alignment identity recalled in Section 2.

I also use the already completed edge-distribution star/triangle theorem from

`fleet03/B07`, `yspennstate/math-open-problems@0b3ca7e927cad2a7c7805a7f2ba6b88b12d000fd`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T143620Z-fleet03-B07-QFORM-r12/REPORT.md`.

For any probability law `w` on unordered pairs with ordered disjoint mass `rho=P(E cap F=empty)`, it proves that, with

`kappa(rho)=1-rho-rho^(1/3)`,                                        (1.1)

either one vertex has incident mass at least `kappa(rho)`, or one triangle has internal edge mass at least `kappa(rho)`.

Finally, the exact bang-bang reduction of the assigned partner is source-pinned at

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`:
for every measurable `0<=K<=1`, the supremum over independent densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over product indicators `1_{E_i}`, `|E_i|=1`. Thus every density statement below has the corresponding product-set slab interpretation, with no interval-extremality assumption.

## 2. Partner pair laws

Use exactly the nested-heavy notation of fleet02/B13. Let

`A=R Lambda R^T`, `R^T R=I_3`,

and choose physical rows

`r_i=sqrt(c)e1`,
`r_j=rho0 e1+sqrt(h)e2`,

with `c>1/2`, `h>1/2`. For residual physical coordinates write

`r_k=a_k e1+b_k e2+z_k e3`.

Set

`B=1-h`,
`s=h+rho0^2`,
`beta=rho0^2+h(1-c)`,
`alpha=cB`,
`Delta=(1-c)(1-h)-rho0^2`,

and

`u_k=(sqrt(h)a_k-rho0 b_k)/sqrt(s)`,
`U=sum_k u_k^2=beta/s`,
`d_*=max_k z_k^2`.

The coefficient vectors `b,u,z` satisfy `b perp z`, `u perp z`, `sum z_k^2=1`. When `B,beta>0`, normalize

`x_k=b_k/sqrt(B)`,
`y_k=u_k/sqrt(U)`.

Then `x,y,z` are unit vectors and `x perp z`, `y perp z`.

The assigned partner defines residual unordered-pair weights

`p_kl=c(b_k z_l-z_k b_l)^2`,
`q_kl=s(u_k z_l-z_k u_l)^2`,

with total masses `alpha` and `beta`. Hence the normalized laws

`mu_kl:=p_kl/alpha=(x_k z_l-z_k x_l)^2`,                      (2.1)
`nu_kl:=q_kl/beta =(y_k z_l-z_k y_l)^2`                       (2.2)

are probability distributions on residual unordered pairs.

Let

`chi=sum_{e cap f=empty} mu_e nu_f`.                            (2.3)

The partner's physical disjoint-exterior estimate gives

`chi <= D0/(2 alpha beta)`,                                    (2.4)

where `D0` is the ordered disjoint rank-three Pluecker mass. Its exact alignment identity gives

`|<x,y>|^2=1-theta`,
`theta:=h Delta/(B beta)`,                                     (2.5)

and after choosing the sign of `y`,

`||x-y||_2^2=2(1-sqrt(1-theta)) <=2 theta`.                    (2.6)

## 3. New transfer: cross-disjoint smallness implies self-disjoint smallness

Let

`a_e=(x wedge z)_e`, `b_e=(y wedge z)_e`.

Because `x,z` and `y,z` are orthonormal pairs,

`sum_e a_e^2=sum_e b_e^2=1`,

and `mu_e=a_e^2`, `nu_e=b_e^2`. Moreover, since `x-y perp z`,

`||a-b||_2=||(x-y) wedge z||_2=||x-y||_2`.                     (3.1)

Therefore

`||mu-nu||_1
 <= ||a-b||_2 ||a+b||_2
 <=2||x-y||_2
 <=2 sqrt(2 theta)`.                                          (3.2)

Let

`rho_mu=sum_{e cap f=empty} mu_e mu_f`.                        (3.3)

Replacing the second `mu` by `nu` costs at most the total-variation `L1` distance, hence

`rho_mu <= chi+||mu-nu||_1`.                                  (3.4)

Combining (2.4), (3.2), and (3.4),

`boxed(rho_mu <= r:=D0/(2 alpha beta)+2 sqrt(2 theta)).`        (3.5)

This is the first new inequality of the run. It converts the assigned partner's **cross** pair-incidence information into the **self** disjointness parameter needed by the completed star/triangle theorem.

## 4. A Pluecker triangle cannot carry almost all mass when the transverse direction is diffuse

For each residual physical coordinate define the two-dimensional row

`v_k=(x_k,z_k) in R^2`.

Since `x,z` are orthonormal,

`sum_k v_k v_k^T=I_2`.                                        (4.1)

For any three residual vertices `T={a,b,c}`, Cauchy--Binet gives the exact internal-triangle mass

`tau_T:=mu_ab+mu_ac+mu_bc
      =det( sum_{k in T} v_k v_k^T ).`                         (4.2)

Write `S_T=sum_{k in T}v_kv_k^T`. Because `0<=S_T<=I_2`, its eigenvalues lie in `[0,1]`, and

`det S_T <= (tr S_T/2)^2`.                                    (4.3)

Also

`tr S_T=sum_{k in T}(x_k^2+z_k^2)
         <=1+3d_*`,                                           (4.4)

since `sum x_k^2=1` and each `z_k^2<=d_*`. Therefore every triangle obeys

`boxed(tau_T <= (1+3d_*)^2/4).`                               (4.5)

This is a genuinely Pluecker constraint; an arbitrary edge law need not satisfy it. In particular, when `d_*->0`, no triangle can carry more than `1/4+o(1)` of the normalized `p`-mass.

## 5. Main theorem: full-planar star forcing

Define

`kappa(t)=1-t-t^(1/3)` for `t>=0` where the right side is useful.  (5.1)

### Theorem 5.1 — `QFORM-NESTED-HEAVY-FULL-PLANAR-STAR-v1`

In the setup of Section 2, suppose `alpha beta>0` and set `r` by (3.5). If

`kappa(r) > (1+3d_*)^2/4`,                                     (5.2)

then there exists one residual physical coordinate `k` such that

`boxed(x_k^2 >= kappa(r)-d_*).`                               (5.3)

Equivalently,

`boxed(b_k^2/B >= kappa(r)-d_*).`                             (5.4)

Moreover

`boxed(y_k^2 >= ( sqrt((kappa(r)-d_*)_+) - sqrt(2theta) )_+^2 ).`  (5.5)

Hence

`sum_{l!=k} b_l^2
 <= B[1-kappa(r)+d_*]`,                                       (5.6)

and

`sum_{l!=k} u_l^2
 <= U{1-[sqrt((kappa(r)-d_*)_+)-sqrt(2theta)]_+^2}.`           (5.7)

#### Proof

By (3.5), the self-disjoint mass of `mu` satisfies `rho_mu<=r`. Apply the completed fleet03/B07 star/triangle theorem to `mu`. Since `kappa` is decreasing, either

(a) some vertex `k` has incident `mu`-mass at least `kappa(r)`, or

(b) some triangle has internal `mu`-mass at least `kappa(r)`.

Alternative (b) contradicts (4.5) under (5.2). Thus (a) holds. The exact incidence identity for the decomposable edge law is

`sum_{l!=k} mu_kl=x_k^2+z_k^2`.                               (5.8)

Therefore

`x_k^2+z_k^2>=kappa(r)`.

Since `z_k^2<=d_*`, (5.3)-(5.4) follow.

For (5.5), choose the sign of `y` so that (2.6) holds. Then

`|y_k| >= |x_k|-|x_k-y_k|
       >= sqrt((kappa(r)-d_*)_+) - ||x-y||_2`
`       >= sqrt((kappa(r)-d_*)_+) - sqrt(2theta)`.

Squaring the positive part yields (5.5). Equations (5.6)-(5.7) follow from `sum x_l^2=sum y_l^2=1`. QED.

This improves the assigned partner's previous `1/2-o(1)` planar concentration to `1-o(1)` once the genuine decomposable-edge geometry and final-direction diffuseness are used together.

## 6. Full planar capture outside one residual row

The original first planar coefficient is recovered from `u,b` by

`a_l=(sqrt(s)u_l+rho0 b_l)/sqrt(h)`.                           (6.1)

Therefore for the index `k` in Theorem 5.1,

`sum_{l!=k} a_l^2
 <= (2s/h) sum_{l!=k}u_l^2 +(2rho0^2/h)sum_{l!=k}b_l^2`.      (6.2)

Since `h>1/2`, `s<=1`, and `rho0^2<=1-h<1/2`,

`sum_{l!=k} a_l^2
 <=4 sum_{l!=k}u_l^2 +2 sum_{l!=k}b_l^2`.                     (6.3)

Thus whenever `r,d_*,theta ->0`,

`sum_{l!=k}(a_l^2+b_l^2) ->0`.                                (6.4)

At the same time `z_k^2<=d_*->0` and `sum_l z_l^2=1`, so

`sum_{l!=k} z_l^2 ->1`.                                       (6.5)

Hence **all of the residual heavy-plane covariance is asymptotically captured by one physical row, while the transverse spectral direction is asymptotically carried by the complementary diffuse bank.**

Together with the original two heavy physical rows `i,j`, this produces a genuine three-row/full-plane concentration geometry, not merely a third row carrying half of one planar profile.

## 7. Consequence for any putative unbounded non-boundary nested-heavy sequence

The completed fleet03/B13 and fleet01/B13 results already imply along every putative unbounded nested-heavy exact-rank-three sequence

`d_*->0`, `Delta->0`, `D0->0`.                                (7.1)

The assigned fleet02/B13 theorem says that if `alpha beta->0`, then after a subsequence one of the original heavy physical coordinates approaches leverage one. Consider instead a non-boundary subsequence on which

`alpha beta>=eta>0`.                                           (7.2)

Because `alpha=cB<=B`, (7.2) implies `B beta>=eta`. Therefore

`theta=h Delta/(B beta)<=Delta/eta ->0`,                       (7.3)

and from (3.5)

`r <= D0/(2eta)+2 sqrt(2Delta/eta) ->0`.                       (7.4)

Thus (5.2) holds eventually because its left side tends to one while its right side tends to `1/4`. Theorem 5.1 then gives indices `k_m` for which

`b_{k_m}^2/B ->1`,
`u_{k_m}^2/U ->1`,
`z_{k_m}^2 ->0`,                                               (7.5)

and (6.4)-(6.5) show

`sum_{l!=k_m}(a_l^2+b_l^2)->0`,
`sum_{l!=k_m}z_l^2->1`.                                       (7.6)

### Corollary 7.1 — terminal geometry sharpened

Every putative unbounded nested-heavy exact-rank-three sequence has a subsequence of one of the following two types:

1. **leverage-one boundary:** one of the first two physical rows has leverage tending one;
2. **three-row/full-plane plus diffuse-transverse:** three original coordinates `i,j,k` asymptotically carry the entire two-dimensional heavy plane, while all remaining original coordinates asymptotically carry only the final transverse spectral direction, diffusely.

This strictly sharpens the previous `three-planar-heavy plus diffuse-transverse` statement, where the third row was only known to carry asymptotically one half of each relevant planar energy.

## 8. Relation to the assigned partner's finite-direction theorem

The exact limiting geometry in Corollary 7.1(2) has at most four projective row directions: the three concentrated planar rows plus the transverse line. The assigned partner's completed finite-direction theorem

`yspennstate/math-open-problems@8a21bd3d25ce1622121616ce789589e1e073f68d`

therefore pays the exact limit with

`||p_Q||_infinity <92`.                                       (8.1)

This does **not** yet close the approaching sequence. Under the target hypotheses the input supports may escape to infinity, so coefficient convergence alone is not a uniform perturbation principle. For example, even the vanishing scalar perturbation `epsilon X^2` is order one on the perfectly admissible cap-one law

`X ~ Uniform[epsilon^(-1/2), epsilon^(-1/2)+1]`.               (8.2)

Thus one may not silently pass the `<92` bound from the exact four-direction limit to nearby frames. A source-valid stability theorem must preserve arbitrary translations and fragmentation, or aggregate the diffuse bank before taking the limit.

## 9. Exact old/new unpaid implication

**Old unpaid implication:** `QFORM-RANK3-THREE-ISOTROPIC-ROWS-DIFFUSE-TRANSVERSE-v1`, where the third residual row was known only to carry a fixed positive fraction of the remaining planar energy.

**New proved implication:** in every non-boundary unbounded sequence, one residual row captures asymptotically **all** remaining planar energy, and the complementary bank becomes asymptotically purely transverse in total `l2` coefficient energy.

The new first unpaid implication is

`QFORM-RANK3-FOUR-DIRECTION-STABILITY-WITH-ESCAPING-SUPPORT-v1`:

> prove a uniform density/slab bound when three original coordinates carry all but `epsilon` of the heavy-plane coefficient energy and the complementary independent bank carries all but `epsilon` of the transverse energy, with a bound independent of dimension, support locations, fragmentation, and `epsilon` sufficiently small; or construct a genuine cap-one product-law counterexample.

The likely source-valid route is to aggregate the transverse bank **before** conditioning and prove a perturbative version of the four-direction theorem that is affine/translation robust. A plain operator-norm perturbation argument is insufficient by (8.2).

## 10. Status

- `QFORM-NESTED-HEAVY-FULL-PLANAR-STAR-v1`: **PROVED supporting structural theorem**.
- Assigned partner `fleet02/B13`: **substantively applied** through (2.1)-(2.6), (3.5), and the non-boundary dichotomy.
- Exact four-direction limit: **already paid by the completed partner theorem**.
- Stability of nearby frames under arbitrary cap-one product laws: **OPEN**.
- Exact-rank-three QFORM: **OPEN**.
- Full arbitrary-matrix QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuous-density conclusion: **not proved here**.
