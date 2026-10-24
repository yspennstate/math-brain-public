# account02/B02 partner addendum — E2 determinant + independent shifted square

Fresh named partner account03/B02 completed `20260922T140148Z-account03-B02-QFORM-r11`, canonical math-open-problems commit `f70e9260accfb191c44e874bfc20085580b69b23`. Its integrated-square theorem was applied after the main B02 report was archived.

Combining the partner inequality

`||phi_[d(X+H)^2+R]||_1 <= 2*3^(1/6)*pi^(1/3)|d|^(-1/3)||phi_R||_(3/2)`

(valid when X is independent of (H,R) and H is independent of R) with the reviewed q=1 regularized determinant estimate yields:

if R has an original-coordinate cross block B with leverage `max diag(P_range(B))<=1/2` and

`E_2(B)=sum_{|S|=|T|=2} det(B[S,T])^2>0`,

then

`||p_Q||_infinity <= [3^(1/6)e^(2/3)/2] BETA(1/4,1/8)^(2/3) |d|^(-1/3)E_2(B)^(-1/6)`

with numerical prefactor about `5.9667325591`. The output density is continuous and vanishes at infinity.

Canonical derivation: `yspennstate/math-open-problems@7e3464d0cabd85ed0ac5f61dcbf4f1c8043f34b3:proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T140817Z-account02-B02-qform-r11/PARTNER_ADDENDUM.md`, blob `bd99d94c8bb2778982415b3d82e93f3555e4d3dd`.

This pays the borderline two-cross-direction Fourier exponent whenever the third square channel is genuinely product-independent. The general overlapped shift/residual case remains open, as does the full target.
