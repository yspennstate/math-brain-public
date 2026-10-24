Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — Reed–Muller derivative gaps pay hereditary allocation at algebraic degree

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI):
\[
\mathbf H(f)\le C\,\mathbf I(f)
\]
with one finite universal constant \(C\) for every Boolean \(f\) on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved. The source metric “finite universal upper bound for \(C_{\rm FEI}\)” remains **UNKNOWN -> UNKNOWN**. The inherited native P03 finite-dimensional atlas remains **6 -> 6** and is not enlarged here.

**Mechanism-level movement.** The preceding P03 report reduced the fresh-variable-free stopping-tree architecture to hereditary allocation. This run proves a new all-dimensional derivative-profile payment. If
\[
f=(-1)^P,\qquad P:\mathbb F_2^n\to\mathbb F_2
\]
has algebraic degree \(d\), and the nonconstant derivative \(D_iP\) has degree \(r_i\), then with
\[
j_i(f):=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
\qquad
\phi(r):=2^r h_2(2^{-r}),
\]
one has
\[
\boxed{\quad
\mathbf H(f)\le \sum_{i:D_iP\ {\rm nonconstant}}\phi(r_i)\,j_i(f).
\quad}
\tag{0.1}
\]
The same local estimate pays the P03 hereditary allocation at **every node of every adaptive physical restriction tree**:
\[
\boxed{\quad
R_{\mathcal T}(f)\le
\sum_{v\ {\rm internal}}w_v\phi(r_v)j_{i(v)}(f_v).
\quad}
\tag{0.2}
\]
For algebraic degree at most \(d\),
\[
\boxed{\quad
R_{\mathcal T}(f)\le \kappa_d J_{\mathcal T}(f)
\le \kappa_d Q_{\mathcal T}(f),\qquad
\mathbf H(f)\le\kappa_d J(f)\le\kappa_d I(f),
\quad}
\tag{0.3}
\]
where
\[
\kappa_1=0,\qquad
\kappa_d=2^{d-1}h_2(2^{1-d})
\le d-1+\frac1{\ln2}\quad(d\ge2).
\tag{0.4}
\]
Thus P03's tree-optimized hereditary allocation ratio satisfies
\[
\boxed{\mathcal A(f)\le\kappa_d}
\tag{0.5}
\]
for every degree-\(\le d\) Boolean phase, in every dimension, without fresh controls.

This strictly improves P03's archived degree-descent estimate
\[
\mathbf H(f)\le3d\,J(f)
\]
to \(\mathbf H(f)\le\kappa_dJ(f)\), asymptotically \((d+0.4427\ldots)J(f)\), and it upgrades a direct class inequality to a hereditary statement valid under arbitrary dependent physical branching. It does **not** give a universal constant because \(d\) may grow with \(n\).

## 1. Exact scope and dependencies consumed

The progress-first directive was followed: only dependencies needed for this derivation were read, not the whole archive.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: T01 asks for hereditary allocation or paid dependent recombination without fresh-control dependence. It identifies NM13-02 as P03's current complementary FEI worker.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: preserves the restricted fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` under its control hypotheses and explicitly says that this is not full FEI.
- `proofnet24/P03-fei/README.md`, blob `b880799e93758ca6576dfc9aa9711c1d4c32d08a`: full FEI remains open; the shifted-threshold family refutes Han's stronger all-coordinate absolute-overlap criterion; the retired pointwise erasure, resolvent and fixed-coefficient affine-drift routes stay retired.
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`: P03's preceding substantive run proves the exact adaptive-tree telescope and pays dependent-branch recombination by \(2/\ln2\) times charged influence. It identifies hereditary allocation \(R_{\mathcal T}\) as the remaining obstruction.
- `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`: exact one-coordinate erasure/JS identity, \(B_i=H(Z_i\mid Z_{-i})\), and the spectral-marginal identity used below.
- `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T23-20-52Z__report.md`, blob `4ebadd5bbaeae49280e37e80c63a48b826f7c261`: the archived all-degree bound \(H\le3dJ\), the majority refutation of every finite affine-drift constant, and the erasure-curvature identity. The affine-drift route is not reopened here.
- `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T03-10-31+0300__quadratic-rank-hereditary-allocation.md`, blob `cd7b18429c67d2b20c14932ff17340b68be86069`: the companion worker proves the exact quadratic-phase identity \(\mathcal A(f)=\operatorname{rank}M/(2I(f))\le1\) and proposes sparse-cubic quadratic-leaf rank variation as its next route. The present run deliberately takes a different route: a general derivative-degree payment valid for all algebraic degrees.
- `POSTED.md` was checked for exact-scope exclusions. The posted percolation entropy result is not universal FEI and is not reused as a full-scope claim.

### Current public-source scope

The Friedgut–Kalai conjecture remains the universal target. González–MacManus–Pereyra, arXiv:2606.00246v2 (revised 9 June 2026), still presents full FEI as open and proves restricted classes through a restriction/stopping-tree framework; its listed classes include \(\delta\)-tribes, monotone tribe-separation functions and semi-separation functions. Xiao Han's 2025 general result has the influence-profile logarithmic term and is not a universal FEI constant.

A bounded fresh search for FEI plus algebraic degree / Reed–Muller terms recovered the 2014 Gangopadhyay–Stănică cryptographic FEI paper (strict avalanche, plateaued functions, monomial ANF, direct sums, concatenations, and quadratic affine-equivalence statements) but did not surface the derivative-profile/hereditary theorem proved below. This is **bounded negative evidence only**; novelty is **UNVERIFIED**.

## 2. Why this route is genuinely different

Three live approaches were compared.

1. **Erasure curvature + Boolean signed convolution.** This remains a universal route, but the missing signed-cancellation estimate has not been found. Repeating the curvature identity would be an unchanged run.
2. **Quadratic rank potential.** NM13-02 has just solved this exactly for quadratic phases and is taking the sparse-cubic quadratic-leaf route. Duplicating it would violate complementary scope.
3. **Reed–Muller derivative gap.** A physical derivative of an algebraic-degree-\(d\) phase has degree at most \(d-1\). The minimum-distance theorem for Reed–Muller codes prevents a nonconstant low-degree derivative from being arbitrarily rare or arbitrarily common. Since hereditary erasure is at most the binary entropy of the derivative probability, this gives an explicit local payment that survives every physical restriction. This route was selected and completed.

The key point is that this is not the previously failed “binary entropy of local influence” as a universal constant argument. That envelope does lose a logarithm when the derivative degree grows. Here the exact loss is isolated as \(\phi(r)\), tied to the **algebraic degree of the derivative**, and the theorem records precisely that remaining cost rather than hiding it.

## 3. Notation

Work on \(\mathbb F_2^n\). Every Boolean function can be written uniquely as
\[
f(x)=(-1)^{P(x)}
\]
with \(P\) multilinear over \(\mathbb F_2\). Let \(d=\deg P\).

Let \(Z\subseteq[n]\) have the squared Fourier law
\[
\Pr(Z=S)=\widehat f(S)^2.
\]
Write
\[
p_i:=\operatorname{Inf}_i(f)
=\Pr_x[f(x)\ne f(x+e_i)].
\]
By Parseval applied to the discrete derivative,
\[
\Pr(i\in Z)=\sum_{S\ni i}\widehat f(S)^2=p_i.
\tag{3.1}
\]
Set
\[
j_i:=\min\{p_i,1-p_i\},\qquad J(f):=\sum_i j_i.
\tag{3.2}
\]
For a physical coordinate \(i\), P03's hereditary erasure is
\[
B_i(f):=H(Z_i\mid Z_{-i}).
\tag{3.3}
\]

For a nonconstant derivative
\[
D_iP(x):=P(x)+P(x+e_i)
\]
(which does not depend on \(x_i\)), put
\[
r_i:=\deg(D_iP)\ge1.
\tag{3.4}
\]
If \(D_iP\) is constant, no \(r_i\) is needed.

All Shannon entropies below are in bits. Put
\[
h_2(t)=-t\log_2t-(1-t)\log_2(1-t).
\]

## 4. Reed–Muller minimum-distance lemma, proved from scratch

**Lemma 4.1.** Let \(R:\mathbb F_2^m\to\mathbb F_2\) be a nonzero multilinear polynomial of degree at most \(r\). Then
\[
\Pr[R=1]\ge2^{-r}.
\tag{4.1}
\]

### Proof

Induct on \(m\). The statement is trivial for \(m=0\). Write
\[
R(x',x_m)=A(x')+x_mB(x')
\]
with \(\deg A\le r\) and, if \(B\ne0\), \(\deg B\le r-1\).

If \(B=0\), then \(A\ne0\), and by induction its support on \(\mathbb F_2^{m-1}\) has size at least \(2^{m-1-r}\). Both values of \(x_m\) reproduce that support, so
\[
|\operatorname{supp}R|
=2|\operatorname{supp}A|
\ge2^{m-r}.
\]

If \(B\ne0\), then for every \(x'\) with \(B(x')=1\), the two bits
\[
R(x',0)=A(x'),\qquad R(x',1)=A(x')+1
\]
are opposite, so exactly one belongs to the support. Therefore
\[
|\operatorname{supp}R|
\ge|\operatorname{supp}B|
\ge2^{(m-1)-(r-1)}
=2^{m-r}
\]
by induction applied to \(B\). Divide by \(2^m\). QED.

**Corollary 4.2 (two-sided derivative gap).** If \(D_iP\) is nonconstant of degree \(r_i\), then
\[
\boxed{j_i(f)\ge2^{-r_i}.}
\tag{4.2}
\]

### Proof

The pivotal indicator is exactly
\[
1_{\{f(x)\ne f(x+e_i)\}}=D_iP(x),
\]
so
\[
p_i=\Pr[D_iP=1].
\]
Because \(D_iP\) is nonconstant, both \(D_iP\) and \(1+D_iP\) are nonzero polynomials of degree \(r_i\). Lemma 4.1 applied to both gives
\[
p_i\ge2^{-r_i},\qquad1-p_i\ge2^{-r_i}.
\]
Taking the minimum proves (4.2). QED.

Constant derivatives are exactly the harmless endpoints: \(D_iP\equiv0\) gives \(p_i=0\), while \(D_iP\equiv1\) gives \(p_i=1\). In both cases \(j_i=0\).

## 5. The sharp scalar conversion from derivative rarity to entropy

Define for integers \(r\ge1\)
\[
\phi(r):=\frac{h_2(2^{-r})}{2^{-r}}=2^rh_2(2^{-r}).
\tag{5.1}
\]

**Lemma 5.1.** The function \(t\mapsto h_2(t)/t\) is strictly decreasing on \((0,1)\). Consequently, if \(0<j\le1/2\) and \(j\ge2^{-r}\), then
\[
h_2(j)\le\phi(r)j.
\tag{5.2}
\]

### Proof

A direct derivative gives
\[
h_2'(t)=\log_2\frac{1-t}{t}.
\]
Therefore
\[
t h_2'(t)-h_2(t)=\log_2(1-t)<0,
\]
and
\[
\frac{d}{dt}\frac{h_2(t)}t
=\frac{t h_2'(t)-h_2(t)}{t^2}<0.
\]
Thus \(h_2(t)/t\) decreases. Since \(j\ge2^{-r}\), (5.2) follows. QED.

Since \(2^{-r}\) decreases with \(r\), \(\phi(r)\) increases with \(r\).

There is also a simple explicit estimate. Put \(\delta=2^{-r}\). Then
\[
\phi(r)
=r+(2^r-1)\log_2\frac1{1-2^{-r}}.
\tag{5.3}
\]
Using
\[
-\ln(1-\delta)\le\frac{\delta}{1-\delta},
\]
we obtain
\[
(2^r-1)\log_2\frac1{1-2^{-r}}
\le\frac1{\ln2}.
\]
Hence
\[
\boxed{\phi(r)\le r+\frac1{\ln2}.}
\tag{5.4}
\]

## 6. The derivative-profile entropy theorem

**Theorem 6.1 (anisotropic derivative-degree payment).** For every Boolean \(f=(-1)^P\),
\[
\boxed{
H(\widehat f^2)
\le
\sum_{i:D_iP\ {\rm nonconstant}}
\phi(r_i)\,j_i(f).
}
\tag{6.1}
\]

### Proof

By entropy subadditivity and (3.1),
\[
H(Z)\le\sum_iH(Z_i)
=\sum_i h_2(p_i)
=\sum_i h_2(j_i).
\tag{6.2}
\]
If \(D_iP\) is constant, then \(p_i\in\{0,1\}\), so its term in (6.2) is zero.

If \(D_iP\) is nonconstant of degree \(r_i\), Corollary 4.2 gives
\[
j_i\ge2^{-r_i}.
\]
Lemma 5.1 therefore gives
\[
h_2(j_i)\le\phi(r_i)j_i.
\]
Sum over coordinates. QED.

This estimate is genuinely profile-sensitive: a high-degree phase can still receive a small coefficient on any coordinate whose *actual derivative* has low degree.

## 7. Uniform algebraic-degree consequence and improvement over the archived \(3dJ\) bound

If \(\deg P=d\), every nonconstant \(D_iP\) has degree
\[
r_i\le d-1.
\]
Since \(\phi\) is increasing,
\[
H(f)\le\phi(d-1)\sum_i j_i.
\]
Define
\[
\kappa_1:=0,\qquad
\kappa_d:=\phi(d-1)
=2^{d-1}h_2(2^{1-d})\quad(d\ge2).
\tag{7.1}
\]

**Corollary 7.1.** Every Boolean phase of algebraic degree at most \(d\) satisfies
\[
\boxed{
H(f)\le\kappa_dJ(f)\le\kappa_dI(f).
}
\tag{7.2}
\]
For \(d\ge2\),
\[
\boxed{
\kappa_d\le d-1+\frac1{\ln2}
=d+0.442695\ldots .
}
\tag{7.3}
\]

For reference,
\[
\begin{array}{c|ccccccc}
d&2&3&4&5&6&7&8\\ \hline
\kappa_d&
2&
3.2451124978&
4.3485155456&
5.3966410659&
6.4199143780&
7.4313648195&
8.4370447799
\end{array}
\]
The archived P03 derivative-chain theorem gives \(H\le3dJ\). Thus (7.2) is a strict all-dimensional improvement throughout \(d\ge2\), obtained without fresh variables or derivative-chain growth.

For \(d=2\), (7.2) gives \(H\le2J\), consistent with the companion's sharper exact quadratic allocation formula \(\mathcal A\le1\). The present theorem is not intended to replace that rank identity; it extends a uniform mechanism to every algebraic degree.

## 8. Hereditary allocation on arbitrary dependent physical restriction trees

Now return to P03's live obstruction. Let \(\mathcal T\) be an arbitrary finite adaptive physical restriction tree. At an internal node \(v\), the current Boolean restriction is
\[
f_v=(-1)^{P_v},
\]
the queried coordinate is \(i(v)\), and the node weight is \(w_v=2^{-\operatorname{depth}(v)}\). Recall
\[
R_{\mathcal T}(f)
=\sum_{v\ {\rm internal}}w_vB_{i(v)}(f_v),
\]
\[
J_{\mathcal T}(f)
=\sum_{v\ {\rm internal}}w_vj_{i(v)}(f_v),
\qquad
Q_{\mathcal T}(f)
=\sum_{v\ {\rm internal}}w_v\operatorname{Inf}_{i(v)}(f_v).
\]

For each node-coordinate with nonconstant derivative, set
\[
r_v:=\deg D_{i(v)}P_v.
\]

**Theorem 8.1 (hereditary derivative-degree allocation).** Every adaptive physical restriction tree satisfies
\[
\boxed{
R_{\mathcal T}(f)
\le
\sum_{v:D_{i(v)}P_v\ {\rm nonconstant}}
w_v\phi(r_v)j_{i(v)}(f_v).
}
\tag{8.1}
\]
If the root phase has degree at most \(d\), then
\[
\boxed{
R_{\mathcal T}(f)
\le\kappa_dJ_{\mathcal T}(f)
\le\kappa_dQ_{\mathcal T}(f).
}
\tag{8.2}
\]

### Proof

At any node,
\[
B_i(f_v)=H((Z_v)_i\mid(Z_v)_{-i})
\le H((Z_v)_i)
=h_2(p_i(f_v))
=h_2(j_i(f_v)).
\tag{8.3}
\]
If the derivative is constant, \(p_i\in\{0,1\}\) and both sides of the desired local payment vanish.

If the derivative is nonconstant of degree \(r_v\), the Reed–Muller gap applies to the restricted polynomial exactly as before:
\[
j_i(f_v)\ge2^{-r_v}.
\]
Hence Lemma 5.1 gives
\[
B_i(f_v)\le\phi(r_v)j_i(f_v).
\]
Multiply by \(w_v\) and sum to prove (8.1).

Physical restriction cannot increase algebraic degree, so for a root of degree at most \(d\), every nonconstant derivative at every descendant has degree at most \(d-1\). Hence \(\phi(r_v)\le\kappa_d\). This proves the first inequality of (8.2); the second is termwise \(j_i\le\operatorname{Inf}_i\). QED.

For a full restriction tree, P03's exact influence telescope gives
\[
Q_{\mathcal T}(f)=I(f),
\]
because every leaf is constant. Therefore
\[
\boxed{
\mathcal A(f):=
\frac1{I(f)}\inf_{\mathcal T\ {\rm full}}R_{\mathcal T}(f)
\le\kappa_d.
}
\tag{8.4}
\]
In fact (8.2) holds for **every** full tree, not just an optimized one.

This is the main mechanism-level gain of the run. The hereditary allocation obstruction is universally paid on the entire restriction-closed degree-\(\le d\) class, under arbitrary branch-dependent coordinate choices, without fresh controls.

## 9. A sharper residual full-scope target

The theorem also isolates a weighted derivative-degree charge that would suffice for full FEI.

For any tree define
\[
D_{\mathcal T}^{\deg}
:=
\sum_{v\ {\rm internal}}
w_v\,r_v\,j_{i(v)}(f_v),
\tag{9.1}
\]
with zero contribution for constant derivatives. From (5.4) and (8.1),
\[
R_{\mathcal T}
\le
D_{\mathcal T}^{\deg}
+\frac1{\ln2}J_{\mathcal T}.
\tag{9.2}
\]
P03's preceding paid-recombination theorem gives
\[
S_{\mathcal T}
\le\frac2{\ln2}J_{\mathcal T}.
\tag{9.3}
\]
For a full tree, \(H=R_{\mathcal T}+S_{\mathcal T}\) and \(J_{\mathcal T}\le Q_{\mathcal T}=I(f)\). Therefore:

**Corollary 9.1 (conditional full-FEI reduction).** If there is a universal \(K\) such that every Boolean \(f\) admits a full physical restriction tree with
\[
D_{\mathcal T}^{\deg}\le K I(f),
\tag{9.4}
\]
then
\[
\boxed{
H(f)\le\left(K+\frac3{\ln2}\right)I(f)
}
\tag{9.5}
\]
for every Boolean \(f\).

No universal bound (9.4) is proved here. This is a reduction, not closure. Its value is that it turns “hereditary allocation” into a concrete weighted quantity: large derivative degree is costly only when multiplied by the **folded influence actually charged at that node**.

This target is complementary to NM13-02's sparse-cubic rank-variation route. Their route exploits exact quadratic structure after a hitting set of cubic monomials is queried. The present residual target asks instead whether high derivative degree can be scheduled where its charged folded influence is small enough in aggregate.

## 10. Sanity checker actually executed

New checker:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__check_reed_muller_allocation.py`.

Archived output:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__reed_muller_allocation_check.json`.

The checker was executed before report persistence. It independently computes ANF coefficients, algebraic derivative degrees, Walsh spectra, influences, \(B_i\), \(H\), \(J\), profile payments and the uniform \(\kappa_d\) payment.

It exhaustively checked **every Boolean function through dimension 4**:
- \(n=1\): 4 functions;
- \(n=2\): 16 functions;
- \(n=3\): 256 functions;
- \(n=4\): 65,536 functions.

It also checked 2,000 deterministic seed-20260920 random ANF samples in dimension 5, with degree caps cycled through 2,3,4,5.

Every case verified:
1. the Parseval influence / derivative-weight identity;
2. the two-sided Reed–Muller gap \(j_i\ge2^{-r_i}\) for nonconstant derivatives;
3. the local hereditary estimate \(B_i\le\phi(r_i)j_i\);
4. the global profile estimate \(H,B\le\sum_i\phi(r_i)j_i\);
5. the uniform degree bound \(H,B\le\kappa_dJ\).

Archived status: `PASS`. Maximum numerical violation: `0.0` at tolerance \(2\times10^{-9}\). The maximum observed ratios \(H/J\) in dimensions 1–4 were respectively
\[
0,\quad2,\quad2.9558895823,\quad3.4024755512.
\]
Finite checks are self-checks only; the theorem is the written proof in Sections 4–8.

## 11. What moved, what did not, and failed-route preservation

### Source-level quantity

- Full universal FEI: **OPEN -> OPEN**.
- Universal finite constant: **UNKNOWN -> UNKNOWN**.
- Native finite-dimensional atlas: **6 -> 6**.
- No publication-priority or independent-review claim.

### Genuine mechanism gain

Before this run:
- P03 had paid arbitrary dependent-branch recombination universally, but hereditary allocation remained unbounded.
- P03 had only \(H\le3dJ\) as a general algebraic-degree estimate.
- NM13-02 had just solved hereditary allocation exactly for quadratic phases.

After this run:
- every degree-\(\le d\) Boolean phase, in every dimension, has hereditary allocation
  \[
  R_{\mathcal T}\le\kappa_dJ_{\mathcal T}\le\kappa_dQ_{\mathcal T}
  \]
  on **every adaptive physical restriction tree**;
- the direct class estimate improves to
  \[
  H\le\kappa_dJ,\qquad
  \kappa_d\le d-1+1/\ln2;
  \]
- the stronger anisotropic payment uses each actual derivative degree \(r_i\);
- the remaining full-scope route is sharpened to the weighted derivative-degree charge (9.4).

### Failed lemmas that remain retired

Nothing here revives:
- the all-constant affine-drift payment \(L\le C\Delta_{\rm aff}\), refuted by majority for every finite \(C\);
- the false pointwise \(H\le B+(2/\ln2)I\);
- retired resolvent/erasure interpolation inequalities;
- coefficient-specific drift claims;
- the all-coordinate absolute-overlap selector, refuted by shifted thresholds;
- independence between dependent physical branches.

The binary-entropy envelope by itself is **not** claimed universal: its coefficient is exactly \(\phi(r)\), which grows with derivative degree. The new input is the Reed–Muller support gap, and the residual growth is stated openly.

## 12. Next attack

The most direct complementary P03 target is now to test whether the weighted tree charge
\[
D_{\mathcal T}^{\deg}
=\sum_vw_v r_vj_v
\]
can be bounded independently of dimension by choosing the restriction coordinate adaptively. Two adversarial families are especially informative:

1. the shifted-threshold family that killed Han's absolute-overlap criterion, where algebraic degree is high but symmetry may permit cheap early queries;
2. lexicographic / recursive-composition lower-bound families for the FEI constant, where any proposed adaptive degree payment should be stress-tested against known large \(H/I\).

If (9.4) fails on one of these, that will be a decisive obstruction to this route. If it survives, the next proof task is a scheduling/hitting-set lemma that lowers derivative degree while charging only folded influence. The NM13-02 sparse-cubic rank calculation remains complementary and should not be duplicated.

## 13. ledger_delta

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
    - paid_dependent_recombination_proved_but_general_hereditary_allocation_open
    - archived_general_algebraic_degree_bound_H_le_3dJ
    - exact_quadratic_A_le_1_only_from_companion
  mechanism_after:
    - H_le_sum_i_phi_derivative_degree_i_times_folded_influence_i
    - every_degree_d_tree_R_le_kappa_d_Jtree_le_kappa_d_Qtree
    - every_degree_d_phase_A_le_kappa_d
    - H_le_kappa_d_J_with_kappa_d_approximately_d_plus_0.4427
    - conditional_full_FEI_reduction_to_weighted_derivative_degree_tree_charge
  phi_r: 2^r_h2(2^-r)
  kappa_d: 2^(d-1)_h2(2^(1-d))
  kappa_upper: d-1+1/ln2
  arbitrary_adaptive_restriction_tree: true
  fresh_controls: false
  branch_independence_assumed: false
  quadratic_peer_result_preserved: true
  restricted_fresh_control_result_preserved: true
  full_FEI_claimed: false
  novelty: UNVERIFIED
  checker_status: PASS
  exhaustive_dimension: 4
  random_dimension5_samples: 2000
  failed_routes_preserved:
    - resolvent
    - pointwise_erasure
    - affine_drift_all_constants
    - Han_absolute_overlap
  substantive_unchanged_run_count: 0
  remaining_obstruction: universal_bound_or_counterexample_for_weighted_derivative_degree_charge
  next_attack: adaptive_degree_charge_on_shifted_threshold_and_lexicographic_obstruction_families
  artifacts:
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__check_reed_muller_allocation.py
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__reed_muller_allocation_check.json
```

**End of complete run report.**
