# T225 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session date: 15 November 2026, Asia/Tbilisi; exact local clock recorded below.

## Setup and short literature check

Read the earlier REPORT.md, LOG.md, PROOF.md, AUDIT.md and LITERATURE.md in
`~/codex_op_1114/briefs/T225`, without editing them.
`rg --files` found no computation scripts in that folder, consistent with its
report. Read the brain navigation index and compute governor state. The latter
reported `status: warn`, `mode: owner_away_open`, CPU saturation. This session
will use analytic arguments, with no simulation or heavy computation.

The explicit folder-only instruction takes precedence over the global mesh,
checklist and brain-write instructions: their commands write outside this
folder and were not run. No subagents or git commands are used.

Initial shell inspection used `pwd`, `rg --files`, `cat` and `ls`. Subsequent
shell commands request `OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints
`nice: setpriority: Operation not permitted`, so actual priority cannot be
verified. Only short read-only inspection commands have run; no numerical
program will be run with unverified priority.

Web searches (the literature check ended within five minutes):

- `mean field Langevin dynamics polynomial convergence low temperature two layer neural networks 2026 2025`
- `"2606.31429" Langevin`
- `"mean-field Langevin" "sine" convergence`

Opened the arXiv pages for 2408.07254, 2606.31429, 2602.11999 and 2610.35528.
The first two retain the same versions as the earlier report. The latter two
concern local convergence/stability. No newly located whole-problem solution
was found. This limited search does not establish absence of one. Exact
authors, links and scope will be recorded in LITERATURE.md.

## Earlier result: independent re-derivation

The claimed asymptotic holds. With `t=1/(2 lambda^2)`, Gaussian integration
gives `E_A exp(A g(w)/lambda)=exp(t g(w)^2)`. Thus the w marginal is
`Z^-1 exp(t g(w)^2) gamma(dw)`, with
`g(w)=[exp(-(w-1)^2/2)-exp(-(w+1)^2/2)]/2`.
For every fixed delta>0, a neighborhood of a maximizer gives
`Z >= c_delta exp(t (M-delta)^2)`, while `Z <= exp(t M^2)`.
An odd sign cutoff has variance tending to one and energy confined to a
strip where `g^2 <= delta^2`; its Rayleigh quotient therefore has upper
logarithmic exponent `-M^2/(2 lambda^2)`. Conversely the density comparison
to a product Gaussian has ratio at most `exp(t M^2)`, and the shear
`(b,w) -> (b+g(w)/lambda,w)` costs at most `(1+L/lambda)^2`.
These bounds reproduce both LSI and Poincare exponents, with the same factor
one half. The identity `a sin(wx)=(-a) sin(-wx)` confirms that the sign
cutoff perturbation changes no predictor. No defect was found in the stated
earlier theorem.

## Chosen extension, recorded before the proof

Prove a polynomial lower bound on the Poincare constant restricted to
functions invariant under `(a,w)->(-a,-w)`, for the same frozen proximal
law. Folding to `w>=0` leaves a single peak of `g^2`. An elementary anchored
one-dimensional inequality should bound the Poincare constant of the folded
w marginal uniformly in lambda; tensorization and the same shear should
then give a quotient constant at least `c/(1+L/lambda)^2`.

Why this piece: the earlier report explicitly asks for a study after removing
the sign symmetry. This would distinguish a genuine slow prediction mode
from the parameter-label bottleneck, without claiming anything about the
still-changing self-consistent drift. A consequence to check is polynomial
relaxation of the frozen linear dynamics started at the Gaussian prior.

## Proof saved: quotient gap and frozen relaxation

Exact clock from the setup command: `2026-11-15 03:33:54 +04`
(Asia/Tbilisi). The task arrived shortly before this, at approximately 03:31.

Saved PROOF.md. The folded marginal has density proportional to
`exp(-r^2/2+g(r)^2/(2 lambda^2))` on `r>=0`. With `c tanh(c)=1`,
the exact monotonicity of `g^2` gives two temperature-independent ratios:

- `q(r)/q(s) <= exp(c^2/2)` for `0<=r<=s<=c`;
- `q(r)/q(s) <= exp(-c(r-s))` for `r>=s>=c`.

Anchoring at c gives Poincare coefficient
`C=max(c^2 exp(c^2/2)/2,4/c^2)` for this marginal. Tensorizing with the
conditional centered output Gaussian and using the shear gives
`beta_S >= 1/[K(1+L/lambda)^2]`, where `K=max(1,C)<=2e^2` and `L<=1`.
Thus `beta_S >= lambda^2/(8e^2)` for `0<lambda<=1`.

For the frozen diffusion with physical diffusion coefficient lambda,
the symmetric Gaussian initial density has exactly
`chi^2(pi||p_lambda)=Z_lambda^2-1`. Its decay rate is at least
`lambda^3/(4e^2)`. Despite its exponentially large initial chi-square norm,
the logarithm of that norm is only O(lambda^-2). PROOF.md equation (31)
therefore gives an explicit polynomial time to its own equilibrium predictor.

Also proved `lambda^2 R(p_lambda) -> M^2(1-exp(-2c^2))/4 > 0`.
This checks that frozen relaxation cannot be reported as successful learning.
The changing self-consistent correlation g_t is not controlled by the proof.

An attempted empty log patch had a context mismatch and made no change;
the present append records the actual saved result. All writes use apply_patch
and stay in the current task folder. No computation has been executed.

## Independent audit and exact nonlinear symmetry check

Saved AUDIT.md with a second proof of the temperature-independent folded
marginal gap, using its CDF and median. Separately recovered the exact left
anchored constant by a Hilbert--Schmidt kernel bound and the right constant
by integration by parts. Checked the shear singular value, Gaussian factor,
physical-time factor lambda, exact initial chi-square norm, and predictor
second moment. A separate two-variable kernel expansion reproduces the
positive frozen-risk asymptotic.

The audit also checked whether the odd mode could feed back into predictions
through the changing nonlinear drift. It cannot: symmetrization preserves
the predictor, hence preserves the drift, and commutes with its generator.
Added the complete weak-equation calculation to PROOF.md Section 7.
It applies to a prescribed common annealing schedule as well. Within any
class of unique solutions, the earlier odd-cutoff perturbed laws have equal
prediction trajectories for all times. This is an algebraic consequence of
the chosen quotient extension, not a nonlinear convergence-rate claim.

No gap was found in the new inequalities. The missing step is control of
the evolving even residual correlation; its single-peak shape has not been
proved. No quotient LSI, optimal quotient-gap power, or nonlinear learning
time is claimed.

## Final recheck before reporting

Added a genuinely different-coordinate verification of the earlier exponent
to AUDIT.md: a sign cutoff in a rather than w. For a fixed r>0,
`p_lambda(|a|<=r) <= exp(rM/lambda)/Z_lambda`; since
`lambda^2 log Z_lambda -> M^2/2`, its Rayleigh quotient gives the same
upper exponent `-M^2/2`. This and the checked shear lower bound confirm
the main earlier claim by an independent bottleneck calculation.

Read back the saved PROOF.md and checked its equations (1)--(40). Corrected
two TeX formatting slips. A multi-file patch containing a log-context mismatch
was rejected atomically; readback confirmed no partial change before retrying.
Reopened the arXiv page for 2610.35528 solely to verify the authors Jing An
and Lihan Wang; no further literature search was undertaken.

Readback commands (all completed immediately):

```sh
OMP_NUM_THREADS=1 nice -n 15 wc -l LOG.md PROOF.md AUDIT.md LITERATURE.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '1,230p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '231,540p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 head -8 PROOF.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '1,65p' AUDIT.md
OMP_NUM_THREADS=1 nice -n 15 tail -15 LOG.md
```

The first line count, before the final audit append, reported PROOF.md 555,
AUDIT.md 175, LITERATURE.md 40 and LOG.md 125 lines. Every shell invocation
again printed `nice: setpriority: Operation not permitted`. There are no
numerical scripts or claimed numerical outputs; the result is an analytic
inequality and its consequences.

## Completed report and final readback

Wrote REPORT.md with the required first line
`VERDICT: PARTIAL polynomial symmetry-restricted spectral gap for the sine proximal law and exact nonlinear symmetry reduction`.
Read it in full and checked its constants and scope against PROOF.md.
Also read the last proof section through equation (41), and confirmed the
corrected TeX lines. Commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 head -6 PROOF.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '126,140p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '530,565p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
OMP_NUM_THREADS=1 nice -n 15 wc -l LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md
```

Readback showed PROOF.md 555, AUDIT.md 197, LITERATURE.md 40 and REPORT.md
104 lines (LOG.md was 157 lines before this append). All reads finished
immediately and again printed the priority warning. No further mathematical
changes were needed. The original nonlinear risk-time problem remains open;
the complete chosen quotient extension and its limitations are saved.
