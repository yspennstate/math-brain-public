Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — a double-logarithmic hereditary stopping theorem for finite Hamming defects of quadratic phases

## Status / before-after

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant \(C\) such that
\[
H(\widehat f^{\,2})\le C I(f)
\]
for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved here. The source-level quantity “finite universal upper bound for \(C_{\rm FEI}\)” remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**.

**Mechanism-level advance.** This run proves a new all-dimensional, fresh-variable-free hereditary theorem for arbitrary finite Hamming perturbations of quadratic phases. Let
\[
f(x)=(-1)^{q(x)}\sigma_D(x),\qquad |D|\le t,
\]
where \(q\) is any polynomial of degree at most two over \(\mathbb F_2\), and \(\sigma_D=-1\) on \(D\) and \(+1\) outside. Put
\[
L=\lceil\log_2 t\rceil\quad(L=0\text{ for }t=1),\qquad
a=\max\{3,L\},\qquad d_t=L+a-1,
\]
and
\[
C_t=12.04+\log_2 d_t.
\]
Then there exists a full adaptive physical restriction tree \(\mathcal T\) such that
\[
\boxed{R_{\mathcal T}(f)\le C_t I(f)}
\tag{A}
\]
and, in particular,
\[
\boxed{H(\widehat f^{\,2})\le C_t I(f).}
\tag{B}
\]
For \(t\ge8\), \(L\ge3\), so
\[
\boxed{C_t=12.04+\log_2(2\lceil\log_2t\rceil-1)=O(\log\log t).}
\tag{C}
\]
The constant is independent of the ambient dimension, the rank/density of the quadratic phase, and the geometry of the defect set. This strictly extends the one-point-quadratic-defect hereditary class proved by companion NM13-02, although it is much less sharp at \(t=1\). It is a restricted theorem, not full FEI.

The proof deliberately avoids P03's newest consumed-curvature condition. It uses a different stopping principle: while the restricted quadratic part has a nonzero polar row and the ambient residual dimension is large compared with \(\log t\), query such a row. The query has folded influence bounded below by \(1/4\), so its hereditary allocation is paid locally by marginal spectral entropy. Once the quadratic polar part vanishes, the leaf is an affine character times a sparse sign defect; cube isoperimetry pays that leaf. If the dimension becomes only \(O(\log t)\), the published part-symmetric FEI theorem applied with singleton parts pays the leaf. Thus dense quadratic curvature is never charged.

## Dependencies actually consumed

The progress-first directive was followed; only complete dependencies needed for this route were read.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains T01 owner; roughly 90% effort is new derivation, with NM13-02 as the current entropy companion.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` requires appended controls and a density hypothesis and is explicitly not full FEI.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open; the pointwise erasure shortcut, all-fixed-coefficient drift route, resolvent/interpolation targets, and Han absolute-overlap selector remain retired.
- Newest own substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T06-31-37+0300__fei-character-defect-curvature-allocation.md`, blob `86e75e9bdecea0a4477be4432bc5d4eab6f4c9d1`: supplies the local conditional spectral-bit viewpoint and records the newest curvature stopping obstruction.
- P03 recombination report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: supplies the exact partial-tree identities and the paid dependent-branch recombination estimate
  \[
  H-H_L=R_{\mathcal T}+S_{\mathcal T},\quad
  I-I_L=Q_{\mathcal T},\quad
  0\le S_{\mathcal T}\le\frac2{\ln2}J_{\mathcal T}\le\frac2{\ln2}Q_{\mathcal T}.
  \]
- Newest companion report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T07-05-27+0300__descendant-influence-hereditary.md`, blob `dfbd0ec25828d1edff10d6b7f9bf8a10e45b66e0`: proves the descendant-influence recursion and a bounded-depth-to-quadratic-leaves theorem, and proposes an influence-lifetime/high-degree-monomial-cover route. The present proof takes complementary scope: finite Hamming perturbations of arbitrary quadratic phases, with no defect-separation tree and no high-degree monomial cover.
- `proofnet24/P03-fei/continuations/2026-09-20-quadratic-symmetry/REPORT.md`, blob `11605492453c978a7cb45261eb563d006fee2db0`: records the published O'Donnell--Wright--Zhou input in the form that every \(d\)-part-symmetric Boolean function satisfies FEI with constant \(12.04+\log_2d\). Singleton parts therefore give a dimension-\(d\) leaf certificate with that constant.
- `POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem is duplicated.

No peer file or peer claim was edited.

## Current public-source scope

A fresh source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246, which still states universal FEI as the Friedgut--Kalai conjecture and develops a coordinate-restriction/stopping-tree sufficient framework plus restricted positive classes. It does not prove a universal finite FEI constant. Friedgut--Kalai's 1996 source attribution is preserved. A bounded source search did not recover the finite-Hamming-defect theorem below; that is negative evidence only, so publication priority remains **UNVERIFIED**.

## 1. Tree notation inherited from P03

For a physical restriction tree \(\mathcal T_0\), each internal node \(v\) carries a restricted Boolean function \(f_v\), a queried physical coordinate \(i(v)\), and cylinder weight \(w_v=2^{-\operatorname{depth}(v)}\). Put
\[
B_i(g)=H(Z_i\mid Z_{-i}),\qquad
j_i(g)=\min\{\operatorname{Inf}_i(g),1-\operatorname{Inf}_i(g)\},
\]
\[
R_{\mathcal T_0}=\sum_{v\text{ internal}}w_v B_{i(v)}(f_v),\quad
J_{\mathcal T_0}=\sum_vw_vj_{i(v)}(f_v),\quad
Q_{\mathcal T_0}=\sum_vw_v\operatorname{Inf}_{i(v)}(f_v).
\]
Let \(H_L=\sum_\ell w_\ell H(f_\ell)\) and \(I_L=\sum_\ell w_\ell I(f_\ell)\). The earlier P03 report proves the exact identities quoted above. They are used only after the new local and leaf estimates below are proved.

## 2. Sparse signs have an ambient-dimension-free FEI bound once density is exponentially small

For \(A\subseteq\mathbb F_2^d\), let \(u_A=-1\) on \(A\) and \(+1\) outside. Write
\[
m=|A|,\qquad \varepsilon=m2^{-d}\le\frac12,\qquad
\Lambda=\log_2(1/\varepsilon)=d-\log_2m.
\]
The empty case \(m=0\) is constant and trivial.

### Lemma 2.1 (cube edge isoperimetry, with normalization)

If \(m\le2^{d-1}\), then the number of undirected cube edges leaving \(A\) satisfies
\[
\boxed{|\partial A|\ge m\log_2\frac{2^d}{m}=m\Lambda.}
\tag{2.1}
\]
Consequently
\[
\boxed{I(u_A)=\frac{|\partial A|}{2^{d-1}}\ge2\varepsilon\Lambda.}
\tag{2.2}
\]

#### Proof

Induct on \(d\). Split by the last coordinate into sections \(A_0,A_1\subseteq\mathbb F_2^{d-1}\), with sizes \(m_0\ge m_1\) after relabeling. Internal boundary edges contribute at least
\[
m_0\log_2\frac{2^{d-1}}{m_0}+m_1\log_2\frac{2^{d-1}}{m_1}
\]
by induction. The cross-section boundary contains at least \(m_0-m_1\) edges, since the overlap between the two sections has size at most \(m_1\). Put \(m=m_0+m_1\) and \(p=m_1/m\in[0,1/2]\). Dividing the desired comparison by \(m\), the excess of this lower bound over \(\log_2(2^d/m)\) is
\[
h_2(p)-2p.
\]
The binary entropy \(h_2\) is concave and agrees with the chord values \(0\) at \(p=0\) and \(1\) at \(p=1/2\); hence \(h_2(p)\ge2p\) on \([0,1/2]\). This proves (2.1). Equation (2.2) follows because each boundary edge contributes one disagreeing physical edge and each coordinate has \(2^{d-1}\) undirected edges in its influence denominator. QED.

### Lemma 2.2 (sparse-sign spectral entropy)

For \(0<m\le2^{d-1}\),
\[
\boxed{
\frac{H(u_A)}{I(u_A)}
\le
4+\frac{2(\log_2m+\log_2e-1)}{\Lambda}.
}
\tag{2.3}
\]

#### Proof

The constant Fourier coefficient is \(1-2\varepsilon\), so the total nonconstant squared Fourier mass is
\[
W=1-(1-2\varepsilon)^2=4\varepsilon(1-\varepsilon).
\]
Among probability distributions with one atom of mass \(1-W\) and at most \(2^d-1\) remaining atoms of total mass \(W\), entropy is maximized by spreading the remaining mass uniformly. Hence
\[
H(u_A)\le h_2(W)+W\log_2(2^d-1)
\le h_2(W)+Wd.
\]
Using
\[
h_2(W)\le W\log_2\frac eW,
\]
we obtain
\[
H(u_A)\le W\left[d+\log_2\frac eW\right].
\]
Divide by (2.2), substitute \(W=4\varepsilon(1-\varepsilon)\), \(d=\Lambda+\log_2m\), and set
\[
A_0=\log_2m+\log_2e-2.
\]
The resulting right side is
\[
\frac{2(1-\varepsilon)}{\Lambda}
\left[2\Lambda+A_0-\log_2(1-\varepsilon)\right].
\]
We claim this is at most the right side of (2.3). After multiplying the desired inequality by \(\Lambda/2\), the difference between the proposed upper bound and the displayed quantity is
\[
\varepsilon(2\Lambda+A_0)+1+(1-\varepsilon)\log_2(1-\varepsilon).
\]
Since \(\Lambda\ge1\), \(m\ge1\),
\[
2\Lambda+A_0\ge\log_2e>0.
\]
Also \(1-\varepsilon\in[1/2,1]\), so
\[
1+(1-\varepsilon)\log_2(1-\varepsilon)\ge\frac12>0.
\]
Thus the difference is positive and (2.3) follows. QED.

### Corollary 2.3 (uniform sparse leaf constant)

Suppose \(m\le t\), \(L=\lceil\log_2t\rceil\), \(a=\max\{3,L\}\), and
\[
d\ge L+a.
\]
Then \(\Lambda=d-\log_2m\ge a\), and Lemma 2.2 gives
\[
\frac{H(u_A)}{I(u_A)}
\le C_{\rm sp}(t):=
4+\frac{2(\log_2t+\log_2e-1)}a.
\tag{2.4}
\]
If \(L\le2\), then \(C_{\rm sp}<5.63\). If \(L\ge3\), then \(a=L\), \(\log_2t\le L\), and
\[
C_{\rm sp}
\le6+\frac{2(\log_2e-1)}3
=6.2951300272\ldots.
\tag{2.5}
\]
Moreover every coordinate influence of \(u_A\) is at most \(2\varepsilon\le2^{1-a}\le1/4\), so \(J(u_A)=I(u_A)\). Multiplication by an affine character translates the Fourier law and folds physical influences, hence preserves \(H\) and \(J\). Therefore every affine-character twist \(\chi u_A\) satisfies
\[
H(\chi u_A)\le C_{\rm sp}(t)J(\chi u_A)\le C_{\rm sp}(t)I(\chi u_A).
\tag{2.6}
\]

## 3. A nonzero quadratic polar row remains influence-paid under at most t defects

Write \(f=(-1)^q\sigma_D\) on \(d\) free variables and suppose the polar row of the quadratic part of \(q\) at coordinate \(i\) is nonzero.

### Lemma 3.1 (defect-stable half influence)

If \(m=|D|\), then
\[
\boxed{
\left|\operatorname{Inf}_i(f)-\frac12\right|
\le\frac{m}{2^{d-1}}.
}
\tag{3.1}
\]

#### Proof

For the pure quadratic phase \((-1)^q\), the multiplicative derivative in direction \(i\) is a nonconstant affine character on the other \(d-1\) variables because the polar row is nonzero. Exactly half of the \(i\)-directed cube edges therefore disagree.

Multiplying by \(\sigma_D\) toggles the disagreement status of an \(i\)-edge exactly when that edge crosses the defect boundary in direction \(i\). Each such edge has exactly one endpoint in \(D\), so there are at most \(m\) such edges. There are \(2^{d-1}\) total \(i\)-edges. This proves (3.1). QED.

### Corollary 3.2 (uniform local allocation payment)

If \(m\le t\) and \(d\ge L+a\), then
\[
\frac m{2^{d-1}}\le2^{1-a}\le\frac14.
\]
Hence
\[
j_i(f)\ge\frac12-2^{1-a}\ge\frac14.
\tag{3.2}
\]
Since the spectral-bit marginal satisfies \(\Pr(i\in Z)=\operatorname{Inf}_i(f)\),
\[
B_i(f)=H(Z_i\mid Z_{-i})\le H(Z_i)=h_2(j_i(f)).
\]
The function \(h_2(x)/x\) is decreasing on \((0,1/2]\), so
\[
\boxed{
B_i(f)\le c_*j_i(f),
\qquad c_*:=4h_2(1/4)=3.2451124978\ldots.
}
\tag{3.3}
\]
This is a purely physical, fresh-variable-free local payment. It uses neither root curvature nor child independence.

## 4. The adaptive stopping construction

Start at \(f=(-1)^q\sigma_D\). At every physical restriction, the same representation persists: the restricted phase is still quadratic and the surviving defect set has cardinality at most \(t\).

At a node with \(d\) free variables:

1. If \(d\le d_t=L+a-1\), **stop**.
2. Otherwise, if the quadratic polar matrix is zero, then the phase is affine; **stop**.
3. Otherwise choose any coordinate whose current polar row is nonzero and query it.

Every internal node in case 3 has
\[
d\ge d_t+1=L+a,
\]
so Corollary 3.2 applies. The procedure terminates because each query decreases \(d\). Let \(\mathcal T_0\) be this stopping prefix. Summing (3.3),
\[
\boxed{
R_{\mathcal T_0}\le c_*J_{\mathcal T_0}\le c_*Q_{\mathcal T_0}.
}
\tag{4.1}
\]

## 5. Every stopping leaf has the same explicit FEI constant Ct

There are two leaf types.

### Type I: small residual dimension

If a leaf has \(d\le d_t\), regard each remaining coordinate as a singleton symmetry part. The published \(d\)-part-symmetric FEI theorem gives
\[
H(g)\le(12.04+\log_2d)I(g)
\le C_tI(g).
\tag{5.1}
\]
(For \(d=0\), the leaf is constant and trivial.)

### Type II: affine quadratic remainder in high dimension

If the polar matrix vanishes while \(d>d_t\), then \(q\) is affine and therefore
\[
g=\pm\chi_Au_{D'}
\]
for a surviving defect set \(|D'|\le t\). Here \(d\ge L+a\), so Corollary 2.3 gives
\[
H(g)\le C_{\rm sp}(t)I(g).
\tag{5.2}
\]
The explicit bounds above give
\[
C_{\rm sp}(t)<6.296.
\]
Also
\[
c_*+\frac2{\ln2}=6.1305025796\ldots.
\tag{5.3}
\]
On the other hand \(d_t\ge2\), so
\[
C_t=12.04+\log_2d_t\ge13.04.
\tag{5.4}
\]
Thus the single constant \(C_t\) dominates both the leaf constant and the local-allocation-plus-recombination constant.

## 6. Proof of the FEI class theorem

Apply the inherited partial-tree identities to \(\mathcal T_0\). By (4.1), the paid dependent-branch recombination theorem, and the leaf bounds,
\[
\begin{aligned}
H(f)
&=R_{\mathcal T_0}+S_{\mathcal T_0}+H_L\\
&\le \left(c_*+\frac2{\ln2}\right)Q_{\mathcal T_0}+C_tI_L\\
&\le C_t(Q_{\mathcal T_0}+I_L)\\
&=C_tI(f).
\end{aligned}
\]
This proves (B). When \(t\ge8\), \(a=L\) and \(d_t=2L-1\), giving (C).

## 7. Hereditary allocation certificate

The same construction proves more than the class FEI inequality. Complete each stopping leaf by an arbitrary full physical restriction tree. For any Boolean leaf \(g\), the full-tree identity has constant terminal leaves, so
\[
H(g)=R_{\rm leaf}+S_{\rm leaf},\qquad S_{\rm leaf}\ge0,
\]
and therefore
\[
R_{\rm leaf}\le H(g)\le C_tI(g).
\]
Splicing these completions into \(\mathcal T_0\),
\[
R_{\mathcal T}
\le c_*Q_{\mathcal T_0}+C_tI_L
\le C_t(Q_{\mathcal T_0}+I_L)
=C_tI(f).
\]
This proves (A), equivalently
\[
\boxed{\mathcal A(f):=\inf_{\mathcal T\text{ full}}R_{\mathcal T}(f)/I(f)\le C_t.}
\tag{7.1}
\]
Thus the theorem is a genuine hereditary-allocation result, not merely a direct FEI estimate.

## 8. Why this is a real mechanism gain

The preceding P03 run isolated curvature-aware stopping as a live route but showed that blind root curvature can be quadratic in dimension even when total influence is linear. The newest NM13-02 run then showed that on cubic stars the natural one-query path directly into a quadratic leaf can have consumed-curvature/query ratio tending to infinity. The present theorem bypasses both prices on a different nontrivial family: while quadratic structure remains, one pays only the queried spectral bit using the defect-stable half-influence lemma; once the quadratic structure becomes affine, the defect itself is sparse enough to be paid by isoperimetry.

For a defect set of size \(t\), a naive tree that isolates defect points can have depth of order \(t\), so the companion descendant-depth recursion gives an \(O(t)\)-scale hereditary constant on that naive route. Here no defect point is isolated and the constant grows only as \(O(\log\log t)\). For \(t=1\), NM13-02's specialized one-defect constant is much sharper; this report claims scope growth, not a better one-point constant.

This route is also distinct from NM13-02's announced next attack on influence lifetime / fractional covers of high-degree monomials. No peer scope is duplicated.

## 9. Retired routes remain retired

Nothing here revives any of the following:

- the false pointwise erasure shortcut;
- any fixed-coefficient affine-drift payment;
- the retired resolvent/interpolation inequalities;
- Han's refuted absolute-overlap selector;
- the derivative-degree scalar scheduling route refuted by the one-defect family;
- a blind universal root square-curvature bound;
- a universal direct consumed-curvature/query ratio, already obstructed by cubic stars.

The restricted fresh-control theorem remains restricted and is not used in this proof.

## 10. Executed sanity checks

A new checker was executed and preserved at

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T07-29-11+0300__check_finite_defect_quadratic.py`

creation commit `9d18262b3da60cc9b76b131814499e6dab45ae1b`, blob `48e87a7424ec6fd396c2cc294e4a8c2906933277`.

Its actual output was preserved at

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T07-29-11+0300__finite_defect_quadratic_check.json`

creation commit `9225bf4ae5ef8c1e3fc0926edcd659f4cac3f626`, blob `07f0aba865833b311909558f979f1059f491c86c`.

Checks performed:

- **39,376** exhaustive sparse-sign cases through dimension four;
- **31,376** exhaustive nonzero-polar pivot cases through dimension four, over all quadratic edge masks and every defect set of size at most two;
- **3,500** deterministic-seed sampled quadratic-defect functions through dimension seven.

The maximum pivot-lemma numerical violation was exactly `0.0`. The largest sampled class-bound margin was negative (`-10.0841104177484`). The largest FEI ratio observed among the exhaustive sparse cases was `3.402475551198587`. The checker status is `PASS`. These finite checks support but do not replace the all-dimensional proofs above.

## 11. Remaining full-scope obstruction and next attack

Full FEI remains open because an arbitrary Boolean function need not stay close in Hamming distance to a quadratic phase under restriction. The present argument identifies a more flexible possible generalization: replace cardinality \(|D|\) by a restriction-stable complexity of the defect set that simultaneously guarantees

1. nonzero quadratic polar rows remain bounded away from folded influence zero while the residual dimension is large; and
2. once the polar part vanishes, the defect leaf has an ambient-dimension-free entropy/influence certificate.

The next nonredundant P03 attack should test **decision-tree complexity or edge-boundary complexity of the defect set** as this replacement. This remains complementary to NM13-02's high-degree-monomial influence-lifetime route.

## Metrics

- full FEI: `OPEN -> OPEN`;
- finite universal source constant: `UNKNOWN -> UNKNOWN`;
- P03 native finite-dimensional atlas: `6 -> 6`;
- fresh-variable dependence in the new theorem: `none`;
- new class parameter: Hamming distance `t` from an arbitrary quadratic phase;
- new hereditary/FEI constant: `C_t=12.04+log2(L+max(3,L)-1)`, `L=ceil(log2 t)`; for `t>=8`, `C_t=12.04+log2(2L-1)=O(log log t)`;
- independent audit: `pending`;
- publication priority: `UNVERIFIED`.

## ledger_delta

```yaml
ledger_delta:
  owner: P03
  parent: T01_Friedgut_Kalai_FEI
  source_status_before: OPEN_PARTIAL
  source_status_after: OPEN_PARTIAL
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  native_atlas_before: 6
  native_atlas_after: 6
  new_claim:
    id: P03-FEI-FINITE-DEFECT-QUADRATIC-STOPPING-01
    status: PROVED_SELF_CHECKED
    scope: "If f differs from a quadratic phase at at most t>=1 cube points, then there is a full physical restriction tree with R_T<=C_t I(f) and H(f)<=C_t I(f), where L=ceil(log2 t), a=max(3,L), d_t=L+a-1, C_t=12.04+log2 d_t. For t>=8, C_t=12.04+log2(2 ceil(log2 t)-1)=O(log log t)."
    fresh_variables: false
    full_FEI: false
    audit: pending
    priority: unverified
  mechanism_gain:
    - nonzero quadratic polar rows remain queried-influence-paid while ambient size dominates Hamming defect count
    - affine high-dimensional leaves are paid by sparse-sign entropy plus cube isoperimetry
    - low-dimensional leaves use the published d-part-symmetric FEI theorem with singleton parts
    - dense quadratic curvature is never charged
  preserved_failures:
    - pointwise_erasure
    - fixed_coefficient_affine_drift
    - resolvent_interpolation
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - blind_root_square_curvature
    - direct_curvature_over_queried_influence_cubic_star
  companion_coordination:
    worker: NM13-02
    newest_blob: dfbd0ec25828d1edff10d6b7f9bf8a10e45b66e0
    complementary_scope: finite_Hamming_defects_of_quadratics_not_influence_lifetime_high_degree_monomial_cover
  artifacts:
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T07-29-11+0300__check_finite_defect_quadratic.py
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T07-29-11+0300__finite_defect_quadratic_check.json
  next_attack: restriction_stable_defect_complexity_via_decision_tree_or_edge_boundary
```

**End of complete run report.**
