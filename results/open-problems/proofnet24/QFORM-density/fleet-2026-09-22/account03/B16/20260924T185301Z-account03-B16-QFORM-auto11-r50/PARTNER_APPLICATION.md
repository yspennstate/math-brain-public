# Partner application: strict-target repair by a definite projected plane

Add a fresh independent Y~Uniform[-1/2,1/2] to the five-variable construction and set Qtilde=Q+Y^2.

The three nonzero eigenvalues are

eps+1/eps,  -(eps+2/eps),  1,

so for 0<eps<=1/4 all three have modulus at least one.

In the original-coordinate bank (U,T1,Y), define the orthonormal projected coordinates

Z1=(sqrt(eps) U + T1/sqrt(eps))/sqrt(eps+1/eps),
Z2=Y.

After conditioning on the disjoint bank (H,S,T2), the quadratic part in (Z1,Z2) is definite with matrix diag(eps+1/eps,1).

The designated account04/B16 theorem at commit 7f2bb2d330022b09a6af6e39ab09d054caeaa346 therefore gives

||p_Qtilde||_infinity <= 2 pi / sqrt(eps+1/eps)
                      <= 4 pi / sqrt(17)
                      < 3.048.

This is an actual three-large-eigenvalue target inequality. The argument retains dependence inside the two-dimensional projection and uses independence only between disjoint original-coordinate banks. I record essential boundedness only; continuity is not claimed from this partner theorem.
