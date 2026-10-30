# A074 reconstruction of the actual rare-core obstruction

All entropy uses bits. Bits x encode signs y=1-2x. The gate h is negative exactly on {0,1,2,4,8,16,32,6,17,40}. Define g0=h, g1=h(g0^6), g2=h((-g1)^6), g3=h(g2^6), always on six disjoint copies. These finite circuits have respectively 6,36,216,1296 physical variables. The two children h(g3^6),h((-g3)^6) each have 7776 variables. Circuit descriptions specify actual Boolean functions without listing their exponentially long truth tables.

## Independent representation

For any table f on k bits write f(x)=sum_T c_T product_{i in T}x_i, with integer/rational c_T obtained by binary inclusion-exclusion (Moebius inversion). At independent bit bias p, substitute x_i=p+(x_i-p). The centered coefficient is b_S=sum_{T containing S}c_T p^{|T|-|S|}. Orthogonality gives squared normalized coefficient b_S^2[p(1-p)]^{|S|}. This uses neither a uniform Walsh-to-biased conversion nor the source's enumeration of centered moments. Every computed mass is rational and reconstructed from the actual gate table.

For an outer coordinate j write h=A+y_j D. The 32 section values give A=(h0+h1)/2 and D=(h0-h1)/2. Form the binary polynomials for C=A+mD and D, where m=1-2p. Their centered masses on the other five variables are U_T and D_T. Thus the complete outer biased spectrum consists of U_T and vD_T, v=4p(1-p). The checker independently compares this law with the full six-variable binary polynomial, verifies Parseval and expected spectral degree, and checks all six pivotal probabilities.

The gate is antitone in each sign variable: its negative binary set is downward closed. Therefore D takes only values -1,0. Physical enumeration, or expansion of the above polynomials, gives

q(p)=E D^2=-E D=2p(1-p)^3(2-p),

alpha(p)=P(h=-1)=(1-p)^4(1+4p-2p^2).

Indeed, the negative set has weight counts 1,6,3 in weights 0,1,2, so alpha=(1-p)^6+6p(1-p)^5+3p^2(1-p)^4. For a chosen coordinate, the pivotal other-variable assignments are precisely the four nonpartner singletons and the two matched pairs not containing that coordinate. Therefore q=4p(1-p)^4+2p^2(1-p)^3, giving the displayed formulas. In the checker these closed formulas are checked at every attained rational p, and all six section expectations and pivotal masses agree. No numerical interpolation is used as proof.

## Exact spectral and physical recurrences

Let a core have mean m, singleton square t, physical influence d_i, conditional erasure B_i, and full spectral entropy H. Put Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b), continuously at zero. A centered occupied outer block expands into the inner nonempty Fourier spectrum. The occupied block pattern and its nonempty filling are unique for each physical Fourier set.

For every pair of physical Fourier sets differing only in coordinate i, with a nonempty residual set in its block, the two coefficients inherit the inner pair and sum to q B_i after all other block fillings are integrated. The empty residual instead gives the pair (U_T,t D_T). Subtracting the inherited empty pair gives exactly

R_p(t)=sum_T Phi(U_T,t D_T)-q Phi(m^2,t),

B'_(j,i)=q B_i+R_p(t),    d'_(j,i)=q d_i.

The second identity also follows directly from pivotal events: an inner edge flips the output exactly when that inner edge is bichromatic and its outer coordinate is pivotal; the outer pivotal event depends only on the other blocks. The new singleton is (E D) times the oriented inner singleton, hence t'=q^2 t. The seed has t=d^2 by direct character sums and edge counting, so this relation persists.

Write rho for the normalized nonempty inner squared spectrum. Its total unnormalized mass is v, so H(g)=h2(v)+v H(rho). The outer occupied-pattern entropy identity is H(F)=H_p(h)+6vq H(rho). Consequently

H(F)=6q H(g)+C_p,  C_p=H_p(h)-6q h2(v),

I(F)=6q I(g).

All signs of C_p and all terminal entropy are retained. Equivalently H(F)/I(F)=H(g)/I(g)+C_p/(6q I(g)). This is an identity, not an absolute FEI bound.

The gate's three paired coordinates may be permuted and each pair swapped: all 3!2^3=48 permutations preserve the truth table and act transitively. The checker enumerates these permutations directly. Recursion on identical disjoint blocks preserves transitivity, including common output complements. Thus every physical coordinate has the calculated ratio, and the calculated value is the actual minimum E rather than a selected-coordinate proxy.

## A different rigorous logarithm enclosure

For positive rational x, find the exact integer k with x=2^k u and 1<=u<2. Put t=1-1/u in [0,1/2). Then ln(u)=sum_{j=1}^N t^j/j+r, with 0<=r<=2^-N/(N+1). The implementation uses N=180 and the grid 2^-160. It brackets t outwards, brackets every successive power outwards using integer floor/ceiling division, and brackets each division by j. The tail bound is added with upward rounding. The same construction at t=1/2 brackets ln2; dividing its positive interval gives a rigorous log2 interval. Signed weighted interval sums give Phi, entropy, R, C_p and ratios. Fractions retain the exact rational endpoints. Floats occur only in display fields.

The implementation has no call to floating logarithms, imports no source helper and loads no source output until the independent certificate is complete. Its positive geometric log series differs from the source's odd-power atanh series. No claimed sign depends merely on a nominal precision setting: every sign is compared against a saved interval endpoint.

## All-depth bias absorption

For 0<s<=1/16 the two possible common orientations give minority probabilities

1-alpha(s)=12s^2-28s^3+27s^4-12s^5+2s^6,

alpha(1-s)=s^4(3-2s^2).

The second lies strictly between zero and 3s^4. For the first, positivity follows from actual full-support biased inputs and a nonconstant gate. Its bracket after factoring s^2 is <=12 since -28+27s-12s^2+2s^3<0: use 27s+2s^3<=27/16+2/4096<28. Both upper bounds are at most 12s^2<=3s/4<1/2, establishing the correct minority branches as well as absorption. Induction gives 12s_j<=(12s_0)^(2^j) for every future common-sign sequence. This says nothing about independently flipping only some blocks.

## Exact conclusion and first unpaid line

out/VALIDATION.json independently proves E(g3)>669/200 and 0<p_min(g3)<1/16, while both children have E<669/200 and negative reserve at every physical coordinate. out/SOURCE_COMPARISON.json subsequently checks agreement with all six author rows without using them as computation premises. Thus A080@1 is independently accepted at exactly its original scope. Every H/I remains finite; both children increase H/I despite the erasure loss. Neither an unbounded-ratio Boolean family nor a universal FEI constant follows.

The first unsupported universal line is an owned, dimension-independent payment for signed reserve losses and the entire terminal entropy correction, or another operation with an appropriate global telescope. A072's newer one-flip escape changes the operation and may supply a bounded excursion price; it does not contradict the common-sign obstruction or pay repeated excursions. Reviewing that arbitrary-core ledger is the next dependency, rather than repeating finite six-bit admission.
