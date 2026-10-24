# Deterministic checks — account02/B20 `20260924T000452Z-account02-B20-QFORM-auto11`

All checks are coefficient-level; no stochastic simulation is used.

1. Anchor coloring scale:

`(1/144)/16 = 1/2304`.

2. Minkowski split scale:

`(1/2304)/4 = 1/9216`.

3. Pinned D5 threshold:

`5 sqrt(2e) (1/1024)^(-1/10) = 10 sqrt(2e) = 23.3164398159712...`.

4. Medium-small nonzero anchor payment:

`8 e^(1/4) (1/4096)^(-1/4) (1/2304)^(-1/8)`

`=64 e^(1/4) 48^(1/4)`

`=216.303677807774...`.

5. Favorable shared-hub E2 branch:

`C_h=3*2^(7/6)e^(1/3)=9.39913188784886...`.

With `R_*>=1/36864`,

`C_h 36864^(1/6)=54.2235757060507...`.

At zero pivot, `R_*>=1/9216`, giving

`C_h 9216^(1/6)=43.0372805586311...`.

6. Exact-rank-one shared-hub branch:

`3*2^(2/3) 2304^(1/6)=17.3069948436889...`.

7. Tiny-pivot raw-E2 threshold:

If `0<|a|<1/4096` and `a^2 E2(N)>=1/9216`, then

`E2(N) > 4096^2/9216 = 16384/9 = 1820.444444...`.

8. E2/E3 rank-two tube:

For singular-square values `x_i`, pair-volume sampling gives exactly

`E_[{i,j}~x_i x_j/e2] sum_(k notin {i,j})x_k = 3e3/e2`.

At `E2(N)>16384/9` and `E3(N)<1/1024`,

`sum_(k>=3)s_k^2 < 3(1/1024)/(16384/9)=27/2^24`.

Therefore

`||N-N_2||_F < sqrt(27)/4096 = 3sqrt(3)/4096 = 0.00126859190007486...`.

9. Marginal-free E3 threshold from the newest designated-partner source:

`C_E3=3*2^(4/3)e^(1/3)` and

`C_E3 * 1024^(1/6)=24e^(1/3)=33.4946982021...<33.495`.

10. The scalar-Schur identity used in the pivot branch is exact:

for every residual physical `2x2` row/column choice `P,Q`,

`det [[a,r_Q^T],[c_P,N[P,Q]]] = a det (N-c r^T/a)[P,Q]`.

Squaring and summing yields `D=a^2 E2(S)` with no omitted cross terms.
