# B16 — exact shared-variable product ledger: positive XOR reference, signed coherent transport, and physical overlap

**Run:** 2026-09-21T12:29:07Z, fleet02/B16  
**Live role:** FEI signed transport proof; sprint specialization: **fleet02/B16 — a composition or restriction identity that retains dependence terms**  
**Directive:** `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z` under `BRAIN-BENCHMARK-FEI-2026-09-21-01`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI status:** **OPEN / NOT PROVED**.

**Measurable quantity.** The candidate shortcut “replace coherent shared-variable multiplication by the incoherent XOR convolution” had no checked sign. This run gives an exact four-term ledger and an exact four-variable witness with
\[
H(p)-H(q)=0.3671693682655901\ldots>0,\qquad
I(p)-I(q)=-3/8.
\]
Thus the shortcut fails in both dangerous directions at once: the incoherent law can have *smaller* entropy and *larger* influence. The remaining universal obligation is not that shortcut; it is a signed payment inequality for the exact ledger below.

The three new `FLEET_RULES` moves used here are **#5 ADD A PARAMETER AND DIFFERENTIATE** (interpolate between the incoherent and coherent spectral laws), **#11 DUALIZE** (move shared-variable multiplication to XOR convolution of Walsh amplitudes), and **#25 COUNT THE SAME THING TWICE** (compute the influence correction once from physical simultaneous flips and once from spectral XOR marginals). The previous B16 run used #2/#14/#4, so these are different moves.

No absolute values are taken in the coherent correction. Multiplicity is retained as a conditional entropy, destructive/constructive interference remains signed, the KL curvature term is kept as a nonnegative refund, and the influence correction is expressed in the original physical coordinate geometry.

---

## 1. Fresh continuity and complementary ownership

The current FEI entry says full FEI is still open. The active three-hour sprint assigns fleet02/B16 specifically to a **shared-variable composition or restriction identity retaining dependence terms**; this report implements that scope rather than continuing the preceding q-flip multiplier calculation.

Two directly relevant complete peer reports were read.

1. `fleet04/B16/20260921T100953Z-signed-transport/REPORT.md`, blob `88d9d9d43403c51157eb2010863d6e0236d28709`, proves a canonical signed three-phase transport for \(u,v,uv\), with genuine squared Fourier marginals, and shows
   \[
   \mathscr H_\mu(A,B\mid A\oplus B)=\frac12\{H(u)+H(v)-H(uv)\}.
   \]
   Its internal negative mass is real and must not be replaced by a fictitious positive coupling.

2. `fleet01/B16/20260921T114047Z-coordinate-noise-radon-lowmode/REPORT.md`, blob `e7f10a03a65e711b02c45481dd281a54a6b38e52`, proves an exact original-coordinate cut/noisy-square bridge and a dimension-free \(L^2\) payment for bounded mean-zero q-flip kernels, then proves that the raw random-order generator baseline has fixed low Walsh multipliers of order \(n\). Hence exact refunds must cancel low modes, not merely the mean.

The present calculation is complementary: it replaces neither signed transport nor the cut geometry. It gives an exact **positive-reference disintegration** of the shared product \(uv\), identifies the original-coordinate dependence cost, and exposes the single signed coherent transport that remains.

---

## 2. Normalization

Let \(G=\mathbb F_2^n\), with normalized Walsh transform
\[
\widehat a(s)=2^{-n}\sum_{x\in G}a(x)(-1)^{s\cdot x}.
\]
For a Boolean phase \(a:G\to\{\pm1\}\), write
\[
P_a(s)=\widehat a(s)^2,\qquad
H(a)=-\sum_sP_a(s)\log_2P_a(s),\qquad
I(a)=\sum_s |s|P_a(s).
\]
Parseval gives \(\sum_sP_a(s)=1\).

Take two arbitrary Boolean phases \(a,b\) on the **same** cube; no independence or disjointness is assumed. Set
\[
h=ab,\quad
\alpha_t=\widehat a(t),\quad
\beta_u=\widehat b(u),\quad
\gamma_s=\widehat h(s).
\]
Fourier multiplication is coherent XOR convolution:
\[
\gamma_s=\sum_t\alpha_t\beta_{s\oplus t}.
\tag{2.1}
\]
Define the genuine output spectral law
\[
p_s=\gamma_s^2
\tag{2.2}
\]
and the **incoherent XOR reference**
\[
q_s=\sum_t \alpha_t^2\beta_{s\oplus t}^2.
\tag{2.3}
\]
Equivalently, if \(T\sim P_a\) and \(U\sim P_b\) are independent, then \(Q=T\oplus U\) has law \(q\).

Both \(p\) and \(q\) are probability laws. Moreover \(p_s>0\) implies \(q_s>0\), because a nonzero coherent sum in (2.1) contains at least one nonzero summand.

Put
\[
\Delta_s=p_s-q_s,\qquad \sum_s\Delta_s=0.
\tag{2.4}
\]

---

## 3. The positive-reference coherent interpolation

For \(0\le\theta\le1\), define
\[
r_\theta(s)=q_s+\theta\Delta_s=(1-\theta)q_s+\theta p_s.
\tag{3.1}
\]
This is an honest probability law for every \(\theta\). Coordinates with \(q_s=0\) also have \(p_s=0\) and may be omitted.

Let
\[
\mathcal E(\theta)=H(r_\theta).
\]

### Theorem 3.1 — exact integrated coherent transport

For every pair of Boolean phases \(a,b\),
\[
\boxed{
\mathcal E'(\theta)
=\sum_s\Delta_s\log_2\frac1{r_\theta(s)}
}
\tag{3.2}
\]
and
\[
\boxed{
\mathcal E''(\theta)
=-\frac1{\ln2}\sum_s\frac{\Delta_s^2}{r_\theta(s)}
\le0.
}
\tag{3.3}
\]
Consequently
\[
\boxed{
H(ab)
=H(q)+\int_0^1
\sum_s\Delta_s\log_2\frac1{q_s+\theta\Delta_s}\,d\theta.
}
\tag{3.4}
\]

#### Proof

Differentiate
\[
-\sum_s r_\theta(s)\log_2 r_\theta(s).
\]
The derivative contains
\[
-\sum_s\Delta_s\log_2 r_\theta(s)
-\frac1{\ln2}\sum_s\Delta_s.
\]
The second sum vanishes by (2.4), giving (3.2). Differentiating once more gives (3.3). Integrating (3.2) from \(0\) to \(1\) gives (3.4). No sign of \(\Delta_s\) is changed. \(\square\)

The interpolation is a literal signed transport through positive intermediate laws. The curvature is always negative, and its magnitude is the exact quadratic coherence cost.

Define
\[
\operatorname{Coh}(a,b)
:=\sum_s\Delta_s\log_2\frac1{q_s},
\tag{3.5}
\]
and
\[
D(p\|q)=\sum_{s:p_s>0}p_s\log_2\frac{p_s}{q_s}.
\tag{3.6}
\]

### Corollary 3.2 — endpoint tangent minus KL refund

\[
\boxed{
H(p)-H(q)=\operatorname{Coh}(a,b)-D(p\|q).
}
\tag{3.7}
\]
Moreover
\[
\boxed{
D(p\|q)
=\frac1{\ln2}\int_0^1(1-\theta)
\sum_s\frac{\Delta_s^2}{r_\theta(s)}\,d\theta.
}
\tag{3.8}
\]

#### Proof

Taylor's formula with integral remainder gives
\[
\mathcal E(1)-\mathcal E(0)
=\mathcal E'(0)+\int_0^1(1-\theta)\mathcal E''(\theta)d\theta.
\]
Substitute (3.2)–(3.3). The resulting Bregman remainder is exactly \(D(p\|q)\), which can also be checked directly by expanding (3.5). \(\square\)

Thus the dangerous signed term is not replaced by its absolute value: the endpoint signed cross-entropy \(\operatorname{Coh}\) is accompanied by the exact nonnegative KL refund.

---

## 4. Dual-code multiplicity is an exact entropy refund

Because \((T,U)\mapsto(T,Q=T\oplus U)\) is bijective,
\[
H(T,U)=H(T,Q)=H(Q)+H(T\mid Q).
\]
Since \(T,U\) are independent,
\[
H(T,U)=H(a)+H(b).
\]

Define the collision/multiplicity entropy
\[
\mathcal M(a,b):=H(T\mid Q)=H(T,U\mid Q)\ge0.
\tag{4.1}
\]
Then
\[
\boxed{
H(q)=H(a)+H(b)-\mathcal M(a,b).
}
\tag{4.2}
\]

Combining (3.4) and (4.2) gives the first main identity.

### Theorem 4.1 — shared-variable entropy composition ledger

For arbitrary Boolean \(a,b\) on the same cube,
\[
\boxed{
H(ab)=H(a)+H(b)-\mathcal M(a,b)
+\int_0^1\sum_s\Delta_s\log_2\frac1{r_\theta(s)}\,d\theta.
}
\tag{4.3}
\]
Equivalently,
\[
\boxed{
H(ab)=H(a)+H(b)-\mathcal M(a,b)
+\operatorname{Coh}(a,b)-D(p\|q).
}
\tag{4.4}
\]

This retains **all** XOR multiplicity. In particular, the signed triangle defect from fleet04 has the positive-reference disintegration
\[
\boxed{
H(a)+H(b)-H(ab)
=\mathcal M(a,b)+D(p\|q)-\operatorname{Coh}(a,b).
}
\tag{4.5}
\]
Thus fleet04's signed conditional functional is exactly one half of the right side of (4.5). The term \(\operatorname{Coh}\) can have either sign; \(\mathcal M\) and \(D\) are genuine nonnegative credits.

---

## 5. Original-coordinate influence dependence

For each physical coordinate \(i\), define the flip indicators
\[
A_i(x)=1_{\{a(x)\ne a(x\oplus e_i)\}},\qquad
B_i(x)=1_{\{b(x)\ne b(x\oplus e_i)\}}.
\]
The product \(ab\) flips across an \(i\)-edge exactly when one, but not both, of \(a,b\) flips. Hence, with
\[
R_i(a,b)=\mathbb E_x A_i(x)B_i(x),\qquad
R(a,b)=\sum_iR_i(a,b),
\tag{5.1}
\]
we have the exact physical identity
\[
\boxed{
I(ab)=I(a)+I(b)-2R(a,b).
}
\tag{5.2}
\]

This is the dependence term that disappears under disjoint variables. It is not a product of marginals.

There is a second exact count. Let
\[
\Omega(a,b)=\sum_i \operatorname{Inf}_i(a)\operatorname{Inf}_i(b).
\tag{5.3}
\]
Because \(Q=T\oplus U\) for independent spectral samples and
\(\Pr(i\in T)=\operatorname{Inf}_i(a)\),
\[
\boxed{
I(q)=I(a)+I(b)-2\Omega(a,b).
}
\tag{5.4}
\]
Therefore the coherent/incoherent first-moment shift is
\[
\boxed{
I(p)-I(q)=2\{\Omega(a,b)-R(a,b)\}.
}
\tag{5.5}
\]

Equation (5.5) is the requested “count the same thing twice” bridge: the discrepancy between the incoherent spectral XOR and the actual shared-variable product is exactly the discrepancy between independent spectral overlap and simultaneous **physical** edge flips. No Hamming surrogate replaces the original coordinate geometry.

---

## 6. Exact FEI-deficit recursion for a shared product

For a real \(C>0\), let
\[
\Phi_C(g)=H(g)-C I(g).
\tag{6.1}
\]

### Theorem 6.1 — coherent shared-product deficit identity

For every pair of Boolean phases on the same cube,
\[
\boxed{
\Phi_C(ab)
=\Phi_C(a)+\Phi_C(b)
+2C\,R(a,b)-\mathcal M(a,b)
+\int_0^1\sum_s\Delta_s\log_2\frac1{r_\theta(s)}\,d\theta.
}
\tag{6.2}
\]
Equivalently,
\[
\boxed{
\Phi_C(ab)
=\Phi_C(a)+\Phi_C(b)
+2C\,R(a,b)-\mathcal M(a,b)
+\operatorname{Coh}(a,b)-D(p\|q).
}
\tag{6.3}
\]

#### Proof

Subtract \(C\) times (5.2) from (4.3) or (4.4). \(\square\)

This is a genuine shared-variable composition identity. It identifies the exact four-way payment:

* **physical dependence debit:** \(2CR\);
* **XOR multiplicity credit:** \(-\mathcal M\);
* **signed coherent cross-entropy:** \(+\operatorname{Coh}\);
* **curvature/KL refund:** \(-D(p\|q)\).

No one of these may be silently discarded.

A decomposition proof of FEI through products would therefore need to show that the accumulated positive shared-overlap/coherent charges are paid by inherited factor slack plus \(\mathcal M+D\). The local sufficient condition
\[
2CR+\operatorname{Coh}\le \mathcal M+D
\tag{6.4}
\]
makes \(\Phi_C\) subadditive at that product node, but (6.4) is **not claimed universally true** and is stronger than FEI because factor slack can also pay the node.

### Sanity checks

* **Disjoint variable blocks.** Every output label has a unique spectral decomposition, so \(p=q\), \(\mathcal M=0\), and \(R=0\). Equation (6.2) reduces to exact tensorization.
* **Character factor.** If \(b\) is a character, \(p=q\) is only a spectral shift and \(\mathcal M=0\). Equation (6.2) reduces to the exact influence change under output-character multiplication.
* **Multiplicative derivatives.** Taking \(b(x)=a(x+z)\) and averaging over uniform \(z\), orthogonality gives \(\mathbb E_zp^{(z)}=q\). Hence the averaged signed cross-entropy vanishes and
  \[
  2H(a)-\mathbb E_zH(a(\cdot)a(\cdot+z))
  =\mathcal M+\mathbb E_zD(p^{(z)}\|q).
  \tag{6.5}
  \]
  This recovers the existing sharp-derivative identity
  \(D_\times=H(S\mid S+T)+I(S+T;Z)\); (6.5) is included as a compatibility check, **not announced as new**.

---

## 7. Exact obstruction: incoherent XOR can underestimate entropy and overestimate influence

A tempting shortcut would be
\[
H(p)\le H(q),
\tag{7.1}
\]
which would let one throw away the integrated coherent term. It is false even in four variables.

Let
\[
f(x)=(-1)^{x_1x_2+x_3x_4}.
\tag{7.2}
\]
This is a nondegenerate quadratic phase, so its Fourier law is uniform:
\[
P_f(s)=1/16,\qquad H(f)=4,\qquad I(f)=2.
\tag{7.3}
\]

Let \(b\) be the one-point defect
\[
b(0)=-1,\qquad b(x)=1\ (x\ne0),
\tag{7.4}
\]
and set
\[
a=fb.
\tag{7.5}
\]
Then \(ab=f\) exactly.

The one-point defect has
\[
P_b(0)=49/64,\qquad P_b(s)=1/64\quad(s\ne0).
\tag{7.6}
\]
Flipping the value of the bent phase at the origin shifts every Fourier amplitude by \(-1/8\). The quadratic \(f\) has six negative and ten positive Fourier amplitudes, so
\[
P_a(s)\in\{9/64,1/64\},
\]
with multiplicities six and ten.

Using (2.3),
\[
q_s=\frac{48P_a(s)+1}{64}.
\]
Therefore
\[
\boxed{
q_s=
\begin{cases}
31/256,&6\text{ labels},\\
7/256,&10\text{ labels}.
\end{cases}
}
\tag{7.7}
\]
The coherent product law \(p=P_f\) is uniform. Since uniform measure uniquely maximizes entropy on sixteen points,
\[
\boxed{H(p)=4>H(q).}
\tag{7.8}
\]
Numerically,
\[
H(q)=3.632830631734410\ldots,
\quad
H(p)-H(q)=0.367169368265590\ldots.
\tag{7.9}
\]

The influence direction is simultaneously unfavorable to the shortcut. Directly,
\[
I(a)=5/2,\qquad I(b)=1/2,\qquad I(ab)=2.
\tag{7.10}
\]
The simultaneous physical flip overlap is
\[
R(a,b)=1/2.
\tag{7.11}
\]
The spectral marginal overlap is
\[
\Omega(a,b)=5/16,
\tag{7.12}
\]
and hence
\[
\boxed{
I(q)=19/8,\qquad I(p)-I(q)=-3/8.
}
\tag{7.13}
\]

So replacing coherent multiplication by the positive XOR law \(q\) would **lower entropy by 0.367 bits and raise influence by 3/8**. It biases an FEI estimate in exactly the favorable-but-invalid direction. The signed coherent transport cannot be omitted or bounded by zero.

For this witness the decomposition numerically reads
\[
\mathcal M=1.393782923897933\ldots,\quad
D(p\|q)=0.387579557318919\ldots,
\]
\[
\operatorname{Coh}=0.754748925584509\ldots,
\]
so indeed
\[
H(p)-H(q)=\operatorname{Coh}-D>0.
\]

This is a counterexample only to the stronger shortcut (7.1), **not** to FEI.

---

## 8. Self-check

`check_shared_product_coherent_ledger.py` uses exact rational Walsh probabilities for every mass/influence identity and binary64 only for the logarithms. It:

* exhausts all **65,536 ordered pairs** of Boolean functions on \(n=3\);
* checks the coherent/incoherent probability laws and both exact influence counts;
* checks (4.4)/(4.5) numerically, with maximum entropy identity error
  \(4.440892098500626\times10^{-16}\);
* verifies the four-variable witness's exact distributions
  \(p\equiv1/16\) and \(q\in\{31/256,7/256\}\) with multiplicities \(6,10\);
* verifies \(I(a)=5/2\), \(I(b)=1/2\), \(I(p)=2\), \(I(q)=19/8\), \(R=1/2\), and \(\Omega=5/16\).

The checker is a self-check of the algebra and witness; it is not an independent audit and does not prove full FEI.

---

## 9. Prior-art check and applicability

A current primary-source search was performed before making any novelty claim.

* O'Donnell–Tan, **“A composition theorem for the Fourier Entropy-Influence conjecture”**, arXiv:1304.1347 (2013), gives the standard FEI composition theorem for inner functions on **disjoint variable sets**. The shared-variable dependence terms above are precisely absent in that hypothesis.
* González–MacManus–Pereyra, **“Further evidence towards the Fourier Entropy-Influence conjecture”**, arXiv:2606.00246 (29 May 2026), develops restriction/stopping-tree induction and explicitly leaves the universal FEI statement open.
* Potapov, **“On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions”**, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued and partially bent classes, not arbitrary shared-variable products.

The repository's existing sharp-derivative theorem already contains the averaged specialization (6.5), and fleet04's current signed three-phase transport contains the signed triangle defect. The contribution here is the shared-pair **positive XOR reference + signed integrated interpolation + original-coordinate simultaneous-flip ledger** and the exact obstruction to discarding its coherent correction. I did not find this exact packaging in the targeted search, but a search miss is not a novelty proof, so **no publication-priority claim is made**.

---

## 10. Claim ledger

| Claim | Status | Scope |
|---|---|---|
| Exact interpolation identities (3.2)–(3.4) | **PROVED** | every pair of Boolean phases |
| KL curvature refund (3.7)–(3.8) | **PROVED** | every pair |
| Multiplicity entropy identity (4.2) | **PROVED** | every pair |
| Shared-variable entropy ledger (4.3)–(4.5) | **PROVED** | every pair |
| Physical influence overlap identity (5.2) | **PROVED** | every pair, original coordinates |
| Spectral XOR first-moment identity (5.4) and bridge (5.5) | **PROVED** | every pair |
| FEI-deficit recursion (6.2)–(6.3) | **PROVED** | every \(C>0\), every pair |
| Universal local payment (6.4) | **OPEN / not asserted** | sufficient strengthening |
| Shortcut \(H(p)\le H(q)\) | **DISPROVED** | exact \(n=4\) Boolean witness |
| Full FEI | **OPEN / NOT PROVED** | unrestricted Boolean functions |

---

## 11. Residual universal obligation and next attack

The identity isolates a sharper signed target than “control shared composition somehow.” At a product node,
\[
\Xi_C(a,b)
:=2C R(a,b)-\mathcal M(a,b)
+\int_0^1\sum_s\Delta_s
\log_2\frac1{q_s+\theta\Delta_s}\,d\theta.
\tag{11.1}
\]
Then
\[
\Phi_C(ab)=\Phi_C(a)+\Phi_C(b)+\Xi_C(a,b).
\tag{11.2}
\]

The universal problem is to control the accumulated \(\Xi_C\) by factor slack/influence **without** positive-parting the signed integral. The four-variable obstruction proves that the integrated term itself is not always nonpositive. The next concrete attack should therefore combine (3.3)'s exact curvature refund with the fleet01 cut-field \(L^2\) bank: seek an original-coordinate representation of \(\Delta=p-q\) whose low modes are paid by \(\mathcal M\) and whose high modes are paid by
\[
\int_0^1\sum_s \frac{\Delta_s^2}{r_\theta(s)}\,d\theta
\]
or by the existing noisy-square/q-flip energy. A successful estimate must keep the \(2CR\) physical overlap term visible rather than replacing it with independent spectral overlap \(\Omega\).

That is the next unpaid theorem. No claim of full FEI closure is made.
