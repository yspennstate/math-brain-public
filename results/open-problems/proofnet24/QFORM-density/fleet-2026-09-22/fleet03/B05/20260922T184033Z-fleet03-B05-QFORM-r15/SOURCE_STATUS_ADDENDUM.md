# Source-status correction and the actual new B05 obstruction

**Run:** `20260922T184033Z-fleet03-B05-QFORM-r15`  
**Status:** source correction + new mechanism counterexample; full QFORM remains open.

## 1. Correction to the immutable REPORT.md

After committing `REPORT.md`, the required duplicate-source check found a stronger earlier theorem that already closes the full physical `n=3` scope:

`QFORM-FIXED-MATRIX-BOUNDED-v1`, complete analytic source

`yspennstate/math-open-problems@058acb5c8f9186ef199bbaf136b57f4dd9ea3800`

`proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`.

That theorem proves for every fixed symmetric matrix of rank at least three, using a nonsingular physical principal `3 x 3` block `B`,

`||p_Q||_infinity <= (2*pi+3*sqrt(3))/sigma_min(B)`.

Thus when the entire physical dimension is `n=3` and the owner hypothesis gives `sigma_min(A)>=1`, it already yields

`||p_Q||_infinity <=2*pi+3*sqrt(3) <11.48`.

Therefore `QFORM-PHYSICAL-N3-ENDTOEND-v1` in the immutable report is a **correct independent rederivation / structural synthesis, but not a new scope theorem**. Its larger constant is superseded by the earlier result. The immutable report is not rewritten; this addendum is the controlling source-status note.

Likewise, the qualitative fact that every fixed nonzero coloop pivot can be paid is already implicit in the completed rank-two affine half-Riesz source. The formula in the report improves the source constant in the zero-affine coloop specialization to `16*sqrt(30)` but should be treated as a sharpened corollary, not a new qualitative closure.

The genuinely new mathematical contribution of this run is the mechanism obstruction below.

## 2. A target-valid family on which the absolute half-Riesz bridge must lose a logarithm

The remaining coloop issue is the uniform transition from nonzero pivot `a` to the exact-zero theorem. A natural attempt is exactly the inequality used in the report:

`p_Q(t) <= |a|^(-1/2) E |R_a-t|^(-1/2)`                         (2.1)

obtained by completing the square in the untouched original coloop coordinate and then replacing its translated density by its cap one.

The next proposition shows that **this architecture cannot be uniform as `a ->0`**, even on an extremely simple target-valid three-coordinate product family whose true output densities are uniformly bounded.

### Proposition — `QFORM-NEARZERO-HALF-RIESZ-LOG-LOSS-v1`

For `0<a<=1/3`, put

`B_a=sqrt(1+a)`

and

`A_a = [[a,B_a,0],[B_a,0,0],[0,0,1]].`                              (2.2)

Let `X_0,X_1,X_2` be independent `Uniform[0,1]`. Then:

1. `A_a` has eigenvalues exactly `{1+a,-1,1}`. Hence it satisfies the owner target uniformly with `sigma_min(A_a)=1`.
2. The completed-square residual is

   `R_a = X_2^2 - ((1+a)/a) X_1^2`,                                  (2.3)

   so the scalar-shell / absolute-half-Riesz interface at `t=0` is

   `H(a):=a^(-1/2) E |R_a|^(-1/2)`.                                  (2.4)

3. For every `0<a<=1/3`,

   `boxed(
   H(a) >= (1/sqrt(1+a))
            log( sqrt((1+a)/a)/2 ).
   )`                                                                  (2.5)

   In particular `H(a) -> infinity` logarithmically as `a downarrow0`.
4. Nevertheless the **actual** densities of `X^T A_a X` are uniformly bounded by the earlier fixed-principal-triple theorem:

   `||p_{X^T A_a X}||_infinity <=2*pi+3*sqrt(3)`                      (2.6)

   for every `a` in this range.

Therefore the divergence in (2.5) is purely a proof-interface loss. Any near-zero coloop proof that first takes the absolute fractional trace in (2.1) cannot yield a universal constant.

### Proof

The `2 x 2` upper-left block in (2.2) has trace `a` and determinant `-(1+a)`, hence its two eigenvalues are `1+a` and `-1`. The third eigenvalue is `1`, proving item 1.

Complete the square in `X_0`:

`aX_0^2+2B_a X_0X_1+X_2^2`

`=a(X_0+(B_a/a)X_1)^2
  +X_2^2-(B_a^2/a)X_1^2`

`=a(X_0+(B_a/a)X_1)^2+R_a`,                                          (2.7)

which is item 2.

Set

`L=(1+a)/a`.

Since the inputs are uniform on `[0,1]`,

`H(a)
 =a^(-1/2) int_0^1 int_0^1 |y^2-Lx^2|^(-1/2) dx dy`.                 (2.8)

Make the change `u=sqrt(L)x`. Since

`a^(-1/2)L^(-1/2)=1/sqrt(1+a)`,

we obtain

`H(a)
 ={1/sqrt(1+a)}
   int_0^1 int_0^{sqrt(L)} |y^2-u^2|^(-1/2) du dy`.                  (2.9)

For `a<=1/3`, `L>=4`, so `sqrt(L)>=2`. Restrict (2.9) to

`0<=y<=1`, `2<=u<=sqrt(L)`.

On this region `u>y` and

`(u^2-y^2)^(-1/2) >= 1/u`,                                           (2.10)

because `sqrt(u^2-y^2)<=u`. Therefore

`H(a)
 >= {1/sqrt(1+a)} int_0^1 dy int_2^{sqrt(L)} du/u`

` = {1/sqrt(1+a)} log(sqrt(L)/2)`,                                   (2.11)

which is exactly (2.5). This tends to infinity like `(1/2)log(1/a)`.

Finally, the earlier fixed-principal-triple theorem applies directly to the whole `3 x 3` physical matrix `A_a`, whose smallest singular value is one. This gives (2.6). QED.

## 3. What factor is actually missing

The example isolates the lost factor more sharply than the generic statement “the half-Riesz constant blows up.” In (2.7), the critical translation of the scalar density is

`-(B_a/a) X_1`,

which sweeps a range of order `1/a`. Replacing the translated scalar density by the pointwise cap `1` **before** integrating over `X_1` treats every one of those moving critical locations as if the fixed density of `X_0` could simultaneously saturate there. The logarithm in (2.5) is exactly the tax for that discarded translation coherence.

This mirrors the preceding B05 scalar-conditioning correction: there, normalizing each scalar fiber erased its small mass; here, taking the absolute fractional trace after the square completion erases the fact that all moving critical translates use the **same fixed one-dimensional density**.

Hence the first unpaid implication should not be phrased as another absolute half-Riesz estimate. A viable near-zero theorem must retain the scalar density inside the joint coarea integral, for example in the form

`int f_0(x_0) rho_Y(y)
     delta(t-a x_0^2-2B_a x_0 y_1-y^T C y) dx_0 dy`,                  (3.1)

and exploit the moving translation before taking absolute envelope bounds. Equivalently, one needs a translation-coherent weighted coarea estimate, not a normalized or absolute worst-fiber inequality.

## 4. Source-valid next target

`QFORM-COLOOP-NEARZERO-WEIGHTED-COAREA-v1`:

> In the exact coloop geometry, for `|a|` small and `||Lambda^{-1}||<=1`, prove a uniform interval/density bound directly from the original product integral while retaining the fixed scalar factor `f_0(x_0)` through the moving critical translation. The theorem must recover the already-paid `a=0` hyperbolic-square endpoint and must not pass through `a^(-1/2) E|R_a-t|^(-1/2)`, because Proposition 2.1 proves that interface itself can diverge logarithmically on target-valid inputs.

This is a correction to a proof architecture, **not** a counterexample to QFORM. Full QFORM and continuity remain open.
