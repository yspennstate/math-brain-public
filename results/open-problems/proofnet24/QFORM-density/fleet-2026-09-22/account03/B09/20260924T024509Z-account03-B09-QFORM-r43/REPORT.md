SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T02:45:09Z.
attacking: the nonphysical-kernel rank-two endpoint by Schur-completing a genuine physical coordinate and computing exactly how the grouped rank-two overlap currency survives as residual physical two-volume before any reciprocal minor is selected.

# account03/B09 r43 — physical Schur compiler for a nonphysical rank-two kernel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations  
Run: `20260924T024509Z-account03-B09-QFORM-r43`  
Status: **NEW SUPPORTING THEOREM / NONPHYSICAL-KERNEL SUBBRANCH PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and scope

Fresh control at startup was `yspennstate/math-research-brain@22755523d8f88f79b7b3f066007469d441b994b4`, OWNER CONTROL revision `2026-09-22.15`. QFORM remains the sole research target and no account03/B09 pause or reassignment was present. The current assignment remains the bilinear-block mechanism in original coordinates.

The unrestricted target is unchanged: independent real ORIGINAL coordinates with marginal densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. Nothing below assumes moments, support bounds, connected support, Gaussianity, log-concavity, iid laws, a diagonal eigenbasis, or independence after rotation.

The live correction package was reread. In particular this report does not use law-uniform pointwise van-der-Corput decay, arbitrary-joint rank-three coarea, a positive moment of a worst conditional projection density, a dimension-growing fiber supremum, deletion of a small coefficient on unbounded inputs, or the claim that aggregate determinant mass contains one universally large physical minor.

The immediate relevant predecessor is account03/B09 r42/r43. The adaptive grouped rank-two theorem gives, for a physical left triple `L`, a right bank `J`, rank-two cross block `C=A[L,J]`, unit `n in ker(C^T)`, `a=Pn`, and `Delta=sigma_1(C)sigma_2(C)`, the overlap currency

`V=Delta^2 ||a||_2^2`                                              (1.1)

and a logarithmic endpoint in the general nonphysical-kernel case. The physical-kernel follow-up removes that logarithm when `n` itself is an original coordinate. The unresolved local issue is therefore exactly the nonphysical kernel.

A second completed input is account01/B03 `QFORM-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1`, source

`yspennstate/math-open-problems@588fa418bc29d4b889fcbbee2b61370234ceef37`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T175336Z-account01-B03-QFORM-r30/REPORT.md`.

For an exact two-row physical crossing matrix `M`, let

`S=sqrt(det(MM^T))>0`.                                             (1.2)

Its exact-rank-two Plancherel branch gives

`|phi_R(t)| <= min{1, pi sqrt(2) S^(-1/2)|t|^(-1)}`.              (1.3)

Consequently

`sup_s E|R-s|^(-1/2) <= 2^(11/4) S^(-1/4)`.                      (1.4)

If one further genuine original coordinate completes as `d[X+h]^2+R`, then

`||p_Q||_(infinity,ess) <= 2^(11/4)|d|^(-1/2)S^(-1/4)`.          (1.5)

This is a linear `O(|I|)` small-ball receiver. Continuity is not claimed by the square/half-Riesz interface.

The newest account02/B09 source, `20260924T021301Z-account02-B09-QFORM-r16`, is also retained: an exact nonzero rank-one physical pair with a nonzero kernel-star is paid with arbitrary pair-to-leaf cross rank and arbitrary leaf curvature. It identifies the genuinely near-rank-one physical-pair collar as the current singular-pair frontier.

## 2. Setup

Let `L={1,2,3}` be three literal original coordinates and let `J` be a disjoint original-coordinate bank. Condition on all original coordinates outside `L union J`. Write

`Q=Y^T P Y + 2 Y^T C Z + G(Z)+ell^T Y+const`,                    (2.1)

where `Y=X_L`, `Z=X_J`, `P=A[L,L]`, `C=A[L,J]`, and `G` is an arbitrary real quadratic-affine polynomial on the entire right bank.

Assume

`rank C=2`.                                                        (2.2)

Let `n` be a unit vector spanning `ker(C^T)`, put

`a=Pn`,                                                            (2.3)

and

`Delta=sigma_1(C)sigma_2(C)>0`.                                  (2.4)

No coordinate of `n` is assumed to vanish. Thus this includes the genuinely nonphysical-kernel branch.

Fix a physical index `i in L`. Let `K=L\{i}`. In block notation write

`d=P_ii`, `p=P[K,i]`, `c=C[i,:]`, `B=C[K,:]`.                    (2.5)

Assume `d!=0` for the moment.

## 3. First essential implication: exact Schur-area identity

Complete the square in the literal original coordinate `X_i`. The residual cross matrix between the two remaining physical left coordinates and the original right bank is exactly

`M_i = B - d^(-1) p c`.                                          (3.1)

Define its total squared two-volume

`Z2_i = det(M_i M_i^T)=e_2(M_iM_i^T)`.                           (3.2)

### Theorem 3.1 — `QFORM-RANK2-PHYSICAL-SCHUR-AREA-IDENTITY-v1`

For every rank-two `C`, every symmetric `P`, and every physical pivot `i` with `d=P_ii!=0`,

`boxed:
 Z2_i = Delta^2 ((Pn)_i/d)^2.
`                                                                    (3.3)

Equivalently,

`boxed:
 |d| sqrt(Z2_i) = Delta |(Pn)_i|.
`                                                                    (3.4)

This is an exact coefficient identity. It uses no rotation of the random variables and no approximation.

### Proof

Put `G=CC^T`. Because `rank C=2`, `G` is positive semidefinite of rank two, has kernel `span(n)`, and

`adj(G)=Delta^2 n n^T`.                                           (3.5)

Let `v in R^3` have `v_i=0` and `v_K=p/d`, and define the determinant-one row operation

`T=I-v e_i^T`.                                                     (3.6)

Then

`C'=TC`                                                            (3.7)

has unchanged pivot row `c` and its two `K` rows are precisely `M_i`. Therefore the `(i,i)` cofactor of

`G'=C'C'^T=TGT^T`                                                  (3.8)

is

`adj(G')_ii=det(M_iM_i^T)=Z2_i`.                                  (3.9)

Since `det T=1`, the adjugate congruence identity gives

`adj(G')=T^(-T) adj(G) T^(-1)`.                                  (3.10)

Also `T^(-T)=I+e_i v^T`, so

`e_i^T T^(-T)n
 =n_i+v^T n
 =n_i+(p^T n_K)/d
 =(d n_i+p^T n_K)/d
 =(Pn)_i/d`.                                                       (3.11)

Substituting (3.5) into (3.10) and taking the `(i,i)` entry gives exactly (3.3). QED.

A useful aggregate form is

`sum_{i:P_ii!=0} P_ii^2 Z2_i
 =Delta^2 sum_{i:P_ii!=0}(Pn)_i^2`.                               (3.12)

Thus every component of the one-overlap currency carried on a nonzero physical diagonal survives exact physical Schur completion as genuine disjoint residual two-volume. There is no reciprocal-minor selection in (3.12).

## 4. Linear interval receiver

### Theorem 4.1 — `QFORM-RANK2-PHYSICAL-SCHUR-SQUARE-RECEIVER-v1`

Under (2.1)-(2.5), if

`d (Pn)_i !=0`,                                                    (4.1)

then the full conditional law has an essentially bounded density and

`boxed:
 ||p_Q||_(infinity,ess)
 <= 2^(11/4) [Delta |d (Pn)_i|]^(-1/4).
`                                                                    (4.2)

Consequently every interval `I` obeys

`boxed:
 P{Q in I}
 <= 2^(11/4) [Delta |d (Pn)_i|]^(-1/4)|I|.
`                                                                    (4.3)

### Proof

Exact completion of the genuine source coordinate gives

`Q=d[X_i+h(X_K,Z)]^2+R_i(X_K,Z)`,                                 (4.4)

where the residual two-bank cross matrix is `M_i` from (3.1). By Theorem 3.1, (4.1) implies `Z2_i>0`, hence `M_i` has rank two and its singular product is

`S_i=sqrt(Z2_i)=Delta |(Pn)_i|/|d|`.                              (4.5)

Apply the exact physical two-row crossing estimate (1.3) to `R_i`, then its translation-uniform half-Riesz consequence (1.4), and finally the genuine square peel (1.5):

`||p_Q||_(infinity,ess)
 <=2^(11/4)|d|^(-1/2) S_i^(-1/4)`
` =2^(11/4)[Delta |d(Pn)_i|]^(-1/4).`                             (4.6)

No probability is squared and no small-ball square root is converted back afterward; the final estimate is directly linear in interval length. QED.

Continuity note: the exact rank-two residual crossing has an `L^2`/critical Fourier estimate, while the final square receiver is used through a half-Riesz potential. This proves an essentially bounded density and (4.3); this report does **not** claim continuity for Theorem 4.1.

## 5. Quantitative routing of the previous nonphysical-kernel endpoint

Let

`A0=||Pn||_2`, `V=Delta^2 A0^2`, `R_aniso=A0^2/Delta`.            (5.1)

Assume `A0>0`, and choose a physical index `i` with

`|(Pn)_i|>=A0/sqrt(3)`.                                           (5.2)

There are two elementary branches.

### 5.1 A physical diagonal is present on the heavy overlap component

If

`|P_ii|>=A0/(2sqrt(3))`,                                          (5.3)

then

`|P_ii(Pn)_i|>=A0^2/6`.                                          (5.4)

Theorem 4.1 gives

`||p_Q||_(infinity,ess)
 <=2^(11/4) 6^(1/4) (Delta A0^2)^(-1/4)`
` =2^(11/4) 6^(1/4) R_aniso^(-1/12) V^(-1/6)`.                  (5.5)

Hence in the difficult high-anisotropy chamber `R_aniso>=1`,

`boxed:
 ||p_Q||_(infinity,ess)
 <= 2^(11/4)6^(1/4) V^(-1/6)
 <10.529 V^(-1/6).
`                                                                    (5.6)

For `R_aniso<=1`, the previous r42 `p=3` estimate already gives a continuous density with coefficient `6.872 V^(-1/6)`. Therefore the nonphysical nature of `n` causes no loss at all whenever the heavy component of `Pn` sits on a physical diagonal of size (5.3).

### 5.2 Failure of the diagonal route forces a large literal off-diagonal pair

Suppose instead

`|P_ii|<A0/(2sqrt(3))`.                                           (5.7)

Since `||n||_2=1`,

`sum_{j!=i}|n_j|<=sqrt(2)`.                                      (5.8)

From

`(Pn)_i=P_ii n_i+sum_{j!=i}P_ij n_j`,                            (5.9)

(5.2), (5.7), and (5.8) imply

`A0/sqrt(3)
 < A0/(2sqrt(3)) + sqrt(2) max_{j!=i}|P_ij|`.                    (5.10)

Therefore some literal original-coordinate pair `{i,j}` satisfies

`boxed:
 |P_ij| >= A0/(2sqrt(6)).
`                                                                    (5.11)

This is a source-coordinate structural route, not a density conclusion by itself. It shows that after the new Schur receiver the only high-anisotropy survivor exposes a quantitatively large physical two-coordinate core. If that core is exactly rank one and has nonzero kernel-star, the newest account02/B09 theorem pays it even with arbitrary cross rank and arbitrary leaf curvature. If it is definite and quantitatively nonsingular, the standard physical-ellipse receiver pays it. The remaining difficult geometry is therefore the already-live invertible-indefinite / near-rank-one physical-pair third-resource collar, rather than an abstract nonphysical-kernel logarithm.

This is the main structural advance of the run: the previous endpoint `QFORM-GROUPED-RANK2-NONPHYSICAL-KERNEL-ENDPOINT-v1` is reduced to an explicit physical-pivot-or-physical-pair fork.

## 6. Target-valid regressions

### 6.1 Genuine nonphysical kernel paid by the new receiver

Take

`C=[[1,0],[0,1],[-1,-1]]`, `P=2 I_3`.                            (6.1)

Then

`n=(1,1,1)/sqrt(3)`, `Delta=sqrt(3)`, `Pn=2n`,
`A0=2`, `V=12`, `R_aniso=4/sqrt(3)>1`.                            (6.2)

Thus the rank-two kernel is genuinely nonphysical. For every pivot,

`d=2`, `|(Pn)_i|=2/sqrt(3)`,
`Delta |d(Pn)_i|=4`.                                              (6.3)

Theorem 4.1 gives

`boxed:
 ||p_Q||_(infinity,ess)
 <=2^(9/4)
 =4.756828460010884... .
`                                                                    (6.4)

For the full five-coordinate coefficient matrix

`A=[[P,C],[C^T,0]]`,                                              (6.5)

the eigenvalues are

`{-1,-0.414213562...,2,2.414213562...,3}`,                        (6.6)

so the owner target is satisfied.

### 6.2 The zero-diagonal survivor is real but becomes a physical-pair problem

Keep the same `C` and take

`P=[[0,1,1],[1,0,1],[1,1,0]]`.                                   (6.7)

Again

`n=(1,1,1)/sqrt(3)`, `Delta=sqrt(3)`, `Pn=2n`, `V=12`,            (6.8)

but every scalar Schur pivot in Theorem 4.1 has `d=0`. The full matrix has spectrum

`{-2.302775638...,-1.618033989...,0.618033989...,1.302775638...,2}`, (6.9)

so it is target-valid. The forced physical-pair alternative is visible directly: every off-diagonal coefficient of `P` equals one, while

`A0/(2sqrt(6))=1/sqrt(6)=0.408248...`.                            (6.10)

Thus the scalar-pivot theorem is not a disguised full solution; its exact complement is a quantitatively strong physical-pair geometry, consistent with (5.11).

## 7. Required account04/B09 partner application

The completed designated partner theorem is

`QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`,
source `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It proves that a literal invertible physical `3x3` cross block `K` gives

`||p_Q||_infinity<=3|det K|^(-1/3)`                               (7.1)

with arbitrary same-side curvature and a continuous density.

Apply it to the six-coordinate target-valid matrix

`A_partner=[[0,K],[K,0]]`, `K=diag(1,2,3)`.                      (7.2)

Its spectrum is `{-3,-2,-1,1,2,3}` and `det K=6`, so the actual final-law inequality is

`boxed:
 ||p_Q||_infinity <= 3*6^(-1/3)
 =1.650963624447313...,
`                                                                    (7.3)

and

`P{Q in I}<=1.650963624447313... |I|`.                            (7.4)

This branch has a continuous density.

## 8. Exact remaining B09 debt

The previous nonphysical-kernel logarithm is no longer the correct first obstruction. The new precise debt is

`QFORM-RANK2-HEAVY-OFFDIAGONAL-PAIR-THIRDRESOURCE-v1`:

> in the high-anisotropy rank-two packet, after (5.11) exposes a literal physical pair with off-diagonal coefficient at least `A0/(2sqrt(6))`, jointly spend the pair and the surviving Schur cross/curvature resource uniformly through the invertible-indefinite and near-rank-one transition. Do not first take a worst half-Riesz slice, because the newest target-valid near-rank-one example shows that such a slice can diverge logarithmically even while the full law is benign.

This lines up with account02/B09's independently found frontier `QFORM-NEARRANKONE-PAIR-THIRDRESOURCE-BEFORE-HALFRIESZ-v1`.

The unrestricted conjecture remains **OPEN**. Full-target continuity remains **OPEN**. No full-target counterexample was found.

## 9. Deterministic verification

The accompanying `CHECK.py` verifies on 200 seeded well-conditioned rank-two matrices that

`det(M_iM_i^T)=Delta^2((Pn)_i/P_ii)^2`                            (9.1)

for every available physical pivot, to absolute error below `1e-9`. It also verifies both target-valid spectra above, the constants in (5.6), (6.4), and (7.3), and the exact numerical currencies `Delta=sqrt(3)`, `V=12` in the regressions.

These computations audit algebra and arithmetic only; they are not evidence for the universal probability theorem beyond the proofs above.
