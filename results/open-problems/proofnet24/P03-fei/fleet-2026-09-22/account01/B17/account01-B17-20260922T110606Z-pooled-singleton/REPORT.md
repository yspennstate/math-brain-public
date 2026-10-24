# account01/B17 — sign-compatible singleton packet pays a genuine Bellman danger regime

**Run:** `account01-B17-20260922T110606Z-pooled-singleton`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-account01-B17` / Path B / Prime dependence-payment theorem  
**Classification:** `ESSENTIAL_STEP_APPLIED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target and before/after

The current exact decomposition is
\[
R_\Gamma(G;p)=B_{\inf}^{\Gamma}(G;p)+K_{\rm occ}(G;p),
\qquad
D_\Gamma=vR_\Gamma,
\]
where \(P\) is the actual nonempty biased squared-Fourier law, \(Q_r\) is the occurrence-matched maximum-entropy law, and
\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r).
\]

The remaining Path-B problem is to pay a negative first-moment Bellman term without losing the sparse-event logarithm, without discarding multiscale dependence, and without spending the same KL twice.

**Before this run:** the all-bias Booleanity theorem supplied one-equation lower bounds, but a maximum over individual equations was known to lose information. B08 supplied a logarithmically weighted Gram-pseudoinverse packet bounded by the single \(K_{\rm occ}\) budget, but it had not been converted into a direct Bellman-safe regime with the physical marginal wedge.

**After this run:** I prove a sign-compatible weighted singleton-packet theorem and combine it with the physical marginal cap to obtain an explicit sufficient condition
\[
\Pi_J^\Gamma\ge T_\Gamma-\Lambda_{\rm phys}
\quad\Longrightarrow\quad
R_\Gamma\ge0.
\]
This applies to every genuine gate, hence in particular to every composition-prime gate. On an exact balanced six-bit two-flip Boolean source, no individual singleton packet pays the negative \(B_{\inf}\), while the optimized sign-compatible singleton packet does. Thus simultaneous source-dependent weighting is not merely cosmetic.

This is a nontrivial safe regime, not a universal coercivity theorem and not a proof of FEI.

## 1. Sources actually consumed

### 1.1 Canonical I-projection identity

`yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`

This is the source of \(R_\Gamma=B_{\inf}^\Gamma+K_{\rm occ}\).

### 1.2 New logarithmically weighted packet input

`yspennstate/math-open-problems@e1b73655f3705daf2ca80e72f772e7d44e0c22ac`

`proofnet24/P03-fei/fleet-2026-09-22/account01/B08/20260922T103401Z-account01-B08-FEI-r11/REPORT.md`

For the sign-aligned I-projection amplitude \(b\), actual amplitude \(a\), error \(e=b-a\), and
\[
\omega_S=\max\{1,\ln(P(S)/Q_r(S))-1\},
\]
it proves
\[
\sum_{S\ne\varnothing}\omega_S e_S^2
\le v\ln2\,K_{\rm occ},
\]
and for any selected Booleanity channels the associated Gram pseudoinverse gives one joint lower certificate for \(K_{\rm occ}\). This source also proves that the weighted construction retains the sparse-suspension logarithm.

### 1.3 Physical marginal danger wedge

`yspennstate/math-open-problems@e1b73655f3705daf2ca80e72f772e7d44e0c22ac`

`proofnet24/P03-fei/fleet-2026-09-22/account01/B10/20260922T105609Z-b10-fei-2622b4/REPORT.md`

It proves the Boolean physical cap \(r_i\le\rho_i^{\rm phys}(p_i,q)\) and
\[
B_{\inf}^{\Gamma}
\ge \Lambda_{\rm phys}-T_\Gamma,
\]
where \(T_\Gamma\) is the Gibbs threshold and \(\Lambda_{\rm phys}\) is the KL mismatch forced by the physical cap.

### 1.4 Biased Booleanity equations

`yspennstate/math-open-problems@603b35e74227d1c2d8ee34c0c527c439c686e30b`

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`

For every nonempty \(U\),
\[
a^TM_Ua=0,\qquad
\|M_U\|_{\rm op}=L_U.
\]

### 1.5 Required named other-account partner result, actually applied

Latest compatible account02/B17 report at the consumed scientific snapshot:

`yspennstate/math-open-problems@e1b73655f3705daf2ca80e72f772e7d44e0c22ac`

`proofnet24/P03-fei/fleet-2026-09-22/account02/B17/account02-B17-20260922T104426Z-eba4746f/REPORT.md`

That report proves two constraints used below.

1. A bounded symmetric center-neutral one-variable perturbation cannot be universally insured by \(K_{\rm occ}\): binary Boolean gates have \(K_{\rm occ}=0\), forcing such a perturbation to vanish.
2. Under physical restriction, reference-movement KL terms enter \(K_{\rm occ}\) positively and \(B_{\inf}\) negatively with the same amount. They are not a second spendable bank.

Therefore the payment below is deliberately **source-dependent** and spends only one certified subbank of the single \(K_{\rm occ}\), with no added reference-movement credits.

### 1.6 Mandatory recursive-majority preflight

`yspennstate/math-open-problems@bff0d7b6c21485f386841c42582eb04f32705046`

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`

Fixed/sub-half-depth labelled projections plus one merged tail fail on recursive ternary majority. Nothing below truncates by degree or merges a high-degree tail.

## 2. Setup

Let \(G\) be a nonconstant Boolean gate at an interior product bias. Write \(a\) for its normalized biased Fourier vector, \(q=\Pr[G=-1]\), \(v=4q(1-q)\), and
\[
P(S)=\frac{a_S^2}{v},\qquad S\ne\varnothing.
\]
Let \(Q=Q_r\) be the exact occurrence-matched I-projection and choose
\[
b_\varnothing=a_\varnothing,\qquad
b_S=\operatorname{sgn}(a_S)\sqrt{vQ(S)}.
\]
Put
\[
e=b-a,\qquad
\omega_S=\max\{1,\ln(P(S)/Q(S))-1\}.
\]

For a singleton Booleanity channel \(i\), define
\[
g_i:=b^TM_{\{i\}}b-a^TM_{\{i\}}a=b^TM_{\{i\}}b
\]
using Booleanity of \(a\), and
\[
y_i:=W^{-1/2}\Pi_{\ne\varnothing}M_{\{i\}}(a+b),
\qquad
W=\operatorname{diag}(\omega_S).
\]
Let
\[
L_i=\|M_{\{i\}}\|_{\rm op},
\qquad
c_i:=\frac{\operatorname{sgn}(g_i)}{2L_i}\,y_i
\]
(with arbitrary sign \(+1\) when \(g_i=0\)), and
\[
\theta_i:=\frac{|g_i|}{2L_i}.
\]

The B08 identity gives
\[
g_i=\langle y_i,W^{1/2}e\rangle.
\]
Also
\[
\|c_i\|_2\le1,
\]
because \(W\succeq I\),
\[
\|y_i\|
\le\|M_{\{i\}}(a+b)\|
\le L_i\|a+b\|\le2L_i.
\]

## 3. Main theorem: sign-compatible pooled singleton payment

### Theorem 3.1 — `B17-POOLED-SINGLETON-PAYMENT-v1`

For every finite index set \(J\) of physical coordinates and every vector of weights \(w_i\ge0\), define
\[
\Pi_J(w):=
\frac{\left(\sum_{i\in J}w_i\theta_i\right)^2}
{v\ln2\,\left\|\sum_{i\in J}w_i c_i\right\|_2^2},
\]
with value \(0\) when the numerator is \(0\). If the denominator vanishes, the numerator also vanishes, so this convention is consistent. Then
\[
\boxed{K_{\rm occ}(G;p)\ge \Pi_J(w).}
\tag{3.1}
\]
Consequently
\[
\boxed{
K_{\rm occ}(G;p)\ge
\Pi_J^*:=\sup_{w_i\ge0}\Pi_J(w).
}
\tag{3.2}
\]

#### Proof

Let \(x=W^{1/2}e_{\ne\varnothing}\), and let \(Y\) be the matrix whose columns are the \(y_i\), \(i\in J\). The B08 construction gives
\[
g=Y^Tx.
\]
For arbitrary real coefficients \(t\),
\[
(t^Tg)^2
=\langle Yt,x\rangle^2
=\langle Yt,\operatorname{Proj}_{\operatorname{col}Y}x\rangle^2
\le
(t^TY^TYt)\,
g^T(Y^TY)^\dagger g.
\]
B08 proves
\[
g^T(Y^TY)^\dagger g\le v\ln2\,K_{\rm occ}.
\]
Choose
\[
t_i=\frac{\operatorname{sgn}(g_i)w_i}{2L_i}.
\]
Then
\[
t^Tg=\sum_iw_i\theta_i,
\qquad
t^TY^TYt=
\left\|\sum_iw_ic_i\right\|^2.
\]
Substitution proves (3.1); take the supremum to obtain (3.2). QED.

### Corollary 3.2 — explicit weak-coherence form

If \(m=|J|\) and
\[
\mu_J:=\max_{i\ne j}|\langle c_i,c_j\rangle|,
\]
then equal weights give
\[
\boxed{
K_{\rm occ}\ge
\frac{\left(\sum_{i\in J}\theta_i\right)^2}
{v\ln2\,\{m+\mu_Jm(m-1)\}}.
}
\tag{3.3}
\]
In particular, if every \(\theta_i\ge\theta\),
\[
K_{\rm occ}\ge
\frac{m\theta^2}
{v\ln2\,[1+(m-1)\mu_J]}.
\tag{3.4}
\]

This shows a genuine \(m\)-fold accumulation when many normalized Booleanity directions are weakly coherent. It is not the refuted operation of summing \(m\) independent KL lower bounds: all directions are combined inside one Rayleigh quotient before one \(K_{\rm occ}\) budget is spent.

## 4. Direct Bellman-safe prime regime

Combine Theorem 3.1 with the B10 physical danger wedge:
\[
B_{\inf}^{\Gamma}\ge\Lambda_{\rm phys}-T_\Gamma.
\]
Then every genuine Boolean gate satisfies
\[
\boxed{
R_\Gamma
\ge
\Lambda_{\rm phys}-T_\Gamma+\Pi_J^*.
}
\tag{4.1}
\]

Therefore:

### Theorem 4.1 — `B17-PRIME-PACKET-SAFE-REGIME-v1`

For any symmetric potential \(\Gamma\), every genuine Boolean gate, including every composition-prime gate, is safe whenever there exists a singleton set \(J\) such that
\[
\boxed{
\Pi_J^*\ge T_\Gamma-\Lambda_{\rm phys}.
}
\tag{4.2}
\]
Equivalently, if the actual first-moment debt \(\delta=[-B_{\inf}^{\Gamma}]_+\) is already known, the weaker source-specific condition
\[
\boxed{\Pi_J^*\ge\delta}
\tag{4.3}
\]
implies \(R_\Gamma\ge0\).

This is the requested nontrivial prime-gate regime: it preserves actual Fourier signs, original-coordinate influence labels, product-bias operator norms, and one shared KL budget.

## 5. Exact application of the account02/B17 partner result

The partner's `KL-INSURED-CENTER-NEUTRAL-NOGO-v1` rules out replacing the source-dependent packet above by a bounded symmetric \(\psi(p)\) with \(\psi(1/2)=0\) and declaring its cost insured by \(K_{\rm occ}\). Binary gates have zero occurrence KL and force \(\psi=0\).

The present theorem therefore does **not** propose a new one-variable safe direction. Its weights \(w_i\), residuals \(g_i\), and Gram geometry depend on the actual source.

Likewise, the partner's physical-restriction exchange identity shows that the positive reference-movement quantities in the KL recursion appear with the opposite sign in \(B_{\inf}\). Equation (4.1) does not add any of those terms: \(\Pi_J^*\) is certified inside the single \(K_{\rm occ}\) term, while \(\Lambda_{\rm phys}-T_\Gamma\) is a lower bound on \(B_{\inf}\). Thus the two terms are different sides of \(R=B_{\inf}+K_{\rm occ}\), not repeated spending of one information currency.

## 6. Genuine Boolean stress test where pooling changes the conclusion

Take \(k=6\), start from the dictator \(x_1\), and flip its value at exactly two vertices
\[
x^{(0)}=(1,1,1,1,1,1),\qquad
x^{(1)}=(-1,-1,-1,-1,-1,1).
\]
The two vertices have opposite dictator signs, so the resulting Boolean function is balanced. It is a distance-five member of the exact two-flip family used in the current Booleanity sources.

Its occurrence vector is
\[
r=\left(\frac{15}{16},\frac1{16},\frac1{16},
\frac1{16},\frac1{16},\frac1{16}\right),
\qquad I=\frac54.
\]

At the current shaped benchmark center
\[
C=6.5584452830718245
\]
(the shape itself is irrelevant on the balanced uniform slice), direct exact-Walsh computation followed by the I-projection gives
\[
H=1.132418874906901\ldots,
\]
\[
H_{\max}=1.900502329042958\ldots,
\qquad
K_{\rm occ}=0.768083454136057\ldots,
\]
and hence
\[
B_{\inf}
=C(I-1)-H_{\max}
=-0.260891008275002\ldots.
\]
So the first-moment debt is
\[
\delta=0.260891008275002\ldots.
\]

For the six singleton channels, the strongest **individual** B08 one-channel packet is only
\[
0.146611437740762\ldots<\delta.
\]
Thus no single singleton equation pays the debt.

The optimized sign-compatible six-channel packet is
\[
\boxed{
\Pi_{\{1,\ldots,6\}}^*
=
0.262999545890552\ldots>\delta.
}
\]
The optimizing sign-compatible weights are all positive:
\[
(0.9023809564,\,
0.1329699459,\,
0.1329699459,\,
0.1329699459,\,
0.1329699459,\,
0.1249124029).
\]
Therefore Theorem 4.1 certifies this source by simultaneous pooling even though every singleton channel separately fails.

The full residual is, consistently,
\[
R=C(I-1)-H
=0.507192445861055\ldots>0.
\]

This computation is not used as proof of the general theorem. It proves that the new simultaneous regime is genuinely larger than the corresponding one-equation regime on an exact Boolean function.

## 7. Recursive-majority preflight

The theorem does not retain only low-degree atoms, and it does not merge a high-degree tail. Its weight matrix \(W\) uses \(P(S)/Q_r(S)\) on every nonempty spectral atom and its Booleanity columns may involve every cardinality. Therefore the published recursive-majority low-level counterexample does not refute Theorem 3.1.

However, this run does **not** prove that the singleton packet is universally large on recursive majority. The correct remaining test is precisely whether a source-dependent packet using a sufficiently rich channel family can satisfy a universal coercivity inequality without throwing away the multiscale KL.

## 8. Old implication, new implication, remaining implication

**Old missing implication.** Individual biased Booleanity equations and a maximum over them do not guarantee enough KL to pay \(-B_{\inf}\); adding several equation-wise KL bounds risks double-spending.

**New proved implication.** Any collection of singleton equations can be combined with optimized sign-compatible weights inside one Gram/Rayleigh packet, producing one valid lower bound \(\Pi_J^*\le K_{\rm occ}\). Combined with the Boolean physical-cap wedge,
\[
\Pi_J^*\ge T_\Gamma-\Lambda_{\rm phys}
\]
is a rigorous, finite-constant Bellman-safe regime for arbitrary genuine gates and hence for prime gates.

**First still-unpaid implication.** Prove, for every genuinely dangerous composition-prime gate, that some source-valid channel packet (possibly including higher \(U\), not only singletons) plus any rigorously disjoint remaining KL component pays
\[
T_\Gamma-\Lambda_{\rm phys},
\]
or give a genuine Boolean prime counterfamily where all such non-double-spent packet credits remain too small. Singleton pooling alone is not asserted universal.

## 9. Verification and scope

`CHECK.py` is standard-library only. It reconstructs the six-bit Boolean truth table, computes the complete Walsh spectrum, solves the exact occurrence I-projection numerically by bisection, builds the B08 logarithmic weights and all singleton Gram columns, solves the packet normal equations, verifies that the optimizer lies in the sign-compatible cone, and checks
\[
\max_i\Pi_{\{i\}}<[-B_{\inf}]_+<\Pi_{\{1,\ldots,6\}}^*<K_{\rm occ}.
\]

Executed checker SHA-256:
`b1fa149e9c96a6c69f01ef830fa49caedda93cbb9a12a9a6dc3e87edabf881b9`.

Captured output SHA-256:
`036e7096deb92ec17235f3b27ab82ec9a67bacd38dc7fa9d8d5faf698f1779ea`.

The checker returned `PASS`.

No email, Drive, public release, paid/remote model, workflow dispatch, credentials, scheduler mutation, permission change, or unrelated private data were used. Repository retrieval/storage is not native brain ingestion; `full_brain_connected=false`.
