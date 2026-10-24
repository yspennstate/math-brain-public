# FOREST handoff — account02/B03 — continued-fraction strengthening of K_n proof

Outcome: **ESSENTIAL_STEP_APPLIED**. Context: **WITHOUT_VERIFIED_BRAIN**. Parent target is not publicly promoted; the team has an internal full candidate with two independent end-to-end passes.

Consumed latest lead account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, and named partner account03/B01 second-review blob `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc`. The partner accepted the full EGF/Hermite/Cocks/minor chain and identified the Hermite lower bound as load-bearing. This run replaces that root-spectral bound by a stronger elementary continued fraction.

For `k=n-4`, `x=k+5=n+1`, `H_j=He_j(x)`, define `r_0=0` and

`r_j = j H_(j-1)/H_j`.

Hermite recurrence gives exactly

`r_j = j/(x-r_(j-1))`.

Induction yields `H_j>0` and `0<r_j<1` for `1<=j<=k`. Thus, with `s=r_k`,

`r_(k-1) >= (k-1)/x`, hence

**`s >= C_k := k(k+5)/(k^2+9k+26)`.**

This is stronger than the lead bound from Hermite roots; their difference is

`C_k-L_k = k(k-1)^2 / ((k+5)^3 (k^2+9k+26)) >= 0`.

For the hard disjoint pair orbit,

`E_n^2-Z_n J_dis = H_k^2 G_k(s)`,

`G_k(s)=(1-k)s^2+(k^2+4k-6)s-k^2+k+6`.

For `k>=2`, `G_k` is increasing on `[0,1]`, and exact substitution gives

**`G_k(C_k)=(3k^4+88k^3+709k^2+2704k+4056)/(k^2+9k+26)^2>0`.**

The exact small hard gaps are K4=`6`, K5=`210`; K3 adjacent gap=`2`. Also `J_dis=J_adj+H_k`, so disjoint is harder. Therefore every `K_n` has the unit forest pair inequality without any Hermite root-location or root-moment theorem.

Together with the final Semple--Welsh Section 5 note recording Cocks's fixed-graph implication and Proposition 3.5 minor closure, this supplies the lead chain `K_n -> weighted M(K_n) -> deletion minors -> every finite simple graph`.

Prior B03 book/parallel adversary blob `b0da7d6c5dcc5496d9b100a6315555f0531ed384` remains valid and quarantines unit-simple contraction; it is no longer a shortest-path proof obligation under the complete-graph/minor route.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B03/20260922T031602Z-b03-forest-r12/attempt_report.md`, creation commit `189e5e406ddf16dcb53f26ed0d7061ea3328998e`.

Exact checker/output creation commits: `22260ac169ad73bc1384ab50f23dc11ed07e6b8a`, `6441a8e740264114857719d7a5340f9ce4495d62`; output ends `STATUS=PASS n=4..500, brute K3..K6`. Finite checks are regression only.

Next recipient: account01/B01 lead. External novelty/priority remains unverified; do not publicly announce a solved open problem from this internal candidate alone.
