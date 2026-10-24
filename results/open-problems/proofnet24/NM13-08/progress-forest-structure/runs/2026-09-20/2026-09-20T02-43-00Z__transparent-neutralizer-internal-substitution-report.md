Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — arbitrary-edge transparent PF insertion and a non-series-parallel activity neutralizer

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted closure and application theorems below, pending later independent review.** The uniform-all-forests conjecture for arbitrary finite graphs remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and the new attack

The preceding NM13-08 work established three ingredients.

1. **Two-terminal substitution.** If an edge is replaced by a two-terminal gadget `A`, forest sums and Rayleigh differences factor through the terminal-disconnected/connected sums `D_A,C_A` and the interface quantity
   \[
   J_A(p)=D_A C_{A,p}-C_A D_{A,p}.
   \]
2. **Transparent unit substitution.** A PF/I-Rayleigh gadget with terminal activity `t_A=C_A/D_A=1` may replace an edge of an arbitrary unit-weight p-NC core without asking the core for an all-weight Rayleigh theorem.
3. **PF-Rayleigh macro calculus.** If only one distinguished virtual terminal edge is allowed to vary over `s>=0`, PF-Rayleigh is closed under terminal series and parallel composition. The port-deleted split atoms
   \[
   Q_n=(K_4\vee\overline{K_n})-01
   \]
   are PF-Rayleigh for every `n>=1`.

The newest companion NM13-04 report also enlarges the PF atom catalog to the port-deleted `K_5\vee\overline{K_n}` family. That is preserved and not duplicated here.

This run takes a different structural step. It proves that **transparent PF gadgets can be inserted into an arbitrary internal edge of an already PF two-terminal host, not just at the host's decomposition port, while preserving the host's external PF property and its external terminal activity exactly**. This is stronger than the earlier terminal series/parallel closure in the direction needed for recursive decoration.

The second step exploits a numerical coincidence that becomes exact algebra: the split atom `Q_7` has activity `25/7`. A PF network of activity `16/9` therefore neutralizes it in series to activity exactly `1`. The resulting transparent gadget contains a non-series-parallel split atom, so it can be inserted into **arbitrary unit-only p-NC cores** by the earlier transparent substitution theorem. Applying this to every wheel produces a new unbounded graph class that is neither the NM13-04 split family nor the earlier theta-only wheel expansion.

`POSTED.md` was checked through the current T07 material. No source-level closure or duplicate posted theorem is claimed. Novelty/priority of the exact internal-insertion lemma and neutralizer construction is **UNVERIFIED**.

## 1. Parent theorem before/after, kept separate from mechanism progress

For a finite graph `G=(V,E)`, let
\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]
At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** spanning forests, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-graph vertex order in repository continuity:** `9 -> 9`.  
**Counterexample-order lower bound:** `>=10 -> >=10`.

No finite-order source metric moves in this run.

The **mechanism scope** does move:

* before: terminal PF series/parallel composition, plus transparent series-parallel theta gadgets;
* after: arbitrary-internal-edge transparent insertion preserves PF-Rayleigh and terminal activity, and there is an explicit infinite family of **non-series-parallel transparent PF gadgets** obtained by neutralizing the split atom `Q_7`.

That new transparent family transfers directly to any unit-p-NC core, not merely to a core carrying a weighted/PF hypothesis.

## 2. Exact recovered source/P14/literature scope

Only dependencies needed for this argument were reread.

### Grimmett–Winkler

Grimmett and Winkler, `math/0302185`, *Negative association in uniform forests and connected graphs* (Random Structures & Algorithms 24 (2004), 444–460), study the uniform measure on **all forests**. They report numerical verification for every graph with at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree negative-association theorem from the uniform-forest conjecture.

### Preserved P14 continuation

Repository continuity from P14/HARD10 completes the complementary dense nine-vertex sector, so every simple graph through nine vertices is certified at unit forest weights. P14 also preserves:

* block/direct-sum factorization, reducing a vertex-minimal counterexample to 2-connected;
* a two-separator transfer together with the fixed-graph balanced-to-weighted implication, reducing a vertex-minimal counterexample further to 3-connected;
* exact one-edge-field quadratics;
* failures of the generic degree-three star/mesh mixed-polarization route, the reverse-Cauchy sufficient inequality, and naive Lorentzian/stability shortcuts.

This run does not revive those failed universal claims.

### Erickson and later work

Erickson, `arXiv:1008.3660`, proves a sum-of-squares theorem for the spanning-forest Rayleigh difference of series-parallel graphs and works with the stronger **I-Rayleigh** condition in which all positive edge weights may vary. Earlier I-Rayleigh two-sum closure cited there is also stronger in weight scope than the one-port PF property used here.

Huang, `arXiv:2311.00965`, treats arboreal-gas negative correlation in restricted settings and continues to describe the general problem as open.

Bado, DOI `10.1016/j.spl.2026.110960`, proves strict pairwise negative edge correlation for every wheel `W_m=K_1+C_m`, `m>=3`, under the uniform measure on all forests. This gives the all-parameter base class used in Section 7.

Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified complete-graph spanning-subgraph ensembles, including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`. That is not the arbitrary-graph, all-component uniform-forest law here.

Fresh bounded searches on 20 September 2026 did not surface the exact combination “transparent terminal activity + internal edge substitution + one-port Rayleigh + split-graph neutralizer.” This is negative evidence only, not a priority certificate.

## 3. Two-terminal notation

Let `A` be a two-terminal graph with terminals `u,v`, all real edges at unit weight. Write
\[
I_A=D_A+C_A,
\]
where `D_A` sums forests in which `u,v` are disconnected and `C_A` sums forests in which they are connected. Define
\[
t_A=\frac{C_A}{D_A},
\qquad
J_A(p)=D_A C_{A,p}-C_A D_{A,p}.
\]
The empty forest guarantees `D_A>0`.

Let `\widehat A(s)` be obtained by adjoining a virtual terminal edge of weight `s>=0`. Then
\[
I_{\widehat A(s)}=I_A+sD_A,
\qquad
\Delta_{\widehat A(s)}(p,g)=J_A(p),
\]
independently of `s`.

Recall: `A` is **PF-Rayleigh** if `\widehat A(s)` has every Rayleigh difference nonnegative for every `s>=0`, with every real edge frozen at weight `1`.

Call `A` **transparent** if
\[
t_A=1,
\quad\text{i.e.}\quad C_A=D_A.
\]

## 4. New closure/sign theorem: arbitrary internal transparent insertion preserves PF-Rayleigh

### Theorem `T07-PF-TRANSPARENT-INTERNAL-CLOSURE-08`

Let `Q` be a PF-Rayleigh two-terminal graph with external terminals `x,y`. Let `e=uv` be **any real edge of `Q`**, not necessarily a series/parallel decomposition edge. Let `A` be a PF-Rayleigh two-terminal graph with fresh interior and `t_A=1`. Replace `e` by `A`, identifying the terminals of `A` with `u,v`; call the resulting two-terminal graph `Q[e<-A]`.

Then:

1. `Q[e<-A]` is PF-Rayleigh with respect to the same external terminals `x,y`;
2. its external terminal activity is unchanged:
   \[
   t_{Q[e<-A]}=t_Q;
   \]
3. more precisely, for every external field `s>=0`, all Rayleigh signs split into exact nonnegative factors as in (4.3)–(4.5) below.

This allows transparent PF gadgets to decorate arbitrary internal edges recursively without changing the host's external activity.

### Proof

Fix `s>=0` and write
\[
H_s=\widehat Q(s),
\]
where the outer virtual edge `h=xy` has weight `s`. Delete the internal edge `e=uv` from `H_s` and call the remaining weighted graph `B_s`, viewed as a two-terminal graph with terminals `u,v`. Let
\[
D_B=D_{B_s},\qquad C_B=C_{B_s}.
\]
These are nonnegative weighted forest sums; `D_B>0`.

The substituted graph is the parallel union of `A` and `B_s` at `u,v`. A union of an `A`-forest and a `B_s`-forest is acyclic iff the two forests do **not both** connect `u` to `v`. Therefore
\[
I'=D_A(D_B+C_B)+C_A D_B.
\tag{4.1}
\]
For a gadget edge `p`, define `D_{A,p},C_{A,p}` in the obvious way, and analogously for an old edge `r` of `B_s`.

#### Old-edge / old-edge pairs

Because `C_A=D_A`, equation (4.1) becomes
\[
I'=D_A(C_B+2D_B).
\]
But `C_B+2D_B` is exactly the forest polynomial of `H_s=B_s+e` with the real edge `e` restored at weight `1`. This identity holds polynomially in every surviving old edge weight. Hence for any two old edges `r,k != e` (including the outer virtual edge `h` when relevant),
\[
\boxed{
\Delta_{Q[e<-A]}(r,k;s)
=D_A^2\Delta_Q(r,k;s)\ge0.
}
\tag{4.2}
\]
PF-Rayleigh of `Q` supplies the sign.

#### Gadget-edge / gadget-edge pairs

Rewrite (4.1) instead as
\[
I'=D_B\left[I_A+\frac{C_B}{D_B}D_A\right].
\]
Thus the environment presents the gadget with a single effective nonnegative port field
\[
t_B(s)=\frac{C_B}{D_B}\ge0.
\]
For gadget edges `p,q`, differentiation gives
\[
\boxed{
\Delta_{Q[e<-A]}(p,q;s)
=D_B^2\Delta_{\widehat A(t_B(s))}(p,q)\ge0.
}
\tag{4.3}
\]
PF-Rayleigh of `A` supplies the sign.

#### Gadget-edge / old-edge pairs

Differentiate (4.1) once in a gadget edge `p` and once in an old edge `r`. Direct cancellation yields
\[
\boxed{
\Delta_{Q[e<-A]}(p,r;s)
=J_A(p)J_{B_s}(r).
}
\tag{4.4}
\]
The exact symbolic cancellation is archived in the checker. Since adjoining `e` back to `B_s` at unit weight gives `H_s`,
\[
J_{B_s}(r)=\Delta_{H_s}(e,r).
\]
Also `J_A(p)` is the Rayleigh difference between `p` and the virtual port edge of `A`, independent of that port's weight. Hence
\[
\boxed{
\Delta_{Q[e<-A]}(p,r;s)
=J_A(p)\Delta_{H_s}(e,r)\ge0.
}
\tag{4.5}
\]
This includes the case `r=h`, the external virtual port edge.

Equations (4.2)–(4.5) cover every pair of edges in the completed substituted graph, for every `s>=0`. Therefore `Q[e<-A]` is PF-Rayleigh.

#### External terminal activity is exactly preserved

Refine the forest sum of `Q` by whether the **external** terminals `x,y` are disconnected or connected. For either external state `sigma in {D,C}`, the corresponding sum is affine in the internal edge weight `z_e`:
\[
F_\sigma(z_e)=a_\sigma+z_e b_\sigma.
\]
After replacing `e` by `A`, forests in the `a_sigma` class are paired with terminal-disconnected forests of `A`, while forests in the `b_sigma` class are paired with terminal-connected forests of `A`. Hence
\[
F'_\sigma=D_Aa_\sigma+C_Ab_\sigma
=D_A(a_\sigma+b_\sigma)
=D_AF_\sigma(1),
\]
because `C_A=D_A`. Thus both external sums scale by the same factor:
\[
D_{Q[e<-A]}=D_AD_Q,
\qquad
C_{Q[e<-A]}=D_AC_Q,
\]
and therefore
\[
\boxed{t_{Q[e<-A]}=t_Q.}
\tag{4.6}
\]
This completes the proof. QED.

### Why this adds something beyond the preceding SP macro theorem

The preceding PF theorem composes whole two-terminal objects at their **outer terminals** by series or parallel operations. The present theorem permits insertion into an **arbitrary internal real edge** of a PF host and proves that the host's original external port response survives unchanged. In particular, an atom may be decorated internally without redoing its one-port Rayleigh calculation.

## 5. Exact activity of the split-4 PF atoms and the special value `n=7`

Let
\[
H_n=K_4\vee\overline{K_n},
\qquad
Q_n=H_n-01,
\]
with terminals `0,1`. The preceding NM13-08 port-field theorem proves that every `Q_n` is PF-Rayleigh.

This run extracts an exact closed form for its activity. In the 15-state terminal-partition transfer,
\[
M=5I+N,\qquad N^4=0.
\]
Therefore every terminal-conditioned count is `5^n` times a polynomial in `n` of degree at most three. Exact evaluation of the fixed linear functionals gives
\[
\boxed{
D_n=5^{n-2}(8n^2+107n+350),
}
\tag{5.1}
\]
\[
\boxed{
C_n=5^{n-3}(16n^3+247n^2+1112n+1250).
}
\tag{5.2}
\]
The attached checker rebuilds all 15 states, verifies `N^4=0`, and verifies (5.1)–(5.2) exactly for `n=1,...,12`. Because the nilpotence gives the degree bound, four exact values already determine the degree-3 expression; the additional values are overdetermined readback checks rather than heuristic interpolation.

At the special value `n=7`,
\[
D_7=4,659,375,
\qquad
C_7=16,640,625,
\]
so
\[
\boxed{
t_{Q_7}=\frac{C_7}{D_7}=\frac{25}{7}.}
\tag{5.3}
\]
This rational value is the input to the neutralizer construction.

## 6. New transparent non-series-parallel PF gadget factory

The earlier theta construction gives, for every integer `ell>=2`, a transparent PF gadget `U_ell`:

* take `r_ell=2^ell-1` internally disjoint paths of length `ell` in parallel;
* one length-`ell` path has
  \[
  D=2^\ell-1,\qquad C=1,\qquad t=\frac1{2^\ell-1};
  \]
* parallel activities add, hence
  \[
  t_{U_\ell}=r_\ell\frac1{r_\ell}=1.
  \]

Each `U_ell` is PF-Rayleigh because its port completion is series-parallel (equivalently by the previously proved PF SP closure).

### 6.1 A PF activity `16/9` neutralizer

Take four fresh copies of `U_ell` in parallel and call the result `P_ell`. Then
\[
t_{P_\ell}=4.
\]
Put two fresh copies of `P_ell` in series and call the result `B_ell`. For series composition,
\[
t_{A\circ B}=\frac{t_At_B}{1+t_A+t_B},
\]
so
\[
\boxed{
t_{B_\ell}=\frac{4\cdot4}{1+4+4}=\frac{16}{9}.}
\tag{6.1}
\]
The PF SP closure shows `B_ell` is PF-Rayleigh.

### 6.2 Neutralizing the non-series-parallel atom `Q_7`

Put `Q_7` and `B_ell` in series. Then, using (5.3) and (6.1),
\[
\begin{aligned}
t_{Q_7\circ B_\ell}
&=\frac{(25/7)(16/9)}{1+25/7+16/9}\\
&=\frac{400/63}{(63+225+112)/63}\\
&=1.
\end{aligned}
\]
Thus
\[
\boxed{T_\ell:=Q_7\circ B_\ell\text{ is transparent and PF-Rayleigh for every }\ell\ge2.}
\tag{6.2}
\]

This transparent gadget is **not** series-parallel: `Q_7` occurs as a subgraph of `T_ell`, and `Q_7` contains a `K_4` subgraph (for example vertices `0,2,3,x` for any independent-side vertex `x`). Thus (6.2) is qualitatively different from the earlier transparent theta gadgets.

### 6.3 Arbitrary internal decoration without changing the neutralizing ratio

The new Theorem 4 may now be used inside `Q_7`. Replace any finite set of real edges of `Q_7`, in any adaptive order, by arbitrary transparent PF gadgets such as `U_{ell_1},U_{ell_2},...`. Every intermediate graph remains PF-Rayleigh and, by (4.6), retains
\[
t=25/7.
\]
Call any such decorated atom `R`. Then
\[
R\circ B_\ell
\]
is again transparent PF-Rayleigh by the same `25/7` versus `16/9` calculation. Hence there are infinitely many internally decorated non-series-parallel transparent PF gadgets, not just the single shape `T_ell`.

### 6.4 Exact size formulas for the simple undecorated subfamily

Let `r=2^ell-1`. Then
\[
|V(U_\ell)|=2+r(\ell-1),\qquad |E(U_\ell)|=r\ell.
\]
Four parallel copies give
\[
|V(P_\ell)|=2+4r(\ell-1),\qquad |E(P_\ell)|=4r\ell.
\]
Two copies in series give
\[
|V(B_\ell)|=3+8r(\ell-1),\qquad |E(B_\ell)|=8r\ell.
\]
Since `Q_7` has 11 vertices and 33 edges,
\[
\boxed{
|V(T_\ell)|=13+8(2^\ell-1)(\ell-1),
}
\tag{6.3}
\]
\[
\boxed{
|E(T_\ell)|=33+8\ell(2^\ell-1).
}
\tag{6.4}
\]
For `ell=2`, this is a 37-vertex, 81-edge transparent non-series-parallel PF gadget.

All constructions remain simple graphs: the theta pieces have no direct terminal edge, parallel copies use disjoint interiors, and `Q_7` has its terminal port edge deleted.

## 7. New all-parameter application: non-SP transparent expansions of every wheel

Bado proves strict p-NC for every wheel
\[
W_m=K_1+C_m,\qquad m\ge3,
\]
under the uniform measure on all forests.

Take any wheel `W_m`. Repeatedly, in any adaptive order, choose any current edge and replace it by any transparent non-series-parallel gadget `T_ell` from (6.2), or by any internally decorated neutralized gadget from Section 6.3. The earlier transparent substitution theorem applies at every step because the current graph needs only **unit** p-NC, not PF-Rayleigh.

### Theorem `T07-WHEEL-NONSP-TRANSPARENT-EXPANSIONS-10`

Every graph obtainable from any wheel `W_m`, `m>=3`, by finitely many arbitrary edge replacements using the transparent PF gadgets of Section 6 has pairwise negative edge correlation for the uniform measure on all forests.

For the explicit undecorated subfamily with replacement lengths `ell_1,...,ell_k`,
\[
\boxed{
|V|=m+1+\sum_{i=1}^k\left[11+8(2^{\ell_i}-1)(\ell_i-1)\right],
}
\tag{7.1}
\]
\[
\boxed{
|E|=2m+\sum_{i=1}^k\left[32+8\ell_i(2^{\ell_i}-1)\right].
}
\tag{7.2}
\]
The parameters are completely free:
\[
m\ge3,\qquad k\ge0,\qquad \ell_i\ge2.
\]
For example, replacing one edge of `W_4` by `T_2` yields a graph with 40 vertices and 88 edges.

### Why this application is genuinely outside the predecessor classes

* For `k>=1` these graphs are not wheels, so Bado's theorem alone does not cover them.
* The replacement gadget `T_ell` contains a `K_4` subgraph and is not series-parallel, so Erickson's series-parallel theorem does not certify the whole graph or even the inserted piece by itself.
* NM13-04 proves split-family atoms such as `K_4\vee\overline{K_n}` and `K_5\vee\overline{K_n}`; the wheel-expansion graphs here are not those split families.
* The earlier NM13-08 theta-wheel theorem allowed transparent **series-parallel** replacements. The present family permits transparent replacements containing the non-series-parallel split atom `Q_7` and arbitrarily many internal transparent decorations.
* Tang–Zhang's fixed-component complete-graph results use a different graph class and a different probability ensemble.

Thus the result is an actual transfer theorem plus an unbounded application, not finite enumeration.

## 8. Exact checker and what it certifies

The executed exact checker is

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T02-43-00Z__transparent_neutralizer_checker.py`

with archived output

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T02-43-00Z__transparent_neutralizer_checker.out`.

It performs four independent checks.

1. **Universal algebraic factorization.** Exact symbolic expansion verifies
   \[
   \Delta_{A\parallel B}(p,r)
   =(D_AC_{A,p}-C_AD_{A,p})(D_BC_{B,r}-C_BD_{B,r}),
   \]
   the cross-edge identity used in (4.4).
2. **Split activity transfer.** It rebuilds the 15 terminal partitions, verifies `M=5I+N`, `N^4=0`, and checks (5.1)–(5.2) exactly through `n=12`.
3. **Neutralization arithmetic.** It verifies
   \[
   t(Q_7)=25/7,\qquad t(B_\ell)=16/9,\qquad t(T_\ell)=1
   \]
   exactly for sample `ell=2,...,8`; the displayed formulas prove all `ell>=2`.
4. **Size arithmetic.** It verifies (6.3)–(6.4), including the concrete `W_4` one-replacement count `(V,E)=(40,88)`.

The output terminates with

`ALL_EXACT_CHECKS_PASS`.

The checker does **not** pretend to re-audit the inherited PF theorem for every `Q_n`; that complete symbolic theorem is in the preceding NM13-08 report and its exact certificate. This run uses it as an essential dependency and verifies the new activity/closure arithmetic that was not previously present.

## 9. Honest scope, residual obstruction, and next attack

### Parent theorem

`OPEN -> OPEN`; complete all-graph order `9 -> 9`.

No spanning-tree result, fixed-component result, complete-graph-only result, or restricted family result is mislabeled as the general uniform-forest conjecture.

### Demonstrated mechanism gain

The new gain is not a larger finite census. It is the exact closure

\[
\boxed{
\text{PF host + arbitrary internal transparent PF insertion}
\Longrightarrow
\text{PF host with identical external activity},
}
\]
plus an explicit activity neutralization
\[
\boxed{
25/7\ \circ\ 16/9=1
}
\]
that turns a non-series-parallel split atom into a transparent PF gadget and therefore bridges the PF macro theory back to arbitrary unit-only p-NC cores.

### Residual obstruction

This still does not solve the source conjecture. A hypothetical minimal counterexample is 3-connected by the preserved P14 reduction, and a general 3-connected graph need not expose an edge replacement by a transparent two-terminal piece. The present PF theory also controls only one external port field at a time; it does not establish simultaneous arbitrary real-edge weights.

The next genuinely different structural attack should therefore be a **two-port or three-terminal sign calculus** capable of surviving a 3-connected composition, rather than another finite census or another series/parallel restatement. A natural target is to derive an exact two-port analogue of (4.4) and determine whether the resulting mixed polarization is sign-controlled on the split PF atoms. That directly addresses the remaining P14 three-terminal obstruction.

## 10. Ledger delta

A structured machine-readable delta is saved beside this report as

`2026-09-20T02-43-00Z__ledger_delta.yaml`.

Summary:

* parent: `OPEN -> OPEN`;
* all-graph order: `9 -> 9`;
* new closure theorem: arbitrary internal transparent PF insertion preserves PF and external activity;
* new explicit split-atom activity: `t(Q_7)=25/7`;
* new neutralizer: PF activity `16/9`, yielding transparent non-SP gadgets;
* new application: every wheel admits arbitrary repeated replacements by this non-SP transparent gadget family;
* restricted theorem package: `CANDIDATE_FULL`, pending later independent review;
* novelty/priority: `UNVERIFIED`.
