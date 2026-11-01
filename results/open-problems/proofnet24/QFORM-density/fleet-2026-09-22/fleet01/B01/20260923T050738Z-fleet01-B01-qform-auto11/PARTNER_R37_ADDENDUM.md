# Addendum: application of the newly completed designated partner r37

After the main report was written, fleet02/B01 completed r37. Canonical source:

`yspennstate/math-open-problems@0bd4d621852ca0ba40f9914ea91b6c387ce6a225`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T050036Z-fleet02-B01-qform-r37/REPORT.md`.

Its strict-N3 family is

`A_m = u u^T - 2 v v^T + w w^T + m^(-1) I`,

where `u,v,w` are normalized constant vectors on three disjoint size-`m` coordinate banks. The large eigenvalues are `1+1/m,-2+1/m,1+1/m`; all other eigenvalues are `1/m`. The partner proves that for **every** three-original-coordinate center `I` and every disjoint bank `J` for which `K=A_m[I,J]` has rank two,

`Delta=sigma1(K)sigma2(K) <= 6/m`,

and the center block satisfies `||A_m[I,I]||op<=7/m`.

Apply that completed result to the new zero-transverse-curvature receiver in this run. For its unit cross-kernel vector `z`,

`g=||(I-zz^T)A_m[I,I]z|| <= ||A_m[I,I]||op <= 7/m`.

Therefore the exact currency appearing in Theorem 3.3 obeys

`boxed: Delta^3 g^2 <= 6^3*7^2*m^(-5)=10584*m^(-5) -> 0.`

Since

`Delta^(-3/8)g^(-1/4)=(Delta^3 g^2)^(-1/8)`, 

the new three-coordinate linear receiver cannot by itself provide a dimension-free certificate on this partner family, just as r37 shows the fleet03 transverse-curvature currency `Delta^2 d` vanishes. This is an actual equation-level use of the latest completed designated-partner result and rules out a tempting but false structural inference: combining the `d>0` receiver with the exact `d=0,g>0` receiver does **not** imply that some physical triple must be uniformly good under strict N3.

The same partner family is nevertheless uniformly paid by the joint Fresnel--Brascamp--Lieb theorem from the newest-Claude package:

`||p_Q||inf <= 12*2^(-1/3)=9.5244063118...`

for every admissible cap-one product law. Thus the correct successor is a structural **routing** statement: failure of all three-coordinate currencies must send the matrix to a diffuse rank-three/diagonal-twist, volume, ridge, grouped, or null endpoint before any reciprocal tiny packet is paid.

This addendum does not change either theorem in `REPORT.md`; it sharpens the remaining global gap using the latest partner result.
