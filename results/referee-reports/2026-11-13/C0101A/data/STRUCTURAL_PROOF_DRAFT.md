# Local rigidity draft (to audit)

Let H:Z^d->Z satisfy Delta H<=0 and H(x)>=q_D(x)+b0.x+c, with ||D||op<1/(10d). Claim: D is negative semidefinite.

Choose epsilon>0 arbitrarily small and x0 within epsilon of inf_x[H(x)-q_D(x)-b0.x]. Translate x0 to 0, subtract H(x0) and an integer linear function. Obtain integer h, h(0)=0, Delta h<=0, and h(x)>=q_D(x)+b.x-epsilon, with each |b_i|<=1/2.

For sufficiently small epsilon, q_D(+-e_i)+b.(+-e_i)-epsilon>-1. Thus h(+-e_i)>=0, and Delta h(0)<=0 forces all these values to be zero. Consequently |b_i|<=epsilon-D_ii/2<=epsilon+||D||op/2.

Suppose Dv=lambda v, |v|=1, lambda>0. Choose the sign of v so b.v>=0. There is a nearest-neighbor lattice path from 0 following tv (t>=0) within distance sqrt(d)/2 (allow an ordering at simultaneous coordinate crossings). Every path vertex and its lattice neighbors can be written tv+e with t>=0 and |e|<=2sqrt(d). Write delta=||D||op. Then

q_D(tv+e)+b.(tv+e)-epsilon
 >= lambda t^2/2-lambda t |e|-delta |e|^2/2-|b||e|-epsilon
 >= -delta |e|^2-|b||e|-epsilon
 >= -5d delta-(2d+1)epsilon > -1.

Choose epsilon with 5d delta+(2d+1)epsilon<1. Hence h>=0 on this path and all its neighbors. Starting at h(0)=0, the superharmonic inequality forces h=0 on successive vertices. But along the path q_D+b.x-epsilon grows to +infinity, contradicting h=0. Thus no positive lambda exists.

For an asymptotic representative H=q_D+o(|x|^2), replace D by D-eta I to get the required lower bound, choosing eta small enough to preserve a positive eigenvalue and the strict norm bound. For a topological closure of such matrices, the forbidden set (positive eigenvalue and norm<1/(10d)) is open.

Application: M integer symmetric, tr M=1. Define p_M(x)=sum_i M_ii x_i(x_i-1)/2 + sum_{i<j} M_ij x_i x_j. Then p_M integer, Delta p_M=1, Hessian M. Subtract p_M from any representative for B. The lemma implies B<=M whenever ||B-M||op<1/(10d). Hence M is isolated among maximal matrices, with an explicit isolation radius. M is maximal because tr B<=1 and a nonzero positive semidefinite B-M would have positive trace.

## Diagonal ceiling bound and exact diagonal classification

For any symmetric A in Gamma_1, let k_i=ceil(A_ii), K=diag(k_i), s=sum k_i. If s>=2, subtract the integer quadratic p_K. The residual H has Delta H<=1-s<0 and a lower quadratic obstacle with Hessian D=A-K, whose diagonal entries all lie in (-1,0]. Normalize an epsilon-contact at the origin and the slope to [-1/2,1/2]^d, as above. For epsilon sufficiently small every lattice neighbor has obstacle value >-1, so its integer H value is >=0. But H(0)=0 and Delta H(0)<0, contradiction. Thus s<=1. For asymptotic representatives use A-eta I; ceilings are unchanged for sufficiently small eta>0. The condition persists under closure: ceilings at a limit cannot exceed their limiting lower values.

For diagonal A, k_i-a_i=p_i>=0. If p_i>0 define the integer convex function
 F_p(n)=sup_{m in Z}(m n-ceil(m^2/(2p))).
Then q_p(n)-1-1/(8p)<=F_p(n)<=q_p(n); it is convex as a supremum of affine functions, and integer-valued. Set F_0=0. The function sum_i[k_i*n_i(n_i-1)/2-F_{p_i}(n_i)] is integer, has Delta<=sum k_i<=1 and differs from q_A-sum k_i*n_i/2 by O(1). This proves sufficiency for every real diagonal A, including irrational entries. Such irrational members are dominated by integer diagonal matrices; they are not irrational maximal elements.

## Closed obstacle class (any dimension)

Let A_n->A with integer g_n satisfying Delta g_n<=1 and g_n>=q_{A_n}+affine. Translate an epsilon_n-contact, subtract its integer value and integer linear slope. Then g_n(0)=0 and g_n>=q_{A_n}+b_n.x-epsilon_n, |b_{n,i}|<=1/2, epsilon_n->0. This gives a uniform lower bound on every finite set. From Delta g_n(x)<=1, a bound above at x and bounds below at its other neighbors give an upper bound at each neighbor. Starting at 0, propagate finite upper bounds throughout each finite ball. Integer-valuedness and a diagonal subsequence give a pointwise limit g, together with b_n->b. It satisfies Delta g<=1 and g>=q_A+b.x. Thus the obstacle class is closed. This argument also justifies using contact limits below.

## Zero-coordinate reduction and lifting maximal points

Let C be k by k with sum_i ceil(C_ii)=1. Then
 C direct-sum 0_(d-k) in Gamma_1(Z^d) iff C in Gamma_1(Z^k).

The forward implication: subtract p_K where K=diag(ceil C_ii,0,...,0), whose Laplacian is one. The residual has Delta<=0. Normalize epsilon_n-contacts and slopes; the argument used for the ceiling bound forces every neighbor value to zero, and yields |b_{n,j}|<=epsilon_n in the added zero directions. Use the compactness argument just given to obtain integer h with Delta h<=0 and
 h(x,z)>=q_{C-K}(x)+b.x
with no linear term in z. For each x define H(x)=min_{z in Z^(d-k)}h(x,z). This minimum is finite and attained since h is integer and bounded below for fixed x. At a minimizing z, Delta_z h>=0 and Delta_x H<=Delta_x h. Hence Delta H<=0. Add back p_K on Z^k to obtain a representative for C. The reverse implication is the constant extension of a representative.

If C is maximal in Gamma_1(Z^k), tr C>0 and sum ceil C_ii=1, then C direct-sum 0 is maximal in every larger dimension. Indeed, suppose B>=C direct-sum 0 and B is admissible. Any positive diagonal entry in an added direction would make sum ceil B_ii>=2, impossible. Thus the added diagonal entries of the positive semidefinite difference vanish. All corresponding rows and columns of that difference vanish as well. So B=C' direct-sum 0, C'>=C. Moreover tr C'>0, so the ceiling bound implies sum ceil C'_ii=1. Zero-coordinate reduction gives C' in Gamma_1(Z^k), and maximality gives C'=C.

In particular every 2D Apollonian circle matrix has positive trace, ceiling sum one, and is maximal by LPS. Its zero extension to Z^3 (or any larger dimension) is therefore a rational maximal matrix. Integer trace-zero symmetric translations preserve admissibility and maximality, by adding/subtracting the associated integer harmonic quadratic.
