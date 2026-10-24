# Deterministic checks for r43

Run `20260924T015542Z-account01-B18-qform-auto11-r43`.

For

`H=[[0,a,rho],[a,c,0],[rho,0,0]]`,

direct expansion gives

`det H = -c rho^2`.

For the two-row map

`L=[b^T;v^T]`, `||v||=1`, `a=<b,v>`, `rho^2=||b||^2-a^2`,

`det(LL^T)=||b||^2-a^2=rho^2`.

Thus the spectral determinant currency and the LPP pair-density Jacobian use the same transverse quantity `rho`.

Numerical constants:

`3*4^(2/3) = 7.559526299369239...`

and for the literal endpoint pair cap `M=1`,

`3*2^(2/3) = 4.762203155904598...`.

Sanity check at `A_*=[[0,1,0],[1,0,0],[0,0,1]]`: spectrum is `{-1,1,1}`, `c=1`, `rho=1`, so `|c|rho^2=1=|(-1)(1)(1)|` and the endpoint inequality is scale-consistent.
