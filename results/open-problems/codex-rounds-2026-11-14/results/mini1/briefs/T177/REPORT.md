VERDICT: PROVED a finite-window total-variation reduction and a conditional first-order correction

Let q_n=P(X_n>0) and g(k)=(m-1)m^{-k}. The full nonconstant critical
conjecture is not proved here.

For every n with q_n>0 and L>=1, define
delta=max_{0<=j<=L}|q_{n+j}/q_n-1|. The proved estimate is

\[
 d_{\rm TV}(\mathcal L(X_n\mid X_n>0),g)
 \leq \frac{\delta}{m-1}+(1+\delta)m^{-L}
                   +m(1+\delta)^2q_n.
\]

PROOF.md gives a slightly sharper bound with weighted survival differences.
These estimates require no moment or criticality assumption. If q_n->0 and
q_n>0 eventually, conditional convergence to g is equivalent to
q_{n+1}/q_n->1, and also equivalent to convergence of the conditional mass
at 1 to (m-1)/m. This reduces the conditional-law question to one scalar
regularity question.

There is also a first-order result. Under the additional assumptions

\[
 q_n=o(n^{-1}),\qquad q_{n+1}/q_n=1-\beta/n+o(n^{-1}),\quad\beta>0,
\]

the conditional law equals g+h_beta/n+o(1/n) in l1, where

\[
 h_\beta(k)=\beta m^{-k}\{m-(m-1)k\}.
\]

In particular its total-variation distance from g is asymptotic to beta/(mn).
For beta=2 this gives 2/(mn). The ratio expansion is an unproved additional
hypothesis for the critical model; a survival asymptotic alone does not imply
that expansion. No novelty claim relative to all previous work is made.

The literal supplied statement has an omitted deterministic exception:
m=2, X_0=1 almost surely is critical and has X_n=1 forever. PROOF.md
classifies it as the only critical initial law with no atom at zero. This
does not settle the intended nonconstant problem. The nonconstant assumption
is present in the original source.

Validation command, from this directory:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_bounds.py > audit_output.txt 2>&1
```

The final run passed on 24 rational initial laws: 68 one-step identities,
58 independent tuple-enumeration comparisons, 28 critical moment checks,
147 finite-window identities and bounds, and 33 checks of the first-order
constant. It uses exact fractions and includes the infinite geometric tail
analytically. Full data are in exact_checks.csv; the model definitions and
counts are in audit_summary.json. AUDIT.md records the independent derivations
and the assumptions tested.

The initial run failed because Darwin rejected the address-space resource
limit, before doing the calculation. The final script instead guards actual
resident memory and array sizes, and caps CPU time at 180 seconds and wall
time at 240 seconds. The final run took less than a second and used
17,285,120 bytes peak resident memory. The requested nice wrapper reports
that it cannot change priority because the inherited process is already at
nice 20; the script verifies and records that value. No heavier computation
or simulation was needed.

The literature check used the web search tool and ended within ten minutes.
No complete solution was found. The papers actually opened, authors and links
are recorded in LOG.md. In particular the September 2026 paper by Thomas
Duquesne and Zhan Shi, [arXiv:2609.11435](https://arxiv.org/html/2609.11435v1),
still describes the original discrete-to-continuous scaling limit as unproved.
The opened survival theorem requires a stronger exponential moment than the
minimal critical equality. These literature observations are context, not
this session's mathematical result.

Next: prove q_{n+1}/q_n->1 for nonconstant critical initial laws in a useful
integrability class. Together with established decay of q_n, Corollary 2
would give the conditional geometric limit without first establishing the
sharp survival constant. A stronger estimate
q_{n+1}/q_n=1-2/n+o(1/n), together with q_n=o(1/n), would activate the
first-order expansion. Nothing here establishes the universal survival
constant, the critical mean asymptotic, or either of these ratio estimates.

Task: “push this problem forward by one checkable piece” — 2026-11-14,
approximately 21:19 Asia/Tbilisi.
