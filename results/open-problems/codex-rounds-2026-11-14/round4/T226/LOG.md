# T226 continuation log

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta”. Session date: 15 November 2026, Asia/Tbilisi. The actual starting clock is recorded below when queried; the earlier round's 03:34 time is not this session's receipt time.

## Orientation and read-only audit

Read the two earlier REPORT.md, LOG.md, PROOF.md files and their verification scripts. Read the startup memory index at `~/.claude/projects/-Users-user/memory/MEMORY.md`, the brain navigation index, and the compute governor state. Governor reports warn / owner_away_open with saturated CPU. Checks will be tiny standard-library scalar computations, one thread, under nice 15. No subagents, git, or writes outside this directory. The specific restriction on writes supersedes the standing mesh, checklist, recall logging and brain-write instructions; those commands are not run.

Independent derivation of the round-3 claim: direct multiplication of the two simultaneous gradient updates gives q'=q-2h+v^TCv, C'=C+(q-2)vv^T, and v'=(I-C-qI+hI)v. The augmented factor update is Z'=Z(I-K), where K has off-diagonal blocks v and v^T, so det G'=det G(1-h)^2. For q0+c0<2, h<=q0*c0<1 and sum h<=q0/(2-c0), giving a positive infinite-product determinant, a uniform Gram lower bound, eventual residual contraction, and parameter convergence. The small-target persistence proof uses a finite iterate and a contracting local ball, with a point-dependent target threshold. Reverse Fatou gives precisely a limsup probability statement. These claims hold; no uniform finite-eta estimate follows. Re-derived the first round's norm bootstrap as S<=3||B||_*+2||v||, yielding 5+3/128<6 and segment Hessian bound 25/2<13. Its constants and probability exponent also hold.

## Bounded literature check

Web searches: `"edge of stability" "2026" "random initialization" convergence`; `"edge of stability" Gan "4.4" minimizing manifold`; `"edge of stability" "2025" "global" deep linear convergence`.

Opened the arXiv pages for Jaerin Lee and Kyoung Mu Lee, *A Journey to the Edge of Stability*, 2609.32290; Peter Zaika and Zakhar Shumaylov, *Non-Euclidean Gradient Descent Has Many Edges of Stability*, 2610.15223; Hee-Sung Kim and Sungyoon Lee, *Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway*, 2606.05219; and Berk Tinaz, Changzhi Xie and Mahdi Soltanolkotabi, *When Both Layers Learn: Training Dynamics of Representing Linear Models via ReLU Networks*, 2606.04476. The last abstract proves convergence from moderately small random initialization, not an edge endpoint theorem. Opened Kim–Lee's full HTML and Appendix E.7: its EoS contraction assumes sharpness bracketing and the entry problem remains outside the local analysis. Nothing opened changes the earlier verdict. This bounded search is closed; it is not an exhaustive assertion of openness. No SOLVED_ELSEWHERE.md is justified.

## Chosen extension, before the proof

Analyze the larger zero-target region q0<2 and ||C0||<2 named in round 3, allowing q0+||C0||>=2. Seek a parameter-convergence lemma using the exact Gram recurrences. Here h may equal 1 and destroy rank; away from that algebraic exceptional set, its summability still preserves a positive determinant, although the old residual contraction proof no longer applies. The main missing step is convergence when some limiting output eigenvalues are at or above 2. In parallel with the proof, test the possibility of supercritical limiting spectator directions; do not equate a limiting eigenvalue with an edge phase.

## 05:11–05:14 — convergence mechanism and attempted counterexamples

First queried local clock: 2026-11-15 05:11:01 +04; runner output started at approximately 05:09. Literature search ended before the five-minute limit. Some initial combined read outputs were truncated; targeted rereads covered the round-3 proof/log/script and the first-round proof and script. No result relies on a truncated snippet.

The missing convergence lemma has an elementary correction. Let H_t=C_t+q_t I, w_t=H_t^{-1}v_t and F_t=Z_t(I-K(w_t)). If augmented rank never collapses then the determinant product supplies H_t>=gamma I. Monotonicity gives sum h<infinity and ||H_(t+1)-H_t||<=4h_t. The residual recurrence implies w_(t+1)-w_t=-v_t+O(h_t||v_t||). Consequently

F_(t+1)-F_t = -Z_t K(v_t+w_(t+1)-w_t) + Z_t K(v_t)K(w_(t+1)),

whose norm is O(h_t). Thus F_t converges and Z_t-F_t tends to zero, proving parameter convergence without strict residual contraction. Need write and independently check every identity and the probability-zero exceptional-set argument.

Stronger-than-spectator counterexample: q0=c0=17/9, v0=5/3 has h0=25/9 and v1=(1-34/9+25/9)v0=0. Both q1 and c1 equal 128/81; endpoint sharpness is 256/81>2. Rational vectors A=(4/3,1/3), U1=(52/51,47/51) realize these Gram data with determinant det[A,U1]=8/9. Append orthogonal columns of norm 1/2 for any d>=2 and pad rows to m>=d+1. This is full augmented rank and trains both layers. It has zero probability under a continuous initialization law; it refutes a universal endpoint bound, not an almost-sure one. It is part of auditing the same enlarged-basin lemma, not a separate toy-model explanation of EoS.

## Proof saved; independent executable audit prepared

Saved PROOF.md. The theorem proves convergence in the whole rectangle except initial rank deficiency and the countable algebraic exceptional sets h_t=1. Both exceptions have probability zero under any jointly absolutely continuous initialization law. It preserves full rank at the endpoint. It asserts no rate and no endpoint upper bound 2, and treats zero target only. The proof contains an explicit error bound for parameters in terms of the residual-square tail.

Prepared verify_rectangular.py using column-based direct gradients, independently of the earlier row-based scripts. Checks use exact rational matrices for the old recurrences and the two new cancellation identities; independent determinant elimination; a direct one-step realization of the 256/81 example; full Hessian action on a lifted eigenvector at its endpoint; a genuine h=1 rank-collapse example; and 26 finite trajectories entirely outside the earlier q0+c0<2 basin. Resource guard: effective nice>=15, OMP_NUM_THREADS=1, standard library only, 60-second CPU cap and 90-second wall alarm; small fixed-size arrays far below 1 GB.

## First verification run: finite stopping expectation failed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_rectangular.py > verification.stdout.txt 2> verification.stderr.txt`.

Exit 1. All exact rational checks and earlier finite cases completed, but case 7 still had residual norm 4.137805211333266e-7 after the 5,000-step budget. The script incorrectly demanded residual <1e-11 for every finite probe. The theorem has no rate, and no such finite-time claim was proved. Preserve this output, remove the unsupported stopping expectation, and report budget-limited trajectories explicitly instead of calling them numerically converged. Keep all checks of actual proved identities and monotonicity. Standard error also contains the known nice warning; the script's effective-priority guard passed.

## 05:17 — audited run passed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_rectangular.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt`.

Exit 0. Program wall time 2.4445 seconds, effective nice 20, peak RSS 17,416,192 bytes. Thirty-two exact rational cases verified old recurrences, determinant identity, inverse correction identity (12), and parameter correction identity (15). All 26 finite starts had q0+c0>=2 while q0,c0<2. Thirteen had some h>1, and sixteen had at least one loss increase. Twenty-five reached residual <1e-13 within the cap; one remained at 4.137805211333266e-7 after 5,000 updates. Finite probes check identities and qualitative behavior, not the infinite-time theorem. Corrected the output's step counter to report actual updates rather than the loop index; final rerun follows.

The exact example verified q0=c0=17/9, h0=25/9, q1=c11=128/81 and endpoint sharpness 256/81. Independent direct parameter updates and Gram recurrences agree, and a nonzero eigenvector of the full endpoint Hessian has precisely eigenvalue 256/81. The first-round conservative constants were recomputed rationally, and the round-3 probability constant was evaluated both as exp[-72(3-log4)] and 4^72 exp(-216), agreeing to rounding.

## Attempts to break the proof

- The determinant argument does not take log(1-h) when h>1. It retains every early nonzero squared factor and takes logs only after h<=1/2. The bound fails exactly when h_t=1; a full-rank q0=c0=3/2, h0=1 example is checked and loses rank in one step. No claim is made about all rank-collapse trajectories.
- The exceptional sets are null because finite iterates are polynomial functions of the initial entries and h_t-1 evaluates to -1 at zero initialization. This uses no global invertibility of the GD map and does not assume conditional residual distributions have densities.
- Full Gram positivity gives both q>=mu and C>=mu I, hence H>=2mu I. No subcritical upper bound is used: H may approach an eigenvalue at 2 or above 2. Inequality ||v_next||<=9||v|| only uses H<4I and h<4.
- Re-expanded the corrected-frame argument from the telescoping product Z_(t+1)(I-K(w_(t+1)))-Z_t(I-K(w_t)); its linear term cancels exactly because w_(t+1)-w_t=-v_t+O(h_t||v_t||). The remainder is O(h_t), not merely O(sqrt(h_t)); this distinction is essential. Both expansions are checked with rational arithmetic.
- Recomputed the inverse bound from H_next^-1-H^-1=H_next^-1(H-H_next)H^-1. The correction error constant is 4/gamma^2+4/gamma+1/gamma. The two terms in the corrected increment are bounded respectively by 2B h and (9/gamma)h. Summable h, not unproved summable residual norms, gives convergence.
- The explicit supercritical example has no dormant high-curvature mode responsible for the largest endpoint eigenvalue: the active first output mode itself has eigenvalue 256/81. Its exact one-step landing is algebraically exceptional, so it gives no positive-probability supercritical-endpoint statement.
- No small-nonzero-target persistence is inferred near a supercritical or critical endpoint. The earlier local lemma requires its output spectrum strictly below 2; that requirement remains necessary for that argument.

## Final verification and report

Final command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_rectangular.py > verification.final.stdout.txt 2> verification.final.stderr.txt`.

Exit 0, 2.5671 seconds, effective nice 20, peak RSS 18,317,312 bytes. Same 32 exact cases and 26 finite probes passed. Actual largest update count is 5,000. One trajectory is explicitly budget-limited; all other residuals reached the stated stopping tolerance. Final machine-readable output is verification.json and complete console output is retained in verification.final.stdout.txt and verification.final.stderr.txt. No computation exceeded the one-thread, memory or runtime constraints.

Saved REPORT.md with the required PARTIAL verdict, the precise improvement over round 3, the full-rank counterexample, failed stopping expectation, actual validation outputs, literature scope and next step. The remaining endpoint-probability question is explicitly unresolved. No changes were made to the earlier folders, no git commands were used, and nothing was published or sent externally.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 15 November 2026, approximately 05:09 Asia/Tbilisi.
