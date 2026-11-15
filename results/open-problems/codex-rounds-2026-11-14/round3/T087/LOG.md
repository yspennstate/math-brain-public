# T087 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, about 01:19 Asia/Tbilisi (tool clock:
14 November 2026, 21:19 UTC).

## Orientation and scope

Read the earlier REPORT.md, PROOF.md, AUDIT.md, LOG.md and
SOLVED_ELSEWHERE.md in ~/codex_op_1114/briefs/T087.
`ls -la` confirms that directory has no computation scripts to rerun.
Read ~/.claude/brain_startup.md and the compute state.
The latter reports `warn`, `cpu_saturated`, `owner_away_open`. No numerical
workload or subagent is launched. The explicit folder-only rule overrides
shared checklist, mesh and brain mutations; those tools are not invoked.
Only this directory will be changed. No git or external posting.

Read commands: `cat` on the named files, `ls -la` on both task directories,
and `rg --files` to locate local instructions. No scripts in the earlier
directory were omitted: there are none.

## Brief literature check (started 01:19)

Web search queries:

- `percolation three dimensions critical exponents existence proof 2025 2026`
- `percolation continuity critical probability September 2026 Z3`
- `percolation number clusters connecting two sets exponential tail expectation BK inequality tightness`
- `percolation number spanning clusters submultiplicative tail distribution tightness hyperscaling`

Opened primary sources:

1. Tom Hutchcroft, *Dimension dependence of critical phenomena in long-range
   percolation*, arXiv:2510.03951v1,
   https://arxiv.org/html/2510.03951v1 .
2. Michael Aizenman, *On the Number of Incipient Spanning Clusters*,
   arXiv:cond-mat/9609240v4,
   https://arxiv.org/html/cond-mat/9609240v4 .
3. C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness
   of Critical Crossing Probabilities Implies Hyperscaling*, MSR-TR-98-26,
   https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
4. OpenAI, *Critical bond and site percolation on the cubic lattice*,
   24 September 2026, primary README at
   https://raw.githubusercontent.com/openai/math/main/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md .
   The GitHub directory again returns a cache miss. The README is metadata,
   not verification of its continuity claim. No arXiv id is supplied there.

No verified complete solution to T087 found. A continuity theorem alone
would not settle exponent existence. The literature status check will stop
within five minutes; subsequent reading concerns the chosen lemma only.

## Independent recheck of the earlier result

Let S be a uniformly chosen vertex of B_n, independent of the edges. In a
configuration, the probabilities that S lies in each crossing component
are s_i/V_n. Their sum is W/V_n. For an independent second uniform vertex T,
the conditional probability of lying in the same crossing component is
Q/V_n^2. Cauchy–Schwarz over the probability space of configurations and
the counting measure of their crossing components gives

    (E W/V_n)^2 <= E K_n * E Q/V_n^2.

The first quantity E W/V_n is at least pi(3n), by first exit from B_{2n}.
Also E Q/V_n^2 <= X(2n)/V_n, by unrestricted pair connectivity and
translation invariance. Therefore

    X(2n) >= V_n pi(3n)^2 / E K_n.

The volume factor and the single power of E K_n agree with the earlier
proof. No independence between component mass and count is required.

Separately checked the reverse exponent transfer: if X(n)=n^{s+o(1)},
0<s<d, compare m=3n with N=ceil((3n)^{1/t}), t<1. Then
X(m)/X(N)=N^{-s(1-t)+o(1)} -> 0. The independent endpoint-arm bound gives
pi(n)^2 >= [X(N)-X(m)]/V_N, hence limsup[-log pi(n)/log n]
<= (d-s)/(2t). The earlier finite-scale inequality and subpolynomial
E K_n give the opposite inequality as t tends to one. Both claims hold.
The upper endpoint-arm bound uses deterministic disjoint edge sets and
does not assert independence of cluster counts. No earlier error found.

## Direction under examination

The earlier report asks for expected crossing-count control and warns
that tightness alone does not control expectation for arbitrary counts.
Investigate the specific percolation geometry, comparing the exact
free-boundary annulus count with classical rectangular crossing criteria.
An argument using disjoint open paths must distinguish their maximum
number from the number of distinct open components: they are different
observables. The final extension will be chosen and recorded before its
proof is written.

## Choice, recorded before the proof

Extend the earlier reduction to the critical cluster-volume tail. Under
the same expected-count hypothesis (H) and pi(n)=n^{-a+o(1)},
0<a<d/2, aim to prove

    P(|C(0)| >= t) = t^{-a/(d-a)+o(1)}.

This supplies existence of the volume-tail exponent delta=(d-a)/a from
the earlier inputs, without scale-ratio regularity. It is one additional
critical exponent, conditional on the earlier unproved hypotheses.
Classical conditional hyperscaling already relates these quantities;
no priority claim is intended.

The missing lemma is a lower bound on the expected largest free-boundary
cluster mass. To avoid a false independence assertion, use a buffered
annulus outside B_{8m}, while the inner arm events stop at B_{7m}.
Control the annulus component count by a finite cover with translated
copies of the *exact* earlier K_m, with each small box contained in the
annulus. This geometry is the point to audit especially carefully.

The brief status check is closed at about 01:22, under five minutes after
it began. No complete solution located; further source reading concerns
this conditional volume-tail extension, not another status search.

## Sharpened hypothesis, before the proof

The buffered argument can use a weaker hypothesis than (H):

    (P) for every epsilon>0, P(K_n > n^epsilon) -> 0.

The selected piece remains the volume-tail exponent theorem. Prove it
under (P), which follows from (H) by Markov's inequality and also follows
from tightness. Do NOT infer subpolynomial E K_n from (P).

Key additional step: logarithmic arm decay supplies scales m=8^j at which
pi(3m)/pi(24m) is bounded by 8^{a+1}. Such scales occur in every interval
[N,N^{1+zeta}] for each fixed zeta>0 and all sufficiently large N:
otherwise the log ratios telescope to an average slope greater than a.
At these scales the buffered bad-count contribution is negligible even
with no rate in (P). Monotonicity then fills the gaps on logarithmic scales.

This also aims to recover X(n)=n^{d-2a+o(1)} from the new tail law and a
radius/volume split. That is a consequence of the one selected theorem,
and shows why the weaker probabilistic hypothesis matters for the earlier
result. No reverse existence transfer under (P) will be claimed.

Source comparison: opened pp. 28–29 of Borgs–Chayes–Kesten–Spencer
(equations (5.36)–(5.39)), and pp. 7–8, equations (2.23)–(2.29).
Their slowly varying remainder condition is explicitly stronger than a
logarithmic limit. Their eta in (2.29) is a supremum exponent. The present
argument will keep uniform pointwise decay separate. Their use of
buffered inner/outer independence is classical; the claimed deliverable
is an explicit proof for (P) and the earlier exact K_n, not novelty over
all classical conditional hyperscaling theorems.

## Proof saved

Saved PROOF.md with the conditional theorem

    pi(n)=n^{-a+o(1)}, 0<a<d/2, and (P)
      => F(t)=t^{-a/(d-a)+o(1)}, X(n)=n^{d-2a+o(1)}.

The proof uses no computation. Its finite covering inequality is
J_m <= sum_{z in Z_m} K_m(z), where A_m has radii 8m and 16m,
Z_m=m*partial B_12, and every z+B_{2m} lies between radii 10m and 14m.
At good scales, a buffered first-moment argument proves

    E M_m >= V_{4m} pi(20m)/(2 ceil(m^epsilon)),

where M_m is the largest free-boundary cluster size in B_{16m}.
The edge sets defining U_m (inside B_{7m}) and J_m (outside B_{8m})
are disjoint. W_m is not treated as independent of J_m.

The earlier expected-count inequality remains valid, but is not used
with an unproved E K_n estimate in the new proof. The upper volume-tail
bound follows from F(t)<=pi(n)+X(n)/t and the separated-arm upper bound
for X. The new lower tail uses the largest-cluster estimate, then
monotonicity across logarithmically dense good scales. The consequence
for X follows from X(n)>=t[F(t)-pi(n)]. There is no circular invocation
of the earlier forward theorem under its stronger hypothesis.

## Independent audit saved

Saved AUDIT.md. Re-derived the covering count in d=3 three ways:
25^3-23^3=3458; disjoint face allocation gives 1250+1150+1058=3458;
and the shell formula gives 24*12^2+2=3458. Checked the extremal radii
10m and 14m both by the reverse triangle inequality and coordinatewise.
Checked that an endpoint on partial B_{16m} is at least 4m from any
assigned center on partial B_{12m}.

Independently recovered the largest-mass estimate by sampling a uniform
core vertex and conditioning on its location. Independently recovered
the conversion V_{16m}F(q)>=E M_m-q by sampling a uniform vertex of the
outer box. Balanced the upper tail orders n^{-a} and n^{d-2a}/t, and
separately eliminated m from the lower mass order m^{d-a} and its
mass/volume probability m^{-a}; both give a/(d-a).

Attempted failure cases: rare huge counts; nonmonotone component-count
events; merging outside the annulus; splitting in small boxes; repeated
returns of the crossing path to the core; tangential boundary edges;
nonregular arm ratios; sparse scales; infinity atoms; circular use of X;
and excluded endpoint exponents. No invalid step found. The last-visit
argument and the 7m/8m separation are essential explicit details.

Algebraic checks only: d=2, a=5/48 gives delta=91/5 and d-2a=43/24.
With a=2, the output delta=d/2-1 recovers the expected dimensional
obstruction above six instead of incorrectly predicting mean-field
hyperscaling. No measured percolation numbers are used.

## Final text verification

Command:

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,380p' PROOF.md

Output: the complete saved proof, reread. The command also printed
`nice: setpriority: Operation not permitted`, as in the earlier session;
the short text read nevertheless completed with exit code 0. No numerical
or sustained computational program was run. This environment does not
permit certifying the requested priority adjustment for that text read.

Checked every bound in the saved text against the report, especially
the direction of the good-scale arm ratio and of F(t)>=F(q), the
independence of U_m and J_m, and the use of unrestricted translation
invariance in (22). Renamed the unrelated shell-bound constant b_d to
avoid reusing c_d, which denotes the exact covering cardinality.

A final logging patch initially failed its context check and made no
changes. Inspected the last 38 lines of LOG.md with `tail` and the
relevant lines of PROOF.md and REPORT.md with `rg`, both with
`OMP_NUM_THREADS=1 nice -n 15`; each short read completed and reported
the same priority-adjustment denial. Reapplied the patch with the exact
context. No mathematical claim changed.

Saved REPORT.md with the required first line `VERDICT: PARTIAL ...`.
The result is a conditional extension; it does not establish T087 or
the needed hypotheses on Z^3. All new artifacts are in this folder:
LOG.md, PROOF.md, AUDIT.md and REPORT.md. No SOLVED_ELSEWHERE.md is
created because no complete solution was verified.
