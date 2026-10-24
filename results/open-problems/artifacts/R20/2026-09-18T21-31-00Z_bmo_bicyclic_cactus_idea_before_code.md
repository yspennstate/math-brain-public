# R20 idea before code — BMO Conjecture 2.6, bicyclic cactus route

Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

This note is intentionally written before any checker for this run.

## Target of this run

Continue the exclusive R20 Bensmail–Marcille–Orenga Conjecture 2.6 target, not the retired I0100 Paley target and not the handed-off KNSV target. The fixed all-graphs metric remains `n_all=8`; the research goal here is structural progress toward the source-raised cactus problem `P^l(G)<=2`.

Use new Section-B moves #6 (deform from solved pseudoforests), #12 (find the conserved obstruction), and #30 (solve exactly the next scale: two-cycle cacti).

## New route

Write every edge label modulo 3 as

`w_uv = 1 + rho(u) + rho(v)`.

Then `sigma(v)` modulo 3 is simply the sum of incident `w` labels. A strong modulo-3 proper scheme is one in which the endpoint sums are different modulo 3 on every non-pendant edge; choosing push representatives in `{0,1,2}` then gives an integer proper pushing scheme, while a pendant edge is automatically proper because its nonleaf endpoint has at least one additional positive edge label.

Three interfaces should make the two-cycle cactus tractable.

1. **Tree transparency.** If a core already has a strong modulo-3 proper scheme, any tree attached at a core vertex can be added without changing the core vertex sum modulo 3. Put residue 0 on every edge from the core into the tree; then prescribe proper residues on all new nonleaf vertices and determine the remaining child-edge residues recursively. Because a tree has no cycle, arbitrary edge residues are realizable by unique child push residues once the root push is fixed.

2. **Leaf-cycle interface.** For a cycle `C_l = v_0 ... v_{l-1} v_0` attached at root `v_0`, keep the root push residue `r` fixed. Require the two incident cycle-edge residues to sum to 0 so the old root sum is preserved. If `l>=4`, I expect a cycle word `w_0,...,w_{l-1}` for every old root color `s` and every `r`, with `w_{i-1} != w_{i+1}` (internal properness), root-neighbor colors avoiding `s`, and the exact closure condition needed for the `w` word to come from push residues. A length-6 insertion should preserve every condition: in each parity subsequence append `t+1,t+2,t`; the endpoint returns to `t`, the added sum is 0 in F3, and consecutive values remain unequal. Hence only lengths 4 through 9 need base words.

   The triangle is exceptional and supplies the conserved syndrome. If its other vertices are `u,v`, then

   `sigma(u)+sigma(v) = 1-r (mod 3)`.

   Properness of the triangle forces `{s,sigma(u),sigma(v)}=F3`, hence necessarily

   `s = r-1 (mod 3)`.

   Conversely that condition is sufficient, and the triangle's total contribution to the root can be any residue. Thus a leaf triangle is not transparent: it forces the root color-minus-push syndrome `s-r=-1`.

3. **Two-triangle core.** If two triangles are joined by a path `p_0,...,p_k`, set path push residues `rho(p_i)=i mod 3`. Every internal path sum is then `rho(p_i)-1`, so adjacent path sums differ. At each endpoint the triangle condition asks for exactly the same target color `rho(p_i)-1`, and its arbitrary root contribution can be chosen to make that target hold. If the triangles share a cutvertex (`k=0`), choose any root push `r`, target color `r-1`, and split that target as the two arbitrary triangle contributions.

These facts would prove the following next-scale theorem once the nontriangle leaf-cycle interface is checked and written carefully:

**Candidate theorem (SELF_CHECK_ONLY until validated): every connected cactus with exactly two cycles has `P^l(G)<=2`.**

Proof architecture: strip attached trees by tree transparency. If at least one cycle has length at least 4, regard it as a leaf cycle attached to the remaining unicyclic core, use the previous run's strong modulo-3 unicyclic scheme on that core, and attach the nontriangle cycle transparently. If both cycles are triangles, use the explicit path construction above. Restore all tree branches transparently.

The fixed metric `n_all` will not move from 8 merely because this proves an infinite subclass. Validation should test only the new finite base interfaces and the resulting theorem on an independent finite cactus census; it is not the proof.
