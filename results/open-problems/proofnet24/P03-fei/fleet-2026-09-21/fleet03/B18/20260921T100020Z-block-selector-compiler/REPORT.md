# B18 — exact physical-block influence telescope and critical-core selector compiler

**Status: PARTIAL / PROVED structural implication. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** This run used fresh authorized source material but no genuine authenticated brain retrieval/context.

## 0. Source-exact frontier and nonoverlap

Fresh source head used for the derivation: `59fbce9e02bdb8a7cf1fbdffb7dfa62993ac6143`.

This continuation combines two already-proved compatible ingredients without changing their claims:

1. `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T12-05-16Z__report.md`, blob `590719f32062225e1e225a97dbcd06523146db9b`: for every physical block `A`,
   
   \[
   B_A(f)\le \Delta_A H(f)\le 2B_A(f),
   \]
   
   and adaptive block entropy decrements telescope. That report left open a hereditary proper-block selector plus repeated-cost/lifetime accounting.
2. `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/2026-09-21T095741Z-critical-descendant-selector/REPORT.md`, blob `95ae302edfd4be5f47e5ab4677a068d1be57926e`: a descendant maximizing `H/I` is coordinate-critical, i.e. `Delta_i H >= (H/I) Inf_i` for every relevant coordinate.

The present B18 scope is nonoverlapping: extend the critical-descendant argument from coordinates to **every physical block**, and close the block report's missing **lifetime/summability implication** exactly. No packet-arithmetic claim from B15 and no signed-transport claim from B16 is duplicated.

## 1. Notation

Let `f:{-1,1}^R->{-1,1}` be Boolean after deleting irrelevant coordinates. For a nonempty physical block `A subseteq R`, and `a in {-1,1}^A`, write `f_a` for the restriction fixing `A=a`. Put

\[
\Delta_AH(f):=H(f)-2^{-|A|}\sum_a H(f_a),
\]

\[
I_A(f):=\sum_{i\in A}\operatorname{Inf}_i(f),
\]

and, for the Fourier spectral sample `S`,

\[
B_A(f):=H(S_A\mid S_{A^c}).
\]

The inherited block theorem is

\[
B_A\le \Delta_AH\le2B_A. \tag{1}
\]

## 2. PROVED: exact physical-block influence telescope

### Lemma 2.1
For every Boolean `f` and every physical block `A`,

\[
\boxed{
I(f)-2^{-|A|}\sum_a I(f_a)=I_A(f).
}
\tag{2}
\]

### Proof
For every free coordinate `j notin A`, an edge in direction `j` never changes the fixed `A`-assignment. Averaging the child edge-disagreement probability over all `a` therefore gives exactly the parent influence:

\[
2^{-|A|}\sum_a \operatorname{Inf}_j(f_a)=\operatorname{Inf}_j(f).
\]

Summing over `j notin A`,

\[
2^{-|A|}\sum_a I(f_a)=\sum_{j\notin A}\operatorname{Inf}_j(f)
=I(f)-I_A(f).
\]

This is (2). QED.

## 3. PROVED: the maximal-ratio descendant is critical for every block

For nonconstant `h`, write `r(h)=H(h)/I(h)`.

### Theorem 3.1 — all-block critical descendant
Given any nonconstant Boolean `f`, choose among all nonconstant physical restriction descendants a descendant `g` maximizing `r`. Then `r(g)>=r(f)`, and for **every nonempty physical block** `A` of relevant coordinates of `g`,

\[
\boxed{
\Delta_A H(g)\ge r(g) I_A(g).
}
\tag{3}
\]

Consequently, by (1),

\[
\boxed{
B_A(g)\ge \frac{r(g)}2 I_A(g)
}
\tag{4}
\]

for every such block, in particular every nonempty proper block.

### Proof
Every child `g_a` is a physical restriction descendant of `f`. If it is nonconstant, maximality gives

\[
H(g_a)\le r(g)I(g_a).
\]

If it is constant, both sides vanish, so the same inequality holds. Average over `a` and use Lemma 2.1:

\[
\begin{aligned}
H(g)
&=\Delta_AH(g)+2^{-|A|}\sum_a H(g_a)\\
&\le \Delta_AH(g)+r(g)2^{-|A|}\sum_a I(g_a)\\
&=\Delta_AH(g)+r(g)(I(g)-I_A(g)).
\end{aligned}
\]

Since `H(g)=r(g)I(g)`, cancellation yields (3). The upper half of (1), `Delta_AH<=2B_A`, yields (4). QED.

### Counterexample-core consequence
If some Boolean `f` violates `H(f)<=C I(f)`, then a physical restriction descendant `g` satisfies `r(g)>C` and simultaneously, for **every** nonempty proper physical block `A`,

\[
\boxed{
\frac{B_A(g)}{I_A(g)}>\frac C2.
}
\tag{5}
\]

Thus B14's all-coordinate critical core upgrades to an **all-proper-block critical core**. Any universal proper-block selector with coefficient `K` rules out counterexamples above `2K`.

## 4. PROVED: repeated proper-block influence costs telescope exactly

Consider any finite adaptive physical-block restriction tree `T`. At internal node `v`, let `f_v` be the current restricted Boolean function, query a nonempty block `A_v`, and let `w_v` be the probability of reaching that node. Let

\[
I_L:=\sum_{\ell\text{ leaf}} w_\ell I(f_\ell).
\]

### Theorem 4.1 — exact lifetime identity

\[
\boxed{
\sum_{v\text{ internal}} w_v I_{A_v}(f_v)=I(f)-I_L\le I(f).
}
\tag{6}
\]

### Proof
Apply Lemma 2.1 at every internal node, multiply by `w_v`, and sum. Each child influence term appears once with positive sign from its parent and, if internal, once with negative sign from its own local identity. All internal terms cancel. The root contributes `I(f)` and the leaves contribute `-I_L`. QED.

This closes the specific repeated-cost accounting gap left in the September-20 block report: once a **local** proper-block payment `B_A<=K I_A` is available at every nonterminal state, there is no additional lifetime/summability theorem to prove for physical influence.

## 5. PROVED: local proper-block selector alone compiles to full FEI

### Theorem 5.1 — proper-block selector compiler
Assume there is a finite constant `K` such that every Boolean `h` with at least two relevant coordinates has some nonempty proper physical block `A subsetneq R(h)` satisfying

\[
B_A(h)\le K I_A(h). \tag{7}
\]

Then every Boolean function satisfies

\[
\boxed{H(f)\le2K I(f).} \tag{8}
\]

### Proof
Build a physical block tree recursively: whenever the current state has at least two relevant coordinates, choose a proper block satisfying (7) and restrict it. Stop when a leaf has at most one relevant coordinate. Such a leaf is constant or a one-coordinate character up to sign, hence its Fourier entropy is zero. Because each query fixes at least one relevant coordinate, the construction terminates.

Let

\[
R_{\rm blk}(T)=\sum_v w_v B_{A_v}(f_v).
\]

By (7) and the lifetime identity (6),

\[
R_{\rm blk}(T)
\le K\sum_vw_v I_{A_v}(f_v)
=K(I(f)-I_L)
\le K I(f).
\]

The inherited block-tree theorem gives

\[
H(f)-H_L\le2R_{\rm blk}(T).
\]

Here `H_L=0`, so `H(f)<=2K I(f)`. QED.

### Quantitative equivalence of finite constants
Define

\[
K_{\rm sel}:=\sup_{h:\,|R(h)|\ge2}
\min_{\varnothing\ne A\subsetneq R(h)}\frac{B_A(h)}{I_A(h)}.
\]

Theorem 5.1 gives

\[
C_{\rm FEI}\le2K_{\rm sel}. \tag{9}
\]

Conversely, if FEI holds with coefficient `C`, then the standard conditional-entropy/Shearer inequality

\[
\sum_i B_i\le H(h)
\]

implies some relevant coordinate `i` has

\[
\frac{B_i}{\operatorname{Inf}_i(h)}\le\frac{H(h)}{I(h)}\le C.
\]

A singleton is a proper block whenever `|R(h)|>=2`, so

\[
K_{\rm sel}\le C_{\rm FEI}. \tag{10}
\]

Therefore

\[
\boxed{
\frac12 C_{\rm FEI}\le K_{\rm sel}\le C_{\rm FEI},
}
\tag{11}
\]

with the convention that finiteness is simultaneous. In particular, the full FEI conjecture is equivalent to finiteness of this **local proper-block selector constant**; the adaptive lifetime is automatic.

## 6. Challenge of tempting shortcuts

**REFUTED / circular shortcut 1 — query all remaining coordinates.** Taking `A=R(h)` gives `B_A=H(h)` and simply restates FEI. Properness is essential.

**REFUTED / circular shortcut 2 — co-singleton block from influence mass alone.** Choosing `A=R\setminus\{j\}` with a minimum-influence `j` guarantees `I_A>=I/2`, but `B_A=H(S_A|S_j)=H-h_2(Inf_j)` can still be of order `H`. This does not produce a universal `B_A/I_A` bound without already controlling `H/I`.

**Preserved B14 dead route.** The condition that all coordinates are locally bad is necessary at a maximal-ratio descendant but is not sufficient by itself for a global counterexample; negative child residuals can offset local excess. The present theorem strengthens the necessary condition to all physical blocks but does not reverse it.

**Product-spectrum endpoint is not enough.** The exact-product classification from fleet01/B18 proves a sharp constant 2 for independent spectral membership bits, but no dimension-free quantitative stability theorem from near-product structure is supplied here. It cannot be substituted for (7).

## 7. Status and next universal obligation

**PROVED in this continuation:** Lemma 2.1; Theorem 3.1; Theorem 4.1; Theorem 5.1; the factor-two comparison (11) between the optimal full-FEI constant and the optimal local proper-block selector constant.

**OPEN:** prove a dimension-independent finite bound on `K_sel`, equivalently find one proper physical block with `B_A<=K I_A` in every Boolean state with at least two relevant coordinates. This is now the single local obstruction for the block route; no separate repeated-lifetime accounting remains.

**Full FEI:** OPEN / NOT PROVED.

A nonredundant next attack should exploit Booleanity to produce the proper block. The strongest current counterexample-core target is: rule out a restriction-maximal Boolean `g` for which **every** nonempty proper block satisfies `B_A/I_A > C/2`, while simultaneously retaining B14's small-influence and diffuse-profile constraints. That is strictly stronger structure than the earlier every-coordinate core and is compatible with, but not solved by, the product-spectrum and packet/signed-transport routes.
