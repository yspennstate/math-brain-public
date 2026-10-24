SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-24T00:52:02Z.
attacking: the exact rank-one overlap-two collar with arbitrary same-leaf curvature, by identifying the full anchored third-compound matrix and routing physical star concentration to an already-paid principal-triple receiver.

# account01/B09 — anchored compound matrix and concentration-to-diffusion reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism / GEOMETRY  
Run: `20260924T005202Z-account01-B09-QFORM-auto11`  
Status: **ESSENTIAL STEP APPLIED / NEW STRUCTURAL-ANALYTIC REDUCTION / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. This report treats the exact rank-one physical-pair / rank-one pair-to-leaf collar while retaining an **arbitrary symmetric quadratic block on the same active leaf coordinates**. The new payment is for the physically concentrated star branch; the complementary branch is reduced to a quantitative diffuse-star condition. No leaf-curvature term is deleted or called a small random perturbation.

## 1. Source-pinned premises

Fresh control at startup was `yspennstate/math-research-brain/main@d8582d7c48a489ed23147d480fed5c21991fa1ee`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no account01/B09 pause or stop.

The full target and continuity claims are still OPEN in the current `CLAIMS.json`. Live corrections used here include the failure of law-uniform pointwise quadratic-phase decay, the prohibition on post-rotation independence, the failure of naive fiber-sup dimension-free bounds, and the fact that aggregate Frobenius minor mass does not by itself furnish a uniformly large single physical minor.

Two immutable mathematical dependencies were read in full before use:

1. `QFORM-PHYSICAL-TRIPLE-DET-v1`, source
   `yspennstate/math-open-problems@bf4ba08b75ab774aef671c62ba4898a371059c0d`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T170850Z-account02-B01-qform-r25/REPORT.md`.
   For every literal physical triple `T` with `d=|det A[T,T]|>0`, conditioning all outside original coordinates gives
   `||p_Q||_infinity <=216 d^(-1/3)`, uniformly over the induced affine term. Continuity is not claimed.

2. The designated partner account02/B09 r15 theorem, source
   `yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T224553Z-account02-B09-QFORM-r15/REPORT.md`.
   At an exact rank-one physical pair, its collinear zero-active-leaf star theorem gives
   `||p_Q||_infinity <=6 |tau|^(-1/3)||A[I,H]k||_2^(-2/3)`
   and in particular `<=6 Omega_(2,H)^(-1/6)` when the overlap-two packet is positive.

## 2. New exact identity: the full anchored compound matrix

Let `H={h1,h2}` be a literal pair of original coordinates and `L=H^c`. Assume only that the pair-to-leaf cross block has rank one, and write

`B=A[H,H] in R^(2x2)`,
`A[H,L]=g r^T`,
`D=A[L,L]`,

where `g in R^2`, `r in R^L`. The normalization of `g,r` is irrelevant. Set

`delta=det B`,
`kappa=g^T adj(B) g`.

Define the `L x L` anchored third-compound matrix

`N_H(i,j)=det A[H union {i}, H union {j}]`.

### Theorem `QFORM-PAIR-ANCHORED-COMPOUND-MATRIX-v1`

For every symmetric `B,D` and every rank-one cross factorization above,

`boxed: N_H = delta D - kappa r r^T.`                           (2.1)

This identity is valid whether `B` is invertible, singular, definite, indefinite, or zero.

### Proof

For fixed leaves `i,j`, the relevant `3 x 3` block is

`[[ B,        g r_j ],
  [ r_i g^T,  D_ij  ]]`.

The size-two block determinant expansion, valid algebraically without invertibility, is

`det [[B,u],[v^T,d]] = det(B)d - v^T adj(B)u`.

Substituting `u=g r_j`, `v=g r_i` gives

`det A[H union {i},H union {j}]
 = delta D_ij - r_i r_j g^T adj(B)g
 = delta D_ij-kappa r_i r_j`.

This is (2.1). QED.

When `delta!=0`, (2.1) is exactly the Schur-complement identity

`N_H=delta [D-(kappa/delta)rr^T]`.

The singular endpoint is qualitatively different and is the reason this identity is useful.

## 3. Exact rank-one pair: overlap-two currency is completely blind to leaf curvature

Assume now that `B` has rank one and is nonzero. Then `delta=0`. Write

`B=tau ell ell^T`,

where `tau!=0`, and let `k` be a unit vector spanning `ker B`. In two dimensions

`adj(B)=tau k k^T`,

so

`kappa=tau (k^T g)^2`.

The identity (2.1) collapses to

`boxed: N_H=-kappa r r^T`,                                    (3.1)

**independently of the arbitrary leaf block `D`**.

Consequently, if

`P_H = sum_i det A[H union {i},H union {i}]^2`

is the principal-triple square mass anchored on `H`, and

`Omega_(2,H)=sum_(i!=j) det A[H union {i},H union {j}]^2`

is the ordered overlap-two packet, then

`boxed: P_H = kappa^2 sum_i r_i^4`,                            (3.2)

`boxed: Omega_(2,H)
 = kappa^2[(sum_i r_i^2)^2-sum_i r_i^4]`,                     (3.3)

and therefore

`boxed: P_H+Omega_(2,H)=kappa^2 ||r||_2^4`.                   (3.4)

Thus no argument using only this anchored overlap-two packet can control the same-bank leaf curvature `D` at a singular pair: `D` literally disappears from the entire anchored compound matrix. This is a structural limitation on the intermediate mechanism, not a counterexample to the QFORM target.

## 4. New analytic collar payment: physical star concentration is harmless even with arbitrary leaf curvature

Assume `Omega_(2,H)>0`; then `kappa!=0` and `r!=0`. Define the normalized physical star leverage

`q = max_i r_i^2 / ||r||_2^2`.

Let

`m_H=max_i |det A[H union {i},H union {i}]|`.

By (3.1),

`m_H=|kappa| max_i r_i^2
    =q |kappa| ||r||_2^2
    =q sqrt(P_H+Omega_(2,H))`.

Hence

`boxed: m_H >= q sqrt(Omega_(2,H)).`                           (4.1)

Every maximizing `H union {i}` is a literal original-coordinate principal triple. The completed physical-triple determinant theorem therefore gives the following branch with **no assumption whatsoever on `D`**.

### Corollary `QFORM-SINGULARPAIR-HIGHSTAR-ARBITRARY-CURVATURE-v1`

If the exact rank-one pair / rank-one cross geometry above satisfies

`Omega_(2,H)>=omega>0`, `q>=eta>0`,

then the full ambient quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=216 eta^(-1/3) omega^(-1/6).`                              (4.2)

The identical constant multiplies interval length:

`P{Q in I}<=216 eta^(-1/3)omega^(-1/6)|I|`.

Continuity is not claimed by this branch.

### Proof

Equation (4.1) gives a physical principal triple with determinant at least `eta sqrt(omega)`. Apply `QFORM-PHYSICAL-TRIPLE-DET-v1`, conditioning every outside coordinate. Its allowance for arbitrary induced affine terms retains all of the same active leaf curvature. QED.

At the global-overlap scale `omega=1/4`, taking `eta=1/16` gives the explicit dichotomy

`boxed:
 Omega_(2,H)>=1/4
 => [ ||p_Q||_infinity <686 ]
    or [ q<1/16 ].`                                           (4.3)

Indeed the paid-branch constant is

`216*(1/16)^(-1/3)*(1/4)^(-1/6)
 =216*32^(1/3)
 =685.7572544502...`.

This is the main gain of the run: **the physically concentrated exact singular-pair collar is closed even for completely arbitrary same-bank leaf curvature**. Any still-unpaid fixed-pair singular collar with overlap-two mass at least `1/4` is automatically a genuinely diffuse star with `q<1/16`.

Equivalently, if every anchored physical principal triple satisfies `|det|<d`, then

`boxed: q < d / sqrt(Omega_(2,H))`.                            (4.4)

So a failure of the principal-triple receiver quantitatively forces diffuseness rather than leaving an unstructured singular endpoint.

## 5. Target-valid stress family: arbitrary dense leaf curvature is invisible to the singular-pair packet

For `m>=2`, let

`B=diag(1,0)`, `g=e2`,
`r=(1/sqrt(m),...,1/sqrt(m)) in R^m`.

Choose any unit vector `v perpendicular to r` and any real `t`, and set

`D=t v v^T`.

Then the active matrix is

`A_t = [[1,0,0],
       [0,0,r^T],
       [0,r,t vv^T]]`.

The orthogonal decomposition into the first hub, `span{second hub,r}`, `span{v}`, and the remaining leaf orthocomplement gives the exact nonzero spectrum

`{1,+1,-1,t}`

(with `t=0` simply removing the fourth nonzero eigenvalue). Thus this is target-valid for every real `t`.

Nevertheless the anchored compound matrix is, for every `t`,

`N_H=-rr^T`,

and

`P_H=1/m`,
`Omega_(2,H)=1-1/m`,
`q=1/m`.                                                       (5.1)

Hence arbitrarily large, dense same-leaf curvature can coexist with exactly the same singular-pair overlap-two ledger. This proves that the next diffuse-star step really must spend the curvature through another overlap/crossing mechanism or prove a direct entangled star-curvature inequality; it cannot reconstruct `D` from `Omega_(2,H)`.

For `m=64`, every anchored principal triple determinant equals `1/64<1/32`, while

`Omega_(2,H)=63/64`, `q=1/64<1/16`.

This is a literal regression of the new concentration-to-diffusion boundary.

## 6. Required account02/B09 result applied to an actual inequality

Use the preceding family at `t=0` and `m=64`. It is exactly the designated partner's collinear rank-one star:

`B=diag(1,0)`,
`A[i,h1]=0`,
`A[i,h2]=1/8`,
`A[I,I]=0`.

Its spectrum is `{1,+1,-1}` plus zeros, so it satisfies the owner target. The partner theorem has

`tau=1`,
`||A[I,H]k||_2=||r||_2=1`.

Therefore the completed account02/B09 r15 result gives the actual target inequality

`boxed: ||p_Q||_infinity <=6`,                                (6.1)

and

`boxed: P{Q in J}<=6 |J|`.                                   (6.2)

This zero-curvature instance lies on the **diffuse** side of the new dichotomy: `q=1/64`, while `Omega_(2,H)=63/64`. Thus the partner result genuinely pays one point of the remaining diffuse chamber; the arbitrary-`t` family in section 5 shows exactly what extra same-bank curvature is still unaccounted for.

## 7. Scope and first unpaid implication

This run does **not** solve the unrestricted conjecture and does not prove continuity on the new principal-triple branch. It also does not claim that small `q` alone pays arbitrary `D`.

The exact singular rank-one-pair/rank-one-cross collar is now divided rigorously as follows:

1. `q>=1/16` with `Omega_(2,H)>=1/4`: paid at `<686`, for arbitrary same-leaf curvature.
2. `q<1/16`: a genuinely diffuse star. At `D=0` the designated partner theorem pays it directly; for general `D`, the packet `Omega_(2,H)` contains no information about `D` by (3.1).

The first unpaid B09 implication is therefore

`QFORM-SINGULARPAIR-DIFFUSESTAR-CURVATURE-EXIT-v1`:

> In the exact singular-pair / rank-one-cross branch with `q<1/16`, either spend arbitrary same-active-leaf curvature through a disjoint physical crossing / one-shared overlap / mixed-hub receiver, or prove a direct diffuse-star curvature inequality. The exact identity `N_H=-kappa rr^T` must be respected: overlap-two mass alone cannot supply the missing curvature information.

A near-rank-one physical pair remains a separate quantitative passage. For `det B!=0`, identity (2.1) becomes the exact Schur relation `N_H=det(B)[D-(kappa/det(B))rr^T]`; no inference treats a small determinant as a small random perturbation.

No valid full-target counterexample was found in this run.
