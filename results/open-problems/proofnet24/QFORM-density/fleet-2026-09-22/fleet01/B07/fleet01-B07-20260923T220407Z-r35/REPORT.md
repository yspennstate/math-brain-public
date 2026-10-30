SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T22:04:07Z.
attacking: the principal-overlap/core survivor after determinant-weighted coordinate selection; prove that a macroscopic physical principal 3x3 determinant is payable from its determinant alone, then split the support-diffuse principal packet into disjoint-role diagonal/edge/triangle currencies.

# fleet01/B07 r35 — determinant-only physical triple payment and principal-E3 diffuse currency compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `fleet01-B07-20260923T220407Z-r35`  
Fresh brain main before publication: `yspennstate/math-research-brain@18f446e214be7ab49bb6d4ea3ab131182daf3264`  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: **NEW DETERMINANT-ONLY PHYSICAL-TRIPLE RECEIVER + PRINCIPAL-CORE BRANCH PAID + NEW SUPPORT-DIFFUSE H3 TRI-COLOR COMPILER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

All coordinate sets below are ORIGINAL physical coordinates. No random variable is rotated. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is introduced. No small nonzero coefficient tail is deleted. The corrected pointwise van-der-Corput shortcut and the corrected one-good-minor shortcut are not used.

## 1. Source-pinned inputs

### 1.1 Existing full-third-compound role selection

Own earlier theorem `QFORM-COARSE-ROLE-COLORING-v1` is source-pinned at

`yspennstate/math-open-problems@b08aeb182c7e4448b960e93db1953cb06cbccb9f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T070624Z-r19/REPORT.md`.

For a target-admissible symmetric `A`,

`sum_{h=0}^3 W_h(A)=e_3(A^2)>=1`,

where `W_h` is the total squared `3x3`-minor mass with row/column overlap `h`. Hence some `W_h>=1/4`. In particular the principal branch is

`W_3=sum_{|I|=3} det A[I,I]^2 >=1/4`.                         (1.1)

The same source proves the determinant-marginal core/diffuse split after applying the designated fleet02/B07 theorem below.

### 1.2 Designated partner fleet02/B07: determinant-marginal core theorem

Completed source:

`yspennstate/math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T023322Z-r11/REPORT.md`, theorem `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1`.

If a determinant-square packet of mass `P` has row/column inclusion tails `delta_R,delta_C` outside physical supports `R0,C0`, then the packet mass wholly inside `R0 x C0` is at least

`(1-delta_R-delta_C)P`.                                          (1.2)

I apply (1.2) to an actual principal determinant law in Section 4.

### 1.3 Fixed physical triple and indefinite-pair analytic receivers

The physical-triple scalar-Schur theorem is in

`yspennstate/math-open-problems@96b7296e7bb30bdddb70522eda0177190e316bc4`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T184724Z-fleet03-B20-QFORM-r15/REPORT.md`, theorem `QFORM-PHYSICAL-TRIPLE-DETERMINANT-PAYMENT-v1`:

if a physical principal `3x3` block `B` has `det B !=0` and one physical diagonal entry `a!=0`, then

`||p_Q||_infinity <=128 (|a det B|)^(-1/4)`.                    (1.3)

Its full-matrix physical indefinite-pair input is source-pinned at

`yspennstate/math-open-problems@058acb5c8f9186ef199bbaf136b57f4dd9ea3800`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`:

for an invertible indefinite physical pair with `D=|det P|`, `kappa=sigma_min(P)`, and full-matrix `s_3(A)>=s`,

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`.         (1.4)

Both statements retain arbitrary outside couplings/affine terms after conditioning on ORIGINAL coordinates.

### 1.4 Latest completed designated partner at the source refresh

The newest completed fleet02/B07 report visible before publication is

`yspennstate/math-open-problems@b2d2cccb46aa3fc83162b2cc4fba61a5e040ebd2`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T211034Z-fleet02-B07-qform-mixedvolume/REPORT.md`.

Its theorem `QFORM-E2-AGGREGATE-TRANSVERSE-TO-PHYSICAL-E3-v1` gives, in its actual live carrier,

`e_3(MM^T) >= (Z/144) sum_i q_i^2`.                              (1.5)

At `Z>Z0 h^4`, `Z0=854675.100194511`, `h=(2sqrt(2)-1)/1572864`, and `sqrt(sum q_i^2)>=h/1024`, it gives

`e_3(MM^T)>0.0056602895272739135 h^6`                            (1.6)

and hence, by the completed marginal-free physical cross-E3 receiver,

`||p_Q||_infinity<24.991153492 h^(-1)<2.150e7`,                  (1.7)

with a continuous `C_0` density. This is an equation-level application of the current designated partner result, not a citation-only dependency.

## 2. First attempted implication and mechanism change

The r34 fallback had produced a coefficient decomposition `A=R+T` with `rank R<=72` and an extremely small but nonzero operator tail. A tempting coordinate-selection step would be to force a uniformly conditioned bounded-cardinality physical principal core from the bounded rank.

That implication is false even with `T=0`: a flat rank-three projection has rank three and three unit eigenvalues while every fixed-cardinality physical principal block tends to zero as the ambient dimension grows. This obstruction is already source-visible in the fleet and therefore I do not duplicate that failed mechanism.

Instead this run returns to the *complete determinant law*. The first missing principal-overlap implication is attacked directly: once determinant-weighted concentration has produced a genuinely macroscopic physical principal determinant, can it be paid without separately lower-bounding a scalar pivot? The answer is yes.

## 3. Main theorem: determinant alone pays a macroscopic physical principal triple

### Theorem 3.1 — `QFORM-PHYSICAL3-DETERMINANT-ONLY-v1`

Let `A` be a real symmetric target-admissible matrix, so `s_3(A)>=1`. Suppose an ORIGINAL-coordinate principal triple `I` has

`B=A[I,I]`,
`|det B|>=d`,                                                     (3.1)

where `0<d<=1`. Then the full ambient quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity <=128 sqrt(2) d^(-1/3).
`                                                                    (3.2)

No lower bound on any individual diagonal of `B` is assumed.

#### Proof

Put

`r=d^(1/3)/2`,
`eta=r/2=d^(1/3)/4`.                                              (3.3)

Write, after relabeling the three physical coordinates,

`B=[[a,x,y],[x,b,z],[y,z,c]]`.

There are two exhaustive cases.

### Case A: a physical diagonal is at least `eta`

If

`max(|a|,|b|,|c|)>=eta`,                                         (3.4)

use that coordinate in the completed physical-triple theorem (1.3). Since `|det B|>=d`,

`||p_Q||_infinity
 <=128 (eta d)^(-1/4)
 =128 sqrt(2) d^(-1/3)`.                                         (3.5)

### Case B: all three physical diagonals are smaller than `eta`

Assume

`|a|,|b|,|c|<eta`.                                               (3.6)

If also

`|x|,|y|,|z|<r`,                                                  (3.7)

then the exact determinant identity

`det B=abc+2xyz-a z^2-b y^2-c x^2`                               (3.8)

gives

`|det B|
 < eta^3+2r^3+3 eta r^2
 = (1/8+2+3/2)r^3
 = (29/8)r^3
 =29d/64
 <d`,                                                            (3.9)

contradicting (3.1). Therefore at least one physical edge, say `x`, obeys

`|x|>=r`.                                                         (3.10)

Consider the actual physical principal pair

`P=[[a,x],[x,b]]`.

The zero-diagonal reference `[[0,x],[x,0]]` has eigenvalues `+|x|,-|x|`, while the diagonal perturbation has operator norm below `eta`. Weyl therefore gives one eigenvalue of `P` at least

`|x|-eta >= r-eta=eta`,

and the other at most `-eta`. Thus `P` is quantitatively indefinite and

`kappa=sigma_min(P)>=eta`,
`D=|det P|>=eta^2`.                                                (3.11)

Apply the completed full-matrix indefinite-pair theorem (1.4) with the actual target scale `s=1`:

`||p_Q||_infinity
 <=3*400^(1/3) (eta^5)^(-1/6)
 =3*400^(1/3)*1024^(1/6) d^(-5/18).`                              (3.12)

Since `400^(1/3)<8`, `1024^(1/6)=2^(5/3)<4`, and `0<d<=1`,

`(3.12)<96 d^(-5/18)
       <=96 d^(-1/3)
       <128 sqrt(2)d^(-1/3)`.                                    (3.13)

This proves (3.2). QED.

### Remarks

1. This does **not** claim that the bare spectral hypothesis supplies one such determinant. The theorem is a receiver after determinant-weighted coordinate selection has already produced a macroscopic physical triple.
2. The proof never reciprocates a tiny scalar pivot: if all scalar pivots are small, the determinant identity forces a macroscopic physical edge, and that edge creates a quantitatively indefinite physical pair.
3. I claim essential boundedness only. The two input receivers used above do not jointly supply a continuity theorem at this scope.

## 4. Designated-partner application: the concentrated principal-E3 branch is now paid

Assume the active coarse overlap class is `h=3`, so by (1.1)

`P3=W_3>=1/4`.                                                    (4.1)

Normalize the principal determinant weights

`w(I)=det A[I,I]^2/P3`, `|I|=3`,

and let

`alpha_i=P_w(i in I)`, so `sum_i alpha_i=3`.                     (4.2)

Take the heavy physical set

`H={i:alpha_i>3/5}`.                                              (4.3)

Then `|H|<=4`. Put

`delta=sum_(i notin H) alpha_i`.                                 (4.4)

Because this is a principal packet, its row and column determinant laws are the same. Apply the completed **fleet02/B07** marginal-tail theorem (1.2) with `R0=C0=H`; when

`delta<=1/4`,                                                     (4.5)

it gives retained principal packet mass at least

`(1-2delta)P3 >=P3/2 >=1/8`.                                    (4.6)

There are at most `binom(4,3)=4` physical principal triples inside `H`. Hence one actual original-coordinate triple `I_*` satisfies

`boxed:
 |det A[I_*,I_*]|^2 >=1/32,
}`                                                                    (4.7)

so

`|det A[I_*,I_*]|>=d0:=1/sqrt(32)`.                              (4.8)

This selected determinant is not a tiny representative: it is produced only after the determinant law puts at least half of the entire active principal packet on at most four physical coordinates.

Apply Theorem 3.1 with `d=d0`. Since

`d0^(-1/3)=32^(1/6)`,

we obtain the universal full-form estimate

`boxed:
 ||p_Q||_infinity
 <=128 sqrt(2) 32^(1/6)
 =128*2^(4/3)
 =322.539788773... .
}`                                                                    (4.9)

Thus the **support-concentrated principal-overlap branch is fully paid** at the essential-supremum level. This is a genuine completed designated-partner application: fleet02/B07 converts determinant marginals to a macroscopic physical triple, and the new theorem spends that triple without a separate pivot-size assumption.

Consequently every unpaid active `h=3` packet must satisfy

`boxed: delta>1/4.`                                               (4.10)

That is a true support-diffuse principal-determinant law.

## 5. New compiler for the support-diffuse principal packet

The concentrated branch is no longer the issue. The remaining principal packet should be converted to currencies on disjoint original-coordinate roles before any local inversion.

Randomly color every physical coordinate independently with one of three labels `U,V,W`, each with probability `1/3`. A fixed principal triple is rainbow with probability

`6/3^3=2/9`.                                                      (5.1)

Hence there are pairwise disjoint physical banks `U,V,W` for which

`P_rain
 :=sum_(i in U,j in V,k in W) det A[{i,j,k},{i,j,k}]^2
 >=(2/9)P3
 >=1/18`.                                                        (5.2)

For one such triple put

`a=A_ii`, `b=A_jj`, `c=A_kk`,
`x=A_ij`, `y=A_jk`, `z=A_ki`.

Then

`det A[{i,j,k},{i,j,k}]
 =abc+2xyz-a y^2-b z^2-c x^2`.                                  (5.3)

Define the disjoint-role aggregate currencies

`D_U=sum_(i in U) A_ii^2`, and cyclically `D_V,D_W`,              (5.4)

`F_UV=sum_(i in U,j in V) A_ij^4`, and cyclically,               (5.5)

`T_triangle=sum_(i in U,j in V,k in W)
 A_ij^2 A_jk^2 A_ki^2`.                                          (5.6)

By Cauchy--Schwarz on the five summands of (5.3),

`det^2
 <=5[(abc)^2+4(xyz)^2+(a y^2)^2+(b z^2)^2+(c x^2)^2]`.         (5.7)

Summing over the three disjoint banks factorizes four of the five terms exactly and gives

`boxed:
 P_rain
 <=5[ D_U D_V D_W
      +4 T_triangle
      +D_U F_VW
      +D_V F_WU
      +D_W F_UV ].
}`                                                                    (5.8)

Therefore:

### Theorem 5.1 — `QFORM-H3-RAINBOW-DIAG-EDGE-TRIANGLE-COMPILER-v1`

On every active principal-overlap branch, one of the following original-coordinate aggregate currencies is forced:

`boxed: D_U D_V D_W >=1/450,`                                    (5.9)

or

`boxed: T_triangle >=1/1800,`                                    (5.10)

or, cyclically,

`boxed: D_U F_VW >=1/450.`                                       (5.11)

No individual diagonal, edge, or triangle is selected in (5.9)--(5.11).

### Support-diffuse refinement

Under the genuinely unpaid condition (4.10), the principal determinant law puts more than `P3/12>=1/48` determinant-square mass on triples using at least one coordinate outside the heavy set `H`: indeed `delta=E|I\H|>1/4` and `|I\H|<=3` imply `P(I not subset H)>1/12`.

Apply the same random three-coloring only to that light-using subpacket. Some rainbow light-using packet has mass

`P_rain,light > (2/9)(1/48)=1/216`.                              (5.12)

Repeating (5.8) with only those nonnegative summands gives a light-supported version of the compiler: one of the corresponding five disjoint-role currencies is at least `1/5400`, with the triangle currency itself at least `1/21600` when the `4T` term wins. This preserves explicit support-diffuse provenance for the next receiver rather than erasing it by choosing the largest minor.

## 6. Interaction with the latest fleet02/B07 carrier

The newest partner theorem (1.5) is already an `h=0` producer. Quantitatively, whenever its aggregate transverse defect obeys

`sqrt(sum_i q_i^2)>=h/1024`,

(1.6)--(1.7) pay the branch continuously. Thus the newest partner low-defect survivor enters the present principal analysis only after that literal disjoint-cross payment has failed.

Independently, the global third-compound identity used in r19 says that if the full disjoint overlap class has mass `W_0>=1/4`, coarse two-coloring produces a literal cross-E3 packet of mass at least `1/256`, which the marginal-free cross-E3 theorem pays continuously. Therefore every globally unpaid state has a genuinely overlapping determinant class. Sections 3--5 now remove the **concentrated `h=3`** face completely and replace its diffuse face by the explicit disjoint-role currencies (5.9)--(5.12).

This means the r34 abstract `rank<=72 + operator-small` coefficient tube is no longer the sharpest B07 endpoint: before trying to treat a nonzero operator tail probabilistically, the complete determinant law can be routed into the overlap compilers, and the principal concentrated case is already paid without deleting any tail.

## 7. What remains

Full QFORM is still **OPEN**. Global continuity is still **OPEN**.

The first remaining B07 principal obligation is now

`QFORM-H3-DIFFUSE-RAINBOW-CURRENCY-RECEIVER-v1`:

> Starting from the support-diffuse light-using rainbow packet, spend one of the forced aggregate currencies `D_U D_V D_W`, `T_triangle`, or `D_U F_VW` (and cyclic variants) by a product-preserving receiver that retains all same-bank curvature and all nonzero residual spectrum.

The promising next split is:

- `D_U F_VW`: normalize the squared-edge law on `V x W`; edge concentration should force a quantitative physical indefinite/definite pair, while edge diffusion should feed a grouped cross/Fresnel receiver;
- `T_triangle`: treat the squared three-cycle law on the disjoint banks by collision versus support diffusion, rather than selecting one triangle;
- `D_U D_V D_W`: use collective diagonal smoothing on three disjoint physical banks; do not silently replace the banks by three single diagonal coordinates.

The already-proved r31 overlap-one/two compilers remain the correct routes for `h=1,2`. The new theorem here is specifically the missing determinant-only payment for a concentrated principal triple and the explicit aggregate geometry of the diffuse `h=3` face.

## 8. Deterministic checks

A 10,000-instance random symmetric `3x3` regression verified the deterministic dichotomy in Theorem 3.1: whenever all three diagonals were below `eta=d^(1/3)/4`, at least one edge exceeded `r=d^(1/3)/2`, and the resulting pair had opposite-sign eigenvalues of magnitude at least `eta`. Zero violations occurred.

A separate 500-instance random symmetric rainbow-bank regression verified (5.8) directly; zero violations occurred. The largest observed ratio `P_rain / RHS` was `0.435718`. These checks are regression only; the proofs are the exact inequalities above.
