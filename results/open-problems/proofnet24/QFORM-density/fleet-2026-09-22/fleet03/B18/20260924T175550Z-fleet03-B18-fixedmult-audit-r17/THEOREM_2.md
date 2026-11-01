# Lemma: dependent two-slope reciprocal half moment

Let (T1,T2) have joint density cap M12 and marginal density caps M1,M2. Then

E |T1 T2|^(-1/2) <= 8( sqrt(M1 M2) + sqrt(M12) ).

Proof. For a,b>0 split R^2 into the four regions determined by |x|<=a and |y|<=b. The central rectangle contributes at most 16 M12 sqrt(ab). The two cross strips contribute at most 4 M1 sqrt(a/b) and 4 M2 sqrt(b/a), using the corresponding marginal cap. The outer region contributes at most 1/sqrt(ab).

Set a=t/M1 and b=t/M2. With M=sqrt(M1 M2) and rho=M12/(M1 M2), the total is at most

M(16 rho t + 8 + 1/t).

The minimizing t is 1/(4 sqrt(rho)), giving 8 M(1+sqrt(rho)), which is the stated bound. No independence of T1,T2 is used.
