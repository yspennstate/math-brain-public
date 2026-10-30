# Exact logarithm enclosure used by the validators

For a positive rational x, extract an integer e so m=x/2^e belongs to[1,2). Let z=(m-1)/(m+1), so0<=z<1/3. For L=16, the rational sum

    s=2 sum_(k=0)^(L-1) z^(2k+1)/(2k+1)

is a lower bound on ln m. The positive omitted tail is at most

    2 z^(2L+1)/[(2L+1)(1-z^2)],

by bounding every omitted denominator below by2L+1 and summing a geometric series. Apply the same enclosure to m=2 to enclose ln2 by positive rationals. Since ln m>=0, divide its lower numerator by the upper ln2, and its upper numerator by the lower ln2; adding e gives lower/upper log2 x bounds even when e<0. Rounding outward to multiples of2^-40 preserves the inequalities. Every cost coefficient is a nonnegative rational, so summing upper log bounds gives a rigorous cost upper bound. Lower bounds are used for the obstruction atom. No floating-point log or sign test is used; only wall-clock timings use floats.
