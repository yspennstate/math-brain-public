# Arbitrary-seed signed profile and one unchanged source bank

Entropy is in bits. All cubes are finite and uniform. This continues the preceding two-control attachment; the seed is now ANY Boolean sign, not a bent or flat-spectrum seed. It does not assert that every physical data query has this attachment form.

## 1. Physical functions, accounts and complete spectra

For an integer d>=0 put N=2^d, delta=1/N. Let b:{0,1}^d->{-1,+1} satisfy b(0)=1. The negative marked-point case is reduced by multiplying all outputs by -1. Let

    c(x,j)=b(x)-2*1_(x=0,j=1), q(z)=(-1)^z,
    F(x,j,z)=c(x,j)+1_(x=0,j=0)(q(z)-1).

Equivalently F=b+1_(x=0)(r(j,z)-1), where r=+1 only at j=z=0. These are actual Boolean signs. Query DATA coordinate j in the incoming core c; keep both physical children:

    F_0(x,z)=b(x)+1_(x=0)(q(z)-1),
    F_1(x,z)=b(x)-2*1_(x=0).

The second child's z remains a physical dummy. The same A066 accounts are G=0 and R=(d+1)delta/2. The children have G_0=G_1=0, R_0=d delta, R_1=0. Thus e=Inf_j(F)=delta/2 and the actual reserve release D_R=e, with E R_child=R-e. No reserve is renewed.

Write a_T=hat b(T), h(u)=-u^2 log2(u^2), h(0)=0, and E(v)=sum_T h(a_T-v). Parseval and Fourier inversion give sum a_T^2=1 and sum a_T=1. The COMPLETE Fourier arrays, with U a subset of {j,z}, are

    hat F(T,empty)=a_T-3delta/2; hat F(T,U)=delta/2 if U nonempty;
    hat F_0(T,empty)=a_T-delta; hat F_0(T,{z})=delta;
    hat F_1(T,empty)=a_T-2delta; hat F_1(T,{z})=0.

Both child entropies, including empty Fourier atoms and dummy occupancy, are retained. Their exact entropy decrement is

    DeltaH=H(F)-E H(F_j)
          =E(3delta/2)-[E(delta)+E(2delta)]/2+delta*(d/2+3/2).  (1)

This is the same profile as stage7, with its previous bent-core width d=2m. No old constant has been changed on the same variables.

## 2. The arbitrary-seed curvature bound, including zeros

For v in [delta,2delta],

    sum_T(a_T-v)^2=1-2v+Nv^2 <=1,                          (2)

because Nv is in [1,2]. At points where no a_T-v vanishes, concavity of ln gives

    sum_T ln((a_T-v)^2)
       <=N ln([sum_T(a_T-v)^2]/N)<=N ln(1/N)=-Nd ln2.

Direct differentiation therefore yields

    E''(v)=-(2 sum_T ln((a_T-v)^2)+6N)/ln2
           >=N*(2d-6/ln2)=:mu.                            (3)

ZERO CHECK: h is C1 on the whole real line, since u ln(u^2)->0 as u->0. Its second derivative need not exist at zero. There are finitely many exceptional v=a_T. On each open subinterval avoiding them, the derivative of E(v)-mu*v^2/2 is nondecreasing by (3). That derivative is continuous across every exceptional v, so it is nondecreasing on the entire interval. Hence E(v)-mu*v^2/2 is convex there. This proves the midpoint inequality without canceling a zero coefficient or invoking an unjustified twice-differentiable extension. It also covers d=0 and negative mu.

The exact midpoint consequence is

    E(3delta/2)-[E(delta)+E(2delta)]/2
       <=-mu*delta^2/8=-delta*d/4+3delta/(4ln2).

Combining with (1) proves, for EVERY such seed and every d>=0,

    DeltaH <=delta*(d/4+3/2+3/(4ln2))
           =R/2+kappa*e, kappa=5/2+3/(2ln2)<19/4.          (4)

The strict rational bound follows from ln2>2/3, e.g. the positive atanh series at1/3. This proof uses the two spectral moments, not flatness, a nonvanishing hypothesis, support granularity or a minimum Fourier coefficient. Booleanity is additionally used in the physical influence calculations below.

## 3. Sharpness within the same mechanism

For d=2m and the quadratic bent seed, let s=2^-m, so all a_T=+/-s. On the entire v interval, v/s<=2s<=1/2 for m>=2. Since |ln|1+u||<=2|u| for |u|<=1/2, the difference between E''/N and 2d-6/ln2 has absolute value <=16s/ln2. Applying the same nonnegative midpoint kernel, whose total mass is delta^2/8, gives

    kappa-4s/ln2 <=(DeltaH-R/2)/e<=kappa.                  (5)

Thus the additive constant in (4) is sharp for the coefficient R/2. A coefficient strictly below1/2 in front of R cannot work with any fixed e-charge: the stage7 lower bound gives DeltaH/e>=d/2+3 while R/e=d+1. This is sharpness of a specified local charge, not a lower bound on the full FEI constant or a failure of selecting another query.

The preceding bent-only claim remains a corollary. For d=2m,m>=2, (5) implies DeltaH/e>=m+3; (4) implies its old upper bound3m+3. Maximum entropy on the N empty-control atoms gives H(F_0)<=2m+delta*(2m+1/ln2) and H(F_1)<=2m. With actual-spectrum references Q_s=p_s (not arbitrary references), the exact influences below give the same rate-four bank B=4Ibar-E H(F_s)>=2m. At tau=0 it satisfies (7), and the earlier residual bound B-R-L>=(59m+1)/32 remains valid: the new bound gives(244m-5)/128, exceeding the old(236m+4)/128 for m>=2. Thus this is version2 of the same one-query statement, extending its profile and admission mechanism rather than opening another broad FEI candidate. The former bent-specific negative empty boundary remains specific to that subfamily; section6 does not assert it for general seeds.

## 4. Actual influence and one original source with old debits

Let t be the number of neighbors of0 on which b=-1. Counting the physical edges incident to the marked point gives

    I(F_0)=I(b)+delta*(d-2t)+delta,
    I(F_1)=I(b)+2delta*(d-2t),
    Ibar=E I(F_j)=I(b)+(3/2)delta*(d-2t)+delta/2,
    I(F)=Ibar+e.

The t originally pivotal edges alone contribute2delta*t to I(b). Therefore

    Ibar >=delta*(3d/2-t+1/2)>=delta*(d+1)/2=R.             (6)

Destroyed original edges are included in these equalities; no net-influence positivity is assumed. Equality in (6) is possible for the positive point seed, so it is not a strict-margin assertion.

Now fix ANY two normalized complete terminal references Q_0,Q_1 with finite cross-entropies CE_s=sum p_s log2(1/Q_s). Reference atoms with zero actual mass contribute zero; every positive actual atom must have positive Q_s. Keep both whole CE_s, and hence their full KL costs, unchanged. Let A be a FIXED supplied original source quota and tau>=0 an already-booked old debit against that quota. Any off-path cost is already permanently withheld. Neither A nor Q_s is renewed from descendant influence. Define the SAME unused source

    U=A-E CE_s-tau.

This is an eligibility condition on an existing original account, not a new source certificate. No Q_s is replaced and no fresh root or descendant canonical reference is manufactured. Suppose

    U >=(3/2)R-e/4.                                      (7)

Book R once from U. The actual additional debit is L=max(DeltaH-4e-D_R,0)=max(DeltaH-5e,0). By (4),

    L <=R/2-e/4, U-R-L>=0.                               (8)

The right side is nonnegative because R=(d+1)e>=e. The complete data debit is paid by the disjoint owners4e, D_R=e and L from U-R. The SAME leftover reserve is R-e and the same unspent source is U-R-L. In particular the whole ledger, including both terminal references, the OLD debit and all remaining reserve, obeys

    DeltaH+E CE_s+tau+(R-e)+(U-R-L)
       <=4e+A.                                          (9)

Thus (7) is a uniform arbitrary-seed one-query admission test with both full terminal costs and arbitrary previous debit explicitly present. If the ORIGINAL quota additionally satisfies A<=K Ibar at K>=4, then (9)<=K I(F); that comparison is an extra supplied certificate, not automatic inheritance. For a source originally fixed at A=K Ibar and E CE_s<=C0 Ibar, U>=(K-C0)Ibar-tau; by (6), the stronger condition (K-C0)Ibar-tau>=(3/2)Ibar-e/4 suffices. This is a ONE-STEP source-margin statement, not a recursively renewed increase of K.

For fixed physical rate4 and the mandated booking of the same R, the leading admission coefficient3/2 cannot be improved uniformly using only these owners: (5) makes R+L asymptotic to(3/2)R as d grows. Extra legitimate source credits or a different selected query are not ruled out.

## 5. Admission is not automatic

Take b identically+1. Then F_0 and F_1 are ordinary point defects on d+1 and d bits. For a point defect on n bits, p=2^-n, I_n=2np and its nonconstant Fourier mass is4p(1-p). Discarding only the nonnegative empty-atom entropy gives

    4I_n-H_n <=8p+8(n-1)p^2<=12p,

using (n-1)2^-n<=1/2. With exact actual-spectrum references, the source bank at rate4 is at most9delta. But R=(d+1)delta/2>9delta for d>=18. The source cannot even book R there, before any old debit. These are genuine Boolean functions satisfying their known point-defect FEI bounds; the failure concerns admission (7), not FEI. This guard prevents promoting (4), (6) or root influence capacity into unused source surplus. Initial cheap references for arbitrary seeds are still absent.

## 6. Noise semigroup, endpoints and signed boundary

For each finite actual g, L chi_S=|S|chi_S, q_t(S)=hat g(S)^2 exp(-2t|S|) is unnormalized. Define J_g(t)=sum_(S nonempty)|S|q_t(S)ln(1/hat g(S)^2), K(g)=integral J_g, and b0(g)=p_empty ln(1/p_empty). Then J_g(t)<=J_g(0) near zero and J_g(t)<=e^(-2t)J_g(0) at infinity. Both endpoints are integrable, and finite termwise integration gives2K=ln2 H-b0. Differentiating raw entropy minus2t sum |S|q_t gives-2J. The correction and the boundary are required. Since b0<=Var<=I, an all-dimensional bound2K<=A I would imply FEI at(A+1)/ln2; it remains unproved.

For the SAME DATA query,2DeltaK=ln2 DeltaH-Delta b0. Equation(4) yields

    2DeltaK <=ln2*(R/2+kappa e)-Delta b0.                 (10)

For arbitrary seeds the boundary can have EITHER sign; the negative bent boundary from stage7 is not inherited universally. The checker independently computes the nonempty-spectrum area and retains the signed boundary. No uniform absolute-boundary influence payment or universal integrable time envelope is inferred.

## 7. Rung and first unsupported line

Rung: analytic author proof with exact finite checks, pending independent review. The optional core Lean submission addresses only the cleared-denominator budget implication after the analytic profile bound. No formalization of Jensen/zero-crossing curvature or the complete entropy theorem is claimed without a verified receipt.

FIRST UNSUPPORTED UNIVERSAL LINE: ensure (7), or a different selected continuation payment, from a genuinely UNUSED inherited original source on arbitrary data queries after all prior debits. The wrapped arbitrary-seed profile removes the flatness restriction, but does not supply a cheap seed/terminal reference, preserve bank eligibility indefinitely, or price a fresh-reference reset. Its prescribed two-control attachment is not every arbitrary-core data split. These missing statements cannot be replaced by (6), because influence capacity is not unused surplus.
