# T225 round 6 log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, approximately 11:23 Asia/Tbilisi.

## Setup and literature update

Read the brain navigation index and startup memory and the compute state.
The task-specific folder-only instruction takes precedence over shared
mesh/checklist/recall commands, which write outside this folder. No git,
subagents, or outside writes. Earlier folders are read only.

Every shell command after the initial listing requests
`OMP_NUM_THREADS=1 nice -n 15`. The sandbox reports
`nice: setpriority: Operation not permitted`. No numerical program or
simulation will be run under unverified priority. The governor reports
warn/cpu_saturated, owner_away_open. Work is analytic.

The first-five-minute web check used queries
`"mean-field Langevin" "polynomial" regression 2025 2026` and
`"mean-field Langevin" low temperature convergence single index`.
Opened arXiv pages 2606.31429, 2602.11999, 2406.17054, 2408.07254,
and full HTML for the first two. These concern spherical stationary
geometry, local rates assuming a Poincare inequality, bilevel dynamics,
or additional manifold assumptions. No solution of the stated general
Euclidean risk-time question was found. This is a bounded check, not an
absence or novelty claim. An accidentally mistyped arXiv id 2408.12019
opened an unrelated number theory paper; it is not used as evidence.
Literature checking ends here; authors and scope go in LITERATURE.md.

## Independent recheck before extension

The initial Fokker--Planck derivative is
`dot rho_0 = a ell(v) pi`, with `ell=g+v g'-g''`.
Gaussian integration by parts gives
`E ell(V) sin(Vx) = (1+x^2)H(x)+x H'(x)`,
`H=exp(-(1+x^2)/4) sin(x/2)/sqrt(2)`.
Its sine transform is `D=-2h''-w h'`, where
`h=exp(-(1+w^2)/3)sinh(w/3)/sqrt(3)`.
Differentiation recovers the reported coefficients 10, -2 and 5.
The initial risk dissipation independently equals
`E[g(V)^2+g'(V)^2] = (13 exp(-1/3)-3 exp(-1))/(18 sqrt(3))`.
The previous main claim holds. Readback of all earlier reports, logs,
proofs and available scripts is being completed; directory inventory
found no scripts in the four preceding folders.

## Chosen extension (before deriving it)

Compute the exact second time derivative of the actual nonlinear
residual at initialization, including its temperature contribution.
Use its sign and a justified third-order absolute remainder to attempt
to improve the previous positivity window `kappa<2` to
`kappa<sqrt(6)` in units `sqrt(log(1/t))`. This is one extension of
the local residual analysis, not an inference about risk convergence
time. A whole-tail sign at fixed positive time remains a separate issue.

## Earlier folders read; second derivative derived

Read the original, round-3 and round-4 REPORT.md, LOG.md and PROOF.md
in full, and round-5 REPORT.md, LOG.md, PROOF.md, AUDIT.md and
LITERATURE.md. No scripts were present. Read commands were `rg --files`,
`wc`, `cat`, `head`, with the priority prefix above. Their substantive
output is the earlier analytic formulas, not numerical computation.

Write `B=partial_v^2-v partial_v`, `ell_q=(1-B)q`, and let
`J_q(w)=E[q(V)K(V,w)+q'(V)partial_v K(V,w)]`.
The exact second derivative is
`ddot G_0 = E + lambda Z`,
where `E=J_D` and `Z=(-2 partial_w^2-w partial_w)D`.
The quadratic nonlinear drift terms disappear at initialization by
oddness in the centered output weight a. The temperature term does
not vanish at second order.

Direct differentiation gives
`ell_D(v)=exp(-(1+v^2)/3)/(81sqrt(3)) *
 [(20v^4-177v^2+146)sinh(v/3)+(269v-64v^3)cosh(v/3)]`.
Gaussian integration then gives
`E(w) ~ [5/(4096sqrt(2))] w^4 exp(-(5w^2-2w+5)/16)`.
Independently, applying the input-space initial neural tangent operator
twice gives the same exponent and coefficient. Also
`Z(w) ~ [2/(81sqrt(3))] w^4 exp(-(w^2-w+1)/3)`.
Both tails are positive. Thus E/g and Z/g have finite lower bounds,
uniformly yielding `E+lambda Z >= -C g` for 0<=lambda<=1.
The second-order tangent is globally positive for sufficiently small t.

The third-generator expression has parameter growth at most degree
four, so the earlier fourth moment bound suffices for a uniform
`O(t^3 min(|w|,1))` remainder. A proof with the time-dependent
operator terms written explicitly is being saved. This would improve
the actual-solution positivity window to every kappa<sqrt(6).

## Proof and independent audit saved

Saved PROOF.md with the exact second derivative, a closed Gaussian
formula for E, both positive tail asymptotics, and the cubic absolute
remainder. The solution class is the same fourth-moment energy class
used in round 5. Third differentiation costs at most fourth parameter
growth, so no stronger moment assumption is needed. The exact operator
formula is `L^3+2 L dot L+dot L L+ddot L` applied to aK.

Saved AUDIT.md. Independent input-space square completion reproduces
both the exponent `-(5w^2-2w+5)/16` and coefficient
`5/(4096sqrt(2))` of E. Applying the input operator twice independently
recovers the coefficient `2/(81sqrt(3))` of the temperature tail.
Single-exponential-branch differentiation checks all coefficients
20,-177,146,269,-64 in ell_D. The moment bound is re-derived by scalar
Ito calculus. Cutoff convergence at degree four is handled after time
integration, without assuming uniform integrability of fourth moments.

The resulting actual-flow window is
`L_3(t)^2=6 log(1/t)-1-2 log(4 C3(T))`, with G_t>=g/4 there for
sufficiently small t. C3(T) is finite and uniform in temperature but
not explicitly evaluated. This is an improvement in the leading
logarithmic coefficient, not necessarily a larger numerical interval
at any specified finite time. The whole-tail positive-time sign and
the original risk-time problem remain unresolved.

Saved LITERATURE.md with exact authors and opened primary sources.
No program, numerical value, eigenvalue computation or simulation is
claimed. All mathematical verification so far is analytic.

## Final report and readback

Saved REPORT.md with the required first-line verdict and the handoff.
Read all of PROOF.md and AUDIT.md back, and re-read REPORT.md in full.
An additional sign audit gives `E(1)=||U||_2^2>0` and
`Z(1)=E ell_g(V)^2>0`; hence
`ddot R_0=2||U||_2^2+lambda E ell_g(V)^2>0` independently of the
tail calculation. No correction to the main formulas was needed.

Final shell commands (all under the requested prefix):

```sh
OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l PROOF.md AUDIT.md LOG.md LITERATURE.md REPORT.md; cat REPORT.md; sed -n "180,440p" PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
OMP_NUM_THREADS=1 nice -n 15 sh -c 'sed -n "1,179p" PROOF.md; cat AUDIT.md; rg --files ~/codex_op_1114/briefs/T225 ~/codex_op_1114r3/briefs/T225 ~/codex_op_1114r4/briefs/T225 ~/codex_op_1114r5/briefs/T225; head -1 REPORT.md'
```

Output before this append: PROOF.md 428 lines, AUDIT.md 183,
LOG.md 120, LITERATURE.md 43, REPORT.md 81. Clock:
`2026-11-15 11:30:07 +04`. The repeated inventory confirms no earlier
computation scripts. Both reads completed immediately and repeated
the nice permission warning. All deliverables stay in this folder.
The chosen extension is complete; the original risk-time problem
and remote positive-time residual sign remain unresolved.
