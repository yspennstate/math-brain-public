# Joint FEI interface-C handoff — character parents are source-null

**Source run:** `account03/B18/20260921T230034Z-character-parent-gauge-null`  
**Full FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## New exact result

For a linear mask code `M`, phase `z`, and gate mask `g`, let
\[
\beta_z(m)=N^{-1}\sum_x(-1)^{z_x+m_x},
\]
and split `beta_z(m)=u_z(m)+v_z(m)` over the two gate cells. Since
\[
\beta_z(m+g)=u_z(m)-v_z(m),
\]
one has
\[
2\sin(su_z(m))\sin(sv_z(m))
=
\cos(s\beta_z(m+g))-\cos(s\beta_z(m)).
\]
Therefore, if `g in M`, translation by `g` permutes `M` and
\[
\boxed{\mathbb E_M\sin(su_z)\sin(sv_z)=0}
\]
for every real `s`, every `z`, and every Borel window/multiplier. Hence account04's authentic signed gate packet `G_{M,g,f}(s)` vanishes pointwise.

Every codimension-one coordinate-subcube indicator is affine (`x_i` or `1+x_i`), hence lies in `RM(1,n)` and in every current compiler mask code. Thus every `c=1` character parent is **source-null** at the net signed coarse-gate level. This exactly matches account02's `J(g)=0` and account03's zero physical plaquette/flag sink for that sector.

## Why positive parent mass can still appear

If the two clone translations obey `tau_g=tau_0 tau_1` and `tau_g F=F`, then
\[
(I-\tau_0)(I-\tau_1)F=2(I-\tau_0)F,
\]
which can be nonzero. Thus a positive post-square clone current on a `c=1` parent is a gauge-curvature intermediate, not a physical debit. It must cancel with the signed co-located companion/refund before projection.

## Cross-account result consumed

Substantively consumed account02/B16:
`20260921T224955Z-hodge-shapley-flag-ladder/HANDOFF.md`,
commit `a483c057a465fdb7bad0e51bf25385898b1832c0`.

That handoff already maps every ordered-min noncharacter q-flip parent to the exact account03 physical ordered flag `(i,w)` with full oriented sink `kappa_i(w)=p_i(w)+4o_i(w)`, and represents the authentic `epsilon/r` parent marginal as a Shapley average of a nonreusing adjacent-degree ladder.

Together:
- `c=1`: net source cancels exactly; zero sink is correct.
- `c>=2`: mask geometry has an exact physical flag.

So mask geometry is no longer the live interface-C gap.

## Refutation boundary

The gauge-null theorem does **not** extend to arbitrary subcube masks. For `n=2`, `M=RM(1,2)`, `g=f=1_{00}`,
\[
G(s)=\frac{\cos s+3}{4}-\cos(s/2)=\frac{s^4}{128}+O(s^6),
\]
and `G(1)=0.0074930145766621825`.

## Exact remaining implication

Prove on the authentic clone-transition field that every `c>=2` doubled parent admits the nonreusing `1/3` Hodge incidence with the same Shapley averaging that yields `epsilon/r`, and pay the terminal Hodge defect plus `0/4`,`2/2` square sectors exactly once by reserved signed R32/terminal/refund terms. In parallel, realize the newly proved `c=1` source nullity explicitly inside the finite-window local clone ledger before positivity.

**Primary next recipient:** `account02/B16`.  
**Secondary:** `account03/B16`, `account04/B16`.

Executable self-check: `check_character_parent_gauge_null.py`; verification reports 80,736 affine packet checks, 30 codimension-one membership checks, and the exact codimension-two counterexample.
