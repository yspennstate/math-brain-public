Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not authenticated as GPT-6 at maximum.

# NM13-02 T01 — truncated minor-child load and hereditary allocation for one-point perturbations of quadratic phases

## Parent scope and mechanism delta

**Parent problem:** the Friedgut--Kalai Fourier entropy--influence conjecture on finite uniform cubes,
\[
H(\widehat f^2)\le C I(f)
\]
for one finite universal constant and every Boolean function.

**Parent-problem status before -> after:** **OPEN -> OPEN.**

**Universal finite upper bound for \(C_{\rm FEI}\): UNKNOWN -> UNKNOWN.**

The mathematical gain in this run is separate from that unchanged parent metric:

1. P03's newest arbitrary-child theorem leaves the residual minor-child load
   \[
   L_{\mathcal T}=\sum_v w_v\min\{I(f_v^+),I(f_v^-)\}.
   \]
   I prove an all-dimensional strengthening in which the residual is replaced by a **truncated minor-child load** supported only on low folded-influence queries:
   \[
   R_{\mathcal T}
   \le C_\chi J_{\mathcal T}+\widetilde L_{\mathcal T},
   \]
   where
   \[
   \widetilde L_{\mathcal T}
   =\sum_vw_v\min\left\{
      m_v,\,[h_2(j_v)-C_\chi j_v]_+
   \right\},
   \qquad
   m_v=\min\{I(f_v^+),I(f_v^-)\}.
   \]
   The residual is identically zero whenever \(j_v\ge\rho\), where \(\rho=0.3111084359\ldots\) is the unique solution in \((0,1/2)\) of \(h_2(\rho)=C_\chi\rho\).
2. Using that sharpening together with the preceding NM13-02 quadratic and character-child certificates, I prove a new hereditary theorem for an all-dimensional nonquadratic class: **every Boolean phase obtained by flipping one truth-table value of an arbitrary quadratic phase has a full physical restriction tree with**
   \[
   \boxed{R_{\mathcal T}(f)\le C_\chi I(f)},
   \qquad
   C_\chi=2+\frac1{\sqrt e\ln2}=2.8750387749\ldots .
   \]
3. This directly disposes of the concrete stress family proposed at the end of P03's newest proof: random one-point perturbations of bent phases are **not** counterexamples to bounded hereditary allocation. They lie in the theorem above. The raw minor-child term can still be very pessimistic; the new theorem avoids paying it on the high-folded-influence polar pivots.

This is **PARTIAL** progress. It does not settle unrestricted FEI. The FEI corollary using P03's separately reported recombination theorem remains PROJECT-CONDITIONAL pending later independent review.

## Compact handoff of prior NM13-02 mathematics

The following prior results remain in force and are used here without changing their scope.

- **Quadratic rank telescope:** for a quadratic phase \((-1)^q\) with polar rank \(r\), every full adaptive physical tree has hereditary allocation \(R=r/2\), hence \(R\le I\).
- **Exact influence budget / max-splicing:** local allocation certificates and branch-dependent continuation certificates combine with the maximum of their constants because queried influence plus weighted residual leaf influence is exactly the root influence.
- **Character-child theorem:** if one physical child is a signed character, then
  \[
  B_i(f):=H(Z_i\mid Z_{-i})\le C_\chi\operatorname{Inf}_i(f).
  \]
- The false pointwise erasure shortcut, fixed-coefficient drift rules, derivative-degree selector, and Han absolute-overlap criterion remain retired. No such lemma is revived below.

## Current dependency and exact live obstruction

The controlling directive is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`; LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

The newest P03 substantive report is
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22+0300__fei-minor-child-allocation.md`, blob `7e12f35a9c2fae61f3c63e8434a493762a0e8081`.
Its all-dimensional theorem is
\[
B_i(f)\le C_\chi j_i(f)+\min\{I(f^+),I(f^-)\},
\qquad
j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\tag{D1}
\]
Summed on a tree, P03 obtains
\[
R_{\mathcal T}\le C_\chi J_{\mathcal T}+L_{\mathcal T}.
\tag{D2}
\]
P03 explicitly identifies the remaining universal obstruction as controlling the recursive minor-child load, and proposes one-point perturbations of bent phases as a natural stress family.

The earlier P03 report
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`, reports the fresh-variable-free recombination estimate
\[
S_{\mathcal T}\le\frac2{\ln2}J_{\mathcal T}\le\frac2{\ln2}Q_{\mathcal T}.
\tag{D3}
\]
I use (D1) as a project dependency and do not take ownership of P03's proof. The restricted fresh-control results remain restricted and are not used to infer full FEI.

`POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem is being rediscovered.

### Fresh public-source status, 20 September 2026

A bounded fresh search recovered González--MacManus--Pereyra, arXiv:2606.00246 (submitted 29 May 2026), which still states universal FEI as a conjecture and develops stopping-tree/restriction sufficient conditions and restricted classes rather than a universal proof. Li--Han, arXiv:2512.03117 (2 December 2025), still has the additional coordinate-influence logarithmic term in its general inequality. Thus no source-matching universal finite FEI constant was recovered in this check. A bounded search is not a worldwide novelty certificate.

## 1. General theorem: truncate the minor-child load to low folded influence

Let \(Z\) be the spectral random set of \(f\), so
\[
\Pr(Z=S)=\widehat f(S)^2.
\]
For a physical coordinate \(i\), set
\[
B_i(f)=H(Z_i\mid Z_{-i}),
\quad
\delta_i=\operatorname{Inf}_i(f),
\quad
j_i=\min\{\delta_i,1-\delta_i\},
\quad
m_i=\min\{I(f^+),I(f^-)\}.
\]

### Theorem 1 (truncated minor-child payment)

For every Boolean \(f\) and every physical coordinate \(i\),
\[
\boxed{
B_i(f)
\le C_\chi j_i+\lambda_i,
\qquad
\lambda_i:=\min\{m_i,[h_2(j_i)-C_\chi j_i]_+\}.
}
\tag{1.1}
\]
Consequently every adaptive physical restriction tree satisfies
\[
\boxed{
R_{\mathcal T}(f)
\le C_\chi J_{\mathcal T}(f)+\widetilde L_{\mathcal T}(f),
}
\tag{1.2}
\]
with
\[
\boxed{
\widetilde L_{\mathcal T}(f)
:=\sum_{v\text{ internal}}w_v
\min\left\{
\min(I(f_v^+),I(f_v^-)),
[h_2(j_v)-C_\chi j_v]_+
\right\}.
}
\tag{1.3}
\]
In particular, if \(\rho\in(0,1/2)\) is the unique root of
\[
h_2(\rho)=C_\chi\rho,
\tag{1.4}
\]
then every node with \(j_v\ge\rho\) contributes **zero** to \(\widetilde L_{\mathcal T}\).
Numerically
\[
\rho=0.311108435929919\ldots .
\]

### Proof

Two independent upper bounds are available.

First, P03's arbitrary-child theorem (D1) gives
\[
B_i(f)\le C_\chi j_i+m_i.
\tag{1.5}
\]
Second, conditional entropy is at most marginal entropy:
\[
B_i(f)=H(Z_i\mid Z_{-i})\le H(Z_i).
\]
The spectral-bit marginal is
\[
\Pr(i\in Z)=\sum_{S\ni i}\widehat f(S)^2
=\operatorname{Inf}_i(f)=\delta_i,
\]
so
\[
B_i(f)\le h_2(\delta_i)=h_2(j_i).
\tag{1.6}
\]
Taking the smaller of (1.5) and (1.6) gives
\[
B_i(f)
\le C_\chi j_i+\min\{m_i,h_2(j_i)-C_\chi j_i\}
\]
whenever the last difference is nonnegative, while if it is negative then (1.6) already gives \(B_i(f)\le C_\chi j_i\). This is exactly (1.1). Summing with node weights proves (1.2)--(1.3).

Finally, for \(t\in(0,1)\),
\[
\frac{d}{dt}\frac{h_2(t)}t
=\frac{t h_2'(t)-h_2(t)}{t^2}
=\frac{\log_2(1-t)}{t^2}<0.
\]
Hence \(h_2(t)/t\) is strictly decreasing, so (1.4) has a unique solution and \(h_2(j)\le C_\chi j\) exactly for \(j\ge\rho\) on \((0,1/2]\). QED.

### Why this is not cosmetic

The raw \(L_{\mathcal T}\) cannot be bounded on arbitrary blind full trees. For the \(n\)-variable parity character, every local hereditary allocation is zero, yet if one expands all variables without using the character stopping certificate then at depth \(d\) the minor-child influence is \(n-d-1\). Hence
\[
L_{\mathcal T}=\sum_{d=0}^{n-2}(n-d-1)=\frac{n(n-1)}2,
\]
while \(I(f)=n\). Thus \(L_{\mathcal T}/I(f)=(n-1)/2\to\infty\) even though the true allocation is zero. The truncation (1.3) identifies exactly why this bookkeeping is spurious on many high-information splits: marginal entropy already pays the local bit before any child influence is charged.

## 2. One-point perturbations of quadratic phases

Work on \(\mathbb F_2^d\). Let
\[
\phi_q(x)=(-1)^{q(x)}
\]
for a quadratic polynomial \(q\), and choose one point \(a\in\mathbb F_2^d\). Define the one-point perturbation
\[
f(x)=\begin{cases}
-\phi_q(a),&x=a,\\
\phi_q(x),&x\ne a.
\end{cases}
\tag{2.1}
\]
Let \(M_q\) denote the symmetric zero-diagonal polar matrix of the quadratic part.

Under any physical restriction, exactly one branch contains the defect point. The other branch is a pure quadratic phase, while the defect branch is again a one-point perturbation of the restricted quadratic phase. This gives a canonical single live spine with quadratic stopping leaves.

### Lemma 2.1 (nonzero polar row has almost-half queried influence)

At a live defect node on \(d\) free variables, suppose row \(i\) of the current polar matrix is nonzero. Then
\[
\boxed{
\operatorname{Inf}_i(f)
=\frac12\pm2^{1-d},
\qquad
j_i(f)=\frac12-2^{1-d}.
}
\tag{2.2}
\]

**Proof.** For the unperturbed quadratic phase, the directional derivative
\[
q(x)+q(x+e_i)
\]
is a nonconstant affine function of the other \(d-1\) variables because the polar row is nonzero. Therefore exactly half of the \(2^{d-1}\) physical \(i\)-edges are disagreements. Flipping the sign at one vertex toggles the disagreement status of exactly the single \(i\)-edge incident to that vertex. Thus the number of disagreeing \(i\)-edges changes by \(\pm1\), proving (2.2). QED.

### Lemma 2.2 (all nonzero-polar pivots in dimension at least four are paid with no minor load)

If \(d\ge4\) in Lemma 2.1, then
\[
\boxed{B_i(f)\le C_\chi\operatorname{Inf}_i(f).}
\tag{2.3}
\]

**Proof.** By Lemma 2.1,
\[
j_i\ge\frac12-\frac18=\frac38.
\]
The monotonicity of \(h_2(t)/t\) gives
\[
\frac{h_2(j_i)}{j_i}
\le \frac{h_2(3/8)}{3/8}
=2.5451573411\ldots<C_\chi.
\]
Hence by marginal conditioning,
\[
B_i(f)\le h_2(j_i)\le C_\chi j_i\le C_\chi\operatorname{Inf}_i(f).
\]
Equivalently, the truncated residual \(\lambda_i\) from Theorem 1 vanishes. QED.

The only nontrivial small-dimensional polar pivot left is \(d=3\).

### Lemma 2.3 (exact three-variable polar pivot)

Let \(d=3\), let the current quadratic polar matrix be nonzero, and query a coordinate with nonzero polar row. For the one-point perturbation (2.1),
\[
\operatorname{Inf}_i(f)\in\left\{\frac14,\frac34\right\}
\]
and
\[
\boxed{
B_i(f)=\frac38+\frac58h_2\!\left(\frac1{10}\right).
}
\tag{2.4}
\]
Therefore
\[
\boxed{
\frac{B_i(f)}{\operatorname{Inf}_i(f)}
\le \frac32+\frac52h_2\!\left(\frac1{10}\right)
=2.67248898397\ldots<C_\chi.
}
\tag{2.5}
\]

**Proof.** A nonzero alternating \(3\times3\) matrix over \(\mathbb F_2\) has rank two, so the derivative in the queried direction is a nonconstant affine function and Lemma 2.1 gives the two possible influences.

After fixing the queried coordinate, both unperturbed children have the same quadratic part on two variables and differ by a nonconstant affine character. On two variables there are only two possibilities for the quadratic coefficient: zero or one. A pure two-variable phase with zero quadratic coefficient is an affine character, with squared Fourier law a point mass. A pure two-variable phase with nonzero quadratic coefficient is bent, with squared Fourier law uniform on the four frequencies.

Flipping one truth-table value toggles the unique degree-two ANF coefficient on two variables: the point-indicator polynomial has degree-two coefficient one. Consequently the defect child has the opposite type from the corresponding pure child. Thus, at this split, one child's squared Fourier law is a point mass and the other child's squared Fourier law is uniform on four frequencies.

In the unique fiber containing the point-mass Fourier frequency, the two child coefficient magnitudes are \(1\) and \(1/2\). Hence the parent fiber mass is
\[
q=\frac{1+1/4}{2}=\frac58,
\]
and the conditional spectral-bit probability is either \(1/10\) or \(9/10\), according to the relative sign. The entropy is the same in both cases. In each of the other three fibers, the magnitudes are \(0\) and \(1/2\), so the fiber mass is \(1/8\) and the conditional bit is fair. Summing the four contributions gives (2.4). Dividing by the smaller possible influence \(1/4\) gives (2.5). QED.

### Lemma 2.4 (rank-zero tail is character-canalizing)

If the restricted polar matrix is zero, the unperturbed phase is a signed character. At every subsequent physical query, the branch not containing the defect point is therefore a signed character. The preceding NM13-02 character-child theorem gives
\[
B_i(f)\le C_\chi\operatorname{Inf}_i(f)
\]
at every node of that tail.

For dimensions \(d\le2\), the one-point perturbation itself is still a degree-at-most-two Boolean phase, because the point indicator has degree at most two. Hence it is already covered by the quadratic rank theorem.

## 3. Main hereditary theorem

### Theorem 3 (one-point quadratic perturbations have constant hereditary allocation)

Every one-point perturbation (2.1) of every quadratic Boolean phase admits a full adaptive physical restriction tree \(\mathcal T\) satisfying
\[
\boxed{
R_{\mathcal T}(f)\le C_\chi I(f),
\qquad
C_\chi=2+\frac1{\sqrt e\ln2}<2.876.
}
\tag{3.1}
\]
Equivalently, the hereditary allocation functional obeys
\[
\boxed{\mathcal A(f)\le C_\chi.}
\tag{3.2}
\]

### Proof

Construct a single live defect spine.

- If the current polar matrix is nonzero and the live dimension is at least four, choose any coordinate whose polar row is nonzero. By Lemma 2.2 its local conditional allocation is at most \(C_\chi\) times the queried influence. Stop the branch not containing the defect; it is a pure quadratic phase and has a continuation certificate with hereditary constant \(1\) by the earlier quadratic rank theorem. Continue on the unique defect branch.
- If a nonzero polar matrix first reaches dimension three, query a nonzero polar row. Lemma 2.3 gives the same local \(C_\chi\) payment. Both children now live on two variables and are quadratic phases, so both may be completed with constant \(1\).
- If the polar matrix becomes zero first, use Lemma 2.4 down the remaining defect spine. Each local node has the \(C_\chi\) character-child payment, while the nondefect branch is a character and costs zero hereditary allocation. The final dimension-at-most-two defect leaf is quadratic.

This process must terminate because the physical dimension decreases at every live step; no claim that every nonzero-row deletion lowers polar rank is needed.

At every live internal node the local allocation is bounded by \(C_\chi\) times its actually queried influence. Every stopped nondefect branch has a continuation certificate of constant at most \(1<C_\chi\). Apply the previously proved exact influence-budget/max-splicing theorem. Queried influence and weighted residual leaf influence partition the root influence, so the grafted full tree has allocation at most the maximum continuation constant, namely \(C_\chi\). This proves (3.1)--(3.2). QED.

## 4. Direct application to P03's newest obstruction

P03's report ends by proposing **random one-point perturbations of bent phases** as a natural first test for whether every stopping-tree decomposition can suffer unbounded minor-branch depth/load.

A bent Boolean phase is a quadratic phase with nonsingular polar form, so it is a special case of Theorem 3. Therefore every such one-point perturbation satisfies
\[
\boxed{\mathcal A(f)\le C_\chi<2.876.}
\tag{4.1}
\]
This is all-dimensional and does not rely on finite verification.

More importantly, Theorem 1 explains why the raw P03 residual is misleading on this family. Along every nonzero-polar live pivot of dimension \(d\ge4\),
\[
j_i=\frac12-2^{1-d}\ge\frac38>\rho,
\]
so the improved residual \(\lambda_i\) is **exactly zero**, regardless of how large the minor child's total influence is. The last possible three-variable polar pivot is handled by the exact Lemma 2.3, and once the polar part vanishes the character-child theorem takes over. Thus the proposed stress family does not force recursive payment of minor-child influence at all.

This does not prove that \(\widetilde L_{\mathcal T}\) is universally bounded for every Boolean function. It narrows the live obstruction further:

> any genuine obstruction to this route must sustain many restriction nodes with **folded queried influence below \(\rho\approx0.3111\)** while simultaneously avoiding the existing quadratic, character-canalizing, symmetric, and other certified stopping classes.

That is strictly sharper than the previous requirement of merely having large minor-child influence.

### Conditional FEI consequence using P03's recombination theorem

If the separately reported P03 theorem (D3) is accepted as a project dependency, apply it to the full tree from Theorem 3. Since \(J_{\mathcal T}\le Q_{\mathcal T}\le I(f)\),
\[
H(f)=R_{\mathcal T}(f)+S_{\mathcal T}(f)
\le\left(C_\chi+\frac2{\ln2}\right)I(f)
=5.76042885669\ldots\,I(f).
\tag{4.2}
\]
This is **PROJECT-CONDITIONAL** and only for one-point perturbations of quadratic phases. It is not a universal FEI theorem and does not convert finite checks into a proof of full FEI.

## 5. Failed/retired directions preserved honestly

1. **Bound the raw minor-child load on arbitrary full trees:** impossible as a proof architecture. Parity already gives \(L/I=(n-1)/2\) on the blind full tree while true hereditary allocation is zero. This is a bookkeeping counterexample, not a counterexample to FEI or to carefully chosen stopping trees.
2. **Use only a marginal entropy envelope:** P03's one-defect family already shows that summing the marginal envelope can diverge logarithmically relative to influence. The marginal bound is used here only as a local cap to *truncate* P03's stronger arbitrary-child estimate, and only high-folded-influence nodes are discharged by it.
3. **Revive absolute Fourier overlap / fixed drift / derivative degree:** not used. Their recorded counterexamples remain intact.

## 6. Executed sanity checks

The new checker was actually executed before persistence:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T06-10-00+0300__check_quadratic_one_defect.py`

created at commit `dea74d3fe0597718d267f2b8493b436478d949ad`.

Archived output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T06-10-00+0300__quadratic_one_defect_check.out`

created at commit `b036d9c5da2c5eb0a0111b3f0be246bc457be418`.

The run output is `PASS` and records:

- \(\rho=0.311108435929919\ldots\);
- \(h_2(3/8)/(3/8)=2.545157341133240<C_\chi\);
- all **1152** three-variable rank-two polar/linear/defect/query cases have exactly the fiber pattern used in Lemma 2.3;
- exact three-variable value \(B=0.668122245993301\ldots\) and worst ratio \(2.672488983973203\ldots<C_\chi\);
- all 16 two-variable one-flip rank-two cases become affine characters;
- additional exhaustive nonzero-polar local checks for all polar edge masks through dimension five passed (`2, 18, 224, 4800` tested local pivots for dimensions 2--5 under the symmetry-reduced normalization).

The theorem is analytical; these checks are only sanity checks and do not substitute for the proof.

## 7. Next attack

The live residual is now the low-folded-influence part
\[
\widetilde L_{\mathcal T}
=\sum_{v:j_v<\rho}w_v
\min\{m_v,h_2(j_v)-C_\chi j_v\}.
\]
A genuinely new next step is to seek an **entropy-drop or spectral-concentration potential specifically on the region \(j<\rho\)**. High-\(j\) nodes no longer need minor-child payment. The most useful target would be a theorem showing that repeated low-\(j\) entries force rapid approach to a character/quadratic/symmetric stopping class, or else yield a source-valid family with unbounded \(\widetilde L/I\). This is narrower than P03's previous raw-\(L\) problem and avoids retesting bent one-point perturbations, which are now certified.

## ledger_delta

- `NM13-02-T01-TRUNCATED-MINOR-LOAD-01 = PROVED / ALL-DIMENSIONAL / SELF-CHECKED / FRESH-VARIABLE-FREE / INDEPENDENT-REVIEW-PENDING`.
- `NM13-02-T01-ONE-POINT-QUADRATIC-02 = PROVED HEREDITARY ALLOCATION R<=C_chi I / ALL-DIMENSIONAL / SELF-CHECKED / FULL-FEI-STILL-OPEN / INDEPENDENT-REVIEW-PENDING`.
- Universal FEI finite constant: `UNKNOWN -> UNKNOWN`.
- P03 raw residual `L_T` is sharpened, not declared solved: only the truncated low-\(j\) residual remains in this route.
- P03's proposed one-point-bent stress family is discharged as a counterexample candidate for hereditary allocation; it is not a counterexample to FEI.
- Preserve prior quadratic, character-child, max-splicing, symmetric stopping-class, fresh-control and false-lemma scopes exactly.
- No peer claim, historical report, root ledger, schedule, workflow, permission, public post, email, Drive object or paid compute was modified.

**End of immutable substantive report.**
