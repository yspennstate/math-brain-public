Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not authenticated as GPT-6 at maximum.

# NM13-02 T01 — paid dependent-branch allocation splicing and a hereditary symmetric certificate

## Scope and parent metric

**Parent problem:** Friedgut--Kalai Fourier entropy--influence (FEI) conjecture on finite uniform cubes,
\[
H(\widehat f^2)\le C I(f)
\]
with one finite universal constant for every Boolean function.

**Parent-problem status before -> after:** **OPEN -> OPEN.**  
**Universal finite upper bound for \(C_{\rm FEI}\): UNKNOWN -> UNKNOWN.**

No universal FEI constant is claimed. The advance below is mechanism-level: it gives an exact way to splice branch-dependent hereditary allocation certificates without paying an additive branch penalty, and it applies that theorem to P03's current high-degree shifted-threshold stress family. The application deliberately uses an already-known restricted FEI theorem for symmetric functions; this does **not** turn that restricted theorem into full FEI.

Status of the new statements: **PARTIAL / proved in scope; novelty UNVERIFIED.** Any use of P03's newest internal recombination theorem remains a project dependency pending later independent review.

## Compact handoff from the previous NM13-02 run

The preceding T01 run proved an exact restriction-tree theorem for every quadratic phase \(f=(-1)^q\). If \(M_q\) is the alternating polar matrix with rank \(r\), then the squared Fourier law is uniform on an affine \(r\)-flat, \(H(f)=r\), and for every physical coordinate
\[
B_i(f):=H(Z_i\mid Z_{-i})=\frac{r-r_i}{2}\in\{0,1\},
\]
where \(r_i\) is the rank after principal deletion. On every adaptive physical tree,
\[
R_{\mathcal T}(f)=S_{\mathcal T}(f)
=\frac{r-\sum_\ell w_\ell r_\ell}{2};
\]
hence every full tree has \(R_{\mathcal T}=S_{\mathcal T}=r/2\) and
\[
\mathcal A(f)=\frac{r}{2I(f)}\le1.
\]
This also showed that P03's old parity/erasure-synergy family is not an obstruction to the live hereditary-allocation functional. None of the old false pointwise-erasure, resolvent, absolute-overlap, or fixed-affine-drift lemmas is revived here.

## Essential current dependencies and source status

Current `operations/PROGRESS20_2026-09-20.md` assigns NM13-02 to T01 hereditary entropy/recombination theory, companion P03, and supersedes the old intake-only role.

P03's newest substantive report is `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__fei-reed-muller-hereditary-allocation.md` (commit `15988a86dcfa27e8b2c20abdf819ac14d926c6b3`). It proves internally that for \(f=(-1)^P\), with nonconstant derivative degrees \(r_i=\deg D_iP\),
\[
R_{\mathcal T}(f)\le\sum_v w_v\phi(r_v)j_{i(v)}(f_v),
\qquad \phi(r)=2^r h_2(2^{-r}),
\]
and for algebraic degree at most \(d\),
\[
R_{\mathcal T}(f)\le\kappa_d Q_{\mathcal T}(f),
\qquad \kappa_d=2^{d-1}h_2(2^{1-d})\le d-1+1/\ln2.
\]
For a full tree P03 also has the exact influence telescope \(Q_{\mathcal T}(f)=I(f)\). Its current unresolved universal issue is that derivative degree can grow with dimension; its newest report names the shifted-threshold obstruction family as a stress test where high algebraic degree may nevertheless allow cheap physical queries.

The public-source status was checked afresh on 20 September 2026. González--MacManus--Pereyra, arXiv:2606.00246, still states full FEI as a conjecture and develops a stopping-tree sufficient framework plus restricted classes; it is not a universal proof. Xiao Han's Combinatorica 45 (2025) theorem remains
\[
H(f)=O\!\left(I(f)+\sum_i I_i(f)\log\frac1{I_i(f)}\right),
\]
not a dimension-free universal FEI bound. O'Donnell--Wright--Zhou (ICALP 2011) proves FEI for symmetric Boolean functions with the explicit constant \(12.04\). A bounded current search did not surface a later source-matching universal FEI proof. This is bounded negative evidence, not a worldwide priority certificate.

The restricted fresh-control theorem preserved elsewhere in the project remains restricted and is not used as universal FEI. P03's shifted-threshold report also analytically refutes Han's stronger existential absolute-overlap criterion; this correction is preserved below rather than bypassed.

## 1. Exact partial-tree influence budget

Let \(\mathcal T_0\) be any finite adaptive physical restriction tree, not necessarily full. Node \(v\) has cylinder weight \(w_v=2^{-\operatorname{depth}(v)}\), current restriction \(f_v\), and, if internal, queried coordinate \(i(v)\). Define
\[
Q_{\mathcal T_0}(f)
:=\sum_{v\text{ internal}}w_v\operatorname{Inf}_{i(v)}(f_v),
\]
and define the residual leaf influence
\[
L_{\mathcal T_0}(f)
:=\sum_{\ell\text{ leaf}}w_\ell I(f_\ell).
\]

### Theorem 1 (exact partial influence telescope)

For every Boolean \(f\) and every finite adaptive physical restriction tree,
\[
\boxed{Q_{\mathcal T_0}(f)+L_{\mathcal T_0}(f)=I(f).}
\tag{1.1}
\]

### Proof

Fix an original coordinate \(j\). Along a root-to-leaf path, either \(j\) is eventually queried, at a unique first node, or the path reaches a leaf while \(j\) is still free. The cylinders corresponding to all first-query nodes for \(j\), together with all leaves at which \(j\) remains free, partition the full cube.

Every such cylinder is determined only by coordinates queried before \(j\), hence its indicator is independent of \(x_j\). If \(C_v\) is a first-query cylinder, then
\[
w_v\operatorname{Inf}_j(f_v)
=\Pr_x\bigl(C_v\ \&\ f(x)\ne f(x^{\oplus j})\bigr).
\]
The same identity holds for a terminal cylinder \(C_\ell\) with \(j\) free, with \(w_\ell\operatorname{Inf}_j(f_\ell)\) on the left. Summing over this partition gives exactly \(\operatorname{Inf}_j(f)\). Finally sum over \(j\). QED.

This strictly extends the full-tree identity \(Q_{\mathcal T}=I(f)\) used by P03: an unfinished branch keeps exactly the unspent influence budget at the leaf.

## 2. Paid dependent-branch allocation splicing

At any restriction \(g\), let
\[
B_i(g)=H(Z_i\mid Z_{-i})
\]
for its squared-Fourier random set \(Z\), and for a physical tree \(\mathcal T\) let
\[
R_{\mathcal T}(g)=\sum_{v\text{ internal}}w_v B_{i(v)}(g_v).
\]

### Theorem 2 (dependent-branch max-splicing)

Let \(\mathcal T_0\) be any finite adaptive physical restriction tree for \(f\). Suppose every internal node \(v\) has a certified local payment
\[
B_{i(v)}(f_v)\le c_v\operatorname{Inf}_{i(v)}(f_v).
\tag{2.1}
\]
For every leaf \(\ell\), allow a **different**, branch-dependent full continuation tree \(\mathcal U_\ell\) satisfying
\[
R_{\mathcal U_\ell}(f_\ell)\le k_\ell I(f_\ell).
\tag{2.2}
\]
Graft the \(\mathcal U_\ell\)'s onto \(\mathcal T_0\). Then
\[
\boxed{
R_{\rm graft}(f)
\le
\sum_{v\text{ internal}}w_v c_v\operatorname{Inf}_{i(v)}(f_v)
+\sum_{\ell\text{ leaf}}w_\ell k_\ell I(f_\ell).
}
\tag{2.3}
\]
In particular, if
\[
C=\max\left\{\sup_v c_v,\sup_\ell k_\ell\right\},
\]
then
\[
\boxed{R_{\rm graft}(f)\le C I(f).}
\tag{2.4}
\]

### Proof

Allocation is additive under grafting with the outer branch weights:
\[
R_{\rm graft}(f)
=
\sum_{v\text{ internal in }\mathcal T_0}w_v B_{i(v)}(f_v)
+
\sum_\ell w_\ell R_{\mathcal U_\ell}(f_\ell).
\]
Apply (2.1) and (2.2) to obtain (2.3). Bounding every coefficient by \(C\) gives
\[
R_{\rm graft}(f)
\le C\left(Q_{\mathcal T_0}(f)+L_{\mathcal T_0}(f)\right)
=C I(f)
\]
by Theorem 1. QED.

The point is the **max**, not a sum of branch constants. A route may spend some influence before the split and use completely different hereditary arguments after different dependent branches; the exact budget identity prevents paying the same influence twice.

## 3. Ordinary FEI on a restriction-closed class gives hereditary allocation

The preceding theorem becomes useful with a simple information inequality that is independent of P03's unreviewed recombination theorem.

### Lemma 3 (Han allocation inequality)

For every Boolean \(g\) with squared-Fourier random vector \(Z\),
\[
\boxed{\sum_i B_i(g)\le H(\widehat g^2).}
\tag{3.1}
\]

### Proof

Han's entropy inequality gives
\[
\sum_i H(Z_{-i})\ge (n-1)H(Z).
\]
Therefore
\[
\sum_i H(Z_i\mid Z_{-i})
=nH(Z)-\sum_iH(Z_{-i})\le H(Z).
\]
QED.

### Theorem 4 (restriction-closed FEI -> hereditary allocation)

Let \(\mathscr C\) be a class of Boolean functions closed under physical restrictions. Assume the ordinary restricted-class FEI estimate
\[
H(\widehat g^2)\le K I(g)
\tag{3.2}
\]
holds for every \(g\in\mathscr C\). Then every nonconstant \(g\in\mathscr C\) has a coordinate \(i\) with
\[
\boxed{B_i(g)\le K\operatorname{Inf}_i(g).}
\tag{3.3}
\]
Recursively choosing such a coordinate on every branch produces a full adaptive physical restriction tree with
\[
\boxed{R_{\mathcal T}(g)\le K I(g),\qquad \mathcal A(g)\le K.}
\tag{3.4}
\]

### Proof

If \(\operatorname{Inf}_i(g)=0\), then \(\Pr(i\in Z)=0\), so \(B_i(g)=0\). For positive-influence coordinates, if every ratio \(B_i/\operatorname{Inf}_i\) exceeded \(K\), then Lemma 3 would give
\[
H(\widehat g^2)\ge\sum_iB_i>K\sum_i\operatorname{Inf}_i=K I(g),
\]
contradicting (3.2). Thus (3.3) holds. Restriction closure lets the same argument be repeated at each child. A nonconstant Boolean function has some positive influence, so the recursion eventually reaches constants after at most the number of remaining variables. Theorem 2, or directly the full-tree version of Theorem 1, then gives (3.4). QED.

This theorem is **not** a universal FEI proof: taking \(\mathscr C\) to be all Boolean functions would assume exactly the parent theorem one is trying to prove. Its value is that any genuinely known restriction-closed FEI class automatically supplies the hereditary object demanded by P03's architecture.

### Corollary 5 (coordinate-transitive strengthening)

If, additionally, every restriction in \(\mathscr C\) is transitive on its remaining coordinates, then (3.3) holds for **every** remaining coordinate, so **every** full adaptive physical restriction tree satisfies
\[
R_{\mathcal T}(g)\le K I(g).
\tag{3.5}
\]

Indeed transitivity makes all \(B_i\)'s equal and all influences equal, so (3.1)--(3.2) give the coordinatewise bound.

## 4. Application: the precise P03 shifted-threshold obstruction has cheap hereditary allocation

O'Donnell--Wright--Zhou prove ordinary FEI for every symmetric Boolean function with \(K=12.04\). A physical restriction of a symmetric function is symmetric in the still-free variables: it depends only on their Hamming weight plus the number of already fixed \(+1\)'s. Therefore the symmetric class is restriction-closed, and every restriction is coordinate-transitive on its free variables.

Corollary 5 yields the new mechanism statement
\[
\boxed{
R_{\mathcal T}(f)\le12.04\,I(f)
\quad\text{for every symmetric Boolean }f
\text{ and every full adaptive physical tree }\mathcal T.
}
\tag{4.1}
\]
Thus \(\mathcal A(f)\le12.04\) for all symmetric functions in the exact hereditary sense used by P03.

Now apply this to P03's shifted thresholds
\[
f_m(x)=\operatorname{sgn}\left(\sum_{j=1}^{m^2+1}x_j-m\right).
\tag{4.2}
\]
P03 proved analytically that every coordinate has
\[
\frac{O_i(f_m)}{I_i(f_m)}
\ge\frac{1}{2\pi^2}\log(m^2+1)-O(1),
\]
so Han's stronger absolute-overlap selector criterion fails simultaneously at every coordinate as \(m\to\infty\). Nevertheless, (4.1) gives
\[
\boxed{\mathcal A(f_m)\le12.04,}
\tag{4.3}
\]
and in fact the same \(12.04\) allocation bound holds on **every** full adaptive physical tree.

This separates two obstructions sharply: absolute Fourier overlap can diverge logarithmically at every coordinate while the actual hereditary allocation cost remains uniformly bounded.

### Exact high-degree check on an infinite subfamily

For \(m=2^r\ge2\), the algebraic degree of the phase bit of (4.2) is exactly
\[
\boxed{\deg P_m=m^2=n-1.}
\tag{4.4}
\]
To see this, put \(x_j=2y_j-1\), \(n=m^2+1\), and take \(P_m(y)=1\) exactly when \(f_m=-1\). Then
\[
P_m(y)=1_{\{|y|\le t\}},
\qquad t=\frac{m^2+m}{2}.
\]
For a symmetric lower-tail Boolean function, the ANF coefficient of any degree-\(d\) monomial is
\[
a_d\equiv\sum_{j=0}^{\min(d,t)}\binom dj\pmod2.
\]
For \(1\le d\le t\) this is \(2^d\equiv0\). For \(d>t\), Pascal cancellation gives
\[
a_d\equiv\binom{d-1}{t}\pmod2.
\tag{4.5}
\]
At \(d=m^2=2^{2r}\), the number \(d-1\) has all its lower \(2r\) binary digits equal to one, so Lucas' theorem gives \(\binom{d-1}{t}\) odd. At \(d=n=m^2+1\), (4.5) is \(\binom{m^2}{t}\), which is even because \(m^2\) has a single one-bit while \(0<t<m^2\). Hence (4.4).

Therefore the scalar degree-only consequence of P03's newest theorem, \(\mathcal A(f)\le\kappa_d\sim d\), can grow like \(m^2\) on this explicit stress family, while the true hereditary certificate above stays at \(12.04\). This does **not** prove that P03's finer weighted derivative-degree charge must itself grow; it shows only that replacing the adaptive profile by its worst algebraic degree loses the decisive symmetry.

Within P03's current project architecture, its reported universal recombination payment is \(S_{\mathcal T}\le(2/\ln2)I(f)\). Combining that project dependency with (4.1) would give \(H\le(12.04+2/\ln2)I\) on the symmetric class, which is weaker than OWZ's already-known \(12.04\) direct theorem. Hence the source-level class bound does not improve; the gain is specifically the hereditary allocation mechanism P03 needs.

## 5. Sharper threshold payment attempted, not proved

The symmetry argument above imports the known constant \(12.04\). I also tested the stronger threshold-specific possibility
\[
B_i(f)\le c_*\operatorname{Inf}_i(f),
\qquad
c_*:=\frac32+\frac52h_2(1/10)
=2.672488983973203\ldots .
\tag{5.1}
\]
Exact/small-dimensional computation supports it strongly but does **not** prove it:

- all symmetric Boolean functions through \(n=8\) were exhausted; the largest observed \(B_i/I_i\) was \(c_*\), at \(n=3\);
- all ordinary unweighted thresholds through \(n=12\) were exhausted; the same \(c_*\) was the largest observed ratio;
- the shifted-threshold ANF degree formula (4.4) was checked exactly at \(m=2,4,8,16\);
- the exact partial influence budget (1.1) was checked with rational arithmetic on 1,000 random adaptive partial trees for random Boolean functions through \(n=5\).

The attempted proof of (5.1) did not close. A generic marginal-entropy estimate recovers the familiar logarithmic loss, and the absolute-overlap route is unavailable because P03's shifted thresholds analytically refute any universal overlap/influence ratio. Thus (5.1) is recorded only as **CONJECTURAL**.

Executed checker:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T04-18-00+0300__check_allocation_splicing.py`
(commit `3f4e15c78d0e17d1c4c20b2da2ea9860ce1c6218`).

Archived actual output:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T04-18-00+0300__check_allocation_splicing.json`
(commit `edefa47fcabd9d272d8df9664364dff6ef8d44f8`), status `PASS`.

Finite checks are sanity checks only. Theorems 1--4 and Corollary 5 are justified by the written arguments above; (5.1) is not promoted from experiment to theorem.

## 6. Demonstrated mechanism gain versus parent gain

**Parent problem:** universal FEI remains OPEN; universal finite \(C_{\rm FEI}\) remains UNKNOWN -> UNKNOWN.

**Mechanism before this run:** exact quadratic rank allocation \(\mathcal A\le1\); P03's new degree-profile hereditary upper bound with a worst-degree coefficient growing like \(d\); P03's shifted thresholds remained an explicit high-degree stress test and already killed the stronger absolute-overlap selector criterion.

**Mechanism after this run:**

1. exact unfinished-tree budget \(Q_{\mathcal T_0}+L_{\mathcal T_0}=I\);
2. a branch-dependent max-splicing theorem, allowing different continuation mechanisms after different physical branches without summing their constants;
3. a general transfer from ordinary FEI on any physical-restriction-closed class to P03-style hereditary allocation on that class;
4. an every-tree hereditary certificate \(R_{\mathcal T}\le12.04I\) for symmetric Boolean functions;
5. application to P03's precise shifted-threshold stress family, proving \(\mathcal A(f_m)\le12.04\) despite logarithmically divergent absolute-overlap ratios and, for \(m\) a power of two, algebraic degree exactly \(n-1\).

This is a genuine application of the framework, not a receipt/checker-only run, but it does not solve full FEI.

## 7. Next attack

The most concrete next step is the unproved threshold-local estimate (5.1), approached through the signed Krawtchouk three-term recurrence for the two adjacent Fourier fibers that enter \(B_i\), **without** taking the absolute-overlap relaxation that P03 has already disproved. A proof with any universal constant below \(12.04\) would improve the hereditary certificate for the shifted-threshold family and test whether the branch-splicing theorem can combine symmetry payments near threshold branches with quadratic/rank or Reed--Muller payments after branches enter simpler algebraic regimes.

```yaml
ledger_delta:
  track: NM13-02
  assignment: T01_FEI_hereditary_entropy_recombination
  companion: P03
  parent_problem: Friedgut_Kalai_FEI
  parent_status_before: OPEN
  parent_status_after: OPEN
  parent_metric: universal_finite_C_FEI
  parent_metric_before: UNKNOWN
  parent_metric_after: UNKNOWN
  prior_handoff: quadratic_phases_exact_A_le_1_preserved
  mechanism_gain:
    - exact_partial_tree_influence_budget_Q_plus_leafI_equals_I
    - paid_dependent_branch_allocation_max_splicing
    - restriction_closed_FEI_implies_hereditary_allocation
    - symmetric_every_tree_R_le_12.04_I
    - shifted_thresholds_A_le_12.04_despite_overlap_divergence
    - shifted_threshold_phase_degree_n_minus_1_for_m_power_of_2
  theorem_status: PARTIAL_PROVED_IN_SCOPE
  novelty: UNVERIFIED
  checker: 2026-09-20T04-18-00+0300__check_allocation_splicing.py
  checker_output: 2026-09-20T04-18-00+0300__check_allocation_splicing.json
  checker_status: PASS
  failed_route: threshold_local_constant_2.672488983973203_remains_CONJECTURAL
  full_FEI_claimed: false
  next_attack: signed_Krawtchouk_local_erasure_payment_for_thresholds
```
