VERDICT: PARTIAL sharp exp(-Theta(lambda^-2)) proximal LSI asymptotic for a realizable sine teacher with fixed Gaussian prior

For `X~N(0,1)`, activation `sin`, teacher `sin(X)`, half squared loss, and
fixed prior `N(0,I_2)`, PROOF.md proves that the proximal Gibbs law at
initialization `rho_0=pi` satisfies

\[
 \lim_{\lambda\downarrow0}\lambda^2\log\alpha_\lambda
 =\lim_{\lambda\downarrow0}\lambda^2\log\beta_\lambda
 =-M^2/2,
 \quad
 M=\max_w e^{-(1+w^2)/2}|\sinh w|.
\]

Here alpha is the best LSI constant and beta is the best Poincare constant,
both defined explicitly in the proof. The maximum occurs at the unique
positive root of `w tanh(w)=1` and its negative. Completing the square in
the unbounded output weight, followed by a bounded density comparison and
a Lipschitz shear, gives the lower estimate. A sign test gives the matching
upper estimate. The proof includes the functional-inequality ingredients.

This rules out a uniform bound `alpha>=c exp(-C/lambda)` in this allowed
example with a fixed Gaussian prior. It sharpens the caveat about vanilla
unbounded output weights: bounded activation alone does not give the usual
Arrhenius scale. A fixed quadratic penalty independent of temperature is a
different convention and is not covered by this asymptotic.

It does **not** establish an exponential risk-time lower bound. Simultaneous
sign reversal of `(a,w)` leaves `a sin(wx)` unchanged. The bottleneck
perturbations used here therefore have exactly equal predictors and risks.
Also, this proximal law is frozen at initialization; it is not asserted to
be a self-consistent stationary law. The full question remains unresolved
by this session.

The short primary-source literature check found no whole-problem solution.
LITERATURE.md lists the opened sources and their scope, including
[Mousavi-Hosseini, Wu, Erdogdu, arXiv:2408.07254v2](https://arxiv.org/html/2408.07254v2)
and
[Shang, Wakayama, Lecué, Suzuki, arXiv:2606.31429v2](https://arxiv.org/html/2606.31429v2).
The search is not exhaustive and originality of the proximal-LSI calculation
has not been established.

Verification: AUDIT.md re-derives the load-bearing constants and records
attempts to break the result. No numerical experiment or numerical value
of an LSI constant is claimed. There is no computation script or data file
because the contribution is a proof.

Commands and tools: the exact web queries and significant shell output are
in LOG.md. The mathematical result requires no execution. Files were written
with `apply_patch`. Read-only shell commands included `pwd`, `rg --files`,
`cat` of the compute governor state, and `sed` of startup memories. Later
reads were invoked with `OMP_NUM_THREADS=1 nice -n 15`; the sandbox reported
`nice: setpriority: Operation not permitted` and denied `ps`. No heavy
program was run under the unverified priority. No git, network posting,
subagent, or file mutation outside this folder was used.

Next worker: study the dynamics after quotienting out
`(a,w)~(-a,-w)`, or derive a dissipation inequality directly for prediction
risk. Any runtime lower bound must exhibit a slow mode that changes the
predictor and persists under the changing self-consistent drift. The exact
Gaussian elimination in Sections 2–3 offers a simple test case for that work.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:21 Asia/Tbilisi.
