Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — paid dependent-branch recombination and hereditary block refinement

**Source target:** Friedgut--Kalai Fourier entropy--influence conjecture on finite uniform cubes:
\[
\mathbf H(f)\le C\,\mathbf I(f)
\]
for one universal finite constant and every Boolean function.

**Status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved here. The source-level quantity “finite universal upper bound for \(C_{\rm FEI}\)” remains **UNKNOWN -> UNKNOWN**. The inherited native P03 finite-dimensional atlas value remains the previously reported **6 -> 6**; it was not extended and is not promoted as full-scope progress.

**Mechanism-level movement:** a fresh-variable-free **paid dependent-branch recombination theorem** is proved below. For an arbitrary adaptive physical restriction tree, every entropy loss not belonging to hereditary erasure allocation is paid by at most \((2/\ln2)\) times the tree’s actually charged influence. For a physical block \(A\), every ordered singleton refinement has hereditary erasure within the same paid additive budget of the coarse block conditional entropy. Consequently, allowing larger physical blocks does not evade the hereditary allocation obstruction: coarse proper-block selection and ordered hereditary allocation are equivalent up to the already-paid additive constant \(2/\ln2\). The remaining full-scope problem is the hereditary allocation bound itself, not dependent branch recombination.

This is an all-dimensional structural theorem and not a restricted fresh-control inequality. It introduces no fresh variables and assumes no independence between branches.

## 1. Dependencies actually consumed

Current master was read under the progress-first directive. The following complete dependencies were used rather than a whole-archive scan.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: T01 asks specifically for hereditary entropy allocation or paid dependent-branch recombination without fresh-control dependence; restricted theorems do not close FEI.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the current restricted starting point is `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` under fresh controls and `2^{-c}M_0(f)<=1`; this is explicitly not full FEI.
- `proofnet24/P03-fei/README.md`, blob `b880799e93758ca6576dfc9aa9711c1d4c32d08a`: full FEI remains open; Han’s stronger all-coordinate absolute-overlap criterion is now refuted by the shifted-threshold family; the prior false resolvent, erasure and drift shortcuts remain retired.
- `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T16-28-42Z__OWNER_FEI_RECOVERY_CONTINUATION.md`, blob `9a78d276550d45b9a9aa42cc072fb93166284bc3`: preserves the strengthened coding obstruction, the 27-variable zero-boundary-decomposition obstruction, and the unchanged native atlas. No current metric was reset.
- `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T22-18-30Z__report.md`, blob `22362306d41f9b6d3d0f221ddda3d303b8a47968`: reconstructs the fresh-control latent-mixture theorem and its exact scope. Nothing below uses fresh controls.
- `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`: exact one-coordinate erasure/JS identity and the sharp-enough universal JS payment used below.
- `proofnet24/P03-fei/solo-2026-09-17/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md`, blob `5a6790b95c7d44c85fa5507623f3129e1c48ede9`: exact coarse block entropy identity and block channel payment. The present theorem does **not** re-claim that identity; it compares the coarse block term to every hereditary singleton refinement and gives an aggregate stopping-tree criterion.
- `proofnet24/P03-fei/solo-2026-09-17/ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md`, blob `9c51848a64225879ba1b7ce96eecb968d14817c0`: parity-synergy refutes naive mixture-erasure recombination, and `D=H-B` is FEI-complete. The theorem below is designed to survive that obstruction.
- `proofnet24/P03-fei/continuations/2026-09-20-shifted-thresholds/REPORT.md`: the new symmetric shifted-threshold obstruction to Han’s stronger coordinate criterion was read so that no refuted selector condition is silently reused.
- `POSTED.md`: exact-scope exclusions were checked. Nothing below duplicates a posted full-FEI result.

The companion path expected from the new LIVE20 map, `proofnet24/NM13-02/progress-entropy`, was not present on current master when checked. No peer file or claim was edited. This run therefore takes the complementary precise scope “dependent-branch recombination/refinement”; the remaining allocation problem is left available to the companion worker.

## 2. Current primary-source scope

The current arXiv version of González--MacManus--Pereyra, arXiv:2606.00246, still states full FEI as open and develops a restriction induction/stopping-tree approach. Its sufficient stopping-tree condition requires the entropy decrement inequality at every branching node (or a known FEI bound at a stopping leaf). The theorem below weakens the *proof architecture*: local bad nodes may be compensated by other nodes, because only the weighted aggregate hereditary-erasure allocation needs a bound. It does **not** prove that aggregate bound for every Boolean function.

The source conjecture is the Friedgut--Kalai universal inequality. No bounded literature search is treated as a novelty certificate.

## 3. Notation and the one-step identity

Let \(g:\{-1,1\}^V\to\{-1,1\}\) be Boolean and let \(Z\) be its spectral random subset,
\[
\Pr(Z=S)=\widehat g(S)^2.
\]
For a physical coordinate \(i\in V\), write
\[
B_i(g):=H(Z_i\mid Z_{V\setminus\{i\}}).
\]
Let \(g^+,g^-\) be the two restrictions at \(x_i=+1,-1\). Define the nonnegative one-step recombination remainder
\[
J_i^{\rm rec}(g)
:=H(g)-\frac{H(g^+)+H(g^-)}2-B_i(g).
\tag{3.1}
\]
The already-proved erasure/JS identity identifies this with the Jensen--Shannon divergence between the two restriction spectral laws. In particular,
\[
0\le J_i^{\rm rec}(g)
\le \frac{2}{\ln2}\,j_i(g),
\qquad
j_i(g):=\min\{\operatorname{Inf}_i(g),1-\operatorname{Inf}_i(g)\}.
\tag{3.2}
\]
We also use the exact influence decomposition
\[
I(g)=\frac{I(g^+)+I(g^-)}2+\operatorname{Inf}_i(g).
\tag{3.3}
\]
No new claim is made for (3.1)--(3.3); they are the inputs.

## 4. Theorem A — paid dependent-branch recombination on an arbitrary stopping tree

A finite **physical restriction tree** \(\mathcal T\) starts at \(f\). At an internal node \(v\), some coordinates have already been fixed, the current Boolean restriction is \(f_v\), and one still-free physical coordinate \(i(v)\) is split into its two signs. The two children have equal conditional probability. The choice \(i(v)\) may depend arbitrarily on the previous physical branch; there is no common coordinate order requirement.

Give a node at depth \(d\) weight \(w_v=2^{-d}\). Define
\[
\begin{aligned}
R_{\mathcal T}(f)
&:=\sum_{v\text{ internal}} w_v B_{i(v)}(f_v),\\
S_{\mathcal T}(f)
&:=\sum_{v\text{ internal}} w_v J^{\rm rec}_{i(v)}(f_v),\\
Q_{\mathcal T}(f)
&:=\sum_{v\text{ internal}} w_v\operatorname{Inf}_{i(v)}(f_v),\\
J_{\mathcal T}(f)
&:=\sum_{v\text{ internal}} w_v j_{i(v)}(f_v),
\end{aligned}
\tag{4.1}
\]
and the weighted leaf quantities
\[
H_L:=\sum_{\ell\text{ leaf}}w_\ell H(f_\ell),
\qquad
I_L:=\sum_{\ell\text{ leaf}}w_\ell I(f_\ell).
\tag{4.2}
\]

**Theorem A (exact tree telescope and paid recombination).** Every such tree satisfies
\[
\boxed{H(f)-H_L=R_{\mathcal T}(f)+S_{\mathcal T}(f)},
\tag{4.3}
\]
\[
\boxed{I(f)-I_L=Q_{\mathcal T}(f)},
\tag{4.4}
\]
and
\[
\boxed{0\le S_{\mathcal T}(f)
\le \frac{2}{\ln2}J_{\mathcal T}(f)
\le \frac{2}{\ln2}Q_{\mathcal T}(f)}.
\tag{4.5}
\]
In particular, if all leaves satisfy
\[
H(f_\ell)\le C_0 I(f_\ell)
\tag{4.6}
\]
and the tree has the **aggregate hereditary allocation bound**
\[
R_{\mathcal T}(f)\le K Q_{\mathcal T}(f),
\tag{4.7}
\]
then
\[
\boxed{H(f)\le
\max\left\{C_0,K+\frac2{\ln2}\right\}I(f)}.
\tag{4.8}
\]

### Proof

At one internal node \(v\), multiply (3.1) by \(w_v\):
\[
w_v H(f_v)-\sum_{u\text{ child of }v}w_u H(f_u)
=w_v B_{i(v)}(f_v)+w_vJ^{\rm rec}_{i(v)}(f_v),
\]
because each child has weight \(w_v/2\). Sum over all internal nodes. Every nonroot internal entropy occurs once positively and once negatively, so the left side telescopes to \(H(f)-H_L\), proving (4.3).

Applying the same weighted telescoping to (3.3) proves (4.4).

Equation (4.5) follows term by term from (3.2) and \(j_i(g)\le\operatorname{Inf}_i(g)\).

Finally, (4.3), (4.5), (4.6) and (4.7) give
\[
H(f)\le C_0I_L+\left(K+\frac2{\ln2}\right)Q_{\mathcal T}.
\]
Using (4.4), \(I_L+Q_{\mathcal T}=I(f)\), so the last expression is at most the right side of (4.8). QED.

### Why this is stronger than a nodewise stopping-tree hypothesis

The source stopping-tree ansatz pays the full entropy decrement locally at every branching node. Theorem A needs no local inequality of the form \(B_i(f_v)\le K\operatorname{Inf}_i(f_v)\), nor the stronger full-decrement version. A node with arbitrarily bad local ratio is allowed provided the **weighted sum over all dependent branches** satisfies (4.7). Branches are not made independent and no fresh control coordinate is introduced.

Thus the dependent recombination part of the induction has a universal payment already. The live full-FEI obstruction becomes the hereditary allocation quantity \(R_{\mathcal T}\).

## 5. Theorem B — every coarse physical block is equivalent to hereditary singleton allocation up to the same paid constant

Let \(A\subseteq[n]\) be a nonempty physical block and \(C=[n]\setminus A\). Fix **any** ordering
\[
\pi=(i_1,\dots,i_k)
\]
of \(A\). For \(t\ge1\), let \(X_{<t}\) be the uniformly random physical assignments already fixed at \(i_1,\dots,i_{t-1}\), and write \(f_{X_{<t}}\) for that restriction. Define
\[
R_{\pi,A}(f):=
\sum_{t=1}^k
\mathbb E_{X_{<t}}B_{i_t}(f_{X_{<t}}),
\tag{5.1}
\]
\[
J_{\pi,A}(f):=
\sum_{t=1}^k
\mathbb E_{X_{<t}}
\min\{\operatorname{Inf}_{i_t}(f_{X_{<t}}),
1-\operatorname{Inf}_{i_t}(f_{X_{<t}})\}.
\tag{5.2}
\]
Let \(Z\) be the original spectral subset of \(f\).

**Theorem B (hereditary refinement sandwich).** For every Boolean \(f\), every block \(A\), and every ordering \(\pi\),
\[
\boxed{
0\le H(Z_A\mid Z_C)-R_{\pi,A}(f)
\le \frac2{\ln2}J_{\pi,A}(f)
\le \frac2{\ln2}I_A(f).}
\tag{5.3}
\]
Moreover the nonnegative refinement gap has the exact information representation
\[
\boxed{
H(Z_A\mid Z_C)-R_{\pi,A}(f)
=\sum_{t=1}^k I(X_{<t};K_t\mid Y_t),}
\tag{5.4}
\]
where, conditional on \(X_{<t}=x\), \((K_t,Y_t)\) is sampled from the squared Fourier law of the restriction \(f_x\); \(K_t\) is the spectral bit at the current physical coordinate \(i_t\), and \(Y_t\) is the collection of spectral bits on \(i_{t+1},\dots,i_k\) and on \(C\).

### Proof of the exact nonnegative gap

For a fixed prefix assignment \(x\), let \(q_x^{(t)}\) be the squared Fourier law of \(f_x\) on the remaining coordinates. Averaging \(q_x^{(t)}\) over the uniform physical prefix \(x\) gives exactly the marginal of the original spectral law obtained by summing out the earlier Fourier coordinates \(i_1,\dots,i_{t-1}\). This is partial Fourier Parseval: if a remaining Fourier coefficient of the restriction is expanded as a Walsh polynomial in the prefix assignment, averaging its square kills the cross terms and leaves the sum of the corresponding original squared Fourier coefficients.

Therefore the \(t\)-th chain-rule term of the coarse conditional entropy is
\[
H(Z_{i_t}\mid Z_{i_{t+1}},\dots,Z_{i_k},Z_C)
=H(K_t\mid Y_t)
\]
under the mixture joint law obtained by first taking uniform \(X_{<t}\) and then sampling from \(q_{X_{<t}}^{(t)}\). The \(t\)-th term of (5.1) is
\[
\mathbb E_{X_{<t}}H_{q_{X_{<t}}^{(t)}}(K_t\mid Y_t)
=H(K_t\mid Y_t,X_{<t}).
\]
Their difference is exactly
\[
I(X_{<t};K_t\mid Y_t)\ge0.
\]
Summing the chain rule over \(t\) proves (5.4), hence the first inequality in (5.3). This argument is where parity-type branch dependence is retained rather than replaced by an independent-mixture surrogate.

### Proof of the paid upper bound

Write
\[
D_A(f):=H(f)-\mathbb E_{x_A}H(f_{x_A}).
\]
The pre-existing exact coarse block identity gives
\[
D_A(f)=H(Z_A\mid Z_C)+M_A(f),
\qquad M_A(f)\ge0,
\tag{5.5}
\]
where \(M_A\) is the physical-block/spectral-output mutual information.

Now execute the ordered singleton restriction tree \(\pi\) through all coordinates of \(A\). Theorem A, stopped after \(A\) is fixed, gives
\[
D_A(f)=R_{\pi,A}(f)+S_{\pi,A}(f),
\tag{5.6}
\]
with
\[
S_{\pi,A}(f)\le \frac2{\ln2}J_{\pi,A}(f).
\tag{5.7}
\]
Subtract (5.5) from (5.6):
\[
H(Z_A\mid Z_C)
=R_{\pi,A}+S_{\pi,A}-M_A
\le R_{\pi,A}+\frac2{\ln2}J_{\pi,A}.
\]
This proves the middle inequality of (5.3).

Finally, iterating (3.3) through the coordinates of \(A\) and comparing with the exact block influence decomposition gives
\[
\sum_{t=1}^k
\mathbb E_{X_{<t}}
\operatorname{Inf}_{i_t}(f_{X_{<t}})
=I_A(f).
\tag{5.8}
\]
Since each folded influence in (5.2) is at most the corresponding ordinary influence, (5.8) proves the final inequality. QED.

## 6. Corollary — proper-block selection and hereditary allocation are the same obstruction up to a paid constant

Theorem B has two immediate directions.

1. If a useful proper block \(A\) satisfies
   \[
   H(Z_A\mid Z_C)\le K I_A(f),
   \]
   then **every** ordering of that same block satisfies
   \[
   R_{\pi,A}(f)\le K I_A(f).
   \]

2. Conversely, if for some ordering of a proper block
   \[
   R_{\pi,A}(f)\le K I_A(f),
   \]
   then
   \[
   H(Z_A\mid Z_C)
   \le\left(K+\frac2{\ln2}\right)I_A(f).
   \]

Thus enlarging from singleton hereditary restrictions to coarse physical blocks cannot by itself evade the allocation problem. Coarse recombination costs only the already-paid \(2/\ln2\) term. The only unbounded quantity left is the hereditary erasure allocation \(R\).

For \(A=[n]\), this specializes to every full physical restriction order:
\[
R_{\pi,[n]}(f)\le H(f)
\le R_{\pi,[n]}(f)+\frac2{\ln2}I(f).
\tag{6.1}
\]
Hence a universal bound on accumulated hereditary erasure along even one universally available order-selection rule is equivalent, up to the displayed additive constant, to full FEI. Equation (6.1) is a reduction, not a solution: no universal \(R_{\pi}/I\) bound is proved here.

## 7. What obstruction was removed, and what remains

The progress target requested either hereditary allocation or a **paid dependent-branch recombination estimate without fresh-variable dependence**. The latter is now proved in Theorems A--B.

What is removed:

- no fresh controls are needed to pay recombination;
- no independence between physical branches is assumed;
- a stopping tree may contain locally bad splitting nodes;
- larger physical blocks do not create an additional uncontrolled synergy term beyond the universal JS/channel payment;
- the parity-synergy counterexample does not invalidate the theorem because its synergy is retained in the exact conditional mutual-information refunds (5.4), rather than discarded.

What remains exactly:

> Prove that every Boolean function admits a stopping restriction tree (or a proper block/order recursively) for which the aggregate hereditary erasure satisfies \(R_{\mathcal T}\le KQ_{\mathcal T}\) with one universal finite \(K\); or construct a Boolean family for which the optimal such ratio diverges.

This is now a sharper target than “control branch recombination”. It is also directly comparable to arXiv:2606.00246: their local branching inequality is sufficient, while Theorem A shows that a weighted aggregate allocation inequality is sufficient even when individual nodes fail.

A natural next attack is therefore on the **tree-optimized allocation ratio**
\[
\mathcal A(f):=
\inf_{\mathcal T\text{ full restriction tree}}
\frac{R_{\mathcal T}(f)}{Q_{\mathcal T}(f)}
=\frac1{I(f)}\inf_{\mathcal T}R_{\mathcal T}(f),
\tag{7.1}
\]
for nonconstant \(f\). Full FEI follows from \(\sup_f\mathcal A(f)<\infty\), and FEI itself implies this finiteness up to the same additive constant by (6.1). The important point is that \(\mathcal A\) is hereditary and uses only original physical coordinates; there is no fresh-variable escape hatch.

No claim is made here that a greedy coordinate rule controls \(\mathcal A\).

## 8. Failed routes explicitly preserved

Nothing in this run revives any of the following:

- the false all-constant scalar or full-resolvent pointwise estimates;
- the false pointwise erasure shortcut;
- the false resource potential `M<=a v+b delta_M` for fixed finite nonnegative coefficients;
- the refuted coefficient-four entropy-drift potential;
- the false zero-artificial-boundary decomposition;
- Han’s now-refuted universal all-coordinate absolute-overlap selector criterion.

The fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` remains valid only under its stated added-control hypothesis and is not used to claim (4.8) or (5.3).

## 9. Sanity checks executed this run

A new checker was executed on the theorem’s finite identities before persistence. It exhausts every Boolean function in dimensions 1, 2 and 3, every nonempty physical block and every order of that block, and additionally checks 50 fixed-seed random Boolean functions in dimension 4. It checks
\[
0\le H(Z_A\mid Z_C)-R_{\pi,A}
\le (2/\ln2)I_A
\]
and the exact chain decomposition of the refinement gap.

Recorded result:

```json
{
  "status": "PASS",
  "cases": 7108,
  "exhaustive_dimensions": [1, 2, 3],
  "random_dimension_4_functions": 50,
  "random_seed": 1,
  "min_refinement_gap": -2.220446049250313e-16,
  "max_gap_over_I_A": 1.3983932542605313,
  "theorem_upper_constant_2_over_ln2": 2.8853900817779268,
  "max_chain_identity_error": 2.220446049250313e-16
}
```

The tiny negative minimum and identity error are machine-roundoff scale. Universal validity rests on the written proof, not on enumeration.

Artifacts:

- `proofnet24/P03-fei/artifacts/2026-09-20T02-31-19+0300/check_refinement_recombination.py`, creation commit `5a144af36009c35c6ba44c8baf2c40bd8ad7afa5`.
- `proofnet24/P03-fei/artifacts/2026-09-20T02-31-19+0300/refinement_recombination_check.json`, creation commit `6cb9e47d047c315b624b99c2b46927d561a7ca39`.

These are self-checks, not independent audits.

## 10. Prior-art/source check and novelty qualification

The current arXiv:2606.00246 source was checked in its present 2026 version. It states full FEI as open and uses a local restriction/stopping-tree inequality; it does not, in the inspected scope, supply the aggregate hereditary allocation theorem above. Friedgut--Kalai remains the source conjecture. The new shifted-threshold continuation was also checked to avoid reusing Han’s stronger false selector condition.

This was a bounded source check, not comprehensive priority clearance. Theorems A--B are therefore **PROVED IN THIS REPOSITORY / PRIORITY UNVERIFIED**, not claimed publication-novel.

## 11. Before/after accounting

### Original FEI scope

- Universal finite \(C\) for all Boolean functions: **OPEN -> OPEN**.
- Universal upper bound actually established: **none -> none**.
- Native finite-dimensional atlas: **6 -> 6**, unchanged and not counted as full-scope movement.
- Fresh-control restricted theorem: unchanged and still restricted.

### Mechanism scope

Before this run, the block identity isolated an uncontrolled coarse conditional entropy and parity synergy showed naive branch-mixture erasure can blow up. The new theorem proves that the *recombination difference between coarse blocks and hereditary singleton restrictions is universally paid* by at most \((2/\ln2)\) times the actually charged folded influence. An arbitrary adaptive stopping tree likewise needs only an aggregate allocation bound; local bad nodes are allowed.

This removes **dependent-branch recombination** as a separate unbounded obstruction and leaves a single named obstruction: hereditary allocation \(R_{\mathcal T}/Q_{\mathcal T}\).

## 12. Next mathematical attack

Do not spend the next run reproving the recombination theorem. Attack \(\mathcal A(f)\) in (7.1) directly.

The most informative next alternatives are:

1. prove a universal recursive selector bound for \(\mathcal A\) using the signed Boolean convolution constraints \(\sum_S \widehat f(S)\widehat f(S\triangle U)=0\), not marginal entropy alone;
2. stress-test \(\mathcal A\) analytically on the one-point, recursive-majority, parity-lift and shifted-threshold obstruction families and determine whether any family forces divergence;
3. if two distinct selector mechanisms fail, switch to the direct logarithmic-edge subproblem rather than returning to resolvent/drift tuning.

The companion entropy worker should take the hereditary allocation/selector side; P03 has now supplied the complementary paid recombination lemma.

## ledger_delta

```yaml
track: P03
parent: Friedgut--Kalai FEI
source_status_before: OPEN_PARTIAL
source_status_after: OPEN_PARTIAL
source_metric:
  universal_FEI_upper_bound_before: UNKNOWN
  universal_FEI_upper_bound_after: UNKNOWN
  native_finite_dimension_atlas_before: 6
  native_finite_dimension_atlas_after: 6
mechanism_added:
  name: HEREDITARY_DEPENDENT_BRANCH_RECOMBINATION
  status: PROVED_SELF_CHECKED_PRIORITY_UNVERIFIED
  statement: >-
    For every adaptive physical restriction tree, entropy loss equals hereditary
    erasure allocation plus a recombination remainder bounded by (2/ln2) times
    the tree's charged folded influence. For every physical block and every
    singleton ordering, coarse block conditional entropy differs from hereditary
    sequential erasure by a nonnegative refinement refund and by at most the
    same paid budget.
full_FEI_closed: false
fresh_variable_dependence_removed_for_recombination: true
remaining_obligation: >-
  Bound the tree-optimized hereditary allocation ratio R_T/Q_T by a universal
  constant, or construct a Boolean family showing that this route diverges.
failed_routes_preserved:
  - full_resolvent_pointwise
  - scalar_resource_potential
  - pointwise_erasure_shortcut
  - coefficient_four_entropy_drift
  - zero_boundary_decomposition
  - Han_absolute_overlap_selector
peer_files_edited: false
```

**End of complete run report.**
