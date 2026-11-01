# Scoped independent reconstruction of A044's three-input mux checkpoint

Source: A044/runs/20261012T040658Z-fleet05-A044-non-symmetric-gate-classes/out/DERIVATION_CHECKPOINT.md, section on the three-input multiplexer. This is a checkpoint, not a reviewed campaign claim version. Verdict: HOLDS for the explicit three-input spectrum, global bound and sharp supremum reconstructed below. No acceptance is supplied for the broader profile-transfer claims.

Let the address bit have probability q of selecting data sign X1 rather than X0. Write mj=E Xj, vj=1-mj^2, d=|m1-m0|, and vA=4q(1-q). The five nonconstant spectral masses are

    P0=(1-q)^2 v0, P1=q^2 v1, PA=q(1-q)d^2,
    PA0=q(1-q)v0, PA1=q(1-q)v1.

They follow by expanding f=(1-A)X0+A X1 in centered normalized address and data coordinates. There is no data-data or triple mass. Thus delta=q(1-q)(v0+v1). With E=(ln2)H+ and A(t)=t ln(1/t)/(1-t), direct substitution into E=sum P(S)ln(vS/P(S)) gives

    E/delta=ln4+[d^2 ln(4/d^2)+2v0 A(1-q)+2v1 A(q)]/(v0+v1).

The zero-d term is its continuous value zero. Fixing a difference d between two means in [-1,1], the maximum of their squared norms occurs when one is an endpoint. Hence v0+v1>=d(2-d). The elementary inequality ln(2/d)<=2/d-1, for 0<d<=2, gives

    d^2 ln(4/d^2)<=2d(2-d)<=2(v0+v1).

Also A(t)<=1, by ln(1/t)<=1/t-1. Therefore E<=(4+ln4)delta, strictly for nondegenerate interior biases. The fixed-address bound is ln4+2[1+max(A(q),A(1-q))] in natural units. A is increasing: A'(t)=[ln(1/t)-1+t]/(1-t)^2>=0. If q<=1/2, choose m0=-1+epsilon, m1=1-epsilon^2; then v0/(v0+v1)->1, and d^2 ln(4/d^2)/(v0+v1)->2. This attains the fixed-q supremum. Exchange the data means if q>=1/2. Finally q->0 yields the global bit-unit supremum C*=2+4/ln2.

For a single interior path, set address q=t and data probabilities (t^2,1-t^4). Then the same two fractions tend to 2 and 1, respectively, while A(1-t)->1. This proves sharpness without interchanging an uncontrolled supremum and limit.

Independence: explicit centered-coordinate reconstruction, direct Fraction moments and a rigorously bounded logarithm checker, rather than copying the checkpoint's computational implementation. No repair of the scoped source was necessary. The stage checker records exactly which cases were replayed; it does not inherit validation counts from A044.
