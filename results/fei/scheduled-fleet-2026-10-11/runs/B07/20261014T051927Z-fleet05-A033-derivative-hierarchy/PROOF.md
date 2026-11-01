# Two nonfair marginals: complete endpoint and retained entropy

Author proof with an exact finite endpoint certificate; independent review pending.
All entropies are in bits and all influences use original physical coordinates.

## Statement

Let F(X,Y) be Boolean on two independent uniform physical address bits X and any number of uniform data bits Y. Set h_J=2 E_X F chi_J, w_J=E h_J^2/4. For every positive row assume its normalized squared Fourier law p_J is a coordinate product with at most TWO nonfair nondeterministic marginals. Fixed-zero/fixed-one coordinates and arbitrary Fourier signs are allowed. Then

    H(S_Y|S_X) <= [3/2+(5/2)h2(1/10)] I_Y(F), sharply,
    H(F) <= [6+2 log2(65/64)] I(F) < 7 I(F).

The conditional constant is sharp at the three-bit point defect; the joint constant is not claimed sharp. Neither constant increases from the accepted single-nonfair result. This refines the accepted at-most-one-nonfair terminal case. We do not know from this stage whether an actual Boolean four-row cover realizes two nonfair marginals; no strict nonempty enlargement is asserted.

## Full Booleanity and the row hierarchy

For normalized Fourier coefficients a_S, Booleanity is equivalent to
sum_S a_S a_(S xor T)=1_(T=empty) for EVERY T. No finite-order truncation is substituted. On every physical address face its Walsh transform gives the stronger usable integer admission: h_J is in {0,+/-1,+/-2}; either one row has magnitude 2 and the others vanish, or all four have magnitude 1 and their sign product is -1. Thus M={|h_J|=1} is shared, pure sets E_J={|h_J|=2} partition M^c, and 4h_J^2-h_J^4=3 1_M. The proof below uses these exact heights and shared mask, not merely a norm or a square defect.

## Universal complete entropy ledger (reconstructed from A079)

Write delta=Pr(M) and R_J=H_(1/2)(p_J)=2log2(sum sqrt(p_J)). By the physical row classification, the mixed part contributes delta to I_X=sum_J |J|w_J, so delta<=I_X. Inversion implies ||h_J||_infinity<=2sqrt(w_J) sum sqrt(p_J). If row J has a pure point, log2(1/w_J)<=R_J. Otherwise its nonzero support is M, its maximum is 1 and w_J=delta/4; then log2(1/w_J)<=R_J+2. The total weight of these mixed-only rows is at most delta. Consequently

    H(w)<=sum_J w_J R_J+2 I_X,
    H(F)<=sum_J w_J[H(p_J)+R_J]+2 I_X.             (L)

This holds for every two-address Boolean F, without product assumptions. All conditional and address entropy is retained exactly once. A large Renyi/I ratio by itself is not paid by (L).

## Finite-to-infinite endpoint certificate

For a product row remove its deterministic spectral character. Its remaining inverse depends only on varying physical coordinates and is still integer-valued of height at most two: multiplying by a deterministic character changes only signs. Write m for the number of fair varying coordinates and N for the number of nonfair varying coordinates.

If N=2 and m=0, the inverse is an integer height-two function on exactly two physical bits. There are exactly 5^4=625 possibilities, including zero. For its direct integer Walsh vector W, full-support product magnitudes are characterized by

    W_00^2 W_11^2 = W_01^2 W_10^2.

The finite certificate code/endpoint.py computes this determinant, the two marginal numerators and their exact fairness status for every row. out/endpoint.json contains every admitted nonzero product row and its Walsh vector. It finds 176 product rows, with counts (N,m): (0,0):16, (0,1):32, (0,2):32, (1,0):32, (1,1):64, and NONE with N=2. Thus no N=2,m=0 endpoint exists in ANY data dimension. This is a complete exact certificate for the reduced endpoint, not an extrapolation from small n. The verifier recomputes all 625 rows independently rather than trusting this list.

The separately frozen code/three_endpoint.py tests all 5^8=390625 height-two rows on three physical bits, using the complete identities z_s T^2=product_i marginal_numerator_i(s_i), z=W^2 and T=sum z. Exactly 2208 nonzero product rows are admitted and NONE has two nonfair marginals. The direct-character independent implementation code/verify_three.py reconstructs the same full census and histogram. Hence N=2,m=1 is also impossible in every data dimension; every N=2 row needs m>=2. This is a complete reduced endpoint certificate, not a small-n extrapolation.

If N=1,m=0, the two remaining physical values are integers of absolute value <=2. Their sum and difference give either a deterministic/fair spectrum or the sole nonfair primitive magnitude ratio 3:1, from physical magnitudes 2 and 1. Its row weight is 5/8 and its mixed mask is a physical halfcube. If N=0, H(p)=R=m and row influence is at least m/2.

## Why the exceptional companion rows are fair

If an N=1,m=0 row occurs, it has a pure point at every point outside its halfcube M. The other three rows therefore vanish outside M and have magnitude one on M. Their weights are each 1/8.

For any product row, integer Walsh magnitudes on its coordinate face factor as t times products of coprime positive integer pairs (a_i,b_i); t is an integer because the gcd of those products is one (Bezout in each factor). A fair pair is (1,1). Each nonfair pair has a_i^2+b_i^2 with an odd divisor greater than one. If one is even this sum is odd and >=5. If both are odd the sum is 2 modulo 8, and its odd part could be one only if the sum were 2, forcing the fair pair. Parseval's denominator and the coordinate-face size are powers of two. Thus ANY nonfair pair introduces an odd factor into the reduced numerator of w. It cannot cancel against that denominator. Weight 1/8 is impossible for a nonfair product row, even with two such coordinates. All companion rows are fair. Their halfcube support forces its split coordinate to vary in frequency; hence each has at least one fair coordinate.

Let b=h2(1/10)<=1 and let e=sum_other (m_J-1)/16>=0. Then

    H(S_Y|S_X)=(5/8)b+3/8+2e <=1+2e,
    I_Y >=1/4+e,
    I_X >=1/2.

Fixed-one coordinates only increase influence. More precisely H(S_Y|S_X)=Kcond/4+2e with Kcond=3/2+(5/2)b>5/2>2; therefore H(S_Y|S_X)<=Kcond I_Y, with equality for the three-bit point defect. The bound b>2/5 is certified by 10^10>2^4*9^9. Address entropy H(w)<=2<=4I_X gives joint payment H(F)<=4I(F), stronger than the stated joint rate. This handles the shared-mask endpoint, including the vacuous three-bit point defect.

## Regular rows: the fair coordinate pays the entropy remainder

For every remaining nonfair row m>=N and N belongs to {1,2}. Let q_i<=1/2 be the smaller of the two orientations of each nonfair marginal and let d_J=E_(p_J)|S| be its ORIGINAL physical row influence. Then

    d_J >=m/2+sum_i q_i,
    H(p_J)=m+sum_i h2(q_i),
    R_J=m+sum_i H_(1/2)(Ber(q_i))<=m+N.

The Gibbs bound h2(q)<=c q+log2(1+2^-c) follows by expanding the nonnegative divergence to Bernoulli(1/(1+2^c)). At c=5/2, put a=log2(1+2^-5/2)<1/4. Squaring and simplifying the equivalent positive comparison gives sqrt(2)>11/8, certified by 128>121. Therefore

    H(p_J)<=m+(5/2)sum q_i+N a
             <=(5/2)(m/2+sum q_i)<=(5/2)d_J,

because the difference is m/4-N a>=0 when m>=N.

Fair-only rows pay at rate 2. Summing proves H(S_Y|S_X)<=Kcond I_Y unless the exceptional endpoint exists, which was handled above.

For the complete ledger set l=log2(65/64)>0 and apply Gibbs at c=6:

    H(p_J)+R_J<=2m+6sum q_i+N(1+l)


Put K=6+2l. The difference between K(m/2+sum q_i) and the last expression is

    (1+l)(m-N)+2l sum q_i >=0.

Fair rows have H+R=2m<=4d_J. Summing in (L) gives H(F)<=K I_Y+2I_X<=K I(F). Since 65^4<2^25, log2(65/64)<1/4 and K<13/2<7. No influence budget is duplicated and no terminal spectrum is dropped.

## Controls, scope and exact first unsupported line

The normalized non-Boolean psi=(sqrt(1023)+y)/32 has a product spectrum with one nonfair marginal 1/1024 and no fair coordinate. Its H/I>10 because the rare-atom entropy alone is 10/1024 and the other term is positive. It violates both stated constants, which are <7 (Kcond<=4). Its inverse fails actual Boolean integer-height admission; normalization and product spectra do not suffice.

The three-bit point defect is admitted and handled by the exceptional shared-mask analysis. Arbitrary Boolean spectators are admitted only if their resulting rows still meet the product/at-most-two-nonfair hypotheses. Otherwise their full entropy remains a terminal debt; there is no arbitrary tensor completion.

The first unsupported line toward B07's universal target remains Q=sum w_J N_J<=K0[H(w)+I_X] independent of the number of nonfair marginals, or an equivalent signed conditional payment for nonproduct rows. Even three nonfair marginals are outside this theorem. The exact no-fair endpoint argument above does not imply that arbitrary many nonfair marginals require proportional fair count. Thus no universal FEI constant has been proved. NEXT should seek a shared-mask admission/energy inequality that forces such payment, or an actual two-nonfair cover showing where the accepted terminal class first enlarges.
