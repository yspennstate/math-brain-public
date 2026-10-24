Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-04 / T07 — triangle-seeded cyclic/clique atom response-strip theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short predecessor handoff and substantive move

The preceding NM13-04 run proved strict pairwise negative edge correlation for

\[
K_3\vee\left(mC_3\sqcup\bigsqcup_{\ell=1}^{15}n_\ell P_\ell\right)
\]

with all multiplicities arbitrary. The mechanism was the triangle-seeded five-state response algebra and the insertion lemma: unmarked terminal-symmetric right components collapse to

\[
U=I+uN+vN^2,\qquad N^3=0,\qquad
v=\frac{u^2}{2}-hu,
\]

and all marked local responses are checked uniformly on a continuous interval of `h`.

The latest complementary NM13-08 report then supplied two useful advances without duplicating the triangle seed: it computed the cyclic atom `C4` in the same algebra, and proved the general identity that the exceptional quartic discriminant after the strip substitution is independent of `h`.

This run uses those ideas but makes a distinct triangle-seeded extension. It proves that both **right four-cycles and right four-cliques may be inserted with arbitrary multiplicity**, together with all previously allowed paths and right triangles. The `K4` atom lies below the previous response-strip endpoint, so this is not a formal insertion into the old strip: the proof widens the strip and re-certifies the entire predecessor path sector on that larger continuous region.

Essential dependencies read: `operations/PROGRESS20_2026-09-20.md`; current LIVE20 ownership; `POSTED.md`; the preceding NM13-04 cyclic-triangle report; the newest NM13-08 cyclic-atom report; and the inherited P14 handoff. No historical or peer file was modified.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of two distinct edge indicators under the uniform measure on **all** spanning forests of `G`.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite census is promoted to a general theorem.

**Mechanism before:**

\[
H=mC_3\sqcup\bigsqcup_{\ell=1}^{15}n_\ell P_\ell.
\]

**Mechanism after:**

\[
\boxed{
H=aC_3\sqcup bC_4\sqcup cK_4\sqcup
\bigsqcup_{\ell=1}^{15}n_\ell P_\ell,
\qquad a,b,c,n_1,\ldots,n_{15}\ge0.
}
\]

All eighteen multiplicities are independent and unbounded. The theorem is for `G=K_3 vee H`.

A clean genuinely new subfamily is

\[
G_c=K_3\vee(cK_4),\qquad c\ge2.
\]

It has

\[
|V(G_c)|=3+4c,\qquad |E(G_c)|=3+18c.
\]

Deleting the three left-clique vertices disconnects the right `K4` blocks, while deleting any two vertices leaves a left-clique vertex adjacent to every surviving right vertex; hence `G_c` is exactly 3-connected. It is noncomplete for `c>=2` and contains `K_{3,3}`, so it is outside Erickson's series-parallel theorem.

## 2. Preserved P14 proof state and failed routes

The inherited P14 boundary remains unchanged and is not silently retried.

1. Grimmett–Winkler plus the repository dense-nine completion cover every simple graph through nine vertices in the unit all-forest scope.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with its fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal source counterexample further to a **3-connected** graph.
4. The generic degree-three apex / star-mesh route leaves a mixed three-terminal polarization with no universal sign.
5. Universal positivity of that mixed term is false.
6. The proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex apex graph although the actual Rayleigh gap there remained positive.
7. Naive stability, Lorentzian / complete-log-concavity, and Gårding shortcuts still lack the required hypothesis for arbitrary graphic independence polynomials.

The theorem below enlarges a structured 3-connected positive region; it does not remove the arbitrary 3-connected obstruction.

## 3. Current source scope check

A bounded 20 September 2026 source check continues to separate nearby laws.

- Grimmett–Winkler, `arXiv:math/0302185` / Random Structures & Algorithms 24 (2004), formulate the uniform-**all-forests** edge-correlation conjecture and report numerical verification for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves the stronger positive-weight Rayleigh / sum-of-squares statement for **series-parallel** spanning-forest polynomials.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified uniform spanning-subgraph ensembles of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph all-component uniform-forest law.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), treat high-degree regular random-cluster regimes; at `Q=0` the model is Bernoulli bond percolation conditioned to be connected, not uniform all forests.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict unit p-NC for wheel graphs under the uniform-all-forests law, another infinite 3-connected non-series-parallel family.

A bounded search did not locate the exact triangle-seeded `P_1,...,P_15,C3,C4,K4` theorem below. This is negative evidence only. Novelty remains **UNVERIFIED**.

## 4. Response algebra and insertion principle

Use the five connectivity states of the three left terminals. One fresh right vertex gives

\[
S=4I+N,\qquad N^3=0,\quad N^2\ne0.
\]

Every terminal-symmetric component used here has an exact unmarked transfer

\[
T=A I+B N+C N^2,\qquad A>0.
\]

After normalization,

\[
\widehat T=I+aN+cN^2,
\qquad a=B/A,\quad c=C/A,
\]

and define

\[
\rho(T)=\frac{a^2/2-c}{a}.
\]

For any finite product of normalized unmarked layers,

\[
\prod_j(I+a_jN+c_jN^2)=I+uN+vN^2,
\]

nilpotence gives

\[
u=\sum_j a_j,
\qquad
\frac{u^2}{2}-v
=\sum_j\left(\frac{a_j^2}{2}-c_j\right)
=\sum_j\rho_j a_j.
\]

Hence, when `u>0`,

\[
\boxed{
v=\frac{u^2}{2}-hu,
\qquad
h=\frac{\sum_j\rho_ja_j}{\sum_j a_j}.
}
\]

Thus `h` is a positive weighted average of the component responses. This is the response-strip product/insertion principle: once every local marked response is positive on an interval containing every allowed component's `rho`, the multiplicities disappear from the sign proof.

For a marked pair `e,f`, expose the at most two right components containing the marked edges, together with any marked left-core edge. Every remaining component contributes only the common unmarked `U`. Consequently each of `I,I_e,I_f,I_ef` is affine in `(u,v)`, and every Rayleigh numerator is an exact quadratic

\[
Q_{e,f}(u,v).
\]

The unbounded graph family is therefore reduced to finitely many **local marked response types**, checked on a continuous strip; it is not reduced to finitely many global graph orders.

## 5. New exact atoms and the widened strip

Exact state enumeration gives the already-used right triangle transfer

\[
T_{C_3}=178I+144N+41N^2,
\qquad
\rho_{C_3}=\frac{1535}{12816}.
\]

The right four-cycle, independently found by NM13-08 and reconstructed here under the triangle seed machinery, has

\[
T_{C_4}=1014I+1096N+\frac{1384}{3}N^2,
\qquad
\rho_{C_4}=\frac{2767}{23153}.
\]

The genuinely new clique atom has four right vertices inducing `K4`, with all four adjacent to all three terminals. Exact enumeration of its terminal-state transfer gives

\[
\boxed{
T_{K_4}=1763I+1952N+850N^2,
}
\]

and hence

\[
\boxed{
\rho_{K_4}=\frac{203301}{1720688}.
}
\]

The predecessor path endpoint is

\[
\rho_{15}
=
\frac{13162845795778912063}{109915919585249991540}.
\]

Exact comparison gives the strict ordering

\[
\boxed{
\rho_{K_4}<\rho_{C_4}<\rho_{15}<\rho_{C_3}<\frac18.
}
\]

The checker records positive exact margins

\[
\rho_{C_4}-\rho_{K_4}
=\frac{54115643}{39839089264},
\]

\[
\rho_{15}-\rho_{C_4}
=\frac{622019217282424403459}{2544883286157293054125620},
\]

\[
\rho_{C_3}-\rho_{15}
=\frac{2158737054683334541}{117390202117046990964720},
\qquad
\frac18-\rho_{C_3}=\frac{67}{12816}.
\]

Therefore an arbitrary product of unmarked components selected from

\[
P_1,\ldots,P_{15},C_3,C_4,K_4
\]

lies in the single continuous strip

\[
\boxed{
u\ge0,
\qquad
v=\frac{u^2}{2}-hu,
\qquad
\rho_{K_4}\le h\le\frac18.
}
\]

Because `rho_K4 < rho15`, the old theorem cannot simply be cited: the old path marked responses must be rechecked on this larger strip.

## 6. Re-certification of the entire predecessor path sector

Modulo simultaneous `S3` permutation of the terminals, path reversal, and exchange of equal-length marked path components, there are exactly

\[
11017
\]

local marked-pair representatives involving only the left triangle and paths `P_1,...,P_15`.

Substitute

\[
v=u^2/2-hu,
\qquad h\in[\rho_{K_4},1/8].
\]

For **10,814** representatives, every coefficient of the resulting quartic in `u` is nonnegative on the whole strip by exact degree-two Bernstein coefficients, with strictly positive constant term. The minimum regular constant is `2` and the minimum positive Bernstein coefficient is `1`.

The remaining **203** representatives are precisely the inherited exceptional same-path different-terminal spoke sector. Here I use NM13-08's algebraic discriminant cancellation. For

\[
Q(u,v)=q_{00}+q_{10}u+q_{01}v+q_{20}u^2+q_{11}uv+q_{02}v^2,
\]

write after substitution

\[
Q\!\left(u,u^2/2-hu\right)
=c_4u^4+c_3(h)u^3+c_2(h)u^2+c_1(h)u+c_0.
\]

Then

\[
4c_4c_2-c_3^2
=q_{02}\left(q_{20}+\frac{q_{01}}2\right)-\frac{q_{11}^2}{4},
\]

so it is exactly independent of `h`. For all 203 exceptional path responses the checker verifies positive leading coefficient, nonnegative lower terms on the widened strip, and positive discriminant margin. The minimum exact margin is

\[
\boxed{16476912}.
\]

There are **zero path-sector failures** on the widened `K4` strip.

This re-certification is essential: it is what permits a component whose `rho` lies below the predecessor lower endpoint.

## 7. Exhaustive new cyclic/clique local responses

It remains to check every marked pair involving `C3`, `C4`, or `K4`. The checker classifies local types under simultaneous terminal permutations and each atom's internal automorphism group. All checks are over the full widened interval `[rho_K4,1/8]`, not merely at physical integer multiplicities.

### `C3` sector

The exact orbit counts are

- core / `C3`: 3;
- same `C3`: 6;
- two distinct `C3` copies: 4;
- `C3` / path `P_l`, `1<=l<=15`: 304.

Total: **317** local response polynomials. Every one is Bernstein-positive on the widened strip. Minimum constant: `13052`; minimum positive Bernstein coefficient: `270`.

### `C4` sector

Adding one marked `C4` and allowing prior `C3` atoms gives

- core / `C4`: 3;
- same `C4`: 9;
- two distinct `C4` copies: 4;
- `C4` / path: 304;
- `C4` / `C3`: 5.

Total: **325** local response polynomials. Every one is Bernstein-positive on the widened strip. Minimum constant: `508152`; minimum positive Bernstein coefficient: `3240`.

### `K4` sector

Adding one marked `K4` and allowing prior `C3,C4` atoms gives

- core / `K4`: 3;
- same `K4`: 7;
- two distinct `K4` copies: 4;
- `K4` / path: 304;
- `K4` / `C3`: 5;
- `K4` / `C4`: 5.

Total: **328** local response polynomials. Every one is Bernstein-positive on the widened strip. Minimum constant: `1312038`; minimum positive Bernstein coefficient: `17118`.

There are **zero failures** in all new atom sectors.

## 8. New all-parameter theorem

### Theorem `T07-TRIANGLE-P15-C3-C4-K4-STRIP-22`

Let

\[
H=aC_3\sqcup bC_4\sqcup cK_4\sqcup
\bigsqcup_{\ell=1}^{15} n_\ell P_\ell
\]

for arbitrary nonnegative integers `a,b,c,n_1,...,n_15`. Let

\[
G=K_3\vee H.
\]

Then for every two distinct present edges `e,f` of `G`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Hence the uniform probability measure on **all** spanning forests of every graph in this eighteen-parameter family has strict pairwise negative edge correlation.

### Proof

Every unmarked allowed right component has transfer `A(I+aN+cN^2)` with `A>0` and response parameter in `[rho_K4,1/8]`. By the product identity in Section 4, after removing the positive scalar product of the `A` factors, all unmarked components collapse to

\[
U=I+uN+vN^2,
\qquad
u\ge0,
\qquad
v=u^2/2-hu,
\qquad
h\in[\rho_{K_4},1/8].
\]

Fix distinct edges `e,f`. They touch at most two right components. Expose those components and any marked left-core edge. The four forest counts entering `Delta` are affine in `(u,v)`, so the gap is one of the local quadratic response polynomials classified above.

If both marked edges are in the predecessor triangle/path sector, Section 6 proves strict positivity on the widened strip: 10,814 types are Bernstein-positive and 203 are closed by the exact discriminant identity. If at least one marked edge lies in a cyclic/clique atom, Section 7 exhausts its local symmetry class and proves coefficientwise Bernstein positivity with positive constant term. These cases exhaust all pairs.

Restoring the discarded positive scalar factors multiplies `Delta` by a positive square and cannot change its sign. Therefore `Delta_G(e,f)>0` for every distinct pair. QED.

The proof is an all-parameter local-response theorem. The finite computation is finite **local-type** coverage coupled to an analytic multiplicity transfer, not finite global graph-order coverage.

## 9. Independent all-pairs sanity check

As an independent check that does not reuse the transfer matrices for the pair counts, the executable evaluates

\[
K_3\vee(K_4\sqcup K_1)
\]

by a component-partition recurrence whose connected-block weights are Kirchhoff spanning-tree counts. Required edges are handled by exact contraction, retaining parallel-edge multiplicities after contraction.

For this 8-vertex, 24-edge noncomplete graph it obtains

\[
I_G(\mathbf1)=177186,
\]

and checks all `276` unordered edge pairs. The minimum and maximum Rayleigh gaps are

\[
\boxed{\min\Delta=8118180},
\qquad
\boxed{\max\Delta=1320302284}.
\]

The total forest count independently agrees with the transfer calculation. This check is only a sanity check; the all-parameter theorem is supplied by Sections 4–8.

## 10. Essential executable and actual output

Exact checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T12-18-00Z__triangle-cyclic-clique-atom-extension-checker.py`

Creation commit:

`4a51ab748cf6b9b0a02a50110ba2e32318f13cab`

Verified Git blob:

`218fa83b79d8d515fb34db85e7dd2794e696ad55`

Local executed source SHA-256 before upload:

`5892f051f9d2ecd77ef727b4224fbe742cc4e0a95f008c923561cddccc079a5b`

Executed output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T12-18-00Z__triangle-cyclic-clique-atom-extension-checker.out`

Creation commit:

`29592878be8fe5c7ea08996d6d7eb11b16acd0a4`

Verified Git blob:

`78edb584992b58aead8caf64de4305e1667315cd`

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

The checker recomputes the allowed component transfers, the exact `rho` ordering, all 11,017 widened-strip path responses, all 970 new atom response representatives (`317+325+328`), and the independent all-pairs partition/Kirchhoff sanity check.

## 11. Honest failures, residual obstruction, and next attack

No negative Rayleigh value was found. This run did encounter a real proof obligation rather than a computational failure: `K4` has `rho_K4<rho15`, so the previous insertion theorem by itself was insufficient. The old 15-path theorem had to be re-certified on the wider strip. That re-certification succeeded exactly, including all 203 exceptional path responses.

The parent obstruction remains arbitrary 3-connected graphs. The present class is highly structured by a common 3-vertex core, so it does not prove the P14 3-connected case.

The next promising attack is **not** another blind finite path cutoff. The response-strip machinery now suggests a reusable notion of a triangle-seeded strip-admissible right atom. The next run should derive a component-level deletion/contraction criterion ensuring:

1. `T_B=A(I+aN+cN^2)` with `A,a>0` and `rho_B` inside or only slightly below the current strip;
2. every marked local `B/B`, core/`B`, `B`/old-atom response lies in the Bernstein/discriminant sign cone;
3. if `rho_B` lowers the strip endpoint, the predecessor sector can be re-certified by a symbolic endpoint/discriminant argument rather than repeating large orbit enumeration.

`C5` is a natural first refutation target; the complete-clique sequence `K_r` is a second, more ambitious target because terminal symmetry may permit a recurrence in `r`. A first exact sign failure in either family should be preserved as a localized counterexample template rather than hidden by a larger positive census.

## 12. ledger_delta

```yaml
ledger_delta:
  parent:
    id: T07
    statement: pairwise negative edge correlation for the uniform measure on all forests of every finite graph
    before: OPEN
    after: OPEN
    complete_all_simple_graph_order_before: 9
    complete_all_simple_graph_order_after: 9
    source_valid_counterexample_order_lower_bound_before: ">=10"
    source_valid_counterexample_order_lower_bound_after: ">=10"
  mechanism:
    id: T07-TRIANGLE-P15-C3-C4-K4-STRIP-22
    before: "K3 join of arbitrary P1..P15 and C3 right-component multiplicities"
    after: "K3 join of arbitrary P1..P15, C3, C4 and K4 right-component multiplicities"
    new_unmarked_transfer: "T_K4 = 1763 I + 1952 N + 850 N^2"
    new_response_parameter: "rho_K4 = 203301/1720688"
    continuous_strip_after: "203301/1720688 <= h <= 1/8"
    widened_predecessor_path_recheck:
      local_types: 11017
      bernstein_certified: 10814
      discriminant_certified: 203
      failures: 0
      min_discriminant_margin: 16476912
    new_local_atom_checks:
      C3: 317
      C4: 325
      K4: 328
      failures: 0
  parent_connection:
    kind: structural_sign_theorem
    note: "Infinite 18-parameter family; finite computation is exhaustive only at local response-type level, with arbitrary multiplicities transferred analytically."
  p14_preserved:
    minimal_counterexample_reduction: "3-connected"
    failed_routes:
      - "generic degree-three mixed polarization has no universal sign"
      - "universal mixed-term positivity false"
      - "reverse-Cauchy sufficient inequality exactly refuted on a physical six-vertex graph"
      - "generic stability/Lorentzian/Garding shortcuts still lack hypothesis"
  companion_coordination:
    NM13_08: "uses its terminal-symmetric algebra and h-independent discriminant identity; distinct triangle seed and K4/widened-strip application here"
  proof_status:
    parent: PARTIAL
    restricted_theorem: CANDIDATE_FULL
    novelty: UNVERIFIED
    independent_review: pending
  artifacts:
    checker_commit: 4a51ab748cf6b9b0a02a50110ba2e32318f13cab
    checker_blob: 218fa83b79d8d515fb34db85e7dd2794e696ad55
    output_commit: 29592878be8fe5c7ea08996d6d7eb11b16acd0a4
    output_blob: 78edb584992b58aead8caf64de4305e1667315cd
    output_terminal: ALL_EXACT_CHECKS_PASS
```
