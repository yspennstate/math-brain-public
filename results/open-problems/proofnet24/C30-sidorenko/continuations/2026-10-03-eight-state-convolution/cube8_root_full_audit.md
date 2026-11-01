# Root audit of the full eight-state Boolean convolution theorem

2 October 2026 UTC. **PASS within the stated host family.** I read the full
proof and its final completion changes, complete K audit, all exact
generators and the failed-route research checkpoint. I reran the complete
coverage, rooted-label, forward-Walsh and independent fundamental-cycle /
inverse-Walsh / direct-multiplier routes. Every complete coefficient map
agrees. The proof resolves this restricted family, not general Sidorenko.
Historical novelty and external specialist review remain unverified.

## Analytic reduction

The source is ML10 with bipartite edges j-i in {0,1,-1} mod5. It has
ten vertices, fifteen edges and cycle rank six. With W(x,y)=8p_(x+y),
the edge density is s=sum p. Uniform averaging gives normalization 8^5
times the full label sum. Simultaneous translation in F2^3 preserves
every edge sum and has orbits of size eight; fixing one root is therefore
legitimate and gives the factor 8^6. This argument is specific to
translation-transitive convolution hosts and does not justify root fixing
for arbitrary regular kernels.

I checked affine invariance explicitly: transform one bipartition by A
and the other by A followed by b. Every edge color becomes A(x+y)+b.
Only AGL(3,2), not arbitrary permutations of eight colors, is used.
For aligned p(t,u)=a(u)+(-1)^t b(u) with a,b>=0, averaging source bits
annihilates precisely the selected-edge sets having an odd-degree vertex.
All remaining terms are nonnegative; the empty term is the pair-averaged
kernel. Its quotient normalization is 4q with q=2a and unchanged s.

On F2^2 every preference table on its two pairs is affine, so repeated
averaging proves the qualitative four-state bound for any bipartite
source. This is a standard expansion argument and a credited rederivation.
On F2^3 a four-pair preference table is affine iff its XOR parity is even.
Differences between linear transversals, and translations, flip an even
number of representatives. Thus the orientation test is compatible with
the actual affine symmetry.

The exhaustive coverage checks all 40,320 strict orders. Exactly 1,344
have odd orientation in every direction, and their entire set equals
one affine orbit. The independent ternary-law enumeration uses a
different transversal and reproduces the same set, not just its size.
Every other chamber follows by averaging to four states.

## Exact polynomial identity

The density polynomial has 89,168 host-weight terms. Its complete forward
Walsh transform has 3,964 Fourier terms and agrees with all 262,144 flows.
An independent fundamental-cycle basis on C10 with diameters reconstructs
the same Fourier polynomial and then reconstructs all host coefficients
through inverse Walsh butterflies. I read all loops, exponent encodings,
binomial coefficients, graph edges and normalizations before running them.

For the single exceptional descending order (3,5,6,7,4,2,1,0), increasing-
index shears give p_(o_i)=d_i+...+d7. The order of shears is essential.
The raw gap has 170,406 nonzero terms and 367 negative coefficients;
raw coefficient positivity is explicitly false. With L=d0+...+d6,
the full degree-17 identity L^2(F-s^15) has 345,312 strictly positive
integer coefficients. The independent route multiplies by seven square
terms and twenty-one cross terms rather than two successive L factors.
Both complete maps agree with the author Python and C++ generators.

For L>0 this identity proves the desired sign by division; for L=0 the
host is constant and equality is checked directly. The seven positive
pure-gap monomials give strictness on the exceptional nonconstant
chamber only; no global equality classification is claimed. Polynomial
continuity covers all ties, zeros and the zero host.

Packed exponent fields cannot carry at degrees fifteen or seventeen.
The full absolute-mass bound for relevant signed intermediates is
49*(2^90+36^15)<10^30<2^127. Thus the signed 128-bit calculations are
safe, and Python's independent maps use unbounded integers. No numerical
optimization is part of the certificate.

## Actual root runs and failed stronger claims

The root rebuilt all four C++ executables from the archived sources.
The rooted enumerator passed all 134,217,728 assignments; coverage passed
all 40,320 orders; the forward-Walsh check passed all 3,964 coefficients;
the independent reconstruction and complete map comparison passed every
density, raw-gap and multiplier coefficient. The minimum and maximum
certificate coefficients are 262143 and166970267349065400320.

The exact root obstruction script also reconstructs the coefficient-14
failure at p0=0,p_g=1/7: density688615849984/678223072849 and gap
-58807078/678223072849. It reconstructs the actual nonnegative four-state
host (1,1,3/2,0) whose individual character-block fifth trace is
-1351501/32768, while its normalized whole density is
7568741675008/4747561509943>1. Both are failures of stronger proof steps,
not Sidorenko counterexamples. The colored-cycle quartic coefficient
failure likewise obstructs coefficientwise positivity only; numerical
searches of the full colored coefficients remain evidence, not proof.

## Sources and limits

The primary Fox--Himwich--Mani--Zhou article (5 September2025) identifies
ML10 as a notorious general open case. Rossman's primary May2025 ladder
transfer is prior art. Zhao's even-subdivision and two-sided-correlation
papers do not imply this cubic signed-spectrum statement: their source
or spectral assumptions differ. These source checks do not certify that
the particular finite-host theorem is historically new.

The uniform eight-state Boolean convolution theorem, its complete exact
data and internal audits are now mathematically complete. Arbitrary
regular hosts, unequal host measures, larger Boolean groups, arbitrary
abelian groups and the unrestricted graphon conjecture remain outside
the theorem. No outside publication or contact is authorized or made.
