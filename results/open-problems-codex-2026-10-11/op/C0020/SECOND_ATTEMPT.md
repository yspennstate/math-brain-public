# Additional attempt at C0020 — 2026-10-12

The remaining gap from ATTEMPT.md is unchanged at the start: the critical
triangular-site square-crossing query exponent is between 3/2 and 7/4. The
conditional-score variance reduction is exact, but supplies no percolation
estimate on its residual term.

Two approaches not pursued in the first attempt:

1. **Construct a conditional-pivotal greedy tree.** At each restricted crossing
   function, query a coordinate of maximum conditional pivotal probability.
   This is suggested by Random-Turn Hex optimal play (Peres–Schramm–Sheffield–
   Wilson), but game-winning optimality does not imply minimum expected query
   cost. Compute exact greedy costs and compare with Bellman optima; derive the
   restriction identities for influence and output variance. Then test whether
   the centered influence-square quantity is a useful decreasing potential.
   A genuine multiscale drift estimate could yield an improved upper bound.

2. **Pack unresolved pivotal regions to force score variance.** Apply independent
   local resampling in separated mesoscopic boxes after conditioning on a tree
   transcript. Try to force multiple independently signed revealed-bit sums,
   giving a lower bound on E Var(M|f) in ATTEMPT.md equation (4). The obstacle is
   that conditioning on the transcript is spatially selective, and its queries
   need not be local. Arm probabilities under an unconditioned product measure
   cannot simply be multiplied after that conditioning. This requires a new
   transcript-uniform geometric lemma, rather than the existing global score
   identity.

Approach 1 is selected: it defines an explicit exact algorithm, and every local
algebraic assertion and proposed potential can be tested on all finite restricted
states. Approach 2 currently lacks a testable transcript-uniform statement.

The brain has been asked specifically about conditional queried-score variance,
O'Donnell–Servedio, and Peres–Schramm–Sheffield–Wilson conditional pivotal play.
Its answers will be recorded as hints, never treated as proofs.

## Brain response and checked neighbouring theorem

The exact queries were:

- `conditional variance queried score O Donnell Servedio percolation influence`
- `Peres Schramm Sheffield Wilson Random Turn Hex pivotal optimal strategy`
- walk `claim_0c1e55cfd7605d30089c4ffeca09b142d03be5573c9ce9401839396350a60738`

The first returned the OSSS source, Fisher information, and unrelated
martingale-variance cards, but no bound on the residual in ATTEMPT.md (4).
The second returned pivotal-measure references and a Cerf pivotal-set theorem
card. That card's formula is corrupted in recall output and was not used.
Neither supplied a solution or a relevant proved residual-variance estimate.

Instead I checked the already downloaded Peres–Schramm–Sheffield–Wilson paper,
arXiv:math/0508580v2. Lemma 3.1 on PDF p.5 says that a move in a monotone
win-or-lose random-turn selection game is optimal iff it is most likely to be
pivotal under uniform completion. The next paragraph explicitly identifies
shared optimal play with a decision procedure. Its meaning is winning-strategy
optimality, not minimum expected query cost. Theorem 4.1 on PDF pp.7–8 gives the
known 3/2 lower exponent; the discussion gives only simulated 1.5–1.6 exponents.

## Exact restriction identities

Let a state s leave u fair bits unknown, let F_s be its increasing 0/1 function,
and write q_s=E F_s, I_s=sum of conditional pivotal probabilities, and
V_s=q_s(1-q_s). If the next queried coordinate has conditional pivotal
probability a, and its children have parameters (q_0,I_0,V_0),(q_1,I_1,V_1), then

    q_1-q_0=a,
    I_s-(I_0+I_1)/2=a,
    V_s-(V_0+V_1)/2=a^2/4.                              (5)

Complete proof: monotonicity makes F_s(1,z)-F_s(0,z) equal either zero or one;
it is one exactly for pivotal z. Averaging gives the first identity. For any
other coordinate j, conditioning the event that j is pivotal on the queried
fair coordinate partitions its probability into the equally weighted child
probabilities. The queried coordinate's own contribution a vanishes in both
children. Sum these equalities over j to obtain the second identity. Finally
q_s=(q_0+q_1)/2, and direct expansion gives
q_s(1-q_s)-[q_0(1-q_0)+q_1(1-q_1)]/2=(q_1-q_0)^2/4.

For any exact nonrepeating tree, let a_t be the chosen conditional influence
at time t before its value is observed, and set it to zero after stopping.
Since the stopping time is bounded by the input count, conditional expectation
and telescoping (5) give

    E sum_{t<=tau} a_t = I_root,
    E sum_{t<=tau} a_t^2 = 4V_root.                       (6)

The leaf has I=V=0. Random choices can first be conditioned on, so the proof
also applies to randomized trees. Cauchy–Schwarz on the finite occupation
measure of active (input,randomness,time) pairs gives
I_root^2 <= E[tau] * E sum a_t^2 = 4V_root C(A).
This recovers the known lower bound, with no assumed spatial uniformity.
For a greedy tree a_t is the maximum current influence; (5) and (6) alone give
no upper bound on the number of times a_t can be very small.

## Exact counterexample to minimum-cost greedy play

Use the 3×3 triangular rhombus specified in ATTEMPT.md, with row-major sites
0 through 8. Its root influences are

    (13,26,39,26,41,26,39,26,13)/128.

Thus site 4 is the unique maximum. The exact best expected query costs when
the first queried site is fixed, allowing *arbitrary optimal continuation*, are

    (617,578,555,578,563,578,555,578,617)/128.              (7)

Every maximum-influence-first algorithm therefore costs at least 563/128,
while a tree starting at site 2 or 6 costs 555/128. The difference is 1/16.
This refutes the claim that conditional-pivotal greedy play minimizes expected
query cost, even for a small triangular-site crossing. It does not refute a
conjectured asymptotic exponent for greedy square crossings.

The full greedy recursion has cost 563/128 for every choice of maximizing
ties on this instance. `greedy_attempt.py` computes both the best and worst
continuation among such ties, and both coincide. Proof of these exact finite
statements uses the Bellman induction already proved in ATTEMPT.md Section 1:
the greedy recurrence restricts its minimum (or maximum) to coordinates attaining
the current maximum pivotal probability. Counts of positive completions compute
the influences exactly. No candidate algorithm subset is used to assert the
unrestricted optimum.

Every complete input was replayed for the unrestricted optimal, best greedy,
and worst greedy policies; the total depths equal their recurrence values.
Additionally E[M]=0, E[M^2]=C and E[(2F-1)M]=I were checked exactly for each
replayed policy. A second independent implementation of (7) is being checked
using explicit compatible completions and a depth-first graph traversal.

## Why the simplest drift proof cannot work uniformly

Define H(s)=I_s^2/[4V_s] at a nonconstant restricted function, and H=0 at a
constant function. If every greedy step on every relevant restricted state
satisfied

    H(s) - (H(s,0)+H(s,1))/2 >= c > 0,                   (8)

then bounded-time telescoping would give c E[tau] <= H(root). In critical
triangular-site squares, I(root)=n^(3/4+o(1)) and V(root) is bounded away from
zero, so this would prove an upper exponent 3/2. The statement needs proof;
being a lower-bound quantity does not make H an upper-bound potential.

The proposed *uniform over all restrictions* version of (8) is false even in
triangular rhombi. Close all sites outside one horizontal row, leave its k
sites unknown, and the restricted crossing is AND_k. Its q=2^(-k),
I=k/2^(k-1), and therefore

    H_k = k^2/(2^k-1).

Every remaining coordinate is maximally pivotal. After querying one, the zero
child is constant and the one child is AND_(k-1). Consequently for k>=2

    drift_k = k^2/(2^k-1) - (k-1)^2/[2(2^(k-1)-1)].       (9)

This tends to zero, since both displayed terms do. Thus no fixed positive c
works for all such states. This is a genuine restricted crossing configuration,
not an arbitrary Boolean-function substitution. It need not be reached by
greedy play from the initial square. Accordingly this counterexample rules out
the stated uniform lemma but DOES NOT rule out a trajectory-averaged drift
estimate which controls the time spent in rare states.

The 4×3 computation contains an AND_6 restriction: known closed mask 425,
one mask 0, maximally pivotal queried site 1. Its H=4/7, its children have
H=0 and H=25/31, and its drift is 73/434, matching (9) for k=6.
An independent DFS check over all 128 completions confirms that its six
required sites are 1,2,4,6,10,11 and its seventh unknown site, 9, is irrelevant.

## A neighbouring percolation counterexample to a universal upper bound

There is no universal constant K such that C(F)<=K I(F)^2/[4 Var(F)] for
all nondegenerate monotone connectivity functions, even with independent fair
inputs. This is relevant because (5)–(6) alone contain no square geometry.

Complete construction and proof: for k>=2 let m=2^k and let F be the OR of m
disjoint k-bit ANDs. Equivalently take a graph with m internally vertex-disjoint
length-k paths between terminals and perform fair bond percolation. A crossing
exists iff at least one path has all its edges open. This graph is planar and
simple for k>=2, but its terminal degrees grow with m and it is NOT the
critical triangular-site square model.

Put q=2^(-k)=1/m and r=(1-q)^m=P(F=0). Along m=2^k one has 1/4<=r<1/2.
For the lower bound, at m=2 the expression equals 1/4, and

    (1-1/(2m))^(2m)/(1-1/m)^m
      = [1+1/(4m^2(1-1/m))]^m > 1.

The upper bound follows from (1-1/m)^m <= e^(-1)<1/2, using
log(1-x)<=-x for 0<x<1. Thus Var(F)=r(1-r)>=3/16.
An edge is pivotal precisely when all other edges of its own path are open and
all other paths fail. Its influence is 2^(-(k-1))(1-q)^(m-1), whence

    I(F)=2k(1-q)^(m-1)<=2k,
    H(F)=I(F)^2/[4 Var(F)] <= (16/3)k^2.

On F=0, any zero certificate must contain a queried zero from each path.
Otherwise a path with no revealed zero could be completed to all ones while
preserving every observation, contradicting decisiveness. Thus every exact
algorithm makes at least m queries on every negative input, and

    C(F)>=m r>=2^k/4.

It follows that C(F)/H(F)>=3*2^k/(64k^2), which diverges. This proves the claimed
counterexample. It does not give a counterexample to C0020 or alter its interval.

The greedy tree for this example can also be described and evaluated exactly.
It queries a path until finding a zero or completing it, then starts a new path
if necessary. Proof that it is forced by the pivotal rule: once r_obs>=1 ones
have been observed on the active path, its remaining length is l=k-r_obs. Its
coordinate influence relative to an untouched path is

    2^r_obs (1-2^(-k))/(1-2^(-l)) > 1.

This follows by cancelling the common failure probabilities of all other
untouched paths. Variables in a path already containing a revealed zero have
influence zero. Initially all untouched paths tie; their equal size and fair
bits make their order irrelevant. Each examined path has expected query count
d=1+1/2+...+2^(-(k-1))=2(1-q). The j-th path is examined with probability
(1-q)^(j-1), independently of its own bits. Therefore

    C_greedy(F) = 2(1-q)[1-(1-q)^m]/q.                    (10)

This is an upper bound for C(F), not an asserted general optimality theorem.
Together with the certificate lower bound it proves C(F)=Theta(2^k), while
H(F)=O(k^2). In particular a successful proof for greedy square crossings must
use their spatial geometry, not just the two influence occupation identities.

## Remaining gap after pursuing the construction

The conditional-pivotal algorithm is an exact crossing algorithm, but computing
its conditional influences may itself be expensive; that overhead is not part
of the source's query-cost model. Its query exponent in source squares is still
unproved. Greedy first-query optimality is false, a uniform H-drift lemma over
all restrictions is false, and an H-based universal upper bound for general
monotone connectivity is false. None disproves a favourable average drift for
critical square crossings. What remains for this approach is a quantitative
bound on the occupation of low-influence/low-drift restricted states under the
specific greedy trajectory, exploiting critical two-dimensional geometry.
No such bound is established here; [3/2,7/4] remains unchanged.

Here is a precise sufficient estimate for further work. For the particular
greedy trajectory write d(s,i)=H(s)-[H(s,i=0)+H(s,i=1)]/2. For c>0 define

    B_n(c)=E sum_{t<=tau} (c-d(s_t,i_t))_+.

Since the actual next state is either child with probability 1/2, conditional
expectation followed by bounded-time telescoping gives E sum d(s_t,i_t)=H(root).
For every real d, c<=d+(c-d)_+. Sum this inequality over active times and take
expectations to obtain the proved implication

    C_greedy(f_n) <= [H(root)+B_n(c)]/c.                  (11)

No positivity of individual drifts is assumed. Constant functions have H=0;
everything is a finite sum. Thus a bound B_n(c)<=n^(3/2+epsilon+o(1)) for one
fixed c>0 and epsilon<1/4 would improve the upper exponent. Such bounds for
every epsilon>0 would close the problem at 3/2, in the asymptotic-infimum sense
specified in ATTEMPT.md. These proposed deficit estimates are unproved targets,
not results or numerical extrapolations. The obstacle is now a specific
trajectory-weighted deficit, rather than the false all-restrictions drift lemma.

Even at a balanced state the drift can be quantitatively small. For q=1/2,
0<a<1, and b=(I_1-I_0)/2, identities (5) give

    d=[2Ia-a^2(1+I^2)-b^2]/(1-a^2)
      <= 2Ia/(1-a^2).                                  (12)

Proof: q_0=(1-a)/2 and q_1=(1+a)/2, so both child variances are
(1-a^2)/4; their influences have mean I-a. Their average squared influence
is (I-a)^2+b^2. Substitute into H and expand. This formula makes no uniform
boundary-influence assertion for source squares. In particular, a bulk query
with I of order n^(3/4+o(1)) and a of order n^(-5/4+o(1)) has drift at most
n^(-1/2+o(1)); applying this to the selected greedy coordinate would require
checking its location or a uniform maximum-influence bound. Neither extra
percolation premise is proved or assumed here.

## Final referee verification record

The independent graph implementation confirmed all 512 inputs against the
11-minimal-mask monotone DNF. It confirmed the pivotal-count vector and every
fixed-first-query optimum in (7). A complete certificate of all 3^9=19683
ternary-state Bellman totals is saved in `bellman_3x3_certificate.json`.
`verify_greedy_certificate.py` checked all entries against explicit-completion
constancy or the exact child-minimum recurrence, and confirmed the root total
2220 and forced-center total 2252 over 512 equiprobable inputs. This is a
finite, independently checkable optimality certificate, not a sampled result.

`greedy_attempt.py` also proves the 4×3 finite greedy optimum among maximizing
choices is 10783/2048, while unrestricted optimum is 10685/2048. The best and
worst greedy choices coincide. Across the four tested rhombi, all three
restriction identities were checked at 1528833 state-coordinate transitions.
Every input was replayed under each of the three policies, with the three
queried-score identities verified exactly. No asymptotic exponent was fitted.

`second_referee_checks.py` checks the AND_6 subcube, evaluates the explicit
tribes greedy tree on all 256,4096,256 inputs in three small examples, and
compares these costs with (10) using exact rational arithmetic. The family
bounds r>=1/4, V>=3/16, H<=(16/3)k^2 and C_greedy>=mr were checked exactly for
k=1,...,10. Floating display ratios in its JSON are only illustrations; all
claimed comparisons and the infinite-family proof above use exact arithmetic.

Lean 4 accepted `GreedyWitness.lean` with exit code 0 and no warnings. It imports
only `Mathlib.Data.Nat.Basic`. The complete nine-coordinate pivotal-count vector,
the individual center and corner counts, and the AND_6 cleared numerator and
denominator are checked with `decide +kernel`. There is no `sorry`,
`native_decide`, or axiom declaration. The graph-to-DNF equivalence is checked
on all 512 inputs by Python, not formally in Lean; the Bellman certificate and
the probabilistic arguments are also not formalized. Their precise scope is
given above. An initial import failed because the prebuilt
`Mathlib.Data.Rat.Basic` object was absent; the unnecessary import was removed.
No shared library was built or changed. The final command was
`lake env lean ~/brain_workers/TRIO_1011/op/C0020/GreedyWitness.lean`
from `~/lean_verify`, with a 3600-second timeout. Only one Lean
invocation ran at a time. The final log is `greedy_lean_check.log`.

A rerun of the largest new computation with explicit resource guards finished
in 62.11 seconds and measured peak working set 584019968 bytes (557.0 MiB).
The script checks a 768 MiB ceiling and an eight-minute time ceiling periodically
and fails gracefully if either is exceeded. Its result agrees with the first
run. Both stay within the requested per-job resource limits.

Additional hostile-referee pitfalls addressed:

- A unique root maximum is established, so tie-breaking cannot rescue the
  3×3 first-query counterexample. Best/worst tie continuations are separately
  optimized and replayed; the unrestricted center continuation is also bounded
  by the complete Bellman certificate.
- Fixed-input query costs use the uniform source query model. Conditional
  influences are computed by completion counts with denominator 2^(u-1), not
  by unconditional arm probabilities after selective revelation.
- The graph DFS, minimal-mask DNF, and Bellman checking routines are separately
  implemented. Full certificates check all valid restrictions, not merely
  states visited by an alleged optimal algorithm.
- The corridor state has an irrelevant seventh unknown bit, explicitly checked
  rather than inferred from its q and I. This does not affect its AND_6 law.
- The universal connectivity counterexample has growing terminal degree and
  a different graph/model. No transfer to critical squares is claimed.
- The estimate (11) is a sufficient reduction; the required bound on B_n(c)
  remains unproved. Formula (12) does not silently assume a uniform maximum
  influence bound at square boundaries.

Final assessment: **PARTIAL**. This additional attempt produced exact greedy
counterexamples, complete restriction identities, two rigorous obstruction
families, and a sharper statement of the remaining sufficient deficit estimate.
It did not determine the source crossing exponent or improve either endpoint.
