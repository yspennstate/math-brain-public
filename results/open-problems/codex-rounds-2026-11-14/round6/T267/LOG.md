# T267 work log

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 11:41 Asia/Tbilisi (first shell timestamp; tool clock at 07:42:43 UTC).

## Orientation and restrictions

All deliberate file edits stay here. No git, subagents, publications, messages, mesh, checklist, or brain-memory writes: the task's explicit restriction overrides those standing write procedures. Read startup guidance and compute state. Compute state: `warn`, `owner_away_open`, CPU saturated. An initial `nice -n 15 env OMP_NUM_THREADS=1 python3 .../brain.py recall 'startup identity working mathematician epoch double descent'` printed `nice: setpriority: Operation not permitted`, then completed recall. It also reported an attempted telemetry persistence and failed detached index refresh; this recall command is therefore not a purely read-only operation and will not be repeated. No numerical program will run because lowered priority cannot be verified. Subsequent shell commands only inspect text; writes use the patch tool.

Read commands so far: `pwd`, `rg --files` in all predecessor folders, `cat` of startup guidance and compute state, `wc -l` of predecessor documents; individual and combined `cat` reads. Large combined outputs truncated, so remaining predecessor reading is being completed in smaller chunks before the new proof.

## Literature check, closed within five minutes

Queries: `"epoch-wise double descent" "gradient flow" neural network 2025 2026`; `"2110.11805" concentration hypothesis random feature gradient flow`; `"epoch-wise double descent" rigorous two layer networks risk`.

Opened Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, [arXiv:2110.11805](https://arxiv.org/abs/2110.11805) and [full NeurIPS paper](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf); Reinhard Heckel and Fatih Furkan Yilmaz, *Early Stopping in Deep Networks: Double Descent and How to Eliminate it*, [arXiv:2007.10099](https://arxiv.org/abs/2007.10099) and [full PDF](https://arxiv.org/pdf/2007.10099); Tomoki Kubo, Ryuken Uda and Yusuke Iida, *Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting*, [arXiv:2601.08316](https://arxiv.org/abs/2601.08316). The last is explicitly empirical. Inspecting the two older PDFs for the precise caveats continues as verification of already found sources, not an extended search. No opened source has supplied the requested theorem, and no SOLVED_ELSEWHERE.md is warranted. This short search does not certify openness.

## Independent recheck of round 5

Re-derived the fourth trace by expanding `sum_ik (B^2_ik)^2`. The diagonal terms give `(n)_2*kappa4+(n)_3*v^2`; off-diagonal equal middle indices give another `(n)_3*v^2`; distinct middle indices give `(n)_4*D*lambda^4`. Here `v=3/[d(d+2)]-1/d^2`, `lambda=2/[d(d+2)]`, `D=(d-1)(d+2)/2`. Thus the leading term is `2*n^3*4/d^4`, and `d E tr B^4 -> 8/gamma^3`, agreeing with round 5. The raw fourth centered moment is `105/[d(d+2)(d+4)(d+6)]-60/[d^2(d+2)(d+4)]+18/[d^3(d+2)]-3/d^4`, agreeing with its kappa4. The kernel diagonal in its exact-diagonal comparison is `a_i^2/4+mu_d*a_i^2+(1/4-mu_d)*a_i^2=a_i^2/2`; the quadratic radial correction has operator size `(1/(4*pi*d))*n -> 1/(4*pi*gamma)`. The main claim holds on this analytic recheck; no error found.

## Choice, before the new proof

Chosen single extension: prove the all-time radial-spike removal statement requested by round 5 for its linear prediction, under the same centered Gaussian teacher/noise law. The extension will include the first time derivative of this linear prediction if the same estimate permits it. It will not claim derivative convergence of the original network risk or a double-descent theorem.

Route: set `A=XX^T/(4d)+cI`, `B=A+mu_d aa^T`. The rank-one inverse identity yields `||B^{-1}a||=O_P(n^{-1/2})`. Conditional Gaussian labels have bounded covariance. Consequently `a^T H_t(B)y` has variance `O(1/n)` for every t. A polynomial mesh on a logarithmic time interval, then the spectral gap, should give a uniform `O_P(sqrt(log n/n))` bound. The comparison ODE `delta'=-A delta-mu_d a[a^T H_t(B)y]`, `delta(0)=0`, then gives the desired prediction estimate after multiplication by `X^T/(4d)`. Unlike deletion by operator norm, this uses the label law explicitly.

Audit targets: prove the mesh/tail estimates rather than assume fixed-time concentration is uniform; check t=0 and infinity; check the Sherman–Morrison denominator independently; test noncentered labels aligned with a; distinguish prediction derivatives from risk derivatives of the full network.

## Reading completed and source caveats verified

Read all four predecessor REPORT.md, LOG.md and PROOF.md files, rereading truncated combined outputs in smaller pieces (`cat`, `sed -n '1,240p'`, and remaining sections below). Read all four ancestral scripts in `~/math_loop/T267` with `cat`; none was executed. Their numerical extrema counts can include a descending grid endpoint, so they are not evidence for two interior minima. The PDFs independently confirm: Bodin–Macris explicitly retain the concentration hypothesis on printed page 3, Section 2.3; Heckel–Yilmaz Theorem 2 on printed page 10 gives risk 'at most' a displayed expression. Kubo–Uda–Iida is empirical by its opened arXiv abstract.

## A stronger route to the chosen lemma

The Gaussian mesh argument is unnecessary. For any `cI <= A <= MI`, `B=A+mu aa^T`, and `lambda=mu||a||^2`, Duhamel gives

`exp(-tB)a = exp(-lambda*t)a - integral_0^t exp(-(t-u)B) A a exp(-lambda*u) du`.

Therefore `integral_0^infinity ||exp(-tB)a|| dt <= (1+M/c)/(mu||a||)` by Tonelli and the gap c. If `E[yy^T | design] <= C I`, then

`E[sup_t |a^T H_t(B)y| | design] <= sqrt(C)*(1+M/c)/(mu||a||)`.

This proves the radial bound in mean with rate `n^(-1/2)`, without Gaussian tails or a grid. The comparison ODE gives an O(1) mean bound for `sup_t ||delta(t)||` and `sup_t ||delta'(t)||`; multiplying by `||X||/(4d)=O_P(n^(-1/2))` proves the requested statement and its first-derivative counterpart with that rate. This is the new lemma. The sharper argument was found before writing the proof, and replaces the proposed mesh route.

Its direct corollary, using rounds 4–5 and the existing Gaussian quadratic-form/spectral argument from round 3, is the actual all-time ReLU risk limit. Including this corollary makes explicit what the missing lemma now permits; it is not an additional positive double-descent claim. The first derivative of the *full* risk is not covered: a radial prediction of size n^(-1/2) can have derivative of size n^(1/2) in the initial 1/n layer.

## Proof saved

Saved PROOF.md. Equations (3)–(5) prove the deterministic conditional-moment lemma; (12) proves the round 5 target and its first-derivative version with rate `O_P(n^(-1/2))`. The semigroup identity is checked by differentiating `exp(-(t-u)B) exp(-lambda*u) a` and integrating; its sign is negative in (6). The total integral bound is `(1+M/kappa)/(mu*||a||)`. After multiplying the scalar forcing by `mu*||a||`, that denominator cancels, yielding dimension-independent mean bounds for the coefficient difference and its derivative. This avoids all fine-time grid issues.

Equation (26) gives the resulting actual realized-sample risk limit uniformly on all times, with the explicit formula in (25). This uses the two exact prior inputs, round 4 equation (6) and round 5 equation (8), rather than re-proving them. The Gaussian quadratic-form and spectral passages are written out. The sufficient width condition is still `m/n^2 -> infinity`. The limiting risk has the earlier MP classification: decreasing for positive signal and `s^2/4 <= E*c`, exactly one nondegenerate minimum for positive signal and `s^2/4 > E*c`, and the stated zero-signal cases. No interior limiting peak occurs.

Opened the original sample-covariance reference page: V. A. Marchenko and L. A. Pastur, *Distribution of eigenvalues for some sets of random matrices*, Mathematics of the USSR-Sbornik 1:4 (1967), 457–483, https://www.mathnet.ru/eng/sm4101 . The standard Gaussian sample-covariance theorem is the only random-matrix limit invoked. This reference verification is distinct from the closed five-minute search for a solution of T267.

## First adversarial audit

Endpoint check: Sherman–Morrison gives the same n^(-1/2) radial scale. The inverse difference has rank at most one and operator norm at most 1/kappa, independently giving `E||delta(infinity)||^2 <= C_y/kappa^2`. This checks the all-time coefficient bound's order without using its integral proof.

Exact diagonal check: `A=kappa I`, `a=sqrt(n)e_1` reduces all three functions to scalar exponentials. It confirms the forcing sign, delta(0)=delta'(0)=0, radial order n^(-1/2), and order-one coefficient and first-derivative differences. Replacing the bounded-moment label by y=a makes `P delta(infinity)` nonzero for `P=I/sqrt(n)`, showing why a label norm bound alone fails in the general lemma.

The same exact example shows why full-risk derivative convergence is not a corollary. The radial squared risk is O_P(1/n) uniformly, yet its derivative at t=tau/n converges in distribution to `2*mu*(1-exp(-mu*tau))*exp(-mu*tau)*chi_1^2`. This is explicitly an inference check in a diagonal comparison, not a theorem about the Gaussian network's initial layer. Also delta''(0)=-mu*a*a^T*y, so there is no second-derivative extension as written.

Risk constants checked a second way from theta'(0), theta''(0) in the comparison ODE, and exact Gaussian traces `E tr(X^T X)=nd`, `E tr((X^T X)^2)=nd(n+d+1)`. They give `R'(0)=-E/(2*gamma)` and `R''(0)=E*(1+gamma)/(4*gamma^2)+E*c/(2*gamma)+s^2/(8*gamma)`, agreeing with direct differentiation of (25). The MP noise coefficient is s^2/4. The density-ratio Jacobian is 1/2 and the derivative of `(k/2-a0)/(k-a0)` is `a0/[2*(k-a0)^2]`, confirming the reproduced one-minimum proof.

No numerical program or simulation has run. Remaining work: final readback, check the probability localization, check all boundary cases and artifact consistency, and save REPORT.md.

## Final audit and report

Read back PROOF.md in two pieces (`sed -n '1,245p' PROOF.md`, `sed -n '245,520p' PROOF.md`) and all of LOG.md. Rechecked the conditional Markov bound on fixed high-probability X events: the projected estimate has constants independent of n, a and mu; the radial rate additionally uses ||a|| asymptotic to sqrt(n) and positive limiting mu. No Gaussian concentration or exchange of time suprema with probabilities is hidden in the new lemma; Tonelli bounds an actual integrable supremum.

Checked the all-time quadratic-form and spectral steps independently: both include t=infinity, the compact-time interpolation uses a uniformly bounded derivative, and their tails decay at rate exp(-ct). At zero eigenvalue the risk integrand is E. The atom for gamma>1 is retained. Equality s^2/4=E*c gives strict decrease for E>0. If E=s^2=0, the zero flow is included without division by those quantities. The full-network derivative caveat does not weaken the zero-order all-time risk theorem.

Opened the English PDF of the original Marchenko–Pastur paper through its page link: https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=4101&what=fullteng . It states the limiting spectral theorem; the iid finite-fourth-moment example includes the Gaussian case. The paper-page author spellings are used in the references.

Saved REPORT.md with the required partial verdict, new lemma and risk corollary, independent checks, failed shortcuts, exact scope, and the next-worker derivative/positive-construction targets. Corrected a trailing LaTeX backslash in the displayed diagonal-example distributional limit; no formula changed. Final artifact/format checks follow.

Final read-only commands: `cat PROOF.md`, `cat REPORT.md`, `tail -22 LOG.md`; both tool calls exited 0. A lightweight check in the tool orchestrator found 45 matching display-math delimiter pairs and equation tags 1 through 35 in order. REPORT.md starts with the required `VERDICT: PARTIAL` line. Read back the report in full and checked its claims against the proof: the rate applies to spike removal, not to all kernel errors; the derivative claim applies to linear prediction only; the all-time deterministic risk formula uses the stated very-wide regime and prior proved nonlinear inputs. Changed the report's computational wording to 'no numerical experiment' to distinguish this from the initial brain recall, which did execute as disclosed above.

No counterexample to the new lemma or its risk corollary was found in the analytic audit. No positive double-descent or peak theorem is claimed. The three completed artifacts are REPORT.md, PROOF.md and LOG.md; no script was needed.

Task completed for this session: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 11:41 Asia/Tbilisi.
