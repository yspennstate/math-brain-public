# T160 work log, round 6

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 11:06 Asia/Tbilisi (07:06 UTC).

## Scope and startup

All writes stay in this folder. The task-specific prohibition on outside
writes takes precedence over the general brain, mesh and checklist logging
commands. Read the startup memory index and the compute state; no logging
command that might mutate the shared store was run. No git or subagents.
The compute state reports ok, owner_away_open, 62% free memory. Only small
standard-library enumerations are planned, under nice 15 (or inherited
lower priority), OMP_NUM_THREADS=1, with a time limit and memory guard.

## Literature check

Within the first three minutes, searched the web tool for
`"incipient infinite cluster" "three dimensions" 2026 existence` and
`"incipient infinite cluster" "quasi-multiplicativity" 2026`.
Opened the primary arXiv pages:

- Deepan Basu and Artem Sapozhnikov, *Kesten's incipient infinite cluster
  and quasi-multiplicativity of crossing probabilities*,
  https://arxiv.org/abs/1603.06884 . Its construction assumes
  quasi-multiplicativity and uniqueness, and verifies the slab case.
- Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe,
  *Robust construction of the incipient infinite cluster in high dimensional
  critical percolation*, https://arxiv.org/abs/2502.10882 . The input remains
  high-dimensional two-point asymptotics.
- Zhenhao Cai and Jian Ding, *Incipient infinite clusters and volume growth
  for Gaussian free fields and loop soups on metric graphs*,
  https://arxiv.org/abs/2412.05709 . This is a different percolation model.

An attempted HTML opening of arXiv:2412.05706v3 returned 404; it is not
used as an opened paper. No verified resolution of the Z^3 Bernoulli
problem was found. The status check ends here; no SOLVED_ELSEWHERE.md
is warranted by these sources.

## Read-through in progress

Read round 5 PROOF.md and LOG.md, the three earlier reports, and the
startup memory index. The round-5 last-exit construction appears valid:
take the last vertex of a target path in the union of all local components
meeting the inner boundary; replace its prefix inside that component.
The tail misses every other inner-boundary component, so these supply
disjoint short crossings even when mergers occur outside the local box.
Complete independent verification and the choice of extension follow below.

## Independent recheck of round 5

All four earlier folders' reports, logs, proofs and Python scripts have now
been read. No earlier script was imported or run in its source folder.
Independently contract every local component meeting S_m to a single node.
A simple path from the contracted source set to the target has a last source
node. Lift a path inside that component to its departure point; all other
active nodes supply disjoint short crossings. BK therefore gives exactly
b_(m,n)*b_(m,R)^(k-1). One active component cannot absorb another component
meeting S_m through later edges, because those other components miss S_R.
This independently recovers reconstruction and the response-error bound.
The earlier result holds analytically, including its one-endedness argument.

Created recheck.py using union-find, inclusion-minimal witness edge sets,
and exhaustive set packing, independently of the earlier simple-path audit.
The first run, `nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py >
recheck_output.txt 2>&1`, stopped at startup: macOS rejected setting
RLIMIT_AS to 800 MB with `ValueError: current limit exceeds maximum limit`.
No enumeration had started. Use RLIMIT_DATA at 800 MB, a 120-second alarm,
and measured peak RSS below 1 GB instead; rerun next.

The RLIMIT_DATA attempt was also rejected before enumeration. A tiny
read-only Python probe reported both DATA and AS limits as
9223372036854775807 and peak RSS 11,780,096 bytes. Removed unsupported
limit-setting calls. The enumeration has a fixed state space of fewer
than 2,000 masks, a 120-second alarm, and a final measured-RSS assertion.

The corrected command exited 0. Output:

```text
nice: setpriority: Operation not permitted
PASS: 1280 configurations; 937 independent disjoint-witness inclusions
PASS: 742 exact one-active partition reconstructions
PASS: 33 exact BK-tail bounds and nine localization-error bounds
Priority: 20; OMP_NUM_THREADS=1
Elapsed seconds: 0.012
Peak RSS bytes: 14270464
PASS: round-5 result holds
```

## Chosen extension, before proof and computation

Prove a uniform finite-box approximation for membership in the *full*
root cluster, then use it to pass the ordinary cluster spatial Markov law
to every subsequential cylinder limit under the extinction premise.
The proposed conclusion is: conditional on the vertex set C of the infinite
root cluster, edges with both endpoints outside C remain independent
Bernoulli(p). Equivalently, deleting C leaves ordinary product percolation
on the induced complement. Its residual configuration is stochastically
dominated by unconditioned Bernoulli percolation.

Why this piece: root-cluster membership is not a cylinder observable, so
the ordinary finite-cluster factorization cannot simply be passed through
cylinder convergence. Round 5's one-active-component estimate should
supply exactly the missing uniform approximation, including paths that
return from beyond the intermediate box. This extends the characterization
of subsequential limits, without purporting to control their remaining
survival-weight oscillation. No novelty claim is intended.

Target error: for fixed m<R<n, with a_star as in round 4,

  mu_n(C(0) intersect B_m != C_R(0) intersect B_m)
      <= b_(m,R)/a_star.

Here C_R is the root component using all edges of B_R. The same bound
should hold under any subsequential limit mu. It will yield joint
convergence of local edge states and full-root-cluster membership along
the same subsequence, which is stronger than edge-cylinder convergence.
Audit by exact small-graph enumeration with exterior returns, mergers,
cycles, several targets, and non-root internal edges; recompute the
conditional background laws independently by factorization over cluster
boundaries.

## Proof saved

PROOF.md now proves the uniform cluster-mark approximation, joint convergence
of local edges and full-root membership, and the conditional product law
outside the root cluster. The deterministic argument uses the full graph
inside B_R: every component meeting B_m and S_R contains the unique active
exterior component, so all such components coincide with the root component.
Every other component meeting B_m misses S_R and cannot change afterward.

For joint laws the explicit bound is

  TV(Gamma_n^m,Gamma_mu^m) <= 2*b_(m,R)/a_star
                               + TV(mu_n|F_R,mu|F_R).

Fix R before taking the subsequential limit; only then send R to infinity.
The full-root factorization under mu_n is proved by summing over finite
root-cluster vertex sets W: {C=W} fixes internal connectivity and closes
the edge boundary, leaving all induced-complement edges independent.
The joint convergence passes this identity for finite membership tests;
the bounded monotone-class theorem extends to all measurable functions
of C. A coupling with fresh independent product edges gives residual
stochastic domination. The proof includes a second derivation by passing
finite-n domination directly through joint convergence.

Next: exact finite-graph audit and independent cluster/cut calculation.

## Exact finite audit

Created audit.py, a BFS-based enumeration of five graphs with 7--13 edges.
The models include returns through the inner graph, returns beyond the
intermediate boundary, cycles, multiple targets, and a detached cyclic
background. Tests use exact rationals at p=1/3,1/2,2/3. They check the
root-cluster trace, complete stabilization of non-root components meeting
the inner region on the good event, the normalization bound, the joint-TV
error, every conditional background pattern given each possible root
cluster, and an explicit monotone coupling with independent product edges.

Command:

    nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1

Exit status 0. Output:

```text
nice: setpriority: Operation not permitted
PASS: 5 finite graphs; 12928 complete configurations
PASS: 1670 one-active root-trace reconstructions; 707 frozen non-root components
PASS: 125 genuine exterior-return trace changes, all charged to the bad event
PASS: 15 exact probability and joint-TV bounds
PASS: 1620 conditional product-pattern identities; 438 cluster normalizations
PASS: 543 residual-law atoms matched by explicit monotone coupling
inner_return P(E)=35/256 bad=4/7 trace_error=4/35 joint_TV=4/35
outer_return P(E)=19/128 bad=9/19 trace_error=2/19 joint_TV=2/19
background_cycle P(E)=957/4096 bad=230/957 trace_error=28/957 joint_TV=28/957
two_targets P(E)=515/2048 bad=371/515 trace_error=59/515 joint_TV=59/515
isolated_background P(E)=1/16 bad=3/4 trace_error=0 joint_TV=0
Priority: 20; OMP_NUM_THREADS=1
Elapsed seconds: 2.033
Peak RSS bytes: 17874944
PASS: all exact cluster-background checks
```

The exact per-cluster and residual distributions are saved in
certificates.json. The table values concern the finite test graphs, not
critical cubic-lattice probabilities. Positive trace-error cases show
that simply passing root-cluster membership through cylinder convergence
would miss a real event. The exceptional-event estimate, rather than an
assumption that local root membership is already exact, is necessary.

Created independent.py. It uses a triangular recurrence over induced
vertex sets W:

  1 = sum_{A subset W, 0 in A} conn(A)*(1-p)^cut_W(A).

Solve for conn(W), multiply by the probability that the full edge boundary
of W is closed, then normalize over W that hit the target. This does not
enumerate open configurations or import any audit helper. Mixing product
laws on each complement should independently reproduce every saved
cluster and residual atom. Run next.

Command:

    nice -n 15 env OMP_NUM_THREADS=1 python3 independent.py > independent_output.txt 2>&1

Exited 0. The independent recursion reproduced all saved probabilities.
Exact output is independent_output.txt; counts and resource use are recorded
in the final audit below. This gives a second computation of every
load-bearing probability in the new background factorization, using
vertex subsets and closed cuts rather than full open-edge configurations.

## Strengthened conditioning and second audit

Refined the same extension to condition on the *full* root-cluster record
(C,tau), where tau retains all internal open-edge states and is zero
elsewhere. The finite-cluster independence proof allows any function of
that record; the local joint convergence also includes its finite edge
coordinates. Therefore the complement product field is independent even
after all internal root-cluster information is specified. This avoids
leaving a possible hidden dependence between internal cluster edges and
the background after conditioning only on the vertex set.

The whole configuration is reconstructed from the record plus independent
Bernoulli edges on its complement. Finite coordinates of that reconstruction
use only finite record coordinates. Consequently convergence of the
root-cluster-record laws is equivalent to the original edge-cylinder
convergence, under extinction. This is a reduction of the unresolved
distribution, not a proof that the record laws converge.

Two initial proof-patch attempts had mismatched context and changed no file;
the corrected patch saved the stronger statement. Updated audit.py to test
all background patterns conditional on each full record, and independent.py
to compute every record mass directly as

  p^(number of open internal edges)
    * (1-p)^(number of closed internal edges + boundary edges) / P(E).

The existing vertex-set recursion still independently computes the denominator
and every vertex-set and residual mass. Rerun these two scripts sequentially
because the tested assertion was strengthened.

## Final exact runs and independent localization audit

The strengthened audit command exited 0. It retained all earlier counts
and additionally passed 7,938 background-pattern identities conditional
on 6,207 full root-cluster records across the 15 graph/parameter models.
The monotone coupling matched all 543 residual-law atoms. Final runtime
was 2.014 seconds, peak RSS 19,169,280 bytes, priority 20, one thread.
Exact output is audit_output.txt.

The first strengthened independent run verified 7,203 values. Extended
the same independent calculation to audit the numerical localization
columns as well: reconstruct successful configurations from independently
weighted root records and product complement patterns, compute annulus
components by bitset transitive closure, and sum the trace-error, bad-event
and joint-TV values. Recompute a_star from the induced-set recurrence,
and the two exterior arm probabilities from separate exterior-edge sums.
This is a different decomposition from the audit's full-configuration BFS.

Final command:

    nice -n 15 env OMP_NUM_THREADS=1 python3 independent.py > independent_output.txt 2>&1

Exit status 0. Output:

```text
nice: setpriority: Operation not permitted
PASS: 142113 independent induced-subgraph connectivity recurrence terms
PASS: 7293 exact event, cluster, full-record, residual and localization values independently reproduced
PASS: 15 cluster/cut factorizations and residual product-mixture laws
Vertex-set recursion, closed cuts and cluster-conditioned reconstruction; no audit imports.
Priority: 20; OMP_NUM_THREADS=1
Elapsed seconds: 0.480
Peak RSS bytes: 17285120
PASS: all independent cluster-background checks
```

Independently recounted the certificate checks: 15 event probabilities,
438 vertex-cluster masses, 6,207 full-record masses, 543 residual atoms,
and 6*15 additional localization values total 7,293. For a graph with v
vertices, the triangular recurrence has 3^(v-1)-2^(v-1) proper-subset
terms. The five vertex counts are 8,7,9,10,10; three parameters therefore
give exactly 142,113 terms, matching the measured count.

## Adversarial analytic audit

- Re-derived the deterministic localization two ways: use the last exit
  from B_m of a path to S_R to identify its unique active exterior
  component; equivalently, distinct full local components meeting both
  B_m and S_R would contain distinct active exterior components. Once
  there is just one, every other local component meeting B_m is trapped
  away from S_R and cannot change when farther edges are added.
- A far path can join an inner vertex to the root without any local
  connection. The outer-return graph has conditional trace error 2/19
  at p=1/2; 125 complete test configurations exhibit this phenomenon.
  Every such case has at least two active exterior components. No
  assumption of immediate local root-membership agreement is used.
- The conditioning denominator is bounded by requiring the single-block
  interior independently of H_(m,n), not by applying BK to root survival.
  This gives precisely b_(m,R)/a_star. It need not be less than one at
  small R; fixed m and extinction suffice to make it vanish eventually.
- Both approximations in the joint-law triangle inequality cost epsilon,
  explaining the factor two in (7). Only finite events pass through
  cylinder convergence. Full cluster membership is passed only after
  the uniform estimate has been proved. In the new two-horizon bound
  (10), reconstruction is a common probability kernel, so total variation
  contracts; the reverse comparison uses the same two approximation errors.
- The finite factorization conditions on all internal root-cluster edges,
  including closed ones, not only its vertex set or a chosen spine.
  The event {C=W} closes the entire edge boundary. Hence the remaining
  induced-complement edges are free product edges. The 6,207 record
  normalizations and 7,938 conditional pattern checks test this stronger
  assertion, including configurations with internal cycles.
- There is no independence assertion for edges crossing the cluster
  boundary: they are closed. Nor is the whole residual configuration
  unconditionally a product law. Its random allowed domain depends on
  the sampled root cluster. The coupling first samples the root record,
  then an independent full product field, then deletes all edges incident
  to the record's vertex set. It gives domination, not equality with P_p.
- Re-derived domination both directly by this conditional coupling and
  by passing the finite-n domination inequalities through the established
  joint convergence. These routes agree. The stronger factorization
  also reconstructs the entire edge configuration from its root record.
- Extinction is used twice: root clusters under mu_n are finite, allowing
  the sum over finite W, and b_(m,R) vanishes as R grows. Under the
  subsequential law the root cluster is infinite; its conditional product
  background is proved by the uniform approximation and a monotone-class
  argument, never by summing over finite clusters under that law.
- All numerical probabilities are exact fractions. The examples are
  finite graphs and supply no estimate of cubic-lattice critical decay.
  No finite calculation replaces the analytic limiting argument.

## What remains unresolved

No survival-weight comparison, quasi-multiplicativity, or contraction of
the root-cluster-record laws was obtained. The reduction isolates that
distribution as the remaining issue: every subsequential law is its
root record plus independent product background, but different record
laws may still occur. The earlier tree obstruction is compatible with
this conclusion. The theta(p_c)=0 premise and T160 remain open here.
No novelty claim is made for the spatial Markov factorization.

Next: save REPORT.md with the partial verdict and audit the saved artifacts.

## Completion

Saved REPORT.md with the required first-line partial verdict. Ran a final
inline standard-library check under `nice -n 15 env OMP_NUM_THREADS=1
python3 -`. It read the ten deliverables, compiled script sources in memory
without creating bytecode files, checked all successful saved outputs,
verified all 15 certificate normalizations, and independently recovered
the graph sizes from audit.py's syntax tree. Output:

```text
nice: setpriority: Operation not permitted
PASS: ten nonempty deliverables, required verdict, script syntax and three successful outputs
PASS: 15 certificates; 438 vertex clusters, 6207 full records, 543 residual atoms; 7293 values
PASS: independent counts 12928 configurations and 142113 recurrence terms
Priority: 20 ; OMP_NUM_THREADS=1
Peak RSS bytes: 19070976
```

Exit status 0. No proof or script changed after this validation. The last
edit is this completion log. The auxiliary theorem is proved under
extinction; existence of the T160 limiting law remains unresolved.

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, approximately 11:06 Asia/Tbilisi.
