# R15 idea-first note — projective fourth-order obstruction

Status: SELF_CHECK_ONLY / NOT CLAIMED. This is a research idea recorded before any checker.

For the retained Talagrand F0111 k=2 hazard, let G=P-F be a nonnegative quadratic-certificate gap with an interior exact contact q. If H=D^2G(q) has a null vector h, then Hh=0 and local nonnegativity already gives D^3G(q)[h,h,h]=0. Instead of staying on the straight line q+eps h, bend the path at order eps^2:

    x(eps)=q+eps h+eps^2 v.

The eps^4 coefficient is

    (1/2)<v,Hv> + (1/2)D^3G(q)[v,h,h] + (1/24)D^4G(q)[h,h,h,h].

It must be nonnegative for every v. Hence the cubic functional b(v)=D^3G[v,h,h] must vanish on ker H, and minimization over v gives the stronger tangent-cone condition

    D^4G[h^4] >= 3 b^T H^+ b.

A particularly useful certificate-free specialization is v=c q. The preceding all-ray theorem says q^T H q=-g_q''(1)=K(q)>0, where g_q(s)=F(sq)/s and K is the dimensionless all-ray curvature functional. Since P is quadratic and F=linear-log S,

    D^4 log S(q)[h^4] * K(q)
      >= 3 (D^3 log S(q)[q,h,h])^2.

This is a new necessary condition for any Hessian-null global quadratic certificate. It should be tested first on the exact n=4 local null candidate from the earlier graph-flow report; preliminary hand calculation indicates a large violation, which would explain its failure without using a special coordinate-face test.

Methods intended this run: #5 add a projective bending parameter; #11 dualize/minimize the fourth-order form; #24 find the extremal bend v. Previous run used #18/#20/#27, so this is a different triple.
