Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — one-defect functions decisively obstruct the derivative-degree / marginal-entropy scheduling route

## Status and mathematical delta

**Parent problem:** Friedgut--Kalai Fourier entropy--influence (FEI), asking for one universal finite constant \(C\) such that
\[
H(\widehat f^2)\le C I(f)
\]
for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved. The source metric “finite universal upper bound for \(C_{\rm FEI}\)” remains **UNKNOWN -> UNKNOWN**. The inherited native finite-dimensional atlas remains **6 -> 6**.

**Mechanism-level movement:** the preceding P03 run isolated the sufficient weighted derivative-degree tree charge
\[
D_{\mathcal T}^{\deg}
 =\sum_{v\text{ internal}}w_v r_v j_{i(v)}(f_v)
\]
and asked whether every Boolean function admits a full physical restriction tree with \(D_{\mathcal T}^{\deg}=O(I(f))\). This run gives a decisive negative answer. For the one-defect / OR-type family \(f_n(0)=-1\), \(f_n(x)=+1\) otherwise,
\[
\boxed{\frac{1}{I(f_n)}\inf_{\mathcal T\text{ full}}D_{\mathcal T}^{\deg}(f_n)=\frac{n-1}{2}\to\infty.}
\]
In fact every full adaptive tree has exactly this charge.

More strongly, the failure is not specifically algebraic degree: every tree also has a diverging **marginal spectral-bit entropy envelope**
\[
M_{\mathcal T}:=\sum_v w_v h_2(j_{i(v)}(f_v)),
\qquad
\frac{M_{\mathcal T}(f_n)}{I(f_n)}=\frac{n-1}{2}+O(1),
\]
while the true hereditary allocation is bounded and in fact
\[
\boxed{\frac{R_{\mathcal T}(f_n)}{I(f_n)}\longrightarrow 2,\qquad R_{\mathcal T}(f_n)<4I(f_n)}
\]
for every full tree. Thus the loose step is the replacement
\[
B_i=H(Z_i\mid Z_{-i})\le H(Z_i)=h_2(j_i),
\]
not dependent-branch recombination. On this family the Reed--Muller support gap used in the previous run is attained with equality, so the previous local payment \(\phi(r)j\) is exactly the bad marginal envelope.

This is a **decisive obstruction to the proposed universal scheduling route**, not a counterexample to FEI. OR/AND functions are a classical FEI-positive family.

## 1. Dependencies actually consumed

The progress-first directive was followed. I read only the dependencies needed to attack the live obstruction.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: T01 asks for hereditary allocation or paid dependent recombination without fresh-variable dependence and prioritizes new mathematics over routine audits.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the fresh-control theorem \(L(\Gamma_cf)\le12\Delta_{\rm aff}(\Gamma_cf)\) is explicitly restricted and not full FEI.
- `proofnet24/P03-fei/README.md`, current blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI is open; shifted thresholds refute Han's stronger absolute-overlap selector; the current README also records newer restricted quadratic-twist results without promoting them to universal FEI. The false resolvent, pointwise-erasure and fixed-coefficient drift shortcuts remain retired.
- P03 preceding substantive run `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__fei-reed-muller-hereditary-allocation.md`, blob `fbcc39447666a43d398403ad2e89b7e50c6adf1b`: proves the derivative-profile bound, hereditary degree-\(d\) allocation, and Corollary 9.1 reducing full FEI to a hypothetical universal \(D_{\mathcal T}^{\deg}/I\) bound. The present run attacks that exact hypothetical bound.
- P03 earlier `2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`: arbitrary dependent-branch recombination is already paid by at most \(2/\ln2\) times charged influence. This remains intact.
- `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T22-18-30Z__report.md`, blob `22362306d41f9b6d3d0f221ddda3d303b8a47968`: reconstructed the fresh-control latent-mixture theorem and its exact restriction \(2^{-c}M_0(f)\le1\). Nothing below uses fresh controls.
- Companion NM13-02 newest report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T04-18-00+0300__dependent-branch-allocation-splicing.md`, blob `ab5435f679d3df57163fd1301fde323ad2cc4d29`: proves the exact partial-tree budget, max-splicing of branch-dependent certificates, and hereditary \(12.04\) allocation on symmetric functions. It also shows P03's shifted-threshold family has cheap true allocation despite high algebraic degree. The present run takes the complementary question left open there: whether P03's finer *weighted* derivative-degree charge itself can still be universal. It cannot.
- `POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem is reused or duplicated.

### Public-source scope checked now

González--MacManus--Pereyra, arXiv:2606.00246, still states full FEI as a conjecture and develops an inductive/stopping-tree sufficient framework plus restricted classes. Its introduction explicitly lists AND/OR as canonical examples already satisfying FEI. Friedgut--Kalai, Proc. AMS 124 (1996), 2993--3002, remains the historical source attribution used by the modern FEI literature. No claim here depends on a priority assertion.

## 2. Why this family is the right stress test

The preceding P03 run proposed paying a queried coordinate \(i\) at a restricted node \(g=(-1)^P\) by
\[
r_i(g)\,j_i(g),
\qquad
r_i(g)=\deg D_iP,
\qquad
j_i(g)=\min\{\operatorname{Inf}_i(g),1-\operatorname{Inf}_i(g)\}.
\]
The hope was that an adaptive tree could arrange for large derivative degree only where folded influence is tiny enough in aggregate.

The one-defect family is the smallest place where this hope can be tested exactly. It has three features simultaneously:

1. every coordinate has the smallest possible nonzero influence allowed by its derivative degree;
2. every adaptive tree has only one nonconstant child after every split, so there is no scheduling freedom hidden in branch dependence;
3. the actual spectral conditional entropy \(B_i=H(Z_i\mid Z_{-i})\) is only a constant multiple of the influence, so true hereditary allocation is cheap.

Thus any divergence comes from the proposed surrogate rather than from FEI itself.

## 3. One-defect family and exact restriction structure

Work on \(\mathbb F_2^n\). Define
\[
f_n(x)=\begin{cases}-1,&x=0,\\+1,&x\ne0.\end{cases}
\tag{3.1}
\]
Equivalently,
\[
f_n=(-1)^{P_n},
\qquad
P_n(x)=\prod_{j=1}^n(1+x_j)
\tag{3.2}
\]
over \(\mathbb F_2\).

For every coordinate \(i\),
\[
D_iP_n(x)=\prod_{j\ne i}(1+x_j).
\tag{3.3}
\]
For \(n\ge2\), this derivative is nonconstant of exact degree
\[
r_i=n-1.
\tag{3.4}
\]
It is one precisely when all other \(n-1\) coordinates vanish, so
\[
\operatorname{Inf}_i(f_n)=2^{1-n}=:p_n.
\tag{3.5}
\]
For \(n\ge2\), \(p_n\le1/2\), hence
\[
j_i(f_n)=p_n=2^{-(n-1)}=2^{-r_i}.
\tag{3.6}
\]
Thus the Reed--Muller minimum-distance inequality used in the preceding P03 run is **exactly saturated** at every live node.

If the queried coordinate is fixed to \(1\), the product in (3.2) vanishes and the restriction is constant \(+1\). If it is fixed to \(0\), the restriction is exactly \(f_{n-1}\) on the remaining coordinates. Therefore every full adaptive physical restriction tree has a unique nonconstant path
\[
f_n\to f_{n-1}\to\cdots\to f_1\to\text{constant},
\tag{3.7}
\]
and the node carrying \(f_m\) has cylinder weight
\[
w_m=2^{-(n-m)}.
\tag{3.8}
\]
There is no coordinate-order advantage: permutation symmetry makes every choice identical, and every nonconstant branch has the same future state.

The total influence is
\[
I(f_n)=np_n=n2^{1-n}.
\tag{3.9}
\]

## 4. Theorem A — the weighted derivative-degree reduction is false

**Theorem A.** For every \(n\ge1\) and every full adaptive physical restriction tree \(\mathcal T\) of \(f_n\),
\[
\boxed{
D_{\mathcal T}^{\deg}(f_n)
=\frac{n-1}{2}\,I(f_n).
}
\tag{4.1}
\]
Consequently
\[
\boxed{
\inf_{\mathcal T\text{ full}}
\frac{D_{\mathcal T}^{\deg}(f_n)}{I(f_n)}
=\frac{n-1}{2}\to\infty.
}
\tag{4.2}
\]
In particular, the universal hypothesis (9.4) of P03's preceding Corollary 9.1 is false.

### Proof

At the unique node with current restriction \(f_m\), \(m\ge2\), equations (3.4)--(3.6) give
\[
r_v=m-1,
\qquad
j_{i(v)}(f_v)=p_m=2^{1-m}.
\]
Using (3.8),
\[
w_mp_m=2^{-(n-m)}2^{1-m}=2^{1-n}=p_n.
\tag{4.3}
\]
The final \(f_1\) derivative is constant, hence contributes zero by the definition of \(D^{\deg}\). Therefore
\[
D_{\mathcal T}^{\deg}(f_n)
=\sum_{m=2}^n(m-1)w_mp_m
=p_n\sum_{s=1}^{n-1}s
=p_n\frac{n(n-1)}2.
\]
Using \(I(f_n)=np_n\) gives (4.1). QED.

This is stronger than finding one bad coordinate order: **all** adaptive trees have the same divergent ratio.

## 5. Theorem B — the real obstruction is marginalization \(B_i\le H(Z_i)\)

The preceding P03 hereditary derivative-degree proof begins locally with
\[
B_i(g)=H(Z_i\mid Z_{-i})\le H(Z_i)=h_2(j_i(g)).
\tag{5.1}
\]
Define the corresponding tree marginal envelope
\[
M_{\mathcal T}(f):=
\sum_{v\text{ internal}}w_v h_2(j_{i(v)}(f_v)).
\tag{5.2}
\]

**Theorem B.** Every full adaptive tree of \(f_n\) satisfies
\[
\boxed{
\frac{n-1}{2}
\le
\frac{M_{\mathcal T}(f_n)}{I(f_n)}
\le
\frac{n-1}{2}+\frac{1}{\ln2}.
}
\tag{5.3}
\]
Hence \(M_{\mathcal T}/I\) diverges linearly for every tree.

Moreover, because \(j_i(f_m)=2^{-(m-1)}\) exactly saturates the Reed--Muller gap,
\[
\phi(m-1)j_i(f_m)=h_2(j_i(f_m)).
\tag{5.4}
\]
Thus the preceding P03 derivative-profile payment is **exactly** the marginal envelope on this family, not merely comparable to it.

### Proof

Again \(w_mp_m=p_n\). Therefore
\[
\frac{M_{\mathcal T}(f_n)}{I(f_n)}
=\frac1n\sum_{m=2}^n\frac{h_2(p_m)}{p_m}.
\tag{5.5}
\]
Since \(p_m=2^{1-m}\),
\[
\frac{h_2(p_m)}{p_m}
=(m-1)+\frac{1-p_m}{p_m}\log_2\frac1{1-p_m}.
\tag{5.6}
\]
The second term is nonnegative. Also
\[
-\ln(1-p)\le\frac{p}{1-p}
\]
gives
\[
0\le\frac{1-p}{p}\log_2\frac1{1-p}\le\frac1{\ln2}.
\tag{5.7}
\]
Insert (5.6)--(5.7) into (5.5) and use
\[
\frac1n\sum_{m=2}^n(m-1)=\frac{n-1}{2}.
\]
This proves (5.3). Equation (5.4) is the definition
\[
\phi(r)=2^rh_2(2^{-r})
\]
with \(r=m-1\) and \(j=2^{-r}\). QED.

**Interpretation.** No improvement that merely schedules the scalar upper bound \(B_i\le h_2(j_i)\), or the equivalent minimum-distance envelope \(\phi(r_i)j_i\), can prove universal FEI. The missing information is the dependence between the spectral bit \(Z_i\) and the rest of the spectrum.

## 6. Exact spectral conditional entropy and cheap true hereditary allocation

The squared Fourier law of \(f_m\) is explicit. Put
\[
p=p_m=2^{1-m}.
\]
The Fourier coefficients are
\[
\widehat f_m(\varnothing)=1-p,
\qquad
\widehat f_m(S)=-p\quad(S\ne\varnothing).
\tag{6.1}
\]
Hence the squared spectral law has mass
\[
(1-p)^2
\]
at the empty set and mass
\[
p^2
\]
at every nonempty subset.

Fix a coordinate \(i\). To compute
\[
B_m:=B_i(f_m)=H(Z_i\mid Z_{-i}),
\]
pair the spectral atoms \(T\) and \(T\cup\{i\}\) for \(T\subseteq[m]\setminus\{i\}\).

If \(T\ne\varnothing\), both atoms have mass \(p^2\), so that fiber contributes \(2p^2\) bits. There are \(2^{m-1}-1=p^{-1}-1\) such fibers, for total
\[
2p(1-p).
\tag{6.2}
\]
For the exceptional fiber \(T=\varnothing\), the two masses are \((1-p)^2\) and \(p^2\). Therefore
\[
\boxed{
B_m
=2p(1-p)
+\big((1-p)^2+p^2\big)
 h_2\!\left(\frac{p^2}{(1-p)^2+p^2}\right).
}
\tag{6.3}
\]

### Lemma 6.1. For every \(m\ge2\), \(B_m\le4p_m\), and \(B_m/p_m\to2\).

Let
\[
E_m:=\big((1-p)^2+p^2\big)
 h_2\!\left(\frac{p^2}{(1-p)^2+p^2}\right).
\]
For fixed \(b=p^2\), the function
\[
F(a)=(a+b)h_2\left(\frac b{a+b}\right)
\]
is increasing in \(a\ge0\), because
\[
F'(a)=\log_2\frac{a+b}{a}\ge0.
\]
Since \((1-p)^2\le1-p^2\),
\[
E_m\le h_2(p^2).
\tag{6.4}
\]
The elementary inequality
\[
-(1-x)\log_2(1-x)\le\frac{x}{\ln2}
\]
gives
\[
h_2(p^2)
\le p^2\left(2\log_2\frac1p+\frac1{\ln2}\right)
=p^2\left(2(m-1)+\frac1{\ln2}\right).
\tag{6.5}
\]
Since \(1/\ln2<2\) and \(m2^{1-m}\le1\) for \(m\ge2\),
\[
E_m\le2mp^2\le2p.
\tag{6.6}
\]
Combining (6.2) and (6.6) yields \(B_m\le4p\).

Also (6.5) gives
\[
\frac{E_m}{p}\le p\left(2(m-1)+\frac1{\ln2}\right)\to0,
\]
while \(2p(1-p)/p\to2\). Hence \(B_m/p_m\to2\). QED.

Now every full adaptive tree has
\[
R_{\mathcal T}(f_n)
=\sum_{m=2}^n w_mB_m.
\]
Because \(w_mp_m=p_n\),
\[
\boxed{
\frac{R_{\mathcal T}(f_n)}{I(f_n)}
=\frac1n\sum_{m=2}^n\frac{B_m}{p_m}.
}
\tag{6.7}
\]
Lemma 6.1 immediately gives
\[
\boxed{R_{\mathcal T}(f_n)<4I(f_n)}
\tag{6.8}
\]
and Cesàro convergence gives
\[
\boxed{
\frac{R_{\mathcal T}(f_n)}{I(f_n)}\longrightarrow2.
}
\tag{6.9}
\]
Since every full tree has the same value, this is also the exact asymptotic of P03's optimized hereditary functional
\[
\mathcal A(f_n)=\frac1{I(f_n)}\inf_{\mathcal T\text{ full}}R_{\mathcal T}(f_n).
\]

The family therefore separates the two quantities by a factor of order \(n\):
\[
\frac{D_{\mathcal T}^{\deg}}{I}\sim\frac n2,
\qquad
\frac{M_{\mathcal T}}I\sim\frac n2,
\qquad
\frac{R_{\mathcal T}}I\to2.
\tag{6.10}
\]

## 7. This is not an FEI counterexample: the actual FEI ratio tends to four

For completeness, (6.1) gives an exact entropy formula. With \(p=p_n\),
\[
H(f_n)
=-(1-p)^2\log_2(1-p)^2
+(2^n-1)p^2\,2(n-1).
\tag{7.1}
\]
Since
\[
(2^n-1)p^2=2p-p^2,
\]
the second term divided by \(I(f_n)=np\) tends to \(4\). For the first term, \(-a\ln a\le1-a\) with \(a=(1-p)^2\) gives
\[
0\le
\frac{-(1-p)^2\log_2(1-p)^2}{np}
\le\frac{2}{n\ln2},
\]
so
\[
\boxed{\frac{H(f_n)}{I(f_n)}\longrightarrow4.}
\tag{7.2}
\]
Thus this canonical family is perfectly compatible with FEI, as already known in the literature.

Using P03's exact full-tree telescope \(H=R+S\), equations (6.9) and (7.2) also imply
\[
\frac{S_{\mathcal T}(f_n)}{I(f_n)}\to2.
\tag{7.3}
\]
So the previous universal payment of dependent-branch recombination is not what fails here. The divergence is entirely introduced by replacing conditional spectral entropy with marginal spectral entropy.

## 8. Consequences for the live FEI program

### 8.1 The preceding conditional reduction is retired

P03 Corollary 9.1 from the previous run was explicitly conditional on a universal constant \(K\) with
\[
D_{\mathcal T}^{\deg}\le KI(f)
\]
for some full adaptive tree of every Boolean function. Theorem A proves that such a \(K\) does not exist. That **route is refuted**.

The preceding Reed--Muller derivative-profile theorem itself remains correct and useful on bounded-degree classes. What fails is trying to make its scalar local envelope universal by adaptive scheduling.

### 8.2 A stronger negative lesson: influence rarity alone is insufficient

On \(f_m\), the local data
\[
(r_i,j_i)=(m-1,2^{1-m})
\]
already saturate the minimum-distance constraint. The scalar marginal entropy \(h_2(j_i)\) is of order \(m j_i\), but the true conditional spectral entropy \(B_i\) is only about \(2j_i\). Therefore the missing universal mechanism must exploit **spectral fiber dependence**: how knowing \(Z_{-i}\) predicts \(Z_i\). Any proof that forgets \(Z_{-i}\) before paying the node necessarily loses the decisive factor on this family.

This sharply narrows the hereditary-allocation problem. A promising next target is not another degree penalty, but a structure-sensitive estimate for
\[
B_i=H(Z_i\mid Z_{-i})
\]
that can be preserved and spliced under physical restriction. NM13-02's max-splicing theorem is directly compatible with such branch-specific certificates.

### 8.3 Restricted results remain restricted

- The fresh-control theorem \(L(\Gamma_cf)\le12\Delta_{\rm aff}(\Gamma_cf)\) still adds fresh variables and does not solve fixed-domain hereditary allocation.
- NM13-02's symmetric hereditary \(12.04\) certificate already covers this OR family abstractly. The new contribution here is different: an exact calculation proving that P03's proposed weighted degree charge diverges although the true hereditary cost remains bounded.
- The newer quadratic-twist/symmetric-core continuation in the P03 README remains a restricted class theorem, not full FEI.

## 9. Sanity checker executed and preserved

Executed checker:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T04-29-36+0300__check_one_defect_degree_charge.py`

Archived actual output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T04-29-36+0300__one_defect_degree_charge_check.json`

The checker brute-forces complete Walsh spectra through dimension \(8\), independently verifies the exact spectral law and influences, computes \(B_i\) from conditional spectral fibers, and compares with formula (6.3). It also evaluates the exact \(D^{\deg}/I=(n-1)/2\) identity and the hereditary ratio through \(n=1024\).

Actual status: `PASS`.

- maximum influence-formula error: `0.0`;
- maximum \(B_i\)-formula discrepancy: `3.469446951953614e-18`;
- no violation of \(B_i\le4p_i\);
- \(D^{\deg}/I=511.5\) at \(n=1024\), while \(R/I=2.0004605556719373\).

These are sanity checks only. The all-dimensional claims are proved analytically above.

## 10. Failed-route preservation

Nothing here revives any retired claim. In particular, still excluded are:

- the all-constant affine-drift payment, refuted by majority for every finite coefficient;
- the false pointwise erasure shortcut;
- retired resolvent/interpolation inequalities;
- coefficient-specific drift claims;
- Han's all-coordinate absolute-overlap selector, refuted by shifted thresholds;
- independence substitutions between dependent physical branches.

Newly retired after this run:

- **universal weighted derivative-degree scheduling** \(D_{\mathcal T}^{\deg}=O(I)\);
- more generally, any universal proof that pays every node only by the marginal envelope \(h_2(j_i)\) and then sums it along a full physical tree.

## 11. Next nonredundant attack

The live full-scope obstruction returns to the true hereditary quantity
\[
\mathcal A(f)=\frac1{I(f)}\inf_{\mathcal T\text{ full}}R_{\mathcal T}(f),
\qquad
R_{\mathcal T}=\sum_vw_vH((Z_v)_{i(v)}\mid(Z_v)_{-i(v)}).
\]
The present family shows that scalar influence/degree summaries are too coarse. The next materially different method should preserve conditional spectral fibers. Two concrete routes are now better motivated:

1. **fiber-collision / posterior route:** express \(B_i\) directly through paired spectral masses \((p_T,p_{T\cup i})\) and seek a branch-stable payment by a collision or posterior-predictability statistic that telescopes under physical restriction;
2. **certified stopping-class splicing:** use NM13-02's exact partial influence budget and max-splicing theorem to stop branches as soon as they enter a restriction-closed class with a known hereditary certificate, while proving an aggregate conditional-fiber payment only on the genuinely uncertified trunk.

A repeat of the Reed--Muller degree charge would now be an unchanged failed route.

## 12. Before/after and ledger_delta

```yaml
ledger_delta:
  worker: P03
  assignment: T01_Fourier_entropy_influence
  companion: NM13-02
  parent_problem: Friedgut_Kalai_FEI
  parent_status_before: OPEN
  parent_status_after: OPEN
  parent_metric: universal_finite_C_FEI
  parent_metric_before: UNKNOWN
  parent_metric_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  source_level_movement: false
  mechanism_before:
    - paid_dependent_recombination_available
    - hereditary_degree_d_allocation_available
    - conditional_full_FEI_reduction_to_universal_weighted_derivative_degree_charge
  mechanism_after:
    - one_defect_family_refutes_universal_weighted_derivative_degree_charge
    - every_full_tree_Ddeg_over_I_equals_(n-1)/2
    - marginal_entropy_tree_envelope_also_diverges_linearly
    - exact_true_hereditary_allocation_on_same_family_is_less_than_4I_and_tends_to_2I
    - divergence_localized_to_B_i_le_H_Zi_marginalization_step
  newly_refuted_route:
    - universal_Ddeg_tree_bound
    - universal_sum_of_h2_folded_influence_node_payment
  previous_reed_muller_theorem_status: preserved_valid_on_bounded_degree_classes
  fresh_controls: false
  branch_independence_assumed: false
  full_FEI_claimed: false
  novelty: UNVERIFIED
  checker_status: PASS
  exhaustive_checker_dimension: 8
  large_n_formula_check: 1024
  failed_routes_preserved:
    - resolvent
    - pointwise_erasure
    - affine_drift_all_constants
    - Han_absolute_overlap
  substantive_unchanged_run_count: 0
  remaining_obstruction: universal_structure_sensitive_bound_on_true_hereditary_conditional_spectral_entropy
  next_attack: conditional_spectral_fiber_payment_or_branch_certified_max_splicing
  artifacts:
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T04-29-36+0300__check_one_defect_degree_charge.py
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T04-29-36+0300__one_defect_degree_charge_check.json
```

**End of complete run report.**
