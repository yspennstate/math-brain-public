# C0020 research attempt — 2026-10-12

## Exact problem and scope

The fetched source is Garban–Steif, arXiv:1102.5761v3 (29 May 2012).
Definition VIII.2, printed p.89/PDF p.91, defines C(A) as the expected number of
single-coordinate queries, averaged over independent uniform input bits and
algorithmic randomness. An algorithm stops only when all completions of the
unrevealed bits give the same output (printed p.83/PDF p.85). Thus it is exact,
zero error. Repeated queries can be eliminated by caching.

Theorem VIII.3, printed p.87/PDF p.89, specifies critical **site** percolation on
the **triangular** lattice in an n by n box; the square-bond analogue there has
an unspecified positive exponent. The open question is printed p.90/PDF p.92:

> Open Question: Find the smallest σ such that there are algorithms A_n for f_n with C(A_n) ≤ n^σ. (We know σ ∈ [6/4, 7/4].)

The source actually gives n^(7/4+o(1)) and n^(6/4+o(1)) immediately before this
question. To avoid an endpoint assertion these bounds do not establish, the
asymptotic exponent in this attempt means

    sigma_* = limsup_{n→∞} log C(f_n)/log n,

equivalently the infimum of exponents admitting an eventual polynomial upper
bound. Existence of a limit, attainment of an endpoint with no o(1), and the
literal bound for every small n are separate issues. None is settled here.

The known interval remains [3/2,7/4]. No literature solution was identified;
coverage limits and later papers are recorded in LITERATURE.md.

## 1. Exact finite optimization and derandomization

Let f be any function on N independent fair bits. A state s records which bits
are known and their values. Write u(s) for the number unknown, and call a state
decisive when f is constant over its completions. Let T(s) be the minimum sum
of additional query depths over all 2^u(s) completions. Then

    T(s)=0                                        if s is decisive,
    T(s)=2^u(s)+min_i [T(s,i=0)+T(s,i=1)]         otherwise,

where i ranges over unknown coordinates. C(f)=T(empty)/2^N.

Proof: induct on u. At a decisive state stopping is exact and optimal. At a
nondecisive state every exact algorithm must query a bit. For a fixed choice i,
the initial query contributes 2^u to the sum of depths. Completions partition
into the two equally sized child subcubes. The induction hypothesis minimizes
each child contribution, and joining minimizing child trees attains their sum.
Choosing a minimum over finitely many i proves both the lower bound and
attainment. A randomized first choice gives a convex combination of these
candidate expected costs, never less than their minimum. The same induction
handles subsequent random choices. Alternatively fix the entire random seed:
for a finite input space, zero error for each input implies almost every seed
is exact on all inputs simultaneously, and averaging deterministic costs
cannot improve on their minimum. This is also Remark VIII.1(i) of the source;
it is not claimed as a new result. Revealment minimization is different.

For monotone f the stopping test needs only the minimum completion (all unknown
bits zero) and maximum completion (all unknown bits one). If their outputs
agree, monotonicity sandwiches every other output between them. If they differ,
they themselves exhibit incompatible completions. This proves the test exactly.

## 2. An integer-valued refinement of the influence lower bound

Here f:{-1,1}^N→{-1,1} is increasing, p=P(f=1) lies strictly between zero and
one, and I=sum_i P(i is pivotal). For a real x let

    phi(x) = x^2 + {x}(1-{x}),

where {x}=x-floor(x). Every exact randomized decision algorithm satisfies

    C(A) ≥ p phi(I/(2p)) + (1-p) phi(-I/(2(1-p))).              (1)

In particular for balanced f,

    C(A) ≥ phi(I) = I^2+{I}(1-{I}).                            (2)

Without the fractional corrections, (1) gives I^2/[4p(1-p)], the centered
version of Theorem VIII.6. The correction in (1) is at most 1/4 and hence does
not improve the percolation exponent. No novelty claim is made for this lemma.

Complete proof: eliminate repeated queries and put τ≤N for the number queried,
J for their set, and M=sum_{i in J} X_i. For t≤N let D_t equal the t-th queried
bit if t≤τ and zero otherwise. The event t≤τ and the identity of the next bit
are determined before its value is observed. Conditional on this past and
algorithmic randomness, any previously unqueried bit is independent and fair.
Consequently E[D_t|past]=0 and E[D_t^2|past]=1_{t≤τ}. For r<t, D_r is measurable
with respect to the past at t, so E[D_r D_t]=0. Summing gives E[M]=0 and
E[M^2]=sum_t P(t≤τ)=Eτ=C(A). These are finite sums, with no unbounded stopping
or limit interchange.

For an increasing ±1 function E[f X_i]=P(i pivotal): conditioning on all other
bits, either the function is constant in bit i and the expectation is zero,
or its two values are -1 and +1 and the expectation is one. Furthermore
E[f X_i 1_{i not in J}]=0. To see this, fix all other bits and the random seed.
If the tree never queries i, flipping i cannot change its transcript or final
output, so the two terms cancel. If it queries i on one input, it queries it
on both, since the histories before that query coincide, and both terms are
zero. Hence E[f M]=sum_i E[f X_i]=I.

Write μ_+=E[M|f=1], μ_-=E[M|f=-1]. The equations E[M]=0 and E[fM]=I give

    μ_+=I/(2p),  μ_-=-I/(2(1-p)).

For any integer-valued random variable Z of finite second moment, let k=floor
E[Z]. For every integer z, (z-k)(z-k-1)≥0: either z≤k so both factors are
nonpositive, or z≥k+1 so both are nonnegative. Taking expectations yields

    E[Z^2] ≥ (2k+1) E[Z]-k(k+1)
             = (E[Z])^2+{E[Z]}(1-{E[Z]}) = phi(E[Z]).

Apply this separately to the integer M conditional on f=1 and f=-1 and combine
with E[M^2]=C(A) to obtain (1). The function phi is even (its linear pieces
interpolate the even integer-square function); for p=1/2, μ_±=±I, proving (2).
For constant f the appropriate statement is simply C(f)=I=0.

There is also an exact reduction, rather than just an inequality. By conditional
variance decomposition and the conditional means already proved,

    C(A) = I^2/[4p(1-p)] + E[Var(M_A | f)].                    (3)

Indeed E[M_A]=0, and E[(E[M_A|f])^2] equals
p(I/(2p))^2+(1-p)(I/(2(1-p)))^2 = I^2/[4p(1-p)]. Subtract this
from E[M_A^2]=C(A). Taking the infimum over exact nonrepeating algorithms gives

    C(f) = I^2/[4p(1-p)] + inf_A E[Var(M_A | f)].              (4)

This locates the unresolved term exactly: a percolation-specific estimate on
the minimum conditional score variance, beyond the bounded integrality
correction, is necessary to improve this route. It is an equivalent reduction,
not a proved geometric estimate. For the balanced 3×3 rhombus, the exact table
gives minimum conditional variance 9039/16384; its unavoidable integrality part
is 847/16384, leaving exactly 1/2 beyond that correction.

## 3. A complete 2 by 2 triangular-site special case

For finite computations use the explicitly defined triangular rhombus with
sites (x,y), 0≤x<w, 0≤y<h, and neighbor differences
(±1,0), (0,±1), (1,-1), (-1,1). Left/right boundaries are x=0 and x=w-1.
All sites are independently occupied with probability 1/2. In Euclidean
coordinates this is a rhombus, not the source's square; finite values are not
asserted to equal its square values.

For w=h=2 label row-major sites a,b,c,d. Every left-right crossing contains a
cross-boundary edge, and the possible such edges are ab, cb, cd. Therefore

    F = (a and b) or (c and b) or (c and d).

The count of positive assignments is eight of sixteen. Its four pivotal
probabilities are 1/4,1/2,1/2,1/4: a is pivotal exactly when b=1,c=0; d exactly
when c=1,b=0; b when either c=1,d=0 or c=0,a=1; c by symmetry. Thus the ±1
version is balanced and I=3/2. Formula (2) gives C(F)≥(3/2)^2+1/4=5/2.

An attaining algorithm queries b first. If b=0, the remaining function is cd;
query c and, only if c=1, d. Its additional expected cost is 3/2. If b=1,
the remaining function is a or c; query c and, only if c=0, a. Again the
additional expected cost is 3/2. The total is 1+3/2=5/2. This proves the exact
optimum over all randomized exact algorithms, with a matching lower bound
and construction. This is a special case, not a solution to C0020.

## 4. Certificate lower bounds and nonadaptive obstruction

In an increasing function, any decisive partial assignment with output one can
discard its queried zeros and retain only its queried ones: setting all other
bits zero still yields one, and monotonicity handles all completions. For output
zero the symmetric argument discards queried ones. Thus the minimum certificate
size at configuration x can be computed by minimizing over occupied subsets S
with F(S)=1 if F(x)=1, or over closed subsets S with F(V\S)=0 if F(x)=0. Every
algorithm's final queried set is a certificate, so C(A)≥E[w(X)]. A shortest
occupied path gives a positive certificate, but finding that path can cost much
more than its size; an existential chemical-distance bound is not an algorithm.

For a fully nonadaptive algorithm the queried set is chosen independently of
input values and every chosen bit is read. It must contain every relevant
coordinate almost surely. Proof: for each relevant i there exist two inputs
differing only at i with different outputs. If i is omitted, their transcripts
coincide, so no common output is correct on both. Under a full-support finite
product law both inputs have positive probability; zero error forbids this
event. Take the finite union over relevant i. In the rhombus every site is
relevant: occupy exactly its entire horizontal row, close all other rows, and
then close the specified site. A left-right crossing is destroyed. The optimal
nonadaptive cost is therefore wh. If w=1 this event is OR_h; if h=1 it is AND_w,
with adaptive optimum 2(1-2^(-h)) and 2(1-2^(-w)), respectively, by early stopping.
These boundary cases test the model, not the two-dimensional critical exponent.

## 5. Exact computations and their checks

`exact_crossings.py` implements the integer Bellman recurrence, graph traversal
truth tables, certificate enumeration, and full-input policy replay. No floating
probability or Monte Carlo estimate enters a claimed exact value. Fractions are
reduced exactly. Results are in `exact_results.json` and `exact_*x*.json`:

| rhombus | C(F) | E minimum certificate | I |
|---|---:|---:|---:|
| 1×1 | 1 | 1 | 1 |
| 2×1 | 3/2 | 5/4 | 1 |
| 1×3 | 7/4 | 5/4 | 3/4 |
| 2×2 | 5/2 | 2 | 3/2 |
| 3×2 | 103/32 | 75/32 | 25/16 |
| 3×3 | 555/128 | 389/128 | 249/128 |
| 4×3 | 10685/2048 | 14063/4096 | 1039/512 |

For N≤9 a second recurrence checks decisiveness by enumerating *all compatible
full inputs*, rather than using monotonicity; its root optimum agrees. All
optimal-policy paths were replayed (2,4,8,16,64,512,4096 full inputs). Their total
depths agree with Bellman integer sums. Every final leaf was checked against
minimum and maximum completions, and every input's depth dominates its enumerated
minimum certificate. Costs dominate I^2/[4p(1-p)]. The largest run visited 517243
states and finished in 2.15 seconds of Python wall time, below the 1 GB budget
(a later measured rerun is recorded separately). The 3×3 optimum is an exact
computer-assisted finite result; the full all-algorithm argument is the Bellman
proof in Section 1, not extrapolation from tested algorithms.

## 6. Hostile referee checks and precise gap

Potential failure: interchange zero-error input and seed quantifiers. Resolved
by finite-input union of null exceptional-seed sets. Potential failure: adaptive
selection biases the next bit. Resolved by choosing only unqueried bits based on
the past; the fresh bit is fair. Potential failure: unread bits correlate with
the stopping event. Resolved by the paired-input cancellation argument, not an
unsupported independence assertion. Potential failure: confusing indicator and
±1 influences. Pivotal probabilities are invariant under the recoding 2F-1;
the factor 4p(1-p) is the variance of the recoded output. Potential failure:
using shortest-path length as query cost. Rejected; certificate information does
not provide a method of finding the certificate. Potential failure: treating
rhombi as source squares or fitting a critical exponent from N≤12. Neither
identification nor fit is claimed. Potential failure: source location/model.
Resolved from the downloaded definition and Theorem VIII.3, not the intake.

The previous intake's uniform-revealment shortcut is false, as independently
recorded by w336: C(A)=sum_i δ_i does not imply δ_i=O(C(A)/N). One may prepend a
query of a fixed site to a subquadratic crossing algorithm, increasing cost by
at most one but forcing that site's revealment to one. The earlier intake's
assertions about third Fourier levels and six-arm probabilities are unsupported;
they are not used or reasserted here. The actual source lower bound is the
O'Donnell–Servedio total-influence-square inequality, not a product of revealment
and complexity.

What remains: either construct exact decision trees with exponent below 7/4 and
establish a matching lower bound, or strengthen the universal lower bound above
3/2 until it matches an algorithm. The integer refinement adds at most 1/4, so
even its complete proof leaves this gap unchanged. Finite Bellman tables grow
exponentially and no valid composition law for planar square crossings has been
proved here. Consequently sigma_* is undetermined and C0020 is NOT solved.

## 7. Final verification record

Lean 4/Mathlib v4.33.1 accepted `FiniteBellman.lean` with exit code 0 and no
warnings. Command: `lake env lean ~/brain_workers/TRIO_1011/op/C0020/FiniteBellman.lean`,
run from `~/lean_verify`, with a 3600-second subprocess timeout,
one Lean invocation at a time. The final log is `lean_check.log`. Only
`Mathlib.Data.Nat.Basic` and `Mathlib.Algebra.Order.Ring.Int` are imported.
The three finite evaluations use `decide +kernel`; the general integer product
nonnegativity lemma uses kernel-checked `omega` and ordered-ring multiplication.
There is no `sorry`, `native_decide`, or axiom declaration in the checked file.
The formalization checks the integer gap and the four-site recurrence evaluation;
it does not formalize the probabilistic proof or the general Bellman optimality
theorem. Those have full written proofs above.

`check_integer_bound.py` checked all monotone truth tables with N=1,2,3,4
(3,6,20,168 functions, totaling 197), using exact rational arithmetic. Constants
were handled separately. The general bound and its centered comparison passed
for every table; the balanced specialization agreed identically. Run time was
0.215 seconds. The largest rhombus rerun measured peak working set 136531968
bytes (about 130.2 MiB); it finished in 1.30 seconds. Evidence is in
`integer_bound_checks.json` and `memory_check.json`.

Final assessment: PARTIAL. The proved refinement, variance reduction, restricted
nonadaptive case, and finite rhombus optima survive these checks. The original
critical triangular-site square-crossing exponent has not been determined.

## Additional attempt requested by the user

See SECOND_ATTEMPT.md for the two new approaches, the pursued conditional-pivotal construction, full proofs of restriction identities and obstruction families, the exact 3x3 counterexample to greedy cost optimality, and the precise remaining trajectory-deficit estimate. The verdict remains PARTIAL; the exponent interval is unchanged.
