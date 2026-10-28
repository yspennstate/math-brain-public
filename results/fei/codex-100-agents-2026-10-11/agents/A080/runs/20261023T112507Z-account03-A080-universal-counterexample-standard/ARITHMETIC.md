# Checked logarithm enclosure

The exact helper uses GRID=2^384 and96 positive atanh-series terms. For
0<=z<=1/3, ln((1+z)/(1-z))=2 sum_(j>=0) z^(2j+1)/(2j+1).
The omitted positive tail is at most
2 z^193/[193(1-z^2)]<=9/(772*3^193), hence at most the conservative
9/(772*3^191) actually added. Integer fixed-point lower products and
quotients round down; upper products and quotients round up. Induction
therefore encloses every retained term, and the explicit tail encloses
the rest. LN is this enclosure at z=1/3, i.e. ln2.

For a positive rational spectral mass x<=1, the helper finds exact integer
k and rational y in[1,2) with x=2^k*y. Set z=(y-1)/(y+1). Then
log2 x=k+ln(y)/ln2; divide outward by positive LN, multiply by -x with
endpoints reversed, and round out to GRID. At x=0 use ell=0 exactly.
Every entropy is a finite sum of these rigorous intervals. Decimal values
are illustrations only and never determine a sign. In particular the
critical n3 sign has the separate integer-power certificate and independent
literal prime-log reconstruction in code/audit.py.
