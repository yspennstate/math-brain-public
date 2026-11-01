# Shared-control source transfer

All signs are actual Boolean functions of a uniform cube; entropy is in bits. Fix the complete singleton-leaf binary tree T=(T_Y,(T_C,(T_U,T_V))). Gamma is the complete code expectation, W=Gamma-1. All references are fixed before the Fourier sample.

## 1. Abstract edge property

Let coordinates split into X and Z. A Boolean source g(X) is independent of Z; q(X,Z) is any Boolean mask. For each X-edge e define p_e=P_Z(q differs across e). Assume p_e<=theta<=1/2. Let d_e be the source disagreement indicator (0 or 1), including its dependence on the other X coordinates. The final f=gq disagrees across e with probability

    t_e=(1-d_e)p_e+d_e(1-p_e).                         (1)

For nonnegative K,M put A=max(M,(K+M theta)/(1-theta)). Pointwise,

    K d_e+M p_e <= A t_e.                             (2)

For d_e=0 this uses A>=M. For d_e=1 the ratio (K+Mp)/(1-p) increases with p and is bounded at theta. Z-edges have no source disagreement and contribute exactly the mask's influence. Thus

    K I(g)+M I(q)<=A I(gq).                           (3)

If the SAME complete hierarchy has Gamma(g)<=K I(g) and W(q)<=M I(q), Boolean product-cost subadditivity gives H(f)<=Gamma(f)<=A I(f). This is a conditional transfer theorem, not a universal paid-source assertion. The nonnegative source slack is retained; the signed cancellation conversion has been paid using (2), rather than assuming its refund alone is positive. No real-valued extension is asserted.

## 2. Compatible masks satisfy the property despite shared controls

Let disjoint nonempty C,U,V,Y have sizes r,s,t,k. Let A={C=c*,U=u*}, B={C=c*,V=v*}; q=(1-2*1_A)(1-2*1_B). Put a=2^-s,b=2^-t,c=2^-r and p=a+b-2ab<=1/2. The last inequality follows from (1-2a)(1-2b)>=0. On a C-edge crossing the common subcube boundary, q changes precisely when exactly one private event occurs, a probability p. Other C-edges have probability zero, and all Y-edges have probability zero. Taking X=C union Y and Z=U union V, every source g(C,Y) therefore satisfies (1) with theta=p.

The independently accepted A069-BOOLEAN-MASK-REFUND@1 supplies W(q)<=12 I(q), and hence any paid source Gamma(g)<=K I(g) yields

    H(gq)<=max(12,(K+12p)/(1-p)) I(gq)
           <=(2K+12) I(gq).                          (4)

This includes arbitrary dependence on ALL common controls, with no access to private controls. The A070 source g=q*y lies outside this hypothesis. The edge property is proved directly for this family; it is not imported from geometric percolation estimates.

## 3. One shared coordinate, two unequal retained cores

Choose x in C and choose T_C so x has depth d<=1 within T_C: d=0 for r=1; otherwise T_C=(x,T_(C minus x)). Let

    g(x,Y)=h_+(Y) when x=+1, h_-(Y) when x=-1,
    D=P_Y(h_+ != h_-), J=(I(h_+)+I(h_-))/2,
    B=(Gamma_(T_Y)(h_+)+Gamma_(T_Y)(h_-))/2.

The cores are arbitrary Boolean signs; they may be unequal, biased or constant. Both terminal code bills remain in B on the SAME Y tree. After fixing ALL controls, every actual final Y core is a scalar sign times h_+ or h_-; each source branch has weight one half. Therefore B=E_(C,U,V) Gamma_(T_Y)(f_(C,U,V)) is exactly the average code cost of the actual final terminals, not a hypothetical source-only terminal substitute. Parseval after restricting x gives exactly W_Y(g)=(W_Y(h_+)+W_Y(h_-))/2. All control spectrum of g contains x, of total squared mass D. Consequently

    Gamma_T(g)=B+2 Var(g)+2(d+1)D.                    (5)

Here 2 Var(g) pays the outer join, 2D the control join, and 2dD the path inside C. Uniform-cube Poincare gives Var(g)<=J+D; thus Gamma_T(g)<=B+2J+(2d+4)D. Multiplication by q keeps every Y edge unchanged, so I_Y(f)=J. On the shared x boundary use (2) with K=2d+4,M=12,theta=1/2; off that boundary the source-only cost is bounded by the same coefficient. On other control edges only the mask bill occurs. We obtain the full-reference bound

    H(f)<=Gamma_T(f)<=B+2 I_Y(f)+(4d+20) I_(C,U,V)(f). (6)

More sharply replace 4d+20 by max(12,(2d+4+12p)/(1-p)). Formula (6) pays both source terminals once and all joins. If EACH source core satisfies Gamma_(T_Y)(h_sigma)<=K I(h_sigma), then

    H(f)<=max(K+2,4d+20) I(f),                       (7)

in particular max(K+2,20) for r=1 and max(K+2,24) for arbitrary r. Constant cores are allowed in (5)-(6), but not silently admitted to the paid-code hypothesis of (7). The root bit of every constant code remains in B. This is a code-cost transfer; it asserts no overlapping-product entropy subadditivity.

## 4. Exact scope and first unsupported line

All displayed statements above are proved. Universal FEI remains open. The first unsupported universal step is supplying a complete paid source code or transferring arbitrary normalized terminal references into this one common hierarchy with a nonnegative budget. If the source depends on private coordinates, d_e is correlated with the private mask flip; (1) cannot average d_e and p_e separately. Even for a paid source, no universal theta<=1/2 follows in that situation. Nested use of (4) may also grow constants unless the shared-edge budget is owned once. This stage neither supplies physical stopping-tree ownership nor a dimension-independent payment for arbitrary g.
