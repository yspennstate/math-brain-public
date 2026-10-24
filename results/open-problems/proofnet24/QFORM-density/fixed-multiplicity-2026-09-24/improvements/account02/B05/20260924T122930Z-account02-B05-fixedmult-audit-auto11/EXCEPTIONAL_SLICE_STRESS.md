# QFORM-B05-EXCEPTIONAL-SLICE-STRESS-20260924

Run: `20260924T122930Z-account02-B05-fixedmult-audit-auto11`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This artifact records three exact cap-one product examples that delimit what a valid lower-threshold proof may assume. They are **not** counterexamples to the manuscript's 17-eigenvalue theorem. They are counterexamples to stronger slice shortcuts that the manuscript correctly avoids.

## 1. Bounded projected marginal, unbounded conditional rotated slices

Let `X_1,X_2` be independent uniforms on `[-1/2,1/2]`, and rotate orthogonally:

`Y=(X_1+X_2)/sqrt(2)`, `Z=(X_1-X_2)/sqrt(2)`.

The joint density of `(Y,Z)` is exactly one on `|Y|+|Z|<=1/sqrt(2)`. Therefore `p_Y(y)=sqrt(2)-2|y|` on its support, so `||p_Y||_infty=sqrt(2)`, in agreement with the manuscript's product-projection lemma. However `Z|Y=y` is uniform on a slice of length `sqrt(2)-2|y|`, so its conditional density is the reciprocal and tends to infinity at the boundary. Thus unconditional projection-density bounds cannot be reused as uniform conditional density caps after a rotation.

**Status:** exact counterexample to the shortcut; manuscript unaffected.

## 2. Indefinite two-coordinate fiber has a logarithmic critical singularity

Let `W_1,W_2` be independent uniforms on `[-1/2,1/2]` and let `q=2W_1W_2`. Direct integration gives, for `0<|z|<1/2`,

`p_q(z)=log(1/(2|z|))`.

Hence `p_q` is unbounded at the critical level. A valid coarea/fiber argument cannot replace the hyperbolic branch by an unrestricted finite fiber supremum. The manuscript's logarithmic envelope is of the correct qualitative type.

**Status:** exact counterexample to a bounded-hyperbolic-fiber shortcut; manuscript unaffected.

## 3. Scalar square profile is genuinely inverse-square-root singular

Let `Y` be uniform on `[-1/2,1/2]` and `T=Y^2`. Then `p_T(t)=t^{-1/2}` for `0<t<1/4`. Therefore a scalar pivot does not admit a uniform conditional-density cap. The manuscript's half-potential domination is necessary at this level of generality.

**Status:** exact counterexample to a bounded-square-profile shortcut; manuscript unaffected.

## Consequence for threshold reduction

Any attempt to replace the current order-five no-pivot receiver by a lower-order argument must preserve the original product structure through the integration itself. It may use bounded projected marginals, but it cannot infer bounded conditional rotated slices, and it cannot take unrestricted suprema over square or hyperbolic fibers. Exceptional critical slices must be integrated with their actual inverse-square-root/logarithmic kernels before averaging.

No `17 -> 16` or smaller theorem is claimed by this note.
