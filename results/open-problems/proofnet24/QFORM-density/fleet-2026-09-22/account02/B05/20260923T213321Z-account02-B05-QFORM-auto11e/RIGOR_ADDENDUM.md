# Rigor addendum — affine/sheared transverse square normalization

This addendum records the deterministic normalization used implicitly in `REPORT.md`, so that the fresh two-bank tube theorem is invoked with exactly its stated `+V^2/(2L)` geometry.

Start from

`Q=2HL+2bLP+lambda(V+sL+v0)^2+alpha L^2+beta L+gamma0`, `|lambda|>=1`.

Let `eps=sign(lambda)` and define

`V_* = sqrt(|lambda|)(V+sL+v0)`.

On each of the two independent three-dimensional banks, replace `(L_i,V_i,P_i)` by

`(L_i, sqrt(|lambda|)(V_i+sL_i), P_i)`,

and put the deterministic translation `sqrt(|lambda|)v0` into one bank. This is a deterministic invertible shear followed by a transverse scaling. It makes no independence claim about the coordinates within a bank and preserves independence between the two original-coordinate banks. The shear has determinant one; the scaling has determinant `sqrt(|lambda|)>=1`, so the transformed `(L,V_*)` marginal and three-dimensional joint density caps do not exceed the corresponding old caps. The one-dimensional law of `L` is unchanged.

Thus it suffices to treat

`Q=2HL+2bLP+eps V_*^2+alpha L^2+beta L+gamma0`.

For `eps=+1`, division by `2L` gives the tube centre

`H+bP+alpha L/2+beta/2+(gamma0-t+V_*^2)/(2L)`.

For `eps=-1`, replace `L` by `L_*=-L` in both product banks. The shell `r<=|L|<=2r` and all density caps are unchanged, and after division the tube centre becomes

`H+bP-alpha L_*/2+beta/2+(t-gamma0+V_*^2)/(2L_*)`.

Therefore the basic tube theorem applies exactly in both signs. In the stronger noncritical estimate its source parameter is `gamma=gamma0-t` in the positive-square case and `gamma=t-gamma0` in the negative-square case, so the noncritical gate is precisely

`|t-gamma0|>=1`.

This normalization uses only deterministic changes of the compressed bank coordinates. It neither rotates the original independent inputs nor asserts post-transformation coordinate independence.
