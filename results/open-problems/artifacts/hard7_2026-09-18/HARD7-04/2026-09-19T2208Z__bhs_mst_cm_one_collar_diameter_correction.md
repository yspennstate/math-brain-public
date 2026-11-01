Runtime identification: **GPT-5.6 Sol; reasoning telemetry UNVERIFIED — not GPT-6 maximum.**

# HARD7-04 correction checkpoint — one-collar path count is rigorous on the post-giant residual

This note corrects one overstatement in the immediately preceding immutable idea checkpoint `2026-09-19T2156Z__bhs_mst_cm_one_collar_diameter_idea.md`. The preceding note used the outside `B`-stub count as the denominator of a specified `B` pairing. That is not exact: the fresh `B` matching is uniform on **all** `B` half-edges, so a specified `B` pair has denominator equal to the total `B` matching pool. Moreover, after the lower `A` principal component is explored, the deferred-decision argument gives an exactly fresh residual `A` matching only on the still-unexplored post-giant vertices; pre-giant components have already been exposed. Therefore the rigorous theorem proved below is a **post-giant residual one-collar diameter bound**, not yet a bound for every component outside the giant.

The correction does not affect the earlier MD5 theorem or the two-type deterministic target; it changes the path-count bookkeeping and narrows the geometric conclusion to the region where deferred decisions are exact.

## 1. Residual setup

Use the same explicit Pareto-quantile subclass and mesoscopic scale

`epsilon_n=(log n)^3 n^{-eta}`, `eta=(tau-3)/(tau-1)`,

with lower color `A` at `p_n=(1+epsilon_n)/nu_n` and collar color `B` of width

`Delta_n=delta epsilon_n/nu_n`, `0<delta<beta=tau-3`.

Run the standard continuous-time exploration of the lower `A` configuration model. Let `T_2` be the end of the principal barely-supercritical component and let `V_post` be the vertices still sleeping immediately after `T_2`. By deferred decisions, conditional on the full exploration history through `T_2`, the unmatched `A` half-edges incident to `V_post` form a uniform perfect matching. The edge-color-first construction makes the entire `B` matching independent of the `A` exploration and uniform on the total `B` half-edge set.

Let

- `A_v` be the number of residual `A` half-edges of `v in V_post`;
- `B_v` its number of `B` half-edges;
- `S_A=sum_{V_post} A_v`;
- `S_B=sum_{V_post} B_v`;
- `L_B=sum_v B_v`, the total `B` half-edge count over all vertices.

The MD5 proof plus the fact that the pre-giant squared-degree mass is `o_P(epsilon_n n)` imply that deleting the pre-giant vertices changes all first/second mixed marked sums only by `o_P(epsilon_n n)`. The hypergeometric `B`-sampling step from the 20:30Z checkpoint then gives, on an event of probability `1-o(1)`, the effective post-giant two-type matrix

`Mpost = [[ sum A_v(A_v-1)/S_A,
            (S_B/L_B) * sum A_v B_v/S_A ],
          [ sum A_v B_v/S_B,
            sum B_v(B_v-1)/L_B ]]`

`       = h_n'(q_n) [[p_n, Delta_n],[p_n, Delta_n]] + o(epsilon_n)` entrywise.      (1)

The `S_B/L_B` factor in the `A->B` entry is the probability that a uniformly paired `B` stub remains in `V_post`; in the `B->B` entry the same factor cancels the size-bias denominator `S_B`, leaving the exact total-pool denominator `L_B`.

The finite-`n` Pareto duality already proved on this track gives

`max_i sum_j Mpost(i,j) <= 1-c_0 epsilon_n`                    (2)

with high probability for any fixed `c_0<(beta-delta)/2` and all large `n`.

## 2. Exact finite-matching path count on `V_post`

Let `N_l^post` be the number of oriented vertex-simple paths of length `l` that stay entirely in `V_post` and use only `A` and `B` edges.

Conditional on the exploration history and the colored degree profile, a prescribed collection of `m_A` disjoint residual `A` pairings and `m_B` prescribed `B` pairings has probability

`prod_{j=0}^{m_A-1}(S_A-(2j+1))^{-1}
 * prod_{j=0}^{m_B-1}(L_B-(2j+1))^{-1}`.                       (3)

This is the corrected denominator. The candidate-vertex sums corresponding to (3) are exactly the factorial/mixed sums in (1). Dropping the vertex-distinctness constraint only enlarges the first moment, so summing over color words yields

`E[N_l^post | good profile, exploration history]
 <= C n * R_l * ||Mpost||_infty^(l-1)`,                         (4)

where `R_l` is the without-replacement correction. Since `S_A=Theta(n)` and `L_B=Theta(epsilon_n n)`,

`log R_l = O(l^2/S_A + l^2/L_B)`.                               (5)

Take `l_n=ceil(K epsilon_n^{-1} log n)`. Then

`l_n^2/L_B
 = O(epsilon_n^{-3}(log n)^2/n)
 = O(n^(3 eta-1)/(log n)^7)
 ->0`,                                                          (6)

because `eta<1/3`; also `l_n^2/S_A->0`. Thus `R_l=1+o(1)` uniformly for `l<=l_n`.

By (2),

`E[N_l_n^post | good profile, history]
 <= C n exp[-c_0 epsilon_n l_n+o(1)]`.                           (7)

Choose `K>3/c_0`. The right side tends to zero. Hence Markov gives

`P(N_l_n^post>0)->0`.                                           (8)

Every component of the `(A,B)` graph induced on `V_post` with diameter at least `l_n` contains a vertex-simple shortest path of length `l_n`. Therefore

`Delta_max(G_{A union B}[V_post])
 = O_P(epsilon_n^{-1} log n)
 = O_P(n^eta/(log n)^2)
 = o_P(n^eta)`.                                                 (9)

This is a genuine finite-matching geometric consequence of MD5, not a Galton--Watson approximation or finite simulation.

## 3. What is still missing

The preceding broader statement for *all* outside-giant vertices is not promoted. The unresolved pieces are now sharply separated:

1. **pre-giant geometry:** the early-awakening argument proves their total quadratic marked mass is `o_P(epsilon_n n)`, but this alone does not bound their maximum diameter at the `epsilon_n^{-1} log n` scale;
2. **uniform Kruskal ladder:** even after controlling one post-giant collar, the source theorem needs a uniform sequence of thresholds from fixed critical-window `lambda` through the mesoscopic regime and eventually to the full MST;
3. **Hausdorff attachment control:** the CM analogue of the source's rank-one upper-MST approximation must show the entire forest attached outside the critical core has `o_P(n^eta)` height in the correct order of limits.

Thus the corrected source-style blocker remains

`lim_{lambda->infinity} limsup_{n->infinity}
 P(n^{-eta} d_H(M_{n,lambda},M_n)>varepsilon)=0`                (10)

for every `varepsilon>0`.

No checker is created: there is no finite exhaustive claim. The correction and proof are on the page.