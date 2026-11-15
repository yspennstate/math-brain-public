# T170-LEAD-ROLLING-D15-001 v1: PASS, mathematical correctness

Kind: audit. T170 targets3 (new upper comparison) and4 (dimension15).
Exact proof SHA256: `3c4be1f9744c50269c26b83c4ab01751680e2c4665bef6be0bbe25ac3268dd23`. Source `~\crash_recovery_20261014\workers_1015\term_362ebe34\T170-LEAD-ROLLING-D15-001_v1.md`. Checked 2026-10-15T18:27:50.659148+03:00.
Actual execution account4 at start and finish; same account as author lead.
This is a mathematical crosscheck, NOT a second distinct-account admission.
No claim of literature priority, lower dimensions, or the full conjecture.

## Statement and pinned premises

For independent Exp(1) unoriented nearest-neighbor bond FPP on Z15, in
Euclidean units in each direction, the proof correctly establishes

mu_axis <= 48279340039/549755813888
        < 88164156999/1000000000000 <= mu_diag.

The strict gap is 46244591732093897/134217728000000000000. Therefore the
limit shape is not a Euclidean ball, conditional on the retained audited
chord5 diagonal premise. This is bond FPP/Richardson growth, not a claim
about every process that has been called Eden.

Every one of the17 submission artifact hashes and all5 dependency hashes
was independently compared with actual bytes. Author programs were NOT
imported, executed, or copied to produce our checker. The own integer
checker was written from Sections1 and4 of the mathematical proof. The
manifest also lists old Dhar/C004/C007 audits: those are provenance, not
a justification for this new physical comparison. Sections2-3 are checked
afresh below. The diagonal data SHA is
e78ecf283aa59fbfd46b237bcd5dc82d52335b8ff56cf2d56ca9be347a16d7af;
proof SHA 9a0d7617781f2496d2e1fc3cae58ee718b3878198d47102262715b6678b7de96.
The retained data row d15 is ALREADY in Euclidean units. Its exact rational
is at least the submitted floor, independently verified with Fraction.
It must not be divided by sqrt15 again. No new check of its1778 vectors
is claimed; it is the explicitly accepted previously checked premise.

## Section1: finite boundary lemma

For n<=512, our checker counts edges directly in the binary initial
segment of Q14 by testing every vertex and each of14 flipped coordinates.
It counts each internal edge once, and verifies this count equals
f(n)=sum_(j<n)popcount(j). The resulting rates are 28n-2f(n)>0.
All65536 positive splits n<=512,1<=b<=floor(n/2) are checked with integers,
with minimum slack0; zero splits are identities, and symmetry covers the
others. The stronger prior independent25million-split receipt for n<=10000
is available in checks/t170_d16_boundary_own.json and was not rerun.

The mathematical induction is on arbitrary hypercube dimension, not14:
two slices with cardinalities a,b have at most f(a)+f(b) internal edges,
and their cross edges form a matching of size at most min(a,b). Thus the
checked split inequality proves the bound for every Q_D set of size<=512.
Base dimension0 and empty slices hold. For a finite Z14 set, translate
into a box and replace each coordinate by its unary string. Hamming
distance equals lattice L1 distance, so unit edges are preserved exactly.
This transfers an INTERNAL-edge bound; the boundary is then computed in
the original lattice of degree28, not in the embedding cube. Hence the
lemma holds for arbitrary disconnected shapes too. Binary initial
segments attain the internal count in14 coordinates; attainment is not
needed for the lower-rate construction. There is no floating point or
unchecked citation in this boundary proof.

## Section2: the two coupled laws and pathwise inclusion

Full process: independent rate1 clocks on unoriented nearest-neighbor
edges; at a ring with exactly one infected endpoint infect the other.
Given any finite infected set its boundary edges have independent residual
Exp(1) clocks, giving the Richardson generator with rate equal to the
number of infected neighbors at each uninfected vertex. This is the same
origin infection-field law as independent static Exp(1) bond FPP: on an
edge's first exposure its unused residual passage time is fresh Exp(1);
memorylessness gives exactly that generator until the target is infected.
No assertion is needed about simultaneous static metrics from all seeds.

Restricted process: keep only its own infected sets in the two slabs,
and use the SAME edge rings, ignoring all rings outside its selected
edges. Its selection depends only on its geometry and independent fresh
auxiliary randomness, not on full-process infection status. The finite
boundary lemma supplies at least sigma(a),sigma(b) horizontal edges.
There are at least max(a-b,0) forward edges into unoccupied columns of
the second slab, since at most b predecessor columns can be occupied.
All b forward edges into the entirely new third slab exist. The first
and second horizontal families and the two forward families consist of
distinct edges. Shared TARGETS within a family do not change the total
rate: simultaneous rings have probability0, and the first ring adds one
site and causes immediate reselection. Disabled cap terms are exactly0.

Selections are made after an accepted event and used on the next open
time interval, so they are predictable. Strong Markov independence of
future Poisson increments and fresh auxiliary draws justifies reselection
even for edges previously ignored. Thus every realized geometry with
counts(a,b) has the rates printed in the proof. Geometry can affect which
site is born but cannot affect the count transition rates. At(a,b)=(1,1)
a front event changes the physical window but not its count label;
retaining this event and its reward is essential.

Pathwise induction proves inclusion in the full process: a selected ring
starts at a restricted infected point, hence at a full infected point.
Its target is either already full infected or becomes infected by that
ring. Removing the left slab removes restricted points and cannot break
inclusion. This proves precisely the comparison used; it does not assert
an arbitrary pathwise comparison of FPP metrics under independent seeds.

## Section3: canonical spatial regeneration, integrability, and axis

A single allowed initial forward infection gives the vertical two-site
string. Startup waiting time is finite. Between shifts counts only
increase; a return to(1,1) can only occur at a front shift (including a
self shift). Immediately before that shift the right slab has ONE point
x. Immediately afterwards it is the unique retained left point, and
the new right point is x+e1. Therefore EVERY return has the identical
aligned geometry up to translation. This also directly verifies the
proof's monotonic-singleton explanation without assuming that a count
label alone determines geometry.

Use first accepted return, not the count generator's first strict jump.
The two-step sequence of front advances sends any(a,b) to(b,1), then to
(1,1). If an earlier return terminates the cycle, that only helps the
tail bound. Total accepted rate is <=(4m+2)C=29696 and >=1; each specified
front event has conditional probability >=1/29696. Thus the cycle event
count has a geometric tail in pairs. Conditional holding means are <=1,
so cycle duration has finite mean; cycle axial advance is between1 and
the number of accepted events. Its transverse anchor displacement has
absolute L1 norm bounded by the number of horizontal births: the new
anchor is connected genealogically to the starting string by accepted
birth edges; forward edges have zero transverse displacement. All first
moments used in the proof therefore exist. The chain's finite rates also
exclude explosion.

Return times are stopping times for the full clock/auxiliary filtration.
Strong Markov independence and translation invariance give iid cycles
after translation, even if the full process already has other infected
sites nearby: the restricted rule ignores those sites. Uniform subset
selection is equivariant under each transverse reflection, the canonical
string is reflection invariant, and return events and cycle lengths
respect those reflections. Hence each integrable transverse displacement
has mean0. No reflection in the forward axis is assumed.

Let X_j be the retained left point after j cycles, S_j the controlled
time, A the axial advance and T the duration in a cycle. The iid law of
large numbers gives X_j/j -> E[A]e1 and S_j/j -> E[T], with E[A]>0.
The full infection time at X_j is <=S_j by the proven inclusion. The FPP
shape theorem applies uniformly to random lattice points with this linear
growth; Exp(1) has all required moments and zero mass at0. The continuous
homogeneous deterministic norm therefore gives
T_full(X_j)/j -> mu(E[A]e1)=E[A]mu_axis. Consequently
mu_axis<=E[T]/E[A]. This is an axis bound via actual point displacements,
not an unjustified identification of a first hyperplane hit with an axis.

## Section4: exact certificate and stopped identities

Our own checks/t170_d15_rolling_own.py reconstructs all512 boundary rates
by direct Q14 edge counts, not by reading author rate tables. It reads
the frozen dyadic bias DATA and checks all262144 entries are integers in
the specified row order. Scale S=2^40, alpha*S=96558680078 exactly.
At every(a,b), the checker constructs the three rates from Section2,
omits cap terms, and evaluates the CLEARED integer expression

ra(H[a+1,b]-H[a,b])+rb(H[a,b+1]-H[a,b])
 +b(H[b,1]-H[a,b])+S-96558680078*b.

All262144 values are <=0. Maximum0 at(423,1). Lowering alpha by1/S makes
that inequality fail, an independent sign/scaling negative control.
No floating point enters this verification; discovery's stationary solve
is irrelevant. Our receipt records the minimum, maximum, rates and hashes.
This checks the actual inequalities, not an assertion that author code
reported PASS. It does not claim a fresh independent discovery of H.

As a separate model control, exact Fraction Gaussian elimination for the
four cap2 states computes the stationary law and also solves the killed
first-return equations, including the self front return at(1,1). Both
routes give E[T]/E[A]=883/1709. Omitting that self reward gives a different
ratio, detected by an explicit negative control. The cap2 test diagnoses
conventions; the all512 proof is the full inequality check plus coupling.

On the finite count space h is bounded and Lh is bounded. For the cycle
time T, stop first at T wedge n. Dynkin's formula applies, and bounded h
plus E[T]<infinity permits dominated convergence for h and the integral
of Lh. The front counting process, INCLUDING count self events, has
intensity b<=512. Its stopped compensator identity gives E[A]=E[int b dt];
the integrals are dominated by512T and the stopped counts increase to A.
Both endpoints have count(1,1), hence the h expectations cancel. Integrate
Lh+1-alpha*b<=0 to obtain E[T]-alpha E[A]<=0. This justifies stopping and
the ratio, rather than relying on a numerical stationary distribution.

## Literature, independence, and conclusion

Primary BP arXiv:1705.08143v2, Theorem1 and Sections2-3, was already
checked for the dimension22 profile architecture and its unproved
increment-monotonicity remark. Kumar-Dhar arXiv:1909.12001v1 was also read
for IBP1/IBP2 diagonal estimates. Our D16 source/citing-paper screen and
the primary sources remain the same-day context. Additional bounded
arXiv title/object queries for rolling windows, Markov chains/regeneration,
Dhar/Eden/anisotropy and the last90days returned no entries. The closest
BP OpenAlex citation screen returned Kumar-Dhar and the lattice chase
paper; these finite index searches do NOT establish global novelty.
See checks/t170_rolling_literature_own.json and checks/t170_d16_literature_own.json.

Brain recall top3 supplied no relevant graphical-coupling or regeneration
lemma; it is logged honestly in BRAIN_USE.jsonl and no test memory was
opened. The physical comparison is derived above. No defective step or
missing hypothesis remains in this exact proof version. PASS is solely
mathematical correctness conditional on the explicitly accepted diagonal
premise. Actual account4 author/auditor identity means this does not
satisfy a distinct-account admission by itself. No ledger was edited.
