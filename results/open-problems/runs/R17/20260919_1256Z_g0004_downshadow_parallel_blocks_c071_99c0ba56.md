Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; substantive unchanged count `2 -> 3`; SECTION-I STUCK TRIGGERED; methods #18 SAY IT IN ANOTHER LANGUAGE / #25 COUNT THE SAME THING TWICE / #30 DO ONE SCALE, ONE DIRECTION AT A TIME.**

# R17 C071 — G0004: exact downshadow reformulation, Boolean-boundary dichotomy, and articulation-parallel reduction

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R17, HARD OUTSIDE.
Status: **OPEN / PARTIAL; three-run stuck trigger reached at the end of this run.**

## 0. Continuity, source, ownership, and metric

The canonical claim remains `operations/claims/G0004.md`: R17 is the exclusive owner of Lucas Flammant, *A finite-graph conjecture related to theta(p_c)=0 for Bernoulli bond percolation on Z^d*, arXiv:2609.03492v2, Conjecture 2.2. The original Chvátal--Sankoff binary-LCS target remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and D0064 remains terminal for R17 at `R_class=0/3`. Neither is reopened.

At run start I reread the controlling campaign index/ranking, root posting/queue surfaces, the new-methods policy, the direct G0004 claim, C069, C070, the R7-02 G0004 admission mathematics, indexed intake material, and current neighboring ownership/search records. I also used repository-wide search/tree indexing to check for a newer R17/G0004 report or a conflicting owner claim; none was found before this work. A fresh bounded web search on 2026-09-19 by exact arXiv id, title, and conjecture wording still returned arXiv:2609.03492v2 (dated 2026-09-04 in current metadata), with the general finite-graph statement presented as the conjecture and the outer-face planar theorem as the proved case. I found no later primary source claiming the full arbitrary-finite-graph conclusion. This is bounded negative evidence, not a worldwide openness or novelty certificate.

The fixed metric is unchanged:

\[
U_F:=\inf\Bigl\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under the full source quantifiers}\Bigr\}.
\]

Before: `U_F=1`. After: `U_F=1`.

C069 and C070 are inherited, not rederived: sharp star asymptotics, automorphism symmetrization, the exact fractional-selector dual, the heterogeneous independent-arm theorem, and root-neighborhood star domination.

## 1. Exact setup

Let `mu=mu_p` be Bernoulli bond percolation on a finite graph `G=(V,E)`, let `o` be the root and `B` the boundary. Write

\[
S(\omega)=\{b\in B:o\leftrightarrow b\},
\qquad C=\{S\ne\varnothing\}.
\]

After the exact R7-02 elimination of auxiliary randomness, an admissible adverse family is a collection of decreasing kernels

\[
q_b:\{0,1\}^E\to[0,1],
\qquad \mathbb E q_b\le\varepsilon,
\]

and the fixed-instance failure ratio is

\[
R(G,p,o,B;q)
=
\frac{\mathbb E[\mathbf1_C\min_{b\in S}q_b]}{\mathbb P(C)}.
\]

The source-wide supremum is `R_*(epsilon)`; Flammant Conjecture 2.2 is equivalent to `R_*(epsilon)->0`.

## 2. Method #18 — exact Boolean-lattice downshadow formulation

The selector dual in C070 is exact but still phrased as an optimization over fractional selectors. Thresholding the kernels produces a second exact formulation in which the connectivity-specific obstruction is visible directly in the Boolean lattice.

For a decreasing set `F subseteq {0,1}^E` and a boundary vertex `b`, define its **connectivity downshadow**

\[
\operatorname{Sh}_b(F)
:=\downarrow(F\cap C_b),
\qquad C_b:=\{o\leftrightarrow b\},
\]

where

\[
\downarrow A:=\{\eta:\exists\omega\in A\text{ with }\eta\le\omega\}.
\]

### Theorem 2.1 (exact threshold/downshadow equivalence)

Fix a finite percolation instance and `delta in [0,1]`. Let

\[
T_G(\delta)
:=
\sup_{\substack{D_b\downarrow\\ \mu(D_b)\le\delta}}
\frac{\mu\{\omega\in C:\omega\in D_b\ \forall b\in S(\omega)\}}{\mu(C)}.
\]

Then

\[
\boxed{
T_G(\delta)
=
\sup_{\substack{F\downarrow,\ C^c\subseteq F\\
\mu(\operatorname{Sh}_b(F))\le\delta\ \forall b}}
\frac{\mu(F\cap C)}{\mu(C)}.
}
\]

#### Proof

Start from decreasing bad sets `(D_b)`, and define

\[
A_D:=\{\omega\in C:\omega\in D_b\text{ for every }b\in S(\omega)\},
\qquad F_D:=C^c\cup A_D.
\]

`F_D` is decreasing. Indeed, if `omega in A_D` and `eta<=omega`, then either `eta notin C`, or `S(eta) subseteq S(omega)` and decreasingness of every `D_b` gives `eta in D_b` for every `b in S(eta)`.

For each `b`,

\[
F_D\cap C_b=A_D\cap C_b\subseteq D_b.
\]

Since `D_b` is decreasing,

\[
\operatorname{Sh}_b(F_D)=\downarrow(F_D\cap C_b)\subseteq D_b,
\]

so `mu(Sh_b(F_D))<=delta`, and the objective is `mu(F_D cap C)/mu(C)=mu(A_D)/mu(C)`.

Conversely, let `F` be decreasing, contain `C^c`, and satisfy the shadow constraints. Put

\[
D_b:=\operatorname{Sh}_b(F).
\]

If `omega in F cap C` and `b in S(omega)`, then `omega in F cap C_b subseteq D_b`, so `omega` is a threshold failure. If `omega in C\F` and `b in S(omega)`, then `omega notin D_b`: otherwise there would be `x in F cap C_b` with `omega<=x`, and the downset property of `F` would force `omega in F`, a contradiction. Hence the threshold failure set is exactly `F cap C`. This proves both inequalities and the formula. `square`

This is source-specific. The full threshold problem is no longer “many rare downsets indexed by boundary points”; it is one downset `F` containing disconnection, together with the requirement that every connectivity-generated downshadow of `F` be rare.

### Corollary 2.2 (source-equivalent threshold compression)

Let

\[
T_*(\delta):=\sup_G T_G(\delta)
\]

with the same full source supremum over all finite instances, and set `T_*(delta)=1` for `delta>=1`. Then

\[
T_*(\varepsilon)\le R_*(\varepsilon)
\]

and

\[
R_*(\varepsilon)
\le
\int_0^1
T_*\!\left(\min\left\{1,\frac{\varepsilon}{t}\right\}\right)\,dt.
\]

Consequently

\[
\boxed{R_*(\varepsilon)\to0\quad\Longleftrightarrow\quad T_*(\delta)\to0.}
\]

#### Proof

For the first inequality, take `q_b=1_{D_b}`. For the second, use layer cake:

\[
\min_{b\in S}q_b
=
\int_0^1
\mathbf1\{q_b\ge t\ \forall b\in S\}\,dt.
\]

The threshold set `D_b(t)={q_b>=t}` is decreasing and Markov gives

\[
\mu(D_b(t))\le\min\{1,\varepsilon/t\}.
\]

Apply Theorem 2.1 at every `t`, divide by `mu(C)`, and integrate. If `T_*(delta)->0`, dominated convergence gives `R_*(epsilon)->0`; the reverse implication follows from `T_*<=R_*`. `square`

Thus the exact remaining source problem can be written as one Boolean-lattice statement:

\[
\boxed{
\sup_{G,p,o,B}
\sup_{\substack{F\downarrow,\ C^c\subseteq F\\
\mu(\downarrow(F\cap C_b))\le\delta\ \forall b}}
\frac{\mu(F\cap C)}{\mu(C)}
\xrightarrow[\delta\downarrow0]{}0.
}
\]

That is the cleanest exact blocker I have obtained so far.

### Lemma 2.3 (connectivity contact supports are union-closed)

For `0<p<1`, the support

\[
\mathcal S:=\{S(\omega):\omega\in\{0,1\}^E\}
\]

of boundary-contact sets is closed under unions.

#### Proof

Let `S_1,S_2` be realized by configurations whose root clusters have vertex sets `K_1,K_2`. Each `K_i` is connected and contains `o`, hence `K:=K_1 union K_2` is connected. Open a spanning tree of `G[K]` and close every edge from `K` to `V\K`. The root cluster is then exactly `K`, so its boundary trace is

\[
B\cap K=(B\cap K_1)\cup(B\cap K_2)=S_1\cup S_2.
\]

Every finite configuration has positive product probability when `0<p<1`. The degenerate `p=0,1` cases are trivial. `square`

This elementary structural constraint cleanly separates genuine connectivity from the source's arbitrary-increasing-event surrogate. For example, with independent gate bits `g_1,...,g_N`, the increasing events

\[
A_i=\{g_j=1\text{ for every }j\ne i\}
\]

have support `emptyset`, the singletons, and `B`; for `N>=3` this support is not union-closed. Taking the rare decreasing sets `D_i={g_i=0}` makes failure occur whenever exactly one gate is closed, and the conditional failure ratio is

\[
\frac{N\delta}{1-\delta+N\delta},
\]

which can tend to one while `delta->0`. This is a diagnostic reconstruction of the arbitrary-increasing-event obstruction, not a claim that it is literally the source's displayed counterexample. Connectivity cannot realize this exact support table for `N>=3`.

Union-closedness by itself is only qualitative: it forces intermediate contact sets to exist, but gives no lower bound on their product probability. Quantifying that forced interpolation is one of the remaining difficulties.

## 3. Method #25 — count the Boolean boundary two ways

The downshadow language gives an exact local charging statement for every edge leaving a bad downset.

Use the canonical threshold representation from Theorem 2.1, so `D_b=Sh_b(F)` and the bad set is `F cap C`. Let `x in F` and let `e` be closed in `x`; write `y=x+e`. Suppose

\[
y\notin F.
\]

Because `C^c subseteq F`, necessarily `y in C`. Since `y` is not bad, there is some `b in S(y)` with `y notin D_b`.

### Lemma 3.1 (exit-edge dichotomy)

Every upward Boolean-lattice edge `x -> y=x+e` leaving `F` can be charged to at least one boundary vertex `b` for which exactly one of the following mechanisms occurs:

1. **bad-set boundary exit:** `b in S(x)` and
   \[
   x\in D_b,\qquad y\notin D_b;
   \]
   thus opening `e` crosses the upward boundary of the rare downset `D_b`;
2. **connectivity pivot:** `b notin S(x)` and `b in S(y)`;
   thus `e` is pivotal for the connectivity event `C_b` at `x`.

#### Proof

Choose `b in S(y)` with `y notin D_b`. If `b in S(x)`, then `x in F cap C_b subseteq Sh_b(F)=D_b`, giving case 1. Otherwise opening `e` changes `C_b` from false to true, giving case 2. `square`

In particular, if `m` is maximal in the downset `F`, then every closed edge of `m` is an exit edge and therefore receives one of these two charges. This counts the same Boolean boundary in two languages: rare-downset exits or newly-created connectivity.

This is exactly where the general proof currently stops. Small measure `mu(D_b)<=delta` does **not** control the total edge boundary/influence of `D_b` uniformly in graph size, while a single pivotal edge can create many boundary connections at once. The missing global inequality would have to fractionally charge these two mechanisms without paying either `|E|` or `|B|`. C070's independent-arm proof succeeds precisely because each coordinate has one canonical boundary label; Lemma 3.1 shows what replaces that label in a general graph and why it is multivalued.

The lemma also sharpens the failure of the naive co-singleton counterexample route. The arbitrary-event gate model above tries to create `N` essentially disjoint singleton bad modes with no two-point intermediate contact state. Lemma 2.3 forbids that exact connectivity support, while Lemma 3.1 says that any attempted approximation must pay either rare-set boundary exits or actual connectivity pivots between the modes. What is not yet proved is a dimension-free lower bound on that payment.

## 4. Method #30 — one articulation and one independent direction at a time

C070 treated genuine independent arms and also graphs whose boundary already contains the entire root neighborhood. A different decomposable class remains exactly reducible even when every branch has arbitrary internal, possibly nonplanar, topology.

### Theorem 4.1 (serial-stem / parallel one-terminal modules)

Suppose the edge set decomposes disjointly as

\[
E=E_0\sqcup E_1\sqcup\cdots\sqcup E_m
\]

with the following geometry.

- `H_0=(V_0,E_0)` contains `o` and an articulation vertex `v`.
- For `i>=1`, `H_i=(V_i,E_i)` meets the rest of the graph only at `v` and contains one designated boundary vertex `b_i`.
- `B={b_1,...,b_m}`, and every `o-b_i` path consists of a path from `o` to `v` in `H_0` followed by a path from `v` to `b_i` in `H_i`.

The branch graphs may otherwise be arbitrary finite graphs or multigraphs. Then for every admissible global decreasing kernel family and every `0<epsilon<=1/2`,

\[
\boxed{
R(G,p,o,B;q)
\le
4\varepsilon\log^2\frac1\varepsilon
+7\varepsilon\log\frac1\varepsilon
+2\varepsilon.
}
\]

Hence this entire articulation-parallel class satisfies Flammant's qualitative conclusion uniformly in the number, size, reliability, and nonplanar topology of the modules.

#### Proof

Let

\[
A=\{o\leftrightarrow v\text{ in }H_0\},
\qquad
X_i=\mathbf1_{\{v\leftrightarrow b_i\text{ in }H_i\}}.
\]

The edge blocks are disjoint, so `A,X_1,...,X_m` are independent, and the `X_i` are Bernoulli with arbitrary parameters `r_i=P(X_i=1)`. Moreover

\[
C=A\cap\{K>0\},\qquad K:=\sum_iX_i.
\]

If `P(A)=0` there is nothing to prove. Otherwise, for every `i` and every branch-status vector `x`, define

\[
\bar q_i(x):=\mathbb E[q_i\mid A, X=x].
\]

First, the budget survives conditioning on the serial stem. Since `A` is increasing and `q_i` is decreasing, Harris--FKG gives

\[
\mathbb E[q_i\mid A]\le\mathbb E q_i\le\varepsilon.
\]

Hence `E_X bar q_i(X)<=epsilon`.

Second, `bar q_i` is coordinatewise decreasing in `x`. Fix all branch indicators except `X_j`. After averaging over the stem under `A` and all other branch blocks under their fixed indicator conditions, the remaining conditional integrand is still a decreasing function of the edge configuration in branch `j`. In a product measure, conditioning on the increasing event `{X_j=1}` stochastically dominates conditioning on its complement: for every decreasing function `h`, Harris--FKG implies

\[
\mathbb E[h\mid X_j=1]\le \mathbb E[h\mid X_j=0].
\]

Thus changing `x_j` from `0` to `1` cannot increase `bar q_i(x)`.

Finally, condition on `A` and `X`. Concavity of the minimum gives

\[
\mathbb E\left[
\min_{i:X_i=1}q_i\mid A,X
\right]
\le
\min_{i:X_i=1}\bar q_i(X).
\]

Therefore

\[
\mathbb E\left[\mathbf1_C\min_{i:X_i=1}q_i\right]
\le
\mathbb P(A)
\mathbb E_X\left[
\mathbf1_{\{K>0\}}\min_{i:X_i=1}\bar q_i(X)
\right].
\]

Also `P(C)=P(A)P(K>0)`. Cancelling the stem factor reduces the ratio exactly to the heterogeneous independent-arm problem of C070, with the feasible decreasing kernels `(bar q_i)`. C070 Theorem 3.1 gives the displayed bound. `square`

This theorem is not subsumed by a star calculation: every module can contain arbitrary cycles and nonplanar structure, and the common serial stem can itself be arbitrary. What makes the reduction work is a genuine one-directional decomposition across a single articulation, not local degree.

## 5. What moved mathematically, and what did not

New results in this run:

1. an exact threshold/downshadow variational formula for every finite instance;
2. a proof that the full source conjecture is equivalent to decay of the resulting source-wide Boolean-lattice shadow functional `T_*(delta)`;
3. the union-closed support lemma for genuine root-cluster boundary traces, ruling out the exact co-singleton support mechanism behind a natural arbitrary-increasing-event obstruction;
4. an exact exit-edge dichotomy charging every bad-downset boundary edge either to a rare-kernel boundary crossing or to a connectivity pivotal;
5. a uniform `O(epsilon log^2(1/epsilon))` theorem for arbitrary serial-stem / parallel one-terminal module graphs, with completely arbitrary internal module topology.

These are source-valid structural/restricted advances, but none gives a dimension-free bound on the downshadow functional for **all** finite graphs. Therefore the strict source-wide metric remains

\[
U_F:1\longrightarrow1.
\]

No finite numerical enumeration is promoted here, so no exact-arithmetic checker artifact is added. Every theorem-sized claim above has a proof on the page.

## 6. Three-run stuck trigger and the exact remaining obligation

This is the third consecutive substantive G0004 run with no movement of the fixed source metric:

- C069: `U_F 1 -> 1`;
- C070: `U_F 1 -> 1`;
- C071: `U_F 1 -> 1`.

Therefore Section I is now triggered. **The next R17 run on G0004 must be a stuck thinking run, not a fourth ordinary lemma run.** The exact blocking statement is

\[
\boxed{
T_*(\delta)
=
\sup_{G,p,o,B}
\sup_{\substack{F\downarrow,\ C^c\subseteq F\\
\mu(\downarrow(F\cap C_b))\le\delta\ \forall b}}
\frac{\mu(F\cap C)}{\mu(C)}
\xrightarrow[\delta\downarrow0]{}0.
}
\]

C069--C071 now explain three things a successful proof has to do simultaneously:

- exploit the minimum over many connected boundary vertices without paying a contact-count factor;
- quantify the connectivity-specific interpolation that the union-closed support lemma only detects qualitatively;
- globally charge the Lemma 3.1 Boolean boundary without paying total rare-set influence or the number of newly connected boundary vertices.

The next stuck report must contain the owner's full five-part diagnosis and choose exactly one permitted recovery action. No recovery is consumed by C071 itself; `recovery_count` remains `0`. A fresh next-run method triple is reserved as **#1 CHANGE THE CATEGORY / #12 FIND WHAT IS CONSERVED / #22 READ THE FAILURES, NOT THE SUCCESSES**. It is intentionally different from all three substantive G0004 triples already used.

## 7. Model / scheduler-control status

The exposed task-management schema in this runtime still has schedule/prompt/title/enablement/timing controls but no bindable model-family field, no reasoning-effort field, and no authenticated runtime-model attestation. Hence `GPT-6 / maximum` remains a prompt request only; this run must honestly report `GPT-5.6 Sol / UNVERIFIED`.

The historical `You cannot modify this task` result for P26 is an authorization-context boundary. The valid workaround remains the owning/admin-authorized scheduler context or platform support. Duplicating a task, editing repository files, or attempting a permission bypass is not a scheduler repair.

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
    before: 2
    after: 3
  section_I_stuck_triggered: true
  methods_tried: [18, 25, 30]
  results:
    - exact threshold/downshadow variational equivalence
    - source-equivalent threshold compression R_* <-> T_*
    - union-closed connectivity-contact support lemma
    - Boolean exit-edge rare-boundary/connectivity-pivotal dichotomy
    - serial-stem / parallel one-terminal module theorem
  source_closed: false
  recovery_count:
    before: 0
    after: 0
  next_run_type: SECTION_I_STUCK_THINKING
  next_methods: [1, 12, 22]
  shared_root_edits: false
  peer_file_edits: false
  artifacts_added: false
```
