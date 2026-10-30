# Checkpoint: all-parameter statements being certified

For canonical lex f_n=-1 on index<floor(2^n/10), n>=5, the top three
coordinates minimize B_i/I_i. Their ratio is psi(2 floor(2^n/10)/2^n),
psi(d)=2-2d+Phi((1-d)^2,d^2)/d, and the limit is
(17 log2 17-56)/5 = 2.697373660... . The display decimal is not the certificate.

The unqualified assertion that t/2^n ->1/10 determines this minimum's
limit is false. Take m>=5, L=m^2, n=m+L, t=2^L floor(2^m/10)+1.
The newly relevant bottom coordinates minimize for all m>=5 and have
ratios in [2-2d0,2+d0(6L+8)], d0=2^(1-L). Thus their minimum tends to 2
although t/2^n ->1/10. Old-coordinate stability is proved by a binary
conditional-entropy continuity estimate, not by a numerical extrapolation.

For raw recursion F_0=x, F_d=f_5(F_(d-1),...,F_(d-1)) with disjoint
copies, f_5=-1 on numerical index<3, choose a bottom leaf whose ancestor
orbit path is T,B,T,B,... (T=one of the three high coordinates,
B=one of the two low coordinates). Its ratio is <3 for every depth.
This proves min_i B_i/I_i <3 in all dimensions 5^d; this mechanism
cannot cross 3.39 or supply an unbounded existential-erasure obstruction.

The exact bounded pilot (profiles.py) certifies all coordinate profiles
for n=5..24 on the canonical lex family, and all 2^d coordinate-orbit
paths for depths d=1..4 of the raw recursion. Full proofs, small-cube
independent validation, continuum scalar certificate, and protocol
handoff are being completed. No universal FEI theorem is asserted.
