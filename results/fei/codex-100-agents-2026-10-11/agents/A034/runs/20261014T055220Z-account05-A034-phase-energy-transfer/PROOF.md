# All-product conditional rows: complete phase-energy payment

Actual Boolean F on exactly two address bits X and any number of uniform physical data bits Y; independent uniform input. Set h_J=2 E_X F chi_J, w_J=E h_J^2/4 and p_J=hat(h_J)^2/(4w_J), omitting zero rows. Assume every p_J is a coordinate product, allowing any number of nonfair coordinates, arbitrary odds and arbitrary real Fourier signs. Entropy is in bits and all influence uses the original physical coordinates.

Write b=h2(1/10), Kcond=3/2+(5/2)b and Kall=6+2log2(65/64). Then

    H(S_Y|S_X)<=Kcond I_Y,
    H(F)<=Kall I(F), Kall<7.

Also Q=sum_J w_J N_J<=(5/2)I_Y sharply. Regular rows have N<=m<=2a; the exceptional configuration has Q=5/8 and I_Y>=1/4. This is data-energy payment, not the separate address-only target.

The conditional constant is sharp at the three-bit point defect. This extends A079's single-nonfair and A033's two-nonfair mechanisms to ALL coordinate-product rows, without increasing either constant. It does not prove the separate Q/address-only target or admit nonproduct laws.

## 1. Primitive integer product factors and a proportional fair-count bound

Consider one nonzero integer row h of height at most2. Remove deterministic spectral characters and unused coordinates. Its reduced physical cube has n=N+m bits, where N counts nonfair varying marginals and m counts fair varying marginals. The reduction preserves integrality, height and normalized entropy, and does not increase physical row influence. Every coefficient on the reduced frequency cube is nonzero.

Let P=2^n and W be the raw Walsh transform. Product squares imply

    |W_s|=c product_i a_i^(1-s_i)b_i^s_i,

where a_i,b_i are coprime positive integers and c is an integer: the products have gcd1, so the rational common scale has denominator1. Odd divisors of c divide every h value by integer inverse transformation (P has no odd factor). Height<=2 excludes any such divisor, so c is a power of two. A primitive fair pair is(1,1). A nonfair primitive pair has odd part u_i of a_i^2+b_i^2 at least5: opposite parities give an odd sum>=5; both odd give valuation exactly1 and odd part>=5 unless the pair is(1,1).

With k=sum_y h(y)^2, Parseval says c^2 product_i(a_i^2+b_i^2)=P k. Since c and P are powers of two, the odd part of k equals product of the odd parts of these primitive sums. In particular

    5^N<=oddpart(k)<=k<=4*2^(N+m).                 (A)

If N>=4 and m<=N-1, (A) gives5^N<=2*4^N, impossible:5^4=625>512=2*4^4 and the left/right ratio increases by5/4 with N. Thus m>=N for every N>=4. For N=3, m<=1 is excluded by125>64. For N=2, m=0 is excluded by25>16. The ONLY remaining low-fair endpoints are N=2,m=1 and N=3,m=2 (besides N=1,m=0).

## 2. An analytic exclusion of the N=2,m=1 endpoint

Here P=8,25<=oddpart(k)<=k<=32. Both nonfair odd factors must be5: if one were an odd integer>=7 their product would be>=35. Thus oddpart(k)=25 and k=25. A primitive sum with odd part5 is either5 or10 (a coprime sum of two squares has valuation at most1), and its pair is respectively(1,2) or(1,3), up to swapping.

Let B be the number of(1,3) pairs. The fair pair contributes2 and the norm identity reads c^2*25*2^(B+1)=8*25. Hence B+2log2(c)=2: the possibilities are B=0,c=2 or B=2,c=1. A mixed B=1 is impossible.

Because h takes values0,+/-1,+/-2 and has k=25 on eight points, its counts obey mu+4e=25 and mu+e<=8. Therefore mu=1,e=6, with exactly one zero point. Denote the parity of the mixed point by t=+/-1 and of the zero point by z=+/-1. The signed square moment is

    A=sum_y h(y)^2 chi_full(y)=-3t-4z in{+/-1,+/-7}.

The full-complement convolution is sum_s W_s W_(s xor full)=8A. In B=0 every summand has magnitude c^2 product_i a_i b_i=16, so16 divides8A, impossible for odd A. In B=2 every summand has magnitude9, so9 divides8A and hence A, impossible for A=+/-1,+/-7. This rejects every phase assignment without a five-valued truth-table census.

## 3. The N=3,m=2 endpoint is the accepted concentrated singleton obstruction

Now P=32 and125<=oddpart(k)<=k<=128. Every nonfair odd factor is5 (otherwise the product is>=175), so oddpart(k)=125 and k=125. Counting physical heights gives mu+4e=125 and mu+e<=32, hence mu=1,e=31 and no zeros. This is precisely a concentrated row of height1 at one point and height2 everywhere else.

For completeness, every raw Walsh coefficient is odd. Thus c=1 and all primitive pairs are odd; all three nonfair pairs must be(1,3). The full-complement product magnitude is27. The signed square moment is-3t with t=+/-1, so27 must divide3P=96, which it does not. This is the independently accepted concentrated clause of A034 version2, reconstructed here; no disputed coupled assertion is used.

Consequently EVERY nonfair product row has m>=N, except N=1,m=0.

## 4. The exceptional row and the actual common mask

For N=1,m=0 remove its deterministic physical character. The two physical values are integers in{-2,-1,0,1,2}. Their sum/difference gives the only nonfair nondeterministic primitive ratio3:1. Its physical absolute values are1 and2, so the shared mixed set M is exactly a half cube in that physical coordinate. At every point of its complement this row owns the unique pure entry. Therefore this row has mass5/8; each other row has magnitude1 on M and zero off M, with mass1/8.

The companion rows' squared norms, after removing deterministic/unused variables, are powers of two: weight1/8 implies k=P/2. Equation(A)'s exact odd-part identity forces N=0 for each companion, regardless of how many nonfair coordinates were initially allowed. Every companion has at least one fair frequency coordinate, since support on one physical half cube makes the relevant frequency coordinate fair. If d_J is its number of fair coordinates, d_J>=1.

Let e=sum_(companions)(d_J-1)/16>=0. Fixed-one frequency bits only add physical influence. Then

    I_Y>=1/4+e,
    H(S_Y|S_X)=(5/8)b+3/8+2e=Kcond/4+2e,
    I_X>=1/2,
    H(F)=4-(9/8)log2(3)+2e.

These bounds pay the entire conditional entropy at Kcond and the whole entropy at Kall>6. The point defect attains the conditional equality. No address debt or terminal entropy is erased.

## 5. Regular rows and the complete address ledger

For the N nonfair coordinates let q_i<=1/2 be their smaller marginal probabilities. The original physical row influence a satisfies a>=m/2+sum q_i. Product laws give H(p)=m+sum h2(q_i), and H_1/2(p)<=m+N.

Gibbs gives h2(q)<=c q+log2(1+2^-c). At c=5/2, log2(1+2^-5/2)<1/4: squaring the positive comparison and simplifying is equivalent to sqrt(2)>11/8 (121<128). Thus when m>=N,

    H(p)<=m+(5/2)sum q_i+N/4<=(5/2)a.

Kcond>5/2 follows from b>21/50:5^10>2^23 and3^5<2^8 give b=1+log2(5)-(9/5)log2(3)>21/50. Fair-only rows pay at2, and the exceptional common-mask ledger already pays at Kcond.

For complete joint entropy set l=log2(65/64)>0. Gibbs at6 gives

    H(p)+H_1/2(p)<=2m+6sum q_i+N(1+l)
                         <=(6+2l)(m/2+sum q_i),

since the difference is(1+l)(m-N)+2l sum q_i>=0. Fair-only rows pay this sum at4.

Reconstruct A079's universal Boolean address ledger. At every y the four h_J entries are either one pure magnitude2 or four mixed magnitudes1; let delta=Pr(M). The mixed part contributes delta to I_X, so delta<=I_X. Fourier inversion bounds max|h_J|<=2 sqrt(w_J) sum sqrt(p_J). A row with a pure point therefore has log2(1/w_J)<=H_1/2(p_J); a mixed-only row has log2(1/w_J)<=H_1/2(p_J)+2. A mixed-only row's mass is delta/4, and their total mass is at most delta. Hence

    H(w)<=sum_J w_J H_1/2(p_J)+2I_X,
    H(F)<=sum_J w_J[H(p_J)+H_1/2(p_J)]+2I_X.

The regular payment and exceptional ledger prove the announced theorem using one physical influence account. H(S_Y|S_X) is retained in full. Kall<7 because65^2<2*64^2.

## 6. Guards, stability limits and the first unsupported line

Tensor admission is restrictive. If an admitted actual Boolean function factors with a fresh Boolean data seed g, each nonzero row's conditional law factors with the squared spectrum of g. Product admission forces that seed spectrum to be coordinate product. The primitive odd-part identity applied to the height1 seed has k=P, so it has no nonfair marginals: every active coordinate is fair. Arbitrary Boolean seeds are excluded. Tensoring with such an admitted seed preserves the class, entropy and influence add exactly, and its entire conditional spectrum is paid. No closure under arbitrary physical restrictions or under correlated physical input laws is asserted; the original affine quadratic-row stability theorem remains the previously proved stable subclass.

The normalized non-Boolean control psi=(sqrt(255)+y)/16, independent of addresses, has product spectrum with q=1/256, I=q and H=h2(q)>8q. It violates both advertised constants (each<7), so Boolean height admission is essential. The actual three-bit point defect tests the vacuous single-data-coordinate hypothesis and attains Kcond.

The separate lead target Q=sum w_J N_J<=K(H(w)+I_X) is still unproved: m>=N only pays Q from fair physical data energy, not address entropy. The first unsupported extension of the entropy theorem is nonproduct conditional rows, retaining the exact signed address/Renyi gap and terminal entropy. A universal H_1/2/I inequality is not substituted for that unpaid implication.
