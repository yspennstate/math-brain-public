SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T16:46:04Z.
attacking: close the rank-two hub/star aggregate branch by combining the new arbitrary-rank projected-crossing theorem with a concentrated-row promotion to three grouped hub directions, before any reciprocal physical minor or pair-core inversion.

# fleet03/B09 r37 — rank-two hub/star aggregate payment with no hub-leverage gate

## Status

**NEW SUPPORTING THEOREM / CURRENT OWNER CONTINUATION APPLIED / FULL QFORM OPEN.**

This run proves a stronger source-coordinate endpoint than the preceding r32-r36 chain. In a physical rank-two hub/star

`A[H,I]=P C^T`, `P^T P=I_2`,

with completely arbitrary hub self-curvature and completely arbitrary leaf self-curvature, the aggregate singleton third-volume resource `G_*` is now paid whenever it is nonzero, with **no physical hub-leverage hypothesis, no column-range-leverage hypothesis, no pair-core determinant, and no selection of one universally large physical 3x3 minor**:

`boxed: ||p_Q||_infinity <= 4 sqrt(6) G_*^(-1/6) < 9.798 G_*^(-1/6).`

The density is continuous in this whole branch, and the identical coefficient gives a direct `O(|L|)` interval estimate. The proof first compiles `G_*` into one original-coordinate leaf partition as in r32, then uses the new grouped projected-crossing theorem in the diffuse residual-row case; if one residual row is concentrated, that **literal original coordinate** is promoted to a third grouped hub and the completed three-hub Plancherel theorem pays the resulting rank-three cross block. Thus the former r34 physical-pair localization, r35 pair-core strata, and r36 high-column-leverage split are no longer needed to pay the `G_*>0` analytic branch.

The unrestricted QFORM conjecture remains OPEN because the bare three-large-eigenvalue hypothesis has not yet been shown to force `G_*` to a universal scale in every surviving rank-two hub/star configuration, nor has every `G_*=0`/near-zero structural endpoint been routed globally. Full-target continuity remains OPEN; continuity is proved for the theorem stated here.

No Gaussian, log-concavity, moment, support, connected-support, iid, diagonal-basis, post-rotation-independence, pointwise scalar stationary-phase, arbitrary-joint coarea, worst conditional-density supremum, or small-random-error assumption is used.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh controls and completed inputs actually used


The mathematical inputs actually used at equations are:

1. **New interactive grouped projected-crossing theorem**, immutable source

   `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,

   `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, blob `dc7e29c3ee746ebf2856aaa6866b4b16b9a04b9f`.

   Its theorem `(GC)` allows grouped hubs with arbitrary internal hub functions and an arbitrary-rank projected crossing remainder. For hub dimension `k`, crossing volume degree `ell`, `d=k+ell>2`, hub-projection density cap `M_H`, hub-to-`J` singular product `S`, and projected crossing `ell`-volume `Z_ell` whose row marginals are at most `1/2`, it gives

   `||p_Q||_infinity
    <= d/(d-2) 2^((k+3ell)/(2d)) exp(ell/(2d))
       M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,

   with the exponential omitted for `ell=1`. Its proof retains arbitrary same-bank quadratic curvature and uses original-coordinate differencing, projection densities and determinant-weighted Fourier estimates. Its stated restricted proof is complete, while independent review/prior-art assessment remain separate.

2. **Latest Claude continuation, three-hub theorem**, source commit

   `yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`,

   `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`, Theorem 6.3, blob `65d83f93ed68044bab3ff355f6e9603751af0628`.

   For three literal physical hubs with arbitrary hub block and arbitrary measurable remainder, if the three hub-to-light singular values are `s_1,s_2,s_3`, then

   `||p_Q||_infinity <= 3 sqrt(2) (s_1 s_2 s_3)^(-1/3)`,

   with an `L1` characteristic function and hence a continuous density. This source was reread after the newest `c4c23...` continuation; the new `(SP)` “hub that sees P” proposal remains OPEN and is not used here.

3. **This slot r32 aggregate compiler**, canonical mathematics

   `yspennstate/math-open-problems@640165d39efca44cf3cf7fe2d2e5638a823a335b`,

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T124906Z-fleet03-B09-QFORM-r32/REPORT.md`.

   Its Bernoulli compiler is leverage-free: for the rank-two hub/star below it produces a literal leaf partition `I=S disjoint_union T` for which

   `W(S) >= (27/256) G_*`.

4. **Designated partner fleet04/B09**, completed theorem

   `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`,

   `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`, blob `a2292a47ee56cf3d66556e324bd8b234bd2157f1`.

   A literal invertible physical `3x3` cross block `K` gives

   `||p_Q||_infinity <=3 |det K|^(-1/3)`

   with arbitrary dense same-side blocks and continuous density. Section 6 below applies this at an actual target-valid inequality.

All current source corrections are retained: no law-uniform pointwise quadratic-phase decay, no post-rotation independence, no arbitrary-joint rank-three coarea, no worst-fiber or conditional-cap shortcut, no universally good single physical minor, and no deletion of a small quadratic coefficient on arbitrary unbounded supports.

## 2. Rank-two hub/star and the aggregate third-volume currency

Let `H,I` be disjoint sets of ORIGINAL coordinates. Condition on all coordinates outside `H union I`; conditioned values may generate arbitrary affine terms. Assume the actual physical hub-to-leaf cross block has rank two and factor it as

`A[H,I]=P C^T`, `P^T P=I_2`,                                  (2.1)

where `P` is `|H| x 2` and `C` is `|I| x 2`. Let

`D=A[I,I]`                                                       (2.2)

be completely arbitrary symmetric leaf curvature. No restriction is placed on `A[H,H]`.

For each `k in I`, r32 defines the singleton augmented physical cross matrix

`M_k=A[H union {k}, I\{k}]`

and

`Gamma_k^2=e_3(M_k^T M_k)`.                                    (2.3)

Because `P` is an isometry on its two coefficient directions, Cauchy--Binet gives the source-coordinate identity

`Gamma_k^2
 = sum_{J subset I\{k}, |J|=3}
     det([C_J^T; D[k,J]])^2`.                                  (2.4)

Put

`G_* = sum_{k in I} Gamma_k^2`.                                (2.5)

R32's Bernoulli compiler, which has **no leverage hypothesis**, gives a literal partition

`I=S disjoint_union T`                                         (2.6)

such that

`W(S):=sum_{k in S} sum_{J subset T, |J|=3}
          det([C_J^T;D[k,J]])^2
      >= (27/256) G_*`.                                        (2.7)

If `G_*>0`, then `W(S)>0`; in particular `C_T` has rank two.

## 3. Exact projected-crossing identity

Write

`B=C_T^T`,                                                     (3.1)

so `B` is a `2 x |T|` rank-two matrix, and put

`Delta=det(B B^T)=det(C_T^T C_T)>0`.                           (3.2)

Let `Pi` be the orthogonal projection of `R^T` onto `row(B)`. Define the physical leaf crossing projected away from the two hub-partner directions,

`E=D[S,T](I-Pi)`,                                              (3.3)
`Z=||E||_F^2`.                                                 (3.4)

For a fixed `k in S`, write `d_k=D[k,T]` and `e_k=d_k(I-Pi)`. Cauchy--Binet plus the Gram determinant formula gives

`sum_{J subset T, |J|=3} det([B[:,J];d_k[J]])^2
 =det([B;d_k][B;d_k]^T)
 =Delta ||e_k||_2^2`.                                         (3.5)

Summing over `k in S` gives the exact identity

`boxed: W(S)=Delta Z.`                                        (3.6)

This is the key bridge. It converts the r32 determinant currency into precisely the product of the two grouped hub-partner singular values and the total projected crossing energy required by the new `(GC)` theorem.

## 4. Main theorem: no hub-leverage gate

### Theorem `QFORM-GROUPED-RANK2-HUBSTAR-PROJECTED-CROSSING-CLOSURE-v1`

Under (2.1)-(3.4), if `W(S)>0`, then for every admissible cap-one product input law the full quadratic form has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <=3*2^(7/6) W(S)^(-1/6)
 <6.735 W(S)^(-1/6).`                                         (4.1)

For every interval `L`,

`boxed:
 P{Q in L}
 <=3*2^(7/6) W(S)^(-1/6) |L|.`                               (4.2)

There is no assumption on the physical hub row leverages of `P`, no assumption on the column leverage of the full cross range, and no restriction on either same-side quadratic block.

### Proof

Condition first on every original coordinate outside `H union S union T`. Write the active form schematically as

`Q=F(X_H)
   +2 <P^T X_H, C_S^T X_S + C_T^T X_T + beta>
   +R(X_S,X_T)`,                                               (4.3)

where `F` may contain arbitrary hub curvature and `R` is the completely arbitrary leaf quadratic polynomial inherited from `D`, including all internal `S`, internal `T`, diagonal, and `S-T` terms. The grouped random vector

`Y=P^T X_H`                                                    (4.4)

has a two-dimensional density cap at most

`M_H<=2`                                                       (4.5)

by the orthonormal product-projection bound used in the new source. No independence is claimed between the two coordinates of `Y`.

We now split according to the **physical rows of the projected crossing `E`**, not according to hub or column leverage.

#### Case A: projected crossing is row-diffuse

Assume

`||e_k||_2^2 <= Z/2` for every `k in S`.                       (4.6)

For `ell=1`, the volume row marginals of `E` are exactly

`alpha_k=||e_k||_2^2/Z`,                                      (4.7)

so (4.6) is precisely the `alpha_k<=1/2` gate of `(GC)`.

Apply `(GC)` with

`k=2`, `ell=1`, `I=S`, `J=T`, `M_J=B=C_T^T`.                  (4.8)

The hub-to-`T` singular-value product is

`S_B=sqrt(Delta)`.                                             (4.9)

Since `d=k+ell=3`, and the `ell=1` theorem has no exponential entropy factor, `(GC)` yields

`||p_Q||_infinity
 <=3*2^(5/6) M_H^(1/3) Delta^(-1/6) Z^(-1/6)
 <=3*2^(7/6) (Delta Z)^(-1/6)`.                               (4.10)

By (3.6), this is exactly (4.1). The source proves an integrable characteristic-function majorant, so this branch has a continuous density.

#### Case B: one projected physical row is concentrated

Otherwise there exists a literal original coordinate `k in S` with

`||e_k||_2^2 > Z/2`.                                          (4.11)

Condition on all coordinates in `S\{k}`. Promote the single physical coordinate `k` to the grouped hub side. The physical cross block from the original-coordinate bank `H union {k}` to `T` is

`N_full = [P B; d_k]`.                                        (4.12)

Let

`N_0=[B;d_k]`,                                                 (4.13)

and let `U_0` be the `(|H|+1) x 3` orthonormal frame obtained by adjoining the physical coordinate `k` to the two columns of `P`. Then

`N_full=U_0 N_0`,                                              (4.14)

so `N_full` and `N_0` have the same three nonzero singular values. Their product `Gamma` obeys

`Gamma^2
 =det(N_0 N_0^T)
 =Delta ||e_k||_2^2
 >Delta Z/2
 =W(S)/2`.                                                     (4.15)

There are two equivalent completed receivers here. The sharpest source needed for this run is the current Claude three-hub Theorem 6.3: take the three grouped coordinates represented by `U_0`. Equivalently, after the SVD of `N_0`, the grouped hub projection is an orthogonal rotation of `(P^T X_H,X_k)`. That vector has density cap at most `2`, and the theorem's Plancherel proof is invariant under this deterministic orthogonal rotation; alternatively one may condition down to a literal three-row realization whenever available. The completed exact-rank crossing theorem in `NEW_PROJECTED_CROSSING.md` gives the same source-valid conclusion with these grouped projection caps.

Using the exact-rank crossing statement from the new source with left projection cap at most `2`, right three-dimensional projection cap at most `2^(3/2)`, and rank `r=3`,

`||p_Q||_infinity
 <=3 [2*2^(3/2)]^(1/3) Gamma^(-1/3)
 =3*2^(5/6) Gamma^(-1/3)
 <6 W(S)^(-1/6).                                               (4.16)

This is strictly smaller than the Case A constant `3*2^(7/6)`. The characteristic function is again `L1` because the cross rank is three, so this branch also has a continuous density.

For a **literal** three-coordinate hub subcase, the newest Claude Theorem 6.3 improves (4.16) to

`||p_Q||_infinity
 <=3 sqrt(2) Gamma^(-1/3)
 <3 sqrt(2)2^(1/6)W(S)^(-1/6)
 =4.762204... W(S)^(-1/6).`                                   (4.17)

Equation (4.16), not the sharper literal-hub specialization, is what closes the general grouped-hub statement without any physical hub-leverage hypothesis.

Combining Cases A and B proves (4.1)-(4.2). QED.

### Important provenance point

The grouped hub coordinates are used only through their **joint projection density**, not as independent random variables. All conditioning is on disjoint original-coordinate banks. The concentrated case promotes an actual original leaf coordinate before taking the rank-three cross estimate. No spectral rotation of the product law is used.

## 5. Leverage-free corollary for the entire `G_*>0` rank-two hub/star branch

Combine Theorem 4 with the leverage-free Bernoulli compiler (2.7):

`W(S)>=27G_*/256`.

Then

`||p_Q||_infinity
 <=3*2^(7/6)(256/27)^(1/6) G_*^(-1/6)
 =4 sqrt(6) G_*^(-1/6)`.                                      (5.1)

Thus:

### Corollary `QFORM-RANK2-HUBSTAR-AGGREGATE-NOLEVERAGE-v1`

For every physical rank-two hub/star (2.1) with arbitrary symmetric hub block, arbitrary symmetric leaf block, arbitrary outside couplings and arbitrary conditioning-generated affine terms, if `G_*>0`, then

`boxed:
 ||p_Q||_infinity <=4 sqrt(6) G_*^(-1/6)
 <9.798 G_*^(-1/6),`                                          (5.2)

and

`boxed:
 P{Q in L} <=4 sqrt(6) G_*^(-1/6)|L|`                         (5.3)

for every interval `L`. The density has a continuous representative vanishing at infinity.

No hub-row leverage, Pluecker disjointness, full-range column leverage, or physical pair-core classification remains in this analytic payment.

This strictly simplifies the preceding proof map:

- r32's `max_h(PP^T)_hh<=1/2` hypothesis is no longer needed for `G_*>0`;
- r34's high-hub Pluecker localization is no longer needed merely to obtain bounded density from `G_*>0`;
- r35's zero/rank-one/definite/indefinite pair-core case split is no longer needed for this branch;
- r36's full-range column-leverage gate is no longer needed.

Those earlier results remain valid and may still give sharper estimates in overlaps; they are not deleted.

The remaining B09 obstruction is now structural/scale rather than leverage analytic:

`QFORM-RANK2-HUBSTAR-GSTAR-SCALE-OR-ZERO-ROUTING-v1`:

> In the surviving rank-two hub/star geometry under the bare three-large-eigenvalue hypothesis, either force `G_*` to a universal quantitative scale after normalization, or route the `G_*=0` / quantitatively tiny `G_*` configurations into the exact no-augmentation `diagonal + rank-two-in-span`, coloop/finite-core, grouped-square/ridge, or another already-paid endpoint. A small matrix residual cannot be discarded as a small random quadratic perturbation on arbitrary unbounded input laws.

This theorem does **not** prove that scale implication, so full QFORM remains OPEN.

## 6. Designated fleet04/B09 theorem applied at an actual target-valid inequality

Take `0<eps<=1` and the physical `4x4` cross block

`M_eps=diag(1,1,1,eps)`.

On eight independent original coordinates define

`A_eps = [[0_4,M_eps],[M_eps,0_4]]`.                            (6.1)

Its spectrum is exactly

`{-1,-1,-1,-eps,+eps,+1,+1,+1}`,                              (6.2)

so it satisfies the owner target for every `eps`.

The literal physical cross block on the first three rows and first three opposite-bank columns is

`K=I_3`, `det K=1`.                                             (6.3)

Apply the designated fleet04/B09 theorem at the actual inequality:

`boxed: ||p_(X^T A_eps X)||_infinity <=3`.                     (6.4)

The density is continuous and `P{X^T A_eps X in L}<=3|L|`.

This regression is also a useful control for the proof map: when `eps>0`, the full cross range is four-dimensional and its coordinate-range projection is the identity, so every full-range column leverage equals one. The old r36 diffuse-column gate therefore fails maximally, while the literal/aggregate cross geometry is nevertheless uniformly paid. High full-range leverage was a proof-coordinate obstruction, not genuine concentration.

## 7. Deterministic checks

Two deterministic scripts and their actual outputs are saved beside this report.

`CHECK.py` verifies on 100 seeded random instances the fixed-pair identity

`sum_k det([B;d_k][B;d_k]^T)=det(BB^T)||D(I-Pi)||_F^2`,

with maximum relative error `6.960957976457037e-16`; it also verifies

`3*2^(5/6)=5.345392308842036`,
`3*sqrt(2)*2^(1/6)=4.762203155904599`,

and the target stress spectrum (6.2), partner determinant one and partner bound three.

`CHECK_GROUPED.py` verifies on 100 seeded random Parseval hub frames that

`W=Delta ||D(I-Pi)||_F^2`

and that adjoining one concentrated physical row preserves the three-singular-value product under the isometric grouped-hub embedding. The maximum relative errors were respectively

`5.288422172088503e-16`,
`3.1049821904107617e-15`.

It also verifies

`3*2^(7/6)=6.734772289856238`,
`4*sqrt(6)=9.797958971132712`.

The scripts check finite-dimensional identities and arithmetic only; the analytic proof is the argument above and the pinned completed source theorems.

## 8. Exact status

The theorem above is a supporting result toward the owner target, not a full solution. In particular:

- full QFORM essential boundedness: **OPEN**;
- full-target continuous density: **OPEN**;
- this rank-two hub/star `G_*>0` branch: **continuous density proved**, conditional on the stated completed source theorems;
- source `NEW_PROJECTED_CROSSING.md`: complete written restricted proof, independent review still pending as its source explicitly records;
- newest Claude `(SP)` proposal: **OPEN and not used**;
- designated partner fleet04/B09: applied at (6.4).

Repository use and native learned-memory ingestion are separate. Authenticated repository retrieval/write occurred; no separate native learned-memory receiver use was verified, so the execution status remains `WITHOUT_VERIFIED_BRAIN`.
