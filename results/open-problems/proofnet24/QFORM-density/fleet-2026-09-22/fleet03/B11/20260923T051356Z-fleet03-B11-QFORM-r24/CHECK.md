# Exact algebra check for B11 r24

For the balanced three-bank compressed matrix

B_m = [[m,m-5,m-1/10],[m-5,m,m-1/10],[m-1/10,m-1/10,m]],

the vector (1,-1,0) is an eigenvector with eigenvalue 5. On the orthogonal symmetric two-plane the trace and determinant are

T=3m-5,
D=-(23/5)m-1/50.

Therefore

det(B_m)=5D=-(230m+1)/10,

and the characteristic polynomial factors as

-(lambda-5)(-50 lambda^2+150m lambda-250 lambda+230m+1)/50.

For the quadratic factor p(lambda)=lambda^2-T lambda+D,

p(-3/2)=-(10m+527)/100<0.

Since D<0, its two roots have opposite signs; hence the negative root is strictly below -3/2. The third eigenvalue is 5. Thus for m>5 the exact-rank-three matrix has signature (2,1) and all nonzero eigenvalues have absolute value >1.

Numerical spot checks from the actual run:

m=6:  [-1.8588276689976089, 5.0, 14.858827668997609]
m=20: [-1.6250751071992946, 5.0, 56.625075107199294]
m=100:[-1.5512328026843258, 5.0, 296.55123280268435]

The rank-two local-packet estimate is deterministic: every normalized 2x2 submatrix differs entrywise from J_2 by at most 5/m, so its second singular value is at most its perturbation Frobenius norm, at most 10/m.

For the sign-frustrated companion pattern C0=[[1,-1,1],[-1,1,1],[1,1,1]], the characteristic polynomial is (lambda-2)^2(lambda+1). The physical one-from-each-bank triple is within eta=5/m entrywise of this sign pattern. Thus the designated partner theorem gives 6 sqrt(pi)/(1-10/m), in particular 12 sqrt(pi)=21.269446210866192 at m=20 and 11.816359006036773 at m=100.

For the balanced family the three-bank aggregation plus the source-pinned n=3 finite-dimensional theorem yields 8 sqrt(pi)=14.179630807244127.

QFORM_B11_R24_BALANCED_BANK_CHECK_PASS
