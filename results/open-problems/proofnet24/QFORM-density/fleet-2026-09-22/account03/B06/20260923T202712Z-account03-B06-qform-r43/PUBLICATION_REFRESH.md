# r43 publication refresh and invariant rank-one innovation form

Final-source refresh observed `yspennstate/math-research-brain@7389cb618dbfd01d87b29746449528bea2359be1`. The protected owner control remains revision `2026-09-22.15`, programme revision `2026-09-22.5`, QFORM-only. The new concurrent handoff at that commit is a scoped independent-square product-band theorem; it explicitly leaves fully overlapping square directions and the full arbitrary-rank conjecture open, so it does not supersede r43.

The live correction inbox was reread after the r43 mathematics. In particular the fresh account03/B15 correction refutes a different nonzero-square affine-slope `L^(3/2)` shortcut; r43 does not use that shortcut. The r43 correction event is written immutably under its own event path and is left for the keeper/owner-authorized merger rather than racing a shared inbox update.

## Coordinate-symmetric form of the r43 rank-one theorem

For the rank-one nonzero hub core

`H=[[a,b],[b,d]]`

and the `2 x m` original-product slope matrix

`E=[[alpha^T],[beta^T]]`,

define

`J_1=||a beta-b alpha||_2`,
`J_2=||d alpha-b beta||_2`.

These are exactly the two row norms of `adj(H)E` (in reverse order), so

`J_H := ||adj(H) E||_F = sqrt(J_1^2+J_2^2)`.                    (1)

Theorem 3.1 in `REPORT.md` applies with pivot `a` whenever `a!=0` and gives

`||p_Q||_infinity <=2^(11/4) J_1^(-1/2)`.                       (2)

After swapping the two literal physical hub coordinates it gives, whenever `d!=0`,

`||p_Q||_infinity <=2^(11/4) J_2^(-1/2)`.                       (3)

A nonzero symmetric rank-one `H` has at least one nonzero diagonal. If both are nonzero choose the larger of `J_1,J_2`; if one diagonal is zero, rank one forces `b=0` and the corresponding unavailable innovation is itself zero. Hence in every case with `J_H>0`,

`max(J_1,J_2) >= J_H/sqrt(2)`

and one valid physical pivot realizes that maximum. Therefore the same proof yields the coordinate-symmetric corollary

`boxed: ||p_Q||_infinity <= 8 J_H^(-1/2).`                       (4)

Indeed `2^(11/4)*2^(1/4)=8`.

This makes the structural meaning of the unpaid endpoint explicit: `adj(H)` is the rank-one projector direction onto the physical hub null line up to scale, so `J_H` measures the complete original-coordinate cross coupling of that null line. When `J_H` is tiny, the missing third curvature cannot be manufactured by that hub-null cross coupling and must be sought in the retained environmental quadratic bank. This is the precise interface for the next `QFORM-NEARRANK1-HUB-THIRD-CURVATURE-BRIDGE-v1` step.

The concurrent independent-square all-level receiver may be useful in that next step if the retained third curvature supplies an original-coordinate square component with genuinely unused mass `rho>0`; no such decomposition is asserted here without proof.
