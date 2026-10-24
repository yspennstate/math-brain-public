SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T02:54:29Z.
attacking: optimize the new volume-marginal Fourier certificate, independently check its matrix/tail gate, and enlarge the genuinely rotated indefinite class it covers.

# Early substantive checkpoint

Fresh controls keep QFORM as the sole target. This run first independently checked the new volume-stability package at `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, especially `REPORT.md` and `PEER_TAIL_EXTENSION.md`.

The checked Fourier theorem is: if `Z=e3(M^T M)>0`, `1<=q<3/2`, and every third-volume row inclusion marginal obeys `alpha_i<=q/2`, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,

with a continuous `C_0` density and arbitrary self-block terms/outside couplings retained. I independently re-derived the Hausdorff--Young exponents, the row/column Brascamp--Lieb entropy factors, the Jensen exponent, and the Fourier inversion coefficient. I also checked the matrix identity `W<=I`, `W<=(E2/E3)MM^T`, the implication `3E3>=kappa^2 E2`, and the projection estimate

`sqrt(alpha_i)<=sqrt(P_ii)+(sqrt(3) epsilon/kappa)sqrt(1-P_ii)`.

The q-dependent coefficient is strictly increasing on `[1,3/2)` because

`d/dq log[3e/((3-2q)sqrt(q))] = 2/(3-2q)-1/(2q) = (6q-3)/(2q(3-2q))>0`.

Therefore an actual marginal cap `alpha_*` should use the smallest admissible exponent

`q_* = max(1,2 alpha_*)`,

not the convenient fixed choice `q=4/3`. This yields an immediate quantitative improvement and a wider admissibility gate.

Using the completed account01/B20 tail identity `T2 E2<=3E3`, the checked tail certificate is

`sqrt(alpha_i)<=sqrt(P_ii)+sqrt(3) epsilon/sqrt(T2) sqrt(1-P_ii)`.

For `max_i P_ii<=1/2`, put `rho=epsilon/sqrt(T2)` and `delta=sqrt(3)rho`. Then

`alpha_* <= (1+delta)^2/2`,
so the optimized exponent is `q_*=(1+delta)^2` whenever `delta>0`. A finite Fourier bound requires only

`delta < sqrt(3/2)-1`, equivalently
`rho < (sqrt(3/2)-1)/sqrt(3) = 0.1297565119969...`,

whereas the source package used the stronger sufficient condition `rho<=1/15=0.0666...` to fit `q=4/3`. Thus the variable-q mechanism almost doubles the permitted relative tail error.

A clean new corollary already follows at `rho<=1/10`: then `q_*=(1+sqrt(3)/10)^2=1.3764101615...<3/2` and

`||p_Q||_infinity <= 28.1208886793 [s1(M)^2 s2(M)^2 T2]^(-1/6)`.

This is a supporting theorem, not the full conjecture. The remaining work in this run is to write the proof carefully, give a target-valid diffuse indefinite family that passes the new `1/10` gate but fails the old `1/15` gate, refresh corrections, and publish the final immutable report/handoff/memory/receipt.
