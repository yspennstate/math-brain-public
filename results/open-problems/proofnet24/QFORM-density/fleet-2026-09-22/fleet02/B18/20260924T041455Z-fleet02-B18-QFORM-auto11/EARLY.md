# Early calculation — harmonic frame private-square obstruction

Let n>=6, theta_j=2*pi*j/n (j=0,...,n-1), and

r_j = n^{-1/2}(1, sqrt(2) cos theta_j, sqrt(2) sin theta_j) in R^3.

With R having rows r_j, the root-of-unity identities give R^T R=I_3, hence A_n=RR^T is a rank-three orthogonal projection with nonzero spectrum {1,1,1}. Also ||r_j||^2=3/n<=1/2.

For nonzero w=(a,b,c),

(Rw)_j=n^{-1/2}(a+sqrt(2)b cos theta_j+sqrt(2)c sin theta_j).

A nonzero first-harmonic trigonometric polynomial a+B cos theta+C sin theta has at most two zeros on the circle. Therefore every nonzero u in range(R) has at least n-2 nonzero ORIGINAL coordinates.

Consequence to be proved carefully in REPORT.md: any exact spectral rank-one square uu^T treated as a private source bank consumes at least n-2 original coordinates. An applicable disjoint-cross/private-square receiver can then use at most two remaining original coordinates, whose cross coefficient has magnitude <=||r_i|| ||r_j||=3/n. Thus its reciprocal-cross certificate necessarily deteriorates like sqrt(n), whereas pinned e5f Theorem F pays the same family uniformly by 12.

This is an obstruction to that proof extraction, not a counterexample to QFORM.