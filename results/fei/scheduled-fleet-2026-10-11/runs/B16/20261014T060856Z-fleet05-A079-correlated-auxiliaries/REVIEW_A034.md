# Independent reconstruction of A034-ALL-PRODUCT-ROW-PAYMENT@1

Verdict: **HOLDS at the stated two-address, coordinate-product scope.** This is
an independent reconstruction of the entire unbounded-count proof chain, not
an extension to nonproduct rows or a repair. No upstream checker was imported.
The withdrawn coupled-gcd assertion in A034-SIGNED-ODD-MASK-ADMISSION@1 is not
used. Corrected version2 is compatible with the reconstruction below.

## Primitive norm reconstruction

Let h=2 E_X F chi_J. Actual Booleanity gives integral values in
{0,+/-1,+/-2}. Remove fixed frequency characters and inactive physical
coordinates. If the squared Fourier law is product, its remaining n=N+m
coordinates have N nonfair and m fair marginals, with no zero coefficients.
Ratios of absolute raw Walsh coefficients along each coordinate are positive
rationals. Reduce each ratio to coprime integers (a_i,b_i). All coefficient
magnitudes then equal c times products choosing one element from each pair.
For every prime a choice exists in each pair avoiding that prime, so the gcd of
these products is1. Since all raw coefficients are integers, c is an integer.
An odd prime dividing c would divide every inverse physical value: the inverse
denominator is a power of two. A nonzero height-two row cannot have such a
divisor. Thus c is a power of two, including c=1.

Set P=2^(N+m), k=sum_y h(y)^2. Parseval is
c^2 product_i(a_i^2+b_i^2)=Pk. For a primitive pair, its sum of squares has
2-adic valuation0 or1. Its odd part equals1 only for (1,1): for opposite
parities the nonfair minimum is5; for both odd, valuation1 and the first
nonfair pair is (1,3), again odd part5. Therefore

    oddpart(k)=product_nonfair oddpart(a_i^2+b_i^2)>=5^N,
    k<=4P.

For N>=4, m<N would imply 5^N<=2*4^N, contradicted by 625>512 at N=4
and multiplication of the ratio by5/4 for each subsequent N. N=3,m<=1 and
N=2,m=0 are rejected by125>64 and25>16. The remaining endpoints are
N=2,m=1 and N=3,m=2, in addition to N=1,m=0. This is an all-N induction;
no finite-N assertion is extrapolated.

## Independent endpoint argument in physical space

For N=2,m=1, P=8 and 25<=oddpart(k)<=32. Both primitive nonfair odd
parts must be5, because5*7>32. Thus k=25. The only sums are5 and10,
arising from pairs (1,2) and (1,3). Including the fair factor2 in Parseval
forces either both pairs (1,2) with c=2 or both (1,3) with c=1. The
physical heights force one point of absolute value1, six of absolute value2,
and one zero. If t and z denote the full physical parity at the unit and zero
points, the full-parity square moment is A=-3t-4z in{+/-1,+/-7}.

The complementary Walsh convolution is sum_s W_s W_(s xor full)=8A.
Every summand has magnitude16 in the (1,2) case, so 16|8A would force A
even. Every summand has magnitude9 in the (1,3) case, so9|A. Both are
impossible. This proof covers every Fourier phase.

The independent checker instead enumerates all physical placements and signs
at that forced norm, fixing the unique unit value positive modulo global sign:
8*7*2^6=3584 rows. It verifies exact norm, square moment and complementary
convolution, and tests the FULL product identity using integer marginals. No
row is product, independently rejecting the endpoint without using the author's
512 Fourier phase assignments or A033's complete five-valued census.

For N=3,m=2, 125<=oddpart(k)<=128 gives k=125. Physical heights force
one unit point and31 height-two points, with no zeros. Every Walsh coefficient
is odd, hence c=1 and all pairs are odd. Each of the three nonfair pairs is
(1,3). The complementary products have magnitude27. The square moment is
A=-3t, so27 must divide32A=+/-96, impossible. Our checker independently
tests all32 singleton locations. The argument eliminates arbitrary signs
analytically; it does not pretend to enumerate2^32 phase choices.

Consequently every product row has m>=N except the one-coordinate endpoint.

## Complete shared-mask and entropy reconstruction

For N=1,m=0, enumerate the two integer physical values in[-2,2]. The only
nonfair nonzero Fourier pair is primitive ratio3:1, from absolute physical
values2 and1. The common mixed mask M is a physical halfcube. The heavy row
has w=5/8 and owns every pure point. Its three companions have weight1/8
and support exactly M. Their reduced squared norms k=P/2 are powers of two;
the exact odd-part identity above excludes EVERY nonfair marginal in them.
Each companion's support on M forces at least one fair frequency coordinate.

Writing b=h2(1/10) and e=sum_companions(d_J-1)/16 gives
H(Y|X)=5b/8+3/8+2e=Kcond/4+2e and I_Y>=1/4+e.
Fixed-one characters add influence and no entropy. Also I_X>=1/2 and
H(F)=4-(9/8)log2(3)+2e. This exceptional configuration pays sharply at
Kcond=3/2+(5/2)b, and its nonfair mass Q=5/8 pays at Q/I_Y<=5/2.
The actual three-bit point defect gives both equalities.

For regular rows let q_i be the smaller nonfair marginal. Physical row mean
degree a>=m/2+sum_i q_i, whereas H=m+sum_i h2(q_i) and R=H_1/2<=m+N.
Gibbs/KL gives h2(q)<=c q+log2(1+2^-c). At c=5/2 the logarithm is
<1/4: its equivalent positive comparison is sqrt(2)>11/8, certified by
128>121. Because m>=N, H<= (5/2)a. At c=6 set l=log2(65/64).
Then H+R<=2m+6sum q_i+(1+l)N, and the excess of
(6+2l)(m/2+sum q_i) over that expression is
(1+l)(m-N)+2l sum q_i>=0. Fair-only rows pay H<=2a and H+R<=4a.
Also N<=m<=2a, paying the regular nonfair mass at2, below the exceptional5/2.

The address ledger retains the entire conditional spectrum. At each data
point the four h_J are either one magnitude2 or four magnitudes1. If delta
is the mixed probability, the mixed part contributes exactly delta to I_X.
Fourier inversion gives ||h_J||infinity<=2sqrt(w_J)sum sqrt(p_J).
A pure row satisfies log2(1/w_J)<=R_J. A mixed-only row satisfies
log2(1/w_J)<=R_J+2 and has w_J=delta/4. Their total mass is<=delta.
Thus H(w)<=sum w_J R_J+2I_X, and
H(F)<=sum w_J[H(p_J)+R_J]+2I_X. Apply the regular payment, or the
exceptional full ledger if that endpoint is present. This proves the original
conditional and joint constants and Q<=5I_Y/2, with no repeated physical
account and no unproved theorem premise.

The constant comparisons can be checked with integers: b>21/50 follows from
5^10>2^23 and3^5<2^8; therefore Kcond>5/2. Kall=6+2l<7 follows from
65^2<2*64^2. All these comparisons are separately checked in our scalar
certificate. Joint sharpness is not asserted.

## Guards and honest frontier

The height-one norm argument rejects any nonfair product marginal in a fresh
Boolean tensor factor, since k=P has no odd factor. Its fair/deterministic
spectrum carries H<=2I. Product admission therefore excludes arbitrary seed
tensors. No physical restriction closure is inferred. Our independent actual
nonproduct fixtures lie outside the reviewed theorem, even where the two
conditional frequency branches are product. Those branches are partial
Fourier rows, not Boolean terminal restrictions: their norms and physical
height must be carried explicitly. The first unsupported line is a paid
nonproduct transfer retaining H(w)-E R and the entire two-branch entropy from
one unused physical reserve. This review supplies no such payment and closes
neither unrestricted FEI nor C018.
