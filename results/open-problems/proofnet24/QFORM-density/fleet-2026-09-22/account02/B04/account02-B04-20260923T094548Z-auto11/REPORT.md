# account02/B04 — balanced third-volume support versus soft ridge on the same physical matrix

Run: `account02-B04-20260923T094548Z-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples  
Status: `PROVED SUPPORTING THEOREM / REFUTED INTERMEDIATE ROUTING / EXPLICIT TARGET-VALID ESTIMATE`; full QFORM remains OPEN.

## 0. First unpaid implication

The first unpaid implication is now

`QFORM-SUPPORT-DEFICIENT-DOUBLE-HUB-QUANTITATIVE-PAYMENT-v1`:

> In the low-total-tail / double-hub survivor, first separate mere failure of the soft-ridge gate from genuine failure of physical third-volume support balancing.  If q=1 support balancing fails, use the exact rank-3 base-packing defect proved below (coloop / at most three exceptions to a rank-1 flat / at most five nonzero rows) and combine it with determinant scale and the target spectral hypothesis to enter a completed coloop, grouped-bank, physical-pair, or half-Riesz endpoint without paying a vanishing individual coefficient.  If support balancing succeeds, optimize the determinant/entropy weight before routing to ridge.

The reason for inserting this support test is an explicit target-valid matrix below: both orientations fail the newest partner's fixed soft-ridge gate and therefore produce an aggregate double hub, but the q=1 third-volume law is perfectly balanced and globally optimal in the weighted-volume family.  Thus “double hub” alone is not the hard branch.

## 1. Sources and corrections actually used

The full target is the arbitrary product-law problem: independent one-dimensional probability densities bounded by one and real symmetric A with at least three eigenvalues of modulus at least one.  No moment, support, log-concavity, iid, Gaussian, diagonal-basis, or post-rotation-independence assumption is used here.

Corrections retained throughout: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea estimate; no positive moment of worst conditional projected-density caps; no universal good single physical minor or rank-three cross cut.

Three completed mathematical dependencies are used at equations.

1. **Claude/e5 Theorem D**, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`: for an original-coordinate cross block M with `Z=E3(M)>0`, any probability weight on nonzero physical 3x3 minors whose row marginals are at most 1/2 yields the product-Fourier density estimate with the corresponding determinant/entropy volume.  For the canonical squared-minor law the stated constant is `6 sqrt(e) Z^(-1/6)`.

2. **Sharp q-dependent weighted-volume theorem**, `yspennstate/math-open-problems@96ef944654c4056cc75bba6256e600eb791fb2d1`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`: if `1<=q<3/2` and the row marginals obey `alpha_i<=q/2`, then

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`,

where

`G(w)=exp(sum w_ST log det(M_ST)^2 + H(w))`.

The same-bank phases may be arbitrary measurable functions and outside coordinates may be conditioned on; no random-coordinate rotation is used.  The resulting density is continuous and vanishes at infinity.

3. **Designated partner account03/B04 r30**, canonical report `yspennstate/math-open-problems@1e5343fdf008f0da0d800b028dcfeec46550b1b0`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T091659Z-account03-B04-qform-auto11-r30/REPORT.md`: for `T2=sum_{j>=3}s_j(M)^2`, at `theta=1/3` the fixed soft-ridge exit succeeds if `max diag K<=1/3`, where

`K=MM^T(MM^T+(T2/3)I)^(-1)`.

If both M and M^T fail this gate, the theorem produces an aggregate physical row and column hub.  This run applies that result to an explicit obstruction.

For the direct ridge comparison I also use the completed ridge theorem source-pinned in account03/B04 r24: if

`K_gamma=MM^T(gamma^2 I+MM^T)^(-1)`, `theta_gamma=tr K_gamma`,

`max_i(K_gamma)_ii<=1/2`, and `theta_gamma>2`, then

`||p_Q||inf <= sqrt(e)/(sqrt(2) gamma) * theta_gamma/(theta_gamma-2)`.

All self blocks and outside couplings are unrestricted.

## 2. New support theorem: q=1 admissibility is exactly two-base packing

Let M be any real physical cross block of rank at least three.  On its row set E consider the rank-three truncation matroid `N`: a triple `S subset E` is a base exactly when the three physical rows of M indexed by S are linearly independent.  Equivalently, S is a base exactly when there exists at least one physical column triple T with

`det M[S,T] != 0`.

Let `r(A)` denote the rank function of this truncation, so `0<=r(A)<=3`.

### Theorem `QFORM-THIRDVOLUME-Q1-BASEPACKING-v1`

The following are equivalent.

1. There is a probability weight `w_ST` supported on nonzero physical 3x3 minors such that every physical row inclusion marginal

`alpha_i=sum_{S,T:i in S} w_ST`

satisfies `alpha_i<=1/2`.

2. The rank-three row matroid N contains two disjoint bases.

#### Proof: disjoint bases imply an admissible minor law

Let `B1,B2` be disjoint row bases.  Since each Bk has row rank three, choose a physical column triple `Tk` with `det M[Bk,Tk] != 0`.  Put probability `1/2` on each of the two minors `(B1,T1)` and `(B2,T2)`.  A physical row occurs in at most one of the two bases, so every row marginal is at most `1/2`.

#### Proof: an admissible law implies two disjoint bases

Project w to a probability law `mu` on the row bases.  For any subset `A subset E`, every base B satisfies

`|B \ A| >= 3-r(A)`.

Averaging gives

`3-r(A) <= E_mu |B\A| = sum_{i in E\A} alpha_i <= |E\A|/2`.

Thus for every A,

`2(3-r(A)) <= |E\A|`.                                      (2.1)

The Edmonds matroid base-packing theorem says that a rank-three matroid contains two disjoint bases if and only if (2.1) holds for every A.  Hence N has two disjoint bases.  QED.

The base-packing statement is standard and follows from the matroid union theorem.  The useful point here is that the Fourier marginal gate has become an exact combinatorial support condition in ORIGINAL physical coordinates.

### Corollary: exact support-defect trichotomy

If no q=1 supported third-volume weighting exists, the base-packing theorem supplies A with

`|E\A| < 2(3-r(A))`.

Only three cases can occur.

- `r(A)=2`: `|E\A|<2`.  Since total rank is three, exactly one physical row lies outside A.  That row belongs to every rank-three row basis: it is a genuine coloop.
- `r(A)=1`: `|E\A|<4`, so all but at most three physical rows lie in one rank-one flat.
- `r(A)=0`: `|E\A|<6`.  Enlarging A by all zero rows preserves rank zero, so M has at most five nonzero physical rows.

This is a support theorem only.  It does not lower-bound any nonzero determinant, so determinant/entropy degeneration remains a quantitative debt.

## 3. A balanced matrix that defeats the “double hub = hard branch” interpretation

Define the explicit orthogonal matrix

`S=(1/7) [[ 6,-2,-3],
           [-2, 3,-6],
           [-3,-6,-2]]`.

Direct multiplication gives `S^T S=I_3` and `det S=-1`; all nine entries are nonzero.

Define `U,V in R^(6x3)` by three signed row pairs:

`U_(2j-1)= e_j/sqrt(2)`, `U_(2j)= -e_j/sqrt(2)`, `j=1,2,3`,

and

`V_(2k-1)= s_k/sqrt(2)`, `V_(2k)= -s_k/sqrt(2)`, `k=1,2,3`,

where `s_k` is row k of S.  Then `U^T U=V^T V=I_3`, and every physical row of either frame has squared norm `1/2`.

Let

`D=diag(4,2,1)`, `M=UDV^T`.

Its singular values are exactly `(4,2,1)`.  In physical coordinates,

`M =`

`[[ 12/7,-12/7, -4/7, 4/7, -6/7, 6/7],`
` [-12/7, 12/7,  4/7,-4/7,  6/7,-6/7],`
` [ -2/7,  2/7,  3/7,-3/7, -6/7, 6/7],`
` [  2/7, -2/7, -3/7, 3/7,  6/7,-6/7],`
` [ -3/14, 3/14,-3/7, 3/7, -1/7, 1/7],`
` [  3/14,-3/14, 3/7,-3/7,  1/7,-1/7]].`

Thus every one of its 36 physical cross coefficients is nonzero.

### Exact minor structure

Because each U row lies on exactly one of the three coordinate axes, a nonzero three-row determinant must choose exactly one member from each U pair.  There are `2^3=8` such row triples, each with

`|det U_S|=1/(2 sqrt(2))`.

The same is true for V because its three row directions form the orthonormal basis given by S.  There are eight nonzero column triples, each with

`|det V_T|=1/(2 sqrt(2))`.

Therefore precisely `8*8=64` physical 3x3 minors of M are nonzero, and for every one,

`|det M[S,T]| = |det U_S| det D |det V_T|`

`                 = (1/(2sqrt(2))) * 8 * (1/(2sqrt(2)))`

`                 = 1`.                                      (3.1)

Consequently

`E3(M)=64`.                                                    (3.2)

The canonical squared-minor law is uniform on the 64 minors.  Each physical row occurs in exactly half of the eight admissible row triples, hence every row marginal is exactly `1/2`; likewise every column marginal is `1/2`.

## 4. Global optimization of the weighted-volume certificate on this M

For an arbitrary probability weight w supported on the 64 nonzero minors, (3.1) gives

`G(w)=exp(sum w log 1 + H(w))=exp(H(w))`.

Entropy on 64 points obeys `H(w)<=log 64`, with equality only for the uniform law.  Hence

`G(w)<=64`,                                                     (4.1)

and the uniform law is already q=1 admissible.

For the sharp q-dependent volume theorem, the scalar coefficient is

`C(q)=3e/[(3-2q)sqrt(q)]`, `1<=q<3/2`.

Its logarithmic derivative is

`d/dq log C(q)=2/(3-2q)-1/(2q)`

`                =3(2q-1)/(2q(3-2q)) >0`                    (4.2)

for every q in the allowed interval.  Combining (4.1)-(4.2), the global minimum of the entire supported weighted-volume certificate over **all** w and all admissible `1<=q<3/2` is attained uniquely by the uniform minor law at q=1.  It gives

`||p_Q||inf <= 3e * 64^(-1/6)`

`             = 3e/2`

`             = 4.077422742688568...`.                       (4.3)

This is a genuine global entropy-weight optimization for this physical matrix, not a symmetric ansatz.

### Required application of the completed e5 result

The same uniform law has row marginals exactly `1/2`, so Claude/e5 Theorem D applies directly to the actual quadratic form with this cross block.  Since `E3=64`, it gives

`||p_Q||inf <= 6sqrt(e) * 64^(-1/6)`

`             = 3sqrt(e)`

`             = 4.946163812100385...`.                       (4.4)

Equation (4.4) is the requested equation-level application of a completed result from the pinned e5 source.  Equation (4.3) uses the later sharp-Hausdorff-Young refinement of the same product-space mechanism.

## 5. The newest designated partner gate fails in both orientations

Apply account03/B04 r30 at its fixed intrinsic scale `theta=1/3`.  Since the singular values are `(4,2,1)`,

`T2=sum_{j>=3}s_j^2=1`.

The three nonzero eigenvalues of

`K=MM^T(MM^T+(1/3)I)^(-1)`

are

`16/(16+1/3)=48/49`,

`4/(4+1/3)=12/13`,

`1/(1+1/3)=3/4`.                                              (5.1)

Because the U rows are signed half-axis vectors, the six physical row diagonal entries are

`24/49,24/49,6/13,6/13,3/8,3/8`.                            (5.2)

In particular `max diag K=24/49>1/3`, so the row-side fixed-scale partner exit fails.

For the transpose, the same singular-mode eigenvalues occur and each V row has squared norm `1/2`.  Since the smallest eigenvalue in (5.1) is `3/4`, every physical column diagonal obeys

`(K_transpose)_jj >= (3/4)*(1/2)=3/8>1/3`.                  (5.3)

Thus the partner exit fails in both orientations and its theorem produces the aggregate row/column double-hub survivor.

But Sections 3-4 show that the physical third-volume support is maximally well balanced: q=1 is feasible with equality in every row marginal, and the uniform weighting globally maximizes G.  Therefore the implication

`both soft-ridge gates fail  =>  third-volume branch is hard/unavailable`

is false.  The correct remaining structural condition must mention support deficiency or determinant/entropy scale in addition to hub concentration.

This is a source-valid counterexample to an intermediate routing idea, not a counterexample to QFORM.

## 6. Same physical matrix: direct ridge versus volume

To compare mechanisms on the identical cross block, apply the completed direct ridge theorem with

`gamma=1/sqrt(2)`, so `gamma^2=1/2`.

The singular-mode ridge eigenvalues are

`32/33, 8/9, 2/3`.                                           (6.1)

On the U side the maximum physical diagonal is half the largest mode:

`max_i (K_gamma)_ii =16/33 <1/2`.                            (6.2)

The trace is

`theta_gamma=32/33+8/9+2/3=250/99>2`.                       (6.3)

Hence the ridge theorem applies and gives the explicit certificate

`||p_Q||inf`

` <= sqrt(e)/(sqrt(2)gamma) * theta_gamma/(theta_gamma-2)`

` = sqrt(e) * (250/99)/(52/99)`

` = (125/26)sqrt(e)`

` = 7.926544570673695...`.                                   (6.4)

No claim is needed about global optimization of the ridge scale.  The valid same-scale comparison is already strict:

`3e/2 = 4.07742...   <   3sqrt(e)=4.94616...   <   (125/26)sqrt(e)=7.92654...`.

So on this physical matrix the entropy-balanced three-volume route is stronger than the displayed ridge certificate, while the partner's fixed-scale soft-ridge test fails in both orientations.

## 7. Explicit genuinely rotated indefinite target

Embed M as

`A = [[0,M],[M^T,0]]`,

an explicit 12x12 symmetric matrix in the original product coordinates.  The nonzero eigenvalues of such a block matrix are the signed singular values of M, hence

`spec(A)={+4,+2,+1,-4,-2,-1,0,0,0,0,0,0}`.                 (7.1)

Thus A is indefinite, non-diagonal in the physical product coordinates, every physical cross entry is nonzero, and six eigenvalues satisfy the target threshold `|lambda|>=1`.

For every collection of independent real input variables with one-dimensional densities bounded by one, the sharp product-Fourier estimate (4.3) gives

`boxed: ||p_(X^T A X)||inf <= 3e/2 = 4.077422742688568...`.  (7.2)

The source theorem yields a continuous C0 density for this displayed family.  No continuity claim is made here for the unrestricted conjecture.

## 8. What changed in the proof map

1. **New exact structural fact.** q=1 third-volume support admissibility is equivalent to two disjoint bases in the rank-three truncation of the physical row matroid.  Therefore failure is not an amorphous “concentrated marginal” event: it forces a coloop, a rank-one-flat-with-at-most-three-exceptions geometry, or at most five nonzero rows.

2. **New routing obstruction.** Both orientations of the newest partner soft-ridge test can fail on a matrix whose q=1 minor law is perfectly balanced and globally optimal.  Aggregate double hub alone is therefore not the right terminal hard class.

3. **Required e5 theorem applied.** The completed e5 Theorem D gives the concrete bound `3sqrt(e)` on the target-valid matrix (7.1).

4. **Same-matrix optimized comparison.** The sharp weighted-volume certificate is `3e/2`, while a valid direct ridge certificate is `(125/26)sqrt(e)`.

5. **Remaining quantitative debt.** The base-packing theorem sees only zero versus nonzero minors.  A full proof still needs a universal way to combine this support classification with determinant/entropy magnitude and the three-large-eigenvalue hypothesis.  In particular, when two disjoint physical row bases exist but every lift to nonzero column triples has tiny determinant product, one must show that a ridge/grouped/hub/pair endpoint becomes available before that tiny scale is inverted.

Full QFORM remains OPEN.  This run does not use or revive any refuted pointwise-decay, arbitrary-joint coarea, conditional-cap, or post-rotation-independence premise.
