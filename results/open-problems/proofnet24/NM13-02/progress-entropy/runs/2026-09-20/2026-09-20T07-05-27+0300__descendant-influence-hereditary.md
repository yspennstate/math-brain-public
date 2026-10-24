Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not authenticated as GPT-6 at maximum.

# NM13-02 T01 — descendant-influence hereditary payment and a bypass of P03's curvature/query obstruction

## Parent scope and demonstrated mechanism gain

**Parent problem:** Friedgut--Kalai Fourier entropy--influence (FEI) on finite uniform cubes,
\[
H(\widehat f^{\,2})\le C I(f)
\]
for one finite universal constant and every Boolean function.

**Parent-problem status before -> after:** **OPEN -> OPEN.**

**Universal finite upper bound for \(C_{\rm FEI}\): UNKNOWN -> UNKNOWN.**

The source-level metric therefore does not move. The mathematical gain is a fresh-variable-free hereditary payment that directly addresses the newest obstruction in P03's curvature stopping theorem.

For every physical split at coordinate \(i\), with children \(f^+,f^-\), folded queried influence
\[
j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
\]
and hereditary spectral-bit allocation
\[
B_i(f)=H(Z_i\mid Z_{-i}),
\]
I prove
\[
\boxed{
B_i(f)\le \frac{1}{\ln2}\,j_i(f)+\frac{I(f^+)+I(f^-)}2.
}
\tag{A}
\]
Thus the physical-derivative curvature term discovered by P03 can be paid by **descendant residual influence**, not only by the influence of the queried coordinate.

If a stopping leaf \(\ell\) has hereditary certificate \(R\le K_\ell I\), then labels propagated upward by
\[
\boxed{
K_v=\max\left\{\frac1{\ln2},1+K_{v,+},1+K_{v,-}\right\}
}
\tag{B}
\]
certify \(R_v\le K_v I(f_v)\) on the whole dependent-branch tree. In particular, a restriction prefix of height at most \(d\) whose leaves are quadratic phases has
\[
\boxed{R_{\mathcal T}(f)\le(d+1)I(f)}
\tag{C}
\]
for \(d\ge1\), using the earlier NM13-02 exact quadratic certificate \(R\le I\) at the leaves.

For a degree-\(\le3\) phase \(f=(-1)^P\), if \(\tau_3(P)\) is the size of a set of physical variables meeting every cubic monomial of \(P\), querying that set leaves only quadratics, hence
\[
\boxed{\mathcal A(f)\le \tau_3(P)+1.}
\tag{D}
\]
This improves P03's generic degree-three hereditary constant \(\kappa_3=4h_2(1/4)=3.2451124978\ldots\) to \(2\) on cubic-star phases (\(\tau_3=1\)). It remains a restricted structural theorem, not full FEI.

## Compact handoff of prior NM13-02 mathematics

The preceding T01 results remain unchanged in scope.

- **Quadratic rank telescope:** if \(f=(-1)^q\) is quadratic with polar rank \(r\), every full adaptive physical tree has \(R=r/2\le I(f)\).
- **Exact influence budget / max-splicing:** queried influence and weighted residual leaf influence partition the root total influence, allowing branch-dependent certificates to combine by the maximum relevant constant.
- **Character-child theorem:** a split with a signed-character child has \(B_i\le C_\chi\operatorname{Inf}_i\), where \(C_\chi=2+1/(\sqrt e\ln2)\).
- **Truncated minor-child theorem:** the previous run removed the raw minor-child payment whenever folded queried influence is at least \(0.3111084359\ldots\), and proved one-point perturbations of arbitrary quadratics have bounded hereditary allocation.
- The pointwise erasure shortcut, fixed-coefficient affine-drift rule, Han absolute-overlap selector, and resolvent interpolation remain retired. Nothing below revives them.

## Current dependency and exact P03 obstruction

The controlling owner directive is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Current LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

The newest P03 substantive report is `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T06-31-37+0300__fei-character-defect-curvature-allocation.md`. P03 proves/reports the local physical-derivative estimate
\[
B_i(f)\le\frac12 I(D_i f)+\frac1{\ln2}j_i(f),
\qquad D_i f=f^+f^-,
\tag{P1}
\]
and its exact adaptive-tree curvature telescope. Together with its earlier reported dependent-recombination theorem, P03 obtains the sufficient stopping condition
\[
\mathcal C_{\mathcal T}\le KQ_{\mathcal T}
\quad\Longrightarrow\quad
H(f)\le \max\left\{C_0,\frac K2+\frac3{\ln2}\right\}I(f)
\tag{P2}
\]
when the stopping leaves have FEI constant \(C_0\). P03 also shows that full root curvature need not be \(O(I)\): dense quadratic phases have quadratic-size curvature and only linear total influence. Its live obstruction is therefore to find a stopping tree whose **consumed curvature** is controlled by the **queried influence** before entering certified leaves.

The theorem below is complementary rather than a takeover of P03's claim: it converts the same physical derivative into child residual influence and proves a different hereditary recursion. The local step is reproduced independently below from the standard cube edge-isoperimetric inequality, so this report does not treat P03's reported proof as external certification.

`POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem is claimed or duplicated.

### Current primary-source status

A fresh bounded source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246, submitted 29 May 2026. It still states universal FEI as the Friedgut--Kalai conjecture and develops the stopping-tree/restriction architecture plus restricted positive classes; it does not state a universal proof. Li--Han, arXiv:2512.03117 (2 December 2025), strengthens Han's general inequality to sharp constants but retains the coordinate-influence logarithmic term \(\sum_i I_i(f)\ln(1/I_i(f))\). Thus no source-matching universal finite FEI constant was recovered in this bounded check. This is not a worldwide novelty certificate for the lemmas below.

## 1. Local curvature reproduced from the disagreement set

Let \(f:\{-1,1\}^{V}\to\{-1,1\}\), fix \(i\in V\), and put
\[
\alpha=\operatorname{Inf}_i(f),\qquad j=\min\{\alpha,1-\alpha\}.
\]
Multiplying \(f\) by the physical character \(x_i\) sends \(\alpha\) to \(1-\alpha\), leaves \(B_i(f)\) unchanged, and changes \(D_i f\) only by a global sign. Thus assume \(\alpha=j\le1/2\).

The spectral bit marginal satisfies \(\Pr(i\in Z)=\alpha\), so conditioning only lowers entropy:
\[
B_i(f)=H(Z_i\mid Z_{-i})\le H(Z_i)=h_2(j).
\tag{1.1}
\]
Let \(D=D_i f\) on the \(|V|-1\) residual cube. Its negative set has density \(j\). The standard edge-isoperimetric inequality on the uniform Boolean cube, in the present influence normalization, gives
\[
I(D)\ge2j\log_2\frac1j.
\tag{1.2}
\]
(Equality holds for a subcube, so the normalization is sharp.) Also
\[
(1-j)\log_2\frac1{1-j}
=\frac{-(1-j)\ln(1-j)}{\ln2}
\le\frac j{\ln2},
\tag{1.3}
\]
because \(-\ln(1-j)\le j/(1-j)\). Hence
\[
h_2(j)\le\frac12 I(D)+\frac j{\ln2}.
\]
Together with (1.1),
\[
\boxed{B_i(f)\le\frac12I(D_i f)+\frac1{\ln2}j_i(f).}
\tag{1.4}
\]
This reproduces the P03 curvature step from a standard exact cube boundary theorem.

## 2. New derivative triangle: curvature is at most the sum of child influences

Write \(g=f^+\), \(h=f^-\). For a residual coordinate \(k\ne i\), let
\[
A_k=\{g(x)\ne g(x^{(k)})\},\qquad
C_k=\{h(x)\ne h(x^{(k)})\}.
\]
Because \(D_i f=gh\), its sign changes on the \(k\)-edge exactly when one, but not both, of \(g,h\) changes there. Therefore
\[
\{D_i f(x)\ne D_i f(x^{(k)})\}=A_k\triangle C_k.
\]
Consequently
\[
\operatorname{Inf}_k(D_i f)
=\Pr(A_k\triangle C_k)
\le\Pr(A_k)+\Pr(C_k)
=\operatorname{Inf}_k(g)+\operatorname{Inf}_k(h).
\]
Summing over residual coordinates proves
\[
\boxed{I(D_i f)\le I(f^+)+I(f^-).}
\tag{2.1}
\]
Combining (1.4) and (2.1) yields the universal local payment
\[
\boxed{
B_i(f)\le \frac1{\ln2}j_i(f)+\frac{I(f^+)+I(f^-)}2.
}
\tag{2.2}
\]
This is the first new theorem of the run.

## 3. Descendant-influence hereditary recursion

At an internal node \(v\), suppose the continuations below its two children have hereditary allocation certificates
\[
R_{v,\sigma}\le K_{v,\sigma}I(f_{v,\sigma}),\qquad \sigma\in\{+,-\}.
\]
Using (2.2),
\[
R_v\le \frac1{\ln2}j_v
 +\frac12(1+K_{v,+})I(f_{v,+})
 +\frac12(1+K_{v,-})I(f_{v,-}).
\tag{3.1}
\]
The exact physical influence decomposition is
\[
I(f_v)=\operatorname{Inf}_{i(v)}(f_v)
+\frac12I(f_{v,+})+\frac12I(f_{v,-}).
\tag{3.2}
\]
Since \(j_v\le\operatorname{Inf}_{i(v)}(f_v)\), any
\[
K_v\ge\frac1{\ln2},\qquad K_v\ge1+K_{v,+},\qquad K_v\ge1+K_{v,-}
\]
gives \(R_v\le K_vI(f_v)\). This proves (B).

Equivalently, for a finite prefix tree \(\mathcal T_0\) with node weights \(w_v\),
\[
R_{\mathcal T_0}(f)
\le\frac1{\ln2}J_{\mathcal T_0}(f)
+\sum_{u\ne\mathrm{root}\atop u\text{ child of an internal prefix node}}w_u I(f_u).
\tag{3.3}
\]
Thus descendant influence is an explicit paid branch-dependent resource rather than an independence assumption.

### Corollary 3.1: bounded restriction depth to quadratic leaves

The preceding NM13-02 quadratic theorem gives leaf constant \(K=1\). If every root-to-leaf path in a prefix has length at most \(d\), and every prefix leaf is quadratic, repeated application of (B) gives \(K_{\rm root}\le d+1\) for \(d\ge1\), because \(1/\ln2<2\). Hence (C).

### Corollary 3.2: cubic monomial vertex-cover bound

Let \(f=(-1)^P\), \(\deg P\le3\), and let \(E\) meet every degree-three monomial in the ANF support of \(P\), with \(|E|=\tau\). Query all coordinates in \(E\). Every resulting restriction has degree at most two, hence is a quadratic leaf. Therefore
\[
\boxed{\mathcal A(f)\le\tau+1.}
\tag{3.4}
\]
Minimizing over \(E\) proves (D). This is an all-dimensional class theorem, not finite-dimensional verification.

## 4. Application: cubic stars expose the curvature/query price and are paid by descendants

For \(r\ge1\), on \(2r+1\) bits in \(\mathbb F_2\) notation define
\[
Q_r(y)=\sum_{s=1}^{r}y_{2s-1}y_{2s}\pmod2,
\qquad
F_r(x_0,y)=(-1)^{x_0Q_r(y)}.
\tag{4.1}
\]
All cubic monomials contain \(x_0\), so \(\tau_3=1\). Querying \(x_0\) gives one constant child and the quadratic phase \(q_r=(-1)^{Q_r}\).

For one pair \((u,v)\), \(\mathbb E(-1)^{uv}=1/2\); independence gives \(\mathbb E q_r=2^{-r}\). Therefore
\[
\alpha_r:=\operatorname{Inf}_{x_0}(F_r)
=\Pr(q_r=-1)=\frac{1-2^{-r}}2.
\tag{4.2}
\]
The quadratic child has \(2r\) coordinates of influence \(1/2\), hence
\[
I(q_r)=r.
\tag{4.3}
\]
Each \(y\)-coordinate of \(F_r\) has influence \(1/4\), so
\[
I(F_r)=\frac r2+\alpha_r.
\tag{4.4}
\]

Now examine P03's newest sufficient curvature condition on the natural one-query stopping prefix. Since \(D_{x_0}F_r=q_r\),
\[
\mathcal C_{\mathcal T}=r,
\qquad Q_{\mathcal T}=\alpha_r,
\]
and therefore
\[
\boxed{
\frac{\mathcal C_{\mathcal T}}{Q_{\mathcal T}}
=\frac{2r}{1-2^{-r}}\longrightarrow\infty.
}
\tag{4.5}
\]
So no universal \(K\) can make P03's condition \(\mathcal C_{\mathcal T}\le KQ_{\mathcal T}\) hold on this natural one-step prefix, even though that prefix lands immediately in a fully certified quadratic class. This does **not** prove every possible P03 stopping tree for \(F_r\) has a large curvature/query ratio; it proves queried influence alone can badly price the direct route into the known quadratic leaf class.

The descendant-influence theorem pays exactly that missing mass. The constant child has hereditary constant zero and the quadratic child has constant one. Applying (B) at the root gives
\[
\boxed{R(F_r)\le2I(F_r).}
\tag{4.6}
\]
More explicitly, (2.2) at the root plus the weighted quadratic leaf allocation gives
\[
R(F_r)
\le\frac{\alpha_r}{\ln2}+\frac r2+\frac r2
=r+\frac{\alpha_r}{\ln2}
\le r+2\alpha_r=2I(F_r),
\tag{4.7}
\]
because \(1/\ln2<2\).

This is the demonstrated connection to P03's newest obstruction: the divergent derivative curvature is real, but it is already stored in a descendant quadratic branch whose influence can be used once and then discharged by the exact quadratic leaf certificate. The new recursion captures that bookkeeping without fresh controls or independent branches.

## 5. Scope, failures, and preserved corrections

The full FEI conjecture remains open and no universal \(C_{\rm FEI}\) is produced. P03's curvature/query condition remains a valid sufficient condition; (4.5) only shows it is too restrictive on the direct quadratic-leaf prefix for the cubic-star family. P03's reported dependent-recombination theorem is preserved as a peer dependency and is not re-claimed here; (A)--(D) are hereditary statements independent of that peer result. The cubic theorem is structural and all-dimensional but restricted. Restricted fresh-control results remain restricted. No Han absolute-overlap, pointwise erasure, fixed-drift, or resolvent lemma is revived.

## 6. Executed sanity check

Executed code:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T07-05-27+0300__check_descendant_influence.py`, created at commit `fbd0e756b91a6d46dd4f47d6f7285fe97ab88b54`.

Essential output archive:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T07-05-27+0300__descendant_influence_check.json`, created at commit `d0f01b30734640999817ea4de2466f5206ccdf43`.

The checker exhausts every Boolean truth table through dimension four, totaling **262,948 coordinate cases**, and separately evaluates the exact cubic-star formulas through \(r=16\). It reports `PASS`, with maximum observed violation exactly `0.0` for \(I(D_i f)\le I(f^+)+I(f^-)\), the curvature step (1.4), and the child-budget step (2.2). For the cubic-star family the exact curvature/query ratio grows from \(4\) at \(r=1\) to \(2097152/65535=32.000488\ldots\) at \(r=16\), while the descendant-payment hereditary upper bound stays below \(2I(F_r)\). The analytic proofs above, not the floating-point enumeration, establish the theorems.

## 7. Residual obstruction and next attack

The price in (C)--(D) is currently **restriction depth**: descendant influence may be paid once per level until the branch reaches a certified leaf. That cannot be universal without more structure. The next route is to replace worst-case depth by an **influence-lifetime potential**: charge a residual coordinate's influence only while it still participates in unresolved high-degree monomials, and try to telescope that lifetime against a fractional/transversal potential of the high-degree ANF hypergraph. The first target is cubic phases where a branch-adaptive fractional cover can be strictly smaller than the integral \(\tau_3\), while retaining exact quadratic leaf discharge. If that fails, combine the descendant payment with the preceding low-\(j\) truncation so high-folded-influence nodes are paid by marginal entropy and only low-\(j\) nodes consume descendant lifetime.

```yaml
ledger_delta:
  slot: NM13-02
  parent: T01_FEI
  parent_status_before: OPEN
  parent_status_after: OPEN
  universal_C_before: UNKNOWN
  universal_C_after: UNKNOWN
  mechanism_gain:
    local_descendant_influence_payment: PROVED
    dependent_branch_recursive_certificate: PROVED
    quadratic_leaf_depth_bound: "R <= (d+1) I"
    cubic_vertex_cover_bound: "A(f) <= tau_3(P)+1"
    cubic_star_bound: "A(F_r) <= 2"
    p03_natural_curvature_prefix_ratio: "2r/(1-2^{-r}) -> infinity"
  project_dependencies:
    p03_curvature_report: "2026-09-20T06-31-37+0300__fei-character-defect-curvature-allocation.md"
    p03_recombination: PRESERVED_PEER_RESULT_NOT_RECLAIMED
    nm13_quadratic_rank: USED
  finite_check:
    coordinate_cases: 262948
    status: PASS
  failed_or_retired_preserved:
    - Han_absolute_overlap_selector
    - pointwise_erasure_shortcut
    - fixed_coefficient_affine_drift
    - resolvent_interpolation
  next_step: "influence-lifetime / fractional high-degree-monomial cover potential, hybridized with low-j truncation if needed"
```
