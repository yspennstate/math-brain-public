# Exact full-drift maximum: independent reconstruction

A072-EXACT-THREE-BIT-FULL-DRIFT-MAXIMUM@1 HOLDS unchanged. Its finite maximum
is 3 log2(3)-4. This is an independently checked finite certificate. Full FEI
remains OPEN; no all-dimensional upper bound follows from this census.

Fix a Boolean h on three sign inputs, a three-bit Boolean core g, and two
independent fresh dictator cores. For a query i inside g set q to the outer
pivotal probability, C=H(h(g,y1,y2))-q H(g), and d=Inf_i(g). Every entropy is
the Shannon entropy in bits of the complete squared Fourier spectrum.

Coverage is proved before evaluating the maximum. Relabeling the three physical
core coordinates puts i first. Permuting h's arguments puts the queried output
first; since every h is enumerated, this loses no gate or selected input. The
other two cores remain independent uniform dictators. Among the four remaining
core assignments, let (a,b,c,e) count the oriented output pairs (++,+-,-+,--).
These four nonnegative integers sum to four, giving exactly C(7,3)=35 profiles.
They give mu=(a-e)/4, t=(b-c)/4 and d=(b+c)/4. Every such profile is realizable:
place its indicated ordered pairs on the four edges along coordinate zero.

For completeness, the exact whole-row identity explains why arrangements of
the same profile cannot change the ratio. Write h=A+z D and let Ahat_W,Dhat_W
be their Fourier coefficients on the other two physical dictator bits. For
eta(v)=-v log2(v), eta(0)=0, define

 L(x,y)=eta(x²)+eta(y²)-[eta((x+y)²)+eta((x-y)²)]/2.

Restriction pairs coefficients across the queried coordinate; their full
entropy decrement is L. All scaling-log terms cancel, so L is homogeneous of
degree two. Every nonempty remaining-core-frequency row in h(g,y1,y2) is
Dhat_W times the corresponding inner row. These complete decrements cancel
against q times the inner entropy decrement, because sum Dhat_W²=q. The
exceptional empty-core row leaves exactly

 mean C_child-C_parent
   =q L(mu,t)-sum_W L(Ahat_W+mu Dhat_W,t Dhat_W).

Thus the full drift depends only on h,mu,t, while physical query influence is
q d. This proves the profile reduction, including constant and dummy queries,
without division by a zero influence or a variance. This algebra is independently
reconstructed here and in A074's preceding accepted A075 review; it does not
require the sharper A084 continuum coefficient or any FEI assumption.

There are 256*35=8960 representatives. The executable also maps all 256*3=768
literal core/query pairs to the 35 profiles and checks that every profile occurs.
Their multiplicities sum to 768. Together with three outer-slot choices and all
256 gates, the reduction covers 589824 literal queries before quotienting.
Exactly 240 gates have q>0 for a fixed selected slot and 30 profiles have d>0,
giving 7200 positive-influence representatives; the remaining 1760 have zero
influence and zero drift. There is no sign or complement quotient on profiles.

For each representative the new implementation constructs actual parent and
both complete child truth tables. It computes their FULL Fourier spectra by
bitset character counts on the negative set: if N is the table length and m its
negative-set size, W0=N-2m and Ws=-2(m-2*odd_negative_count(s)) for s nonzero.
This differs from the producer's exceptional-row/signature enumeration and FWHT
route. Every spectrum satisfies integer inverse identities and Parseval; physical
edge influence agrees with the squared-spectrum influence. Actual full entropy
differences compute drift directly rather than merely evaluating the row formula.

Let lambda=3 log2(3)-4. For each row the program computes the exact prime-log
profile of lambda*(q d)-drift. Clearing rational denominators turns its sign into
an integer product comparison. All 8960 profiles are nonnegative and 128
positive-influence representatives are exactly zero. The artifact auditor verifies
all keys and gaps, and independently certifies each of the 40 distinct gap forms
with rational logarithm intervals; symbolic zeros stay exact. These checks prove
the finite maximum, with no floating-point decisions.

The logarithm auditor uses 48 terms of the positive atanh series after dyadic
range reduction. For z in [0,1/3], the omitted tail is at most
2 z^97/[97(1-z²)]. The positive enclosure of ln2 converts natural-log bounds
to base two. Every nonzero gap has strictly positive lower bound at that fixed
precision. No unresolved sign is assigned a branch. Three deliberately forged
drifts above the maximum are rejected by this second arithmetic path.

The source's literal five-bit witness is also reconstructed. Take h negative
exactly at outer assignments 0,1,2 (mask7), insert g negative at core assignments
0,1 (mask3) in outer slot2, and query core coordinate1. Its physical truth mask
is 16579836, including its dummy physical bit0. Direct character sums, independent
of the bitset spectrum path, reproduce every source Walsh integer. With l=log2(3),
H(parent)=6-27l/16, H(g)=2, q=3/4, and the full child entropies are
4-9l/8 and 2. Both inner child entropies vanish. Therefore

 drift=9l/8-3/2,     Inf_query=3/8,     drift/Inf_query=3l-4.

The ratio exceeds 1/2, since 3 log2(3)>9/2 is equivalent to 9>8. This disproves
a proposed universal full-drift coefficient 1/2 on an actual Boolean composition.
The literal witness has bounded H/I and does not disprove FEI.

The finite certificate and its coverage argument are the achieved proof rung.
The guarded Lean attempt for the elementary integer sign returned
RUNTIME_UNVERIFIED; no Lean-checked statement or axiom audit is claimed.

First unsupported universal line: funding the INITIAL arbitrary-core bank or
rho_K from an absolute multiple of SAME unused original physical influence,
retaining old debit labels and both full terminals. The accepted finite lower
bound constrains possible local-drift shortcuts; it neither proves an upper
bound in arbitrary dimension nor supplies that initial owner.
