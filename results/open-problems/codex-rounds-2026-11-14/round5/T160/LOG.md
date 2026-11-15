# T160 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 08:31 Asia/Tbilisi (04:31 UTC).

## Scope and orientation

All writes are confined to this folder. The specific instruction prohibiting
outside writes overrides the general brain, mesh and checklist write routines.
Read the startup memory index, mesh protocol and compute state without running
their logging commands. No git, subagents, background processes or external
publication. Compute state: warn/cpu_saturated, owner_away_open, 80% memory free;
only tiny standard-library exact enumerations are planned, each under nice 15
or the inherited lower scheduling priority, one thread, 120-second alarm and
less than 1 GB memory.

## Literature check, within the first five minutes

Searched the web for 2026 Bernoulli IIC existence in three dimensions and
quasi-multiplicativity. Opened these primary sources:

- Deepan Basu and Artem Sapozhnikov, arXiv:1603.06884,
  https://arxiv.org/abs/1603.06884 . The abstract assumes uniqueness and
  quasi-multiplicativity, verifies these for slabs, and does not prove the
  required three-dimensional Bernoulli input.
- Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe,
  arXiv:2502.10882, https://arxiv.org/abs/2502.10882 . The construction uses
  high-dimensional two-point asymptotics.
- Malo Hillairet, arXiv:2509.18852v3 (28 May 2026),
  https://arxiv.org/abs/2509.18852 . The setting is planar.
- Jian Ding and Zhenhao Cai, “Quasi-multiplicativity and Regularity for Metric
  Graph Gaussian Free Fields”, published 28 October 2026,
  https://doi.org/10.1007/s00220-026-05772-5 . Its model is the metric-graph
  GFF; the Bernoulli application is conditional on quasi-multiplicativity.

No verified resolution of T160 was found. The abstract of the last source
has a potentially misleading compressed statement about Bernoulli IICs;
the explicit conditional hypothesis in Remark 1.2 is decisive. No
SOLVED_ELSEWHERE.md is warranted. This was a short search, not an exhaustive
review. Literature-status check ends here.

## Independent re-derivation of round 4

For an interior atom eta, independence gives
P(eta,0<->boundary B_n)=alpha(eta) h(pi(eta)). Divide by the sum of these
atom weights and then group by pi. This independently gives the stated
mixture with lambda_pi=a_pi*r_pi/Z. The inverse is
r_pi=(a_star/a_pi)*(lambda_pi/lambda_star), and lambda_star>=a_star>0.
For two response vectors r,s, write Z=sum ar, W=sum as and D=sum a|r-s|.
Then 2 TV=sum|ar/Z-as/W| <= (D+|Z-W|)/Z <=2D/a_star.
Conversely |Z-W|=a_star*|lambda_star-gamma_star|/(lambda_star*gamma_star)
<=TV/a_star, so D<=2TV+TV/a_star. The main ratio criterion holds.
The full partition, including non-root components, is necessary: the
round-4 five-edge exterior return path uses the extra interior edge b-c.
Its 828 exterior edges and 823 closed-edge exponent will be independently
checked in the new script rather than assumed.

## Chosen extension, recorded before proof and computation

Prove and audit a uniform localization estimate for the round-4 exterior
response. For m<R<n, consider the ordinary, unwired exterior graph between
B_m and B_R. Call a component active if it meets both boundary B_m and
boundary B_R. The target is

  P(at least two active components | boundary B_m <-> boundary B_n)
      <= P(boundary B_m <-> boundary B_R),

where all connections use exterior edges. The proposed deterministic
inclusion uses disjoint occurrence: on the conditioning event choose the
last active component visited by a path to boundary B_n, and use another
component for an edge-disjoint connection to boundary B_R. Apply BK.
With exactly one active component, the full marked partition at radius n
is already determined at radius R. This should approximate every normalized
response with error at most the exterior one-arm probability, uniformly
over n>R and all realizable interior partitions. Under critical extinction
that error tends to zero for fixed m.

Why this piece: it supplies an actual vanishing error estimate on Z^3 for
the response state, while retaining all finite return components identified
in round 4. It does not assert that the remaining conditional finite-annulus
law converges. That distinction will be explicit in the proof and report.
The deterministic disjoint-path inclusion is the part most likely to fail;
test it by independent exhaustive finite-graph path enumeration, including
components that merge only outside the intermediate box.

## Read-through complete and deterministic argument refined

Read the complete REPORT.md, LOG.md, PROOF.md and all Python scripts in
the three source folders. No source file was run or edited. The round-3
tree classification and round-4 criterion are consistent with the direct
re-derivation above. Read the verified macOS priority memory: getpriority,
not os.nice(0), is the safe way to inspect inherited nice 20.

The path argument can be made precise without choosing an arbitrary
root-to-target path as the witness. Let U be the union of all local
components meeting the inner boundary. A path to the distant target has a
last vertex v in U. The local component containing v is active: an open
edge leaving it cannot stay within the intermediate graph. Join an inner
boundary vertex to v within that component and append the tail of the path.
Every other active component supplies an edge-disjoint short crossing.
Thus k active components give disjoint witnesses for one distant and k-1
intermediate crossing events. Iterated BK should give the geometric tail
b_(m,R)^(k-1), with constant one.

For the external theorem used in this extension, opened the original paper
J. van den Berg and H. Kesten, “Inequalities with Applications to Percolation
and Reliability” (1985),
https://sites.math.northwestern.edu/~auffing/papers/vBK.pdf . This is a
source check for the BK inequality, not a renewed literature-status search.
Also read Ding–Cai Remark 1.2 directly: it explicitly assumes the Bernoulli
quasi-multiplicativity hypothesis.

Plan for the exact audit: independently enumerate all open simple-path
witnesses and compare against the last-exit construction; compute the
conditional marked-partition law and its local reconstruction; test the
response approximation on every abstract interior partition of the finite
terminal set. Include outer mergers and nonmonotonic component counts.

## Independent round-4 computation

Created recheck.py using repeated set expansion for full connectivity and
a separate graph contraction for partition responses; no earlier imports
or code execution. Command:

    nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1

Exit status 0. Exact output:

    nice: setpriority: Operation not permitted
    PASS: 9216 full-connectivity versus contracted-partition comparisons
    PASS: 144 exact conditional atom laws and nine partition inversions
    PASS: 9 exact two-sided TV comparisons
    PASS: independent cubic degree counts and return-path witness; exponent 823
    Priority: 20; OMP_NUM_THREADS=1
    Elapsed seconds: 0.062
    Peak RSS bytes (macOS): 14581760
    PASS: round-4 result holds

The saved output is authoritative for timing and memory. The inherited nice
priority is 20, so the redundant relative nice request warns and retains a
lower scheduling priority than requested. The analytic criterion and the
finite checks agree; the earlier result holds.

## Extension proof saved

PROOF.md proves the disjoint-witness inclusion, its geometric component-count
tail with constant one, and reconstruction of the marked partition on the
one-active-component event. It gives the response error <=b_(m,R), the
normalized interior-law error <=b_(m,R)/a_star, and the oscillation bound

  D_m(n,l) <= 2 b_(m,R) + TV(Law(L_(m,R)|H_(m,n)),
                             Law(L_(m,R)|H_(m,l))).

The last conditional-law distance is not controlled. Under theta(p)=0,
b_(m,R)<=(24m^2+2)*alpha_p(R-m) tends to zero for each fixed m. The same
estimate proves that every subsequential conditioned law has a unique,
one-ended infinite cluster containing the root. This structural statement
does not prove uniqueness of the limiting law. Next: exact adversarial audit
of the finite deterministic inclusion and approximation constants.

## Exact localization audit

Created audit.py. It enumerates full edge configurations on six small
graphs, constructs the last-exit certificate, and separately enumerates all
simple-path witnesses to verify the required disjoint occurrence. Local
and full marked partitions are computed without using that certificate.
All abstract partitions of root plus inner terminals are tested, a superset
of those realizable by any particular finite interior. Probability checks
use exact rational arithmetic at p=1/3,1/2,2/3.

Command:

    nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1

Exit status 0. Output:

    nice: setpriority: Operation not permitted
    PASS: 6 graph models; 2560 complete configurations
    PASS: 1572 multi-path inclusions, independent exhaustive witnesses
    PASS: 874 one-active exact partition reconstructions
    PASS: 69 exact BK-tail bounds across 18 graph/parameter models
    PASS: 240 response approximation checks; 36 normalization checks
    PASS: 76 outer-merger test states; 16 component-count decreases
    PASS: seven independent cubic-boundary counts; |S_m|=24m^2+2
    Exact p=1/2 certificates: graph, b_local, P(multi | far), partition TV
    two_sources_cycle 15/16 3/43 7/129
    outer_merger 7/8 25/37 15/37
    two_stage_outer_merger 7/8 69/97 51/97
    local_return 7/8 3/5 12/25
    cyclic_local_return 15/16 61/121 37/121
    two_targets 7/8 95/139 57/139
    Priority: 20; OMP_NUM_THREADS=1
    Elapsed seconds: 0.080
    Peak RSS bytes (macOS): 16203776
    PASS: all exact checks

The tail checks include k=1 and impossible k>|S_m|, so their count does
not mean 69 distinct nontrivial inequalities. certificates.csv records exact
finite probabilities, not simulated lattice probabilities. These small
models verify the finite argument, not the unknown critical input.

Adversarial cases include two or three local active components merging
outside R, local cycles, a return through a different inner terminal,
multiple target vertices, and configurations where opening an edge
DECREASES the number of active components. Thus applying BK directly to
the active-count event would be invalid; the proof uses the disjoint-path
inclusion instead. The proof also uses the last visit to the union of ALL
inner-boundary components, not only the active ones.

Next: independently recompute the probability certificates with bitset
transitive closure and separate local/far edge sums; audit the
subsequential-limit argument without passing a non-cylinder event through
weak convergence.

## Independent recomputation and final adversarial audit

Created independent.py without importing the audit. It computes
connectivity by bitset transitive closure, splits the product sum into local
and far configurations, and recomputes all five probability columns in
certificates.csv. On these six models it also checks the local crossing
probability a third way, as one minus the probability that every edge
leaving the inner source set is closed.

Command:

    nice -n 15 env OMP_NUM_THREADS=1 python3 independent.py > independent_output.txt 2>&1

Exit status 0. All 90 certificate values agree. The 18 local/far
decompositions agree with full enumeration, and the six edge-count products
independently sum to 2560 complete configurations.

Two audit diagnostics were refined before final reporting. recheck.py
initially printed “nine partition inversions”, meaning nine models, but
actually checked 108 individual inversions; it now counts them explicitly.
The initial “outer-merger” diagnostic tested a full connection between two
inner terminals, which could already exist locally. It now requires a
merger of two DISTINCT local active components. That exact count is 87,
replacing the earlier diagnostic count 76. Neither correction changes a
theorem, inequality, response probability or CSV value. All three scripts
were rerun sequentially with the commands above, each exiting 0. Final
outputs are recheck_output.txt, audit_output.txt and independent_output.txt.

Final recheck: 9216 connectivity comparisons; 144 conditional atoms;
108 partition inversions; 9 TV comparisons; cubic witness exponent 823.
Runtime 0.058 seconds, peak RSS 14,942,208 bytes.

Final extension audit: 2560 configurations on 6 graphs; 1572 disjoint-path
inclusions; 874 exact reconstructions on the one-active event; 69 tail
checks across 18 parameter models; 240 response checks; 36 normalization
checks; 87 true outer-merger states; 16 decreases in active count.
Runtime 0.078 seconds, peak RSS 16,318,464 bytes.

Final independent audit: 90 matching exact probability values and 18
independent closed-cut checks. Runtime 0.085 seconds, peak RSS 15,613,952
bytes. Every run reported priority 20 and OMP_NUM_THREADS=1.

Analytic checks independent of the numerical audit:

- The constant one in the conditional tail bound comes from exactly one
  long witness plus k-1 short witnesses. No union bound over source
  vertices, and hence no omitted source-cardinality factor, occurs there.
- Re-derived the response error by the shared bad event and separately by
  the coupling bound on partition total variation. Both give b_(m,R).
  Normalizing adds at most the factor 1/a_star, as in the round-4 lemma;
  comparing two radii adds exactly two approximation errors.
- Re-derived |S_m| by subtracting the two cube volumes and by enumerating
  the boundary vertices for m=1,...,7. The constant is 24m^2+2.
- The local component count is never computed with S_R wired. The
  reconstructed state retains every finite boundary component. Several
  surviving components can be wired together at the distant target; the
  proof charges this to the bad event instead of identifying them early.
- The last-exit tail avoids the union of all local source components,
  including inactive ones. The selected component is active because the
  very next edge leaves B_R. This prevents a hidden return-path error.
- In the subsequential-limit corollary, only the finite event
  {N_(m,R)>=2} passes through cylinder convergence. The event of two
  infinite exterior components is bounded by that finite event for every
  R, then assigned probability zero using b_(m,R)->0. No passage of an
  infinite event through weak convergence is assumed.
- Deleting finitely many edges from a connected locally finite infinite
  graph leaves finitely many components and at least one infinite one.
  This justifies the one-endedness argument after enclosing a proposed
  finite vertex cut inside B_m; the boundary vertices of B_m are retained
  in the exterior graph.
- Small-graph probabilities such as 25/37 and 15/37 are exact examples,
  not estimates for actual cubic annuli. The vanishing-error statement on
  Z^3 depends on theta(p)=0; that premise has not been established here
  at p_c.

What remains: the conditional law of L_(m,R) given H_(m,n) can still
change with n. Critical extinction controls the reconstruction error,
not that conditional law. The earlier tree illustrates the distinction:
one-ended subsequential limits need not coincide. No contraction,
quasi-multiplicativity, or three-dimensional IIC convergence is proved.

## Completion

Saved REPORT.md with the required first-line verdict. A final inline
standard-library validation, launched as
`nice -n 15 env OMP_NUM_THREADS=1 python3 -`, read all ten deliverables,
compiled the three scripts in memory without creating bytecode files,
checked the successful terminal line in each saved output, verified the
18 CSV rows and independently recalculated the main audit counts from
graph sizes and partition counts. Output:

    nice: setpriority: Operation not permitted
    PASS: ten nonempty deliverables, required verdict, script syntax and three successful saved runs
    PASS: 18 exact CSV rows and independent totals 2560, 240, 69, 9216, 108
    Priority: 20 ; OMP_NUM_THREADS=1
    Peak RSS bytes (macOS): 16613376

One attempted completion-log patch was rejected by JavaScript parsing
before execution; the corrected call saved this entry. No proof or
computation changed after validation. All writes stayed inside this task
folder. The new localization lemma is proved; the existence and uniqueness
of the T160 limiting law remain unresolved here.
