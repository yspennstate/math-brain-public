# account02/B18 r28 early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

## First unpaid implication

For the exact target-valid circular Schur-isotropic family from account02/B18 r27,

v_j=m^{-1/2}(1,sqrt(2) cos(2pi j/m),sqrt(2) sin(2pi j/m)),

u_0=m e_1, D_m=[[0,(1+m^2)^(-1/2),0],[(1+m^2)^(-1/2),0,0],[0,0,1]], A_m=U D_m U^T,

the nonzero spectrum is exactly {-1,1,1}. The pinned e5f ruled-surface theorem already pays the one-sheet side t>=0 by p_Q(t)<=pi sqrt(2). The unpaid side is t<0.

Latest designated-partner account03/B18 r27 supplies an all-pivot theorem for three pairwise disjoint ORIGINAL-coordinate scalar banks: if conditioning outside leaves S^T K S+ell^T S+c with sigma_min(K)>=s, then ||p_Q||_infinity<296/s. The source-matching question is whether the circular family admits such an exact scalar-bank representation with s bounded below.

## New obstruction under proof

Claim `QFORM-CIRCULAR-SCALAR-BANK-COMPILER-BARRIER-v1`: every exact three-disjoint-scalar-bank representation of a conditioned principal subform of A_m has sigma_min(K)<=18/m. If the hub is one of the active banks, then sigma_min(K)<=12/m. Thus the partner theorem cannot yield a dimension-free certificate on this family; a multidimensional/product-coupled aggregation is genuinely required.

Proof skeleton. Let T=[a_1,a_2,a_3] have disjoint unit columns supported on the three banks. Exact dependence only through S=T^T x forces A_BB=T K T^T, so each within-bank principal block has rank <=1.

1. A bank containing the hub and any residual coordinate is impossible. A_00=0. Since the hub coefficient in its aggregate is nonzero, A[bank,bank]=K_rr a_r a_r^T implies K_rr=0, so the whole bank block would vanish. But for every residual j, either A_0j!=0 or, if A_0j=0 (cos theta_j=0), A_jj=2/m!=0.

2. Any residual-only bank contains at most two coordinates. For any three distinct residual rows, the 3x3 matrix V_J is invertible: after the common first coordinate is removed this is equivalent to three distinct points on the unit circle being collinear, impossible. Since D_m is invertible, det(V_J D_m V_J^T)=det(V_J)^2 det(D_m)!=0. Hence a three-point bank would have rank 3, contradicting rank <=1.

3. If all banks are residual, their union has at most six coordinates. ||D_m||op=1 and ||v_j||^2=3/m, so |A_ij|<=3/m on the residual block and therefore ||K||op<=||A_BB||op<=18/m. Hence sigma_min(K)<=18/m.

4. If the hub is active, it must be a singleton bank and the other two banks use at most four residual coordinates. In the bank basis K=[[0,b^T],[b,C]], with ||C||op<=12/m. Choose unit z perpendicular to b and w=(0,z). Then ||Kw||=||Cz||<=12/m, hence sigma_min(K)<=12/m.

This is a proof-method obstruction, not a QFORM counterexample and not a lower bound on the true output density.

Primary-source checkpoint: Livshyts--Paouris--Pivovarov Theorem 1.1 (arXiv:1507.07949) assumes a genuine product f=prod f_i of bounded one-dimensional probability densities and gives ||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2),2^(k/2)) prod ||f_i||_infinity^{gamma_i}; in the cap-one class, <=2^(k/2). It does not create independence among projected coordinates.
