SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-22T20:57:49Z.
attacking: a two-original-bank zero-pivot compiler in which one bank supplies a scalar and the second bank supplies a genuinely dependent two-dimensional projection; pay the dependence by the sharp product-marginal theorem and the nonlinear trace by account04/B18.

# account03/B18 r17 — sharp two-bank zero-pivot product-projection compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Literature-to-proof transfer  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING TARGET-LEVEL BRANCH / FULL QFORM OPEN**.


## 1. The exact literature transfer

Primary source: Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889, arXiv:1507.07949.

For a product probability density `prod_j f_j` with every one-dimensional factor bounded by one, the density of every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`. There are no moment, centering, log-concavity, compact-support, connected-support, identical-law, or smoothness hypotheses.

Two exact consequences will be used. If `u != 0` and `U=<u,X>`, then

`||p_U||_infinity <= sqrt(2)/||u||_2`.                         (1.1)

If `v,w` are linearly independent and

`(V,W)=(<v,X>,<w,X>)`,

then

`boxed: ||p_(V,W)||_infinity <= 2/||v wedge w||.`             (1.2)

Here `||v wedge w||=sqrt(||v||^2||w||^2-<v,w>^2)`.

To verify (1.2), let `E=span{v,w}` and let `R` have orthonormal columns spanning `E`. The orthogonal projection coordinate `Z=R^T X` has density cap at most `2` by LPP (if `E` is the entire ambient bank, the direct orthogonal-change cap is actually at most one, so the displayed bound remains valid). Write `(V,W)^T=C Z`. Then

`|det C|=sqrt(det [[<v,v>,<v,w>],[<w,v>,<w,w>]])=||v wedge w||`,

and the linear change of variables gives (1.2).

I also rechecked Juškevičius–Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190. Its multidimensional theorem concerns sums of independent random vectors with bounded ambient-dimensional densities. It cannot be applied term-by-term to `(V,W)=sum_j (v_j X_j,w_j X_j)` because each summand is supported on a line in `R^2` and therefore has no finite two-dimensional density. LPP is the source-valid theorem here because it controls the full orthogonal marginal without asserting independence of its coordinates.

## 2. Partner theorem actually consumed

The designated completed partner is account04/B18:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

That report applies the completed account01/B18 zero-pivot theorem. In the exact form needed here:

> Let `X` be a scalar random variable with density cap one, independent of a two-dimensional random vector `Y` having an arbitrary joint density cap `M`. Let `H` be a nonsingular real symmetric `3 x 3` matrix with `H_11=0`. Then `(X,Y)^T H (X,Y)` has a continuous density and
>
> `||p||_infinity <= 6 M^(2/3)|det H|^(-1/3)`.                (2.1)

Arbitrary affine terms are also harmless: since `H` is nonsingular, completing the square translates `X` and `Y` by deterministic vectors, preserving scalar-versus-vector independence and the density caps. This is precisely the interface used below.

## 3. Main theorem: one scalar bank plus a dependent two-dimensional bank

### Theorem 3.1 — `QFORM-LPP-TWOBANK-ZEROPIVOT-v1`

Let `I,J,O` be pairwise disjoint sets of original coordinates. All original coordinates are independent real random variables with densities bounded by one. Choose

`u in R^I`, `u !=0`,
`v,w in R^J`, `v wedge w !=0`,

and define

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_J>`, `Z=(U,V,W)^T`.

Let `K` be a nonsingular symmetric `3 x 3` matrix with

`K_11=0`.                                                        (3.1)

Assume that after conditioning on the outside coordinates `X_O=o`, the full quadratic form has the exact active representation

`Q_o = Z^T K Z + 2 d(o)^T Z + c(o)`,                            (3.2)

where `d(o)` and `c(o)` are arbitrary measurable functions of the outside variables. Equivalently, the physical quadratic block on `I union J` factors through the three displayed projections and all outside couplings into that block lie in their span; arbitrary quadratic curvature on `O` is allowed.

Then the unconditional law of `Q` has a **continuous** density satisfying

`boxed:
 ||p_Q||_infinity
 <= 12 / [ (||u||_2 ||v wedge w||)^(2/3) |det K|^(1/3) ].
`                                                                  (3.3)

No independence between `V` and `W` is assumed or used.

### Proof

Because the banks `I` and `J` are disjoint original-coordinate sets, `U` is genuinely independent of the entire pair `(V,W)`. The coordinates `V,W` themselves may be dependent.

By (1.1), choose the scalar density cap

`N=sqrt(2)/||u||_2`.                                             (3.4)

Then `X_0=N U` has density cap at most one. By (1.2), the pair has joint density cap

`M=2/||v wedge w||`.                                            (3.5)

Condition on `X_O=o`. Complete the affine term in (3.2) using the nonsingularity of `K`; this only translates the scalar and the pair and hence preserves (3.4)–(3.5) and their independence split.

Write `D=diag(N,1,1)` and `Z'=D Z`. The quadratic coefficient matrix in the variables `Z'` is

`K'=D^(-1) K D^(-1)`.                                          (3.6)

Its first diagonal entry remains zero, and

`det K'=det K/N^2`.                                             (3.7)

Apply the completed account04/B18 partner theorem (2.1) to `X_0` and `(V,W)`. Uniformly in the outside conditioning,

`||p_(Q|X_O=o)||_infinity
 <=6 M^(2/3)|det K'|^(-1/3)
 =6(MN)^(2/3)|det K|^(-1/3).`                                 (3.8)

Now (3.4)–(3.5) give

`MN <= 2sqrt(2)/(||u||_2 ||v wedge w||)`

and `(2sqrt(2))^(2/3)=2`. Therefore (3.8) is exactly (3.3).

The partner theorem gives a continuous conditional density for almost every outside value. The bound (3.3) is uniform in that value. If `t_n -> t`, conditional continuity gives pointwise convergence of the conditional densities and the uniform bound supplies a probability-integrable dominator. Dominated convergence after averaging in `X_O` proves continuity of the unconditional density. QED.

## 4. Exact target-valid diffuse overlapping family

The theorem is not merely a finite-coordinate control. Let `I` and `J` be disjoint banks. Take `u` to be a unit flat vector on `I`. On `J` choose two orthonormal diffuse vectors `v,w`; for example on `2m` coordinates,

`v=(1,...,1)/sqrt(2m)`,
`w=(1,...,1,-1,...,-1)/sqrt(2m)`

with `m` plus signs followed by `m` minus signs. Let

`K=[[0,1,1],[1,0,1],[1,1,0]].`                                (4.1)

The three physical vectors `u,v,w` are orthonormal, so the nonzero spectrum of the induced physical matrix is exactly the spectrum of `K`, namely

`{2,-1,-1}`.                                                    (4.2)

Thus the owner's three-large-eigenvalue hypothesis is satisfied exactly for every bank size. For non-Gaussian product inputs the pair `(V,W)` is generally dependent because the two projections use the same bank; no rotated-coordinate independence is available. Nevertheless `||u||=||v wedge w||=1` and `|det K|=2`, so Theorem 3.1 gives the distribution-free continuous-density estimate

`boxed: ||p_Q||_infinity <= 12/2^(1/3) = 9.5244063118... .`   (4.3)

Every individual physical matrix entry in the diffuse banks is `O(1/m)`. Thus the estimate is genuinely aggregate-before-inversion: it does not select one coordinate coefficient or minor whose reciprocal would diverge with `m`.

Arbitrary additional outside coordinates and outside quadratic curvature may be added under the aligned-coupling hypothesis of Theorem 3.1 without changing the bound. A direct independent outside summand is the simplest special case.

## 5. Source-valid upgrade of the current transverse-square branch

The same literature transfer sharpens the completed account03/B09 transverse-square theorem without changing its proof. That theorem states that if `U` is independent of `(V,W)`, `||p_U||_infinity<=N`, `||p_(V,W)||_infinity<=M`, and

`T=2aUV+cW^2+affine`,

then

`||p_T||_infinity <= C0 (MN)^(2/3)|a|^(-2/3)|c|^(-1/3)`,
`C0=(3/2)10^(2/3)`.                                             (5.1)

For the same two-bank product projections as above, LPP gives (3.4)–(3.5), hence

`boxed:
 ||p_T||_infinity
 <= 3*10^(2/3)
    (||u||_2 ||v wedge w||)^(-2/3)
    |a|^(-2/3)|c|^(-1/3).
`                                                                  (5.2)

This replaces the weaker generic pair-marginal constant previously used in that application. More importantly, Theorem 3.1 handles an arbitrary nonsingular `2 x 2` self-quadratic block on the dependent `(V,W)` side, not only one transverse square.

## 6. Why the live corrections do not hit the theorem

1. **No independence after rotation.** `U` is independent of `(V,W)` only because their original-coordinate banks are disjoint. `V,W` are explicitly allowed to be dependent.
2. **No arbitrary-joint coarea claim.** The nonlinear trace estimate is the proved scalar-versus-vector partner theorem, and the pair's joint cap is obtained from product provenance by LPP.
3. **No conditional projection moment.** Product aggregation occurs before conditioning; only the outside original coordinates are conditioned.
4. **No fixed good minor.** The two-dimensional pair is paid by the whole wedge `||v wedge w||`, which may be assembled from arbitrarily many physical coordinates.
5. **No pointwise oscillatory decay or Gaussian/log-concave hypothesis.** None enters the proof.
6. **No claim that the spectral hypothesis forces this factorization.** This is a paid analytic branch, not the missing universal structural extraction.

## 7. Remaining implication to the full target

The full QFORM conjecture remains **OPEN / NOT PROVED**. The new theorem removes one structural tax: a useful three-dimensional effective zero-pivot form need not decompose into three independent original-coordinate banks. It is enough that one original-coordinate bank supplies one scalar direction and a second disjoint bank supplies two linearly independent, possibly dependent, projection directions.

The next honest structural target is therefore a two-bank aggregate routing statement. Outside the already-paid ridge/exterior-half-Riesz/physical-pair/scalar-Schur branches, derive from `s_3(A)>=1` an exact or quantitatively controlled representation of the form in Theorem 3.1 with

`|det K| ||u||_2^2 ||v wedge w||^2 >= c0>0`,                  (7.1)

or route the same exterior mass to an existing paid branch. Equation (7.1) is exactly the scale quantity needed by (3.3), since cubing its denominator produces that product. No assertion that (7.1) follows from the bare spectral hypothesis is made here.

Continuity is **proved for Theorem 3.1 and the family (4.1)**. Continuity for the unrestricted target remains open.

## 8. Source pins

- LPP primary source: arXiv:1507.07949 / Israel J. Math. 216 (2016), 877–889.
- Juškevičius–Lee source audit: arXiv:1503.09190.
- Designated partner: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.
- Partner's underlying zero-pivot proof: `yspennstate/math-open-problems@dd94932dae1791af1bca9396c062e17d0e55142a`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T175509Z-qform-B18-a01-r15/REPORT.md`.
- Current B18 execution label: `WITHOUT_VERIFIED_BRAIN`; repository synchronization is not authenticated native learned-memory ingestion.
