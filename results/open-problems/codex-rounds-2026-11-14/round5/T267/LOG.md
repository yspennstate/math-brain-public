# T267 work log

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 09:03 Asia/Tbilisi. Tool clock during orientation: 2026-11-15 05:04:37 UTC, hence 09:04:37 Asia/Tbilisi. The compute-state timestamp was already local and must not be shifted a second time.

## Scope and orientation

All writes stay in this folder. No git, subagents, external messages, or numerical experiments. The task's explicit prohibition on writes elsewhere overrides the standing mesh/checklist/brain write procedures. Read the startup memory and compute state read-only. Compute state was `ok`, `owner_away_open`; CPU was busy. Every shell command was launched through `nice -n 15 env OMP_NUM_THREADS=1` after initial file discovery. The sandbox reports `nice: setpriority: Operation not permitted`, so no lowered priority is verified and no numerical program will be run. Read-only text commands still complete.

Read the three predecessor folders' REPORT.md, LOG.md and PROOF.md. They contain no Python scripts. Reading the four ancestral scripts under `~/math_loop/T267` is also required and will be completed before the new proof. Their notes are not accepted as proved kernel approximations.

Read commands: `pwd`; `rg --files` in the three predecessor folders and ancestral T267 folder; `cat` of the predecessor artifacts, `~/.claude/brain_startup.md`, `~/.claude/compute/compute_state.json`, and `~/math_loop/T267/T267_lazy.md`. Large outputs are being reread in smaller pieces to avoid truncation.

## Literature check (closed within five minutes)

Web search queries:

- `"epoch-wise double descent" neural networks rigorous gradient flow 2025 2026`
- `"random feature" "epoch" "double descent" rigorous risk gradient flow`

Opened Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, [arXiv](https://arxiv.org/abs/2110.11805) and [NeurIPS full paper](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf). The PDF still explicitly leaves the concentration hypothesis in Section 2.3 unproved (printed page 3). Opened Chi-Ning Chou, Oscar Uzdelewicz, Neng-Chun Chiu, Yao-Yuan Yang and SueYeon Chung, *Two Speeds of Learning: A Representation-Readout Decomposition of Grokking and Double Descent*, arXiv:2605.27078, [arXiv](https://arxiv.org/abs/2605.27078). Its abstract concerns a representation/readout analysis and experimental diagnostics, and does not assert the requested Gaussian-network risk/extrema theorem. An OpenReview candidate (`https://openreview.net/pdf?id=O2cW5Q3bH_M`) returned a browser-verification page and cannot be used as evidence. No inspected source establishes the requested theorem; this short check does not certify openness. No SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of the round 4 result

The linear ReLU test coefficient follows independently from `ReLU(z)=(z+|z|)/2`: odd/even cross terms vanish and the odd part has covariance one quarter of the preactivation covariance. For the quadratic component use `Q(u)=u*u^T-I/d`, with inner product `<Q(u),Q(v)>=(u.v)^2-1/d`. Its covariance on traceless symmetric matrices is exactly multiplication by `lambda=2/[d(d+2)]`. This gives the predecessor's test covariance `lambda*D_a*(G circ G-J/d)*D_a` independently of the componentwise calculation. Schur contraction bounds the latter centered Gram by `||XX^T/d||`, recovering test-operator error `O_P(1/d)`.

The degree-four training term has squared off-diagonal Frobenius norm with expectation `105*n*(n-1)/[d(d+2)(d+4)(d+6)]`, which tends to zero. Positivity of its coefficient supplies a fixed bulk gap. Conditional on X,W, the labels are centered Gaussian with covariance `(E/d)*XX^T+s^2*I`, bounded in operator norm in probability. The rank-one inverse identity gives `||K_m^{-1} a||=O_P(n^{-1/2})`, hence radial prediction variance `O_P(1/n)` at every time. A polynomial grid and the fixed spectral gap give the stated uniform radial disappearance. These rederivations support the main round 4 claim; no error found. This does not replace its training kernel by a linear matrix.

## Choice, recorded before the new proof

Chosen extension: prove the operator approximation of the centered quadratic training Gram, preserving its diagonal and the radial rank-one term, then deduce the corresponding full ReLU training-kernel approximation. This is precisely the next missing lemma named by round 4. The extension will remain a training-operator theorem; no unproved flow reduction, deterministic risk formula, risk-derivative limit, or positive double-descent theorem will be claimed.

Proposed elementary route: for independent uniform directions, set B_ii=0 and B_ij=(u_i.u_j)^2-1/d. Expand E tr(B^4) by the number of distinct vertices of a closed four-step walk. With traceless features Q(u), covariance lambda times the identity and deterministic squared norm r=1-1/d, the contributions with four, three and two distinct vertices are respectively `(n)_4*D*lambda^4`, `2*(n)_3*(lambda*r)^2` and `(n)_2*E[(U_1^2-1/d)^4]`, where `D=(d-1)(d+2)/2`. Their total is O(1/d) for n proportional to d, giving ||B||=O_P(d^(-1/4)). This avoids the nonvanishing Frobenius norm of B. The higher-degree training remainder is handled off the diagonal by eighth moments, retaining its diagonal exactly.

Audit plan: enumerate the walks independently; derive the fourth centered moment both by spherical moments and a beta-distribution identity; check n=2, n=3 and d=2; check the diagonal of the resulting ReLU approximation; compare retaining mu_d versus c0+c2/d in its radial coefficient. Inspect what fails if the quadratic rank-one mean or its diagonal is discarded.

## Predecessor reading completed

Read the round 4 log individually, both later reports together, and all four ancestral Python scripts together using read-only `cat` under the stated thread environment. No script was executed. The scripts measure finite-test-set risks on time grids; their extrema routine sometimes counts a descending endpoint as a minimum. Those measurements are not used as a theorem or as verification of this proof. Rereading the round 3 final audit and the initial session's proof is still needed where earlier combined output was truncated.

## Fourth-trace calculation and training-kernel consequence

The three closed-walk terms above are correct. The exact fourth central moment is

`kappa4 = 105/[d(d+2)(d+4)(d+6)] - 60/[d^2(d+2)(d+4)] + 18/[d^3(d+2)] - 3/d^4`

`= 12*(d-1)*(5*d^2-13*d+12)/[d^4*(d+2)*(d+4)*(d+6)]`.

Thus `E tr(B^4)=O(1/d)` when n is proportional to d. The full-kernel consequence retains exact radial coefficient mu_d and exact diagonal: with L=XX^T/(4d),

`K_infinity = L + mu_d*a*a^T + (1/4-mu_d)*D_a^2 + O_P(d^(-1/4))`

in operator norm. Replacing the displayed diagonal by cI, c=1/4-1/(2*pi), is also valid with o_P(1) error (indeed the norm-concentration error is smaller than d^(-1/4)). The finite-width training error remains `O_P(n/sqrt(m))` under the previous hypotheses. This is a training-kernel statement only. PROOF.md will give all steps and independent checks.

## Proof saved and consequences checked

Saved PROOF.md. Equation (3) is the exact fourth-trace identity; (6)--(8) give the infinite- and finite-width training-kernel approximations. Equation (26) combines this one new lemma with the independently checked round 4 theorem to replace the nonlinear K_m inside the all-time realized-risk reduction by `K_* = XX^T/(4d)+mu_d*a*a^T+c*I`. This corollary retains the spike and does not identify a deterministic risk curve. Duhamel's H_t perturbation bound requires only a fixed lower spectral gap, not an upper spectral bound, so the order-n spike does not obstruct this particular replacement.

Completed the remaining readback of the predecessor documents, including the full round 3 log, its final proof audit, and the initial proof's final pages. Commands: read-only `cat LOG.md`, `tail -95 PROOF.md`, `sed -n '65,260p' PROOF.md`, and `tail -25 PROOF.md` on the respective predecessor paths, all through `nice -n 15 env OMP_NUM_THREADS=1`. No predecessor file was edited.

## Independent and adversarial audit

Re-enumerated E tr(B^4) through `sum_ik (B^2_ik)^2` instead of closed walks. Diagonal entries give `(n)_2*kappa4+(n)_3*v^2`; off-diagonal entries give `(n)_3*v^2+(n)_4*D*lambda^4`. This confirms the factor 2 and all falling-factorial counts. Direct n=2 gives `2*kappa4`; n=3 gives `6*kappa4+12*v^2`. A scalar variance calculation independently gives `v=3/[d(d+2)]-1/d^2`, agreeing with the traceless-matrix covariance calculation. The leading third-vertex term is `2*n^3*(2/d^2)^2`, hence the exact limiting constant `8/gamma^3` after multiplication by d.

Derived the fourth centered spherical moment a second way using integration by parts for `Z=U_1^2 ~ Beta(1/2,(d-1)/2)`. Its centered-moment recurrence gives the same rational expression for kappa4, with numerator `12*(d-1)*(5*d^2-13*d+12)`. At d=2, direct angular integration gives `3/128`, agreeing with the formula. Raw beta moments independently reproduce the eighth-moment constant 105. No numerical program was used for these checks.

Checked the ReLU coefficients separately from the covariance formula: squared feature mean gives c0, odd/even splitting gives 1/4, separate square-root/arcsine expansions give c2, and total feature variance gives c. The comparison matrix in (6) has diagonal exactly a_i^2/2, the raw ReLU second moment. The (25) bound at infinite time also agrees with the inverse resolvent identity.

Tried the insufficient Frobenius shortcut: `||B||_F^2` actually converges in probability to `2/gamma^2`; its variance is `2*(n)_2*(kappa4-v^2)=O(d^(-2))`, since distinct unordered edge squares have zero covariance. Thus that shortcut cannot close the training-operator gap. The fourth trace avoids it.

Tried removing the quadratic correction from the radial coefficient. This fails: `||(mu_d-c0)*a*a^T|| -> c2/gamma = 1/(4*pi*gamma)`, not zero. The new theorem and reverse triangle inequality show the simpler matrix `L+c0*a*a^T+cI` has exactly this nonzero limiting operator error. Keeping only `c0+c2/d` in place of the exact mu_d is sufficient, with O_P(1/d) error. Replacing a by the all-ones vector is not justified by this proof.

The first attempted patch adding final audit paragraphs failed because it also included a nonexistent LOG.md context. No partial changes were applied; a follow-up `rg` confirmed the paragraphs were absent, and the corrected patch added them to PROOF.md. No mathematical assertion changed in this correction.

Remaining limits: the operator rate d^(-1/4) is sufficient and not claimed sharp. The width threshold m/n^2 -> infinity is sufficient. The present work does not control the change in realized risk when the retained spike is deleted, nor risk derivatives in the initial time layer, proportional width, feature learning, double descent, or a peak time. No counterexample to the stated new lemma was found.

## Final report and readback

Saved REPORT.md with the required first-line partial verdict, the exact new result, independent checks, failed shortcuts, limits, commands, and a concrete next-worker target: control the difference of H_t with and without the retained spike after applying X^T/(4d) to the stated labels. All three deliverables agree that no deterministic ReLU risk or positive double-descent theorem is proved.

Final read-only command: `nice -n 15 env OMP_NUM_THREADS=1 cat PROOF.md REPORT.md LOG.md` exited 0, again reporting that the priority adjustment is unavailable. Read through the resulting files in full. Final model review made independence of W and X and nonnegative E,s^2 explicit. A lightweight formatting check in the tool orchestrator found matching display-math delimiters, no odd inline-dollar lines and equation tags 1 through 26 in order. No local numerical process was launched for this check.

Task completed for this session: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 09:03 Asia/Tbilisi.
