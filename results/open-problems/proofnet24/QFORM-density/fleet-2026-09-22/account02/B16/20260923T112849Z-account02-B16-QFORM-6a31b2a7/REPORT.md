SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T11:28:49Z.
attacking: true near-coloop duplicated-gate failure — aggregate two diffuse original-coordinate source banks before reciprocal determinant payment, and use the pinned ruled projection theorem on the complementary curved side without inventing projected independence.

# account02/B16 — true near-coloop gate failure can be harmless after source-bank aggregation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T112849Z-account02-B16-QFORM-6a31b2a7`  
Status: `NEW SUPPORTING THEOREM / SOURCE-VALID OBSTRUCTION TO ATOMWISE PAYMENT / FULL QFORM OPEN`  
Regularity: essential boundedness is proved for the family below. The pinned ruled theorem supplies a continuous-side estimate on the one-sheet side; global continuity is not claimed here.

## 1. First unpaid implication

The current partner reduction leaves a genuine near-coloop collar. Account03/B16 r28 proves `QFORM-XOR-BALANCED-BASIS-v1`: after the prior disjoint-basis and transverse escapes, duplicated-gate failure is paid whenever `a=1-c>=1/64`; therefore only `c>63/64` remains. Its exact source is

`yspennstate/math-open-problems@5f7b47acd0c385e3c65a9c20c808eca6a5527e71`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T105237Z-account03-B16-QFORM-r28/REPORT.md`.

The first unpaid B16 implication is consequently

`QFORM-TRUE-NEAR-COLOOP-BANK-COMPILER-v1`:

> In the `c>63/64` duplicated-gate chamber, either extract a bounded number of disjoint original-coordinate banks whose **aggregate** variables make a uniformly nondegenerate curved receiver, or pay the genuinely shared-bank endpoint by a source-first Fresnel/volume mechanism. One may not replace the source law by independent projected coordinates or by normalized conditional projection caps.

This run proves a concrete family in the actual r28 collar for which the first alternative works uniformly while every analogous atom-by-atom physical-triple certificate diverges with the bank size.

## 2. Exact target-valid frame inside the r28 hard collar

Fix

`0<a<1/64`, `c=1-a`, `h=1/128`.

Put

`q=sqrt(a) h`,

`t1^2=a(1-h)(1-2h^2)`,

`t2=-t1 sqrt(h/(1-h))`,

with `t1>0`. In spectral coordinates `e1,e2,e3`, take the hub row

`r0=(sqrt(c),0,0)`

and four aggregate residual rows

`u1=(t1,sqrt(h),0)`,

`u2=(t2,sqrt(1-h),0)`,

`u3=(q,0,1/sqrt(2))`,

`u4=(-q,0,1/sqrt(2))`.

The identities are exact:

`sum_(nu=1)^4 (u_nu)_1^2=a`,

`sum_(nu=1)^4 (u_nu)_(2:3)(u_nu)_(2:3)^T=I_2`,

`sum_(nu=1)^4 (u_nu)_1 (u_nu)_(2:3)=0`.

Indeed

`t1^2+t2^2=a(1-2h^2)`,

`q^2+q^2=2ah^2`,

and `t1 sqrt(h)+t2 sqrt(1-h)=0`, while the `u3,u4` slope/transverse cross terms cancel. Hence

`r0 r0^T + sum_(nu=1)^4 u_nu u_nu^T=I_3`.                      (2.1)

Now choose an integer `m>=64`. Keep `u1` as one physical original-coordinate row, and replace each of `u2,u3,u4` by `m` identical physical rows `u_nu/sqrt(m)`. Equation (2.1) is unchanged, so the resulting physical frame `R` still satisfies

`R^T R=I_3`.                                                       (2.2)

Every residual **transverse** physical leverage is below `1/64`:

`h_1=h=1/128`,

`h_(2,k)=(1-h)/m<1/64`,

`h_(3,k)=h_(4,k)=1/(2m)<1/64`.                                  (2.3)

The special row `u1` fails the r28 duplicated gate by a fixed amount:

`h+t1^2/(2a)
 =h+(1-h)(1-2h^2)/2
 =1/2+h/2-h^2(1-h)
 =1/2+8065/2097152
 >1/2`.                                                           (2.4)

At the same time `a<1/64`, equivalently `c>63/64`. Thus this family is genuinely in the **surviving** r28 near-coloop gate-failure collar, rather than in the branch r28 already pays.

Take

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`.                              (2.5)

It has eigenvalues `{1,-1,1}`. Since `R` has orthonormal columns, the physical matrix

`A=R Lambda R^T`                                                   (2.6)

has nonzero spectrum exactly `{1,-1,1}`. Therefore every member of the family is a strict instance of the full three-large-eigenvalue target.

## 3. Original-product coordinates and the exact projection interface

Let `X0,X1` be the hub and special original-coordinate variables. For the three disjoint size-`m` source banks define

`Y_nu=m^(-1/2) sum_(k=1)^m X_(nu,k)`, `nu=2,3,4`.                 (3.1)

The five objects

`X0, X1, Y2, Y3, Y4`                                              (3.2)

are genuinely independent because they are functions of disjoint original-coordinate groups. No spectral rotation is used to infer this.

By the one-dimensional product projection theorem,

`||p_(Y_nu)||_infinity<=sqrt(2)`.                                (3.3)

More importantly for the assigned projection/product interface, `(Y2,Y3)` is a two-dimensional orthogonal projection of the original product law: its two physical coefficient vectors are orthonormal. The pinned Livshyts--Paouris--Pivovarov bound therefore gives

`||p_(Y2,Y3)||_infinity<=2`.                                     (3.4)

This statement survives arbitrary orthogonal mixing of the two projected coordinates. Such a mix need **not** preserve independence. For example, with compact non-Gaussian source laws, the support of `(Y2,Y3)` is a Cartesian product of intervals, whereas a generic non-axis orthogonal rotation has a rotated support and is not a product law. Thus (3.4) is used only as a joint marginal statement; it is never upgraded to projected independence.

The spectral coordinates of `RX` are

`S=sqrt(c)X0+t1 X1+t2 Y2+qY3-qY4`,

`T=sqrt(h)X1+sqrt(1-h)Y2`,

`V=(Y3+Y4)/sqrt(2)`.                                              (3.5)

Consequently

`Q=X^TAX=2ST+V^2`.                                                (3.6)

This is the curved quadratic pushforward to which the projection information must be connected.

## 4. Pinned completed result applied on the ruled side

The required pinned Claude source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

proves the ruled one-sheet estimate (Theorem C): for every exact-rank-three signature `(+,+,-)` form with the three absolute eigenvalues at least one, the density on the one-sheet side is bounded by `pi sqrt(2)`. Its proof uses line rulings of the hyperboloid and the cap-two **two-dimensional product marginal**, not independence of the spectral coordinates.

Our matrix has eigenvalues `{1,1,-1}` after an orthogonal spectral diagonalization, so this theorem applies directly and gives

`boxed: p_Q(s)<=pi sqrt(2) for a.e. s>=0`.                        (4.1)

Thus the actual two-dimensional projection theorem pays one full curved side of this near-coloop family. The remaining side is the place where a generic planar density cap by itself is not enough; source provenance is still needed.

## 5. Aggregate two source banks before curvature: global bound <211

Condition on the independent source objects `X1,Y4`. The remaining variables

`X0,Y2,Y3`                                                        (5.1)

are independent. In these variables the conditional form has arbitrary affine and constant terms plus the quadratic block

`B=[[0, sqrt(c(1-h)), 0],
    [sqrt(c(1-h)), 2 t2 sqrt(1-h), q sqrt(1-h)],
    [0, q sqrt(1-h), 1/2]]`.                                     (5.2)

The determinant has a decisive cancellation:

`det B=-c(1-h)/2`.                                                (5.3)

The terms involving `t2` and `q` disappear from the determinant because the first row has only one nonzero off-diagonal entry. This is exactly why the weak near-coloop slope leakage can be retained rather than discarded.

From (3.3), set

`Z2=sqrt(2)Y2`, `Z3=sqrt(2)Y3`.                                  (5.4)

Then `X0,Z2,Z3` are independent cap-one variables. The rescaled quadratic block is the congruence

`B'=D B D`, `D=diag(1,1/sqrt(2),1/sqrt(2))`,                     (5.5)

hence

`|det B'|=c(1-h)/8`.                                              (5.6)

Because `c>63/64` and `1-h=127/128`,

`|det B'| > (63*127)/(64*128*8)=8001/65536`.                    (5.7)

Now apply the completed designated-partner theorem

`QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`,

source

`yspennstate/math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T202347Z-account03-B16-QFORM-r15/REPORT.md`.

It states that three independent cap-one variables with any invertible symmetric quadratic block `B'` and arbitrary affine translation have

`||p||_infinity <= C3 |det B'|^(-1/3)`,

`C3=16 sqrt(30) 2^(1/4)=104.216889989...`.                       (5.8)

The estimate is uniform in the conditioning, so averaging gives

`||p_Q||_infinity
 <= C3 [8/(c(1-h))]^(1/3)
 < C3 (65536/8001)^(1/3)
 =210.07933258...
 <211`.                                                           (5.9)

This proves the new family-level theorem:

### `QFORM-GATEFAIL-NEARCOLOOP-BANK-AGGREGATE-v1`

For every `0<a<1/64`, every integer `m>=64`, and every independent original-coordinate input law with one-dimensional density caps at most one, the exact-rank-three target family (2.1)--(2.6) has

`boxed: ||p_(X^TAX)||_infinity<211`.                              (5.10)

The conclusion uses only genuine original-source independence. It does not assume moments, bounded support, log-concavity, identical laws, or independence of projected coordinates.

## 6. Atomwise reciprocal determinant payment loses `m^(2/3)`

The aggregation in Section 5 is not cosmetic. Instead of the aggregate variables `Y2,Y3`, select one physical coordinate from bank 2 and one from bank 3, together with the hub coordinate `X0`, while conditioning on all other original coordinates. The corresponding physical `3 x 3` block is obtained from (5.2) by scaling its second and third coordinates by `m^(-1/2)`. Therefore

`|det B_phys|=c(1-h)/(2m^2)`.                                    (6.1)

Applying the same partner physical-triple theorem directly to that one physical triple yields only

`||p_Q||_infinity
 <= C3 [2m^2/(c(1-h))]^(1/3)`,                                   (6.2)

which grows as `m^(2/3)`.

By contrast, aggregating the two disjoint original-coordinate banks first produces the uniform block (5.6) and the constant bound (5.9). The ratio between the atomwise and aggregate determinant certificates is exactly

`(m^2/4)^(1/3)=m^(2/3)/4^(1/3)`.                                 (6.3)

Hence **single-physical-triple reciprocal payment is not a uniform compiler even inside the true near-coloop gate-failure chamber**. A proof has to aggregate source banks before paying determinant curvature whenever such bank structure is present.

This is a mechanism obstruction, not a counterexample to QFORM.

## 7. What this says about projection-product interaction

There are three distinct facts and they must not be conflated.

1. The two-dimensional product projection theorem gives the robust joint cap (3.4), including after orthogonal mixing.
2. A generic orthogonal mix of `(Y2,Y3)` need not be independent, so one cannot feed (3.4) into an argument requiring independent projected coordinates.
3. The global curved estimate (5.9) is recovered because the original source decomposition tells us how to **unmix** to the two disjoint bank aggregates before applying the three-variable theorem.

On the ruled side, item 1 alone is enough because the geometry converts the coarea integral into line integrals that are exactly two-dimensional marginals; that is (4.1). On the opposite side, item 1 alone has no generic indefinite-receiver theorem, so item 3 is the relevant source-level invariant. This is the exact interface the B16 assignment asks to quantify.

## 8. Remaining implication

The full conjecture is still open. The new construction removes only an explicit subfamily of the true near-coloop collar. The unresolved structural bridge is sharper:

`QFORM-TRUE-NEAR-COLOOP-BANK-COMPILER-v1`.

Given a general exact-rank-three r28 residual frame with `c>63/64`, all residual transverse leverages `<1/64`, and duplicated-gate failure, prove one of the following with universal quantitative constants:

- two (or a bounded number of) disjoint original-coordinate source banks carry enough transverse Gram mass that their normalized aggregate variables form a uniformly nondegenerate conditioned three-variable receiver; or
- the absence of such a bank decomposition forces a genuinely shared-bank geometry that triggers mixed Fresnel, cross-volume, or an equivalent source-first estimate.

The explicit family shows why searching only for one good physical triple is too narrow: all analogous physical triples decay as the diffuse bank size grows, while two bank aggregates remain uniformly good. Arbitrary additional spectrum remains a separate full-target interface and is not removed here.

## 9. Source ledger and status

Owner target/control: QFORM only, revision `2026-09-22.15`, full claim open.  
Pinned Claude product/Fourier/ruled source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.  
Latest compatible designated partner used structurally: account03/B16 r28 `QFORM-XOR-BALANCED-BASIS-v1` at `math-open-problems@5f7b47acd0c385e3c65a9c20c808eca6a5527e71`.  
Completed partner theorem used quantitatively: account03/B16 r15 `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1` at `math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`.

Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.  
No post-rotation independence, conditional projection-height supremum, hidden moment/support assumption, or small-quadratic-perturbation deletion is used.
