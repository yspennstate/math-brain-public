# Three-core order-free refund: exact finite closure

All signs Boolean, cube uniform, entropy bits. Point blocks A_r,B_s are fresh and independent of the shared data cube, with a=2^-r,b=2^-s. Three cores g0,g1,g2 occupy the SAME data coordinates. Define h=g1+B_s(g2-g1), f=g0+A_r(h-g0). Query A first, B only on success, then STOP at the actual core. Terminal probabilities are pi=(1-a,a(1-b),ab). They are physical probabilities, not independent copies or spectral weights.

## Independently reconstructed nested identities

Let gamma_ij=P(gi!=gj), Iij=I(gi gj), I_B=2s b gamma_12, I_A=2r a[(1-b)gamma_01+b gamma_02]. Actual removed influence is I_C=I_A+a I_B; terminal influence I_T=sum pi_j I(gj), entropy H_T=sum pi_j H(gj). Direct edges give I(f)=I_C+I_T. The outer product g0 h has data influence (1-b)I01+b I02 and B-control influence I_B, because multiplying by g0 cannot change whether a B edge flips. Applying the reviewed A023@3 block payment twice therefore asks for

    R_data=2a(1-a)[(1-b)I01+b I02]+2ab(1-b)I12,
    R_control=2a(1-a)I_B.

These are actual source reserves. The control part cannot be omitted from that sufficient nested derivation. Data-edge pivots of a product are the XOR of branch pivots, so each coordinate has terminal rate owners

    core0:2a; core1:2(1-a+b); core2:2(2-a-b).

For example, the g2 coefficient is 2ab(1-a)+2ab(1-b), divided by its terminal probability ab. This gives the source's finite two-block rate and signed child-slack condition, without a renewed terminal allowance.

Define a different, order-free DATA reserve

    R_star=2 sum_{i<j} pi_i pi_j Iij.

Expanding coefficients gives the exact identity

    R_data-R_star=2a(1-a)b(1-b)I12.

For each data coordinate k, Iij's contribution is <=Inf_k(gi)+Inf_k(gj), so

    R_star,k <=sum_j 2(1-pi_j)pi_j Inf_k(gj).

Hence R_star<=2I_T, with each terminal coordinate marked once. The extra hierarchy charge is a real difference between two sufficient reserves; its positivity is NOT a proof that actual entropy needs it. Conversely, just deleting it from the source upper bound is invalid. These statements independently confirm A029 DERIVATION.md's nested algebra and diagnostic distinction.

## Exact finite theorem

Declared domain D consists of (i) EVERY ordered triple of the16 Boolean signs on two shared data bits at r=s=1, including constants, repetitions and ignored data bits; (ii) EVERY ordered triple of pairwise-distinct NONCONSTANT two-bit signs at (r,s)=(1,2),(2,1),(2,2). There are 4096+14*13*12*3=10648 labeled cases. No quotient or random sampling occurs. The largest cube has six bits.

For every f in this exact domain,

    H(f)-H_T <=4 I_C+R_star.                              (1)

Proof is the complete exact certificate in code/check_three.py, code/sharp_rate.py and their saved outputs. The checker builds actual truth tables, counts each physical edge and uses integer Walsh transforms. Every entropy is a rational linear combination of log2 primes. The helper is pinned own stage4 code, never another agent's script. It verifies the displayed coordinate/control/terminal identities, the source bound including both charges, and the new order-free bound. Each completed case is flushed immediately.

For the stronger rate4 in (1), the second checker compares ALL10632 positive-I_C cases exactly. It normalizes (H-H_T-R_star)/I_C as a prime-log vector and selects the maximum by exact differences, retaining all ties. The maximum is

    M=33/2-(25/8)log2(5)-(27/8)log2(3)<4.

There are64 ties. One is core indices(1,0,1), r=s=1, in lexicographic truth-table order {-1,1}^4: g0=g2=(-1,-1,-1,+1), g1=(-1,-1,-1,-1). Its I_C=1/4, H_T=3/2, R_star=3/8; the saved direct entropy vector verifies M. This is a repeated-core extremizer, while the additional wider-block domain deliberately requires distinct nonconstant cores. No claim that M maximizes any omitted domain is made. For the16 cases with I_C=0, all three reachable cores coincide; entropy increment and reserve are zero, verified exactly. Thus (1) follows on every declared case.

The exact log algorithm: for prime p, write p=2^k x with1<=x<2, z=(x-1)/(x+1). Then ln x lies between 2sum_{j<T}z^{2j+1}/(2j+1) and that sum plus2 z^{2T+1}/[(2T+1)(1-z^2)]. Divide by positive certified ln2 endpoints, combine signs correctly, and round outward to100-bit dyadics.24 terms suffice for every saved sign;48 is the frozen fallback. Identically zero vectors are exact equality. The saved rational endpoints, not decimal approximations, prove every sign and every maximum comparison. This provides a complete finite proof, not floating search evidence.

Every nonconstant sign on two bits has I>=1: its disagreement boundary has at least2 undirected edges of the four-cycle and normalized influence equals half its boundary. Fourier support has at most4, hence H<=2. Constants have H=I=0. Thus H_T<=2I_T. Combining (1) with R_star<=2I_T proves

    H(f)<=4I(f) for all10648 cases.                       (2)

Strict rate4 slack occurs when I_C>0. No terminal entropy is discarded. A fresh point activation of any of these f's has H<6I for positive new control influence: constant-child splits have B/d<3, JS/d<3, retained terminal entropy2^-t H(f)<=4*2^-t I(f). For fixed nonconstant f, its influence is2^-t[I(f)+t(1-Ef)], tending to zero. This yields an unbounded rare-activation family using a complete finite seed certificate, not an arbitrary-core FEI assumption.

## Universal first unsupported line

There is NO all-dimensional proof of H-H_T<=4I_C+R_star, or even the original tested5.5 rate, for arbitrary three shared-data cores and widths. The exact finite certificate does not justify subtracting the grouping/control charges from A029's general sufficient bound. It also does not control localized bad-face credit. The next critical case is three balanced bent/edit branches (two distinct edit vertices), where contrast grows with core dimension and nonempty Fourier rows interfere coherently. An analytic signed refund there would address the omitted mechanism; simply increasing the two-bit census would not.
