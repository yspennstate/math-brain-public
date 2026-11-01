# fleet01/B06 r17 improvement: four-eigenvalue structural hub dichotomy

Let A=A^T with s4(A)>=1. Let Phi be four orthonormal eigenvectors for four eigenvalues of modulus at least one, Lambda their diagonal eigenvalue matrix, and A=Phi Lambda Phi^T+E with ||E||=s5(A). For row phi_i put ell_i=|phi_i|^2.

Fix delta in (0,1/4), H_delta={i:ell_i>delta}, K=sum_{i in H_delta} phi_i phi_i^T, and eigenvalues kappa1>=kappa2>=kappa3>=kappa4 of K. Put all heavy coordinates in I and randomly split the light coordinates. For some split,
K_I=Phi_I^T Phi_I=(I+K)/2+Z,
K_J=Phi_J^T Phi_J=(I-K)/2-Z,
with ||Z||<=||Z||_F<=sqrt(delta), because
E||Z||_F^2=(1/4)sum_light ell_i^2<=delta.
Hence
lambda_min(K_I)>=1/2-sqrt(delta),
lambda_3(K_J)>=(1-kappa2)/2-sqrt(delta).
Polar factorization and s4(Lambda)>=1 give
s3((Phi Lambda Phi^T)_{I,J})>=sqrt((1/2-sqrt(delta))*(((1-kappa2)/2-sqrt(delta))_+)).
Therefore
s3(A_{I,J})>=sqrt((1/2-sqrt(delta))*(((1-kappa2)/2-sqrt(delta))_+))-||E||.

Consequently, if ||E||<=tau and every cut has s3<c, then
kappa2 > 1-2 sqrt(delta)-2(c+tau)^2/(1/2-sqrt(delta))
whenever the right side is positive.

Take delta=1/9 and c=tau=1/1000. Then kappa2>62491/187500. Since sum ell_i=4 and every heavy row has ell_i>1/9, there are at most 35 heavy rows. Cauchy-Binet gives
sum_{h<k in H_delta}|phi_h wedge phi_k|^2=e2(K)>=kappa1*kappa2>=kappa2^2.
Thus some physical pair H={h,k} obeys
|phi_h wedge phi_k|^2 > (62491/187500)^2/595 >1.86e-4.

Now use pivot thresholds eta=1e-4 and zeta=1e-8. In the no-pivot case every diagonal is <eta and every off-diagonal is <sqrt(eta^2+zeta)=sqrt(2)/10000, so B=A_HH has ||B||<(1+sqrt2)/10000. With R=H^c, C=A_HR and G=CC^T,
G=(A^2)_HH-B^2.
Since A^2 >= Phi Phi^T in Loewner order, (A^2)_HH>=S_H:=Phi_H Phi_H^T. Also tr S_H<=2 and det S_H=|phi_h wedge phi_k|^2, hence lambda_min(S_H)> (62491/187500)^2/1190. Weyl gives
lambda_min(G)> (62491/187500)^2/1190-(1+sqrt2)^2/1e8 >9e-5.
Therefore det G>8.1e-9.

Thus for s4(A)>=1 at least one holds:
(1) a diagonal pivot |a_ii|>=1e-4;
(2) a principal pair determinant has modulus >=1e-8;
(3) s5(A)>=1e-3;
(4) some coordinate cut has s3(A_IJ)>=1e-3;
(5) two literal hubs H satisfy ||A_HH||<(1+sqrt2)/10000 and lambda_min(A_HR A_HR^T)>9e-5.
Branches 1-4 are already paid by existing theorems. If A_HH=0 in branch 5, the existing two-hub lemma gives ||p_Q||_infty<436. The only remaining s4 endpoint under this dichotomy is the same quantitative two-hub configuration with a small nonzero hub block.

Secondary exact improvement: for an orthonormal k-frame Phi, Lemma 6.3 sharpens to
E||Q_epsilon||_F^2 <= a^2(k^2+k-2 sum_i ell_i^2) <= a^2(k^2+k),
using sum_{i neq j}ell_i ell_j=k^2-sum ell_i^2 and sum_{i neq j}(phi_i dot phi_j)^2=k-sum ell_i^2.

This does not claim the universal s4 theorem; the small-nonzero-hub analytic receiver remains open.
