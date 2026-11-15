# T078 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Session date 2026-11-15, Asia/Tbilisi; exact user-message clock time unavailable.

## Orientation and literature check

Inventoried all four earlier directories with `rg --files`. There are no numerical scripts in those directories, and the first directory has no PROOF.md. Read the first and round 3 reports/logs/proof; reading rounds 4 and 5 is in progress. Read the startup memory index and compute state without writing to their stores. The task-specific ban on writes outside this directory excludes brain recall logging, checklist and mesh mutations. No git or subagents.

Shell reads use `OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints `nice: setpriority: Operation not permitted` but executes reads. No numerical program or heavy computation has been run. Compute state reports status `ok`, mode `owner_away_open`; this task needs only short reads and exact mathematics.

Web searches: `quantum Heisenberg ferromagnet spontaneous magnetization 2026 proof`, `"Heisenberg" "RegularComponents" "openai"`, and `"quantum Heisenberg ferromagnet" "November" "2026" proof`. Opened the existing September 24, 2026 manuscript's community landing page. Search again locates the same preprint and October follow-ups already known to earlier workers; no new resolution was established. The preprint remains a solution claim, whose spatial assumptions are the subject of this task, rather than a newly verified solution. Literature search stops within the five-minute allowance.

Read round 5 PROOF.md in full. Its main estimate uses rate one per edge, undirected energy and a full-lattice Green kernel; the next step must address removed vertices without making the invalid monotonicity comparison in the wrong direction.

## Earlier result rechecked independently

Finished reading round 4 PROOF.md, REPORT.md and LOG.md and round 5 LOG.md and REPORT.md. The directory inventories found no scripts to rerun. Short reads used `cat`; clock command `OMP_NUM_THREADS=1 nice -n 15 date '+%Y-%m-%d %H:%M:%S %z'` returned `2026-11-15 10:36:10 +0400`.

The round 5 bound holds. Here is a pair-interaction verification, different from its endpoint-centered potential estimate. Its heat-kernel proof yields BOTH G(x)<=3 and G(x)<=432/|x| for |x|>0. Hence G(x)<=435/(1+|x|): for r<=144 use 3, for r>=144 use 432/r. For injection endpoints a,b belonging to labels i,j, respectively, |a-b|>=(|x_i-x_j|-2R)_+. Thus their Green interaction is at most 435/[1+(|x_i-x_j|-2R)_+]. For each i, layer-cake summation against the label growth condition bounds the sum over j by L(1+2R)^alpha/(1-alpha). Summing the masses (each <=1) gives energy <=435 L(1+2R)^alpha m/(1-alpha), which is <=870 L(1+R)^alpha m/(1-alpha). This independently implies the reported coefficient 1000, including repeated labels and coincident endpoints. The killed Green comparison gives the same bound in every finite containing volume. The undirected energy identity has coefficient one; the one-site operator A_{ {0} }=6 checks it independently. These details will be written out in PROOF.md.

## Source inspection and choice of ONE extension

Fetched RegularComponents.lean and FlowCongestion.lean at immutable revision `4eaee87548250b2682affda7d05d947c05554bae` through the read-only GitHub connector after raw web opens returned cache misses. Also fetched their routing dependencies FlowRouting.lean and HullRouting.lean and the caller RegularKernels.lean. `regular_component_envelope` reduces near components to cardinality <2d using radius-8 connectivity, and transfers far component bounds by a triangle inequality. `connected_envelope` still depends on `routed_envelope`, then on finite hull routing and boundary connectivity. Reading these proof bodies is not a completed verification of their dependencies, and no source error has been found.

Chosen extension, before writing its proof: construct a uniformly bounded linear rerouting operator for the cubic lattice with an arbitrary set Z of removed sites satisfying |z-z'|_infinity>=3 for distinct holes. Prove that it preserves divergence at surviving sites for currents with zero divergence on Z, with energy cost at most a universal constant independent of the number of holes. Apply it to the rechecked sparse injections. This is a first perforated-lattice case of the spatial step that round 5 explicitly lacked. This local separation is a different geometric assumption from Regular and does not settle its general hypotheses. It permits explicit local bypasses and an independent dual extension argument, so the key geometric assertion can be checked without importing the manuscript's hull machinery. Examine adjacent bypass boxes, arbitrary signed currents, infinite Z, and finite Dirichlet boundaries; do not claim a finite-volume result unless boundary handling is justified.

## Rerouting theorem proved

Wrote PROOF.md with explicit paths in each radius-one cube around a hole. Five neighbor-to-hub paths replace the deleted six-edge star. The hub receives the right divergence because the original divergence at the hole is zero. Only two paths share edges, giving exact correction energy 2b^2+2(b+c)^2+2(d^2+e^2+f^2), at most six times the deleted star energy. Separation three makes these local correction supports disjoint, even for infinitely many holes. Thus the global linear operator costs at most seven in aggregate energy, by Cauchy-Schwarz between surviving-edge and deleted-star energies.

Applied to the independently rechecked round 5 current, this proves energy <=7000 L(1+R)^alpha m/(1-alpha) on the perforated graph. The estimate is for the aggregate current itself, so it incurs no extra factor of m. It allows every alpha<1, distributed/coincident endpoints and arbitrary many holes. The source's general Regular construction, which permits clusters, is not established.

An independent dual construction extends each test function to a hole by its hub value. Telescoping along paths gives full-lattice energy <=7 times perforated energy: the largest edge coefficient is 4+2=6, plus one for the original surviving-edge energy. This reproduces the finite-volume bound and capacity bound without an assumption that the finite volume contains the bypass cubes. The killed operator uses the degree in the surviving graph; a one-site volume next to a hole has energy 1/5, compared with 1/6 in the unperforated one-site volume.

All statements are exact analytical calculations, not numerical results. No script, numerical run, Lean build or heavy computation was needed. Writes used apply_patch only in this directory; source reads used the read-only connector. The two failed raw-source opens returned cache misses, not mathematical evidence.

## Attempts to break the result

Checked path vertices and all their pairwise overlaps by their displayed coordinates, signs of divergence at each endpoint and the hub, arbitrary signed star currents, empty Z, separation exactly three, infinite Z, repeated source labels, zero masses, alpha=0 and arbitrary finite Dirichlet boundaries. At separation three, cubes can have a connecting edge but have no common vertex: that edge remains an original surviving edge and creates no overlap of corrections. Both the flow and test-function proofs include boundary edges through zero extension.

Tested the tempting omission of geometric separation: the six removed neighbors of 0 isolate it and rule out a unit flow, although every radius-eight hole component has diameter two. This satisfies a component envelope with C=2,nu=0 but violates the source's strict local count <6. Thus it is a counterexample to using the envelope alone, and is not a counterexample to the source. At separation two the present disjoint-support proof fails; no impossibility claim is made for that case.

## Final audit and handoff

Read PROOF.md back in full. Added an independent local matrix check: the nontrivial 2-by-2 block has characteristic polynomial lambda^2-6lambda+4 and eigenvalues 3+-sqrt(5), both <6. Checked the final Cauchy-Schwarz step by the exact residual square (sqrt(6 E_surviving)-sqrt(E_deleted))^2. The dual proof independently checks the seven and the finite-volume bound. The Green constants were re-derived in Section 2, then used in a pairwise summation which independently recovers the earlier 1000; seven times that constant gives the stated 7000.

Clarified that separation three and the source's Regular condition are different restrictions, rather than asserting one implies the other: portions of 3Z^3 have separation three but unbounded radius-eight components. The theorem covers their intersection and also other separated configurations. The general spatial hypothesis is still unresolved by this work.

Wrote and reread REPORT.md. Final commands: `OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md`, `OMP_NUM_THREADS=1 nice -n 15 wc -l -c LOG.md PROOF.md REPORT.md`, `OMP_NUM_THREADS=1 nice -n 15 rg -n 'stronger than|factor|characteristic|Condition \(1\)|VERDICT' LOG.md PROOF.md REPORT.md`, and the prefixed date command. Outputs before this append: LOG.md 41 lines/7862 bytes; PROOF.md 252 lines/18507 bytes; REPORT.md 21 lines/3966 bytes. Report begins with the required PROVED verdict naming only the sparse injection result for isolated removed sites. Final clock: 2026-11-15 10:43:29 +0400. Priority-setting denial persisted; no computation was run at unverified priority.

All new files are in this directory. No earlier directory was edited, no git or subagent was used, and no shared memory/checklist/mesh, posting, messaging or other external mutation was performed. The next worker's concrete targets and the remaining cluster/congestion gap are in REPORT.md. No SOLVED_ELSEWHERE.md is warranted by the brief update check.
