# fleet02/B14 — sharp coherent-recombination payment in Poincare currency

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository/control context was consumed through the authorized connector, but no authenticated cognitive-brain retrieval/runtime entered the mathematics.  
**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. **Configured/known reasoning level:** UNKNOWN / not exposed. **Provider usage/thinking time:** not exposed.

## 0. Control change, predecessor comparison, and exact missing implication

Fresh owner control revision `2026-09-22.2` supersedes the older selector-specific task text and orders the FEI fleet to converge on the all-gate reformulation. The proposed read-once-potential AND/decomposable extremality has already been rigorously refuted, so this run does **not** rescan that dead claim.

Named completed **other-account** results actually consumed:

1. `fleet04/B12/20260922T0127Z-two-step-quadratic-refund/REPORT.md`, blob `42eca23e9ead06095b2fca98bf3b4999c1af23ce`: on the certified arity-10 balanced obstruction, the unique bad one-step pure-quadratic restriction is uniformly repaired by every legal second step. The exact currency is the Poincare drop `Q` from the fleet02/B16 martingale ledger.
2. `fleet04/B13/20260922T0120Z-balanced-restriction-atom/REPORT.md`, blob `e8d32e431be87ac5875048e11012bcf3d2a51df5`: that same arity-10 obstruction has no proper balanced codimension-one or codimension-two descendant and no proper balanced descendant carrying its positive old-base margin. Hence a useful restriction proof must keep genuinely unbalanced excursions rather than rebalance after each split.
3. The source witness itself is `fleet03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`, blob `d12fe592f4fa6db16cb571557f6cc41392dd5860`.

The exact all-depth currency identity used below is the completed fleet02/B16 result `20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`.

The last three B14 mechanism families (`20260921T220126Z-stationary-trigger-selector`, `20260921T230653Z-asymmetric-shortcircuit-ledger`, and `20260922T000131Z-diagonal-tag-transfer-selector`) all left the same target-level fact unpaid: a globally summable physical restriction numerator. This run changes the mechanism rather than renaming that gap: it works in the exact Poincare currency `Q` and proves that the entire coherent Jensen-Shannon part is globally summable with a **sharp constant**. Only the erasure part remains.

FLEET_RULES moves used: **2** (attack the negation first: exhaustive search for a violation), **24** (find the extremal object: two-input AND/OR attains equality), and **25** (count the same quantity twice: Fourier harmonic overlap versus physical pivotal variance).

## 1. Normalization and the exact restriction pieces

Let `g:{-1,1}^m->{-1,1}` and physically restrict coordinate `i`. Write the two children as `g_+` and `g_-` and set

\[
a=\frac{g_++g_-}{2},\qquad b=\frac{g_+-g_-}{2}.
\tag{1.1}
\]

Pointwise, because `g_+,g_-` are Boolean,

\[
a,b\in\{-1,0,1\},\qquad ab=0,\qquad a^2+b^2=1.
\tag{1.2}
\]

Let `A_S=\widehat a(S)`, `B_S=\widehat b(S)`, and

\[
d=\mathbb E b^2=\operatorname{Inf}_i(g).
\tag{1.3}
\]

The child spectral laws are

\[
\mu_\pm(S)=(A_S\pm B_S)^2,
\tag{1.4}
\]

and their equal mixture is `m_S=A_S^2+B_S^2`. The exact restriction entropy identity is

\[
\Delta_i H=B_i+JS_i,
\tag{1.5}
\]

where `B_i` is the spectral erasure term and `JS_i=JS(\mu_+,\mu_-)` is the coherent recombination term.

For the Poincare potential

\[
P(g)=\frac{I(g)}4-q_g(1-q_g),\qquad q_g=\Pr[g=-1],
\tag{1.6}
\]

the exact one-step currency is

\[
Q_i=P(g)-\frac{P(g_+)+P(g_-)}2
=\frac14\left(d-(q_+-q_-)^2\right).
\tag{1.7}
\]

Since `q_+-q_-=-\mathbb E b`,

\[
\boxed{4Q_i=\operatorname{Var}(b)=d-(\mathbb E b)^2.}
\tag{1.8}
\]

This is the same source currency used in the all-depth martingale ledger; no surrogate influence is introduced.

## 2. Scalar entropy lemma

For `|r|<=1/2`,

\[
\boxed{1-h_2(1/2+r)\le 4r^2.}
\tag{2.1}
\]

A short proof: put `u=2|r|` and

\[
F(u)=h_2\!\left(\frac{1+u}{2}\right)-1+u^2,\qquad 0\le u\le1.
\]

Then `F(0)=F(1)=0` and

\[
F'(u)=2u-\frac{\operatorname{artanh}u}{\ln2},
\qquad
F''(u)=2-\frac1{\ln2\,(1-u^2)}.
\]

`F''` decreases from `2-1/ln2>0` to `-infinity`, so `F'` first increases from zero and then decreases to `-infinity`, crossing zero exactly once in `(0,1)`. Hence `F` increases and then decreases between equal zero endpoints and is nonnegative. This is (2.1).

## 3. Harmonic-overlap lemma from physical Booleanity

For nonnegative numbers

\[
x_S=A_S^2,\qquad y_S=B_S^2,
\]

Parseval and (1.2) give

\[
\sum_Sx_S=1-d,\qquad \sum_Sy_S=d.
\tag{3.1}
\]

Using

\[
\frac{x y}{x+y}
=\frac14\left[(x+y)-\frac{(x-y)^2}{x+y}\right]
\]

and Cauchy-Schwarz,

\[
\sum_S\frac{(x_S-y_S)^2}{x_S+y_S}
\ge
\frac{(\sum_Sx_S-\sum_Sy_S)^2}{\sum_S(x_S+y_S)}
=(1-2d)^2.
\]

Therefore

\[
\sum_S\frac{A_S^2B_S^2}{A_S^2+B_S^2}
\le d(1-d).
\tag{3.2}
\]

But `b` is a signed indicator of the pivotal set: `|b|=b^2` pointwise. Hence

\[
|\mathbb E b|\le\mathbb E|b|=d,
\]

so

\[
d(1-d)\le d-(\mathbb E b)^2=\operatorname{Var}(b).
\tag{3.3}
\]

Combining (3.2)-(3.3),

\[
\boxed{
\sum_S\frac{A_S^2B_S^2}{A_S^2+B_S^2}
\le\operatorname{Var}(b).
}
\tag{3.4}
\]

This is where genuine Boolean physical structure enters. An arbitrary pair of orthogonal Fourier vectors does not satisfy the needed conclusion.

## 4. Main theorem — sharp `JS_i <= 16 Q_i`

For every Boolean `g` and every physical coordinate `i`,

\[
\boxed{JS_i(g)\le16Q_i(g).}
\tag{4.1}
\]

### Proof

For a fibre with `m_S=A_S^2+B_S^2>0`, the posterior branch probability in the equal child mixture is

\[
\frac{\mu_+(S)}{\mu_+(S)+\mu_-(S)}
=\frac12+\frac{A_SB_S}{A_S^2+B_S^2}.
\]

Thus

\[
JS_i
=\sum_Sm_S\left[
1-h_2\!\left(\frac12+\frac{A_SB_S}{m_S}\right)
\right].
\]

Apply (2.1) fibrewise and then (3.4):

\[
JS_i
\le4\sum_S\frac{A_S^2B_S^2}{A_S^2+B_S^2}
\le4\operatorname{Var}(b).
\]

By (1.8), `Var(b)=4Q_i`, proving (4.1). `square`

### Sharpness

For the two-input AND/OR gate at uniform input and either relevant coordinate,

\[
JS_i=1,\qquad Q_i=\frac1{16},
\]

so equality holds in (4.1). Therefore the constant `16` cannot be improved in this universal one-step statement.

This does **not** assert any prescribed-coordinate erasure bound. The known fixed-coordinate erasure counterexamples remain untouched: only the coherent `JS` term is controlled for every coordinate.

## 5. Global adaptive-tree corollary — every recombination refund is paid once

Take any finite adaptive physical restriction tree that eventually reaches affine leaves. At each visited node `r`, let `Q_r`, `B_r`, `JS_r` denote the currency, erasure and coherent terms of the selected physical coordinate.

The fleet02/B16 exact currency telescope gives

\[
P(f)=\mathbb E\sum_r Q_r.
\tag{5.1}
\]

Entropy telescopes because affine leaves have spectral entropy zero:

\[
H(f)=\mathbb E\sum_r(B_r+JS_r).
\tag{5.2}
\]

Applying (4.1) node by node yields the policy-independent global bound

\[
\boxed{
\mathbb E\sum_r JS_r\le16P(f).
}
\tag{5.3}
\]

For a balanced root, `P(f)=(I(f)-1)/4`, hence

\[
\boxed{
\mathbb E\sum_r JS_r\le4\,[I(f)-1].
}
\tag{5.4}
\]

So the coherent recombination term is **not** the source of an unbounded balanced FEI ratio: under every adaptive physical policy it has an exact globally summable budget, with each local refund charged once in the Poincare currency.

The remaining numerator is purely erasure:

\[
\boxed{
H(f)\le \mathbb E\sum_r B_r+4[I(f)-1]
\qquad (f\ \text{balanced}).
}
\tag{5.5}
\]

The additive `4` in (5.5) is a coherent-recombination surcharge. It is **not** the previously refuted claim that the erasure constant itself is four.

## 6. A source-exact adaptive erasure constant and the new FEI sandwich

Define

\[
K_{\rm tree}
:=\sup_{\substack{f\ \mathrm{balanced}\\ I(f)>1}}
\inf_{\pi}
\frac{\mathbb E_\pi\sum_r B_r}{I(f)-1},
\tag{6.1}
\]

where `pi` ranges over finite adaptive **physical** restriction policies ending at affine leaves. No affine coordinate change, sign-free spectral relaxation, or prescribed-coordinate selector is allowed.

The balanced-excess equivalence consumed by the current gate programme says

\[
C_{FEI}
=
\sup_{f\ \mathrm{balanced}, I(f)>1}
\frac{H(f)}{I(f)-1}.
\tag{6.2}
\]

Since the cumulative erasure is nonnegative and at most the total telescoping entropy, (5.5)-(6.2) give

\[
\boxed{
K_{\rm tree}\le C_{FEI}\le K_{\rm tree}+4.
}
\tag{6.3}
\]

This is the actual target-level change of the run: the universal conjecture is reduced, up to a sharp dimension-free coherent surcharge `4`, to a **pure adaptive erasure** problem in the exact restriction currency. The restriction policy can pass through unbalanced descendants, which is necessary by the fleet04/B13 balanced-atom theorem.

A proof that `K_tree<infinity` would therefore prove full FEI, with the explicit bound

\[
H(f)\le(K_{\rm tree}+4)I(f)
\]

(and the sharper balanced form `(K_tree+4)(I-1)`). No such finiteness proof is supplied here.

## 7. Relation to the certified two-step obstruction/refund

The fleet04/B12 arity-10 calculation showed a concrete bad first quadratic step whose deficit is repaired at depth two. Theorem (4.1) explains one part of why such repairs can telescope safely: coherent child-spectrum distinguishability is automatically priced in exactly the same `Q` currency used by the continuation ledger. The theorem does **not** by itself explain or bound the erasure part of that two-step witness, and therefore does not promote the finite calculation to a universal depth-two theorem.

Similarly, fleet04/B13 proves the witness is a balanced-restriction atom. The global corollary here does not attempt to return to balance after one or two restrictions; (4.1) applies at every genuinely unbalanced node, so the whole unbalanced excursion is admissible and its coherent charge is still globally paid.

## 8. Sanity check and primary-literature status

`check_js_poincare_currency.py` exhaustively checked every nonconstant Boolean function through four variables and every coordinate: `262,928` coordinate cases, `261,846` with positive currency. The maximum observed `JS_i/Q_i` is exactly `16`, attained already by the two-input AND/OR geometry. This is regression evidence only; Sections 2-5 are the all-dimensional proof.

Current primary-source checks (22 September 2026) still leave full FEI open. González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), explicitly develop restriction-decrement/stopping-tree methods and do not prove the universal conjecture. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued and partially bent classes, not universally. No novelty or publication-priority claim is made for (4.1), (5.3), or (6.3); the bounded search did not establish priority.

## 9. Before/after and exact remaining obligation

**FULL-PROBLEM CHANGE:** no full proof; `C_FEI<infinity` is still unproved.  
**MECHANISM CHANGE:** yes, and it applies to the exact missing restriction numerator.

Before this run, the gate/restriction ledger had a globally telescoping denominator `Q` but the coherent Shannon term was controlled only by influence/folded-influence envelopes that need not telescope in the same currency. After this run,

\[
JS_i\le16Q_i
\]

holds at **every physical restriction node**, sharply, so all coherent recombination over an arbitrary adaptive tree costs at most `16P(root)` exactly once.

The first remaining implication is now unambiguous:

\[
\boxed{
\text{construct a physical adaptive policy with }
\mathbb E\sum_r B_r\le K[I(f)-1]
\text{ for every balanced Boolean }f,
}
\tag{9.1}
\]

for one finite dimension-independent `K`, or build a genuine Boolean family showing this particular tree-erasure formulation cannot have finite `K`. Equation (6.3) proves that (9.1), if established, closes full FEI with constant `K+4`.
