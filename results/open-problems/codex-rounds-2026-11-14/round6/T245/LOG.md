# T245 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 11:27 Asia/Tbilisi (session receipt, minute precision).

## Orientation and bounded literature check

The task-specific folder-only rule supersedes global requests to write checklist, mesh, recall logs, or brain memories outside this folder. Read the startup memory index and compute state directly. Compute state was ok, owner_away_open; nevertheless every computation will be single-threaded under `OMP_NUM_THREADS=1 nice -n 15`, standard library only, below 1 GB and 20 minutes. No subagents, git, or external messages. Earlier folders remain read-only, including bytecode.

Literature check started at approximately 11:28 Asia/Tbilisi and ended before 11:31, within five minutes. Used the web search tool for joint depth/width NTK training and recent results. Opened the actual arXiv pages:

- Boris Hanin, Mihai Nica, *Finite Depth and Width Corrections to the Neural Tangent Kernel*, arXiv:1909.05989, https://arxiv.org/abs/1909.05989. Their abstract already includes the mean first-SGD-update result; initialization fluctuations are not their only training-related result.
- Jiaoyang Huang, Horng-Tzer Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, arXiv:1909.08156, https://arxiv.org/abs/1909.08156. Infinite hierarchy and controlled truncations under its conditions.
- Andrea Combette, Nelly Pustelnik, Antoine Venaille, *Correlation flow governs learning at criticality*, arXiv:2608.08350, https://arxiv.org/abs/2608.08350. Sequential width/depth limit at critical initialization, not the requested proportional training law.
- Ruijia Zhang, Soufiane Hayou, *Width and Depth Limits Commute During Training in Linear Residual Networks*, arXiv:2610.30729v2, https://arxiv.org/abs/2610.30729. Fixed GD horizons, linear residual networks, depth-muP scaling; clipped updates give L2 convergence, ordinary updates give convergence in probability. Different model from nonresidual Gaussian/ReLU T245.
- Blake Bordelon, Cengiz Pehlevan, *Deep Linear Network Training Dynamics from Random Initialization: Data, Width, Depth, and Hyperparameter Transfer*, arXiv:2502.02531, https://arxiv.org/abs/2502.02531. Infinite-depth limit uses scaled residual branches.

No whole-problem solution found in this bounded check. No SOLVED_ELSEWHERE.md is warranted. This is a bounded search, not proof of absence.

Reading all four preceding REPORT.md, LOG.md, PROOF.md and scripts before substantive calculation. The latest result retains one symmetric depth field J for the first learning-rate correction. Its main theorem will be independently rechecked before choosing the extension.

## Earlier result: independent recheck

Finished reading the four earlier sets of reports, proofs, logs and scripts. Re-derived the first Euler error directly in the original profile coordinates: if Y_dot=F(Y), then Y_k^eta=Y(k eta)+eta Z(k eta)+O(eta^2), where Z_dot=DF(Y)Z-(1/2)DF(Y)F(Y). Applying the endpoint map Phi gives p_dot=D(DPhi F)Z-(1/2)DPhi DF F. The second chain rule Df F=D^2Phi[F,F]+DPhi DF F explains the positive half-Hessian insertion in the previous endpoint equation. Summing the exact discrete balance defect gives E=-t integral [G,G^T] d tau; differentiating the general Gram identity gives precisely its forced Dirichlet problem. No sign, order, or normalization error found.

Created recheck.py to integrate the original nonlinear C,b flow and its first Euler sensitivity Z with finite differences of the original vector field. This implementation never uses J, its transport equation, the Gram boundary problem, or the proposed endpoint sensitivity forcing. Compare its differentiated endpoint and full kernel with round 5. Earlier imports disable bytecode and do not run main functions. Command:

`OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck_output.txt 2>&1`

First run stopped at an overstrict 2e-8 flow-observation comparison, after its independent sensitivity comparison passed 2e-7. Expose the actual errors before the assertions and use depth refinement to distinguish quadrature error from a mathematical error. No theorem failure inferred from that threshold.

At grid 64 the original-profile sensitivity and the round-5 correction differ by 1.854833e-7, and the flow observations differ by 6.220702e-8. Exact rational benchmark checks reproduce the two commutators and the memory slopes -1/24 and -1/48. The run passed after the flow tolerance was corrected; runtime 3.76 s, peak RSS 22.8 MB, priority 20. A grid-128 run is under way. The main result holds at this algebraic and independent numerical recheck.

## ONE extension chosen, before its calculation

Replace the evolving depth field in the first-order correction by a finite Taylor jet in depth, and prove a uniform truncation error on fixed training intervals. The memory equation is pointwise and analytic in depth; differentiating it at depth zero should give a triangular finite system for its first m+1 coefficients, without feedback from discarded coefficients. This is a controlled finite-dimensional approximation, not a claim of an exact finite-moment closure. The target is an error O(eta^2+eta rho^(-m)) for every fixed rho>1, hence m=O(log(1/eta)) suffices to retain the previous full first-order accuracy. This advances the compression question while making the approximation and its cost explicit. All scope restrictions of the structured linear model and the iterated size/step limits remain in force.

## Proof and implementation saved

Grid 128 in the independent recheck gives sensitivity error 4.636415e-8 and flow-observation error 1.555176e-8, each approximately one quarter of grid 64. It passes; runtime 7.72 s, peak RSS 23.9 MB, priority 20. Complete results are recheck_output.txt, recheck_refined_output.txt, and recheck_data.json (the refined run).

Saved PROOF.md. Expanding R(z) gives r_a=-t(-1)^(a-1) ad_K^(a-1)(vg^T)/a!, r_0=0. The source coefficients follow from exponential powers and a matrix Lyapunov recurrence. The resulting j_q equations are exactly triangular: j_q_dot uses only j_0,...,j_(q-1) and endpoint-dependent forcing. Every finite truncation therefore computes the retained Taylor coefficients exactly. Complex-depth bounds prove that J is entire and give a uniform Cauchy tail M_rho rho^(-m)/(rho-1). A Green-function comparison bounds the forced-Gram inverse by (t/8)exp(2 k_*) in Frobenius norm. Propagating this error through the sensitivity equation proves full-state error O(eta^2+eta rho^(-m)). A matrix-exponential construction shows that even the instantaneous polynomial-source boundary problem uses finite matrices.

Created verify.py. It checks the coefficient identities by independent exact rational multiplication of exponential series, compares finite jets to the previous field evolution and an independent spectral evaluation of R, checks prefix independence across truncation orders, and compares the m=6 correction to the original nonlinear discrete profile. The script uses no arrays larger than a few hundred small matrices. Command:

`OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1`

## First verification output

Exact rational coefficient checks passed through degree 8, using direct double/triple multiplication of exponential series as a second derivation of the commutator and Lyapunov recurrences. Repeated scalar K with nonparallel v,g retains a nonzero source; all retained RHS prefixes agree exactly across truncations. The wrong commutator sign gives error 1.085185, so that check distinguishes the sign. Mandatory kernel slopes again equal -1/24 and -1/48 exactly.

For the stronger test (t,S,T)=(2,1.3,1.2), maximum depth-field errors at degrees 0,1,2,4,6,8,12 were respectively 3.21472e-2, 1.51562e-2, 4.58081e-3, 2.65194e-4, 7.12255e-5, 4.20195e-6, 2.46080e-9. Maximum full first-correction errors were 2.39709e-2, 4.77669e-3, 9.21364e-4, 1.95190e-5, 3.67404e-6, 1.53265e-7, 8.09286e-11. Every retained Taylor coefficient agrees bit for bit across the integrated truncations. Independent spectral integration of R gives the same field errors, within the reference evaluation floor. The rest of the run is testing refinement, original discrete trajectories, and edge cases.

Compute state before this run's continuation: warn / owner_away_open due to CPU saturation, no distress. The task uses one process at priority 20 and no numerical libraries or worker pool.

## Verification completed; attempts to break the result

The verification command exited 0. All checks passed. Runtime 72.18 s, peak RSS 21,921,792 bytes, one thread, priority 20. Independent spectral R evaluation differs from the earlier field at the sampled depths by at most 7.07203e-11. Refining the degree-8 reconstruction's depth evaluation from 64 to 128 and training integrator from .002 to .001 changes its full correction by 6.41651e-10. This is larger than the degree-12 same-grid correction discrepancy of 8.10e-11; the latter is a comparison between implementations, not a certified absolute integration error.

For degree 6 at time .4, the discrepancies in the full first-order coefficient from the field implementation are 4.36e-17, 1.20e-11, 2.72e-8 for (t,S)=(.5,.7),(1,1),(2,1.3). Full-state errors against the original nonlinear discrete profile at eta=.04,.02,.01,.005 are:

- t=.5: 2.29551e-5, 5.65749e-6, 1.40445e-6, 3.49887e-7.
- t=1: 1.04714e-4, 2.57060e-5, 6.36945e-6, 1.58560e-6.
- t=2: 9.80879e-4, 2.39059e-4, 5.89591e-5, 1.45736e-5.

Halving eta reduces these errors by approximately four. Zero residuals, zero inputs, scalar commuting trajectories, repeated eigenvalues with a nonzero source, and the attained inverse-Dirichlet norm 1/8 all passed. Degree 6 is not an exact closure: at time 1.2 in the strong test its memory-field error is 7.12e-5. Only the theorem's growing m rule guarantees asymptotic O(eta^2).

Re-derived the source coefficient formula directly as the triple exponential product, checked the alternating conjugation sign independently, and checked the 1/8 Green bound both by scalar maximum principle and the exact constant-source polynomial solution. The dimension count uses symmetric matrices; the Python implementation stores four entries per 2 by 2 matrix for convenience. No claim that a global analytic bound is numerically sharp is made: its constants can be extremely large.

Added audit.py for one additional load-bearing check: freeze K=0, v=e1, g=e1+e2 in the linear memory equation. Its 11 component solves J_dot=-2zJ-1, so its exact Taylor coefficients are -tau^(q+1)(-2)^q/(q+1)!, nonzero at every order. This independently checks the factorials and the Cauchy tail bound and prevents mistaking the triangular truncation for exact termination. These prescribed coefficients are a manufactured equation, not an asserted training endpoint path. The audit also recomputes all error ratios from saved data. Command:

`OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1`

## Final audit and report

The manufactured audit passed. At tau=.7 its exact scalar field errors for degrees 0,2,4,8,12,16 were .3232985, .0619651, .00434115, 3.53168e-6, 5.82639e-10, 3.10308e-14, all below the Cauchy estimates. Its exact nonzero coefficient formula checks every order algebraically; the script checks through order 16. Recomputed discrete-error ratios lie between 4.01400098 and 4.10307493, and the independent recheck's grid-refinement ratio is 4.00057596. Runtime .076 s, peak RSS 21.7 MB, priority 20 on the first audit.

Saved REPORT.md with verdict PARTIAL. It distinguishes the proved finite approximation from exact fixed-dimensional closure, records the iterated limit order and S-dependent constants, and identifies a certified practical tail bound as the next step. Added the manufactured equation and its scope qualification to PROOF.md. No literature novelty is claimed for analytic Taylor approximations.

Reran only the lightweight audit after the report/proof additions. Exit code 0, Audit passed. It checked the exact report first line, local report links, balanced display delimiters, absence of control characters, successful saved verification outputs, manufactured formulas, and independently recomputed numerical ratios. No mathematical code changed after the successful main verification, so that longer run was not repeated. The explicit 1/8 boundary-inverse factor, factorials, alternating commutator sign, symmetric-state dimension count, and numerical ratios were all checked a second way.

All writes stayed in this folder. No subagents, git, external messages, GPU, torch, MLX, or outside-folder state mutations were used. Earlier modules were imported read-only with bytecode disabled. Every computation ran under OMP_NUM_THREADS=1 and nice -n 15, at verified inherited priority 20, well below the memory/time limits.

Task completed: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 11:27 Asia/Tbilisi (session receipt, minute precision). The original Gaussian/ReLU problem remains unresolved.
