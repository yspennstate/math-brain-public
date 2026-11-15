# T122 work log, round 6

Task: “take the NEXT checkable step on this problem, building on that work”.
Received 2026-11-15 approximately 11:00 +04 (Asia/Tbilisi).
First exact clock: 2026-11-15 07:03:09 UTC = 11:03:09 +04.

## Orientation and bounded literature check

Read the startup memory index and compute_state.json (warn,
owner_away_open, CPU saturated). The task's folder-only write rule
supersedes shared mesh, checklist and brain logging. Those write-producing
commands were not invoked. No git, subagents, or writes outside this folder.

Inventoried all four earlier folders. Read the original REPORT.md,
LOG.md and SOLVED_ELSEWHERE.md; round 3 REPORT.md, LOG.md and PROOF.md;
round 4 REPORT.md, LOG.md and PROOF.md; round 5 PROOF.md and LOG.md
(a truncated combined output is being completed by a targeted read).
The original has no PROOF.md. No earlier folder has a research script.
The round 5 report is also supplied in the task; its on-disk copy will
be read separately. No earlier file was edited.

Read commands: pwd, rg --files, ls -la, cat, sed -n. The first pwd and
inventory were invoked before adding the wrapper; subsequent targeted
reads were launched with `nice -n 15 env OMP_NUM_THREADS=1`. The sandbox
reports `nice: setpriority: Operation not permitted`, although the reads
execute. As in earlier rounds, no research computation is run under
this unresolved priority restriction. An initially overbroad inventory
was truncated; subsequent reads were restricted to the named folders.

Web searches, finished within five minutes of the opening:

* "maximum cut" "Parisi" "2026" sparse random graphs exact formula
* "RSB bounds on the maximum cut" Harangi
* "max-cut" "Lopatto" Aronow
* "diluted" "antiferromagnet" "Parisi" "2026" formula
* "maximum cut" "cavity" "formula" "2026"

Opened the primary arXiv abstract of Viktor Harangi, RSB bounds on the
maximum cut, arXiv:2506.21296, and its full v1 HTML; P. M. Aronow and
Patrick Lopatto, Maximum cut and maximum bisection in random regular
graphs, arXiv:2609.19057; Dmitry Panchenko, The Mézard-Parisi formula,
arXiv:2610.39545 (still v1); and full HTML of Amin Coja-Oghlan and Will
Perkins, Spin systems on Bethe lattices, arXiv:1808.03440v1. No new
regular-ensemble cavity equality was found. The already known Poisson
advance does not change the round 5 regular-ensemble gap. Subsequent
paper reads will inspect these identified sources, not extend searching.

## Independent recheck of the round 5 main claim

Re-derived its marked-Poisson identity by testing a nonnegative function
g: the transformed intensity integral is
int rho(dz) int q x^(-1-q) g(x f(z)/c) dx
= int q y^(-1-q) g(y) dy * E f^q/c^q.
Thus c=(E f^q)^(1/q) restores the process. In a two-level cascade,
first divide each terminal multiplier w(z1,z2) by
c1(z1)=(E_2 w(z1,Z2)^zeta1)^(1/zeta1), then divide each top
multiplier c1(z1) by c0=(E_1 c1(Z1)^zeta0)^(1/zeta0).
The two ratios telescope to w/c0. The standardized descendant point
process has a conditional law independent of the ancestor mark and
top point process, so the next sorting permutation preserves its law.
Induction gives exactly the previous tree tilt lemma. The transformed
marks themselves can be biased; the proof needs only the point-process
law and a permutation of the entire product column space.

Checked the coordinate map independently: if new leaf alpha corresponds
to old leaf theta(alpha), set old coordinate at delta equal to new
coordinate theta^(-1)(delta). The old row at theta(alpha) then evaluates
h on precisely the new alpha-path coordinates. This is a product-measure
preserving coordinate permutation. The tilted row masses therefore give
the same weak-kernel law. Bounds exp(-beta)<=D,Q<=1 cover all finite
cavity products, even endpoint messages. The claimed trial inclusion
holds, conditional on the external invariant-law theorem used to turn
it into p_d(beta)<=J_d(beta).

Independent normalization: C=exp(beta)Q multiplies the site factor
by exp(beta*d), the edge factor by exp(beta), so site minus d/2 edge
adds beta*d/2. The spin prior contributes log 2. This agrees with
Z_cut=2^n exp(beta*dn/2) Z_normalized_uncut. No defect was found in
the earlier result. Its external theorem remains an unaudited dependency.

## Choice of ONE extension (before proof work)

Derive a zero-temperature variational problem for the regular finite-
hierarchy infimum J_d(beta), with an error uniform in hierarchy depth,
parameters and message function. Use energetic fields
m=tanh(beta*x/2), min-plus site/edge costs, and scaled cascade
parameters y_k=beta*zeta_k. Target: prove that J_d(beta)/beta has a
limit equal to an infimum over all finite y-hierarchies, without
assuming fixed depth or exchanging a nonuniform limit with an infimum.
This extends the previous report's explicit lack of such an interchange
and isolates the remaining comparison with c_d as a temperature-free
variational gap. It does not attempt the unproved reverse comparison.

## Derivation before writing the proof

Completed the targeted round 5 LOG.md read and read its on-disk REPORT.md.
Re-read Harangi Theorem 3.2 and its exponent convention, and Section 3.2:
its displayed zero-temperature specialization restricts the innermost
messages to {-1,0,+1}. Section 4 also discusses fractional exponential
approach rates to endpoint messages. The result sought here is the
uniform passage of the entire optimized finite-hierarchy functional,
not novelty of using zero-temperature fields or a new numerical bound.

For an energetic field x, write a_sigma=(|x|-sigma*x)/2 and
p_sigma=exp(-beta*a_sigma)/(1+exp(-beta*|x|)). There are two terms in
the denominator. Taking minima in the two-spin and star sums gives,
after clipping x to [-1,1],

  E(x1,x2)=(|x1|+|x2|-|x1-x2|)/2,
  S(x1,...,xd)=(sum_j |xj|-|sum_j xj|)/2.

Direct finite-sum bounds give
  -2 log2 <= log B + beta E <= 2 log2,
  -(d+1) log2 <= log A + beta S <= d log2.
The estimates cover x=0 and deterministic-spin endpoints by allowing
one a_sigma=infinity, with exp(-infinity)=0.

The conditional operator f -> -(1/y)log E exp(-y*f) is monotone,
commutes with constant addition, and is 1-Lipschitz in the sup norm.
Thus these local errors do not accumulate with the number of hierarchy
levels. Scaling y=beta*zeta converts the nested cascade power means
exactly into these operators. The expected trial logarithm identity
needed here is independently supplied by the two-level Poisson scale
calculation above and its inductive repetition.

Candidate energetic functional:
  K_d(r,y,x)=d/2 - L_y(S) + (d/2)L_y(E).
Let K_d^{<beta} be its infimum over all finite hierarchies with
0<y0<...<y_(r-1)<beta and measurable x:[0,1]^r -> [-1,1].
Both directions of trial conversion should yield
  K_d^{<beta} - 2d log(2)/beta <= J_d(beta)/beta
     <= K_d^{<beta} + (2d+1)log(2)/beta.
The domains increase with beta and exhaust all finite positive y;
their infima decrease to K_d^infinity. This would prove existence
of lim J_d(beta)/beta=K_d^infinity without a bound on depth.
Next: write all endpoint conventions and both infimum comparisons,
then test the signs and constants independently.

## 11:08 +04 — proof saved and read back

Wrote PROOF.md and read it in full with
`nice -n 15 env OMP_NUM_THREADS=1 cat PROOF.md`.
Clock: 2026-11-15 07:07:55 UTC = 11:07:55 +04.
The proposed theorem holds with the two constants recorded above.
It proves existence of the optimized hierarchical zero-temperature
limit and its equality with the energetic infimum, independently of
any additional graph theorem. Using the earlier regular upper bound
then gives c_d<=K_d^infinity and
lim Delta_d(beta)/beta=K_d^infinity-c_d>=0.

Independent checks and attempts to break it:

* Re-derived the edge minimum by explicitly listing its four costs.
  For nonnegative fields xi,eta they are 1, eta, xi, xi+eta+1;
  opposite preferred signs give a zero-cost configuration. The
  clipped expression E matches in all cases, including zeros.
* Re-derived the star bound by one sum over 2^(d+1) spin assignments,
  rather than d applications of the two-term D estimate. The
  denominator is between 2 and 2^(d+1); numerator counting reproduces
  log A + beta S in [-(d+1)log2,d log2]. Four edge assignments with
  denominator in [1,4] reproduce the edge interval independently.
* Recalculated the final errors directly in normalized cut pressure:
  lower = [1-(d+1)-d]log2/beta, upper=[1+d+d]log2/beta.
  These are -2d log2/beta and (2d+1)log2/beta. Both sites and
  edges use a monotone, translation-equivariant operator, so neither
  constant depends on r or on a small gap between cascade parameters.
* At r=2, substitution gives
  L_y f=-(1/y0)log E_1[(E_2 exp(-y1*f))^(y0/y1)].
  For f=f1(z1)+f2(z2), it splits into the separate y0 and y1
  logarithmic means. Marking the two Poisson levels separately gives
  the identical expression, checking scaling and order independently.
* Constant zero field gives K=d/2; direct finite-temperature algebra
  gives H=log2+(d/2)log((1+exp(beta))/2), with the same slope.
  Constant positive field t in (0,1] gives K=d/2+dt/2. Direct
  logarithmic slopes of D and B reproduce it. This catches an
  erroneous edge sign or replacement of fractional fields by signs.
* An exact nonconstant test: d=3, r=1, fair fields +/-1 give
  P(S=0)=1/4, P(S=1)=3/4, P(E=0)=P(E=1)=1/2. Counting eight
  triples and four pairs checks those probabilities a second way.
  At y=log3 the value is 3-(5/2)log2/log3, strictly between 1
  and 3/2 by the integer comparisons 32<81 and 32>27.
  This is a check, not a new numerical best bound.
* Both trial-conversion directions are necessary: arbitrary old h
  maps through an extended logarithmic field and then clipping;
  each bounded energetic field lifts to h=tanh(beta*x/2). Clipping
  preserves the minimum costs, not the finite-temperature values.
  Uniform local bounds control the resulting discrepancy.
* Checked h=+/-1, field zero, mixed zeros and endpoints, fractional
  magnitudes, beta-dependent messages, varying depth, parameters
  approaching zero or the moving cutoff beta, and strict ordering
  with arbitrarily small gaps. No step takes a limit inside a
  nonuniform hierarchy recursion.
* The exhaustion argument controls the limit but supplies no rate
  for K_d^{<beta}-K_d^infinity. Claiming an O(1/beta) rate to the
  unrestricted energetic infimum would not follow. The report will
  state this limitation explicitly.

No counterexample or mathematical failure was found. No research
script or numerical program was needed or run. Priority changes
remain denied. The graph equality K_d^infinity=c_d is still unproved;
this result alone cannot force the nonnegative gap in (22) to vanish.

## Final source comparison and readback

Read REPORT.md and LOG.md in full with
`nice -n 15 env OMP_NUM_THREADS=1 cat REPORT.md LOG.md`.
Opened the already identified Harangi paper at Section 4. Its
phi_star and phi_edge are exactly the S and E costs used here.
Added this explicit attribution to PROOF.md and REPORT.md: the new
piece beyond round 5 is the bound uniform over arbitrary finite
hierarchies and the consequent optimized limit, not the local costs
or a new one-step formula. This source check confirms the fractional
field normalization independently.

A prose cleanup patch initially failed to match a line beginning
with "cost. If either". It was repeated with exact context; no
mathematical change resulted. Clarified the both-zero field case
and replaced informal "slope" language by limits of beta^(-1)log
of each factor. The report now records the theorem, its checks,
commands, limitations, and next-worker target. No requested work
remains within this chosen piece. All three deliverables are here.
