SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-24T05:25:37Z.
attacking: QFORM-WITT-FORCED-RESIDUAL-RECEIVER-v1 — use the fresh cross-star decomposition in the actual orthonormal Witt frame, determine what its regression-gap branch really forces, and rule out replacing the residual product projection by an arbitrary bounded joint law.

# fleet02/B05 — the bank-gap branch forces shared-shear residual; joint-cap cancellation obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Status:** `PROVED_SUPPORTING_STRUCTURAL_THEOREM + PROVED_TARGET-SPECTRUM_INTERFACE_COUNTEREXAMPLE + SOURCE-DISJOINT RECEIVER`; full unrestricted QFORM remains **OPEN**.  
**Regularity:** essential boundedness only in the source-disjoint paid theorem; full-target continuity remains separate/open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The live owner corrections remain binding: no arbitrary-joint three-dimensional coarea theorem, no post-rotation independence, no curved-fiber supremum, no pointwise one-dimensional quadratic-phase decay, and no support/moment/log-concavity assumption.

## 1. Inputs actually used

The source-pinned package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

at `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I reread `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.  I use the proved square-peel interface

`||p_(delta W^2+R)||_infty <= |delta|^(-1/2) H_(1/2)(R)`

for a literal independent cap-one square coordinate (with the usual completed-square shift), and retain the source conclusion that the ruled one-sheet side of an independent exact-rank-three `(2,1)` form is already bounded by `pi sqrt(2)` while the convex/two-sheet side is the open geometric side.

The newest compatible fleet03/B05 result used here is r40,

`yspennstate/math-open-problems@e7f663c23c3e00b53c51054040ea9b1e54c5e5a8`,

which proves the exact cross-star decomposition

`M_JK=(1-s)d_J+s d_K+s(1-s)(alpha_J-alpha_K)^2`                       (1.1)

and then a grouped coarea theorem under an additional bank-collinearity hypothesis for the shared-shear vector.

I also use the fresh fleet02/B01 theorem

`QFORM-ZERODIAG-EDGE-HALFRIESZ-v1`,

`yspennstate/math-open-problems@6efd5124aa67510aa22fb5aff7acd57463050ba8`,

which gives, for a literal zero-diagonal endpoint and literal edge `mu`,

`H_(1/2)(R) <= 4 sqrt(2) |mu|^(-1/2)`                                (1.2)

with arbitrary remaining curvature.

## 2. Live exact Witt geometry

In the exact-rank-three heavy-null survivor, after the completed transverse square, the form is

`Q=2a V H+2a kappa U V+A V^2+delta Z^2`,                              (2.1)

where `H` is one literal original coordinate, independent of the residual original-coordinate product bank.  Before the shear `Z=W+(gamma/delta)V`, the residual coefficient vectors

`u,v,w`

of `(U,V,W)` form an orthonormal three-frame.  The shear preserves every `(v,w)` Pluecker coefficient and every within-bank regression residual/gap appearing below.

The target-normalized determinant-star currency remains

`S_i=a^2 |delta| >= 1/2`.                                             (2.2)

The previous fleet02/B05 max-cut theorem supplies a partition `J sqcup K` of the residual original coordinates for which the `(v,w)` cross-star mass is at least `1/2`.  Fleet03/B05 r40 then decomposes that mass as in (1.1).

## 3. New theorem: a nonzero bank gap forces shared-shear residual

### Theorem `QFORM-WITT-GAP-FORCES-U-RESIDUAL-v1`

Let `u,v,w` be orthonormal vectors in `R^N`, and let `J sqcup K={1,...,N}` satisfy

`0<s:=||v_J||_2^2<1`.

Regress `w` and `u` separately on `v` inside each bank:

`w_J=alpha_J v_J+r_J`,   `w_K=alpha_K v_K+r_K`,
`u_J=beta_J v_J+p_J`,    `u_K=beta_K v_K+p_K`,                       (3.1)

with

`r_J perp v_J`, `r_K perp v_K`, `p_J perp v_J`, `p_K perp v_K`.

Define

`G=s(1-s)(alpha_J-alpha_K)^2`,
`G_u=s(1-s)(beta_J-beta_K)^2`.                                       (3.2)

Then

`boxed: G+||r_J||^2+||r_K||^2=1,`                                   (3.3)

`boxed: G_u+||p_J||^2+||p_K||^2=1,`                                 (3.4)

and, most importantly,

`boxed: ||p_J||^2+||p_K||^2 >= G.`                                  (3.5)

#### Proof

Because `<v,w>=0`,

`s alpha_J+(1-s)alpha_K=0`.                                          (3.6)

The squared norm of the piecewise-collinear slope part is therefore

`s alpha_J^2+(1-s)alpha_K^2
 =s(1-s)(alpha_J-alpha_K)^2=G`.                                      (3.7)

Orthogonality of the regression residuals to the bank restrictions of `v` gives (3.3).  The identical argument using `<v,u>=0` gives (3.4).

The two piecewise-collinear slope parts both lie in the same one-dimensional contrast subspace of `span{v_J,v_K}` orthogonal to `v`.  Hence the magnitude of their inner product is exactly

`sqrt(G G_u)`.                                                        (3.8)

Since `<u,w>=0`, this slope inner product is canceled by the residual inner product, so

`sqrt(G G_u)
 =|<p_J,r_J>+<p_K,r_K>|
 <=sqrt((||p_J||^2+||p_K||^2)(||r_J||^2+||r_K||^2))`                 (3.9)

by Cauchy-Schwarz.  Using (3.3)-(3.4),

`G G_u <=(1-G_u)(1-G)`.                                              (3.10)

The common `G G_u` term cancels, leaving

`G+G_u<=1`.                                                          (3.11)

Therefore (3.4) gives

`||p_J||^2+||p_K||^2=1-G_u>=G`,

which is (3.5).  QED.

### Corollary 3.2 — what the r40 gap currency means in the actual Witt packet

The r40 max-cut decomposition has three nonnegative currencies.  If its third currency obeys

`G=s(1-s)(alpha_J-alpha_K)^2 >=1/6`,                                 (3.12)

then the live orthonormal Witt geometry necessarily has

`boxed: ||p_J||^2+||p_K||^2 >=1/6.`                                 (3.13)

Hence at least one bank carries shared-shear residual energy at least `1/12`.

Combining this with (1.1), whenever `M_JK>=1/2` one has the sharpened actual-frame alternative

`boxed:
 max{(1-s)d_J, s d_K, ||p_J||^2+||p_K||^2} >=1/6.
}`                                                                    (3.14)

This replaces a formally attractive but unavailable “pure regression-gap with no shared-shear residual” endpoint by a quantitative residual currency.

### Corollary 3.3 — the r40 bank-collinear gap hypothesis is empty in the exact orthonormal survivor

Suppose, as in the scoped r40 grouped theorem, that after the transverse shear both `z=w+lambda v` and `u` are bank-collinear with `v`:

`z_J=a_J v_J`, `z_K=a_K v_K`,
`u_J=b_J v_J`, `u_K=b_K v_K`,                                       (3.15)

with `0<s<1` and `a_J!=a_K`.  Since adding `lambda v` changes both `w` slopes by the same amount, the gap is still nonzero.  But `u perp v` and `u perp z`.  The two equations

`s b_J+(1-s)b_K=0`,
`s a_J b_J+(1-s)a_K b_K=0`                                          (3.16)

have determinant `s(1-s)(a_K-a_J)!=0`, so `b_J=b_K=0`, contradicting `||u||=1`.

Thus the r40 theorem remains a correct scoped theorem, but its nonzero-gap / fully bank-collinear shared-shear subcase does not occur inside the actual exact Witt orthonormal frame.  The live gap branch necessarily contains the residual quantified by (3.13).

## 4. Positive comparator: source-disjoint shared shear is uniformly paid

The preceding obstruction is genuinely about **source sharing**, not about the scalar coefficient `kappa` by itself.

### Theorem `QFORM-WITT-SOURCE-DISJOINT-SHEAR-v1`

Let `H,U,V,W` be independent scalar random variables with densities bounded by one.  Let `a delta !=0`, and allow arbitrary real `kappa,alpha,gamma`.  Then

`Q=2aV(H+kappa U)+alpha V^2+2gamma VW+delta W^2`                     (4.1)

has an essentially bounded density satisfying

`boxed:
 ||p_Q||_(infinity,ess) <=4 sqrt(2) |a delta|^(-1/2).
}`                                                                    (4.2)

The bound is completely uniform in `kappa`.

#### Proof

Complete the literal independent `W` square:

`Q=delta (W+(gamma/delta)V)^2+R`,                                    (4.3)

where

`R=2aV(H+kappa U)+(alpha-gamma^2/delta)V^2`.                         (4.4)

In `R`, the literal coordinate `H` has zero diagonal and the literal edge `H--V` has coefficient `a`.  Fleet02/B01's completed zero-diagonal-edge theorem (1.2) applies with all `U`-terms and the `V^2` term left intact:

`H_(1/2)(R) <=4 sqrt(2)|a|^(-1/2).`                                  (4.5)

Now apply the source-pinned square peel from `FOURIER_ROUTE_REPORT.md` to the literal independent `W` coordinate in (4.3):

`||p_Q||_(infinity,ess)
 <=|delta|^(-1/2) H_(1/2)(R)
 <=4 sqrt(2)|a delta|^(-1/2).`                                       (4.6)

No moment, support, or continuity assumption is used. QED.

### Target-valid family

For

`Q_kappa=2V(H+kappa U)+W^2`, `0<=kappa<=1`,                         (4.7)

the symmetric matrix in `(H,U,V,W)` is

`[[0,0,1,0],[0,0,kappa,0],[1,kappa,0,0],[0,0,0,1]]`,                (4.8)

whose characteristic polynomial is

`-lambda(lambda-1)(kappa^2-lambda^2+1)`.                             (4.9)

Thus its nonzero spectrum is

`{1,+sqrt(1+kappa^2),-sqrt(1+kappa^2)}`,                             (4.10)

so it lies in the exact owner target.  Theorem (4.2) gives the actual uniform target inequality

`boxed: ||p_(Q_kappa)||_(infinity,ess) <=4 sqrt(2)<5.657.}`           (4.11)

This is the required direct use of a completed `e5f71d79...` interface: the pinned square peel converts the fresh half-Riesz currency to an actual density bound.

## 5. Sharp interface obstruction: bounded joint residual density is not enough

The next construction shows why (4.11) cannot be transferred to the live packet by forgetting how `(U,V,W)` was produced.

### Proposition `QFORM-WITT-JOINT-CAP-CANCELLATION-OBSTRUCTION-v1`

Fix `0<kappa<=1`.  There exists a probability density `rho(u,v,w)<=1` on `R^3` such that every one-coordinate and every coordinate-pair marginal of `rho` is also bounded by one, and an independent cap-one scalar `H`, for which the target-spectrum polynomial

`Q_kappa=2V(H+kappa U)+W^2`                                          (5.1)

has an unbounded density with a logarithmic singularity at zero.

#### Construction

Let `H,E,V,W` be independent `Unif[-1/2,1/2]`, and for `V!=0` define

`U=E-W^2/(2 kappa V)`.                                                (5.2)

(The null set `V=0` can be defined arbitrarily.)  The map

`(e,v,w) -> (u,v,w)`                                                  (5.3)

has Jacobian determinant one.  Therefore `(U,V,W)` has density

`rho(u,v,w)
 =1_{|v|<=1/2} 1_{|w|<=1/2}
  1_{|u+w^2/(2 kappa v)|<=1/2}`,                                     (5.4)

which has total mass one and pointwise cap one.  For fixed `(u,v)` or `(u,w)`, the remaining integration variable ranges over a subset of an interval of length one; hence the corresponding pair marginals are at most one.  The same is immediate for `(V,W)`, and all scalar marginals are therefore also at most one.

But substitution of (5.2) into (5.1) gives the exact cancellation

`Q_kappa=2V(H+kappa E)`.                                              (5.5)

Put `S=H+kappa E`.  Since `0<kappa<=1`, its convolution density is at least `3/4` on `|s|<=1/4`.  Hence, for `0<|q|<1/4`, the product-density formula gives

`p_(Q_kappa)(q)
 =int_(|v|<=1/2) [1/(2|v|)] p_S(q/(2v)) dv
 >=(3/4) int_(2|q|)^(1/2) dv/v
 =(3/4) log(1/(4|q|)).`                                              (5.6)

Thus

`boxed: ||p_(Q_kappa)||_(infinity,ess)=infinity.}`                    (5.7)

The matrix is still exactly (4.8), with the target spectrum (4.10).  What fails is only scalar product provenance: `(U,V,W)` is a nonlinear volume-preserving shear of a product law, not an orthogonal linear projection of the original independent coordinates.

### Consequence

Even in the exact target spectrum, the following data are insufficient for a Witt receiver:

- `H` genuinely independent and cap one;
- the full residual joint density bounded by one;
- every residual scalar and coordinate-pair marginal bounded by one;
- a literal transverse square `W^2`;
- a fixed nonzero shared-multiplier coefficient `kappa`.

The missing hypothesis is precisely the **linear product-projection structure** of the residual triple.  This is a more targeted obstruction than the generic shell counterexample to arbitrary-joint 3D coarea: it realizes exact cancellation of the transverse square inside the live Witt algebra and produces the rank-two product logarithm.

The source-pinned ruled theorem gives `p(s)<=pi sqrt(2)` on the one-sheet side for the corresponding independent product projection.  Proposition 5.1 shows that dropping product provenance can destroy boundedness for the very same target-spectrum matrix, so that theorem's product-marginal input is mathematically essential rather than cosmetic.

## 6. What the fresh fleet03/B05 result now buys

R40's exact decomposition (1.1) is still valuable: combined with Theorem 3.1, it converts the max-cut `M_JK>=1/2` into the actual live-frame quantitative alternative (3.14).  In particular, its gap mechanism is not a branch where the shared shear can be ignored; it is a branch where the shared shear is forced to have at least the same total regression-residual energy.

That is a real equation-level application of the completed partner result and changes the next proof obligation.

## 7. First unpaid implication

The first unpaid B05 implication is now

`QFORM-WITT-FORCED-RESIDUAL-PRODUCT-RECEIVER-v1`:

> In the exact Witt packet (2.1), take the source-disjoint max-cut `J sqcup K` with `M_JK>=1/2`.  Use the original product laws inside the two banks to convert the quantitative alternative
>
> `max{(1-s)d_J, s d_K, ||p_J||^2+||p_K||^2}>=1/6`
>
> into a Borel/interval density bound uniform for `0<=kappa<1`, without slicing on a projected residual coordinate, replacing the residual law by an arbitrary joint density, selecting a tiny individual Pluecker edge, or taking an unrestricted curved-fiber supremum.

The proposition in Section 5 proves that a receiver stated only in terms of joint density caps is false.  The positive theorem in Section 4 proves that complete source separation is already enough.  Therefore the remaining mathematical content is exactly the intermediate **linear product-projection / two-bank source-sharing** structure.

Full unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED.  No target-valid scalar-product counterexample is produced here.
