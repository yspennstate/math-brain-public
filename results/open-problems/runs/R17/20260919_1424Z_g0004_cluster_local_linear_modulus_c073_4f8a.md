Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; STUCK RECOVERY 1/2 EXECUTED with a new restricted theorem `phi(epsilon)=1-epsilon` for heterogeneous cluster-measurable boundary observables; methods #3 PROVE SOMETHING STRONGER / #15 BREAK THE SYMMETRY ON PURPOSE / #27 SWAP THE QUANTIFIERS.**

# R17 C073 — G0004 recovery 1: heterogeneous cluster-local observables have the sharp linear modulus

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R17, HARD OUTSIDE.
Status: **OPEN / PARTIAL / STUCK RECOVERY 1/2**.

## 0. Continuity and owner checks

The canonical claim `operations/claims/G0004.md` still names R17 as exclusive owner of Lucas Flammant's finite-graph percolation Conjecture 2.2. The predecessor Chvatal--Sankoff binary-LCS source remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and the later Rhodes--Vargas D0064 source remains terminal at `R_class=0/3`. Neither predecessor is reopened.

At run start I reread `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the G0004 claim, C069--C072, current neighboring G0004 admission screens, and the G-intake identity. A direct compare from C072 commit `2eee8ab2d442072a9b810c8b17f940559345891f` to then-current `master` showed 119 intervening commits but no replacement or release of `operations/claims/G0004.md` and no newer R17 report.

The fixed source-wide metric remains

\[
U_F:=\inf\left\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under the full source quantifiers}\right\}.
\]

Before: `U_F=1`. After: `U_F=1`.

This run executes the one recovery action selected in C072: **port the conditioned-slack / first-relay machinery from the nearest solved-looking finite-graph gluing problem.** It is not a second stuck declaration; the recovery counter remains `1/2`.

## 1. Fresh source and dependency status

A fresh 2026-09-19 check of arXiv:2609.03492 still presents Conjecture 2.2 as the arbitrary-finite-graph statement and explicitly says the general conjecture remains open. The source's quantifiers permit extra randomness: an event `E_b` is called increasing when

\[
f_b(\omega):=\mathbb P(E_b\mid\pi=\omega)
\]

is increasing on the edge cube. The source proves only the outer-face planar case, with `phi(epsilon)=1-2 sqrt(epsilon)`, and its Section 2.1 shows that connectivity cannot simply be replaced by arbitrary increasing events.

For the recovery I use one imported theorem from the pinned mechanically checked artifact

`anthropics/formal-math @ 795efb86f191735c5481675763537cfb4ff37e55`.

The exact Lean source `percolation/Percolation/Continuity/AdditiveGluing/GenOfSurplusTransfer.lean` proves the following **GEN / first-relay inequality** for any finite weighted graph. For every increasing nonnegative cluster functional `F`, relay set `A`, origin `o`, and rank of relays compatible with

\[
m_a:=\mathbb E F(C_a),
\]

if `P_a^o` is the event that `a` is the first relay of `A` in `C_o`, then

\[
\boxed{
\mathbb E[F(C_o);\ o\leftrightarrow A]
\ge \sum_{a\in A}\mathbb P(P_a^o)\,\mathbb E F(C_a).
}
\tag{GEN}
\]

The `P_a^o` partition `{o<->A}`. The pinned artifact is machine checked but expressly not independently refereed; I therefore record GEN as an imported mechanically checked dependency, not as an R17 novelty and not as an independent audit.

A bounded prior-art search on 2026-09-19 for Flammant + cluster-local/cluster-functional variants found the source itself and expositions of the GEN/additive-gluing artifact, but no statement matching the heterogeneous cluster-local theorem below. This is bounded negative evidence only, not a novelty certificate.

## 2. New idea before code

The C072 recovery target allowed a different cluster observable for each boundary vertex. At first sight GEN seems unusable because it accepts **one** common functional `F`, whereas Flammant gives a family `(f_b)`.

The key move is to swap the order of those choices. Instead of selecting a boundary vertex and then using its functional, first combine all boundary functionals into the common envelope

\[
F(K):=\max_{b\in B\cap K}F_b(K),
\qquad \max\varnothing:=0.
\tag{2.1}
\]

Then use GEN on this single `F`. This is method #27 in a literal form: the family of boundary labels is absorbed *before* the first-relay quantifier is resolved.

The envelope is monotone even when the graph and the `F_b` are completely asymmetric. This is method #15: there is no automorphism averaging and no common observable assumption.

Finally the conclusion is stronger than the qualitative source target on this subclass: the modulus is exactly the linear lower bound `1-epsilon`, not merely some function tending to one. This is method #3.

## 3. Theorem — cluster-measurable Flammant events have `phi(epsilon)=1-epsilon`

### Statement

Consider the exact setting of Flammant Conjecture 2.2: a finite undirected loopless multigraph, iid Bernoulli bond percolation `pi` with `p in (0,1)`, origin `o`, finite boundary `B`, and events `(E_b)_{b in B}` on a probability space which may contain auxiliary randomness. Put

\[
f_b(\omega)=\mathbb P(E_b\mid\pi=\omega).
\]

Assume, in addition to the source hypotheses, that for every `b`, `f_b` is measurable with respect to the **vertex set of the open cluster** `C_b(omega)`; equivalently, configurations with the same `b`-cluster vertex set have the same value of `f_b`. Suppose

\[
f_b\text{ is increasing on }\{0,1\}^E,
\qquad \mathbb P(E_b)=\mathbb E f_b\ge1-\varepsilon.
\]

Then

\[
\boxed{
\mathbb P\!\left[\bigcup_{b\in B}
\bigl(\{o\leftrightarrow b\}\cap E_b\bigr)\right]
\ge (1-\varepsilon)\,\mathbb P(o\leftrightarrow B).
}
\tag{3.1}
\]

Thus the full Flammant conclusion holds on this subclass with the universal modulus

\[
\boxed{\varphi(\varepsilon)=1-\varepsilon.}
\]

The theorem permits arbitrary finite graphs, arbitrary `p`, unbounded `|B|`, arbitrary asymmetry, a different observable for every boundary vertex, and arbitrary dependence among the auxiliary events `(E_b)`.

### Proof, Step 1: turn cluster measurability into an increasing cluster functional

Fix `b`. Since `p in (0,1)`, every deterministic edge configuration has positive probability, so `f_b(omega)` is pointwise defined by the source convention. Cluster measurability gives a function `g_b(K)` on the connected vertex sets `K` containing `b` which occur as `C_b(omega)`.

If two such connected sets satisfy `K subset L`, choose a deterministic configuration `omega_K` whose only open edges are a connected spanning subgraph of `K`, and a configuration `omega_L >= omega_K` obtained by opening enough additional edges to connect every vertex of `L` while leaving every edge from `L` to its complement closed. Then

\[
C_b(\omega_K)=K,\qquad C_b(\omega_L)=L.
\]

Because `f_b` is increasing on configurations,

\[
g_b(K)\le g_b(L).
\tag{3.2}
\]

Extend `g_b` to every vertex set by

\[
F_b(A):=\max\{g_b(K): b\in K\subseteq A,\ K\text{ connected}\},
\tag{3.3}
\]

with value zero if the set in braces is empty. Then `F_b` is increasing in `A`. If `A=C_b(omega)`, (3.2) shows every connected `K subset A` containing `b` has `g_b(K)<=g_b(A)`, while `K=A` is allowed, hence

\[
F_b(C_b(\omega))=g_b(C_b(\omega))=f_b(\omega).
\tag{3.4}
\]

So every cluster-measurable source observable has an increasing vertex-cluster representation.

### Proof, Step 2: form one common envelope

Define `F` by (2.1). If `K subset L`, then for every `b in B cap K`,

\[
F_b(K)\le F_b(L)\le \max_{c\in B\cap L}F_c(L),
\]

and therefore `F(K)<=F(L)`. Thus `F` is an increasing nonnegative cluster functional with `0<=F<=1`.

For every boundary relay `b`, the vertex `b` always belongs to its own cluster, so

\[
F(C_b)\ge F_b(C_b)=f_b.
\]

Consequently

\[
m_b:=\mathbb E F(C_b)
\ge \mathbb E f_b
=\mathbb P(E_b)
\ge1-\varepsilon.
\tag{3.5}
\]

### Proof, Step 3: apply the first-relay inequality

Apply GEN with relay set `B`, origin `o`, and the common functional `F`. Choose any rank compatible with the means `(m_b)`. Since the first-relay events partition `{o<->B}`, (3.5) gives

\[
\begin{aligned}
\mathbb E[F(C_o);\ o\leftrightarrow B]
&\ge \sum_{b\in B}\mathbb P(P_b^o)m_b\\
&\ge(1-\varepsilon)\sum_{b\in B}\mathbb P(P_b^o)\\
&=(1-\varepsilon)\mathbb P(o\leftrightarrow B).
\end{aligned}
\tag{3.6}
\]

### Proof, Step 4: the envelope is pointwise dominated by conditional success

Fix a percolation configuration `omega` with `o<->B`, and write

\[
S(\omega)=B\cap C_o(\omega).
\]

For every `b in S(omega)`, connected vertices have the same open cluster, so `C_b(omega)=C_o(omega)`. Hence by (3.4),

\[
F(C_o(\omega))
=\max_{b\in S(\omega)}F_b(C_o(\omega))
=\max_{b\in S(\omega)}f_b(\omega).
\tag{3.7}
\]

Condition on `pi=omega`. Connectivity is then deterministic, while the auxiliary events may be arbitrarily dependent. Nevertheless the probability of their union dominates the largest marginal:

\[
\begin{aligned}
&\mathbb P\!\left[
\bigcup_{b\in B}(\{o\leftrightarrow b\}\cap E_b)
\,\middle|\,\pi=\omega\right]\\
&\qquad=\mathbb P\!\left[\bigcup_{b\in S(\omega)}E_b\,\middle|\,\pi=\omega\right]
\ge\max_{b\in S(\omega)}f_b(\omega)
=F(C_o(\omega)).
\end{aligned}
\tag{3.8}
\]

For configurations with `o not<->B`, both sides contribute zero after multiplication by the connection indicator. Integrating (3.8) and applying (3.6) proves (3.1). QED.

### Dependency / audit label

The proof above is complete after importing GEN. GEN is not an R17 claim: I verified its exact finite-graph theorem signature in the pinned Lean file and the artifact reports successful kernel checking, but the artifact has not been independently refereed. Accordingly this run records the result as **PARTIAL / restricted theorem with a pinned mechanically checked external dependency**, not as source closure.

## 4. Method #15 also breaks the most tempting extension: cluster projection is not monotone

The theorem suggests projecting a general increasing source observable `f_b(omega)` onto the cluster `C_b`. That reduction is false even on a two-edge path.

Take the path

\[
b\;--e_1--\;x\;--e_2--\;y
\]

with iid edge probability `p=3/4`, and the increasing observable

\[
f(\omega)=\mathbf 1_{\{e_2\text{ open}\}}.
\]

Let

\[
g(K):=\mathbb E[f\mid C_b=K].
\]

Then

\[
\begin{array}{c|c|c}
K & \mathbb P(C_b=K) & g(K)\\ \hline
\{b\} & 1/4 & 3/4\\
\{b,x\} & 3/16 & 0\\
\{b,x,y\} & 9/16 & 1.
\end{array}
\]

Thus

\[
\{b\}\subset\{b,x\}
\quad\text{but}\quad
 g(\{b\})=3/4>0=g(\{b,x\}).
\tag{4.1}
\]

The reason is exact: observing `C_b={b,x}` certifies that `e_2` is closed, while observing `C_b={b}` leaves `e_2` independent. Therefore ordinary conditional expectation onto the vertex-cluster sigma-field destroys monotonicity.

This finite claim was checked with exact rational arithmetic, not simulation:

- `artifacts/R17/20260919T1423Z_g0004_cluster_projection_counterexample_c073.py`
- `artifacts/R17/20260919T1423Z_g0004_cluster_projection_counterexample_c073.out`

The archived execution ends `EXACT_COUNTEREXAMPLE_PASS`.

## 5. What this changes about the blocker

C072 asked whether the conditioned-slack machinery could handle a family of different boundary observables. For **cluster-local** observables, the answer is unexpectedly clean: no label-dependent extension of CSH is needed. The max-envelope (2.1) converts the heterogeneous family into one common increasing cluster functional, and the already-proved first-relay theorem does the rest.

Therefore the full G0004 obstruction is now narrower than C072 stated. It is not heterogeneity of the labels by itself. The obstruction is the genuinely **non-cluster-local information** in an arbitrary increasing conditional probability `f_b(omega)`: an increasing event may inspect edges whose states are not determined by the vertex set `C_b`, and the exact path witness (4.1) shows that projecting this information onto `C_b` can reverse monotonicity.

The source-wide downshadow blocker from C071 remains

\[
T_*(\delta)=
\sup_{G,p,o,B}
\sup_{\substack{F\downarrow,\ C^c\subseteq F\\
\mu(\downarrow(F\cap C_b))\le\delta\ \forall b}}
\frac{\mu(F\cap C)}{\mu(C)}
\xrightarrow[\delta\downarrow0]{}0.
\tag{5.1}
\]

The present theorem does not imply (5.1) for arbitrary edge-cube observables, so the strict metric remains `U_F=1`.

## 6. Method-by-method outcome

### #3 PROVE SOMETHING STRONGER

Succeeded on the C072 recovery subclass. Instead of merely proving a qualitative modulus `phi(epsilon)->1`, the theorem gives the linear source-normalized estimate

\[
\phi(\varepsilon)=1-\varepsilon.
\]

It also upgrades C072's explicit-representation hypothesis to the intrinsic assumption that the source conditional probability is measurable with respect to `C_b`; monotonicity then constructs the increasing cluster functional automatically.

### #15 BREAK THE SYMMETRY ON PURPOSE

Succeeded in two ways. The theorem allows a completely different `F_b` for every boundary vertex and arbitrary asymmetric graphs; the common envelope removes the need for automorphisms. The same method was then used adversarially to test the obvious extension, producing the exact two-edge counterexample (4.1) to monotonicity of cluster projection.

### #27 SWAP THE QUANTIFIERS

Succeeded. The decisive step is to combine all boundary observables into `F=max_b F_b` **before** selecting the first relay. GEN can then use one common functional, while the pointwise maximum at the connected cluster recovers the best boundary-specific conditional success probability.

## 7. Recovery accounting and next route

This is the substantive execution of **stuck recovery 1/2**, not recovery 2. It proves the simplest special case selected in C072 and exposes a sharper obstruction, but because the source-wide fixed metric did not move, G0004 remains OPEN / PARTIAL.

The next run must not repeat the current triple. Reserve the fresh, previously unused G0004 methods:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** interpolate an arbitrary increasing `f_b` between its full edge-cube value and a cluster-local surrogate by resampling / sprinkling the edges not certified by `C_b`; identify a derivative controlled by pivotal information;
- **#13 FIND WHAT ONLY INCREASES:** look for a residual-information potential under cluster exploration whose loss is monotone and which can be charged without `|B|` or `|E|`;
- **#28 REPLACE FOR ALL WITH FOR TYPICAL:** first prove that outside a quantitatively small exceptional set of cluster realizations the non-cluster-local residual can be dominated by a monotone cluster functional, then determine whether the exceptional mass can be made `o(P(o<->B))` uniformly.

The immediate target is no longer a label-dependent CSH. It is a decomposition

\[
f_b(\omega)=\text{cluster-local monotone part}+\text{residual}
\]

in which the residual admits a dimension-free aggregate bound. The exact path witness says any such decomposition must retain information about unrevealed / boundary-edge states; plain conditional expectation on `C_b` cannot be it.

## 8. Structured ledger delta

```yaml
ledger_delta:
  track: R17
  source_id: G0004
  source: "Flammant arXiv:2609.03492v2, Conjecture 2.2"
  status_before: "OPEN / PARTIAL / STUCK RECOVERY 1/2"
  status_after: "OPEN / PARTIAL / STUCK RECOVERY 1/2"
  metric: U_F
  value_before: 1
  value_after: 1
  movement: "NO SOURCE-METRIC MOVEMENT"
  methods_attempted: [3, 15, 27]
  recovery_action: "port conditioned-slack / GEN first-relay machinery"
  recovery_result: "SUCCESS on selected cluster-measurable subclass; full source unresolved"
  new_restricted_theorem:
    name: "heterogeneous cluster-measurable Flammant theorem"
    conclusion: "success probability >= (1-epsilon) P(o<->B)"
    modulus: "phi(epsilon)=1-epsilon"
    scope: "arbitrary finite graph, p, o, unbounded B; different cluster-measurable increasing conditional success functional for each b; arbitrary auxiliary dependence"
    dependency: "GEN at anthropics/formal-math@795efb86f191735c5481675763537cfb4ff37e55; mechanically checked, not independently refereed"
  new_exact_obstruction:
    statement: "conditional projection of an increasing edge observable onto C_b need not be monotone"
    witness: "two-edge path, p=3/4, f=1{e2 open}: g({b})=3/4 > g({b,x})=0"
    checker: "artifacts/R17/20260919T1423Z_g0004_cluster_projection_counterexample_c073.py"
    output: "artifacts/R17/20260919T1423Z_g0004_cluster_projection_counterexample_c073.out"
  predecessor_binary_lcs_width: 0.033609950762282626
  predecessor_d0064_R_class: "0/3"
  next_methods: [5, 13, 28]
  shared_root_edits: none
  peer_file_edits: none
  email_drive_public_scheduler_permission_workflow_actions: none
```

## 9. Model / scheduler control remains unresolved at the platform level

The scheduler surface described by the controlling repository policy exposes title, prompt, schedule, timing mode and enablement, but no bindable model-family selector, reasoning-effort selector, or authenticated runtime-model telemetry. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable or attestable scheduler setting here. This run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED and does not claim otherwise.

The historical P26 `You cannot modify this task` result is an authorization-context restriction, not a mathematical issue. The repository records that P26 was subsequently updated from another authorized context. The valid remedies remain the owning/admin-authorized task surface or platform support; duplicating the task, changing repository text as a substitute for a native scheduler edit, or bypassing permissions is not permitted.

No shared root, canonical claim, peer file, email, Drive item, public posting, scheduler configuration, workflow, purchase, or permission was changed in this run.
