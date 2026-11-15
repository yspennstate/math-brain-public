# T245 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Receipt: 15 November 2026, 08:49 Asia/Tbilisi.

## Orientation

The current task's folder-only rule takes precedence over global requests for checklist, mesh, recall logging, or brain-memory writes. Read the startup memory and compute state directly; no outside-folder mutation, subagents, git, or external messages. Compute state: warn, owner_away_open, CPU saturated. Every Python command will use OMP_NUM_THREADS=1 and nice -n 15, standard library only, with small memory and run time. Earlier folders remain read-only; imports will disable bytecode.

Read the round-4 REPORT, LOG and PROOF, and began reading all preceding artifacts and scripts. Round 4 establishes balanced gradient-flow closure but gives a nonzero discrete defect. The intended extension is a first-order learning-rate correction, with its required depth information made explicit. The choice will be fixed after the independent recheck.

## Bounded literature check, 08:49–08:52

Used web search for simultaneous depth/width NTK training limits, later work, and discrete corrections to deep-linear balancedness. Opened:

- Boris Hanin, Mihai Nica, *Finite Depth and Width Corrections to the Neural Tangent Kernel*, https://arxiv.org/abs/1909.05989.
- Jiaoyang Huang, Horng-Tzer Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, https://arxiv.org/abs/1909.08156.
- William St-Arnaud, Margarida Carvalho, Golnoosh Farnadi, *Revisiting the Neural Tangent Kernel: the role of large width and depth*, https://arxiv.org/abs/2511.07272 (revised June 2026). This studies large-width activations and depth/stopping-time scaling, not a joint L/n>0 training kernel law.
- Blake Bordelon, Cengiz Pehlevan, *Deep Linear Network Training Dynamics from Random Initialization: Data, Width, Depth, and Hyperparameter Transfer*, https://arxiv.org/abs/2502.02531. Its infinite-depth construction is residual, with depth-scaled branches.

No solution of the stated joint Gaussian/ReLU problem found in this bounded check. This is not proof of absence. No SOLVED_ELSEWHERE.md is warranted. Literature check ends here, within five minutes.

## Earlier result rechecked before choosing the extension

Finished reading the REPORT.md, LOG.md, PROOF.md and verify.py in all three earlier folders, plus the first session's literature file. Independently re-derived the round-4 main bridge. For H=C+C^T and A=U^T U, U_z=tCU implies A_z=t U^T H U. Differentiating again gives

`A_zz - A_z A^-1 A_z = t U^T ((C+C^T)_z-t[C,C^T]) U`.

The vector field G=-S V^T e g^T U^T satisfies G_z=t[G,C^T], so the displayed defect is conserved in continuous training time and is initially zero. Thus (A^-1 A_z)_z=0, A(0)=I, and A(z)=A(1)^z. This independently recovers the endpoint flow and both kernel terms, with the same t and S normalization as round 4. Expanding one Euler step gives exactly D(C+eta G)=D(C)-t eta^2[G,G^T]. The prior main result holds at this recheck.

For the mandatory two-example case, U_1=I+(eta z/2)e1 e2^T and V_1=I+(eta(1-z)/2)e1 e2^T. Direct polynomial multiplication/integration gives the previous M1 and B1, and the kernel/endpoint commutator eta^3/48+eta^5/640. The second update gives C2_22=eta^2(1-eta)(1-z)/4. Exact rational checks will be included in the new verification script.

## ONE extension chosen before calculation

Derive the complete first-order small-learning-rate correction to the round-4 endpoint flow and full NTK on each fixed training interval. Retain one symmetric matrix field J(tau,z) for accumulated imbalance, but eliminate the full nonlinear profile C from the correction equations. A forced linear boundary problem for the prefix Gram correction should then express the extra kernel information. This is the first correction proposed in the previous report. It does not presume that finitely many additional matrices suffice; whether the field can be compressed further will remain a separate question. All assertions remain within the structured deep-linear model and take size first, then eta to zero.

## Proof and first independent verification

Saved PROOF.md with the first-order endpoint and kernel expansion. Let E=-t integral_0^tau [G,G^T] ds and J=U^T E U. Along the known balanced endpoint flow, its equation is J_dot=R^T J+J R-tN, with R,N explicit in P,b and spectral powers of H=P^TP/S^2. The excess Gram variation W has zero endpoint values and solves W_zz=W_z K+K W_z-K W K+tJ, K=log H. Conjugation by exp(-zK/2) reduces it to scalar Dirichlet equations with the explicit hyperbolic-sine Green function. Kernel differentiation then gives the order-eta correction at the actual discrete endpoint. The endpoint sensitivity also includes the ordered double-insertion Hessian and the usual Euler correction. Uniform O(eta^2) remainders at training nodes follow from the Banach-space Euler error expansion.

Created verify.py, with new correction equations and checks. Only low-level round-4 matrix/spectral helpers and the independent round-3 raw profile solver are imported, read-only with bytecode disabled. Earlier main functions are not run. Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
```

Exit code 0. Exact Fraction arithmetic independently reproduces M1, B1, C2_22, both earlier commutators and the exact discrete defect. The new initial correction constants are -1/24 in M22 and -1/48 in B, derived a second way by polynomial integration. The forced Gram solver converges by about 16 per grid doubling on manufactured smooth solutions, including repeated eigenvalues. Ordered Hessian insertion versus central differences of the original profile gives error 2.00e-8 at epsilon=.005.

At training time .4, eta=.04,.02,.01,.005, full-state corrected errors were:

- (t,S)=(.5,.7): 2.296e-5,5.657e-6,1.404e-6,3.499e-7.
- (t,S)=(1,1), mandatory two-example case: 1.047e-4,2.571e-5,6.369e-6,1.586e-6.
- (t,S)=(2,1.3): 9.809e-4,2.391e-4,5.896e-5,1.457e-5.

They decrease by approximately four on halving eta, versus the original flow's approximately two. The correction-equation grid/time refinements change the correction coefficients by at most 2.18e-9. Raw nonlinear profile grids 128 and 256 differ by at most 7.65e-8. These are numerical diagnostics, not proved error constants. Direct integration of the physical profile and its accumulated commutator gives J within 2.84e-9 of the new endpoint-driven J equation. Scaled discrete defect at eta=.005 differs from its leading limit by .0002756. Complete outputs are verification_output.txt and verification_data.json.

## Attempt to break the result and second verification

Re-derived the forced Gram equation directly by varying A_zz=A_z A^-1 A_z+t U^T D U, checking the inverse variation sign. Independently expanded the nilpotent one-step Gram matrix and its endpoint spectral power; their difference is eta^2 z(1-z) diag(1,-1)/8, which agrees with the memory boundary solution. Re-derived the ordered Hessian by two insertions in the depth product and checked that the larger depth is on the left. The bias-only exact Euler formula gives beta(tau)=mean(y)*tau*exp(-tau)/2, with positive sign. These checks address the load-bearing signs and factors separately from the new ODE implementation.

Added negative controls: reversing the Hessian multiplication order and deleting the transport terms from J. Reran the same command. Exit code 0, all assertions passed. Reversed insertion differs by .00363575 while the correct formula differs from direct profile differentiation by 1.99869e-8. Omitting transport gives J error .00611283 while the complete equation differs from direct physical-profile integration by 2.83620e-9. Thus these terms are numerically consequential. At eta=.005 in the two-example case the leading memory correction is M=[-6.1991e-6,.000525366,.000525366,-.0116502] and B=-.00580726. Actual-minus-balanced kernel divided by eta approaches these values; its maximum discrepancy is 4.32e-5, consistent with a first-order remainder in that quotient.

Repeated singular values, stationary data, zero inputs and scalar commuting orbits passed. Their memory is zero to below 5.1e-18, while scalar/bias trajectory corrections can remain nonzero. No numerical assertion failed. Final run: 10.2602 seconds, 28,508,160 bytes peak RSS, OMP_NUM_THREADS=1, priority 20. The nice warning reflects inherited priority 20, independently checked inside the script. All allocations are a few hundred small matrices.

Saved REPORT.md with verdict PARTIAL, formulas, limit order, verification table, failure controls, remaining scope and the finite-state compression question for the next worker. Two report-save tool calls were rejected before writing (JavaScript syntax, then a malformed patch); the corrected patch succeeded. All earlier folders have been used read-only, with bytecode generation disabled. No outside-folder writes, git, subagents, external messages or heavy computation were used.

## Final artifact audit

Command: OMP_NUM_THREADS=1 nice -n 15 python3 - with a read-only inline audit. It checked all six artifact files, first-line verdict, balanced display delimiters, absence of control characters, successful final test output, JSON resources and corrected-error ratios independently from the saved data. Output: Artifact audit passed. Consecutive corrected-error ratios were [4.05747,4.02827,4.01400] for t=.5, [4.07353,4.03583,4.01706] for t=1, and [4.10307,4.05466,4.04561] for t=2. Thus the printed fourfold improvement was independently recalculated from the recorded errors. No rerun of computation was needed after prose-only report edits.

Task completed: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 08:49 Asia/Tbilisi (session receipt). Verdict PARTIAL: the first-order correction is proved for the preceding structured model; the original Gaussian/ReLU problem remains unresolved.
