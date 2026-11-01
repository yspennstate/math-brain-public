# Exact conditional-product endpoint: one address bit, and a two-bit boundary

Date: 2026-09-30. Full FEI remains OPEN. This is an exact arithmetic endpoint for the collective wringing route, not an approximate stability theorem. Publication priority is unverified.

## 1. A norm-arithmetic lemma

Let a be a nonzero finite vector of dyadic rational amplitudes indexed by a Boolean cube. Suppose its normalized squared law is a product law. Then its squared norm w is dyadic and its reduced odd numerator is congruent to 1 modulo 4.

**Proof.** Remove all coordinates deterministic under the product law. On the remaining r active coordinates every amplitude is nonzero. Since ratios of nonzero amplitudes are rational, the ratio of their magnitudes along coordinate i can be written B_i/A_i, where A_i,B_i are positive coprime integers. Product magnitudes then have the form

    |a_s|=c product_i A_i^(1-s_i) B_i^s_i.

The gcd of the integer products is one: for any prime, choose in each coordinate a factor not divisible by that prime. Thus a finite integer combination of those products equals one. Since all |a_s| are dyadic, the same combination shows that c is dyadic.

Consequently

    w=c² product_i (A_i²+B_i²).

If exactly one of A_i,B_i is odd, the corresponding sum of squares is odd and congruent to 1 modulo 4. If both are odd, its 2-adic valuation is exactly one and its odd part is again 1 modulo 4, since odd squares are 1 modulo 8. The odd part of the square factor c² is also 1 modulo 4. Their product proves the claim. Deterministic or one-atom components are included by an empty product. QED.

### Corollary 1.1

If two nonzero dyadic product-amplitude vectors have squared norms w0,w1 summing to one, then w0=w1=1/2.

Indeed, write wj=uj/2^dj in reduced form. Both dj>=1. Unequal denominators give an odd numerator when brought to the larger denominator, which cannot equal its even denominator. Thus d0=d1=d. Since u0 and u1 are each 1 modulo 4, their sum is 2 modulo 4; hence 2^d has d=1, forcing u0=u1=1.

If a dyadic product-amplitude vector has norm squared 1/2, every nondegenerate marginal of its normalized squared law is 1/2. In the factorization above the odd part of w is one, so each primitive A_i²+B_i² is a power of two. This forces A_i=B_i=1. The number r of active fair coordinates is odd, since c²2^r=1/2 and c is dyadic. At norm squared one the same argument gives an even number of fair coordinates, recovering the prior exact-product endpoint.

## 2. One address bit is paid with constant two

### Theorem 2.1

Let f be Boolean, and suppose that, conditional on either positive-probability value of one spectral coordinate X_j, the squared Fourier law of all other coordinates is a product law. Then

    H(f)<=2 I(f).

In fact the theorem holds for any unit vector of dyadic amplitudes with that conditional-product property; full Booleanity is used only to guarantee dyadic amplitudes and norm one.

**Proof.** The two coefficient slices across j are dyadic product-amplitude vectors. If both have positive mass, Corollary 1.1 makes both masses 1/2. Let r0,r1 be their respective fair-coordinate counts and k0,k1 their fixed-one counts. Their conditional entropies are r0,r1, and conditional expected remaining sizes are k0+r0/2 and k1+r1/2. Therefore

    H(f)=1+(r0+r1)/2,
    2I(f)=1+k0+k1+(r0+r1)/2 >=H(f).

If only one slice has positive mass, its mass is one and the prior exact-product argument gives H<=2I on the remaining coordinates. A fixed-one queried bit adds influence but no entropy. QED.

The constant two is attained by a two-bit bent Boolean function. This is a coupled arithmetic result: an individual half-difference/half-sum projection need not be Boolean or have fair conditional marginals, but its complementary slice cannot simultaneously be product with incompatible mass.

## 3. Exact two-address Boolean obstruction to extending the same constant

The one-bit statement does not extend unchanged to two address bits.

On four physical bits x, in least-significant-bit order, define the ternary function

    g=[1,-1,-1,0,-1,0,0,1,-1,-1,-1,0,-1,0,0,1].

Its Walsh coefficients multiplied by sixteen are

    [-4,-4,-4,4,-4,4,4,4,2,2,2,2,2,2,2,2].

The normalized squared law is product with marginals `(1/2,1/2,1/2,1/5)`, and its squared norm is 5/8. This is allowed by the norm-arithmetic lemma: its odd numerator is five.

Let h1,h2,h3 be the indicators of the three disjoint edges specified by low-three-bit values 3,5,6 respectively, with bit3 free. These edges partition the zero set of g. Introduce two address bits y1,y2 and put

    F(y1,y2,x)=g(x)+chi_1(y)h1(x)+chi_2(y)h2(x)
                       +chi_{1,2}(y)h3(x).

Exactly one summand is nonzero at each physical x, and it equals a sign. Thus F is Boolean.

Its four partial Walsh projections on y are exactly g,h1,h2,h3. Their masses are

    (5/8,1/8,1/8,1/8).

Every normalized conditional spectrum is product. The first has the marginals above, and the other three have `(1/2,1/2,1/2,0)`.

The full squared Fourier law has eight atoms of mass 1/16 and thirty-two atoms of mass 1/64. Hence H(F)=5. Directly from the four projection laws, or from pivotal-edge counting, its physical influence vector in order `(y1,y2,x0,x1,x2,x3)` is

    (1/4,1/4,1/2,1/2,1/2,1/8).

Therefore

    I(F)=17/8,   H(F)/I(F)=40/17>2.

This is a genuine six-variable Boolean counterexample to the two-address constant-two extension. It does not refute a different finite collective constant, an estimate paying the entire address entropy, or FEI.

## 4. Checks, review, and relation to prior work

The original zero-address product rigidity is prior September21 work cited in REPORT.md; it is not claimed as new. A bounded repository search did not locate this exact one-address extension, but absence from a search is not a novelty certificate.

The coordinating researcher independently checked the norm-arithmetic and one-address proofs. The researcher then supplied the two-address construction, which this report's author independently reconstructed with integer Walsh transforms and the exact mass/entropy/influence calculation above. No formal proof-assistant certification is claimed.

`check_endpoint.py` exhausts Boolean truth tables through dimension four for the distinguished first spectral coordinate, using exact integer factorization tests for both conditional product laws. It also independently verifies the six-variable counterexample. The output is recorded in `endpoint_verification.json`. These finite checks support, but do not prove, the arbitrary-dimensional one-address theorem.

The general collective payment in REPORT.md equation (5.1), its approximate-product version, and arbitrary-address control remain OPEN.
