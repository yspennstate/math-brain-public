# T267 work log

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 03:43 Asia/Tbilisi (local shell timestamp).

## Orientation and scope

All deliverable writes stay in this folder. No git, subagents, or external messages. The task's explicit restriction on writes elsewhere overrides the standing mesh/checklist/memory write procedures. Read `~/codex_op_1114/briefs/T267/{REPORT,LOG,PROOF}.md` in full. That folder contains no Python scripts. Also read the four ancestral scripts `t267_lazy.py`, `t267_rf.py`, `t267_scale.py`, `t267_scan.py` and `T267_lazy.md` under `~/math_loop/T267`, read-only.

Commands: `pwd`; `rg --files` in the current and earlier folders; `cat` of the preceding artifacts and `~/.claude/compute/compute_state.json`. Compute state: `warn`, CPU saturated, owner away. No numerical computation is planned. Startup recall was attempted using `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall 'startup identity voice T267 epoch double descent'`. It completed, but `nice` reported `setpriority: Operation not permitted`; this does not verify a lowered priority. Do not launch numerical experiments. The returned T267 memory repeats the ancestral restricted theorem, superseded by the earlier report's proof. Read the startup navigation in `brain-views/BRAIN_INDEX.md`.

## Literature check (closed within five minutes)

Web search tool queries:

- `"epoch-wise double descent" "gradient flow" neural network 2025 2026 proof`
- `"random feature" "Bodin" "Macris" concentration hypothesis gradient flow double descent`
- `"epoch-wise double descent" "2026" neural networks theorem`
- `"epoch-wise double descent" "2025" nonlinear gradient flow rigorous`

Opened: Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, https://arxiv.org/abs/2110.11805 and the NeurIPS PDF https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf . The paper retains its explicitly unproved concentration hypothesis. Opened Reinhard Heckel and Fatih Furkan Yilmaz, *Early Stopping in Deep Networks: Double Descent and How to Eliminate it*, arXiv:2007.10099, https://arxiv.org/abs/2007.10099 and https://arxiv.org/pdf/2007.10099 . Its network guarantee is an upper bound. Also opened Antoine Bodin and Nicolas Macris, *Gradient flow in the gaussian covariate model: exact solution of learning curves and multiple descent structures*, arXiv:2212.06757, https://arxiv.org/abs/2212.06757 . Its abstract does not supply a new nonlinear-network three-extremum theorem. Recent search results chiefly concern experiments or linear models. None of the inspected sources establishes that the target has been solved; this short search does not certify openness. No SOLVED_ELSEWHERE.md is justified.

## Independent recheck of earlier result

Re-derived the derivative from the scalar flow: with `k=l+c`, `B=s^2/4`, it is `2*l/k*((B-E*c)*exp(-k*t)-(E*l+B)*exp(-2*k*t))`. On changing the second rate from `k` to `2k`, the density has Jacobian `1/2`. Direct division gives `w(k/2)/w(k)=2*sqrt((b-k/2)*(k/2-a)/((b-k)*(k-a)))`, so the earlier quotient is correct. Its rational factors have derivatives `b/(2*(b-k)^2)>0` and `a/(2*(k-a)^2)>=0`. For `a=0`, the lower limit is `A/sqrt(2)<A`; it does not become an extra sign change. Multiplying the signed Laplace transform by `exp(r*t)` gives a strictly positive derivative. Initial slope independently from the flow is `-2*E*tr(T)/d`, agreeing with `-E/(2*gamma)`. The earlier theorem holds as a theorem about its stated surrogate. It has not established a ReLU-network limit.

## Choice recorded before new proof work

Chosen extension: prove the actual realized-sample test-risk limit, with two time derivatives uniformly on compact intervals, for a zero-initialized two-layer **sine** random-feature network with both sample size and Gaussian input dimension proportional, and width `m/n^2 -> infinity`. Only the output layer is trained. Then apply the earlier MP shape argument with the correct sine constants. This addresses one explicit missing step, the network-to-surrogate passage, for a genuinely nonlinear activation without the ReLU constant/radial modes. It does not prove double descent or feature learning.

Reason for this choice: the exact infinite-width sine kernel is `exp(-(r_i+r_j)/2)*sinh(x_i.x_j/d)`. Its off-diagonal remainder starts at degree three and tends to zero in Frobenius norm; its diagonal leaves a positive ridge `c=exp(-1)*(sinh(1)-1)`. Thus the full reduction can be proved using elementary moment bounds rather than assuming a kernel equivalence or a concentration hypothesis. The intended output is an analytic proof; no simulation is needed.

## Kernel reduction derived

The training-kernel approximation is `K0=q*X*X^T/d+c*I`, with `q=exp(-1)` and `c=(1-exp(-2))/2-exp(-1)>0`. The off-diagonal cubic remainder has squared Frobenius norm controlled by `sum_{i!=j}(x_i.x_j/d)^6`, whose expectation is exactly `15*n*(n-1)*d*(d+2)*(d+4)/d^6=O(1/d)`. Diagonal norm fluctuations tend to zero uniformly. The test-kernel remainder needs an **operator** estimate: its naive Frobenius estimate for the radial linear part is insufficient after multiplying by a label vector of size `sqrt(n)`. Rotational invariance gives `E[(exp(-r/2)-exp(-1/2))^2*x*x^T]=tau_d*I`, with `tau_d <= 1/(2*d)+2/d^2`. This supplies the missing extra factor. The cubic test remainder has squared Hilbert--Schmidt norm `O(n/d^3)`.

Finite-width estimates use bounded sine features: `E||Km-Kinf||_F^2 <= n^2/m` and `E||test_m-test_inf||_HS^2 <= n/m`. Thus `m/n^2 -> infinity` is a sufficient width condition. No sharper width threshold is claimed.

The positive ridge allows a strengthening of the initial choice: prove convergence uniformly for **all** `t>=0`, for risk and its first two derivatives. Kernel spectra are bounded below by `c/2` with high probability, so the semigroup estimates and tail estimates are uniform. This still does not rule out additional finite-sample extrema at times tending to infinity, where the limiting derivative tends to zero.

For the standard Gaussian sample-covariance law only, opened V. A. Marchenko and L. A. Pastur, *Distribution of eigenvalues for some sets of random matrices*, Math. USSR-Sb. 1:4 (1967), 457--483, https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=4101&wshow=paper . The stale direct PDF URL redirected to the site front page; a mirror timed out and an EPFL URL redirected. Clicking the paper page's English PDF link succeeded: https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=4101&what=fullteng (27-page PDF). This reference check supports a standard input to the new proof; it is separate from the five-minute check for a solution of T267.

## Proof saved

Wrote `PROOF.md`: the exact actual-risk formula is (8), and (9) proves convergence in probability uniformly over all training times for risk and its first two derivatives. The first layer is fixed, the output starts at zero, the activation is sine, and `m/n^2 -> infinity` is required. The earlier one-minimum argument applies after replacing the scale `1/4` by `q=exp(-1)` and the noise coefficient by `q*s^2`. Thus this explicit nonlinear random-feature network has a one-minimum limiting profile, or a monotone profile in the stated degenerate/noise ranges. It does not supply the target double-descent construction.

Checks already written into the proof: sine-kernel constants independently from Gaussian integration by parts and total feature variance; short-time first and second risk derivatives independently from the ODE; first two spectral moments independently from exact finite-dimensional Gaussian trace calculations; the cubic remainder's `5/12` coefficient independently from the sixth moment. No numerical run was launched. A readback found inline LaTeX delimiters lost in string escaping; restored them as dollar-delimited inline mathematics without changing formulas. Next step is a line-by-line adversarial proof audit, particularly the all-time assertion and the test-operator bound.

## Adversarial audit

Rechecked every dimension factor in the reduction. The training-kernel sampling error is `O_P(n/sqrt(m))`, and the test sampling map has Hilbert--Schmidt error `O_P(sqrt(n/m))`; multiplying the latter by `||y||=O_P(sqrt(n))` again requires `m/n^2 -> infinity`. No independence between the two approximation errors or the coefficient vector is assumed: the comparison uses pathwise operator inequalities. The test radial factor has size `O_P(1/d)` as an operator, while the diagonal training norm error contributes `o_P(1/sqrt(d))`, both sufficient. A naive Frobenius bound for the whole radial linear term would leave an order-one prediction error and was rejected.

The all-time bound uses an actual lower spectral gap `c/2`, obtained from `K0>=c*I` and operator convergence. It does not follow from compact-time convergence alone. Duhamel's formula bounds the filter difference uniformly by the integral of `u*exp(-c*u/2)`. The remaining concentration step is uniform on compact intervals by a finite grid and a third-derivative bound; the tail is controlled separately by `exp(-c*t)`. The Gaussian quadratic form at `t=infinity` is included, so the zero-order tail is not silently discarded.

Independently checked the sixth-moment coefficient using the dot-product moment generating function `(1-u^2/d^2)^(-d/2)`. Independently computed the radial constant exactly from the chi-square Laplace transform: `tau_d=(1+2/d)^(-d/2-1)-2*exp(-1/2)*(1+1/d)^(-d/2-1)+exp(-1)`, whose leading term is `exp(-1)/(2*d)`. Both agree with the conditional-moment and Lipschitz derivations used in the proof. Clarified `tr((X^T X)^2)` to avoid ambiguous trace notation.

Boundary checks: `gamma=1` causes no inverse singularity because `c>0`; `gamma>1` retains the unlearned zero-eigenvalue signal mass; `s^2=0`, `E=0`, and equality `q*s^2=E*c` have the claimed signs. The minimum-transfer assertion uses second derivatives as well as first derivatives. It is confined to fixed finite intervals and does not claim absence of late finite-sample extrema.

The same elementary cubic-remainder proof does not apply to uncentered ReLU: its kernel has a constant mode and a quadratic off-diagonal term, so the Frobenius remainder estimate used here would not tend to zero. The present work deliberately leaves those terms, feature learning, and the requested positive double-descent/peak-time theorem unresolved. No counterexample to the stated sine theorem was found in this audit.

## Report saved

Wrote `REPORT.md` with the partial verdict and the precise model/width/time conventions. The result is an actual nonlinear random-feature risk limit with an explicit one-minimum classification, not a solution of the original double-descent request. The report names what failed, the unproved regimes, and the next worker's ReLU test-operator task. All three deliverables are present. A final readback will check the statement, proof, inline-math formatting, and report against each other.

Final readback: `cat REPORT.md; tail -70 PROOF.md; tail -30 LOG.md` displayed the saved deliverables. The accompanying `rg` search for known formatting defects returned no matches (exit 1 is the expected no-match result). A second `cat PROOF.md` read through the entire final proof; a lightweight check in the tool orchestrator confirmed balanced display delimiters, paired inline dollar delimiters on each line, and equation tags 1 through 41 in order. No numerical computation or extra worker was used. The final scope in the theorem, report, and log agrees: very wide sine random features only; actual realized-risk limit; at most one limiting minimum; T267's double-descent construction remains unresolved.
