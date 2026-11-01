# P0457 idea note — adversarial disconnected-shell correction

Date: 2026-09-18 UTC
Track: NM13-04
Source/claim: P0457 / `operations/claims/P0457.md`

## Idea before code

The newest all-s theorem has a quantifier defect in its exact-shell clause. It says that for **every nonedge** `uv`, the shell grown from `N_G(u)` meets `N_G(v)` within `s` steps and hence `d_G(u,v)=2+j_*`. But the proof invokes the connected-diameter lemma. If `u,v` lie in different connected components, no such shell intersection exists and their extended graph distance is infinite.

A source-valid exact witness already occurs at `n=4, s=2, k=n-1-s=1`. Assign distinct integer edge weights

- `w(1,2)=1`, `w(3,4)=2`;
- `w(1,3)=10`, `w(1,4)=11`, `w(2,3)=12`, `w(2,4)=13`.

Each vertex's unique lowest-weight incident edge is its partner, so `LK(4,1)` is exactly two disjoint edges `{1,2}` and `{3,4}`. For the nonedge `(1,3)`, `N(1)={2}` and `N(3)={4}`. Shell expansion from `{2}` remains inside component `{1,2}` forever, so it never meets `{4}`; in particular no `j_* in {0,1,2}` exists.

This refutes only the universal wording of item 5 in `P0457-ALL-S-CLASS`, not the complement-degeneracy theorem and not the near-logarithmic random-diameter theorem.

## Repair to prove

Strengthen the component statement instead of assuming global connectivity:

1. `\bar G` is `s`-degenerate as already proved.
2. **Every connected component** of `G` has diameter at most `s+2`: take a geodesic inside any component; the same induced-path argument in the induced complement gives `d-2<=s`.
3. If `u,v` are nonadjacent but lie in the same component, then `d_G(u,v)=2+dist_G(N(u),N(v))<=s+2`, so the shell index `j_*<=s` exists and gives the exact finite distance.
4. If `u,v` lie in different components, set `d_G(u,v)=+infinity`; no shell-intersection claim is made.
5. Hence a complete classifier first computes components, then runs at most `s` shell expansions only for same-component nonedges. Under the alternative convention “diameter = maximum finite component diameter”, take the maximum of those finite distances. Under the ordinary connected-graph convention, a disconnected graph has infinite diameter.

Therefore the frozen metric `S_exact=UNBOUNDED` survives the correction: the classifier remains parameter-uniform for every `s`, but its disconnected boundary state must be explicit.

This note is intentionally committed before the exact finite checker.