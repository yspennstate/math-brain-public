# Early checkpoint — rank-three volume concentration to three hubs

Programme: QFORM-DENSITY-3EIG-20260922  
Worker: fleet02/B01  
Run: `20260923T142922Z-fleet02-B01-qform-r44`

Let `M=A[I,J]` be any original-coordinate cross block with

`Z=e_3(M^T M)=sum_{|S|=|T|=3} det(M_ST)^2>0`,

and let `w_ST=det(M_ST)^2/Z` be the completed Claude volume law. Write

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`.

Fix `h=11/16`.

**First calculation.** If three distinct rows `H={i1,i2,i3}` satisfy `alpha_i>=h`, then since `|S|=3`,

`P_w(S=H)=P(i1,i2,i3 all in S)>=alpha_i1+alpha_i2+alpha_i3-2>=1/16`.

By Cauchy--Binet,

`det(M_H M_H^T)=sum_T det(M_HT)^2=Z P_w(S=H)>=Z/16`.

Let `B=A[H,H^c]` be the *full* three-row slope matrix. Since `J subset H^c`,

`B B^T >= M_H M_H^T`

in Loewner order, hence

`Pi_3(B)=sqrt(det(BB^T)) >= Z^(1/2)/4`.

Applying the preceding B01 theorem `QFORM-THREE-HUB-JOINT-PLANCHEREL-v1` gives

`||p_Q||_infinity <= 3 sqrt(2) Pi_3(B)^(-1/3)
                  <= 3 sqrt(2) 4^(1/3) Z^(-1/6)
                  < 6.735 Z^(-1/6)`.

If instead `max_i alpha_i<=11/16`, the completed Claude D' estimate gives

`||p_Q||_infinity
 <=6 sqrt(e) (11/8)^(-1/2) (1/4)^(-1) Z^(-1/6)
 =24 sqrt(e) sqrt(8/11) Z^(-1/6)
 <33.745 Z^(-1/6)`.

The same two alternatives hold after transposing `M` and using the column marginals `beta_j`.

Therefore a target-scale rank-three volume cut that escapes both D' orientations and both three-hub conversions can have **only one or two `11/16`-heavy volume coordinates on each side**. This is the first substantive reduction; the next step is to stress whether that `<=2 x <=2` heavy survivor is real in strict N3 and whether a completed mixed-hub theorem pays it.
