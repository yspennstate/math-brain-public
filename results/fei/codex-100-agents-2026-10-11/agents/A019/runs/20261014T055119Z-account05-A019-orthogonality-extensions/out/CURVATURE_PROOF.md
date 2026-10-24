Let eta(t)=-t log2(t), Psi(u)=eta((1+u)^2/4)+eta((1-u)^2/4)+1-u^2-eta(u^2)/2, and phi(b)=Psi(b/2). For b!=0, phi''(b)=one-quarter log2(b^2/(4-b^2)). Thus -phi'' is even, positive, and decreasing as |b| increases on[-1,1]; its logarithmic singularity at zero is integrable. Extend it by zero outside this interval.

For midpoint t and radius r with t+-r in[-1,1], Jensen's gap is

phi(t)-[phi(t-r)+phi(t+r)]/2 = (1/2) integral_(u=-r..r) (r-|u|)(-phi''(t+u)) du.

The integral is largest at t=0: write the triangular kernel as an integral of centered interval indicators, and use the fact that the integral of a nonnegative even decreasing function over an interval of given length is maximal for the centered interval. This can be proved directly by comparing the two displaced end segments, or by layer-cake intervals. The integrable singularity is handled by monotone truncation; phi is continuously differentiable and the identity follows by absolutely continuous derivatives.

Therefore the gap is between zero and phi(0)-phi(r). The function k(r)=phi(0)-phi(r) is convex on[0,1], has k(0)=0, and lies below its chord r*k(1). Exactly k(1)=2-Psi(1/2)=9/8 log2(3)-1=:A.

For children of any actual private Boolean query with means b0,b1 and disagreement d, r=|b0-b1|/2<=d. Hence 0<=phi((b0+b1)/2)-[phi(b0)+phi(b1)]/2<=A*d. Equality is attained by the actual core h=(-1)^y: b0=1,b1=-1,d=1. Both nonconstant children can approach equality by taking h0 a rare point-defect core and h1=-h0; d remains1 and their means approach+-1. This is an all-dimensional proof, not a finite scalar grid.

For a nonlinear two-bit sign mask its mean is+-1/2, so Psi(beta*mean(mask))=phi(beta). This proves a sharp profile curvature charge through arbitrary genuine private-data exposures while the nonlinear mask remains nonconstant.
