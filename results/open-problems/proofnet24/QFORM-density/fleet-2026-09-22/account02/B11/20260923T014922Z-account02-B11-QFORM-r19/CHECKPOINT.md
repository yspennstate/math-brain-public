# B11 early checkpoint — near-coloop conditioning loses the third-direction smoothing

Status: substantive partial calculation; full QFORM open.

For `m>=1` and `0<eps<=1/2`, let `S` be the `(2+2m) x 3` isometry whose first column has entries `sqrt(1-eps),sqrt(eps)` on coordinates `0,1`, whose second column is `m^{-1/2}` on bank `B`, and whose third column is `m^{-1/2}` on disjoint bank `C`.  Put

`A0=[[0,-1,-1],[-1,0,-1],[-1,-1,0]]`,  `A=S A0 S^T`.

Then `A` has nonzero spectrum `{1,1,-2}`, every physical diagonal is zero, coordinate `0` has leverage `1-eps`, and every physical off-diagonal entry has magnitude at most `m^{-1/2}`.  For independent inputs write

`Y=m^{-1/2} sum_{j in B} X_j`, `W=m^{-1/2} sum_{k in C} X_k`, `Z=sqrt(1-eps)X_0+sqrt(eps)X_1`.

The form is exactly

`Q=-2[Z(Y+W)+YW]`.

With `U=Y+W`, `V=Y-W`,

`Q=-2 ZU -(1/2)U^2 +(1/2)V^2`.

For iid `Uniform[-1/2,1/2]` inputs, Ball's one-dimensional product projection bound gives `||p_Y||inf,||p_W||inf<=sqrt(2)`, hence `||(V,U)||` has joint density cap at most `1`.  Also `||p_Z||inf<=1/sqrt(1-eps)<=sqrt(2)`.  Therefore the completed canonical saddle-plus-square bound recorded and applied by account03/B11 r21 yields

`||p_Q||inf <= 3*2^(4/3) < 7.560`, uniformly in `m,eps`.

In contrast, after conditioning the near-coloop coordinate at `X_0=0`,

`R_eps=-2[sqrt(eps) X_1(Y+W)+YW]`.

For fixed `m`, the bank-sum density satisfies

`p_Y(y),p_W(y) >= c_m := sqrt(m)(4m)^(-(m-1))`

whenever `|y|<=delta_m:=1/(8sqrt(m))`.  If `eps<=1/(1024m)`, conditioning further on `(Y,W)=(y,w)` and integrating on

`0<y<=sqrt(eps)/4`, `2sqrt(eps)<=w<=delta_m/2`

gives the exact lower bound

`p_{R_eps}(0) >= (c_m^2/9) log(1/(32 sqrt(m eps)))`,

which diverges as `eps->0` for each fixed `m`.  At `eps=0`, `R_0=-2YW` has the genuine rank-two logarithmic singularity.

Thus a uniform proof cannot eliminate a near-coloop null coordinate by the sup-conditional inequality `||p_Q||inf <= sup_x ||p_{Q|X_0=x}||inf`: this family has a uniformly bounded full law but a logarithmically diverging conditional slice.  The hub average and the transverse square have to be retained jointly.
