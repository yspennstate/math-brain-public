# T225 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 2026-11-15 01:07:42 UTC, 05:07:42 Asia/Tbilisi.

## Setup and literature check (01:07–01:10 UTC)

Read the original and round-3 REPORT.md, LOG.md, PROOF.md, AUDIT.md and
LITERATURE.md. The recursive file listing found no computation scripts in
either earlier folder. Read the startup memory and compute state; the latter
reports `warn`, `owner_away_open`, and CPU saturation. No simulation is planned.
The folder-only order precludes shared mesh/checklist/brain mutations, so
those commands are not run. No git or subagents.

Read commands request `OMP_NUM_THREADS=1 nice -n 15`. The sandbox reports
`nice: setpriority: Operation not permitted`; no heavy program will be run
under this unverified priority. Only short file reads and analytic work.

Web queries:

- `"mean field Langevin" polynomial convergence two layer 2026`
- `"2602.11999" Langevin`
- `"mean-field Langevin" lower bound low temperature neural networks`

Opened https://arxiv.org/abs/2602.11999,
https://arxiv.org/abs/2606.31429 and https://arxiv.org/abs/2408.07254.
The first is local convergence, the second stationary spherical geometry,
and the third has conditional polynomial spherical guarantees. No new
whole-problem solution was found. This limited update ends within five minutes;
it does not prove absence of a solution elsewhere.

## Independent recheck of earlier results

The original Gaussian square-completion identity gives
`a|w ~ N(g(w)/lambda,1)` and marginal proportional to
`exp(g(w)^2/(2 lambda^2)) gamma(dw)`. Its LSI comparison costs exactly
`exp(M^2/(2 lambda^2))` and a polynomial shear. A cutoff through `w=0`
recovers the matching upper exponent. This original claim holds.

For the round-3 restricted gap, independently use integration by parts on
the right of c: if Q(s)=int_s^infty q(r)dr, the density ratio gives
`Q(s)<=q(s)/c`. With v(c)=0, Tonelli/integration by parts gives
`int v^2 q = 2 int v v' Q <= (2/c)(int v^2 q)^(1/2)
(int v'^2 q)^(1/2)`, hence the coefficient `4/c^2`.
On the left the direct integral kernel is bounded by
`exp(c^2/2)(cs-s^2/2)<=c^2 exp(c^2/2)/2`. Tensorization and the shear
give precisely `K(1+L/lambda)^2`. Folding is legitimate for S-invariant
tests. The physical generator is lambda times the reversible unit generator;
its chi-square rate has factor `2 lambda beta_S`. All these claims hold.
The nonlinear symmetrization identity also holds because every feature is
S-invariant and the residual drift is S-equivariant. As in round 3,
this assertion is conditional on uniqueness in the selected solution class.

## Chosen extension, before proving it

Test stability of the single-peak residual geometry near initialization.
Use the explicit symmetric law `rho_eta = Law(B+eta*g(W),W)`, with B,W
independent standard Gaussians and `0<eta<=1`. This is the exact frozen
output drift for duration eta with w held fixed and the initial residual
held fixed; it is NOT a claimed point on the full nonlinear
MFLD trajectory. Its KL to pi is exactly `eta^2 E[g(W)^2]/2`, so it approaches
pi arbitrarily closely.

The residual correlation is `G_eta(w)=g(w)-eta*h(w)`, where independent
Gaussian integration gives `h(w)=exp(-(1+w^2)/3)*sinh(w/3)/sqrt(3)`.
The broader Gaussian tail forces a sign change on the positive half-line.
The intended theorem is an exponentially small symmetry-restricted proximal
gap for every fixed eta>0, with a bottleneck that demonstrably changes the
predictor. This would obstruct extending the earlier frozen gap to all nearby
laws merely by KL, moments, symmetry or small risk decrease. It would still
leave the actual nonlinear trajectory and risk-time question open.

## Analytic result saved

Wrote PROOF.md with the explicit residual, its unique positive zero,
the exponentially small S-restricted proximal Poincare and LSI bounds,
and prediction visibility of centered cutoff perturbations. The exponent
upper bound is `-min(A_eta^2,B_eta^2)/2` in `lambda^2 log beta_S`, where
A_eta and B_eta are the two positive lobe heights. The proof retains both
well masses, including an exponentially rare well. The standard comparison
lower bound gives the complementary `exp(-O_eta(lambda^-2))` scale.

Wrote AUDIT.md. Its independent routes are: direct two-kernel integration
for h rather than the predictor calculation, a second-derivative test for
the ratio h/g rather than its power series, the exact one-dimensional
capacity rather than a linear bridge cutoff, and a sharp-gate covariance
for prediction rather than Fourier uniqueness. J is recovered both as
`E g(W)^2` and as `h(1)`. No discrepancy was found.

The main attempted overinterpretation fails: these are explicit nearby
laws, not identified states of the nonlinear trajectory. The theorem does
not prove an exponential nonlinear risk-time lower bound. The rare well's
nonzero predictor effect need not have a size independent of lambda.

## Final readback and handoff

Saved LITERATURE.md and REPORT.md. The first multi-file patch for these two
files was rejected before writing because a LOG.md context line did not
match; the corrected patch succeeded. The correction also replaced an
ambiguous reference to an output-only gradient flow with the precise
description “frozen output drift.” No mathematical claim changed.

Final inspection commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 wc -l PROOF.md AUDIT.md LOG.md LITERATURE.md REPORT.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '1,240p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '241,470p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md LOG.md LITERATURE.md
```

The line count before this log append was PROOF.md 444, AUDIT.md 186,
LOG.md 93, LITERATURE.md 42, REPORT.md 82. Readback confirmed the verdict
prefix, all factors of 1/2, the two interval masses in the variance bound,
the scope qualifications, and the handoff. Every shell inspection again
printed `nice: setpriority: Operation not permitted`. No numerical program,
simulation or external mutation was run. All claimed constants are symbolic
and independently re-derived in AUDIT.md.

Next checkable step: derive the full initial predictor derivative under
MFLD, including hidden-weight motion, and assess the residual's far-tail
sign with quantitative error control. An output-only frozen shear cannot
substitute for that calculation. Any later risk-time obstruction must also
bound the secondary well's effect on epsilon risk from below.
