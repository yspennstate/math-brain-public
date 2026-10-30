SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-24T09:30:03Z.
attacking: the partner r45 genuinely two-dimensional same-bank overlap by proving a determinant-homogeneous receiver for an arbitrary dependent projected pair plus one disjoint source scalar when that scalar has zero quadratic pivot.

# Early calculation — pair plus null scalar

Let Z=(S,U) have an arbitrary joint probability density rho with ||rho||_infinity<=M. Let V be independent of Z with scalar density f satisfying ||f||_infinity<=N. Consider

Q = Z^T C Z + 2 V ell^T Z + p^T Z + qV + c,

where C is symmetric 2x2 and

B = [[C,ell],[ell^T,0]]

is invertible. I claim

||p_Q||_infinity <= 6 (MN)^(2/3) |det B|^(-1/3).

This is exactly the interface left open by fleet03/B16 r45: the two coordinates of Z may be dependent projections of the same original product bank; V alone is source-separated.

Translate Z so that qV is absorbed into 2V ell^T Z. Let L=||ell||>0, choose e=ell/L and w perpendicular to e, and write x=w^T Z, y=e^T Z. Orthogonal change of the pair preserves its joint density cap M and does NOT create independence. Writing the rotated C as [[a,c],[c,d]], the carrier matrix in (x,y,V) is

[[a,c,0],[c,d,L],[0,L,0]],

hence

det B = -a L^2.

Thus invertibility forces a!=0. Complete the x-square by the determinant-one shear

s = x + (c/a)y + p_x/(2a).

The joint density of (s,y) is still bounded by M, and Q becomes

Q = a s^2 + h(y) + 2 L y V + constant,

where h is an arbitrary real quadratic polynomial. For a.e. t,

p_Q(t)= integral [1/(2L|y|)] J_t(y) dy,

J_t(y)= integral rho_tilde(s,y) f((t-h(y)-a s^2)/(2Ly)) ds.

Two bounds are available before any conditional density is formed:

J_t(y) <= N m(y),    m(y)=integral rho_tilde(s,y)ds,

and, using the joint cap through the square,

J_t(y) <= M integral f((t-h(y)-a s^2)/(2Ly)) ds
        <= 4M sqrt(N L|y|/|a|).

The last inequality is the same half-potential computation as the preceding fleet02/B16 curved-cap theorem: for every probability density f<=N,

sup_z integral f(v)|v-z|^(-1/2)dv <= 2sqrt(2N).

Therefore

p_Q(t) <= integral min(A m(y)/|y|, B0/|y|^(1/2))dy,
A=N/(2L),   B0=2M sqrt(N/(|a|L)).

Splitting at |y|=R yields

p_Q(t) <= 4 B0 sqrt(R) + A/R.

Optimizing at sqrt(R)=(A/(2B0))^(1/3) gives

||p_Q||_infinity <= 6(MN)^(2/3)(|a|L^2)^(-1/3)
                  = 6(MN)^(2/3)|det B|^(-1/3).

For source projections from disjoint original-coordinate banks, the pinned completed two-dimensional projection theorem gives

M <= 2 det(G)^(-1/2),

where G is the Gram matrix of the two projection coefficient vectors, while the scalar projection bound gives N<=sqrt(2)/tau. Hence

||p_Q||_infinity <= 12 [|det B| det(G) tau^2]^(-1/3).

If the physical form has exact rank three with carrier columns given by those source projections, then |pdet A|=|det B|det(G)tau^2. Thus three nonzero eigenvalues of modulus at least one imply the target-level bound <=12.

Partner r45 strict family Q_*=3S^2+6(S+U)V has det B_*=-27. If S,U are now allowed to be an orthonormal dependent projection pair from ONE product bank and V is a unit projection from a disjoint bank, M<=2, N<=sqrt(2), so

||p_Q*||_infinity <= 6(2sqrt(2))^(2/3) 27^(-1/3)=4.

This closes r45's named two-dimensional shared-overlap gap for every invertible zero-pivot 3x3 carrier, not merely its rank-one overlap normal form.
