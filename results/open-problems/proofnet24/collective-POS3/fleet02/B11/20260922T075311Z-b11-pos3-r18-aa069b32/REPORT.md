# POS3 fleet02/B11 r18 — incomparability articulations collapse to a one-leaf interface after span descent

**Run:** `20260922T075311Z-b11-pos3-r18-aa069b32`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are under the uniform law on all full linear extensions of the original finite poset. No deletion-induced distribution is silently replaced by a uniform law.

## 1. Fresh state and mechanism change

Fresh owner controls were resolved from `yspennstate/math-research-brain` at initial main
`c9318536d273284e720d580b795f4b204cecf098` and refreshed before scientific writes at
`2026-09-22.2`; `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` remains active and new
installation/benchmark work remains stopped.

The latest complete campaign-lead version consumed is fleet04/B10 r17,
`proofnet24/collective-POS3/fleet04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`,
blob `61c94984acd303d2fbed96f2f3bb77664a51297b`. It reduces its same-ray exception to a
coherent width-saturating three-antichain gate.

The named OTHER-account result consumed and applied is fleet03/B19
`20260922T070336Z-b19-pos3-r11-same-ray-export`, whose scientific report proves that a
same-ray gate cannot recycle inside its present strong-order envelope: it must export
one or two new relation distinguishers unless strict span descent occurs. Its first
remaining statement is `CROSS-ENVELOPE REUSE EXCLUSION`.

The preceding B11 run attacked leaf capacity. This run changes mechanism: it treats
**cut vertices of the incomparability graph** and derives an exact ordinal-corridor
normal form. This directly targets the assigned minimal-counterexample /
ordinal-decomposition reduction rather than another local packet estimate.

## 2. Incomparability articulation normal form

Let \(P\) be a cardinality-minimal width-at-most-three counterexample to POS3. Use the
already-established reduction that the incomparability graph \(\operatorname{Inc}(P)\)
is connected. Suppose \(v\) is a cut vertex of \(\operatorname{Inc}(P)\), and let
\[
Q_1,\ldots,Q_k
\]
be the connected components of \(\operatorname{Inc}(P-v)\), ordered so that
\[
P-v = Q_1\oplus Q_2\oplus\cdots\oplus Q_k. \tag{2.1}
\]
The ordering exists because two distinct incomparability components are uniformly
comparable.

### Lemma 2.1 — only the two boundary components can compare with the cut vertex

Every component \(Q_i\) contains an element incomparable with \(v\). Moreover
\[
\operatorname{Pred}(v)\subseteq Q_1,\qquad
\operatorname{Succ}(v)\subseteq Q_k, \tag{2.2}
\]
and \(v\) is incomparable with every element of every interior component
\(Q_i\), \(1<i<k\).

**Proof.**
If \(v\) had no incomparability edge into some \(Q_i\), then \(Q_i\) would remain a
separate connected component even after \(v\) is restored, contradicting connectedness
of \(\operatorname{Inc}(P)\).

Suppose \(q<v\) with \(q\in Q_i\), \(i\ge2\). Choose
\(r\in Q_{i-1}\) with \(r\parallel v\). By (2.1), \(r<q<v\), contradiction.
Thus no predecessor of \(v\) occurs after \(Q_1\). The successor statement is dual.
An interior element is therefore neither below nor above \(v\), hence is incomparable
with \(v\). \(\square\)

### Lemma 2.2 — exact uniformity of every interior marginal

For \(1<i<k\), the restriction of a uniform random full extension of \(P\) to \(Q_i\)
is the **uniform** law on \(L(Q_i)\).

**Proof.**
A linear extension of \(P-v\) is the concatenation
\[
\lambda_1\lambda_2\cdots\lambda_k,\qquad \lambda_i\in L(Q_i).
\]
By Lemma 2.1, all predecessor constraints on the insertion of \(v\) occur in
\(\lambda_1\), all successor constraints occur in \(\lambda_k\), and \(v\) is
incomparable with every interior element. Consequently, for fixed
\(\lambda_1,\lambda_k\), the number of legal insertion places for \(v\) depends on
those two boundary extensions and on the fixed sizes of the interior blocks, but not
on the internal order of any \(\lambda_i\), \(1<i<k\). Summing over the two boundary
extensions gives the same multiplicity to every member of \(L(Q_i)\). \(\square\)

### Corollary 2.3 — interior components are singletons

Every interior \(Q_i\) is a singleton.

**Proof.**
If an interior \(Q_i\) were a nonchain, it is a smaller width-at-most-three nonchain
poset. Cardinality minimality supplies a balanced pair under the uniform law on
\(L(Q_i)\), and Lemma 2.2 transfers the same pair probability unchanged to \(P\),
contradiction. Hence \(Q_i\) is a chain. But a connected component of an
incomparability graph which is a chain can have only one vertex. \(\square\)

Thus every incomparability articulation has the exact form
\[
P-v=Q_1\oplus\{z_1\}\oplus\cdots\oplus\{z_m\}\oplus Q_k,
\qquad m=k-2. \tag{2.3}
\]
Each \(z_j\) is an incomparability-graph leaf whose unique incomparable neighbour is
\(v\).

## 3. Exact corridor increments

Put
\[
W=e(Q_1)e(Q_k),\qquad E=e(P),\qquad
p_j=\Pr_P(v<z_j).
\]
For consecutive interior vertices,
\[
p_{j+1}-p_j=\frac{W}{E}. \tag{3.1}
\]

**Proof.**
Because \(z_j<z_{j+1}\),
\[
N(v<z_{j+1})-N(v<z_j)=N(z_j<v<z_{j+1}).
\]
For each pair of boundary extensions
\((\lambda_1,\lambda_k)\in L(Q_1)\times L(Q_k)\), insertion of \(v\) in the unique
gap between \(z_j,z_{j+1}\) is legal: all possible predecessors in \(Q_1\) are
already before \(v\), all possible successors in \(Q_k\) are after \(v\), and all
interior vertices are incomparable with \(v\). Hence the middle event has exactly
\(W\) full extensions. \(\square\)

There are also \(m+1\) always-legal universal gaps for \(v\): immediately after
\(Q_1\), each of the \(m-1\) gaps between consecutive \(z_j\), and immediately before
\(Q_k\). Therefore
\[
E\ge(m+1)W,\qquad
\delta:=\frac{W}{E}\le\frac1{m+1}. \tag{3.2}
\]

## 4. Strong-majority order forces a single corridor orientation

In a no-balanced poset define \(u\prec_*w\) by the poset order when \(u<w\), and for
incomparable \(u,w\) by
\[
u\prec_*w \iff \Pr(u<w)>2/3.
\]
This is a total transitive order. Indeed, a directed triangle
\(u\prec_*w\prec_*t\prec_*u\) would give three events, each of probability strictly
greater than \(2/3\) (or equal to one for a comparable relation). The sum of their
complement probabilities is strictly below one, so some full extension would realize
all three cyclic inequalities simultaneously, impossible.

Since \(z_1<\cdots<z_m\), the point \(v\) occupies a single cut in this total order.
If \(m\ge2\) and that cut lay between \(z_j\) and \(z_{j+1}\), then
\[
p_j<1/3,\qquad p_{j+1}>2/3,
\]
so (3.1) would give
\[
\delta=p_{j+1}-p_j>1/3.
\]
But (3.2) gives \(\delta\le1/(m+1)\le1/3\), contradiction. Hence for \(m\ge2\)
all interior leaves lie on the same strong-majority side:
\[
v\prec_*z_1\prec_*\cdots\prec_*z_m
\quad\text{or}\quad
z_1\prec_*\cdots\prec_*z_m\prec_*v. \tag{4.1}
\]

## 5. Applying the preceding B11 leaf theorem: at most one interior level survives terminal descent

The immediately preceding B11 theorem states: for an incomparability leaf \(x\) with
unique neighbour \(b\), if \(b\prec_*x\), then after balanced pairs and strict
strong-majority span descent are excluded, the maximal elements of
\[
\operatorname{Pred}(x)\setminus\operatorname{Pred}(b)
\]
must consist of **exactly two** Hasse predecessors. The order-dual statement holds
when \(x\prec_*b\).

Assume the first orientation in (4.1) and \(m\ge2\). Apply that theorem to the leaf
\(x=z_2\), \(b=v\). Every element of \(Q_1\) lies below \(z_1\), so regardless of
which boundary elements lie below \(v\),
\[
\max\bigl(\operatorname{Pred}(z_2)\setminus\operatorname{Pred}(v)\bigr)=\{z_1\}.
\]
Moreover \(z_1\lessdot z_2\). Thus the required terminal double fan is impossible:
the state must already contain a balanced pair or strict span descent.

In the second orientation, apply the order-dual statement to \(x=z_1\), \(b=v\).
Every element of \(Q_k\) lies above \(z_2\), and
\[
\min\bigl(\operatorname{Succ}(z_1)\setminus\operatorname{Succ}(v)\bigr)=\{z_2\}.
\]
Again the terminal double fan is impossible.

Therefore:

> **Articulation-corridor reduction.** In a cardinality-minimal POS3 counterexample,
> after the collective strict strong-majority span-descent mechanism has been
> exhausted, every cut vertex \(v\) of the incomparability graph satisfies
> \(k\le3\). Equivalently,
> \[
> P-v=Q_1\oplus Q_2
> \]
> or
> \[
> P-v=Q_1\oplus\{z\}\oplus Q_3,
> \]
> with \(z\) an incomparability leaf adjacent only to \(v\).
> Otherwise strict span descent is forced.

This is arbitrary-size and uses the exact full-extension law.

## 6. Application to the named partner and lead

Fleet03/B19's current `CROSS-ENVELOPE REUSE EXCLUSION` says that a same-ray export
cannot close inside its present envelope; any surviving cycle must reuse a vertex
from an earlier/larger envelope or alternate rays.

The theorem above applies directly whenever such reuse is mediated by an
incomparability articulation. It excludes a hidden multi-level ordinal corridor:
two or more interior levels force strict span descent. Thus an articulation-mediated
reuse can survive only through a **two-boundary interface** or a
**two-boundary-plus-one-leaf interface**. Otherwise the propagation takes place
inside a 2-connected incomparability-graph block.

This also interfaces with fleet04/B10 r17's coherent three-antichain gate: any
attempt to send the coherent gate through an articulation has only those two residual
interface types after descent exhaustion. The lead/partner global recycling problem
therefore need not track arbitrarily long ordinal corridors behind a cut vertex.

## 7. Counterexample to a tempting stronger shortcut

An incomparability articulation need not itself have a balanced incident pair.

Take the five-element poset with Hasse covers
\[
0<3,\quad0<4,\quad1<2,\quad1<4,\quad2<3.
\]
It has width two (hence at most three), both comparability and incomparability graphs
connected, and \(v=2\) is a cut vertex of the incomparability graph. Removing \(v\)
leaves the two incomparability components
\[
Q_1=\{0,1\},\qquad Q_2=\{3,4\}.
\]
There are \(E=8\) full linear extensions, with
\[
N(2<0)=2,\qquad N(2<4)=6.
\]
Thus both incomparable pairs incident to \(v\) are unbalanced (\(1/4\) and \(3/4\)).
Balanced pairs exist elsewhere:
\[
N(0<1)=3,\qquad N(3<4)=3,
\]
so both have probability \(3/8\). This refutes only the stronger cut-vertex-local
shortcut, not POS3, and shows that the residual boundary-block cases are genuine.

## 8. Exact regression

The independent exact-arithmetic verifier exhaustively enumerated all distinct
naturally labelled transitively closed posets on \(2\le n\le6\). It checked the
component order, boundary localization, exact interior uniform marginal, singleton
corridor increment, and the adversary above.

```text
POS3_ARTICULATION_CORRIDOR_V1_PASS
posets=5230
width_le3=3701
inc_connected=2937
inc_cut_states=2236
interior_components_checked=403
nontrivial_interior=65
singleton_corridor_states=279
universal_gaps_checked=47
adversary_covers=(0,3),(0,4),(1,2),(1,4),(2,3)
adversary_E=8
articulation_v=2
N(v<0)=2
N(v<4)=6
balanced_elsewhere_N(0<1)=3
balanced_elsewhere_N(3<4)=3
```

Verifier SHA-256:
`db9c3b9cd195a2e257220755a77c0e09e5aea20b88410e98b36a8ff3459d8cad`.

Captured stdout SHA-256:
`49dce621a54e1ccc1b437d0ad5f8ab82ae20ec8cc862b5979ee05737b2f0bbac`.

The finite census is a regression check for the symbolic theorem, not a closure
argument. The verifier exited zero and printed the PASS terminator.

## 9. First genuinely unresolved implication

The first unpaid articulation statement is now:

> **ONE-LEAF / TWO-BOUNDARY ARTICULATION EXIT.** In a cardinality-minimal,
> series- and parallel-indecomposable, span-descent-exhausted no-balanced
> width-three poset, exclude the remaining incomparability-cut shapes
> \(P-v=Q_1\oplus Q_2\) and
> \(P-v=Q_1\oplus\{z\}\oplus Q_3\), or prove that every surviving global
> coherent-gate/cross-envelope reuse occurs inside a 2-connected
> incomparability block.

This is materially narrower than the partner's arbitrary cross-envelope reuse
problem, but it is not yet proved. POS3 therefore remains open.

## 10. Integrity

No benchmark work or sealed material was touched. No credential, scheduler identifier,
machine path, unrelated private datum/transcript, email, Drive, public post, paid
API/model/Codex call, workflow dispatch, permission change, or deletion-induced-uniform
substitution was used.

Model self-report: `GPT-5.6 Sol`.  
Requested reasoning: `maximum actually supported`.  
Configured/known reasoning effort: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning-token/time counters: `null / NOT_EXPOSED`.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The current account inventory was inspected read-only: the twenty managed B01--B20
slots are enabled, hourly, role-aligned and quiet; no deficit was found and B11 made
no scheduler mutation. The canonical brain-status login write was attempted after
the fresh control read but denied by the platform safety layer; it was not bypassed
or fabricated later. The scientific start record is immutable and records that
failure honestly.
