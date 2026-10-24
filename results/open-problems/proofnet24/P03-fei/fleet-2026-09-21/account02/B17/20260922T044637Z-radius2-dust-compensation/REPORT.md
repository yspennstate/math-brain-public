# account02/B17 — radius-two support rigidity and sparse-pair Fourier-dust compensation

**Run:** `20260922T044637Z-b17-radius2-dust`  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED / REPLACEMENT_MECHANISM_PROVED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source artifacts were read directly; no installed/native mathematical-brain retrieval/context was used.

## 1. Live candidate, control, and peer inputs

The later owner control keeps B12--B18 on the all-gate reformulation. The exact live fixed candidate remains

\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]

with universal missing implication

\[
\boxed{D_{\Gamma_*}(P;p)\ge 0}
\tag{1.1}
\]

for every finite composition-prime Boolean gate \(P\), every arity, and every interior product-bias vector \(p\). By the already-proved composition cocycle, (1.1) propagates to all decomposable gates; by the all-gate reformulation, that would imply full FEI with finite constant \(C_*\).

On a balanced gate at uniform bias, (1.1) reduces to

\[
D_{\Gamma_*}(G;1/2,\ldots,1/2)
=C_*[I(G)-1]-H(G),
\tag{1.2}
\]

so a balanced uniform falsifier must have \(H(G)/(I(G)-1)>C_*\).

I consumed and applied two completed other-account results.

1. **account03/B18 `20260922T035359Z-fixed-support-host-partitions`**, report blob `cbb4f5cecdd1f1f9dba695cfca0b5e1bc9173411`, proves that on the published 18-cell exceptional support \(T\), the inherited nine source pairs uniquely maximize \(H-CI\) among *all* host set partitions for every \(C>4\). It explicitly leaves changed exceptional support as the next adversarial move.
2. **account01/B14 `20260922T0425Z-core-selector-local-rigidity`**, report blob `b58c83d1267f1f8b3d6ed7c224b4786f4578b644`, proves that replacing one complete source pair by an arbitrary pair is far below \(C_*\). This leaves the first genuinely coordinated support move: remove arbitrary two old cells, possibly from different source pairs, and add two genuinely new cells.

I also consumed the newer account03/B13 handoff `20260922T043158Z-balanced-six-two-generation`, which repairs its preceding pointwise-local failure on the balanced six-bit zero-singleton slice by an exact two-generation ledger. That result is used below to motivate a source-admissible aggregate replacement for sparse local debits rather than another pointwise payment attempt.

The preceding three substantive B17 mechanisms were: the gate-slack composition cocycle, the thin shared-coordinate spine lower-bound construction, and the one-cell changed-support rigidity theorem. The present run changes the adversarial mechanism twice: first to an exhaustive symmetric-difference-four support attack, then to a general signed sparse-pair aggregate theorem.

## 2. Source geometry and exact two-cell attack

The inherited nine-core source has \(512\) rows. Its exact exceptional support is

\[
T=\{78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457\}.
\tag{2.1}
\]

Let \(P\) be the \(265\) rows on which the reconstructed signed base truth table equals \(+1\); \(T\subset P\). Let \(a_T\) denote the empty-host core obtained by zeroing the eighteen exceptional rows. Its integer Walsh numerators are \(A_T(S)\), \(S\subseteq[9]\).

For distinct \(x_1,x_2\in T\) and distinct \(y_1,y_2\in P\setminus T\), define the exact support exchange

\[
T'=(T\setminus\{x_1,x_2\})\cup\{y_1,y_2\}.
\tag{2.2}
\]

The signed Walsh update is exact:

\[
\boxed{
A_{T'}(S)=A_T(S)
+\chi_S(x_1)+\chi_S(x_2)
-\chi_S(y_1)-\chi_S(y_2).
}
\tag{2.3}
\]

There are

\[
\binom{18}{2}\binom{247}{2}
=153\cdot 30381
=\boxed{4,648,293}
\tag{2.4}
\]

such symmetric-difference-four supports. Every resulting pair-host construction is an actual Boolean gate in the inherited source geometry.

### 2.1 Host-bank bound independent of pairing

For any distinct two-cell host block \(B=\{u,v\}\), the host entropy is exactly

\[
H_B=\frac1{16}.
\tag{2.5}
\]

Its host-plus-core influence is

\[
I_B=
\begin{cases}
5/256,& |u\oplus v|=1,\\
11/512,& |u\oplus v|\ge2.
\end{cases}
\tag{2.6}
\]

Therefore *every* partition of the eighteen cells of \(T'\) into nine host pairs has total host entropy \(9/16\) and host influence at least

\[
9\cdot\frac5{256}=\frac{45}{256}.
\tag{2.7}
\]

This is deliberately optimistic for the adversary: I grant every mutated support the minimum possible host influence even when no all-edge pairing exists. Thus if

\[
\frac{H_{\rm empty}(T')+9/16}
{I_{\rm empty}(T')+45/256-1}<C,
\tag{2.8}
\]

then every actual nine-pair regrouping of \(T'\) is \(C\)-safe.

## 3. Exact finite theorem: all radius-two support mutations are below 6.48

### Theorem 3.1

For every support \(T'\) of the form (2.2), and every partition of \(T'\) into nine pair-host blocks,

\[
\boxed{
\frac{H(F_{T'})}{I(F_{T'})-1}<6.48.
}
\tag{3.1}
\]

Hence every such actual Boolean gate has a uniform-balanced \(\Gamma_*\)-slack reserve because

\[
6.48<C_*=6.5218512.
\tag{3.2}
\]

### Certificate

The checker exhausts all \(4,648,293\) supports. The empty-host Walsh numerators are integers. For every possible integer numerator \(z\), its entropy atom

\[
\phi(z)=\frac{z^2}{512^2}
\log_2\frac{512^2}{z^2}
\tag{3.3}
\]

is enclosed by rational positive-atanh logarithm bounds and then rounded outward on the dyadic scale \(2^{30}\). The width of every stored atom interval is at most one dyadic unit. All influence calculations and all final ratio comparisons are integer arithmetic.

The maximum of the **rigorous outward upper ratios** over all \(4,648,293\) supports occurs at the optimistic support exchange

\[
\{78,79\}\longrightarrow\{30,31\}.
\tag{3.4}
\]

For that support, with the optimistic host bank,

\[
I_{\rm opt}=\frac{131}{64}=2.046875,
\tag{3.5}
\]

and the checker proves

\[
6.477964853172872
<
\frac{H_{\rm upper/lower\ bracket}}{I_{\rm opt}-1}
<
\boxed{6.477965043551886}.
\tag{3.6}
\]

The exact \(6.48\)-comparison has certified margin

\[
6.48\,(I_{\rm opt}-1)-H_{\rm upper}
>0.002130345031619072.
\tag{3.7}
\]

Because the selected support already maximizes the *outward upper* ratio, (3.6)--(3.7) prove (3.1) for the entire family.

### Consequence

The published source ratio is below but extremely close to \(6.5218457109230466\), whereas every genuine symmetric-difference-four support mutation is below \(6.48\). Thus the published support has a radius-two moat of more than \(0.0418\) even before comparing with the stable center, and the stable center gap is at least

\[
6.5218512-6.477965043551886
>
\boxed{0.043886156448}.
\tag{3.8}
\]

Combined with the preceding one-cell theorem and account01/B14's complete one-source-pair replacement theorem, this removes the entire first coordinated local support neighborhood from the adversarial search.

This is a finite theorem about this exact source geometry. It does **not** prove (1.1), and it is not an FEI proof.

## 4. Why another local payment is the wrong replacement

The newest account03/B13 result is important context. Its preceding bent-swap construction showed that a pointwise local corrected restriction debit can grow without bound on genuine Boolean sources. The newer two-generation theorem proves that child slack can compensate that local debit on the balanced six-bit zero-singleton slice.

That suggests an aggregate question: can a sparse local Boolean defect be made globally dangerous merely by diluting it in many dummy coordinates?

The answer is no for the most basic balanced two-point defect. The following theorem is analytic and source-admissible; it keeps the exact signed interference rather than replacing the two restrictions by an arbitrary real relaxation.

## 5. Sparse balanced-pair Fourier-dust theorem

### Theorem 5.1

Fix a balanced Boolean function

\[
f:\{0,1\}^r\to\{\pm1\}
\]

and points \(a,b\in\{0,1\}^r\) with

\[
f(a)=+1,\qquad f(b)=-1.
\]

For \(m\ge1\), put \(n=r+m\), extend \(f\) by dummy coordinates,

\[
F_m(x,y)=f(x),
\]

and choose

\[
u=(a,0^m),\qquad
v=(b,e_1).
\]

Let \(g_m\) be obtained from \(F_m\) by flipping exactly the two values at \(u,v\). Then \(g_m\) is balanced. Put

\[
q_m=2^{2-n}.
\]

As \(m\to\infty\),

\[
\boxed{
H(g_m)-H(f)=4nq_m+O_f(q_m),
}
\tag{5.1}
\]

\[
\boxed{
I(g_m)-I(f)=nq_m+O_f(q_m).
}
\tag{5.2}
\]

Consequently,

\[
\boxed{
\frac{H(g_m)-H(f)}
{I(g_m)-I(f)}
\longrightarrow 4
}
\tag{5.3}
\]

(the denominator is positive for all sufficiently large \(m\)). In particular, for every fixed \(C>4\),

\[
\boxed{
\bigl[C(I(g_m)-1)-H(g_m)\bigr]
-
\bigl[C(I(f)-1)-H(f)\bigr]
=
(C-4)nq_m+O_f(q_m)>0
}
\tag{5.4}
\]

for all sufficiently large \(m\).

Thus sparse balanced two-point physical defects become **strictly safer**, not more dangerous, for any balanced-uniform gate center \(C>4\).

### Proof

Write a Walsh character as \(S=(T,U)\) with \(T\subseteq[r]\), \(U\subseteq[m]\), and put \(d=a\oplus b\ne0\). The dummy extension has

\[
\widehat F_m(T,U)=\widehat f(T)\mathbf1_{\{U=\varnothing\}}.
\tag{5.5}
\]

Flipping \(u\) and \(v\) changes a Walsh coefficient by

\[
2^{1-n}\bigl(\chi_S(v)-\chi_S(u)\bigr).
\tag{5.6}
\]

Since \(v=u\oplus(d,e_1)\), this vanishes when

\[
\langle T,d\rangle+U_1=0\pmod2
\]

and otherwise equals \(-q_m\chi_T(a)\). Therefore

\[
\boxed{
\widehat g_m(T,U)
=
\widehat f(T)\mathbf1_{\{U=\varnothing\}}
-
q_m\chi_T(a)
\mathbf1_{\{\langle T,d\rangle+U_1=1\}}.
}
\tag{5.7}
\]

This exact signed formula separates the old finite baseline from a Fourier-dust cloud.

Because \(d\ne0\), exactly \(2^{r-1}\) baseline frequencies \(U=0\) are active. Because the vector \((d,e_1)\) has Hamming weight at least two, the active parity hyperplane in the full \(n\)-cube contains \(2^{n-1}\) frequencies and every coordinate occurs in exactly half of them. Hence the dust set \(U\ne0\) contains

\[
N_{\rm dust}=2^{n-1}-2^{r-1}
\tag{5.8}
\]

frequencies, all with squared mass \(q_m^2\), and its total Fourier-degree sum is

\[
D_{\rm dust}
=n2^{n-2}-L_d,
\qquad
L_d:=\sum_{\langle T,d\rangle=1}|T|.
\tag{5.9}
\]

Therefore its entropy and influence are exactly

\[
H_{\rm dust}
=
(2^{n-1}-2^{r-1})q_m^2(2n-4)
=
4nq_m+O_r(q_m),
\tag{5.10}
\]

\[
I_{\rm dust}
=
(n2^{n-2}-L_d)q_m^2
=
nq_m+O_r(q_m^2).
\tag{5.11}
\]

Only the fixed set of \(2^{r-1}\) active baseline coefficients can interfere with the old spectrum. If \(\widehat f(T)\ne0\), the entropy atom
\(-x^2\log_2x^2\) is differentiable near \(\widehat f(T)\), so its change is \(O_f(q_m)\). If \(\widehat f(T)=0\), the new atom is \(q_m^2\log_2(q_m^{-2})=o(q_m)\). Summing over the fixed \(2^r\) baseline frequencies gives

\[
\Delta H_{\rm baseline}=O_f(q_m).
\tag{5.12}
\]

The baseline influence is a quadratic polynomial in the perturbed coefficients, hence

\[
\Delta I_{\rm baseline}=O_f(q_m).
\tag{5.13}
\]

Combining (5.10)--(5.13) proves (5.1)--(5.2), then (5.3)--(5.4). \(\square\)

The checker independently verifies the exact coefficient identity (5.7), the parity counts, and the dust degree count on all balanced Boolean sources through \(r\le3\), all opposite-sign point pairs, and \(m=1,2,3\): \(3,438\) exact small-source families.

## 6. Interpretation for the live candidate

Theorem 5.1 is not a universal proof of `LIMIT-PRIME-GATE-LIFT-v1`. It does make one obstruction precise.

The stable center satisfies \(C_*=6.5218512>4\). Therefore a bad pointwise restriction debit cannot be promoted to a balanced-uniform global violation simply by taking a fixed Boolean source, adding arbitrarily many dummy coordinates, and inserting one balanced opposite-sign point pair. The new Fourier dust has asymptotic entropy/influence slope exactly \(4\), while the current center charges \(6.5218512\) per unit influence. The signed baseline interference is lower order.

This is compatible with account03/B13's newer two-generation compensation theorem: local information debt can be real and large, but source-admissible descendant/global slack can absorb it. The replacement search should therefore target **coherent macroscopic interference**: overlapping/reused host channels, a changed base core, genuinely nonuniform biases, or multi-row exchanges whose size grows with the core. Isolated bounded-size sparse defects diluted in dummies are asymptotically subcritical.

The exact universal obligation remains

\[
D_{\Gamma_*}(P;p)\ge0
\quad
\text{for every composition-prime Boolean gate }P
\text{ and every }p\in(0,1)^k.
\tag{6.1}
\]

Nothing in this report closes that quantifier.

## 7. FULL-PROBLEM CHANGE / MECHANISM CHANGE

**FULL-PROBLEM CHANGE:** none. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**MECHANISM CHANGE:** yes.

- **Before:** one-cell changed-support search had closed only symmetric difference two around the 18-cell shared core; pointwise local restriction payment had separately been shown false and then repaired only on a structured six-bit slice by a two-generation ledger.
- **After:** every symmetric-difference-four support mutation in the exact 18-cell geometry is rigorously below \(6.48\) even with an unrealistically favorable host bank, and a separate analytic theorem proves that arbitrary fixed Boolean sources cannot turn one sparse balanced pair defect into a dangerous asymptotic gate margin: its incremental slope is \(4\).
- **Remaining:** a falsifier must leave this bounded local geometry, for example through growing coordinated support moves, overlap/reuse, changed base core, or genuinely nonuniform product bias; alternatively prove (6.1) by an aggregate source-admissible ledger.

The finite search establishes only its stated finite family. The sparse-pair theorem is analytic but only for the stated two-point perturbation model. Neither is a counterexample to FEI, and no novelty/publication-priority claim is made.

## 8. Verification and literature check

`CHECKER.py` exited `PASS`. It exhausts all \(4,648,293\) radius-two supports with rigorous dyadic entropy upper bounds and exact influence, and performs \(3,438\) exact small-source checks of the sparse-pair Walsh identity.

Checker SHA-256:
`5987200c99af5c0d55e12f41535cf700c3459f1fd059265c062631361c3b5bfd`.

Captured output SHA-256:
`b0acb246a35e6dbdee381aa6b86418fe9be408aa83cea2581096de4a76421f41`.

A fresh literature search on 2026-09-22 found Potapov's September 18 preprint on plateaued/partially bent functions (arXiv:2609.21563) and González--MacManus--Pereyra's May 29 stopping/restriction work (arXiv:2606.00246). Both concern structured classes/frameworks; neither source claims a universal FEI proof. This report makes no novelty claim.

Scoped privacy review: the artifacts contain only FEI mathematics, logical account/slot labels, source-bound repository paths/hashes, and aggregate run provenance. They contain no credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private material, email/Drive content, paid-model/API substitutions, public-posting actions, remote-workflow actions, or permission changes.
