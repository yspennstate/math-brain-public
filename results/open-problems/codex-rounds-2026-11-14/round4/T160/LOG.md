# T160 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 Nov 2026, approximately 04:58 Asia/Tbilisi.

## Scope and startup

Read both earlier REPORT.md, LOG.md, PROOF.md and audit.py files. The task's
specific order forbids writes outside this folder, so shared brain, mesh and
checklist commands which mutate external state are not run. No git,
subagents, background jobs or external publication. All computations will use
`nice -n 15 env OMP_NUM_THREADS=1 python3`, standard library only, a short
alarm, and less than 1 GB. Compute state read at startup: warn/cpu_saturated,
mode owner_away_open, memory free 69%. Only small exact checks are planned.

## Literature check (finished within five minutes)

Web searches: `"incipient infinite cluster" "three" 2026 percolation existence`
and `"Kesten" "incipient" "Z" 2026 quasi multiplicativity`.
Opened these arXiv pages:

- Deepan Basu and Artem Sapozhnikov, *Kesten's incipient infinite cluster and
  quasi-multiplicativity of crossing probabilities*,
  https://arxiv.org/abs/1603.06884.
- Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe,
  *Robust construction of the incipient infinite cluster in high dimensional
  critical percolation*, https://arxiv.org/abs/2502.10882.
- Malo Hillairet, *Short, Quantitative Construction of the IIC in Planar
  Percolation*, https://arxiv.org/abs/2509.18852 (v3, 28 May 2026).
- Zhenhao Cai and Jian Ding, *Incipient infinite clusters and volume growth
  for Gaussian free fields and loop soups on metric graphs*,
  https://arxiv.org/abs/2412.05709.

The first uses quasi-multiplicativity, the second high-dimensional two-point
asymptotics, the third planarity, and the fourth a different model. No
verified new solution of the three-dimensional Bernoulli question was
located. This is a short check, not an exhaustive review. No
SOLVED_ELSEWHERE.md is warranted. Literature check stops here.

## Recheck of the earlier result

Independent derivation: conditional on a generation with z open vertices,
the next generation is Binomial(b_i*z,p). Dividing its second moment by
M_i^2 gives the increment (1-p)/M_i. At p=1/2 the unary backward survival
map is t/2 and the binary one is t-t^2/4. In reciprocal coordinates their
Lipschitz constants on [1,infinity) are 2 and at most 1, respectively.
Consequently 0 <= 1/q(n+1)-1/q(n) <= 1/M_n. The previous binary plateau
gives q(n)/M_n <= 8*2^(2k-1)/N_(k-1) = 2^(-k^2+4k-9) throughout stage k.
For w=q_A/(q_A+q_B), substitution gives |Delta w| <= epsilon_k/4.
The exponent -k^2+4k-11 is correct.

For a fixed branch prefix, conditioning has density
[1-(1-t)^Z_m]/q(n). As t decreases to zero, this converges to Z_m/M_m.
Separately, forcing a uniform root-to-level-m path multiplies a compatible
configuration's mass by 2^m and has Z_m compatible paths out of V_m;
this gives the same density. For branch-success probabilities u=q_A/2,
v=q_B/2, inclusion-exclusion gives the mixture error coefficient uv/(u+v).
Thus the preceding classification follows from the vanishing adjacent
increments and the alternating endpoint weights. No error found. Fresh
exact finite checks, independent of the earlier scripts, will be recorded.

## Chosen extension (recorded before proof work)

Prove an exact finite-box response formula and a necessary-and-sufficient
ratio criterion for cylinder convergence on Z^3. For each interior edge
configuration retain the partition of all boundary vertices by interior
open connectivity, together with its distinguished root component.
Represent the exterior by a partition of the boundary and one target
terminal. Join the two partitions before testing root-to-target connectivity.
Normalize exterior response probabilities by the all-open interior response.
Prove that convergence of these finitely many normalized responses for
every fixed box is equivalent to the requested cylinder convergence, with
an explicit total-variation comparison. Audit by exact finite-graph
enumeration, including a path which leaves the root component, returns
through another interior component, and exits again.

Why: this is the next step named in round 3. It replaces the tree's scalar
survival ratio with the correct finite-dimensional lattice object. Merely
tracking the root-connected boundary set discards possible returns through
other components. The criterion itself will prove no asymptotic ratio
estimate on Z^3 and no existence theorem for T160.

## Fresh independent recheck completed

Created recheck.py without importing or executing either earlier script.
It uses exact binomial population transitions to check the prefix law and
backward survival, exact atom probabilities for the mixture identity, and
integer suppression counts through 64 stages. Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1
```

Exit status 0. Output is saved in recheck_output.txt; the main counts are
63 tree distributions/second moments, 321 prefix/TV checks, 126 horizon
checks, 144 union-mixture atoms, 459 weight-increment checks and 64 stage
certificates. (The saved output is authoritative for the counts.) Together
with the analytic rederivation above, the earlier result holds. Inherited
nice priority is 20; the redundant nice request warns but retains priority
20. No exponential-size tree is generated.

## Finite-box derivation

Use the disjoint edge sets E(B_m) and E(B_n) minus E(B_m), n>m>=1.
Let S=boundary B_m and wire all outer target vertices to a terminal *.
The interior determines a partition pi of S union {0}; the exterior
determines a partition xi of S union {*}. The connection event is precisely
that 0 and * lie in the same block of the transitive join pi vee xi.
This handles any number of alternating visits to the two regions.

Let H be the exterior event S connects to the target, and let rho_n be the
law of xi conditional on H. The normalized response is
r_n(pi)=rho_n(0 connected to * in pi vee xi). For all-open interior r=1;
for all states 0<=r<=1. With a_eta the ordinary product probability of an
interior atom, Z_n=sum a_eta*r_n(pi_eta) lies in [a_open,1]. The conditional
atom law is a_eta*r_n(pi_eta)/Z_n. Conversely
r_n(pi_eta)=a_open*mu_n(eta)/(a_eta*mu_n(all-open)), where
mu_n(all-open)>=a_open>0. This proves the stated equivalence for all
realizable partitions. Convergence of the entire exterior partition law is
sufficient but is not assumed in the equivalence.

For two horizons define D=sum a_eta*|r_n(pi_eta)-r_l(pi_eta)| and
delta=TV(mu_n,mu_l). Normalizing the two finite measures gives
delta<=D/a_open. Inverting through the all-open atom gives
D <= (2+1/a_open)*delta. These constants are finite for a fixed box and
are not uniform as m increases. No critical extinction assumption is used.

An explicit cubic-lattice witness for the need to retain other components:
inside B_1 let o=(0,0,0), a=(1,0,0), b=(1,1,0), c=(0,1,0).
Only o-a is open in eta_0; eta_1 additionally opens b-c. Both have the
same root-connected boundary set {a}. In the exterior of B_1 in B_3,
open only a-(2,0,0)-(2,1,0)-b and c-(0,2,0)-(0,3,0).
The root reaches boundary B_3 exactly for eta_1. This exterior event has
strictly positive probability for every 0<p<1; monotonicity therefore gives
strictly different exterior responses at n=3. No assumption about p_c is
needed for this finite example.

## Proof saved and reference constant improved

PROOF.md now gives the full proof. Grouping interior atoms by their
realizable boundary partition gives an exact mixture of the fixed laws
nu_pi=P_p(interior | pi). The mixture supports are disjoint, so total
variation equals the total variation of the partition weights. The
single-block reference partition may occur for many interior configurations;
using its full probability a_star improves the earlier all-open-atom
constant. The bounds are D/(2+1/a_star) <= TV <= D/a_star, and
a_star >= p^((2m+1)^3-1) by opening a fixed spanning tree. The inverse
formula also uses reference-partition probabilities. No uniform-in-m
constant or asymptotic convergence is asserted.

One attempted proof-file patch was rejected by JavaScript string escaping
before execution; it changed no file. Reissued using a raw string and
saved successfully. Next: independent connectivity checks by BFS versus
partition joins, exact response/mixture/inverse calculations, and explicit
cubic-coordinate checks of the witness.

## Exact audit completed

Created audit.py. It computes partitions with union-find and independently
checks full connectivity with breadth-first search. Four finite graphs
cover a return through another interior component, two successive returns,
an interior component hidden from the terminal set, cycles, multiple target
vertices, and a single boundary terminal. At p=1/3,1/2,2/3 each graph is
checked for three target choices. This is an exact finite-graph audit, not
enumeration of all configurations on a lattice box.

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
```

Exit status 0. Output:

```text
nice: setpriority: Operation not permitted
PASS: 36 exact graph/parameter/target models
PASS: 41760 BFS versus partition-join configurations
PASS: 756 conditional atom formulas; 504 partition mixture/inverse formulas
PASS: 36 TV comparisons, disjoint-support equalities and exterior-law bounds
PASS: 768 independent exact normalization and inverse stress checks
PASS: cubic witness: 54 interior edges, 828 exterior edges, 5-edge return pattern
PASS: sparse-witness conditional response gap p^5; full-box lower bound p^5(1-p)^823 > 0
PASS: four cubic edge counts by degree sum; four explicit spanning trees and exponents
Priority: 20; OMP_NUM_THREADS=1
Elapsed seconds: 0.322
Peak RSS bytes (macOS): 16613376
PASS: all exact checks
```

The recheck.py run reported 0.028 seconds and peak RSS 14,123,008 bytes.
Both computations are single-threaded at inherited nice 20 and use only
exact rational arithmetic for probabilities. No floating-point probability
estimate is used in the proof. Both scripts have 120-second alarms.

## Adversarial audit

- Re-derived the normalized response law by conditioning on a full interior
  atom and, independently, grouping by the boundary partition. The fixed
  laws within partition classes have disjoint support, making the TV
  identity exact rather than only a contraction inequality.
- Re-derived the inverse in two forms: ratios of partition probabilities,
  and reconstruction of the unnormalized masses as Z*lambda. The latter
  yields D <= (2+1/a_star)*TV. Independently stressed both inequalities on
  768 rational response pairs, with zero coordinates and reference mass
  as small as 1/100. The reference coordinate stays one, so no zero
  denominator is hidden.
- All interior partitions are restricted to those actually realizable in
  the fixed box. Positivity of 0<p<1 makes each such partition's product
  probability strictly positive. Necessity is not asserted for artificial
  boundary conditions that no interior configuration can realize.
- A root component missing the boundary gives response zero. Components
  missing all terminals can be omitted. Components meeting other boundary
  vertices must be retained; the explicit cubic witness proves this.
- Exterior blocks reaching different target vertices can be marked with a
  single terminal. A joined path is stopped at its first visit to that
  terminal; there is no reliance on a physical connection between target
  vertices. Multiple-target graph enumerations check this distinction.
- The graph audit includes two successive returns, ruling out an accidental
  one-return-only implementation. The proof uses full transitive closure
  and allows any finite number of alternations.
- Checked the cubic witness in actual integer coordinates: all five
  exterior edges lie outside E(B_1) and inside E(B_3), the terminal is
  (0,3,0), and both root-connected boundary sets equal {a}. With all
  unlisted exterior edges closed the response gap is exactly p^5.
  Allowing all exterior configurations gives a gap at least
  p^5*(1-p)^823, by monotonicity and the one positive-probability witness.
- Counted cubic edges two ways, by positive-coordinate edges and by the
  sum of six-neighbor degrees. E(B_1) has 54 edges and E(B_3) has 882,
  hence G_(1,3) has 828 and 823 are unlisted in the witness. Explicit BFS
  spanning trees in B_m for m=1,2,3,4 have (2m+1)^3-1 edges, independently
  checking the lower-bound exponent.
- The constants deteriorate with the fixed box. No limit uniform in m,
  contraction across annuli, quasi-multiplicativity, or critical exponent
  is deduced. Both numerator and denominator in the response ratio may
  tend to zero; the reference normalization prevents finite-box division
  problems but gives no control of the ratio as n grows.

## What failed and next estimate

Final analytic check of the earlier critical parameter and one-ray claims:
the suppression schedule gives D_s(n)->infinity and D_s(n)=o(n). Thus
M_n(p)=(2p)^n*2^(-D_s(n)) tends to zero for p<=1/2; the same is true of
M_n(p)/M_j(p) at every fixed vertex in generation j. Markov's inequality
and a countable union rule out every critical infinite open component.
For p>1/2, M_n grows exponentially and sum 1/M_n is finite, so the exact
second-moment identity bounds survival away from zero. This proves
p_c=1/2 independently of the finite audit. Under the uniform-spine law,
each off-spine subtree remains ordinary critical percolation. Countably
many vertexwise extinction events rule out every competing infinite ray
and every off-spine infinite component. The mixture classification therefore
has no hidden assumption of uniqueness under the unconditioned tree law.

Startup memory index and the verified macOS priority card were read
without running the brain recall logger, since its writes would violate
the task-specific folder restriction. Priority is read with getpriority,
not os.nice(0), in both scripts.

There is no Z^3 asymptotic estimate in this work. Tracking only the
root-connected boundary set fails by the explicit finite witness; the
correct state is the entire realizable boundary partition with root mark.
After that correction, the next missing step is still convergence of
r_(m,n)(pi) for every fixed m and realizable pi at p_c. Equivalently, prove
that the weighted oscillation D_m(n,l) tends to zero as n,l tend to infinity.
Convergence of the conditioned marked exterior partition law would suffice,
but is a stronger input than the response criterion and is not proved.
Do not confuse these exact conditioning identities with evidence that the
required ratios converge. No novelty claim is made.

## Completion check

Saved REPORT.md with the required first-line partial verdict. A final
standard-library check under nice -n 15 and OMP_NUM_THREADS=1 verified seven
nonempty deliverables, compiled both scripts without running them again,
checked both saved successful outputs, and independently recomputed
36 models, 41,760 configuration comparisons, 756 atom checks, and the
witness exponent 823 from graph sizes. Output:

    PASS: seven deliverables, script syntax, verdict, saved successful outputs, independent audit counts and witness exponent
    Priority: 20
    Peak RSS bytes (macOS): 16023552

All numerical checks completed successfully. The proof's last addition
states the positive witness-gap bound already checked by the audit; no
computation changed after the successful run. T160 remains unresolved.
Only this folder was modified; both earlier folders remain read only.
