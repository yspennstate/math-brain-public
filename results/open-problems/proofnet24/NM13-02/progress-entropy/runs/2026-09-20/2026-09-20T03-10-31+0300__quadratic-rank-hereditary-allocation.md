Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# NM13-02 T01 — exact hereditary allocation for quadratic Boolean phases

**Parent problem:** Friedgut--Kalai Fourier entropy--influence conjecture
\[
H(\widehat f^2)\le C\,I(f)
\]
for a universal finite constant and every Boolean function on every finite uniform cube.

**Parent status / source-level quantity before -> after:** **OPEN -> OPEN; universal finite upper bound \(C_{\rm FEI}\): UNKNOWN -> UNKNOWN.** This report does not prove full FEI and does not improve a certified universal constant.

**Mechanism-level movement:** P03's newest report reduces its dependent-branch architecture to the tree-optimized hereditary allocation ratio
\[
\mathcal A(f)=\frac1{I(f)}\inf_{\mathcal T\text{ full restriction tree}}R_{\mathcal T}(f).
\]
For every quadratic Boolean phase \(f(x)=(-1)^{q(x)}\), this run proves the exact formula
\[
\boxed{\mathcal A(f)=\frac{\operatorname{rank} M_q}{2I(f)}\le1,}
\]
and, more strongly, on every physical stopping tree,
\[
\boxed{R_{\mathcal T}(f)=S_{\mathcal T}(f)=\frac{\operatorname{rank}M_q-\sum_\ell w_\ell\operatorname{rank}M_{q_\ell}}2.}
\]
Thus the parity/erasure-synergy family that killed the earlier mixture-erasure lemma is *not* an obstruction to P03's new hereditary allocation functional: for its selector \(F_m\), \(\mathcal A(F_m)=1\) exactly, while for the restrictions \(g_0,g_1\), \(\mathcal A=(m-1)/m<1\). This is an all-dimensional theorem for a restriction-closed class and uses no fresh control variables.

Status of this result: **PARTIAL / proved in-scope, novelty UNVERIFIED.** It removes a concrete project obstruction family but not the general FEI obstruction.

## 1. Transition handoff and dependencies actually consumed

The preceding NM13-02 lane had remained admission-pending under the old residue-1 CLOSABLE assignment and had produced no successor mathematics. Its screening history is preserved untouched under `proofnet24/NM13-02/runs/`. Current `operations/PROGRESS20_2026-09-20.md` supersedes that operational role: LIVE20 now assigns NM02 to **T01 hereditary entropy/recombination theory**, paired with P03, at report root `proofnet24/NM13-02/progress-entropy`. This run therefore changes research assignment without rewriting or deleting the old admission history.

Essential dependencies read on current master:

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: T01 asks for hereditary allocation or paid dependent-branch recombination, and explicitly says restricted theorems are not full FEI.
- `operations/PROB10_2026-09-20.md`: preserves the restricted fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` under its stated control hypotheses and says it is **not** full FEI.
- `proofnet24/P03-fei/README.md`, blob `b880799e93758ca6576dfc9aa9711c1d4c32d08a`: full FEI remains open; Han's stronger all-coordinate absolute-overlap criterion is refuted by shifted thresholds; the false pointwise shortcut `H<=B+(2/ln2)I`, retired resolvent inequalities and fixed-coefficient affine-drift routes stay retired.
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`: P03 proves the exact stopping-tree telescope and a universal payment for the recombination remainder, then identifies the live obstruction as the full-tree hereditary allocation ratio `mathcal A(f)`; it expressly leaves that allocation problem to the companion worker.
- `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`: exact one-coordinate erasure/JS identity and the Boolean convolution constraints.
- `proofnet24/P03-fei/solo-2026-09-17/ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md`, blob `9c51848a64225879ba1b7ce96eecb968d14817c0`: parity synergy refutes naive mixture-erasure recombination and fixed linear interpolation potentials; its explicit family will be analyzed exactly below.
- `POSTED.md`: no posted full-FEI theorem was treated as a fresh target.

The old NM13 report had read an earlier operational state in which PROGRESS20 did not yet select NM13-02. The **current** LIVE20 table does select NM02, so that older operational conclusion is superseded; its mathematics and archived screening history are not altered.

## 2. Current source status

The public primary-source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246v2, revised 9 June 2026. It still states the full FEI inequality as a conjecture, proves new classes, and develops the restriction/stopping-tree sufficient condition rather than a universal proof. Xiao Han's published 2025 result gives the general bound
\[
H(f)=O\!\left(I(f)+\sum_i I_i(f)\log\frac1{I_i(f)}\right),
\]
which is dimension-dependent through the influence profile and is not a universal FEI constant. A bounded fresh search did not surface a later source-matching proof of full FEI. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Three routes compared before selecting the rank invariant

### Route A: marginal-influence entropy under random reveal — rejected as too loose

For a physical derivative indicator \(Y_i(x)=1_{f(x)\ne f(x^i)}\), after fixing a prefix \(X_A=a\),
\[
\operatorname{Inf}_i(f_a)=\Pr(Y_i=1\mid X_A=a).
\]
Hence \(B_i(f_a)\le h(\operatorname{Inf}_i(f_a))\). It is tempting to average this along a random coordinate order. This envelope loses the decisive spectral pairing information: for an AND-type rare pivotal event, the expected conditional binary entropy remains larger than the influence by a factor growing with dimension. So a proof through `h(local influence)` alone repeats the known logarithmic loss and was abandoned.

### Route B: parity-lift gateway — valid but only a transfer

The parity lift in the synergy/duality report has \(B=0\) at the root and restricting its selector recovers the original function. Querying that selector first therefore transfers hereditary allocation from the original function to the lift without worsening the ratio. This explains why top-level zero erasure is not itself dangerous, but it does not bound the original function and so is not enough as the main result.

### Route C: quadratic-phase polar rank — selected and completed

The explicit parity-synergy counterexample is built from quadratic phases. For quadratic phases the squared Fourier law is uniform on an affine subspace determined by the polar matrix. Conditional spectral-bit entropy is then an exact **rank drop** under principal deletion, and physical restriction deletes precisely that row/column. This creates a telescoping integer potential that survives arbitrary dependent branch selection.

## 4. Quadratic Fourier lemma

Work on \(\mathbb F_2^n\). Let
\[
q(x)=c+\ell\cdot x+\sum_{1\le i<j\le n}m_{ij}x_ix_j,
\qquad
f(x)=(-1)^{q(x)}.
\]
Let \(M\) be the symmetric zero-diagonal matrix with entries \(M_{ij}=m_{ij}\) for \(i\ne j\), and put
\[
r=\operatorname{rank}_{\mathbb F_2}M.
\]
The rank of an alternating matrix over \(\mathbb F_2\) is even.

### Lemma 4.1 (flat affine Fourier law)

The squared Fourier law of \(f\) is uniform on an affine coset of \(\operatorname{im}M\). In particular its support has size \(2^r\), each occupied atom has probability \(2^{-r}\), and
\[
\boxed{H(f)=r.}
\]

### Proof

The constant \(c\) only changes the global sign and may be ignored. Write
\[
Q(x)=\sum_{i<j}m_{ij}x_ix_j,
\qquad
B(x,y)=Q(x+y)+Q(x)+Q(y)=x^TMy.
\]
For the normalized Walsh coefficient
\[
\widehat f(s)=2^{-n}\sum_x(-1)^{q(x)+s\cdot x},
\]
expand its square and set \(z=x+y\):
\[
\widehat f(s)^2
=2^{-2n}\sum_{x,z}(-1)^{q(x)+q(x+z)+s\cdot z}.
\]
Now
\[
q(x+z)+q(x)=\ell\cdot z+Q(z)+x^TMz.
\]
The sum over \(x\) is zero unless \(Mz=0\), in which case it equals \(2^n\). Therefore
\[
\widehat f(s)^2
=2^{-n}\sum_{z\in\ker M}(-1)^{\ell\cdot z+Q(z)+s\cdot z}.
\tag{4.1}
\]
On \(\ker M\), the map \(d(z)=\ell\cdot z+Q(z)\) is linear because its polarization is \(z^TMz'=0\). Thus (4.1) is the Fourier transform of a character of \(\ker M\): it equals \(2^{-n}|\ker M|=2^{-r}\) exactly when \(s\) lies in one affine coset of \((\ker M)^\perp=\operatorname{im}M\), and it is zero otherwise. Hence the law is uniform on \(2^r\) points and has entropy \(r\). QED.

## 5. One-coordinate hereditary entropy is exactly half a rank drop

For coordinate \(i\), let \(M_{-i}\) denote the principal submatrix obtained by deleting row and column \(i\), and set \(r_i=\operatorname{rank}M_{-i}\).

### Lemma 5.1

For the spectral random vector \(Z\) of a quadratic phase,
\[
\boxed{B_i(f):=H(Z_i\mid Z_{-i})=\frac{r-r_i}{2}\in\{0,1\}.}
\tag{5.1}
\]

### Proof

By Lemma 4.1, \(Z\) is uniform on an affine coset \(a+V\) with \(V=\operatorname{im}M\). Projection onto all coordinates except \(i\) has fibers of size two iff its kernel on \(V\) is \(\{0,e_i\}\), i.e. iff \(e_i\in V\); otherwise every fiber has size one. Therefore
\[
B_i(f)=1_{\{e_i\in\operatorname{im}M\}}.
\tag{5.2}
\]
It remains to identify this indicator with the rank drop.

Write \(M\), after moving coordinate \(i\) first, as
\[
M=\begin{pmatrix}0&v^T\\ v&N\end{pmatrix},\qquad N=M_{-i}.
\]
Deleting one row and column changes rank by at most two; both \(M,N\) are alternating, so \(r-r_i\in\{0,2\}\).

Also \(\operatorname{im}M=(\ker M)^\perp\), hence \(e_i\notin\operatorname{im}M\) iff some kernel vector of \(M\) has first coordinate one. Such a vector has form \((1,u)\) and satisfies \(Nu=v\) and \(v^Tu=0\); the latter is automatic when \(Nu=v\) because \(u^TNu=0\) for alternating \(N\). Thus \(e_i\notin\operatorname{im}M\) iff \(v\in\operatorname{im}N\). In that case the first row/column adds no rank and \(r=r_i\).

Conversely, if \(e_i\in\operatorname{im}M\), then \(v\notin\operatorname{im}N\), so the alternating bordered matrix adds two to the rank and \(r=r_i+2\). Combining with (5.2) gives (5.1). QED.

## 6. Restriction preserves the quadratic matrix by principal deletion

Fixing the physical bit \(x_i=a\) removes every monomial containing \(x_i\). The quadratic part on the remaining variables is exactly the principal matrix \(M_{-i}\); only the linear term changes with the branch value \(a\). Therefore **both children have the same quadratic rank \(r_i\)**, even though their affine Fourier-support cosets may differ.

By Lemma 4.1,
\[
\frac{H(f_{i=0})+H(f_{i=1})}{2}=r_i.
\]
So the full one-step entropy decrement is
\[
\Delta_i(f)=r-r_i.
\tag{6.1}
\]
Together with Lemma 5.1 and P03's exact decomposition \(\Delta_i=B_i+J_i^{\rm rec}\), this yields an exact balance unavailable for general functions:
\[
\boxed{J_i^{\rm rec}(f)=B_i(f)=\frac{r-r_i}{2}.}
\tag{6.2}
\]
Thus a rank-preserving query has zero allocation and zero recombination cost; a rank-dropping query drops rank by two and contributes exactly one bit to each.

## 7. The stopping-tree rank telescope

Let \(\mathcal T\) be **any** finite adaptive physical restriction tree for the quadratic phase \(f\). At node \(v\), write \(r_v\) for the rank of the quadratic matrix of the current restriction and \(w_v\) for the usual branch weight. If \(v\) queries coordinate \(i(v)\), both children have the same rank \(r'_v\), namely the rank of the corresponding principal deletion.

From (5.1) and (6.2),
\[
B_{i(v)}(f_v)=J^{\rm rec}_{i(v)}(f_v)=\frac{r_v-r'_v}{2}.
\]
Multiply by \(w_v\) and sum over internal nodes. Since the two child weights sum to \(w_v\), the rank terms telescope exactly:
\[
\boxed{
R_{\mathcal T}(f)=S_{\mathcal T}(f)
=\frac{r-\sum_{\ell\text{ leaf}}w_\ell r_\ell}{2}.}
\tag{7.1}
\]
This proof permits the queried coordinate to depend arbitrarily on the earlier physical branch; no common order and no branch independence is used.

For a **full** restriction tree every leaf is constant and has rank zero. Hence every full tree, not merely an optimized one, satisfies
\[
\boxed{R_{\mathcal T}(f)=S_{\mathcal T}(f)=r/2.}
\tag{7.2}
\]
This is the promised hereditary allocation theorem.

## 8. Exact tree-optimized ratio and FEI consequence for quadratic phases

For coordinate \(i\), the Boolean derivative of the quadratic phase is the affine linear phase
\[
q(x+e_i)+q(x)=\ell_i+\sum_{j\ne i}M_{ij}x_j.
\]
If row \(i\) of \(M\) is nonzero, this affine form is balanced and
\[
\operatorname{Inf}_i(f)=1/2.
\]
If the row is zero, the derivative is constant and the influence is \(0\) or \(1\) according to the linear coefficient.

Let \(d\) be the number of nonzero rows of \(M\), and let \(h\) be the number of zero rows carrying linear coefficient one. Then
\[
I(f)=d/2+h.
\tag{8.1}
\]
Since the rank \(r\) is at most the number \(d\) of nonzero rows,
\[
\frac r2\le \frac d2\le I(f).
\tag{8.2}
\]
For every nonconstant quadratic phase, P03's full-tree functional therefore has the exact value
\[
\boxed{
\mathcal A(f)=\frac{r}{2I(f)}\le1.}
\tag{8.3}
\]
Also Lemma 4.1 and (8.2) give the direct class theorem
\[
\boxed{H(f)=r\le 2I(f).}
\tag{8.4}
\]
Equation (8.4) is a restricted-class FEI theorem, not full FEI. The sharper mechanism statement for the current project is (7.1)--(8.3): the P03 hereditary allocation obstruction is exactly solved on a nontrivial restriction-closed class with maximal branch dependence.

## 9. Application to P03's erasure-synergy counterexample

P03's preserved counterexample uses odd \(m\ge3\), \(r=m-1\), the bent quadratic phase
\[
b(t)=(-1)^{t_1t_2+t_3t_4+\cdots+t_{r-1}t_r},
\]
then
\[
g_0(y)=b(y_1+y_m,\ldots,y_{m-1}+y_m),
\qquad
g_1(y)=(-1)^{y_m}g_0(y),
\]
and a selector \(F(z,y)\) with restrictions \(g_0,g_1\).

All three are quadratic phases: indeed
\[
F(z,y)=g_0(y)(-1)^{zy_m}.
\]
For \(g_0\), the quadratic polar matrix has rank \(m-1\), while every physical row is nonzero. Therefore
\[
H(g_0)=m-1,\qquad I(g_0)=m/2,
\qquad
\boxed{\mathcal A(g_0)=\frac{m-1}{m}<1,}
\]
and the same holds for \(g_1\).

For \(F\), adding the selector edge \(z y_m\) makes the alternating polar matrix full rank \(m+1\). Every row is nonzero, so
\[
H(F)=m+1,\qquad I(F)=(m+1)/2,
\qquad
\boxed{\mathcal A(F)=1.}
\]
Thus the family for which one mixing bit creates \(m\) units of aggregate erasure and destroys the naive mixture inequality has a perfectly bounded tree-optimized hereditary allocation ratio. The failure mechanism in the old lemma is therefore **not inherited by P03's new \(\mathcal A\) obstruction**.

There is also an exact explanation of where the entropy goes: on every full physical restriction tree for \(F\),
\[
R_{\mathcal T}(F)=S_{\mathcal T}(F)=(m+1)/2.
\]
Half of the spectral entropy is hereditary allocation and half is true dependent-branch recombination. The latter is not a small-error perturbation, but it is organized exactly by the same rank potential.

This does not address the shifted-threshold obstruction to Han's absolute-overlap criterion; those functions are not quadratic phases. It instead removes the separate parity-synergy/branch-dependence obstruction from the live allocation architecture.

## 10. Exact sanity check executed

The exact checker created in this run is

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T03-10-31+0300__check_quadratic_allocation.py`.

Actual archived output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T03-10-31+0300__quadratic_allocation_check.json`.

It uses integer Walsh transforms and GF(2) Gaussian elimination. It exhaustively checked every quadratic coefficient choice and every linear term through dimension five (constant/global sign omitted because it changes neither squared spectrum nor influence):

- n=1: 2 forms;
- n=2: 8 forms;
- n=3: 64 forms;
- n=4: 1024 forms;
- n=5: 32768 forms.

For every checked form it verified: support size \(2^r\); equal nonzero squared Walsh magnitude; the exact identity \(B_i=(r-r_i)/2\); and the derivative/influence classification above. It also checked the full fixed-order rank telescope for every quadratic matrix and every coordinate order through n=4 (1536 order instances at n=4). Finally it checked the P03 synergy family at m=3,5,7,9, obtaining
\[
\mathcal A(F_m)=1,
\qquad
\mathcal A(g_0)=\frac{m-1}{m}.
\]
The archived result is `status: PASS`. These finite checks are self-checks only; the theorem is the algebraic proof above.

## 11. What failed, what moved, and what remains

**Failed route 1:** replacing \(B_i\) by binary entropy of local influence under random reveal reproduces a logarithmic loss and discards spectral adjacency.

**Failed route 2 as a standalone closure:** querying the parity-lift gateway first transfers allocation but cannot control an arbitrary base function, so it is a reduction rather than a bound.

**Successful route:** quadratic polar rank is an exact hereditary potential. It handles arbitrary dependent physical branching and gives exact allocation/recombination accounting.

**Demonstrated mechanism gain:** the project previously had a parity-synergy family showing that branch mixing could amplify erasure by an arbitrarily large amount and thereby refuting a proposed local mixture lemma. The present theorem proves that this entire family has `mathcal A<=1` (exactly 1 at the selector). Hence P03's new allocation functional survives that obstruction for a structural reason, not by finite enumeration.

**Remaining full-scope obstruction:** prove \(\sup_f\mathcal A(f)<\infty\) for arbitrary Boolean functions, or replace it by another source-valid hereditary quantity. Nothing here controls shifted thresholds, arbitrary cubic/higher-degree phases, or general Boolean spectra.

A concrete next attack is to keep the rank telescope as the solved degree-two base and study **quadratic-leaf stopping trees for sparse cubic phases**: query a hitting set of cubic monomials until every leaf is quadratic, then bound only the pre-leaf hereditary allocation. The branch-dependent change of the quadratic polar matrix is the first genuinely new term; if its rank variation can be paid by the influence charged on the cubic hitting set, this extends the exact mechanism without reverting to fresh controls or the refuted absolute-overlap criterion.

## 12. ledger_delta

```yaml
ledger_delta:
  worker: NM13-02
  assignment: T01_Fourier_entropy_influence_theory
  companion: P03
  parent_problem: Friedgut_Kalai_FEI
  parent_status_before: OPEN
  parent_status_after: OPEN
  parent_metric: universal_finite_C_FEI
  parent_metric_before: UNKNOWN
  parent_metric_after: UNKNOWN
  source_level_movement: false
  mechanism_metric: tree_optimized_hereditary_allocation_ratio_mathcal_A
  mechanism_before: no_bound_on_P03_parity_synergy_family_under_new_full_tree_functional
  mechanism_after: exact_A_equals_rank_M_over_2I_le_1_for_all_quadratic_Boolean_phases
  theorem_scope:
    class: all_quadratic_phases_over_F2_all_dimensions
    hereditary_under_physical_restriction: true
    arbitrary_adaptive_restriction_tree: true
    fresh_controls: false
  exact_tree_identity: R_T_equals_S_T_equals_half_root_rank_minus_half_weighted_leaf_rank
  direct_class_FEI_constant: 2
  p03_synergy_application:
    selector_Fm_A: 1
    restriction_g0_g1_A: (m-1)/m
  proof_label: PARTIAL_PROVED_SELF_CHECKED
  novelty: UNVERIFIED
  finite_checker_status: PASS
  exhaustive_quadratic_phase_dimension: 5
  full_order_telescope_dimension: 4
  parent_full_FEI_claimed: false
  restricted_fresh_control_result_preserved: true
  false_lemmas_revived: false
  old_NM13_admission_history_overwritten: false
  substantive_unchanged_run_count: 0
  next_obstruction: paid_rank_variation_before_quadratic_leaves_for_sparse_cubic_phases
  artifacts:
    - proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T03-10-31+0300__check_quadratic_allocation.py
    - proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T03-10-31+0300__quadratic_allocation_check.json
```
