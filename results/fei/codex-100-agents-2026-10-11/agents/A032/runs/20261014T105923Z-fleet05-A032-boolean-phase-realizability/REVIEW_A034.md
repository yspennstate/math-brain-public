# Independent reconstruction of A034-ALL-PRODUCT-ROW-PAYMENT version1

Verdict: HOLDS at the stated two-address, arbitrary data dimension, product-row
scope. Reviewer A032; no repair supplied. Source: A034 run20261014T055220Z,
PROOF.md sections1--6. This consumes the proof gap correction: the withdrawn
coupled-gcd clause is not a dependency. Review is analytical, not a new census.

The gcd of a coprime product magnitude tensor is1. Raw integer Walsh entries
therefore give integer scale c, whose odd divisors would divide every height-two
physical value. Since a nonzero value has magnitude1 or2, c is a power of two.
Consequently oddpart(k) is precisely the product of the primitive norm odd parts,
and each nonfair factor is at least5. The bound5^N<=4*2^(N+m) excludes m<N
for N>=4 by625>512. The only remaining endpoints are(1,0),(2,1),(3,2).

For(2,1) k=25, the physical height counts force one magnitude1, six magnitude2,
one zero. The two raw primitive possibilities are both(1,2),c=2 or both(1,3),c=1.
The signed full-parity square sum is -3t-4z=+/-1 or+/-7. Full-complement Walsh
convolution equals8 times that sum. Every product term is a multiple of16 in
the first case and9 in the second, contradicting the listed signed sums.
For(3,2), k=125 forces one magnitude1 and31 magnitude2; raw Walsh entries are
odd, so all three pairs are(1,3),c=1. The same convolution requires27|96,
impossible. These are exact all-phase exclusions; neither uses the earlier gcd gap.

For(1,0) the two physical values have magnitudes1 and2 and frequency odds3:1.
The heavy row has mass5/8 and its common mixed half cube forces three companions
of mass1/8, supported exactly on that half cube. Their norms have odd part1, so
all varying marginals are fair. Each companion has at least one fair coordinate
from that half-cube support. Writing e=sum(d_J-1)/16 gives I_Y>=1/4+e and
H_Y|X=Kcond/4+2e. Since Kcond>5/2>2, this pays all companion entropy without
resetting a bank. The mixed half cube contributes at least1/2 to I_X. Directly
H(F)=4-(9/8)log2(3)+2e, which is paid by Kall>6 using I>=3/4+e.

For regular rows m>=N and a>=m/2+sum q_i. Gibbs at5/2 has constant<1/4:
(1+1/(4sqrt2))^2=33/32+sqrt2/4<sqrt2 iff sqrt2>11/8, and121<128.
Thus H(p)<=2.5a. The exceptional Kcond dominates2.5; the source's exact bounds
5^10>2^23 and3^5<2^8 give h2(.1)>21/50. Gibbs at6 and R<=m+N give
H+R<=(6+2log2(65/64))a: the residual is(1+log2(65/64))(m-N)+2log2(65/64)sum q_i>=0.

Finally, reconstruct the full address ledger from physical heights. At each data
point the four rows are one magnitude2 or four magnitudes1. The mixed set has
density delta<=I_X. A pure-point row satisfies log(1/w)<=R by inverse Walsh
triangle; a mixed-only row satisfies log(1/w)<=R+2. The mixed-only total mass
is at most delta, hence H(w)<=sum wR+2I_X. This retains H_Y|X in full and pays
H(F)<=Kall I(F). The exceptional rows are handled by the previous exact ledger.
Regular rows give Q<=2I_Y, the exceptional ledger gives Q<=2.5I_Y sharply.
Kall<7 follows65^2<2*64^2. No universal Renyi/I or address-only Q bound is used.

Tensor seeds admitted by product-row spectra must themselves have product Boolean
spectrum; their norm odd part is1, so they are fair. Their entire entropy and
physical influence add and are paid. The actual three-bit point defect is admitted
and sharp for conditional Kcond; the normalized non-Boolean control with marginal
1/256 has H/I>8 and is excluded by integer height. General nonproduct rows,
arbitrary tensor seeds, Q paid solely by address entropy, and full FEI remain open.
