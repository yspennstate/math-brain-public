# T078 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Session start 2026-11-15 04:40 +04; exact user-message time unavailable.

## Orientation and prior work

Read both prior REPORT.md, LOG.md, SOLVED_ELSEWHERE.md, and round 3 PROOF.md. `find` confirms no mathematical scripts in either folder and no PROOF.md in round 1. Both folders remain untouched. Read compute state: status warn, owner_away_open, CPU saturated. No heavy computation planned. Task-specific local-only writes override the global mesh/checklist/memory write instructions; those stores will not be changed.

Read-only shell commands used `OMP_NUM_THREADS=1 nice -n 15` with `cat` and `find`. The sandbox reports `nice: setpriority: Operation not permitted`, though commands execute. No successful priority adjustment is claimed. An initial brain recall was started under the same prefix, unexpectedly imported ONNX, and was interrupted rather than allowed to continue; this was an orientation attempt, not mathematical computation. Its internal recall logging was not inspected, so no claim is made that the attempted recall was internally side-effect-free. No further brain recall will be launched. No git, subagents, or numerical computation. All explicit file edits are confined to this folder.

## Initial literature check

Web searches: `quantum Heisenberg ferromagnet OpenAI September 2026 proof long range order`; `Heisenberg ferromagnet spontaneous magnetization 2026 mesh_matrix_surface`. They recover the existing September solution claim, not a newly established resolution or correction. Inspecting primary sources within the five-minute search allowance.

Opened CompletedSurface.lean and MeshRoom.lean via the web tool. The former invokes `mesh_matrix_surface` at line 31; MeshRoom imports PeriodicCount. This is the exact next input named in the round 3 report. Merely finding the same claim is not independent certification that T078 is solved.

## Independent recheck of the round 3 scalar result

With Y=8M/V and z=bV/8, the signed numerator for the target tilted mean is E[(Y-1)e^(zY)]. Tail Y>=2 contributes at least e^(2z). Write x=1-Y on Y<1, so x ranges over (0,5]. Its negative contribution has magnitude e^z x e^(-zx). Independently maximize this using the logarithmic derivative 1/x-z: x=5 when z<=1/5; x=1/z when z>=1/5. Thus the exact lower bound is L e^(2z)-(1-L)5e^(-4z), or L e^(2z)-(1-L)e^(z-1)/z. These reproduce both previous criteria. Two-point masses L at Y=2 and 1-L at Y=1-x attain them. At z=0 the minimum mean is 6L-4, giving L>=5/6. Both branches agree at z=1/5. The earlier result holds on its stated domain b>=0, V>0, 0<L<=1. It makes no claim that the requisite spatial tail is proved.

## Chosen extension, before doing it

Audit the finite-mesh surface-tail input `mesh_matrix_surface`, following the imports from CompletedSurface. The aim is one independently checkable estimate or a definite obstruction, not certification of the entire manuscript. Stop if the initial literature check establishes a resolution; otherwise isolate the first substantive probabilistic inequality on which the tail depends. Record its hypotheses and test its limiting or small finite cases analytically before making a verdict.

## Literature check closed; first dependency identified

The initial update check ended within five minutes. Searches for a 2026 correction and the exact lemma recover the same September 24 and October 5 claims, already known in round 3. Opened the actual 54-page September manuscript by OpenAI via its catalogue PDF link and rechecked equation (1.1) and Theorem 1.1: same model and S/4 KMS-state claim. No new proof certification or correction was established; continue the requested audit. No arXiv identifier established for this manuscript.

Opened MeshMatrixSurface.lean: `mesh_matrix_surface` is a conversion of `mesh_surface_tail` from a normalized loop probability into a trace inequality, using positive partition function and the mesh trace identities. It does not itself prove the probabilistic tail. Import chain: CompletedSurface -> MeshRoom -> PeriodicCount -> MeshMatrixSurface -> ColorClockLimit -> ExchangeOnMesh. MeshRoom's arithmetic check independently holds: delta(k+1)=t and 2(s+delta)<=t imply 2(floor(s/delta)+1)<=k+1; multiplication by Q preserves it. This does not check the tail.

The first interruption request to the brain recall returned completed/terminated output (not retained in the truncated combined display); a second returned `Unknown process id 11694`. No orientation worker remains associated with that session. The attempt is not used as evidence about the mathematics.

## Concrete audit target and proposed improvement

Located the substantive source in MeshSurface.lean (a guessed MeshSurfaceTail.lean returned 404). Its `mesh_surface_tail` has two inputs: the deep `Bootstrap.mesh_pin_bound`, and `BoundaryMesh.mean_boundary_cycles`. BoundaryMesh proves a deterministic bound of |D|+2 times the active K-marks, then uses mean active marks <=2 sum rates. This gives |D|+4 sum rates and the exponential cost in MeshMatrixSurface. The bootstrap is still unaudited.

Choose this boundary-cost estimate as the ONE concrete extension. It is a finite combinatorial/probabilistic part of the requested mesh audit and admits an independent proof. A transposition crossing D has exactly one directed exit from D; transpositions with both endpoints in D have none. Thus the proposed deterministic improvement is n_D<=|D|+J_cross, where J_cross counts only active crossing transpositions. Furthermore, under the unpinned 2^cycles law, changing one coin changes the cycle count by one, so its conditional activation probability is at most 2r/(1+r). Iterating conditional expectations should give

    P(all cycles meeting D are up) >= 2^(-|D|) product_cross (1+r_j)^(-1).

At uniform spatial rate r=delta/2 this is 2^(-|D|)(1+delta/2)^(-K_cross). In a fixed-time mesh limit it becomes 2^(-|D|)exp(-t J_cross/2). The earlier coefficient was 2 log(2) t J_K and J_cross<=J_K. Derive both estimates in full, verify the one-coin ratio and cycle orientation a second way, and test degeneracies before claiming them. This proves no bootstrap estimate.

Primary sources opened for this step: MeshMatrixSurface.lean, MeshSurface.lean, BoundaryMesh.lean; September manuscript, Lemma 8.1, read at printed pages 46–47. The source's boundary argument has slack; no false source assertion has been found. Attempted GitHub directory/API listings failed and are not evidence of missing files.

## Boundary estimate proved and challenged

Wrote PROOF.md with a complete finite-mesh theorem. The base coins are independent only before weighting by 2^cycles. The proof uses no independence under that weighted law. A crossing active transposition supplies one directed exit, giving n_D<=|D|+J_cross. Flipping a nonidentity coin splits or merges exactly one permutation cycle; the conditional cycle-weight ratio is at most 2. Hence conditional activation is at most 2r/(1+r), and the conditional expectation of 2^(-coin) is at least 1/(1+r). Iteration proves the proposed product bound, including rates 0 and 1.

Second derivation: with the other coins summed out (and arbitrary nonnegative factors on them), weights A,B with B<=2A satisfy

    [(1-r)A+(r/2)B]-[(1-r)A+rB]/(1+r)
      =r(1-r)(A-B/2)/(1+r)>=0.

This rechecks the exact denominator and factors 2. A separate cycle traversal checks the one-exit count. Empty D, full D, no crossing layers, identity transpositions, and deterministic coins all satisfy the claim.

Exact two-slot test, two crossing layers at rates r,s: loop partition Z=4-2r-2s+4rs; pinned partition Z_D=2-r-s+rs. The four configurations have cycle counts 2,1,1,2 and boundary-cycle counts 1,1,1,2. The difference after clearing the proposed bound's positive denominators is 2[2r+2s-r^2-s^2-rs+r^2s^2]>=0 on [0,1]^2. At r=s=1 the actual coloring probability is 1/4. This breaks a tempting stronger bound based only on boundary slots at the seam. One crossing layer instead has probability 1/2, showing that the proved product bound is not generally sharp.

Conditional spectral tail: if every time-zero slot avoids the pins with probability <=p under the all-boundary-cycles-up law, the conditional mean is >=n(1-p)/2, so the probability of M>=n/4 is >=1-2p. Thus multiply the proved boundary probability by 1-2p. For N repeated spatial sweeps at rate delta/2, delta=t/N, the product factor tends to exp(-t J_cross/2). The source's corresponding time exponent is 2 log(2) t J_K, with J_cross<=J_K. This is an improvement of the boundary cost conditional on the same bootstrap, not a temperature threshold or a proof of spatial order.

Opened MeshPin.lean: the remaining `mesh_pin_bound` calls `periodic_return_estimate` at line 45, `regularity_of_pin_induction` at line 46, `choose_parameters` at lines 47–49, and closes a finite pin induction. These spatial estimates are outside the proved boundary-cost result. No counterexample to the manuscript has been found, and no Lean compilation or full formal audit was performed.

## Independent continuous-time check and final audit

Added a separate Poisson derivation: the unweighted mean crossing count is Lambda=t J_cross/2. Inserting one crossing transposition changes cycle weight by at most a factor 2. Under a Laplace tilt exp(-u J), the weighted mean count is therefore <=2 Lambda exp(-u). Integrating the logarithmic derivative from u=0 to log 2 gives E[2^(-J)]>=exp(-Lambda). This reproduces the coefficient 1/2 independently of the finite-mesh logarithm limit. The Poisson insertion identity is justified directly by reindexing the factorial series in PROOF.md.

The scalar sufficient bound from round 3 also survives a separate convexity check: for g(z)=log E exp(zY), g''=Var_z(Y)>=0 and g(0)=0 imply g'(z)>=g(z)/z>=2+log L/z. For z>=log(1/L) this is >=1; the z=0,L=1 endpoint is immediate. Thus its convenient bV>=8 log(1/L) bound is valid as well as its exact criterion.

Wrote REPORT.md with the required PROVED verdict naming only the finite-mesh boundary-cost result. Re-read the entire PROOF.md and REPORT.md using `OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md REPORT.md`. Output confirms both derivations, every hypothesis, and the stated remaining spatial input. Added an independent Markov-inequality check of the factor 1-2p. The two-layer example with its second coin fixed active attains the conditional bound 2r/(1+r), checking the factor 1/(1+r) exactly. Corrected the report to distinguish source filenames from Lean namespaces.

Final artifacts are LOG.md, PROOF.md, REPORT.md. No mathematical script was needed or run; no local formal verification is claimed. All formulas and test cases are exact. The next task is the uniform spatial input in MeshPin.lean, not another field-selection or boundary-coloring refinement.

Final command outputs: `head -n 1 REPORT.md` returned `VERDICT: PROVED smaller boundary-coloring cost for finite transposition meshes`. `wc -l -c LOG.md PROOF.md REPORT.md` returned 70/10909, 195/14836, and 26/3996 (lines/bytes, before this final log append). Both commands had the OMP/nice prefix and again reported priority-setting denied. Final clock: 2026-11-15 04:49:46 +04. This append records that verification and ends the task.
