SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B19, 2026-09-23T22:39:20Z.
attacking: the principal-minimal base-subcritical rank-six carrier — test whether it forces a quantitative spectral gap/collar, pay the sharp threshold-transfer model by the source-pinned Fresnel receiver, and quantify spectral pinning in the strict local-no-pivot chamber.

# fleet02/B19 auto11 — principal-minimal threshold transfer: a sharp obstruction and two paid/narrowed exits

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS / complementary source-valid constructions  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_STRUCTURAL_IMPLICATION_REFUTED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** full-target continuity remains OPEN; the explicit Fresnel-paid model below has a continuous `C_0` density.

## 1. Fresh source boundary and current proof graph

Owner control was refreshed from `math-research-brain` and remained revision `2026-09-22.15`, QFORM-only. The current exact target remains: arbitrary independent real coordinates with one-dimensional densities bounded by one, arbitrary symmetric coefficient matrix with at least three eigenvalues of modulus at least one, and a universal essential density bound for the quadratic form. No moment, support, iid, log-concavity, diagonal-basis, post-rotation-independence, or small-random-perturbation assumption is introduced.

The completed designated partner input is fleet03/B19 r43,

`yspennstate/math-open-problems@39db1d98a37e71ccc28619a59bc53b79d1be8408`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T220120Z-fleet03-B19-QFORM-r43/REPORT.md`.

Its exact theorem `QFORM-PRINCIPAL-MINIMAL-INDUCTIVE-REDUCTION-v1` says that one may prove the affine interval-density theorem only for matrices that are **principal-minimal at threshold 1**: `N_A(1)>=3`, while every proper ORIGINAL-coordinate principal submatrix has `N<=2`. Conditioning a complementary original bank then gives strong induction with no coefficient deletion and no constant loss. Its spectral-count corollary reduces principal-minimal matrices to `N_A(1)=3`, or `N_A(1)=4` with mixed signs.

The immediate finite-core input used by r43 is fleet03/B20 r39. Every still-unpaid state there has an ORIGINAL-coordinate partition `H disjoint_union L`, `|H|<=124`, with

`A[H,H]=L_H+E_H`, `rank(L_H)<=2`, `||E_H||_op<0.0003707865472226546`,

`A[H,L]=C_2+R_C`, `rank(C_2)<=2`, `||R_C||_op<1/64`,

and therefore

`A = diag(0_H,D) + K + E`, `D=A[L,L]`, `rank(K)<=6`,

`||E||_op<0.015995786547222654`.

The error is retained exactly. Partner r43 removes any state with `N_D(1)>=3` by original-bank conditioning, so the first local analytic debt is

`N_D(1)<=2`, full `N_A(1)=3` or mixed-sign `4`, rank-six carrier, retained nonzero error, and arbitrary subthreshold spectrum of `D` allowed arbitrarily close to `+/-1`.

Thus the live proof graph at this point is:

1. if a proper physical principal submatrix is target-active, descend exactly by r43;
2. otherwise work in the principal-minimal class (`N=3` or mixed-sign `4`);
3. all previously completed physical pair/triple, projected-crossing `D/D'/D5`, Fresnel `F/H`, ridge/window, grouped-hyperbolic and related exits retain their stated scopes;
4. on the current finite-core spine, fleet03/B20 r39 either pays a physical pair/triple branch or yields the rank-six retained-error carrier above;
5. in an inductively minimal carrier, `N_D(1)<=2` by r43;
6. the first unpaid analytic implication is to spend the third/fourth threshold crossing created jointly by the base and carrier, uniformly as subthreshold eigenvalues of `D` approach `+/-1`, without dropping `E`.

This run attacks gate 6 directly.

## 2. Main obstruction theorem: no fixed base gap and no fixed carrier collar

### Theorem 2.1 — `QFORM-PRINCIPALMINIMAL-NEARTHRESHOLD-VANISHING-CARRIER-v1`

For every `0<delta<=1/2` and every integer `m>=2`, there is a real symmetric target matrix `A=A(delta,m)` on `3m+1` ORIGINAL coordinates with all of the following properties:

1. `spec_nonzero(A)={1,1,-1,-delta}`, hence `N_A(1)=3` exactly;
2. `A` is principal-minimal at threshold one;
3. for the physical partition `H={h}`, `L=H^c`, the untouched base `D=A[L,L]` has
   `spec_nonzero(D)={1,-1,1-delta}` and therefore `N_D(1)=2`, `s_3(D)=1-delta`;
4. the retained carrier is exact rank two and error-free:
   `E=0`, `rank(K)=2`, `||K||_op=||A[H,L]||_op=sqrt(delta)`;
5. consequently
   `1-s_3(D)=delta=||A[H,L]||_op^2`;
6. every physical scalar diagonal is at most `1/m` in magnitude, every physical two-by-two principal determinant is at most `max(1/m^2,delta/m)`, and every physical three-by-three principal determinant is at most `max((1-delta)/m^3,delta/m^2)`.

In particular, for every fixed `c>0` and every fixed local-pivot threshold `tau>0`, one may first choose `delta<min(c,c^2,1/2)` and then `m` sufficiently large so that simultaneously

`1-s_3(D)<c`, `||K||_op<c`,

and all scalar, pair-determinant and triple-determinant physical pivots are below `tau`.

Hence the current principal-minimal carrier hypotheses, even with exact zero retained error and rank two instead of rank six, do **not** imply either a universal positive base deficit `1-s_3(D)>=c` or a universal positive carrier/cross norm `||K||>=c`.

### Construction

Take three disjoint original-coordinate banks `U+`,`U-`,`V`, each of size `m`, and one physical hub coordinate `h`. Let `u+`,`u-`,`v` be the flat unit vectors on those banks and `e_h` the hub vector. Define

`A = u+u+^T - u-u-^T +(1-delta)vv^T + sqrt(delta)(e_h v^T+v e_h^T)`.  (2.1)

The four displayed vectors are orthonormal. On their span, `A` is

`diag(1,-1) direct_sum [[1-delta,sqrt(delta)],[sqrt(delta),0]]`.  (2.2)

The last characteristic polynomial is

`lambda^2-(1-delta)lambda-delta=(lambda-1)(lambda+delta)`,        (2.3)

which proves item 1. Items 3--5 are immediate from the physical cut `H={h}`.

### Principal minimality

Delete the hub. The remaining target-scale eigenvalues are exactly `+1,-1`.

Delete one coordinate from `U+`. The `u+` rank-one eigenvalue becomes `1-1/m<1`, while the `u-` eigenvalue `-1` and the `(v,h)` eigenvalue `+1` remain. Thus only two target-scale modes remain. Deleting one coordinate from `U-` is analogous.

Delete one coordinate from `V`. Put `a=1-1/m`. On the normalized restricted `v` and the hub, the relevant block is

`M_a=[[a(1-delta),sqrt(a delta)],[sqrt(a delta),0]]`.             (2.4)

Its characteristic polynomial `f` satisfies

`f(0)=-a delta<0`, `f(1)=1-a=1/m>0`,                            (2.5)

so the positive root lies in `(0,1)`. Also, because `delta<=1/2`,

`f(-1)=1+a(1-2delta)>0`,                                        (2.6)

so the negative root lies in `(-1,0)`. The untouched `u+`,`u-` modes contribute exactly `+1,-1`; hence this deletion again has exactly two target-scale modes.

Every proper physical principal submatrix is contained in a one-coordinate deletion. Cauchy interlacing cannot increase either the count of eigenvalues `>=1` or the count `<=-1`, so every proper principal submatrix has `N<=2`. Thus `A` is principal-minimal. This applies partner r43 at its exact equation-level boundary: the family cannot be removed by the new dimension descent.

### Local pivots

Physical diagonals are `1/m` on `U+`, `-1/m` on `U-`, `(1-delta)/m` on `V`, and zero at the hub. Within one leaf bank, every pair block is rank one. Across distinct leaf banks, the pair determinant magnitude is at most `1/m^2`. A hub--`V` pair has determinant exactly `-delta/m`; all other hub pairs have zero determinant. This proves the two-by-two claim.

For triples, a triple with one coordinate from each leaf bank has determinant magnitude `(1-delta)/m^3`; a hub--`V`--`U+` or hub--`V`--`U-` triple has magnitude `delta/m^2`; all repetitions inside a single rank-one bank only reduce rank. This proves item 6.

The construction is therefore a source-valid strict-no-local-pivot stress family, not an artefact of a spectral-coordinate model.

## 3. The same obstruction family is uniformly paid by the required source theorem

The user-specified source package was reread at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, together with its `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`.

Apply its completed **Theorem F (Fresnel--Brascamp--Lieb)** directly to (2.1). Use the ORIGINAL-coordinate source bank

`I=U+ union U- union V`,                                        (3.1)

with the three source vectors

`v_1=u+`, `v_2=u-`, `v_3=v`,                                   (3.2)

and coefficients

`lambda_1=1`, `lambda_2=-1`, `lambda_3=1-delta`.                (3.3)

Put the hub crossing into the residual

`B=sqrt(delta)(e_hv^T+ve_h^T)`.                                (3.4)

On the source bank, `B[I,I]=0`, which is diagonal exactly; the source Gram is

`G_I=I_3`,                                                       (3.5)

and every normalized physical row leverage is exactly `1/m<=1/2`. Theorem F therefore applies while retaining the hub and its full crossing term. It gives the actual inequality

`||p_Q||_infinity
 <=12(|lambda_1 lambda_2 lambda_3| det G_I)^(-1/3)
 =12(1-delta)^(-1/3)
 <=12*2^(1/3)
 =15.119052598738477...`.                                       (3.6)

Its integrable characteristic-function majorant also gives a continuous `C_0` density on this explicit family.

This is the decisive interpretation of Theorem 2.1: the vanishing collar itself is not a density obstruction. The correct currency in this sharp model is the whole **three-Fresnel leaf packet**, including the subthreshold third base eigenvalue `1-delta`; trying to infer a fixed carrier norm or fixed distance of `s_3(D)` below one throws away exactly the resource that pays the law.

### Corollary 3.1 — `QFORM-BASE-THIRDMODE-FRESNEL-EXIT-v1`

More generally, in any current carrier state, if some ORIGINAL-coordinate source bank `I` admits

`A[I,I]=sum_{k=1}^3 lambda_k v_kv_k^T + diagonal`,               (3.7)

with the normalized three-frame leverage at most `1/2`, then all outside blocks, carrier couplings and affine terms may remain arbitrary and Theorem F gives

`||p_Q||_infinity <=12(|lambda_1lambda_2lambda_3| det G_I)^(-1/3)`. (3.8)

In particular, if `|lambda_k|>=1/2` and `det G_I>=g>0`, this branch is paid by

`||p_Q||_infinity <=24 g^(-1/3)`.                               (3.9)

Thus any genuinely hard near-threshold base state must fail this exact source-valid three-Fresnel interface (or hit another already-paid exit); mere subcriticality of the third base eigenvalue is not enough to make it hard.

## 4. New structural theorem in the strict local-no-pivot principal-minimal chamber

The fresh completed fleet01/B08 r37 report source-pins its preceding deletion theorem. In its notation, if `R` is an orthonormal selected three-eigenvector frame for eigenvalues of modulus at least `L`, an ORIGINAL coordinate `i` has selected leverage `p=||R_{i,*}||^2`, deletion gives child matrix `C`, and `tau` is the star component transverse to the top-two child absolute-eigenspace, then whenever `x=s_3(C)/L<1`,

`tau >=(1-x)L sqrt((1-p)/p)
      =(L-s_3(C)) sqrt((1-p)/p)`.                               (4.1)

This can be spliced with principal minimality and local-pivot weakness to obtain a dimension-free threshold pinning statement.

### Theorem 4.1 — `QFORM-PRINCIPALMINIMAL-N3-SPECTRAL-SURPLUS-COLLAPSE-v1`

Let `A=A^T` be principal-minimal at threshold one in dimension `n>=4`, and let

`L=s_3(A)>=1`                                                    (4.2)

be the third largest singular value. Suppose that for one `alpha>0`, every ORIGINAL coordinate satisfies

`|A_ii|<alpha`,                                                   (4.3)

and every ORIGINAL physical pair satisfies

`|A_ii A_jj-A_ij^2|<alpha`.                                     (4.4)

Then

`boxed:
 L-1
 < sqrt( [3(n-1)/(n-3)] (alpha+alpha^2) )
 <=3 sqrt(alpha+alpha^2).}`                                     (4.5)

At `alpha=2^(-20)` this gives

`s_3(A)<1.002929688897`.                                        (4.6)

At `alpha=2^(-40)` it gives

`s_3(A)<1.000002861023`.                                        (4.7)

#### Proof

Select orthonormal eigenvectors for three eigenvalues whose moduli are at least `L`, and let `p_i` be their physical row leverages. Since `sum_i p_i=3`, there is a coordinate `i` with

`p:=p_i<=3/n<1`.                                                 (4.8)

If `p=0`, deleting that coordinate preserves all three selected eigenvectors and contradicts principal minimality. Hence `p>0`.

Let `C=A[-i,-i]`. Principal minimality gives

`s_3(C)<1<=L`,                                                   (4.9)

so (4.1) applies and yields

`tau >(L-1)sqrt((1-p)/p)`.                                      (4.10)

If `b=A[-i,i]` is the full physical star, then `tau<=||b||_2`. From (4.3)--(4.4), for every `j!=i`,

`|A_ij|^2
 <=|A_ii A_jj|+|A_ii A_jj-A_ij^2|
 <alpha^2+alpha`.                                                (4.11)

Therefore

`tau^2 <=||b||_2^2 <(n-1)(alpha+alpha^2)`.                       (4.12)

Combining (4.10)--(4.12),

`(L-1)^2 < [p/(1-p)](n-1)(alpha+alpha^2)`.                       (4.13)

The function `p/(1-p)` is increasing, so (4.8) gives

`p/(1-p)<=3/(n-3)`.                                              (4.14)

This is (4.5). QED.

Dimension `n=3` is not an obstruction to the global proof: a target-active three-dimensional matrix has `|det A|>=1`, so the completed literal physical-triple determinant receiver applies directly after conditioning any outside coordinates.

The theorem shows that, after quantitative scalar/pair local pivots have failed, a principal-minimal survivor cannot hide a large spectral surplus. The remaining hard state is genuinely pinned to the owner threshold, exactly as the model in Section 2 suggests.

## 5. What was refuted, what was paid, and what remains

Two tempting shortcuts are now ruled out at the current first gap:

- **false:** principal-minimality plus `N_D(1)<=2` forces `s_3(D)<=1-c` for a universal `c>0`;
- **false:** the same hypotheses force the rank-six carrier/crossing to have a universal positive norm.

Theorem 2.1 simultaneously drives both quantities to zero, even with `E=0`, while remaining principal-minimal and while all fixed local scalar/pair/triple pivots vanish.

One substantial near-threshold chamber is nevertheless paid: whenever the base/collar geometry exposes a source-valid diffuse three-Fresnel packet as in Corollary 3.1, the required source theorem gives an explicit uniform density bound. The sharp model is paid by `<15.12` all the way to `delta=0+`.

The first compatible unpaid implication is therefore sharpened to

`QFORM-PRINCIPALMINIMAL-BASESUBCRITICAL-NONFRESNEL-THRESHOLD-TRANSFER-v1`:

> Starting from the fleet03/B20 r39 retained-error carrier
> `A=diag(0_H,D)+K+E`, `|H|<=124`, `rank K<=6`, `||E||_op<0.015995786548`,
> with partner-r43 constraints `N_D(1)<=2` and full `N_A(1)=3` or mixed-sign `4`, and after all completed physical pair/triple, `D/D'/D5`, `F/H`, ridge/window and grouped exits have failed, prove a universal essential density bound uniformly as subthreshold spectrum of `D` approaches `+/-1`; or give an exact original-coordinate descent to one of those paid mechanisms.

The remaining receiver must tolerate all of the following simultaneously:

- no fixed gap between `s_3(D)` and one;
- no fixed lower bound on `||K||`;
- arbitrary non-diagonal and high-rank subthreshold curvature inside `D`;
- the genuine retained nonzero coefficient error `E` (which cannot be dropped probabilistically);
- arbitrary fragmented/unbounded cap-one product input laws;
- no post-rotation independence or fiber-supremum dimension loss.

The positive clue from the model is that the near-threshold third base mode and the vanishing carrier have to be spent **jointly**, before either is rounded away. The obstruction is not the scalar size of either object but the lack, in the general survivor, of a source-valid three-Fresnel/physical-cross packet with which to perform that joint payment.

## 6. Verification

`CHECK.py` in this run directory independently verifies, for several `(m,delta)` values, the exact nonzero spectrum `{1,1,-1,-delta}`, principal-minimality under every one-coordinate deletion, the scalar/pair/triple pivot bounds, and the identity

`1-s_3(D)=||A[H,L]||_op^2=delta`.

It also evaluates

`12*2^(1/3)=15.119052598738477...`,

and

`1+3 sqrt(2^(-20)+2^(-40))=1.0029296888969834...`.

The exact proofs above do not depend on the numerical checker.

## 7. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. Theorem 2.1 is a structural counterexample to two candidate proof implications, not a counterexample to the conjecture. The model itself is uniformly and continuously paid by Theorem F. The required two independent end-to-end reviews of a full proof do not exist.
