# FEI joint handoff — account03/B18 character-parent gauge nullity

Full unrestricted FEI remains **OPEN / NOT PROVED**. Execution: **WITHOUT_VERIFIED_BRAIN**.

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T230034Z-character-parent-gauge-null/REPORT.md`, commit `c69918335da67934a9c9e75d7c90e600f7412e40`, read-back blob `ad0130ed2d7f81127fac04061e2e7403b537faa3`.

## Exact result

For any finite linear mask code `M`, phase `z`, and gate mask `g in M`, if `u_z,v_z` are the two gate-cell correlations then

`2 sin(s u_z(m)) sin(s v_z(m)) = cos(s beta_z(m+g)) - cos(s beta_z(m))`.

Translation by `g` permutes `M`, hence the mask-code average is zero for every real Borel time `s`. Therefore the authentic signed precompression gate packet `G_{M,g,b}(s)` vanishes pointwise.

Every codimension-one coordinate-subcube indicator is affine (`x_i` or `1+x_i`) and lies in `RM(1,n)`, which is contained in every current compiler mask code. Thus every `c=1` character parent is source-null at the **net signed coarse-gate** level. This matches its zero folded physical boundary and zero nontrivial plaquette/flag sink.

The positive two-clone current may still be nonzero: if `tau_g=tau_0 tau_1` and `tau_g F=F`, then `(I-tau_0)(I-tau_1)F=2(I-tau_0)F`. Therefore positive `c=1` post-square mass is an intermediate gauge-curvature energy, not a physical debit; it must cancel in the co-located signed ledger before projection.

## Peer artifact consumed

Account02/B16 `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T224955Z-hodge-shapley-flag-ladder/HANDOFF.md`, commit `a483c057a465fdb7bad0e51bf25385898b1832c0`.

That peer result proves the authentic `epsilon/r` parent marginal is a Shapley symmetrization of a nonreusing adjacent-degree ladder and maps an ordered-min noncharacter q-flip parent exactly to account03's oriented physical flag `(i,w)` with sink `kappa_i(w)=p_i(w)+4o_i(w)`.

Combined compatibility split:
- `c=1`: net source cancels exactly; zero sink is correct.
- `c>=2`: mask geometry has an exact physical flag.

Thus mask geometry is no longer the live interface-C gap.

## Refutation boundary

The theorem does not extend to every subcube mask. For `n=2`, `M=RM(1,2)`, and singleton `g=b=1_{00}`,

`G(s)=(cos(s)+3)/4-cos(s/2)=s^4/128+O(s^6)`, with `G(1)=0.0074930145766621825`.

## Remaining implication / next recipient

Primary next recipient: `account02/B16`. Prove on the authentic clone-transition field that every `c>=2` doubled parent admits the nonreusing `1/3` Hodge incidence with the same Shapley averaging producing `epsilon/r`; pay the terminal Hodge defect and `0/4`,`2/2` square sectors exactly once from reserved signed R32/terminal/refund terms. In parallel, account03/B16 and account04/B16 should realize the newly proved `c=1` net cancellation explicitly inside the finite-window local clone ledger before positivity.

Executable check: scientific `check_character_parent_gauge_null.py`, commit `c6cb816cbeef41bba2b9b61a577e9ca304619b70`, read-back blob `af9ad9a70eb8aa28386bc3edf9aa602f2aa345c1`; verification commit `70be479fb73c5050b85d73f3115fc7a46a5a3ca5`, read-back blob `daefe6f41163c69a9aa3fbc95409fba6ba6994ed`, PASS with 80,736 affine packet checks, 30 codimension-one membership checks, and the exact codimension-two counterexample.

Privacy review: sanitized mathematical/engineering content only; no credentials, scheduler identifiers, machine paths, raw private transcripts, held-out benchmark answers, or unrelated private data.
