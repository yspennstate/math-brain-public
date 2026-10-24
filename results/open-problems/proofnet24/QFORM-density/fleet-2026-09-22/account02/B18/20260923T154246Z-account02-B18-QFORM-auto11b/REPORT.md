SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T15:42:46Z.
attacking: the heavy-anchor near-null geometry; close every two-heavy transverse state by an original-coordinate pair-or-Schur dichotomy, then splice the exact-null diffuse complement with account03/B18 r28.

# account02/B18 — double-heavy transverse closure and exact-null heavy-anchor completion

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SUPPORTING EXACT-RANK3 CLOSURE / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Continuity:** not claimed for the new pair-or-Schur theorem; the partner-paid exact-null diffuse branch has a continuous `C_0` density.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and first unpaid implication

The owner target remains: arbitrary independent real original coordinates, each with probability density bounded by one, and an arbitrary real symmetric physical matrix with at least three eigenvalues of modulus at least one. Prove one universal essential-density bound for `X^T A X`, or give a valid counterexample. No moments, support bound, log-concavity, iid assumption, symmetry, diagonal-basis assumption, or post-rotation independence is used here.

The incoming B18 state had reduced the exact-rank-three heavy-anchor obstruction to a large-leverage original row `u_i`, with `c_i=||u_i||^2>1/2`, and the debt was either a punctured near-null scalar pivot or a reroot state containing a second transverse-heavy ORIGINAL row. This report closes the latter state uniformly even when the first pivot is small but nonzero. Consequently, after the partner splice below, the remaining exact-rank-three heavy-anchor debt is only a **nonzero near-null transverse-diffuse collar**.

## 2. Completed results applied literally

### 2.1 Pinned e5f scalar square peel

The required source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md` and `FOURIER_ROUTE_REPORT.md`, proves the original-coordinate scalar square peel

`Dens(Q) <= |a|^(-1/2) H_(1/2)(S)`,                            (2.1)

where `a=A_ii!=0`, `S=A/A_ii` is the scalar Schur complement and `H_(1/2)(S)=sup_t E|R-t|^(-1/2)` for the residual quadratic-affine random variable. This run applies (2.1) at the actual physical pivots `i` and `j`; no pointwise stationary-phase surrogate is used.

### 2.2 Orientation-free rank-two half-Riesz endpoint

The completed source

`math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

proves, for a rank-two quadratic form in independent cap-one ORIGINAL coordinates with arbitrary affine term,

`H_(1/2)(R) <=128 |pdet_2 R|^(-1/4)`.                          (2.2)

For exact rank three `A=RMR^T`, `R^TR=I_3`, write `D=|det M|`, let `u_k` be physical spectral row `k`, `c_k=||u_k||^2`, and let `a=A_kk!=0`. Scalar Schur determinant factorisation plus Cauchy--Binet gives

`|pdet_2(A/A_kk)| = c_k D/|a|`.                                (2.3)

Indeed, for every residual pair `p<q`,

`det A[{k,p,q}] = a det(A/A_kk)[{p,q}]`
`               = det(M) det(u_k,u_p,u_q)^2`,

and after a coefficient-space rotation putting `u_k=sqrt(c_k)e_1`, the transverse residual rows are a Parseval frame in `R^2`, so the sum of the determinant squares is `c_k`. Combining (2.1)--(2.3) gives the source-valid physical-pivot estimate

`boxed: ||p_Q||_infinity <=128 [c_k D |A_kk|]^(-1/4).`          (2.4)

This is the first completed e5f implication actually spent below.

### 2.3 Physical indefinite-pair theorem

The completed pair-log source

`math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

states: if an original-coordinate principal block is exact rank three with its three nonzero eigenvalues of modulus at least `s`, and two ORIGINAL coordinates form an invertible indefinite pair `B`, then the full ambient quadratic form satisfies

`||p_Q||_infinity <=8 sqrt(5) [|det B| sigma_min(B) s]^(-1/4)`. (2.5)

Outside coefficients, couplings and affine shifts are arbitrary. The theorem does not divide by either scalar diagonal of the pair.

## 3. New theorem — every double-heavy transverse state is paid

### `QFORM-DOUBLEHEAVY-TRANSVERSE-CLOSURE-v1`

Let

`A=R M R^T`, `R^T R=I_3`,                                      (3.1)

be exact rank three, and suppose all three eigenvalues of `M` have modulus at least one. Assume some ORIGINAL physical row `u_i` has

`c_i=||u_i||^2>1/2`.                                           (3.2)

Put `n=u_i/sqrt(c_i)`. Suppose another ORIGINAL row `u_j` is transverse-heavy relative to `i`:

`q:=||P_(n^perp)u_j||^2>1/2`.                                  (3.3)

Then for arbitrary independent cap-one original-coordinate laws,

`boxed: ||p_(X^T A X)||_infinity <363.`                         (3.4)

The conclusion is essential boundedness / absolute continuity. Continuity is not asserted by this proof.

### Proof

Write

`a=A_ii=u_i^T M u_i`.

If `|a|>=1/32`, then (2.4), `c_i>1/2`, and `D>=1` give

`||p_Q||_infinity
 <128[(1/2)(1/32)]^(-1/4)
 =256 sqrt(2)
 <363.`                                                         (3.5)

It remains to assume

`|a|<1/32`.                                                      (3.6)

Set

`epsilon=a/c_i`, so `|epsilon|<1/16`.                           (3.7)

Write

`u_j=alpha n+beta t`,                                           (3.8)

where `t` is unit, `t perpendicular n`, and `beta^2=q`. Since every Parseval row has leverage at most one,

`alpha^2+beta^2=||u_j||^2<=1`,                                  (3.9)

so `|alpha|<1/sqrt(2)` and `|beta|>1/sqrt(2)`.

The small Rayleigh quotient (3.7) rules out a definite `M` whose eigenvalues all have modulus at least one. Thus `M` is indefinite. Replacing `M` by `-M` if necessary only replaces `Q` by `-Q`, leaving its density norm unchanged; orient so the signature is `(2+,1-)`. In the orthonormal coefficient basis `(n,t)`, the compression of `M` is

`C=[[epsilon,gamma],[gamma,delta]]`.                             (3.10)

Let `p` be its larger eigenvalue. Cauchy interlacing with the three eigenvalues of `M` gives

`p>=1`.                                                         (3.11)

The characteristic equation at `p` gives

`(p-epsilon)(p-delta)=gamma^2`,

hence, writing `g=|gamma|`,

`delta=p-gamma^2/(p-epsilon)
      >=1-g^2/(1-|epsilon|)
      >1-(16/15)g^2.`                                          (3.12)

Let

`d=A_jj=u_j^T M u_j
       =alpha^2 epsilon+2 alpha beta gamma+beta^2 delta`.        (3.13)

If `|d|>=1/8`, then `c_j=||u_j||^2>=q>1/2`, and another application of the actual physical-pivot estimate (2.4) gives

`||p_Q||_infinity<128[(1/2)(1/8)]^(-1/4)=256.`                 (3.14)

So suppose also

`|d|<1/8`.                                                       (3.15)

We claim

`g>9/32`.                                                        (3.16)

If instead `g<=9/32`, the lower bound in (3.12) is positive. Using `alpha^2<1/2`, `2|alpha beta|<=1`, and `beta^2=q>1/2` in (3.13),

`d > -1/32 - g + (1/2)(1-(16/15)g^2).`                         (3.17)

The right side is decreasing for `g>=0`; at `g=9/32` it is exactly

`93/640 >1/8`,                                                  (3.18)

contradicting (3.15). This proves (3.16).

Now the ORIGINAL physical off-diagonal entry is

`b=A_ij
  =sqrt(c_i)(alpha epsilon+beta gamma)`.                       (3.19)

Because `sqrt(c_i)|beta|>1/2`, while `sqrt(c_i)|alpha|<1/sqrt(2)<3/4`, equations (3.7) and (3.16) imply

`|b|> (1/2)(9/32) -(3/4)(1/16)
     =3/32.`                                                     (3.20)

Consider the original-coordinate physical pair

`B=[[a,b],[b,d]]`.                                               (3.21)

By (3.6), (3.15), and (3.20),

`det B=ad-b^2
      <(1/32)(1/8)-(3/32)^2
      =-5/1024`.                                                (3.22)

Thus `B` is uniformly indefinite and

`|det B|>5/1024`.                                               (3.23)

For an indefinite symmetric `2x2` pair,

`sigma_min(B)
 =(sqrt((a-d)^2+4b^2)-|a+d|)/2
 >=|b|-(|a|+|d|)/2
 >3/32-(1/32+1/8)/2
 =1/64.`                                                        (3.24)

Apply the completed pair theorem (2.5) with `s=1`:

`||p_Q||_infinity
 <8 sqrt(5)[(5/1024)(1/64)]^(-1/4)
 =128*5^(1/4)
 <192.`                                                         (3.25)

Together, (3.5), (3.14), and (3.25) prove (3.4). QED.

The coefficient-space basis `(n,t)` is used only to read the compression of `M`; the random variables remain the original independent coordinates throughout. The final pair `(i,j)` is an ORIGINAL physical pair.

## 4. Compatible designated partner applied — exact-null heavy anchors are now complete

The completed designated-partner result account03/B18 r28 is

`math-open-problems@43b16ba3992035298289170540682e8aa62a9ad4`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T120257Z-account03-B18-QFORM-r28/REPORT.md`.

Its `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1` says that for an exact Schur-isotropic null hub, if every residual ORIGINAL physical row has transverse leverage at most `1/2`, then

`||p_Q||_infinity <=3*2^(4/3)[r^2|det D_s|]^(-1/3)`,            (4.1)

with a continuous `C_0` density.

Apply it to an exact-null heavy row `i` in (3.1): assume

`A_ii=0`, `c_i>1/2`.                                            (4.2)

For `c_i<1`, set `G=I-u_i u_i^T`, `H=G^(1/2)`, reroot the residual rows as `v_k=H^(-1)u_k`, and set `D_i=H M H`. The same physical matrix becomes a Schur-isotropic packet whose hub shear has squared norm `c_i/(1-c_i)`. Its null direction is `n`, its residual transverse leverages are exactly

`||P_(n^perp)v_k||^2=||P_(n^perp)u_k||^2`,                     (4.3)

and the partner determinant currency is exactly

`r_i^2 |det D_i|=c_i |det M|`.                                 (4.4)

Therefore, if every transverse leverage in (4.3) is at most `1/2`, the partner theorem gives

`||p_Q||_infinity
 <=3*2^(4/3)[c_i |det M|]^(-1/3)
 <3*2^(5/3)
 =9.5244063118092... .`                                        (4.5)

If `c_i=1`, the isometric null-hub endpoint cited and proved in the partner report applies directly with the same determinant currency.

If instead some residual row has transverse leverage `>1/2`, the new theorem in Section 3 applies and gives `<363`. Hence:

### `QFORM-EXACTNULL-HEAVY-ANCHOR-COMPLETE-v1`

For every exact-rank-three target matrix with three nonzero eigenvalues of modulus at least one, if some ORIGINAL physical spectral row has leverage `>1/2` and physical diagonal exactly zero, then

`boxed: ||p_Q||_infinity <363.`                                 (4.6)

The transverse-diffuse subcase is in fact continuous with the sharper bound (4.5). This is a genuine partner splice: r28 pays one side of an exhaustive physical-row dichotomy and Section 3 pays the other.

## 5. Sharpened remaining debt

The same theorem also closes the **punctured double-heavy** state. If a heavy original row `i` has `c_i>1/2` and a second row has transverse leverage `>1/2`, Section 3 pays the form regardless of whether `A_ii` is zero, tiny, or large.

Moreover, if `|A_ii|>=1/32`, (3.5) already pays the form without a second heavy row. Therefore the only heavy-anchor state left by this B18 mechanism is

`boxed: 0<|A_ii|<1/32,  c_i>1/2,
        and  ||P_(n_i^perp)u_j||^2<=1/2  for every j!=i.}`      (5.1)

Call this `QFORM-NEARNULL-TRANSVERSE-DIFFUSE-COLLAR-v1`. It is genuinely nonzero, so the exact-null partner theorem cannot simply be invoked; deleting the small coefficient would violate the live unbounded-support correction. The next proof must retain this Rayleigh term quantitatively, or route it through a source-matching near-null mixed-Fresnel/collar theorem.

This is strictly narrower than the incoming debt: **all exact-null heavy anchors and all double-heavy punctured states are now paid** in exact rank three.

## 6. Primary-source boundary checked

The inherited Fourier/BL endpoint uses only source-matching classical inputs. Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1, assumes an actual product `f=prod_i f_i` of bounded one-dimensional probability densities and proves

`||pi_E f||_infinity
 <=min{(n/(n-k))^((n-k)/2), 2^(k/2)} prod_i ||f_i||_infinity^(gamma_i)`,

with `gamma_i in [0,1]` and `sum gamma_i=k`. Thus cap-one inputs give the exact `k=2` orthogonal-marginal cap `2`. Their Theorem 3.3 is the normalized geometric rank-one Brascamp--Lieb inequality used in the completed rank-two proof: unit vectors and positive weights satisfying `sum c_i u_i tensor u_i=I` imply the stated product-integral inequality. Neither theorem asserts independence of projected coordinates.

Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182, is the primary sharp Hausdorff--Young source used by the rank-two endpoint; the pinned proof states the exact normalization it uses. No theorem requiring moments, compact support, log-concavity, smoothness, centering, symmetry, iid inputs or spectral-coordinate independence was transferred.

The required pinned `COUNTEREXAMPLE_SEARCH.md` reports no valid QFORM counterexample and explicitly leaves the two-sheet/convex geometry as the delicate rank-three side. The present theorem does not reinterpret those numerical searches as novelty evidence; it supplies an exact physical-coordinate structural payment.

## 7. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a supporting exact-rank-three theorem and narrows one live structural branch. It does not handle arbitrary additional spectrum, and it does not claim full-target continuity.

No task identity, schedule, enabled state, notification/email setting, cross-account authentication, paid API/model call, public release, remote workflow, permission, installation, benchmark, or unrelated data was changed.
