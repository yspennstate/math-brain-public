# FOREST — account03/B01 — exact STAR-2 unitization and scope correction

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## Inputs consumed

Fresh owner controls: `yspennstate/math-research-brain` main `e83003429e1e47ebd24f1d4c2f50b72b4aeeaa06`, owner revision `2026-09-22.2`, collective campaign `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.

Latest complete lead snapshot consumed: account01/B01 handoff blob `4cee205cb7d254caf785692838111988a0b8a155`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. It rejects the old fixed-graph Cocks globalization and identifies a `{1,2}` STAR-2 contraction comparison as the first triangle-conditioning debt.

Named partner result consumed and applied: account04/B02 handoff blob `b7dfefb859db57dc5f48f44ddc0026693ac05414`, commit `8aa0b17b6f043c6e90a669429ba38032b9b54775`. Its K4 witness proves that a residual Hall injection preserving coordinate union and intersection, and even a full-radius transfer-only map, cannot be universal.

Compatible other-account input checked: account04/B01 commit `686787b589421a290feafda74ea9cd77ca42f5ee`, especially its exact two-terminal substitution factorization. The result below gives an exact finite response-2 specialization.

## Theorem 1: an exact simple unit response-2 gadget

Let `Q` have terminals `a,b`, fresh internal vertices `z1,z2,z3`, and edges

`ab`, `a-zi`, `zi-b` for `i=1,2,3`.

For a two-terminal unit graph write `D` for the forest count with terminals disconnected and `C` for the forest count with terminals connected. Each length-two path has three disconnected states and one connecting state; the direct edge has one of each. A forest can use at most one connecting branch. Hence

`D_Q=3^3=27`,

`C_Q=3^3+3*3^2=54`,

and therefore `C_Q/D_Q=2` exactly.

## Theorem 2: exact forest-network substitution

Delete an unmarked edge `h=ab` of a simple base graph `H` and replace it by a two-terminal unit network `N` with fresh internal vertices, disconnect/connect forest sums `(D,C)`, and response `r=C/D`. For every exterior forest, the internal network is either disconnected (macro-edge absent) or connected (macro-edge present). A macro cycle occurs exactly when the union contains a graph cycle. Consequently

`Z_sub = D Z_H|_{y_h=r}`.

For marked edges `e,f` outside the network, the same factor multiplies `Z,Z_e,Z_f,Z_ef`, and therefore

`Delta_sub(e,f)=D^2 Delta_H(e,f)|_{y_h=r}`.

Independent substitutions multiply these factors.

## Corollary: exact finite unitization of every STAR-2 Rayleigh instance

Let `H` be simple with activities in `{1,2}` and all activity-2 edges contained in one star. Fix distinct marked edges `e,f`. Since for

`Z=A+y_eB+y_fC+y_ey_fD`

one has `Delta_H(e,f)=BC-AD`, the Rayleigh difference is independent of the two marked activities. Reset `y_e,y_f` to one.

Let `d` be the number of remaining activity-2 edges. Replace each by a fresh copy of `Q`. The resulting graph `H*` is finite, simple, and unit-weight, and

`boxed: Delta_{H*}(e,f)=27^(2d) Delta_H(e,f).`

Thus a STAR-2 violation gives an ordinary unit simple-graph FOREST violation by an explicit finite construction. Conversely, a unit FOREST instance is STAR-2 with empty doubled star. Therefore the unrestricted universal STAR-2 theorem is exactly equivalent in truth value to the parent FOREST conjecture.

This is a scope correction to the lead debt: in a minimal-counterexample proof, the useful obligation is not unrestricted STAR-2, but a **size-controlled STAR-2 induction statement**. If the contraction has `m=n-1` vertices and `d` unmarked doubled edges, this exact unitization has `m+3d` vertices. When `d=0`, ordinary minimality already settles the contraction; when `d>=1`, the unitized graph has at least `n+2` vertices, so this exact gadget does not itself close the induction.

## Conditional-disconnection scope correction

The split representation from the previous account03/B01 run remains valid: the STAR-2 contraction law is the projection of the uniform forest law on `J=G\g` conditioned on split terminals `u,v` being disconnected. But the unrestricted statement

`Cov_J(1_e,1_f | u not connected to v) <= 0`

for all `J,u,v,e,f` is itself parent-equivalent. For any arbitrary FOREST instance `H`, adjoin two isolated vertices `u,v`; the conditioning event has probability one, so the conditional law is exactly the original uniform forest law on `H`. Thus the lead must exploit the special split geometry and/or the minimal-counterexample hypotheses rather than prove a universal conditional theorem under a new name.

## Named partner applied

The account04/B02 K4 obstruction means the required size-controlled coupling cannot simply be the old union/intersection-preserving or transfer-only residual injection. Combined with the exact unitization above, the viable direct-coupling target is now sharply constrained: it must preserve enough size/order information to invoke minimality while allowing genuine cross-fiber cut/join moves that may alter coordinate union or intersection.

## Exact finite verification

An independent exact enumerator in this run verified:

- `(C_Q,D_Q)=(54,27)`;
- the identities for `Z,Z_e,Z_f,Z_ef` and `Delta` on 3,972 small labelled STAR-2 marked-edge instances based on all simple graphs on 3 or 4 vertices, with up to two unmarked doubled edges: zero failures;
- no simple unit two-terminal graph on at most four total vertices has response exactly 2, while the five-vertex `Q` above does. The last item is a finite diagnostic and is not required by the theorem.

## Next obligation

Parent FOREST remains `OPEN`. The first useful missing implication is now:

`SIZE-CONTROLLED STAR-2`: from pairwise NC of all smaller unit simple graphs, prove pairwise NC for the specific `{1,2}`-star contraction produced by a triangle edge in an edge-minimal counterexample.

Any new injection should allow cross-fiber changes of union/intersection, in accordance with the named partner's K4 Hall obstruction.
