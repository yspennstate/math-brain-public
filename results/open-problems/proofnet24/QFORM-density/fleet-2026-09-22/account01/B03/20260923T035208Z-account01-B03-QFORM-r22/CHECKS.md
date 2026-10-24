# r22 finite checks

These checks only verify algebra/constants and the explicit target-family spectrum; they are not proof certificates.

1. `C_star = 4*2^(1/4) = 4.756828460010884...`.
2. `C_time = 2*Gamma(1/4)*cos(pi/8)*C_star = 31.867200062359164...`.
3. `3*2^(4/3)*C_star^(2/3) = 3*2^(17/6) = 21.38156923536814...`.
4. In the heavy-row half-power branch, `4*sqrt(2*(4*2^(1/4))) = 2^(29/8) = 12.337686603263526...`.
5. Since `h>1/2`, the heavy-row scalar factor is bounded by `2^(29/8)*(1/2)^(-1/8)=2^(15/4)=13.454342644059432...`.
6. For `S_(m,a)=[[a,v^T],[v,0_m]]` with `||v||_2=1`, the only nonzero eigenvalues are the roots of `lambda^2-a lambda-1=0`, namely `(a +/- sqrt(a^2+4))/2`; their product is `-1`, so at least one has modulus at least one. Direct summing with `[[0,1],[1,0]]` supplies two more eigenvalues `+1,-1`, hence at least three target-size eigenvalues for every real `a`.
7. For the same star cross block with hub row `v^T`, `Z_1=||v||_2^2=1` and the sole row marginal is `h=1`.
