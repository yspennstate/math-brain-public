# account02/B07 early calculation — third compound controls the dangerous exterior tail

Programme: QFORM-DENSITY-3EIG-20260922. Full unrestricted theorem remains OPEN.

Incoming live separator from account03/B07 r48: a literal original-coordinate cut M has

- s2(M) > d_* = 0.10429071727552326290...,
- s1(M)s2(M) > p_* = 1.19876993884320...,
- dist_F(M,rank<=2) < 2^-16,

unless an already-paid physical E3 branch occurs. The r48 pair-block determinant law also has E2(M)>p_*^2, and all but at most two matched physical pairs K have actual two-minor inclusion marginal beta_K<=2/3.

Write x_j=s_j(M)^2, Z2=e2(x), Z3=e3(x), and

R2 := Z2-x1 x2
    = (x1+x2)T+U,
T=sum_{j>=3}x_j,
U=sum_{3<=i<j}x_i x_j.

Then

Z3=x1 x2 T+(x1+x2)U+V,
V=e3(x_3,x_4,...),

and therefore

Z3-(x2/2)R2
 = (x2/2)(x1-x2)T+(x1+x2/2)U+V >=0.

Hence the exact inverse-free inequality

    R2 <= 2 Z3 / s2(M)^2.                                      (E1)

This directly resolves the reciprocal-fan warning once a genuine s2 floor is available: a Frobenius-small tail can carry order-one second exterior volume only by forcing order-one third volume.

Set eta=1/144 and

    delta_* := d_*^2 p_*^2 / 288
             = 5.427133547214097e-5.

If Z3>=delta_*, the completed marginal-free physical-Z3 receiver gives a universal density bound. If Z3<delta_*, then (E1), s2>d_* and Z2>p_*^2 imply

    (Z2-x1x2)/Z2 < 1/144.                                      (E2)

Let z be the full vector of physical 2x2 minors of M and a its leading exterior singular component

    a=s1s2 (u1 wedge u2)(v1 wedge v2)^T.

After normalisation w=z/sqrt(Z2), v=a/(s1s2), orthogonality gives

    <w,v>^2 = x1x2/Z2 > 143/144.

For the squared-coordinate probability laws p_c=w_c^2 and q_c=v_c^2,

    d_TV(p,q)
      <= (1/2)||w-v||_2 ||w+v||_2
      = sqrt(1-<w,v>^2)
      < 1/12.                                                    (E3)

Thus the actual determinant law is within 1/12 total variation of the product Pluecker law of the leading left/right two-planes. In particular, for every r48 determinant-stable matched pair K (beta_K(p)<=2/3),

    q{column pair intersects K} < 3/4,
    q{column pair avoids K} > 1/4.                              (E4)

Therefore deleting K from the *leading rank-two SVD carrier* L=s1u1v1^T+s2u2v2^T leaves

    e2(L_{-K}L_{-K}^T)
      > (1/4)(143/144)p_*^2
      = 0.35676746419652866...,

so

    s1(L_{-K}) s2(L_{-K}) > 0.597300145819946... .              (E5)

The nonzero tail is not deleted: column restriction only gives ||(M-L)_{-K}||_F<2^-16.

This is the first substantive calculation for this run. It carries the whole second-minor law and does not select or invert a single coordinate minor.
