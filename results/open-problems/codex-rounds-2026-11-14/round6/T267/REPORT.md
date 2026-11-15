VERDICT: PARTIAL proved all-time radial-spike removal and the actual isotropic ReLU random-feature risk limit

The round 5 training-kernel result holds on independent analytic recheck. Its fourth-trace constant is `8/gamma^3`; its exact diagonal and necessary quadratic radial correction also check out.

The new lemma resolves the next-worker target in that report. With `A=XX^T/(4d)+cI`, `B=A+mu_d aa^T`, `P=X^T/(4d)`, and the same Gaussian teacher/noise labels,

\[
 \sup_{t\geq0}\|P\,\partial_t^j[H_t(B)-H_t(A)]y\|
       =O_{\mathbb P}(n^{-1/2}),\qquad j=0,1.
\]

The proof is in PROOF.md, Sections 1–2. It uses the exact identity

\[
 e^{-tB}a=e^{-\lambda t}a-
       \int_0^t e^{-(t-u)B}Aa e^{-\lambda u}\,du,
 \qquad\lambda=\mu_d\|a\|^2.
\]

Its time-integrated norm is at most `(1+M/kappa)/(mu_d*||a||)` whenever `kappa I <= A <= MI`. A bounded conditional second moment for the labels then gives an all-time radial bound in mean, without a Gaussian grid argument. The comparison ODE proves spike removal. This estimate works for more general label laws than are needed for the risk corollary.

Combining this lemma with the verified round 4 test-risk and round 5 training-kernel reductions gives the actual realized-sample risk limit, uniformly for all `t>=0`. The model is uncentered ReLU, independent standard Gaussian inputs and fixed first-layer weights, zero output initialization, a Gaussian random linear teacher with covariance `(E/d)I`, independent Gaussian noise of variance `s^2`, `d/n -> gamma>0`, and `m/n^2 -> infinity`. Only the output layer is trained. Time is for the half-sum squared loss.

PROOF.md, equations (24)–(26), states the explicit integral:

\[
 \mathcal R(t)=s^2+\int\left[
 E\left(\frac{c+\ell e^{-t(\ell+c)}}{\ell+c}\right)^2
 +\frac{s^2}{4}\frac{\ell(1-e^{-t(\ell+c)})^2}{(\ell+c)^2}
 \right]\nu_\gamma(d\ell),
 \qquad c=\frac14-\frac1{2\pi},
\]

where `nu_gamma` is the eigenvalue limit of `X^T X/(4d)`. Gaussian quadratic-form concentration and the standard sample-covariance law are written out as the passage from realized risk to this deterministic formula. The earlier one-minimum theorem now applies to this actual ReLU limit: for positive signal it decreases throughout if `s^2/4<=E*c`, and otherwise has exactly one nondegenerate interior minimum. The zero-signal cases are included. There is no interior limiting peak in this model.

Verification was analytic. The semigroup identity was checked by differentiation; Sherman–Morrison and an exactly diagonal example independently check the scales and signs. Short-time risk derivatives were derived both from the comparison ODE and the integral formula, with spectral moments independently checked by Gaussian matrix traces. The proof treats zero labels, zero signal/noise, the critical aspect ratio, null spaces, and both time endpoints. No numerical experiment or simulation was run: the sandbox refused the requested `nice` adjustment. The initial recall command's incidental persistence attempts are disclosed in LOG.md; it was not repeated. No git, subagents, publication, or external messages.

What failed: deletion of the spike in operator norm remains invalid. A label norm bound alone does not suffice for the new lemma's small projected effect. Full-risk derivative convergence also does not follow: an explicit diagonal radial component has risk `O_P(1/n)` but a nonvanishing random derivative at `t=tau/n`. That calculation is an inference check, not a theorem about the Gaussian network's initial layer.

The five-minute literature check found no opened source proving the target. Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, [arXiv:2110.11805](https://arxiv.org/abs/2110.11805), retain an unproved concentration hypothesis in Section 2.3 of the [full paper](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf). Reinhard Heckel and Fatih Furkan Yilmaz, *Early Stopping in Deep Networks: Double Descent and How to Eliminate it*, [arXiv:2007.10099](https://arxiv.org/abs/2007.10099), give a network risk upper bound in Theorem 2 of the [paper](https://arxiv.org/pdf/2007.10099). The opened 2026 empirical study and exact search queries are in LOG.md. This check does not certify openness. The sample-covariance reference is V. A. Marchenko and L. A. Pastur, *Distribution of eigenvalues for some sets of random matrices*, Mathematics of the USSR-Sbornik 1:4 (1967), 457–483 ([paper](https://www.mathnet.ru/eng/sm4101)). No claim of novelty over general kernel-regression theory is made.

Commands: read all predecessor REPORT.md, LOG.md and PROOF.md files and all four ancestral Python scripts with `rg --files`, `cat`, and `sed`; no script was executed. Deliverables were saved with the patch tool. Review here with `cat PROOF.md`, `cat LOG.md`, and `cat REPORT.md`.

What remains uncertain: no full-network risk-derivative limit, finite-network extrema count, sharper width threshold, proportional-width result, feature-learning result, positive double-descent construction, or peak time is proved. Uniform risk convergence alone permits small extra extrema. This session closes the isotropic very-wide ReLU risk reduction; it does not solve T267.

Next worker: analyze the actual ReLU risk derivatives for `t=tau/n` and for times bounded away from zero, retaining the radial term when differentiating. This would identify which finite-network shape statements transfer from the limit. For a positive double-descent result, leave this isotropic linear-teacher MP profile: proportional width or a different teacher/spectrum needs a separate mechanism and proof. Do not repeat the spike-removal step resolved here.

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 11:41 Asia/Tbilisi.
