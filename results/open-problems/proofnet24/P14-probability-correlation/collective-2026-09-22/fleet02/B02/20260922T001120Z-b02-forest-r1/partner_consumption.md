# Auxiliary partner-consumption addendum — fleet03/B03

This is an auxiliary provenance/math-routing addendum to the immutable `report.md`, not a second proof report.

After the main report was committed, the named partner artifact became visible on the scientific branch:

- partner: `fleet03/B03`
- run: `20260921T235852Z-fleet03-B03-forest-r11`
- candidate version: `FOREST-OVERLAP-RESPONSE-v2`
- report: `structured_k3m_adversary_report.md`
- report blob: `0e8c55353a1cde3138b667510163e5567772640d`

I read and applied it before finalization.

## Partner result used

For the three-terminal signature `(d,a,b,c,t)`, the partner defines

`eta = (d t-a b-a c-b c)/d^2`

and proves exact additivity under parallel union of edge-disjoint three-terminal pieces. A weighted triangle has `eta=0`, while one three-spoke star has `eta=1/16`, so

`eta(K_{3,m})=m/16`.

Thus compression of an arbitrary three-terminal forest environment to only three pairwise virtual-edge weights is structurally incomplete. The partner also applies the fleet01/B03 overlap identity to same-star spokes in `K_{3,m}` and proves that the q-free target `n00*n11 <= n10*n01` fails by a growing amount even though the true Rayleigh gap remains positive; the overlap/reconnection reservoir `N q` is leading-order and indispensable.

## Application to fleet02/B02's spectral/deletion-contraction route

The main report derived the necessary minimal-counterexample inequality

`2 sum_{e<f in C} L_{h;ef} < |C|-2 sum_{e<f in C} rho_{ef}`

for every nontrivial bad class `C` and every external edge `h`, where the left side consists of deletion/contraction Rayleigh-gap lower bounds and the right side is a complete-log-concavity Gram budget.

The partner result rules out a tempting way to discharge the remaining implication: **one cannot hope to lower-bound the `L_{h;ef}` universally by replacing a three-terminal side with only three effective pairwise weights or by a q-free switching count.** Any separator-local proof of a contradiction to the spectral budget must retain at least the full five-state signature `(d,a,b,c,t)`, equivalently the extra normalized coordinate `eta`, and any overlap switching must retain the reconnection reservoir `q` (or an exactly equivalent state).

So the joined next obligation is sharpened to:

> Derive a lower bound on the deletion/contraction sum `sum L_{h;ef}` in the full five-state / overlap-aware response space, and show that for some external edge it violates the spectral Gram budget; or exhibit a genuine 3-connected response satisfying both.

This is an actual application of the named partner result: it eliminates a lower-dimensional proof architecture for the first missing implication and fixes the state space in which the next inequality must be sought.

No parent closure is claimed. Status remains **ESSENTIAL_STEP_APPLIED / parent OPEN**.
