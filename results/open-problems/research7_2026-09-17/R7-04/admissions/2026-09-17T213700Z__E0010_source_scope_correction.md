Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0010 source-scope correction — meaning of “nontrivial stationary distribution”

This is an additive correction to `2026-09-17T213400Z__E0010_admission.md`; the earlier admission file is not edited.

The first admission record reproduced Durrett Problem 4 correctly but stated its closure criterion too literally as “exactly one invariant law other than the absorbing all-zero law.” Taken literally, that cannot be right: if `delta_0` and a positive invariant law `nu` are stationary, then every convex combination `a delta_0+(1-a)nu` is stationary.

The primary source itself fixes the intended convention immediately before the fast-stirring section. In its discussion of the one-type contact process it says that the positive stationary laws are unique **when one specifies that there is no mass on the all-zero state**, and then says all stationary distributions are convex combinations of the extremal phase laws. Problem 4 is introduced as the analogous desired uniqueness/convergence question for sexual reproduction.

Accordingly, throughout R7-04 the exact source closure criterion is interpreted as follows:

For every fixed `beta>4.5`, prove that there exists `epsilon_0(beta)>0` such that for every `0<epsilon<epsilon_0(beta)` there is a unique stationary probability law `nu_bar` satisfying

`nu_bar({all-zero configuration}) = 0`.

Equivalently, the only extremal invariant laws should be the absorbing `delta_0` and the unique positive law `nu_bar`; then all invariant laws are their convex combinations. A full complete-convergence theorem would be stronger, but is not silently required unless it is needed by the proof.

This interpretation matches the source's own convention and removes the otherwise trivial convex-mixture obstruction without changing the mathematical model or adding a new conjecture.

The admission metric `Q_SR` is therefore read with

`I^nt_{beta,epsilon} = { stationary mu : mu({0-bar})=0 }`.

The one-site definition remains sufficient: translations of any such stationary `mu` are again in `I^nt`, and the upper invariant law is translation invariant. Thus `Q_SR=0` forces equality of every one-site marginal at every translate; under a monotone coupling with the upper invariant law, each sitewise disagreement is nonnegative with zero mean, hence vanishes almost surely at every site and the two laws coincide.

No source verdict changes: E0010 remains ADMITTED / CLOSABLE OUTSIDE / OPEN under bounded current-status review.
