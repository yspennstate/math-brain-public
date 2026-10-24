Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0029 — positive first-merge mixture for the actual two-peak law

## 1. Target, source scope, and run purpose

Target: `P0029`, Krzysztof Burdzy, *My favorite open problems*, Problem 9, “Do peaks of random labelings repell each other?”

Primary source: https://sites.math.washington.edu/~burdzy/open_mathjax.php

For a uniformly random labeling of the `n x n` discrete square conditioned on exactly two peaks, with `rho_n` their graph distance, the source asks whether

\[
\rho_n/n \Longrightarrow 0.
\]

The admission-frozen metric remains

\[
D_*:=\limsup_{n\to\infty}\mathbb E[\rho_n/n\mid\text{exactly two peaks}].
\]

This artifact executes the single recovery action selected in the preceding STUCK1 report: replace the signed independent-set representation by a positive two-front / first-merge representation of the **actual** two-peak pair law. The three Section-B methods are exactly:

- **B1 — change the category:** from alternating independent-set correlations to a positive absorbing two-component growth process;
- **B13 — find what only increases:** identify an exact pre-merge distance/size monovariant and a neutral-growth count;
- **B19 — make it an algorithm:** derive the exact two-component recursion and merge hazard.

The fixed source metric does not move in this artifact. The new results are structural theorems, not a source-level asymptotic answer.

Fresh source/literature check on 2026-09-18 UTC: Burdzy’s current official page still displays Problem 9 with the square-grid question above and separately marks Problem 10 solved. Burdzy–Pal, *Twin peaks*, Random Structures & Algorithms 56 (2020), 432–460, DOI 10.1002/rsa.20883, studies the same conditioned-labeling framework but its abstracted square result is the one-peak geometry and its two-peak results are on tree graphs, not this square endpoint. Agrawal–Erturk–Louis, *Successive vertex orderings of connected graphs*, arXiv:2604.07408 (2026), supplies closely related arbitrary-graph successive-ordering / independent-set machinery. A bounded current search found no later source-level solution of Burdzy Problem 9; this is negative evidence only, not a novelty certificate.

## 2. Descending reveal notation

Let `G=(V,E)` be a finite connected simple graph, `N=|V|`. A labeling is equivalent to a descending-label order

\[
\omega=(x_1,\ldots,x_N).
\]

A revealed vertex `x_k` is a **birth** iff it has no neighbor among the previously revealed vertices. Births are exactly peaks of the completed labeling.

For every nonempty seed set `T\subseteq V`, define

\[
F_G(T)
\]

to be the number of orders of `V\setminus T` which, appended after all vertices of `T` are already revealed, create no further birth. Thus, with

\[
\partial T:=\{x\notin T:N(x)\cap T\ne\varnothing\},
\]

we have the exact recursion

\[
F_G(V)=1,
\qquad
F_G(T)=\sum_{x\in\partial T}F_G(T\cup\{x\}).
\tag{2.1}
\]

If `C\subseteq V` induces a connected subgraph and `r\in C`, define

\[
h_C(r):=F_{G[C]}(\{r\}),
\tag{2.2}
\]

the number of successive orderings of the induced graph `G[C]` whose first vertex is `r`.

For nonadjacent vertices `r,v`, let

\[
W_G(r,v)
\]

be the number of full descending orders whose births are exactly `r` first and `v` second. Since the first revealed vertex is always a birth, `r` is the highest peak.

## 3. The positive first-merge state

Suppose `S\subset V` induces exactly two connected components `A` and `B`. Define the common merge frontier

\[
M_G(S):=\{x\in V\setminus S:
N(x)\cap A\ne\varnothing,
\quad
N(x)\cap B\ne\varnothing\},
\tag{3.1}
\]

and the weighted immediate-merge suffix count

\[
g_G(S):=\sum_{x\in M_G(S)}F_G(S\cup\{x\}).
\tag{3.2}
\]

The weight `g_G(S)` is positive exactly when a no-new-birth completion can merge the two components at its next step through some common-boundary vertex.

## 4. B1 theorem: exact ordered first-merge decomposition

### Theorem 4.1

Let `G` be a finite connected graph and let `r,v` be distinct nonadjacent vertices. Then

\[
\boxed{
W_G(r,v)=
\sum_{S}
\binom{|S|-1}{|A|-1}
 h_A(r)h_B(v)g_G(S),
}
\tag{4.1}
\]

where the sum is over all `S\subset V` such that `G[S]` has exactly two connected components `A,B`, with `r\in A` and `v\in B`.

### Proof

Take a full order counted by `W_G(r,v)`. Immediately after the second birth `v` appears, the revealed induced graph has exactly two components: the old component containing `r`, and the new singleton component containing `v`. Every later vertex before the components merge is not a birth, so it attaches to at least one already revealed component. Until the first time the two components become connected, every such vertex attaches to exactly one of the two components; hence the revealed graph continues to have exactly two components.

Because the final graph `G` is connected, there is a unique first reveal time at which the two components merge. Let `x` be that first merge vertex and let `S` be the revealed set immediately before `x`. Let `A,B` be the two components of `G[S]`, with `r\in A`, `v\in B`. There is no edge from `A` to `B`, otherwise they would already be one component. The vertex `x` is adjacent to both components, so `x\in M_G(S)`.

Restrict the pre-merge order to `A`. It begins at `r`, and every later vertex of `A` has an earlier neighbor in `A`; otherwise that vertex would have been another birth. Thus the restricted order is one of the `h_A(r)` successive orderings of `A`. Similarly, the restriction to `B` is one of the `h_B(v)` successive orderings of `B` and begins at `v`.

Write `a=|A|`, `b=|B|`, `s=a+b`. The global first vertex is fixed to be `r`. Once one rooted successive order on `A` and one on `B` are fixed, the remaining `a-1` vertices of the `A` order and all `b` vertices of the `B` order may be interleaved while preserving both internal orders. The number of such interleavings is

\[
\binom{s-1}{a-1}.
\tag{4.2}
\]

Because there is no edge between `A` and `B`, the first `B` vertex `v` has no earlier neighbor and is a birth; every later vertex of either component has an earlier internal neighbor and is not a birth. Hence `v` is the unique second birth before the merge.

After the pre-merge set `S` is revealed, choose the first merge vertex `x\in M_G(S)`. There are exactly `F_G(S\cup\{x\})` suffix orders after this choice which produce no further birth. Summing over `x` gives `g_G(S)`.

This construction is reversible. Given `S`, its ordered rooted component orders, their interleaving, a merge vertex `x`, and a suffix counted by `F_G(S\cup\{x\})`, one obtains a unique full order with births exactly `r,v` and with `S,x` as its first-merge state. Conversely every full order counted by `W_G(r,v)` has a unique first-merge state. Therefore the classes are disjoint and exhaustive, proving (4.1). ∎

## 5. Exact unordered law: the signed cancellation disappears completely

For a nonadjacent unordered pair `\{r,v\}`, define its actual two-peak weight

\[
U_G(\{r,v\}):=W_G(r,v)+W_G(v,r).
\tag{5.1}
\]

For a two-component state `S=A\sqcup B`, `r\in A`, `v\in B`, the contribution from the first orientation has interleaving coefficient `\binom{s-1}{a-1}` and the reverse orientation has coefficient `\binom{s-1}{b-1}=\binom{s-1}{a}`. Pascal’s identity gives

\[
\binom{s-1}{a-1}+\binom{s-1}{a}=\binom{s}{a}.
\]

Hence:

### Corollary 5.1 (positive unordered pair law)

\[
\boxed{
U_G(\{r,v\})=
\sum_{S}
\binom{|S|}{|A|}
 h_A(r)h_B(v)g_G(S),
}
\tag{5.2}
\]

where `S` ranges over two-component induced states with `r` and `v` in different components.

Every summand in (5.2) is a nonnegative integer. The actual pair law therefore has an **exact cancellation-free representation**; the alternating independent-set formula from the preceding run is no longer needed for the asymptotic attack.

## 6. Positive mixture over pre-merge states

For a connected induced graph `C`, put

\[
R(C):=\sum_{u\in C}h_C(u),
\qquad
\mu_C(u):=\frac{h_C(u)}{R(C)}.
\tag{6.1}
\]

For a two-component state `S=A\sqcup B`, define

\[
\Omega_G(S):=
\binom{|S|}{|A|}R(A)R(B)g_G(S).
\tag{6.2}
\]

Summing (5.2) over all unordered pairs gives the exact number of full orders with exactly two peaks:

\[
\boxed{
Z_2(G):=\#\{\omega:\omega\text{ has exactly two births}\}
=
\sum_{S:\,\kappa(G[S])=2}\Omega_G(S).
}
\tag{6.3}
\]

Moreover, conditional on the first-merge prestate `S=A\sqcup B`, the peak in `A` and the peak in `B` are independent with laws `\mu_A` and `\mu_B`:

\[
\boxed{
\Pr(R_A=r,R_B=v\mid S,\,\text{two peaks})
=
\mu_A(r)\mu_B(v).
}
\tag{6.4}
\]

Indeed, in (5.2) all factors other than `h_A(r)h_B(v)` depend only on `S`; normalization over `r\in A,v\in B` yields (6.4).

Thus the actual conditioned mean distance is exactly

\[
\boxed{
\mathbb E[\rho\mid\text{two peaks}]
=
\frac{
\sum_{S:\kappa(G[S])=2}
\Omega_G(S)
\mathbb E_{R_A\sim\mu_A,\,R_B\sim\mu_B} d_G(R_A,R_B)
}{
\sum_{S:\kappa(G[S])=2}\Omega_G(S)
}.
}
\tag{6.5}
\]

This is the main recovery result: the source problem has become a positive mixture of two independent **one-peak root laws** on the two components present immediately before their first merge.

## 7. One-peak probabilities remove the size-split binomial factor

Let

\[
p_1(C):=\Pr(\text{a uniformly random labeling/order of }C\text{ has exactly one peak}).
\]

The number of one-peak orders of `C` is precisely `R(C)`, so if `m=|C|`,

\[
R(C)=m!\,p_1(C).
\tag{7.1}
\]

Substituting into (6.2), with `a=|A|`, `b=|B|`, `s=a+b`, gives the exact cancellation

\[
\boxed{
\Omega_G(S)
=s!\,p_1(A)p_1(B)g_G(S).
}
\tag{7.2}
\]

The apparent combinatorial entropy of how the `s` pre-merge vertices split between the two components is therefore already absorbed exactly into the two one-peak probabilities. What remains is the geometry of the two component shapes and the merge-suffix weight `g_G(S)`.

## 8. A reversible-conductance representation of the component root law

The one-peak root law `\mu_C` itself has an exact positive edge representation.

### Proposition 8.1

For every connected induced graph `C` with `|C|\ge2` and every `r\in C`,

\[
\boxed{
h_C(r)=\sum_{y\sim_C r} F_{G[C]}(\{r,y\}).}
\tag{8.1}
\]

### Proof

Every successive order of `C` beginning at `r` has a unique second vertex `y`. Since no birth is allowed after `r`, that vertex must satisfy `y\sim_C r`. Once the ordered pair `(r,y)` is fixed, the rest of the order is exactly a no-further-birth completion counted by `F_{G[C]}(\{r,y\})`. The classes for distinct `y` are disjoint and exhaustive. ∎

Set the symmetric edge conductance

\[
c_C(\{x,y\}):=F_{G[C]}(\{x,y\}).
\tag{8.2}
\]

Then

\[
\boxed{
\mu_C(r)=
\frac{\sum_{y\sim_C r}c_C(\{r,y\})}
     {2\sum_{e\in E(C)}c_C(e)}.
}
\tag{8.3}
\]

So `\mu_C` is exactly the stationary vertex measure of the reversible nearest-neighbor walk on `C` with conductances `c_C`. In particular,

\[
\boxed{\max_{r\in C}\mu_C(r)\le \frac12}
\tag{8.4}
\]

for every connected `C` with at least two vertices, because the incident conductance at one vertex is at most the total edge conductance. The bound is sharp on stars. This does not by itself imply macroscopic separation on the square, but it turns the conditional peak locations in (6.4) into standard reversible-measure objects rather than signed derivatives.

## 9. B13: exact distance/size monovariant before first merge

Fix a contributing state `S=A\sqcup B` and roots `r\in A`, `v\in B`. Promote `v` to be revealed immediately after `r` while retaining the two rooted internal component orders; because there are no `A`–`B` edges, this promotion preserves validity of the pre-merge construction.

At any subsequent pre-merge time `t`, let `A_t,B_t` be the two revealed components and define

\[
\delta_t:=d_G(A_t,B_t).
\]

Adding one vertex to one component cannot increase `\delta_t` and can decrease it by at most one: if the new vertex `y` is adjacent to `A_t`, then by the triangle inequality

\[
d_G(y,B_t)\ge d_G(A_t,B_t)-1.
\]

Therefore

\[
\Phi_t:=|A_t|+|B_t|+\delta_t
\tag{9.1}
\]

is nondecreasing at every pre-merge addition. Initially the state is `\{r\},\{v\}`, so `\delta_0=d_G(r,v)`. Immediately before the merge, the two components have no cross-edge but possess a common neighbor, hence their distance is exactly `2`. If `s=|S|`, the `s-2` additions before the merge therefore contain exactly

\[
\boxed{d_G(r,v)-2}
\tag{9.2}
\]

distance-decreasing steps and exactly

\[
\boxed{s-d_G(r,v)}
\tag{9.3}
\]

distance-neutral steps. In particular,

\[
\boxed{d_G(r,v)\le |S|.}
\tag{9.4}
\]

This identifies the geometric entropy that an asymptotic proof must control. Macroscopically close roots can still live inside very large pre-merge states, but only by accumulating many neutral/interface-growth steps. The unresolved issue is whether those neutral histories dominate the positive mixture weight `\Omega_G(S)` on the square.

## 10. B19: exact two-component recursion and merge hazard

For a two-component state `S=A\sqcup B`, partition its frontier into

\[
L_A(S)=\{y\notin S:y\sim A,\ y\not\sim B\},
\]

\[
L_B(S)=\{y\notin S:y\sim B,\ y\not\sim A\},
\]

and the common boundary `M_G(S)`. The basic suffix recursion (2.1) gives the exact identity

\[
\boxed{
F_G(S)=
 g_G(S)
 +\sum_{y\in L_A(S)}F_G(S\cup\{y\})
 +\sum_{y\in L_B(S)}F_G(S\cup\{y\}).
}
\tag{10.1}
\]

Under the uniform suffix order conditioned to create no further birth from `S`, the probability that the very next vertex is the first merge vertex is therefore

\[
\boxed{
\lambda_G(S):=\frac{g_G(S)}{F_G(S)}.
}
\tag{10.2}
\]

This is a genuine absorbing-hazard formulation. Until absorption, the state evolves by adding a boundary vertex to one of the two components with transition weight proportional to `F_G(S\cup\{y\})`; absorption occurs through `M_G(S)` with total hazard `\lambda_G(S)`.

Equations (6.5), (8.3), and (10.2) expose the smallest currently known positive data needed by the square problem:

1. the distribution of the two-component pre-merge shape `S` under weight `\Omega_G`;
2. the reversible root measures `\mu_A,\mu_B` on its components;
3. the weighted common-boundary hazard encoded by `g_G(S)`.

Distance and component sizes alone do **not** close the recursion; interface shape enters through the `F`-weighted boundary. That is the precise remaining shape statistic rather than an unspecified “cancellation problem.”

## 11. Check against the solved path mechanism

Let `C` be a path interval of length `m`, with vertices numbered from left to right and root at position `j\in\{1,\dots,m\}`. A successive ordering grows the occupied interval by repeatedly taking its left or right boundary. To finish with `j-1` left expansions and `m-j` right expansions, the choices may be interleaved arbitrarily, so

\[
\boxed{h_C(j)=\binom{m-1}{j-1}.}
\tag{11.1}
\]

Consequently

\[
R(C)=2^{m-1},
\qquad
\mu_C(j)=2^{-(m-1)}\binom{m-1}{j-1}.
\tag{11.2}
\]

Thus the unique-peak root on a path component is exactly a shifted `Binomial(m-1,1/2)` variable.

Now let `S=A\sqcup B` be a contributing two-component state on the ambient path `P_N`, with `|A|=a`, `|B|=b`, `s=a+b`. If `g(S)>0`, the two intervals are separated by exactly one missing vertex `x`, the future merge vertex. Then `S\cup\{x\}` is one contiguous interval. If the unrevealed tails outside this interval have lengths `L` and `R`, then `L+R=N-s-1` and

\[
\boxed{
g_{P_N}(S)=F_{P_N}(S\cup\{x\})=\binom{N-s-1}{L}.}
\tag{11.3}
\]

Therefore

\[
\boxed{
\Omega_{P_N}(S)
=
\binom{s}{a}2^{s-2}\binom{N-s-1}{L}.
}
\tag{11.4}
\]

The first-merge mixture therefore collapses on the path to explicit binomial factors and binomial root laws, precisely the positive one-dimensional mechanism behind the earlier macroscopic-separation theorem. This validates the recovery category change against the already solved deformation rather than merely producing a new formal identity.

## 12. Exact finite self-check

After writing the mathematics above, I implemented an independent exact-integer self-check:

- source: `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T214200Z__P0029_first_merge_check.py`
- source creation commit: `24bae13ec54bcc694771b13746fbe31bb3630601`
- output: `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T214201Z__P0029_first_merge_check.out`
- output creation commit: `f917912beb90e14a41ed63552825ca9280bb26cd`

The checker enumerates **all labeled connected simple graphs on 2 through 5 vertices**. For each graph it brute-forces the birth sequence of every relevant permutation, verifies (4.1) ordered pair-by-pair, verifies (5.2) unordered pair-by-pair, and checks the rooted conductance identity (8.1) on every connected induced subgraph. Exact totals:

- connected graphs checked: `771`;
- ordered pair identities: `6454`;
- unordered pair identities: `3227`;
- rooted conductance induced-subgraph checks: `16312`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. This is a self-check of the finite theorem identities, not an independent audit and not source closure.

## 13. What changed, and what did not

### New mathematical content

1. Formula (4.1) proves the STUCK1 candidate first-merge decomposition, with the correct ordered interleaving factor.
2. Formula (5.2) is stronger for the source: it gives the **actual unordered peak-pair law as a positive sum**.
3. Formula (6.4) shows that, conditional on the pre-merge state, the two peaks are independent one-peak roots of the two components.
4. Formula (7.2) cancels the component-size binomial exactly into one-peak probabilities.
5. Formula (8.3) represents each one-peak root law as a reversible conductance stationary measure.
6. Formulae (9.2)–(9.3) exactly count distance-decreasing versus neutral pre-merge growth steps.
7. Formula (10.2) identifies the exact merge hazard and the shape information that remains uncontrolled.

### Source-level status

The source is still OPEN / PARTIAL. We have not proved either `D_*=0` or `D_*>0`. In particular, no estimate yet shows that a fixed positive fraction of the `\Omega`-mass lies on states whose two component-root laws remain macroscopically separated.

Frozen metric:

\[
D_*:\quad \text{UNKNOWN/UNMEASURED}\longrightarrow\text{UNKNOWN/UNMEASURED}.
\]

Movement: **NO MOVEMENT**.

This is the first ordinary run after STUCK1. The ordinary unchanged count therefore moves `3 -> 4`; the number of stuck recoveries remains `1`.

## 14. Exact next obstruction

Combining (6.5) and the square source, the remaining source-valid task is now purely positive:

\[
\boxed{
\limsup_{n\to\infty}
\frac{1}{n}
\frac{
\sum_{S}\Omega_n(S)
\mathbb E_{\mu_A\otimes\mu_B} d(R_A,R_B)
}{
\sum_S\Omega_n(S)
}
\stackrel{?}{>}0.
}
\tag{14.1}
\]

A NO answer to Burdzy’s proposed convergence follows from any positive lower bound in (14.1). The old obstacle of signed cancellation has been removed. The new obstacle is to control the **positive pre-merge shape measure** `\Omega_n` and the spatial separation of its two reversible root measures.

## 15. Next nonrepeating Section-B methods

The next ordinary attack should use three methods not previously used on P0029:

- **B11 — dualize.** For each state `S=A\sqcup B`, lower-bound `E d(R_A,R_B)` using a 1-Lipschitz coordinate or cut potential: `E d(R_A,R_B) >= |E f(R_A)-E f(R_B)|`. Search for a coarse dual observable of the conductance root laws rather than pairwise estimates.
- **B12 — find what is conserved.** Treat (10.1) as a flow on the DAG of two-component states and seek a conserved/telescoping flux whose absorbed part is `g(S)`. The goal is to control aggregate `\Omega`-mass across a spatial separator without enumerating shapes.
- **B27 — swap the quantifiers.** Do not control every two-component state. It is enough to exhibit a family of states carrying a fixed positive fraction of total `\Omega`-mass and prove macroscopic root-law separation only on that family.

No checker extension to a larger square is proposed; the next work should attack (14.1) directly.
