# T078 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Session start 2026-11-15 08:03 +04 (04:03 UTC); exact user-message clock time unavailable.

## Orientation and brief literature check

Read the original session's REPORT.md, LOG.md, SOLVED_ELSEWHERE.md; round 3 REPORT.md, LOG.md, PROOF.md; and round 4 REPORT.md, LOG.md, PROOF.md. Inventoried all three folders using `rg --files` and `ls -la`: none contains a mathematical script, and the original session has no PROOF.md. No prior folder was edited.

Read `~/brain-views/BRAIN_INDEX.md` and the compute governor as read-only orientation. The current task prohibits all writes outside this folder, so memory recall with internal logging, mesh, and shared checklist mutation commands were not invoked. No git or subagents. Governor says `status: warn`, `mode: owner_away_open`, CPU saturated. Only short reads and exact mathematics are planned.

Shell reads after inventory used `OMP_NUM_THREADS=1 nice -n 15`. The sandbox reports `nice: setpriority: Operation not permitted` but executes the reads. No numerical computation is being run at unverified priority.

Web search queries: `quantum Heisenberg ferromagnet spontaneous magnetization OpenAI September 2026 proof MeshPin`; `"Heisenberg ferromagnet" "2026" "long-range order"`. The same September 24, 2026 claim and October companions appear; no new resolution or correction was established. Opened the primary manuscript landing page and `lean/docs/271.md`. Direct access to the formerly readable PDF failed. The scope note still claims the same theorem; this is not new evidence of correctness. The literature-update stage ends here, within five minutes. No new SOLVED_ELSEWHERE finding is asserted.

Opened primary source files MeshPin.lean, BoundaryMesh.lean, BootstrapParameters.lean through the web tool. The next dependency is `periodic_return_estimate`, followed by the regularity estimate; the parameter selection uses only scalar powers.

## Independent recheck of the round 4 result

Its main boundary-cost estimate holds. Here is an independent partition-sum removal argument. Let W(c)=2^{k(c)} and J(c) count active crossing layers. Removing an active crossing transposition changes cycle count by one, so W(c with that mark inserted)<=2 W(c with it removed). For any nonnegative multiplier H depending only on the other coins, let A=sum H w_other W_0 and B=sum H w_other W_1; then B<=2A. At crossing rate r,

    (1+r)[(1-r)A+r B/2]-[(1-r)A+r B]
       =r(1-r)(A-B/2)>=0.

Iterate removal over crossing layers. This proves E_nu[2^{-J}]>=product(1+r)^{-1}. Separately, a cycle visiting D without a layer-zero point in D must leave D; different such cycles use different directed exits. Each active crossing transposition supplies exactly one exit. Therefore n_D<=|D|+J and P(all boundary cycles up)>=2^{-|D|}product(1+r)^{-1}. This checks the bound without treating weighted coins as independent. With r=t/(2N), N sweeps, taking logarithms gives the coefficient t J_cross/2. Empty D, full D, rates zero/one, and deterministic within-side seam permutations do not invalidate either argument. Round 4's conditional magnetization implication also follows from Markov applied to the number of down slots, of mean at most np/2, at threshold n/4.

## Chosen extension, before doing it

Audit the spatial input `mesh_pin_bound`, beginning at its call of `periodic_return_estimate`. The goal is one checkable spatial statement or a precisely located obstruction, rather than another scalar or boundary-coloring improvement. Follow only the source dependencies needed to identify what is actually being estimated. If a universal finite-volume pinning bound fails under its printed assumptions, supply an explicit example; otherwise isolate and prove a genuinely spatial lemma needed by it. No complete Lean verification is claimed.

## Spatial dependency located; precise special case selected

Read PeriodicReturnEstimate -> BootstrapMeshBounds -> RegularPin -> PinBridge. The return estimate calls `Flow.indexed_prefix_leakage`. A read-only GitHub connector directory fetch succeeded where the web directory fetch failed; connector search located that theorem in PeriodicLeakage.lean. Read PeriodicLeakage.lean, RegularKernels.lean, MeanLeakage.lean, LayerRegularity.lean. These separate the problem into transport leakage, sparse injection flows on a perforated lattice, and probabilistic regularity. No false assertion was identified. Guessed Flow.lean / IndexedPrefixLeakage.lean / FlowLeakage.lean paths failed; these were access failures, not mathematical findings. Additional keyword searches were source-code navigation, not an extension of the literature stage.

Concrete ONE extension: prove the sparse injection estimate on the unperforated three-dimensional lattice, allowing any growth exponent 0<=alpha<1, and displacement R of injected mass from its sparse source labels. Establish energy <= C_alpha L (1+R)^alpha times the number of labels, uniformly over finite volumes containing the injection sites. This verifies an actual spatial special case of the role played by `regular_injection_energy`, rather than a scalar tilt or boundary-color count. The perforated-lattice case and its random regularity remain outside the result. A self-contained Green-function proof will also yield a Dirichlet-capacity lower bound. Check repeated labels, coinciding displaced endpoints, alpha=0, finite-volume boundary conditions, and the threshold alpha=1 before reporting.

The connector search returned immutable source links at revision `4eaee87548250b2682affda7d05d947c05554bae`; record that revision with any source comparison. No local Lean build or numerical run is planned, since requested niceness cannot be set in this sandbox.

## Spatial estimate proved

Wrote PROOF.md, Sections 1-5. Its full-lattice Green function, for rate one per edge and energy counting each undirected edge once, obeys G(x)<=1000/(1+|x|_infinity). The constant follows from an explicit heat-kernel and Chernoff argument, not a numerical approximation. The key sparse estimate is a layer-cake integral:

    sum_i [1+max(|x_i-z|-R,0)]^{-1}
       <= L integral_0^infinity (1+R+t)^alpha/(1+t)^2 dt
       <= L(1+R)^alpha/(1-alpha).

This gives the claimed energy bound by positivity of the killed Green function and the exact Dirichlet identity. The bound also produces an infinite-lattice current to infinity by cube exhaustion and a linear capacity lower bound for sparse sets. The proof includes finite-volume invertibility, boundary edges, and the generator/energy normalization. Next: independent estimates for the integral and energy identity, and sharpness or failure at the excluded cases.

## Attempts to break the result; exact second derivations

Added Sections 6-9 of PROOF.md. Coinciding endpoints are allowed and give a sharpness test: x_j=(floor(j^(1/alpha)),0,0), j<=floor(R^alpha), have growth L=3, while all mass can move to zero. The required energy is at least m^2/6, independently checked by the delta-function Dirichlet test and the walk's mean first holding time 1/6. Thus the displacement power alpha cannot be reduced.

At alpha=1 the straight segment of m labels has L=2 but energy at least m log(m)/(16pi^2) in the infinite-volume limit. A Fourier integral over a planar annulus proves the stated coefficient; a different rectangular integration region independently gives m log(m)/(24pi^3), confirming the logarithmic obstruction. No claimed source theorem is contradicted: its exponent is 1/100, strictly below this endpoint.

The layer-cake estimate has an independent dyadic-shell check, recovering both (1+R)^alpha and alpha<1. The exact denominator 1-alpha is re-derived with v=1/(1+t). The energy identity is checked both by grouping undirected edges and by the Fourier symbol sum_i |1-exp(i theta_i)|^2. The Green-function arithmetic before rounding is [192 exp(-2)+96sqrt(2pi)]/r, bounded by 432/r and then 864/(1+r); C=1000 includes r=0. All checks are analytical; no numerical script, heavy program, or local Lean compilation was run.

Remaining uncertainty: no source error has been found; the theorem just proved handles no removed sites. Domain/edge monotonicity goes in the wrong direction to infer the perforated case from it. The next worker should audit the geometric detour/flow construction under Regular, not repeat the scalar or boundary-cost calculations.

## Final audit and handoff

Command `OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md` read the entire proof back; `OMP_NUM_THREADS=1 nice -n 15 wc -l -c LOG.md PROOF.md` reported 56 lines/8470 bytes and 281 lines/16026 bytes before final additions. Priority setting was again denied. Clock then read 2026-11-15 04:11:53 UTC (08:11:53 +04).

Fetched RegularKernels.lean at immutable revision 4eaee87548250b2682affda7d05d947c05554bae: its 14792-character content exactly matched the previously inspected main-branch content. Connector searches and primary-file reads located `connected_envelope` in FlowCongestion.lean and `regular_component_envelope` in RegularComponents.lean. Those are now the precise handoff targets, not an unspecified pinning lemma. Their proof bodies were read to locate their role; no claim of verifying them is made.

Added the explicit decomposition into endpoint unit currents, so the proved bound matches the aggregate-current role of the source, with the stated edge-counting convention. Wrote REPORT.md with the required verdict, exact scope, commands, access failures, limitations, and next dependency. No SOLVED_ELSEWHERE.md is created: this session found no new established resolution beyond the already recorded claim.

Final read-only checks: `OMP_NUM_THREADS=1 nice -n 15 head -n 1 REPORT.md` returned the required PROVED verdict naming only the full-lattice sparse injection result. `wc -l -c LOG.md PROOF.md REPORT.md` under the same prefix returned 64/9717, 285/16935, 21/4298 (lines/bytes, before this append). `ls -la` confirmed the three deliverables, and `tail -n 18 PROOF.md` confirmed the scope and precise dependency links. The priority-setting denial persisted. Final clock: 2026-11-15 08:13:26 +04. This append records the check and ends the task.
