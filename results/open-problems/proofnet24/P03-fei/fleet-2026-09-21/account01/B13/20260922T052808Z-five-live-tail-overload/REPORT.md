# B13 — five-live-variable tail reserve forces a genuinely nonterminal FEI overload

**Classification:** `ESSENTIAL_STEP_APPLIED / NONTERMINAL_DEPTH_LOCALIZATION`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were read directly; no installed/authenticated brain receiver context entered the mathematics.

## 0. Exact candidate and conditional end-to-end chain

The current fixed candidate is the account01/B18 source candidate
`account01/B18/20260922T050337Z-complementary-mux-address-tube/REPORT.md`,
which keeps
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]
For a Boolean gate \(G\) at product bias \(p\),
\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]
The universal missing statement remains \(D_{\Gamma^\dagger}(P;p)\ge0\) for every composition-prime finite Boolean gate and every interior product bias. By the exact composition cocycle and the all-gate reformulation, that would imply full FEI with constant \(C^\dagger\).

This report does not prove that universal statement. It proves the structural condition actually needed by the selected random-restriction route on the uniform-cube slice: any negative root defect must create a quantitatively excessive signed correction request **before** the restriction chain reaches five live variables. Thus the terminal tautology identified by account02/B18 can no longer be the location of a putative uniform FEI obstruction.

## 1. Exact peer results consumed and applied

### 1.1 account02/B18 random-depth signed barycenter

I use
`account02/B18/20260922T051105Z-random-depth-barycenter/REPORT.md`.
For a uniformly random permutation of the physical coordinates, reveal the first \(r\) coordinates and their actual branch values, and let \(G_r\) be the resulting random restriction. Define
\[
F_r^{(c)}:=\mathbb E\,D_{\Gamma_c}(G_r),
\qquad
\Gamma_c(u)=\Gamma_0(u)+c\,u(1-u),
\]
and let
\[
\mathsf P_r:=\mathbb E\,M(G_r),\qquad
M(H)={1\over4}\Big(\sum_i \operatorname{It}_i(H)-V_{p_{\rm out}(H)}\Big)\ge0.
\]
Then
\[
F_r^{(c)}=F_r^{(0)}+c\,\mathsf P_r.
\]
Put
\[
L_r^{(0)}:=F_r^{(0)}-F_{r+1}^{(0)},\qquad
\Delta_r:=\mathsf P_r-\mathsf P_{r+1}.
\]
For every root with positive Poincare currency, \(\Delta_r>0\) for \(0\le r\le n-2\), and
\[
\lambda_r:=-{L_r^{(0)}\over\Delta_r}
\]
is the exact signed base-correction request at depth \(r\). Hence
\[
F_r^{(a)}-F_{r+1}^{(a)}
=\Delta_r(a-\lambda_r).
\tag{1.1}
\]
The same peer report correctly observes that stopping only at \(r=n-1\) is tautological because all descendants are constants/literals.

### 1.2 account01/B17 complete five-input uniform theorem

I also use
`account01/B17/20260922T043923Z-arity5-uniform-c001/REPORT.md`.
It proves for **every** five-input Boolean gate at the uniform input-bias vector, with dummy inputs allowed,
\[
D_{\Gamma_{.01}}(H;1/2^5)\ge0,
\qquad
\Gamma_{.01}(u)=\Gamma_0(u)+0.01\,u(1-u).
\tag{1.2}
\]
Thus the entire five-live-variable tail is certified at a scalar coefficient \(0.01\), far below \(a^\dagger=0.268204856\). The result is not restricted to balanced, unate, or composition-prime gates.

These two theorems fit exactly: account02/B18 supplies the signed restriction ledger, while account01/B17 supplies a genuinely nonterminal terminal class with positive reserve.

## 2. Safe-tail localization lemma

The next statement is useful independently of the number five.

### Lemma 2.1 — safe-tail overload

Fix \(0\le b<a\). Let \(G\) be a Boolean gate on \(n\) uniform coordinates, and let \(m<n\). Assume every descendant after \(n-m\) random physical restrictions satisfies
\[
D_{\Gamma_b}(G_{n-m})\ge0
\]
branchwise. Suppose
\[
D_{\Gamma_a}(G)<0.
\]
Set
\[
r_0=n-m,\qquad
\mathsf Q_{r_0}:=\mathsf P_0-\mathsf P_{r_0}
=\sum_{r=0}^{r_0-1}\Delta_r.
\]
Then \(\mathsf Q_{r_0}>0\), and
\[
\boxed{
{1\over\mathsf Q_{r_0}}
\sum_{r=0}^{r_0-1}\Delta_r\lambda_r
>
a+(a-b){\mathsf P_{r_0}\over\mathsf Q_{r_0}}.
}
\tag{2.1}
\]
Consequently at some genuinely nonterminal depth \(0\le r<r_0\),
\[
\boxed{
\lambda_r>
a+(a-b){\mathsf P_{r_0}\over\mathsf Q_{r_0}}
>a.
}
\tag{2.2}
\]

#### Proof

Branchwise safety at coefficient \(b\) gives
\[
F_{r_0}^{(b)}\ge0.
\]
Since \(F_{r_0}^{(a)}=F_{r_0}^{(b)}+(a-b)\mathsf P_{r_0}\),
\[
F_{r_0}^{(a)}\ge(a-b)\mathsf P_{r_0}.
\tag{2.3}
\]
Telescoping (1.1) from the root to depth \(r_0\) gives
\[
F_0^{(a)}-F_{r_0}^{(a)}
=\sum_{r<r_0}\Delta_r(a-\lambda_r).
\]
Therefore
\[
\sum_{r<r_0}\Delta_r(\lambda_r-a)
=F_{r_0}^{(a)}-F_0^{(a)}
>(a-b)\mathsf P_{r_0},
\tag{2.4}
\]
because the root defect is strictly negative. Divide by
\(\mathsf Q_{r_0}=\sum_{r<r_0}\Delta_r>0\) to obtain (2.1). Since the left side is a positive-\(\Delta_r\) weighted average, (2.2) follows. \(\square\)

This is the exact correction to the terminal-scale tautology: a putative counterexample cannot postpone its entire deficit to the constant/literal end of the tree if a smaller nonterminal class has already been certified.

## 3. Root-spectrum lower bound for the surviving tail currency

For the uniform cube one can quantify the reserve in (2.1) directly from the root spectrum.

Let
\[
W_k:=\sum_{|S|=k}\widehat G(S)^2.
\]
Leave a uniformly random \(m\)-subset \(R\) of coordinates alive. For a root spectral set \(S\) of size \(k\), put \(L=|S\cap R|\). Averaged physical restriction sends its contribution to the descendant Poincare currency with coefficient
\[
{1\over4}\mathbb E (L-1)_+.
\]
For \(k\ge2\),
\[
(L-1)_+\ge {2\over k}{L\choose2},
\]
because for \(L\ge2\),
\[
{2\over k}{L\choose2}
={L(L-1)\over k}\le L-1.
\]
Taking expectations and using the hypergeometric pair-survival probability,
\[
\mathbb E{L\choose2}
={k\choose2}{m(m-1)\over n(n-1)},
\]
gives
\[
\mathbb E(L-1)_+
\ge
(k-1)\theta_{m,n},
\qquad
\theta_{m,n}:={m(m-1)\over n(n-1)}.
\tag{3.1}
\]
Summing over the spectral levels yields the universal currency retention bound
\[
\boxed{
\mathsf P_{n-m}\ge\theta_{m,n}\,\mathsf P_0,
}
\tag{3.2}
\]
and therefore
\[
\boxed{
{\mathsf P_{n-m}\over\mathsf Q_{n-m}}
\ge
{\theta_{m,n}\over1-\theta_{m,n}}
=
{m(m-1)\over n(n-1)-m(m-1)}.
}
\tag{3.3}
\]
No Boolean relaxation is used here: \(\mathsf P_r\) is the exact Poincare currency of the actual random physical restrictions.

Combining Lemma 2.1 with (3.3) gives
\[
\boxed{
{1\over\mathsf Q_{n-m}}
\sum_{r=0}^{n-m-1}\Delta_r\lambda_r
>
a+(a-b)
{m(m-1)\over n(n-1)-m(m-1)}.
}
\tag{3.4}
\]

## 4. Apply the five-input certificate to the live candidate

Now set
\[
a=a^\dagger=0.268204856,\qquad b=0.01,\qquad m=5.
\]
Every branch at depth \(n-5\) has exactly five physical coordinates left, with the uniform biases inherited from the root, so the account01/B17 theorem (1.2) applies branchwise. Therefore any uniform-input gate with
\[
D_{\Gamma^\dagger}(G)<0
\]
must satisfy
\[
\boxed{
{1\over\mathsf Q_{n-5}}
\sum_{r=0}^{n-6}\Delta_r\lambda_r
>
0.268204856+
{20(0.258204856)\over n(n-1)-20}.
}
\tag{4.1}
\]
In particular, at some depth with at least six physical variables still alive,
\[
\boxed{
\lambda_r>
0.268204856+
{5.16409712\over n(n-1)-20}
>
0.268204856.
}
\tag{4.2}
\]

Equation (4.2) is the promised structural condition for the selected restriction. It is not an assumed critical-core profile. It follows from the exact signed restriction ledger plus a fully certified lower-dimensional class.

### Direct implication for an FEI counterexample

At uniform input,
\[
D_{\Gamma^\dagger}(f)
=
C^\dagger I(f)-H(f)-\Gamma^\dagger(\Pr[f=-1]).
\]
The candidate potential is nonnegative. Hence
\[
H(f)>C^\dagger I(f)
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(f)<0.
\]
Therefore every counterexample to FEI at the proposed constant \(C^\dagger\) must satisfy the nonterminal overload condition (4.1)-(4.2). This is a statement about the full uniform-cube target, not merely a read-once formula subclass.

## 5. Decisive six-variable calculation

For \(n=6\), the cutoff \(n-5=1\) leaves only the root step. Thus the weighted average in (4.1) is simply \(\lambda_0\).

The exact retained and consumed currencies are
\[
\mathsf P_1
={1\over24}\sum_{k\ge2}(5k-6)W_k,
\qquad
\mathsf Q_1
={1\over24}\sum_{k\ge2}kW_k.
\tag{5.1}
\]
Since
\[
{5k-6\over k}=5-{6\over k}\ge2
\qquad(k\ge2),
\]
we have
\[
{\mathsf P_1\over\mathsf Q_1}\ge2.
\tag{5.2}
\]
Consequently any six-input uniform gate violating the live candidate would have to obey
\[
\boxed{
\lambda_0>
a^\dagger+2(a^\dagger-0.01)
=0.784614568.
}
\tag{5.3}
\]

This is a large overload compared with the live scalar lift \(a^\dagger=0.268204856\): the root random-pivot request would have to exceed the scalar budget by more than \(0.5164\).

The compatible account03/B13 theorem
`20260922T043158Z-balanced-six-two-generation/REPORT.md`
adds a genuinely Boolean correlation restriction on the balanced slice: a balanced six-input uniform counterexample must have every singleton Walsh coefficient nonzero, hence
\[
|\widehat G(\{j\})|\ge {1\over16}\quad\forall j,
\qquad
W^{=1}(G)\ge {3\over128}.
\tag{5.4}
\]
Thus a balanced six-bit threat must lie simultaneously in the strict first-order correlation chamber (5.4) **and** satisfy the signed overload (5.3).

No finite search is promoted here: (5.3) is exact analytic arithmetic from the two consumed theorems and the hypergeometric currency identity.

## 6. Obstruction families required by the execution order

The new implication was checked against the already-known source-valid obstructions before being promoted.

* **Addressing/MUX.** The latest account01/B18 lead report closes the common-data addressing family for the same \(C^\dagger,\Gamma^\dagger\), and its newest report opens a complementary-data MUX address-bias tube. These are therefore not counterexamples to (4.1); no addressing shortcut is assumed.
* **Sparse defects.** account01/B14 `20260922T051021Z-dummy-block-sparse-defect-selector/REPORT.md` gives an explicit nonterminal dummy-tag block whose corrected residual becomes positive on the genuine sparse balanced-pair Fourier-dust tail. Thus the known sparse-defect mechanism does not falsify the safe-tail localization.
* **Tensor/decomposable gates.** account02/B17's exact composition cocycle shows corrected slack and Poincare currency compose with the same nonnegative weights. Tensoring or disjoint recursive composition cannot manufacture a worse normalized global margin than a prime factor; the theorem above does not charge a hidden component label.
* **Majority and tribes.** no special majority/tribes assumption enters the proof. If such a uniform gate were a counterexample, it would be subject to (4.1) exactly like every other Boolean gate. Existing lead measurements put the named families in slack, but the analytic theorem does not rely on those measurements.
* **Biased limits.** this report makes no all-bias claim. The five-input theorem consumed in (1.2) is a uniform-input theorem, so the universal composition-prime/all-interior-bias statement remains open. This limitation is explicit rather than hidden in the restriction.

## 7. Old and new missing implications

**Old missing implication.** The exact random-depth barycenter identified the correct signed depth average, but its only automatic endpoint was the \(n-1\) terminal level, which is the original target in disguise. It did not force the obstruction to occur at a genuinely nonterminal scale.

**New proved inference.** The complete five-input uniform certificate supplies a positive tail reserve. Therefore every uniform negative defect must generate, before the chain reaches five live variables, a signed base-correction request exceeding the live scalar coefficient. Quantitatively it must satisfy (4.1), and a six-bit counterexample would require the sharp explicit overload (5.3).

**Still missing.** Prove a source-valid upper bound/cancellation principle preventing the early nonterminal average in (4.1) from exceeding \(a^\dagger\), or construct an actual Boolean prime counterexample that realizes such an overload. For the lead's full all-bias gate candidate, the corresponding biased five-live-variable base theorem is also not yet available.

This is why the classification is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`: a genuine structural gap in the selected restriction has been removed, but the new early-overload condition has not yet been contradicted universally.

## 8. Scope

Only FEI mathematics, repository-relative source references and sanitized proof metadata are included. No credentials, machine-local paths, scheduler identifiers, email/Drive material, held-out benchmark material, public-posting action, permission change, remote workflow, or paid compute is used. No publication-priority claim is made.
