# fleet02/B08 r36 deterministic checks

All checks below are exact arithmetic/radical consequences; no simulation is used.

1. `sigma=sqrt(67/800)/2=0.14469796128487783...`, hence `sigma/8=0.01808724516060973...`.
2. For Theorem 2.1, `D^T D >= s_2(D)^2 P_R`; with `|<u,w_r>|>=1/8`, this gives `||Dw_r||>=s_2(D)/8` exactly.
3. For `K=[[0,sqrt(2)],[sqrt(2),1]]`, `det(K-lambda I)=lambda^2-lambda-2=(lambda-2)(lambda+1)`, hence the stress-family hub/carrier eigenvalues are `2L,-L`.
4. On a Walsh half-cut independent of `u_1,u_2,u_3`, the normalized restrictions `sqrt(2)u_j|_J` and `sqrt(2)u_j|_K` are orthonormal. Therefore `C_epsilon[J,K]` has singular values exactly `L/2,L/2,epsilon L/2`.
5. For `m>=16384`, `sqrt(2)/sqrt(m)<=sqrt(2)/128=0.011048543456...<1/64`, and `6/m<=6/16384=0.0003662109375<1/64`; hence every physical `2 x 2` block in the stress family has least singular value below `L/64`.
6. At `epsilon=2^-16`, the fixed-source Theorem-F constant is `12 epsilon^(-1/3)=12*2^(16/3)=483.8096831596312...`.

`QFORM_B08_R36_CHECK_PASS`
