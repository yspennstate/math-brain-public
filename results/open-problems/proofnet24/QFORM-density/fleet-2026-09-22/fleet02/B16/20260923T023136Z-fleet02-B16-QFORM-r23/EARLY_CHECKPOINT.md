# fleet02/B16 r23 — early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## First unpaid implication attacked

Fleet03/B16 r21 leaves the approximate-coloop/isotropic-leakage regime: a leverage-heavy physical row with nonzero leakage must be aggregated with the genuine product-projection bank before any reciprocal small pivot is paid. I isolate a source-valid subcase where the coloop direction is distributed over an ORIGINAL-coordinate bank disjoint from the transverse spectral plane.

Let an exact-rank-three form be written in a spectral basis as

`A=R B R^T`, `R^T R=I_3`, `s_min(B)>=1`.

Assume an original-coordinate partition `I union J=[n]` and a spectral unit vector `e` such that every row `r_i`, `i in I`, is collinear with `e`, while every `r_j`, `j in J`, lies in `e^perp`. Parseval then gives a normalized scalar bank variable

`S=sum_(i in I) a_i X_i`, `sum a_i^2=1`,

and an orthonormal two-dimensional product projection `Y` from the disjoint bank `J`. Hence `S` is genuinely independent of the whole pair `Y`; the two coordinates of `Y` need not be independent.

The source projection bounds give

`||p_S||_infinity <= sqrt(2)`, `||p_Y||_infinity <=2`.

Apply fleet03/B16 r21 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v2` after rescaling a scalar density cap `L`: its near-null estimate becomes

`||p_Q||_infinity <= 3*2^(8/3) L^(2/3) M^(2/3) (D P)^(-1/6)`,

where `D=|det B|` and `P=beta^2|e_22|` after rotating only inside the receiver plane. The partner cross-resource lemma gives `P >= (1-|a|)D` whenever `|a|<1`, with `a=B_00`. With `L=sqrt(2)`, `M=2`, and `D>=1`,

`near <= 3*2^(11/3) (1-|a|)^(-1/6)`.

For `|a|>0`, scalar completion plus the completed rank-two product-projection half-Riesz theorem gives

`far <= sqrt(2) * 16*2^(3/4) |a|^(-1/4) D^(-1/4)`.

At the rational split `|a|=4/7`, these are respectively `43.8761...` and `43.7691...`, so both are `<44`. Thus the planned theorem is a uniform `<44` bound for this distributed line-plane bank class, independent of how mass is split inside the scalar bank; in particular it covers leverage `c in (1/2,1)` when the leakage of the heavy direction stays in the same line bank and is source-disjoint from the transverse plane.

The newest Claude source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` is used at a real inequality: its two-dimensional product-marginal theorem gives `||p_Y||_infinity<=2`, and its ruled Theorem C separately sharpens the majority-sign side to `pi sqrt(2)`. No projected independence is inferred.

Remaining gap after this subcase: genuinely OVERLAPPING leakage, where the same original leaf coordinates carry both the heavy spectral direction and the transverse plane. There the scalar-bank / pair independence above is absent; small matrix leakage cannot simply be discarded for unbounded inputs.
