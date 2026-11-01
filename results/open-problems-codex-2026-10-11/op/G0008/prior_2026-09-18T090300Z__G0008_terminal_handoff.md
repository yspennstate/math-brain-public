# R7-06 terminal HARD handoff — G0008 / square-lattice two-point connectivity monotonicity

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested in prompt text, but no authenticated runtime model-family / reasoning-effort telemetry or binding selector is exposed.

Date: 2026-09-18 UTC  
Slot: `R7-06 Hard Conjecture Certificates`  
Native ID: `6aabe827777c8191a43330b4a87d481d`  
Own root: `research7_2026-09-17/R7-06/`  
Canonical target: `G0008`  
Canonical claim: `operations/claims/G0008.md`  
Category: **HARD OUTSIDE**  
Handoff status: **PARTIAL / SOURCE OPEN / ROUTE RETIRED FOR R7-06**

## 1. Outside source and exact endpoint

Alberto M. Campos and Bernardo N. B. de Lima, *The probability of connection between two vertices cannot be monotone with the distance for Bernoulli Percolation on transitive graphs*, arXiv:2601.00291v1 (2026), Abstract/Introduction and Section 3.

For homogeneous Bernoulli bond percolation on the square lattice, put

\[
\tau_n(p)=\mathbb P_p(0\leftrightarrow (0,n)).
\]

The square-lattice source question is whether

\[
\tau_{n+1}(p)\le \tau_n(p)
\]

for every `p in (0,1)` and every `n>=1`. The canonical claim also preserves the source's broader `Z^d` wording as a stronger endpoint; R7-06 did not silently reduce that full scope.

The fresh 2026-09-18 source record still explicitly calls the square-lattice monotonicity question open. A bounded exact-title / author / follow-up search did not recover a later all-`p`, all-`n` resolution. This is negative evidence only, not a novelty certificate. König--Richthammer's layered-graph theorem remains a nearby partial analogue: finite transverse graphs have eventual monotonicity after a width-dependent threshold, not the infinite-width square-lattice `n=1` endpoint.

## 2. Frozen metric at handoff

The admission-frozen metric was

`M_axis := largest N>=1 for which R7-06 has rigorously proved tau_{n+1}(p)<=tau_n(p) simultaneously for every p in (0,1) and every 1<=n<=N.`

Handoff value: **UNKNOWN/UNMEASURED**.

No source-valid all-`p` first-step theorem was proved, so the metric was never honestly promoted to `1`.

The final ordinary recovery run leaves the metric unchanged and advances the ordinary no-movement count from **4 to 5**. The target is nevertheless retired for this slot now because both allowed HARD-target stuck recoveries have already been consumed and the prescribed final recovery has failed to move the frozen source metric. This is not the six-run CLOSABLE retirement rule.

## 3. Cumulative mathematical results worth preserving

### 3.1 Exact first-step punctured-star reduction

Delete the four edges incident to the middle vertex `y=e_1` and record the noncrossing partition of its four neighbours. Under `D_4` symmetry let

\[
\theta_p=(\sigma_p,\alpha_p,\beta_p,\gamma_p,\delta_p,\epsilon_p)
\]

be the six orbit probabilities per specified partition, with orbit sizes `(1,4,2,2,4,1)`. Then

\[
\tau_1(p)-\tau_2(p)=(1-p)F_p(\theta_p),
\]

where

\[
\begin{aligned}
F_p(\theta)={}&p\sigma+2p(3-2p)\alpha+(2p-1)\beta\\
&+2p(1-p)(2-p)\gamma\\
&+(2p^3-7p^2+8p-2)\delta-(1-p)^3\epsilon.
\end{aligned}
\tag{3.1}
\]

Thus the exact first source milestone is the all-parameter inequality `F_p(theta_p)>=0`.

### 3.2 Critical and off-critical partial certificates

R7-06 obtained explicit low- and high-density first-step intervals and an exact critical-point certificate

\[
\boxed{\tau_1(1/2)-\tau_2(1/2)\ge 13/4096>0.}
\]

Continuity gives a nonempty homogeneous interval around `p=1/2`. These remain **PARTIAL**, not the all-`p` first-step result.

### 3.3 Exact one-edge planar dual conservation

For nearest-neighbour detour probability `D(p)` after deleting one edge,

\[
\boxed{D(p)+D(1-p)=1.}
\]

Equivalently, defining

\[
L_\theta(r)=\sigma+2(1+r)\alpha+(1+r)\beta+2r\gamma+(1+3r^2)\delta+r^3\epsilon,
\]

one has

\[
\boxed{L_{\theta_p}(1-p)+L_{\theta_{1-p}}(p)=1.}
\]

A key correction was also established: deleting primal star edges dualizes to **wired/contracted** dual boundary edges, not to a second free punctured-star law. A naive free-law Kreweras identity is invalid.

### 3.4 Full `NC(4)` association + stochastic-order no-go theorem

The final recovery changed category to the full 14-state noncrossing partition lattice `NC(4)`. The actual punctured product-measure law is positively associated on this finite poset, and the monotone coupling in the parameter gives stochastic order `theta_p <=_st theta_q` for `p<q`.

The complete finite-poset association system has exactly **234 up-sets**, hence **27,495** unordered up-set-pair inequalities per law.

At `p=1/3`, keep

\[
\theta^-=
\left(\frac14,0,\frac{19}{108},0,\frac1{27},\frac14\right).
\]

At `q=2/3`, the sparse extremal construction

\[
\theta^+=
\left(\frac14,0,0,0,\frac1{64},\frac{11}{16}\right)
\]

is forced by setting `alpha=beta=gamma=0`, saturating the previously omitted opposite-connection stochastic-order up-set, and imposing exact scalar dual conservation.

An exact rational exhaustive checker proves simultaneously:

- `theta^-` satisfies all 27,495 `NC(4)` association inequalities;
- `theta^+` satisfies all 27,495 `NC(4)` association inequalities;
- `theta^- <=_st theta^+` on all 234 increasing up-sets;
- both satisfy the retained pairwise terminal FKG inequalities, BK inequality and leaf-surgery constraints;
- `L_{theta^-}(2/3)=19/27`, `L_{theta^+}(1/3)=8/27`, so the scalar primal/dual conservation law is exact;
- detour directions are correct: `8/27<1/3` and `19/27>2/3`;
- nevertheless

\[
\boxed{F_{1/3}(\theta^-)=-37/729<0.}
\]

while `F_{2/3}(theta^+)=133/864>0`.

The exact output ends `ALL_EXACT_CHECKS_PASS`.

This is **not** a Bernoulli-percolation counterexample. It is a rigorous no-go result for the proof architecture consisting of boundary normalization + the entire `NC(4)` association cone + full cross-parameter stochastic order + the retained BK/finite-energy inequalities + scalar primal/dual detour conservation.

## 4. Exact remaining blocker

Any successful continuation must use information that distinguishes actual punctured independent-edge percolation laws from arbitrary associated, stochastically ordered `NC(4)` laws.

The present strongest formulation of the missing ingredient is:

> Find a geometry/product-measure realizability constraint on the one-parameter family `theta_p` which is not implied by full boundary positive association and stochastic order, and which is strong enough to force `F_p(theta_p)>=0` for every `p`.

Three concrete forms that remain plausible are:

1. an exact **primal-free / dual-wired annular deletion-contraction relation** at full partition level, rather than the scalar detour identity;
2. **Russo-type derivative constraints** coupling `theta_p` across `p`, using pivotal-edge geometry and not just stochastic order;
3. **witness-sensitive disjoint-occurrence inequalities** retaining which interior edges witness terminal connections, rather than only the induced boundary partition.

Adding more FKG inequalities on the boundary partition alone is exhausted: the final pair already passes all of them.

## 5. Recovery history and why R7-06 must rotate

Ordinary G0008 research reached the prescribed stagnation trigger, followed by:

- STUCK1: `research7_2026-09-17/R7-06/runs/2026-09-18/2026-09-18T055700Z__report.md`;
- recovery run deriving exact one-edge primal/dual conservation and a scalar relaxation obstruction: `.../2026-09-18T073200Z__report.md`;
- STUCK2: `.../2026-09-18T074905Z__report.md`, which corrected the earlier incomplete FKG screen and selected exactly one final recovery action, with methods B1/B19/B24;
- final recovery: full `NC(4)` association/stochastic-order construction above, with **NO MOVEMENT** of `M_axis`.

Both allowed HARD stuck recoveries are now consumed. R7-06 therefore terminates its own attack on G0008 here and must not open a third recovery cycle. The canonical claim file is not edited by this attacking worker; any shared ownership/release reconciliation belongs to the authorized coordinator. R7-06 itself treats the route as retired and will only work a fresh, separately admitted unclaimed shard-5 HARD OUTSIDE source.

## 6. Artifacts to inherit

Final exact checker:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T085600Z__G0008_nc4_association_order_checker.py`

creation commit `51f8894e23241d15deb473681b85823506e7812a`.

Archived exact output:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T085600Z__G0008_nc4_association_order_checker.out`

creation commit `ca1069935bd914256c16a691c8ed8c5e97b2230b`.

Full derivation:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T085900Z__G0008_full_NC4_association_stochastic_order_no_go.md`

creation commit `67f8ddbe3868c0be46d160e01c50c1a5c3d5568e`.

All three were read back at their exact creation commits before this handoff.

## 7. Honest handoff verdict

`G0008`: **PARTIAL / SOURCE OPEN / M_axis UNKNOWN_UNMEASURED / R7-06 ROUTE RETIRED AFTER TWO STUCK RECOVERIES**.

No source-level proof or certified refutation exists here. No independent closure audits are requested because there is no closure claim.
