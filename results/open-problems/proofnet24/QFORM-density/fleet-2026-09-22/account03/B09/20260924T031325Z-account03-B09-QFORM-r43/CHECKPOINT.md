SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T03:13:25Z.
attacking: the heavy physical off-diagonal pair endpoint by combining exact pair Schur algebra with aggregate original-coordinate linear anti-concentration on the Schur-null face, before any worst physical leaf is selected.

# Early substantive checkpoint

Let L={1,2,3}, J disjoint original coordinates, P=A[L,L], C=A[L,J] with rank C=2. Let n span ker(C^T), a=Pn, and Delta=sigma_1(C)sigma_2(C). Choose an invertible indefinite physical pair H=L\{k}, B=P[H,H], p=P[H,k], d=P_kk, C_H=C[H,:], c=C[k,:]. After exact completion of the physical pair B, the Schur remainder on {k} union J has

s=d-p^T B^{-1}p,

m=c-p^T B^{-1}C_H.

Two exact identities are

s=det(P)/det(B),

n_k m^T = - C_H^T B^{-1} a_H,

where a_H=(Pn)_H. The second follows by inserting c=m+p^TB^{-1}C_H into C^T n=0 and using Bn_H+p n_k=a_H.

When det(P)=0, s=0. If n_k!=0 then C_H has rank two and

det(C_H C_H^T)=Delta^2 n_k^2,

so sigma_min(C_H)>=sigma_2(C)|n_k| and therefore

||m|| >= sigma_2(C)||B^{-1}a_H|| >= sigma_2(C)||a_H||/||B||op.

On the exact Schur-null face s=0, the residual is linear in the genuine original coordinate X_k:

R=2 X_k (m^T X_J)+beta X_k+G(X_J).

The original-product projection theorem gives the slope T=2m^T X_J+beta density cap M<=1/(sqrt(2)||m||). Conditioning on X_J,

P(|R-t|<rho | X_J)<=min(1,2rho/|T|).

Splitting at eta and optimizing gives

sup_t P(|R-t|<rho)<=2^(7/4)||m||^(-1/2) sqrt(rho).

Inserting this H0 into the completed indefinite-pair log/small-ball theorem yields

||p_Q||infinity <= 2^(27/8) ( |det B| sigma_min(B) ||m|| )^(-1/4).

Thus the det(P)=0 / rank-two-cross / invertible-indefinite-pair / n_k!=0 subbranch is paid at O(interval length) without selecting a leaf coordinate. The remaining work is to write the complete scope, quantify the target-valid regression, and separate the near-Schur-null collar det(P)!=0 small from this exact face.
