# T170-LEAD-ROLLING-D14-001 v1: PASS, mathematical correctness

Kind: audit. Targets T170-3 upper comparison and T170-4 dimension14.
Source: `~\crash_recovery_20261014\workers_1015\term_362ebe34\T170-LEAD-ROLLING-D14-001_v1.md`. Exact SHA256 `5489019ce25b821c1992e94faa79427e5750a1fd1678e4e30d24de85c9907510`. Audit time 2026-10-15T18:33:26.730482+03:00.
Actual execution account4 at semantic read and finish, same account as
author lead: this is NOT a second distinct-account admission. No priority,
lower-dimension, or full-conjecture claim. No live ledger was edited.

## Exact claim and accepted dependency

For independent Exp(1) unoriented nearest-neighbor bond FPP on Z14,
with the axis and diagonal each normalized to Euclidean length1:

mu_axis <= 49312208313/549755813888
        < 22866068359/250000000000 <= mu_diag.

The exact gap is237013616084657783/134217728000000000000>0. Thus the
shape is not a Euclidean ball, conditional on the explicitly retained
previously audited chord5 diagonal theorem C003v2. Its proof SHA is
9a0d7617781f2496d2e1fc3cae58ee718b3878198d47102262715b6678b7de96
and exact data SHA is
e78ecf283aa59fbfd46b237bcd5dc82d52335b8ff56cf2d56ca9be347a16d7af.
Our own Fraction comparison verifies the d14 rational is at least the
submitted downward floor. These data already use Euclidean units;
there is no second division by sqrt14. No rerun of its1778-state proof
is claimed or needed for this explicitly accepted premise.

All28 submission artifact hashes and both
dependency hashes were checked against actual bytes. Author executable
sources were not imported, executed, copied, or used to derive our code.
Our checker is checks/t170_d14_rolling_own.py, with the exact full result
checks/t170_d14_rolling_own.json. Inputs are the pinned BASE integer DATA;
discovery estimates in that JSON are not used.

## Section1: horizontal bound and controlled law

The finite all-split lemma already independently proved in the D16 audit
applies to sets of every ambient cube dimension with cardinality<=10000.
For clarity its proof is dimension induction: cross edges between the
two slices are a matching, so their number is <=min(a,b); the checked
f(a)+f(b)+min(a,b)<=f(a+b) closes induction, including zero slices and Q0.
The unary lattice-box embedding preserves the complete L1 metric and
therefore internal unit edges. Compute the boundary back in original
Z13, whose degree is26, giving sigma(n)=26n-2f(n) for every shape and
every n<=256. No connectivity assumption is made. The prior own
25million-split receipt is checks/t170_d16_boundary_own.json. It was
not repeated. This run independently constructs all256 rates by directly
counting every induced Q13 edge of the binary initial segment and checks
against the popcount sum and strict positivity.

Fresh physical check: use one rate1 clock per unoriented lattice edge.
For the full process, boundary-clock residuals are independent Exp(1),
giving exactly the Richardson generator and the origin infection-field
law of independent static Exp(1) edge FPP. This does not assert a common
static metric simultaneously for all hypothetical source restarts.
The restricted rule inspects only its own three slab sets and fresh
auxiliary randomness. Its horizontal boundaries contain the requested
integer numbers of edges. Between successive slabs at most the receiving
count's columns can be occupied, so max(a-b,0) and max(b-c,0) eligible
forward edges exist. The next slab is restricted-empty because the
window advances only forward. The five birth-edge families and the
front family are disjoint; shared targets do not reduce their total
instantaneous rate, since an accepted ring adds one site and immediately
triggers reselection. At cap all corresponding births are disabled.

Selections are predictable on the open interval following an accepted
event. Poisson strong Markov supplies independent future increments after
every accepted stopping time, even on ignored edges. Thus the printed
four event rates hold for every physical geometry, not just a sampled
state. Count self front events at(1,1,1) are actual events and rewards.
By event induction, restricted infection is a subset of full infection:
its starting endpoint is full infected and its target is either already
full infected or infected by the same ring. Removing a slab cannot break
this inclusion. No monotonicity of an estimated numerical value table,
no assumed independent edge passage times after arbitrary restarts, and
no new application of an old Dhar supremum argument is used here.

## Section2: three-site geometry, iid cycles, and the directional norm

The three-site startup is made by two selected forward infections with
finite mean cost. A physical retained slab's set never decreases while
that slab exists. A return of counts to(1,1,1) must occur at a front event:
births only increase counts. Just before that event, the middle and right
slabs each contain one point. The middle slab was already a singleton
when its successor was first created, since its count cannot decrease.
That successor was born from its unique point by a forward edge, so the
two singleton points are aligned. The new front singleton is one forward
step from the unique right point. Therefore ALL THREE retained points
are aligned after the return, regardless of the discarded left count.
The initial aligned startup supplies the induction base. A count reset
alone in an arbitrary geometry would not suffice; this birth history is
the necessary extra argument and it holds here.

Future Poisson increments and new selections are fresh at each first
accepted return, including a self return. After translation the physical
configuration and rule are identical, so successive displacement/time/
advance cycles are iid. Neither discarded infected sites nor already
full infected sites enter the restricted rule. The canonical string and
uniform subset selection respect every transverse coordinate reflection.
The cycle law is reflection invariant; integrable transverse displacement
therefore has mean0. The process intentionally need not respect axial
reflection.

The total accepted rate is bounded by (6m+3)C=20736: horizontal rates
<=6mC, the two forward birth families <=2C, front <=C. It is >=1. Three
successive fronts send(a,b,c) to(b,c,1), then(c,1,1), then(1,1,1), and each
has conditional chance>=1/20736. An earlier return only improves the
bound. Hence cycle event count N has a geometric tail in blocks of3;
holding conditional means are<=1, so E[T]<=E[N]<infinity. Each cycle has
at least one and at most N front advances. The final anchor is connected
genealogically to the initial aligned string by accepted infection edges;
transverse displacement is bounded in L1 by horizontal births, hence N.
All law-of-large-numbers first moments exist, and bounded rate prevents
restricted explosion.

For retained left anchors X_j and cycle times S_j, iid sums give
X_j/j -> E[A]e1 and S_j/j -> E[T], with E[A]>0. The full infection time
at X_j is<=S_j by pathwise inclusion. The uniform FPP shape theorem and
norm continuity/homogeneity yield T_full(X_j)/j -> E[A]mu_axis, since
X_j/j converges to a nonzero deterministic vector. Exp(1) satisfies all
required moment/positivity hypotheses. Thus mu_axis<=E[T]/E[A]. This
uses actual random spatial points, not an unsupported hyperplane-to-axis
identification. BP1705.08143v2 Introduction p1 states the simultaneous
large-time shape inclusion used here, before its Section2 profile method.

## Section3: independently defined and verified all2^24 bias values

The pinned BASE has65536 signed integers in the specified row order,
scale2^40 and A0=98624416626. Its SHA is
884c5412e7d1418a02a952674cc12a415aa3e777e4fcdaf53cd1144e593c3079.
Our checker stores only a current and previous256x256 a-plane, plus BASE.
For a,b,c descending, all nonzero birth children are already defined;
the front value is BASE[b,c]. Thus the ceiling recipe uniquely specifies
all16,777,216 values. Cap children are omitted, and c=1 is BASE[a,b].

Using Python unbounded integers, we independently construct every one of
the16,711,680 c>=2 values using divmod and q+(remainder!=0). Explicit
negative-numerator tests verify SIGNED ceiling, not truncation to zero.
We separately evaluate each generator expression from the three child
differences and the front difference; every residual equals numerator
minus total_rate*value and lies in[-(total_rate-1),0]. This direct check
is not merely trusting that a ceiling routine ran. Minimum ceiling slack
is0; maximum is13907.

All65536 c=1 inequalities are then directly checked. The maximum required
A0 is98624394809, leaving21817 integer units below the submitted A0.
The actual extremal base row, its rates and ALL used child values are
saved. Decreasing the tested coefficient to that row requirement minus1
produces residual+1 on the same reconstructed row, an actual scope/sign
fault control. It is not a tautological claim that some generic inequality
would fail. No author residual table was read or compared.

All constructed values lie within[-S,S]; observed extrema are
-94329449330 and92961094949 units. Maximum absolute numerator
is1325221394950205. Native overflow is not needed for our proof,
since our arithmetic is unbounded; independently its stated bound
(1+20736+256)S<2^55 for numerators and <2^56 for direct difference sums
is valid given |h|<=S and A0<S. The all-value hash in the receipt has its
full ordering and byte convention; no equality to an author full-value
hash is asserted. All values and inequalities were independently computed.

Exact8-state Fraction elimination at cap2 independently derives the
stationary law and killed first-return time and advance equations. Both
ratios are61803/119341. Omitting the self reward produces the different
ratio2289/4420, detected explicitly. The cap2 control
checks conventions; it is not substituted for the full cap256 replay.
This complete one-core run took71.835s, with two small
planes under20MB, after checking over2GB free memory. It has exited.

## Section4: stopped inequality and conclusion

On the finite count space h and Lh are bounded. Apply Dynkin at T wedge t
and pass to integrable cycle end T using bounded h and domination by a
constant times T. Endpoint count(1,1,1) makes the h expectations cancel.
The front counting process INCLUDING count self events has predictable
intensity c<=256. Its stopped compensator expectation passes to T by
domination of the integral by256T and monotone convergence of counts.
Consequently E[A]=E[integral c ds]. Integrating the ALL-state inequality
L(h/S)+1-alpha*c<=0 gives E[T]-alpha E[A]<=0 and the claimed axis bound.
The exact floor comparison gives the strict nonball conclusion.

The same-day BP/Kumar-Dhar primary-source and BP citing-paper screen in
checks/t170_d16_literature_own.json remains applicable; the additional
rolling-method and90day arXiv screens are in
checks/t170_rolling_literature_own.json. Empty bounded index results are
not priority proof. Novelty remains UNCLEAR. No separate account's audit
was used to replace any step above. PASS is mathematical correctness
conditional on the explicitly retained checked diagonal premise; actual
account4 overlap prevents counting this as distinct-account admission.
