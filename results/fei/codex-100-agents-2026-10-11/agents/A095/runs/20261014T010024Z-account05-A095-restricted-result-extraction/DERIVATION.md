# Linear and asymptotically sharp shared-collision tax

Author reconstruction, 2026-10-14. Entropies, relative entropies and complete-reference costs are in bits. This extends the paid-reference application of A095-RANK-KL-EQUIVALENCE v2, not its universal equivalence. No universal FEI solution is claimed.

## 1. Exact setup and folding

For every t>=2 and arbitrary disjoint private cubes X,Y, let G(s,X), H(s,Y) be Boolean signs, s a shared t-bit uniform cube, and z a fresh bit. Put F=(G+H)/2+z(G-H)/2 and d=Pr(G!=H)=Inf_z(F). Write Delta=H(F)-(H(G)+H(H))/2. Sign-flipping H exchanges the two selector-frequency atoms at every residual Fourier set, preserving all three entropies and every child spectrum. It changes d to 1-d. Consequently we may prove a bound using d*=min(d,1-d)<=1/2, replacing H by -H when necessary. Endpoints d*=0 have identical or opposite children on the union cube and Delta=0.

Let a_T,b_T be embedded child Fourier coefficients; C consists of all N=2^t subsets of the shared block. These are precisely the possibly colliding rows. Conditional means u(s)=E_X G and v(s)=E_Y H are in [-1,1]. Conditional independence gives 2d*=E_s(1-u v). For x,y in [-1,1], |x-y|<=1-xy because (1-xy)^2-(x-y)^2=(1-x^2)(1-y^2)>=0. Therefore, after folding, |a_T-b_T|<=2d* for every T in C.

## 2. Minority-cap bound

At a collision row let m_T=(a_T^2+b_T^2)/2 and e_T=(a_T-b_T)^2/4. The selector entropy packet is m_T h2(e_T/m_T). Set delta=sum_C e_T. Parseval on the full union cube gives sum_all (a_T-b_T)^2/4=d*, so delta<=d*. The coordinate cap gives e_T<=d*^2 and hence delta<=N d*^2. Also sum_C m_T<=1. Add a dummy row of mass 1-sum_C m_T and minority zero. Jensen for h2 proves

    B_C <= h2(delta),  0<=delta<=min(d*,N d*^2).

No probability mass or conditional normalizer is removed. Outside C a nonzero coefficient identifies a unique child, and its selector bit is fair. Thus

    B_out=(2-E u^2-E v^2)/2 <= E(1-u v)=2d*.

The inequality follows from E(u-v)^2>=0.

## 3. Uniform linear payment, including arbitrarily rare selectors

For 0<=q<=1, h2(q)<=q log2(e/q), since -(1-q)ln(1-q)<=q. The latter follows by integrating -ln(1-q), or by differentiating q+(1-q)ln(1-q). The function h2 is increasing up to 1/2. If d*>=1/N, delta<=d*<=1/2, so B_C<=h2(d*)<=d*log2(e/d*)<=d*(t+1/ln2).

If 0<d*<=1/N, then delta<=N d*^2<=1/N<=1/4. Put x=N d*<=1. Monotonicity gives

    B_C/d* <= x log2(e N/x^2) <= log2(e N).

The final inequality is analytic, not extrapolation: the derivative of x(1+ln N-2ln x) is ln N-1-2ln x>=ln4-1>0 on (0,1]. The limit at zero is zero. Thus in both regimes B_C<=(t+1/ln2)d*.

For completeness the scalar JS term J is <=2d*/ln2. On a row put alpha=(a+b)/2, beta=(a-b)/2, q=alpha^2+beta^2 and w=2|alpha beta|/q. Its JS contribution is q D(w)/ln2, with D(w)=((1+w)ln(1+w)+(1-w)ln(1-w))/2. The derivative bound atanh(w)<=w/sqrt(1-w^2) follows by differentiation (both sides vanish at zero); integration gives D(w)<=1-sqrt(1-w^2). Therefore the row cost is <=2 min(alpha^2,beta^2)/ln2<=2 beta^2/ln2. Parseval sums beta^2 to d*. By the entropy chain rule Delta=B_C+B_out+J. We have proved for all finite cubes

    Delta <= (t+2+3/ln2) min(d,1-d),  t>=2.                 (L)

The exact identity I(F)=(I(G)+I(H))/2+d follows by conditioning on z for each data coordinate, including shared coordinates. Each physical coordinate is counted once.

## 4. One complete reference with exact terminal debt

Supply arbitrary normalized references R_G,R_H positive on each child's true Fourier support; no bounded-cost construction for arbitrary children is assumed. For each child calibrate every shared-only atom T in C to its exact squared Fourier coefficient, and multiply the complementary reference by v_child/R_child(C-complement), where v_child is the true complementary mass. If v_child=0 set that complement to zero. The denominator is positive whenever v_child>0. The categorical KL chain rule shows that CE decreases by exactly the KL of the partition into all singleton C-atoms and their complement. Conditional private-sector debt remains.

Embed calibrated references in the union cube. Define r=(R_G^c+R_H^c)/2 and q=(P_G+P_H)/2. For q(T)>0 use K(0|T)=(a_T+b_T)^2/(4q(T)), K(1|T)=(a_T-b_T)^2/(4q(T)); at q(T)=0 fix K(0|T)=1. Set Q(U,T)=r(T)K(U|T). It is normalized, including reference mass at off-target fibers, and positive on the true parent support. It is fixed before sampling the spectral output. On C, r=q; outside C the nonzero true row and reference row both identify the same unique child. Expanding KL row by row therefore proves

    D(P_F||Q)=(D(P_G||R_G^c)+D(P_H||R_H^c))/2,
    CE(P_F,Q)=(c_G^c+c_H^c)/2+Delta.

Sign folding leaves the calibrated references unchanged and permutes the selector kernel, so (L) bounds this same complete cost. Hence

    CE(P_F,Q) <= (c_G^c+c_H^c)/2+(t+2+3/ln2)d*.

If supplied child costs are <=K_G I(G), <=K_H I(H), the full root cost is <=max(K_G,K_H,t+2+3/ln2) I(F). This is a conditional fixed-overlap class theorem, uniform in private dimensions. At t=0,1 use A097's sharper one-shared/l1 bound; this stage's new theorem concerns t>=2. Costs are ideal negative-log probabilities; prefix-rounding is separate.

## 5. Sharp leading coefficient

Let kappa_t be the supremum of Delta/d* over all Boolean children and private dimensions with 0<d*<=1/2 and exactly t available shared coordinates (dummy coordinates allowed). For even t>=4 take b(s)=(-1)^(s1*s2+...+s_(t-1)*s_t), using binary inputs, and b'=b-2 1_{s=0}. This is an actual Boolean point flip. Every Walsh coefficient of b is +/-e, e=2^(-t/2), by multiplying the two-bit Walsh transforms. Each coefficient of b' is that coefficient minus 2 epsilon, epsilon=2^-t. Thus d*=epsilon and the parent selector-sector masses at every shared row are

    A_T=(+/-e-epsilon)^2, B_T=epsilon^2.

As e>=4epsilon, A_T>=(9/16)epsilon. For positive A,B, (A+B)h2(B/(A+B))>=B log2(A/B). Sum the N rows to get B_C>=epsilon[t-log2(16/9)]. J>=0, so kappa_t>=t-log2(16/9). For odd t>=5 use the same example on t-1 coordinates with one dummy shared coordinate. Consequently

    t-1-log2(16/9) <= kappa_t <= t+2+3/ln2,  t>=4,
    lim_(t->infinity) kappa_t/t = 1.

The bent point-flip obstruction was already established by A097/A086/A094. The new result is its matching linear upper bound and sharp asymptotic coefficient. These are not functions with unbounded H/I: their child influence supplies substantial cost.

## 6. Exact unsupported universal line

No line in the stated restricted theorem is unsupported. For universal closure the first unsupported line is replacing the dimension-dependent collision payment (or the retained arbitrary terminal cost) by an absolute influence payment using a named reserve in the physical child budgets, with no reuse across the composition tree. Selector-only payment cannot be absolute, as Section 5 proves. The new cap delta<=min(d*,2^t d*^2) identifies where a reserve must act, but does not construct it.
