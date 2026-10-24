SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T17:42:33Z.
attacking: the `G_*=0` aligned rank-two hub/star survivor with nonzero physical hub core—retain dense same-side curvature and identify an undecoupled source-coordinate exit before any reciprocal physical-pair payment.

# account02/B09 r18 — aligned rank-one grouped-hub exit and the exact critical decoupling obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **NEW SUPPORTING STRUCTURAL/ANALYTIC COROLLARY + NEW METHOD OBSTRUCTION / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. No valid counterexample to the owner target is produced here.

## 0. First unpaid implication

The first unpaid implication is now

**`QFORM-GSTARZERO-RANK1-OVERLAPPING-GROUPED-HUB-v1`.**

In the exact `G_*=0` rank-two hub/star normal form, after the source-separated grouped-hub exit proved below, pay the canonical overlapping model

`Q = F_H(X_H) + 2 U L + 2 W V + lambda V^2 + sum_i phi_i(X_i) + affine`,

where `(U,W)=P^T X_H` is a **dependent two-dimensional projection of one original product hub bank**, `(L,V)=Z^T X_I` is the corresponding two-dimensional leaf frame, `lambda != 0`, the physical row leverages are diffuse, and `F_H` is arbitrary dense hub curvature.  One must keep the joint hub phase: conditioning `W` is not product-safe, while absolute Cauchy--Schwarz cancellation of `F_H` is proved below to land exactly at the non-integrable `|t|^{-1}` threshold.  Rank-two aligned leaf curvature is a further unpaid subcase unless another already-paid exit applies.

This is strictly narrower than the previous `QFORM-GSTARZERO-ALIGNED-HUBCORE-INTERPOLATION-v1`: rank-one aligned curvature is now paid whenever either one literal hub row is quantitatively transverse or the two aggregate hub directions can be separated into disjoint source-coordinate banks.

## 1. Sources actually used

The required pinned Claude record was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The completed mixed-hub Theorem H there is used at an actual target inequality in Section 4.  Its exact useful feature here is that a literal original-coordinate hub contributes one full power of `|t|^{-1}` while a transverse spread square contributes the remaining half power, with arbitrary hub core, outside blocks and affine terms retained.  No probability squaring is used in that theorem.

The current Claude continuation `c4c23b784395630c094ba299a50712209921d1ae` was also read.  It records, among other things, the two-hub and spread-hub mechanisms and explicitly warns that a remaining large square lying *along* the two hub partners is not paid by the transverse-square theorem; that is exactly the alignment issue treated here.

The grouped-hub theorem used in Section 3 is account03/B09 r29,

`QFORM-GROUPED-HUB-PLUCKER-SMOOTHING-v1`,

`yspennstate/math-open-problems@ba035d3e65b7687b9ec8c05320f6340caabc34bb`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T101630Z-account03-B09-QFORM-r29/REPORT.md`.

The latest compatible designated-partner result read and applied in Section 6 is account03/B09 r37,

`QFORM-LOCALIZED-HUBPAIR-PROJECTED-CROSSING-CLOSURE-v1`,

with canonical mathematics at `yspennstate/math-open-problems@cc52744b60b9a747aec8356a913cd0b0729d5515`.

The pinned counterexample search reports no valid counterexample to full QFORM, and this run found none.

## 2. Starting point: the exact aligned `G_*=0` normal form

Use the rank-two physical hub/star notation from the preceding B09 run:

`A[H,I]=P C^T`, `P^T P=I_2`, `G=C^T C>0`, `Z=C G^(-1/2)`, so `Z^T Z=I_2`.

Write the physical rows of `Z` as `z_i` and their leverages as

`ell_i=|z_i|^2`.

The preceding exact row identity and stitching argument proved that, away from a deletion coloop, `G_*=0` forces the entire opposite-bank curvature into

`A[I,I]=Lambda+Z R Z^T`,                                         (2.1)

where `Lambda` is diagonal and `R=R^T` is `2 x 2`.  This is a coefficient identity in original coordinates; it does not rotate the random vector.

This run first treats the rank-one aligned case

`R=lambda v v^T`, `|v|=1`, `lambda != 0`.                       (2.2)

Put `r=Z v`.  For a physical hub coordinate `h`, with `p_h` the `h`-th row of `P`,

`A[I,h]=C p_h=Z G^(1/2) p_h`.

Define

`q_h=G^(1/2)p_h`,
`theta_h=|v wedge q_h|^2`.                                      (2.3)

The number `theta_h` is the exact source-coordinate transversality between the aligned square and the leaf partner of the literal hub `h`.

## 3. New structural exit: source-separated diffuse hubs are already paid

### Corollary `QFORM-GSTARZERO-RANK1-SOURCE-SEPARATED-GROUPED-EXIT-v1`

Let the original hub bank split into two disjoint coordinate banks

`H=H_1 disjoint_union H_2`.

Suppose, after an invertible deterministic change of basis **only in the two-dimensional coefficient space**, the rank-two cross block has the exact source-separated form

`A[H,I]=p c^T + q v^T`,                                         (3.1)

where `supp(p) subset H_1`, `supp(q) subset H_2`, `p != 0`, and the leaf block is

`A[I,I]=D+lambda v v^T`,                                        (3.2)

with `D` diagonal, `lambda != 0`, and `v,c` linearly independent.  No condition is imposed on `A[H,H]`: it may be dense, indefinite, singular and may couple `H_1` to `H_2`.  Blocks involving a further disjoint bank and all affine terms are arbitrary.

Normalize `p_0=p/|p|`, put `c_0=|p|c`, and form the two-column leaf matrix

`W=[v,c_0]`, `G_0=W^T W`.                                       (3.3)

Let `U_0=W G_0^(-1/2)` be its whitened physical leaf frame, and let

`rho=P(S cap T=empty)`                                          (3.4)

for two iid Pluecker-basis samples of this two-frame, exactly as in account03/B09 r29.  If `rho>0`, then

`boxed:
||p_Q||_infinity <= 3e [rho det(G_0) |lambda|]^(-1/3),`         (3.5)

and

`boxed:
P{Q in L} <= 3e [rho det(G_0) |lambda|]^(-1/3) |L|`             (3.6)

for every interval `L`.  The density is continuous.

### Proof

Condition on **all original coordinates in `H_2`** and on every further outside bank.  This is legitimate product-coordinate conditioning.  The term `q v^T` in (3.1) becomes only a linear term in the leaf variables.  Every `H_1-H_2` term of the arbitrary dense hub block becomes a linear term in the retained `H_1` variables, while `A[H_1,H_1]` remains completely arbitrary.

The active cross block is therefore the rank-one grouped block

`p c^T=p_0 c_0^T`,

and the exact leaf block is still (3.2).  Apply `QFORM-GROUPED-HUB-PLUCKER-SMOOTHING-v1` with grouped hub rank `h=1`, leaf rank `r=1`, grouped projection `p_0^T X_(H_1)`, displayed square `lambda v v^T`, and mixed leaf frame `W=[v,c_0]`.

The product-law corollary of that theorem is

`||p_Q||_infinity <= e (r+2h)/(r+2h-2)
 [rho det(G_0) |lambda|]^(-1/(r+2h)).`

With `r=h=1` this is exactly (3.5).  The theorem has an `L^1` characteristic-function envelope, so continuity and (3.6) follow directly.  No projected hub coordinates are declared independent; the grouped projection theorem uses only its source-valid density cap.  QED.

### What changed

This removes the need to locate one large physical hub coefficient whenever the two aggregate hub directions are source-separated.  A whole diffuse bank can supply the hub smoothing while every physical cross coefficient tends to zero.  The obstruction is therefore not “diffuse hub” by itself; it is **overlap of the two hub partner directions on the same source coordinates**.

## 4. Pinned Theorem H applied to a real target inequality

Take two literal physical hubs `a,b` and a leaf bank of Walsh size `m>=4`.  Let `u,v` be flat orthonormal leaf vectors and set

`Q_m = X_a^2 + X_b^2
       + 4 X_a <u,Y> + 4 X_b <v,Y>
       + <v,Y>^2`.                                               (4.1)

On the aggregate basis `(e_a,u,e_b,v)` the coefficient matrix is the direct sum

`[[1,2],[2,0]] direct_sum [[1,2],[2,1]]`.                       (4.2)

Hence its spectrum is

`{(1+sqrt(17))/2, (1-sqrt(17))/2, 3, -1}`.                     (4.3)

Every eigenvalue has modulus at least one, so (4.1) is an actual owner-target family.

Condition on the literal coordinate `X_b`.  Use the pinned `e5f71d79...` Theorem H with the single literal hub `a`, displayed same-side square vector `v`, and hub-leaf vector `2u`.  The mixed Gram matrix is

`diag(1,4)`,                                                     (4.4)

and the normalized mixed leverage at leaf coordinate `i` is

`v_i^2+u_i^2=2/m<=1/2`.                                         (4.5)

The rank-one/one-hub specialization of Theorem H therefore gives

`boxed:
||p_(Q_m)||_infinity <= 3*2^(4/3) * 4^(-1/3)
                     = 3*2^(2/3)
                     = 4.7622031559... .}`                       (4.6)

The same coefficient multiplies interval length:

`P{Q_m in L} <= 3*2^(2/3)|L|`.                                 (4.7)

This retains the dense same-side square `<v,Y>^2` and a nonzero hub core.  The proof is undecoupled and reaches the linear small-ball scale directly.

## 5. Literal-hub corollary inside the aligned star

The same calculation gives a useful exact criterion in the normal form (2.1)-(2.2).

### Corollary `QFORM-GSTARZERO-RANK1-PHYSICAL-HUB-EXIT-v1`

Assume

`max_i ell_i<=1/2`                                               (5.1)

and choose a literal hub `h` with `theta_h>0`.  Condition every other original hub coordinate.  The mixed leaf rows for Theorem H are

`rho_i=((Zv)_i,A_{ih})=z_i [v,q_h]`.                             (5.2)

Because `[v,q_h]` is invertible, whitening is invariant under this deterministic basis change:

`rho_i^T (sum_j rho_j rho_j^T)^(-1)rho_i=|z_i|^2=ell_i`.        (5.3)

Moreover

`det(sum_i rho_i rho_i^T)
 =det([v,q_h]^T[v,q_h])
 =theta_h`.                                                      (5.4)

Thus

`boxed:
||p_Q||_infinity
 <=3*2^(4/3)(|lambda| theta_h)^(-1/3),`                         (5.5)

with continuous density and the same coefficient in the interval inequality.  All hub-hub curvature, including a nonzero or nearly singular physical pair core, is retained because Theorem H allows the hub block and all conditioned outside blocks to be arbitrary.

The physical currencies satisfy the exact aggregate identity

`sum_(h in H) theta_h
 =v_perp^T G^(1/2)(sum_h p_h p_h^T)G^(1/2)v_perp
 =v_perp^T G v_perp`.                                           (5.6)

Equation (5.6) is useful but does **not** permit replacement of the sum by one universal physical row.  A diffuse transverse hub direction can make every `theta_h` small.

## 6. Latest designated-partner theorem applied to an actual inequality

The latest compatible account03/B09 result, r37 `QFORM-LOCALIZED-HUBPAIR-PROJECTED-CROSSING-CLOSURE-v1`, pays a transverse projected crossing while retaining arbitrary same-side curvature.  Apply it to the following source-coordinate target family.

Let `a,b` be literal hubs.  Let `T` carry three flat orthonormal vectors `u,v,w`; let a disjoint bank `S` carry a flat unit vector `s` on at least two physical coordinates.  Set

`Q_tau = X_a^2+X_b^2
       +4X_a<u,X_T>+4X_b<v,X_T>
       +<v,X_T>^2
       +2 tau <s,X_S><w,X_T>`.                                  (6.1)

The first four aggregate directions have the target spectrum (4.3), while the last two contribute `+|tau|,-|tau|`.  Hence the full owner target holds for every real `tau`, including `tau=0`.

For the physical pair `{a,b}` and the cut against `T`,

`B_T=A[{a,b},T]` has rows `2u^T,2v^T`, so

`Delta=det(B_T B_T^T)=16`.                                      (6.2)

Project the `S x T` crossing onto the orthogonal complement of `row(B_T)=span(u,v)`.  Since `w` is orthogonal to both,

`C=tau s w^T`, `||C||_F^2=tau^2`.                              (6.3)

The r37 Cauchy--Binet identity gives

`V_ab(S)=Delta ||C||_F^2=16 tau^2`.                             (6.4)

Its row volume marginals are exactly `s_k^2`; for a flat `S`-bank they are `1/|S|<=1/2`.  Therefore r37 gives, for `tau!=0`,

`boxed:
||p_(Q_tau)||_infinity
 <=3*2^(5/6)(16 tau^2)^(-1/6)
 =3*2^(1/6)|tau|^(-1/3)
 =3.3673861449... |tau|^(-1/3).}`                               (6.5)

This is a real inequality, not a citation-only use of the partner theorem.

On the same family the pinned mixed-hub estimate (4.6) remains valid **uniformly in `tau`**: condition the entire `S` bank and `X_b`; the `tau`-crossing becomes only a leaf linear term, which Theorem H allows.  Thus the actual combined estimate is

`boxed:
||p_(Q_tau)||_infinity
 <= min(3*2^(2/3), 3*2^(1/6)|tau|^(-1/3)).}`                    (6.6)

This is a concrete complementary interpolation.  Projected crossing is stronger when the transverse resource is substantial; source-coordinate mixed-hub smoothing prevents the reciprocal crossing scale from blowing up at the aligned endpoint.

## 7. Source-separated diffuse target family: grouped smoothing removes the physical-row loss

The new Section 3 corollary is genuinely stronger than selecting one literal hub row.

Take two disjoint hub banks `H_1,H_2`, each of size `N`, with flat unit vectors `p` and `q`.  Take two disjoint leaf groups `I_1,I_2`, each of size `m>=2`, with flat unit vectors `c_1,c_2`.  Define

`A_HH = p p^T + q q^T`,                                         (7.1)

`A_HI = 2 p c_1^T + 2 q c_2^T`,                                (7.2)

`A_II = c_2 c_2^T`.                                             (7.3)

The supports of `p` and `q` are disjoint original coordinate sets; likewise `c_1,c_2` have disjoint leaf supports.  In the aggregate basis `(p,c_1,q,c_2)` the active matrix is again (4.2), so the spectrum is exactly (4.3): this is a target-valid family for every `N,m`.

Condition `H_2`.  Apply Section 3 to the grouped `H_1` projection.  Here

`W=[c_2,2c_1]`, `det(W^T W)=4`.                                 (7.4)

The whitened two-frame has one unit vector on each `m`-coordinate leaf group.  Its Pluecker basis law chooses one physical coordinate from each group uniformly.  Two iid bases are disjoint iff both chosen coordinates differ, so

`rho=(1-1/m)^2`.                                                 (7.5)

Therefore

`boxed:
||p_Q||_infinity
 <=3e [4(1-1/m)^2]^(-1/3).}`                                   (7.6)

For example, at `m=8` the bound is

`||p_Q||_infinity <=5.615526`,                                  (7.7)

and it tends to `3e/4^(1/3)=5.137231...` as `m` grows.  It is independent of the hub-bank size `N`.

By contrast, any one physical coordinate `h in H_1` has

`theta_h=4/N`,                                                  (7.8)

so the literal-hub estimate (5.5) deteriorates as

`3*2^(2/3) N^(1/3)`.                                            (7.9)

Thus the grouped source-separated theorem pays an honest diffuse star with dense same-side hub curvature and dense same-side leaf curvature that a single-coordinate extraction loses by a power of dimension.  No post-rotation independence is asserted: only original-coordinate conditioning of the disjoint bank `H_2` is used.

## 8. New exact method obstruction: absolute hub decoupling is critical in the aligned survivor

A natural attempt on the still-overlapping case is to cancel the arbitrary hub phase by Cauchy--Schwarz and then use the pinned Fresnel/Brascamp--Lieb theorem on doubled leaf variables.  The following exact rank calculation shows why this does not reach `O(|L|)`.

Consider the aligned two-plane phase, after deterministic whitening of coefficient frames only,

`Q=F_H(X_H)
  +2(P^T X_H)^T S(Z^T Y)
  +(Z^T Y)^T R(Z^T Y)
  +Y^T Lambda Y+linear`,                                       (8.1)

where `P,Z` have two orthonormal columns, `S` is invertible, `R=R^T` is arbitrary, and `Lambda` is diagonal.

Cauchy--Schwarz in the hub bank gives

`|phi_Q(t)|^2 <= E_(X_H) |E_Y exp(i t[...])|^2`.                (8.2)

Introduce an independent leaf copy `Y'`.  In aggregate coordinates

`u=P^T X_H`, `z=Z^T Y`, `z'=Z^T Y'`,

the low-rank quadratic matrix on the right of (8.2) is

`M_6 = [[0,S,-S],
        [S^T,R,0],
        [-S^T,0,-R]].`                                         (8.3)

Use the orthogonal leaf-copy variables

`a=(z+z')/sqrt(2)`, `b=(z-z')/sqrt(2)`.                         (8.4)

Then (8.3) becomes

`[[0,0,sqrt(2)S],
  [0,0,R],
  [sqrt(2)S^T,R,0]]`.                                          (8.5)

Group `(u,a)` as a four-dimensional left block and `b` as a two-dimensional right block.  The matrix is exactly

`[[0,K],[K^T,0]]`, `K=[sqrt(2)S; R]` (`4 x 2`).                 (8.6)

Since `S` is invertible, `rank K=2`, and hence

`boxed: rank(M_6)=4`                                             (8.7)

for **every** aligned same-side matrix `R`, including invertible rank two.

Even if all physical leverage gates are ideal, Theorem F applied after (8.2) can therefore supply at most

`|phi_Q(t)|^2 <= C |t|^-2`,                                     (8.8)

which becomes only

`|phi_Q(t)| <= C^(1/2)|t|^-1`.                                 (8.9)

The Fourier integral is critical.  The same-side aligned curvature is spent in the difference `R,-R` and creates no post-square-root gain.

### Repeating the moment does not repair it

If `R` is invertible, apply the same idea to a `2k`-th absolute moment.  There are `k` positive and `k` negative independent leaf copies.  Their block-diagonal aligned curvature is

`L=diag(R,...,R,-R,...,-R)`,                                    (8.10)

and the hub couples with signs `+S` and `-S`.  Since `L` is invertible, eliminate the leaf block.  Its Schur complement on the two hub directions is

`-sum_(positive) S R^-1 S^T
 -sum_(negative) (-S)(-R^-1)(-S^T)=0`;                          (8.11)

the positive and negative copies cancel exactly.  Consequently the moment-form rank is exactly `4k`.  Rank-`4k` Fresnel decay is `|t|^-2k`; taking the `2k`-th root again gives precisely `|t|^-1`.

Thus no even-moment absolute decoupling that first cancels the hub phase and then invokes only rank/Fresnel volume can cross the integrability threshold in this aligned model.  This is a **method obstruction**, not a QFORM counterexample.  It sharply identifies why the next step must keep phase information in the overlapping two-dimensional hub projection, or switch to a genuinely real-variable source-coordinate argument.

## 9. Scope and remaining debt

The run establishes three concrete things.

1. Rank-one aligned `G_*=0` curvature is paid by pinned Theorem H whenever one literal hub row is quantitatively transverse, uniformly through arbitrary nonzero hub-core strata.
2. The same rank-one aligned case is paid **without any large physical hub row** when the two aggregate hub directions are supported on disjoint original-coordinate banks; the grouped-hub theorem gives a dimension-free direct linear small-ball bound while retaining arbitrary dense hub curvature.
3. The obvious fallback—cancel arbitrary overlapping hub curvature by absolute Cauchy--Schwarz and hope the aligned square restores the lost half-power—is algebraically critical at `|t|^-1` for every aligned `R` and for every even moment.

Accordingly the next B09 mathematical debt is not another physical-minor search.  It is the overlapping grouped phase:

`Q=F_H(X_H)+2UL+2WV+lambda V^2+diagonal leaf twist`,             (9.1)

with `(U,W)` a dependent two-dimensional projection of the **same** original hub product bank.  A successful estimate must exploit that source provenance jointly, rather than conditioning one projected component or taking absolute values that erase the aligned phase.  The latest Claude `(SP)`-type conditional-adaptation problem is conceptually adjacent, but it remains proposed rather than proved and is not used as a premise here.

Full QFORM remains **OPEN**.  Full-target continuity remains **OPEN**; continuity is proved only in the Fourier-integrable branches explicitly stated above.
