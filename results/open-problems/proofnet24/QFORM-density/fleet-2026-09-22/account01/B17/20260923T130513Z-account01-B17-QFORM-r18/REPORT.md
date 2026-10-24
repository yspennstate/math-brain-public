SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T13:05:13Z.
attacking: non-Lindeberg diffuse rare-fragment banks; derive the exact compound-Poisson-plus-Gaussian limit for a dense rotated {1,1,-1} frame and close the finite-stage off-tip spike loophole.

# B17 r18 — finite-intensity rare fragments cannot beat the `3 sqrt(2)` obstruction

**Status:** `NEW_SUPPORTING_SHARP-WITNESS_THEOREM`. The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The unrestricted continuity conclusion remains separate and open. Execution is `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and sources consumed

This run attacks an unpaid witness class left by the completed diffuse-Lindeberg theorem: exact-rank-three Parseval frames with maximum leverage tending to zero, but with triangular-array physical laws that fail Lindeberg because every row has probability of order `1/m` to make an order-`sqrt(m)` excursion.

The construction keeps the original-coordinate product law throughout. It does **not** use post-rotation independence, the refuted arbitrary-joint rank-three coarea estimate, a worst conditional projection-density moment, a law-uniform pointwise stationary-phase estimate, a fixed-fragment-count reduction, or a uniformly good physical minor.

The two analytic inputs actually applied are:

1. **Newest Claude/Fresnel--Brascamp--Lieb Theorem F**, source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`. For an exact three-mode Parseval physical frame with every row leverage at most `1/2`, it supplies the actual finite-form inequality
   
   `|phi_Q(t)| <= min(1,(4 pi)^(3/2)|t|^(-3/2))`                    (1.1)
   
   when the three spectral magnitudes equal one. Its `L^1` integral is exactly `24 pi`.

2. **Affine Gaussian ceiling**, account03/B17, source `yspennstate/math-open-problems@41abd73cd97a7544510aedf03cc62485b6a34b80`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T070310Z-account03-B17-QFORM-r25/REPORT.md`: if `G~N(h,Sigma)`, `Sigma >= I/12`, and `s_3(A)>=1`, then
   
   `||p_{G^T A G}||_infinity <= 3 sqrt(2)`.                         (1.2)
   
   In the exact rank-three isotropic signature `(2,1)`, every nonzero mean gives a **strictly** smaller global supremum.

The designated partner account02/B17 is used twice below. Its completed diffuse-Lindeberg report, source `yspennstate/math-open-problems@60d5d506c96acbf92025f220fc25f3d78c1d9ac6`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/account02-B17-20260923T1142Z-r11/REPORT.md`, identifies (1.1) as the finite-stage no-spike mechanism. Its newer completed teleporter theorem is source `yspennstate/math-open-problems@867fd7a538d5412db882ad21d65bd4a71e885dd0`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T125417Z-account02-B17-QFORM-auto11/`; an actual application to the same rotated frame is given in Section 8.

## 2. A cap-one finite-intensity remote-fragment law

For each bank `j=1,2,3`, fix a finite nonzero atomic measure

`nu_j = sum_{l=1}^{L_j} c_{j,l} delta_{a_{j,l}}`,                    (2.1)

where `c_{j,l}>0`, every `a_{j,l}` is nonzero, and equal atoms have already been combined. Put

`C_j=sum_l c_{j,l}`, `C=sum_j C_j`.                                  (2.2)

For all sufficiently large integers `m`, define

`L_{j,m}=1-C_j/m`                                                     (2.3)

and

`f_{j,m}(x)=1_{[-L_{j,m}/2,L_{j,m}/2]}(x)
 + sum_l 1_{[a_{j,l} sqrt(m)-c_{j,l}/(2m),
             a_{j,l} sqrt(m)+c_{j,l}/(2m)]}(x)`.                      (2.4)

For large `m` all displayed intervals are disjoint. Their total length is

`L_{j,m}+sum_l c_{j,l}/m=1`,                                         (2.5)

so (2.4) is a probability density satisfying the exact cap

`0 <= f_{j,m} <=1`.                                                   (2.6)

Let `X_{j,1}^{(m)},...,X_{j,m}^{(m)}` be iid with density (2.4), independently across the three banks, and set

`S_{j,m}=m^(-1/2) sum_{k=1}^m X_{j,k}^{(m)}`.                        (2.7)

The source support is deliberately nonlocal: its remote pieces lie at physical distance `asymp sqrt(m)`.

## 3. Exact compound-Poisson plus Gaussian bank limit

Write `sinc z=sin(z)/z`. The characteristic function of one summand after the `1/sqrt(m)` bank scaling is exactly

`psi_{j,m}(t)
 = L_{j,m} sinc(L_{j,m}t/(2sqrt(m)))
 + sum_l (c_{j,l}/m) e^{i a_{j,l}t}
       sinc(c_{j,l}t/(2m sqrt(m))).`                                  (3.1)

For every fixed `t`, Taylor expansion gives

`psi_{j,m}(t)
 =1+(1/m){-t^2/24+sum_l c_{j,l}(e^{i a_{j,l}t}-1)}+O_t(m^-2)`.        (3.2)

Consequently

`psi_{j,m}(t)^m ->
 exp(-t^2/24)
 exp(sum_l c_{j,l}(e^{i a_{j,l}t}-1)).`                              (3.3)

Thus

`S_{j,m} ==> G_j+P_j`,                                                (3.4)

where

`G_j ~ N(0,1/12)`                                                     (3.5)

and `P_j` is compound Poisson with Levy measure `nu_j`; all `G_j,P_j` can be taken independent. This is the exact finite-intensity non-Gaussian escape from the ordinary diffuse CLT.

### Genuine Lindeberg failure

This is not merely a different representation of the partner's Lindeberg class. Fix `eps>0` below half the modulus of at least one atom. The triangular-array Lindeberg cost satisfies

`sum_{k=1}^m E[(X_{j,k}^{(m)}/sqrt(m))^2
  1{|X_{j,k}^{(m)}|/sqrt(m)>eps}]
 -> sum_{l:|a_{j,l}|>eps} c_{j,l} a_{j,l}^2 >0`.                     (3.6)

Hence vector Lindeberg fails whenever at least one remote atom is present. In particular, the theorem below is not a corollary of account02/B17's preceding diffuse-Lindeberg theorem.

## 4. Exact dense rotated finite target matrices

Use the orthogonal matrix

`O=(1/7) [[ 6,-2,-3],
           [-2, 3,-6],
           [-3,-6,-2]]`,                                             (4.1)

and `J=diag(1,1,-1)`. Exact multiplication gives

`B=O^T J O
 =(1/49)[[ 31,-36,-12],
          [-36,-23,-24],
          [-12,-24, 41]]`,                                           (4.2)

with

`O^T O=I`, `B^2=I`, `spec(B)={1,1,-1}`.                              (4.3)

Every entry of `B` is nonzero.

Build a `3m x3` matrix `R_m` by repeating, for each `j=1,2,3`, the physical row

`r_{j,k}=O e_j/sqrt(m)`, `1<=k<=m`.                                  (4.4)

Then

`R_m^T R_m=I_3`,                                                     (4.5)

and

`A_m=R_m J R_m^T`                                                     (4.6)

has exact nonzero spectrum

`{1,1,-1}`                                                           (4.7)

for every finite `m`. Its `(j,k)-(j',k')` physical entry is `B_{jj'}/m`, so **every entry of `A_m` is nonzero**. This is a genuinely dense rotated target, not a diagonal control.

Moreover

`R_m^T X = O S_m`,                                                    (4.8)

and therefore the exact finite quadratic form is

`Q_m=X^T A_m X=S_m^T B S_m`.                                        (4.9)

By (3.4) and the continuous-mapping theorem,

`Q_m ==> Q_infty=(G+P)^T B(G+P)`,                                    (4.10)

where `G~N(0,I_3/12)` and `P=(P_1,P_2,P_3)` is independent of `G`.

## 5. Main theorem: the finite-intensity non-Lindeberg limit is capped by `3 sqrt(2)`

### Theorem `QFORM-DIFFUSE-COMPOUND-POISSON-GLOBAL-NOESCAPE-v1`

For the exact source-valid family above,

`||p_{Q_infty}||_infinity <=3 sqrt(2)`.                              (5.1)

If the fragment cloud is nontrivial, then in fact

`||p_{Q_infty}||_infinity <3 sqrt(2)`.                               (5.2)

Furthermore all sufficiently large finite `Q_m` have continuous densities and

`||p_{Q_m}-p_{Q_infty}||_infinity ->0`,                              (5.3)

hence

`||p_{Q_m}||_infinity -> ||p_{Q_infty}||_infinity <3 sqrt(2)`         (5.4)

for every fixed nontrivial fragment cloud.

### Proof of the limiting ceiling

Condition on `P=p`. Then `G+p~N(p,I_3/12)`. Since `B` is orthogonally conjugate to `J`, (1.2) applies directly:

`||p_{(G+p)^T B(G+p)}||_infinity <= M`, `M=3sqrt(2)`.                (5.5)

Averaging the conditional densities gives (5.1).

For strictness, let `p_0` be the centered Gaussian quadratic density. It lies in `C_0(R)`, has the unique global maximum

`p_0(0)=M`,                                                          (5.6)

and `p_0(s)<M` for every `s!=0`. The compound-Poisson vector has positive mass at zero; at least the no-jump event has probability

`w_nojump=e^{-C}>0`.                                                  (5.7)

For every nonzero `p`, the strict part of the affine-Gaussian theorem gives

`||p_{(G+p)^T B(G+p)}||_infinity <M`.                                (5.8)

Since a finite-atomic compound-Poisson vector has countable support, its density mixture is a uniformly convergent probability-weighted sum of `C_0` functions with common supremum at most `M`; hence `p_{Q_infty}` also lies in `C_0`.

At `s=0`, the positive probability of `P!=0` and (5.8) imply `p_{Q_infty}(0)<M`. At every `s!=0`, using the positive zero-mass of `P`,

`p_{Q_infty}(s)
 <=Pr(P=0)p_0(s)+(1-Pr(P=0))M<M`.                                    (5.9)

Thus `p_{Q_infty}(s)<M` pointwise. Because it is `C_0`, it attains its maximum, proving (5.2).

### Proof that no narrow finite-stage spike escapes

Every row in (4.4) has leverage exactly `1/m`; hence for `m>=2` the hypotheses of Theorem F are satisfied with the whole physical coordinate set, Gram `I_3`, and spectral product magnitude one. The newest-Claude inequality (1.1) gives the **actual finite form** bound

`|phi_{Q_m}(t)|
 <= min{1,(4pi)^(3/2)|t|^(-3/2)}.                                   (5.10)

The majorant is integrable, with integral `24pi`. Weak convergence (4.10) gives pointwise convergence of characteristic functions. Dominated convergence therefore yields

`||phi_{Q_m}-phi_{Q_infty}||_1 ->0`.                                (5.11)

Fourier inversion now gives

`||p_{Q_m}-p_{Q_infty}||_infinity
 <=(2pi)^(-1)||phi_{Q_m}-phi_{Q_infty}||_1 ->0`.                     (5.12)

This proves (5.3)-(5.4), and also gives the scoped continuity statement for every finite member and the limit. No full-target continuity claim is made.

## 6. A new source-valid lower-bound robustness statement

The same construction is near-sharp inside a class that genuinely fails Lindeberg. On the event of **no remote jump in any bank**, whose limiting probability is exactly `e^{-C}`, the limit is the centered Gaussian extremizer. Since all mixture components are nonnegative,

`p_{Q_infty}(0) >= e^{-C} 3sqrt(2)`.                                (6.1)

Together with (5.2), every nontrivial fixed finite fragment cloud satisfies

`boxed: e^{-C} 3sqrt(2)
       <= ||p_{Q_infty}||_infinity
       < 3sqrt(2).`                                                   (6.2)

For every `eta>0`, choose a fixed positive total intensity `C` so small that `e^{-C}>1-eta`. The resulting triangular array still fails Lindeberg by (3.6), yet

`lim_m ||p_{Q_m}||_infinity >= (1-eta)3sqrt(2)`.                     (6.3)

Therefore the already certified target-level obstruction

`C_univ >=3sqrt(2)`                                                   (6.4)

can be approached arbitrarily closely by **genuinely non-Lindeberg, fragmented, dense rotated exact-target sequences**. A prospective sharp proof cannot discard all non-Lindeberg near-extremizers, even in the fully diffuse leverage regime.

This does **not** prove that `3sqrt(2)` is the unrestricted sharp constant.

## 7. Why this is not covered by the latest partner teleporter theorem

The newest account02/B17 theorem (`QFORM-DIFFUSE-TELEPORTER-GLOBAL-NOESCAPE-v1`) assumes that arbitrary exceptional laws are carried by a distinguished row set whose **aggregate Gram tends to zero**. Here the rare remote event can occur on every one of the `3m` physical rows. The union of rows carrying the fragmented law has aggregate Gram exactly `I_3`, not `o(1)`. The exceptional object is probabilistic (a rare event), not a vanishing-Gram row subset. Thus Sections 2-6 pay a genuinely different non-Lindeberg mechanism.

## 8. Actual application of the newest designated-partner theorem

For comparison, apply the newest account02/B17 theorem to the **same explicit rotated frame** (4.4). In each bank make only the first row exceptional. Let fixed independent variables `Z_1,Z_2,Z_3` have bounded densities `g_j`, and set

`X_{j,1}^{(m)}=sqrt(m) Z_j`;                                         (8.1)

for all other rows use centered unit intervals. For sufficiently large `m`,

`||f_{X_{j,1}^{(m)}}||_infinity
 =m^(-1/2)||g_j||_infinity <=1`.                                    (8.2)

The exceptional-row Gram is exactly

`D_m=sum_{j=1}^3 r_{j,1}r_{j,1}^T=I_3/m ->0`,                       (8.3)

while its latent aggregate is **order one**:

`H_m=sum_j r_{j,1} X_{j,1}^{(m)}
    =sum_j Oe_j Z_j=OZ`.                                             (8.4)

Therefore the partner theorem applies at the actual inequality

`boxed: limsup_{m->infinity} ||p_{\widetilde Q_m}||_infinity
       <=3sqrt(2).`                                                   (8.5)

Thus the two complementary diffuse non-CLT stresses now have global no-escape statements on the same dense rotated spectral core: (i) a vanishing-Gram set of order-one teleporter rows, by account02/B17; and (ii) finite-intensity remote events spread across a full-Gram collection of rows, by the present theorem.

## 9. Remaining sharp-witness frontier

A source-valid witness above `3sqrt(2)`, if one exists, must now leave both of these diffuse non-Gaussian mechanisms. The clearest surviving B17 stresses are:

- exceptional structures with **nonvanishing aggregate Gram / intermediate leverage** and genuinely interacting heavy rows;
- non-tight diffuse aggregates or infinite-activity/heavy-tail triangular arrays for which no independent `N(0,I/12)` core survives in the limit;
- additional active spectrum or full-matrix tails coupled to the three strong modes;
- finite/mesoscopic structures outside the common rank-three Fresnel envelope.

These are witness constraints, not a proof of the full theorem.

## 10. Verification and review status

`CHECK.py` verifies in exact rational arithmetic `O^T O=I`, the matrix (4.2), `B^2=I`, and nonvanishing physical coefficients; it also checks the first-order characteristic-function expansion numerically at high precision and the exact identity

`integral_R min(1,(4pi)^(3/2)|t|^(-3/2)) dt=24pi`.                  (10.1)

Saved output begins `QFORM_B17_NONLINDEBERG_CP_CHECK_PASS`. The checker is a consistency check, not an independent mathematical review.

**Independent complete review:** not performed in this run. The full QFORM theorem remains open.
