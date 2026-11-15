# T226 round-5 log

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta”. Received 15 November 2026, approximately 08:46 Asia/Tbilisi (first clock query 04:46:50 UTC).

## Orientation and scope

Read the startup memory index and compute governor state. State: warn / owner_away_open, CPU saturated, ample free RAM. All numerical work will use one thread, nice >=15, bounded small standard-library arrays, and hard time limits. No subagents and no git. The specific instruction to write only in this folder supersedes the global mesh, checklist and brain commands, which would write elsewhere; those commands are not run. Earlier round folders remain read only.

Read the earlier REPORT.md, LOG.md, PROOF.md and verification scripts in the original, round-3 and round-4 folders. Broad combined tool output sometimes truncated; targeted reads cover the mathematical arguments and scripts.

## Bounded literature check (closed within five minutes)

Queries: `"edge of stability" "random initialization" convergence 2026 Gan`; `"edge of stability" deep linear critical sharpness convergence 2025 2026`; `"A Bifurcation Theory Framework for Gradient Descent" arxiv`; `"Convergence Rates for Gradient Descent on the Edge" MacDonald`.

Opened:
- Elon Litman, *The Origin of Edge of Stability*, https://arxiv.org/abs/2604.20446 and https://arxiv.org/html/2604.20446v1 . Theorems 4.1–4.3 concern weighted curvature and require unbounded accumulated squared step lengths for their asymptotic forcing conclusion; they give no random-entry or endpoint theorem. For the rectangle considered here those squared step lengths are summable. Thus the abstract's global-forcing language does not resolve this task.
- Eric Gan, *A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability*, https://arxiv.org/abs/2606.15551 and https://arxiv.org/html/2606.15551v1 . Theorem 4.4 explicitly assumes initialization in a neighborhood of a particular minimum and a learning rate matched to its sharpness. This is the local theorem already identified in the problem.
- Eric Regis and Sinho Chewi, *Rod Flow: A Continuous-Time Model for Gradient Descent at the Edge of Stability*, https://arxiv.org/abs/2602.01480 . The abstract states an ODE approximation and self-stabilization results for quartic potentials, not the requested global entry theorem.

OpenReview links for J4Dvxv7WnG and MU0JuT0A54 returned browser verification, so no theorem is attributed to their unviewed full texts. No opened source settles the question. No SOLVED_ELSEWHERE.md is justified. This bounded search is not an exhaustive claim of openness.

## Independent audit of round 4

The main result holds on independent derivation. With Z=[A U], v=U^T A, h=||v||^2, q=||A||^2, C=U^TU and H=C+qI, direct expansion gives
q'=q-2h+v^TCv, C'=C-(2-q)vv^T, v'=(I-H+hI)v.
Thus q0<2, ||C0||<2 imply monotonicity and sum h<infinity. The full Gram determinant has multiplier (1-h)^2. Retain all finitely many h>1/2 factors rather than taking logarithms of negative 1-h; excluding h=1 gives a positive determinant bound. This bounds H away from zero.

Independently rewrite the correction as w'=H'^{-1}[(I-H)v+hv]. Subtract w=H^{-1}v and add v. The remaining terms are (H'^{-1}-H^{-1})v + H'^{-1}(H'-H)v + hH'^{-1}v, of order h||v||. Therefore F=Z(I-K(H^{-1}v)) has increments O(h), and Z-F tends to zero. This proves parameter convergence without assuming a subcritical endpoint. The polynomial exceptional-set argument is valid. The exact one-step example has q0=c0=17/9, h0=25/9, q1=c1=128/81 and endpoint sharpness 256/81. A new independent script will check these identities with row-based direct updates and exact arithmetic.

## Chosen extension, before doing it

Determine the endpoint obstruction in the same full multi-input zero-target model. The round-4 report asks whether an eigenvalue of H_infinity at least 2 occurs with positive Gaussian probability. Seek a deterministic obstruction using the rank-one monotone C update and the residual Krylov subspace, and a null-set argument if necessary. Treat critical equality separately from strict instability; a generic unstable-fixed-point assertion alone does not settle equality. Do not infer an edge residence phase from an endpoint statement.

## Endpoint mechanism derived

A strict-instability stable-manifold theorem would miss equality at 2. The rank-one update supplies a direct argument covering both. Write alpha=2-q and theta=(1-q)(1-h). Then C'=C-alpha vv^T and v'=(theta I-C')v. For a top spectral cluster separated from the rest by delta>0, let P(s) be its projector for C-s alpha vv^T. Differentiating P^2=P and [C-s alpha vv^T,P]=0 gives
(d/ds)||P(s)v||^2=-2 alpha sum_{i in top,j outside} vi^2 vj^2/(lambda_i-lambda_j).
Consequently ||P(1)v|| >= exp(-alpha h/delta)||P(0)v||. This is a multiplicative estimate, not an additive perturbation bound.

If the limiting top output eigenvalue is >=2, choose the entire top limiting eigenspace as the cluster. Monotonicity supplies a fixed gap to the remaining spectrum for large time. On this cluster, |theta_t-lambda_j(C_(t+1))|>=1-h_t. Hence its residual weight at time t+1 is at least (1-h_t)exp(-2h_t/delta) times the old weight. Since sum h_t<infinity, the product stays positive. Residual convergence to zero forces the cluster weight to be exactly zero at some finite time.

To make this null under random initialization, use D(C,v)=det[v,Cv,...,C^(d-1)v]. The exact identity is
D(C',v')=det(theta I-C') D(C,v).
Indeed rank-one feedback along v does not change the determinant of its Krylov columns, and v'=(theta I-C')v. Each factor is a polynomial of the initial parameters and equals 1 at zero initialization. D(C0,v0) is a nonzero polynomial: take U_j=j e_j and A=e_(d+1)+sum_j e_j, giving distinct diagonal C_jj=j^2 and v_j=j. Thus D_t is not identically zero for any finite t. Its zero set is null. This would prove almost-sure strictly subcritical endpoints throughout the round-4 rectangle, with eventual geometric convergence. Need audit the projector differentiability, repeated top eigenvalues, and exact determinant identity before accepting.

## Proof saved and second derivation

Saved PROOF.md with the deterministic implication S_infinity>=2 => D_T=0 at a finite time, the polynomial null-set argument, almost-sure endpoint strictness and eventual geometric convergence. The small-nonzero-target conclusion is a corollary of the existing round-3 local contraction argument, now available for almost every starting point in the larger rectangle; it is written out again for completeness.

Re-derived the spectral estimate directly from the scalar b(s)=v^TP(s)v rather than eigenvector derivatives. Differentiating P^2=P removes the within-cluster blocks. Differentiating BP=PB gives cross block Pdot_ij=-alpha vi vj/(lambda_i-lambda_j). Thus bdot=-2 alpha sum vi^2 vj^2/gap >=-2 alpha h b/delta. This covers repeated internal eigenvalues and yields the stated exponent after taking square roots. Monotonicity brackets the entire downdate segment between C_t and C_(t+1), so it has the same fixed top-cluster gap eventually. No assumption of a simple limiting top eigenvalue is needed.

A case that must not be missed: supercritical endpoints need not be finite-time exact landings. An explicit full-rank spectator construction has A=e1, U1=(e1+e2)/4, U2=(6/5)e3, and small orthogonal other columns. Its first active step has q1=113/128, c_active,1=1/16, v_active,1=-1/64. The spectator stays fixed. Monotonicity gives sum_(t>=1) h_t<=8/143 and q_infinity>=14111/18304, so q_infinity+36/25>2 while residual stays nonzero at every finite step. Here D0=0 because the spectator is exactly invisible. This tests the necessity and precise content of the exceptional-set theorem.

Next: independent row-based exact audits, a closed-form 2-by-2 spectral-projector check against the general eigensolver, and bounded multi-input trajectory probes. Finite numerical stopping will not be confused with convergence when current sharpness remains >=2.

## First executable run: a diagnostic reduction was invalid

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_endpoint.py > verification.stdout.txt 2> verification.stderr.txt`.

Exit 1 at the independent reduced-2D check for a repeated top cluster. All preceding 32 exact recurrence/Krylov checks, round-4 correction checks, exact endpoint and spectator constants, and simple-spectrum projector checks passed. The diagnostic incorrectly reduced diag(3,3,1,0) to a two-dimensional matrix using only v_top and v_bottom; the bottom eigenvalues 1 and 0 differ, so v_bottom is not a bottom eigenvector and its span is not invariant. The projector lemma itself needs no such reduction. Preserve the failed output. Apply the independent 2D reduction only when both diagonal blocks are scalar; keep the distinct-bottom-spectrum case as a separate test with a direct projector derivative check.

## Audited executable run passed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_endpoint.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt`.

Exit 0. Effective nice 20, elapsed 1.590130417 seconds, peak RSS 17,661,952 bytes; CPU cap 60 seconds, wall alarm 90 seconds. Standard library only, one process/thread, fixed small lists, no numerical training library. `nice` emitted its known setpriority warning; the independently measured effective priority passed the >=15 guard before arithmetic.

Thirty-two exact rational cases across d=1,2,3,4 verified direct row-based gradients against q, C, v, Gram determinant, alternative residual filter, Krylov-column and Krylov-determinant recurrences. All 32 also independently verified both round-4 parameter-correction identities. Vandermonde nonzero witnesses through d=6 agree with independent Gaussian-elimination determinants.

Thirty-four spectral-projector cases passed, including repeated internal top eigenvalues and distinct bottom eigenvalues. Maximum Jacobi eigenvector residual 1.9984e-15; closed 2D projector formula discrepancy 6.9389e-17; independent finite-difference projector derivative discrepancy 2.8375e-12. The repeated-eigenvalue derivative at the degenerate diagonal point is checked directly, without differentiating an eigenvector basis.

The old full-rank exact landing has endpoint 256/81 by direct parameters and a full-Hessian lifted eigenvector. The new spectator constants pass exact arithmetic and an independent coordinate derivation: q_infinity>=14111/18304; sharpness lower bound 1011719/457600>2. A 200-step numerical spectator trajectory gives output sharpness 2.3223380455996305. This finite number is diagnostic; the exact lower bound is proved independently.

Forty generic finite probes (24 accepted Gaussian starts and 16 normalized dense starts) all reached residual below 1e-13 with output sharpness below 2. Thirty-three started outside the old q+c<2 basin; 14 had a loss increase and 11 had h>1. The largest update count was 2611; maximum final residual norm 9.9962069751e-14; largest final output sharpness 1.875754404225669. Gaussian acceptance took 28 draws for 24 points. The probes are finite implementation checks, not a proof of endpoint probabilities or convergence rates.

Earlier Chernoff constant independently recomputed as exp[-72(3-log4)] and 4^72 exp(-216), agreeing to rounding at 3.47305198969364e-51. No proved identity failed. The only failed assertion was the invalid auxiliary invariant-subspace reduction, retained in the first run's output.

## Final mathematical audit and report

Checked all load-bearing signs again: C_s downdates, so the cross-block projector derivative is negative; the bound is multiplicative in the existing top residual weight. The residual filter is theta I-C_next with theta=(1-q)(1-h), not the superficially similar 1-q+h. Monotonicity gives lambda_j(C_next)+q_t>=c_*+q_infinity>=2 in the entire top limiting cluster, hence lambda_j(C_next)-theta>=1-h. Taking the whole cluster handles repeated top eigenvalues; when the whole spectrum is the cluster, P=I and no artificial gap is introduced. The infinite product argument is used only in the tail h<=1/2. Exact finite zero residual and exactly inactive spectator directions are both covered by D_T=0.

The nonzero-polynomial argument uses the product identity, not an unsupported density claim for later iterates: D0 is a Vandermonde polynomial and every finite multiplier evaluates to 1 at zero initialization. All later D_T are therefore nonzero polynomials globally. No update-map invertibility is assumed. The parameter-rate proof separately excludes initial rank deficiency and h_t=1 using the earlier polynomial argument and Gram determinant product.

Rechecked the target perturbation without assuming q or C monotonicity for nonzero target: finite-time continuity reaches a fixed ball around the zero-target endpoint, the residual contracts there, and a geometric bound on total path length prevents exit. The small-target threshold and endpoint gap depend on the draw; bounded convergence gives only a limiting probability statement. No quantitative gap-distribution or uniform eta claim was introduced.

Created REPORT.md with a PARTIAL verdict: almost-sure strictly subcritical endpoints throughout the larger rectangle, including exclusion of equality, eventual geometric convergence, and the fixed-target corollary. The original network problem remains open in this work. Next step recorded: a quantitative Gaussian law near the endpoint threshold. The report lists the exact verification command, resources, failed diagnostic, sources actually opened, and all remaining limitations. Minor inline-math formatting in PROOF.md was corrected after rereading; no mathematical or script change followed the passing run.
