# Linear order is necessary, even with primitivity and full support

This is an actual Boolean lower family for an ALL-relevant-coordinate price. It is not a positive high-K critical family or a disproof of FEI. All entropy is in bits.

For each odd integer k>=3 put R=2^k, L=R-1, m=L-k (even), d=2^-m, t=2^(-m/2), n=R, p=2^-n. Let H be the k by L binary matrix whose columns are all nonzero k-bit vectors. It has rank k, because it contains the unit columns. Its kernel C has dimension m and no nonzero vector of weight1 or2: its columns are distinct and nonzero. Take an m by L matrix A whose rows are any basis of C.

Let g(y)=(-1)^(y1*y2+y3*y4+...) on m bits; every coefficient is sigma_u*t, sigma_u=+1 or-1. There are c_+=(2^m+2^(m/2))/2 positive signs and c_-=(2^m-2^(m/2))/2 negative signs. Define the actual seed F(x,z)=g(Ax). Its full Fourier support is C with selector bit0, hence minimum distance at least3.

The fibre Ax=0 has exactly R points. First flip F on E={Ax=0,z=1}; then also flip the physical zero vertex (which is outside E). Call the result G*. It differs from F at exactly R+1 vertices. It is the pullback of the bent-selector function on the first edit, followed by one extra physical point flip.

At physical labels A^T u without z, G* has coefficient sigma_u*t-d-2p; at labels A^T u with z it has coefficient d-2p; everywhere else its coefficient is-2p. These groups give its FULL spectrum. They are all nonzero because d=2Rp, R>=8 and t<=1/4 imply d+2p=t^2(1+1/R)<t/2.

F has even negative count: each logical input has 2R preimages including z. The R+1 edits are odd, so G* has odd negative count. A product of Boolean functions on two nonempty disjoint coordinate sets has an even negative count, since it is a(2^v-b)+(2^u-a)b. Therefore G* has no nontrivial Boolean tensor factorization. Full Fourier support also makes every coordinate essential.

Query the ORIGINAL physical selector z. Before the last point edit its influence is d; the last edit removes one crossing edge, so the exact final influence is

    I_z=d-2p=d(1-1/R).

For every occupied seed Fourier row, a=sigma*t-d-2p, b=d-2p and q=a^2+b^2>=d/4. As b^2<=d^2, its off-anchor conditional entropy term is at least b^2(m-2). Summing all2^m occupied rows gives

    beta=2^m(d-2p)^2=d(1-1/R)^2,
    L_z=B_z+J_z >= beta(m-2),
    L_z/I_z >= (m-2)(1-1/R)
              =(R-k-3)(1-1/R).                 (1)

All other conditional-entropy contributions and the complete Jensen-Shannon term are nonnegative. This lower bound preserves the complete physical root and both terminal spectra in the exact identity; it creates no new bank and drops no negative terminal reserve.

Since the edit count is R+1 and k/R->0, the right side of(1) divided by R+1 tends to1. Thus no o(edit count) upper price can pay EVERY relevant coordinate of all these neighborhoods. The main37/4 times edit-count theorem has the correct order. Selection or genuine criticality must supply any further dimension-independent improvement.

The family is nevertheless FEI(3). Every nonzero row of the dual C-perp has weight2^(k-1)>=4, because half of all nonzero k-bit labels pair to1 with a fixed nonzero vector. Thus no unit vector belongs to C-perp and A has no zero column. Bent derivatives in any nonzero logical direction are balanced, so I(F)=(R-1)/2. Arbitrary R+1 vertex edits change total influence by at most2n(R+1)p=(R+1)d. Since d<=1/16,

    I(G*) >= (7R-9)/16.

Entropy is at most n=R; for R>=8, 3(7R-9)>=16R. Therefore H(G*)<=3I(G*). The displayed unpaid high-price coordinate does not make these roots critical at K>=3.

The shortest unpaid universal line remains a criticality-conditioned ORIGINAL block selection with sufficient independent unused release and the complete SAME terminal bank. This family explains why primitivity or full support alone cannot replace that condition.
