# Root derivation — a common hyperbolic shift pays X044's last scalar

Status: proved comparison for the exact scalar forms supplied by X044. Root contribution, not an extra sub-agent. The surrounding count-Hessian identification and its theorem belong in agents/X044.md.

X044 reduces its remaining plus block to

    q=B(x+y)^2+u x^2+v y^2.

Let r=tanh(a), s=tanh(b), with a≥b≥0 after swapping the variables if necessary. Put A=a+b, D=a−b, l=log cosh(A), m=log cosh(D), and r0=tanh(D). The supplied exact formulas are

    B=1+exp(A)/cosh(D)−A−log cosh(A),
    u=(r−s)^2/[(1−r)(1−rs)]+(1−s)l+2s m,
    v=(r−s)^2/[(1−s)(1−rs)]+(1−r)l+2r m.

Hold D fixed and compare with b=0, a=D, namely the rank-one singular-value case (r0,0). Define

    Uc=exp(D) sinh(D)^2/cosh(D),
    Vc=exp(−D) sinh(D)^2/cosh(D).

The elementary identities r−s=sinh(D)/(cosh(a)cosh(b)) and 1−rs=cosh(D)/(cosh(a)cosh(b)) give

    u=(1+s)Uc+(1−s)l+2s m,
    v=(1+r)Vc+(1−r)l+2r m.

At the rank-one baseline, u0=Uc+m and v0=(1+r0)(Vc+m). Consequently

    u−u0=s Uc+(1−s)(l−m)+s m≥0,
    v−v0=(r−r0)Vc+(1−r)(l−m)+(r−r0)m≥0.

All signs follow from A≥D≥0, l≥m≥0, and r≥r0. The remaining coefficient is monotone because

    dB/dA=exp(A)[1/cosh(D)−1/cosh(A)]≥0.

Thus B≥B0 as well. It follows exactly that

    q−q0=(B−B0)(x+y)^2+(u−u0)x^2+(v−v0)y^2≥0.

X044 checked that q0 is X030's positive rank-one form under T=x+y, S=y. For D>0 its strict positivity therefore transfers to every common hyperbolic shift b≥0. If D=0 but b>0, m=Uc=Vc=0, u=v=(1−r)log cosh(2b)>0, and B>0 by the displayed monotonicity from B0=2. The zero matrix case retains its expected Hessian degeneracy.

This resolves the scalar plus-block condition without discarding either logarithmic term or estimating the divergent logarithms separately. It does not by itself claim a full measured-entropy theorem; use X044's independently derived complete count-Hessian identity for that implication.
