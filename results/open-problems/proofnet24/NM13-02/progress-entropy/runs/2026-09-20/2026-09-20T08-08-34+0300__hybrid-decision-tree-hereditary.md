Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — hybrid hereditary decision-tree payment; uniform <3 allocation for quadratic twists of nested canalizing cores

## 0. Parent status, scope, and this run's mathematical movement

**Parent problem:** Friedgut--Kalai Fourier entropy--influence (FEI) on the finite uniform cube,
\[
H(\widehat f^{\,2})\le C I(f)
\]
with one finite universal constant for every Boolean function.

**Parent status before -> after:** **OPEN -> OPEN.**  
**Universal finite upper bound for the unrestricted source constant:** **UNKNOWN -> UNKNOWN.**

This run therefore does **not** claim full FEI. The demonstrated mechanism gain is instead a new branch-dependent hereditary recursion that combines two different local payments rather than paying descendant influence once per restriction level.

Let
\[
c_0:=\frac1{\ln2}=1.4426950408\ldots,
\qquad
C_\chi:=2+\frac1{\sqrt e\,\ln2}=2.8750387749\ldots .
\]
For a physical decision-tree node with child hereditary constants \(K_+,K_-\), define
\[
D(K_+,K_-):=\max\{c_0,1+K_+,1+K_-\},
\]
\[
M(K_+,K_-):=\max\left\{C_\chi,K_+,K_-,1+\frac{K_++K_-}{2}\right\},
\]
and
\[
\boxed{\Phi(K_+,K_-):=\min\{D(K_+,K_-),M(K_+,K_-)\}.}
\tag{0.1}
\]
The main theorem below proves that \(\Phi\) is a valid hereditary-allocation propagation rule.

Consequently, if \(h\) is computed by any physical decision tree \(T\), \(Q\) is any quadratic polynomial (including arbitrary couplings among the decision-tree coordinates and all other coordinates), and
\[
f=(-1)^Qh,
\]
then putting \(\kappa=1\) at every leaf of \(T\) and propagating by (0.1) gives
\[
\boxed{\mathcal A(f)\le\kappa(T),}
\qquad
\mathcal A(f):=\inf_{\mathcal T\ {m full}}\frac{R_{\mathcal T}(f)}{I(f)}.
\tag{0.2}
\]
This is an all-dimensional hereditary theorem with no fresh variables.

Two explicit consequences are:

1. if \(T\) has height \(d\), then \(\kappa(T)\le d+1\), recovering the earlier descendant-depth bound;
2. if \(T\) has \(L\) leaves, then
   \[
   \boxed{\kappa(T)\le C_\chi-\log_2 3+\log_2L
   =1.2900762742\ldots+\log_2L.}
   \tag{0.3}
   \]

More importantly, a one-live-child (nested-canalizing) spine of arbitrary depth has
\[
\boxed{\kappa(T)<3}
\tag{0.4}
\]
uniformly in its depth. This directly answers, on a large structured class, the precise decision-tree-complexity route proposed at the end of P03's newest proof.

The theorem is hereditary allocation, not merely finite-dimensional verification. The checker at the end is only a sanity check.

## 1. Controlling directive, compact handoff, and current dependencies

The controlling owner policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Current LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory, paired with P03. The policy explicitly prioritizes new mathematics and says restricted FEI classes do not close the parent conjecture.

`POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem is duplicated.

### Compact handoff of prior NM13-02 mathematics

The following earlier T01 results are preserved without scope inflation.

- **Quadratic rank telescope.** For a quadratic phase \((-1)^q\), every full adaptive physical restriction tree has hereditary allocation \(R=r/2\le I\), where \(r\) is the polar rank.
- **Exact influence budget / max-splicing.** Queried influence plus weighted residual-leaf influence is exactly root influence, so branch-dependent leaf certificates can be grafted without summing their constants.
- **Character-child payment.** A split with a signed-character child has local allocation constant \(C_\chi\).
- **Truncated minor-child payment.** The raw minor-child load is unnecessary at sufficiently large folded queried influence; one-point perturbations of arbitrary quadratic phases have bounded hereditary allocation.
- **Descendant-influence payment.** For every split,
  \[
  B_i(f)\le c_0j_i(f)+\frac{I(f^+)+I(f^-)}2.
  \tag{1.1}
  \]
  This gave the previous depth recursion \(K_v\le1+\max K_{v,\pm}\), bounded-depth-to-quadratic certificates, and the cubic-star theorem.

The false pointwise erasure shortcut, fixed-coefficient affine-drift route, Han absolute-overlap selector, derivative-degree scalar scheduler, and retired resolvent/interpolation routes remain false/retired. Nothing below reintroduces them.

### P03 dependency actually needed in this run

The newest P03 report is
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T07-29-11+0300__fei-finite-defect-quadratic-stopping.md`, blob `4595de09809b9a7f7bd2fe91a7bf1354a81c863b`.
It proves a hereditary/FEI theorem for Hamming distance \(t\) from a quadratic phase with constant \(O(\log\log t)\), and ends by identifying the next full-scope obstruction: replace raw cardinality \(|D|\) by a **restriction-stable defect complexity**, explicitly suggesting decision-tree complexity or edge-boundary complexity. The theorem below takes the decision-tree branch of that suggestion.

The local arbitrary-child inequality used here was first proved by P03 in
`2026-09-20T05-32-22+0300__fei-minor-child-allocation.md`, blob `7e12f35a9c2fae61f3c63e8434a493762a0e8081`:
\[
B_i(f)\le C_\chi j_i(f)+\min\{I(f^+),I(f^-)\}.
\tag{1.2}
\]
P03 retains ownership of that local lemma. To avoid treating a reported peer proof as automatically established, Section 2 below independently rederives (1.2) from its Fourier-fiber formula before using it. The new claim of this report is the hybrid propagation rule and its decision-tree consequences.

P03 also separately reports the paid recombination theorem
\[
S_{\mathcal T}\le\frac2{\ln2}J_{\mathcal T}\le\frac2{\ln2}Q_{\mathcal T}.
\tag{1.3}
\]
That theorem is **not** needed for the hereditary result proved here. It is used only for an explicitly PROJECT-CONDITIONAL FEI corollary in Section 7, pending later independent review.

## 2. Recheck of the P03 arbitrary-child local payment

Let \(i\) be a physical coordinate and let \(g=f^+\), \(h=f^-\) be the two restrictions. For each residual Fourier label \(T\), write
\[
a_T=\widehat g(T),\qquad b_T=\widehat h(T).
\]
The two full Fourier coefficients in the fiber over \(T\) are
\[
\frac{a_T+b_T}{2},\qquad \frac{a_T-b_T}{2}.
\]
Hence, with
\[
q_T:=\frac{a_T^2+b_T^2}{2},\qquad
 e_T:=\frac{(a_T-b_T)^2}{4},
\]
the exact conditional spectral-bit entropy is
\[
\boxed{B_i(f)=\sum_Tq_T h_2(e_T/q_T),}
\tag{2.1}
\]
with zero-mass fibers contributing zero.

Multiplication by the physical character \(x_i\) complements the spectral bit and exchanges queried influence \(\delta\) with \(1-\delta\), while preserving \(B_i\) and both child total influences. Thus normalize
\[
\varepsilon:=j_i(f)=\Pr[g\ne h]\le\frac12.
\]
Exchange the children if necessary so that \(I(g)=\min\{I(f^+),I(f^-)\}\), and multiply both by a common sign so that \(\mathbb Eg\ge0\). Put
\[
\eta=\Pr[g=-1]\le\frac12,\qquad \beta=\Pr[h=-1].
\]
Since \(g,h\) differ on an \(\varepsilon\)-fraction,
\[
|\beta-\eta|\le\varepsilon.
\tag{2.2}
\]

For nonconstant fibers, \(h_2\le1\), so
\[
\begin{aligned}
\sum_{T\ne\varnothing}q_Th_2(e_T/q_T)
&\le\sum_{T\ne\varnothing}q_T\\
&=\frac12(\operatorname{Var}g+\operatorname{Var}h)\\
&=2\eta(1-\eta)+2\beta(1-\beta).
\end{aligned}
\]
If \(t=\beta-\eta\), then \(|t|\le\varepsilon\), and because \(\eta\le1/2\),
\[
\beta(1-\beta)-\eta(1-\eta)
=t(1-2\eta)-t^2\le\varepsilon(1-\varepsilon).
\]
Also cube Poincare gives \(4\eta(1-\eta)=\operatorname{Var}(g)\le I(g)\). Therefore
\[
\sum_{T\ne\varnothing}q_Th_2(e_T/q_T)
\le I(g)+2\varepsilon(1-\varepsilon).
\tag{2.3}
\]

At the constant Fourier fiber,
\[
e_\varnothing=(\beta-\eta)^2\le\varepsilon^2.
\]
For fixed \(e\), the function \(q\mapsto qh_2(e/q)\) is increasing on \([e,1]\), and
\[
h_2(x)\le x\log_2(e/x).
\]
Thus
\[
q_\varnothing h_2(e_\varnothing/q_\varnothing)
\le\varepsilon^2\log_2\frac e{\varepsilon^2}.
\tag{2.4}
\]
Combining (2.3)--(2.4),
\[
B_i(f)\le I(g)+\varepsilon U(\varepsilon),
\]
where
\[
U(\varepsilon)=2(1-\varepsilon)+\varepsilon\log_2\frac e{\varepsilon^2}.
\]
A direct derivative calculation gives the unique maximizer
\[
\varepsilon_0=\frac1{2\sqrt e},
\qquad
\max_{0<\varepsilon\le1/2}U(\varepsilon)
=2+\frac1{\sqrt e\ln2}=C_\chi.
\]
Therefore
\[
\boxed{B_i(f)\le C_\chi j_i(f)+\min\{I(f^+),I(f^-)\}.}
\tag{2.5}
\]
This reproduces the exact P03 local input; no independent-audit claim is made.

## 3. The new hybrid branch-propagation theorem

At a node \(v\), let the queried coordinate be \(i\), write
\[
\alpha=\operatorname{Inf}_i(f),\quad j=j_i(f),\quad
a=I(f^+),\quad b=I(f^-),
\]
and suppose the chosen continuation trees below the children satisfy
\[
R_+\le K_+a,\qquad R_-\le K_-b.
\]
The hereditary allocation of the grafted tree is
\[
R_v=B_i(f)+\frac12R_++\frac12R_-.
\tag{3.1}
\]
The exact influence decomposition is
\[
I(f)=\alpha+\frac{a+b}{2},
\qquad j\le\alpha.
\tag{3.2}
\]

### Theorem 3.1 (hybrid propagation)

With \(D,M,\Phi\) defined in (0.1),
\[
\boxed{R_v\le\Phi(K_+,K_-)I(f).}
\tag{3.3}
\]

### Proof, route D: descendant-influence payment

Using the already-proved descendant estimate (1.1),
\[
R_v\le c_0j+\frac12(1+K_+)a+\frac12(1+K_-)b.
\]
Therefore any
\[
K\ge c_0,\qquad K\ge1+K_+,\qquad K\ge1+K_-
\]
gives, by (3.2), \(R_v\le KI(f)\). Thus \(D(K_+,K_-)\) is a valid certificate.

### Proof, route M: minor-child payment

Use (2.5). If \(a\le b\), then
\[
R_v\le C_\chi j+a+\frac12K_+a+\frac12K_-b.
\]
Put \(t=a/(a+b)\in[0,1/2]\). After paying the root term by \(K\alpha\), the coefficient required on \((a+b)/2\) is
\[
\frac{(K_++2)a+K_-b}{a+b}
=t(K_++2)+(1-t)K_-.
\]
As an affine function of \(t\in[0,1/2]\), its maximum is attained at an endpoint and equals
\[
\max\left\{K_-,1+\frac{K_++K_-}{2}\right\}.
\]
Thus for \(a\le b\), it suffices that
\[
K\ge C_\chi,\quad K\ge K_-,\quad
K\ge1+\frac{K_++K_-}{2}.
\]
The case \(b\le a\) is symmetric and adds \(K\ge K_+\). Therefore \(M(K_+,K_-)\) is also a valid certificate.

Both certificates hold for the same node and continuations, so their minimum \(\Phi\) is valid. QED.

### What changed versus the preceding run

The preceding descendant recursion always paid a full additive `+1` to the worse child constant. The new route M pays the minor child once and therefore uses the **average** of the two child constants. When one branch is already easy, the hard branch can continue for arbitrarily many levels without accumulating an unbounded constant. This is precisely the dependent-branch imbalance that the old depth payment could not exploit.

## 4. Decision-tree theorem for arbitrary quadratic twists

Let \(h:\mathbb F_2^n\to\{\pm1\}\) be computed by a physical decision tree \(T\). The tree may be adaptive and need not be balanced. Let \(Q\) be any polynomial of degree at most two on the same cube, and put
\[
f=(-1)^Qh.
\]
At every leaf of \(T\), the restricted value of \(h\) is constant. Therefore the restricted \(f\) is, up to global sign, a quadratic phase. By the prior NM13-02 quadratic rank theorem, that leaf has a full physical completion with hereditary allocation at most its total influence. Assign leaf label \(\kappa=1\), and propagate labels upward by \(\Phi\).

Repeated application of Theorem 3.1 proves:

### Theorem 4.1 (quadratic twist of a decision-tree core)

\[
\boxed{
\exists\ \text{a full physical restriction tree }\mathcal T
\text{ with }
R_{\mathcal T}((-1)^Qh)\le\kappa(T) I((-1)^Qh).
}
\tag{4.1}
\]
There is no Hamming-density assumption on \(h\), no restriction on the quadratic interaction graph of \(Q\), and no fresh-control variable.

This theorem directly instantiates the decision-tree-complexity replacement suggested by P03's newest finite-defect proof. It is complementary to P03's Hamming-cardinality theorem: structure of the defect sign, rather than the number of defect vertices, pays the branch recursion.

## 5. Two shape bounds and an exact nested-spine theorem

### Corollary 5.1 (height)

Since every child label is at least one,
\[
D(K_+,K_-)=1+\max\{K_+,K_-\}.
\]
Hence a tree of height \(d\) obeys
\[
\boxed{\kappa(T)\le d+1.}
\tag{5.1}
\]
This recovers, and does not worsen, the preceding bounded-depth theorem.

### Corollary 5.2 (leaf count)

Let \(L(T)\) be the number of leaves and put
\[
A:=C_\chi-\log_2 3=1.290076274193\ldots .
\]
Then
\[
\boxed{\kappa(T)\le A+\log_2L(T).}
\tag{5.2}
\]

**Proof.** For one leaf, \(1\le A\). For two leaves, direct use of route D gives \(\kappa=2<A+1\). Now let \(L=L_++L_-\ge3\) and assume the claim below the root. Route M gives
\[
\kappa(T)\le\max\left\{C_\chi,\kappa_+,\kappa_-,1+\frac{\kappa_++\kappa_-}{2}\right\}.
\]
The first term is at most \(A+\log_2L\) because \(L\ge3\). Each child term is at most the same quantity. For the average term,
\[
1+\frac{\kappa_++\kappa_-}{2}
\le1+A+\frac12\log_2(L_+L_-)
\le A+\log_2(L_++L_-),
\]
where the last inequality is exactly \(2\sqrt{L_+L_-}\le L_++L_-\). QED.

Thus
\[
\boxed{\kappa(T)\le\min\{d+1,A+\log_2L(T)\}.}
\tag{5.3}
\]
The exact recursion can be much better than either coarse envelope.

### Corollary 5.3 (nested-canalizing spine: uniform constant below 3)

Suppose every internal node has one child that is already a stopping leaf and one child continuing the spine. Let \(\kappa_d\) be the certificate for a spine with \(d\) internal nodes. Then
\[
\kappa_0=1,\qquad \kappa_1=2,\qquad \kappa_2=C_\chi,
\]
and for every \(d\ge2\),
\[
\kappa_{d+1}=\frac32+\frac12\kappa_d.
\]
Therefore
\[
\boxed{
\kappa_d=3-\frac{3-C_\chi}{2^{d-2}}<3
\quad(d\ge2).
}
\tag{5.4}
\]

**Proof.** At a spine node the two child labels are \(1\) and \(K\). Route D gives \(1+K\). Route M gives
\[
\max\left\{C_\chi,K,\frac32+\frac K2\right\}.
\]
Starting from \(K=1\), the first node is paid by D with constant two. The second has M-value \(C_\chi\). Once \(C_\chi\le K<3\), the term \(3/2+K/2\) is larger than both \(C_\chi\) and \(K\), but remains below three, while route D is larger. This gives the recurrence and its closed form. QED.

This is the main shape-sensitive gain: the depth can tend to infinity while the hereditary constant stays below three.

## 6. Concrete dense high-degree family: P03's decision-tree obstruction is genuinely bypassed

On \(k\) ordered bits define
\[
p_k(x)=x_1+x_1x_2+x_1x_2x_3+\cdots+x_1x_2\cdots x_k\pmod2,
\qquad
h_k=(-1)^{p_k}.
\tag{6.1}
\]
This has algebraic degree exactly \(k\). It satisfies the exact recursion
\[
p_k=x_1(1+p_{k-1}(x_2,\ldots,x_k)).
\tag{6.2}
\]
Hence querying \(x_1\) gives one constant child (when \(x_1=0\)) and one signed copy of \(h_{k-1}\) (when \(x_1=1\)). Thus \(h_k\) has a physical decision-tree spine of depth \(k\).

For **every** quadratic polynomial \(Q\) on these coordinates (and, by the same theorem, with arbitrary additional quadratic couplings to other coordinates), Theorem 4.1 and (5.4) give
\[
\boxed{
\mathcal A((-1)^Qh_k)<3
\quad\text{uniformly in }k.
}
\tag{6.3}
\]

This is not merely another sparse-defect instance. Let
\[
b_k:=\Pr[p_k=1].
\]
From (6.2),
\[
b_k=\frac12(1-b_{k-1}),\qquad b_0=0,
\]
so
\[
\boxed{
b_k=\frac13-\frac{(-1)^k}{3\,2^k}.}
\tag{6.4}
\]
Thus on the \(k\)-cube the Hamming defect set relative to the quadratic base \((-1)^Q\) has exact cardinality
\[
\boxed{|D_k|=\frac{2^k-(-1)^k}{3},}
\tag{6.5}
\]
a positive-density set asymptotic to one third of the whole cube.

P03's newest Hamming-cardinality theorem applies formally with \(t=|D_k|\), but its stated constant grows like \(12.04+\log_2 k\). The present hereditary certificate stays below three. The published part-symmetric theorem with singleton parts likewise gives a constant growing like \(12.04+\log_2k\). Hence the gain here is not finite coverage: it is a new all-dimensional structural payment for a dense, unbounded-degree, branch-asymmetric core under arbitrary quadratic twisting.

This is the promised application to P03's exact newest obstruction. Decision-tree complexity can replace raw Hamming cardinality **when the tree is shape-paid by (0.1)**, and nested dependent branches cost a bounded amount rather than one unit per level.

## 7. What this does and does not imply for FEI

The hereditary theorem above is self-contained modulo the previously proved/self-checked quadratic leaf theorem; the P03 local inequality was rederived in Section 2 rather than assumed.

P03's separately reported dependent-recombination theorem (1.3) would, if retained after later independent review, turn a full hereditary certificate \(R\le K I\) into
\[
H(\widehat f^{\,2})\le\left(K+\frac2{\ln2}\right)I(f).
\]
Therefore the nested-canalizing quadratic-twist family would satisfy the **PROJECT-CONDITIONAL** restricted estimate
\[
\boxed{
H(\widehat f^{\,2})
<\left(3+\frac2{\ln2}\right)I(f)
=5.8853900818\ldots I(f).
}
\tag{7.1}
\]
This is deliberately not promoted to an independently reviewed FEI theorem, and certainly not to full FEI.

### Failure / remaining obstruction

The hybrid recursion is **not** universally bounded. On a perfectly balanced decision tree whose two child certificates remain equal, both local payments incur an additive unit at the next level; \(\kappa\) grows linearly with balanced height (equivalently logarithmically with leaf count). Thus this run does not hide the original conjecture inside a notation change.

The remaining mechanism question is sharper: can a genuinely arbitrary Boolean core be restricted so that hard hereditary mass flows through sufficiently unbalanced branches, or can one find another conserved potential that pays simultaneous hard children without the `+1` average cost? That is the natural next attack. The edge-boundary-complexity alternative named by P03 remains untouched and complementary.

## 8. Current primary-source status

A bounded fresh public-source check on 20 September 2026 recovered:

- María José González, Paul MacManus, María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, submitted 29 May 2026 and updated 2 June 2026. Its abstract still states universal FEI as a conjecture; its stopping-tree/restriction framework says that a suitable restriction inequality would imply FEI and proves restricted classes, not a universal theorem.
- Peijie Li and Guangyue Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*, arXiv:2512.03117, submitted 2 December 2025. Its sharp general inequality still contains the additional coordinate-profile term \(\sum_i I_i(f)\ln(1/I_i(f))\), so it is not a universal \(CI(f)\) theorem.

A fresh September-2026 search did not recover a source-matching universal resolution. This bounded search is negative evidence only, not a worldwide priority or novelty certificate.

## 9. Executed sanity checks

Executed script:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T08-08-34+0300__check_hybrid_decision_tree.py`

Creation commit: `a1df7d03345e674579f2a63eb624412eb2ed8bef`.

Archived actual output:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T08-08-34+0300__hybrid_decision_tree_check.json`

Creation commit: `d87b72238ccc557d0c25f3813a673a6638a71ee0`.

The checker returned `PASS` and performed:

- exhaustive enumeration of all **6,918** ordered full-binary tree shapes with at most ten leaves, with zero violation of the height and proved leaf-count envelopes;
- exact verification (to floating evaluation of the displayed constants) of the closed spine recurrence through depth twelve;
- direct Walsh/Fourier computation for **all 2,196 quadratic twists** of the explicit nested core through dimension four;
- deterministic-seed tests of 300 dimension-five and 200 dimension-six quadratic twists.

The largest observed direct hereditary ratio through the exhaustive dimension-four twist scan was `1.8266230937148955`, below the theorem certificate. The largest numerical value of `R-kappa I` was `-0.5710683000068681`. These computations are sanity checks only; the all-dimensional claims rest on the proofs above.

## 10. ledger_delta

```yaml
ledger_delta:
  owner: NM13-02
  assignment: T01_Friedgut_Kalai_FEI_hereditary_entropy
  companion: P03
  parent_status_before: OPEN
  parent_status_after: OPEN
  universal_FEI_constant_before: UNKNOWN
  universal_FEI_constant_after: UNKNOWN
  substantive_gain:
    id: NM13-02-FEI-HYBRID-DT-01
    status: PROVED_SELF_CHECKED_PROJECT
    statement: "For any quadratic Q and any Boolean core h computed by a physical decision tree T, a full physical restriction tree for (-1)^Q h has hereditary allocation R <= kappa(T) I, where leaf kappa=1 and internal kappa is propagated by min{max(1/ln2,1+K+,1+K-), max(C_chi,K+,K-,1+(K++K-)/2)}."
    consequences:
      - "kappa(T) <= height(T)+1"
      - "kappa(T) <= C_chi-log2(3)+log2(leaves(T))"
      - "nested-canalizing spines have kappa<3 uniformly in depth"
      - "the dense high-degree core p_k=sum_{r<=k} prod_{s<=r} x_s, under arbitrary quadratic twist, has hereditary constant <3"
    fresh_variables: false
    full_FEI: false
    independent_audit: pending
  p03_newest_obstruction_addressed: "decision-tree complexity as a restriction-stable replacement for Hamming defect cardinality"
  preserved_restrictions_and_failures:
    - fresh_control_theorem_remains_restricted
    - pointwise_erasure_false
    - fixed_coefficient_affine_drift_retired
    - Han_absolute_overlap_selector_refuted
    - derivative_degree_scalar_schedule_refuted
    - blind_root_square_curvature_retired
  project_conditional_only:
    dependency: P03_paid_recombination
    consequence: "nested spine FEI constant < 3 + 2/ln2 = 5.8853900818..."
  checker_status: PASS
  checker_commit: a1df7d03345e674579f2a63eb624412eb2ed8bef
  output_commit: d87b72238ccc557d0c25f3813a673a6638a71ee0
  next_attack: "seek a branch-imbalance or boundary-flow potential that pays the balanced-hard-child case without a full additive unit; keep P03's edge-boundary-complexity route complementary"
```

**End of substantive run report.**
