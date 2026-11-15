# T423 session log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, 03:51 Asia/Tbilisi (14 November 23:51 UTC).

## 1. Startup and bounded literature check

Read the preceding REPORT.md, LOG.md and the complete PROOF.md in
`~/codex_op_1114/briefs/T423`. The file listing contains
no research scripts; only the analytic proof and runtime files. Nothing in
that directory was edited. Read the local brain startup and memory index
and the compute-state file. No global recall/checklist/mesh commands are
run because they write outside this folder, forbidden by this task.
No git or subagents are used.

Commands used `OMP_NUM_THREADS=1 nice -n 15` throughout. The wrapper warns
`setpriority: Operation not permitted`; independent Python inspection
`os.getpriority(os.PRIO_PROCESS,0)` reports **20**, already a lower priority
than requested. Compute state is warn/owner_away_open, CPU saturated;
only small reads and analytic work are needed.

Web-tool queries:

- `"super-Brownian" "pathwise uniqueness" "2026"`
- `"stochastic heat equation" "square root" "pathwise uniqueness" 2025 2026`
- `"super-Brownian" "pathwise" "uniqueness" November 2026 density`
- `"2607.22220"`

Primary pages actually opened:

- Hao Wang, https://arxiv.org/abs/1612.06055: still withdrawn because of
  a gap in the main proof.
- Leonid Mytnik and Johanna Weinberger,
  https://arxiv.org/abs/2509.10984 (v3, 12 August 2026): weak uniqueness.
- Yi Han, https://arxiv.org/abs/2611.07310 (5 November 2026): weak
  uniqueness on the torus with uniformly nondegenerate diffusion.
- Jie Xiong and Wen Xu, https://arxiv.org/abs/2607.22220 (v2, 6 September
  2026): cyclic catalytic finite-dimensional SDEs.
- Yu-Ting Chen, https://arxiv.org/abs/1308.5141: nonuniqueness with
  immigration, as in the preceding report.

No verified resolution of the stated density SPDE was found. These pages
do not supply it. The literature check ended within five minutes of
session start; no SOLVED_ELSEWHERE.md is warranted. This is limited search
coverage, not a proof that no later result exists.

## 2. Independent check of the earlier main result

Write h=sqrt(u)-sqrt(v). Integrating the *mild* difference at a fixed
terminal time, rather than repeating the weak-form cutoff calculation,
gives D_T=integral h dW: the heat kernel integrates to one, and
E integral h^2 <= 2mT makes stochastic Fubini legitimate (a detailed
Hilbert-space argument is included in PROOF.md). Itô isometry then gives
E D_T^2=E integral A. A nonnegative zero integral and joint continuity
give equality of the fields on the full interval. The earlier main
claim **holds**. A second check expands the two marginal variances and
their cross covariance and gives the same identity.

The occupation normalization also holds: the average over a in
[-epsilon,epsilon] of |z-a|-|a| equals the preceding piecewise quadratic
F_epsilon(z). Applying Tanaka at level a and integrating gives exactly
Q_epsilon=E F_epsilon(D_T), hence error in [0,epsilon/2]. This verifies
the main finite-width claim by averaging Tanaka, independently of the
preceding generalized-Itô argument.

## 3. Choice recorded before extending the proof

Prove that equality almost surely of the single terminal extinction
indicator 1_{U_T=0}=1_{V_T=0} is equivalent to equality of the whole pair
on [0,T]. Also derive its exact white-noise energy formula and a stopped
quantitative estimate. This is one extension: replace the preceding
real-valued terminal observation by a binary observation.

Reason: the conditional extinction probability at time T is
exp(-2 U_t/(T-t)), injective in current mass for t<T. Its difference is
a bounded martingale in the actual joint filtration. The crucial audit
is to derive this conditional law there, rather than silently use a
marginal Markov property in an enlarged filtration. Endpoint convergence
and the possible event of extinction exactly at T must also be proved.
No extinction synchrony for actual pairs is assumed or claimed.

## 4. Conditional-law calculation and first audit

For fixed lambda and terminal T, apply Itô to exp(-q_s U_s), where
q_s=lambda/(1+(T-s)lambda/2). The time derivative and bracket drift
cancel. The stochastic integral is in the actual joint filtration, so
the resulting conditional Laplace transform is valid there. Letting
lambda increase to infinity gives
P(U_T=0 | F_t)=exp(-2 U_t/(T-t)). No enlargement-of-filtration Markov
assumption is required. The same calculation works for V.

The difference of these two bounded martingales has terminal value
1_{U_T=0}-1_{V_T=0}. Its squared terminal expectation is exactly the
probability delta_T that the extinction indicators disagree. Its noise
coefficient is -q_s[p_s(U_s)sqrt(u_s)-p_s(V_s)sqrt(v_s)], q_s=2/(T-s).
Isometry gives the new energy identity. Equality of terminal indicators
forces equality of conditional probabilities and hence current masses;
the preceding reduction then gives equality of the fields up to T.

Endpoint issue resolved independently of any assumption about an atom
at extinction time T: U_T is the limit of U_t as t increases to T, hence
its extinction indicator belongs to F_{T-}. Conditional-expectation
martingale convergence gives the terminal limit in L2. Singular q_s
causes no unproved integrability: apply isometry up to r<T and use
bounded-martingale convergence and monotone convergence of the energy.

Additional consequence within this same extension: absence of immigration
makes zero absorbing. For 0<t<T, on the event E_t that exactly one mass
is zero, the only future disagreement is survival of the other mass.
Thus delta_T >= E[1_{E_t}(1-exp(-2(U_t+V_t)/(T-t)))]. Multiplying by T
and dominated convergence gives liminf T*delta_T >=
2 E[(U_t+V_t)1_{E_t}]. Every nontrivial pair has delta_t>0 for some t,
so this lower bound is strictly positive. Universally delta_T <=
2(1-exp(-2m/T)) <= 4m/T. Consequently uniqueness of a given pair for
all times is equivalent to liminf_{T->infinity} T*delta_T=0. The
required improvement over the automatic O(1/T) bound is still unproved.

## 5. Proof saved and adversarial checks

Saved PROOF.md with all derivations, including an independent mild-form
proof of the earlier result. Read it back in full with
`OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md`.

The new proof supplies:

- Exact equivalence between field equality through T and almost-sure
  equality of the binary terminal extinction indicators.
- The exact energy identity for the probability delta_T of terminal
  extinction disagreement.
- For sigma=t wedge tau_K, the stopped estimate
  E integral_0^sigma A <= (T^2/4) exp(4K/(T-t))*delta_T.
- The natural-scale criterion liminf T*delta_T=0 for equality of a
  fixed pair for all times, and a strictly positive lower bound for
  nontrivial pairs.

Adversarial checks written out in PROOF.md:

1. The finite-lambda conditional Laplace calculation is in the actual
   joint filtration. Weak uniqueness alone is not used to enlarge a
   filtration or identify Brownian drivers.
2. Conditional-expectation convergence to the terminal indicators holds
   because continuous mass paths make them F_{T-}-measurable. The
   singular coefficient 2/(T-s) is handled only after finite-r isometry.
3. Direct isometry and an independent product/covariance expansion give
   the same extinction-disagreement energy and factor 2 in the cross term.
4. The inverse-function derivative checks the squared stopped constant
   T^2/4 and exponent 4K/(T-t). K must exceed initial mass; no uniform
   bound is asserted when K increases to infinity.
5. The large-time lower bound is checked by both the exponential
   difference quotient and its exact integral representation. The
   integrable dominator is 4*S_t for T>=2t. Both give factor 2.
6. The Bernoulli union bounds and a separate product expansion give the
   same upper bound 2 min(p,1-p), hence 4m/T.
7. Zero initial mass, mass-cap hitting, endpoint continuity, equality
   as a global almost-sure property, and countable integer horizons are
   covered. No unbounded stopping-time identity is used.

A tempting shortcut fails. The weighted noise coefficient in the new
energy is not uniformly coercive in A: u=f, v=4f, integral f=1, and
q=log(2)/3 give weighted coefficient zero but A=1. This is exact,
since exp(3q)=2. Equal-mass disjoint profiles also retain positive
weighted energy. These are deterministic profile tests, not SPDE
counterexamples. Thus the new identity has not secretly proved the
missing synchrony estimate.

## 6. Reproducible audit and final handoff

Saved REPORT.md and the standard-library audit.py. Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
```

Output (exit code 0, under one second; before this log append):

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1; inherited nice= 20
Tanaka average and epsilon/2 error: 183 exact rational cases
Weighted energy versus covariance expansion: 162 exact cases
Bernoulli disagreement bound: 202 exact endpoint cases
Noncoercivity test: weighted coefficient=0; A=1
Tail check: T=100, T*(1-exp(-2S/(T-t)))=4.0398431423
Tail check: T=10000, T*(1-exp(-2S/(T-t)))=4.0003999866
Tail check: T=1e+06, T*(1-exp(-2S/(T-t)))=4.0000040000
Tail normalization target: 2S=4
Document checks: balanced math delimiters; labels 1..21; partial verdict
PROOF.md: 464 lines, 15171 bytes
REPORT.md: 108 lines, 4931 bytes
LOG.md: 164 lines, 8581 bytes
audit.py: 85 lines, 3319 bytes
```

The mathematical result is analytic; this script checks algebra and
normalizations and does not verify an SPDE uniqueness theorem. Its
largest loops have only hundreds of tiny rational calculations, and
it reads less than 40 KB of documents. No substantial memory, parallel
work, or numerical simulation is involved.

Read back REPORT.md in full and listed this folder. The verdict is
PARTIAL. The new checked piece is the binary extinction reduction,
its exact weighted energy, the stopped estimate, and the inverse-time
disagreement criterion. The general synchrony estimate remains open.
Next concrete target: prove delta_{T_j}=o(1/T_j) on a deterministic
sequence tending to infinity using properties of actual same-noise
spatial solutions, or identify a useful quantitative estimate toward
that condition. No claim that the reduction is new in the literature.

Task completed for this session: “take the NEXT checkable step on this
problem, building on that work.” — 15 November 2026, 03:51 Asia/Tbilisi.
