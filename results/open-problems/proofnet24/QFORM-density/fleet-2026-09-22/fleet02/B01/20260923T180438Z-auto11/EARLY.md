SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-23T18:04:38Z.
attacking: remove the remaining projected one-volume heavy-row gate by promoting a heavy row to a literal second hub and spending the resulting rank-two |t|^-1 envelope through the half-Riesz square peel.

# Early substantive checkpoint

Let an original-coordinate scalar completion give

Q = a(X_0+h)^2 + R,

with a != 0 and

R = F(Y) + 2Y(<m_I,X_I>+<m_J,X_J>+beta) + X_{I union J}^T A_R X_{I union J} + affine,

where Y,X_I,X_J are disjoint original coordinates. Put m=m_J !=0 and

C=A_R[I,J](I-P_m),  F_C=||C||_F.

I claim the row-marginal gate can be removed completely whenever F_C>0:

H_{1/2}(R) <= 8 (||m|| F_C)^(-1/4),
||p_Q||_infinity <= 8 |a|^(-1/2) (||m|| F_C)^(-1/4).

Proof split. Write rows c_i of C and alpha_i=||c_i||^2/F_C^2.

1. If every alpha_i<=1/2, apply the reviewed grouped projected-crossing estimate at k=1, ell=1. It gives

|phi_R(t)| <= min(1, 2*pi*(||m|| F_C)^(-1/2)*|t|^(-1)).

The required 20260922T211500Z Fourier report proves c_{1/2}=(2*pi)^(-1/2) and
H_{1/2}(R)<=c_{1/2} integral |t|^(-1/2)|phi_R(t)|dt. Since
integral_R |t|^(-1/2) min(1,K/|t|)dt=8 sqrt(K), this gives exactly
H_{1/2}(R)<=8(||m||F_C)^(-1/4).

2. If some alpha_i>1/2, condition all I\{i}. Decompose the physical row a_i=A_R[i,J]=lambda_i m+c_i, c_i perpendicular m. The two literal original hubs (Y,X_i) have cross matrix [m;a_i] into J, whose singular-value product is

S_i=sqrt(det([m;a_i][m;a_i]^T))=||m|| ||c_i||.

The reviewed exact-rank-two crossing theorem with arbitrary internal functions gives, because the hub-side projection density is <=1 and the two-dimensional J projection density is <=2,

|phi_R(t)| <= min(1, pi*sqrt(2)*S_i^(-1/2)*|t|^(-1)).

The same half-potential calculation gives

H_{1/2}(R)<=2^(11/4) S_i^(-1/4).

Since alpha_i>1/2, ||c_i||>F_C/sqrt(2), hence

H_{1/2}(R)<2^(23/8)(||m||F_C)^(-1/4)<8(||m||F_C)^(-1/4).

Finally the required square peel gives ||p_Q||_infinity<=|a|^(-1/2)H_{1/2}(R).

This uses no pointwise scalar quadratic-phase decay and keeps every promoted variable in original coordinates. The remaining projected-crossing obstruction in this scalar-completion branch is therefore C=0, not a heavy row and not rank one.
