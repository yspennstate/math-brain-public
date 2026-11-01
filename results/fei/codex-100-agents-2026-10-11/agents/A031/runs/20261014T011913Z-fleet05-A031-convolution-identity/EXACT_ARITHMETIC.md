The checker imports the immutable A031 stage-3 rational logarithm kernel,
whose source path and hash are recorded in SOURCE_MANIFEST.json.
For a positive rational x, divide by powers of two until x is in[1,2).
With z=(x-1)/(x+1), z lies in[0,1/3]. The positive atanh series is
ln x=2 sum_(j>=0) z^(2j+1)/(2j+1). After40 terms its omitted tail is
between0 and2 z^81/[81(1-z^2)]. Divide the positive ln intervals by the
positive ln2 interval with directed endpoints, then add the extracted
integer power. Rational weighted sums use the sign of each coefficient
to choose endpoints. Certificate endpoints are rounded outward onto
denominator2^128. No floating-point logarithm or entropy decides a sign.

Truth-table validation uses signed integer Walsh transforms, direct
physical flip counts, exact Fraction normalization and likelihood ratios.
Large balanced tribes cases use exact signed factor formulas, not ambient
truth-table allocation. The independent degree review constructs exact
PGFs by Fraction convolution; it never supposes uniformity within degree.
