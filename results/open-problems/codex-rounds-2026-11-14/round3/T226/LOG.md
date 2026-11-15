# T226 continuation log

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta”. Session start: 15 November 2026, approximately 03:34 Asia/Tbilisi (local shell clock). Only this folder may be written; the earlier folder is read-only.

## Orientation and bounded literature check

Read the earlier REPORT.md, PROOF.md, LOG.md and all of verify.py. Read startup MEMORY.md and BRAIN_INDEX.md, and the compute governor state. Governor: warn, owner_away_open, CPU saturated; all checks here will be small, single-thread standard-library programs under nice 15. No subagents, git or external writes. The task-specific instruction to write only here overrides the standing mesh/checklist/brain writes; no such commands are run.

Commands: `pwd`; targeted file listings; `cat ~/.claude/compute/compute_state.json`; `cat ~/codex_op_1114/briefs/T226/{PROOF,LOG,REPORT}.md`; `sed -n '1,220p' .../verify.py` and `sed -n '220,300p' .../verify.py`; read startup index at `~/.claude/projects/-Users-user/memory/MEMORY.md`. The initial broad file listing was unnecessarily large and was truncated; subsequent reads were targeted.

Web search began within the orientation and is capped at five minutes. Queries: `edge stability gradient descent random initialization deep linear network 2026 convergence sharpness`; `"edge of stability" "random initialization" 2025 2026 theorem`; `"Gradient Descent with Large Step Size Restores Symmetry" deep linear 2026`; `"edge of stability" "random" "2026" convergence linear networks`.

Opened Jaerin Lee and Kyoung Mu Lee, *A Journey to the Edge of Stability*, arXiv:2609.32290 (abstract and HTML); Peter Zaika and Zakhar Shumaylov, *Non-Euclidean Gradient Descent Has Many Edges of Stability*, arXiv:2610.15223 (abstract); Elon Litman, *The Origin of Edge of Stability*, arXiv:2604.20446v1 (HTML); and the proceedings entry and HTML for Hee-Sung Kim and Sungyoon Lee, *Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway*, arXiv:2606.05219. The Lee paper concerns empirical optimizer/learning-rate sweeps. The Zaika–Shumaylov paper concerns non-Euclidean dynamics for positive-definite quadratics. Neither abstract claims the required network/random-basin result. Kim–Lee scope is being checked in the full text. No solution found in this bounded search; no exhaustive openness claim.

## Independent audit of the earlier result, before the extension

Re-derived the deterministic bootstrap without relying on its numerical script. If earlier descent holds, the exact cancellation in B=WW^T-aa^T gives ||B_t||_* <= S0+2 eta L0. Since ||r0||<=R/2, this is <=R+eta R^2/4. Solving q^2-Dq-||v||^2<=0 directly gives q<=(D+sqrt(D^2+4||v||^2))/2<=D+||v||, hence S_t<=3D+2||v||<6R. The proposed step segment lies in S<8R, its Hessian norm is <13R, and 13 eta R<=13/32<1 closes descent without circularity. At iterates ||H||<=9R+||b||<10R. All signs and the treatment of indefinite B hold.

Independently re-derived the tail from the density rather than its moment-generating function: on S>T, exp(-S/(2 sigma^2)) <= exp(-T/(4 sigma^2)) exp(-S/(4 sigma^2)); integration gives 2^(p/2) exp(-T/(4 sigma^2)). With T=1/(64 eta), exponent 1/(256 sigma^2 eta) follows. Checked eta<=1/(128||b||) gives R cutoff S>1/(64 eta). The endpoint exclusion needs only continuity of H at a parameter limit. No convergence or saddle-avoidance hypothesis is hidden. Earlier main claim holds on this audit. An independent executable check will additionally verify exact recurrences and conservative constants.

## Chosen extension (recorded before proving it)

Study the zero-target boundary map named in the earlier report, in the full multi-input model, not a scalar invariant slice:

A^+=A-Uv, U^+=U-Av^T, v=U^T A.

Prove convergence on the open spectral region ||A0||^2+||U0||_op^2<2, with full column rank of [A0 U0]. This allows initial total squared norm much larger than the previous 1/32 cutoff. The proposed mechanism: both q=||A||^2 and C=U^T U decrease (scalar and Loewner order); their exact recurrences dissipate ||v||^2. The determinant of the full Gram matrix evolves by det G^+=det G (1-||v||^2)^2. Summable ||v||^2 and a uniform gap below 1 should preserve positive determinant, supply a lower singular-value bound, and make residual decay geometric. This would give a fixed positive-probability basin at variance tau^2/eta whose endpoints stay a fixed relative distance below 2/eta. The full boundary law remains unclassified. Need audit the determinant argument, residual contraction, and rank assumptions before accepting.

## Literature check closed (within five-minute budget)

Kim–Lee full-text Sections 3.2–3.3 impose target-aligned singular-vector-stationary structure and depth-balanced initialization; Appendix E.7 explicitly limits the dynamics analysis to a local regime. This is useful partial work, not the Gaussian full-parameter basin theorem requested here. No SOLVED_ELSEWHERE.md. Literature work stops here.

## Extension derivation and planned nonzero-target corollary

Exact identities for q=||A||^2, C=U^TU, h=||v||^2 are q^+=q-2h+v^TCv and C^+=C+(q-2)vv^T. Thus q0+||C0||<2 makes q and C nonincreasing and gives sum h <= q0/(2-||C0||). Also h<=q0||C0||<=s0^2/4<1. With Z=[A U] and K=[[0,v^T],[v,0]], Z^+=Z(I-K); hence det(Z^{+T}Z^+)=det(Z^TZ)(1-h)^2. The inequality log(1-h)>=-h/(1-rho), rho=q0||C0||<1, gives a strictly positive determinant lower bound. A trace upper bound then bounds the smallest Gram eigenvalue away from zero. Residual recurrence v^+=[I-C-qI+hI]v becomes a strict contraction once h is small, proving parameter convergence by summable step lengths. This removes any need to cite an analytic convergence theorem.

Same piece, nonzero-target persistence: after the zero-target trajectory approaches its subcritical full-rank minimum, use its output Gram spectral interval strictly inside (0,2) to construct a neighborhood with uniform residual contraction. The exact residual recurrence for target y is r^+=[I-C-qI+(v^Tr)I]r, r=v-y. Finite-time continuity in y and a local geometric-series bound should show that every initial point in the zero-target spectral basin still converges for all sufficiently small y=eta b. This yields a boundary-scale Gaussian endpoint-probability bound for any fixed b, rather than restricting the final conclusion to b=0. This persistence is part of the same basin theorem; no claim is made about initial points outside the spectral region.

## Proof saved

Wrote PROOF.md with the spectral basin theorem and its small-target persistence argument. For any fixed b, any full-column-rank Z0 with s0=||A0||^2+||U0||_op^2<2 converges for all sufficiently small eta under variance-scaled coordinates, and eta times endpoint sharpness is <=(2+s0)/2<2. The eta threshold depends on initialization. Reverse Fatou on the common scaled Gaussian initialization gives limsup edge-endpoint probability <=Pr(s0>=2). A chi-square Chernoff bound for m=16,d=8,tau^2=1/288 gives exp[-72(3-log 4)], approximately 3.5e-51. This constant still requires an independent numerical and algebraic audit. This is a limsup for b!=0, not a finite-eta bound.

A useful attempt to falsify the basin statement: initial top Hessian eigenvalue need not be below 2 despite s0<2, because the residual contributes an indefinite Hessian term. An explicit rational full-rank example has A=e1, U column 1=(4/5)e1+(1/10)e2 and remaining columns (1/10)e_(j+1). Then s0=33/20<2. The Hessian Rayleigh quotient in the simultaneous A_1,U_11 direction is 121/50>2. The basin theorem predicts convergence from an open neighborhood of this example. This will be checked independently; it distinguishes the new basin from a condition requiring subcritical initial Hessian sharpness.

## Independent executable verification — passed

Command (run only in this folder):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_extension.py > verification.stdout.txt 2> verification.stderr.txt
```

Exit 0; tool wall time 0.4063 seconds. Effective nice 20, peak RSS 16,744,448 bytes, standard-library scalar/list arithmetic only, no worker threads. A 60-second CPU cap and 90-second wall alarm were installed. The fixed-size data structures are far below 1 GB. Standard error: `nice: setpriority: Operation not permitted`; the process was already nice 20, and its guard verified that before arithmetic.

Results: 40 exact rational multi-input cases verify the old imbalance and total-norm laws and the new q, C, residual and full-Gram determinant recurrences. The determinant is computed independently by Gaussian elimination. The earlier bootstrap constants pass separate exact rational checks. Fifty-two finite trajectories (13 full-rank starts, each with scaled target norm 0, 0.01, 0.0001, 0.000001) converge numerically, needing at most 262 steps to residual below 1e-12. Maximum final residual norm 9.960063627182131e-13; maximum relative determinant-identity error 3.5368228105121905e-15. All endpoint bounds tested hold. These finite checks do not prove the basin or the limsup statement.

The initial-supercritical example verifies s0=33/20 and Hessian Rayleigh quotient 121/50 exactly. Two independent evaluations of the Chernoff number give 3.473051989693640e-51 and 3.473051989693646e-51: optimized log-MGF versus 4^72 exp(-216). The exponent is -116.18680599936788. Data: verification.json; complete stdout/stderr retained.

## Final attempts to break the argument

- Rank and strictness: with full rank and s0=2, A=e1, U_j=e_(j+1) is stationary with sharpness exactly 2 in scaled coordinates. The script verifies this exactly. Thus the proof must keep s0<2. With rank deficient A=U_1=x e1 and the remaining columns zero, x^+=x(1-x^2) can tend to zero with step ratio tending to one; the positive determinant and geometric-rate assertions cannot be extended to that case by the same argument.
- No assumption on Gaussian target samples, alignment or layer balance is used. Full column rank of the augmented m-by-(d+1) matrix is crucial and holds almost surely for m>=d+1. The example has all nine columns independent.
- Re-derived det G^+=det G(1-h)^2 from eigenvalues of K, and independently checked it by elimination on 40 exact rational Gram matrices. The positive determinant lower bound is valid because h<=rho<1 and sum h<infinity. The eigenvalue lower bound direction is correct: det G<=lambda_min(G) M^d.
- Residual contraction is only used after h becomes small. The proof does not incorrectly infer per-step loss contraction from s0<2. For y!=0, monotonicity of q and C is not assumed; finite-time continuity reaches a local contracting region, whose total path-length bound prevents exit.
- The local radius is chosen after the zero-target endpoint is known. All local inequalities have fixed positive margins. Entry occurs at a finite time, and continuity of the finite composition justifies a target threshold depending on the initial point. This does not justify a uniform threshold over random initializations.
- The probability argument uses the same scaled Gaussian draw for each eta and reverse Fatou along an arbitrary sequence eta_n->0. No unjustified exchange of a uniform eta threshold with probability occurs. The result is limsup only for a fixed nonzero target; an explicit finite-eta numerical probability is not claimed.
- The initial Hessian example was checked a second way by exact symmetric differences of the quartic loss along a line, eliminating the quartic coefficient. It gives the same quotient 121/50 without the Hessian formula. Added this example to PROOF.md.
- At a final nonzero-target endpoint, independently differentiated the gradient in all 144 parameter coordinates and compared the full Hessian to J^T J. Also formed JJ^T directly and compared it to U^TU+||A||^2 I. This checks the sharpness conversion including eta normalization.

Audited command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_extension.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt
```

Exit 0, tool wall time 0.4271 seconds. All 40 exact cases and 52 trajectories passed again. Complete final output is in verification.audited.stdout.txt; the JSON includes all trajectories. No mathematical check failed. The single nice warning remains; measured effective nice is 20. A late direct `find` in the already opened Kim–Lee paper verified the Appendix E.7 citation: its global entry statement is explicitly left unproved. No further literature search was conducted.

Two optional startup-memory reads used a nonexistent relative path and returned file-not-found; no memory content or mathematical inference came from those failed reads. Startup MEMORY.md and BRAIN_INDEX.md had already been read successfully. All outputs and new artifacts remain in this folder.

## Report saved

Created REPORT.md with a PARTIAL verdict. It states the new boundary-scale basin theorem, asymptotic probability bound, distinction from the earlier fixed-scale result, actual commands and outputs, limitations and next lemma. Final measured peak RSS is 17,645,568 bytes; endpoint Hessian finite-difference error 9.169687578691743e-13. No mathematical failures. Main unresolved issue is the complementary spectral region, and the nonzero-target probability result has no explicit finite-eta rate.
