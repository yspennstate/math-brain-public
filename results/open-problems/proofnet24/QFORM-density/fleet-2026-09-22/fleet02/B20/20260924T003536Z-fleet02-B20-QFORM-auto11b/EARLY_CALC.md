# fleet02/B20 early calculation — anchored exact-rank-two decomposition

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

Fresh designated-partner input is fleet03/B20 r42: after its paid diagonal/principal/disjoint-E3 exits, the overlap-one survivor contains one literal original coordinate j and disjoint literal banks R,C with

J_sep >= 1/2304

for the anchored physical block

M = [[b,r^T],[c,N]] = A[{j} union R,{j} union C].

This note attacks the exact-rank-two N endpoint without rotating random variables.

Assume rank(N)=2. Write an SVD only as deterministic coefficient geometry,

N = s1 u1 v1^T + s2 u2 v2^T,   s1>=s2>0,

and decompose

c=a1 u1+a2 u2+c_perp,   r=d1 v1+d2 v2+r_perp,

with c_perp perpendicular span(u1,u2), r_perp perpendicular span(v1,v2). Put

q=b-d1 a1/s1-d2 a2/s2.

Then the exact anchored third-volume identity is

J_sep = (s1 s2 q)^2
      + ||c_perp||^2[(s1 d2)^2+(s2 d1)^2]
      + ||r_perp||^2[(s1 a2)^2+(s2 a1)^2]
      + ||c_perp||^2||r_perp||^2(s1^2+s2^2).

Proof: for x,y in the C-side projection, the component containing the shared anchor in the exterior image equals

T(x wedge y)=b Nx wedge Ny-(r.x)c wedge Ny+(r.y)c wedge Nx.

Evaluate T on v1 wedge v2, v1 wedge w, v2 wedge w for w in ker N. The input sectors are orthogonal. On v1 wedge v2 the u1 wedge u2 component is s1 s2 q and the orthogonal c_perp wedge span(u1,u2) component has squared norm ||c_perp||^2[(s1d2)^2+(s2d1)^2]. Summing the null-input sectors gives the final two terms. Cauchy-Binet identifies ||T||_HS^2 with J_sep.

Hence J_sep>=1/2304 forces at least one of the four displayed square-roots to be >=1/96. This is denominator-free as an identity in the anchored volume even though q itself is written using the two nonzero singular values.

A second analytic calculation gives a source-valid one-transverse payment. Let Z be one original cap-one coordinate, independent of two source banks. Suppose Y=(Y1,Y2,Y3) and W=(W1,W2) are linear projections of the two banks with joint density caps M_R,M_C. For arbitrary same-bank measurable phases, the form with cross terms

2(s1 Y1 W1+s2 Y2 W2)+2Z(gamma1 Y1+gamma2 Y2+alpha Y3+delta1 W1+delta2 W2)

obeys

|phi(t)| <= min{1, pi^(3/2)(M0 M_R M_C)^(1/2)|s1 s2 alpha|^(-1/2)|t|^(-3/2)},

where M0 is the density cap of Z. The proof partially Fourier-transforms Y3, uses the exact two-dimensional bilinear L2 transform norm pi/(|t| sqrt(|s1s2|)), then integrates Z using its density cap. Thus

||p||_infinity <= 3(M0 M_R M_C)^(1/3)|s1 s2 alpha|^(-1/3).

For original cap-one sources, the product-marginal theorem gives M0=1, M_R<=2^(3/2), M_C<=2, hence

||p||_infinity <= 3*2^(5/6)|s1s2 alpha|^(-1/3).

The symmetric C-side version is identical. In particular either

s1s2||c_perp|| >=1/96  or  s1s2||r_perp|| >=1/96

pays the entire ambient form by <24.476, while retaining arbitrary same-bank curvature.

The remaining exact-rank-two collar can therefore be expressed purely in fixed currencies. If additionally E2(N)=s1^2s2^2>4/9 and both one-transverse payments fail, then ||c_perp||,||r_perp||<1/(96s1s2). If the fourth anchored currency is >=1/96, necessarily

s2 < sqrt(2)/64 = 0.0220971...,

and the condition number s1/s2 >4096/3 =1365.333... . Thus the genuinely unpaid fourth-currency endpoint is an extremely ill-conditioned rank-two collar, not a generic rank-two crossing.

All coefficient rotations above are deterministic identities only. No projected random coordinates are asserted independent; density caps are invoked only through source-valid product-marginal bounds.