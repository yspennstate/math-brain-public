# account03/B14 r33 checks

Run `20260923T103613Z-account03-B14-QFORM-r33`.

These are exact algebra checks supporting REPORT.md; they are not Monte Carlo evidence and are not used as a substitute for proof.

## 1. Cofactor gate

For a symmetric rank-two 3x3 matrix `B` with eigenvalues `lambda_+,lambda_-,0` and unit kernel `k`,

`adj(B)=lambda_+ lambda_- k k^T`.

Deleting coordinate `i` gives

`det B[S\{i},S\{i}]=lambda_+ lambda_- k_i^2`.

Thus if `lambda_+lambda_-<0` and `k_i!=0`, the physical 2x2 block is invertible indefinite. Choosing maximal `|k_i|` gives `|k_i|>=1/sqrt(3)`.

## 2. Post-Schur leakage identity

Write

`B=[[C,b],[b^T,d]]`,

and outside coupling column blocks as `[[F],[g^T]]`. Since `det B=0` and `C` is invertible,

`d-b^T C^-1 b=0`.

The kernel relation gives `k_P=-C^-1 b k_i`, hence

`A[S^c,S]k=F^T k_P+g k_i=k_i(g-F^T C^-1 b)`.

So the full Euclidean kernel leakage is exactly `L=|k_i| ||a||_2` for the post-Schur slope coefficient `a=g-F^T C^-1b`.

## 3. Constant calculation

The slope `beta+2a^T V` has cap at most

`H=sqrt(2)/(2||a||_2)=|k_i|/(sqrt(2)L)`.

With `D=nu_1 nu_2 k_i^2` and `kappa>=nu_2 k_i^2`, the random-slope pair bound gives

`8 sqrt(H/kappa)+2D^-1/2`

`<=8/[2^(1/4)sqrt(nu_2 L |k_i|)] +2/[sqrt(nu_1nu_2)|k_i|]`.

Using `|k_i|>=1/sqrt(3)` gives

`8(3/2)^(1/4)/sqrt(nu_2L)+2sqrt(3)/sqrt(nu_1nu_2)`.

At `nu_1=nu_2=L=1`, the relaxed universal-coordinate constant is approximately `12.318`; when `|k_i|=1`, the sharper constant is `8*2^(-1/4)+2`, approximately `8.728`.

## 4. Diffuse star stress family

For `B=diag(1,-1,0)` and `w_m=m^-1/2(1,...,1)`, the active star block

`[[0,w_m^T],[w_m,0]]`

has eigenvalues `+||w_m||_2=+1`, `-||w_m||_2=-1`, and `0` with multiplicity `m-1`. Adding the first two diagonal physical coordinates gives full spectrum

`{1,-1,1,-1,0,...,0}`.

For a single outside coordinate `j`, the physical 4x4 enlargement has singular values `1,1,m^-1/2,m^-1/2`, while `|k^T c_j|=m^-1/2`. Thus the designated partner one-coordinate bound scales as `C4 sqrt(m)`, whereas the aggregate theorem pays `||w_m||_2=1` and is uniform in `m`.

CHECK STATUS: exact identities consistent; full QFORM remains open; no continuity claim follows from these checks.
