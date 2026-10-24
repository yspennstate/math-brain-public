SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T16:45:41Z.
attacking: the exact-rank-three hybrid/near-null physical direction; consume the ruled-side theorem, preserve source-product provenance after projection, and force a bank-level inequality or source-valid obstruction.

# Early substantive checkpoint: exact hub discriminant and a logarithmic route obstruction

Status: supporting identity plus source-valid obstruction; full QFORM remains open.

Let A=R M R^T with R^T R=I_3 and M real symmetric invertible. Assume the three eigenvalues of M have modulus at least 1. Choose an ORIGINAL physical row u_0=sqrt(h) r, ||r||=1. Relative to r direct-sum r^perp write

M = [[q,b^T],[b,C]],

and for every other spectral row write u_j=t_j r+p_j, p_j in r^perp. Parseval gives

sum t_j^2=1-h,   sum p_j p_j^T=I_2,   sum t_j p_j=0.

For the leaf variables set T=sum t_j X_j and V=sum p_j X_j. Then, with z=sqrt(h)X_0+T,

Q=q z^2+2 z b^T V+V^T C V.

For q != 0 and a target level s, solving Q=s in the ORIGINAL independent coordinate X_0 gives

(qz+b^T V)^2 = D_s(V),
D_s(V)=V^T K V+q s,
K=bb^T-qC.

Thus for a.e. s for which the density is represented by the one-coordinate coarea formula,

p_Q(s) <= h^(-1/2) E[ 1_{D_s(V)>0} D_s(V)^(-1/2) ].                         (1)

The longitudinal leaf variable T cancels from the discriminant exactly. The remaining random vector V is a genuine two-dimensional projection of the original independent leaf coordinates: its frame rows are the p_j and sum p_j p_j^T=I_2. No post-rotation independence is asserted.

The 2x2 discriminant matrix obeys the exact determinant identity

det K = q det M.                                                            (2)

Indeed det(qC-bb^T)=q^2 det C-q b^T adj(C)b=q det M, and det(-(qC-bb^T)) is the same in dimension two. Also ||b||^2=||Mr||^2-q^2 >=1-q^2. For inertia (2,1), q<0 makes K positive definite, q>0 makes K indefinite, and q=0 collapses K to the rank-one matrix bb^T.

Equation (1) is tempting but cannot be the uniform near-null bridge. Fix h=7/8 and 0<eps<=1/4, and take

M_eps=[[eps,sqrt(1+eps),0],[sqrt(1+eps),0,0],[0,0,1]].

Its eigenvalues are exactly {1+eps,1,-1}. Use the Parseval rows

sqrt(h)e1, sqrt(1-h)e1, e2, e3.

Let the original coordinates corresponding to e2 and e3 be independently Uniform[0,1] and Uniform[1,2], respectively (the other two laws may be any cap-one probability densities). Then q=eps,

K=diag(1+eps,-eps),
D_0(Y,Z)=(1+eps)Y^2-eps Z^2.

The absolute discriminant receiver on the right of (1) satisfies

E[1_{D_0>0}D_0^(-1/2)]
 >= integral_{1}^{2} integral_{2 sqrt(eps)}^{1} ((1+eps)y^2-eps z^2)^(-1/2) dy dz
 >= (1+eps)^(-1/2) log(1/(2 sqrt(eps))),                                  (3)

whenever 2sqrt(eps)<=1. Hence this receiver diverges logarithmically as eps downarrow 0.

This is not a counterexample to QFORM. The required ruled one-sheet theorem from math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 applies to this exact target family and gives at s=0 (indeed on the entire one-sheet side)

p_Q(s) <= pi sqrt(2).                                                       (4)

At the exact-null endpoint q=0, the completed designated-partner account03/B10 r24 theorem gives, for h=7/8 and |det M|>=1,

||p_Q||_infinity <= 3*2^(4/3)(h|det M|)^(-1/3) < 7.952.                    (5)

Therefore the nonzero near-null proof cannot integrate out the hub first and then forget the joint original-product geometry behind the transverse discriminant. The logarithm in (3) is a loss of that proof interface, while (4)-(5) show the actual endpoint/ruled-side output remains uniformly controlled.

First unpaid implication after consuming (4)-(5): the two-sheet side of a genuinely nonzero near-null heavy hub. Any successful receiver must keep the hub and at least one transverse product resource coupled through the smoothing step; a bound depending only on the absolute expectation in (1) cannot close the collar.
