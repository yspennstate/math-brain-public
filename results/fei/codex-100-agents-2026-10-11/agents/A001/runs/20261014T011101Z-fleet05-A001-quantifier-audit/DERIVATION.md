# Immediate bounded-degree refund obstruction

For a row on residual subsets T, let C_L retain each T with |T|<=L individually and merge every |T|>L into one tail atom. Use the COMPLETE row reference r_i(T)=p_T+p_(T+i), not its conditioning on derivative support. Put D_i^L=D(C_L mu_i||C_L r_i) and M^L=sum_i e_i[log2(1/e_i)-D_i^L]. Data processing gives M^L>=M>=0.

For any fixed L>=0, let ell=L+2, let f_n be the n-bit one-point defect, n>=2, and take m=2^n disjoint copies. Put h=chi_Z f_n^tensor(m), and F=1+A_k(h-1), k=n, q=2^-n. Each seed-coordinate influence in h is e=2^(1-n), the seed influence total is ne, and I(F)=q(2n+ell+n). Every residual row carrying a core coefficient has degree >=ell-1>L. Thus for every seed coordinate C_L mu is concentrated on the tail. The complete reference tail mass is

    r_i(tail)=q+q^2 sum_{j=L+1}^k binom(k,j),
    D_i^L=log2(1/r_i(tail))<=k.

Hence the seed coordinates alone contribute at least q*2n*(n-1) to M^L. Other rows contribute nonnegatively. Therefore

    M^L(F)/I(F)>=2n(n-1)/(3n+ell)->infinity.

This is an actual Boolean, vanishing-influence family. Its genuine H/I is <4, and genuine M/I<=2. The point seed satisfies M/I=1-e+e log2(((1-e)^2+e^2)/e^2)<=1+2(n-1)e<=2; A096's exact transport pays the activation control M at <=2 times its influence. The entropy estimate follows from the explicit point spectrum and balanced activation spectrum, retaining all terminal entropy. No FEI counterexample is asserted.

The lost refund is inside the high-degree bucket. These coarse-grainings preserve their full normalizer but cannot pay a universal retained-KL bill. This excludes only a fixed bounded-degree inspection plus a single undifferentiated tail; it does not exclude adaptive deeper inspection, a structural tail reference, or the full signed Booleanity mechanism.

## Stronger unpadded full-support tensor witness

Fix L and take n>=max(6,2L+2), e=2^(1-n), m=2^floor(n/2), G_n=f_n^tensor(m). All Fourier coefficients are nonzero and all physical influences equal e. I(G_n)=mn e tends to zero, while H/I<4 and M/I<=2 by exact tensor additivity. No declared coordinates are dummies or independent parity factors.

For any row, split its residual set into the original seed block and m-1 spectator blocks. The row laws tensor as mu_seed times p_seed spectators, and r_seed times the SAME p_seed spectators. Probability of an individually inspected |T|<=L atom under mu is at most beta=e sum_{j=0}^L binom(n-1,j). On every occupied atom mu/r<=1/e, so the total low-atom KL contribution is at most beta(n-1).

The complete reference tail has probability at least the event that exactly one spectator block has degree >L and all other spectators are empty. Its mass is (m-1)z a^(m-2), where a=(1-e)^2 and z=e^2 sum_{j=L+1}^n binom(n,j). Since n>=2L+2, z>=e. Since n>=6, me<=1/4, (m-1)>=m/2, and a^(m-2)>=1-2e(m-2)>=1/2. Hence r_tail>=me/4=2^-(ceil(n/2)+1). The tail KL contribution is at most log2(1/r_tail)<=ceil(n/2)+1, even if its signed contribution is negative.

Thus every row has D_i^L<=beta(n-1)+ceil(n/2)+1, and

    M^L(G_n)/I(G_n)>=floor(n/2)-2-beta(n-1)->infinity.

For fixed L, beta(n-1) is an exponentially decaying polynomial in n. This stronger obstruction avoids the removable parity factor in the first witness and meets even vanishing-total-influence admission. The missing information is genuine within-tail conditional KL, not a missing normalizer.

Exact KL chain rule gives D_i-D_i^L=mu_i(tail) D(mu_i(.|tail)||r_i(.|tail)), since every other cell is a singleton. Consequently (M^L-M)/I >= floor(n/2)-4-beta(n-1) on the full-support tensor witness. A source-compatible quotient discarding only the independent spectator blocks has zero KL loss: the two row laws share the same spectator factor and their conditional seed likelihood ratio is unchanged. Absolute-degree merging instead erases the required seed likelihood ratios. This exact comparison is the intended next-reference guard.
