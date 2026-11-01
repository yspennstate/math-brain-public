# Universal split deficit and balanced composition of parallel-slab gates

Date: 2026-10-02. **Candidate general lemma, independent audit requested.**
This removes unateness from the short near-dictator step in
`strong_ltf_and_balanced_composition_proof.md`. Generic balanced
composition is established by O'Donnell–Tan (2013); no new composition
theorem is claimed. The intended additional application is to the newly
proved class of parallel-slab gates.

All inputs are independent uniform signs. Write \(V(f)=\operatorname{Var}(f)\)
and use base-2 spectral entropy.

## Generic local conversion

For any Boolean split \(f=A+zB\), let
\[
 \alpha=\mathbb EB^2,\quad\beta=\mathbb EB,\quad
 \delta=1-\alpha,\quad\nu=\alpha-\beta^2.
\]
Pointwise, \(A,B\in\{-1,0,1\}\), \(A^2+B^2=1\), \(AB=0\), and
\(\mathbb E|B|=\alpha\). Consequently
\(|\beta|\le\alpha\), \(|\mathbb EA|\le\delta\), and
\[
 \nu\ge\alpha(1-\alpha)=\alpha\delta\ge0.
\tag{1}
\]
Let \(P_S=\widehat A(S)^2+\widehat B(S)^2\) and let
\(\mathcal C=\sum_SP_Sh_2(\widehat B(S)^2/P_S)\), omitting zero-mass
subsets. We derive the universal split estimate explicitly. For one pair
\(a=\widehat A(S)\), \(b=\widehat B(S)\), \(P=a^2+b^2>0\), put
\(q=b^2/P\), \(r=(a+b)^2/(2P)\). Its full entropy contribution is
\(-P\log_2P+Ph_2(q)\); its average restricted contribution is
\(-P\log_2(2P)+Ph_2(r)\). Therefore
\[
 \Delta_zH(f)=\sum_SP_S[1+h_2(q_S)-h_2(r_S)].
\]
Since \(r(1-r)=(1-2q)^2/4\) and \(h_2(t)\ge4t(1-t)\),
\(1-h_2(r)\le4q(1-q)\le h_2(q)\). Thus \(\Delta_zH(f)\le2\mathcal C\).
For an elementary verification of the binary inequality, the positive series
\[
 1-h_2((1+x)/2)=\frac1{\ln2}\sum_{j\ge1}
               \frac{x^{2j}}{(2j)(2j-1)}
\]
has coefficients summing to 1, so it is at most \(x^2\) on \([-1,1]\).

Suppose \(\alpha>1/2\). If \(\delta=0\), then \(A=0\) and
\(f=zB\), where \(B\) is Boolean. The two restrictions are \(\pm B\)
and the full spectral law merely appends \(z\), so the entropy increment
is zero. Otherwise \(0<\delta<1/2\). The empty pair has mass
\(P_0=(\mathbb EA)^2+\beta^2\ge\beta^2\), so the nonempty subsets
contribute at most \(1-\beta^2=\nu+\delta\) to \(\mathcal C\).

Writing \(a=\mathbb EA\), its empty-subset contribution is
\[
 a^2\log_2(P_0/a^2)+\beta^2\log_2(P_0/\beta^2)
 \le a^2\log_2(1/a^2)+a^2\log_2e
 \le2\delta^2\log_2(1/\delta)+\delta^2\log_2e
 <2\delta.
\]
Indeed \(P_0\le1\), the other summand is at most \(a^2\log_2e\) by
\(\ln(1+t)\le t\), and \(t\log_2(1/t)\) increases on \([0,1/4]\).
The final strict bound follows from
\[
 2\delta\log_2(1/\delta)+\delta\log_2e
 \le\frac{2\log_2e}{e}+\frac{\log_2e}{2}<2.
\]
This calculation does not use the sign of \(B\). If \(\beta=0\), its
zero summand is omitted and these inequalities remain valid. Zero
coefficients otherwise use the usual continuous conventions. Therefore
\[
 \mathcal C\le\nu+3\delta\le7\nu,
 \qquad\Delta_zH(f)\le14\nu,
 \quad(\alpha>1/2),
\tag{2}
\]
where (1) gives \(\delta\le2\nu\).

If the original local estimate \(\Delta_zH(f)\le C\alpha\) holds and
\(\alpha\le1/2\), (1) gives \(\nu\ge\alpha/2\), so
\(\Delta_zH(f)\le2C\nu\). At \(\alpha=0\), the restrictions coincide
and \(\Delta H=\nu=0\). Combining all regimes proves
\[
 \boxed{\Delta_zH(f)\le K[\alpha-(\mathbb EB)^2],
 \qquad K=\max\{2C,14\}.}
\tag{3}
\]
The high-influence branch is universal for all Boolean functions; the
low-influence branch retains exactly the hypothesized local entropy bound.

## Restriction induction

Let \(\mathcal F\) be a restriction-closed Boolean class. Suppose every
nonconstant \(f\in\mathcal F\) has a splitting coordinate satisfying
\(\Delta H\le C I_z(f)\), with one class-wide constant. Then
\[
 \boxed{H(f)\le K[I(f)-V(f)]\quad(f\in\mathcal F).}
\tag{4}
\]
Indeed, for every Boolean split, not just a monotone one,
\[
 V(f)-\tfrac12[V(f^+)+V(f^-)]=(\mathbb EB)^2,
\]
while the influence gap is \(\alpha\). Thus the exact \(I-V\) gap is
\(\nu\), and (3) inducts from the constant base case. If an irrelevant
coordinate is selected its gap is zero, and one can still reduce dimension.

This argument is stronger than deriving a class-wide strengthened inequality
from ordinary FEI alone: it explicitly uses the available local split
estimate for a coordinate at every restriction.

## Parallel-slab and formula consequence

The class of Boolean indicators/complements of one interval in a weighted
linear form is restriction-closed. The completed parallel-slab theorem
supplies a largest-weight local bound with universal \(C_{\rm slab}\).
Therefore (4) holds for every such gate with
\(K=\max\{2C_{\rm slab},14\}\).

For clarity, here is the exact balanced composition step. Let
\(F=g(f_1,\ldots,f_m)\), with balanced child functions on disjoint input
blocks, and suppose \(g\) and every child satisfy
\(H(h)\le K[I(h)-V(h)]\). Expand the outer Fourier polynomial and then
the child polynomials. Since a balanced child has zero empty coefficient,
each selected child spectral set is nonempty, and the final set uniquely
determines which blocks were selected. Conditional entropy and expected
degree give
\[
 H(F)=H(g)+\sum_iI_i(g)H(f_i),\qquad
 I(F)=\sum_iI_i(g)I(f_i),\qquad V(F)=V(g).
\]
The last identity uses independent uniform child outputs. Also
\(V(f_i)=1\) and \(\sum_iI_i(g)=I(g)\), so
\[
 H(F)\le K\left[I(g)-V(g)+\sum_iI_i(g)(I(f_i)-1)\right]
       =K[I(F)-V(F)].
\]
This is the established balanced FEI composition framework of
O'Donnell–Tan (2013), reproduced here to check the precise hypotheses.

Applying it from leaves to root gives the same \(I-V\) inequality, with no
constant inflation, for read-once formulas using arbitrary parallel-slab
gates, provided every nonroot output is balanced. Leaves have \(H=0\),
\(I=V=1\), beginning the induction. This includes halfspace gates and
allows arbitrary fan-in, depth, and size. The root may be biased.
Shared-input circuits and arbitrary biased child outputs are not covered.

The same generic conversion applies to the strict-separated \(m\)-crossing
class: its separation condition is preserved by restrictions, and its local
constant \(C_m\) gives \(K_m=\max\{2C_m,14\}\). Balanced read-once
composition applies to that gate family as well.

## Audit targets

Check \(|\mathbb EB|\le\alpha\) for signed derivatives, the empty-pair
entropy bound when \(\beta=0\), the \(\delta=0\) case \(f=zB\), and
the exact variance split without unateness. This does not establish full
Boolean FEI: the low-influence local premise is unknown in general and
fails for several prescribed coordinate rules.

The established composition source is Ryan O'Donnell and Li-Yang Tan,
*A composition theorem for the Fourier Entropy-Influence conjecture*,
ICALP 2013: <https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf>.
The local parallel-slab constant is supplied by the separately audited
parallel-slab proof; its primary halfspace inputs are Keller–Klein (2019),
Klivans–O'Donnell–Servedio (2004), and standard cube hypercontractivity.
No novelty or external peer review is certified for this continuation.
