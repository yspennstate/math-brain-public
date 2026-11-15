# T170-LEAD-ROLLING-D15-001 v1: a rolling-window dimension15 candidate

Status: NOT ADMITTED. Requires two full independent exact-content reviews
on distinct accounts. This introduces a physical comparison and does not
inherit its correctness merely from prior Dhar profile audits. Priority
is unverified. No claim about lower dimensions or full T170 is made.

For independent Exp(1) undirected nearest-neighbor bond FPP on Z^15, with
axis and diagonal both normalized to Euclidean length1, the candidate is

 mu_axis <= 48279340039/549755813888
         < 88164156999/1000000000000 <= mu_diag.

The last inequality is a rounded-down consequence of the previously
audited w685 T170-C003 v2 chord5 diagonal certificate (retained premise,
not a new diagonal proof). Its exact data are chord5_exact_certificates.json,
SHA256 e78ecf283aa59fbfd46b237bcd5dc82d52335b8ff56cf2d56ca9be347a16d7af.
The submission manifest pins the proof and dependency bytes. Thus this
would prove a non-Euclidean-ball limit shape in dimension15 if admitted.

## 1. Finite horizontal rate lemma

Write m=14, C=512, f(n)=sum_{j=0}^{n-1}popcount(j), sigma(n)=28n-2f(n).
For every finite S subset Z^14 of size n<=C, its edge boundary has size
at least sigma(n)>0. The finite all-split inequality
f(a)+f(b)+min(a,b)<=f(a+b), a+b<=10000, is exhaustively certified by
T170_DISCRETE_RATE_RECEIPT.json (25million integer comparisons).
Split a hypercube set on its last coordinate: cross edges form a matching,
so dimension induction bounds its internal edges by f(n). Zero slices
are equality. Embed a lattice box isometrically into a binary hypercube
by replacing coordinate k by k leading ones followed by zeros. This
preserves exactly the unit edges. Counting degrees gives the asserted
boundary bound, including disconnected sets. See the pinned boundary
note for the full finite induction, not an unverified cited theorem.

## 2. Controlled graphical construction

Use independent rate1 Poisson clocks on undirected lattice edges. The full
infection process started from the origin has the Richardson generator,
hence the same infection-field law as Exp(1) undirected bond FPP. We build
a restricted process coupled inside it; unused rings are ignored.

Keep two consecutive slabs perpendicular to the first axis. Restricted
infected sets in them have counts (a,b) in {1,...,C}^2. No backward or
outside-window infections are allowed. If a<C choose uniformly sigma(a)
horizontal boundary edges in the first slab. If b<C choose uniformly
sigma(b) horizontal boundary edges in the second slab and max(a-b,0)
eligible forward edges from the first to the second. These exist because
at most b predecessor columns are occupied. All selected edges are
distinct. At a cap disable all births into that slab. In addition select
all b forward edges from the second slab into the empty next slab.

After each accepted event reselect uniformly using independent auxiliary
randomness. The selections are predictable after the previous event;
strong Markov memorylessness supplies fresh independent future clocks.
Their rates therefore depend only on counts, even if different selected
edges have the same target. A ring from either type of internal edge adds
one site. A ring into the next slab adds one site there, discards the
left slab permanently and shifts the window. Thus the count process has

 (a,b)->(a+1,b) at rate r_a=1_{a<C} sigma(a),
 (a,b)->(a,b+1) at rate r_b=1_{b<C}(sigma(b)+max(a-b,0)),
 (a,b)->(b,1) at rate b, with axial advance reward1.

The last event is counted even at (1,1), where it is a count self-event.
Every restricted infection is also present in the full coupled infection:
its selected edge rings with a restricted infected endpoint and a target
that either is already full-infected or becomes full-infected then.
Discarding a slab cannot invalidate this inclusion. This comparison is
of the full origin infection law and does not assert static edge weights
simultaneously for all possible starting sources.

## 3. Spatial regeneration and the directional bound

Construct a two-site canonical vertical string from the origin by a
single restricted forward infection; its finite startup cost is harmless.
Whenever counts are (1,1), the two sites form such a string: counts in a
retained slab never decrease, so the left singleton was already singleton
when the right singleton was born from its unique site. This proves the
geometry rather than inferring regeneration from a count-state label.

Define a cycle to end at the first accepted event returning to (1,1),
including a self front advance. At that event the geometry is canonical
up to translation. Future Poisson increments and selection randomness
are fresh, so cycles after translation are iid. Uniform edge selections
respect every transverse reflection, giving zero mean transverse cycle
displacement. All moments needed for the law of large numbers are finite:
total selected event rate is bounded by R=(4m+2)C=29696 and at least1;
two successive front advances return to (1,1) from every count state,
each with conditional probability at least1/R. Thus cycle event counts
have a geometric bound in pairs and cycle durations have finite mean.
The transverse anchor displacement is bounded by the number of accepted
horizontal births in the cycle. Axial advance A is positive on every
cycle and at most its event count.

Let T be cycle duration. The cycle law of large numbers gives return
positions per cycle tending to (E A,0,...,0), and time per cycle E T.
Full infection times at these actual points are bounded by controlled
times. The FPP shape theorem and continuity/homogeneity of its norm
therefore imply mu_axis<=E T/E A. This uses actual spatial regeneration,
not an unsupported identification of a first hyperplane hit with an axis.

## 4. Rational finite bias certificate

Let Lh=r_a(h(a+1,b)-h(a,b))+r_b(h(a,b+1)-h(a,b))
+b(h(b,1)-h(a,b)), omitting absent cap terms. The submitted 262144-entry
dyadic bias table has denominator2^40 and SHA256
8f1168cc2c921af711cd7ffe7690b067e2e6e5c8277c6aaa6ab0b943fbfa012b.
At every state the exact integer certificate is

 Lh+1-alpha*b<=0, alpha=48279340039/549755813888.

The self front event contributes zero to Lh but still contributes rate1
to the advance reward at (1,1). Boundedness of h on this finite state
space, integrability of cycle time and the compensator integral b dt for
advance counts justify stopped Dynkin/compensator formulas. Endpoint h
values cancel, giving E T-alpha E A<=0, hence the directional upper bound.

The bias was found by eliminating the acyclic births before each front
advance. The resulting C-state embedded chain K gives its mean holding
time vector t; stationarity gives alpha_est=pi*t, and a Poisson solve
(I-K+1*pi)h=t-alpha_est gives a trial bias. All floating point work is
discovery only. verify_t170_rolling_bias.py imports no solver/numpy/scipy,
reconstructs rates by explicit Q14 edges, and verifies every cleared
inequality with unbounded integers. A strictly lowered bound fails at a
tight state. Independent C=2 stationary and first-cycle calculations give
883/1709 and detect omission of the self advance reward. C=128 agrees
with the earlier distinct sparse-uniformization solver. These are lead
controls, not substitutes for the two required independent audits.

Open review targets: the adaptive clock coupling, exact canonical cycle
argument, reflection and shape-theorem passage, stopping justification,
boundary induction, every finite inequality, and retained diagonal scope.
