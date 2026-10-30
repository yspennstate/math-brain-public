# fleet03/B19 — selected co-pair I-projection payment after the correct tensor baseline

**Run:** `20260922T103024Z-b19-fei-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`  
**Assignment:** Terminal-to-KL conversion  
**Classification:** `ESSENTIAL_STEP_APPLIED / INTER_PATH_KL_BRIDGE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication/novelty status:** not assessed; this is a private source-bound research artifact.

## 0. Control transition and exact target

This invocation began from the older POS3 prompt, but the fresh owner control changed during the invocation. Revision `2026-09-22.3` redirects every existing B01--B20 worker in all four accounts to full FEI and explicitly suspends new POS3 work. The fleet03/B19 card therefore controls this run:

> Show that the full terminal criticality inequalities force a measurable nonlocal occurrence-dependence credit. Translate exact pair/support identities into conditional relative entropy with tensor baselines removed and prove nonreuse.

The exact partner is `fleet04/B19`. At the pre-publication snapshot no compatible FEI handoff yet existed at the new shared handoff path for that worker, so this run did not fabricate partner uptake or wait. It consumed the assignment-card source `fleet04/B18` below as the required completed other-account mathematical input and sends the result to the assigned recipient `fleet01/B20`.

The first missing global implication before this run was not merely positivity of pair mutual information. It was a source-valid conversion of the Path-C co-pair/hidden-curvature variables into the Path-B irreducible occurrence KL, with the tensor/conditioning baseline removed and without summing the same KL credit repeatedly over many pairs.

This report proves such a conversion. It **does not** yet prove that the resulting selected-pair credit is always large enough to close the terminal class.

## 1. Source-pinned premises actually used

### 1.1 Terminal critical core

Source: `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`.

In the character-centered gauge,
\[
q_i=\operatorname{Inf}_i(f)\le \tfrac12,
\qquad J=\sum_i q_i,
\qquad
\mathcal P=\sum_i\mathfrak j(q_i),
\qquad F=H-\mathcal P.
\]
A minimum-dimensional ratio obstruction may be chosen genuinely ratio-extremal and all-block critical. In particular the source proves the physical-block inequalities
\[
U_A\ge \rho D_A
\]
for every nonempty physical block in a ratio-\(\rho\) core and the exact co-singleton phase-support tax. Full FEI would follow from a finite-\(K\) proof of `ALL-BLOCK-TERMINAL(K) => F<=KJ`.

### 1.2 Co-pair/hidden-curvature identity

Source: `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`.

For distinct physical coordinates \(i,j\), in its fixed median-character gauge, let
\[
s_{ij}:=\Pr(i,j\in X)
\]
for the full Fourier spectral random set \(X\), let \(p_{ij}\) be derivative-support disagreement, \(o_{ij}\) opposite-sign overlap, and \(c_{i\leftarrow j}\ge0\) the singleton posterior crossing into row \(i\). The source proves
\[
\boxed{s_{ij}=\frac{p_{ij}}4+o_{ij}}
\tag{1.1}
\]
and, with the fleet04/B18 hidden variable,
\[
\boxed{\omega_{i\leftarrow j}
=p_{ij}-2c_{i\leftarrow j}+4o_{ij}
=4s_{ij}-2c_{i\leftarrow j}\ge0.}
\tag{1.2}
\]
It also proves that raw hidden curvature cannot be bounded by \(O(J)\) from all-block terminality plus tensor primitivity alone; exact tensor orientation is a real baseline and survives near-tensor surgery.

### 1.3 Other-account result consumed: hidden-curvature bank

Source: `yspennstate/math-open-problems@200e3fd37fe201f78d882ba8809414d201efb829`,
`proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`.

This is the completed **other-account** result applied here. It defines
\[
U_4=\sum_i(4+\mathfrak j'(q_i))\sum_{j\ne i}\omega_{i\leftarrow j}
\tag{1.3}
\]
and reduces the robust-row weighted-depth obstruction to the already-paid visible bank plus a small coefficient times this hidden bank. Its explicit unpaid issue is that raw \(U_4\) contains tensor orientation and therefore needs a tensor-centered or nonreusing payment.

### 1.4 Irreducible occurrence KL

Source: `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For a probability law \(P\) on nonempty subsets with occurrence marginals \(r_i\) and mean size \(\mu=\sum_i r_i\), the source constructs the unique maximum-entropy nonempty law \(Q_r\). If \(\mu>1\), the parameter \(c\in(0,1]\) is the unique positive solution of
\[
1-c=\prod_i(1-cr_i),
\tag{1.4}
\]
and \(Q_r\) is independent Bernoulli with probabilities \(cr_i\), conditioned on nonemptiness. The irreducible occurrence credit is
\[
\boxed{K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P).}
\tag{1.5}
\]
It is exactly the part of the Gibbs KL not payable by arbitrary original-coordinate first moments.

## 2. The correct full-law lift of the I-projection

Let \(f:\{-1,1\}^n\to\{-1,1\}\) be nonconstant in the fixed centered gauge used by the co-pair source. Let \(\pi\) be the **full** squared-Fourier law,
\[
\pi(S)=\widehat f(S)^2,
\qquad
v:=\Pr_\pi[X\ne\varnothing]=1-\widehat f(\varnothing)^2>0.
\tag{2.1}
\]
Then
\[
q_i=\Pr_\pi(i\in X),
\qquad
J=\sum_iq_i.
\tag{2.2}
\]
Condition on nonemptiness:
\[
P:=\pi(\cdot\mid X\ne\varnothing),
\qquad
r_i=\frac{q_i}{v},
\qquad
\mu=\frac Jv\ge1.
\tag{2.3}
\]
Let \(Q_r\) be the I-projection from (1.4)--(1.5). Define a law \(\bar Q\) on **all** subsets by restoring the exact empty mass of \(\pi\):
\[
\bar Q(\varnothing)=1-v,
\qquad
\bar Q(S)=vQ_r(S)\quad(S\ne\varnothing).
\tag{2.4}
\]

### Lemma 2.1 — lifted KL and the pair baseline

For \(\mu>1\),
\[
\boxed{D_{\rm KL,2}(\pi\Vert\bar Q)=vK_{\rm occ}.}
\tag{2.5}
\]
Moreover \(\bar Q\) has the same one-coordinate occurrence marginals \(q_i\) as \(\pi\), and for every distinct \(i,j\),
\[
\boxed{
\Pr_{\bar Q}(i,j\in X)
=b_{ij}:=\frac cv\,q_iq_j.
}
\tag{2.6}
\]
If \(\mu=1\), both \(P\) and \(Q_r\) are singleton-supported, so all pair atoms are zero; set \(b_{ij}=0\) and every pair statement below is trivial.

**Proof.** The empty atoms of \(\pi\) and \(\bar Q\) agree. For nonempty \(S\), \(\pi(S)=vP(S)\) and \(\bar Q(S)=vQ_r(S)\), hence
\[
D(\pi\Vert\bar Q)=vD(P\Vert Q_r)=vK_{\rm occ}.
\]
Under \(Q_r\), start from independent Bernoulli variables with probabilities \(t_i=cr_i\) and condition on a nonempty vector, whose probability is exactly \(c\). Therefore
\[
Q_r(i,j\in X)=\frac{t_it_j}{c}=cr_ir_j.
\]
Multiplying by \(v\) and using \(r_i=q_i/v\) gives (2.6). The one-coordinate calculation is the same: \(vQ_r(i\in X)=vr_i=q_i\). QED.

**Important correction to the naive tensor subtraction.** The Path-C note suggested starting from \(s_{ij}-q_iq_j\). The occurrence-I-projection shows that the exact reference seen by \(K_{\rm occ}\) is instead
\[
\boxed{s_{ij}-\frac cv q_iq_j.}
\tag{2.7}
\]
Only when \(c=v\) does this reduce to \(s_{ij}-q_iq_j\). This distinction is forced by the nonempty conditioning and is not optional bookkeeping.

## 3. Main theorem: exact selected-pair KL payment

Write binary KL in bits as
\[
d_2(a\Vert b)
=a\log_2\frac ab+(1-a)\log_2\frac{1-a}{1-b},
\tag{3.1}
\]
with the standard boundary conventions.

Let \(\alpha=(\alpha_{ij})_{i\ne j}\) be **any probability distribution on ordered physical pairs**, chosen as a deterministic function of the current Boolean state if desired, but sampled independently of the Fourier set \(X\).

### Theorem 3.1 — nonreused selected-pair occurrence credit

For every nonconstant Boolean \(f\) as above,
\[
\boxed{
vK_{\rm occ}
\ge
\sum_{i\ne j}\alpha_{ij}
\,d_2\!\left(s_{ij}\middle\Vert b_{ij}\right),
\qquad
b_{ij}=\frac cv q_iq_j.
}
\tag{3.2}
\]
Combining with the exact co-pair identity (1.2), define
\[
\Psi_b(\omega)
:=
\begin{cases}
 d_2(\omega/4\Vert b),&\omega>4b,\\
 0,&\omega\le4b.
\end{cases}
\tag{3.3}
\]
Then
\[
\boxed{
vK_{\rm occ}
\ge
\sum_{i\ne j}\alpha_{ij}\,
\Psi_{b_{ij}}(\omega_{i\leftarrow j}).
}
\tag{3.4}
\]
In particular, by Pinsker in bits,
\[
\boxed{
vK_{\rm occ}
\ge
\frac1{8\ln2}
\sum_{i\ne j}\alpha_{ij}
\bigl(\omega_{i\leftarrow j}-4b_{ij}\bigr)_+^2.
}
\tag{3.5}
\]
The exact logarithmic bound (3.4), not the quadratic corollary (3.5), is the principal statement; it retains rare-event logarithms.

### Proof

Introduce an auxiliary ordered-pair label \(Z=(I,J)\sim\alpha\), sampled independently of \(X\). Compare
\[
\alpha\otimes\pi
\quad\text{and}\quad
\alpha\otimes\bar Q.
\]
Because the same selector \(\alpha\) is used on both sides,
\[
D(\alpha\otimes\pi\Vert\alpha\otimes\bar Q)
=D(\pi\Vert\bar Q)=vK_{\rm occ}.
\tag{3.6}
\]
Apply the deterministic channel
\[
(Z,X)\longmapsto
\left(Z,\mathbf 1_{\{I,J\}\subseteq X}\right).
\]
Data processing gives
\[
vK_{\rm occ}
\ge
\sum_{i\ne j}\alpha_{ij}
 d_2(s_{ij}\Vert b_{ij}),
\]
which proves (3.2).

Now (1.2) and \(c_{i\leftarrow j}\ge0\) imply
\[
s_{ij}=\frac14\omega_{i\leftarrow j}
+\frac12c_{i\leftarrow j}
\ge\frac14\omega_{i\leftarrow j}.
\tag{3.7}
\]
If \(\omega_{i\leftarrow j}>4b_{ij}\), then both \(s_{ij}\) and \(\omega_{i\leftarrow j}/4\) lie strictly above \(b_{ij}\). For fixed \(b\), the function \(a\mapsto d_2(a\Vert b)\) is increasing on \([b,1]\), hence
\[
d_2(s_{ij}\Vert b_{ij})
\ge d_2(\omega_{i\leftarrow j}/4\Vert b_{ij}).
\]
If \(\omega\le4b\), the right side of (3.3) is zero. Summing proves (3.4).

Finally, binary Pinsker in base two gives
\[
d_2(s\Vert b)\ge\frac2{\ln2}(s-b)^2.
\]
When \(\omega>4b\), (3.7) gives
\[
s-b\ge\frac14(\omega-4b),
\]
which yields (3.5). QED.

## 4. Why this is a genuine nonreuse statement

It would be invalid to write
\[
K_{\rm occ}\ge\sum_{i\ne j}d_2(s_{ij}\Vert b_{ij})
\]
without further structure: the same global dependence can appear in many pair projections. The selector \(Z\) avoids that mistake. Equation (3.2) is one application of data processing to **one randomized observed pair**. The right side is an average under a single selector, not a fictitious additive bank of all pair marginals.

Equivalently, for any nonnegative deterministic weights \(\lambda_{ij}\), \(\Lambda=\sum\lambda_{ij}>0\), choosing \(\alpha_{ij}=\lambda_{ij}/\Lambda\) gives the exact weighted form
\[
\boxed{
\sum_{i\ne j}\lambda_{ij}
 d_2(s_{ij}\Vert b_{ij})
\le \Lambda\,vK_{\rm occ}.
}
\tag{4.1}
\]
The normalization \(\Lambda\) is essential. Removing it would reintroduce repeated spending.

Thus a realizable Path-C stopping rule is now allowed to choose **one pair** according to any state-dependent selector and charge its tensor-renormalized hidden-curvature excess to the canonical Path-B occurrence KL without reuse.

## 5. Application to the hidden-curvature bank

By (1.2), each directed hidden atom satisfies
\[
\omega_{i\leftarrow j}
\le4s_{ij}.
\]
The correct I-projection baseline is \(4b_{ij}=4(c/v)q_iq_j\). Therefore
\[
\boxed{
\omega_{i\leftarrow j}
\le 4b_{ij}
+\bigl(\omega_{i\leftarrow j}-4b_{ij}\bigr)_+.
}
\tag{5.1}
\]
Consequently the raw bank (1.3) splits into
\[
U_4
\le
4\sum_i(4+\mathfrak j'(q_i))
  \sum_{j\ne i}b_{ij}
+
\sum_i(4+\mathfrak j'(q_i))
  \sum_{j\ne i}(\omega_{i\leftarrow j}-4b_{ij})_+.
\tag{5.2}
\]
The first term is the **conditional-product/tensor baseline**. It is not dependence credit and must not be charged to \(K_{\rm occ}\). The second is genuine positive excess above that baseline. Theorem 3.1 supplies an exact logarithmic KL payment for any single-pair selector applied to that excess.

This resolves one specific ambiguity in the previous Path-C state: raw orientation and irreducible dependence are now separated by the I-projection itself rather than by the ad hoc subtraction \(q_iq_j\).

## 6. Sharp regression: a tensor-bent Boolean source has raw orientation but zero occurrence KL

To verify that the baseline subtraction is necessary, take the two-bit Boolean bent gate
\[
g(a,b)=(-1)^{ab},\qquad a,b\in\{0,1\},
\]
and the four-bit tensor
\[
f(a,b,c,d)=g(a,b)g(c,d).
\tag{6.1}
\]
All sixteen Walsh coefficients have squared magnitude \(1/16\). Therefore
\[
v=15/16,
\qquad q_i=1/2,
\qquad r_i=8/15,
\qquad c=15/16,
\tag{6.2}
\]
and the conditional nonempty spectral law is exactly uniform on the fifteen nonempty subsets, i.e. \(P=Q_r\). Hence
\[
\boxed{K_{\rm occ}=0.}
\tag{6.3}
\]
For a cross-factor pair, say \(i=1,j=3\),
\[
s_{13}=1/4,
\qquad b_{13}=(c/v)q_1q_3=1/4.
\tag{6.4}
\]
The co-pair tensor formula gives \(p_{13}=0\), \(o_{13}=q_1q_3=1/4\), \(c_{1\leftarrow3}=0\), hence
\[
\omega_{1\leftarrow3}=1=4b_{13}.
\tag{6.5}
\]
So raw hidden orientation is positive while the irreducible occurrence KL is exactly zero; the renormalized excess is exactly zero. Any theorem trying to pay raw \(\omega\) directly from \(K_{\rm occ}\) is false even on this elementary genuine Boolean tensor. This regression is not a counterexample to FEI and is not a ratio-critical terminal core.

The accompanying standard-library certificate recomputes the Walsh squares and the exact rational values in (6.2)--(6.4). It is only a regression check; Theorem 3.1 is analytic.

## 7. What this does and does not close

### New applied inference

The two paths now share a proved source-valid quantity:
\[
\boxed{
\text{positive hidden-curvature excess above }
4(c/v)q_iq_j
\quad\Longrightarrow\quad
\text{exact binary occurrence-KL credit}.
}
\]
The selector version (3.4) proves nonreuse for one randomized physical pair and retains the rare-event logarithm. This is stronger and more faithful than using pair mutual information alone or an unweighted squared convolution norm.

### Remaining first global implication

The full fleet03/B19 target is **not yet closed**. What remains is a realizable terminal selector theorem:

> **TERMINAL-SELECTOR-TO-KL.** For every genuine ratio-critical core in the uncovered robust/small-row branch, construct a state-dependent probability law \(\alpha\) on physical ordered pairs such that the exact selected-pair charge
> \[
> \sum_{i\ne j}\alpha_{ij}\Psi_{b_{ij}}(\omega_{i\leftarrow j})
> \]
> controls, with one dimension-independent constant and the correct physical reach probabilities, the trigger/entropy deficit that still has to be paid. The remaining baseline term in (5.2) must be absorbed by tensor-centered additivity/criticality or cause an affordable block; it cannot be charged again to \(K_{\rm occ}\).

This is now narrower than “pay \(U_4\)” and excludes the near-tensor false route by construction. If the selector theorem holds, the Path-C stopping proof can spend an actual Path-B information currency without pairwise double counting. If it fails, the failure must exhibit a ratio-critical Boolean core for which the terminal deficit lives entirely in the I-projection baseline or in selected-pair KL that is too sparse at every realizable scale.

## 8. Outcome

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

The run proves an exact inter-path bridge and identifies the correct conditional-product pair baseline \((c/v)q_iq_j\). It does **not** claim FEI, a bound on total raw \(U_4\), or an additive sum of all pair KLs. The exact next recipient is `fleet01/B20`; the designated partner `fleet04/B19` had no compatible completed FEI handoff at the checked snapshot, so no partner result is invented.
