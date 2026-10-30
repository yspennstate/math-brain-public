# Early calculation: Poisson satellite barrier

Programme `QFORM-DENSITY-3EIG-20260922`; worker `fleet02/B17`; run `20260924T064827Z-fleet02-B17-QFORM-auto11`.

Full QFORM remains OPEN. This calculation attacks a genuinely non-Lindeberg root-m satellite witness family.

For m>=2 set eps=1/m, ell=1-eps, R=sqrt(m/3), and let the third-bank physical density be the indicator of

`[-ell/2,ell/2] union [R-eps/4,R+eps/4] union [-R-eps/4,-R+eps/4]`.

Its total support length is exactly one, so the density cap is exactly one. Banks 1 and 2 use `Unif[-1/2,1/2]`. Let `Y_j=m^{-1/2} sum_k X_{jk}` and

`Q_m=Y_1^2+Y_2^2-Y_3^2`.

The physical matrix is `diag(J_m/m,J_m/m,-J_m/m)`, hence its exact nonzero spectrum is `{1,1,-1}`.

The third-bank one-coordinate characteristic function at scale `t/sqrt(m)` is

`ell sinc(t ell/(2 sqrt(m))) + eps sinc(t eps/(4 sqrt(m))) cos(t/sqrt(3))`.

Therefore the normalized third bank converges to

`G_3 + S/sqrt(3)`,

where `G_3~N(0,1/12)` and `S` is a symmetric compound-Poisson variable with characteristic function `exp(cos t-1)`. The first two banks converge to iid `N(0,1/12)`. The Lindeberg condition genuinely fails: for any fixed delta<1/sqrt(3), the third-bank Lindeberg sum tends to `1/3` rather than zero.

The completed pinned Fresnel-Brascamp-Lieb Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies to the actual physical frame: every row leverage is `1/m<=1/2`, `G_I=I_3`, and there is no residual quadratic block. Hence

`|Phi_m(t)| <= min(1,(4 pi)^(3/2)|t|^(-3/2))`,

an integrable m-independent envelope. Weak convergence of `Q_m` therefore upgrades by dominated convergence and Fourier inversion to uniform convergence of the whole output density.

Conditioning the limit on `S=k` gives

`G_1^2+G_2^2-(G_3+k/sqrt(3))^2`.

The latest compatible fleet03/B17 theorem `QFORM-MINORITY-AXIS-NONCENTRAL-RIGIDITY-v1` gives the global conditional ceiling `3 sqrt(2)` and, for `k!=0`, the quantitative factor at most

`eta=exp(-(3-2 sqrt(2)))<1`

because its noncentral parameter is `b=|k|>=1`. Writing `w_0=P(S=0)=e^(-1) I_0(1)`, the mixture therefore obeys

`||p_infinity||_infinity <= 3 sqrt(2) [w_0+(1-w_0) eta] < 3 sqrt(2)`.

Numerically the bracket is about `0.91577106145`, giving the ceiling `3.88528756539...`.

This is a real obstruction to a counterexample mechanism: root-m remote fragments can survive in the limit as a non-Gaussian compound-Poisson component and still cannot overshoot the Gaussian sharp obstruction when their jumps lie on the minority-sign axis. The next unpaid Poissonized witness is an off-axis/majority-plane jump mixture on the two-sheet side.
