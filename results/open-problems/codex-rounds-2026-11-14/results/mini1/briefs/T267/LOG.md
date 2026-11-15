# T267 work log

Task received 2026-11-14, approximately 22:09 Asia/Tbilisi: "push this problem forward by one checkable piece."

## Initial orientation and literature search

All writes stay in this folder. No git, subagents, deployments, or external messages. The standing mesh/checklist/brain write procedures are omitted because this task explicitly prohibits writes elsewhere. The compute-state file reports `warn`, `owner_away_open`, with CPU saturation; no substantial computation is planned.

Read-only commands: `pwd`, `rg --files`, and `cat ~/.claude/compute/compute_state.json`. Initial files: PROMPT.md, codex.log, run.pid. A startup recall was attempted with `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall 'epoch wise double descent neural network gradient flow startup identity'`; the sandbox printed `nice: setpriority: Operation not permitted`, and recall did not finish immediately. This is an environment limitation, not evidence that priority was lowered. Avoid further numerical programs unless the required priority can be verified.

Web searches: "epoch wise double descent neural networks gradient flow exact risk random features theory 2025 2026" and "epochwise double descent two layer neural network asymptotic risk gradient flow". Strong candidate found: *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model* (NeurIPS 2021). Also inspecting Heckel--Yilmaz (2020) and Olmin--Lindsten (2024). Search snippets are leads only; papers must be opened before any claim.

Opened the NeurIPS 2021 paper by Antoine Bodin and Nicolas Macris, arXiv:2110.11805, https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf . Its introduction, pp. 2--3, explicitly says the analysis is not entirely mathematically controlled because of a concentration hypothesis. Therefore it is a close pre-existing analytical advance, not the requested high-probability theorem. Its Fig. 5 supplies epoch-wise curves, rather than a proof of three strict extrema with a peak asymptotic. The abstract and full PDF of Heckel--Yilmaz, arXiv:2007.10099, and the arXiv page/HTML of Amanda Olmin and Fredrik Lindsten, arXiv:2407.09845, were opened. The latter concerns linear networks and is outside the target.

The startup recall completed and surfaced a prior T267 memory: `t267_lazy_relu_network_single_min_isotropic_double_descent_two_scale_2026_10_30`. Reading it before selecting the new piece. No numerical run has been started. `ps` is blocked by the sandbox, so niceness cannot be checked that way.

## Choice, before proof work

Literature check ended within ten minutes of starting. Additional opened sources: Vivek Shripad Borkar, *A dynamic view of some anomalous phenomena in SGD*, arXiv:2505.01751 (arXiv page); Tomoki Kubo, Ryuken Uda, Yusuke Iida, *Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting*, arXiv:2601.08316 (arXiv page); Chi-Ning Chou, Oscar Uzdelewicz, Neng-Chun Chiu, Yao-Yuan Yang, SueYeon Chung, *Two Speeds of Learning: A Representation-Readout Decomposition of Grokking and Double Descent*, arXiv:2605.27078 (arXiv page and full HTML). None supplied the requested proportional Gaussian-network risk theorem. Heckel--Yilmaz's Theorem 2 is a risk upper bound. No SOLVED_ELSEWHERE claim is warranted by this check; absence from a short search is not proof of openness.

Read the complete previous note `~/math_loop/T267/T267_lazy.md` (read-only). Its isotropic Marchenko--Pastur surrogate conjecture remains unproved between aspect ratios about 0.03 and 17.9. Its final assertion that input anisotropy is necessary exceeds its proof and numerical evidence.

Chosen piece: prove that this explicit isotropic Marchenko--Pastur risk profile has at most one minimum for EVERY positive aspect ratio and every nonnegative implicit ridge. This closes the prior surrogate conjecture, rather than claiming a theorem for the actual nonlinear network. Reason: after weighting the MP density by l/(l+c), the rate density is proportional to sqrt((b-k)(k-a))/k. The ratio of the density dilated by two to the original density is monotone on their overlap. Thus the signed density for R'(t) has one sign change even when the two supports overlap, replacing the earlier disjoint-support restriction.

Planned audit: derive the risk derivative separately from bias/variance and from a scalar gradient-flow equation; prove the density ratio's monotonicity by differentiating its two rational factors; handle a=0, c=0, the MP atom at zero, zero noise, and zero teacher energy explicitly. No numerical experiment is needed for this analytic piece.

## Proof completed

Wrote `PROOF.md` using the file-edit tool. Main result: for the explicit scaled MP spectral profile, if E>0 and A=s^2/4-Ec<=0 the risk is strictly decreasing; if A>0 it has exactly one nondegenerate minimum for every gamma>0. Zero signal is treated separately. This closes the previous profile conjecture for all aspect ratios.

Load-bearing calculation: with rate density w(k)=(2/pi)sqrt((b-k)(k-a))/k, the negative density divided by w(k), on 2a<k<b, is
`Q(k)=(E*k/2+A)*sqrt(((b-k/2)/(b-k))*((k/2-a)/(k-a)))`.
The two rational factors have derivatives `b/(2*(b-k)^2)>0` and `a/(2*(k-a)^2)>=0`. Thus Q increases through A exactly once. The signed density h is positive then negative. Multiplying its Laplace transform F by exp(r*t), where r is the sign-change rate, gives a strictly increasing function; F(0)<0 and F is positive eventually. This proves exactly one simple zero.

The finite-sample surrogate risk was derived exactly, conditional on the design and averaged over teacher/noise. Its derivative was derived a second way directly from the scalar ODE. Both initial-slope calculations give `R'(0)=-E/(2*gamma)`. The spectral-moment check uses interval length `1/sqrt(gamma)` and the semicircle-area identity, not the first derivation.

No numerical outputs or data are asserted; no numerical script is needed for this proof. Remaining audit: verify that the MP shape is essential, rather than accidentally proving an invalid arbitrary-spectrum assertion, and reread the final scope restrictions.

## Adversarial audit completed

Checked all singular/degenerate cases: gamma=1,c=0 has w(k) proportional to k^(-1/2), integrable, and Q(0+)=A/sqrt(2)<A; a positive zero-eigenvalue atom contributes constant signal risk and no derivative; E=0 gives increasing pure-noise risk; s^2=0 gives decreasing signal risk. The sign-changing density proof covers both overlapping supports and disjoint supports with a possible gap. The minimum is nondegenerate because `(exp(r*t)*F(t))'>0` at its zero.

Independent change-of-variable check: `w(k/2)/w(k)=2*sqrt(((b-k/2)*(k/2-a))/((b-k)*(k-a)))`; its factor 2 cancels the dilation Jacobian 1/2. This catches the most consequential possible factor-of-two error.

Tried to extend the theorem to arbitrary spectra and found an exact obstruction, now in the audit section of `PROOF.md`. With spectral masses 9999/10000 at 100 and 1/10000 at 1, c=0,E=1,s^2=4, the derivative half F has signs negative, positive, negative, positive at `0`, `log(2)/10`, `log(2)/2`, `2*log(2)`. Exact checks: `9999*923=9229077>1048576`; `9999*2^(-50)<1/4`; `1/sqrt(2)<3/4`. Thus arbitrary spectra can have double descent, and the proof genuinely uses MP shape. This is an algebraic falsification test, not a numerical run and not an answer to the network problem.

Rechecked the normalization scale independently: T=X^T X/(4d), d/n=gamma, so `E[tr(T)/d]=n/(4d)`. The continuous density in (1) has first moment `(ell_plus-ell_minus)^2/4=1/(4*gamma)`, agreeing with the matrix calculation. Signal/noise averaging is explicit throughout; no high-probability result for realized samples is asserted.

`REPORT.md` records the partial verdict, missing network reduction, exact artifacts, and next step. No peak time is supplied because the proved curve has no local maximum. No further literature search or numerical computation was performed after the choice.

Final readback command: `cat REPORT.md; sed -n '1,100p' PROOF.md; tail -65 PROOF.md; tail -30 LOG.md` (exit 0). It confirmed the verdict, theorem, finite-sample model, and audit were saved. This readback caught a minor missing hypothesis in the interpretation: the test input and test noise must be centered, and a random design independent of the teacher/noise. Those hypotheses were made explicit in `PROOF.md`; the profile theorem and its proof were unchanged. Final artifacts: `PROOF.md`, `LOG.md`, `REPORT.md`.
