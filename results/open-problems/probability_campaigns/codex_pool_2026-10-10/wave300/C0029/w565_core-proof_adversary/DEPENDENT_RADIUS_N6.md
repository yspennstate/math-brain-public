# Dependent-radius obstruction at a nontrivial C0029 scale

This refinement was derived after reading the paired proof, and is separate from the earlier frozen independent checkpoint. It is a proof written by w565; w566's independent check is pending. It refutes the independent-radius shortcut, and does not refute the parent conjecture.

Let A be the 5 by 6 sign matrix [J_5-2I_5 | 1], where J_5 is the all-ones matrix and 1 is the all-ones column. Its Gram matrix is AA^T=4I_5+2J_5, with eigenvalues 14 once and 4 four times. A unit kernel vector is v=(1,1,1,1,1,-3)/sqrt(14). The right singular vector corresponding to sqrt(14) is u=(3,3,3,3,3,5)/sqrt(70). These two vectors are orthogonal.

For X uniform on {-1,+1}^6, put S=X_1+...+X_5, eta=X_6, y=<X,v>^2=(S-3eta)^2/14, and b=<X,u>^2=(3S+5eta)^2/70. The sum of the other four squared singular coordinates is 6-y-b. At t=3/8, the exact squared radius in the spectral threshold identity is

r(X)^2 = 9/64 + 9b/887 + 9(6-y-b)/247.

The threshold event is E(X)={y<=r(X)^2}. The corresponding epsilon is t sqrt(6), and epsilon^2=27/32<1. The six classes below group (S,eta) with their simultaneous sign reversals. Counts are among all 64 rows.

| S and eta class | count | y | b | r(X)^2 >= 2/7 | E(X) |
| --- | ---: | ---: | ---: | --- | --- |
| abs(S)=5, eta has the sign of S | 2 | 2/7 | 40/7 | no | no |
| abs(S)=3, eta has the sign of S | 10 | 0 | 14/5 | no | yes |
| abs(S)=1, eta has the sign of S | 20 | 2/7 | 32/35 | yes | yes |
| abs(S)=1, eta has the opposite sign | 20 | 8/7 | 2/35 | yes | no |
| abs(S)=3, eta has the opposite sign | 10 | 18/7 | 8/35 | no | no |
| abs(S)=5, eta has the opposite sign | 2 | 32/7 | 10/7 | no | no |

All entries and inequalities are rational. The close boundary in the second row is strict: 2/7-r(X)^2=39125/490759360>0. In all classes r(X)^2<8/7. Hence P(E(X))=(10+20)/64=15/32.

If X' is an independent copy of X and only the radius is replaced, P(y(X)<=r(X')^2)=10/64+(22/64)(40/64)=95/256. The independent replacement underestimates by 25/256. Orthogonal linear coordinates of X have zero covariance because Cov(X)=I_6, but their joint law does not factor. Marginal information and zero covariance cannot justify this upper comparison.

The matrix A is an admissible realization of five iid Bernoulli rows. Its particular ordered realization has probability 2^(-30). The example refutes a pointwise inference used inside conditioning; the missing signed average over actual skeleton laws remains unproved.

NEXT: Obtain w566's check of the six rational classes and the <= boundary, keeping the parent signed replacement estimate open.
