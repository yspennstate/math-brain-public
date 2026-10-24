# FOREST handoff — account02/B01 — source-safe 2-cut theta-grid compression

Outcome: `ESSENTIAL_STEP_APPLIED`; parent FOREST remains open. Context: `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B01/B01-20260922T055947Z-forest-r16/report.md`, report blob `0c1f336a3ef05168e3e36dd413a6549f52080f77`.

## Correction applied

Account01/B02 `20260922T054825Z` (handoff blob `fb4265dc413059fc93e8dada0ef0ba90a008d947`) refutes the inherited rank-degree complete-log-concavity argument already on `K_3`. I retract that proof from my r15. The useful rank-width conclusion is re-proved here without CLC.

## Same-side 2-cut state

For an edge-minimal loopless-multigraph counterexample, take a proper 2-separation with both marks in side `B` and a non-singleton outside `O`. Let `D,C` be outside forest counts with terminals disconnected/connected, `lambda=C/D`, `q=lambda/(1+lambda)`, and

`Delta_G(e,f)=D^2 R(lambda)`, `R(s)=d0+b s+d1 s^2`.

Minimality gives `R(0),R(1),d1>=0`. If `J=(alpha,beta)` is the negative interval and `ell=alpha/(1+alpha)`, `u=beta/(1+beta)`, `delta=u-ell`, then for every outside edge `h` the source-safe deletion/contraction straddling is

`q0(h) <= ell < q < u <= q1(h)`.

Writing `p_h=P(h in F)` gives the new pointwise consequences

`Cov(X_h,Y) >= kappa := ((q-ell)(u-q))/(u-ell)`,

`(q-ell)/(1-ell) <= p_h <= q/u`, and `p_h<=1/2`.

## Rank/edge budgets, now source-safe

Let `K=sum_h X_h`, `S=sum_h p_h(1-p_h)`, and `r=rank(O)`. Minimality makes every pair of physical outside edges nonpositively correlated, so `Var K<=S`; straddling gives `Cov(K,Y)>=delta S`. Cauchy therefore gives `delta^2 S<=q(1-q)`. Deletion injectivity gives `S>=E K/2`; elementary independent-set extension counting gives `E K>=r/2`. Hence

`r delta^2 <= 4 q(1-q)`.

No CLC is used. Also

`4 |E(O)| kappa^2 <= q(1-q)`,

`|E(O)|(q-ell)/(1-ell) <= r`, and `r/2 <= |E(O)| q/u`.

## Exact theta-grid exclusion — named partner applied

Apply account03/B02 `20260922T051758Z` (blob `c165e7c6b6ca991a97c5ed3d646611f91cf96adc`). Its unit gadget `Q(k,a)` consists of `k` internally disjoint length-`a` paths and has

`D_Q=(2^a-1)^k`, `C_Q=k(2^a-1)^(k-1)`, response `s=k/(2^a-1)`.

If `m=|E(O)|` and `ak<m`, replacing `O` by `Q(k,a)` creates a strictly smaller loopless **unit** multigraph, so minimality and exact gluing force

`R(k/(2^a-1))>=0`.

Thus the forbidden interval satisfies

`J intersect {k/(2^a-1): a,k>=1, ak<m} = emptyset`.

Also every `m`-edge outside obeys `lambda<=m` by deleting one edge of the unique terminal path from a connected forest. The strict cost is sharp: `Q(k,a)` itself has cost `ak`, and `m` parallel terminal edges attain response `m`.

## First unpaid step

`THETA-HIT / source-realizability`: prove that no genuine unit outside `O` can simultaneously satisfy the all-edge straddling inequalities, the rank/edge budgets above, and avoidance of every cheaper theta response; equivalently force a cheaper theta point into `J`, or build an actual graph-side/outside counterexample to this mechanism.

This is narrower than arbitrary weighted Rayleigh closure and keeps the actual boundary distribution. The separate minimality-conditioned triangle-contraction/STAR-2 debt remains open, so this is not a full-proof candidate.

Exact checker blob `a0d038942fb8b9814602d7242f11c32777b91b00`; output blob `59f2cc66a73db25c02573743dddef1020b72ef76`, terminating `STATUS=PASS` after 15 exact theta enumerations and 7,539 exact-rational mixture checks. Finite checks are auxiliary only.
