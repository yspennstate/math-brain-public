# Parity coding after genuine point activation

All cubes are physical uniform cubes, all signs Boolean, all entropies in bits. Write q_g(v)=P[g(y)!=g(y+v)], including q_g(0)=0. M is the minimum total influence over all full-rank affine parity codes and output-character modulations. The earlier A078 basis theorem reconstructs M(g) as the minimum basis sum of min(q_g(v),1-q_g(v)); redundant columns cannot improve it. Its independent whole-proof review remains pending. The argument below reconstructs the needed basis reduction directly.

## 1. The activation changes the coding metric

Let g have m bits, mu=Eg>=0, c=1-mu, r>=1, p=2^-r, and V(y,t)=1+1{t=0}(g(y)-1). This is an actual Boolean truth formula. A direction (v,0) has disagreement p q_g(v). A direction (v,u) with u!=0 moves between disjoint active control vertices. The two active endpoints give disagreement p(1-mu)=pc, independently of v and u. Both costs are <=1/2; thus output-character modulation cannot reduce any of them. Input translation also preserves them.

For a full-rank code with columns w_j and output character bits epsilon_j, each physical influence is q_V(w_j) if epsilon_j=0, and 1-q_V(w_j) otherwise. Its Fourier coefficients are injectively relabelled (and possibly signed), so entropy is exactly preserved. Any column basis has no more influence than the entire code. Therefore the optimum is an actual invertible code and is the minimum directional basis sum.

Define T_c(g)=min_{basis v_1,...,v_m} sum_j min(q_g(v_j),c), using UNFOLDED seed disagreements. Then exactly

    M(V)=p[T_c(g)+r c].                                      (1)

Proof: for a cost threshold h<c, the span of available directions is the core span of {v:q_g(v)<=h}; for h>=c, all directions with nonzero controls are available and span the whole m+r space. The minimum-basis rank integral is consequently p[r c+integral_0^c(m-rank{q_g<=h})dh]. Greedy basis selection on capped seed costs identifies the integral with T_c. Equivalently, take a minimum capped core basis, replace every column of seed cost>c by that column plus the first control unit, and include all r control units. These are independent and realize (1). This explicitly supplies a Boolean coding construction, not a proposed spectral law.

The folded metric M(g) cannot be substituted for T_c. For g(y)=(-1)^y, mu=0, M(g)=0 (an output modulation makes it constant), but T_1(g)=1 and M(V)=p(r+1). Dropping that extra p is a false auxiliary influence calculation. The activation's entropy is retained, so no contradiction with the constant seed's zero entropy occurs.

## 2. Exact minimum for the shared bent/spike family

For even k>=2, s in F_2^k, private x and selector z, define G=1-2*1{s=0,x=0}, h(s)=(-1)^Q(s), Q(s)=sum_j s_(2j-1)s_(2j), and F=G if z=0 else h. Put a=2^-k,b=2^(-k/2). A direction has labels (t,e,d) on (s,x,z). Its actual disagreement is

    d=0,t=0,e=1: a/2;
    d=0,t!=0: D=1/4+a/2;
    d=1: C_+=(1-b+a)/2 if Q(t)=0,
         C_-=(1-b-a)/2 if Q(t)=1.                    (2)

The zero direction has cost0. For d=0 this follows from the two shifted exceptional vertices of G and the balanced nonzero derivative of the nonsingular quadratic h. For d=1 both cross correlations equal b-a h(t): averaging the two selector states does not erase either core. All displayed costs are below1/2, so folding has no effect.

For k>=4, a/2<D<C_-<C_+. The first two strata span dimensions1 and k+1; adding any Q(t)=1 selector direction gives dimension k+2. Thus

    M(F)=a/2+kD+C_-=I(F)-a.                         (3)

For k=2, C_-=a/2=1/8; the only Q(t)=1 shared shift is t=(1,1), and the low-cost directions span exactly dimension2. At D=C_+=3/8 the span becomes dimension4. The minimum is2/8+6/8=1, again (3). A concrete optimum for every k is the original private/shared unit basis and selector column replaced by z+s_1+s_2. It saves exactly a physical influence, preserving every Fourier probability.

Mean EF=(1-a+b)/2, hence c=(1+a-b)/2=C_+. Every seed direction in (2) costs <=c, so T_c(F)=M(F). For every r>=1 point activation W=1+A_r(F-1),

    M(W)=p[M(F)+r C_+],
    I(W)=p[I(F)+r C_+],
    I(W)-M(W)=p a.                                  (4)

Consequently parity mixing of controls and data cannot hide the shared-core influence k/4 or the added r control costs. Arbitrary redundant parity columns and output modulations cannot improve (4).

## 3. Complete entropy bill and scalable closure

The prior complete spectrum bound is H(F)<=2(k+1)a+k/2+2. For k>=4 its gap below4M(F) is k/2-2b-2a>0. At k=2 all16 coefficients are nonzero and unequal, so H(F)<log2(16)=4=4M(F). Thus H(F)<4M(F) for every even k>=2.

For completeness reconstruct the constant-child point-control estimate, rather than incorrectly importing it from the earlier core-first transport lemma. At a split choosing 1 or an arbitrary residual g, let c=1-Eg in [0,2] and j=c/2. Nonempty Fourier rows contribute (1-(Eg)^2)/2=c-c^2/2 to erasure B. The empty row contributes Phi((1-c/2)^2,c^2/4). If c<=1, the squared row total is <=1, so

    B/j <=2+c log2(1/c)+c/(2 ln2)<=3.

Indeed max_{0<=c<=1} c[ln(1/c)+1/2]=e^(-1/2)<=2/3<=ln2 (e>=9/4 and ln2>=2/3). If c>=1, put d=2-c<=1; B is unchanged by swapping the empty-row entries and by negating the nonconstant child. Thus B<=3d/2<=3c/2=3j. The exact entropy split is Delta H=B+JS of the actual child spectral laws; the universal physical estimate JS<=2j/ln2<=3j follows from squared-amplitude Jensen-Shannon (the same elementary entropy telescope used in previous stages). Consequently Delta H<=6j. Query the point controls first: physical consumed control influence is rpc, actual terminal entropy is pH(g), and the constant inactive leaves have zero entropy. Therefore H(1+A_r(g-1))<=pH(g)+6rpc. No terminal entropy is dropped.

Applying this to F yields H(W)<4pM(F)+6rpC_+<=6M(W). Hence EVERY actual full-rank parity-coded/modulated W has H<6I. Unactivated F has H<4I under every such code. Independent tensor products of these factors retain a bound6 under arbitrary joint parity recoding by the earlier exact tensorization of M. These conclusions concern full entropy and full physical influence, not a selected local obstruction.

## 4. Universal frontier and ownership

Equation (1) is universal within nonnegative-mean point activations and closes their exact coding cost, but does not pay an arbitrary g's entropy. The first unsupported universal line is a dimension-independent H(1+A_r(g-1))<=C p[T_c(g)+r(1-Eg)] for arbitrary g. Nor does optimizing total influence create a spendable repeated-query selector reserve: the physical tree still owns both retained core spectra and each consumed coordinate once. A023's symmetric terminal refund and A076/A077's second-collision deficit remain open. This stage rules out a parity-code hiding mechanism on their actual stress family rather than falsely supplying that refund.
