# T170-LEAD-ROLLING-D14-001 v1: three-slab dimension14 candidate

NOT ADMITTED. Two independent full exact-content reviews on distinct
accounts are required. New three-slab geometry and constructive finite
certificate need review; neither follows from a numeric pilot alone.
Priority unverified. Model: independent Exp(1) unoriented nearest-neighbor
bond FPP on Z^14, Euclidean length1 in both directions.

Proposed conclusion:

 mu_axis <= 49312208313/549755813888
         < 91464273436/1000000000000 <= mu_diag.

The diagonal inequality retains the audited w685 T170-C003v2 premise.
Its proof and exact DATA are pinned by the submission manifest; DATA
SHA256 e78ecf283aa59fbfd46b237bcd5dc82d52335b8ff56cf2d56ca9be347a16d7af.
The dimension14 DATA rational is rounded DOWN by integer division at10^12.
No new diagonal proof, lower dimension or full T170 claim is made.

## 1. Horizontal geometry and the controlled three-slab process

Set m=13, C=256, S=2^40, f(n)=sum_{j<n}popcount(j), sigma(n)=26n-2f(n).
For any finite subset of Z^13 of size n<=C, its horizontal edge boundary
is at least sigma(n)>0. Indeed the pinned all-split certificate verifies
f(a)+f(b)+min(a,b)<=f(a+b) for a+b<=10000. Induction on ambient binary
cube dimension bounds internal edges by f(n), including empty split sides.
The unary embedding of a finite lattice box preserves its full L1 metric
as Hamming distance, hence its induced unit edges. Original lattice degree
26 then gives26n-2f(n). The full elementary proof and finite integer
certificate are submission subjects; disconnected sets are included.

Use independent rate1 Poisson clocks on UNDIRECTED lattice edges. Full
origin infection crossing every ringing infected-to-uninfected edge has
the same generator and infection-field law as Exp(1) bond FPP. It is
nonexplosive on this finite-degree graph. Couple a restricted process
inside it, ignoring unused rings and restricting movement to three
consecutive slabs in the first coordinate direction.

Let their restricted infected counts be(a,b,c) in{1,...,C}^3. Below the
respective cap choose uniformly sigma(count) horizontal boundary edges.
Into the middle slab additionally choose max(a-b,0) eligible forward
edges, and into the right slab choose max(b-c,0). At a cap disable all
births into that slab. Such forward edges exist because at most the
receiving count's columns can already be occupied. Finally keep all c
forward edges into the next, restricted-empty slab. All these edge sets
are disjoint. Distinct edges sharing a target contribute additive rates;
simultaneous rings have probability zero.

After each accepted event choose fresh subsets with independent auxiliary
randomness without inspecting future clocks. Poisson strong Markov gives
the following exact count event rates, regardless of geometry:

 r_a=1_{a<C}sigma(a),
 r_b=1_{b<C}[sigma(b)+max(a-b,0)],
 r_c=1_{c<C}[sigma(c)+max(b-c,0)],
 r_front=c.

Births increase the indicated count by1. A front event sends(a,b,c) to
(b,c,1), discarding the left slab permanently, and advances the window
axially by1. Count self-events at(1,1,1) are retained as reward events.
Full infection dominates every restricted infection at every accepted
event. Previously ignored rings and previously full-infected targets do
not obstruct this comparison: all Poisson clocks continue indefinitely.
No static edge environment for all restarted sources is being asserted.

## 2. Spatial regeneration and conversion to the directional norm

Start from a canonical three-site vertical string using two restricted
forward infections from the origin, at finite startup cost. At any later
state(1,1,1), all three sites are aligned: a retained slab's count never
decreases, so its singleton was already singleton when its successor
singleton was born through a vertical edge. Apply this successively to
the left/middle and middle/right pairs. Thus the count reset entails an
actual canonical spatial configuration, not just a count-state label.

End a cycle at the first accepted event returning to(1,1,1), including a
self front event and excluding time zero. Translated cycles are iid by
Poisson strong Markov and fresh choices; neither discarded sites nor the
full infection state enters the restricted rule. Uniform choices respect
every transverse reflection, so mean transverse displacement is zero.

Total accepted rate is at least1 and at most R=(6m+3)C=20736. Three
successive front events return to(1,1,1) from every state, each with
conditional probability at least1/R. Cycle event count N therefore has
a geometric tail in blocks of3. Holding-time conditional means are at
most1, so E T<=E N<infinity. Axial reward A is positive each cycle and
at most N. Anchor transverse displacement is bounded by horizontal births
in that cycle and hence by N. These facts justify integrability and the
cycle law of large numbers. Actual return anchors per cycle tend to
(E A)e1 and controlled times per cycle to E T. Full infection reaches
each anchor by that time. The uniform outer FPP shape theorem, norm
continuity/homogeneity, and vanishing startup costs imply

 mu_axis <= E T/E A.

This uses actual spatial points and no decreasing-increment conjecture.

## 3. Compact exact definition of all16,777,216 bias values

The BASE JSON stores65536 signed integer values H[a,b], ascending index
(a-1)C+(b-1), SHA256
884c5412e7d1418a02a952674cc12a415aa3e777e4fcdaf53cd1144e593c3079.
It also fixes A0=98624416626. All values below are integer bias units;
physical h is their value divided by S. Set h[a,b,1]=H[a,b].

For a,b descending C..1 and c descending C..2, define uniquely

 h[a,b,c] = ceil((S+r_a*h[a+1,b,c]+r_b*h[a,b+1,c]
                    +r_c*h[a,b,c+1]+c*(H[b,c]-A0))
                   /(r_a+r_b+r_c+c)),

omitting zero-rate child terms at caps. Each dependency has already been
defined in this descending order; a single previous a-slice suffices.
This constructive recipe, not an implicit linear equation or a floating
table, specifies every h. Discovery of H and A0 used floating point; the
resulting stored integers are arbitrary exact input data for this check.

For every c>=2 the defining ceiling gives

 Lh+S-A0*c<=0,

where L uses the four displayed event rates, including the front child
h[b,c,1]=H[b,c]. For c=1 the finite checker verifies the same inequality
directly. Its maximum required coefficient across ALL65536 base states
is98624394809, strictly below A0. All16,711,680 interior inequalities
hold, with minimum cleared ceiling slack0. Thus EVERY state satisfies

 L(h/S)+1-alpha*c<=0, alpha=A0/S=49312208313/549755813888.

Native check_three_compressed.cpp and separate standard-library Python
verify_three_compressed_python.py independently reconstruct ALL2^24
values and inequalities from the base. The latter uses unbounded integers
and agrees exactly. Both source/input identities are pinned. All h units
lie in[-S,S]. The native signed64 arithmetic is also safe: total rate
<=20736, so every intermediate numerator has absolute value at most
(1+20736+256)S<2^55; direct base difference sums are below2^56.
Signed integer ceiling is implemented correctly for negative numerators.

Independent8-state Fraction stationary and first-return calculations at
C=2 validate the three-slab generator and reward convention. Omitting
the self front reward changes the exact ratio and is detected. A separate
fault check reconstructs an actual base row and rejects a coefficient
below that row's requirement. The first Python replay's scalar fault
boolean was only an algebra check; the supplementary actual-row receipt
is explicitly bound, without changing the valid full replay or its bytes.

## 4. Bias-to-speed implication and scope

The constructed h is bounded on the finite state space. Dynkin's formula
stopped at cycle end intersect time t passes to cycle end because Lh is
bounded and E T finite; endpoint h values cancel. The front reward has
predictable intensity c, including the self event. Its compensator gives
E A=E integral_0^T c_s ds. Integrating the all-state inequality yields
E T-alpha E A<=0. Together with Section2 this proves the proposed axis
bound; the retained diagonal inequality gives the strict nonball claim.

Two full distinct-account audits are still required before admission,
including the three-slab canonical geometry, adaptive coupling, stopping,
shape passage, compact bias recurrence, every base/interior check and
diagonal normalization. No priority or global optimality is asserted.
