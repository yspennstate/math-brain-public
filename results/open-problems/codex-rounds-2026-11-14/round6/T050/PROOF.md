# A phase-uniform estimate for the two-wall link field

## Assumptions and statement

Let v,w be linearly independent planar vectors. Use the maximum norm in
this basis, denoted by ||.||_*. Fix

    0 < s < 1/10,  r=s/1000,
    A=v+sw,  B=w+sv,  d=1-s^2.

Positions lie on a scaled square lattice. Edge weights are positive, iid,
and have finite mean. Costs count traversal multiplicity and fractions of
edges. There is a random potential P, affine on physical edges, such that,
for a deterministic linear functional f and every physical path gamma,

    Q(gamma)=cost(gamma)-f(end-start),
    D(gamma)=Q(gamma)-P(end)+P(start) >= 0.             (1)

Assume integrability of P at vertices. No locality of P is assumed.
The potential is defined from the edge field and a calibration extension,
without using road phases or private road inputs.

There are A- and B-road rules with the following properties. Each road is
a two-sided lattice walk with a continuous nondecreasing nominal
parameter tending to the respective infinities at its ends. Every compact
nominal interval has finitely many edge occurrences, including pause
records. Each road tracks its nominal line to error r and is determined
on each deterministic parameter interval by product inputs within
||.||_*-distance 10 of that interval's nominal segment. The first occurrence
of each marked level specifies its cut; a pause at a marked integer belongs
to the following period. Every marked period has expected defect at most
beta. The same bound holds for each translated road and every fixed phase
used below. Road periods have integrable physical cost.

Private inputs are independent primitive coordinates with deterministic
spatial locations, independent of the edge field and of the calibration's
extra randomness. Locality refers to these primitive coordinates, including
private completions. In particular, there is no common random mesh offset
or common private seed required at distant spatial locations.

Let F be any finite subgroup of R/Z. All its elements are represented in
[0,1). On the nominal line jA+RB place a B-road W_j with independent
uniform phase phi_j in F, independent of all spatial inputs. Its marked
levels relative to jA are phi_j+Z. For every a in F place auxiliary A-roads
on the lines iB+aB+RA, i in Z, with deterministic longitudinal phases and
spatial private inputs. All required displacements are lattice translations;
this is a divisibility restriction on the lattice scale. The lattice scale
is also large enough that every edge has (A,B)-coordinate length at most
2r. Uniform period bounds are understood conditional on the wall phases.

In the basis (v,B), write a point as uv+yB. Then A=(d,s), B=(0,1).
Fix any deterministic row height h. Put

    b=s/50,  b'=s/20,  delta=b+2r,
    Z_j=jd v+h B,       t_j=h-js.

A link competitor is a physical path from W_j to W_(j+1), with specified
endpoint occurrences, contained in the closed rectangle

    |y-h| <= b,     jd-b' <= u <= (j+1)d+b',           (2)

and with horizontal drawdown at most b': later points have horizontal
coordinate at least an earlier point's coordinate minus b'. Closed lattice
padding may be used, provided it is contained in (2). Equivalently one may
fix sufficiently divisible rational boundaries. Let c_j be the first
occurrence on W_j with nominal parameter t_j.

There are local anchor gauges, obtained from the round-4 finite-cell
construction and averaged over F, with the following property. Interpolate
these gauges on the roads as in (9) below. For a competitor gamma from
occurrence x on W_j to occurrence y on W_(j+1), set

    L(gamma)=Q_j(c_j,x)+Q(gamma)+Q_(j+1)(y,c_(j+1))
                         -g_(j+1)(c_(j+1))+g_j(c_j). (3)

The two road costs in (3) are signed costs in occurrence order, rather
than physical backward travel. Let X_(j,h) be the infimum of (3) over the
band-and-drawdown competitors just described. Further closed restrictions
are allowed if they are preserved by loop deletion and have a finite
continuous constraint description on each simple route type. If the family
is empty, use a no-path symbol with negative part zero. Then, conditional
on every fixed assignment of wall phases,

    E X_(j,h)^- <= (24+147 C_(2,40)) beta,             (4)

where C_(2,40) is the explicit finite constant in the round-4 theorem.
It is independent of F, the row mesh, s, the scale, and the road rules.
Here and below expectations with fixed phases integrate spatial inputs
and calibration randomness only.

The observable X_(j,h) uses only primitive spatial inputs within radius
408 of Z_j in ||.||_*, and wall phases with indices in

    {j,j+1,...,j+244}.                                (5)

Thus, for any countable set of deterministic row heights, entire-column
sigma-fields at indices in one residue class modulo 2000 are mutually
independent. The column includes all those rows. No supremum over the
rows or over possible phase assignments is asserted in (4).

The constant is deliberately generous. The claim is an auxiliary link
estimate under (1) and the road assumptions, not strict convexity.

## 1. Uniform local comparisons

Fix the phases and an offset a. In (A,B) coordinates the comparison mesh
has nominal points (i,k+a). Put an A-road on each horizontal mesh line
and use W_i on its vertical line. Coordinate conversion from ||.||_* to
(A,B) maximum coordinates has norm 1/(1-s)<2. Write epsilon_r=2r.
Each road stays within epsilon_r of its nominal position.

Near (i,k+a), inspect the two incident roads in nominal windows of
half-width 4 epsilon_r. Their subarcs crossing the small square from left
to right and from bottom to top meet, by the planar rectangle-crossing
property. One proof erases loops in the first arc, joins its endpoints
outside the square, and applies the Jordan curve theorem to the second.
At an intersection both coordinates differ from the nominal crossing by
at most epsilon_r. If the intersection is in a shared edge, a neighboring
vertex differs by at most one edge, hence at most epsilon_r. At that
vertex the nominal parameters on the two roads differ from the nominal
crossing parameters by at most 3 epsilon_r. It remains inside the
inspected windows. Select the first eligible vertex occurrence on the
A-road, and then the first eligible occurrence on the B-road. Denote
this reference vertex by X_(i,k)^a.

The selection uses only the two inspected records. All records are finite.
In particular the reference anchor uses phase phi_i and no other wall
phase. Since 8 epsilon_r<1, the inspected intervals at neighboring
crossings are disjoint and ordered along each road.

Additional anchors at mesh site z=(i,k) may be any first occurrence on W_i
at nominal level k+a+lambda, |lambda|<=1/2. Include the reference anchor
as the distinguished label 0; tag the cut labels separately, so a cut
with lambda=0 is not confused with the reference label. It suffices to
keep the countable set of labels needed for the stated rows, phases,
offsets and integer marks.
All statements about versions can consequently be made simultaneously.

The signed B-road trip between an additional anchor and the reference
anchor has nominal length at most

    1/2+3 epsilon_r < 1.

The whole deterministic interval between the fixed cut level and the
reference parameter window of half-width 3 epsilon_r has length less
than one. It is enclosed in
at most two fixed complete marked B-periods. Between reference
anchors at neighboring mesh sites, the A- or B-road interval has nominal
length at most 1+6 epsilon_r<2; its two reference parameter windows are enclosed
in at most three fixed complete marked periods. For any selected interval
its defect is nonnegative and at most the sum of the enclosing
complete-period defects, pathwise.
This bound does not condition on the selected interval.

Join two labeled anchors at neighboring sites by an attachment to the
reference network, one network step, and an attachment to the other
anchor. The error of its signed Q-cost as an approximation to the P
increment is the sum of signed defects. Its absolute first moment is at
most

    (2+3+2) beta = 7 beta.                            (6)

At one site the two attachments give at most 4 beta. A reference label
requires no attachment. Reversing a signed trip changes its error's sign
and not the bound.

These comparisons have a uniform finite support. Every nominal road
point needed for them, including the crossing inspection, is at
(A,B)-maximum distance less than 2 from the departure mesh site.
The radius-10 input neighborhood is at (A,B)-distance less than 20
from such points. Assign every primitive to its containing half-open
unit parallelogram; a microscopic edge can be assigned by its midpoint.
Rounding to a cell index adds at most one. All needed cells are therefore
within index distance 23, and hence within Q_40 of the departure index.
The product cells are independent, for each offset separately.

For fixed scale all anchor values of P are integrable: each anchor is
in a deterministic bounded set of lattice edges, and domination bounds
its potential difference from a fixed vertex by finitely many deterministic
coordinate-path costs. Finite mean weights suffice. Therefore the
round-4 finite-cell theorem applies to these V=P(anchor) with

    H=40, epsilon=7 beta, c=7 C_(2,40).               (7)

It gives local gauges satisfying error at most c beta for any labeled
same-site or neighboring-site increment. No estimate in (6) counts labels,
possible phases or offsets.

For reference, the constants used from that theorem are

    R=3H+1=121,  L=5H+1=201,
    m=(2H+1)^2, N=(2R+1)^2 2^((4H+1)^2),
    J=5R+2,    C_(2,H)=2+2 N J 2^m.                 (8)

## 2. Averaging and four enclosing periods

An anchor on a wall with nominal level kappa is registered in offset
mesh a at (i, round(kappa-a)), where round uses a fixed translation-
invariant tie convention. Its residual label is in [-1/2,1/2]. The
same physical anchor is registered in every mesh; the roads are not
changed. Write g^a for its mesh gauge and g=|F|^(-1) sum_a g^a.

For two anchors, subtract their common P increment. The increment error
of g is exactly the average of the mesh errors. The triangle inequality
therefore preserves every c beta increment bound, with no factor |F|.
Independence of the mesh gauges is unnecessary.

For consecutive marks on one wall the registered indices differ by
(0,1), and the residual labels are the same. Their averaged increment
error is at most c beta.

On a marked period [kappa,kappa+1], put

    C_i=Q(kappa,kappa+1)-g_(i+1)+g_i,
    g(o)=g_i+Q(kappa,o)-(t(o)-kappa) C_i.              (9)

The Q terms and nominal parameters are the same on every offset mesh.
Since the coefficients of the endpoint gauges sum to one, (9) commutes
with their normalized average. It is therefore consistent to average
first or interpolate first.

A point on W_j with physical height in the band (2) has nominal parameter
t satisfying

    |t-t_j| <= b+2r=delta.                           (10)

Indeed its height differs from js+t by at most 2r in (v,B) coordinates.
Now 2 delta=11s/250<1. Define

    kappa_j=phi_j+floor(t_j-delta-phi_j).

Then

    kappa_j <= t_j-delta,
    t_j+delta < kappa_j+2.

Thus all endpoint occurrences, and c_j, are in the window of two
complete marked periods starting at kappa_j. This includes every visit
during a pause at the lower marked level. The strict upper inequality
excludes the pause assigned to the following window. Each of the two
walls needs two periods: the total number of periods is four.

The starting nominal parameters on the two walls obey

    |kappa_(j+1)-kappa_j| < 1+s.

To check this, write kappa_j=t_j-delta-u_j with 0<=u_j<1 and use
t_(j+1)=t_j-s. In any offset mesh, nearest-integer registration changes
this difference by at most one. The registered vertical difference is
an integer of absolute value less than 2+s<2.1, hence at most two.
The horizontal difference is one. A mesh path of at most three steps
joins the starting anchors' registrations. Use reference labels at
intermediate sites and the required physical labels at its endpoints.
The neighboring comparison applies to arbitrary endpoint labels, so
these three steps already include the label changes. Their telescoped
error has first moment at most 3c beta, including after averaging.

Write e_i for each of the four period increment errors and e_0 for this
starting-anchor error. The exact comparison budget from round 5 is

    Lambda=2 sum_(four periods) E D_i
                     +sum_(four periods) E|e_i|+E|e_0|
           <= (8+4c+3c) beta = (8+7c) beta.          (11)

The comparison tree has one edge, whose error is bounded by three
neighboring comparisons. This distinction avoids counting the meshes
as new road labels.

## 3. Link lower bound

Here is a direct derivation of the physical-competitor estimate, using
the four periods just fixed. Put h(o)=g(o)-P(o), and e_i=g_(i+1)-g_i
-P_(i+1)+P_i. On one period, C_i=D_i-e_i and (9) gives

    h(o)-h(i)=D(i,o)-(t(o)-kappa_i) C_i.

The cumulative defect is nondecreasing from 0 to D_i. Hence the total
variation of h over that period is at most D_i+|C_i|. Define

    B_0=sum_(four periods)(D_i+|C_i|)+|e_0|,
    A_0=sum_(four periods)|C_i|.

Joining occurrences through the two window starts shows that every
h difference between these windows has absolute value at most B_0.
Also A_0<=B_0 and, by C_i=D_i-e_i,

    E B_0 <= Lambda.                                (12)

Every corrected signed road subinterval has absolute cost at most A_0,
by splitting (9) at marks. For any physical gamma from x to y, (1) gives

    Q(gamma)-g(y)+g(x) >= h(x)-h(y) >= -B_0.

Adding the two corrected signed arms from the centers changes this
by at least -2 A_0. The result is exactly (3), by cancellation of the
endpoint gauges. Therefore all competitors, simultaneously, satisfy

    L(gamma) >= -B_0-2 A_0 >= -3 B_0.                (13)

Their negative infimum is at most 3 B_0. Equations (7), (11), (12)
give (4). Imposing the band or drawdown constraints only removes
competitors, and cannot worsen this lower bound.

Local measurability does not require B_0 to be observable. For fixed
local records there are finitely many endpoint edge occurrences.
Delete loops in a physical competitor: its Q-cost decreases, its endpoint
adjustments are unchanged, and all-pairs drawdown is preserved by taking
a subsequence. Subdivide the finite graph at its domain boundaries.
There are finitely many simple route types. On each type the two endpoint
fractions lie in a compact subset of [0,1]^2 defined by continuous band,
drawdown and occurrence-window constraints. The objective is continuous.
Its minimum is measurable: if F_0>=0 is a continuous constraint function
with zero set equal to that compact feasible set, the minima equal the
limits of infima of the continuous objective over rational pairs with
F_0<1/n. For an empty set these infima are eventually +infinity.
Take the minimum over the finitely many types. This proves locality,
measurability and attainment whenever the family is nonempty. Arbitrarily
many paths and repeated endpoint visits introduce no expectation factor.

The assertion applies to the full band-and-drawdown family, or to further
closed restrictions with the same finite-route description. No claim of
measurability for an arbitrary unspecified random family is needed.

## 4. Support, phases and entire columns

Every marked anchor used in either two-period window has nominal height
within 2 of its row center. Its mesh registration differs by at most 1/2
in the B direction. A primitive in a cell of Q_L of that registration
has (A,B)-coordinate distance at most L+1 from it. Thus its ||.||_*
distance from that wall's row center is at most

    2+1/2+(1+s)(L+1) < 2L+5 = 407.                 (14)

The original road records for the two complete periods need only radius
10+2=12. Interpolation needs these same records and the three anchor
gauges. Offset averaging enlarges no support: every offset is registered
relative to the same physical anchor and satisfies (14).

The two wall row centers are at ||.||_*-distance d<1. All link-domain
edge primitives are within radius 3 of the left center, including an
edge-midpoint assignment and sufficiently small lattice padding. Taking
the union proves the radius-408 assertion. This includes gauge inputs,
private coordinates for all offset meshes, and the weights of the link
domain; it does not include P.

It remains to track phases inside the conditional projections. In the
round-4 formula a gauge at index z is a finite sum of

    Pi_S(V_(z,lambda)-V_(a(S),0)),
    k(S) in Q_R(z),   a(S)=k(S)+(R+1)e_1.           (15)

The physical labeled anchor on W_j uses phase phi_j. The reference
anchor at a(S) uses only the phase of wall a(S)_1, because its A-road
has deterministic phase. For z_1=j, the possible reference indices
are between j+1 and j+2R+1. Product conditional expectations in Pi_S
integrate spatial inputs with the phases fixed. A function depending on
phases only through its two anchors yields a conditional-expectation
kernel with the same phase list: integrate the unobserved product
coordinates, including any calibration extension, without integrating
or introducing other phase parameters. The same observation applies
to the deterministic mean in the gauge formula. This can be done first
for every phase value in the finite list, fixing simultaneous versions.

Registrations and residual labels may themselves depend on phi_j; this
adds no other phase. Interpolation adds only the same wall phase.
For the right wall replace j by j+1 in the preceding range. The union
is precisely contained in (5), since 2R+2=244. The link minimization
adds only the two incident wall phases. No gauge for another row or
another possible phase is maximized here.

Let S_j be the sigma-field generated by all primitive spatial inputs
in the strip

    |u-jd| <= 816

and the phases in (5). Each column observable is measurable with respect
to S_j: a ||.||_*-ball of radius 408 has horizontal (v,B) width at most
(1+s)408<816, regardless of its row height. Distinct spatial primitive
coordinates are independent, and phases are independent of them and of
each other. For |j-j'|>=2000,

    |j-j'|d > 2000(99/100)=1980 > 2*816=1632,
    |j-j'| >= 2000 > 244.

The strips and phase-index intervals are disjoint. The coordinate
families generating S_j at indices in one residue class modulo 2000
are disjoint, proving their joint independence, and hence that of the
entire-column sigma-fields. The calibration extension is not a generating
input to these fields. Its possible long-range dependence is irrelevant.

## 5. Checks on the operations and their limits

There is a second way to verify that averaging does not lose a factor.
On the event the competitor family is nonempty, for one physical
competitor the averaged objective is exactly the average
of its mesh objectives, because each has the same physical Q-cost and
road arms. Consequently

    inf_gamma average_a L_a(gamma)
                       >= average_a inf_gamma L_a(gamma).

For real numbers z_a, (average z_a)^-<=average z_a^-. Thus the
negative part of the averaged infimum is bounded by the average of the
mesh negative envelopes. Taking expectations gives the same constant
as (11)–(13), without interchanging the infimum and average as an equality.

The coefficient in (11) can also be counted without its three-step tree:
eight beta pays for twice the defects of the four periods; four c beta
pays for their four anchor increments; three c beta connects the starts.
The physical competitor and its two arms give the factor three, yielding
24+21c=24+147 C_(2,40). Independently, the starting-level difference
is -s+u_j-u_(j+1), with both u's in [0,1), giving the same distance-three
registration bound. Formula (14) is bounded above by 2L+9/2, so the
integer radius 407 has a half-unit margin. The independent-column
separation has margin at least 348 in horizontal coordinates.

The short-arm cost can be checked more sharply. For attachments in (10),
the nominal center-to-endpoint length is at most delta. In each period,
the corrected arm is its nominal length times C_i by (9). Hence each
arm's absolute corrected cost is bounded by delta times the sum of
the two period |C_i|'s. Its expected supremum is at most
2 delta(1+c) beta. The more generous bound (13) is valid without using
this improvement.

Uniform conditional estimates allow independent random phases to be
sampled without loss: integrate (4) over their product distribution.
They do not allow phases to be selected after inspecting the spatial
inputs, or a maximum over all possible phases. For example, take J
uniform on {1,...,m} and Z_a=-m beta 1_{J=a}. For every fixed a,
E Z_a^-=beta. The normalized average of all Z_a equals -beta, and
an independent uniform choice of a still has expected negative part
beta. The choice a=J, or the negative minimum over a, has negative
part m beta on every outcome. This is an example about the inference
from fixed-parameter expectations, not an FPP counterexample.

Likewise (4) at every row does not bound a maximum over an increasing
number of rows. Whole-column independence is consistent with sharing
one phase throughout an infinite wall; it does not give two-dimensional
finite dependence. A separate selected-path or template argument is
required whenever rows or phase assignments are optimized.

## Source and scope

OpenAI, *Strict convexity and differentiability of the planar exponential
first-passage limit shape*, September 24, 2026,
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
Remark 10.7, Section 11 and Section 14.1, motivates this lemma. The result
above supplies explicit period, registration, support and phase-index
counts for its two-wall link construction, using the finite-cell theorem
and fixed-window estimate proved in the previous rounds. It does not
verify the selected-path template bounds, common-baseline gauge
comparisons, output-road support, or the contraction in Section 15.
