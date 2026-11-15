# T423 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, 06:39 Asia/Tbilisi (02:39 UTC).

## 1. Reading and literature check

Read both predecessor REPORT.md, LOG.md, PROOF.md files and round 3's
audit.py. The first folder contains no standalone research script;
its log contains a document-check script. Both folders remain untouched.
Read the brain startup, navigation index and compute state. Global brain,
mesh and checklist commands would write outside this folder and are not
run under the task-specific restriction. No git or subagents.

Compute state: warn, owner_away_open, CPU saturated. Only tiny standard
library checks and analytic work are planned. Subsequent local commands
use OMP_NUM_THREADS=1 and nice -n 15. Initial read-only orientation
commands omitted the prefix; no numerical workload was involved.

The web-search check took less than five minutes. Queries:

- `"super-Brownian" "pathwise uniqueness" 2025 2026 density`
- `"stochastic heat equation" "sqrt" "pathwise uniqueness" immigration super-Brownian 2026`

Primary arXiv records actually opened:

- Hao Wang, https://arxiv.org/abs/1612.06055: withdrawn, with a gap in
  the main proof explicitly recorded.
- Leonid Mytnik and Johanna Weinberger,
  https://arxiv.org/abs/2509.10984: weak existence and uniqueness with
  irregular drift; latest revision displayed is 12 August 2026.
- Yi Han, https://arxiv.org/abs/2611.07310: weak uniqueness with
  uniformly nondegenerate diffusion on the torus, submitted 5 November 2026.
- Yu-Ting Chen, https://arxiv.org/abs/1308.5141: nonuniqueness with immigration.

No verified resolution of the stated equation was found. Limited search
coverage does not establish absence of a resolution.

## 2. Independent verification of the earlier result

Let U,V be the two masses, C=integral sqrt(uv), and
A=U+V-2C. Expansion of the two marginal variances and their covariance
gives E(U_t-V_t)^2=2mt-2 E integral C=E integral A. Thus the
terminal-mass reduction holds. The nonnegative zero integral forces
field equality by joint continuity.

For the round 3 main claim, independently solve the backward equation
f_s+(x/2)f_xx=0 with f(s,x)=exp(-b_s x),
b_s=lambda/(1+(T-s)lambda/2). Ito's formula in the actual joint
filtration gives E(exp(-lambda U_T)|F_t)=exp(-b_t U_t).
The bounded lambda-to-infinity limit is exp(-2U_t/(T-t)). Equality
almost surely of terminal extinction indicators forces equality of these
conditional expectations, hence equality of U_t,V_t for every rational
t<T, then of paths and fields. This main claim holds. No marginal
Markov argument in an enlarged filtration is needed.

Absorption gives the prior lower bound by retaining E_t at a fixed
earlier time; conditional survival and the limit T(1-exp(-2S/(T-t)))
give factor 2. Its domination by 4S for T>=2t is valid. The prior
large-time criterion therefore also holds.

## 3. Choice made before the extension

Try to connect the inverse-time extinction-disagreement tail exactly
to the expected local time at zero of D=U-V. At minimum, improve the
prior lower bound from 2 E[(U_t+V_t)1_{E_t}] to 2 E|U_t-V_t|,
using conditional Jensen and the injective exponential observation.
The stronger target is an exact large-time limit in terms of total
expected local time. This is one extension of the prior tail criterion.

Reason: E|D_t| is monotone and bounded by 2m, and Tanaka identifies it
with expected local time. A change-of-variables formula for the minimum
of the two exponential martingales may express delta_T through that
same local-time measure, rather than the quadratic weighted energy.
Audit targets are its Tanaka factor, the singular terminal time, tail
contributions with t close to T, and any unjustified uniform integrability.

## 4. Extension derived

The stronger target works. With symmetric local time normalized by
|D_t|=integral sgn(D)dD+L_t, put ell=E L_infinity=lim E|D_t|<=2m.
For theta>0 and b_s=theta/(1+(T-s)theta/2), the min/max Tanaka
calculation gives the exact identity

    E|exp(-theta U_T)-exp(-theta V_T)|
      = E integral_0^T b_s exp(-b_s U_s) dL_s.

Local time is supported where U=V, so either mass can appear in the
integrand. The two half-local-time terms from min and max add to one.
Their quadratic-variation densities are respectively min(U,V) and
max(U,V), so the two backward-Feller drifts cancel separately.

Set theta=lambda/T. Then T*b_s<=lambda, and at every fixed finite s,
T*b_s tends to 2lambda/(lambda+2), while b_s U_s tends to zero.
Dominated convergence against the finite measure E dL on [0,infinity)
therefore gives

    lim T E|exp(-lambda U_T/T)-exp(-lambda V_T/T)|
      = (2lambda/(lambda+2))*ell.

The marginal Laplace formula gives a uniform approximation bound

    |T*delta_T - T E|exp(-lambda U_T/T)-exp(-lambda V_T/T)||
       <= 8m/(lambda+2).

Letting lambda tend to infinity AFTER the T limit proves

    lim_(T->infinity) T*delta_T = 2*ell = 2 lim E|U_t-V_t|.

This is an exact coefficient, beyond the prior liminf criterion. It
does not prove ell=0 for actual same-noise spatial pairs. Directly
applying dominated convergence to the singular theta=infinity kernel
would be unjustified; the finite-lambda approximation avoids it.

## 5. Proof saved and adversarial audit

Saved PROOF.md with a self-contained derivation from the same marginal
mass input used by both predecessors. The joint martingale, covariance,
conditional Laplace, min/max decomposition, finite-measure dominated
convergence and uniform approximation steps are written out.

Checks independent of the main derivation:

- Conditional Jensen gives liminf T*delta_T >= 2 E|D_t| at every
  fixed t, and then >=2*ell. Its domination is 4|D_t| for T>=2t.
  This independently verifies the sign and leading factor.
- Tanaka on the difference of the two Laplace martingales gives
  the same local-time weight b*exp(-b*U), checking that the two
  min/max half terms add to one, rather than one half or two.
- Independent Feller masses give delta_T=2p(1-p), tail coefficient
  4m, and ell=2m from E min <=m*P(V_t>0). The partially common
  decomposition U=X+Y, V=X+Z gives coefficient 4b and ell=2b.
  These are scalar consistency examples, not SPDE counterexamples.
- The error constant is checked directly from
  2T[exp(-(2m/T)*lambda/(lambda+2))-exp(-2m/T)]
  <=8m/(lambda+2), using the integral of exp(-r) over the exact
  interval of length 4m/[T*(lambda+2)].

What did not work: direct domination at the infinite Laplace parameter
fails near s=T. No uniform bound on 2T/(T-s) follows from integrability
of the local-time measure. It must be replaced by the finite-lambda
kernel, bounded by lambda, before the large-T limit. The order of
limits is essential to the proof as given. No uniform integrability
of D, optional stopping at infinity, or common scalar Brownian driver
has been assumed.

## 6. Reproducible script check

Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
```

Output (exit code 0, under one second):

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1; inherited nice= 20
Backward drift, kernel bound, Tanaka factor, error constant: 27 exact cases
Direct square-root discrepancy versus covariance expansion: 81 exact cases
Uniform extinction-approximation bound: 27 numerical cases
Scalar a=1, b=0: T*delta=0.000000000, 0.000000000, 0.000000000; target=0
Scalar a=0, b=1: T*delta=3.881846831, 3.998800187, 3.999988000; target=4
Scalar a=2, b=0.5: T*delta=1.892978183, 1.998900303, 1.999989000; target=2
Finite lambda=0.5: scalar bounds [0.399999240, 0.399999640], target=0.400000000
Finite lambda=2: scalar bounds [0.999996750, 0.999997750], target=1.000000000
Finite lambda=10: scalar bounds [1.666658750, 1.666660417], target=1.666666667
Documents: balanced delimiters, unique labels 1..23, partial verdict
All checks passed; analytic SPDE conclusions depend on PROOF.md, not these checks.
```

The nice wrapper tries to raise inherited nice 20 to nice 15 and warns;
the process remains at nice 20, below the requested priority. No heavy
run, third-party numerical library, parallel thread or simulation is used.
The script's largest exact loop has 81 tiny rational cases.

Expanded the independent local-time change-of-variables check into a
product-formula argument: N=-H D with smooth positive H. Comparing
Tanaka for HD with the product formula for H|D| gives L(N)=integral H dL(D).
At D=0, H=b*exp(-b*U), reproducing exactly the coefficient in (18).
This is a proof clarification, not a new numerical change.

## 7. Final readback and handoff

Read PROOF.md and REPORT.md back in full with
`OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md REPORT.md`.
Checked the support of dL, the tie-selection convention, square
integrability of both min/max martingale terms, finiteness of the
random local-time measure, the order of limits, m=0, and the
countable-horizon upgrade to indistinguishability. No gap found in
the stated partial result. The scalar examples are expressly not
admissible density-SPDE counterexamples.

Artifacts: PROOF.md, REPORT.md, LOG.md and audit.py. No external
solution is claimed and SOLVED_ELSEWHERE.md is not created. The
next worker should address the spatial mechanism that might force
ell=0, rather than redoing the now exact tail coefficient calculation.

Task completed for this session: “take the NEXT checkable step on this
problem, building on that work.” — 15 November 2026, 06:39 Asia/Tbilisi
session start.
