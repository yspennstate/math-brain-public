# FOREST handoff — two-cut forbidden-interval straddling + rank influence budget v1

Source run: `fleet02/B01/B01-20260922T0529Z-forest-r15`.  
Outcome: `ESSENTIAL_STEP_APPLIED`. Parent FOREST remains open.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

Consumed lead: fleet01/B01 `20260922T050946Z-b01-forest-auto11`, shared blob `4cee205cb7d254caf785692838111988a0b8a155`; used its source-safe rank-homogeneous complete-log-concavity variance budget, not any fixed-graph weighted theorem. Consumed named partner fleet03/B02 `20260922T051758Z`, shared blob `c165e7c6b6ca991a97c5ed3d646611f91cf96adc`; used only the exact proper-2-sum counting identity, not its Cocks-dependent weighted closure. Independent-set CLC source is bound here to Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III*, arXiv `1811.01600`.

For an edge-minimal loopless-multigraph counterexample and a proper 2-cut with both bad marks in bridge `B`, let the actual outside response be `lambda=C/D`. The exact parent gap is

`Delta_G(e,f)=D^2 R(lambda)`,  `R(s)=d0+m s+d1 s^2`,

with `d0>=0`, `d1>=0`, `R(1)>=0` by unit minimality. Let the negative set of `R` on the projective half-line be the open forbidden interval `(alpha,beta)` and suppose `lambda` lies inside it.

**New straddling theorem.** For every physical outside edge `h`, if `q_i=P(u<->v | X_h=i)` then

`q_0 <= alpha/(1+alpha) < beta/(1+beta) <= q_1`,

with `infinity/(1+infinity)=1`. Proof: unit NC of `h` with a new virtual `uv` edge in the smaller augmented outside gives response monotonicity; deletion/contraction of `h` in the whole counterexample are smaller unit instances and therefore cannot have their response inside the same forbidden interval. Thus every outside edge has terminal-connectivity influence at least

`delta = beta/(1+beta)-alpha/(1+alpha) >0`.

Let `r` be outside graphic rank, `K` outside forest size, and `q=lambda/(1+lambda)`. Then

`Cov(K,1[u<->v]) >= delta*r/4`.

Here deletion injection gives every outside edge marginal `p_h<=1/2`, while elementary matroid augmentation counting gives `E K>=r/2`. The rank-homogeneous CLC bound gives `Var(K)<=r/4`. Cauchy therefore yields the exact necessary condition

`boxed: r*delta^2 <= 4*q*(1-q) = 4*lambda/(1+lambda)^2 <= 1`.

Equivalently `r <= 4 lambda /((1+lambda)^2 delta^2) <= 1/delta^2`.

This is strictly stronger than the prior scalar unsafe-orientation condition and retains the **actual** outside boundary distribution. It does not close all same-bridge 2-cuts: the next source-bound step is to lower-bound `delta` from the marked bridge's genuine forest counts strongly enough to contradict the rank budget, or construct an actual graph-side/outside pair satisfying all straddling constraints. Cross-bridge pairs remain closed by the earlier exact unit factorization.

Auxiliary exact regression only: the run's integer zeta checker found no one-new-virtual-edge weighted failure on every labelled simple bridge graph at n=6 or n=7, all marked pairs up to terminal-preserving symmetry (860,160 and 110,100,480 marked graph/pair instances respectively). This finite PASS is not universal closure or novelty evidence.

Canonical scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet02/B01/B01-20260922T0529Z-forest-r15/report.md`.
