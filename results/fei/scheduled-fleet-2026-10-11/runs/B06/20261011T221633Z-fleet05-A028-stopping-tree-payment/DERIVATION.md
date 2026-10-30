# Earlier checkpoint: exact unbalanced activation cost

The stronger final mismatch/KL bill and its coefficient are proved in REPORT.md. This saved checkpoint bounds the smaller exact entropy decrement with a different coefficient; it is retained as provenance, not the final claim.

Let g be any Boolean sign, delta=Pr(g=-1), m=1-2delta, v=4delta(1-delta), p=2^-r, r>=1, and F=1+A_r(g-1) on fresh point-control bits. Write eta(t)=t log2(1/t), eta(0)=0.

Integer Walsh coefficients give the exact full control-first path cost

D_r(delta)=H(F)-pH(g)
=eta((1-2pdelta)^2)-p eta(m^2)
+4p(1-p)delta^2 log2(1/(4p^2delta^2))+2rpv.

This retains every terminal term. The queried influence is Q=2rpdelta and the remaining terminal influence is pI(g). In the expression above, the terms proportional to r sum to 8rpdelta(1-pdelta)<=4Q.

The remaining positive part is at most 4pdelta log2(e)+8pdelta [delta log2(1/(2delta))]_+. The scalar maximum of t log2(1/(2t)) on t>0 is log2(e)/(2e). Consequently

0<=D_r(delta)<=kappa Q, kappa=4+2log2(e)(1+1/e)<8.

The lower bound follows from the exact uniform physical-block entropy identity, not from dropping a negative term. Constants delta=0,1 and m=0 are included by continuity.

A certified terminal cost K I(g) therefore gives complete expected path plus terminal cost at most max(kappa,K) I(F). Products on disjoint physical supports preserve this bound. Arbitrary finite nesting of fresh point activations and disjoint products preserves the same maximum constant. No assertion is made for shared physical variables or for arbitrary terminal cores without an FEI certificate.
