# Universal split deficit and balanced composition of parallel-slab gates

Date: 2026-10-02. **Complete proof, internally audited; novelty unverified.**

This note proves a universal high-influence split inequality for signed
Boolean derivatives. It converts a local entropy–influence bound available
at every restriction into an entropy bound by total influence minus
variance. Applying the conversion to the internally audited parallel-slab
theorem yields the same bound for balanced read-once formulas of arbitrary
parallel-slab gates, with no dependence on their fan-in or the formula's
depth. Generic balanced composition is established by O'Donnell–Tan (2013)
and is credited below.

The [candidate](universal_split_deficit_and_slab_composition_candidate.md)
is preserved. The [independent analytic audit](universal_split_deficit_ant_audit.md)
and exhaustive numerical checks cover every Boolean function through four variables, including
signed derivatives with mean zero and influence one. These internal
checks are separate from external peer review and a novelty determination.

All inputs are independent uniform signs. Define
\[
 H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},\qquad
 I(f)=\sum_i\Pr[f(X)\ne f(X^{\oplus i})],\qquad
 V(f)=\operatorname{Var}(f).
\]
Here \(\widehat f(S)=\mathbb E[f\prod_{i\in S}X_i]\). Terms with zero
Fourier coefficient have value zero. For a split on
coordinate \(z\), write \(f^\pm=f(\cdot,\pm1)\) and
\(\Delta_zH(f)=H(f)-[H(f^+)+H(f^-)]/2\).

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

If the original local estimate \(\Delta_zH(f)\le C\alpha\), with
\(C\ge0\), holds and
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
\(\Delta H\le C I_z(f)\), with one class-wide constant \(C\ge0\). Then
\[
 \boxed{H(f)\le K[I(f)-V(f)]\quad(f\in\mathcal F).}
\tag{4}
\]
Indeed, for every Boolean split, not just a monotone one,
\[
 V(f)-\tfrac12[V(f^+)+V(f^-)]=(\mathbb EB)^2.
\]
The variance identity follows by writing the two restricted means as
\(\mathbb EA\pm\beta\). For every other coordinate, averaging its
influences in the two restrictions gives its original influence, while
the pivot influence is \(I_z(f)=\alpha\). Hence
\[
 I(f)-\tfrac12[I(f^+)+I(f^-)]=\alpha,
\]
and the exact \(I-V\) gap is \(\nu\).

Now induct on the number of input coordinates. A zero-dimensional Boolean
function is constant, so \(H=I=V=0\). For a nonconstant member choose
the hypothesized pivot. Its restrictions belong to the class and have
lower dimension. Their inductive bounds and (3) give
\[
\begin{aligned}
 H(f)
 &\le \tfrac K2\sum_{\sigma\in\{+,-\}}
       [I(f^\sigma)-V(f^\sigma)] + K\nu\\
 &=K[I(f)-V(f)].
\end{aligned}
\]
Constants in higher dimension satisfy the same bound directly. If an
irrelevant coordinate is selected, its gap is zero and the argument
still reduces dimension.

The derivation uses the available local split estimate for a coordinate
at every restriction; a class-wide ordinary FEI bound alone does not
provide this premise.

## Parallel-slab and formula consequence

The class of Boolean indicators/complements of one interval in a weighted
linear form is restriction-closed. The completed
[parallel-slab theorem](../2026-10-02-parallel-slabs/stripe_extension_parallel_slabs_proof.md)
supplies a largest-weight local bound with universal \(C_{\rm slab}\);
its explicit value is \(C_{\rm slab}=\max\{8,C_2\}\), with \(C_2\)
defined in the linked proof solely using absolute constants and the
Keller–Klein influence constant.
Therefore (4) holds for every such gate with
\(K=\max\{2C_{\rm slab},14\}\).

For clarity, here is the exact balanced composition step. Let
\(F=g(f_1,\ldots,f_m)\), with balanced child functions on disjoint input
blocks, and suppose \(g\) and every child satisfy
\(H(h)\le K[I(h)-V(h)]\). Expand the outer Fourier polynomial and then
the child polynomials. Since a balanced child has zero empty coefficient,
each selected child spectral set is nonempty, and the final set uniquely
determines which blocks were selected. More explicitly, for a set whose
nonempty block intersections are \(S_i\), \(i\in T\), its coefficient is
\[
 \widehat F\left(\bigcup_{i\in T}S_i\right)
 =\widehat g(T)\prod_{i\in T}\widehat f_i(S_i).
\]
Thus a random spectral set of \(F\) is generated by first drawing \(T\)
with probability \(\widehat g(T)^2\), and then, independently for each
\(i\in T\), drawing a nonempty \(S_i\) from the child spectral law.
The unique decomposition means its entropy is the entropy of \(T\)
plus the conditional child entropies. A block is selected with
probability \(\sum_{T\ni i}\widehat g(T)^2=I_i(g)\), and the expected
degree is the sum of the selected child degrees. These facts give
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
class in the [parallel-slab proof](../2026-10-02-parallel-slabs/stripe_extension_parallel_slabs_proof.md):
its retained points are actual sign jumps, their labels belong to the
adjacent intervals, and there are no extra isolated point anomalies.
Successive retained points have distance strictly greater than twice the
largest input weight. Restrictions translate the points and decrease the
largest remaining weight, preserving the condition. Its local constant
\(C_m\) therefore gives \(K_m=\max\{2C_m,14\}\). Balanced read-once
composition applies to that gate family as well.

## Scope and validation

The universal part proves (2) for every Boolean function, without
unateness. The full converted bound requires the specified local estimate
for a coordinate at every restriction. Ordinary FEI for a class alone
does not supply that premise. Full Boolean FEI is unresolved by this
argument; the low-influence premise remains unknown in general and fails
for several prescribed coordinate selection rules.

The [independent checker](independent_universal_split_check.py) and its
[results](independent_universal_split_checks.json) exhaust every Boolean
function through dimension four: 65,814 functions and 262,948 pivots.
Integer Walsh numerators verify the influence, variance, and budget
identities exactly. Entropy checks use double precision with tolerance
\(2\cdot10^{-11}\); they include 9,262 high-influence mean-zero signed
derivatives and 1,062 influence-one nonconstant signed derivatives.
The analytic argument, rather than finite enumeration, establishes the
dimension-independent theorem. The checker uses Python and NumPy and
has no local helper imports.

The established composition source is Ryan O'Donnell and Li-Yang Tan,
*A composition theorem for the Fourier Entropy-Influence conjecture*,
ICALP 2013: <https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf>.
The local parallel-slab constant is supplied by the separately audited
[parallel-slab proof](../2026-10-02-parallel-slabs/stripe_extension_parallel_slabs_proof.md); its primary halfspace inputs are Keller–Klein (2019),
Klivans–O'Donnell–Servedio (2004), and standard cube hypercontractivity.
No novelty or external peer review is certified for this continuation.
