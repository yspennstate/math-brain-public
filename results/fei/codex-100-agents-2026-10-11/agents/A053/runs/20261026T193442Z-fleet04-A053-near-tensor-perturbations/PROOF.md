# Tensor repair density forced by complete critical terminals

All signs are Boolean on a finite uniform binary cube. Entropy is in bits,
influence is physical total influence, and D_K(h)=H(h)-K I(h), K>=0.
Let C_K(m)={g:{0,1}^m->{-1,1}:D_K(g)<=0}. Constants belong to this
finite class, and the class is closed under global sign. Define

    r_K(h)=min_{g in C_K(m)} |{x:g(x)!=h(x)}|,
    rho_K(h)=r_K(h)/2^m.

If h violates FEI(K), r_K(h)>=1. If it does not, r_K(h)=0.

## 1. Every parallel fibre must be repaired

Take a coordinate product F=product_j h_j(x_j), on disjoint nonempty
blocks of sizes m_j, with at least two blocks. Let G differ from F on
exactly R vertices of its n-bit cube, delta=R/2^n. Fix any nonempty
PROPER collection J of factors, let m=sum_{j in J} m_j and h_J=product
of these factors. Query ALL complementary original coordinates. On
each of the 2^(n-m) complete physical fibres y, the seed is exactly
sigma_y h_J, sigma_y in {-1,1}. Let e_y be its number of edits. Then

    sum_y e_y=R.                                             (1)

Sign symmetry gives the exact same repair radius on every fibre.
If every complete cofactor of G on this partition is K-certified,
each e_y>=r_K(h_J). Hence

    R >= 2^(n-m) r_K(h_J),   delta >= rho_K(h_J).              (2)

A least-essential-dimension positive K-witness, represented on exactly
its n essential coordinates, has EVERY smaller
Boolean cofactor K-certified. Thus it satisfies (2) simultaneously
for EVERY nonempty proper factor subproduct J of EVERY coordinate
product F used as a comparison seed. No stationarity, Fourier packing,
full support, curvature, parity of R, or fresh budget is assumed.
The product may have irrelevant directions; the retained cube dimension
is still strictly smaller than n, and its essential dimension is no larger.

For one violating m-bit factor alone, R<2^(n-m) already contradicts
criticality. For a fixed violating core and arbitrarily many copies,
every critical perturbation must change a POSITIVE density at least
rho_K(h), not merely a growing number of vertices. If F itself violates
K, tensor additivity of H and I implies some factor violates K.
If all factors are K-certified, this argument supplies no exclusion.

## 2. Exact count and signed complete-bank bounds

Assume r=r_K(h_J)>0. At most floor(R/r) fibres can be K-certified:
each such fibre spends at least r distinct edits, and fibres are disjoint.
Therefore at least max(0,2^(n-m)-floor(R/r)) ACTUAL complete cofactors
violate K. This count concerns the full labelled terminal family.

Set mu=min{D_K(g):dist(g,h_J)<r}. The set is finite, nonempty, and
disjoint from C_K(m), so mu>0. Sign changes do not alter mu. Put
theta=min(1,delta/rho_K(h_J)). The fraction of fibres with e_y>=r
is at most theta. Since H>=0 and I<=m, every cofactor has D_K>=-Km.
Consequently, retaining BOTH positive and negative terminal deficits,

    E_y D_K(G_y) >= mu-(mu+Km) theta,                        (3)
    E_y max(D_K(G_y),0) >= mu max(0,1-delta/rho_K(h_J)).      (4)

Equation (3) rules out even averaged nonnegative full-terminal reserve
S=-E D when delta<rho*mu/(mu+Km). Equation (2), the stronger bound
delta>=rho, needs INDIVIDUAL smaller-child eligibility. Positive-part
debt (4) is not interchangeable with the signed S: negative siblings
may offset positive ones. No child influence or phase price is credited
as new money, and no terminal is pruned.

Boundary checks: r=0 makes the radius claim vacuous and equations(3)--(4)
are not invoked. K=0 has no positive witness because certified functions
have entropy0 and general signs may violate; the same finite argument
still holds when r>0. m>=1 and m<n are essential for the critical
corollary. Equality delta=rho does not force a violating fibre.

## 3. Sharpness of the original-core-fibre bound, and its exact limit

Let h on three bits be negative only at000 and K=2. Its H is
4-(9/8)log2(3), I=3/4, so D_2=5/2-(9/8)log2(3)>0
(integer certificate 2^20>3^9). Flipping its unique negative point gives
a constant. Flipping any other point gives a sign negative on TWO points.
For distinct vertices a,b their difference v!=0 has weight w>=1.
The spectrum has four equal squared masses1/4, so H=2, and physical
edge counting gives I=(3/2) if w>1, and I=1 if w=1. Thus every one-point
edit is K-certified and r_2(h)=1, rho=1/8. This also follows from
the exhaustive exact table check. (The special opposite-pair spectrum
still has four equal masses; the influence is3/2.)

For t>=2, identify each three-bit block label with F_2^3 and define

    F_t=product_j h(x_j),
    E_t={x:x_1 xor ... xor x_t=0},
    G_t=F_t(1-2*1_{E_t}).

Exactly one point is edited in EACH original one-factor fibre. Thus
|E_t|=8^(t-1), delta=1/8, and every such complete three-bit fibre is
K-certified. Equality in (2) is sharp for this named terminal criterion.
This does NOT construct a genuine critical witness. The exact n6
certificate tests G_2, and the n9 certificate retains the proper n6
cofactor G_3|x_3=0=-G_2 to test the missing larger-terminal condition.
No assertion that these examples violate full FEI is made.

## 4. Scoped independent reconstruction of A054's retained phase price

A054 PAIR_RANK_INTERFACE equations(1)--(6) are independently reconstructed
at their analytic scope. A partition-preserving basis consists of a basis
inside W and independently chosen lifts of a quotient basis. Their union
is independent by projecting a putative relation to V/W. Conversely every
such chart has this form; hence J=m_W+m_Q is the actual minimum. For a
two-dimensional quotient any two distinct nonzero directions are independent,
so m_Q is the sum of the two least of its three lift costs.
For the threshold-rank integrals, sort all candidate directions by cost
and retain a direction exactly when independent of its predecessors.
At each threshold the retained directions span exactly the threshold set.
Thus the number of retained basis elements above threshold is dimension
minus threshold rank. Integrating this finite step function gives the
sum of basis costs and proves A054 equation(2), both inside W and in the
quotient. Ties and zero-cost directions cause no change to this argument.

For A054's physical rematch formula(3), inside the changed branch each
character coordinate toggles its derivative disagreement, changing its
cost by1-2Inf_j(g_r), at branch reach1/4. A query-direction edge between
r and r+e_j has endpoint reach1/2; its disagreement changes from
(1-C_(j,0))/2 to(1-s C_(j,v))/2. Its contribution is therefore
(C_(j,0)-s C_(j,v))/4. Summing gives exactly the stated Delta.
The complete mixed-row transform is the direct normalized four-point
Walsh sum; both s signs and every outside coefficient remain.

Write Delta=I(F)-I(f), R=I(F)-J and Omega=H(f)-H(F)+K Delta.
Actual composite phase/reset stationarity gives Omega>=KR. Put
Pi=Omega-KR and t=average optimized child influence. The full child
entropies are unchanged by character rematching. Direct expansion gives

    D_K(f)+S*=L_F-K(J-t)+Pi
              =L_F-K(J+u-t)+(Pi+Ku), 0<=u<=R.

Only joint initial stationarity makes Pi nonnegative, and only genuine
criticality makes S* nonnegative. The exact n3 guard f=h, rematched negative
set{0,5}, has H(F)=2,I(F)=3/2,J=1,R=1/2,t=S*=0, and Pi=D_2(h)>0.
Thus a paid new row cannot certify the original root by dropping Pi.
The proof and fixture HOLD unchanged. This review does not adopt A054's
source census, local flux theorem, or any high-K selection conclusion.

## First unsupported universal line

To finish FEI one must select and pay an original proper block on EVERY
genuine high-K critical source. The repair-density theorem excludes
near products containing violating factor subproducts. It neither bounds
distance to such a product for an arbitrary critical source nor pays Pi
on the complementary class. A supplied product with only certified factors
has r=0 and cannot be used to infer a positive radius. No root-local
comparison seed becomes a fresh inherited reference after restriction.
