# Mixed star-minor theorem: statement and setup

Assume A is real symmetric, s_7(A) >= 1, eta=1/100, kappa=1/6400, there is no eta scalar or principal-pair pivot, and V_3(A) < kappa^3. The audited order-two spectral-volume argument gives V_2(A) >= kappa^2.

Define U_2(A) by summing, over disjoint two-sets S,T, all h outside S union T and all s in S, the quantity

A_sh^2 * det A[(S minus {s}) union {h}, T]^2.

Then

U_2(A) > (558009/2560000) V_2(A)
       >= 558009/104857600000000.

Proof setup: sample nonsingular disjoint two-seeds (S,T) with probability det(A[S,T])^2/V_2. Their interpolation completion A=D+R+E has rank(R)<=6 and D diagonal, zero on S union T. The volume-sampling estimate gives E ||E||_F^2 <= 9 V_3/V_2 < 9/6400. Put eps*=3 sqrt(2)/80, so eps*^2=18/6400. Markov therefore shows that seeds with ||E||_F <= eps* carry strictly more than half of the V_2 determinant-squared mass.
