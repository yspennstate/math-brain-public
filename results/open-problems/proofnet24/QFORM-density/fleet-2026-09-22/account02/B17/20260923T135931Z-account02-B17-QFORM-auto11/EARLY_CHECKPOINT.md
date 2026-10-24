# Early checkpoint — unequal opposite rank-one cube banks

Run `20260923T135931Z-account02-B17-QFORM-auto11`.

For unit vectors `a,b` on disjoint centered-unit-interval banks, let `S=sum a_i U_i`, `T=sum b_j V_j`, with even unimodal densities `h,g`, and let `X` be independent with arbitrary probability density `f<=1`. For

`Q = X^2 + S^2 - T^2`

the physical matrix `diag(1,aa^T,-bb^T)` has exact nonzero spectrum `{1,1,-1}`.

Define

`F(h,g)=int_0^infty g(t) int_0^{2pi} h(t sin(theta)) dtheta dt`.

The square-density formula gives for `s>=0`, after discarding `f<=1`, polar coordinates, and `t=sqrt(r^2-s)`,

`p_Q(s) <= int_0^infty g(t) int_0^{2pi} h(sqrt(t^2+s) sin(theta)) dtheta dt <= F(h,g)`.

For `s=-a<=0`, the same formula and monotonicity of `r -> g(r)/r` give directly `p_Q(-a)<=F(h,g)`. Thus the unequal-bank problem reduces globally to one cone integral without needing identical residual laws.

Ball/Rogozin cube projection bounds give `||h||inf,||g||inf<=sqrt(2)`. Applying the same projection theorem to `(S-S')/sqrt(2)` and `(T-T')/sqrt(2)` gives `||h||_2^2,||g||_2^2<=1`. Hence, with `I(u)=int_0^infty g(t)h(ut)dt`,

`I(u)<=min(sqrt(2)/2, 1/(2sqrt(u)))`,

so

`F(h,g) <= (pi/2)(sqrt(2)+2^(1/4)) = 4.0894436371... < 3sqrt(2)`.

This strictly extends the predecessor identical-bank theorem to arbitrary unequal coefficient profiles. Full derivation and source application follow in `REPORT.md`.
