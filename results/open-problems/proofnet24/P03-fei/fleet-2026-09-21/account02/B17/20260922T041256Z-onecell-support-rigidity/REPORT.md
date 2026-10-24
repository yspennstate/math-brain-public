# account02/B17 — radius-one changed-support rigidity for the 18-row prime FEI obstruction

**Run:** `20260922T041256Z-account02-B17-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / CHANGED-SUPPORT ONE-EXCHANGE ESCAPE CLOSED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and source mathematics were read, but no authenticated installed research-brain receiver context was used.

## 0. Control, last-three comparison, and live target

Fresh owner control is revision `2026-09-22.2`. The later OWNER MESSAGE converges B12--B18 on the all-gate reformulation, so it supersedes the older task wording where incompatible. The live stable post-falsifier candidate used by neighboring workers is

\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]

with the still-open universal obligation
\[
D_{\Gamma_*}(P;p)\ge0
\]
for every composition-prime Boolean gate \(P\) and every interior product bias \(p\).

The last three substantive B17 mechanisms before this run were different: hierarchical branch-surplus coding, the all-gate composition cocycle/prime reduction, and the distinguished one-coordinate shared-graft spine. The last of these raised the certified FEI lower floor above \(6.5218511673423\ldots\), but did not cross \(C_*\). This run does **not** repeat the spine recurrence. It attacks the next source-valid construction freedom identified by a completed other-account theorem: change the exceptional support of the 18-input prime gate itself.

**FULL-PROBLEM CHANGE:** none. Full FEI remains open.  
**MECHANISM CHANGE:** yes. The object is now a signed Walsh support-exchange functional on the physical 9-cube, not recursive composition/spine transport.

FLEET_RULES moves used substantively:
- **#2 ATTACK THE NEGATION FIRST:** mutate the current near-extremal prime Boolean gate before trying to prove a universal potential inequality.
- **#24 FIND THE EXTREMAL OBJECT:** test whether the published 18-row support is even locally extremal after allowing arbitrary host regrouping.
- **#30 ONE SCALE / ONE DIRECTION:** certify every radius-one support exchange exactly before opening multi-row search.

No novelty or publication-priority claim is made.

## 1. Named completed OTHER-account result consumed

The primary completed peer input is **account03/B18**,

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T035359Z-fixed-support-host-partitions/REPORT.md`

(report blob `cbb4f5cecdd1f1f9dba695cfca0b5e1bc9173411`).

It reconstructs the exact balanced 18-variable prime source gate and proves that, on its fixed exceptional support

\[
T=\{78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457\},
\]

the published nine source pairs are uniquely optimal for \(H-C(I-1)\) for every \(C>4\), even against arbitrary host-group sizes. Its stated next adversarial freedom is **changed exceptional support** (or overlap/nonuniform bias), not another fixed-\(T\) repartition.

I also preserve the newest account04/B16 joint-credit warning: cancellation/orientation must remain live until the genuine joint source is formed. Accordingly the exchange below is kept as the signed Walsh update
\[
A'(S)=A(S)+\chi_S(x)-\chi_S(y),
\]
rather than replacing it by absolute values or a sign-free relaxation.

## 2. Exact source model

Let \(g_0:\{0,1\}^9\to\{-1,+1\}\) be the exact 9-bit source truth table reconstructed from the inherited hexadecimal source. It has 265 positive and 247 negative rows, so

\[
\sum_x g_0(x)=18.
\]

Every row of \(T\) is positive. For an 18-element positive support \(U\), define the punctured empty-host core

\[
a_U(x)=
\begin{cases}
0,&x\in U,\\
g_0(x),&x\notin U.
\end{cases}
\]

Because \(|U|=18\) and all removed rows are positive, \(a_U\) has mean zero.

Partition \(U\) into nine unordered pairs \(\pi=\{B_1,\ldots,B_9\}\), introduce one independent balanced host bit for each pair, and put the corresponding host literal on the two rows in that pair. Off \(U\), keep \(g_0\). Call the resulting 18-variable Boolean gate \(F_{U,\pi}\). Every such gate is balanced.

The published support \(T\) has source pairing

\[
(78,79),(113,121),(228,484),(170,186),(149,151),
(338,466),(284,316),(291,295),(393,457),
\]

all nine pairs being Hamming-distance-one edges. The inherited source values are

\[
I(F_{T,\pi_0})=\frac{261}{128},
\qquad
\frac{H(F_{T,\pi_0})}{I(F_{T,\pi_0})-1}
=6.5218457109230465\ldots .
\]

## 3. Host-bank lemma: arbitrary regrouping can be bounded away

### Lemma 3.1

For any two distinct 9-cube rows \(u,v\), the degree-one host block supported on \(\{u,v\}\) has spectral entropy exactly

\[
H_{\{u,v\}}=\frac1{16}.
\]

Its influence is

\[
I_{\{u,v\}}=
\begin{cases}
\frac5{256},&d_H(u,v)=1,\\[1mm]
\frac{11}{512},&d_H(u,v)\ge2.
\end{cases}
\]

In particular, for **every** nine-pair partition \(\pi\) of any 18-row support,

\[
H_{\rm host}=\frac9{16},
\qquad
I_{\rm host}\ge\frac{45}{256}.
\tag{3.1}
\]

### Proof

The host-character Walsh numerator is
\[
W(S)=\chi_S(u)+\chi_S(v).
\]
Exactly half of the 512 characters have \(W(S)=0\) and half have \(|W(S)|=2\). Hence the block has 256 equal nonzero squared masses \(4/512^2\), giving entropy \(1/16\) and total spectral mass \(1/256\).

The controlling host coordinate contributes \(1/256\) to influence. If \(d_H(u,v)=1\), the parity constraint \(\chi_S(u)=\chi_S(v)\) forces one core support bit to zero and leaves the other eight unbiased, giving expected core level \(4\). If the Hamming distance is at least two, every individual core support bit remains unbiased under the one parity constraint, giving expected core level \(9/2\). This yields the two displayed influence values. QED.

The important consequence is that a changed support can be tested **optimistically** by pretending all nine host pairs are adjacent, whether or not such a perfect matching exists.

## 4. Signed one-cell exchange theorem

Let
\[
P=\{x:g_0(x)=+1\}.
\]
For \(x\in T\) and \(y\in P\setminus T\), define the radius-one support mutation

\[
T_{x\to y}=(T\setminus\{x\})\cup\{y\}.
\]

There are exactly

\[
18(265-18)=4446
\]

such mutations.

Let
\[
A_U(S)=\sum_z a_U(z)\chi_S(z)
\]
be the integer Walsh numerator of the punctured empty core. Then the mutation is the exact signed two-atom update

\[
\boxed{
A_{T_{x\to y}}(S)=A_T(S)+\chi_S(x)-\chi_S(y).
}
\tag{4.1}
\]

No sign is discarded.

Define the optimistic ratio

\[
R_{\rm opt}(U)=
\frac{H(a_U)+9/16}
     {I(a_U)+45/256-1}.
\tag{4.2}
\]

By Lemma 3.1, every actual nine-pair host realization obeys

\[
R(F_{U,\pi})\le R_{\rm opt}(U).
\tag{4.3}
\]

### Theorem 4.1 — radius-one changed-support rigidity

For every \(x\in T\), every \(y\in P\setminus T\), and every nine-pair partition \(\pi\) of \(T_{x\to y}\),

\[
\boxed{
\frac{H(F_{T_{x\to y},\pi})}
     {I(F_{T_{x\to y},\pi})-1}
<6.492.
}
\tag{4.4}
\]

Consequently the published support is a strict radius-one local maximizer in this entire source-valid support-exchange family, with certified gap from the published ratio exceeding

\[
6.5218457109230465-6.492
>0.029845710923.
\tag{4.5}
\]

### Certificate

`CHECKER.py` reconstructs \(g_0,T,A_T\) from the exact inherited source. For every one of the 4446 exchanges it computes the integer Walsh vector in (4.1), the exact influence

\[
I(a_U)=\sum_S |S|\frac{A_U(S)^2}{512^2},
\]

and a rigorous rational upper enclosure for

\[
H(a_U)=\sum_{S:A_U(S)\ne0}
\frac{A_U(S)^2}{512^2}
\log_2\frac{512^2}{A_U(S)^2}
\]

using the positive-remainder atanh series for logarithms. Pass/fail uses only rational inequalities.

With \(C=1623/250=6.492\), the worst certified exchange is \(78\to63\). Even after granting the unrealistically favorable host influence \(45/256\), the checker proves

\[
C\,[I_{\rm opt}-1]-H_{\rm opt}
>
0.00071224674763732394555413110561327447.
\tag{4.6}
\]

Here \(I_{\rm opt}=1047/512\) and the rigorous entropy upper enclosure is

\[
H_{\rm opt}<
6.78292056575236267605444586889438672553.
\]

Thus (4.4) follows.

The finite certificate proves only the explicit radius-one theorem. It is not a universal FEI computation.

## 5. Replacement mechanism: optimize the punctured core, not the host labels

The peer fixed-support theorem and Theorem 4.1 together remove two successive false degrees of freedom:

1. keeping \(T\) fixed and changing host grouping/orientation/character labels does not improve the stable obstruction;
2. changing a **single** exceptional row of \(T\) also cannot help, even if the new support is granted a globally optimal all-adjacent host pairing for free.

Therefore the next genuine construction search should no longer enumerate host labels. It should optimize the **punctured-core functional**

\[
\mathcal J_C(U)
=
H(a_U)-C\,I(a_U),
\qquad
U\subseteq P,\ |U|=18,
\tag{5.1}
\]

and only afterward add the explicit host-bank correction. Equation (4.1) makes every support exchange a signed rank-two Walsh update, so multi-row branch-and-bound or exact exchange inequalities can retain all cancellation.

For the two-row-host family, any actual candidate satisfies

\[
H(F_{U,\pi})-C[I(F_{U,\pi})-1]
\le
\mathcal J_C(U)
+rac9{16}
-C\!\left(\frac{45}{256}-1\right).
\tag{5.2}
\]

Thus a source support capable of challenging the present near-extremal gate must be at support-exchange distance at least two from \(T\) (symmetric difference at least four), or must change the empty base core / reuse hosts / move to a genuinely biased product point. This is a materially narrower adversarial search space.

This support-functional comparison is also the correct place to use the newest joint-credit lesson: the signed update \(\sum_{x\in T\setminus U}\chi_x-\sum_{y\in U\setminus T}\chi_y\) must stay intact until entropy is evaluated. A sign-free \(\ell_1\) estimate would erase precisely the cancellation the source construction exploits.

## 6. Integer-spine diagnostic, kept at finite scope

As a secondary falsification check, I recomputed the scalar fixed-point forcing for constant distinguished-spine depths \(r=1,\ldots,12\) in the exact source core. The unique best value in that tested set is again \(r=4\), with forcing approximately

\[
6.5218511673478,
\]

while \(r\ge5\) decreases toward the static 18-input source value. This is only a finite diagnostic; it is **not** promoted to an all-depth theorem. The account02/B18 global signed-singleton ceiling remains the rigorous same-core mechanism theorem.

## 7. Before/after and remaining universal implication

**Before.** account03/B18 had closed every repartition of the fixed 18-row support and explicitly left changed support as a next source-valid adversarial freedom. The known spine lower floor sat only about \(3.3\times10^{-8}\) below the live center \(C_*=6.5218512\).

**After.** Every one-cell change of the exact support is rigorously far worse: all actual pair-host realizations have excess ratio below \(6.492\). The published support is therefore not merely optimal among fixed-support recodings; it has a certified radius-one basin of width \(>0.0298\) in ratio.

**Remaining universal formula.** None of this proves

\[
D_{\Gamma_*}(P;p)\ge0
\quad
\text{for every composition-prime Boolean }P
\text{ and every }p\in(0,1)^k.
\]

Full FEI remains **OPEN / NOT PROVED**. The highest-value next adversarial move inside this construction class is a genuinely coordinated multi-row support exchange (or overlap/reuse/nonuniform bias), not another single-row mutation, host regrouping, sign flip, or integer-spine rerun.

## 8. Literature and verification boundary

Current primary literature checked this run remains consistent with open universal status: O'Donnell--Tan's composition theorem gives the disjoint composition framework; Hod's lexicographic work gives the classical \(>6.454784\) lower construction; the May 2026 restriction/stopping paper and September 2026 plateaued-function paper prove additional structured classes but not unrestricted FEI. No novelty claim is made for generic Walsh/Dirichlet identities.

`CHECKER.py` SHA-256:
`0608f99bbd355d71ff6b1dc662990563f09f84020a98f3ed8263aef444085268`

Captured verification SHA-256:
`88ea23da51bad0d935a33785282ca3556ab99d782488f4507e15d54f0e8885ee`

Scoped privacy review: the artifacts contain only FEI mathematics, repository-relative provenance, source hashes, and sanitized run metadata. They contain no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated private data, email/Drive material, paid/remote compute instructions, workflow dispatch, notification changes, or permission changes.
