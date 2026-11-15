# T179, round 6

Task: “take the NEXT checkable step on this problem, building on that work.”
Received: 15 November 2026, approximately 11:07 Asia/Tbilisi.

## Orientation and literature check

Read the startup memory and compute state. The latter says `status=warn`,
`mode=owner_away_open`; only tiny single-process arithmetic checks are planned.
The task-specific instruction forbidding writes outside this folder overrides
the usual external mesh, checklist, and brain-log writes. No git or subagents.
Earlier folders are read-only inputs.

Web searches, completed in under five minutes:

- `"2611.07310" Han stochastic heat uniqueness`
- `"Weak uniqueness" "full Hölder regime" Han stochastic heat`
- `"Han" "stochastic heat" "uniqueness" "November" "2026" "2611"`
- `"stochastic heat" "nondegenerate" "uniqueness" "2611.07310" delay`

Opened the official abstract and full HTML:
https://arxiv.org/abs/2611.07310 and
https://arxiv.org/html/2611.07310v1.
The abstract identifies Yi Han and the submission history still lists only
v1, 5 November 2026. This is the paper already recorded in round 1's
SOLVED_ELSEWHERE.md and used conditionally in rounds 3--5. No later result
changing their picture appeared. This is not a new discovery of a solution;
the unbounded-coefficient/general-L2 corner and the proposed drift extension
are assessed using the earlier reports' precise scope, not the abstract alone.

## Initial audit and choice, before the extension

Read round 5's full PROOF.md. Reconstructed its causal Bochner averages:
continuous adapted averages are raw predictable; their pointwise limit is
predictable and agrees with the Borel drift for almost every time on each
individual path. Continuity of the state preserves the current-norm bound
at the differentiation limit. No exceptional set common to all paths is
needed. The weighted elementary approximation in Section 5 also checks:
its squared error converges in probability under the drift-free measure,
then under every equivalent measure. Cauchy--Schwarz controls the drift
correction and localization at the bracket controls stochastic integral
errors. Neither step requires convergence in L2 under the new measure.

Choice: extend the growth assumption to
`||B(t,path)|| <= K(1 + sup_(r<=t)||path_r||)`.
The missing piece is a maximal moment estimate uniform in all predictable
drift multipliers in [0,1], including both stopped Girsanov equations.
Use factorization in H (rather than spatial supremum estimates), with
eighth moments and factorization exponent 3/16. This keeps the diffusion
estimate dependent only on its linear growth, not on beta approaching one.
First prove the stopped maximal estimate, then apply the already audited
canonical-density construction. Unbounded delay drifts will give a strict
new example. No independent proof of Han's main uniqueness theorem is claimed.

Further reading, independent reruns, constants, and attempted counterchecks
will be appended as they are completed.

## 11:09--11:15 +04: predecessor audit completed

Read all four reports, logs, proofs and Python scripts. Re-read smaller
chunks where an initial concatenation exceeded the tool output limit.
The first script writes a CSV beside itself and was not rerun, to preserve
the earlier folder. The round-5 script has no file writes and was rerun:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T179/check_history.py
```

Exit 0; output:

```text
nice: setpriority: Operation not permitted
Two-stage history-dependent Gaussian laws: 54 cases passed
Normalization and both entropies checked by 1D quadrature
Positive/negative first drift and history control; zero cases included
Largest normalization/doubled-entropy residual: 9.83e-11
Entropy difference has the sign of the first drift when k != 0
Causal time average: four exact piecewise-polynomial error checks
L1 error = window; squared L2 error = 2*window/3
nice=20; elapsed=0.280s; peak RSS=13.89 MiB
```

The launcher warning is the same inherited-priority issue as before: the
script verified nice 20 before calculation. No earlier file was changed.

Independently checked the main density identity without the diagnostic:
the state martingale integral of `B/g^2` is `J`; under the drifted law it
is `integral (B/g) dW + A`. Thus the forward log density is `J-A/2`,
with means `+E_B A/2` under the drifted law and `-E_0 A/2` under the
drift-free law. Weighted approximation transfers in probability, and
its finite-variation error is at most sqrt(A) times the weighted error.
The raw predictable representative also checks path by path, including
nonconvergence points and time zero. No error in round 5 was found.

For the chosen extension, the H-valued factorization uses p=8 and eta=3/16.
The inner heat singularity is 7/8<1; the outer Holder exponent is -13/14>-1.
After the two time integrations their combined small-time factor is t,
matching p/4-1=1. This yields an ordinary integral Gronwall inequality
for the stopped running maximum, rather than an invalid substitution of
sup E for E sup. Detailed proof is being saved next.

## Extension proof and diagnostic saved

Wrote PROOF.md with the maximal estimate and the full transfer proof.
For arbitrary predictable kappa in [0,1], it gives
`E sup_(t<=T)||U_t||^8 <= C8(T)(1+||h||^8)` and hence
`E(1+sup_(t<=T)||U_t||^2) <= C2(T)(1+||h||^2)`.
The constants are explicit, using a proved terminal martingale constant
`b8=28^4*(8/7)^24`. The stopped convolution is distinct from the stopped
state; its histories agree with the original only through the stop.
This suffices for the running-norm growth bound.

Reconstructed predictability, both stopped changes of measure, canonical
density, uniqueness, and entropy identities with the new maximal energy
bound. No extra uniqueness assumption on state and noise is introduced.
The drift `B(t,path)=a path_((t-delta)^+)` is a strict extension: a past
spike can have arbitrarily large norm while the current state is zero.

Added check_maximal.py. It checks the fractional exponents with rational
arithmetic, the time integral using v=x^8, the general p>4 scaling law,
the beta integral after a nonsingular change of variable, and the exact
mass variance for a delayed Brownian equation in two independent ways.
It also checks continuous fixed-start spike laws showing why fixed-time
moment bounds do not imply a uniform maximal bound. No SPDE is simulated.
Next: run it and audit the proof against the output. One combined patch
failed context matching and changed no file; it was reapplied correctly.

## 11:17 +04: new diagnostic passed

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_maximal.py
```

Exit 0; output:

```text
nice: setpriority: Operation not permitted
p=8, eta=3/16: inner exponents -3/8 and -7/8; outer -13/14
outer factor 14^7*t^(1/2); combined singular factor t^1
five independent p>4 scaling checks: p/4 - 1
inner time integral and factored F(t): 9 exact checks
terminal martingale constant: 28^4*(8/7)^24, exact
factorization beta integral: quadrature residual 1.27e-12
delayed mass variance: 24 exact covariance/isometry/square checks
four continuous fixed-start spike laws: marginal bound 4/3; max square n
four initial-norm moment reductions checked exactly
nice=20; elapsed=0.001s; peak RSS=13.58 MiB
```

Again actual nice is 20; no calculation was affected by the launcher warning.
No diagnostic failed. Peak memory is below 1 GiB by a factor greater than 70.

## Self-audit and failed shortcuts

Re-derived the load-bearing time powers independently: for arbitrary p>4,
the inner singular contribution has exponent `(1/2-2eta)*p/2`, and the
outer one has exponent `p*eta-1`. Their sum is `p/4-1`, independent of
eta. For p=8 it is one, matching the direct `t^(1/2)*Q(t)^4` calculation.
The substitutions v=x^8 and v=x^14 verify the three denominators 8/5,
8, and 14 separately. The factorization beta constant was checked by a
smooth quadrature after x=y^16 and inversion on the infinite half-line.
The terminal moment constant follows from Ito's coefficients 4+24=28
and Doob's eighth-moment factor, not an unstated numerical BDG value.

The random triangular-bump example shows exactly why the earlier fixed-time
bound alone cannot handle the new growth condition. Its mixture has
infinite expected squared maximum while every fixed-time moment is <=4/3.
These are moment examples, not SPDE solutions or counterexamples to uniqueness.

The rank-one delay drift gives a direct independent density check. On
[0,2delta] its stochastic integral is conditionally Gaussian given the
first-interval history, with variance A. The conditional exponential has
mean one even for large coefficients. Both entropies equal a^2 delta^2/4.
Full Novikov fails whenever a^2 delta^2>=3 by the Gaussian-integral lower
bound; this is a sufficient, non-sharp condition. The stopped proof and
the direct conditional normalization still work.

Checked the strictness example even on paths starting from the fixed zero
state: a path can have height N at delta and return to zero at 2delta.
Unbounded diffusion, beta near one, arbitrary deterministic L2 initial
states, zero drift, and either sign of a or g are all allowed. Constants
are very large but finite; no sharpness or useful numerical bound is claimed.

## Report saved; final audit

Wrote REPORT.md with the required first-line verdict. The result is the
running-maximum growth extension conditional on (D), not a new proof of
the positive-Hölder drift-free theorem. The report states both commands,
actual resource use, the failed shortcuts, the external uncertainty, and
one concrete next step. All changes are confined to this folder.

Rechecked the proof's successive dependencies: law-independent predictable
representative; factorization for bounded then integrable H-valued noise
coefficients; finite stopped eighth moments before Gronwall; equality of
histories only before the norm stop; energy control under both stopped
Girsanov measures; and weighted canonical approximation after full
normalization. The entropy formulas use energy under the correct law.
The strict delay example and its rank-one diagnostic are distinguished,
so no whole-path entropy is inferred from a mass projection alone.

No further numerical run is needed after the example and prose additions:
the diagnostic and all its tested formulas were unchanged. The Gaussian
delay normalization and entropy checks are analytic in PROOF.md. The next
worker should first audit Sections 2--3, then consider random initial laws
with finite second moment by conditional estimates and measurable mixtures.
