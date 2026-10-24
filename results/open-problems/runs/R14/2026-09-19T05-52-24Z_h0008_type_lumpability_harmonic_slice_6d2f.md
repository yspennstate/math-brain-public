Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf = a_hi-a_lo -> same`; this is the first unchanged H0008 run after the preceding certification movement. Methods actually used: #2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY, #20 FIND WHY THE ALGORITHM FAILS.**

# R14 HARD OUTSIDE — H0008 harmonic measure: exact type-lumpability slice and the obstruction beyond it

## 0. Continuity, ownership, and fixed metric

I preserve all prior R14 hard-task handoffs. I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034. The active exclusive R14 claim remains `operations/claims/H0008.md`, Achyut Kumar (2026), arXiv:2608.15987v1, Section 12.3 open problem (6), **Boundary fluctuations**.

The source asks for fluctuation theory on the failed boundary: the multifractal spectrum of transmission-weighted flows and the harmonic measure of the failed cluster, where a dimension drop is expected. The preceding R14 run completed the finite-type multifractal clause under its stated hypotheses and certified the frozen metric exactly as

\[
I_{\rm mf}=a_{\rm hi}-a_{\rm lo}.
\]

This run attacks the remaining harmonic-measure clause. It does not enlarge that already-maximal multifractal exponent interval, so the fixed metric has **no movement**.

A fresh source check on 19 September 2026 found arXiv:2608.15987 still at v1, submitted 17 August 2026. Its Section 12.3 still states Boundary fluctuations as open and explicitly names the harmonic measure/dimension-drop question. The later Kumar--Duddala companion arXiv:2608.21125, submitted 21 August 2026, treats front propagation/Bramson correction and continuous-type limit theory, not this harmonic-measure clause. A bounded current search found no later primary paper explicitly resolving H0008. This is bounded negative evidence, not a novelty certificate.

Before research I also reread/targeted-search recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the new-methods owner directive, the canonical H0008 claim, the newest R14 H0008 reports, the verified H intake, and neighboring same-source ownership for H0003/H0005/H0006/H0011. No release, reassignment, POSTED exclusion, or competing H0008 owner was found.

## 1. Source branching law used in this run

Under the source front-decoupling reduction, the nonroot failed genealogy is a finite-type Galton--Watson process on a finite type set `D`. Write

\[
q_j=q(j)>0,\qquad \sum_{j\in D}q_j=1,
\]

and let `nu` be the size-biased forward offspring count, common to all fine types, with

\[
m_*:=\mathbb E\nu=\frac{g''(1)}{g'(1)}>0.
\]

For a failed parent of fine type `i`, each of its `nu` potential children independently receives fine type `j` with probability `q_j`, and conditional on `(i,j)` that edge transmits failure with probability `p_{ij}`. Thus, conditional on `nu`, the failed-child vector is obtained by independent multinomial thinning, and the source mean matrix is

\[
M_{ij}=m_*q_jp_{ij}.
\tag{1.1}
\]

This is exactly the structure in source Theorem 3.1 and Appendix D. It is stronger information than the mean matrix alone and is what makes the reduction below possible.

The prior R14 harmonic report derived the exact electrical recursion. If `B_u` is the descendant escape probability through child `u`, then

\[
\mathrm{HARM}_T(u)=\frac{B_u}{\sum_v B_v}.
\tag{1.2}
\]

For a general finite-type law, the distributions of the `B_u` depend on fine type, which is why a one-type LPP theorem cannot normally be quoted directly.

## 2. Method #2 — attack the negation: heterogeneous transmission does not force a genuinely multitype harmonic problem

A tempting working belief after the previous conductance reduction was:

> if the matrix `(p_ij)` is nonconstant, then the harmonic problem necessarily retains the full fine type.

That belief is false.

Define the `q`-weighted row-average transmission

\[
\bar p_i:=\sum_{j\in D}q_jp_{ij}.
\tag{2.1}
\]

If all row averages are the same number `c`, then, conditional on `nu`, the **total** number of failed children of any parent is

\[
K\mid\nu\sim\operatorname{Bin}(\nu,c),
\tag{2.2}
\]

independently of the parent's fine type. In fact the entire type-erased genealogy is then an ordinary one-type Galton--Watson tree. Thus a highly nonconstant positive matrix `(p_ij)` can still have a completely one-type unlabelled failed cluster.

An exact two-type source-compatible witness is

\[
q=(1/2,1/2),\qquad \nu\equiv2,
\qquad
P=(p_{ij})=
\begin{pmatrix}
1&1/2\\
3/4&3/4
\end{pmatrix}.
\tag{2.3}
\]

Both row averages are `3/4`, although `P` is nonconstant. Hence the type-erased tree has

\[
K\sim\operatorname{Bin}(2,3/4),
\quad
\mathbb P(K=0,1,2)=\left(\frac1{16},\frac38,\frac9{16}\right),
\quad
\mathbb EK=\frac32.
\tag{2.4}
\]

Here `m_*=2` and `q_j=1/2`, so the source mean matrix is exactly

\[
M=
\begin{pmatrix}
1&1/2\\
3/4&3/4
\end{pmatrix},
\]

whose eigenvalues are `3/2` and `1/4`. Therefore `rho(M)=3/2`, while the unlabelled tree is the nondegenerate one-type Galton--Watson tree (2.4). Lyons--Pemantle--Peres then gives, on survival,

\[
\dim_H(\mathrm{HARM})<\log(3/2)=\log\rho(M).
\tag{2.5}
\]

So a genuinely heterogeneous transmission matrix can already exhibit the predicted strict source dimension drop without any new multitype harmonic theorem.

The finite arithmetic in (2.3)--(2.4) is checked exactly in

`artifacts/R14/2026-09-19T05-52-24Z_h0008_lumpability_example_checker.py`

with archived output

`artifacts/R14/2026-09-19T05-52-24Z_h0008_lumpability_example_checker.out`

ending `ALL_EXACT_CHECKS_PASS`.

## 3. Method #4 — prove the weaker source slice completely

The preceding example is the one-block case of an exact quotient theorem.

### Theorem R14-H0008-05A (exact type lumpability for the source failed genealogy)

Let

\[
\mathcal P=\{C_1,\dots,C_r\}
\]

be a partition of the fine type set `D`. For a parent of fine type `i`, define the aggregate failed-child probabilities

\[
c_{iB}:=\sum_{j\in C_B}q_jp_{ij},
\qquad B=1,\dots,r.
\tag{3.1}
\]

Then the fine-type source branching process, after replacing every fine type by its block in `P`, is exactly an `r`-type Galton--Watson process whose offspring law depends only on the parent block **if and only if**

\[
\boxed{
 i,i'\in C_A
 \quad\Longrightarrow\quad
 c_{iB}=c_{i'B}
 \text{ for every }B.
}
\tag{3.2}
\]

#### Proof: sufficiency

Fix a parent fine type `i`. Conditional on `nu`, each potential child independently lands in failed block `B` with probability `c_{iB}` and is absent from the failed genealogy with probability

\[
1-\sum_B c_{iB}.
\]

Therefore the vector of failed-child block counts conditional on `nu` is multinomial with category probabilities

\[
(c_{i1},\dots,c_{ir},1-\sum_Bc_{iB}).
\tag{3.3}
\]

If (3.2) holds, this conditional law depends on `i` only through its parent block `C_A`. Averaging over the common source law of `nu` therefore gives a block-offspring law depending only on `A`.

It remains to verify the branching property rather than merely the one-generation marginals. Conditional on all fine child types and the source offspring primitives, descendant subtrees from distinct children are independent. For any child whose fine type lies in block `C_B`, condition (3.2) says its block-offspring law is the same as that of every other fine type in `C_B`. Integrating out the fine type thus leaves independent descendant block-subtrees, each with a law determined only by `B`. Induction over generations proves that the block-labelled genealogy is exactly an `r`-type Galton--Watson process. `square`

#### Proof: necessity

Conversely, suppose the block-labelled process is an `r`-type Galton--Watson process whose offspring law depends only on parent block. If `i,i'` lie in the same parent block `C_A`, the expected number of failed children in block `C_B` must agree. But by the source construction,

\[
\mathbb E_i N_B=m_*c_{iB},
\qquad
\mathbb E_{i'} N_B=m_*c_{i'B}.
\]

Since `m_*>0`, equality of these expectations gives `c_{iB}=c_{i'B}` for every `B`, which is (3.2). `square`

The theorem is an elementary branching analogue of strong lumpability. I do **not** claim the abstract lumpability mechanism as novel; the bounded prior-art search did not locate this exact source-specialized formulation, so novelty is **UNVERIFIED**.

### Corollary R14-H0008-05B (one-block reduction and harmonic dimension drop)

Take the single-block partition `P={D}`. Then the type-erased failed genealogy is an ordinary one-type Galton--Watson process **if and only if**

\[
\boxed{
\bar p_i=\sum_jq_jp_{ij}=c
\quad\text{for every }i.
}
\tag{3.4}
\]

In that case its offspring law is exactly

\[
K\mid\nu\sim\operatorname{Bin}(\nu,c),
\tag{3.5}
\]

with generating function

\[
F_K(s)=\mathbb E(1-c+cs)^\nu,
\qquad
\mathbb EK=m_*c.
\tag{3.6}
\]

Moreover the source mean matrix has constant row sum:

\[
M\mathbf1=m_*c\,\mathbf1.
\tag{3.7}
\]

For irreducible positive `M`, Perron--Frobenius therefore gives

\[
\rho(M)=m_*c.
\tag{3.8}
\]

If `m_*c>1`, then on survival the full failed-boundary dimension is

\[
\dim_H\partial S=\log(m_*c)=\log\rho(M).
\tag{3.9}
\]

If the offspring law `K` is nondegenerate, the classical Lyons--Pemantle--Peres harmonic-measure theorem applies to this type-erased Galton--Watson tree and gives the strict source-predicted drop

\[
\boxed{
\dim_H(\mathrm{HARM})<\log\rho(M).
}
\tag{3.10}
\]

If `K` is deterministic, the tree is regular after the root and harmonic measure is uniform, so equality holds instead.

#### Proof of the iid type-erased branching law

Equation (3.5) gives the correct one-vertex law. For different vertices, source reproduction primitives are independent conditional on their fine types. Under (3.4), the conditional law of `K` is the same for every fine type. Hence, after integrating out all fine types, the reproduction counts at distinct vertices remain independent copies of the single law (3.5). This is precisely an ordinary Galton--Watson genealogy. The special root law of `UGW(g)` can alter only finitely many initial edges and does not affect end-boundary dimensions. Equations (3.7)--(3.8) are immediate. The strict inequality (3.10) is then exactly the one-type LPP theorem for a nondegenerate supercritical Galton--Watson tree. `square`

Under the source constraints `0<p_{ij}\le1` and `q_j>0`, the equality class is transparent. If `0<c<1` and the process is supercritical, thinning itself makes `K` nondegenerate because

\[
\mathbb E[\operatorname{Var}(K\mid\nu)]
=c(1-c)m_*>0.
\]

If `c=1`, then (3.4) and `p_{ij}\le1` force `p_{ij}=1` for every `i,j`, and `K=\nu`; equality of harmonic and boundary dimensions can therefore occur on this slice only when the forward offspring count `nu` itself is deterministic. In other words, within the constant-row-average source slice, the only no-drop case is the fluctuation-free deterministic regular tree.

This settles the harmonic-measure clause completely on a nontrivial source family containing heterogeneous transmission matrices, but it remains **PARTIAL** for H0008.

## 4. Method #20 — find why the reduction fails outside the slice

The exact obstruction is no longer vaguely “multitype conductance.” It is the failure of the aggregate offspring profiles (3.1) to lump.

For the full one-block erasure, the obstruction is simply variation of

\[
\bar p_i=\sum_jq_jp_{ij}.
\tag{4.1}
\]

If two fine types `i,i'` have different row averages, then already the conditional first moment of the untyped failed-child count differs:

\[
\mathbb E[K\mid i]=m_*\bar p_i
\neq
m_*\bar p_{i'}=\mathbb E[K\mid i'].
\tag{4.2}
\]

Therefore the untyped genealogy is not an ordinary Galton--Watson process; the hidden parent type remains statistically visible in its offspring distribution. More generally, a proposed quotient partition fails exactly when some two fine types inside one parent block have different aggregate vectors `(c_{iB})_B`.

This isolates what the one-type LPP algorithm has that the general H0008 process lacks: after every exit along the harmonic ray, the descendant tree law in LPP is sampled from one common Galton--Watson law. Here, when the aggregate vectors vary, the next descendant law depends on the inherited hidden type; additionally the harmonic child is selected by the random conductance ratio

\[
\frac{B_u}{\sum_vB_v}.
\]

The missing general theorem must therefore control a conductance-biased **finite-type environment seen from the harmonic ray**, or prove a dimension-drop inequality without explicitly constructing that invariant environment.

The quotient theorem also gives a useful preprocessing step: before attacking the full state space, collapse the maximal partition satisfying (3.2). Only the irreducible residual quotient needs genuinely multitype harmonic analysis. This avoids carrying fine types that provably do not affect the unlabelled genealogy.

## 5. Prior art and novelty boundary

The one-type harmonic statement is classical, not new. Lyons--Pemantle--Peres, *Ergodic theory on Galton--Watson trees: speed of random walk and dimension of harmonic measure* (ETDS 15, 1995), proves that on a nondegenerate supercritical Galton--Watson tree the simple-random-walk harmonic measure has almost surely strictly smaller Hausdorff dimension than the whole boundary. Lyons--Peres, *Probability on Trees and Networks*, Theorem 17.27 and its `p_0>0` extension record the corresponding statement in the modern formulation.

Rousselin's 2018 work gives explicit invariant-measure/flow-rule machinery for one-type marked Galton--Watson trees and reinforces that an environment seen from the harmonic ray is the correct technology. Existing multitype random-walk work such as Altok and Dembo--Sun supplies reversibility/biased-walk machinery, but the bounded search did not recover a theorem that directly computes the H0008 harmonic dimension for the general source offspring law.

The partition criterion (3.2) is elementary and should be treated as a source-specialized reduction / folklore-level mechanism unless a dedicated prior-art search establishes otherwise. The source-specific payoff is not a claim to have invented lumpability; it is the exact identification of a broad H0008 family for which the open harmonic clause collapses to the classical one-type theorem, plus the precise obstruction when it does not.

## 6. Fixed metric, status, and remaining obligation

The frozen metric remains

\[
\boxed{
I_{\rm mf}: a_{\rm hi}-a_{\rm lo}\longrightarrow a_{\rm hi}-a_{\rm lo}.
}
\]

So this is **NO FIXED-METRIC MOVEMENT**, first unchanged H0008 run after the preceding certification movement. The authoritative shared stagnation count remains UNKNOWN; the own-report count since last movement is `1`.

Source status remains **PARTIAL / OPEN**:

- multifractal clause: complete under the source finite-type branching reduction and the hypotheses in the preceding reports;
- harmonic clause: now complete on the constant-row-average one-block slice (and, structurally, reducible on every exactly lumpable partition), but open for the genuinely multitype residual quotient.

The clean remaining target is:

\[
\boxed{
\text{For a supercritical irreducible finite-type source law failing all nontrivial lumpability reductions,}
\quad
\dim_H(\mathrm{HARM})<\log\rho(M)
\text{ outside the deterministic equality class.}
}
\tag{6.1}
\]

A proof would need an ergodic/invariant law for the conductance-biased harmonic-ray environment, or a replacement entropy argument that controls it without a closed-form invariant density. A new finite-pressure calculation alone cannot suffice: the preceding R14 pressure-insufficiency example already showed that the entire pressure curve does not determine harmonic dimension.

## 7. Next genuinely different methods

Do not repeat #2/#4/#20 next run. The next fresh triple is:

- **#3 PROVE SOMETHING STRONGER:** seek a quantitative theorem stable under small violations of lumpability, e.g. `bar p_i=c+epsilon r_i`, rather than only an exact-equality slice;
- **#14 FIND THE GROUP ACTING:** compute the maximal quotient of fine types with identical aggregate offspring profiles and formulate the harmonic problem on that minimal quotient;
- **#28 REPLACE FOR ALL WITH FOR TYPICAL:** derive the stationary law or entropy rate first for the type/conductance environment along a typical harmonic ray, then ask whether that is sufficient for almost-sure exact dimensionality.

If those routes fail to move the source frontier for three consecutive post-movement runs, invoke the Section-I stuck protocol rather than adding more local lemmas.

## 8. Exact artifact and model-control note

Exact finite checker:

- `artifacts/R14/2026-09-19T05-52-24Z_h0008_lumpability_example_checker.py`
- `artifacts/R14/2026-09-19T05-52-24Z_h0008_lumpability_example_checker.out`
- archived output: `ALL_EXACT_CHECKS_PASS`.

The model-control limitation is unchanged. The exposed task-control surface provides prompt/title/schedule/timing/enabled/notification controls but no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run model telemetry. GPT-6/maximum is therefore prompt-only in this context. The historical P26 `You cannot modify this task` event was authorization-context dependent and a later authorized context succeeded; the legitimate remedy for any such denied task remains the owning/admin-authorized context or platform support, not a permission bypass or duplicate task. No scheduler or permission setting was changed in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  source_id: H0008
  source: "Achyut Kumar, arXiv:2608.15987v1, Section 12.3 Open problem (6), Boundary fluctuations"
  ownership: "exclusive R14 claim preserved"
  source_status: PARTIAL_OPEN
  metric:
    name: I_mf
    before: "a_hi-a_lo (exact full certified value)"
    after: "a_hi-a_lo (same)"
    movement: false
  harmonic_clause:
    progress: "strict dimension drop proved on the source constant-q-row-average slice via exact type erasure to one-type GW; general residual multitype case remains open"
    new_reduction: "partition P is an exact branching quotient iff c_iB=sum_{j in C_B} q_j p_ij is constant over fine parent types i inside each parent block"
    equality_class_on_one_block_slice: "only deterministic regular forward tree; otherwise LPP gives strict drop"
  methods_used: [2, 4, 20]
  next_methods: [3, 14, 28]
  stagnation:
    authoritative_shared_count: UNKNOWN
    own_since_last_metric_movement: 1
  exact_artifact:
    checker: "artifacts/R14/2026-09-19T05-52-24Z_h0008_lumpability_example_checker.py"
    output: "artifacts/R14/2026-09-19T05-52-24Z_h0008_lumpability_example_checker.out"
    result: ALL_EXACT_CHECKS_PASS
  exclusions_preserved:
    - original negative-margin perceptron terminal handoff
    - H0017 terminal handoff
    - D0036 terminal handoff
    - D0039 terminal handoff
    - D0034 terminal handoff
  shared_roots_modified: false
  scheduler_changed: false
```
