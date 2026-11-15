# T224 working log

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 11:21 Asia/Tbilisi (first captured tool clock: 07:21 UTC).

## Startup and literature check

Read startup memory, memory index, compute governor and mesh protocol. The task-specific rule forbids writes outside this folder, so no shared mesh, checklist, recall logging or brain mutation is performed. No subagents, git, or external mutations. All Python runs use one thread, nice 15 and standard-library-only small computations. Earlier folders remain read only.

Within five minutes, searched the exact source title and arXiv number with the web tool and opened https://arxiv.org/abs/2605.22010, https://arxiv.org/html/2605.22010v3, and https://arxiv.org/abs/1804.06561. Margalit Glasgow and Joan Bruna's source is still v3, revised 11 November 2026. Remark 6 treats the critical exponent 2; Section 6 still asks about slower rates or a counterexample. No later settlement was found. Song Mei, Andrea Montanari, and Phan-Minh Nguyen are the authors on the opened background arXiv page. No SOLVED_ELSEWHERE.md is warranted; this search is not a literature-priority claim.

## Independent re-check in progress

Read the preceding scalar proof and audit in full. Independently subtracting its scalar clock equations gives q'=-k(t)q-zeta with 0<=k<=B^2. The integrating factor has modulus at most one, yielding ||q(t)||_L2<=At/sqrt(m) and ||output error||_L2<=A(1+B^2 t)/sqrt(m). Loss monotonicity gives the same all-time constants 4 and 6. Thus its main theorem holds in the stated one-dimensional output-span setting. The inherited audit will also be rerun locally.

## Chosen extension (before proof)

Test and prove the proposed two-direction commuting-gradient extension, in fact for any fixed finite number of orthonormal output directions. Let psi=(psi_1,...,psi_k) and X_j=grad psi_j. If the complete X_j commute, their joint flow should satisfy partial_j Psi_s=X_j(Psi_s). Then the feature-average map has Jacobian E[Dpsi Dpsi^T], which is symmetric positive semidefinite, giving a contractive vector-clock comparison. This is the concrete missing lemma named by round 5. The goal is the same m^(-c/(c+2)) bound with vector-norm constants, with no claim about noncommuting fields or sharpness. Check whether commutation adds hidden rigidity; give a source-admissible two-input example and expose a noncommuting obstruction if possible within this same extension.

## Earlier files read and audit rerun

Read all four earlier REPORT.md, LOG.md, PROOF.md and Python audit scripts. The earlier rounds establish curvature-conditional bounds, and the latest round establishes the scalar-clock special case. All were inspected read only.

Reran the latest audit from this folder (its only write is relative to cwd):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T224/audit_scalar_clock.py
```

PASS: 500 autonomous-flow checks, 6 exact sample variances, 6,000 exact comparison intervals, 95 raw-neuron/clock cases with 401 time points, 500 rational prefactor checks, and 6 exact exponent balances. Maximum raw-neuron/clock error 4.984679335962028e-11; clock comparison violation 0. Actual nice 20, peak RSS 16,384,000 bytes, script-reported elapsed 0.403 seconds. The wrapper prints a setpriority restriction; the independently read priority satisfies the author's limit. Full output is scalar_clock_results.json. Together with the independent integrating-factor derivation, this verifies the inherited scalar theorem in its stated scope.

## Extension derived

For commuting C1 fields, the variational equation shows D Phi_i^s X_j = X_j composed with Phi_i^s. This proves commutation of the complete flows and partial_j Psi_s=X_j(Psi_s) for their joint action. Hence D_s[psi(Psi_s(z))]=Dpsi(Psi_s(z))Dpsi(Psi_s(z))^T, a symmetric PSD Gram matrix bounded by B^2. Averaging preserves both properties. The empirical vector-clock difference therefore solves q'=-K_t q-zeta_t, where K_t is the segment average of that Gram Jacobian and is symmetric PSD. Its evolution is contractive even when the matrices K_t at different times do not commute. Thus exactly the scalar finite-time bound A^2(1+B^2 t)^2/m holds, and the same all-time constants and exponent follow. Next: save the complete proof, construct a coupled two-output audit, and test the obstruction when feature-gradient fields do not commute.

## Full proof saved

PROOF.md now proves the joint-action lemma from the variational equation, the PSD feature-average Jacobian, the vector-clock representation and uniqueness, and the all-time bound with exponent c/(c+2). The stochastic comparison is re-derived using a regularized norm and the evolution matrix of a time-varying PSD system. There is no assumption that these time-varying matrices commute.

Included a source-admissible two-input arctangent example: X uniform on sqrt(2)e_1,sqrt(2)e_2, Y=pi/2, initial law uniform on the four coordinate choices 0,1/sqrt(2). In orthonormal output coordinates psi_j=atan(sqrt(2)w_j)/sqrt(2), so A=pi/2 and B=1. Scaling a_j=sqrt(2)w_j cancels both input-probability factors and gives exactly the old scalar physical-time ODE. Therefore L_t~1/(2 sqrt(t)) and the theorem applies with c=1/2. The proof re-derives this asymptotic from (a_0^4)'->4 rather than just citing the previous round.

Also derived an explicit limitation of the proposed extension. With normalized scalar inputs alpha,2alpha, alpha=sqrt(2/5), and arctan activation, the two feature gradients do not commute. At clock point (0,35/(6 sqrt(2))), the ordered-flow feature map has Jacobian [[1/50,1/25],[2/125,4/125]]. Its quadratic form in direction (1,-1) is -1/250 and its symmetric-part determinant is -9/62500. This disproves monotonicity of the ordered map after dropping commutation; it is expressly not a counterexample to T224. Next checks will recompute these fractions separately and compare with finite differences of exact autonomous flows.

## New audit, first run

Saved audit_commuting_clocks.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_commuting_clocks.py
```

PASS. Full data are in commuting_clock_results.json. Counts: 300 exact rational Gram cases in unequal dimensions, 500 joint-action/group/Jacobian cases, 6 exact vector sampling variances with correlated output coordinates, 6,000 exact time-varying PSD matrix comparison intervals, 207 raw-particle/vector-clock flow cases with 201 time points, 300 exact vector prefactor checks, and 6 exact exponent balances. A nonorthogonal mixing of two arctangent features gives nonzero Gram off-diagonal entries and coupled clock dynamics; this is not merely a check of two independent scalar clocks. The sampled initial law has correlated parameter coordinates, and every multinomial composition for widths 1,2,4,8 is included. One target makes the population clock stationary while empirical clocks move.

Maximum joint group error 9.93e-16; action derivative error 5.06e-11; Gram Jacobian error 9.52e-11; raw-neuron/clock error 3.43195545468579e-10; forcing-comparison violation 0. The time-varying matrix test includes noncommuting matrices (maximum commutator entry 49.9966), which checks that no invalid matrix integrating-factor formula is used. Maximum expected finite-time output error divided by the theorem bound is 0.01781; this loose upper bound is not a sharpness test.

The obstruction is recomputed with exact fractions as -1/250 and -9/62500. Separately differentiating its exact ordered autonomous flow gives maximum Jacobian error 5.36e-12. Three finite directional ratios are -0.0040001922, -0.0040000223, -0.0040000023, tending to -1/250. Actual nice 20, peak RSS 17,727,488 bytes, elapsed 8.71 seconds. This is a finite-time/algebra audit, not an infinite-time simulation. Next: finish an independent normalization and edge-case check, and record the exact transported-commutator defect for the next worker.

## Commutator defect and final independent checks added

The proof now records the exact defect E(s_2)=integral_0^{s_2} D Phi_2^{s_2-u} C(Phi_2^u) du, where C=DX_2 X_1-DX_1 X_2. It follows by subtracting the variational equation and the transported first field, and applies to either sign of s_2. The ordered-map Jacobian is Gram plus (Dpsi E)e_1^T. A curve with ordered clocks also has the extra physical velocity tau_1' E; controlling only the Jacobian would not make the ordered-clock curve solve the original ODE. This distinction matters for any proposed almost-commuting extension. The crude uniform commutator estimate is B K |s_2|exp(M|s_2|), which by itself does not resolve the long-time problem.

Extended the audit with a separate random stream: 300 exact raw-field commutation checks at rational parameter values in possibly unequal k,d; 60 independent transported-defect quadratures (including reversed intervals) compared with the scalar flow derivative formula; and 300 direct source-example normalization checks with both residual signs. These check the structural assumption and the input-probability/time-scaling factors independently of the Gram implementation. Rerunning the same command next.

The extended audit PASSes with all prior counts and error maxima unchanged. Maximum transported-defect quadrature error is 4.2816694634240093e-11; maximum source-rescaling error is 4.440892098500626e-16. Actual nice 20, peak RSS 18,448,384 bytes, elapsed 7.995 seconds. Final data are in commuting_clock_results.json. The only subsequent proof edit renames the bracket function to avoid confusing it with the scalar loss-envelope constant.

## Attempts to break the result

- Joint action: derived preservation of each gradient field by the other flows from two solutions of the same variational equation. Independently checked exact raw bracket cancellation and finite differences of the complete closed-form mixed action. The proof requires global commutation, not commutation at initialization only.
- Matrix comparison: derived the estimate by a regularized Euclidean norm and separately by contraction of the nonautonomous evolution matrix. Matrices at different physical times may not commute. The 6,000 exact rank-one exponential intervals exercise this case and zero damping.
- Sampling: the vector iid variance identity is evaluated only at the deterministic population clock. Exact ordered-sample enumeration includes nonuniform laws and correlated output coordinates. No temporal independence or independence after interaction is used.
- Constants: Minkowski gives A(1+B^2 t)/sqrt(m), not an extra factor sqrt(2). Independent vector squared-triangle checks give all-time coefficients 4 and 6. Exact rational balances give 2/(c+2)-1=-c/(c+2). This optimizes only the displayed estimate, not the true error.
- Normalization: derived the two-input source example directly from its population loss and again from orthonormal output coordinates. The factor sqrt(2) in a_j cancels the input probability 1/2 exactly. The old scalar asymptotic therefore has no extra time factor. Independently (a_0^4)'->4 gives sqrt(t)L_t->1/2. This example has a two-dimensional output span, although its physical coordinates separate.
- Coupled example: the flow audit uses nonorthogonal output mixing and correlated parameter coordinates; its Gram matrix is not diagonal. This generic bounded-feature audit is distinguished from the separate ridge-network example in Section 6 of the proof.
- Degeneracy: k=1 recovers the old theorem. Singular Gram matrices, k>d, zero directions, stationary population clocks and moving empirical clocks are permitted. A=0 or B=0 gives zero true output error; no division by A,B,M,C occurs. T=0 and m=1 are allowed. No initial parameter moment is needed because coupled particles start at the same point and have bounded velocities.
- Output norm: U is an isometry, so finite output coordinates retain the exact L2(P_X) norm. Loss convergence forces the target into the finite affine span. The theorem is sup_t E error^2; no E sup_t estimate or measure-Wasserstein estimate is asserted.
- Noncommutation: recomputed the negative matrix direction with exact rational outer products and independently by finite differences of the actual ordered flow. Also derived its bracket from direct field derivatives. The negative direction invalidates only ordered-map monotonicity, not the original desired bound.
- Commutator extension: an ordered-clock curve has both a Jacobian correction and an extra velocity. Equations (39)--(41) retain both. A generic bound on the commutator gives exp(M|clock|), so it does not by itself extend the theorem to the general slow-loss setting.

No gap found in the inherited scalar theorem or the stated commuting-gradient extension. Exact commutation is an additional sufficient hypothesis; neither its necessity nor a sharp exponent is proved. The unrestricted question remains open in this work.

## Final artifacts and file audit

Saved REPORT.md with the required PARTIAL first line, theorem, noncommuting obstruction, verification commands, failures and next step. Read back the full proof and report. A final standard-library Python heredoc under the same one-thread/nice wrapper verified all six required artifacts, both PASS JSON outputs, 41 consecutively numbered equations, 54 paired display environments and paired split environments. It also checked that no SOLVED_ELSEWHERE.md was created, the iid variance equation occurs once, and both audits satisfy the memory/priority limits. Final file audit PASS; nice 20 and RSS 14,352,384 bytes. The heredoc was a read-only artifact check and wrote no files.

Final deliverables: REPORT.md, PROOF.md, LOG.md, audit_commuting_clocks.py, commuting_clock_results.json, scalar_clock_results.json. All substantive writes stayed in this folder; all earlier folders remained read only. No git, subagents, external publication, shared coordination mutation or heavy computation was used. The completed piece is the finite-output-rank commuting-gradient extension and its exact commutator limitation; the original general problem is not claimed solved.
