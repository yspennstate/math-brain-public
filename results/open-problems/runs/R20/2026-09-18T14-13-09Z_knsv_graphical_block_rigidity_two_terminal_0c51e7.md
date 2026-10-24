Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `N_sep > 11 -> N_sep > 11`; methods #15 BREAK THE SYMMETRY ON PURPOSE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

# R20 — KNSV Conjecture 8.2: graphical low-block rigidity and an exact two-terminal n=12 no-go

## 0. Current state recovered; stale Paley title not reopened

I continued from the newest immutable R20 report

`runs/R20/2026-09-18T12-59-00Z_knsv_rooted_subdivision_no_go_a4e8c2.md`

and the create-only exclusive claim

`operations/claims/KNSV-2026-LOOPY-U.md`.

The retired predecessor I0100 / Randomstrasse Conjecture 26 remains frozen at `p_max=1213` after its six-unchanged-run handoff. It is not reopened here. The current R20 target is **Kirillov--Nenashev--Shapiro--Vaintrob, arXiv:2609.07728v1, Conjecture 8.2**, status **CLAIMED / READY / CLOSABLE OUTSIDE**.

I reread the required campaign state (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`) and the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`. The current claim remains exclusively owned by R20; I found no newer R20 report after the predecessor above.

### Fresh source/current-literature check — 18 September 2026

I rechecked the current arXiv record and the author-hosted PDF `https://staff.math.su.se/shapiro/Articles/LoopyFinal.pdf`. The PDF still carries `arXiv:2609.07728v1 [math.CO] 7 Sep 2026`, still states Conjecture 8.2 for simple graphs, and still says the conjecture is verified through 11 vertices while simplicity is essential because of a five-vertex loopless-multigraph counterexample. Bounded fresh searches for the exact title, exact arXiv id, `Conjecture 8.2`, `proof`, `counterexample`, and `simple graphs` surfaced the source and indexing/mirror pages but no later source-matching proof or refutation. This is bounded negative evidence, not a worldwide novelty claim.

The source's Section 9.2 is especially relevant. For a nonempty block `B`, it defines

\[
C_G(B;q)=\sum_{A\subseteq E(G[B]),\ (B,A)\text{ connected}}q^{|A|},
\]

and, for `|B|=s`, the linear transform

\[
T_s\bigl(q^{s-1}(1+q)^r\bigr)=x_{s-1+r}.
\]

For an integer partition `lambda`, `S^G_lambda(q)` is the symmetrized sum of products of the block polynomials, while the corresponding loopy layer is the same symmetrized sum after applying the size-dependent maps `T_s` blockwise. The source notes only that one-nonsingleton-block profiles are automatic and gives an **arbitrary polynomial-valued set-function** obstruction at profile `(2,2)`; it explicitly says a proof must exploit graphical origin. The present run does exactly that.

## 1. Idea before validation

The route was formulated first and archived as

`artifacts/R20/2026-09-18T13-58-00Z_knsv_block_rigidity_two_terminal_idea_74c2a1.md`

before committing the new finite checker. The two attacks are genuinely different from the previous one-root and independent-subdivision searches:

1. exploit the severe form of graphical 2- and 3-vertex block polynomials to push the source's automatic-profile boundary much farther;
2. leave the articulation architecture completely and exhaust two-terminal, two-new-vertex extensions of the ten-vertex source seed at the first possible order `n=12`.

## 2. #18 + #25 — graphical low-block rigidity theorem

Write

\[
u=1+q,
\qquad
\mathcal B^G_\lambda(x)
:=
\sum_{\pi:\lambda(\pi)=\lambda}
\prod_{B\in\pi}T_{|B|}(C_G(B;q)).
\]

Thus `S^G_lambda(q)` is the ordinary block layer and `mathcal B^G_lambda` is its loopy-transformed layer.

### Theorem (SELF-CHECK ONLY: automatic graphical profile families)

For a simple graph `G`, `mathcal B^G_lambda` is determined by `S^G_lambda(q)` alone in either of the following two families:

1. **all parts of `lambda` are at most 3**;
2. **`lambda=(s,2^a,1^c)` for some `s>=4`**, i.e. there is one block of size at least four and every other nonsingleton block has size two.

Consequently, if two simple graphs have equal ordinary `U` (equivalently equal `X_B`, hence equal every `S_lambda`) but different `L`, then at least one offending block profile contains

\[
\boxed{\text{one block of size at least }4\quad\text{and a distinct block of size at least }3.}
\]

In particular the first potentially nonautomatic graphical profile is `(4,3)` (with any remaining singleton blocks), not `(2,2)`.

### Proof, family 1: all parts <=3

Write

\[
\lambda=(3^b,2^a,1^c).
\]

For a simple two-vertex induced graph,

\[
C_G(B;q)\in\{0,q\},
\qquad
T_2(C_G(B;q))\in\{0,x_1\}.
\]

For three vertices, a connected simple induced graph is either a path or a triangle, so

\[
C_G(B;q)=
\begin{cases}
0,&G[B]\text{ disconnected},\\
q^2,&G[B]\cong P_3,\\
3q^2+q^3=q^2(2+u),&G[B]\cong K_3.
\end{cases}
\]

Hence uniquely

\[
C_G(B;q)=q^2(\alpha_B+\beta_Bu),
\qquad
(\alpha_B,\beta_B)\in\{(0,0),(1,0),(2,1)\},
\]

and

\[
T_3(C_G(B;q))=\alpha_Bx_2+\beta_Bx_3.
\]

For a partition `pi` of type `lambda`, let `E_pi` be the product of the zero-one edge indicators contributed by its 2-blocks. Then

\[
\prod_{B\in\pi}C_G(B;q)
=q^{a+2b}E_\pi\prod_{j=1}^b(\alpha_j+\beta_ju).
\]

After summing over all `pi` of this type there are uniquely determined integers `M_0,...,M_b` such that

\[
q^{-a-2b}S^G_\lambda(q)=\sum_{k=0}^bM_ku^k.
\]

But expanding the transformed product counts **the same choices of the `beta` term twice**: once as the coefficient of `u^k`, and once as the coefficient of `x_2^{b-k}x_3^k`. Therefore

\[
\boxed{
\mathcal B^G_\lambda(x)
=x_0^c x_1^a\sum_{k=0}^bM_kx_2^{b-k}x_3^k.
}
\]

Thus this loopy layer is read directly from `S^G_lambda`.

### Proof, family 2: one large block and only 2-blocks besides it

Let

\[
\lambda=(s,2^a,1^c),\qquad s\ge4.
\]

Fix the unique `s`-block `B`. A nonzero contribution from each 2-block means precisely that the 2-blocks are edges of `G[V\setminus B]`; because they are disjoint, they are a matching of size `a`. Let

\[
m_a(G[V\setminus B])
\]

be the number of such matchings. There is a one-to-one correspondence between the nonzero set partitions with large block `B` and these matchings. Therefore

\[
S^G_\lambda(q)
=q^a\sum_{|B|=s}m_a(G[V\setminus B])C_G(B;q).
\]

Set

\[
R(q):=q^{-a}S^G_\lambda(q).
\]

Each summand lies in `q^{s-1}Q[1+q]`, so `T_s(R)` is defined. By linearity of `T_s`,

\[
\boxed{
\mathcal B^G_\lambda(x)
=x_0^c x_1^a T_s(R(q)).
}
\]

Again the transformed layer is determined by the ordinary layer. This proves the theorem and its corollary. `square`

## 3. The first real graphical obstruction is a triangle--4-block correlation

The preceding theorem makes `(4,3,1^{n-7})` the first profile where a block-transform failure can actually hide.

For a four-set `B`, write uniquely

\[
C_G(B;q)=q^3A_B(u),
\qquad
A_B(u)=\sum_{j=0}^3a_j(B)u^j,
\]

where the degree is at most three because a simple four-vertex graph has at most six edges. For a three-set `C`, write

\[
C_G(C;q)=q^2(\alpha_C+\beta_Cu),
\]

where `beta_C=1` exactly when `G[C]` is a triangle and is zero otherwise.

Write the known normalized ordinary layer as

\[
q^{-5}S^G_{(4,3,1^{n-7})}(q)
=\sum_{k=0}^4s_ku^k.
\]

Define, for `1<=k<=4`,

\[
h_k:=\sum_{\substack{|B|=4,\ |C|=3,\\B\cap C=\varnothing}}
a_{k-1}(B)\,\beta_C.
\]

Thus `h_k` is a weighted correlation between the `(k-1)`-st activity coefficient of a 4-block and a disjoint triangle. Comparing coefficients of `u^k` gives

\[
s_k
=\sum a_k(B)\alpha_C+h_k
\]

(with `a_{-1}=a_4=0`). In particular `h_4=s_4`, so only `h_1,h_2,h_3` can be hidden from this ordinary layer.

The loopy-transformed profile is exactly

\[
\boxed{
\mathcal B^G_{(4,3,1^{n-7})}
=x_0^{n-7}
\left[
\sum_{j=0}^3(s_j-h_j)x_{3+j}x_2
+\sum_{j=0}^3h_{j+1}x_{3+j}x_3
\right],
}
\]

where `h_0:=0` and `h_4=s_4`.

So the first potential obstruction is not an amorphous failure of the linear maps `T_s`: it is the three-dimensional hidden statistic

\[
\boxed{(h_1,h_2,h_3),}
\]

a triangle-versus-four-block activity correlation. This is the sharpest structural target recovered so far from the source's block-transform formulation.

This theorem is a **SELF-CHECK ONLY** symbolic argument. It has not received either required independent audit, and I do not claim source closure or publication novelty from the bounded search.

## 4. #15 — exact two-terminal attack at the first possible order n=12

The previous run showed that one-root attachments are structurally dead on the ten-vertex KNSV seed collision. This run genuinely broke that symmetry.

Let the source seed pair be the graph6 codes

`I?bB@_wYO`, `I?bB@_wk_`.

For every unordered pair `(r,s)` of old vertices I computed an exact two-terminal ordinary-U state. For each spanning edge subset it records:

- whether `r,s` lie in the same component;
- their distinguished component size(s);
- the multiset of all other component sizes;
- total cyclomatic number.

This state is sufficient for gluing along both terminals. If both sides connect the terminals, identification creates one additional cycle; in every other connectivity case cyclomatic numbers simply add. Component sizes follow by inclusion-exclusion of the one or two identified terminal vertices. Thus the ordinary-U convolution is exact.

### Strong seed-state fact

Among all `45 x 45` cross terminal-pair comparisons, the complete exact congruence relation is

\[
\boxed{
R_U^{(2)}(G_1;r,s)=R_U^{(2)}(G_2;r',s')
\iff ((r,s),(r',s'))=((2,9),(2,9)).
}
\]

That is stronger than the one-root picture: there is a unique two-terminal state match.

I did not stop at state-preserving gadgets. I exhaustively enumerated **all** simple extensions in the following `n=12` architecture, independently on both seed sides:

- choose any two old terminals;
- add two labelled new vertices 10 and 11;
- add an arbitrary simple graph supported on those four vertices;
- allow the terminal--terminal edge when it is absent from the seed;
- forbid duplicating it when it is already present.

Equivalently, the combined neighborhood of the two new vertices inside the old seed has support size at most two. Each seed has 14 old edges, so among its 45 terminal pairs there are 14 adjacent and 31 nonadjacent pairs. Hence the exact extension count is

\[
14\cdot 2^5+31\cdot2^6=2432
\]

per seed.

I grouped ordinary-U values first by exact integer coefficient dictionaries. Across the two 2432-element families there are

- `52` common ordinary-U classes;
- `5778` exact cross pairs with equal `U`;
- `262` collision-involved extension tags on each side.

Different tags can represent the same added edge set, leaving only `78` distinct collision-involved added-edge sets on each side for the `L(1,x)` calculation.

For `L(1,x)` I used an exact spanning-forest/activity dynamic program. I choose all seed edges first and added edges afterwards; this is legitimate because the forest activity expansion is edge-order independent. At an omitted edge the activity count increases exactly when its endpoints are already connected by earlier selected forest edges; a selected edge is allowed only when it joins two different forest components. Final component exponents are `|V(T)|-1+epsilon(T)`.

The result is exact:

\[
\boxed{
5778\text{ U-equal cross pairs},\qquad
0\text{ with different }L(1,x).
}
\]

Since the source proves that `L_G(t,x)` and `L_G(1,x)` determine one another, **none of these 5778 pairs is a separator in the attacked direction `U_G=U_H` but `L_G!=L_H`.**

This is a substantial architecture no-go, but it does **not** imply `N_sep>12`: arbitrary 12-vertex graphs, and even extensions of this seed whose two new vertices jointly see three or more old vertices, remain outside the search.

## 5. Exact checker and archived output

No floating point arithmetic is used.

- idea: `artifacts/R20/2026-09-18T13-58-00Z_knsv_block_rigidity_two_terminal_idea_74c2a1.md` @ `4dc6eacd9a2dfc3862f1858917af6b2c5283acc9`;
- checker: `artifacts/R20/knsv_two_terminal_n12_check.py` @ `dad85001788e2254406b7f974065c8f792764a97`;
- executed output: `artifacts/R20/knsv_two_terminal_n12_check.out` @ `e5c631c2bb543f0bb4c7a094d37e3fbf92c1f48b`.

The checker executed successfully. Its archived output ends

`U_equal_but_L1_different_pairs=0`

and labels its scope `PARTIAL_ONLY`.

The finite computation is a **SELF-CHECK / EXACT-FINITE** result, not an independent audit.

## 6. What moved conceptually, and what did not

The frozen source metric does **not** move:

\[
N_{\rm sep}>11\quad\longrightarrow\quad N_{\rm sep}>11.
\]

What changed is the mechanism. Two broad classes are now eliminated or reduced:

1. all source block profiles made only from 1-, 2-, and 3-blocks, plus every profile `(s,2^a,1^c)`, are **symbolically automatic** for simple graphs;
2. at minimal counterexample order 12, the full two-new-vertex extension family of the ten-vertex KNSV seed with old-neighbor support at most two contains no `U`-equal / `L`-different separator.

The next route should therefore not add a third one-root or two-terminal gadget lemma. The natural target is the first nonautomatic block profile `(4,3)`, especially the hidden triangle--4-block vector `(h_1,h_2,h_3)`.

Recommended next methods, not repeating this run: **#11 DUALIZE, #19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT.** Concretely:

- view `(h_1,h_2,h_3)` as a linear functional on the kernel of the ordinary-U block data;
- scan U-collision classes by this three-number statistic before computing full `L`;
- at `n=12`, prioritize seed perturbations or independent collision pairs maximizing the discrepancy of this hidden vector.

## 7. Model and scheduler control

The requested GPT-6 / maximum setting is still not enforceable from the exposed scheduler surface. The actual runtime model here is GPT-5.6 Sol and the reasoning level is UNVERIFIED. The operative implementation record exposes task prompt/title, schedule/timing, timing mode and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed one-hour execution field**. Enforcing GPT-6 / maximum would require an authorized product/backend surface that exposes those controls and attests the applied model/reasoning level.

The P26 permission history is context-dependent, not contradictory. `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records a context in which P26 returned `You cannot modify this task`; the newer root reconciliation records a later successful P26 update from another authorized context. The lawful workaround is therefore an owning/admin-authorized surface or platform support. There is no legitimate permission-bypass workaround, and no scheduler change was attempted here.

## 8. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  source: "Kirillov--Nenashev--Shapiro--Vaintrob, arXiv:2609.07728v1, Conjecture 8.2"
  source_scope: "simple graphs; equivalence of ordinary loopy L and ordinary U distinguishing power"
  metric: N_sep
  metric_definition: "minimum vertex count of a rigorously certified simple U/L separator in either direction"
  before: ">11"
  after: ">11"
  status: "PARTIAL / CLAIMED / OPEN-looking"
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  tried_moves: [15, 18, 25]
  evidence:
    - "operations/claims/KNSV-2026-LOOPY-U.md"
    - "runs/R20/2026-09-18T12-59-00Z_knsv_rooted_subdivision_no_go_a4e8c2.md"
    - "artifacts/R20/2026-09-18T13-58-00Z_knsv_block_rigidity_two_terminal_idea_74c2a1.md"
    - "artifacts/R20/knsv_two_terminal_n12_check.py"
    - "artifacts/R20/knsv_two_terminal_n12_check.out"
  audit_ids: []
  new_symbolic_reduction: "All profiles with parts <=3, and all (s,2^a,1^c), are automatic; any U=>L obstruction must contain a >=4 block and another >=3 block. First profile (4,3); hidden vector (h1,h2,h3)."
  new_exact_finite_result: "2432 extensions per seed; 52 common U classes; 5778 U-equal cross pairs; 0 U-equal/L1-different pairs for n=12 two-new-vertex extensions with combined old-neighbor support <=2."
  remaining_obligation: "Find a source-valid simple separator or prove the full equivalence. Next attack: determine whether the (4,3) hidden triangle--4-block correlation vector is forced by the full ordinary-U data, or construct a U collision where it differs."
  next_moves: [11, 19, 24]
  retired_predecessor: "I0100 Paley one-localization remains frozen at p_max=1213; not reopened"
```

**NO I0100 REOPENING. NO CONJECTURE-8.2 CLOSURE CLAIM. CURRENT R20 TARGET REMAINS KNSV-2026-LOOPY-U, PARTIAL.**
