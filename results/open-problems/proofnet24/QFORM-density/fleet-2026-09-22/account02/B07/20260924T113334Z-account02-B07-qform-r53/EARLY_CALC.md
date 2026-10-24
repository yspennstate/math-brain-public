# account02/B07 r53 early calculation

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains open.

Incoming captured state from account03/B07 r52 and account02/B07 r52: with `eps=1/64`, `B=A[K,K]`, `D=A[K,K^c]`, `s_3(B),s_3(D)<eps`, and top-two truncations `B_2,D_2`,

`C_0=B_2^2+D_2D_2^T`, `lambda_3(C_0)>=gamma:=511/2048`, `rank(C_0)<=4`.

Let `theta_4` be the fourth eigenvalue of `C_0` (zero in rank three), and let `P` be the top-three spectral projection. Put

`B_3=P B_2 P`, `D_3=P D_2`.

Because `B_2^2<=C_0` and `D_2D_2^T<=C_0`, with `Q=I-P`,

`||Q B_2||_op, ||B_2Q||_op, ||Q D_2||_op <= sqrt(theta_4)`.

Moreover

`P B_2^2 P = B_3^2 + P B_2 Q B_2 P <= B_3^2 + theta_4 P`,

so

`C_3:=B_3^2+D_3D_3^T >= P C_0 P-theta_4 P`,

and therefore

`lambda_3(C_3)>=gamma-theta_4`.

If `theta_4<=1/512` and the top-three frame has all physical row leverages at most `1/12`, a Rademacher partition has both Gram matrices at least `I_3/4`. The same physical-cut argument as r52 then gives for the rank-three projected base crossing

`s_3(M_3)>=(1/4)sqrt(gamma-theta_4)`.

Restoring the actual matrices costs at most

`E(theta_4)=sqrt((eps+2sqrt(theta_4))^2+(eps+sqrt(theta_4))^2)`

in operator norm. At `theta_4=1/512`,

`(1/4)sqrt(gamma-theta_4)-E(theta_4)=0.004400193079861364>0`.

Thus this branch already produces an actual physical `E_3` crossing. If instead a top-three row leverage exceeds `1/12`, then for that physical row `h`,

`(A^2)_{hh}>= (C_0)_{hh}>=gamma/12=0.020792643229...`.

If `theta_4>1/512`, either the full rank-four frame is diffuse and r52 already pays, or some row has full-carrier leverage `>1/16`; then

`(A^2)_{hh}>theta_4/16>1/8192`.

So the projected-rank-three refinement appears to replace the r52 `<=64` heavy-set residual by a single physical energetic row, unless an actual third-volume crossing already pays. The remaining task is to write the projected-cut proof carefully and identify the correct analytic regression for the energetic-row branch without selecting one edge/minor.