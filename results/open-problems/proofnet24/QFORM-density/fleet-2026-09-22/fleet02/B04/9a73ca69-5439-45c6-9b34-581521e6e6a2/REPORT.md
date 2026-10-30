SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-24T07:26:12Z.
attacking: exact low-tetrad Schur-numerator geometry: classify the zero disjoint-tetrad face and compare the new pair-numerator receiver against pinned volume/ridge gates on one fully dense six-coordinate target matrix.

# fleet02/B04 r21 — zero-tetrad clique is a real cross-volume/ridge blind spot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING CONSTRUCTION / ACTUAL e5 INEQUALITY / EXACT SAME-MATRIX VOLUME-RIDGE-PARTNER OBSTRUCTION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: only essential boundedness is claimed below; continuity remains separate.

## First unpaid implication

The fresh fleet03/B04 r52 theorem compresses its overlap-two branch to a literal physical pair `H` for which the Schur numerator

`N_H = det(B) D - C adj(B) C^T`

has target-scale off-diagonal energy `J_2(H)` but very small disjoint tetrad volume `D_2^disj(N_H)`. My early calculation in this same run proves that the exact boundary `D_2^disj=0` is either a star or a diagonal-plus-signed-rank-one clique (isolated vertices allowed).

The first unpaid implication is therefore now:

`QFORM-LOW-TETRAD-STABILITY-TO-STAR-CLIQUE-OR-RENEWED-VOLUME-v1`:
quantitatively stabilize that exact classification when `D_2^disj/J_2^2` is small, but route the two exact boundary types by different product-preserving receivers. The construction below shows why a single “renew cross volume or ridge” conclusion is impossible even on a fully dense, strongly target-valid matrix: the exact clique boundary can make **every** physical cross block rank at most two.

## 1. Source-pinned inputs

Fresh owner control on `math-research-brain/main` remains revision `2026-09-22.15`, QFORM-only, with the live corrections forbidding law-uniform pointwise quadratic-phase decay and post-rotation independence.

Required pinned source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` read. I use the completed physical-principal-block Theorem A from `COUNTEREXAMPLE_SEARCH.md` at an actual inequality in Section 5. I also test pinned D/D' and D5 on the same physical matrix.

Fresh designated partner:

`fleet03/B04` r52, canonical mathematics
`yspennstate/math-open-problems@fbc50959f73f2a66b91acacbbacc37cbf2b66720`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260924T064507Z-fleet03-B04-QFORM-auto11-r52/REPORT.md`.

It proves `QFORM-PAIR-SCHUR-NUMERATOR-2VOLUME-v1`: if a literal physical pair `H` has a residual cut `I,J` with

`Z_N=e_2(N_H[I,J]N_H[I,J]^T)>0`,

then

`||p_Q||_infinity <= 8*2^(1/4)(1+pi) Z_N^(-1/12)`,

and after averaging cuts it gives the disjoint-tetrad version with `D_2^disj(N_H)^(-1/12)`. The construction below lies exactly on the zero-tetrad face, so this theorem is applied as a precise obstruction rather than outside its hypotheses.

The direct ridge comparison uses the completed ridge-window criterion at
`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`: for a physical cross block its regularized ridge trace `theta` must satisfy `theta>2q` with `q>=1`.

## 2. General clique-boundary family with cross rank at most two

Let `H={1,2}` and `K={3,...,m+2}`. Take an invertible symmetric `2x2` matrix `B`, a nonzero vector `u in R^m`, a vector `v in R^2`, and

`S=d I_m + tau u u^T`.

Put

`C=u v^T`,
`D=S+C B^(-1) C^T`,
`A=[[B,C^T],[C,D]].`                                               (2.1)

Then the physical Schur complement at `H` is exactly `S`, and hence

`N_H=det(B) S.`                                                     (2.2)

For distinct residual indices `i,j`,

`(N_H)_{ij}=det(B) tau u_i u_j`.                                  (2.3)

Thus, if every `u_i` and `tau` are nonzero, the off-diagonal support of `N_H` is a clique and is exactly a signed rank-one factor. Every disjoint `2x2` tetrad vanishes, so

`boxed: D_2^disj(N_H)=0.`                                          (2.4)

Now write

`kappa=tau+v^T B^(-1)v`,                                          (2.5)

so the residual block is

`D=d I_m+kappa u u^T`.                                             (2.6)

Assume `kappa != 0`. Let `sigma=sign(kappa)` and choose a vector `w` by

`w_K=sqrt(|kappa|)u`,
`w_H=sigma v/sqrt(|kappa|).`                                      (2.7)

Then all pair-to-residual and residual-to-residual off-diagonal coefficients of `A` are supplied by `sigma w w^T`. The only off-diagonal coefficient not thereby fixed is the single physical edge `12`. Therefore

`A = (diagonal matrix) + sigma w w^T + r(e_1e_2^T+e_2e_1^T)`       (2.8)

for one scalar `r`.

For **every** pair of disjoint original-coordinate sets `I,J`, the physical crossing is consequently

`A[I,J]=sigma w_I w_J^T + r E_{I,J}`,                              (2.9)

where `E_{I,J}` has rank at most one: because `I,J` are disjoint, at most one orientation of the single edge `12` can cross the cut. Hence

`boxed: rank A[I,J] <= 2 for every physical disjoint cut I,J.`      (2.10)

This is an exact coefficient statement; no random tail is discarded.

### Consequences for the B04 Fourier/volume interfaces

Equation (2.10) implies for every physical cut

`e_3(A[I,J]^T A[I,J])=0`,
`e_5(A[I,J]^T A[I,J])=0`.                                         (2.11)

So there is no supported physical third-minor weight to optimize: the globally optimal determinant-entropy currency for pinned D/D' is exactly zero. D5 also has zero fifth volume. No reweighting can repair absent minors.

For the direct ridge family, a positive regularization has at most two nonzero ridge eigenvalues, each strictly below one. Therefore

`theta_gamma=tr K_gamma<2`.                                        (2.12)

The ridge criterion requires `q>=1` and `theta_gamma>2q>=2`, which is impossible at every scale. Thus the entire direct ridge family is also blind to (2.1).

This shows that the exact low-tetrad clique face is not automatically a renewed-volume or ridge face.

## 3. Fully dense six-coordinate target matrix

Take `m=4` and the exact choices

`B=[[3,1],[1,-3]],`
`u=(1,1,1,1)^T,`
`v=(1/10,1/5)^T,`
`d=2, tau=1.`                                                      (3.1)

Since

`B^(-1)=(1/10)[[3,1],[1,-3]]`

and

`v^T B^(-1)v=-1/200`,

we have

`kappa=199/200>0`.                                                  (3.2)

The resulting matrix is

`A_* =`

`[[3, 1, 1/10,1/10,1/10,1/10],`
` [1,-3, 1/5, 1/5, 1/5, 1/5],`
` [1/10,1/5,599/200,199/200,199/200,199/200],`
` [1/10,1/5,199/200,599/200,199/200,199/200],`
` [1/10,1/5,199/200,199/200,599/200,199/200],`
` [1/10,1/5,199/200,199/200,199/200,599/200]].`                    (3.3)

Every physical coefficient of `A_*` is nonzero. It is therefore genuinely non-diagonal in the independent coordinates and is indefinite.

The Schur complement of the first physical pair is

`S=2I_4+11^T`.                                                      (3.4)

Since `det B=-10`,

`N_H=-10S`,                                                        (3.5)

so its diagonal entries are `-30` and all twelve ordered off-diagonal entries are `-10`. Consequently

`boxed: J_2(H)=sum_{i!=j}(N_H)_{ij}^2=1200,`
`boxed: D_2^disj(N_H)=0.`                                         (3.6)

Thus this matrix is not merely near the fresh partner's coherent chamber: it lies on its exact zero-tetrad boundary while carrying enormous overlap-two energy.

For the rank-two-crossing decomposition, put `kappa=199/200`. With

`w_K=sqrt(kappa)(1,1,1,1),`
`w_H=(1/10,1/5)/sqrt(kappa),`

one has

`A_* = diagonal + w w^T + (195/199)(e_1e_2^T+e_2e_1^T).`           (3.7)

Hence the universal physical-cross-rank bound (2.10) is literal on this fully dense matrix.

## 4. Rigorous spectral target check

Let

`A_0=diag(B,S)`.

Its spectrum is

`{-sqrt(10), 2,2,2, sqrt(10), 6}`.                                (4.1)

The perturbation is

`A_*-A_0=[[0,C^T],[C,CB^(-1)C^T]].`

Here

`||C||_op=sqrt(5)/5`,
`||CB^(-1)C^T||_op=1/50`,

so

`||A_*-A_0||_op <= sqrt(5)/5+1/50 <0.468.`                         (4.2)

By Weyl, the unique negative eigenvalue remains below

`-sqrt(10)+0.468<-2.69`,

and every positive eigenvalue remains above

`2-0.468>1.53`.                                                     (4.3)

Therefore

`boxed: all six eigenvalues of A_* have modulus >1.`               (4.4)

For audit only, direct deterministic diagonalization gives approximately

`-3.17666914, 2,2,2, 3.13839042, 6.01827872`; the proof uses only (4.1)-(4.3).

## 5. Actual e5 completed result pays the matrix

Now condition on the three original coordinates `X_1,X_2,X_6`. The remaining literal physical coordinates `X_3,X_4,X_5` stay independent with density caps one. Their quadratic principal block is

`A_*[{3,4,5},{3,4,5}]
 =2I_3+(199/200)11^T`.                                             (5.1)

Its eigenvalues are exactly

`2, 2, 997/200`.                                                    (5.2)

All couplings to the conditioned variables become arbitrary linear terms, which are explicitly allowed by the completed Theorem A in the required pinned `COUNTEREXAMPLE_SEARCH.md`. That theorem gives, for a three-dimensional principal block whose eigenvalue magnitudes are all at least `sigma`,

`||p||_infinity <= 6 sqrt(pi)/sigma`.                              (5.3)

Taking `sigma=2` yields the actual target-valid inequality

`boxed:
 ||p_{X^T A_* X}||_infinity <= 3 sqrt(pi)
 =5.317361552716548... .`                                         (5.4)

This is a direct application of the required `e5f71d...` source to the same physical matrix on which the product-crossing certificates fail.

## 6. Same-matrix comparison: optimized volume, partner numerator, ridge

On `A_*`:

1. **Pinned D / D'.** Every physical crossing has rank at most two. Thus every physical `3x3` crossing minor is zero. The supported-minor feasible set is empty and the globally optimized determinant-entropy currency is `G_3=0`; no D or D' certificate exists on any cut.
2. **Pinned D5.** Likewise `G_5=Z_5=0` on every cut; the marginal-free fifth-volume theorem has no finite certificate.
3. **Fresh fleet03/B04 r52.** For the first physical pair, `J_2(H)=1200` but `D_2^disj(N_H)=0`; equivalently every possible residual two-volume `Z_N(I,J)` is zero. The partner theorem correctly leaves this exact clique face unpaid.
4. **Direct ridge.** Every physical crossing has rank at most two, so `theta_gamma<2` for every positive regularization. Since the completed gate requires `q>=1` and `theta_gamma>2q`, it is impossible at every scale.
5. **Localized physical principal block.** The pinned e5 Theorem A succeeds with the explicit universal-in-input-law bound `3 sqrt(pi)`.

Thus this fully dense target matrix simultaneously defeats **all** physical third/fifth-volume weight optimizations, the direct ridge family, and the fresh Schur-numerator two-volume receiver, while an original-coordinate three-variable curvature receiver pays it immediately.

## 7. Structural conclusion

The exact low-tetrad classification from the early calculation is not merely cosmetic. Its clique side contains target-valid matrices where all original-coordinate cross ranks collapse to two, even though the matrix itself is fully dense and has six eigenvalues of modulus greater than one. Therefore a quantitative stability theorem for the r52 low-tetrad chamber cannot have only the outcomes “renew disjoint cross volume” or “ridge”. It must retain a **principal-curvature / square-bank / diagonal-plus-rank-one** endpoint as a separate receiver.

A useful sharpened next statement is:

`QFORM-LOW-TETRAD-STABILITY-WITH-PRINCIPAL-CURVATURE-v1`:
for `J_2(H)>=1/144` and small `D_2^disj(N_H)/J_2(H)^2`, prove that either
(i) a residual physical pair/kernel star is quantitatively payable,
(ii) a physical principal triple has target-scale smallest singular value and is payable by the localized theorem,
(iii) a grouped square/diagonal-plus-low-rank receiver applies, or
(iv) disjoint numerator two-volume regenerates at target scale.

The example above proves that outcome (ii) cannot be omitted. The still-unproved content is quantitative stability away from the exact star/clique boundary; no small rough quadratic tail may be dropped in making that passage.

No scheduler, task identity, cadence, enabled/quiet state, notification, email, permission, cross-account authentication, paid call, public release, FEI, installation, benchmark, gold-data, or unrelated-data state was changed.