SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T00:04:00Z.
attacking: one-sided rank-two cross carriers plus a disjoint square, retaining an arbitrary high-rank same-side curvature exactly and quantifying why cross-volume certificates degenerate.

# Early calculation — one-sided curvature kernel branch

Let X in R^m, Y in R^n and scalar W be disjoint original-coordinate product banks, all coordinate densities <=1. Let C be an m x n real matrix, c=||C||op>0, let B=B^T be n x n, and a!=0. Consider

Q = 2 X^T C Y + Y^T B Y + a W^2 + (arbitrary affine terms allowed after conditioning outside original coordinates).

The latest completed fleet03/B18 theorem QFORM-ONE-SIDED-CROSS-SQUARE-LP-v1 applies with M=2C, sigma=2c. At q=3/2 it gives

||p_Q||_infinity <= (12/2^(1/3)) (|a| c^2)^(-1/3).      (E1)

No restriction on B is needed for this density estimate: Y^T B Y is absorbed into the theorem's arbitrary measurable G(Y).

Now let u,v be top left/right singular vectors, Cv=cu and C^T u=cv. If Bv=0, then the physical symmetric block

A = [[0,C,0],[C^T,B,0],[0,0,a]]

has the invariant vectors (u,+v,0)/sqrt(2), (u,-v,0)/sqrt(2), and the W coordinate, with eigenvalues +c,-c,a. Hence c>=1 and |a|>=1 make this an exact owner-target family, regardless of every other eigenvalue of B on v^perp. Equation (E1) then gives the universal whole-line cap 12/2^(1/3)=9.5244063118... .

Stress family: take C=uv^T, a=1, and B_epsilon=epsilon(I-vv^T), 0<epsilon<1. Then

spec_nonzero(A_epsilon)={-1,1,1, epsilon (multiplicity n-1)},

so exactly three eigenvalues have modulus >=1, while an arbitrary-dimensional nonzero same-side tail is retained. Equation (E1) is uniform in epsilon,m,n.

For every original-coordinate cut I|J, the cross block A_epsilon[I,J] is the sum of at most two rank-one pieces from the uv carrier and one rank-one piece -epsilon v_I v_J^T from the Y-tail; W contributes no cross edge. Thus rank<=3. Removing the epsilon term leaves rank<=2, so

s_3(A_epsilon[I,J]) <= epsilon ||v_I|| ||v_J|| <= epsilon/2.

Also ||A_epsilon[I,J]||op<=||A_epsilon||op=1. Therefore, whenever the cut has rank three,

Z=e_3(M^T M)=s_1^2 s_2^2 s_3^2 <= epsilon^2/4.

The pinned e5f Theorem D numerical certificate, if its row-marginal gate is met, is therefore at least

6 sqrt(e) Z^(-1/6) >= 6 sqrt(e) 2^(1/3) epsilon^(-1/3),

while if the gate fails the theorem is unavailable. The pinned D_5 certificate is unavailable on every cut because rank<=3. This is a certificate obstruction, not a lower bound on the true density.

At epsilon=0 the pinned e5f ruled one-sheet theorem applies to the exact rank-three signature (2+,1-) core and yields p_Q(t)<=pi sqrt(2) for a.e. t>=0. The fleet03/B18 receiver is what remains uniform on the whole line after the high-rank one-sided tail is switched on.

Full QFORM remains OPEN. The next question is whether a general surviving matrix can be routed to a product-preserving one-sided curvature-free cross bank plus a disjoint scalar square, or whether failure forces an existing ridge/grouped-cross/hub/volume receiver.
