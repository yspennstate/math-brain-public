# Packed sparse spectra: exact point-surgery orientation and a uniform criticality exclusion

Uniform finite cubes, Boolean signs, entropy in bits. Let F on n>=3 named coordinates have Fourier support distance>=3. A singleton support has distance infinity. Let G=F-2F(v)1_v, N=2^n, p=N^-1, e=2p. Put s=|supp hat(F)| and d_v=the number of pivotal physical edges incident to v in F. O_i=Inf_i-beta_i; beta_i is the singleton spectral minority mass. Pair refunds are A052's actual nonnegative merging variances and R_sum is their total over all unordered pairs. T=sum_i O_i+R_sum.

## 1. Packing and Boolean parity eliminate a coefficient-floor hypothesis

The radius-one Hamming balls about the support indices are disjoint, so

    s(n+1)<=N.                                                (1)

In particular the spectrum has a zero coefficient. For n>=2 every integer Walsh sum is congruent modulo4 to minus twice the number of negative truth values, independently of its spectral index. A zero Walsh sum therefore forces even negative count. All seed Walsh sums are multiples of4, and every nonzero seed Fourier coefficient has magnitude at least4p=2e. The edit changes every integer Walsh sum by plus/minus2, giving full Fourier support and odd negative count. These conclusions use Booleanity as well as support geometry.

Every singleton row contains at most one seed coefficient. After editing its formerly empty partner has magnitude e. The previously occupied coefficient has magnitude at least e; a formerly zero row has both magnitudes e. Thus every row contributes exactly e^2 to its weighted minority mass, giving the NEW exact identities

    beta_i(G)=2p for every i,
    O_i(G)=Inf_i(F)+2p[F(v)F(v^i)-1],
    sum_i O_i(G)=I(F)-4p d_v,
    T(G)=I(G)-2np+R_sum.                                    (2)

The influence identity is the physical incident-edge formula Inf_i(G)-Inf_i(F)=2pF(v)F(v^i). By the earlier elementary row Cauchy--Schwarz estimate, which follows by inserting the edited empty amplitude e, C_i(G)<=8p and each pair refund sum<=16p. Consequently

    |T(G)-I(F)|<=4np+16 binom(n,2)p,
    Theta(G)=1+[R_sum-2np]/I(G).                            (3)

This replaces the O(n sqrt(p)) orientation estimate by an exact incident-edge ledger and O(n^2 p) total error on this support class. It does not discard orientation when refunds vanish.

## 2. Packed row weights give prices independent of dimension

Fix i. Exactly s singleton rows were occupied before the edit. Each of the N/2-s formerly empty rows has edited mass2e^2, minority fraction1/2, B-row1 bit and J-row1 bit. Their total mass is

    W=4p-8s p^2,  b=s e^2=4s p^2<=b_0:=4p/(n+1).          (4)

Here b is the total off-anchor/minority mass in the occupied rows. Write Q=1-W for their total mass. Concavity gives their entropy at most Q h2(b/Q)<=b log2(1/b)+b/ln2. Their channel is at most(2/ln2)b. Hence, with L_i=B_i+J_i,

The channel estimate can be proved and re-centered separately on each row: for physical row(a+b,a-b), the two-point inequality Ent(w^2)<=(w_0-w_1)^2/2 gives natural-log information<=2b^2. Multiplying the row by the queried character exchanges a,b and preserves its square, yielding2min(a^2,b^2). To prove that two-point inequality, replace physical values by their absolute values, normalize their mean square to1, and compare entropy of1+u,1-u with1-sqrt(1-u^2). The difference has derivative u/sqrt(1-u^2)-atanh(u)>=0, because its derivative is(1-u^2)^(-3/2)-(1-u^2)^(-1)>=0. Scaling and division by ln2 give the asserted bound; zero values follow by continuity.

    L_i(G)<=2W+b[log2(1/b)+3/ln2]
           <=8p+b_0[n+log2(n+1)-2+3/ln2]
           <16p.                                           (5)

The function b[log2(1/b)+3/ln2] increases on(0,1], justifying b<=b_0. For the last rational constant, ln2>2/3 and log2(n+1)<=(n+1)/2 for integers n>=3. The latter has equality at n=3 and its induction step follows from(5/4)^2<2. These yield an upper bound15.5p, strictly below16p. When b=0 the entropy term is0 by continuity.

For the collision upper certificate V_i=B_i+Gamma_i, the occupied collision is at most4b and Gamma<=C/ln2. The analogous bound gives

    V_i(G)<19p.                                             (6)

For a queried pair, the N/4-s formerly zero rows each have mass4e^2 and uniform four-atom squared Fourier law. Their physical row is a one-assignment spike; both B and Gamma are2 bits. Their total mass is W2=4p-16s p^2. In occupied rows, the off-anchor mass is epsilon=3s e^2<=12p/(n+1); their collision is at most(16/3)epsilon. Thus

    V_pair(G)<=4W2+epsilon[log2(1/epsilon)+log2 3+19/(3ln2)]
              <54p.                                        (7)

To verify the last constant, the bracket is increasing after multiplication by epsilon on the needed interval. Substitute epsilon_0=12p/(n+1), collect log2 3-log2 12=-2, use ln2>2/3 and log2(n+1)<=(n+1)/2. The resulting coefficient is below16+18+78/(n+1)<=53.5. These bounds improve the earlier n-dependent surgery prices by exploiting the actual masses of occupied and newly created rows. They apply to any seed support of distance3, including coded reductions of arbitrary cores; no lower bound on individual influences is assumed.

## 3. A uniform paid singleton and criticality exclusion at every K>=8

If F is nonconstant, the two indicators(1+F)/2 and(1-F)/2 have Fourier support of size at most s+1. At a point where either indicator is1, Fourier inversion and Cauchy--Schwarz imply1<=sqrt(s+1)*sqrt(its expectation). Therefore each physical sign class has probability at least

    1/(s+1)>=(n+1)/(N+n+1).                                (8)

For n>=4, N>=3(n+1); flipping one point leaves both sign classes of G with probability at least

    a_n=(3n-1)p/4.

a_n decreases for n>=4 and a_4=11/64. If alpha is the minority physical probability of G, alpha>=a_n and alpha<=1/2. Parseval gives the elementary Boolean Poincare inequality I(G)>=Var(G)=4alpha(1-alpha), since every nonempty Fourier set has size>=1. Thus

    I(G)>=4a_n(1-a_n)>=(53/64)(3n-1)p>2np.                 (9)

The last strict inequality is31n>53, true for n>=4.

Suppose G were a least-essential-dimension FEI(K) violation, K>=8, on this same essential cube. Define actual S_i=-E D_K(G restricted at i)>=0 and D=D_K(G)>0. Its singleton telescope and(5) imply

    K Inf_i(G)+D+S_i=L_i(G)<16p.

Summing over ALL i keeps every reserve:

    K I(G)+nD+sum_i S_i<16np,

contradicting(9) and K>=8. No minimum coordinate influence or dimension-dependent deficit floor enters. The edited function has full support, so its named dimension is its essential dimension.

The remaining cases require no high-threshold premise. At n=3, packing gives s<=2; a Boolean function with exactly two Fourier coefficients is impossible, since the nonconstant Fourier coefficient of its square would be2ab!=0. Thus F is a signed character. The edited spectrum has one mass(1-2p)^2 and all others4p^2. With k the character degree, direct averaging gives I(G)=k(1-4p)+2np>=3/4, while H(G)<=3, so R(G)<=4. If F is constant at any n>=3, the same point-defect spectrum has I=2np and H<8np: the dominant atom entropy is at most4p(1-p)/ln2<6p(1-p), while all minor atoms contribute8p(1-p)(n-1). Hence R(G)<4. These sources cannot violate K>=8.

All cases give I(G)>=2np. Choose a coordinate i of maximum influence; then Inf_i(G)>=I(G)/n>=2p. Equations(5),(6) give the NEW uniform selected-coordinate bounds

    L_i(G)<8 Inf_i(G), V_i(G)<(19/2) Inf_i(G).              (10)

They require neither criticality nor a healthy coordinate. For any fixed K>=8 this singleton has D_K(G)+S_i=L_i-KInf_i<0. If the root violates K, its average physical-child deficit is strictly greater than its root deficit. In particular a violating smaller-dimensional child is actually retained, and even the weaker condition that every immediate singleton child is K-certified is impossible. The queried class need not remain distance3 after restricting this coordinate; the terminal obligation is not erased.

Conclusion: NO least-essential-dimension FEI(K) violation for ANY K>=8 is a one-point edit of a Boolean function with Fourier support distance>=3. This is a uniform paid-root/critical-source exclusion, not FEI(8) for the entire edited class: arbitrary high-ratio coded roots can still violate8 and then their physical child reserve must fail eligibility. In particular a maximum-influence singleton transports strictly more than the positive root deficit to its actual children.

## 4. Scope and remaining bridge

A052's exact Gibbs banks remain valid and explicitly distinguish the tiny row minority weights from a reusable child bank. The proof above supplies a strict contradiction on a structural neighborhood even when all physical influences are weak, closing the loophole in A053's former healthy-influence-only exclusion. It does not classify every hypothetical critical witness. The first unsupported line is a paid relative block-selection rule for sources whose Fourier support is not within this one-point neighborhood, especially multiple nearby-index fibers with uncontrolled signed phase/refund cost. The next physical query can reduce code distance3 to2; paying that distance-two retained-row interface with actual child deficits is the next step. Absolute smallness and qualitative full support remain insufficient.
