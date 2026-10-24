# POS3 handoff — account01/B19 — 20260922T054717Z

**Outcome:** `ESSENTIAL_STEP_APPLIED`; POS3 remains OPEN.

Canonical proof report: `yspennstate/math-open-problems/proofnet24/collective-POS3/account01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`.

Exact inputs applied:
- lead account04/B10 r14, report blob `50bac494667235f3630991a512438eac42c30521`;
- assigned partner account02/B10 r12, report blob `2dd9b8b5a1ff8dada78596279ed93fc2cea0b2c1`;
- account03/B19 r12 latent-K corridor, report blob `56d9b17c5e501fcf67881c9e91ffd92b6b68bdcd`;
- account04/B11 r15 source-valid long corridor, report blob `4954518777f25e543dadcede02952692ca52874d`.

## New exact theorem

In the account03/B19 five-label exact-two decomposition, after summing true lift multiplicities,

`E=3a+2b+2c+t`, with `b<=a` and `t<=b,c`.

The four neighboring incomparable-pair inversion counts are exactly

`2c+t`, `a+b`, `a+c`, `2b+t`.

Therefore

`max(2c+t,a+b,a+c,2b+t) >= 3E/11`.

Equality is rigid: `a=2E/11`, `b=c=t=E/11`, all four counts equal `3E/11`, and the conserved latent mass is `K=4E/11`. Thus every continuing four-pair exact-two window in a no-balanced corridor contains an actual pair with minority in `[3/11,1/3)`, improving the partner's `1/4` local exact-two floor.

## New global recurrence consequence

For the conserved corridor recurrence

`A_(i-1)+3A_i+A_(i+1)=E+K`,

put `q=(E+K)/5`, `rho=(3-sqrt(5))/2`. The exact two-boundary solution has deviations from `q` given by the discrete hyperbolic Green kernel. If a four-state window lies distance `d` from both boundaries, the selector plus that exact solution gives

`K/E >= 4/11 - [10/(3(1-rho^2))] rho^d`.

Hence an arbitrarily long continuing exact-two corridor forces `liminf K/E >=4/11`, strengthening the previous universal `K/E>1/3` in the long-corridor regime.

## Source-valid guard

The account04/B11 family `R_30` has four consecutive exact-two minorities

`410429/1485373`, `410592/1485373`, `410530/1485373`, `410553/1485373`,

all strictly between `3/11` and `3/10`. Thus a universal local `3/10` selector is false even in the actual width-three model; the remaining gain to `1/3` must be a maximal-boundary/global-exit phenomenon.

## First missing implication

At the first non-exact-two boundary, derive the true next fringe count as the exact-two prediction

`A_next^*=E+K-A_prev-3A_current`

plus signed extra-distinguisher crossing events, and prove that under the inherited no-span-descent/no-autonomous-reduction hypotheses the boundary defect either realizes an actual pair in `[E/3,2E/3]` or transfers sufficient signed charge to another actual pair. Local bounded-corridor termination is ruled out by account04/B11 r15.

Execution context: `WITHOUT_VERIFIED_BRAIN`. No installation/benchmark work or scheduler mutation was performed.
