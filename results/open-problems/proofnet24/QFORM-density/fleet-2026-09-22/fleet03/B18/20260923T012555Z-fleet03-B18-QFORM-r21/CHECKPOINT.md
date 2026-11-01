# fleet03/B18 r21 — early mathematical checkpoint

Status: substantive partial derivation; full QFORM remains open.

I apply the exact Schur-isotropic coefficient geometry proved by fleet04/B18 r3:

- `Q=(Y+u X_0)^T D (Y+u X_0)`, with `X_0` an ORIGINAL coordinate independent of the residual product block;
- `Y=V^T X'`, `V^T V=I_3`, `D=D^T` invertible, and `u^T D u=0`;
- `L=[u,V^T]`, so `LL^T=I+uu^T` and `|pdet(L^T D L)|=|det D|(1+||u||^2)`.

Write `r=||u||>0`, `n=u/r`, residual rows `v_j^T`,
`p_j=||v_j||^2`, and `q_j=||(I-nn^T)v_j||^2`.
The partner constructs two exact basis-volume probability laws:

`mu_S=det(V_S)^2` on residual triples, with marginal `p_j`;
`nu_jk=det[n,v_j,v_k]^2` on residual pairs, with marginal `q_j`.

Instead of the partner's fixed 1/2--1/2 mixture, let `x in [0,1/2]` be the probability of the shear-pair bank and put

`w_S=(1-x)mu_S`, `w_{0jk}=x nu_jk`.

Then the capped-basis marginals are

`alpha_0=x`,
`alpha_j=(1-x)p_j+x q_j`.

The determinant-entropy score in fleet01/B18's proved capped-basis Fresnel theorem is EXACTLY

`Z(x)=(1-x)^(-(1-x)) (r^2/x)^x`,

with the continuous endpoint interpretation at `x=0`.
Indeed every residual basis has `det(L_S)^2/mu_S=1`, and every shear basis has `det[u,v_j,v_k]^2/nu_jk=r^2`, so

`log Z=(1-x)log(1/(1-x))+x log(r^2/x)`.

Differentiation gives

`d/dx log Z = log(r^2(1-x)/x)`,

hence the unconstrained optimum is

`x_*=r^2/(1+r^2)`, `Z(x_*)=1+r^2`.

For `0<r<=1`, `x_*<=1/2`. Moreover `q_j<=p_j`; therefore if the residual Parseval frame is diffuse in the sharp sense `p_j<=1/2` for all j, then

`alpha_j=(p_j+r^2 q_j)/(1+r^2)<=p_j<=1/2`.

Thus the primary-source-backed capped-basis theorem applies and gives

`||p_Q||_infinity <=3e [|det D|(1+r^2)]^(-1/3)`.

For an exact-rank-three target matrix with all three nonzero eigenvalue magnitudes at least one,
`|det D|(1+r^2)=|pdet A|>=1`, so

`||p_Q||_infinity <=3e`.

This removes the small-shear blow-up of fleet04/B18's fixed 1/2 mixture on the whole diffuse-residual subbranch `0<r<=1`. Continuity follows from the same integrable characteristic-function estimate in the capped-basis theorem.

Primary-source mechanism being checked in this run: Beckner's sharp Hausdorff--Young theorem and Lieb's Gaussian-exhaustion theorem for Brascamp--Lieb, in the Bennett--Carbery--Christ--Tao formulation. No arbitrary-joint coarea, post-rotation independence, conditional-height moment, or small-matrix-error-as-small-random-error step is used.
