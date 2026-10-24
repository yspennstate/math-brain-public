SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T11:19:25Z.
attacking: fourth-compound two-sample disjointness product-Fourier gate and its four-row/four-column compound-hub complement.

# account03/B04 — fourth-volume disjoint-pair Fourier rearrangement

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T111925Z-account03-B04-auto11`  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Inputs actually used

Fresh owner control was read at brain commit `02e2134e540b7268895d2ffb346725d8f58d8b42`; final correction refresh used later main `e9da9e142dc86da409d1a46f50044af52f0838c1`, with `CORRECTION_INBOX.json` blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe` unchanged.

The completed analytic input is the product Brascamp--Lieb/volume theorem in
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, especially its general `D_k` calculation. I also use the already-completed arbitrary-minor-weight extension mechanism from
`yspennstate/math-open-problems@04297a630381fcfcf429b4c5ec560886bebacb39:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T052139Z-account02-B04-qform-auto11/REPORT.md`: in the determinant AM--GM step, replacing canonical minor weights by any probability weight `w` replaces `Z_k` by

`G_k(w)=exp(E_w log det(M_ST)^2 + H(w)) = Z_k exp(-D(w||nu))`.

The designated `account04/B04` partner still has no canonical current-QFORM subtree or handoff visible at the fresh repository reads, so no partner theorem is fabricated.

Corrections preserved: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint coarea; no fiber-sup shortcut; no claim that one uniformly good physical minor exists.

## 2. New theorem

Let `I,J` be disjoint sets of ORIGINAL independent coordinates. After conditioning all remaining original coordinates, write

`Q=F(X_I)+2 X_I^T M X_J+G(X_J)`,

where `F,G` are arbitrary quadratic-plus-affine functions. Define the fourth compound volume

`Z4=E4(M)=sum_{|S|=|T|=4} det(M_ST)^2`.

Assume `Z4>0`, and let

`nu(S,T)=det(M_ST)^2/Z4`

be the canonical probability law on nonzero physical `4x4` minors. Let `(S1,T1),(S2,T2)` be iid with law `nu`. Set

`delta_r=P(S1 cap S2 = emptyset)`,
`delta_c=P(T1 cap T2 = emptyset)`,
`delta=max(delta_r,delta_c)`.

### Theorem `QFORM-FOURTHVOLUME-DISJOINT-PAIR-v1`

If `delta>0`, then the law of `Q` has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= 4 sqrt(e) Z4^(-1/8) delta^(-1/16).`

The same conclusion is uniform under all outside conditioning, hence applies to the full ambient quadratic form whenever such an original-coordinate cross block is exposed.

### Proof

Suppose first `delta_r>0`. Condition the iid full-minor pair on the event

`E={S1 cap S2 = emptyset}`

and let `mu` be the resulting symmetric joint law. Let `w` be either full-minor marginal under `mu`.
For every physical row `i`, disjointness gives

`1_{i in S1}+1_{i in S2} <=1`.

By symmetry of `mu`,

`alpha_i:=P_w(i in S)<=1/2`.                                           (2.1)

Moreover

`D(mu || nu x nu)=log(1/delta_r)`.

Writing the KL divergence relative to `nu x nu` as marginal divergences plus mutual information,

`D(mu || nu x nu)=D(w||nu)+D(w||nu)+I_mu((S1,T1);(S2,T2))`

and therefore

`D(w||nu)<= (1/2) log(1/delta_r)`.                                   (2.2)

Hence the entropy-adjusted determinant currency satisfies

`G4(w)=Z4 exp(-D(w||nu)) >= Z4 delta_r^(1/2)`.                         (2.3)

Now apply the completed `k=4,q=1` product Brascamp--Lieb estimate with the arbitrary weight `w`. Equation (2.1) is exactly the Hausdorff--Young admissibility gate. The determinant expansion and weighted AM--GM give

`E F_t <= e^2 (2pi/|t|)^4 G4(w)^(-1/2)`

for the decoupled product, so

`|phi_Q(t)| <= min{1, 4 pi^2 e G4(w)^(-1/4) |t|^(-2)}`.               (2.4)

For `B>0`,

`integral_R min(1,B |t|^-2) dt = 4 sqrt(B)`.

Fourier inversion thus yields

`||p_Q||_infinity <= 4 sqrt(e) G4(w)^(-1/8)`

and (2.3) gives

`||p_Q||_infinity <= 4 sqrt(e) Z4^(-1/8) delta_r^(-1/16)`.

Since the characteristic function is integrable, the density is continuous and in `C_0`.
If instead `delta_c>0`, swap the two original-coordinate banks; the quadratic form and determinant data are unchanged and the same proof applies. This proves the theorem. QED.

## 3. Quantitative failure side: a four-by-four compound hub

Fix `0<tau<1`. If `delta_r<tau`, then

`delta_r=E_{S~nu_r}[ nu_r({S':S' cap S=emptyset}) ]`.

Hence some physical four-row set `S0` in the support satisfies

`P_nu(S cap S0 = emptyset) <= delta_r < tau`,

so at least `1-tau` of canonical fourth-volume mass has row set meeting `S0`. Likewise, if `delta_c<tau`, some physical four-column set `T0` meets at least `1-tau` of the column mass. By a union bound on the full minor law,

`P_nu(S cap S0 != emptyset AND T cap T0 != emptyset) >= 1-2tau`.       (3.1)

Thus every fourth-volume packet has the explicit dichotomy:

* either `delta>=tau`, and
  `||p_Q||_infinity <= 4 sqrt(e) tau^(-1/16) Z4^(-1/8)`;
* or its fourth compound volume is concentrated, up to mass `2tau`, on minors simultaneously hitting one fixed physical four-row set and one fixed physical four-column set.

This is an order-4 analogue of the earlier third-volume compound-hub reduction, but the proof is different: pair-disjoint conditioning supplies the `1/2` marginal gate exactly, and failure directly exhibits a four-coordinate hitting set. It does not solve the resulting low-rank/rank-three survivor.

## 4. Explicit genuinely rotated indefinite target

Let `H` be the `4x4` Sylvester Hadamard matrix divided by `2`, hence orthogonal. Define an `8x4` matrix `R` by the rows

`sqrt(9/10)e1, sqrt(1/10)e1,
 (1/sqrt2)e2,(1/sqrt2)e2,
 (1/sqrt2)e3,(1/sqrt2)e3,
 (1/sqrt20)e4,(1/sqrt20)e4`,

and put

`M=R H`.

All 32 physical entries of `M` are nonzero. Its singular values are exactly

`1,1,1,1/sqrt(10)`.

For the symmetric quadratic-form matrix

`A=[[0,M],[M^T,0]]`

we therefore have

`spec(A)={+/-1,+/-1,+/-1,+/-1/sqrt(10),0,0,0,0}`,

so `A` is indefinite and has six eigenvalues of absolute value at least one.

The canonical third-volume law has

`E3(M)=13/10`

and its first physical row marginal is exactly

`(9/10)*(12/13)=54/65=0.830769...>3/4`.

Thus the unmodified third-volume `D'` marginal gate fails on this matrix.

For fourth volume,

`E4(M)=1/10`.

There are exactly 16 nonzero `4x4` row minors, one row chosen from each duplicated axis pair. For two iid canonical fourth-minor row sets,

`delta_r=[2*(9/10)*(1/10)]*(1/2)^3=9/400`.

Conditioning on disjointness makes each member of each pair equiprobable, so all eight conditioned row marginals equal `1/2`. The exact entropy-adjusted determinant currency is

`G4=(2 sqrt((9/10)(1/10))) * 1 * 1 * (2*(1/20)) = 3/50`.

Consequently the sharper weighted form of the theorem gives, for every admissible cap-one product input law,

`boxed: ||p_{X^T A X}||_infinity <= 4 sqrt(e) (50/3)^(1/8)
       = 9.374288735030278... .`

The generic `delta` corollary alone would give `11.147970861787865...`. The output density is continuous and vanishes at infinity. No independence is asserted after multiplying coefficient matrices by `H`; `H` is part of the fixed physical matrix.

Finite arithmetic, spectrum, marginals, `delta_r`, `G4`, and constants are recorded in `CHECKS.json` in this run directory.

## 5. What this changes and what remains

This supplies a new product-Fourier exit for rank-four-and-higher cross packets whose natural third-volume law can be too concentrated. It also gives an immediate structural compression when the Fourier exit fails: almost all fourth-compound mass is trapped by fixed four-row/four-column physical hubs.

It does **not** prove the bare three-large-eigenvalue conjecture, because a hard survivor may have negligible or zero fourth compound volume (in particular an exact rank-three cross packet). The next B04 implication is therefore:

`QFORM-E4-HUB-OR-RANK3-ROUTING-v1` — combine the four-by-four compound-hub residue with the existing third-volume/ridge/star endpoints, or show that small `E4` quantitatively forces a rank-three tube to which one of the paid rank-three mechanisms applies without a vanishing local reciprocal.

Continuity is proved in the theorem above; full-target continuity remains open together with the full target itself.
