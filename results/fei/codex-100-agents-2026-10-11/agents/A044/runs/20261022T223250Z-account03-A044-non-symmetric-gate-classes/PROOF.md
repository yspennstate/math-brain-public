# Finite all-profile reserve truncation has exponential error

The singleton hierarchy of A043 does not extend with a dimension-independent deficit error to all integer mixed profiles. The obstruction is an actual Boolean product of two-bit bent gates. Its entropy is exactly twice its influence. Thus this is an obstruction to a proposed approximation mechanism, not to FEI.

All logarithms are natural unless marked as bits. Inputs in this theorem are fair and physically distinct. For each integer r>=1 put n=2r and

    f_r(x)=(-1)^(sum_{j=1}^r x_(2j-1)x_(2j)),  x in {0,1}^(2r).

Each two-bit factor has four Walsh coefficients of magnitude 1/2. Disjoint tensorization therefore gives P(S)=4^(-r) for every S, including the empty set. In particular

    H_bits(f_r)=2r, I(f_r)=r, Var(f_r)=1-4^(-r),
    Delta_r=r-1+4^(-r)>0.

This calculation is exact at every r; the family is a read-once product of explicit two-bit gates.

For nonempty S of size k define the actual physical integer profile

    Z_S=(1/2) sum_{b in {0,1}^S} (-1)^(k-|b|) f_r(b,x_notS),
    a_k=4^(1-k), t_k=|E Z_S|=2^(k-1-r).

The previous A044 scaling, independently reconstructed by A042, gives

    E Z_S^2=2^(k-2),
    Var(Z_S)=2^(k-2)-t_k^2,
    E_S=(k-1)ln(4) P(S)+a_k h(t_k),
    h(t)=t^2 ln(1/t^2).

The second-moment formula follows directly by summing the 2^(2r-k) identical Fourier masses over supersets of S, then multiplying by 4^(k-1). No independent ownership fragments are assumed. In particular every profile mean is nonzero. A refund triggered only by an exactly zero mean does nothing on this family.

For 0<=t<=1 let

    phi(t)=2t(1-t)-h(t),
    phi_m(t)=t(1-t) sum_{j=1}^m 2(1-t)^j/[j(j+1)], m>=0.

The positive coefficient series from A043 gives phi_m<=phi and

    phi(t)-phi_m(t)
      =t(1-t) sum_{j>m} 2(1-t)^j/[j(j+1)].             (1)

For any integer profile with t=|E Z|<=1 the exact local reserve is

    2 Var(Z)-h(t)=2(E Z^2-t)+phi(t).

Thus replacing phi by phi_m in every such profile increases the resulting entropy upper ledger by EXACTLY

    D_(r,m)=sum_{k=1}^r binom(2r,k)4^(1-k)
                         [phi(t_k)-phi_m(t_k)].        (2)

The degree k=r+1 has t=1 and zero error. At k>r+1, keep the exact negative h(t) instead of approximating it. This is the favorable version of the attempted extension: its failure cannot be blamed on discarding those negative refunds. Formula (2) is an approximation error, not the actual entropy or a required code length.

## A quantitative all-dimensional obstruction

For k<=r, 0<t_k<=1/2. Keeping the first omitted term of (1) gives

    phi(t_k)-phi_m(t_k)
      >= 2t_k(1-t_k)^(m+2)/[(m+1)(m+2)]
      >= 2^(-m-1)t_k/[(m+1)(m+2)].

Since 4^(1-k)t_k=2^(1-k-r),

    D_(r,m)>=2^(-m-r)/[(m+1)(m+2)]
                         sum_{k=1}^r binom(2r,k)2^(-k).

Pairing k and 2r-k shows that the sum from k=0 through r is at least half the complete binomial sum: the smaller index has the larger weight. Removing k=0 therefore proves

    D_(r,m)>= [2^(-m-1)/((m+1)(m+2))](9/8)^r
                   -2^(-m-r)/((m+1)(m+2)).           (3)

For every fixed finite m, D_(r,m)/Delta_r tends to infinity, because Delta_r<=r and an exponential of base 9/8 exceeds every linear function. All biases are interior, all profiles come from the same Boolean f_r, and none has zero mean. Consequently there is NO finite K_m such that the all-profile truncation error is <=K_m Delta for every dimension. This does not challenge A043's singleton error <=4Delta/(m+1), whose sum has only singleton profiles.

For completeness the exact fixed-order rate is

    D_(r,m) ~ [4/(m+1)](9/8)^r as r->infinity.          (3a)

To see this without an unjustified limit exchange, let K have distribution Bin(2r,1/3) and put F_m(t)=(1-t)sum_{j>m}2(1-t)^j/[j(j+1)]. Dividing (2) by 2(9/8)^r gives exactly E[1_(1<=K<=r) F_m(2^(K-1-r))]. The positive summable coefficient tail shows that 0<=F_m<=2/(m+1) and F_m(t)->2/(m+1) as t->0. Also Var(K)=4r/9, so Chebyshev gives Pr(K>5r/6)<=16/r. The event K=0 has probability (4/9)^r. On 1<=K<=5r/6 the argument is at most 2^(-r/6-1), which tends uniformly to zero. The bounded expectation on the complementary event tends to zero, proving (3a) by a finite event split.

## A growing-order lower bound

There is also a useful quantitative obstruction when m is allowed to grow. Suppose r is a positive multiple of four, M=m+1, and M<=2^(r/4-1). Restrict (2) to k<=3r/4. Then t_k<=2^(-r/4-1), so 2M t_k<=1/2. For M<=j<=2M-1, Bernoulli's inequality gives (1-t_k)^j>=1-jt_k>=1/2. The coefficient sum over that band telescopes to 1/M. Consequently

    phi(t_k)-phi_m(t_k)>=t_k/(4M).

For K distributed as Bin(2r,1/3), E K=2r/3. Markov's inequality gives Pr(K<=3r/4)>=1/9 (using the weaker threshold bound suffices). Hence

    sum_{k=1}^{3r/4} binom(2r,k)2^(-k)
      >=(1/9)(9/4)^r-1.

Substitution yields

    D_(r,m)>= [(9/8)^r/18-2^(-r-1)]/(m+1).            (4)

The right side is positive for these r. Within the displayed range, any asserted D_(r,m)<=K Delta_r forces

    m+1 >= [(9/8)^r/18-2^(-r-1)]/(K r).

Thus an all-profile polynomial truncation needs rapidly increasing order even on this simple tensor family. No assertion is made about the best adaptive or joint reference.

## A complete reference calibration

The single reference Q_r(S)=4^(-r) on ALL subsets is normalized, equals P, and has ordinary KL(P||Q_r)=0. Its complete base-two cross-entropy is 2r=2I(f_r), including the empty coefficient. Thus the family has a fully paid whole-set reference with no omitted terminal entropy. The exponential D_(r,m) is wholly an artifact of summing local approximation errors. Any bent Boolean function on 2r fair coordinates has the same squared Fourier law and therefore the same obstruction and reference calibration; the displayed tensor family supplies explicit realizability in every even dimension.

## Exact first unsupported line

The unsupported extension was: because every local reserve has a convergent positive hierarchy and the singleton tail is O(Delta/(m+1)), the same finite order controls the sum over all mixed profiles by O(Delta). Equations (3)-(4) refute that implication. Exact zero-profile refunds do not repair it; this example has full spectral support. Exclusive splitting is independently excluded by A045's inherited-integer-profile admission obstruction. The remaining viable target is a merged or conditional whole-set reference that sums and cancels before local approximation, includes the ordinary KL and normalizer, and pays both terminal laws from the same unspent degree-weighted source. Existence of such a reference remains unproved.

This is an author derivation pending independent review. Exact finite checks validate the physical formulas, scalar identities, bounds (3)-(4), small and boundary cases, and actual H/I. A requested Lean check is limited to a rational scalar tail coefficient identity; it does not certify this complete analytic proof.
