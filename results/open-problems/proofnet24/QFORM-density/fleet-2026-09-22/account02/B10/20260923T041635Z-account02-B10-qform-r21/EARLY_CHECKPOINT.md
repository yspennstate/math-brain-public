SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T04:16:35.232584Z.
attacking: the exact-rank-three near-coloop survivor; test whether the rank-three cross-volume/Fourier exit can remain uniform as hub leverage tends to one, while preserving the product-coordinate bank structure.

# Early substantive checkpoint

Fresh designated-partner input actually used: account03/B10 r25, canonical `yspennstate/math-open-problems@291d344e0c5af27b8b5074dbba22fee22abddbf8`, reduces the unpaid exact-rank-three collar to (among other cases) a near-coloop state `c>7/8`, nonzero small hub diagonal, normalized hub Rayleigh `<1/16`, fixed aggregate star norm, and all residual transverse row leverage `<1/4`.

New exact calculation. Write an exact-rank-three form as `A=R Lambda R^T`, `R^T R=I_3`, `D=|det Lambda|`. For disjoint physical row sets `I,J`, put `G_I=R_I^T R_I`, `G_J=R_J^T R_J`, `M=A_IJ=R_I Lambda R_J^T`. Cauchy--Binet gives

`e_3(M^T M)=D^2 det(G_I) det(G_J)`.

If a hub row is `r_0=sqrt(c)e` with `c>3/4`, every rank-three volume-sampling/Fourier certificate D' whose constrained side has row marginal `<3/4` must put the hub outside that constrained side: if `0 in I` and `G_I` is invertible, its exact rank-three volume marginal is `r_0^T G_I^{-1} r_0 >= ||r_0||^2=c>3/4`, since `G_I<=I`. If `0 notin I` and total spectral leakage away from the hub is `rho=1-c`, then `e^T G_I e<=rho`; because `0<=G_I<=I`, `det(G_I)<=lambda_min(G_I)<=e^T G_I e<=rho`. Also `det(G_J)<=1`. Hence every D'-admissible rank-three cross block satisfies

`e_3(A_IJ^T A_IJ) <= D^2 rho`.

Thus the completed rank-three volume theorem necessarily loses at least `rho^(-1/6)` in this near-coloop limit. The unrestricted fifth-volume exit is identically unavailable for exact rank three because every cross block has rank at most three.

Next: build an exact target-valid near-coloop family with `rho ->0` that satisfies the partner collar, has this degeneration for every admissible cut, but remains uniformly density-bounded by a legitimate disjoint-bank compression. This will distinguish a proof-interface obstruction from a QFORM counterexample and identify the needed endpoint-stable hub interpolation.
