SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-24T02:28:56Z.
attacking: the fixed-positive-E2 / curvature-flip frontier by normalization, full-cut re-entry, and orthogonal low-action peeling of the finite-rank carrier.

# fleet02/B20 — active-localized carrier extraction from the fixed-E2 / curvature-flip frontier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper / SYNTHESIS  
Run: `20260924T022856Z-fleet02-B20-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / ACTIVE-LOCALIZED-CARRIER / CURVATURE-FLIP-TRANSVERSE-E2 / FULL-QFORM-OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains separate and OPEN.

## 1. Fresh source boundary

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no fleet02/B20 stop, pause, or reassignment observed before publication. The live correction inbox was reread. In particular this report does not use law-uniform pointwise quadratic-phase decay, a worst-fibre density cap, an arbitrary-joint coarea shortcut, independence after a spectral/SVD rotation, a one-good-minor inference from aggregate energy, or deletion of a nonzero coefficient tail.

The newest compatible completed designated partner remained fleet03/B20 r44:

- `yspennstate/math-open-problems@d579d083dcdd2d2a7757632dabbe94ec15adfa40`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T014735Z-fleet03-B20-QFORM-r44/REPORT.md`.

Its exact aligned-collar scale is

`eps_r44=(9*2^-18)^(1/4)=sqrt(6)/32=0.07654655446197431...`,

and in its finite-carrier branch the skeleton obeys `rank(S)<=9`, `s3(S)>=1/4`. The preceding B20 closure, using these exact r44 expressions, proved a literal full-cut floor

`c0=((sqrt(766)-4sqrt(3))^2)/16384
   =0.026275654659752182...`                                      (1.1)

and reduced every unpaid r44 finite-carrier/strong packet to either a paid D5/rank-three exit, a fixed-positive E2 packet, or a finite curvature-flip packet. The E2 floor is

`z0=(1/4096)[(63/64)c0-3/4096]
   =6.135907148606825e-6.`                                        (1.2)

At the curvature flip there is a physical partition `P sqcup Q sqcup R=[n]` with

`||A[P,Q]||_F^2>961/4096`,                                       (1.3)
`||A[P,R]||_op>0.1120996781`,                                    (1.4)

and the `P|Q` block remains strong-top-four and in the absolute rank-one tube `s2<1/64`.

The fresh integrated-Fourier source used below is fleet01/B02 r43:

- `yspennstate/math-open-problems@041bd053495db9b7e7c12d994501de10c059c459`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T022016Z-fleet01-B02-qform-auto11-r43/REPORT.md`.

It first completes every partial physical block with `E2>4/9` to a full original-coordinate cut. Apart from an already-tracked giant near-rank-one branch and paid E3/coordinate-core branches, its ultra-rank-two survivor has an exact decomposition

`A=D+R+E`,                                                        (1.5)

where `D` is diagonal with `||D||op<1/8`, `rank(R)<=42`,

`s3(R)>gamma0:=0.8749992111292801...`,                            (1.6)
`||E||F<eta0:=7.888707199262311e-7.`                              (1.7)

The earlier fleet01/B02 r38 finite-rank carrier theorem says that for any exact original-coordinate decomposition `A=D+R+E` with `rank(R)=r>=3`, `s3(R)>=gamma`, and `||E||F<=eta`, either a literal physical E3 cut pays the law whenever

`sigma=(sqrt(3)/8)gamma-eta>0`,                                  (1.8)

or there is a unit carrier vector localized by more than half its squared mass on at most `16r^2` original coordinates.

## 2. New theorem: orthogonal low-action peeling

The localization certificate by itself does not say that the localized carrier direction actually carries a quantitatively nontrivial coefficient action. The following converts it into such a certificate, or pays the law first.

### Theorem 2.1 — `QFORM-FINITELOCALIZED-ACTIVE-DIRECTION-PEEL-v1`

Assume (1.5)-(1.7). Then either the full ambient quadratic law is paid by a completed physical-E3 Fourier branch with

`||p_Q||_infinity < 479.633`                                     (2.1)

(and a continuous `C_0` density there), or there is another exact decomposition

`A=D+R_*+E_*`                                                     (2.2)

with

`3<=rank(R_*)<=42`,                                               (2.3)
`s3(R_*)>0.7370029475929075`,                                    (2.4)
`||E_*||F<0.13799705240709254`,                                  (2.5)

and an exact nonzero carrier factorization

`R_*=V K V^T`, `V^T V=I`,                                        (2.6)

for which there are a unit `u` and a physical coordinate set `H` satisfying

`|H|<=16 rank(R_*)^2<=28224`,                                    (2.7)
`||(Vu)_H||_2^2>1/2`,                                            (2.8)
`||Ku||_2>=1/64`.                                                 (2.9)

Every coefficient peeled below remains exactly in `E_*`; it is not deleted from the random quadratic form.

### Proof

Start with a fixed isometric carrier factorization `R=V0 K0 V0^T`. At a current stage, represent the retained carrier as

`R_j=V0 K_j V0^T`,                                                (2.10)

where `K_j` is symmetric and supported on a subspace `W_j` of the original carrier space. Factor only its nonzero support when invoking the r38 theorem. If r38 gives its diffuse alternative, (1.8) pays the full law. Otherwise it gives a unit vector `u_j` in the nonzero support whose physical carrier image has more than half its mass on a set of at most `16 r_j^2` original coordinates.

Fix

`a:=1/64`.                                                        (2.11)

If `||K_j u_j||>=a`, stop: this is (2.9). Otherwise project out `u_j`. With `P_j` the orthogonal projection in `W_j` onto `u_j^perp`, put

`K_{j+1}=P_j K_j P_j`,
`R_{j+1}=V0 K_{j+1} V0^T`,
`F_j=R_j-R_{j+1}`.                                                (2.12)

This is an exact coefficient operation; define the new retained tail by adding `F_j` to the old tail.

In the orthogonal splitting `W_j=span(u_j) direct_sum W_{j+1}`, write

`K_j u_j = alpha_j u_j + b_j`, `b_j in W_{j+1}`.                 (2.13)

Then the coefficient increment has block form

`K_j-K_{j+1}=[[alpha_j,b_j^T],[b_j,0]]`,                          (2.14)

so

`||F_j||_F^2=alpha_j^2+2||b_j||^2
            <=2||K_j u_j||^2
            <2a^2.`                                               (2.15)

The crucial improvement over a triangle-inequality accumulation is that these successive increments are Frobenius-orthogonal. For `i<j`, `K_i-K_{i+1}` has zero block on `W_{i+1} x W_{i+1}`, whereas every later increment is supported entirely inside that block. Hence

`<F_i,F_j>_F=0`.                                                  (2.16)

After `m` low-action peels,

`||sum_{j<m}F_j||_F^2=sum_{j<m}||F_j||_F^2<2ma^2`,                (2.17)

and therefore the exact decomposition at that stage satisfies

`||E_m||F < eta0 + sqrt(2m)/64`,                                 (2.18)
`s3(R_m) > gamma0 - sqrt(2m)/64`                                 (2.19)

by the singular-value perturbation inequality.

The rank drops by at least one at every peel (any new kernel only accelerates the drop). Starting at rank at most 42, there can be at most 39 low-action peels before reaching rank three. A further low-action peel at rank three would produce rank at most two, contradicting (2.19), which remains strictly positive even after one additional peel. Thus either a diffuse exit occurs or an active localized direction occurs by the rank-three stage.

For every `m<=39`, the r38 diffuse parameter is bounded below by

`sigma_m
 >= (sqrt(3)/8)(gamma0-sqrt(2m)/64)
    -(eta0+sqrt(2m)/64)
 >= sigma_*`,                                                     (2.20)

where

`sigma_*=0.021568766412774748...>0`.                              (2.21)

Using the completed current physical-E3 constant `C3=10.3450832321475...`,

`||p_Q||_infinity <= C3/sigma_* =479.6325869624...<479.633`,      (2.22)

and

`integral_R |phi_Q(t)|dt <=2pi C3/sigma_*
                         <3013.621.`                              (2.23)

At `m=39`, (2.18)-(2.19) give exactly (2.4)-(2.5). QED.

### Independent review A: support/rank bookkeeping

If a compression `P_jK_jP_j` acquires an additional kernel, factor its actual nonzero support before the next r38 invocation. The next localized coefficient vector embeds back into `W_{j+1}`, so the nested-support orthogonality (2.16) is unchanged. Because `V0` is an isometry, Frobenius norms of coefficient-space increments and physical matrices agree.

### Independent review B: no hidden probabilistic perturbation

At every stage

`A=D+R_m+[E_0+(R_0-R_m)]`                                        (2.24)

is an exact matrix identity. The accumulated term is used only in deterministic Frobenius and Weyl estimates. No statement treats its random quadratic contribution as negligible, and no projected/rotated random coordinates are declared independent.

## 3. Fixed-positive E2 is no longer a generic frontier category

The preceding B20 theorem only supplied the small but universal floor `e2(M^TM)>z0`. Normalize the **entire** coefficient matrix by the fixed scalar

`Lambda := ((4/9)/z0)^(1/4)
         =16.405318852237478... .`                                (3.1)

Then the same literal physical block in `A'=Lambda A` satisfies

`e2((Lambda M)^T(Lambda M))>4/9`.                                (3.2)

The source law is unchanged, and `A'` still satisfies the target spectral hypothesis. Hence fleet01/B02 r43 applies to `Q'=Lambda Q`. If one of its paid branches fires, scaling the output back gives a universal bound for `Q` (the largest displayed paid constant from its initial E3 gate is `<43446.895`). If its giant near-rank-one branch fires, the state re-enters the already-tracked giant-R1/exterior-third-mode collar. If its ultra-rank-two branch reaches the finite-rank localization endpoint, Theorem 2.1 either pays it or yields, after dividing (2.2) by `Lambda`, an original-scale exact certificate

`A=D_hat+R_hat+E_hat`,                                            (3.3)

with

`rank(R_hat)<=42`,
`s3(R_hat)>0.04492463415256264`,                                  (3.4)
`||E_hat||F<0.008411726321812482`,                                (3.5)

and a carrier factorization `R_hat=V K_hat V^T` having

`||(Vu)_H||^2>1/2`, `|H|<=28224`,
`||K_hat u||>=1/(64 Lambda)
              =0.0009524350084709843... .`                        (3.6)

Thus the old phrase “fixed-positive E2 packet” can be replaced by two explicit existing/new descendants: a giant near-rank-one collar or a finite **active localized carrier**. Scaling is global, so it does not alter independence or erase any same-bank term.

## 4. Curvature flip: transverse arm either creates E2 or aligns to one hub line

Return to the curvature-flip packet (1.3)-(1.4). Let

`M=A[P,Q]`, `H=A[P,R]`,

and let `u_1` be the top left singular vector of `M`, with `Pi=u_1u_1^T`. Because the `P|Q` block is strong-top-four and `s2(M)<1/64`, writing `x_j=s_j(M)^2` gives

`x1 > (63/64)(961/4096)-3/4096
    =60351/262144
    =0.23022079467773438... .`                                    (4.1)

Consider the literal augmented physical cross block

`B=A[P,Q union R]=[M H]`.                                        (4.2)

Cauchy-Binet after a deterministic right SVD of `M` (coefficient geometry only) gives the positive exterior-volume sub-sum

`e2(BB^T) >= x1 ||(I-Pi)H||_F^2.`                                (4.3)

Indeed the selected two-column minors pair the top singular column `s1 u1` with each actual `H` column, and their squared areas sum to the right-hand side.

Define

`delta_*:=sqrt(z0/(60351/262144))
        =0.005162583810831281... .`                               (4.4)

If

`||(I-Pi)H||F >= delta_*`,                                       (4.5)

then (4.3) gives `e2(BB^T)>z0`, so Section 3 routes the curvature flip into the normalized E2 compiler.

Otherwise

`||(I-Pi)H||F<delta_*`,                                          (4.6)

and the physical arm remains quantitatively nontrivial along the same coefficient hub line:

`||Pi H||op
 >=||H||op-||(I-Pi)H||op
 >0.1120996781-delta_*
 >0.1069370942891687.`                                           (4.7)

### Theorem 4.1 — `QFORM-R44-CURVATUREFLIP-E2-OR-COMMONHUB-v1`

Every r44 curvature-flip survivor is either routed to the fixed-positive E2 compiler of Section 3 by a literal original-coordinate augmented cut, or it has a literal physical arm `A[P,R]` within Frobenius distance `<0.005163` of the top left singular line of `A[P,Q]`, while retaining aligned operator norm `>0.106937`. The actual transverse coefficient tail remains present in the law.

This changes the mechanism after repeated rank-one reproduction: the final flip cannot be treated as an arbitrary second arm. Unless E2 already appears, both arms are forced into one common physical coefficient hub line.

## 5. Required pinned interactive source applied at an actual live inequality

The owner-pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its unrestricted D5 theorem says for every literal physical cross block `N`, with arbitrary same-bank curvature and outside couplings retained,

`||p_Q||infinity <=5sqrt(2e) e5(N^T N)^(-1/10).`                 (5.1)

Apply this to the actual full cut already supplied by the r44/B20 compiler (or to any full-cut completion in Section 3). Whenever

`e5(N^T N)>=1/1024`,                                             (5.2)

one has the concrete full-law bound

`boxed: ||p_Q||infinity <=10sqrt(2e)<23.317.`                    (5.3)

Thus every still-unpaid descendant discussed here may additionally assume the corresponding literal live cut has `e5<1/1024`; this is not a statement about a rotated block.

## 6. Strongest current conditional proof graph

Combining the newest designated partner r44, the preceding B20 full-cut re-entry theorem, the fresh fleet01/B02 full-cut completion, and Theorems 2.1 and 4.1 gives the following source-preserving global splice inside the all-small-diagonal chamber:

1. r44's finite carrier / strong physical packets produce the exact full-cut floor (1.1); diffuse fifth-volume and third-singular-direction states are already paid.
2. A surviving fixed-positive E2 packet `e2>z0` is globally normalized by the fixed scalar `Lambda`; it is then either paid, enters the already-tracked giant near-rank-one collar, or collapses to the active localized certificate (3.3)-(3.6).
3. A rank-one-reproduction chain that reaches the curvature flip is either transverse enough to create the same fixed E2 packet by (4.3), or collapses to the explicit common-hub line collar (4.6)-(4.7).
4. The newer exact-rank-one physical-pair theorem of fleet02/B09 separately removes the old arbitrary-leaf-curvature obstruction at an exact nonzero rank-one pair whenever its kernel-star is nonzero; it does not justify perturbing through a merely near-rank-one pair.

The first source-complete unpaid implication is therefore narrowed to

`QFORM-ACTIVELOCALIZED-OR-COMMONHUB/GIANTR1-PAYMENT-v1`:

> Under the original independent cap-one product hypotheses and the target `s3(A)>=1`, after the completed scalar/principal/E3/D5/grouped-rank-three exits, prove a universal density bound for either (i) the active finite-localized carrier certificate (3.3)-(3.6), (ii) the common-hub curvature-flip collar (4.6)-(4.7), or (iii) the already-tracked giant near-rank-one/exterior-third-mode collar, while retaining every same-bank quadratic block, every nonzero coefficient tail, all outside couplings, signs, affine terms, fragmented/unbounded source laws, and arbitrary extra spectrum.

A productive next move is to use the active lower action `||K_hat u||>=0.0009524` together with `>1/2` physical mass on at most 28224 coordinates to force a literal physical star/pair packet, while using the common-hub collar as its complementary source-preserving endpoint. A worst-slice half-Riesz argument is not valid in the merely near-rank-one case.

No full proof or full-target counterexample is claimed. The bounded-density conjecture remains OPEN; unrestricted continuity remains separately OPEN.
