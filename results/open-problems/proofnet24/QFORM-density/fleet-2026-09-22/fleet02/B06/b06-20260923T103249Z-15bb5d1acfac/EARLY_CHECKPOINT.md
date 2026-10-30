SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T10:32:49Z.
attacking: near-collinear transverse high-leverage branch: turn partner exact rank-three curvature into a product-weighted hub/row-volume payment, or exhibit a source-valid obstruction.

# Early checkpoint — determinant currency on the ruled side

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture remains OPEN. This checkpoint is supporting mathematics only.

Source pins actually consumed before this checkpoint:
- partner fleet03/B06 r32: `yspennstate/math-open-problems@9583647ef39bb355508b8f8fb49f05ded8b594f2`;
- newest-Claude package required by owner: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially Theorem F / Theorem C and the counterexample notes.

## 1. Determinant-only ruled-side extension

The newest-Claude ruled formula for a rank-three form with signature `(2,1)` is, on the one-sheet side,

`p(s) <= (abc)^(-1/2) integral_0^(2pi) [sin^2(theta)/a + cos^2(theta)/b + 1/c]^(-1/2) dtheta`,

where `a,b,c>0` are the absolute nonzero eigenvalues. The geometric derivation does not require `a,b,c>=1`; that hypothesis was only used in the source's final simplification.

Put `x=1/a`, `y=1/b`, `z=1/c`. Pointwise AM-GM gives

`x sin^2(theta)+y cos^2(theta)+z >= 3 (xyz)^(1/3)|sin(theta)cos(theta)|^(2/3)`.

Therefore

`p(s) <= C_R (abc)^(-1/3)`,

`C_R = [2/sqrt(3)] B(1/3,1/3) = 6.119816148228773...`.

Equivalently, for any rank-three indefinite packet `B` on its ruled side,

`p(s) <= C_R |pdet(B)|^(-1/3)`.

This uses the original product law through the source theorem's two-dimensional marginal/X-ray bound; it is not an arbitrary-joint coarea statement. The two-sheet side is not claimed.

## 2. Full null-pivot packet pseudodeterminant

In partner r32 notation, let `U=u.Z`, `V=v.Z`, `G=det Gram(u,v)>0`, let

`h=a u+b v+w`,  `w perp span(u,v)`,

and consider the whole null-pivot quadratic packet, including the genuine independent physical scalar `X`,

`Q_2 = 2k U [gamma X + h.Z] + beta V^2`,  `k beta gamma !=0`.

Define three coefficient vectors in the enlarged original product source `(X,Z)`:

`c_U=(0,u)`, `c_V=(0,v)`, `c_E=(gamma,h)`.

Then `Q_2 = (U,V,E) S (U,V,E)^T` with

`S=[[0,0,k],[0,beta,0],[k,0,0]]`, so `det S=-beta k^2`.

Column operations replace `c_E` by `(gamma,w)` without changing the Gram determinant, and this vector is orthogonal to `c_U,c_V`. Hence

`det Gram(c_U,c_V,c_E) = G (gamma^2+||w||^2)`

and therefore

`boxed: pdet(Q_2) = - beta k^2 G (gamma^2+||w||^2)`.

This strengthens the partner's background-only transverse identity `-beta k^2 G||w||^2`: after the genuinely independent scalar is retained, the determinant currency does not collapse as `w -> 0`.

Combining with the ruled-side extension gives, uniformly in the in-plane coefficients `a,b`,

`p_one-sheet(s) <= C_R [|beta| k^2 G (gamma^2+||w||^2)]^(-1/3)
                  <= C_R [|beta| k^2 gamma^2 G]^(-1/3)`.

## 3. Diffuse full-density splice with newest-Claude Theorem F

The same packet has exact rank three. If the range projection of the three coefficient vectors has every physical-coordinate leverage at most `1/2`, newest-Claude Theorem F applies directly and gives the full essential-density bound

`||p_Q2||_inf <= 12 [|beta| k^2 G (gamma^2+||w||^2)]^(-1/3)`.

Thus partner r32's spectral-imbalance problem is removed completely in the diffuse branch: no lower bound on the smallest singular value is needed, and the leverage gate improves from `1/32` to `1/2`. What remains is only the high-leverage two-sheet branch (plus any genuinely additional quadratic remainder not belonging to this exact packet).

Finite algebra check: 240 random instances in dimensions 3,5,9 gave maximum relative discrepancy `2.16e-14` between the product of the three nonzero ambient eigenvalues and `-beta k^2 G(gamma^2+||w||^2)`. This is a check, not a proof.
