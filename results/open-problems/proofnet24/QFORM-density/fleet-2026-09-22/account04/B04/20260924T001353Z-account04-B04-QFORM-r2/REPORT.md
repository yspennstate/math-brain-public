SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B04, 2026-09-24T00:13:53Z.
attacking: downshift a high fourth-volume carrier row to a strict entropy-weighted third-volume law, or force a quantitative double-anchor certificate on the same original-coordinate block.

# QFORM-HIGH-CARRIER-ANCHORED-DOWNSHIFT-v1

Programme: \(\texttt{QFORM-DENSITY-3EIG-20260922}\)  
Run: \(\texttt{20260924T001353Z-account04-B04-QFORM-r2}\)  
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The full universal conjecture is not proved here. The new result attacks the first branch left by the preceding account04/B04 nested-anchor payment: a physical fourth-volume carrier row with leverage \(>1/25\). It applies the completed account01/B04 entropy-weighted third-volume theorem to an actual probability law on physical minors.

## 1. Source-pinned input

The analytic input is account01/B04's theorem
\(\texttt{QFORM-ENTROPY-WEIGHTED-THREE-VOLUME-v1}\), pinned at

- \(\texttt{math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127}\).

For a literal original-coordinate cross block \(M=A[I,J]\), a probability law \(w\) on supported \(3\times3\) physical minors has row marginals \(\alpha_k\) and entropy currency
\[
G(w)=\exp\!\left(
 \sum_{S,T}w_{S,T}
 \log\frac{\det(M[S,T])^2}{w_{S,T}}
\right).
\]
If \(1\le q<3/2\) and \(\max_k\alpha_k\le q/2\), then, retaining arbitrary same-bank terms, outside couplings, signs, and affine terms,
\[
\|p_Q\|_\infty
\le
\frac{3e}{(3-2q)\sqrt q}\,G(w)^{-1/6},
\tag{1.1}
\]
and \(p_Q\) has a continuous \(C_0\) representative.

The fourth-volume deletion theorem used for comparison is account01/B04 at
\(\texttt{72d2768d509944880036a97581ff5115208bd8f4}\).
The earlier account04/B04 nested-anchor payment is at
\(\texttt{3224f273e92d97a8bff7424e9b1191c1e49d0611}\).

## 2. Anchored face law

Let the physical rows of \(M\) be \(m_1,\dots,m_N\), and suppose
\[
E_4(M)=e_4(M^\top M)>0.
\]
For a four-row set \(R\), write
\[
d_R=\det(M[R,:]M[R,:]^\top).
\]
The canonical fourth-volume law is
\[
\pi(R)=\frac{d_R}{E_4(M)}.
\]
Fix a physical row \(i\), and define its carrier leverage
\[
\rho_i=\mathbb P_\pi(i\in R),\qquad
H_i=\sum_{R\ni i}d_R=\rho_iE_4(M).
\tag{2.1}
\]

For every three-row set \(S\subset[N]\setminus\{i\}\), put
\[
a_S=\det(M[S,:]M[S,:]^\top),
\qquad
h_i(S)^2=\operatorname{dist}\!\left(m_i,\operatorname{span}\{m_s:s\in S\}\right)^2.
\]
The Gram height identity gives
\[
d_{S\cup\{i\}}=a_Sh_i(S)^2.
\tag{2.2}
\]
Assume \(H_i>0\), and define the anchored face law
\[
\mu_i(S)=\frac{a_Sh_i(S)^2}{H_i}.
\tag{2.3}
\]
It is a probability law. Its row marginals are
\[
\beta_j=\mathbb P_{\mu_i}(j\in S)
       =\mathbb P_\pi(j\in R\mid i\in R),
\qquad j\ne i.
\tag{2.4}
\]

Lift \(\mu_i\) to physical \(3\times3\) minors by the canonical conditional column-volume law:
\[
w_{S,T}
=
\mu_i(S)\frac{\det(M[S,T])^2}{a_S}.
\tag{2.5}
\]
Cauchy--Binet shows that \(w\) is normalized and has row marginals \(\beta_j\).

## 3. Exact anchored entropy currency

For every supported \((S,T)\),
\[
\frac{\det(M[S,T])^2}{w_{S,T}}
=
\frac{a_S}{\mu_i(S)}
=
\frac{H_i}{h_i(S)^2}.
\]
Therefore, defining
\[
h_{\mathrm{geo}}^2
=
\exp\!\left(\sum_S\mu_i(S)\log h_i(S)^2\right),
\tag{3.1}
\]
we obtain the exact identity
\[
\boxed{G(w)=\frac{H_i}{h_{\mathrm{geo}}^2}.}
\tag{3.2}
\]
Since \(h_i(S)^2\le\|m_i\|_2^2\),
\[
\boxed{
G(w)\ge \frac{\rho_iE_4(M)}{\|m_i\|_2^2}.
}
\tag{3.3}
\]

This is the anchored counterpart of account01/B04's uniform four-face deletion currency. It is specifically adapted to a high carrier row: the carrier is deleted, and the remaining triple is paid in the original coordinates.

## 4. Density-or-double-anchor theorem

### Theorem

Let
\[
\beta_*=\max_{j\ne i}\beta_j.
\]
If \(\beta_*<3/4\), set
\[
q_i=\max\{1,2\beta_*\}<3/2.
\]
Then the full ambient quadratic form has a continuous \(C_0\) density and
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{3e}{(3-2q_i)\sqrt{q_i}}
\left(\frac{H_i}{h_{\mathrm{geo}}^2}\right)^{-1/6}.
}
\tag{4.1}
\]
In particular,
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{3e}{(3-2q_i)\sqrt{q_i}}
\left(\frac{\rho_iE_4(M)}{\|m_i\|_2^2}\right)^{-1/6}.
}
\tag{4.2}
\]

If instead \(\beta_*\ge\theta\) for any chosen \(0<\theta<1\), then some \(j\ne i\) satisfies the literal same-matrix double-anchor inequality
\[
\boxed{
\mathbb P_\pi(i,j\in R)=\rho_i\beta_j\ge\theta\rho_i.
}
\tag{4.3}
\]

### Proof

The row marginal of \(w\) at \(j\) equals \(\beta_j\). Thus
\[
\max_j\alpha_j=\beta_*\le q_i/2.
\]
Equation (4.1) follows directly from (1.1) and the exact currency (3.2); (4.2) follows from (3.3). Equation (4.3) is exactly the conditional-probability identity in (2.4). No rotated random variables or conditional density cap is used. \(\square\)

## 5. Actual live inequality at carrier leverage \(>1/25\)

Take the clean threshold \(\theta=2/3\). If the surviving physical carrier obeys
\[
\rho_i>\frac1{25},
\tag{5.1}
\]
then exactly one of the following occurs.

### Entropy-payment branch

If \(\beta_*\le2/3\), then \(q_i\le4/3\). The prefactor in (4.2) is at most its value at \(q=4/3\):
\[
\frac{3e}{(3-8/3)\sqrt{4/3}}
=
\frac{9e\sqrt3}{2}.
\]
Consequently,
\[
\boxed{
\|p_Q\|_\infty
<
\frac{9e\sqrt3}{2}
\left(\frac{25\|m_i\|_2^2}{E_4(M)}\right)^{1/6}.
}
\tag{5.2}
\]

### Double-anchor branch

If \(\beta_*>2/3\), then for some \(j\ne i\),
\[
\boxed{
\mathbb P_\pi(i,j\in R)>\frac{2}{75}.
}
\tag{5.3}
\]
Thus failure of the strict anchored \(D'\) gate does not merely say that a marginal is heavy: it produces a quantitative pair of physical carrier rows on the same original-coordinate matrix.

Equations (5.2)--(5.3) are the promised new implication for the first branch left after the nested-anchor result.

## 6. Same-matrix comparison of \(D'\), \(D_5\), and ridge

All three certificates are evaluated on the same literal block \(M=A[I,J]\).

1. **Optimized \(D'\) / third-volume entropy.**  
   The anchored face law gives the exact currency
   \[
   G_i=\frac{H_i}{h_{\mathrm{geo}}^2}
   \ge\frac{\rho_iE_4(M)}{\|m_i\|_2^2}.
   \]
   It pays whenever the conditional face marginals are \(<3/4\), and it gives the explicit live estimate (5.2) at the \(2/3\) threshold.

2. **\(D_5\).**  
   A fifth-volume certificate requires \(E_5(M)>0\) at the relevant scale. The anchored theorem assumes only \(E_4(M)>0\), so it remains available for exact rank four, where
   \[
   E_5(M)=0.
   \]
   Hence \(D_5\) does not subsume (4.1).

3. **Ridge.**  
   Ridge payment depends on a spectral-window leverage gate for the regularized range projection. Neither \(H_i>0\) nor the conditional face marginals \(\beta_j\) imply that gate. Conversely, ridge can pay diffuse full-rank blocks even when the anchored fourth-volume currency is poor. Thus the two mechanisms are complementary, not interchangeable.

The uncovered same-matrix state after these comparisons is explicit:
\[
\rho_i>\frac1{25},
\qquad
\beta_*>\frac23,
\qquad
\mathbb P_\pi(i,j\in R)>\frac2{75},
\tag{6.1}
\]
together with failure of the already-established \(D_5\) and ridge thresholds. This is a genuine double-anchor packet, not an arbitrary “heavy leverage” label.

## 7. Remaining full-target implication

The full conjecture remains open. The next structural obligation is:

> Starting from the double-anchor mass (6.1), either promote its anchored fourth-volume to the already-paid physical \(E_3\) or rank-four receivers while retaining all same-bank leakage, or prove that simultaneous failure forces the existing two-star--Frobenius or compound-hub currency at a universal scale.

The present theorem does not infer a large individual minor, does not drop a weak singular direction, and does not convert coefficient smallness into probabilistic smallness. Continuity is asserted only on the entropy-payment branch through the completed Fourier theorem.
