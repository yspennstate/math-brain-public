# A strengthened LTF entropy bound and composition with balanced children

Date: 2026-10-02. **Complete proof, internally audited.** Research novelty
and external peer review are not certified. This continuation uses the
completed [all-LTF proof](../2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md); its longer
[candidate route](strong_ltf_and_balanced_composition_candidate.md) is
preserved separately.

All input bits are independent uniform signs. Put
\[
 H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},\quad
 I(f)=\sum_S|S|\widehat f(S)^2,\quad V(f)=1-(\mathbb Ef)^2.
\]
The quantity \(I(f)-V(f)\) is nonnegative: it is exactly
\(\sum_{S\ne\varnothing}(|S|-1)\widehat f(S)^2\).
Let \(C_*\) be the universal largest-weight split constant established in
the all-LTF proof, and define \(C_+=2\max\{C_*,8\}\).

**Theorem.** Every Boolean linear threshold function satisfies
\[
 \boxed{H(f)\le C_+[I(f)-V(f)].}
\tag{S}
\]
The same estimate, with the same universal constant, holds for every
read-once formula of arbitrary depth and size whose gates are LTFs of
arbitrary fan-in and whose nonroot outputs are balanced. The root may have
arbitrary bias. In particular these formulas satisfy ordinary FEI.

## 1. A universal near-dictator lemma for unate splits

Write any Boolean split \(f(x,z)=A(x)+zB(x)\), where the function is
increasing in \(z\). Thus \(B\in\{0,1\}\), \(A\in\{-1,0,1\}\),
and \(A^2+B^2=1\). Let \(\alpha=\mathbb EB=I_z(f)\) and
\(\delta=1-\alpha\). Set
\[
 P_S=\widehat A(S)^2+\widehat B(S)^2,\qquad
 \mathcal C=\sum_{S:P_S>0}P_Sh_2(\widehat B(S)^2/P_S).
\]
The exact split identity from the all-LTF proof gives
\(\Delta_zH(f)\le2\mathcal C\). We shall prove
\[
 \alpha>1/2\quad\Longrightarrow\quad\Delta_zH(f)\le8(1-\alpha).
\tag{N}
\]
This lemma applies to every unate split; no halfspace assumption is needed.
An output or coordinate sign change covers decreasing splits as well.

If \(\delta=0\), then \(B=1\), \(A=0\), and \(f=z\), so its
increment is zero. Otherwise \(0<\delta<1/2\). At the empty subset,
put \(a=\mathbb EA\), \(b=\mathbb EB=\alpha\),
\(P_0=a^2+b^2\). Since \(|A|=1-B\), we have \(|a|\le\delta\),
while \(P_0\ge\alpha^2\). The nonempty subsets therefore contribute
at most \(1-P_0\le1-\alpha^2\le2\delta\) to \(\mathcal C\).

The empty subset contributes
\[
 a^2\log_2(P_0/a^2)+b^2\log_2(P_0/b^2)
 \le a^2\log_2(1/a^2)+a^2\log_2e.
\]
Here \(P_0\le1\), and the second summand uses \(\ln(1+t)\le t\).
Use the convention \(0\log(1/0)=0\). Since \(a^2\le\delta^2<1/4\)
and \(t\log_2(1/t)\) increases for \(0\le t\le1/4\), this is at
most
\[
 2\delta^2\log_2(1/\delta)+\delta^2\log_2e
 \le\left(\frac{2\log_2e}{e}+\frac{\log_2e}{2}\right)\delta
 <2\delta.
\]
The bound uses \(\sup_{t>0}t\ln(1/t)=1/e\) and \(\delta<1/2\).
Thus \(\mathcal C\le4\delta\), proving (N).

## 2. Largest-weight split with a variance budget

For an LTF, flip coordinate signs to make it increasing, remove zero
weights, and remove threshold ties by moving the threshold in a finite
score gap. These operations preserve the quantities of interest. Choose
a largest input-weight coordinate and put \(\alpha=I_z(f)\).
The completed all-LTF theorem gives \(\Delta H\le C_*\alpha\).
When \(\alpha\le1/2\), this is at most
\(2C_*\alpha(1-\alpha)\). When \(\alpha>1/2\), (N) gives
\(\Delta H\le8(1-\alpha)\le16\alpha(1-\alpha)\). Consequently
\[
 \Delta_zH(f)\le C_+\alpha(1-\alpha).
\tag{L}
\]

For an increasing Boolean split, \(\mathbb EB=\alpha\), and the two
restricted means are \(\mathbb EA\pm\mathbb EB\). Direct calculation gives
\[
 V(f)-\tfrac12[V(f^+)+V(f^-)]=(\mathbb EB)^2=\alpha^2.
\tag{V}
\]
The exact influence decomposition is
\(I(f)=\alpha+\tfrac12[I(f^+)+I(f^-)]\). Hence the potential
\(I-V\) has split increment \(\alpha(1-\alpha)\).

Now induct on the number of variables. Constants and zero-variable
functions have \(H=I=V=0\). Every restriction is again an LTF. Assuming
(S) for smaller dimensions, (L) and (V) give
\[
 \begin{aligned}
 H(f)&\le C_+\alpha(1-\alpha)
       +\tfrac12[H(f^+)+H(f^-)]\\
 &\le C_+\left(\alpha-\alpha^2
       +\tfrac12[(I(f^+)-V(f^+))+(I(f^-)-V(f^-))]\right)\\
 &=C_+[I(f)-V(f)].
 \end{aligned}
\]
Sign changes preserve variance, so this applies to LTFs of arbitrary signs,
weights, and output bias. If a chosen coordinate is irrelevant, its split
increment is zero and can be omitted. The proof never divides by its
influence.

## 3. Exact closure under balanced disjoint composition

This is the balanced specialization of the established FEI composition
framework of O'Donnell and Tan (2013), including the strengthened
\(I-V\) budget; it is not claimed as a new composition theorem. We give
the exact specialization below to make the hypotheses and lack of a
biased-input assumption explicit. The additional conclusion here comes
from placing every LTF gate, with no fan-in restriction, into that framework.

Let \(F=g(f_1,\ldots,f_m)\), where the child functions use pairwise
disjoint input blocks and all satisfy \(\mathbb Ef_i=0\). Assume
\(g,f_1,\ldots,f_m\) obey \(H(h)\le C[I(h)-V(h)]\) with the same
constant. We prove the same inequality for \(F\).

The Fourier expansion gives a direct description of the spectral law:
draw \(T\) with probabilities \(\widehat g(T)^2\); for each \(i\in T\),
independently draw \(S_i\) with probabilities \(\widehat f_i(S_i)^2\);
then take the union of the selected sets. Every selected \(S_i\) is
nonempty because \(f_i\) is balanced. Thus the union determines \(T\)
and all \(S_i\), with no overlap or interference between outer terms.
Conditional entropy and expected degree give the exact identities
\[
 H(F)=H(g)+\sum_iI_i(g)H(f_i),\qquad
 I(F)=\sum_iI_i(g)I(f_i).
\tag{C}
\]
Disjoint balanced child outputs are independent uniform signs, so
\(\mathbb EF=\mathbb Eg\), \(V(F)=V(g)\), and \(V(f_i)=1\).
Since \(\sum_iI_i(g)=I(g)\),
\[
 \begin{aligned}
 H(F)&\le C\left[I(g)-V(g)+\sum_iI_i(g)(I(f_i)-1)\right]\\
 &=C[I(F)-V(F)].
 \end{aligned}
\]
This proves exact closure with no loss in the constant.

Apply the closure from the leaves upward in a read-once LTF formula.
Leaves are balanced variables or their negatives, with \(H=0\), \(I=V=1\).
All nonroot children are balanced by assumption, while every gate satisfies
the strengthened LTF theorem. The same \(C_+\) therefore works throughout
the entire formula, independently of fan-in, size, or depth. The root need
not be balanced.

## 4. Scope and verification

This covers disjoint read-once formulas; shared-input circuits are not
covered. Balanced children are required: arbitrary biased children induce
a nonuniform product input law at a parent, which this proof does not
address. Nothing here claims a variance-normalized FEI theorem for arbitrary
biased input measures. The general Boolean FEI conjecture remains outside
the proved class.

The near-dictator lemma is elementary. The only non-elementary inputs are
those already sourced and audited in the all-LTF proof: Keller–Klein's
maximum-influence theorem, KOS's biased-halfspace noise bound, and uniform
cube hypercontractivity. The composition identities are derived above.

The composition framework is due to Ryan O'Donnell and Li-Yang Tan,
*A composition theorem for the Fourier Entropy-Influence conjecture*,
ICALP 2013: <https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf>.
The balanced identities are reproduced here only for self-contained
verification. The research-priority statement concerns the LTF gate bound
and its resulting unbounded-fan-in subclass, not generic composition.

Independent internal audits are recorded in
[the strengthened-proof audit](strong_ltf_composition_independent_audit.md)
and [the separate algebra audit](strong_ltf_balanced_composition_k_audit.md).
They also verify the longer complementary-KL proof in the preserved
candidate. These audits do not establish external acceptance or novelty.

The [separate checker](verify_strong_ltf_composition.py) and
[results](strong_ltf_composition_checks.json) exhaustively check 7,778
monotone functions through dimension five, 3,488 near-dictator splits,
401 LTF examples, and 150 composition nodes including 90 formula roots
through 13 leaves. The exact composition identity error was below
\(4\times10^{-15}\). There are also
[independently written checks](independent_strong_ltf_check.py) with
[their own results](independent_strong_ltf_checks.json).
