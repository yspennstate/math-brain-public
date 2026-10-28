SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T18:27:46Z.
attacking: the exact dual-small-aggregate rank-three/rank-four carrier produced by the latest account03/B09 collapse, with special attention to uniform passage through a vanishing fourth carrier eigenvalue by source-coordinate grouped mixed-hub smoothing rather than deletion or square-root decoupling.

# account02/B09 r20 — diffuse dual-zero carrier receiver and a loss-free rank-transition family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL STEP APPLIED / NEW SUPPORTING RECEIVER + NEW UNIFORM RANK-TRANSITION APPLICATION / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. No counterexample to the owner target is produced. The new work closes the diffuse exact-rank-three endpoint of account03/B09's newest dual-aggregate collapse, gives the corresponding scale-dependent rank-four bound without any probability squaring, and then exhibits a genuine target-valid aligned rank-four family for which grouped mixed-hub smoothing stays uniform as the fourth carrier eigenvalue tends to zero even though the naive rank-four Fresnel bound diverges.

## 0. First unpaid implication

The first unpaid B09 implication is now

**`QFORM-DUALZERO-R4-OVERLAPPING-RANKTRANSITION-v1`.**

After the newest account03/B09 theorem reduces exact two-sided singleton-aggregate zero to

`A=D_0+S`, `rank(S)<=4`,

pay the genuinely **overlapping** diffuse rank-four carrier uniformly as `s_4(S)->0`, while retaining that nonzero fourth carrier direction exactly. The source-separated rank-one aligned transition is paid below. The exact rank-three diffuse endpoint is also paid below. What remains is therefore not a generic rank transition but the case in which the two carrier directions overlap on the same original-coordinate source bank so that no legitimate source-separated grouped-hub conditioning is available. High carrier leverage `>1/2` is a separate endpoint. A positive universal-scale fixed-pair anchored fourth volume is already paid by account01/B09 and is not part of this debt.

The small fourth carrier direction may not be discarded as a small random quadratic perturbation: arbitrary cap-one input laws have no moment or support control.

## 1. Sources actually consumed


The owner-required pinned source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The completed result used at the decisive inequality is the general-rank **Fresnel--Brascamp--Lieb Theorem F** from `FOURIER_ROUTE_REPORT.md`: if

`A=D+sum_(j=1)^r lambda_j v_j v_j^T`,

`D` is physical diagonal, the `v_j` are orthonormal, and every physical row leverage in their span is at most `1/2`, then

`|phi_Q(t)| <= (4 pi)^(r/2) |t|^(-r/2) prod_j |lambda_j|^(-1/2)`.   (1.1)

No decoupling is used; diagonal and affine terms are harmless one-coordinate twists. For `r>2`, exact integration of `min(1,B|t|^(-r/2))` gives

`boxed:
 ||p_Q||_infinity
 <= 4r/(r-2) (prod_j |lambda_j|)^(-1/r).`                         (1.2)

Thus the constants are `12` at rank three and `8` at rank four. The characteristic function is integrable, hence the density is continuous and the same coefficient gives the linear interval estimate.

The same pinned source's mixed-hub Theorem H is applied to a separate actual source-coordinate star in Section 5.

The newest compatible designated partner is account03/B09 r38,

`QFORM-RANK2-DUAL-AGGREGATE-COLLAPSE-v1`,

canonical report

`yspennstate/math-open-problems@b2a0ccad9d4f4d654e0fc84dd0323ce84230ebc4`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T175610Z-account03-B09-QFORM-r38/REPORT.md`.

Its exact-zero endpoint is used at equations (2.1)-(2.6), not merely cited. Its late-source note also records account01/B09's fixed-pair fourth-volume receiver; that route is treated as an already-paid exit rather than re-proved here.

The grouped mixed-hub theorem used for the uniform rank transition is account03/B09 r29,

`QFORM-GROUPED-HUB-PLUCKER-SMOOTHING-v1`,

`yspennstate/math-open-problems@ba035d3e65b7687b9ec8c05320f6340caabc34bb`.

I apply it through the already-proved account02/B09 r18 source-separated corollary at

`yspennstate/math-open-problems@e7a440cdcf3adb7740b6fbeba60f4f0c75f1936a`.

The pinned counterexample search still reports no valid counterexample to full QFORM; this run found none.

## 2. Normalize the partner's exact dual-zero carrier

Use the exact setup of account03/B09 r38. The complete active original-coordinate set is split into two physical banks

`H disjoint_union I`,

and the physical cross block has rank two,

`A[H,I]=P C^T`, `P^T P=I_2`, `G=C^T C>0`.                       (2.1)

Let

`R=C G^(-1/2)`, so `R^T R=I_2`.                                (2.2)

Write the two singleton augmented third-volume aggregates of r38 as `G_I,G_H`, and the two maximal cross-frame leverages as

`q_I=max_i c_i^T G^(-1)c_i`,
`q_H=max_h ||p_h||_2^2`.                                        (2.3)

Assume the exact dual-zero, no-coloop branch

`G_I=G_H=0`, `q_I<1`, `q_H<1`.                                 (2.4)

The partner theorem gives physical diagonal matrices `Lambda_H,Lambda_I` and symmetric `2 x 2` matrices `N,M` such that

`A=D_0+S`,                                                       (2.5)

where

`D_0=diag(Lambda_H,Lambda_I)`

and, after the harmless deterministic coefficient normalization (2.2),

`S=U_0 K_0 U_0^T`,
`U_0=diag(P,R)`, `U_0^T U_0=I_4`,                               (2.6)

with

`K_0 = [[N, G^(1/2)],
        [G^(1/2), G^(1/2) M G^(1/2)]].`                         (2.7)

This is just r38's exact carrier rewritten with an orthonormal four-column physical frame; no random variable is rotated.

A physical row of `U_0` in the `H` bank has squared norm `||p_h||^2`; a row in the `I` bank has squared norm `c_i^T G^(-1)c_i`. Therefore

`boxed:
 max_x ||(U_0)_{x,*}||_2^2 = q:=max(q_H,q_I).`                  (2.8)

This elementary identity is the bridge from the partner's structural currencies to the pinned theorem's physical leverage gate.

## 3. New receiver: the diffuse exact rank-three carrier is paid

### Theorem `QFORM-DUALZERO-DIFFUSE-CARRIER-RECEIVER-v1`

Assume (2.1)-(2.8) and

`q<=1/2`.                                                        (3.1)

Let `r=rank(K_0)=rank(S)`.

If `r=3`, then for arbitrary cap-one independent original-coordinate laws and arbitrary affine terms,

`boxed:
 ||p_Q||_infinity <= 12 |pdet(K_0)|^(-1/3).`                    (3.2)

If `r=4`, then

`boxed:
 ||p_Q||_infinity <= 8 |det(K_0)|^(-1/4).`                      (3.3)

Both branches have continuous densities and the same constants multiply interval length.

If in addition the owner target holds,

`s_3(A)>=1`,                                                     (3.4)

and the partner diagonal satisfies

`||D_0||_op<=tau<1`,                                             (3.5)

then r38's spectral transfer gives

`s_3(S)>=1-tau=:a`.                                              (3.6)

Consequently the rank-three branch is the target-level bound

`boxed:
 ||p_Q||_infinity <= 12/a = 12/(1-tau),`                        (3.7)

while in rank four, writing `sigma=s_4(S)>0`,

`boxed:
 ||p_Q||_infinity <= 8 [a^3 sigma]^(-1/4).`                     (3.8)

### Proof

Diagonalize the symmetric coefficient carrier on its nonzero range,

`K_0=O Lambda O^T`,                                              (3.9)

where `O` has `r` orthonormal columns and `Lambda=diag(lambda_1,...,lambda_r)` contains the nonzero eigenvalues. Put

`V=U_0 O`.                                                       (3.10)

Because `U_0^T U_0=I_4` and `O^T O=I_r`,

`V^T V=I_r`.                                                     (3.11)

For every physical coordinate `x`, orthogonal projection in coefficient space can only decrease row norm, so

`||V_{x,*}||_2^2
 <= ||(U_0)_{x,*}||_2^2
 <= q
 <=1/2`.                                                        (3.12)

Moreover

`S=sum_(j=1)^r lambda_j v_j v_j^T`.                              (3.13)

Therefore

`A=D_0+sum_(j=1)^r lambda_j v_j v_j^T`                           (3.14)

is exactly in the pinned general-rank Theorem-F class. Equation (1.2) gives (3.2) for `r=3` and (3.3) for `r=4`. This proof never squares `phi`; the `O(|L|)` estimate is the direct Fourier inversion of an integrable characteristic-function envelope.

For (3.7)-(3.8), Weyl's singular-value perturbation inequality and (3.4)-(3.5) imply (3.6). At rank three all three nonzero singular values of `S` are at least `a`, so `|pdet K_0|>=a^3`. At rank four the three largest singular values are at least `a` and the fourth is `sigma`, so `|det K_0|>=a^3 sigma`. Substitute into (3.2)-(3.3). QED.

### What this actually closes

The newest partner report called the exact rank-three/rank-four carrier the mandatory first endpoint. The diffuse exact **rank-three** endpoint is now fully paid at the target scale whenever (3.5) holds. The rank-four theorem also pays every instance with `s_4(S)` bounded below. Its only rank-transition loss is the explicit factor `s_4(S)^(-1/4)`.

That loss is not automatically structural: Section 4 gives a target-valid exact-dual-zero family for which a source-coordinate mixed-hub receiver removes it completely.

## 4. Uniform source-separated rank transition with dense same-side couplings

### Proposition `QFORM-DUALZERO-SOURCESEPARATED-RANKTRANSITION-v1`

Let `N>=4` be even. On each of two disjoint physical banks take the two-column frame whose `i`th row is

`(1,s_i)/sqrt(N)`,                                               (4.1)

with exactly `N/2` signs `s_i=+1` and `N/2` signs `s_i=-1`. Denote the two identical orthonormal frames by `P_N,R_N`, and put

`U=diag(P_N,R_N)`.                                               (4.2)

For `0<=epsilon<=1`, let `t=1+epsilon` and define the coefficient carrier

`K_epsilon = [[diag(t,0), I_2],
              [I_2, diag(t,0)]],`                               (4.3)

and the physical matrix

`A_epsilon=U K_epsilon U^T`.                                    (4.4)

Then:

1. `A_epsilon` satisfies the exact owner spectral hypothesis for every `epsilon in [0,1]`;
2. both r38 singleton third-volume aggregates vanish exactly and every physical carrier leverage is `2/N`;
3. the two same-side blocks are dense aligned rank-one matrices;
4. nevertheless

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <= 3e [ ((1+epsilon)/2)(1-2/N)^2 ]^(-1/3)`                    (4.5)

for every admissible product law, and the same coefficient multiplies interval length. The density is continuous.

In particular the bound is uniform through the rank transition `epsilon downarrow 0`:

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <=3e [ (1/2)(1-2/N)^2 ]^(-1/3).`                               (4.6)

For `N=8` the right side is `<12.447`; as `N->infinity` it tends to

`3e 2^(1/3)=10.2744614856...`.                                  (4.7)

### Exact spectral and aggregate checks

Permute the four coefficient coordinates into the two cross directions. The carrier is the direct sum

`[[t,1],[1,t]] direct_sum [[0,1],[1,0]]`.                        (4.8)

Hence

`spec(K_epsilon)={2+epsilon, epsilon, 1, -1}`.                  (4.9)

Because `U` has orthonormal columns, these are exactly the nonzero physical eigenvalues of `A_epsilon`. Thus at least three eigenvalues have modulus at least one for every `epsilon`, including the rank-three endpoint `epsilon=0`.

The same-side blocks are

`t p_1 p_1^T` and `t r_1 r_1^T`,                                (4.10)

so their physical entries are of order `1/N`. The cross block is `P_N R_N^T`, whose entries are `0` or `2/N`. Thus this is a genuinely diffuse source-coordinate family.

For any leaf coordinate `i`, every row of the singleton-augmented matrix

`A[H union {i}, I\{i}]`

lies in the two-dimensional row span of `R_N[I\{i},:]`: the hub rows do so by the rank-two cross factorization, and the extra leaf row does so by (4.10). Therefore its rank is at most two and its third volume is zero. Summing gives `G_I=0`; the same argument with the banks reversed gives `G_H=0`. Every row leverage is exactly `2/N`.

Thus this family is an actual exact-zero instance of the latest partner's carrier chamber, not an unrelated toy.

### Loss-free grouped mixed-hub payment

Now apply a `45`-degree deterministic change of basis **only inside the two-dimensional coefficient planes**, simultaneously to `P_N` and `R_N`. This does not rotate any random coordinate and leaves the physical cross block unchanged.

In the new coefficient basis, the two hub-frame columns have disjoint original-coordinate supports: one is supported on the `+` sign class and the other on the `-` sign class. The same is true for the two leaf-frame columns, call them `c_1,c_2`.

The leaf same-side coefficient `diag(t,0)` becomes

`t w w^T`, `w=(1,1)/sqrt(2)`,                                   (4.11)

so the physical leaf block is the dense rank-one square along

`v=(c_1+c_2)/sqrt(2)`.                                          (4.12)

Condition the entire physical hub bank supporting the second hub-frame column. This is legitimate original-coordinate conditioning. The conditioned second cross direction becomes only a leaf linear term. The first hub bank remains as a grouped source-coordinate hub, while **all** hub same-side curvature, including its dense rank-one block and its coupling to the conditioned bank, is retained as allowed hub phase/linear terms.

Apply the completed r18 source-separated corollary of account03/B09 r29 with grouped hub rank `h=1`, displayed leaf rank `r=1`, cross direction `c_1`, and displayed square `v`.

The two-column leaf frame `[v,c_1]` has Gram determinant

`det Gram(v,c_1)=1-|<v,c_1>|^2=1-1/2=1/2`.                     (4.13)

Its Pluecker basis law is unchanged by the invertible coefficient transformation from `[c_1,c_2]`. A basis consists of one `+` leaf coordinate and one `-` leaf coordinate, uniformly. Two iid bases are disjoint exactly when both selected coordinates differ, hence

`rho_N=(1-2/N)^2`.                                               (4.14)

The r18/r29 product-law bound is therefore exactly (4.5). It is obtained from an integrable characteristic-function envelope before any probability squaring, so (4.5) is a direct linear small-ball estimate.

### Why this is a genuine rank-transition advance

If one instead displays all four carrier eigenvalues in Theorem F, (3.3) gives only

`||p||_infinity <=8[(2+epsilon)epsilon]^(-1/4),`                 (4.15)

which diverges as `epsilon downarrow 0`. At the endpoint `epsilon=0`, the rank-three theorem gives the finite bound

`12*2^(-1/3)=9.5244063118...`.                                  (4.16)

The grouped mixed-hub estimate (4.6) stays finite on the entire interval `0<=epsilon<=1`. Hence the fourth-eigenvalue blow-up in (4.15) is a **method loss**, not an intrinsic concentration phenomenon, whenever the two coefficient directions are source-separable.

## 5. Owner-required pinned mixed-hub theorem applied to an actual source-coordinate star

The previous sections use pinned Theorem F and the newer grouped theorem. For completeness, apply the pinned `e5f71d79...` **Theorem H itself** to an actual target-valid star with dense same-side leaf coupling.

Let `m` be a Walsh size `m>=8`, let `u,v,w` be three flat orthonormal Walsh vectors on one original-coordinate leaf bank, and let `X_h` be a disjoint literal physical hub. Define

`Q_m = X_h^2
      +4 X_h <u,Y>
      +<v,Y>^2
      -<w,Y>^2.`                                                 (5.1)

On the aggregate basis `(e_h,u,v,w)`, its coefficient matrix is

`[[1,2],[2,0]] direct_sum [1] direct_sum [-1]`,                 (5.2)

so

`spec={ (1+sqrt(17))/2, (1-sqrt(17))/2, 1, -1 }`.              (5.3)

All four eigenvalues have modulus at least one. This is therefore an actual owner-target family.

For Theorem H use one physical hub and the two displayed same-side square directions `v,w`. The mixed physical leaf frame is

`[v,w,2u]`,                                                      (5.4)

whose Gram matrix is `diag(1,1,4)`, determinant `4`. After whitening, every physical leaf leverage is

`u_i^2+v_i^2+w_i^2=3/m<=3/8<1/2`.                              (5.5)

Theorem H therefore gives

`|phi_(Q_m)(t)|
 <= (2|t|)^(-1)(4 pi |t|)^(-1)(4 pi)^3 * 4^(-1/2)
 =4 pi^2 |t|^(-2).`                                             (5.6)

Since

`integral_R min(1,4 pi^2 t^(-2)) dt = 8 pi`,                   (5.7)

Fourier inversion gives the concrete inequality

`boxed:
 ||p_(Q_m)||_infinity <=4,`                                     (5.8)

and hence

`boxed:
 P{Q_m in L}<=4|L|`                                             (5.9)

for every interval `L`. The density is continuous.

The dense same-side operator `<v,Y>^2-<w,Y>^2` is retained in original source coordinates. No spectral-coordinate independence is asserted, and no square-root decoupling is used.

## 6. Relation to the newest fixed-pair fourth-volume receiver

Account03/B09 r38's late-source refresh consumes account01/B09 `QFORM-FIXEDPAIR-AGGREGATE-FOURVOLUME-v1`: for a fixed physical pair `{a,b}`, positive anchored disjoint fourth-volume currency `U_ab` gives

`||p_Q||_infinity <8.279 U_ab^(-1/8)`                            (6.1)

with arbitrary pair core and same-side curvature retained.

This is compatible with the present receiver. It does not replace Section 4 in a diffuse rank transition: a fixed physical pair can have Pluecker weight tending to zero with dimension, and the rank-four determinant itself vanishes like `epsilon` in the family (4.3). The grouped source-separated mechanism instead spends an entire original-coordinate bank and stays uniform in both the physical row scale and `epsilon`.

Thus an unpaid exact dual-zero rank-four carrier may, without loss of currently paid cases, be assumed to have no universal-scale fixed-pair anchored fourth volume and no source-separated rank-one mixed-hub exit of the type above.

## 7. Remaining gap and scope discipline

The new proof does **not** establish that every r38 carrier has `q<=1/2`; r38 only gives no-coloop gates `<1`. High carrier leverage remains separate.

It also does **not** permit deletion of a small nonzero fourth carrier eigenvalue. The family (4.3) demonstrates why the correct goal is a uniform interpolation theorem, not a perturbative omission.

The specific next B09 target is therefore the overlapping phase version of the rank transition:

`A=D_0+U_0 K_epsilon U_0^T`,                                    (7.1)

with `U_0` a diffuse four-frame inherited from the two rank-two cross frames, `s_3(U_0 K_epsilon U_0^T)` bounded below, `s_4 ->0`, but no coefficient basis separates the hub partner directions into disjoint original-coordinate banks and no transverse projected crossing/fixed-pair fourth-volume exit has universal scale. A successful argument must preserve the fourth direction inside the phase, likely by a grouped source-law estimate rather than an even-moment absolute decoupling. The r18 exact rank calculation already shows that cancelling the overlapping hub phase first stalls at `|t|^-1`.

No hidden moments, support bounds, iid assumptions, log-concavity, Gaussianity, or post-rotation independence are used above. Continuity is asserted only in the branches with an explicit integrable characteristic-function envelope.

Full-target essential boundedness: **OPEN**.  
Full-target continuous density: **OPEN**.
