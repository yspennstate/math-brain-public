SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T10:37:52Z.
attacking: grouped mixed-hub smoothing for an actual source-coordinate star with dense same-side curvature, retaining original-coordinate product provenance and a direct linear interval bound.

# account02/B09 — grouped one-hub mixed-frame smoothing with dense hub curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This run gives a clean grouped one-hub corollary of the newest partner theorem and applies the required `e5f71d79...` mixed-hub theorem to an exact full-target family. No post-rotation independence, moments, support restrictions, log-concavity, diagonal-basis reduction, probability squaring, or square-root decoupling is used.

## 1. First unpaid implication

`QFORM-GENERAL-LEAF-CURVATURE-PACKET-OR-CROSSVOLUME-v1`:

Starting only from `s_3(A)>=1`, in the remaining no-small-pivot/hub geometry, force one of:

1. a grouped source-coordinate hub/star for which the opposite-bank curvature admits a determinant-balanced diagonal-plus-low-rank packet with a uniformly useful mixed-frame certificate;
2. an already-paid cross-volume / physical-pair / ridge / definite / multi-hyperbolic exit; or
3. a genuinely general opposite-bank curvature operator that must be retained inside a new phase-sensitive estimate rather than conditioned away or replaced by a worst conditional density supremum.

The newest partner theorem pays arbitrary curvature on the grouped hub bank, but not arbitrary curvature on the opposite leaf bank. That is now the clean B09 frontier.

## 2. Source-pinned completed inputs


Required analytic source:

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its completed mixed-hub Theorem H works directly in original product coordinates. With one physical hub, one spread square, and leaf mixed-frame Gram `G`, it gives an integrable `|t|^{-3/2}` characteristic-function envelope and therefore

`||p_Q||_infinity <= 3*2^(4/3) [|lambda| det G]^(-1/3)`            (2.1)

under the stated leverage condition. Arbitrary outside blocks survive conditioning.

Newest completed designated partner result:

account03/B09 `QFORM-GROUPED-HUB-PLUCKER-SMOOTHING-v1`, canonical source
`math-open-problems@ba035d3e65b7687b9ec8c05320f6340caabc34bb`.

Split original coordinates as `H union I union J`, condition only `J`, and factor

`A[H,I]=P C^T`, `P^T P=I_h`.

If

`A_II=D+sum_(k=1)^r lambda_k v_k v_k^T`,
`W=[v_1,...,v_r,C]`, `G=W^T W>0`,

and `rho` is the disjoint-basis mass of the whitened `(r+h)`-frame, then the partner product-law corollary gives

`||p_Q||_infinity <= e (r+2h)/(r+2h-2)
 [rho det(G) prod_k |lambda_k|]^(-1/(r+2h))`                    (2.2)

whenever `r+2h>2`. The same coefficient multiplies every interval length, and the density is continuous. Crucially `A_HH` is arbitrary: after disintegrating under `Y=P^T X_H`, all hub-bank curvature is retained in the bounded complex amplitude

`a_t(y)=p_Y(y) E[exp(it F_H(X_H)) | Y=y]`,

so no independence of projected hub coordinates is asserted.

## 3. New specialized theorem: grouped one-hub dense-hub-curvature smoothing

### Theorem `QFORM-GROUPED-ONEHUB-DENSE-HUB-CURVATURE-v1`

Partition the original independent coordinates as `H union I union J`. Assume the physical cross block has rank one,

`A[H,I]=p c^T`, with `||p||_2=1`,                              (3.1)

and the exact leaf block has

`A_II=D+lambda v v^T`, `lambda != 0`,                           (3.2)

with `D` diagonal. Set

`Delta=||v||_2^2 ||c||_2^2 - <v,c>^2 >0`.                      (3.3)

Let `U=[v,c] G^(-1/2)`, where

`G=[[||v||^2,<v,c>],[<v,c>,||c||^2]]`,

and let `rho>0` be the probability that two iid Pluecker bases drawn from the squared-minor law of `U` are disjoint.

Then, with completely arbitrary `A_HH` and arbitrary blocks involving the conditioned bank `J`,

`boxed: ||p_Q||_infinity <= 3 e [rho |lambda| Delta]^(-1/3).`   (3.4)

Moreover the density is continuous and

`boxed: P{Q in L} <= 3 e [rho |lambda| Delta]^(-1/3) |L|`       (3.5)

for every interval `L`.

### Proof

Apply the partner theorem (2.2) with `h=r=1`. Then `det G=Delta`, and

`e (r+2h)/(r+2h-2)=e*3/1=3e`.

Nothing is conditioned inside the hub bank `H`; its complete quadratic form is absorbed into the conditional phase amplitude. Thus dense, indefinite, singular, or large same-side hub curvature is retained exactly. Since the characteristic function has an integrable envelope, (3.5) is a direct linear small-ball estimate rather than a square-root conversion. QED.

The quantity `Delta=||v wedge c||^2` is the exact source-coordinate transversality resource. It is not a rotated-independence statement.

## 4. Required `e5f71d79...` theorem applied to an actual target inequality

Let a single original physical hub be `X_0`. Let the leaf bank consist of two disjoint groups of `m>=2` coordinates. Put

`c=m^(-1/2) 1_(first group)`,
`v=m^(-1/2) 1_(second group)`.

Then `c,v` are orthonormal, the mixed-frame Gram is `G=I_2`, and every row leverage is `1/m<=1/2`. Consider

`Q_m=2 X_0 <c,X_I> + <v,X_I>^2`.                               (4.1)

In the deterministic coefficient basis `{e_0,c,v}` the matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,

so its nonzero spectrum is exactly `{1,-1,1}`. This is therefore a literal full-target family for every `m`.

Applying completed Theorem H from the required `e5f71d79...` source gives

`boxed: ||p_(Q_m)||_infinity <= 3*2^(4/3) < 7.560`,             (4.2)

and hence

`boxed: P{Q_m in L} <= 3*2^(4/3) |L|`.                         (4.3)

The same-side leaf coupling `<v,X_I>^2` is dense on its physical group. The proof acts on original leaf coordinates and does not treat `<c,X_I>` and `<v,X_I>` as independent random variables.

## 5. Designated-partner theorem applied to a target family with dense same-side hub curvature

Take a disjoint hub bank `H` with orthonormal flat vectors `p,w`, and a disjoint leaf bank `I` with orthonormal vectors `c,v`, where `c` and `v` are flat on two disjoint groups of size `m`. Define

`F_m=2 <p,X_H><c,X_I> + <v,X_I>^2 + <w,X_H>^2`.                (5.1)

The projected variables `<p,X_H>` and `<w,X_H>` are generally dependent; no independence is assumed. The full `H x H` block is the dense rank-one matrix `w w^T`, which is retained inside the partner theorem's arbitrary hub phase.

On the coefficient subspace `{p,c,v,w}`, the matrix is the direct sum of a hyperbolic block and two positive squares, hence

`spec_nonzero(F_m)={1,-1,1,1}`.                                (5.2)

Thus this is again target-valid. Here `lambda=1`, `Delta=1`, and the squared-minor basis law chooses one leaf coordinate from each group, so

`rho=(1-1/m)^2`.                                                (5.3)

The new corollary (3.4), i.e. the completed account03/B09 theorem at this actual inequality, gives

`boxed: ||p_(F_m)||_infinity <= 3e (1-1/m)^(-2/3).`             (5.4)

For `m=16`, the right side is `8.5133708559...`; as `m` grows it tends to `3e=8.1548454854...`. The same coefficient multiplies `|L|`.

If `p,w` are flat on a hub bank of size `N`, then physical cross coefficients are `O((Nm)^(-1/2))`, the dense hub-square coefficients are `O(N^-1)`, and the dense leaf-square coefficients are `O(m^-1)`, while (5.4) stays dimension-free.

## 6. Boundary and remaining debt

This run does **not** prove that an arbitrary leaf operator `A_II` can be replaced by `D+lambda vv^T`, nor that `rho |lambda| Delta` is forced at universal scale by `s_3(A)>=1`. The partner theorem removes the arbitrary-curvature obstruction on the grouped **hub** side only. The surviving structural/analytic debt is exactly the implication stated in Section 1.

The required counterexample-search source reports no valid counterexample to full QFORM; it also does not close this leaf-curvature routing gap. Full QFORM and full-target continuity therefore remain OPEN.
