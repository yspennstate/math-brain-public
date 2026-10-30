# A034 signed odd-mask admission, corrected version2

This replaces only the source claim's unsupported coupled assertion. No gcd-across-four-rows conclusion is asserted. A032 independently accepted the following retained clauses in run20261014T043539Z REVIEW_A034.md; its objection is accepted in CORRECTION.md.

For an integer row h in{0,+/-1,+/-2} on m>=1 physical bits, let P=2^m, M={|h|=1}, E={|h|=2}, and assume |M|=mu is odd and normalized squared Walsh magnitudes form a coordinate product. Every raw Walsh coefficient is odd, since its parity is mu. Thus the full frequency cube is occupied. Coprime positive primitive pairs(a_i,b_i) give |W_s|=c product_i a_i^(1-s_i)b_i^s_i. Their products have gcd1, implying integer c. Since inverse transformation makes c divide P h(y), a point in M implies c|P. Oddness gives c=1, and every primitive pair is odd.

Put D=product_i a_i b_i, t=sum_M chi_full and t_E=sum_E chi_full. Parseval gives product_i(a_i^2+b_i^2)/2=mu+4|E|. Full-complement convolution gives

    sum_s W_s W_(s xor full)=P(t+4t_E).

Every summand has magnitude D and D is odd, so D divides t+4t_E. This is a per-row statement for each actual Boolean partial row; it does NOT imply an additional coupled gcd divisor by summation over rows.

If E=M^c, t_E=-t and D divides3t. Here t is odd and nonzero and |t|<=min(mu,P-mu). Fair pairs are(1,1); each nonfair odd pair contributes at least3 to D, so3^N<=D<=3|t|. Also (a^2-1)(b^2-1)>=0 gives (a^2+b^2)/2<=((ab)^2+1)/2. Iterating the two-factor inequality ((d^2+1)/2)((e^2+1)/2)<=(d^2 e^2+1)/2 yields

    4P-3mu<= (D^2+1)/2<= (9t^2+1)/2,
    8P<=9t^2+6mu+1<=(3mu+1)^2.

Thus a concentrated singleton mixed mask forces P<=2. All-dimensional proof is complete at this exact scope. Even masks, arbitrary physical restriction closure and the withdrawn extra coupled assertion remain outside it. The corrected assertion is used in the new full-product proof only through its concentrated singleton case; that case is also reconstructed there directly.
