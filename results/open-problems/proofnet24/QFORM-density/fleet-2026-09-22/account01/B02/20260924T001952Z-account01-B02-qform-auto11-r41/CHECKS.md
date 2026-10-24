# r41 checks

Analytic checks for `QFORM-CHIRP-MAXIMAL-WEAKL2-COUNTEREXAMPLE-v1`.

1. Periodic averaging. For `F(u)=1_{dist(u,2pi Z)<=pi/12}`, the period mean is `1/12`. With `K=49`, the main term in `int_1^K F(Rz^2)dz` is `(1/12)(48)=4`. Writing `F=1/12+G` with bounded primitive of `G` gives error `O(R^-1)` after `u=Rz^2`, so the good-set measure is at least `2` for all sufficiently large `R`.

2. Time-window phase error. `a=(pi/12)/(2*49^2)=5.4518822948594214e-5`. For `|t-T_j|<=a lambda^-2` and `y<=49 lambda`, the extra phase is at most `a*49^2=pi/24`; together with the defining `pi/12` phase error this is `pi/8`.

3. Own-packet amplitude. `c0=cos(pi/8)=0.9238795325112867`, hence the resonant packet contributes at least `c0 lambda` in real part.

4. Off-packet suppression. The family `1_{S_k}(y)e^{-ity^2}` is compact in `L1` for `t` in the finite union of compact target intervals. Uniform Riemann--Lebesgue therefore permits a single sufficiently large translation spacing `D` making every wrong packet at most `c0 lambda/(2N)` for the selector modulation.

5. Weak-L2 divergence. At level `mu=c0 lambda/4`, the superlevel set contains `N` intervals of total measure `2aN lambda^-2`, so

`mu^2 meas{U_N>mu} >= (c0^2 a/8)N = 5.816840772365872e-6 N`.

6. Partner arithmetic. At `E3(M)>=2^-18`, account02/B02 gives

`||p_Q||inf <=10.345084*(2^-18)^(-1/6)=82.760672`,

`int |phi_Q| <=2pi*82.760672=520.0006383227089`.

These checks verify algebra/constants only; the proof is in `REPORT.md` plus `CORRECTION.md`.
