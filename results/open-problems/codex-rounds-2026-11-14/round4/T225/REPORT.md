VERDICT: PARTIAL prediction-relevant exponentially small symmetry-restricted proximal gaps arbitrarily near Gaussian initialization

The general nonlinear MFLD risk-time question remains unresolved. The new
result shows that the polynomial frozen quotient gap from round 3 cannot
be extended uniformly to even a small fixed KL neighborhood of its Gaussian
initialization, including symmetric laws of lower risk and bounded moments.

For the same sine teacher, Gaussian inputs and fixed Gaussian parameter
prior, take independent standard Gaussians B,W and the explicit laws

\[
 \rho_\eta=\operatorname{Law}(B+\eta g(W),W),\qquad0<\eta\leq1.
\]

Here `g(w)=E sin(X)sin(wX)`. These laws have
`KL(rho_eta||pi)=eta^2 J/2`, second parameter moment `2+eta^2 J`, and
strictly lower teacher risk than pi, where
`J=(exp(-1/3)-exp(-1))/(2sqrt(3))`.
Their exact residual correlation is

\[
 G_\eta(w)=g(w)-\frac\eta{\sqrt3}
                   e^{-(1+w^2)/3}\sinh(w/3).
\]

PROOF.md proves that G_eta has exactly one positive zero. It has a positive
lobe and a negative lobe on the positive half-line. If A_eta and B_eta
are their positive heights, the corresponding proximal law satisfies

\[
 \limsup_{\lambda\downarrow0}\lambda^2\log\beta_S(p_{\eta,\lambda})
 \leq-\tfrac12\min(A_\eta^2,B_\eta^2)<0,
\]

and the same bound holds for its restricted LSI constant. Here S reverses
both parameter signs, as in round 3. The usual density comparison supplies
an exponential lower bound of the same order in lambda^-2; the precise
exponent is not claimed. The separating cutoffs are S-invariant, and
centered perturbations along them change predictions and give a nonconstant
quadratic teacher risk. Thus this bottleneck survives symmetry reduction
and is visible to prediction.

The earlier results hold. LOG.md records the independent re-derivation of
the original exponent, round-3 folded inequality, physical-time factor,
and nonlinear symmetrization identity. AUDIT.md independently checks the
new residual by two-kernel Gaussian integration, the unique zero by a
second-derivative test, the gap exponent by exact bridge capacity, and
prediction visibility by a conditional covariance. It also recovers J a
second way. No numerical simulation or eigenvalue computation was needed.

What failed: a nearby-law counterexample cannot be promoted to a statement
about the actual nonlinear trajectory. These rho_eta are explicit frozen
output-drift shears, not proved MFLD states. A rare well's prediction effect
can be very small, so visibility alone does not prove a lower bound for
reaching epsilon risk. The exponent depends on eta and tends to zero as
eta tends to zero; no contradiction with the earlier initialization gap
is present. No nonlinear runtime or annealing guarantee is claimed.

The brief web update found no whole-problem solution. LITERATURE.md lists
the three opened primary sources and their scope. This check does not
establish absence of a solution or novelty of the present application.

Commands: read-only inspections used `rg --files`, `cat` and `sed` under
`OMP_NUM_THREADS=1 nice -n 15`; final inspections are recorded in LOG.md.
The sandbox printed `nice: setpriority: Operation not permitted`, so no
heavy or numerical program was run with unverified priority. There is no
computation script or dataset. Deliverables were written with apply_patch
only inside this folder. Both earlier folders were read only. No git,
subagents, shared-state commands, posting or external mutation was used.

Next worker: analyze the actual trajectory's broader residual tails and
their prediction mass. One concrete starting point is the exact initial
predictor derivative: it has both output-weight and hidden-weight motion,
whereas the shear above keeps only the former and freezes the residual.
Determine whether the true residual develops a negative secondary lobe,
then whether that lobe carries enough mass to affect epsilon risk. A
uniform quotient-gap argument based only on symmetry, nearby KL, lower
risk and bounded second moments is now ruled out.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 05:07 Asia/Tbilisi; first recorded clock
was 05:07:42.
