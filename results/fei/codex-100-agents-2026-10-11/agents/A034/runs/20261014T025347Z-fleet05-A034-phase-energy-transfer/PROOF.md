# Signed odd-mask concentrated-row obstruction

All physical bits are independent uniform bits; Walsh transforms below are unnormalized integer transforms. Entropy uses bits. This is a necessary admission theorem, not an entropy-influence theorem or a hereditary class extension.

Let m>=1, P=2^m, and h:{0,1}^m->{-2,-1,1,2}. Let M={y:|h(y)|=1} have odd cardinality mu. Suppose the normalized squares of W_s=sum_y h(y)(-1)^(s dot y) form a coordinate product. Define t=sum_(y in M)(-1)^|y|. Every W_s is odd, since W_s=sum h mod2=mu mod2. Thus every spectral coordinate is active and no coefficient vanishes.

For each coordinate choose coprime positive integers a_i,b_i representing the ratio |W_(s xor e_i)|/|W_s| when s_i=0. Product squares imply that this ratio is independent of the other coordinates. Consequently |W_s|=c product_i a_i^(1-s_i)b_i^s_i. The rational c is an integer: the integer products on the right have gcd product_i gcd(a_i,b_i)=1, so the denominator of c must be1. Moreover c divides P h(y) for every y by inverse transformation. As M is nonempty and h=+/-1 there, c divides P. Every W is odd, hence c=1 and all a_i,b_i are odd.

Parseval gives product_i(a_i^2+b_i^2)=P(4P-3mu). Dividing by P gives

    product_i u_i = 4P-3mu,  u_i=(a_i^2+b_i^2)/2.

Let D=product_i a_i b_i and N count nonfair coordinates, equivalently a_i!=b_i. Fair primitive pairs are(1,1), whereas each nonfair odd pair has a_i b_i>=3. Therefore D>=3^N.

For U={1,...,m}, Fourier multiplication gives the exact signed identity

    sum_s W_s W_(s xor U) = P sum_y h(y)^2 (-1)^|y| = -3P t.

Each summand has absolute value D, because complementing every coordinate swaps the two primitive factors. Thus D divides3Pt. Since D is odd, D divides3t. In particular D<=3|t|. The number t is odd and nonzero. The two parity classes have P/2 points each, so |t|<=min(mu,P-mu).

For a,b>=1, (a^2-1)(b^2-1)>=0 proves (a^2+b^2)/2<=((ab)^2+1)/2. Also for d,e>=1, ((d^2+1)/2)((e^2+1)/2)<=(d^2 e^2+1)/2. Applying these inequalities to all primitive pairs yields

    4P-3mu <= (D^2+1)/2 <= (9t^2+1)/2,
    8P <= 9t^2+6mu+1 <= (3mu+1)^2,
    3^N <= D <= 3|t| <= 3 min(mu,P-mu).

In particular mu=1 forces P<=2: a concentrated row with one mixed physical point and at least two data bits cannot have product conditional spectrum, regardless of its Fourier signs. This closes a specific all-dimensional admission regime. Even-cardinality masks and allocation of the pure region among several rows are not covered. Adding dummy physical data bits makes mu even, so this theorem is not asserted to be restriction or tensor stable.

## Actual Boolean origin and exact phantom rejection

For two address bits X, h_J=2 E_X F chi_J has values0,+/-1,+/-2. At each physical Y point there is either one pure row of magnitude2 or four mixed rows of magnitude1 with product of signs-1. The theorem applies when one row owns the entire pure region and the shared mixed mask has odd size. Any h with the displayed value pattern can be completed to an actual two-address Boolean F: on M take rows(h,1,1,-h), and on M's complement take(h,0,0,0), then invert the address transform. The other three rows need not have product spectrum; no such assumption is concealed in the completion.

P=32, mu=1 is a useful norm-only phantom. Choose three primitive pairs(1,3) and two pairs(1,1). The32 candidate magnitudes are3^popcount(s&7). They have squared norm4000=P(4P-3), gcd1 and the correct odd parity. But D=27 does not divide3P=96. No choice of signs can realize the prescribed physical squared values. This rejects the magnitude law without enumerating2^32 phase assignments. It is not a Boolean counterexample to FEI.

## Shared-mask transfer without pure concentration

There is also an exact common-mask consequence which permits zeros and arbitrary division of the pure region. Let h_J take values0,+/-1,+/-2 with common odd-size M and disjoint pure supports E_J partitioning M's complement. Suppose every row has coordinate-product squared spectrum. The preceding oddness/gcd proof works separately for every row: c_J=1, all primitive pairs are odd, and the full spectral face is occupied. Put e_J=|E_J|, t_J=sum_(y in E_J)(-1)^|y|, D_J=product_i a_Ji b_Ji. Then

    product_i (a_Ji^2+b_Ji^2)/2 = mu+4e_J,
    D_J divides t+4t_J,
    gcd_J(D_J) divides3t.

The first identity is Parseval. The second follows from the same full-complement signed autocorrelation, now with h_J^2=indicator_M+4 indicator_EJ. The third follows by summing the four divisible integers, since sum_J t_J=-t. All primitive odd pairs have (a^2+b^2)/2=1 mod4, so mu=1 mod4 is necessary. That congruence is a norm-arithmetic consequence rather than the new phase constraint.

These are coupled necessary conditions in arbitrary data dimension, not a sufficient realization criterion or a bound on weighted N. In the concentrated row E=M's complement, t_J=-t and the stronger D divides3t estimate above follows. The next missing step is using the coupled four-row divisibility and actual phase compatibility to obtain weighted payment when no row owns the whole pure region, including even mixed masks.

## Full conditional ledger and guards

For actual F whose nonzero conditional row spectra are products, retain

    H(F)=H(w)+H(S_Y|S_X),
    H(S_Y|S_X)=sum_J w_J sum_i h2(q_Ji),
    I_Y=sum_J w_J sum_i q_Ji,
    H(S_Y|S_X)<=2 I_Y+Q, Q=sum_J w_J N_J.

Here h2(q)<=2q+1 suffices for a nonfair coordinate; fair and deterministic coordinates satisfy h2(q)<=2q. The theorem constrains N for an odd-mask concentrated row but does not prove Q<=K(H(w)+I_X). The first unsupported line remains that payment for arbitrary compatible row phases in every data dimension. Address entropy is retained and not paid by the present result.

The three-bit point defect has mu=1,P=2 and dominant h=(1,2) up to signs/translations. It is admitted, with primitive pair(1,3), N=1, w=(5,1,1,1)/8 and I_X=1/2. Its one-data-coordinate product condition is vacuous, as required by the lead's guard.

The normalized non-Boolean control psi_m=product_i(3+4y_i)/5, independent of addresses, has product squared spectrum with q_i=16/25, w_empty=1, Q=m and H(w)+I_X=0. Its all-plus physical value is(7/5)^m, so it is excluded by actual Booleanity. Its rows also violate the five-valued integer admission used above. The primitive-factor norm arithmetic alone is insufficient: the phantom passes its norm test but fails the signed identity. No arbitrary Boolean tensor factor or correlated physical input law is admitted by this argument.

## Scope of an address-dimension-independent weighted target

For r>=2 address bits and one data bit, take the actual(r+1)-bit point defect F=1-2 indicator_(X=0,Y=0), p=2^-r. Its Fourier coefficients are1-p at the empty set and-p elsewhere. The empty address row has mass w0=(1-p)^2+p^2 and a nonfair conditional marginal p^2/w0. Every other row has mass2p^2 and a fair data marginal. Thus Q=w0, I_X=rp, eta=1-w0=2p(1-p), and H(w)=h2(eta)+eta log2(2^r-1).

Since eta>=p, eta<=2p, and log2(e)<2, h2(eta)<=eta(log2(1/eta)+log2(e))<=2p(r+2). Hence H(w)+I_X<=(5r+4)p and Q/[H(w)+I_X]>=w0/[(5r+4)p] tends to infinity. This rules out an absolute weighted-payment constant when the number of address bits and X degree r are unbounded. It does not rule out a constant for fixed two addresses, or a degree-dependent constant, and does not disprove FEI.
