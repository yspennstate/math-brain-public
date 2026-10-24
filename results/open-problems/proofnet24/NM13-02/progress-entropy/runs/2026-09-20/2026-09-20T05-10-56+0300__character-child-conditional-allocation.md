Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not authenticated as GPT-6 at maximum.

# NM13-02 T01 — character-child conditional allocation repairs P03's one-defect marginalization obstruction

## Scope and parent metric

**Parent problem:** Friedgut--Kalai Fourier entropy--influence (FEI) conjecture on finite uniform cubes,
\[
H(\widehat f^2)\le C I(f)
\]
for one finite universal constant and every Boolean function.

**Parent-problem status before -> after:** **OPEN -> OPEN.**

**Universal finite upper bound for \(C_{\rm FEI}\): UNKNOWN -> UNKNOWN.**

**Demonstrated mechanism gain:** a new all-dimensional local hereditary-allocation theorem is proved for every physical split having a character child. If one restriction at coordinate \(i\) is a signed character on the remaining variables, then the true spectral conditional entropy obeys
\[
B_i(f):=H(Z_i\mid Z_{-i})\le C_\chi\,\operatorname{Inf}_i(f),
\qquad
C_\chi:=2+\frac1{\sqrt e\,\ln2}=2.8750387749\ldots .
\]
The bound is obtained from an exact formula depending only on the queried influence. It is hereditary under restriction and combines with the preceding NM13-02 max-splicing theorem. This gives \(R_{\mathcal T}\le C_\chi I\) for character-canalizing restriction spines, and in particular repairs the precise one-defect family on which P03's derivative-degree and marginal-entropy surrogates diverge.

This is **PARTIAL** progress. It is not a proof of full FEI, and the numerical evidence for the sharp character-child constant is not promoted to a theorem.

## Compact handoff from preceding NM13-02 work

Two prior T01 results are preserved unchanged.

1. **Quadratic rank telescope.** For every quadratic phase \(f=(-1)^q\), if the alternating polar matrix has rank \(r\), then the squared Fourier law is uniform on an affine \(r\)-flat, every physical deletion has exact conditional allocation \(B_i=(r-r_i)/2\), and every full adaptive tree has \(R_{\mathcal T}=r/2\). Hence \(\mathcal A(f)=r/(2I(f))\le1\).
2. **Exact influence budget and max-splicing.** For every partial physical restriction tree \(\mathcal T_0\), queried influence plus weighted residual leaf influence equals the root influence exactly. Consequently branch-dependent continuation certificates combine by the maximum of their constants, not their sum. The same run transferred the known symmetric-function FEI theorem into hereditary allocation on the restriction-closed symmetric class.

No old false pointwise-erasure, resolvent, absolute-overlap, fixed-affine-drift, or derivative-degree scheduling lemma is revived here.

## Current dependency and source status

The current LIVE20 directive `operations/PROGRESS20_2026-09-20.md` assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

P03's newest substantive report is
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T04-29-36+0300__fei-one-defect-marginalization-obstruction.md`.
It proves that the one-defect family
\[
f_n(0)=-1,\qquad f_n(x)=+1\ (x\ne0)
\]
forces the preceding weighted derivative-degree charge to satisfy
\[
\inf_{\mathcal T}\frac{D_{\mathcal T}^{\deg}(f_n)}{I(f_n)}=\frac{n-1}{2}\to\infty,
\]
and likewise makes the tree marginal spectral-bit envelope diverge. At the same time its exact true hereditary allocation stays bounded and tends to \(2I(f_n)\). Therefore the live obstruction is specifically the lossy replacement
\[
H(Z_i\mid Z_{-i})\le H(Z_i)=h_2(\operatorname{Inf}_i),
\]
not dependent-branch recombination. The present run attacks exactly that gap, without taking ownership of P03's recombination theorem.

Fresh public-source check on 20 September 2026:

- Friedgut--Kalai (Proc. AMS 124 (1996), 2993--3002) is the historical source attribution for FEI.
- González--MacManus--Pereyra, arXiv:2606.00246 (submitted 29 May 2026, updated 2 June 2026), still presents universal FEI as a conjecture and gives a stopping-tree/restriction sufficient framework plus restricted classes, not a universal proof.
- Xiao Han, *Combinatorica* 45 (2025), proves a general entropy bound with an additional influence-profile logarithmic term.
- Li--Han, arXiv:2512.03117 (December 2025), sharpens that general inequality to constants 1 in its normalization, but the \(\sum_i I_i\log(1/I_i)\) term remains; it is not full FEI.

`POSTED.md` was checked for exact-scope exclusions. No posted unrestricted Boolean FEI theorem is being rediscovered. Restricted fresh-control results remain restricted and are not used as universal FEI.

## 1. Exact character-child formula

Let \(f:\{-1,1\}^{\{i\}\cup V}\to\{-1,1\}\). Let \(f^+,f^-\) be its two physical restrictions at coordinate \(i\), and let \(Z\) be the spectral random subset with law \(\widehat f(S)^2\).

### Theorem 1 (character-child conditional allocation)

Assume one child, say \(f^+\), is a signed character on the remaining variables:
\[
f^+(y)=\varepsilon\chi_A(y).
\]
Put
\[
\delta:=\operatorname{Inf}_i(f)=\Pr_y[f^+(y)\ne f^-(y)].
\]
Then
\[
\boxed{
B_i(f)=\Psi(\delta)
:=2\delta(1-\delta)
+q\,h_2\!\left(\frac{\delta^2}{q}\right),
\qquad
q=(1-\delta)^2+\delta^2.
}
\tag{1.1}
\]
In particular,
\[
\boxed{
B_i(f)\le C_\chi\,\delta,
\qquad
C_\chi:=2+\frac1{\sqrt e\,\ln2}<2.876.
}
\tag{1.2}
\]

### Proof of the exact formula

Multiply the whole function by \(\varepsilon\chi_A(y)\). This preserves \(\operatorname{Inf}_i\). In Fourier space it only translates the \(V\)-part of every spectral set by symmetric difference with \(A\), so it preserves \(H(Z_i\mid Z_V)\). We may therefore assume
\[
f^+\equiv1,
\qquad
f^-=g.
\]
Let
\[
\mu=\mathbb E g=1-2\delta.
\]
For \(T\subseteq V\), the two Fourier coefficients in the fiber above \(T\) are
\[
\widehat f(T)=\frac{1_{T=\varnothing}+\widehat g(T)}2,
\qquad
\widehat f(T\cup\{i\})=\frac{1_{T=\varnothing}-\widehat g(T)}2.
\tag{1.3}
\]
If \(T\ne\varnothing\), the two squared masses are equal, both \(\widehat g(T)^2/4\). Hence that fiber has conditional spectral bit entropy one, weighted by total fiber mass \(\widehat g(T)^2/2\). Summing these fibers and using Parseval gives
\[
\frac12\sum_{T\ne\varnothing}\widehat g(T)^2
=\frac{1-\mu^2}{2}
=2\delta(1-\delta).
\tag{1.4}
\]
For \(T=\varnothing\), the two masses are
\[
\frac{(1+\mu)^2}{4}=(1-\delta)^2,
\qquad
\frac{(1-\mu)^2}{4}=\delta^2.
\tag{1.5}
\]
Their total is \(q=(1-\delta)^2+\delta^2\), and their conditional entropy contribution is
\[
q\,h_2\!\left(\frac{\delta^2}{q}\right).
\]
Adding (1.4) and (1.5) proves (1.1). QED.

## 2. Universal analytic payment below 2.876

We use only the elementary binary-entropy estimate
\[
h_2(t)\le t\log_2\frac e t,
\qquad 0<t\le1.
\tag{2.1}
\]
Indeed
\[
(1-t)\log_2\frac1{1-t}
=\frac{(1-t)(-\ln(1-t))}{\ln2}
\le\frac{t}{\ln2}.
\]
Apply (2.1) to the exceptional fiber in (1.1): since \(q\le1\),
\[
q h_2(\delta^2/q)
\le \delta^2\log_2\frac{e q}{\delta^2}
\le \delta^2\log_2\frac e{\delta^2}.
\tag{2.2}
\]
Thus for \(0<\delta\le1\),
\[
\frac{B_i(f)}\delta
\le
U(\delta):=
2(1-\delta)+\delta\log_2\frac e{\delta^2}.
\tag{2.3}
\]
A direct derivative computation gives
\[
U'(\delta)
=-2+\log_2\frac e{\delta^2}-\frac2{\ln2},
\qquad
U''(\delta)=-\frac2{\delta\ln2}<0.
\]
Hence the unique maximizer is
\[
\delta_0=\frac1{2\sqrt e},
\]
and
\[
\max_{0<\delta\le1}U(\delta)
=2+\frac1{\sqrt e\,\ln2}
=C_\chi.
\]
The endpoint \(\delta=0\) has \(B_i=0\) by continuity. This proves (1.2). QED.

The constant \(C_\chi\) is a clean proved bound, not claimed sharp. Numerical maximization of the exact function \(\Psi(\delta)/\delta\) gives about `2.697376955` near \(\delta=0.199435\); this is sanity-check evidence only.

## 3. Hereditary splicing for character-canalizing branches

A signed character has a deterministic squared Fourier law. Therefore every physical query on a character restriction has \(B_j=0\); it can be completed to a full physical tree at zero hereditary allocation cost.

### Theorem 2 (character-canalizing max-splicing)

Let \(\mathcal T_0\) be a finite adaptive physical restriction tree such that at every internal node \(v\), one of the two children created by querying \(i(v)\) is a signed character of the remaining free variables. Allow the other branch to continue adaptively. Suppose every terminal non-character leaf \(\ell\) has a branch-dependent continuation certificate
\[
R_{\mathcal U_\ell}(f_\ell)\le K_\ell I(f_\ell).
\]
Then the grafted full tree satisfies
\[
\boxed{
R_{\rm graft}(f)
\le
\max\left\{C_\chi,\sup_\ell K_\ell\right\}I(f).
}
\tag{3.1}
\]

### Proof

At every internal node Theorem 1 gives
\[
B_{i(v)}(f_v)\le C_\chi\operatorname{Inf}_{i(v)}(f_v).
\]
Character children have continuation constant zero. Apply the exact partial-tree influence budget and branch-dependent max-splicing theorem proved in the preceding NM13-02 run. Queried influence and weighted residual leaf influence partition \(I(f)\), so the largest coefficient among \(C_\chi\) and the terminal continuation constants pays the entire grafted allocation. QED.

Two useful special cases are immediate.

1. A fully character-canalizing spine has \(R_{\mathcal T}\le C_\chi I(f)\).
2. If the unique surviving non-character branch eventually reaches a quadratic phase, the preceding quadratic theorem gives leaf constant 1, hence the whole hybrid still has \(R\le C_\chi I\).

This is a genuine hereditary closure operation: different mechanisms are allowed after dependent physical branches, and no fresh control coordinate is introduced.

## 4. Application to P03's exact newest obstruction

For the one-defect family \(f_n\), every physical query at the live restriction \(f_m\) has one constant child and one child equal to \(f_{m-1}\). Thus every full adaptive tree is character-canalizing in the sense of Theorem 2. Consequently
\[
\boxed{
R_{\mathcal T}(f_n)\le C_\chi I(f_n)<2.876\,I(f_n)
\quad\text{for every full physical tree.}
}
\tag{4.1}
\]
This strengthens the `<4I` bound recorded in P03's newest obstruction report and proves it by a reusable local theorem rather than a family-specific summation.

In fact, with
\[
p_m=2^{1-m},
\]
Theorem 1 gives the exact local payment \(B_i(f_m)=\Psi(p_m)\). Since the unique live node with restriction \(f_m\) has weight \(2^{-(n-m)}\), and
\[
2^{-(n-m)}p_m=2^{1-n},
\]
we get the exact tree ratio
\[
\boxed{
\frac{R_{\mathcal T}(f_n)}{I(f_n)}
=\frac1n\sum_{m=2}^n\frac{\Psi(2^{1-m})}{2^{1-m}}.
}
\tag{4.2}
\]
Because \(\Psi(\delta)/\delta\to2\) as \(\delta\downarrow0\), Cesaro convergence gives
\[
\frac{R_{\mathcal T}(f_n)}{I(f_n)}\to2,
\]
recovering P03's asymptotic value while adding the uniform all-\(n\) bound (4.1).

The contrast with P03's failed surrogates is now explicit:
\[
\frac{D_{\mathcal T}^{\deg}(f_n)}{I(f_n)}=\frac{n-1}{2}\to\infty,
\]
and its marginal spectral-bit envelope also diverges, but the true conditional allocation has a uniform local payment below `2.876`.

**What changed conceptually:** on a character-child split, every nonexceptional Fourier fiber has perfectly balanced membership masses, while the only exceptional fiber has mass ratio determined by \(\delta\) itself. The spectral side information \(Z_{-i}\) therefore removes the logarithmic marginal-entropy loss that doomed the derivative-degree route. No absolute-overlap criterion is required.

This directly addresses the precise newest P03 obstruction. It does **not** show that an arbitrary Boolean split has such a fiber structure.

## 5. Relation to full FEI and current P03 recombination theorem

The new theorem is self-contained at the hereditary-allocation level. P03 separately reports the all-dimensional tree recombination estimate
\[
S_{\mathcal T}\le\frac2{\ln2}Q_{\mathcal T}.
\]
If that internal theorem is accepted as a project dependency, then a full character-canalizing tree gives the restricted FEI estimate
\[
H(f)\le\left(C_\chi+\frac2{\ln2}\right)I(f)
<5.761 I(f).
\]
This corollary is **PROJECT-CONDITIONAL on P03's reported theorem pending later independent review**; it is not presented as a new independent proof of P03's claim, and it remains a restricted class result rather than full FEI.

The parent universal problem is unchanged. The missing step is to find an analog of Theorem 1 for sufficiently general non-character children, or an aggregate tree argument that recovers the lost conditional information without reducing to the false marginal envelope.

## 6. Failed extension in this run

I tried to replace the character child by an arbitrary small-complexity child using a fiberwise bound. This does not close at the pointwise level. If the two child Fourier coefficients in one fiber are \(u,v\), then the membership mass is proportional to \((u-v)^2\), while the conditional entropy of that fiber can carry an additional logarithm when \(u\approx v\). Thus no uniform pointwise estimate of the form
\[
\text{fiber conditional entropy}\le C\,(u-v)^2
\]
can hold. The character theorem succeeds because all but one fibers have one child coefficient exactly zero after twisting, and the remaining exceptional fiber is globally tied to the same disagreement probability \(\delta\). A broader theorem must aggregate Boolean constraints across fibers rather than bound each overlap fiber separately.

No claim is made here for general Fourier-sparse children.

## 7. Executed sanity check

Executed script:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T05-10-56+0300__check_character_child_allocation.py`
created at commit `57cd9ed9b3ccc2e596344b911dae913c8bf8cea4`.

Archived actual output:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T05-10-56+0300__character_child_allocation_check.json`
created at commit `fb88fb7626c1f79ced68066d87825a8e1d0c0bf4`.

The run returned `PASS`. It exhaustively checked every opposite Boolean branch and every character child for up to three remaining variables (2122 cases), with zero floating discrepancy between direct Walsh computation and formula (1.1). It also scanned 199999 values of \(\delta\), finding exact-ratio maximum about `2.69737695496105` near `0.199435`, below the proved analytic constant. For the one-defect tree it reproduced \(R/I=2.0429732414\) at \(n=10\), `2.0235764981` at \(n=20\), and `2.0047160901` at \(n=100\), while P03's derivative-degree ratio grows to `49.5` at \(n=100\).

The checker supports the algebra but is not the proof; the theorem arguments are above.

## 8. Residual obstruction and next attack

The next useful generalization is **not** another derivative-degree or marginal-entropy scheduler. The natural target is a two-component split theorem where one child is not a character but has a certified hereditary spectral decomposition, and where the exceptional overlap fibers are paid in aggregate by the exact influence budget. A concrete first case is a character-canalizing prefix ending in a quadratic core (already covered by max-splicing), followed by the first genuinely new case: one child quadratic and the other arbitrary. The quadratic child's affine-flat spectrum may permit a rank-indexed grouping of overlap fibers, replacing the failed pointwise comparison by a coset aggregate.

If that quadratic-child aggregation fails, the next materially different route is an information-theoretic lower bound on the mutual information
\[
I(Z_i;Z_{-i})=h_2(\operatorname{Inf}_i)-B_i
\]
using the physical disagreement set, rather than any absolute Fourier-overlap surrogate already refuted by shifted thresholds.

## ledger_delta

```yaml
slot: NM13-02
assignment: T01_FEI_hereditary_entropy_recombination
parent_problem: universal_Fourier_entropy_influence
parent_status_before: OPEN
parent_status_after: OPEN
parent_metric: finite_universal_upper_bound_C_FEI
parent_metric_before: UNKNOWN
parent_metric_after: UNKNOWN
mechanism_gain:
  theorem: character_child_conditional_allocation
  statement: B_i(f) <= (2 + 1/(sqrt(e) ln 2)) Inf_i(f) whenever one physical child is a signed character
  exact_formula: B_i = 2 delta(1-delta) + ((1-delta)^2+delta^2) h2(delta^2/((1-delta)^2+delta^2))
  hereditary_transfer: character-canalizing max-splicing with arbitrary certified terminal continuations
application:
  target: P03_one_defect_marginalization_obstruction
  previous_true_allocation_bound: <4 I and asymptotic 2 I
  new_uniform_bound: <2.876 I for every full tree
  exact_ratio_formula: (1/n) sum_{m=2}^n Psi(2^(1-m))/2^(1-m)
  p03_failed_surrogate_preserved: derivative-degree and marginal-entropy charges diverge like (n-1)/2
status: PARTIAL
full_FEI_claimed: false
restricted_fresh_control_promoted: false
false_lemmas_revived: false
p03_peer_claim_taken_over: false
conditional_dependency:
  p03_paid_recombination: pending_later_independent_review
artifacts:
  checker: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T05-10-56+0300__check_character_child_allocation.py
  output: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T05-10-56+0300__character_child_allocation_check.json
next_attack: quadratic-child affine-coset aggregate conditional-entropy payment
```
