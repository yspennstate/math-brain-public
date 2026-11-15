VERDICT: PARTIAL polynomial symmetry-restricted spectral gap for the sine proximal law and exact nonlinear symmetry reduction

The general polynomial-versus-exponential MFLD risk-time question remains
unresolved. The new result follows the earlier report's suggested step of
removing the feature-preserving sign symmetry.

For the same one-neuron sine teacher, Gaussian input and fixed Gaussian
parameter prior, let p_lambda be the proximal law frozen at initialization.
For functions invariant under `S(a,w)=(-a,-w)`, PROOF.md proves

\[
 \beta_S(p_\lambda)\geq
 \frac1{K(1+L/\lambda)^2}
 \geq\frac{\lambda^2}{8e^2}\quad(0<\lambda\leq1),
\]

where `L=sup|g'|<=1`, `g(w)=E[sin(X)sin(wX)]`, and K is an explicit
absolute constant at most 2e^2. Here beta_S uses variance versus Euclidean
gradient energy on the invariant subspace. This is a lower bound on the
restricted gap, rather than an asserted sharp asymptotic.

The proof folds to w>=0. The squared correlation g^2 has one peak there.
Two elementary density-ratio estimates give a temperature-independent
Poincare coefficient for the folded w marginal. Tensorization with the
centered conditional output Gaussian and a Lipschitz shear finish the proof.
The unrestricted gap still has the earlier exponentially small scale.

The frozen linear diffusion started at the Gaussian prior consequently
approaches its own equilibrium predictor within input L2 distance delta by
the explicit time

\[
 \frac{4e^2}{\lambda^3}
 \left[\frac{M^2}{\lambda^2}
 +\log\frac{1+M^2/\lambda^2}{\delta^2}\right],
 \qquad M=\max|g|,\quad0<\delta<1.
\]

This follows despite the exponentially large initial chi-square divergence:
its logarithm is only O(lambda^-2). It is a frozen-drift relaxation result,
not a learning-time result. Indeed the same proof establishes

\[
 \lim_{\lambda\downarrow0}\lambda^2R(p_\lambda)
 =\frac{M^2}{4}(1-e^{-2c^2})>0,\qquad c\tanh c=1.
\]

There is also an exact nonlinear consequence of removing the symmetry.
Symmetrization `rho -> (rho+S_#rho)/2` preserves predictions and commutes
with the nonlinear MFLD equation, including a prescribed annealing schedule.
In a class of unique solutions, initial laws with equal symmetrizations
have identical prediction and risk trajectories. Thus the earlier odd-cutoff
bottleneck perturbations cannot affect risk through later nonlinear feedback.
PROOF.md states the solution-class qualification explicitly; it does not
claim a general well-posedness theorem.

The earlier main claim holds. In addition to checking its Gaussian integration
and comparison lower bound, AUDIT.md re-derives the upper exponent with a
different cutoff: for fixed r>0,
`p_lambda(|a|<=r) <= exp(rM/lambda)/Z_lambda`. A clipped output-sign test
then recovers `lim lambda^2 log beta = -M^2/2`, independently of the earlier
hidden-weight sign test. The verified LSI lower bound and alpha<=beta give
the same LSI exponent.

AUDIT.md checks the new marginal gap a second way using its CDF and median,
and separately recovers both precise anchored constants by an integral-kernel
bound and integration by parts. It also checks the shear, physical-time
factor lambda, initial chi-square norm and predictor second moment. An
independent kernel expansion reproduces the frozen-risk constant.

The five-minute literature update found no whole-problem solution. The
opened sources and exact authors are recorded in LITERATURE.md, including
[Mousavi-Hosseini, Wu, Erdogdu, arXiv:2408.07254](https://arxiv.org/abs/2408.07254)
and [Wang, Chizat, arXiv:2602.11999](https://arxiv.org/abs/2602.11999).
The check is limited; originality of the functional-inequality application
has not been established.

What failed: transferring the frozen gap directly to nonlinear MFLD has no
justification. The evolving residual correlation need not have the geometry
used by the proof; no preservation theorem was obtained. Uncertainty remains
about the optimal quotient-gap power and the prediction-relevant nonlinear
rate. No quotient LSI, annealing runtime or exponential risk-time lower bound
is claimed.

Commands and output: LOG.md records the web queries, source reads, analytic
checks and final readback commands. No numerical computation or simulation
was run, so there is no computation script or numerical dataset. Shell
readbacks used `OMP_NUM_THREADS=1 nice -n 15`; the sandbox repeatedly printed
`nice: setpriority: Operation not permitted`. No heavy program was run under
the unverified priority. All deliverables were written with apply_patch in
this folder. The earlier folder was read only. No git, subagents or external
mutations were used.

Next worker: analyze the changing even residual kernel
`g_t(w)=K(1,w)-int a K(v,w) rho_t(da,dv)`, where
`K(v,w)=[exp(-(v-w)^2/2)-exp(-(v+w)^2/2)]/2`. Determine what geometry or
prediction-dissipation estimate can be maintained along the actual trajectory
from pi. The odd sector is now algebraically excluded, and its frozen
counterpart has a polynomial gap. A nonlinear bound must control the even
sector as the residual changes.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 03:31 Asia/Tbilisi; first recorded local
clock was 03:33:54.
