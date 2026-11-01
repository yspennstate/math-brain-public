# fleet02/B18 latest-partner addendum

Run: `b18-20260923T180826Z-cd3f2e4b`.

After the main REPORT was published, the designated partner fleet03/B18 published a newer completed r32 at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T182225Z-fleet03-B18-QFORM-r32/REPORT.md`.

It is compatible with `QFORM-NULLHUB-PLANAR-TWIST-CLOSURE-v1` and does not invalidate the main report.

## Latest partner theorem actually applied

The partner proves `QFORM-NULLHUB-SOURCE-SEPARATED-SHEAR-v1`: in the exact-rank-three null-hub normal form

`Q=2(X0+ell·X_L)(g·X_L)+d(beta·X_L)^2`,

if the original leaf indices split as `J disjoint_union K` with `g_K=beta_K=0` and

`ell_J=a g_J/gamma+b beta_J`,

then

`||p_Q||_infinity <= 6*2^(2/3)(|d|gamma^2)^(-1/3)`,

and the density is continuous and vanishes at infinity. The proof retains genuine independence only between the disjoint original source blocks and uses the LPP two-dimensional joint marginal cap; it does not infer independence of the projected pair.

Apply this latest theorem to the target-valid family from the main REPORT:

`u=(sqrt(2/3),-1/sqrt(6),-1/sqrt(6))`,
`beta=(0,1/sqrt(2),-1/sqrt(2))`,
`g=4u`, `d=4`, `ell=beta`,

`Q=4[2(X0+beta·X)(u·X)+(beta·X)^2]`.

Here take `J={1,2,3}`, `K=emptyset`, `a=0`, `b=1`, `gamma=4`. Therefore the latest partner gives the concrete whole-line target inequality

`||p_Q||_infinity <= 6*2^(2/3)*64^(-1/3)`
`                   = (3/2)*2^(2/3)`
`                   = 2.381101577952299...`,

with a continuous `C_0` density.

The planar-twist theorem in the main REPORT is sharper numerically on this same family: its uniform scalar envelope gives `9^(1/3)=2.080083823051904...`, and the exact pure-hub branch gives `2.009037710678627...`; continuity was deliberately not claimed for those sharper certificates.

Thus the new partner result supplies an independent provenance-safe closure of the same genuine target example and confirms that the rank-two physical partner cross block is not itself an obstruction. It also covers source-separated shear states arbitrarily close to `q_i=1`, whereas the planar-twist certificate deteriorates as `(1-q_i)^(-1/3)`. The remaining local debt is therefore genuinely source-entangled: simultaneous near-coloop/near-planar states must fail the partner's literal original-coordinate source separation and evade the diffuse nonzero-leakage gate.

Full unrestricted QFORM remains OPEN.
