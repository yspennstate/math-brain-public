VERDICT: PARTIAL exact initial nonlinear residual motion and a quantitative positivity window for the sine teacher

The general polynomial-versus-exponential MFLD risk-time question remains
unresolved. The preceding shear obstruction is correct. The new result
derives the actual nonlinear flow's initial motion and shows why that
shear cannot substitute for it.

For the same one-neuron sine teacher, Gaussian inputs and fixed standard
Gaussian parameter prior, define
\[
 g(w)=e^{-(1+w^2)/2}\sinh w,\qquad
 G_t(w)=\mathbb E[(\sin X-f_{\rho_t}(X))\sin(wX)].
\]
Starting from the prior, PROOF.md proves
\[
 \dot G_0(w)=-\frac{e^{-(1+w^2)/3}}{9\sqrt3}
 [(10-2w^2)\sinh(w/3)+5w\cosh(w/3)].
\]
This derivative includes output-weight and hidden-weight motion and is
independent of the initial temperature. Its sign changes exactly once
on the positive half-line, from negative to positive, at a frequency
between 3 and 5. In particular the true initial residual derivative is
positive in the far-frequency tail; the earlier shear's derivative is
negative there.

Writing D for the negative of this derivative, the tangent residual
`g-tD` is positive on the entire positive half-line for sufficiently
small t. For actual local MFLD solutions, the proof also establishes
\[
 |G_t(w)-g(w)+tD(w)|\leq C_Tt^2\min(|w|,1),
\]
uniformly over constant temperatures `0<lambda<=1`. Consequently
`G_t(w)>=g(w)/4>0` for
\[
 0<w\leq\sqrt{4\log(1/t)-1-2\log(4C_T)}
\]
at sufficiently small times. The explicit, loose constant is
`C_T=15000(13exp(20T))^2`. These statements apply to W2-continuous
weak MFLD solutions with locally bounded fourth moments and the
free-energy inequality, initialized at the prior. No general
well-posedness theorem is claimed.

The initial risk slope is exactly
\[
 \dot R_0=-\frac{13e^{-1/3}-3e^{-1}}{18\sqrt3}.
\]
AUDIT.md independently recovers the residual derivative from the initial
Fokker–Planck density derivative and Gaussian moment-generating functions,
and the risk slope from parameter-gradient dissipation. It rechecks
the moment and Taylor constants with scalar Itô calculus and a second
product-rule expansion of the generator. The earlier restricted-gap
exponent is re-derived using exact bridge capacity, including the rare
well's mass. No discrepancy was found.

What failed: the Taylor estimate is absolute, not relative to the
Gaussian-decaying g. It cannot establish positivity on the whole
half-line at a fixed positive time. A remote or later negative lobe
remains possible. No restricted proximal-gap estimate along the actual
flow, polynomial learning-time guarantee, exponential learning-time lower
bound, or annealing remainder estimate is obtained.

The five-minute web update found no whole-problem solution. LITERATURE.md
records the three opened primary sources and their scope. This is a
limited check and does not establish absence of a solution or novelty.

Commands: earlier work and the deliverables were inspected with
`rg --files`, `cat`, `head`, `sed` and `wc`, using
`OMP_NUM_THREADS=1 nice -n 15` after the initial directory listing.
The sandbox reports `nice: setpriority: Operation not permitted`, so no
simulation or numerical program was run under unverified priority.
There is no computation script or dataset: the result is analytic.
LOG.md records the searches, derivations and readback commands. All
writes used apply_patch inside this folder. Earlier folders were read
only; no git, subagents or shared-state commands were used.

Next worker: obtain a remainder estimate that resolves the residual
tail at positive time, rather than merely its derivative at zero.
The useful exact starting point is
`dot rho_0 = a[g(v)+v g'(v)-g''(v)]pi` and the kernel generator formula
in PROOF.md (37). Determine whether remote negative lobes occur beyond
the positivity window, or whether an appropriate sign/shape property
persists. Any eventual risk-time obstruction must also quantify the
prediction mass of the secondary well. The shear is a valid nearby-law
counterexample, but its tail sign does not match the full initial flow.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 08:44 Asia/Tbilisi.
