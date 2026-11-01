# Independent reconstruction of A073's positive-erasure remainder

All logarithms are base two. Fix even d>=2, delta=2^-d, t=sqrt(delta)=2^(-d/2), e=delta/2. Put b(y)=(-1)^(y1*y2+...+y(d-1)*yd), q(u,v)=-1 only at (1,1), and F=b+1[y=0](q-1). It is Boolean since b(0)=1. Use 0/1 physical labels and characters (-1)^(S dot x).

The two-bit bent factor has coefficients (1,1,1,-1)/2, so b has coefficients sigma_T*t. Their sum is b(0)=1, giving N_+-N_-=1/t and N_++N_-=1/delta. The coefficients of q are (1,1,1,-1)/2. Therefore the four F amplitudes over each core set T are sigma_T*t-delta/2, delta/2, delta/2, -delta/2. They are nonzero since t<=1/2 and t>delta/2. Every squared Fourier atom is positive and both queried erasures are strictly positive.

Consider query u and let V denote whether the residual set contains v. On V=0, the two paired masses are (sigma*t-delta/2)^2 and delta^2/4; on V=1 both are delta^2/4. The upper mass totals e=delta/2. Thus the complete derivative law mu(T,V) is delta/2 for every T,V. The complete reference r(T,V), which includes all residual atoms, is delta*c_sigma on V=0 and delta^2/2 on V=1, where c_sigma=1-sigma*t+delta/2. Summing yields r_V=(1-e,e), while mu_V=(1/2,1/2). These are complete normalized laws, with no derivative-support conditioning.

Given V=1, both conditional core laws are uniform, with each atom delta. Given V=0, the derivative law remains uniform and the reference has masses delta*c_sigma/(1-e). KL chain decomposition gives

    D(mu||r) = D((1/2,1/2)||(1-e,e)) + D0/2,
    D0 = sum_sigma N_sigma*delta*log2((1-e)/c_sigma).

Thus quotient loss in influence-weighted divergence is L_u=e*D0/2. Symmetry gives the same result for v. Both sigma values occur with positive counts, and their c values differ, so strict KL nonnegativity gives D0>0.

For the upper bound, c_- >= c_+. Moreover

    7*c_+ - 5*(1-e) = (2-3t)*(1-2t) >= 0.

Every conditional likelihood ratio is therefore at most 7/5, implying D0<=log2(7/5). The exact integer inequality 7^128 < 2^63*5^128 gives log2(7/5)<63/128. Consequently

    0 < L_u/e <= log2(7/5)/2 < 63/256 = 1/4-1/256.

The two losses together are e*D0<delta/4. Each core coordinate has influence (1+delta)/2: the original bent influence is 1/2, all edges from 0 to a basis vector were nonpivotal, and the edit reverses those edges for exactly one quarter of the gate assignments, adding delta/2. Because delta<=1/4,

    delta/4 <= (1+delta)/20 = Inf_y1/10.

Strictness in the first inequality proves the stated dedicated reserve bound, including d=2 where the second inequality is equality. This fraction pays only these two losses, once; no entropy or other row charge is assigned to it.

The complete retained row price is not bounded by this remainder estimate. Direct substitution of the binary KL gives

    M_u/e = 1 + (1/2)log2((1-e)/e) - D0/2
          > d/2 + 3/4,

since (1-e)/e=2^(d+1)-1>=2^d and D0/2<1/4. Summing actual physical influences gives I=d/2+(d/2+1)*delta. The spectrum lives on d+2 coordinates, so H<=d+2 and H/I<=2+4/d<=4. None of these functions disproves FEI.

This proves every clause of A073-NONZERO-ERASURE-BINARY-REMAINDER@1 without modifying its statement or adding a repair. A098 is an independent reviewer of this version. Its analytic quantifiers cover all even d>=2; the five fixed-dimensional truth tables independently verify the coefficient and conditional-law identities, not an extrapolation. The universal first unsupported line remains a complete normalized conditional partition and globally nonoverlapping terminal reserve for arbitrary Boolean rows, sufficient to pay sum_i e_i*D_i >= sum_i e_i*log2(1/e_i)-K*I with one absolute K.

The checker represents KL as rational linear forms in logarithms of integer primes. Differences of predicted and complete-law expressions cancel exactly, before any interval estimate. For signs, it reduces positive rational log arguments to a power of two times x in [1,2), then uses z=(x-1)/(x+1) and 12 fixed terms of 2*sum z^(2j+1)/(2j+1). The positive remainder is bounded by 2*z^25/(25*(1-z^2)); division by the positive analogous ln2 interval preserves rigorous endpoints. No floating logarithm or repeated precision search is used.
