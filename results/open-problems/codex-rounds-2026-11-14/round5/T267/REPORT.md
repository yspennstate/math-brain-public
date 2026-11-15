VERDICT: PARTIAL proved the centered quadratic training-Gram approximation and the ReLU training-kernel reduction with its radial spike retained

The round 4 ReLU test-risk reduction checks out. The new piece is the training-side lemma that report requested. For independent uniform directions, let B have zero diagonal and off-diagonal entries `(u_i.u_j)^2-1/d`. Equation (3) of PROOF.md gives the exact fourth-trace identity

\[
 \mathbb E\operatorname{tr}B^4
 =(n)_4D\lambda^4+2(n)_3(\lambda r)^2+(n)_2\kappa_4,
\]

where `D=(d-1)(d+2)/2`, `lambda=2/[d(d+2)]`, `r=1-1/d`, and the explicit fourth centered moment kappa4 is in equation (2). If `d/n -> gamma>0`, then `d*E tr(B^4) -> 8/gamma^3`. Therefore `||B||_op=O_P(d^(-1/4)) -> 0`. The rate is not asserted sharp.

For standard Gaussian inputs, uncentered ReLU features and independent standard Gaussian first-layer weights, this proves

\[
 K_m=\frac{XX^T}{4d}+\mu_d aa^T+cI+o_{\mathbb P}(1)
\]

in operator norm, provided `m/n^2 -> infinity`. Here `a_i=||x_i||/sqrt(d)`, `c=1/4-1/(2*pi)`, and `mu_d=1/(2*pi)+1/(4*pi*d)+O(d^(-2))` is the exact radial mean from round 4. Equation (6) also gives a comparison preserving the diagonal exactly. The total finite-width operator error is `O_P(d^(-1/4)+n/sqrt(m))`.

An important failed simplification is now quantified: replacing mu_d by `1/(2*pi)` alone leaves operator error tending to `1/(4*pi*gamma)`. Keeping the quadratic radial correction is necessary for this operator approximation. Also `||B||_F^2 -> 2/gamma^2` in probability, so the elementary Frobenius shortcut fails despite operator convergence.

Equation (26), using the previous test-risk theorem and the new training lemma, replaces the original nonlinear training matrix inside its all-time realized-risk reduction by the displayed linear-plus-radial matrix. The network has only its output layer trained from zero, a Gaussian random linear teacher of energy E and independent Gaussian label noise of variance s^2. The radial spike is retained in H_t. This is not a deterministic limiting risk formula, a proof of two minima, or a peak-time calculation. Neither layer-learning dynamics nor proportional width is covered.

Verification was analytic. Re-enumerated the fourth trace by squaring B^2; checked n=2 and n=3; derived kappa4 both from raw spherical moments and a centered beta-moment recurrence; checked d=2 by angular integration; independently checked the covariance, eighth moment, ReLU constants, exact diagonal and all-time filter perturbation. No numerical program was run: the sandbox refuses the requested nice adjustment. No error in the stated new lemma was found.

The literature check closed within five minutes. The inspected [paper by Antoine Bodin and Nicolas Macris](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf), *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, still leaves a concentration hypothesis unproved. The opened recent diagnostic work and exact search queries are recorded in LOG.md. No inspected source supplied the requested theorem; this short check does not certify openness. No novelty claim over existing general kernel-linearization theorems is made for the training approximation itself; the contribution here is a self-contained proof closing this sequence's specific gap.

Commands and artifacts: read all three predecessor REPORT.md, LOG.md and PROOF.md files and all four ancestral Python scripts read-only. Text inspection used `rg --files`, `cat`, `sed` and `tail`; shell commands were prefixed with `nice -n 15 env OMP_NUM_THREADS=1` after initial discovery, and priority failure was recorded. Writes used the file-edit tool. Review `PROOF.md`, `LOG.md` and `REPORT.md` in this folder. No scripts, git, subagents, outside writes, publication or external messages.

What remains uncertain: the order-n radial spike cannot be deleted by a small operator perturbation. Its dynamical effect on the linear prediction still needs proof. The new rate and width condition may be improved, but neither supplies a positive double-descent example. No risk-derivative convergence or control of late finite-sample extrema is claimed.

Next worker: with `A=XX^T/(4d)+cI`, prove or refute

\[
 \sup_{t\geq0}\left\|\frac{X^T}{4d}
 [H_t(A+\mu_d aa^T)-H_t(A)]y\right\|\to0
 \quad\text{in probability}
\]

for the stated centered Gaussian teacher/noise law. A separate argument is needed for time derivatives near the initial order-1/n layer. If spike removal holds, use Gaussian quadratic-form concentration and the standard sample-covariance spectral law to derive the actual ReLU risk limit; the earlier isotropic MP profile has only one minimum. A positive double-descent construction must use a mechanism beyond that particular profile.

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 09:03 Asia/Tbilisi.
