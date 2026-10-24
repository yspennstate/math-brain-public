# account01/B07 — aggregate cross-minor determinant smoothing and a fixed-cut obstruction

**Run:** `a01-b07-20260922T134418Z-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and dependencies

The owner target is the full arbitrary-product-law statement: for independent real coordinates with scalar densities at most one and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X`, or give a target-valid counterexample. Continuity is tracked separately.

This report proves a new aggregate-minor consequence of the regularized-determinant estimate and identifies an exact obstruction to replacing determinant-weighted averaging by one selected coordinate cut. It does **not** prove the full target.

Source-pinned inputs actually used:

1. **Regularized determinant theorem**, interactive report `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. For a physical cross block `B=A[I,J]`, `1<=q<2`, and left range leverage at most `q/2`, it gives
   
   `|phi_Q(t)| <= det(I + 2 q t^2 B B^T/(pi^2 e^2))^(-1/(4q))`.

   The `q=2` version is unconditional.
2. **Assigned partner account02/B07**, result `determinant-weighted disjoint-basis selection`, canonical report `yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`. For an orthonormal `n x 3` spectral frame `U`, with Pluecker weights `w_K=det(U_K)^2`, it defines
   
   `delta = sum_{K cap L=empty} w_K w_L`
   
   and proves the exact-rank/separable-residual density estimate `||p_Q||_infinity <= 3 e delta^(-1/3)`, together with its localized alternative when `delta` is small.

Fresh corrections used: pointwise law-uniform Fresnel decay is false; a single cross minor is insufficient; a good local principal block versus rank-three cross-cut dichotomy is false; conditioning on transformed variables does not preserve the scalar density cap. No such premise is used below.

## 2. Conditional end-to-end route

A sufficient route to the full theorem would be:

1. find a physical cut `I,J` (or a determinant-weighted mixture of cuts) carrying a universal amount of **aggregate third cross-minor mass**;
2. pay the coordinate-leverage obstruction without rotating the independent variables;
3. apply the regularized determinant estimate, which already tolerates arbitrary self-block phases, outside couplings, signs, and additional small singular values;
4. obtain `phi in L^1`, hence a bounded **continuous** density by Fourier inversion.

The first essential missing implication is step 2. Sections 3--6 make steps 1 and 3 exact and show by an explicit rank-three source-valid example that step 2 cannot be replaced by “choose one good cross cut”.

## 3. Aggregate exterior-minor version of the determinant theorem

For a real matrix `B` and integer `k>=1`, define

`E_k(B) = e_k(B B^T)`.

By Cauchy--Binet,

`E_k(B) = sum_{K,L, |K|=|L|=k} det(B[K,L])^2`,

where `K` ranges over row `k`-sets and `L` over column `k`-sets. Thus `E_k` is the total squared `k x k` cross-minor mass; no single minor is selected.

### Theorem `QFORM-AGGREGATE-CROSSMINOR-DETERMINANT-v1`

Let `I,J` be disjoint original-coordinate sets and `B=A[I,J]`. Fix `1<=q<=2`. If `q<2`, assume the diagonal of the orthogonal projection onto `range(B) subset R^I` is at most `q/2`; for `q=2` no leverage hypothesis is needed. Let `k` be an integer with

`k > 2q`.

If `E_k(B)>0`, then the law of `Q=X^T A X` has a continuous density, vanishing at infinity, and

`||p_Q||_infinity <= C_{k,q} E_k(B)^(-1/(2k))`,

where

`C_{k,q} = [e/sqrt(2q)] * [1/(2k)] * Beta(1/(2k), 1/(4q)-1/(2k))`.

In particular, at the three-direction threshold `q=1`, `k=3`,

`||p_Q||_infinity <= C_3 E_3(B)^(-1/6)`,

with

`C_3 = e/(6 sqrt(2)) Beta(1/6,1/12) = 5.655763773...`.

This replaces a lower bound on the **third individual singular value** by the determinant-weighted aggregate `E_3(B)`.

### Proof

The regularized determinant theorem gives

`|phi_Q(t)| <= det(I + beta t^2 B B^T)^(-1/(4q))`,

where `beta=2q/(pi^2 e^2)`.

If the eigenvalues of `B B^T` are `s_j^2`, then

`det(I+beta t^2 B B^T)
 = sum_{r>=0} beta^r t^(2r) e_r(BB^T)
 >= 1 + beta^k t^(2k) E_k(B)`.

Therefore

`|phi_Q(t)| <= (1 + beta^k E_k(B) t^(2k))^(-1/(4q))`.

Because `k>2q`, this majorant is integrable. With

`u = beta^(1/2) E_k(B)^(1/(2k)) |t|`,

Fourier inversion gives

`||p_Q||_infinity
 <= (1/pi) beta^(-1/2) E_k(B)^(-1/(2k))
    integral_0^infinity (1+u^(2k))^(-1/(4q)) du`.

The integral is

`[1/(2k)] Beta(1/(2k), 1/(4q)-1/(2k))`,

and `(1/pi) beta^(-1/2)=e/sqrt(2q)`. This proves the formula. Since the characteristic function is in `L^1`, Fourier inversion gives a continuous density vanishing at infinity. QED.

Two useful scopes are:

* `q=1,k=3`: three-minor aggregate smoothing under leverage `<=1/2`;
* `q=2,k=5`: unconditional five-minor aggregate smoothing, with constant `C_{5,2}=6.770121056...`.

The second is only a control; it does not change the three-eigenvalue target.

## 4. Exact determinant-weight accounting under coordinate conditioning

The regularized leverage condition itself has an exact determinant-decrement identity, so its failure can be tracked without paying one reciprocal minor.

Fix a cut `I,J`, frequency `t`, and `q`. Put

`z = 2q t^2/(pi^2 e^2)`,

`D_I(t)=det(I + z B^T B)`.

For a row `b_i^T` of `B` (`i in I`), define its regularized leverage

`d_i(t)= z b_i^T (I+z B^T B)^(-1) b_i`.

If `B_{-i}` denotes the matrix after conditioning/removing the original coordinate `i` from the left block, the matrix determinant lemma gives the exact identity

`D_{I\{i}}(t) = D_I(t) (1-d_i(t))`.

Thus the `q=1` obstruction `d_i(t)>1/2` has a precise meaning: conditioning that physical coordinate discards **more than half of the regularized determinant at that frequency**. The quantity

`sum_i d_i(t) = tr[z B^T B (I+z B^T B)^(-1)]`

is the effective rank at that scale.

This is the correct determinant currency for a stopping/selection argument. It also explains why repeatedly deleting high-leverage coordinates without another payment mechanism can destroy exactly the mass needed for Fourier integrability.

## 5. Exact exterior averaging identity and application of the assigned partner result

Now specialize temporarily to exact rank three,

`A = U Lambda U^T`, `U^T U=I_3`,

with invertible symmetric `Lambda`. For a coordinate triple `K`, put

`w_K=det(U_K)^2`,

so `sum_K w_K=1`. Let

`delta = sum_{K cap L=empty} w_K w_L`

be the partner's disjoint-basis probability.

For a cut `S,T=S^c`, write `B_S=A[S,T]`. Since `rank(B_S)<=3`, Cauchy--Binet gives the exact identity

`E_3(B_S)
 = |det Lambda|^2
   [sum_{K subset S, |K|=3} w_K]
   [sum_{L subset T, |L|=3} w_L]`.

Equivalently,

`E_3(B_S)=|det Lambda|^2 det(U_S^T U_S) det(U_T^T U_T)`.

Average over a uniform Bernoulli cut. A fixed disjoint ordered pair `(K,L)` is separated with `K subset S`, `L subset T` with probability exactly `2^-6`, while an overlapping pair can never be separated. Hence

`boxed( E_S E_3(B_S) = 2^-6 |det Lambda|^2 delta. )`

Consequently some cut satisfies

`E_3(B_S) >= |det Lambda|^2 delta/64`.

If that same cut obeys the `q=1` left- or right-range leverage gate, Theorem 3 gives

`||p_Q||_infinity
 <= 2 C_3 |det Lambda|^(-1/3) delta^(-1/6)
 = 11.311527546... |det Lambda|^(-1/3) delta^(-1/6)`.

For `delta>=1/8` and `|det Lambda|>=1`, this is below `15.997`.

This is a genuine application of account02/B07's completed `delta` invariant to an actual regularized-determinant density inequality. The exponent `delta^(-1/6)` here is not claimed to improve the partner's exact-rank bound `3e delta^(-1/3)`; the point is that the present route is compatible with the determinant theorem's arbitrary-self-phase architecture once a leverage payment is available.

## 6. Source-valid counterexample to the hoped-for single-cut leverage implication

The preceding averaging identity does **not** imply that a cut carrying `E_3` also satisfies the `q<2` leverage gate.

Take the exact rank-three frame in `R^6` with rows

`u_1=u_2=e_1/sqrt(2)`,
`u_3=u_4=e_2/sqrt(2)`,
`u_5=u_6=e_3/sqrt(2)`,

and take `Lambda=I_3` for simplicity. Then `U^T U=I_3`. The only nonzero Pluecker weights choose one coordinate from each pair; there are eight of them and each equals `1/8`. For every sampled basis there is exactly one disjoint sampled basis, so

`delta = 1/8`.

A coordinate cut has cross rank three **only if it splits every pair**, one coordinate to each side. For every such cut,

`U_S^T U_S=U_T^T U_T=(1/2)I_3`,

so

`E_3(B_S)=det(B_S B_S^T)=1/64`.

However each side then contains exactly three independent rows spanning its entire three-dimensional coordinate space. Therefore the orthogonal projection onto `range(B_S)` is the identity on that side: every coordinate leverage equals `1`.

Hence **every rank-three cross cut fails every fractional determinant gate `q<2`**, including the needed `q=1` threshold `1/2`, even though `delta=1/8` and the aggregate cross-minor mass is a fixed constant.

This is not a counterexample to QFORM. Indeed the assigned partner theorem applies directly and gives

`||p_Q||_infinity <= 3e (1/8)^(-1/3) = 6e`.

It is instead a decisive counterexample to the intermediate implication

> constant determinant-weighted disjoint-basis mass => existence of one rank-three cross cut with the required leverage cap.

Therefore the full proof cannot replace determinant-weighted averaging by a single fixed cut, even in a six-coordinate exact-rank-three model.

## 7. Full-matrix exterior accounting

For an arbitrary symmetric `A`, define the overlap classes

`M_r(A) = sum_{|K|=|L|=3, |K cap L|=r} det(A[K,L])^2`, `r=0,1,2,3`.

Then

`sum_{r=0}^3 M_r(A) = || wedge^3 A ||_F^2`.

If `A` has at least three eigenvalues of absolute value at least one, then

`||wedge^3 A||_F^2 >= ||wedge^3 A||_op^2 >= 1`.

Thus at least one overlap class carries mass at least `1/4`. Moreover, for a uniform random cut `S,S^c`,

`E_S E_3(A[S,S^c]) = M_0(A)/64`.

So the disjoint class `M_0` is already exactly converted into aggregate cross-minor mass. If `M_0>=1/4`, some cut has `E_3>=1/256`; with a valid `q=1` leverage payment Theorem 3 would give a universal continuous-density bound.

If `M_0<1/4`, at least `3/4` of the exterior-three mass lies in minors sharing one, two, or three physical coordinates. This is the precise mixed-minor remainder; it cannot be replaced by the already-refuted “one principal minor or one rank-three cross cut” dichotomy.

## 8. First surviving implication

The next target is `QFORM-DETERMINANT-MIXTURE-LEVERAGE-PAYMENT-v1`:

> Starting from the regularized determinant identity after original-coordinate decoupling, replace the fixed-cut `max leverage<=1/2` hypothesis by a determinant-weighted mixture/stopping argument that either (a) preserves enough aggregate `E_3` mass for an integrable `q=1` bound, or (b) sends the lost regularized determinant to an explicitly bounded set of original heavy coordinates and pays those coordinates by a separate product-preserving smoothing inequality.

The paired-frame example proves that branch (a) cannot always be represented by one cut. The partner's disjoint-basis entropy theorem supplies exactly the kind of mixture that succeeds in the exact-rank/separable-residual case. The remaining work is to carry that mixture through the arbitrary-self-phase / arbitrary-residual decoupling used by the regularized determinant theorem.

A second, equivalent full-matrix formulation is to pay the overlap classes `M_1,M_2,M_3` without a Schur-complement shortcut; the current correction inbox shows that a single scalar-pivot/rank-two-Schur extraction is false.

## 9. Status

`ESSENTIAL_STEP_APPLIED`:

* aggregate `k x k` coordinate-minor mass now directly controls the density under the exact determinant-theorem leverage scope;
* the `k=3,q=1` constant is explicit (`5.655763773...`);
* determinant loss under physical-coordinate conditioning is an exact multiplicative regularized-leverage factor;
* the assigned partner's `delta` invariant is linked exactly to average third cross-minor mass;
* a six-coordinate exact rank-three frame refutes the hoped-for reduction from determinant mass to one leverage-good cross cut.

`FULL_TARGET_OPEN`: the determinant-weighted mixture/heavy-coordinate payment and the mixed-overlap classes remain unresolved for arbitrary symmetric `A`.
