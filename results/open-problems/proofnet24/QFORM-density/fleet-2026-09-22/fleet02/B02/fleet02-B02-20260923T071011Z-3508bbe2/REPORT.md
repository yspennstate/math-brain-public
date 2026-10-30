SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T07:10:11Z.
attacking: the first unpaid high-volume/high-marginal edge-times-E2 branch by a direct original-coordinate integrated Fourier estimate, avoiding the corrected false identification of a cross-only Schur packet with a true physical-pair Schur packet.

# fleet02/B02 — sharp-HY mixed edge/E2 L1 compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet02-B02-20260923T071011Z-3508bbe2`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new L1-Fourier branch only; full-target continuity remains open.

## 1. Exact obligation and current boundary

The target remains unrestricted: independent ORIGINAL real coordinates with densities at most one and a real symmetric matrix having at least three eigenvalues of modulus at least one. No moments, support restrictions, log-concavity, identical laws, diagonal-basis independence, or post-rotation independence are used.

The required newest Claude package was used at its actual scopes: D' on third exterior volume, D5 on fifth exterior volume, and the reviewed sharp Hausdorff--Young refinement. The latest designated `fleet03/B02` result was also consumed: `QFORM-PAIR-TRUE-SCHUR-E2-UNCONDITIONAL-v1` at `yspennstate/math-open-problems@40bf94187444ad5a6008bcf4b06931689b0e7383`, which pays the invertible-indefinite TRUE-pair-Schur E2 branch without an E2 marginal gate.

Two corrections are essential here. First, the current `fleet03/B02` r21 repair shows that the cross-only anchored Schur packet need not equal the TRUE physical-pair Schur packet when same-side anchor couplings are present. Second, the fresh `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1` correction forbids treating a small matrix perturbation as a law-uniformly small output perturbation. The new argument below uses neither identification nor perturbative passage: it works directly in the exact physical cross block under one-sided Weyl differencing.

## 2. Paid preceding exits on the same physical cross block

Let `I,J` be disjoint original-coordinate banks and

`B=A[I,J]`.

All same-bank quadratic terms, all outside couplings/spectrum, and all affine terms are arbitrary.

The reviewed sharp-HY fractional-volume theorem gives, with `Z3=E3(B)=e3(B^T B)`,

`||p_Q||infinity <= 3e/[(3-2q)sqrt(q)] Z3^(-1/6)`                 (2.1)

whenever the normalized squared 3-minor row marginals are at most `q/2`, `1<=q<3/2`; the same applies after transposing `B`. At `q=4/3`,

`||p_Q||infinity <= (9sqrt(3)e/2) Z3^(-1/6)`                     (2.2)

under the exact `2/3` marginal gate.

The reviewed D5 branch is

`||p_Q||infinity <= (5e/sqrt(2)) E5(B)^(-1/10)`.                  (2.3)

It has no marginal gate. Equations (2.1)-(2.3) are genuine integrated-characteristic-function bounds and give continuous densities on their stated branches.

The problem below is the complementary collar: D' fails on both orientations and D5 is unavailable or too small to pay the desired uniform scale.

## 3. Setup for the new edge/E2 transducer

Choose an actual physical anchor row `x in I` and column `y in J` and reindex them first:

`B = [[a, r^T], [c, N]]`,                                        (3.1)

where `N` is the residual physical cross block. Assume `a!=0` and put

`S=N-c r^T/a`.                                                    (3.2)

The exact incident-minor identity is

`J := sum_(R,T) det B[{x} union R,{y} union T]^2
   = a^2 E2(S)`,                                                   (3.3)

where `R,T` run over residual row/column pairs. Put

`E=E2(N)`.                                                        (3.4)

Assume `J,E>0`. Define the normalized squared 2-minor laws

`nu_S(R,T)=det S[R,T]^2/E2(S)`,
`nu_N(R,T)=det N[R,T]^2/E2(N)`.                                   (3.5)

Draw independent full minor samples `(R_S,T_S)~nu_S` and `(R_N,T_N)~nu_N`, and define the row and column cross-disjointness probabilities

`delta_r=P(R_S cap R_N=empty)`,
`delta_c=P(T_S cap T_N=empty)`.                                   (3.6)

These are deterministic functions of the exact physical cross block; they introduce no random-variable rotation.

## 4. Main theorem — `QFORM-EDGE-E2-CROSSDISJOINT-SHARP-HY-L1-v1`

### Theorem 4.1

In the setup above, if `delta_r>0`, then the full ambient quadratic form has a continuous density satisfying

`boxed:
  integral_R |phi_Q(t)| dt
  <= 10*pi*e^(4/5) (delta_r J E)^(-1/10),
}`                                                                  (4.1)

and hence

`boxed:
  ||p_Q||infinity
  <= 5 e^(4/5) (delta_r J E)^(-1/10)
  < 11.127705 (delta_r J E)^(-1/10).
}`                                                                  (4.2)

The identical conclusion holds with `delta_c` in place of `delta_r`, by transposing the cross block.

This is a direct unweighted L1 characteristic-function estimate. It uses no physical-pair inverse and is therefore valid even when the anchor's full symmetric `2x2` principal pair is singular.

### Proof

Condition all coordinates outside `I union J`. The resulting quadratic polynomial has the same physical cross block `B`; only arbitrary same-bank and affine terms are added. One-sided Weyl differencing in the `J` bank gives the standard product-preserving estimate

`|phi_Q(t)|^2
 <= integral_(R^J) prod_(i in I) h_i((B w)_i)
                    prod_(j in J) g_j(w_j) dw`,                   (4.3)

where

`h_i(s)=|psi_i(2ts)|`,                                            (4.4)

`psi_i` is the characteristic function of the original cap-one density `f_i`, and `g_j=f_j*f_j~` is the density of the independent difference `X_j-X_j'`. Thus

`0<=g_j<=1`, `integral g_j=1`.                                   (4.5)

Every same-bank quadratic phase and every affine phase has disappeared from the absolute-value integrand in (4.3). This is precisely why the r21 cross-Schur/true-Schur correction does not affect the present route.

Now condition the independent pair of full minor samples in (3.5) on

`R_S cap R_N=empty`.                                              (4.6)

Let `mu_S,mu_N` be the two conditioned marginal laws. Their relative entropies obey

`D(mu_S||nu_S)+D(mu_N||nu_N)
 <= log(1/delta_r)`,                                               (4.7)

because the KL divergence of the conditioned joint law from `nu_S tensor nu_N` is exactly `log(1/delta_r)` and splits as the two marginal divergences plus mutual information.

Let `alpha_k^S,alpha_k^N` be the conditioned residual-row inclusion marginals and `beta_l^S,beta_l^N` the conditioned residual-column inclusion marginals. Put

`alpha_k=(alpha_k^S+alpha_k^N)/2`,
`beta_l=(beta_l^S+beta_l^N)/2`.                                   (4.8)

Each sampled row set has size two and the two row sets are disjoint pointwise under (4.6), so

`0<=alpha_k<=1/2`, `sum_k alpha_k=2`.                             (4.9)

Also `0<=beta_l<=1`, `sum_l beta_l=2`.                            (4.10)

Apply geometric Brascamp--Lieb to the integral in (4.3), using exponents

- anchor row of `B`: `1/2`;
- residual row `k`: `alpha_k`;
- anchor coordinate map `e_y`: `1/2`;
- residual coordinate map `e_l`: `1-beta_l`.

The exponents sum to `|J|`, the dimension of the differenced bank.

To bound the BL Gaussian determinant, use two exact basis families. Family S selects the anchor row of `B`, two residual rows `R`, and all coordinate basis vectors outside `{y} union T`; its basis determinant is

`det B[{x} union R,{y} union T] = a det S[R,T]`.                  (4.11)

Family N selects the anchor coordinate vector `e_y`, two residual rows `R`, and all residual coordinate vectors outside `T`; its basis determinant is

`det N[R,T]`.                                                     (4.12)

Let `p_x,p_k,q_y,q_l>0` denote arbitrary Gaussian weights in the determinant formula. Weighted AM--GM with `mu_S` on family S gives

`A_S >= J exp(-D(mu_S||nu_S)) p_x
        prod_k p_k^(alpha_k^S)
        prod_l q_l^(1-beta_l^S)`.                                 (4.13)

The N family gives

`A_N >= E exp(-D(mu_N||nu_N)) q_y
        prod_k p_k^(alpha_k^N)
        prod_l q_l^(1-beta_l^N)`.                                 (4.14)

Since the full determinant contains both nonnegative basis sums,

`det(...) >= A_S+A_N >=2 sqrt(A_S A_N)`.                          (4.15)

The factor two in (4.15) exactly cancels the two `1/2`-exponent normalization factors from the anchor row and anchor coordinate in Lieb's Gaussian formula. Therefore the BL constant obeys

`BL <= exp((D_S+D_N)/4) (J E)^(-1/4)
      prod_k alpha_k^(-alpha_k/2)
      prod_l (1-beta_l)^(-(1-beta_l)/2)`.                         (4.16)

Using (4.7),

`exp((D_S+D_N)/4) <= delta_r^(-1/4)`.                            (4.17)

Now insert the reviewed sharp Hausdorff--Young estimate. With Fourier convention `hat f(u)=integral exp(iux)f(x)dx`, Beckner's sharp inequality and `0<=f<=1`, `integral f=1`, imply for every `rho>=2`

`integral |hat f(u)|^rho du
 <=2pi rho^(-1/2) [rho/(rho-1)]^((rho-1)/2)`.                    (4.18)

Equivalently, for `0<c<=1/2`, after the scaling in (4.4),

`integral h_i(s)^(1/c) ds
 <=(pi/|t|) sqrt(c) (1-c)^(-(1-c)/(2c)).`                         (4.19)

Write each original factor `h_i` as `(h_i^(1/c_i))^(c_i)` with the BL row exponent `c_i`. For residual rows, the factor `alpha_k^(alpha_k/2)` supplied by (4.19) cancels the inverse alpha factor in (4.16). At the anchor `c=1/2`, the corresponding `c` and `1-c` factors cancel each other. Hence the row norm product contributes

`(pi/|t|)^(5/2)
 prod_k (1-alpha_k)^(-(1-alpha_k)/2)`.                            (4.20)

The coordinate functions contribute at most one by (4.5). Finally,

`- (1-u) log(1-u) <= u`,                                         (4.21)

so, using (4.9)-(4.10), both entropy products satisfy

`prod_k (1-alpha_k)^(-(1-alpha_k)/2) <= e`,
`prod_l (1-beta_l)^(-(1-beta_l)/2) <= e`.                        (4.22)

Combining (4.3), (4.16)-(4.22) yields

`|phi_Q(t)|^2
 <= e^2 pi^(5/2) delta_r^(-1/4)(J E)^(-1/4)|t|^(-5/2)`.         (4.23)

Thus

`|phi_Q(t)|
 <= min{1,
        e pi^(5/4)(delta_r J E)^(-1/8)|t|^(-5/4)}.`              (4.24)

For `A>0`,

`integral_R min(1,A|t|^(-5/4))dt =10 A^(4/5)`.                  (4.25)

Apply (4.25) to (4.24):

`integral |phi_Q(t)|dt
 <=10 pi e^(4/5)(delta_r J E)^(-1/10)`,                          (4.26)

which is (4.1). Fourier inversion gives (4.2), continuity, and vanishing at infinity. QED.

Zero exponents in (4.16) are handled by omission/limits exactly as in the endpoint-safe diagonal-plus-PSD determinant expansion of the reviewed Theorem D; no positivity of a discarded Gaussian coordinate parameter is assumed.

## 5. Exact failure certificate — two-row/two-column residual compound hub

The new theorem has a clean structural complement rather than an unspecified marginal failure. From the definition of `delta_r`,

`delta_r
 = E_((R,T)~nu_S) [ E2(N[R^c,*]) / E2(N) ]`.                    (5.1)

Therefore, for every `eta>0`, if `delta_r<eta` there is a physical residual row pair `H` in the support of `nu_S` such that

`E2(N[H^c,*]) < eta E`.                                          (5.2)

Similarly, `delta_c<eta` produces a residual column pair `L` with

`E2(N[*,L^c]) < eta E`.                                          (5.3)

If both disjointness probabilities are `<eta`, then under the canonical squared-2-minor law of `N`, the row pair intersects `H` with probability `>1-eta` and the column pair intersects `L` with probability `>1-eta`. Hence by the union bound

`boxed:
 sum_(R cap H !=empty, T cap L !=empty) det N[R,T]^2
 > (1-2eta) E.
}`                                                                  (5.4)

At `eta=1/16`, more than `7/8` of the entire residual second exterior volume passes simultaneously through one fixed two-row/two-column physical compound hub. At the exact endpoint `delta_r=0`, some such `H` leaves `rank N[H^c,*] <=1`; similarly for columns.

This gives an exhaustive local alternative: either the mixed edge/E2 characteristic function is integrable, or the residual E2 currency is physically concentrated on four anchor coordinates before any reciprocal minor is paid.

## 6. Application to the live D' failure branch

Take `q=4/3` in D'. Suppose its row and column marginal gates both fail. Under the normalized squared 3-minor law, choose a heavy physical row `x` and column `y`. Since their inclusion probabilities are each `>2/3`,

`P(x in row triple AND y in column triple)>1/3`.                 (6.1)

Thus the joint incident mass of this anchor pair satisfies

`J>Z3/3`.                                                         (6.2)

The completed joint-star block compiler gives, for (3.1),

`sqrt(J) <= |a| sqrt(E) + ||c|| ||r|| F_perp`,                   (6.3)

where `F_perp=||P_(c^perp) N P_(r^perp)||_F`.

If the two-star term in (6.3) is at least `sqrt(J)/2`, it is the already identified two-star transverse branch. Suppose instead the edge/E2 term fires:

`a^2 E >= J/4 > Z3/12`.                                          (6.4)

Then `a!=0`, and Theorem 4.1 is applicable whenever either `delta_r` or `delta_c` is positive. Quantitatively, if

`max(delta_r,delta_c)>=eta`,                                     (6.5)

then (4.2), (6.2), and (6.4) give

`boxed:
 ||p_Q||infinity
 < 5 e^(4/5) [36 a^2/eta]^(1/10) Z3^(-1/5).
}`                                                                  (6.6)

This is an actual integrated-Fourier payment of the edge-times-E2 currency and requires neither a true-pair inverse nor an E2 marginal gate.

In the strict no-`tau`-pivot class, `|A_kk|<tau` and every physical pair determinant has modulus `<tau`, so the anchor edge obeys

`a^2 < tau(1+tau)`.                                               (6.7)

Consequently

`||p_Q||infinity
 < 5 e^(4/5) [36 tau(1+tau)/eta]^(1/10) Z3^(-1/5).`              (6.8)

At the concrete values `tau=1/64`, `eta=1/16`,

`boxed: ||p_Q||infinity < 13.884 Z3^(-1/5).`                      (6.9)

If both disjointness parameters are `<1/16`, (5.4) instead forces more than `7/8` of `E2(N)` through a fixed residual two-row/two-column compound hub. Thus the edge/E2 branch no longer ends at a generic second-volume marginal obstruction.

## 7. Latest designated partner result actually applied

The latest compatible completed `fleet03/B02` theorem is `QFORM-PAIR-TRUE-SCHUR-E2-UNCONDITIONAL-v1`, source

`yspennstate/math-open-problems@40bf94187444ad5a6008bcf4b06931689b0e7383`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T053047Z-fleet03-B02-qform-auto11/REPORT.md`.

For an invertible indefinite physical pair `P`, with `D=|det P|`, `kappa=sigma_min(P)`, and a physical cross block `T` of its TRUE Schur residual with `Delta=E2(T)>0`, it proves

`||p_Q||infinity
 <=17.607048 (D kappa)^(-1/4) Delta^(-1/16)`.                    (7.1)

I apply (7.1) as the paid receiver on the r21 correction-safe true-Schur alternative. In particular, r21 gives on its `q=4/3` true-Schur branch

`a^2 Delta > Z3/12`,                                              (7.2)

so (7.1) yields the actual inequality

`||p_Q||infinity
 <20.565316 |a|^(1/8)(D kappa)^(-1/4) Z3^(-1/16)`.               (7.3)

This branch needs no residual E2 marginal gate. The new Theorem 4.1 is complementary: it is a genuine `L1_t` estimate on the exact physical cross block and does not require `D kappa>0`, so it supplies a new route on singular-pair or pair-inversion-hostile edge/E2 configurations. On any overlap one may take the minimum of (4.2) and (7.1).

## 8. What remains

The full three-large-eigenvalue conjecture remains OPEN. No target-valid counterexample to the full unweighted `integral |phi_Q|` criterion was found; that stronger criterion also remains OPEN target-wide.

The first unpaid B02 implication is now

`QFORM-FOUR-ANCHOR-E2-HUB-ROUTING-v1`:

starting from the failure certificate (5.4), spend a residual E2 law with a universal fraction of its determinant mass simultaneously incident to a fixed two-row and two-column physical hub. The intended exits are a direct mixed-hub/graph-BL L1 estimate, a grouped hyperbolic receiver, a paid physical pair/triple, or a second physical cross block with a D'/D5/disjointness certificate. No local tiny minor should be selected before aggregation.

The other live r21 debts remain the same-side correction packet and the genuinely singular pair when the new disjointness branch also collapses. The fresh matrix-perturbation correction is preserved: none of these steps uses a law-uniform output continuity argument in `||A-A0||op`.

## 9. Deterministic checks

A deterministic 200-instance algebra check is saved beside this report. It checks the exact incident identity (3.3), conditioned average row marginal `<=1/2`, the entropy inequality (4.7), and the mixed determinant lower bound (4.15). The saved output ends `STATUS=PASS` with maximum relative incident-identity error `3.11e-14`, maximum conditioned average row marginal `0.5000000000000007`, maximum KL excess `-0.94327`, and maximum determinant-RHS/LHS ratio `0.20270`. It also evaluates

`5e^(4/5)=11.127704642462339`

and the concrete coefficient in (6.9) as `13.883634728174602`.

These computations are regression checks only; the theorem is proved symbolically above.
