# fleet01/B19 — robust-trigger forest selection and a linear co-pair information tax

**Run:** `20260922T104653Z-b19-fei-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, Path C  
**Classification:** `ESSENTIAL_STEP_APPLIED / CRITICAL_CORE_SUBCLASS_EXCLUSION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read, but no separately authenticated native brain retrieval/context was used.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Owner supersession and the live target

The live owner control is revision `2026-09-22.3`. It redirects all eighty existing workers to FEI, suspends new POS3/FOREST/BT4/MOC4 work and installation/benchmark work, and assigns fleet01/B19 the Path-C target **critical-core exclusion from selected pairs**. This run therefore does not continue the older POS3 prompt.

The B19 assignment asks for a contradiction to a genuine minimum-dimensional ratio core with

\[
\rho:=\frac{\mathcal F}{\mathcal J}>4
\]

using the co-pair tax on a source-selected family of physical pairs, while preserving original-coordinate costs. The newest same-account B12 result leaves precisely a matching/cover problem: robust trigger edges each carry centered pair information, but a vertex-disjoint matching may lose most of the robust-row mass when many rows share triggers.

This run replaces the matching requirement by a different source-valid object: a **directed trigger forest**. Tree entropy pays all selected pair mutual informations jointly, so shared trigger vertices are allowed without reusing the same global information bank. The resulting theorem gives a dimension-free *linear* (not quadratic) payment for the entire robust-row influence mass in terms of total correlation. It does not close FEI because total correlation itself is not `O(J)`; recursive ternary majority gives a genuine Boolean obstruction to that shortcut.

## 1. Exact sources actually used

### Current critical-core and co-pair sources

1. **TERMINAL_CORE** — `yspennstate/math-open-problems`, commit `85ffa60db26997421d980b1f86c03d82259504ca`, path
   `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, Sections 3--7.  It supplies the genuine minimum-dimensional `F/J` ratio core and the physical-block inequality. In particular, on a ratio-`rho` core, singleton blocks imply
   \[
   h_2(q_k)\ge \rho q_k.
   \tag{1.1}
   \]

2. **COPAIR_BARRIER** — same repository/commit, path
   `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`, Sections 3--7. It supplies the exact Boolean-square identity
   \[
   r_{ik}:=\Pr(i,k\in X)=\frac14p_{ik}+o_{ik},\qquad o_{ik}\ge0,
   \tag{1.2}
   \]
   where `p_ik` is derivative-support disagreement and `r_ik` is the actual joint spectral occurrence probability.

3. **Same-account pair selector** — `yspennstate/math-open-problems`, immutable snapshot commit `b49be89db2ee2b99563dbd224613e2db66983eed`, path
   `proofnet24/P03-fei/fleet-2026-09-22/fleet01/B12/20260922T101952Z-fleet01-B12-r11/REPORT.md`, Sections 2--7. It proves the centered pair law, tensor-baseline-safe pair payment, and for every relative-`1/16` robust trigger edge `(i,k)` in a true `rho>4` core the weaker Pinsker tax
   \[
   I(X_i;X_k)>\frac{169}{288\ln2}q_i^2.
   \tag{1.3}
   \]
   Its first unpaid implication is a source-valid matching/cover lemma.

### Named OTHER-account results consumed and applied

4. **fleet04/B12, robust-row codimension staircase**, commit
   `a1b2a93210fe7cc871cd10c5bbbf43b1b983a254`, path
   `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T094436Z-robust-row-codimension-staircase/REPORT.md`, Sections 2--4. For a relative-`eta` robust row with trigger set `F_i`, it proves
   \[
   p_{ik}\ge2(1-2\eta)q_i\quad(k\in F_i)
   \tag{1.4}
   \]
   and, on an all-block terminal core at level `K`,
   \[
   |F_i|\ge
   \left\lceil\log_2\frac1{(1+\eta)q_K}\right\rceil,
   \quad \frac{h_2(q_K)}{q_K}=K.
   \tag{1.5}
   \]
   At `eta=1/16` and `K>4`, this gives at least three distinct trigger coordinates.

5. **fleet04/B18, robust-trigger overlap collapse**, immutable snapshot commit
   `3739dd232ab781de9e899a5caf364a7144cf5bef`, path
   `proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T101158Z-robust-trigger-overlap-collapse/REPORT.md`, Theorem 4.1. On a genuine `rho>4` critical core, if `R` is the set of relative-`1/16` robust rows and
   \[
   H_4=\sum_{k}\sum_{i\ne k}(4+\mathfrak j'(q_k))
   [p_{ki}-2c_{k\leftarrow i}],
   \]
   then
   \[
   \sum_{i\in R}q_i
   \le \frac2{33}[\mathcal P-\operatorname{DTC}(X)]
      +\frac1{33}H_4.
   \tag{1.6}
   \]
   I combine this exact OTHER-account result with the new forest tax below; no raw `U_4=O(J)` assertion is used.

6. **fleet03/B18 recursive-majority barrier**, commit
   `bff0d7b6c21485f386841c42582eb04f32705046`, path
   `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`, Section 2. It gives, for depth-`m` recursive ternary majority `M_m`,
   \[
   N_m=3^m,\qquad q_i=2^{-m},\qquad
   \mathcal J=(3/2)^m,\qquad H=4(\mathcal J-1).
   \tag{1.7}
   \]
   This is used below to falsify the tempting generic shortcut `TC(X)=O(J)`.

### Assigned partner status

The assigned partner is `fleet02/B19`. At the pre-publication source check there was no completed compatible FEI artifact at
`proofnet24/P03-fei/fleet-2026-09-22/fleet02/B19/` and no completed fleet02/B19 handoff in the live FEI handoff root. Older fleet02/B19 POS3 artifacts are suspended and were not imported into FEI. In accordance with the owner order, the run continued from the complete snapshots above rather than waiting.

## 2. Setup and the compact conditional end-to-end route

Use the centered character gauge. Let `X` be the squared-Fourier spectral random subset, and write

\[
q_i=\Pr(i\in X)\le\frac12,
\qquad
\mathcal J=\sum_iq_i,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),
\qquad
\mathcal P=\sum_i\mathfrak j(q_i),
\qquad
\mathcal F=H(X)-\mathcal P.
\]

Suppose for contradiction that the Path-C stopping theorem fails at `K=4`, and choose the genuine minimum-dimensional critical descendant with

\[
\rho=\frac{\mathcal F}{\mathcal J}>4.
\tag{2.1}
\]

Let `R` be its relative-`1/16` robust derivative rows, with physical trigger sets `F_i`. The live conditional route is:

1. eliminate the zero-depth branch by the existing integrability classification;
2. control robust rows by a realizable/nonreusing source statistic;
3. control the complementary small/nonrobust rows by the separate multiscale/integrability route;
4. combine the two controls to obtain an affordable physical block, contradicting ratio-criticality.

This report proves a stronger version of step 2 **provided the available bank is total correlation**: all robust-row first-moment influence is paid linearly by a source-selected forest of actual co-pairs. The first remaining implication is to turn that forest payment into an affordable physical stopping credit without assuming total correlation itself is `O(J)`.

## 3. New Lemma: robust trigger edges carry a linear mutual-information tax

For `rho>2`, let `q_rho` be the unique number in `(0,1/2)` satisfying

\[
\frac{h_2(q_\rho)}{q_\rho}=\rho.
\tag{3.1}
\]

The ratio `h_2(q)/q` is strictly decreasing because

\[
\frac{d}{dq}\frac{h_2(q)}q
=\frac{\log_2(1-q)}{q^2}<0.
\tag{3.2}
\]

The singleton critical-core inequality (1.1) therefore gives

\[
q_k\le q_\rho<q_4,
\qquad
q_4=0.1564173549642720155\ldots .
\tag{3.3}
\]

Define

\[
\alpha:=\frac7{16},
\qquad
c_\rho:=D_{\rm KL,2}(\operatorname{Ber}(\alpha)
\Vert\operatorname{Ber}(q_\rho)).
\tag{3.4}
\]

Explicitly,

\[
c_\rho=
\frac7{16}\log_2\frac{7/16}{q_\rho}
+\frac9{16}\log_2\frac{9/16}{1-q_\rho}.
\tag{3.5}
\]

### Lemma 3.1 — `ROBUST-TRIGGER-LINEAR-COPAIR-TAX`

For every relative-`1/16` robust row `i` and every trigger `k in F_i`,

\[
\boxed{I(X_i;X_k)\ge c_\rho q_i.}
\tag{3.6}
\]

In particular, uniformly over every `rho>4` critical core,

\[
\boxed{I(X_i;X_k)>c_4q_i,}
\qquad
c_4:=D_{\rm KL,2}(\operatorname{Ber}(7/16)
\Vert\operatorname{Ber}(q_4))
=0.32031813133655726\ldots .
\tag{3.7}
\]

#### Proof

By fleet04/B12 (1.4), at `eta=1/16`,

\[
p_{ik}\ge\frac74q_i.
\tag{3.8}
\]

By the exact co-pair identity (1.2),

\[
r_{ik}=\Pr(X_i=X_k=1)
=\frac14p_{ik}+o_{ik}
\ge\frac7{16}q_i.
\tag{3.9}
\]

Thus

\[
t_{ik}:=\Pr(X_k=1\mid X_i=1)
=\frac{r_{ik}}{q_i}\ge\frac7{16}=\alpha.
\tag{3.10}
\]

Mutual information is the expected posterior KL divergence from the marginal. Therefore

\[
\begin{aligned}
I(X_i;X_k)
&=q_iD_2(\operatorname{Ber}(t_{ik})\Vert\operatorname{Ber}(q_k))\\
&\quad +(1-q_i)
D_2(\mathcal L(X_k\mid X_i=0)\Vert\operatorname{Ber}(q_k))\\
&\ge q_iD_2(\operatorname{Ber}(t_{ik})\Vert\operatorname{Ber}(q_k)).
\end{aligned}
\tag{3.11}
\]

For `t>q`, `D_2(Ber(t)||Ber(q))` is increasing in `t` and decreasing in `q`:

\[
\partial_tD_2=\log_2\frac{t(1-q)}{q(1-t)}>0,
\qquad
\partial_qD_2=\frac{q-t}{q(1-q)\ln2}<0.
\tag{3.12}
\]

Since `t_ik>=alpha` and `q_k<=q_rho<alpha`, (3.11)--(3.12) give (3.6). Since `rho>4` implies `q_rho<q_4`, the same monotonicity gives the strict uniform form (3.7). QED.

### Why this is stronger than the current pair result

The previous centered Pinsker step gave `I_ik >= 0.84658... q_i^2`. Lemma 3.1 is **linear in `q_i`**. The gain is source-specific: a robust trigger does not merely perturb the pair law by `O(q_i)` in total variation; conditioned on the rare event `X_i=1`, the trigger bit has posterior at least `7/16` while its unconditional marginal is at most `q_rho<0.157`. The resulting KL per occurrence of `i` is bounded below by a fixed positive constant.

## 4. New combinatorial lemma: every robust trigger digraph has a high-mass directed forest

Form the directed physical trigger graph `D` on the active original coordinates, with an arc

\[
i\to k\quad\Longleftrightarrow\quad i\in R,\ k\in F_i.
\tag{4.1}
\]

Only robust rows have outgoing arcs. Let

\[
d_\rho:=
\left\lceil\log_2\frac{16}{17q_\rho}\right\rceil.
\tag{4.2}
\]

By the fleet04/B12 codimension staircase, every robust vertex has at least `d_rho` distinct out-neighbors; for `rho>4`, `d_rho>=3`.

### Lemma 4.1 — `DIRECTED-TRIGGER-FOREST-COVER`

Let nonnegative weights `w_i` be assigned to robust vertices. There is a subset `T` of trigger arcs such that

1. the underlying undirected graph of `T` is a forest;
2. every robust vertex is the tail of at most one selected arc;
3. if `R_T` is the set of robust vertices that are tails of selected arcs, then
   \[
   \boxed{
   \sum_{i\in R_T}w_i
   \ge\frac{d_\rho}{d_\rho+1}
   \sum_{i\in R}w_i.}
   \tag{4.3}
   \]

#### Proof

Take the strongly connected components of `D` and its condensation DAG.

A nonrobust vertex has no outgoing arc, so it cannot belong to a nontrivial strongly connected component. Hence every nontrivial SCC consists entirely of robust vertices.

For each sink SCC `S` consisting of robust vertices, every outgoing trigger of every `i in S` stays in `S`. Since each `i` has at least `d_rho` distinct out-neighbors and loops are absent,

\[
|S|\ge d_\rho+1.
\tag{4.4}
\]

Choose as the root of `S` a vertex of minimum `w_i`. Then

\[
w_{\rm root}\le\frac1{|S|}\sum_{i\in S}w_i
\le\frac1{d_\rho+1}\sum_{i\in S}w_i.
\tag{4.5}
\]

Because `S` is strongly connected, it has a directed in-arborescence toward that root: every nonroot vertex has one selected outgoing arc on a directed path toward the root.

For every nonsink SCC, choose one outgoing condensation edge toward a successor SCC and choose its tail as the local root. Inside the SCC choose a directed in-arborescence toward that tail; the local root then uses the selected outgoing inter-SCC arc. Do this following the acyclic condensation graph until a sink is reached.

The resulting directed graph has outdegree one at every robust vertex except the chosen roots of robust sink SCCs, and no directed cycle. A finite graph with outdegree at most one and no directed cycle cannot contain an undirected cycle: on an undirected cycle, the number of selected cycle edges equals the number of cycle vertices, forcing every vertex to use its unique outgoing edge on that cycle, which would create a directed cycle. Thus the underlying graph is a forest.

The only uncovered robust weights are the minimum-weight roots in robust sink SCCs. Summing (4.5) over the disjoint sink SCCs proves (4.3). QED.

For the live `rho>4` regime, (4.3) gives at least `3/4` of the robust weight. The argument is insensitive to arbitrarily large trigger overlap; a star-like overlap is allowed.

## 5. New main theorem: robust influence is paid linearly by total correlation

Define the spectral total correlation

\[
\operatorname{TC}(X)
:=\sum_j H(X_j)-H(X)
=\sum_j h_2(q_j)-H(X).
\tag{5.1}
\]

### Lemma 5.1 — forest mutual-information inequality

For every forest `T` on a subset of the coordinates,

\[
\boxed{
\sum_{\{u,v\}\in E(T)}I(X_u;X_v)
\le\operatorname{TC}(X).}
\tag{5.2}
\]

#### Proof

Root every tree. By the chain rule and the fact that conditioning reduces entropy,

\[
H(X_{V(T)})
\le\sum_{\text{roots }r}H(X_r)
 +\sum_{v\ne r}H(X_v\mid X_{\mathrm{parent}(v)}).
\]

Rearranging gives

\[
\sum_{e\in T}I_e
\le\sum_{v\in V(T)}H(X_v)-H(X_{V(T)})
=\operatorname{TC}(X_{V(T)}).
\]

Total correlation is monotone under adjoining variables because
`TC(Y,Z)=TC(Y)+I(Z;Y)`. Hence `TC(X_{V(T)})<=TC(X)`. QED.

### Theorem 5.2 — `ROBUST-FOREST-TC-PAYMENT-v1`

On every genuine centered minimum-dimensional `rho>4` ratio-critical core,

\[
\boxed{
\sum_{i\in R}q_i
\le
\frac{d_\rho+1}{d_\rho c_\rho}\,
\operatorname{TC}(X).}
\tag{5.3}
\]

Uniformly over all `rho>4`,

\[
\boxed{
\sum_{i\in R}q_i
<\frac{4}{3c_4}\operatorname{TC}(X)
=4.162528445610855\ldots\,\operatorname{TC}(X).}
\tag{5.4}
\]

Equivalently,

\[
\boxed{
\operatorname{TC}(X)
>0.24023859850241795\ldots
\sum_{i\in R}q_i.}
\tag{5.5}
\]

#### Proof

Apply Lemma 4.1 with `w_i=q_i`, obtaining a directed trigger forest `T` whose covered tails `R_T` satisfy

\[
\sum_{i\in R_T}q_i
\ge\frac{d_\rho}{d_\rho+1}\sum_{i\in R}q_i.
\tag{5.6}
\]

Every selected edge has a unique robust tail `i`, so Lemma 3.1 gives

\[
\sum_{e=(i,k)\in T}I(X_i;X_k)
\ge c_\rho\sum_{i\in R_T}q_i.
\tag{5.7}
\]

Lemma 5.1 bounds the same left side by `TC(X)`. Combine (5.6)--(5.7) to get (5.3). Since `rho>4` gives `d_rho>=3` and `c_rho>c_4`, (5.4)--(5.5) follow. QED.

### Exact subclass exclusion

A true `rho>4` critical core satisfying

\[
\operatorname{TC}(X)
\le0.24023859850241795\ldots
\sum_{i\in R}q_i
\tag{5.8}
\]

cannot exist. In particular, an all-robust critical core with

\[
\operatorname{TC}(X)\le0.24023859850241795\ldots\,\mathcal J
\tag{5.9}
\]

is excluded. This is a literal contradiction lemma on a source-defined subclass, not a claim that all critical cores satisfy the extra low-`TC` condition.

## 6. Direct integration with fleet04/B18's newest overlap theorem

Let

\[
Q_R:=\sum_{i\in R}q_i.
\]

The named OTHER-account result fleet04/B18 `20260922T101158Z-b18-fei-a11` gives (1.6), while Theorem 5.2 gives (5.3). Therefore every genuine `rho>4` critical core satisfies the simultaneous two-bank bound

\[
\boxed{
Q_R
\le
\min\left\{
\frac{d_\rho+1}{d_\rho c_\rho}\operatorname{TC}(X),
\frac2{33}[\mathcal P-\operatorname{DTC}(X)]+\frac1{33}H_4
\right\}.}
\tag{6.1}
\]

The two terms are genuinely different:

- the new term is tensor-baseline safe because it uses actual pair mutual information and a forest entropy ledger;
- the fleet04/B18 term pays repeated trigger addresses through the crossing-visible bank plus the support-hidden bank `H_4` and does not spend the opposite-sign orientation component.

Thus a critical core with a large robust fraction is forced simultaneously into a **high-total-correlation** regime and, once the robust fraction exceeds the explicit crossing-only threshold, a **large support-hidden-curvature** regime.

For example, if every active row is robust, `Q_R=J`, then

\[
\operatorname{TC}(X)>0.2402385985\,\mathcal J,
\tag{6.2}
\]

and because `P<=2J/ln2` and `DTC>=0`, (1.6) also forces

\[
\boxed{
H_4>\left(33-\frac4{\ln2}\right)\mathcal J
=27.2292198364\ldots\,\mathcal J.}
\tag{6.3}
\]

No assertion `H_4=O(J)` is made; (6.3) is a necessary condition, consistent with the published warning that raw hidden curvature can be large under weaker hypotheses.

## 7. Genuine Boolean obstruction: total correlation is not an affordable `O(J)` bank

Theorem 5.2 removes the *pair-overlap* obstruction, but it would be invalid to finish by asserting `TC(X)<=C J` universally.

Use the source-valid recursive ternary-majority family `M_m` from fleet03/B18. Its exact data are (1.7):

\[
N_m=3^m,\qquad q_i=2^{-m},\qquad
J_m=(3/2)^m,\qquad H(M_m)=4(J_m-1).
\]

Therefore

\[
\begin{aligned}
\frac{\operatorname{TC}(X^{(m)})}{J_m}
&=
\frac{3^m h_2(2^{-m})-4[(3/2)^m-1]}{(3/2)^m}\\
&=
\frac{h_2(2^{-m})}{2^{-m}}-4+\frac4{(3/2)^m}.
\end{aligned}
\tag{7.1}
\]

As `q downarrow 0`,

\[
\frac{h_2(q)}q
=\log_2\frac1q+\frac1{\ln2}+o(1).
\]

Hence

\[
\boxed{
\frac{\operatorname{TC}(X^{(m)})}{J_m}
=m+\frac1{\ln2}-4+o(1)\longrightarrow\infty.}
\tag{7.2}
\]

This is a genuine Boolean family, not an abstract subset law. It satisfies FEI at ratio asymptotic to `4`; it refutes only the proposed generic payment `TC=O(J)`. Consequently Theorem 5.2 cannot be converted to full FEI by declaring total correlation an `O(J)` reserve.

This guard is important: the new forest method solves the overlap geometry but exposes the correct next mathematical burden rather than hiding the rare-event logarithm in a new bank.

## 8. Exact first missing implication after this run

The first unpaid implication is now:

> **`C-ROBUST-FOREST-TC-TO-PHYSICAL-BLOCK`.** On a genuine minimum-dimensional `rho>4` critical core, use the *specific trigger-forest mutual information* produced above—not raw total correlation—to construct an affordable physical restriction/block, or prove that if this forest information remains trapped in high-order total correlation then the complementary nonrobust/multiscale structure yields an affordable block.

A sufficient version would be any source-valid theorem of the following form. Let `T` be the directed trigger forest from Lemma 4.1. If

\[
\sum_{e\in T}I_e\ge c_\rho\frac{d_\rho}{d_\rho+1}Q_R,
\]

then either

1. one actual physical block `A` satisfies `Delta_A F < 4D_A`, contradicting ratio-criticality; or
2. the forest information can be injected, without reuse, into the already affordable `P-DTC`/crossing bank; or
3. the remaining folded influence belongs to the small/nonrobust branch targeted by B11, with an explicit quantitative transfer.

The distinction from the old matching gap is material. Vertex-disjointness is no longer required to prevent pair-information reuse: tree entropy already performs the nonreuse. What remains is a **physical-spending conversion** from the selected forest information, under the exact critical-core restriction identities. Recursive majority shows that an unqualified global `TC=O(J)` conversion is false.

## 9. What changed at target level

**Before this run:** the live B12 pair-selected theorem had a source-valid centered information tax on every robust trigger, but only quadratic in `q_i` after Pinsker, and its explicit first gap was a matching/cover lemma. Large trigger overlap could destroy a vertex-disjoint matching.

**After this run:**

- every robust trigger carries the stronger linear tax `I_ik >= c_rho q_i`;
- a directed forest covers at least `d_rho/(d_rho+1)` of robust-row influence, at least `3/4` uniformly;
- all selected edge mutual informations are jointly nonreused through the exact forest entropy inequality;
- therefore `Q_R <= ((d_rho+1)/(d_rho c_rho)) TC`, with the explicit uniform constant `4.1625284456...`;
- combined with fleet04/B18, robust load is simultaneously constrained by total correlation and the crossing/support-hidden bank;
- the tempting final shortcut `TC=O(J)` is source-validly refuted by recursive ternary majority.

This is an `ESSENTIAL_STEP_APPLIED` and a genuine critical-core subclass exclusion. It is **not** full FEI closure.

## 10. Provenance and scope

All mathematical objects above are original physical-coordinate/spectral-source quantities from the cited Boolean function. No spectral-label oracle, fake product law, raw-U4 payment, fixed-depth projection payment, refuted fixed potential, or unproved AND-extremality statement is used. No benchmark answer, credential, scheduler identifier, machine path, unrelated private data, public posting, email/Drive action, paid model/API, remote workflow, or permission change is included.
