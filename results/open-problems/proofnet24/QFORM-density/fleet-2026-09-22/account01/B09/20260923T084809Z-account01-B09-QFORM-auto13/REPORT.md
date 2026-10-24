SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T08:48:09Z.
attacking: determinant-balanced multi-hub bilinear smoothing; extend the completed two-hub Pluecker mechanism to any number of untouched physical hubs and preserve a direct O(interval length) estimate.

# account01/B09 auto13 — determinant-balanced multi-hub Pluecker smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control observed: revision `2026-09-22.15`  
Role: bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution label: **WITHOUT_VERIFIED_BRAIN**

The unrestricted quadratic-form bounded-density conjecture remains OPEN. The result below is a source-coordinate smoothing theorem. It preserves arbitrary physical hub curvature, arbitrary conditioned outside curvature, and arbitrary affine terms. It proves a continuous density and a linear interval bound on its exact scope. It does not assert that the bare three-large-eigenvalue hypothesis automatically supplies the determinant-balanced frame.

## 1. Exact source inputs

The completed designated partner theorem used and extended is account02/B09 `QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T064043Z-account02-B09-QFORM-r13/REPORT.md`.

Its proof combines the source-coordinate mixed-hub Fresnel identity from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

with `QFORM-PLUCKER-ENTROPY-BL-v1` from

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`.

The only facts used here from those sources are:

1. after conditioning only disjoint original coordinates, each untouched physical hub integration contributes the exact Jacobian `(2|t|)^(-1)` while its quadratic hub-core phase has modulus one;
2. each displayed rank-one leaf square `lambda_k (v_k dot X_I)^2` contributes `(4 pi |t lambda_k|)^(-1/2)` after Fresnel linearisation;
3. for an `N x d` orthonormal coefficient frame `U`, if `rho` is the probability that two iid Pluecker bases are disjoint, the determinant-entropy Brascamp--Lieb estimate gives

`int_(R^d) prod_i |hat g_i(<U_i,z>+a_i)| dz <= (2pi)^d e^(d/2) rho^(-1/2)`

for the cap-one coordinate phases that arise here.

No law-uniform pointwise one-dimensional Fresnel decay, post-rotation independence, arbitrary-joint coarea, conditional density supremum, compact support, moments, log-concavity, or probability squaring is used.

## 2. New theorem

### Theorem `QFORM-MULTIHUB-PLUCKER-SMOOTHING-v1`

Split the original independent coordinates as

`H union I union J`,

where `H={h_1,...,h_h}` consists of `h>=1` literal physical coordinates, `I` is an untouched leaf bank, and `J` is a conditioned bank. Assume

`r+2h>2`.

After conditioning `X_J`, allow all generated affine terms. Suppose the exact leaf principal block is

`A_II = D + sum_(k=1)^r lambda_k v_k v_k^T`,

where `D` is diagonal, `r>=0`, and every displayed `lambda_k` is nonzero. Let

`c_a=A[I,h_a]`, `a=1,...,h`,

and form the deterministic coefficient matrix

`W=[v_1,...,v_r,c_1,...,c_h]`,
`d=r+h`,
`G=W^T W`.

Assume `G>0`, and whiten only this deterministic coefficient frame:

`U=W G^(-1/2)`, so `U^T U=I_d`.

For each `d`-subset `S` of leaf coordinates set

`w_S=det(U_S)^2`.

By Cauchy--Binet, `sum_S w_S=1`, so `w` is a probability law on bases. Let `S,T` be iid from this Pluecker law and define

`rho=P(S cap T=empty)`.

If `rho>0`, then the full quadratic form has a continuous density and

`boxed:
||p_Q||_infinity
 <= C_(h,r)
    [rho det(G) prod_(k=1)^r |lambda_k|]^(-1/(r+2h)),
`

where

`C_(h,r)=((r+2h)/(r+2h-2)) exp((r+h)/(r+2h)).`

Consequently, for every interval `L`,

`boxed:
P{Q in L}
 <= C_(h,r)
    [rho det(G) prod_k |lambda_k|]^(-1/(r+2h)) |L|.
`

The blocks `A_HH`, `A_HJ`, `A_IJ`, and `A_JJ` are arbitrary. In particular, the entire actual physical `h x h` hub core may be definite, indefinite, singular, near-null, or dense.

### Proof

Condition on the original coordinates `X_J`. This preserves independence and the density caps of the variables in `H union I`; it changes only affine terms and an additive constant in the remaining form.

Fix the leaf-frequency variable `t`. Integrate the `h` literal hub coordinates in the same source-coordinate order as in the partner proof. For fixed leaf variables, every term involving only the hubs contributes a phase of modulus one. The hub-to-leaf terms produce linear Fourier tilts. After the substitution

`y=2t x_H` in `R^h`,

the hub integrations contribute exactly

`(2|t|)^(-h)`.

Fresnel-linearise the `r` displayed leaf squares. Their absolute prefactor is

`prod_(k=1)^r (4 pi |t lambda_k|)^(-1/2)`.

After these two exact steps, the remaining coefficient integral has dimension

`d=r+h`

and has the form

`J_t=int_(R^d) prod_(i in I) |hat g_(i,t)(<W_i,z>+a_i)| dz`,

with `|g_(i,t)|=f_i`; the diagonal leaf coefficients and all conditioning-generated linear terms are harmless one-coordinate phases.

Whiten only the deterministic frame via `z'=G^(1/2)z`. Then

`J_t=det(G)^(-1/2)
      int_(R^d) prod_i |hat g_(i,t)(<U_i,z'>+a_i)| dz'.`

Apply the determinant-entropy Pluecker bound quoted above:

`J_t <= det(G)^(-1/2)(2pi)^d e^(d/2) rho^(-1/2).`

Combining all factors, the powers of two cancel exactly:

`2^(-h) * 2^(-r) * 2^(r+h)=1`,

while the powers of pi give

`pi^(-r/2) * pi^(r+h)=pi^(h+r/2)`.

Set

`alpha=h+r/2=(r+2h)/2 >1`.

Therefore

`|phi_Q(t)| <= A |t|^(-alpha)`,

where

`A=pi^alpha e^((r+h)/2)
   [rho det(G) prod_k |lambda_k|]^(-1/2).`

Together with `|phi_Q(t)|<=1`,

`int_R |phi_Q(t)| dt
 <= 2 alpha/(alpha-1) A^(1/alpha).`

Fourier inversion yields

`||p_Q||_infinity
 <= alpha/[pi(alpha-1)] A^(1/alpha)`

`= alpha/(alpha-1)
   exp((r+h)/(2alpha))
   [rho det(G) prod_k |lambda_k|]^(-1/(2alpha))`.

Since `2alpha=r+2h`, this is exactly

`((r+2h)/(r+2h-2)) exp((r+h)/(r+2h))
 [rho det(G) prod_k |lambda_k|]^(-1/(r+2h)).`

The characteristic function is integrable, so Fourier inversion supplies a continuous density. Integrating that density over an interval gives the stated linear small-ball estimate. QED.

## 3. Consistency with the designated partner

For `h=2`, the theorem reduces exactly to account02/B09's completed theorem:

`C_(2,r)=((r+4)/(r+2)) exp((r+2)/(r+4))`,

with exponent `-1/(r+4)`.

Thus this run does not rename a different result: it identifies and proves the full `h`-hub form of the same source-coordinate determinant-balanced mechanism.

For `h=3,r=0`, the new endpoint is especially simple:

`boxed:
||p_Q||_infinity <= (3/2) sqrt(e) [rho det(C^T C)]^(-1/6).
`

This retains an arbitrary physical `3 x 3` hub core and an arbitrary conditioned outside block, provided the surviving leaf self-block is diagonal.

For `h=1,r=1`, one obtains the determinant-balanced one-hub/one-square endpoint

`||p_Q||_infinity <=3 e^(2/3)
 [rho det(G)|lambda_1|]^(-1/3).`

This is valid whenever the two-dimensional Pluecker basis law has positive disjointness mass.

## 4. Required designated-partner result applied to an actual inequality

Apply the completed account02/B09 `h=2,r=0` theorem, not merely its proof, to the following target-valid source-coordinate family.

Let `m>=2`. Take two physical hubs `X_1,X_2`, two disjoint leaf groups of size `m`, and unit flat vectors `c_1,c_2` supported on the two respective groups. Add one independent physical coordinate `Z`. For `epsilon>0`, set

`Q_(2,m)=epsilon(X_1^2+X_2^2)
 +2X_1<c_1,Y>+2X_2<c_2,Y>+Z^2.`

The two hub-leaf blocks are orthogonal, so `Delta=det(C^TC)=1`. The rank-two Pluecker basis law chooses one coordinate from each group independently; hence

`rho_2=(1-1/m)^2`.

The partner theorem gives the actual inequality

`boxed:
||p_(Q_(2,m))||_infinity
 <=2sqrt(e)(1-1/m)^(-1/2).
`

For `m=16`,

`||p_(Q_(2,16))||_infinity <3.406`,

and the same coefficient multiplies every interval length.

This family satisfies the target spectral hypothesis for every `epsilon>0`: each of the two orthogonal grouped blocks

`[[epsilon,1],[1,0]]`

has one eigenvalue `(epsilon+sqrt(epsilon^2+4))/2>1`, and the independent `[1]` block from `Z^2` supplies a third eigenvalue of modulus one. Thus the displayed inequality is a literal target-valid application of the designated partner theorem.

## 5. New three-hub target-valid stress

Now take three physical hubs `X_1,X_2,X_3`, three mutually disjoint leaf groups of size `m`, and unit flat vectors `c_1,c_2,c_3` on those groups. Let

`Q_(3,m)=epsilon sum_(a=1)^3 X_a^2
 +2 sum_(a=1)^3 X_a <c_a,Y>.`

Here `C^T C=I_3`, so `det G=1`, and the rank-three Pluecker basis law picks one coordinate independently from each group. Therefore

`rho_3=(1-1/m)^3`.

The new `h=3,r=0` theorem gives

`boxed:
||p_(Q_(3,m))||_infinity
 <=(3/2)sqrt(e)(1-1/m)^(-1/2).
`

For `m=16`, this is

`||p_(Q_(3,16))||_infinity <2.555`.

The spectrum is the union of three copies of the spectrum of

`[[epsilon,1],[1,0]]`,

so it has at least three eigenvalues strictly larger than one in modulus on the positive side. Hence this is target-valid for every `epsilon>0`. The theorem would still allow an arbitrary dense `3 x 3` physical hub core; the diagonal choice here is only for a transparent spectral certificate.

## 6. Structural consequence and next unpaid implication

The analytic cost of adding an untouched physical hub is favorable: with no displayed same-side leaf curvature (`r=0`), the reciprocal determinant exponent falls from `1/4` for two hubs to `1/6` for three hubs, while the entire physical hub core remains free.

This gives a concrete routing target for the current small-disjointness/high-leverage frontier. When a two-hub determinant-balanced packet localizes onto a physical leaf or when a genuinely higher-rank same-side packet supplies another literal source-coordinate hub with an independent coupling direction, elevate that physical coordinate before paying reciprocal local minors. If the resulting three-hub coefficient frame has positive quantitative Pluecker disjointness, the theorem above closes it directly with an `O(|L|)` bound.

The first unpaid implication for this worker is therefore

`QFORM-HIGHRANK-LEAF-TO-MULTIHUB-FRAME-v1`:

> Starting from the current two-hub wedge plus a same-side bank operator that fails the determinant-balanced two-hub certificate through localization/high leverage, prove that either a third literal physical coordinate can be retained whose coupling row enlarges the source-coordinate coefficient frame with quantitative determinant/disjointness, or the localized packet lies in an already-paid finite-core, physical-pair, ridge, grouped-square, or cross-volume branch. The promotion must use the actual full matrix and must not delete small quadratic coefficients on unbounded inputs.

The low-rank identity `A_II=D+sum lambda_k v_kv_k^T` shows an important caveat: promoting a leaf whose only off-diagonal couplings are generated by the displayed `v_k` can create a new hub column lying in the old curvature span. Such a promotion does not automatically make `G` nonsingular. The remaining structural work must therefore distinguish genuine new physical coupling directions from algebraically redundant curvature directions.

## 7. Scope, continuity, and target status

On the exact theorem scope, the output density is continuous because the characteristic function is in `L^1`. The universal full-target continuity statement remains open because the spectral hypothesis has not yet been shown to force this packet.

The theorem and examples match all input-law quantifiers: every original coordinate remains independent and has only the density cap `<=1`; no moments, support bounds, connected support, Gaussianity, or log-concavity are used. No random coordinate rotation occurs.

Full QFORM remains OPEN. No counterexample to the conjecture is supplied here, and no claim of literature-wide novelty is made.