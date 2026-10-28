# Independent reconstruction of A032 product-branch mass rigidity

Verdict: HOLDS at the exact stated scope of A032-PRODUCT-BRANCH-MASS-RIGIDITY@1.
This is a paper proof reconstruction, with exact finite checks supplied separately;
the full Fourier theorem is not claimed Lean-checked.

For Boolean g(z,y), the partial rows a=(g_++g_-)/2 and b=(g_+-g_-)/2
are ternary, satisfy ab=0 and a^2+b^2=1, and have masses summing to one.
For any positive ternary row with coordinate-product squared Walsh spectrum,
remove deterministic frequency coordinates by multiplying by their character
and deleting now-unused physical variables. On the remaining frequency face,
all Walsh coefficients are nonzero integers and their absolute ratios along
each coordinate are rational and independent of the other coordinates.
Writing each ratio in coprime positive integers gives magnitudes
c times a tensor of primitive integer pairs. That tensor has gcd one: for
each prime choose, independently at each coordinate, an entry not divisible
by the prime. Thus c is an integer. Every odd divisor of c divides every
inverse Walsh value since its denominator is a power of two. A nonzero
ternary row has a value of absolute value one, so c is a power of two.

Parseval now says 2^d k=c^2 product_i(A_i^2+B_i^2), k the support count.
For opposite-parity primitive pairs the sum of squares is 1 mod 4; for
two odd entries it is 2 mod 8 and its odd part is 1 mod 4. Therefore the
reduced numerator of the positive dyadic mass k/2^d is 1 mod 4.

Two positive such masses adding to one must both equal 1/2. Equal reduced
denominator exponents >=2 give 1+1=0 mod 4. Unequal exponents give an odd
left numerator (or, more precisely, residues 3 or 1 mod 4) against a
multiple of four. The only remaining exponent is one. A mass 1/2 has
odd support-count part one, hence all primitive pairs have odd sum-of-squares
part one. Coprimality forces each pair to be (1,1): an opposite-parity pair
has sum at least five; a nonconstant odd pair has half-sum at least five.
The same argument handles the single positive mass one. The varying
conditional marginals are consequently fair in every dimension and for
every possible signing. Fixed-one characters merely increase influence.

With two positive branches of fair counts m_0,m_1 and mean degrees d_0,d_1,
H(g)=1+(m_0+m_1)/2 and I(g)=1/2+(d_0+d_1)/2, where d_i>=m_i/2.
Thus H(g)<=2I(g). If one branch is absent use its sole fair count and
include any deterministic z-frequency in influence. No physical restriction
closure and no generic real-amplitude theorem follows.

Potential failure checks: zero rows; deterministic frequency labels; rational
primitive factors and gcd; lost powers of two in Parseval; unequal reduced
denominators; non-Boolean normalized amplitudes; arbitrary seed admission.
The finite checker audits all ternary tables through three bits and reduced
dyadic masses through denominator 2^10. The proof above, rather than that
bounded audit, establishes the all-dimensional modular conclusion.

This consumes and supersedes the unequal-mass two-product NEXT in A079
stage5: the requested unequal-mass extension is impossible. A single product
branch with mass 5/8 is permitted; its mass 3/8 complement is forced outside
the product class. This is precisely where the next scope guard applies.
