SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T18:39:29Z.
attacking: convert the near-null moving-slope geometry into a genuine Borel square-root Carleson estimate before any conditional normalization, and isolate the remaining two-base hub receiver.

# account01/B05 auto15 — orthogonal moving-slope compiler and Borel-stable transverse-square currency

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound / equivalent interval bound preserving arbitrary product densities  
**Run:** `20260923T183929Z-account01-B05-QFORM-auto15`  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM / BOREL-STABLE COAREA CURRENCY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** no new full-target continuity claim; full continuity remains OPEN.

The unrestricted owner target remains OPEN. No Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation-independence, conditional-density-cap, or law-uniform pointwise van-der-Corput assumption is added.

The central correction consumed here is the current one: interval-only square-root control is not a Borel profile for arbitrary fragmented laws, and a worst conditional projection-density cap is not a valid substitute for preserving the original product source. The point of this run is to obtain an actual Borel profile directly from a product-projection density **before** the bad normalization step.

## 1. Sources actually used


The immediate B05 state is the preceding run

`yspennstate/math-open-problems@35c8dcccdfd52b14eefbdc31f81dbc56a466231d`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T172848Z-account01-B05-QFORM-auto14/REPORT.md`,

which left the punctured near-coloop loss after the Pluecker/projected-crossing aggregation.

The designated partner source actually applied is account02/B05 auto11,

`yspennstate/math-open-problems@f7b47e4c61130a654ab90c68457c8b1e1fbee73d`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T175242Z-account02-B05-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-HUB-BOREL-FROSTMAN-RECEIVER-v1` states that if a cap-one scalar `X` is independent of `(L,Y)` and the unnormalised `L=l` slices satisfy

`sup_E mu_l(E)/|E|^beta <= K`,

then for `Q=2aXL+Y`,

`||p_Q||_infinity <= ((1+beta)/beta) K^(1/(beta+1)) |a|^(-1/(beta+1))`; in particular at `beta=1/2`,

`||p_Q||_infinity <= 3 K^(2/3)|a|^(-2/3)`.                         (1.1)

The moving-slope geometry used below is the completed account02/B05 near-null report

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T160925Z-account02-B05-QFORM-d5159a85/REPORT.md`,

which proves the uniformly transverse pair `(L,W)` and, in the genuine near-null collar, the joint-density cap `||p_(L,W)||_infinity <=4/sqrt(3)`.

The product-projection input is the source-pinned Livshyts--Paouris--Pivovarov transfer in

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T115514Z-qform-B18-a01/REPORT.md`: an orthonormal `r`-dimensional projection of an original-coordinate product density with factors at most one has joint density at most `2^(r/2)`.

## 2. Heavy near-null normal form

Work in the exact-rank-three active state

`A=R M R^T`, `R^T R=I_3`, `s_min(M)>=1`.                           (2.1)

Let physical coordinate `0` be heavy, rotate only the deterministic active basis so

`r_0=sqrt(c)e_1`, `c>1/2`, `rho=1-c`,                              (2.2)

and align the transverse component of `M e_1` with `e_2`:

`M=[[eta,b,0],[b,alpha,delta],[0,delta,gamma]].`                    (2.3)

On the residual original-coordinate product bank write the longitudinal coefficient as `sqrt(rho) xi`, with `xi,v,w` orthonormal, and put

`T=xi.X`, `V=v.X`, `W=w.X`, `S=sqrt(c)X_0+sqrt(rho)T`.             (2.4)

Then

`Q=eta S^2+2bSV+alpha V^2+2delta VW+gamma W^2`.                    (2.5)

The only immediate independence is `X_0` from the complete residual original-coordinate bank. No independence is asserted among `T,V,W`.

In the genuine near-null collar

`|eta|<=1/2`,                                                       (2.6)

`||M e_1||>=1` gives

`|b|>=sqrt(3)/2`.                                                   (2.7)

A second target-specific gate from the preceding B05 algebra is also crucial. Apply `||Mz||>=||z||` to

`z=(delta,0,-b)`.

Since `Mz=(eta delta,0,-gamma b)`,

`eta^2 delta^2+gamma^2 b^2 >= delta^2+b^2`.

Thus, because `|eta|<=1` and `b!=0`,

`boxed: |gamma|>=1.`                                               (2.8)

This means a genuine transverse square remains at unit scale throughout the near-null collar; it is not the missing curvature.

## 3. Orthogonal moving-slope coordinates

Put

`kappa=sqrt(b^2+eta^2 rho)`                                        (3.1)

and define the normalized moving slope and its complementary source projection by

`L_0=(eta sqrt(rho) T+bV)/kappa`,
`P=(bT-eta sqrt(rho)V)/kappa`.                                     (3.2)

Their coefficient vectors are

`e_L=(eta sqrt(rho) xi+bv)/kappa`,
`e_P=(b xi-eta sqrt(rho)v)/kappa`.                                 (3.3)

A direct calculation gives

`<e_L,e_P>=0`, `||e_L||=||e_P||=1`, and both are orthogonal to `w`. Hence

`boxed: (L_0,P,W) is an orthonormal three-dimensional projection of the original residual product source.`   (3.4)

The inverse rotation is

`T=(eta sqrt(rho)/kappa)L_0+(b/kappa)P`,
`V=(b/kappa)L_0-(eta sqrt(rho)/kappa)P`.                            (3.5)

By the product-projection theorem, `(L_0,P,W)` therefore has a joint density `g` satisfying

`boxed: ||g||_infinity <=2 sqrt(2).`                               (3.6)

This has **no** `eta` or `rho` loss.

Expanding the physical hub first, its entire cross term is

`2 sqrt(c) X_0(eta sqrt(rho)T+bV)=2 sqrt(c) kappa X_0 L_0`.        (3.7)

Moreover the only terms containing `W` are `2delta VW+gamma W^2`. Completing that square and using (3.5) gives the exact canonical form

`boxed:
Q=c eta X_0^2+2 sqrt(c) kappa X_0 L_0
  +gamma (W-phi_eta(L_0,P))^2+F_eta(L_0,P),`                        (3.8)

where

`phi_eta(l,p)=-(delta/(gamma kappa))(b l-eta sqrt(rho)p)`          (3.9)

and

`F_eta(L_0,P)
 =eta rho T^2+2b sqrt(rho)TV+(alpha-delta^2/gamma)V^2`,            (3.10)

with `T,V` replaced by (3.5). Thus `F_eta` is an explicit quadratic polynomial in `(L_0,P)`.

Equation (3.8) is the exact near-null one-hub/two-base normal form. The hub sees only `L_0`; the transverse square has a center which sees `(L_0,P)`; and `(L_0,P,W)` retains genuine product-projection provenance.

## 4. Main theorem: Borel square-root currency survives arbitrary moving centers

### `QFORM-NEARNULL-TWOBASE-BOREL-CARLESON-v1`

Let `g` be the joint density in (3.6). For **any** measurable center `phi:R^2->R`, define, for a.e. `(l,p)`, the unnormalised square-pushforward slice

`nu_(l,p)^phi(E)
 = integral 1_{ {gamma (w-phi(l,p))^2 in E} } g(l,p,w) dw`         (4.1)

for Borel `E subset R` of finite measure. Then

`boxed:
nu_(l,p)^phi(E)
 <= (4 sqrt(2)/sqrt(|gamma|)) |E|^(1/2)
 <=4 sqrt(2)|E|^(1/2).`                                           (4.2)

Equivalently, for every Borel base set `A subset R^2`,

`boxed:
P( (L_0,P) in A,
   gamma(W-phi(L_0,P))^2 in E )
 <=4 sqrt(2) |A| |E|^(1/2).`                                      (4.3)

The theorem applies in particular to the **actual** moving center `phi_eta` from (3.9).

#### Proof

Translation in `w` does not alter one-dimensional Lebesgue measure, so it suffices to estimate the preimage of `E` under `w -> gamma w^2`. For `gamma>0`, writing `F=(E/gamma) intersect [0,infinity)`, the total preimage length is

`int_F y^(-1/2) dy`.

Because `y^(-1/2)` is decreasing, rearrangement gives

`int_F y^(-1/2)dy <= int_0^{|F|} y^(-1/2)dy=2|F|^(1/2)
                   <=2|E|^(1/2)/sqrt(gamma).`                     (4.4)

The case `gamma<0` is identical after reflection. Multiplying (4.4) by the pointwise density cap `2sqrt(2)` from (3.6) proves (4.2), and integrating over `(l,p) in A` gives (4.3). QED.

This is a genuine **Borel** estimate, not an interval estimate. Fragmented sets `E` are allowed. It therefore does not cross the live interval-to-Borel correction.

### One-base sharpening when the center sees only `L`

The partner moving-slope theorem gives for the unnormalised slope `L=kappa L_0`

`||p_(L,W)||_infinity <=2/kappa <=4/sqrt(3).`                      (4.5)

Hence for every measurable `psi:R->R`, a.e. `l`, and every Borel `E`,

`boxed:
int 1_{ {gamma(w-psi(l))^2 in E} } p_(L,W)(l,w)dw
 <=4/(kappa sqrt(|gamma|)) |E|^(1/2)
 <=8/sqrt(3) |E|^(1/2).`                                         (4.6)

This is the designated partner moving-slope result spent at an actual Borel small-set inequality, not merely at a rectangle.

## 5. What this pays, and what it does not

The earlier correction showed that a frozen **interval** square-root estimate cannot be fed into a rough-hub layer-cake argument. Equations (4.2) and (4.6) remove that issue for the actual transverse square: its Borel square-root concentration is uniformly paid before any conditional normalization.

To see the exact scope, suppose temporarily that the residual base were one-dimensional and the hub were linear, so the form had

`Z=2aXL+gamma(W-psi(L))^2+F(L)`                                   (5.1)

with `X` independent and cap one. Then (4.6) supplies the precise hypothesis of the designated partner theorem `QFORM-HUB-BOREL-FROSTMAN-RECEIVER-v1`; equation (1.1) would give directly

`||p_Z||_infinity
 <=3 [4/(kappa sqrt(|gamma|))]^(2/3)|a|^(-2/3).`                  (5.2)

This is an equation-level application of the partner theorem to the Borel currency proved here.

The actual near-null target (3.8) contains two additional features which (5.2) does not erase:

1. the physical hub has the nonzero quadratic term `c eta X_0^2`;
2. the square center and the residual quadratic depend on the second same-source base variable `P`.

Neither feature may be dropped as a small random perturbation under the owner's hypotheses.

The same point can be quantified by fixing `P=p`. Let `m(p)=p_P(p)`. The normalized conditional pair `(L_0,W)|P=p` has joint-density cap at most `2sqrt(2)/m(p)`. The homogeneous `(X_0,L_0,W)` coefficient matrix at fixed `P` has exact determinant

`boxed: det B_p=(c b^2/kappa^2) det M.`                            (5.3)

Its scalar/pair coupling coefficient is

`beta=sqrt(c) kappa`,                                               (5.4)

while the `W^2` coefficient is `gamma`. Therefore

`boxed:
|beta^2 gamma det B_p|
 =c^2 b^2 |gamma det M|
 >=3/16,`                                                          (5.5)

using `c>1/2`, `b^2>=3/4`, `|gamma|>=1`, and `|det M|>=1`.

Applying account02/B05's completed scalar/dependent-pair receiver to this **actual fixed-P target fiber** gives

`||p_(Q|P=p)||_infinity
 <=31 (2sqrt(2)/m(p))^(2/3)(3/16)^(-1/6).`                        (5.6)

Multiplying by the fiber mass yields the subprobability bound

`boxed:
||p_(Q; P in dp)/dp||_infinity
 <=62(16/3)^(1/6) m(p)^(1/3)
 <82 m(p)^(1/3).`                                                 (5.7)

This is a second direct designated-partner application. It confirms that **all fixed-base determinant currency is already uniform**. The remaining failure is the nonuniform integral of `m(p)^(1/3)` if one normalizes `P` fibers before combining them. Cap-one product laws can spread a one-dimensional projection over arbitrarily long ranges, so no universal bound on `int m^(1/3)` is available; the preceding B05 run gave an explicit Hadamard-family witness for the same phenomenon.

Thus the correct next receiver must use the two-base Borel estimate (4.2) jointly, rather than normalize or maximize over `P`.

## 6. Precise unpaid implication

The first B05 debt is now

`QFORM-QUADRATIC-HUB-TWOBASE-BOREL-CARLESON-BRIDGE-v1`:

> For the exact normal form (3.8), where `X_0` is an independent cap-one original coordinate, `(L_0,P,W)` is an orthonormal projection of the residual product source with joint density at most `2sqrt(2)`, `|gamma|>=1`, `kappa>=sqrt(3)/2`, and the unnormalised `(l,p)` square slices obey the universal Borel profile (4.2), prove a universal output interval/density bound **without** first normalizing `P` fibers and without replacing the product-projection law by an arbitrary bounded joint law.

The missing operation is now very specific. It must combine the physical-hub chirp

`c eta X_0^2+2sqrt(c)kappa X_0L_0`

with the two-base Borel-Carleson square currency **before** any `P`-fiber supremum or normalization. The current source's “hub that sees P” functional is aimed at precisely this type of source-sensitive operation.

This is strictly sharper than saying “control the moving center”: the moving square itself is already Borel-controlled uniformly in `(l,p)`. What is unpaid is the integration of that Borel currency against the second same-source base variable and the nonzero hub diagonal.

## 7. Scope and status

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- Full continuity: `OPEN`; this report does not claim it.
- New proved supporting theorem: `QFORM-NEARNULL-TWOBASE-BOREL-CARLESON-v1`, equations (4.2)-(4.3).
- New exact compiler: orthogonal moving-slope normal form (3.8), with no `eta`/`rho` loss in the residual three-dimensional projection density.
- Partner result applied at actual inequalities: the pair-density theorem gives (4.6), and the scalar/dependent-pair receiver gives the target-fiber estimate (5.6)-(5.7).
- The result does not use conditional projected-coordinate independence, interval-to-Borel transfer, pointwise quadratic-phase decay, compact support, or moments.
- Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval/write occurred, but no actual native learned-memory receiver use was verified.
- No scheduler state, email/push setting, public-release state, paid model/API/Codex call, cross-account authentication, permission, or unrelated data was changed.

A narrowly scoped manual privacy review of the two new math files found no credentials, scheduler identifiers, signed download URLs, machine paths, or unrelated private data. No installation work was performed.
