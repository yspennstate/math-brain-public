# account02/B17 r11 — s8 proof, part I

Claim (normalized): if coordinate density caps are one and s_8(A)>=1, then the output density is <2371. General scaling is K^2/s. The only analytic dependency is the audited nine/400 paper at eeb752c8943536541b34b42b8bf48e924f4d3d2f.

Set eta=1/100 and kappa=1/6400. A physical pivot means |A_ii|>=eta or a principal 2x2 determinant has modulus >=eta.

Pivot branches are already below 2371 using the source: scalar pivot <990 (five-direction full half-potential <99), definite pair <10pi<32, indefinite pair <193.

Assume no pivot. Then
|A_ii|<1/100 and |A_ij|^2<101/10000.                                    (1)

Let V_r be the ordered disjoint r-minor volume.

First V_1>=kappa. Otherwise
||A||<1/100+1/80<1,
contradicting s_8(A)>=1.

Next V_2>=kappa V_1. If V_2<kappa V_1, the source order-one sampled completion gives
A=D+R+E,
||E||_F<1/40,
rank R<=3,
rank R[L,L]<=1.
Thus s_5(D)>=39/40. Choose two complement indices with |D_i|>=39/40. On them
|R_ii|>39/40-1/100=0.965,
while (1) gives
|R_ij|<sqrt(101/10000)+1/40<0.126.
The 2x2 restricted block is strictly diagonally dominant, contradicting rank R[L,L]<=1. Hence
V_2>=kappa^2.                                                         (2)

If V_3>=kappa^3, a fair literal coordinate cut gives Z_3>=kappa^3/64. The source order-three receiver gives
||p_Q||_infinity <=160 C_3
=2370.934026...<2371,
C_3=3 sqrt(2)e(9/2)^(1/6).                                         (3)

Assume for contradiction V_3<kappa^3. Then V_3/V_2<kappa. Sample nonsingular ordered disjoint two-seeds B=A[S,T] with weights det(B)^2/V_2. The source interpolation estimate gives
E ||E_B||_F^2 <9kappa.
Seeds with ||E_B||_F^2<=18kappa carry at least V_2/2.

For such a seed set eps=3sqrt(2)/80. Its completion has global rank <=6 and restricted complement rank <=2, so s_2(D)>=1-eps. Choose two complement coordinates H with |D_h|>=1-eps.

Writing P=A[:,T]B^{-1}A[S,:],
|P_hh|>=1-eps-eta,
|P_hh'|<=sqrt(eta+eta^2)+eps.
Therefore
|det P[H,H]|>=delta,
delta=(1-eps-eta)^2-(sqrt(eta+eta^2)+eps)^2
=0.8543351401...>4/5.                                                (4)

Since P[H,H]=A[H,T]B^{-1}A[S,H],
|det A[S,H] det A[H,T]|>=delta |det B|.                              (5)

For each literal pair H define
D_H=sum_{U subset H^c, |U|=2} det A[H,U]^2
=det(C_H C_H^T).
Cauchy-Binet gives sum_H D_H=V_2. Assign one certified H to each good seed and let w_H be its assigned determinant-squared mass. Since sum w_H>=V_2/2, some H has w_H>=D_H/2. Squaring (5) and summing assigned seeds gives delta^2 w_H<=D_H^2. Consequently for this literal physical pair
g:=det(CC^T)=D_H>=delta^2/2>8/25,
C=A[H,H^c].                                                          (6)

Part II proves that (6), the no-pivot entry cap and s_8(A)>=1 force a disjoint third volume >1/150, contradicting V_3<kappa^3.
