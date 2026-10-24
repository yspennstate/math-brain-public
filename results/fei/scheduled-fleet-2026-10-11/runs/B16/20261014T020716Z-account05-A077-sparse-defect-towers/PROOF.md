# Common activation does not repair a rare private collision

All bits are independent uniform bits in {0,1}; signs are Walsh characters. All logarithms and entropy are bits. This is a local-payment obstruction, not an FEI counterexample.

## 1. Actual branches and full physical ledger

For even k>=2, r>=1, N=2^k, a=1/N, b=2^(-k/2), q=2^-r, define

    G(s,x)=1-2*1{s=0,x=0},
    H(s)=(-1)^(s1*s2+...+s(k-1)*sk),
    A(t)=1{t=0},
    G'=1+A(G-1), H'=1+A(H-1),
    W=G' if z=0, H' if z=1.

Equivalently W=1+A(F-1), where F selects G/H. These are truth formulas, not hypothetical spectra. Put c=(1-b+a)/2. Direct pivotal counting gives

    E G'=1-qa, E H'=1-q(1-b), E W=1-qc,
    Inf_x(W)=qa/2,
    Inf_sj(W)=q(a+1/2)/2,
    Inf_z(W)=qc,
    Inf_tj(W)=qc,
    I(W)=q[k/4+(k+1)a/2+(r+1)c].                  (1)

All influences are at most q. Taking r=k even to infinity makes both branches overwhelmingly +1, every coordinate influence tend to zero, and total I(W) tend to zero. G' is itself a point defect on k+r+1 bits. H' has relevant s influence q/2 and relevant t influence q(1-b); hence no fixed hereditary derivative gap is available at its root. Activation does not create free controls.

## 2. Exact retained common-frequency rows

Write phi(p)=p log2(1/p), Phi(p,d)=phi(p)+phi(d)-phi(p+d), and

    S(u,d;v)=[Phi((u+v)^2,d^2)+Phi((u-v)^2,d^2)]/4
               -Phi(u^2,d^2)/2.

The physical private query x has exact signed correction

    D=B_x(W)-B_x(G')/2
     =q(N-1)S(-a,a;b)+q(1-q)S(-a,a;b-1)
       +S(1-qa,qa;1-q+qb).                         (2)

Indeed G' half-difference coefficients all have magnitude qa. Its mean-profile coefficient is 1-qa at the empty common row and -qa elsewhere. H' has coefficients qb times a sign on each nonempty s frequency and each of the 2^r gate frequencies; empty s and nonempty t has q(b-1), and the fully empty row is 1-q+qb. S is even in each amplitude, and homogeneous of degree two. Summing all (N-1)2^r nonempty-s rows, all 2^r-1 remaining control rows and the fully empty row proves (2). Nothing is omitted or assumed additive across overlapping spectra.

## 3. Uniform-in-r divergence, even though both branches are rare

For p,d>0, Phi(p,d)>=d log2(p/d). Applying this to the two shifted nonempty-s amplitudes, whose product is (b^2-a^2)^2, gives

    S(-a,a;b)>=(a^2/2)log2(N-1)-a^2.

Every S has lower bound -Phi(u^2,d^2)/2. Thus S(-a,a;b-1)>=-a^2. For d=qa<=1/2 and p=(1-d)^2,

    Phi(p,d^2)<=d^2 log2((p+d^2)/d^2)+d^2/ln2
                <=d^2[2(k+r)+3/2].

Here p+d^2<=1, ln(1+t)<=t, and 1/ln2<3/2. The fully empty row is at least -(qa)^2(k+r+3/4). Consequently, for even k>=4,

    D/Inf_x(W)>=(1-a)log2(N-1)-2(1-a)
                    -2a(1-q)-2qa(k+r+3/4)
                >=k-3-a(k-1)-2qa(k+r-1/4)
                >=k-3-2ka >=k-4.                  (3)

The last estimate uses q<=1/2, rq<=1/2 for every integer r>=1, and 2k/2^k<=1 for k>=4. The latter follows at k=4 and decreases thereafter. This is an all-parameter proof. No finite extrapolation is used.

If Q_x=sum min(u_T^2,d_T^2)log2((u_T^2+d_T^2)/min), then

    0<=B_x-Q_x<=sum min(u_T^2,d_T^2)/ln2
                      <=Inf_x(W)/ln2.

For each row the first difference equals max(p,d)log2(1+min/max), which is <=min/ln2. Since inherited B_x(G')/2>=0, (3) implies Q_x/Inf_x(W)>=k-11/2. Thus minority bias, small total influence, and small influences at every root coordinate do not repair a prescribed rare-private-query price. This does not refute selection of another physical coordinate.

## 4. Activation controls give an exclusive paid escape

For ANY Boolean core f, let V=1+A_l(f-1), p=2^-l, c_f=1-E f, and j=p c_f=Inf_t(V). At a gate-coordinate query, direct Fourier counting gives

    B_t(V)=Phi((1-j)^2,j^2)+2j(1-j) <=4j.           (4)

The derivative's squared norm is j; its empty coefficient is -j. At every nonempty residual frequency the mean and derivative amplitudes agree up to sign, so the erasure is twice their squared derivative amplitude. The elementary envelope Phi(u^2,v^2)<=2|uv| gives (4). This remains valid for 0<=j<=1, including zero boundaries.

Query t1,...,tr first, stop immediately if a queried gate bit is one. At depth d on the sole live gate history the reach probability is 2^-d, the residual activation probability is 2^-(r-d), and j=2^-(r-d)c. Each gate depth therefore consumes exactly qc of the physical influence. The gate prefix consumes rq c, has B bill <=4rq c, and leaves the full actual F with probability q (constants elsewhere):

    E I(leaf)=q I(F),
    E H(leaf)=q H(F)
       =q[H(G)+H(H)]/2+q R(G,H).                  (5)

These are retained terminal costs, not free leaf certificates. The two branch gate bills are rqa and rq(1-b), whose half-sum is rq c. They are the same physical account in (1), not extra reserves.

Consume A076's scoped data-only policy for the surviving A078 base core: query H-relevant coordinates until the quadratic branch is constant, then G-relevant coordinates. Quadratic relevant influences are >=1/2 hereditarily, giving B_i(F)<=4Inf_i(F). In the constant-H suffix the shifted-row comparison gives B_i(F)<=B_i(G)/2+Inf_i(G). For a point defect with delta=2^(1-m), B_i(G)=Phi((1-delta)^2,delta^2)+2delta(1-delta)<=3delta (m>=2), and m=1 has B=0. Hence suffix B_i(F)<=5Inf_i(F). The point bound follows from Phi<=delta^2 log2(e/delta^2): for m=2,3 use log2(e)<2; for m>=4 use 2(m-1)/2^(m-1)<=3/4. Every terminal wrapper is constant or a character in z and has entropy zero. This independently reconstructs A076 OWNED_PIVOT_PROOF equations (8)-(9), without its checker.

The combined complete physical policy therefore has

    B_tree(W)<=4rq c+5q I(F)<=5 I(W),
    Q_tree(W)<=B_tree(W).                          (6)

The universal scalar JS bound JS_i<=2Inf_i/ln2, reconstructed in our previous proof by differentiation of
[(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2),
then yields H(W)<8 I(W). Both active terminal core costs in (5) are paid by the subsequent policy, using only q I(F); gate influence is never reused. This is weaker than some class entropy bounds and is stated solely to certify that the new family is not an FEI counterexample.

## 5. Review and exact frontier

A078 v2 PROOF Sections 1-2, equations (1),(3),(4), are independently reconstructed by the actual constructor and row formulas; HOLDS at those locators. Earlier quarter-profile/transport clauses of the bundled claim are not independently accepted here. A076 v4 OWNED_PIVOT_PROOF Sections 1-5 equations (1)-(9) have been reconstructed at their stated derivative-gap scope; HOLDS without repair, with finite tests focused on the quadratic/point-defect fixture. Earlier bundled material is excluded from this review.

The new rare/rare extension refutes only a uniform local correction or Q payment at a prescribed private coordinate, even conditioned on both minority probabilities and all root influences tending to zero. The shortest open line is a paid adaptive gate/pivot selection or one exclusive terminal-slack debit for two genuinely interacting rare branches without an exposed common activation factor. Activation-first is not an algorithmic discovery theorem for arbitrary Boolean functions. No universal C018/C019 constant follows.
