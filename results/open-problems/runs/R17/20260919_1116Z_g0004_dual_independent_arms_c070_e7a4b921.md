Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; substantive unchanged count `1 -> 2`; methods #11 DUALIZE / #20 FIND WHY THE ALGORITHM FAILS / #24 FIND THE EXTREMAL OBJECT.**

# R17 C070 — G0004: exact selector dual, independent-arm theorem, and root-neighborhood star domination

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R17, HARD OUTSIDE.
Status: **OPEN / PARTIAL**.

## 0. Continuity, source, ownership, and metric

The controlling canonical claim remains `operations/claims/G0004.md`: R17 is the exclusive owner of Lucas Flammant, *A finite-graph conjecture related to theta(p_c)=0 for Bernoulli bond percolation on Z^d*, arXiv:2609.03492v2, Conjecture 2.2. The original binary-LCS source remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and D0064 remains terminal for R17 at `R_class=0/3`. Neither is reopened.

At run start I reread campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the direct G0004 claim, C069, the R7-02 G0004 screen, and the G/H intake records around arXiv:2609.03492. A fresh 2026-09-19 bounded primary-source search still finds arXiv v2 as the current source statement, with the outer-face planar theorem and the general finite-graph statement still presented as a conjecture. I found no later primary source claiming the full arbitrary-finite-graph conclusion. This is bounded negative evidence, not a global novelty certificate.

C069 already proved: (i) automorphism symmetrization, (ii) the exact full kernel optimization on every homogeneous star, and (iii)

\[
S_{\rm star}(\varepsilon)
:=\sup_{m,p}R_{\rm star}(m,p,\varepsilon)
\sim \varepsilon\log(1/\varepsilon).
\]

Those results are inherited, not rederived as new work here.

The fixed source-wide metric remains

\[
U_F:=\inf\bigl\{u:\ \limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under the full source quantifiers}\bigr\}.
\]

Before: `U_F=1`. After: `U_F=1`. The new theorems below are restricted or reformulatory, so the source metric does not move.

## 1. Exact setup inherited from R7-02

Let Bernoulli bond percolation with parameter `p` live on a finite graph `G=(V,E)`, with root `o` and boundary set `B`. For a configuration `omega`, put

\[
S(\omega)=\{b\in B:o\leftrightarrow b\},
\qquad C=\{S\ne\varnothing\}.
\]

After eliminating auxiliary randomness, the adverse high-probability events are represented by decreasing kernels

\[
q_b:\{0,1\}^E\to[0,1],\qquad \mathbb E q_b\le\varepsilon.
\]

The exact failure numerator on a fixed instance is

\[
F(q):=\mathbb E\left[\mathbf1_C\min_{b\in S}q_b\right],
\]

and the failure ratio is `F(q)/P(C)`. The source conjecture is equivalent to the supremum of this ratio over all finite instances tending to zero with `epsilon`.

## 2. Method #11 — exact fractional-selector dual

The failed monotone-selector architecture from R7-02 imposed too much structure. The correct dual does not require a monotone selector at all.

For every configuration `omega in C`, let `Delta(S(omega))` be the probability simplex on `S(omega)`. Let `A` be the set of arrays `alpha=(alpha_b(omega))` such that

\[
\alpha_b(\omega)\ge0,\qquad
\alpha_b(\omega)=0\ (b\notin S(\omega)),\qquad
\sum_{b\in S(\omega)}\alpha_b(\omega)=1
\]

for `omega in C`; set all `alpha_b(omega)=0` off `C`.

For any nonnegative function `f` on the configuration space define the monotone-budget functional

\[
H_\varepsilon(f)
:=\sup\left\{
\mathbb E[fq]:
0\le q\le1,\ q\text{ decreasing},\ \mathbb E q\le\varepsilon
\right\}.
\]

### Theorem 2.1 (exact selector minimax)

For every fixed finite percolation instance,

\[
\boxed{
\sup_{(q_b)}F(q)
=
\min_{\alpha\in A}\sum_{b\in B}H_\varepsilon(\alpha_b).
}
\]

Hence **every** fractional selector `alpha` gives an upper-bound certificate

\[
\sup_q F(q)\le \sum_b H_\varepsilon(\alpha_b),
\]

and the best such certificate is exact.

#### Proof

Pointwise, for every `omega in C`,

\[
\min_{b\in S(\omega)}q_b(\omega)
=
\min_{a\in\Delta(S(\omega))}
\sum_{b\in S(\omega)}a_bq_b(\omega).
\]

Therefore

\[
F(q)=\min_{\alpha\in A}
\sum_b\mathbb E[\alpha_bq_b].
\]

The feasible kernel set is a finite-dimensional compact convex polytope and so is `A`; the displayed payoff is bilinear and continuous. Finite-dimensional minimax therefore gives

\[
\sup_q\min_\alpha\sum_b\mathbb E[\alpha_bq_b]
=
\min_\alpha\sup_q\sum_b\mathbb E[\alpha_bq_b].
\]

The kernel constraints separate over `b`, so the inner supremum is exactly `sum_b H_epsilon(alpha_b)`. This proves the formula. `square`

This is materially different from the inherited impossible monotone partition-of-unity attempt: `alpha` need not be increasing, decreasing, deterministic, or equivariant. The only exact constraint is that it fractionally selects currently connected boundary vertices.

### Theorem 2.2 (downset LP dual for `H_epsilon`)

For every nonnegative `f`,

\[
\boxed{
H_\varepsilon(f)
=
\inf_{\lambda\ge0}
\left\{
\lambda\varepsilon
+
\sup_{D\ \mathrm{decreasing}}
\mathbb E[(f-\lambda)\mathbf1_D]
\right\}.
}
\]

#### Proof

For fixed `lambda>=0`, finite LP Lagrange duality for the budget `E q<=epsilon` gives

\[
H_\varepsilon(f)
=
\inf_{\lambda\ge0}
\left[
\lambda\varepsilon+
\sup_{0\le q\le1,\ q\downarrow}
\mathbb E[(f-\lambda)q]
\right].
\]

It remains to identify the last supremum. Every decreasing `q:[0,1]^E->[0,1]` has the layer-cake representation

\[
q(\omega)=\int_0^1
\mathbf1_{\{q\ge t\}}(\omega)\,dt,
\]

and every superlevel set `{q>=t}` is decreasing. Thus every feasible `q` is a convex mixture of indicators of decreasing sets. A linear functional on this order polytope is therefore maximized by a decreasing-set indicator. Substitution proves the claim. `square`

The full conjecture can now be restated as a **fractional-selector discrepancy problem**: uniformly over every finite connectivity instance, construct `alpha` with

\[
\sum_bH_\varepsilon(\alpha_b)=o(\mathbb P(C)).
\]

That is a substantially more precise target than trying to make the selector itself monotone.

## 3. Method #20 — the independent-arm algorithm and the exact place it breaks

The dual above suggests first understanding when membership in the connected boundary set is genuinely independent. That model admits a complete quantitative theorem with arbitrary arm probabilities and arbitrary decreasing kernels.

Let `X_1,...,X_m` be independent Bernoulli variables with parameters `r_i in (0,1)`. Put

\[
K=\sum_iX_i,\qquad C=\{K>0\}.
\]

Let `q_i:{0,1}^m->[0,1]` be arbitrary decreasing functions with `E q_i<=epsilon`. Define

\[
R_{\rm ind}:=
\frac{\mathbb E[\mathbf1_C\min_{i:X_i=1}q_i]}{\mathbb P(C)}.
\]

### Theorem 3.1 (heterogeneous independent-arm modulus)

For `0<epsilon<=1/2`, uniformly over `m`, all arm probabilities `(r_i)`, and all feasible decreasing kernels,

\[
\boxed{
R_{\rm ind}
\le
4\varepsilon\log^2\frac1\varepsilon
+7\varepsilon\log\frac1\varepsilon
+2\varepsilon.
}
\]

In particular the full independent-arm class satisfies the qualitative Flammant conclusion.

#### Proof

For `t in (0,1]` define the decreasing bad sets

\[
D_i(t):=\{q_i\ge t\}.
\]

By Markov,

\[
\mathbb P(D_i(t))\le\delta:=\varepsilon/t.
\]

Let `F_t` be the family consisting of the zero vector together with all nonzero configurations `x` for which every active coordinate is bad:

\[
x\in F_t,\ x\ne0
\quad\Longleftrightarrow\quad
D_i(t)\text{ holds for every }i\text{ with }x_i=1.
\]

Because every `D_i(t)` is decreasing, `F_t` is a downset.

For coordinate `i`, let the link be

\[
(F_t)_i
:=\{x_{-i}:(1,x_{-i})\in F_t\}.
\]

Membership in this link implies `D_i(t)` with `X_i=1`. Since `D_i(t)` is decreasing while `{X_i=1}` is increasing, Harris-FKG gives

\[
\mu_{-i}((F_t)_i)
\le \mathbb P(D_i(t)\mid X_i=1)
\le \mathbb P(D_i(t))
\le\delta.
\]

Write `lambda=E K=sum_i r_i`. Counting the same marked bad configuration by each active coordinate gives

\[
\mathbb E[K\mathbf1_{F_t}]
=
\sum_i r_i\mu_{-i}((F_t)_i)
\le\delta\lambda.
\]

Assume first `delta<=1/2` and put `L=log(1/delta)`.

If `lambda<=8L`, then

\[
\mathbb P(F_t\cap C)
\le \mathbb E[K\mathbf1_{F_t}]
\le\delta\lambda.
\]

Also

\[
\mathbb P(C)=1-\prod_i(1-r_i)\ge1-e^{-\lambda}\ge\frac{\lambda}{1+\lambda},
\]

so

\[
\frac{\mathbb P(F_t\cap C)}{\mathbb P(C)}
\le\delta(1+\lambda)
\le\delta(1+8L).
\]

If `lambda>8L`, split at `K=lambda/2`. The first-moment estimate gives

\[
\mathbb P(F_t\cap\{K\ge\lambda/2\})
\le\frac2\lambda\mathbb E[K\mathbf1_{F_t}]
\le2\delta.
\]

The standard multiplicative Chernoff lower tail for a Poisson-binomial sum gives

\[
\mathbb P(K<\lambda/2)\le e^{-\lambda/8}<e^{-L}=\delta.
\]

Thus `P(F_t cap C)<=3 delta`; dividing by `P(C)>=1-e^{-lambda}` and using `delta<=1/2` yields the looser uniform estimate

\[
\frac{\mathbb P(F_t\cap C)}{\mathbb P(C)}
\le \delta(7+8L).
\]

The same bound also covers the previous case. For `delta>1/2` use the trivial bound `1`.

Finally, layer cake gives

\[
R_{\rm ind}
=
\int_0^1
\frac{\mathbb P(F_t\cap C)}{\mathbb P(C)}\,dt.
\]

For `t<=2epsilon`, use `1`; this contributes at most `2epsilon`. For `2epsilon<=t<=1`, substitute `delta=epsilon/t`:

\[
R_{\rm ind}
\le
2\varepsilon+
\int_{2\varepsilon}^1
\frac{\varepsilon}{t}
\left(7+8\log\frac{t}{\varepsilon}\right)dt.
\]

The integral equals

\[
7\varepsilon\log\frac1{2\varepsilon}
+4\varepsilon
\left[
\log^2\frac1\varepsilon-\log^22
\right],
\]

which is bounded by the displayed claim. `square`

### Why this algorithm does not immediately solve arbitrary graphs

There is a useful general fact: for every threshold `t`, if we adjoin `C^c` to the graph-percolation failure event

\[
\{C\text{ and }q_b\ge t\text{ for every }b\in S\},
\]

the resulting subset of the edge hypercube is decreasing. So the obstruction is **not** failure of downset structure.

The independent-arm proof succeeds because each Boolean coordinate has a canonical boundary label `i`, and the `i`-link of the failure downset is contained in the single rare set `D_i(t)`. Hence every coordinate link has measure at most `delta`.

For a general graph edge `e`, no such canonical label exists. Opening one edge can connect many boundary vertices at once, can merge two large components, or can leave `S(omega)` unchanged while changing the order in which an exploration discovers connections. Thus the edge link of the failure downset is not contained in any one rare `D_b(t)`, and the link estimate driving Theorem 3.1 disappears.

This matches the obstruction recorded in Flammant's Section 4: cyclic edge changes can preserve the connected boundary set while altering a DFS-type discovery order, and a satisfactory global recursion over all connections is missing. The exact selector dual above is a candidate global object, but one still needs a geometry-free way to charge its decreasing-set discrepancy to the `epsilon` budgets.

This is the precise reason the independent-arm algorithm fails to extend automatically; it is not merely “dependencies are hard.”

## 4. Method #24 — stars remain extremal after arbitrary interior decoration when the boundary contains the root neighborhood

The next theorem is source-valid and allows completely arbitrary nonplanar structure away from the root.

### Theorem 4.1 (root-neighborhood star domination)

Let `G` be any finite loopless graph or multigraph with root `o`, and assume

\[
N(o)\subseteq B.
\]

Let `m=deg(o)`, counting parallel incident edges. Then for every `p` and every admissible decreasing kernel family,

\[
\boxed{
R(G,p,o,B;q)
\le R_{\rm star}(m,p,\varepsilon)
\le S_{\rm star}(\varepsilon).
}
\]

Consequently, using C069,

\[
\sup_{\substack{G,o,B:\ N(o)\subseteq B}}
R(G,p,o,B;q)
=
O\!\left(\varepsilon\log\frac1\varepsilon\right)
\]

uniformly over all graph sizes, all interior topology, and `p`; more sharply the worst asymptotic constant is at most the star constant from C069.

#### Proof

Let `I` be the multiset of edges incident to `o`, so `|I|=m`, and let `X=(X_e)_{e in I}` be their open/closed states. These coordinates are independent Bernoulli(`p`). Since every endpoint of an incident edge belongs to `B`,

\[
C=\{\exists e\in I:X_e=1\}.
\]

For each incident edge `e=ob`, assign the kernel `q_e:=q_b`. If `X_e=1`, then its endpoint `b` is certainly connected to `o`; therefore the set of endpoints of open incident edges is contained in `S(omega)`. Hence pointwise on `C`,

\[
\min_{b\in S(\omega)}q_b(\omega)
\le
\min_{e\in I:X_e=1}q_{b(e)}(\omega).
\]

Condition on the incident-edge vector `X`. Because `min` is concave,

\[
\mathbb E\left[
\min_{e:X_e=1}q_{b(e)}\mid X
\right]
\le
\min_{e:X_e=1}
\mathbb E[q_{b(e)}\mid X].
\]

Define

\[
\widetilde q_e(X):=
\mathbb E[q_{b(e)}\mid X].
\]

Averaging over all nonincident edges preserves coordinatewise decreasingness, so every `tilde q_e` is a decreasing function of the independent incident-edge vector. Also

\[
\mathbb E\widetilde q_e=\mathbb E q_{b(e)}\le\varepsilon.
\]

Thus the conditioned right-hand side is a feasible kernel family for the ordinary homogeneous `m`-arm star. Parallel edges create duplicate endpoint labels before conditioning, but relaxing those duplicates to arbitrary star kernels can only enlarge the supremum. The denominator is exactly the same star denominator,

\[
\mathbb P(C)=1-(1-p)^m.
\]

Taking expectations gives the first inequality, and C069 gives the second. `square`

This identifies a genuine extremal phenomenon: **arbitrary interior decoration cannot make the source harder when the boundary already swallows the root neighborhood**. Any counterexample, if one exists, must exploit connectivity that is created only after at least one nontrivial interior step from `o`; it cannot be generated by complicated downstream geometry attached behind already-boundary incident neighbors.

## 5. What moved mathematically, and what did not

New exact results in this run:

1. an exact finite-instance fractional-selector minimax formula;
2. an exact downset/Lagrange representation of each selector cost `H_epsilon`;
3. a uniform `O(epsilon log^2(1/epsilon))` theorem for arbitrary heterogeneous independent membership arms and arbitrary decreasing kernels;
4. exact domination by the homogeneous star for every finite loopless graph/multigraph satisfying `N(o) subseteq B`, hence the sharp C069 `epsilon log(1/epsilon)` scale on that whole decorated class;
5. a precise obstruction to porting the independent-arm proof: general graph edge links cannot be assigned to a single rare boundary bad set.

None of these controls arbitrary finite graphs, so the strict metric remains `U_F=1`. This is the second consecutive substantive G0004 run with no source-metric movement, not yet a Section-I stuck episode.

No finite numerical enumeration is promoted as a theorem in this report, so no exact-arithmetic checker artifact is required. All theorem-sized claims above have written proofs on the page.

## 6. Next route

The next triple, deliberately different from C069 and C070, is:

- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite threshold failure as an order-ideal / Boolean-lattice boundary problem and the selector dual as a fractional flow;
- **#25 COUNT THE SAME THING TWICE:** count edge-boundary exits of the failure downset both by pivotal edges and by newly connected boundary vertices, looking for the missing global charging inequality;
- **#30 DO ONE SCALE / ONE DIRECTION AT A TIME:** first prove the needed charging inequality for a single labeled cut separating `o` from `B`, then identify exactly what prevents gluing cuts through cycles.

If `U_F` remains unchanged on the next substantive run, the three-run trigger will require the formal Section-I stuck report and one of the permitted HARD recovery choices.

## 7. Model / scheduler-control status

The exposed task-management schema in this runtime still provides schedule/prompt/title/enablement/timing controls but **no bindable model-family field, no reasoning-effort field, and no authenticated runtime-attestation field**. Thus “GPT-6, maximum” remains a prompt request only here. Enforcing it requires an authorized product/API/workspace scheduler surface that actually exposes model and reasoning settings and reports the model used at execution.

The historical `You cannot modify this task` result for P26 is an authorization-context boundary, not a mathematical or repository issue. The repository reconciliation records that P26 was later successfully updated from another authorized context. The valid workaround for a denied native edit is therefore the owning/admin-authorized task context or platform support; duplicating a task, editing GitHub, or bypassing permissions is not a scheduler repair.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  worker: R17
  target: G0004
  source: "Flammant arXiv:2609.03492v2, Conjecture 2.2"
  lane: HARD_OUTSIDE
  status: PARTIAL
  metric:
    name: U_F
    before: 1
    after: 1
    movement: false
  unchanged_substantive_runs:
    before: 1
    after: 2
  methods_tried: [11, 20, 24]
  results:
    - exact fractional-selector minimax dual
    - exact downset LP dual for selector cost
    - heterogeneous independent-arm O(epsilon log^2(1/epsilon)) theorem
    - root-neighborhood star-domination theorem
  source_closed: false
  recovery_count: 0
  next_methods: [18, 25, 30]
  shared_root_edits: false
  peer_file_edits: false
  artifacts_added: false
```
