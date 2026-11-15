# T267 work log

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 06:30 Asia/Tbilisi.

## Orientation and literature check

All writes stay in this folder. The task's specific prohibition on outside writes overrides the standing mesh, checklist and brain-write routines. Read the startup memory index and compute-state file read-only; no recall command that might log outside this folder was run. Compute state was `warn`, `owner_away_open`, CPU saturated. No numerical program is planned. No git, subagents, external messages or publication.

Commands: `pwd`; `rg --files` on both predecessor folders and this folder; `cat` of predecessor REPORT.md, LOG.md and PROOF.md; read-only startup-memory and compute-state reads. Neither predecessor folder contains a numerical script. The ancestral scripts under `~/math_loop/T267` are also being read. An initial overly broad file listing was truncated; the subsequent scoped listing supplied the relevant inventory.

Literature check closed within five minutes (local shell time 06:31:25). Web searches: `"epoch-wise double descent" "gradient flow" neural network theorem`; `"epoch-wise" "double descent" rigorous nonlinear random features 2025 2026`. Opened:

- Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf . The introduction and Section 2.3 retain an unproved concentration hypothesis.
- Amanda Olmin and Fredrik Lindsten, *Towards Understanding Epoch-wise Double descent in Two-layer Linear Neural Networks*, arXiv:2407.09845, https://arxiv.org/abs/2407.09845 . Linear networks.
- Tomoki Kubo, Ryuken Uda and Yusuke Iida, *Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting*, arXiv:2601.08316, https://arxiv.org/abs/2601.08316 . Empirical study, as stated in its abstract.
- Vivek Shripad Borkar, *A dynamic view of some anomalous phenomena in SGD*, arXiv:2505.01751, https://arxiv.org/abs/2505.01751 . Abstract describes a plausible two-time-scale explanation. The journal page returned 403; no claim depends on its unavailable text.
- Chi-Ning Chou, Oscar Uzdelewicz, Neng-Chun Chiu, Yao-Yuan Yang and SueYeon Chung, *Two Speeds of Learning: A Representation-Readout Decomposition of Grokking and Double Descent*, arXiv:2605.27078, https://arxiv.org/abs/2605.27078 . Abstract describes a diagnostic framework, not the requested Gaussian-network theorem.

No opened source supplies the requested result. This short check does not prove openness; no SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of predecessors

Re-derived the sine kernel from `sin(u)sin(v)=(cos(u-v)-cos(u+v))/2`: `exp(-(r_i+r_j)/2)*sinh(x_i.x_j/d)`. Its degree-one energy is independently `(E[G sin G])^2=exp(-1)`, and its diagonal residual is `(1-exp(-2))/2-exp(-1)>0`. Conditional noise forcing covariance in the comparison flow is `(q*s^2/d)*T`, giving the predecessor's `q*s^2`, not `s^2`.

Independent scalar-ODE differentiation yields `R'(t)/2 = integral l/(l+c)*[(q*s^2-E*c)*exp(-(l+c)*t)-(E*l+q*s^2)*exp(-2*(l+c)*t)] dnu`. The dilation Jacobian is 1/2 and cancels the factor 2 from `w(k/2)/w(k)`. The two density-ratio factors have derivatives `b/(2*(b-k)^2)` and `a/(2*(k-a)^2)`. Thus the one-minimum proof checks out. Initial derivatives are `-2*E*q/gamma` and `4*E*q^2*(1+gamma)/gamma^2+2*E*c*q/gamma+2*q^2*s^2/gamma`, also obtained from `theta'(0)` and `theta''(0)` in the ODE.

Read the all-time reduction line by line: the positive gap c, the test-operator scale `o_P(d^(-1/2))`, the `m/n^2` condition and Gaussian quadratic-form variance `O(1/d)` are sufficient for the stated sine theorem. No contradiction found. Its all-time absolute derivative convergence still does not control late finite-sample signs.

## Choice, recorded before new proof work

Prove one missing lemma for the actual uncentered ReLU random-feature model: a test-kernel operator approximation that retains the constant/radial mode and the quadratic component. The target is a rank-one radial term plus `Xx/(4d)`, with residual operator norm `o_P(d^(-1/2))`. This is the next worker's explicit task in the previous report. It is narrower than a complete ReLU risk theorem: training-kernel and dynamical spike control remain separate.

Reason: ReLU's odd part is exactly linear; its even kernel has a constant angular component and a quadratic angular component. Removing only the constant pointwise does not make the quadratic part negligible in Hilbert--Schmidt norm after multiplication by arbitrary labels. Rotational symmetry and a fourth-trace estimate for the centered quadratic Gram matrix should give the required operator improvement. Every constant will be checked independently by Gaussian/spherical moments.

## Test-operator calculation

Read all four ancestral scripts with `cat`: `t267_lazy.py`, `t267_rf.py`, `t267_scale.py`, `t267_scan.py`. They contain empirical kernel comparisons, not a proof of the omitted radial terms. No script was run.

The quadratic estimate is simpler than anticipated: no fourth-trace estimate is needed. Write `u_i=x_i/||x_i||`, `a_i=||x_i||/sqrt(d)` and `x=sqrt(d)*a(x)*u`. The centered quadratic test functions are `a(x)*a_i*((u_i.u)^2-1/d)`. Their covariance matrix is exactly `2/[d*(d+2)] * D_a * (G Hadamard G - J/d) * D_a`, where `G_ij=u_i.u_j`. The centered Gram matrix is positive semidefinite. The Schur contraction with the correlation matrix G bounds its weighted operator norm by `||X||_op^2/d`. Consequently the quadratic test operator is `O_P(1/d)`, the needed improvement over its Hilbert--Schmidt norm `O_P(1/sqrt(d))`.

Keep the exact angular mean `mu_d=d*(E[(U_1)_+])^2`, rather than just `1/(2*pi)`. Its expansion is `1/(2*pi)+1/(4*pi*d)+O(d^(-2))`. The even arc-cosine kernel minus its constant and quadratic Taylor terms is bounded globally by `C*rho^4`, with `C=(pi-3)/(4*pi)`. After centering its angular mean, its test Hilbert--Schmidt norm is `O_P(d^(-3/2))`. Thus the full retained radial/linear test-kernel approximation has residual operator norm `O_P(1/d)`.

Useful additional consequence within the same lemma: at infinite width the residual is exactly orthogonal in Gaussian L2 to every linear function and to `a(x)`. Hence the actual risk for *any* coefficient vector b has an exact radial-plus-linear-plus-nonnegative-residual decomposition; for `||b||=O_P(sqrt(n))`, the final residual is `O_P(1/d)`. This identity does not solve the training dynamics or supply a deterministic limiting risk.

## Proof and finite-width flow consequence saved

Wrote PROOF.md with the deterministic test-operator inequality (4), exact risk decomposition (17), and an all-time actual-risk reduction for the finite-width ReLU flow (6). The linear coefficient in (6) still contains `H_t(K_m)` for the original nonlinear training kernel. This is not the missing deterministic risk limit.

The application to all times does not require the unresolved degree-two training approximation. ReLU's power series has positive coefficients; its degree-four coefficient is `1/(48*pi)`. The off-diagonal fourth-power direction Gram matrix has squared Frobenius expectation `105*n*(n-1)/[d*(d+2)*(d+4)*(d+6)]=O(d^(-2))`. That single positive term supplies a fixed lower gap for the bulk `A=K-c0*a*a^T`. Schur contraction bounds the rest of the bulk from above. Finite-width training sampling error is `O_P(n/sqrt(m))`, and the test-map sampling error is `O_P(sqrt(n/m))`. Thus the predecessor's sufficient width condition also suffices here.

The rank-one inverse identity gives `||K_m^(-1)*a||=O_P(1/sqrt(n))`, which bounds all-time radial predictions. For the stated centered Gaussian labels, their conditional variance is `O(1/n)` at every time. A grid of `O(n^3*log(n))` points up to `2*log(n)/kappa`, derivative interpolation and an exponential tail give `sup_t |a^T H_t(K_m)y|=O_P(sqrt(log(n)/n))`. Hence the retained radial risk also vanishes uniformly. The final statement is actual realized test risk with the original nonlinear training matrix retained in the linear predictor.

No numerical program was launched. These are analytic computations saved via the file-edit tool. Next: adversarial readback and independent checks of all constants, the orthogonality and the time-uniform Gaussian argument.

## Adversarial audit

Read back the full saved PROOF.md with `cat PROOF.md`. Independently re-derived the linear coefficient from `ReLU(z)=(z+abs(z))/2`; the angular coefficients from separate square-root and arcsine expansions; the degree-four remainder constant from the endpoint value; the spherical eighth moment from a beta integral; the test-sampling constant `(d+2)/(4*d)` from a radial Gaussian calculation; and the `1/sqrt(n)` inverse scale in an eigenbasis of the bulk matrix. All agree with the main derivations.

Checked the centered quadratic covariance on both diagonal pairs and orthogonal direction pairs. They give `2*(d-1)/[d^2*(d+2)]` and `-2/[d^2*(d+2)]`, fixing both the centering `J/d` and factor two. The covariance matrix is positive semidefinite despite possible negative entries: it is the Gram matrix of traceless tensors. Schur contraction was proved from diagonal coordinate matrices, not assumed as an entrywise inequality.

Tried to discard the radial term at operator level: this fails by testing `b=a/||a||`, giving norm at least `mu_d*||a||` of order `sqrt(n)`. Tried to remove it using only `||y||=O(sqrt(n))`: this also fails. Deterministic radial labels `y=a` have long-time radial coefficient tending to `1/c0`. The stated centered Gaussian label law is necessary for the small-radial-prediction argument as written. Both falsification checks are now in the proof.

Checked time uniformity separately from pointwise concentration. On the high-probability spectral events the grid has polynomial size, each variance is bounded by a fixed constant divided by n, interpolation is `O_P(n^(-2))`, and the tail is controlled by the actual fixed lower gap. No independence of grid variables is required. The Gaussian labels are conditioned only on X,W; their covariance is exactly `(E/d)*X*X^T+s^2*I`, of bounded norm. Dependence of b on all training data is harmless because the test estimate is an operator inequality.

Zero signal, zero noise, the all-zero problem, the critical aspect ratio and nontrivial null spaces of X cause no singular inverse. The inverse used is of the full ReLU kernel, whose fourth-order positive term supplies a gap. No claim about risk derivatives is made: the radial eigenvalue is of order n and may create an initial time layer. No deterministic limit or extrema follow until the degree-two training matrix and its coupling to the radial spike are controlled.

Audit found no counterexample within the hypotheses. No numerical computation, simulation output or statistical experiment is asserted.

## Final artifacts and readback

Saved REPORT.md with the required first-line partial verdict, the new ReLU result, its precise limits, commands, failed shortcuts and next step. Final review explicitly added mutual independence of teacher and training noise and centering of test noise to the model statement.

Final read-only commands: `cat REPORT.md`, `tail -60 LOG.md`, and individual `cat PROOF.md`, `cat LOG.md`, `cat REPORT.md`. All exited 0. A lightweight check in the tool orchestrator, without launching a local numerical program, found 52 matching display-math delimiter pairs in PROOF.md, no odd inline-dollar lines, and equation tags 1 through 32 in order. REPORT.md has the required verdict as its first line. The report, proof and log agree on scope: a test-risk reduction for lazy uncentered ReLU networks, original nonlinear training matrix retained, no limiting double-descent curve or peak time.

Task completed for this session: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 06:30 Asia/Tbilisi.
