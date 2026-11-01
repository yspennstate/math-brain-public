SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T10:08:19Z.
attacking: the common-anchor E2 Schur/star receiver left after the incident-(3+2) cross-disjoint Fourier exit, by replacing independent-disjoint sampling with an entropy/transport certificate and then classifying its failure in physical coordinates.

# fleet02/B02 — common-anchor E2 transport receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T100819Z-fleet02-B02-qform-r11`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on every new `phi_Q in L1` branch below; unrestricted continuity remains open.  
**Target-wide unweighted Fourier criterion:** `OPEN_NOT_REFUTED`.

## 1. Source boundary and the analytic review requested by the owner

The target is unchanged: the coordinates are independent ORIGINAL real variables with probability densities at most one, and the real symmetric matrix has at least three eigenvalues of modulus at least one. No moments, support hypothesis, log-concavity, iid assumption, diagonal-basis independence or post-rotation independence is used.

The required newest-Claude package was read at the pinned commit

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`,

and the owner continuation was read at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

I independently rechecked the analytic/constants/endpoints part of the sharp Hausdorff--Young refinement. For a physical cross block `M=A[I,J]`, put `Z3=e3(M^T M)`. If the third-volume row marginals satisfy `alpha_i<=q/2`, `1<=q<3/2`, Beckner Hausdorff--Young gives

`|| |psi_i(2t .)|^q ||_(1/alpha_i)
 <= (pi/|t|)^alpha_i
    (alpha_i/q)^(alpha_i/2)
    (1-alpha_i/q)^(-(q-alpha_i)/2)`.                            (1.1)

The `alpha_i` powers cancel the volume-sampling BL normalization. Since `sum alpha=sum beta=3` and `-(1-s)log(1-s)<=s`, the two entropy products contribute at most `e^(3/2)` each, hence

`E F_t^q <= e^3 q^(-3/2)(pi/|t|)^3 Z3^(-1/2)`.                 (1.2)

Thus

`|phi_Q(t)| <= min(1,K|t|^(-3/(2q)))`,                          (1.3)

and exact integration followed by Fourier inversion gives

`boxed:
 ||p_Q||_infinity
 <= 3e/[(3-2q)sqrt(q)] Z3^(-1/6).
}`                                                               (1.4)

The endpoint bookkeeping is exact: `q=1` is allowed; `q=3/2` gives only `|t|^-1` and is not an `L1_t` endpoint; `q<3/2` is precisely the integrable range of this envelope. The same sharp-HY calculation at exterior degree five gives the ungated paid exit

`boxed:
 ||p_Q||_infinity <= (5e/sqrt(2)) E5(M)^(-1/10).
}`                                                               (1.5)

Therefore the analytic/constants/endpoints scope assigned to fleet02/B02 is **PASS**. I do not claim the separately assigned matrix/tail review.

The newest compatible designated partner `fleet03/B02` is r25,

`QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1`,

at `yspennstate/math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T085705Z-fleet03-B02-qform-r25/REPORT.md`.

The immediately preceding B02 report is pinned at

`yspennstate/math-open-problems@94189deb89884b0dd57057041ec04f98a85e6764`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T091200Z-fleet02-B02-QFORM-auto11/REPORT.md`.

It left the explicit debt `QFORM-COMMON-ANCHOR-E2-SCHURSTAR-RECEIVER-v1`.

## 2. The live common-anchor packet

Let `I,J` be disjoint original-coordinate banks and

`B=A[I,J]`.

All same-bank quadratic terms, all outside coordinates/couplings, and all affine terms are arbitrary. Fix an outer physical row anchor `x in I` and column anchor `y in J`. Define the incident third volume

`J3 = sum det B[{x} union R,{y} union T]^2`,                    (2.1)

where `R subset I\{x}`, `T subset J\{y}`, `|R|=|T|=2`. Let

`N=B[I\{x},J\{y}]`, `E2=e2(N^T N)`.                             (2.2)

Write `mu3` for the normalized squared incident-minor law in (2.1), viewed as a law on residual row/column pairs `(R3,T3)`.

The preceding B02 cross-disjoint theorem showed that in the two-sided D' failure collar one has

`J3>Z3/3`,                                                       (2.3)

where `Z3=E3(B)`, and if its first `L1_t` exit fails at the concrete threshold used there, one gets a fixed residual physical row `i` and column `j` with

`H := H2^(i,j)(N)
   = sum_(R contains i,T contains j) det N[R,T]^2
   > 7E2/32.`                                                    (2.4)

The completed partner r25 identity is exact. Reindex this residual anchor first,

`N=[[a,r^T],[c,M]]`.                                             (2.5)

Then

`boxed:
 H=||aM-c r^T||_F^2.
}`                                                               (2.6)

If `a!=0`, this is `a^2||M-c r^T/a||_F^2`; if `a=0`, it is the exact two-star product `||c||_2^2||r||_2^2`. The theorem below uses `H` directly and therefore does **not** divide by `a` and does not distinguish those two algebraic cases.

Let `nu` be the normalized squared-minor law defining `H`. Every row sample under `nu` is `{i,K}` for a single far residual row `K`, and every column sample is `{j,L}` for a single far residual column `L`.

## 3. New theorem — `QFORM-INCIDENT32-DISJOINT-TRANSPORT-L1-v1`

The independent-disjoint event used previously is stronger than necessary. What the BL/HY proof actually needs is only a pair of determinant laws whose inclusion marginals can be **coupled disjointly**.

### Theorem 3.1

Let `F` be any nonempty family of residual `2x2` minors of `N`, with total squared mass

`H_F=sum_((R,T) in F) det N[R,T]^2>0`,                           (3.1)

and normalized squared-minor law `mu2`. Let `tilde_mu3 << mu3` and `tilde_mu2 << mu2` be probability laws. Assume there exists a coupling `Pi` of their **row-pair marginals** supported on

`R3 cap R2=empty`.                                                (3.2)

Put

`D3=D(tilde_mu3||mu3)`, `D2=D(tilde_mu2||mu2)`.                 (3.3)

Then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity and

`boxed:
 integral_R |phi_Q(t)| dt
 <= 10*pi*e*2^(-1/5)
    exp((D3+D2)/10) (J3 H_F)^(-1/10),
}`                                                               (3.4)

hence

`boxed:
 ||p_Q||_infinity
 <= 5e*2^(-1/5)
    exp((D3+D2)/10) (J3 H_F)^(-1/10).
}`                                                               (3.5)

The identical statement holds with a column-disjoint coupling, by transposing `B`.

### Proof

One-sided Cauchy--Schwarz/Weyl differencing in the original `J` bank gives

`|phi_Q(t)|^2
 <= integral prod_(u in I) h_u((Bw)_u)
             prod_(v in J) g_v(w_v) dw`,                         (3.6)

where `h_u(s)=|psi_u(2ts)|` and `g_v=f_v*tilde f_v` has mass one and cap at most one. All same-bank quadratic and affine phases have disappeared through this legitimate differencing step; no sum/difference independence is asserted.

Let `alpha^(3),beta^(3)` be the inclusion marginals of `tilde_mu3`, and `alpha^(2),beta^(2)` those of `tilde_mu2`. In the diagonal-plus-PSD Gaussian determinant expansion retain two positive basis families.

The incident-third family gives by weighted AM--GM

`A3 >= J3 exp(-D3) d_x
       prod_(u!=x)d_u^(alpha_u^(3))
       prod_(v!=y)e_v^(1-beta_v^(3)).`                           (3.7)

The selected residual-two family gives

`A2 >= H_F exp(-D2) e_y
       prod_(u!=x)d_u^(alpha_u^(2))
       prod_(v!=y)e_v^(1-beta_v^(2)).`                           (3.8)

Define equal-mixture exponents

`alpha_x=1/2`,
`alpha_u=(alpha_u^(3)+alpha_u^(2))/2` for u!=x,                 (3.9)

and similarly `beta_y=1/2`, `beta_v=(beta_v^(3)+beta_v^(2))/2`. The disjoint coupling (3.2) implies pointwise

`1_(u in R3)+1_(u in R2)<=1`,                                   (3.10)

hence

`0<=alpha_u<=1/2`, `sum alpha=5/2`.                             (3.11)

No analogous cap is required on the `beta` side; only `0<=beta_v<=1`, `sum beta=5/2` is used.

Since the full Gaussian determinant contains `A3+A2`,

`det(D_J+B^T D_I B)
 >=2 (J3 H_F)^(1/2) exp[-(D3+D2)/2]
   prod_u d_u^alpha_u prod_v e_v^(1-beta_v).`                   (3.12)

Lieb's Gaussian characterization therefore gives

`BL <=2^(-1/2) exp[(D3+D2)/4](J3H_F)^(-1/4)
      prod_u alpha_u^(-alpha_u/2)
      prod_v(1-beta_v)^(-(1-beta_v)/2).`                         (3.13)

At the exact `q=1` sharp-HY gate, for `0<c<=1/2`,

`int |psi_u(2ts)|^(1/c) ds
 <=(pi/|t|)sqrt(c)(1-c)^(-(1-c)/(2c)).`                          (3.14)

The `sqrt(c)` factors cancel the inverse-alpha normalization in (3.13). The row and column entropy products are each at most `e^(5/4)`, so

`|phi_Q(t)|^2
 <=2^(-1/2)e^((D3+D2)/4)e^(5/2)pi^(5/2)
   (J3H_F)^(-1/4)|t|^(-5/2).`                                   (3.15)

Thus

`|phi_Q(t)|
 <=min{1,
 2^(-1/4)e^(5/4)pi^(5/4)e^((D3+D2)/8)
 (J3H_F)^(-1/8)|t|^(-5/4)}.`                                    (3.16)

Finally

`int_R min(1,A|t|^(-5/4))dt=10A^(4/5)`.                         (3.17)

Equations (3.16)--(3.17) yield (3.4), and Fourier inversion yields (3.5). QED.

### Corollary 3.2 — the old independent event is only one feasible transport

If

`delta_r=P_(mu3 tensor mu2)(R3 cap R2=empty)>0`,                (3.18)

condition the product law on this event. Its two marginal KL divergences have sum at most `log(1/delta_r)`, so Theorem 3.1 recovers

`||p_Q||_infinity
 <=5e*2^(-1/5) delta_r^(-1/10)(J3H_F)^(-1/10).`                 (3.19)

The transport form is strictly more flexible: a low-cost disjoint coupling can exist even when independent disjoint sampling is very inefficient.

## 4. Anchored H2 has an exact weighted Hall test

Now take `H_F=H` from (2.4). Let

`p_i=P_mu3(i in R3)`.                                            (4.1)

Assume first `p_i<1`, and condition the incident law on `i notin R3`; call the resulting row-pair law `bar_mu`. Its KL cost is exactly

`D(bar_mu||mu3)=log(1/(1-p_i)).`                                (4.2)

Let `kappa_k=P_nu(K=k)` be the far-row marginal of the anchored H2 law. For `bar_mu`, put

`bar_p_k=P(k in R)`,
`bar_m_kl=P(R={k,l})`.                                           (4.3)

A coupling of `bar_mu` and `kappa` supported on `K notin R` exists **if and only if**

`kappa_k <= 1-bar_p_k` for every k,                              (4.4)

and

`kappa_k+kappa_l <= 1-bar_m_kl` for every k!=l.                 (4.5)

Indeed this is the weighted Hall/max-flow criterion for the bipartite graph whose allowed edges are `(R,k)` with `k notin R`. For a set `A` of singleton vertices, a row-pair `R` has no neighbor in `A` exactly when `A subset R`. Since `|R|=2`, Hall constraints for `|A|>=3` are automatic; `|A|=1` gives (4.4), and `|A|=2` gives (4.5). Thus (4.4)--(4.5) are complete, not merely sufficient.

### Corollary 4.1 — zero-reciprocal common-anchor receiver

If

`p_i<=3/4`                                                       (4.6)

and the Hall conditions (4.4)--(4.5) hold, Theorem 3.1 applies with `D2=0`, `D3<=log 4`, giving

`boxed:
 ||p_Q||_infinity
 <=5e*2^(-1/5)4^(1/10)(J3H)^(-1/10)
 <13.591410 (J3H)^(-1/10).
}`                                                               (4.7)

This is a genuine integrated-characteristic-function estimate on the common-anchor packet. It pays both the partner's exact two-star case `a=0` and the algebraic cross-Schur case `a!=0` without dividing by `a` and without identifying the cross Schur expression with a TRUE full symmetric-pair Schur complement.

The same result holds from the column side if the corresponding incident column anchor probability is at most `3/4` and its Hall conditions hold.

### What Hall failure means physically

The Hall test also has a finite physical obstruction. If (4.4) fails, then

`kappa_k+bar_p_k>1`,                                             (4.8)

so either `kappa_k>1/2` or `bar_p_k>1/2`. If (4.5) fails, then

`kappa_k+kappa_l+bar_m_kl>1`,                                   (4.9)

so either `kappa_k+kappa_l>1/2` or `bar_m_kl>1/2`.

Under (4.6), `1-p_i>=1/4`. Consequently every Hall failure forces one of the following actual packets:

* more than half of `H` lies on anchored H2 minors whose far row belongs to a fixed one- or two-row set; or
* more than `J3/8` of the incident third volume contains one fixed additional residual row, or even one fixed residual row pair.

No tiny individual determinant has been selected in deriving this alternative.

## 5. Application to the live D' / D5 collar

The source result (1.4) at `q=4/3` pays either D' orientation when all corresponding third-volume marginals are at most `2/3`. If both orientations fail, choose a heavy outer row `x` and column `y`; inclusion--exclusion in the normalized third-minor law gives (2.3), `J3>Z3/3`. The ungated D5 estimate (1.5) remains an independent exit whenever fifth exterior volume is large enough at the desired scale.

On the residual handed to this run by the preceding B02 theorem, (2.4) also holds. Substituting (2.3)--(2.4) into the Hall receiver (4.7) gives the actual inequality

`boxed:
 ||p_Q||_infinity
 <17.659639 (Z3 E2)^(-1/10),
}`                                                               (5.1)

whenever either physical orientation passes its `3/4` anchor test and exact weighted Hall test.

This applies the completed partner r25 packet (2.6) to a new Fourier inequality rather than merely citing it.

There is a second paid exit which needs no Hall test. Define the anchored product-disjointness probabilities

`delta_r^H=P_mu3,nu(R3 cap {i,K}=empty)`,
`delta_c^H=P_mu3,nu(T3 cap {j,L}=empty)`.                        (5.2)

If

`max(delta_r^H,delta_c^H)>=1/32`,                               (5.3)

Corollary 3.2 and (2.3)--(2.4) give

`boxed:
 ||p_Q||_infinity
 <21.741566 (Z3 E2)^(-1/10).
}`                                                               (5.4)

Thus the common-anchor Schur/star packet is now paid whenever either (a) it admits the exact low-entropy Hall transport or (b) ordinary independent disjoint sampling has probability at least `1/32`.

## 6. Exact residual after both new exits fail

The point of using both transport and independent-disjoint compilers is that their simultaneous failure gives a much smaller physical collar.

Suppose the row-side exits fail. If `p_i>3/4`, record the **anchor-heavy** alternative

`P_mu3(i in R3)>3/4`.                                            (6.1)

Otherwise `p_i<=3/4`; because the event exit also failed, `delta_r^H<1/32`. Conditioning on `i notin R3`, whose probability is at least `1/4`, gives

`E[ P(K notin R3) | i notin R3 ]
 = delta_r^H/(1-p_i) <1/8.`                                     (6.2)

Hence some incident residual row pair `R0` with `i notin R0` satisfies

`boxed:
 P_nu(K in R0)>7/8.
}`                                                               (6.3)

So the only row-side survivors are: incident volume is `>3/4` anchored at `i`, or more than `7/8` of the anchored H2 packet has its far row in one fixed two-row set. The identical column dichotomy holds for `j` and a fixed far-column pair `T0`.

This leaves four finite configurations.

### 6.1 Anchor-heavy on both sides

If both incident anchor probabilities exceed `3/4`, then by inclusion--exclusion under `mu3`,

`P_mu3(i in R3 and j in T3)>1/2`.                               (6.4)

Therefore the partner r25 double-anchored incident mass obeys

`G3^(x,i;y,j)(B)>J3/2>Z3/6.`                                    (6.5)

Move physical rows `(x,i)` and columns `(y,j)` first and write

`B=[[P,R],[C,M1]]`.                                              (6.6)

The completed partner identity now gives the actual obstruction inequality

`boxed:
 ||det(P)M1-C adj(P)R||_F^2 > Z3/6.
}`                                                               (6.7)

If `det(P)!=0`, this is

`|det(P)| ||M1-C P^(-1)R||_F > sqrt(Z3/6)`.                     (6.8)

If `det(P)=0`, positivity forces `rank P=1`; factoring `adj(P)=uv^T` gives the inverse-free two-star obstruction

`boxed:
 ||Cu||_2 ||R^T v||_2 > sqrt(Z3/6).
}`                                                               (6.9)

This is the second concrete application of the designated partner result.

### 6.2 Concentrated on both sides

If (6.3) holds on both physical sides, then under the anchored H2 law

`P(K in R0)>7/8`, `P(L in T0)>7/8`.                              (6.10)

Hence

`P(K in R0,L in T0)>3/4`.                                       (6.11)

There are at most four pairs `(k,l) in R0 x T0`, so one literal physical residual `2x2` cross minor satisfies

`det N[{i,k},{j,l}]^2 > 3H/16 > 21E2/512.`                      (6.12)

Thus this endpoint is no longer a diffuse compound statement: a fixed `3`-row by `3`-column residual core containing `(i,j)` carries a definite fraction of the H2 packet, and one of its four anchored minors carries more than `21/512` of all residual `E2`.

Equation (6.12) is a structural certificate only; it is **not** fed into a false rule saying that one cross minor is automatically a good TRUE principal pair.

### 6.3 The two mixed configurations

The remaining two cases are symmetric:

* `P_mu3(i in R3)>3/4` while more than `7/8` of `H` has far column in a fixed two-column set; or
* more than `7/8` of `H` has far row in a fixed two-row set while `P_mu3(j in T3)>3/4`.

These are one-sided double-anchor / bounded-width H2-strip geometries. They are strictly narrower than the previous generic Schur/star packet and identify the next mixed-hub receiver without selecting a vanishing local pivot.

## 7. Why the argument survives the correction inbox

The preserved corrections are respected literally.

* No law-uniform pointwise estimate for `E exp(itX^2)` is used; all decay comes from Weyl differencing plus sharp Hausdorff--Young and Brascamp--Lieb.
* No rotated random coordinates are declared independent.
* No arbitrary conditional projection density is assigned cap one.
* The partner identity `H=||aM-cr^T||_F^2` is used only as an algebraic cross-block identity. When `a!=0`, `M-cr^T/a` is **not** called the TRUE full symmetric pair Schur residual.
* The exact two-star case `a=0` is retained, so the fresh near-zero/half-Riesz correction is not bypassed by replacing zero with a merely small coefficient.
* No small matrix tail is deleted as a law-uniformly small random perturbation.

The newest source counterexample search found no target counterexample. This run likewise found no source-valid target counterexample to the stronger statement `int |phi_Q|<infinity`; that target-wide criterion remains open rather than refuted.

## 8. First unpaid implication

The first unpaid implication is now

`QFORM-TRANSPORT-FAIL-MIXEDHUB-RECEIVER-v1`.

After D', D5, the preceding incident-(3+2) compiler, and the new transport receiver, the live common-anchor collar has only the four configurations in Section 6. The next useful mechanism should pay one of:

1. the partner double-anchor Schur/two-star packet (6.7)--(6.9),
2. the fixed bounded-width residual core (6.12), or
3. one of the two one-sided anchor/strip hybrids,

while keeping arbitrary same-bank curvature and original-coordinate product provenance. A grouped hub/graph-BL argument or a separately verified TRUE pair/scalar Schur theorem is source-valid; simply inverting a tiny cross edge, treating the algebraic cross Schur packet as a true symmetric Schur residual, or reverting to pointwise scalar Fresnel decay is not.

## 9. Deterministic regression

`CHECK.py` beside this report recomputes the constants and independently compares the weighted Hall conditions (4.4)--(4.5) against a linear-program feasibility test for 500 deterministic-seed random laws on 2-subsets/singletons. The captured values are

`base=11.832008884813199`,
`hall_log4=13.591409142295225`,
`live_hall=17.659638353384853`,
`live_event_eta_1_32=21.741565100461380`,
`fixed_minor_ratio=21/512=0.041015625`,

with `hall_lp_mismatches=0/500` and `STATUS=PASS`.

This numerical check is not the proof; Sections 3--6 are symbolic.

## 10. Status

`ESSENTIAL_STEP_APPLIED`. The full QFORM conjecture remains OPEN. The new result turns the preceding common-anchor E2 Schur/star debt into an actual integrated-Fourier bound on every low-entropy disjoint-transport branch, with a finite physical concentration classification on the complement. Continuity is established only on the new `phi_Q in L1` exits.
