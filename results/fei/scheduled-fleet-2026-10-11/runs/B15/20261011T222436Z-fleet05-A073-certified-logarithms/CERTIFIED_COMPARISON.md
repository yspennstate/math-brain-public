# Exact logarithm comparison

All entropy units are bits. Let R be a rational linear combination of entropies of finite rational probability laws and rational constants. Replace each entropy by -sum_t t log2(t), omitting t=0, and replace a constant c by c log2(2). Factor every positive rational argument. This gives R=sum_p c_p log2(p), over finitely many primes p, with rational c_p. Choose a positive integer L clearing their denominators and define

    U = product_{L*c_p>0} p^(L*c_p),
    V = product_{L*c_p<0} p^(-L*c_p).

Then L*R=log2(U/V). The logarithm is strictly increasing, so sign(R)=sign(U-V), including equality. This is an exact finite integer comparison. Unique prime factorization also proves that R=0 exactly when all aggregated prime coefficients vanish. No transcendence assumption is needed. To compare R with a rational m/n, n>0, compare U^n and V^n*2^(L*m), moving the power of 2 to the other side if m<0. This last option can be expensive; our witnesses need only small dyadic comparisons.

For an independent rational enclosure, write x=2^k*t, 1<=t<2. Set y=(t-1)/(t+1), 0<=y<1/3. The identity and tail bound are

    ln(t) = 2*sum_{j>=0} y^(2j+1)/(2j+1),
    0 <= tail_N <= 2*y^(2N+1)/((2N+1)*(1-y^2)).

The tail inequality follows by replacing every remaining denominator by 2N+1 and summing a geometric series. The identity follows by integrating 2/(1-y^2) from 0 to y. Enclose ln(2) by the same formula at y=1/3. If [a,b] encloses ln(t) and [c,d] encloses ln(2), then log2(x) belongs to [k+a/d,k+b/c]. Here only the nonnegative reduced numerator is divided, so a negative integer k cannot cause the historical negative-numerator division error. Powers of 2 are exact. For every negative linear coefficient, reverse the endpoints before multiplication. All operations use Fraction. We use N=8 once and do not refine it.

For a physical block A, let mu be the parent squared biased Fourier law, q its residual marginal, and mu_z the actual child law with branch probability w_z. The exact mixture identity q=sum_z w_z mu_z gives

    M-J = H(mu)-2H(q)+sum_z w_z H(mu_z).

Each witness is checked from an actual Boolean sign table with little-endian assignment order. The A072 engine checks signed inversion, Parseval and physical pivotal probabilities. A second implementation independently reconstructs selected squared masses by direct centered weighted moments and reconstructs the unfactored entropy product, using neither A072 nor the prime-factor helper.

The minimum-positive record selected by A071 has table (1,1,1,-1,1,1,1,1), p=(1/8,1/8,1/2), and A={2}. Its parent masses are (3969,7,7,49,1,7,7,49)/4096, marginal (1985,7,7,49)/2048, and children (961,7,7,49)/1024 and (1,0,0,0), each with probability 1/2. Because the selected coordinate is uniform, Delta_A=0, so D=M+Delta-J=M-J. Exact expansion yields

    2048*D = log2(U/V),
    U = 1985^3970,
    V = 2^10240 * 3^7938 * 7^3969 * 31^1922.

The integer comparisons certify 2^5*V < U < 2^6*V. Thus

    5/2048 < D < 3/1024.

The separate N=8 enclosure, outward rounded by rational floor/ceiling at scale 10^8, certifies

    0.00256646 < D < 0.00256649 bits.

This confirms this selected record, not its minimality or the entire grid.

The exact-zero record has table (1,-1,-1,-1,-1,1,1,1), the same p and A. Its aggregated prime-log coefficient dictionary is empty, so D=0 exactly. This is code15 under A071's output-complement convention. No near-zero tolerance or precision increase is used.

For tax-free AND, table (1,1,1,-1), p=(1/8,1/4), A={0}, let R=J-M. Its exact comparison is

    128*R = log2(U/V),
    U = 2^224 * 3^225 * 5^225 * 7^14,
    V = 29^232.

The integer comparisons give 15/128<R<1/8. The independent N=8 rational enclosure certifies 0.11954501<R<0.11954502, in particular R>1195/10000. This corroborates the existing repaired B09 helper counterexample. It does not refute FEI or give any unbounded H/I family.

Exact rational bounds, input laws, prime exponents, product bytes, and SHA256 hashes are saved in LOG_SIGN_CERTIFICATE.json and out/. Product signs are determined before the separate interval check. There are no unresolved signs, precision refinements, or all-real-parameter claims.
