# Revision 2026-09-22.8 route check: uniform conditional 3-D projection cap is false

A late control refresh during this run advanced the OWNER CONTROL to revision `2026-09-22.8`. The owner message proposes a rank-three coarea route whose explicit open gap is a universal bound on the conditional 3-D spectral-projection density after conditioning on the complementary spectral coordinates.

That particular conditional-density implication is false under the exact target assumptions. This is consistent with the already-live `QFORM-UV-CONDITIONAL-CAP-FALSE` correction, but the following 4-variable embedding shows it directly at the exact 3-D interface.

Let `X_1,X_2,X_3,X_4` be independent `Uniform[0,1]` variables. Set

`U=(X_1+X_2)/sqrt(2)`, `V=(X_1-X_2)/sqrt(2)`,

and let the three selected spectral coordinates be

`Y=(U,X_3,X_4)`,

with complementary spectral coordinate `V`. The map `(X_1,X_2)->(U,V)` is orthogonal, so its Jacobian is one. The joint density of `(U,V)` is therefore one on the rotated unit square. For

`|v|<1/sqrt(2)`,

the allowed `u`-section is

`|v| <= u <= sqrt(2)-|v|`,

of length

`L(v)=sqrt(2)-2|v|`.

Hence

`p_V(v)=L(v)`

and the conditional law `U | (V=v)` is uniform on that section with density

`||p_{U|V=v}||_infinity = 1/L(v)
 = 1/(sqrt(2)-2|v|) -> infinity`

as `|v| -> 1/sqrt(2)`.

Because `X_3,X_4` remain independent of `(U,V)`, the conditional 3-D density satisfies

`||p_{(U,X_3,X_4)|V=v}||_infinity
 = 1/(sqrt(2)-2|v|)`,

and is therefore not uniformly bounded in `v`.

This is already an exact rank-three target geometry: take the orthonormal spectral directions corresponding to `U,e_3,e_4` with eigenvalues `(1,1,1)` and let the `V` direction have eigenvalue zero. Thus the statement

> the conditional density of the selected three spectral coordinates, given all complementary spectral coordinates, is universally bounded

is false even for product uniforms and a definite rank-three form.

This does **not** refute rank-three coarea itself and does **not** refute QFORM. It refutes only the proposed completion by a uniform conditional projection-density cap. The averaging over the complementary coordinate must remain inside the curved/coarea argument; taking a conditional `L^infinity` supremum first loses the compensation. This aligns with the live fiber-sup and conditional-cap corrections.
