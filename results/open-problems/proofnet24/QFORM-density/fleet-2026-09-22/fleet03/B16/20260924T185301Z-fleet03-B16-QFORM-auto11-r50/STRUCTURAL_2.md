# Structural proof step 2

For a good seed S={s1,s2}, T, let b=det A[S,T]. The completion has rank at most six outside its diagonal defect. Since s_7(A)>=1, there is h outside S union T with |D_h|>=1-epsstar.

Writing C1=det A[{s2,h},T] and C2=det A[{s1,h},T], the bordered determinant identity gives

b(D_h-A_hh)=A_s1h C1-A_s2h C2

up to signs. Since |A_hh|<eta, Cauchy gives

(1-epsstar-eta)^2 b^2 <= 2(A_s1h^2 C1^2+A_s2h^2 C2^2).

Summing this over good seeds, whose determinant-squared mass exceeds V_2/2, proves U_2 > (1-epsstar-eta)^2 V_2/4.
